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

# États de jeu
etat_jeu = "menu"  # Peut être "menu", "jeu", "infos"
musique_jouee = False


def init_game():
    pyxel.init(160, 120, title="Pong")
    # Création des sons et de la musique
    create_music()
    pyxel.run(update, draw)

def create_music():
    pyxel.sound(0).set("c3", "p", "3", "s", 10)
    pyxel.sound(1).set("c3e2g3c4", "p", "7", "vffn", 25)

def update():
    global etat_jeu, musique_jouee
    if etat_jeu == "menu":
        if not musique_jouee:
            pyxel.play(0,1, loop=True)
            musique_jouee = True
        if pyxel.btnp(pyxel.KEY_S):
            etat_jeu = "jeu"
            pyxel.stop()  # Arrêter la musique lorsqu'on quitte le menu
            musique_jouee = False
        elif pyxel.btnp(pyxel.KEY_I):
            etat_jeu = "infos"
            pyxel.stop()  # Arrêter la musique lorsqu'on quitte le menu
            musique_jouee = False
    elif etat_jeu == "jeu":
        update_jeu()
    elif etat_jeu == "infos":
        if pyxel.btnp(pyxel.KEY_Q):
            etat_jeu = "menu"

def update_jeu():
    global position_balle, position_raquette, score

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
    if etat_jeu == "menu":
        draw_menu()
    elif etat_jeu == "jeu":
        draw_jeu()
    elif etat_jeu == "infos":
        draw_infos()

def draw_menu():
    pyxel.cls(0)
    pyxel.text(50, 40, "PONG", pyxel.frame_count % 16)
    pyxel.text(50, 60, "S - Start", 7)
    pyxel.text(50, 70, "I - Infos", 7)

def draw_jeu():
    pyxel.cls(0)
    # Dessiner la balle
    pyxel.circ(position_balle[0], position_balle[1], 2, 7)
    # Dessiner la raquette
    pyxel.rect(position_raquette[0], position_raquette[1], 2, hauteur_raquette, 7)
    # Afficher le score
    pyxel.text(5, 5, f"Score: {score}", 7)

def draw_infos():
    pyxel.cls(0)
    pyxel.text(10, 10, "Informations du jeu", 7)
    # Ajoutez plus d'informations sur le jeu ici si nécessaire
    pyxel.text(10, 110, "Q - Retour au menu", 7)

init_game()
