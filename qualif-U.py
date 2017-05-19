#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
Victor Herrmann                Concours Astérios                        15/05/17 
Damien Lesecq                     Groupe Borée                          19/05/17
--------------------------------------------------------------------------------
"""

from boree import *

enAvant = 200

cache()

# ~~~~ Première ligne droite ~~~~

droit(enAvant,dist=300)

# ~~~~ Virage ~~~~

pivoter2(1)

# ~~~~ Seconde ligne droite ~~~~

droit(enAvant,dist=300)
        
# ~~~~ Second virage ~~~~

pivoter2(1)

# ~~~~ Troisième ligne droite ~~~~

droit(enAvant)

fin()