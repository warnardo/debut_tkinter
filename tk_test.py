# coding: utf-8
import tkinter as tk


class affiche(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ma fenêtre")
        self.geometry("300x200")

    def clic(self):
        self.bouton["text"] = "Clic effectué"
    
    def age():
        if affiche.check_input_num(value.get()):
            label_age["text"]=value.get()

    def nom():
        label_nom["text"]=value.get()

    def check_input_num(input):
        return input.isdigit()
        


fenetre = affiche()

bouton_quit=tk.Button(fenetre, text="fermer",command=fenetre.quit)
#bouton_quit.grid(column=0,row=3)
bouton_quit.pack()



frame1=tk.Frame(fenetre)
bouton_age=tk.Button(frame1, text="changer age", command=affiche.age, width=15)
#bouton_age.grid(column=0,row=4)
bouton_age.pack(side="left",padx=10,pady=10)
label_age= tk.Label(frame1, text="",width=15)
#label_age.grid(column=0,row=1)
label_age.pack(side="left",padx=10,pady=10)
frame1.pack()


frame2=tk.Frame(fenetre)
bouton_nom=tk.Button(frame2, text="changer nom", command=affiche.nom, width=15)
#bouton_nom.grid(column=1, row=4)
bouton_nom.pack(side="left",padx=10,pady=10)
label_nom=tk.Label(frame2, text="",width=15)
#label_nom.grid(column=0,row=2)
label_nom.pack(side="left",padx=10, pady=10)
frame2.pack()


# entrée
value = tk.StringVar()
value.set("texte par défaut")
entree = tk.Entry(fenetre, textvariable=value, width=30)
#entree.grid(column=0,row=5)
entree.pack()

fenetre.mainloop()