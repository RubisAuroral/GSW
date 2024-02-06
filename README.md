# Géolocalisation de smartphone par wifi --- Projet thématique M2

BOULMONT Clément
BRASSEUR Corentin
COURTIAL Azad
MENET Alan

# Installation

## Installer les raspberry :

- Vous pouvez utiliser https://www.raspberrypi.com/software/ (Raspberry pi imager) pour installer votre système d'exploitation linux préféré. On recommande quand même raspberry pi os qui fait très bien le travail 

- Installez aircrack-ng : sudo apt install aircrack-ng
- Si non installé, installez tcpdump : sudo apt install tcpdump
- Si non installé, installez netcat : sudo apt install netcat -> par défaut, netcat s'utilise avec nc

Votre raspberry devrait être prête à utilisation

## Installer l'unité centrale : 

Il peut s'agir d'un pc ou d'une raspberry, comme votre bon vouloir. Les installations sont les mêmes que sur la raspberry
De plus, il devra avoir les éléments suivants :
- python
- pip install pandas
- pip install numpy
- pip install pyarrow

# Mise en place :

- Vous devez avoir :
  - Des dongle wifi -> En effet les interfaces wifi des raspberry pi 4 ne possèdent pas de mode moniteur, primordial à ce projet
  - Un appareil utilisé pour l'etalonnage, dont vous connaissez l'adresse MAC (ifconfig)

- Executez sur toutes les raspberry, ainsi que l'unité centrale : 
  - sudo airmon-ng start wlan1
  - Si votre unité centrale n'est pas une raspberry, remplacez wlan1 par la bonne interface (sudo airmon-ng affiche toutes les interfaces)
ATTENTION, vous n'aurez plus internet sur l'interface en question

Vous pouvez maintenant utiliser les différents code. Bonne chance & bon courage
