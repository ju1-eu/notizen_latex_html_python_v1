# Backup und Quellcodeverwaltung mit Git

Git ermöglicht nicht nur die Versionierung und sichere Aufbewahrung deines Codes, sondern auch eine effiziente Zusammenarbeit in Teams.

## Git-Repository initialisieren

Starte damit, ein Git-Repository in deinem Projektverzeichnis zu erstellen. Dies ermöglicht es dir, Änderungen am Code zu verfolgen und Versionen zu verwalten.

1. **Öffne ein Terminal** und navigiere zu deinem Projektverzeichnis:

2. **Initialisiere das Git-Repository**:

```bash
git init
```

Dieser Befehl erstellt ein neues Git-Repository in deinem Projektverzeichnis.

## Erster Commit

Nachdem du das Repository initialisiert hast, ist es Zeit, deinen ersten Commit zu erstellen.

1. **Füge alle Projektdateien zum Staging-Bereich hinzu**:

    ```bash
    git add .
    ```

2. **Erstelle den ersten Commit**: Mit dieser Aktion hast du den aktuellen Zustand deines Projekts in der Git-Historie gesichert.

    ```bash
    git commit -m "Initialer Commit"
    ```

## Änderungen verfolgen

Mit Git kannst du fortlaufend Änderungen an deinem Projekt verfolgen.

1. **Füge geänderte Dateien zum Staging-Bereich hinzu**:

    ```bash
    git add <Dateiname>
    ```

2. **Erstelle einen neuen Commit**: Wiederhole diesen Prozess, um die Entwicklung deines Projekts zu dokumentieren.

    ```bash
    git commit -m "Beschreibe hier deine Änderungen"
    ```

## Zurückkehren zu früheren Versionen

Git ermöglicht es dir, zu jedem früheren Zustand deines Projekts zurückzukehren.

1. **Finde die Commit-ID**, zu der du zurückkehren möchtest, indem du die Commit-Historie ansiehst:

    ```bash
    git log
    ```

2. **Wechsle zu diesem Commit**:

    ```bash
    git checkout <Commit-ID>
    ```

    - Um wieder zum aktuellen Zustand deines Hauptbranches (z.B. `main` oder `master`) zurückzukehren:

    ```bash
    git checkout main
    ```

## Änderungen mit Remote-Repositories teilen

Wenn du mit anderen zusammenarbeitest oder deine Änderungen sicher in der Cloud speichern möchtest, solltest du ein Remote-Repository einrichten.

1. **Erstelle ein Remote-Repository** auf Plattformen wie GitHub, GitLab oder Bitbucket.

2. **Verbinde dein lokales Repository mit dem Remote-Repository**:

    ```bash
    git remote add origin <URL-des-Remote-Repository>
    ```

3. **Sende deine Commits an das Remote-Repository**:

    ```bash
    git push -u origin main
    ```

## Wiederherstellung

### Einrichten eines Remote-Repositories

Ein Remote-Repository auf einer Plattform wie GitHub, GitLab oder Bitbucket dient als externes Backup deines Projekts. Wenn du noch kein Remote-Repository eingerichtet hast, folge den Anweisungen der jeweiligen Plattform, um eines zu erstellen, und verknüpfe es dann mit deinem lokalen Repository:

```bash
git remote add origin <URL-des-Remote-Repository>
```

### Regelmäßiges Pushen von Änderungen

Um sicherzustellen, dass deine lokale Arbeit regelmäßig gesichert wird, pushe deine Änderungen häufig zum Remote-Repository:

```bash
git push origin main
```

### Klonen eines Repositories

Wenn du auf einem neuen Gerät arbeiten oder eine Kopie deines Projekts wiederherstellen möchtest, kannst du das Remote-Repository klonen. Dies erstellt eine vollständige Kopie des Repositories auf deinem lokalen Gerät:

```bash
git clone <URL-des-Repository>
```

### Wiederherstellung eines früheren Zustands

Wenn du zu einem bestimmten früheren Zustand deines Projekts zurückkehren musst, kannst du dies tun, indem du zu dem entsprechenden Commit wechselst oder einen Branch auscheckst, der diesen Zustand repräsentiert. Um zu einem bestimmten Commit zurückzukehren, verwende:

```bash
# Commit-Historie
git log
git log --oneline
# Liste aller lokalen Branches anzeigen
git branch

# Zurückkehren zu einem bestimmten Commit
# die ersten 7 Zeichen der Commit-ID reichen
# alte Zustände zu betrachten
git checkout <Commit-ID>
# zum neuesten Stand des main Branches zurückkehren
git checkout main
git checkout -

# Fehler oder unerwünschte Änderungen sicher rückgängig zu machen
git revert <Commit-ID>

# Zurücksetzen des Arbeitsverzeichnisses und der Index (Staging Area) ohne Änderung der Working Directory-Dateien:
git reset --mixed <commit-id>
# Zum vollständigen Zurücksetzen inklusive aller Änderungen im Arbeitsverzeichnis:
git reset --hard <commit-id>

# Erstellen eines neuen Branches basierend auf einem älteren Commit
git checkout -b <neuer-branch-name> <commit-id>
```

### Nutzen von Tags für wichtige Meilensteine

Um wichtige Versionen deines Projekts leicht wiederherstellen zu können, kannst du Git Tags verwenden. Ein Tag erstellt einen benannten Ankerpunkt in der Projektgeschichte, den du leicht auschecken kannst:

```bash
git tag -a v1.0 -m "Mein erster Meilenstein"
git push origin --tags
```

### Erstellen von Branches für experimentelle Features

Für experimentelle Features oder größere Änderungen ist es ratsam, separate Branches zu verwenden. Dies ermöglicht es dir, Veränderungen zu isolieren und bei Bedarf leicht zum stabilen Zustand deines Projekts (z.B. dem `main` Branch) zurückzukehren:

