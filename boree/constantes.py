#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
Victor Herrmann                Concours Astérios                        15/05/17 
Damien Lesecq                     Groupe Borée                          19/05/17
--------------------------------------------------------------------------------
"""

# ----------------------------------- Import -----------------------------------

from math import pi

# --------------------------------- Constantes ---------------------------------

# -- Paramètres du moteur --
VIT_MOT = 180  # Entre 0 et 255, 0 pas de vitesse, 255 vitesse max.
GAIN_MOT = 1    # Plus la valeur est élevé, plus les oscillations sont petites.
GAIN_MOT2 = 1

# -- Paramètres des roues --
VOIE = 130      # mm distance entre les 2 roues motrices.
R_ROUE = 32.5   # mm.

# -- Paramètres des tops --
NB_TOP = 18                             # Nombre de tops pour un tour de roue.
DCB = 3                                 # Décalage à corriger de base.
DIST_TOP = 2 * pi * R_ROUE / NB_TOP     # Distance parcourue pour un top.
#DIST_TOP_EXP = 11.47                    # Mesuré pour un décalage sur 1200 mm.
DIST_TOP_EXP = 14.20                   # Mesuré pour un décalage sur 200 mm.

# -- Longueur --
VOIE_EXT = 150
L_AV = 130
L_ARR = 140


L_CASE = 400

"""
    Le robot: avec O l'origine 
        
           +--+--+                ^
              |                   |
         +------------------+     |
         |    |             |     |
         |    |          ++ |     |
         |    O         +--+|     | VOIE_EXT
         |    |          ++ |     |
         |    |             |     |
         +------------------+     |
              |                   |
           +--+--+                v
           
    <-----><------------>
     L_AV     L_ARR
         <------------------>
               LONGUEUR
"""