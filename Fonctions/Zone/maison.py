def maison():
    from Fonctions.display_scene import display_scene
    from Fonctions.Zone.salon import salon
    from Fonctions.Zone.entre_maison import entre_maison

    print("vous êtes dans votre maison.")
    print("1. Aller dans la cuisine")
    print("2. Aller dans le salon")
    print("3. Sortir de la maison")
    choix = input("Quel est votre choix ? ")
    if choix == "1":
        display_scene([
            "Vous essayez d'aller dans la cuisine mais l'aura de votre mère vous en empêche.",
            "Vous revenez sur vos pas et vous vous retrouvez dans le hall d'entrée.",
        ])
        maison()
    elif choix == "2":
        display_scene([
            "Vous entrez dans le salon.",
            "Le salon est confortable, avec un canapé et une télévision.",
            "Votre père est assis sur le canapé, il vous regarde et dit : 'Tu devrais vraiment chercher un emploi.'"
        ])
        salon()
    elif choix == "3":
        display_scene([
            "Vous sortez de la maison.",
            "L'air frais vous frappe le visage.",
            "Vous devez maintenant décider où aller."
        ])
        entre_maison()
    else:
        print("Choix invalide, essayez à nouveau.")
        maison()