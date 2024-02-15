---
title: "Git-Workflow-C-Entwicklung"
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!-----------------------------------------------------------------------
ju 9-2-24 Git-Workflow-C-Entwicklung.md
pandoc Git-Workflow-C-Entwicklung.md -o Git-Workflow-C-Entwicklung.html -c inhalt.css --mathjax
------------------------------------------------------------------------->
# Git-Workflow C-Entwicklung



## C-Entwicklung

```C
// hallo-welt.c
#include <stdio.h>

int main() {
    printf("Hallo Welt\n");
    return 0; // Erfolgreicher Exit-Code
}
```

ChatGPT <https://chat.openai.com/>

```markdown
# Für C- oder C++-Projekte wird oft der JavaDoc-Stil empfohlen
Erstelle Code mit Doxygen-kompatiblen Kommentaren

# Zusammenfassung
GitHub-Flavored Markdown
Schreibstil: Expositorisch ohne Form du/sie
Erstelle je nach Schreibstil eine ansprechende Zusammenfassung des folgenden Artikels in Aufzählungsform und gleichzeitig gebe die wichtigsten Informationen (Didaktische Reduktion) genau wieder. Bereite die Antwort gehirngerecht auf.
```

```bash
# Dokumentation aktualisieren
# Dokumentation/html/index.html
# Dokumentation/latex/refman.pdf
# Terminal
doxygen Doxyfile #oder make docs
# cd /Users/jan/daten/start/Programmierung/Git/C-Entwicklung/hello-world/Dokumentation/latex/
#make  # .pdf

make
make DEBUG=1 // für den Debug-Modus
make DEBUG=0 // Release-Modus
make clean
make docs
make quality
make check_format

./run_tests.sh
npm test

mkdir Beispiele Projekte Dokumentation Tutorials
#mkdir .github/workflows
vim .github/workflows/ci.yml
vim .github/workflows/nodejs.yml
vim .gitignore
vim Makefile
vim run_tests.sh
vim .clang-format

git add .
git commit -m"update "
git push
```

**cppcheck**

Der Inhalt von `checkers_report.txt` bietet eine umfassende Übersicht über die von `cppcheck` während der Analyse aktivierten Prüfungen (Checker). Dieser Bericht zeigt, dass eine Vielzahl von Prüfungen für verschiedene Aspekte der Codequalität und -sicherheit durchgeführt wurden, einschließlich, aber nicht beschränkt auf:

- **Buffer Overruns**: Prüfungen, die darauf abzielen, Pufferüberläufe und falsche Array-Index-Zugriffe zu identifizieren.
- **Null Pointer Dereferencing**: Identifizierung von Fällen, in denen möglicherweise ein Nullzeiger dereferenziert wird.
- **Memory Leaks**: Suchen nach Speicherlecks, wo allozierter Speicher nicht freigegeben wird.
- **Uninitialized Variables**: Erkennung von Variablen, die verwendet werden, bevor sie initialisiert wurden.
- **Incorrect String Operations**: Überprüfung auf falsche Nutzung von String-Funktionen, die zu Pufferüberläufen oder anderen Fehlern führen können.
- **Arithmetic Checks**: Überprüfung auf mögliche Überläufe, Division durch Null und andere arithmetische Fehler.

Die Prüfungen sind in verschiedene Kategorien unterteilt, darunter kritische Fehler, Open-Source-Prüfungen, Premium-Prüfungen (nicht verfügbar in der Open-Source-Version von `cppcheck`), und spezifische Regelsätze für Standards wie AUTOSAR, CERT C/C++, und MISRA C/C++.



## GitHub Actions Workflow

Der GitHub Actions Workflow automatisiert den gesamten Prozess des Kompilierens und Testens Ihres Programms bei jedem Push oder Pull Request. Die Workflow-Datei (`ci.yml`), die Sie in Ihrem `.github/workflows` Verzeichnis erstellen, könnte folgendermaßen aussehen, um das Makefile und das Testskript auf einem macOS-Runner zu nutzen:

1. Wird bei jedem Push oder Pull Request auf den `main` Branch ausgelöst.
2. Führt den Build-Prozess durch (`make all`), um Ihr Programm zu kompilieren.
3. Führt Tests aus (`make test`), was das `run_tests.sh` Skript aufruft.

