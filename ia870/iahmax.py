# -*- encoding: utf-8 -*-
# Module iahmax

from numpy import *
from ia870.iasecross import iasecross

def iahmax(f, h=1, Bc=iasecross()):
    from ia870.iasubm import iasubm
    from ia870.iainfrec import iainfrec

    g = iasubm(f,h)
    y = iainfrec(g,f,Bc);
    return y

