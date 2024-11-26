import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.backends.backend_pdf import PdfPages
import locale

# Daten für das Beispiel
# Kategorie 1 = Zu erledigen, 2 = In Bearbeitung, 3 = Erledigt
data = [
    {"Datum": "2024-03-10", "Beschreibung": "Motoren", "Kategorie": 3},
    {"Datum": "2024-03-12", "Beschreibung": "Hindernis", "Kategorie": 3},
    {"Datum": "2024-03-15", "Beschreibung": "Ultraschallsensor", "Kategorie": 3},
    {"Datum": "2024-03-20", "Beschreibung": "Hindernisvermeidung + Folgesystem", "Kategorie": 3},
    {"Datum": "2024-04-01", "Beschreibung": "RGB-LED Streifen", "Kategorie": 2},
    {"Datum": "2024-04-05", "Beschreibung": "Energiesystem", "Kategorie": 1},
    {"Datum": "2024-04-10", "Beschreibung": "Servokippmechanismus", "Kategorie": 1},
    {"Datum": "2024-05-01", "Beschreibung": "Kamera Echtzeitsteuerung", "Kategorie": 1},
    {"Datum": "2024-05-10", "Beschreibung": "App", "Kategorie": 1},
]

df = pd.DataFrame(data)
df["Datum"] = pd.to_datetime(df["Datum"])

# Größe B5 in Zoll umrechnen (1 Zoll = 2.54 cm), quer Format
# fig_size = (10.0, 7.0)  # B5-Größe in Zoll
fig_size = (11.69, 8.27)  # DIN-A4 quer -Größe in Zoll


def visualize_meilensteine(df):
    fig, ax = plt.subplots(figsize=fig_size)
    ax.set(title="Kanban-Board - Projekt: Mars-Rover")

    # Definiere ein Farbschema für die Kategorien
    color_map = {1: "red", 2: "orange", 3: "green"}

    # Meilensteine nach Kategorien plotten
    for index, row in df.iterrows():
        ax.scatter(
            row["Datum"],
            row["Kategorie"],
            color=color_map[row["Kategorie"]],
            label=f"{index+1}. {row['Beschreibung']}",
            s=100,
            marker="x",
        )

    # Setze X-Achse nur für spezifische Meilenstein-Daten
    ax.set_xticks(df["Datum"])
    ax.set_xticklabels([datum.strftime("%Y-%m-%d") for datum in df["Datum"]])

    fig.autofmt_xdate()

    # Setze Y-Achse für Kategorien
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(["Zu erledigen", "In Bearbeitung", "Erledigt"])

    ax.legend()
    plt.tight_layout()

    # SVG- und PDF-Dateien speichern
    plt.savefig("Kanban-Board-Projekt-Mars-Rover.svg", format="svg")
    with PdfPages("Kanban-Board-Projekt-Mars-Rover.pdf") as pdf:
        pdf.savefig(fig, bbox_inches="tight")

    plt.show()
    plt.close()


visualize_meilensteine(df)
