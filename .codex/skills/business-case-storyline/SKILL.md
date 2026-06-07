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
- what the current POC/system actually does and produces, when the deck is based on one;
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

For section 1, do not collapse the requirement into a generic "context" slide. The storyline must explicitly show:

- `Contesto`: current situation and business rationale;
- `Esigenza`: need, pain, trigger, constraint, or opportunity;
- `Obiettivi`: decision or outcome the project/deck should enable.

In compact decks, these may be fused into one slide, but the slide title, labels, or body must make all three visible.

## POC / Repository Narrative Bridge

When source material is a POC, prototype, existing software repository, accelerator, or technical demonstrator, the storyline must include a concrete bridge between need and future-state proposal.

Before roadmap and economics, the deck must answer:

- `Cosa fa oggi`: what inputs it takes, what functions it performs, and what output it returns.
- `Come lo fa`: the operating flow or components, translated into business meaning rather than implementation jargon.
- `Cosa produce`: measurable or inspectable artifacts such as classifications, dates, facts, evidence, diagnostics, reports, run history, payloads, dashboards, or decisions.
- `Limiti attuali`: what is not yet covered, validated, production-ready, integrated, governed, or scalable.
- `Evoluzione`: what the POC can become and which customer/business use cases it enables.

For compact CEO decks, this bridge may be compressed into one slide named for example `Cosa fa la POC e come puo' evolvere`, but it must not disappear. Avoid storylines where the reader only sees "POC exists", KPI numbers, and then a roadmap without understanding the asset being evolved.

## Software-Development Proposal Lens

For software-development projects, cover:

- current process/application/system landscape;
- current POC/system function, mechanism, outputs, and limits when applicable;
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

For the first content slide, prefer a section label such as `Contesto / Esigenza / Obiettivi` or an equivalent message title that still exposes the three elements.

## Quality Checks

The storyline is ready when:

- all five sections are represented or intentionally adapted;
- the first section explicitly covers context, need, and objectives;
- POC/repo-derived decks explain what the current asset does, how it works, what it produces, its limits, and its evolution path;
- every slide has a role in the commercial argument;
- technical details are tied to business value, risk, time, or economics;
- assumptions are visible;
- no unsupported claim is phrased as fact;
- economics maturity is clear: range, LOI, estimate, or final offer.
- assumptions used to proceed have been disclosed to the user;
- unasked questions are labeled as open questions, not as approvals already requested.
