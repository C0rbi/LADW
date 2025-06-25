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



scene = [
    "??? - WEIMIN!!! FAUT QU'ON PARLE!!!\n",
    "vous vous reveillez par les cris de votre mère qui vous appelle.",
    "vous êtes dans votre chambre, allongé sur votre lit.",
    "Vous vous levez et vous allez voir votre mère.\n",
    "el mama - il est 14h30, tu a dormi toute la matinée et tu na toujour pas de travail.\n",
    "Vous descendez les escaliers.",
    "Dans la cuisine, vous voyez votre mère, accompagnée de votre père.\n",
    "CHOIX"
]

display_scene()
time.sleep(1)
print("Vous avez jusqu'à ce soir pour trouver du travail, sinon vous devrez quitter la maison de vos parents.") 

### Les imports fonctions sont à mettre dans les fonctions, pas dans le main.py ###