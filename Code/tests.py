import cv2
from matplotlib import pyplot
from pathlib import Path

from exercice1 import *
from exercice2 import *


def main ():

    cheminImages = str (Path (__file__).resolve ().parent) + "/images/"
    stego = cv2.imread (cheminImages + "01_stego.png")


    # Exercice 1

    message = lireMessage (stego, 1176)
    pi = decimalesPi (message)

    print (message)
    print (pi)
    
    
    # Exercice 2
    
    message = "La librairie OpenCV n'est pas claire."
    tatouage = ecrireMessage (stego, message)
    print (lireMessage (tatouage, 296))
    
    pyplot.imshow (cv2.cvtColor (tatouage, cv2.COLOR_BGR2RGB))
    pyplot.title ("Exercice 2 : tatouage")
    pyplot.show ()


main ()