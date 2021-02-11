import tkinter as tk
import random as rd


noel = tk.Tk()
noel.title("Sapin de Noël")
noel.geometry("1920x1080")

def sapin():
    canvas.create_polygon((1100, 900), (600, 900), (850, 350), fill = "forest green")
    canvas.create_rectangle((900, 900), (800, 1000), fill = "brown")

def guirlande():
    canvas.create_line((1100, 900), (650, 800), (1008, 700), (740,600), (920, 500), (805, 450), width = 3, fill = "blue")

def boule():
    x = rd.randint(600, 1100)
    y = rd.randint(350, 900)
    canvas.create_oval((x + 30, y + 30), (x + 10, y + 10), fill = "red")

def etoile():
    canvas.create_polygon((850, 250), (840, 350), (750, 360), (840, 370), (850, 450), (860, 370), (950, 360), (860, 350), fill = "yellow")
    
    
boutton_sapin = tk.Button(noel, text = "Sapin", bg = "RoyalBlue1", command = sapin)
boutton_guirlande = tk.Button(noel, text = "Guirlande", bg = "red", command = guirlande)
boutton_boule = tk.Button(noel, text = "Boule", bg = "gold3", command = boule)
boutton_etoile = tk.Button(noel, text = "étoile", bg = "yellow", command = etoile)

boutton_sapin.grid(column = 0, row = 0)
boutton_guirlande.grid(column = 1, row = 0)
boutton_boule.grid(column = 2, row = 0)
boutton_etoile.grid(column = 3, row = 0)


canvas = tk.Canvas(noel, width = 1700, height = 1000, bg = "black")
canvas.grid(column = 1, row = 1)

noel.mainloop()