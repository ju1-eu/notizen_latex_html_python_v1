---
thema: "Projektmanagement auf GitHub"
runningtitle: "Issues"
keywords: ""
abstract: |
	Effizientes Projektmanagement ist der Schlüssel zum Erfolg jedes Softwareentwicklungsprojekts. GitHub, eine der führenden Plattformen für Softwareentwicklung, bietet vielfältige Werkzeuge zur Unterstützung dieses Prozesses. Dieser Artikel gibt eine Einführung in die effektive Nutzung von Issues, Labels, Meilensteinen und Pull Requests für ein strukturiertes Projektmanagement.

	Issues sind zentral für die Organisation und Priorisierung von Aufgaben. Durch die Anwendung von Git Labels können Issues und Pull Requests kategorisiert werden, was eine schnellere Identifizierung und Bearbeitung ermöglicht. Labels wie `bug`, `documentation` und `enhancement` helfen, den Typ oder Zustand eines Issues zu erkennen.

	Die Priorisierung von Issues erfolgt durch eine Kombination aus der Übersichtlichkeit, die durch `gh issue list` erreicht wird, und der gezielten Bewertung basierend auf Benutzeranforderungen oder Sicherheitsbedenken. Labels und Meilensteine erleichtern diese Priorisierung zusätzlich.

	Für die Bearbeitung von Issues ist die Erstellung spezifischer Branches üblich. Dies ermöglicht eine geordnete Entwicklung und das Festhalten von Fortschritten durch regelmäßige Commits. Sobald eine Lösung für ein Issue gefunden wurde, wird ein Pull Request erstellt, um die Änderungen in den Hauptbranch zu integrieren.

	Meilensteine sind besonders wertvoll für die Planung und Durchführung von Projektphasen. Sie unterstützen die Organisation von Issues in größere Arbeitspakete oder Releases. Durch die Möglichkeit, Meilensteine zu erstellen, zu aktualisieren und zu löschen, bleibt das Projektmanagement flexibel und übersichtlich.

	\section*{Schlüsselwörter}
	
	\begin{enumerate}
		\item \textbf{GitHub}: Eine Plattform für Softwareentwicklung, die Werkzeuge für Versionskontrolle und Kollaboration bietet.
		\item \textbf{Issues}: Aufgaben, Vorschläge, Bugs oder andere Anliegen, die innerhalb eines Projekts verfolgt und verwaltet werden.
		\item \textbf{Labels}: Markierungen, die Issues oder Pull Requests kategorisieren, um deren Zustand, Typ oder Priorität anzugeben.
		\item \textbf{Meilensteine}: Werkzeuge zur Gruppierung von Issues und Pull Requests in größere Arbeitspakete oder Releases mit Zielsetzungen und Fristen.
		\item \textbf{Pull Requests}: Vorschläge zur Änderung des Codes, die überprüft, diskutiert und in das Projekt integriert werden können.
		\item \textbf{Branch}: Eine parallele Version eines Repositories, die verwendet wird, um Änderungen isoliert zu entwickeln.
		\item \textbf{Merge}: Der Prozess, Änderungen aus einem Branch in einen anderen zu integrieren.
		\item \textbf{Git Labels}: Spezifische Kategorien wie `bug`, `documentation`, und `enhancement`, die helfen, Issues und Pull Requests zu organisieren.
		\item \textbf{Priorisierung}: Die Bewertung und Anordnung von Issues basierend auf ihrer Wichtigkeit oder Dringlichkeit.
		\item \textbf{gh issue list}: Ein Befehl in der GitHub CLI, um eine Liste von Issues anzuzeigen.
		\item \textbf{gh pr merge}: Ein Befehl, um Pull Requests über die GitHub CLI zu mergen.
		\item \textbf{Rebase and merge}, \textbf{Squash and merge}: Methoden zum Integrieren von Änderungen, die unterschiedliche Strategien für die Zusammenführung und Historie bieten.
	\end{enumerate}
author: 'ju'
date: \today
---
<!-------------------------------------------------------------------------------------------------------------
ju 2024-03-06 Git-Workflow-Issues.md
pandoc Git-Workflow-Issues.md -o Git-Workflow-Issues.html -c navigation.css --mathjax --citeproc --bibliography=literatur.bib --csl=zitierstil-number.csl

