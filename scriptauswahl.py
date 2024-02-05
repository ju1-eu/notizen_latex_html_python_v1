"""
Dieses Script (`scriptauswahl.py`) stellt ein interaktives Menüsystem bereit, das verschiedene
Automatisierungsbefehle für die Verarbeitung von LaTeX- und HTML-Dateien anbietet.

Hauptfunktionen:
- `kombinierte_html_verarbeitung()`: Führt eine Reihe von HTML-bezogenen Befehlen sequenziell aus.
- `sicherer_aufruf(befehl)`: Führt einen gegebenen Befehl sicher aus, fängt und behandelt Fehler.
- `zeige_menue_und_waehle()`: Zeigt das Befehlsmenü an und liest die Benutzerauswahl ein.
- `pause()`: Pausiert die Ausführung, bis der Benutzer eingreift.
- `verarbeite_alle_tex_dateien()`: Synchronisiert alle `.tex`-Dateien in einem
    bestimmten Verzeichnis.
- `kombinierte_latex_verarbeitung()`: Führt eine Sequenz von Schritten zur Verarbeitung
    von LaTeX-Dateien durch.
- `main()`: Initialisiert die Benutzerschnittstelle des Menüsystems und
    verarbeitet Benutzereingaben.

Parameter:
- Keine expliziten Parameter für die Hauptfunktionen; sie werden hauptsächlich
    durch Benutzerinteraktion gesteuert.

Rückgabewerte:
- Keine der Funktionen liefert explizite Werte zurück; sie führen Seiteneffekte aus
    (z.B. Dateiverarbeitung, Ausgabe auf die Konsole).
"""

import subprocess

# Konstanten für die Befehle
LATEX_KONVERTIEREN = ["python3", "python-scripte/latex_convert1.py"]
LATEX_ENTFERNEN = ["python3", "python-scripte/latexcode_entfernen2.py"]
LATEX_SUCHEN_ERSETZEN = ["python3", "python-scripte/suchen_ersetzen.py"]
SYNC_TEX_FILES = ["python3", "python-scripte/sync_tex.py"]
MAKE = ["make"]
MAKE_XELATEX = ["make", "ENGINE=xelatex"]
MAKE_LUALATEX = ["make", "ENGINE=lualatex"]
MAKE_CLEAN = ["make", "clean"]
MAKE_CLEAN_PDF = ["make", "clean-pdf"]
HTML_PYTHON_MD = ["python3", "python-scripte/html_konverter_py_markdown1.py"]
HTML_PANDOC = ["python3", "python-scripte/html_konverter_pandoc1.py"]
HTML_VERARBEITEN = ["python3", "python-scripte/html_dateien_verarbeiten2.py"]
HTML_NAVIGATION = ["python3", "python-scripte/navigationsseite_html.py"]
HTML_ENTFERNEN = ["python3", "python-scripte/html_entfernen2.py"]


def kombinierte_html_verarbeitung():
    """Führt HTML-bezogene Befehle in einer Sequenz aus."""
    for befehl in [HTML_PANDOC, HTML_VERARBEITEN, HTML_NAVIGATION, HTML_ENTFERNEN]:
        sicherer_aufruf(befehl)


def sicherer_aufruf(befehl):
    """Führt einen Befehl sicher aus und fängt bekannte sowie unerwartete Fehler.

    Args:
        befehl (list): Der auszuführende Befehl als Liste, z.B. ['ls', '-l'].

    Verarbeitet `subprocess.CalledProcessError` für Fehler, die auftreten, wenn der Prozess
    mit einem Fehler beendet. Fängt allgemeine Ausnahmen für unerwartete Fehler, dokumentiert
    die Entscheidung für diese breite Fehlerbehandlung.
    """
    print(f"Ausführender Befehl: {befehl}")  # Debug-Ausgabe
    try:
        subprocess.run(befehl, check=True)
    except subprocess.CalledProcessError:
        print("Es gab einen Fehler beim Ausführen des Befehls.")
    except Exception as error:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {error}")
        # Die Entscheidung, Exception zu fangen, beruht auf dem Wunsch, das Skript
        # vor unvorhergesehenen Ausnahmen zu schützen, die außerhalb der Kontrolle
        # der spezifischen subprocess.run Nutzung liegen. Es wird empfohlen, diese
        # Praxis mit Vorsicht zu verwenden und spezifische Ausnahmen zu fangen,
        # wo immer es praktikabel ist.


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
    4: {"name": "Synchronisiere .tex-Dateien mit Auswahl einer Datei oder allen",
        "command": SYNC_TEX_FILES},
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
    """
    Hauptfunktion, die ein interaktives Menüsystem zur Ausführung verschiedener
    Befehle bereitstellt.

    Diese Funktion zeigt ein Menü mit verfügbaren Befehlen an, die der Benutzer ausführen kann.
    Der Benutzer wählt einen Befehl durch Eingabe der entsprechenden Nummer aus.
    Bestimmte Befehle führen spezialisierte Aufgaben aus, wie z.B. die Verarbeitung von
    LaTeX- oder HTML-Dateien. Die Funktion unterstützt auch kombinierte Befehle für
    erweiterte Verarbeitungssequenzen. Die Ausführung endet, wenn der Benutzer 'q' eingibt.

    Parameter: Keine
    Rückgabewerte: Keine.
    """
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
