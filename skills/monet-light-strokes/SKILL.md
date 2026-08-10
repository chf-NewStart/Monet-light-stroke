---
name: monet-light-strokes
description: Transform photos or generate original scenes with luminous Claude Monet-inspired Impressionist atmosphere, painting-first abstraction, coarse irregular broken-color brushwork, colored shadows, reflective water, softened architecture, rhythmic foliage, and optional period-inspired presentation frames. Use for image style transfers, profile pictures, portraits, landscapes, gardens, seascapes, river towns, posters, illustrations, or framed-art presentations when the user asks for Monet, French Impressionism, painterly light, visibly loaded oil strokes, water-lily color fields, or an ornate gilt frame around the result. Preserve identity, pose, outfit, subject count, props, recognizable surroundings, aspect ratio, and complete visible bodies unless the user explicitly requests changes or cropping.
---

# Monet Light & Strokes

Create an original Impressionist interpretation in which light and atmosphere organize the scene. Synthesize the shared visual grammar across the references; never reproduce a particular painting's composition, exact palette, or signature.

Read [references/style-system.md](references/style-system.md) before writing the final generation or edit prompt. Read [references/benchmarks.md](references/benchmarks.md) when an approved benchmark should guide a new result, and use its image only for paint behavior—not scene content. Read [references/frames.md](references/frames.md) only when the user requests a frame, supplies a frame reference, or asks to compare presentation options. Use the image-generation tool for raster output.

## Establish the Contract

Determine the operation from the request:

- **Style transfer:** treat the source image as factual authority for people, pose, clothing, objects, setting, framing, and aspect ratio. Do not treat its pixel-level texture, tiny edges, individual ripples, or exact tonal map as invariants; reconstruct those through paint.
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

1. **Inventory invariants.** List internally what must not change: subject count, identities, pose, full-body extent, outfit, props, setting landmarks, camera angle, and crop.
2. **Choose an atmospheric key.** Select a coherent time of day, weather, season, and dominant temperature from the source or request. Light is the main structural device.
3. **Map and simplify large masses.** Squint or mentally blur the source, reduce it to roughly five to nine dominant value-color zones, and merge minor repeated detail into those zones. Establish sky, ground or water, foliage, architecture, and figures from these connected masses before adding selective detail.
4. **Route and layer strokes by material, state, and scale.** Default to medium-to-broad, coarse, irregular marks that remain visible at normal viewing size. Build visible temporal depth from underpainting, scumbled masses, broken descriptive strokes, selective opaque accents, and partial revisions. Distinguish calm reflective water from choppy open sea instead of using one generic water texture. Introduce controlled hand-made variation inside each material's directional logic. Reconstruct forms with paint rather than tracing the source's micro-edges. Follow the stroke routing in the reference.
5. **Write the generation prompt.** State preservation requirements first, painterly transformation second, exclusions last.
6. **Generate and inspect.** Check the complete image rather than accepting an attractive detail crop.
7. **Retry once when needed.** Make the correction concrete, such as “zoom out to restore both shoes and surrounding street,” not merely “improve composition.”
8. **Add presentation only after acceptance.** If a frame was selected, make a separate frame edit and re-check both the unchanged artwork and the physical frame.

## Prompt Priorities

Use this order in edit prompts:

1. Preserve the source composition, complete visible body, face, pose, outfit, props, and surroundings.
2. Keep the original aspect ratio unless the user requests another format.
3. Repaint the scene through luminous outdoor atmosphere and broken-color oil strokes.
4. Specify the material-dependent stroke behavior and chosen light key.
5. After the artwork passes inspection, use a separate edit to add any selected frame outside it using the frame reference rules.
6. Exclude hard outlines, smooth digital gradients, muddy black shadows, plastic skin, photographic sharpness, text, unrequested frames, and signatures.

Do not use “in the style of Monet” as the entire prompt. Translate the desired look into observable decisions about light, palette, edges, and strokes.

## Non-Negotiables

- Preserve full-body framing when a body is fully visible in the source. Keep head, hands, legs, and shoes inside the canvas with breathing room.
- Preserve facial identity and expression while simplifying features into painterly planes.
- Keep shadows chromatic: blue, violet, green, rose, or warm gray instead of flat black.
- Preserve recognizable source color identities where they carry factual meaning, especially skin, clothing, and key props, but tune hue, temperature, and chroma within those identities to express the atmospheric light. Treat literal sampled color as a starting point rather than a ceiling.
- Define silhouettes and contours through neighboring shifts of value, temperature, and reflected color rather than heavy black outlines. Keep the deepest accents chromatic and allow light to break selected edges.
- Use adjacent broken colors that mix optically; avoid globally blended or airbrushed surfaces.
- Build the paint surface from fewer broad and medium overlapping strokes with selective thick accents. Avoid covering the image in tiny, uniformly distributed mosaic marks.
- Preserve the factual skeleton, not the photographic microtexture. Keep the crop, subject silhouettes, identities, pose, landmarks, major value bands, and light direction, but simplify, merge, omit, and repaint minor ripples, leaves, texture, and incidental edges.
- Allow mark-level randomness in angle, spacing, pressure, length, opacity, temperature, overlap, and edge quality. Keep scene-level facts—composition, identity, anatomy, object count, light direction, and reflection placement—strictly fixed.
- Soften distant forms with lower contrast, cooler color, and fewer marks.
- Let reflections echo objects as broken vertical color paths interrupted by horizontal water strokes.
- Use dark accents sparingly for eyes, boats, branches, windows, or figure anchors; avoid ink-like contouring.
- Produce an original result. Do not add Monet's signature, labels, watermarks, copied arrangements from a reference painting, or any frame the user did not select.
- When a frame is selected, preserve the accepted painting as a distinct inner artwork. Do not repaint it, fuse ornament into it, cover important content, or imply that a period-inspired frame is historically authenticated.

## Quality Check

Before returning the image, verify:

- The requested subject and source composition remain recognizable.
- No person or important prop has been cropped, invented, removed, or duplicated.
- The light condition is coherent across sky, subject, ground, and reflections.
- Stroke direction changes with the material instead of becoming one generic texture.
- The material-transfer test passes: a representative patch of sky, ground, foliage, water, masonry, or cactus marks would look visibly wrong if transplanted unchanged onto another material. If several passages seem interchangeable, reroute their direction, scale, loading, density, edges, and layering.
- Dominant strokes remain clearly visible at normal viewing size and vary in width, length, loading, and edge quality.
- Repeated marks feel hand placed rather than stamped: clusters, pauses, imperfect overlaps, and occasional corrective or off-color strokes remain visible without damaging legibility.
- When blurred or viewed as a thumbnail, the image is organized by a small number of clear color-value masses rather than a traced photographic tonal map.
- Most photographic micro-edges and local texture are gone. Only a few focal edges remain; secondary edges merge, break, or dissolve into adjacent paint.
- Water has a continuous painted body beneath its surface gestures. Open-sea movement is carried by irregular sweeping crests and dragged foam rather than interlocking rectangular color slabs.
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
