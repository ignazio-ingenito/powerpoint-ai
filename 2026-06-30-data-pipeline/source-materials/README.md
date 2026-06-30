# Source Materials

Materiali raccolti per la presentazione `Data Pipeline Blueprint`.

## Provenienza

### `cdg-data-pipeline-repo/`

Snapshot selettivo non segreto da `/home/iingenito/projects/txt/cdg-data-pipeline`.

Contiene:

- `README.md`, `AGENTS.md`, `.env.example`
- `docker-compose.yaml`, `docker-compose.metabase.yaml`
- `docs/architecture/`
- `docs/specs/`
- `docs/status/`
- `docs/legacy/`
- `init/001_schema.sql`
- `init/002_stg_jira_views.sql`
- `init/003_tempo_issue_account_mart.sql`
- `dagster/ingestion.py`
- `dagster/repository.py`
- configurazioni runtime Dagster
- mapping YAML in `input/config/`

Escluso intenzionalmente:

- `.env`
- `.git/`
- cache Python
- output runtime
- credenziali e secret reali

### `cdg-data-pipeline-docs/`

Copia da `/home/iingenito/projects/txt/cdg-data-pipeline-docs`.

Contiene documenti storici e funzionali, inclusi:

- analisi funzionale processi CDG
- file Excel di analisi e campi
- project plan CDG migration
- XMind di processo
- deck `CDG Process Reengineering.pptx`
- archivio `v2.zip`

### `cdg-tools/`

Copia selettiva da `/home/iingenito/projects/txt/tools`.

Contiene:

- `New_CDG Migration_Project Plan.xlsx`
- `output.gantt`
- `xls2gantt.py`
- `rundeck-vs-dagster.md`

Uso previsto:

- ricostruire un macropiano CDG gia' espresso in forma Gantt;
- estrarre fasi, milestone e attivita' candidate per una slide piano;
- usare il confronto Rundeck/Dagster come spunto architetturale sull'orchestrazione, senza trattarlo come decisione definitiva.

### `obsidian-txt-novigo/`

Copia selettiva da:

`/mnt/c/Users/iingenito/OneDrive - TXT e-solutions S.p.A/Documents/Obsidian Vault/Domains/Work/TXT-Novigo`

Contiene:

- `CDG/`: appunti su processo CDG, estrazioni Jira/Tempo/Excel/gestionali e task infra.
- `ProSignal/`: appunti su file fixed-column, controlli, output regolamentari, retention e requisiti operativi.
- `context/`: appunti trasversali su AWS/data platform, Operations e DevOPS con segnali deboli su Kiron e principi architetturali.

Uso previsto:

- confrontare il caso CDG con un caso diverso di file-processing regolamentare;
- derivare requisiti comuni della blueprint: tracciati variabili, controlli, output, retention, audit e modalita' operative;
- mantenere separati appunti storici, inferenze e contenuti validati per slide.

## Note Di Uso

- Usare questi file come materiale sorgente, non come deliverable.
- Prima di usare nel deck contenuti sensibili o cliente-specifici, verificare permessi e contesto.
- Non trasformare dettagli implementativi in claim executive senza grounding e validazione.
