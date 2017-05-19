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

trajet = ('av','g','av_mur','g','av_mur','d','av_mur','d','av_mur','g','av_mur','d','av_mur','g','av_mur','d','arrivee') # C'est le laby des qualifs

cache()
for mouv in trajet:
    if mouv == 'av':
        tout_droit(400,dcG=DCB)
        
    elif mouv == 'av_mur':
        droit(200,dist=250)
        
    elif mouv == 'g':
        pivoter2(0)
        
    elif mouv == 'd':
        pivoter2(1)

    elif mouv == 'arrivee':
        droit(200)
        
    else:
        alert("Erreur sur le trajet.")

fin()