```bash
node -v
npm -v
# Initialisieren eines neuen Node.js-Projekts
# erstellt package.json
npm init
# Node.js aktualisieren
# Node.js mit einem Paketmanager (nvm = Node Version Manager)
nvm install 20
nvm use 20
# npm zu aktualisieren
npm install -g npm@10.2.4

# Abhängigkeiten installieren die in package.json definiert sind.
npm install
# Tests ausführen
npm test

vim package.json
    {
    "name": "hello-world",
    "version": "1.0.0",
    "description": "Eine kurze Beschreibung Ihres Projekts. Dies sollte das Hauptziel und den Zweck Ihres Projekts klar umreißen.",
    "main": "index.js",
    "scripts": {
        "test": "(./run_tests.sh)"
    },
    "repository": {
        "type": "git",
        "url": "git+https://github.com/ju1-eu/hello-world.git"
    },
    "author": " (Jan Unger)",
    "license": "ISC",
    "bugs": {
        "url": "https://github.com/ju1-eu/hello-world/issues"
    },
    "homepage": "https://github.com/ju1-eu/hello-world#readme"
    }

# Erstellen einer Doxyfile
doxygen -g Doxyfile
vim Doxyfile
    # PROJECT_NAME: C-Entwicklung
    # INPUT: .
    # RECURSIVE: YES
    # OUTPUT_DIRECTORY: Dokumentation
    # FILE_PATTERNS = *.c *.h
    # EXCLUDE =
    # EXCLUDE_PATTERNS =
    # GENERATE_HTML = YES
    # HAVE_DOT = YES
    # CLASS_GRAPH            = YES
    # COLLABORATION_GRAPH    = YES
    # INCLUDE_GRAPH          = YES
    # CALL_GRAPH             = YES
    # CALLER_GRAPH           = YES
    # DOT_PATH               = /usr/local/Cellar/graphviz/9.0.0/bin

# Für C- oder C++-Projekte wird oft der JavaDoc-Stil empfohlen
# Erstelle Code mit Doxygen-kompatiblen Kommentaren versehen
    /**
    * @file main.c
    * @brief Eine Beispiel-Funktion.
    *
    * Diese Funktion demonstriert den JavaDoc-Kommentarstil.
    * @param x Ein Eingabeparameter vom Typ int.
    * @return Das Ergebnis der Berechnung als int.
    */
    float floatValue = 1.23f; ///< Float mit begrenzter Präzision
# @file tag gibt an, zu welcher Datei der Kommentar gehört.
# @brief bietet eine kurze Beschreibung des nachfolgenden Codes.
# @return beschreibt, was die Funktion zurückgibt.
# Variablen können mit ///< direkt nach ihrer Deklaration kommentiert werden

# Dokumentation zu aktualisieren
# Dokumentation/html/index.html
# Dokumentation/latex/refman.pdf
doxygen Doxyfile
cd Dokumentation/latex/
make

# C
make
# make DEBUG=1 // für den Debug-Modus
# make DEBUG=0 // Release-Modus
# make clean
# make docs
# make quality
# make check_format

./run_tests.sh
npm test

brew update
brew install cppcheck doxygen clang-format
# latex
brew install --cask mactex
# Neustart des Terminals:
eval "$(/usr/libexec/path_helper)"
pdflatex --version

# Dateien zu Git-Repository hinzuzufügen
mkdir -p .github/workflows
vim .github/workflows/ci.yml
vim .github/workflows/nodejs.yml
vim .gitignore
vim Makefile
vim run_tests.sh
vim .clang-format

ls -a
git add package.json package-lock.json
git commit -m "Add package.json and package-lock.json"
git add .github/workflows/nodejs.yml .github/workflows/ci.yml
git commit -m "Add .github/workflows/nodejs.yml .github/workflows/ci.yml"
git add .gitignore Makefile run_tests.sh
git commit -m "Add .gitignore Makefile run_tests.sh"

git add .
git commit -m""
git push
```

**github/workflows/ci.yml**

