# material-1a2201341036

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J134 Recovery capsule part 3 of 4 — input correction and selected producing closure

## Mandatory correction and dependency boundary

Part1 is [internal-source-reference] (SHA a7f923bbc865cf4c6caa894d3139d461929dd3c7da001e5ce84204e3dc3c000c). Part2 is [internal-source-reference] (SHA edfe772f494c0ed744d62639dbd75ecfbdd37482e99f4e99db7656619a627e43). ONE transcription token in part2's J134_C2_TWIST_G10.input.json was mistyped while storing the otherwise correct local inputs: the mirrored row contains `-3665023311/80000000000`, but the correct exact value is `-3665023311/80000000`. The corresponding positive partner was already correct. All executed computations, local endpoint files and EXPECTED134.json hashes used the CORRECT token. The correction below is mandatory and idempotent. It changes exactly that token and asserts the originally expected full input hash. This supersedes the earlier prose that parts1+2 alone suffice: endpoint recovery now requires parts1+2 and this correction from part3. It is a transport transcription correction, not a changed polyhedron or an alias. Do not claim that the uncorrected part2 recovers all six bodies.

Save the units under their headings. Cold exact reconstruction command: `python correct_part2.py && python replay134.py`. Expected terminal markers: `J134_PART2_TRANSCRIPTION_CORRECTION_PASS`, then `J134_SIX_OWN132_RECOVERY_PASS_NO_110`. All six original exact rational reconstructions were executed; a later cold-copy replay checked five successive bodies against input, point and audit hashes before its wall-time limit, not a completed six-body terminal marker at this material's creation. The command is complete, but this replay is not a second independent engine.

Full selected producing reconstruction: `python input134.py && python produce_selected134.py`. It uses the actual selected binary64 kappa checkpoints and explicit non-default curve parameters, constructs their physical H geometry, rounds only the new polar rows ties-to-even, enforces the first through-apex row/C2 partners exactly, reconstructs the rational H body, and verifies the expected hashes. This extracted selected-producer driver was newly written and had not itself completed a run at storage; its constituent body/freeze computations and checkpoints had already been executed. Expected marker: `J134_SELECTED_PRODUCER_RECOVERY_PASS_NO_110`. The exact endpoint authority is the corrected rational input plus the exact census, not floating-point producer output on an arbitrary platform.

Environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0; OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. Part1 supplies input134.py, geom134.py, freeze134.py and replay134.py; part2 supplies EXPECTED134.json and all endpoint inputs. No old sandbox or omitted helper is needed.

## Scientific mechanism and finite limits

The two-root through-apex head simultaneously gives positive reference arrows from the two old near-apex polar roots in each C2 half. For directions d_i with consecutive cosines positive, radial increments pay -log(d_i.d_{i+1}) plus uniform positive slack. A twisted chain therefore uses its actual spherical turn costs, not an incorrectly reused great-circle bound. The physical H intersection has a new axial cap. The one remaining scalar kappa is numerically adjusted against the ACTUAL filled-volume centroid. Its rational endpoint has gx=gy=0 exactly, but gz is only close to the chosen rational reference c; every reported equilibrium is recomputed at its exact own centroid.

The original700-point single-root polar trial had456 chain-admissible candidates and244 chain failures; none closed its physical mass bracket. A larger-kappa trial subsequently gave opposite signs, so this is NOT a family exclusion. The two-root head closes actual mass and reference S1 but creates a physical U pair: the selected exact endpoints are own132, not110. The coarse56-point twist grid closed only six zero-twist cases. The later100-point grid in fine134.py includes the selected SHORT/WIDE/TWIST cases; small nonzero twist detaches the stable14-gon from ALL U. Larger sampled twists often lose the mass bracket. No finite grid is an impossibility proof. The older hspace134 face-ordering error was corrected by measuring face angles relative to the face-vertex centroid; the invalid early joint-cut pilot was discarded. Floating H intersections may split exact C2/apex coincidences into spurious tiny features. Only the exact reconstructed maximal-facet endpoint audit establishes the six stated classes and counts.

