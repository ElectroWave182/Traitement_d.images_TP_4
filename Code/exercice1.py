import cv2
from numpy import *


def base2a10 (base2):

    chiffres = list (base2)
    chiffres.reverse ()
    poids = 1
    base10 = 0

    for chiffre in chiffres:
    
        base10 += int (chiffre) * poids
        poids *= 2
    
    return base10


def lireMessage (image, taille):

    largeur = image.shape [0]
    hauteur = image.shape [1]
    
    message = ""
    octet = ""
    lus = 0

    for ligne in range (hauteur):
        for colonne in range (largeur):
            pixel = image [ligne] [colonne]
            octet += str (pixel [0] % 2)
            
            lus += 1
            
            if lus % 8 == 0:
                message += chr (base2a10 (octet))
                octet = ""
            
            if lus == taille:
                return message


def decimalesPi (message):

    pi = "3."

    for mot in message.split () [1:]:
        pi += str (len (mot))
        
    return float (pi)
