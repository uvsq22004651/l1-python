from tkinter import *
from tkinter.messagebox import *

info = Tk()
info.geometry('500x500')

dico = {0:'1-Vous êtes :', 1:'un homme', 2:'une femme', 3:'2-Indiquez votre date de naissance :'}

#==================================================================> Sexe

Q1 = Label(info, text = dico[0]).place(x = 0, y = 0)
men = Radiobutton(info, text = dico[1], value = 'homme').place(x = 80, y = 0)
women = Radiobutton(info, text = dico[2], value = 'femme').place(x = 170, y = 0)

#==================================================================> date de naissance

Q2 = Label(info, text = dico[3]).place(x = 0, y = 40)
list_day = Spinbox(info, from_ = 1, to = 31).place(x = 200, y = 40, width = 40, height = 20)
list_month = Spinbox(info, values = ('janvier','février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre')).place(x = 245, y = 40, width = 75, height = 20)
list_year = Spinbox(info, from_ = 1900, to = 2021).place(x = 325, y = 40, width = 60, height = 20)

info.mainloop()