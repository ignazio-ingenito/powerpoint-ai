# Planning Handoff - TO BE Scenarios

## Stato

Questo handoff recepisce il cambio di direzione richiesto dall'utente dopo la prima bozza di storyline.

Questo file e' il riferimento operativo piu' aggiornato per la prossima fase di pianificazione.

La struttura precedente in `drafts/05-storyline-and-deck-structure.md` resta come lavoro preparatorio/storico, ma non va usata come struttura corrente del deck senza adattamento.

Gli altri file in `drafts/` restano fonti di supporto:

- `00-intake-brief.md`: intake e assunzioni iniziali;
- `01-source-inventory.md`: inventario fonti;
- `02-chat-memory-findings.md`: evidenze da chat/memoria;
- `03-use-case-synthesis.md`: sintesi casi d'uso;
- `04-internal-cdg-analysis.md`: analisi Internal CDG;
- `05-storyline-and-deck-structure.md`: bozza superata, utile solo come materiale preparatorio.

## Nuova Direzione Confermata

Per questa presentazione il flusso standard del repo viene adattato in modo esplicito:

- **saltare la sezione AS IS** come blocco narrativo autonomo;
- concentrarsi su una **struttura TO BE comparativa**;
- presentare due ipotesi architetturali:
  1. pipeline con **Dagster + dbt + Metabase**;
  2. pipeline con **Talend + Qlik**;
- mantenere comunque:
  - `Contesto / Esigenza / Obiettivi`;
  - `TO BE`;
  - `Piano di lavoro`;
  - `Economics / benefici / limiti`;
  - proiezione sui tre casi target: **Kiron CDG**, **CDG interno**, **ING ProSIGNAL**.

## Decisioni Utente Del 2026-06-30

- **Discussione che il deck deve abilitare:** presentare al CEO, a Gianfranco, al CTO e al Tech Committee le due opzioni, mantenendo neutralita' comparativa, per aprire una discussione informata sull'adozione futura della blueprint.
- **Audience:** C-level / Gianfranco, CTO e Tech Committee.
- **Posizionamento del confronto:** restare neutrale tra le due ipotesi, evidenziando trade-off, criteri di valutazione e domande da discutere.
- **Scenario Talend/Qlik:** Talend e' considerato come opzione; ipotesi utente da verificare: Talend potrebbe essere compreso nella licenza Qlik. Target BI indicato: **Qlik Cloud Analytics Premium**.
- **Scenario Dagster/dbt/Metabase:** target cloud **AWS**. Compute candidato: **ECS o EC2**, non EKS. Database: **RDS o database cliente**, in funzione della volonta' del cliente e del modello di hosting.
- **Priorita' casi target:** ProSIGNAL e Kiron sono clienti esterni e hanno priorita' rispetto al CDG interno.
- **Economics:** non entrare in dettaglio; fornire una prima idea dei costi come range e driver, coerente con una blueprint.
- **Metodo:** produrre gli artifact intermedi che migliorano il risultato prima di passare al PowerPoint.

## Guardrail

- Non inventare contenuti o informazioni non presenti nelle fonti, salvo dove l'utente ha autorizzato l'uso di best practice.
- Dove si usano best practice o scenari comuni, marcarli esplicitamente come `Best practice / ipotesi di lavoro`, non come fatto cliente.
- Se un documento, allegato o fonte citata non e' raggiungibile, chiedere all'utente di recuperarlo.
- Per Talend, Qlik, Dagster, dbt, Metabase, cloud, pricing, licenze, limiti e deployment, verificare documentazione aggiornata prima di trasformare il contenuto in claim.
- Non inventare costi, effort, date o commitment.
- Kiron CDG ha ora materiali specifici in `source-materials/cdg-kiron/`: analisi funzionale, campi input/output, tabelle guida e regole. Non va piu' trattato come caso solo ipotetico.
- ProSIGNAL ha materiali aggiornati nel vault indicato dall'utente e gia' copiati nel progetto; usare comunque cautela perche' il contenuto funzionale storico dichiara analisi da riconsiderare e mancano esempi file/tracciati/output.
- Per ogni definizione o modifica del piano eseguire `grill-with-docs`, `Review` e `Humanize` prima di considerare l'artifact pronto.
- Il primo obiettivo di delivery e' un PowerPoint editabile, il piu' fedele possibile al layout standard/consigliato dalle linee guida di Gianfranco e dai riferimenti visuali del repo.
- Se non e' possibile produrre un PowerPoint editabile con fedelta' sufficiente, produrre immagini o PDF come alternativa, esplicitando che l'assemblaggio finale in PowerPoint sara' manuale.

## Direzione Visuale

