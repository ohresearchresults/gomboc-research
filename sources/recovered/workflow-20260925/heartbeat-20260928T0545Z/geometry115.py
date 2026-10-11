"""Numerical true-face geometry, actual uniform mass and full radial graph bars.
For numerical search only; roundoff thresholds are explicit and no exact
strict/weak classification is claimed by this module.
"""
import numpy as np
from scipy.spatial import ConvexHull
from collections import defaultdict

def read_h(path):
    a=np.loadtxt(path,skiprows=1); header=open(path).readline().split()
    assert len(a)==int(header[0]); return a/float(header[1])

def geometry(n):
    n=np.asarray(n,dtype=float)
    qh=ConvexHull(n)
    if qh.equations[:,3].max()>=-1e-10: raise ValueError('origin not inside polar')
    # Generic input assumption: dual hull facets are triangles. Reject any
    # nontriangular polar facet rather than counting triangulation diagonals.
    normals=qh.equations[:,:3]; offs=qh.equations[:,3]
    vs=-normals/offs[:,None]
    if len(vs)>1:
        from scipy.spatial.distance import pdist
        if pdist(vs).min()<1e-9: raise ValueError('nongeneric input: merged dual facet')
    tri=qh.simplices.copy()
    faces={}; polys=[]; total=0.; first=np.zeros(3)
    for j in qh.vertices:
        inds=np.where(np.any(tri==j,axis=1))[0]
        a=n[j]; axis=np.eye(3)[np.argmin(abs(a))]
        e=np.cross(a,axis); e/=np.linalg.norm(e); f=np.cross(a,e)
        c=vs[inds].mean(axis=0); delta=vs[inds]-c
        inds=inds[np.argsort(np.arctan2(delta@f,delta@e))]
        faces[int(j)]=inds.tolist()
        for b,cidx in zip(inds[1:-1],inds[2:]):
            ids=[inds[0],b,cidx]; x=vs[ids]
            d=np.linalg.det(x)/6
            if d<=0: raise ValueError('nonpositive tetrahedron')
            total+=d;first+=d*x.sum(axis=0)/4;polys.append(ids)
    g=first/total
    ed={}
    for j,ids in faces.items():
        for a,b in zip(ids,ids[1:]+ids[:1]):ed.setdefault(tuple(sorted((a,b))),[]).append(j)
    if any(len(a)!=2 for a in ed.values()):raise ValueError('bad edge incidence')
    pe=np.array(sorted(ed),int); qe=np.array([ed[tuple(x)] for x in pe],int)
    assert len(vs)-len(ed)+len(faces)==2
    assert np.max(vs@n.T-1)<1e-7
    p=vs-g; q=n/(1-n@g)[:,None]
    return dict(n=n,vertices=vs,triples=tri,faces=faces,edges=pe,dual_edges=qe,
                tetrahedra=np.asarray(polys,int),g=g,volume=total,p=p,q=q,active=qh.vertices)

def bars(x,edges):
    """0D superlevel persistence of ||x||^2 on the continuous edge graph.
    Includes every positive float difference; consumers must state any cutoff.
    Returns [(depth, birth vertex, death edge, squared birth, squared death)].
    """
    sq=np.einsum('ij,ij->i',x,x)
    d=x[edges[:,1]]-x[edges[:,0]];dd=np.einsum('ij,ij->i',d,d)
    t=np.clip(-np.einsum('ij,ij->i',x[edges[:,0]],d)/dd,0,1)
    z=x[edges[:,0]]+t[:,None]*d;level=np.einsum('ij,ij->i',z,z)
    order=np.argsort(-level,kind='stable');parent=np.arange(len(x));birth=np.arange(len(x));out=[]
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for k in order:
        a,b=map(int,edges[k]);ra,rb=find(a),find(b)
        if ra==rb:continue
        if (sq[birth[ra]],-birth[ra])<(sq[birth[rb]],-birth[rb]):ra,rb=rb,ra
        bi=int(birth[rb]);death=float(level[k]);dep=(float(sq[bi])-death)/float(sq[bi])
        if dep>0:out.append((dep,bi,[a,b],float(sq[bi]),death))
        parent[rb]=ra
    return sorted(out,reverse=True)

def census(m,tol=1e-10):
    p,q=m['p'],m['q']; pe,qe=m['edges'],m['dual_edges'];nr=len(q)
    def scores(x,ed,active):
        s=np.full(len(x),-np.inf)
        for a,b in ed:
            s[a]=max(s[a],x[a]@(x[b]-x[a]));s[b]=max(s[b],x[b]@(x[a]-x[b]))
        return s,np.array([i for i in active if s[i]<-tol],int)
    ps,u=scores(p,pe,range(len(p)));qs,s=scores(q,qe,m['active'])
    P=bars(p,pe);Q=bars(q,qe)
    return dict(V=len(p),E=len(pe),F=len(m['faces']),g=m['g'].tolist(),volume=m['volume'],
                U=u.tolist(),S=s.tolist(),P=[z for z in P if z[0]>1e-12],Q=[z for z in Q if z[0]>1e-12],
                rawPcount=len(P),rawQcount=len(Q),
                physical_scores=ps,polar_scores=qs)

if __name__=='__main__':
    import sys,json
    m=geometry(read_h(sys.argv[1])); c=census(m)
    print(json.dumps({k:v for k,v in c.items() if not k.endswith('scores')},indent=2))
    for i in c['U']:print('U',i,'triple',m['triples'][i].tolist(),'point',m['p'][i].tolist())
    s=c['S'][0];r=m['q'][s]
    for i in c['U']:
        p=m['p'][i];print('direct-stable-cut support',i,(r@p+np.linalg.norm(r)*np.linalg.norm(p))/2)
