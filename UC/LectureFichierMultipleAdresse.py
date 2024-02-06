import numpy as np
import pandas as pd
import sys


# Check l'argument (chemin fichier + adresse voulu)(sinon mettre ==2)
def CheckArgument(Argument):
    if len(Argument) == 3:
        CheminFichier = sys.argv[1]
        
        print("On prend le fichier en argument")

    else:
        print("Aucun fichier en argument, On prend le fichier test")
        CheminFichier = "./ExempleDeValeurs.csv"

    data = pd.read_csv(CheminFichier)
    return data


def CreationVecteur(Liste):
    ValeurVecteur = [-1,-1]
    for Valeur in Liste:
        #print("valeur", Valeur)
        if len(Valeur) != 0:
            ValeurVecteur.append(np.mean(Valeur))
        else:
            ValeurVecteur.append(100)
    return ValeurVecteur


#Declaration variable
Dataframe = CheckArgument(sys.argv)

ColonneNumeroCapteur = Dataframe['NumeroCapteur']
ColonneHeure = Dataframe['Heure']
ColonnePuissance = Dataframe['Puissance']
ColonneAdresse = Dataframe['Adresse']

Test = []

print(len(ColonneAdresse.unique())) # == 2
for NombreDadresse in range(len(ColonneAdresse.unique())):
    adresse = ColonneAdresse[NombreDadresse]

    Capteur1 = []
    Capteur2 = []
    Capteur3 = []
    Capteur4 = []
    Capteur5 = []
    ListeValeur = []

    i = -1
    for NumeroCapteur in ColonneNumeroCapteur:
        i=i+1
        if NumeroCapteur == 1 and adresse == ColonneAdresse[i]:
            Capteur1.append(ColonnePuissance[i])
        if NumeroCapteur == 2 and adresse == ColonneAdresse[i]:
            Capteur2.append(ColonnePuissance[i])
        if NumeroCapteur == 3 and adresse == ColonneAdresse[i]:
            Capteur3.append(ColonnePuissance[i])
        if NumeroCapteur == 4 and adresse == ColonneAdresse[i]:
            Capteur4.append(ColonnePuissance[i])
        if NumeroCapteur == 5 and adresse == ColonneAdresse[i]:
            Capteur5.append(ColonnePuissance[i])
    
    ListeValeur = [Capteur1, Capteur2, Capteur3, Capteur4, Capteur5]
    #print("ListeValeur", ListeValeur)

    Test.append(ListeValeur)
    #print(ListeValeur)



Vecteur1 = CreationVecteur(Test[0])
Vecteur2 = CreationVecteur(Test[1])

print(Vecteur1)
print(Vecteur2)
"""
print("test")
print(Test[0])

print(Test[1])
#print(Vecteur)"""