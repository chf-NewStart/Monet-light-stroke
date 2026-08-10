---
name: monet-light-strokes
description: Transform photos or generate original scenes with luminous Claude Monet-inspired Impressionist atmosphere, painting-first abstraction, coarse irregular broken-color brushwork, colored shadows, reflective water, softened architecture, rhythmic foliage, and optional period-inspired presentation frames. Use for image style transfers, profile pictures, portraits, landscapes, gardens, seascapes, river towns, posters, illustrations, or framed-art presentations when the user asks for Monet, French Impressionism, painterly light, visibly loaded oil strokes, water-lily color fields, or an ornate gilt frame around the result. Preserve identity, pose, outfit, subject count, props, recognizable surroundings, aspect ratio, and complete visible bodies unless the user explicitly requests changes or cropping.
---

# Monet Light & Strokes

Create an original Impressionist interpretation in which light and atmosphere organize the scene. Synthesize the shared visual grammar across the references; never reproduce a particular painting's composition, exact palette, or signature.

Read [references/style-system.md](references/style-system.md) before writing the final generation or edit prompt. Read [references/benchmarks.md](references/benchmarks.md) when an approved benchmark should guide a new result, and use its image only for paint behavior—not scene content. Read [references/frames.md](references/frames.md) only when the user requests a frame, supplies a frame reference, or asks to compare presentation options. Use the image-generation tool for raster output.

## Establish the Contract

Determine the operation from the request:

- **Style transfer:** treat the source image as factual authority for people, pose, clothing, objects, setting, framing, aspect ratio, displayed orientation, and left/right spatial order. Never mirror, flip, rotate, transpose, or swap sides unless the user explicitly requests it. Do not treat its pixel-level texture, tiny edges, individual ripples, or exact tonal map as invariants; reconstruct those through paint.
- **Original scene:** treat the user's scene description as factual authority, then invent a fresh composition.
- **Profile picture:** default to square, but keep the complete visible figure inside the canvas. Do not turn a full-body source into a headshot.
- **Series:** keep the subject, viewpoint, crop, and overall stroke grammar recognizable while deliberately varying time of day, weather, season, and light key. Never reuse one visible texture pattern across the series.

If the request is sufficiently specified, generate directly. Ask only when an unresolved choice would materially change the result.

## Choose the Presentation

Default to **no frame**. Treat a frame as an optional presentation layer, never as part of the Impressionist paint treatment.

When the user requests a frame without choosing one, offer a concise choice:

- **Rectangular carved gilt:** safest default; keeps every part of the painting visible.
- **Oval salon aperture:** dramatic and historical-looking, but conceals the painting's corners; require explicit acceptance of that crop and never conceal a face, complete visible body, or essential prop.
- **Simple aged gilt:** narrower, quieter rails with restrained ornament.
- **Reference-led:** use an attached frame only for its aperture, carving, patina, proportions, and physical finish; never copy the painting, wall, label, glare, or photographic UI inside that reference.

For framed output, use a two-pass workflow: create and inspect the artwork without a frame first, then add the selected frame in a separate edit while treating the accepted artwork as invariant. Prefer extending the outer canvas or scaling the artwork uniformly inside a rectangular aperture over cropping it. Keep frame-level randomness in small carving and patina; keep aperture geometry, rail continuity, corner joins, artwork content, and frame lighting controlled.

## Build the Image

