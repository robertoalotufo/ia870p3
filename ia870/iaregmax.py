# -*- encoding: utf-8 -*-
# Module iaregmax

from numpy import *
from ia870.iasecross import iasecross

def iaregmax(f, Bc=iasecross()):
    from ia870.iasubm import iasubm
    from ia870.iahmax import iahmax
    from ia870.iabinary import iabinary
    from ia870.iaregmin import iaregmin
    from ia870.ianeg import ianeg

    y = iasubm(f, iahmax(f,1,Bc))
    return iabinary(y)
    #return iaregmin( ianeg(f),Bc)

