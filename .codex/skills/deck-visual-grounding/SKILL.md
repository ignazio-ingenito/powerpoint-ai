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

Produce a concise visual brief:

```markdown
## Visual Brief

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

## Quality Checks

The visual approach is ready when:

- references were inspected fresh;
- the baseline is explicit;
- the deck can remain editable;
- typography and layout support C-level readability;
- visual choices do not introduce non-authoritative logos, images, or claims.
