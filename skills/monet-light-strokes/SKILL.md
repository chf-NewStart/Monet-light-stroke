---
name: monet-light-strokes
description: Transform photos or generate original scenes with luminous Claude Monet-inspired Impressionist atmosphere, painting-first abstraction, coarse irregular broken-color brushwork, colored shadows, reflective water, softened architecture, and rhythmic foliage. Use for image style transfers, profile pictures, portraits, landscapes, gardens, seascapes, river towns, posters, or illustrations when the user asks for Monet, French Impressionism, painterly light, visibly loaded oil strokes, or water-lily color fields. Preserve identity, pose, outfit, subject count, props, recognizable surroundings, aspect ratio, and complete visible bodies unless the user explicitly requests changes or cropping.
---

# Monet Light & Strokes

Create an original Impressionist interpretation in which light and atmosphere organize the scene. Synthesize the shared visual grammar across the references; never reproduce a particular painting's composition, exact palette, or signature.

Read [references/style-system.md](references/style-system.md) before writing the final generation or edit prompt. Read [references/benchmarks.md](references/benchmarks.md) when an approved benchmark should guide a new result, and use its image only for paint behavior—not scene content. Treat B010 as the primary general benchmark for light-defined form; use the other positive benchmarks only for their stated materials or conditions. For daylight architecture wrapped in flowering foliage, pair B010 with B014 and transfer from B014 only its description scale, edge loss, foliage massing, and chromatic-shadow behavior. Use the image-generation tool for raster output.

Return the artwork only. Do not add or offer frames, mats, walls, glass, labels, or museum-style presentation mockups. Physical presentation is intentionally outside this skill's scope because it requires separate composition, scale, and shared-lighting control.

## Establish the Contract

Determine the operation from the request:

- **Style transfer:** treat the source image as factual authority for people, pose, clothing, objects, setting, framing, aspect ratio, displayed orientation, and left/right spatial order. Never mirror, flip, rotate, transpose, or swap sides unless the user explicitly requests it. Do not treat its pixel-level texture, tiny edges, individual ripples, or exact tonal map as invariants; reconstruct those through paint.
- **Original scene:** treat the user's scene description as factual authority, then invent a fresh composition.
- **Profile picture:** default to square, but keep the complete visible figure inside the canvas. Do not turn a full-body source into a headshot.
- **Series:** keep the subject, viewpoint, crop, and overall stroke grammar recognizable while deliberately varying time of day, weather, season, and light key. Never reuse one visible texture pattern across the series.

If the request is sufficiently specified, generate directly. Ask only when an unresolved choice would materially change the result.

## Build the Image

1. **Inventory invariants.** List internally what must not change: subject count, identities, pose, full-body extent, outfit, props, setting landmarks, camera angle, crop, displayed orientation, and left/right anchor order. For an asymmetric scene, write two or more concrete spatial anchors such as “the illuminated house occupies the right third” or “the stairs rise from lower center toward upper right.”
2. **Choose an atmospheric key.** Select a coherent time of day, weather, season, and dominant temperature from the source or request. Light is the main structural device.
3. **Map and simplify large masses.** Squint or mentally blur the source, reduce it to roughly five to nine dominant value-color zones, and merge minor repeated detail into those zones. Establish sky, ground or water, foliage, architecture, and figures from these connected masses before adding selective detail. Budget descriptive resolution: broad masses must remain the first read, medium strokes may explain their movement, and small marks may only punctuate a few focal sites.
4. **Route and layer strokes by material, state, distance, and scale.** Default to medium-to-broad, coarse, irregular marks that remain visible at normal viewing size. Build visible temporal depth from underpainting, scumbled masses, broken descriptive strokes, selective opaque accents, and partial revisions. Distinguish calm reflective water from choppy open sea instead of using one generic water texture. Treat broken color as neighboring pigment notes, not permission to tessellate the canvas with one repeated dab or palette-knife footprint. Aim for chaotic yet structured paint: local marks may be restless and surprising while the large value masses, silhouettes, light direction, and material boundaries remain stable. Introduce controlled hand-made variation inside each material's directional logic, then reduce edge certainty, contrast, and mark count with distance. Reconstruct forms with paint rather than tracing the source's micro-edges. Follow the stroke routing in the reference.
5. **Write the generation prompt.** State preservation requirements first, painterly transformation second, exclusions last.
6. **Generate and inspect.** Check the complete image rather than accepting an attractive detail crop. Run both the factual-preservation check and the mark-family check before judging color or mood.
7. **Reject and retry once when needed.** A mirrored composition, missing subject, or canvas-wide repeated brush footprint is a failed edit even when attractive. Retry from the original source with one concrete correction, such as “replace the repeated diagonal lozenge texture with broad quiet sky scumbles, planar architectural strokes, and dragged granular ground clusters.” Do not return a result that still fails a non-negotiable.

