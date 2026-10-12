# material-396dd247b013

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""True homogeneous polar/projective-metric orbit of literal H44 G6.
Numerical search only. Imports the complete h44_lead_probe.py input/probe.
Run --baseline or --search; all search parameters are explicit in main.
"""
import argparse, json, platform, time
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import minimize
from h44_lead_probe import seed, geometry, barcodes

Q0=seed()
V0,faces,rows,owner,volume,centroid=geometry(Q0)
tri=[]
for vi in range(len(V0)):
    ix=[int(rows[j]) for j,f in enumerate(faces) if vi in f]
    if len(ix)!=3:raise ValueError('expected simple primal vertex')
    if np.linalg.det(Q0[ix])<0:ix[1],ix[2]=ix[2],ix[1]
    tri.append(ix)
TRI=np.asarray(tri,dtype=int)
OWN={}
for fi,t in enumerate(TRI):
    for i in range(3):OWN.setdefault(tuple(sorted((int(t[i]),int(t[(i+1)%3])))),[]).append(fi)
ED=np.asarray(list(OWN),dtype=int)
DE=np.asarray(list(OWN.values()),dtype=int)
assert len(TRI)==84 and len(ED)==126 and all(len(a)==2 for a in OWN.values())

def vertices(x):
    x=np.asarray(x,dtype=float)
    den=1-Q0@x[:3]
    if den.min()<=1e-4 or np.max(abs(x[3:5]))>4:raise ValueError('outside parameter domain')
    d=np.exp([x[3],x[4],-x[3]-x[4]])
    A=np.array([[d[0],0,0],[x[5],d[1],0],[x[6],x[7],d[2]]])
    return (Q0/den[:,None])@A.T

def mesh(V):
    a,b,c=V[TRI[:,0]],V[TRI[:,1]],V[TRI[:,2]]
    det=np.einsum('ij,ij->i',a,np.cross(b,c))
    vol6=det.sum()
    if vol6<=0:raise ValueError('negative volume')
    g=(det[:,None]*(a+b+c)).sum(axis=0)/(4*vol6)
    n=np.cross(b-a,c-a)
    h=np.einsum('ij,ij->i',n,a-g)
    if h.min()<=0:raise ValueError('centroid outside')
    pol=n/h[:,None]
    return vol6/6,g,pol,n,h

def census(V,tol=1e-9):
    vol,g,pol,n,h=mesh(V)
    Y=V-g
    nn=n/np.linalg.norm(n,axis=1)[:,None]
    R=np.linalg.norm(Y,axis=1).max()
    # Signed barycentric coordinates of own-centroid orthogonal facet feet.
    a,b,c=V[TRI[:,0]],V[TRI[:,1]],V[TRI[:,2]]
    u,v=b-a,c-a
    proj=g+(h/np.einsum('ij,ij->i',n,n))[:,None]*n
    w=proj-a
    uu=np.einsum('ij,ij->i',u,u);uv=np.einsum('ij,ij->i',u,v);vv=np.einsum('ij,ij->i',v,v)
    wu=np.einsum('ij,ij->i',w,u);wv=np.einsum('ij,ij->i',w,v);D=uu*vv-uv*uv
    beta=(vv*wu-uv*wv)/D;gam=(uu*wv-uv*wu)/D
    sm=np.min(np.c_[1-beta-gam,beta,gam],axis=1)
    Umax=np.full(len(V),-np.inf)
    d=Y[ED[:,1]]-Y[ED[:,0]];dd=np.einsum('ij,ij->i',d,d)
    for k,(i,j) in enumerate(ED):
        Umax[i]=max(Umax[i],float(Y[i]@d[k])/np.sqrt(float(Y[i]@Y[i])*dd[k]))
        Umax[j]=max(Umax[j],float(-Y[j]@d[k])/np.sqrt(float(Y[j]@Y[j])*dd[k]))
    H=[];wh=[]
    for k,(i,j) in enumerate(ED):
        t=-float(Y[i]@d[k])/dd[k];p=Y[i]+t*d[k]
        ij=DE[k];A=nn[ij].T
        coef=np.linalg.lstsq(A,p,rcond=None)[0]/R
        s=np.r_[t,1-t,coef]
        if np.all(s>tol):H.append([int(i),int(j)])
        elif np.all(s>=-tol):wh.append([int(i),int(j)])
    return {'V':44,'E':126,'F':84,'C':252,'S':np.flatnonzero(sm>tol).tolist(),'U':np.flatnonzero(Umax < -tol).tolist(),'H':H,'weak':[np.flatnonzero((sm>=-tol)&(sm<=tol)).tolist(),np.flatnonzero((Umax>=-tol)&(Umax<=tol)).tolist(),wh], 'volume':float(vol),'centroid':g.tolist(),'P':barcodes(Y,ED),'Q':barcodes(pol,DE)}

def loss(x):
    try:
        V=vertices(x);vol,g,pol,n,h=mesh(V)
        pb=barcodes(V-g,ED);qb=barcodes(pol,DE)
        # Sum of relative depths, with no intentional tiny-bar suppression beyond 1e-13.
        return sum(b['depth'] for b in pb+qb)
    except (ValueError,np.linalg.LinAlgError,FloatingPointError):return 100.+float(np.linalg.norm(x))

def baseline():
    out={'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__}}
    for name,z in [('origin',np.zeros(3)),('primal_centroid',centroid)]:
        x=np.r_[z,np.zeros(5)];r=census(vertices(x));out[name]={'x':x.tolist(),'audit':r}
    def vf(z):
        den=1-Q0@z
        if den.min()<=1e-5:return 1e10+float(np.sum(np.maximum(1e-5-den,0)))*1e10
        return np.log(mesh(Q0/den[:,None])[0])
    def vg(z):
        q=Q0/(1-Q0@z)[:,None];return 4*mesh(q)[1]
    res=minimize(vf,np.zeros(3),jac=vg,method='SLSQP',constraints=[{'type':'ineq','fun':lambda z:1-Q0@z-1e-4,'jac':lambda z:-Q0}],options={'ftol':1e-13,'maxiter':500})
    x=np.r_[res.x,np.zeros(5)]
    out['santalo_numerical']={'success':bool(res.success),'message':str(res.message),'x':x.tolist(),'gradient_norm':float(np.linalg.norm(vg(res.x))),'audit':census(vertices(x))}
    print(json.dumps(out,indent=2,sort_keys=True))
    return out

def search(outpath,steps,random_seed):
    rng=np.random.default_rng(random_seed)
    ledger=[];best=None;start=time.time()
    cons=[{'type':'ineq','fun':lambda x:1-Q0@x[:3]-1e-3}]
    bounds=[(-2,2)]*3+[(-1.5,1.5)]*2+[(-2,2)]*3
    for i in range(steps):
        if i==0:x=np.zeros(8)
        elif i==1:x=np.r_[centroid,np.zeros(5)]
        elif best is not None and i%3:x=best['x']+rng.normal(0,.12 if i%2 else .4,8)
        else:x=rng.normal(0,.4,8)
        # Put projective pole strictly inside K along its radial ray.
        mx=float(np.max(Q0@x[:3]));x[:3]/=max(1,mx/.75)
        res=minimize(loss,x,method='SLSQP',constraints=cons,bounds=bounds,options={'ftol':1e-10,'maxiter':200,'eps':1e-6})
        r=census(vertices(res.x))
        z={'index':i,'x':res.x.tolist(),'loss':float(res.fun),'success':bool(res.success),'nit':int(res.nit),'counts':[len(r['S']),len(r['U']),len(r['H'])],'P':len(r['P']),'Q':len(r['Q'])}
        ledger.append(z)
        if best is None or res.fun<best['loss']:
            best={'x':res.x.copy(),'loss':float(res.fun),'audit':r};print('POLAR_ORBIT_BEST',i,res.fun,z['counts'],flush=True)
        payload={'status':'numerical_not_exact','random_seed':random_seed,'steps_requested':steps,'ledger':ledger,'best':{'x':best['x'].tolist(),'loss':best['loss'],'audit':best['audit']},'elapsed_seconds':time.time()-start}
        Path(outpath).write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
        if z['counts']==[1,1,0] and not any(r['weak']):print('NUMERICAL_OWN110_CANDIDATE_NOT_CERTIFIED',flush=True);break
    return payload

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--baseline',action='store_true');p.add_argument('--search',action='store_true');p.add_argument('--out',default='H44_polar_search.json');p.add_argument('--steps',type=int,default=8);p.add_argument('--seed',type=int,default=20260924);a=p.parse_args()
    if a.search:search(a.out,a.steps,a.seed)
    else:
        r=baseline();Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
