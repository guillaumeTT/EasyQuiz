import tkinter
from tkinter import messagebox
import FrameContenu
import ChoixApprendre

def show_modal_window():
    msgbox = messagebox.showinfo("Erreur", "Une erreur est survenue !")

def MenuPanel(tkinterNamePanel):
    menu_bar = tkinter.Menu(tkinterNamePanel)
    file_menu = tkinter.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Supprimer", command=tkinterNamePanel.quit)
    option_menu = tkinter.Menu(menu_bar, tearoff=0)
    option_menu.add_command(label="Afficher contenu des boîtes", command=afficherContenu)
    option_menu.add_command(label="Changer de test")
    menu_bar.add_cascade(label="Fichier", menu=file_menu)
    menu_bar.add_cascade(label="Sélection", menu=option_menu)
    menu_bar.add_cascade(label="Apprendre", command=getChoixApprendre)
    menu_bar.add_cascade(label="Sauvegarde", command=show_modal_window)
    menu_bar.add_cascade(label="Aide", command=show_modal_window)
    tkinterNamePanel.config(menu=menu_bar)
    
def getChoixApprendre():
    ca = ChoixApprendre.ChoixApprendre()
    ca.affichage()
    
    
def afficherContenu():
    fc = FrameContenu.FrameContenu()
    fc.affichage()