# coding: utf-8
import tkinter as tk


class affiche(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ma fenêtre")
        self.geometry("300x200")

        self.bouton_quit=tk.Button(self, text="fermer",command=self.quit)
        #bouton_quit.grid(column=0,row=3)
        self.bouton_quit.pack()
    
        #frame 1 bouton_age et affichage age
        self.frame1=tk.Frame(self)
        self.bouton_age=tk.Button(self.frame1, text="changer age", command=self.age, width=15)
        #bouton_age.grid(column=0,row=4)
        self.bouton_age.pack(side="left",padx=10,pady=10)
        self.label_age= tk.Label(self.frame1, text="",width=15)
        #label_age.grid(column=0,row=1)
        self.label_age.pack(side="left",padx=10,pady=10)
        self.frame1.pack()

        #affichage nom et bouton pour changer nom
        self.frame2=tk.Frame(self)
        self.bouton_nom=tk.Button(self.frame2, text="changer nom", command=self.nom, width=15)
        #bouton_nom.grid(column=1, row=4)
        self.bouton_nom.pack(side="left",padx=10,pady=10)
        self.label_nom=tk.Label(self.frame2, text="",width=15)
        #label_nom.grid(column=0,row=2)
        self.label_nom.pack(side="left",padx=10, pady=10)
        self.frame2.pack()

        #entree user
        self.frame3=tk.Frame(self)
        # entrée
        self.value = tk.StringVar()  
        self.value.set("texte par défaut")
        self.entree = tk.Entry(self.frame3, textvariable=self.value, width=30)
        #entree.grid(column=0,row=5)
        self.entree.pack()
        self.frame3.pack()



    def age(self):
        if affiche.check_input_num(self.value.get()):
            self.label_age["text"]=self.value.get()

    def nom(self):
        self.label_nom["text"]=self.value.get()

    def check_input_num(input):
        return input.isdigit()
        


fenetre = affiche()

fenetre.mainloop()