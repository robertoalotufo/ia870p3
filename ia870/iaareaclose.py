# -*- encoding: utf-8 -*-
# Module iaareaclose

def iaareaclose(f, a, Bc=None):
    from ia870 import ianeg,iaareaopen,iasecross

    if Bc is None:
        Bc = iasecross()
    y = ianeg( iaareaopen( ianeg(f),a,Bc))
    return y

