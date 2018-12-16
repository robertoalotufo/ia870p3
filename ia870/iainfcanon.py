# -*- encoding: utf-8 -*-
# Module iainfcanon

from numpy import *

def iainfcanon(f, Iab, theta=45, DIRECTION="CLOCKWISE"):
    from ia870.iaunion import iaunion
    from ia870.iainterot import iainterot
    from ia870.iaintersec import iaintersec
    from ia870.iainfgen import iainfgen

    DIRECTION = DIRECTION.upper()
    y = iaunion(f,1)
    for t in range(0,360,theta):
        Irot = iainterot( Iab, t, DIRECTION )
        y = iaintersec( y, iainfgen(f, Irot))

    return y

