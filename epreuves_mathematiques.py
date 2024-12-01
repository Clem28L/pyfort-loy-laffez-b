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
        print("Bravo , Vous avez gagné une clé!!")
        return True
    else:print("Mauvaise réponse !! La bonne réponse était :",bonne_reponse,".")
    return False


def est_premier(n):
    Premier=True
    i=2
    while Premier and i<n:
        if n%i==0:
            Premier=False
        i+=1
    return Premier

def premier_le_plus_proche(n):
    while est_premier(n)==False:
        n=n+1
    return n

def epreuve_math_premier():
    nombre_aleatoire=randint(10,20)
    print("Trouvez le nombre premier le plus proche de :",nombre_aleatoire)
    bonne_reponse=premier_le_plus_proche(nombre_aleatoire)
    reponse_joueur=int(input("Entrez votre réponse :"))
    if bonne_reponse==reponse_joueur:
        print("Bravo , Vous avez gagné une clé!!")
        return True
    else:
        print("Mauvaise réponse !! La bonne réponse était :", bonne_reponse, ".")
    return False
