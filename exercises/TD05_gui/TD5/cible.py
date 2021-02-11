import tkinter as tk

racine = tk.Tk()
racine.title("Cible") 
taille = 500
epeseur = taille //100
couleur = ['blue', 'green', 'black', 'yellow', 'magenta', 'red']
canvas = tk.Canvas(racine, width=taille, height=taille, bg="black", relief="sunken")
canvas.grid(column = 0, row = 0)
for i in range(65):
    canvas.create_oval((epeseur *i,  epeseur *i), (taille-i * epeseur, taille-i * epeseur), fill= couleur[i % len(couleur)])
racine.mainloop()