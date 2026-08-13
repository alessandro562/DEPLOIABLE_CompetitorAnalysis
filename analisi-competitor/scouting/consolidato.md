# FASE 2 — Consolidamento dello scouting competitor

**Data di elaborazione:** 11/08/2026
**Data di consultazione delle verifiche svolte in questa fase:** 11/08/2026

## Fonti consolidate

Sette file prodotti dagli angoli di scouting, letti integralmente:

| Sigla | File | Angolo | Righe in tabella principale |
|---|---|---|---|
| A | `a-appalti.md` | Appalti e gare pubbliche | 4 |
| B | `b-osservatori.md` | Osservatori e associazioni di categoria (Open Innovation Lookout PoliMi) | 44 |
| C | `c-programmi-corporate.md` | Gestori di programmi corporate e acceleratori | 14 |
| D | `d-eventi.md` | Relatori, sponsor ed espositori di eventi di settore | 15 |
| E | `e-casi-cliente.md` | Fornitori citati nei materiali ufficiali dei clienti | 11 |
| F | `f-annunci-lavoro.md` | Annunci di lavoro e nuovi entranti | 20 |
| G | `g-estero.md` | Operatori esteri come riferimenti di modello | 12 |

Totale righe grezze in ingresso: **120**.

## Metodo di deduplica applicato

1. **Unità di conteggio = l'operatore, non la denominazione.** Sono state unificate le varianti di denominazione («Opinno» / «Opinno Italia» / «Opinno Italy»; «Plug and Play Italy» / «Plug and Play (Italia)»; «Twenty Ventures» / «20V»; «Consorzio ELIS» / «ELIS Innovation Hub»; «Nana Bianca S.r.l.» / «Nana Bianca»; «CiaoTech» / «PNO Innovation Italy»; «Mind The Bridge» / «Mind the Bridge»; «OrgTech S.r.l.» / «Humagine»; «Warrant Hub» / «Tinexta Innovation Hub»; «AC75 Startup Accelerator S.p.A.» / «AC75»).
2. **La provenienza conta la tabella principale, non le sezioni dubbi.** Un operatore «emerso da un angolo» è un operatore che quell'angolo ha messo nella propria tabella principale. Le citazioni nelle sole sezioni dubbi di altri angoli sono riportate come annotazione fra parentesi nella colonna «Angoli di provenienza» ma **non incrementano** il numero di angoli. È una scelta conservativa: una menzione nei dubbi è un'evidenza più debole di una riga di tabella, e gonfiarne il peso falserebbe il segnale «3+ angoli».
3. **Gli operatori dell'angolo G non sono mai fusi con quelli di A-F** e stanno in tabella separata: sono riferimenti di modello, non concorrenti.
4. **Gli operatori esteri con presidio italiano emersi dagli angoli A-F restano in Tabella A** (Plug and Play, Opinno, Eatable Adventures, Startup Wise Guys, Wazoku, NineSigma, Mind the Bridge, BCG X, Devoteam, Ayming, Leyton, Fincons): competono davvero sulle commesse italiane. Sono segnalati con la nota «estero con presidio italiano».
5. **Le marcature di affidabilità degli angoli sono mantenute:** `[V]` verificato da fonte terza · `[D]` dichiarato dall'operatore · `[S]` aggregatore/osservatorio · `[N]` non trovato.
6. **Non sono stati aggiunti operatori nuovi.** Ogni riga di questo file proviene da uno dei sette file. Le uniche informazioni nuove sono gli esiti delle verifiche di dominio svolte in questa fase.

### Verifica di esistenza dei domini — cosa ho fatto e cosa no

Il tentativo di verifica massiva via `curl` è fallito: il proxy di egress di questo ambiente ha risposto **403 a tutte le CONNECT verso host esterni** (policy di organizzazione; il README del proxy prescrive di segnalare, non di aggirare). La verifica è quindi stata fatta con **WebFetch**, dando priorità — come da istruzioni — ai domini emersi da **un solo angolo** e a quelli **mai fetchati dagli agenti precedenti**.

- **Domini interrogati in questa fase: 66.**
- **Risolti e coerenti con l'operatore atteso: 52.**
- **Non risolti, morti o divergenti: 4** (`gfactor.it`, `aiventurebuilder.com`, `warranthub.it`, `djungle.io`) — dettaglio in §4.
- **Non verificabili per blocco tecnico: 10** (`k-digitale.com`, `e12.it`, `arsenalia.it`, `soft-strategy.com`, `ciaotech.com`, `pnoconsultants.com/it`, `devoteam.com/it`, `thedoers.co`, più `strategyinnovation` che non ha dominio dichiarato e `teamdev` la cui sede resta ND).
- **Non re-interrogati in questa fase, perché già fetchati e dichiarati attivi dagli agenti precedenti (17):** `gellify.com`, `exprivia.it`, `ised.it`, `almaviva.it` (angolo A); `infinitearea.com`, `nanabianca.it`, `startup-bakery.com` (angolo B); `almacube.com`, `wylab.net`, `socialfare.org`, `plugandplaytechcenter.com`, `eatableadventures.com`, `h-farm.com` (angolo C); `cefriel.com`, `mindthebridge.com`, `innovationmatch.io` (angoli D/E); `i3p.it` (angolo E).
- **I 12 domini esteri della Tabella B non sono stati re-interrogati:** l'angolo G dichiara di aver letto direttamente ciascun sito il 11/08/2026.

---

## 2. Tabella A — operatori italiani (e operatori esteri con presidio italiano)

Ordinata per numero di angoli decrescente. `OI` = open innovation · `VB` = venture building su commissione · `AI` = AI adoption · `M&A` = assistenza ad acquisizioni.

### 2.1 Emersi da 3 o più angoli — priorità massima

| Denominazione | Sito | Sede | Categoria | Linee presidiate | Segmenti | Perché è rilevante | Angoli di provenienza | N. angoli | Fonte URL principale |
|---|---|---|---|---|---|---|---|---|---|
| **GELLIFY** | https://gellify.com | Casalecchio di Reno (BO), Milano, Modena, Dubai | Innovation factory: consulenza + venturing | OI, VB, AI, M&A | Corporate, aziende 40M+, PMI, gruppi pubblici | Unico operatore su tutti i canali: gara pubblica FS vinta, censimento PoliMi, due acceleratori CDP, eventi, referenza cliente Ducati | A, B, C, D, E (+cit. dubbi F) | **5** | https://gellify.com/news-and-events/gellify-si-aggiudica-la-gara-di-ferrovie-dello-stato-per-linnovazione/ `[V]` |
| **Nana Bianca S.r.l.** | https://nanabianca.it | Firenze | Startup studio + gestore acceleratori su commessa | VB, OI | Corporate, PMI, enti pubblici | Startup studio dal 2012 con 7 programmi su commessa; opera l'Italian Lifestyle Program per Intesa Sanpaolo Innovation Center | B, C, D | **3** | https://italianlifestyleprogram.it/ `[V]` |
| **Plug and Play Italy** *(estero con presidio italiano)* | https://www.plugandplaytechcenter.com | Milano, Modena, Torino (HQ USA) | Acceleratore corporate + piattaforma OI a sottoscrizione | OI, M&A/scouting | Corporate, aziende 40M+ | Quattro clienti la citano sui propri canali (Marelli, Nexi, A2A, Esselunga): referenza più solida del panel; due acceleratori CDP | C, D, E | **3** | https://www.marelli.com/en/news/marelli-partners-with-plug-and-play-motor-valley-accelerator.html `[V]` |
| **ELIS Innovation Hub (Consorzio ELIS)** | https://www.elis.org | Roma | Hub consortile di corporate innovation | OI, AI | Aziende 40M+, filiere di PMI, enti pubblici | Coordina Open Italy con ~140 grandi imprese, due acceleratori CDP e Terna Innovation Zone; citata da Poste e FS Italiane | C, E, F (+cit. dubbi D) | **3** | https://www.elis.org/innovation-hub/open-innovation/ `[V]` |
| **SocialFare — Impresa Sociale S.r.l.** | https://socialfare.org | Torino | Centro per l'innovazione sociale, incubatore certificato + seed fund | OI, VB | Enti pubblici, fondazioni, corporate, PMI | Co-gestore dell'acceleratore CDP Personae, FOUNDAMENTA decennale, call Planet Foundamentals 2026 aperta | C, E, F | **3** | https://socialfare.org/ `[V]` |
| **Opinno (Opinno Italy)** *(estero con entità italiana)* | https://www.opinno.com | Milano, Roma, Torino, Catania (HQ San Francisco/Madrid) | Consulenza open innovation internazionale | OI, VB, AI | Corporate (40+ Fortune 500), PMI, enti pubblici | Presidia esplicitamente il corporate venture building; unica boutique di innovazione con posizione junior aperta in Italia | B, D, F | **3** | https://www.openinnovationlookout.it/player/opinno/ `[S]` |

### 2.2 Emersi da 2 angoli

