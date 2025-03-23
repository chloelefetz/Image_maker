from PIL import Image, ImageTk
import tkinter as tk
from globale import zoom
import numpy as np

def choix_tampons(d):
    """
    Ouvre la fenêtre pour choisir le fichier qui va servir de tampon
    """
    file_path = tk.filedialog.askopenfilename(initialdir="tampons/")
    d.choix = str(file_path)

def boite_tampons(canvas, d):
    """
    Créé une fenêtre "Collage" avec un bouton valider qui lance la fonction tampons\n
    Cette fenêtre contient :\n
    - un exemple de l'utilité de la fonction\n
    - Le choix de l'image qui va servir de tampon \n
    - Le choix de la taille du tampon \n
    - L'emplcement du tampon est déterminé par l'emplacement du clic gauche sur le canvas
    """

    # création d'une nouvelle fenetre
    fenetre_collage = tk.Toplevel()
    fenetre_collage.title("Collage")
    fenetre_collage.iconbitmap("image_logiciel\logo.ico")
    fenetre_collage.resizable(width=False, height=False)
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
    text_hauteur = tk.Label(fenetre_collage, text="2) Choissisez la hauteur de votre tampon : ")
    text_hauteur.pack()
    hauteur = tk.Entry(fenetre_collage)
    hauteur.pack()
    a = tk.Label(fenetre_collage, text="Choissisez la largeur de votre tampon :")
    a.pack()    
    largeur = tk.Entry(fenetre_collage)
    largeur.pack() 

    # Création de la frame pour pouvoir avoir une image et du texte côte à côte  
    frame1 = tk.Frame(fenetre_collage)
    frame1.pack(padx=3, pady=3)
    img1 = Image.open("image_logiciel\clic_gauche.png").convert("RGBA")
    img_exemple1 = ImageTk.PhotoImage(img1)
    # Créer un label pour afficher l'image du clic gauche
    image_label1 = tk.Label(frame1, image=img_exemple1)
    image_label1.pack(side=tk.LEFT, padx=3, pady=3)
    # Créer la zone de texte
    texte1 = "3) Choissisez la position du tampon en effectuant un click gauche de la souris sur l'image "
    texte_label1 = tk.Label(frame1, text=texte1)
    texte_label1.pack(side=tk.LEFT, padx=3, pady=3)

    # Création d'un bouton valider
    bouton_valider = tk.Button(fenetre_collage, text="Valider", command=lambda:(tampons(canvas, d, hauteur, largeur), fenetre_collage.destroy()))
    bouton_valider.pack()

    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_tampon.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_collage, image=img_exemple)
    image_label.pack()

    fenetre_collage.mainloop()
    

def tampons(canvas, d, hauteur, largeur):
    """
    Remplace les valeurs de l'image d'entrée par celle de l'image tampon à l'endroit où le tampon doit apparaitre \n
    Tient compte de la transparence du tampon \n
    Tient compte des zones du tampon qui depassent de l'image d'entrée
    """
    global photo

    # Récupère la largeur et hauteur du tampon sous forme de chiffre 
    largeur = int(largeur.get())    
    hauteur = int(hauteur.get())
    # Charge l'image ouverte par la fonction ouvrir_image
    image = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png").convert("RGBA")
    image2 = Image.open(d.choix).convert("RGBA")
    image2 = image2.resize((largeur,hauteur), Image.Resampling.LANCZOS)

    # Crée des tableaux numpy avec l'image et le tampon
    image_np = np.asarray(image)
    image_sortie = np.copy(image_np)
    tampon = np.asarray(image2)
    image2_np = np.copy(tampon)

    # Calcul les coordonnées où commence et fini le tampon
    debut_x = d.x1-largeur//2
    debut_y = d.y1-hauteur//2
    fin_x = debut_x + largeur
    fin_y = debut_y + hauteur

    if debut_x < 0 :
        image2_np = image2_np[:, abs(debut_x):]
        debut_x = 0
    
    if debut_y < 0 :
        image2_np = image2_np[abs(debut_y):,:]
        debut_y = 0
    
    if fin_x > image.width-1 :
        image2_np = image2_np[:, :image.width - fin_x]
        fin_x = image.width
    
    if fin_y > image.height-1 :
        image2_np = image2_np[:image.height - fin_y,:]
        fin_y = image.height

    # Calcul l'image finiale en tenant compte de la transparence
    image_temporaire = image_np[debut_y : fin_y, debut_x : fin_x,:]
    image_transparence = image2_np[:,:,3]/255
    image_resultat = np.empty(image2_np.shape)
    image_resultat[:,:,0] = image_temporaire[:,:,0]*(1-image_transparence)+image2_np[:,:,0]*image_transparence
    image_resultat[:,:,1] = image_temporaire[:,:,1]*(1-image_transparence)+image2_np[:,:,1]*image_transparence
    image_resultat[:,:,2] = image_temporaire[:,:,2]*(1-image_transparence)+image2_np[:,:,2]*image_transparence
    image_resultat[:,:,3] = np.maximum(image2_np[:,:,3], image_temporaire[:,:,3])
    
    image_sortie[debut_y : fin_y, debut_x : fin_x,:] = image_resultat

    # Sauvegarde les images pour pouvoir les afficher
    Image.fromarray(image_sortie).save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    
    # Charge l'image modifiée
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logiciel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)
    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    # Affiche le résultat final avec le zoom et la grille
    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1




