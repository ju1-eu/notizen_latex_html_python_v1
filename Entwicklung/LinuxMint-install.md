---
title: 'Linux Mint'
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!--update 2-3-24-->

# Linux Mint

## Konfiguration

### 1. Systemaktualisierungen durchführen

- Öffnen Sie das Terminal und führen Sie den folgenden Befehl aus, um Ihre Paketquellen zu aktualisieren:
  ```
  sudo apt update
  ```
- Führen Sie dann folgenden Befehl aus, um alle verfügbaren Systemaktualisierungen zu installieren:
  ```
  sudo apt upgrade
  ```

### 2. Installieren Sie zusätzliche Treiber

- Linux Mint verfügt über ein Tool namens "Driver Manager", das Ihnen hilft, zusätzliche Treiber für Ihre Hardware zu finden und zu installieren. Obwohl es grafisch ist, können Sie überprüfen, ob zusätzliche Treiber verfügbar sind, indem Sie:
  ```
  sudo ubuntu-drivers list
  ```
- Und installieren Sie sie mit:
  ```
  sudo ubuntu-drivers autoinstall
  ```

### 3. Installieren Sie Codecs und zusätzliche Software

- Um Multimedia-Codecs zu installieren, die für die Wiedergabe von Musik und Videos erforderlich sind, verwenden Sie:
  ```
  sudo apt install mint-meta-codecs
  ```

### 4. Firewall-Konfiguration

- Aktivieren Sie die UFW-Firewall (Uncomplicated Firewall) mit folgendem Befehl:
  ```
  sudo ufw enable
  ```
- Überprüfen Sie den Status der Firewall mit:
  ```
  sudo ufw status
  ```

### 5. Systembereinigung

- Nach der Installation von Updates und neuen Paketen können Sie alte Pakete und Abhängigkeiten entfernen, die nicht mehr benötigt werden, mit:
  ```
  sudo apt autoremove
  ```

### 6. Installieren von Software aus dem Terminal

- Sie können Software direkt über das Terminal mit `apt` installieren. Zum Beispiel, um den Texteditor Vim zu installieren, verwenden Sie:
  ```
  sudo apt install vim
  ```

### 7. Erstellen Sie regelmäßige Backups

- Es ist eine gute Idee, ein Backup-Tool wie Timeshift zu verwenden, um Systembackups zu erstellen. Timeshift ist in Linux Mint vorinstalliert und kann über das Terminal konfiguriert werden, aber die Einrichtung und Verwaltung ist hauptsächlich über die grafische Oberfläche verfügbar.

### 8. Anpassen des Terminals

- Personalisieren Sie Ihr Terminal durch Anpassen der `.bashrc`- oder `.bash_aliases`-Dateien in Ihrem Home-Verzeichnis, um Aliase oder Funktionen für häufig verwendete Befehle zu erstellen.

### 9. Überwachen Sie Systemressourcen

- Installieren Sie `htop`, ein interaktives Tool zur Prozessüberwachung:
  ```
  sudo apt install htop
  ```
- Sie können es starten, indem Sie einfach `htop` in Ihrem Terminal eingeben.

### 10. Tastenkombinationen im Terminal

- Gewöhnen Sie sich an die Verwendung von Tastenkombinationen im Terminal, wie `Ctrl + C` zum Beenden eines Prozesses, `Ctrl + Z` zum Stoppen eines Prozesses und `fg` zum Fortsetzen im Vordergrund.

### Zusätzliche Tipps

- Experimentieren Sie mit verschiedenen Terminal-Emulatoren und Shells (wie zsh mit Oh My Zsh), um eine für Sie angenehme Arbeitsumgebung zu schaffen.
- Erkunden Sie die `man`-Seiten (Manual Pages) für Befehle, um mehr über ihre Funktionen und Optionen zu erfahren.

```bash
# Info
echo "Benutzer:" && whoami && echo "Hostname:" && hostname && echo "Festplattenspeicher:" && df -h && echo "RAM-Speicher:" && free -h && echo "IP-Adresse(n):" && hostname -I
# update
sudo apt update && sudo apt upgrade -y
```

### Netzwerkschnittstelle identifizieren

Zuerst müssen Sie den Namen der Netzwerkschnittstelle identifizieren, die Sie konfigurieren möchten. Dies können Sie mit dem Befehl `ip link` tun:

```bash
ip link
nmcli con show
```

