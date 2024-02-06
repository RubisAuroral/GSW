import numpy as np
import pandas as pd
import sys

from MoindreCarre import *

# Lancer le programme avec
# python3 LectureFichierAdresseSeule.py ../ExempleDeValeurs.csv 00:b5:d0:ed:54:3B
# python3 LectureFichierAdresseSeule.py ../Donnees.csv 00:b5:d0:ed:54:3B
# python3 LectureFichierAdresseSeule.py ExempleDeValeurs.csv 00:b5:d0:ed:54:3B

# 00:b5:d0:ed:54:3b

# Check l'argument (chemin fichier + adresse voulu)(sinon mettre ==2)
def CheckArgument(Argument):   

    if len(Argument) == 3:
        CheminFichier = sys.argv[1]
        Adresse = sys.argv[2]
        
        #print("On prend le fichier en argument")

    else:
        #print("Aucun fichier en argument, On prend le fichier test")
        CheminFichier = "ExempleDeValeurs.csv"
        Adresse = "22:a6:6b:a5:a8:f2"

    data = pd.read_csv(CheminFichier)
    return data, Adresse


def CreationVecteur(Liste):
    ValeurVecteur = [-1,-1]
    for Valeur in Liste:
        if len(Valeur) != 0:
            ValeurVecteur.append(np.mean(Valeur))
        else:
            ValeurVecteur.append(100)
    return ValeurVecteur




#Declaration variable
Dataframe, Adresse = CheckArgument(sys.argv)

ColonneNumeroCapteur = Dataframe['NumeroCapteur']
ColonneHeure = Dataframe['Heure']
ColonnePuissance = Dataframe['Puissance']
ColonneAdresse = Dataframe['Adresse']

Capteur1 = []
Capteur2 = []
Capteur3 = []
Capteur4 = []
Capteur5 = []
i = -1


for Sample in ColonneNumeroCapteur:
    i=i+1
    if Sample == 1 and ColonneAdresse[i] == Adresse:
        Capteur1.append(ColonnePuissance[i])
    if Sample == 2 and ColonneAdresse[i] == Adresse:
        Capteur2.append(ColonnePuissance[i])
    if Sample == 3 and ColonneAdresse[i] == Adresse:
        Capteur3.append(ColonnePuissance[i])
    if Sample == 4 and ColonneAdresse[i] == Adresse:
        Capteur4.append(ColonnePuissance[i])
    if Sample == 5 and ColonneAdresse[i] == Adresse:
        Capteur5.append(ColonnePuissance[i])

ListeValeur = [Capteur1, Capteur2, Capteur3, Capteur4, Capteur5]
Vecteur = CreationVecteur(ListeValeur)

Resultat = MoindreCarre(Vecteur)

