from globale import zoom
import tkinter as tk 
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
from os import remove, path
from PIL import Image, ImageTk
from supprimer_selection import boite_supprimer
from Flouter_selection import boite_flouter_selection
from Flouter_image import boite_flouter

for i in range(10000):
    if path.isfile(f"temporaire\image_temporaire_{i}.png"):
        remove(f"temporaire\image_temporaire_{i}.png")

d = info_image()

def clic_gauche_canvas(event, text_selectionG, d):
    """
    Récupère les coordonnées x, y de l'endroit où on à cliqué avec le clique gauche
    """
    d.x1 = int(event.x/zoom[0])
    d.y1 = int(event.y/zoom[0])
    pipette(d.x1, d.y1, text_pipette, d)
    nouveau_texte = "\nCoordonnées clique gauche\nx : " + str(d.x1) + "/ y : " + str(d.y1)
    text_selectionG.config(text=nouveau_texte)

def clic_droit_canvas(event, text_selectionD, d):
    """
    Récupère les coordonnées x, y de l'endroit où on à cliqué avec le clique droit
    """
    d.x2 = int(event.x/zoom[0])
    d.y2 = int(event.y/zoom[0])
    pipette(d.x2, d.y2, text_pipette, d)
    nouveau_texte = "\nCoordonnées clique droit\nx : " + str(d.x2) + "/ y : " + str(d.y2)
    text_selectionD.config(text=nouveau_texte)

# ------------------------------------------ Mise en page de l'appareil photo ------------------------------------------
    
# Création de la fenêtre principale
window = tk.Tk()
window.title("Application")
window.geometry("1024x768")
window.iconbitmap("image_logiciel\logo.ico")
window.config(background="black")

# Création d'une frame avec couleur de fond de la largeur totale de la grille pour remplir les espaces entre les images
frame_row0 = tk.Frame(window, bg="white", height=70, bd=0)
frame_row0.grid(row=0, column=0, columnspan=3, sticky="ew")
frame_row1 = tk.Frame(window, bg="lightgray", height=77, bd=0)
frame_row1.grid(row=1, column=0, columnspan=3, sticky="ew")
frame_row3 = tk.Frame(window, bg="lightgray", height=34, bd=0)
frame_row3.grid(row=3, column=0, columnspan=3, sticky="ew")

# Chargement des images de l'appareil photo
image1 = tk.PhotoImage(file="image_logiciel\_appareil00.png")
image2 = tk.PhotoImage(file="image_logiciel\_appareil01.png")
image3 = tk.PhotoImage(file="image_logiciel\_appareil02.png")
image4 = tk.PhotoImage(file="image_logiciel\_appareil10.png")
image5 = tk.PhotoImage(file="image_logiciel\_appareil11.png")
image6 = tk.PhotoImage(file="image_logiciel\_appareil12.png")
image7 = tk.PhotoImage(file="image_logiciel\_appareil30.png")
image8 = tk.PhotoImage(file="image_logiciel\_appareil32.png")

# Création des widgets Label pour les images de l'appareil photo
label1 = tk.Label(window, image=image1, bd=0)
label2 = tk.Label(window, image=image2, bd=0)
label3 = tk.Label(window, image=image3, bd=0)
label4 = tk.Label(window, image=image4, bd=0)
label5 = tk.Label(window, image=image5, bd=0)
label6 = tk.Label(window, image=image6, bd=0)
label7 = tk.Label(window, image=image7, bd=0)
label8 = tk.Label(window, image=image8, bd=0)

# Positionnement des images de l'appareil photo dans les colonnes et lignes correspondant
label1.grid(row=0, column=0, padx=0, pady=0) 
label2.grid(row=0, column=1, padx=0, pady=0)  
label3.grid(row=0, column=2, padx=0, pady=0)
label4.grid(row=1, column=0, padx=0, pady=0)  
label5.grid(row=1, column=1, padx=0, pady=0)  
label6.grid(row=1, column=2, padx=0, pady=0)
label7.grid(row=3, column=0, padx=0, pady=0) 
label8.grid(row=3, column=2, padx=0, pady=0)

# Définir la taille pour les colonnes et lignes de la grille
window.grid_columnconfigure(0, weight=0, minsize=25)
window.grid_columnconfigure(2, weight=0, minsize=25)
window.grid_columnconfigure(1, weight=1)  #weight=1 signifie que la cellule prend la place restante
window.grid_rowconfigure(0, weight=0, minsize=25)
window.grid_rowconfigure(1, weight=0, minsize=25)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=0, minsize=25)

