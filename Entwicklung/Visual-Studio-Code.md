---
title: "Visual-Studio-Code"
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!-----------------------------------------------------------------------
ju 9-2-24 Visual-Studio-Code.md
pandoc Visual-Studio-Code.md -o Visual-Studio-Code.html -c inhalt.css --mathjax
------------------------------------------------------------------------->
## Visual-Studio-Code

<https://chat.openai.com/>

Prompt: Die Struktur des Dokuments ändern (z.B. die Reihenfolge der Abschnitte optimieren, um den Lesefluss zu verbessern)?
und Markdown-Stilrichtlinien überprüfen

Prompt: erstelle mir ein beispiel Lernen und Lehren:
Bildungsressourcen: Die Flexibilität und Zugänglichkeit von Jupyter Notebooks machen sie zu einem beliebten Werkzeug in der Bildung, insbesondere in den Bereichen Data Science und maschinelles Lernen. Lehrkräfte nutzen Notebooks, um komplexe Konzepte zu vermitteln, während Studierende sie für praktische Übungen und Projekte verwenden.

Neue Struktur des Dokuments

1. **Einführung**
   - Kurze Einführung in Visual Studio Code und den Zweck des Dokuments.

2. **Installation von Visual Studio Code**
   - Schritte zur Installation von VS Code auf macOS.
   - Hinweis zur Installation des Shell-Befehls (`code`) im PATH.

3. **Erste Schritte mit VS Code**
   - Öffnen von Projekten.
   - Übersicht über die Benutzeroberfläche.
   - Nutzung der Kommando-Palette.

4. **Erweiterungen installieren und verwalten**
   - Erläuterung des Extensions-Views.
   - Anleitung zur Installation der wichtigsten Erweiterungen für verschiedene Entwicklungsumgebungen:
     - Webentwicklung (HTML, CSS, JavaScript).
     - Python-Entwicklung.
     - C/C++ Entwicklung.
     - LaTeX-Dokumenterstellung.
     - Arduino und ESP32-Programmierung.
   - Hinweis auf die automatische Installation mittels eines Skripts.

