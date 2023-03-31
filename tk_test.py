# coding: utf-8
from tkinter import *
fenetre = Tk()
label = Label(fenetre, text="Hello World")
#label.grid(column=0,row=0)
label.pack()


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
        



frame1=Frame(fenetre)
bouton_age=Button(frame1, text="changer age", command=age, width=15)
#bouton_age.grid(column=0,row=4)
bouton_age.pack(side=LEFT,padx=10,pady=10)
label_age= Label(frame1, text="",width=15)
#label_age.grid(column=0,row=1)
label_age.pack(side=LEFT,padx=10,pady=10)
frame1.pack()


frame2=Frame(fenetre)
bouton_nom=Button(frame2, text="changer nom", command=nom, width=15)
#bouton_nom.grid(column=1, row=4)
bouton_nom.pack(side=LEFT,padx=10,pady=10)
label_nom=Label(frame2, text="",width=15)
#label_nom.grid(column=0,row=2)
label_nom.pack(side=LEFT,padx=10, pady=10)
frame2.pack()


# entrée
value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=value, width=30)
#entree.grid(column=0,row=5)
entree.pack()

fenetre.mainloop()