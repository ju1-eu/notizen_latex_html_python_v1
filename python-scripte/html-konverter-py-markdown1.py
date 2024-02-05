import os
import markdown

"""
Zusammenfassung:
Dieser Quellcode integriert notwendige Programme und stellt Funktionen zur Umwandlung von Markdown-Dateien in HTML bereit. Dabei wird das Modul "markdown" für die Konvertierung verwendet und die resultierenden HTML-Dateien werden sicher in ein Zielverzeichnis gespeichert.
pip install markdown
pyhton3 ./html-konverter-py-markdown1.py # Markdown in HTML Konvertierung mit Python
pyhton3 ./html-konverter-pandoc1.py # Markdown in HTML Konvertierung mit pandoc
pyhton3 ./html-dateien-verarbeiten2.py # HTML Dateien verarbeiten
"""

# Konstanten
QUELL_ORDNER = "md"
ZIEL_ORDNER = "html"
ERWEITERUNG = ".md"


def sicher_verknuepfen(ordner, dateiname):
    """Verknuepft einen Ordner und einen Dateinamen sicher, um Traversierungsversuche zu vermeiden."""
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
