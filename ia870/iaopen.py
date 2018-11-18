# -*- encoding: utf-8 -*-
# Module iaopen

def iaopen(f, b=None):
    from ia870 import iadil,iaero,iasecross
    
    if b is None:
        b = iasecross()

    y = iadil( iaero(f,b),b)

    return y

