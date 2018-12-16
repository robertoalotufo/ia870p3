# -*- encoding: utf-8 -*-
# Module iaaddm

import numpy as np

def iaaddm(f1, f2):
    from ia870.ialimits import ialimits

    if type(f2) is np.array:
        assert f1.dtype == f2.dtype, 'Cannot have different datatypes:'
    k1,k2 = ialimits(f1)
    y = np.clip(f1.astype(np.int64)+f2, k1, k2)
    y = y.astype(f1.dtype)
    return y

