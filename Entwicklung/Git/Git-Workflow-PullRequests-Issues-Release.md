---
thema: "Management von Git-Prozessen"
runningtitle: "PullRequests - Issues - Release"
keywords: ""
abstract: |
	Der Prozess der Softwareentwicklung mit Git umfasst verschiedene Schritte, die von der Initialisierung eines Projekts bis hin zur Veröffentlichung eines Releases reichen. Zunächst wird ein neues Repository für das Projekt angelegt und mit einer `README.md` auf GitHub hochgeladen. Für jede neue Funktion oder jeden Bugfix werden dedizierte Feature-Branches erstellt, die nach Fertigstellung in den Hauptbranch gemergt werden. Dies geschieht über Pull Requests, die eine zentrale Rolle im Überprüfungsprozess spielen und vor der Genehmigung selbst überprüft werden können.

	Während der Entwicklung auftretende Bugs werden als Issues festgehalten und nach ihrer Lösung geschlossen. Das Endziel ist die Veröffentlichung eines Releases, welches nach abschließenden Tests aus dem Entwurfsmodus genommen und offiziell veröffentlicht wird. Git bietet zudem Labels zur Kategorisierung von Pull Requests und Issues, um den Überblick über den Projektstatus zu behalten und die Priorisierung zu erleichtern.

	Die Befehlszeilenschnittstelle GitHub CLI (`gh`) erleichtert die Interaktion mit GitHub, indem sie das Erstellen und Verwalten von Pull Requests, Issues und Releases direkt vom Terminal aus ermöglicht. Der gesamte Workflow unterstreicht die Bedeutung von Selbstüberprüfung, Kommunikation und transparentem Projektmanagement. Die Fähigkeit, Änderungen effektiv zu integrieren und Feedback umzusetzen, bildet das Rückgrat eines erfolgreichen Entwicklungsprozesses.

	\section*{Keywords}

	\begin{description}
		\item[Git] Ein Versionskontrollsystem, das es Entwicklern ermöglicht, Änderungen am Code nachzuverfolgen und mit anderen zusammenzuarbeiten.
		\item[GitHub] Eine Plattform für die gemeinsame Codeverwaltung und Kollaboration, die auf Git aufbaut.
		\item[Repository (Repo)] Ein Speicherort für ein Projekt, der den gesamten Code, die Dokumentation und die Versionshistorie enthält.
		\item[README.md] Eine Markdown-Datei, die eine Übersicht über das Projekt, Installationsanweisungen und weitere wichtige Informationen bietet.
		\item[Feature-Branch] Ein separater Branch im Git-Repository, der für die Entwicklung neuer Funktionen oder das Beheben von Fehlern verwendet wird.
		\item[Pull Request] Ein Vorschlag für Änderungen am Hauptbranch, der zur Überprüfung und Diskussion gestellt wird.
		\item[Issue] Ein Eintrag auf GitHub, der ein Problem oder eine Anfrage für eine Verbesserung im Projekt beschreibt.
		\item[Release] Eine veröffentlichte Version eines Projekts, die für Endnutzer verfügbar gemacht wird.
		\item[Label] Tags oder Kennzeichnungen in GitHub, die dazu dienen, Issues und Pull Requests zu kategorisieren und zu organisieren.
		\item[GitHub CLI (`gh`)] Eine Kommandozeilenschnittstelle, die es ermöglicht, GitHub-Funktionen direkt aus dem Terminal zu nutzen.
	\end{description}
author: 'ju'
date: \today
---
<!-------------------------------------------------------------------------------------------------------------
ju 2024-03-06 Git-Workflow-PullRequests-Issues-Release.md
pandoc Git-Workflow-PullRequests-Issues-Release.md -o Git-Workflow-PullRequests-Issues-Release.html -c navigation.css --mathjax --citeproc --bibliography=literatur.bib --csl=zitierstil-number.csl

Quelle [@spanner:2019:robotik].

Fußnote.[^1]
[^1]: Text der Fußnote.

[Google](https://www.google.com)

![Logo 2](images/Logo/Logo2.pdf)

**Tabelle 1:** Beschreibung

pandoc Git-Workflow-PullRequests-Issues-Release.md --to latex --output Git-Workflow-PullRequests-Issues-Release.tex --template=vorlage-main.tex --lua-filter=combined-filter.lua
pdflatex Git-Workflow-PullRequests-Issues-Release.tex
biber Git-Workflow-PullRequests-Issues-Release
pdflatex Git-Workflow-PullRequests-Issues-Release.tex
pdflatex Git-Workflow-PullRequests-Issues-Release.tex

ChatGPT:

Zusammenfassung in Latex: Schreibstil: Expositorisch ohne Form du/sie
Erstellen Sie eine kurze (ca. 200 Wörter) und ansprechende Zusammenfassung zum nachfolgenden Text. Die Zusammenfassung sollte für jemanden ohne wissenschaftlichen Hintergrund verständlich sein und gleichzeitig die wichtigsten Fakten genau wiedergeben. Beachte den Zusammenhang. Textinhalt: " "

Keywords: Erstelle mir eine Liste der wichtigsten Keywords zum Textinhalt.

Erklärung in Latex: Erkläre die Schlüsselwörter. Bereite die Antwort gehirngerecht auf mit Didaktische Reduktion.

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
---------------------------------------------------------------------------------------------------------------->

# Git

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
    gh pr create --base main --head feature/neue-funktion --title "Neue Funktion hinzufügen" --body "Fügt die    Funktionalität X hinzu, um das Problem Y zu lösen." --reviewer @teammitglied1,@teammitglied2 --label    "enhancement"
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

3. **Pull Requests überprüfen und genehmigen**:
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

6. **Issues bearbeiten und schließen**:
    - Entdeckst du während der Entwicklung einen Bug, erstellst du ein Issue als Erinnerung, um diesen später zu beheben.

    ```bash
    gh issue create --title "Bug in neuer coole Funktion" --body "Die Funktion XYZ verursacht einen Fehler unter bestimmten Bedingungen." --assignee "@me" --label "bug"

    gh pr list
    # Issue-Nummer
    gh issue close 2
    ```

7. **Releases finalisieren und veröffentlichen**:
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
