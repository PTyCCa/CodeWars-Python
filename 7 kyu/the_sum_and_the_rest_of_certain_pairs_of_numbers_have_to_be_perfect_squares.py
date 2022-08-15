import numpy as np


def closest_pair_tonum(upper_lim):
    #your code Here

    for i in range(upper_lim - 1, upper_lim//2-1, -1):
        for j in range(i-1, 1, -1):
            if 0.0 == np.sqrt(i + j) % 1 and  0.0 == np.sqrt(i - j) % 1  and i > j:
                return (i, j)


def closest_pair_tonum_2(uLim):
    return next( (a,b) for a in reversed(range(1,uLim)) for b in reversed(range(1,a))
                       if not (a+b)**.5%1 and not (a-b)**.5%1 )