# -*- encoding: utf-8 -*-
# Module ialastero

from numpy import *
from ia870.iasecross import iasecross

def ialastero(f, B=iasecross()):
    from ia870.iaisbinary import iaisbinary
    from ia870.iadist import iadist
    from ia870.iaregmax import iaregmax

    assert iaisbinary(f),'Can only process binary images'
    dt = iadist(f,B)
    y = iaregmax(dt,B)
    return y