```yaml
# .github/workflows/ci.yml
name: C/C++ CI on macOS

on: [push, pull_request]

jobs:
  build-and-test:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v2

      - name: Setup environment
        run: |
          brew update
          brew install cppcheck doxygen clang-format graphviz
          echo "/usr/local/Cellar/graphviz/$(ls /usr/local/Cellar/graphviz)/bin" >> $GITHUB_PATH

      - name: Build
        run: make

      - name: Run tests
        run: |
          chmod +x ./run_tests.sh
          ./run_tests.sh > test_results.txt
        shell: bash

      - name: Generate documentation
        run: doxygen Doxyfile

      - name: Code Quality Check
        run: cppcheck --enable=all --suppress=missingIncludeSystem $(find . -name '*.c')

      - name: Check Format
        run: |
          FILES=$(find . -name '*.c' -or -name '*.h')
          clang-format -i $FILES -style=file

      - name: Upload Test Results
        uses: actions/upload-artifact@v2
        with:
          name: test-results
          path: test_results.txt

      - name: Upload HTML Documentation
        uses: actions/upload-artifact@v2
        with:
          name: html-documentation
          path: Dokumentation/html/

      - name: Upload LaTeX Documentation
        uses: actions/upload-artifact@v2
        with:
          name: latex-documentation
          path: Dokumentation/latex/
```


**GitHub Actions Workflow für ein Node.js-Projekt**


```yaml
# GitHub Actions Workflow für ein Node.js-Projekt
# .github/workflows/nodejs.yml
name: Node.js Workflow

on: [push]

jobs:
  build:
    runs-on: macos-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm install

      - name: Run tests
        run: npm test
```

## Makefile

Der bereitgestellte Makefile ist für die Verwendung mit GitHub Actions konzipiert und bietet verschiedene Modi für die Kompilierung von C-Programmen, einschließlich Debug- und Release-Modi, sowie Ziele für die Bereinigung, Dokumentationserstellung, Code-Qualitätsprüfung und Formatüberprüfung.

### Grundkonfiguration und Modi

- `DEBUG ?= 1`: Setzt den Debug-Modus standardmäßig auf aktiv (`1`). Dies kann durch das Setzen der `DEBUG`-Variable beim Aufruf von `make` überschrieben werden.
- `CC = gcc`: Legt den Compiler auf GCC fest.
- `CFLAGS = -Wall -Wextra -std=c11`: Setzt grundlegende Compiler-Flags, darunter Warnungen und den C11-Standard.
- `LDFLAGS = -lm`: Linker-Flags, hier zum Linken der Mathematikbibliothek.

### Dateien und Ziele

- `SRCS = $(wildcard *.c)`: Findet alle `.c`-Dateien im aktuellen Verzeichnis.
- `TARGETS = $(SRCS:.c=)`: Generiert Namen für die ausführbaren Ziele basierend auf den `.c`-Dateinamen.

### Bedingte Kompilierung

- Basierend auf dem `DEBUG`-Flag werden zusätzliche Compiler-Flags hinzugefügt (`-g3` für Debugging, `-O2` für Optimierung im Release-Modus), und die Namen der Ziele werden entsprechend angepasst, um `Debug` oder `Release` zu enthalten.

### Regeln

- `all`: Das Hauptziel, das alle ausführbaren Dateien erstellt.
- `%Debug` und `%Release`: Musterregeln zum Erstellen der ausführbaren Dateien im Debug- bzw. Release-Modus.
- `clean`: Entfernt alle generierten Dateien, um eine saubere Arbeitsumgebung wiederherzustellen.
- `test`: Führt ein Testskript aus und speichert die Ergebnisse in `test_results.txt`.
- `docs`: Generiert Dokumentation mit Doxygen basierend auf der `Doxyfile`-Konfigurationsdatei.
- `quality`: Führt eine statische Code-Analyse mit `cppcheck` durch.
- `check_format`: Formatierung des Codes mit `vim .clang-format` gemäß den Stilvorgaben Google C++ Style Guide in der Konfigurationsdatei.

```bash
# .clang-format
# Google C++ Style Guide
# clang-format -i -style=file main.c
BasedOnStyle: Google
IndentWidth: 4
ColumnLimit: 80
AccessModifierOffset: -2
```

### Spezielle Ziele

- `.PHONY`: Gibt an, dass die nachfolgenden Ziele nicht physisch repräsentierte Dateien sind, sondern Aktionen darstellen.

### Verwendung

