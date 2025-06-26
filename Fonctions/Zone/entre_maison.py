def entre_maison():
    from Fonctions.display_scene import display_scene
    from Fonctions.variables import access_maison
    from Fonctions.Zone.maison import maison
    from Fonctions.Zone.ruelle import ruelle

    print("Vous êtes devant l'entrée de votre maison.")
    print("1. Rentrer dans la maison")
    print("2. Aller dans la ruelle d'à côté")
    print("3. Aller au parc")
    choix = input("Quel est votre choix ? ")
    if choix == "1":
        if access_maison: # Vérification si l'accès à la maison est autorisé
            display_scene([
                "Vous entrez dans la maison.",
                "L'intérieur est familier, mais vous sentez une pression de devoir trouver un travail rapidement."
            ])
            maison()  # Rappel de la fonction pour rester dans la maison
        else:
            display_scene([
                "Vous essayez d'entrer dans la maison, mais la porte est verrouillée.",
            ])
    elif choix == "2":
        display_scene([
            "Vous allez dans la ruelle d'à côté.",
            "La ruelle est sombre et étroite, avec des poubelles renversées et des graffitis sur les murs."
        ])
        ruelle()
    elif choix == "3":
        display_scene([
            "Vous allez au parc.",
            "Le parc est calme et paisible, avec des arbres et des bancs."
        ])
        # Ici, vous pouvez ajouter le code pour gérer le parc
    else:
        print("Choix invalide, essayez à nouveau.")
        entre_maison()  # Rappel de la fonction en cas de choix invalide
