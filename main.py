'''
??? - WEIMIN!!! FAUT QU'ON PARLE!!!

vous vous reveillez par les cris de votre mère qui vous appelle. 
vous êtes dans votre chambre, allongé sur votre lit. 
Vous vous levez et vous allez voir votre mère.

el mama - il est 14h30, tu a dormi toute la matinée et tu na toujour pas de travail.

Vous descendez les escaliers et vous voyez votre mère dans la cuisine avec votre père a coté d'elle.

rep 1- oui maman, tu me répétes toujour la même chose, je vais trouver du travail.
rep 2- sa va sa va

maman rep 1- tu nous dit sa tout les jours a ton père et a moi, mais tu ne fais rien pour trouver du travail.

maman rep 2- non sa ne va pas dutout.

maman - si tu ne trouves pas de travail a partir de ce soir, tu vas devoir partir de la maison.

vous sortez de la maison en quéte de travail.
vous vous retrouvez dans la rue, vous avez jusqu'à ce soir pour trouver du travail, sinon vous devrez quitter la maison de vos parents.
'''

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