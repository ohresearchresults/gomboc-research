# material-147c6926ff6f

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J92 complete numerical producers: actual mass, direct/detour bridges and one-cap centring

All outputs here are numerical nominations, NOT exact claims or global exclusions. The authoritative exact negative controls are J92_EXACT_RECOVERY.md, [internal-source-reference]. The complete exact C390 input is in [internal-source-reference]; extract its complete unencoded nine-unit core as in REPLAY92.py. No previous sandbox is required.

Observed environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu (Torch is used by the separately preserved optimization producers), OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1. No random seed is used by these deterministic nomination families. Qhull is SciPy's default at the stated version; no jitter option. The numerical vertex deduplication at11 decimals below is NOT an exact geometry conclusion; the exact H-triple auditor reconstructed all selected controls independently from their literal rational inputs.

Save each complete source below by its heading. Commands, in order:
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python nominate92.py`
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python detour92.py`
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python capcentre92.py`
`python freeze92.py`
The first creates direct great-circle checkpoints BRIDGE_N9..N16.npz and BRIDGE_SCREEN.json; the second creates strict positive-chain detours and DETOUR_SCREEN.json; the third creates five centroid-fitted cap checkpoints and CAPCENTRE_SCREEN.json. Freeze writes the three exact integer H inputs plus LOW. Deterministic exact endpoint data, hashes and verification commands are separately literal in J92_EXACT_RECOVERY.md; they do not depend on repeating floating optimization bit-for-bit.

## Scientific outcomes and limitations
Direct positive chain first appears at9 links. It cuts away the physical U and loses17.376% volume. A10-link latitude detour keeps the old U but creates another at supports13/22/78, losing13.580% volume. Both are reference121, NOT reference110. Wider detours and the two subsequent optimization producers are in J92_NUMERICAL_METHODS_OPT.md. The single-cap objective F(lambda)=integral_K max(0,1+lambda.(x-gref)) dx has gradient equal to the first moment of the retained cap relative to gref. The implemented H intersection therefore fits a true uniform-mass cap, not a density or reference-point adjustment. For the .03-bump detour the fitted centre is close to gref but the new facet79 is stable, giving own255; exact rounding confirms this. Solver success/precision-loss messages are retained in each output and are not exact proofs.

## geom92.py
```python
"""Numerical nominations ONLY; exact90.cpp supplies terminal exact claims.
H rows satisfy Y.x<=1. Rebuild the actual convex body and integrate uniform mass.
No equilibrium count tolerance is silently interpreted as an exact conclusion.
"""
import numpy as np
from scipy.spatial import ConvexHull

def vm(P):
    h=ConvexHull(P)
    t=h.simplices.copy()
    a,b,c=P[t[:,0]],P[t[:,1]],P[t[:,2]]
    s=np.einsum('ij,ij->i',np.cross(b-a,c-a),h.equations[:,:3])
    ii=s<0;t[ii,1],t[ii,2]=t[ii,2].copy(),t[ii,1].copy()
    a,b,c=P[t[:,0]],P[t[:,1]],P[t[:,2]]
    # origin is interior in all nominations here
    w=np.einsum('ij,ij->i',a,np.cross(b,c))/6
    V=w.sum();g=(w[:,None]*(a+b+c)/4).sum(0)/V
    return V,g,h,t

def hbody(Y):
    Y=np.asarray(Y,dtype=float)
    qh=ConvexHull(Y)
    if np.any(qh.equations[:,3]>=-1e-10):raise ValueError('H intersection not certified numerically bounded/interior')
    t=qh.simplices
    X=np.linalg.solve(Y[t],np.ones((len(t),3,1)))[:,:,0]
    # Remove duplicate triangulations of a nonsimplicial dual facet only numerically.
    _,ids=np.unique(np.round(X,11),axis=0,return_index=True)
    X=X[np.sort(ids)]
    V,g,ph,pt=vm(X)
    act=qh.vertices
    return X,Y[act],g,V,act,ph,pt

def roots(P,tol=0.):
    R=P@P.T-(P*P).sum(1)[:,None]
    np.fill_diagonal(R,-np.inf)
    vals=R.max(1)
    return np.where(vals<=tol)[0],vals

