import pyxel

# Variables de la balle
position_balle = [80, 60]  # Position initiale au centre
vitesse_balle = [2, 2]  # Vitesse en x et y

def init_game():
    pyxel.init(160, 120, title="Pong")
    pyxel.run(update, draw)

def update():
    global position_balle, vitesse_balle

    # Mise à jour de la position de la balle
    position_balle[0] += vitesse_balle[0]
    position_balle[1] += vitesse_balle[1]

    # Rebond sur les bords gauche et droit
    if position_balle[0] <= 0 or position_balle[0] >= pyxel.width:
        vitesse_balle[0] *= -1

    # Rebond sur les bords supérieur et inférieur
    if position_balle[1] <= 0 or position_balle[1] >= pyxel.height:
        vitesse_balle[1] *= -1

def draw():
    pyxel.cls(0)
    # Dessiner la balle
    pyxel.circ(position_balle[0], position_balle[1], 2, 7)

init_game()
