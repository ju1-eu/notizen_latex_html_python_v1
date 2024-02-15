---
title: "Git-Workflow-Python-Entwicklung"
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!-----------------------------------------------------------------------
ju 9-2-24 Git-Workflow-Python-Entwicklung.md
pandoc Git-Workflow-Python-Entwicklung.md -o Git-Workflow-Python-Entwicklung.html -c inhalt.css --mathjax
------------------------------------------------------------------------->
# Python-Entwicklung

Python-Programme zu entwickeln, die Markdown (.md) in LaTeX und HTML-Dokumente umwandeln, und unter Verwendung von Git und GitHub für Versionskontrolle und Zusammenarbeit.

### 1. Einrichtung des Repositories

- **Repository erstellen**: Erstelle ein neues Repository auf GitHub (oder einem ähnlichen Dienst) für dein Projekt. Dies wird das zentrale Remote-Repository sein, wo der Code und die Dokumentation gespeichert werden.

### 2. Lokales Arbeiten

- **Repository klonen**: Klone das Repository zu deinem lokalen System, um eine Arbeitskopie deines Projekts zu haben.
- **Branching-Strategie definieren**: Entscheide, ob du Feature-Branches für jede neue Funktion oder Verbesserung verwenden möchtest. Dies hält Änderungen organisiert und isoliert vom Hauptentwicklungszweig (`main` oder `master`).

### 3. Entwicklung

- **Neue Branches erstellen**: Für jede neue Funktion oder jeden Bugfix erstelle einen neuen Branch von `main`.
- Branch-Namenskonventionen: Implementiere klare Namenskonventionen für Branches, die den Zweck oder den Typ der Arbeit widerspiegeln, z.B. feature/, bugfix/, hotfix/, oder docs/, um die Übersichtlichkeit und das Management der Branches zu verbessern.
- Verwendung von git fetch regelmäßig: Führe regelmäßig git fetch aus, um den lokalen Status deines Repositories mit dem Remote-Repository zu synchronisieren und über neue Änderungen oder Branches informiert zu sein.
- **Commits machen**:
    - Atomare Commits: Halte Commits klein und fokussiert, mit jeder Änderung, die einen einzigen logischen Zweck erfüllt. Dies vereinfacht das Debugging und eventuelle Rollbacks.
    - Commit-Nachrichten: Verwende eine klare und konventionelle Struktur für Commit-Nachrichten, z.B. mit einem prägnanten Titel, einer leeren Zeile und einer detaillierteren Beschreibung des Commits, um die Lesbarkeit und Nachvollziehbarkeit zu verbessern.
- **Regelmäßig pushen**: Push deine Commits regelmäßig zu deinem Remote-Branch, um deine Änderungen auf GitHub zu sichern und für andere sichtbar zu machen.

### 4. Zusammenarbeit und Integration

- **Pull Requests verwenden**: Wenn du bereit bist, deine Änderungen in den `main`-Branch zu integrieren, erstelle einen Pull Request (PR) auf GitHub. Beschreibe, was dein PR macht, und verlinke alle relevanten Issues.
- **Code Reviews**:
    - Stelle sicher, dass Pull Requests (PRs) gründlich von mindestens einem anderen Teammitglied überprüft werden, bevor sie gemerged werden. Erwäge die Verwendung von GitHub's Review- und Kommentarfunktionen, um Feedback zu geben und zu erhalten.
- **Konflikte lösen**: Wenn es Merge-Konflikte gibt, löse sie manuell auf, bevor der PR gemerged werden kann.
- **PRs mergen**: Nachdem der PR überprüft und genehmigt wurde, merge ihn in den `main`-Branch. GitHub bietet Werkzeuge, um dies direkt in der Benutzeroberfläche zu tun.

### 5. Aktualisierung und Wartung

- **Regelmäßige Updates**: Halte deinen lokalen `main`-Branch regelmäßig mit `git pull` aktualisiert, um die neuesten Änderungen zu erhalten.
- **Releases taggen**: Verwende Git-Tags, um Releases oder Versionen deines Codes zu markieren. Dies erleichtert die Nachverfolgung von Versionen und die Veröffentlichung deiner Software.

### 6. Forks und Beiträge

