def entre_maison(text_widget, button_frame):
    from Fonctions.display_scene import display_scene, display_choix
    from Fonctions.variables import game_state
    from Fonctions.Zone.maison import maison
    from Fonctions.Zone.ruelle import ruelle

    scene_entre_maison = [
        "Vous êtes devant l'entrée de votre maison."
    ]

    choix_entre_maison = [
        "Rentrer dans la maison",
        "Aller dans la ruelle d'à côté",
        "Aller au parc"
    ]

    def handle_choix_1():
        if game_state.access_maison:  # Vérification si l'accès à la maison est autorisé
            display_scene([
                "Vous entrez dans la maison.",
                "L'intérieur est familier, mais vous sentez une pression de devoir trouver un travail rapidement."
            ], text_widget, lambda: maison(text_widget, button_frame))
        else:
            display_scene([
                "Vous essayez d'entrer dans la maison, mais la porte est verrouillée.",
            ], text_widget, lambda: entre_maison(text_widget, button_frame))

    def handle_choix_2():
        display_scene([
            "Vous allez dans la ruelle d'à côté.",
            "La ruelle est sombre et étroite, avec des poubelles renversées et des graffitis sur les murs."
        ], text_widget, lambda: ruelle(text_widget, button_frame))

    def handle_choix_3():
        display_scene([
            "Vous allez au parc.",
            "Le parc est calme et paisible, avec des arbres et des bancs."
        ], text_widget, lambda: entre_maison(text_widget, button_frame))
        # Ici, vous pouvez ajouter le code pour gérer le parc

    rep_entre_maison = [
        "Vous vous dirigez vers la porte d'entrée.",
        "Vous vous dirigez vers la ruelle sombre.",
        "Vous marchez vers le parc."
    ]

    callbacks = [handle_choix_1, handle_choix_2, handle_choix_3]

    def show_choices():
        display_choix_with_callbacks(choix_entre_maison, rep_entre_maison, text_widget, button_frame, callbacks)

    display_scene(scene_entre_maison, text_widget, show_choices)

def display_choix_with_callbacks(choix_list, rep_list, text_widget, button_frame, callbacks):
    import tkinter as tk
    
    # Efface les anciens boutons
    for widget in button_frame.winfo_children():
        widget.destroy()

    text_widget.config(state=tk.NORMAL)
    for i, choix in enumerate(choix_list):
        text_widget.insert(tk.END, f"{i+1}. {choix}\n")
    text_widget.config(state=tk.DISABLED)

    def on_choix(idx):
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END, f"\n{rep_list[idx]}\n\n")
        text_widget.config(state=tk.DISABLED)
        for widget in button_frame.winfo_children():
            widget.config(state=tk.DISABLED)
        if callbacks[idx]:
            text_widget.after(1000, callbacks[idx])

    for i, choix in enumerate(choix_list):
        btn = tk.Button(button_frame, text=choix, font=("Arial", 12), command=lambda idx=i: on_choix(idx))
        btn.pack(side=tk.LEFT, padx=5, pady=5)
