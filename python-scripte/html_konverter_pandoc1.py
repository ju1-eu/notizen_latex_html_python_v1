"""
Dieses Skript konvertiert Markdown-Dateien in HTML unter Verwendung von Pandoc und berücksichtigt
dabei Zitierungen
mit einem spezifischen Zitierstil sowie mehrere Bibliographiequellen. Es ermöglicht die Erstellung
von HTML-Dokumenten
mit akademischen Referenzen direkt aus Markdown-Quelldateien.

Funktionalitäten:
- Durchsucht einen spezifizierten Quellordner nach Markdown-Dateien und konvertiert diese in
    HTML-Dateien im Zielordner.
- Nutzt Pandoc für die Konvertierung und wendet dabei einen spezifischen CSL-Zitierstil an.
- Bezieht Informationen aus mehreren Bibliographiequellen (.bib-Dateien) für die Zitierungen.
- Prüft, ob Pandoc auf dem System installiert ist, bevor mit der Konvertierung begonnen wird.
- Verwendet sichere Pfadverknüpfungen, um Traversierungsversuche zu verhindern.

Konstanten:
- QUELL_ORDNER: Verzeichnis, das die zu konvertierenden Markdown-Quelldateien enthält.
- ZIEL_ORDNER: Verzeichnis für die resultierenden HTML-Dateien.
- ERWEITERUNG: Die Dateierweiterung der zu konvertierenden Dateien (Standard: ".md").
- csl_datei: Der Pfad zur CSL-Datei, die den Zitierstil definiert.
- bib_dateien: Eine Liste von Pfaden zu .bib-Dateien, die die Bibliographiequellen enthalten.

Funktionen:
- sicher_verknuepfen(ordner, dateiname): Verknüpft einen Ordner und einen Dateinamen sicher.
- markdown_nach_html_konvertieren(quell_datei, ziel_datei): Konvertiert eine einzelne
    Markdown-Datei in eine HTML-Datei unter Verwendung von Pandoc.
- pandoc_ist_installiert(): Überprüft, ob Pandoc auf dem System installiert ist.
- main(): Hauptfunktion, die die Konvertierung koordiniert und die anderen Funktionen aufruft.

Verwendung:
- Stellen Sie sicher, dass Pandoc installiert ist und die erforderlichen .bib- und .csl-Dateien
    verfügbar sind.
- Passen Sie bei Bedarf die Konstanten an Ihre Umgebung an.
- Führen Sie das Skript aus, um die Konvertierung zu starten.

Beispielaufruf:
    python3 mein_skript.py

Anforderungen:
- Pandoc muss auf dem System installiert sein.

Hinweis:
- Das Skript setzt voraus, dass die Quelldateien korrekt formatiertes Markdown enthalten und
    dass die Bibliographiequellen und der Zitierstil korrekt definiert sind.
"""

import os
import subprocess


# Konstanten
QUELL_ORDNER = "md"
ZIEL_ORDNER = "html"
ERWEITERUNG = ".md"
CSL_DATEI = "content/zitierstil-number.csl"
bib_dateien = ["content/literatur-kfz.bib",
               "content/literatur-sport.bib", "content/literatur.bib"]


def sicher_verknuepfen(ordner, dateiname):
    """Verknüpft einen Ordner und einen Dateinamen sicher, um Traversierungsversuche
    zu vermeiden."""
    if os.path.isabs(dateiname) or dateiname.startswith(".."):
        return None
    return os.path.join(ordner, dateiname)


def markdown_nach_html_konvertieren(quell_datei, ziel_datei):
    """Verwendet Pandoc, um eine Markdown-Datei in HTML zu konvertieren mit Zitierungen."""
    befehl = ["pandoc", "--mathjax", "--csl", CSL_DATEI]

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
