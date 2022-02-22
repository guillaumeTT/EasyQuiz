import tkinter
import AppBoite
import quiz
import tkinterQuiz

class ChoixApprendre:
    def __init__(self, app):
        """Constructeur de la classe tkinterQuiz.
        Elle affiche la fenêtre du logiciel
        """
        self.taille_text   = 15
        self.couleur_fond  = '#7DB1FE'
        self.titre         = "Quoi apprendre ?"
        self.font_family   = "Sans serif"
        self.app           = tkinter.Frame(app)
        self.a             = AppBoite.AppBoite( quiz.returnBox() )          
        self.lb            = tkinter.Listbox(self.app)
        self.app.config(background=self.couleur_fond)
            
    def affichage(self):
        """Cette méthode permet l'affichage de l'ensemble du contenu"""
        # Le titre
        label_app = tkinter.Label(self.app, text=self.titre, font=(self.font_family, 25), bg=self.couleur_fond)
        label_app.pack()
        
        self.lb.config(width=30, font=('Helvetica', 15))
        self.lb.insert(1,"Anglais")
        self.lb.insert(2,"Polonais")
        self.lb.insert(3,"Chinois")
        self.lb.insert(4,"Capitales par continent")
        self.lb.insert(5,"Administration des SI")
        self.lb.insert(6,"Histoire")
        self.lb.pack()
        
        tkinter.Button(self.app, text="J'ai fais mon choix",command=self.getValueList,font=(self.font_family, self.taille_text), bg='#02C80A').pack()

        self.app.grid(column=1, row=0)
    
    def getValueList(self):
        t = tkinterQuiz.tkinterQuiz()
        t.getMotAleaFichier()
        """return self.lb.curselection()[0]"""
        if self.lb.curselection()[0] == 0:
            val = quiz.getMotAlea("anglais","Question-anglais-1")
            t.labelMotAlea["text"] = val
            return val
        elif self.lb.curselection()[0] == 1:
            t.labelMotAlea["text"] = quiz.getMotAlea("dataPolonais","Question-polonais")
        elif self.lb.curselection()[0] == 2:
            t.labelMotAlea["text"] = quiz.getMotAlea("dataChinois","Question-chinois")
        elif self.lb.curselection()[0] == 3:
            #Pour le test
            t.labelMotAlea["text"] = quiz.getMotAlea("data","Qestion-geo","Capitale-par-continent","Europe")
        elif self.lb.curselection()[0] == 4:
            t.labelMotAlea["text"] = quiz.getMotAlea("data","Question-administration")
        elif self.lb.curselection()[0] == 5:
            t.labelMotAlea["text"] = quiz.getMotAlea("data","Question-histoire")
    
    def getValueList(self):
        t = tkinterQuiz.tkinterQuiz()
        t.getMotAleaFichier()
        """return self.lb.curselection()[0]"""
        if self.lb.curselection()[0] == 0:
            val = quiz.getMotAlea("anglais","Question-anglais-1")
            t.labelMotAlea["text"] = val
            return val
            
        
if __name__ == '__main__':
    pass