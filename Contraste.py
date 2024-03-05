import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
from globale import zoom

def boite_contraste(canvas, d):
    """
    Création d'une nouvelle fenêtre, "Modifier le contraste", tkinter\n
    Champ créé pour ecrire un nombre synchronisé avec le slider\n
    Bouton Valider qui appel la fonction contraste_image
    """ 
    # Création d'une nouvelle fenetre tkinter
    fenetre_contraste = tk.Toplevel()
    fenetre_contraste.title("Modifier le contraste")
    fenetre_contraste.iconbitmap("image_logiciel\logo.ico")
    fenetre_contraste.resizable(width=False, height=False)
    
    # Créé une zone pour ecrire un nombre
    chiffre = tk.StringVar()
    chiffre_entry = tk.Entry(fenetre_contraste, textvariable=chiffre)
    chiffre_entry.pack()
    chiffre_entry.insert(0, str(100))
    # Creation du slider pour modifier le nombre à la souris 
    slider = tk.Scale(fenetre_contraste, from_=0, to=200, orient="horizontal")
    slider.pack(padx=0, pady=0)
    slider.set(100)
    # Création du bouton
    ajouter_bouton = tk.Button(fenetre_contraste, text="Valider", command=lambda:(contraste_image(canvas, chiffre_entry, d), fenetre_contraste.destroy()))
    ajouter_bouton.pack()
    slider.bind("<B1-Motion>", lambda event: on_slider_change(event, chiffre_entry)) # <B1-Motion> = Mouvement souris avec bouton 1/gauche enfoncé
    slider.bind("<ButtonRelease-1>", lambda event: on_slider_change(event, chiffre_entry)) # <ButtonRelease-1> = l'utilisateur relache le bouton 1
    chiffre_entry.bind("<Return>", lambda event: on_entry_change(event, slider)) # <Return> = L'utilisateur appuie sur entrer

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_contraste.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_contraste, image=img_exemple)
    image_label.pack()

    fenetre_contraste.mainloop()

def contraste_image(canvas, chiffre_entry, d):
    """
    Permet d'accentuer le contraste d'une image \n
    Ouvre image_temporaire.png\n
    Transforme l'image en tableau a trois dimention\n
    Change la valeur des pixels de l'image\n
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
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
            for i in range(3):
                new_color = (image_sortie[ligne,col,i]-127)*(valeur/100)+127
                image_sortie[ligne,col,i] = max(0, min(new_color,255))
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