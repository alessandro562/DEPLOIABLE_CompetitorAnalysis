# Il campo — strumento di decisione competitiva

**Deploiable · versione 3.0 · 13 agosto 2026**

Non è una dashboard. È un registro vivo con sopra un'interrogazione e sotto un
generatore di brief. Tre oggetti distinti, tenuti distinti apposta.

| Oggetto | Che cos'è | Cadenza | Chi lo tocca |
|---|---|---|---|
| **Il registro** | `dati.json` — operatori, servizi, competenze, prezzi, fonti | continua | chiunque nel team, in scrittura |
| **Lo strumento** | `index.html` — filtri, confronti, tagli | a richiesta | chi deve decidere |
| **Il brief** | l'uscita, un documento datato che risponde a una domanda | a evento | chi va in riunione |

Lo strumento **genera** i brief dal registro. I brief non si scrivono a mano: se
un brief è sbagliato, si corregge il registro.

---

## Per chi deve solo usarlo

Apri **`campo.html`** con un doppio clic. Si apre nel browser, funziona senza
connessione, non serve installare niente e non serve un server. È un file solo:
si manda per email.

Quattro schermate, non nove. Ognuna risponde a **una** domanda e finisce con
**una** riga che dice cosa fare.

| | Domanda a cui risponde |
|---|---|
| **Oggi** | Cosa è cambiato da quando ho guardato l'ultima volta, e cosa richiede attenzione |
| **Il campo** | Chi c'è, cosa vendono che noi non vendiamo, dove possiamo chiedere di più, su cosa siamo indistinguibili |
| **Chi** | Chi incontro da questo cliente |
| **Brief** | Cosa mi porto in riunione |

**Le tre cose da sapere prima di usarlo.**

1. **Il rosso segnala una cosa sola: dove non sappiamo.** Non è una scala di
   minaccia, non è una categoria. Una cella rossa è un buco del registro; una
   cella bianca su un operatore che ha catalogo vuol dire «non risulta a
   catalogo», ed è un fatto. Una riga con il nome in rosso è un operatore su cui
   non si può decidere nulla.
2. **Ogni affermazione porta la propria fonte, la propria data e la propria
   marcatura.** Non l'operatore: l'affermazione. `V` verificato da fonte terza
   controllabile · `D` dichiarato dall'operatore · `S` stimato da aggregatore ·
   `N` cercato e non trovato.
3. **I giudizi sono separati dai fatti** e portano il nome di chi li ha
   espressi. Nella scheda di un operatore i fatti stanno nel catalogo servizi e
   nel profilo di competenza; i giudizi stanno nel loro blocco, ciascuno con
   autore, data e motivazione.

**Tutto lo stato sta nell'indirizzo.** Taglio, filtri, selezione, operatore
aperto. Copia l'indirizzo dalla barra, mandalo a un collega: lui apre e vede
esattamente la tua schermata, filtri compresi. Il pulsante indietro funziona.

Premi `/` (o `Ctrl+K`) per cercare ovunque: operatori, servizi, argomenti di
trattativa, segnali, incertezze.

`Ctrl+P` stampa. Il brief è pensato per finire su carta e su un proiettore.

---

## Per chi corregge il registro

**Ogni campo di giudizio si modifica in linea.** Vai su **Chi**, doppio clic sul
valore. Lo strumento chiede la motivazione in una riga e la registra con autore
e data. Un giudizio senza motivazione non si salva: un giudizio senza autore è
un dato falso.

Si può correggere anche lo **stato** di un operatore — attivo, archiviato, da
verificare — che è la decisione di chi entra e chi esce, e il pulsante **«Ho
verificato oggi»** aggiorna `ultima_verifica` con il nome di chi l'ha fatto.

Le modifiche vivono nello spazio locale del browser. Il pulsante **Modifiche**
in alto a destra mostra il differenziale ed esporta una **patch JSON**. Chi
tiene il registro la applica a `dati.json`. **Nessuno deve ricompilare niente.**

---

## Per chi mantiene il registro

```bash
# 1. si modifica dati.json (a mano, o applicando una patch esportata)
python3 verifica-dati.py     # il contratto dati regge?
python3 contrasto.py --css   # ogni coppia testo-fondo sopra 4,5:1?
python3 costruisci.py        # genera campo.html, il file da distribuire
```

