# -*- encoding: utf-8 -*-
# Module iacdil

from numpy import *
from ia870.iasecross import iasecross

def iacdil(f, g, b=iasecross(), n=1):
    from ia870.iaintersec import iaintersec
    from ia870.iadil import iadil
    from ia870.iaisequal import iaisequal

    y = iaintersec(f,g)
    for i in range(n):
        aux = y
        y = iaintersec( iadil(y,b),g)
        if iaisequal(y,aux): break
    return y

