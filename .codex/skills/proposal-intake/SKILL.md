---
name: proposal-intake
description: Use at the start of any commercial proposal or business-case deck for software-development work. Inventory source materials, classify gaps, and decide whether Codex can proceed or must ask questions before drafting.
---

# Proposal Intake

## Purpose

Turn heterogeneous inputs into a grounded proposal brief before any storyline or slide work starts.

Inputs may include appunti, documents, images, transcripts, source decks, commercial notes, technical notes, and user clarifications.

## Required Reads

Read fresh:

1. `AGENTS.md`
2. `.codex/adoption.md`
3. `.codex/deck-pipeline.md`
4. `CONTEXT.md`
5. all `docs/reference*.md`

If visual work is part of the same task, also read `docs/ui/README.md` and list files under `docs/ui/`.

## Intake Checklist

Capture:

- deck type;
- target audience;
- business objective;
- customer or internal sponsor;
- project context;
- current situation;
- desired future state;
- proposed solution strategy;
- known technologies or constraints;
- delivery approach;
- milestones;
- economics;
- source materials available;
- confidentiality constraints;
- output filename and format.

## Gap Classification

Critical gaps block generation until clarified:

- customer/project identity when needed for the deck;
- business objective;
- scope and proposed solution direction;
- economics when economics will be presented as an offer or commitment;
- dates, milestones, effort, or commitments;
- permission to reuse sensitive/reference content;
- target audience when tone and detail level depend on it.

Minor gaps may proceed only as explicit assumptions:

- exact labels for non-critical workstreams;
- preliminary sequencing details;
- visual preference among available reference styles;
- wording of non-binding benefits;
- detail level for appendix material.

## Output

Produce a short intake brief:

```markdown
## Intake Brief

- Deck type:
- Audience:
- Business objective:
- Source materials:
- Confirmed facts:
- Critical gaps:
- Minor assumptions allowed:
- Material not to reuse:
- Recommended next step:
```

If critical gaps exist, ask focused questions before proceeding. Ask one question at a time when the answer affects storyline, economics, scope, or executive message.

If minor gaps do not block the current phase, Codex may proceed only by explicitly telling the user which assumptions are being used and why they are non-blocking. Do not hide these assumptions solely inside the generated artifact.

## Stop Conditions

Stop before drafting when:

- the value proposition is unclear;
- economics would be invented;
- the project scope is not inferable from sources;
- the deck could imply a customer commitment not present in the materials;
- confidential reuse permissions are unclear.