Basierend auf der Ausgabe, die Sie erhalten haben, ist der Name Ihrer kabelgebundenen Verbindung `"Kabelgebundene Verbindung 1"`. Um nun Google's DNS-Server (8.8.8.8) für diese Verbindung zu konfigurieren, verwenden Sie den folgenden `nmcli` Befehlssatz:

1. DNS-Server auf 8.8.8.8 setzen:

```bash
nmcli con mod "Kabelgebundene Verbindung 1" ipv4.dns "8.8.8.8"
```

2. Automatische DNS-Einstellungen ignorieren:

```bash
nmcli con mod "Kabelgebundene Verbindung 1" ipv4.ignore-auto-dns yes
```

3. Die IP-Einstellungen auf automatisch belassen (sofern Sie keine statische IP verwenden möchten):

```bash
nmcli con mod "Kabelgebundene Verbindung 1" ipv4.method auto
```

4. Nachdem Sie diese Änderungen vorgenommen haben, starten Sie die Verbindung neu, um die Änderungen zu übernehmen:

```bash
nmcli con down "Kabelgebundene Verbindung 1" && nmcli con up "Kabelgebundene Verbindung 1"
```

Um den DNS-Server auch für Ihre WLAN-Verbindung, die als `"n2g"` bezeichnet wird, auf 8.8.8.8 zu setzen, folgen wir einem ähnlichen Prozess wie zuvor. Dies wird sicherstellen, dass Ihre WLAN-Verbindung ebenfalls von der schnellen und zuverlässigen Namensauflösung durch Google's DNS profitiert. Denken Sie daran, wie ein Navigator, der plötzlich eine klarere und präzisere Karte erhält; so verbessert ein schneller DNS-Server die Navigation im Internet.

1. **DNS-Server für die WLAN-Verbindung setzen:**
   
   Beginnen wir damit, Google's DNS-Adresse der Verbindung `n2g` zuzuweisen. Dieser Schritt ist vergleichbar mit dem Einstellen eines neuen Ziels in Ihrem GPS:
   ```bash
   nmcli con mod "n2g" ipv4.dns "8.8.8.8"
   ```

2. **Automatische DNS-Einstellungen ignorieren:**
   
   Als Nächstes sagen wir Ihrem System, dass es nicht mehr die automatisch zugewiesenen DNS-Server verwenden soll, ähnlich wie wenn Sie entscheiden, nicht den vorgeschlagenen Routen eines GPS zu folgen, weil Sie einen besseren Weg kennen:
   ```bash
   nmcli con mod "n2g" ipv4.ignore-auto-dns yes
   ```

3. **IP-Einstellungen auf automatisch belassen:**
   
   Wir behalten die automatische IP-Konfiguration bei. Das ist so, als würden Sie sich entscheiden, die Automatikfunktion Ihres Autos zu nutzen, während Sie gleichzeitig das Ziel selbst bestimmen:
   ```bash
   nmcli con mod "n2g" ipv4.method auto
   ```

4. **Verbindung neu starten:**
   
   Zum Schluss, ähnlich wie das Neustarten eines Geräts nach einer Softwareaktualisierung, starten wir die Verbindung neu, um die Änderungen wirksam zu machen:
   ```bash
   nmcli con down "n2g" && nmcli con up "n2g"
   ```


## zweiten Benutzer erstellen

### 1. Benutzer banking erstellen

Zuerst erstellen Sie den neuen Benutzer `banking`. Der folgende Befehl fügt den Benutzer hinzu und erstellt ein Home-Verzeichnis für ihn:

```bash
sudo adduser banking
```

Folgen Sie den Anweisungen, um das Passwort festzulegen und die optionalen Benutzerinformationen auszufüllen.

### 2. Sicherheitsmaßnahmen

#### a. Festlegen starker Passwörter

Stellen Sie sicher, dass für alle Benutzerkonten, einschließlich `banking`, starke Passwörter verwendet werden. Linux Mint verwendet PAM (Pluggable Authentication Modules), um Passwortrichtlinien zu verwalten. Sie können die Passwortkomplexität in der Konfigurationsdatei `/etc/pam.d/common-password` anpassen. Zum Beispiel:

```bash
sudo vim /etc/pam.d/common-password
#password requisite pam_pwquality.so retry=3 minlen=8 difok=3 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

#### b. Firewall aktivieren

Aktivieren Sie die UFW (Uncomplicated Firewall), um den Netzwerkzugriff zu kontrollieren:

```bash
sudo ufw enable
sudo ufw status verbose
```

Konfigurieren Sie die Regeln nach Bedarf, z.B.: erlauben

```bash
sudo ufw allow ssh
sudo ufw allow from 192.168.1.0/24 to any port 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw reload
```

#### c. SELinux oder AppArmor

Prüfen Sie, ob AppArmor (standardmäßig in Ubuntu und Mint) aktiv und korrekt konfiguriert ist. Sie können den Status mit folgendem Befehl überprüfen:

```bash
sudo apparmor_status
```

Für eine strengere Zugriffskontrolle und Sicherheitsrichtlinien könnte SELinux eine Alternative sein, erfordert jedoch eine sorgfältige Konfiguration.

#### d. Regelmäßige Updates

Stellen Sie sicher, dass Ihr System und alle Anwendungen regelmäßig aktualisiert werden, um Sicherheitslücken zu schließen:

```bash
sudo apt update && sudo apt upgrade -y
```

#### e. Verschlüsselung nutzen

Für zusätzliche Sicherheit, insbesondere für einen Banking-Benutzer, sollten Sie die Verschlüsselung von Daten in Betracht ziehen, z.B. mit `ecryptfs` für das Home-Verzeichnis oder `veracrypt` für Container-basierte Verschlüsselung.

#### f. Zugriffsrechte einschränken

Das Einschränken von Zugriffsrechten für den Benutzer `banking` auf nur die notwendigen Ressourcen ist eine wichtige Maßnahme, um die Sicherheit Ihres Systems zu erhöhen. Linux bietet dafür die Befehle `chmod` (Change Mode) und `chown` (Change Owner), mit denen Sie die Zugriffsrechte und den Besitz von Dateien und Verzeichnissen steuern können. Hier sind einige grundlegende Schritte und Beispiele, wie Sie dies tun können:

##### Verstehen der Zugriffsrechte

- Zugriffsrechte in Linux werden für den Besitzer (u), die Gruppe (g) und andere (o) definiert.
- Rechte können Lesezugriff (r), Schreibzugriff (w) und Ausführung (x) umfassen.

##### Besitz mit chown ändern

- Um den Besitzer einer Datei oder eines Verzeichnisses zu ändern, verwenden Sie `chown`. Zum Beispiel, um den Besitzer der Datei `datei.txt` auf den Benutzer `banking` zu ändern:
  ```bash
  sudo chown banking:datei.txt
  ```
- Um den Besitzer rekursiv in einem Verzeichnis und seinen Unterverzeichnissen zu ändern, verwenden Sie die Option `-R`:
  ```bash
  sudo chown -R banking /pfad/zum/verzeichnis
  ```

##### Zugriffsrechte mit chmod ändern

- Verwenden Sie `chmod`, um die Zugriffsrechte zu ändern. Zum Beispiel, um dem Besitzer Lese- und Schreibrechte zu geben, aber alle anderen auszuschließen:
  ```bash
  chmod 600 datei.txt
  ```
  Hier bedeutet `600`, dass der Besitzer lesen (`4`) und schreiben (`2`) kann, aber niemand anderes Zugriff hat.

- Um einem Verzeichnis Lese-, Schreib- und Ausführungsrechte für den Besitzer zu geben und die Rechte für die Gruppe und andere zu entfernen:
  ```bash
  chmod 700 /pfad/zum/verzeichnis
  ```
  `700` gibt dem Besitzer alle Rechte, während Gruppe und andere keine Rechte haben.

##### Beschränken des Zugriffs auf bestimmte Verzeichnisse

- Stellen Sie sicher, dass der Benutzer `banking` nur Zugriff auf die Verzeichnisse hat, die er benötigt. Verwenden Sie `chown` und `chmod`, um den Zugriff auf andere Verzeichnisse zu beschränken. Zum Beispiel:
  - Beschränken Sie den Zugriff auf das Home-Verzeichnis des Benutzers `banking`:
    ```bash
    sudo chown -R banking:banking /home/banking
    sudo chmod -R 700 /home/banking
    ```

## VS-Code

### 1. Python installieren

Linux Mint kommt typischerweise mit Python 3 vorinstalliert. Sie können die Installation überprüfen und die Version anzeigen lassen mit:
```bash
python3 --version
```
Wenn Python 3 nicht installiert ist oder Sie eine spezifische Version benötigen, können Sie es mit folgendem Befehl installieren:
```bash
sudo apt update
sudo apt install python3
```

### 2. Visual Studio Code (VS Code) installieren

VS Code kann über die Kommandozeile mittels Snap (falls verfügbar) oder durch Hinzufügen des offiziellen Microsoft Repositories installiert werden. Hier ist der Weg über das Repository:

```bash
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm microsoft.gpg

