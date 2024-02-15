/**
 * @file main.cpp
 * @brief Hauptdatei, die Setup und Loop für ein ESP32-Projekt enthält.
 * 
 * Dieses Programm initialisiert eine serielle Verbindung und eine LED,
 * sendet eine "Hallo Welt!"-Nachricht beim Start und lässt die LED in einer
 * Endlosschleife blinken.
 * 
 * Erweiterung des Programms um weitere Funktionalitäten: 
 * WiFi-Verbindung, Sensorabfrage und Datenverarbeitung 
 */

#include <Arduino.h>
#include "led.h"
#include "serial.h"

/**
 * @brief Setzt das System auf und sendet eine Startnachricht.
 * 
 * Diese Funktion wird beim Start des Mikrocontrollers aufgerufen. Sie
 * initialisiert die serielle Kommunikation und die LED und sendet
 * anschließend eine "Hallo Welt!"-Nachricht über die serielle Schnittstelle.
 */
void setup() {
  serialSetup(); // Initialisiert die serielle Kommunikation
  ledSetup();    // Initialisiert die LED
  
  // Sendet eine "Hallo Welt!"-Nachricht beim Start
  Serial.println("Hallo Welt!");
}

/**
 * @brief Hauptprogrammschleife, blinkt eine LED und sendet Nachrichten.
 * 
 * Diese Endlosschleife lässt eine LED blinken und sendet nach jedem Blinken
 * eine Nachricht ("LED blinked!") über die serielle Schnittstelle. Zwischen
 * den Blinkvorgängen wird eine Verzögerung von einer Sekunde eingehalten.
 */
void loop() {
  ledBlink(); // Lässt die LED blinken
  serialPrintMessage("LED blinked!"); // Sendet eine Nachricht, dass die LED geblinkt hat
  delay(1000); // Wartezeit zwischen den Blinkvorgängen
}
