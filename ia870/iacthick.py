# -*- encoding: utf-8 -*-
# Module iacthick

from numpy import *

def iacthick(f, g, Iab=None, n=-1, theta=45, DIRECTION="CLOCKWISE"):
    from ia870.iaisbinary import iaisbinary
    from ia870.iasupgen import iasupgen
    from ia870.iainterot import iainterot
    from ia870.iaintersec import iaintersec
    from ia870.iaunion import iaunion
    from ia870.iaisequal import iaisequal
    from ia870.iahomothick import iahomothick
    if Iab is None:
        Iab = iahomothick()

    DIRECTION = DIRECTION.upper()
    assert iaisbinary(f),'f must be binary image'
    if n == -1: n = product(f.shape)
    y = f
    old = y
    for i in range(n):
        for t in range(0,360,theta):
            sup = iasupgen( y, iainterot(Iab, t, DIRECTION))
            y = iaintersec( iaunion( y, sup),g)
        if iaisequal(old,y): break
        old = y

    return y

