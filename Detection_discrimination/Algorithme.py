from numpy import *
from keras import *
import tkinter as tk

model = Sequential()
model.add(layers.Dense(units=16,input_shape=[4]))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=1))


# Jeu de données formaté sous forme de liste avec pour indices:
    # 1er indice: Age;
    # 2ème indice: Durée de la formation en années;
    # 3ème indice: Expérience professionnelle en années;
    # 4ème indice: Sexe (0=homme/1=femme);
    # 5ème indice: Salaire mensuel en euros.
    
data = [
    [18, 2, 0, 0, 2100],
    [32, 4, 10, 0, 3400],
    [44, 2, 20, 0, 3200],
    [60, 6, 34, 0, 5500],
    [20, 2, 2, 1, 2300],
    [24, 4, 0, 1, 2700],
    [44, 5, 21, 1, 3200],
    [19, 3, 0, 0, 2150],
    [30, 4, 8, 0, 3100],
    [45, 2, 21, 0, 3250],
    [59, 6, 32, 0, 5350],
    [22, 2, 4, 1, 2400],
    [26, 3, 0, 1, 2550],
    [42, 5, 18, 1, 3000],
    [21, 2, 2, 0, 2300],
    [32, 4, 9, 0, 3300],
    [42, 2, 18, 0, 3150],
    [60, 6, 33, 0, 5400],
    [21, 2, 3, 1, 2370],
    [25, 4, 2, 1, 2700],
    [43, 5, 19, 1, 3100],
]


# Création de tableau à partir des données
data_array = array(data)
entree = data_array[:, 0:4]
sortie = data_array[:, 4]

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x=entree, y=sortie, epochs=5000, verbose=0) 



# Création de l'interface graphique
window = tk.Tk()
window.geometry("600x400")

age = tk.Entry(window)
formation = tk.Entry(window)
experience = tk.Entry(window)
sexe = tk.Entry(window)

tk.Label(window, text="Âge").grid(row=0)
tk.Label(window, text="Durée de la formation (années)").grid(row=1)
tk.Label(window, text="Expérience (années)").grid(row=2)
tk.Label(window, text="Sexe (homme=0, femme=1)").grid(row=3)

age.grid(row=0, column=1)
formation.grid(row=1, column=1)
experience.grid(row=2, column=1)
sexe.grid(row=3, column=1)

result = tk.Text(window, height=8, width=70)
result.grid(row=6, column=0, columnspan=2)

def prediction():
    inputs = array([[int(age.get()), int(formation.get()), int(experience.get()), int(sexe.get())]])

    homme = inputs.copy()
    homme[0, 3] = 0
    femme = inputs.copy()
    femme[0, 3] = 1

    salaire_homme = model.predict(homme)
    salaire_femme = model.predict(femme)

    salaire_homme = model.predict(homme)
    salaire_femme = model.predict(femme)

    diff_euros = abs(salaire_homme - salaire_femme)

    if inputs[0, 3] == 0:  # Si l'utilisateur est un homme
        result_text = f"Salaire prédit pour un homme : {salaire_homme[0][0]:.2f} euros\n" # Affichage du salaire à 2 décimales maximum afin de réduire la longueur du résultat
        result_text += f"Salaire prédit pour une femme : {salaire_femme[0][0]:.2f} euros\n"
    else:  # Si l'utilisateur est une Femme
        result_text = f"Salaire prédit pour une femme : {salaire_femme[0][0]:.2f} euros\n"
        result_text += f"Salaire prédit pour un homme : {salaire_homme[0][0]:.2f} euros\n"

        result_text += f"Écart constaté : {diff_euros[0][0]:.2f} euros\n"
            # Prévoir l'affichage d'un message d'alerte si un écart >= 250 euros est constaté
    if diff_euros > 250: 
        result_text += "Discrimination fondée sur le sexe suspectée."


    result.delete(1.0, tk.END)
    result.insert(tk.END, result_text)

btn = tk.Button(window, text="Prédire le salaire", command=prediction)
btn.grid(row=40, columnspan=20)


window.mainloop()
