# -*- encoding: utf-8 -*-
# Module iaopenrecth

from numpy import *

def iaopenrecth(f, bero=None, bc=None):
    from ia870.iasubm import iasubm
    from ia870.iaopenrec import iaopenrec
    from ia870.iasecross import iasecross
    if bero is None:
        bero = iasecross()
    if bc is None:
        bc = iasecross()

    y = iasubm(f, iaopenrec( f, bero, bc))

    return y

