---
name: monet-light-strokes
description: Transform photos or generate original scenes as luminous Claude Monet-inspired French Impressionist oil paintings with painting-first abstraction, irregular broken color, chromatic shadows, material-specific brushwork, and atmospheric edge loss. Use for Monet or Impressionist style transfers, portraits, landscapes, gardens, flowers, water, architecture, posters, profile pictures, and original illustrations. In edits, preserve the source composition, displayed orientation, aspect ratio, people, identity, pose, clothing, props, landmarks, and complete visible bodies unless the user explicitly requests a change or crop.
---

# Monet Light & Strokes

Create an original Impressionist interpretation in which light and atmosphere organize the scene. Translate reference paintings into observable behavior—palette relationships, edge hierarchy, stroke routing, and paint loading—without copying their subjects, composition, exact palette, visible mark pattern, or signature.

Use the image-generation tool for raster output. Return the artwork only. Never add or offer a frame, mat, wall, glass, label, museum mockup, signature, watermark, text, or photographic UI.

## Load the Right Guidance

- Read [references/style-system.md](references/style-system.md) completely before writing the final generation or edit prompt.
- Read [references/people-in-scenes.md](references/people-in-scenes.md) completely whenever any person is visible, including crowds, cyclists, distant figures, or people used only as scale anchors.
- Read [references/benchmarks.md](references/benchmarks.md) when a benchmark should guide the result. Use B010 as the general benchmark; select at most the few scene-specific benchmarks named in its routing table. Use benchmark images only for their stated paint behavior.

Resolve conflicts in this order: the user's current instruction; source or approved-edit invariants; this file's non-negotiables; scene-specific material guidance; benchmark traits. A benchmark never overrides source facts or a passage the user explicitly approved.

## Establish the Contract

- **Style transfer:** treat the source as factual authority for subject count, identity, pose, outfit, props, setting, landmarks, viewpoint, crop, aspect ratio, displayed orientation, and left/right order. Preserve this factual skeleton, not photographic microtexture or every tiny edge.
- **Original scene:** treat the requested subjects, setting, viewpoint, and format as factual authority; invent the remaining composition.
- **Profile picture:** default to square, but keep the complete visible figure. Do not turn a full-body source into a headshot.
- **Series:** keep the requested subject, viewpoint, crop, and stroke grammar recognizable while varying only the requested light, weather, season, or time. Rebuild the value compression, surviving edges, shadow and reflection shapes, color dominance, and paint activity for each observation; do not make a recolor or reuse one visible texture pattern.

Treat the motif as a measuring instrument for light and weather. Preserve or invent enough subject structure to make the scene factual and legible, but let the observed atmospheric condition govern value compression, temperature, edge survival, and paint activity. The object is not a pre-rendered drawing that later receives an Impressionist surface.

Generate directly when the request is sufficiently specified. Ask only when an unresolved choice would materially change the result.

## Build the Painting

1. **Lock invariants.** Record the source facts internally. For asymmetric edits, state at least two anchors that would expose a mirror, rotation, side swap, or viewpoint drift.
2. **Choose one light key.** Preserve source time and weather unless the user requests a change. Record its dominant value interval, light direction, atmospheric visibility, and temperature bias; let those four properties organize color, edge certainty, and paint loading. In a compressed interval, try warm-cool separation before inventing stronger value contrast.
3. **Map five to nine masses.** Establish broad connected value-color zones before parts. Treat foliage, blossoms, meadows, forests, crowds, roofs, and similar repeated units as collective masses before adding sparse individual clues.
4. **Define form with color boundaries.** Use a light plane, chromatic shadow plane, reflected color, overlap, and lost-and-found edges. Simplify secondary detail without dissolving all structure: major forms must remain legible through neighboring value and temperature changes, not continuous outlines or smooth blur.
5. **Build visible paint chronology.** Use thin ground, broad scumble, brushed or dragged joins, irregular broken middle strokes, partial burial or revision, and a few opaque accents. Let broad and medium marks dominate; reserve small marks and thick impasto for focal sites. Treat broken color as varied visible touch, not as a requirement to cover every region in discrete dabs.
6. **Route marks by material, state, and depth.** Sky, water, ground, architecture, foliage, flowers, skin, hair, fabric, and props must not share one universal stamp. Within each material, vary direction, length, width, loading, opacity, spacing, overlap, and edge quality. Where the source has conventional recession, reduce contrast, mark count, loading, and edge certainty with distance. Do not force cooler distance or near-to-far scaling when the source light or an all-over reflection field contradicts it.
7. **Write the prompt in priority order.** State preservation requirements first, requested changes second, painterly construction third, exclusions last. For a localized revision, explicitly freeze every approved passage and change only the named region or property.
8. **Generate and inspect the complete image.** Check factual preservation before aesthetics, then large masses, form boundaries, mark hierarchy, color, and material routing.
9. **Retry once when required.** Return to the original source or last explicitly approved edit, freeze successful passages, and correct one diagnosed failure. Do not compound drift by repeatedly editing a failed derivative.

