---
name: pptx-package-validation
description: Use before final delivery of a generated, repaired, merged, or modified .pptx file, especially when PowerPoint package integrity or open-without-repair behavior matters.
---

# PPTX Package Validation

## Purpose

Validate a `.pptx` as an Office Open XML package before claiming it is ready.

Use this as the technical gate. Use `commercial-deck-quality-review` for storyline and business quality.

## Required Reads

Read:

1. `.codex/execution.md`
2. `.codex/skills/powerpoint-manipulation/SKILL.md`

## Checks

Run equivalent checks for the target `.pptx`:

1. File exists in the project root unless explicitly requested otherwise.
2. `unzip -t "<file>.pptx"` passes.
3. Every XML file parses.
4. Every `[Content_Types].xml` override points to an existing part.
5. Every non-external `.rels` target resolves.
6. Expected media assets exist.
7. Slide XML has no negative extents (`cx < 0`, `cy < 0`).
8. No source deck was overwritten without approval.
9. LibreOffice PDF export passes when available and useful.
10. PowerPoint manual open-without-repair is requested when local automation cannot prove it.

## Failure Handling

If validation fails:

- do not call the deck ready;
- identify the failing package part;
- repair into a new file unless in-place repair was approved;
- rerun the full validation set after repair.

## Final Report

Report:

```markdown
## PPTX Validation

- File:
- unzip:
- XML parse:
- content types:
- relationships:
- media:
- negative extents:
- PDF export:
- PowerPoint manual check:
- Result:
- Residual risk:
```

## Common Risks

- Dangling content type overrides.
- Missing media targets.
- Relationship paths that resolve incorrectly from `_rels` folders.
- Negative extents from line shapes.
- Notes master/theme relationships that trigger PowerPoint repair.
- Successful LibreOffice export but PowerPoint repair warning still possible.
