#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
Victor Herrmann                Concours Astérios                        15/05/17 
Damien Lesecq                     Groupe Borée                          19/05/17
--------------------------------------------------------------------------------
"""

# ----------------------------------- Import -----------------------------------

import os
import time
import platform
import sys

from boree import *

from datetime import datetime

# --------------------------------- Affichage ----------------------------------

pVolt()

print("""Système :\t{}
Distribution :\t{}
Plateforme :\t{}
Version :\t{}
Machine :\t{}
Python :\t{}""".format(
    platform.system(),
    ' '.join(platform.dist()),
    platform.platform(),
    platform.version(),
    platform.machine(),
    sys.version.replace('\n','')
    ))

print("\nDernières modifications :")

print("Asterios :")
for file in os.listdir("/home/pi/Desktop/Asterios"):
    if(file[-3:] == '.py'):
        t  = datetime.fromtimestamp(os.path.getmtime(file)).strftime("%Y-%m-%d %H:%M:%S")
        
        print("{}\t{}".format(t,file))

dbg("fin")
#
#print("boree :")
#for file in os.listdir("/home/pi/Desktop/Asterios/boree"):
#    print("ok")
#    if(file[-3:] == '.py' and file != '__init__.py'):
#        t  = datetime.fromtimestamp(os.path.getmtime(file)).strftime("%Y-%m-%d %H:%M:%S")
#
#        if(file == "movement.py"):
#            file = clr(file,fg.green)
#            t = clr(t,fg.green)
#
#        print("{}\t{}".format(t,file))