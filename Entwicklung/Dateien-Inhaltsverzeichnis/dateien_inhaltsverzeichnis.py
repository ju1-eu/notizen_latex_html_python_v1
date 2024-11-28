"""
Dieses Skript automatisiert die Konvertierung verschiedener Dateitypen
(".md", ".cc", ".py", ".php", ".css", ".js", ".c") in HTML-Dateien.
Es wurde primär entwickelt, um Lehrmaterialien und Übungen effizient
für die Webdarstellung aufzubereiten. Neben der Konvertierung einzelner Dateien erzeugt das Skript
auch eine strukturierte Inhaltsübersicht aller verarbeiteten Materialien.

Globale Variablen:
- VERZEICHNIS: Pfad zum Quellverzeichnis, das die zu konvertierenden Dateien enthält (anpassbar).
- ZIELVERZEICHNIS: Pfad zum Zielverzeichnis, in das die konvertierten HTML-Dateien
    gespeichert werden.
- PYGMENTS_CSS_DATEI: Name der CSS-Datei, die von Pygments für das Syntax-Highlighting
    verwendet wird.
- CUSTOM_CSS_DATEI: Name der benutzerdefinierten CSS-Datei für die Formatierung der HTML-Ausgabe.

Funktionen:
- run_command(command): Führt einen gegebenen Shell-Befehl aus und gibt den Erfolg
    der Ausführung zurück.
- konvertiere_zu_html_oder_kopiere(dateipfad, zielverzeichnis): Konvertiert Dateien basierend
    auf ihrer Erweiterung in HTML oder kopiert sie direkt, falls keine Konvertierung nötig ist.
- verzeichnisstruktur_erzeugen(ordnerpfad, tiefe=0, root_verzeichnis=None): Erzeugt rekursiv
    eine HTML-Struktur, die die Verzeichnis- und Dateistruktur abbildet.
- schreibe_custom_css(zieldateipfad, inhalt): Schreibt den Inhalt der benutzerdefinierten CSS-Datei
    in das Zielverzeichnis.
- schreibe_inhaltsverzeichnis(inhalt_html_pfad, struktur_html, custom_css_datei): Erstellt das
    HTML-Inhaltsverzeichnis basierend auf der generierten Verzeichnisstruktur.
- kopiere_css_in_zielverzeichnis(quellpfad, zielverzeichnis, css_dateiname): Kopiert die CSS-Dateien
    in das Zielverzeichnis, um die Formatierung der HTML-Ausgabe zu unterstützen.

Verwendung:
- Passen Sie die Pfade in den globalen Variablen an Ihre Bedürfnisse an.
- Führen Sie das Skript aus, um die Dateien im angegebenen Quellverzeichnis zu konvertieren und
    die Ergebnisse im Zielverzeichnis zu speichern.
"""

import os
import shutil
import subprocess

# Globale Variablen
VERZEICHNIS = "./Testordner"  # anpassen
ZIELVERZEICHNIS = "./html"
PYGMENTS_CSS_DATEI = "pygments_style.css"
CUSTOM_CSS_DATEI = "custom_style.css"

# Mapping von Dateiendungen zu Sprachoptionen für pygmentize
sprachoptionen = {
    ".py": "python",
    ".php": "php",
    ".js": "javascript",
    ".c": "c",
    ".cc": "cpp",  # Korrektur für C++ Dateien
}


def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    # Ausgabe unabhängig vom Erfolg, um zu helfen, das Problem zu diagnostizieren
    print(
        f"Ausgeführter Befehl: {' '.join(command)}\nStdout: {result.stdout}\nStderr: {result.stderr}"
    )
    return result.returncode == 0


def konvertiere_zu_html_oder_kopiere(dateipfad, zielverzeichnis):
    dateiname, dateiendung = os.path.splitext(os.path.basename(dateipfad))
    zieldateipfad = os.path.join(zielverzeichnis, dateiname + ".html")

    if dateiendung.lower() == ".md":
        css_dateipfad = os.path.abspath(os.path.join(ZIELVERZEICHNIS, CUSTOM_CSS_DATEI))
        command = ["pandoc", dateipfad, "-o", zieldateipfad, "-s", "--mathjax", "-c", css_dateipfad]
        if run_command(command) and os.path.exists(zieldateipfad):
            print(f"Markdown-Datei erfolgreich konvertiert: {zieldateipfad}")
        else:
            print(
                f"Konvertierung fehlgeschlagen oder Ausgabedatei nicht erstellt für {zieldateipfad}"
            )
    elif dateiendung.lower() == ".pdf":
        shutil.copy2(dateipfad, zieldateipfad)  # Kopiert die PDF-Datei direkt ins Zielverzeichnis
        print(f"PDF-Datei kopiert: {dateipfad}")
    elif dateiendung.lower() in sprachoptionen:
        sprache = sprachoptionen[dateiendung.lower()]
        command = [
            "pygmentize",
            "-l",
            sprache,
            "-f",
            "html",
            "-O",
            f"full,cssfile={PYGMENTS_CSS_DATEI}",
            "-o",
            zieldateipfad,
            dateipfad,
        ]
        if not run_command(command):
            print(f"Konvertierung fehlgeschlagen für {dateipfad}")
        else:
            print(f"Code-Datei erfolgreich hervorgehoben und konvertiert: {dateipfad}")
    else:
        print(f"Keine Aktion definiert für Dateiendung: {dateiendung}")


