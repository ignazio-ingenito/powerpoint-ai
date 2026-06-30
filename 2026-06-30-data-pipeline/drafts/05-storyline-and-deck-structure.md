# Storyline And Deck Structure - Data Pipeline Blueprint

> Stato: superata dalla nuova direzione documentata in `drafts/06-to-be-scenarios-planning-handoff.md`.
>
> Questa bozza resta utile come materiale preparatorio, ma la struttura corrente deve saltare l'AS IS autonomo e concentrarsi su due scenari TO BE: Dagster/dbt/Metabase e Talend/Qlik.

## Vincoli Operativi Aggiunti

Questi vincoli valgono per la prossima pianificazione, per il creative handoff e per l'eventuale produzione del deck.

### Output e fedelta' layout

- Provare prima a creare una presentazione PowerPoint il piu' possibile fedele al layout standard o consigliato nelle linee guida di Gianfranco e nel sistema visuale del repository.
- Usare come riferimento narrativo le linee guida `docs/reference*.md`, in particolare:
  - `Contesto / Esigenza / Obiettivi`;
  - TO BE;
  - Piano di lavoro;
  - Economics / benefici / limiti.
- Usare come riferimento visuale `docs/template.pptx`, `docs/template.pdf` se disponibile, `docs/ui/` e gli eventuali materiali visuali nella cartella progetto.
- Se non e' possibile produrre un PowerPoint editabile con fedelta' sufficiente, creare un output alternativo in immagini o PDF, chiarendo che sara' l'utente a trasferirlo manualmente in PowerPoint.
- Non salvare deliverable finali fuori dalla cartella `2026-06-30-data-pipeline/`.

### Direzione visuale

- Preferire infografiche, schemi architetturali, mappe di processo, matrici comparative e disegni esplicativi rispetto a lunghi blocchi di testo.
- Quando vengono generate immagini, salvare anche gli asset e gli artefatti usati per costruirle, in modo che la presentazione possa essere ricostruita o modificata in PowerPoint.
- Salvare asset e artefatti in `2026-06-30-data-pipeline/generated-assets/` o, se sono tentativi non finali, in `2026-06-30-data-pipeline/attempts/`.
- Per icone, diagrammi e immagini illustrative preferire formati vettoriali o PowerPoint-editable rispetto a bitmap raster, quando possibile.
- Usare bitmap solo quando l'asset deve restare visuale o non esiste un'alternativa vettoriale ragionevole.
- Mantenere tono professionale, look clean, leggibilita' alta e densita' controllata.

### Gate obbligatori su ogni piano

Ogni volta che viene definito o modificato un piano, una storyline, una struttura slide, un creative handoff o una strategia di deck, eseguire e documentare tre passaggi:

1. **grill-with-docs:** stressare il piano rispetto al linguaggio del repo, alle linee guida di Gianfranco, alle cinque sezioni standard e alle decisioni gia' documentate. Se emergono incoerenze, correggere il piano prima di procedere.
2. **Review:** verificare completezza, fonti, gap, claim non supportati, informazioni mancanti, aderenza alla richiesta utente e rischio di inventare contenuti.
3. **Humanize:** rendere i testi piu' leggibili, naturali e meno robotici senza cambiare fatti, assunzioni, vincoli o fonti.

### Esito grill-with-docs su questa modifica

- Le linee guida di Gianfranco richiedono cinque sezioni cardine, ma l'utente ha chiesto esplicitamente di saltare l'AS IS autonomo: la struttura resta accettabile solo se l'adattamento e' dichiarato e se `Contesto / Esigenza / Obiettivi`, `TO BE`, `Piano di lavoro` ed `Economics` restano visibili.
- La presentazione deve evitare un confronto puramente tecnico tra tool: il confronto Dagster/dbt/Metabase vs Talend/Qlik deve essere legato a valore, riuso, scalabilita', costi, rapidita', complessita' e blocker.
- La proiezione su Kiron CDG deve restare marcata come scenario/best practice finche' non arrivano fonti specifiche.
- Per claim su Talend, Qlik, Dagster, dbt, Metabase, cloud, licensing e deployment serve verifica aggiornata prima di testo definitivo.

## Scopo

Prima struttura narrativa della presentazione `Data Pipeline Blueprint`, basata sui materiali raccolti in:

