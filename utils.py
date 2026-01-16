import json
import os

def sauvegarder_fichier(chemin, data):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def charger_fichier(chemin):
    if not os.path.exists(chemin):
        return None
    with open(chemin, 'r', encoding='utf-8') as f:
        return json.load(f)

def gestion_erreur(message):
    print(f"\n[ERREUR] : {message}")