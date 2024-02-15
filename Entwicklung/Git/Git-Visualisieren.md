---
title: "Git-Visualisieren"
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!-----------------------------------------------------------------------
ju 9-2-24 Git-Visualisieren.md
pandoc Git-Visualisieren.md -o Git-Visualisieren.html -c inhalt.css --mathjax
------------------------------------------------------------------------->
# Git-Visualisieren

## Git-Begriffe

Git ist ein unverzichtbares Werkzeug im modernen Softwareentwicklungs-Workflow, das die Zusammenarbeit und Versionierung von Code vereinfacht.

1. **Repository (Repo)**: Ein Repository ist ein Speicherort für dein Projekt. Es enthält alle Dateien und den Verlauf ihrer Änderungen. Du kannst ein lokales Repository auf deinem Computer haben und ein Remote-Repository auf einem Server wie GitHub, GitLab oder Bitbucket.

2. **Clone**: Wenn du mit einem bestehenden Repository arbeiten möchtest, beginnst du damit, es zu "klonen", d.h., du erstellst eine lokale Kopie des Repositories auf deinem Computer. So kannst du Änderungen vornehmen, ohne das Original zu beeinträchtigen.

3. **Branch**: Ein Branch erlaubt es dir, von der Hauptentwicklungslinie (meistens "main" oder "master" genannt) abzuzweigen, um neue Features oder Bugfixes zu entwickeln. So können mehrere Entwickler gleichzeitig an unterschiedlichen Aspekten eines Projekts arbeiten, ohne sich gegenseitig zu stören.

4. **Commit**: Ein Commit ist eine Aufzeichnung der Änderungen, die du an Dateien in deinem Repository vorgenommen hast. Jeder Commit hat eine eindeutige ID und speichert Informationen über den Autor, das Datum und eine Nachricht, die die Änderungen beschreibt.

5. **Push**: Nachdem du Commits lokal in deinem Branch gemacht hast, kannst du diese Änderungen "pushen", um sie in das Remote-Repository hochzuladen. So sind deine Änderungen für andere Teammitglieder sichtbar.

6. **Pull**: bezieht sich auf die Aktion, Änderungen aus einem Remote-Repository in dein lokales Repository zu integrieren. Mit dem Befehl git pull holst du dir die neuesten Commits aus einem Remote-Branch und führst diese automatisch in deinen aktuellen lokalen Branch ein. Diese Operation ist eine Kombination aus git fetch, das die neuesten Informationen aus dem Remote-Repository holt, und git merge, das diese Änderungen in deinen lokalen Arbeitsbereich integriert.

7. **Merge**: Wenn du fertig bist mit der Arbeit in einem Branch, kannst du ihn "mergen", d.h. die Änderungen in den Hauptbranch (z.B. "main") überführen. Das Zusammenführen vereint die Entwicklungsstränge und integriert deine Änderungen in das Projekt.

8. **Pull Request (PR) / Merge Request (MR)**: ist ein Begriff, der vor allem auf GitHub und ähnlichen Plattformen verwendet wird. Ein Pull Request ist eine Anfrage, die du an das Team des Original-Repositories (oder an den Besitzer) sendest, in der du vorschlägst, Änderungen aus deinem Fork oder Branch in den Hauptbranch des Original-Repositories zu übernehmen. Ein PR öffnet eine Diskussion um deine Änderungen, und es ist üblich, dass diese vor der Integration überprüft, kommentiert und eventuell angepasst werden müssen. PRs sind ein zentraler Bestandteil des kollaborativen Entwicklungsprozesses, da sie Code-Reviews und Diskussionen über vorgeschlagene Änderungen ermöglichen.

9. **Conflict**: Ein Konflikt tritt auf, wenn Git nicht automatisch Änderungen in unterschiedlichen Branches zusammenführen kann, weil an denselben Dateien oder Zeilen gearbeitet wurde. Konflikte müssen manuell gelöst werden, bevor der Merge abgeschlossen werden kann.

10. **Fork**: Ein Fork ist eine Kopie eines Repositories auf einem Server. Forks werden oft verwendet, um an Projekten beizutragen, zu denen man keinen direkten Schreibzugriff hat. Du kannst Änderungen in deinem geforkten Repository vornehmen und dann einen Pull Request stellen, um sie in das ursprüngliche Repository einzubringen.

