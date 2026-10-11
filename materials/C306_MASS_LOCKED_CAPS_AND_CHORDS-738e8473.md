# material-738e84735c7f

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C306 two exact-mass deformation principles and complete finite numerical scouts

This is a reusable method capsule, not a new accepted own110 body or a geometric exclusion. The complete exact C306 input is the literal farthest_merged_G10000.json and exact_tri_audit.py in immutable [internal-source-reference] (source SHA f86dc15bccb15df88836b33a6d6852b2a33a1f66cc77168c4c51fb4a31af7f21). Both complete imported helpers cut_search.py and hinge_search.py are in immutable [internal-source-reference] (SHA4b28984fd34e3e0f4866cb7114468873034e67b40cca4cbf07e1419df105cbd2). These two materials are explicit required dependencies; their literal source files, not IDs alone, must accompany this capsule for worker recovery. No originating sandbox or optimizer checkpoint is required. C306 means V53/E153/F102 own121weak000 at its ordinary volume centroid, Sface0,Uinput0/14,H44–46; it is not a renamed C318.

## 1. Balanced opposite pyramidal caps: exact analytic mass lock
Take a convex central belt K0 between parallel opposite facets B0:n.x=l and B1:n.x=u, l<u. Its remaining side inequalities are fj(x)<=0. Attach a0 below l and a1 above u, each satisfying every side inequality. Each apex sees only its respective base. The body is the belt plus the two pyramids, not an assumed-convex arbitrary union. To see convexity, a lower-cap facet built from a side fj is fj(x)+lambda_j(l-n.x)<=0 with lambda_j=-fj(a0)/(l-n.a0)>=0. The other apex satisfies this inequality because fj(a1)<=0 and l-n.a1<0. The same argument applies to upper-cap facets, so both additions are mutually compatible and their union is the convex hull. Redundant side inequalities do not affect this argument.

Let Vi be the volume of pyramid i and gi the true uniform area centroid of its fixed base. Its first moment is Mi=Vi(ai+3gi)/4. Tangential apex shifts a0->a0+t and a1->a1-(V0/V1)t, n.t=0, preserve both fixed normal heights, hence the individual volumes and all three total first moments exactly. The actual ordinary centroid is constant throughout the family. The permitted t form a linear two-dimensional halfspace polytope from the side inequalities. Rational base geometry, tangent basis, heights and shifts give rational bodies and rational volume ratios. The code below uses floating orthonormal coordinates only as a scout. Its section-vertex arithmetic means choose interior anchor points; they are NOT misidentified as the gi used in the proof.

The initially shortened cap replacements generally change the original C306 volume/centroid. The analytic lock and numerical comparison are within each resulting two-cap family, not a claim that every family retains the original C306 center. Nonparallel bases generally permit only one common tangential shift direction.

Executed balanced_caps.py scan: seed19192603,300requested/300valid/0rejected families,11503 actual-hull body evaluations,865 different(S,U) pairs,minimum observed S6,minimum U2,minimum(S+U)14. No numericalSU11. Maximum volume/centroid deviation from each family's baseline6.661338147750939e-16. Each evaluation takes the actual convex hull and recomputes filled moments through geom_fast. No candidate was exactified or promoted. These numbers are from the complete on-disk JSON/log associated with the source hash below; they are finite numerical observations, not a general theorem that cap deformation cannot work.

## 2. Constant-width parallel chords and a Steiner/reflection homotopy
For a unit direction v and projected x in a fixed planar convex domain D, write K={(x,z):g(x)<=z<=f(x)}, with g convex and f concave. Let c_v be the original ordinary centroid component along v. For t in[0,1], define
 g_t=(1-t)g-t f+2t c_v,
 f_t=(1-t)f-t g+2t c_v.
Then g_t is convex, f_t concave and f_t-g_t=f-g=w. Volume and both horizontal first moments are unchanged. The chord midpoint is m_t=(1-2t)m+2t c_v. Since the w-weighted mean of the old midpoint m is c_v, the vertical first moment is unchanged as well. Thus the actual ordinary centroid is exactly constant. t=0 is the input, t=1 its reflection in z=c_v, and t=1/2 its centroid-plane Steiner symmetrization. Parallel-chord movements and Steiner shadow systems are established constructions; no novelty of that general notion is asserted. The above centered formula and deductions are explicit here.

