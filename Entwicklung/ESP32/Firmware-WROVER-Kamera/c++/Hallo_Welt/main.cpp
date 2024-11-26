// main.cpp
#include <Arduino.h>

void setup() {
  // Initialisiere die serielle Kommunikation mit einer Baudrate von 9600.
  Serial.begin(9600);
}

void loop() {
  // Sende "Hallo Welt" gefolgt von einem Zeilenumbruch an die serielle Schnittstelle.
  Serial.println("Hallo Welt!");
  // Warte eine Sekunde (1000 Millisekunden).
  delay(1000);
}
