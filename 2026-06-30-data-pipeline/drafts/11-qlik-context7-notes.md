# Qlik Context7 Notes

## Scopo

Annotare i riscontri ottenuti tramite Context7 sulla documentazione Qlik, da usare come materiale di supporto per lo scenario Talend + Qlik Cloud Analytics Premium.

Queste note non sostituiscono una verifica commerciale su licenze, packaging o limiti contrattuali.

## Fonti Context7

### Qlik Help

Context7 library: `/websites/help_qlik`

Riscontri utili:

- Qlik Cloud viene descritto come stack che combina data integration e analytics per portare dati enterprise da fonti on-premise e cloud verso analytics self-service Qlik o altri ambienti analytics.
- Qlik Talend Cloud viene descritto come pacchetto unificato di data integration e data quality per pipeline che producono dati trusted.
- Qlik Automate viene descritto come interfaccia no-code per costruire workflow automatizzati di analytics e data workflow.
- Qlik Cloud supporta webhook per eventi di sistema, inclusi eventi legati ad automation, API, app, data integration e utenti.

### Qlik Developer

Context7 library: `/websites/qlik_dev`

Riscontri utili:

- Qlik Cloud espone API per gestire task e task chain.
- Le API citate coprono creazione, aggiornamento, cancellazione e avvio task.
- Sono documentati run, ultimo run e log del run.
- Qlik Developer documenta automazioni per task chaining, incluse versioni scheduled e webhook-triggered.

## Implicazioni Per Lo Scenario B

Lo scenario Talend + Qlik puo' essere rappresentato come:

```text
Sorgenti
  -> Talend / Qlik data integration
  -> controlli e data quality
  -> storage / mart da definire
  -> Qlik Cloud Analytics Premium
  -> automazioni, reload, task chain, monitoraggio operativo
```

## Claim Utilizzabili Nel Deck

- Qlik documenta capability di data integration, data quality, analytics e automazione.
- Qlik Developer documenta API e automazioni utili a operationalizzare reload, task chain, run e log.
- Lo scenario Qlik/Talend puo' essere posizionato come ipotesi piu' platform-oriented rispetto a Dagster/dbt/Metabase.

## Claim Da Non Fare Senza Verifica

- Non affermare che Talend e' incluso in Qlik Cloud Analytics Premium.
- Non affermare che Qlik/Talend copra senza custom tutti i casi ProSIGNAL, soprattutto file grandi, fixed-column e controlli cross-file.
- Non affermare costi o range economici Qlik senza fonte commerciale.
- Non affermare che Qlik Automate sostituisce sempre un orchestratore data engineering.

## Gap Da Verificare

- Packaging commerciale effettivo di Qlik Cloud Analytics Premium e Talend.
- Runtime/deployment Talend nel contesto target.
- Limiti su volumi, scheduling, task chain, refresh e run log applicabili al tenant/licenza.
- Fit tecnico su fixed-column file processing e file molto grandi.
- Governance multi-cliente e riuso cross-tenant.

## grill-with-docs

- I riscontri sono stati usati solo per rafforzare lo scenario Qlik/Talend, non per spostare la raccomandazione.
- I punti non confermati restano marcati come gap.
- Il confronto rimane neutrale e adatto a CEO/CTO/Tech Committee.

## Review

- Le note distinguono capability documentate e aspetti commerciali da verificare.
- Non sono stati introdotti prezzi, promesse di licenza o limiti quantitativi non supportati.
- I risultati sono coerenti con i draft `08-scenario-comparison.md` e `10-architecture-brief.md`.

## Humanize

Qlik/Talend puo' essere presentato come una strada piu' piattaforma e meno custom, ma non va venduto come scorciatoia automatica. Prima di decidere serve capire cosa include davvero la licenza e quanto lo stack regge sui casi piu' esigenti, in particolare ProSIGNAL.