def report(Y,gref=None):
    X,Z,g,V,act,h,t=hbody(Y)
    C=X-g;Q=Z/(1-Z@g)[:,None]
    u,uv=roots(C);s,sv=roots(Q)
    out=dict(V=len(X),F=len(Z),E=len(X)+len(Z)-2,volume=float(V),centroid=g.tolist(),S=act[s].tolist(),U=u.tolist(),strict_float=[len(s),len(u)],min_nonroot_primal=float(np.min(uv[uv>0])) if np.any(uv>0) else None,min_nonroot_polar=float(np.min(sv[sv>0])) if np.any(sv>0) else None)
    if gref is not None:
      ur,uvr=roots(X-gref);sr,svr=roots(Z/(1-Z@gref)[:,None]);out['reference_float']=[len(sr),len(ur)];out['reference_S']=act[sr].tolist();out['reference_U']=ur.tolist();out['drift']=(g-gref).tolist()
    return out

def slerp(a,b,t):
    x=a/np.linalg.norm(a);y=b/np.linalg.norm(b);angle=np.arccos(np.clip(x@y,-1,1))
    return (np.sin((1-t)*angle)*x+np.sin(t*angle)*y)/np.sin(angle)

def chain(a,b,n):
    # n links; n-1 intermediate support points, endpoints unchanged
    t=np.arange(1,n)/n
    R0=np.linalg.norm(a);R1=np.linalg.norm(b)
    return np.array([slerp(a,b,float(s))*np.exp((1-s)*np.log(R0)+s*np.log(R1)) for s in t])
```

## nominate92.py
```python
import numpy as np,json
from pathlib import Path
from fractions import Fraction
from geom92 import *
D=Path(__file__).parent
Y=np.loadtxt(D/'J90_DETACHED_C390_G8.txt',skiprows=1)/1e8
Y=np.vstack([Y,np.array([[-36360454,-31213549,42273558],[-42575066,-16376129,44614942],[-34061100,-28210691,45960444]])/1e8])
X,Z,g,V,act,h,t=hbody(Y)
print('LOW',report(Y),flush=True)
Q=Y/(1-Y@g)[:,None]
rr,_=roots(Q);print('S',rr,'r2',(Q[rr]**2).sum(1),'angle',np.arccos(Q[rr[0]]@Q[rr[1]]/np.linalg.norm(Q[rr[0]])/np.linalg.norm(Q[rr[1]])),flush=True)
rr=sorted(rr,key=lambda i:np.linalg.norm(Q[i]));a,b=Q[rr]
rows=[]
for n in range(2,17):
    C=chain(a,b,n);qn=np.vstack([a,C,b]);guards=np.einsum('ij,ij->i',qn[:-1],np.diff(qn,axis=0))
    YY=np.vstack([Y,C/(1+C@g)[:,None]])
    d=report(YY,g);d.update(n=n,chain_margin=float(min(guards)),actual_added=len(C));rows.append(d)
    print('N',n,d,flush=True)
    if min(guards)>0:
      np.savez(D/f'BRIDGE_N{n}.npz',Y=YY,Ybase=Y,gref=g,polarchain=qn)
Path(D/'BRIDGE_SCREEN.json').write_text(json.dumps(rows,indent=2)+'\n')
```

## detour92.py
```python
"""Finite axis-detour polar chains, numerical nominations only.
Save all actual H inputs/checkpoints; exact90 is required before an exact claim.
"""
import json
from pathlib import Path
import numpy as np
from geom92 import *
D=Path(__file__).parent
base=np.load(D/'BRIDGE_N9.npz');Y=base['Ybase'];g0=base['gref']
X,Z,g,V,act,h,t=hbody(Y);u=X[roots(X-g0)[0][0]]-g0;axis=u/np.linalg.norm(u)
Q=Y/(1-Y@g0)[:,None];a,b=Q[65],Q[15];r0,r1=np.linalg.norm(a),np.linalg.norm(b)
th0,th1=np.arccos([a@axis/r0,b@axis/r1]);e1=a/r0-axis*(a@axis/r0);e1/=np.linalg.norm(e1)
p=b/r1-axis*(b@axis/r1);p/=np.linalg.norm(p);az=np.arccos(np.clip(p@e1,-1,1));e2=p-e1*(p@e1);e2/=np.linalg.norm(e2)
rows=[]
for n in range(9,19):
 for bump in [0.,.015,.03,.06,-.015]:
  tt=np.arange(1,n)/n;theta=(1-tt)*th0+tt*th1+bump*np.sin(np.pi*tt)
  r=np.exp((1-tt)*np.log(r0)+tt*np.log(r1))
  dirs=np.cos(theta)[:,None]*axis+np.sin(theta)[:,None]*(np.cos(az*tt)[:,None]*e1+np.sin(az*tt)[:,None]*e2)
  C=r[:,None]*dirs;full=np.vstack([a,C,b]);guard=np.einsum('ij,ij->i',full[:-1],np.diff(full,axis=0))
  if min(guard)<=0 or max(C@u)>=1:continue
  YY=np.vstack([Y,C/(1+C@g0)[:,None]]);out=report(YY,g0)
  name='DETOUR_N%d_B%s'%(n,str(bump).replace('-','m').replace('.','p'))
  out.update(name=name,n=n,bump=bump,margin=float(min(guard)),u_gap=float(1-max(C@u)))
  rows.append(out);np.savez(D/(name+'.npz'),Y=YY,Ybase=Y,gref=g0,polarchain=full)
  print(name,'VEF',out['V'],out['E'],out['F'],'ref',out['reference_float'],'own',out['strict_float'],'dV',1-out['volume']/V,'g',out['centroid'],'margin',out['margin'],'ugap',out['u_gap'],flush=True)
