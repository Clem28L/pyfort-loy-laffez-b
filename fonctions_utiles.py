""""#---------Pyfort-Epreuve-Finale---------#
Rôle : Fichier contenant les fonctions utiles pour le projet
Auteurs: Nathan Laffez/Clément Loy
"""

def introduction():
    '''
    Parametres : /
    Sortie : aucune sortie juste de l'affichage
    Rôle: fonction qui affiche l'introduction au jeu
    '''
    print("#-------------------------Fort-Boyard-------------------#")
    print("bienvenue dans l'aventure Fort-Boyard")
    print("tu doit accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor")
    print("L'objectif est de ramasser trois clés pour accéder à la salle du trésor")


def composer_equipe():
    '''
    Parametres : /
    Sortie :  dictionnaire contenant l'equipe
    Rôle: fonction qui permet de crée une equipe avec au maximun 3 membres
    '''
    nb_joueurs = int(input("Combien de joueur dans l'équipe ?"))
    equipe = {}
    joueur1 = {}
    joueur2 = {}
    joueur3 = {}
    while nb_joueurs > 3:
        print("Max 3 joueurs dans l'équipe !")
        nb_joueurs = int(input("Combien de joueur dabs l'équipe ?"))
    for i in range(nb_joueurs):
        if i == 0:
            nom = input("Nom du joueur : ")
            profession = input("Profession du joueur : ")
            leader = int(input("Le joueurs est leader ? (0 pour non / 1 pour oui)"))
            joueur1["Nom"] = nom
            joueur1["Profession"] = profession
            joueur1["Leader"] = leader
            equipe = {1: joueur1}
        if i == 1:
            nom = input("Nom du joueur : ")
            profession = input("Profession du joueur : ")
            leader = int(input("Le joueurs est leader ? (0 pour non / 1 pour oui)"))
            joueur2["Nom"] = nom
            joueur2["Profession"] = profession
            joueur2["Leader"] = leader
            equipe = {1: joueur1, 2: joueur2}
        if i == 2:
            nom = input("Nom du joueur : ")
            profession = input("Profession du joueur : ")
            leader = int(input("Le joueurs est leader ? (0 pour non / 1 pour oui)"))
            joueur3["Nom"] = nom
            joueur3["Profession"] = profession
            joueur3["Leader"] = leader
            equipe = {1: joueur1, 2: joueur2, 3: joueur3}
    equipe["Clé gagné"] = 0
    for i in range(1, nb_joueurs + 1):
        if equipe[i]["Leader"] == 1:
            return equipe
        else:
            equipe[1]["Leader"] = 1
    return equipe


def choisir_joueur(equipe):
    '''
    Parametres : equipe (dictionnaire)
    Sortie : joueur sous forme de dictionnaire
    Rôle: permet de chosir un joueur pour l'épreuve
    '''
    for i in range(1, len(equipe)):
        if equipe[i]["Leader"] == 1:
            print(str(i), '. ' + equipe[i]["Nom"] + " (" + equipe[i]["Profession"] + ") - Leader")
        else:
            print(str(i), '. ' + equipe[i]["Nom"] + " (" + equipe[i]["Profession"] + ") - Membre")
    nb = int(input("Entrez le numéro du joueur: "))
    return equipe[nb]


def menu_epreuves():
    '''
    Parametres : /
    Sortie : entier qui reprensente une epreuve
    Rôle: permet de chosir une épreuve
    '''
    print("Menu des Épreuves :")
    print("1. Épreuve de Mathématiques")
    print("2. Épreuve de Logique")
    print("3. Épreuve du hasard")
    print("4. Énigme du Père Fouras")
    choix = int(input("Veuillez indiquer le numero de l'épreuve chosie"))
    while choix<= 1 and choix >=1:
        choix = int(input("Veuillez indiquer le numero de l'épreuve choisie (entre 1 et 4) "))
    return choix



print(choisir_joueur(composer_equipe()))