- `drafts/00-intake-brief.md`
- `drafts/01-source-inventory.md`
- `drafts/02-chat-memory-findings.md`
- `drafts/03-use-case-synthesis.md`
- `drafts/04-internal-cdg-analysis.md`
- `source-materials/cdg-data-pipeline-repo/`
- `source-materials/cdg-data-pipeline-docs/`
- `source-materials/obsidian-txt-novigo/`

Questa bozza serve a validare storyline, sezioni e messaggi prima di passare a creative handoff o generazione PowerPoint.

## Posizionamento Proposto

La presentazione dovrebbe posizionare la blueprint come un modello operativo e tecnico riusabile per costruire pipeline dati governate, partendo da Internal CDG come caso sorgente e usando ProSignal come caso di stress test su file grandi, tracciati variabili e controlli regolamentari.

Kiron CDG puo' essere citato come beneficiario target o caso di riuso potenziale, ma non come caso documentato: al momento non ci sono fonti funzionali specifiche.

## Assunzioni Usate Per Procedere

- Audience provvisoria: management TXT/Novigo, IT/data stakeholder, owner CDG/ProSignal/Kiron.
- Obiettivo provvisorio: allineare una blueprint interna e decidere se industrializzarla, non vendere ancora una proposta cliente finale.
- Economics: in questa fase solo driver qualitativi e possibili leve di valore, non effort/prezzi/date.
- Internal CDG e CDG sono trattati come lo stesso caso sorgente principale, salvo diversa indicazione.
- ProSignal e' trattato come caso candidato con materiali iniziali ma da aggiornare.
- Kiron e' trattato come beneficiario target non ancora documentato.

## Domande Aperte Prima Del PPTX

1. La presentazione deve essere per C-level, IT management, PMO o team delivery?
2. La decisione richiesta e': approvare blueprint, finanziare industrializzazione, aprire fase di analisi, o preparare una proposta cliente?
3. ProSignal deve essere uno stress test architetturale o un secondo caso quasi pari a Internal CDG?
4. Vuoi includere una slide economics con stime qualitative, oppure solo benefici/driver senza numeri?
5. Esistono materiali Kiron CDG da recuperare prima di citarlo oltre il ruolo di beneficiario target?
6. Vuoi usare il deck `CDG Process Reengineering.pptx` come base visuale/contenutistica o solo come fonte interna sintetizzata?

## Struttura Consigliata

Formato consigliato: 12-14 slide, executive/technical blueprint.

La struttura segue le cinque sezioni standard:

1. Contesto ed esigenza/obiettivi
2. AS IS
3. TO BE
4. Piano di lavoro
5. Economics

## Proposed Storyline

