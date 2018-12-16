# -*- encoding: utf-8 -*-
# Module iaskelmrec

from numpy import *

def iaskelmrec(f, B=None):
    from ia870.iabinary import iabinary
    from ia870.iaintersec import iaintersec
    from ia870.iadil import iadil
    from ia870.iaunion import iaunion
    from ia870.iasecross import iasecross
    if B is None:
        B = iasecross(None)

    y = iabinary( iaintersec(f, 0))
    for r in range(max(ravel(f)),1,-1):
        y = iadil( iaunion(y,iabinary(f,r)), B)
    y = iaunion(y, iabinary(f,1))
    return y

