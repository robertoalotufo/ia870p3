# -*- encoding: utf-8 -*-
# Module iapatspec

from numpy import *

def iapatspec(f, type='OCTAGON', n=65535, Bc=None, Buser=None):
    from ia870.iaisbinary import iaisbinary
    from ia870.iaopentransf import iaopentransf
    from ia870.iahistogram import iahistogram
    from ia870.iasecross import iasecross
    if Bc is None:
        Bc = iasecross(None)
    if Buser is None:
        Buser = iasecross(None)

    assert iaisbinary(f),'Error: input image is not binary'
    g=iaopentransf(f,type,n,Bc,Buser)
    h=iahistogram(g)
    h=h[1:]
    return h

