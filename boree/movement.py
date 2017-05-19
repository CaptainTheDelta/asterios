#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
Victor Herrmann                Concours Astérios                        15/05/17 
Damien Lesecq                     Groupe Borée                          19/05/17
--------------------------------------------------------------------------------
"""

# ----------------------------------- Import -----------------------------------

from localisation import *
from fonctions import *

from sys import exit,argv

# ------------------------------------ Init ------------------------------------

if(__name__ == '__main__'):
    print("Ne pas executer ce fichier en 1er. Uniquement importable.")
    exit(0)

# ---------------------------- Fonctions mouvement -----------------------------

def debut():
    """Cache et initialisation de la position."""
    print(clr("{0} Lancement de {1} {0}".format('='*25,argv[0][:-3]),fg.cyan))
    cache()
    initPos()


def tout_droit(distance,dcG=0,dcD=0):
    """Avance tout droit de la distance.

    Nota Bene: Ajouter du dcG fait tourner vers la droite, et vis versa

    Args:
        distance (float): Distance à parcourir (en mm).
        dcG (int)[0]: Décalage de tops de la roue gauche.
        dcD (int)[0]: Décalage de tops de la roue droite. 
    """
    # ~~~~ Préparation : ~~~~
    if(distance < 0):
        alert("Distance négative !")
        return False

    setTops()

    delta = 6
    # Calcul du nombre de tops à parcourir :
    nbr_tops = distance / DIST_TOP_EXP - delta
    enc_g,enc_d = 0,0
    ecart = [0]
    vit = {'g':[0],'d':[0]}

    dbg("Nbr tops : "+str(nbr_tops))
    
    # ~~~~ En avant : ~~~~

    setSpeedLR(VIT_MOT,VIT_MOT)

    while enc_g < nbr_tops or enc_d < nbr_tops:
        enc_g,enc_d = getTops(dcG,dcD)
        ecart += [enc_g - enc_d]
        
        # ~~~~ Correction du déphasage des roues : ~~~~

        v_g = VIT_MOT - GAIN_MOT * ecart[-1] - GAIN_MOT2 * ecart[-2]
        v_d = VIT_MOT + GAIN_MOT * ecart[-1] + GAIN_MOT2 * ecart[-2]
        
        vit['g'] += [v_g]
        vit['d'] += [v_d]

        setSpeedLR(v_g,v_d)
        
        fwd()

    
    penc(enc_g, enc_d, ecart[-1])

    maj_position(distance)
    dbg("GoPiGo : ({};{})".format(*get_position()))
    dbg("Case : ({};{})".format(*get_case()))
    stop()
    print



def pivoter(cote,cor=0,dcG=0,dcD=0):
    """Fait tourner le robot sur place, avec une vitesse prédéfinie.
    
    Args:
        direction (int): 0 pour la gauche, 1 pour la droite.
        cor (float)[0]: Correction de l'angle.
        dcG (int)[0]: Décalage de tops de la roue gauche.
        dcD (int)[0]: Décalage de tops de la roue droite.
    """
    # ~~~~ Préparation : ~~~~

    if cote != 0 and cote != 1:
        alert("Erreur sur le paramètre direction")
        return False

    dbg("Tournant à {}. --------------------".format(["gauche","droite"][cote]))

    rot = (left_rot, right_rot)
    
    set_speed(int(0.5 * VIT_MOT))
    setTops()

    delta = 1
    # Par expérience :
    nbr_top = 6 #+ delta
    ecart = [0]

    dbg("Nbr top : " +str(nbr_top))
    
    # ~~~~ Virage : ~~~~
    
    enc_g,enc_d = 0,0
    
    while enc_g < nbr_top and enc_d < nbr_top:
        rot[cote]()

        enc_g,enc_d = getTops(dcG,dcD)
        ecart += [enc_g - enc_d]
    
    penc(enc_g, enc_d, ecart[-1])

    maj_direction(cote)
    stop()
    print



def pivoter2(cote,cor=0,dcG=0,dcD=0):
    """Fait tourner le robot, avec une vitesse prédéfinie.
    
    Args:
        cote (int): 0 pour la gauche, 1 pour la droite.
        cor (float)[0]: Correction de l'angle.
        dcG (int)[0]: Décalage de tops de la roue gauche.
        dcD (int)[0]: Décalage de tops de la roue droite.
    """
    # ~~~~ Préparation : ~~~~

    if cote != 0 and cote != 1:
        alert("Erreur sur le paramètre direction")
        return False

    c = [-1,1][cote]
    vit = [VIT_MOT,0][::c]
    dbg(vit)

    dbg("Tournant à {}. --------------------".format(["gauche","droite"][cote]))

    setSpeedLR(*vit)
    setTops()

    delta = [1,2][cote]
    # Par expérience :
    nbr_top = 10 + delta
    ecart = [0]

    dbg("Nbr top : " +str(nbr_top))
    
    # ~~~~ Virage : ~~~~
    
    enc_g,enc_d = 0,0
    
    while enc_g < nbr_top and enc_d < nbr_top:
        fwd()

        enc_g,enc_d = getTops(dcG,dcD)
        ecart += [enc_g - enc_d]
    
    penc(enc_g, enc_d, ecart[-1])

    maj_direction(cote)
    stop()
    print


def droit(enAvant,dist=200,ecart=2,dcG=2,dcD=5):
    """Avance tout droit tant qu'il ne se prend pas de mur, avec des pauses tous
    les enAvant mm.

    Args:
        enAvant (float): Distance à parcourir par le robot entre chaque pause.
        dist (int): Distance à laquelle s'arrêter du mur.
        ecart (float)[2]: Ecart autorisé pour centrer le GoPiGo.
        dcG (int)[0]: Décalage de tops de la roue gauche.
        dcD (int)[0]: Décalage de tops de la roue droite.
    """
    dbg("Tout droit jusqu'au prochain mur.")

    global sens

    mur = False
    g,m,d = 0,0,0
    sec = (400 - L_AV) / 10
    alert('sécurité :'+str(sec))

    # ~~~~ Approche ~~~~

    while(not mur):
        g,m,d = mesure()
    
        if(m < sec):
            mur = True

        elif(abs(g - d) < ecart):
            tout_droit(enAvant,dcG=DCB)
    
        elif(g > d):
            dbg("Correction vers la gauche.")
            tout_droit(enAvant,dcG=(DCB+dcG))
        
        else:
            dbg("Correction vers la droite.")
            tout_droit(enAvant,dcG=DCB,dcD=dcD)

    #  Mise en place au milieu de la case

    delta = -70

    d = m * 10 + L_AV - dist - delta
    dbg('dist : '+str(dist))
    dbg('m : '+str(m))
    dbg('L_AV : '+str(L_AV))
    dbg('d : '+str(d))


    tout_droit(d,dcG=DCB)

    stop()
    print


def mesure2(cote,n=5):
    """renvoie les mesures du milieu et du côté"""
    global sens

    if (cote != 0 and cote != 1):
        alert("Erreur sur le côté.")
        return False

    pos = [('g','m'),('m','d')][cote]
    mes = []

    s = 1 if sens else -1
    sens ^= 1             # Permet d'inverser le sens.

    for p in pos[::s]:
        servoPos(p)
        sleep(0.5)
        mes += [us_moy(n)]

    mes = mes[::s]

    dbg('mesure : {}\t{}'.format(*mes))

    return mes




def droit_mur(cote,step=200,dcG=3,dcD=2):
    """Longe le mur tant qu'il existe.

    Args:
        distance (float): Distance à parcourir en suivant le mur (!= distance 
            avt le mur !!!).
        cote (int): 0 pour la gauche, 1 pour la droite.
        step (float)[200]: Distance à parcourir par le robot entre chaque pause.
        dcG (int)[0]: Décalage de tops de la roue gauche.
        dcD (int)[0]: Décalage de tops de la roue droite.
    """
    if (cote != 0 and cote != 1):
        alert("Erreur sur le côté.")
        return False

    dbg("Tout droit jusqu'au prochain mur.")

    global sens
    ecart = 2
    vide = False
    mur = False
    sec = (400 - L_AV) / 10
    
    servoPos(['g','d'][cote])
    dist = us_moy(10)
    dbg(dist)
    d = 0

    # ~~~~ Longement du mur ~~~~

    if(cote == 0):
        while(not mur and not vide):
            g,m = mesure2(0)

            if(m < sec):
                mur = True
                dbg("Mur en approche")

            elif(g > 40):
                dbg("Vide à gauche.")
                vide = True

            elif(abs(g - dist) < ecart):
                tout_droit(step,dcG=DCB)

            elif(g > dist):
                dbg("Correction vers la gauche.")
                tout_droit(step,dcG=(DCB+dcG))
        
            else:
                dbg("Correction vers la droite.")
                tout_droit(step,dcG=DCB,dcD=dcD)

    else:
        while(not mur and not vide):
            m,d = mesure2(1)

            if(m < sec):
                mur = True
                dbg("Mur en approche")

            elif(d > 40):
                dbg("Vide à droite.")
                vide = True

            elif(abs(d - dist) < ecart):
                tout_droit(step,dcG=DCB)

            elif(d > dist):
                dbg("Correction vers la gauche.")
                tout_droit(step,dcG=(DCB+dcG))
        
            else:
                dbg("Correction vers la droite.")
                tout_droit(step,dcG=DCB,dcD=dcD)

    # ~~~~ Avance jusqu'au mur ~~~~

    #if(mur):
    #    droit(200,dist=200,ecart=2,dcG=dcG,dcD=dcD)









# ---- Pas dépréciée, mais inutile. ----

def virageTops(rayon, cor=0):
    """Renvoie le nombre de tops pour un virage de pi/2 et un rayon défini.

    Explication :                                   2 x pi x rRoue
    Pour un top, la distance parcourue est : d = --------------------
                                                 nb de top pr un tour
    Le nombre de tops à parcourir est :

         dist    rayon x pi   nb de top pr un tour   rayon       18
    t = ------ = ---------- x -------------------- = ------ x --------
          d           2          2 x pi x R_ROUE       4       R_ROUE
         9     rayon
      = --- x --------
         2     R_ROUE

    Args:
        rayon (float): Rayon (en mm).
        cor (int)[0]: Correction (en tops).

    Return:
        (float): Nombre de tops.
    """
    return (9 / 2 * rayon / R_ROUE) - cor


# ================================= dépréciée ==================================


def virage(direction,rayon,corG=0,corD=0,dcG=0,dcD=0):
    """Fait tourner le robot, avec une vitesse et un rayon prédéfinis.
    
    Args:
        direction (int): 0 pour la gauche, 1 pour la droite.
        rayon (float): Rayon (en mm).
        corG (int)[0]: Décalage de tops de la roue gauche.
        corD (int)[0]: Décalage de tops de la roue droite.
        dcG (int)[0]: Autre décalage de tops de la roue gauche.
        dcD (int)[0]: Autre décalage de tops de la roue droite.
    """
    # ~~~~ Préparation : ~~~~
    
    setTops()
    # Accélération d'une roue par rapport à l'autre (normal pr un virage)
    # Calcul du nombre de tops que doivent parcourir chaque roue.
    if direction == 0:
        setSpeedLR(VIT_MOT / (2 + (VOIE / rayon)),
                    (rayon + VOIE) * VIT_MOT / (2 * rayon + VOIE))

        nbr_top_g = virageTops(rayon,corG)
        nbr_top_d = virageTops(rayon + VOIE,corD)
    
    elif direction == 1:
        setSpeedLR((rayon + VOIE) * VIT_MOT / (2 * rayon + VOIE),
                    VIT_MOT / (2 + (VOIE / rayon)))

        nbr_top_g = virageTops(rayon + VOIE,corG)
        nbr_top_d = virageTops(rayon,corD)
        
    else:
        alert("Erreur sur le paramètre direction")
        return False

    enc_g,enc_d = 0,0
    
    # ~~~~ Virage : ~~~~
    
    # Tant qu'aucune des roues n'a dépassé sa distance à parcourir (via les tops):
    while enc_g < nbr_top_g and enc_d < nbr_top_d:
        fwd()
        sleep(0.01)
        enc_g,enc_d = getTops(dcG,dcD)
        print("{}\t{}\t{}\t{}".format(enc_g, nbr_top_g + corG, enc_d, nbr_top_d + corD))

    # ~~~~ Correction du déphasage des roues : ~~~~
    
    if enc_g < nbr_top_g:
        warning("Correction à gauche")
        set_right_speed(0)
        
        while enc_g < nbr_top_g:
            fwd()
            sleep(0.01)
            enc_g,enc_d = getTops(dcG,dcD)
            print("{}\t{}\t{}\t{}".format(enc_g, nbr_top_g + corG, enc_d, nbr_top_d + corD))
    
    elif enc_d < nbr_top_d:
        set_left_speed(0)
        warning("Correction à droite")
        
        while enc_d < nbr_top_d:
            fwd()
            sleep(0.01)
            enc_g,enc_d = getTops(dcG,dcD)
            print("{}\t{}\t{}\t{}".format(enc_g, nbr_top_g + corG, enc_d, nbr_top_d + corD))
    
    stop()