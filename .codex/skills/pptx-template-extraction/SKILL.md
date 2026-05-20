---
name: pptx-template-extraction
description: Use when deriving reusable visual rules, slide patterns, theme details, or layout guidance from docs/template.pptx, a source deck, or PowerPoint visual references.
---

# PPTX Template Extraction

## Purpose

Extract a practical visual system from a `.pptx` template or source deck so future slides preserve style instead of approximating it.

## Required Reads

Read:

1. `AGENTS.md`
2. `.codex/skills/powerpoint-manipulation/SKILL.md`
3. `.codex/skills/deck-visual-grounding/SKILL.md`
4. `docs/ui/README.md`

Inspect:

- `docs/template.pptx` for new decks;
- the source deck when modifying an existing presentation;
- relevant files under `docs/ui/`.

## Extraction Checklist

Extract:

- slide size and orientation;
- theme fonts;
- theme colors;
- master/layout names;
- header and footer objects;
- logo/media assets and relationship ids;
- cover slide pattern;
- section divider pattern;
- content slide grid;
- title and subtitle geometry;
- card/table/diagram styling;
- gradients, fills, borders, shadows;
- icon treatment;
- closing slide pattern.

## Output

Produce a visual system brief:

```markdown
## Template Extraction Brief

- Source file:
- Slide size:
- Theme fonts:
- Palette:
- Masters/layouts:
- Reusable slide patterns:
- Header/footer rules:
- Logo/media rules:
- Card/table rules:
- Diagram/roadmap rules:
- Economics slide rules:
- Constraints:
- Manual checks:
```

## Rules

- Treat the `.pptx` package as authoritative over screenshots.
- Prefer exact geometry and assets from the deck when allowed.
- Do not infer customer facts from visual examples.
- If a logo or decorative asset exists as media, reuse the media asset; do not recreate it with text or shapes.
- When the extraction is used for future decks, document any deviations from the template.
