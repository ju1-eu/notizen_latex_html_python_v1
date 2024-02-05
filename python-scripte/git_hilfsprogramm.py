"""
Dieses Skript automatisiert Git-Operationen, um den Workflow mit lokalen und entfernten
Git-Repositories zu vereinfachen.
Es bietet Funktionen für gängige Git-Aufgaben wie das Erstellen und Initialisieren
lokaler Repositories, das Verknüpfen mit GitHub,
das Hinzufügen, Commiten, Pushen und Pullen von Änderungen, das Verwalten von Branches und
das Anzeigen von Repository-Informationen.

Funktionsübersicht:
- Erstellen und Initialisieren eines lokalen Git-Repositories.
- Verknüpfen eines lokalen Repositories mit einem entfernten GitHub-Repository.
- Hinzufügen von Änderungen zum Staging-Bereich und Commiten dieser Änderungen.
- Pushen von Änderungen zu einem entfernten Repository und Pullen von Änderungen.
- Erstellen, Wechseln und Zusammenführen von Branches.
- Anzeigen von Status, Logs und Konflikten.
- Stashen von Änderungen und Löschen eines GitHub-Repositories.

Verwendung:
Das Skript wird über die Kommandozeile mit dem Namen des Zielordners als Argument aufgerufen, z.B.:
    python3 git_hilfsprogramm.py MeinProjekt

Es startet ein interaktives Menü, das es dem Benutzer ermöglicht, verschiedene Git-Operationen
auszuführen, indem die entsprechende Menüoption ausgewählt wird.

Anforderungen:
- Git muss auf dem System installiert und konfiguriert sein.
- Für einige Funktionen ist das GitHub CLI-Tool 'gh' erforderlich.
- Eine Internetverbindung ist für Operationen mit entfernten Repositories erforderlich.

Dieses Skript zielt darauf ab, die Verwendung von Git zu vereinfachen und Routineaufgaben
zu automatisieren, um die Effizienz bei der Versionskontrolle und Zusammenarbeit zu steigern.
"""
import subprocess
import os
import re
import sys
import requests


GITHUB_URL = "https://github.com/ju1-eu/"
README_FILE = "README.md"


def ausfuehren_befehl(befehl, ordner):
    """
    Führt einen gegebenen Shell-Befehl in einem spezifizierten Ordner aus und behandelt Fehler.

    Diese Funktion versucht, einen Shell-Befehl auszuführen, indem sie `subprocess.run` verwendet.
    Sie gibt die Standardausgabe des Befehls aus und kehrt mit True zurück, wenn der Befehl
    erfolgreich war.
    Bei einem Fehler im Befehl (gefangen als `subprocess.CalledProcessError`) wird der Benutzer
    gefragt,ob der Befehl erneut ausgeführt werden soll. Dies gibt dem Benutzer die Möglichkeit,
    auf Fehler zu reagieren und gegebenenfalls den Befehl zu wiederholen.

    Args:
        befehl (str): Der Shell-Befehl, der ausgeführt werden soll.
        ordner (str): Der Pfad des Ordners, in dem der Befehl ausgeführt werden soll.

    Returns:
        bool: True, wenn der Befehl erfolgreich ausgeführt wurde, False bei einem Fehler
              und darauf folgender Abbruch durch den Benutzer.

    Sicherheitshinweis:
        Die Verwendung von `shell=True` kann ein Sicherheitsrisiko darstellen, insbesondere
        wenn der Befehl aus unsicheren Quellen stammt oder Benutzereingaben enthält. Stellen Sie
        sicher, dass der Befehl vertrauenswürdig ist oder vermeiden Sie die direkte Ausführung
        von Benutzereingaben.
    """
    max_versuche = 3  # Maximale Anzahl von Versuchen
    for versuch in range(max_versuche):
        try:
            prozess = subprocess.run(befehl, shell=True, text=True, capture_output=True,
                                     check=True, cwd=ordner)
            print(prozess.stdout)
            return True
        except subprocess.CalledProcessError as error:
            print(f"Fehler bei Ausführung des Befehls: {error.cmd}\nFehlerausgabe:\n{error.stderr}\n{error.stdout}")
            if versuch < max_versuche - 1:
                entscheidung = input(
                    "Möchten Sie den Befehl erneut ausführen? (ja/nein): ").lower()
                if entscheidung != "ja":
                    print("Befehl wurde abgebrochen.")
                    break
            else:
                print(
                    "Maximale Anzahl von Versuchen erreicht. Befehl wurde abgebrochen.")
    return False


