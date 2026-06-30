# Context

Status: Active
Authority Class: Domain Glossary
Owner: Repository Owner
Scope: Glossary for TXT/Novigo deck-production work
Created: 2026-06-05
Last Reviewed: 2026-06-05
Review Cadence: Quarterly or when terminology changes
Supersedes: None
Superseded By: None
Related Artifacts: AGENTS.md, docs/reference.1.md, docs/reference.2.md, .codex/deck-pipeline.md
Invalidation Triggers: new deck family, new proposal methodology, changed PMO vocabulary

# Glossary

## Business Case

A commercial/executive presentation that explains why a proposed initiative is worth pursuing, connecting current pain, target state, delivery path, economics, assumptions, and expected business value.

## Proposta Commerciale

A customer-facing proposal deck intended to sell or position a project. It must be grounded in supplied material and must not invent customer facts, costs, dates, commitments, or scope.

## Software-Development Project

A project whose value is delivered through software, application evolution, system integration, workflow automation, data/application modernization, or a reusable platform/accelerator.

## Five Cardinal Sections

The mandatory proposal storyline sections defined by `docs/reference*.md`:

1. Contesto ed esigenza/obiettivi.
2. AS IS.
3. TO BE.
4. Piano di lavoro.
5. Economics.

They may be adapted to project complexity, but they must not disappear without an explicit reason.

## Contesto ed Esigenza

The opening narrative that explains why the project matters now, what business or operational need exists, and what objectives the proposal should satisfy.

## AS IS

The current situation before the proposed intervention. It may include architecture, systems, processes, criticalities, constraints, inefficiencies, risks, and missed opportunities.

For a POC or existing software asset, AS IS must also make the current asset understandable: what it does, how it works at executive level, what it produces, and what it does not yet cover.

## TO BE

The proposed future state after the intervention. It may include solution strategy, target architecture, new or changed systems, managed processes/functions, work breakdown, and key value elements.

For a POC or existing software asset, TO BE should explain the evolution path from current asset to reusable capability, customer application, business workflow, or governed service.

## POC Narrative Bridge

The mandatory explanatory bridge for decks derived from a POC, prototype, accelerator, or software repository.

It connects `Contesto ed esigenza/obiettivi` to `TO BE`, `Piano di Lavoro`, and `Economics` by explaining:

- what the asset does today;
- how it works at executive level;
- what it produces or makes measurable;
- its current limits;
- what it can evolve into.

It may be one or more slides, depending on deck length, but it must not disappear in the name of executive compression.

## Piano di Lavoro

The delivery path. At executive level it covers analysis, realization, validation, rollout, governance, and main milestones. At detailed level it may include releases, WBS links, activities, and dependencies.

## Economics

The economic framing of the proposal. It may be a range for LOI, a managerial business-case estimate, or a final offer with detailed scope, depending on source maturity.

## Grounding

The discipline of tying every material claim in the deck to supplied source material, user clarification, or explicit assumption.

## Critical Gap

A missing or ambiguous element that would cause Codex to invent or misrepresent business value, project scope, economics, dates, commitments, technology choices, or customer facts.

Critical gaps require user clarification before generation.

## Minor Assumption

A non-critical missing detail that can be carried in the deck as an explicit assumption or validation point without changing the commercial commitment.

## Visual Reference

A file under `docs/ui/`, `docs/template.pptx`, a presentation-folder `visual-references/` directory, or a source deck used to infer visual style, slide structure, layout, typography, palette, icons, cards, tables, diagrams, and density.

## Presentation Folder

A root-level folder named `yyyy-mm-dd-<project-name>/` that contains all material for one presentation. It must use the standard subfolders `drafts/`, `prompts/`, `source-materials/`, `visual-references/`, `generated-assets/`, and `attempts/`, plus final deliverables in the folder root unless a task explicitly chooses a subfolder.

Visual references are not content sources unless the user explicitly authorizes reuse.

## Editable PowerPoint

A `.pptx` where text, shapes, tables, and diagrams remain editable in PowerPoint where practical. Rasterized text should be avoided.

## Handoff

A final or interim note that records output files, decisions, assumptions, verification evidence, open questions, and residual risk. A handoff is not policy.
