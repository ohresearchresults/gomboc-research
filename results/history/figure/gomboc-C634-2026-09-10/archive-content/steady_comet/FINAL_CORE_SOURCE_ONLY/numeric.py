"""Numerical screening only. Exact certificates are generated separately."""
import itertools, json, numpy as np
from fractions import Fraction


def recover(data, controls=None):
    X=np.asarray(data['controls'],float)/data['grid'] if controls is None else np.asarray(controls,float).copy()
    n=data['n_supports']; X[n]=[0,0,1]
    for i,deps,axes in data['plan']:
        if deps:
            rest=[k for k in range(3) if k not in axes]
            X[i,axes]=np.linalg.solve(X[np.ix_(deps,axes)],1-X[np.ix_(deps,rest)]@X[i,rest])
    return X


def topology(faces):
    V=1+max(max(c) for c in faces)
    owners=[[] for _ in range(V)]
    ef={}
    for fi,cy in enumerate(faces):
        for v in cy:owners[v].append(fi)
        for a,b in zip(cy,cy[1:]+cy[:1]):ef.setdefault(tuple(sorted((a,b))),[]).append(fi)
    assert all(len(c)>=3 for c in owners)
    assert all(len(x)==2 for x in ef.values())
    assert V-len(ef)+len(faces)==2
    return owners,ef


def triangles(faces):
    return np.array([(cy[0],cy[k],cy[k+1]) for cy in faces for k in range(1,len(cy)-1)],dtype=int)


def best_triples(q,owners):
    out=[]
    for cy in owners:
        cs=np.array(list(itertools.combinations(cy,3)),dtype=int)
        out.append(cs[np.argmax(np.abs(np.linalg.det(q[cs])))])
    return np.array(out,dtype=int)


def vertices(q,owners,triples=None):
    if triples is None:triples=best_triples(q,owners)
    return np.linalg.solve(q[triples],np.ones((len(triples),3,1)))[:,:,0]


def mechanics(q,faces,P=None,details=False,tol=1e-8):
    owners,ef=topology(faces)
    if P is None:P=vertices(q,owners)
    inc=np.zeros((len(P),len(q)),bool)
    for i,cy in enumerate(owners):inc[i,cy]=True
    gaps=1-P@q.T; mg=float(gaps[~inc].min()); ie=float(np.abs(gaps[inc]).max())
    tri=triangles(faces);a,b,c=P[tri[:,0]],P[tri[:,1]],P[tri[:,2]]
    dv=np.einsum('ij,ij->i',a,np.cross(b,c))/6
    vol=dv.sum(); moment=(dv[:,None]*(a+b+c)/4).sum(0); cent=moment/vol
    x=P-cent; hh=1-q@cent; n=q/hh[:,None]
    # Strict maxima of the convex squared-radius functions, on primal and polar.
    def esc(z):
        dot=z@z.T; zz=np.diag(dot); num=dot-zz[:,None]
        dist=np.linalg.norm(z[None,:,:]-z[:,None,:],axis=2)
        den=np.linalg.norm(z,axis=1)[:,None]*dist
        cos=np.divide(num,den,out=np.full_like(num,-np.inf),where=den>1e-15)
        np.fill_diagonal(num,-np.inf); np.fill_diagonal(cos,-np.inf)
        return num,cos
    su,scos=esc(n);uu,ucos=esc(x)
    S=np.where(su.max(1)<-tol)[0].tolist();U=np.where(uu.max(1)<-tol)[0].tolist()
    E=np.array(sorted(ef),int);pol=np.array([ef[tuple(e)] for e in E],int)
    a=x[E[:,0]]; d=x[E[:,1]]-a; dd=np.einsum('ij,ij->i',d,d)
    t=-np.einsum('ij,ij->i',a,d)/dd; z=a+t[:,None]*d
    ni=n[pol[:,0]];nj=n[pol[:,1]]
    aa=np.einsum('ij,ij->i',ni,ni);bb=np.einsum('ij,ij->i',ni,nj);cc=np.einsum('ij,ij->i',nj,nj)
    rr=np.einsum('ij,ij->i',z,ni); ss=np.einsum('ij,ij->i',z,nj); D=aa*cc-bb*bb
    al=(rr*cc-ss*bb)/D;be=(ss*aa-rr*bb)/D
    ev=np.array([t,1-t,al,be]).T
    HS=np.flatnonzero(ev.min(1)>tol)
    out=dict(V=len(P),E=len(E),F=len(q),counts=[len(S),len(U),len(HS)],S=S,U=U,H=E[HS].tolist(),Hpolar=pol[HS].tolist(),volume=float(vol),centroid=cent.tolist(),min_gap=mg,max_incidence_error=ie,min_tetra=float(dv.min()),min_height=float(hh.min()),polar_escape_min=float(np.delete(scos.max(1),S).min()) if len(S)<len(q) else None,primal_escape_min=float(np.delete(ucos.max(1),U).min()) if len(U)<len(P) else None)
    if details:out.update(P=P,q=q,n=n,x=x,scos=scos,ucos=ucos,gaps=gaps,inc=inc,owners=owners,edges=E,polar_edges=pol,edge_values=ev,tri=tri)
    return out


def merge_faces(faces,a,b):
    # preserve orientation and support row IDs; deterministic vertex renumbering.
    keep=[i for i in range(1+max(max(c) for c in faces)) if i!=b]
    idx={i:k for k,i in enumerate(keep)};idx[b]=idx[a]
    out=[]
    for cy in faces:
        cc=[]
        for v in cy:
            j=idx[v]
            if not cc or j!=cc[-1]:cc.append(j)
        if len(cc)>1 and cc[0]==cc[-1]:cc.pop()
        if len(cc)<3 or len(set(cc))<len(cc):raise ValueError('collapsed support or non-simple boundary')
        out.append(cc)
    topology(out)
    return out


def snapped(data,faces,a,b, moved):
    """Extend existing contact atlas by merging edge a,b; move only support `moved`.
    The endpoint not incident to `moved` must supply an old/new contact point.
    The moved support must have no downstream chart dependents.
    """
    owners,ef=topology(faces)
    assert tuple(sorted((a,b))) in ef
    if moved in owners[a] and moved not in owners[b]:a,b=b,a
    assert moved not in owners[a] and moved in owners[b]
    union=sorted(set(owners[a])|set(owners[b]))
    assert set(owners[b])-set(owners[a])=={moved}
    assert not any(moved in deps for i,deps,ax in data['plan'])
    z=json.loads(json.dumps(data));n=z['n_supports']; X=recover(z)
    step=next(t for t in z['plan'] if t[0]==moved)
    assert len(step[1])<3
    z['plan'].remove(step)
    groups=z['groups']
    found=[k for k,c in enumerate(groups) if set(c)==set(owners[a])]
    if found:
        gi=found[0];pidx=n+gi;groups[gi]=union
    else:
        assert len(owners[a])==3
        gi=len(groups);pidx=len(z['controls']);assert pidx==n+gi
        p=np.linalg.solve(X[owners[a]],np.ones(3));z['controls'].append(np.rint(p*z['grid']).astype(np.int64).tolist());groups.append(union)
        z['plan'].append([pidx,owners[a],[0,1,2]])
        X=np.vstack([X,p])
    deps=step[1]+[pidx]
    axes=max(itertools.combinations(range(3),len(deps)), key=lambda ax:abs(np.linalg.det(X[np.ix_(deps,ax)])))
    assert abs(np.linalg.det(X[np.ix_(deps,axes)]))>1e-10
    z['plan'].append([moved,deps,list(axes)])
    nf=merge_faces(faces,a,b)
    return z,nf
