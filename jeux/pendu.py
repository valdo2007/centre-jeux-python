import random

def jouer_pendu():
    mots = ["PYTHON", "ALGORITHME", "TERMINAL", "JOUEUR", "PROGRAMME"]
    mot = random.choice(mots)
    lettres = []
    vies = 7
    print("\n--- LE PENDU ---")
    
    while vies > 0:
        affichage = "".join([l if l in lettres else "_" for l in mot])
        print(f"\nMot : {affichage} (Vies: {vies})")
        if "_" not in affichage:
            print("Victoire !")
            return 100
        
        tentative = input("Lettre : ").upper()
        if tentative in lettres: continue
        lettres.append(tentative)
        
        if tentative not in mot:
            vies -= 1
            print("Raté !")
            
    print(f"Perdu ! Le mot était {mot}")
    return 0