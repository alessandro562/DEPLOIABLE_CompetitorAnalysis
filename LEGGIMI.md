# DEPLOIABLE — analisi competitiva

Due cartelle, due cose diverse.

| Cartella | Che cos'è | Da dove si parte |
|---|---|---|
| **`strumento/`** | **Lo strumento di decisione.** Un registro vivo con sopra un'interrogazione e sotto un generatore di brief | apri `strumento/campo.html` |
| `analisi-competitor/` | **L'archivio di ricerca** della tornata V2 dell'11/08/2026: schede, screening, prezzi, firme verbali, incertezze. È la fonte da cui il registro è stato costruito | leggi `analisi-competitor/ANALISI-COMPETITOR-V2.md` |

Sono separati apposta. L'archivio di ricerca, lo strumento di interrogazione e il
materiale di vendita hanno utenti, cadenze e forme diverse: impilarli peggiora
tutti e tre.

---

## Se hai due minuti

Apri **`strumento/campo.html`** con un doppio clic. Quattro schermate, ognuna
risponde a una domanda e finisce con una riga che dice cosa fare.

- **Oggi** — cosa è cambiato, cosa chiede una verifica, cosa non sappiamo e
  quanto costa non saperlo. È la coda di lavoro, non un riassunto.
- **Il campo** — l'interrogazione, con cinque tagli e un solo insieme di filtri.
  Il rosso segnala una cosa sola: dove non sappiamo.
- **Chi** — la scheda di un operatore, con indirizzo proprio e modificabile in
  linea.
- **Brief** — il documento datato da portare in riunione. Si genera dal
  registro; se è sbagliato, si corregge il registro.

Istruzioni complete, contratto dati e limiti dichiarati: **`strumento/LEGGIMI.md`**.

## Se devi aggiornare

Il dato sta in `strumento/dati.json`. Chi corregge un giudizio lo fa
dall'interfaccia ed esporta una patch JSON; chi tiene il registro la applica e
rigenera:

```bash
cd strumento
python3 verifica-dati.py     # il contratto dati regge?
python3 contrasto.py --css   # ogni coppia testo-fondo sopra 4,5:1?
python3 costruisci.py        # rigenera campo.html
```

Serve solo Python 3. Nessuna dipendenza.

## Che cosa questo materiale non è

**Non è un censimento.** È il campo visibile da fonti aperte in una sessione di
ricerca, con il budget di ricerca web esaurito prima che lo screening
cominciasse. Nessuno dei 93 operatori screenati ha un fatturato verificato, la
categoria dei sostituti non è stata lavorata, e diciassette righe del registro
non hanno mai avuto una lettura diretta riuscita. Lo strumento lo dichiara in
apertura, riga per riga, invece di nasconderlo.

**Uso interno.** Contiene giudizi competitivi espliciti su operatori nominati.
