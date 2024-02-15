---
title: "Git-Workflow-PullRequests-Issues-Release"
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!-----------------------------------------------------------------------
ju 9-2-24 Git-Workflow-PullRequests-Issues-Release.md
pandoc Git-Workflow-PullRequests-Issues-Release.md -o Git-Workflow-PullRequests-Issues-Release.html -c inhalt.css --mathjax
------------------------------------------------------------------------->
# Git Workflow - Pull Requests - Issues - Releases

1. **Projektinitialisierung**:
   - Erstellung eines neuen GitHub-Repositorys für "MeinProjekt".
   - Initialisierung des Git-Repositorys, Hinzufügen der `README.md`, und Hochladen des Projekts auf GitHub.

2. **Feature-Entwicklung**:
   - Für neue Funktionen oder Bugfixes werden separate Feature-Branches erstellt, z.B. `feature/neue-coole-funktion`.
   - Änderungen werden gepusht, um sie auf GitHub verfügbar zu machen.

3. **Pull Requests überprüfen und genehmigen**:
   - Erstellung eines Pull Requests vom Feature-Branch in den Hauptbranch (`main`) mit einer detaillierten Beschreibung der Änderungen.
   - Selbstüberprüfung des Pull Requests, eventuelles Hinterlassen von Kommentaren für zukünftige Verbesserungen und Durchführen erforderlicher Änderungen.

4. **Issues bearbeiten und schließen**:
   - Bei Entdeckung eines Bugs während der Entwicklung wird ein Issue erstellt, um diesen später zu beheben.
   - Issues können geschlossen werden, sobald sie gelöst sind.

5. **Releases finalisieren und veröffentlichen**:
   - Vorbereitung und Erstellung eines Releases im Entwurfsmodus nach Abschluss der Feature-Entwicklung und Tests.
   - Veröffentlichung des Releases durch Entfernen des Entwurfsmodus.

## Git Labels


- **bug** Etwas funktioniert nicht
- **documentation** Verbesserungen oder Ergänzungen der Dokumentation
- **duplicate** Dieses Problem oder diese Pull-Anfrage existiert bereits
- **enhancement** Neue Funktion oder Anfrage
- **good first issue** Gut für Neueinsteiger
- **help wanted** Besondere Aufmerksamkeit ist erforderlich
- **invalid** Das scheint nicht richtig zu sein
- **question** Weitere Informationen werden erbeten
- **wontfix** Daran wird nicht gearbeitet

## Pull Requests - Issues - Releases


### Pull Requests

```bash
gh pr create
gh pr list
gh pr status
gh pr checkout
gh pr close
```

**Situation**: Du hast an einer neuen Funktion in einem Feature-Branch namens `feature/neue-funktion` gearbeitet und möchtest nun deine Änderungen in den Hauptbranch (`main`) mergen.

**Aktionen**:

- **Anzeigen von Pull Requests**: Überprüfe, ob es bereits offene Pull Requests gibt, die ähnliche Änderungen beinhalten.
  ```bash
  gh pr list
  ```
- **Erstellen eines Pull Requests**:
    - Erstelle einen neuen Pull Request, um deine Änderungen vorzuschlagen.
    ```bash
    gh pr create --base main --head feature/neue-funktion --title "Neue Funktion hinzufügen" --body "Fügt die Funktionalität X hinzu, um das Problem Y zu lösen." --reviewer @teammitglied1,@teammitglied2 --label "enhancement"
    ```
    - **Pull Requests auflisten**:
    ```sh
    gh pr list
    ```
    - **Pull Request auschecken**:
    ```sh
    gh pr checkout <pr-number>
    gh pr checkout 123
    ```

### Issues

```bash
gh issue create
gh issue list
gh issue status
gh issue close
```

**Situation**: Während der Entwicklung hast du einen Bug entdeckt, den du später bearbeiten möchtest.

**Aktionen**:

- **Anzeigen von Issues**: Sieh nach, ob der Bug bereits gemeldet wurde.
  ```bash
  gh issue list
  ```
