from PIL import Image, ImageTk, ImageDraw
import numpy as np
import tkinter as tk

def inverser_couleur_image(canvas):
    """
    Permet d'inverser les couleurs d'une image\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimention\n
    Change la valeur des pixels de l'image -> l'inverse de la couleur du pixel initial\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open("image_temporaire.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape  

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np)
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            for i in range(3):
                image_sortie[ligne,col,i] = 255 - image_sortie[ligne,col,i]

    # Sauvegarde les images pour pouvoir les afficher
    Image.fromarray(image_sortie).save("image_temporaire.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file="image_temporaire.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)


def rouge_image(canvas):
    """
    Permet d'inverser les couleurs d'une image\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimention\n
    Change la valeur des pixels de l'image -> l'inverse de la couleur du pixel initial\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open("image_temporaire.png")
    image = np.asarray(image_entrée)
    # nb_lignes,nb_colonnes,_ = image.shape

    image_sortie = np.copy(image)
    # for ligne in range(nb_lignes):
    #     for col in range(nb_colonnes):
    #         image_sortie[ligne,col] = np.dot(image_sortie[ligne, col], (0, 1, 0))

            
    # image_np = np.asarray(image_entrée)
    # nb_lignes, nb_colonnes, _ = image_np.shape 

    # # Créé l'image de sortie sous forme de tableau numpy
    # rouge = (1, 0, 0)
    # image_sortie = np.copy(image_np)

    for i in range(image_sortie.shape[0]):
        for j in range(image_sortie.shape[1]):
            r, v, b, _ = image_sortie[i, j]
            image_sortie[i, j] = (99-r, 99-v, 99-b)

    # for i in range(image_sortie.shape[0]):
    #     for j in range(image_sortie.shape[1]):
    #         r, v, b = image_sortie[i, j]
    #         image_sortie[i, j] = (r, 0, 0)

    # for ligne in range(nb_lignes):
    #     for col in range(nb_colonnes):
    #         image_sortie[ligne,col] = image_sortie[ligne, col] * (0, 1, 1)

    # Sauvegarde les images pour pouvoir les afficher
    Image.fromarray(image_sortie).save("image_temporaire.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file="image_temporaire.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def symetrie_centrale(canvas):
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"image_temporaire_1.png")
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
    Image.fromarray(image_sortie).save(f"image_temporaire_1.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_1.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def symetrie_verticale(canvas):
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"image_temporaire_1.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape  

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np)
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne,col] = image_sortie[ligne,nb_colonnes-1 -col]

    # Sauvegarde les images pour pouvoir les afficher
    Image.fromarray(image_sortie).save(f"image_temporaire_1.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_1.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def symetrie_horizontale(canvas):
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"image_temporaire_1.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape  

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np)
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne,col] = image_sortie[nb_lignes-1 -ligne,col]

    # Sauvegarde les images pour pouvoir les afficher
    Image.fromarray(image_sortie).save(f"image_temporaire_1.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_1.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def miroir_vertical(canvas):
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"image_temporaire_1.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np) 
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne, col] = image_np[ligne, nb_colonnes - 1 - col]

    Image.fromarray(image_sortie).save(f"image_temporaire_1.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_1.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def miroir_horizontal(canvas):
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"image_temporaire_1.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np) 
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne, col] = image_np[nb_lignes - 1 - ligne, col]

    Image.fromarray(image_sortie).save(f"image_temporaire_1.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_1.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
