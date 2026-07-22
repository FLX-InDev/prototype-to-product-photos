---
name: prototype-to-product-photos
description: Prototype product photo fidelity for generating high-end French e-commerce and editorial lifestyle images from original prototype images plus a factual product brief. Use when product category, semantic use, component construction, material behavior, and brand-appropriate French interiors must stay locked to the source product.
---

# Prototype To Product Photos

Use this skill to produce construction-locked, QA-passed identity-matched lifestyle photos from original prototype images. The source product stays authoritative; scene design exists only to present it.

## Required Inputs

Require both before generation:

1. **Original prototype image set:** one or more original-resolution images of the same SKU, motif, colorway, material, and construction.
2. **Short factual product description:** category, composition, function, allowed and forbidden placements, and any known dimensions or hidden construction facts.

Ask for the missing input before generating. Treat multiple images as one reference set only when they show the same product. Split different SKUs, colorways, materials, or designs into separate jobs.

Minimum description schema:

```text
Brand, if applicable:
Product category/name:
Material/composition:
Allowed uses or placements:
Forbidden uses or placements:
Optional dimensions:
Optional hidden construction or reversible-side facts:
```

## Source Authority

The original prototype set is the only authoritative product reference. Never use a generated image as product reference for a retry or new generation. Always restart from the original SKU prototype images.

Prototype images control visible product facts: color, pattern, motif, texture, material behavior, proportions, silhouette, folds, drape, compression, gravity behavior, hems, borders, flanges, piping, binding, cuffs, fringe, tassels, seams, labels, closures, hardware, and other visible construction.

The product description controls semantic facts: product category, material composition, function, allowed supports and placements, forbidden uses and placements, dimensions, and explicitly stated hidden construction facts.

If prototype images conflict with the description, or the description contradicts itself, stop and ask for clarification. If a construction-critical detail is unknown, request a close-up, keep the detail out of view, or use source-pixel same-state mode.

## Priority And Gates

Apply this priority order on every plan, prompt, retry, and delivery decision:

1. Correct product category and semantic use
2. Exact component inventory and construction topology
3. Product visual identity
4. Physically believable material behavior
5. Controlled lived-in styling
6. Premium French interior quality
7. E-commerce clarity

Use [references/fidelity-qa.md](references/fidelity-qa.md) as the single authoritative QA checklist. `Unclear` counts as failure. Reject every image that fails or leaves unclear any required gate.

## Required Workflow

1. Inspect the original prototype images at full resolution until product-bearing regions are separated from inserts, filler pillows, mattresses, headboards, furniture, decorative textiles, props, backgrounds, and reflections.
2. Build a product-region map that identifies which exact image regions control product color, trim, construction, inventory, and pattern.
3. Build the exact component inventory, with count, source region, visible construction, explicitly absent features, and `UNKNOWN` fields for unresolved facts.
4. Build the visual identity lock, construction topology lock, and semantic-use lock. The locks are complete only when every visible product-controlled attribute is recorded or marked `UNKNOWN`.
5. Read and apply the matching category section in [references/product-rules.md](references/product-rules.md). Stop if the planned support, placement, contact, fill, fold, drape, contents, safety, or scale is not approved.
6. Read [references/brand-layers.md](references/brand-layers.md). If the user specifies a brand, select exactly one matching user-defined brand layer. If no brand is specified, use the neutral/default layer. If the specified brand is missing or ambiguous, ask for clarification before generation. Brand layers control environment and mood only; they never change the product.
7. Choose the generation mode. Default to identity-locked lifestyle mode. Use source-pixel same-state mode only when the same viewpoint, silhouette, folds, drape, and source pixels must remain unchanged.
8. Plan controlled folds, compression, support contact, French interior setting, and photography grammar. The shot plan is complete only when it passes semantic-use lock and leaves construction landmarks readable.
9. Build the prompt from the locks and attach the complete original prototype set on every image-generation call.
10. Generate exactly one final image per image-generation call. For a requested series, make separate calls for separate shots, attach the original prototype set to every call, and inspect each result independently. Do not create contact sheets, collages, multi-panel layouts, or multiple shots inside one image unless the user explicitly requests them. For exploratory concept generation, the user may explicitly authorize batch generation. Batch generation is not suitable for final product-fidelity images and must not replace per-image QA.
11. Inspect the result against the five QA gates in this order: semantic use, component construction, visual identity and material behavior, lived-in styling, French interior and commerce quality.
12. Deliver only images that pass every gate. Retry failed images from the original prototype set, correcting one failure class at a time while preserving all product locks.

Do not lower the standard to fill a requested image count. After repeated construction drift, simplify overlap, use a source-adjacent viewpoint, switch to source-pixel same-state mode, or request another prototype view. When the product passes but the room fails, preserve all product locks and rebuild only the setting.

## Product Locks

### Product-Region Map

Inspect every prototype at full resolution. Non-product objects never control product color, trim, construction, inventory, or pattern.

### Component Construction Lock

Inventory every included component and count. Map each component separately; never transfer construction from one component or prop to another.

```text
Component and count:
Prototype image and exact region:
Main panel or body:
Edge stack from body to outermost edge:
Border, band, or flange placement and width ratio:
Binding, piping, welt, hem, cuff, or stitch placement:
Seam path and stitch-line position:
Corner treatment:
Front/back or reversible placement:
Opening, closure, tie, label, and hardware:
Explicitly absent features:
UNKNOWN construction details:
```

