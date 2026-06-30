# Prompt - TO BE Scenario Planning

Usa questo prompt per pianificare la nuova struttura della presentazione `2026-06-30-data-pipeline` dopo il cambio di direzione richiesto dall'utente.

```text
Devi aggiornare la pianificazione della presentazione Data Pipeline Blueprint.

Leggi prima:

- AGENTS.md
- .codex/deck-pipeline.md
- docs/reference*.md
- 2026-06-30-data-pipeline/drafts/06-to-be-scenarios-planning-handoff.md
- 2026-06-30-data-pipeline/drafts/01-source-inventory.md
- 2026-06-30-data-pipeline/drafts/03-use-case-synthesis.md
- 2026-06-30-data-pipeline/drafts/04-internal-cdg-analysis.md

Nuova direzione:

- Saltare la sezione AS IS come blocco autonomo.
- Costruire il TO BE intorno a due ipotesi:
  1. Dagster + dbt + Metabase
  2. Talend + Qlik
- Aprire con una slide di architettura logica/applicativa della buona pipeline.
- Creare una slide su parti comuni e introduzione ai due scenari.
- Per ogni scenario spiegare come ciascun componente della pipeline viene soddisfatto/eseguito.
- Per ogni scenario creare uno schema architetturale con cloud/zone/connessioni:
  - sorgenti;
  - ingestion/orchestrazione;
  - verifica dati/data quality;
  - manipolazione/preparazione;
  - trasformazioni;
  - mart/output;
  - presentation layer;
  - monitoring/audit.
- Evidenziare benefici, limiti, riuso, scalabilita', costi, rapidita'/complessita' e blocker.
- Proiettare le soluzioni su Kiron CDG, CDG interno e ING ProSIGNAL.
- Creare una WBS per ciascun progetto, spacchettata per processi e funzioni, stile XMind.
- Elaborare un piano di lavoro derivante dalle WBS, possibilmente comune ai tre progetti.

Regole:

- Non inventare contenuti o informazioni non presenti nelle fonti, salvo dove l'utente ha autorizzato l'uso di best practice.
- Quando usi best practice, dichiarale esplicitamente come best practice o ipotesi di lavoro.
- Kiron CDG ha ora fonti specifiche in `source-materials/cdg-kiron/`: trattarlo come caso documentato, marcando come ipotesi solo i dettagli non coperti o gli open point.
- ProSIGNAL ha fonti aggiornate dal vault, ma non esempi file/tracciati/output: segnalare i limiti come gap documentali, non inventare dettagli.
- Per Talend/Qlik, le fonti ufficiali Qlik indicano capability Qlik Talend Cloud nei piani Analytics e piani Qlik Talend Cloud separati: formulare i claim come scenario coerente, non come licenza pienamente confermata.
- Per claim su Talend, Qlik, Dagster, dbt, Metabase, cloud, licensing, costi, limiti e deployment, verificare documentazione aggiornata prima di scrivere affermazioni definitive.
- Non inventare prezzi, date, effort o commitment.

Produci questi artifact:

1. drafts/07-to-be-scenario-storyline.md
2. drafts/08-scenario-comparison.md
3. drafts/09-wbs-and-workplan.md
4. drafts/10-architecture-brief.md

Ogni artifact deve distinguere:

- fatti confermati;
- best practice / ipotesi di lavoro;
- inferenze ragionate;
- gap;
- domande aperte prima del PPTX.
```
