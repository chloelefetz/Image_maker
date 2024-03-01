from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from globale import zoom

def boite_inverser_couleur(canvas, d):
    """
    Créé une fenêtre "Inverser Couleur" avec un bouton valider qui lance la fonction inverser_couleur_image
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_inv_couleur = tk.Toplevel()
    fenetre_inv_couleur.title("Inverser Couleur")
    fenetre_inv_couleur.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_inv_couleur, text="Valider", command=lambda:(inverser_couleur_image(canvas, d), fenetre_inv_couleur.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logitiel\chiens_inverser_couleur.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)

    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_inv_couleur, image=img_exemple)
    image_label.pack()
    fenetre_inv_couleur.mainloop()

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
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape  

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np)
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            for i in range(3):
                image_sortie[ligne,col,i] = 255 - image_sortie[ligne,col,i]
    
    # Sauvegarde les images pour pouvoir les afficher
    Image.fromarray(image_sortie).save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logitiel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)

    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1

def boite_rouge(canvas, d):
    """
    Créé une fenêtre "Image Rouge" avec un bouton valider qui lance la fonction rouge_image
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_rouge = tk.Toplevel()
    fenetre_rouge.title("Image Rouge")
    fenetre_rouge.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_rouge, text="Valider", command=lambda:(rouge_image(canvas, d), fenetre_rouge.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logitiel\chiens_rouge.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)

    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_rouge, image=img_exemple)
    image_label.pack()
    fenetre_rouge.mainloop()

def rouge_image(canvas, d):
    """
    Permet d'inverser les couleurs d'une image\n
    Ouvre image_temporaire.png\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image = np.asarray(image_entrée)
    image_sortie = np.copy(image)

    # Appliquer le filtre rouge
    image_sortie[:, :, 1] = 0  # Mettre à zéro le canal vert
    image_sortie[:, :, 2] = 0  # Mettre à zéro le canal bleu


    Image.fromarray(image_sortie).save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logitiel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)

    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1
    
def boite_verte(canvas, d):
    """
    Créé une fenêtre "Image Verte" avec un bouton valider qui lance la fonction vert_image
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_vert = tk.Toplevel()
    fenetre_vert.title("Image Verte")
    fenetre_vert.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_vert, text="Valider", command=lambda:(vert_image(canvas, d),fenetre_vert.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logitiel\chiens_vert.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_vert, image=img_exemple)
    image_label.pack()
    fenetre_vert.mainloop()

def vert_image(canvas, d):
    """
    Permet d'inverser les couleurs d'une image\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimension\n
    Change la valeur des pixels de l'image -> l'inverse de la couleur du pixel initial\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image = np.asarray(image_entrée)
    image_sortie = np.copy(image)
    
    # Appliquer le filtre vert
    image_sortie[:, :, 0] = 0  # Mettre à zéro le canal rouge
    image_sortie[:, :, 2] = 0  # Mettre à zéro le canal bleu


    Image.fromarray(image_sortie).save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logitiel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)

    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1
    
def boite_bleu(canvas, d):
    """
    Créé une fenêtre "Image Bleue" avec un bouton valider qui lance la fonction bleu_image
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_bleue = tk.Toplevel()
    fenetre_bleue.title("Image Bleue")
    fenetre_bleue.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_bleue, text="Valider", command=lambda:(bleu_image(canvas, d), fenetre_bleue.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logitiel\chiens_bleu.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)

    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_bleue, image=img_exemple)
    image_label.pack()
    fenetre_bleue.mainloop()

def bleu_image(canvas, d):
    """
    Permet d'inverser les couleurs d'une image\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimension\n
    Change la valeur des pixels de l'image -> l'inverse de la couleur du pixel initial\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image = np.asarray(image_entrée)
    image_sortie = np.copy(image)
    
    # Appliquer le filtre bleu
    image_sortie[:, :, 0] = 0  # Mettre à zéro le canal rouge
    image_sortie[:, :, 1] = 0  # Mettre à zéro le canal vert


    Image.fromarray(image_sortie).save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logitiel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)

    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1
    
def boite_cyan(canvas, d):
    """
    Créé une fenêtre "Image Cyan" avec un bouton valider qui lance la fonction cyan_image
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_cyan = tk.Toplevel()
    fenetre_cyan.title("Image Cyan")
    fenetre_cyan.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_cyan, text="Valider", command=lambda:(cyan_image(canvas, d), fenetre_cyan.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logitiel\chiens_cyan.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)

    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_cyan, image=img_exemple)
    image_label.pack()
    fenetre_cyan.mainloop()

