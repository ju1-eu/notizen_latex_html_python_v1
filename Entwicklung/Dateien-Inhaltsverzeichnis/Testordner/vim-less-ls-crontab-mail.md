---
title: "ls - vim - less - crontab - mail"
---
# ls

```bash
ls -lR
ls -lR | less
ls -lR > verzeichnisliste.txt
ls -lR ./02_Basics | grep '\.cc$'
ls -lR | grep '\.py$'

ls -l > verzeichnisliste.txt
ls -lR ./02_Basics > verzeichnisliste.txt
```

# Vim Bedienung

## Suchen

- **Suchen**: Drücken Sie `/`, gefolgt von Ihrem Suchbegriff und Enter. Zum Beispiel, `/suchtext` sucht nach "suchtext". Drücken Sie `n`, um zum nächsten Vorkommen und `N` für das vorherige zu springen.

## Suchen und Ersetzen

- **Suchen und Ersetzen**: Um alle Instanzen eines Wortes in der gesamten Datei zu ersetzen, verwenden Sie `:%s/alt/neu/g`. Zum Beispiel, `:%s/apfel/birne/g` ersetzt jedes Vorkommen von "apfel" durch "birne".

## Letzte Zeile springen

- **Zur letzten Zeile springen**: Drücken Sie `G`.

## Eine Zeile löschen

- **Eine Zeile löschen**: Bewegen Sie den Cursor zu der Zeile, die Sie löschen möchten, und drücken Sie `dd`.

## Mehrere Zeilen löschen

- **Mehrere Zeilen löschen**: Um zum Beispiel 5 Zeilen zu löschen, drücken Sie `5dd`.

## Kopieren und Einfügen

- **Eine Zeile kopieren**: Bewegen Sie den Cursor zu der Zeile, die Sie kopieren möchten, und drücken Sie `yy`.
- **Ein Wort kopieren**: Bewegen Sie den Cursor zum Anfang des Wortes und drücken Sie `yiw`.
- **Inhalt einfügen**: Bewegen Sie den Cursor zu der Position, an der Sie den Inhalt einfügen möchten, und drücken Sie `p`.

## Den gesamten Inhalt löschen

- **Den gesamten Inhalt löschen**: Geben Sie `ggdG` ein.

## Von Terminal zu Vim wechseln und Prozesse verwalten

Um von der Terminal-Shell zu Vim zu wechseln, ohne Vim zu schließen, und zwischen Hintergrund- und Vordergrundprozessen zu wechseln, verwenden Sie Jobsteuerungsbefehle von Bash oder Ihrer bevorzugten Shell.

## Vim im Hintergrund ausführen

- **Vim öffnen**: `vim datei.txt`
- Um Vim vorübergehend zu verlassen und in den Hintergrund zu verschieben, drücken Sie `Ctrl + Z`.
- Um zu sehen, welche Jobs im Hintergrund laufen, verwenden Sie `jobs`.
- Um Vim wieder in den Vordergrund zu holen, verwenden Sie `fg`. Wenn Sie mehrere Jobs im Hintergrund haben, nutzen Sie `fg %jobnummer`, wobei `jobnummer` die Nummer des Jobs ist, die Sie von `jobs` bekommen.

## Von less zu Vim wechseln

`less` bietet keine direkte Option, um die aktuell angezeigte Datei in Vim zu öffnen. Sie müssten `less` verlassen und dann `vim` mit der Datei als Argument öffnen.

- Wenn Sie in `less` sind, verlassen Sie es mit `q`.
- Öffnen Sie dann die Datei in Vim mit `vim datei.txt`.

# less

`less` ist ein Programm zum Betrachten von Textdateien in der Unix- und Unix-ähnlichen Befehlszeilenumgebung, das das Blättern sowohl vorwärts als auch rückwärts durch Dokumente ermöglicht. Es ist besonders nützlich für lange Dateien, da es Ihnen erlaubt, die Datei seitenweise anzusehen, ohne sie ganz lesen zu müssen (wie es `cat` tut) oder in einen Bearbeitungsmodus zu wechseln (wie bei `vi` oder `nano`).

