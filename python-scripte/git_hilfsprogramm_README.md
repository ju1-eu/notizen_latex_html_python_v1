# README

update: 26-8-23

Das Skript `git_hilfsprogramm.py` ist ein Hilfsprogramm für Git, das eine Benutzeroberfläche im Terminal bietet, um verschiedene Git-Aufgaben durchzuführen.

## Beschreibung:

Das Skript bietet eine Reihe von Funktionen, um mit Git zu interagieren:

1. **lokales_repo_erstellen_und_initialisieren**: Erstellt ein lokales Repository und initialisiert es. Es überprüft auch, ob eine `.gitignore`-Datei vorhanden ist und erstellt sie, falls nicht.
2. **lokales_repo_mit_github_verknüpfen**: Verknüpft ein lokales Repository mit einem GitHub-Repository.
3. **änderungen_hinzufügen**: Fügt Dateien/Änderungen zur Git-Staging-Area hinzu.
4. **änderungen_commiten**: Committet Änderungen im lokalen Repository.
5. **änderungen_pushen**: Pusht Änderungen von einem lokalen Repository zu GitHub.
6. **änderungen_pullen**: Holt Änderungen von GitHub und führt einen Merge im lokalen Repository durch.
7. **repository_klonen**: Klont ein GitHub-Repository.
8. **branch_erstellen**: Erstellt einen neuen Git-Branch.
9. **branch_wechseln**: Wechselt zwischen Git-Branches.
10. **branches_auflisten**: Listet alle verfügbaren Git-Branches auf.
11. **merge_branch**: Führt einen Git-Branch in einen anderen ein.
12. **stash_änderungen**: Verwendet den Befehl `git stash` um Änderungen temporär zu speichern.
13. **konflikte_anzeigen**: Zeigt Git-Konflikte an.
14. **pull_requests_auflisten**: Listet alle verfügbaren Pull-Requests auf (dies erfordert möglicherweise zusätzliche Konfiguration oder Abhängigkeiten).
15. **gitignore_anzeigen**: Zeigt den Inhalt der `.gitignore`-Datei an.
16. **gitignore_verwalten**: Verwaltet Einträge in der `.gitignore`-Datei.
17. **log_anzeigen**: Zeigt den Git-Log an.
18. **status_anzeigen**: Zeigt den Git-Status an.
19. **github_repositorys_anzeigen**: Listet alle GitHub-Repositories des Benutzers auf (dies erfordert möglicherweise zusätzliche Konfiguration oder Abhängigkeiten).
20. **github_repository_löschen**: Löscht ein GitHub-Repository (dies erfordert möglicherweise zusätzliche Konfiguration oder Abhängigkeiten).
21. **Beenden**: Beendet das Programm.

### Benutzung:

Um das Skript zu verwenden, führen Sie es mit Python aus und geben Sie den Ordnernamen als Argument an:

```
python3 git_hilfsprogramm.py MeinProjekt
```

Nachdem das Skript gestartet ist, zeigt es ein Menü mit den oben beschriebenen Optionen an. Der Benutzer kann eine Option auswählen, indem er die entsprechende Nummer eingibt.

```
--- Git-Hilfsprogramm ---
1. Neues lokales Repository erstellen
2. Neues Repository auf GitHub verbinden
3. Änderungen hinzufügen (git add)
4. Änderungen commiten (git commit)
5. Änderungen pushen (git push)
6. Änderungen pullen (git pull)
7. Repository klonen
8. Branch erstellen
9. Zu einem Branch wechseln
10. Alle Branches auflisten
11. Merge eines Branches
12. Änderungen stashen
13. Merge-Konflikte anzeigen
14. Pull Requests auflisten
15. .gitignore-Dateiinhalt anzeigen
16. .gitignore verwalten
17. Git-Logs anzeigen
18. Git-Status anzeigen
19. GitHub-Repositorys anzeigen
20. GitHub-Repositorys löschen
21. Beenden
#########################################################
```

**Git-Status anzeigen**

```
# Wählen Sie eine Option: 18
Erklärung
## zeigt den aktuellen Branch an, gefolgt von den Änderungen in Bezug auf den Remote-Branch.
M - Geänderte Datei (modifiziert)
A - Hinzugefügte Datei (neu hinzugefügt)
D - Gelöschte Datei
?? - Ungetrackte Datei
#########################################################
## main...origin/main
 M .gitignore
 M README.md
 M git_hilfsprogramm.py
```

