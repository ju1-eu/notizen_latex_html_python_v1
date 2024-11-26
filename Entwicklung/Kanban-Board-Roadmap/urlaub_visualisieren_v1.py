import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.backends.backend_pdf import PdfPages


def visualize_meilensteine(data):
    df = pd.DataFrame(data)
    df["Datum"] = pd.to_datetime(df["Datum"])

    # Farben und Größe der Visualisierung
    colors = ["red", "green", "blue", "orange", "purple"]
    # fig_size = (10.0, 7.0)  # B5-Größe in Zoll
    fig_size = (11.69, 8.27)  # DIN-A4 quer -Größe in Zoll

    fig, ax = plt.subplots(figsize=fig_size)
    ax.set(title="Spanienreise - Roadmap")

    # Plotten der Meilensteine basierend auf Entfernung
    for index, (color, row) in enumerate(zip(colors, df.iterrows())):
        row = row[1]
        ax.scatter(
            row["Datum"],
            row["Entfernung"],
            color=color,
            s=100,
            label=f"{index + 1}. {row['Beschreibung']} ({row['Entfernung']} km)",
        )

    heute = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    ax.axvline(heute, color="red", linestyle="--", label="Heute")

    startdatum = df["Datum"].min()
    tage_bis_start = (startdatum - heute).days
    legende_text = f"Tage bis Start: {tage_bis_start}"
    ax.plot([], [], " ", label=legende_text)

    # Setzen der X-Achsen-Ticks auf die Datumsangaben der Meilensteine plus heute
    alle_datums = sorted(df["Datum"].tolist() + [heute])
    ax.set_xticks(alle_datums)
    ax.set_xticklabels(
        [datum.strftime("%Y-%m-%d") for datum in alle_datums], rotation=45, ha="right"
    )

    # Y-Achse für Entfernungen
    ax.set_ylabel("Entfernung in km")
    ax.set_ylim(0, max(df["Entfernung"]) + 100)  # Etwas zusätzlicher Raum an der Spitze

    ax.legend(title="Legende", loc="upper left", frameon=True, framealpha=0.8)
    plt.tight_layout()
    plt.savefig("Spanienreise-Roadmap-aktualisiert.svg", format="svg")
    with PdfPages("Spanienreise-Roadmap-aktualisiert.pdf") as pdf:
        pdf.savefig(fig)
    plt.show()
    plt.close()


# Urlaubsdaten mit Entfernungen
data_urlaub = [
    {"Datum": "2024-06-01", "Beschreibung": "Home - La Jonquera", "Entfernung": 1244},
    {"Datum": "2024-06-02", "Beschreibung": "Guardamar del Segura - Alicante", "Entfernung": 718},
    {"Datum": "2024-06-19", "Beschreibung": "Bilbao - Umgebung", "Entfernung": 838},
    {"Datum": "2024-06-21", "Beschreibung": "Frankreich", "Entfernung": 800},
    {"Datum": "2024-06-22", "Beschreibung": "Frankreich - Belgien - Home", "Entfernung": 800},
]

visualize_meilensteine(data_urlaub)
