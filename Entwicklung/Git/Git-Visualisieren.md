---
thema: "Git-Visualisieren"
runningtitle: "Git-Visualisieren"
keywords: ""
abstract: |
	Git ist ein mächtiges Werkzeug für die Softwareentwicklung, das Teams ermöglicht, effizient zusammenzuarbeiten und den Code-Entwicklungsprozess zu verwalten. Im Herzen jedes Git-Projekts steht das \textbf{Repository}, ein spezieller Ordner, der den gesamten Code und die Änderungshistorie beinhaltet. Um an einem Projekt mitzuarbeiten, beginnen Entwickler oft mit einem \textbf{Clone}, einer lokalen Kopie des Repositories. Innerhalb dieses Repositories können sie über \textbf{Branches} parallel an verschiedenen Features oder Bugfixes arbeiten, ohne die Hauptentwicklungslinie zu beeinträchtigen. \textbf{Commits} zeichnen Änderungen auf und dienen als Checkpoints. Sobald die Arbeit in einem Branch abgeschlossen ist, kann dieser mit einem \textbf{Merge} in den Hauptbranch integriert werden. Für die Zusammenarbeit mit externen Repositories bieten \textbf{Forks} eine Kopie des Original-Repositories, auf der unabhängig gearbeitet werden kann. \textbf{Pull Requests} fördern die Diskussion über Änderungen, bevor diese in das Hauptprojekt eingefügt werden. Git hilft auch bei der \textbf{Konfliktlösung}, wenn beim Mergen Widersprüche auftreten. Dieser Leitfaden erleichtert den Einstieg in die Nutzung von Git und unterstreicht dessen Bedeutung für die moderne Softwareentwicklung.

	\section*{Schlüsselwörter und Erklärungen}

	\begin{description}
		\item[Repository] Ein digitales Verzeichnis, das den Code und die Änderungshistorie eines Projekts speichert.
		\item[Clone] Eine lokale Kopie eines Git-Repositories, die es erlaubt, Änderungen am Projekt vorzunehmen.
		\item[Branch] Eine unabhängige Entwicklungslinie innerhalb eines Repositories, die parallele Arbeit an verschiedenen Features ermöglicht.
		\item[Commit] Ein "Snapshot" der Änderungen im Repository, der Autor, Nachricht und Änderungen beinhaltet.
		\item[Push] Das Hochladen von lokalen Änderungen an ein Remote-Repository.
		\item[Pull] Das Herunterladen und Integrieren von Änderungen aus einem Remote-Repository in das lokale Repository.
		\item[Merge] Das Zusammenführen von Änderungen aus verschiedenen Branches in einen einzigen Entwicklungsstrang.
		\item[Pull Request/Merge Request] Eine Anfrage, Änderungen aus einem Branch oder Fork in das Hauptprojekt zu integrieren, die eine Diskussion und Überprüfung ermöglicht.
		\item[Conflict] Eine Situation, die auftritt, wenn Git die Änderungen aus verschiedenen Branches nicht automatisch zusammenführen kann.
		\item[Fork] Eine Kopie eines Repositories auf einer Plattform wie GitHub, die es ermöglicht, unabhängig an Änderungen zu arbeiten und diese später durch Pull Requests vorzuschlagen.
	\end{description}
author: 'ju'
date: \today
---
<!-------------------------------------------------------------------------------------------------------------
ju 2024-03-06 Git-Visualisieren.md
pandoc Git-Visualisieren.md -o Git-Visualisieren.html -c navigation.css --mathjax --citeproc --bibliography=literatur.bib --csl=zitierstil-number.csl

Quelle [@spanner:2019:robotik].

Fußnote.[^1]
[^1]: Text der Fußnote.

[Google](https://www.google.com)

![Logo 2](images/Logo/Logo2.pdf)

**Tabelle 1:** Beschreibung

pandoc Git-Visualisieren.md --to latex --output Git-Visualisieren.tex --template=vorlage-main.tex --lua-filter=combined-filter.lua
pdflatex Git-Visualisieren.tex
biber Git-Visualisieren
pdflatex Git-Visualisieren.tex
pdflatex Git-Visualisieren.tex

ChatGPT:

Zusammenfassung in Latex: Schreibstil: Expositorisch ohne Form du/sie
Erstellen Sie eine kurze (ca. 200 Wörter) und ansprechende Zusammenfassung zum nachfolgenden Text. Die Zusammenfassung sollte für jemanden ohne wissenschaftlichen Hintergrund verständlich sein und gleichzeitig die wichtigsten Fakten genau wiedergeben. Beachte den Zusammenhang. Textinhalt: " "

Keywords: Erstelle mir eine Liste der wichtigsten Keywords zum Textinhalt.

Erklärung in Latex: Erkläre die Schlüsselwörter. Bereite die Antwort gehirngerecht auf mit Didaktische Reduktion.

neue Infos: Erklären Sie einem Gymnasiasten, der sich mit Programmierung beschäftigt, das Konzept von Git.

Gedankenkette: Könnten Sie kurz das Konzept von Git erläutern? Wie beeinflusst Git die Programmiersprache und in welchen Zusammenhang steht es?

Kognitives Prüfmuster: Wenn ich eine Frage zu Git stelle, teilen Sie sie in drei kleinere Fragen auf, die Ihnen helfen, eine genauere Antwort zu geben. Kombinieren Sie die Antworten auf diese Unterfragen, um die endgültige Antwort zu erhalten.

Rolle: Nehmen Sie die Rolle eines erfahrenen Programmierexperten an. Führen Sie anhand dieser Person ein Codeüberprüfung durch.

Zusammenfassung: Thema: C - Programmierung
Schreibstil: Expositorisch ohne Form du/sie, verwende Markdown
Erstelle eine ansprechende Zusammenfassung zum nachfolgenden Text in Aufzählungsform und gleichzeitig gebe die wichtigsten Informationen genau wieder. Bereite die Antwort gehirngerecht auf mit Didaktische Reduktion.
Textinhalt: " "

Fragen: Erstelle 5x Fragen zum Lerninhalt (beachte den Focus: tieferes Verständnis und kritisches Denken zu fördern) mit Lösung. Lerninhalt: " "

Projekt: Erstelle ein Projekt zum Anwenden des gelernten mit Lösung.
---------------------------------------------------------------------------------------------------------------->

# Git-Begriffe

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

**Arbeitsverzeichnis - Staging-Bereich - Lokales Repository - Remote-Repository:**

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

**Aktualisierungen holen und integrieren:**

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

**Branching und Mergin:**

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

**Änderungen in der Arbeitskopie rückgängig machen:**

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

**Gestagede Änderungen rückgängig machen:**

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

**Letzten Commit rückgängig machen:**

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

**Änderungen an einer Datei rückgängig machen:**

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

**Einen früheren Commit wiederherstellen:**

```plaintext
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

\newpage

# Git C-Entwicklung

Datei-Löschungen committen und den Stand Ihres lokalen Branches main auf den neuesten Stand mit dem Remote-Repository bringen.

```bash
# Terminal:
git add -A
git commit -m "Entferne ignorierte Dateien aus dem Repository"
git push origin main
```

```plaintext
Arbeitsverzeichnis      Staging-Bereich       Lokales Repository     Remote-Repository
       |                       |                       |                      |
       |  Änderungen im        |                       |                      |
       |  Arbeitsverzeichnis   |                       |                      |
       |  identifizieren       |                       |                      |
       |  (gelöschte und       |                       |                      |
       |  modifizierte         |                       |                      |
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
