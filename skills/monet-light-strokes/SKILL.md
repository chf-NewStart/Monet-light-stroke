---
name: monet-light-strokes
description: Transform photos or generate original scenes as luminous Claude Monet-inspired French Impressionist oil paintings with painting-first abstraction, irregular broken color, chromatic shadows, material-specific brushwork, and atmospheric edge loss. Use for Monet or Impressionist style transfers, portraits, landscapes, gardens, flowers, water, architecture, posters, profile pictures, and original illustrations. In edits, preserve the source composition, displayed orientation, aspect ratio, people, identity, pose, clothing, props, landmarks, and complete visible bodies unless the user explicitly requests a change or crop.
---

# Monet Light & Strokes

Create an original Impressionist interpretation in which light and atmosphere organize the scene. Translate reference paintings into observable behavior—palette relationships, edge hierarchy, stroke routing, and paint loading—without copying their subjects, composition, exact palette, visible mark pattern, or signature.

Use the image-generation tool for raster output. For photo transformations in this user's workflow, return two separate deliverables by default: the clean converted painting first, then a companion collage that pairs the approved conversion with the original photo. The clean painting must never contain a frame, mat, wall, glass, label, museum mockup, signature, watermark, text, photographic UI, or collage treatment. The companion collage is a distinct graphic artifact and follows [references/collage-output.md](references/collage-output.md).

## Load the Right Guidance

- Read [references/style-system.md](references/style-system.md) completely before writing the final generation or edit prompt.
- Read [references/people-in-scenes.md](references/people-in-scenes.md) completely whenever any person is visible, including crowds, cyclists, distant figures, or people used only as scale anchors.
- Read [references/benchmarks.md](references/benchmarks.md) when a benchmark should guide the result. Use B010 as the general benchmark; select at most the few scene-specific benchmarks named in its routing table. Use benchmark images only for their stated paint behavior.
- Read [references/collage-output.md](references/collage-output.md) completely for the default companion collage or whenever the user requests a collage, poster, comparison layout, or presentation graphic.

Resolve conflicts in this order: the user's current instruction; source or approved-edit invariants; this file's non-negotiables; scene-specific material guidance; benchmark traits. A benchmark never overrides source facts or a passage the user explicitly approved.

## Establish the Contract

- **Style transfer:** treat the source as factual authority for subject count, identity, pose, outfit, props, setting, landmarks, viewpoint, crop, aspect ratio, displayed orientation, and left/right order. Preserve this factual skeleton, not photographic microtexture or every tiny edge.
- **Original scene:** treat the requested subjects, setting, viewpoint, and format as factual authority; invent the remaining composition.
- **Profile picture:** default to square, but keep the complete visible figure. Do not turn a full-body source into a headshot.
- **Paired photo output:** unless the user opts out, approve the clean converted painting before making a separate collage from that exact conversion and the original photo. Default to the original photo as a smaller upper panel and the converted painting as the larger lower focal panel inside a complete museum-style carved frame isolated on the graphic field. Derive the collage's field color, accents, patina, and decorative motif from the source's dominant and focal colors. Treat any supplied collage or frame example as structural inspiration only unless the user explicitly asks to copy particular text, graphics, or ornament.
- **Series:** keep the requested subject, viewpoint, crop, and stroke grammar recognizable while varying only the requested light, weather, season, or time. Rebuild the value compression, surviving edges, shadow and reflection shapes, color dominance, and paint activity for each observation; do not make a recolor or reuse one visible texture pattern.
- **Historical handling:** default an unspecified Monet request to a classic middle-period balance of broken color, directed visible touch, and legible structure. Use tighter early handling or broader all-over late handling only when requested or clearly appropriate; change paint behavior, never source facts.

Treat the motif as a measuring instrument for light and weather. Preserve or invent enough subject structure to make the scene factual and legible, but let the observed atmospheric condition govern value compression, temperature, edge survival, and paint activity. The object is not a pre-rendered drawing that later receives an Impressionist surface.

Generate directly when the request is sufficiently specified. Ask only when an unresolved choice would materially change the result.

