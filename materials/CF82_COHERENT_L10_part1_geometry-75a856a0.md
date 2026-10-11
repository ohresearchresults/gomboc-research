# material-75a856a046bd

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Numerical convex geometry, true edge graphs, filled mass and whole elder gaps.
Discovery only. Integer/rational predicates are required for promotion.
"""
import itertools
import numpy as np
from scipy.spatial import ConvexHull

def geometry(Y):
    Y=np.asarray(Y,dtype=float)
    h=ConvexHull(Y)
    t=h.simplices.copy()
    a,b,c=Y[t[:,0]],Y[t[:,1]],Y[t[:,2]]
    flip=np.einsum('ij,ij->i',np.cross(b-a,c-a),h.equations[:,:3])<0
    t[flip]=t[flip][:,[0,2,1]]
    a,b,c=Y[t[:,0]],Y[t[:,1]],Y[t[:,2]]
    anchor=Y[h.vertices].mean(0)
    vv=np.einsum('ij,ij->i',a-anchor,np.cross(b-anchor,c-anchor))/6
    volume=vv.sum()
    g=(vv[:,None]*(a+b+c+anchor)).sum(0)/(4*volume)
    # Group numerical coplanar triangles to avoid diagonal edges in graph reports.
    groups={};labels=[]
    for eq in h.equations:
        labels.append(groups.setdefault(tuple(np.round(eq,10)),len(groups)))
    eq=np.array([h.equations[labels.index(i)] for i in range(len(groups))])
    faces=[set() for _ in groups]; own={}
    for f,tri in zip(labels,t):
        faces[f].update(map(int,tri))
        for i,j in itertools.combinations(tri,2):
            own.setdefault(tuple(sorted((int(i),int(j)))),set()).add(f)
    own={e:sorted(fs) for e,fs in own.items() if len(fs)>1}
    assert all(len(fs)==2 for fs in own.values())
    ids=h.vertices; ix={int(v):k for k,v in enumerate(ids)}
    E=np.array([[ix[i],ix[j]] for i,j in own],dtype=int)
    QE=np.array(list(own.values()),dtype=int)
    Q=eq[:,:3]/(-eq[:,3]-eq[:,:3]@g)[:,None]
    return dict(Y=Y,T=t,ids=ids,raw_edges=np.array(list(own)),E=E,QE=QE,
                X=Y[ids]-g,Q=Q,volume=float(volume),g=g,
                faces=[sorted(f) for f in faces],eq=eq)

def scores(X,E):
    D=X[E[:,1]]-X[E[:,0]];ll=np.linalg.norm(D,axis=1)
    r=np.linalg.norm(X,axis=1);v=np.full(len(X),-np.inf);target=np.full(len(X),-1)
    for i in range(len(E)):
        a,b=E[i];s=X[a]@D[i]/r[a]/ll[i];s1=-X[b]@D[i]/r[b]/ll[i]
        if s>v[a]:v[a],target[a]=s,b
        if s1>v[b]:v[b],target[b]=s1,a
    return v,target

def bars(X,E):
    R=(X*X).sum(1);D=X[E[:,1]]-X[E[:,0]]
    t=np.clip(-np.einsum('ij,ij->i',X[E[:,0]],D)/(D*D).sum(1),0,1)
    height=((X[E[:,0]]+t[:,None]*D)**2).sum(1)
    par=list(range(len(X)));out=[]
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for k in sorted(range(len(E)),key=lambda k:(height[k],*E[k]),reverse=True):
        a,b=map(find,E[k])
        if a==b:continue
        if (R[a],-a)<(R[b],-b):a,b=b,a
        if R[b]-height[k]>1e-12*max(R):
            out.append(dict(peak=int(b),elder=int(a),edge=E[k].tolist(),birth=float(R[b]),death=float(height[k]),depth=float(R[b]-height[k])))
        par[b]=a
    return out

def report(Y):
    z=geometry(Y);p,pt=scores(z['X'],z['E']);q,qt=scores(z['Q'],z['QE'])
    pb,qb=bars(z['X'],z['E']),bars(z['Q'],z['QE'])
    volume=z['volume'];etas=[(b['death']**(-.5)-b['birth']**(-.5))/2/volume**(1/3) for b in qb]
    return dict(V=len(z['X']),E=len(z['E']),F=len(z['Q']),S=int((q< -1e-10).sum()),U=int((p< -1e-10).sum()),
      volume=volume,centroid=z['g'].tolist(),unstable_inputs=z['ids'][p< -1e-10].tolist(),stable_faces=[z['faces'][i] for i in np.where(q< -1e-10)[0]],
      Pbars=pb,Qbars=qb,eta=max(etas,default=0.),sum_eta=sum(etas),physical_guard=float(np.min(np.delete(p,np.argmax((z['X']**2).sum(1))))),
      TP=sum(b['depth'] for b in pb)/volume**(2/3),TQ=sum(b['depth'] for b in qb)*volume**(2/3))
