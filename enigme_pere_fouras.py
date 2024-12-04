"""#-----------------------------Pyfort-Enigme-pere-fouras---------------------#
Rôle : Comporte la fonction charger enigmes et enigme pere fouras permettant de lancer une enigme
Auteurs:Nathan Laffez/Clément Loy
"""

import json
from random import randint


def charger_enigmes(fichier):
    '''
    Parametres : fichier (Nom du fichier json)
    Sortie : liste_enigmes (Liste des dictionnaires comprenant les questions ainsi que les reponses)
    Rôle: permet de charger le fichier json et de retourner le dictionnaire comportant les question et reponse
    '''
    with open(fichier, 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    liste_enigmes = []
    for enigme in donnees:
        liste_enigmes.append({"question": enigme["question"], "reponse": enigme["reponse"]})
    return liste_enigmes




def enigme_pere_fouras():
    '''
    Parametres : aucun parametres
    Sortie : aucune sortie fonction principal qui permet d'afficher et d'interagir avec l'utilisateur
    Rôle: permet de donner une enigme a l'utilisateur et qu'il puisse y repondre, le joueur a trois essaie pour trouver la reponse
    '''
    liste_enigmes = charger_enigmes("enigmesPF.json")
    enigme = liste_enigmes[randint(0, len(liste_enigmes) - 1)]
    print(enigme["question"])
    essaie = 3
    while essaie >0:
        reponse = input("Quel est ta réponse à l'engime ?").lower()
        if reponse == enigme["reponse"].lower():
            print("Bravo, tu as resolu l'énigme du pere fouras, voici ta clé !")
            return True
        else:
            essaie -= 1
            print("reponse incorrecte, cherche encore il te reste ", str(essaie),"essaie pour trouver !")
    print("Malheurement tu as perdu, la reponse était", str(enigme["reponse"]))

enigme_pere_fouras()