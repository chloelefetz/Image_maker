import tkinter as tk
from PIL import Image, ImageTk
from globale import zoom

def affiche_zoom(canvas,d):
    """
    Affiche l'image avec un niveau de zoom conforme à celui choisi par le slider
    """
    global photo
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png").convert("RGBA")

    # grille de transparence image png
    grille = Image.open('image_logiciel\grille.png')
    grille = grille.convert("RGBA").resize(image_entrée.size)
    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    # Affiche le résultat final avec le zoom et la grille
    canvas.delete("all")
    new_width = int(image_entrée.width*zoom[0])
    new_height = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((new_width, new_height), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=new_width, height=new_height, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

def on_entry_change(event, canvas, d):
    """
    La fonction prend en paramètre "event" qui est un evenement de tkinter\n
    Met à jour la valeur du slider quand on appuie sur entrer
    """
    value = event.widget.get()
    zoom[0] = value / 100
    affiche_zoom(canvas, d)