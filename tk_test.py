# coding: utf-8
from tkinter import *
fenetre = Tk()
label = Label(fenetre, text="Hello World")
#label.grid(column=0,row=0)
label.pack()
label_age= Label(fenetre, text="")
#label_age.grid(column=0,row=1)
label_age.pack()
label_nom=Label(fenetre, text="")
#label_nom.grid(column=0,row=2)
label_nom.pack()
bouton_quit=Button(fenetre, text="fermer",command=fenetre.quit)
#bouton_quit.grid(column=0,row=3)
bouton_quit.pack()

def age():
    if check_input_num(value.get()):
        label_age["text"]=value.get()

def nom():
    label_nom["text"]=value.get()

def check_input_num(input):
    return input.isdigit()
        

# entrée
value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=value, width=30)
#entree.grid(column=0,row=5)
entree.pack()


bouton_age=Button(fenetre, text="changer age", command=age, width=15)
#bouton_age.grid(column=0,row=4)
bouton_age.pack()
bouton_nom=Button(fenetre, text="changer nom", command=nom, width=15)
#bouton_nom.grid(column=1, row=4)
bouton_nom.pack()

fenetre.mainloop()