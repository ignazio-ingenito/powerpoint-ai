---
name: repo-to-deck-brief
description: Use when analyzing a software repository to extract source-grounded material for a commercial proposal, business case, assessment, or executive deck.
---

# Repo To Deck Brief

## Purpose

Convert a software repository into a structured dossier that can feed the deck pipeline. The output is not a PowerPoint deck; it is a grounded brief for storyline, plan, effort, benefits, economics, and open questions.

## Required Reads

In this PowerPoint repo, read:

1. `AGENTS.md`
2. `.codex/deck-pipeline.md`
3. `.codex/authority.md`
4. `CONTEXT.md`
5. all `docs/reference*.md`
6. `prompt.repo-analysis-for-deck.md` when a reusable prompt artifact is useful

In the analyzed software repo, read fresh:

- `AGENTS.md` or equivalent agent instructions;
- `README*`;
- architecture docs, ADRs, specs, roadmap, deployment docs, issue templates;
- package/dependency manifests;
- source structure and high-level entry points.

Use GitNexus only if the analyzed repository supports it and the task benefits from code-intelligence. Do not use GitNexus for this PowerPoint repo's deck materials.

## Output Sections

Produce one Markdown dossier with:

1. Executive summary.
2. Source inventory.
3. Contesto ed esigenza/obiettivi.
4. AS IS.
5. TO BE.
6. Piano di lavoro.
7. Effort and team estimate.
8. Benefici attesi.
9. Economics drivers.
10. Risks and open points.
11. Proposed deck storyline.
12. Questions before deck creation.

## Evidence Rules

Label every important statement as one of:

- **Fatto confermato**
- **Inferenza ragionata**
- **Stima**
- **Assunzione**
- **Domanda aperta**

Never present inferred benefits, timelines, effort, or economics as commitments.

## Estimation Rules

Estimates are allowed when useful, but must include:

- range, not single-point commitment;
- rationale;
- drivers that could change the estimate;
- what needs validation.

Use tables for:

- phases and project plan;
- effort by role;
- benefits and validation method;
- economics drivers.

## Stop Conditions

Stop and ask before creating deck content if:

- project objective is unclear;
- target audience is unclear;
- repository purpose cannot be inferred;
- economics would require invented numbers;
- customer commitments or sensitive claims are involved.
