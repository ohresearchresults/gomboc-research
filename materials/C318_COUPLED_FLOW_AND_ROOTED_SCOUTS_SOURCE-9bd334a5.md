# material-9bd334a526e9

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Complete physical coupled-coordinate scout and two exact source variants

Status: reusable numerical METHOD plus honest negative results, not exact own110 evidence. Final exact C306_G4_OWN121 literal body/census are independently durable in [internal-source-reference]. Exact original input.json, including all 55 P1000 rows and106 triangles, is the file block in self-contained material [internal-source-reference], input SHA256 5cd9cf50c8574da530c02d1b13d24840c0a9d15562fc8c3fe92e32b2eaebf90b,1958 bytes. This material explicitly depends on that exact input unit; attach BOTH materials for workers. No sandbox, unnamed checkpoint, hidden seed, or archived worker result is required. The two complete Python source units below plus that immutable exact input reproduce all searches. Do not substitute the unrelated C318_PROTECTED15 geometry.

Environment used: Python3.11.8, numpy2.3.5, scipy1.17.0, torch2.10.0+cpu; one torch thread and OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1. Default seed190926, trust0.02. scipy Qhull proposes the hull; each finite trial recomputes filled centroid and centered polar points from the complete current boundary. Autodiff includes actual mass motion. The LP moves all coordinates or a12-vertex patch, fixes infinitesimal translation/scale gauges, and proposes improvement of deficient escape arrows while protecting current positive ones. Accepted steps recenter and preserve filled volume. The reported E=3F/2 is only a floating simplicial proposal, not a true-complex certificate. No negative numerical checkpoint here is an exact equilibrium certificate.

The local-arrow heuristic has an important FAILURE: even cosine-normalized escape tends to zero when two vertices nearly coincide, although the closed unwanted basin survives. Choosing the root by the most-negative local angular escape was additionally a bad continuation heuristic; the corrected version chooses the farthest physical (and polar) vertex. That root correction alone does not fix coalescence. The rooted variant selects max-min directed paths to the global root via a settled-parent algorithm, removes nonexposed input points at each iteration, and therefore exposes a much larger basin barrier rather than declaring the nearly coincident pair solved. It also failed in the runs below, generating many additional S/U.

