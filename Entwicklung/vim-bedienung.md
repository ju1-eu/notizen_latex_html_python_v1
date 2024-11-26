---
title: "vim-bedienung"
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!-----------------------------------------------------------------------
ju 5-2-24 vim-bedienung.md
pandoc vim-bedienung.md -o vim-bedienung.html -c inhalt.css --mathjax
------------------------------------------------------------------------->
# Vim-Editor - Bedienung

## Grundlegende Befehle:

1. **Starten und Beenden**:
   ```bash
   vi dateiname oder vim dateiname
   # Beenden ohne Änderungen zu speichern - Drücke  Esc
   :q!
   # Speichern von Änderungen - Drücke Esc
   :wq
   ```

1. **Modi**:
    - **Normalmodus**: Der Standardmodus. Hier können Sie Navigations- und Bearbeitungsbefehle ausführen.
    - **Einfügemodus**: Fügen Sie Text in die Datei ein.
        - `i` (um vor dem Cursor einzufügen)
        - `a` (um nach dem Cursor einzufügen)
        - `Esc`, um zum Normalmodus zurückzukehren.
    - **Befehlszeilenmodus**: Geben Sie Befehle wie Speichern oder Beenden ein.
        - `:` im Normalmodus, um in diesen Modus zu wechseln.

2. **Bewegung im Normalmodus**:
    - Bewegen Sie den Cursor mit
        - `h` (links), `j` (unten), `k` (oben) und `l` (rechts).
    - Springen Sie zum Anfang der Datei mit
        - `gg` und zum Ende mit `G`
    - Springen Sie zum Anfang oder Ende einer Zeile mit
        - `0` bzw. `$`

3. **Bearbeiten im Normalmodus**:
    - Löschen Sie einen Zeichen mit
        - `x`
    - Löschen Sie eine Zeile mit
        - `dd`
    - Kopieren (yank) Sie eine Zeile mit
        - `yy`
    - Fügen Sie eine kopierte oder gelöschte Zeile ein
        - `p`

4. **Suchen und Ersetzen**:
    - Suchen Sie nach einem Wort, indem Sie
        - `/wort` eingeben und `Enter` drücken.
    - Ersetzen Sie ein Wort global in der Datei mit
        - `:%s/alt/neu/g`

## Suchen:

- **Vorwärts nach einem Wort suchen**: `/Wort`
- **Rückwärts nach einem Wort suchen**: `?Wort`
- **Zum nächsten Treffer**: `n`
- **Zum vorherigen Treffer**: `N`

## Suchen & Ersetzen:

- **Alle Vorkommen in der Datei ersetzen**:
    - `:%s/altesWort/neuesWort/g`
- **Alle Vorkommen zwischen bestimmten Zeilen ersetzen**:
    - `:StartZeile,EndZeile s/altesWort/neuesWort/g`
    - (z.B. `:5,10s/altes/neues/g`)
- **Ersetzen mit Bestätigung**:
    - `:%s/altesWort/neuesWort/gc`
- **Erstes Vorkommen in jeder Zeile ersetzen**:
    - `:%s/altesWort/neuesWort/`
- **Ersetzen in einem ausgewählten Bereich**:
    1. Markieren Sie den Bereich im visuellen Modus
        - (drücken Sie `v` und bewegen Sie den Cursor).
    2. Dann `:s/altesWort/neuesWort/g`
- **Vom Anfang der Datei bis zur aktuellen Position**:
    - `:1,.s/altesWort/neuesWort/g`
- **Von der aktuellen Position bis zum Ende**:
    - `:.,$s/altesWort/neuesWort/g`


## Navigieren:

- **Zum Anfang der Datei**: `gg`
- **Zum Ende der Datei**: `G`

## Inhalt kopieren:

- **Kopiere den gesamten Inhalt ohne Zeilennummern in die Zwischenablage**:
    - `:%y+`