For a generic direction of a simplicial input with N vertices and F0 facets, let h be the number of silhouette edges and x the number of proper crossings between projected upper-internal and lower-internal edges. Their overlay has F0-1+x planar cells. If no further accidental coincidences occur and 0<t<1, both surfaces carry every overlay crease, so V'=2N-h+2x, F'=2(F0-1+x), E'=3F0-h+4x. This is an overlay combinatorial count, not an exact audit of near-degenerate floating outputs. For C306,N53,F0102,5000 random unit directions(seed26091933) gave minimum predicted E872, at direction index3361, v=(.5184362964147529,.1541264820047212,.8411116656571843),x147,h22,V'378,F'496. All5000 were valid. It is only a finite directional minimum, not a lower bound for every possible direction or every chord deformation.

The20 directions of least predicted E were each tested at t=.005,.02,.05,.1,.2,.35,.5:140 actual-hull evaluations,maximum original-volume/centroid discrepancy1.7763568394002505e-15. Minimum observed S5,U2,and S+U7; noSU11. Floating actual V+F-2 ranged872..983, far above310. At a near-endpoint t=.005 even small Steiner mixing creates all generic interface edges. Finite mass preservation succeeded; both complexity and equilibrium counts failed the research objective. None of these outputs is an accepted exact nonwinner.

## Next constructive frontier, not yet an executed result
The uniform Steiner mixture unnecessarily puts both original crease meshes on both surfaces. A more general piecewise-affine chord shift beta(x) yields lower g+beta, upper f+beta. On a conforming common projected triangulation, convexity of the lower and concavity of the upper are linear inequalities in nodal beta. Width/volume/horizontal moments stay fixed; the one vertical first-moment condition is integral_D w*beta=0, linear in beta, with exact triangle mass-matrix coefficients when w and beta are affine on each triangle. This offers a linear feasible region of exact-own-mass convex deformations. Finite endpoint coalescences may remove transferred creases, but no such low-complexity endpoint has been constructed or proved here. Use a conforming overlay, NOT unconstrained Delaunay that may cross old crease edges. Rebuild genuine maximal facets/edges after coalescence. Affine shear directions make the unbounded feasible set noncompact; any box/gauge used for LP sampling must be explicitly scoped rather than mistaken for a global obstruction.

## Reconstruct, run, inspect
Recover the exact input and imported full helper files from the two explicit immutable dependencies. Save both Python units below in the same directory with LF and one final newline. Run there with assertions enabled:
```sh
OPENBLAS_NUM_THREADS=1 python -u balanced_caps.py 300 > balanced_caps_scan.log
OPENBLAS_NUM_THREADS=1 python -u steiner_scout.py 5000 > steiner_scout.log
python - <<'PY'
import json
b=json.load(open('balanced_caps_scan.json'));r=b['records']
assert b['families_valid']==300 and len(r)==11503
assert not any(q['g']['S']==q['g']['U']==1 for q in r)
a=json.load(open('steiner_directions.json'));assert len(a['records'])==5000
assert a['best']['expected']['E']==872
s=json.load(open('steiner_trials.json'));assert len(s['records'])==140
assert s['maximum_mass_error']<1e-9
assert not any(q['g']['S']==q['g']['U']==1 for q in s['records'])
print('C306_MASS_LOCKED_FAMILIES_FINITE_REPLAY_PASS')
PY
```
Expected terminal lines BALANCED_CAPS_SCAN_DONE300 11503 6.661338147750939e-16 865 6 2; STEINER_DIRECTIONS_DONE5000(minimumE872); STEINER_TRIALS_DONE140 1.7763568394002505e-15 7. The final checking heredoc is provided for recovery; original outcomes were inspected directly in the emitted JSON/logs. CPython3.13.5 GCC14.2.0,NumPy2.3.5,SciPy1.17.0,float64,OPENBLAS_NUM_THREADS=1 were used. Float/Qhull/platform differences may alter exact output bytes or threshold counts. geom_fast groups facet equations to9decimals and uses1e-9 strict thresholds: neither hash agreement nor these numerical counts substitutes for the full exact maximal-complex/strict/weak auditor.

