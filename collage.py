from PIL import Image, ImageTk, ImageDraw, ImageFilter
import tkinter as tk
from Ouvrir_image2 import *


def collage(canvas):
    """
    
    """

    global photo
    # Charge l'image ouverte par la fonction ouvrir_image et l'image ouverte par la fonction ouvrir_image2
    image_entrée = Image.open("image_temporaire2.png")
    image_sortie = image_entrée.copy()
    image_collé =  Image.open("image_temporaire3.png")
    image_sortie.paste(image_collé)
    image_sortie.show
    image_sortie.save("image_temporaire2.png")
    # mask_im = Image.new("L", image_collé.size, 0)
    # draw = ImageDraw.Draw(mask_im)
    # draw.ellipse((30, 20, 500, 500), fill=255)
    # mask_im.save('mask_circle.jpg')

    # mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(10))
    # mask_im_blur.save('mask_circle_blur.jpg')
    
    

    # Sauvegarde les images pour pouvoir les afficher
    
    # photo = ImageTk.PhotoImage(file="image_temporaire.png")
    # largeur_image = photo.width()
    # hauteur_image = photo.height()
    # canvas.config(width=largeur_image, height=hauteur_image)
    # canvas.create_image(0, 0, anchor=tk.NW, image=photo)



def boite_image2(canvas):
    """
    Création une nouvelle page tkinter
    bouton importer une image 
    """ 
    # Création d'une nouvelle fenetre tkinter
    fenetre_import = tk.Tk()
    fenetre_import.title("nouvelle image")

    # Créé un bouton pour importer une image
    button_import = tk.Button(fenetre_import, text="Importer l'image n°1", command=lambda:ouvrir_image2(canvas))
    button_import.pack()
    button_import = tk.Button(fenetre_import, text="Importer l'image n°2", command=lambda:ouvrir_image3(canvas))
    button_import.pack()
    fenetre_import.mainloop() 