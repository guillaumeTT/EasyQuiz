import random
import json
import AppBoite
import Save_object


NB_TOUR   = 10

point     = 0
continent = ["Europe", "Asie", "Oceanie", "Afrique", "Amerique-du-nord","Amerique-centrale", "Amerique-du-Sud","Les-Antilles"]
box       = [ [] , [] , [] , [] , [] ]
a         = AppBoite.AppBoite( box )

def afficherContinent():
    """Affiche la liste des continents qu'on choisit"""
    for num , pays in enumerate(continent):
        print(str(num+1) + ") " + pays)
        cpt = num
    print("---------")

def modeSansSaisie(p,motAlea, motConnu, save, nomSave = ""):
    """On devine la réponse et on appuie pour révéler la réponse"""
    input("Appuyer une touche pour révéler le mot...")
    mot = input("As-tu deviné (o/n) : " + motConnu + "\n")
    if mot == "o":
        p += 1
        print("✔️  +1 point !")
        a.motRetenue( motAlea )
        print( a.afficherBoites() )
    elif mot == "n":
        print("❌")
        a.motOublie(motAlea)
        print( a.afficherBoites() )
    else:
        print("Erreur de saisie")
        modeSansSaisie(p, motAlea,motConnu, save, nomSave)
    if save == "o":
        Save_object.save_test(a, nomSave)
    return p

def modeAvecSaisie(p, motConnu, motAConnaitre):
    """On compare la saisie avec le mot Connu"""
    if motConnu.lower() == motAConnaitre.lower():
        p +=1
        print("Bravo ! +1 point !")
    else:
        print("Perdu ! Le mot était " + motConnu)
    return p

def questionnaire(p, objet_python, bOk, nameS,*chemin):
    """On aura l'ensemble de l'affichage avec cette méthode"""
    i = 0
    if len(chemin) == 1:
        while i < NB_TOUR:
            # On récupère les clés de l'ensemble des pays d'Europe
            liste = list(objet_python[chemin[0]])
            alea_q = liste[ random.randint(0, len(liste)-1) ]
            
            reponse = objet_python[chemin[0]][alea_q]
            print(alea_q + "\n")
            # On définit la variable d'en haut pour la modifier en la mettant dans la méthode
            p = modeSansSaisie(p,alea_q,reponse, bOk, nameS)
            i+=1
        print("Tu as " + str(p) + " points sur " + str(NB_TOUR))
    elif len(chemin) == 2:
        choix = int( input("Quel continent pour s'entraîner ? : ") )-1
        print( a.afficherBoites() )
        while i < NB_TOUR:
            if continent[choix] in continent :
                # On récupère les clés de l'ensemble des pays d'Europe
                liste = list(objet_python[chemin[0]][chemin[1]][continent[choix]])
                alea_q = liste[ random.randint(0, len(liste)-1) ]
                
                capital = objet_python[chemin[0]][chemin[1]][continent[choix]][alea_q]
                print("Quelle est la capitale de : "+ alea_q + " ?\n")
                # On définit la variable d'en haut pour la modifier en la mettant dans la méthode
                p = modeSansSaisie(p, alea_q, capital, bOk, nameS)
            else : 
                print("Erreur de saisie")
            i+=1
        print("Tu as " + str(p) + " points sur " + str(NB_TOUR))
    else:
        print("Tu as mis trop d'arguments")

def getMotAlea(nomFic,*chemin):
    """Avoir un mot aléatoire avec la lecteur d'un fichier JSON"""
    with open(nomFic+".json", "r", encoding="utf8") as f:
        jsonContent = f.read()
        obj_python = json.loads(jsonContent)
        if len(chemin) == 1:
            # On récupère les clés de l'ensemble des pays d'Europe
            liste = list(obj_python[chemin[0]])
            alea = liste[ random.randint(0, len(liste)-1) ]
            return alea
        elif len(chemin) == 2:
            #if continent[choix] in continent :
                # On récupère les clés de l'ensemble des pays d'Europe
            #    liste = list(obj_python[chemin[0]][chemin[1]][continent[choix]])
            liste = list(obj_python[chemin[0]][chemin[1]])
            alea = liste[ random.randint(0, len(liste)-1) ]
            return alea
        elif len(chemin) == 3:
            liste = list(obj_python[chemin[0]][chemin[1]][chemin[2]])
            alea = liste[ random.randint(0, len(liste)-1) ]
            return alea

def getReponseMotAlea(alea_q,nomFic,*chemin):
    with open(nomFic+".json", "r", encoding="utf8") as f:
        jsonContent = f.read()
        obj_python = json.loads(jsonContent)
        if len(chemin) == 1:
            return obj_python[chemin[0]][alea_q]
        elif len(chemin) == 2:
           # if continent[choix] in continent :
                # On récupère les clés de l'ensemble des pays d'Europe
            #    liste = list(obj_python[chemin[0]][chemin[1]][continent[choix]])
            #capital = obj_python[chemin[0]][chemin[1]][continent[choix]][alea_q]
            #    return capital
            return obj_python[chemin[0]][chemin[1]][alea_q]
        elif len(chemin) == 3:
            return obj_python[chemin[0]][chemin[1]][chemin[2]][alea_q]

