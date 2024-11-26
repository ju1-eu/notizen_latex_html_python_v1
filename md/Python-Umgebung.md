# Python - Verwendung von virtuellen Umgebungen


1. Deaktivieren Sie zuerst Ihre aktuelle virtuelle Umgebung:

   ```
   deactivate
   ```

2. Erstellen Sie eine neue virtuelle Umgebung:

   ```
   python3 -m venv myenv_new
   ```

3. Aktivieren Sie die neue Umgebung:

   ```
   source myenv_new/bin/activate
   ```

4. Überprüfen Sie, ob Sie jetzt die richtige Python-Version verwenden:

   ```
   which python3
   ```

   Dies sollte nun einen Pfad in Ihrer neuen virtuellen Umgebung anzeigen, etwa `/path/to/myenv_new/bin/python3`.

5. Wenn der Pfad korrekt ist, versuchen Sie erneut, PyYAML zu installieren:

   ```
   python3 -m pip install PyYAML
   ```

6. Wenn die Installation erfolgreich war, können Sie Ihr Skript in dieser neuen Umgebung ausführen:

   ```
   python3 ./scriptauswahl.py
   ```

7. Um die Ausgabe mit einem benutzerdefinierten Header zu versehen:

   ```
   (
   echo "Installed Python packages in myenv_system environment:"
   echo "Date: $(date)"
   echo "----------------------------------------"
   pip list --format=freeze | cut -d '=' -f 1
   ) > installed_packages.txt
   ```

8. Inhalt im Terminal anzeigen:

```
cat installed_packages.txt
```

## Keywords: Datenwissenschaft und Maschinelles Lernen mit Python

- Keywords: Python, maschinelles Lernen, Pandas, NumPy, SciPy, Matplotlib, Seaborn,  Plotly, Traditionelles Maschinelles Lernen, Scikit-learn, Supervised Learning, Unsupervised Learning, Tiefes Lernen, TensorFlow, Training tiefer neuronaler Netzwerke, Bilderkennung, PyTorch, Jupyter Notebooks, Explorative Datenanalyse, Statistische Grafiken, Verständnis von Datenmustern, Algorithmen, Regression, Klassifikation, Überwachtes Lernen

### Python

Python ist eine vielseitige Programmiersprache, ähnlich einem Schweizer Taschenmesser für Entwickler und Wissenschaftler. Sie ermöglicht die Lösung einfacher Aufgaben wie das Sortieren einer Liste von Namen ebenso effizient wie die Durchführung komplexer Datenanalysen oder das Entwickeln von Lernalgorithmen für künstliche Intelligenz.

### Maschinelles Lernen

Maschinelles Lernen ist vergleichbar mit dem Lernprozess eines Kindes, das aus Erfahrungen lernt. Statt zu sagen: "Das ist ein Hund", lernt der Computer aus vielen Bildern, was einen Hund kennzeichnet, und kann schließlich selbstständig Hunde auf Bildern erkennen.

### Pandas

Pandas ist eine Bibliothek in Python, die als multifunktionales Werkzeug für Datenanalysten und Wissenschaftler dient. Sie kann als ein extrem effizientes und flexibles Werkzeug betrachtet werden, das Daten sortieren, bereinigen und analysieren kann, ähnlich einem Taschenrechner, der speziell für die Arbeit mit großen Datensätzen konzipiert wurde.

### NumPy

NumPy erweitert die Fähigkeiten von Python, indem es Unterstützung für große, mehrdimensionale Arrays und Matrizen bietet, zusammen mit einer umfangreichen Sammlung von mathematischen Funktionen. Man kann es als das Fundament eines Gebäudes betrachten, auf dem komplexere Datenanalyse- und Wissenschaftsprojekte aufgebaut sind.

### SciPy

SciPy nutzt NumPy, um weitere Funktionalitäten für wissenschaftliches Rechnen hinzuzufügen, wie Optimierung, Statistik und Signalverarbeitung. Es ist wie ein erweitertes Laborwerkzeug, das spezielle Instrumente für verschiedene wissenschaftliche Aufgaben bereitstellt.

