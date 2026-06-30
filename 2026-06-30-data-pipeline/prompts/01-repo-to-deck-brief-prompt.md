# Prompt - Repo To Deck Brief Data Pipeline Blueprint

Usa questo prompt per produrre il dossier `02-repo-to-deck-brief.md` partendo dai materiali raccolti in questa cartella progetto.

## Input

- Cartella progetto PowerPoint: `2026-06-30-data-pipeline/`
- Materiali sorgente:
  - `source-materials/cdg-data-pipeline-repo/`
  - `source-materials/cdg-data-pipeline-docs/`
  - `source-materials/cdg-tools/`
  - `source-materials/obsidian-txt-novigo/`
  - `drafts/01-source-inventory.md`
  - `drafts/02-chat-memory-findings.md`
  - `drafts/03-use-case-synthesis.md`
- Obiettivo di lavoro: blueprint per data pipeline riusabile su Kiron CDG, Internal CDG e ProSIGNAL.

## Istruzioni

Produci un dossier grounded, non un deck, seguendo `.codex/skills/repo-to-deck-brief/SKILL.md`.

Deve includere:

1. Executive summary.
2. Inventario fonti.
3. Contesto ed esigenza/obiettivi.
4. Cosa fa oggi il sistema CDG.
5. Come funziona a livello executive.
6. Cosa produce e come si osservano risultati/output.
7. Cosa rende ProSIGNAL un caso di stress test diverso da CDG.
8. Limiti AS IS e gap.
9. Blueprint TO BE riusabile.
10. Piano di lavoro.
11. Effort/team estimate solo se marcato come stima.
12. Benefici attesi solo se marcati come inferenze/assunzioni.
13. Economics drivers, non prezzi.
14. Rischi e punti aperti.
15. Proposta storyline.
16. Domande prima della creazione deck.

## Guardrail

- Non inventare materiale Kiron se non presente.
- Non inventare contenuti, informazioni, claim, esempi o dettagli non presenti nelle fonti, salvo richiesta esplicita di usare assunzioni.
- Se un documento, link o allegato citato non e' raggiungibile, non ricostruirne il contenuto: inserirlo tra i gap e chiedere all'utente di recuperarlo.
- Usare ProSIGNAL solo per quanto emerge dai markdown copiati, marcando come da riverificare il contesto dichiarato datato.
- Trattare Kiron CDG come caso target/candidato finche' non ci sono fonti specifiche.
- Non usare segreti, token, `.env` o dati live.
- Separare **Fatto confermato**, **Inferenza ragionata**, **Stima**, **Assunzione**, **Domanda aperta**.
- Non trasformare backlog tecnico in commitment.
- Non generare ancora PPTX.
