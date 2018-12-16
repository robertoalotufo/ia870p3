# -*- encoding: utf-8 -*-
# Module iatoggle

from numpy import *

def iatoggle(f, f1, f2, OPTION="GRAY"):
    from ia870.iabinary import iabinary
    from ia870.iasubm import iasubm
    from ia870.iagray import iagray
    from ia870.iaunion import iaunion
    from ia870.iaintersec import iaintersec
    from ia870.ianeg import ianeg


    y=iabinary( iasubm(f,f1),iasubm(f2,f))
    if OPTION.upper() == 'GRAY':
        t=iagray(y)
        y=iaunion( iaintersec( ianeg(t),f1),iaintersec(t,f2))


    return y