def sichere_eingabe(eingabeaufforderung):
    """
    Fordert den Benutzer zur Eingabe auf und validiert diese auf potenziell unsichere Zeichen.

    Diese Funktion verhindert, dass Eingaben mit bestimmten Zeichen, die in Shell-Befehlen
    missbraucht werden könnten (wie z.B. ;, &, |, <, >), akzeptiert werden.
    Bei Erkennung solcher Zeichen wird der Benutzer aufgefordert, seine Eingabe zu wiederholen.

    Args:
        eingabeaufforderung (str): Der Text, der dem Benutzer als Aufforderung angezeigt wird.

    Returns:
        str: Die vom Benutzer eingegebene Zeichenfolge, die keine unsicheren Zeichen enthält.
    """
    eingabe = input(eingabeaufforderung)
    if re.search(r"[;&|<>]", eingabe):
        print("Potenziell unsichere Eingabe erkannt. Bitte versuchen Sie es erneut.")
        return sichere_eingabe(eingabeaufforderung)
    return eingabe


def lokales_repo_erstellen_und_initialisieren(ordner):
    """
    Erstellt und initialisiert ein lokales Git-Repository in einem angegebenen Ordner.

    Dies umfasst die Erstellung des Ordners (falls er noch nicht existiert), die Initialisierung
    des Git-Repositories, sowie das Hinzufügen einer .gitignore- und einer README-Datei.
    Anschließend werden die Dateien zum Repository hinzugefügt und ein erster Commit durchgeführt,
    falls Änderungen vorhanden sind.

    Args:
        ordner (str): Der Name des Ordners, in dem das Repository erstellt werden soll.

    Die Funktion führt mehrere Git-Befehle aus und nutzt dabei eine Hilfsfunktion
    `ausfuehren_befehl` für die Ausführung und Fehlerbehandlung. Es wird angenommen, dass
    diese Hilfsfunktion existiert und korrekt implementiert ist.

    Hinweis: Bei der Ausführung von Shell-Befehlen werden potenzielle Sicherheitsrisiken
    berücksichtigt. Die Funktion ist für den Einsatz in vertrauenswürdigen Umgebungen gedacht.
    """
    ordner_pfad = os.path.join(os.getcwd(), ordner)

    # Überprüfen und Erstellen des Ordners, falls er nicht existiert
    if not os.path.exists(ordner_pfad):
        os.makedirs(ordner_pfad)

    # Überprüfen, ob die .gitignore-Datei vorhanden ist, und erstellen, falls nicht
    gitignore_pfad = os.path.join(ordner_pfad, ".gitignore")
    if not os.path.exists(gitignore_pfad):
        with open(gitignore_pfad, 'w', encoding='utf-8') as gitignore:
            gitignore.write(
                "# Hier Dateien und Verzeichnisse angeben, die von der Versionskontrolle "
                "ausgeschlossen werden sollen\n")
    # Erstellen der README-Datei mit der ersten Zeile
    with open(os.path.join(ordner_pfad, README_FILE), 'w', encoding='utf-8') as readme:
        readme.write(f"# {ordner} Repository\nThis is the README for the {ordner} repository.\n")

    # Git-Befehle ausführen
    befehle = [
        f"git init {ordner_pfad}",
        f"cd {ordner_pfad} && git add {README_FILE}"
    ]
    for befehl in befehle:
        ausfuehren_befehl(befehl, ordner_pfad)

    # Überprüfen, ob es Änderungen gibt, die committet werden können
    prozess = subprocess.run(["git", "-C", ordner_pfad, "status", "-s"],
                             check=True, text=True, capture_output=True)
    if prozess.stdout.strip():
        ausfuehren_befehl(
            f'cd {ordner_pfad} && git commit -m "first commit"', ordner_pfad)
    else:
        print(
            "Keine Änderungen im Arbeitsverzeichnis vorhanden. Es gibt nichts zu committen.")


