def calculer_points(profil, points_gagnes):
    profil['score_total'] += points_gagnes
    return profil

def verifier_succes(profil):
    nouveaux = []
    total = profil['score_total']
    nb_parties = len(profil['parties'])
    
    succes_possibles = [
        ("Débutant", total >= 100),
        ("Expert", total >= 500),
        ("Maître", total >= 1000),
        ("Fidèle", nb_parties >= 10)
    ]
    
    for nom, condition in succes_possibles:
        if condition and nom not in profil['succes']:
            profil['succes'].append(nom)
            nouveaux.append(nom)
    
    if nouveaux:
        print(f"\n🏆 Nouveaux succès débloqués : {', '.join(nouveaux)} !")

def mettre_a_jour_statut(profil):
    # Logique simple de niveau
    niveau = (profil['score_total'] // 100) + 1
    print(f"Niveau actuel : {niveau}")