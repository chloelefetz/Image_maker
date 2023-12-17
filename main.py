import tkinter as tk 
from PIL import Image, ImageTk
import numpy as np
from Ouvrir_image import ouvrir_image
from sauvegarder import sauvegarder_image
from Luminosité import boite_luminosite
from filtres import *
from Rogner import rogner_image
from Redimentionner import boite_redimentionner
from pixeliser import boite_pixeliser
from Pipette import pipette
# from collage import boite_image2
from Retour import *
from tkinter import *
# from Rotation import rotation
# from Theme_image import theme_image

x1 = None
y1 = None
x2 = None
y2 = None

def click_gauche_canvas(event):
    """
    Récupère les coordonnées x, y de l'endroit où on à cliqué avec le clique gauche
    """
    global x1, y1
    x1 = event.x
    y1 = event.y

def click_droit_canvas(event):
    """
    Récupère les coordonnées x, y de l'endroit où on à cliqué avec le clique droit
    """
    global x2, y2
    x2 = event.x
    y2 = event.y


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
window.iconbitmap("logo.ico")
window.config(background="black")

#Création frame barre d'outils
frame_outil = tk.Frame(window, bg="gray", bd=1)
frame_outil.pack(side="left", fill="y")

#Ajouter du texte
text_outil = tk.Label(frame_outil, text = "Barre d'outils", font=("Arial", 10), fg="black")
text_outil.pack()

#Création d'une image vierge de taille 300x300px
width = 300
height = 300
canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()
photo = ImageTk.PhotoImage(file="vierge.png")
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Associe des actions aux evenement clique bouton gauche et bouton droit
canvas.bind("<Button-1>", click_gauche_canvas)
canvas.bind("<Button-3>", click_droit_canvas)

# création de l'indice pour la sauvegarde
# indice_temp = 0

# Création de la barre de menu
menuBar = Menu(window) 

# Création des menus dans le menu
menuFichier  = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Fichier",menu=menuFichier) 
menuCouleur  = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Couleur",menu=menuCouleur)
menuLuminosité  = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Luminosité",menu=menuLuminosité)
menuContraste  = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Contraste",menu=menuContraste)
menuCollage  = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Collage",menu=menuCollage)
menuPixeliser  = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Pixeliser",menu=menuPixeliser)
menuPosition  = Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Position",menu=menuPosition)

# Création des sous menus du menu
menuFichier.add_command(label="Ouvrir image", command=lambda:ouvrir_image(canvas)) 
menuFichier.add_command(label="Sauvegarder", command=sauvegarder_image) 
menuFichier.add_command(label="Quitter", command=quit) 
menuCouleur.add_command(label="Rouge") 
menuCouleur.add_command(label="Bleu") 
menuCouleur.add_command(label="Vert") 
menuCouleur.add_command(label="Inverser Couleurs", command=lambda:inverser_couleur_image(canvas)) 
menuLuminosité.add_command(label="Luminosité", command=lambda:boite_luminosite(canvas))
menuPixeliser.add_command(label="Pixeliser", command=lambda:boite_pixeliser(canvas))
# menuPosition.add_command(label="Rotation",  command=lambda:rotation(canvas)) 
menuPosition.add_command(label="Miroir", command=lambda:miroir(canvas))
menuPosition.add_command(label="Mirroir central", command=lambda:miroir_central(canvas)) 
menuPosition.add_command(label="Miroir vertical", command=lambda:miroir_vertical(canvas))
menuPosition.add_command(label="Miroir horizontal", command=lambda:miroir_horizontal(canvas))
 
# Configuration de la barre des menus
window.config(menu=menuBar)

#Créations boutons 
button_filtre = tk.Button(frame_outil, text="Inverser les couleurs", command=lambda:inverser_couleur_image(canvas))
button_filtre.pack()
# button_filtre = tk.Button(frame_outil, text="filtre rouge", command=lambda:rouge_image(canvas))
# button_filtre.pack()
button_rogner = tk.Button(frame_outil, text="Rogner", command=lambda:rogner_image(canvas))
button_rogner.pack()
button_redimentionner = tk.Button(frame_outil, text="Redimensionner", command=lambda:boite_redimentionner(canvas))
button_redimentionner.pack()
button_pipette = tk.Button(frame_outil, text="Pipette", command=lambda:pipette(x1, y1))
button_pipette.pack()
# button_collage = tk.Button(frame_outil, text="Collage", command=lambda:boite_image2(canvas))
# button_collage.pack()
button_collage = tk.Button(frame_outil, text="<-", command=lambda:retour_arriere(canvas))
button_collage.pack()
button_collage = tk.Button(frame_outil, text="->", command=lambda:retour_avant(canvas))
button_collage.pack()

button_test = tk.Button(frame_outil, text="TEST", command=test_image)
button_test.pack()



window.mainloop()
