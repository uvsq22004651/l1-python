import tkinter as tk
import random as rd

couleur = tk.Tk()
couleur.title = 'Color'

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel():
    canvas.create_line((128, 128), (129, 128), fill = 'red')

def ecran_aleatoire():
    for a in range(256):
        for b in range(256):
            color = get_color(rd.randint(0, 255), rd.randint(0, 255),rd.randint(0, 255))
            canvas.create_line((a, b), (a + 1, b), fill = color)


def degrade_gris():
    for a in range(256):
        for b in range(256):
            color = get_color((a), (a), (a))
            canvas.create_line((a, b), (a + 1, b), fill = color)

def degrade_d():
    for a in range(256):
        for b in range(256):
            color = get_color((a), (0), (255 - a))
            canvas.create_line((a, b), (a + 1, b), fill = color)        

bouton_aleatoire = tk.Button(couleur, bg = 'white', fg = 'blue', text = 'Aléatoire', font = ('Times', '20'), command = ecran_aleatoire)
bouton_degrade_gris = tk.Button(couleur, bg = 'white', fg = 'blue', text = 'Dégardé gris', font = ('Times', '20'), command = degrade_gris)
bouton_degrade_2d = tk.Button(couleur, bg = 'white', fg = 'blue', text = 'Dégradé 2D', font = ('Times', '20'), command = degrade_d)

bouton_aleatoire.grid(column = 0, row = 0)
bouton_degrade_gris.grid(column = 0, row = 1)
bouton_degrade_2d.grid(column = 0, row = 2)


canvas = tk.Canvas(couleur, width = 256, height = 256, bg = 'black')
canvas.grid(column = 1, row = 0, rowspan = 3)

couleur.mainloop()