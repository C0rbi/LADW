import sys
import os
import tkinter as tk

from Fonctions.display_scene import display_scene, display_choix
from Fonctions.Zone.entre_maison import entre_maison
from story.intro import scene_intro, choix_intro, rep_intro, scene_intro_2

def main():
    root = tk.Tk()
    root.title("Affichage de la scène")
    root.geometry("600x400")

    # Frame principale en bas
    frame_bas = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    frame_bas.pack(side=tk.BOTTOM, fill=tk.X, padx=500, pady=50)  # Réduit le padding

    # Zone de texte
    text_widget = tk.Text(frame_bas, height=10, wrap=tk.WORD, font=("Arial", 12), state=tk.DISABLED)
    text_widget.pack(fill=tk.BOTH, expand=True)

    # Frame pour les boutons de choix, placée FIXEMENT en bas
    button_frame = tk.Frame(frame_bas)
    button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)  # Toujours en bas

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
            lambda: entre_maison(text_widget, button_frame)
        )

    next_scene()
    root.mainloop()

if __name__ == "__main__":
    main()