(D/'DETOUR_SCREEN.json').write_text(json.dumps(rows,indent=2)+'\n')
```

## capcentre92.py
```python
"""Convex maximum-volume one-cap centroid fitting on a changed physical H body.
All centres/censuses here are floating nominations, never exact acceptance.
The kept cap is 1+lambda.(x-gref)>=0; in reference coordinates add polar row -lambda.
"""
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from geom92 import hbody,report,roots
D=Path(__file__).parent

def fit(Y,gref):
 Q=Y/(1-Y@gref)[:,None]
 def fg(lam):
  X,Z,g,V,act,h,t=hbody(np.vstack([Q,-lam]))
  return V*(1+lam@g),V*g
 res=minimize(fg,np.zeros(3),jac=True,method='BFGS',options={'gtol':2e-12,'maxiter':300})
 C=np.vstack([Q,-res.x]); YY=C/(1+C@gref)[:,None]
 d=report(YY,gref);d.update(lam=res.x.tolist(),solver_success=bool(res.success),solver_message=str(res.message),gradient=res.jac.tolist(),iterations=int(res.nit))
 return YY,d

if __name__=='__main__':
 names=sys.argv[1:] or ['BRIDGE_N9','DETOUR_N10_B0p0','DETOUR_N10_B0p03','DETOUR_N10_B0p06','DETOUR_N12_B0p03']
 out=[]
 for name in names:
  d=np.load(D/(name+'.npz'));YY,r=fit(d['Y'],d['gref']);r['name']=name+'_CAP'
  out.append(r);np.savez(D/(name+'_CAP.npz'),Y=YY,gref=d['gref'])
  print(json.dumps(r),flush=True)
 (D/'CAPCENTRE_SCREEN.json').write_text(json.dumps(out,indent=2)+'\n')
```

## freeze92.py
```python
"""Freeze selected J92 controls on the 10^12 integer normal grid.
First 70 rows are exactly the C390 10^8 input plus the three KF27C_LOW_G8 rows.
Only newly generated rows are rounded, using Python exact binary64 ratio and
nearest ties-to-even Fraction rounding. These objects are NOT own110 claims.
"""
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
D=Path(__file__).parent;scale=10**12
base=[[int(v) for v in line.split()] for line in (D/'J90_DETACHED_C390_G8.txt').read_text().splitlines()[1:]]
base += [[-36360454,-31213549,42273558],[-42575066,-16376129,44614942],[-34061100,-28210691,45960444]]
low='70 100000000\n'+'\n'.join(' '.join(map(str,p)) for p in base)+'\n'
(D/'J92_LOW_G8.txt').write_text(low)
names={'J92_DIRECT9_G12':'BRIDGE_N9','J92_DETOUR10_G12':'DETOUR_N10_B0p0','J92_DETOUR_CAP_G12':'DETOUR_N10_B0p03_CAP'}
for label,name in names.items():
 Y=np.load(D/(name+'.npz'))['Y'];rows=[[v*10**4 for v in p] for p in base]
 rows += [[round(F(float(v))*scale) for v in p] for p in Y[70:]]
 data=f'{len(rows)} {scale}\n'+'\n'.join(' '.join(map(str,p)) for p in rows)+'\n';(D/(label+'.txt')).write_text(data)
 print(label,len(data.encode()),hashlib.sha256(data.encode()).hexdigest())
```
