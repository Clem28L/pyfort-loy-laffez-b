from enigme_pere_fouras import enigme_pere_fouras
from enregistrement import *
from epreuve_finale import salle_De_tresor
from epreuves_hasard import epreuve_hasard
from epreuves_logiques import jeu_battaile_navale
from epreuves_mathematiques import epreuve_math
from fonctions_utiles import *
#Lancer de l'introduction et de la fonction pour composer une équipe
introduction()
equipe = composer_equipe()
nb_partie = recuperer_nb_partie()

initialisation_sauvegarde_partie(equipe, nb_partie)

#Boucle permettant de compter le nombre de clés
cle = 0
while cle != 3:
    print("#--------------------------------------------------------------------------------#")
    print("                          "+str(cle)+" cle                   ")
    print("#--------------------------------------------------------------------------------#")
    choix = menu_epreuves()
    print(choix)
    nb_joueur = choisir_joueur(equipe)
    #condition qui permet de lancer une épreuve et de verifier si elle et gagné
    if choix ==1 :
        if epreuve_math() == True:
            equipe[nb_joueur]["cle"] += 1
            equipe["Clé gagné"] += 1
            sauvegarder_epreuve(equipe, "Mathematiques", nb_joueur, True, nb_partie)
        else:
            sauvegarder_epreuve(equipe, "Mathematiques", nb_joueur, False, nb_partie)
    elif choix ==3 :
        if epreuve_hasard() == True:
            equipe[nb_joueur]["cle"] += 1
            equipe["Clé gagné"] += 1
            sauvegarder_epreuve(equipe, "Hasard", nb_joueur,True , nb_partie)
        else:
            sauvegarder_epreuve(equipe, "Hasard", nb_joueur, False, nb_partie)

    elif choix ==2 :
        if jeu_battaile_navale() == True:
            equipe[nb_joueur]["cle"] += 1
            equipe["Clé gagné"] += 1
            sauvegarder_epreuve(equipe, "Bataille navale", nb_joueur, True, nb_partie)
        else:
            sauvegarder_epreuve(equipe, "Bataille navale", nb_joueur, False, nb_partie)
    elif choix ==4 :
        if enigme_pere_fouras() == True:
            equipe[nb_joueur]["cle"] += 1
            equipe["Clé gagné"] += 1
            sauvegarder_epreuve(equipe, "Enigme_pere_fouras", nb_joueur, True, nb_partie)
        else:
            sauvegarder_epreuve(equipe, "Enigme_pere_fouras", nb_joueur, False, nb_partie)

#Epreuve final permettant de savoir si elle est gagné ou non
print("#-----------------Epreuve final --------------------#")
print("bravo tu as recuperé 3 clé, maintenant c'est heure de l'epreuve finale")
if salle_De_tresor() == True:
    print("bravo vous avez gagné !!")
    sauvegarder_partie_terminee(equipe,nb_partie,True)
else:
    print("perdu .....")
    sauvegarder_partie_terminee(equipe, nb_partie, False)