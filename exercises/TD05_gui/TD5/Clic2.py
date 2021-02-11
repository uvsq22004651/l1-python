import tkinter as tk
le_clic = tk.Tk()
le_clic.title("Clic")

def affichage_cercle_droit(event):
    event.x, event.y
    x = event.x
    y = event.y
    if x > 250:
        canvas.create_oval((x + 25, y + 25), (x - 25, y - 25 ), fill = 'red')
    else:
        canvas.create_oval((x + 25, y + 25), (x - 25, y - 25 ), fill = 'blue')
        
le_clic.bind('<Button-1>', affichage_cercle_droit)

canvas = tk.Canvas(le_clic, width = 500, height = 500, bg = 'black')
canvas.grid(column = 0, row = 0)

canvas.create_line((250, 0), (250, 500), fill = 'white')

le_clic.mainloop()