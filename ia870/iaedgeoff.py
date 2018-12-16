# -*- encoding: utf-8 -*-
# Module iaedgeoff

from numpy import *
from ia870.iasecross import iasecross

def iaedgeoff(f, Bc=iasecross()):
    from ia870.iaframe import iaframe
    from ia870.iasubm import iasubm
    from ia870.iainfrec import iainfrec

    edge = iaframe(f)
    return iasubm( f, iainfrec(edge, f, Bc))

