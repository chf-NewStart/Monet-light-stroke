# Monet Light & Strokes

A reusable Codex skill for turning photographs and original scenes into luminous, painting-first French Impressionist images while preserving factual composition.

The skill grew from iterative visual critique rather than a single prompt. It encodes broken color, chromatic shadows, relational luminosity, atmospheric color exchange, selective impasto, material-specific brushwork, painting-first abstraction, and strict preservation of people, pose, architecture, props, crop, and orientation.

## What consistency means

Image generation is stochastic: the same source and skill can produce different marks and occasionally different mistakes. The goal is therefore not identical pixels. It is a bounded family of results that repeatedly passes the same factual and painterly checks.

More examples help when they add information. Useful examples are:

- diverse across water, sky, ground, foliage, architecture, people, light, and weather;
- annotated with the exact qualities that passed or failed;
- paired with rejected comparisons when the distinction is subtle;
- explicit about scene invariants such as subject count, crop, orientation, and landmark geometry;
- versioned so a new rule can be tested against old wins instead of silently replacing them.

Many near-duplicate “pretty” images without annotations can make the system less clear and encourage accidental motif copying.

Large historical image collections may be used to derive recurring behavior such as value compression, edge survival, palette dominance, serial variation, and material-specific mark routing. Keep the source archive outside the skill unless redistribution rights are explicit; encode transferable observations and test cases rather than bundling paintings or copying their compositions.

## Repository layout

```text
skills/monet-light-strokes/
  SKILL.md                 Core workflow and preservation contract
  agents/openai.yaml       Codex UI metadata
  references/
    style-system.md        Palette, layering, material, and retry rules
    people-in-scenes.md    Figure distance, clothing, and integration rules
    benchmarks.md          Accepted and rejected benchmark registry
    collage-output.md      Paired clean-artwork and source-derived collage rules
  assets/benchmarks/       Redistributable calibration images
evals/cases.yaml           Scene-diverse regression suite and scoring gates
```

## Use

Ask Codex to install the skill from this repository, then invoke `$monet-light-strokes` with an attached image or an original scene request.

For a photo transfer, the source remains factual authority. Paint-level randomness is welcome; randomness in identity, anatomy, object count, orientation, crop, light direction, or landmark geometry is a failure.

### Paired photo output

For photo transformations, the skill returns the clean converted painting first and a separate portrait collage by default. The collage places the original photo as a smaller upper panel and the approved conversion as the larger lower focal panel inside a restrained source-colored editorial frame. Its background and accent palette come from the source's dominant colors, with sparse subject-related decoration. Supplied collage examples guide layout only unless the user explicitly requests their text or graphics. Original-scene generation remains artwork-only unless a collage is requested.

Museum frames, walls, glass, and environmental presentation mockups remain excluded. The companion collage may use a flat graphic border and keyline around the converted panel, never a physical mockup wrapped around the clean painting.

## Benchmark policy

An image becomes an accepted benchmark only after explicit user approval. Record:

1. the intended material or behavior;
2. accepted visual qualities;
3. rejected failure modes;
4. a transfer rule that forbids copying scene content;
5. provenance and redistribution status.

Keep private source photographs out of the public repository unless their owner explicitly approves publication. Historical reference B004 is documented as an external source and is not bundled because its image-use terms are narrower than a general open-source release.

## Project status and license

This is an experimental public source repository. It does not yet include a license, so it is not yet offered under formal open-source reuse terms. Choose and add a license before announcing it as open source.
