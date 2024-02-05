---
title: "Workflow"
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!-----------------------------------------------------------------------
ju 5-2-24 Workflow.md
pandoc Workflow.md -o Workflow.html -c inhalt.css --mathjax
------------------------------------------------------------------------->

# Workflow - 5x Schritte

1. **Entwicklung** Makefile für C
2. **Debugging** gdb oder lldb
3. **Optimierung** ChatGPT
4. **Dokumentation** Pythonscripte => Latex & HTML, Makefile für Latex
5. **Versionierung** Git & GitHub

## Entwicklung

ChatGPT <https://chat.openai.com/?model=gpt-4>

- **Prompt:** Erstelle mir den Code in C

```bash
make
make DEBUG=1 # Debug-Modus = make
make DEBUG=0 # Release-Modus
make clean
```

### Makefile

```bash
# Verwendung:
# make
# make DEBUG=1 // für den Debug-Modus
# make DEBUG=0 // Release-Modus
# make clean

# Einstellung für Debug-Modus, standardmäßig auf 1 gesetzt
DEBUG ?= 1

# Compiler-Definition
CC = gcc
# Grundlegende Compiler Flags
CFLAGS = -Wall -Wextra -std=c11
# Linker Flags
LDFLAGS = -lm

# Findet alle .c-Dateien im Verzeichnis
SOURCES = $(wildcard *.c)
# Erstellt eine Liste der ausführbaren Dateien, eine für jede .c-Datei
EXECUTABLES = $(SOURCES:.c=)

# Bedingte Einstellungen basierend auf dem DEBUG-Flag
ifeq ($(DEBUG), 1)
    CFLAGS += -g3
    EXECUTABLES := $(addsuffix Debug, $(EXECUTABLES))
else
    CFLAGS += -O2
    EXECUTABLES := $(addsuffix Release, $(EXECUTABLES))
endif

# Hauptziel
all: $(EXECUTABLES)

# Regeln zum Erstellen der ausführbaren Programme
%Debug: %.c
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS)

%Release: %.c
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS)

# Clean up
clean:
	rm -f $(EXECUTABLES)
	rm -f *Debug *Release
	rm -rf *.dSYM


# Spezielle Ziele, die keine Dateien sind
.PHONY: all clean
```

## Testen und Debugging

1. **LLDB starten mit dem Programm**:
   ```bash
   lldb ./dateiDebug
   ```

2. **Breakpoint setzen**:
   ```lldb
   list
   b <Zeilennummer>
   ```
   Zum Beispiel, um einen Breakpoint in Zeile 32 zu setzen:
   ```lldb
   b 32
   ```
3. **Programm ausführen**:
   ```lldb
   run
   ```
   Startet das Programm innerhalb des Debuggers.

4. **Überprüfen von Variablenwerten**:
   Nachdem das Programm am Breakpoint angehalten hat:
   ```lldb
   frame variable <Variablenname>
   ```
   Beispiel:
   ```lldb
   frame variable floatResult
   frame variable doubleResult
   frame variable longDoubleResult
   ```

5. **Nächste Zeile ausführen**:
   ```lldb
   next
   ```
   Führt die nächste Zeile des Codes aus und bleibt im gleichen Funktionskontext.

6. **Fortsetzen der Ausführung bis zum nächsten Breakpoint**:
   ```lldb
   continue
   ```
   Setzt die Ausführung des Programms fort.

7. **LLDB beenden**:
   ```lldb
   quit
   ```

### Zusätzliche hilfreiche Befehle

- **Liste der Breakpoints anzeigen**:
  ```lldb
  breakpoint list
  ```
  Zeigt alle gesetzten Breakpoints an.

- **Informationen über den aktuellen Thread**:
  ```lldb
  thread list
  ```
  Listet alle Threads auf und zeigt den aktuellen Thread an.

- **Code um den aktuellen Punkt anzeigen**:
  ```lldb
  list
  ```
  Zeigt den Quellcode um die aktuelle Zeile herum an.

- **Zurückverfolgung des Aufrufstacks**:
  ```lldb
  bt
  ```
  Zeigt den Stack-Trace des aktuellen Threads an.

## Optimierung

ChatGPT <https://chat.openai.com/?model=gpt-4>

-  Prüfe und optimiere


## Dokumentation


**ChatGPT** <https://chat.openai.com/?model=gpt-4>

- Verwende den **Schreibstil**: Expositorisch ohne Form du/sie. **Datum** im internationalen Format: "Jahr-Monat-Tag"

- Erstelle eine **Beschreibung zum Quellcode**

- Erstelle eine **README.md**

- Erstelle eine **Entwickler-Info im Code**, um wichtige Informationen und Anweisungen für die Nutzung des Scripts bereitzustellen.

- Erstelle eine **strukturierte Dokumentation** für das Projekt.

- **Zusammenfassung**
  ```
  Thema: C - Programmierung
  Verwende GitHub-Flavored Markdown
  Schreibstil: Expositorisch ohne Form du/sie
  Erstelle je nach Schreibstil eine ansprechende Zusammenfassung zum Lerninhalt in Aufzählungsform und gleichzeitig gebe   die wichtigsten Informationen (Didaktische Reduktion) genau wieder. Bereite die Antwort gehirngerecht auf.

  Lerninhalt: " "
  ```