- Standardmäßige Kompilierung (Debug-Modus): `make`
- Release-Modus: `make DEBUG=0`
- Bereinigung: `make clean`
- Dokumentation: `make docs`
- Code-Qualitätsprüfung: `make quality`
- Formatüberprüfung: `make check_format`

```bash
brew update
brew upgrade
brew doctor
brew cleanup
brew install cppcheck doxygen clang-format bash graphviz
brew install --cask basictex  # LaTeX to PDF conversion
tlmgr update --self # Update TeX Live Manager
tlmgr install latexmk # Install latexmk for PDF generation
```

Dieser Makefile bietet eine flexible und automatisierte Methode, um Softwareprojekte zu kompilieren, zu testen und zu warten, was besonders nützlich in kontinuierlichen Integrationsumgebungen wie GitHub Actions ist.

```makefile
# Makefile für GitHub Actions mit Debug- und Release-Modus
# Verwendung:
# make
# make DEBUG=1 // für den Debug-Modus
# make DEBUG=0 // Release-Modus
# make clean
# make docs
# make quality
# make check_format

# Einstellung für Debug-Modus, standardmäßig auf 1 gesetzt
DEBUG ?= 1

# Compiler-Definition
CC = gcc
# Grundlegende Compiler Flags
CFLAGS = -Wall -Wextra -std=c11
# Linker Flags
LDFLAGS = -lm

# Findet alle .c-Dateien im Verzeichnis
SRCS = $(wildcard *.c)
# Erstellt eine Liste der ausführbaren Dateien, eine für jede .c-Datei
TARGETS = $(SRCS:.c=)

# Bedingte Einstellungen basierend auf dem DEBUG-Flag
ifeq ($(DEBUG), 1)
    CFLAGS += -g3
    TARGETS := $(addsuffix Debug, $(TARGETS))
else
    CFLAGS += -O2
    TARGETS := $(addsuffix Release, $(TARGETS))
endif

# Hauptziel
all: $(TARGETS)

# Regeln zum Erstellen der ausführbaren Programme
%Debug: %.c
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS)

%Release: %.c
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS)

# Clean up
clean:
	rm -f $(TARGETS) *Debug *Release
	rm -rf *.dSYM

# Test-Regel hinzugefügt, um das Testskript auszuführen
test: all
	./run_tests.sh > test_results.txt

docs:
	doxygen Doxyfile
	cd Dokumentation/latex/ && latexmk -pdf refman.tex
  latexmk -c && cd ../../

quality:
	cppcheck --enable=all --suppress=missingIncludeSystem $(SRCS)

check_format:
	clang-format -i $(SRCS) -style=file

# Spezielle Ziele, die keine Dateien sind
.PHONY: all clean test docs quality check_format
```

## Shell-Skript (run_tests.sh)


Das Skript `run_tests.sh` ist ein Bash-Skript, das für das automatisierte Testen von C-Programmen konzipiert ist. Es kompiliert die Programme mit `make`, führt eine Liste von Testprogrammen aus und prüft, ob diese erfolgreich abgeschlossen wurden.

1. **Start des Testprozesses**: Das Skript beginnt mit einer Ausgabe, die den Beginn des Testprozesses anzeigt.

2. **Initialisierung des Exit-Codes**: Es wird eine Variable `exit_code` mit dem Wert `0` initialisiert. Diese Variable dient als Indikator dafür, ob alle Tests erfolgreich waren oder ob Fehler aufgetreten sind.

3. **Kompilierung der Programme**: Das Skript versucht, die Programme mit dem `make`-Befehl zu kompilieren. Wenn die Kompilierung fehlschlägt (`make` gibt einen non-zero Exit-Code zurück), gibt das Skript eine Fehlermeldung aus und beendet sich mit Exit-Code `1`.

4. **Testprogramme und Eingaben**: Es definiert zwei Arrays: `tests` enthält die Namen der Testprogramme, und `inputs` enthält die entsprechenden Eingaben für diese Tests. Jedes Testprogramm wird mit der zugehörigen Eingabe ausgeführt.

5. **Ausführung der Testprogramme**: Das Skript durchläuft jedes Testprogramm in einer Schleife. Für jedes Programm wird die entsprechende Eingabe angezeigt und dann mittels Pipe an das Programm übergeben. Falls kein spezifischer Input erforderlich ist, wird das Programm ohne Eingabe ausgeführt.

