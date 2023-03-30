# coding: utf-8
from tkinter import *
fenetre = Tk()
label = Label(fenetre, text="Hello World")
label.pack()
label_age= Label(fenetre, text="")
label_age.pack()
label_nom=Label(fenetre, text="")
label_nom.pack()
bouton_quit=Button(fenetre, text="fermer",command=fenetre.quit)
bouton_quit.pack()

def age():
    label_age["text"]=value.get()

def nom():
    label_nom["text"]=value.get()

bouton_age=Button(fenetre, text="changer age", command=age)
bouton_age.pack()
bouton_nom=Button(fenetre, text="changer nom", command=nom)
bouton_nom.pack()
# entrée
value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

fenetre.mainloop()