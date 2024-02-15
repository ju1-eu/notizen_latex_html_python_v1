---
title: "PlattformIO"
author: 'ju'
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!-----------------------------------------------------------------------
ju 9-2-24 PlattformIO.md
pandoc PlattformIO.md -o PlattformIO.html -c inhalt.css --mathjax
------------------------------------------------------------------------->

## PlattformIO - ESP32 programmieren

ChatGPT <https://chat.openai.com/>

```markdown
# Für C- oder C++-Projekte wird oft der JavaDoc-Stil empfohlen
Erstelle Code mit Doxygen-kompatiblen Kommentaren

# Zusammenfassung
benutze Konventionen für Markdown
Schreibstil: Expositorisch ohne Form du/sie
Erstelle je nach Schreibstil eine ansprechende Zusammenfassung des folgenden Artikels in Aufzählungsform und gleichzeitig gebe die wichtigsten Informationen (Didaktische Reduktion) genau wieder. Bereite die Antwort gehirngerecht auf.

# ESP32 für PlattformIO programmieren
# Konventionen von PlatformIO für C++-Projekte
Erstelle ein "Hallo Welt"-C++Programm für einen ESP32 Mikrocontroller 
Erstelle ein "Hallo Welt"-Programm in MicroPython für einen ESP32 Mikrocontroller 
```


## PlatformIO installieren in VSCode

### Überprüfen der Installation

1. **Suchen Sie nach "PlatformIO IDE"** und klicken Sie auf "Installieren".
2. **Installieren Sie PlatformIO Core**
   ```sh
   python3 -m pip install -U platformio
   ```
3. **Überprüfen der Installation**
   ```sh
   pio --version
   ```

## VSCode für die Entwicklung mit MicroPython vorbereiten

### 1. Installieren von Visual Studio Code