| # | Section | Slide message | Role in the deck | Source basis | Assumptions / gaps |
|---|---|---|---|---|---|
| 1 | Cover | Data Pipeline Blueprint | Inquadra il tema come blueprint riusabile, non come singolo progetto CDG | Richiesta utente, folder progetto | Titolo finale da confermare |
| 2 | Contesto / Esigenza / Obiettivi | CDG e ProSignal mostrano lo stesso bisogno: trasformare dati eterogenei in output governati e ripetibili | Esplicita contesto, esigenza e obiettivi in una slide conforme allo standard | `03-use-case-synthesis.md`, `04-internal-cdg-analysis.md`, appunti ProSignal | Audience e decisione target da confermare |
| 3 | AS IS | Internal CDG oggi e' un processo dati ricco ma composto da molte fonti, mapping e controlli operativi | Fa capire la complessita' del caso sorgente | `Analisi funzionale processi CDG.docx`, `Analisi sequenza file.xlsx`, appunti CDG | Non usare valori o dati sensibili dai file Excel |
| 4 | AS IS | I processi P1-P6 rendono visibile il valore: ore, economics, integrazione SAP e forecast | Traduce l'analisi Internal CDG in mappa executive dei data product | `04-internal-cdg-analysis.md`, `Campi output.xlsx`, XMind Processi CDG | Dettaglio P1-P6 da tenere sintetico |
| 5 | AS IS / Bridge | La prima implementazione CDG dimostra il pattern tecnico: ingestion, raw/ref, staging, mart e BI | Ponte narrativo tra analisi funzionale e blueprint tecnica | repo `cdg-data-pipeline`, docs architecture/specs/status | Verificare allineamento tra docs e implementazione corrente prima del deck finale |
| 6 | AS IS / Reuse stress test | ProSignal introduce requisiti diversi: file fixed-column, grandi volumi, controlli e output regolamentari | Mostra perche' la blueprint deve generalizzare oltre Jira/Tempo | appunti ProSignal, AWS Summit note | Materiale ProSignal datato e da riconsiderare |
| 7 | TO BE | La blueprint separa motore dati, layer applicativo e strumenti di consumo | Presenta il principio architetturale chiave | `03-use-case-synthesis.md`, AWS Summit note, repo CDG | Evitare claim su tecnologie obbligatorie non decise |
| 8 | TO BE | Il modello riusabile organizza ogni iniziativa in source adapters, metadata, raw, staging, output e quality gates | Introduce il reference architecture blueprint | `03-use-case-synthesis.md`, `04-internal-cdg-analysis.md` | Decidere se chiamare `mart` o `output layer` per ProSignal |
| 9 | TO BE | La governance dei mapping e dei tracciati e' parte della pipeline, non un dettaglio operativo | Evidenzia reference data, schema registry, versioni tracciati e ownership | tabelle guida CDG, ProSignal tracciati modificabili | Nomi finali dei componenti da definire |
| 10 | TO BE | Controlli, audit e storicizzazione rendono la pipeline affidabile e difendibile | Converte dettagli tecnici in valore business/rischio | P1-P6, ProSignal header/tail, controlli scostamento, SLA/error objects da memoria | Non quantificare benefici senza metriche |
| 11 | Piano di lavoro | Il percorso parte da Internal CDG, valida ProSignal come stress test e poi abilita riusi come Kiron | Propone una roadmap progressiva | CDG Process Reengineering XMind/PPTX, `03-use-case-synthesis.md` | Date e effort da non inventare |
| 12 | Piano di lavoro | La delivery va organizzata per fasi: assessment, blueprint, reference implementation, pilot, rollout | Collega metodo PMO e progetto realizzabile | docs/reference, CDG macropiano, deck pipeline | Serve scelta se piano manageriale o più tecnico |
| 13 | Economics | Il valore atteso deriva da riduzione manualita', minore rischio operativo, riuso e maggiore auditabilita' | Sezione economics qualitativa senza pricing | CDG deck benefici, `03-use-case-synthesis.md` | Numeri e percentuali solo se confermati |
| 14 | Decision / Next steps | La decisione proposta e' validare la blueprint e recuperare i gap prima del deck operativo | Chiude con decisione e prossimi passi | gap inventory, domande aperte | Dipende dal tipo di audience |

## Slide Briefs

### 1. Data Pipeline Blueprint

- **Section:** Cover
- **Message title:** Data Pipeline Blueprint
- **Key message:** Modello riusabile per pipeline dati governate su Internal CDG, ProSignal e futuri casi target.
- **Mandatory content:** titolo, data, eventuale sottotitolo "Blueprint riusabile per iniziative data-intensive".
- **Source basis:** richiesta utente.
- **Assumptions:** titolo finale non ancora confermato.

### 2. CDG e ProSignal mostrano lo stesso bisogno: trasformare dati eterogenei in output governati e ripetibili

- **Section:** Contesto / Esigenza / Obiettivi
- **Contesto:** Internal CDG consolida dati granulari da fonti diverse fino a output gestionali; ProSignal lavora su file posizionali e controlli regolamentari.
- **Esigenza:** evitare pipeline one-off, manualita', controlli dispersi e dipendenza da file/processi non governati.
- **Obiettivi:** definire una blueprint riusabile, separare motore dati e layer applicativo, rendere controlli/output tracciabili e riapplicabili.
- **Source basis:** `04-internal-cdg-analysis.md`, appunti ProSignal, `03-use-case-synthesis.md`.
- **Assumptions:** presentazione orientata a decisione interna.

### 3. Internal CDG oggi e' un processo dati ricco ma composto da molte fonti, mapping e controlli operativi

- **Section:** AS IS
- **Body:** Mostrare le macro-fonti: Jira/Tempo, SAP, CDG app, organico, file ricavi/forecast, tabelle guida.
- **Executive implication:** la complessita' non e' solo tecnica: e' di controllo, responsabilita', dipendenze e qualita' del dato.
- **Source basis:** `Analisi funzionale processi CDG.docx`, `04-internal-cdg-analysis.md`.
- **Assumptions:** non entrare nel dettaglio di valori o mapping sensibili.

### 4. I processi P1-P6 rendono visibile il valore: ore, economics, integrazione SAP e forecast

- **Section:** AS IS
- **Body:** Mappare i sei output:
  - Actual ore mensile;
  - Actual ore inframensile;
  - Linked issue / ore secondarie;
  - Actual economics;
  - Ore SAP per integrazione economics;
  - Storico forecast.
