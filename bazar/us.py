from init import *


def us_moy(n):
    """Renvoie la moyenne des n prises de mesures us.

    Args:
        n (int): Nombre de mesures.

    Return:
        (float): Valeur moyenne des distances.
    """
    return sum([us_dist(pin=1) for i in range(n)]) / n

for i in range(100):
    print('\r'+str(us_moy(5)))