Input identity farthest_merged_G10000.json2051bytes(no final newline),SHA89599e0825f7075c151639b70d9db5959fcdc058c0be555d1a96d8598ccdea3e. Imported cut_search.py3937bytes SHA71d96309d3f6f43c6f2895050d8f735cd4059c3671df77216ff49e18b9f4326f; hinge_search.py4568bytes SHA875db74467f5de4d44c5aea588283dd9c3e7999afca1587668c89e28136488dc.
Observed source/output byte identities:
- balanced_caps.py3952 SHA4a6154fbcd06c896bff8b5d410beb386d6bc5b013dc339b6683bf2750f02858e
- balanced_caps_scan.json8102936 SHA91cf4f9c426988cdfff5eb651fb3f7044f8c94c05923fd07b227f75d92a5b73e
- balanced_caps_scan.log64 SHA7d28aa875dce7a8e5ffe5a8b5bc77d25f949b77a12f51d75f8201f5bb947d8a1
- steiner_scout.py3280 SHA4f94e44d9414fa88d79050e2a5bca1a1fb8645e2d3f4780fec916ec9c7c91128
- steiner_directions.json730552 SHA754eec8d26bac875f4c1f6350d0261bcdac387c51ee84ddc383cbb4be719cb9d
- steiner_trials.json75632 SHAbf752080cfe1b7e6d6967aec11be89f1927b0b41ec73c81f5c50b264b602fc94
- steiner_scout.log2453 SHA705236bf3f37ed71f349630a58ed2a02a9224337578b2e172581e50c2ab34e83
Bulk scan arrays are reproduced from the complete literal inputs/source/seeds rather than redundantly embedded.

