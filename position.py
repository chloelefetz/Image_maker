from PIL import Image, ImageTk, ImageDraw
import numpy as np
import tkinter as tk

def symetrie_centrale(canvas, d):
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"image_temporaire_{d - 1}.png")
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
    Image.fromarray(image_sortie).save(f"image_temporaire_{d}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def symetrie_verticale(canvas, d):
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"image_temporaire_{d - 1}.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape  

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np)
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne,col] = image_sortie[ligne,nb_colonnes-1 -col]

    # Sauvegarde les images pour pouvoir les afficher
    Image.fromarray(image_sortie).save(f"image_temporaire_{d}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def symetrie_horizontale(canvas, d):
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"image_temporaire_{d - 1}.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape  

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np)
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne,col] = image_sortie[nb_lignes-1 -ligne,col]

    # Sauvegarde les images pour pouvoir les afficher
    Image.fromarray(image_sortie).save(f"image_temporaire_{d}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def miroir_vertical(canvas, d):
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"image_temporaire_{d - 1}.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np) 
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne, col] = image_np[ligne, nb_colonnes - 1 - col]

    Image.fromarray(image_sortie).save(f"image_temporaire_{d}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def miroir_horizontal(canvas, d):
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"image_temporaire_{d - 1}.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np) 
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            image_sortie[ligne, col] = image_np[nb_lignes - 1 - ligne, col]

    Image.fromarray(image_sortie).save(f"image_temporaire_{d}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)