1. **Inventory invariants.** List internally what must not change: subject count, identities, pose, full-body extent, outfit, props, setting landmarks, camera angle, crop, displayed orientation, and left/right anchor order. For an asymmetric scene, write two or more concrete spatial anchors such as “the illuminated house occupies the right third” or “the stairs rise from lower center toward upper right.”
2. **Choose an atmospheric key.** Select a coherent time of day, weather, season, and dominant temperature from the source or request. Light is the main structural device.
3. **Map and simplify large masses.** Squint or mentally blur the source, reduce it to roughly five to nine dominant value-color zones, and merge minor repeated detail into those zones. Establish sky, ground or water, foliage, architecture, and figures from these connected masses before adding selective detail.
4. **Route and layer strokes by material, state, and scale.** Default to medium-to-broad, coarse, irregular marks that remain visible at normal viewing size. Build visible temporal depth from underpainting, scumbled masses, broken descriptive strokes, selective opaque accents, and partial revisions. Distinguish calm reflective water from choppy open sea instead of using one generic water texture. Treat broken color as neighboring pigment notes, not permission to tessellate the canvas with one repeated dab or palette-knife footprint. Aim for chaotic yet structured paint: local marks may be restless and surprising while the large value masses, silhouettes, light direction, and material boundaries remain stable. Introduce controlled hand-made variation inside each material's directional logic. Reconstruct forms with paint rather than tracing the source's micro-edges. Follow the stroke routing in the reference.
5. **Write the generation prompt.** State preservation requirements first, painterly transformation second, exclusions last.
6. **Generate and inspect.** Check the complete image rather than accepting an attractive detail crop. Run both the factual-preservation check and the mark-family check before judging color or mood.
7. **Reject and retry once when needed.** A mirrored composition, missing subject, or canvas-wide repeated brush footprint is a failed edit even when attractive. Retry from the original source with one concrete correction, such as “replace the repeated diagonal lozenge texture with broad quiet sky scumbles, planar architectural strokes, and dragged granular ground clusters.” Do not return a result that still fails a non-negotiable.
8. **Add presentation only after acceptance.** If a frame was selected, make a separate frame edit and re-check both the unchanged artwork and the physical frame.

## Prompt Priorities

Use this order in edit prompts:

1. Preserve the source composition, displayed orientation, left/right spatial order, complete visible body, face, pose, outfit, props, and surroundings. Explicitly forbid mirroring, flipping, rotation, transposition, and side-swapping.
2. Keep the original aspect ratio unless the user requests another format.
3. Repaint the scene through luminous outdoor atmosphere and broken-color oil strokes.
4. Specify the material-dependent stroke behavior and chosen light key.
5. After the artwork passes inspection, use a separate edit to add any selected frame outside it using the frame reference rules.
6. Exclude hard outlines, smooth digital gradients, muddy black shadows, plastic skin, photographic sharpness, text, unrequested frames, and signatures.

Do not use “in the style of Monet” as the entire prompt. Translate the desired look into observable decisions about light, palette, edges, and strokes.

## Non-Negotiables