sudo apt install apt-transport-https
sudo apt update
sudo apt install code

sudo apt update
sudo apt install thunderbird

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
```

### 3. code zum PATH hinzufügen

Normalerweise wird der `code`-Befehl automatisch zum PATH hinzugefügt. Sie können dies überprüfen, indem Sie `code --version` eingeben. Sollte der Befehl nicht gefunden werden, stellen Sie sicher, dass der Installationspfad von VS Code zu Ihrem PATH hinzugefügt ist. Dies kann je nach Installationsmethode variieren.

### 4. clang-format installieren

Um `clang-format` zu installieren, verwenden Sie den folgenden Befehl:
```bash
sudo apt update
sudo apt install clang-format
```

### Überprüfen der Installationen und PATH-Konfiguration

Nachdem Sie diese Schritte durchgeführt haben, sollten Sie in der Lage sein, `python3`, `code`, und `clang-format` direkt aus dem Terminal heraus zu verwenden. Verwenden Sie die `--version` Option, um die Installation jeder dieser Anwendungen zu überprüfen:

```bash
python3 --version
code --version
clang-format --version
```


## Anaconda

Um Anaconda Version 2024.02-1 auf einem Linux x86_64-System zu installieren, führen Sie die folgenden Schritte im Terminal aus. Diese Anleitung geht davon aus, dass Sie bereits die notwendigen Voraussetzungen installiert haben, wie in Ihrer vorherigen Nachricht beschrieben.

### Schritt 1: Anaconda-Installer herunterladen

Öffnen Sie ein Terminal und verwenden Sie `curl` oder `wget`, um den Anaconda-Installer herunterzuladen. Da Sie den Dateinamen bereits angegeben haben (`Anaconda3-2024.02-1-Linux-x86_64.sh`), können Sie den folgenden Befehl direkt verwenden:

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh
```

### Schritt 2: Installer-Skript ausführbar machen

Machen Sie das heruntergeladene Skript ausführbar:

```bash
chmod +x Anaconda3-2024.02-1-Linux-x86_64.sh
```

### Schritt 3: Anaconda installieren

Starten Sie nun die Installation mit dem folgenden Befehl:

```bash
rm -rf ~/anaconda3
./Anaconda3-2024.02-1-Linux-x86_64.sh
```

Folgen Sie den Anweisungen auf dem Bildschirm. Dabei werden Sie aufgefordert, die Lizenzvereinbarungen zu akzeptieren, einen Installationsort auszuwählen und zu entscheiden, ob `conda init` ausgeführt werden soll. Es wird empfohlen, `yes` zu wählen, um `conda init` auszuführen, da dies sicherstellt, dass Conda korrekt in Ihrer Shell initialisiert wird.

### Schritt 4: Shell neu starten

Um die Installation abzuschließen und Änderungen wirksam zu machen, schließen Sie Ihr aktuelles Terminalfenster und öffnen Sie ein neues. Alternativ können Sie die Konfiguration Ihrer aktuellen Shell mit dem folgenden Befehl aktualisieren:

```bash
source ~/.bashrc
```

### Schritt 5: Überprüfen der Installation

Überprüfen Sie abschließend, ob Anaconda korrekt installiert wurde, indem Sie die Conda-Version überprüfen:

```bash
conda --version

conda update conda
conda update anaconda
```



Um Python 3.12.1 mit `pyenv` unter Linux Mint zu installieren, folgen Sie diesen Schritten. `pyenv` ist ein einfaches, leistungsstarkes Tool, das es Ihnen ermöglicht, problemlos zwischen mehreren Python-Versionen zu wechseln.

### Schritt 1: Abhängigkeiten für den Python-Bau installieren

Vor der Installation von `pyenv` ist es wichtig, alle erforderlichen Bibliotheken zu installieren, die für den Bau verschiedener Python-Versionen benötigt werden. Führen Sie den folgenden Befehl aus, um die gängigsten Abhängigkeiten zu installieren:

```bash
sudo apt-get update
sudo apt-get install libssl-dev
pip install cryptography

sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev git
```

### Schritt 2: pyenv installieren

Es gibt verschiedene Methoden, `pyenv` zu installieren. Eine der einfachsten ist die Verwendung von `git`:

```bash
curl https://pyenv.run | bash
```

Dieser Befehl lädt ein Skript herunter und führt es aus, das `pyenv` und auch einige häufig verwendete Plugins wie `pyenv-virtualenv` installiert.

### Schritt 3: pyenv Umgebung konfigurieren

Nach der Installation müssen Sie die Shell-Umgebung konfigurieren, um `pyenv` automatisch zu initialisieren. Fügen Sie die folgenden Zeilen am Ende Ihrer `~/.bashrc` oder `~/.zshrc` Datei hinzu:

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

Anschließend führen Sie den folgenden Befehl aus, um die Änderungen zu übernehmen:

```bash
source ~/.bashrc
```

### Schritt 4: Python 3.12.1 installieren

Jetzt, wo `pyenv` konfiguriert ist, können Sie Python 3.12.1 installieren:

```bash
pyenv install 3.12.1
```

Dieser Vorgang kann einige Minuten dauern, da `pyenv` die angegebene Python-Version aus dem Quellcode kompiliert.

### Schritt 5: Die globale Python-Version einstellen

Nach der Installation können Sie Python 3.12.1 als Ihre globale Python-Version festlegen:

```bash
pyenv global 3.12.1
```

### Schritt 6: Überprüfen der Python-Version

Überprüfen Sie abschließend, ob die richtige Python-Version eingestellt ist:

```bash
python --version
conda list python
```


## Latex und Pandoc


1. **Wählen Sie ein Arbeitsverzeichnis:**
   Normalerweise wird `/tmp` als temporäres Verzeichnis verwendet, aber Sie können jedes gewünschte Verzeichnis wählen.

   ```bash
   cd /tmp
   ```

2. **Download des Installations-Skripts:**
   Verwenden Sie `wget` oder `curl`, um das TeX Live Installations-Skript herunterzuladen.

   ```bash
   wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
   ```
  

3. **Extrahieren des Installations-Skripts:**
   Extrahieren Sie die heruntergeladene Datei.

   ```bash
   zcat < install-tl-unx.tar.gz | tar xf -
   ```

4. **Wechseln Sie in das Installationsverzeichnis:**

   ```bash
   cd install-tl-20240302
   ```

5. **Starten Sie die Installation:**
   Führen Sie die Installation mit Perl und ohne Interaktion durch. Sie müssen entweder Root-Rechte haben oder in ein Verzeichnis schreiben, für das Sie Schreibrechte besitzen.

   ```bash
   perl ./install-tl --no-interaction --paper=a4 --scheme=full --no-doc-install --no-src-install
   ```

6. **Aktualisieren Sie Ihre PATH-Umgebungsvariable:**
   Fügen Sie den Pfad zum TeX Live-Verzeichnis Ihrer `PATH`-Umgebungsvariable hinzu, um die TeX Live-Befehle systemweit verfügbar zu machen. Ersetzen Sie `YYYY` durch das Installationsjahr und `PLATFORM` durch Ihre Plattform (z.B. `x86_64-linux`).

   ```bash
   export PATH=/usr/local/texlive/2023/bin/x86_64-linux:$PATH
   source ~/.bashrc
   ```

```bash
# update
sudo apt-get update
sudo apt-get upgrade

which tlmgr
sudo /usr/local/texlive/2023/bin/x86_64-linux/tlmgr update --self
sudo /usr/local/texlive/2023/bin/x86_64-linux/tlmgr update --all
export PATH=/usr/local/texlive/2023/bin/x86_64-linux:$PATH
source ~/.bashrc

sudo apt-get install pandoc

# Editor
sudo update-alternatives --config editor
source ~/.bashrc

sudo apt-get update
sudo apt-get install ghostscript
sudo apt-get install webp
pip3 install jinja2
```

### Überprüfung der Installationen

- Um die Version von TeX Live/LaTeX zu überprüfen, verwenden Sie:
  
  ```bash
  latex --version
  pdflatex --version
  pandoc --version
  ```


### Schritte zur Installation von ImageMagick 7 aus dem Quellcode auf Linux Mint:

1. **Abhängigkeiten installieren:**

   Bevor Sie mit der Installation beginnen, müssen Sie einige Abhängigkeiten installieren, die für den Bau von ImageMagick notwendig sind:

   ```bash
   sudo apt-get update
   sudo apt-get install libheif-dev

   sudo apt-get install build-essential checkinstall libx11-dev libxext-dev zlib1g-dev libpng-dev libjpeg-dev libfreetype6-dev libxml2-dev
   ```

2. **ImageMagick herunterladen:**

   Laden Sie den neuesten Quellcode von ImageMagick von der offiziellen Website herunter:

   ```bash
   wget https://www.imagemagick.org/download/ImageMagick.tar.gz
   ```

3. **Quellcode extrahieren:**

   Extrahieren Sie den heruntergeladenen Tarball:

   ```bash
   tar xvzf ImageMagick.tar.gz
   ```

4. **In das Verzeichnis wechseln:**

   Wechseln Sie in das Verzeichnis, das durch das Extrahieren des Tarballs erstellt wurde. Der genaue Name des Verzeichnisses variiert je nach der Version von ImageMagick, die Sie heruntergeladen haben:

   ```bash
   cd ImageMagick-7*
   ```

5. **Konfigurieren des Builds:**

   Führen Sie das Konfigurationsskript aus, um den Build-Prozess vorzubereiten:

   ```bash
   ./configure --with-heic=yes
   ```

6. **ImageMagick kompilieren:**

   Kompilieren Sie ImageMagick mit dem `make`-Befehl:

   ```bash
   make
   ```

7. **ImageMagick installieren:**

   Installieren Sie ImageMagick auf Ihrem System:

   ```bash
   sudo make install
   ```

8. **Konfigurieren Sie die dynamische Linker-Laufzeit-Bindungen:**

   ```bash
   sudo ldconfig /usr/local/lib
   ```

9. **Überprüfen der Installation:**

   Überprüfen Sie, ob ImageMagick korrekt installiert wurde:

   ```bash
   magick -version
   magick -list format | grep HEIC
   ```

### Schrift

```bash
mkdir -p ~/.local/share/fonts
cp ~/Downloads/static/SourceCodePro*.ttf ~/.local/share/fonts/
fc-cache -fv
```


### Nutzung

- Um ein LaTeX-Dokument in ein PDF umzuwandeln, navigieren Sie im Terminal zum Verzeichnis Ihres `.tex`-Dokuments und verwenden Sie:

  ```bash
  pdflatex mein_dokument.tex
  pandoc mein_dokument.md -o mein_dokument.pdf
  ```

## Backup

```bash
#!/bin/bash -e
# ju 2-3-24 backup.sh
# Backup erstellen
# chmod +x backup.sh
# ./backup.sh

# Variablen
QUELLE="/media/guenther/start/"
ZIEL="/home/guenther/"

# Verzeichnisname, der gesichert werden soll
VERZEICHNIS="start"

# Backup von Verzeichnis
echo "Starte Backup von $VERZEICHNIS..."
rsync -av --delete "$QUELLE$VERZEICHNIS/" "$ZIEL$VERZEICHNIS/"

# Log
echo "+ Backup von $VERZEICHNIS fertig."
```

## Hardware Info


### 1. lscpu

Zeigt Informationen über die CPU-Architektur an, einschließlich Anzahl der CPUs, Kerne pro CPU, Threads pro Kern, CPU-Familie und Modell.

```bash
lscpu
```

### 2. lsblk

Listet alle verfügbaren Speichergeräte auf, einschließlich Festplatten und Partitionen, sowie deren Größe und Montagepunkte.

```bash
lsblk
```

### 3. free und vmstat

- `free` zeigt Informationen über den freien und genutzten Arbeitsspeicher (RAM) sowie den Swap-Speicher des Systems an.

```bash
free -h
```

- `vmstat` berichtet über den virtuellen Speicher, Prozesse, Paging und CPU-Aktivität.

```bash
vmstat
```

### 4. lspci

Zeigt detaillierte Informationen über alle PCI-Busse und Geräte im System an, wie Grafikkarten, Netzwerkkarten usw.

```bash
lspci
```

### 5. lsusb

Zeigt Informationen über USB-Busse im System und die daran angeschlossenen Geräte an.

```bash
lsusb
```

### 6. df und du

- `df` berichtet über die Systemdateisystem-Disk-Nutzung.

```bash
df -h
```