### Matplotlib, Seaborn, Plotly

Diese Bibliotheken dienen der Datenvisualisierung. Matplotlib ermöglicht grundlegende Grafiken und Diagramme, Seaborn fügt attraktive Designs und einfache Schnittstellen für komplexe statistische Grafiken hinzu, und Plotly erlaubt interaktive, webbasierte Grafiken. Zusammen bilden sie ein Toolkit, vergleichbar mit einem Satz von Zeichenwerkzeugen, der es ermöglicht, Daten in visuell ansprechender Form darzustellen.

### Traditionelles Maschinelles Lernen und Scikit-learn

Traditionelles maschinelles Lernen mit Scikit-learn beinhaltet Techniken wie Regression und Klassifikation. Man kann sich das vorstellen wie das Erlernen der Grundlagen des Autofahrens: Bevor man lernt, wie man ein Rennauto fährt (tiefe neuronale Netzwerke), muss man mit einem normalen Auto umgehen können, einschließlich des Schaltens, Lenkens und Parkens.

### Supervised und Unsupervised Learning

Supervised Learning ist, als würde man einem Kind beibringen, Rad zu fahren, indem man es an der Hand hält und ihm Richtungen gibt. Unsupervised Learning hingegen ist wie das Erkunden eines unbekannten Raumes ohne Anleitung, um selbst Muster oder Strukturen zu erkennen.

### Tiefes Lernen, TensorFlow und PyTorch

Tiefes Lernen mit TensorFlow oder PyTorch ist vergleichbar mit dem Bau und der Feinabstimmung eines Raumschiffs. Es handelt sich um fortschrittliche Werkzeuge, die es ermöglichen, komplexe Modelle zu entwickeln, die Aufgaben wie Bild- und Spracherkennung durchführen können, weit über das hinaus, was mit traditionellem maschinellem Lernen möglich ist.

### Jupyter Notebooks

Jupyter Notebooks sind interaktive Dokumente, die Code, Text und Visualisierungen kombinieren. Sie sind vergleichbar mit einem Laborjournal, in dem Wissenschaftler ihre Experimente dokumentieren, durchführen und die Ergebnisse für andere sichtbar machen können.

### Explorative Datenanalyse und Statistische Grafiken

Explorative Datenanalyse ist der Prozess des Durchstöberns von Daten, um Einsichten und Muster zu finden, ähnlich einem Detektiv, der nach Hinweisen sucht. Statistische Grafiken helfen dabei, diese Muster sichtbar zu machen, wie eine Lupe, die kleinste Details hervorhebt.

### Algorithmen, Regression, Klassifikation und Überwachtes Lernen

Algorithmen sind die Rezepte des maschinellen Lernens, Schritt-für-Schritt-Anweisungen, um Daten zu analysieren und Vorhersagen zu treffen. Regression und Klassifikation sind zwei grundlegende Arten des überwachten Lernens, vergleichbar mit dem Lösen von Gleichungen in der Mathematik bzw. dem Ordnen von Objekten in Kategorien in der Biologie.

\newpage

## Mindmap: Datenwissenschaft und Maschinelles Lernen mit Python

**Zentrales Thema: Datenwissenschaft und Maschinelles Lernen mit Python.**

1. Grundlegende Bibliotheken
   - **Pandas**
     - Datenmanipulation
     - Datenreinigung
     - Zeitreihenanalyse
   - **NumPy**
     - Mehrdimensionale Arrays
     - Mathematische Operationen
   - **SciPy**
     - Wissenschaftliches Rechnen
     - Statistik
     - Optimierungsaufgaben

2. Datenvisualisierung
   - **Matplotlib**
     - Basisdiagramme und -grafiken
     - Anpassung von Plots
   - **Seaborn**
     - Statistische Grafiken
     - Attraktive Standarddesigns
   - **Plotly**
     - Interaktive, webbasierte Grafiken
     - Komplexere Visualisierungen