def lokales_repo_mit_github_verknuepfen(ordner):
    if not os.path.exists(ordner):
        print(f"Das Verzeichnis '{ordner}' existiert nicht.")
        return

    prozess = subprocess.run(
        "git remote show origin", shell=True, text=True, check=True, capture_output=True,
        cwd=ordner)
    if "fatal: Remote origin already exists." in prozess.stderr:
        print("Fehler: Externes Repository origin existiert bereits.")
        return

    entscheidung = input(
        "Möchten Sie ein bereits vorhandenes GitHub-Repository verwenden oder ein neues erstellen "
        "und verknüpfen? (vorhanden/neu): ").lower()

    if entscheidung == "vorhanden":
        github_repo_url = input(
            "Geben Sie die URL des vorhandenen GitHub-Repositorys ein: ")
        subprocess.run(f"git remote add origin {github_repo_url}", shell=True, cwd=ordner, check=True)
        subprocess.run("git branch -M main", shell=True,
                       cwd=ordner, check=True)
        subprocess.run("git push -u origin main",
                       shell=True, cwd=ordner, check=True)
        print(f"Das lokale Repository '{ordner}' wurde erfolgreich mit dem GitHub-Repository verknüpft.")
    elif entscheidung == "neu":
        befehl = f"""
        gh repo create {ordner} --public
        git remote add origin {GITHUB_URL}{ordner}
        git branch -M main
        git push -u origin main
        """
        ausfuehren_befehl(befehl, ordner)
        print(f"Das lokale Repository '{ordner}' wurde erfolgreich erstellt und mit einem neuen GitHub-Repository verknüpft.")
    else:
        print("Ungültige Auswahl. Bitte 'vorhanden' oder 'neu' eingeben.")


def commiten_und_pushen(ordner):
    dateien = input(
        "Welche Dateien möchten Sie hinzufügen? (z.B. 'file1.txt file2.txt' oder '.' für alle): ")
    commit_nachricht = input("Geben Sie eine Commit-Nachricht ein: ")
    befehl = f"cd {ordner} && git add {dateien} && git commit -m '{commit_nachricht}' && git push origin main"
    ausfuehren_befehl(befehl)


def aenderungen_ziehen(ordner):
    ausfuehren_befehl("cd {ordner} && git pull origin main")


def status_anzeigen(ordner):
    print("Erklärung")
    print("## zeigt den aktuellen Branch an, gefolgt von den Änderungen in Bezug "
          "auf den Remote-Branch.")
    print("M - Geänderte Datei (modifiziert)")
    print("A - Hinzugefügte Datei (neu hinzugefügt)")
    print("D - Gelöschte Datei")
    print("?? - Ungetrackte Datei")
    drucke_trennlinie()
    ausfuehren_befehl("git status -s -b -u", os.path.join(os.getcwd(), ordner))


def zu_branch_wechseln(ordner):
    branch_name = input(
        "Geben Sie den Namen des Branches ein, zu dem Sie wechseln möchten: ")
    ausfuehren_befehl(f"cd {ordner} && git checkout {branch_name}")


def log_anzeigen(ordner):
    ausfuehren_befehl("git log", os.path.join(os.getcwd(), ordner))


def aenderungen_hinzufuegen(ordner):
    # Vor dem Commit überprüfen, ob es Änderungen gibt
    status_prozess = subprocess.run(
        f"git -C {ordner} status -s", shell=True, text=True, capture_output=True, check=True)
    status_output = status_prozess.stdout.strip()
    if not status_output:
        print(
            "Keine Änderungen im Arbeitsverzeichnis vorhanden. Es gibt nichts zu committen.")
        return

    nachricht = input("Geben Sie eine Commit-Nachricht ein: ")
    ausfuehren_befehl(f'git commit -m "{nachricht}"', ordner)


def repo_klonen(ordner):
    repositories = get_user_repositories(get_username_from_url(GITHUB_URL))

    if repositories:
        print("Verfügbare Repositories zum Klonen:\n")
        for idx, repo in enumerate(repositories, start=1):
            repo_name = repo["name"]
            repo_url = GITHUB_URL + repo_name
            print(f"{idx}. Repository: {repo_name}\n   URL: {repo_url}\n")

        try:
            auswahl = int(input(
                "Geben Sie die Nummer des Repositories ein, das Sie klonen möchten, oder "
                "0 zum Abbrechen: "))

            if 0 < auswahl <= len(repositories):
                repo_name = repositories[auswahl - 1]["name"]

                repo_url = GITHUB_URL + repo_name
                print(f"Klone das Repository '{repo_name}' von der URL '{repo_url}' in den Ordner '{ordner}'.")

                ausfuehren_befehl(f"git clone '{repo_url}' .", ordner)

                print(f"Repository '{repo_name}' wurde erfolgreich in den Ordner '{ordner}' geklont.")
            elif auswahl == 0:
                print("Befehl wurde abgebrochen.")
            else:
                print("Ungültige Auswahl.")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Nummer ein.")
    else:
        print("Keine öffentlichen Repositories gefunden.")


def aenderungen_pushen(ordner):
    ausfuehren_befehl("git push -u origin main", ordner)


