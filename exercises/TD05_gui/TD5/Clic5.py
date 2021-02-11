import tkinter as tk
le_clic = tk.Tk()
le_clic.title("Clic")

nb_clic = 0
couleur = 'red'


def vider_remplir(event):
    global nb_clic, carré_remplit, carré_vide
    while nb_clic <= 9:
        if nb_clic % 2 != 0:
            nb_clic += 1
            canvas.delete(le_clic, carré_remplit)
            carré_vide 
            print('vide')
        elif nb_clic % 2 == 0:
            nb_clic += 1
            canvas.delete(le_clic, carré_vide)
            carré_remplit
            print('remplit')
    else:
        le_clic.destroy()
        print('détruit')

le_clic.bind("<Button-1>", vider_remplir)

canvas = tk.Canvas(le_clic, width = 500, height = 500, bg = 'black')
canvas.grid()

carré_remplit = canvas.create_rectangle((300, 300), (200, 200), fill = 'MediumOrchid3')
carré_vide = canvas.create_line((200, 200), (300, 200), (300, 300), (200, 300), (200, 200), fill = 'MediumOrchid3')

le_clic.mainloop()