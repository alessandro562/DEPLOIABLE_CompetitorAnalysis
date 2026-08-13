#!/usr/bin/env python3
"""Fonde dati/righe/<operatore>.csv in dati/registro.csv.

Regola della pipeline: ogni sessione scrive SOLO su dati/righe/<slug>.csv.
registro.csv è generato, non modificato a mano: ogni esecuzione lo riscrive.

Il parsing è fatto con il modulo csv, non con tail/cat, perché i campi
contengono virgole, virgolette e a volte terminatori di riga diversi
(alcuni file sono CRLF, altri LF). Concatenare a mano questi file
disallinea le colonne in silenzio, che è il modo tipico in cui un
registro si rompe senza che nessuno se ne accorga.

Uso:  python3 dati/fondi-registro.py      (dalla cartella analisi-competitor/)
"""

import csv
import glob
import io
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RIGHE = os.path.join(BASE, "dati", "righe")
OUT = os.path.join(BASE, "dati", "registro.csv")


def leggi(percorso):
    with open(percorso, "rb") as fh:
        testo = fh.read().decode("utf-8-sig")
    return list(csv.reader(io.StringIO(testo)))


def main():
    files = sorted(glob.glob(os.path.join(RIGHE, "*.csv")))
    if not files:
        sys.exit(f"Nessun file in {RIGHE}/. Niente da fondere.")

    header = None
    righe = []
    errori = []

    for f in files:
        nome = os.path.basename(f)
        rows = leggi(f)
        if len(rows) < 2:
            errori.append(f"{nome}: meno di due righe (header + dati)")
            continue
        if header is None:
            header = rows[0]
        elif rows[0] != header:
            errori.append(f"{nome}: header diverso dal primo file")
            continue
        for r in rows[1:]:
            if not any(c.strip() for c in r):
                continue
            if len(r) != len(header):
                errori.append(f"{nome}: riga con {len(r)} campi invece di {len(header)}")
                continue
            righe.append(r)

    if errori:
        for e in errori:
            print("ERRORE:", e, file=sys.stderr)
        sys.exit(2)

    righe.sort(key=lambda r: r[0].lower())

    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(righe)

    print(f"Fusi {len(files)} file → {os.path.relpath(OUT, BASE)} "
          f"({len(righe)} righe operatore, {len(header)} colonne)")
    for r in righe:
        print("  -", r[0])


if __name__ == "__main__":
    main()