def aenderungen_pushen(ordner):
    prozess = subprocess.run("git status --porcelain", shell=True, text=True, check=True,
                             capture_output=True, cwd=os.path.join(os.getcwd(), ordner))
    if prozess.stdout.strip():
        print("Es gibt uncommitierte Änderungen im Arbeitsverzeichnis. Bitte committen oder "
              "staschen Sie diese, bevor Sie Änderungen ziehen.")
        return

    remote_branch = input(
        "Geben Sie den Remote-Branch ein, von dem Sie Änderungen ziehen möchten: ")
    ausfuehren_befehl(f"git pull origin {remote_branch}", os.path.join(os.getcwd(), ordner))


def branch_erstellen(ordner):
    branch_name = sichere_eingabe(
        "Geben Sie den Namen des neuen Branches ein: ")
    ausfuehren_befehl(
        f"git checkout -b {branch_name}", os.path.join(os.getcwd(), ordner))


def branch_wechseln(ordner):
    branch_name = sichere_eingabe("Zu welchem Branch möchten Sie wechseln?: ")
    ausfuehren_befehl(f"git checkout {branch_name}",
                      os.path.join(os.getcwd(), ordner))


def branches_auflisten(ordner):
    ausfuehren_befehl("git branch", os.path.join(os.getcwd(), ordner))


def merge_branch(ordner):
    branch_name = input(
        "Welchen Branch möchten Sie in den aktuellen Branch mergen?: ")
    ausfuehren_befehl(f"git merge {branch_name}", ordner)


def stash_aenderungen(ordner):
    ausfuehren_befehl("git stash", ordner)
    print("Änderungen wurden gestashed.")


def gitignore_verwalten(ordner):
    print("1. .gitignore anzeigen")
    print("2. Eine neue Regel zu .gitignore hinzufügen")
    auswahl = input("Wählen Sie eine Option: ")
    if auswahl == "1":
        gitignore_anzeigen(ordner)
    elif auswahl == "2":
        regel = input("Geben Sie die Regel ein, die Sie hinzufügen möchten: ")
        with open(os.path.join(ordner, ".gitignore"), 'a', encoding='utf-8') as file:
            file.write(f"\n{regel}")
        print(f"Regel '{regel}' zu .gitignore hinzugefügt.")


def konflikte_anzeigen(ordner):
    ausfuehren_befehl("git diff --name-only --diff-filter=U", ordner)
    print("Oben sind die Dateien mit Merge-Konflikten aufgelistet.")


def pull_requests_auflisten(ordner):
    print("Beachten Sie, dass dies nur funktioniert, wenn Sie über das GitHub "
          "CLI-Tool 'gh' verfügen.")
    ausfuehren_befehl("gh pr list", ordner)


def gitignore_anzeigen(ordner):
    gitignore_path = os.path.join(ordner, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print(".gitignore existiert nicht in diesem Repository.")


def get_user_repositories(username):
    response = requests.get(f"https://api.github.com/users/{username}/repos")

    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print(f"Fehler beim Abrufen der Repositories für Benutzer {username}. Statuscode: {response.status_code}")
        return []


def get_username_from_url(url):
    match = re.match(r"https://github.com/(.*)/$", url)
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
        print("Ungültige GITHUB_URL. Stellen Sie sicher, dass der Benutzername in der URL "
              "enthalten ist.")


def github_repository_loeschen():
    repository_name = input(
        "Geben Sie den Namen des zu löschenden Repositories ein: ")
    befehl = f"gh repo delete {repository_name}"
    erneut_ausfuehren = True

    while erneut_ausfuehren:
        erneut_ausfuehren = False
        try:
            ausfuehren_befehl(befehl + " --yes", '.')
            print(f"Repository '{repository_name}' wurde erfolgreich gelöscht.")
        except subprocess.CalledProcessError as error:
            print(f"Fehler bei Ausführung des Befehls: {error.cmd}\nFehlerausgabe:\n{error.stderr}\n{error.stdout}")
            entscheidung = input(
                "Möchten Sie den Befehl erneut ausführen? (ja/nein): ").lower()
            if entscheidung == "ja":
                erneut_ausfuehren = True
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
            lokales_repo_mit_github_verknuepfen(ordner)
        elif wahl == "3":
            aenderungen_hinzufuegen(ordner)
        elif wahl == "4":
            aenderungen_hinzufuegen(ordner)
            drucke_trennlinie()
        elif wahl == "5":
            aenderungen_pushen(ordner)
        elif wahl == "6":
            aenderungen_pushen(ordner)
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
            stash_aenderungen(ordner)
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
            github_repository_loeschen()
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
