# Analisi competitor V2 — come si usa e come si aggiorna

**Deploiable · 11/08/2026**

---

## Per chi deve solo leggere

Apri **`analisi-competitor-v2.html`** con un doppio clic. Si apre nel browser, funziona senza
connessione, non serve installare niente e non serve un server. Si può mandare per email o mettere
in una cartella condivisa: è un file solo.

**Le tre cose da sapere prima di usarlo.**

1. **Ogni affermazione porta scritto quanto è affidabile.** `V` verificato da fonte terza
   controllabile · `D` dichiarato dall'operatore · `S` stimato, da aggregatore o banca dati ·
   `N` cercato e non trovato. Non è un dettaglio di metodo: è la differenza fra un'analisi e una
   raccolta di brochure riscritte.
2. **Il pulsante «solo verificato»**, in alto a destra, sbiadisce tutto ciò che non poggia su una
   fonte terza. Premilo su una scheda qualsiasi: quello che resta leggibile è quanto sappiamo
   davvero. È anche il modo più rapido per decidere che cosa controllare per primo.
3. **Le schede contengono fatti, la sintesi strategica contiene giudizi.** Sono documenti diversi e
   la dashboard lo dice in testa a ciascuno. Non citare un giudizio come se fosse un dato.

Premi `/` per cercare. La ricerca copre i nomi degli operatori e i titoli di sezione; per cercare
dentro il testo di un documento usa la ricerca del browser (`Ctrl+F` o `Cmd+F`).

Il tema chiaro o scuro segue le impostazioni del sistema operativo. La pagina si stampa in modo
decente: `Ctrl+P` stampa la sezione aperta.

---

## Che cosa c'è dentro

| Sezione | Che cos'è |
|---|---|
| **Apertura** | I numeri, i tre risultati negativi, i limiti. Si legge in due minuti |
| **Documento finale** | Le sette sezioni del metodo, comprese le cinque conclusioni operative |
| **I 100 operatori** | 93 screenati con punteggio da 1 a 5, più i 7 della base. Filtrabile e cercabile |
| **Schede** | 13 profili a 14 campi, con fonte e data su ogni campo |
| **Prezzi e ricavi** | Come si fanno pagare, e i 77 contratti pubblici |
| **Firme e territori** | 46 firme verbali alla lettera, e la mappa di che cosa resta libero |
| **Sintesi strategica** | Sovrapposizione e argomenti in gara. **Contiene giudizi** |
| **Scouting · Screening · Selezione · Metodo** | Come è stato fatto, per intero: chiunque può rifarlo |
| **Incertezze · Verifica** | Che cosa non sappiamo, e il controllo avversariale sul documento finale |

---

## Per chi deve aggiornare

**La fonte sono i file markdown di questa cartella, non l'HTML.** L'HTML è una vista generata:
se lo modifichi a mano, la modifica si perde al primo rigenera.

Il flusso è:

```bash
# 1. modifichi i markdown — una scheda, il documento finale, i dubbi…
#    e la riga CSV corrispondente in dati/righe/<operatore>.csv

# 2. rifondi il registro
python3 dati/fondi-registro.py

# 3. rigeneri la dashboard
python3 dashboard/estrai.py      # markdown → dashboard/dati.json
python3 dashboard/costruisci.py  # dati.json + modello.html → analisi-competitor-v2.html
```

Serve Python 3 e la libreria `mistune` (`pip install mistune`). Nient'altro.

**Per aggiungere un operatore con scheda completa:**

1. lancia il **PROMPT 2** di `02-prompt-agenti.md` — è autosufficiente;
2. salva la scheda in `schede/<slug>.md`;
3. crea `dati/righe/<slug>.csv` con l'header identico agli altri (34 colonne);
4. aggiungi le domande aperte in `dubbi.md`;
5. registra lo slug in `SCHEDE` dentro `dashboard/estrai.py`;
6. rilancia i tre comandi sopra.

`dati/fondi-registro.py` si ferma con un errore se un header non combacia o se una riga ha un numero
di campi diverso: è voluto, perché un registro che si disallinea in silenzio è peggio di un registro
che non esiste.

**Per cambiare l'aspetto** si tocca solo `dashboard/modello.html`: contiene tutto il CSS e tutto il
JavaScript, e un segnaposto `/*DATI*/` dove viene iniettato il JSON.

---

## Struttura della cartella

```
analisi-competitor/
├── analisi-competitor-v2.html   ← la dashboard, il file da distribuire
├── LEGGIMI.md                   ← questo file
│
├── 01-metodo-e-schema.md        metodo, tassonomia, marcature
├── 02-prompt-agenti.md          i cinque prompt, autosufficienti
├── 03-base-e-buchi.md           base di partenza, con lo stato dei buchi
├── 04-pipeline-scouting.md      la pipeline in otto fasi
│
├── ANALISI-COMPETITOR-V2.md     il documento finale
├── sintesi-strategica.md        giudizi: sovrapposizione e argomenti in gara
├── modelli-di-ricavo-e-prezzi.md
├── firme-verbali.md
├── dubbi.md                     registro delle incertezze
├── verifica.md                  verifica avversariale e correzioni applicate
│
├── schede/                      13 schede a 14 campi
├── scouting/                    7 angoli, consolidato, screening, selezione
├── dubbi-parziali/              le domande aperte per scheda, prima della fusione
├── dati/
│   ├── righe/<operatore>.csv    una riga per file: evita i conflitti fra sessioni
│   ├── registro.csv             generato dalla fusione
│   └── fondi-registro.py
└── dashboard/
    ├── estrai.py                markdown → dati.json
    ├── costruisci.py            dati.json + modello.html → HTML unico
    ├── modello.html             CSS e JavaScript della dashboard
    └── dati.json                generato
```

---

## Formati e licenza d'uso interno

Tutto è in **markdown**, **CSV** e **HTML**: formati aperti, leggibili con qualunque editor,
versionabili con git, senza licenze e senza dipendenza da un fornitore. Se un giorno l'analisi va
messa in un wiki, in un sito statico o in un altro strumento, il materiale è già pronto: sono file
di testo.

La dashboard **non fa chiamate di rete** tranne il caricamento dei font da Google Fonts, che serve
solo all'estetica: senza connessione la pagina usa i font di sistema e resta perfettamente
leggibile. Nessun tracciamento, nessun dato esce dal file.

**Questo materiale è per uso interno.** Contiene giudizi competitivi espliciti su operatori nominati,
la nostra lettura dei loro punti deboli e i nostri buchi. Se un giorno dovesse diventare pubblico,
va prodotta una versione depurata: fatti e marcature sì, `sintesi-strategica.md` e la sezione
«argomenti in gara» no.

---

## Il controllo che manca ancora

Il metodo prescrive una cosa che nessuno ha ancora fatto: **aprire almeno una fonte per operatore**
prima di portare il materiale in riunione. La verifica avversariale in `verifica.md` ha controllato
la coerenza fra il documento finale e i file interni, **non la verità dei file interni**.

Se avete mezz'ora sola, spendetela così: aprite su ANAC i due CIG di Seedble e i sei contratti sopra
i 130.000 €. Trasformano da `S` a `V` i primi prezzi verificati che questa analisi possieda.