## correct_part2.py — 650 bytes; SHA256 3e7fb9852c5592381e55e77d5badf1560a0f5ae9869b8d34f2a6f7e2c1d1fa47
```python
"""Mandatory correction of one transcription token in material part2.
Only the stored material's mirrored TWIST_G10 row had the extra three zeros;
all actual computations and EXPECTED134 use the correct denominator.
"""
from pathlib import Path
import hashlib
p=Path('J134_C2_TWIST_G10.input.json')
b=p.read_bytes();good='578608de652d707ca6b19ff73f8c903fe0df527203ce69e235ac983a56dde34a'
if hashlib.sha256(b).hexdigest()!=good:
 old=b'"-3665023311/80000000000"';new=b'"-3665023311/80000000"'
 assert b.count(old)==1
 b=b.replace(old,new)
 assert hashlib.sha256(b).hexdigest()==good
 p.write_bytes(b)
print('J134_PART2_TRANSCRIPTION_CORRECTION_PASS')
```

## produce_selected134.py — 1064 bytes; SHA256 86f63c3d74aaf922d5cf94489d37c4fc7de54e4851dec384f0a2c841bcfae694
```python
"""Complete selected numerical producer with literal binary64 checkpoints.
The exact endpoint authority remains the part2 rational inputs plus audit.
Run input134.py first. This reconstructs the selected physical head/curve
nomination and the grid freeze, without re-running every discarded search.
"""
import json
from pathlib import Path
import twist134 as t,freeze134 as f,geom134 as e
CHECKPOINTS=[('SHORT',-.98,12,0.,0.408604706659637),('WIDE',-.95,16,0.,0.4435169638151425),('TWIST',-.98,20,-.05,0.430875906596358)]
expected=json.loads(Path('EXPECTED134.json').read_text())
for tag,c,n,tau,kap in CHECKPOINTS:
 z=t.body(c,kap,n,tau,0,True);r=e.serial(dict(c=c,n=n,tau=tau,mode=0,kappa=kap,H=z['Hraw']))
 for grid in [4,10]:
  name=f'J134_C2_{tag}_G{grid}';out=f.freeze(r,name,grid)
  for receipt in out['receipts']:
   key='inputs'if receipt['name'].endswith('.input.json')else'outputs';v=expected[key][receipt['name']]
   assert receipt['bytes']==v['bytes'] and receipt['sha256']==v['sha256']
print('J134_SELECTED_PRODUCER_RECOVERY_PASS_NO_110',flush=True)
```

## fine134.py — 551 bytes; SHA256 820e3eeacb983abf7f317baa6163954f8a9a92d220ec595502da58080dd9cf63
```python
"""The executed100-point finite twist grid; not a family impossibility proof."""
import json
from pathlib import Path
import twist134 as t
out=[]
for c in [-.99,-.98,-.97,-.95]:
 for n in [12,16,20,24,28]:
  for tau in [0.,.015,.05,.1,-.05]:
   try:r=t.close(c,n,tau)
   except Exception as exc:r=dict(c=c,n=n,tau=tau,error=str(exc))
   out.append(r)
   if 'own'in r:print(c,n,tau,r['E'],r['own'],r['kappa'],flush=True)
   Path('TWIST134_FINE.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('TWIST134_FINE_100_COMPLETE',flush=True)
```