[VSCode](https://code.visualstudio.com/)

### 2. Installieren der Python-Erweiterung

Python-Erweiterung von Microsoft.

### 3. Installieren der Pylance-Erweiterung (optional)

Pylance bietet erweiterte Intellisense-Funktionen, schnelle Autovervollständigung und Typüberprüfung.

### 4. Installieren der PyMakr-Erweiterung von Pycom

PyMakr ermöglicht es Ihnen, Code direkt auf MicroPython-Geräte hochzuladen, die REPL (Read-Eval-Print Loop) zu verwenden, um Befehle auf dem Gerät auszuführen, und bietet viele andere nützliche Funktionen für die MicroPython-Entwicklung.




## MicroPython-Firmware auf den ESP32 flashen

1. **Download der MicroPython-Firmware für ESP32**: <https://micropython.org/download/esp32/>

2. **Installieren eines seriellen Kommunikationstools**
   ```
   pip install esptool
   ```


## Entwickeln mit MicroPython

Sobald MicroPython auf Ihrem ESP32 installiert ist, können Sie Python-Skripte schreiben und auf dem Gerät ausführen. MicroPython bietet eine Vielzahl von Bibliotheken und Modulen, die speziell für die Hardwaresteuerung und -interaktion entwickelt wurden, einschließlich Netzwerkmodule, GPIO-Steuerung und vieles mehr.

```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)

while True:
    led.value(not led.value())
    time.sleep(0.5)
```


## Wechsel von C++ zu MicroPython:

Firmware-Auswahl <https://micropython.org/download/esp32/>


- **WROOM, PICO Module**: Verwenden Sie die Standard-Firmware ohne spezielle Zusätze im Dateinamen.
- **WROVER Module (mit SPIRAM/PSRAM)**: Wählen Sie die Firmware mit "spiram" im Dateinamen für Module, die über zusätzlichen SPIRAM verfügen.
- **OTA Updates**: Wenn Sie Over-the-Air-Update-Funktionalität benötigen, wählen Sie die "ota" Variante.


1. **Löschen des Flash-Speichers**:
   ```
   ls /dev/cu.*
   # WROOM
   esptool.py --chip esp32 --port /dev/cu.usbserial-0001 erase_flash
   # WROVER (Kamera)
   esptool.py --chip esp32 --port /dev/cu.usbserial-1460 erase_flash
   ```

2. **Flashen der MicroPython-Firmware**: 
   - **Für WROOM, PICO Module**:
     ```sh
     # Chip is ESP32-D0WD-V3 (revision v3.0)
     # Features: WiFi, BT, Dual Core, 240MHz
     esptool.py --chip esp32 --port /dev/cu.usbserial-0001 --baud 460800 write_flash -z 0x1000 ESP32_GENERIC-20240105-v1.22.1.bin
     ```
   - **Für WROVER Module (mit SPIRAM)**:
     ```sh
     # Chip is ESP32-D0WD-V3 (revision v3.0)
     # Features: WiFi, BT, Dual Core, 240MHz
     esptool.py --chip esp32 --port /dev/cu.usbserial-1460 --baud 460800 write_flash -z 0x1000 ESP32_GENERIC-SPIRAM-20240105-v1.22.1.bin
     ```

3. **MicroPython-Code auf den ESP32 hochladen**

Python-Skripte direkt auf dem Gerät ausführen.

- **ampy**: Ein Tool von Adafruit, um Dateien zu übertragen, Skripte auszuführen und mit der Python-REPL auf dem Mikrocontroller zu interagieren.
  ```bash
  pip install adafruit-ampy
  ls /dev/cu.*

  #------------------------------------------------
  # Python Entwicklung
  vim main.py
  #------------------------------------------------

  # WROOM
  ampy --port /dev/cu.usbserial-0001 put main.py
  # WROVER (Kamera)
  ampy --port /dev/cu.usbserial-1460 put main.py


  # Terminalprogramm: (seriellen Port)
  # Beenden: Ctrl-A + k
  # 
  screen /dev/cu.usbserial-0001 115200
  # 
  screen /dev/cu.usbserial-1460 115200
  ```

## Wechsel von MicroPython zu C++:


1. **Löschen des Flash-Speichers**:
   ```
   ls /dev/cu.*
   # WROOM
   esptool.py --chip esp32 --port /dev/cu.usbserial-0001 erase_flash
   # WROVER (Kamera)
   esptool.py --chip esp32 --port /dev/cu.usbserial-1460 erase_flash
   ```

3. **Vorbereiten der C++-Umgebung**: 
   - ESP-IDF (Espressif IoT Development Framework)
   - PlatformIO
   - Arduino-IDE.

4. **Kompilieren und Flashen des C++-Programms**:
   ```bash
     #------------------------------------------------
     # C++ Entwicklung
     vim main.cpp
     #------------------------------------------------
   ```

Uno - Esp-wrover-kit (Kamera) - Esp32dev


```bash
# platformio.ini
# Uno - Esp-wrover-kit (Kamera) - Esp32dev
[env:uno]
platform = atmelavr
board = uno
framework = arduino

[env:esp-wrover-kit]
platform = espressif32
board = esp-wrover-kit
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino

; Setzen Sie die Monitor-Optionen
monitor_speed = 115200
monitor_port = /dev/cu.usbserial-0001
monitor_filters = esp32_exception_decoder

# Pakete und Frameworks in PlatformIO zu aktualisieren
# Terminal
pio pkg update
pio pkg list
```

## Entwicklung von C++-Programmen

```cpp
// main.cpp
#include <Arduino.h>

void setup() {
  // Initialisiere die serielle Kommunikation mit einer Baudrate von 115200.
  Serial.begin(115200);
}

void loop() {
  // Sende "Hallo Welt" gefolgt von einem Zeilenumbruch an die serielle Schnittstelle.
  Serial.println("Hallo Welt!");
  // Warte eine Sekunde (1000 Millisekunden).
  delay(1000);
}
```

### DHT-Sensorbibliothek

Adafruit Unified Sensor-Bibliothek hinzufügen


```ini
# platformio.ini
lib_deps =
  adafruit/DHT sensor library@^1.4.0
  adafruit/Adafruit Unified Sensor
```

## Projektstruktur

```bash
# Projektstruktur
projekt/
|-- src
|   |-- main.cpp
|   |-- led.cpp
|   |-- serial.cpp
|-- include
|   |-- led.h
|   |-- serial.h
├── scripts/
│   └── setup_environment.py  # Python-Skript für Setup-Aufgaben
│
└── README.md
|
|-- platformio.ini
```


### Dateiinhalte

**platformio.ini** - Projekt-Konfigurationsdatei

```ini
; PlatformIO Project Configuration File
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
; Setzen Sie die Monitor-Optionen
monitor_speed = 115200
monitor_port = /dev/cu.usbserial-0001
monitor_filters = esp32_exception_decoder
```

**main.cpp** - Hauptdatei, die Setup und Loop enthält

```cpp
#include <Arduino.h>
#include "led.h"
#include "serial.h"

void setup() {
  serialSetup();
  ledSetup();
  // Sendet eine "Hallo Welt!"-Nachricht beim Start
  Serial.println("Hallo Welt!");
}

void loop() {
  ledBlink();
  serialPrintMessage("LED blinked!");
  delay(1000); // Wartezeit zwischen den Blinkvorgängen
}
```

**led.cpp** - Steuerung der LED

```cpp
// led.cpp - Steuerung der LED
#include <Arduino.h>
#include "led.h"

// Fügen Sie diese Zeile hinzu, wenn LED_BUILTIN nicht definiert ist.
#ifndef LED_BUILTIN
#define LED_BUILTIN 2
#endif

void ledSetup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void ledBlink() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}
```

**serial.cpp** - Serielle Kommunikation

```cpp
#include <Arduino.h>
#include "serial.h"

void serialSetup() {
  Serial.begin(115200);
}

void serialPrintMessage(const char* message) {
  Serial.println(message);
}
```

**led.h** - Header-Datei für die LED-Steuerung

```cpp
#ifndef LED_H
#define LED_H

void ledSetup();
void ledBlink();

#endif
```

**serial.h** - Header-Datei für die serielle Kommunikation

```cpp
#ifndef SERIAL_H
#define SERIAL_H

void serialSetup();
void serialPrintMessage(const char* message);

#endif
```

### Anleitung

1. Erstellen Sie die Projektstruktur
2. Öffnen Sie PlatformIO und importieren Sie Ihr Projekt

## Backup

### Erstellen eines `.code-workspace` für Visual Studio Code

1. **Öffnen Sie Ihr Projekt in Visual Studio Code**
2. **Erstellen Sie eine Workspace-Datei**: Sobald Ihr Projekt geöffnet ist, gehen Sie zu „File“ > „Save Workspace As...“ und speichern Sie die Workspace-Datei im Hauptverzeichnis Ihres Projekts. Geben Sie Ihrer Workspace-Datei einen passenden Namen und die Erweiterung `.code-workspace`.

### Wichtige Dateien und Ordner für ein Backup

- **src/**: Enthält Ihre Quellcode-Dateien (.cpp, .c) und Header-Dateien (.h).
- **include/**: Wird oft verwendet, um zusätzliche Header-Dateien zu speichern, die von Ihrem Quellcode referenziert werden.
- **lib/**: Falls Sie externe Bibliotheken hinzugefügt haben, die nicht über den PlatformIO-Bibliotheksmanager verwaltet werden, befinden sie sich hier.
- **test/**: Enthält Unit-Tests für Ihr Projekt.
- **platformio.ini**: Die Konfigurationsdatei Ihres Projekts, die die Board-Konfiguration, Abhängigkeiten und andere Einstellungen spezifiziert.
- **.vscode/**: Enthält VS Code-spezifische Einstellungen, einschließlich der Konfiguration für den Debugger und andere persönliche Einstellungen.
- **.code-workspace**: Die Workspace-Datei, die Sie erstellt haben, um Ihr Projekt in Visual Studio Code zu organisieren.

### Erstellen eines Backups

```bash
# Projektordner
cd /Users/jan/PlatformIO/Projects
zip -r Projekt_Backup_hallo_welt.zip hallo_welt/
zip -r Projekt_Backup_Projektstruktur.zip Projektstruktur/
mv *.zip /Users/jan/daten/start/IOT/Projekte-ESP32/Firmware-WROOM/c++

# Workspace-Datei  .code-workspace
/Users/jan/daten/start/IOT/Projekte-ESP32/Firmware-WROOM
  c++    python
/Users/jan/daten/start/IOT/Projeke-ESP32/Firmware-WROVER-Kamera
  c++    python
```

1. **Komprimieren**: Projektordner in eine ZIP-Datei

2. **Speichern auf einem externen Laufwerk oder in der Cloud**

3. **Versionierung**: Git, um Änderungen an Ihrem Projekt zu verfolgen und Backups einfacher zu verwalten.

