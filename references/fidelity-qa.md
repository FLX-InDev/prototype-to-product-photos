# Product fidelity and acceptance QA

Use only the original SKU prototype set for every comparison and retry. Never compare a new candidate against a previously generated image as product authority.

## Input and authority manifest

```text
Original prototype files:
Same product/SKU/colorway confirmed:
Brand, if specified:
Product category/name:
Material/composition:
Allowed uses or placements:
Forbidden uses or placements:
Dimensions:
Explicit hidden construction facts:
Prototype-description conflicts:
Unknowns requiring clarification or concealment:
```

Stop and clarify when a required input is missing, a prototype and description conflict, or an unknown construction-critical detail cannot be kept out of view.

## Product-region and component manifest

```text
Prototype image and product-bearing region:
Excluded insert/furniture/prop/background regions:
Component name and count:
Main body/panel:
Edge stack:
Border/band/flange:
Piping/welt/binding/hem/cuff:
Seam and stitch path:
Corner treatment:
Front/back/reversible side:
Opening/closure/tie/label/hardware:
Explicitly absent features:
UNKNOWN construction details:
```

Create one component block for every included part. Never borrow construction from a different component or from excluded non-product regions.

## Visual identity manifest

```text
Intrinsic color and tonal boundaries:
Pattern, repeat, scale, direction, landmarks, reversible layout:
Material and finish:
Texture, weave/knit, nap/pile, grain, gloss, translucency:
Softness, fluidity/stiffness, weight, density, loft, thickness:
Overall and part-to-part proportions:
Silhouette and scale cues:
Folds, drape, compression, gravity behavior:
Visible construction landmarks:
Labels/text/hardware confirmed from source:
UNKNOWN visual details:
```

Do not guess fiber, finish, dimension, color code, label wording, hardware, or hidden construction. Use the description for factual composition and function; use prototypes for appearance and visible construction.

## Gate 1 — semantic use

Reject if any answer is `no` or `unclear`:

1. Does the object remain the described category and function?
2. Is every visible component present in the exact requested count?
3. Does the scene use only an approved support, contact, placement, and room context?
4. Are all forbidden uses and placements absent?
5. Is product-support contact physically plausible for the material and function?
6. Is scale plausible or supported by supplied dimensions?
7. Is the product visibly removable from furniture unless described as upholstery?
8. Are props clearly different product categories, secondary, and physically separate?

For blankets, require that they are off the floor and unmistakably used as removable blankets unless floor contact or another use is explicitly allowed.

## Gate 2 — component construction topology

Reject if any answer is `no` or `unclear`:

1. Does the component inventory and count match exactly?
2. Does every component match its corresponding original prototype region independently?
3. Do edge type, layer count, feature count, relative width, color, material, seam path, stitch position, continuity, corner treatment, reversible placement, opening, closure, tie, label, and hardware match?
4. Are explicitly absent features still absent?
5. Has no border, band, flange, piping, welt, binding, hem, cuff, seam, stitch, label, closure, tie, or hardware been added, removed, duplicated, simplified, widened, narrowed, recolored, relocated, interrupted, or converted?
6. Has no construction been borrowed from another component, insert, furniture item, or prop?
7. Are folds and overlaps structurally possible, without impossible trim crossing or topology changes?
8. Is every construction-critical detail sufficiently visible, sharp, lit, and front-facing to verify?

For a double-layer overlocked or serged edge, confirm both layers where visible. Natural closing or separation is allowed; simplification into one generic edge is not.

## Gate 3 — visual identity and material behavior

Reject if any answer is `no` or `unclear`:

1. Do intrinsic color, tonal boundaries, pattern, scale, direction, repeat, landmarks, and reversible layout match?
2. Do texture, weave, knit, nap, pile, grain, gloss, and translucency match?
3. Do softness or stiffness, weight, density, thickness, loft, folds, drape, compression, and gravity behavior match?
4. Do overall proportions, silhouette, part-to-part ratios, and scale remain plausible?
5. Are all visible edge details, seams, labels, closures, and hardware source-confirmed?
6. Is product color globally unchanged, with only physically plausible local highlight and shadow variation?
7. Is perspective, contact shadow, highlight direction, reflection, color temperature, brightness, saturation, depth of field, grain, and edge sharpness coherent with the room?
8. Is the product free of cutout edges, halos, floating contact, inconsistent blur, compositing seams, and CGI artifacts?

