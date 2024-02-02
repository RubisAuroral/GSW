
import math
import numpy as np

# Localisation
# Telephone
P1 = [0, 0, -23, -76.67, -98.90, -76.67, -61.18]
P2 = [100, 0, -76.67, -23, -76.67, -98.90, -61.18]
P3 = [100, 100, -98.90, -76.67, -23, -76.67, -61.18]
P4 = [0, 100, -76.67, -98.90, -76.67, -23, -61.18]


P5 = [25, 25, -48.46, -67.93, -81.22, -67.93, -48.46]
P6 = [25, 75, -67.93, -48.46, -67.93, -81.22, -48.46]
P7 = [75, 75, -81.22, -67.93, -48.46, -67.93, -48.46]
P8 = [75, 25, -67.93, -81.22, -67.93, -48.46, -48.46]

P9 = [50, 50, -61.18, -61.18, -61.18, -61.18, -23]

ListePosition = [P1,P2,P3,P4,P5,P6,P7,P8,P9]

# Capteur
# Valeur en %, faut remettre sur 8*8 metres
C1 = [0, 0]
C2 = [100, 0]
C3 = [100, 100]
C4 = [0, 100]
C5 = [50, 50]

print("A", P1)

test = [-1, -1, -81.89, -75.27, -48.55, -60.26, -48.55]
#test = [-1, -1, -78.95, -82.71, -55.26, -47.62, -47.62]

print("Test", test)


def CalculVecteur(Capteur, Actuelle):


    Tempo = 0
    for i in np.arange(np.shape(Capteur)[0]-2):

        #print(Capteur[i+2])
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


