import pyxel

def init_game():
    pyxel.init(160, 120, title="Pong")
    pyxel.run(update, draw)

def update():
    pass

def draw():
    pyxel.cls(0)  # Efface l'écran avec une couleur noire

init_game()
