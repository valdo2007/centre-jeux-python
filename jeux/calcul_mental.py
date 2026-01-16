import random
import time

def jouer_calcul():
    print("\n--- CALCUL MENTAL (30 secondes) ---")
    score = 0
    debut = time.time()
    while time.time() - debut < 30:
        a, b = random.randint(1, 12), random.randint(1, 12)
        op = random.choice(['+', '-', '*'])
        res = eval(f"{a}{op}{b}")
        try:
            reponse = int(input(f"{a} {op} {b} = "))
            if reponse == res:
                score += 10
                print("Correct !")
            else:
                print(f"Faux ! C'était {res}")
        except: break
    print(f"Temps écoulé ! Score : {score}")
    return score