import pandas as pd

# Charger le fichier csv
df = pd.read_csv('code_insee_regions.csv', sep=';', header=None)

# Supprimer les doublons
df_unique = df.drop_duplicates()

# Créer un dictionnaire où les codes de région sont les clés et les noms de région sont les valeurs
region_dict = pd.Series(df_unique[1].values,index=df_unique[0]).to_dict()

# Afficher le dictionnaire
print("Dictionnaire des régions :", region_dict)
