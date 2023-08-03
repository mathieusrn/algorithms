import pandas as pd

def load_data_from_csv(file_path):
    # Chargement des données depuis le fichier CSV
    data = pd.read_csv(file_path, delimiter=';', quotechar="'")

    # Suppretion des guillemets simples des valeurs
    data = data.applymap(lambda x: x.strip("'") if isinstance(x, str) else x)

    # Conversion des données du DataFrame en liste de tuples avec des entiers
    data_list = data.values.tolist()
    data_list = [[int(float(item)) if isinstance(item, str) and item.replace('.', '', 1).isdigit() else item for item in row] for row in data_list]

    # Afficher la variable data_list
    print(data_list)

    return data_list

# Chemin d'accès:
csv_file_path = "donnees_immo.csv"

# Appel de la fonction afin de charger les données
data_list = load_data_from_csv(csv_file_path)