## hspace134.py — 1707 bytes; SHA256 34dce85621a1c9346237dd9bfbd128ff4f737f6564033d3defadca6a63e6bac4
```python
"""Known-support finite C2 cuts, physical mass, and full numerical radial census."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np
from scipy.spatial import ConvexHull,HalfspaceIntersection
import geom134 as e

def geometry(H,interior=np.zeros(3),full=False):
 H=np.asarray(H,float);interior=np.asarray(interior,float);hs=HalfspaceIntersection(H,interior);X=hs.intersections
 faces=[];ids=[]
 for f in range(len(H)):
  inds=[i for i,ls in enumerate(hs.dual_facets)if f in ls]
  if len(inds)<3:continue
  n=H[f,:3];n=n/np.linalg.norm(n);u=X[inds[0]]-X[inds].mean(0);u-=n*(u@n);u/=np.linalg.norm(u);v=np.cross(n,u);W=X[inds]-X[inds].mean(0);ang=np.arctan2(W@v,W@u);ids.append(f);faces.append(np.array(inds)[np.argsort(ang)].tolist())
 E={};tri=[]
 for f,cy in enumerate(faces):
  for a,b in zip(cy,cy[1:]+cy[:1]):E.setdefault(tuple(sorted((a,b))),[]).append(f)
  tri.extend((cy[0],cy[j],cy[j+1])for j in range(1,len(cy)-1))
 assert all(len(ls)==2 for ls in E.values());assert len(X)-len(E)+len(faces)==2
 tri=np.array(tri);d=np.einsum('ij,ij->i',X[tri[:,0]],np.cross(X[tri[:,1]],X[tri[:,2]]));V=d.sum()/6
 assert V>0;g=(d[:,None]*X[tri].sum(1)).sum(0)/(24*V);Y=X-g
 n=H[ids,:3];h=-H[ids,3]-n@g;assert h.min()>0;Q=n/h[:,None]
 A=e.chords(Y);B=e.chords(Q);S=np.flatnonzero(B.max(1)<0);U=np.flatnonzero(A.max(1)<0)
 root=int(np.argmax((Q*Q).sum(1)));w,pa=e.widest(B,root)
 z=dict(V=len(X),E=len(E),F=len(faces),volume=V,centroid=g,S=len(S),U=len(U),S_indices=S,U_indices=U,X=X,Q=Q,A=A,B=B,root=root,capacity=w,faces=faces,ids=ids,edges=np.array(list(E)),dual=np.array(list(E.values())))
 if full:z.update(P=e.persistence(Y,z['edges']),Qbars=e.persistence(Q,z['dual']))
 return z
```

