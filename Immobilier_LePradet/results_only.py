import pickle
import tkinter as tk
from tkinter import messagebox

# Chargement du modèle entrainé à partir du fichier
with open('modele_entreaine.pkl', 'rb') as fichier:
    model = pickle.load(fichier)

# Définition de la fonction destinée aux prédictions
def faire_prediction():
    # Récupération des valeurs saisies par l'utilisateur
    valeurs_saisies = [int(entry_type.get()), int(entry_surface.get()), int(entry_nb_pieces.get()),
                       int(entry_etage.get()), int(entry_climatisation.get()), int(entry_balcon.get()), int(entry_terrasse.get())]

    # Vérification de l'intégrité des données saisies
    if None in valeurs_saisies:
        messagebox.showwarning("Erreur", "Veuillez remplir toutes les valeurs.")
    else:
        # Réaliser des prédictions à partir des nouvelles données
        nouvelles_donnees = [valeurs_saisies]
        resultat_prediction = model.predict(nouvelles_donnees)

        # Afficher le résultat des prédictions avec les milliers séparés par un point et le texte souhaité
        resultat_formate = "{:,.0f}".format(resultat_prediction[0][0]).replace(",", ".")
        resultat_label.config(text="Le prix estimé est de: " + resultat_formate + " euros")

# Création de l'interface graphique
fenetre = tk.Tk()
fenetre.title("Interface de prédiction")
fenetre.geometry("300x380")
fenetre.resizable(False, False)

# Labels et inputs qui permettent à l'utilisateur de saisir les nouvelles données
label_type = tk.Label(fenetre, text="Type (Appartement=0, Maison=1):")
label_type.pack()
entry_type = tk.Entry(fenetre)
entry_type.pack()

label_surface = tk.Label(fenetre, text="Surface:")
label_surface.pack()
entry_surface = tk.Entry(fenetre)
entry_surface.pack()

label_nb_pieces = tk.Label(fenetre, text="Nb de pièces:")
label_nb_pieces.pack()
entry_nb_pieces = tk.Entry(fenetre)
entry_nb_pieces.pack()

label_etage = tk.Label(fenetre, text="Étage du bien:")
label_etage.pack()
entry_etage = tk.Entry(fenetre)
entry_etage.pack()

label_climatisation = tk.Label(fenetre, text="Climatisation (Non=0, Oui=1):")
label_climatisation.pack()
entry_climatisation = tk.Entry(fenetre)
entry_climatisation.pack()

label_balcon = tk.Label(fenetre, text="Balcon (Non=0, Oui=1):")
label_balcon.pack()
entry_balcon = tk.Entry(fenetre)
entry_balcon.pack()

label_terrasse = tk.Label(fenetre, text="Terrasse (Non=0, Oui=1):")
label_terrasse.pack()
entry_terrasse = tk.Entry(fenetre)
entry_terrasse.pack()

# Bouton dédié au lancement de la prédiction
bouton = tk.Button(fenetre, text="Go!", command=faire_prediction)
bouton.pack()

# Case spécifique dedié à l'affichage du résultat de la prédiction du prix
resultat_label = tk.Label(fenetre, text="", font=("Arial", 12))
resultat_label.pack()

# Boucle principale de l'interface graphique
fenetre.mainloop()
