import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import os

def redimentionner_image(canvas, vertical_entry, horizontal_entry, image_entrée):
    """
    Permet de redimentionner une image 
    Ouvre image_temporaire.png
    Transforme l'image en tableau a trois dimention
    Change le nombre de pixels de l'image -> agrandissement ou retrecissement
    Sauvegarde le resultat dans image_temporaire.png
    """
    global photo
    # Recupère le chiffre entré précedement
    valeur_vertical = int(vertical_entry.get())
    valeur_horizontal = int(horizontal_entry.get())
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_np = np.asarray(image_entrée)  
    nb_lignes, nb_colonnes, _ = image_np.shape 
    # Créé l'image de sortie sous forme de tableau numpy 
    image_sortie = np.copy(image_np)
    image_np = image_np.astype(np.float64)
    image_sortie = image_sortie.astype(np.float64)
    
    # Traitement des lignes
    modif_ligne = nb_lignes - valeur_horizontal
    if modif_ligne > 0: # On reduit le nombre de lignes
        pas_ligne = nb_lignes / modif_ligne
        for ligne in range(nb_lignes-1, -1, -1):
            if ligne // pas_ligne != (ligne-1) // pas_ligne : # Regarde si il faut traiter cette ligne ou non
                a = image_np[max(0,ligne-1),:,:]
                b = image_np[ligne,:,:]                           
                image_sortie[max(0,ligne-1),:,:] = (a + b)/2

                a = image_np[min(nb_lignes-1,ligne+1),:,:]
                b = image_np[ligne,:,:]
                image_sortie[min(nb_lignes-1, ligne+1),:,:] = (a + b)/2

                image_sortie = np.delete(image_sortie, ligne, axis=0)
                nb_lignes -= 1
    elif modif_ligne < 0: # On augmente le nombre de lignes
        pas_ligne = nb_lignes / modif_ligne
        for ligne in range(nb_lignes-1, -1, -1):
            if ligne // pas_ligne != (ligne-1) // pas_ligne : # Regarde si il faut traiter cette ligne ou non
                a = image_np[max(0,ligne-1),:,:]
                b = image_np[ligne,:,:]                           
                c = (a + b)/2

                image_sortie = np.insert(image_sortie, ligne, c, axis=0)
                nb_lignes += 1

    # Traitement des colonnes
    image_np = image_sortie
    nb_lignes, nb_colonnes, _ = image_np.shape 
    modif_colonne = nb_colonnes - valeur_vertical
    if modif_colonne > 0: # On reduit le nombre de colonnes
        pas_colonne = nb_colonnes / modif_colonne
        for col in range(nb_colonnes-1, -1, -1):
            if col // pas_colonne != (col-1) // pas_colonne : # Regarde si il faut traiter cette colonne ou non
                a = image_np[:,max(0,col-1),:]
                b = image_np[:,col,:]                         
                image_sortie[:,max(0,col-1),:] = (a + b)/2
                a = image_np[:,min(nb_colonnes-1,col+1),:]
                b = image_np[:,col,:]
                image_sortie[:,min(nb_colonnes-1, col+1),:] = (a + b)/2

                image_sortie = np.delete(image_sortie, col, axis=1)
                nb_colonnes -= 1
    elif modif_colonne < 0: # On augmente le nombre de colonnes
        pas_colonne = nb_colonnes / modif_colonne
        for col in range(nb_colonnes-1, -1, -1):
            if col // pas_colonne != (col-1) // pas_colonne : # Regarde si il faut traiter cette colonne ou non
                a = image_np[:,max(0,col-1),:]
                b = image_np[:,col,:]                           
                c = (a + b)/2

                image_sortie = np.insert(image_sortie, col, c, axis=1)
                nb_colonnes += 1

    # Sauvegarde les images pour pouvoir les afficher
    image_sortie = image_sortie.astype(np.uint8)
    Image.fromarray(image_sortie).save("image_temporaire.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file="image_temporaire.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def boite_redimentionner(canvas):
    """
    Cration une nouvelle page tkinter (fenetre_redimentionner)
    Créé un champ pour ecrire un nombre (hauteur et largeur) 
    Bouton Valider qui appel la fonction luminosite_image
    """ 
    # Création d'une nouvelle fenetre tkinter
    fenetre_redimentionner = tk.Tk()
    fenetre_redimentionner.title("Modifier les dimentions de l'image")
    # cmd = fenetre_luminosité.register(lambda s: not s or s.isdigit())
    # Regarde si le fichier "image_temporaire.png" existe
    if os.path.exists("image_temporaire.png"):
        image_entrée = Image.open("image_temporaire.png")
        largeur, hauteur = image_entrée.size # Récupère la largeur et hauteur de l'image  
    else : 
        largeur, hauteur = 0, 0 
    # Créé une zone pour ecrire un nombre
    label_largeur = tk.Label(fenetre_redimentionner, text="LARGEUR : ")
    label_largeur.pack()
    vertical_entry = tk.Entry(fenetre_redimentionner)
    vertical_entry.pack()
    vertical_entry.insert(0, str(largeur))
    label_hauteur = tk.Label(fenetre_redimentionner, text="HAUTEUR : ")
    label_hauteur.pack()
    horizontal_entry = tk.Entry(fenetre_redimentionner)
    horizontal_entry.pack()
    horizontal_entry.insert(0, str(hauteur))

    # Création du bouton Valider
    ajouter_bouton = tk.Button(fenetre_redimentionner, text="Valider", command=lambda:redimentionner_image(canvas, vertical_entry, horizontal_entry, image_entrée))
    ajouter_bouton.pack()
    
    fenetre_redimentionner.mainloop()