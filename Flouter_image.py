import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import shutil
from globale import zoom

def boite_flouter(canvas, d):
    """
    Crée un nouvelle fenêtre "Flouter"\n
    Elle contient : \n
    - Une image d'exemple\n
    - Un bouton qui lance la fonction flouter_image\n
    - Une zone pour entrer un chiffre qui défini l'intensité du floutage et un slider qui est lié 
    """
    global photo
    # Création d'une nouvelle fenetre tkinter
    fenetre_flouter = tk.Toplevel()
    fenetre_flouter.title("Flouter")
    fenetre_flouter.iconbitmap("image_logiciel\logo.ico")
    fenetre_flouter.resizable(width=False, height=False)
    ajouter_bouton = tk.Button(fenetre_flouter, text="Valider", command=lambda:(flouter_image(canvas, chiffre_entry, d), fenetre_flouter.destroy()))
    ajouter_bouton.pack()

    # Création d'une zone pour entrer un chiffre et d'un slider
    chiffre = tk.StringVar()
    chiffre_entry = tk.Entry(fenetre_flouter, textvariable=chiffre)
    chiffre_entry.pack()
    chiffre_entry.insert(0, str(0))
    slider = tk.Scale(fenetre_flouter, from_=0, to=100, orient="horizontal")
    slider.pack(padx=0, pady=0)
    initial_value = 0
    slider.set(initial_value)

    # Mise en place d'un slider
    slider.bind("<B1-Motion>", lambda event: on_slider_change(event, chiffre_entry)) # <B1-Motion> = Mouvement souris avec bouton 1/gauche enfoncé
    slider.bind("<ButtonRelease-1>", lambda event: on_slider_change(event, chiffre_entry)) # <ButtonRelease-1> = l'utilisateur relache le bouton 1
    chiffre_entry.bind("<Return>", lambda event: on_entry_change(event, slider)) # <Return> = L'utilisateur appuie sur entrer

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_flouté.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_flouter, image=img_exemple)
    image_label.pack()

    fenetre_flouter.mainloop()


def flouter_image(canvas, chiffre_entry, d):
    """
    Permet de flouter l'entièreté de l'image \n
    Chaque point valant la moyenne des points à coté de lui 
    """
    global photo
    # Recupère le chiffre entré précedement
    valeur = int(chiffre_entry.get())
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau numpy
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)
    # Créé l'image de sortie sous forme de tableau numpy 
    image_sortie = np.copy(image_np)
    image_np = image_np.astype(np.float64)
    image_sortie = image_sortie.astype(np.float64)
    for i in range (0, valeur+1):
        # Créé des images décalé de 1 pixel dans toutes les directions
        image_decal_droite = np.concatenate((image_sortie[:, :1, :], image_sortie), axis=1)
        image_decal_gauche = np.concatenate((image_sortie, image_sortie[:, -1:, :] ), axis=1)
        image_decal_haut = np.concatenate((image_sortie[:1,:, :], image_sortie), axis=0)
        image_decal_bas = np.concatenate((image_sortie, image_sortie[-1:,:, :]), axis=0)
        # Fusionne toutes les images décalées
        image_sortie = (image_decal_droite[:, :-1, :] + image_decal_gauche[:, 1:, :] + image_decal_haut[:-1, :, :] + image_decal_bas[1:, :, :])/4

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
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1


def on_entry_change(event, slider):
    """
    La fonction prend en paramètre "event" qui est un evenement de tkinter\n
    et met à jour la valeur du slider quand on appuie sur entrer
    """
    value = event.widget.get()
    slider.set(value)


def on_slider_change(event, chiffre_entry):
    """
    La fonction prend en paramètre "event" qui est un evenement de tkinter\n
    et met à jour chiffre entry (valeur du tk.entry)
    """
    value = event.widget.get()
    chiffre_entry.delete(0, tk.END)  # Supprime le texte actuel dans l'Entry
    chiffre_entry.insert(0, str(value))  # Ajoute la nouvelle valeur dans l'Entry