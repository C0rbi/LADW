def choix(choix_list, rep_list):
    import time
    for idx, choix_txt in enumerate(choix_list, 1):
        print(f"{idx}. {choix_txt}")
    while True:
        try:
            choice = int(input(f"Quel est votre choix ? "))
            if 1 <= choice <= len(rep_list):
                print()  # espace avant la réponse
                for lettre in rep_list[choice - 1]:
                    print(lettre, end='', flush=True)
                    time.sleep(0.05)
                print()  # espace après la réponse
                break
            else:
                print("Choix invalide, essayez à nouveau.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")