# -*- encoding: utf-8 -*-
# Module iaclose

def iaclose(f, b=None):
    from ia870 import iaero,iadil,iasecross

    if b is None:
        b = iasecross()

    y = iaero( iadil(f,b),b)

    return y

