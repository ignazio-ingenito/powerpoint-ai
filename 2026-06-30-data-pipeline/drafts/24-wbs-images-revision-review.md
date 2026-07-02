# WBS Images Revision Review

## Scopo

Revisione delle immagini WBS del PDF finale image-based, per allinearle alle linee guida di Gianfranco:

- WBS nel TO BE;
- evidenza di processi e funzioni gestiti;
- primo livello sempre per processi;
- secondo livello sempre per funzioni;
- blueprint generica prima delle WBS applicative;
- stessa ossatura comune nei tre casi, con processi non applicabili comunque visibili come `N/A`.

## Artifact aggiornati

- `generated-assets/final-image-pdf/sources/data-pipeline-image-final-v1.html`
- `generated-assets/final-image-pdf/slides/slide-13.png`
- `generated-assets/final-image-pdf/slides/slide-14.png`
- `generated-assets/final-image-pdf/slides/slide-15.png`
- `generated-assets/final-image-pdf/slides/slide-16.png`
- `generated-assets/final-image-pdf/slides/slide-17.png`
- `generated-assets/final-image-pdf/slides/slide-18.png`
- `generated-assets/final-image-pdf/slides/slide-19.png`
- `generated-assets/final-image-pdf/slides/slide-20.png`
- `generated-assets/final-image-pdf/previews/source-render-v1.pdf`
- `generated-assets/final-image-pdf/previews/image-final-v1-contact.png`
- `2026_TXT_001 - Data Pipeline Blueprint - Image Final v1.0.pdf`
- `generated-assets/final-image-pdf/manifest.md`

## Nuova struttura delle immagini WBS

| Slide | WBS | Ruolo |
| ----- | --- | ----- |
| 13 | Blueprint comune | Catalogo processi/funzioni riusabili |
| 14 | ING ProSIGNAL | Applicazione con focus file regolamentari |
| 15 | Kiron CDG | Applicazione CDG-like con Actual, Forecast e BI |
| 16 | CDG interno | Reference implementation sui processi P1-P6 |

## Grill-with-docs

- Il termine `WBS` resta coerente con `docs/reference.1.md`: non è una lista di tool, ma una vista che evidenzia processi e funzioni gestiti.
- La distinzione `processo` / `funzione` è ora visibile nel layout: il processo è sempre la riga o card principale; le funzioni sono i chip secondari.
- La blueprint non è trattata come progetto cliente: è il catalogo comune da riusare sui casi applicativi.
- Le differenze di ProSIGNAL, Kiron e CDG interno sono espresse come funzioni o estensioni specifiche, non come rottura della struttura comune.

## Critic

- Rischio mitigato: le WBS precedenti erano troppo aggregate e non mostravano una blueprint prima dei casi.
- Rischio mitigato: Kiron e CDG interno erano accorpati; ora hanno due slide distinte.
- Rischio mitigato: i processi non applicabili non spariscono; restano visibili in grigio come `N/A`.
- Rischio residuo: ProSIGNAL resta meno documentato di CDG/Kiron. Le funzioni sono quindi sintetiche e non includono dettagli non supportati da esempi reali di file o output.

## Review

- Le quattro WBS sono presenti.
- Il primo livello è sempre un processo.
- Il secondo livello è sempre una funzione.
- I tre casi applicativi condividono la stessa ossatura comune.
- Le differenze specifiche sono espresse come estensioni o funzioni dedicate.
- Il PDF finale è stato rigenerato e contiene 20 pagine.
- Le slide PNG sono 2560 x 1440.
- La contact sheet è stata rigenerata.

## Humanize

Le WBS ora raccontano la stessa idea in modo più semplice: prima mostriamo il modello comune, poi facciamo vedere come quel modello si adatta ai tre casi. Il comitato può leggere subito cosa resta uguale, cosa cambia e cosa non si applica.
