import os
import subprocess

"""
Zusammenfassung:
Dieser Quellcode stellt Funktionen bereit, um Markdown-Dateien in HTML umzuwandeln, wobei Zitierungen mit einem spezifischen Stil und verschiedenen Bibliographiequellen berücksichtigt werden. Er nutzt das Tool "Pandoc" für die Konvertierung.
"""

# Konstanten
QUELL_ORDNER = "md"
ZIEL_ORDNER = "html"
ERWEITERUNG = ".md"
csl_datei = "content/zitierstil-number.csl"
bib_dateien = ["content/literatur-kfz.bib",
               "content/literatur-sport.bib", "content/literatur.bib"]


def sicher_verknuepfen(ordner, dateiname):
    """Verknüpft einen Ordner und einen Dateinamen sicher, um Traversierungsversuche zu vermeiden."""
    if os.path.isabs(dateiname) or dateiname.startswith(".."):
        return None
    return os.path.join(ordner, dateiname)


def markdown_nach_html_konvertieren(quell_datei, ziel_datei):
    """Verwendet Pandoc, um eine Markdown-Datei in HTML zu konvertieren mit Zitierungen."""
    befehl = ["pandoc", "--mathjax", "--csl", csl_datei]

    for bib in bib_dateien:
        befehl.extend(["--bibliography", bib])

    befehl.extend([quell_datei, "-o", ziel_datei])

    try:
        subprocess.run(befehl, check=True)
    except subprocess.CalledProcessError:
        print(f"Fehler beim Konvertieren von '{quell_datei}' mit Pandoc.")


def pandoc_ist_installiert():
    """Überprüft, ob Pandoc auf dem System installiert ist."""
    try:
        subprocess.run(["pandoc", "--version"], check=True)
        return True
    except Exception:
        return False


def main():
    if not pandoc_ist_installiert():
        print("Bitte stellen Sie sicher, dass Pandoc auf Ihrem System installiert ist.")
        return

    if not os.path.exists(QUELL_ORDNER):
        print(f"Der Ordner '{QUELL_ORDNER}' existiert nicht.")
        return

    os.makedirs(ZIEL_ORDNER, exist_ok=True)

    for dateiname in os.listdir(QUELL_ORDNER):
        if not dateiname.endswith(ERWEITERUNG):
            continue

        quell_pfad = sicher_verknuepfen(QUELL_ORDNER, dateiname)
        ziel_pfad = sicher_verknuepfen(
            ZIEL_ORDNER, os.path.splitext(dateiname)[0] + ".html")

        if not quell_pfad or not ziel_pfad:
            print(f"Ungültiger Dateiname: {dateiname}")
            continue

        markdown_nach_html_konvertieren(quell_pfad, ziel_pfad)

    print("Konvertierung abgeschlossen.")


if __name__ == "__main__":
    main()