3. Maschinelles Lernen
   - **Traditionelles Maschinelles Lernen**
     - **Scikit-learn**
       - Algorithmen für Supervised Learning (z.B. Regression, Klassifikation)
       - Algorithmen für Unsupervised Learning (z.B. Clustering)
   - **Tiefes Lernen**
     - **TensorFlow**
       - Aufbau und Training tiefer neuronaler Netzwerke
       - Anwendungsbereiche (Bilderkennung, Sprachverarbeitung)
     - **PyTorch**
       - Dynamische Berechnungsgraphen
       - Forschungsfreundlich

4. Entwicklungsumgebung
   - **Jupyter Notebooks**
     - Interaktive Code-Ausführung
     - Integration von Text, Code und Visualisierungen

5. Schlüsselkonzepte
   - **Datenanalyse**
     - Explorative Datenanalyse
     - Datenbereinigung und -vorbereitung
   - **Statistische Grafiken**
     - Verständnis von Datenmustern
   - **Explorative Datenanalyse**
     - Erste Schritte der Datenuntersuchung
   - **Algorithmen**
     - Verstehen, wie maschinelles Lernen funktioniert
   - **Regression und Klassifikation**
     - Zwei Haupttypen des überwachten Lernens

## Mindmap: Python, Anaconda und Jupyter Notebooks in der Datenwissenschaft

![PDF: Mindmap - Python](images/Mindmap-Python.pdf "Abb.: Python")

**Zentrales Thema: Python, Anaconda und Jupyter Notebooks in der Datenwissenschaft.**

1. **Python**
   - Definition: Hochrangige Programmiersprache
   - Eigenschaften
     - Klarheit
     - Einfachheit
   - Anwendungsbereiche
     - Programmierung
     - Datenanalyse
   - Unterstützung durch Bibliotheken

2. **Anaconda**
   - Definition: Open-Source-Distribution für Python und R
   - Rolle: Werkzeugkasten für Datenwissenschaftler
   - Hauptmerkmale
     - Vereinfachung von Installation und Verwaltung
     - Sammlung von Bibliotheken für Datenwissenschaft und maschinelles Lernen

3. **Jupyter Notebooks**
   - Definition: Open-Source-Webanwendung
   - Funktionen
     - Erstellung lebendiger Dokumente
     - Integration von Code, Gleichungen und Visualisierungen
   - Nutzungskontext
     - Explorative Datenanalyse
     - Bildung
     - Projektzusammenarbeit

4. **Synergie und Integration**
   - Verbindung der Komponenten
     - Python als Basis
     - Anaconda als vereinfachende Plattform
     - Jupyter Notebooks als interaktive Arbeitsumgebung
   - Anwendungsszenarien
     - Datenaufbereitung
     - Analyse
     - Visualisierung
     - Präsentation

5. **Praktische Anwendung**
   - Effizienz in der Datenwissenschaft
     - Schneller Einstieg durch Anaconda
     - Flexibilität und Leistungsfähigkeit durch Python
     - Interaktivität und Dokumentation durch Jupyter Notebooks
   - Kooperation und Kommunikation
     - Gemeinsame Nutzung von Notebooks
     - Erleichterung der Zusammenarbeit und des Lernens

\newpage

## Kewords: Python, Anaconda, Jupyter Notebooks

- **Kewords**: Python, Anaconda, Jupyter Notebooks, Programmierung, Bibliotheken, Datenwissenschaft, maschinelles Lernen, explorative Datenanalyse, Pandas, Scikit-learn, Matplotlib, Seaborn

### Was ist Python?

Python ist eine Programmiersprache, ähnlich wie Englisch eine Sprache für die Kommunikation zwischen Menschen ist. Python wird wegen seiner Klarheit und Einfachheit geschätzt, ähnlich wie ein einfaches Werkzeug, das für viele Aufgaben verwendet werden kann. In der Datenwissenschaft ermöglicht Python es, mit Daten zu "sprechen", sie zu analysieren und aus ihnen zu lernen.

### Was ist Anaconda?

