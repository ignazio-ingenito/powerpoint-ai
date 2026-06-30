---
name: powerpoint-manipulation
description: Use when inspecting, editing, merging, validating, repairing, exporting, or programmatically manipulating PowerPoint .pptx files in this repository.
---

# PowerPoint Manipulation

## Purpose

Manipulate `.pptx` files as editable PowerPoint packages while preserving visual fidelity, source grounding, and package integrity.

Use this skill with the local deck pipeline, visual grounding, and quality review skills.

## Required Reads

Before manipulating a deck, read fresh:

1. `AGENTS.md`
2. `.codex/execution.md`
3. `.codex/deck-pipeline.md`
4. `.codex/skills/deck-visual-grounding/SKILL.md`
5. `.codex/skills/commercial-deck-quality-review/SKILL.md`

For content-bearing changes, also read all `docs/reference*.md` and task-specific source materials.

## Operating Rules

- Do not overwrite a source deck without explicit approval.
- Save new final deliverables in the relevant presentation folder.
- Keep text, tables, shapes, connectors, and diagrams editable where practical.
- Prefer copying/adapting existing slide layouts over rebuilding them from scratch.
- Reuse actual logo/image assets from an authorized source deck or template; do not recreate logos with text.
- Treat `docs/template.pptx` and source decks as PowerPoint package baselines, not just screenshots.
- Do not copy customer-specific content from reference decks unless explicitly authorized.
- Do not assume Node dependencies exist. This repo may intentionally have no `package.json`.
- When generating from `docs/ui/` references, respect the creative handoff or visual plan. For slides marked `Creative freedom: Low`, adapt the relevant reference pattern closely. For `Medium` or `High`, preserve message, brand guardrails, editability, and source grounding without forcing exact layout replication.
- Do not replace a clearly required formal pattern, such as `Contesto / Esigenza / Obiettivi`, formal economics, cover, or institutional closing, with a generic card/dashboard layout unless the handoff explicitly allows it.

## Inspection Workflow

For any `.pptx` that will be modified or used as a reference:

1. Inventory the package:
   - `unzip -l "<file>.pptx" | sed -n '1,80p'`
2. Inspect core structure:
   - `[Content_Types].xml`
   - `ppt/presentation.xml`
   - `ppt/slides/*.xml`
   - `ppt/slides/_rels/*.rels`
   - `ppt/slideMasters/*`
   - `ppt/slideLayouts/*`
   - `ppt/theme/*`
   - `ppt/media/*`
3. Extract slide text when needed.
4. Inspect dimensions, object types, fonts, colors, fills, lines, relationships, and media assets.
5. Map slide numbers to storyline sections and source evidence.

## Editing Strategy

Choose the least risky strategy:

| Need | Preferred strategy |
|---|---|
| Change text only | edit existing text boxes or regenerate using copied layout |
| Add a similar slide | duplicate a similar slide pattern and replace content |
| Build a new deck | use `docs/template.pptx`, `docs/ui/`, and any presentation-folder `visual-references/` as visual references |
| Preserve exact style | copy geometry, theme, media, and XML patterns from source deck |
| Repair package issues | normalize package parts without changing visible content |
| Heavy generation | add a script/dependency only after confirming it is needed |

If a script is needed, keep it under `scripts/` and document why a static/manual approach is insufficient.

For generated decks, the script should encode reusable layout functions that support the selected creative direction. Use stricter reference-pattern functions for low-freedom slides, and more flexible functions for high/medium-freedom slides such as flow, before/after, layered architecture, decision map, table, or process lane.

## Package Validation

Before final handoff of a generated or modified `.pptx`, run equivalent checks:

- `unzip -t "<file>.pptx"`
- parse all XML files;
- verify every `[Content_Types].xml` override points to an existing part;
- verify every non-external relationship target resolves;
- scan slide XML for negative shape extents (`cx < 0` or `cy < 0`);
- check that expected media assets exist;
- check that source deck was not overwritten;
- export to PDF with LibreOffice when available and useful.

## PowerPoint Repair Signals

If PowerPoint reports repair or package validation finds suspicious structure, check:

- dangling content type overrides;
- missing relationship targets;
- missing media assets;
- invalid XML;
- negative shape extents;
- notes master/theme relationships;
- empty paired XML tags that PowerPoint canonicalizes;
- slide master/layout references that point to missing parts.

Fix package-level issues in a new output file unless the user approved in-place repair.

## Final Report

Report:

- source deck and output deck;
- manipulation strategy used;
- assets/layouts reused;
- content assumptions or open questions;
- validation commands run;
- residual manual checks needed in PowerPoint.