def apprendreAutreChose(ficJsonSansExtension,*chemin):
    """Pareil que mainCode() mais en mettant plus d'argument avec le JSon"""
    with open(ficJsonSansExtension + ".json", "r") as f:
        jsonContent = f.read()
        obj_python = json.loads(jsonContent)

        print("Appel")
        chargerPartie = input("Veux-tu charger la partie (o/n) : ")
        if chargerPartie == "o":
            nomChargerPartie = input("Saisie le nom de la partie chargé : ")
            # Pour les save, tjrs faire 'a = machin' pour remodifier l'objet
            a = Save_object.charger_test( nomChargerPartie )
        
        choix = input("Es-tu admin ? (o/n) ? : ")
        if choix == "o":
            #admin créer des tests
            print("mode admin")
        elif choix == "n":

            bOkSave = input("Voudras-tu sauvegarder la partie ? (o/n) :")
            if bOkSave == "o":
                nameSave = input("Inscris le nom de la sauvegarde (pas d'extension) : ")
            else:
                nameSave = ""

            modeAnki = input("Jouer en mode Anki (o/n) : ")
            if modeAnki == "o":
                if len(chemin) == 1:
                    print( a.afficherBoites() )
                    questionnaire(point,obj_python, bOkSave, nameSave,chemin[0])
                elif len(chemin) == 2:
                    print( a.afficherBoites() )
                    questionnaire(point,obj_python, bOkSave, nameSave,chemin[0], chemin[1])
                elif len(chemin) == 3:
                    print( a.afficherBoites() )
                    questionnaire(point,obj_python, bOkSave, nameSave,chemin[0], chemin[1], chemin[2])
            else:
                print("Mode avec saisie non disponible pour le moment pour ce genre de test !!!")

def returnBox():
    """Retourne le contenu de la box"""
    return box

def mainCode():
    """Code principal pour faire le quiz en Mode Console"""
    chargerPartie = input("Veux-tu charger la partie (o/n) : ")
    if chargerPartie == "o":
        nomChargerPartie = input("Saisie le nom de la partie chargé : ")
        # Pour les save, tjrs faire 'a = machin' pour remodifier l'objet
        a = Save_object.charger_test( nomChargerPartie )

    with open("data.json", "r", encoding="utf8") as f:
        jsonContent = f.read()
        obj_python = json.loads(jsonContent)

        choix = input("Es-tu admin ? (o/n) ? : ")
        if choix == "o":
            #admin créer des tests
            print("mode admin")
        elif choix == "n":

            bOkSave = input("Voudras-tu sauvegarder la partie ? (o/n) :")
            if bOkSave == "o":
                nameSave = input("Inscris le nom de la sauvegarde (pas d'extension) : ")
            else:
                nameSave = ""

            modeAnki = input("Jouer en mode Anki (o/n) : ")
            if modeAnki == "o":

                question = input("Des questions :\n - d'[h]istoire ?\n - d'[a]nglais ?\n - de [g]éo ?\n - de l'[i]ut ?\n=> ")

                if question == "h":
                    print( a.afficherBoites() )
                    questionnaire(point,obj_python, bOkSave, nameSave,"Question-histoire")
                elif question == "a":
                    print( a.afficherBoites() )
                    questionnaire(point,obj_python, bOkSave, nameSave,"Question-anglais")
                elif question == "g":
                    afficherContinent()
                    questionnaire(point,obj_python, bOkSave, nameSave,"Qestion-geo","Capitale-par-continent")
                elif question == "i":
                    print( a.afficherBoites() )
                    questionnaire(point,obj_python, bOkSave, nameSave,"Question-administration")
                else:
                    print("Erreur de saisie")

            elif modeAnki == "n":

                afficherContinent()

                choix = int( input("Quel continent pour s'entraîner ? : ") )-1
                i = 0
                while i < NB_TOUR:
                    if continent[choix] in continent :
                        # On récupère les clés de l'ensemble des pays d'Europe
                        list_pays = list(obj_python["Qestion-geo"]["Capitale-par-continent"][continent[choix]])
                        alea_pays = random.choice(list_pays)
                        
                        capital = obj_python["Qestion-geo"]["Capitale-par-continent"][continent[choix]][alea_pays]
                        saisieCapital = input("Quelle est la capitale de : "+ alea_pays+ " ?\n")
                        # On définit la variable d'en haut pour la modifier en la mettant dans la méthode
                        point = modeAvecSaisie(point,capital, saisieCapital)
                    else : 
                        print("Erreur de saisie")
                    i+=1
                print("Tu as " + str(point) + " points sur " + str(NB_TOUR))


if __name__ == "__main__":
    #mainCode()
    #import calendar
    #cal = calendar.month(2021, 10)
    #print("Here is the calendar:")
    #print(cal)
    pass