Um eine Datei mit `less` zu öffnen, geben Sie `less` gefolgt vom Dateinamen ein:

```sh
less dateiname.txt
```

## Grundlegende Navigation

- **Vorwärts blättern**: Drücken Sie die **Spacebar** (Leertaste), um eine Seite nach unten zu blättern.
- **Rückwärts blättern**: Drücken Sie **b**, um eine Seite nach oben zu blättern.
- **Eine Zeile nach unten scrollen**: Drücken Sie **Enter** oder **e**.
- **Eine Zeile nach oben scrollen**: Drücken Sie **y** oder **k**.
- **Zum Anfang der Datei gehen**: Drücken Sie **g**.
- **Zum Ende der Datei gehen**: Drücken Sie **G**.
- **Suche**: Geben Sie **/** gefolgt von Ihrem Suchbegriff ein und drücken Sie Enter. Drücken Sie **n**, um zur nächsten Instanz zu springen, oder **N**, um zur vorherigen Instanz zu springen.
- **Beenden**: Drücken Sie **q**, um `less` zu verlassen.

- **Eine Datei öffnen und zu einer spezifischen Zeile springen**: Verwenden Sie `+` gefolgt von einem Befehl. Zum Beispiel, `less +100 dateiname.txt` öffnet `dateiname.txt` und springt zur Zeile 100.
- **Mit Dateien interagieren**: Während `less` läuft, können Sie **v** drücken, um die aktuelle Datei in Ihrem Standardeditor zu öffnen.
- **Horizontales Scrollen**: Verwenden Sie die Pfeiltasten nach links und rechts, um horizontal zu scrollen, falls die Zeilen länger als die Bildschirmbreite sind.

# Cron-Jobs Anzeigen

```sh
# liste
crontab -l
# bearbeiten
crontab -e
# löschen
crontab -r
```

# Mail im Terminal

1. **Mail öffnen**: Öffnen Sie das Terminal und geben Sie `mail` ein, um das Mail-Programm zu starten. Wenn Sie neue Nachrichten haben, zeigt es eine Liste Ihrer ungelesenen Nachrichten.

2. **Nachrichten lesen**: Wenn Sie Ihre Mails durchsehen möchten, können Sie einfach die Nummer der Nachricht eingeben, die Sie lesen möchten, nachdem Sie `mail` gestartet haben. Das Programm zeigt Ihnen dann den Inhalt der spezifischen Nachricht.

3. **Durch Nachrichten navigieren**: Sie können Befehle wie `next` (für die nächste Nachricht) und `prev` (für die vorherige Nachricht) verwenden, um durch Ihre Nachrichten zu navigieren.

4. **Eine Nachricht beantworten**: Um auf eine Nachricht zu antworten, können Sie den Befehl `reply` verwenden, während Sie eine Nachricht lesen. Das erlaubt Ihnen, direkt zu antworten.

5. **Eine neue Nachricht senden**: Um eine neue Nachricht zu senden, können Sie den Befehl `mail` gefolgt von der E-Mail-Adresse des Empfängers verwenden. Zum Beispiel: `mail adresse@example.com`.

6. **Mail verlassen**: Um das Mail-Programm zu verlassen, tippen Sie `q` (für Quit).

## Nachricht Lesen

- Um die Nachricht zu lesen, geben Sie einfach die Nummer der Nachricht ein, in diesem Fall `1`, und drücken Sie Enter. Das wird den Inhalt der Nachricht anzeigen.

## Nächste Schritte im `mail`-Programm

- **Antworten**: Um auf eine Nachricht zu antworten, können Sie `r` eingeben, während Sie die Nachricht lesen.
- **Weiterleiten**: Um die Nachricht weiterzuleiten, können Sie `f` eingeben.
- **Löschen**: Um eine Nachricht zu löschen, geben Sie `d` ein, gefolgt von der Nachrichtennummer (z.B. `d 1`).
- **Verlassen**: Um das Mail-Programm zu verlassen und zurück zum Terminal-Prompt zu kommen, tippen Sie `q`.
