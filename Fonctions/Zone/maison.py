def maison(text_widget, button_frame):
    from Fonctions.display_scene import display_scene
    from Fonctions.Zone.salon import salon
    from Fonctions.Zone.entre_maison import entre_maison, display_choix_with_callbacks

    scene_maison = [
        "Vous êtes dans votre maison."
    ]

    choix_maison = [
        "Aller dans la cuisine",
        "Aller dans le salon",
        "Sortir de la maison"
    ]

    def handle_choix_1():
        display_scene([
            "Vous essayez d'aller dans la cuisine mais l'aura de votre mère vous en empêche.",
            "Vous revenez sur vos pas et vous vous retrouvez dans le hall d'entrée.",
        ], text_widget, lambda: maison(text_widget, button_frame))

    def handle_choix_2():
        display_scene([
            "Vous entrez dans le salon.",
            "Le salon est confortable, avec un canapé et une télévision.",
            "Votre père est assis sur le canapé, il vous regarde et dit : 'Tu devrais vraiment chercher un emploi.'"
        ], text_widget, lambda: salon(text_widget, button_frame))

    def handle_choix_3():
        display_scene([
            "Vous sortez de la maison.",
            "L'air frais vous frappe le visage.",
            "Vous devez maintenant décider où aller."
        ], text_widget, lambda: entre_maison(text_widget, button_frame))

    rep_maison = [
        "Vous vous dirigez vers la cuisine.",
        "Vous vous dirigez vers le salon.",
        "Vous vous dirigez vers la sortie."
    ]

    callbacks = [handle_choix_1, handle_choix_2, handle_choix_3]

    def show_choices():
        display_choix_with_callbacks(choix_maison, rep_maison, text_widget, button_frame, callbacks)

    display_scene(scene_maison, text_widget, show_choices)