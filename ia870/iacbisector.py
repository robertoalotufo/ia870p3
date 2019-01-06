# -*- encoding: utf-8 -*-
# Module iacbisector

from numpy import *

def iacbisector(f, B, n):
    from ia870.iaintersec import iaintersec
    from ia870.iasesum import iasesum
    from ia870.iaero import iaero
    from ia870.iacdil import iacdil
    from ia870.iasubm import iasubm
    from ia870.iaunion import iaunion

    y = iaintersec(f,0)
    for i in range(n):
        nb = iasesum(B,i)
        nbp = iasesum(B,i+1)
        f1 = iaero(f,nbp)
        f2 = iacdil(f1,f,B,n)
        f3 = iasubm( iaero(f,nb),f2)
        y  = iaunion(y,f3)
    return y

