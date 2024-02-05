"""
Dieses Skript konvertiert Markdown-Dateien (.md) in HTML-Dateien und speichert diese in einem
Zielverzeichnis.
Es nutzt das 'markdown'-Modul für die Konvertierung und stellt sicher, dass die Dateipfade sicher
gehandhabt werden, um Verzeichnistraversierungen zu vermeiden.

Verwendung:
1. Stellen Sie sicher, dass das 'markdown'-Modul installiert ist: `pip install markdown`.
2. Führen Sie das Skript aus dem Verzeichnis aus, das die Markdown-Dateien enthält.

Funktionsweise:
- Der Skript durchsucht den Quellordner nach Dateien mit der Erweiterung '.md'.
- Für jede gefundene Markdown-Datei wird der Inhalt konvertiert und als HTML-Datei im Zielordner
    gespeichert.
- Dateinamen und Verzeichnispfade werden sicher gehandhabt, um Sicherheitsrisiken wie
    Verzeichnistraversierung zu minimieren.

Konstanten:
- QUELL_ORDNER: Verzeichnis mit den Quelldateien (Standard: "md").
- ZIEL_ORDNER: Verzeichnis für die konvertierten HTML-Dateien (Standard: "html").
- ERWEITERUNG: Die Dateierweiterung der zu konvertierenden Dateien (Standard: ".md").

Funktionen:
- sicher_verknuepfen(ordner, dateiname): Verknüpft einen Ordner und einen Dateinamen sicher.
- markdown_nach_html_konvertieren(quell_datei): Konvertiert den Inhalt einer Markdown-Datei
    in HTML.
- html_in_datei_schreiben(html_inhalt, ziel): Speichert den HTML-Inhalt in einer Datei im
    Zielverzeichnis.
- main(): Hauptfunktion, die die Konvertierung koordiniert und die anderen Funktionen aufruft.

Hinweise:
- Das Skript setzt voraus, dass das 'markdown'-Modul installiert ist und verwendet wird.
- Es wird empfohlen, dieses Skript in einer vertrauenswürdigen Umgebung auszuführen, da es
    Dateioperationen durchführt.

Beispielaufruf:
    python3 html-konverter-py-markdown1.py
"""

import os
import markdown


# Konstanten
QUELL_ORDNER = "md"
ZIEL_ORDNER = "html"
ERWEITERUNG = ".md"


def sicher_verknuepfen(ordner, dateiname):
    """Verknuepft einen Ordner und einen Dateinamen sicher, um Traversierungsversuche
    zu vermeiden."""
    if os.path.isabs(dateiname) or dateiname.startswith(".."):
        return None
    return os.path.join(ordner, dateiname)


def markdown_nach_html_konvertieren(quell_datei):
    """Konvertiert eine Markdown-Datei in HTML."""
    with open(quell_datei, 'r', encoding='utf-8') as f:
        inhalt = f.read()
    return markdown.markdown(inhalt, extensions=['fenced_code'])


def html_in_datei_schreiben(html_inhalt, ziel):
    """Schreibt den HTML-Inhalt in eine Datei."""
    with open(ziel, 'w', encoding='utf-8') as f:
        f.write(html_inhalt)


def main():
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
            print(f"Ungueltiger Dateiname: {dateiname}")
            continue

        try:
            html_inhalt = markdown_nach_html_konvertieren(quell_pfad)
            html_in_datei_schreiben(html_inhalt, ziel_pfad)
        except Exception as e:
            print(f"Fehler beim Verarbeiten von '{dateiname}': {e}")

    print("Konvertierung abgeschlossen.")


if __name__ == "__main__":
    main()
