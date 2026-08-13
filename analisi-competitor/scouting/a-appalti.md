# Angolo 1A — Appalti e gare pubbliche

**Data di esecuzione:** 11/08/2026
**Angolo:** società che negli ultimi 24 mesi (ago 2024 – ago 2026) si sono aggiudicate appalti, gare o affidamenti pubblici in Italia su innovazione / open innovation, trasformazione digitale, adozione di intelligenza artificiale, accelerazione d'impresa, scouting tecnologico, progettazione di programmi di innovazione.
**Fonti:** solo fonti aperte consultate in questa sessione (WebSearch + WebFetch). Ogni riga ha URL e data di consultazione (tutte le consultazioni: 11/08/2026).

## Nota su metodo e limiti dell'ambiente

Il metodo previsto dall'angolo (interrogare banche dati appalti, portali «amministrazione trasparente», determine di aggiudicazione, ricerca per CIG) si è scontrato con vincoli tecnici severi di questo ambiente. In sintesi, cosa ho provato e cosa ha funzionato:

- **TED (ted.europa.eu):** bloccato da robots.txt. Nessun accesso agli avvisi di aggiudicazione europei.
- **ANAC — Portale dati aperti (dati.anticorruzione.it):** richieste respinte da WAF («The requested URL was rejected»). Nessun accesso alla BDNCP.
- **ANAC — Piattaforma di Pubblicità a Valore Legale (pubblicitalegale.anticorruzione.it):** single-page application JavaScript; WebFetch restituisce solo i metadati della pagina, nessun risultato di ricerca. È la fonte che avrebbe risolto l'angolo.
- **Motori di ricerca alternativi** (DuckDuckGo lite, Mojeek, SearXNG) per aggirare l'indicizzazione debole: tutti bloccati (robots.txt, verifica browser o errore server).
- **Ricerca su stampa specializzata italiana** via query WordPress `?s=` (corrierecomunicazioni.it, economyup.it, industriaitaliana.it): bloccata da robots.txt o paywall (402).
- **Budget WebSearch esaurito** a metà lavoro (200/200 chiamate consumate a livello di sessione). Da quel punto ho lavorato solo con WebFetch su URL noti o ricostruiti.
- **Cosa ha funzionato:** (a) API CKAN di dati.gov.it per individuare dataset L.190/2012; (b) API Socrata di dati.lombardia.it, che espone i dataset «Elenco affidamenti beni e servizi» con CIG, oggetto, partecipanti, aggiudicatario e importo, interrogabili full-text; (c) fetch diretto di comunicati aziendali e testate che riportano aggiudicazioni; (d) portale esiti gare del Gruppo FS (gare.ferservizi.it).

