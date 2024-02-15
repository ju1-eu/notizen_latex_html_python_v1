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
