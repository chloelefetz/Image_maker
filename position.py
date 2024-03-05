from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from globale import zoom

def boite_rotation(canvas, d):
    """
    Créé une fenêtre "Rotation" avec un bouton valider qui lance la fonction rotation\n
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_rotation = tk.Toplevel()
    fenetre_rotation.title("Rotation")
    fenetre_rotation.iconbitmap("image_logiciel\logo.ico")
    fenetre_rotation.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_rotation, text="Valider", command=lambda:(rotation(canvas, d), fenetre_rotation.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_rotation.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_rotation, image=img_exemple)
    image_label.pack()
    fenetre_rotation.mainloop()

def rotation(canvas, d):
    """
    Fait une rotation de l'image de 90 degrès dans le sens anti-horaire 
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau numpy
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)

    # Effectue une rotation de 90° d'un tableau dans le plan des deux premiers axes
    image_sortie = np.rot90(image_np)

    # Sauvegarde les images pour pouvoir les afficher
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

def boite_symetrie_centrale(canvas, d):
    """
    Créé une fenêtre "Symetrie centrale" avec un bouton valider qui lance la fonction symetrie_centrale\n
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_sym_centrale = tk.Toplevel()
    fenetre_sym_centrale.title("Symetrie centrale")
    fenetre_sym_centrale.iconbitmap("image_logiciel\logo.ico")
    fenetre_sym_centrale.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_sym_centrale, text="Valider", command=lambda:(symetrie_centrale(canvas, d), fenetre_sym_centrale.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_sym_centrale.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_sym_centrale, image=img_exemple)
    image_label.pack()
    fenetre_sym_centrale.mainloop()

def symetrie_centrale(canvas, d):
    """
    Utilise le quart inferieur droit et le duplique 4 fois de manière symétrique par rapport au centre 
    """
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau numpy
    global photo
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape  

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np)
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne,col] = image_sortie[ligne,nb_colonnes-1 -col]
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne,col] = image_sortie[nb_lignes-1 -ligne,col]

    # Sauvegarde les images pour pouvoir les afficher
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

def boite_symetrie_verticale(canvas, d):
    """
    Créé une fenêtre "Symetrie verticale" avec un bouton valider qui lance la fonction symetrie_verticale\n
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_sym_verticale = tk.Toplevel()
    fenetre_sym_verticale.title("Symetrie verticale")
    fenetre_sym_verticale.iconbitmap("image_logiciel\logo.ico")
    fenetre_sym_verticale.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_sym_verticale, text="Valider", command=lambda:(symetrie_verticale(canvas, d), fenetre_sym_verticale.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_sym_verticale.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)

    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_sym_verticale, image=img_exemple)
    image_label.pack()
    fenetre_sym_verticale.mainloop()

def symetrie_verticale(canvas, d):
    """
    Duplique la moitié droite de l'image selon une symetrie verticale
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau numpy
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape  

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np)
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne,col] = image_sortie[ligne,nb_colonnes-1 -col]

    # Sauvegarde les images pour pouvoir les afficher
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

def boite_symetrie_horizontale(canvas, d): 
    """
    Créé une fenêtre "Symetrie horizontale" avec un bouton valider qui lance la fonction symetrie_horizontale\n
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_sym_horizontale = tk.Toplevel()
    fenetre_sym_horizontale.title("Symetrie horizontale")
    fenetre_sym_horizontale.iconbitmap("image_logiciel\logo.ico")
    fenetre_sym_horizontale.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_sym_horizontale, text="Valider", command=lambda:(symetrie_horizontale(canvas, d), fenetre_sym_horizontale.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_sym_horizontale.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)

    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_sym_horizontale, image=img_exemple)
    image_label.pack()
    fenetre_sym_horizontale.mainloop()

def symetrie_horizontale(canvas, d):
    """
    Duplique la moitié basse de l'image selon une symetrie horizontale
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape  

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np)
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne,col] = image_sortie[nb_lignes-1 -ligne,col]

    # Sauvegarde les images pour pouvoir les afficher
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

def boite_miroir_vertical(canvas, d):
    """
    Créé une fenêtre "Miroir vertical" avec un bouton valider qui lance la fonction miroir_vertical\n
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_mir_vertical = tk.Toplevel()
    fenetre_mir_vertical.title("Miroir Vertical")
    fenetre_mir_vertical.iconbitmap("image_logiciel\logo.ico")
    fenetre_mir_vertical.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_mir_vertical, text="Valider", command=lambda:(miroir_vertical(canvas, d), fenetre_mir_vertical.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_mir_vertical.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)

    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_mir_vertical, image=img_exemple)
    image_label.pack()
    fenetre_mir_vertical.mainloop()

def miroir_vertical(canvas, d):
    """
    Affiche le miroir de l'image selon l'axe vertical
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np) 
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne, col] = image_np[ligne, nb_colonnes - 1 - col]

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

def boite_miroir_horizontal(canvas, d):
    """
    Créé une fenêtre "Miroir horizontal avec un bouton valider qui lance la fonction miroir_horizontal\n
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_mir_horizontal = tk.Toplevel()
    fenetre_mir_horizontal.title("Miroir horizontal")
    fenetre_mir_horizontal.iconbitmap("image_logiciel\logo.ico")
    fenetre_mir_horizontal.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_mir_horizontal, text="Valider", command=lambda:(miroir_horizontal(canvas, d), fenetre_mir_horizontal.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_mir_horizontal.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_mir_horizontal, image=img_exemple)
    image_label.pack()
    fenetre_mir_horizontal.mainloop()

def miroir_horizontal(canvas, d):
    """
    Affiche le miroir de l'image selon l'axe horizontal
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np) 
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne, col] = image_np[nb_lignes - 1 - ligne, col]

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