```bash
git checkout -b feature-branch
git checkout main
```

### Backup des .git-Verzeichnisses

Für ein manuelles Backup kannst du das gesamte `.git`-Verzeichnis deines Projekts kopieren. Dieses Verzeichnis enthält die gesamte Git-Historie und alle Branches. Beachte jedoch, dass es besser ist, für regelmäßige Backups und Wiederherstellungen die standardmäßigen Git-Werkzeuge und Remote-Repositories zu verwenden.

## Richtlinien für Commit-Kommentare

### 1. Strukturierte Kommentare

Klare Struktur verwenden:

- **Kurze Zusammenfassung**: Starte mit einer kurzen, prägnanten Zusammenfassung des Commits. Versuche, diese unter 50 Zeichen zu halten.
- **Detaillierte Beschreibung**: Falls notwendig, füge nach einer Leerzeile eine detailliertere Beschreibung hinzu, die erläutert, was geändert wurde und vor allem warum.

### 2. Verwende den Imperativ

Auch im Deutschen solltest du den Imperativ verwenden, um Konsistenz mit den Git-Konventionen zu wahren (z.B. "Füge Feature hinzu" statt "Feature hinzugefügt").

### 3. Fokussiere auf das "Warum"

Der Kommentar sollte erklären, warum die Änderungen vorgenommen wurden. Dies ist besonders wichtig bei komplexen Änderungen oder Fehlerbehebungen.

### Beispiele

- **Feature hinzufügen**:

  ```bash
  git commit -m "Füge Suchfunktion zur Kontaktliste hinzu"
  ```

- **Fehler beheben**:

  ```bash
  git commit -m "Behebe Absturz beim Versuch, einen nicht existierenden Kontakt zu bearbeiten"
  ```

- **Dokumentation aktualisieren**:

  ```bash
  git commit -m "Aktualisiere README mit neuen Installationsanweisungen"
  ```

- **Abhängigkeiten aktualisieren**:

  ```bash
  git commit -m "Aktualisiere Django auf Version 3.2.1 für Sicherheitspatch"
  ```

- **Code aufräumen**:

  ```bash
  git commit -m "Refaktorisiere Kontaktverwaltungsmodul für mehr Klarheit"
  ```

- **Leistungsverbesserungen**:

  ```bash
  git commit -m "Optimiere Datenbankabfragen im Berichtsmodul"
  ```

## Unterschied zwischen git checkout und git revert

`git checkout <commit-id>` und `git revert <commit-id>` sind zwei verschiedene Git-Befehle, die auf unterschiedliche Weise mit der Historie eines Git-Repositorys arbeiten. Beide können verwendet werden, um auf frühere Zustände eines Projekts zuzugreifen oder Änderungen rückgängig zu machen, aber sie tun dies auf sehr unterschiedliche Art und Weise.

### `git checkout <commit-id>`

- **Zweck**: Der `git checkout <commit-id>`-Befehl wird verwendet, um den Arbeitsbaum (die Dateien in deinem Projektverzeichnis) und den HEAD (den aktuellen Branch-Zeiger) auf den Zustand zu setzen, den sie zum Zeitpunkt des angegebenen Commits hatten. Dieser Befehl ändert nicht die Projektgeschichte oder die aktuellen Branches; er wechselt lediglich in einen "detached HEAD"-Zustand, in dem du den Zustand des Repositories zu einem bestimmten Zeitpunkt betrachten kannst.
- **Verwendung**: Typischerweise nutzt du `git checkout` für die Untersuchung oder das Experimentieren mit alten Versionen deines Projekts. Änderungen, die du im "detached HEAD"-Zustand machst, können durch Erstellen eines neuen Branches gespeichert werden, sonst riskierst du, sie zu verlieren, wenn du zu einem anderen Commit wechselst.
- **Wichtig**: `git checkout` ändert nichts an der Historie deines Repositories. Wenn du zurück zu einem früheren Commit gehst, um von dort aus weiterzuarbeiten, musst du einen neuen Branch erstellen, sonst sind deine neuen Commits nicht an einen Branch gebunden.

### `git revert <commit-id>`

- **Zweck**: Der `git revert <commit-id>`-Befehl wird verwendet, um die Änderungen eines bestimmten Commits rückgängig zu machen, indem ein neuer Commit erstellt wird. Im Gegensatz zu `git checkout` ändert `git revert` die Projektgeschichte, indem aktiv ein neuer Zustand erzeugt wird, der die Änderungen des ursprünglichen Commits nicht mehr enthält.
- **Verwendung**: Du würdest `git revert` verwenden, wenn du einen Fehler oder unerwünschte Änderungen in deinem Projekt rückgängig machen möchtest, ohne die Historie zu verlieren. Es ist eine sichere Methode, Änderungen rückgängig zu machen, die bereits gepusht wurden, da es die Zusammenarbeit nicht stört.
- **Wichtig**: `git revert` erstellt einen neuen Commit, der das Gegenteil des angegebenen Commits bewirkt. Die ursprünglichen Commits bleiben im Repository-Verlauf erhalten.

### Zusammenfassung

- **`git checkout <commit-id>`**: Wechselt in einen Zustand, der dem angegebenen Commit entspricht, ohne die Projektgeschichte zu ändern. Wird hauptsächlich verwendet, um alte Zustände zu betrachten oder darauf basierend zu experimentieren.
- **`git revert <commit-id>`**: Erstellt einen neuen Commit, der die Änderungen eines früheren Commits rückgängig macht, und ändert damit effektiv die Projektgeschichte, ohne jedoch frühere Commits zu entfernen. Wird verwendet, um Fehler oder unerwünschte Änderungen sicher rückgängig zu machen.