- `du` zeigt den Speicherplatz an, der von Dateien oder Verzeichnissen belegt wird.

```bash
du -sh <Verzeichnispfad>
```

### 7. hdparm und smartctl

- `hdparm` zeigt Informationen über Festplattenlaufwerke und kann auch Einstellungen ändern.

```bash
sudo hdparm -I /dev/sda
```

- `smartctl` prüft den Zustand von Festplatten unter Verwendung der SMART-Selbstüberwachungstechnologie.

```bash
sudo smartctl -a /dev/sda
```

### 8. inxi

`inxi` ist ein leistungsstarkes Befehlszeilen-Systeminformations-Tool, das eine detaillierte Übersicht über die Systemhardware bietet. Es ist möglicherweise nicht standardmäßig installiert, kann aber leicht hinzugefügt werden.

```bash
sudo apt install inxi
inxi -F
```


- **System:** Sie verwenden Linux Mint 21.3 Virginia mit dem Kernel 5.15.0-91-generic auf einem Lenovo ThinkPad E550 Laptop. Das Desktop-Umgebung ist Xfce 4.18.1.

- **CPU:** Ihr Laptop hat einen Intel Core i5-5200U Prozessor mit zwei Kernen und Hyper-Threading, was insgesamt vier Threads ermöglicht. Die durchschnittliche Geschwindigkeit beträgt etwa 2212 MHz.

- **Grafik:** Es ist eine Intel HD Graphics 5500 Grafikkarte installiert. Die Grafikausgabe erfolgt über X11 mit dem i915 Treiber. Die Bildschirmauflösung beträgt 1920x1080 bei 60Hz.

- **Audio:** Es sind mehrere Audiogeräte installiert, darunter Intel Broadwell-U Audio und Intel Wildcat Point-LP High Definition Audio, beide nutzen den Treiber snd_hda_intel. Es laufen mehrere Soundserver, darunter ALSA, PulseAudio und PipeWire.

- **Netzwerk:** Für die Netzwerkverbindung sind ein Intel Ethernet I218-V und ein Intel Wireless 3160 Adapter installiert. Beide Geräte sind aktiv und verbunden.

- **Bluetooth:** Ein Intel Bluetooth wireless Interface ist vorhanden und aktiv.

- **Speicher:** Das System verfügt über insgesamt 1.02 TiB Speicherplatz, wovon 140.22 GiB verwendet werden. Die Hauptfestplatte ist eine Western Digital WD10SPCX-08S8TT0 mit 931.51 GiB Speicherkapazität. Zusätzlich ist ein 114.61 GiB großer SanDisk USB 3.2Gen1 Speicher angeschlossen.

- **Partitionen:** Die Hauptpartition `/` hat eine Größe von 907.84 GiB, von denen 75.99 GiB verwendet werden. Es gibt eine separate EFI-Systempartition mit 486 MiB und eine Swap-Partition mit 7.63 GiB.

- **Sensoren:** Die CPU-Temperatur liegt bei 45.0°C und die PCH-Temperatur bei 41.0°C. Der CPU-Lüftergeschwindigkeit wird als 0 RPM angezeigt, was darauf hindeuten könnte, dass der Lüfter entweder sehr leise läuft oder die Messung nicht verfügbar ist.


- **HDD (Hard Disk Drive) oder eine SSD (Solid State Drive)**


```bash
lsblk -d -o name,rota
```

In der Ausgabe dieses Befehls steht die Spalte `ROTA` für "Rotational". Wenn der Wert in dieser Spalte `1` ist, deutet dies darauf hin, dass das Gerät rotierende Teile hat, was typisch für eine HDD ist. Ein Wert von `0` in dieser Spalte weist hingegen auf eine SSD hin, da SSDs keine rotierenden Teile enthalten.

Die Ausgabe dieses Befehls ist ähnlich der des `lsblk`-Befehls: `1` für HDDs und `0` für SSDs.

## PlatformIO

### 1. Deinstallieren der aktuellen PlatformIO-Version

```bash
sudo apt remove platformio
```

### 2. Überprüfen, ob pip installiert ist

Bevor Sie fortfahren, stellen Sie sicher, dass `pip`, der Python-Paketmanager, auf Ihrem System installiert ist. Wenn `pip` nicht installiert ist, können Sie es mit dem folgenden Befehl installieren:

```bash
sudo apt install python3-pip
```

### 3. Installieren von PlatformIO über pip

