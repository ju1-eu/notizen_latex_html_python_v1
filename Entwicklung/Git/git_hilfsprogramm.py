"""
Dieses Skript bietet eine Benutzeroberfläche für verschiedene Git-Operationen,
die über ein einfaches Menüsystem zugänglich gemacht werden. Es ermöglicht Benutzern,
verschiedene Git-Befehle wie das Erstellen und Initialisieren von lokalen Repositories,
das Verknüpfen mit GitHub, das Hinzufügen, Commiten, Pushen und Pullen von Änderungen,
sowie fortgeschrittenere Operationen wie das Mergen von Branches, Stashing von Änderungen,
Anzeigen von Merge-Konflikten, Auflisten von Pull Requests und Verwalten der .gitignore-Datei
durchzuführen. Die `main`-Funktion dient als Einstiegspunkt und verarbeitet Benutzereingaben,
um die entsprechenden Aktionen basierend auf der Auswahl zu initiieren.

Jeder Befehl im `BEFEHLE`-Mapping ist einem Schlüssel zugeordnet, der eine Nummer enthält,
die die Aktion beschreibt, und einem Wert, der ein Dictionary mit dem Befehl selbst und einer
Beschreibung der Aktion enthält. Benutzer interagieren mit dem Menü, indem sie die Nummer der
gewünschten Aktion eingeben. Das Programm führt dann die entsprechende Funktion aus und zeigt
Ergebnisse oder Statusmeldungen im Terminal an.

Benutzung:
    python git_hilfsprogramm.py <Ordnername>

Argumente:
    Ordnername - Der Name des Verzeichnisses, in dem die Git-Operationen durchgeführt werden sollen.

Autor: Jan Unger
Version: 1.1
Datum: 2024-02-06
"""
import os
import re
import subprocess
import sys
import traceback
from dotenv import load_dotenv

import requests


GITHUB_URL = "https://github.com/ju1-eu/"
README_FILE = "README.md"
# Umgebungsvariablen aus der .env-Datei laden
load_dotenv()

# Zugriff auf den Token
github_token = os.getenv('GITHUB_TOKEN')