5. **Konfiguration von VS Code**
   - Anpassung der `settings.json` für eine optimierte Entwicklungsumgebung.
   - Spezifische Konfigurationen für:
     - Python.
     - C/C++ (inkl. Google's C++ Code Style).
     - LaTeX.
     - Webentwicklung.
   - Hinweis auf die Bedeutung von `.clang-format` und anderen Konfigurationsdateien.

6. **Nutzung von Git und GitHub**
   - Installation und Konfiguration der Git-bezogenen Erweiterungen (GitLens, Git Graph, Git History).
   - Verwaltung von GitHub Pull Requests und Issues.

7. **Markdown-Unterstützung**
   - Verwendung von Markdown All in One und Markdown Preview Enhanced für die Bearbeitung von Markdown-Dokumenten.
   - Linting und Konvertierung von Markdown zu PDF.

8. **Tipps und Tricks**
   - Nützliche Tipps zur Steigerung der Produktivität in VS Code.
   - Empfehlungen für Shortcuts und unbekannte Features.

9. **Häufig gestellte Fragen (FAQ)**
   - Antworten auf häufig gestellte Fragen zur Nutzung von VS Code.

10. **Ressourcen und weiterführende Links**
    - Offizielle Dokumentation und Tutorials.
    - Community-Ressourcen und Foren.

11. **Anhang**
    - Detaillierte Schritte zur Deinstallation von VS Code und zur Sicherung von Konfigurationen.
    - Skriptbeispiele zur Automatisierung von Routinetasks.

## Visual Studio Code entfernen

Um Visual Studio Code (VS Code) auf einem macOS zu entfernen und dabei Ihre `settings.json` zu sichern.

### Schritt 1: Sichern der settings.json

1. **Öffnen Sie Finder** und navigieren Sie zu Ihrem Benutzerordner.
2. **Gehen Sie zu** `Library/Application Support/Code/User/`. Der `Library`-Ordner könnte versteckt sein. Um versteckte Ordner anzuzeigen, drücken Sie `Cmd + Shift + .` im Finder.
3. **Kopiere** `settings.json` auf Ihren Desktop oder einen anderen sicheren Ort. Sie können dies tun, indem Sie die Datei auswählen, `Cmd + C` drücken, um sie zu kopieren, und dann zum gewünschten Zielort navigieren und `Cmd + V` drücken, um sie einzufügen.

### Schritt 2: Deinstallieren von VS Code

1. **Öffnen Sie Finder** und gehen Sie zum `Applications`-Ordner.
2. **Suchen Sie Visual Studio Code** und ziehen Sie das Symbol in den Papierkorb oder klicken Sie mit der rechten Maustaste darauf und wählen Sie `In den Papierkorb legen`.
3. **Leeren Sie den Papierkorb**, um den Deinstallationsprozess abzuschließen.

### Schritt 3: Löschen zugehöriger Daten (optional)

```bash
rm -rf ~/Library/Application\ Support/Code
rm -rf ~/.vscode
```

### code im PATH installieren

- Öffnen Sie VS Code.
- Öffnen Sie die Kommando-Palette mit Cmd+Shift+P auf macOS.
- Geben Sie Shell-Befehl in die Kommando-Palette ein und wählen Sie dann den Eintrag Shell-Befehl: 'code' im PATH installieren

<https://code.visualstudio.com/docs/setup/mac>

```bash
brew install clang-format
clang-format -style=google -dump-config > .clang-format
clang-format -i Regelungstechnik.ino
find . -iname *.h -o -iname *.ino | xargs clang-format -i


pip install --upgrade pip
pip install ipykernel    

# Script VS-Code anpassen
python install_vscode_extensions.py

# Liste der Erweiterungs-IDs mit Beschreibungen
# ERGÄNZEN ....................................
# PlatformIO IDE 
# PyMakr
extensions = {
   "ban.spellright": "Spell Right ist eine Rechtschreibprüfungserweiterung.",
   "ritwickdey.LiveServer": "Ermöglicht Live-Vorschau von Webseiten direkt im Browser.",
   "dbaeumer.vscode-eslint": "Integriert ESLint für JavaScript Linting.",
   "esbenp.prettier-vscode": "Code-Formatter für verschiedene Sprachen.",
   "ms-python.python": "Umfassende Unterstützung für Python-Entwicklung.",
   "ms-toolsai.jupyter": "Erstellung und Bearbeitung von Jupyter Notebooks.",
   "ms-python.vscode-pylance": "Erweiterte Python-Sprachunterstützung.",
   "ms-vscode.cpptools": "Unterstützung für C/C++ Entwicklung.",
   "ms-vscode.cmake-tools": "Unterstützung für CMake in VS Code.",
   "xaver.clang-format": "Automatische Formatierung von C/C++ Code.",
   "vsciot-vscode.vscode-arduino": "Unterstützung für Arduino-Entwicklung.",
   "ecmel.vscode-html-css": "Autovervollständigung für CSS-Klassen in HTML.",
   "bmewburn.vscode-intelephense-client": "PHP IntelliSense.",
   "James-Yu.latex-workshop": "Unterstützung für das Schreiben von LaTeX-Dokumenten.",
   "eamodio.gitlens": "Erweiterte Git-Integration und -Funktionalität.",
   "GitHub.vscode-pull-request-github": "Verwaltung von GitHub Pull Requests und Issues.",
   "yzhang.markdown-all-in-one": "Alles-in-einem Markdown-Unterstützung.",
   "shd101wyy.markdown-preview-enhanced": "Erweiterte Markdown-Vorschau.",
   "felixfbecker.php-debug": "PHP Debugging mit XDebug; ermöglicht das Debuggen von PHP-Code.",
   "xabikos.JavaScriptSnippets": "Sammlung von JavaScript (ES6)-Snippets für beschleunigte Entwicklung.",
   "ajshort.include-autocomplete": "Automatische Vervollständigung für #include-Anweisungen in C/C++.",
   "njpwerner.autodocstring": "Generiert automatisch detaillierte Docstrings für Python-Funktionen.",
   "DavidAnson.vscode-markdownlint": "Linting für Markdown-Dateien zur Sicherstellung von Konsistenz und Sauberkeit.",
   "yzane.markdown-pdf": "Konvertiert Markdown-Dateien in PDF, was die Verteilung und Präsentation vereinfacht.",
   "bierner.markdown-checkbox": "Unterstützung für interaktive Checkboxes in Markdown-Dokumenten.",
   "mhutchie.git-graph": "Visualisiert den Git-Verlauf als Graph, um die Repository-Historie zu veranschaulichen.",
   "DonJayamanne.githistory": "Ermöglicht die Anzeige der Git-Commit-Historie, einschließlich der Änderungen an Dateien.",
   "shaharkazaz.git-merger": "Vereinfacht den Git-Merge- und Rebase-Prozess innerhalb von VS Code.",
   "waderyan.gitblame": "Zeigt in der Statusleiste an, wer bestimmte Zeilen eines Files geändert hat."
}
```

```bash
# versteckte Ordner anzuzeigen, Cmd + Shift + . im Finder.
# /Users/jan/Library/Application Support/Code/User/settings.json
# vim .vscode/settings.json
# Konfigurationen für settings.json
settings = {
   "spellright.spellCheck": True,
   "spellright.documentTypes": ["markdown", "plaintext", "latex"],
   "spellright.language": ["de"],
   "spellright.ignoreWords": ["someCustomWord", "anotherWord"],
   "spellright.ignoreFiles": ["**/.git/**"],
   "editor.tabSize": 4,
   "editor.formatOnSave": True,
   "eslint.alwaysShowStatus": True,
   "python.analysis.typeCheckingMode": "basic",
   "python.linting.enabled": True,
   "python.linting.pylintEnabled": True,
   "python.linting.flake8Enabled": True,
   "python.formatting.provider": "black",
   "C_Cpp.updateChannel": "Default",
   "cmake.configureOnOpen": True,
   "clang-format.style": "file",
   "liveServer.settings.donotShowInfoMsg": True,
   "html-css-class-completion.enableEmmetSupport": True,
   "latex-workshop.latex.autoBuild.run": "onSave",
   "gitlens.views.repositories.files.layout": "tree",
   "markdown-all-in-one.italic.indicator": "_",
   "markdown-preview-enhanced.previewTheme": "github-dark.css",
   "latex-workshop.view.pdf.viewer": "tab",
   "markdown.preview.fontSize": 14,
   "markdown.preview.lineHeight": 1.6,
   "python.linting.flake8Args": ["--max-line-length=120"],
   "editor.codeActionsOnSave": {
   "source.fixAll.eslint": True
   },
   "python.testing.pytestArgs": [],
   "python.testing.unittestEnabled": False,
   "python.testing.nosetestsEnabled": False,
   "python.testing.pytestEnabled": True,
   "C_Cpp.clang_format_fallbackStyle": "Google",
   "files.autoSave": "onFocusChange",
   "editor.fontSize": 14,
   "platformio-ide.projectsDir": "/Ihr/Neuer/Pfad/PlatformIO/Projects"
}
```

## Git

### 1. GitLens — Git supercharged

GitLens verbessert die integrierte Git-Unterstützung von VS Code erheblich. Es bietet tiefgreifende Einblicke in die Codehistorie, erweiterte Blame-Informationen, die Anzeige von Änderungen in der Statusleiste, und vieles mehr. GitLens macht es einfacher zu verstehen, wer, warum und wann bestimmte Änderungen gemacht wurden, und bietet eine mächtige, interaktive Revisionshistorie und Vergleichsansichten.

### 2. Git Graph

Mit dieser Erweiterung können Sie eine visuelle Darstellung des Verzweigungs- und Merging-Verlaufs Ihres Repositories sehen. Git Graph unterstützt das Anzeigen von Refs, Commits, Tags, Branches und vielem mehr in einem interaktiven grafischen Format. Es ist besonders nützlich, um komplexe Verzweigungshistorien auf einen Blick zu verstehen.

### 3. Git History

Git History ermöglicht es Ihnen, die Historie von Commits, Branches oder Dateien in einem Git-Repository zu durchsuchen. Sie können die Historie von Dateien anzeigen, Vergleiche zwischen Commits durchführen und die Änderungen in verschiedenen Versionen Ihrer Dateien sehen.

### 4. Project Manager for Git

Diese Erweiterung vereinfacht das Wechseln zwischen Git-Repositories innerhalb von VS Code. Es ist besonders nützlich, wenn Sie an mehreren Projekten gleichzeitig arbeiten und schnell zwischen ihnen wechseln möchten.

### 5. Git Merger

Git Merger hilft beim Vereinfachen des Merge- und Rebase-Prozesses von Git-Branches direkt innerhalb von VS Code. Es bietet eine Benutzeroberfläche, um Konflikte zu lösen und den Merge- oder Rebase-Vorgang effizienter zu gestalten.

### 6. Git Blame

Mit der Git Blame-Erweiterung können Sie schnell sehen, wer eine bestimmte Zeile oder einen Block im Code geändert hat, indem Sie den Blame-Informationen direkt im Editor folgen. Es ist hilfreich, um zu verstehen, warum Änderungen vorgenommen wurden.

## Markdown

### 1. Markdown All in One

- **Features**: Unterstützt viele nützliche Funktionen wie Tastenkombinationen, automatisches Erstellen von Inhaltsverzeichnissen, schnelles Umschalten zwischen Bearbeitung und Vorschau, und vieles mehr.
- **Nutzen**: Vereinfacht die Bearbeitung von Markdown-Dokumenten und verbessert die Effizienz.

### 2. Markdown Preview Enhanced

- **Features**: Diese Erweiterung bietet eine erweiterte Vorschau-Funktion für Markdown-Dokumente. Es unterstützt Mermaid-Diagramme, KaTeX-Mathematik-Rendering, PlantUML-Diagramme und mehr.
- **Nutzen**: Ermöglicht eine umfassendere und flexiblere Vorschau von Markdown-Dokumenten, einschließlich der Darstellung von komplexen Diagrammen und mathematischen Formeln.

### 3. MarkdownLint

- **Features**: Bietet Linting für Markdown-Dateien, um die Einhaltung von Stil- und Syntaxregeln zu gewährleisten.
- **Nutzen**: Hilft, konsistente und fehlerfreie Markdown-Dokumentation zu schreiben.

### 4. Markdown PDF

- **Features**: Konvertiert Markdown-Dateien in PDF, HTML, PNG oder JPEG Dateien direkt aus VS Code heraus.
- **Nutzen**: Ermöglicht die einfache Verteilung oder Veröffentlichung von Markdown-Inhalten in verschiedenen Formaten.

### 5. Markdown Checkboxes

- **Features**: Bietet Unterstützung für das Hinzufügen und Verwalten von interaktiven Checkboxes in Markdown-Dokumenten.
- **Nutzen**: Ideal für die Erstellung von Aufgabenlisten oder das Verfolgen von Fortschritten direkt in Markdown.

## Python

### Python von Microsoft

- **Name**: Python
- **Herausgeber**: Microsoft
- **Features**:
  - **IntelliSense**: Autocomplete und Code-Vorschläge basierend auf der Python-Sprachspezifikation und installierten Bibliotheken.
  - **Linting**: Unterstützt verschiedene Linter wie Pylint, flake8, mypy, pydocstyle, und mehr, um Codequalität und Stil-Einhaltung zu gewährleisten.
  - **Debugging**: Leistungsstarkes Debugging-Tool, das lokale Skripte, Remote-Skripte, Multi-Threaded-Anwendungen und Web-Anwendungen unterstützt.
  - **Code-Formatierung**: Unterstützt Autopep8, black, und yapf, um den Code gemäß den PEP 8-Richtlinien und anderen Formatierungsstandards zu formatieren.
  - **Test-Unterstützung**: Ermöglicht das Ausführen und Debuggen von Tests direkt in der Editor-Oberfläche mit Unterstützung für Test-Frameworks wie unittest, pytest, und doctest.
  - **Jupyter-Notebooks**: Ermöglicht das Erstellen, Bearbeiten und Ausführen von Jupyter-Notebooks innerhalb von VS Code.
  - **Refactoring**: Bietet grundlegende Refactoring-Tools wie das Umbenennen von Symbolen, Extrahieren von Methoden oder Variablen und mehr.

- **Jupyter**: Eine Erweiterung, die speziell für die Arbeit mit Jupyter Notebooks innerhalb von VS Code entwickelt wurde, falls Sie intensiv mit Datenwissenschaft oder maschinellem Lernen arbeiten.
- **Python Docstring Generator**: Generiert automatisch detaillierte Docstrings für Python-Funktionen.
- **Pylance**: Eine Erweiterung von Microsoft, die eine schnelle, feature-reiche Sprachunterstützung für Python basierend auf der Sprachserverarchitektur bietet. Pylance baut auf der Python-Erweiterung auf und bietet erweiterte Funktionen wie Typüberprüfung, Auto-Import, und mehr.

## C und C++

### C/C++ von Microsoft

- **Name**: C/C++
- **Herausgeber**: Microsoft
- **Features**:
  - **IntelliSense**: Genießen Sie Autovervollständigung, Definitionen, Hover-Informationen, Signaturen und mehr, um das Schreiben von Code zu beschleunigen und Fehler zu minimieren.
  - **Debugging**: Die Erweiterung integriert sich nahtlos mit dem VS Code Debugger, was das Einstellen von Breakpoints, das Durchschreiten von Code, das Inspektieren von Variablen und das Ansehen von Call Stacks ermöglicht.
  - **Code-Navigation**: Unterstützt Features wie „Gehe zu Definition“, „Gehe zu Deklaration“, „Gehe zu Referenzen“ und „Peek Definition“, um schnell durch den Code zu navigieren.
  - **Code-Formatierung**: Automatisches Formatieren von Code unter Verwendung von Clang-Format oder anderen konfigurierbaren Formatierern.
  - **Linting**: Erkennen von potenziellen Problemen durch die Integration von externen Linting-Tools.
  - **CMake Integration**: Unterstützung für CMake-basierte Projekte, einschließlich der Möglichkeit, Build-Konfigurationen zu erstellen und zu verwalten.

- **CMake Tools**: Bietet Unterstützung für CMake-basierte Projekte, einschließlich Konfiguration, Build-Management und sogar Debugging. Diese Erweiterung ist besonders nützlich, wenn Sie komplexe Projekte mit CMake als Build-System haben.
- **Clang-Format**: Ermöglicht das automatische Formatieren von C/C++ Code unter Verwendung von Clang-Format. Dies kann helfen, einen konsistenten Code-Stil innerhalb Ihres Projekts zu gewährleisten.
- **Include Autocomplete**: Verbessert die Autovervollständigung für #include-Anweisungen, basierend auf den Pfaden, die in Ihrem Projekt konfiguriert sind.

## Google's C++ Code Style

### Schritt 1: Clang-Format installieren

- **macOS**: Installation über Homebrew mit `brew install clang-format`.

### Schritt 2: Clang-Format Erweiterung in VS Code installieren

Obwohl VS Code eine eingebaute Unterstützung für das Formatieren bietet, kann die Installation der **Clang-Format Erweiterung** die Benutzererfahrung verbessern:

1. Öffnen Sie den Extensions-View in VS Code (`Ctrl+Shift+X` / `Cmd+Shift+X`).
2. Suchen Sie nach "Clang-Format" und installieren Sie die Erweiterung.

### Schritt 3: Clang-Format konfigurieren

Um Google's C++ Code Style zu verwenden, müssen Sie eine `.clang-format`-Datei in Ihrem Projektverzeichnis oder in einem übergeordneten Verzeichnis erstellen, die VS Code mitteilt, welchen Stil es verwenden soll. Sie können diese Datei manuell erstellen oder ein Clang-Format-Befehl ausführen, um eine Vorlage zu generieren:

```bash
clang-format -style=google -dump-config > .clang-format
```

Diese Befehlszeile erstellt eine `.clang-format`-Datei mit den Standardkonfigurationen für Google's C++ Code Style.

### Schritt 4: Code Formatierung verwenden

Mit der eingerichteten `.clang-format`-Datei können Sie nun in VS Code den Befehl „Format Document“ verwenden (Rechtsklick im Dokument und „Format Document“ wählen oder die Tastenkombination `Shift+Alt+F` nutzen), um Ihren C/C++ Code automatisch gemäß Google's C++ Style Guide zu formatieren.

## LaTeX

### LaTeX Workshop

- **Name**: LaTeX Workshop
- **Herausgeber**: James Yu
- **Features**:
  - **PDF-Vorschau**: Direkte Anzeige des PDF-Ergebnisses innerhalb von VS Code, mit automatischem Update nach dem Kompilieren des LaTeX-Dokuments.
  - **Automatisches Kompilieren**: Unterstützt das automatische Kompilieren von LaTeX-Dateien bei Änderungen, basierend auf benutzerdefinierten Regeln oder beim Speichern.
  - **Syntax-Highlighting**: Verbessert die Lesbarkeit des LaTeX-Codes durch farbliche Hervorhebung der LaTeX-Syntax.
  - **Code-Schnipsel**: Bietet eine Sammlung von wiederverwendbaren LaTeX-Schnipseln, um die Eingabe häufig verwendeter LaTeX-Befehle zu beschleunigen.
  - **IntelliSense**: Unterstützt Autovervollständigung für LaTeX-Befehle und -Pakete.
  - **Linting**: Prüft den LaTeX-Code auf Fehler und Warnungen, um Probleme frühzeitig zu erkennen.
  - **Unterstützung für BibTeX**: Integrierte Unterstützung für das Arbeiten mit Bibliografien in BibTeX-Format.
  - **Mehrere LaTeX-Distributionen unterstützt**: Funktioniert mit verschiedenen LaTeX-Distributionen wie TeX Live, MiKTeX und MacTeX.

### Zusätzliche Konfiguration

Um die bestmögliche Erfahrung mit LaTeX Workshop zu erzielen, möchten Sie vielleicht Ihre VS Code Einstellungen anpassen, um Ihren Workflow zu optimieren. Dies kann beinhalten:

- **Anpassen der Kompilierungsoptionen**: Sie können in den Einstellungen der Erweiterung oder in der `settings.json`-Datei von VS Code spezifische Kompilierungsbefehle und -flags festlegen.
- **Einstellen der PDF-Vorschau**: Konfigurieren Sie, wie und wo die PDF-Vorschau angezeigt werden soll, zum Beispiel in einem neuen Editor-Tab, neben dem aktuellen LaTeX-Code oder in einem externen PDF-Viewer.

## Webentwicklung mit HTML, CSS, JavaScript und PHP

### Für HTML & CSS

- **Name**: Live Server
- **Beschreibung**: Startet einen lokalen Entwicklungsserver mit Live-Reload-Funktion für statische und dynamische Seiten.
- **Vorteile**: Ermöglicht es Ihnen, Änderungen an Ihrer HTML- und CSS-Datei in Echtzeit im Browser zu sehen, ohne die Seite manuell neu laden zu müssen.

- **Name**: HTML CSS Support
- **Beschreibung**: Bietet CSS-Klassen- und ID-Verknüpfungen innerhalb von HTML-Dokumenten.
- **Vorteile**: Verbessert die Autovervollständigung für CSS-Klassen und IDs in HTML, was die Entwicklungsgeschwindigkeit erhöht.

### Für JavaScript

- **Name**: ESLint
- **Beschreibung**: Integriert den ESLint-Linter in VS Code für JavaScript-Code.
- **Vorteile**: Hilft, gängige Fehler und Code-Stil-Probleme in JavaScript zu finden und zu beheben, um die Code-Qualität zu verbessern.

- **Name**: JavaScript (ES6) code snippets
- **Beschreibung**: Bietet Code-Snippets für JavaScript ES6-Syntax.
- **Vorteile**: Beschleunigt die Entwicklung durch die Bereitstellung von Snippets für gängige JavaScript-ES6-Patterns.

### Für PHP

- **Name**: PHP Intelephense
- **Beschreibung**: Eine schnelle, leistungsstarke und hochkonfigurierbare PHP-IDE-Funktionen wie IntelliSense, Definitionen finden, Hover, Dokumentationssuche und vieles mehr.
- **Vorteile**: Verbessert die PHP-Entwicklung durch Bereitstellung von erweiterten Code-Intelligence-Funktionen, die weit über die grundlegende Syntax-Hervorhebung hinausgehen.

- **Name**: PHP Debug    von XDebug
- **Beschreibung**: Integriert die XDebug PHP-Erweiterung, um Debugging-Funktionen in VS Code zu ermöglichen.
- **Vorteile**: Ermöglicht das Setzen von Breakpoints, das Inspektieren von Variablen und das Schritt-für-Schritt-Debugging von PHP-Code.

## Arduino und ESP32

### Arduino von Microsoft

- **Name**: Arduino
- **Herausgeber**: Microsoft
- **Features**:
  - **IntelliSense**: Profitieren Sie von Autovervollständigung und Fehlerhervorhebung für Ihre Arduino-Sketches.
  - **Board-Verwaltung**: Einfaches Hinzufügen und Wechseln zwischen verschiedenen Arduino- und ESP32-Boards direkt in VS Code.
  - **Bibliotheksverwaltung**: Suchen, installieren, verwalten und inkludieren von Arduino- und ESP32-Bibliotheken direkt aus dem VS Code.
  - **Sketch-Upload**: Laden Sie Ihre Sketche mit einem Klick auf Ihr Board hoch.
  - **Serieller Monitor**: Überwachen Sie die serielle Kommunikation zwischen VS Code und Ihrem Board.

### Konfiguration für ESP32

Nach der Installation der Arduino-Erweiterung müssen Sie einige zusätzliche Schritte unternehmen, um mit der Entwicklung für ESP32 zu beginnen:

1. **Installieren Sie die ESP32-Boardunterstützung** im Arduino IDE Board-Manager, falls noch nicht geschehen. Dies ist notwendig, damit die Arduino-Erweiterung in VS Code die ESP32-Boards erkennen kann.
2. **Wählen Sie Ihr ESP32-Board aus**: Nach der Installation der Board-Unterstützung können Sie Ihr ESP32-Board aus der Liste der verfügbaren Boards in der Arduino-Erweiterung auswählen.
3. **Konfigurieren Sie die serielle Verbindung**: Stellen Sie sicher, dass Sie den richtigen COM-Port für die Kommunikation mit Ihrem ESP32-Board ausgewählt haben.
