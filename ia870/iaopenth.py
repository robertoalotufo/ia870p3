# -*- encoding: utf-8 -*-
# Module iaopenth

from numpy import *

def iaopenth(f, b=None):
    from ia870.iasubm import iasubm
    from ia870.iaopen import iaopen
    from ia870.iasecross import iasecross
    if b is None:
        b = iasecross()

    y = iasubm(f, iaopen(f,b))

    return y

