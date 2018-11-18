# -*- encoding: utf-8 -*-
# Module iagradm

def iagradm(f, Bdil=None, Bero=None):
    from ia870 import iasubm,iadil,iaero,iasecross

    if Bdil is None: Bdil = iasecross()
    if Bero is None: Bero = iasecross()

    y = iasubm( iadil(f,Bdil),iaero(f,Bero))
    return y

