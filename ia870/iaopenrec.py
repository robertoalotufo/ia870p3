# -*- encoding: utf-8 -*-
# Module iaopenrec

from numpy import *
from ia870.iasecross import iasecross

def iaopenrec(f, bero=iasecross(), bc=iasecross()):
    from ia870.iainfrec import iainfrec
    from ia870.iaero import iaero

    return iainfrec( iaero(f,bero),f,bc)