Anaconda kann man sich als einen großen Koffer für einen Wissenschaftler vorstellen, der alle Instrumente und Geräte enthält, die für Experimente benötigt werden. In diesem Koffer finden sich alle möglichen Werkzeuge (Bibliotheken und Programme) für die Datenwissenschaft und das maschinelle Lernen, vorinstalliert und bereit zur Verwendung mit Python. Anaconda vereinfacht die Organisation und den Zugriff auf diese Werkzeuge erheblich.

### Was ist Jupyter Notebooks?

Jupyter Notebooks sind wie interaktive Notizbücher, in denen Wissenschaftler ihre Gedanken (Code und Anmerkungen) sowie die Ergebnisse ihrer Experimente (Grafiken und Daten) festhalten können. Diese digitalen Notizbücher unterstützen die explorative Datenanalyse, indem sie die unmittelbare Ausführung von Code und die Visualisierung der Ergebnisse in einem einzigen Dokument ermöglichen.

### Programmierung

Programmierung in diesem Kontext bezieht sich auf den Prozess der Erstellung von Instruktionen, die es dem Computer ermöglichen, mit Daten umzugehen und aus ihnen zu lernen. Es ist vergleichbar mit dem Schreiben eines Rezeptes, das genau beschreibt, welche Zutaten benötigt werden und wie sie zu einem Gericht verarbeitet werden.

### Bibliotheken

Bibliotheken in Python sind Sammlungen von Werkzeugen und Funktionen, die spezifische Aufgaben erleichtern. Man kann sie sich vorstellen wie Bücher in einer Bibliothek, die Wissen zu bestimmten Themen bereitstellen. Statt jedes Mal ein Buch von Grund auf neu zu schreiben, nutzen Wissenschaftler diese Bücher, um schnell auf bestehendes Wissen zuzugreifen.

### Datenwissenschaft

Datenwissenschaft ist das Feld, das Methoden und Techniken nutzt, um aus großen Mengen von Daten nützliche Informationen zu gewinnen. Man kann es mit der Archäologie vergleichen, bei der aus verstreuten Fragmenten wertvolle Artefakte und Wissen über vergangene Zivilisationen zusammengetragen werden.

### Was ist Maschinelles Lernen?

Maschinelles Lernen ist ein Bereich innerhalb der Datenwissenschaft, der Computern die Fähigkeit gibt, aus Daten zu lernen, ohne explizit programmiert zu sein. Es ist, als würde man einem Roboter beibringen, aus Erfahrungen zu lernen und seine Aufgaben mit der Zeit besser zu erfüllen.

### Was ist Explorative Datenanalyse?

Explorative Datenanalyse ist der Prozess des ersten "Erkundens" der Daten, um Muster, Anomalien oder interessante Beziehungen zu entdecken, ohne vorher spezifische Hypothesen zu haben. Es ist wie das erste Öffnen einer Schatzkiste, um zu sehen, was darin versteckt ist.

### Was ist Pandas?

Pandas ist eine Bibliothek in Python, speziell entwickelt für die Datenmanipulation und -analyse. Man kann sich Pandas als ein multifunktionales Schweizer Taschenmesser vorstellen, das für die Arbeit mit tabellarischen Daten optimiert ist.

### Scikit-learn

Scikit-learn ist eine Bibliothek für maschinelles Lernen in Python. Sie bietet einfache und effiziente Werkzeuge für Datenmining und Datenanalyse. Man kann sich Scikit-learn als einen Werkzeugkasten vorstellen, der alle notwendigen Werkzeuge für den Bau und das Verständnis komplexer maschineller Lernmodelle enthält.

### Matplotlib und Seaborn

Matplotlib und Seaborn sind Bibliotheken für die Datenvisualisierung in Python. Während Matplotlib grundlegende Grafiken und Diagramme ermöglicht, baut Seaborn darauf auf und bietet eine höhere Abstraktionsebene für die Erstellung statistisch anspruchsvoller Visualisierungen. Zusammen bieten sie das künstlerische Werkzeug, mit dem Wissenschaftler die Geschichte ihrer Daten durch visuelle Darstellungen erzählen können.