def choix_fond(d):
    """
    Ouvre la fenêtre pour choisir le fichier qui va servir de fond
    """
    file_path = tk.filedialog.askopenfilename(initialdir="fond/")
    d.choix = str(file_path)

def boite_fond(canvas, d):
    """
    Créé une fenêtre "Choix fond" \n
    Elle contient : \n
    - Un bouton pour choisir l'image à mettre en fond\n
    - Un bouton valider qui lance la fonction fond\n
    - Un exemple de l'utilité de la fonction
    """

    # création d'une nouvelle fenetre
    fenetre_collage = tk.Toplevel()
    fenetre_collage.title("Choix fond")
    fenetre_collage.iconbitmap("image_logiciel\logo.ico")
    fenetre_collage.resizable(width=False, height=False)
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
    
    # Charger une image d'exemple
    img = Image.open("image_logiciel\sportif_fond.png").convert("RGBA")
    img_exemple = ImageTk.PhotoImage(img)
    # Créer un label pour afficher l'image exemple
    image_label = tk.Label(fenetre_collage, image=img_exemple)
    image_label.pack()

    fenetre_collage.mainloop()
    


def fond(canvas, d):
    """
    Remplace les pixels de l'image par ceux du fond là où l'image est transparente\n
    Ajuste les dimmentions du fond
    """
    global photo

    # Charge l'image ouverte par la fonction ouvrir_image
    image = Image.open(f"temporaire\image_temporaire_{d.indice_temp - 1}.png").convert("RGBA")
    image2 = Image.open(d.choix).convert("RGBA")
    image2 = image2.resize((image.width, image.height), Image.Resampling.LANCZOS)

    # Crée des tableaux numpy avec l'image et le fond
    image_np = np.asarray(image)
    image_sortie = np.copy(image_np)
    fond = np.asarray(image2)
    image2_np = np.copy(fond)

    # Calcul l'image finiale en tenant compte de la transparence
    image_transparence = image_np[:,:,3]/255
    image_resultat = np.empty(image2_np.shape)
    image_resultat[:,:,0] = image_sortie[:,:,0]*image_transparence+image2_np[:,:,0]*(1-image_transparence)
    image_resultat[:,:,1] = image_sortie[:,:,1]*image_transparence+image2_np[:,:,1]*(1-image_transparence)
    image_resultat[:,:,2] = image_sortie[:,:,2]*image_transparence+image2_np[:,:,2]*(1-image_transparence)
    image_resultat[:,:,3] = np.maximum(image2_np[:,:,3], image_sortie[:,:,3])

    image_sortie = image_resultat

    # Sauvegarde les images pour pouvoir les afficher
    image_sortie = (image_sortie).astype(np.uint8)
    Image.fromarray(image_sortie).save(f"temporaire\image_temporaire_{d.indice_temp}.png")
    
    # Charge l'image modifiée
    image_entrée = Image.open(f"temporaire\image_temporaire_{d.indice_temp}.png")

    # grille de transparence image png
    grille = Image.open('image_logiciel\grille.png')
    image_entrée = image_entrée.convert("RGBA")
    grille = grille.convert("RGBA").resize(image_entrée.size)
    # Superposer l'image sur la grille
    image_entrée = Image.alpha_composite(grille, image_entrée)

    # Affiche le résultat final avec le zoom et la grille
    canvas.delete("all")
    largeur_image = int(image_entrée.width*zoom[0])
    hauteur_image = int(image_entrée.height*zoom[0])
    resized_image = image_entrée.resize((largeur_image, hauteur_image), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.config(width=largeur_image, height=hauteur_image, borderwidth=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    d.indice_temp += 1