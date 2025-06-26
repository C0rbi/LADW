def ruelle():
    from Fonctions.display_scene import display_scene
    from Fonctions.Zone.entre_maison import entre_maison
    from Fonctions.variables import blessure, piece

    display_scene([
        "Vous êtes dans une ruelle sombre et étroite.",
        "Des poubelles renversées jonchent le sol, et des graffitis recouvrent les murs.",
        "Un SDF vous regarde avec un sourire étrange.",
    ])
    print("1. Parler au SDF")
    print("2. Dormir dans une poubelle")
    print("3. Retourner devant la maison")
    choix = input("Quel est votre choix ? ")

    if choix == "1":
        if blessure and not piece:
            display_scene([
                "Le SDF vous regarde avec compassion.",
                "le SDF vous donne une pièce par pitié.",
                "Vous sentez une étrange connexion avec lui, mais vous décidez de ne pas rester"
            ])
            piece = True
        else:
            display_scene([
                "Le SDF vous regarde d'un air indifférent.",
            ])
        entre_maison()