| Denominazione | Sito | Sede | Categoria | Linee presidiate | Segmenti | Perché è rilevante | Angoli di provenienza | N. angoli | Fonte URL principale |
|---|---|---|---|---|---|---|---|---|---|
| Almacube S.r.l. | https://www.almacube.com | Bologna (+ Valenzano, BA) | Innovation hub societario (soci UniBo, Confindustria Emilia, Fondazione Golinelli) | OI, venture clienting | Corporate, PMI, enti pubblici | Gestisce Good Food Makers di Barilla dal 2019 ed è citata da Philip Morris Italia sul sito del programma BeLeaf | C, E | 2 | https://www.beleafbethefuture.com/ `[V]` |
| Wylab S.r.l. (Tigullio Digital) | https://wylab.net | Chiavari (GE), La Spezia, Roma | Gestore acceleratori corporate e call for startup | OI, VB | Aziende 40M+, enti pubblici | Acceleratori CDP (FAROS, We Sport Up, VitalMatch) e call proprietarie per Illumia, Crédit Agricole, Sport e Salute | C, E | 2 | https://wylab.net/open-innovation/ `[D]`+`[V]` |
| Eatable Adventures *(estero con presidio italiano)* | https://eatableadventures.com | Hub Verona (HQ Madrid) | Acceleratore/venture builder foodtech | OI, VB | Corporate food & retail, PMI | Gestore unico di FoodSeed con Amadori, Veronafiere, UniCredit; si posiziona come innovation partner dell'agroalimentare italiano | C, E | 2 | https://foodseed.it/ `[V]` |
| Cefriel S.cons.r.l. (Società Benefit) | https://www.cefriel.com | Milano | Centro di innovazione consortile (PoliMi + imprese) | AI, OI | Aziende 40M+, PMI, PA | Offerta commerciale piena su AI & data e business transformation; Gold Sponsor AI Forum 2025 | D, E | 2 | https://www.cefriel.com/it `[D]` |
| Startup Bakery | https://startup-bakery.com | Milano (Via C. Farini 5) | Startup studio | VB, AI | PMI e aziende medio-grandi, corporate | Dichiara venture building su commissione per PMI e medio-grandi: verticale B2B SaaS + AI | B, D (+cit. dubbi E, F) | 2 | https://www.openinnovationlookout.it/player/startup-bakery/ `[S]` |
| Mind the Bridge *(estero con presidio italiano)* | https://mindthebridge.com | San Francisco + Italia | Advisory di open innovation + ricerca | OI, M&A | Corporate, corporate VC | Scouting e corporate-startup deal con ricerca proprietaria; organizza lo Scaleup Summit di Torino | B, D (+cit. dubbi F) | 2 | https://mindthebridge.com/ `[D]` |
| Innovation Match S.r.l. | https://www.innovationmatch.io | Milano | Piattaforma + servizi di open innovation | OI | PMI, aziende 40M+, corporate | Costruisce posizionamento organizzando eventi propri: Spark! Summit, Innovation Meetup, Open Innovation Awards | B, D | 2 | https://www.economyup.it/innovazione/spark-innovation-summit-2025-il-30-ottobre-levento-sullopen-innovation/ `[V]` |
| Grownnectia S.r.l. | https://www.grownnectia.com | Roma, Desenzano del Garda (BS) | Advisory + acceleratore per PMI e startup | OI, VB, AI | PMI, startup, aziende 40M+ | Vende Hackstorm (hackathon aziendale 48 ore) e percorsi di AI transition; sei posizioni aperte | C, F | 2 | https://www.grownnectia.com/eventi-innovazione-aziende/ `[D]` |
| CiaoTech S.r.l. / PNO Innovation Italy (PNO Group) | ciaotech.com · pnoconsultants.com/it — **non verificabili in questa sessione** | Milano, Roma | Innovation consulting e finanza per l'innovazione | OI | PMI, corporate, enti pubblici | Presidio storico sulle PMI industriali; annuncio Innovation Consultant Manufacturing a Roma | B, F | 2 | https://www.openinnovationlookout.it/categoria_player/societa-di-consulenza-open-innovation/ `[S]` |
| BIP — Business Integration Partners | https://www.bip-group.com | Milano, Roma | Consulenza direzionale e tecnologica italiana | AI, OI, M&A | Corporate 40M+, enti pubblici | Consulenza italiana di scala con practice xTech; volume di annunci più alto fra le italiane | B, F | 2 | https://www.bip-group.com `[D]` |

### 2.3 Emersi da 1 angolo

