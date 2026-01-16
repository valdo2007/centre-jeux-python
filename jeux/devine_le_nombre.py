import random

def jouer_devinette():
    print("\n--- DEVINE LE NOMBRE (1-100) ---")
    cible = random.randint(1, 100)
    essais = 0
    while True:
        try:
            choix = int(input("Votre nombre : "))
            essais += 1
            if choix < cible: print("C'est plus !")
            elif choix > cible: print("C'est moins !")
            else:
                print(f"Gagné en {essais} coups !")
                points = max(10, 100 - (essais * 5))
                return points
        except ValueError:
            print("Entrez un nombre valide.")