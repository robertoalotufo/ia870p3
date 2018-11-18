# -*- encoding: utf-8 -*-
# Module ianeg

def ianeg(f):
    from ia870 import ialimits

    if f.dtype == bool:
        return ~ f
    elif ialimits(f)[0] == (- ialimits(f)[1]):
       y = -f
    else:
       y = ialimits(f)[0] + ialimits(f)[1] - f
    y = y.astype(f.dtype)
    return y