| Denominazione | Sito | Sede | Categoria | Linee presidiate | Segmenti | Perché è rilevante | Angoli di provenienza | N. angoli | Fonte URL principale |
|---|---|---|---|---|---|---|---|---|---|
| Exprivia S.p.A. | https://www.exprivia.it | Molfetta (BA) | Sostituto: system integrator / trasformazione digitale | AI, digital transformation | PA centrale e locale, sanità, grandi imprese | Mandataria di un RTI di 11 imprese su gara Consip da 86 mln per la digitalizzazione delle PA locali | A | 1 | https://www.lineaedp.it/news/exprivia-si-aggiudica-gara-consip-per-la-digitalizzazione-della-pal/ `[V]` |
| I.S.E.D. S.p.A. (gruppo expert.ai) | https://www.ised.it | Roma | Sostituto: AI / trasformazione digitale | AI | PA regionali, sanità pubblica | Due aggiudicazioni 2025 su PA regionali (InnovaPuglia, LAZIOcrea) con componente AI | A | 1 | https://www.ised.it/expert-ai-la-controllata-ised-si-aggiudica-la-gara-indetta-da-innovapuglia-s-p-a-per-la-fornitura-dei-servizi-ict-a-supporto-della-trasformazione-digitale-della-pa-della-regione-puglia/ `[D]` |
| AlmavivA S.p.A. | https://www.almaviva.it | Roma | Sostituto: AI adoption / digital | AI | PA centrale, sanità pubblica, trasporti | Accordo quadro Agenas da ~10 mln su teleriabilitazione con AI, realtà aumentata e IoT | A | 1 | https://www.ildenaro.it/intelligenza-artificiale-e-realta-aumentata-per-la-riabilitazione-almaviva-si-aggiudica-la-gara-agenas/ `[V]` |
| Infinite Area | https://www.infinitearea.com | Montebelluna (TV) | Società di consulenza open innovation | OI | Corporate, PMI, spin-off | Technology scouting, feasibility e proof-of-concept per programmi corporate di innovazione | B (+cit. dubbi D, F) | 1 | https://www.openinnovationlookout.it/player/infinite-area/ `[S]` |
| iN3 Ventures | https://in3.ventures | Milano (Largo Donegani 2) | Società di consulenza open innovation | OI, M&A | Multinazionali, corporate | Corporate Lab, Startup Radar e Deal Analysis su partnership e acquisizioni: copre OI + M&A | B (+cit. dubbi D, F) | 1 | https://www.openinnovationlookout.it/player/in3-ventures/ `[S]` |
| OrgTech S.r.l. (brand Humagine) | https://www.humagine.it (orgtech.it reindirizza 302) | Milano | Consulenza OI censita, **oggi trasformazione organizzativa** | OI, AI (posizionamento attuale: HR/organizzativo) | Corporate (es. Heineken Italia) | Censita come consulenza OI, ma il sito verificato oggi vende sviluppo organizzativo e coaching: rischio di ricadere nelle esclusioni | B (+cit. dubbi D, F) | 1 | https://www.openinnovationlookout.it/player/orgtech-s-r-l/ `[S]` |
| Indicon Società Benefit | https://www.indicon-innovation.tech | Milano | Consulenza OI verticale life science | OI | Big pharma, startup life science | Innovation management life science: ponte fra startup e grandi farmaceutiche | B (+cit. dubbi D, F) | 1 | https://www.openinnovationlookout.it/player/indicon-societa-benefit/ `[S]` |
| Buono & Partners | https://www.buonopartners.com | Roma (Via Mercalli 13) | Boutique di consulenza strategico-relazionale | OI, M&A | Corporate, istituzioni | Dichiara supporto a operazioni straordinarie e intermediazione di capitali oltre all'ecosistema OI | B | 1 | https://www.openinnovationlookout.it/player/buono-partners/ `[S]` |
| K-Digitale S.r.l. | k-digitale.com — **non verificabile** (timeout su robots.txt) | Perugia | Consulenza OI, deep tech | OI, AI | PMI, corporate | Consulenza open innovation con specializzazione deep tech; presidio del Centro Italia | B (+cit. dubbi D, F) | 1 | https://www.openinnovationlookout.it/player/k-digitale-srl/ `[S]` |
| TeamDev S.r.l. | https://www.teamdevecosystem.it | ND `[N]` | Consulenza OI / software GIS, smart city, IoT | OI, AI | Corporate, PA | Fatturato dichiarato €2-10M con quota OI; sito verificato ma il profilo è più software che advisory | B | 1 | https://www.openinnovationlookout.it/player/teamdev-srl/ `[S]` |
| BTO Research (BTO — Digital Renaissance) | https://www.btoresearch.com | ND `[N]` | Consulenza OI + ricerca | OI, AI | Corporate, PMI | Digital trend analysis, selezione software e report su commessa; scheda Lookout priva di dati | B (+cit. dubbi D, F) | 1 | https://www.openinnovationlookout.it/player/bto-research/ `[S]` |
| StrategyInnovation | **nessun dominio dichiarato** `[N]` | ND `[N]` | Consulenza open innovation | OI | Corporate, PMI | Censita dal Lookout, ma la scheda non espone né sito né sede né dati: esistenza non verificabile | B (+cit. dubbi D, F) | 1 | https://www.openinnovationlookout.it/player/strategyinnovation/ `[S]` |
| Warrant Hub → **Tinexta Innovation Hub S.p.A.** (gruppo Tinexta) | https://www.tinextainnovationhub.com (warranthub.it reindirizza 302) | Correggio (RE) | Consulenza su finanza agevolata e innovazione | OI | PMI, corporate, enti pubblici | Grande rete con forte penetrazione PMI; il brand Warrant Hub è confluito nel nuovo Tinexta Innovation Hub | B | 1 | https://www.tinextainnovationhub.com/ `[V]` (verifica 11/08/2026) |
| Wazoku *(estero, opera in Italia)* | https://www.wazoku.com | Regno Unito | Piattaforma + servizi di crowdsourcing dell'innovazione | OI | Corporate, enti pubblici, accademia | Vende sia licenza sia challenge management as-a-service: la soglia software/servizio resta da verificare | B | 1 | https://www.openinnovationlookout.it/categoria_player/societa-di-consulenza-open-innovation/ `[S]` |
| NineSigma *(estero, opera in Italia)* | https://www.ninesigma.com | USA / Europa | Broker di open innovation e technology scouting | OI | Corporate | Broker storico di open innovation e scouting tecnologico su commessa corporate | B | 1 | https://www.openinnovationlookout.it/categoria_player/societa-di-consulenza-open-innovation/ `[S]` |
| FoolFarm S.r.l. | https://www.foolfarm.com | Milano | Venture builder AI-native | VB, AI | Corporate, investitori | Venture builder AI-native che dichiara anche corporate venture building; oltre €8,15M investiti | B (+cit. dubbi D, F) | 1 | https://www.openinnovationlookout.it/player/foolfarm/ `[S]` |
| Alien Technology Transfer | https://alientt.com | Roma (Via C. Colombo 348) | Censita venture builder, **oggi grant advisory** | VB, OI | Corporate, startup | Il sito verificato (giugno 2026) vende oggi grant funding non diluitivo UE/USA, non venture building | B | 1 | https://www.openinnovationlookout.it/player/alien/ `[S]` |
| CubeLabs S.p.A. | https://www.cube-labs.com | Roma (Via G. Caccini 1) | Venture builder healthcare, quotata Euronext Growth Milan | VB | Healthcare, life science, corporate | Venture builder verticale healthcare attivo dal 2013, con struttura quotata | B (+cit. dubbi F) | 1 | https://www.openinnovationlookout.it/player/cubelabs-milano/ `[S]` |
| Day One S.r.l. | https://www.day-one.biz | Roma (V.le Oceano Atlantico 18) | Innovation studio deeptech | VB, OI | Ricerca, deeptech, corporate | Finanzia e porta a mercato tecnologie di ricercatori europei; venture building + technology transfer | B (+cit. dubbi F) | 1 | https://www.openinnovationlookout.it/player/dayone/ `[S]` |
| Enry's Island S.p.A. Benefit | https://www.enrysisland.com | Isole Tremiti (FG) | Venture builder quotato (Vienna Stock Exchange, EIOS) | VB | Corporate, investitori, imprenditori | Piattaforma di venture building con 25+ startup; unico venture builder dichiaratamente quotato | B | 1 | https://www.openinnovationlookout.it/player/enrys-island/ `[S]` |
| Feat. Ventures | https://featventures.com | Torino (Via M. Gioia 11) | Venture builder | VB | Corporate, industry expert | Co-creazione di digital venture con industry expert come cofondatori: modello vicino a quello del committente | B (+cit. dubbi F) | 1 | https://www.openinnovationlookout.it/player/feat-ventures/ `[S]` |
| Enzima12 | e12.it — **non verificabile** (errore certificato SSL) | Milano (Via L. Manara 15) | Venture builder | VB | Edtech, servizi per il lavoro | Crea, abilita e lancia società nei servizi per formazione e lavoro | B (+cit. dubbi F) | 1 | https://www.openinnovationlookout.it/player/enzima12/ `[S]` |
| Twenty Ventures / 20V (Twenty Investments Holding S.r.l.) | https://20v.it | Roma | Venture builder / startup studio + fondi early stage | VB | Founder pre-seed, corporate | Ecosistema integrato che combina venture building, advisory strategica e fondi early-stage | B | 1 | https://www.openinnovationlookout.it/player/twenty-ventures/ `[S]` |
| Archangel ADVenture S.r.l. | https://www.archangeladventure.it | Roma (V.le Angelico 34) | Venture builder | VB | Corporate, startup | Venture builder romano fondato nel 2020, dimensione comparabile a quella del committente | B | 1 | https://www.openinnovationlookout.it/player/archangel-adventure/ `[S]` |
| Venture Architect S.r.l. | https://www.venturearchitect.it | Milano (Via Trebazio 4) | Growth equity advisory boutique | VB, M&A | PMI, startup | Sito verificato: business model innovation, incubazione e advisory di growth equity per PMI | B (+cit. dubbi F) | 1 | https://www.openinnovationlookout.it/player/venture-architect/ `[S]` |
| Magnisi S.r.l. | https://www.magnisi.com | Palermo (Via E. Amari 148) | Venture studio a impatto + formazione AI | VB, AI | Impact, corporate, PMI | Ecosistema mediterraneo che porta capitale, strategia e formazione AI alle imprese: presidio Sud Italia | B | 1 | https://www.openinnovationlookout.it/player/magnisi/ `[S]` |
| Kitzanos Soc. Coop. | https://www.kitzanos.com | Cagliari | Venture builder + innovation hub | VB, OI | **PMI**, startup, scaleup | Tre linee, fra cui la consulenza direzionale per PMI: sovrapposizione di segmento | B | 1 | https://www.openinnovationlookout.it/player/kitzanos-soc-coop-arl/ `[S]` |
| TechBricks | https://www.techbricks.io | Roma (Via V. Orsini 19) | Venture studio / tech lab | VB, OI, AI | Corporate, startup, ricerca | Venture studio deep tech; il sito oggi enfatizza i founder mission-driven più dell'OI per imprese | B (+cit. dubbi F) | 1 | https://www.openinnovationlookout.it/player/techbricks/ `[S]` |
| Djungle Studio | djungle.io — **dominio divergente** (serve una pagina generata con Lovable) | Torino | Startup studio | VB, OI | Corporate | Startup factory che valida, crea e itera modelli di business digitali; sito dichiarato non più coerente | B (+cit. dubbi E) | 1 | https://www.openinnovationlookout.it/player/djungle-studio/ `[S]` |
| Mamazen S.r.l. | https://www.mamazen.it | Torino (Via Bossolasco 11) | Startup studio | VB | **Micro-imprese, artigiani** | Startup studio verticale su micro-business: segmento contiguo ma distinto dalle PMI 40M+ | B (+cit. dubbi E) | 1 | https://www.openinnovationlookout.it/player/mamazen/ `[S]` |
| Rainmakers S.r.l. | https://www.rainmakers.it | Milano (Via Carducci 8) | Startup studio | VB | Corporate, founder | Fra i più longevi (dal 2011), ma l'ultima modifica del sito risulta 2021: **attività recente non provata** | B | 1 | https://www.openinnovationlookout.it/player/rainmakers-s-r-l/ `[S]` |
| Opificio137 | https://www.opificio137.com | Milano (Via Ripamonti 137) | Venture builder digital media | VB, AI | Media, creator, corporate | Venture builder su digital communication e tool AI-driven; fondato 2022 | B (+cit. dubbi E) | 1 | https://www.openinnovationlookout.it/player/opificio137/ `[S]` |
| Feedel Ventures | https://feedel.ventures | Latiano (BR) | Startup studio | VB | Corporate, founder | Idea lab e startup factory con oltre 20 startup a portafoglio; presidio Sud Italia | B (+cit. dubbi E) | 1 | https://www.openinnovationlookout.it/player/feedel-ventures/ `[S]` |
| Start Factor | https://www.startfactor.it | Milano (Via Carducci 8) | Startup studio insurtech | VB | Insurtech, compagnie assicurative | Venture building verticale assicurativo: crea startup e fa consulenza strategica alle compagnie | B (+cit. dubbi E) | 1 | https://www.openinnovationlookout.it/player/start-factor/ `[S]` |
| Finnovaction | https://www.finnovaction.com | Milano (Via F. D'Ovidio 3) | Startup studio fintech | VB | Fintech, banche, investitori | Primo startup studio fintech italiano, oggi fintech+AI: contiguo al segmento banche | B (+cit. dubbi F) | 1 | https://www.openinnovationlookout.it/player/finnovaction/ `[S]` |
| ZNEXT S.r.l. (gruppo Zanichelli Editore) | https://znext.io | Bologna | Venture builder corporate internalizzato | VB, M&A | Editoria, edtech, future of work | Venture builder lanciato da Zanichelli nel 2025; dichiara venture building **e M&A**: non solo in-house | B | 1 | https://www.economyup.it/innovazione/startup-studio-che-cosa-sono-come-funzionano-le-fabbriche-di-startup-e-quali-sono-in-italia/ `[S]` |
| 12Venture | https://12venture.com | Italia | Startup studio EdTech/HRtech | VB | EdTech, HRtech | Startup studio verticale fondato 2023, censito sia dal Lookout sia da Economyup | B (+cit. dubbi F) | 1 | https://www.openinnovationlookout.it/categoria_player/venture-builders-startup-studio/ `[S]` |
| a\|cube SB S.r.l. (gruppo Avanzi) | https://acube.avanzi.org | Milano | Gestore acceleratori impact, incubatore certificato | OI, VB | Aziende 40M+, enti pubblici | Co-gestore di due acceleratori CDP (FAROS, Personae) e advisor del fondo a\|impact | C | 1 | https://acube.avanzi.org/chi-siamo/ `[D]` |
| AC75 Startup Accelerator S.p.A. | https://www.ac75sa.com | Ancona | Gestore acceleratori verticali | OI, VB | Aziende 40M+, enti pubblici | Gestore unico di NextAge (silver economy) per CDP dal 2022; programmi per spin-off e territorio | C | 1 | https://www.ac75sa.com/accelerator/ `[D]`+`[V]` |
| Startup Wise Guys *(estero con presidio italiano)* | https://startupwiseguys.com | Tallinn (EE), operativo a Cosenza | Acceleratore B2B verticale | OI | Aziende 40M+, enti pubblici | Gestore operativo del CyberXcelerator per CDP con Leonardo, Italgas e NTT Data | C | 1 | https://www.cyberxcelerator.it/ `[V]` |
| Innois S.r.l. | https://innois.it | Cagliari | Gestore programmi territoriali e acceleratori | OI | PMI, enti pubblici | Co-gestore di Frontech; piattaforma di innovazione della Fondazione di Sardegna con programmi ricorrenti | C | 1 | https://innois.it/cosa-e-innois/ `[D]` |
| H-FARM S.p.A. | https://www.h-farm.com | Roncade (TV) | Gestore acceleratori + innovation advisory | OI, VB | Aziende 40M+, enti pubblici | Gestore operativo dell'acceleratore CDP FuturEd con Cisco, IED e Vodafone Italia | C | 1 | https://www.h-farm.com/en/startup `[D]` |
| Alan Advantage S.r.l. | https://alanadvantage.com | Roma, Napoli | «Operational venture» / consulenza innovazione | OI, VB, AI | PMI, corporate, enti pubblici | Consulenza innovazione più acceleratore proprietario (Fucina Cyber Lab) e framework di adozione AI | D | 1 | https://makerfairerome.eu/en/partners/archive/partners-2025/ `[V]` |
| Arsenalia | arsenalia.it — **non fetchabile** (robots/connessione) | Venezia, Milano, Roma | Gruppo AI-driven / system integration | AI, M&A | Aziende 40M+, corporate | Cresce per acquisizioni (10 società fuse), 100 mln di ricavi 2025; Main Sponsor AI Week 2026 | D | 1 | https://askanews.it/2026/05/18/da-one-company-a-one-ai-driven-company-arsenalia-chiude-2025-a-100-mln-euro/ `[V]` |
| altermAInd | https://www.altermaind.com | Milano | Società di AI governance & adoption | AI | Corporate in settori regolati, PA | Governance e industrializzazione dell'AI in settori regolati, non vendita di licenze | D | 1 | https://partner.aiweek.it/ `[V]` |
| JAKALA S.p.A. | https://www.jakala.com | Milano | Performance/AI consulting | AI, M&A | Corporate, aziende 40M+, PA | «AI Factory» e crescita per acquisizioni: presidia l'adozione AI su scala enterprise in 14 verticali | D | 1 | https://www.aiforum.eu/2025/ `[V]` |
| Over Ventures | https://www.overventures.com | Italia | Crowdfunding studio / venture building | VB, M&A (raccolta capitali) | PMI, corporate, startup | Combina venture building, equity crowdfunding e corporate advisory: 200+ deal, oltre 100 mln raccolti | D | 1 | https://digitalinnovationdays.com/sponsor-e-partner `[V]` |
| Growth Capital | https://growthcapital.vc | Milano, Madrid, Londra | Tech investment bank | M&A | Soggetti acquirenti, scaleup, corporate | **Unico operatore M&A puro emerso in tutti gli angoli:** assiste chi acquisisce startup e scaleup | D | 1 | https://growthcapital.vc/ `[D]` |
| G-Factor | **gfactor.it non risolve** — scheda su fondazionegolinelli.it | Bologna | Incubatore/acceleratore societario di Fondazione Golinelli | OI, accelerazione su commissione, investimento | Corporate, PMI innovative, startup | CRIF la indica nella propria area stampa come soggetto che realizza I-Tech Innovation 2025-2026 | E | 1 | https://www.crif.it/area-stampa/11-imprese-selezionate-i-tech-innovation-program-2025-2026/ `[V]` |
| CRIT S.r.l. | https://crit-research.it | Vignola (MO) | Technology broker / centro privato di ricerca a base consortile | OI, scouting tecnologico, R&S | PMI e grandi manifatturiere | Marelli la cita come *managing partner* del Motor Valley Accelerator; soci Ferrari, IMA, Sacmi, Tetra Pak | E | 1 | https://www.marelli.com/en/news/marelli-partners-with-plug-and-play-motor-valley-accelerator.html `[V]` |
| I3P S.c.p.A. | https://www.i3p.it | Torino | Incubatore del Politecnico di Torino con offerta corporate | OI su commissione | Grandi aziende, startup | Iveco Group la cita nel proprio comunicato come co-progettista della piattaforma Beyond Lab (2026) | E | 1 | https://markets.financialcontent.com/workboat/article/gnwcq-2026-3-10-iveco-group-launches-its-beyond-lab-open-innovation-platform-in-collaboration-with-i3p `[V]` |
| BCG X (Boston Consulting Group Italia) *(estero con presidio italiano)* | https://www.bcg.com/x | Milano, Roma | Unità build & AI di big consulting | AI, VB | Grandi aziende, enti pubblici | Apre in Italia Forward Deployed AI Engineer e AI Scientist: porta il modello FDE nel mercato italiano | F | 1 | https://it.indeed.com/cmp/Boston-Consulting-Group/jobs `[S]` |
| Devoteam Italia *(estero con entità italiana)* | devoteam.com/it — **403 alla verifica** | Milano | Consulenza IT e cloud | AI | Grandi aziende, PMI | Cerca AI Forward Deployed Engineer e Sales Executive AI-Powered Process Transformation | F | 1 | https://it.indeed.com/cmp/Devoteam/jobs `[S]` |
| indigo.ai | https://indigo.ai | Milano | Piattaforma AI agents con delivery a progetto | AI | Grandi aziende | Assume FDE e AI Implementation Intern: sta costruendo il layer di servizio sopra il prodotto | F | 1 | https://it.indeed.com/cmp/Indigo.ai/jobs `[S]` |
| Lutech S.p.A. | https://www.lutech.group | Milano | System integrator e consulenza, acquirente seriale | AI, M&A (lato acquisizioni) | Grandi aziende, enti pubblici | Annuncio AI Strategy & Adoption Consultant su maturità digitale: ruolo nuovo per un system integrator | F | 1 | https://it.indeed.com/q-generative-ai-consultant-offerte-lavoro.html `[S]` |
| Fincons Group *(HQ svizzero, forte presenza italiana)* | https://www.finconsgroup.com | Vimercate (MB), Milano | Consulenza IT e system integration | AI | Grandi aziende, enti pubblici | Cerca Technology & AI Innovation Strategist a 60-90k: fascia senior, segnale di nuova linea di offerta | F | 1 | https://it.indeed.com/q-innovation-strategist-offerte-lavoro.html `[S]` |
| Soft Strategy | soft-strategy.com — **non fetchabile** | Roma, Bari | Consulenza direzionale e tecnologica italiana | AI | Grandi aziende | Quattro annunci aperti di cui due AI Engineer: costruisce capacità AI di delivery su commessa | F | 1 | https://it.indeed.com/cmp/Soft-Strategy/jobs `[S]` |
| P4I — Partners4Innovation (gruppo Digital360) | https://www.p4i.it | Milano | Advisory su trasformazione, modello «Roles as a Service» | AI, OI | Aziende medio-grandi, enti pubblici | Ruoli a noleggio e practice AI & Data: modello di vendita alternativo sul segmento del committente | F | 1 | https://www.p4i.it `[D]` |
| Maritime Ventures S.r.l. (operata da B-C Ventures) | https://www.maritime-ventures.com | Genova, Trieste | Venture builder di filiera promosso da CDP | VB | Grandi aziende, enti pubblici | Recluta Entrepreneur in Residence/CEO con equity: venture building di filiera su mandato di corporate industriali | F | 1 | https://www.maritime-ventures.com/ `[D]` |
| Ayming Italia *(estero con entità italiana)* | https://www.ayming.it | Milano | Consulenza su finanza dell'innovazione, società benefit | OI (adiacente) | PMI, grandi aziende | Cerca Expert Innovation Consultant con responsabilità diretta sul cliente: adiacente, non sovrapposta | F (+cit. dubbi B) | 1 | https://www.glassdoor.it/Lavoro/milano-innovation-manager-lavori-SRCH_IL.0,6_IC2802090_KO7,25.htm `[S]` |
| Leyton Italia *(estero con entità italiana)* | https://leyton.com/it | Milano | Consulenza su incentivi e finanza dell'innovazione | OI (adiacente) | PMI, grandi aziende | Innovation Consultant pubblicato di recente in Lombardia; 3.000 imprese italiane servite dichiarate | F (+cit. dubbi B) | 1 | https://it.talent.com/jobs?k=innovation+consultant&l=Italia `[S]` |
| AIWONDER S.r.l. | https://www.aiwonder.it | Brescia | Boutique AI on-premise per imprese | AI | PMI, industria, sanità, enti pubblici | Costituita 04/2025, già con annuncio Senior AI Engineer/Tech Lead RAG: AI sovrana per PMI del Nord | F | 1 | https://www.quibrescia.it/citta/2025/04/16/a-brescia-nasce-ai-wonder-lai-per-le-imprese-senza-dipendere-dallestero/762342/ `[V]` |
| AI Factory S.r.l. — brand «AI Venture Builder» | **aiventurebuilder.com in vendita (GoDaddy)** — nessun sito societario | Italia (operatività Torino/Campania), holding UK | Venture builder AI | VB, AI | PMI, difesa, cybersecurity, industria | 1,3 mln di ricavi 2025 e 10 clienti attivi dichiarati su piattaforma di crowdfunding autorizzata, ma **nessun sito verificabile** | F | 1 | https://www.crowdfundme.it/projects/ai-venture-builder-2/ `[S]`+`[D]` |
| Yellow Tech S.r.l. | https://yellowtech.it | Milano | AI transformation company | AI | PMI, aziende medio-grandi | Costituita 06/2024; formazione all'adozione AI e agenti in produzione; crescita dichiarata +1.105% nel 2025 | F | 1 | https://www.tecnelab.it/news/attualita/yellow-tech-ricavi-in-crescita-del-1-105-nel-2025 `[V]` |
| M-AI S.r.l. | https://www.m-ai.it | Grottaglie (TA), Milano | Startup innovativa di tool AI su misura per PMI | AI | PMI, enti pubblici | Costituita 03/2025, clienti dichiarati fra cui Circet Italia e MEF: verticale back-office PMI | F | 1 | https://www.fatturatoitalia.it/m-ai-srl-03441940735 `[S]` |

