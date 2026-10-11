# material-e5b2094d17df

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C114_FINITE_ADDITIONS — Recovery capsule part 1/3

Object identities: COORD_C120_ADDED_G4/G5/G6 (own233) and COORD_C120_CENTERED_G6 (own222), all nonwinners, derived from the literal physical VL12_DUAL_CANCEL21_G4 in immutable figure-0438, SHA16684588638a09e8929f3ce23437b244db8ef4f46a3cfe29b4deea8a906b0547, read completely before use. These are NOT own110, not an incumbent replacement, and not excluded continuous families.
All three ordered parts are required for the complete campaign/recovery closure. Part1: complete numerical producing sources. Part2: complete exact mechanical and whole-elder checkers. Part3: literal inputs, exact binary64 checkpoints, full nondefault settings and campaign totals, replay source, source/output manifests and extraction command. Byte-counted @@FILE units include their final newline when present; the separator newline before @@END is not part of the source. No original sandbox or external helper is required after all three parts are extracted.

Numerical environment actually used: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1. Commands: `python cap_search.py --out results --random-count 2400 --generations 80` and `python centered_caps.py`. Exact replay needs only Python standard library. Optimizer trajectories can vary across environments; literal checkpoints define the frozen exact bodies. The original large chronological reports are supplementary, not needed to reconstruct the endpoints or rerun complete producing units.

@@FILE cap_search.py 7453 9aca9b719fed5537438430f00cf62ff7cc800eb845177350219e5deb1caa48ac
"""Finite physical point-addition scout on literal VL12_DUAL_CANCEL21_G4.
Numerical ONLY. No exact H/weak certification; no optimizer failure is an exclusion.
Run: OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python cap_search.py --out results
"""
import argparse, hashlib, itertools, json, os, platform
from pathlib import Path
import numpy as np
import scipy
from scipy.spatial import ConvexHull, QhullError
from scipy.optimize import differential_evolution

DATA={"grid":10000,"points":[[-13513,10001,-9032],[7585,971,-5336],[9215,2535,-2766],[9859,3065,-261],[10414,1455,1511],[10533,-561,2627],[10245,-2747,3309],[9489,-4870,3884],[8292,-6612,4622],[6777,-7643,5870],[4984,-8225,7187],[2841,-8790,8032],[556,-8903,8725],[-1868,-8784,9006],[-4342,-8346,8933],[-6808,-7570,8472],[-9197,-6461,7561],[-11427,-4979,6139],[-13362,-2964,4209],[-14798,-281,1613],[-15515,3415,-2186]]}
P=np.array(DATA['points'],dtype=float)/DATA['grid']

def root_scores(X):
    diff=X[None,:,:]-X[:,None,:]
    lengths=np.linalg.norm(diff,axis=2)
    radii=np.linalg.norm(X,axis=1)
    scores=np.einsum('ij,ikj->ik',X,diff)/(radii[:,None]*np.where(lengths>0,lengths,1))
    np.fill_diagonal(scores,-np.inf)
    return np.max(scores,axis=1)

def bars(X,edges):
    r2=np.einsum('ij,ij->i',X,X)
    pa=list(range(len(X)))
    def find(a):
        while pa[a]!=a:
            pa[a]=pa[pa[a]];a=pa[a]
        return a
    events=[]
    for i,j in edges:
        d=X[j]-X[i]; dd=d@d
        if dd<=1e-28: raise ValueError('zero edge')
        t=np.clip(-X[i]@d/dd,0.,1.)
        z=X[i]+t*d;events.append((float(z@z),int(i),int(j)))
    out=[]
    for death,i,j in sorted(events,reverse=True):
        a,b=find(i),find(j)
        if a==b:continue
        if (r2[a],-a)<(r2[b],-b):a,b=b,a
        delta=float(r2[b]-death)
        if delta>1e-11*max(r2):out.append(dict(peak=b,elder=a,edge=[i,j],birth=float(r2[b]),death=death,depth=delta))
        pa[b]=a
    return out

