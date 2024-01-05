import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
from globale import zoom

def affiche_zoom(canvas):
    global zoom
    global photo
    image_entrée = Image.open("image_temporaire.png")
    canvas.delete("all")
    new_width = int(image_entrée.width*zoom)
    new_height = int(image_entrée.height*zoom)
    resized_image = image_entrée.resize((new_width, new_height), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=new_width, height=new_height)
    # photo = ImageTk.PhotoImage(image_entrée)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def zoom_in(canvas):
    global zoom
    zoom = zoom*1.2
    affiche_zoom(canvas)

def zoom_out(canvas):
    global zoom
    zoom = zoom*0.8
    affiche_zoom(canvas)