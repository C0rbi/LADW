class GameState:
    def __init__(self):
        self.access_maison = True
        self.blessure = False
        self.piece = False

# Instance globale partagée
game_state = GameState()