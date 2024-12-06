"""
#---------Pyfort-Epreuve-Finale---------#
Rôle : Fichier contenant l'epreuve finale
Auteurs: Nathan Laffez/Clément Loy
"""

import json
from random import randint


def charger_donnee():
    '''
    Parametres : /
    Sortie : liste de mots
    Rôle: permet de charger les donnees et les inserer dans une liste, ceci pour facilité la lecture
    '''
    with open("indicesSalle.json", 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    liste_mot_code = []
    #boucle qui insere les données dans une liste
    for annee in donnees["Fort Boyard"]:
        for mot in donnees["Fort Boyard"][annee]:
            liste_mot_code.append({"indices":donnees["Fort Boyard"][annee][mot]["Indices"],"MOT-CODE":donnees["Fort Boyard"][annee][mot]["MOT-CODE"]})
    return liste_mot_code



def salle_De_tresor():
    '''
    Parametres : /
    Sortie : Aucune sortie, juste de l'affichage
    Rôle: permet de formater un affichage pour les bonneteaux
    '''
    liste_mot_code = charger_donnee() #initilise la liste des données
    numero_emission = randint(0, len(liste_mot_code)-1)
    mot_a_deviner = liste_mot_code[numero_emission]
    #donne les 3 premiers indices
    for i in range(3):
        print(mot_a_deviner["indices"][i])
    essaie = 3
    reponse_correcte = False
    while essaie > 0 and reponse_correcte == False:
        reponse = input("Quel est le mot code ?")
        if reponse == mot_a_deviner["MOT-CODE"]:
            reponse_correcte = True
        else:
            essaie -= 1
            if essaie > 0:
                print("Le mot code est incorrecte, il te reste "+ str(essaie) + " essaie, voici un indice de plus")
                print(mot_a_deviner["indices"][3+(3-essaie)])
    if reponse_correcte == True:
        print("Le mot code est correcte, BRAVO")
    else:
        print("tu n'a pas reussi à trouver le mot code... le mot code etait "+ mot_a_deviner["MOT-CODE"])


