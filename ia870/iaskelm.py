# -*- encoding: utf-8 -*-
# Module iaskelm

from numpy import *
from ia870.iasecross import iasecross

def iaskelm(f, B=iasecross(), option="binary"):
    from ia870.iaisbinary import iaisbinary
    from ia870.ialimits import ialimits
    from ia870.iagray import iagray
    from ia870.iaintersec import iaintersec
    from ia870.iasesum import iasesum
    from ia870.iaero import iaero
    from ia870.iaisequal import iaisequal
    from ia870.iaopenth import iaopenth
    from ia870.iasedil import iasedil
    from ia870.iaunion import iaunion
    from ia870.iabinary import iabinary
    from ia870.iapad import iapad
    from ia870.iaunpad import iaunpad

    assert iaisbinary(f),'Input binary image only'
    option = option.upper()
    f = iapad(f,B)
    print(f)
    k1,k2 = ialimits(f)
    y = iagray( iaintersec(f, k1),'uint16')
    iszero = asarray(y)
    nb = iasesum(B,0)
    for r in range(1,65535):
        ero = iaero( f, nb)
        if iaisequal(ero, iszero): break
        f1 = iaopenth( ero, B)
        nb = iasedil(nb, B)
        y = iaunion(y, iagray(f1,'uint16',r))
    if option == 'BINARY':
        y = iabinary(y)
    y = iaunpad(y,B)
    return y

