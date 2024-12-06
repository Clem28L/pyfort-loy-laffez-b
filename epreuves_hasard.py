from random import randint

"""
#---------Pyfort-Epreuves-Hasard---------#
Rôle : Comporte toutes les épreuves de hasard et 
permet de choisir une épreuve de hasard aléatoirement
Auteurs: Nathan Laffez/Clément Loy
"""

def affichage_bonneteau(liste_bonneteau):
    '''
    Parametres : liste_bonneteau(liste de str)
    Sortie : Aucune sortie, juste de l'affichage
    Rôle: permet de formater un affichage pour les bonneteaux
    '''
    print("#-------Bonneteau  disponible-------#")
    print("      ", end="")
    print("_____     " * len(liste_bonneteau))
    print("     " + "|     |   " * len(liste_bonneteau))
    print("     ",end="")
    for lettre in liste_bonneteau:
        print("|  " + lettre+"  |   ",end="" )
    print("\n     " + "|     |   " * len(liste_bonneteau))
    print("     " + "|_____|   " * len(liste_bonneteau))
    print("#-----------------------------------#")


def bonneteau():
    '''
    Parametres : /
    Sortie : aucune sortie, juste de l'affichage de l'epreuve des bonneteaux
    Rôle: fonction qui simule le jeu du bonneteau
    '''
    liste_elements = ["A","B","C"]
    tentative = 2
    print("te voila arrivé dans l'epreuve du bonneteau, c'est assez simple, la clé se trouve sous un de ses bonneteaux, tu as deux essaie a toi de le retrouver "+ str(tentative))

    bonneteau_gagnant = liste_elements[randint(0,len(liste_elements)-1)]
    #boucle qui permet de lancer le jeu du bonneteau avec 3 essaie
    while tentative >0:
        affichage_bonneteau(liste_elements)
        print('il te reste '+str(tentative)+" tentative, choisie entre les differents bonneteaux disponibles")
        bonneteau_choisie = input().upper()
        #saisie securisé du bonneteau
        while bonneteau_choisie not in liste_elements:
            print("Choix du boneteau incorrecte veuillez en choisir un autre")
            bonneteau_choisie = input().upper()
        if bonneteau_gagnant == bonneteau_choisie:
            print("Gagné tu as trouvé le bonneteau")
            return True
        #permet de supprimer de la liste des bonneteaux le bonneteau choisie
        del liste_elements[liste_elements.index(bonneteau_choisie)]
        tentative = tentative -1
    print("tu as perdu... la clé se trouvé sous le bonneteau "+ liste_elements[0])


def afficher_de(face):
    '''
    Parametres : face (entier)
    Sortie : Aucune sortie, juste de l'affichage
    Rôle: permet de formater un affichage pour les dés
    '''
    if face == 1:
        print("|-----|")
        print("|     |")
        print("|  *  |")
        print("|     |")
        print("|-----|")
    elif face == 2:
        print("|-----|")
        print("| *   |")
        print("|     |")
        print("|   * |")
        print("|-----|")
    elif face == 3:
        print("|-----|")
        print("| *   |")
        print("|  *  |")
        print("|   * |")
        print("|-----|")
    elif face == 4:
        print("|-----|")
        print("| * * |")
        print("|     |")
        print("| * * |")
        print("|-----|")
    elif face == 5:
        print("|-----|")
        print("| * * |")
        print("|  *  |")
        print("| * * |")
        print("|-----|")
    elif face == 6:
        print("|-----|")
        print("| * * |")
        print("| * * |")
        print("| * * |")
        print("|-----|")


def jeu_lance_des():
    '''
    Parametres : /
    Sortie : Aucune sortie, juste de l'affichage
    Rôle: fonction qui simule le jeu des dés
    '''
    essais = 3
    # boucle qui permet de lancer le jeu de dés avec 3 essaie
    while essais > 0:
        print("il vous reste "+ str(essais)+ " essais")
        input("Appuie sur ESPACE pour lancer les dès")
        des = (randint(1,6), randint(1,6))
        print("Vous avez obtenu le dé suivant ")
        afficher_de(des[0])
        #condition qui permet de verifié la victoire
        if des[0] == 6:
            print("Vous avez gagné !!")
            return True
        print("Le maitre a obtenu le dé suivant")
        afficher_de(des[1])
        # condition qui permet de verifié la victoire
        if des[1] == 6:
            print("Vous avez perdu ...")
            return False
        # condition qui permet de verifié le match nul
        if des[1] != 6 and des[0] != 6:
            print("personne n'a obtenu de 6.")
            if essais == 0:
                print("Apres 3 essaie personne n'a obtenu de 6, match nul !")
                return False
            print("On recommence !!")
            essais -= 1


def epreuve_hasard():
    """
    Parametres : /
    Sortie : Booléen
    Rôle: Choisis aleatoirement une épreuve et renvois le résultats du resulats de l'épreuve
    """
    epreuves=[jeu_lance_des,bonneteau]
    epreuve=randint(0,len(epreuves)-1)
    return epreuves[epreuve]()

epreuve_hasard()










