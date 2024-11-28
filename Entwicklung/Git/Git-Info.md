---
thema: "Git-Info"
runningtitle: "Git-Info"
keywords: ""
abstract: |
  Die GitHub-API spielt eine entscheidende Rolle in der Automatisierung und Effizienzsteigerung der Softwareentwicklung. Um die durch GitHub auferlegten Anfragebeschränkungen zu umgehen, ist die Authentifizierung mittels eines persönlichen Zugangstokens (PAT) ein bewährter Weg. Dieses Verfahren beginnt mit dem Erstellen eines PAT über die GitHub-Einstellungen, das sorgfältig mit den notwendigen Berechtigungen, wie dem Zugriff auf Repositories, der Lektüre von Organisations- und Teammitgliedschaften und dem Management von GitHub Actions-Workflows, konfiguriert wird. Nach der Generierung ist es essentiell, diesen Token sicher aufzubewahren, da er nur einmalig von GitHub angezeigt wird.

  Die Integration des Tokens in das GitHub Command Line Interface (CLI) ermöglicht eine effektivere Interaktion mit GitHub, einschließlich der Überprüfung der Authentifizierung, des Listenings von Repositories, des Klonens, Erstellens und Löschens von Repositories sowie der Durchführung von Initialisierungen und Erstcommits. Darüber hinaus erleichtert das Verständnis von Konzepten wie Merge-Konflikten, den Unterschieden zwischen Push und Fetch sowie Merge und Rebase die Kollaboration und das Management von Code innerhalb von Projekten.

  Diese Einführung bietet eine verständliche Übersicht über die Nutzung der GitHub-API und grundlegende Git-Operationen, die für eine effiziente und sichere Softwareentwicklung unerlässlich sind.

  \section*{Schlüsselwörter}

  \begin{description}
      \item[GitHub-API] Eine Schnittstelle für die Interaktion mit GitHub-Diensten, die Entwicklern erlaubt, Aktionen programmatisch auszuführen.
      \item[Personal Access Token (PAT)] Ein Token, das für die Authentifizierung bei der GitHub-API genutzt wird, um höhere Anfragegrenzen und Zugriff auf geschützte Daten zu ermöglichen.
      \item[Repository] Ein digitaler Speicherort auf GitHub, der den Quellcode und die dazugehörigen Dateien eines Projekts enthält.
      \item[Commit] Eine Aktion, die Änderungen im Repository festhält und protokolliert, ähnlich wie das Speichern einer neuen Version eines Dokuments.
      \item[Push] Das Hochladen lokaler Repository-Änderungen auf das entfernte Repository auf GitHub.
      \item[Fetch] Das Herunterladen von Änderungen aus dem entfernten Repository, ohne diese automatisch mit dem lokalen Repository zu verschmelzen.
      \item[Merge] Das Zusammenführen von Änderungen aus verschiedenen Entwicklungszweigen (Branches) in einen einzigen Branch.
      \item[Pull Request] Eine Anfrage in GitHub, mit der vorgeschlagen wird, Änderungen aus einem Branch in einen anderen zu übernehmen, meist von einem Fork zurück in das ursprüngliche Repository.
      \item[Merge-Konflikt] Eine Situation, die auftritt, wenn Änderungen aus unterschiedlichen Branches nicht automatisch zusammengeführt werden können und manuelle Eingriffe erfordern.
  \end{description}
author: 'ju'
date: \today
---
<!-------------------------------------------------------------------------------------------------------------
ju 2024-03-06 Git-Info.md
pandoc Git-Info.md -o Git-Info.html -c navigation.css --mathjax --citeproc --bibliography=literatur.bib --csl=zitierstil-number.csl

Quelle [@spanner:2019:robotik].

Fußnote.[^1]
[^1]: Text der Fußnote.

