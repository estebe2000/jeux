import pyxel

# Variables de la balle
position_balle = [80, 60]
vitesse_balle = [2, 2]

# Variables de la raquette
position_raquette = [10, 60]  # Position initiale de la raquette
hauteur_raquette = 20
vitesse_raquette = 2

# Variable de score
score = 0

def init_game():
    pyxel.init(160, 120, title="Pong")
    # Création du son
    pyxel.sound(0).set("c3", "p", "3", "s", 10)
    pyxel.run(update, draw)

def update():
    global position_balle, position_raquette

    # Mise à jour de la position de la balle
    position_balle[0] += vitesse_balle[0]
    position_balle[1] += vitesse_balle[1]

    # Rebond de la balle sur les bords
    if position_balle[0] <= 0 or position_balle[0] >= pyxel.width:
        vitesse_balle[0] *= -1
        pyxel.play(0, 0)  # Jouer le son
    if position_balle[1] <= 0 or position_balle[1] >= pyxel.height:
        vitesse_balle[1] *= -1
        pyxel.play(0, 0)  # Jouer le son

    # Contrôles de la raquette
    if pyxel.btn(pyxel.KEY_Z) and position_raquette[1] > 0:
        position_raquette[1] -= vitesse_raquette
    if pyxel.btn(pyxel.KEY_S) and position_raquette[1] < pyxel.height - hauteur_raquette:
        position_raquette[1] += vitesse_raquette

def draw():
    pyxel.cls(0)
    # Dessiner la balle
    pyxel.circ(position_balle[0], position_balle[1], 2, 7)
    # Dessiner la raquette
    pyxel.rect(position_raquette[0], position_raquette[1], 2, hauteur_raquette, 7)
    # Afficher le score
    pyxel.text(5, 5, f"Score: {score}", 7)

init_game()
