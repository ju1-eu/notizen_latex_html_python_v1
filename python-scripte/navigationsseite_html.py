"""
Dieses Skript durchsucht einen spezifizierten Ordner nach HTML-Dateien und erstellt eine
Navigationsseite, die Links zu diesen Dateien enthält. Die Navigationsseite wird auf der Basis
einer Jinja2-Vorlage generiert. Nach der Erstellung der Navigationsseite gibt das Skript eine
Benachrichtigung über die Anzahl der in die Navigationsseite eingebundenen Links aus.

Funktionen:
- finde_html_dateien(ordnerpfad): Durchläuft den angegebenen Ordner und generiert einen Generator
    für alle HTML-Dateinamen.
- erstelle_navigationsseite(ordnerpfad, vorlagenpfad, vorlagenname, ausgabe_dateiname): Verwendet
    die gefundenen HTML-Dateien und eine Jinja2-Vorlage, um die Navigationsseite zu erstellen und in
    einer spezifizierten Datei zu speichern.
- main(): Definiert die Pfade und Namen für Ordner, Vorlage und Ausgabedatei und ruft die Funktion
    zum Erstellen der Navigationsseite auf.

Verwendung:
- Das Skript wird ohne Argumente ausgeführt. Die Pfade und Namen für den Ordner mit den

HTML-Dateien, den Pfad zur Vorlage, den Namen der Vorlagendatei und den Namen der Ausgabedatei
sind im Code festgelegt.

Beispiel:
    python create_navigation.py

Anforderungen:
- Python 3
- Jinja2

Konstanten:
- ordnerpfad: Der Pfad zum Ordner, der die HTML-Dateien enthält, die in die Navigationsseite
    eingebunden werden sollen.
- vorlagenpfad: Der Pfad zum Ordner, der die Jinja2-Vorlage enthält.
- vorlagenname: Der Name der Jinja2-Vorlagendatei.
- ausgabe_dateiname: Der Name der Datei, in der die Navigationsseite gespeichert wird.

Hinweis:
- Stellen Sie sicher, dass Jinja2 mit `pip install Jinja2` installiert ist, bevor Sie das Skript
    ausführen.
"""

import os
from html import escape
from jinja2 import Environment, FileSystemLoader



def finde_html_dateien(ordnerpfad):
    """Durchläuft den angegebenen Ordner und generiert einen Generator
    für alle HTML-Dateinamen."""
    for dateiname in os.listdir(ordnerpfad):
        if dateiname.endswith('.html'):
            yield dateiname


def erstelle_navigationsseite(ordnerpfad, vorlagenpfad, vorlagenname, ausgabe_dateiname):
    """Verwendet
    die gefundenen HTML-Dateien und eine Jinja2-Vorlage, um die Navigationsseite zu erstellen und in
    einer spezifizierten Datei zu speichern."""
    dateinamen = list(finde_html_dateien(ordnerpfad))

    if not dateinamen:
        print("Keine HTML-Dateien gefunden.")
        return

    dateinamen = [escape(dateiname) for dateiname in sorted(
        dateinamen)]  # Sortiere die Dateinamen hier

    env = Environment(loader=FileSystemLoader(vorlagenpfad))
    vorlage = env.get_template(vorlagenname)

    with open(ausgabe_dateiname, 'w', encoding='utf-8') as nav_file:
        nav_file.write(vorlage.render(dateinamen=dateinamen))

    print(f"'{ausgabe_dateiname}' wurde erfolgreich erstellt mit {len(dateinamen)} Links.")


def main():
    """Definiert die Pfade und Namen für Ordner, Vorlage und Ausgabedatei und ruft die Funktion
    zum Erstellen der Navigationsseite auf."""
    ordnerpfad = "html"  # Setzen Sie hier den Pfad zum Ordner
    vorlagenpfad = './content'  # Der aktuelle Ordner
    vorlagenname = 'vorlage-nav.html'  # Der Name der Vorlagendatei
    ausgabe_dateiname = 'NAVIGATION.html'  # Der Name der Ausgabe-Datei
    erstelle_navigationsseite(ordnerpfad, vorlagenpfad,
                              vorlagenname, ausgabe_dateiname)


if __name__ == "__main__":
    main()