def geometry(Y,with_bars=False):
    H=ConvexHull(Y)
    T=H.simplices.copy(); a,b,c=Y[T[:,0]],Y[T[:,1]],Y[T[:,2]]
    signs=np.einsum('ij,ij->i',np.cross(b-a,c-a),H.equations[:,:3])
    T[signs<0]=T[signs<0][:,[0,2,1]]
    # Interior-anchor positive tetrahedra, independent of location of old origin.
    anchor=Y[H.vertices].mean(axis=0)
    a,b,c=Y[T[:,0]],Y[T[:,1]],Y[T[:,2]]
    vol=np.einsum('ij,ij->i',a-anchor,np.cross(b-anchor,c-anchor))/6
    V=float(vol.sum()); g=(vol[:,None]*(a+b+c+anchor)).sum(axis=0)/(4*V)
    X=Y[H.vertices]-g
    Q=H.equations[:,:3]/(-H.equations[:,3]-H.equations[:,:3]@g)[:,None]
    # Reject nomination degeneracy rather than call duplicate dual points extra roots.
    dQ=Q[:,None,:]-Q[None,:,:];d2=np.einsum('ijk,ijk->ij',dQ,dQ);np.fill_diagonal(d2,np.inf)
    if d2.min()<1e-18:raise ValueError('numerically coplanar triangulation')
    vi={int(i):k for k,i in enumerate(H.vertices)}
    owners={}
    for f,tri in enumerate(T):
        for i,j in itertools.combinations(tri,2):owners.setdefault(tuple(sorted((int(i),int(j)))),[]).append(f)
    if any(len(o)!=2 for o in owners.values()):raise ValueError('not a paired triangular hull')
    edges=np.array([[vi[i],vi[j]] for i,j in owners]);qedges=np.array(list(owners.values()))
    ps,qs=root_scores(X),root_scores(Q)
    pr=int(np.argmax(np.einsum('ij,ij->i',X,X)));qr=int(np.argmax(np.einsum('ij,ij->i',Q,Q)))
    pnon=np.delete(ps,pr);qnon=np.delete(qs,qr)
    loss=float(np.minimum(pnon,0)@np.minimum(pnon,0)+np.minimum(qnon,0)@np.minimum(qnon,0))
    result=dict(V=len(X),E=len(edges),F=len(Q),volume=V,centroid=g.tolist(),S=int((qs < -1e-10).sum()),U=int((ps < -1e-10).sum()),loss=loss,
      min_edge_relative=float(np.min(np.linalg.norm(X[edges[:,1]]-X[edges[:,0]],axis=1))/np.linalg.norm(X,axis=1).max()),
      physical_nonroot_min=float(pnon.min()),polar_nonroot_min=float(qnon.min()),active_inputs=H.vertices.tolist(),
      stable_triangles=T[qs < -1e-10].tolist(),unstable_inputs=H.vertices[ps < -1e-10].tolist())
    if with_bars:
        pb,qb=bars(X,edges),bars(Q,qedges)
        result.update(Pbars=pb,Qbars=qb,TP=sum(z['depth'] for z in pb)/V**(2/3),TQ=sum(z['depth'] for z in qb)*V**(2/3),
        relative_P=sum(z['depth'] for z in pb)/np.max(np.sum(X*X,axis=1)),relative_Q=sum(z['depth'] for z in qb)/np.max(np.sum(Q*Q,axis=1)))
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='results');ap.add_argument('--random-count',type=int,default=6000);ap.add_argument('--generations',type=int,default=160);args=ap.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    raw=json.dumps(DATA,separators=(',',':')).encode();assert len(raw)==415
    assert hashlib.sha256(raw).hexdigest()=='df0a606ee746a5546f046a4800f1eed5c833bf27e0fbe31d28da4984a482a6f2'
    (out/'parent.json').write_bytes(raw)
    base=geometry(P,True);print('BASELINE',json.dumps(base),flush=True)
    rng=np.random.default_rng(2026092014);g=np.array(base['centroid']);R=np.linalg.norm(P-g,axis=1).max()
    counts={};valid=0;fail=0;best=None;top=[];ledger=[]
    # Global candidates, and candidates beyond each of the parent's two stable triangles.
    H=ConvexHull(P);stable=base['stable_triangles'];facets=[]
    for tri in stable:
        a,b,c=P[tri];n=np.cross(b-a,c-a);n/=np.linalg.norm(n)
        if n@(g-a)>0:n=-n
        h=n@(a-g);foot=g+h*n;facets.append((foot,n,h))
    def evaluate(v,tag):
        nonlocal valid,fail,best
        try:r=geometry(np.vstack([P,v]))
        except (QhullError,ValueError,FloatingPointError):fail+=1;return 1e3
        valid+=1;k=f"{r['S']},{r['U']}";counts[k]=counts.get(k,0)+1
        # Search preference is only a heuristic; full root/bar reports decide scientific scope.
        cost=r['loss']+.001*max(0,r['S']-1)+.001*max(0,r['U']-1)
        if r['min_edge_relative']<.02:cost+=10*(.02-r['min_edge_relative'])**2
        if best is None or cost<best['cost']:
            rr=geometry(np.vstack([P,v]),True);best=dict(cost=cost,tag=tag,point=v.tolist(),geometry=rr);ledger.append(best.copy())
            (out/'checkpoint.json').write_text(json.dumps(best,indent=2));print('BEST',valid,k,cost,rr['TP'],rr['TQ'],flush=True)
        return cost
    for i in range(args.random_count):
        d=rng.normal(size=3);d/=np.linalg.norm(d)
        if i%3==0:
            v=g+R*(.25+2*rng.random())*d
        else:
            foot,n,h=facets[(i%3)-1];tangent=d-n*(n@d)
            v=foot+R*(.01+1.5*rng.random())*n+R*(2*rng.random()-1)*tangent
        evaluate(v,'random_'+str(i))
    de=[]
    for seed in (2026092001,2026092002):
        r=differential_evolution(lambda v:evaluate(v,'de_'+str(seed)),[(float(x-2*R),float(x+2*R)) for x in g],seed=seed,maxiter=args.generations,popsize=10,tol=1e-9,atol=1e-12,polish=True,workers=1,updating='immediate')
        de.append(dict(seed=seed,nit=r.nit,nfev=r.nfev,success=bool(r.success),message=str(r.message),x=r.x.tolist(),fun=float(r.fun)))
    report=dict(parent=base,best=best,ledger=ledger,counts=counts,valid=valid,fail=fail,de=de,settings=vars(args),
      versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),evidence='Numerical single-added-point family only; H/weak unverified; no exclusion or own110 claimed.')
    (out/'report.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    print('C114_SINGLE_ADDITION_SCOUT_COMPLETE',valid,fail,json.dumps(counts,sort_keys=True),flush=True)
if __name__=='__main__':main()

@@END

@@FILE centered_caps.py 3842 5e9ba19596f09e0ad0825d721d7aed8c0a56cb0b4fea639ecdff5f21fc3566ce
"""Single physical point addition followed by origin-fixing projective volume-centroid closure.
New uniformly filled solids, not transported nonuniform density. Numerical scout only.
All producing source dependencies: this file and cap_search.py; literal input in cap_search.
"""
import json,platform
from pathlib import Path
import numpy as np
import scipy
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import differential_evolution
from cap_search import P,geometry

base=geometry(P,True);g0=np.array(base['centroid']);X=P-g0
R=np.linalg.norm(X,axis=1).max()

def centered(Z):
    H=ConvexHull(Z);T=H.simplices.copy()
    a,b,c=Z[T[:,0]],Z[T[:,1]],Z[T[:,2]]
    ss=np.einsum('ij,ij->i',np.cross(b-a,c-a),H.equations[:,:3]);T[ss<0]=T[ss<0][:,[0,2,1]]
    bpar=np.zeros(3)
    def stats(bp,second=False):
        den=1+Z@bp
        if min(den)<=0:return None
        Y=Z/den[:,None];a,b,c=Y[T[:,0]],Y[T[:,1]],Y[T[:,2]]
        vol=np.einsum('ij,ij->i',a,np.cross(b,c))/6
        if min(vol)<=0:return None
        V=vol.sum();s=a+b+c;M=(vol[:,None]*s).sum(axis=0)/4
        M2=sum(np.einsum('i,ij,ik->jk',vol,u,u) for u in (s,a,b,c))/20 if second else None
        return V,M,M2,Y
    for it in range(40):
        q=stats(bpar,True)
        if q is None:raise ValueError('chart failed')
        V,M,M2,Y=q
        if np.linalg.norm(M)/V <1e-11*np.max(np.linalg.norm(Y,axis=1)):
            return Y,bpar,it
        step=np.linalg.solve(5*M2,M)
        for k in range(45):
            alpha=2.**(-k);v=stats(bpar+alpha*step)
            if v is not None and v[0]<=V-.4*alpha*(M@step):break
        else:raise ValueError('centering line search')
        bpar+=alpha*step
    raise ValueError('centering residual')

def main():
    out=Path('centered_results');out.mkdir(exist_ok=True);rng=np.random.default_rng(2026092044)
    best=None;valid=0;fail=0;counts={};ledger=[];de=[]
    def evaluate(v,tag):
        nonlocal best,valid,fail
        try:
            Y,b,n=centered(np.vstack([X,v]));r=geometry(Y)
            if np.linalg.norm(r['centroid'])>1e-9*np.linalg.norm(Y,axis=1).max():raise ValueError('own mass cross-check')
        except (ValueError,QhullError,FloatingPointError,np.linalg.LinAlgError):fail+=1;return 1e3
        valid+=1;k=f"{r['S']},{r['U']}";counts[k]=counts.get(k,0)+1
        cost=r['loss']+.001*(max(0,r['S']-1)+max(0,r['U']-1))+10*max(0,.02-r['min_edge_relative'])**2
        if best is None or cost<best['cost']:
            rr=geometry(Y,True);best=dict(cost=cost,point=v.tolist(),projective=b.tolist(),center_iterations=n,physical_points=Y.tolist(),geometry=rr,tag=tag);ledger.append(best.copy())
            (out/'checkpoint.json').write_text(json.dumps(best,indent=2));print('BEST',valid,k,cost,rr['TP'],rr['TQ'],flush=True)
        return cost
    for i in range(800):
        d=rng.normal(size=3);d/=np.linalg.norm(d);evaluate(R*(.4+1.4*rng.random())*d,'random_'+str(i))
    for seed in [2026092041,2026092042]:
        r=differential_evolution(lambda v:evaluate(v,'de_'+str(seed)),[(-2*R,2*R)]*3,seed=seed,maxiter=80,popsize=10,tol=1e-9,atol=1e-12,polish=True,workers=1,updating='immediate')
        de.append(dict(seed=seed,nit=r.nit,nfev=r.nfev,success=bool(r.success),message=str(r.message),x=r.x.tolist(),fun=float(r.fun)))
    report=dict(best=best,ledger=ledger,valid=valid,fail=fail,counts=counts,de=de,base=base,settings=dict(random_seed=2026092044,random_count=800,maxiter=80,popsize=10,newton_iterations=40,centroid_tol=1e-11),versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),evidence='Numerical only, not exact class or exclusion.')
    (out/'report.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    print('C114_CENTERED_ADDITION_SCOUT_COMPLETE',valid,fail,counts,flush=True)
if __name__=='__main__':main()

@@END
