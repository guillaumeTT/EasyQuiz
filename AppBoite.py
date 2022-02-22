class AppBoite(object):
    """Cette classe définit le jeu des boites"""
    def __init__(self, boite ):
        self.boite = boite
    
    def motRetenue(self, mot):
        """Je prends l'indice du mot pour depalcer le mots plus facilement"""
        for i, val in enumerate(self.boite):
            if mot not in self.boite[0] and mot not in self.boite[1] and mot not in self.boite[2] and mot not in self.boite[3] and mot not in self.boite[4]:
                self.ajouterMot(mot)
            else:
                index = self.rechercheMot(mot)
                if mot not in self.boite[4]:
                    self.boite[index+1].append(mot)
                    self.boite[index].remove(mot)
                    break

    def ajouterMot(self,mot):
        """On ajoute le nouveau élément dans la premiere boite"""
        self.boite[0].append(mot)

    def motOublie(self, mot):
        """Le mot oublié retourne au début"""
        for i, val in enumerate(self.boite):
            if mot not in self.boite[0] and mot not in self.boite[1] and mot not in self.boite[2] and mot not in self.boite[3] and mot not in self.boite[4]:
                self.ajouterMot(mot)
            else:
                index = self.rechercheMot(mot)
                self.boite[index].remove(mot)
                self.boite[0].append(mot)
                break
        
    def rechercheMot(self, mot):
        """Pour rechercher un mot, puis son indice 
        et s'en service pour le déplacer après les tests"""
        for i, val in enumerate(self.boite):
            if mot in self.boite[i]:
                return i
    
    def afficherNbElement(self, boite):
        """Permet de retourner le nombre d'element qu'il y a
        dans une boite pour l'afficher par la suite"""
        return str(len(boite))

    def afficherBoites(self):
        """Affiche l'ensemble du contenu des boites"""
        s = ""
        for num, i in enumerate(self.boite):
            s += f"Boite {num+1} : {self.boite[num]}\n"
        return s

if __name__ == "__main__":
    box = [["f","r"],[],["w","q","s"],[],["v"]]
    a = AppBoite(box)
    print(a.afficherBoites())
    motIndex = a.rechercheMot("s")
    print(motIndex)
    a.motRetenue("k")
    print(a.afficherBoites())
    print("-----------")
    a.motOublie("k")
    print(a.afficherBoites())

    la_boite = 5
    print(f"Taille de la boite {la_boite} : {a.afficherNbElement(a.boite[la_boite-1])}")

    