- Preferire infografiche, schemi architetturali, mappe di processo, matrici comparative e disegni esplicativi rispetto a lunghi blocchi di testo.
- Quando vengono generate immagini, salvare anche gli asset e gli artefatti usati per costruirle, in modo che la presentazione possa essere ricostruita o modificata in PowerPoint.
- Salvare asset e artefatti in `2026-06-30-data-pipeline/generated-assets/` o, se sono tentativi non finali, in `2026-06-30-data-pipeline/attempts/`.
- Per icone, diagrammi e immagini illustrative preferire formati vettoriali o PowerPoint-editable rispetto a bitmap raster, quando possibile.
- Usare bitmap solo quando l'asset deve restare visuale o non esiste un'alternativa vettoriale ragionevole.
- Mantenere tono professionale, look clean, leggibilita' alta e densita' controllata.

## Nuova Struttura Narrativa Richiesta

### 1. Apertura: componenti di una buona pipeline

Creare una prima slide TO BE di architettura logica/applicativa che rappresenti le componenti di una pipeline dati robusta.

Componenti da includere, da rifinire:

- ingestion;
- validazione/verifica dei dati;
- data quality e controlli;
- parsing/manipolazione;
- normalizzazione e preparazione;
- trasformazioni;
- costruzione dei mart/output data product;
- storicizzazione/audit;
- orchestrazione e monitoraggio;
- esposizione/presentation layer;
- governance di mapping, tracciati, metadati e ownership.

La slide deve spiegare il modello concettuale prima di parlare degli strumenti.

### 2. Parti comuni e introduzione ai due scenari

Creare una slide che evidenzi:

- parti comuni concettuali;
- parti comuni eventualmente pratiche;
- cosa cambia davvero tra le due ipotesi;
- criteri di confronto.

Possibili parti comuni:

- sorgenti dati e file;
- data contracts e tracciati;
- mapping/reference data;
- quality gates;
- storicizzazione e audit;
- output/mart;
- consumo BI;
- governance operativa.

Possibili criteri di confronto:

- riuso;
- scalabilita';
- costi/licensing;
- rapidita' di realizzazione;
- complessita' di implementazione;
- skill richieste;
- lock-in;
- operating model;
- blocker e dipendenze.

### 3. Scenario A - Dagster + dbt + Metabase

Descrivere come ogni componente della pipeline viene soddisfatta nello scenario open/data-engineering oriented.

Stack indicativo:

- Dagster per orchestrazione, job/asset, scheduling, observability operativa;
- dbt per trasformazioni, modellazione, test e lineage logico;
- Metabase per presentation layer/dashboard;
- database/warehouse da definire;
- compute AWS per esecuzione pipeline;
- eventuale storage/object storage e database per raw/staging/mart.

Richiesto:

- slide di mapping componenti -> strumenti;
- schema architetturale con cloud/zone/connessioni:
  - sorgenti;
  - ingestion/orchestration compute;
  - storage/db;
  - transformation layer;
  - mart/output;
  - presentation/Metabase;
  - monitoring/logging.
- evidenziare benefici;
- evidenziare limiti;
- valutare riuso, scalabilita', costi, rapidita'/complessita' e blocker.

### 4. Scenario B - Talend + Qlik

Descrivere come ogni componente della pipeline viene soddisfatta nello scenario enterprise/data-integration + BI.

Stack indicativo:

- Talend per ingestion, integrazione, trasformazione e data quality/data integration;
- Qlik per analytics/presentation e possibile cloud presentation layer;
- cloud Qlik dove pertinente;
- database/warehouse/storage da definire;
- compute o runtime Talend da chiarire.

Richiesto:

- slide di mapping componenti -> strumenti;
- schema architetturale con cloud/zone/connessioni:
  - sorgenti;
  - Talend/runtime;
  - storage/db;
  - trasformazioni/quality;
  - mart/output;
  - Qlik Cloud / presentation;
  - monitoring/governance.
- evidenziare benefici;
- evidenziare limiti;
- valutare riuso, scalabilita', costi, rapidita'/complessita' e blocker.

### 5. Confronto tra scenari

Creare una slide comparativa sintetica.

Dimensioni minime:

- riuso;
- scalabilita';
- costi/licensing;
- rapidita' di realizzazione;
- complessita' di realizzazione;
- gestione operativa;
- competenze necessarie;
- blocker;
- fit con i tre casi target.

Non assegnare punteggi numerici se non richiesti o se non ci sono fonti.

### 6. Proiezione sui tre casi target

Applicare i due scenari a:

1. **Kiron CDG**
2. **CDG interno**
3. **ING ProSIGNAL**

Per ogni caso:

- indicare fit dello scenario Dagster/dbt/Metabase;
- indicare fit dello scenario Talend/Qlik;
- evidenziare cosa e' comune;
- evidenziare cosa cambia;
- evidenziare gap informativi;
- non inventare dettagli specifici non disponibili.