## head134.py — 2705 bytes; SHA256 ef06156832a7d9de6af71cf6854517275829751a6e4d583b29eb91dcc4616334
```python
"""Two-root polar head covering the entire near-apex parent S pool.
The head is a through-apex plane pair. It simultaneously gives positive
reference arrows from the two old polar roots in each half-turn half.
Then an explicit radial great-circle chain reaches the horizontal root.
The physical mass is closed by solving kappa, not by moving a free centre.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from pathlib import Path
import json,numpy as np
from scipy.optimize import brentq
import polar134 as p,geom134 as e,hspace134 as hs

Q0=p.H0[:,:3]/(-p.H0[:,3])[:,None]
W=Q0[[69,126],:2];headxy=np.linalg.solve(W,(W*W).sum(1)+1e-5)
head=np.r_[headxy,-1.];hr=np.linalg.norm(head);phi=np.arccos(-1/hr)

def body(c,kappa,n,full=False):
 cc=np.array([0.,0.,c]);rootR=1/(kappa*(1+c));r=hr/(1+c);chainratio=(rootR/r)*np.cos(phi/n)**n
 if chainratio<=1:raise ValueError('Nonpositive chain')
 u=head[:2]/np.linalg.norm(head[:2]);rows=[head/(1+c),head*np.array([-1,-1,1])/(1+c)]
 for k in range(1,n):
  ang=phi*(1-k/n);rr=r*(rootR/r)**(k/n);v=rr*np.r_[np.sin(ang)*u,np.cos(ang)];rows.extend([v,v*np.array([-1,-1,1])])
 rows.append(np.array([0.,0.,rootR]));rows=np.array(rows);H=np.vstack((p.H0,np.c_[rows,-1-rows@cc]));z=hs.geometry(H,interior=cc,full=full)
 ids=z['ids'];qr=H[ids,:3]/(-H[ids,3]-H[ids,:3]@cc)[:,None];A=e.chords(z['X']-cc);B=e.chords(qr)
 z.update(Hraw=H,referenceS=int(sum(B.max(1)<0)),referenceU=int(sum(A.max(1)<0)),chainratio=chainratio)
 return z

def run():
 out=[]
 print('HEAD',head.tolist(),'norm',hr,'phi',phi,'margins',(W@headxy-(W*W).sum(1)).tolist(),flush=True)
 for c in [-.98,-.97,-.95,-.9]:
  for n in [26,28,30,32,34,36,38]:
   upper=np.cos(phi/n)**n/hr-1e-7
   try:
    lo=.43;zl=body(c,lo,n);zu=body(c,upper,n);fl=zl['centroid'][2]-c;fu=zu['centroid'][2]-c
    rec=dict(c=c,n=n,low=lo,upper=upper,mass_bracket=[float(fl),float(fu)])
    if fl*fu<0:
     kap=brentq(lambda x:float(body(c,x,n)['centroid'][2])-c,lo,upper,xtol=2e-13);z=body(c,kap,n,True)
     rec.update(kappa=kap,V=z['V'],E=z['E'],F=z['F'],reference=[z['referenceS'],z['referenceU']],own=[z['S'],z['U']],g=z['centroid'].tolist(),X=z['X'].tolist(),H=z['Hraw'].tolist(),P=z['P'],Q=z['Qbars'],chainratio=z['chainratio'])
     print('CLOSURE',c,n,kap,'VEF',z['V'],z['E'],z['F'],'ref',z['referenceS'],z['referenceU'],'own',z['S'],z['U'],'Pmax',max([x['depth']for x in z['P']],default=0),flush=True)
    else:print('NO_BRACKET',c,n,fl,fu,flush=True)
    out.append(e.serial(rec))
   except Exception as exc:out.append(dict(c=c,n=n,error=str(exc)))
   Path('HEAD134_RESULTS.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('DONE',len(out),flush=True)
if __name__=='__main__':run()
```

