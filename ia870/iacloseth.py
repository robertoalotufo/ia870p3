# -*- encoding: utf-8 -*-
# Module iacloseth

from numpy import *

def iacloseth(f, b=None):
    from ia870.iasubm import iasubm
    from ia870.iaclose import iaclose
    from ia870.iasecross import iasecross
    if b is None:
        b = iasecross()

    y = iasubm( iaclose(f,b), f)
    return y

