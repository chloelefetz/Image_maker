from PIL import Image, ImageTk
import numpy as np
import tkinter as tk

def rogner_image(canvas):
    """
    Permet de rogner une image 
    Ouvre image_temporaire.png
    Transforme l'image en tableau a trois dimention
    #// à compléter 
    Sauvegarde le resultat dans image_temporaire.png
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open("image_temporaire.png")
    image_np = np.asarray(image_entrée)
    # Créé l'image de sortie (éclaircie) sous forme de tableau numpy
    image_sortie = image_np[160:218,120:185]

    # Sauvegarde les images pour pouvoir les afficher
    Image.fromarray(image_sortie).save("image_temporaire.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file="image_temporaire.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)