## Build the Painting

1. **Lock invariants.** Record the source facts internally. For asymmetric edits, state at least two anchors that would expose a mirror, rotation, side swap, or viewpoint drift.
2. **Choose one light key.** Preserve source time and weather unless the user requests a change. Record its dominant value interval, light direction, atmospheric visibility, and temperature bias; let those four properties organize color, edge certainty, and paint loading. In a compressed interval, try warm-cool separation before inventing stronger value contrast.
3. **Choose hue latitude and handling.** Let the light and motif determine how wide the neighboring hue range should be: restrained and convergent in fog or quiet atmosphere; wider but still organized in gardens, flowers, and late reflective fields. Apply the requested historical handling mode without changing the source skeleton.
4. **Map five to nine masses.** Establish broad connected value-color zones before parts. Treat foliage, blossoms, meadows, forests, crowds, roofs, and similar repeated units as collective masses before adding sparse individual clues.
5. **Define form with color boundaries.** Use a light plane, chromatic shadow plane, reflected color, overlap, and lost-and-found edges. Simplify secondary detail without dissolving all structure: major forms must remain legible through neighboring value and temperature changes, not continuous outlines or smooth blur.
6. **Build visible paint chronology.** Use thin ground, broad scumble, brushed or dragged joins, irregular broken middle strokes, partial burial or revision, and a few opaque accents. Let broad and medium marks dominate; reserve small marks and thick impasto for focal sites. Treat broken color as varied visible touch, not as a requirement to cover every region in discrete dabs.
7. **Route activity as well as marks.** Route marks by material, state, and depth, and concentrate paint activity where light changes, overlap, motion, texture, or recognition carry information. Preserve quieter intervals elsewhere. Within each material, vary direction, length, width, loading, opacity, spacing, overlap, and edge quality. Where the source has conventional recession, reduce contrast, mark count, loading, and edge certainty with distance. Do not force cooler distance or near-to-far scaling when the source light or an all-over reflection field contradicts it.
8. **Write the prompt in priority order.** State preservation requirements first, requested changes second, painterly construction third, exclusions last. For a localized revision, explicitly freeze every approved passage and change only the named region or property.
9. **Generate and inspect the complete image.** Check factual preservation before aesthetics, then large masses, form boundaries, activity hierarchy, mark hierarchy, color, and material routing.
10. **Retry once when required.** Return to the original source or last explicitly approved edit, freeze successful passages, and correct one diagnosed failure. Do not compound drift by repeatedly editing a failed derivative.
11. **Build the companion collage after approval.** Use the original photo and final approved conversion as fixed panels. Choose a source-derived background, one restrained counter-accent, and a subject-related decorative motif; inspect both panels for crop, orientation, and content drift before returning both files.

## Non-Negotiable Painting Rules