def verzeichnisstruktur_erzeugen(ordnerpfad, tiefe=0, root_verzeichnis=None):
    """Erzeugt die Verzeichnisstruktur als HTML."""
    if root_verzeichnis is None:
        root_verzeichnis = ordnerpfad

    struktur_html = ""
    for element in sorted(os.listdir(ordnerpfad)):
        voller_pfad = os.path.join(ordnerpfad, element)
        einzug = "    " * tiefe
        if os.path.isdir(voller_pfad):
            struktur_html += f"{einzug}<li class='dir'>{element}<ul>\n"
            struktur_html += verzeichnisstruktur_erzeugen(voller_pfad, tiefe + 1, root_verzeichnis)
            struktur_html += f"{einzug}</ul></li>\n"
        else:
            dateiname, dateiendung = os.path.splitext(element)
            # Hier überprüfen Sie, ob die Datei eine .pdf-Datei ist
            if dateiendung.lower() == ".pdf":
                # Für PDF-Dateien verwenden Sie den originalen Dateinamen und Pfad
                pfad_zur_datei = os.path.relpath(voller_pfad, start=root_verzeichnis)
                struktur_html += (
                    f"{einzug}<li class='file'><a href='./{pfad_zur_datei}'>{element}</a></li>\n"
                )
            elif dateiendung.lower() in [".md", ".cc", ".py", ".php", ".css", ".js", ".c"]:
                # Für andere Dateitypen (außer .pdf) generieren Sie eine .html-Datei
                html_dateiname = dateiname + ".html"
                struktur_html += (
                    f"{einzug}<li class='file'><a href='./{html_dateiname}'>{element}</a></li>\n"
                )
            # Für .pdf Dateien ist keine Konvertierung nötig, nur das Kopieren
    return struktur_html


def schreibe_custom_css(zieldateipfad, inhalt):
    with open(zieldateipfad, "w", encoding="utf-8") as css_file:
        css_file.write(inhalt)


def schreibe_inhaltsverzeichnis(inhalt_html_pfad, struktur_html, custom_css_datei):
    with open(inhalt_html_pfad, "w", encoding="utf-8") as html_datei:
        html_datei.write(
            "<!DOCTYPE html>\n<html lang='de'>\n<head>\n<meta charset='UTF-8'>\n<title>Inhaltsverzeichnis</title>\n"
        )
        html_datei.write(f"<link rel='stylesheet' href='./{custom_css_datei}'>\n")
        html_datei.write("</head>\n<body>\n")
        html_datei.write(
            "<div class='container'>\n<h1>Inhaltsverzeichnis</h1>\n<ul class='root'>\n"
        )
        html_datei.write(struktur_html)
        html_datei.write("</ul>\n</div>\n</body>\n</html>")


def kopiere_css_in_zielverzeichnis(quellpfad, zielverzeichnis, css_dateiname):
    quell_dateipfad = os.path.join(quellpfad, css_dateiname)
    ziel_dateipfad = os.path.join(zielverzeichnis, css_dateiname)
    shutil.copy2(quell_dateipfad, ziel_dateipfad)
    print(f"CSS-Datei '{css_dateiname}' wurde nach '{zielverzeichnis}' kopiert.")


# Hauptlogik
if __name__ == "__main__":
    # Erstelle das Zielverzeichnis, falls es nicht existiert
    os.makedirs(ZIELVERZEICHNIS, exist_ok=True)

    # Kopiere die CSS-Datei in das Zielverzeichnis
    kopiere_css_in_zielverzeichnis(".", ZIELVERZEICHNIS, CUSTOM_CSS_DATEI)

    # Unterstützte Dateiendungen für die Konvertierung
    unterstuetzte_dateiendungen = [".md", ".cc", ".py", ".php", ".css", ".pdf", ".js", ".c"]

    # Durchlaufe das Verzeichnis und konvertiere alle unterstützten Dateien
    for root, dirs, files in os.walk(VERZEICHNIS):
        for file in files:
            # Prüfe, ob die Dateiendung in der Liste der unterstützten Endungen ist
            if any(file.endswith(endung) for endung in unterstuetzte_dateiendungen):
                voller_pfad = os.path.join(root, file)
                konvertiere_zu_html_oder_kopiere(voller_pfad, ZIELVERZEICHNIS)

    # Erzeuge die Verzeichnisstruktur als HTML
    struktur_html = verzeichnisstruktur_erzeugen(VERZEICHNIS)
    inhalt_html = os.path.join(ZIELVERZEICHNIS, "inhaltverzeichnis.html")

    # Schreibe das Inhaltsverzeichnis und die Verzeichnisstruktur in eine HTML-Datei
    schreibe_inhaltsverzeichnis(inhalt_html, struktur_html, CUSTOM_CSS_DATEI)

    print(
        "Konvertierung abgeschlossen. Die HTML- und CSS-Dateien befinden sich im Verzeichnis:",
        ZIELVERZEICHNIS,
    )
