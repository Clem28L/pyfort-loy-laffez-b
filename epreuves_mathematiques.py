from random import randint, random


def factorielle(n):
    facto=1
    for i in range(1,n+1):
        facto*=i
    return facto

def epreuve_math_factorielle():
    factorielle_aleatoire=randint(1,10)
    print("Vous devez calculer la factorielle de :",factorielle_aleatoire,"!")
    reponse_joueur=int(input("Entrez votre réponse  :"))
    bonne_reponse=factorielle(factorielle_aleatoire)
    if reponse_joueur==bonne_reponse:
        print("Vous avez gagné une clé!!")
        return True
    else:print("Mauvaise réponse !! La bonne réponse était :",bonne_reponse,".")
    return False


epreuve_math_factorielle()