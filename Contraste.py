from tkinter import * 
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def contraste_image(canvas, chiffre_entry):
    """
    Permet d'accentuer le contraste d' une image 
    Ouvre image_temporaire.png
    Transforme l'image en tableau a trois dimention
    Change la valeur des pixels de l'image
    Sauvegarde le resultat dans image_temporaire.png
    """
    global photo
    # Recupère le chiffre entré précedement
    valeur = chiffre_entry.get()
    valeur = int(valeur)
    # Charge l'image ouverte par la fonction ouvrir_image et la transforme en tableau couleurs
    image_entrée = Image.open("image_temporaire.png")
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
    Image.fromarray(image_sortie).save("image_temporaire.png")
    canvas.delete("all")
    photo = ImageTk.PhotoImage(file="image_temporaire.png")
    largeur_image = photo.width()
    hauteur_image = photo.height()
    canvas.config(width=largeur_image, height=hauteur_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def boite_contraste(canvas):
    """
    Création une nouvelle page tkinter
    Champ créé pour ecrire un nombre 
    Bouton Valider qui appel la fonction contraste_image
    """ 
    # Création d'une nouvelle fenetre tkinter
    fenetre_contraste = tk.Tk()
    fenetre_contraste.title("Modifier le contraste")
    # Créé une zone pour ecrire un nombre
    chiffre = tk.StringVar()
    chiffre_entry = tk.Entry(fenetre_contraste, textvariable=chiffre)
    chiffre_entry.pack()
    chiffre_entry.insert(0, str(100))
    slider = tk.Scale(fenetre_contraste, from_=0, to=200, orient="horizontal")
    slider.pack(padx=50, pady=50)
    initial_value = 100
    slider.set(initial_value)
    ajouter_bouton = tk.Button(fenetre_contraste, text="Valider", command=lambda:contraste_image(canvas, chiffre_entry))
    ajouter_bouton.pack()
    slider.bind("<B1-Motion>", lambda event: on_slider_change(event, chiffre_entry)) # <B1-Motion> = Mouvement souris avec bouton 1/gauche enfoncé
    slider.bind("<ButtonRelease-1>", lambda event: on_slider_change(event, chiffre_entry)) # <ButtonRelease-1> = l'utilisateur relache le bouton 1
    chiffre_entry.bind("<Return>", lambda event: on_entry_change(event, slider)) # <Return> = L'utilisateur appuie sur entrer
    fenetre_contraste.mainloop()

def on_entry_change(event, slider):
    """
    La fonction prend en paramètre "event" qui est un evenement de tkinter
    et met à jour la valeur du slider quand on appuie sur entrer
    """
    value = event.widget.get()
    slider.set(value)


def on_slider_change(event, chiffre_entry):
    """
    La fonction prend en paramètre "event" qui est un evenement de tkinter
    et met à jour chiffre entry (valeur du tk.entry)
    """
    value = event.widget.get()
    chiffre_entry.delete(0, tk.END)  # Supprime le texte actuel dans l'Entry
    chiffre_entry.insert(0, str(value))  # Ajoute la nouvelle valeur dans l'Entry

    
