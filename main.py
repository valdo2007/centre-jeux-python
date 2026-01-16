import sys
import os
from datetime import datetime

# Ajout du dossier jeux au path pour l'import
sys.path.append(os.path.join(os.path.dirname(__file__), 'jeux'))

import profils
import gamification
import classements
from devine_le_nombre import jouer_devinette
from calcul_mental import jouer_calcul
from pendu import jouer_pendu

def menu_principal():
    print("\n=== CENTRE DE JEUX TERMINAL ===")
    print("1. Choisir/Créer un profil")
    print("2. Jouer : Devine le Nombre")
    print("3. Jouer : Calcul Mental")
    print("4. Jouer : Le Pendu")
    print("5. Voir Classement")
    print("6. Voir mon Historique")
    print("7. Quitter")
    return input("Choix : ")

def main():
    joueur_actuel = None
    
    while True:
        choix = menu_principal()
        
        if choix == "1":
            joueur_actuel = profils.creer_profil()
            if joueur_actuel:
                profils.afficher_profil(joueur_actuel)
        
        elif choix in ["2", "3", "4"]:
            if not joueur_actuel:
                print("Connectez-vous d'abord (Option 1) !")
                continue
            
            # Lancement du jeu
            if choix == "2": 
                pts = jouer_devinette()
                nom_jeu = "Devinette"
            elif choix == "3": 
                pts = jouer_calcul()
                nom_jeu = "Calcul"
            else: 
                pts = jouer_pendu()
                nom_jeu = "Pendu"
            
            # Mise à jour
            joueur_actuel = gamification.calculer_points(joueur_actuel, pts)
            joueur_actuel['parties'].append({
                "jeu": nom_jeu, 
                "points": pts, 
                "date": str(datetime.now().strftime("%d/%m %H:%M"))
            })
            
            gamification.verifier_succes(joueur_actuel)
            profils.sauvegarder_fichier(f"data/profils/{joueur_actuel['nom']}.json", joueur_actuel)
            classements.mettre_a_jour_classement(joueur_actuel, pts)
            print(f"Points gagnés : {pts}")

        elif choix == "5":
            classements.afficher_classement()
        
        elif choix == "6":
            if joueur_actuel: classements.afficher_historique(joueur_actuel)
            else: print("Connectez-vous d'abord !")
            
        elif choix == "7":
            print("Au revoir !")
            break

if __name__ == "__main__":
    main()