# Governance

Status: Active
Authority Class: Repository Policy
Owner: Repository Owner
Scope: Lifecycle and maintenance of durable repository knowledge
Created: 2026-06-05
Last Reviewed: 2026-06-05
Review Cadence: Quarterly
Supersedes: None
Superseded By: None
Related Artifacts: .codex/authority.md, .codex/knowledge-map.md
Invalidation Triggers: new durable artifact type, stale deck standard, conflicting policy

# Artifact Classes

## Repository Policy

Files that define how agents must operate:

- `AGENTS.md`
- `.codex/adoption.md`
- `.codex/routing.md`
- `.codex/authority.md`
- `.codex/execution.md`
- `.codex/governance.md`
- `.codex/knowledge-map.md`
- `.codex/deck-pipeline.md`

Changes require careful review and consistency checks.

## Domain Glossary

`CONTEXT.md` defines domain terms only.

It must not become a spec, implementation plan, or dumping ground for prompts.

## Method References

`docs/reference*.md` define proposal method and expected storyline.

They are authoritative for content structure unless the user gives a task-specific exception.

## Visual References

`docs/template.pptx` and `docs/ui/` define visual style, layout, and baseline patterns.

They are not content sources unless the user explicitly authorizes reuse.

## Working Notes

`.codex-work/` stores ephemeral handoffs, verification notes, and temporary investigation notes.

Important findings must be promoted into durable docs when they affect future work.

# Lifecycle States

Use these states in durable docs when relevant:

- Draft: useful but not yet accepted.
- Active: currently authoritative.
- Superseded: replaced by a newer artifact.
- Archived: retained for history only.

# Required Header

Durable repository policy and decision files should include:

- Status
- Authority Class
- Owner
- Scope
- Created
- Last Reviewed
- Review Cadence
- Supersedes
- Superseded By
- Related Artifacts
- Invalidation Triggers

# Promotion Rules

Promote a working note into durable docs when it:

- changes the deck-production workflow;
- changes the content or visual standard;
- resolves a recurring ambiguity;
- defines a reusable quality gate;
- records a hard-to-reverse decision.

Do not promote:

- task-specific assumptions;
- one-off deck decisions;
- temporary extraction notes;
- unreviewed generated content.

# ADR Rules

Create an ADR under `docs/adr/` only when the decision is:

- hard to reverse;
- surprising without context;
- based on a real trade-off.

Do not create ADRs for simple file additions, obvious policy clarifications, or one-off deck choices.

# Maintenance

Review these periodically:

- whether `AGENTS.md` points to the right folders;
- whether `docs/ui/README.md` matches actual visual references;
- whether local skills duplicate or contradict global skills;
- whether generated scripts still match the current visual system.