## Homebrew (kurz "brew"), dem Paketmanager für macOS

```bash
# Homebrew installieren
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Homebrew aktualisieren
brew update
brew upgrade
brew cleanup
brew doctor

brew install <paketname>
# Installierte Pakete auflisten
brew list
# Informationen über ein Paket anzeigen
brew info <paketname>
# Paket aktualisieren
brew upgrade <paketname>
brew uninstall <paketname>
# Suche nach Paketen
brew search <suchbegriff>
# Abhängigkeiten anzeigen
brew deps <paketname>

# php, mysql, apache, mosquitto (ESP32)
brew services list
brew services restart httpd
brew services restart mosquitto
brew services restart mysql
brew services restart php

# Systeminfo
brew install neofetch
neofetch
```

## Namenskonventionen für HostName, LocalHostName und ComputerName

1. **HostName:**
   - **Ziel:** Ein eindeutiger, vollqualifizierter Domänenname (FQDN) für die Netzwerkdienste und Unix-Befehle.
   - **Empfehlung:** imacj.example.com
   - **Befehl:**

     ```bash
     sudo scutil --set HostName imacj.example.com
     ```

2. **LocalHostName:**
   - **Ziel:** Ein eindeutiger Name für die lokale Netzwerkerkennung, der von Bonjour verwendet wird. Dieser Name sollte keine Leerzeichen oder Sonderzeichen enthalten und in Kleinbuchstaben sein.
   - **Empfehlung:** imacj
   - **Befehl:**

     ```bash
     sudo scutil --set LocalHostName imacj
     ```

3. **ComputerName:**
   - **Ziel:** Ein benutzerfreundlicher Name, der in der macOS-Oberfläche und Netzwerkerkennung angezeigt wird.
   - **Empfehlung:** iMac von Jan
   - **Befehl:**

     ```bash
     sudo scutil --set ComputerName "iMac von Jan"
     ```

### Schritte zur Umsetzung:

1. **Setze den HostName:**

   ```bash
   sudo scutil --set HostName imacj.example.com
   ```

2. **Setze den LocalHostName:**

   ```bash
   sudo scutil --set LocalHostName imacj
   ```

3. **Setze den ComputerName:**

   ```bash
   sudo scutil --set ComputerName "iMac von Jan"
   ```

4. **Überprüfe die Änderungen:**

   ```bash
   scutil --get HostName
   scutil --get LocalHostName
   scutil --get ComputerName
   ```

### Erklärung

- **HostName (imacj.example.com):** Der HostName wird verwendet, wenn der Mac in größeren Netzwerken oder durch Dienste und Skripte eindeutig identifiziert werden muss. Die Verwendung eines vollqualifizierten Domänennamens (FQDN) sorgt für Eindeutigkeit.
- **LocalHostName (imacj):** Der LocalHostName wird von Bonjour für die lokale Netzwerkerkennung verwendet. Ein kurzer, prägnanter Name ohne Sonderzeichen oder Leerzeichen erleichtert die Identifikation.
- **ComputerName (iMac von Jan):** Der ComputerName ist der benutzerfreundliche Name, der in der macOS-Benutzeroberfläche angezeigt wird. Die Verwendung eines verständlichen Namens macht es einfacher, den Mac in Netzwerken oder in der Systemeinstellung "Freigaben" zu identifizieren.

Durch diese Namenskonventionen wird sichergestellt, dass dein Mac sowohl technisch einwandfrei als auch benutzerfreundlich und eindeutig im Netzwerk identifiziert wird.

## zshrc

