from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages


def visualize_meilensteine(data):
    df = pd.DataFrame(data)
    df["Datum"] = pd.to_datetime(df["Datum"])

    datumsbereich = (df["Datum"].max() - df["Datum"].min()).days

    # Bestimme den Locator und Formatter basierend auf dem Datumsbereich
    if datumsbereich <= 30:
        locator = mdates.DayLocator()
        formatter = mdates.DateFormatter("%Y-%m-%d")
    elif (
        datumsbereich < 365 * 2
    ):  # Für einen Bereich von bis zu zwei Jahren Monat und Jahr anzeigen
        locator = mdates.MonthLocator()
        formatter = mdates.DateFormatter("%Y-%m")
    else:  # Zeige nur das Jahr an, wenn der Zeitraum länger ist
        locator = mdates.YearLocator()
        formatter = mdates.DateFormatter("%Y")

    colors = ["red", "green", "blue", "orange", "purple"]  # Roadmap 5 Meilensteine
    # fig_size = (10.0, 7.0)  # B5-Größe in Zoll
    fig_size = (11.69, 8.27)  # DIN-A4 quer -Größe in Zoll
    fig, ax = plt.subplots(figsize=fig_size)
    ax.set(title="Spanienreise - Roadmap")

    for index, (color, row) in enumerate(zip(colors, df.iterrows())):
        row = row[1]
        ax.scatter(row["Datum"], row["Kategorie"], color=color, s=100)
        ax.text(
            row["Datum"], row["Kategorie"], str(index + 1), color="white", ha="center", va="center"
        )

    heute = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    ax.axvline(heute, color="red", linestyle="--")
    datum_text = heute.strftime("%d.%m.%Y")  # Formatierung des aktuellen Datums
    ax.plot([], [], color="red", linestyle="--", label=f"Heute: {datum_text}")

    tage_bis_erster_meilenstein = (df["Datum"].min() - heute).days
    ax.plot([], [], " ", label=f"Tage bis Start: {tage_bis_erster_meilenstein}")

    for index, color in enumerate(colors):
        ax.plot([], [], "o", color=color, markersize=10, label=df.iloc[index]["Beschreibung"])

    ax.legend(title="Legende", loc="upper left")
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    fig.autofmt_xdate()  # Verbessert die Darstellung der Datumsangaben auf der x-Achse

    ax.set_ylim(0, max(df["Kategorie"]) + 1)
    ax.yaxis.set_visible(False)

    plt.tight_layout()
    plt.savefig("Spanienreise-Roadmap.svg", format="svg")
    with PdfPages("Spanienreise-Roadmap.pdf") as pdf:
        pdf.savefig(fig)
    plt.show()
    plt.close()


# Beispiel-Daten für verschiedene Szenarien
# Roadmap 5 Meilensteine
data_jahr_monat = [
    {"Datum": "2024-03-10", "Beschreibung": "1. Home - La Jonquera (1244 km)", "Kategorie": 1},
    {
        "Datum": "2024-07-22",
        "Beschreibung": "2. Guardamar del Segura - Alicante (718 km)",
        "Kategorie": 1,
    },
    {"Datum": "2025-03-24", "Beschreibung": "3. Bilbao - Umgebung (ca. 838 km)", "Kategorie": 1},
    {"Datum": "2025-04-25", "Beschreibung": "4. Frankreich (ca. 800 km)", "Kategorie": 1},
    {
        "Datum": "2025-05-26",
        "Beschreibung": "5. Frankreich - Belgien - Home (ca. 800 km)",
        "Kategorie": 1,
    },
]

data_jahre = [
    {"Datum": "2024-03-20", "Beschreibung": "1. Home - La Jonquera (1244 km)", "Kategorie": 1},
    {
        "Datum": "2025-03-22",
        "Beschreibung": "2. Guardamar del Segura - Alicante (718 km)",
        "Kategorie": 1,
    },
    {"Datum": "2026-03-24", "Beschreibung": "3. Bilbao - Umgebung (ca. 838 km)", "Kategorie": 1},
    {"Datum": "2027-03-25", "Beschreibung": "4. Frankreich (ca. 800 km)", "Kategorie": 1},
    {
        "Datum": "2028-03-26",
        "Beschreibung": "5. Frankreich - Belgien - Home (ca. 800 km)",
        "Kategorie": 1,
    },
]

data_tage = [
    {"Datum": "2024-03-21", "Beschreibung": "1. Home - La Jonquera (1244 km)", "Kategorie": 1},
    {
        "Datum": "2024-03-22",
        "Beschreibung": "2. Guardamar del Segura - Alicante (718 km)",
        "Kategorie": 1,
    },
    {"Datum": "2024-03-24", "Beschreibung": "3. Bilbao - Umgebung (ca. 838 km)", "Kategorie": 1},
    {"Datum": "2024-03-25", "Beschreibung": "4. Frankreich (ca. 800 km)", "Kategorie": 1},
    {
        "Datum": "2024-03-26",
        "Beschreibung": "5. Frankreich - Belgien - Home (ca. 800 km)",
        "Kategorie": 1,
    },
]

# Urlaub
data_urlaub = [
    {"Datum": "2024-06-01", "Beschreibung": "1. Home - La Jonquera (1244 km)", "Kategorie": 1},
    {
        "Datum": "2024-06-02",
        "Beschreibung": "2. Guardamar del Segura - Alicante (718 km)",
        "Kategorie": 1,
    },
    {"Datum": "2024-06-19", "Beschreibung": "3. Bilbao - Umgebung (ca. 838 km)", "Kategorie": 1},
    {"Datum": "2024-06-21", "Beschreibung": "4. Frankreich (ca. 800 km)", "Kategorie": 1},
    {
        "Datum": "2024-06-22",
        "Beschreibung": "5. Frankreich - Belgien - Home (ca. 800 km)",
        "Kategorie": 1,
    },
]

# Wähle die passenden Daten für die Visualisierung
# visualize_meilensteine(data_jahr_monat)
# visualize_meilensteine(data_jahre)
# visualize_meilensteine(data_tage)
visualize_meilensteine(data_urlaub)
