from random import randint


def affichage_bonneteau(liste_bonneteau):
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
    liste_elements = ["A","B","C"]
    tentative = 2
    print("te voila arrivé dans l'epreuve du bonneteau, c'est assez simple, la clé se trouve sous un de ses bonneteaux, tu as deux essaie a toi de le retrouver "+ str(tentative))

    bonneteau_gagnant = liste_elements[randint(0,len(liste_elements)-1)]
    while tentative >0:
        affichage_bonneteau(liste_elements)
        print('il te reste '+str(tentative)+" tentative, choisie entre les differents bonneteaux disponibles")
        bonneteau_choisie = input().upper()
        while bonneteau_choisie not in liste_elements:
            print("Choix du boneteau incorrecte veuillez en choisir un autre")
            bonneteau_choisie = input().upper()
        if bonneteau_gagnant == bonneteau_choisie:
            print("Gagné tu as trouvé le bonneteau")
            return True
        del liste_elements[liste_elements.index(bonneteau_choisie)]
        tentative = tentative -1
    print("tu as perdu... la clé se trouvé sous le bonneteau "+ liste_elements[0])

bonneteau()