- **Erstellen eines Issues**: Melde den neuen Bug.
  ```bash
  gh issue create --title "Bug: XYZ funktioniert nicht" --body "Wenn ich XYZ tue, passiert ZYX statt ABC." --assignee @du --label "bug"
  ```

### Releases

**Situation**: Deine neue Funktion ist fertig, getestet und bereit für die Veröffentlichung.

**Aktionen**:

- **Anzeigen von Releases**: Prüfe die bisherigen Releases.
  ```bash
  gh release list
  ```
- **Erstellen eines Releases**: Markiere die neue Version deiner Software.
  ```bash
  gh release create v1.2.0 --title "Release v1.2.0" --notes "Neue Funktion X hinzugefügt. Verschiedene Bugs behoben." --draft
  ```


## Git Workflow

1. **Projektinitialisierung**:
    - Du erstellst ein neues Repository auf GitHub für "MeinProjekt".
    ```bash
    gh repo list
    gh repo delete

    echo "# MeinProjekt" >> README.md
    git init
    git add README.md
    git commit -m "Projekt init"
    gh repo create MeinProjekt --private --source=. --remote=origin
    git push --set-upstream origin main
    git st
    git lg
    git push
    ```

2. **Feature-Entwicklung**:
    - Für jede neue Funktion oder jeden Bugfix erstellst du einen separaten Feature-Branch, z.B. `feature/neue-coole-funktion`.
    ```bash
    git checkout -b feature/neue-coole-funktion
    git push -u origin feature/neue-coole-funktion
    ```

### Pull Requests überprüfen und genehmigen

3. **Pull Request erstellen**:
    - Nach Abschluss der Arbeit an der Funktion erstellst du einen Pull Request für `feature/neue-coole-funktion` gegen den `main`-Branch.
    ```bash
    echo "Hallo Welt" >> code.c
    git add code.c
    git commit -m "Neue Funktion hinzugefügt"
    git log main..feature/neue-coole-funktion

    gh pr create --base main --head feature/neue-coole-funktion --title "Neue coole Funktion" --body "Fügt eine neue coole Funktion hinzu, die XYZ verbessert." --reviewer ju1-eu
    ```

4. **Selbstüberprüfung**:
    - Da du alleine arbeitest, übernimmst du die Rolle des Reviewers und überprüfst den Pull Request selbst. Du hinterlässt ggf. Kommentare für zukünftige Verbesserungen oder Dokumentationszwecke.
    - Führe die erforderlichen Änderungen durch und aktualisiere den Pull Request entsprechend.
    ```bash
    # PR-Nummer: 1
    gh pr list
    gh pr status
    gh pr review 1 --comment -b "Bitte füge noch Unit Tests für die neue Funktion hinzu."
    ```
5. **Pull Request genehmigen und mergen**:
    - Genehmige den Pull Request selbst und merge ihn in den `main`-Branch.
    ```bash
    gh pr list
    gh pr merge 1 --squash --delete-branch
    ```

### Issues bearbeiten und schließen

6. **Issue erstellen**:
    - Entdeckst du während der Entwicklung einen Bug, erstellst du ein Issue als Erinnerung, um diesen später zu beheben.
    ```bash
    gh issue create --title "Bug in neuer coole Funktion" --body "Die Funktion XYZ verursacht einen Fehler unter bestimmten Bedingungen." --assignee "@me" --label "bug"

    gh pr list
    # Issue-Nummer
    gh issue close 2
    ```

### Releases finalisieren und veröffentlichen

7. **Release vorbereiten**:
    - Sobald die Funktion fertig und getestet ist, bereitest du ein Release vor.
    ```bash
    # Release im Entwurfsmodus
    gh release create v1.1.0 --title "Release v1.1.0 - Neue coole Funktion" --notes "Version 1.1.0 fügt eine neue coole Funktion hinzu." --draft
    # Release veröffentlichen
    gh release edit v1.1.0 --draft=false
    # check
    gh release list
    gh release view v1.1.0
    git st
    git push
    git pull
    git lg
    * f8403af (HEAD -> main, tag: v1.1.0, origin/main) Neue Funktion hinzugefügt (#1)
    * 9e04d8a Projekt init
    ```


