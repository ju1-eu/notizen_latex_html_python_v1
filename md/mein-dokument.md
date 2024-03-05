---
thema: "Anwendung von Markdown-Techniken für Dokumentationen"
runningtitle: "Dokumentation mit Markdown"
keywords: "Markdown, Dokumentation, Pandoc, Konvertierung, Fußnoten, Tabellen, Code-Blöcke, Hyperlinks, Bilder, Multimedia-Integration"
abstract: |
  In der heutigen schnelllebigen Zeit ist die Fähigkeit, komplexe Informationen klar und effizient zu kommunizieren, von entscheidender Bedeutung. Markdown, eine leichtgewichtige Markup-Sprache, hat sich als ein wertvolles Werkzeug für die Erstellung technischer Dokumentationen und die Unterstützung von Entwicklungsprojekten etabliert.

  Ein weiterer Vorteil von Markdown ist die nahtlose Konvertierung in andere Formate wie HTML und PDF durch Werkzeuge wie Pandoc, was die Verbreitung von Dokumenten über verschiedene Plattformen und Medien hinweg vereinfacht.
author: 'ju'
date: \today
---
<!-------------------------------------------------------------------------------------------------------------
ju 5-2-24 mein-dokument.md
pandoc mein-dokument.md -o mein-dokument.html -c navigation.css --mathjax --citeproc --bibliography=literatur.bib --csl=zitierstil-number.csl

Quelle [@spanner:2019:robotik].

Fußnote.[^1]
[^1]: Text der Fußnote.

[Google](https://www.google.com)

![Logo 2](images/Logo/Logo2.pdf)

**Tabelle 1:** Beschreibung

pandoc mein-dokument.md --to latex --output mein-dokument.tex --template=vorlage-main.tex --lua-filter=combined-filter.lua
pdflatex mein-dokument.tex
biber mein-dokument
pdflatex mein-dokument.tex
pdflatex mein-dokument.tex
---------------------------------------------------------------------------------------------------------------->
# Dokumente in Markdown erstellen


```plaintext
// Projektübersicht
Entwicklung               git_hilfsprogramm.py      mein-dokument.fls
LICENSE                   html                      mein-dokument.tex
Makefile                  image_resizer.py          navigation.css
NAVIGATION.html           images                    python-scripte
README.md                 literatur-kfz.bib         scriptauswahl.py
TODO.md                   literatur-sport.bib       tex
Tabellen                  literatur.bib             vorlage-design-main.cls
content                   md
dokumentation.py
```



Beispiel Quellenangabe

- Fachbuchautor [@dalwigk:2024:fachbuchautor].
- Online Kurse [@schaffranek:2024:kurse].
- Hacking und Cyber Security mit KI [@dalwigk:2023:hacking].
- Python für Einsteiger [@dalwigk:2022:python].
- Mikrocontroller ESP32 [@brandes:2023:mikrocontroller].
- Roboterauto [@brandes:2022:esp32].
- Daten mit Raspberry Pi im Netz speichern und visualisieren [@brandes:2023:daten].

Hier ist ein Text, der eine Fußnote benötigt.[^2]

[^2]: Text der Fußnote.

Liste

1. eins
2. zwei

**Tabelle 1:** Diese Tabelle gibt eine übersichtliche Darstellung der ausgeführten Skripte, ihrer jeweiligen Funktionen und der Ergebnisse der Ausführung.

| Skriptname                     | Beschreibung                            | Ergebnis                              |
| :----------------------------- | :-------------------------------------- | :------------------------------------ |
| `html_konverter_pandoc1.py`    | Konvertiert HTML-Dokumente mit Pandoc   | Erfolgreich abgeschlossen             |
| `html_dateien_verarbeiten2.py` | Verarbeitet HTML-Dateien                | Erfolgreich abgeschlossen             |
| `navigationsseite_html.py`     | Erzeugt Navigationsseiten mit Jinja2    | Fehler: Modul 'jinja2' nicht gefunden |
| `html_entfernen2.py`           | Bearbeitet die Datei mein-dokument.html | Erfolgreich abgeschlossen             |


\newpage

```cpp
// Quellcode: HalloWelt.cpp
#include <iostream>

int main() {
    std::cout << "Hallo Welt" << std::endl;
    return 0;
}
```

```markdown
// Markdown
[Google](https://www.google.com)

![Logo 2](images/Logo/Logo2.pdf)
```

Website [Google](https://www.google.com) und GitHub <https://github.com/ju1-eu> und meine Website <https://bw-ju.de/>

![Logo 2](images/Logo/Logo2.pdf)

![Git-Python-Entwicklung](images/Git-Python-Entwicklung.pdf)
