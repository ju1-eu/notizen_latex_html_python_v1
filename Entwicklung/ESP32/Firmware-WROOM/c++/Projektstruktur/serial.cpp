// serial.cpp - Serielle Kommunikation
#include <Arduino.h>
#include "serial.h"

void serialSetup() {
  Serial.begin(115200);
}

void serialPrintMessage(const char* message) {
  Serial.println(message);
}