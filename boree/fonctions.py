#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
Victor Herrmann                Concours Astérios                        15/05/17 
Damien Lesecq                     Groupe Borée                          19/05/17
--------------------------------------------------------------------------------
"""

# ----------------------------------- Import -----------------------------------

from constantes import *
from colors import *
from gopigo import *

from time import sleep,time

# --------------------------------- Variables ----------------------------------

tops = {'g':[0],'d':[0]}

t0 = time()
tc = 0

sens = 0              # pour le sens de prise de mesure du capteur us.

# --------------------------------- Fonctions ----------------------------------

def cor_us(distance_mesuree):
    """ Corrige la distance US mesuré avec un modèle affine.

    Args:
        distance_mesuree (float): Distance mesurée.

    Return:
        (float): Distance corrigée.
    """
    return 0.7777 * distance_mesuree + 1.2795


def us_moy(n):
    """Renvoie la moyenne des n prises de mesures us.

    Args:
        n (int): Nombre de mesures.

    Return:
        (float): Valeur moyenne des distances.
    """

    s = sum([cor_us(us_dist(pin=1)) for i in range(n)]) / float(n)
    #dbg('dist : '+str(s))
    
    return s


def mesure(n=5):
    """Renvoie les mesures à gauche, en face et à droite.
    
    Args:
        n (int)[0]: Nombre de mesure us à moyenner.

    Return:
        (tuple): Ensemble des trois mesures (g,m,d).
    """
    global sens

    pos = ['g','m','d']
    mes = []

    s = 1 if sens else -1
    sens ^= 1             # Permet d'inverser le sens.

    for p in pos[::s]:
        servoPos(p)
        sleep(0.4)
        mes += [us_moy(n)]

    mes = mes[::s]

    dbg('mesure : {}\t{}\t{}'.format(str(mes[0]),str(mes[1]),str(mes[2])))

    return mes


def cache():
    """Attend le retrait du cache pour continuer."""
    global tc

    us = 0
    led_on(0)
    led_on(1)
    
    while us < 10:
        us = us_moy(5)
        sleep(0.5)
        dbg("cache :"+clr(us,fg.orange))

    led_off(0)
    led_off(1)
    print


def getTops(dcG=0,dcD=0):
    """Renvoie un tuple contenant les valeurs des encoder depuis le dernier 
    enregistremnt, en additionnant les décalages.

    Args:
        dcG (int)[0]: Décalage de tops de la roue gauche.
        dcD (int)[0]: Décalage de tops de la roue droite.
    
    Return:
        (tuple): topG,topD
    """
    return enc_read(0) - tops['g'][-1] + dcG, enc_read(1) - tops['d'][-1] + dcD


def setTops():
    """Enregistre les tops des roues dans le dictionnaire."""
    global tops

    tops['g'] += [enc_read(0)]
    tops['d'] += [enc_read(1)]


def setSpeedLR(vG,vD):
    """Applique les vitesses gauche et droite au robot.

    Args:
        vG (int): Vitesse roue gauche.
        vD (int): Vitesse roue droite.
    """
    set_left_speed(vG)
    set_right_speed(vD)


def pVolt(n=1):
    """Affiche la tension parcourant le robot.

    Args:
        n (int)[1]: Nombre de prises de mesure.
    """
    v = sum([volt() for i in range(n)]) / float(n)

    if(v <= 6):
        v = clr(v,fg.red)
    
    elif(6 < v <= 8):
        v = clr(v,fg.orange)
    
    else:
        v = clr(v,fg.green)

    print("La tension est de {} V.".format(v))


def getTime():
    """Renvoie le temps écoulé depuis le début du programme.

    Return:
        (float): Temps (s).
    """
    return time() - t0


def servo2(angle):
    """Tourne le servo moteur d'un angle compris entre -74 et 82°.

    Args:
        angle (int): Angle dans [-75;81].
    """
    if(angle < -74):
        warning("Angle invalide !")
        angle = -74

    elif(angle > 82):
        warning("Angle invalide !")
        angle = 82

    servo(angle + 83)


def servoPos(pos):
    """Place le servo à la position demandée.

    Args:
        pos (char): d(roite), m(ilieu) ou g(auche).
            (int): eq:  1        0           -1.
    """
    angle = {1:9, 0:83, -1:165, 'd':9, 'm':83, 'g':165}[pos]

    servo(angle)

    
def liberte():
    """ Renvoye le triplet (g,m,d) indiquant si les cases autour du robot sont
    libre: retourne 1 pour une direction libre, 0 pour une direction occuper (
    avec un mur).
    
    Return:
        (tuple): Triplet indiquant la présence de mut ou non.
    """
    mesures = mesure(10)
    result = [0,0,0]

    for i,m in enumerate(mesures):
        if m > 40:
            result[i] = 1

    print('{}\t{}\t{}'.format(str(result[0]),str(result[1]),str(result[2])))            
    
    return result
    
def is_number(s):
    """Renvoie si un string représente un nombre.

    Args:
        s (string): String.

    Return:
        (bool)
    """
    try:
        float(s)
        return True
        
    except ValueError:
        return False


def clignotant(n):
    """Clignote en alternance, n répétitions.

    Args
        n (int): Nombre de répétition.
    """
    led_off(0)
    led_off(1)

    for i in range(n):
        led_on(0)
        sleep(0.5)
        led_off(0)

        led_on(1)
        sleep(0.5)
        led_off(1)


def fin():
    """Indique la fin de l'exécution du prgm."""
    servo2(0)
    stop()
    dbg("Exécution en : {} s.".format(getTime() - tc))
    clignotant(3)


def penc(a,b,c):
    """Affiche de manière jolie.
    
    Args:
        a,b,c (values): Valeur à afficher.
    """
    dbg("{}\t{}\t{}".format(clr(a,fg.red), clr(b,fg.blue), clr(c,fg.purple)))