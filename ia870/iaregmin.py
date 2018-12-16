# -*- encoding: utf-8 -*-
# Module iaregmin

from numpy import *
from ia870.iasecross import iasecross

def iaregmin(f, Bc=iasecross(), option="binary"):
    from ia870.iahmin import iahmin
    from ia870.iaaddm import iaaddm
    from ia870.iasubm import iasubm
    from ia870.iabinary import iabinary
    from ia870.iasuprec import iasuprec
    from ia870.iaunion import iaunion
    from ia870.iathreshad import iathreshad

    if option != "binary":
        raise Exception("iaregmin accepts only binary option")

    return iabinary(iasubm(iahmin(f,1,Bc), f))