# Git-Arbeitsablauf

**Arbeitsverzeichnis - Staging-Bereich - Lokales Repository - Remote-Repository**

```plaintext
#  Git-Arbeitsablauf
Arbeitsverzeichnis (Working Directory)
        |
        | git add <dateien> / git add .
        V
Staging-Bereich (Index / Stage)
        |
        | git commit -m "Nachricht"
        V
Lokales Repository (Local Repo)
        |
        | git push
        V
Remote-Repository (Remote Repo)
```

**Aktualisierungen holen und integrieren**

```plaintext
# Aktualisierungen holen und integrieren:
Remote-Repository (Remote Repo)
        |
        | git fetch
        V
Fetch-Kopie im Lokalen Repo (Nicht automatisch gemerged)
        |
        | git merge ORIGIN/BRANCH
        V
Lokales Repository (Local Repo) [nach git fetch + git merge]
        |
        | git pull
        V
Lokales Repository (Local Repo) [nach git pull, automatisch gemerged]
```

**Branching und Mergin**

```plaintext
# Branching und Merging:
Erstellen eines neuen Branches
        |
        | git branch NEW-BRANCH
        V
Neuer Branch (NEW-BRANCH) erstellt, parallel zu Main
        |
        | git checkout NEW-BRANCH
        V
Arbeit in NEW-BRANCH -> Commit Änderungen in NEW-BRANCH
        |
        | git checkout MAIN
        | (Wechsel zurück zum Hauptbranch)
        |
        | git merge NEW-BRANCH
        V
MAIN-Branch (inklusive der Änderungen aus NEW-BRANCH)
```

# Änderungen rückgängig machen

**Änderungen in der Arbeitskopie rückgängig machen**

```plaintext
# Änderungen in der Arbeitskopie rückgängig machen
Arbeitsverzeichnis (Working Directory)
         |
         | (Bearbeitungen)
         |
         V
+----------------------+          +--------------------+
| Einzelne Dateien     |          | Alle Änderungen    |
| rückgängig machen    |          | rückgängig machen  |
+----------------------+          +--------------------+
         |                                     |
         | git restore <dateiname>             | git restore .
         V                                     V
     Arbeitskopie                         Arbeitskopie
    (Einzelne Datei                      (Alle Änderungen
     zurückgesetzt)                      zurückgesetzt)
```

**Gestagede Änderungen rückgängig machen**

```plaintext
# Gestagede Änderungen rückgängig machen
Staging-Bereich (Index)
         |
         | (Staging mit git add)
         |
         V
+------------------------+
| Gestagede Änderungen   |
| rückgängig machen      |
+------------------------+
         |
         | git restore --staged <dateiname>
         | oder
         | git restore --staged . (alle Änderungen)
         V
     Staging-Bereich
    (Änderungen entfernt)
```

**Letzten Commit rückgängig machen**

```plaintext
# Letzten Commit rückgängig machen
Lokales Repository (Commits)
         |
         | (Commit mit git commit)
         |
         V
+--------------------------+
| Letzten Commit ändern,   |
| aber Änderungen behalten |
+--------------------------+
         |
         | git reset --soft HEAD~1
         V
     Arbeitskopie und
     Staging-Bereich
    (Änderungen zum erneuten
     Commit bereit)

+--------------------------+
| Letzten Commit und       |
| Änderungen verwerfen     |
+--------------------------+
         |
         | git reset --hard HEAD~1
         V
     Lokales Repository
    (Zurück zum vorherigen
     Zustand, Änderungen verworfen)
```

**Änderungen an einer Datei rückgängig machen**

```plaintext
# Änderungen an einer Datei rückgängig machen
+----------------------------+
| Änderungen an einer Datei  |
| rückgängig machen          |
+----------------------------+
         |
         | git restore <dateiname>
         V
     Arbeitskopie
    (Datei zurückgesetzt)
```

**Einen früheren Commit wiederherstellen**

```
# Einen früheren Commit wiederherstellen
+----------------------------+
| Einen früheren Commit      |
| wiederherstellen           |
+----------------------------+
         |
         | git revert <commit-hash>
         V
     Lokales Repository
    (Neuer Commit, der die
     Änderungen des angegebenen
     Commits rückgängig macht)
```

