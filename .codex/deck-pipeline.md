# Quality-First Deck Pipeline

Status: Active
Authority Class: Repository Policy
Owner: Repository Owner
Scope: Pipeline for commercial proposals and business cases for software-development projects
Created: 2026-06-05
Last Reviewed: 2026-06-05
Review Cadence: Quarterly
Supersedes: None
Superseded By: None
Related Artifacts: AGENTS.md, .codex/routing.md, .codex/skills/*
Invalidation Triggers: new deck standard, new template, recurring quality failure, new deck type

# Goal

Produce editable, executive-ready PowerPoint proposals and business cases for software-development projects, grounded in supplied materials and visually coherent with TXT/Novigo references.

# Primary Output

The primary deliverable is a `.pptx` saved in the project root.

Optional outputs:

- `.pdf` export when requested;
- slide images or previews when requested;
- review notes or handoff notes when useful.

# Pipeline

## 1. Intake

Inventory all supplied materials:

- appunti;
- text documents;
- customer documents;
- images;
- transcripts;
- source decks;
- requested output filename;
- target audience;
- business objective;
- commercial constraints.

Classify missing information:

- critical gap: blocks storyline, value, scope, plan, economics, or customer commitment;
- minor gap: can be carried as an explicit assumption or validation point.

Critical gaps require questions before generation.

If Codex proceeds with minor assumptions, it must disclose them in the user-facing message before or during the step where they are used. Do not leave assumptions only inside the generated artifact.

Questions that were not actually asked must not be presented as approved gates. Label them as "questions to ask before the next step" or "open questions", and state whether Codex proceeded because they were non-blocking for the current phase.

When the input is a software repository, use `.codex/skills/repo-to-deck-brief/SKILL.md` before deck planning.

## 2. Grounding

Create a source-grounded brief:

- confirmed facts;
- likely implications;
- unsupported claims;
- assumptions allowed by the user;
- open questions;
- material that must not be reused.

Never use a reference deck as a source for new customer facts.

## 3. Storyline

Build the proposal around the five standard sections unless the user explicitly asks otherwise:

1. Contesto ed esigenza/obiettivi.
2. AS IS.
3. TO BE.
4. Piano di lavoro.
5. Economics.

For software-development projects, the TO BE should connect:

- proposed solution strategy;
- target architecture or application landscape;
- main capabilities/processes handled;
- delivery approach;
- operational and business impact.

Slide titles must state the message of the slide, not only the section label.

Use `.codex/skills/executive-slide-writing/SKILL.md` when drafting or compressing slide language.

For CEO, portfolio, or multi-initiative decks, apply a CEO-readiness pattern:

- avoid repeated slides unless each slide adds a new decision, evidence, or narrative step;
- use a visible navigator or recurring structure for macro-areas and initiatives;
- for each initiative, clarify current state, results achieved, next steps, value generated, open points, owner/funding when relevant;
- include sizing, timing, cost, benefit, or at least an explicit order-of-magnitude estimate when the slide asks for investment or prioritization;
- translate technical terms into business impact, risk, dependency, cost, or decision.

## 4. Visual Grounding

Before producing slides:

- read `docs/ui/README.md`;
- list actual files under `docs/ui/`;
- inspect relevant visual references;
- inspect `docs/template.pptx` when creating a new deck;
- inspect the source deck when revising one.

Use `.codex/skills/pptx-template-extraction/SKILL.md` when a reusable visual-system brief is needed.

Derive:

- slide grid and whitespace;
- title/header/footer conventions;
- palette and gradients;
- typography scale;
- card/table/process/architecture/economics patterns;
- icon usage.

Do not copy customer-specific content from visual references.

## 5. Plan

Before generating or heavily editing a deck, produce a short plan when the change affects storyline, economics, scope, or executive message.

The plan should include:

- proposed slide structure;
- section coverage;
- source mapping;
- assumptions;
- open questions;
- visual approach;
- validation criteria.

Ask for approval when the plan changes commercial positioning, economics, or scope.

Before moving from Markdown planning artifacts to PPTX generation, ask the user any remaining questions that affect audience, positioning, economics, baseline metrics, output fidelity, or customer-facing claims. Do not generate the PPTX while those questions are only listed inside an artifact.

For software-development estimates, use `.codex/skills/software-delivery-estimation/SKILL.md` to produce delivery phases, effort ranges, role mix, dependencies, risks, and estimate assumptions. These estimates are delivery inputs, not binding pricing.

## 6. Build

Create or update the `.pptx`:

- keep it editable in PowerPoint;
- use real text boxes, shapes, tables, connectors, and PowerPoint-native objects;
- use images only for visual assets;
- use `.codex/skills/powerpoint-manipulation/SKILL.md` for package inspection, editing, validation, repair, and export;
- prefer `pptxgenjs` for generated decks only when a generation script/dependency is intentionally added for the task;
- keep scripts under `scripts/`;
- save final deliverables in the project root.

Do not overwrite existing files without confirmation.

## 7. Verify

Run a focused quality review:

- storyline coverage;
- source grounding;
- assumptions and open questions;
- executive clarity;
- commercial tone;
- visual consistency;
- readability;
- package integrity;
- no accidental content copied from references;
- deliverable location and filename.

For generated `.pptx` files, validate package integrity when practical.

Use `.codex/skills/pptx-package-validation/SKILL.md` as the technical delivery gate for generated, repaired, or heavily modified `.pptx` files.

## 8. Handoff

Final response or handoff notes should include:

- output file path;
- major content decisions;
- assumptions left in the deck;
- open questions;
- validation performed;
- residual risks or manual PowerPoint checks needed.

# Quality Gates

## Gate A: Intake Complete

Passes when:

- material inventory is clear;
- target deck type and audience are clear;
- critical gaps have been asked or explicitly accepted by the user.
- assumptions used to proceed have been disclosed to the user, not only written in the artifact.

## Gate B: Storyline Grounded

Passes when:

- the five standard sections are present or intentionally adapted;
- each slide has a source or declared assumption;
- unsupported claims are removed or marked.
- repeated slides have been fused or justified;
- CEO-facing initiative slides state value, evidence, next steps, decision needs, and sizing/economics gaps.
- unasked questions are clearly labeled as open questions, not approval already obtained.

## Gate C: Visual System Applied

Passes when:

- visual references were inspected fresh;
- layout uses the template/source deck language;
- text remains readable;
- visual elements are editable where practical.

## Gate D: Deliverable Validated

Passes when:

- the output exists in root;
- PowerPoint package integrity is checked;
- remaining assumptions are explicit;
- final report lists validation and residual risk.
