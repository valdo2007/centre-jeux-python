from utils import sauvegarder_fichier, charger_fichier

FICHIER_CLASSEMENT = "data/classements.json"

def mettre_a_jour_classement(profil, score):
    data = charger_fichier(FICHIER_CLASSEMENT) or {"top": []}
    data['top'].append({"nom": profil['nom'], "score": profil['score_total']})
    # Garder les meilleurs scores uniques
    data['top'] = sorted(data['top'], key=lambda x: x['score'], reverse=True)[:10]
    sauvegarder_fichier(FICHIER_CLASSEMENT, data)

def afficher_classement():
    data = charger_fichier(FICHIER_CLASSEMENT)
    print("\n--- TOP 10 GLOBAL ---")
    if not data: print("Aucune donnée."); return
    for i, entry in enumerate(data['top'], 1):
        print(f"{i}. {entry['nom']} - {entry['score']} pts")

def afficher_historique(profil):
    print(f"\n--- 20 DERNIÈRES PARTIES ---")
    for p in profil['parties'][-20:]:
        print(f"{p['date']} | {p['jeu']} | {p['points']} pts")