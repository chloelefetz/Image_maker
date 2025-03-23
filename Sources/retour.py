import tkinter as tk 
from PIL import Image, ImageTk
from os import remove, path
from globale import zoom

def retour_arriere(canvas, text_resolution, d):
    """
    Permet de revenir à l'étape précédente 
    """
    global photo
    canvas.delete("all")
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 2}.png").convert("RGBA")

    # grille de transparence image png
    grille = Image.open('image_logiciel\grille.png')
    grille = grille.convert("RGBA").resize(image_entrée.size)
    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    d.indice_temp -= 1
    # Affiche le résultat final avec le zoom et la grille
    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    # Modifie le texte de la hauteur et largeur de l'image dans la frame information
    nouveau_texte = "\nRésolution\nLargeur : " + str(photo.width()) + "px\nHauteur : " + str(photo.height()) + "px"
    text_resolution.config(text=nouveau_texte)
    # Modifie le texte de la hauteur et largeur de l'image dans la frame information
    nouveau_texte = "\nRésolution\nLargeur : " + str(photo.width()) + "px\nHauteur : " + str(photo.height()) + "px"
    text_resolution.config(text=nouveau_texte)

def retour_debut(canvas, text_resolution, d):
    """
    Permet de revenir à l'image originale\n
    Supprime les fichiers temporaires
    """
    # Suppression des fichiers temporaire
    for i in range(1, 10000):
        if path.isfile(f"temporaire\image_temporaire_{i}.png"):
            remove(f"temporaire\image_temporaire_{i}.png")
            
    d.indice_temp = 1
    global photo
    canvas.delete("all")
    image_entrée = Image.open(f"temporaire\image_temporaire_0.png").convert("RGBA")

    # grille de transparence image png
    grille = Image.open('image_logiciel\grille.png')
    grille = grille.convert("RGBA").resize(image_entrée.size)
    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)
    
    # Affiche le résultat final avec le zoom et la grille
    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    # Modifie le texte de la hauteur et largeur de l'image dans la frame information
    nouveau_texte = "\nRésolution\nLargeur : " + str(photo.width()) + "px\nHauteur : " + str(photo.height()) + "px"
    text_resolution.config(text=nouveau_texte)
    # Modifie le texte de la hauteur et largeur de l'image dans la frame information
    nouveau_texte = "\nRésolution\nLargeur : " + str(photo.width()) + "px\nHauteur : " + str(photo.height()) + "px"
    text_resolution.config(text=nouveau_texte)