\newpage
# Python-Entwicklung

1. **Repository erstellen auf GitHub**: Startpunkt des Projekts, wo das zentrale Remote-Repository angelegt wird.
2. **Lokales Arbeiten und Branching**: Klonen des Repositories für eine lokale Arbeitskopie und Festlegen einer Branching-Strategie.
3. **Entwicklung und Commits**: Erstellen neuer Branches für Features oder Fixes, Durchführung atomarer Commits mit prägnanten Nachrichten.
4. **Zusammenarbeit und Integration mit PRs**: Erstellen von Pull Requests für die Integration der Änderungen in den `main`-Branch, Durchführung von Code-Reviews und Konfliktlösung.
5. **Aktualisierung und Wartung**: Regelmäßiges Aktualisieren des lokalen `main`-Branches mit `git pull`, Markierung von Releases mit Git-Tags.
6. **Forks und Beiträge**: Bearbeitung von Forks und Pull Requests von der Community, Erweiterung der `CONTRIBUTING.md` für klare Beitragshinweise.
7. **GitHub Actions und Issues**: Nutzung von GitHub-spezifischen Werkzeugen für CI/CD-Prozesse und das Tracking von Aufgaben, Features und Bugs.

![Git Python-Entwicklung](images/Git-Python-Entwicklung.pdf)

\newpage
# Git Fork

1. **Forken des Repositorys**: Erstelle eine eigene Kopie des Ziel-Repositorys auf GitHub.
2. **Klonen des Forks**: Hole den Code deines Forks auf deinen lokalen Computer.
3. **Erstellen eines neuen Branches**: Trenne deine Änderungen vom Hauptentwicklungszweig.
4. **Vornehmen von Änderungen und Commit**: Arbeite am Code und sichere deine Änderungen.
5. **Pushen des Branches zu deinem Fork**: Lade deine Änderungen auf GitHub hoch.
6. **Erstellen eines Pull Requests**: Beantrage die Integration deiner Änderungen in das Hauptprojekt.
7. **Kommunikation und Feedback**: Diskutiere mit den Projektverantwortlichen über deine Änderungen.
8. **Endgültige Überprüfung und Genehmigung**: Warte auf die Genehmigung deines Beitrags.
9. **Merge des Pull Requests**: Deine Änderungen werden in das Hauptprojekt integriert.
10. **Aufräumen nach dem Merge**: Entferne deinen Feature-Branch nach dem erfolgreichen Merge.
11. **Synchronisiere deinen Fork**: Halte deinen Fork auf dem neuesten Stand mit dem Haupt-Repository.

![Git Fork](images/Git-Fork.pdf)


# Git C-Entwicklung

Datei-Löschungen committen und den Stand Ihres lokalen Branches main auf den neuesten Stand mit dem Remote-Repository bringen.

```bash
git add -A
git commit -m "Entferne ignorierte Dateien aus dem Repository"
git push origin main
```

```plaintext
Arbeitsverzeichnis      Staging-Bereich       Lokales Repository     Remote-Repository
       |                       |                       |                      |
       |  Änderungen im        |                       |                      |
       |  Arbeitsverzeichnis   |                       |                      |
       |  identifizieren        |                       |                      |
       |  (gelöschte und       |                       |                      |
       |  modifizierte          |                       |                      |
       |  Dateien)             |                       |                      |
       |                       |                       |                      |
       +---------------------->+                       |                      |
       |  git add -A           |                       |                      |
       |  (Änderungen zum      |                       |                      |
       |  Commit vormerken)    |                       |                      |
       |                       |                       |                      |
       |                       +---------------------->+                      |
       |                       |  git commit -m "Ent-  |                      |
       |                       |  ferne ignorierte     |                      |
       |                       |  Dateien aus dem      |                      |
       |                       |  Repository"          |                      |
       |                       |                       |                      |
       |                       |                       +--------------------->+
       |                       |                       |  git push origin main|
       |                       |                       |  (Änderungen zum     |
       |                       |                       |  Remote-Repository   |
       |                       |                       |  pushen)             |
       |                       |                       |                      |
```
