from PIL import Image, ImageTk, ImageDraw
import numpy as np
import tkinter as tk

def inverser_couleur_image(canvas, d):
    """
    Permet d'inverser les couleurs d'une image\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimention\n
    Change la valeur des pixels de l'image -> l'inverse de la couleur du pixel initial\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape  

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np)
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            for i in range(3):
                image_sortie[ligne,col,i] = 255 - image_sortie[ligne,col,i]

    # Sauvegarde les images pour pouvoir les afficher
    Image.fromarray(image_sortie).save(f"image_temporaire_{d.indice_temp}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d.indice_temp}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1
    
def rouge_image(canvas, d):
    """
    Permet d'afficher l'image avec seulement la couleur rouge\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimention\n
    Change la valeur des pixels de l'image -> supprime les pixel de couleur autre que le rouge\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"image_temporaire_{d.indice_temp - 1}.png")
    image = np.asarray(image_entrée)
    image_sortie = np.copy(image)

    # Appliquer le filtre rouge
    image_sortie[:, :, 1] = 0  # Mettre à zéro le canal vert
    image_sortie[:, :, 2] = 0  # Mettre à zéro le canal bleu


    Image.fromarray(image_sortie).save(f"image_temporaire_{d.indice_temp}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d.indice_temp}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1

def vert_image(canvas, d):
    """
    Permet d'afficher l'image avec seulement la couleur verte\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimention\n
    Change la valeur des pixels de l'image -> supprime les pixel de couleur autre que le vert\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"image_temporaire_{d.indice_temp - 1}.png")
    image = np.asarray(image_entrée)
    image_sortie = np.copy(image)
    
    # Appliquer le filtre vert
    image_sortie[:, :, 0] = 0  # Mettre à zéro le canal rouge
    image_sortie[:, :, 2] = 0  # Mettre à zéro le canal bleu


    Image.fromarray(image_sortie).save(f"image_temporaire_{d.indice_temp}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d.indice_temp}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1

def bleu_image(canvas, d):
    """
    Permet d'afficher l'image avec seulement la couleur bleue\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimention\n
    Change la valeur des pixels de l'image -> supprime les pixel de couleur autre que le bleu\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"image_temporaire_{d.indice_temp - 1}.png")
    image = np.asarray(image_entrée)
    image_sortie = np.copy(image)
    
    # Appliquer le filtre bleu
    image_sortie[:, :, 0] = 0  # Mettre à zéro le canal rouge
    image_sortie[:, :, 1] = 0  # Mettre à zéro le canal vert


    Image.fromarray(image_sortie).save(f"image_temporaire_{d.indice_temp}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d.indice_temp}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1

def cyan_image(canvas, d):
    """
    Permet de donner une teinte de couleur cyan à l'image\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimention\n
    Change la valeur des pixels de l'image -> supprime les pixel de couleur rouge\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"image_temporaire_{d.indice_temp - 1}.png")
    image = np.asarray(image_entrée)
    image_sortie = np.copy(image)
    
    # Appliquer le filtre cyan
    image_sortie[:, :, 0] = 0  # Mettre à zéro le canal rouge

    Image.fromarray(image_sortie).save(f"image_temporaire_{d.indice_temp}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d.indice_temp}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1

def jaune_image(canvas, d):
    """
    Permet de donner une teinte de couleur jaune à l'image\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimention\n
    Change la valeur des pixels de l'image -> supprime les pixel de couleur bleue\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"image_temporaire_{d.indice_temp - 1}.png")
    image = np.asarray(image_entrée)
    image_sortie = np.copy(image)
    
    # Appliquer le filtre jaune
    image_sortie[:, :, 2] = 0  # Mettre à zéro le canal bleu

    Image.fromarray(image_sortie).save(f"image_temporaire_{d.indice_temp}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d.indice_temp}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1

def magenta_image(canvas, d):
    """
    Permet de donner une teinte de couleur magenta à l'image\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimention\n
    Change la valeur des pixels de l'image -> supprime les pixel de couleur verte\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"image_temporaire_{d.indice_temp - 1}.png")
    image = np.asarray(image_entrée)
    image_sortie = np.copy(image)
    
    # Appliquer le filtre magenta
    image_sortie[:, :, 1] = 0  # Mettre à zéro le canal vert

    Image.fromarray(image_sortie).save(f"image_temporaire_{d.indice_temp}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d.indice_temp}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1

def nuance_de_gris(canvas, d):
    """
    Permet de convertir une image couleur en nuance de gris\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimension\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"image_temporaire_{d.indice_temp - 1}.png")
    image_sortie = image_entrée.convert("L")

    image_sortie.save(f"image_temporaire_{d.indice_temp}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d.indice_temp}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1

def sepia(canvas, d):
    """
    Permet de convertir une image couleur en sépia\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimension\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    global photo
    image_entrée = Image.open(f"image_temporaire_{d.indice_temp - 1}.png")
    Taille = image_entrée.size
    image_sortie_Sepia = Image.new("RGB", Taille)

    for x in range(Taille[0]):
        for y in range(Taille[1]):
            Pixel = image_entrée.getpixel((x, y))
            R = Pixel[0]
            G = Pixel[1]
            B = Pixel[2]
            
            taux_rouge = int(0.393 * R + 0.769 * G + 0.189 * B)
            taux_vert = int(0.349 * R + 0.686 * G + 0.168 * B)
            taux_bleu = int(0.272 * R + 0.534 * G + 0.131 * B)
            
            if taux_rouge > 255: taux_rouge = 255
            if taux_vert > 255: taux_vert = 255
            if taux_bleu > 255: taux_bleu = 255
            
            image_sortie_Sepia.putpixel((x, y), (taux_rouge, taux_vert, taux_bleu))

    image_sortie_Sepia.save(f"image_temporaire_{d.indice_temp}.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file=f"image_temporaire_{d.indice_temp}.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1