# ------------------------------------------ Mise en place des frames outils et informations ------------------------------------------

#Création de la frame barre d'outils
frame_outil = tk.Frame(window, bg="darkgray", bd=0, highlightthickness=0)
frame_outil.grid(row=2, column=0, sticky="nsw")

#Création de la frame informations
frame_infos = tk.Frame(window, bg="darkgray", bd=0, highlightthickness=0)
frame_infos.grid(row=2, column=2, sticky="nse", padx=0, pady=0)

#Ajout de texte dans frame outils et frame informations
text_outil = tk.Label(frame_outil, text = "\n Barre d'outils \n", font=("Arial", 10, "bold", "underline"), fg="black", width=20, bg="darkgray")
text_outil.pack()
text_infos = tk.Label(frame_infos, text = "\n Informations", font=("Arial", 10, "bold", "underline"), fg="black", width=20, bg="darkgray")
text_infos.pack()
text_resolution = tk.Label(frame_infos, text = "\nRésolution\nLargeur : nd\nHauteur : nd", font=("Arial", 10), fg="black", width=20, bg="darkgray")
text_resolution.pack()
text_selectionG = tk.Label(frame_infos, text = "\nCoordonnées clique gauche\nx : nd / y : nd", font=("Arial", 10), fg="black", width=20, bg="darkgray")
text_selectionG.pack()
text_selectionD = tk.Label(frame_infos, text = "\nCoordonnées clique droit\nx : nd / y : nd", font=("Arial", 10), fg="black", width=20, bg="darkgray")
text_selectionD.pack()
text_pipette = tk.Label(frame_infos, text = "\nCouleur selectionnée\nR : nd\nV : nd\nB : nd\nA : nd", font=("Arial", 10), fg="black", width=20, bg="darkgray")
text_pipette.pack()

# Insertion image décorative d'un bouton directionnel
image_directionnel = tk.PhotoImage(file="image_logiciel\_bouton_directionnel.png")
label_directionnel = tk.Label(frame_infos, image=image_directionnel, bd=0, bg="darkgray")
label_directionnel.pack(side="bottom")


#Création d'une image vierge de taille 300x300px
width = 300
height = 300
canvas = tk.Canvas(window, width=width, height=height, borderwidth=0, highlightthickness=0)
canvas.grid(row=2, column=1)
photo = ImageTk.PhotoImage(file="image_logiciel\_vierge.png")
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Associe des actions aux evenement clique bouton gauche et bouton droit
canvas.bind("<Button-1>", lambda event:clic_gauche_canvas(event, text_selectionG, d))
canvas.bind("<Button-3>", lambda event:clic_droit_canvas(event, text_selectionD, d))

# Création de la barre de menu
menuBar = tk.Menu(window) 

# Création des différents menus dans le menu
menuFichier  = tk.Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Fichier",menu=menuFichier) 
menuCouleur  = tk.Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Couleur",menu=menuCouleur)
menuControleImage = tk.Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Contrôle d'image",menu=menuControleImage)
menuCollage  = tk.Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Collage",menu=menuCollage)
menuEffets  = tk.Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Effets avancés",menu=menuEffets)
menuPosition  = tk.Menu(menuBar, tearoff = 0) 
menuBar.add_cascade(label="Position",menu=menuPosition)
menuRedimensionner = tk.Menu(menuBar, tearoff = 0 )
menuBar.add_cascade(label="Redimensionner", menu=menuRedimensionner, command=lambda: boite_redimentionner(canvas, text_resolution, d))

