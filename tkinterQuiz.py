import tkinter
import PanelEnsBoite, MenuPanel
import quiz
import AppBoite
from tkinter import messagebox
from Save_object import *

class tkinterQuiz:
    def __init__(self):
        """Constructeur de la classe tkinterQuiz.
        Elle affiche la fenêtre du logiciel
        """
        self.taille_text           = 15
        self.paddingY              = 15
        self.couleur_fond          = '#7DB1FE'
        self.titre                 = "Test de connaissance"
        self.font_family           = "Sans serif"
        self.msgError              = "Veuillez choisir ce que vous voulez apprendre !!!"
        self.app                   = tkinter.Tk()
        self.a                     = AppBoite.AppBoite( quiz.returnBox() )
        self.frameGauche           = tkinter.Frame(self.app, bg=self.couleur_fond)
        self.frameDroite           = tkinter.Frame(self.app, bg=self.couleur_fond)
        self.p                     = PanelEnsBoite.PanelEnsBoite(self.frameGauche)
        self.motA                  = ""
        self.labelMotAlea          = tkinter.Label(self.frameGauche, text=self.motA,pady=self.paddingY, font=(self.font_family, self.taille_text),bg=self.couleur_fond, wraplength=300)
        self.labelAfficherMotConnu = tkinter.Label(self.frameGauche, text="",pady=self.paddingY, font=(self.font_family, self.taille_text), bg=self.couleur_fond, wraplength=300)
        self.lb                    = tkinter.Listbox(self.frameDroite)
        self.choixValider          = 0
        self.app.title(self.titre)
        self.app.minsize(640, 480)
        self.app.config(background=self.couleur_fond)
        
    def ajoutMotBox(self, mot):
        """Elle doit ajouter le mot dans le paquet suivant qui lui correspond et
        changer le label"""
        if mot == "":
            msgbox = messagebox.showerror("Erreur", self.msgError)
        else:
            self.a.motRetenue(mot)
            print( self.a.afficherBoites() )
            self.p.update()
            self.changerMotAlea()
            self.labelAfficherMotConnu["text"] = ""

    def suppMotBox(self,mot):
        """Elle doit supprimer le mot du paquet qui lui correspond, le remettre au début et
        changer le label. """
        if mot == "":
            msgbox = messagebox.showerror("Erreur", self.msgError)
        else:
            self.a.motOublie(mot)
            self.p.update()
            print( self.a.afficherBoites() )
            self.changerMotAlea()
            self.labelAfficherMotConnu["text"] = ""
    
    def afficherReponse(self, question):
        """On affiche la réponse à la question demandé dans le quiz"""
        if question == "":
            msgbox = messagebox.showerror("Erreur", self.msgError)
        else:
            self.getValueAnswerList(question)
        
    def changerMotAlea(self):
        """Changer le label avec un nouveau mot et
        ce ceux label qui va se mettre dans les boites"""
        self.getValueList()

    def affichage(self):
        """Cette méthode permet l'affichage de l'ensemble du contenu"""

        MenuPanel.MenuPanel(self.app)      
          
        label_app = tkinter.Label(self.frameGauche, text=self.titre, font=(self.font_family, 25), bg=self.couleur_fond)
        label_app.pack()

        self.p.panelEnsBoite(self.frameGauche)

        self.labelMotAlea.pack()
        
        btnMotConnu = tkinter.Button(self.frameGauche, text="👇  Afficher la réponse  👇",command=lambda:self.afficherReponse(self.labelMotAlea["text"]) ,font=(self.font_family, self.taille_text), bg='#02C80A').pack()
        
        self.labelAfficherMotConnu.pack()

        labelConnaitreMot = tkinter.Label(self.frameGauche, text="As-tu deviné la réponses ?",pady=self.paddingY, font=(self.font_family, self.taille_text), bg=self.couleur_fond).pack()
        
        # Une Frame pour avoir le Oui Non sur une ligne
        frameRepOuiNon = tkinter.Frame(self.frameGauche)

        # Nous ajoutons ou supprimons le label. self.motA sert uniquement pour l'affichage
        btnOui = tkinter.Button(frameRepOuiNon, text="Oui", command=lambda:self.ajoutMotBox(self.labelMotAlea["text"]), font=(self.font_family, self.taille_text), padx=10).grid(column=0, row=0)
        btnNon = tkinter.Button(frameRepOuiNon, text="Non", command=lambda:self.suppMotBox (self.labelMotAlea["text"]), font=(self.font_family, self.taille_text), padx=10).grid(column=1, row=0)

        frameRepOuiNon.pack()
        
        self.frameGauche.grid(column=0, row=0)
                
        label_ap = tkinter.Label(self.frameDroite, text="Quoi apprendre ?", font=(self.font_family, 25), bg=self.couleur_fond)
        label_ap.pack()
        
        self.lb.config(width=30, font=('Helvetica', 15))
        self.lb.insert(1,"Anglais")
        self.lb.insert(2,"Polonais")
        self.lb.insert(3,"Chinois")
        self.lb.insert(4,"Capitales en Europe")
        self.lb.insert(5,"Capitales en Asie")
        self.lb.insert(6,"Capitales en Océanie")
        self.lb.insert(7,"Capitales en Afrique")
        self.lb.insert(8,"Capitales en Amerique du Nord")
        self.lb.insert(9,"Capitales en Amerique Centrale")
        self.lb.insert(10,"Capitales en Amerique du Sud")
        self.lb.insert(11,"Capitales dans Les Antilles")
        self.lb.insert(12,"Administration des SI")
        self.lb.insert(13,"Histoire")
        self.lb.pack()
        
        tkinter.Button(self.frameDroite, text="J'ai fais mon choix",command=self.getValueList,font=(self.font_family, self.taille_text), bg='#02C80A').pack()

        self.frameDroite.grid(column=1, row=0)    
                
        self.app.mainloop()
        
    def getValueList(self):
        """return self.lb.curselection()[0]"""
        if self.lb.curselection()[0] == 0:
            self.labelMotAlea["text"] = quiz.getMotAlea("anglais","Question-anglais-1")
        elif self.lb.curselection()[0] == 1:
            self.labelMotAlea["text"] = quiz.getMotAlea("dataPolonais","Question-polonais")
        elif self.lb.curselection()[0] == 2:
            self.labelMotAlea["text"] = quiz.getMotAlea("dataChinois","Question-chinois")
        elif self.lb.curselection()[0] == 3:
            self.labelMotAlea["text"] = quiz.getMotAlea("data","Qestion-geo","Capitale-par-continent","Europe")
        elif self.lb.curselection()[0] == 4:
            self.labelMotAlea["text"] = quiz.getMotAlea("data","Qestion-geo","Capitale-par-continent","Asie")
        elif self.lb.curselection()[0] == 5:
            self.labelMotAlea["text"] = quiz.getMotAlea("data","Qestion-geo","Capitale-par-continent","Oceanie")
        elif self.lb.curselection()[0] == 6:
            self.labelMotAlea["text"] = quiz.getMotAlea("data","Qestion-geo","Capitale-par-continent","Afrique")
        elif self.lb.curselection()[0] == 7:
            self.labelMotAlea["text"] = quiz.getMotAlea("data","Qestion-geo","Capitale-par-continent","Amerique-du-nord")
        elif self.lb.curselection()[0] == 8:
            self.labelMotAlea["text"] = quiz.getMotAlea("data","Qestion-geo","Capitale-par-continent","Amerique-centrale")
        elif self.lb.curselection()[0] == 9:
            self.labelMotAlea["text"] = quiz.getMotAlea("data","Qestion-geo","Capitale-par-continent","Amerique-du-Sud")
        elif self.lb.curselection()[0] == 10:
            self.labelMotAlea["text"] = quiz.getMotAlea("data","Qestion-geo","Capitale-par-continent","Les-Antilles")
        elif self.lb.curselection()[0] == 11:
            self.labelMotAlea["text"] = quiz.getMotAlea("data","Question-administration")
        elif self.lb.curselection()[0] == 12:
            self.labelMotAlea["text"] = quiz.getMotAlea("data","Question-histoire")
    
    def getValueAnswerList(self, question):
        """return self.lb.curselection()[0]"""
        if self.lb.curselection()[0] == 0:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"anglais","Question-anglais-1")
        elif self.lb.curselection()[0] == 1:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"dataPolonais","Question-polonais")
        elif self.lb.curselection()[0] == 2:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"dataChinois","Question-chinois")
        elif self.lb.curselection()[0] == 3:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"data","Qestion-geo","Capitale-par-continent","Europe")
        elif self.lb.curselection()[0] == 4:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"data","Qestion-geo","Capitale-par-continent","Asie")
        elif self.lb.curselection()[0] == 5:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"data","Qestion-geo","Capitale-par-continent","Oceanie")
        elif self.lb.curselection()[0] == 6:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"data","Qestion-geo","Capitale-par-continent","Afrique")
        elif self.lb.curselection()[0] == 7:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"data","Qestion-geo","Capitale-par-continent","Amerique-du-nord")
        elif self.lb.curselection()[0] == 8:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"data","Qestion-geo","Capitale-par-continent","Amerique-centrale")
        elif self.lb.curselection()[0] == 9:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"data","Qestion-geo","Capitale-par-continent","Amerique-du-Sud")
        elif self.lb.curselection()[0] == 10:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"data","Qestion-geo","Capitale-par-continent","Les-Antilles")
        elif self.lb.curselection()[0] == 11:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"data","Question-administration")
        elif self.lb.curselection()[0] == 12:
            self.labelAfficherMotConnu["text"] = quiz.getReponseMotAlea(question,"data","Question-histoire")
    
    
if __name__ == '__main__':
    t = tkinterQuiz()
    t.affichage()