import cv2
from numpy import *


def base10a2 (base10):

    base2 = ""

    while (base10 != 0):
        base2 = str (base10 % 2) + base2
        base10 //= 2
    
    reste = "0" * (8 - len (base2))
    base2 = reste + base2
    
    return base2
    
    
def encoder (message):

    code = ""
    for caractere in message:
        code += base10a2 (ord (caractere))
        
    return list (map (int, code))
    
    
def ecrireMessage (image, message):

    tatouage = image.copy ()
    largeur = image.shape [0]
    hauteur = image.shape [1]
    
    code = encoder (message)
    taille = len (code)
    compteur = 0
    
    for ligne in range (hauteur):
        for colonne in range (largeur):
            pixel = tatouage [ligne] [colonne]
            
            if compteur == taille:
                return tatouage
                
            for couleur in range (3):
                pixel [couleur] -= pixel [couleur] % 2
                pixel [couleur] += code [compteur]
                
            compteur += 1
