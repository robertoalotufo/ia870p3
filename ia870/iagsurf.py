# -*- encoding: utf-8 -*-
# Module iagsurf

def iagsurf(f, vx=1, vy=0, vz=1):

    import numpy as np
    zd = np.pad(f,(1,1),'constant').astype(np.float)
    gv = zd[1:-1,2:] - zd[1:-1,1:-1]
    gv /= gv.max()
    gh = zd[2:,1:-1] - zd[1:-1,1:-1]
    gh /= gh.max()
    gz = 1.0/(gv**2 + gh**2 + 1)
    gv *= gz
    gh *= gz
    v = np.sqrt(vx*vx + vy*vy + vz*vz)
    vx = vx/v; vy = vy/v; vz = vz/v
    gv *= vx
    gh *= vy
    gz *= vz
    gz += gh + gv
    m,M = gz.min(),gz.max()
    gn = (255.*(gz - m)/(M-m)).astype(np.uint8)
    return gn

