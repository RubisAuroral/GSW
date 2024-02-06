
import math
import numpy as np

# matrice resultat
Grille = np.zeros((100,100))
print(Grille)





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


# Capteur
# Valeur en %, faut remettre sur 8*8 metres
C1 = [0, 0]
C2 = [100, 0]
C3 = [100, 100]
C4 = [0, 100]
C5 = [50, 50]

print("A", P1)

#test = [-1, -1, -81.89, -75.27, -48.55, -60.26, -48.55]
test = [-1, -1, -78.95, -82.71, -55.26, -47.62, -47.62]

print("Test", test)



"""
Ce qu'on veut
C'est avoir un vecteur random de format
[x,y, C1,C2,C3,C4,C5]

x,y, 50,80,45,20,90

On regarde les points les plus proches
Comment derterminer le spoints les plus proches

Ensuite, on les relie /prend la moitié pour augmenter la precision
On compare ensuite ces nouveaux resultats et on continue


prendre les deux maximums parmi les axes

"""

# determination des valeurs

"""
def Correspondance(ListePrincipale, Valeur1, Valeur2, Valeur3):
    NewListe = [-1,-1,-1]
    indice = 0
    for value in ListePrincipale:
        
        if value == Valeur1:
            NewListe[0]=indice

        indice=indice+1

    #print("Liste",NewListe)
    return NewListe
"""

def Correspondance(ListePrincipale, Valeur1):
    NewListe = -1
    indice = 0
    for value in ListePrincipale:
        
        if value == Valeur1:
            NewListe=indice

        indice=indice+1

    #print("Liste",NewListe)
    return NewListe

"""
Faire un tableau, le trier, et prendre la premiere colonne 
    == permet de recup la 2eme et 3eme colonne aussi
"""
def Comparer(Vecteur, Indice):
    Capteur1 = Vecteur[Indice]
    #print("C", Capteur1)

    CA = abs(P1[Indice] - Capteur1)
    CB = abs(P2[Indice] - Capteur1)
    CC = abs(P3[Indice] - Capteur1)
    CD = abs(P4[Indice] - Capteur1)
    CE = abs(P5[Indice] - Capteur1)
    CF = abs(P6[Indice] - Capteur1)
    CG = abs(P7[Indice] - Capteur1)
    CH = abs(P8[Indice] - Capteur1)
    CI = abs(P9[Indice] - Capteur1)

    ListeCapteur=[CA,CB,CC,CD,CE,CF,CG,CH,CI]

    #print("valeur A", CA)
    #print("valeur B", CB)
    #print("valeur C", CC)
    #print("valeur D", CD)
    #print("valeur E", CE)
    #print("valeur F", CF)
    #print("valeur G", CG)
    #print("valeur H", CH)
    #print("valeur I", CI)

    trier = sorted(ListeCapteur)
    #print(trier)
   
    ListeCapteur = Correspondance(ListeCapteur, trier[0])
    #ListeCapteur = Correspondance(ListeCapteur, trier[0], trier[1], trier[2])

    return ListeCapteur



def AssocieResultat(ValeurIndice):

    if ValeurIndice == 0:
        return P1
    elif ValeurIndice == 1:
        return P2
    elif ValeurIndice == 2:
        return P3
    elif ValeurIndice == 3:
        return P4
    elif ValeurIndice == 4:
        return P5
    elif ValeurIndice == 5:
        return P6
    elif ValeurIndice == 6:
        return P7
    elif ValeurIndice == 7:
        return P8
    elif ValeurIndice == 8:
        return P9
    else:
        print("erreur", ValeurIndice )
        return -1


    

print("Capteur 0 =",Comparer(test, 2))
print("Capteur 1 =",Comparer(test, 3))
print("Capteur 2 =",Comparer(test, 4))
print("Capteur 3 =",Comparer(test, 5))
print("Capteur 4 =",Comparer(test, 6))

Resultat1 = AssocieResultat(Comparer(test, 2))
Resultat2 = AssocieResultat(Comparer(test, 3))
Resultat3 = AssocieResultat(Comparer(test, 4))
Resultat4 = AssocieResultat(Comparer(test, 5))
Resultat5 = AssocieResultat(Comparer(test, 6))

print(Resultat1[0:2])
print(Resultat2[0:2])
print(Resultat3[0:2])
print(Resultat4[0:2])
print(Resultat5[0:2])


distance1X = (Resultat1[0]-C1[0])**2
distance1Y = (Resultat1[1]-C1[1])**2
Resultat1XY = math.sqrt(distance1X+distance1Y)
print("distance1", Resultat1XY)

distance2X = (Resultat2[0]-C2[0])**2
distance2Y = (Resultat2[1]-C2[1])**2
Resultat2XY = math.sqrt(distance2X+distance2Y)
print("distance2", math.sqrt(distance2X+distance2Y))

distance3X = (Resultat3[0]-C3[0])**2
distance3Y = (Resultat3[1]-C3[1])**2
Resultat3XY = math.sqrt(distance3X+distance3Y)
print("distance3", math.sqrt(distance3X+distance3Y))

distance4X = (Resultat4[0]-C4[0])**2
distance4Y = (Resultat4[1]-C4[1])**2
Resultat4XY = math.sqrt(distance4X+distance4Y)
print("distance4", math.sqrt(distance4X+distance4Y))

distance5X = (Resultat5[0]-C5[0])**2
distance5Y = (Resultat5[1]-C5[1])**2
Resultat5XY = math.sqrt(distance5X+distance5Y)
print("distance5", math.sqrt(distance5X+distance5Y))






"""
A plus ou moins 20 de la distance == je fais +1

"""

def RemplissageMatrice(Grille, DistanceMax, Capteur):
    print(Capteur[0], Capteur[1])
    for i in np.arange(np.shape(Grille)[0]):
        for j in np.arange(np.shape(Grille)[1]):
            distanceTempo = (((i-Capteur[0])**2 + (j-Capteur[1])**2)**0.5)
            

            if i == 0 and j == 0: 
                print("tempo", distanceTempo, "max", DistanceMax)
            

            if distanceTempo <= DistanceMax+8 and distanceTempo >= DistanceMax-8:
                Grille[i][j]=Grille[i][j]+1

    

RemplissageMatrice(Grille, Resultat1XY, C1)
RemplissageMatrice(Grille, Resultat2XY, C2)
RemplissageMatrice(Grille, Resultat3XY, C3)
RemplissageMatrice(Grille, Resultat4XY, C4)
RemplissageMatrice(Grille, Resultat5XY, C5)



print(Grille)
np.savetxt("MatriceDiagonal2.txt", Grille, fmt='%d', delimiter='\t')

"""
# Position a determiner avec nos valeur juste avant
X=-10
Y=-10

test[0]=X
test[1]=Y

print("vecteur =", test, "Position =", test[0:2])
"""