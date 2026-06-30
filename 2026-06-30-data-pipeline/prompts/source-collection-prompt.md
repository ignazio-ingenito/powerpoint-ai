# Prompt operativo — raccolta fonti Data Pipeline 2026-06-30

Usa questo prompt per una successiva sessione di recupero fonti, dopo avere accesso al repository o ai workspace originali.

## Obiettivo

Raccogliere e classificare materiali per la presentazione `2026-06-30-data-pipeline`, senza generare ancora PowerPoint/PDF.

## Query principali

- Kiron
- Kiron CDG
- Internal CDG
- CDG
- controllo di gestione
- ProSignal / PROSignal
- fixed column / posizionale
- segnalazioni di vigilanza
- data pipeline
- Jira Tempo
- Dagster
- dlt
- dbt
- Metabase
- NocoDB
- Power BI
- OutSystems file grandi
- SharePoint CDG
- WebGenesys

## Output richiesti

Aggiorna:

- `drafts/chatgpt-source-inventory.md`
- `drafts/chatgpt-findings.md`
- `source-materials/chatgpt-collected/README.md`

Copia solo materiali sanitizzati in:

- `source-materials/chatgpt-collected/CDG/`
- `source-materials/chatgpt-collected/ProSignal/`
- `source-materials/chatgpt-collected/Kiron/`
- `source-materials/chatgpt-collected/context/`

## Controlli prima del commit

- Nessun `.env` reale.
- Nessun token, password, private key, cookie o sessione.
- Nessun URL SharePoint firmato o link con query string sensibile.
- Nessun dump dati cliente.
- Tutte le modifiche sotto `2026-06-30-data-pipeline/`.
- `git status --short` pulito tranne path attesi.

Commit suggerito:

```bash
git add 2026-06-30-data-pipeline
git commit -m "docs(data-pipeline): collect ChatGPT source findings"
git push
```