def cyan_image(canvas, d):
    """
    Permet d'inverser les couleurs d'une image\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimension\n
    Change la valeur des pixels de l'image -> l'inverse de la couleur du pixel initial\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image = np.asarray(image_entrée)
    image_sortie = np.copy(image)
    
    # Appliquer le filtre bleu
    image_sortie[:, :, 0] = 0  # Mettre à zéro le canal rouge

    Image.fromarray(image_sortie).save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logitiel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)

    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1 

def boite_jaune(canvas, d):
    """
    Créé une fenêtre "Image Jaune" avec un bouton valider qui lance la fonction jaune_image
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_jaune = tk.Toplevel()
    fenetre_jaune.title("Image Jaune")
    fenetre_jaune.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_jaune, text="Valider", command=lambda:(jaune_image(canvas, d), fenetre_jaune.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logitiel\chiens_jaune.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)

    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_jaune, image=img_exemple)
    image_label.pack()
    fenetre_jaune.mainloop()   

def jaune_image(canvas, d):
    """
    Permet d'inverser les couleurs d'une image\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimension\n
    Change la valeur des pixels de l'image -> l'inverse de la couleur du pixel initial\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image = np.asarray(image_entrée)
    image_sortie = np.copy(image)
    
    # Appliquer le filtre bleu
    image_sortie[:, :, 2] = 0  # Mettre à zéro le canal rouge

    Image.fromarray(image_sortie).save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logitiel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)

    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1


def boite_magenta(canvas, d):
    """
    Créé une fenêtre "Image Rouge" avec un bouton valider qui lance la fonction magenta_image
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_magenta = tk.Toplevel()
    fenetre_magenta.title("Image Magenta")
    fenetre_magenta.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_magenta, text="Valider", command=lambda:(magenta_image(canvas, d), fenetre_magenta.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logitiel\chiens_magenta.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)

    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_magenta, image=img_exemple)
    image_label.pack()
    fenetre_magenta.mainloop()    

def magenta_image(canvas, d):
    """
    Permet d'inverser les couleurs d'une image\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimension\n
    Change la valeur des pixels de l'image -> l'inverse de la couleur du pixel initial\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image = np.asarray(image_entrée)
    image_sortie = np.copy(image)
    
    # Appliquer le filtre bleu
    image_sortie[:, :, 1] = 0  # Mettre à zéro le canal rouge

    Image.fromarray(image_sortie).save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logitiel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)

    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo) 
    d.indice_temp += 1

def boite_gris(canvas, d):
    """
    Créé une fenêtre "Image Grise" avec un bouton valider qui lance la fonction nuance_de_gris
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_grise = tk.Toplevel()
    fenetre_grise.title("Image Grise")
    fenetre_grise.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_grise, text="Valider", command=lambda:(nuance_de_gris(canvas, d), fenetre_grise.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logitiel\chiens_gris.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)

    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_grise, image=img_exemple)
    image_label.pack()
    fenetre_grise.mainloop()   

def nuance_de_gris(canvas, d):
    """
    Permet d'inverser les couleurs d'une image\n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimension\n
    Change la valeur des pixels de l'image -> l'inverse de la couleur du pixel initial\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    global photo
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    
    image_sortie = image_entrée.convert("L")

    image_sortie.save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logitiel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)

    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1
    
def boite_sepia(canvas, d):
    """
    Créé une fenêtre "Image Sepia" avec un bouton valider qui lance la fonction sepia
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_sepia = tk.Toplevel()
    fenetre_sepia.title("Image Sepia")
    fenetre_sepia.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_sepia, text="Valider", command=lambda:(sepia(canvas, d), fenetre_sepia.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logitiel\chiens_sepia.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_sepia, image=img_exemple)
    image_label.pack()
    fenetre_sepia.mainloop()

def sepia(canvas, d):
    global photo
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
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

    image_sortie_Sepia.save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logitiel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)

    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)
    
    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1