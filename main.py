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

entre_maison()
