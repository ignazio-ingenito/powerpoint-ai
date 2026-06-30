# TO BE Scenario Storyline

## Scopo

Nuova storyline della presentazione `Data Pipeline Blueprint`, aggiornata dopo le decisioni utente del 2026-06-30.

Questa versione salta l'AS IS come sezione autonoma e costruisce il deck intorno a due scenari TO BE:

1. **Dagster + dbt + Metabase su AWS**
2. **Talend + Qlik Cloud Analytics Premium**

## Discussione Che Il Deck Deve Abilitare

Presentare a CEO / Gianfranco, CTO e Tech Committee le due opzioni architetturali per aprire una discussione informata, neutrale e motivata sull'adozione futura di una data pipeline blueprint:

- ING ProSIGNAL;
- Kiron CDG;
- CDG interno;
- altri progetti analoghi.

## Posizionamento Narrativo

La presentazione non deve vendere una tecnologia e non deve chiudere la decisione. Deve mettere il comitato nelle condizioni di discutere in modo strutturato i due modelli possibili.

Il confronto deve essere leggibile per C-level e Tech Committee:

- abbastanza executive da chiarire valore, rischio e costi;
- abbastanza tecnico da rendere credibile il confronto;
- neutrale tra le due ipotesi;
- orientato a riuso su progetti futuri.

## Assunzioni E Grounding

### Fatti / decisioni confermate dall'utente

- Audience: CEO / Gianfranco, CTO, Tech Committee.
- Confronto neutrale tra due opzioni.
- ProSIGNAL e Kiron hanno priorita' rispetto al CDG interno perche' clienti esterni.
- Scenario AWS: ECS o EC2 come compute candidati; no EKS.
- Scenario database AWS: RDS o database cliente, in funzione della scelta del cliente.
- Scenario Metabase: per questa fase si assume che Metabase possa essere accettato dal cliente come layer BI/presentation.
- Scenario Qlik: usare Qlik Cloud Analytics Premium come target.
- Economics: range e driver di costo, non dettaglio di offerta.

### Best practice / ipotesi di lavoro

- Kiron CDG e' trattato come caso documentato grazie ai materiali in `source-materials/cdg-kiron/`.
- Per ProSIGNAL si usano gli appunti aggiornati nel vault indicato dall'utente e pattern comuni di file ingestion / regulatory data processing.
- Per la WBS Kiron e ProSIGNAL, dove manca dettaglio, si usano scenari comuni marcati come ipotesi.

### Da verificare prima del PPTX finale

- Licensing e packaging attuali Talend/Qlik, in particolare cosa include davvero Qlik Cloud Analytics Premium.
- Cost range indicativi: infrastruttura, licenze/subscription, delivery, run.
- Chiarimenti Kiron su regole/open point ancora da definire nel materiale sorgente.
- Esempi file/tracciati/output ING ProSIGNAL, soprattutto Lease e Conto Arancio, se disponibili e autorizzati.
- Requisiti specifici di access control, publishing, embedding/export e governance BI per Metabase, se richiesti dai clienti.
- Fit Qlik/Talend su file grandi, fixed-column e controlli cross-file per ProSIGNAL.

## Struttura Slide Proposta

