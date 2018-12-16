# -*- encoding: utf-8 -*-
# Module iahmin

from ia870.iasecross import iasecross

def iahmin(f, h=1, Bc=iasecross()):
    from ia870.iaaddm import iaaddm
    from ia870.iasuprec import iasuprec

    g = iaaddm(f,h)
    y = iasuprec(g,f,Bc)
    return y

