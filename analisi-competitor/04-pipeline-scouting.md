# Pipeline di scouting e analisi
**Deploiable · analisi competitor V2 · come trovare operatori nuovi e portarli fino alla scheda completa**

Sostituisce il PROMPT 1 del file `02-prompt-agenti.md`, che chiedeva sei angoli di ricerca in un lancio unico. Sei angoli in un lancio producono sei ricerche superficiali: vanno separati.

---

## La pipeline in otto fasi

| Fase | Cosa | Lanci | Chi |
|---|---|---|---|
| **1** | Scouting per angolo | 7 lanci, uno per angolo, parallelizzabili | Agente |
| **2** | Consolidamento e deduplica | 1 lancio | Agente |
| **3** | Screening rapido | 1 lancio su tutta la lista | Agente |
| **4** | Triage | — | **Persona** |
| **5** | Schede complete | 1 lancio per operatore | Agente |
| **6** | Firme verbali e prezzi | 2 lanci trasversali | Agente |
| **7** | Sintesi strategica | 1 lancio | Agente |
| **8** | Documento finale | 1 lancio + revisione | Agente + persona |

La fase 4 resta umana. È dove si decide su cosa spendere le schede complete, che costano molto: una scheda seria è trecento righe di ricerca.

---

## Struttura delle cartelle

```
analisi-competitor/
  01-metodo-e-schema.md
  02-prompt-agenti.md
  03-base-e-buchi.md
  04-pipeline-scouting.md        ← questo file
  scouting/
    a-appalti.md
    b-osservatori.md
    c-programmi-corporate.md
    d-eventi.md
    e-casi-cliente.md
    f-annunci-lavoro.md
    g-estero.md
    consolidato.md               ← fase 2
    screening.md                 ← fase 3
    selezione.md                 ← fase 4, scritta a mano
  schede/
    <operatore>.md
  dati/
    righe/<operatore>.csv        ← una riga per file, per evitare conflitti
    registro.csv                 ← generato dalla fusione
  dubbi.md
```

**Regola tecnica importante:** ogni sessione scrive solo su file propri. Se più sessioni scrivono sullo stesso `registro.csv` in parallelo, si sovrascrivono a vicenda. Ogni scheda produce `dati/righe/<operatore>.csv`, e alla fine un solo comando li fonde.

---

# FASE 1 — Scouting per angolo

Sette prompt indipendenti. Possono girare in parallelo su sessioni separate. Ognuno scrive sul proprio file.

**Preambolo comune** — incollalo in testa a ciascuno dei sette:

