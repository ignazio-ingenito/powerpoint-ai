---
name: software-delivery-estimation
description: Use when estimating software-development delivery scope, phases, timeline, effort, roles, delivery risks, dependencies, MVP options, or project-plan assumptions for a proposal or business case.
---

# Software Delivery Estimation

## Purpose

Estimate the delivery side of a software project: delivery options, macro phases, roles, effort ranges, timeline, risks, dependencies, and assumptions.

This skill does not create pricing. It produces delivery estimates that may later inform the proposal's `Piano di lavoro` and `Economics` sections.

## Required Reads

Read:

1. `AGENTS.md`
2. `CONTEXT.md`
3. `.codex/deck-pipeline.md`
4. `.codex/skills/repo-to-deck-brief/SKILL.md` when the input is a software repository
5. `.codex/skills/business-case-storyline/SKILL.md`
6. all `docs/reference*.md`

Use task-specific source material: repo analysis, appunti, transcript, scope notes, architecture notes, backlog, or user clarifications.

When `docs/gantt.pdf` is available in this repository, use it as the reference pattern for executive project-plan shape: macro lanes, month columns, bars, milestones, releases, replanning points, and run/maintenance. Treat it as a visual/planning pattern, not as a source of project facts.

## Estimation Rules

- Use ranges, not single-point commitments.
- Mark every estimate as **stima da validare** unless the user provides confirmed delivery numbers.
- Separate confirmed scope from inferred scope.
- State the drivers that could change effort or timeline.
- Do not turn effort into price unless pricing rules or rates are provided.
- If the scope is too unclear, ask before estimating.
- For executive decks, express the project plan as a **macro Gantt-like plan**, not as a detailed WBS.
- Do not break the plan down into individual implementation tasks unless the user explicitly asks for an operational plan.
- Keep the **evolution roadmap** separate from the **implementation macro plan**. The roadmap explains product/capability strategy; the macro plan explains feasible delivery phases and indicative timing.

## Delivery Dimensions

Estimate:

- discovery / assessment;
- analysis and requirements;
- UX/UI or process design when relevant;
- architecture and technical design;
- frontend/backend/data/AI implementation;
- integrations;
- migration or data preparation;
- DevOps, environments, CI/CD;
- test, QA, UAT, validation;
- security/privacy hardening;
- rollout, training, hypercare;
- PM, governance, and coordination.

## Output

Produce:

```markdown
## Software Delivery Estimate

### Scope Basis
- Confirmed scope:
- Inferred scope:
- Out of scope:
- Open questions:

### Delivery Options
| Option | Positioning | Scope | Timeline range | Main trade-off |
|---|---|---|---:|---|

### Evolution Roadmap
Use this to explain the strategic evolution of the capability/product before the implementation plan.

| Evolution step | Strategic objective | Capabilities enabled | Expected value | Gate / prerequisite | Assumptions |
|---|---|---|---|---|---|

### Macro Project Plan
Use this as the basis for a Gantt-like slide, inspired by `docs/gantt.pdf` when available. Keep it macro-level: 3-4 lanes/phases and 6-10 macro items maximum. Use indicative ranges such as `Mese 2-3` when exact timing is not known.

| Lane/Phase | Macro item | Type | Indicative start | Indicative end | Output / milestone | Dependencies | Assumptions |
|---|---|---|---:|---:|---|---|---|

Use `Type` to distinguish `Bar`, `Milestone`, `Release`, `Run`, and `Replanning` where relevant.

### Effort By Role
| Role | Effort range | Phase | Rationale | Assumptions |
|---|---:|---|---|---|

### Delivery Risks
| Risk | Impact | Likelihood | Mitigation | Owner/input needed |
|---|---|---|---|---|

### Estimate Drivers
- ...
```

## Option Pattern

When useful, propose three delivery options:

- **MVP / quick win**: narrow scope, fast validation, lower certainty on full target state.
- **Phased rollout**: balanced path, release-based delivery, lower delivery risk.
- **Full scope**: broader implementation, more complete outcome, higher effort and dependency risk.

## Stop Conditions

Ask the user before estimating when:

- the product objective is unclear;
- the current system boundary is unknown;
- target capabilities are not inferable;
- integration count or complexity is central but unknown;
- migration, compliance, or security effort could dominate;
- the estimate would be used as a binding offer.
