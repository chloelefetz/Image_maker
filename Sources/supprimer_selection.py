from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from globale import zoom

def boite_supprimer(canvas, d) :
    """
    Fenetre qui contient : \n
    - Un boutton Valider qui lance la fonction supprimer\n
    - Un exemple de l'utilité de la fonction\n
    - Une explication de son fonctionnement\n

    """
    global photo
    # Création d'une nouvelle fenetre tkinter
    fenetre_supprimer = tk.Toplevel()
    fenetre_supprimer.title("Supprimer la séléction")
    fenetre_supprimer.iconbitmap("image_logiciel\logo.ico")
    fenetre_supprimer.resizable(width=False, height=False)
    fenetre_supprimer.attributes('-topmost', True)

    # Création du bouton valider 
    ajouter_bouton = tk.Button(fenetre_supprimer, text="Valider", command=lambda:(supprimer(canvas, d), fenetre_supprimer.destroy()))
    ajouter_bouton.pack()

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_suppr_selection.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_supprimer, image=img_exemple)
    image_label.pack()
    # Création d'une frame pour mettre une image et du texte côte à côte
    frame1 = tk.Frame(fenetre_supprimer)
    frame1.pack(padx=10, pady=10)
    # Créer un label pour afficher l'image du clic gauche
    img1 = Image.open("image_logiciel\clic_gauche.png").convert("RGBA")
    img_exemple1 = ImageTk.PhotoImage(img1)
    image_label1 = tk.Label(frame1, image=img_exemple1)
    image_label1.pack(side=tk.LEFT, padx=10, pady=10)
    # Créer la zone de texte
    texte1 = "Tous ce qui est à l'interieur du clic gauche et du clic droit sera supprimé"
    texte_label1 = tk.Label(frame1, text=texte1)
    texte_label1.pack(side=tk.LEFT, padx=10, pady=10)
    # Créer un label pour afficher l'image du clic droit
    img2 = Image.open("image_logiciel\clic_droit.png").convert("RGBA")
    img_exemple2 = ImageTk.PhotoImage(img2)
    image_label2 = tk.Label(frame1, image=img_exemple2)
    image_label2.pack(side=tk.LEFT, padx=10, pady=10)

    fenetre_supprimer.mainloop()

def supprimer(canvas, d):
    """
    Permet de supprimer une partie d'image selon une selection
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau numpy
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)
    image_sortie = np.copy(image_np)
    # Rend la zone séléctionnée transparente
    image_sortie[d.y1:d.y2,d.x1:d.x2,3] = 0

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