---
title: "Git-Fork"
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!-----------------------------------------------------------------------
ju 9-2-24 Git-Fork.md
pandoc Git-Fork.md -o Git-Fork.html -c inhalt.css --mathjax
------------------------------------------------------------------------->
# Git Fork

Ein Git Fork bezeichnet das Erstellen einer eigenen Kopie eines bestehenden Repositorys auf deinem eigenen Konto. Dies ermöglicht es dir, unabhängig an einem Projekt zu arbeiten, ohne die Hauptversion des ursprünglichen Repositorys zu beeinflussen.

1. **Unabhängige Entwicklung**: Durch das Forken eines Repositorys kannst du Änderungen vornehmen, Experimente durchführen oder neue Features entwickeln, ohne die Hauptcodebasis zu stören. Dies ist besonders nützlich in Open-Source-Projekten, wo viele Entwickler zusammenarbeiten, aber nicht alle die Berechtigung haben, direkt Änderungen am Hauptrepository vorzunehmen.

2. **Beitrag zu Projekten**: Wenn du Verbesserungen oder Bugfixes in deinem Fork entwickelt hast, kannst du diese Änderungen dem ursprünglichen Repository über einen Pull Request (auf GitHub) oder Merge Request (auf GitLab) vorschlagen. Der Maintainer des Hauptrepositorys kann dann deine Änderungen überprüfen und entscheiden, ob sie in das Hauptprojekt integriert werden sollen.

3. **Lernen und Experimentieren**: Ein Fork bietet eine großartige Möglichkeit, den Code eines Projekts zu studieren und mit ihm zu experimentieren. Da du eine vollständige Kopie des Repositorys hast, kannst du ohne Risiko für das Originalprojekt lernen und experimentieren.

4. **Community und Zusammenarbeit**: Forks fördern die Zusammenarbeit und das Engagement in der Entwicklergemeinschaft. Durch das Forken und Beitragen zu Projekten kannst du mit anderen Entwicklern interagieren, Feedback erhalten und deine eigenen Fähigkeiten verbessern.


## Open-Source-Projekt namens "MeinProjekt"

Open-Source-Projekt namens "MeinProjekt", an dem Sie gerne mitarbeiten möchten. Das Projekt ist auf GitHub gehostet. Sie haben eine Idee für ein neues Feature oder einen Bugfix, den Sie beitragen möchten. Prozess umfasst des Forkens eines Repositories, des Entwickelns neuer Features, des Erstellens und Mergens von Pull Requests sowie des anschließenden Aufräumen.

### Schritt 1: Forken des Repositorys

```bash
# gh auth login
# Voraussetzung: GitHub / Erstelle Organizations: ju1-org / Repository forking erlauben
gh repo list
gh repo fork ju1-eu/MeinProjekt --org "ju1-org" --clone=true
# gh repo set-default --help

git remote -v
    origin	https://github.com/ju1-org/MeinProjekt-5.git (fetch)
    origin	https://github.com/ju1-org/MeinProjekt-5.git (push)
    upstream	https://github.com/ju1-eu/MeinProjekt.git (fetch)
    upstream	https://github.com/ju1-eu/MeinProjekt.git (push)
```

Einen Fork des Repositories ju1-eu/MeinProjekt erstellen, der als ju1-org/MeinProjekt-5 existiert, und diesen Fork lokal als MeinProjekt-5 klonen.

- **origin** wird benötigt, um Ihre lokalen Änderungen zu Ihrem eigenen GitHub-Fork zu pushen.
- **upstream** wird benötigt, um die neuesten Änderungen vom Hauptprojekt zu holen und in Ihren Fork zu integrieren.

### Schritt 2: Wechseln in das Repository-Verzeichnis

```bash
cd MeinProjekt-5
ls -la
# alias git log --oneline --graph --decorate
git lg
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

### Schritt 3: Erstellen eines neuen Branches

Jetzt erstellst du einen neuen Branch, um deine Änderungen isoliert zu halten.

```bash
# Hinzufügen des Upstream-Remotes
git remote -v
#git remote add upstream https://github.com/ju1-eu/MeinProjekt.git
git checkout -b feature-neues-cooles-feature
```

### Schritt 4: Vornehmen von Änderungen und Commit

Nimm die gewünschten Änderungen am Code vor. Dann füge die geänderten Dateien zum Commit hinzu und committe sie mit einer Nachricht.

```bash
#-----------------------------------------------------------------
# BEARBEITEN
#git checkout feature-neues-cooles-feature
ls -a
    .          ..         .git       .gitignore README.md  file.txt
vim file.txt
#-----------------------------------------------------------------
git add .
git commit -m "Ein neues cooles Feature hinzugefügt"
```

### Schritt 5: Pushen des Branches zu deinem Fork

Push deine Änderungen zurück zu deinem Fork auf GitHub.

```bash
git push origin feature-neues-cooles-feature
```

### Schritt 6: Erstellen eines Pull Requests

```bash
# Der PR soll die Änderungen aus dem Branch feature-neues-cooles-feature in den main Branch mergen.
gh pr create --repo ju1-org/MeinProjekt-5 --base main --head feature-neues-cooles-feature --title "Neues cooles Feature" --body "Hier ist eine detaillierte Beschreibung meines neuen coolen Features."
```

**Feedback zum Pull Request erhalten**

Maintainer (Betreuer) können dein PR überprüfen und Feedback geben.

**Pull Request Status überprüfen**

```bash
git remote -v
# Standard-Repository für GitHub setzen
gh repo set-default ju1-org/MeinProjekt-5
# Aktualisieren Sie Ihren lokalen main Branch mit Änderungen aus dem Upstream:
git checkout main
git fetch upstream
git merge upstream/main
git push origin main


