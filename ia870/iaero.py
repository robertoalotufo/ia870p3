# -*- encoding: utf-8 -*-
# Module iaero

def iaero(f, b=None):
    from ia870 import ianeg,iadil,iasereflect,iasecross

    if b is None: b = iasecross()
    y = ianeg( iadil( ianeg(f),iasereflect(b)))
    return y

