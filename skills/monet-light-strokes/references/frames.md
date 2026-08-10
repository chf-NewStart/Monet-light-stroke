# Optional Presentation Frames

Use these rules only after the unframed artwork has passed preservation and painterly checks. The frame is a separate physical presentation object, not another painted material inside the scene.

## Selection

- **None:** default. Return only the painted artwork.
- **Rectangular carved gilt:** recommended when source fidelity matters. Keep the complete artwork visible inside a rectangular aperture.
- **Oval salon aperture:** use only after explicit approval that the four corners will be concealed. Recompose nothing; protect faces, complete visible bodies, props, and landmarks from the aperture.
- **Simple aged gilt:** use narrower rails, shallow carving, restrained corner ornaments, and quieter patina.
- **Reference-led:** label the supplied frame image as a design reference. Extract only aperture shape, rail width, molding profile, ornament density, patina, and color. Ignore any painting, wall, placard, glare, shadow, signature, border, or UI in that image.

Do not claim that a generated period-inspired frame is historically authentic to the depicted artwork or chosen by Claude Monet.

## Two-Pass Construction

1. Generate or edit the artwork without a frame.
2. Inspect and accept its subject fidelity, composition, crop, aspect ratio, light, color, and brushwork.
3. Use that accepted image as the sole artwork authority in a new edit.
4. Add the frame outside the artwork. Extend the outer canvas or scale the artwork uniformly inside the aperture; do not crop a rectangular presentation.
5. Re-check the artwork pixel-for-content: no regenerated people, paint, color relationships, reflections, architecture, or text.

For an oval aperture, treat corner concealment as the only authorized crop. If essential content reaches a corner, recommend a rectangular aperture instead.

## Physical Design

Build the frame as carved wood with aged gold leaf rather than flat yellow decoration.

- Keep four complete rails with believable mitred or carved corner joins.
- Use a regular rectangular or oval inner aperture and a narrow inner liner or dark shadow gap that clearly separates frame from canvas.
- Build relief through a few molding levels: outer crest, recessed band, ornamental band, and inner lip. Do not multiply borders indefinitely.
- Vary small leaf, flower, scroll, bead, and shell details naturally while maintaining coherent large-scale symmetry and rail rhythm.
- Let raised gold catch warm highlights while recesses carry muted umber, olive-brown, violet-brown, and dark gold.
- Add restrained wear, rubbed high points, tiny darkened crevices, and uneven leaf tone. Avoid pristine metallic plastic, extreme corrosion, or random damage.
- Match one coherent light direction across top, sides, and bottom. Retain believable relief shadows and material depth.
- Keep the frame sharper and more materially precise than the Impressionist artwork, but do not render it as glossy CGI.

## Prompt Scaffold

> Image 1 is the accepted artwork and must remain unchanged. Add only a [rectangular carved gilt / oval salon / simple aged gilt / reference-led] physical frame around it. Preserve every subject, mark, color relationship, orientation, and the inner artwork's aspect ratio. [For oval: the user explicitly accepts concealment of the four corners; keep all essential subjects clear of the aperture.] Construct complete carved-wood rails with aged gold leaf, coherent molding levels, believable corner joins, a regular aperture, an inner liner and shadow gap, warm highlights, dark chromatic recesses, restrained patina, and one light direction. Extend the outer canvas or scale the artwork uniformly; do not repaint, regenerate, stretch, or otherwise crop the accepted artwork. No wall, placard, glare, signature, text, watermark, museum UI, broken rail, duplicated ornament cluster, melted carving, or extra frame.

## Quality Check

- The accepted artwork is visibly identical in content and composition.
- The selected aperture shape and frame type are unmistakable.
- Every rail is present; corners meet; the aperture is regular and centered.
- The frame never covers a face, complete visible body, essential prop, or landmark without explicit oval-crop consent.
- Frame relief, gold leaf, patina, liner, and shadows read as one physical object.
- The frame is visually compatible with the artwork but does not copy its brush texture.
- No painting from a frame reference leaks into the result.

Retry a failed frame edit with one concrete correction: restore the unchanged artwork, regularize the aperture, repair the named rail or corner, remove the invented presentation element, or switch from oval to rectangular to recover concealed content.