---

## 3. Tabella B — operatori esteri (angolo G): riferimenti di modello, non concorrenti

Nessuno di questi opera sul mercato italiano (verifica dell'angolo G fatta per assenza di sedi italiane dichiarate — limite noto). Sono elencati per la formula di ricavo o di ingaggio che rendono replicabile.

| Denominazione | Sito | Paese | Categoria | Linee presidiate | Segmenti | Perché è rilevante | Angoli di provenienza | N. angoli | Fonte URL principale |
|---|---|---|---|---|---|---|---|---|---|
| novazoon | https://www.novazoon.de | Germania (Karlsruhe) | Venture builder industriale + trasformazione | VB, AI | Mittelstand industriale, meccanica, manifattura | Dichiara il mid-market manifatturiero come target primario, non le multinazionali: fascia quasi scoperta | G | 1 | https://www.novazoon.de/en/ `[D]` |
| Bridgemaker | https://www.bridgemaker.com | Germania (Berlino) | Venture builder + AI adoption | VB, AI, adiacenza M&A | Aziende consolidate DACH, imprese familiari, portafogli PE | Vende AI e nuove linee di ricavo come value creation ai fondi di private equity, non solo alle aziende | G | 1 | https://www.bridgemaker.com/en `[D]` |
| Stryber | https://www.stryber.com | Germania / Svizzera (Monaco, Zurigo) | Advisory di crescita + venture studio | VB, OI, settore pubblico | Corporate consolidate, entità sovrane, enti governativi | Linea dedicata di «governmental venture building»; vende l'output come *equity story* | G | 1 | https://www.stryber.com/ `[D]` |
| whataventure | https://www.whataventure.com | Austria (Vienna) | Venture builder con fondo di company creation | VB | Corporate medie e grandi internazionali, investitori strategici | **Fondo di creazione d'impresa a più committenti della stessa filiera**: abbassa il ticket per singola azienda | G | 1 | https://www.whataventure.com/blog/whataventure-fund `[D]` |
| Startup Palace | https://www.startup-palace.com | Francia (Nantes/Parigi) | Operatore di programmi di open innovation | OI | Grandi gruppi ed ETI, consorzi settoriali, territori | Programmi condivisi fra concorrenti («coopétition»), **esplicitamente senza equity**: abbatte il costo unitario | G | 1 | https://www.startup-palace.com/ `[D]` |
| WILCO | https://www.wilco-ambitions.com | Francia (Parigi) | Acceleratore ibrido pubblico-privato | OI, venture support | Startup, ETI e grandi gruppi, territori ed enti pubblici | **Triplo committente** che cofinanzia lo stesso programma; obiettivo contrattualizzato in euro di ricavo | G | 1 | https://www.wilco-ambitions.com/ `[D]` |
| Byld | https://byld.xyz | Spagna (Madrid) | Corporate venture builder | VB, OI, CVC | Grandi corporate (Carrefour, Porsche, Caser) | Offerta modulare in building blocks e posizionamento esplicito «socios, no consultores» | G | 1 | https://byld.xyz/about-us/ `[D]` |
| Innsomnia Group | https://innsomniagroup.com | Spagna (Valencia, Madrid, Miami) | Consulente d'innovazione + hub + media + VC | OI, venture support | Corporate, PMI e startup, **settore pubblico** | **Vive di gare pubbliche pluriennali d'innovazione** (Puertos 4.0, 2,4 mln, 4 anni) e gestisce un hub in concessione | G | 1 | https://valenciaplaza.com/mas-startups-para-valencia-innsomnia-y-kpmg-se-adjudican-la-aceleradora-del-sistema-portuario-espanol `[V]` |
| Duodeka | https://duodeka.com | Paesi Bassi | Venture builder proprietario (SaaS) | VB | Sanità, PA, hospitality, software | Parte dal **problema pubblico** come tesi di venture building: le venture nascono già fornitrici della PA | G | 1 | https://duodeka.com/about/ `[D]` |
| Combient Foundry | https://combientfoundry.com | Svezia (Stoccolma) + Helsinki, Monaco, Palo Alto, Singapore | Alleanza di venture clienting | OI | Grandi industriali nordici e tedeschi | **Alleanza a quota associativa** che condivide scouting e framework: trasforma il ricavo a progetto in ricorrente | G | 1 | https://combientfoundry.com/venture-alliance/ `[D]` |
| Futurice | https://futurice.com | Finlandia (+ DE, SE, UK, PL, PT) | Consulenza di trasformazione multi-brand | AI, OI | Enterprise e mid-market, settore pubblico | **Famiglia di marchi specialistici** (Columbia Road, Fram Partners, Meltlake, Qlarify, Recordly, Thriv) con back office condiviso | G | 1 | https://futurice.com/ `[D]` |
| PUBLIC | https://www.public.io | Regno Unito (Londra) | Specialista GovTech (dal 2025 gruppo Solita) | OI, AI | Esclusivamente settore pubblico: ministeri, enti locali, NHS, regolatori | Monosettoriale sul pubblico, con programma a doppio lato che serve ente e startup insieme | G | 1 | https://www.public.io/blog-post/innovation-programmes `[D]`+`[V]` |

---

## 4. Domini non risolti o divergenti

| Dominio | Operatore | Esito della verifica (11/08/2026) | Conseguenza |
|---|---|---|---|
| `gfactor.it` | G-Factor (Fondazione Golinelli) | **Non risolve**: `Name or service not known`. Conferma il limite già dichiarato dall'angolo E | L'operatore esiste ed è documentato dal comunicato CRIF e dalla scheda su fondazionegolinelli.it, ma **non ha un sito proprio raggiungibile**. Usare la scheda di fondazione come riferimento |
| `aiventurebuilder.com` | AI Factory S.r.l. — brand «AI Venture Builder» | **Redirect 302 a `forsale.godaddy.com`**: dominio in vendita | Nessun sito societario esistente. L'operatore ha numeri commerciali su piattaforma di crowdfunding autorizzata ma **denominazione, sede e sito restano da confermare** prima di trattarlo come competitor |
| `warranthub.it` | Warrant Hub (gruppo Tinexta) | **Redirect 302 a `tinextainnovationhub.com`** — sito attivo di **Tinexta Innovation Hub S.p.A.**, che dichiara di essere «la nuova identità di Innovation Hub» e di integrare Co.Mark, Enhancers, Plannet, Warrant Innovation Lab, Trix, Queryo, Privacy Lab | **Divergenza per rebrand di gruppo, non dominio morto.** Il censimento del Lookout riporta una denominazione superata. Aggiornare la denominazione |
| `djungle.io` | Djungle Studio | Il dominio risolve ma **serve una pagina generata con Lovable**, il cui contenuto non è riconducibile a Djungle Studio. Il sito è quello dichiarato dalla scheda Lookout | **Divergente.** O il dominio è stato riassegnato, o è in ricostruzione. L'attività attuale dell'operatore **non è provata**: declassare finché non si trova un dominio alternativo |
| `atlantegroup.it` | Atlante Group S.r.l. | Non risolve (rilevato dall'angolo A) | Aggiudicazione pubblica verificata (CIG B0FE90D1BC, € 420.000) ma nessun sito: resta nei dubbi, non entra in tabella |
| `spici.it` | SPICI S.r.l. | Non verificabile (robots.txt irraggiungibile, angolo A) | Né sito né aggiudicazione verificati: resta nei dubbi |
| `openadvisory.it` | Open Advisory (partecipata ELIS) | Certificato SSL non valido (angolo E) | È la società che coordina operativamente i programmi di filiera ELIS: verifica prioritaria da rifare |

### Domini non verificabili per blocco tecnico (l'operatore non è in discussione, la verifica sì)

`k-digitale.com` (ConnectTimeout su robots.txt) · `e12.it` — Enzima12 (errore di verifica certificato SSL) · `arsenalia.it` (già segnalato dall'angolo D) · `soft-strategy.com` · `ciaotech.com` · `pnoconsultants.com/it` · `devoteam.com/it` (403) · `thedoers.co` (ConnectError).
Inoltre: **StrategyInnovation** non espone alcun dominio sulla propria scheda del Lookout (né sede, né anno di fondazione, né contatti leggibili) — è la riga con l'evidenza più debole dell'intera Tabella A. **TeamDev** ha sito verificato ma sede `[N]`.

---

## 5. Collegamenti societari rilevati

**Appartenenze di gruppo**

| Operatore | Gruppo / controllante | Fonte |
|---|---|---|
| I.S.E.D. S.p.A. | Gruppo **expert.ai** (quotato) | Angolo A |
| Warrant Hub | Gruppo **Tinexta** → confluita in **Tinexta Innovation Hub S.p.A.** insieme a Co.Mark, Enhancers, Plannet, Warrant Innovation Lab, Trix, Queryo, Privacy Lab | Verifica 11/08/2026 |
| a\|cube SB S.r.l. | Gruppo **Avanzi** (condivide l'advisory del fondo a\|impact) | Angolo C + verifica 11/08/2026 |
| P4I — Partners4Innovation | Gruppo **Digital360** | Angoli F + verifica 11/08/2026 |
| CiaoTech S.r.l. / PNO Innovation Italy | **PNO Group** — sono la stessa struttura sotto due denominazioni: unificate in una riga | Angoli B, F |
| OrgTech S.r.l. | **Humagine** è un brand di OrgTech S.r.l. (orgtech.it reindirizza 302 a humagine.it) | Angolo B + verifica 11/08/2026 |
| Twenty Ventures / 20V | **Twenty Investments Holding S.r.l.** — le due schede del Lookout (`/player/20v/` e `/player/twenty-ventures/`) sono lo stesso soggetto | Angolo B + verifica 11/08/2026 |
| ZNEXT S.r.l. | Gruppo **Zanichelli Editore** | Angolo B |
| BCG X | **Boston Consulting Group** | Angolo F |
| Maritime Ventures S.r.l. | Operata da **B-C Ventures**, promossa da CDP Venture Capital con Fincantieri e PSA Italy | Angolo F |
| AI Factory S.r.l. | Holding nel **Regno Unito**; opera con il brand «AI Venture Builder» | Angolo F |
| Fincons Group | Capogruppo **svizzera** (Fincons Group AG) con operatività italiana a Vimercate | Verifica 11/08/2026 |
| Futurice | Casa madre di **Columbia Road, Fram Partners, Meltlake, Qlarify, Recordly, Thriv** | Angolo G |
| PUBLIC | Dal 2025 parte del gruppo **Solita** (Finlandia) | Angolo G |
| Alien Technology Transfer, CubeLabs, Enry's Island | Strutture quotate o con veicoli finanziari propri (Euronext Growth Milan per CubeLabs, Vienna Stock Exchange per Enry's Island) | Angolo B + verifiche 11/08/2026 |

**Soci in comune e legami accademico-fondazionali**

- **Almacube ↔ G-Factor:** entrambe hanno **Fondazione Golinelli** fra i soci/fondatori (Almacube: UniBo + Confindustria Emilia + Fondazione Golinelli; G-Factor è l'acceleratore societario della Fondazione). Due righe distinte della Tabella A che condividono lo stesso azionista bolognese.
- **Cefriel ↔ I3P:** entrambe emanazioni di politecnici (Milano e Torino) con offerta commerciale piena. Stessa classe di soggetto, non stesso gruppo.
- **Bianco Ventures:** costituita a novembre 2025 da **GELLIFY + Deloitte + Arad** — vedi §6, esclusa.
- **Innsomnia ↔ KPMG:** l'aggiudicazione spagnola Puertos 4.0 è stata vinta **in UTE con KPMG**, che è nella lista degli esclusi. Rilevante se si legge Innsomnia come modello: la formula «gara pubblica pluriennale» in Spagna passa da un'alleanza con una Big4.

**Legami operativi ricorrenti (co-gestione di programmi)**

- **GELLIFY ↔ Innois ↔ Cariplo Factory** — co-gestori dell'acceleratore **Frontech** (Cagliari). Cariplo Factory è esclusa perché già nota: significa che GELLIFY e Innois lavorano stabilmente accanto a un operatore già mappato.
- **Wylab ↔ a\|cube ↔ PortXL** — co-gestori di **FAROS** (blue economy).
- **a\|cube ↔ SocialFare** — co-gestori di **Personae** (welfare), con Accenture fra i partner.
- **ELIS ↔ Zest** — co-gestori dell'acceleratore **Zero** (cleantech). ELIS lavora fianco a fianco con un operatore già noto.
- **Plug and Play ↔ CRIT** — rispettivamente gestore e *managing partner* del **Motor Valley Accelerator**, secondo il comunicato Marelli.
- **Opinno:** l'angolo D riporta l'acquisizione di **Tree**, l'angolo E riporta che **Opinno Italia è stata acquisita da eFM**. Le due informazioni non sono state riconciliate: l'assetto societario italiano di Opinno è **da chiarire** prima di profilarla come concorrente.

---

## 6. Esclusi perché già noti o riconducibili a operatori già noti

| Escluso | Dove compariva | Motivazione della decisione |
|---|---|---|
| **The Doers S.r.l.** (Torino) | B, tabella principale; citata anche nei dubbi di D e F | **Escluso.** Acquisita da **Digital Magics** nel 2021; Digital Magics è confluita in **Zest** (fusione con LVenture Group, aprile 2024). Zest è nella lista degli esclusi, quindi The Doers ricade nel perimetro di un operatore già mappato. Ho tentato la verifica diretta: `thedoers.co` **non è fetchabile** (ConnectError), quindi non ho potuto accertare se conservi autonomia commerciale e brand distinto. La scelta prudente è escluderla dal conteggio dei concorrenti nuovi e **segnalare la verifica come da rifare**: se risultasse operativa con offerta e forza vendita proprie, andrebbe reintegrata come «brand autonomo dentro Zest» |
| **LVenture Group** e **Digital Magics** | C, esclusi in corso d'opera | **Esclusi.** Fusi in **Zest** dal 1° aprile 2024. Nota operativa: erano i gestori di Argo, Zero, Fin+Tech, HabiSmart e Magic Spectrum — cioè **cinque acceleratori della rete CDP finiscono dentro un operatore già noto**. È un dato di concentrazione competitiva da tenere presente |
| **Intellera Consulting S.p.A.** | D, tabella principale; F, dubbi | **Escluso, con nota.** Parte del **gruppo Accenture**, già mappato. Ma va detto che opera con **brand, sito e forza vendita autonomi** (oltre 800 professionisti, presidio su PA e sanità) e nel 2025-26 assume in proprio: in una gara sul segmento enti pubblici la si incontra come «Intellera», non come «Accenture». **Da monitorare come brand, non da conteggiare come operatore nuovo** |
| **Ammagamma** (Modena) | E, dubbi | **Escluso.** Acquisita da **Accenture**. L'angolo E aveva trovato una citazione cliente eccellente (Gruppo Hera pubblica sul proprio sito il progetto di AI con Ammagamma e Tecnoform), ma la proprietà la riconduce a un operatore già noto |
| **Bianco Ventures** | B, tabella principale | **Escluso, con nota.** Venture builder deep tech per lusso/moda/retail costituito a novembre 2025 da **GELLIFY + Deloitte + Arad**. Due dei tre soci sono già in lista (GELLIFY in Tabella A, Deloitte/Officine Innovazione fra gli esclusi): conteggiarla come operatore autonomo sarebbe **doppio conteggio**. Inoltre la fonte stessa la dà «in costituzione» e non esiste un sito verificabile. **Va letta come segnale di mercato** — il venture building verticale sul lusso è un segmento che si sta formando — non come riga di concorrente |
| **Officine Innovazione S.r.l. Società Benefit** (Deloitte) | A, nota di igiene | **Escluso.** Già mappato. Dato informativo che vale la pena tenere: compare **ripetutamente** fra i partecipanti alle procedure negoziate di Regione Lombardia 2024, cioè nella committenza regionale l'assistenza tecnica va prevalentemente a operatori già noti al committente |
| **Cariplo Factory** | C (co-gestore Frontech e Terra Next) | **Escluso.** Già mappata |
| **Zest** | C (co-gestore dell'acceleratore Zero con ELIS) | **Esclusa.** Già mappata |
| **Accenture** | C (partner di programmi CDP), E, F | **Escluso.** Già mappato. Compare come partner dell'acceleratore Personae |
| **Deloitte, EY, PwC, KPMG, Capgemini, Reply, Engineering, Zucchetti, TeamSystem, Vento, Seedble** | scartati in fase di spoglio da C, D, E, F | **Esclusi.** Già mappati. Gli angoli li hanno incontrati più volte e omessi come da istruzioni |
| **Avanade** | F, dubbi | **Escluso.** Joint venture **Accenture-Microsoft**: entità giuridica distinta ma riconducibile a un operatore già mappato. Stessa logica di Intellera |
| **Startupbootcamp / Rainmaking** | G, dubbi | **Escluso dalla Tabella B** per una ragione diversa: Startupbootcamp ha avuto programmi in Italia, quindi la premessa «non compete sul mercato italiano» non regge, e il perimetro del gruppo è in movimento |
| **Exor Ventures** | D, limiti | **Escluso.** Fondo, e co-organizzatore di Italian Tech Week con Vento, già escluso |

**Verifica di controllo.** Nessun altro nome della lista di esclusione (Ventive, Startup Geeks, Datapizza, Webidoo, Perspective AI, Mach49, Alloy Partners, Creative Dock, FoundersLane, 27pilots, Bundl, Hexa, Distyl AI) compare nelle tabelle principali dei sette file. **Founders Factory** compare due volte (dubbi di B come operatore estero, dubbi di C come partner di venture building di Fastweb/Vodafone NeXXt Ventures) e **non è nella lista di esclusione**: resta un candidato estero non istruito, non un escluso.

---

## 7. Dubbi consolidati

Unione deduplicata delle sezioni dubbi dei sette file. Raggruppati per tipo di dubbio, perché gli stessi problemi tornano su angoli diversi.

### 7.1 Confine «incubatore/consorzio universitario o non profit» contro «società di servizi»

È il dubbio più ricorrente: torna in B, C, D, E e F.

- **Consorzio ELIS / ELIS Innovation Hub.** Consorzio non profit di matrice formativa, non società di capitali. Modello economico a quote consortili di ~140 aziende. Il coordinamento operativo dei programmi di filiera è affidato a **Open Advisory**, società partecipata da ELIS, il cui sito non è verificabile (certificato SSL). Da decidere se trattarlo come competitor diretto o come ecosistema in cui inserirsi. *(fonti: C-1, E-3, F-7)*
- **Almacube.** S.r.l. con soci Università di Bologna, Confindustria Emilia e Fondazione Golinelli. Inclusa perché ha committenti corporate paganti verificabili (Barilla, Philip Morris) e vende format a catalogo, ma è a metà fra incubatore universitario e società di servizi. *(C-6, E-2)*
- **I3P.** S.c.p.A. del Politecnico di Torino con offerta commerciale corporate dichiarata (analisi dei bisogni, progettazione programmi, scouting, esecuzione) e citazione cliente forte da Iveco Group. Il criterio di esclusione «incubatori universitari» va deciso a monte. *(E-2)*
- **Cefriel.** Società consortile a r.l. partecipata dal Politecnico di Milano, Società Benefit: non è un incubatore e ha offerta commerciale piena, ma il legame accademico conta nel posizionamento. *(D, E)*
- **SocialFare.** Impresa sociale S.r.l. e incubatore certificato: struttura e offerta commerciale ci sono entrambe. Dubbio più leggero degli altri. *(F-7)*
- **G-Factor.** Acceleratore societario di Fondazione Golinelli, senza sito proprio raggiungibile. *(E, §4)*
- **VeniSIA** (Ca' Foscari), **PoliHub**, **I3P**, **TechNest UniCal**: esclusi come incubatori universitari senza offerta commerciale autonoma, ma I3P è poi rientrato per l'angolo E. Incoerenza da sanare a monte. *(C-4, C-18)*
- **AI4I — Istituto Italiano di Intelligenza Artificiale** (Torino, dal 2026, 92 aziende partner, marketplace SUK): istituto di ricerca con infrastruttura pubblica, non società di servizi. Non incluso ma **da monitorare**: presidia lo stesso spazio di AI adoption verso PMI ed è nuovo. *(F-9)*

### 7.2 Confine «software/piattaforma» contro «servizio»

- **Wazoku** e **NineSigma**: piattaforme/broker di crowdsourcing dell'innovazione. Wazoku vende sia licenza sia challenge management as-a-service; il mix non è stato verificato. *(B-6)*
- **indigo.ai**: piattaforma di AI agents, inclusa perché assume esplicitamente ruoli di delivery presso cliente (FDE, due AI Implementation Intern, coordinatore di continuous improvement), cioè sta costruendo la componente di servizio. *(F-5)*
- **TeamDev**: sito verificato ma profilo prevalentemente software (GIS, smart city, IoT) rispetto al censimento come consulenza OI. *(consolidamento)*
- **Nortal** (Estonia): escluso dall'angolo G perché più system integrator che operatore d'innovazione. *(G)*

### 7.3 Operatori il cui posizionamento dichiarato non coincide più con quello verificato

- **OrgTech / Humagine**: censita come consulenza open innovation, ma il sito verificato oggi vende **trasformazione organizzativa, people development e coaching**. Rischio che ricada nell'esclusione «sola consulenza HR». *(B-5, verifica 11/08/2026)*
- **Alien Technology Transfer**: censita come venture builder, ma il sito verificato (giugno 2026) vende **grant funding non diluitivo** e compliance regolatoria. *(verifica 11/08/2026)*
- **TechBricks**: censita come venture studio che «accelera l'open innovation per imprese e startup», ma il sito oggi parla di founder mission-driven e rigenerazione planetaria. *(verifica 11/08/2026)*
- **Rainmakers**: sito con ultima modifica 2021. **Attività recente non provata.** *(verifica 11/08/2026)*
- **Djungle Studio**: il dominio dichiarato non serve più contenuto riconducibile all'operatore. *(§4)*
- **StrategyInnovation**, **BTO Research**, **Innovation Match**, **Mind The Bridge**: schede del Lookout prive di dati. Innovation Match e Mind the Bridge sono poi state confermate dall'angolo D con presenze a evento datate; StrategyInnovation e BTO Research **no**. *(B-9)*

### 7.4 Operatori esteri con presenza italiana: concorrenti o no?

- **Plug and Play, Startup Wise Guys, Eatable Adventures, Opinno**: non sono società italiane ma gestiscono programmi in Italia con team locali e concorrono sulle gare corporate. Inclusi da C e D. Concorrenti reali sulle grandi aziende, **meno sulle PMI**. *(C-8, D, E-5)*
- **MassChallenge, SOSV, Accelerace, PortXL, Startupbootcamp, Techstars**: co-gestori con ruolo prevalentemente metodologico e senza presidio italiano dimostrabile. Non inclusi. *(C-8)*
- **Founders Factory** (UK): partner di venture building di Fastweb+Vodafone NeXXt Ventures; nessuna struttura operativa italiana verificata. Non incluso. *(C-10, B-10)*

### 7.5 Cambi di gestore, acquisizioni e assetti da chiarire

- **VITA Accelerator**: le fonti 2023-24 indicano **Healthware Group** come gestore; il sito del programma oggi indica **EVERSANA** e **Accelerace** (Healthware assorbita in EVERSANA). Da verificare se esista ancora un'entità italiana con offerta propria. *(C-2, E-6)*
- **Opinno**: acquisizione di **Tree** (D) e acquisizione di **Opinno Italia da parte di eFM** (E). Le due informazioni non sono riconciliate: l'assetto italiano è da chiarire. *(D, E-6)*
- **Maritime Ventures**: programma triennale (mag. 2024 – mag. 2027) promosso da CDP con Fincantieri e PSA Italy, operato da **B-C Ventures**. Non è chiaro se abbia autonomia commerciale verso clienti terzi. B-C Ventures come operatore autonomo non è verificabile: le ricerche restituiscono omonimi. *(F-8)*
- **AI Factory / «AI Venture Builder»**: denominazione, sede e sito da confermare; l'anno di costituzione non è determinato con fonti aperte. *(F-1, §4)*
- **KeyPartners**: sito non risolvibile con quella denominazione; escluso per mancato rispetto del vincolo «sito attivo». *(F-4)*

### 7.6 Operatori a perimetro adiacente, non sovrapposto

- **Ayming Italia** e **Leyton Italia**: presidiano finanza dell'innovazione e incentivi R&S più che l'open innovation. Assumono con il titolo «Innovation Consultant» e servono PMI e grandi aziende: adiacenti. L'angolo B li aveva **esclusi**, l'angolo F li ha **inclusi**. Divergenza da sanare: qui li ho tenuti, marcati «OI (adiacente)». *(B-7, F-6)*
- **Growth Engine** (Milano): citata da Economyup fra gli operatori del venture building, ma dalla verifica del sito risulta una **holding di investimento VC pre-seed/pre-Series A**, non un fornitore di servizi. Esclusa per il criterio «fornitori di solo capitale». *(B-4)*
- **Talent Garden** (coworking + formazione), **The Innovation Group** (ricerca/eventi + advisory AI), **0-10x Innovation Business Labs** (offerta quasi interamente formativa, PMI Innovation Business Summit), **DGS S.p.A.** (system integrator, Premium Sponsor AI Week 2026): tutti al confine, tutti esclusi dalle tabelle principali, tutti «da decidere». *(D)*
- **Impact Hub Milano**: gestisce programmi ma la pagina attuale elenca solo percorsi a catalogo propri, senza committente corporate. Manca l'evidenza di gestione **per conto di terzi** negli ultimi 18 mesi. *(C-3)*
- **Fintech District**: parte del gruppo Sella/Fabrick, più piattaforma di community che gestore su commissione. *(C-5)*
- **DOS Design, Svicom, Product Heroes, Sketchin**: emersi dal Lookout senza qualificazione sufficiente delle linee. *(D)*

### 7.7 Venture builder corporate internalizzati

- **ZNEXT** (Zanichelli) è stato **incluso**, **PLAI** (Mondadori) **escluso**: entrambi sono venture builder corporate internalizzati, non fornitori su commissione. Formalmente presidiano la linea VB ma non competono per le stesse commesse. La verifica di questa fase mostra però che ZNEXT dichiara anche **M&A e un programma per fondatori esterni**, il che ne giustifica la permanenza. Scelta da confermare. *(B-3)*
- **Fastweb** compare nella categoria Venture Builder del Lookout ma è un corporate: escluso come non-fornitore. **Snam HyAccelerator** è gestito direttamente dall'azienda: nessun gestore terzo. *(B-8, C-9)*

### 7.8 Dubbi su evidenza e datazione

- **Grownnectia**: offerta coerente e S.r.l. con P.IVA verificabile, ma **nessun committente corporate nominato** né case study datati sul sito. Evidenza di attività debole, marcatura `[D]`. *(C-7)*
- **Nana Bianca — data SIOS**: la pagina speaker di StartupItalia Open Summit non è datata; verosimilmente edizione sarda 2025 e non il decennale di Milano. *(D)*
- **Growth Capital**: presenza a evento documentata solo come co-autore del report VC con Italian Tech Alliance, non come sponsor o speaker in programma pubblicato. Unico M&A puro trovato: da riverificare. *(D)*
- **FoolFarm**: l'unica presenza a evento reperita è del 10/03/2023, **fuori finestra**. *(D)*
- **Citazioni cliente datate**: le referenze di Plug and Play (Marelli 2021, Esselunga 2019, A2A 2020-2023) e di Poste su ELIS (2019) sono precedenti ai 18 mesi. In gara pesano meno. *(E-4)*
- **Cefriel**: nessuna citazione trovata **dal lato cliente**; tutti i casi Enel, Sorgenia, Crédit Agricole, SEA sono pubblicati sul sito Cefriel o ripresi dalla stampa. Marcato `[D]`. *(E-6)*
- **Dintec** e **t2i**: risultano **partecipanti** (non aggiudicatari) a più procedure negoziate di Regione Lombardia 2024 con CIG verificati. Essendo in house camerali operano prevalentemente per affidamento diretto. Siti attivi verificati. Restano candidati non promossi. *(A-3)*
- **Atlante Group** e **SPICI**: vedi §4. *(A-3)*
- **Date degli annunci di lavoro**: nessuno dei portali usati espone in modo affidabile la data di prima pubblicazione. Il criterio «ultimi 12 mesi» è soddisfatto per costruzione (annunci attivi al 11/08/2026) ma non è ricostruibile da quanto tempo ciascun operatore cerca quel profilo. *(F-11)*

### 7.9 Dubbi dell'angolo estero (G) — candidati esclusi dalla Tabella B

Riportati per completezza: sono modelli scartati, non concorrenti.

**Innoleaps** (NL, clientela Fortune 500, criterio 18 mesi non verificato) · **Iterate** (NO, il flusso di cassa della consulenza finanzia società proprie; modello di ricavo non dichiarato) · **Nortal** (EE/FI, profilo da system integrator) · **Impulse Partners** (FR, modello a club settoriali fra i più replicabili, ma attività più recenti trovate ferme al 2024) · **Rainmaking/Startupbootcamp** (DK, ha operato in Italia) · **Barrabés.biz** (ES, sito non più operativo) · **Aimforthemoon** (NL, «the journey has come to an end») · **Bakken & Bæck** (studio di design) · **mantro** (DE, pagina non leggibile automaticamente) · **Excubate** (DE, candidato promettente su venture clienting mid-market, sito blocca l'accesso automatico) · **Reaktor** (FI, nessun elemento distintivo di modello) · **Solita** (FI, controllante di PUBLIC, sito non verificato).

---

## 8. Copertura e limiti

Cosa questa lista **è**: la sintesi di sette ricerche a fonti aperte, tutte condotte in una sola sessione l'11/08/2026, tutte finite contro un tetto di 200 query di ricerca web e contro blocchi tecnici significativi. Cosa **non è**: una mappa esaustiva del mercato.

**1. Il budget di ricerca si è esaurito in tutti e sette gli angoli.** Ognuno dei sette file dichiara di aver consumato le 200 chiamate disponibili prima di completare il proprio piano. Da quel punto ciascun agente ha lavorato solo con fetch diretto di URL già noti o ricostruiti a mano. Questo ha un effetto sistematico e prevedibile: **la lista è sbilanciata verso ciò che è indicizzato e verso ciò di cui si conosceva già il nome.**

**2. La fonte più importante è pubblicamente incompleta rispetto a se stessa.** L'Open Innovation Lookout del Politecnico di Milano dichiara nel rapporto 2026 **503 organizzazioni censite** su 24 categorie, con le società di consulenza open innovation passate da 58 a **103** e gli startup studio/venture builder da 37 a **75**. Il directory pubblico del sito espone ancora i numeri della rilevazione precedente: **circa 84 operatori censiti dall'Osservatorio non sono raggiungibili dal sito pubblico**. Il rapporto integrale richiede registrazione. L'angolo B stima di aver coperto **il 30% circa** del censimento, e le categorie **«acceleratore» e «incubatore» non sono state scorte**: è la lacuna singola più significativa, perché possono contenere operatori privati con offerta commerciale di venture building. Anche le categorie `broker` e `collector`, direttamente pertinenti, restituiscono 404.

**3. Le banche dati appalti sono tutte inaccessibili.** TED bloccato da robots.txt, ANAC-BDNCP respinta da WAF, Piattaforma di Pubblicità a Valore Legale ANAC illeggibile perché SPA JavaScript. Sono le tre fonti che avrebbero risposto direttamente all'angolo A. Conseguenza: **nessun CIG sulle sei aggiudicazioni principali** e nessuna ricerca «per oggetto di gara» su scala nazionale. L'angolo A restituisce 4 operatori invece dei 10-20 attesi. Non coperti: Sardegna Ricerche, ART-ER, Lazio Innova (esiti non pubblicati), Sviluppumbria, Finpiemonte, Puglia Sviluppo, InnovaPuglia, Trentino Sviluppo, Veneto Innovazione, Sviluppo Toscana, ARIA Lombardia.

**4. LinkedIn non è consultabile.** È il limite più pesante dell'angolo F: LinkedIn è di gran lunga il canale principale in Italia per i ruoli di venture architect, venture builder, innovation manager e AI transformation consultant, e diversi operatori (SocialFare in primis) pubblicano solo lì. **InfoJobs è chiuso.** Il registro imprese non è interrogabile in modo parametrico da fonti aperte: `startup.registroimprese.it` espone i filtri solo dietro form interattivo. È il motivo per cui la ricerca sui nuovi entranti restituisce **quattro nomi e non venti**: senza conoscere già denominazione o P.IVA non si arriva ai riepiloghi camerali.

**5. Gli elenchi soci delle associazioni hanno reso quasi zero.** InnovUp: directory di ~492 soci su 25 pagine, filtri per categoria non utilizzabili via URL, 53 «Enabler» pertinenti non estratti. Italian Tech Alliance: elenchi nominativi **non pubblicati** («lista in fase di aggiornamento»). Assintel, Assinter, Confindustria Digitale: non verificate. Registro MIMIT degli incubatori certificati ed elenco PMI innovative: non consultati. Sono i recuperi a resa più alta per un secondo giro.

**6. Le liste sponsor degli eventi più ricchi non sono state spogliate.** We Make Future (errore 400), AI Festival (errore 400), Rome Future Week (robots.txt) — quest'ultima dichiara oltre 2.500 imprese coinvolte. Sono, per ammissione dell'angolo D, le tre lacune maggiori di quel canale.

**7. Il canale «citazione da parte del cliente» è strutturalmente povero.** Sui due bilanci di sostenibilità 2024 controllati integralmente (Saipem, OTB) **non compare alcun fornitore di innovazione citato per nome**. Le pagine «innovazione» delle grandi corporate italiane raramente nominano il gestore: le ricerche mirate su Enel, Eni, Poste, TIM, Leonardo, Ferrovie, A2A, Lavazza, Chiesi, Angelini, Bracco, Campari, Autogrill non hanno restituito il soggetto gestore. **Una quota rilevante di concorrenti resta invisibile** senza accesso a visure, albi fornitori e LinkedIn dei program manager.

**8. Copertura per linea di business fortemente squilibrata.** Le citazioni cliente verificate riguardano quasi solo **open innovation**. Per **venture building su commissione**, **AI adoption** e **M&A** non è stata trovata alcuna citazione cliente-side verificabile: tutti i nomi di venture building della Tabella A poggiano su `[S]` (censimento Lookout) o `[D]`. Sulla linea **M&A** è emerso **un solo operatore puro** (Growth Capital) e nessuno dei dodici esteri la presidia in senso stretto.

**9. Affidabilità del dato dimensionale.** Fatturato, dipendenti e sede delle righe provenienti dal Lookout sono **autodichiarati all'osservatorio e riferiti all'esercizio 2022**: hanno quattro anni e non provano attività corrente. Non sono stati incrociati con bilanci o visure. Vanno letti come ordini di grandezza.

**10. Verifica dell'attività negli ultimi 18 mesi: parziale.** Su 81 righe della Tabella A, l'attività recente è provata con data esplicita solo per una minoranza. In questa fase la verifica dei domini ha aggiunto un dato di esistenza (il sito risponde) ma **non un dato di attività** (il sito è aggiornato), tranne dove il fetch ha restituito una data: Magnisi (maggio 2026), Innois (maggio 2026), Alien TT (giugno 2026), Ayming (luglio 2026), Day One (marzo 2024), Rainmakers (2021).

**11. Cosa implica per la completezza della lista.** Tre conseguenze pratiche.
   - *La lista sottostima i piccoli e i non-milanesi.* Il canale appalti restituisce integratori PA, il canale eventi restituisce chi paga sponsorizzazioni, il canale annunci restituisce chi pubblica su portali nazionali (quasi tutto Milano e Roma). Chi lavora su commessa diretta in un territorio, senza gare né sponsorship né assunzioni pubblicate, **non compare qui**.
   - *La lista sovrastima la solidità delle righe a un solo angolo provenienti dal Lookout.* Trentaquattro delle 81 righe vengono dal solo censimento PoliMi, con dati 2022 e senza alcuna prova indipendente di attività. Il segnale «3+ angoli» esiste proprio per questo.
   - *Il mercato pubblico italiano non è strutturato come «gare di open innovation».* Con l'eccezione della gara FS vinta da GELLIFY, gli appalti che intercettano questo perimetro sono classificati come servizi ICT e vanno a system integrator o, per l'assistenza tecnica, a consulenti già noti e a in house camerali. Chi fa open innovation e venture building «puro» in Italia sembra vendere **fuori dal canale appalti**. È un'ipotesi supportata dai dati raccolti, non una certezza: la verifica richiede l'accesso alla BDNCP ANAC.

---

## 9. Totali

| Voce | Valore |
|---|---|
| **Totale operatori unici italiani (Tabella A)** | **81** |
| di cui italiani in senso stretto | 69 |
| di cui esteri con presidio o entità italiana (concorrono in Italia) | 12 — Plug and Play, Opinno, Eatable Adventures, Startup Wise Guys, Wazoku, NineSigma, Mind the Bridge, BCG X, Devoteam Italia, Ayming Italia, Leyton Italia, Fincons Group |
| **Totale operatori esteri (Tabella B, riferimenti di modello)** | **12** |
| **Emersi da 3 o più angoli** | **6** — GELLIFY (5), Nana Bianca (3), Plug and Play Italy (3), ELIS Innovation Hub (3), SocialFare (3), Opinno (3) |
| Emersi da 2 angoli | 10 |
| Emersi da 1 angolo | 65 |
| Esclusi perché già noti o riconducibili a operatori già noti | 13 voci nominate in §6 (di cui 3 erano in tabella principale di un angolo: The Doers, Intellera Consulting, Bianco Ventures) |
| Domini non risolti, morti o divergenti | 7 (§4) |
| Domini non verificabili per blocco tecnico | 10 |
| Righe grezze in ingresso → operatori unici in uscita | 120 → 93 (81 + 12) |

---

## 10. Correzioni emerse durante la FASE 3 — screening

Aggiunte l'11/08/2026 dopo lo screening. **Da recepire nelle tabelle sopra alla prossima revisione.**

1. **B-C Ventures = Bridgemaker (DE) + Cariplo Factory.** La scheda caso di Bridgemaker dichiara **Maritime Ventures** come cliente italiano, 2024-2027: venture studio fondato e operato tramite la joint venture con Cariplo Factory, con CDP Venture Capital, Fincantieri e PSA Italy fra i promotori e tre venture già scorporate. **Scioglie il dubbio F-8.** Bridgemaker non è un riferimento di modello: è un operatore attivo sui nostri segmenti, con un socio italiano già mappato. **Va spostato dalla Tabella B alla Tabella A.**
2. **Strategy Innovation ha un dominio.** Risultava senza sito dichiarato: è lo spin-off di Ca' Foscari, Venezia. Da correggere in Tabella A.
3. **Warrant Hub è oggi Tinexta Innovation Hub.** Il redirect 302 rilevato in §4 non era un dominio divergente ma un **rebrand di gruppo**, con sette società integrate in dodici mesi. La denominazione del censimento è superata. Da correggere in Tabella A e da togliere dai domini divergenti.
4. **BTO Research è nel gruppo Relatech dal 2022.** Collegamento societario non rilevato in §5. Da aggiungere.

Il dettaglio degli otto campi per tutti i 93 operatori è in `screening-lotto1.md` … `screening-lotto5-estero.md`; l'indice ordinato per punteggio è in `screening.md`.
