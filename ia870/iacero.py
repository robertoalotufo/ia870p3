# -*- encoding: utf-8 -*-
# Module iacero

from numpy import *
from ia870.iasecross import iasecross

def iacero(f, g, b=iasecross(), n=1):
    from ia870.iaunion import iaunion
    from ia870.iaero import iaero
    from ia870.iaisequal import iaisequal

    y = iaunion(f,g)
    for i in range(n):
        aux = y
        y = iaunion( iaero(y,b),g)
        if iaisequal(y,aux): break
    return y

