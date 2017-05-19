#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
Victor Herrmann                Concours Astérios                        15/05/17 
Damien Lesecq                     Groupe Borée                          19/05/17
--------------------------------------------------------------------------------
"""

# ----------------------------------- Import -----------------------------------

from boree import *

# --------------------------------- Programme ----------------------------------

"""
Les portions de trajet possible sont les suivant:
  'av' : avance d'une case
    'av_mur' : avance jusqu'au prochain mur
    'g' : pivote à gauche
    'd' : pivote à droite
"""

cache()

g1, m1, d1 = mesure()
tout_droit(400,dcG=DCB)
g2, m2, d2 = mesure()

tout_droit(150,dcG=DCB+2)


if g1 > 40: # Cas 3
    dbg("C'est le coin 3")
    trajet = ('av','g','av_moins','d','av','g','av_mur','d','av_mur','g','av_mur','g','av_mur','d','av_mur','d','arrivee')

elif d1 > 40: # Cas 2
    dbg("C'est le coin 2")
    trajet = ('av','av_plus','d','av_mur','g','av_mur','d','av_mur','d','av_mur','g','av_mur','d','av_mur','g''av_mur','g','arrivee')

elif g2 > 40: # Cas 1
    dbg("C'est le coin 1")
    trajet = ('g','av_mur','g','av_mur','d','av_mur','d','av_mur','g','av_mur','d','av_mur','g','av_mur','d','arrivee')

else: # Cas 4
    dbg("C'est le coin 4 (par défaut)")
    trajet = ('av','d','av_moins','d','av','g','av_mur','d','av_mur','g','av_mur','g','av_mur','d','av_mur','g','arrivee')


for mouv in trajet:
    if mouv == 'av':
        tout_droit(400,dcG=DCB)
        
    elif mouv == 'av_mur':
        droit(200,dist=300)
        
    elif mouv == 'g':
        pivoter2(0)
        
    elif mouv == 'd':
        pivoter2(1)

    elif mouv == 'arrivee':
        droit(200)

    elif mouv == 'av_moins':
        tout_droit(350,dcG=DCB)
    
    elif mouv == 'av_plus':
        tout_droit(450,dcG=DCB)
        
    else:
        alert("Erreur sur le trajet.")

fin()