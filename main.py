# main.py
# This is the main entry point for the game.
import sys
import os

# Importing necessary modules
from Fonctions.choix import choix
from Fonctions.display_scene import display_scene

def main():
    display_scene(scene)
    choix("Je vais chercher du travail.", "Je reste ici.", "Bonne chance!", "Tu devrais vraiment chercher un emploi.")

print("Vous avez jusqu'à ce soir pour trouver du travail, sinon vous devrez quitter la maison de vos parents.") 