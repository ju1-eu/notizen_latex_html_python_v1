---
title: "Markdown"
thema: "Anwendung von Markdown-Techniken für Dokumentationen"
runningtitle: "Dokumentation mit Markdown"
keywords: "\\textbf{Keywords:} Markdown, Dokumentation, Pandoc, Konvertierung, Fußnoten, Tabellen, Code, Hyperlinks, Bilder, Literatur"
abstract: |
  \includegraphics[width=0.6\textwidth]{images/Mindmap-Markdown.pdf}

  Markdown ist eine leichtgewichtige Auszeichnungssprache, die entwickelt wurde, um das Schreiben von Webinhalten zu vereinfachen. Sie ermöglicht es Autoren, mit einer einfachen Textformatierungssyntax Dokumente zu erstellen, die dann in HTML umgewandelt werden können. Markdown wurde 2004 von John Gruber in Zusammenarbeit mit Aaron Swartz entworfen, mit dem Ziel, Lesbarkeit und Einfachheit in den Vordergrund zu stellen.

  Git ist ein weit verbreitetes Versionskontrollsystem, das von Entwicklern verwendet wird, um den Überblick über Änderungen an ihren Codeprojekten zu behalten. Es unterstützt die Zusammenarbeit, indem es mehreren Benutzern ermöglicht, an denselben Projekten zu arbeiten, ohne sich gegenseitig zu behindern.

  Eine Mindmap ist ein visuelles Diagramm, das dazu dient, Informationen hierarchisch und in einem vernetzten Format darzustellen, wobei ein zentrales Konzept oder Thema in der Mitte platziert und verwandte Themen oder Ideen drum herum angeordnet werden.

  Python ist eine weit verbreitete, hochgradig vielseitige Programmiersprache, die für ihre Einfachheit und Lesbarkeit bekannt ist. Sie unterstützt verschiedene Programmierparadigmen wie objektorientiert, imperativ und in gewissem Maße auch funktional.
date: \today
---
<!-------------------------------------------------------------------------------------------------------------
ju 30-3-24 mein-dokument.md
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

ChatGPT:

Schreibstil: Expositorisch ohne Form du/sie
Prüfe Rechtschreibung und Grammatik
Erstelle eine ansprechende Zusammenfassung zum nachfolgenden Text in Aufzählungsform und gleichzeitig gebe die wichtigsten Informationen genau wieder.

Zusammenfassung in Latex: Schreibstil: Expositorisch ohne Form du/sie
Erstellen Sie eine kurze (ca. 200 Wörter) und ansprechende Zusammenfassung zum nachfolgenden Text. Die Zusammenfassung sollte für jemanden ohne wissenschaftlichen Hintergrund verständlich sein und gleichzeitig die wichtigsten Fakten genau wiedergeben. Beachte den Zusammenhang. Textinhalt: " "

Keywords: Erstelle mir eine kommagetrennte Liste der wichtigsten Keywords zum Textinhalt.

Erklärung in Latex: Erkläre die Schlüsselwörter. Bereite die Antwort gehirngerecht auf mit Didaktische Reduktion.

Basierend auf den Schlüsselwörtern und deren Zusammenhang
erstelle eine detaillierte Struktur für eine Mindmap
erstelle eine Mindmap in LaTeX, benutze das Paket tikz

neue Infos: Erklären Sie einem Gymnasiasten, der sich mit Programmierung beschäftigt, das Konzept von Git.

Gedankenkette: Könnten Sie kurz das Konzept von Git erläutern? Wie beeinflusst Git die Programmiersprache und in welchen Zusammenhang steht es?

Kognitives Prüfmuster: Wenn ich eine Frage zu Git stelle, teilen Sie sie in drei kleinere Fragen auf, die Ihnen helfen, eine genauere Antwort zu geben. Kombinieren Sie die Antworten auf diese Unterfragen, um die endgültige Antwort zu erhalten.

Rolle - Programmierexperten: Nehmen Sie die Rolle eines erfahrenen Programmierexperten an. Führen Sie anhand dieser Person ein Codeüberprüfung durch.

Rolle - Cybersicherheitsexperten: Nehmen Sie die Rolle eines erfahrenen Cybersicherheitsexperten an. Führen Sie anhand dieser Person ein Überprüfung durch.

Zusammenfassung: Thema: C - Programmierung
Schreibstil: Expositorisch ohne Form du/sie, verwende Markdown
Erstelle eine ansprechende Zusammenfassung zum nachfolgenden Text in Aufzählungsform und gleichzeitig gebe die wichtigsten Informationen genau wieder. Bereite die Antwort gehirngerecht auf mit Didaktische Reduktion.
Textinhalt: " "

Fragen: Erstelle 5x Fragen zum Lerninhalt (beachte den Focus: tieferes Verständnis und kritisches Denken zu fördern) mit Lösung. Lerninhalt: " "

Projekt: Erstelle ein Projekt zum Anwenden des gelernten mit Lösung.
------------------------
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

Git

![Was ist Git?](images/Mindmap-Git.pdf)

```bash
# Git Versionierung
gh auth login
git config --global credential.helper cache

git remote -v

git init --bare
git remote add local /Users/jan/notizen_latex_html_python_v1.git
git remote rename localBackup local
git push local main
git pull local main

git init
git remote set-url origin https://github.com/ju1-eu/notizen_latex_html_python_v1.git
git push -u origin main
git pull origin main

git push
git pull
git  st
git ls

git clone https://github.com/ju1-eu/notizen_latex_html_python_v1.git
git clone /Users/jan/notizen_latex_html_python_v1.git notizen_klon
```

Latex

```bash
wget https://mirror.ctan.org/systems/texlive/tlnet/update-tlmgr-latest.sh
sudo sh update-tlmgr-latest.sh -- --accept

sudo chown -R $(whoami) /usr/local/texlive/

# Pakete installieren
tlmgr install pgf

# alle installierten Pakete zu aktualisieren
tlmgr update --all

# Überprüfung der Installation
tlmgr --version
tlmgr list --installed
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

![Was ist eine Mindmap?](images/Mindmap.pdf)

![Was ist Python?](images/Mindmap-Python.pdf)