- Preserve full-body framing when a body is fully visible in the source. Keep head, hands, legs, and shoes inside the canvas with breathing room.
- Preserve the source exactly as displayed after metadata orientation is applied. Never mirror horizontally or vertically, rotate, transpose, reverse a subject's facing direction, reverse the direction of stairs or paths, or move distinctive landmarks to the opposite side unless the user explicitly asks.
- Preserve facial identity and expression while simplifying features into painterly planes.
- Keep shadows chromatic: blue, violet, green, rose, or warm gray instead of flat black.
- Preserve recognizable source color identities where they carry factual meaning, especially skin, clothing, and key props, but tune hue, temperature, and chroma within those identities to express the atmospheric light. Treat literal sampled color as a starting point rather than a ceiling.
- Define silhouettes and contours through neighboring shifts of value, temperature, and reflected color rather than heavy black outlines. Keep the deepest accents chromatic and allow light to break selected edges.
- Use adjacent broken colors that mix optically; avoid globally blended or airbrushed surfaces.
- Build the paint surface from fewer broad and medium overlapping strokes with selective thick accents. Avoid covering the image in tiny, uniformly distributed mosaic marks.
- Interpret broken color as color separation inside a hierarchy of broad fields, medium descriptive strokes, and sparse small accents. “More dabs” must never become one repeated mark shape, size, angle, or spacing across the canvas.
- Keep each material's dominant brush footprint visibly different. Never cover sky, ground, architecture, foliage, water, or figures with the same diagonal lozenges, rectangular facets, leaf stamps, or palette-knife tiles.
- Allow a recurring rhythm inside one material when its marks vary substantially in scale, angle, overlap, loading, edge, spacing, and color and remain subordinate to a clear large-scale structure. Do not reject a bold active passage merely because it is coarse or energetic.
- Preserve the factual skeleton, not the photographic microtexture. Keep the crop, subject silhouettes, identities, pose, landmarks, major value bands, and light direction, but simplify, merge, omit, and repaint minor ripples, leaves, texture, and incidental edges.
- Allow mark-level randomness in angle, spacing, pressure, length, opacity, temperature, overlap, and edge quality. Keep scene-level facts—composition, identity, anatomy, object count, light direction, and reflection placement—strictly fixed.
- Soften distant forms with lower contrast, cooler color, and fewer marks.
- Let reflections echo objects as broken vertical color paths interrupted by the surface's actual water-state gestures: mostly horizontal ripples in calm passages, more oblique or rolling cuts in turbulent passages.
- Use dark accents sparingly for eyes, boats, branches, windows, or figure anchors; avoid ink-like contouring.
- Produce an original result. Do not add Monet's signature, labels, watermarks, copied arrangements from a reference painting, or any frame the user did not select.
- When a frame is selected, preserve the accepted painting as a distinct inner artwork. Do not repaint it, fuse ornament into it, cover important content, or imply that a period-inspired frame is historically authenticated.

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
- Broad connected or thinly scumbled quieter passages remain perceptible beside active broken-color clusters. Quiet may mean lower contrast, thinner loading, softer burial, or slower rhythm rather than a smooth or empty surface. Reject only nearly equal activity and density from edge to edge.
- The chaotic-yet-structured test passes: close inspection reveals irregular, partly revised, non-mechanical marks; thumbnail inspection reveals a stable arrangement of roughly five to nine masses, coherent light, readable silhouettes, and intact source facts.
- Repeated marks feel hand placed rather than stamped: clusters, pauses, imperfect overlaps, and occasional corrective or off-color strokes remain visible without damaging legibility.
- When blurred or viewed as a thumbnail, the image is organized by a small number of clear color-value masses rather than a traced photographic tonal map.
- Most photographic micro-edges and local texture are gone. Only a few focal edges remain; secondary edges merge, break, or dissolve into adjacent paint.
- Water has a continuous painted body beneath its surface gestures. Calm water uses unequal broken horizontal marks; choppy or breaking sea follows the wave forms with rolling arcs, oblique or diagonal slashes, hooks, turning crests, and dragged foam. Reject neat parallel ribbons, state-blind universal marks, random canvas-wide crosshatching, and interlocking rectangular color slabs.
- The paint surface reveals multiple passes: thin ground, partly covered scumbles, varied broken middle strokes, and a few opaque accents. It does not look uniformly rendered in one digital pass.
- Painterly secondary passages remain visibly coarse, approximate, and worked. Do not automatically clean an expressive sky, sand, ground, or foliage field into smoother, more precise illustration.
- Do not self-correct a user-approved bold passage into smoother realism. When an approved benchmark and a cleaner revision conflict, preserve the benchmark's mark separation, optical vibration, and chromatic shadow behavior unless the user requests otherwise.
- Close forms have richer contrast and thicker marks; distant forms dissolve into atmosphere.
- Warm and cool notes vibrate without becoming neon or muddy brown.
- Apparent brightness comes from selective clear color beside quieter grays and chromatic shadows, not from raising exposure or saturation across the whole image.
- Large dark foreground masses remain internally chromatic: weave restrained blue, violet, green, reflected warm, and atmospheric notes through them instead of allowing cactus, foliage, clothing, or ground to collapse into heavy near-black shapes.
- The output reads as an oil painting at both thumbnail size and close inspection.
- The result does not read as a photograph with a paint texture or brush filter laid over it.
- No signature, text, unintended frame, or photographic UI appears.
- When a frame is selected, the artwork remains unchanged inside the aperture; all intended sides and corners connect; carving scale, patina, bevels, inner shadow gap, and lighting read as one physical object; no essential content is concealed beyond an explicitly approved oval crop.

If any preservation check fails, revise before presenting the result.
