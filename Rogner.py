from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from globale import zoom

def boite_rogner_image(canvas, d):
    """
    Création d'une nouvelle fenêtre tkinter : "Rogner l'image"\n
    Elle contient : \n
    - Un bouton Valider qui lance la fonction rogner_image\n
    - Des explications sur son fonctionnement
    """
    global photo
    # Création d'une nouvelle fenetre tkinter
    fenetre_rogner = tk.Toplevel()
    fenetre_rogner.title("Rogner l'image")
    fenetre_rogner.iconbitmap("image_logiciel\logo.ico")
    fenetre_rogner.resizable(width=False, height=False)
    # Création du bouton Valider
    ajouter_bouton = tk.Button(fenetre_rogner, text="Valider", command=lambda:(rogner_image(canvas, d), fenetre_rogner.destroy()))
    ajouter_bouton.pack()

    # Création d'une frame pour mettre une image et du texte côte à côte
    frame1 = tk.Frame(fenetre_rogner)
    frame1.pack(padx=10, pady=10)
    img1 = Image.open("image_logiciel\clic_gauche.png").convert("RGBA")
    img_exemple1 = ImageTk.PhotoImage(img1)
    # Créer un label pour afficher l'image du clic gauche
    image_label1 = tk.Label(frame1, image=img_exemple1)
    image_label1.pack(side=tk.LEFT, padx=10, pady=10)
    # Créer la zone de texte
    texte1 = "Tous ce qui est au-dessus et à gauche\n de l'endroit où vous avec cliqué \n avec votre clic gauche de souris sera supprimé"
    texte_label1 = tk.Label(frame1, text=texte1)
    texte_label1.pack(side=tk.LEFT, padx=10, pady=10)

    # Création d'une frame pour mettre une image et du texte côte à côte
    frame2 = tk.Frame(fenetre_rogner)
    frame2.pack(padx=10, pady=10)
    img2 = Image.open("image_logiciel\clic_droit.png").convert("RGBA")
    img_exemple2 = ImageTk.PhotoImage(img2)
    # Créer un label pour afficher l'image du clic droit
    image_label2 = tk.Label(frame2, image=img_exemple2)
    image_label2.pack(side=tk.LEFT, padx=10, pady=10)
    # Créer la zone de texte
    texte2 = "Tous ce qui est en-dessous et à droite\n de l'endroit où vous avec cliqué \n avec votre clic droit de souris sera supprimé"
    texte_label2 = tk.Label(frame2, text=texte2)
    texte_label2.pack(side=tk.LEFT, padx=10, pady=10)

    fenetre_rogner.mainloop()


def rogner_image(canvas, d):
    """
    Permet de rogner une image \n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimention\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau numpy
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)
    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = image_np[d.y1:d.y2, d.x1:d.x2]
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