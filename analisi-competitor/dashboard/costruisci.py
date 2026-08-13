#!/usr/bin/env python3
"""Inietta dati.json dentro modello.html e produce il file unico da distribuire.

Il risultato è autoconsistente: nessuna dipendenza, nessuna chiamata di rete
(tranne i font di Google, che degradano su stack di sistema se manca la
connessione). Si apre con un doppio clic.

Uso:  python3 dashboard/estrai.py && python3 dashboard/costruisci.py
"""

import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELLO = os.path.join(BASE, "dashboard", "modello.html")
DATI = os.path.join(BASE, "dashboard", "dati.json")
USCITA = os.path.join(BASE, "analisi-competitor-v2.html")


def main():
    with open(MODELLO, encoding="utf-8") as fh:
        modello = fh.read()
    with open(DATI, encoding="utf-8") as fh:
        dati = json.load(fh)

    # I contenuti sono HTML: se contenessero </script> chiuderebbero il blocco
    # in cui li stiamo incorporando. Si neutralizzano i delimitatori senza
    # toccare il testo, che resta identico una volta riletto da JSON.parse.
    testo = json.dumps(dati, ensure_ascii=False)
    testo = (testo.replace("<", "\\u003c")
                  .replace(">", "\\u003e")
                  .replace("&", "\\u0026")
                  .replace(" ", "\\u2028")
                  .replace(" ", "\\u2029"))

    if "/*DATI*/" not in modello:
        raise SystemExit("ERRORE: segnaposto /*DATI*/ non trovato in modello.html")

    fuori = modello.replace("/*DATI*/", testo)

    with open(USCITA, "w", encoding="utf-8") as fh:
        fh.write(fuori)

    kb = os.path.getsize(USCITA) / 1024
    print(f"scritto {os.path.relpath(USCITA, BASE)} — {kb:.0f} KB")
    print(f"  operatori: {len(dati['operatori'])}")
    print(f"  schede: {len(dati['schede'])}")
    print(f"  documenti: {len(dati['documenti'])}")


if __name__ == "__main__":
    main()