**Conseguenza sul risultato:** l'obiettivo di 10-20 operatori non è raggiunto con il livello di prova richiesto. Riporto **4 operatori con aggiudicazione pubblica verificata** e una sezione dubbi con 4 candidati aggiuntivi. Ho preferito non gonfiare l'elenco: le società italiane di open innovation e venture building che il committente considera concorrenti dirette **non sono emerse come aggiudicatarie di appalti pubblici** nelle fonti che sono riuscito a interrogare — e questo è di per sé un risultato (vedi «Limiti» e «Lettura dell'angolo»).

---

## 1. Tabella principale — operatori con aggiudicazione pubblica verificata

| Denominazione | Sito | Sede | Categoria | Linee presidiate | Segmenti | Perché è rilevante (max 20 parole) | Fonte URL |
|---|---|---|---|---|---|---|---|
| GELLIFY | https://gellify.com | Bologna (sedi Milano, Modena, Dubai) | open innovation / venture builder | Open innovation, AI adoption, corporate venture, M&A tech | Corporate, aziende medio-grandi, gruppi pubblici | Unico caso trovato di gara pubblica vinta esattamente sul perimetro WDA: origination, scouting, mentoring, sperimentazione | https://gellify.com/news-and-events/gellify-si-aggiudica-la-gara-di-ferrovie-dello-stato-per-linnovazione/ · https://www.teleborsa.it/News/2024/11/22/gellify-vince-la-gara-di-ferrovie-dello-stato-si-occupera-di-alcuni-servizi-strategici-del-gruppo-167.html (cons. 11/08/2026) |
| Exprivia S.p.A. | https://www.exprivia.it | Molfetta (BA) | sostituto (trasformazione digitale / AI) | AI adoption, trasformazione digitale | PA centrale e locale, sanità, grandi imprese | Mandataria RTI su gara Consip da 86 milioni per digitalizzazione delle PA locali | https://www.lineaedp.it/news/exprivia-si-aggiudica-gara-consip-per-la-digitalizzazione-della-pal/ · https://www.exprivia.it (cons. 11/08/2026) |
| I.S.E.D. S.p.A. (Gruppo expert.ai) | https://www.ised.it | Roma | sostituto (AI / trasformazione digitale) | AI adoption, trasformazione digitale | PA regionali, sanità pubblica | Due aggiudicazioni 2025 su PA regionali (Puglia, Lazio) con componente AI e servizi applicativi | https://www.ised.it/expert-ai-la-controllata-ised-si-aggiudica-la-gara-indetta-da-innovapuglia-s-p-a-per-la-fornitura-dei-servizi-ict-a-supporto-della-trasformazione-digitale-della-pa-della-regione-puglia/ (cons. 11/08/2026) |
| AlmavivA S.p.A. | https://www.almaviva.it | Roma | sostituto (AI adoption / digital) | AI adoption, trasformazione digitale | PA centrale, sanità pubblica, trasporti | Accordo quadro Agenas su teleriabilitazione con AI, realtà aumentata e IoT | https://www.ildenaro.it/intelligenza-artificiale-e-realta-aumentata-per-la-riabilitazione-almaviva-si-aggiudica-la-gara-agenas/ · https://www.almaviva.it (cons. 11/08/2026) |

Siti verificati con WebFetch il 11/08/2026: gellify.com (attivo), exprivia.it (attivo), ised.it (attivo), almaviva.it (attivo).

---

## 2. Tabella aggiudicazioni

| Operatore | Stazione appaltante | Oggetto | Importo | Anno | CIG | Fonte URL | Marcatura |
|---|---|---|---|---|---|---|---|
| GELLIFY | Gruppo Ferrovie dello Stato Italiane | Servizi strategici di innovazione: origination, mentoring, sperimentazione, hub internazionale, reporting, analisi di trend. Gara multi-lotto, GELLIFY aggiudicataria di un lotto | € 8.800.000 (valore complessivo della gara; quota del lotto GELLIFY non dichiarata) — durata 3 anni | 2024 (nov.) | non pubblicato nelle fonti reperite | https://www.teleborsa.it/News/2024/11/22/gellify-vince-la-gara-di-ferrovie-dello-stato-si-occupera-di-alcuni-servizi-strategici-del-gruppo-167.html | [V] (Teleborsa, testata terza) — importo di gara, non di lotto |
| GELLIFY | Gruppo Ferrovie dello Stato Italiane | Stessa gara, comunicato dell'operatore | € 8.800.000 | 2024 | n.d. | https://gellify.com/news-and-events/gellify-si-aggiudica-la-gara-di-ferrovie-dello-stato-per-linnovazione/ | [D] |
| Exprivia S.p.A. (mandataria RTI, 11 imprese) | Consip S.p.A. | Digitalizzazione delle PA locali: sviluppo software, gestione, manutenzione evolutiva, migrazione applicativa in cloud, supporto tecnico-specialistico per Regioni, Comuni, Università, Camere di commercio | € 86.000.000 al raggruppamento — durata 2 anni | 2024 | non riportato nella fonte | https://www.lineaedp.it/news/exprivia-si-aggiudica-gara-consip-per-la-digitalizzazione-della-pal/ | [V] (LineaEDP, testata terza) |
| I.S.E.D. S.p.A. (mandante in RTI, tramite Consorzio Esperia) | InnovaPuglia S.p.A. | Accordo quadro servizi ICT a supporto della trasformazione digitale della PA della Regione Puglia — 2 lotti (sanitario e non sanitario) | Quota I.S.E.D. € 790.000 (Lotto 1: € 1,1 mln totali, € 0,55 mln I.S.E.D.; Lotto 2: € 2,1 mln totali, € 0,24 mln I.S.E.D.). Durata 48 mesi + 48; rilanci competitivi fino a € 32 mln (L1) e € 40 mln (L2) | 2025 | non riportato nella fonte | https://www.ised.it/expert-ai-la-controllata-ised-si-aggiudica-la-gara-indetta-da-innovapuglia-s-p-a-per-la-fornitura-dei-servizi-ict-a-supporto-della-trasformazione-digitale-della-pa-della-regione-puglia/ | [D] (comunicato del gruppo quotato) |
| I.S.E.D. S.p.A. (mandante in RTI) | LAZIOcrea S.p.A. | Servizi di sviluppo software e manutenzione correttiva, evolutiva e adeguativa del Fascicolo Sanitario Elettronico | € 3.900.000 complessivi, di cui € 1.400.000 a I.S.E.D., più € 600.000 per accordo separato di sviluppo tecnologico — fino al 30/06/2026 | 2025 | non riportato nella fonte | https://www.cdr-communication.it/wp-content/uploads/2025/12/CS-Expert-ai-ISED-LAZIOcrea.pdf | [D] (comunicato del gruppo quotato) |
| AlmavivA S.p.A. (mandataria, RTI con BTS Bioengineering) | Agenas — Agenzia Nazionale per i Servizi Sanitari Regionali | Accordo quadro per sistemi di teleriabilitazione (soluzione Helios.Rehab: realtà aumentata, intelligenza artificiale, IoT) | ~ € 10.000.000 — durata 3 anni, con contratti esecutivi attivati dalle aziende sanitarie | 2026 | non riportato nella fonte | https://www.ildenaro.it/intelligenza-artificiale-e-realta-aumentata-per-la-riabilitazione-almaviva-si-aggiudica-la-gara-agenas/ | [V] (Il Denaro, testata terza) |

**Aggiudicazioni con importo trovate: 6** (su 4 operatori). Nessuna delle fonti reperite pubblica il CIG: i comunicati e le testate non lo riportano, e non ho potuto risalire ai provvedimenti di aggiudicazione perché i portali che li contengono (ANAC, TED) non sono accessibili da questo ambiente. **CIG: [N] per tutte e sei le righe.**

### Aggiudicazione verificata ma operatore fuori perimetro (per completezza)

| Operatore | Stazione appaltante | Oggetto | Importo | Anno | CIG | Fonte URL | Marcatura |
|---|---|---|---|---|---|---|---|
| ISFORT S.p.A. | Gruppo FS Italiane (Ferservizi) | Raccolta, produzione ed elaborazione scientifica di dati, ricerche e studi per lo sviluppo di scelte strategiche del Gruppo FS, con banca dati di indagini statistiche (TD 1144/2025/FORN) | non pubblicato nella scheda esito | 2025 | **B92B89D14D** | https://www.gare.ferservizi.it/it/esiti/ferservizi/servizi/td--1144-2025-forn---servizio-di-raccolta--produzione-ed-elabora.html | [V] (portale esiti della stazione appaltante) |
| Atlante Group S.r.l. | Regione Lombardia — Giunta Regionale (GECA 7/2024) | Servizio di supporto specialistico per le attività legate alla digitalizzazione dei beni culturali lombardi | € 420.000 | 2024 | **B0FE90D1BC** | https://www.dati.lombardia.it/resource/9c3a-vjtn.json (dataset «Elenco affidamenti beni e servizi 2024», query full-text «digitalizzazione») | [V] (open data della stazione appaltante) |

ISFORT è un istituto di ricerca sui trasporti: non presidia nessuna delle quattro linee. Atlante Group: aggiudicazione verificata con CIG e importo, ma **non ho potuto verificare un sito attivo** (il dominio atlantegroup.it non risolve), quindi non entra in tabella principale — vedi dubbi.

---

## 3. Dubbi — candidati con evidenza debole

Operatori con sito attivo verificato e attività coerente con le linee del committente, ma **senza aggiudicazione verificata** nelle fonti accessibili. Li segnalo perché l'evidenza raccolta è comunque documentale e riferita a procedure con CIG.

| Candidato | Sito (verificato 11/08/2026) | Cosa fa | Evidenza raccolta | Perché resta un dubbio |
|---|---|---|---|---|
| DINTEC — Consorzio per l'Innovazione Tecnologica S.c.r.l. | https://www.dintec.it (attivo) | Agenzia in house di Unioncamere, Camere di commercio ed ENEA. Linee: innovazione e digitalizzazione, trasferimento tecnologico, poli di innovazione, digitalizzazione PMI, PID Academy. Sede Roma | Risulta **operatore invitato/partecipante** a più procedure negoziate di Regione Lombardia nel 2024: CIG B059EA242B (€ 83.400), CIG B1565A6E0C (€ 46.000), CIG B2C48CBC85 (€ 99.802,62), CIG B292C6249B (€ 131.500). Fonte: https://www.dati.lombardia.it/resource/9c3a-vjtn.json | Nel dataset risulta partecipante, non aggiudicatario [V per la partecipazione, N per l'aggiudicazione]. Essendo in house camerale, opera prevalentemente per affidamento diretto: gli importi non emergono dalle gare |
| t2i — trasferimento tecnologico e innovazione s.c.a r.l. | https://www.t2i.it (attivo) | Consortile camerale veneto: trasferimento tecnologico, trasformazione digitale, AI e automazione, proprietà intellettuale, incubazione certificata (Rovigo). Sede Treviso | Partecipante a procedure Regione Lombardia 2024: CIG B059EA242B (€ 83.400), CIG B1565A6E0C (€ 46.000), CIG B42B8E17F6. Fonte: https://www.dati.lombardia.it/resource/9c3a-vjtn.json | Stessa situazione di Dintec: partecipazione verificata, aggiudicazione [N] |
| Atlante Group S.r.l. | dominio atlantegroup.it non risolvibile — **sito [N]** | Supporto specialistico a Regione Lombardia sulla digitalizzazione dei beni culturali | Aggiudicataria confermata: CIG B0FE90D1BC, € 420.000, 2024 (open data Regione Lombardia) | Ha l'aggiudicazione ma non il sito verificabile, e l'oggetto (digitalizzazione di patrimonio culturale) è più vicino ai servizi documentali che all'open innovation |
| SPICI S.r.l. | spici.it — **non verificabile** (robots.txt non raggiungibile) | Consulenza su politiche dell'innovazione (da denominazione e contesto delle procedure) | Partecipante a procedure Regione Lombardia 2024: CIG B059EA242B (€ 83.400), CIG B0BC02363D (€ 119.000), CIG B3EB3DA9D2 (€ 100.000) | Né sito verificato né aggiudicazione verificata: candidato solo da riprendere con strumenti migliori |

