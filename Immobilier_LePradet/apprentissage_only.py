from numpy import*
from keras import*
import tkinter as tk
from tkinter import messagebox
from numpy import array
from keras.models import Sequential
from keras.layers import Dense
import pickle

model=Sequential()
#La couche d'entrée, composée de 16 , adaptée au nombre de colonnes de la liste=7
model.add(layers.Dense(units=16,input_shape=[7]))
#Deux couches intermédiaires, composées de 64 neurones
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
#La couche de sortie, 1 seul neurone
model.add(layers.Dense(units=1))

# Données récupérées et mises sous forme de liste
data=[[0, 61, 2, 0, 0, 0, 1, 262500], [0, 50, 2, 0, 0, 0, 1, 261000], [0, 23, 1, 3, 0, 0, 0, 119000], [0, 63, 3, 0, 0, 0, 1, 250000], [0, 60, 3, 3, 0, 0, 0, 198000], [0, 65, 3, 3, 0, 1, 0, 274000], [0, 60, 3, 1, 0, 0, 0, 220000], [0, 105, 4, 0, 1, 0, 0, 970000], [0, 76, 3, 2, 0, 0, 0, 278000], [0, 82, 4, 0, 0, 0, 0, 305900], [0, 18, 1, 0, 0, 0, 0, 88000], [0, 85, 4, 0, 0, 0, 0, 456000], [0, 63, 3, 1, 0, 1, 0, 201400], [0, 62, 3, 2, 0, 1, 0, 316900], [0, 92, 4, 0, 0, 0, 0, 573000], [0, 28, 1, 0, 0, 0, 0, 98157], [0, 85, 4, 0, 0, 0, 1, 506000], [0, 86, 4, 1, 0, 1, 0, 360000], [1, 210, 7, 0, 0, 0, 1, 1470000], [1, 98, 8, 1, 0, 0, 1, 679000], [1, 118, 5, 1, 0, 0, 1, 711000], [1, 124, 5, 1, 0, 0, 1, 690000], [1, 128, 5, 1, 0, 0, 1, 646000], [1, 104, 5, 1, 0, 0, 1, 455000], [1, 90, 4, 0, 0, 0, 1, 544000], [1, 284, 9, 2, 0, 0, 1, 596000], [1, 230, 6, 1, 0, 0, 1, 2200000], [1, 69, 3, 1, 0, 0, 1, 324145], [1, 157, 4, 1, 0, 0, 1, 978000], [1, 375, 12, 1, 0, 0, 1, 1295000], [1, 182, 6, 1, 0, 0, 1, 696800], [1, 137, 6, 1, 0, 0, 1, 710600], [1, 161, 6, 1, 0, 0, 1, 550000], [1, 218, 6, 1, 0, 0, 1, 1150000], [1, 138, 5, 1, 0, 0, 1, 1095000], [1, 190, 8, 1, 0, 0, 1, 1312000], [1, 200, 9, 2, 0, 0, 1, 832000], [1, 104, 4, 1, 0, 0, 1, 455000], [1, 297, 8, 1, 0, 0, 1, 1490000], [1, 200, 9, 3, 0, 0, 1, 832000], [1, 180, 7, 1, 0, 0, 1, 895000], [1, 120, 5, 1, 0, 0, 1, 680000], [1, 137, 6, 1, 0, 0, 1, 700000], [1, 180, 5, 1, 0, 0, 1, 942000], [1, 196, 5, 1, 0, 0, 1, 825000], [1, 181, 8, 1, 0, 0, 1, 895800], [1, 211, 5, 1, 0, 0, 1, 885400], [1, 160, 5, 1, 0, 0, 1, 1070000], [1, 150, 6, 1, 0, 0, 1, 1095000]]

data_array=array(data)
entree=data_array[0:50,0:7]
sortie=data_array[0:50,7]  

#Compilation du réseau neuronal
model.compile(loss='mean_squared_error',optimizer='adam')
#Entraînement du réseau avec 10.000 passages
model.fit(x=entree,y=sortie,epochs=10000)
with open('modele_entreaine.pkl', 'wb') as fichier:
    pickle.dump(model, fichier)