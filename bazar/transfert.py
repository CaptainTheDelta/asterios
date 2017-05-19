def liberte()
    """ Renvoye le triplet (g,m,d) indiquant si les cases autour du robot sont libre:
    retourne 1 pour une direction libre, 0 pour une direction occuper (avec un mur)"""
    global sens
    mesures = mesure(sens)
    result = [0,0,0]
    for i in mesures:
        if i > 400:
            result[i] = 1
    return result