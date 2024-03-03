import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from os import remove, path

def ouvrir_image(canvas, text_resolution, slider, d):
    """
    Ouvre un fichier image present dans l'ordinateur\n
    Remplace le canva actuellement affichée par la nouvelle image\n
    Sauvegarde l'image au format RGBA dans un fichier image_temporaire
    """
    global photo
    # Boite pour choisir le fichier qu'on veut ouvrir
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")], initialdir="images/")
    if file_path:
        # Supprimer tout les anciens fichiers temporaire
        for i in range(10000):
            if path.isfile(f"temporaire\image_temporaire_{i}.png"):
                remove(f"temporaire\image_temporaire_{i}.png")
        
        # Charge l'image modifiée
        image_entrée = Image.open(file_path).convert("RGBA")
        d.indice_temp = 0
        image_entrée.save(f"temporaire\image_temporaire_{d.indice_temp}.png")

        # grille de transparence image png
        grille = Image.open('image_logiciel\grille.png')
        image_entrée = image_entrée.convert("RGBA")
        grille = grille.convert("RGBA").resize(image_entrée.size)
        # Superposer l'image sur la grille
        image_entrée = Image.alpha_composite(grille, image_entrée)

        # Affiche le résultat final avec le zoom à 100% et la grille
        canvas.delete("all")
        photo = ImageTk.PhotoImage(image_entrée)
        largeur_image = photo.width()
        hauteur_image = photo.height()
        canvas.config(width=largeur_image, height=hauteur_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        
        # Met à jour le texte de la frame information
        nouveau_texte = "\nRésolution\nLargeur : " + str(largeur_image) + "px\nHauteur : " + str(hauteur_image) + "px"
        text_resolution.config(text=nouveau_texte)

        # Remet le niveau de zoom à 100%
        slider.set(100)
        d.indice_temp += 1