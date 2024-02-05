import os
from html import escape
from jinja2 import Environment, FileSystemLoader

"""
Das Programm durchsucht einen Ordner nach HTML-Dateien und erstellt mithilfe einer Vorlage eine Navigationsseite, die Links zu diesen Dateien enthält. Bei erfolgreicher Erstellung gibt es eine Benachrichtigung über die Anzahl der eingebundenen Links aus.
"""


def finde_html_dateien(ordnerpfad):
    for dateiname in os.listdir(ordnerpfad):
        if dateiname.endswith('.html'):
            yield dateiname


def erstelle_navigationsseite(ordnerpfad, vorlagenpfad, vorlagenname, ausgabe_dateiname):
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

    print(f"'{ausgabe_dateiname}' wurde erfolgreich erstellt mit {
          len(dateinamen)} Links.")


def main():
    ordnerpfad = "html"  # Setzen Sie hier den Pfad zum Ordner
    vorlagenpfad = './content'  # Der aktuelle Ordner
    vorlagenname = 'vorlage-nav.html'  # Der Name der Vorlagendatei
    ausgabe_dateiname = 'NAVIGATION.html'  # Der Name der Ausgabe-Datei
    erstelle_navigationsseite(ordnerpfad, vorlagenpfad,
                              vorlagenname, ausgabe_dateiname)


if __name__ == "__main__":
    main()
