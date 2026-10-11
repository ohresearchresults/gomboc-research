"""Continuous maximum-bottleneck root capacities and active edge witnesses.
For fixed distinct vectors/root set, max_path min_edge W(edge) is a continuous
function of the finite directed escape matrix. A chosen tree's sum of direct
edge penalties need not be continuous when the tree changes. This module returns
the actual capacities, retaining an active edge for each coordinate derivative.
"""
import numpy as np
from geometry import arrows

def capacities(A,roots):
    W=arrows(A);n=len(A);cap=np.full(n,-np.inf);cap[roots]=np.inf;done=np.zeros(n,bool);ii=np.full(n,-1,int);jj=np.full(n,-1,int)
    for _ in range(n):
        j=int(np.argmax(np.where(done,-np.inf,cap)));done[j]=True;candidate=np.minimum(cap[j],W[:,j]);take=(candidate>cap)&(~done)
        for i in np.flatnonzero(take):
            cap[i]=candidate[i]
            if W[i,j]<=cap[j]:ii[i]=i;jj[i]=j
            else:ii[i]=ii[j];jj[i]=jj[j]
    signs=np.ones(n)
    for r in roots:ii[r]=r;jj[r]=int(W[r].argmax());cap[r]=-W[r,jj[r]];signs[r]=-1
    assert np.all(ii>=0) and np.all(jj>=0)
    assert np.max(abs(cap-signs*W[ii,jj]))<1e-12
    return cap,ii,jj,signs
