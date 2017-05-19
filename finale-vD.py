#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
Victor Herrmann                Concours Astérios                        15/05/17 
Damien Lesecq                     Groupe Borée                          19/05/17
--------------------------------------------------------------------------------
"""

from boree import *

debut()

fini = False

culDeSac = False



while(not fini):
    lg,lm,ld = liberte()

    if(lg):
        alert("lg : vide")
        tout_droit(100,dcG=DCB)
        pivoter2(0)
        tout_droit(200,dcG=DCB)

    elif(not lg and lm):
        alert("not lg and lm : suivre mur gauche")
        droit_mur(0)


    elif(not lg and not lm and lg):
        alert("not lg and not lm and lg ")
        pivoter2(1)
        tout_droit(200,dcG=DCB)

    elif(culDeSac):
        alert("cul De Sac")

        pivoter(0)
        pivoter(0)

    else:
        alert("else")
        servoPos('m')
        m = us_moy(5)
        if(m > 30):
            tout_droit(100,dcG=DCB)

        culDeSac = True


    #if(is_on_case() == (4,4) or is_on_case() == (-4,4)):
    #    fini = True

fin()