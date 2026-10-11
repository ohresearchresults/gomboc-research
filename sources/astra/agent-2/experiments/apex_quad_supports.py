"""Free physical support normals with one exact four-plane apex.

Four polar vertices lie exactly in z=1 and form the only prescribed polygon.
Every other support vector has z<1. Hence the primal contains the genuine
degree4 vertex (0,0,1). At most85 active facets then give E<=3F-7<=248.
All other hull incidences may change. The filled primal mass is integrated;
neither the polar centroid nor the coordinate origin substitutes for it.
"""
import sys,json,hashlib
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from gmpy2 import mpq
import jax
import jax.numpy as jnp
from selected_projective import load
from support_persistence import ROOT,barcode
from geometry import angular_scores
jax.config.update('jax_enable_x64',True)

@jax.jit
def unpack(q):return jnp.concatenate([jnp.c_[q[:8].reshape(4,2),jnp.ones(4)],q[8:].reshape(-1,3)],axis=0)

@jax.jit
def physical(q,R,T,A):
    H=unpack(q);other=jnp.linalg.solve(H[R[1:]],jnp.ones((len(R)-1,3,1))).squeeze(-1);X=jnp.concatenate([jnp.array([[0.,0.,1.]]),other],axis=0);a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),axis=1);g=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*six.sum());Z=X-g;Y=H[A]/(1-H[A]@g)[:,None]
    return X,Z,Y,g,six.sum()/6

def state(q):
    H=np.asarray(unpack(q));N=len(H)
    if not 4<N<=85 or np.max(H[4:,2])>=1-1e-10:raise ValueError('outside declared apex-support domain')
    if len(ConvexHull(H[:4,:2]).vertices)!=4:raise ValueError('apex star lost its fourth genuine facet')
    h=ConvexHull(H)
    if h.equations[:,3].max()>=-1e-9:raise ValueError('unbounded or boundary-origin physical intersection')
    dualtri=h.simplices;top=np.all(dualtri<4,axis=1)
    if top.sum()!=2:raise ValueError('unique prescribed polar quadrilateral is absent')
    R=np.r_[dualtri[np.flatnonzero(top)[:1]],dualtri[~top]];labels=np.empty(len(dualtri),int);labels[top]=0;labels[~top]=np.arange(1,1+(~top).sum());adj=defaultdict(list)
    for k,t in enumerate(dualtri):
        for i,j in zip(t,np.roll(t,-1)):adj[tuple(sorted((int(i),int(j))))].append(labels[k])
    if not all(len(v)==2 for v in adj.values()):raise ValueError('polar adjacency fails')
    ep=np.array([e for e,ff in adj.items() if ff[0]!=ff[1]],int);ed=np.array([ff for ff in adj.values() if ff[0]!=ff[1]],int);A=h.vertices;X=np.r_[[[0.,0.,1.]],np.linalg.solve(H[R[1:]],np.ones((len(R)-1,3,1))).squeeze(-1)]
    incidence=np.zeros((N,len(X)),bool);incidence[:4,0]=True
    for j,tri in enumerate(R[1:],1):incidence[tri,j]=True
    gaps=1-H@X.T
    if abs(gaps[incidence]).max()>1e-8 or gaps[~incidence].min()<1e-11:raise ValueError('additional non-simple contact or insufficient numerical separation')
    faces=[]
    for owner in A:
        links=defaultdict(list)
        for edge,dual in zip(ep,ed):
            if owner not in edge:continue
            a,b=map(int,dual);links[a].append(b);links[b].append(a)
        if not links or not all(len(v)==2 for v in links.values()):raise ValueError('primal facet adjacency fails')
        start=min(links);cy=[start];previous=None;now=start
        while True:
            nxt=next(x for x in links[now] if x!=previous)
            if nxt==start:break
            if nxt in cy:raise ValueError('primal facet cycle pinched')
            cy.append(nxt);previous,now=now,nxt
        if len(cy)!=len(links):raise ValueError('primal facet cycle incomplete')
        if np.cross(X[cy[1]]-X[cy[0]],X[cy[2]]-X[cy[0]])@H[owner]<0:cy=cy[::-1]
        faces.append(cy)
    T=np.array([[f[0],f[i],f[i+1]] for f in faces for i in range(1,len(f)-1)],int);X,Z,Y,g,v=map(np.asarray,physical(q,R,T,A));remap={int(v):i for i,v in enumerate(A)};eu=ed;es=np.array([[remap[int(a)],remap[int(b)]] for a,b in ep]);E=len(eu)
    if not 17<=E<=248 or len(X)-E+len(A)!=2 or v<=0:raise ValueError('physical counts/volume outside domain')
    pp,pw,P=barcode(Z,np.ones(len(Z)),eu);qp,qw,Q=barcode(Y,np.ones(len(Y)),es);P/=np.sum(Z[pp[:,0]]**2,axis=1);Q/=np.sum(Y[qp[:,0]]**2,axis=1);us=angular_scores(Z);ss=angular_scores(Y);up=us.argmax(1);sp=ss.argmax(1)
    return dict(H=H,X=X,Z=Z,Y=Y,g=g,volume=float(v),R=R,T=T,A=A,faces=faces,eu=eu,es=es,pp=pp,pw=pw,qp=qp,qw=qw,P=P,Q=Q,Pmax=float(P.max()),Qmax=float(Q.max()),S=int((ss.max(1)<0).sum()),U=int((us.max(1)<0).sum()),up=up,sp=sp,uguards=us[np.arange(len(Z)),up],sguards=ss[np.arange(len(Y)),sp],V=len(X),E=E,F=len(A),minimum_noncontact=float(gaps[~incidence].min()))

