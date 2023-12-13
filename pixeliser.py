import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def pixeliser_image(canvas, chiffre_entry):
    """
    Permet de pixeliser une image 
    Ouvre image_temporaire.png
    Transforme l'image en tableau a trois dimention
    Divise l'image en block de pixels et fait la moyenne de leux couleurs
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
    image_np = image_np.astype(np.float64)
    image_sortie = image_sortie.astype(np.float64)
    for ligne in range(0, nb_lignes, valeur):
        for col in range(0, nb_colonnes, valeur):
            for i in range(3):
                a = image_np[ligne:ligne+valeur, col:col+valeur, i]
                b = np.mean(a) #Fait la moyenne des couleurs des pixels compris dans le block à pixeliser
                image_sortie[ligne:ligne+valeur, col:col+valeur, i] = b
            if np.any(image_sortie[ligne:ligne+valeur, col:col+valeur, 3] > 0): 
                #Met l'oppacité de tous les pixels compris dans la block a pixeliser à 255
                image_sortie[ligne:ligne+valeur, col:col+valeur, 3] = 255 
    # Sauvegarde les images pour pouvoir les afficher
    image_sortie = image_sortie.astype(np.uint8)
    Image.fromarray(image_sortie).save("image_temporaire.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file="image_temporaire.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def boite_pixeliser(image_label):
    """
    Création une nouvelle page tkinter
    Champ créé pour ecrire un nombre 
    Bouton Valider qui appel la fonction pixeliser_image
    """ 
    # Création d'une nouvelle fenetre tkinter
    fenetre_pixeliser = tk.Tk()
    fenetre_pixeliser.title("Block de pixels")
    # Créé une zone pour ecrire un nombre
    cmd = fenetre_pixeliser.register(lambda s: not s or s.isdigit())
    chiffre_entry = tk.Entry(fenetre_pixeliser, validatecommand=(cmd, "%P"))
    chiffre_entry.pack()
    ajouter_bouton = tk.Button(fenetre_pixeliser, text="Valider", command=lambda:pixeliser_image(image_label, chiffre_entry))
    ajouter_bouton.pack()
    fenetre_pixeliser.mainloop() 