import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import tkinter as tk
from tkinter import messagebox
import datetime

# Définition du noms de colonnes
column_names = ["date", "code", "tmoy"]

# Chargement des données
data = pd.read_csv('temp.csv', names=column_names, delimiter=';', header=None)

# Encodage des données
le = LabelEncoder()

# Conversion et encodage de la date
data['date'] = pd.to_datetime(data['date'], format='%d/%m/%Y').dt.dayofyear

# Encodage du code de la région
data['code'] = le.fit_transform(data['code'])

# Split des données
X = data[['date', 'code']]
y = data['tmoy']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Création du pipeline pour l'encodage one-hot et la mise à l'échelle
column_transformer = ColumnTransformer([
    ('ohe', OneHotEncoder(categories='auto'), [1]),  # code de la région se trouve à l'index 1
    ('scaler', StandardScaler(), [0])],  # date se trouve à l'index 0
    remainder='passthrough')

# Création du pipeline pour le modèle
model = Pipeline(steps=[('preprocessor', column_transformer),
                        ('regressor', MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=500, random_state=42))])

# Entraînement du modèle
model.fit(X_train, y_train)

# Prédiction de la température
def predict_temp(date, region_code):
    day_of_year = pd.to_datetime(date, format='%Y-%m-%d').dayofyear
    region_code_transformed = le.transform([region_code])
    prediction = model.predict([[day_of_year, region_code_transformed[0]]])
    return prediction[0]


# Charger le fichier csv
df = pd.read_csv('code_insee_regions.csv', sep=';', header=None)

# Supprimer les doublons
df_unique = df.drop_duplicates()

# Créer un dictionnaire où les codes de région sont les clés et les noms de région sont les valeurs
region_dict = pd.Series(df_unique[1].values,index=df_unique[0]).to_dict()

# Transformer le dictionnaire en une liste de tuples et diviser cette liste en 5 parties
regions_list = list(region_dict.items())
regions_split = [regions_list[i::5] for i in range(5)]

# Interface graphique
def retrieve_input():
    date = entry1.get()
    region_code = entry2.get()
    temp = predict_temp(date, region_code)
    result_label.config(text=f"La température prévue pour le {date} dans la région {region_code} est de {temp:.2f} degrés.")

root = tk.Tk()
root.geometry("500x480") # j'ai augmenté la hauteur pour faire de la place pour le nouveau label
root.title("Prédiction de température")

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0)
tk.Label(root, text="Code de la région :").grid(row=1)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Créer 5 labels pour afficher les régions
for i, regions in enumerate(regions_split):
    regions_label = tk.Label(root, text=str(regions))
    regions_label.grid(row=5+i, column=0, columnspan=2)

tk.Button(root, text='Prédire', command=retrieve_input).grid(row=3, column=1, pady=4)

root.mainloop()