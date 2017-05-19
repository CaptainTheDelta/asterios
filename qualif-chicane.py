#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
Victor Herrmann                Concours Astérios                        15/05/17 
Damien Lesecq                     Groupe Borée                          19/05/17
--------------------------------------------------------------------------------
"""

from boree import *


ecart = 2           # cm.
sens = 0            # Var pour le sens de prise de mesure du capteur us.
dec = 4             # Décalage pour corriger les déviations de trajectoire.

enAvant = 200       # Distance à parcourir par le robot entre chaque pause.

cache()

# ~~~~ Première ligne droite ~~~~

droit(enAvant,dist=300)

# ~~~~ Virage ~~~~

pivoter2(1)

# ~~~~ Seconde ligne droite ~~~~

droit(enAvant,dist=300)
        
# ~~~~ Second virage ~~~~

pivoter2(0)

# ~~~~ Troisième ligne droite ~~~~

droit(enAvant)

fin()