## Non-Negotiable Painting Rules

- Preserve the displayed orientation exactly. Never mirror, flip, rotate, transpose, reverse a facing direction or path, swap sides, zoom, or recrop unless requested.
- Preserve people and meaningful objects: count, identity, scale, pose, silhouette, complete visible extent, clothing-color anchors, props, and placement. Do not invent, remove, duplicate, or redesign them.
- Make light and adjacent color-value fields carry form. Keep a few decisive edges where recognition needs them; let secondary edges break, merge, or disappear into atmosphere.
- Use adjacent pigments that mix optically through unequal dabs, strokes, drags, scumbles, veils, smears, and partial burial. Do not replace broken color with seamless gradients, airbrushing, one premixed fill, or a global blur; do not interpret it as dots everywhere.
- Keep transitions visibly painted but non-mechanical. Reject tiny mosaic cells, interlocking facets, repeated lozenges, uniform stippling, parallel wallpaper stripes, knitted hatching, identical short dabs, and dense crystalline ridges.
- Maintain a hierarchy of broad fields, medium descriptive strokes, and sparse small accents. Do not mistake more dabs or equal heavy impasto for more painterly work.
- Keep shadows and dark anchors chromatic—indigo, cobalt, violet, blue-green, olive, crimson, violet-brown, or reflected warmth—not flat black. Preserve a source-defining dark focal anchor when present.
- Keep the lightest notes tinted by their atmosphere—cream, pearl, peach, lilac, or sky color—rather than using broad pure-white fill. Reserve near-white for a few source-supported accents.
- Create luminosity relationally: place selected clean color and pale paint beside quieter grays and deeper chromatic notes. Do not whiten every material into the same chalky pastel value.
- Preserve the source's value-range strategy. Fog, snow glare, backlight, and some series paintings may compress most of the scene into a narrow high, middle, or dark interval; retain a few decisive chromatic anchors instead of expanding every scene to full contrast.
- Let one source-derived color family govern the broad atmospheric field and use complementary or higher-chroma notes as selective counterweights. Do not distribute every attractive pigment evenly across the canvas.
- Carry restrained ambient and reflected colors across selected boundaries so subjects share one atmosphere. Do not add a uniform milky haze.
- Preserve source color identities that carry factual meaning, while tuning hue and temperature within those identities to express the light.
- Keep local paint behavior irregular and scene facts fixed. Randomize marks, never composition, anatomy, object count, light direction, or landmark geometry.
- Produce an original result. Never copy a reference painting's arrangement, exact palette, signature, border, or distinctive visible stroke pattern.

## Acceptance Checklist

Reject or revise the image if any applicable check fails:

### Factual fidelity

- The crop, aspect ratio, orientation, viewpoint, subject count, landmarks, and left/right order match the source.
- At least two asymmetric anchors confirm that the image is not mirrored, rotated, transposed, or side-swapped.
- Every person and important prop retains placement, scale, pose, identity anchors, and complete visible extent.

### Structure and description

- At thumbnail size, roughly five to nine connected masses, coherent light, and a clear focal hierarchy organize the image; spatial depth is stable or intentionally shallow where the source is a horizonless reflection field.
- At normal size, forms remain legible through simple light-dark and warm-cool boundaries after secondary lines are mentally removed.
- The first read is light, air, and collective masses—not individual leaves, petals, siding boards, folds, stones, ripples, or facial inventory.
- With conventional depth, close forms usually carry more contrast and paint while distant forms use fewer, softer, lower-contrast marks. Let distant temperature follow the source light and atmosphere rather than making it automatically cooler.

### Paint and material

- Broad and medium irregular strokes dominate; small marks and thick impasto are selective.
- Visible touch includes fused, dragged, rubbed, scumbled, and partly buried passages; isolated dot-like marks never become the default unit of foliage, meadow, sky, or the whole canvas.
- Thin ground, scumble, broken middle paint, burial, and accents create multiple passes rather than one digital filter.
- A representative mark patch would look wrong if transplanted unchanged between unrelated materials.
- Active passages include irregular overlaps and interruptions; quiet passages remain visibly worked through thinner paint, lower contrast, softer burial, or longer intervals.

### Color and atmosphere

- Warm and cool notes interact without neon color, muddy brown, flat black, or canvas-wide pastel whitening.
- Dark masses remain internally chromatic, and selected light appears brighter through contrast rather than global exposure or saturation.
- Ambient color crosses selected edges without erasing all boundaries or adding a fog overlay.

### Output

- The result reads as an oil painting at thumbnail and close view, not a photograph behind glass, a paint filter, a fine mosaic, a smooth digital illustration, or a uniformly embossed surface.
- No frame, mat, wall, glass, label, signature, watermark, text, or UI appears.

If a factual preservation check fails, revise before returning the artwork.