## polar134.py — 3232 bytes; SHA256 5187d435c5d5dcd4c4dc1d6c3e2b1d93749d20a74149a8eb7007d729393588e8
```python
"""C2 common-root polar bridge with actual centroid fixed-point closure.
Input is literal C2_COMPACT_G8. Explicit great-circle/radial interpolation
is numerical nomination; original polar hull is enlarged, so old physical
supports may retire. Reference and own census are always kept distinct.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from pathlib import Path
import numpy as np,json,argparse
from scipy.spatial import ConvexHull
from scipy.optimize import brentq
import geom134 as e
import hspace134 as hs
D=json.load(open(Path(__file__).with_name('C2_COMPACT_G8.json')));X0=np.array(D['points'],float)/D['scale'];H0=ConvexHull(X0).equations
# Remove duplicate old horizontal plane without changing the original body.
_,ii=np.unique(np.round(H0,11),axis=0,return_index=True);H0=H0[np.sort(ii)]

def body(c,kappa,n,full=False):
 cc=np.array([0.,0.,c]);hh=-H0[:,3]-H0[:,:3]@cc
 if hh.min()<=0:raise ValueError('Reference outside parent')
 Q0=H0[:,:3]/hh[:,None];rad=np.linalg.norm(Q0,axis=1);j=int(np.argmax(np.where(Q0[:,2]<0,rad,-np.inf)));q=Q0[j];r=rad[j];R=1/(kappa*(1+c));phi=np.arccos(q[2]/r)
 if R<=r or (R/r)*np.cos(phi/n)**n<=1:raise ValueError('No positive equally spaced chain')
 u=q[:2]/np.linalg.norm(q[:2]);rows=[]
 for k in range(1,n):
  p=phi*(1-k/n);rr=r*(R/r)**(k/n);pnt=rr*np.r_[np.sin(p)*u,np.cos(p)];rows.extend([pnt,pnt*np.array([-1,-1,1])])
 rows.append(np.array([0.,0.,R]));rows=np.array(rows);H=np.vstack((H0,np.c_[rows,-1-rows@cc]));z=hs.geometry(H,interior=cc,full=full)
 # Same final physical hull, but reference c rather than its mass centre.
 ids=z['ids'];qr=H[ids,:3]/(-H[ids,3]-H[ids,:3]@cc)[:,None];B=e.chords(qr);Yr=z['X']-cc;A=e.chords(Yr)
 z.update(reference_c=c,referenceS=int(sum(B.max(1)<0)),referenceU=int(sum(A.max(1)<0)),Hraw=H,chain_start=j,chain_ratio=float((R/r)*np.cos(phi/n)**n),kappa=kappa,n=n)
 return z

def run():
 ledger=[];closures=[]
 for kappa in [.34,.35,.38,.4,.45]:
  for n in [6,8,10,12]:
   seq=[]
   for c in np.linspace(-.97,.05,35):
    try:
     z=body(c,kappa,n);g=float(z['centroid'][2]);rec=[kappa,n,float(c),z['V'],z['E'],z['F'],z['referenceS'],z['referenceU'],z['S'],z['U'],g,g-c];ledger.append(rec);seq.append((c,g-c))
    except Exception as exc:ledger.append([kappa,n,float(c),str(exc)])
   for (c0,y0),(c1,y1)in zip(seq,seq[1:]):
    if y0*y1>=0:continue
    try:
     c=brentq(lambda t:float(body(t,kappa,n)['centroid'][2])-t,c0,c1,xtol=2e-13);z=body(c,kappa,n,True)
     out=dict(c=c,kappa=kappa,n=n,V=z['V'],E=z['E'],F=z['F'],referenceS=z['referenceS'],referenceU=z['referenceU'],S=z['S'],U=z['U'],centroid=z['centroid'].tolist(),X=z['X'].tolist(),H=z['Hraw'].tolist(),P=z['P'],Q=z['Qbars'])
     closures.append(e.serial(out));print('CLOSED',kappa,n,c,'VEF',z['V'],z['E'],z['F'],'ref',z['referenceS'],z['referenceU'],'own',z['S'],z['U'],'maxP',max([p['depth']for p in z['P']],default=0),flush=True)
    except Exception as exc:ledger.append([kappa,n,str(exc)])
   Path('POLAR134_LEDGER.json').write_text(json.dumps(ledger,separators=(',',':'))+'\n');Path('POLAR134_CLOSURES.json').write_text(json.dumps(closures,separators=(',',':'))+'\n')
 print('DONE',len(ledger),'closures',len(closures),flush=True)
if __name__=='__main__':run()
```

