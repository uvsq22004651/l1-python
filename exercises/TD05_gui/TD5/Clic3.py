import tkinter as tk
le_clic = tk.Tk()
le_clic.title("Clic")

nb_clic = 0
point = (0, 0)
color = 'green'

def affichage_point1(event):
    """ """
    global nb_clic, point, color
    if nb_clic == 0:
        nb_clic = 1
        point = (event.x, event.y)
        print(point)
    else:
        nb_clic = 0
        if (250 - event.x) * (250 - point[0]) >= 0:
            color = 'blue'
            print(point)
        else:
            color = 'red'
        print(event.x, event.y)
    canvas.create_line(point, (event.x, event.y),  fill = color)

le_clic.bind("<Button-1>", affichage_point1)

canvas = tk.Canvas(le_clic, width = 500, height = 500, bg = 'black')
canvas.grid()

canvas.create_line((250, 0), (250, 500), fill = 'white')

le_clic.mainloop()