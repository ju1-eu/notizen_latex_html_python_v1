/**
 * @file hallo-welt.c
 * @brief Ein einfaches Hallo Welt Programm in C.
 *
 * Dieses Programm gibt die Nachricht "Hallo Welt" auf der Standardausgabe aus.
 * Es dient als einführendes Beispiel für die Ausgabe in C-Programmen.
 */

#include <stdio.h>

/**
 * @brief Hauptfunktion des Programms.
 *
 * Gibt eine Grußnachricht auf der Standardausgabe aus und beendet sich dann
 * mit einem erfolgreichen Exit-Code.
 *
 * @return int Rückgabewert des Programms. 0 signalisiert ein erfolgreiches
 * Beenden.
 */
int main(void) {
  printf("Hallo Welt\n");  // Ausgabe der Grußnachricht
  return 0;                // Erfolgreicher Exit-Code
}
