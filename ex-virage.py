#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
Victor Herrmann                Concours Astérios                        15/05/17 
Damien Lesecq                     Groupe Borée                          19/05/17
--------------------------------------------------------------------------------
"""

from boree import *
servoPos('g')
cache()
dMur = us_moy(5)
print(us_moy(5))
for i in range(4):
    dMesurer = us_moy(6)
    if dMesurer > dMur:
        print("On doit se décaler à gauche !")
        print(dMesurer)
        tout_droit(200,4,0)    # Plus la valeur est grande, plus on va à droite
    else:
        print("On doit se décaler à droite !")
        print(dMesurer)
        tout_droit(200,1,0)
virage(1,150,4,5,3,0) #0 pour la gauche, 1 pour la droite, rayon, cors, 
for i in range(3):
    if us_moy(5) > dMur:
        print("On doit se décaler à gauche !")
        print(dMesurer)
        tout_droit(200,4,0)    # Plus la valeur est grande, plus on va à droite
    else:
        print("On doit se décaler à droite !")
        print(dMesurer)
        tout_droit(200,1,0)
fin()