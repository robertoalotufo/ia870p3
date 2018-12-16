# -*- encoding: utf-8 -*-
# Module iasupgen

from numpy import *

def iasupgen(f, INTER):
    from ia870.iaintersec import iaintersec
    from ia870.iaero import iaero
    from ia870.ianeg import ianeg


    A,Bc = INTER
    y = iaintersec( iaero( f, A),
                   iaero( ianeg(f), Bc))

    return y