6. **Prüfung des Testergebnisses**: Nach der Ausführung jedes Testprogramms prüft das Skript den Exit-Code des Programms. Wenn dieser `0` ist, gilt der Test als erfolgreich, andernfalls als fehlgeschlagen. Der `exit_code` des Skripts wird auf `1` gesetzt, wenn mindestens ein Test fehlschlägt.

7. **Abschluss**: Am Ende des Skripts wird basierend auf dem `exit_code` eine Zusammenfassung ausgegeben. Sind alle Tests erfolgreich, wird eine entsprechende Meldung angezeigt; bei Fehlern wird darauf hingewiesen, dass einige Tests fehlgeschlagen sind.

8. **Beendigung des Skripts**: Das Skript beendet sich mit dem `exit_code`, der den Erfolg der Tests widerspiegelt. Ein `exit_code` von `0` bedeutet, dass alle Tests erfolgreich waren, während `1` auf Fehler hinweist.


```bash
# run_tests.sh
# chmod +x run_tests.sh
#!/bin/bash

echo "Beginne Testprozess..."

# Initialisiere Exit-Code
exit_code=0

# Kompilieren der Programme, wenn nötig
if ! make; then
    echo "Kompilierung fehlgeschlagen."
    exit 1
fi

# Liste der Testprogramme
tests=("rechteck_berechnung_v1Debug" "rechteck_berechnung_v2Debug")

# Eingabe für jeden Test - Achte darauf, dass die Eingaben den Anforderungen entsprechen
inputs=("2.0\n3.0" "2.0\n3.0") # Beide Eingaben als positive Dezimalzahlen

# Durchlaufe alle Testprogramme
for i in "${!tests[@]}"; do
    test=${tests[$i]}
    input=${inputs[$i]}
    echo "Starte Test für: $test..."
    # Ausgabe der Eingabe zur Überprüfung
    echo -e "Eingabe, die an das Programm weitergeleitet wird:\n$input"

    # Verwende printf statt echo -e für konsistentere Handhabung der Eingaben
    printf "$input" | ./$test

    # Überprüfung des Exit-Codes des zuletzt ausgeführten Befehls
    if [ $? -eq 0 ]; then
        echo "$test erfolgreich abgeschlossen."
    else
        echo "FEHLER in $test."
        exit_code=1
    fi
    echo "-----------------------------------"
done

# Generiere PDF aus LaTeX, wenn alle Tests erfolgreich waren
if [ $exit_code -eq 0 ]; then
    echo "Beginne mit der Erstellung der PDF-Dokumentation..."

    # Wechsle ins Verzeichnis der LaTeX-Quellen
    cd Dokumentation/latex/

    # Führe make aus, um die PDF zu erstellen
    if ! make; then
        echo "Erstellung der PDF-Dokumentation fehlgeschlagen."
        exit_code=1
    else
        echo "PDF-Dokumentation erfolgreich erstellt."
    fi

    # Zurück zum ursprünglichen Verzeichnis
    cd -
fi

# Gib den Gesamt-Exit-Code zurück
if [ $exit_code -eq 0 ]; then
    echo "Alle Tests und die Erstellung der Dokumentation erfolgreich abgeschlossen."
else
    echo "Einige Tests oder die Erstellung der Dokumentation sind fehlgeschlagen."
fi

exit $exit_code
```


## Projekt: C-Programmierung mit Git-Versionierung

**Git-Versionierung und Collaboration**

- Anlegen von Verzeichnissen für Beispiele, Projekte, Dokumentation und Tutorials.
- Erstellung und Push von Änderungen über Feature-Branches.
- Pull Requests zur Integration neuer Features in den main-Branch.
- Nutzung von gh pr create zur Erstellung von Pull Requests und gh issue create zur Meldung von Bugs.

#### Schritt 1: Einrichten des Projekts

1. **Repository klonen**
   ```bash
        # Konfigurieren von Git
        # git config --global user.name "Ihr Name"
        # git config --global user.email "ihre.email@example.com"

   gh repo list
   gh repo clone ju1-eu/hello-world
   cd hello-world
   mkdir Beispiele Projekte Dokumentation Tutorials
   ```

#### Schritt 2: Arbeiten mit Branches

