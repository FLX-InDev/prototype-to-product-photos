#!/usr/bin/env python3
"""Composite unchanged product pixels over a generated background plate.

The product transform is limited to uniform scaling and translation. A separate
mask is required when the product image has no useful alpha channel. The script
writes a PNG plus a JSON provenance manifest beside it.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageCms, ImageFilter, ImageOps


def positive_float(value: str) -> float:
    parsed = float(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def unit_float(value: str) -> float:
    parsed = float(value)
    if not 0 <= parsed <= 1:
        raise argparse.ArgumentTypeError("must be between 0 and 1")
    return parsed


def byte_value(value: str) -> int:
    parsed = int(value)
    if not 0 <= parsed <= 255:
        raise argparse.ArgumentTypeError("must be between 0 and 255")
    return parsed


def parse_canvas(value: str) -> tuple[int, int]:
    try:
        width_text, height_text = value.lower().split("x", 1)
        width, height = int(width_text), int(height_text)
    except (ValueError, AttributeError) as exc:
        raise argparse.ArgumentTypeError("use WIDTHxHEIGHT, for example 2048x2560") from exc
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("canvas dimensions must be positive")
    return width, height


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fit_cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_width, target_height = size
    scale = max(target_width / image.width, target_height / image.height)
    resized = image.resize(
        (round(image.width * scale), round(image.height * scale)),
        Image.Resampling.LANCZOS,
    )
    left = (resized.width - target_width) // 2
    top = (resized.height - target_height) // 2
    return resized.crop((left, top, left + target_width, top + target_height))


def checked_srgb_profile(image: Image.Image, path: Path) -> tuple[bytes | None, str]:
    profile_bytes = image.info.get("icc_profile")
    if not profile_bytes:
        return None, "assumed sRGB (no embedded ICC profile)"

    try:
        profile = ImageCms.ImageCmsProfile(BytesIO(profile_bytes))
        profile_name = ImageCms.getProfileName(profile).strip()
    except Exception as exc:
        raise ValueError(f"cannot read ICC profile in {path}: {exc}") from exc

    if "srgb" not in profile_name.lower():
        raise ValueError(
            f"{path} uses non-sRGB profile '{profile_name}'; convert a controlled copy to sRGB first"
        )
    return profile_bytes, profile_name


def load_product_and_mask(
    product_path: Path, mask_path: Path | None
) -> tuple[Image.Image, Image.Image, bytes | None, str]:
    source_file = Image.open(product_path)
    profile_bytes, profile_name = checked_srgb_profile(source_file, product_path)
    source = ImageOps.exif_transpose(source_file).convert("RGBA")

    if mask_path:
        mask = ImageOps.exif_transpose(Image.open(mask_path)).convert("L")
        if mask.size != source.size:
            raise ValueError(
                f"mask size {mask.size} does not match product size {source.size}"
            )
    else:
        mask = source.getchannel("A")
        extrema = mask.getextrema()
        if extrema == (255, 255):
            raise ValueError("product has no transparency; provide --mask")

    bbox = mask.getbbox()
    if bbox is None:
        raise ValueError("mask is empty")

    source = source.crop(bbox)
    mask = mask.crop(bbox)
    source.putalpha(mask)
    return source, mask, profile_bytes, profile_name


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Pixel-lock a prototype over an empty generated background plate."
    )
    parser.add_argument("--product", required=True, type=Path, help="sole prototype image")
    parser.add_argument("--mask", type=Path, help="grayscale mask aligned to the prototype")
    parser.add_argument("--background", required=True, type=Path, help="empty background plate")
    parser.add_argument("--out", required=True, type=Path, help="output PNG path")
    parser.add_argument("--canvas", type=parse_canvas, help="output WIDTHxHEIGHT; defaults to plate size")

    size_group = parser.add_mutually_exclusive_group()
    size_group.add_argument("--scale", type=positive_float, help="uniform product scale; 1 keeps source size")
    size_group.add_argument(
        "--height-ratio",
        type=positive_float,
        default=0.72,
        help="product height divided by canvas height; default 0.72",
    )

    parser.add_argument("--x", type=unit_float, default=0.5, help="normalized product center; default 0.5")
    parser.add_argument(
        "--bottom", type=unit_float, default=0.92, help="normalized product bottom anchor; default 0.92"
    )
    parser.add_argument("--shadow-opacity", type=byte_value, default=36)
    parser.add_argument("--shadow-blur", type=positive_float, default=22.0)
    parser.add_argument("--shadow-offset-x", type=int, default=0)
    parser.add_argument("--shadow-offset-y", type=int, default=10)
    return parser


def main() -> int:
    args = build_parser().parse_args()

    if args.out.suffix.lower() != ".png":
        raise ValueError("--out must end in .png to avoid lossy product changes")

    for path in (args.product, args.background, args.mask):
        if path is not None and not path.is_file():
            raise FileNotFoundError(path)

    background_file = Image.open(args.background)
    background_profile_bytes, background_profile_name = checked_srgb_profile(
        background_file, args.background
    )
    background_source = ImageOps.exif_transpose(background_file).convert("RGBA")
    canvas_size = args.canvas or background_source.size
    canvas = fit_cover(background_source, canvas_size)
    product, product_mask, product_profile_bytes, product_profile_name = load_product_and_mask(
        args.product, args.mask
    )

    if args.scale is not None:
        scale = args.scale
    else:
        scale = (canvas.height * args.height_ratio) / product.height

    resized_size = (max(1, round(product.width * scale)), max(1, round(product.height * scale)))
    product = product.resize(resized_size, Image.Resampling.LANCZOS)
    product_mask = product_mask.resize(resized_size, Image.Resampling.LANCZOS)
    product.putalpha(product_mask)

    left = round(canvas.width * args.x - product.width / 2)
    top = round(canvas.height * args.bottom - product.height)
    if left < 0 or top < 0 or left + product.width > canvas.width or top + product.height > canvas.height:
        raise ValueError("placed product falls outside the canvas; adjust scale, x, or bottom")

    shadow_alpha = Image.new("L", canvas.size, 0)
    shadow_left = left + args.shadow_offset_x
    shadow_top = top + args.shadow_offset_y
    shadow_alpha.paste(product_mask, (shadow_left, shadow_top))
    shadow_alpha = shadow_alpha.filter(ImageFilter.GaussianBlur(args.shadow_blur))
    shadow_alpha = shadow_alpha.point(lambda value: round(value * args.shadow_opacity / 255))
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow.putalpha(shadow_alpha)

    composed = Image.alpha_composite(canvas, shadow)
    product_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    product_layer.alpha_composite(product, dest=(left, top))
    composed = Image.alpha_composite(composed, product_layer)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    output_profile_bytes = product_profile_bytes or background_profile_bytes
    save_options: dict[str, object] = {"format": "PNG", "optimize": True}
    if output_profile_bytes:
        save_options["icc_profile"] = output_profile_bytes
    composed.convert("RGB").save(args.out, **save_options)

    manifest_path = args.out.with_suffix(args.out.suffix + ".manifest.json")
    manifest = {
        "mode": "pixel-locked-composite",
        "source_product": str(args.product.resolve()),
        "source_product_sha256": sha256_file(args.product),
        "source_mask": str(args.mask.resolve()) if args.mask else "embedded alpha",
        "source_mask_sha256": sha256_file(args.mask) if args.mask else None,
        "background": str(args.background.resolve()),
        "background_sha256": sha256_file(args.background),
        "output": str(args.out.resolve()),
        "output_sha256": sha256_file(args.out),
        "canvas": {"width": canvas.width, "height": canvas.height},
        "color_management": {
            "product_profile": product_profile_name,
            "background_profile": background_profile_name,
            "output_profile": "embedded sRGB" if output_profile_bytes else "assumed sRGB",
        },
        "transform": {
            "uniform_scale": scale,
            "left": left,
            "top": top,
            "resampling": "Lanczos",
            "perspective_warp": False,
            "rotation": 0,
            "mirrored": False,
        },
        "shadow": {
            "opacity": args.shadow_opacity,
            "blur": args.shadow_blur,
            "offset_x": args.shadow_offset_x,
            "offset_y": args.shadow_offset_y,
            "placement": "behind product layer",
        },
    }
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {args.out}")
    print(f"Wrote {manifest_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # concise CLI error without a traceback by default
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