## Prompt Priorities

Use this order in edit prompts:

1. Preserve the source composition, displayed orientation, left/right spatial order, complete visible body, face, pose, outfit, props, and surroundings. Explicitly forbid mirroring, flipping, rotation, transposition, and side-swapping.
2. Keep the original aspect ratio unless the user requests another format.
3. Repaint the scene through luminous outdoor atmosphere and broken-color oil strokes.
4. Specify the material-dependent stroke behavior and chosen light key.
5. Exclude hard outlines, smooth digital gradients, muddy black shadows, plastic skin, photographic sharpness, text, frames, presentation mockups, and signatures.

Do not use “in the style of Monet” as the entire prompt. Translate the desired look into observable decisions about light, palette, edges, and strokes.

## Non-Negotiables

- Preserve full-body framing when a body is fully visible in the source. Keep head, hands, legs, and shoes inside the canvas with breathing room.
- Preserve the source exactly as displayed after metadata orientation is applied. Never mirror horizontally or vertically, rotate, transpose, reverse a subject's facing direction, reverse the direction of stairs or paths, or move distinctive landmarks to the opposite side unless the user explicitly asks.
- Preserve facial identity and expression while simplifying features into painterly planes.
- Keep shadows chromatic: blue, violet, green, rose, or warm gray instead of flat black.
- Preserve recognizable source color identities where they carry factual meaning, especially skin, clothing, and key props, but tune hue, temperature, and chroma within those identities to express the atmospheric light. Treat literal sampled color as a starting point rather than a ceiling.
- Create luminosity relationally. Use a few clear, saturated pigment notes beside quieter grays and deeper chromatic shadows; do not brighten the painting by mixing the same opaque white into every sky, wall, leaf, flower, and shadow color. Bright is not synonymous with pastel.
- Preserve a source-appropriate value span and enough deep cobalt, indigo, violet, blue-green, crimson, olive, or violet-brown anchors to make selected light appear radiant. Keep those darks colorful rather than black, and do not force dramatic contrast onto a genuinely misty high-key source.
- When the source uses a dark focal silhouette to organize the composition, preserve that subject as one of the deepest chromatic value anchors. Atmospheric color may enter its edges and a few interior planes, but must not lift its core into the surrounding middle-value field or weaken the source's focal contrast. Keep it dark through indigo, cobalt, violet-brown, blue-green, or olive rather than flat black.
- Build an atmospheric envelope by recurring sky, ground, foliage, and reflected-light colors across material boundaries at altered value and intensity. Let ambient sky color enter architectural and foliage shadows and let nearby reflected color interrupt selected edges; avoid both thin cutout clarity and a uniform milky haze.
- Define silhouettes and contours through neighboring shifts of value, temperature, and reflected color rather than heavy black outlines. Let light cross selected edges, not every contour; retain a few decisive edges and a deep chromatic core where the source needs a visual anchor.
- Use adjacent broken colors that mix optically; avoid globally blended or airbrushed surfaces.
- Build the paint surface from fewer broad and medium overlapping strokes with selective thick accents. Avoid covering the image in tiny, uniformly distributed mosaic marks.
- Interpret broken color as color separation inside a hierarchy of broad fields, medium descriptive strokes, and sparse small accents. “More dabs” must never become one repeated mark shape, size, angle, or spacing across the canvas.
- Reject dense short crystallized ridges, cell-like impasto networks, and equal heavy relief across a passage. Optical mixing requires unequal neighboring color marks plus varied thin, scumbled, soft-edged, and selectively thick paint—not one embossed texture.
- Keep each material's dominant brush footprint visibly different. Never cover sky, ground, architecture, foliage, water, or figures with the same diagonal lozenges, rectangular facets, leaf stamps, or palette-knife tiles.
- Allow a recurring rhythm inside one material when its marks vary substantially in scale, angle, overlap, loading, edge, spacing, and color and remain subordinate to a clear large-scale structure. Do not reject a bold active passage merely because it is coarse or energetic.
- Preserve the factual skeleton, not the photographic microtexture. Keep the crop, subject silhouettes, identities, pose, landmarks, major value bands, and light direction, but simplify, merge, omit, and repaint minor ripples, leaves, texture, and incidental edges.
- Apply mass before parts and atmosphere before drafting. Preserve a building's placement, silhouette, roof pitch, openings, and landmark geometry, but reconstruct siding, gutters, window frames, trim, shingles, and other repeated construction detail as a few interrupted planar strokes. Let sunlight, humidity, reflected color, foliage, and air break or consume secondary architectural edges.
- Make light and color carry form. If a subject remains legible mainly because of continuous contour, perspective drafting, or interior construction lines, repaint it through adjacent value-temperature fields, lost-and-found edges, and atmospheric overlap while preserving its factual silhouette.
- Build foliage and flowers as connected color masses before adding comma strokes, hooks, flicks, and accents. Use broad and medium overlapping marks to suggest collective growth and movement; never translate every leaf, petal, blossom, or midground tree into a separate dot or identical short mark.
- Allow mark-level randomness in angle, spacing, pressure, length, opacity, temperature, overlap, and edge quality. Keep scene-level facts—composition, identity, anatomy, object count, light direction, and reflection placement—strictly fixed.
- Soften distant forms with lower contrast, cooler color, and fewer marks.
- Let reflections echo objects as broken vertical color paths interrupted by the surface's actual water-state gestures: mostly horizontal ripples in calm passages, more oblique or rolling cuts in turbulent passages.
- Use dark accents sparingly for eyes, boats, branches, windows, or figure anchors; avoid ink-like contouring.
- Produce an original result. Do not add Monet's signature, labels, watermarks, copied arrangements from a reference painting, frames, mats, walls, or presentation objects.