- **Keywords:** Erstelle mir eine Liste mit Keywords und Beispielen.

- **Fragen:** Erstelle 5x Fragen zum Lerninhalt (beachte den Focus: tieferes Verständnis und kritisches Denken zu fördern) mit Lösung.

- **Projekt:** Erstelle ein Projekt zum Anwenden des gelernten mit Lösung.


### Notizen in Latex und HTML

```bash
# Workflow.md
# Konvertierung .png und .HEIC => .pdf und .webp
python ImageResizer.py

# Konvertierung .md => Latex und HTML
python scriptauswahl.py

# Latex manuell kompilieren
xelatex neu
xelatex neu
```

### MIT-Lizenz

MIT License

Copyright (c) 2023 Jan Unger

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



## Git-Versionierung

**Git Aliases**

```bash
st = status
cl = clone
c = commit -m
cam = commit -am
ca = commit --amend
co = checkout
br = branch -a
brm = branch --merged
r = reset
lg = log --oneline --graph --decorate
lo = log --oneline --decorate
ls = log --pretty=format:"%C(green)%h\\ %C(yellow)[%ad]%Cred%d\\ %Creset%s%Cblue\\ [%an]" --decorate --date=relative
ll = log --pretty=format:"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [a:%an,c:%cn]" --decorate --numstat
d = diff --word-diff
dc = diff --cached
```


### Schritt 1: Initialisierung des Git-Repositories

```bash
# Git Konfigurationsdatei
vim .git/config
vim ~/.gitconfig

git config --local --list
git config --global --list
git config user.name

# Projektverzeichnis betreten
cd /Users/jan/daten/start/Programmierung/JanSchaffranek/C-Programmierung/c-projekte

# .gitignore erstellen und konfigurieren
# GitHub Vorlagen: https://github.com/github/gitignore/blob/main/C.gitignore
touch .gitignore

# Git-Repository initialisieren
# rm -rf .git
git init
```

### Schritt 2: Erste Dateien hinzufügen und commiten

```bash
# Dateien zum Staging-Bereich hinzufügen
git add .
# Dateien commiten
git commit -m "Initial commit"
```

### Schritt 3: Branches verwalten

```bash
# Neuen Branch für die Entwicklung erstellen
git branch dev
git checkout dev
# oder: git checkout -b dev
```

### Schritt 4: Änderungen verwalten

```bash
# Status der Änderungen überprüfen
git status

# Geänderte Dateien zum Staging-Bereich hinzufügen und commiten
git add <Dateiname>
git commit -m "Beschreibung der Änderungen"
```

### Schritt 5: Änderungen zusammenführen

```bash
# Zum Hauptbranch wechseln und Änderungen zusammenführen
git checkout main
git merge dev
```

### Schritt 6: Remote-Repository hinzufügen (auf dem Mac)

```bash
# Bare Git-Repository lokal auf dem Mac erstellen
# Git-Repository Verzeichnis
cd /Users/jan/daten/start
git init --bare c-projekt.git
git init --bare notizen_latex_html_python_v1

# Remote-Repository verwenden
# Projekt Verzeichnis
cd /Users/jan/daten/start/Programmierung/JanSchaffranek/C-Programmierung/c-projekte
git remote add origin /Users/jan/daten/start/c-projekt.git
cd /Users/jan/daten/latex/notizen_latex_html_python_v1
git remote add origin /Users/jan/daten/start/notizen_latex_html_python_v1

# Lokalen Branch umbenennen
#git branch -m master main
# Neuen Branch 'main' auf Remote-Repository pushen und als Upstream setzen
git remote -v
#git remote set-url origin <korrekte-URL>
#git pull origin main
git push -u origin main
git pull
git push
```

### Schritt 7: Branches synchron halten

#### Synchronisation vom Hauptbranch zum Entwicklungszweig

```bash
# Anzeigen des aktuellen Branch-Status
git lg
# Wechseln zum Hauptbranch und Aktualisieren
git checkout main
git lg
################################################
# CODE bearbeiten
################################################
git st
git add .
git commit -m "Beschreibung"

git pull
git push

# wechseln zum Entwicklungszweig und Zusammenführen der Änderungen aus main
git checkout dev
git merge main

# Änderungen im Hauptbranch zum Remote-Repository pushen
# git push -u origin dev
# Tracking-Informationen für den Branch setzen
# git branch --set-upstream-to=origin/dev dev
git st
git pull
git push

git lg
    * 0dfad45 (HEAD -> dev, origin/main, origin/dev, main) Git Workflow überarbeitet
    * 4b6a496 main
    * 4a153f9 Doku
    * 677d4fd gitignore
    * edbdc2b Workflow beschreiben
    * e64d046 Initial commit
```

#### Synchronisation vom Entwicklungszweig zum Hauptbranch