# Création des sous menus du menu
menuFichier.add_command(label="Ouvrir image", command=lambda:ouvrir_image(canvas, text_resolution, slider, d))
menuFichier.add_command(label="Sauvegarder", command=lambda:sauvegarder_image(canvas, d)) 
menuFichier.add_command(label="Quitter", command=quit) 
menuCouleur.add_command(label="Rouge", command=lambda:boite_rouge(canvas, d))
menuCouleur.add_command(label="Vert", command=lambda:boite_verte(canvas, d))
menuCouleur.add_command(label="Bleu", command=lambda:boite_bleu(canvas, d))
menuCouleur.add_command(label="Cyan", command=lambda:boite_cyan(canvas, d))
menuCouleur.add_command(label="Jaune", command=lambda:boite_jaune(canvas, d))
menuCouleur.add_command(label="Magenta", command=lambda:boite_magenta(canvas, d))
menuCouleur.add_command(label="Inverser Couleurs", command=lambda:boite_inverser_couleur(canvas, d))
menuCouleur.add_command(label="Noir et Blanc", command=lambda:boite_gris(canvas, d))
menuCouleur.add_command(label="Sépia", command=lambda:boite_sepia(canvas, d))
menuControleImage.add_command(label="Luminosité", command=lambda:boite_luminosite(canvas, d))
menuControleImage.add_command(label="Contraste", command=lambda:boite_contraste(canvas, d))
menuControleImage.add_command(label="Transparence", command=lambda:boite_transparence(canvas, d))
menuCollage.add_command(label="Tampon", command=lambda:boite_tampons(canvas, d))
menuCollage.add_command(label="Fond", command=lambda:boite_fond(canvas, d))
menuEffets.add_command(label="Pixeliser", command=lambda:boite_pixeliser(canvas, d))
menuEffets.add_command(label="Flouter", command=lambda:boite_flouter(canvas, d))
menuPosition.add_command(label="Rotation",  command=lambda:boite_rotation(canvas, d)) 
menuPosition.add_command(label="Miroir vertical", command=lambda:boite_miroir_vertical(canvas, d))
menuPosition.add_command(label="Miroir horizontal", command=lambda:boite_miroir_horizontal(canvas, d))
menuPosition.add_command(label="Symetrie centrale", command=lambda:boite_symetrie_centrale(canvas, d))
menuPosition.add_command(label="Symetrie verticale", command=lambda:boite_symetrie_verticale(canvas, d))
menuPosition.add_command(label="Symetrie horizontale", command=lambda:boite_symetrie_horizontale(canvas, d))
menuRedimensionner.add_command(label="Redimensionner", command=lambda:boite_redimentionner(canvas, text_resolution, d))

# Configuration de la barre des menus
window.config(menu=menuBar)

# Créations des boutons dans la frame outils
image_retour = Image.open("image_logiciel\_fleche_retour.png")
photo_retour = ImageTk.PhotoImage(image_retour)
button_collage = tk.Button(frame_outil, text = " Retour", image=photo_retour, compound=tk.LEFT, width=150, bg="lightgray", anchor = "w", command=lambda:retour_arriere(canvas, d))
button_collage.pack()
image_retour_debut = Image.open("image_logiciel\_fleche_retour_debut.png")
photo_retour_debut = ImageTk.PhotoImage(image_retour_debut)
button_collage = tk.Button(frame_outil, text = " Revenir à l'originale", image=photo_retour_debut, compound=tk.LEFT, width=150, bg="lightgray", anchor = "w", command=lambda:retour_debut(canvas, d))
button_collage.pack()
image_rogner = Image.open("image_logiciel\_rogner.png")
photo_rogner = ImageTk.PhotoImage(image_rogner)
button_rogner = tk.Button(frame_outil, text = " Rogner", image=photo_rogner, compound=tk.LEFT, width=150, bg="lightgray", anchor = "w", command=lambda:boite_rogner_image(canvas, d))
button_rogner.pack()
image_supprimer_selection = Image.open("image_logiciel\_supprimer.png")
photo_supprimer_selection = ImageTk.PhotoImage(image_supprimer_selection)
button_supprimer_selection = tk.Button(frame_outil, text = " Supprimer la séléction", image=photo_supprimer_selection, compound=tk.LEFT, width=150, bg="lightgray", anchor = "w", command=lambda:boite_supprimer(canvas, d))
button_supprimer_selection.pack()
image_flouter = Image.open("image_logiciel\_flouter.png")
photo_flouter = ImageTk.PhotoImage(image_flouter)
button_flouter = tk.Button(frame_outil, text = " Flouter la séléction", image=photo_flouter, compound=tk.LEFT, width=150, bg="lightgray", anchor = "w", command=lambda:boite_flouter_selection(canvas, d))
button_flouter.pack()


# Création d'un slider pour régler le zoom de l'image 
slider = tk.Scale(frame_outil, from_=10, to=200, orient="horizontal", bg="darkgray", bd=0, highlightthickness=0)
slider.pack(padx=10, pady=(0, 30), side="bottom")
label_zoom = tk.Label(frame_outil, text="Zoom : ", bg="darkgray", font=("Arial", 10, "bold", "underline"))
label_zoom.pack(side="bottom")
slider.set(100)
slider.bind("<ButtonRelease-1>", lambda event: on_entry_change(event, canvas, d)) # <ButtonRelease-1> = l'utilisateur relache le bouton 1

# ------------------------------------------ Affichage de la fenêtre window ------------------------------------------

window.mainloop()