**Änderungen hinzufügen (git add) und commiten (git commit) und pushen (git push)**

```
# Wählen Sie eine Option: 3
Welche Datei möchten Sie hinzufügen? (Alles: .): .

# Wählen Sie eine Option: 4
Geben Sie eine Commit-Nachricht ein: script fehlerfrei und Beschreibung erstellt
[main b0309c0] script fehlerfrei und Beschreibung erstellt
 3 files changed, 717 insertions(+), 38 deletions(-)

# Wählen Sie eine Option: 5
Branch 'main' folgt nun 'origin/main'.
```

**Repository klonen**

```
# script
python3 git_hilfsprogramm.py MeinProjekt3

# Wählen Sie eine Option: 7
Verfügbare Repositories zum Klonen:

17. Repository: MeinProjekt2
   URL: https://github.com/ju1-eu/MeinProjekt2

Geben Sie die Nummer des Repositories ein, das Sie klonen möchten, oder 0 zum Abbrechen: 17
Klone das Repository 'MeinProjekt2' von der URL 'https://github.com/ju1-eu/MeinProjekt2' in den Ordner 'MeinProjekt3'.

Repository 'MeinProjekt2' wurde erfolgreich in den Ordner 'MeinProjekt3' geklont.
```

**Neues lokales Repository erstellen**

```
# Wählen Sie eine Option: 1
Leeres Git-Repository in /Users/jan/daten/Programmieren/Elektronik-Programmierung/Roboter-Arduino/05-Elektrik-Elektronik-Dr.Dalmaris/Git/MeinProjekt2/.git/ initialisiert


[main (Root-Commit) d0955c1] first commit
 1 file changed, 2 insertions(+)
 create mode 100644 README.md
```

**Neues Repository auf GitHub verbinden**

```
# Wählen Sie eine Option: 2
Möchten Sie ein bereits vorhandenes GitHub-Repository verwenden oder ein neues erstellen und verknüpfen? (vorhanden/neu): neu
https://github.com/ju1-eu/MeinProjekt2
Branch 'main' folgt nun 'origin/main'.

Das lokale Repository 'MeinProjekt2' wurde erfolgreich erstellt und mit einem neuen GitHub-Repository verknüpft.
```

### Hinweis:

Einige Funktionen des Skripts können von externen Bibliotheken oder Tools abhängen (z.B. `requests` oder `gh`), die installiert sein müssen, damit das Skript ordnungsgemäß funktioniert.

Es scheint auch, dass dieses Skript speziell für einen Benutzer namens "ju1-eu" auf GitHub konfiguriert ist. Falls Sie ein anderer Benutzer sind, müssen Sie möglicherweise die `GITHUB_URL`-Variable im Skript ändern.


## Was ist Git?

Git ist ein verteiltes Versionskontrollsystem, das von Linus Torvalds, dem Schöpfer des Linux-Kerns, im Jahr 2005 entwickelt wurde. Es hat sich seitdem zu einem Standardwerkzeug für die Softwareentwicklung entwickelt und wird von vielen Open-Source- und kommerziellen Projekten weltweit verwendet.

Hauptmerkmale und Konzepte von Git:

1.  **Verteilt**: Jeder Entwickler hat eine vollständige Kopie der Historie des Projekts, was die Arbeit offline ermöglicht und das Risiko eines einzelnen Ausfallpunktes eliminiert.
    
2.  **Commit**: Ein "Commit" ist eine Momentaufnahme des Projekts zu einem bestimmten Zeitpunkt. Jeder Commit hat eine eindeutige ID, die als "Hash" bezeichnet wird.
    
3.  **Branches**: Git ermöglicht es, parallele Linien der Entwicklung zu erstellen, die als "Branches" bezeichnet werden. Der Hauptzweig wird oft als "master" oder "main" bezeichnet.
    
4.  **Merge**: Sie können Änderungen von einem Branch in einen anderen übernehmen, indem Sie sie "zusammenführen" oder "mergen".
    
5.  **Pull und Push**: Sie können Änderungen aus einem Remote-Repository "ziehen" (pull) und Ihre lokalen Änderungen in ein Remote-Repository "schieben" (push).
    
6.  **Clone**: Mit `git clone` können Sie eine Kopie eines Remote-Repositories auf Ihren lokalen Computer herunterladen.
    
7.  **Staging Area**: Bevor Änderungen committet werden, können sie in einer "Staging Area" platziert werden. Dies ermöglicht es, gezielt Dateiänderungen für den nächsten Commit auszuwählen.
    