## Quality Check

Before returning the image, verify:

- The requested subject and source composition remain recognizable.
- The displayed orientation and left/right order match the source. Compare at least two asymmetric anchors—such as landmark side, staircase or path direction, subject-facing direction, light placement, or object order—and reject the result immediately if any global mirror, flip, rotation, or side swap occurred.
- No person or important prop has been cropped, invented, removed, or duplicated.
- The light condition is coherent across sky, subject, ground, and reflections.
- Stroke direction changes with the material instead of becoming one generic texture.
- The dominant stroke family fits both material and physical state: upward comma-like flicks for foliage and grass; broken horizontal dashes for calm reflective water; rolling, oblique, diagonal, hooked, or forceful strokes for swelling and breaking sea; selectively crusted clumps for rough solid masonry or cliffs; and scumbled or softly swirling joins for cloud, steam, and fog. Vary each family internally; never turn it into a repeated stamp.
- The material-transfer test passes: a representative patch of sky, ground, foliage, water, masonry, or cactus marks would look visibly wrong if transplanted unchanged onto another material. If several passages seem interchangeable, reroute their direction, scale, loading, density, edges, and layering.
- The mark-family audit passes: compare the largest sky, ground, and subject or architecture regions. Reject the image if substantially the same combined fingerprint of brush silhouette, angle, size band, edge character, loading, and texture density migrates unchanged across two or more materials, especially as mechanical diagonal lozenges or interlocking facets. Do not reject material-specific rhythmic recurrence that varies visibly and supports the form.
- Dominant strokes remain clearly visible at normal viewing size and vary in width, length, loading, and edge quality.
- The ridge test passes: the surface does not resolve into a dense network of similarly raised, hard-edged, short crystalline marks before it reads as broken color and depicted form.
- Broad connected or thinly scumbled quieter passages remain perceptible beside active broken-color clusters. Quiet may mean lower contrast, thinner loading, softer burial, or slower rhythm rather than a smooth or empty surface. Reject only nearly equal activity and density from edge to edge.
- The chaotic-yet-structured test passes: close inspection reveals irregular, partly revised, non-mechanical marks; thumbnail inspection reveals a stable arrangement of roughly five to nine masses, coherent light, readable silhouettes, and intact source facts.
- Repeated marks feel hand placed rather than stamped: clusters, pauses, imperfect overlaps, and occasional corrective or off-color strokes remain visible without damaging legibility.
- When blurred or viewed as a thumbnail, the image is organized by a small number of clear color-value masses rather than a traced photographic tonal map.
- The description-scale audit passes: the first read is large light, air, foliage, ground, water, and architectural masses—not siding boards, gutters, window mullions, individual leaves, blossoms, stones, or ripples. Reject a factually accurate image when its descriptive granularity remains uniformly fine.
- The light-defined-form test passes: mentally remove secondary contour and construction lines. The scene must remain readable through neighboring color-value masses, light direction, chromatic edges, and atmospheric overlap. If the house, boat, tree, or figure collapses without its drawing, the painting is still illustration-led.
- Architecture retains enough broken planar anchors to stay recognizable, but no long secondary contour is ruler-clean. Light and atmosphere interrupt trim, siding, gutter, roof, and window edges without changing the building's factual silhouette or orientation.
- Foliage reads first as overlapping tree, shrub, or forest masses and only later as selective comma-like growth marks. Reject pointillist blossom fields, stippled midground carpets, thousands of isolated leaf or tree dots, and equal tiny marks across foreground and distance.
- Most photographic micro-edges and local texture are gone. Only a few focal edges remain; secondary edges merge, break, or dissolve into adjacent paint.
- Water has a continuous painted body beneath its surface gestures. Calm water uses unequal broken horizontal marks; choppy or breaking sea follows the wave forms with rolling arcs, oblique or diagonal slashes, hooks, turning crests, and dragged foam. Reject neat parallel ribbons, state-blind universal marks, random canvas-wide crosshatching, and interlocking rectangular color slabs.
- The paint surface reveals multiple passes: thin ground, partly covered scumbles, varied broken middle strokes, and a few opaque accents. It does not look uniformly rendered in one digital pass.
- Painterly secondary passages remain visibly coarse, approximate, and worked. Do not automatically clean an expressive sky, sand, ground, or foliage field into smoother, more precise illustration.
- Do not self-correct a user-approved bold passage into smoother realism. When an approved benchmark and a cleaner revision conflict, preserve the benchmark's mark separation, optical vibration, and chromatic shadow behavior unless the user requests otherwise.
- Close forms have richer contrast and thicker marks; distant forms dissolve into atmosphere.
- Edge sharpness, local contrast, and mark count fall with distance. Reject scenes in which foreground leaves, middle-ground house details, and distant rooflines all appear equally focused and exhaustively described.
- Warm and cool notes vibrate without becoming neon or muddy brown.
- Apparent brightness comes from selective clear color beside quieter grays and chromatic shadows, not from raising exposure or saturation across the whole image.
- The focal-value test passes: a source-defining dark bird, figure, boat, trunk, or architectural anchor remains decisively lower in value than its immediate light field. It may retain broken chromatic paint and lost edges, but it must not dissolve into equal-value atmosphere or require outlines to recover emphasis.
- The white-admixture test passes: sky, sunlit architecture, foliage, flowers, and shadows do not all collapse into opaque baby-blue, lime, and cotton-pink mixtures with the same chalky lightness. If every material looks sweet, milky, or frosted, restore cleaner pigment separation and deeper chromatic anchors instead of merely lowering exposure.
- The atmospheric-envelope test passes: ambient sky and reflected colors visibly recur across selected edges and shadow planes, making the air feel continuous around the subjects without becoming a global fog overlay or changing the source weather.
- Large dark foreground masses remain internally chromatic: weave restrained blue, violet, green, reflected warm, and atmospheric notes through them instead of allowing cactus, foliage, clothing, or ground to collapse into heavy near-black shapes.
- The output reads as an oil painting at both thumbnail size and close inspection.
- The result does not read as a photograph with a paint texture or brush filter laid over it.
- No signature, text, frame, mat, wall, glass, label, or photographic UI appears.

If any preservation check fails, revise before presenting the result.