Distinguish constructions precisely: a border or band is a flat panel parallel to the edge; a flange extends flat beyond a seam; piping or welt is a narrow raised cord in a seam; binding wraps an edge; a hem or cuff is a folded finished section. Preserve feature count, color, material, relative width, seam path, continuity, corner shape, and placement.

### Visual Identity Lock

Record every visible product-controlled attribute: intrinsic color, pattern landmarks, surface character, softness or stiffness, weight, density, loft, thickness, proportions, silhouette, reversible faces, edge details, seams, labels, hardware, folds, drape, compression, and gravity behavior. Mark unresolved facts `UNKNOWN`.

### Semantic-Use Lock

Record from the description: category, composition, function, allowed supports and placements, forbidden uses and placements, permitted contact/fold/drape/fill/contents, dimensions, and safety or scale constraints.

Before each shot, verify internally:

```text
This product is a <category>.
It is made of <material>.
This image uses it on/in <approved support or context>.
It must not appear as <forbidden use>.
```

## Generation Modes

### Identity-Locked Lifestyle Mode

Use this by default for new lifestyle photos. Permit a new pose, orientation, fold, drape, or compression only when the semantic-use lock allows it. Preserve every identity and construction lock. Pose-dependent behavior must respond naturally to gravity and the approved support.

Call the result an **identity-matched lifestyle photo**, not a pixel-exact copy.

### Source-Pixel Same-State Mode

Use source-pixel compositing only when source viewpoint, silhouette, folds, drape, and pixels must remain unchanged. Permit only uniform scale, translation, canvas crop, background replacement, and an external contact shadow. Use [scripts/locked_composite.py](scripts/locked_composite.py) with a clean mask.

Call a result **exactly preserved** only when source pixels and pose remain unchanged and script provenance confirms the allowed transforms.

## Scene And Styling

Read [references/shot-recipes.md](references/shot-recipes.md) before selecting the setting and photography grammar.

For bedding, blankets, throws, cushions, and other soft goods, default to controlled lived-in styling: broad gravity-led folds, shallow soft creases, gentle compression, relaxed turn-downs, slight asymmetry, believable loft, clear silhouette, and enough unobstructed surface for material evaluation. Keep at least one locally front-facing defining edge segment readable in every construction-critical photo.

Use authentic French settings such as a Paris Haussmann apartment, hotel particulier, South-of-France limestone villa, Cote d'Azur modernist villa, Provence collector's home, refined wicker winter garden, dark-wood private residence, or luxury Mediterranean vacation residence. Medium or wide room images must include an authentic architectural anchor, substantial crafted furniture, layered premium natural materials, refined lighting, intentional window treatment or soft furnishing, curated art or objects, and controlled negative space that keeps the product dominant.

Make the product look luxurious through setting, styling, composition, and light only. Product-like props stay secondary and physically separate.

## Universal Image Rules

Unless the user specifies otherwise:

- use a 4:5 portrait composition;
- prioritize product fidelity over scene creativity;
- preserve intrinsic product color while allowing local highlights and shadows;
- ensure physically correct perspective, contact shadow, highlights, reflections, color temperature, brightness, saturation, and product-support contact;
- eliminate cutout edges, halos, inconsistent blur, floating contact, and compositing artifacts;
- add no unconfirmed text, logo, watermark, label wording, monogram, hardware, or decorative construction;
- show one complete described product unit or set with exact component count unless multiples are requested;
- generate one image per image-generation call.

Across a series, vary photography grammar rather than decoration alone. Include product-truth, lifestyle-use, and visible-detail views. Across the delivered set, show at least one verifiable view of each identity-defining edge, closure, reversible side, or other construction landmark visible in the prototypes.

## Prompt Template

Attach the complete original prototype set on every call and identify the images as views of the same product.

```text
Use case: product-mockup
Asset type: high-end French e-commerce lifestyle photo
Original input images: Images 1-N are the only appearance references for the same SKU; ignore all non-product regions.
Product description: <verbatim factual brief>
Brand layer: <selected user-defined brand layer | neutral/default>; apply only to environment and mood.
Semantic-use lock: <category, material, allowed use, forbidden use>.
Component inventory: <exact components and count>.
Construction topology lock: <per-component map and explicitly absent features>.
Visual identity lock: <color, pattern, surface, material behavior, proportions, silhouette, reversible sides, edges, seams, labels, hardware>.
Pose behavior: <only approved folds, drape, compression, and contact>.
Lived-in styling: <controlled styling that preserves construction landmarks>.
Setting: <approved French lane and authentic details>.
Photography grammar: <camera, angle, crop, product prominence, negative space>.
Lighting and integration: <material depth without global recoloring; physically correct integration; no cutout artifacts>
Constraints: one complete product/set, exact count, product-like props secondary and separate, no unconfirmed text/logo/watermark/label/hardware.
Avoid: category confusion, forbidden placement, construction substitution, altered identity, invented details, weak interiors, clutter, and CGI artifacts.
```

Repeat every applicable lock on every retry. Correct one failure class at a time, but always restart from the original prototypes.

## Honest Claims

- Call source-pixel same-state composites **exactly preserved** only when source pixels and pose remain unchanged.
- Call normal generated outputs **construction-locked, QA-passed identity-matched lifestyle photos** only after all five gates pass.
- Never claim pixel-exactness for a newly draped or repositioned product.
- Ask for more original prototype views or factual description when unseen identity details block reliable generation.
