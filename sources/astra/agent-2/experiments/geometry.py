"""Numerical discovery only. Final claims require a separate exact audit."""
import numpy as np
from scipy.spatial import ConvexHull, HalfspaceIntersection

def hull_from_supports(Y,tol=1e-8):
    Y=np.asarray(Y,float)
    hi=HalfspaceIntersection(np.c_[Y,-np.ones(len(Y))],np.zeros(3))
    # Qhull may produce repeated representations of nonsimple vertices.
    X=hi.intersections
    keep=[]
    for x in X:
        if not keep or np.min(np.linalg.norm(np.array(keep)-x,axis=1))>tol:
            keep.append(x)
    X=np.array(keep)
    faces=[]; active=[]
    for i,y in enumerate(Y):
        ids=np.flatnonzero(np.abs(X@y-1)<tol)
        if len(ids)<3:continue
        n=y/np.linalg.norm(y)
        axis=np.eye(3)[np.argmin(np.abs(n))]
        a=np.cross(n,axis);a/=np.linalg.norm(a);b=np.cross(n,a)
        xy=X[ids]@np.array([a,b]).T
        q=ConvexHull(xy)
        faces.append(ids[q.vertices].tolist());active.append(i)
    verts=sorted(set(j for f in faces for j in f));remap={v:k for k,v in enumerate(verts)}
    X=X[verts];faces=[[remap[j] for j in f] for f in faces]
    edges={tuple(sorted((a,b))) for f in faces for a,b in zip(f,f[1:]+f[:1])}
    assert len(X)-len(edges)+len(faces)==2,(len(X),len(edges),len(faces))
    tri=np.array([[f[0],f[k],f[k+1]] for f in faces for k in range(1,len(f)-1)])
    return X,Y[active],faces,tri,len(edges),np.array(active)

def mass(X,tri):
    a,b,c=X[tri[:,0]],X[tri[:,1]],X[tri[:,2]]
    six=np.einsum('ij,ij->i',a,np.cross(b,c))
    vol=np.sum(six)/6
    centroid=np.sum(six[:,None]*(a+b+c),axis=0)/(24*vol)
    return vol,centroid

def angular_scores(X):
    delta=X[None,:,:]-X[:,None,:]
    score=np.einsum('ik,ijk->ij',X,delta)
    score/=np.maximum(np.linalg.norm(delta,axis=2),1e-30)*np.linalg.norm(X,axis=1)[:,None]
    np.fill_diagonal(score,-np.inf)
    return score

def escape(X,angular=True):
    if angular:score=angular_scores(X)
    else:
        score=np.einsum('ik,ijk->ij',X,X[None,:,:]-X[:,None,:]);np.fill_diagonal(score,-np.inf)
    return score.max(axis=1),score.argmax(axis=1)

def transform(X,Y,tri,t):
    b=t[:3];den=1+X@b
    if den.min()<=0:return None
    Z=X/den[:,None];vol,c=mass(Z,tri);Q=Y+b
    dh=1-Q@c
    if dh.min()<=0 or vol<=0:return None
    Q=Q/dh[:,None];Z=Z-c
    L=np.array([[np.exp(t[3]),0,0],[t[5],np.exp(t[4]),0],[t[6],t[7],np.exp(-t[3]-t[4])]])
    return Z@L,Q@np.linalg.inv(L).T,c,vol

def summary(X,Y,tri):
    vol,c=mass(X,tri);Z=X-c;Q=Y/(1-Y@c)[:,None]
    u,ui=escape(Z);s,si=escape(Q)
    return {'V':len(X),'F':len(Y),'S':int(np.sum(s<0)),'U':int(np.sum(u<0)),
      'volume':float(vol),'centroid':c.tolist(),'stable':np.flatnonzero(s<0).tolist(),
      'unstable':np.flatnonzero(u<0).tolist(),'u_second':float(np.sort(u)[1]),'s_second':float(np.sort(s)[1])}