> **Contesto.** Lavori per una società italiana di innovazione e venture building con quattro linee: **open innovation** (scouting e adozione di tecnologie esterne dentro organizzazioni esistenti), **venture building su commissione** (costruzione di nuove iniziative per conto di un committente), **AI adoption** (introduzione dell'AI nei processi aziendali), **M&A** (assistenza ad aziende e banche che acquisiscono startup e scale-up). Segmenti serviti: PMI, aziende dai 40 milioni di fatturato in su, enti pubblici, soggetti acquirenti.
>
> **Operatori già mappati, da NON riportare:** Zest, Ventive, Startup Geeks, Datapizza, Webidoo, Perspective AI, Vento, Seedble, Cariplo Factory, Officine Innovazione Deloitte, EY, PwC, KPMG, Accenture, Reply, Engineering, Capgemini, Mach49, Alloy Partners, Creative Dock, FoundersLane, 27pilots, Bundl, Hexa, Distyl AI, TeamSystem, Zucchetti.
>
> **Criteri di inclusione** — tutti e tre necessari: presidia almeno una delle quattro linee; ha evidenza di attività negli ultimi 18 mesi; è una struttura societaria, non un professionista singolo.
>
> **Criteri di esclusione:** fornitori di solo software senza componente di servizio; incubatori universitari senza offerta commerciale; agenzie di comunicazione e marketing; società di sola formazione; consulenti individuali.
>
> **Vincoli di qualità.** Ogni operatore riportato deve avere un sito attivo e verificabile. Non inventare nomi. Se non trovi nulla, dichiaralo: un angolo che non produce risultati è un'informazione utile. Per ogni riga indica la fonte con URL e data.
>
> **Formato di uscita.** Tabella: `Denominazione | Sito | Sede | Categoria (venture builder / open innovation / AI / M&A / sostituto) | Linee presidiate | Segmenti | Perché è rilevante (max 20 parole) | Fonte URL`. Sotto, due sezioni brevi: **dubbi** (candidati con evidenza debole) e **limiti della ricerca** (cosa non sei riuscito a coprire e perché).

---

## PROMPT 1A — Appalti e gare pubbliche
**File di uscita:** `scouting/a-appalti.md` · **È l'angolo più produttivo: usalo per primo**

> [PREAMBOLO COMUNE]
>
> **Angolo.** Cerca le società che negli ultimi 24 mesi si sono aggiudicate appalti, gare o affidamenti pubblici in Italia su: innovazione e open innovation, trasformazione digitale, adozione di intelligenza artificiale, accelerazione d'impresa, servizi di scouting tecnologico, supporto alla progettazione di programmi di innovazione.
>
> **Dove cercare.** Banche dati e portali degli appalti pubblici; sezioni «amministrazione trasparente» e «bandi e gare» dei siti di enti, comuni, regioni, camere di commercio, agenzie regionali per l'innovazione, università, aziende pubbliche; determine di aggiudicazione; codici identificativi di gara.
>
> **Cosa estrarre in più rispetto al formato standard.** Per ogni aggiudicazione: stazione appaltante, oggetto, **importo aggiudicato**, anno, codice identificativo. Gli importi sono pubblici per legge: sono l'unico dato di prezzo verificabile su questo mercato, quindi riportali sempre.
>
> **Obiettivo.** 10-20 operatori. Se un operatore compare con più aggiudicazioni, elencale tutte.

---

## PROMPT 1B — Osservatori e associazioni di categoria
**File di uscita:** `scouting/b-osservatori.md` · **È il censimento più completo che esista**

> [PREAMBOLO COMUNE]
>
> **Angolo.** Estrai gli operatori censiti dagli osservatori e dagli elenchi soci delle associazioni italiane del settore innovazione e digitale.
>
> **Dove cercare.**
> 1. **Open Innovation Lookout** (openinnovationlookout.it) — ha una sezione con le schede dei singoli operatori censiti. È un censimento di oltre 500 organizzazioni: scorrilo sistematicamente, non a campione. **È la fonte più importante di questo angolo.**
> 2. Elenchi soci di: Italian Tech Alliance, InnovUp, Assintel, Assinter, Confindustria Digitale e Confindustria territoriali con sezione innovazione
> 3. Elenchi di incubatori certificati e di società iscritte come PMI innovative con codice attività di consulenza
> 4. Osservatori del Politecnico di Milano, dove pubblicano elenchi di operatori
>
> **Cosa estrarre in più.** Se la fonte espone categoria, fatturato o dimensione, riportali marcandoli come dichiarati all'osservatorio, non verificati.
>
> **Obiettivo.** 20-40 operatori. È l'angolo con il volume più alto: privilegia la completezza sulla profondità, il filtro lo facciamo dopo.

---

## PROMPT 1C — Gestori di programmi corporate
**File di uscita:** `scouting/c-programmi-corporate.md` · **Sono concorrenti diretti e quasi invisibili**

> [PREAMBOLO COMUNE]
>
> **Angolo.** Identifica le società che **gestiscono per conto di terzi** programmi di innovazione: acceleratori corporate, call for startup, hackathon aziendali, programmi di open innovation, corporate venture builder.
>
> **Dove cercare.** Pagine «innovazione» dei siti delle grandi aziende italiane e le loro call for startup; la rete degli acceleratori promossi da operatori pubblici e da fondi di venture capital nazionali, verificando **chi è il gestore operativo** di ciascun programma; comunicati di lancio di programmi corporate, dove il gestore è quasi sempre citato; siti degli acceleratori stessi, alla voce «partner» o «chi siamo».
>
> **Attenzione.** Il nome che compare in evidenza è quello della corporate o del fondo. Il concorrente è **chi gestisce**, e sta nel comunicato o nel piè di pagina. È questo il motivo per cui questi operatori non emergono dalle ricerche generiche.
>
> **Cosa estrarre in più.** Per ogni operatore: quali programmi gestisce, per quale committente, da quando, e se il rapporto è ancora attivo.
>
> **Obiettivo.** 8-15 operatori.

---

## PROMPT 1D — Eventi di settore
**File di uscita:** `scouting/d-eventi.md`

> [PREAMBOLO COMUNE]
>
> **Angolo.** Estrai relatori, sponsor ed espositori degli eventi italiani su innovazione, startup e AI degli ultimi 18 mesi, limitandoti a chi rappresenta società di servizi rientranti nei nostri criteri.
>
> **Dove cercare.** Programmi e liste sponsor degli eventi nazionali di settore, delle fiere dell'innovazione e delle manifestazioni regionali; agende degli osservatori universitari; eventi organizzati dalle associazioni di categoria.
>
> **Cosa estrarre in più.** Evento, data, ruolo (relatore, sponsor, espositore), tema dell'intervento. Chi paga per esserci sta investendo in posizionamento: è un segnale di dove vuole andare.
>
> **Obiettivo.** 10-20 operatori.

---

## PROMPT 1E — Fornitori citati dai clienti
**File di uscita:** `scouting/e-casi-cliente.md` · **È l'unica prova di esecuzione confermata da terzi**

> [PREAMBOLO COMUNE]
>
> **Angolo.** Trova i fornitori di servizi di innovazione **citati nei comunicati e nei casi studio pubblicati dalle aziende clienti**, non nei materiali dei fornitori stessi.
>
> **Dove cercare.** Sale stampa e sezioni «innovazione» dei siti di grandi e medie aziende italiane; bilanci di sostenibilità e relazioni annuali, dove i programmi di innovazione sono spesso descritti con i partner; comunicati di lancio di nuovi prodotti o business unit nati da programmi di innovazione; interviste a innovation manager e direttori generali.
>
> **Perché conta.** Un fornitore citato dal proprio cliente in un documento ufficiale è l'unica forma di referenza che non sia autodichiarata. Sono i concorrenti che in gara ci battono sulle referenze.
>
> **Cosa estrarre in più.** Azienda cliente, oggetto del progetto, anno, dove è citato il fornitore.
>
> **Obiettivo.** 8-15 operatori.

---

## PROMPT 1F — Annunci di lavoro e nuovi entranti
**File di uscita:** `scouting/f-annunci-lavoro.md` · **Anticipa di sei mesi i cambi di offerta**

> [PREAMBOLO COMUNE]
>
> **Angolo, in due parti.**
>
> **Parte 1 — annunci di lavoro.** Trova società italiane di servizi che negli ultimi 12 mesi hanno pubblicato annunci per figure di: venture architect, venture builder, innovation manager o consultant, AI solution architect, forward deployed engineer, AI transformation consultant. Escludi le aziende che assumono per sé: cerca chi assume per servire clienti.
>
> **Parte 2 — nuovi entranti.** Trova società di consulenza su innovazione o AI **costituite dopo il 2023** e già attive commercialmente. Cerca fra le startup e PMI innovative iscritte alla sezione speciale del registro con codice attività di consulenza imprenditoriale o informatica.
>
> **Perché conta.** Chi assume oggi una figura che non aveva, sta cambiando offerta. Chi si è costituito da due anni non ha ancora fatto marketing e non compare in nessun censimento.
>
> **Cosa estrarre in più.** Per la parte 1: quali ruoli, quanti annunci, da quando. Per la parte 2: anno di costituzione e primo segnale di attività commerciale.
>
> **Obiettivo.** 10-20 operatori complessivi.

---

## PROMPT 1G — Estero, per modello
**File di uscita:** `scouting/g-estero.md`

> [PREAMBOLO COMUNE]
>
> **Angolo.** Identifica operatori esteri che **non competono con noi sul mercato italiano** ma il cui modello è replicabile qui. Ci interessano per capire quali formule esistono, non per mappare una minaccia.
>
> **Cosa cercare in particolare.**
> - Operatori che combinano advisory e prodotti proprietari sotto due marchi distinti
> - Operatori che lavorano su aziende di dimensione media, non su multinazionali: è la fascia che ci interessa e che quasi nessuno serve
> - Formule di remunerazione inusuali: quota sul margine generato, royalty sulla linea di ricavo creata, compenso legato all'adozione
> - Operatori specializzati sul settore pubblico
>
> **Geografie prioritarie.** Germania, Francia, Spagna, Paesi Bassi, paesi nordici. Il mercato statunitense è già coperto nella base esistente.
>
> **Cosa estrarre in più.** Per ciascuno: **qual è l'elemento del modello che varrebbe la pena replicare in Italia**, in una riga.
>
> **Obiettivo.** 8-12 operatori.

---

# FASE 2 — Consolidamento

**File di uscita:** `scouting/consolidato.md` · Un solo lancio, dopo che tutti e sette gli angoli hanno prodotto.

> **Compito.** Leggi tutti i file nella cartella `scouting/` prodotti dagli angoli A-G. Consolidali in una lista unica.
>
> **Operazioni da svolgere.**
> 1. **Deduplica** — lo stesso operatore può comparire in più angoli, anche con denominazioni leggermente diverse o con società collegate. Unifica, e per ogni operatore indica **da quanti e quali angoli è emerso**
> 2. **Verifica di esistenza** — controlla che il sito risolva davvero. Segnala i domini morti o divergenti
> 3. **Elimina i già noti** — se qualcuno ha riportato operatori della lista di esclusione, toglili
> 4. **Marca i collegamenti societari** — se due operatori risultano parte dello stesso gruppo o hanno soci in comune, evidenzialo
>
> **Segnale importante.** Un operatore emerso da **tre o più angoli diversi** è quasi sempre rilevante: significa che è presente sul mercato in più modi. Mettilo in cima.
>
> **Formato di uscita.** Tabella unica con le colonne dello scouting più `Angoli di provenienza` e `N. angoli`, ordinata per numero di angoli decrescente. In coda: **domini non risolti**, **collegamenti societari rilevati**, **totale operatori unici**.

---

# FASE 3 — Screening rapido

**File di uscita:** `scouting/screening.md` · Un solo lancio su tutta la lista consolidata.

Serve a decidere chi merita una scheda completa senza spendere una scheda completa per scoprirlo. Massimo quindici minuti di ricerca per operatore.

> **Compito.** Per ciascun operatore della lista in `scouting/consolidato.md`, compila una scheda breve — otto campi, non di più. Non approfondire: questo passaggio serve a stabilire una priorità, non a produrre l'analisi.
>
> **Campi.**
> 1. **Linee presidiate** — quali delle nostre quattro, e per ciascuna se è core o accessoria
> 2. **Segmenti serviti** — PMI, enterprise, enti pubblici, acquirenti
> 3. **Dimensione indicativa** — team e, se reperibile, fatturato. Marcare `[S]` se da aggregatore
> 4. **Modello di ricavo apparente** — cosa si intuisce dal sito, senza approfondire
> 5. **Prove di esecuzione** — ci sono clienti nominati e casi documentati, sì o no
> 6. **Segnali di dinamismo** — negli ultimi 12 mesi: raccolte, acquisizioni, nuove linee, assunzioni
> 7. **Sovrapposizione stimata** — alta, media, bassa, nulla, con una riga di motivazione
> 8. **Punteggio di priorità** da 1 a 5, secondo la griglia sotto
>
> **Griglia del punteggio.**
> - **5** — presidia due o più nostre linee sugli stessi segmenti, con prove di esecuzione documentate
> - **4** — presidia una nostra linea core sugli stessi segmenti, con prove
> - **3** — presidia una nostra linea ma su segmenti diversi, oppure senza prove verificabili
> - **2** — sovrapposizione parziale o marginale
> - **1** — rilevante solo come riferimento di modello, non come concorrente
>
> **Vincoli.** Non inventare. Se un campo non è determinabile in pochi minuti, scrivi `da approfondire`: è esattamente il tipo di segnale che serve. Non superare le dieci righe per operatore.
>
> **Formato di uscita.** Una tabella con gli otto campi, ordinata per punteggio decrescente. In coda, tre righe: **quanti operatori per punteggio**, **quali sono i cinque da analizzare per primi**, **quali scarterei e perché**.

---

# FASE 4 — Triage

**Non si delega a un agente.** File di uscita: `scouting/selezione.md`, scritto a mano.

Leggi lo screening e decidi. Criteri suggeriti:

- **Scheda completa** per tutti i punteggio 5 e per i punteggio 4 che presidiano una linea su cui stiamo per fare offerte
- **Scheda ridotta** — solo i campi 1-8 dello screening, già fatti — per i punteggio 3
- **Solo riga nel registro** per i punteggio 1-2
- **Fuori** per chi non rientra nei criteri, con una riga sul perché: serve a non riesaminarlo fra sei mesi

Aggiungi una nota su chi vuoi che veda Roberto prima di procedere: su alcuni operatori la sua conoscenza diretta rende inutile la ricerca desk.

---

# FASE 5 — Schede complete

Un lancio per operatore, **PROMPT 2** del file `02-prompt-agenti.md`, invariato.

Comando da incollare, uno alla volta:

> Esegui il PROMPT 2 di `02-prompt-agenti.md` su **[NOME]** ([URL]). Contesto obbligatorio: `01-metodo-e-schema.md`. Scrivi la scheda in `schede/[slug].md` e la riga dati in `dati/righe/[slug].csv` seguendo esattamente le colonne di `dati/registro.csv`. Aggiungi in coda a `dubbi.md` una sezione con le cose che non hai potuto verificare. Non usare conoscenze pregresse: solo fonti aperte in questa sessione, con URL e data.

**Parallelizzazione.** Puoi tenere aperte tre o quattro sessioni contemporanee, una per operatore, purché ognuna scriva su file propri. Oltre le quattro diventa difficile controllare la qualità.

---

# FASE 6 — Firme verbali e prezzi

Due lanci trasversali su tutta la lista finale: **PROMPT 3** e **PROMPT 4** del file `02-prompt-agenti.md`.

Sul prompt 4, una precisazione dopo quanto emerso su Seedble: **parti dagli appalti pubblici**. Gli importi aggiudicati sono pubblici e verificabili, mentre i prezzi commerciali quasi mai lo sono. Se l'angolo A ha già prodotto importi, riusali invece di ricercarli.

---

# FASE 7 — Sintesi strategica

**PROMPT 5** del file `02-prompt-agenti.md`, un lancio su tutte le schede completate.

---

# FASE 8 — Documento finale

> **Compito.** Costruisci il documento di analisi competitor a partire da: le schede in `schede/`, il registro in `dati/registro.csv`, la sintesi strategica, e la struttura definita al punto 6 di `01-metodo-e-schema.md`.
>
> **Vincoli.**
> - Non introdurre fatti che non siano nelle schede
> - Ogni affermazione numerica mantiene la marcatura di affidabilità
> - La sezione conclusiva contiene **cinque conclusioni operative**: non un riassunto, cinque cose che cambiano quello che facciamo
> - Chiudi con il **registro delle incertezze** costruito da `dubbi.md`
>
> **Formato.** Markdown, sezioni numerate, tabelle dove il confronto è multiplo.

Il documento va poi riletto da una persona prima di girare al team. Il punto di controllo è sempre lo stesso: aprire almeno una fonte per operatore.

---

## Riepilogo dei comandi, in ordine

```
1.  Esegui PROMPT 1A → scouting/a-appalti.md
2.  Esegui PROMPT 1B → scouting/b-osservatori.md
3.  Esegui PROMPT 1C → scouting/c-programmi-corporate.md
4.  Esegui PROMPT 1D → scouting/d-eventi.md
5.  Esegui PROMPT 1E → scouting/e-casi-cliente.md
6.  Esegui PROMPT 1F → scouting/f-annunci-lavoro.md
7.  Esegui PROMPT 1G → scouting/g-estero.md
        ↑ i sette sopra sono parallelizzabili

8.  FASE 2 consolidamento → scouting/consolidato.md
9.  FASE 3 screening → scouting/screening.md
10. FASE 4 triage → scouting/selezione.md          [PERSONA]
11. PROMPT 2, uno per operatore → schede/*.md
12. PROMPT 3 firme + PROMPT 4 prezzi
13. PROMPT 5 sintesi strategica
14. FASE 8 documento finale → revisione umana
```

**Tempo realistico.** Le fasi 1-3 stanno in una giornata di lavoro con più sessioni in parallelo. Le schede complete sono il collo di bottiglia: conta un'ora ciascuna, inclusa la verifica umana. Se dallo screening escono dodici operatori da approfondire, sono tre giornate — ed è il motivo per cui la fase 4 non si salta.