git lg

# Pull Request Liste überprüfen
gh pr status
gh pr list
# PR-Nummer
gh pr view 1
    Neues cooles Feature #1
    Open • ju1-eu wants to merge 1 commit into main from feature-neues-cooles-feature • about 10 minutes ago
    +1 -0 • No checks


    Hier ist eine detaillierte Beschreibung meines neuen coolen Features.


    View this pull request on GitHub: https://github.com/ju1-org/MeinProjekt/pull/1
```

**Aktualisieren des Pull Requests nach Feedback**

Wenn du basierend auf dem Feedback Änderungen vornehmen musst:

1. Führe die erforderlichen Änderungen durch.
2. Committe und Pushe die Änderungen: Dein PR wird automatisch mit den neuen Änderungen aktualisiert.

```bash
#-----------------------------------------------------------------
# BEARBEITEN
git checkout feature-neues-cooles-feature
ls -a
    .          ..         .git       .gitignore README.md  file.txt
vim file.txt
#-----------------------------------------------------------------
git add .
git commit -m "Feedback umgesetzt und Verbesserungen vorgenommen"
git push origin feature-neues-cooles-feature
```

### Schritt 7: Kommunikation mit Maintainers

Um weiter zu kommunizieren oder Fragen zu stellen, kannst du Kommentare zu deinem PR hinzufügen:

```bash
# Kommunikation mit Maintainers
gh pr review 1 --comment -b "Hier sind weitere Erläuterungen oder Fragen."
```

### Schritt 8: Endgültige Überprüfung und Genehmigung des Pull Requests

- Warten Sie auf die endgültige Überprüfung durch die Maintainer. Seien Sie bereit, weitere Anpassungen vorzunehmen, falls dies erforderlich ist. Die endgültige Genehmigung kann direkt zur Integration Ihrer Änderungen durch einen Merge führen.

- Nutzen Sie Test-Frameworks, die für die Programmiersprache oder das Framework Ihres Projekts geeignet sind, wie JUnit für Java, pytest für Python, oder jest für JavaScript.

```bash
# PR-Nummer: 1
gh pr list
gh pr status
# Überprüfung durch die Maintainer
gh pr review 1 --comment -b "Bitte füge noch Unit Tests für die neue Funktion hinzu."

#-----------------------------------------------------------------
# BEARBEITEN
git checkout feature-neues-cooles-feature
ls -a
    .          ..         .git       .gitignore README.md  file.txt
vim file.txt
#-----------------------------------------------------------------
git add .
git commit -m "Unit Tests für neue Funktion hinzugefügt"
# Änderungen zu Ihrem Fork zu pushen
git push origin feature-neues-cooles-feature
# Änderungen vorgenommen und erneute Überprüfung bitten
gh pr review 1 --comment -b "Ich habe die angeforderten Unit Tests hinzugefügt und die erforderlichen Änderungen vorgenommen. Bitte überprüfen Sie erneut, wenn Sie Zeit haben. Danke!
"
```

### Schritt 9: Merge des Pull Requests

- Nach Genehmigung durch die Maintainer wird Ihr Beitrag in das Hauptrepository integriert. Die Maintainer entscheiden über die Merge-Strategie (z.B. Merge Commit, Squash and Merge, Rebase and Merge).
  ```bash
  gh pr list
  # Projekt-Maintainer
  gh pr merge 1 --squash --delete-branch
  gh pr status
  ```

### Schritt 10: Aufräumen nach dem Merge

- Lokales und Remote-Aufräumen, um Ihr Arbeitsverzeichnis und Ihr Fork sauber zu halten:
  ```bash
  # prüfen
  git branch
  git remote -v
  #git branch -d feature-neues-cooles-feature
  #git push origin --delete feature-neues-cooles-feature
  ```

### Schritt 11: Synchronisieren Ihres Forks

- Sicherzustellen, dass Ihr Fork aktuell bleibt
- Regelmäßig den **lokalen main Branch** synchronisieren, bevor Änderungen pushen.
    - **upstream/main** (dem Hauptrepository) und
    - **origin/main** (Ihr Fork)
  ```bash
  # Fügen Sie das Hauptrepository als Upstream-Remote hinzu
  #git remote add upstream https://github.com/ju1-eu/MeinProjekt.git

  # Holen Sie die neuesten Änderungen von Upstream:
  #git fetch upstream
  # Mergen Sie die Änderungen von Upstream in Ihren lokalen Hauptbranch:
  git checkout main
  #git merge upstream/main

  # Änderungen von Ihrem Fork (origin/main) holen und integrieren
  git pull origin main

  # Änderungen vom ursprünglichen Repository holen und in den lokalen main Branch   mergen
  git pull upstream main
  # Aktualisierten main Branch zu Ihrem Fork pushen
  git push origin main
  ```




