"""Physical projective centroid normalization, with full uniform mass.

For y=x/(1+p.x), the exact smooth-on-incidence derivative of the physical
volume centroid is dg/dp = -5 E[yy^T] + 4 gg^T. It is negative definite for a
full-dimensional solid. The tetrahedral second moment is integrated below.
All finite calculations are numerical nominations, not exact proof of g=0.
Final equilibrium auditing always uses the exact centroid of the saved body.
"""
import numpy as np
from scipy.spatial import ConvexHull
from vertex_geometry import geometry

def moment_jacobian(g):
    X=g['X'];T=g['T'];a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));s=a+b+c;M=(np.einsum('i,ij,ik->jk',v6,a,a)+np.einsum('i,ij,ik->jk',v6,b,b)+np.einsum('i,ij,ik->jk',v6,c,c)+np.einsum('i,ij,ik->jk',v6,s,s))/(120*g['V']);return -5*M+4*np.outer(g['g'],g['g'])

def normalize(X,DX=None,p0=None):
    X=np.asarray(X);hull=ConvexHull(X)
    if max(hull.equations[:,3])>=0:raise ValueError('projective normalization requires the reference origin inside the literal hull')
    p=np.zeros(3)if p0 is None else p0.copy();hist=[]
    for it in range(60):
        den=1+X@p
        if min(den)<=0:raise ValueError('nonpositive physical projective denominator')
        Y=X/den[:,None];g=geometry(Y,False);res=float(np.linalg.norm(g['g']));hist.append(res)
        if res<1e-14:break
        J=moment_jacobian(g);assert max(np.linalg.eigvalsh(J))<0;step=np.linalg.solve(J,-g['g']);ok=False
        for k in range(25):
            pp=p+2.**-k*step;dd=1+X@pp
            if min(dd)<=1e-10:continue
            gg=geometry(X/dd[:,None],False)
            if np.linalg.norm(gg['g'])<res*(1-1e-5):p=pp;ok=True;break
        if not ok:raise ValueError('physical projective centroid normalization failed to descend')
    else:raise ValueError('physical projective centroid normalization exceeded60 iterations')
    if DX is None:return g,p,hist
    g=geometry(Y,True);B=DX/den[:,None,None]-X[:,:,None]*np.einsum('c,icp->ip',p,DX)[:,None,:]/den[:,None,None]**2;J=moment_jacobian(g);Dp=np.linalg.solve(J,-g['Dg']@B.reshape(X.size,-1));DY=B-np.einsum('ic,ij,jp->icp',Y,Y,Dp);g['parameter_DX']=DY;g['normalization_Dp']=Dp;return g,p,hist
