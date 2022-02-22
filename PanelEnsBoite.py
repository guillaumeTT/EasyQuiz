import tkinter
import quiz
import AppBoite

class PanelEnsBoite:
    def __init__(self,tkinterNamePanel):
        self.font_family = "Sans serif"
        self.font_size = 15
        self.string_size = 5
        self.a = AppBoite.AppBoite( quiz.returnBox() )
        self.frame = tkinter.Frame(tkinterNamePanel)
        self.boite1 = tkinter.Frame(self.frame)
        self.boite2 = tkinter.Frame(self.frame)
        self.boite3 = tkinter.Frame(self.frame)
        self.boite4 = tkinter.Frame(self.frame)
        self.boite5 = tkinter.Frame(self.frame)

    def panelEnsBoite(self,tkinterNamePanel):
        self.frame = tkinter.Frame(tkinterNamePanel)

        self.boite1 = tkinter.Frame(self.frame)
        self.boite2 = tkinter.Frame(self.frame)
        self.boite3 = tkinter.Frame(self.frame)
        self.boite4 = tkinter.Frame(self.frame)
        self.boite5 = tkinter.Frame(self.frame)

        # Développement

        #imagelabel1 = tkinter.Label(boite1, width=string_size,font=(font_family, font_size), bg="red"        ).grid(column=0, row=0)
        #chiffre1 = tkinter.Label(boite1, text=a.afficherNbElement(quiz.returnBox()[0]),font=(font_family, font_size)).grid(column=0, row=1)
        imagelabel1 = tkinter.Label(self.boite1, width=self.string_size,font=(self.font_family, self.font_size), bg="red"        ).grid(column=0, row=0)
        self.chiffre1 = tkinter.Label(self.boite1, text=self.a.afficherNbElement(quiz.returnBox()[0]),font=(self.font_family, self.font_size))

        imagelabel2 = tkinter.Label(self.boite2, width=self.string_size,font=(self.font_family, self.font_size), bg="orange"     ).grid(column=0, row=0)
        self.chiffre2 = tkinter.Label(self.boite2, text=self.a.afficherNbElement(quiz.returnBox()[1]),font=(self.font_family, self.font_size))

        imagelabel3 = tkinter.Label(self.boite3, width=self.string_size,font=(self.font_family, self.font_size), bg="yellow"     ).grid(column=0, row=0)
        self.chiffre3 = tkinter.Label(self.boite3, text=self.a.afficherNbElement(quiz.returnBox()[2]),font=(self.font_family, self.font_size))

        imagelabel4 = tkinter.Label(self.boite4, width=self.string_size,font=(self.font_family, self.font_size), bg="light green").grid(column=0, row=0)
        self.chiffre4 = tkinter.Label(self.boite4, text=self.a.afficherNbElement(quiz.returnBox()[3]),font=(self.font_family, self.font_size))

        imagelabel5 = tkinter.Label(self.boite5, width=self.string_size,font=(self.font_family, self.font_size), bg="green"      ).grid(column=0, row=0)
        self.chiffre5 = tkinter.Label(self.boite5, text=self.a.afficherNbElement(quiz.returnBox()[4]),font=(self.font_family, self.font_size))

        # Affichage
        self.chiffre1.grid(column=0, row=1)
        self.chiffre2.grid(column=0, row=1)
        self.chiffre3.grid(column=0, row=1)
        self.chiffre4.grid(column=0, row=1)
        self.chiffre5.grid(column=0, row=1)

        self.boite1.grid(column=0, row=0)
        self.boite2.grid(column=1, row=0)
        self.boite3.grid(column=2, row=0)
        self.boite4.grid(column=3, row=0)
        self.boite5.grid(column=4, row=0)

        self.frame.pack()
    
    def update(self):
        """Met a jour les différents champs"""
        self.chiffre1["text"] = self.a.afficherNbElement(quiz.returnBox()[0])
        self.chiffre2["text"] = self.a.afficherNbElement(quiz.returnBox()[1])
        self.chiffre3["text"] = self.a.afficherNbElement(quiz.returnBox()[2])
        self.chiffre4["text"] = self.a.afficherNbElement(quiz.returnBox()[3])
        self.chiffre5["text"] = self.a.afficherNbElement(quiz.returnBox()[4])


