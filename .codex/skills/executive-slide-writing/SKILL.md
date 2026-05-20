---
name: executive-slide-writing
description: Use when writing or rewriting slide titles, executive summaries, C-level storyline, commercial messaging, assumptions, risks, benefits, or dense technical content for a business deck.
---

# Executive Slide Writing

## Purpose

Turn source material into concise, executive-ready slide language: clear message titles, short body text, business implications, explicit assumptions, and readable commercial framing.

## Required Reads

Read:

1. `AGENTS.md`
2. `CONTEXT.md`
3. `.codex/deck-pipeline.md`
4. `.codex/skills/business-case-storyline/SKILL.md`
5. all `docs/reference*.md`

## Writing Rules

- Write in Italian unless the user asks otherwise.
- Use a commercial, direct, C-level tone.
- Prefer message titles over section labels.
- Keep slide body text short.
- Tie technical details to business value, risk, time, quality, scalability, or economics.
- Separate facts, assumptions, estimates, risks, and open questions.
- Do not make unsupported benefits sound guaranteed.
- Move implementation detail to appendix when it distracts from the decision.
- If proceeding with assumptions, state them explicitly in the user-facing handoff as well as in the slide artifact.
- Do not label unasked questions as approval questions. Use "Open questions before PPTX" or "Questions to ask before next step" unless the questions were actually asked and answered.

## Title Pattern

Weak:

- `AS IS`
- `TO BE`
- `Architettura`
- `Piano`

Better:

- `L'attuale frammentazione limita controllo e scalabilità operativa`
- `La soluzione proposta abilita un percorso evolutivo governabile`
- `Il piano riduce il rischio con rilasci progressivi e validazione continua`

## Compression Pattern

When text is too dense:

1. Identify the decision the slide must support.
2. Keep one governing message.
3. Convert paragraphs into 3-5 bullets or 2-3 cards.
4. Move details, caveats, and implementation notes to appendix or speaker notes.
5. Preserve assumptions visibly.

## Output

For rewritten slide content, provide:

```markdown
## Slide Rewrite

- Section:
- Message title:
- Subtitle/key message:
- Body:
- Visual suggestion:
- Assumptions:
- Source basis:
```

## Quality Bar

A slide is ready when:

- the title communicates the implication;
- the body can be scanned in under 20 seconds;
- the reader understands why it matters;
- no unsupported claim appears as fact;
- the language is specific enough to be useful but not overloaded.