```bash
vim ~/.zshrc
source ~/.zshrc

# ~/.zshrc
# Hilfsfunktion, um Verzeichnisse zum $PATH hinzuzufügen, wenn sie noch nicht vorhanden sind
add_to_path() {
    for dir in "$@"; do
        if [[ -d "$dir" && ":$PATH:" != *":$dir:"* ]]; then
            PATH="$dir:$PATH"
        fi
    done
}

# Systemweite Python-Installation zuerst setzen
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

# Ruby-Initialisierung (falls vorhanden)
if command -v rbenv > /dev/null; then
  eval "$(rbenv init -)"
fi

# Node Version Manager (NVM) Initialisierung
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# LLVM-Umgebungsvariablen
export LDFLAGS="-L/usr/local/opt/llvm/lib"
export CPPFLAGS="-I/usr/local/opt/llvm/include"

# Weitere Pfade hinzufügen
add_to_path \
    "$HOME/bin" \
    "$HOME/Downloads/flutter/bin" \
    "$HOME/.local/bin" \
    "$HOME/esp/esp-idf" \
    /usr/local/opt/llvm/bin \
    /usr/local/opt/openjdk/bin \
    /Library/TeX/texbin \
    /Library/Apple/usr/bin \
    /System/Cryptexes/App/usr/bin \
    /var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin \
    /var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin \
    /var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin

# Aliase
alias ll="ls -laG"
alias ls='ls -G'
alias python=python3
alias maintenancetool='/Users/jan/Qt/MaintenanceTool.app/Contents/MacOS/MaintenanceTool'

# Funktion zum Laden von pyenv
load_pyenv() {
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
}

# Funktion zum Laden von Anaconda
load_anaconda() {
    if [[ -d "$HOME/anaconda3" ]]; then
        export CONDA_PREFIX="$HOME/anaconda3"
        __conda_setup="$("$CONDA_PREFIX/bin/conda" 'shell.zsh' 'hook' 2> /dev/null)"
        if [ $? -eq 0 ]; then
            eval "$__conda_setup"
        else
            if [ -f "$CONDA_PREFIX/etc/profile.d/conda.sh" ]; then
                . "$CONDA_PREFIX/etc/profile.d/conda.sh"
            fi
        fi
        unset __conda_setup
        export PATH="$CONDA_PREFIX/bin:$PATH"
    fi
}

# Prompt-Einstellungen
unsetopt PROMPT_SUBST

# Farben definieren
autoload -U colors && colors

# Git-Branch anzeigen, falls im Git-Repository
parse_git_branch() {
  git branch 2>/dev/null | sed -n '/\* /s///p'
}

# Prompt definieren
PROMPT='%{$fg[green]%}%n@%m%{$reset_color%}:%{$fg[blue]%}%~%{$reset_color%}$(parse_git_branch) $ '

# Wenn in einem Git-Repository, zeige den aktuellen Branch in Rot
RPROMPT='$(parse_git_branch)'

# Optionen, um die Farben des Prompts anzupassen
setopt prompt_subst
```

## Aktualisieren der Python-Version

### Systemweite Python - Installation - Erstellen und Verwalten von virtuellen Umgebungen

```bash
# Aktualisieren von Homebrew
brew update
brew upgrade

# Aktualisieren der Python-Version
brew upgrade python@3.12

# Verlinken der neuesten Python-Version
brew link --force --overwrite python@3.12

# Überprüfen des Pfades und der Python-Version nach dem Update
# HINWEIS: Terminal neu öffnen oder die .zshrc-Datei erneut laden
source ~/.zshrc
which python3
python3 --version

# Anzeigen aller Umgebungen
find ~ -name "activate" -path "*/bin/activate"

# Erstellen und Aktivieren einer virtuellen Umgebung
python3 -m venv myenv_system
source myenv_system/bin/activate

# Überprüfen der Python-Version und des Pfades
python --version  # sollte Python 3.12.4 anzeigen
which python

# Paket-Installation in der virtuellen Umgebung
pip install --upgrade pip
pip install jupyter pandas numpy matplotlib seaborn plotly scikit-learn scipy pyqt5

# Deaktivieren der virtuellen Umgebung
deactivate

# Löschen der virtuellen Umgebung
rm -rf myenv_system
```

### `pyenv`-Installation - Erstellen und Verwalten von virtuellen Umgebungen

