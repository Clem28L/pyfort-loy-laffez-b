def initialisation_sauvegarde_partie(equipe, nb_partie, nom_f='historique.txt'):
    with open(nom_f, 'a') as f:
        f.write('=' * 50 + "\n")
        f.write("         Partie " + str(nb_partie) + "\n")
        f.write('=' * 50 + "\n")
        f.write(f"{'ID':<5}{'Nom':<20}{'Profession':<15}{'Leader':<10}\n")
        f.write("-" * 50 + "\n")
        for joueur_id in equipe:
            joueur = equipe[joueur_id]
            if isinstance(joueur, dict):  # on verifie que 'joueur' est bien un dictionnaire (pour pas avoir une erreur avec la clé gagné)
                if joueur['Leader'] == 1:
                    leader = 'X'
                else:
                    leader = ''
                f.write(f"{joueur_id:<5}{joueur['Nom']:<20}{joueur['Profession']:<15}{leader:<10}\n")


def recuperer_nb_partie(nom_f='historique.txt'):
    with open(nom_f, 'r') as f:
        lignes = f.readlines()
        nb_partie = 0
        for ligne in lignes:
            if ligne.startswith("         Partie"):
                nb_partie += 1
        return nb_partie + 1

def sauvegarder_epreuve(equipe, type_epreuve, joueur_id, resultat, nb_partie, nom_f='historique.txt'):
    with open(nom_f, 'a') as f:
        f.write('=' * 50 + "\n")
        f.write(f"Nouvelle Epreuve pour la Partie {nb_partie}\n")
        f.write(f"Type : {type_epreuve}\n")
        f.write(f"Joueur : {equipe[joueur_id]['Nom']} \n")
        if resultat:
            resultat_str = "Gagne"
        else:
            resultat_str = "Perdu"

        f.write(f"Résultat : {resultat_str}\n")
        f.write(f"Cles totales de l'equipe : {equipe['Clé gagné']}\n")
        f.write('=' * 50 + "\n")

def sauvegarder_partie_terminee(equipe, nb_partie, victoire, nom_f='historique.txt'):
    with (open(nom_f, 'a') as f):
        f.write('=' * 50 + "\n")
        f.write(f"         Resultat de la Partie {nb_partie}\n")
        f.write('=' * 50 + "\n")
        f.write(f"{'ID':<5}{'Nom':<20}{'Profession':<15}{'Leader':<10}{'Cles':<5}\n")
        f.write('=' * 50 + "\n")

        for joueur_id in equipe:
            joueur = equipe[joueur_id]
            if isinstance(joueur, dict):  # on verifie que 'joueur' est bien un dictionnaire (pour pas avoir une erreur avec le clé gagné)
                if joueur['Leader'] == 1:
                    leader = 'X'
                else:
                    leader = ''
                f.write(f"{joueur_id:<5}{joueur['Nom']:<20}{joueur['Profession']:<15}{leader:<10}\n")

        f.write('=' * 50 + "\n")
        f.write(f"Clé gagnee (total equipe) : {equipe['Clé gagné']}\n")
        f.write(f"Partie gagnee : {'Oui' if victoire else 'Non'}\n")
        f.write('=' * 50 + "\n")