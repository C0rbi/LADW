import time

def display_scene(scene):
    for paragraph in scene:
        for lettre in paragraph:
            print(lettre, end='', flush=True)
            time.sleep(0.05)
        print()
        time.sleep(1)  # Pause pour simuler une lecture