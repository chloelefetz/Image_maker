from tkinter import * 
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def luminosite_image(canvas, chiffre_entry):
    """
    Permet d'eclaircir une image 
    Ouvre image_temporaire.png
    Transforme l'image en tableau a trois dimention
    Change la valeur des pixels de l'image -> eclaircissement
    Sauvegarde le resultat dans image_temporaire.png
    """
    global photo
    # Recupère le chiffre entré précedement
    valeur = chiffre_entry.get()
    valeur = int(valeur)
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open("image_temporaire.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape 
    # Créé l'image de sortie sous forme de tableau numpy 
    image_sortie = np.copy(image_np)
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            for i in range(3):
                image_sortie[ligne,col,i] = max(0, min(image_sortie[ligne,col,i]+valeur,255))
    # Sauvegarde les images pour pouvoir les afficher
    Image.fromarray(image_sortie).save("image_temporaire.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file="image_temporaire.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# def entree_valide(valeur) -> bool:
#     """
#     Verifie si la valeur est composée de chiffres
#     Elle renvoie True si elle est composée que de chiffres, autrement elle renvoie False 
#     """
#     if valeur.isdigit():
#         return True
#     else :
#         return False 

def boite_luminosite(canvas):
    """
    Création une nouvelle page tkinter
    Champ créé pour ecrire un nombre 
    Bouton Valider qui appel la fonction luminosite_image
    """ 
    # Création d'une nouvelle fenetre tkinter
    fenetre_luminosité = tk.Tk()
    fenetre_luminosité.title("Modifier la luminosité")
    # Créé une zone pour ecrire un nombre
    cmd = fenetre_luminosité.register(lambda s: not s or s.isdigit())
    chiffre_entry = tk.Entry(fenetre_luminosité, validatecommand=(cmd, "%P"))
    chiffre_entry.pack()
    ajouter_bouton = tk.Button(fenetre_luminosité, text="Valider", command=lambda:luminosite_image(canvas, chiffre_entry))
    ajouter_bouton.pack()
    fenetre_luminosité.mainloop()





