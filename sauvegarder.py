import tkinter as tk 
from PIL import Image, ImageTk
from os import remove, path
import numpy as np

def sauvegarder_image(canvas, d):
    """
    Ouvre image_temporaire.png\n
    Sauvegarde une copie avec le nom choisi
    """
    global photo
    file_path = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")]) 
    if file_path:
        # Ouvre la dernière image temporaire et la sauvegarde dans le chemin indiqué
        image = Image.open(f"temporaire\image_temporaire_{d.indice_temp-1}.png")
        image.save(file_path)

        # Efface l'image affichée et remet le fond noir vierge
        canvas.delete("all")
        photo = ImageTk.PhotoImage(file="image_logiciel\_vierge.png")
        largeur_image = photo.width()
        hauteur_image = photo.height()
        canvas.config(width=largeur_image, height=hauteur_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)

        # Supprime les fichiers temporaires
        for i in range(10000):
            if path.isfile(f"temporaire\image_temporaire_{i}.png"):
                remove(f"temporaire\image_temporaire_{i}.png")