For source-pixel same-state mode, additionally require identical source pixels, pose, folds, silhouette, and orientation, with only documented uniform scale, translation, crop, background replacement, and external contact shadow.

## Gate 4 — controlled lived-in styling

Reject if any answer is `no` or `unclear`:

1. Do soft goods show believable broad folds, shallow creases, soft compression, relaxed turn-downs, slight asymmetry, or natural loft as appropriate?
2. Is the styling relaxed and inviting rather than vacuum-flat, over-smoothed, rigid, generic-hotel, tangled, crushed, collapsed, or carelessly unmade?
3. Do folds remain consistent with prototype weight, thickness, softness, density, and construction?
4. Does the product retain a readable silhouette and enough clear surface for material evaluation?
5. Is at least one defining edge or construction landmark verifiable in every construction-critical image?

## Gate 5 — premium decorated interior and commerce quality

Reject if any answer is `no` or `unclear`:

1. Is the selected French setting authentic and immediately legible?
2. Does a medium or wide room coherently include architecture, substantial crafted furniture, layered premium natural materials, refined lighting, intentional window treatment or soft furnishing, curated art/objects, and controlled negative space?
3. Does a detail frame retain at least three legible premium-interior cues without competing with the product?
4. Does the room feel collected, residential, professionally decorated, and affluent rather than anonymous, sparse, generic, rental-like, or showroom-like?
5. Are anonymous beige styling, cheap or flat-pack furniture, poor hardware, generic hotels, fake-palace ornament, random luxury props, decorative clutter, competing textiles, and glossy CGI absent?
6. Is the product dominant, sharply readable, usefully cropped, and commercially clear?
7. Does the frame follow exactly one selected brand layer, or the neutral/default layer, without blending unrelated brand languages or altering the product?

## Product-specific mandatory checks

Apply every relevant section in [product-rules.md](product-rules.md), including:

- bedding remains on a bed and keeps component-specific construction;
- blankets never become rugs, runners, carpets, floor coverings, upholstery, curtains, tablecloths, wall hangings, or slipcovers unless explicitly allowed;
- cushions keep exact requested inventory, count, shape, and dimensions;
- tray/vase/stone/branch compositions keep the permitted one-of inventory and forbidden-prop list;
- silk eye masks pass the two-independent-ear-loop geometry test;
- silk scrunchies keep specified size and momme relationships.

## Weighted review after all hard gates pass

| Criterion | Points |
|---|---:|
| Correct category, inventory, support, and semantic use | 25 |
| Exact component construction topology | 20 |
| Color, pattern, design, and proportions | 15 |
| Texture, material behavior, and physical integration | 15 |
| Controlled lived-in styling | 10 |
| Premium French interior and brand fit | 10 |
| E-commerce usability | 5 |

Require at least 95/100 and no hard-gate failure. A high score never overrides a failed or unclear gate.

## Required comparison sequence

1. Compare category and semantic use.
2. Compare exact component inventory and every component's construction.
3. Compare color, pattern, material, texture, proportions, and physical behavior.
4. Compare controlled lived-in styling.
5. Compare interior quality, selected brand layer, and e-commerce composition.
6. Record pass/fail/unclear and one correction target.

## Retry decision table

| Failure | Required action |
|---|---|
| Missing product description or original prototype | Stop and request it. |
| Prototype conflicts with description or itself | Stop and ask which fact is correct; never choose silently. |
| Construction-critical detail is unknown | Request a close-up, hide it, or use source-pixel same-state mode. |
| Blanket becomes a rug, runner, carpet, floor covering, upholstery, curtain, tablecloth, wall hanging, or slipcover | Reject; restate category, approved support, removability, forbidden use, and floor-contact rule. |
| Inventory, edge, trim, closure, pattern, color, texture, thickness, or material behavior drifts | Reject; restart from the original prototypes, restate the affected lock, and simplify pose or overlap. |
| Product integrates poorly with the room | Reject; correct perspective, contact, lighting, reflection, blur, color management, and edge artifacts without changing the product. |
| Styling is too smooth or too messy | Change only folds, compression, asymmetry, and landmark visibility. |
| Product passes but room is generic | Preserve every product lock; rebuild only the setting. |
| Room is luxurious but any product gate fails | Reject. Room quality never compensates. |
| Repeated drift | Choose a simpler approved placement and source-adjacent viewpoint, use source-pixel same-state mode, or request another original prototype view. |

Never retry from a generated candidate. Replace every failed or unclear image before delivery.
