def ruelle(text_widget, button_frame):
    from Fonctions.display_scene import display_scene
    from Fonctions.Zone.entre_maison import entre_maison, display_choix_with_callbacks
    from Fonctions.variables import game_state

    scene_ruelle = [
        "Vous êtes dans une ruelle sombre et étroite.",
        "Un SDF vous regarde avec un sourire étrange."
    ]

    choix_ruelle = [
        "Parler au SDF",
        "Dormir dans une poubelle",
        "Retourner devant la maison"
    ]

    def handle_choix_1():
        if game_state.blessure and not game_state.piece:
            display_scene([
                "Le SDF vous regarde avec compassion.",
                "Le SDF vous donne une pièce par pitié.",
                "Vous sentez une étrange connexion avec lui, mais vous décidez de ne pas rester"
            ], text_widget, lambda: entre_maison(text_widget, button_frame))
            game_state.piece = True
        else:
            display_scene([
                "Le SDF vous regarde d'un air indifférent.",
            ], text_widget, lambda: entre_maison(text_widget, button_frame))

    def handle_choix_2():
        display_scene([
            "Vous dormez dans une poubelle.",
            "Ce n'est pas très confortable, mais vous arrivez à vous reposer un peu."
        ], text_widget, lambda: ruelle(text_widget, button_frame))

    def handle_choix_3():
        display_scene([
            "Vous retournez devant la maison."
        ], text_widget, lambda: entre_maison(text_widget, button_frame))

    rep_ruelle = [
        "Vous vous approchez du SDF.",
        "Vous cherchez un endroit pour dormir.",
        "Vous quittez la ruelle."
    ]

    callbacks = [handle_choix_1, handle_choix_2, handle_choix_3]

    def show_choices():
        display_choix_with_callbacks(choix_ruelle, rep_ruelle, text_widget, button_frame, callbacks)

    display_scene(scene_ruelle, text_widget, show_choices)

