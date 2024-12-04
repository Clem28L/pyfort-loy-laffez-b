from random import randint


def suivi(joueur):
    if joueur==0:
        print("C'est au tour du maitre du jeu :")
        joueur = 1
        return joueur
    else:
        joueur = 0
        return joueur

def grille_vide():
    L=[[],[],[]]
    for i in range(3):
        for j in range(3):
            L[i].append(" ")
    return L


def demande_position():
    Ligne=int(input("Saisir un ligne entre 1 et 3:"))-1
    while Ligne<0 or Ligne>2:
        Ligne=int(input("Saisir un ligne :"))-1
    Collone = int(input("Saisir une colonne entre 1 et 3 :")) - 1
    while Collone<0 or Collone>2:
        Collone=int(input("Saisir une colonne entre 1 et 3 :"))-1
    return (Ligne,Collone)


def init():
    Grille=grille_vide()
    for i in range(2):
        print("placez le Bateau",i+1," : ")
        pos=demande_position()
        Lig=pos[0]
        Col=pos[1]
        while Grille[Lig][Col]=="B":
            print("Il y'a deja un bateau a cet emplacement !!")
            pos = demande_position()
            Lig = pos[0]
            Col = pos[1]
        Grille[Lig][Col]="B"
    affiche(Grille,"Découvrez votre grille de jeu avec vos bateaux :")
    return Grille

def init_maitre_du_jeu():
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
    if message=="Découvrez votre grille de jeu avec vos bateaux :":
        print("Découvrez votre grille de jeu avec vos bateaux :")
        for i in range(len(Grille)):
            print("|",end="")
            for j in range(len(Grille[i])):
                    print(Grille[i][j],end=" | ")
            print()
        print("-------------")
    if message=="Rappel de l'historique des tirs que vous avez effectués":
        print("Rappel de l'historique des tirs que vous avez effectués")
        for i in range(len(Grille)):
            print("|",end="")
            for j in range(len(Grille[i])):
                    print(Grille[i][j],end=" | ")
            print()
        print("-------------")



def tour(joueur,grille_tirs_joueur,grille_adversaire):
    if joueur==1:
        TIR=(randint(0,2),randint(0,2))
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
    somme_tirs=0
    for i in range(3):
        for j in range(3):
            if grille_tirs_joueur[i][j]=="x":
                somme_tirs=somme_tirs+1
    if somme_tirs==2:
        return True
    else:return False


def jeu_battaile_navale():
    print("Jeu de 2 joueurs : Chacun doit placer un bateau sur une grille 3x3")
    print("Les bateaux sont représentés par 'B' et les tirs manqués par '.'. Les bateaux coulés sont marqués par 'x'")
    joueur_tour=0
    grille_j0=init()
    grille_tirs_j0=grille_vide()
    joueur_tour=1
    grille_j1=init_maitre_du_jeu()
    grille_tirs_j1=grille_vide()
    print(grille_j1)
    while gagne(grille_tirs_j0)!=True or gagne(grille_tirs_j1)!=True:
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


jeu_battaile_navale()