1. **Neuen Feature-Branch erstellen**:
   ```bash
   git branch -a
   # Branch bereits im Remote-Repository existiert
   git checkout -b feature-coole-neuerung origin/feature-coole-neuerung
   # Beginn
   git checkout -b feature-coole-neuerung
   git push --set-upstream origin feature-coole-neuerung
   ```

2. **Änderungen implementieren und committen**:
    - Änderungen hinzufügen und committen:
    ```bash
    #--------------------------------------------------
    # Entwicklung starten
    vim hallo-welt.c
    #--------------------------------------------------
    git add .
    git commit -m "Neues cooles Feature hinzugefügt"
    git push origin feature-coole-neuerung
    ```

#### Schritt 3: Pull Request erstellen

**Pull Request erstellen** mit `gh`:

```bash
gh pr create --base main --title "Neues cooles Feature" --body "Hier ist eine detaillierte Beschreibung des neuen Features."
# Feedback vor der finalen Überprüfung erhalten
gh pr create --base main --head feature-coole-neuerung --title "Neue coole Funktion" --body "Fügt eine neue coole Funktion hinzu, die XYZ verbessert." --reviewer ju1-eu
```

#### Schritt 4: Interaktion und Collaboration

**Git Labels**

- **bug** Etwas funktioniert nicht
- **documentation** Verbesserungen oder Ergänzungen der Dokumentation
- **duplicate** Dieses Problem oder diese Pull-Anfrage existiert bereits
- **enhancement** Neue Funktion oder Anfrage
- **good first issue** Gut für Neueinsteiger
- **help wanted** Besondere Aufmerksamkeit ist erforderlich
- **invalid** Das scheint nicht richtig zu sein
- **question** Weitere Informationen werden erbeten
- **wontfix** Daran wird nicht gearbeitet

1. **Issue erstellen**, um einen gefundenen Bug zu melden:
   ```bash
        # gh issue --help
   # Issue erstellen
   gh issue create --title "Titel des Issues" --body "Beschreibung des Issues"
   # Issue bearbeiten:
   gh issue list
   gh issue edit 8 --title "Neuer Titel" --add-label "good first issue"

   gh issue create --title "Bug gefunden" --body "Beschreibung des Bugs..." --assignee @me --label bug
   gh issue list
   gh issue status
        # Issues assigned to you: die Ihnen zugewiesen sind.
        # Issues mentioning you: die Sie erwähnen.
        # Issues opened by you: die von Ihnen eröffnet wurden.
   gh issue view 9

   # Issue schließen:
   gh issue close 9

   # Meilenstein erstellen
   gh api \
       --method POST \
       -H "Accept: application/vnd.github+json" \
       -H "X-GitHub-Api-Version: 2022-11-28" \
       /repos/ju1-eu/hello-world/milestones \
       -f title='Meilenstein 1' \
   -f state='open' \
   -f description='Tracking milestone for version 1.1' \
   -f due_on='2024-03-09T23:39:01Z'

   # Issues einem Meilenstein zuordnen
   # Issue-Nummer
   gh issue list
   gh issue edit 8 --milestone "Meilenstein 1"

   # Issue-Nummer
   gh issue list
   gh issue close 8

   # Meilenstein listen
   # Milestone-Nummer "number": 1
   gh api \
       -H "Accept: application/vnd.github+json" \
       -H "X-GitHub-Api-Version: 2022-11-28" \
       /repos/ju1-eu/hello-world/milestones

   # Meilenstein löschen
   # Milestone-Nummer "number": 1
   gh api \
       --method DELETE \
       -H "Accept: application/vnd.github+json" \
       -H "X-GitHub-Api-Version: 2022-11-28" \
       /repos/ju1-eu/hello-world/milestones/1
    ```

2. **Selbstüberprüfung und auf Pull Requests reagieren**:
   - Nehmen Sie sich Zeit, um offene Pull Requests zu überprüfen und konstruktives Feedback zu hinterlassen.
   ```bash
   gh pr status
   gh pr list
   gh pr view 10
   # Anfordern von Reviews
   gh pr create --reviewer ju1-eu

   # Status:
        # Checks pending: Es warten noch Status-Checks (wie Continuous Integration Tests), die durchgeführt und bestanden werden müssen, bevor der Pull Request weiter bearbeitet oder gemerged werden kann.
        # Review required: Es wird mindestens eine Code-Überprüfung (Review) benötigt, bevor der Pull Request gemerged werden kann.

   # Änderungen vorgenommen und erneute Überprüfung bitten
   # gh pr review 10 --comment --body "Meine Kommentare..."
   gh pr review 10 --comment --body "Ich habe die Änderungen vorgenommen. Bitte überprüfen Sie erneut, wenn Sie Zeit haben. Danke!
   "

   # Genehmigen des Pull Requests des aktuellen Branches
   # Branch-Schutzregeln auf GitHub
   gh pr review --approve
   ```

