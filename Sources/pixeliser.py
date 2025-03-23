import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
from globale import zoom

def boite_pixeliser(canvas, d):
    """
    Création d'une nouvelle fenêtre tkinter "Block de pixels"\n
    Elle contient : 
    - Un champ pour ecrire un nombre et un slider lié au champ \n
    - un bouton Valider qui appel la fonction pixeliser_image
    """ 
    # Création d'une nouvelle fenetre tkinter
    fenetre_pixeliser = tk.Toplevel()
    fenetre_pixeliser.title("Block de pixels")
    fenetre_pixeliser.iconbitmap("image_logiciel\logo.ico")
    fenetre_pixeliser.resizable(width=False, height=False)
    fenetre_pixeliser.attributes('-topmost', True)
    
    # Créé une zone pour ecrire un nombre et un slider
    cmd = fenetre_pixeliser.register(lambda s: not s or s.isdigit())
    chiffre_entry = tk.Entry(fenetre_pixeliser, validatecommand=(cmd, "%P"))
    chiffre_entry.insert(0, str(0))
    chiffre_entry.pack()
    slider = tk.Scale(fenetre_pixeliser, from_=0, to=255, orient="horizontal")
    slider.pack(padx=0, pady=0)
    slider.set(0)

    # Création du bouton valider
    ajouter_bouton = tk.Button(fenetre_pixeliser, text="Valider", command=lambda:(pixeliser_image(canvas, chiffre_entry, d), fenetre_pixeliser.destroy()))
    ajouter_bouton.pack()


    slider.bind("<B1-Motion>", lambda event: on_slider_change(event, chiffre_entry)) # <B1-Motion> = Mouvement souris avec bouton 1/gauche enfoncé
    slider.bind("<ButtonRelease-1>", lambda event: on_slider_change(event, chiffre_entry)) # <ButtonRelease-1> = l'utilisateur relache le bouton 1
    chiffre_entry.bind("<Return>", lambda event: on_entry_change(event, slider)) # <Return> = L'utilisateur appuie sur entrer

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_pixeliser.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_pixeliser, image=img_exemple)
    image_label.pack()

    fenetre_pixeliser.mainloop() 

def pixeliser_image(canvas, chiffre_entry, d):
    """
    Permet de pixeliser une image \n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimension\n
    Divise l'image en block de pixels et fait la moyenne de leurs couleurs\n
    Sauvegarde le resultat dans image_temporaire.png
    """
    global photo
    # Recupère le chiffre entré précedement
    valeur = int(chiffre_entry.get())
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)
    nb_lignes, nb_colonnes, _ = image_np.shape 
    # Créé l'image de sortie sous forme de tableau numpy 
    image_sortie = np.copy(image_np)
    image_np = image_np.astype(np.float64)
    image_sortie = image_sortie.astype(np.float64)
    for ligne in range(0, nb_lignes, valeur):
        for col in range(0, nb_colonnes, valeur):
            for i in range(3):
                a = image_np[ligne:ligne+valeur, col:col+valeur, i]
                b = np.mean(a) #Fait la moyenne des couleurs des pixels compris dans le block à pixeliser
                image_sortie[ligne:ligne+valeur, col:col+valeur, i] = b
            if np.any(image_sortie[ligne:ligne+valeur, col:col+valeur, 3] > 0): 
                #Met l'oppacité de tous les pixels compris dans la block a pixeliser à 255
                image_sortie[ligne:ligne+valeur, col:col+valeur, 3] = 255 
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