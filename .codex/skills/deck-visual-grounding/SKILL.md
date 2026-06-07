---
name: deck-visual-grounding
description: Use before creating or modifying a PowerPoint deck to derive layout, typography, colors, icon usage, and slide patterns from docs/template.pptx, docs/ui, and any source deck.
---

# Deck Visual Grounding

## Purpose

Make generated or revised decks visually coherent with TXT/Novigo references while preserving editability in PowerPoint.

## Required Reads and Inspection

Read:

1. `AGENTS.md`
2. `.codex/deck-pipeline.md`
3. `docs/ui/README.md`

List actual visual references:

```bash
find docs/ui -maxdepth 1 -type f | sort
```

Inspect the relevant images or source decks for the requested deck type.

When creating a new deck, inspect `docs/template.pptx` when practical.

If `docs/template.pdf` exists, inspect it as the primary visual fidelity reference. The PDF shows the real exported appearance of the template; the `.pptx` remains the editable source for masters, layouts, theme parts, and assets.

When revising a deck, inspect the source `.pptx` and treat it as the primary visual baseline unless the user says otherwise.

## Visual Aspects to Extract

Derive:

- slide aspect ratio;
- header/footer conventions;
- logo placement;
- title scale and position;
- color palette and gradients;
- typography;
- whitespace and grid;
- card and table style;
- architecture/process diagram style;
- roadmap and economics patterns;
- icon density and treatment;
- closing slide conventions.
- exported-template patterns from `docs/template.pdf`, especially cover, header/footer, three-column initiative slides, thin bordered cards, roadmap layouts, value-generated bands, page numbers, and closing slide.

Also map each major planned slide to a visual reference family or guardrail from `docs/ui/` when one exists. This mapping should guide visual coherence, not prescribe exact coordinates unless strict recreation is required.

At minimum map:

- cover;
- `Contesto / Esigenza / Obiettivi`;
- AS IS / architecture or process;
- TO BE / scenario or target architecture;
- roadmap / piano di lavoro;
- economics;
- decision / next steps.

The visual plan should name the reference file or reference family used for each pattern.

## Creative Freedom Rule

When the output will be used by another model, designer, or slide-generation tool, produce a creative brief instead of a rigid layout specification.

For each slide, separate:

- `Slide brief`: role in the story, message, mandatory content, optional content, source basis, assumptions, and claims to avoid.
- `Creative direction`: reference family, desired feel, density, suggested visual forms, anti-patterns, and brand guardrails.
- `Creative freedom`: `High`, `Medium`, or `Low`.

Use:

- `High` when many visual solutions can communicate the message well.
- `Medium` when the slide should resemble a reference family but can vary composition.
- `Low` when the slide should follow a known pattern closely, such as cover, `Contesto / Esigenza / Obiettivi`, formal economics, or institutional closing.

Do not over-specify arrows, box counts, exact chart type, or coordinates for `High` and `Medium` slides. Give alternative visual forms instead, such as flow, before/after, layered architecture, decision map, process lane, table, or visual metaphor consistent with the references.

## Editability Rules

Prefer:

- real PowerPoint text boxes;
- native shapes;
- native tables;
- connectors;
- reusable image assets only where the element is visual by nature.

Avoid:

- rasterizing text;
- manually recreating logos;
- copying customer-specific visual content;
- overloading slides with small text;
- adding decorative elements that are not present in the reference language.

## Visual Brief Output

Produce a concise creative direction:

```markdown
## Creative Direction

- Baseline:
- Palette:
- Typography:
- Header/footer:
- Section divider pattern:
- Content slide pattern:
- Architecture/process pattern:
- Economics pattern:
- Icon rules:
- Constraints:
```

Use this brief to guide deck generation and review.

For slide-by-slide plans intended for external models/tools, use:

```markdown
## Slide Brief

- Slide:
- Role in story:
- Must communicate:
- Must include:
- Optional content:
- Must not claim:
- Source basis:
- Assumptions:
- Creative direction:
- Suggested visual forms:
- Reference guardrails:
- Creative freedom: High | Medium | Low
```

Avoid approving a handoff where the narrative is vague and the layout is over-specified. The goal is to preserve message, evidence, and brand guardrails while allowing better visual composition.

## Quality Checks

The visual approach is ready when:

- references were inspected fresh;
- `docs/template.pdf` was compared when available;
- the baseline is explicit;
- each major slide type has a slide brief, reference guardrail, and creative freedom level;
- strict matching is required only where `Creative freedom` is `Low`;
- the first content slide follows the `Contesto / Esigenza / Obiettivi` pattern when the deck is a proposal/business case;
- the deck can remain editable;
- typography and layout support C-level readability;
- visual choices do not introduce non-authoritative logos, images, or claims.