3. **Hauptbranch und Merging** (Feature ist fertig und getestet):
   ```bash
   # ANPASSEN
   git checkout main
   gh pr list
   gh pr status
   # Projekt-Maintainer
   gh pr merge 10 --squash --delete-branch

   # PR aus dem Entwurfsstatus zu entfernen: Schaltfläche suchen: Ready for review
   # github: https://github.com/ju1-eu/hello-world/pull/10
   #git pull origin main
   #git checkout main
   #git merge feature-coole-neuerung
   #git push -u origin main

   # Aufräumen
   git branch -a
   git remote -v
   # lokalen Referenzen sauber halten
   git fetch --prune
   #git branch -d feature-coole-neuerung
   #git push origin --delete feature-coole-neuerung

   git pull
   git push
   git status
   git lg
   ```

#### Schritt 5: GitHub Actions für C und Node.js

- Zwei separate Workflows für C- und Node.js-Projekte automatisieren die Testausführung.
- Workflows werden durch Pushes oder Pull Requests auf den main-Branch ausgelöst.


**GitHub Actions Workflow**

- Automatisiert Kompilierung und Tests für C-Programme bei jedem Push oder Pull Request zum main-Branch.
- Workflow-Definition in .github/workflows/ci.yml und .github/workflows/nodejs.yml.

- Nutzt macOS-Runner für C-Programme und Ubuntu-Latest-Runner für Node.js-Projekte.

**Node.js-Projektinitialisierung**

- Befehle node -v und npm -v zeigen die installierten Versionen.
- npm init startet ein neues Node.js-Projekt.
- Node.js und npm werden aktualisiert (nvm install 20, nvm use 20, npm install -g npm@10.2.4).

**Abhängigkeiten und Tests**

- npm install installiert definierte Abhängigkeiten in package.json.
- npm test führt definierte Tests aus, einschließlich Kompilierung von C-Programmen und Ausführung des run_tests.sh Skripts.

**Was bedeutet das für Ihr Projekt?**

- **Funktionalität**: Ihre C-Programme arbeiten korrekt und liefern die erwarteten Ergebnisse. Dies ist ein gutes Zeichen für die Grundfunktionalität Ihres Projekts.
- **Automatisierung**: Die Einrichtung der Testautomatisierung über `npm test` ist erfolgreich. Dies erleichtert das kontinuierliche Testen Ihres Projekts während der Entwicklung und hilft, Fehler frühzeitig zu erkennen.
- **Workflow**: Sie haben einen effektiven Workflow für die Ausführung von Tests eingerichtet, der leicht reproduzierbar ist und sich gut in CI/CD-Pipelines integrieren lässt.

**Nächste Schritte**

- **Weiterentwicklung**: Sie können nun mit der Weiterentwicklung Ihres Projekts fortfahren, neue Features hinzufügen und sicher sein, dass Sie eine solide Basis für das Testen Ihrer Änderungen haben.
- **Erweiterte Tests**: Erwägen Sie, erweiterte Testfälle und vielleicht sogar automatisierte Unit-Tests für komplexere Logik in Ihren Programmen zu schreiben.
- **CI/CD-Integration**: Wenn Sie noch nicht damit begonnen haben, könnten Sie überlegen, Ihren Workflow in eine CI/CD-Pipeline zu integrieren, um Ihre Tests bei jedem Push zu einem Repository oder bei der Erstellung eines Pull Requests automatisch auszuführen.
- **Dokumentation**: Stellen Sie sicher, dass Sie eine klare Dokumentation für Ihr Projekt haben, insbesondere wenn es wächst. Dies umfasst die Dokumentation des Codes selbst sowie Anleitungen für das Setup, die Konfiguration und die Verwendung Ihres Projekts.