Serve **solo Python 3**. Nessuna dipendenza, nessun pacchetto da installare.

Per sviluppare sull'interfaccia senza rigenerare ogni volta:

```bash
python3 -m http.server        # poi http://localhost:8000/
```

`index.html` legge `dati.json` via `fetch`, che il browser blocca su `file://`:
è per questo che il file unico esiste. **`campo.html` è generato: non si
modifica a mano, le modifiche si perdono al primo rigenera.**

### I file

```
strumento/
├── dati.json          il registro. È la fonte.
├── index.html         lo strumento: CSS e JavaScript, nessuna dipendenza
├── campo.html         GENERATO — l'artefatto di distribuzione, file unico
├── costruisci.py      dati.json + index.html → campo.html
├── verifica-dati.py   controlla le cinque regole vincolanti del contratto dati
├── contrasto.py       la tavolozza, e la verifica del contrasto
└── LEGGIMI.md         questo file
```

---

## Il contratto dati

Cinque regole vincolanti, controllate da `verifica-dati.py`. Non sono
preferenze: se una salta, lo strumento mente.

1. **Ogni campo di confronto ha un enum chiuso.** Testo libero solo nei campi
   narrativi — `consegna`, `motivazione`, `nota`, `prova`. Se un campo serve a
   filtrare, ordinare o disegnare un asse, è un enum. Gli enum sono dichiarati
   dentro `dati.json`, non nel codice.
2. **I giudizi sono separati dai fatti** e portano autore, data e motivazione.
   Minaccia, sovrapposizione e somiglianza vivono in `giudizi`, non fra i fatti.
3. **Le scale 0-3 hanno la definizione dei gradini nel dato**, non nel codice, e
   la definizione è visibile nell'interfaccia dove la scala compare. Vedi
   `scale` in `dati.json`.
4. **Nessun numero derivato è salvato.** Copertura, conteggi, letture,
   territori liberi: tutto si ricalcola dal dato a ogni disegno. Se cambi una
   riga, ogni conclusione cambia da sola.
5. **Staleness esplicita.** Ogni operatore ha `ultima_verifica`. Oltre 90 giorni
   la riga si segnala da sola in **Oggi**; `ultima_verifica` a `null` significa
   che una lettura diretta non è mai riuscita, ed è il caso peggiore.

### Le entità

```
operatore   slug · nome · sito · sede · paese · anno · forma_giuridica
            arena[enum] · origine[enum] · stato[attivo|archiviato|da_verificare]
            motivo_archivio · ultima_verifica · verificato_da · nota
            segmenti[enum multiplo] + marcatura
            modello_ricavo[enum multiplo] · chi_rischia[enum]
            economia_nota · economia_fonte_url · economia_data · economia_marcatura

servizio    ← l'unità di analisi
            id · operatore · nome_proprio (come lo chiamano loro)
            tipo[enum 13] · linea[oi|vb|ai|ma|fuori]
            consegna (cosa esce concretamente) · durata · prova
            prezzo · prezzo_natura[enum] · condizioni
            fonte_url · data · marcatura

competenza  operatore · composizione[enum multiplo] · headcount + marcatura
            capacita_tecnica[0-3] · esecuzione_interna[0-3]
            stack[] · deploy[] · asset_proprietari[]
            fonte_url · data · marcatura

firma       operatore · payoff · headline · categoria_autoattribuita
            territorio[enum] · provenienza · fonte_url · data · marcatura

giudizio    ← separato dai fatti, sempre
            id · operatore · campo[enum] · valore · autore · data · motivazione

segnale     id · data · soggetto (slug | mercato | norma) · tipo[enum]
            testo · fonte_url · marcatura

incertezza  id · cosa · perche_conta · fonte_che_la_chiude
            costo_stimato[alto|medio|basso] · ore_stimate · stato · responsabile

lettura     id · domanda · regola · e_quindi · falsifica
            (la regola nomina il calcolo; il numero non è mai salvato)
```

### Perché `prezzo` è tre campi e non uno

