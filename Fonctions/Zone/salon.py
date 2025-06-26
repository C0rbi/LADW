def salon(text_widget, button_frame):
    from Fonctions.display_scene import display_scene
    from Fonctions.Zone.maison import maison
    from Fonctions.Zone.ruelle import ruelle
    from Fonctions.Zone.entre_maison import display_choix_with_callbacks
    from Fonctions.variables import access_maison, blessure

    scene_salon = [
        "Vous êtes dans le salon."
    ]

    choix_salon = [
        "Parler à votre père",
        "Regarder la télévision",
        "Retourner dans le hall d'entrée"
    ]

    def handle_choix_1():
        display_scene([
            "Vous parlez à votre père.\n",
            "Papa - Vas trouvez un travail, tu ne peux pas rester ici toute ta vie.",
            "Vous sentez la pression de devoir trouver un emploi."
        ], text_widget, lambda: salon(text_widget, button_frame))

    def handle_choix_2():
        global access_maison, blessure
        display_scene([
            "Vous regardez la télévision.",
            "Votre père vous regarde, prend sa ceinture et commence à vous battre.",
            "Vous vous reveillez dans la ruelle d'à côté, il fait nuit, vous avez le visage en sang.",
        ], text_widget, lambda: ruelle(text_widget, button_frame))
        access_maison = False
        blessure = True

    def handle_choix_3():
        display_scene([
            "Vous retournez dans le hall d'entrée.",
            "Vous devez maintenant décider où aller."
        ], text_widget, lambda: maison(text_widget, button_frame))

    rep_salon = [
        "Vous vous approchez de votre père.",
        "Vous allumez la télévision.",
        "Vous vous dirigez vers la sortie du salon."
    ]

    callbacks = [handle_choix_1, handle_choix_2, handle_choix_3]

    def show_choices():
        display_choix_with_callbacks(choix_salon, rep_salon, text_widget, button_frame, callbacks)

    display_scene(scene_salon, text_widget, show_choices)