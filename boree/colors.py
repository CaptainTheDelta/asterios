#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
Victor Herrmann                Concours Astérios                        15/05/17 
Damien Lesecq                     Groupe Borée                          19/05/17
--------------------------------------------------------------------------------
"""

# --------------------------------- Constantes ---------------------------------

DEBUG = True

reset='\033[0m'
bold='\033[01m'
disable='\033[02m'
underline='\033[04m'
reverse='\033[07m'
strikethrough='\033[09m'
invisible='\033[08m'

class fg:
    white='\033[0m'
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'

class bg:
    black='\033[40m'
    red='\033[41m'
    green='\033[42m'
    orange='\033[43m'
    blue='\033[44m'
    purple='\033[45m'
    cyan='\033[46m'
    lightgrey='\033[47m'

# ---------------------------------- Fonctions----------------------------------

def clr(value,fg=fg.white,bg=bg.black):
    """Renvoie la valeur avec l'encodage nécessaire pour mettre de la couleur.

    Args:
        value (value): Valeur à compléter.
        fg (str)[fg.white]: Couleur à appliquer au texte.
        bg (str)[bg.black]: Couleur à appliquer au fond.

    Return:
        (str): String.
    """
    return fg + bg + str(value) + reset


def dbg(value):
    """Permet un joli debug.

    Args:
        value (value): Valeur à compléter.

    Return:
        (str): String.
    """
    if(DEBUG):
        print("[DEBUG] "+str(value))


def alert(value):
    """Permet une jolie alerte.

    Args:
        value (value): Valeur à compléter.

    Return:
        (str): String.
    """
    print(clr("[ALERT] "+str(value),fg.red))


def warning(value):
    """Permet un joli warning.

    Args:
        value (value): Valeur à compléter.

    Return:
        (str): String.
    """
    print(clr("[WARNING] "+str(value),fg.orange))
