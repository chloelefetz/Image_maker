import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def pipette(x, y, d):
    """
    Permet de savoir les couleurs RVB d'un pixel aux coordonnées x et y
    """
    image_entrée = Image.open("image_temporaire_{d - 1}.png")
    image_np = np.asarray(image_entrée)
    couleur = image_np[y, x, :]
    r, v, b, a = couleur
    nouveau_texte = "\nCouleur selectionnée\nR : " + str(r) + "\nV : " + str(v) + "\nB : " + str(b) + "\nA : " + str(a)
    text_pipette.config(text=nouveau_texte)
