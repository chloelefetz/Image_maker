from globale import zoom
import tkinter as tk 
import numpy as np
from Ouvrir_image import ouvrir_image
from zoom import on_entry_change
from sauvegarder import sauvegarder_image
from Luminosité import boite_luminosite
from Contraste import boite_contraste
from filtres import *
from position import *
from Rogner import boite_rogner_image
from Redimentionner import boite_redimentionner
from pixeliser import boite_pixeliser
from Pipette import pipette
from transparence import boite_transparence
from Info_image import info_image
from collage import boite_tampons, boite_fond
from Retour import *
from tkinter import *
from Rotation import rotation
# from Theme_image import theme_image
from os import remove, path
from PIL import Image, ImageTk

for i in range(10000):
    if path.isfile(f"temporaire\image_temporaire_{i}.png"):
        remove(f"temporaire\image_temporaire_{i}.png")

d = info_image()

def click_gauche_canvas(event, text_selectionG, d):
    """
    Récupère les coordonnées x, y de l'endroit où on à cliqué avec le clique gauche
    """
    d.x1 = int(event.x/zoom[0])
    d.y1 = int(event.y/zoom[0])
    pipette(d.x1, d.y1, text_pipette, d)
    nouveau_texte = "\nCoordonnées clique gauche\nx : " + str(d.x1) + "/ y : " + str(d.y1)
    text_selectionG.config(text=nouveau_texte)

def click_droit_canvas(event, text_selectionD, d):
    """
    Récupère les coordonnées x, y de l'endroit où on à cliqué avec le clique droit
    """
    d.x2 = int(event.x/zoom[0])
    d.y2 = int(event.y/zoom[0])
    pipette(d.x2, d.y2, text_pipette, d)
    nouveau_texte = "\nCoordonnées clique droit\nx : " + str(d.x2) + "/ y : " + str(d.y2)
    text_selectionD.config(text=nouveau_texte)


# TEST
def test_image():
    #Charger l'image PNG avec transparence
    image = Image.open("image_temporaire.png")
    print(image)

    image=image.convert("RGBA")
    print(image)

    #Convertir l'image en un tableau NumPy
    image_array = np.array(image)
    print(image_array.shape)

    Image.fromarray(image_array).save("imagetest.png")
    #Charger l'image PNG avec transparence
    image = Image.open("imagetest.png")
    print(image)

    #Convertir l'image en un tableau NumPy
    image_array = np.array(image)
    print(image_array.shape)


window = tk.Tk()
window.title("Application")
window.geometry("1024x768")
window.iconbitmap("image_logitiel\logo.ico")
window.config(background="black")

#Création frame barre d'outils
frame_outil = tk.Frame(window, bg="gray", bd=1)
frame_outil.pack(side="left", fill="y")

#Création frame informations
frame_infos = tk.Frame(window, bg="gray", bd=1, width=20)
frame_infos.pack(side="right", fill="y")

#Ajouter du texte
text_outil = tk.Label(frame_outil, text = "Barre d'outils", font=("Arial", 10), fg="black")
text_outil.pack()
text_infos = tk.Label(frame_infos, text = "Informations", font=("Arial", 10), fg="black")
text_infos.pack()
text_resolution = tk.Label(frame_infos, text = "\nRésolution\nLargeur : nd\nHauteur : nd", font=("Arial", 10), fg="black", width=20)
text_resolution.pack()
text_selectionG = tk.Label(frame_infos, text = "\nCoordonnées clique gauche\nx : nd / y : nd", font=("Arial", 10), fg="black", width=20)
text_selectionG.pack()
text_selectionD = tk.Label(frame_infos, text = "\nCoordonnées clique droit\nx : nd / y : nd", font=("Arial", 10), fg="black", width=20)
text_selectionD.pack()
text_pipette = tk.Label(frame_infos, text = "\nCouleur selectionnée\nR : nd\nV : nd\nB : nd\nA : nd", font=("Arial", 10), fg="black", width=20)
text_pipette.pack()


#Création d'une image vierge de taille 300x300px
width = 300
height = 300
canvas = tk.Canvas(window, width=width, height=height, borderwidth=0, highlightthickness=0)
canvas.pack()
photo = ImageTk.PhotoImage(file="vierge.png")
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Associe des actions aux evenement clique bouton gauche et bouton droit
canvas.bind("<Button-1>", lambda event:click_gauche_canvas(event, text_selectionG, d))
canvas.bind("<Button-3>", lambda event:click_droit_canvas(event, text_selectionD, d))

# création de l'indice pour la sauvegarde
# indice_temp = 0

# Création de la barre de menu
menuBar = Menu(window) 

# Création des menus dans le menu
menuFichier  = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Fichier",menu=menuFichier) 
menuCouleur  = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Couleur",menu=menuCouleur)
menuControleImage = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Contrôle d'image",menu=menuControleImage)
menuCollage  = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Collage",menu=menuCollage)
menuPixeliser  = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Pixeliser",menu=menuPixeliser)
menuPosition  = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Position",menu=menuPosition)

