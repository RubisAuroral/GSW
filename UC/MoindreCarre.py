
import math
import numpy as np
import pandas as pd
import sys


CheminEtalonnage = "./Etalonnage.csv"
data = pd.read_csv(CheminEtalonnage)

def RecupEtalon(Colonne):
    PositionEtalon = []
    for Nombre in Colonne:
        PositionEtalon.append(Nombre)
    print(PositionEtalon)
    return PositionEtalon


# Faut juste mettre a la main les differentes positons 
# s'il y a plus que 9 == Ajouter P10 / P11 etc
P1 = RecupEtalon(data['Position1'])
P2 = RecupEtalon(data['Position2'])
P3 = RecupEtalon(data['Position3'])
P4 = RecupEtalon(data['Position4'])

P5 = RecupEtalon(data['Position5'])
P6 = RecupEtalon(data['Position6'])
P7 = RecupEtalon(data['Position7'])
P8 = RecupEtalon(data['Position8'])

P9 = RecupEtalon(data['Position9'])

# Localisation
# Telephone
"""P1 = [0, 0, -23, -76.67, -98.90, -76.67, -61.18]
P2 = [100, 0, -76.67, -23, -76.67, -98.90, -61.18]
P3 = [100, 100, -98.90, -76.67, -23, -76.67, -61.18]
P4 = [0, 100, -76.67, -98.90, -76.67, -23, -61.18]


P5 = [25, 25, -48.46, -67.93, -81.22, -67.93, -48.46]
P6 = [25, 75, -67.93, -48.46, -67.93, -81.22, -48.46]
P7 = [75, 75, -81.22, -67.93, -48.46, -67.93, -48.46]
P8 = [75, 25, -67.93, -81.22, -67.93, -48.46, -48.46]

P9 = [50, 50, -61.18, -61.18, -61.18, -61.18, -23]"""

ListePosition = [P1,P2,P3,P4,P5,P6,P7,P8,P9]

# Capteur
# Valeur en %, faut remettre sur 8*8 metres
C1 = [0, 0]
C2 = [100, 0]
C3 = [100, 100]
C4 = [0, 100]
C5 = [50, 50]

print("A", P1)

# Si on recoit pas de signal == on met valeur a 100
#test = [-1, -1, -81.89, 100, -48.55, -60.26, -48.55]
#test = [-1, -1, -78.95, -82.71, -55.26, -47.62, -47.62]
if len(sys.argv) == 2:
    test = sys.argv[1]
else:
    test = [-1, -1, -81.89, 100, -48.55, -60.26, -48.55]


print("Test", test)


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


MaListeValeur, MaListeIndice = ComparaisonVecteur(ListePosition,test)
print(MaListeValeur)
print(MaListeIndice)

print("Meilleur etalonnage", MaListeIndice[0]+1)
print("Position", ListePosition[MaListeIndice[0]][0:2])
