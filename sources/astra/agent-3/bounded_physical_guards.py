"""Direct facet-foot and angular vertex-edge guards on freshly recomputed hulls."""
from types import SimpleNamespace
import numpy as np
from contact_physical_110 import PhysicalGuards


def evaluate(g,kind,derivative=True):
    if kind=='vertices':
        active=g['vertices'];index={int(v):i for i,v in enumerate(active)}
        faces=[[index[int(i)]for i in tri]for tri in g['T']]
        X=g['Z'][active];Y=g['H'];Z=X;H=Y
        if derivative:DX=DZ=g['DZ'][active];DY=g['DH']
    else:
        faces=g['faces'];X=g['X'];Y=g['Q'][g['labels']];Z=g['Z'];H=g['H']
        if derivative:DX=g['DX'];DZ=g['DZ'];DY=g['DQ'][g['labels']]
    edges=set()
    for cy in faces:
        for i,j in zip(cy,cy[1:]+cy[:1]):edges.add(tuple(sorted((i,j))))
    T=np.array([(cy[0],cy[k],cy[k+1])for cy in faces for k in range(1,len(cy)-1)])
    if not derivative:
        # Zero directional dimensions evaluate the identical physical formula.
        DX=np.zeros((*X.shape,0));DZ=np.zeros((*Z.shape,0));DY=np.zeros((*Y.shape,0))
    c=SimpleNamespace(V=len(X),F=len(Y),faces=faces,pe=np.array(sorted(edges)),T=T)
    gg=dict(X=X,Y=Y,Z=Z,H=H,DX=DX,DZ=DZ,DY=DY)
    v,J,_,_,cl=PhysicalGuards(c,True).evaluate(gg)
    cl.update(V=len(X),F=len(Y))
    return v,J if derivative else None,cl
