---
thema: "GitHub-Management mit der GitHub CLI"
runningtitle: "GitHub CLI"
keywords: ""
abstract: |
	Der Umgang mit GitHub-Projekten wird durch die GitHub CLI (Command Line Interface) vereinfacht, welche die Steuerung verschiedener Aspekte eines GitHub-Kontos direkt aus dem Terminal ermöglicht. Wesentliche Funktionen wie das Erstellen von Issues, das Vorschauen von Markdown-Dateien, das Überprüfen von Authentifizierungsstatus, und das Verwalten von Repositories erleichtern den Workflow erheblich.

	\section*{GitHub CLI Funktionen}

	\begin{itemize}
		\item \textbf{Authentifizierungsstatus}: Mit \texttt{gh auth status} kann man schnell die eigenen Anmeldeinformationen und Token-Berechtigungen überprüfen. Dies umfasst Scopes wie \texttt{delete\_repo}, \texttt{gist}, \texttt{read:org}, \texttt{repo}, \texttt{workflow}, und \texttt{write:discussion}.
		\item \textbf{Benutzerinformationen}: \texttt{gh api user} liefert detaillierte Informationen über das Benutzerkonto, einschließlich Benutzername, ID, URLs zu Profil und Ressourcen, sowie Daten zu öffentlichen Repositories und Aktivitäten.
		\item \textbf{Repository-Liste}: Mit \texttt{gh repo list} erhält man eine Übersicht aller Repositories des angemeldeten Benutzerkontos, inklusive Status und Aktualisierungsdatum.
	\end{itemize}

	\section*{Entwicklung und Repository-Management}

	Die GitHub CLI unterstützt effizientes Branch-Management, das Klonen und Löschen von Repositories, sowie das Handling von unversionierten Dateien. Es wird ermöglicht, Änderungen gezielt zu commiten, Pull Requests zu erstellen und zu mergen, und somit einen nahtlosen Entwicklungsprozess zu gewährleisten. Zudem erleichtert die CLI die Bearbeitung von \texttt{.gitignore}-Dateien und die korrekte Einbindung von Submodulen.

	\section*{Schlüsselwörter}

	\begin{itemize}
		\item \textbf{GitHub CLI}: Eine Kommandozeilenanwendung, die es ermöglicht, GitHub-Funktionen direkt aus dem Terminal ohne Nutzung eines Web-Browsers zu steuern.
		\item \textbf{Authentifizierungsstatus}: Überprüfung der Anmeldeinformationen und der Zugriffsrechte eines Benutzers auf GitHub, um die korrekte Konfiguration und die zugewiesenen Berechtigungen zu bestätigen.
		\item \textbf{Token-Berechtigungen}: Spezifische Zugriffsrechte, die einem Token zugewiesen sind, erlauben unterschiedliche Aktionen auf GitHub, wie das Löschen von Repositories oder das Lesen von Organisationsdaten.
		\item \textbf{Repository (Repo)}: Ein Projektverzeichnis auf GitHub, das alle zugehörigen Dateien, den Verlauf ihrer Änderungen, und zusätzliche Metadaten enthält.
		\item \textbf{Branch}: Eine parallele Version eines Repositories, die es ermöglicht, unabhängig von der Hauptentwicklungslinie (main oder master) an Änderungen, neuen Features oder Fixes zu arbeiten.
		\item \textbf{Merge}: Der Prozess des Zusammenführens von Änderungen aus einem Branch in einen anderen, typischerweise von einem Feature-Branch in den Hauptbranch.
		\item \textbf{Pull Request (PR)}: Eine Anfrage auf GitHub, Änderungen aus einem Branch oder Fork eines Repositories in einen anderen Branch desselben Repositories zu integrieren, üblicherweise begleitet von einer Überprüfung der Änderungen.
		\item \textbf{.gitignore}: Eine Datei in einem Git-Repository, die Git anweist, bestimmte Dateien oder Verzeichnisse nicht zu verfolgen und somit aus dem Versionierungssystem auszuschließen.
		\item \textbf{Submodul}: Ein Repository innerhalb eines anderen Git-Repositories, das es ermöglicht, externe Quellen oder Abhängigkeiten als Teil des übergeordneten Projekts zu verwalten.
		\item \textbf{Commit}: Ein Satz von Änderungen an Dateien in einem Repository, der als einzelne Einheit gespeichert und mit einer eindeutigen ID versehen ist, um die Historie der Änderungen nachvollziehbar zu machen.
	\end{itemize}
