import json
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd


# Funktion zum Laden der Meilensteine aus einer JSON-Datei
def load_meilensteine_from_json(filename):
    try:
        return pd.read_json(filename, convert_dates=["Datum"])
    except FileNotFoundError:
        return pd.DataFrame(columns=["Datum", "Beschreibung", "Kategorie"])


# Funktion zum Speichern der Meilensteine in eine JSON-Datei
def save_meilensteine_to_json(df, filename):
    df.to_json(filename, orient="records", date_format="iso", force_ascii=False)


# Funktion zum Anzeigen von Meilensteinen
def display_meilensteine(df):
    if df.empty:
        print("Keine Meilensteine vorhanden.")
    else:
        print(df)


# Funktion zum Bearbeiten eines Meilensteins
def edit_meilenstein(df):
    display_meilensteine(df)
    index = int(input("Wähle den Index des Meilensteins zum Bearbeiten (beginnend bei 0): "))
    datum = input("Neues Datum (YYYY-MM-DD): ")
    beschreibung = input("Neue Beschreibung: ")
    kategorie = int(input("Neue Kategorie: "))
    df.at[index, "Datum"] = pd.to_datetime(datum)
    df.at[index, "Beschreibung"] = beschreibung
    df.at[index, "Kategorie"] = kategorie
    print("Meilenstein bearbeitet.")


# Funktion zum Löschen eines Meilensteins
def delete_meilenstein(df):
    display_meilensteine(df)
    index = int(input("Wähle den Index des Meilensteins zum Löschen (beginnend bei 0): "))
    df.drop(index, inplace=True)
    df.reset_index(drop=True, inplace=True)  # Index nach dem Löschen zurücksetzen
    print("Meilenstein gelöscht.")


# Hauptfunktion zur Verwaltung von Meilensteinen
def manage_meilensteine(filename):
    df = load_meilensteine_from_json(filename)

    while True:
        action = input(
            "Wähle eine Aktion: Anzeigen (a), Bearbeiten (b), Löschen (l), Beenden (e): "
        )
        if action.lower() == "a":
            display_meilensteine(df)
        elif action.lower() == "b":
            edit_meilenstein(df)
        elif action.lower() == "l":
            delete_meilenstein(df)
        elif action.lower() == "e":
            # Speichere die Änderungen in die JSON-Datei, bevor das Programm beendet wird
            save_meilensteine_to_json(df, filename)
            print("Änderungen gespeichert. Programm beendet.")
            break
        else:
            print("Ungültige Eingabe.")


# Startpunkt des Skripts
if __name__ == "__main__":
    filename = "Meilensteine.json"
    manage_meilensteine(filename)
