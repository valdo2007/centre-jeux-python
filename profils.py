import os
import datetime
from utils import sauvegarder_fichier, charger_fichier

DOSSIER_PROFILS = "data/profils/"

def creer_profil():
    nom = input("Entrez votre pseudo : ").strip()
    if not nom: return None
    
    chemin = f"{DOSSIER_PROFILS}{nom}.json"
    if os.path.exists(chemin):
        print("Ce profil existe déjà !")
        return charger_profil(nom)

    profil = {
        "nom": nom,
        "date_creation": str(datetime.date.today()),
        "score_total": 0,
        "succes": [],
        "parties": [],
        "stats": {"devinette": 0, "calcul": 0, "pendu": 0}
    }
    sauvegarder_fichier(chemin, profil)
    return profil

def charger_profil(nom):
    chemin = f"{DOSSIER_PROFILS}{nom}.json"
    return charger_fichier(chemin)

def afficher_profil(profil):
    print(f"\n--- PROFIL DE {profil['nom']} ---")
    print(f"Score Total : {profil['score_total']} pts")
    print(f"Succès débloqués : {len(profil['succes'])}")
    print(f"Parties jouées : {len(profil['parties'])}")