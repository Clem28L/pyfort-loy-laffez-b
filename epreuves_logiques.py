from random import randint
'''
#-----------------------------Pyfort-Epreuves-Logique-Bataille-Navale---------------------#
Rôle : Permet de jouer à la bataille navale à 1 joueur contre un maitre du jeu qui
joue et place aleatoirement ses bateaux
Auteurs:Nathan Laffez/Clément Loy
'''

def suivi(joueur):
    '''
    Parametres : joueur(entier)
    Sortie : 0 ou 1 (entier)
    Rôle: Permet de changer le tour entre le Joueur 0 et le maitre du jeu (Joueur 1)
    '''
    if joueur==0:
        print("#-----------------------------C'est au tour du maitre du jeu :-----------------------------------#")
        joueur = 1
        return joueur
    else:
        joueur = 0
        return joueur

def grille_vide():
    '''
    Parametres : /
    Sortie :Tableau 2D
    Rôle: Créer une grille 3x3 vide sous forme de tableau 2D
    '''
    L=[[],[],[]]
    for i in range(3):
        for j in range(3):
            L[i].append(" ")
    return L


def demande_position():
    '''
    Parametres : /
    Sortie : tuple(sous forme (x,y)
    Rôle: Demande au joueur une position sur la grille entre 1 et 3
    '''
    print("-------------------------------------------------------------------------------------------------------")
    Ligne=int(input("Saisir un ligne entre 1 et 3:"))-1
    while Ligne<0 or Ligne>2 : # verifie que la ligne entrée est bien comprise entre 0 et 2
        Ligne=int(input("Saisir un ligne entre 1 et 3  :"))-1
    Collone = int(input("Saisir une colonne entre 1 et 3 :")) - 1
    while Collone<0 or Collone>2:# verifie que la collonne entrée est bien comprise entre 0 et 2
        Collone=int(input("Saisir une colonne entre 1 et 3 :"))-1
    print("-------------------------------------------------------------------------------------------------------")
    return (Ligne,Collone)


def init():
    '''
    Parametres : /
    Sortie : Tableau 2D
    Rôle:Permet de créer une grille vide sous forme de tableau 2D et demande au joueur de placer 2 bateaux, cela verifie
    si un bateau est déjà placé à cet emplacement
    '''
    Grille=grille_vide()
    for i in range(2):
        print("#------------------------------Placez le Bateau",i+1," :---------------------------------------# ")
        pos=demande_position()
        Lig=pos[0]
        Col=pos[1]
        while Grille[Lig][Col]=="B":#Demande au joueur du saisir une posistion si a la position saisie un bateau est déjà présent
            print("#-----------------------Il y'a deja un bateau a cet emplacement !!--------------------------#")
            pos = demande_position()
            Lig = pos[0]
            Col = pos[1]
        Grille[Lig][Col]="B"
    affiche(Grille,"Découvrez votre grille de jeu avec vos bateaux :")
    return Grille

def init_maitre_du_jeu():
    '''
    Parametres : /
    Sortie : Tableau 2D
    Rôle: Permet au maitre du jeu de placer 2 bateau aléatoirement sur la grille
    '''
    Grille=grille_vide()
    for i in range(2):
        Lig= randint(0, 2)
        Col= randint(0, 2)
        while Grille[Lig][Col] == "B":
            Lig = randint(0, 2)
            Col = randint(0, 2)
        Grille[Lig][Col] = "B"
    return Grille


def affiche(Grille,message):
    '''
    Parametres : Tableau 2D , message(chaine de caractères)
    Sortie : / -> voir role
    Rôle: affiche la grille des bateaux ou la grille des tirs précédents avec un affichage special
    '''
    if message=="Découvrez votre grille de jeu avec vos bateaux :":
        print("#--------------------------Découvrez votre grille de jeu avec vos bateaux :-----------------------------------#")
        for i in range(len(Grille)):
            print("|",end="")
            for j in range(len(Grille[i])):
                    print(Grille[i][j],end=" | ")
            print()
        print("-------------")
    if message=="Rappel de l'historique des tirs que vous avez effectués":
        print("#----------------------Rappel de l'historique des tirs que vous avez effectués----------------------#")
        for i in range(len(Grille)):
            print("| ",end="")
            for j in range(len(Grille[i])):
                    print(Grille[i][j],end=" | ")
            print()
        print("-----------------------------------------------------------------------------------------------------")



def tour(joueur,grille_tirs_joueur,grille_adversaire):
    '''
    Parametres : joueur(entier),grille_tirs_joueur(tableau 2D),grille_adversaire(tableau 2D)
    Sortie : / -> voir role
    Rôle: si c'est au tour du maitre du jeu -> tir a des positions aléatoires sur la grille
    si tour du joueur-> affiche l'historique des tirs  et demande au joueur une position sur la grille pour tirer
    affiche le résultat du tir touché / a l'eau
    '''
    if joueur==1:
        TIR=(randint(0,2)+1,randint(0,2)+1)
        print("Le maitre du jeu tir en position :",TIR)
        if grille_adversaire[TIR[0]][TIR[1]]=="B":
            print("Touché Coulé !!")
            grille_tirs_joueur[TIR[0]][TIR[1]]="x"
        else:
            grille_tirs_joueur[TIR[0]][TIR[1]]="."
            print("A l'eau !! ")
    else:
        affiche(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués")
        print("C'est a votre tour de faire feu !")
        TIR=demande_position()
        if grille_adversaire[TIR[0]][TIR[1]]=="B":
            print("Touché Coulé !!")
            grille_tirs_joueur[TIR[0]][TIR[1]]="x"
        else:
            grille_tirs_joueur[TIR[0]][TIR[1]]="."
            print("A l'eau !! ")


def gagne(grille_tirs_joueur):
    '''
    Parametres : grille_tirs_joueur(tableau 2D)
    Sortie : booléen
    Rôle: Calcul le nombre de "x" présent dans la grille des tirs du joueur
    '''
    somme_tirs=0
    for i in range(3):
        for j in range(3):
            if grille_tirs_joueur[i][j]=="x":
                somme_tirs=somme_tirs+1
    if somme_tirs==2:
        return True
    else:return False


def jeu_battaile_navale():
    '''
    Parametres : /
    Sortie : booléen
    Rôle: Initialise les 2 grille ( bateaux et tirs) des 2 joueurs et permet un déroulé du jeu
    tant que aucun joueur est déclarer vainceur
    '''
    print("Jeu de 2 joueurs : Chacun doit placer un bateau sur une grille 3x3")
    print("Les bateaux sont représentés par 'B' et les tirs manqués par '.'. Les bateaux coulés sont marqués par 'x'")
    joueur_tour=0
    grille_j0=init()
    grille_tirs_j0=grille_vide()
    joueur_tour=1
    grille_j1=init_maitre_du_jeu()
    grille_tirs_j1=grille_vide()
    while gagne(grille_tirs_j0)!=True or gagne(grille_tirs_j1)!=True:# Permet de jouer tant aucun joueur est déclarer vainqueur
        joueur_tour=suivi(joueur_tour)
        if joueur_tour==0:
            tour(joueur_tour,grille_tirs_j0,grille_j1)
        else:
            tour(joueur_tour,grille_tirs_j1,grille_j0)
        if  gagne(grille_tirs_j0)==True :
            print("Vous avez gagnez !!")
            return True
        elif gagne(grille_tirs_j1)==True :
            print("Le maitre du jeu a gagné !!")
            return False








