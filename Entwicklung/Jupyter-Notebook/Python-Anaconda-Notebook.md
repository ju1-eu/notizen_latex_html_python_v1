---
title: "Python und Anaconda und Jupyter Notebook"
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!------------------------------------------------
ju 5-2-24 Python-Anaconda-Notebook.md
pandoc Python-Anaconda-Notebook.md -o Python-Anaconda-Notebook.html -c inhalt.css --mathjax
------------------------------------------------->
# Python und Anaconda und Jupyter Notebook

## Jupyter Notebook

Jupyter Notebook ist eine interaktive Umgebung, die das Ausführen von Python-Code in einer browserbasierten Anwendung ermöglicht.

### Jupyter Notebook Starten

```bash
# Terminal
conda update --all
# Umgebungen auflisten
conda env list
conda activate base
conda deactivate
# Navigieren zum Projekt-Verzeichnis
jupyter notebook
```

### Grundlegende Bedienung

- **Zellen**: Jupyter Notebooks bestehen aus Zellen, die entweder Code oder Markdown enthalten können.
- **Ausführung von Zellen**:
    - `Shift + Enter`
- **Hinzufügen neuer Zellen**:
    - `Insert` > `Insert Cell Above` oder `Insert Cell Below`

### Python-Code in einer Zelle

```python
# Code
print("Hallo Jupyter!")
# Einfache Rechenoperation
2 + 2
```

### Markdown für Text und Dokumentation


```Markdown
# Markdown
# Überschrift 1
### Überschrift 2
- oder * für Listen
[Linktext](URL)`
![Alt-Text](Bild-URL)
$2 + 2$
```

### Magische Befehle

**Magische Befehle**

- `%time`: Zeigt die Ausführungszeit einer Zeile.
- `%matplotlib inline`: Erlaubt das Anzeigen von Matplotlib-Diagrammen direkt im Notebook.

### Interaktive Widgets

dynamische, interaktive Benutzeroberflächen erstellen.

```python
from ipywidgets import interact
def f(x):
    return x
interact(f, x=10)
```

### Tastenkombinationen

- `Shift + Enter`: Führe die aktuelle Zelle aus und gehe zur nächsten.
- `Esc`: Wechsle in den Kommandomodus.
- `M`: Ändere die Zelle in Markdown.
- `Y`: Ändere die Zelle in Code.

## Anaconda

**Anaconda installieren** <https://www.anaconda.com/products/individual>

```bash
# Anaconda Navigator starten
anaconda-navigator
# Überprüfen der Anaconda-Installation
conda info
# Eine neue Conda-Umgebung erstellen
conda create --name <umgebungsname> python=<version>
# Aktivieren einer Conda-Umgebung
conda activate <umgebungsname>
# Deaktivieren der aktuellen Conda-Umgebung
conda deactivate
# Liste der installierten Pakete in der aktuellen Umgebung anzeigen
conda list
# Ein spezifisches Paket in der aktuellen Umgebung installieren
conda install <paketname>
# Ein spezifisches Paket in einer spezifischen Umgebung installieren
conda install --name <umgebungsname> <paketname>
# Anaconda-Umgebungen auflisten
conda env list
# Eine spezifische Anaconda-Umgebung entfernen
conda env remove --name <umgebungsname>
# Aktualisieren von Anaconda
conda update --all
# Anaconda-Pakete aktualisieren
conda update <paketname>
```


### Workflow - Jupyter Notebook

```bash
# Anaconda und alle Pakete aktualisieren
conda update --all
# Umgebungen auflisten
conda env list
# Eine Umgebung entfernen
conda env remove --name meinenv
# Erstellen einer neuen Umgebung
conda create --name meinenv python=3.11
# Aktivieren der Umgebung
conda activate meinenv
# Installation von Paketen
conda install numpy pandas matplotlib
# Start von Jupyter Notebook
jupyter notebook
# Deaktivieren der Umgebung
conda deactivate
```

### Workflow - Python-Script in einer Anaconda-Umgebung

```bash
# Erstelle eine neue Anaconda-Umgebung (optional, aber empfohlen):
conda create --name PythonGrundlagen_env python=3.11
# Anaconda-Umgebung aktivieren:
conda activate PythonGrundlagen_env
# Suche nach einem spezifischen Paket
conda list | grep PyQt5
# Installiere die benötigte Software
conda install pyqt
# Skript ausführen
python3 kfz_datenbank.py
# Deaktivieren einer Anaconda-Umgebung
conda deactivate
```

**Test grafische Benutzeroberfläche (GUI)**

```python
# name_script.py
# Test GUI
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Testfenster')
window.show()
sys.exit(app.exec_())

