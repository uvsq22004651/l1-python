import tkinter as tk
import random as rd
racine = tk.Tk()
racine.title('Dessin aléatoire')

couleur = 'yellow'

def carre():
    x = rd.randint(0, 450)
    y = rd.randint(0, 450)
    a = canvas.create_rectangle((x + 50, y + 50), (x, y), fill = couleur) 

def lignes():
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    b = canvas.create_line((x, y), (x + 100, y + 100), fill = couleur)
    c = canvas.create_line((x + 100, y), (x, 100 + y), fill = couleur)

def cercle():
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    d = canvas.create_oval((x + 100, y + 100), (x, y), fill = couleur)

def choix_couleur():
    global couleur
    couleur = input('Donnez  une couleur')

def undo():
    if len(canvas.find_all()) > 1:
        a = canvas.find_all()[-1]
        canvas.delete(a)
    elif len(canvas.find_all()) > 2:
        b = canvas.find_all()[-1]
        c = canvas.find_all()[-1]
        canvas.delete(b)
        canvas.delete(c)
    elif len(canvas.find_all()) > 1:
        d = canvas.find_all()[-1]
        canvas.delete(d)

bouton_choisir_couleur = tk.Button(racine, text = 'Choisir une couleur', fg = 'red', command = choix_couleur)
bouton_cercle = tk.Button(racine, text = 'Cercle', bg = 'MediumOrchid3', activebackground = 'cyan', command = cercle)
bouton_croix = tk.Button(racine, text = 'Croix', bg = 'MediumOrchid3', command = lignes)
bouton_carré = tk.Button(racine, text = 'Carré', bg = 'MediumOrchid3', command = carre)
bouton_undo = tk.Button(racine, text = 'Undo', bg = 'MediumOrchid3', command = undo)

bouton_choisir_couleur.grid(column = 1, row = 0)
bouton_cercle.grid(column = 0, row = 1)
bouton_croix.grid(column = 0, row = 2)
bouton_carré.grid(column = 0, row = 3)
bouton_undo.grid(column = 2, row = 0)


canvas = tk.Canvas(racine, width = 500, height = 500, bg = 'black', relief = 'sunken')
canvas.grid(column = 1, row = 1, rowspan = 3)

racine.mainloop()   