[Google](https://www.google.com)

![Logo 2](images/Logo/Logo2.pdf)

**Tabelle 1:** Beschreibung

pandoc Git-Info.md --to latex --output Git-Info.tex --template=vorlage-main.tex --lua-filter=combined-filter.lua
pdflatex Git-Info.tex
biber Git-Info
pdflatex Git-Info.tex
pdflatex Git-Info.tex

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

# Zugriff auf die GitHub-API

**Zugriff auf die GitHub-API** GitHub beschränkt die Anzahl der API-Anfragen, die Sie machen können, insbesondere für unauthentifizierte Anfragen. Um diese Beschränkungen zu erhöhen, können Sie sich authentifizieren, indem Sie einen persönlichen Zugriffstoken (PAT) in Ihren Anfragen verwenden.

## Einen neuen Personal Access Token generieren

1. **Navigieren Sie zu den Token-Einstellungen**: Öffnen Sie Ihren Webbrowser und gehen Sie zur Seite für Personal Access Tokens in Ihren GitHub-Einstellungen: [https://github.com/settings/tokens](https://github.com/settings/tokens).

2. **Generieren Sie einen neuen Token**: Klicken Sie auf den Button "New token" oder "Neuen Token generieren".

3. **Geben Sie dem Token einen Namen**: Damit Sie sich später erinnern können, wofür der Token verwendet wird, geben Sie ihm eine beschreibende Bezeichnung.

4. **Wählen Sie die erforderlichen Scopes aus**: Um sicherzustellen, dass Ihr Token mit dem GitHub CLI kompatibel ist, müssen Sie ihm mindestens die folgenden Scopes zuweisen:
   - `repo`: Vollzugriff auf private und öffentliche Repositories
   - `read:org`: Lesen von Organisations- und Teammitgliedschaften
   - `workflow`: Erlaubt den Zugriff auf GitHub Actions-Workflows
   - `delete_repo`

5. **Generieren und kopieren Sie den Token**: Nachdem Sie den Token generiert haben, stellen Sie sicher, dass Sie ihn kopieren. GitHub zeigt Ihnen den Token nur einmal bei der Erstellung an.

6. **Token im GitHub CLI einfügen**: Gehen Sie zurück zum Terminal, wo das GitHub CLI Sie auffordert, Ihren Authentifizierungstoken einzufügen, und fügen Sie den kopierten Token ein.

```bash
# Terminal:
# https://github.com/settings/tokens
# Zugangstoken:

# 1
gh auth refresh -h github.com -s delete_repo
? Authenticate Git with your GitHub credentials? Yes
! First copy your one-time code:
Press Enter to open github.com in your browser...
✓ Authentication complete.

# 2
gh auth login
? What account do you want to log into? GitHub.com
? What is your preferred protocol for Git operations on this host? HTTPS
X Sorry, your reply was invalid: "<" is not a valid answer, please try again.
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Paste an authentication token
Tip: you can generate a Personal Access Token here https://github.com/settings/tokens
The minimum required scopes are 'repo', 'read:org', 'workflow'.
? Paste your authentication token: ****************************************
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as ju1-eu
! You were already logged in to this account

# 3
unset GITHUB_TOKEN
echo Token| gh auth login --with-token
# Test - Authentifizierung mit dem GitHub CLI
gh api user
gh repo list
```

# GitHub CLI (Command Line Interface) gh

## Repositories

- **Authentifizierung überprüfen**:

  ```bash
  # Terminal:
  gh auth status
  gh api user
  gh repo list
  # Authentifizierung mit dem GitHub CLI
  gh auth refresh -h github.com -s delete_repo
  gh auth login
  # https://github.com/settings/tokens
  # Zugangstoken:
  unset GITHUB_TOKEN
  echo Token | gh auth login --with-token
  ```

- **Repositorys des angemeldeten Benutzers auflisten**:

  ```bash
  gh repo list <username>
  gh repo list ju1-eu
  ```

- **Repository klonen**:

  ```bash
  gh repo clone <repository>
  # Beispiel:
  gh repo clone ju1-eu/hello-world
  git clone https://github.com/ju1-eu/mein-neues-repo.git

  ls -a
  .               ..              mein-neues-repo
  ```

- **Neues Repository erstellen**:

  ```bash
  gh repo create <name> [--public|--private|--internal]
  gh repo create mein-neues-repo --public
  ```

- **Repository löschen**:

  ```bash
  gh repo delete <repository> --yes
  gh repo delete mein-neues-repo --yes
  ```

```bash
# Terminal:
# ======================================================================
# Initialisierung und erstes Commit:
echo "# mein-neues-repo" >> README.md
git init
git add README.md
git commit -m "first commit"
# Hauptbranch wird zu main umbenannt
git branch -M main
# Remote-Repository hinzufügen und Push
git remote add origin https://github.com/ju1-eu/mein-neues-repo.git
git push -u origin main
git st
git lg
git pull
git push
```

# Konfliktauflösung und das Verständnis von Merge-Konflikten

## Erkennen von Merge-Konflikten

Ein Merge-Konflikt tritt auf, wenn Git nicht automatisch Änderungen aus verschiedenen Branches in derselben Datei zusammenführen kann. Dies geschieht häufig, wenn zwei Entwickler gleichzeitig Änderungen an denselben Zeilen einer Datei vornehmen oder wenn ein Entwickler eine Datei löscht, während ein anderer sie bearbeitet hat.

## Verstehen von Merge-Konflikten

Wenn ein Konflikt auftritt, kennzeichnet Git die betroffenen Bereiche in der Datei und unterbricht den Merge-Prozess. Der Konflikt muss manuell gelöst werden, bevor der Merge abgeschlossen werden kann.

In der Datei sehen Konflikte typischerweise so aus:

```plaintext
<<<<<<< HEAD
[Inhalt im aktuellen Branch]
=======
[Inhalt aus dem zu mergenden Branch]
>>>>>>> [Branch-Name]
```

- `<<<<<<< HEAD` markiert den Beginn des konfliktbehafteten Bereichs in Ihrem aktuellen Branch.
- `=======` trennt die unterschiedlichen Inhalte.
- `>>>>>>> [Branch-Name]` markiert das Ende des konfliktbehafteten Bereichs und zeigt den Namen des anderen Branches an.

## Auflösen von Merge-Konflikten

1. **Identifizieren Sie alle Konfliktbereiche** in der Datei. Suchen Sie nach den Markierungen `<<<<<<<`, `=======`, und `>>>>>>>`.

2. **Entscheiden Sie für jeden Konfliktbereich**, welchen Inhalt Sie behalten möchten:
    - Wählen Sie den Inhalt von einem der Branches.
    - Kombinieren Sie Inhalte aus beiden Branches.
    - Schreiben Sie einen neuen Inhalt, der beide Änderungen berücksichtigt.

3. **Bearbeiten Sie die Datei** und entfernen Sie die Markierungen (`<<<<<<<`, `=======`, `>>>>>>>`), sodass nur der gewünschte Inhalt übrig bleibt.

4. **Fügen Sie die gelösten Dateien zum Staging-Bereich hinzu**:

   ```bash
   git add [Dateiname]
   ```

5. **Schließen Sie den Merge-Vorgang ab**. Wenn alle Konflikte gelöst sind, führen Sie den Merge mit einem Commit ab:

   ```bash
   git commit
   ```

6. **Testen Sie die Änderungen**. Stellen Sie sicher, dass Ihr Code nach der Konfliktlösung wie erwartet funktioniert.

# Unterschied push und fetch

## Git push

- **Zweck**: Der Befehl `git push` wird verwendet, um lokale Änderungen an einem Remote-Repository zu übermitteln. Wenn Sie Commits in Ihrem lokalen Repository gemacht haben, die noch nicht im Remote-Repository vorhanden sind, können Sie `git push` verwenden, um diese Änderungen hochzuladen und das Remote-Repository zu aktualisieren.
- **Richtung**: `push` sendet Daten vom lokalen Repository zum Remote-Repository.
- **Zugriffsrechte**: Um `push` ausführen zu können, benötigen Sie Schreibzugriff auf das Remote-Repository. Ohne die entsprechenden Berechtigungen wird der `push`-Versuch mit einer Fehlermeldung abgelehnt.
- **Anwendung**: `push` wird typischerweise verwendet, nachdem Sie lokale Commits gemacht haben und bereit sind, diese Änderungen mit anderen zu teilen oder ein zentrales Repository auf dem neuesten Stand zu halten.

## Git fetch

- **Zweck**: Der Befehl `git fetch` wird verwendet, um Informationen vom Remote-Repository zu holen, ohne diese automatisch mit Ihrem lokalen Arbeitsverzeichnis oder Ihren lokalen Branches zu mergen. `fetch` holt alle neuen Arbeit von dem angegebenen Remote-Repository, einschließlich neuer Branches und Tags sowie Änderungen in bestehenden Branches.
- **Richtung**: `fetch` holt Daten vom Remote-Repository zum lokalen Repository.
- **Zugriffsrechte**: Für `fetch` benötigen Sie lediglich Lesezugriff auf das Remote-Repository. Da es keine Änderungen am Remote-Repository vornimmt, sind die Zugriffsanforderungen weniger streng.
- **Anwendung**: `fetch` wird verwendet, um auf dem Laufenden zu bleiben mit dem, was im Remote-Repository passiert, ohne die eigenen lokalen Änderungen zu beeinflussen. Nach einem `fetch` können Sie entscheiden, ob und wie Sie die geholten Änderungen in Ihre Arbeit integrieren möchten, z.B. durch einen `merge` oder `rebase`.

**Zusammenfassung:**

- `push` **sendet** Änderungen vom lokalen zum Remote-Repository, erfordert Schreibzugriff und wird verwendet, um Ihre Arbeit mit anderen zu teilen.
- `fetch` **holt** Änderungen vom Remote-Repository, erfordert nur Lesezugriff und beeinflusst Ihre lokale Arbeit nicht direkt. Es erlaubt Ihnen, die Änderungen zu sehen und zu entscheiden, wie Sie diese in Ihre Arbeit integrieren möchten.

# Unterschied Merge und rebase

## Git merge

- **Was es tut**: `merge` nimmt die Inhalte von zwei Branches und vereinigt sie in einem neuen "Merge-Commit". Wenn Sie einen `merge` durchführen, bleibt die gesamte Historie der Branches erhalten, und es wird ein neuer Commit erstellt, der zwei Eltern hat: einen für jeden Branch, der zusammengeführt wird.
- **Commit-Historie**: Die resultierende Commit-Historie ist eine nicht-lineare Historie, die die parallele Entwicklung der Branches zeigt. Das macht es leichter, die historischen Kontexte der Entwicklungspfade zu verstehen.
- **Verwendung**: `merge` wird oft in Teams verwendet, um Änderungen aus einem Feature-Branch in den Hauptbranch (z.B. `main` oder `master`) zu integrieren, da es die vollständige Historie und die Entscheidungen hinter den Änderungen bewahrt.

## Git rebase

- **Was es tut**: `rebase` nimmt die Commits von einem Branch und "reappliziert" sie auf einen anderen Branch. Dabei wird die Basis des Feature-Branches auf den aktuellen Endpunkt des Zielbranches verschoben. Dies kann dazu führen, dass die Commit-Historie geändert wird, da die Commit-IDs der rebasierten Commits neu erstellt werden.
- **Commit-Historie**: Die resultierende Commit-Historie ist linear, was eine saubere, gerade Entwicklungslinie ohne die Merge-Commits erzeugt, die man bei der Verwendung von `merge` sieht. Dies kann die Historie übersichtlicher und einfacher zu verstehen machen, insbesondere bei der Untersuchung von Projektverläufen.
- **Verwendung**: `rebase` wird häufig verwendet, um einen lokalen Branch auf den neuesten Stand zu bringen, indem man ihn auf die Spitze des Hauptbranches setzt, bevor man Änderungen zu einem Remote-Repository pushen oder einen Pull-Request erstellen will. Es wird auch verwendet, um eine saubere, lineare Historie zu erstellen, die leichter zu navigieren ist.

**Unterschiede zusammengefasst:**

- **Historie**: `merge` bewahrt die tatsächliche Entwicklungsgeschichte und die Struktur der Branches, während `rebase` eine lineare Historie erstellt, indem es die Commits neu anordnet, als wären sie auf dem neuesten Stand des Zielbranches gemacht worden.
- **Konflikte**: Sowohl `merge` als auch `rebase` können Konflikte erzeugen, die manuell gelöst werden müssen. Bei einem `rebase` müssen diese Konflikte jedoch für jeden Commit einzeln gelöst werden, durch den der `rebase` durchgeführt wird, was in manchen Situationen mühsamer sein kann.
- **Sicherheit und Transparenz**: `merge` gilt als sicherer für die öffentliche oder geteilte Historie, da es die tatsächliche Entwicklungsgeschichte nicht verändert. `Rebase` ändert die Commit-Historie, was in geteilten Branches zu Problemen führen kann, wenn nicht sorgfältig gehandhabt.

**Empfehlungen:**

- Verwenden Sie `merge`, wenn Sie die vollständige Historie und die Kontexte der Branch-Entwicklung bewahren möchten, insbesondere in geteilten Repositories.
- Verwenden Sie `rebase`, um eine saubere, lineare Historie für lokale Änderungen zu schaffen, bevor Sie diese teilen, oder wenn Sie die Übersichtlichkeit und Einfachheit einer linearen Commit-Historie bevorzugen.

# Branch-Schutzregeln

Die Beschränkung, dass Autoren ihre eigenen Pull Requests nicht genehmigen können, ist absichtlich und fördert Best Practices in der Softwareentwicklung. Es wird dringend empfohlen, innerhalb der vorgesehenen Nutzung dieser Funktionen zu bleiben und Code-Reviews als wesentlichen Bestandteil des Entwicklungsprozesses zu betrachten. Falls Sie alleine an einem Projekt arbeiten und dennoch die Vorteile von Pull Requests und Code-Reviews nutzen möchten, erwägen Sie, ein zweites GitHub-Konto als Reviewer einzurichten, wobei zu beachten ist, dass dies zusätzliche Verwaltungsaufgaben mit sich bringt.

Durch das Festlegen dieser Schutzregeln können Sie sicherstellen, dass Änderungen, die in wichtige Branches gemerged werden, bestimmten Qualitäts- und Sicherheitsstandards entsprechen.

## Schritte zum Festlegen oder Anpassen von Branch-Schutzregeln:

1. **Navigieren Sie zum Repository auf GitHub**: Öffnen Sie das GitHub-Repository in Ihrem Webbrowser.

2. **Gehen Sie zu den Einstellungen des Repositories**: Finden Sie die Registerkarte "Settings" (Einstellungen) in der Navigationsleiste oben auf der Repository-Seite und klicken Sie darauf.

3. **Wählen Sie den Bereich "Branches" aus**: Im Menü auf der linken Seite finden Sie einen Abschnitt namens "Branches" unter der Kategorie "Code and automation". Klicken Sie darauf, um die Branch-Schutzregeln zu verwalten.

4. **Branch-Schutzregeln hinzufügen oder bearbeiten**: Sie sehen eine Liste der bereits konfigurierten Schutzregeln. Um eine neue Regel hinzuzufügen, klicken Sie auf "Add rule" (Regel hinzufügen). Um eine bestehende Regel zu bearbeiten, klicken Sie auf den Namen der Regel.

5. **Konfigurieren Sie die Schutzregeln**:
   - **Require approvals** unter den Branch-Schutzregeln für den main-Branch (oder den relevanten Zielbranch des Pull Requests) deaktivieren.
   - **Branch name pattern**: Geben Sie das Muster für den Branch-Namen ein, auf das die Regel angewendet werden soll (z.B. `main` oder `*` für alle Branches).
   - **Require pull request reviews before merging**: Aktivieren Sie diese Option, um zu verlangen, dass Pull Requests vor dem Mergen überprüft und genehmigt werden müssen.
   - **Require review from Code Owners**: Wenn Sie CODEOWNERS in Ihrem Repository haben, können Sie auch verlangen, dass Code-Eigentümer die Änderungen überprüfen.
   - **Dismiss stale pull request approvals when new commits are pushed**: Diese Option, falls aktiviert, macht Genehmigungen ungültig, wenn neue Commits zu einem Pull Request hinzugefügt werden.
   - **Require status checks to pass before merging**: Aktivieren Sie dies, um durchzusetzen, dass bestimmte Statusprüfungen bestanden werden müssen, bevor der Branch gemerged werden kann.
   - **Include administrators**: Administratoren können ebenfalls den Schutzregeln unterliegen, wenn diese Option aktiviert ist.

6. **Speichern Sie die Regel**: Nachdem Sie die gewünschten Einstellungen konfiguriert haben, scrollen Sie nach unten und klicken Sie auf "Save changes" (Änderungen speichern).
