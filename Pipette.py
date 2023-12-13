import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def pipette(x, y):
    """
    Permet de savoir les couleurs RVB d'un pixel aux coordonnées x et y
    """
    image_entrée = Image.open("image_temporaire.png")
    image_np = np.asarray(image_entrée)
    couleur = image_np[y, x, :]
    print(couleur)