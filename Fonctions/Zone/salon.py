def salon():
    from Fonctions.display_scene import display_scene
    from Fonctions.Zone.maison import maison
    from Fonctions.Zone.ruelle import ruelle
    from Fonctions.variables import access_maison, blessure

    print("Vous êtes dans le salon.")
    print("1. Parler à votre père")
    print("2. Regarder la télévision")
    print("3. Retourner dans le hall d'entrée")
    choix = input("Quel est votre choix ? ")
    if choix == "1":
        display_scene([
            "Vous parlez à votre père.\n",
            "Papa - Vas trouvez un travail, tu ne peux pas rester ici toute ta vie.",
            "Vous sentez la pression de devoir trouver un emploi."
        ])
        salon()
    elif choix == "2":
        display_scene([
            "Vous regardez la télévision.",
            "Votre père vous regarde, prend sa ceinture et commence à vous battre.",
            "Vous vous reveillez dans la ruelle d'à côté, il fait nuit, vous avez le visage en sang.",
        ])
        access_maison = False
        blessure = True
        ruelle()
    elif choix == "3":
        display_scene([
            "Vous retournez dans le hall d'entrée.",
            "Vous devez maintenant décider où aller."
        ])
        maison()