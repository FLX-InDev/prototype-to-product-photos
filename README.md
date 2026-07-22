# Prototype To Product Photos

A Codex skill for turning original prototype images into high-fidelity product lifestyle photos while preserving product category, semantic use, component construction, material behavior, and source-controlled visual identity.

The skill is designed for products where visual drift is costly: bedding, blankets, cushions, tableware, decorative objects, home decor, silk accessories, and other SKU-specific products that must remain faithful to a prototype image set.

## What It Does

- Requires original prototype images plus a factual product brief before generation.
- Separates product-bearing regions from props, inserts, furniture, and backgrounds.
- Builds source-locked product, construction, visual identity, and semantic-use locks.
- Uses category rules and QA gates before scene design.
- Supports optional user-defined brand layers for repeatable art direction.
- Produces one QA-inspected image per generation call.
- Uses source-pixel same-state compositing when a product pose must remain exactly preserved.

## Repository Structure

```text
prototype-to-product-photos/
  SKILL.md
  README.md
  LICENSE
  agents/
    openai.yaml
  references/
    brand-layers.md
    fidelity-qa.md
    product-rules.md
    shot-recipes.md
  scripts/
    locked_composite.py
```

## Required Inputs

Use the skill with both:

1. One or more original-resolution prototype images of the same SKU, colorway, material, and construction.
2. A short factual product description with category, composition, function, allowed and forbidden placements, dimensions if known, and hidden construction facts if relevant.

Suggested brief:

```text
Brand, if applicable:
Product category/name:
Material/composition:
Allowed uses or placements:
Forbidden uses or placements:
Optional dimensions:
Optional hidden construction or reversible-side facts:
```

## Brand Layers

Brand layers are user-configurable. Edit `references/brand-layers.md` to define one or more brands, aliases, moods, approved settings, palette relationships, props, photography grammar, and treatments to avoid.

If a user specifies a brand during a conversation, the skill uses exactly one matching brand layer. If no brand is specified, it uses `Neutral / default`. Brand layers affect scene design only; they never override the product locks.

## Installation

Install from GitHub with Codex's skill installer:

```powershell
python <path-to-codex-home>/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo FLX-InDev/prototype-to-product-photos --path .
```

## Example Request

```text
Use $prototype-to-product-photos with these original prototype images.

Product category/name: quilted cotton bed cover
Material/composition: cotton shell, medium loft fill
Allowed uses or placements: on a bed, folded at foot of bed, draped over bedding
Forbidden uses or placements: rug, upholstery, wall hanging
Optional dimensions: 240 x 260 cm
Brand, if applicable: Neutral / default
```

## Publishing Checklist

Before publishing your fork or copy:

- Remove private product images and customer files.
- Remove private brand names or replace them with generic brand layer examples.
- Check for API keys, tokens, emails, and local absolute paths.
- Keep Markdown and YAML files as UTF-8 without BOM.
- Test links from `SKILL.md` to files under `references/` and `scripts/`.

## License

MIT License. See [LICENSE](LICENSE).
