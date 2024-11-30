from random import randint


def bonneteau():
    liste_elements = ["A","B","C"]
    tentative = 2
    print("te voila arrivé dans l'epreuve du bonneteau, c'est assez simple, blablabla "+ str(tentative))
    print("les bonnetaux disponibles sont : ")
    for element in liste_elements:
        print(element, end=" ")
    print(" ")
    position_bonneteau = randint(0,2)
    print(position_bonneteau)
    while tentative >0:
        print('il te reste '+str(tentative)+"tentative choisie entre les differents bonneteaux disponibles")
        bonneteau_choisie = input()
        while bonneteau_choisie not in liste_elements:
            print("Choix du boneteau incorrecte veuillez en choisir un autre")
        if liste_elements[position_bonneteau] == bonneteau_choisie:
            print("Gagné tu as trouvé le bonneteau")
            return True
        else:
            print("Perdu")
        del liste_elements[liste_elements.index(bonneteau_choisie)]
        tentative = tentative -1
    print("tu as perdu... le bonneteaux se trouvé sous le bonneteau "+ liste_elements[position_bonneteau])






bonneteau()