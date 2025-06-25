import time
from fonctions.display_scene import display_scene
from fonctions.choix import choix
from story.intro import scene_intro, choix_intro, rep_intro

display_scene(scene_intro)
choix(choix_intro, rep_intro)
time.sleep(1)
display_scene(["Vous avez jusqu'à ce soir pour trouver du travail, sinon vous devrez quitter la maison de vos parents."])