- Preserve the displayed orientation exactly. Never mirror, flip, rotate, transpose, reverse a facing direction or path, swap sides, zoom, or recrop unless requested.
- Preserve people and meaningful objects: count, identity, scale, pose, silhouette, complete visible extent, clothing-color anchors, props, and placement. Do not invent, remove, duplicate, or redesign them.
- Make light and adjacent color-value fields carry form. Keep a few decisive edges where recognition needs them; let secondary edges break, merge, or disappear into atmosphere.
- Use adjacent pigments that mix optically through unequal dabs, strokes, drags, scumbles, veils, smears, and partial burial. Do not replace broken color with seamless gradients, airbrushing, one premixed fill, or a global blur; do not interpret it as dots everywhere.
- Keep transitions visibly painted but non-mechanical. Reject tiny mosaic cells, interlocking facets, repeated lozenges, uniform stippling, parallel wallpaper stripes, knitted hatching, identical short dabs, and dense crystalline ridges.
- Maintain a hierarchy of broad fields, medium descriptive strokes, and sparse small accents. Do not mistake more dabs or equal heavy impasto for more painterly work.
- Keep shadows and dark anchors chromatic and material-derived—not automatically violet and never flat black. Foliage may favor deep green or olive; cool reflected light may favor indigo, cobalt, violet, or blue-green; warm materials may favor crimson, violet-brown, or reflected warmth. Preserve a source-defining dark focal anchor when present.
- Keep the lightest notes tinted by their atmosphere—cream, pearl, peach, lilac, or sky color—rather than using broad pure-white fill. Reserve near-white for a few source-supported accents.
- Create luminosity relationally: place selected clean color and pale paint beside quieter grays and deeper chromatic notes. Do not whiten every material into the same chalky pastel value.
- Preserve the source's value-range strategy. Fog, snow glare, backlight, and some series paintings may compress most of the scene into a narrow high, middle, or dark interval; retain a few decisive chromatic anchors instead of expanding every scene to full contrast.
- Let one source-derived color family govern the broad atmospheric field and use complementary or higher-chroma notes as selective counterweights. Do not distribute every attractive pigment evenly across the canvas.
- Let hue latitude follow the condition and motif. Keep fog, haze, and restrained atmosphere comparatively convergent; permit a wider organized range in gardens, flower fields, and late all-over reflections. Do not hard-code one hue range for every scene.
- Allocate paint density by information and attention. Cluster stronger contrast, directional change, thicker loading, and smaller accents near meaningful light events, material transitions, motion, and focal recognition; give supporting passages longer, softer, thinner, or partly buried intervals. Do not confuse photographic edge density with pictorial importance.
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
- When a historical handling mode is requested, its edge certainty, stroke scale, paint loading, and degree of all-over abstraction are coherent without altering the factual composition.

### Paint and material

- Broad and medium irregular strokes dominate; small marks and thick impasto are selective.
- Visible touch includes fused, dragged, rubbed, scumbled, and partly buried passages; isolated dot-like marks never become the default unit of foliage, meadow, sky, or the whole canvas.
- Thin ground, scumble, broken middle paint, burial, and accents create multiple passes rather than one digital filter.
- A representative mark patch would look wrong if transplanted unchanged between unrelated materials.
- Active passages include irregular overlaps and interruptions; quiet passages remain visibly worked through thinner paint, lower contrast, softer burial, or longer intervals.
- Paint activity follows pictorial information and attention: focal light, motion, overlap, and material change receive more activity than supporting fields, without becoming an edge-map or uniformly busy surface.

### Color and atmosphere

- Warm and cool notes interact without neon color, muddy brown, flat black, or canvas-wide pastel whitening.
- Dark masses remain internally chromatic, and selected light appears brighter through contrast rather than global exposure or saturation.
- Hue variety matches the atmospheric condition and motif rather than staying equally broad or equally narrow in every scene; dark hue remains locally derived rather than automatically violet.
- Ambient color crosses selected edges without erasing all boundaries or adding a fog overlay.

### Clean painting output

- The result reads as an oil painting at thumbnail and close view, not a photograph behind glass, a paint filter, a fine mosaic, a smooth digital illustration, or a uniformly embossed surface.
- No frame, mat, wall, glass, label, signature, watermark, text, or UI appears.

### Companion collage output

- The approved clean painting and original photo remain distinct, complete, correctly oriented panels; the collage does not silently repaint, mirror, recrop, or substitute either one. By default the smaller original sits above and the larger converted painting sits below inside a complete museum-style carved frame.
- The broad background field comes from the source's dominant color family, while focal or complementary source colors supply restrained accents and a tinted neutral supplies linework or borders.
- Graphic decoration is sparse, subject-related, and confined to negative space. Supplied reference text, icons, controls, logos, and decorative motifs are not copied unless explicitly requested.
- The converted panel's frame reads as aged carved wood with layered molding: outer repeat rail, recessed cove, raised restrained ornament, dark reveal, and thin inner slip. Keep all four sides and corners visible with consistent mitres, believable relief, patina, and one coherent light direction. Isolate it on the poster field without glass, a room, wall, easel, or gallery mockup.
- No invented title, location, date, caption, signature, logo, watermark, wall, hand, or additional photo appears.

If a factual preservation check fails in either deliverable, revise before returning it.
