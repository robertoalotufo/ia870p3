# -*- encoding: utf-8 -*-
# Module iadist

import numpy as np
from ia870.iasecross import iasecross

def iadist(f, Bc=iasecross(), METRIC=None):
    from ia870 import iagray,iaintersec,iaisequal,iaero,iasebox

    if METRIC is not None: METRIC = METRIC.upper()
    f = iagray(f,'uint16')
    y = iaintersec(f,0)
    if (METRIC == 'EUCLIDEAN') or (METRIC == 'EUC2'):
        f = np.int32(f)
        b = np.int32(np.zeros((3,3)))
        i=1
        while np.any(f != y):
            a4,a2 = -4*i+2, -2*i+1
            b = np.int32([[a4,a2,a4],
                          [a2, 0,a2],
                          [a4,a2,a4]])
            y=f
            i=i+1
            f = iaero(f,b)
        if METRIC == 'EUCLIDEAN':
            y = np.uint16(np.sqrt(f)+0.5)
    else:
        if iaisequal(Bc, iasecross()):
            b = np.int32([[-2147483647,  -1, -2147483647],
                          [         -1,   0,          -1],
                          [-2147483647,  -1, -2147483647]])
        elif iaisequal(Bc, iasebox()):
            b = np.int32([[-1,-1,-1],
                          [-1, 0,-1],
                          [-1,-1,-1]])
        else: b = Bc
        while np.any(f != y):
            y=f
            f = iaero(f,b)
    return y

