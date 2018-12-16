# -*- encoding: utf-8 -*-
# Module iacloserec

from numpy import *
from ia870.iasecross import iasecross

def iacloserec(f, bdil=iasecross(), bc=iasecross()):
    from ia870.iasuprec import iasuprec
    from ia870.iadil import iadil

    return iasuprec( iadil(f,bdil),f,bc)

