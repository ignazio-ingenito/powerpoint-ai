---
name: commercial-deck-quality-review
description: Use before considering a commercial proposal or business-case deck complete. Review storyline, grounding, assumptions, executive clarity, visual consistency, and PowerPoint deliverable hygiene.
---

# Commercial Deck Quality Review

## Purpose

Review a deck against the repository's quality-first standard before final handoff.

## Required Reads

Read fresh:

1. `AGENTS.md`
2. `.codex/deck-pipeline.md`
3. `.codex/authority.md`
4. all `docs/reference*.md`
5. `docs/ui/README.md`

Inspect:

- the generated or revised `.pptx`;
- relevant source materials;
- visual references used.

## Review Dimensions

Assess:

- coverage of the five required sections;
- source grounding;
- unsupported claims;
- assumptions and open points;
- executive clarity;
- commercial tone;
- technical detail level;
- economics maturity;
- slide-by-slide readability;
- visual consistency with template/source deck;
- icon and card discipline;
- deliverable location and filename;
- package integrity.

Also check assumption disclosure:

- assumptions used to proceed were stated in the conversation or handoff, not only in the deck;
- unasked questions are not titled as "approval questions" unless the approval was actually requested from the user;
- any remaining questions that affect audience, economics, scope, baseline metrics, or customer-facing claims are raised before PPTX generation.

For CEO, portfolio, or multi-initiative decks, also check CEO readiness:

- no duplicate slide pair without a distinct role;
- navigator or recurring structure is present when the deck has multiple initiatives;
- initiative slides show visible results, not only activity descriptions;
- sizing, timing, costs, benefits, next steps, owner/funding, and open decisions are present or explicitly marked as gaps;
- technical terms are translated into business impact;
- project-detail slides are separated from strategic/portfolio slides when they do not support the executive decision.

## Findings Format

Lead with issues, ordered by severity:

```markdown
## Findings

- Critical:
- Major:
- Minor:

## Assumptions and Open Questions

- ...

## Validation Evidence

- ...

## Residual Risk

- ...
```

If there are no material issues, say so directly and still report residual risks or manual PowerPoint checks.

## Completion Bar

Do not call the deck complete unless:

- the file exists in the project root;
- it is a `.pptx` unless the user requested otherwise;
- package integrity has been checked where practical;
- assumptions are explicit;
- no critical grounding gap remains;
- final response reports what was checked and what remains uncertain.
