from enigme_pere_fouras import enigme_pere_fouras
from epreuve_finale import salle_De_tresor
from epreuves_hasard import epreuve_hasard
from epreuves_logiques import jeu_battaile_navale
from epreuves_mathematiques import epreuve_math
from fonctions_utiles import *
#Lancer de l'introduction et de la fonction pour composer une équipe
introduction()
equipe = composer_equipe()
#Boucle permettant de compter le nombre de clés
cle = 0
while cle != 3:
    print("#--------------------------------------------------------------------------------#")
    print("                          "+str(cle)+" cle                   ")
    print("#--------------------------------------------------------------------------------#")
    choix = menu_epreuves()
    print(choix)
    choisir_joueur(equipe)
    #condition qui permet de lancer une épreuve et de verifier si elle et gagné
    if choix ==1 :
        if epreuve_math() == True:
            cle = cle + 1
    elif choix ==3 :
        if epreuve_hasard() == True:
            cle = cle + 1
    elif choix ==2 :
        if jeu_battaile_navale() == True:
            cle = cle + 1
    elif choix ==4 :
        if enigme_pere_fouras() == True:
            cle = cle + 1

#Epreuve final permettant de savoir si elle est gagné ou non
print("#-----------------Epreuve final --------------------#")
print("bravo tu as recuperé 3 clé, maintenant c'est heure de l'epreuve finale")
if salle_De_tresor() == True:
    print("bravo vous avez gagné !!")
else:
    print("perdu .....")