# Terminal $ python3 name_script.py
```

## PEP 8-Stilrichtlinien

1. **Einrückung**: Verwenden Sie 4 Leerzeichen pro Einrückungsebene.

2. **Zeilenlänge**: Beschränken Sie alle Zeilen auf maximal 79 - 120 Zeichen. Längere Zeilen sollten für verbesserte Lesbarkeit umgebrochen werden.

3. **Importe**:
    - Importe sollten immer am Anfang einer Datei stehen.
    - Reihenfolge:
        - Standardbibliothek-Importe,
        - Importe von Drittanbietern,
        - lokale Anwendungs-/Bibliotheks-spezifische Importe.
    - Vermeiden Sie Wildcard-Importe
        - `from module import *`

4. **Leerzeichen in Ausdrücken und Anweisungen**:
    - Unmittelbar vor einem Komma, Semikolon oder Doppelpunkt.
    - Unmittelbar vor der Klammer, die eine Liste von Argumenten oder Index-Operatoren öffnet.
    - Zwischen dem Funktionsnamen und der folgenden Klammer.
    - Vor oder nach einem Zuweisungs- oder Vergleichsoperator.

5. **Kommentare**: Kommentare sollten klar, präzise und so aktuell wie möglich gehalten werden. Kommentare sollten sich auf das Warum, nicht das Was konzentrieren.

6. **Benennungskonventionen**:
    - Klassenname: `CamelCase`
    - Funktions- und Variablennamen: `snake_case`
    - Konstanten: `UPPER_CASE`

7. **Leerzeilen**:
    - Verwenden Sie zwei Leerzeilen zwischen Funktionen und Klassendefinitionen.
    - Verwenden Sie eine Leerzeile zwischen Methodendefinitionen innerhalb einer Klasse.

8. **Leerzeichen um Operatoren**:
   ```python
   = != < > :
   # Nicht jedoch für Klammerungen und Indexierungen/Slices
   () [] {}
   list[index]
   ```


9.  **Dokumentationsstrings (Docstrings)**:
    - Verwenden Sie dreifache doppelte Anführungszeichen für Docstrings.
    - Der erste Satz des Docstrings sollte kurz und eine zusammenfassende Beschreibung sein.

10. **Dateistruktur und Organisation**:
    - Definieren Sie alle Imports am Anfang des Skripts.
    - Dann definieren Sie Konstanten.
    - Anschließend kommen Funktionen und Klassen.
    - Der ausführbare Teil des Skripts sollte ganz am Ende stehen
        - `if __name__ == "__main__":`


### Prüfen mit Tools wie flake8 oder pylint


```bash
# Installation*
pip install flake8
pip install pylint
# Verwendung
flake8 script.py
pylint script.py
```

## Python und Anaconda Update

**Anaconda-Installation**

```bash
# Anaconda
# Aktualisieren von Conda
conda info
conda list python
conda update conda
# Aktualisieren aller Pakete
conda update --all
# Installieren des Anaconda Metapakets (optional):
conda install anaconda
# aktualisieren
conda update anaconda
conda update jupyter
jupyter --version
conda update pandas matplotlib
conda info --envs
conda deactivate
conda create -n py312 python=3.12.1
conda activate base
conda update anaconda
conda activate py312
conda list python
# Python-Pakete installieren
conda install pillow
```

**Python-Installation**

```python
# Xcode Command Line Tools-Paket
xcode-select -p
#xcode-select --install
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++

# Python-Version-Manager
# Python-Pfad
which python
which python3
# Überprüfe die Python-Version
python --version
python3 --version
pip3 --version
brew update
brew upgrade python
brew install pyenv
pyenv versions
#  pyenv initialisieren und Pfad zur Umgebungsvariablen hinzugefügen
# Homebrew-Link zu Python zu erneuern
#unalias python
#brew link --overwrite python
vim ~/.zshrc
    if command -v pyenv 1>/dev/null 2>&1; then
        eval "$(pyenv init -)"
    fi
    export PATH="/usr/local/bin:$PATH"
    export PATH="/Users/jan/.pyenv/versions/3.12.1/bin:$PATH"
    alias python=python3
source ~/.zshrc
# aktuelles Python 3.12.1 mit pyenv installieren
pyenv install 3.12.1
pyenv global 3.12.1
python --version
# Python-Pakete installieren
pip install Pillow
```

## Homebrew (kurz "brew"), dem Paketmanager für macOS

```bash
# Homebrew installieren
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Homebrew aktualisieren
brew update
brew install <paketname>
# Installierte Pakete auflisten
brew list
# Informationen über ein Paket anzeigen
brew info <paketname>
# Paket aktualisieren
brew upgrade <paketname>
brew uninstall <paketname>
# Überprüfen, ob Ihr System irgendwelche Probleme hat
brew doctor
# Suche nach Paketen
brew search <suchbegriff>
# Abhängigkeiten anzeigen
brew deps <paketname>
```
