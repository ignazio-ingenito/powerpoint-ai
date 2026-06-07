---
name: commercial-deck-quality-review
description: Use before considering a commercial proposal or business-case deck complete. Review storyline, grounding, assumptions, executive clarity, visual consistency, and PowerPoint deliverable hygiene.
---

# Commercial Deck Quality Review

## Purpose

Review a deck against the repository's quality-first standard before final handoff.

Every final delivery must go through:

1. `Critic`: adversarial critique before formal acceptance.
2. `Review`: this quality review.
3. `Humanize`: final readability/naturalness pass on text-bearing artifacts.

If the critic or review pass finds material issues, fix them and repeat the relevant pass before handoff.

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
- explicit coverage of `Contesto / Esigenza / Obiettivi`, not only a generic context or pain-point slide;
- for POC/repo-derived decks, clear explanation of what the current solution does, how it works at executive level, what it produces, what its current limits are, and what it can evolve into;
- source grounding;
- unsupported claims;
- assumptions and open points;
- executive clarity;
- commercial tone;
- technical detail level;
- economics maturity;
- slide-by-slide readability;
- visual consistency with template/source deck;
- respect for creative handoff guardrails and declared `Creative freedom` level;
- concrete resemblance to selected `docs/ui/` reference patterns only where the slide is marked `Creative freedom: Low` or the user requested strict fidelity;
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
- POC/prototype initiatives do not skip the "what it is / how it works / what it produces / how it evolves" bridge in the name of brevity;
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
- `Contesto / Esigenza / Obiettivi` is explicit in the storyline/deck or the adaptation is documented;
- POC/repo-derived decks make the current asset understandable before asking for roadmap, funding, or business-case decisions;
- visual deviations from available `docs/ui/` patterns are acceptable for `High`/`Medium` slides when they preserve the handoff's message and guardrails;
- visual deviations on `Low` slides are documented and intentional;
- the final sequence `Critic -> Review -> Humanize` has been completed for the artifact being delivered;
- final response reports what was checked and what remains uncertain.