## balanced_caps.py
```python
"""Finite own-mass scout in a two-cap family with analytically constant volume/centroid.
Caps have fixed parallel bases and fixed heights. Opposed tangential apex shifts
are weighted by their pyramid volumes. Only feasible single-facet attachments
are sampled; the actual convex hull/filled moment is independently recomputed.
Floating exploration only, never a maximal-complex or equilibrium certificate.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json,sys,pathlib
import numpy as np
from scipy.spatial import ConvexHull,HalfspaceIntersection
from cut_search import P,E
from hinge_search import geom_fast,merit

def basis(n):
 i=int(np.argmin(abs(n)));e=np.eye(3)[i];u=np.cross(n,e);u/=np.linalg.norm(u);v=np.cross(n,u)
 return np.array([u,v])

def section(n,h):
 d=P@n-h;a,b=E.T;w=d[a]*d[b]<0;a=a[w];b=b[w]
 return P[a]+(P[b]-P[a])*(d[a]/(d[a]-d[b]))[:,None]

def family(z):
 # z: normal perturbation(3), lower/upper cut fractions, two cap-height fractions.
 n=np.asarray(z[:3],float);n/=np.linalg.norm(n);B=basis(n);pr=P@n
 lo=pr.min()+z[3]*np.ptp(pr);hi=pr.min()+z[4]*np.ptp(pr)
 if not pr[0]<lo<hi<pr[14]:raise ValueError('roots outside intended caps')
 C0,C1=section(n,lo),section(n,hi)
 if min(len(C0),len(C1))<3:raise ValueError('degenerate bases')
 belt=np.vstack((P[(pr>=lo)&(pr<=hi)],C0,C1))
 base0,base1=C0.mean(0),C1.mean(0)
 a0=z[5]*P[0]+(1-z[5])*base0;a1=z[6]*P[14]+(1-z[6])*base1
 area0=ConvexHull(C0@B.T).volume;area1=ConvexHull(C1@B.T).volume
 V0=area0*(lo-a0@n)/3;V1=area1*(a1@n-hi)/3;rho=V0/V1
 h=ConvexHull(belt);eq=np.unique(np.round(h.equations,12),axis=0)
 side=eq[np.abs(eq[:,:3]@n)<1-1e-8]
 A=np.vstack((side[:,:3]@B.T,-rho*side[:,:3]@B.T))
 b=np.r_[-side[:,:3]@a0-side[:,3],-side[:,:3]@a1-side[:,3]]
 if min(b)<1e-10:raise ValueError('not strictly attachable')
 poly=HalfspaceIntersection(np.c_[A,-b],np.zeros(2)).intersections
 cpoly=ConvexHull(poly);poly=poly[cpoly.vertices]
 return dict(belt=belt,a0=a0,a1=a1,B=B,rho=rho,A=A,b=b,poly=poly,Vcaps=[V0,V1],n=n,lo=lo,hi=hi)

def shape(f,s):
 d=np.asarray(s)@f['B'];return np.vstack((f['belt'],f['a0']+d,f['a1']-f['rho']*d))

def main():
 seed=19192603;rng=np.random.default_rng(seed);NF=int(sys.argv[1]) if len(sys.argv)>1 else 300
 axis=P[14]-P[0];axis/=np.linalg.norm(axis);allr=[];best={};maxerr=0.;accepted=0;fails=0
 for k in range(NF):
  n=axis+rng.normal(0,.20,3)
  z=[*n,rng.uniform(.08,.47),rng.uniform(.53,.92),rng.uniform(.08,.98),rng.uniform(.08,.98)]
  try:f=family(z);g0=geom_fast(shape(f,[0,0]));accepted+=1
  except Exception:fails+=1;continue
  pp=f['poly'];samples=[np.zeros(2),*.99*pp]
  # Uniform mixture of interior convex combinations, not claimed uniform area sampling.
  for _ in range(16):
   w=rng.exponential(1,len(pp));w/=w.sum();samples.append(w@pp)
  for j,s in enumerate(samples):
   if (f['A']@s-f['b']).max()>1e-8:raise AssertionError('cap feasibility')
   g=geom_fast(shape(f,s));err=max(abs(g['vol']-g0['vol']),np.linalg.norm(np.array(g['c'])-g0['c']))
   maxerr=max(maxerr,err)
   if err>2e-10:raise AssertionError(('mass lock failure',err))
   row=dict(k=k,j=j,z=[float(x) for x in z],shift=s.tolist(),g=g,volume_ratio=f['rho'],mass_error=err)
   allr.append(row);key=f"{g['S']}_{g['U']}"
   if key not in best or merit(g)<merit(best[key]['g']):
    best[key]=row
    if g['S']+g['U']<=4:print('CAP_BEST',key,row,flush=True)
   if g['S']==g['U']==1:print('NUMERICAL_CAP_SU11',row,flush=True);break
  if any(r['g']['S']==r['g']['U']==1 for r in allr):break
 out=dict(seed=seed,families_requested=NF,families_attempted=k+1,families_valid=accepted,families_rejected=fails,evaluations=len(allr),maximum_mass_lock_error=maxerr,best=best,records=allr)
 pathlib.Path('balanced_caps_scan.json').write_text(json.dumps(out,separators=(',',':')))
 print('BALANCED_CAPS_SCAN_DONE',accepted,len(allr),maxerr,len(best),min(r['g']['S'] for r in allr),min(r['g']['U'] for r in allr),flush=True)
if __name__=='__main__':main()
```

