# main.py
# This is the main entry point for the game.
import sys
import os

import time
from fonctions.display_scene import display_scene
from fonctions.choix import choix
from story.intro import scene_intro, choix_intro, rep_intro, scene_intro_2

display_scene(scene_intro)
choix(choix_intro, rep_intro)
time.sleep(1)
display_scene(scene_intro_2)