def ausfuehren_befehl(befehl, ordner):
    """
    Führt einen gegebenen Shell-Befehl im spezifizierten Ordner aus und fängt Fehler ab.
    Unterscheidet zwischen echten Fehlern und informativen Nachrichten in der Fehlerausgabe.
    """
    try:
        ergebnis = subprocess.run(befehl, check=True, cwd=ordner,
                                  text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Drucke normale Ausgabe
        if ergebnis.stdout:
            print("Ausgabe:", ergebnis.stdout)

        # Untersuche Fehlerausgabe, um echte Fehler von informativen Nachrichten zu unterscheiden
        # gh pr list  => no open pull requests in ju1-eu/testOrdner
        if ergebnis.stderr:
            # Beispiel: Erkenne bekannte informative Nachrichten
            if "Zu Branch" in ergebnis.stderr or "Bereits aktuell" in ergebnis.stderr:
                print("Info:", ergebnis.stderr)
            else:  # Für alle anderen Fälle, betrachte es als echten Fehler
                print("Fehlerausgabe  (Ignorierbar):", ergebnis.stderr)
    except subprocess.CalledProcessError as error:
        # Echte Fehler werden hier behandelt
        print(f"Fehler bei Ausführung des Befehls: {error.cmd}\nFehlerausgabe:\n{error.stderr}")



def sichere_eingabe(eingabeaufforderung):
    """
    Fordert den Benutzer zur Eingabe auf und validiert diese, um sicherzustellen,
    dass sie keine potenziell gefährlichen Zeichen enthält.
    """
    eingabe = input(eingabeaufforderung)
    if re.search(r"[;&|<>]", eingabe):
        print("Potenziell unsichere Eingabe erkannt. Bitte versuchen Sie es erneut.")
        return sichere_eingabe(eingabeaufforderung)
    return eingabe


def lokales_repo_erstellen_und_initialisieren(ordner):
    """
    Erstellt ein lokales Git-Repository in einem gegebenen Ordner und initialisiert es.
    """
    ordner_pfad = os.path.join(os.getcwd(), ordner)

    # ueberpruefen und Erstellen des Ordners, falls er nicht existiert
    if not os.path.exists(ordner_pfad):
        os.makedirs(ordner_pfad)

    # ueberpruefen, ob die .gitignore-Datei vorhanden ist, und erstellen, falls nicht
    gitignore_pfad = os.path.join(ordner_pfad, ".gitignore")
    if not os.path.exists(gitignore_pfad):
        with open(gitignore_pfad, 'w', encoding='utf-8') as gitignore:
            gitignore.write(
                "# Hier Dateien und Verzeichnisse angeben, die von der Versionskontrolle"
                " ausgeschlossen werden sollen\n")
    # Erstellen der README-Datei mit der ersten Zeile
    with open(os.path.join(ordner_pfad, README_FILE), 'w', encoding='utf-8') as readme:
        readme.write(
            "# " + ordner + " Repository\nThis is the README for the " + ordner + " repository.\n")

    # Git-Befehle ausfuehren
    befehle = [
        f"git init {ordner_pfad}",
        f"cd {ordner_pfad} && git add {README_FILE}"
    ]
    for befehl in befehle:
        ausfuehren_befehl(befehl, ordner_pfad)

    # ueberpruefen, ob es aenderungen gibt, die committet werden können
    prozess = subprocess.run(
        f"git -C {ordner_pfad} status -s", shell=True, text=True, check=True, capture_output=True)
    if prozess.stdout.strip():
        ausfuehren_befehl(
            f'cd {ordner_pfad} && git commit -m "first commit"', ordner_pfad)
    else:
        print(
            "Keine aenderungen im Arbeitsverzeichnis vorhanden. Es gibt nichts zu committen.")


def abfrage_repository_art():
    """
    Fragt den Benutzer, ob ein vorhandenes oder ein neues GitHub-Repository verwendet werden soll.
    """
    while True:
        entscheidung = input(
            "Möchten Sie ein bereits vorhandenes GitHub-Repository verwenden oder ein "
            "neues erstellen und verknuepfen? (vorhanden/neu): ").lower()
        if entscheidung in ['vorhanden', 'neu']:
            return entscheidung
        print("Ungueltige Auswahl. Bitte 'vorhanden' oder 'neu' eingeben.")


def lokales_repo_mit_github_verknuepfen(ordner):
    """
    Verknüpft ein lokales Git-Repository mit einem GitHub-Repository.
    """
    if not os.path.exists(ordner):
        print(f"Das Verzeichnis '{ordner}' existiert nicht.")
        return

    try:
        prozess = subprocess.run(
            "git remote get-url origin", shell=True, text=True, check=True, capture_output=True,
            cwd=ordner)
        if prozess.stdout:
            print("Fehler: Externes Repository origin existiert bereits.")
            return
    except subprocess.CalledProcessError:
        # Wenn dieser Block erreicht wird, bedeutet das, dass 'origin' nicht existiert
        pass

    entscheidung = abfrage_repository_art()

    if entscheidung == "vorhanden":
        github_repo_url = input("Geben Sie die URL des vorhandenen GitHub-Repositorys ein: ")
        subprocess.run(f"git remote add origin {github_repo_url}", shell=True, check=True,
                       cwd=ordner)
        subprocess.run("git branch -M main", shell=True, check=True, cwd=ordner)
        subprocess.run("git push -u origin main", shell=True, check=True, cwd=ordner)
        print(f"Das lokale Repository '{ordner}' wurde erfolgreich mit dem "
              "GitHub-Repository verknüpft.")
    elif entscheidung == "neu":
        # Stellen Sie sicher, dass GITHUB_URL korrekt definiert ist,
        # z.B. GITHUB_URL = "https://github.com/USERNAME/"
        github_repo_url = "https://github.com/USERNAME/"  # Beispiel-URL
        repo_name = input("Geben Sie den Namen für das neue GitHub-Repository ein: ")
        subprocess.run(f"gh repo create {repo_name} --public", shell=True, check=True, cwd=ordner)
        subprocess.run(f"git remote add origin https://github.com/ju1-eu/{repo_name}.git",
                       shell=True, check=True, cwd=ordner)
        subprocess.run("git branch -M main", shell=True, check=True, cwd=ordner)
        subprocess.run("git push -u origin main", shell=True, check=True, cwd=ordner)
        print(f"Das lokale Repository '{ordner}' wurde erfolgreich erstellt und mit "
              "einem neuen GitHub-Repository verknüpft.")
    else:
        print("Ungültige Auswahl. Bitte 'vorhanden' oder 'neu' eingeben.")



def commiten_und_pushen(ordner):
    """
    Führt Git-Operationen aus, um Dateien hinzuzufügen, zu commiten und zu pushen.
    """
    dateien = input(
        "Welche Dateien möchten Sie hinzufuegen? (z.B. 'file1.txt file2.txt' oder '.' fuer alle): ")
    commit_nachricht = input("Geben Sie eine Commit-Nachricht ein: ")
    befehl = (
        f"cd {ordner} && git add {dateien} && git commit -m '{commit_nachricht}' "
        "&& git push origin main"
    )
    ausfuehren_befehl(befehl, ordner)



def aenderungen_ziehen(ordner):
    """
    Zieht Änderungen vom Hauptzweig des Remote-Repositorys in das lokale Repository.
    """
    ausfuehren_befehl(f"cd {ordner} && git pull origin main", ordner)


def aenderungen_hinzufuegen(ordner):
    """
    Fügt Änderungen zu einem lokalen Git-Repository hinzu.
    """
    datei = input("Welche Datei möchten Sie hinzufuegen? (Alles: .): ")
    ausfuehren_befehl(f"git add {datei}", os.path.join(os.getcwd(), ordner))


def aenderungen_commiten(ordner):
    """
    Commitet Änderungen in einem lokalen Git-Repository.
    """
    # Vor dem Commit ueberpruefen, ob es aenderungen gibt
    status_prozess = subprocess.run(
        f"git -C {ordner} status -s", shell=True, text=True, check=True, capture_output=True)
    status_output = status_prozess.stdout.strip()
    if not status_output:
        print(
            "Keine aenderungen im Arbeitsverzeichnis vorhanden. Es gibt nichts zu committen.")
        return

    nachricht = input("Geben Sie eine Commit-Nachricht ein: ")
    ausfuehren_befehl(f'git commit -m "{nachricht}"', ordner)


def repo_klonen(ordner):
    """
    Klont ein ausgewähltes GitHub-Repository in einen lokalen Ordner.

    Fragt den Benutzer nach der Auswahl eines Repositories aus der Liste der verfügbaren
    Repositories eines GitHub-Benutzers. Das ausgewählte Repository wird dann in den angegebenen
    lokalen Ordner geklont.
    Stellt sicher, dass der Zielordner nicht existiert oder leer ist, bevor das Klonen durchgeführt
    wird. Verwendet die globale Variable GITHUB_URL, um die Basis-URL für
    GitHub-Repository-Operationen zu definieren.

    Args:
    - ordner (str): Der Pfad des lokalen Ordners, in den das Repository geklont werden soll.

    Returns:
    - None: Die Funktion gibt nichts zurück, druckt jedoch relevante Nachrichten während
        der Ausführung.
    """
    # Stellen Sie sicher, dass GITHUB_URL korrekt definiert ist und
    # das Schema beinhaltet, z.B. https://github.com/
    repositories = get_user_repositories(get_username_from_url(GITHUB_URL))

    if repositories:
        print("Verfuegbare Repositories zum Klonen:\n")
        for idx, repo in enumerate(repositories, start=1):
            print(f"{idx}. Repository: {repo['name']}\n   URL: {GITHUB_URL}{repo['name']}\n")

        auswahl = int(input("Geben Sie die Nummer des Repositories ein, das Sie klonen möchten, "
                            "oder 0 zum Abbrechen: "))

        if 0 < auswahl <= len(repositories):
            repo_info = repositories[auswahl - 1]
            ziel_ordner = os.path.join(ordner, repo_info["name"])

            if os.path.exists(ziel_ordner) and os.listdir(ziel_ordner):
                print("Fehler: Zielordner existiert bereits und ist nicht leer.")
                return

            print(f"Klone das Repository '{repo_info['name']}' in den Ordner '{repo_info['name']}'.")
            #git clone https://github.com/ju1-eu/hello-world ./hello-world
            ausfuehren_befehl(["git", "clone", GITHUB_URL + repo_info["name"], repo_info["name"]], ordner)
            print(f"Repository '{repo_info['name']}' wurde erfolgreich geklont.")
        elif auswahl == 0:
            print("Befehl wurde abgebrochen.")
        else:
            print("Ungültige Auswahl.")
    else:
        print("Keine öffentlichen Repositories gefunden.")


def aenderungen_pushen(ordner):
    """
    Führt das Pushen der lokalen Änderungen an den Hauptzweig (main) des Remote-Repositorys durch.

    Nutzt die Funktion `ausfuehren_befehl`, um den Git-Befehl `git push -u origin main` im
    spezifizierten Ordner auszuführen. Dies aktualisiert das Remote-Repository mit allen lokalen
    Änderungen, die an den Hauptzweig (main) committed wurden.

    Args:
    - ordner (str): Der Pfad des lokalen Repository-Ordners, von dem aus die Änderungen gepusht
        werden sollen.
    """
    ausfuehren_befehl("git push -u origin main", ordner)



def alle_branches_anzeigen(ordner):
    """
    Zeigt alle lokalen und Remote-Branches in einem Git-Repository an.
    """
    try:
        subprocess.run("git fetch --all", shell=True, check=True, cwd=ordner, text=True)
        prozess = subprocess.run("git branch -a", shell=True, text=True, check=True,
                                 capture_output=True, cwd=ordner)
        print(prozess.stdout)
    except subprocess.CalledProcessError as error:
        print(f"Fehler beim Anzeigen der Branches: {error}")

def aenderungen_pullen(ordner):
    """
    Überprüft das Arbeitsverzeichnis auf uncommitierte Änderungen und ermöglicht
    dem Benutzer, Änderungen von einem spezifischen Remote-Branch zu ziehen.
    """
    try:
        prozess = subprocess.run("git status --porcelain", shell=True, check=True,  text=True,
                                 capture_output=True, cwd=ordner)
        if prozess.stdout.strip():
            print("Es gibt uncommitierte Änderungen im Arbeitsverzeichnis. Bitte committen "
                  "oder stashen Sie diese, bevor Sie Änderungen ziehen.")
            return

        # Zeigt alle Branches vor dem Pull an, um dem Benutzer zu helfen, eine Wahl zu treffen
        alle_branches_anzeigen(ordner)

        remote_branch = input("Geben Sie den Remote-Branch ein, von dem Sie Änderungen "
                              "ziehen möchten (z.B. main): ")
        # Entfernen des "remotes/origin/" Teils, falls vorhanden
        if remote_branch.startswith("remotes/origin/"):
            remote_branch = remote_branch.replace("remotes/origin/", "")

        ausfuehren_befehl(f"git pull origin {remote_branch}", ordner)

    except subprocess.CalledProcessError as error:
        print(f"Fehler beim Pullen der Änderungen: {error}")


def branch_erstellen(ordner):
    """
    Erstellt einen neuen Branch im angegebenen lokalen Git-Repository.
    """
    branch_name = input("Geben Sie den Namen des neuen Branches ein: ")
    ausfuehren_befehl(f"git checkout -b {branch_name}", ordner)


def branch_wechseln(ordner):
    """Branch wechseln"""
    branch_name = input("Zu welchem Branch möchten Sie wechseln?: ")
    befehl = ["git", "checkout", branch_name]
    ausfuehren_befehl(befehl, os.path.join(os.getcwd(), ordner))




def merge_branch(ordner):
    """"Diese Funktion ermöglicht die Integration der Änderungen aus einem separaten
    Entwicklungszweig in den aktuellen Branch"""
    branch_name = input(
        "Welchen Branch möchten Sie in den aktuellen Branch mergen?: ")
    ausfuehren_befehl(f"git merge {branch_name}", ordner)


def stash_aenderungen(ordner):
    """Funktion ermöglicht es dem Benutzer, uncommittete Änderungen im aktuellen Arbeitsverzeichnis
    temporär zu sichern, ohne einen Commit erstellen zu müssen. Diese Funktionalität ist besonders
    nützlich, um eine saubere Arbeitskopie zu erhalten, wenn man zwischen Branches wechseln muss,
    ohne dabei den aktuellen Arbeitsfortschritt zu verlieren."""
    ausfuehren_befehl("git stash", ordner)
    print("aenderungen wurden gestashed.")


def konflikte_anzeigen(ordner):
    """Diese Funktion dient der Identifikation von Dateien, die Merge-Konflikte enthalten
    Merge-Konflikte treten auf, wenn Git nicht in der Lage ist, Änderungen aus
    unterschiedlichen Branches automatisch zusammenzuführen."""
    ausfuehren_befehl("git diff --name-only --diff-filter=U", ordner)
    print("Oben sind die Dateien mit Merge-Konflikten aufgelistet.")


def pull_requests_auflisten(ordner):
    """Liste der Pull Requests für das Repository anzuzeigen"""
    print("Beachten Sie, dass dies nur funktioniert, wenn Sie ueber "
          "das GitHub CLI-Tool 'gh' verfuegen.")
    ausfuehren_befehl("gh pr list", ordner)



def gitignore_verwalten(ordner):
    """
    Bietet eine Benutzerschnittstelle zur Verwaltung der .gitignore-Datei in einem gegebenen Ordner.

    Erlaubt dem Benutzer, die aktuelle .gitignore-Datei anzuzeigen oder eine neue Regel
    hinzuzufügen.
    Bei der Auswahl werden die entsprechenden Aktionen ausgeführt: Anzeigen des Inhalts
    von .gitignore oder Hinzufügen einer neuen Regel zur Datei.

    Args:
    - ordner (str): Der Pfad des Ordners, der das Git-Repository enthält und dessen .gitignore-Datei
                    verwaltet werden soll.
    """
    print("1. .gitignore anzeigen")
    print("2. Eine neue Regel zu .gitignore hinzufuegen")
    auswahl = input("Wählen Sie eine Option: ")
    gitignore_pfad = os.path.join(ordner, ".gitignore")  # Pfadoptimierung

    if auswahl == "1":
        # ueberpruefen, ob die .gitignore-Datei vorhanden ist
        if os.path.exists(gitignore_pfad):
            with open(gitignore_pfad, 'r', encoding='utf-8') as file:
                print(file.read())
        else:
            print(".gitignore existiert nicht in diesem Repository.")
    elif auswahl == "2":
        regel = input("Geben Sie die Regel ein, die Sie hinzufuegen möchten: ")
        with open(gitignore_pfad, 'a', encoding='utf-8') as file:
            file.write(f"\n{regel}")
        print(f"Regel '{regel}' zu .gitignore hinzugefuegt.")


def log_anzeigen(ordner):
    """
    Zeigt den Git-Log für das angegebene lokale Repository an.
    """
    ausfuehren_befehl("git lg", ordner)


def status_anzeigen(ordner):
    """
    Zeigt eine Erklärung der möglichen Statusmeldungen von Git und führt dann den Befehl `git status`
    aus, um den aktuellen Status des Repositories im angegebenen Ordner anzuzeigen.

    Die Ausgabe umfasst Informationen über den aktuellen Branch, Änderungen im Vergleich zum
    Remote-Branch sowie den Status von Dateien (modifiziert, hinzugefügt, gelöscht, ungetrackt).

    Args:
    - ordner (str): Der Pfad des Ordners, der das Git-Repository enthält.
    """
    print("Erklärung")
    print("## zeigt den aktuellen Branch an, gefolgt von den Änderungen "
          "in Bezug auf den Remote-Branch.")
    print("M - Geänderte Datei (modifiziert)")
    print("A - Hinzugefügte Datei (neu hinzugefügt)")
    print("D - Gelöschte Datei")
    print("?? - Ungetrackte Datei\n")
    ausfuehren_befehl("git status", ordner)


def get_user_repositories(username):
    """
    Ruft alle öffentlichen GitHub-Repositories eines bestimmten Benutzers ab.
    """
    page_number = 1
    repositories = []
    headers = {"Authorization": f"token {github_token}"} if github_token else {}

    while True:
        response = requests.get(
            f"https://api.github.com/users/{username}/repos?page={page_number}&per_page=100",
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            current_page_repos = response.json()

            if not current_page_repos:
                break

            repositories.extend(current_page_repos)
            page_number += 1
        else:
            print(
                f"Fehler beim Abrufen der Repositories fuer Benutzer {username} "
                f"auf Seite {page_number}. Statuscode: {response.status_code}")
            break

    return repositories

def get_username_from_url(url):
    """
    Extrahiert den Benutzernamen aus einer GitHub-URL.
    """
    match = re.match(r"https://github.com/([^/]+)/?$", url)
    if match:
        return match.group(1)
    return None



def github_repositorys_anzeigen():
    """
    Zeigt eine Liste der öffentlichen GitHub-Repositories für einen Benutzer an.
    """
    username_match = re.match(r"https://github.com/(.*)/$", GITHUB_URL)
    if username_match:
        username = username_match.group(1)
        repositories = get_user_repositories(username)

        if repositories:
            print(f"Öffentliche Repositories fuer Benutzer {username}:\n")
            for index, repo in enumerate(repositories, start=1):
                repo_name = repo["name"]
                repo_url = GITHUB_URL + repo_name
                print(f"{index}. Repository: {repo_name}\nURL: {repo_url}\n")
        else:
            print("Keine öffentlichen Repositories gefunden.")
    else:
        print("Ungueltige GITHUB_URL. Stellen Sie sicher, dass der Benutzername "
              "in der URL enthalten ist.")


def github_repository_loeschen(ordner):
    repo_name = input("Geben Sie den Namen des zu löschenden Repositories ein: ")
    ausfuehren_befehl(["gh", "repo", "delete", repo_name, "--yes"], ordner)





def zeige_menue_und_waehle():
    """
    Zeigt ein Menü mit verschiedenen Git-Operationen und wartet auf die Benutzerauswahl.

    Das Menü listet eine Reihe von Aktionen auf, die mit Git und GitHub durchgeführt werden können,
    wie das Erstellen und Verbinden von Repositories, das Hinzufügen, Commiten, Pushen und Pullen
    von Änderungen, das Verwalten von Branches und .gitignore, das Anzeigen von Logs und Status,
    sowie das Anzeigen und Löschen von GitHub-Repositories.

    Die Funktion erwartet die Eingabe des Benutzers und gibt die getroffene Auswahl zurück.
    Der Benutzer kann 'q' eingeben, um das Programm zu beenden.

    Returns:
        str: Die vom Benutzer getroffene Auswahl als Zeichenkette.
    """
    print("""
1. Neues lokales Repository erstellen
2. Neues Repository auf GitHub verbinden
3. Änderungen hinzufuegen (git add)
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
15. .gitignore verwalten
16. Git-Logs anzeigen
17. Git-Status anzeigen
18. GitHub-Repositorys anzeigen
19. GitHub-Repositorys löschen
q. Beenden
""")
    auswahl = input("Wählen Sie eine Option (oder 'q' zum Beenden): ")
    return auswahl



def sicherer_aufruf(funktion, *args, **kwargs):
    """
    Führt eine übergebene Funktion sicher aus und fängt dabei gängige Ausnahmen.

    Diese Funktion versucht, die übergebene Funktion mit den angegebenen Argumenten und
    Schlüsselwortargumenten auszuführen. Sie fängt spezifische Ausnahmen wie FileNotFoundError
    und PermissionError, sowie als Fallback alle anderen Exception-Ausnahmen,
    um robuste Fehlerbehandlung zu ermöglichen. Bei einem unerwarteten Fehler wird
    zusätzlich ein Stack-Trace ausgegeben.

    Args:
        funktion (callable): Die auszuführende Funktion.
        *args: Variable Positionalargumente für die Funktion.
        **kwargs: Variable Schlüsselwortargumente für die Funktion.

    Returns:
        None

    Zeigt Fehlermeldungen in der Konsole an und gibt bei spezifischen Fehlern oder unerwarteten
    Ausnahmen entsprechende Hinweise.
    """
    try:
        funktion(*args, **kwargs)
    except FileNotFoundError as error:
        print(f"Datei nicht gefunden: {error}")
    except PermissionError as error:
        print(f"Keine Berechtigung zum Ausführen dieser Operation: {error}")
    except Exception as error:  # Als Fallback, wenn Sie dennoch alle Fehler fangen möchten
        print(f"Ein unerwarteter Fehler ist aufgetreten: {error}")
        traceback.print_exc()  # Gibt den Stack-Trace des Fehlers aus




def pause():
    """
    Pausiert die Ausführung des Programms, bis der Benutzer Enter drückt.

    Diese Funktion wird verwendet, um den Programmfluss anzuhalten und dem Benutzer Zeit zu geben,
    die bisherigen Ausgaben zu überprüfen, bevor das Programm mit der Ausführung fortfährt.
    """
    input("Drücken Sie Enter, um fortzufahren...")


# Mapping der Befehle
BEFEHLE = {
    1: {"command": lokales_repo_erstellen_und_initialisieren, "description": "Neues lokales Repository erstellen"},
    2: {"command": lokales_repo_mit_github_verknuepfen, "description": "Neues Repository auf GitHub verbinden"},
    3: {"command": aenderungen_hinzufuegen, "description": "Änderungen hinzufügen (git add)"},
    4: {"command": aenderungen_commiten, "description": "Änderungen commiten (git commit)"},
    5: {"command": aenderungen_pushen, "description": "Änderungen pushen (git push)"},
    6: {"command": aenderungen_pullen, "description": "Änderungen pullen (git pull)"},
    7: {"command": repo_klonen, "description": "Repository klonen"},
    8: {"command": branch_erstellen, "description": "Branch erstellen"},
    9: {"command": branch_wechseln, "description": "Zu einem Branch wechseln"},
    10: {"command": alle_branches_anzeigen, "description": "Alle Branches auflisten"},
    11: {"command": merge_branch, "description": "Merge eines Branches"},
    12: {"command": stash_aenderungen, "description": "Änderungen stashen"},
    13: {"command": konflikte_anzeigen, "description": "Merge-Konflikte anzeigen"},
    14: {"command": pull_requests_auflisten, "description": "Pull Requests auflisten"},
    15: {"command": gitignore_verwalten, "description": ".gitignore verwalten"},
    16: {"command": log_anzeigen, "description": "Git-Logs anzeigen"},
    17: {"command": status_anzeigen, "description": "Git-Status anzeigen"},
    18: {"command": github_repositorys_anzeigen, "description": "GitHub-Repositorys anzeigen"},
    19: {"command": github_repository_loeschen, "description": "GitHub-Repositorys löschen"}
    # Weitere Befehle können hier ergänzt werden.
}


def main():
    """
    Hauptfunktion des Skripts. Verarbeitet Benutzereingaben aus der Kommandozeile,
    zeigt ein Menü der verfügbaren Git-Operationen an und führt die vom Benutzer
    ausgewählte Operation aus. Verwendet das Mapping `BEFEHLE` zur Zuordnung von
    Befehlen zu Menüoptionen.
    """
    if len(sys.argv) != 2:
        print("Bitte geben Sie den Ordnernamen als Argument an.")
        return

    ordner_name = sys.argv[1]

    while True:
        auswahl = zeige_menue_und_waehle()
        if auswahl == 'q':
            print("Programm beendet.")
            break

        try:
            auswahl_num = int(auswahl)
        except ValueError:
            print("Ungültige Auswahl. Bitte geben Sie eine Zahl ein.")
            continue

        if auswahl_num in BEFEHLE:
            print("\n==================================================\n")
            befehl = BEFEHLE[auswahl_num]['command']

            # Überprüfen, ob die Funktion `ordner_name` benötigt
            if auswahl_num in [18]:
                sicherer_aufruf(befehl)  # Keine Argumente
            else:
                sicherer_aufruf(befehl, ordner_name)

            print("==================================================")
            pause()
        else:
            print("Ungültige Auswahl. Bitte erneut versuchen.")


if __name__ == "__main__":
    main()
