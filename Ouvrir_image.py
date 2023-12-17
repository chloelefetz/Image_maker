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
        canvas.delete("all")
        image = Image.open(file_path).convert("RGBA")
        photo = ImageTk.PhotoImage(image)
        print("1")
        # photo = tk.PhotoImage(file=file_path)
        print("2")
        largeur_image = photo.width()
        hauteur_image = photo.height()
        print("3")
        canvas.config(width=largeur_image, height=hauteur_image)
        print("4")
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        print("5")
        
        print("6")
        image.save(f"image_temporaire.png")
        image.save(f"image_temporaire_1.png")