# Création des sous menus du menu
menuFichier.add_command(label="Ouvrir image", command=lambda:ouvrir_image(canvas, text_resolution, slider, d))
menuFichier.add_command(label="Sauvegarder", command=lambda:sauvegarder_image(canvas, d)) 
menuFichier.add_command(label="Quitter", command=quit) 
menuCouleur.add_command(label="Rouge", command=lambda:boite_rouge(canvas, d))
menuCouleur.add_command(label="Vert", command=lambda:boite_verte(canvas, d))
menuCouleur.add_command(label="Bleu", command=lambda:boite_bleu(canvas, d))
menuCouleur.add_command(label="cyan", command=lambda:boite_cyan(canvas, d))
menuCouleur.add_command(label="jaune", command=lambda:boite_jaune(canvas, d))
menuCouleur.add_command(label="magenta", command=lambda:boite_magenta(canvas, d))
menuCouleur.add_command(label="Inverser Couleurs", command=lambda:boite_inverser_couleur(canvas, d))
menuCouleur.add_command(label="Noir et Blanc", command=lambda:boite_gris(canvas, d))
menuCouleur.add_command(label="Sépia", command=lambda:boite_sepia(canvas, d))
menuControleImage.add_command(label="Luminosité", command=lambda:boite_luminosite(canvas, d))
menuControleImage.add_command(label="Contraste", command=lambda:boite_contraste(canvas, d))
menuControleImage.add_command(label="Transparence", command=lambda:boite_transparence(canvas, d))
menuCollage.add_command(label="Tampon", command=lambda:boite_tampons(canvas, d))
menuCollage.add_command(label="Fond", command=lambda:boite_fond(canvas, d))
menuPixeliser.add_command(label="Pixeliser", command=lambda:boite_pixeliser(canvas, d))
menuPosition.add_command(label="Rotation",  command=lambda:rotation(canvas, d)) 
menuPosition.add_command(label="Miroir vertical", command=lambda:boite_miroir_vertical(canvas, d))
menuPosition.add_command(label="Miroir horizontal", command=lambda:boite_miroir_horizontal(canvas, d))
menuPosition.add_command(label="Symetrie central", command=lambda:boite_symetrie_centrale(canvas, d))
menuPosition.add_command(label="Symetrie vertical", command=lambda:boite_symetrie_verticale(canvas, d))
menuPosition.add_command(label="Symetrie horizontal", command=lambda:boite_symetrie_horizontale(canvas, d))

# Configuration de la barre des menus
window.config(menu=menuBar)

#Créations boutons 
image_retour = Image.open("fleche_retour.png")
photo_retour = ImageTk.PhotoImage(image_retour)
button_collage = tk.Button(frame_outil, text = " Retour", image=photo_retour, compound=tk.LEFT, width=120, command=lambda:retour_arriere(canvas, d))
button_collage.pack()
image_retour_debut = Image.open("fleche_retour_debut.png")
photo_retour_debut = ImageTk.PhotoImage(image_retour_debut)
button_collage = tk.Button(frame_outil, text = " Retour début", image=photo_retour_debut, compound=tk.LEFT, width=120, command=lambda:retour_debut(canvas, d))
button_collage.pack()
image_rogner = Image.open("rogner.png")
photo_rogner = ImageTk.PhotoImage(image_rogner)
button_rogner = tk.Button(frame_outil, text = " Rogner", image=photo_rogner, compound=tk.LEFT, width=120, command=lambda:boite_rogner_image(canvas, d))
button_rogner.pack()
image_redimentionner = Image.open("redimentionner.png")
photo_redimentionner = ImageTk.PhotoImage(image_redimentionner)
button_redimentionner = tk.Button(frame_outil, text = " Redimensionner", image=photo_redimentionner, compound=tk.LEFT, width=120, command=lambda:boite_redimentionner(canvas, text_resolution, d))
button_redimentionner.pack()
# button_pipette = tk.Button(frame_outil, text="Pipette", command=lambda:pipette(x1, y1, text_pipette))
# button_pipette.pack()
# button_collage = tk.Button(frame_outil, text="Collage", command=lambda:boite_image2(canvas))
# button_collage.pack()
 
slider = tk.Scale(frame_outil, from_=10, to=200, orient="horizontal")
slider.pack(padx=10, pady=10, side="bottom")
label_zoom = tk.Label(frame_outil, text="Zoom")
label_zoom.pack(side="bottom")
initial_value = 100
slider.set(initial_value)
slider.bind("<ButtonRelease-1>", lambda event: on_entry_change(event, canvas, d)) # <ButtonRelease-1> = l'utilisateur relache le bouton 1


# button_test = tk.Button(frame_outil, text="TEST", command=lambda:test_zoom(canvas))
# button_test.pack()
window.mainloop()