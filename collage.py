from PIL import Image, ImageTk
import tkinter as tk
from globale import zoom
from tkinter import filedialog
from Info_image import info_image

def choix_tampons(d):
    file_path = filedialog.askopenfilename(initialdir="tampons/")
    d.choix = str(file_path)

def boite_tampons(canvas, d):
    """
    Créé une fenêtre "Symetrie verticale" avec un bouton valider qui lance la fonction symetrie_verticale
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """

    # création d'une nouvelle fenetre
    fenetre_collage = tk.Toplevel()
    fenetre_collage.title("Collage")
    fenetre_collage.resizable(width=False, height=False)
    fenetre_collage.geometry("560x280+50+650")
    fenetre_collage.attributes('-topmost', True)

    # choix du tampon
    text_tampon = tk.Label(fenetre_collage, text="1) Choissisez votre tampon :")
    text_tampon.pack()
    choix = tk.StringVar()
    choix.set(f"{d.choix}")
    text = tk.Label(fenetre_collage, textvariable=choix)
    text.pack()
    bouton_choix = tk.Button(fenetre_collage, text="choix", command=lambda:(choix_tampons(d), choix.set(f"{d.choix}")))
    bouton_choix.pack()

    # choix taille du tampon

    text_longeur = tk.Label(fenetre_collage, text="2) Choissisez la longeur de votre tampon : ")
    text_longeur.pack()
    longeur = tk.Entry(fenetre_collage)
    longeur.pack()
    a = tk.Label(fenetre_collage, text="Choissisez la largeur de votre tampon :")
    a.pack()    
    largeur = tk.Entry(fenetre_collage)
    largeur.pack() 
    # text_emplacement = tk.Label(fenetre_collage, text="3) Choissisez la position du tampon en effectuant un click gauche de la souris sur l'image : ")
    # text_emplacement.pack()

    # Création d'une frame 
    frame1 = tk.Frame(fenetre_collage)
    frame1.pack(padx=3, pady=3)
    img1 = Image.open("image_logitiel\clic_gauche.png").convert("RGBA")
    img_exemple1 = ImageTk.PhotoImage(img1)
    # Créer un label pour afficher l'image du clic gauche
    image_label1 = tk.Label(frame1, image=img_exemple1)
    image_label1.pack(side=tk.LEFT, padx=3, pady=3)
    # Créer la zone de texte
    texte1 = "3) Choissisez la position du tampon en effectuant un click gauche de la souris sur l'image "
    texte_label1 = tk.Label(frame1, text=texte1)
    texte_label1.pack(side=tk.LEFT, padx=3, pady=3)


    # Création d'un bouton valider
    bouton_valider = tk.Button(fenetre_collage, text="Valider", command=lambda:(tampons(canvas, d, longeur, largeur), fenetre_collage.destroy()))
    bouton_valider.pack()
    fenetre_collage.mainloop()

    # Charger une image d'exemple
    # img = Image.open("image_logitiel\chiens_sym_verticale.png").convert("RGBA")
    # img_exemple = ImageTk.PhotoImage(img)

    # Créer un label pour afficher l'image exemple
    # image_label = tk.Label(fenetre_collage, image=img_exemple)
    # image_label.pack()
    


def tampons(canvas, d, longeur, largeur):
    """
    
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")

    image2 = Image.open(d.choix).convert("RGBA")
    image = image_entrée.convert("RGBA")
    image2 = image2.resize((int(longeur.get()),int(largeur.get())))


    image.alpha_composite(image2, dest=(d.x1 - image2.width // 2, d.y1 - image2.height // 2))

    # Sauvegarde les images pour pouvoir les afficher
    image.save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logitiel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)

    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1




def choix_fond(d):
    file_path = filedialog.askopenfilename(initialdir="fond/")
    d.choix = str(file_path)

def boite_fond(canvas, d):
    """
    Créé une fenêtre "Symetrie verticale" avec un bouton valider qui lance la fonction symetrie_verticale
    Cette fenêtre contient un exemple de l'utilité de la fonction
    """

    # création d'une nouvelle fenetre
    fenetre_collage = tk.Toplevel()
    fenetre_collage.title("Collage")
    fenetre_collage.resizable(width=False, height=False)
    fenetre_collage.geometry("550x170+50+650")
    fenetre_collage.attributes('-topmost', True)

    # choix du fond
    text_fond = tk.Label(fenetre_collage, text="1) Choissisez votre fond :")
    text_fond.pack()
    choix = tk.StringVar()
    choix.set(None)
    text = tk.Label(fenetre_collage, textvariable=choix)
    text.pack()
    bouton_choix = tk.Button(fenetre_collage, text="choix", command=lambda:(choix_fond(d), choix.set(f"{d.choix}")))
    bouton_choix.pack()


    # Création d'un bouton valider
    bouton_valider = tk.Button(fenetre_collage, text="Valider", command=lambda:(fond(canvas, d), fenetre_collage.destroy()))
    bouton_valider.pack()
    fenetre_collage.mainloop()

    # Charger une image d'exemple
    # img = Image.open("image_logitiel\chiens_sym_verticale.png").convert("RGBA")
    # img_exemple = ImageTk.PhotoImage(img)

    # Créer un label pour afficher l'image exemple
    # image_label = tk.Label(fenetre_collage, image=img_exemple)
    # image_label.pack()
    


def fond(canvas, d):
    """
    
    """
    global photo
    # Charge l'image ouverte par la fonction ouvrir_image
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png")

    image2 = Image.open(f"{d.choix}")
    image_entrée = image_entrée.convert("RGBA")
    image2 = image2.convert("RGBA").resize(image_entrée.size)
    image = Image.alpha_composite(image2, image_entrée)

    # Sauvegarde les images pour pouvoir les afficher
    image.save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1