# -*- encoding: utf-8 -*-
# Module iasuprec

import numpy as np
from ia870.iasecross import iasecross

def iasuprec(f, g, Bc=iasecross()):
    from ia870.iacero import iacero
    
    n = np.product(f.shape)
    y = iacero(f,g,Bc,n)
    return y