def create(src,out,seed=15971):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);X,H,tri,eu,es,r=load(src);g=np.array([float(mpq(v)) for v in r['raw_centroid']]);X-=g;H/= (1-H@g)[:,None]
    if r['counts'][1]!=1:raise ValueError('source must have exact unique U')
    u=r['unstable_vertices'][0];star=[i for i,f in enumerate(r['faces']) if u in f]
    if len(star)!=4 or len(H)>85:raise ValueError('source does not have the required 85-support/degree4 structure')
    radius=np.linalg.norm(X[u]);ez=X[u]/radius;e=np.eye(3)[np.argmin(abs(ez))];ex=e-ez*(e@ez);ex/=np.linalg.norm(ex);ey=np.cross(ez,ex);rotation=np.column_stack([ex,ey,ez]);H=H@rotation*radius;order=star+[i for i in range(len(H)) if i not in star];H=H[order];H[:4,2]=1.;q=np.r_[H[:4,:2].ravel(),H[4:].ravel()];np.save(out/'unreleased_q.npy',q);(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),star=star,order=order,centroid=g.tolist(),radius=float(radius),rotation=rotation.tolist(),scope='Euclidean frame then explicit generic perturbation; exact audit required'),indent=2)+'\n');rng=np.random.default_rng(seed);rows=[];best=(999,np.inf)
    for exponent in [10,9,8,7,6]:
        for j in range(5):
            qq=q+rng.normal(size=q.shape)*10.**(-exponent);name=f'e{exponent}_trial{j}';np.save(out/(name+'.npy'),qq)
            try:
                s=state(qq);row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(file=name+'.npy',jitter=10.**(-exponent),minimum_U_guard=float(s['uguards'][1:].min()));key=(s['U'],max(s['Pmax'],s['Qmax']))
                if key<best:best=key;np.save(out/'initial_q.npy',qq);(out/'best_release.json').write_text(json.dumps(row,indent=2)+'\n');print('APEX_QUAD_RELEASE',row,flush=True)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as e:row=dict(file=name+'.npy',error=repr(e))
            rows.append(row)
    (out/'release_screen.json').write_text(json.dumps(rows,indent=2)+'\n')
    if not (out/'initial_q.npy').exists():raise ValueError('no admitted separated apex-quad release')
    return np.load(out/'initial_q.npy')

if __name__=='__main__':create(ROOT/sys.argv[1],ROOT/sys.argv[2])
