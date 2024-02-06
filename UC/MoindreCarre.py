
import math
import numpy as np
import pandas as pd

def CalculVecteur(Capteur, Actuelle):
    Tempo = 0
    for i in np.arange(np.shape(Capteur)[0]-2):
        if (Actuelle[i+2]) != 100:
            Tempo = Tempo + (Capteur[i+2]-Actuelle[i+2])**2
    Resultat = math.sqrt(Tempo)

    return Resultat

def ChercherPositionListe(ListeValeur, Valeur):
    i = 0
    for i in np.arange(np.shape(ListeValeur)[0]):
        if ListeValeur[i] < Valeur:
            i = i+1
        else:
            return i
    return i


def ComparaisonVecteur(ListePos, PositionActuelle):
    NombreElement = np.shape(ListePos)[0]
    ListeMeilleurResultat = []
    ListeMeilleurIndice = []

    for i in np.arange(NombreElement):
        Resultat = CalculVecteur(ListePos[i], PositionActuelle)
        Indice = ChercherPositionListe(ListeMeilleurResultat, Resultat)

        ListeMeilleurResultat.insert(Indice, Resultat)  
        ListeMeilleurIndice.insert(Indice, i)    
        
    return ListeMeilleurResultat, ListeMeilleurIndice


def MoindreCarre(Vecteur):
        
    # python .\MoindreCarre.py [Vecteur]
    CheminEtalonnage = "Etalonnage.csv"
    data = pd.read_csv(CheminEtalonnage)

    def RecupEtalon(Colonne):
        PositionEtalon = []
        for Nombre in Colonne:
            PositionEtalon.append(Nombre)
        #print(PositionEtalon)
        return PositionEtalon


    # Position D'etalonnage
    P1 = RecupEtalon(data['Position1'])
    P2 = RecupEtalon(data['Position2'])
    P3 = RecupEtalon(data['Position3'])
    P4 = RecupEtalon(data['Position4'])

    P5 = RecupEtalon(data['Position5'])
    P6 = RecupEtalon(data['Position6'])
    P7 = RecupEtalon(data['Position7'])
    P8 = RecupEtalon(data['Position8'])

    P9 = RecupEtalon(data['Position9'])

    ListePosition = [P1,P2,P3,P4,P5,P6,P7,P8,P9]

    # Position des capteurs
    # Valeur en % de la distance maximal de la salle
    C1 = [0, 0]
    C2 = [100, 0]
    C3 = [100, 100]
    C4 = [0, 100]
    C5 = [50, 50]

    MaListeValeur, MaListeIndice = ComparaisonVecteur(ListePosition,Vecteur)
    print(MaListeValeur)
    print(MaListeIndice)

    print("Meilleur position etalonnage", MaListeIndice[0]+1)
    print("Position correspondante", ListePosition[MaListeIndice[0]][0:2])


    return MaListeIndice[0]+1