```bash
# Installation von pyenv (falls noch nicht installiert)
brew install pyenv

# Installation von pyenv-virtualenv (falls noch nicht installiert)
brew install pyenv-virtualenv

# Laden von pyenv
# passe an ~/.zshrc
load_pyenv

# Überprüfen der pyenv-Version
pyenv --version

# Anzeigen aller installierten Python-Versionen
pyenv versions

# Installation der gewünschten Python-Version
pyenv install 3.12.4

# Anzeigen aller pyenv-virtuellen Umgebungen
pyenv virtualenvs

# Erstellen einer neuen virtuellen Umgebung mit der gewünschten Python-Version
pyenv virtualenv 3.12.4 myenv

# Aktivieren der neuen virtuellen Umgebung
pyenv activate myenv

# Überprüfen der Python-Version und des Pfades nach der Aktivierung
python --version  # sollte Python 3.12.4 anzeigen
which python

# Installation und Aktualisierung spezifischer Pakete in der virtuellen Umgebung
python3.12 -m pip install --upgrade pip
pip install jupyter pandas numpy matplotlib seaborn plotly scikit-learn scipy pyqt5

# Optional: Installation von Deep Learning-Paketen
# pip install tensorflow torch

# Deaktivieren der virtuellen Umgebung
pyenv deactivate

# Löschen der virtuellen Umgebung
pyenv uninstall myenv
```

### Anaconda - Installation - Erstellen und Verwalten von virtuellen Umgebungen

```bash
# Installation von Anaconda (falls noch nicht installiert)
brew install --cask anaconda

# Laden von Anaconda
# passe an ~/.zshrc
load_anaconda

# Überprüfen der Conda-Version
conda --version

# Aktualisieren von Conda selbst
conda update conda

# Anzeigen aller Conda-Umgebungen
conda env list

# Erstellen einer neuen Umgebung mit der gewünschten Python-Version
conda create -n py312_env python=3.12

# Aktivieren der neuen Umgebung
conda activate py312_env

# Aktualisieren aller Pakete in der neuen Umgebung
conda update --all

# Installation und Aktualisierung spezifischer Pakete
conda install jupyter pandas numpy matplotlib seaborn plotly scikit-learn scipy pyqt

# Optional: Installation von Deep Learning-Paketen (empfohlen für Python 3.9)
#conda install tensorflow pytorch

# Überprüfen des Pfades und der Python-Version nach der Installation
which python3
python3 --version

conda deactivate
conda remove -n py312_env --all
```

## Installation von Paketen

1. **Datenanalyse und -visualisierung**: pandas, numpy, matplotlib, seaborn, plotly
2. **Wissenschaftliches Rechnen und numerische Methoden**: numpy, scipy, matplotlib
3. **Maschinelles Lernen**: scikit-learn, numpy, pandas, matplotlib
4. **Deep Learning**: tensorflow, pytorch, numpy, pandas (Python 3.9 empfohlen)
5. **Entwicklung von grafischen Benutzeroberflächen**: pyqt

### Datenanalyse und -visualisierung

```bash
load_anaconda
conda create -n data_analysis_env python=3.12
conda activate data_analysis_env
conda install pandas numpy matplotlib seaborn plotly
conda deactivate
conda remove -n data_analysis_env --all
```

### Wissenschaftliches Rechnen und numerische Methoden

```bash
load_anaconda
conda create -n scientific_computing_env python=3.12
conda activate scientific_computing_env
conda install numpy scipy matplotlib
conda deactivate
conda remove -n scientific_computing_env --all
```

### Maschinelles-Lernen

```bash
load_anaconda
conda create -n ml_env python=3.12
conda activate ml_env
conda install scikit-learn numpy pandas matplotlib
conda deactivate
conda remove -n ml_env --all
```

### Deep Learning

```bash
load_anaconda
conda create -n deep_learning_env python=3.9  # Python 3.9 empfohlen
conda activate deep_learning_env
conda install tensorflow pytorch numpy pandas
conda deactivate
conda remove -n deep_learning_env --all
```

### Entwicklung von grafischen Benutzeroberflächen

```bash
load_anaconda
conda create -n gui_env python=3.12
conda activate gui_env
conda install pyqt
conda deactivate
conda remove -n gui_env --all
```

## Berechtigungen und Ausführrechte setzen

