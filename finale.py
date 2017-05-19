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

trajet = ('av_mur','g','av_moins','d','av','av_plus','g','av','av_plus','d','av_mur','g','arrivee') # C'est le laby des qualifs

cache()
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
        droit(200,dist=230)
    
    elif mouv == 'av_moins':
        tout_droit(350,dcG=DCB)
    
    elif mouv == 'av_moins2':
        tout_droit(390,dcG=DCB)

    elif mouv == 'av_plus':
        tout_droit(430,dcG=DCB)  
    
    else:
        alert("Erreur sur le trajet.")

fin()      