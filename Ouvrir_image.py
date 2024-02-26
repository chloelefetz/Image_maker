import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from Indice_image import index

def ouvrir_image(canvas):
    """
    Ouvre un fichier image present dans l'ordinateur
    Remplace le canva actuellement affichée par la nouvelle image
    Sauvegarde l'image au format RGBA dans un fichier image_temporaire
    """
    global photo
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])
    if file_path:
        for i in range(10000):
            if path.isfile(f"image_temporaire_{i}.png"):
                remove(f"image_temporaire_{i}.png")
                
        canvas.delete("all")
        image = Image.open(file_path).convert("RGBA")
        photo = ImageTk.PhotoImage(image)
        # photo = tk.PhotoImage(file=file_path)
        largeur_image = photo.width()
        hauteur_image = photo.height()
        canvas.config(width=largeur_image, height=hauteur_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        nouveau_texte = "\nRésolution\nLargeur : " + str(largeur_image) + "px\nHauteur : " + str(hauteur_image) + "px"
        text_resolution.config(text=nouveau_texte)
        d.indice_temp = 0
        image.save(f"image_temporaire_{d.indice_temp}.png")
        d.indice_temp += 1
