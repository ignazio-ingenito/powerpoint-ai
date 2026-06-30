# Chat/Memory Findings

## Scope

Questa nota raccoglie informazioni utili emerse dalle chat e memorie locali accessibili.

Le evidenze qui sotto sono materiale di lavoro per la blueprint, non fonti finali da citare nel deck senza riverifica sui repository, documenti o ambienti originali.

## Evidenze Utili Per La Blueprint

- **Pattern raw/stg/mart gia' emerso su CDG:** il caso CDG usa una separazione netta tra layer source-faithful (`raw_*`), pulizia/esposizione BI (`stg_*`) e modello consumabile (`mart_*`). Questo e' il candidato piu' solido per diventare il backbone della blueprint riusabile.
- **Ingestion metadata-driven:** per Jira, i custom field non vanno trattati come ID statici (`customfield_*`) ma risolti tramite metadata/friendly name. Il principio riusabile e': importare e governare anche il catalogo campi, non solo i record transazionali.
- **Raw layer non deve diventare BI layer:** quando i payload contengono JSON complessi, campi opzionali o error objects, la normalizzazione va spostata in staging/mart. Il raw resta fedele alla sorgente per audit e diagnosi.
- **Job separati per modalita' operative diverse:** nelle memorie CDG compaiono job separati per ingestion, refresh SQL-only e refresh end-to-end. Per la blueprint questo diventa un principio operativo: ricalcolo rapido quando i dati sono gia' stati acquisiti, run completa quando serve aggiornare sorgenti e mart.
- **Gestione robusta dei campi opzionali:** dlt puo' omettere colonne raw se un campo e' sempre assente o nullo. La blueprint dovrebbe prevedere contratti minimi di schema, colonne opzionali nullable e controlli di drift.
- **Data quality spiegabile:** casi come SLA Jira rappresentati come error object non vanno nascosti. Devono diventare segnali distinguibili tra problema di contesto progetto, permessi, dato assente o trasformazione.
- **Scalabilita' Jira:** la paginazione via `nextPageToken` e il page size limitato rendono rischiosa una parallelizzazione generica. Le strategie candidate sono slicing per finestre temporali, account o progetto, guidate dalla distribuzione reale dei dati.
- **BI e strumenti di governo separati:** Metabase e NocoDB sono stati trattati come componenti con metadata DB separati. Il principio riusabile e': separare pipeline runtime, BI metadata e strumenti di manutenzione/reference data.
- **ProSignal come lead confermato:** le memorie indicavano folder o note `ProSignal` e `CDG` nel vault/import TXT Novigo. La verifica sul vault OneDrive ha confermato la presenza di markdown pertinenti, ora copiati in `source-materials/obsidian-txt-novigo/`.

## Implicazioni Narrative

La presentazione puo' posizionare la blueprint come capability replicabile, non come clone tecnico del caso CDG:

1. **Source adapters:** Jira, Tempo, Excel e futuri sistemi applicativi come ingressi governati.
2. **Ingestion contract:** metadata, schema opzionali, payload raw, retry e audit.
3. **Data layers:** raw source-faithful, staging semanticamente pulito, mart orientato a use case.
4. **Reference data governance:** mapping manuali o controllati via tool, con ownership chiara.
5. **Orchestration modes:** ingestion-only, transform-only, end-to-end, backfill mirati.
6. **Observability/data quality:** drift schema, campi mancanti, error objects, freshness, riconciliazioni.
7. **BI consumption:** Metabase o altri tool leggono mart stabili, non payload raw.
8. **Reuse model:** ogni nuovo progetto specializza source adapters, mapping e mart, mantenendo invariati i principi architetturali.

## Informazioni Ancora Deboli

- Non ho trovato, nelle memorie consultate, materiale sostanziale specifico su Kiron CDG.
- Le sole memorie non davano materiale sostanziale su Internal CDG, ma l'analisi successiva di `cdg-data-pipeline-docs` ha confermato una documentazione ricca e specifica sul controllo di gestione interno.
- ProSignal ora ha contenuti sorgente locali, ma l'analisi stessa segnala che parte del contesto risale a piu' di un anno e mezzo fa e va riconsiderato.
- GUBER/NOVA compare nello stesso inventario del vault/import, ma non e' tra i beneficiari dichiarati della blueprint in questa fase.

## Prossimo Recupero Materiali Consigliato

1. Cercare eventuali materiali Kiron in altri repository o SharePoint, perche' non sono emersi nel vault locale consultato.
2. Valutare se scaricare o esportare i documenti SharePoint linkati dagli appunti CDG/ProSignal.
3. Aggiornare questa nota distinguendo:
   - evidenze confermate da file;
   - inferenze derivate da chat/memoria;
   - punti aperti per il deck.
