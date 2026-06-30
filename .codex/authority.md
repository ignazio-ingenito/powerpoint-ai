# Authority Model

Status: Active
Authority Class: Repository Policy
Owner: Repository Owner
Scope: Source priority for deck-production work
Created: 2026-06-05
Last Reviewed: 2026-06-05
Review Cadence: Quarterly
Supersedes: None
Superseded By: None
Related Artifacts: AGENTS.md, .codex/knowledge-map.md, .codex/governance.md
Invalidation Triggers: conflicting instructions, new source hierarchy, new client confidentiality rule

# Authority Order

For this repository, use this order:

1. System, developer, safety, sandbox, and tool instructions.
2. Current user instruction.
3. `AGENTS.md`.
4. `.codex/*.md` repository workflow policy.
5. `CONTEXT.md` for glossary terms.
6. `docs/reference*.md` for proposal method and storyline.
7. User-provided source material for the specific deck, including material stored in the relevant presentation folder.
8. `docs/template.pptx` for editable PowerPoint baseline and reusable structure.
9. `docs/ui/README.md` and files under `docs/ui/` for common visual reference.
10. Presentation-folder visual references, normally under `yyyy-mm-dd-<project-name>/visual-references/`.
11. Existing deck source when the task is to revise a specific deck.
12. Durable decisions in `docs/adr/`.
13. Accepted research in `docs/research/accepted/`.
14. Prompt examples, old handoffs, generated decks, and historical artifacts.

# Conflict Rules

- Higher authority beats lower authority.
- Newer does not automatically mean more authoritative.
- A reference deck is visual guidance, not permission to reuse customer-specific content.
- A generated deck is evidence of prior execution, not proof of standard.
- Handoffs are continuity notes, not policy.
- If tool-specific instructions conflict with `AGENTS.md`, follow `AGENTS.md` for this repository.
- If a user asks for a claim that is not grounded in source material, ask for source or mark it as an assumption only with explicit approval.

# Content Authorities

## Proposal Method

Primary:

- `docs/reference.1.md`
- `docs/reference.2.md`

These define the five required business-case sections and the expected commercial framing.

## Deck-Specific Content

Primary:

- user-provided appunti;
- text documents;
- images;
- transcripts;
- source decks;
- explicit user clarifications.

Rules:

- Do not invent facts.
- Do not promote assumptions into claims.
- Do not imply customer commitment from exploratory material.
- Separate confirmed content, assumptions, and open questions.

## Visual System

Primary:

- `docs/template.pptx`
- `docs/ui/README.md`
- current files under `docs/ui/`
- project-specific visual references under the relevant presentation folder
- source deck visual language when revising a deck.

Rules:

- Keep PowerPoint editable.
- Prefer real text boxes, shapes, tables, connectors, and PowerPoint-native objects.
- Use bitmap images only for visual assets that should remain visual.
- Do not recreate logos manually if an authoritative asset exists.

# Low-Authority Artifacts

Low authority artifacts may be useful for context but must not create policy:

- `.codex-work/` handoffs;
- temporary extraction files;
- generated previews;
- old prompt examples;
- unreviewed generated decks;
- draft plans not accepted by the user.
