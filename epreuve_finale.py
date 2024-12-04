import json
from random import randint


def salle_De_tresor():
    with open("indicesSalle.json", 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    liste_mot_code = []
    for annee in donnees["Fort Boyard"]:
        for mot in donnees["Fort Boyard"][annee]:
            liste_mot_code.append({"indices":donnees["Fort Boyard"][annee][mot]["Indices"],"MOT-CODE":donnees["Fort Boyard"][annee][mot]["MOT-CODE"]})
    numero_emission = randint(0, len(liste_mot_code)-1)
    mot_a_deviner = liste_mot_code[numero_emission]
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



salle_De_tresor()