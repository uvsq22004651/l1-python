import tkinter as tk
le_clic = tk.Tk()
le_clic.title("Clic")

def affichage(event):
    event.x, event.y
    x = event.x
    y = event.y
    canvas.create_line((x, y), (x + 1, y + 1), fill = 'red')

le_clic.bind("<Button-1>", affichage)

canvas = tk.Canvas(le_clic, width = 500, height = 500, bg = 'black')
canvas.grid(column = 0, row = 0)

le_clic.mainloop()