```bash
# Wechseln zum Entwicklungszweig
git checkout dev
git lg
################################################
# CODE bearbeiten
################################################
git st
git add .
git commit -m "Beschreibung"

# Nur beim ersten Mal:
# Erstellen und Pushen des Remote-Branches
# git push -u origin dev
# Tracking-Informationen für den Branch setzen
# git branch --set-upstream-to=origin/dev dev
git pull
git push

# Wechseln zum Hauptbranch und Zusammenführen der Änderungen aus dev
git checkout main
git merge dev

# Änderungen im Hauptbranch zum Remote-Repository pushen
git st
git pull
git push

git lg
    * 4a153f9 (HEAD -> main, origin/main, origin/dev, dev) Doku
    * 677d4fd gitignore
    * edbdc2b Workflow beschreiben
    * e64d046 Initial commit
```

### git clone

```bash
# git clone
git clone https://github.com/ju1-eu/hello-world.git
git clone /Users/jan/daten/start/c-projekt.git
git clone /Users/jan/daten/start/notizen_latex_html_python_v1
```


### GitHub

```bash
git clone https://github.com/ju1-eu/hello-world.git
cd hello-world
```

```bash
# Entwickeln auf Feature-Branches
# Dokumentationsupdates auf docs/update-readme
# Erstellen eines Branches für Dokumentationsupdates:
git branch -a
git log --oneline --graph --all
git checkout dev
git checkout -b docs/update-readme

# Durchführen von Änderungen an der Dokumentation:
vim README.md
vim .gitignore
git add .
git commit -m "Update README und .gitignore mit neuen Informationen"
git status

# Pushen des Dokumentationsbranches:
git push --set-upstream origin docs/update-readme

# Erstellen eines Pull Requests von `dev` nach `main`
# Mergen des Dokumentationsbranches in `dev`:
git checkout dev
git pull origin main
git merge docs/update-readme
git push origin dev

# Erstellen des Pull Requests von `dev` nach `main`:
gh pr create --base main --head dev --title "Aktualisierung der Dokumentation" --body "Fügt detaillierte Informationen zur README hinzu."

# Merge des Pull Requests:
# Liste aller offenen Pull Requests anzeigen [PR-Nummer]
gh pr list
gh pr view 2
#gh pr view 2 --web
# Code-Review durchführen
# Genehmigen eines Pull Requests
gh pr review 2 --approve
# PR ablehnen
#gh pr review 2 --request-changes "Bitte Code überprüfen"
gh pr merge 2
gh pr view 2
# Löschen des Feature-Branches:
git branch -d docs/update-readme
git push origin --delete docs/update-readme
git branch -a
git log --oneline --graph --all

# Regelmäßige Updates und Synchronisation
git checkout main
git pull origin main
git checkout dev
git push origin dev
git merge main
git branch -a
git log --oneline --graph --all
```

### GitHub-Repository und Pull Requests

1. **Neues Repository auf GitHub erstellen:**
   - Gehen Sie auf [GitHub](https://github.com) und erstellen Sie ein neues Repository. Für Ihre Anforderungen verwenden Sie `https://github.com/ju1-eu/c-projekt.git` als Repository-URL.

2. **Repository lokal klonen:**
   - Öffnen Sie das Terminal auf Ihrem Mac.
   - Verwenden Sie den Befehl `git clone https://github.com/ju1-eu/c-projekt.git`, um das Repository zu klonen.

3. **Änderungen vornehmen und hochladen:**
   - Nehmen Sie Änderungen vor und führen Sie `git add .` aus, um die Änderungen zum Staging-Bereich hinzuzufügen.
   - Commiten Sie die Änderungen mit `git commit -m "Ihre Nachricht"`.
   - Pushen Sie die Änderungen mit `git push origin main`.

4. **Branches erstellen und verwalten:**
   - Erstellen Sie einen neuen Branch mit `git checkout -b <branch-name>` und pushen Sie ihn mit `git push origin <branch-name>`.

5. **Pull Requests erstellen und mergen:**
   - Erstellen Sie auf GitHub einen Pull Request für Ihren Branch.
   - Überprüfen Sie den Pull Request und mergen Sie ihn, wenn alles in Ordnung ist.

Diese Schritte ermöglichen Ihnen die effektive Erstellung, Verwaltung und Kollaboration in einem GitHub-Repository.

# Projektname

Eine kurze Beschreibung Ihres Projekts. Dies sollte das Hauptziel und den Zweck Ihres Projekts klar umreißen.

## Einleitung

Geben Sie eine detailliertere Beschreibung Ihres Projekts. Erklären Sie, was dieses Projekt macht und warum es nützlich ist.

## Git

```bash
git clone https://github.com/ju1-eu/hello-world.git
cd hello-world
```

## Verwendung


## Mitwirken

Pull Requests sind willkommen. Für größere Änderungen öffnen Sie bitte zuerst ein Issue, um zu besprechen, was Sie ändern möchten.


## Lizenz

[MIT](https://choosealicense.com/licenses/mit/)


## Kontakt

Jan Unger – [Website](https://bw-ju.de/) – esel573@gmail.com

Projektlink: <https://github.com/ju1-eu/hello-world>
