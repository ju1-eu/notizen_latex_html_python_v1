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

- **led.cpp** - Steuerung der LED
- **serial.cpp** - Serielle Kommunikation
- **led.h** - Header-Datei für die LED-Steuerung
- **serial.h** - Header-Datei für die serielle Kommunikation

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

