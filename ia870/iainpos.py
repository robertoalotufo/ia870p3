# -*- encoding: utf-8 -*-
# Module iainpos

from numpy import *
from ia870.iasecross import iasecross

def iainpos(f, g, bc=iasecross()):
    from ia870.iaisbinary import iaisbinary
    from ia870.iagray import iagray
    from ia870.ianeg import ianeg
    from ia870.iadatatype import iadatatype
    from ia870.ialimits import ialimits
    from ia870.iasuprec import iasuprec
    from ia870.iaintersec import iaintersec
    from ia870.iaunion import iaunion

    assert iaisbinary(f),'First parameter must be binary image'
    fg = iagray( ianeg(f), iadatatype(g))
    k1 = ialimits(g)[1] - 1
    y = iasuprec(fg, iaintersec( iaunion(g, 1), k1, fg), bc)

    return y