## steiner_scout.py
```python
"""Centroid-preserving Steiner/reflection homotopy of an exact-input polyhedron.
Floating scout. Counts below assume generic direction and simplicial input.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json,sys,pathlib
import numpy as np
from scipy.spatial import ConvexHull
from cut_search import P,T,E
from hinge_search import geom_fast
A,B,C=np.moveaxis(P[T],1,0);N=np.cross(B-A,C-A);N/=np.linalg.norm(N,axis=1)[:,None];H=(N*A).sum(1)
EF=np.array([[i for i,t in enumerate(T) if set(e).issubset(t)] for e in E])
assert EF.shape==(len(E),2)
BASE=geom_fast(P);CENTER=np.array(BASE['c'])

def basis(v):
 u=np.cross(v,np.eye(3)[np.argmin(abs(v))]);u/=np.linalg.norm(u);return np.array([u,np.cross(v,u)])
def cross2(a,b):return a[...,0]*b[...,1]-a[...,1]*b[...,0]
def diagram(v,detail=False):
 v=np.asarray(v,float);v/=np.linalg.norm(v);B=basis(v);nv=N@v
 if min(abs(nv))<1e-10:raise ValueError('non-generic facet')
 et=np.sign(nv[EF]).sum(1);up=E[et>0];lo=E[et<0];sil=E[et==0]
 X=P@B.T;p=X[up[:,0]][:,None,:];r=(X[up[:,1]]-X[up[:,0]])[:,None,:]
 q=X[lo[:,0]][None,:,:];s=(X[lo[:,1]]-X[lo[:,0]])[None,:,:];d=cross2(r,s)
 den=np.where(abs(d)>1e-13,d,np.inf);aa=cross2(q-p,s)/den;bb=cross2(q-p,r)/den
 mask=(aa>1e-9)&(aa<1-1e-9)&(bb>1e-9)&(bb<1-1e-9)&(abs(d)>1e-13)
 ne=int(mask.sum());h=len(sil);expected=dict(V=2*len(P)-h+2*ne,F=2*(len(T)-1+ne),E=3*len(T)-h+4*ne)
 if not detail:return ne,h,expected
 points=(p+aa[:,:,None]*r)[mask];X=np.vstack((X,points))
 upper=(H[nv>0,None]-(N[nv>0]@B.T)@X.T)/nv[nv>0,None]
 lower=(H[nv<0,None]-(N[nv<0]@B.T)@X.T)/nv[nv<0,None]
 zup=upper.min(0);zlo=lower.max(0)
 if min(zup-zlo)<-1e-8:raise ValueError('bad overlay')
 return dict(v=v,B=B,X=X,up=zup,lo=zlo,c=float(CENTER@v),crossings=ne,silhouette=h,expected=expected)
def shape(d,t):
 lo=(1-t)*d['lo']-t*d['up']+2*t*d['c'];hi=(1-t)*d['up']-t*d['lo']+2*t*d['c']
 return np.vstack((d['X']@d['B']+lo[:,None]*d['v'],d['X']@d['B']+hi[:,None]*d['v']))
def main():
 seed=26091933;rng=np.random.default_rng(seed);num=int(sys.argv[1]) if len(sys.argv)>1 else 5000
 records=[];best=None;bad=0
 for k in range(num):
  v=rng.normal(size=3);v/=np.linalg.norm(v)
  try:cross,h,ex=diagram(v)
  except ValueError:bad+=1;continue
  row=dict(k=k,v=v.tolist(),crossings=cross,silhouette=h,expected=ex);records.append(row)
  if best is None or ex['E']<best['expected']['E']:
   best=row;print('STEINER_OVERLAY_IMPROVED',best,flush=True)
 out=dict(seed=seed,attempted=num,rejected=bad,best=best,records=records)
 pathlib.Path('steiner_directions.json').write_text(json.dumps(out,separators=(',',':')))
 print('STEINER_DIRECTIONS_DONE',len(records),best,flush=True)
 tested=[];maxerr=0.
 for row in sorted(records,key=lambda r:r['expected']['E'])[:20]:
  d=diagram(row['v'],True)
  for t in [.005,.02,.05,.1,.2,.35,.5]:
   g=geom_fast(shape(d,t));err=max(abs(g['vol']-BASE['vol']),np.linalg.norm(np.array(g['c'])-CENTER));maxerr=max(maxerr,err)
   assert err<1e-9
   tested.append(dict(direction=row,t=t,g=g,mass_error=err))
 pathlib.Path('steiner_trials.json').write_text(json.dumps(dict(records=tested,maximum_mass_error=maxerr),separators=(',',':')))
 print('STEINER_TRIALS_DONE',len(tested),maxerr,min(r['g']['S']+r['g']['U'] for r in tested),flush=True)
if __name__=='__main__':main()
```
