# -*- encoding: utf-8 -*-
# Module iaintershow

from numpy import *

def iaintershow(Iab):
    from ia870.iaseunion import iaseunion
    from ia870.iaintersec import iaintersec


    assert (type(Iab) is tuple) and (len(Iab) == 2),'not proper fortmat of hit-or-miss template'
    A,Bc = Iab
    S = iaseunion(A,Bc)
    Z = iaintersec(S,0)
    n = product(S.shape)
    one  = reshape(array(n*'1','c'),S.shape)
    zero = reshape(array(n*'0','c'),S.shape)
    x    = reshape(array(n*'.','c'),S.shape)
    saux = choose( S + iaseunion(Z,A), ( x, zero, one))

    return '\n'.join([ss.tostring().decode() for ss in saux])