## WBS Richiesta

Per ogni progetto creare una WBS, spacchettata per processi e funzioni in stile XMind.

Progetti:

- Kiron CDG;
- CDG interno;
- ING ProSIGNAL.

Regola di grounding:

- per CDG interno usare fonti gia' disponibili (`04-internal-cdg-analysis.md`, `cdg-data-pipeline-docs`, repo `cdg-data-pipeline`);
- per ING ProSIGNAL usare gli appunti del vault indicato dall'utente e best practice dichiarate dove manca dettaglio;
- per Kiron CDG usare i materiali specifici in `source-materials/cdg-kiron/`, marcando come ipotesi solo i dettagli non coperti o gli open point.

Formato consigliato WBS:

```text
Progetto
  Area / Processo
    Funzione
      Attivita' / capability
```

### WBS - CDG interno

Base da fonti:

- P1 Actual Ore Mensile;
- P2 Actual Ore Inframensile;
- P3 Linked Issue / Ore secondarie;
- P4 Actual Economics;
- P5 Ore SAP per integrazione Economics;
- P6 Forecast;
- governance mapping/tabelle guida;
- dashboard CDG e dashboard tecnica;
- controlli/quadrature/audit;
- orchestrazione e monitoraggio.

### WBS - ING ProSIGNAL

Base da appunti + best practice dichiarate:

- gestione tracciati fixed-column;
- upload/ingestion file;
- parsing e validazione formato;
- header/tail/integrity checks;
- aggregazioni e controlli andamentali;
- controlli incrociati file decadali;
- manipolazione/export;
- output per segnalazioni;
- retention output-oriented;
- editor/testo/column mode o funzioni equivalenti.

### WBS - Kiron CDG

Base da `source-materials/cdg-kiron/`:

- assessment fonti CDG;
- ingestion dati gestionali;
- mapping account/WBS/commesse;
- normalizzazione ore/economics;
- controlli e quadrature;
- mart/reporting;
- dashboard;
- governance e run operativo.

## Piano Di Lavoro Richiesto

Elaborare un piano di lavoro derivante dalle WBS, se possibile comune ai tre progetti.

Fasi candidate comuni:

1. **Assessment e perimetro**
   - fonti, processi, output, vincoli, ownership.
2. **Blueprint e data contracts**
   - componenti comuni, tracciati, mapping, regole, controlli.
3. **Setup architetturale**
   - cloud/runtime, database/storage, ambienti, accessi, monitoraggio.
4. **Ingestion e raw/source-faithful layer**
   - connettori, file/API, landing, audit.
5. **Validazione, parsing e data quality**
   - controlli formato, integrita', scarti, anomalie.
6. **Transform/preparation/mart**
   - normalizzazione, arricchimento, mart/output.
7. **Presentation e workflow**
   - dashboard, export, strumenti operativi.
8. **Test, parallel run e quadrature**
   - periodo campione, confronto output, riconciliazione.
9. **Go-live e hypercare**
   - run operativo, formazione, supporto primo ciclo.
10. **Riuso e industrializzazione**
   - standard componenti, template, backlog evolutivo.

## Artifact Da Produrre Nel Prossimo Step

Prima del PPTX, produrre:

1. `drafts/07-to-be-scenario-storyline.md`
   - nuova storyline senza AS IS autonomo;
   - struttura slide aggiornata;
   - due scenari;
   - proiezione sui tre casi.

2. `drafts/08-scenario-comparison.md`
   - confronto Dagster/dbt/Metabase vs Talend/Qlik;
   - benefici/limiti/blocker;
   - parti comuni.

3. `drafts/09-wbs-and-workplan.md`
   - WBS per Kiron CDG, CDG interno, ING ProSIGNAL;
   - piano di lavoro comune derivato.

4. `drafts/10-architecture-brief.md`
   - componenti logiche pipeline;
   - schema architetturale testuale per i due scenari;
   - note per visualizzazione in slide.

## Informazioni Da Verificare Prima Di Scrivere Claim

- Deployment e licensing Talend attuali.
- Deployment e licensing Qlik/Qlik Cloud attuali.
- Limiti applicabili a tenant/licenze e contesto cliente per Qlik/Talend, Dagster/dbt/Metabase e deployment cloud.
- Scelta database/warehouse per entrambi gli scenari.
- Se la pipeline Dagster/dbt/Metabase deve essere tutta su AWS o mista.
- Se Talend/Qlik e' gia' disponibile internamente o va considerato come nuovo stack/licenza.
- Chiarimenti Kiron su regole/open point ancora da definire nel materiale sorgente.
- Esempi file/tracciati/output ING ProSIGNAL e allegati SharePoint autorizzati; le note aggiornate del vault sono gia' state acquisite.