Reconstruction: recover input.json from [internal-source-reference]; write both Python blocks below with one final newline. Run `python replay_variants.py`; expected `COUPLED_VARIANTS_SOURCE_HASH_PASS`. Run in a NEW empty output location, since each output directory must not already exist:
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python coupled_flow_v1.py input.json whole --steps 150
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python coupled_flow.py input.json farthest --steps 180
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python coupled_flow.py input.json patch --steps 180 --mode patch
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python coupled_rooted.py input.json rooted0 --steps 160
python - <<'PY'
import json,numpy as np,pathlib
z=json.loads(pathlib.Path('farthest/best.json').read_text())
P=np.delete(np.array(z['points']),[17,21],axis=0)
pathlib.Path('farthest_merged_input.json').write_text(json.dumps(dict(points=P.tolist(),grid=1)))
PY
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python coupled_rooted.py farthest_merged_input.json rooted_merge --steps 160
```

Source manifests: coupled_flow.py6241 bytes/SHA256426c569d4b87d2e1ad9c4a21a6b1b9c440fbaa95ae5f8887d9b6e5134804c7cf; replay_variants.py1850 bytes/SHA25694eace6ac1650461d5606615b80b6aab8eefa214f0902209ce8a63d1353cbddc. Generated coupled_flow_v1.py6203 bytes/SHA2563950447ddc537c38c030131f4a5c5b2e0a111d0ec5e9f5201f083e17b99ca2e7; coupled_rooted.py6859 bytes/SHA256e69289842b226178a7c5067382d516f70d821fb880792a58c633d0322765bf09.

Observed output checkpoints, no exact claim:
* whole/best.json3708 bytes/SHA25650667520bd0f926ff4f49dee7797b1ea8df670ae56bb0ce36fb49c825d873cf5. V1's falsely selected root17 gives local residual3.934375396004099e-9 but distance(0,1)=5.55620556244302e-9. With correct farthest root0, actual unwanted17 escape is -0.30481933917016685, not nearly solved. Global radii0/1=1.6802375564 versus17=1.2403443509; S1,U2. This is a coalescence artifact.
* farthest/best.json3660 bytes/SHA2567f85f33113df5d6549d7fa27c75258b4fb06d892197d6d944745326874b878a3. Last iteration59, root0, S1,U2, local residual6.488153236443572e-9, distance(14,17)=2.0970087031132617e-9, input21 nonexposed; LP then infeasible. After actual finite deletion of17 and21, the unwanted basin has local escape about-0.3925, not zero. Rounded literal C306_G4 in the companion material is its exact useful nonwinner.
* patch/best.json3715 bytes/SHA256b2d6286031bd92c87047d826477343c93c5e3c3d0f159d7d08cbcb215ca92db0. Last iteration34, S1,U2, deficit0.0013230380002334685, distance(14,17)=5.181504563323291e-10; HiGHS numerical failure. Same geometric collapse, not a no-go theorem.
* rooted0/last.json3386 bytes/SHA2560278c3aec859fb356dfefbb3376e54e8a1ec81464024324152f8097de2f09140. Initial root-path barrier-0.6727172361926923 rather than the shallow local maximum. Iteration159 has V50,E144,F96 provisional,S14,U7, primal root-path margin-0.5106939406965719,polar-0.005066700730219174.
* rooted_merge/last.json3245 bytes/SHA25600e1f52e95c2722ca81f510c25cda1e65f5a831c68c7589266dce90e7621ce3d. Initial merged body S1,U2, rooted barrier-0.6412748474942228. Iteration159 V48,E138,F92 provisional,S23,U6, root-path margin-0.49707630147371573,polar-0.00023171913564418558.

These are finite unsuccessful experiments, NOT exclusions of coupled coordinate motions, rooted methods, different LP merit choices, or C<622. A continuation must retain full physical census and either impose finite feature-size guards or perform genuine discrete contraction and rebuild, not treat an almost-zero edge as successful basin destruction. Preserve both the full-star exact exclusion and C306 exact nonwinner as distinct results; neither is implied by these scouts alone.

## File coupled_flow.py
```python
"""Finite free-vertex physical flow; floating discovery, not an exact certificate.
Rebuild the convex hull and its filled-volume centroid on every finite trial.
Polar points are built about THAT centroid, so their vertex census is the
physical stable-face census. Numerical all-pair margins are only a search
objective; negative-margin improvements do not certify basin reduction.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,pathlib
import numpy as np
import torch
from scipy.spatial import ConvexHull
from scipy.optimize import linprog

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)

def topology(P):
    h=ConvexHull(P);T=h.simplices.copy()
    nn=np.cross(P[T[:,1]]-P[T[:,0]],P[T[:,2]]-P[T[:,0]])
    neg=np.einsum('ij,ij->i',nn,h.equations[:,:3])<0
    T[neg]=T[neg][:,[0,2,1]]
    return T

def geometry(P,T):
    base=P.mean(0);Y=P-base;tri=Y[T]
    d=torch.sum(tri[:,0]*torch.linalg.cross(tri[:,1],tri[:,2]),dim=1)
    volume=d.sum()/6
    c=base+torch.sum(d[:,None]*tri.sum(1),dim=0)/(4*d.sum())
    X=P-c;tri=X[T]
    n=torch.linalg.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0])
    h=torch.sum(n*tri[:,0],dim=1)
    Q=n/h[:,None]
    return X,Q,c,volume

def score(X):
    D=X[None,:,:]-X[:,None,:]
    e=torch.sum(X[:,None,:]*D,dim=2)/(torch.linalg.vector_norm(X,dim=1)[:,None]*torch.linalg.vector_norm(D,dim=2).clamp_min(1e-14))
    return e-torch.eye(len(X),dtype=X.dtype)*1e6

def report(P):
    T=topology(P)
    with torch.no_grad():
        X,Q,c,V=geometry(torch.tensor(P),torch.tensor(T));U=score(X).max(1).values.numpy();S=score(Q).max(1).values.numpy()
    eu=int(torch.sum(X*X,dim=1).argmax());es=int(torch.sum(Q*Q,dim=1).argmax())
    u=np.delete(U,eu);s=np.delete(S,es)
    energy=float(np.maximum(0,-u).sum()+np.maximum(0,-s).sum())
    return dict(V=len(np.unique(T)),E=len(T)*3//2,F=len(T),S=int((S<-1e-10).sum()),U=int((U<-1e-10).sum()),S_near=int((np.abs(S)<=1e-10).sum()),U_near=int((np.abs(U)<=1e-10).sum()),u_root=eu,s_root=es,u_min=float(u.min()),s_min=float(s.min()),energy=energy,volume=float(V),centroid=c.tolist()),T

def run(inp,out,steps,trust,seed,mode):
    z=json.loads(pathlib.Path(inp).read_text());P=np.array(z.get('points',z.get('P1000')),float)/z.get('grid',1000 if 'P1000' in z else 1)
    dst=pathlib.Path(out);dst.mkdir(exist_ok=False);rng=np.random.default_rng(seed)
    history=[];best=None
    for it in range(steps):
        rec,T=report(P);rec['iteration']=it;history.append(rec)
        print(json.dumps(rec),flush=True)
        key=(rec['S']+rec['U'],rec['energy'])
        if best is None or key<best:
            best=key;(dst/'best.json').write_text(json.dumps(dict(points=P.tolist(),grid=1,report=rec),sort_keys=True,separators=(',',':')))
        (dst/'last.json').write_text(json.dumps(dict(points=P.tolist(),grid=1,report=rec),sort_keys=True,separators=(',',':')))
        if rec['S']==rec['U']==1 and rec['s_min']>1e-8 and rec['u_min']>1e-8:break
        pt=torch.tensor(P);tt=torch.tensor(T)
        X,Q,_,_=geometry(pt,tt);Em=score(X);Fm=score(Q)
        wi=Em.argmax(1).numpy();wj=Fm.argmax(1).numpy()
        ri=np.array([i for i in range(len(P)) if i!=rec['u_root']]);rj=np.array([i for i in range(len(T)) if i!=rec['s_root']])
        def selected(flat):
            x,q,c,v=geometry(flat.reshape(-1,3),tt)
            def arrow(Z,i,j):
                D=Z[j]-Z[i]
                return (Z[i]*D).sum(1)/(torch.linalg.vector_norm(Z[i],dim=1)*torch.linalg.vector_norm(D,dim=1).clamp_min(1e-14))
            return torch.cat([arrow(x,ri,wi[ri]),arrow(q,rj,wj[rj])])
        flat=pt.ravel().requires_grad_(True)
        f=selected(flat).detach().numpy()
        J=torch.autograd.functional.jacobian(selected,flat,vectorize=True).detach().numpy()
        bad=f<1e-6
        A=np.column_stack([-J,bad.astype(float)])
        b=f-np.where(bad,f,1e-6)
        # Positive rows keep a fixed absolute cosine floor. Initially tiny
        # positive rows are permitted their current positive value, not a
        # fictitious already-achieved floor.
        b[~bad]=f[~bad]-1e-6
        c=np.r_[np.zeros(P.size),-1.]
        gauge=np.zeros((4,P.size+1))
        for k in range(3):gauge[k,k:P.size:3]=1
        gauge[3,:-1]=(P-P.mean(0)).ravel()
        bounds=[(-trust,trust)]*P.size+[(0,1)]
        if mode=='patch':
            moving=set([0,4,5,7,9,10,11,14,17,20,25,32])
            bounds=[(-trust,trust) if i//3 in moving else (0,0) for i in range(P.size)]+[(0,1)]
        # Common progress on every currently deficient arrow. A tiny secondary
        # random linear term diversifies otherwise degenerate free-coordinate LPs.
        c[:-1]=rng.normal(size=P.size)*1e-8
        opt=linprog(c,A_ub=A,b_ub=b,A_eq=gauge,b_eq=np.zeros(4),bounds=bounds,method='highs')
        if not opt.success or opt.x[-1]<1e-13:
            print('LP_STOP',opt.message,flush=True);break
        d=opt.x[:-1].reshape(-1,3);accepted=False
        old=max(0,-rec['u_min'])+max(0,-rec['s_min'])
        for h in [1,0.5,0.25,0.125,0.0625,0.03125,0.015625,0.0078125,0.00390625,0.001953125,0.0009765625]:
            Pn=P+h*d
            try:new,_=report(Pn)
            except Exception:continue
            merit=max(0,-new['u_min'])+max(0,-new['s_min'])
            if merit<old-1e-5*h*opt.x[-1] and new['energy']<=rec['energy']+max(1e-8,old*0.02):
                # Fixed physical volume removes uniform-shrinking ambiguity.
                P=(Pn-np.array(new['centroid']))*(rec['volume']/new['volume'])**(1/3)
                accepted=True;break
        if not accepted:
            trust*=.5
            if trust<1e-8:print('FINITE_TRUST_STOP',flush=True);break
        else:trust=min(.03,trust*1.1)
    (dst/'history.json').write_text(json.dumps(history,sort_keys=True,separators=(',',':')))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');ap.add_argument('--steps',type=int,default=100);ap.add_argument('--trust',type=float,default=.02);ap.add_argument('--seed',type=int,default=190926);ap.add_argument('--mode',choices=['whole','patch'],default='whole');a=ap.parse_args()
    run(a.input,a.output,a.steps,a.trust,a.seed,a.mode)
```

## File replay_variants.py
```python
"""Generate exactly the two scout variants from the complete coupled_flow.py."""
from pathlib import Path
import hashlib
s=Path('coupled_flow.py').read_text()
old="eu=int(torch.sum(X*X,dim=1).argmax());es=int(torch.sum(Q*Q,dim=1).argmax())"
assert s.count(old)==1
v1=s.replace(old,"eu=int(U.argmin());es=int(S.argmin())")
Path('coupled_flow_v1.py').write_text(v1)
r=s.replace('def report(P):','''def rooted(E,root):
    """Max-min directed paths to root; every parent was already settled."""
    n=len(E);level=np.full(n,-np.inf);level[root]=np.inf
    parent=np.full(n,-1,dtype=int);done=np.zeros(n,dtype=bool)
    for _ in range(n):
        j=int(np.argmax(np.where(done,-np.inf,level)));done[j]=True
        trial=np.minimum(E[:,j],level[j]);take=(~done)&(trial>level)
        level[take]=trial[take];parent[take]=j
    return parent,level

def report(P):''')
r=r.replace("u=np.delete(U,eu);s=np.delete(S,es)","wi,ul=rooted(score(X).numpy(),eu);wj,sl=rooted(score(Q).numpy(),es)\n    u=np.delete(ul,eu);s=np.delete(sl,es)")
r=r.replace("wi=Em.argmax(1).numpy();wj=Fm.argmax(1).numpy()","wi,_=rooted(Em.numpy(),rec['u_root']);wj,_=rooted(Fm.numpy(),rec['s_root'])")
r=r.replace("best=None","best=None\n    P=P[np.unique(topology(P))]")
r=r.replace("rec,T=report(P);rec['iteration']=it;history.append(rec)","P=P[np.unique(topology(P))]\n        rec,T=report(P);rec['iteration']=it;history.append(rec)")
Path('coupled_rooted.py').write_text(r)
expected={'coupled_flow.py':'426c569d4b87d2e1ad9c4a21a6b1b9c440fbaa95ae5f8887d9b6e5134804c7cf','coupled_flow_v1.py':'3950447ddc537c38c030131f4a5c5b2e0a111d0ec5e9f5201f083e17b99ca2e7','coupled_rooted.py':'e69289842b226178a7c5067382d516f70d821fb880792a58c633d0322765bf09'}
for fn,h in expected.items():assert hashlib.sha256(Path(fn).read_bytes()).hexdigest()==h,fn
print('COUPLED_VARIANTS_SOURCE_HASH_PASS')
```
