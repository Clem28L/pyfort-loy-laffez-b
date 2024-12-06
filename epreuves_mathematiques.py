from random import randint, random
'''
#-----------------------------Pyfort-Epreuves-Mathématiques----------------------#
Rôle : Comporte toutes les épreuves de mathématiques et 
permet de choisir une épreuve de math aléatoirement
Auteurs:Nathan Laffez/Clément Loy
'''


def factorielle(n):
    '''
    Parametres : n(entier)
    Sortie : factorielle de n (entier)
    Rôle: Calcul la factorile de n
    '''
    facto=1
    for i in range(1,n+1):
        facto*=i
    return facto

def epreuve_math_factorielle():
    '''
    Parametres : /
    Sortie : Booléen
    Rôle: demande au joueur de calculer la factorile de d'un nombre aléatoire entre 1 et 10
    renvoie Vrai si la réponse du joueur est bonne , Faux si la réponse du joueur est fausse 
    '''
    factorielle_aleatoire=randint(1,10)
    print("Epreuve de la Factorielle :")
    print("Vous devez calculer la factorielle de :",factorielle_aleatoire,"!")
    reponse_joueur=int(input("Entrez votre réponse  :"))
    bonne_reponse=factorielle(factorielle_aleatoire)
    if reponse_joueur==bonne_reponse:#Verifie si la réponse est la bonne
        print("Bravo , Vous avez gagné une clé!!")
        return True
    else:print("Mauvaise réponse !! La bonne réponse était :",bonne_reponse,".")
    return False


def est_premier(n):
    '''
    Parametres : n(entier)
    Sortie : Booléen
    Rôle:Savoir si n est un nombre entier ou non
    '''
    Premier=True
    i=2
    while Premier and i<n:
        if n%i==0:
            Premier=False
        i+=1
    return Premier

def premier_le_plus_proche_sup(n):
    '''
    Parametres : n(entier)
    Sortie : n(entier)
    Rôle: Donner le nombre premier le plus proche 
    de n que soit n ou un nombre supérieur
    '''
    while est_premier(n)==False:
            n=n+1
    return n
def premier_le_plus_proche_inf(n):
    '''
    Parametres : n(entier)
    Sortie : n(entier)
    Rôle: Donner le nombre premier le plus proche
    de n que soit n ou un nombre supérieur
    '''
    while est_premier(n)==False:
            n=n-1
    return n

def epreuve_math_premier():
    '''
    Parametres : /
    Sortie : Booléen
    Rôle: Demande au joueur le nombre premier
    le plus proche d'un nombre aléatoire entre 10 et 20
    renvoie Vrai si la réponse du joueur est bonne , Faux si la réponse du joueur est fausse 
    '''
    print("Epreuve du Nombre Premiers : ")
    nombre_aleatoire=randint(10,20)
    print("Trouvez le nombre premier le plus proche de :",nombre_aleatoire)
    if est_premier(nombre_aleatoire):
        bonne_reponse=nombre_aleatoire
        reponse_joueur=int(input("Entrez votre réponse :"))
        if bonne_reponse == reponse_joueur:  # Verifie si la réponse est la bonne
            print("Bravo , Vous avez gagné une clé!!")
            return True
        else:
            print("Mauvaise réponse !! La bonne réponse était :", bonne_reponse, ".")
            return False
    else:
        if nombre_aleatoire-premier_le_plus_proche_sup(nombre_aleatoire)==nombre_aleatoire-premier_le_plus_proche_inf(nombre_aleatoire):
            bonne_reponse=premier_le_plus_proche_sup(nombre_aleatoire)
            bonne_reponse2=premier_le_plus_proche_inf(nombre_aleatoire)
            reponse_joueur = int(input("Entrez votre réponse :"))
            if bonne_reponse == reponse_joueur or bonne_reponse2==reponse_joueur:  # Verifie si la réponse est la bonne
                print("Bravo , Vous avez gagné une clé!!")
                return True
            else:
                print("Mauvaise réponse !! La bonne réponse était :", bonne_reponse, ".")
                return False
        else:
            bonne_reponse=min(nombre_aleatoire-premier_le_plus_proche_sup(nombre_aleatoire),nombre_aleatoire-premier_le_plus_proche_inf(nombre_aleatoire))
            print(bonne_reponse)
            bonne_reponse=bonne_reponse+nombre_aleatoire
            reponse_joueur=int(input("Entrez votre réponse :"))
            if bonne_reponse==reponse_joueur:#Verifie si la réponse est la bonne
                print("Bravo , Vous avez gagné une clé!!")
                return True
            else:
                print("Mauvaise réponse !! La bonne réponse était :", bonne_reponse, ".")
                return False


def epreuve_roulette_math():
    """  
    Parametre : /
    Sortie : Booléen
    Rôle: Demande au joueur une réponse selon l'opérateur aléatoire :
    additioner/soustraire/multiplier tout les nombres aleétoire entre 1 et 20 entre eux
    renvoie Vrai si la réponse du joueur est bonne , Faux si la réponse du joueur est fausse 
    """
    print("Epreuve de la Roulette mathématique : ")
    nb1=randint(1,20)
    nb2=randint(1,20)
    nb3=randint(1,20)
    nb4=randint(1,20)
    nb5=randint(1,20)
    operation=["+","-","*"]
    nb_op=randint(0,2)
    print("Nombres sur la roulette: [",nb1,",",nb2,",",nb3,",",nb4,",",nb5,"]")
    if operation[nb_op]=="+":#Verifie l'opération a faire pour l'épreuve
            bonne_reponse=nb1+nb2+nb3+nb4+nb5
            print("Calculez le résultat en combinant ces nombres avec une addition ")
            reponse_joueur = int(input("Entrez votre réponse :"))
            if bonne_reponse == reponse_joueur:
                print("Bravo , Vous avez gagné une clé!!")
                return True
            else:
                print("Mauvaise réponse !! La bonne réponse était :", bonne_reponse, ".")
            return False
    if operation[nb_op]=="-":#Verifie l'opération a faire pour l'épreuve
        bonne_reponse=nb1-nb2-nb3-nb4-nb5
        print("Calculez le résultat en combinant ces nombres avec une soustraction")
        reponse_joueur = int(input("Entrez votre réponse :"))
        if bonne_reponse == reponse_joueur:
            print("Bravo , Vous avez gagné une clé!!")
            return True
        else:
            print("Mauvaise réponse !! La bonne réponse était :", bonne_reponse, ".")
            return False
    if operation[nb_op] == "*":#Verifie l'opération a faire pour l'épreuve
        bonne_reponse = nb1 * nb2 * nb3 * nb4 * nb5
        print("Calculez le résultat en combinant ces nombres avec une multiplication")
        reponse_joueur = int(input("Entrez votre réponse :"))
        if bonne_reponse == reponse_joueur:
            print("Bravo , Vous avez gagné une clé!!")
            return True
        else:
            print("Mauvaise réponse !! La bonne réponse était :", bonne_reponse, ".")
            return False


def epreuve_math():
    """  
    Parametres : /
    Sortie : Booléen
    Rôle: Choisis aleatoirement une épreuve et renvois le résultats du resulats de l'épreuve 
    """
    epreuves=[epreuve_math_premier]
    epreuve=randint(0,len(epreuves)-1)
    return epreuves[epreuve]()

epreuve_math()