| # | Sezione | Messaggio slide | Ruolo | Fonti / grounding | Note |
|---|---|---|---|---|---|
| 1 | Cover | Data Pipeline Blueprint | Apertura istituzionale | richiesta utente | Look clean, titolo forte |
| 2 | Contesto / Esigenza / Obiettivi | La discussione non riguarda un singolo progetto, ma una blueprint da riusare su piu' iniziative data-intensive | Spiega perche' serve allineamento ora | decisioni utente, `03-use-case-synthesis.md` | Citare ProSIGNAL, Kiron, CDG interno |
| 3 | TO BE | Una buona pipeline separa ingestion, controlli, trasformazioni, mart e presentation layer | Prima slide logica/applicativa | `03-use-case-synthesis.md`, `04-internal-cdg-analysis.md` | Infografica componenti, non testo lungo |
| 4 | TO BE | Le due opzioni condividono principi e differiscono nel modello operativo | Introduce le due ipotesi | `06`, decisioni utente | Slide parti comuni + differenze |
| 5 | Scenario A | Dagster + dbt + Metabase privilegia controllo ingegneristico, componibilita' e deployment AWS | Presenta scenario A | repo CDG, decisioni AWS utente | Da verificare con docs aggiornate |
| 6 | Scenario A | Nello scenario AWS ogni componente della pipeline resta esplicita e governabile | Mapping componenti -> tool | `06`, repo CDG | Matrice o swimlane |
| 7 | Scenario A | Architettura logica AWS: sorgenti, compute ECS/EC2, database, trasformazioni, mart, Metabase | Schema architetturale | decisioni utente, best practice AWS | No EKS; DB cliente/RDS |
| 8 | Scenario A | Benefici e limiti dello scenario AWS/open stack | Trade-off scenario A | best practice marcata | Range costi solo qualitativi |
| 9 | Scenario B | Talend + Qlik privilegia integrazione enterprise e analytics gestita | Presenta scenario B | decisioni utente | Claim licensing da verificare |
| 10 | Scenario B | Nello scenario Talend/Qlik ingestion, quality e analytics sono concentrati in una filiera piu' product-oriented | Mapping componenti -> tool | `06`, best practice marcata | Verificare confini Talend/Qlik |
| 11 | Scenario B | Architettura logica Talend/Qlik: runtime integrazione, storage/db, Qlik Cloud presentation | Schema architetturale | decisioni utente | Runtime Talend da chiarire |
| 12 | Scenario B | Benefici e limiti dello scenario Talend/Qlik | Trade-off scenario B | best practice marcata | Evidenziare licensing/lock-in |
| 13 | Confronto | I trade-off principali riguardano riuso, scalabilita', costi, velocita', complessita' e modello operativo | Matrice comparativa | decisioni utente | Neutrale, senza vincitore predefinito |
| 14 | Proiezione casi | ProSIGNAL e Kiron guidano la priorita', CDG interno consolida la reference implementation | Applica i due scenari ai tre casi | `03`, `04`, appunti ProSignal, decisioni utente | ProSIGNAL/Kiron sopra CDG interno |
| 15 | WBS | Le WBS dei tre progetti condividono una spina dorsale comune, ma cambiano sorgenti e controlli | Introduce WBS/processi/funzioni | `09-wbs-and-workplan.md` | Mappa tipo XMind |
| 16 | Piano | Un piano comune riduce rischio e abilita riuso progressivo | Piano comune da WBS | `09-wbs-and-workplan.md` | Niente date inventate |
| 17 | Economics | Per una blueprint servono range e driver, non una quotazione definitiva | Economics qualitativo/range | decisione utente | Suggerire range macro, da stimare |
| 18 | Discussione | Il comitato deve discutere trade-off, rischi e prossimi approfondimenti prima di una scelta | Chiusura aperta alla discussione | decisioni utente | Domande guida, non call to action decisionale |

## Slide Chiave Da Rendere Come Infografiche

- Slide 3: pipeline capability map.
- Slide 4: parti comuni vs elementi differenzianti.
- Slide 7: architettura AWS Dagster/dbt/Metabase.
- Slide 11: architettura Talend/Qlik.
- Slide 13: matrice comparativa.
- Slide 14: fit scenario x progetto.
- Slide 15: WBS per processi/funzioni.
- Slide 16: piano comune per fasi.

## Open Questions Prima Del PPTX

1. **Talend/Qlik licensing:** abbiamo bisogno di una conferma commerciale su Qlik Cloud Analytics Premium e sull'eventuale inclusione/uso di Talend.
2. **Kiron CDG:** i materiali specifici sono stati trovati; restano da chiarire solo eventuali regole/open point non chiusi nella documentazione sorgente.
3. **ING ProSIGNAL:** i materiali aggiornati nel vault sono stati trovati; servono ancora esempi tracciati/file/output, se disponibili e autorizzati, per validare i claim su fixed-column, file grandi e controlli cross-file.
4. **Economics:** possiamo usare una stima a range/driver, ma servono almeno ipotesi commerciali su licenze Qlik/Talend e ipotesi cloud/run per rendere i range difendibili.
5. **Discussione finale:** il deck resta neutrale e non deve chiudere la scelta; la chiusura deve proporre domande guida e prossimi approfondimenti.

## grill-with-docs

- Le linee guida di Gianfranco chiedono le cinque sezioni standard. L'AS IS autonomo viene saltato per richiesta esplicita dell'utente, ma il deck mantiene contesto, TO BE, piano ed economics.
- La storyline deve evitare un confronto da vendor selection pura: ogni slide tool deve alimentare una discussione di business/adozione.
- Il lessico deve parlare di blueprint, scenari, trade-off e modello operativo, non di "soluzione vincente" gia' scelta.
- I casi Kiron e ProSIGNAL vanno messi prima del CDG interno per priorita' commerciale, ma senza inventare dettagli.

## Review

- Obiettivo di discussione, audience e neutralita' sono espliciti.
- Le due opzioni sono entrambe rappresentate con mapping, architettura, benefici e limiti.
- Le WBS e il piano comune sono demandati agli artifact dedicati.
- Le informazioni di licensing/costi sono segnate come gap da verificare.
- Non sono stati introdotti prezzi, effort, date o commitment.

## Humanize

La presentazione deve aiutare il comitato a discutere due modelli riusabili, non a leggere una specifica tecnica. La narrazione parte dal problema comune, mostra le componenti di una buona pipeline, confronta due modi credibili di realizzarla e chiude con le domande giuste per il confronto.