## twist134.py — 3390 bytes; SHA256 58a9bb3d1cfaf5daaaa9ed94ce800891577c6500d38cf7c3e363f032b1f28763
```python
"""Finite nonplanar polar chains with actual uniform-centroid closure.
Keep the two-root through-apex head; change azimuth along the chain.
Log-radius increments pay each actual spherical turn plus uniform slack.
This certifies every consecutive reference arrow numerically and avoids
silently reusing a great-circle bound for a twisted curve. Rational endpoint
checks are separate. No sampled failure is a family exclusion.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
import json,argparse,numpy as np
from scipy.optimize import brentq
import head134 as h,polar134 as p,hspace134 as hs,geom134 as e

def directions(n,tau,mode=0):
 k=np.arange(n+1)/n;pol=h.phi*(1-k);az0=np.arctan2(h.head[1],h.head[0])
 if mode==0:az=az0+tau*np.sin(np.pi*k)
 elif mode==1:az=az0+tau*k
 elif mode==2:az=az0+tau*np.sin(2*np.pi*k)
 else:raise ValueError('Unknown curve')
 D=np.c_[np.sin(pol)*np.cos(az),np.sin(pol)*np.sin(az),np.cos(pol)]
 D[0]=h.head/h.hr;D[-1]=[0.,0.,1.]
 cs=np.einsum('ij,ij->i',D[:-1],D[1:]);
 if np.min(cs)<=0:raise ValueError('Turn >= pi/2')
 cost=-np.log(cs);return D,cost

def body(c,kappa,n,tau,mode=0,full=False):
 cc=np.array([0.,0.,c]);D,cost=directions(n,tau,mode);L=-np.log(kappa*h.hr);slack=(L-cost.sum())/n
 if slack<=0:raise ValueError('Nonpositive chain margin')
 r0=h.hr/(1+c);rr=r0*np.exp(np.r_[0.,np.cumsum(cost+slack)]);R=1/(kappa*(1+c));rr[-1]=R
 single=rr[:,None]*D;rows=np.vstack([q for v in single[:-1]for q in (v,v*[-1,-1,1])]+[single[-1]])
 if np.min(rows[:,2]) < -1/(1+c)-1e-8:raise ValueError('Original axial root cut away')
 H=np.vstack((p.H0,np.c_[rows,-1-rows@cc]));z=hs.geometry(H,cc,full=full)
 ids=z['ids'];Q=H[ids,:3]/(-H[ids,3]-H[ids,:3]@cc)[:,None];A=e.chords(z['X']-cc);B=e.chords(Q)
 z.update(Hraw=H,referenceS=int(sum(B.max(1)<0)),referenceU=int(sum(A.max(1)<0)),chain_logslack=slack,chain_max_kappa=np.exp(-cost.sum())/h.hr)
 return z

def close(c,n,tau,mode=0):
 _,cost=directions(n,tau,mode);lo=.334;hi=np.exp(-cost.sum())/h.hr-1e-7
 rec=dict(c=c,n=n,tau=tau,mode=mode,bracket=[lo,hi])
 if hi<=lo:rec['error']='No positive chain within necessary kappa>1/3';return rec
 a=body(c,lo,n,tau,mode);b=body(c,hi,n,tau,mode);fa=float(a['centroid'][2]-c);fb=float(b['centroid'][2]-c);rec['mass_bracket']=[fa,fb]
 if fa*fb>=0:return rec
 kap=brentq(lambda x:float(body(c,x,n,tau,mode)['centroid'][2])-c,lo,hi,xtol=1e-13);z=body(c,kap,n,tau,mode,True)
 rec.update(kappa=kap,V=z['V'],E=z['E'],F=z['F'],own=[z['S'],z['U']],reference=[z['referenceS'],z['referenceU']],g=z['centroid'],chain_logslack=z['chain_logslack'],P=z['P'],Q=z['Qbars'],X=z['X'],H=z['Hraw'])
 return e.serial(rec)

def run(mode=0):
 out=[]
 for c in [-.95,-.9]:
  for n in [18,22,26,30]:
   for tau in [-.8,-.4,-.2,0.,.2,.4,.8]:
    try:r=close(c,n,tau,mode)
    except Exception as exc:r=dict(c=c,n=n,tau=tau,mode=mode,error=str(exc))
    out.append(r)
    if 'own'in r:print('TWIST',c,n,tau,'E',r['E'],'own',r['own'],'kap',r['kappa'],'Pmax',max([x['depth']for x in r['P']],default=0),flush=True)
    Path(f'TWIST134_M{mode}.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('TWIST_FINITE_GRID',len(out),'closures',sum('own'in r for r in out),flush=True)
if __name__=='__main__':
 q=argparse.ArgumentParser();q.add_argument('--mode',type=int,default=0);a=q.parse_args();run(a.mode)
```
