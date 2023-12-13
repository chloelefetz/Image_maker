from tkinter import filedialog
from PIL import Image
import os

def sauvegarder_image():
    """
    Ouvre impage_temporaire.png
    Sauvegarde une copie avec le nom choisi
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")]) 
    if file_path:
        image = Image.open("image_temporaire.png")
        image.save(file_path)
        os.remove("image_temporaire.png")