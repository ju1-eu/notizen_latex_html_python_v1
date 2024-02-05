import subprocess
import glob

# Konstanten für die Befehle
LATEX_KONVERTIEREN = ["python3", "python-scripte/latex-convert1.py"]
LATEX_ENTFERNEN = ["python3", "python-scripte/latexcode-entfernen2.py"]
LATEX_SUCHEN_ERSETZEN = ["python3", "python-scripte/suchen_ersetzen.py"]
SYNC_TEX_FILES = ["python3", "python-scripte/sync_tex.py"]
MAKE = ["make"]
MAKE_XELATEX = ["make", "ENGINE=xelatex"]
MAKE_LUALATEX = ["make", "ENGINE=lualatex"]
MAKE_CLEAN = ["make", "clean"]
MAKE_CLEAN_PDF = ["make", "clean-pdf"]
HTML_PYTHON_MD = ["python3", "python-scripte/html-konverter-py-markdown1.py"]
HTML_PANDOC = ["python3", "python-scripte/html-konverter-pandoc1.py"]
HTML_VERARBEITEN = ["python3", "python-scripte/html-dateien-verarbeiten2.py"]
HTML_NAVIGATION = ["python3", "python-scripte/navigationsseite-html.py"]
HTML_ENTFERNEN = ["python3", "python-scripte/html-entfernen2.py"]


def kombinierte_html_verarbeitung():
    """Führt HTML-bezogene Befehle in einer Sequenz aus."""
    for befehl in [HTML_PANDOC, HTML_VERARBEITEN, HTML_NAVIGATION, HTML_ENTFERNEN]:
        sicherer_aufruf(befehl)


def sicherer_aufruf(befehl):
    """Führt einen Befehl sicher aus."""
    print(f"Ausführender Befehl: {befehl}")  # Debug-Ausgabe
    try:
        subprocess.run(befehl, check=True)
    except subprocess.CalledProcessError:
        print("Es gab einen Fehler beim Ausführen des Befehls.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")


def zeige_menue_und_waehle():
    """Zeigt das Menü und gibt die Auswahl des Benutzers zurück."""
    print("\nBitte wählen Sie einen Befehl aus:\n")
    for key, value in BEFEHLE.items():
        print(f"{key}. {value['name']}")
    auswahl = input(
        "\nGeben Sie die Nummer des gewünschten Befehls ein oder 'q' zum Beenden: ")
    return auswahl


def pause():
    """Pausiert das Skript, bis der Benutzer fortfährt."""
    input("\nDrücken Sie Enter, um fortzufahren...")


def verarbeite_alle_tex_dateien():
    """Automatisierte Version zum Synchronisieren aller .tex-Dateien."""
    # rsync zur Synchronisation aller .tex-Dateien im Verzeichnis 'tex/'
    befehl = ["rsync", "-avh", "--progress", "tex/", "."]
    sicherer_aufruf(befehl)
    print("Alle .tex-Dateien wurden synchronisiert.")


def kombinierte_latex_verarbeitung():
    """Führt die Schritte 1 bis 4 in einer Sequenz aus."""
    print("Starte kombinierte LaTeX Verarbeitung...")

    # Schritt 1: LaTeX konvertieren für alle .tex-Dateien
    sicherer_aufruf(LATEX_KONVERTIEREN)

    # Schritt 2: LaTeX Code entfernen
    sicherer_aufruf(LATEX_ENTFERNEN)

    # Schritt 3: LaTeX Code suchen und ersetzen
    sicherer_aufruf(LATEX_SUCHEN_ERSETZEN)

    # Schritt 4: Synchronisiere .tex-Dateien
    verarbeite_alle_tex_dateien()

    # Schritt 7: make xelatex
    sicherer_aufruf(MAKE_XELATEX)

    print("Kombinierte LaTeX Verarbeitung abgeschlossen.")


BEFEHLE = {
    1: {"name": "LaTeX konvertieren", "command": LATEX_KONVERTIEREN},
    2: {"name": "LaTeX Code entfernen (Alle Dateien)", "command": LATEX_ENTFERNEN},
    3: {"name": "LaTeX Code Suchen und Ersetzen", "command": LATEX_SUCHEN_ERSETZEN},
    4: {"name": "Synchronisiere .tex-Dateien mit Auswahl einer Datei oder allen", "command": SYNC_TEX_FILES},
    5: {"name": "Kombi Latex (Schritte 1-4+7)", "command": kombinierte_latex_verarbeitung},
    6: {"name": "make (# pdflatex)", "command": MAKE},
    7: {"name": "make xelatex", "command": MAKE_XELATEX},
    8: {"name": "make lualatex", "command": MAKE_LUALATEX},
    9: {"name": "make clean - aufräumen ohne PDFs", "command": MAKE_CLEAN},
    10: {"name": "make clean-pdf - aufräumen mit PDFs", "command": MAKE_CLEAN_PDF},
    11: {"name": "Markdown in HTML Konvertierung mit Pandoc", "command": HTML_PANDOC},
    12: {"name": "HTML Dateien verarbeiten", "command": HTML_VERARBEITEN},
    13: {"name": "Navigation über HTML Seiten erstellen", "command": HTML_NAVIGATION},
    14: {"name": "HTML Code entfernen", "command": HTML_ENTFERNEN},
    15: {"name": "Kombi HTML (Schritte 11-14)", "command": kombinierte_html_verarbeitung},
}


def main():
    while True:
        auswahl = zeige_menue_und_waehle()
        if auswahl == 'q':
            break
        if auswahl.isdigit() and int(auswahl) in BEFEHLE:
            print("\n==================================================")
            if int(auswahl) == 15:
                # Rufe die kombinierte Funktion direkt auf
                BEFEHLE[15]['command']()
            elif int(auswahl) == 5:
                # Rufe die kombinierte Funktion direkt auf
                BEFEHLE[5]['command']()
            else:
                befehl = BEFEHLE[int(auswahl)]['command']
                sicherer_aufruf(befehl)
            print("==================================================")
            pause()  # Pausiert hier, damit der Benutzer die Ausgabe sehen kann
        else:
            print("Ungültige Auswahl. Bitte erneut versuchen.")


if __name__ == "__main__":
    main()
