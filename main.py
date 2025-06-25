import time
from fonctions.display_scene import display_scene
from fonctions.choix import choix

# Texte de la scène (par paragraphe)
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