# -*- encoding: utf-8 -*-
# Module iaclohole

from ia870.iasecross import iasecross

def iaclohole(f, Bc=iasecross()):
    from ia870.iaframe import iaframe
    from ia870.ianeg import ianeg
    from ia870.iainfrec import iainfrec

    delta_f = iaframe(f)
    return ianeg( iainfrec( delta_f, ianeg(f), Bc))

