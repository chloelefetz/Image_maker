from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from globale import zoom

def boite_transparence(canvas, d):
    """
    Créé une fenêtre "Transparence" \n
    Elle contient : \n
    - Un bouton valider qui lance la fonction transparence_image\n
    - Une zone pour entrer un nombre lié à un slider\n
    - Un exemple de l'utilité de la fonction
    """
    # Création d'une nouvelle fenêtre
    fenetre_transparence = tk.Toplevel()
    fenetre_transparence.title("Transparence")
    fenetre_transparence.resizable(width=False, height=False)

    # Création d'un bouton valider
    ajouter_bouton = tk.Button(fenetre_transparence, text="Valider", command=lambda:(transparence_image(canvas, chiffre_entry, d), fenetre_transparence.destroy()))
    ajouter_bouton.pack()
    
    # Création d'une zone pour entrer un chiffre et d'un slider
    chiffre = tk.StringVar()
    chiffre_entry = tk.Entry(fenetre_transparence, textvariable=chiffre)
    chiffre_entry.pack()
    chiffre_entry.insert(0, str(0))
    slider = tk.Scale(fenetre_transparence, from_=0, to=100, orient="horizontal")
    slider.pack(padx=0, pady=0)
    slider.set(0)

    # Mise en place du slider
    slider.bind("<B1-Motion>", lambda event: on_slider_change(event, chiffre_entry)) # <B1-Motion> = Mouvement souris avec bouton 1/gauche enfoncé
    slider.bind("<ButtonRelease-1>", lambda event: on_slider_change(event, chiffre_entry)) # <ButtonRelease-1> = l'utilisateur relache le bouton 1
    chiffre_entry.bind("<Return>", lambda event: on_entry_change(event, slider)) # <Return> = L'utilisateur appuie sur entrer

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_transparence.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_transparence, image=img_exemple)
    image_label.pack()

    fenetre_transparence.mainloop()


def transparence_image(canvas, chiffre_entry, d):
    """
    Permet de rendre transparent le couleur choisi par le clic gauche sur l'image avec une marge de tolérence choisi par l'utilisateur
    """
    global photo
    valeur = int(chiffre_entry.get())
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")
    image_np = np.asarray(image_entrée)
    couleur = image_np[d.y1, d.x1, :]
    r, v, b, a = couleur
    # Determine le minimum et la maximum pour chaque canal de couleur
    min_r = r * (1-valeur/100)
    max_r = r * (1+valeur/100)
    min_v = v * (1-valeur/100)
    max_v = v * (1+valeur/100)
    min_b = b * (1-valeur/100)
    max_b = b * (1+valeur/100) 

    # Créé l'image de sortie sous forme de tableau numpy
    image_sortie = np.copy(image_np)

    # Créé un masque qui renvoie True dans les zones qui répondent à nos critères
    condition = (image_sortie[:, :, 0] <= max_r) & (image_sortie[:, :, 1] <= max_v) & (image_sortie[:, :, 2] <= max_b) & (image_sortie[:, :, 0] >= min_r) & (image_sortie[:, :, 1] >= min_v) & (image_sortie[:, :, 2] >= min_b)
    # Met à 0 le canal alpha dans les zones où le masque est à True
    image_sortie[:,:,3][condition] = 0

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