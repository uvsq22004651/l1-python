#  import tkinter as tk dans ce cas, il faut prefixer avec tk.

from tkinter import * 
racine = Tk()


def draw_pixel(event):
    canvas.create_line( (event.x, event.y), (event.x + 1, event.y), fill = 'red')


canvas = Canvas(racine , width=500, hight=500, bg="black", relief="sunken")
canvas.bind("<Button-1>", draw_pixel)
canvas.grid()
racine.mainloop()

from tkinter import * 
racine = Tk()


def draw_cercle(event):
    if event.x < 250:
         color = 'blue'
    else:
        color = 'red'
    canvas.create_oval(( event.x- 50,  event.y - 50), ( event.x + 50, event.y + 50), fill = color)

canvas = Canvas(racine , width=500, hight=500, bg="black", relief="sunken")
canvas.create_line( (250, 0), (250, 500), fill = 'white')
canvas.bind("<Button-1>", draw_cercle)
canvas.grid()
racine.mainloop()

from tkinter import * 
racine = Tk()
nb_clic = 0
point = (0, 0)

def draw_line(event):
    global nb_clic, point
    if nb_clic == 0:
        nb_clic = 1
        point = (event.x, event.y)
    else:
        nb_clic = 0

        if (250 - event.x) * (250 - point[0]) >= 0:

             color = 'blue'

        else:

            color = 'red'

    canvas.create_line(point, (event.x, event.y),  fill = color)

canvas = Canvas(racine , width=500, height=500, bg="black", relief="sunken")
canvas.create_line( (250, 0), (250, 500), fill = 'white')
canvas.bind("<Button-1>", draw_line)
canvas.grid()
racine.mainloop()