author: 'ju'
date: \today
---
<!-------------------------------------------------------------------------------------------------------------
ju 2024-03-06 Git-Workflow-GitHub.md
pandoc Git-Workflow-GitHub.md -o Git-Workflow-GitHub.html -c navigation.css --mathjax --citeproc --bibliography=literatur.bib --csl=zitierstil-number.csl

Quelle [@spanner:2019:robotik].

Fußnote.[^1]
[^1]: Text der Fußnote.

[Google](https://www.google.com)

![Logo 2](images/Logo/Logo2.pdf)

**Tabelle 1:** Beschreibung

pandoc Git-Workflow-GitHub.md --to latex --output Git-Workflow-GitHub.tex --template=vorlage-main.tex --lua-filter=combined-filter.lua
pdflatex Git-Workflow-GitHub.tex
biber Git-Workflow-GitHub
pdflatex Git-Workflow-GitHub.tex
pdflatex Git-Workflow-GitHub.tex

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
# GitHub

<https://cli.github.com/manual/gh_issue_create>

<https://github.com/yusukebe/gh-markdown-preview>

`gh extension install yusukebe/gh-markdown-preview`

`gh markdown-preview README.md`

## gh auth status

Überblick über die Konfiguration und die Berechtigungen des GitHub-CLI-Tools für den angemeldeten Account.

- **Token-Berechtigungen**:
  - Der Token verfügt über folgende Berechtigungen (Scopes): `delete_repo`, `gist`, `read:org`, `repo`, `workflow`, `write:discussion`.

```bash
# Terminal:
gh auth status
github.com
  ✓ Logged in to github.com account ju1-eu (keyring)
  - Active account: true
  - Git operations protocol: https
  - Token: ghp_************************************
  - Token scopes: 'delete_repo', 'gist', 'read:org', 'repo', 'workflow', 'write:discussion'
```

## gh api user

Überblick über das GitHub-Benutzerkonto `ju1-eu`, einschließlich persönlicher Daten, Engagement auf der Plattform und Zugriffspunkte für weitere Informationen über API-Endpunkte.

- **Benutzerkonto und Identifikation**:
  - **Benutzername**: ju1-eu
  - **ID**: 16193593
  - **Node ID**: MDQ6VXNlcjE2MTkzNTkz

- **URLs und Ressourcen**:
  - **Avatar URL**: [https://avatars.githubusercontent.com/u/16193593?v=4](https://avatars.githubusercontent.com/u/16193593?v=4)
  - **Benutzerprofil**: [https://github.com/ju1-eu](https://github.com/ju1-eu)
  - **Follower**, **Following**, **Gists**, **Starred Repositories**, **Abonnements**, **Organisationen**, **Repositories** und **Events**: Spezifische URLs für das Konto sind verfügbar.

- **Kontotyp und Aktivitäten**:
  - **Typ**: User (nicht als Site Admin markiert)
  - **Öffentliche Repositories**: 19
  - **Öffentliche Gists**: 0
  - **Follower**: 0
  - **Following**: 0

- **Erstellungs- und Aktualisierungsdatum**:
  - **Erstellt am**: 2015-12-07
  - **Zuletzt aktualisiert**: 2024-02-06

- **Persönliche Informationen**
  - Name, Unternehmen, Blog, Standort, E-Mail, Verfügbarkeit zur Anstellung (hireable), Biografie, Twitter-Benutzername.

```bash
# Terminal:
gh api user
{
  "login": "ju1-eu",
  "id": 16193593,
  "url": "https://api.github.com/users/ju1-eu",
  "html_url": "https://github.com/ju1-eu",
  "created_at": "2015-12-07T16:16:27Z",
  "updated_at": "2024-02-06T08:50:59Z"
  ...
}
```

## gh repo list

Liste von Repositories, die dem GitHub-Benutzerkonto ju1-eu zugeordnet sind.

```bash
# Terminal:
gh repo list

Showing 20 of 20 repositories in @ju1-eu

NAME                            DESCRIPTION                         INFO     UPDATED
ju1-eu/testOrdner                                                   public   about 17 hours ago
ju1-eu/hello-world              Mein erstes Repository              public   about 25 days ago
...
```

## Entwicklungszweig dev - clone - create - delete Repositorys

- **Branch-Management und Wechsel**:
  - Anzeige vorhandener Branches (`dev`, `docs`, `main`), mit `dev` als aktivem Arbeitsbranch.
  - Wechsel zum Branch `dev` durchgeführt.

- **Klonen und Löschen eines Repositorys**:
  - Erfolgreiches Klonen des `hello-world` Repositorys von GitHub in das lokale Arbeitsverzeichnis.
  - Erstellung eines neuen öffentlichen Repositorys auf GitHub (`mein-neues-repo`) und anschließende Löschung desselben.

- **Umgang mit unversionierten Dateien**:
  - Feststellung, dass `.DS_Store` und `hello-world/` unversioniert sind.
  - Versuch, alle unversionierten Dateien zum Staging-Bereich hinzuzufügen, führt zur Warnung über das eingebettete Repository `hello-world`.

- **Bereinigung und korrekte Einbindung**:
  - Entfernung des `hello-world` Verzeichnisses aus dem Staging-Bereich, um es korrekt als Submodul hinzufügen zu können.
  - Bearbeitung der .gitignore-Datei, wahrscheinlich um `.DS_Store` zu ignorieren, und Entfernung von `.DS_Store` aus dem Staging-Bereich.

- **Integration eines Submoduls**:
  - Korrektes Hinzufügen von `hello-world` als Git-Submodul.
  - Staging von .gitignore und Einbindung der Änderungen in den nächsten Commit.

- **Commit, Pull und Push**:
  - Commit der Änderungen mit Hinweis auf die Integration von `hello-world` als Git-Submodul.
  - Versuch eines Pulls ohne Tracking-Informationen scheitert; anschließender Push des `dev`-Branches zu GitHub, wobei `dev` für Upstream-Tracking konfiguriert wird.
  - Bestätigung, dass der lokale und remote `dev`-Branch auf dem neuesten Stand sind.

- **Git History und Up-to-Date**:
  - Überprüfung der Git-Historie zeigt den aktuellen Stand und die erfolgreiche Integration des Submoduls.
  - Letzte Überprüfung bestätigt, dass keine weiteren Änderungen zum Pushen vorhanden sind.


```bash
# Terminal:
git branch
* dev
  docs
  main

git checkout dev

gh repo clone ju1-eu/hello-world
Klone nach 'hello-world'...
remote: Enumerating objects: 23, done.
remote: Counting objects: 100% (23/23), done.
remote: Compressing objects: 100% (17/17), done.
remote: Total 23 (delta 1), reused 19 (delta 0), pack-reused 0
Empfange Objekte: 100% (23/23), 6.06 KiB | 3.03 MiB/s, fertig.
Löse Unterschiede auf: 100% (1/1), fertig.

ls -a
.           ..          .DS_Store   .git        .gitignore  README.md   hello-world

gh repo create mein-neues-repo --public
✓ Created repository ju1-eu/mein-neues-repo on GitHub
  https://github.com/ju1-eu/mein-neues-repo

gh repo delete mein-neues-repo --yes
✓ Deleted repository ju1-eu/mein-neues-repo

git st
Auf Branch dev
Unversionierte Dateien:
  (benutzen Sie "git add <Datei>...", um die Änderungen zum Commit vorzumerken)
	.DS_Store
	hello-world/

nichts zum Commit vorgemerkt, aber es gibt unversionierte Dateien
(benutzen Sie "git add" zum Versionieren)

git add .
Warnung: Füge eingebettetes Repository hinzu: hello-world
Hinweis: 	git rm --cached hello-world
Hinweis:
Hinweis: See "git help submodule" for more information.

git rm -f --cached hello-world

vim .gitignore

git rm --cached .DS_Store

git submodule add https://github.com/ju1-eu/hello-world.git hello-world

Füge existierendes Repository in 'hello-world' dem Index hinzu

git add .gitignore

git st
Auf Branch dev
Zum Commit vorgemerkte Änderungen:
  (benutzen Sie "git restore --staged <Datei>..." zum Entfernen aus der Staging-Area)
	geändert:       .gitignore
	neue Datei:     .gitmodules
	neue Datei:     hello-world

git commit -a
[dev dada445] git repo als gitmodul hinzugefügt auf dev
 3 files changed, 7 insertions(+)
 create mode 100644 .gitmodules
 create mode 160000 hello-world

git lg
* dada445 (HEAD -> dev) git repo als gitmodul hinzugefügt auf dev
* 7c9e651 (docs) readme änderungen hinzugefügt
* 65331ed gitignore
* b4a0efa first commit

git pull
Es gibt keine Tracking-Informationen für den aktuellen Branch.
Bitte geben Sie den Branch an, gegen welchen Sie "rebase" ausführen möchten.
Siehe git-pull(1) für weitere Details.

    git pull <Remote-Repository> <Branch>

git push -u origin dev
Objekte aufzählen: 6, fertig.
Zähle Objekte: 100% (6/6), fertig.
Delta-Kompression verwendet bis zu 12 Threads.
Komprimiere Objekte: 100% (4/4), fertig.
Schreibe Objekte: 100% (4/4), 505 Bytes | 505.00 KiB/s, fertig.
Gesamt 4 (Delta 1), Wiederverwendet 0 (Delta 0), Pack wiederverwendet 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for 'dev' on GitHub by visiting:
remote:      https://github.com/ju1-eu/testOrdner/pull/new/dev
remote:
To https://github.com/ju1-eu/testOrdner.git
 * [new branch]      dev -> dev
Branch 'dev' folgt nun 'origin/dev'.

git pull
Bereits aktuell.

git push
Everything up-to-date

git lg
* dada445 (HEAD -> dev, origin/dev) git repo als gitmodul hinzugefügt auf dev
* 7c9e651 (docs) readme änderungen hinzugefügt
* 65331ed gitignore
* b4a0efa first commit
```

## Entwicklungszweig main - Statusüberprüfung, Bereinigung, Historie, Synchr. mit Remote-Repository

- **Branch-Übersicht und Auswahl**:
  - Anzeige der verfügbaren Branches mit `main` als aktiven Branch gekennzeichnet.
  - Versuch, zum Branch `main` zu wechseln, resultiert in einer Warnung, dass das Verzeichnis `hello-world` nicht entfernt werden kann, da es nicht leer ist. Der Wechsel zum Branch `main` wird dennoch erfolgreich durchgeführt.

- **Statusüberprüfung und Bereinigung**:
  - Der Statusbefehl zeigt an, dass sich der Branch `main` auf dem gleichen Stand wie `origin/main` befindet.
  - Das Verzeichnis `hello-world` wird als unversioniert aufgelistet.
  - Das Verzeichnis `hello-world` wird aus dem Arbeitsverzeichnis entfernt.
  - Eine erneute Statusüberprüfung bestätigt, dass keine Änderungen zum Commiten vorliegen und das Arbeitsverzeichnis unverändert ist.

- **Historie und Synchronisation mit Remote**:
  - Die Git-Historie (`git lg`) zeigt eine Liste der Commits auf dem Branch `main`, beginnend mit dem neuesten Commit.
  - Ein Versuch, den aktuellen Stand mit dem Remote-Repository zu synchronisieren (`git pull`), zeigt, dass bereits die aktuellste Version vorliegt.
  - Ein Push-Versuch (`git push`) bestätigt ebenfalls, dass keine weiteren Änderungen vorhanden sind und der lokale Branch auf dem neuesten Stand mit dem Remote-Branch ist.

```bash
# Terminal:
git branch
  dev
  docs
* main

git checkout main
Warnung: unable to rmdir 'hello-world': Directory not empty
Zu Branch 'main' gewechselt
Ihr Branch ist auf demselben Stand wie 'origin/main'.

git st
Auf Branch main
Ihr Branch ist auf demselben Stand wie 'origin/main'.

Unversionierte Dateien:
  (benutzen Sie "git add <Datei>...", um die Änderungen zum Commit vorzumerken)
	hello-world/

nichts zum Commit vorgemerkt, aber es gibt unversionierte Dateien
(benutzen Sie "git add" zum Versionieren)

rm -rf hello-world
git st
Auf Branch main
Ihr Branch ist auf demselben Stand wie 'origin/main'.
nichts zu committen, Arbeitsverzeichnis unverändert

git lg
* 6580c23 (HEAD -> main, origin/main) gitignore
* 7c9e651 (docs) readme änderungen hinzugefügt
* 65331ed gitignore
* b4a0efa first commit

git pull
Bereits aktuell.

git push
Everything up-to-date
```

## Entwicklungszweig main - Bearbeitung gitignore, Commit, Synchr. mit dem Remote-Repository

- **Branch-Status und Wechsel**:
  - Der Befehl `git branch` zeigt die verfügbaren Branches, mit `main` als aktuellem Arbeitsbranch.
  - Bestätigung, dass der Branch `main` auf demselben Stand wie `origin/main` ist.

- **Bearbeitung und Status der .gitignore-Datei**:
  - Die .gitignore-Datei wird bearbeitet, um bestimmte Dateien oder Verzeichnisse von der Verfolgung durch Git auszuschließen.
  - `git st` (Status) zeigt Änderungen in .gitignore, die noch nicht zum Commit vorgemerkt sind.

- **Commit der Änderungen**:
  - Durchführung eines Commits mit der Option `-a`, die alle Änderungen von verfolgten Dateien commitet, einschließlich der Änderungen in .gitignore.
  - Nach dem Commit ist der lokale `main` Branch einen Commit voraus gegenüber `origin/main`.

- **Synchronisation mit dem Remote-Repository**:
  - Ein Versuch, den aktuellen Stand mit `git pull` zu aktualisieren, bestätigt, dass der Branch `main` bereits auf dem neuesten Stand ist.
  - Ausführung von `git push` überträgt den neuen Commit erfolgreich auf das Remote-Repository.

- **Überprüfung der Git-Historie**:
  - Der Befehl `git lg` (eine benutzerdefinierte Abkürzung für eine detaillierte Ansicht der Git-Log-Historie) zeigt die aktuelle Commit-Historie auf dem Branch `main`, einschließlich des jüngsten Commits zur .gitignore-Datei.

```bash
# Terminal:
git branch
  dev
  docs
* main

git checkout main
Zu Branch 'main' gewechselt
Ihr Branch ist auf demselben Stand wie 'origin/main'.

vim .gitignore

git st
Auf Branch main
Ihr Branch ist auf demselben Stand wie 'origin/main'.

Änderungen, die nicht zum Commit vorgemerkt sind:
  (benutzen Sie "git add <Datei>...", um die Änderungen zum Commit vorzumerken)
  (benutzen Sie "git restore <Datei>...", um die Änderungen im Arbeitsverzeichnis zu verwerfen)
	geändert:       .gitignore

keine Änderungen zum Commit vorgemerkt (benutzen Sie "git add" und/oder "git commit -a")

git commit -a
[main 34d1fd8] gitignore
 1 file changed, 2 insertions(+), 2 deletions(-)

git st
Auf Branch main
Ihr Branch ist 1 Commit vor 'origin/main'.
  (benutzen Sie "git push", um lokale Commits zu publizieren)
nichts zu committen, Arbeitsverzeichnis unverändert

git pull
Aktueller Branch main ist auf dem neuesten Stand.

git push
Objekte aufzählen: 5, fertig.
Zähle Objekte: 100% (5/5), fertig.
Delta-Kompression verwendet bis zu 12 Threads.
Komprimiere Objekte: 100% (3/3), fertig.
Schreibe Objekte: 100% (3/3), 320 Bytes | 320.00 KiB/s, fertig.
Gesamt 3 (Delta 1), Wiederverwendet 0 (Delta 0), Pack wiederverwendet 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/ju1-eu/testOrdner.git
   6580c23..34d1fd8  main -> main

git lg
* 34d1fd8 (HEAD -> main, origin/main) gitignore
* 6580c23 gitignore
* 7c9e651 (docs) readme änderungen hinzugefügt
* 65331ed gitignore
* b4a0efa first commit
```

## Entwicklungszweig docs - Merge

- **Branch-Überblick und Wechsel**:
  - Die verfügbaren Branches werden gelistet, mit `docs` als aktuell ausgewähltem Branch.
  - Ein Wechsel zum Branch `docs` wird durchgeführt, auch wenn `docs` bereits der aktive Branch ist, was die Bereitschaft zur Arbeit an der Dokumentation zeigt.

- **Merge-Operation**:
  - Durchführung eines Merge von `main` in `docs`, was die Aktualisierungen aus `main` in den `docs` Branch integriert.
  - Der Merge wird als Fast-forward ausgeführt, was darauf hinweist, dass keine separaten Entwicklungswege zusammengeführt werden müssen und die Historie linear bleibt.
  - Die Änderungen umfassen 3 neue Einträge in .gitignore.

- **Historische Übersicht**:
  - Die Git-Log-Historie (`git lg`) zeigt, dass der `docs` Branch nun die gleichen Commits wie `main` und `origin/main` enthält, einschließlich des jüngsten Commits zur .gitignore-Datei.


```bash
# Terminal:
git branch
  dev
* docs
  main

git checkout docs
Zu Branch 'docs' gewechselt

git merge main
Aktualisiere 7c9e651..34d1fd8
Fast-forward
 .gitignore | 3 +++
 1 file changed, 3 insertions(+)

git lg
* 34d1fd8 (HEAD -> docs, origin/main, main) gitignore
* 6580c23 gitignore
* 7c9e651 readme änderungen hinzugefügt
* 65331ed gitignore
* b4a0efa first commit
```

## Entwicklungszweig main - Merge und Konfliktlösung

- **Branch-Status und Wechsel**:
  - Anzeige der verfügbaren Branches, mit `main` als aktuell ausgewähltem Branch.
  - Wechsel zum Branch `main` bestätigt, dass dieser auf dem gleichen Stand wie `origin/main` ist.

- **Merge-Vorgang und Konfliktlösung**:
  - Versuch, Änderungen aus dem Branch `dev` in `main` zu integrieren, führt zu einem Konflikt in der Datei .gitignore.
  - Der Konflikt in .gitignore wird manuell bearbeitet und gelöst.

- **Statusüberprüfung und Commit**:
  - Nach der Konfliktlösung zeigt der Statusbefehl vorbereitete Änderungen für den Commit, einschließlich der Hinzufügung einer `.gitmodules` Datei und eines `hello-world` Verzeichnisses.
  - Der Konflikt wird durch einen Commit abgeschlossen, der die Integration der Änderungen aus `dev` in `main` markiert.

- **Synchronisation mit dem Remote-Repository**:
  - Nachdem der Merge abgeschlossen ist, zeigt eine Statusüberprüfung, dass der lokale `main` Branch zwei Commits vor `origin/main` liegt.
  - Ein Push überträgt die Änderungen erfolgreich auf das Remote-Repository.

- **Historische und strukturelle Übersicht**:
  - Die Git-Log-Historie (`git lg`) nach dem Push zeigt den Merge-Commit zusammen mit der Einbindung der Änderungen aus `dev`, einschließlich der spezifischen Commits, die in den Merge einbezogen wurden.

```bash
# Terminal:
git branch
  dev
  docs
* main

git checkout main
Zu Branch 'main' gewechselt
Ihr Branch ist auf demselben Stand wie 'origin/main'.

git merge dev
automatischer Merge von .gitignore
KONFLIKT (Inhalt): Merge-Konflikt in .gitignore
Automatischer Merge fehlgeschlagen; beheben Sie die Konflikte und committen Sie dann das Ergebnis.

vim .gitignore

git st
Auf Branch main
Ihr Branch ist auf demselben Stand wie 'origin/main'.

Sie haben nicht zusammengeführte Pfade.
  (beheben Sie die Konflikte und führen Sie "git commit" aus)
  (benutzen Sie "git merge --abort", um den Merge abzubrechen)

Zum Commit vorgemerkte Änderungen:
	neue Datei:     .gitmodules
	neue Datei:     hello-world

Nicht zusammengeführte Pfade:
  (benutzen Sie "git add/rm <Datei>...", um die Auflösung zu markieren)
	von beiden geändert:    .gitignore

git commit -a
[main f5fd94d] Merge branch 'dev'

git st
Auf Branch main
Ihr Branch ist 2 Commits vor 'origin/main'.
  (benutzen Sie "git push", um lokale Commits zu publizieren)

nichts zu committen, Arbeitsverzeichnis unverändert

git push
Objekte aufzählen: 4, fertig.
Zähle Objekte: 100% (4/4), fertig.
Delta-Kompression verwendet bis zu 12 Threads.
Komprimiere Objekte: 100% (2/2), fertig.
Schreibe Objekte: 100% (2/2), 370 Bytes | 370.00 KiB/s, fertig.
Gesamt 2 (Delta 0), Wiederverwendet 0 (Delta 0), Pack wiederverwendet 0
To https://github.com/ju1-eu/testOrdner.git
   34d1fd8..f5fd94d  main -> main

git lg
*   f5fd94d (HEAD -> main, origin/main) Merge branch 'dev'
|\
| * dada445 (origin/dev, dev) git repo als gitmodul hinzugefügt auf dev
* | 34d1fd8 (docs) gitignore
* | 6580c23 gitignore
|/
* 7c9e651 readme änderungen hinzugefügt
* 65331ed gitignore
* b4a0efa first commit
```

## Entwicklungszweig docs - Bearbeitung README und Commit der Änderungen und fehlendem Upstream-Branch

- **Branch-Auswahl und Arbeitsumgebung**:
  - Der `docs` Branch wurde als Arbeitsumgebung ausgewählt, um Änderungen an der Dokumentation vorzunehmen.
  - Ein Auflisten der Dateien im Arbeitsverzeichnis zeigt die typischen Verzeichniseinträge, einschließlich der `README.md`-Datei.

- **Bearbeitung und Commit der Änderungen**:
  - Die `README.md`-Datei wurde bearbeitet, um die Dokumentation zu aktualisieren.
  - Die durchgeführten Änderungen an der `README.md`-Datei wurden direkt mit einem Commit im `docs` Branch festgehalten.

- **Konfrontation mit fehlendem Upstream-Branch**:
  - Ein initialer Versuch, die Änderungen zu pushen, scheiterte aufgrund des Fehlens eines konfigurierten Upstream-Branches für `docs`.
  - Durch Setzen des Upstream-Branches mittels `git push --set-upstream origin docs` wurde das Problem behoben und der Push erfolgreich durchgeführt.

- **Ergebnis und Dokumentation des Fortschritts**:
  - Der `docs` Branch, inklusive der jüngsten Änderungen, wurde erfolgreich zum Remote-Repository gepusht.
  - Die Git-Log-Historie (`git lg`) bestätigt, dass der Commit `änderung docs` sowohl im lokalen als auch im Remote-Branch `docs` vorhanden ist.


```bash
# Terminal:
git branch
  dev
* docs
  main

git checkout docs
Zu Branch 'docs' gewechselt

ls -a
.          ..         .DS_Store  .git       .gitignore README.md

vim README.md

git st
Auf Branch docs
Änderungen, die nicht zum Commit vorgemerkt sind:
  (benutzen Sie "git add <Datei>...", um die Änderungen zum Commit vorzumerken)
  (benutzen Sie "git restore <Datei>...", um die Änderungen im Arbeitsverzeichnis zu verwerfen)
	geändert:       README.md

keine Änderungen zum Commit vorgemerkt (benutzen Sie "git add" und/oder "git commit -a")

git commit -a
[docs 294d6ec] änderung docs
 1 file changed, 2 insertions(+)

git st
Auf Branch docs
nichts zu committen, Arbeitsverzeichnis unverändert

git lg
* 294d6ec (HEAD -> docs) änderung docs
* 34d1fd8 gitignore
* 6580c23 gitignore
* 7c9e651 readme änderungen hinzugefügt
* 65331ed gitignore
* b4a0efa first commit

git push
Schwerwiegend: Der aktuelle Branch docs hat keinen Upstream-Branch.

git push --set-upstream origin docs
Objekte aufzählen: 5, fertig.
Zähle Objekte: 100% (5/5), fertig.
Delta-Kompression verwendet bis zu 12 Threads.
Komprimiere Objekte: 100% (3/3), fertig.
Schreibe Objekte: 100% (3/3), 326 Bytes | 326.00 KiB/s, fertig.
Gesamt 3 (Delta 1), Wiederverwendet 0 (Delta 0), Pack wiederverwendet 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for 'docs' on GitHub by visiting:
remote:      https://github.com/ju1-eu/testOrdner/pull/new/docs
remote:
To https://github.com/ju1-eu/testOrdner.git
 * [new branch]      docs -> docs
Branch 'docs' folgt nun 'origin/docs'.

git lg
* 294d6ec (HEAD -> docs, origin/docs) änderung docs
* 34d1fd8 gitignore
* 6580c23 gitignore
* 7c9e651 readme änderungen hinzugefügt
* 65331ed gitignore
* b4a0efa first commit
```

## Entwicklungszweig main - Merge

- **Branch-Überblick und Wechsel**:
  - Die vorhandenen Branches werden aufgelistet, mit `main` als dem aktuell ausgewählten Branch.
  - Der Wechsel zum Branch `main` bestätigt, dass dieser auf demselben Stand wie `origin/main` ist.

- **Zustand des Arbeitsverzeichnisses und Merge-Aktion**:
  - Ein Auflisten der Dateien im Arbeitsverzeichnis zeigt unter anderem `.DS_Store`, .gitignore, `.gitmodules`, `README.md` und ein `hello-world` Verzeichnis.
  - Ein Merge von `docs` in `main` führt zu Änderungen in `README.md`, mit zwei neuen Zeileneinfügungen.

- **Statusüberprüfung und Synchronisation mit Remote**:
  - Nach dem Merge zeigt der Statusbefehl, dass der lokale `main` Branch zwei Commits vor `origin/main` ist.
  - Ein Push überträgt die Merge-Änderungen erfolgreich auf das Remote-Repository.

- **Git-Log und README-Inhalt**:
  - Die Git-Log-Historie (`git lg`) zeigt den Merge-Commit von `docs` in `main` an der Spitze der Commit-Historie.
  - Der Inhalt von `README.md` umfasst eine Basisbeschreibung des Repositories sowie spezifische Änderungen, die sowohl auf dem iMac als auch im `docs` Branch vorgenommen wurden.


```bash
# Terminal:
git branch
  dev
  docs
* main

git checkout main
Zu Branch 'main' gewechselt
Ihr Branch ist auf demselben Stand wie 'origin/main'.

ls -a
.           ..          .DS_Store   .git        .gitignore  .gitmodules README.md   hello-world

git merge docs
Merge made by the 'ort' strategy.
 README.md | 2 ++
 1 file changed, 2 insertions(+)

git st
Auf Branch main
Ihr Branch ist 2 Commits vor 'origin/main'.
  (benutzen Sie "git push", um lokale Commits zu publizieren)
nichts zu committen, Arbeitsverzeichnis unverändert

git push
Objekte aufzählen: 4, fertig.
Zähle Objekte: 100% (4/4), fertig.
Delta-Kompression verwendet bis zu 12 Threads.
Komprimiere Objekte: 100% (2/2), fertig.
Schreibe Objekte: 100% (2/2), 370 Bytes | 370.00 KiB/s, fertig.
Gesamt 2 (Delta 0), Wiederverwendet 0 (Delta 0), Pack wiederverwendet 0
To https://github.com/ju1-eu/testOrdner.git
   f5fd94d..87a9b23  main -> main

git lg
*   87a9b23 (HEAD -> main, origin/main) Merge branch 'docs'
|\
| * 294d6ec (origin/docs, docs) änderung docs
* |   f5fd94d Merge branch 'dev'
|\ \
| |/
|/|
| * dada445 (origin/dev, dev) git repo als gitmodul hinzugefügt auf dev
* | 34d1fd8 gitignore
* | 6580c23 gitignore
|/
* 7c9e651 readme änderungen hinzugefügt
* 65331ed gitignore
* b4a0efa first commit

cat README.md
# testOrdner Repository
This is the README for the testOrdner repository.
Änderung von meinem iMac
Änderung auf docs
```

## Entwicklungszweig docs - Inhalt von README

- **Branch-Management**:
  - Eine Übersicht der vorhandenen Branches wird angezeigt, mit `docs` als dem aktuell ausgewählten Branch.
  - Der Nutzer wechselt explizit zum Branch `docs`, der bereits als der aktive Branch markiert ist.

- **Inhalt der Dokumentation**:
  - Der Befehl `cat README.md` wird verwendet, um den Inhalt der `README.md`-Datei anzuzeigen, die zur Dokumentation des `testOrdner`-Repositories dient.
  - Der Inhalt von `README.md` enthält eine grundlegende Beschreibung des Repositories sowie spezifische Änderungen, die vermerken, dass Bearbeitungen sowohl von einem iMac aus als auch im `docs`-Branch vorgenommen wurden.


```bash
# Terminal:
git branch
  dev
* docs
  main

git checkout docs
Zu Branch 'docs' gewechselt
Ihr Branch ist auf demselben Stand wie 'origin/docs'.

cat README.md
# testOrdner Repository
This is the README for the testOrdner repository.
Änderung von meinem iMac
Änderung auf docs
```

## Entwicklungszweig dev - Inhalt von README

```bash
# Terminal:
git branch
* dev
  docs
  main

git checkout dev
Zu Branch 'dev' gewechselt
Ihr Branch ist auf demselben Stand wie 'origin/dev'.

cat README.md
# testOrdner Repository
This is the README for the testOrdner repository.
Änderung von meinem iMac
```

## Entwicklungszweig main - Überblick

- **Branch-Überblick und Auswahl**:
  - Anzeige der verfügbaren Branches mit dem Fokus auf `main`, der als aktiver Branch gekennzeichnet ist.
  - Wechsel zum Branch `main` bestätigt, dass dieser auf demselben Stand wie `origin/main` ist.

- **Status und Historie**:
  - Der Statusbefehl (`git st`) zeigt an, dass im Branch `main` keine uncommitteten Änderungen vorliegen und das Arbeitsverzeichnis unverändert ist.
  - Die Git-Log-Historie (`git lg`) präsentiert eine Übersicht der Commits auf `main`, einschließlich Merges aus den Branches `docs` und `dev`. Es wird deutlich, dass Änderungen aus diesen Branches erfolgreich in `main` integriert wurden.

- **Wichtige Commits und Merges**:
  - Ein Merge-Commit von `docs` zeigt die Integration von Dokumentationsänderungen in `main`.
  - Ein weiterer Merge-Commit von `dev` dokumentiert die Einführung eines Git-Submoduls in das Projekt.
  - Frühere Commits betreffen primär die .gitignore-Datei und allgemeine Repository-Initialisierungen.

```bash
# Terminal:
git branch
  dev
  docs
* main

git checkout main
Zu Branch 'main' gewechselt
Ihr Branch ist auf demselben Stand wie 'origin/main'.

git st
Auf Branch main
Ihr Branch ist auf demselben Stand wie 'origin/main'.
nichts zu committen, Arbeitsverzeichnis unverändert

git lg
*   87a9b23 (HEAD -> main, origin/main) Merge branch 'docs'
|\
| * 294d6ec (origin/docs, docs) änderung docs
* |   f5fd94d Merge branch 'dev'
|\ \
| |/
|/|
| * dada445 (origin/dev, dev) git repo als gitmodul hinzugefügt auf dev
* | 34d1fd8 gitignore
* | 6580c23 gitignore
|/
* 7c9e651 readme änderungen hinzugefügt
* 65331ed gitignore
* b4a0efa first commit
```
