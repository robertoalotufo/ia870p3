# -*- encoding: utf-8 -*-
# Module iaimg2se

from numpy import *

def iaimg2se(fd, FLAT="FLAT", f=None):
    from ia870 import iaisbinary, iaseshow, ialimits

    fd = (fd > 0)
    #assert iaisbinary(fd),'First parameter must be binary'
    FLAT = FLAT.upper()
    if FLAT == 'FLAT':
        return iaseshow(fd)
    else:
        B = choose(fd, ( ialimits(int32([0]))[0]*ones(fd.shape),f) )
    B = iaseshow(int32(B),'NON-FLAT')

    return B

