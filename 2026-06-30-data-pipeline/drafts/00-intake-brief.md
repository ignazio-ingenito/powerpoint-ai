# Data Pipeline Blueprint - Intake Brief

## Intake Brief

- **Deck type:** blueprint / proposta evolutiva interna per data pipeline riusabile.
- **Audience:** da confermare. Assunzione non bloccante per questa fase: management TXT/Novigo, IT/data stakeholders e owner dei progetti Kiron CDG, Internal CDG e ProSIGNAL.
- **Business objective:** definire una blueprint riusabile per costruire pipeline dati replicabili su piu' progetti, riducendo lavoro one-off e aumentando governance, tracciabilita' e riuso.
- **Presentation folder:** `2026-06-30-data-pipeline/`.
- **Standard subfolders:** presenti: `drafts/`, `prompts/`, `source-materials/`, `visual-references/`, `generated-assets/`, `attempts/`.
- **Source materials:** primo set raccolto in `source-materials/` da:
  - `/home/iingenito/projects/txt/cdg-data-pipeline`
  - `/home/iingenito/projects/txt/cdg-data-pipeline-docs`
  - `/mnt/c/Users/iingenito/OneDrive - TXT e-solutions S.p.A/Documents/Obsidian Vault/Domains/Work/TXT-Novigo`
- **Confirmed facts:**
  - Il repository `cdg-data-pipeline` descrive una pipeline dati per integrare Jira, Tempo e file Excel in MariaDB, orchestrata con Dagster.
  - Lo stack documentato include dlt, MariaDB, dbt come target per trasformazioni, Dagster, Metabase e NocoDB.
  - La convenzione dati e' a layer logici `raw_`, `ref_`, `stg_`, `mart_`.
  - Esistono job Dagster per ingestion Jira, Tempo, Jira+Tempo, refresh SQL, mart Jira/Tempo, ingestion Excel singola e ingestion Excel completa.
  - La documentazione CDG include materiale architetturale, specifiche Jira/Tempo, stato refactoring, legacy process e documenti storici in `cdg-data-pipeline-docs`.
  - Gli appunti Obsidian CDG descrivono processo operativo, estrazioni, campi Jira e task infrastrutturali.
  - `cdg-data-pipeline-docs` contiene analisi Internal CDG dettagliata su processi actual/forecast, fonti, tabelle guida e output P1-P6.
  - Gli appunti Obsidian ProSignal descrivono file fixed-column, controlli, grandi volumi, output regolamentari, retention e requisiti di editing/testo.
- **Critical gaps before storyline/deck:**
  - Audience primaria e livello di dettaglio: C-level, IT management, team delivery o comitato progetto.
  - Decisione che la presentazione deve abilitare: approvare una blueprint, finanziare industrializzazione, allineare architettura, vendere un servizio interno, o preparare una proposta cliente.
  - Perimetro blueprint: Internal CDG come reference implementation o pipeline generica anche per sorgenti ProSIGNAL e altri domini.
  - Materiale specifico Kiron CDG oltre al riferimento nominale.
  - Materiale ProSignal aggiornato: esempi file, tracciati, output e vincoli tecnici correnti.
  - Economics: se servono effort, costi, pricing o solo driver qualitativi.
- **Minor assumptions allowed for material recovery:**
  - Uso "data pipeline blueprint" come nome di lavoro.
  - Tratto `cdg-data-pipeline-docs` e `cdg-data-pipeline` come evidenze principali per Internal CDG.
  - Tratto Kiron CDG come caso target/candidato non ancora documentato.
  - Tratto ProSIGNAL come caso candidato con fonti iniziali ma da riverificare per anzianita' dell'analisi.
- **Material not to reuse directly:**
  - File `.env`, credenziali, token, secret e configurazioni runtime sensibili.
  - Contenuti tecnici che implichino accessi live o dati cliente senza verifica.
- **Recommended next step:**
  - Produrre il dossier `Repo to Deck Brief`, usando `drafts/01-source-inventory.md`, `drafts/02-chat-memory-findings.md` e `drafts/03-use-case-synthesis.md`, poi classificare i gap bloccanti prima della storyline.

## Assunzioni Usate Per Procedere

- Ho proceduto con scaffolding e recupero materiali perche' non richiedono ancora di fissare audience, economics o impegni.
- Non ho generato claim commerciali, stime o roadmap: questi dipendono dalle domande aperte sopra.
- Ho escluso file sensibili e credenziali dal materiale copiato.
