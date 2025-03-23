import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import os
from globale import zoom

def boite_redimensionner(canvas, text_resolution, d):
    """
    Creation une nouvelle fenêtre tkinter : "Modifier les dimensions de l'image"\n
    Elle contient : \n
    - Des champs pour écrire la hauteur et la largeur\n 
    - Un bouton Valider qui appel la fonction redimensionner_image
    """ 
    # Création d'une nouvelle fenetre tkinter
    fenetre_redimensionner = tk.Toplevel()
    fenetre_redimensionner.title("Modifier les dimensions de l'image")
    fenetre_redimensionner.iconbitmap("image_logiciel\logo.ico")
    fenetre_redimensionner.resizable(width=False, height=False)
    fenetre_redimensionner.attributes('-topmost', True)
    
    # Regarde si le fichier "image_temporaire.png" existe
    if os.path.exists(f"temporaire\image_temporaire_{d.indice_temp - 1}.png"):
        image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
        largeur, hauteur = image_entrée.size # Récupère la largeur et hauteur de l'image  
    else : 
        largeur, hauteur = 0, 0 
    # Créé une zone pour ecrire la largeur souhaitée
    label_largeur = tk.Label(fenetre_redimensionner, text="LARGEUR : ")
    label_largeur.pack()
    vertical_entry = tk.Entry(fenetre_redimensionner)
    vertical_entry.pack()
    vertical_entry.insert(0, str(largeur))
    # Créé une zone pour ecrire la hauteur souhaitée
    label_hauteur = tk.Label(fenetre_redimensionner, text="HAUTEUR : ")
    label_hauteur.pack()
    horizontal_entry = tk.Entry(fenetre_redimensionner)
    horizontal_entry.pack()
    horizontal_entry.insert(0, str(hauteur))

    # Création du bouton Valider
    ajouter_bouton = tk.Button(fenetre_redimensionner, text="Valider", command=lambda:(redimensionner_image(canvas, vertical_entry, horizontal_entry, image_entrée, text_resolution, d), fenetre_redimensionner.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_redimensionner.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_redimensionner, image=img_exemple)
    image_label.pack()
    
    fenetre_redimensionner.mainloop()

def redimensionner_image(canvas, vertical_entry, horizontal_entry, image_entrée, text_resolution, d):
    """
    Permet de redimensionner une image \n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimension\n
    Change le nombre de pixels de l'image -> agrandissement ou rétrécissement\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    global photo
    # Recupère le chiffre entré précedement
    valeur_vertical = int(vertical_entry.get())
    valeur_horizontal = int(horizontal_entry.get())
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau numpy
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
    Image.fromarray(image_sortie).save(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # Charge l'image modifiée
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logiciel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)
    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    # Affiche le résultat final avec le zoom et la grille
    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    # Modifie le texte de la hauteur et largeur de l'image dans la frame information
    nouveau_texte = "\nRésolution\nLargeur : " + str(photo.width()) + "px\nHauteur : " + str(photo.height()) + "px"
    text_resolution.config(text=nouveau_texte)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1
    