Nachdem `pip` installiert ist und die alte Version von PlatformIO deinstalliert wurde, können Sie die neueste Version von PlatformIO mit `pip` installieren. Führen Sie den folgenden Befehl aus:

```bash
pip3 install -U platformio
```

Dieser Befehl aktualisiert PlatformIO auf die neueste Version, indem er es global über `pip` installiert.

### PATH


1. **Fügen Sie am Ende der Datei die folgende Zeile hinzu**, um `/home/guenther/.local/bin` zu Ihrem `PATH` hinzuzufügen:

    ```bash
    vim ~/.bashrc
    export PATH="$HOME/.local/bin:$PATH"
    source ~/.bashrc
    ```

2. **Überprüfen Sie, ob pio nun erkannt wird**, indem Sie erneut versuchen, die Version von PlatformIO anzuzeigen:

    ```bash
    pio --version
    ```


### Port Ihres Arduino Uno unter PlatformIO anzeigen

1. **Öffnen Sie ein Terminal** auf Ihrem Computer.

2. **Führen Sie den folgenden Befehl aus:**

   ```bash
   pio device list
   ```

```bash
pio device list
# Ausgabe
/dev/ttyUSB0
------------
Hardware ID: USB VID:PID=10C4:EA60 SER=0001 LOCATION=2-2
Description: CP2102 USB to UART Bridge Controller - CP2102 USB to UART Bridge Controller

/dev/ttyACM0
------------
Hardware ID: USB VID:PID=2341:0043 SER=95635333430351118201 LOCATION=2-1:1.0
Description: ttyACM0

```

### Port in PlatformIO-Projektdatei spezifizieren

Wenn Sie den Port kennen, den Ihr Arduino Uno verwendet, und Sie möchten sicherstellen, dass PlatformIO diesen Port für den Upload verwendet, können Sie den Port in Ihrer `platformio.ini`-Konfigurationsdatei spezifizieren:

```ini
[env:arduino_uno]
platform = atmelavr
board = uno
framework = arduino
upload_port = /dev/ttyACM0
```

### Hinweis

Stellen Sie sicher, dass Ihr Benutzer zur `dialout`-Gruppe gehört, um Zugriff auf den seriellen Port zu haben, ohne `sudo` verwenden zu müssen.

```bash
sudo usermod -a -G dialout $USER
```


### 99-platformio-udev.rules

**Installieren der 99-platformio-udev.rules.** Dies ist notwendig, damit Ihr System die angeschlossenen Entwicklungsboards richtig erkennen und mit den entsprechenden Berechtigungen verwalten kann.

```bash
sudo wget https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules -O /etc/udev/rules.d/99-platformio-udev.rules
```

1. **Reload der udev Regeln**, damit die Änderungen übernommen werden:

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

2. **Hinzufügen Ihres Benutzers zur 'dialout' Gruppe**, um seriellen Zugang zu ermöglichen, falls noch nicht geschehen:

```bash
sudo usermod -a -G dialout $USER
```


## Arduino IDE

### 1. Extrahieren der Zip-Datei

```bash
cd ~/Downloads
unzip arduino-ide_2.3.2_Linux_64bit.zip -d ~/ArduinoIDE
```

### 1. Ausführungsrechte setzen

Zuerst müssen Sie sicherstellen, dass die Haupt-Ausführungsdatei der IDE (`arduino-ide`) ausführbar ist.

```bash
chmod +x arduino-ide
```

### 2. Die Arduino IDE starten

Nachdem Sie die Ausführungsrechte gesetzt haben, können Sie die Arduino IDE direkt ausführen:

```bash
./arduino-ide
```

### Optionale Schritte

- **Erstellen einer Desktop-Verknüpfung:**  `vim ~/.local/share/applications/.desktop` 

```ini
[Desktop Entry]
Name=Arduino IDE
Comment=Open-source electronics platform
Exec=/home/guenther/ArduinoIDE/arduino-ide
Icon=/home/guenther/ArduinoIDE/icon.png
Terminal=false
Type=Application
Categories=Development;IDE;
```

- **Direkter Zugriff über das Terminal:** Sie könnten auch einen Alias in Ihrer `.bashrc` oder `.zshrc` Datei erstellen, um die IDE schnell aus dem Terminal zu starten:

```bash
vim .bashrc
alias arduinoide='/home/guenther/ArduinoIDE/arduino-ide'
```
