import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.backends.backend_pdf import PdfPages

def visualize_meilensteine(data):
    df = pd.DataFrame(data)
    df['Datum'] = pd.to_datetime(df['Datum'])

    # Farben und Größe der Visualisierung
    colors = ['red', 'green', 'blue', 'orange', 'purple']
    #fig_size = (10.0, 7.0)  # B5-Größe in Zoll
    fig_size = (11.69, 8.27)  # DIN-A4 quer -Größe in Zoll

    fig, ax = plt.subplots(figsize=fig_size)
    ax.set(title="Spanienreise - Roadmap")

    # Plotten der Meilensteine
    for index, (color, row) in enumerate(zip(colors, df.iterrows())):
        row = row[1]
        ax.scatter(row['Datum'], row['Kategorie'], color=color, s=100, label=f"{index + 1}. {row['Beschreibung']}")
        ax.text(row['Datum'], row['Kategorie'], str(index + 1), color='white', ha='center', va='center')

    heute = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    ax.axvline(heute, color='red', linestyle='--', label='Heute')

    # Setzen der X-Achsen-Ticks auf die Datumsangaben der Meilensteine plus heute
    alle_datums = sorted(df['Datum'].tolist() + [heute])
    ax.set_xticks(alle_datums)
    ax.set_xticklabels([datum.strftime("%Y-%m-%d") for datum in alle_datums], rotation=45, ha="right")

    ax.legend(title="Legende", loc='upper left')
    ax.set_ylim(0, max(df['Kategorie']) + 1)
    ax.yaxis.set_visible(False)

    plt.tight_layout()
    plt.savefig("Spanienreise-Roadmap.svg", format='svg')
    with PdfPages("Spanienreise-Roadmap.pdf") as pdf:
        pdf.savefig(fig)
    plt.show()
    plt.close()

# Beispiel-Daten für verschiedene Szenarien
# Roadmap 5 Meilensteine
data_jahr_monat = [
    {"Datum": "2024-03-10", "Beschreibung": "Home - La Jonquera (1244 km)", "Kategorie": 1},
    {"Datum": "2024-07-22", "Beschreibung": "Guardamar del Segura - Alicante (718 km)", "Kategorie": 1},
    {"Datum": "2025-03-24", "Beschreibung": "Bilbao - Umgebung (ca. 838 km)", "Kategorie": 1},
    {"Datum": "2025-04-25", "Beschreibung": "Frankreich (ca. 800 km)", "Kategorie": 1},
    {"Datum": "2025-05-26", "Beschreibung": "Frankreich - Belgien - Home (ca. 800 km)", "Kategorie": 1},
]

data_jahre = [
    {"Datum": "2024-03-20", "Beschreibung": "Home - La Jonquera (1244 km)", "Kategorie": 1},
    {"Datum": "2025-03-22", "Beschreibung": "Guardamar del Segura - Alicante (718 km)", "Kategorie": 1},
    {"Datum": "2026-03-24", "Beschreibung": "Bilbao - Umgebung (ca. 838 km)", "Kategorie": 1},
    {"Datum": "2027-03-25", "Beschreibung": "Frankreich (ca. 800 km)", "Kategorie": 1},
    {"Datum": "2028-03-26", "Beschreibung": "Frankreich - Belgien - Home (ca. 800 km)", "Kategorie": 1},
]

data_tage = [
    {"Datum": "2024-03-21", "Beschreibung": "Home - La Jonquera (1244 km)", "Kategorie": 1},
    {"Datum": "2024-03-22", "Beschreibung": "Guardamar del Segura - Alicante (718 km)", "Kategorie": 1},
    {"Datum": "2024-03-24", "Beschreibung": "Bilbao - Umgebung (ca. 838 km)", "Kategorie": 1},
    {"Datum": "2024-03-25", "Beschreibung": "Frankreich (ca. 800 km)", "Kategorie": 1},
    {"Datum": "2024-03-26", "Beschreibung": "Frankreich - Belgien - Home (ca. 800 km)", "Kategorie": 1},
]

# Urlaubsdaten
data_urlaub = [
    {"Datum": "2024-06-01", "Beschreibung": "Home - La Jonquera (1244 km)", "Kategorie": 1},
    {"Datum": "2024-06-02", "Beschreibung": "Guardamar del Segura - Alicante (718 km)", "Kategorie": 1},
    {"Datum": "2024-06-19", "Beschreibung": "Bilbao - Umgebung (ca. 838 km)", "Kategorie": 1},
    {"Datum": "2024-06-21", "Beschreibung": "Frankreich (ca. 800 km)", "Kategorie": 1},
    {"Datum": "2024-06-22", "Beschreibung": "Frankreich - Belgien - Home (ca. 800 km)", "Kategorie": 1},
]

# Wähle die passenden Daten für die Visualisierung
#visualize_meilensteine(data_jahr_monat)
#visualize_meilensteine(data_jahre)
#visualize_meilensteine(data_tage)
visualize_meilensteine(data_urlaub)