- **Executive implication:** la pipeline deve produrre data product controllabili, non solo tabelle tecniche.
- **Source basis:** `04-internal-cdg-analysis.md`, `Campi output.xlsx`, `Processi CDG.xmind`.
- **Assumptions:** nomi output possono essere abbreviati in slide.

### 5. La prima implementazione CDG dimostra il pattern tecnico: ingestion, raw/ref, staging, mart e BI

- **Section:** AS IS / POC narrative bridge
- **Cosa fa oggi:** acquisisce Jira/Tempo/Excel, normalizza e produce mart/output BI.
- **Come lo fa:** Dagster orchestra job, dlt alimenta raw, SQL/dbt target supporta trasformazioni, Metabase/NocoDB supportano consumo e mapping.
- **Cosa produce:** raw/ref/stg/mart, mart Jira/Tempo, output controllabili.
- **Limiti:** allineamento documentazione/implementazione da verificare; alcune fonti operative non sono ancora incluse nei materiali copiati.
- **Source basis:** repo `cdg-data-pipeline`, docs architecture/specs/status, memoria CDG.
- **Assumptions:** non dichiarare production readiness oltre le fonti.

### 6. ProSignal introduce requisiti diversi: file fixed-column, grandi volumi, controlli e output regolamentari

- **Section:** AS IS / Reuse stress test
- **Body:** Evidenziare tracciati modificabili, file fino a 7 GB indicati negli appunti, upload manuale iniziale, header/tail, controlli di scostamento, output per vigilanza, retention output-oriented.
- **Executive implication:** una blueprint vera deve coprire anche file-processing e controlli, non solo API e BI.
- **Source basis:** appunti Obsidian ProSignal, `03-use-case-synthesis.md`.
- **Assumptions:** contesto ProSignal da aggiornare; non trasformare la nota in commitment.

### 7. La blueprint separa motore dati, layer applicativo e strumenti di consumo

- **Section:** TO BE
- **Body:** Il motore dati gestisce ingestion, parsing, trasformazioni, controlli e storicizzazione; i layer applicativi governano workflow/UI; BI e tool operativi consumano output stabili.
- **Executive implication:** riduce rischio di usare strumenti applicativi come motore di elaborazione per file grandi o processi ricorrenti.
- **Source basis:** AWS Summit note, `03-use-case-synthesis.md`, repo CDG.
- **Assumptions:** non prescrivere tecnologia cloud/vendor.

### 8. Il modello riusabile organizza ogni iniziativa in source adapters, metadata, raw, staging, output e quality gates

- **Section:** TO BE
- **Body:** Reference architecture:
  - source adapters;
  - metadata/schema registry;
  - raw/source-faithful layer;
  - staging semantic layer;
  - mart/output layer;
  - quality/audit gates;
  - consumption/workflow layer.
- **Executive implication:** i progetti cambiano sorgenti e regole, ma riusano struttura, controlli e metodo.
- **Source basis:** `03-use-case-synthesis.md`, `04-internal-cdg-analysis.md`.
- **Assumptions:** nomenclatura finale da consolidare.

### 9. La governance dei mapping e dei tracciati e' parte della pipeline, non un dettaglio operativo

- **Section:** TO BE
- **Body:** Reference data, tabelle guida, mapping account-WBS, validita' temporale, tracciati ProSignal, versioni e ownership.
- **Executive implication:** la qualita' della pipeline dipende dalla governance delle regole, non solo dal codice.
- **Source basis:** tabelle guida CDG, appunti ProSignal, CDG Process Reengineering.
- **Assumptions:** ownership dei mapping da confermare.

### 10. Controlli, audit e storicizzazione rendono la pipeline affidabile e difendibile

- **Section:** TO BE
- **Body:** Quadrature fonte vs output, gestione scarti, controlli linked issue/WBS, header/tail, scostamenti andamentali, run history, output storicizzati.
- **Executive implication:** il valore per management/compliance nasce dalla spiegabilita' del dato.
- **Source basis:** Internal CDG P1-P6, ProSignal notes, CDG Process Reengineering.
- **Assumptions:** non quantificare error reduction senza metriche.

### 11. Il percorso parte da Internal CDG, valida ProSignal come stress test e poi abilita riusi come Kiron

