# Prompt - ChatGPT Search Data Pipeline Blueprint

Usa questo prompt in ChatGPT per cercare dentro chat, memoria e documenti disponibili materiale utile alla presentazione `2026-06-30-data-pipeline`.

```text
Devi aiutarmi a raccogliere materiale per una presentazione chiamata:

2026-06-30-data-pipeline

Obiettivo della presentazione:
creare una blueprint riusabile per data pipeline da applicare a piu' progetti, in particolare Kiron CDG, Internal CDG e ProSIGNAL.

Devi cercare dentro:
- le tue chat accessibili;
- la tua memoria;
- eventuali documenti disponibili nel workspace o nelle integrazioni a cui hai accesso;
- eventuali file o appunti che citano CDG, Kiron, ProSIGNAL, data pipeline, ingestion, controlli dati, file fixed-column, Jira, Tempo, Excel, Metabase, NocoDB, Dagster, dlt, dbt, Power BI, OutSystems, SharePoint, controlli regolamentari o segnalazioni di vigilanza.

Repository di destinazione:
ignazio-ingenito/powerpoint-ai

Cartella di destinazione:
2026-06-30-data-pipeline

Puoi committare e pushare sul repo tutto il materiale trovato, ma devi rispettare queste regole:

1. Non committare segreti, token, password, private key, `.env` reali, cookie, sessioni, link con token, URL SharePoint firmati o query string sensibili.
2. Se trovi link o riferimenti potenzialmente sensibili, redigili e conserva solo il fatto che esiste una fonte da recuperare.
3. Non committare dump dati, export operativi, file con dati cliente non selezionati o contenuti personali non pertinenti.
4. Se copi materiale, salvalo dentro `2026-06-30-data-pipeline/source-materials/`, mantenendo sottocartelle per fonte o progetto.
5. Se sintetizzi materiale da chat/memoria, salvalo in `2026-06-30-data-pipeline/drafts/`, indicando chiaramente che e' derivato da chat/memoria e va riverificato.
6. Se crei prompt, salvali in `2026-06-30-data-pipeline/prompts/`.
7. Non generare ancora PowerPoint o PDF: l'obiettivo e' recupero e classificazione fonti.
8. Non inventare contenuti, informazioni, claim, esempi o dettagli se non sono presenti nelle fonti trovate o se non te lo chiedo esplicitamente.
9. Se un documento, link, allegato, deck o file citato non e' raggiungibile, non ricostruirne il contenuto per inferenza: registralo come fonte mancante e chiedimi di recuperarlo o fornirlo.

Struttura standard della cartella progetto:
- drafts/
- prompts/
- source-materials/
- visual-references/
- generated-assets/
- attempts/

Se la struttura non esiste, creala.

Materiali gia' attesi o da cercare:

CDG / Internal CDG:
- pipeline Jira, Tempo, Excel;
- livelli raw/ref/stg/mart;
- Dagster jobs;
- dlt/dbt/MariaDB;
- Metabase, NocoDB, Power BI;
- mapping manuali, WBS, account, organico, dati gestionali;
- processi di controllo di gestione;
- project plan, Gantt, analisi funzionale, deck o XMind CDG.

ProSIGNAL:
- file testuali posizionali o fixed-column;
- file grandi, anche multi-GB;
- upload manuale iniziale;
- header/tail record;
- controlli di integrita';
- controlli di scostamento andamentale;
- aggregazioni per forma tecnica;
- output per segnalazioni di vigilanza;
- retention orientata agli output;
- editing testo/column mode;
- vincolo formato DOS vs UNIX;
- limiti OutSystems su file grandi;
- collaborazione WebGenesys o ING, se citata nei materiali.

Kiron CDG:
- qualsiasi appunto, deck, stima, proposta o riferimento operativo;
- se trovi solo riferimenti nominali, segnala che Kiron resta un beneficiario target non ancora documentato.

Query/keyword da usare:
- "Kiron"
- "Kiron CDG"
- "Internal CDG"
- "CDG"
- "controllo di gestione"
- "ProSignal"
- "PROSignal"
- "fixed column"
- "posizionale"
- "segnalazioni di vigilanza"
- "data pipeline"
- "Jira Tempo"
- "Dagster"
- "dlt"
- "dbt"
- "Metabase"
- "NocoDB"
- "Power BI"
- "OutSystems file grandi"
- "SharePoint CDG"
- "WebGenesys"

Output richiesti nel repo:

1. Aggiorna o crea:
   `2026-06-30-data-pipeline/drafts/chatgpt-source-inventory.md`

   Deve contenere:
   - fonte trovata;
   - tipo fonte: chat, memoria, documento, file, link redatto;
   - path locale se copiato;
   - cosa contiene;
   - autorita': alta/media/bassa;
   - rischio confidenzialita';
   - note su cosa va riverificato.

2. Aggiorna o crea:
   `2026-06-30-data-pipeline/drafts/chatgpt-findings.md`

   Deve separare:
   - fatti confermati da file/documenti;
   - evidenze da chat/memoria;
   - inferenze ragionate;
   - gap;
   - domande aperte prima della storyline.

3. Se trovi file utili e non sensibili, copiali in:
   `2026-06-30-data-pipeline/source-materials/chatgpt-collected/`

   Usa sottocartelle come:
   - `CDG/`
   - `ProSignal/`
   - `Kiron/`
   - `context/`

4. Se trovi solo riferimenti ma non puoi copiare i file, crea:
   `2026-06-30-data-pipeline/source-materials/chatgpt-collected/README.md`

   e documenta:
   - nome fonte;
   - dove si trova;
   - perche' non e' stata copiata;
   - azione necessaria per recuperarla.

Prima di committare:
- esegui una scansione per segreti e link sensibili;
- redigi link SharePoint o URL con token/query sensibili;
- verifica `git status --short`;
- assicurati che tutte le modifiche siano sotto `2026-06-30-data-pipeline/`.

Commit:
usa un Conventional Commit, ad esempio:

docs(data-pipeline): collect ChatGPT source findings

Push:
pusha sul repository `ignazio-ingenito/powerpoint-ai`.

Nel messaggio finale riportami:
- branch;
- commit hash;
- file creati/modificati;
- cosa hai trovato su CDG;
- cosa hai trovato su ProSIGNAL;
- cosa hai trovato su Kiron;
- cosa resta da recuperare;
- eventuali materiali esclusi per rischio segreti/confidenzialita'.
```
