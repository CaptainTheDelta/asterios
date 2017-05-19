#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
Victor Herrmann                Concours Astérios                        15/05/17 
Damien Lesecq                     Groupe Borée                          19/05/17
--------------------------------------------------------------------------------
"""

# ----------------------------------- Inport -----------------------------------

from fonctions import *

# ------------------------------- Documentation --------------------------------

#  L'origine du robot est positionné avec le tuple position (X,Y) en mm selon le 
#  repère suivant.
#  La variable direction indique l'orientation du robot (vers où se situe 
#  l'avant).
#  Initialement, on considère que le robot se situe en position 1 : 
#  A CHANGER SI ON A PLUS D'INFORMATIONS,
#  et on considère qu'il se situe au centre de la case de départ
#  
#      +------+------+------+------+-------
#      |      |      |      |      |      |
#      |      |      |      |      |   <--------+ Arrivée
#      |      |      |      |      |      |
#      +----------------------------------+
#      |      |      |      |      |      |        Variable direction:
#      |      |      |      |      |      |                 0
#      |      |      |      |      |      |                 ^
#      +----------------------------------+                 |
#      |      |      |      |      |      |                 |      
#      |      |      |      |      |      |        3 <-------------> 1
#      |      |      |      |      |      |                 |
#      +----------------------------------+                 |
#      |      |      |      |      |      |                 V
#      |      |      |      |      |      |                 2
#      |      |      |      |      |      |
#    Y ^----------------------------------+
#      |      |      |      |      |      |
#      |   ^  |      |      |      |      |
#      |   |  |      |      |      |      |
#      O------>------+------+------+------+
#          | X
#          +----- Départ

position = {'x':0,'y':0}
direction = 0



def initPos():
    """Initialise les positions initiales."""
    global position

    servoPos('g')

    position['x'] = us_moy(5)
    position['y'] = L_ARR

    servoPos('m')



def maj_position(distance):
    """Met à jour la position du robot.
    
    Args:
        distance (float): distance du déplacement (en mm).
    """
    global position

    if direction == 0:
        position['y'] += distance
    
    elif direction == 1:
        position['x'] += distance
    
    elif direction == 2:
        position['y'] -= distance
    
    elif direction == 3:
        position['x'] -= distance 
    
    else:
        alert("Erreur sur la direction.")
        return False


def maj_direction(cote):
    """Met à jour la direction du robot.
    
      Args:
          distance (bool): 0 pour rotation à gauche, 1 pour à droite.
    """
    global direction
    
    if (cote != 0 and cote != 1):
        alert("Erreur sur la côté.")
        return False
    
    c = [-1,1][cote]
    
    direction = (direction + c) % 4


def get_position():
    """Renvoie la position dans un tupple.
    
    Return:
        (tuple): Coordonnées (X,Y) du robot (en mm).
    """
    return position['x'], position['y']


def initPos():
    """Initialise les positions initiales."""
    global position

    if(direction == 0):
        servoPos('g')
    
        position['x'] = us_moy(5)
        position['y'] = L_ARR
    
        servoPos('m')

    elif(direction == 0):
        servoPos('d')

        position['x'] = L_ARR
        position['y'] = servo_moy(5)
    
        servoPos('m')

    else:
        alert("Erreur à l'initialisation.")
        return False



def get_case(x=0,y=0):
    """Renvoie les coordonnées de la case dans laquelle le robot se trouve.
    
    Args:
        x (float)[0]: Coordonnée à ajouter la position du robot.
        y (float)[0]: Coordonnée à ajouter la position du robot.

    Return:
        (tuple): Coordonnées X,Y (unitaire).
    """
    X,Y = get_position()
    X += x
    Y += y

    return int(X // L_CASE), int(y // L_CASE)


def is_on_case(x,y):
    """Renvoie si le robot est dans la case.

    Args:
        x (int): Abscisse de la case.
        y (int): Ordonnée de la case.

    Return:
        (bool)
    """
    v = VOIE_EXT / 2
    p,q = [((-v,-L_ARR),(v,L_AV)),
            ((-L_ARR,-v),(L_AV,v)),
            ((-v,-L_AV),(v,L_ARR)),
            ((-L_AV,-v),(L_ARR,v))][direction]

    # On prend les coins opposés du GoPiGo.
    
    return get_case(*p) == (x,y) and get_case(*q) == (x,y)