- **Section:** Piano di lavoro
- **Body:** Tre step:
  - consolidare Internal CDG come reference implementation;
  - validare la blueprint su ProSignal;
  - applicare la blueprint ad altri casi target, inclusa Kiron quando arrivano fonti specifiche.
- **Executive implication:** riduce il rischio per iterazioni e dimostra riuso su casi diversi.
- **Source basis:** CDG materials, ProSignal materials, Kiron references as weak signal.
- **Assumptions:** Kiron non e' ancora documentato.

### 12. La delivery va organizzata per fasi: assessment, blueprint, reference implementation, pilot, rollout

- **Section:** Piano di lavoro
- **Body:** Fasi candidate:
  1. Assessment fonti/processi;
  2. Blueprint e data contracts;
  3. Reference implementation Internal CDG;
  4. Pilot ProSignal;
  5. Governance, rollout e riuso.
- **Executive implication:** passaggio controllato da analisi a servizio riusabile.
- **Source basis:** docs/reference, CDG Process Reengineering XMind/PPTX, `03-use-case-synthesis.md`.
- **Assumptions:** niente date/effort senza input.

### 13. Il valore atteso deriva da riduzione manualita', minore rischio operativo, riuso e maggiore auditabilita'

- **Section:** Economics
- **Body:** Driver qualitativi:
  - meno lavoro ripetitivo su estrazioni e mapping;
  - meno rischio operativo da controlli manuali;
  - riuso su piu' iniziative;
  - tracciabilita' e audit;
  - scalabilita' per volumi e nuove sorgenti.
- **Source basis:** CDG deck benefici, Internal CDG needs, ProSignal needs.
- **Assumptions:** nessun numero finche' non viene autorizzata una stima o fornita metrica.

### 14. La decisione proposta e' validare la blueprint e recuperare i gap prima del deck operativo

- **Section:** Decision / Next steps
- **Body:** Decisione richiesta:
  - confermare audience e obiettivo;
  - recuperare materiali Kiron e ProSignal aggiornati;
  - decidere livello economics;
  - approvare passaggio a creative handoff/PPTX.
- **Source basis:** gap inventory e domande aperte.
- **Assumptions:** chiusura con call-to-action interna, non offerta cliente.

## Sezioni Da Non Saltare

- **Contesto / Esigenza / Obiettivi:** deve restare una slide esplicita.
- **Bridge POC/repo:** la slide 5 deve spiegare cosa fa oggi la pipeline CDG, come funziona, cosa produce, limiti ed evoluzione.
- **Economics:** anche se senza numeri, serve almeno una slide di driver economici/valore; altrimenti lo standard a cinque sezioni resta incompleto.

## Appendici Candidate

Se il deck supera 14 slide o serve un taglio piu' tecnico:

- A1. Dizionario input e output Internal CDG.
- A2. Mappa processi P1-P6.
- A3. Confronto CDG vs ProSignal.
- A4. Componenti tecnici CDG corrente.
- A5. Gap materiali e fonti da recuperare.

## Critic

- La storyline e' forte su Internal CDG, abbastanza fondata su ProSignal e debole su Kiron.
- La slide economics e' solo qualitativa: va bene per blueprint interna, non basta per business case con approvazione investimento.
- Il deck rischia di essere troppo tecnico se P1-P6 vengono descritti in dettaglio; vanno visualizzati come data product, non come specifica.
- Il claim di riuso va presentato come proposta/blueprint, non come fatto gia' dimostrato su Kiron.
- La scelta tecnologica non deve sembrare gia' vincolata a Dagster/dlt/dbt per ogni caso: questi sono pattern ed evidenze CDG, non standard aziendale approvato.

## Review

- Le cinque sezioni standard sono presenti.
- `Contesto / Esigenza / Obiettivi` e' esplicito.
- Il ponte repo/POC e' coperto dalla slide 5.
- Internal CDG e' correttamente trattato come caso sorgente principale.
- ProSignal e' trattato come stress test con fonti iniziali e caveat di aggiornamento.
- Kiron e' trattato come beneficiario target senza claim non supportati.
- Assunzioni e gap sono visibili.
- Non sono stati introdotti prezzi, date, commitment o metriche inventate.

## Humanize

La struttura racconta una progressione semplice: il controllo di gestione interno mostra il problema reale e documentato; ProSignal dimostra che il bisogno non e' limitato a Jira/Tempo; la blueprint propone un modo comune di trattare sorgenti, mapping, controlli, output e audit; il piano consente di validarla per passi prima di trasformarla in standard operativo.
