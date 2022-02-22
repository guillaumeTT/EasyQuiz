import tkinter
import PanelEnsBoite, MenuPanel
import AppBoite
import quiz

class FrameContenu:
    def __init__(self):
        """Constructeur de la classe tkinterQuiz.
        Elle affiche la fenêtre du logiciel
        """
        self.taille_text   = 15
        self.couleur_fond  = '#7DB1FE'
        self.titre         = "Contenu des Boîtes"
        self.font_family   = "Sans serif"
        self.app           = tkinter.Tk()
        self.a             = AppBoite.AppBoite( quiz.returnBox() )
        self.p             = PanelEnsBoite.PanelEnsBoite(self.app)
        self.app.title(self.titre)
        self.app.minsize(540, 280)
        self.app.config(background=self.couleur_fond)
            
    def affichage(self):
        """Cette méthode permet l'affichage de l'ensemble du contenu"""
        # Le titre
        label_app = tkinter.Label(self.app, text=self.titre, font=(self.font_family, 25), bg=self.couleur_fond)
        label_app.pack()
        
        # Le menu qui se trouve en haut du logiciel
        MenuPanel.MenuPanel(self.app)

        print(self.a.afficherBoites())
        #Nous allons afficher le contenu des boites des Frame ici
        
        labelEnsBoite = tkinter.Label(self.app, text=self.a.afficherBoites(), wraplength=1000 , font=(self.font_family, self.taille_text)).pack()
        
        self.app.mainloop()
        
if __name__ == '__main__':
    pass