Quelle [@spanner:2019:robotik].

Fußnote.[^1]
[^1]: Text der Fußnote.

[Google](https://www.google.com)

![Logo 2](images/Logo/Logo2.pdf)

**Tabelle 1:** Beschreibung

pandoc Git-Workflow-Issues.md --to latex --output Git-Workflow-Issues.tex --template=vorlage-main.tex --lua-filter=combined-filter.lua
pdflatex Git-Workflow-Issues.tex
biber Git-Workflow-Issues
pdflatex Git-Workflow-Issues.tex
pdflatex Git-Workflow-Issues.tex

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
# Issues

**Einleitung**: Für eine effiziente Projektverwaltung auf GitHub ist das gezielte Management von Issues, Labels, Meilensteinen und Pull Requests entscheidend. Dieser Artikel bietet eine detaillierte Anleitung.

**1. Verwendung von Git Labels**:

- **Zweck**: Labels kategorisieren Issues und Pull Requests, um deren Zustand oder Typ anzugeben, wie z.B. `bug`, `documentation`, `enhancement`.
- **Anwendung**: Labels erleichtern die Priorisierung und Organisation von Aufgaben.

**2. Priorisierung von Issues**:

- **Übersicht**: Erstelle mittels `gh issue list` einen Überblick über offene Issues.
- **Bewertung**: Entscheide basierend auf Faktoren wie Benutzeranforderungen oder Sicherheitsbedenken, welche Issues Vorrang haben.
- **Labels**: Nutze `gh issue create --label` und `gh issue edit --add-label` zur Kennzeichnung der Dringlichkeit.
- **Meilensteine**: Gruppiere Issues in Arbeitspakete oder Releases mit `gh api` zur Meilensteinerstellung und Zuweisung.

**3. Bearbeitung von Issues**:

- **Branch-Erstellung**: Für jedes Issue wird ein spezifischer Branch erstellt (`git checkout -b fix/4-kurze-beschreibung`).
- **Lösungsfindung**: Arbeit im entsprechenden Branch und regelmäßige Commits dokumentieren den Fortschritt.
- **Pull Request**: Nach Fertigstellung wird mit `gh pr create` ein Pull Request erstellt, der das Issue adressiert.

**4. Schließen von Issues**:

- **Pull Request-Merge**: Genehmigte Pull Requests werden gemerged (`gh pr merge`), wobei die Methode (`Create a merge commit`, `Rebase and merge`, `Squash and merge`) je nach Projektbedürfnissen gewählt wird.
- **Manuelles Schließen**: Nicht automatisch geschlossene Issues können manuell beendet werden (`gh issue close`).

**5. Meilensteine handhaben**:

- **Überblick und Organisation**: Meilensteine unterstützen die strukturierte Planung und Durchführung von Projektphasen.
- **Löschen**: Nicht benötigte Meilensteine können entfernt werden, um Klarheit im Projektmanagement zu bewahren.

## Priorisieren von Issues

1. **Überblick verschaffen**:
    - Liste alle offenen Issues auf, um einen Überblick zu bekommen.

    ```bash
    # Issue-Nummer
    gh issue list
    ```

2. **Issues bewerten**:
    - Überlege, welche Issues den größten Einfluss auf das Projekt haben oder am dringendsten sind. Berücksichtige dabei Faktoren wie Benutzeranfragen, Sicherheitslücken oder Abhängigkeiten zwischen Funktionen.

3. **Labels verwenden**:
    - Nutze Labels, um die Dringlichkeit (z.B. `bug`, `enhancement`) der Issues zu kennzeichnen. Du kannst Issues direkt bei der Erstellung oder durch nachträgliche Bearbeitung labeln.

    ```bash
    gh issue create --title "Issue title" --body "Issue body"
    gh issue create --title "Neue Funktion" --body "Beschreibung..." --label "enhancement"
    # Issue-Nummer
    gh issue list
    gh issue edit 4 --add-label "bug"
    ```

4. **Meilensteine setzen**:
    - Ordne Issues Meilensteinen zu, um sie in größere Arbeitspakete oder Releases zu gruppieren.
  
    ```bash
    # Meilenstein erstellen
    gh api \
        --method POST \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        /repos/ju1-eu/mein-neues-repo/milestones \
        -f title='Meilenstein 5' \
    -f state='open' \
    -f description='Tracking milestone for version 1.1' \
    -f due_on='2024-03-09T23:39:01Z'

    # Issues einem Meilenstein zuordnen
    # Issue-Nummer
    gh issue list
    gh issue edit 4 --milestone "Meilenstein 5"
    ```

## Bearbeiten von Issues

1. **Branch erstellen**:
    - Für jedes Issue, das du bearbeiten möchtest, erstelle einen neuen Branch basierend auf dem Issue-Titel oder der -Nummer.
  
    ```bash
    # Issue-Nummer
    gh issue list
    git checkout -b fix/4-kurze-beschreibung
    git push origin fix/4-kurze-beschreibung
    git branch -r
    ```

2. **Problem lösen**:
    - Arbeite im erstellten Branch an der Lösung des Issues. Führe regelmäßig Commits durch, um deine Fortschritte zu speichern.
  
    ```bash
    vim code.c
    git commit -a
    git st
    git lg
    ```

3. **Pull Request erstellen**:
    - Sobald du mit der Lösung zufrieden bist, erstelle einen Pull Request, um die Änderungen im Branch zurück in den Hauptbranch (`main` oder `master`) zu mergen. Verknüpfe den Pull Request mit dem entsprechenden Issue, indem du die Issue-Nummer in der Beschreibung erwähnst.

    ```bash
    # Issue-Nummer
    gh issue list
    gh pr create --base main --head fix/4-kurze-beschreibung --title "Fix für Issue #4" --body "Löst das Problem, indem..."
    ```

## Issues schließen

1. **Pull Request mergen**:
    - Sobald der Pull Request überprüft und genehmigt wurde, merge ihn in den Hauptbranch. GitHub schließt automatisch verknüpfte Issues, wenn der Pull Request einen Hinweis wie Fixes `#<Issue-Nummer>` enthält.

    ```bash
    # pull request-Nummer
    gh pr list
    gh pr merge 6
    ```

    - **Create a merge commit**: Diese Option erstellt einen Merge-Commit, der alle Commits aus dem Pull Request in den Zielbranch einfügt. Die gesamte Commit-Historie des Feature-Branches bleibt erhalten. Diese Methode eignet sich, wenn du die vollständige Historie des Feature-Branches im Hauptbranch nachvollziehen möchtest.

    - **Rebase and merge**: Bei dieser Methode werden die Commits aus dem Feature-Branch auf die Spitze des Hauptbranchs rebasiert, ohne einen Merge-Commit zu erstellen. Dies hält die Projekt-Historie linear und sauber, kann aber die Commit-Zeitstempel ändern.

    - **Squash and merge**: Hierbei werden alle Commits aus dem Pull Request in einen einzigen Commit zusammengefasst und zum Zielbranch hinzugefügt. Diese Methode ist nützlich, um eine saubere Historie zu behalten, besonders wenn der Pull Request viele kleine oder experimentelle Commits enthält.

2. **Issue manuell schließen**:
    - Falls ein Issue nicht automatisch geschlossen wurde, kannst du es manuell schließen, sobald das Problem gelöst ist.

    ```bash
    # Issue-Nummer
    gh issue list
    gh issue close 4
    gh pr list


    # Meilenstein listen
    # Milestone-Nummer "number":
    gh api \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        /repos/ju1-eu/mein-neues-repo/milestones

    # Meilenstein löschen
    # Milestone-Nummer "number": 7
    gh api \
        --method DELETE \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        /repos/ju1-eu/mein-neues-repo/milestones/7

    git st
    git lg
    *   b3f15b6 (HEAD -> main, origin/main) Merge pull request #6 from ju1-eu/fix/4-kurze-beschreibung
    |\
    | * 94b47d2 (origin/fix/4-kurze-beschreibung) ok
    | * 28f44f7 Hallo Welt
    |/
    * f8403af (tag: v1.1.0) Neue Funktion hinzugefügt (#1)
    * 9e04d8a Projekt init
    ```

# Git Labels

- **bug** Etwas funktioniert nicht
- **documentation** Verbesserungen oder Ergänzungen der Dokumentation
- **duplicate** Dieses Problem oder diese Pull-Anfrage existiert bereits
- **enhancement** Neue Funktion oder Anfrage
- **good first issue** Gut für Neueinsteiger
- **help wanted** Besondere Aufmerksamkeit ist erforderlich
- **invalid** Das scheint nicht richtig zu sein
- **question** Weitere Informationen werden erbeten
- **wontfix** Daran wird nicht gearbeitet

# Issues - Probleme diskutieren, Lösungen planen und Fortschritt verfolgen

**Funktionen und Nutzen von Issues:**

- **Kommunikation und Kollaboration**: Issues ermöglichen es Projektmitgliedern und externen Beitragenden, Probleme zu diskutieren, Informationen auszutauschen und gemeinsam an Lösungen zu arbeiten.
- **Aufgabenverwaltung**: Sie dienen als Aufgabentracker, der es ermöglicht, den Fortschritt von bestimmten Aufgaben oder Fehlern im Auge zu behalten.
- **Organisation**: Issues können mit Labels, **Meilensteinen** und Zuweisungen an bestimmte Personen organisiert werden, um Prioritäten zu setzen und die Übersicht zu behalten.
- **Integration**: Sie lassen sich mit Pull Requests verknüpfen, um Änderungen direkt mit dem betreffenden Issue zu verbinden. Dies erleichtert die Nachverfolgung, welche Änderungen zur Lösung eines spezifischen Problems beitragen.
- **Transparenz**: Durch die öffentliche Dokumentation von Diskussionen und Entscheidungen bieten Issues einen transparenten Einblick in die Entwicklung und Entscheidungsprozesse innerhalb eines Projekts.
- **Benachrichtigungen**: Teilnehmer eines Issues erhalten Updates zu Änderungen oder Kommentaren, was eine zeitnahe Reaktion auf neue Informationen ermöglicht.

**Anwendungsbereiche:**

- **Fehlerberichte**: Nutzer oder Entwickler können Bugs dokumentieren, die sie im Code gefunden haben, inklusive einer Beschreibung, wie der Fehler reproduziert werden kann.
- **Feature-Anfragen**: Vorschläge für neue Funktionen oder Erweiterungen können als Issue eingereicht werden, um Interesse und Machbarkeit zu diskutieren.
- **Fragen und Diskussionen**: Bei Unklarheiten oder für den Austausch von Ideen können Issues genutzt werden, um Fragen zu stellen und Diskussionen zu führen.
- **Dokumentationsverbesserungen**: Hinweise auf fehlende oder unklare Dokumentationsteile können ebenfalls als Issues gemeldet werden.

**Befehle Issue:**

- **Issue erstellen**:

  ```sh
  gh issue create --title "<Titel>" --body "<Beschreibung>"
  gh issue create --title "Ein neues Problem" --body "Eine detaillierte Beschreibung des Problems."
  ```

- **Issues auflisten**:

  ```sh
  gh issue list
  ```

- **Issue anzeigen**:

  ```sh
  gh issue view <issue-number>
  gh issue view 1
  ```

```bash
# Terminal:
ls
README.md   hello-world

git lg
* f8e56f1 (HEAD -> main, origin/main) first commit

git push
Everything up-to-date

gh issue create --title "Ein neues Problem" --body "Eine detaillierte Beschreibung des Problems."

Creating issue in ju1-eu/mein-neues-repo

https://github.com/ju1-eu/mein-neues-repo/issues/1

gh issue list

Showing 1 of 1 open issue in ju1-eu/mein-neues-repo

ID  TITLE              LABELS  UPDATED
#1  Ein neues Problem          less than a minute ago

gh issue view 1
Ein neues Problem #1
Open • ju1-eu opened less than a minute ago • 0 comments
  Eine detaillierte Beschreibung des Problems.
View this issue on GitHub: https://github.com/ju1-eu/mein-neues-repo/issues/1
```

# Issues und Meilensteine

**GitHub CLI api** <https://cli.github.com/manual/gh_api>

GitHub CLI bringt GitHub auf Ihr Terminal <https://cli.github.com/> `brew install gh`

- **Meilensteine auflisten**: Nutzen Sie `gh api` mit den entsprechenden Headern, um alle Meilensteine in einem Repository zu listen. Ersetzen Sie die Platzhalter durch Ihre spezifischen Daten.

- **Erstellen eines Meilensteins**: Senden Sie eine POST-Anfrage über `gh api`, um einen neuen Meilenstein mit Titel, Status, Beschreibung und Fälligkeitsdatum zu erstellen.

- **Aktualisieren eines Meilensteins**: Verwenden Sie die Meilenstein-Nummer, um diesen mit einer PATCH-Anfrage zu aktualisieren. Ändern Sie Titel, Status, Beschreibung und Fälligkeitsdatum nach Bedarf.

- **Issues einem Meilenstein zuordnen**:
  - Listen Sie zuerst alle Issues auf.
  - Erstellen Sie Issues mit dem `gh issue create` Befehl.
  - Ordnen Sie bei der Erstellung eines Issues diesem direkt einen Meilenstein zu. Stellen Sie sicher, dass der Meilenstein bereits existiert.

- **Meilensteinfortschritt verfolgen**: Verwenden Sie `gh issue list` mit dem Meilenstein-Parameter, um den Fortschritt zu überwachen.

- **Issues schließen**: Löschen Sie ein Issue direkt über `gh issue delete` mit der entsprechenden Issue-ID.

- **Einen Meilenstein löschen**: Löschen Sie Meilensteine mit der DELETE-Methode über `gh api`, indem Sie die Meilenstein-Nummer angeben.

**Meilensteine listen:**

```bash
gh api \
	-H "Accept: application/vnd.github+json" \
	-H "X-GitHub-Api-Version: 2022-11-28" \
	/repos/ju1-eu/mein-neues-repo/milestones

gh issue list
```

**Einen Meilenstein erstellen:**

```bash
gh api \
	--method POST \
	-H "Accept: application/vnd.github+json" \
	-H "X-GitHub-Api-Version: 2022-11-28" \
	/repos/ju1-eu/mein-neues-repo/milestones \
	-f title='Meilenstein 3' \
	-f state='open' \
	-f description='Tracking milestone for version 1.1' \
	-f due_on='2024-10-09T23:39:01Z'
```

**Einen Meilenstein aktualisieren:**

```bash
# Milestone-Nummer "number": 6
gh api \
	--method PATCH \
	-H "Accept: application/vnd.github+json" \
	-H "X-GitHub-Api-Version: 2022-11-28" \
	/repos/ju1-eu/mein-neues-repo/milestones/6 \
	-f title='Meilenstein 3' \
	-f state='open' \
	-f description='update Tracking milestone for version 1.1' \
	-f due_on='2024-10-30T23:39:01Z'
```

**Issues einem Meilenstein zuordnen:**

```bash
# Listen Sie alle Issues auf
# issue ID: 6
gh issue list

# issue erstellen
gh issue create --title "Ein neues Problem" --body "Eine detaillierte Beschreibung des Problems."

# issue erstellen und MEILENSTEIN zuordnen
# HINWEIS: Einen Meilenstein vorher erstellen
gh issue create --title "Mein Issue" --body "weitere Details." --assignee ju1-eu --label "bug" --milestone "Meilenstein 3"
```

**Meilensteinfortschritt verfolgen:**

```bash
# MEILENSTEIN:
gh issue list --milestone "Meilenstein 3"
```

**issues schließen:**

```bash
# issue ID: 6
gh issue list

# issue löschen ID
gh issue delete 6 --yes
```

**Einen Meilenstein löschen:**

```bash
# Milestone-Nummer "number": 5
gh api \
	--method DELETE \
	-H "Accept: application/vnd.github+json" \
	-H "X-GitHub-Api-Version: 2022-11-28" \
	/repos/ju1-eu/mein-neues-repo/milestones/6
```
