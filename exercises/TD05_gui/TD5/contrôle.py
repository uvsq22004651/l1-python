import tkinter as tk

window = tk.Tk()

boutton_pause = tk.Button(window, text = "Pause", bg = "RoyalBlue1")
canvas = tk.Canvas(width = 600, height = 600, bg = 'black')

canvas.create_rectangle((340, 340), (260, 260), fill = 'blue')

def affichage1(event):
    event.x, event.y
    x = event.x
    y = event.y
    if 260 < x < 340 and 260 < y < 340:
        canvas.create_rectangle((335, 335), (265, 265), fill = 'red')

window.bind("<Button-1>", affichage1)

def affichage2(event):
    event.x, event.y
    x = event.x
    y = event.y
    if 360 > x > 240 and 360 > y > 240:
        canvas.create_rectangle((365, 285), (365, 258), fill = 'green')

window.bind("<Button-1>", affichage2)

if window.bind("<Button-boutton_pause>"):
    boutton_pause = tk.Button(window, text = "Restart", bg = "RoyalBlue1")


boutton_pause.grid(column = 0, row = 1)
canvas.grid(column = 0, row = 0)

window.mainloop()