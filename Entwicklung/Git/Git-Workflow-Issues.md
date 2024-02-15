---
title: "Git-Workflow-Issues"
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!-----------------------------------------------------------------------
ju 9-2-24 Git-Workflow-Issues.md
pandoc Git-Workflow-Issues.md -o Git-Workflow-Issues.html -c inhalt.css --mathjax
------------------------------------------------------------------------->
# Git Workflow - Issues


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


### Priorisieren von Issues

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

### Bearbeiten von Issues

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

### Issues schließen

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

**Befehle Issue**

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
# ======================================================================
Terminal: >_ ls
README.md   hello-world

Terminal: >_ git lg
* f8e56f1 (HEAD -> main, origin/main) first commit

Terminal: >_ git push
Everything up-to-date

Terminal: >_ gh issue create --title "Ein neues Problem" --body "Eine detaillierte Beschreibung des Problems."

Creating issue in ju1-eu/mein-neues-repo

https://github.com/ju1-eu/mein-neues-repo/issues/1

Terminal: >_ gh issue list

Showing 1 of 1 open issue in ju1-eu/mein-neues-repo

ID  TITLE              LABELS  UPDATED
#1  Ein neues Problem          less than a minute ago

Terminal: >_ gh issue view 1
Ein neues Problem #1
Open • ju1-eu opened less than a minute ago • 0 comments


  Eine detaillierte Beschreibung des Problems.


View this issue on GitHub: https://github.com/ju1-eu/mein-neues-repo/issues/1
```


# Issues und Meilensteine

**GitHub CLI api** <https://cli.github.com/manual/gh_api>

GitHub CLI bringt GitHub auf Ihr Terminal <https://cli.github.com/>

`brew install gh`

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


**Meilensteine listen**

```bash
gh api \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  /repos/ju1-eu/mein-neues-repo/milestones

gh issue list
```

**Einen Meilenstein erstellen**

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

**Einen Meilenstein aktualisieren**

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

**Issues einem Meilenstein zuordnen**

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

**Meilensteinfortschritt verfolgen**

```bash
# MEILENSTEIN:
gh issue list --milestone "Meilenstein 3"
```

**issues schließen**

```bash
# issue ID: 6
gh issue list

# issue löschen ID
gh issue delete 6 --yes
```

**Einen Meilenstein löschen**


```bash
# Milestone-Nummer "number": 5
gh api \
  --method DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  /repos/ju1-eu/mein-neues-repo/milestones/6
```

