---
name: business-case-storyline
description: Use when designing or reviewing the narrative structure of a TXT/Novigo commercial proposal or business case for a software-development project.
---

# Business Case Storyline

## Purpose

Build a clear executive storyline that turns project materials into a commercial/business-case proposal.

The standard deck must make a business reader understand:

- why change is needed;
- what the current state costs or limits;
- what the proposed future state enables;
- how delivery will happen;
- what the economics and assumptions are.

## Required Reads

Read fresh:

1. `AGENTS.md`
2. `.codex/deck-pipeline.md`
3. `CONTEXT.md`
4. all `docs/reference*.md`
5. task-specific source materials

## Mandatory Sections

Include these five sections unless the user explicitly approves an adaptation:

1. Contesto ed esigenza/obiettivi.
2. AS IS.
3. TO BE.
4. Piano di lavoro.
5. Economics.

## Software-Development Proposal Lens

For software-development projects, cover:

- current process/application/system landscape;
- pain points, risks, inefficiencies, or missed opportunities;
- proposed solution strategy;
- target capabilities and processes handled;
- architecture or integration view when useful;
- WBS or work packages;
- analysis, execution, validation, rollout, and governance;
- economics as range, assumption, or final offer depending on source maturity.

## Slide Title Rule

Prefer message titles over labels.

Weak:

- `AS IS`
- `TO BE`
- `Architecture`

Better:

- `L'attuale frammentazione applicativa limita scalabilità e controllo operativo`
- `La soluzione proposta concentra i processi chiave in una piattaforma evolutiva`
- `Il piano riduce il rischio con un percorso progressivo per release`

## Storyline Output

Before deck generation, produce:

```markdown
## Proposed Storyline

| # | Section | Slide message | Source basis | Assumptions |
|---|---|---|---|---|
```

Keep slides concise. Move implementation detail to appendix when it is not needed for executive decision-making.

## Quality Checks

The storyline is ready when:

- all five sections are represented or intentionally adapted;
- every slide has a role in the commercial argument;
- technical details are tied to business value, risk, time, or economics;
- assumptions are visible;
- no unsupported claim is phrased as fact;
- economics maturity is clear: range, LOI, estimate, or final offer.
- assumptions used to proceed have been disclosed to the user;
- unasked questions are labeled as open questions, not as approvals already requested.