Nella prima stesura il campo `prezzo` conteneva quattro cose diverse: un prezzo
di listino («3.000 € + IVA»), un importo di aggiudicazione pubblica, la dotazione
di capitale di un programma («Forward Factory 8,64 mln») e la descrizione di un
meccanismo («fee di consulenza più equity»). La lettura costruita sopra diceva
che **23 operatori su 64** espongono un prezzo. È falso: sono **3**.

Un solo campo che tiene insieme il prezzo e il modo in cui si paga produce una
conclusione sbagliata con l'aria di essere misurata. Quindi:

- `prezzo` — solo l'importo, vuoto se non pubblicato;
- `prezzo_natura` — `listino` (leggibile dal cliente prima della trattativa) ·
  `aggiudicazione` (noto a posteriori da una gara) · `dotazione` (il capitale che
  l'operatore governa, non ciò che il cliente paga) · `gratuito` ·
  `non-pubblico`;
- `condizioni` — il meccanismo, in prosa.

Solo `listino` conta nella lettura sul prezzo, e la schermata **Oggi** dichiara
la regola accanto al numero. Stessa correzione su `chi_rischia`: l'equity di
portafoglio in aggiunta alla fee **non** è rischio condiviso, perché la fee di
gestione si incassa comunque — contarla portava la lettura da 11 a 27.

**Tre aggiunte rispetto alla specifica**, tutte per lo stesso motivo — servono a
decidere più in fretta, e senza di esse un intero taglio dell'interrogazione non
esisterebbe:

- `modello_ricavo` e `chi_rischia` sull'operatore, con fonte, data e marcatura
  proprie: reggono il taglio **per prezzo**, e la prima conclusione operativa
  («mettere il prezzo e il rischio nella promessa») non è verificabile senza.
- `firma` come entità propria: regge il taglio **per posizionamento**.
- `incertezza.responsabile` e `incertezza.ore_stimate`: senza un nome e un costo,
  la riga «la prossima azione» di **Oggi** sarebbe un'opinione del codice.

---

## Da dove viene il dato

Dai file della cartella `analisi-competitor/`, tornata V2 dell'11/08/2026:
le tredici schede complete a 14 campi, i cinque file di screening dei 93
operatori, `modelli-di-ricavo-e-prezzi.md`, `firme-verbali.md`,
`sintesi-strategica.md`, `dubbi.md`. **Nessun fatto nuovo è stato introdotto in
questa conversione:** dove serviva un dato assente, il dato è dichiarato
mancante e non stimato per analogia.

**Quello che è cambiato rispetto alla V2** è la copertura del catalogo servizi,
che era il collo di bottiglia dichiarato: da **10 operatori su 36** a **65 su
79**, con fonte, data e marcatura per riga. Sotto una certa copertura uno
strumento sopra un registro è una demo, non un registro.

**Quello che resta non fatto, e va saputo prima di usarlo.**

- **La categoria dei sostituti non è stata lavorata.** TeamSystem e Zucchetti
  sono a registro con zero servizi e stato `da_verificare`: compaiono come
  buchi perché sono buchi. Finché non li misuriamo, sulle PMI stiamo
  analizzando i concorrenti sbagliati.
- **Diciassette operatori non hanno mai avuto una lettura diretta riuscita**
  (dominio non raggiungibile, 403, sito interamente JavaScript). Il loro
  punteggio è limitato dalla verificabilità, non dalla rilevanza: potrebbero
  valere di più.
- **Nessuno dei 93 operatori screenati ha un fatturato verificato**, e lo
  screening è stato fatto senza incrocio di fonti. Ogni riga che poggia sul solo
  screening lo dichiara nella propria motivazione.
- **Il registro è stato verificato tutto lo stesso giorno**, quindi scadrà tutto
  lo stesso giorno: la prima scadenza è il 09/11/2026. Le verifiche vanno
  scaglionate, ed è la prima cosa che il registro dice di sé in **Oggi**.

---

## Uso interno

Contiene giudizi competitivi espliciti su operatori nominati, la nostra lettura
dei loro punti deboli e i nostri buchi. Se dovesse diventare pubblico va
prodotta una versione depurata: fatti e marcature sì, `giudizi` no.

Lo strumento **non fa chiamate di rete**. Nessun font esterno, nessun
tracciamento, nessun dato esce dal file.
