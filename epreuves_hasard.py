from random import randint


def bonneteau():
    liste_elements = ["A","B","C"]
    tentative = 2
    print("te voila arrivé dans l'epreuve du bonneteau, c'est assez simple, blablabla "+ str(tentative))
    print("les bonnetaux disponibles sont : ")
    for element in liste_elements:
        print(element, end=" ")
    print(" ")
    bonneteau_gagnant = liste_elements[randint(0,2)]
    print(bonneteau_gagnant)
    while tentative >0:
        print('il te reste '+str(tentative)+"tentative choisie entre les differents bonneteaux disponibles")
        bonneteau_choisie = input().upper()
        while bonneteau_choisie not in liste_elements:
            print("Choix du boneteau incorrecte veuillez en choisir un autre")
            bonneteau_choisie = input().upper()
        if bonneteau_gagnant == bonneteau_choisie:
            print("Gagné tu as trouvé le bonneteau")
            return True
        del liste_elements[liste_elements.index(bonneteau_choisie)]
        tentative = tentative -1
    print("tu as perdu... le bonneteaux se trouvé sous le bonneteau "+ liste_elements[0])