**Nota di igiene sull'esclusione.** Nelle stesse procedure Regione Lombardia 2024 compare ripetutamente **Officine Innovazione S.r.l. Società Benefit** (Deloitte), già mappata e quindi esclusa dal riporto. Il dato è comunque informativo: nella committenza regionale lombarda l'assistenza tecnica va prevalentemente a operatori già noti al committente.

---

## 4. Limiti della ricerca

**Cosa non sono riuscito a coprire, e perché.**

1. **Nessun accesso alle banche dati appalti.** TED, ANAC-BDNCP e la Piattaforma di Pubblicità a Valore Legale ANAC — cioè le tre fonti che avrebbero risposto direttamente all'angolo — sono risultate rispettivamente bloccate da robots.txt, respinte da WAF e non leggibili perché SPA JavaScript. Senza queste, la ricerca «per CIG» e «per oggetto di gara» su scala nazionale è impossibile in questo ambiente.
2. **CIG mancanti su tutte le aggiudicazioni della tabella 2.** Le uniche fonti utilizzabili (comunicati e testate) non pubblicano il CIG. I due CIG che riporto (B92B89D14D, B0FE90D1BC) vengono da portali di stazione appaltante e da open data, non dalle sei aggiudicazioni principali.
3. **Portali di agenzie regionali per l'innovazione: non consultabili.** Sardegna Ricerche (robots.txt irraggiungibile, due tentativi), ART-ER (idem), Lazio Innova (la sezione «appalti in corso» esiste ma non pubblica esiti né CIG; nessuna gara su innovazione/accelerazione tra quelle esposte: payroll, crediti Azure, internal audit, assicurazioni). Non ho potuto verificare Sviluppumbria, Finpiemonte, Puglia Sviluppo, InnovaPuglia, Trentino Sviluppo, Veneto Innovazione, Sviluppo Toscana, ARIA Lombardia: senza motore di ricerca non ho potuto ricostruire gli URL delle loro sezioni esiti.
4. **Budget di ricerca esaurito.** Le 200 chiamate WebSearch disponibili per la sessione si sono consumate a metà lavoro, e tutti i motori alternativi sono bloccati. Da quel momento ogni nuova pista richiedeva di indovinare un URL.
5. **Ricerche che non hanno prodotto nulla, pur essendo state eseguite.** Query su «scouting tecnologico» + CIG, «servizi di open innovation» + aggiudicazione, «programma di accelerazione» + affidamento, «gestione dell'incubatore» + gara, «servizi di incubazione e accelerazione», «soggetti attuatori» + accelerazione: nessuna ha restituito un provvedimento di aggiudicazione. Il motore di ricerca disponibile è tarato su risultati statunitensi e non indicizza in profondità le determine italiane.
6. **Interrogazioni open data a esito negativo (informative).** Sul dataset «Elenco affidamenti beni e servizi 2024» di Regione Lombardia (~ tutte le procedure della Giunta con CIG, oggetto, importo e aggiudicatario) le query full-text su **«intelligenza artificiale»** e **«scouting»** hanno restituito **zero record**. La query su «innovazione» restituisce solo società che hanno «innovazione» nella ragione sociale, non oggetti di gara sull'innovazione. Regione Lombardia non pubblica il dataset 2025 né 2026: la serie si ferma al 2024.
7. **Piste aperte non chiuse.** (a) La gara FS Italiane sull'innovazione è multi-lotto: gli altri lotti sono stati aggiudicati ad altri operatori, che sarebbero i concorrenti più diretti del committente, ma l'esito completo non è reperibile sul portale esiti di Ferservizi, che espone solo gli avvisi recenti. (b) L'RTI Consip vinto da Exprivia comprende 11 imprese non nominate dalla fonte. (c) La rete degli acceleratori CDP Venture Capital seleziona i gestori con call pubbliche, che non transitano da CIG e quindi non emergono con questo metodo.

**Lettura dell'angolo.** Al netto dei limiti tecnici, un dato sostanziale emerge e va detto: **il mercato pubblico italiano di questi servizi non è strutturato come «gare di open innovation»**. Con l'eccezione della gara FS vinta da GELLIFY, gli appalti che intercettano il perimetro del committente sono classificati come servizi ICT e trasformazione digitale, e vanno a system integrator (Exprivia, AlmavivA, I.S.E.D./expert.ai) e, per l'assistenza tecnica ai programmi, a consulenti già mappati (Officine Innovazione/Deloitte) o a in house camerali (Dintec, t2i). Chi fa open innovation e venture building «puro» in Italia sembra vendere fuori dal canale appalti — via affidamento diretto sotto soglia, via bandi a cascata, o direttamente a corporate e società partecipate. Se l'ipotesi regge, l'angolo appalti è più utile per mappare **sostituti** (integratori e advisor PA) che concorrenti diretti; la verifica richiede però l'accesso alla BDNCP ANAC, che qui non è stato possibile.