```bash
# Berechtigungen für Dateien setzen
find . -type f -name "*.md" -exec chmod 644 {} \;
find . -type f -name "*.txt" -exec chmod 644 {} \;
find . -type f -name "*.html" -exec chmod 644 {} \;
find . -type f -name "*.css" -exec chmod 644 {} \;
find . -type f -name "*.tex" -exec chmod 644 {} \;
find . -type f -name "*.pdf" -exec chmod 644 {} \;

# Ausführrechte für .sh und .py-Dateien setzen
find . -type f -name "*.sh" -exec chmod +x {} \;
find . -type f -name "*.py" -exec chmod +x {} \;

# Berechtigungen für Verzeichnisse setzen
find . -type d -exec chmod 755 {} \;
```

## Anaconda

**Anaconda installieren** <https://www.anaconda.com/products/individual>

```bash
# Anaconda Navigator starten
anaconda-navigator
# Überprüfen der Anaconda-Installation
conda info
# Anaconda aktualisieren
conda update
```

### Workflow - Jupyter Notebook

```bash
# Umgebungen auflisten
conda env list
# Erstellen einer neuen Umgebung
conda create --name meinenv python=3.12
# Aktivieren der Umgebung
conda activate meinenv
# Anaconda aktualisieren
conda update -all
# Installation von Paketen
conda install numpy pandas matplotlib
# Start von Jupyter Notebook
jupyter notebook
# Deaktivieren der Umgebung
conda deactivate
# Eine Umgebung entfernen
conda env remove --name meinenv
```

### Grundlegende Bedienung - Jupyter Notebook

- **Zellen**: Jupyter Notebooks bestehen aus Zellen, die entweder Code oder Markdown enthalten können.
- **Ausführung von Zellen**:
  - `Shift + Enter`
- **Hinzufügen neuer Zellen**:
  - `Insert` > `Insert Cell Above` oder `Insert Cell Below`

#### Python-Code in einer Zelle

```python
# Code
print("Hallo Jupyter!")
# Einfache Rechenoperation
2 + 2
```

#### Markdown für Text und Dokumentation

```Markdown
# Markdown
# Überschrift 1
### Überschrift 2
- oder * für Listen
[Linktext](URL)`
![Alt-Text](Bild-URL)
$2 + 2$
```

#### Magische Befehle

- `%time`: Zeigt die Ausführungszeit einer Zeile.
- `%matplotlib inline`: Erlaubt das Anzeigen von Matplotlib-Diagrammen direkt im Notebook.

#### Interaktive Widgets

dynamische, interaktive Benutzeroberflächen erstellen.

```python
from ipywidgets import interact
def f(x):
    return x
interact(f, x=10)
```

#### Tastenkombinationen

- `Shift + Enter`: Führe die aktuelle Zelle aus und gehe zur nächsten.
- `Esc`: Wechsle in den Kommandomodus.
- `M`: Ändere die Zelle in Markdown.
- `Y`: Ändere die Zelle in Code.

### Workflow - Python-Script

```bash
# Umgebungen auflisten
conda env list
# Erstelle eine neue Anaconda-Umgebung
conda create --name PythonGrundlagen_env python=3.12
# Anaconda-Umgebung aktivieren:
conda activate PythonGrundlagen_env
# Anaconda aktualisieren
conda update -all
# Suche nach einem spezifischen Paket
conda list | grep PyQt5
# Installiere die benötigte Software
conda install pyqt
# Skript ausführen
python3 kfz_datenbank.py
# Deaktivieren einer Anaconda-Umgebung
conda deactivate
# Eine Umgebung entfernen
conda env remove --name PythonGrundlagen_env
```

### Test grafische Benutzeroberfläche (GUI)

```python
# gui_script.py
# Test GUI
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Testfenster')
window.show()
sys.exit(app.exec_())

# Terminal
python3 gui_script.py
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

9. **Dokumentationsstrings (Docstrings)**:
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
# Installation
pip install flake8
pip install pylint
# Verwendung
flake8 script.py
pylint script.py
```
