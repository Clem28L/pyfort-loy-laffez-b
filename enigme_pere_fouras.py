import json
from random import randint


def charger_enigmes(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    liste_enigmes = []
    for enigme in donnees:
        liste_enigmes.append({"question": enigme["question"], "reponse": enigme["reponse"]})
    return liste_enigmes




def enigme_pere_fouras():
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