8.  **Log**: Mit `git log` können Sie die Historie des Projekts ansehen.
    
9.  **Remote**: Ein "Remote" ist ein anderes Repository, mit dem Sie Daten austauschen können. Oft handelt es sich dabei um ein Repository auf einem Server wie GitHub, GitLab oder Bitbucket.
    
10.  **Fetch**: Mit `git fetch` können Sie die neuesten Änderungen aus einem Remote-Repository abrufen, ohne sie automatisch in Ihren aktuellen Branch zu mergen.
    

## Lokales Repository erstellen

1.  **Installation (falls noch nicht geschehen)**:
    
    -  Besuchen Sie die offizielle Git-Website unter [https://git-scm.com/](https://git-scm.com/) und laden Sie Git für Ihr Betriebssystem herunter und installieren Sie es.
2.  **Repository erstellen**:
    
    -  Öffnen Sie Ihr Terminal oder Ihre Befehlszeile.
    -  Navigieren Sie zu dem Verzeichnis, in dem Sie Ihr Repository erstellen möchten.
    -  Geben Sie folgenden Befehl ein:
        ```bash
        git init mein_repo
        ```
        
    -  Wechseln Sie in das neu erstellte Verzeichnis:
        ```bash
        cd mein_repo
        ```
        

## GitHub Repository erstellen

1.  **Konto erstellen (falls noch nicht geschehen)**:
    
    -  Besuchen Sie [https://github.com/](https://github.com/) und erstellen Sie ein Konto, falls Sie noch keines haben.
2.  **Neues Repository auf GitHub erstellen**:
    
    -  Klicken Sie nach dem Einloggen in der rechten oberen Ecke auf das `+` Symbol und wählen Sie "New repository".
    -  Geben Sie einen Namen für Ihr Repository ein (z.B. "mein\_repo").
    -  Wählen Sie die gewünschten Einstellungen (öffentlich/privat, README, .gitignore, Lizenz).
    -  Klicken Sie auf "Create repository".
3.  **Lokales Repository mit GitHub verbinden**:
    
    -  In Ihrem Terminal (stellen Sie sicher, dass Sie sich im `mein_repo` Verzeichnis befinden), geben Sie die folgenden Befehle ein:
        
        ```bash
        git remote add origin https://github.com/IHR_BENUTZERNAME/mein_repo.git
        git add .
        git commit -m "Erster Commit"
        git push -u origin master
        ```
        
    -  Ersetzen Sie `IHR_BENUTZERNAME` durch Ihren tatsächlichen GitHub-Benutzernamen.

Nach diesen Schritten haben Sie ein lokales Repository erstellt und es mit einem GitHub-Repository verknüpft. Sie können jetzt Änderungen in Ihrem lokalen Repository vornehmen und diese Änderungen zu GitHub pushen.

## Git mit Homebrew installieren und aktualisieren

1.  **Homebrew installieren (falls noch nicht geschehen)**:
    
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    
2.  **Homebrew aktualisieren (immer eine gute Idee, bevor Sie neue Software installieren)**:
    
    ```bash
    brew update
    ```
    
3.  **Git mit Homebrew installieren**:
    
    ```bash
    brew install git
    ```
    
4.  **Git aktualisieren (falls in der Zukunft notwendig)**:
    
    ```bash
    brew upgrade git
    ```
    

**Überprüfen Sie Ihre Git-Installation**: Nach der Installation können Sie überprüfen, ob Git korrekt installiert wurde und welche Version Sie haben:

```bash
git --version
```

## GitHub CLI-Tool

1. **GitHub CLI-Tool (gh)**
   
   Dies ist keine Befehlszeile, sondern eine Überschrift oder Anmerkung, die darauf hinweist, dass die folgenden Befehle das GitHub CLI-Tool (`gh`) betreffen.

2. **`brew install gh`**

   Dieser Befehl verwendet den macOS-Paketmanager "Homebrew" (`brew`), um das GitHub Command Line Interface (CLI) Tool `gh` zu installieren. Das `gh`-Tool ermöglicht es, viele GitHub-Aktionen direkt von der Befehlszeile aus durchzuführen, ohne den Webbrowser zu verwenden.

3. **`gh auth login`**

   Mit diesem Befehl melden Sie sich bei Ihrem GitHub-Konto an. Es wird ein Authentifizierungsprozess gestartet, bei dem Sie nach Ihrem Benutzernamen und Passwort gefragt werden. Möglicherweise werden Sie auch aufgefordert, einen Authentifizierungscode einzugeben, wenn Sie die Zwei-Faktor-Authentifizierung aktiviert haben.

4. **`gh auth status`**

   Dieser Befehl überprüft den Authentifizierungsstatus und teilt Ihnen mit, ob Sie erfolgreich bei GitHub angemeldet sind oder nicht.

5. **`gh auth refresh -h github.com -s delete_repo`**

   Dieser Befehl erneuert oder aktualisiert die Berechtigungen Ihres Tokens für das GitHub CLI. Mit den Optionen `-h github.com` wird das Hosting festgelegt (in diesem Fall GitHub) und `-s delete_repo` gibt die Berechtigung an, die aktualisiert werden soll (in diesem Fall die Berechtigung, ein Repository zu löschen).

6. **`gh repo create MeinProjekt2 --public`**

   Dieser Befehl erstellt ein neues Repository mit dem Namen "MeinProjekt2" auf GitHub. Das Flag `--public` stellt sicher, dass das Repository öffentlich zugänglich ist. Wenn Sie stattdessen ein privates Repository möchten, können Sie `--private` verwenden.

7. **`gh repo delete MeinProjekt2`**

    wird verwendet, um ein Repository auf GitHub über das GitHub CLI-Tool (gh) zu löschen.

Diese Befehle ermöglichen es Ihnen, GitHub effizient über die Befehlszeile zu nutzen, ohne auf die Weboberfläche zugreifen zu müssen. Das `gh`-Tool ist besonders nützlich für Entwickler, die sich häufig mit GitHub beschäftigen und Aktionen automatisieren möchten.

## Verwalten eines Repositories

Das Verwalten eines Repositories sowohl lokal als auch auf GitHub erfordert eine Kombination von Git-Befehlen (für lokale Aktionen) und Aktionen, die direkt auf der GitHub-Website durchgeführt werden (für entfernte Aktionen). Hier sind die grundlegenden Schritte und Befehle, um Ihr Repository sowohl lokal als auch auf GitHub zu verwalten:

### Lokales Repository verwalten

1.  **Lokales Repository klonen** (wenn es noch nicht lokal vorhanden ist):
    
    ```bash
    git clone https://github.com/IHR_BENUTZERNAME/REPO_NAME.git
    ```
    
2.  **Änderungen im lokalen Repository machen**:
    
    -   Bearbeiten Sie Ihre Dateien wie gewohnt.
        
    -   Zeigen Sie den Status Ihrer Änderungen an:
        
        ```bash
        git status
        ```
        
    -   Fügen Sie Ihre Änderungen zur Staging Area hinzu:
        
        ```bash
        git add .
        ```
        
        Oder fügen Sie spezifische Dateien hinzu:
        
        ```bash
        git add DATEINAME
        ```
        
    -   Committen Sie Ihre Änderungen:
        
        ```bash
        git commit -m "Beschreiben Sie Ihre Änderungen hier"
        ```
        
3.  **Änderungen zu GitHub pushen**:
    
    ```bash
    git push origin BRANCH_NAME
    ```
    
    Für den Hauptbranch ist `BRANCH_NAME` in der Regel `main` oder `master`.
    
4.  **Änderungen von GitHub ziehen** (um lokal auf dem neuesten Stand zu bleiben):
    
    ```bash
    git pull origin BRANCH_NAME
    ```
    
5.  **Branches verwalten**:
    
    -   Neuen Branch erstellen:
        
        ```bash
        git checkout -b NEUER_BRANCH_NAME
        ```
        
    -   Zwischen Branches wechseln:
        
        ```bash
        git checkout BRANCH_NAME
        ```
        
6.  **Lokale Branches mit GitHub synchronisieren**:
    
    -   Pushen Sie einen neuen Branch zu GitHub:
        
        ```bash
        git push -u origin NEUER_BRANCH_NAME
        ```
        

### Repository auf GitHub verwalten

1.  **Pull Requests (PRs)**:
    
    -   Auf GitHub können Sie PRs erstellen, um Änderungen von einem Branch in einen anderen zu übernehmen.
    -   Reviewen und diskutieren Sie Änderungen in PRs.
    -   Sobald Sie bereit sind, können Sie den PR mergen.
2.  **Issues**:
    
    -   Erstellen Sie Issues, um Bugs zu melden, Features vorzuschlagen oder Diskussionen über bestimmte Aspekte des Projekts zu führen.
3.  **GitHub Actions**:
    
    -   Automatisieren Sie Prozesse wie Tests, Builds und Deployments mit CI/CD-Workflows.
4.  **Repository-Einstellungen**:
    
    -   Konfigurieren Sie die Repository-Zugriffsberechtigungen, fügen Sie Kollaborateure hinzu, verwalten Sie Webhooks und vieles mehr.
5.  **Code-Review**:
    
    -   Überprüfen Sie Commits, PRs und führen Sie Code-Reviews durch, um die Codequalität zu gewährleisten.
6.  **Wiki & Projekte**:
    
    -   Nutzen Sie die integrierte Wiki-Funktionalität von GitHub, um Dokumentationen zu schreiben.
    -   Verwenden Sie Projekte für eine agile Projektverwaltung direkt auf GitHub.
7.  **Releases & Tags**:
    
    -   Markieren Sie wichtige Punkte in Ihrer Code-Historie mit Tags.
    -   Erstellen Sie Releases, um stabile Versionen Ihres Projekts zu veröffentlichen.

Dies sind die grundlegenden Aktionen, um ein Repository sowohl lokal mit Git als auch entfernt auf GitHub zu verwalten. Je nach Ihren spezifischen Anforderungen und Ihrem Workflow können weitere Befehle und Aktionen erforderlich sein.


## Python Script git_hilfsprogramm.py

```python
# git_hilfsprogramm.py
import subprocess
import os
import re
import sys
import shutil
import requests


"""
python3 git_hilfsprogramm.py MeinProjekt
python3 git_hilfsprogramm.py MeinProjekt2
"""


GITHUB_URL = "https://github.com/ju1-eu/"
README_FILE = "README.md"

def ausführen_befehl(befehl, ordner):
    try:
        prozess = subprocess.run(befehl, shell=True, text=True, capture_output=True, check=True, cwd=ordner)
        print(prozess.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei Ausführung des Befehls: {e.cmd}\nFehlerausgabe:\n{e.stderr}\n{e.stdout}")
        entscheidung = input("Möchten Sie den Befehl erneut ausführen? (ja/nein): ").lower()
        if entscheidung == "ja":
            return ausführen_befehl(befehl, ordner)
        else:
            print("Befehl wurde abgebrochen.")
            return False

def sichere_eingabe(eingabeaufforderung):
    eingabe = input(eingabeaufforderung)
    if re.search(r"[;&|<>]", eingabe):
        print("Potenziell unsichere Eingabe erkannt. Bitte versuchen Sie es erneut.")
        return sichere_eingabe(eingabeaufforderung)
    return eingabe

def lokales_repo_erstellen_und_initialisieren(ordner):
    ordner_pfad = os.path.join(os.getcwd(), ordner)
    
    # Überprüfen und Erstellen des Ordners, falls er nicht existiert
    if not os.path.exists(ordner_pfad):
        os.makedirs(ordner_pfad)

    # Überprüfen, ob die .gitignore-Datei vorhanden ist, und erstellen, falls nicht
    gitignore_pfad = os.path.join(ordner_pfad, ".gitignore")
    if not os.path.exists(gitignore_pfad):
        with open(gitignore_pfad, 'w') as gitignore:
            gitignore.write("# Hier Dateien und Verzeichnisse angeben, die von der Versionskontrolle ausgeschlossen werden sollen\n")
    # Erstellen der README-Datei mit der ersten Zeile
    with open(os.path.join(ordner_pfad, README_FILE), 'w') as readme:
        readme.write(f"# " + ordner + " Repository\nThis is the README for the " + ordner + " repository.\n")

    # Git-Befehle ausführen
    befehle = [
        f"git init {ordner_pfad}",
        f"cd {ordner_pfad} && git add {README_FILE}"
    ]
    for befehl in befehle:
        ausführen_befehl(befehl, ordner_pfad)
    
    # Überprüfen, ob es Änderungen gibt, die committet werden können
    prozess = subprocess.run(f"git -C {ordner_pfad} status -s", shell=True, text=True, capture_output=True)
    if prozess.stdout.strip():
        ausführen_befehl(f'cd {ordner_pfad} && git commit -m "first commit"', ordner_pfad)
    else:
        print("Keine Änderungen im Arbeitsverzeichnis vorhanden. Es gibt nichts zu committen.")


def lokales_repo_mit_github_verknüpfen(ordner):
    if not os.path.exists(ordner):
        print(f"Das Verzeichnis '{ordner}' existiert nicht.")
        return

    prozess = subprocess.run("git remote show origin", shell=True, text=True, capture_output=True, cwd=ordner)
    if "fatal: Remote origin already exists." in prozess.stderr:
        print("Fehler: Externes Repository origin existiert bereits.")
        return

    entscheidung = input("Möchten Sie ein bereits vorhandenes GitHub-Repository verwenden oder ein neues erstellen und verknüpfen? (vorhanden/neu): ").lower()

    if entscheidung == "vorhanden":
        github_repo_url = input("Geben Sie die URL des vorhandenen GitHub-Repositorys ein: ")
        subprocess.run(f"git remote add origin {github_repo_url}", shell=True, cwd=ordner)
        subprocess.run("git branch -M main", shell=True, cwd=ordner)
        subprocess.run("git push -u origin main", shell=True, cwd=ordner)
        print(f"Das lokale Repository '{ordner}' wurde erfolgreich mit dem GitHub-Repository verknüpft.")
    elif entscheidung == "neu":
        befehl = f"""
        gh repo create {ordner} --public
        git remote add origin {GITHUB_URL}{ordner}
        git branch -M main
        git push -u origin main
        """
        ausführen_befehl(befehl, ordner)
        print(f"Das lokale Repository '{ordner}' wurde erfolgreich erstellt und mit einem neuen GitHub-Repository verknüpft.")
    else:
        print("Ungültige Auswahl. Bitte 'vorhanden' oder 'neu' eingeben.")



def commiten_und_pushen(ordner):
    dateien = input("Welche Dateien möchten Sie hinzufügen? (z.B. 'file1.txt file2.txt' oder '.' für alle): ")
    commit_nachricht = input("Geben Sie eine Commit-Nachricht ein: ")
    befehl = f"cd {ordner} && git add {dateien} && git commit -m '{commit_nachricht}' && git push origin main"
    ausführen_befehl(befehl)

def änderungen_ziehen(ordner):
    ausführen_befehl("cd {ordner} && git pull origin main")

def status_anzeigen(ordner):
    ausführen_befehl("cd {ordner} && git status")

def branch_erstellen(ordner):
    branch_name = input("Geben Sie den Namen des neuen Branches ein: ")
    ausführen_befehl(f"cd {ordner} && git checkout -b {branch_name}")

def zu_branch_wechseln(ordner):
    branch_name = input("Geben Sie den Namen des Branches ein, zu dem Sie wechseln möchten: ")
    ausführen_befehl(f"cd {ordner} && git checkout {branch_name}")

def log_anzeigen(ordner):
    ausführen_befehl("cd {ordner} && git log")

def änderungen_hinzufügen(ordner):
    datei = input("Welche Datei möchten Sie hinzufügen? (Alles: .): ")
    ausführen_befehl(f"git add {datei}", os.path.join(os.getcwd(), ordner))


def änderungen_commiten(ordner):
    # Vor dem Commit überprüfen, ob es Änderungen gibt
    status_prozess = subprocess.run(f"git -C {ordner} status -s", shell=True, text=True, capture_output=True)
    status_output = status_prozess.stdout.strip()
    if not status_output:
        print("Keine Änderungen im Arbeitsverzeichnis vorhanden. Es gibt nichts zu committen.")
        return
    
    nachricht = input("Geben Sie eine Commit-Nachricht ein: ")
    ausführen_befehl(f'git commit -m "{nachricht}"', ordner)


def repo_klonen(ordner):
    repositories = get_user_repositories(get_username_from_url(GITHUB_URL))
    
    if repositories:
        print("Verfügbare Repositories zum Klonen:\n")
        for idx, repo in enumerate(repositories, start=1):
            repo_name = repo["name"]
            repo_url = GITHUB_URL + repo_name
            print(f"{idx}. Repository: {repo_name}\n   URL: {repo_url}\n")

        try:
            auswahl = int(input("Geben Sie die Nummer des Repositories ein, das Sie klonen möchten, oder 0 zum Abbrechen: "))
            
            if 0 < auswahl <= len(repositories):
                repo_name = repositories[auswahl - 1]["name"]

                repo_url = GITHUB_URL + repo_name
                print(f"Klone das Repository '{repo_name}' von der URL '{repo_url}' in den Ordner '{ordner}'.")
                
                ausführen_befehl(f"git clone '{repo_url}' .", ordner)

                print(f"Repository '{repo_name}' wurde erfolgreich in den Ordner '{ordner}' geklont.")
            elif auswahl == 0:
                print("Befehl wurde abgebrochen.")
            else:
                print("Ungültige Auswahl.")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Nummer ein.")
    else:
        print("Keine öffentlichen Repositories gefunden.")



def änderungen_pushen(ordner):
    ausführen_befehl("git push -u origin main", ordner)


def änderungen_pullen(ordner):
    prozess = subprocess.run("git status --porcelain", shell=True, text=True, capture_output=True, cwd=os.path.join(os.getcwd(), ordner))
    if prozess.stdout.strip():
        print("Es gibt uncommitierte Änderungen im Arbeitsverzeichnis. Bitte committen oder staschen Sie diese, bevor Sie Änderungen ziehen.")
        return

    remote_branch = input("Geben Sie den Remote-Branch ein, von dem Sie Änderungen ziehen möchten: ")
    ausführen_befehl(f"git pull origin {remote_branch}", os.path.join(os.getcwd(), ordner))




def branch_erstellen(ordner):
    branch_name = sichere_eingabe("Geben Sie den Namen des neuen Branches ein: ")
    ausführen_befehl(f"git checkout -b {branch_name}", os.path.join(os.getcwd(), ordner))

def branch_wechseln(ordner):
    branch_name = sichere_eingabe("Zu welchem Branch möchten Sie wechseln?: ")
    ausführen_befehl(f"git checkout {branch_name}", os.path.join(os.getcwd(), ordner))



def branches_auflisten(ordner):
   ausführen_befehl("git branch", os.path.join(os.getcwd(), ordner))

    
def merge_branch(ordner):
    branch_name = input("Welchen Branch möchten Sie in den aktuellen Branch mergen?: ")
    ausführen_befehl(f"git merge {branch_name}", ordner)


def stash_änderungen(ordner):
    ausführen_befehl("git stash", ordner)
    print("Änderungen wurden gestashed.")

def gitignore_verwalten(ordner):
    print("1. .gitignore anzeigen")
    print("2. Eine neue Regel zu .gitignore hinzufügen")
    auswahl = input("Wählen Sie eine Option: ")
    if auswahl == "1":
        gitignore_anzeigen(ordner)
    elif auswahl == "2":
        regel = input("Geben Sie die Regel ein, die Sie hinzufügen möchten: ")
        with open(os.path.join(ordner, ".gitignore"), 'a') as file:
            file.write(f"\n{regel}")
        print(f"Regel '{regel}' zu .gitignore hinzugefügt.")

def konflikte_anzeigen(ordner):
    ausführen_befehl("git diff --name-only --diff-filter=U", ordner)
    print("Oben sind die Dateien mit Merge-Konflikten aufgelistet.")

    
def pull_requests_auflisten(ordner):
    print("Beachten Sie, dass dies nur funktioniert, wenn Sie über das GitHub CLI-Tool 'gh' verfügen.")
    ausführen_befehl("gh pr list", ordner)


def gitignore_anzeigen(ordner):
    gitignore_path = os.path.join(ordner, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            print(f.read())
    else:
        print(".gitignore existiert nicht in diesem Repository.")
        
        
def log_anzeigen(ordner):
    ausführen_befehl("git log", os.path.join(os.getcwd(), ordner))


def status_anzeigen(ordner):
    print("Erklärung")
    print("## zeigt den aktuellen Branch an, gefolgt von den Änderungen in Bezug auf den Remote-Branch.")
    print("M - Geänderte Datei (modifiziert)")
    print("A - Hinzugefügte Datei (neu hinzugefügt)")
    print("D - Gelöschte Datei")
    print("?? - Ungetrackte Datei")
    drucke_trennlinie()
    ausführen_befehl("git status -s -b -u", os.path.join(os.getcwd(), ordner))
    
def get_user_repositories(username):
    page_number = 1
    repositories = []
    
    while True:
        response = requests.get(f"https://api.github.com/users/{username}/repos?page={page_number}&per_page=100")
        
        if response.status_code == 200:
            current_page_repos = response.json()
            
            # Wenn die aktuelle Seite keine Repositories hat, brechen wir die Schleife ab.
            if not current_page_repos:
                break
            
            repositories.extend(current_page_repos)
            page_number += 1
        else:
            print(f"Fehler beim Abrufen der Repositories für Benutzer {username} auf Seite {page_number}. Statuscode: {response.status_code}")
            break
    
    return repositories
    
def get_username_from_url(url):
    match = re.match(r"https://github.com/([^/]+)/?$", url)
    if match:
        return match.group(1)
    return None


    

def github_repositorys_anzeigen():
    username_match = re.match(r"https://github.com/(.*)/$", GITHUB_URL)
    if username_match:
        username = username_match.group(1)
        repositories = get_user_repositories(username)
        
        if repositories:
            print(f"Öffentliche Repositories für Benutzer {username}:\n")
            for index, repo in enumerate(repositories, start=1):
                repo_name = repo["name"]
                repo_url = GITHUB_URL + repo_name
                print(f"{index}. Repository: {repo_name}\nURL: {repo_url}\n")
        else:
            print("Keine öffentlichen Repositories gefunden.")
    else:
        print("Ungültige GITHUB_URL. Stellen Sie sicher, dass der Benutzername in der URL enthalten ist.")




def github_repository_löschen():
    repository_name = input("Geben Sie den Namen des zu löschenden Repositories ein: ")
    befehl = f"gh repo delete {repository_name}"
    erneut_ausführen = True

    while erneut_ausführen:
        erneut_ausführen = False
        try:
            ausführen_befehl(befehl + " --yes", '.')
            print(f"Repository '{repository_name}' wurde erfolgreich gelöscht.")
        except subprocess.CalledProcessError as e:
            print(f"Fehler bei Ausführung des Befehls: {e.cmd}\nFehlerausgabe:\n{e.stderr}\n{e.stdout}")
            entscheidung = input("Möchten Sie den Befehl erneut ausführen? (ja/nein): ").lower()
            if entscheidung == "ja":
                erneut_ausführen = True
            else:
                print("Befehl wurde abgebrochen.")




def drucke_trennlinie():
    print("#########################################################")

def menü_anzeigen():
    print("\n--- Git-Hilfsprogramm ---")
    print("1. Neues lokales Repository erstellen")
    print("2. Neues Repository auf GitHub verbinden")
    print("3. Änderungen hinzufügen (git add)")
    print("4. Änderungen commiten (git commit)")
    print("5. Änderungen pushen (git push)")
    print("6. Änderungen pullen (git pull)")    
    print("7. Repository klonen")
    print("8. Branch erstellen")
    print("9. Zu einem Branch wechseln")
    print("10. Alle Branches auflisten")
    print("11. Merge eines Branches")
    print("12. Änderungen stashen")
    print("13. Merge-Konflikte anzeigen")
    print("14. Pull Requests auflisten")
    print("15. .gitignore-Dateiinhalt anzeigen")
    print("16. .gitignore verwalten")
    print("17. Git-Logs anzeigen")
    print("18. Git-Status anzeigen")
    print("19. GitHub-Repositorys anzeigen")
    print("20. GitHub-Repositorys löschen")
    print("21. Beenden")
    drucke_trennlinie()

def menü(ordner):
    while True:
        drucke_trennlinie()
        menü_anzeigen()
        wahl = input("Wählen Sie eine Option: ")

        if wahl == "1":
            lokales_repo_erstellen_und_initialisieren(ordner)
        elif wahl == "2":
            lokales_repo_mit_github_verknüpfen(ordner)
        elif wahl == "3":
            änderungen_hinzufügen(ordner)
        elif wahl == "4":
            änderungen_commiten(ordner)
            drucke_trennlinie()
        elif wahl == "5":
            änderungen_pushen(ordner)
        elif wahl == "6":
            änderungen_pullen(ordner)
        elif wahl == "7":
            repo_klonen(ordner)
        elif wahl == "8":
            branch_erstellen(ordner)
        elif wahl == "9":
            branch_wechseln(ordner)
        elif wahl == "10":
            branches_auflisten(ordner)
        elif wahl == "11":
            merge_branch(ordner)
        elif wahl == "12":
            stash_änderungen(ordner)
        elif wahl == "13":
            konflikte_anzeigen(ordner)
        elif wahl == "14":
            pull_requests_auflisten(ordner)
        elif wahl == "15":
            gitignore_anzeigen(ordner)
        elif wahl == "16":
            gitignore_verwalten(ordner)
        elif wahl == "17":
            log_anzeigen(ordner)
        elif wahl == "18":
            status_anzeigen(ordner)
        elif wahl == "19":
            github_repositorys_anzeigen()
        elif wahl == "20":
            github_repository_löschen()
        elif wahl == "21":
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")
            drucke_trennlinie()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Bitte geben Sie den Ordnernamen als Argument an.")
    else:
        ordner_name = sys.argv[1]
        menü(ordner_name)
```