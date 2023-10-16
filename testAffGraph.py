import pandas as pd
import matplotlib.pyplot as plt

# Chemin vers votre fichier CSV
file_path = "data/testCSV100MHz.csv"

# 1. Lecture du fichier CSV
df = pd.read_csv(file_path, sep=';', header=None, encoding='utf-8')

# 2. Trouver l'index où commencent les données du spectre
mask = (df.iloc[:, 0] == "Values") & (df.iloc[:, 1] == "501")
if mask.sum() == 0:
    print("Erreur: La chaîne 'Values' suivie de '501' n'a pas été trouvée dans le CSV.")
    exit()
spectrum_data_start_index = df.index[mask][0] + 1

# 3. Extraire les données du spectre
spectrum_data = df.iloc[spectrum_data_start_index:].copy().reset_index(drop=True)

# Les données du spectre sont actuellement stockées en tant que chaînes de caractères.
# Convertir les colonnes en types numériques appropriés.
spectrum_data[0] = spectrum_data[0].astype(float)  # Fréquences
spectrum_data[1] = spectrum_data[1].str.replace(',', '.').astype(float)  # Valeurs de la première colonne de données
spectrum_data[2] = spectrum_data[2].str.replace(',', '.').astype(float)  # Valeurs de la deuxième colonne de données

# 4. Visualiser les données
plt.figure(figsize=(12, 6))

# Tracer les deux colonnes de données
plt.plot(spectrum_data[0], spectrum_data[1], label="Colonne 1")
plt.plot(spectrum_data[0], spectrum_data[2], label="Colonne 2", linestyle='--')

plt.xlabel("Fréquences")
plt.ylabel("Valeurs")
plt.title("Données du spectre")
plt.legend()
plt.grid(True)

plt.show()