- **Mit Forks arbeiten**: Wenn andere an deinem Projekt mitwirken möchten, können sie es forken, Änderungen in ihrem geforkten Repository vornehmen und dann einen Pull Request stellen, um ihre Beiträge einzubringen.
- **Community-Beiträge annehmen**:
    - Detailliertere CONTRIBUTING.md: Erweitere deine CONTRIBUTING.md, um spezifische Anweisungen für das Einrichten der Entwicklungsumgebung, das Erstellen von Issues, das Einreichen von Pull Requests und Richtlinien für die Code-Überprüfung zu geben.
    - Issue- und PR-Templates: Erstelle GitHub Issue- und PR-Templates, um Konsistenz und Vollständigkeit in den Beiträgen zu fördern und den Beitragenden zu erleichtern, alle notwendigen Informationen bereitzustellen.

### GitHub-spezifische Werkzeuge

- **GitHub Actions**: Nutze GitHub Actions für Continuous Integration (CI) und Continuous Deployment (CD) Prozesse, um deine Markdown-zu-Latex/HTML-Konversion automatisch zu testen und zu deployen.
- **GitHub Issues**: Verwende Issues, um Aufgaben, Features und Bugs zu verfolgen. Dies fördert die Transparenz und erleichtert die Zusammenarbeit.


## Git-Workflow Python-Entwicklung

### Schritt 1: Repository Setup auf GitHub

**Repository erstellen**:

```bash
gh repo create md-to-latex-html-converter --public --description "Konverter von Markdown zu LaTeX und HTML"

echo "# md-to-latex-html-converter" >> README.md
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore
cp <Pfad-zur-Lizenzdatei> LICENSE
git add README.md .gitignore LICENSE
git commit -m "Initial commit with README, .gitignore, and LICENSE"
git push -u origin main
```

### Schritt 2: Lokales Setup und Entwicklung

**Repository klonen**:

```bash
gh repo clone <dein-username>/md-to-latex-html-converter
```

**Neue Branch erstellen**:

Branching-Strategie festlegen: Für dieses Beispiel verwenden wir Feature-Branches.

```bash
git checkout -b feature/markdown-to-html
```

**Entwicklung, Commits, und Push**:

Nachdem du deine Entwicklung abgeschlossen hast und bereit bist zu commiten:

```bash
git add .
git commit -m "Füge die Umwandlungslogik von Markdown zu HTML hinzu"
git push --set-upstream origin feature/markdown-to-html
```

### Schritt 3: Zusammenarbeit und Integration

- **Pull Request erstellen**: Gehe zu GitHub und erstelle einen Pull Request für deinen Feature-Branch in den main-Branch.
- **PR-Template nutzen**: Fülle die PR-Beschreibung gemäß dem vordefinierten Template aus.
- **Code Review durchführen**: Lass deinen Code von Teammitgliedern überprüfen und diskutieren.
- **Merge-Konflikte lösen**: Löse etwaige Merge-Konflikte, die GitHub meldet.
- **Pull Request mergen**: Merge den Pull Request, nachdem er genehmigt wurde.

**Pull Request erstellen**:

```bash
gh pr create --base main --head feature/markdown-to-html --title "Markdown zu HTML Konverter" --body "Fügt die Grundfunktionalität für die Umwandlung von Markdown zu HTML hinzu."
```

**Pull Requests auflisten und überprüfen**:

```bash
gh pr list
gh pr view <PR-Nummer> --web
```

**Merge-Konflikte lösen** (dies erfordert manuelles Eingreifen basierend auf den Konflikten).

### Schritt 4: Automatisierung mit GitHub Actions

Python-Tests automatisch auszuführen, wann immer neue Commits gepusht werden.

**Erstellen der CI/CD-Workflows** erfolgt durch direktes Hinzufügen der YAML-Dateien zum `.github/workflows/`-Ordner in deinem Repository und Pushen dieser Änderungen.

```YAML
# .github/workflows/ci.yml
name: Python application

on: [push]

jobs:
  build:
    runs-on: macos-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest
```

### Schritt 5: Beitragenden-Leitfaden und Community-Beiträge

Erklärt, wie andere zu deinem Projekt beitragen können, einschließlich der Einrichtung ihrer Entwicklungsumgebung, der Erstellung von Pull Requests und der Verhaltensregeln.

**CONTRIBUTING.md hinzufügen und pushen**:

```bash
echo "Beitragende Richtlinien" >> CONTRIBUTING.md
git add CONTRIBUTING.md
git commit -m "Füge CONTRIBUTING.md hinzu"
git push
```

**Community-Beiträge annehmen**:

Überprüfen und Mergen von Pull Requests kann auch über `gh pr` Kommandos erfolgen, wie oben gezeigt.

