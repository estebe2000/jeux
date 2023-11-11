import pyxel

# Variables de la balle
position_balle = [80, 60]
vitesse_balle = [2, 2]

# Variables de la première raquette
position_raquette = [10, 60]  # Position initiale de la première raquette
hauteur_raquette = 20
vitesse_raquette = 2

# Variables de la deuxième raquette
position_raquette2 = [150, 60]  # Position initiale de la deuxième raquette
hauteur_raquette2 = 20  # Vous pouvez ajuster si nécessaire
vitesse_raquette2 = 2

# Variable de score
score = 0
score2 = 0

# États de jeu
etat_jeu = "menu"  # Peut être "menu", "jeu", "infos"
musique_jouee = False

def init_game():
    pyxel.init(160, 120, title="Pong")
    create_music()
    pyxel.run(update, draw)

def create_music():
    pyxel.sound(0).set("c3", "p", "3", "s", 10)
    pyxel.sound(1).set("c3e2g3c4", "p", "7", "vffn", 25)

def update():
    global etat_jeu, musique_jouee,score,score2
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
    elif etat_jeu == "fin":
        if pyxel.btnp(pyxel.KEY_Q):  # Permettre de quitter l'écran de fin avec la touche Q
            # Variable de score
            score = 0
            score2 = 0
            etat_jeu = "menu"


def update_jeu():
    global position_balle, position_raquette, position_raquette2, score,score2, vitesse_balle, etat_jeu  
    
    # Mise à jour de la position de la balle
    position_balle[0] += vitesse_balle[0]
    position_balle[1] += vitesse_balle[1]

    # Rebond de la balle sur les bords
    
    if position_balle[1] <= 0 or position_balle[1] >= pyxel.height:
        vitesse_balle[1] *= -1
        pyxel.play(0, 0)  # Jouer le son

    # Collision avec la raquette
    if (position_raquette[0] <= position_balle[0] <= position_raquette[0] + 2 and
            position_raquette[1] <= position_balle[1] <= position_raquette[1] + hauteur_raquette):
        vitesse_balle[0] *= -1  # Inverser la direction horizontale
        # Ajuster la direction verticale en fonction de l'endroit de la collision
        vitesse_balle[1] += (position_balle[1] - (position_raquette[1] + hauteur_raquette / 2)) / 10

    # Collision avec la deuxième raquette
    if (position_raquette2[0] <= position_balle[0] <= position_raquette2[0] + 2 and
            position_raquette2[1] <= position_balle[1] <= position_raquette2[1] + hauteur_raquette2):
        vitesse_balle[0] *= -1  # Inverser la direction horizontale
        # Ajuster la direction verticale en fonction de l'endroit de la collision
        vitesse_balle[1] += (position_balle[1] - (position_raquette2[1] + hauteur_raquette2 / 2)) / 10

    # Collision avec le mur de gauche 
    if position_balle[0] <= 0:
        # Augmenter le score
        score2 += 1

        # Réinitialiser la position de la balle au centre
        position_balle = [80, 60]
        # Réinitialiser la vitesse de la balle
        vitesse_balle = [2, 2]
        pyxel.play(0, 0)  # Jouer le son
        
    # Collision avec le mur de droite
    elif position_balle[0] >= 160:
        # Augmenter le score
        score += 1

        # Réinitialiser la position de la balle au centre
        position_balle = [80, 60]
        # Réinitialiser la vitesse de la balle
        vitesse_balle = [-2, 2]
        pyxel.play(0, 0)  # Jouer le son

    # Contrôles de la première raquette
    if pyxel.btn(pyxel.KEY_Z) and position_raquette[1] > 0:
        position_raquette[1] -= vitesse_raquette
    if pyxel.btn(pyxel.KEY_S) and position_raquette[1] < pyxel.height - hauteur_raquette:
        position_raquette[1] += vitesse_raquette

    # Contrôles de la deuxième raquette
    if pyxel.btn(pyxel.KEY_O) and position_raquette2[1] > 0:
        position_raquette2[1] -= vitesse_raquette2
    if pyxel.btn(pyxel.KEY_L) and position_raquette2[1] < pyxel.height - hauteur_raquette2:
        position_raquette2[1] += vitesse_raquette2
    
    # Vérifier si un joueur a atteint 3 points
    if score >= 3 or score2 >= 3:
        etat_jeu = "fin"
    
def draw():
    if etat_jeu == "menu":
        draw_menu()
    elif etat_jeu == "jeu":
        draw_jeu()
    elif etat_jeu == "infos":
        draw_infos()
    elif etat_jeu == "fin":
        draw_fin()


def draw_menu():
    pyxel.cls(0)
    pyxel.text(50, 40, "PONG", pyxel.frame_count % 16)
    pyxel.text(50, 60, "S - Start", 7)
    pyxel.text(50, 70, "I - Infos", 7)

def draw_jeu():
    pyxel.cls(0)
    # Dessiner la balle
    pyxel.circ(position_balle[0], position_balle[1], 2, 7)
    # Dessiner la première raquette
    pyxel.rect(position_raquette[0], position_raquette[1], 2, hauteur_raquette, 7)
    # Dessiner la deuxième raquette
    pyxel.rect(position_raquette2[0], position_raquette2[1], 2, hauteur_raquette2, 7)
    # Afficher le score
    pyxel.text(40, 5, f"Score1: {score} - Score2: {score2}", 7)

def draw_infos():
    pyxel.cls(0)
    pyxel.text(10, 10, "Informations du jeu", 7)
    pyxel.text(10, 110, "Q - Retour au menu", 7)

def draw_fin():
    pyxel.cls(0)
    pyxel.text(50, 40, "Fin de la partie!", 7)
    pyxel.text(50, 60, f"Score final: {score} - {score2}", 7)
    pyxel.text(50, 80, "Q - Retour au menu", 7)


init_game()
