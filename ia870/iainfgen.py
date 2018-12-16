# -*- encoding: utf-8 -*-
# Module iainfgen

from numpy import *

def iainfgen(f, Iab):
    from ia870.iaunion import iaunion
    from ia870.iadil import iadil
    from ia870.ianeg import ianeg


    A, Bc = Iab
    y = iaunion( iadil(f, A), iadil( ianeg(f), Bc))

    return y

