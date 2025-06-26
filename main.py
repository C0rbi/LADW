import sys
import os

from Fonctions.display_scene import display_scene
from Fonctions.choix import choix
from Fonctions.Zone.entre_maison import entre_maison
from story.intro import scene_intro, choix_intro, rep_intro, scene_intro_2
'''
display_scene(scene_intro)
choix(choix_intro, rep_intro)
display_scene(scene_intro_2)
'''

#entre_maison()

import tkinter as tk
from Fonctions.display_scene import display_scene, display_choix
from story.intro import scene_intro, choix_intro, rep_intro, scene_intro_2

def main():
    root = tk.Tk()
    root.title("Affichage de la scène")
    root.geometry("600x400")

    # Frame en bas de la fenêtre
    frame_bas = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    frame_bas.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    # Zone de texte
    text_widget = tk.Text(frame_bas, height=10, wrap=tk.WORD, font=("Arial", 12), state=tk.DISABLED)
    text_widget.pack(fill=tk.BOTH, expand=True)

    # Frame pour les boutons de choix
    button_frame = tk.Frame(frame_bas)
    button_frame.pack(fill=tk.X, pady=5)

    # Affichage de la première scène
    def next_scene():
        display_scene(
            scene_intro,
            text_widget,
            lambda: display_choix(choix_intro, rep_intro, text_widget, button_frame, next_scene_2)
        )

    def next_scene_2():
        display_scene(
            scene_intro_2,
            text_widget,
            lambda: display_choix(             
                text_widget,
                button_frame,
                None  # Remplace None par une autre fonction pour la suite si besoin
            )
        )

    next_scene()
    root.mainloop()

if __name__ == "__main__":
    main()
