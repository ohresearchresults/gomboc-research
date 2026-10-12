
## 2026-09-15T21:29:19.416Z

### C282 physical-polar chain experiment — complete bounded-method recovery capsule

The exact standalone C282 recovery was executed here from its49 listed integer points and the three unchanged FINCH3 core files, whose entire sources were read and SHA-bound. `python -B -S exact_points.py POINTS49.json recovered282 --core core` reproduced `EXACT_INTEGER_POINT_HULL_AB_MASS_PASS 49 141 94 [2,1,1] [0,0,0]` and every raw/A/B/MASS byte hash in the21:02:48 capsule. This supplied geometry for new constructive work, not a new record.

The proposed physical-polar chain mechanism was then actually executed on a finite27-case domain: n in[12,20,32], bow in[-1,0,1], endpoint gain in[1,1.5,2], bulge0, opposed arcs, forward H28-to-H93, root maxfev160. All27 physical centroid fixed-point solves converged with residual<=2.077e-13, but NONE had own110. Thus solving the true mass closure alone does not cancel the remaining S/H pair. The original endpoint polar radii are approximately15.50468126 and15.76471890. Large bow/gain cuts can replace almost all original material and introduce additional U. Best by(S+U+uncertain,Eproposal) was a numerical own222 proposal with V178/F92/E268 at n32,bow0,gain2; this is NOT an exact retained body or a proved true-edge count. No global geometric exclusion follows. No floating output is used as a descendant checkpoint.

**Complete recovery source and exact inputs.** Place this source as dual_chain.py beside the existing recovered282 directory whose raw.json and A.json are reproduced by the previous C282 capsule. This entire source is5008 UTF-8/LF bytes, final newline, SHAd0677e0070d5475b75039a26c3d90f9bdd56b025d79c3fed3e4729c042b55e7b. CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1. The raw H input must retain SHA8254152f25df690b4da9ab394ab44c25041d449bfaa552272f5455c43b09c1e7 and A.json SHA374a1eda3378fbee5cb42d9fe11d52312215fa3a15b222768a2d5f8d2a16bbce. Numerical grouping by rounding is only proposal machinery, never exact incidence evidence.

```python
"""C282 finite polar escape-chain proposal; mass is always physical hull volume.
Exact input/audit hashes are bound. Numerical output is not an exact certificate.
"""
import argparse,hashlib,json,itertools
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import root

def encoded(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def load():
 p=Path(__file__).resolve().parent/'recovered282';b=(p/'A.json').read_bytes();assert hashlib.sha256(b).hexdigest()=='374a1eda3378fbee5cb42d9fe11d52312215fa3a15b222768a2d5f8d2a16bbce';a=json.loads(b)
 P=np.array([[float(F(t)) for t in v] for v in a['raw_vertices']])/1000
 g=np.array([float(F(t)) for t in a['raw_centroid']])/1000
 H=np.array(json.loads((p/'raw.json').read_bytes())['H'],float);Q=H[:,:3]/H[:,3:]*1000
 return P,Q,g

def mass(P):
 h=ConvexHull(P);anchor=P[h.vertices].mean(axis=0);tri=h.simplices;A=P[tri]-anchor
 d=np.einsum('ni,ni->n',A[:,0],np.cross(A[:,1],A[:,2]));orientation=np.sign(np.einsum('ni,ni->n',np.cross(A[:,1]-A[:,0],A[:,2]-A[:,0]),h.equations[:,:3]));d*=orientation
 assert min(d)>0
 return d.sum()/6,anchor+np.einsum('n,ni->i',d,A.sum(axis=1))/(4*d.sum()),h

def invert(Q):
 h=ConvexHull(Q);b=-h.equations[:,3]
 if min(b)<=1e-11:raise ValueError('Unbounded polar')
 P=h.equations[:,:3]/b[:,None]
 # Merge only for numerical mass conditioning; exact reconstruction is separate.
 _,ix=np.unique(np.round(P,10),axis=0,return_index=True);return P[np.sort(ix)]

def escapes(X):
 D=X[None,:,:]-X[:,None,:];norm=np.linalg.norm(X,axis=1);dn=np.linalg.norm(D,axis=2)
 v=np.einsum('ik,ijk->ij',X,D)/np.maximum(norm[:,None]*dn,1e-300);np.fill_diagonal(v,-np.inf)
 return v.max(axis=1)

def census(P):
 v,g,h=mass(P);X=P[h.vertices]-g;u=escapes(X);n=h.equations[:,:3];b=-h.equations[:,3]-n@g;Q=n/b[:,None];_,ix=np.unique(np.round(Q,9),axis=0,return_index=True);Q=Q[np.sort(ix)];s=escapes(Q)
 return dict(V=len(h.vertices),F=len(Q),E_proposal=len(h.vertices)+len(Q)-2,S=int(sum(s<-1e-9)),U=int(sum(u<-1e-9)),S_uncertain=int(sum(abs(s)<=1e-9)),U_uncertain=int(sum(abs(u)<=1e-9)),stable_ids=np.where(s<-1e-9)[0].tolist(),unstable_ids=np.where(u<-1e-9)[0].tolist(),centroid=g.tolist(),volume=float(v),min_s=float(min(s)),min_u=float(min(u)))

def chain(Q,c,n,bow,bulge,gain,opposed=True,reverse=False):
 d=1-Q@c
 if min(d)<=1e-7:raise ValueError('Centre outside original body')
 R=Q/d[:,None];a=R[28 if not reverse else 93];b=R[93 if not reverse else 28]*gain
 ra,rb=np.linalg.norm(a),np.linalg.norm(b);u=a/ra;v=b/rb;cos=np.clip(u@v,-1,1);phi=np.arccos(cos);e=v-cos*u;e/=np.linalg.norm(e);w=np.cross(u,e)
 t=np.arange(1,n)/n;points=[b[None,:]]
 for angle in ([phi,phi-2*np.pi] if opposed else [phi]):
  direction=np.cos(t*angle)[:,None]*u+np.sin(t*angle)[:,None]*e;direction+=bow*np.sin(np.pi*t)[:,None]*w;direction/=np.linalg.norm(direction,axis=1)[:,None]
  radius=ra*(rb/ra)**t*np.exp(bulge*np.sin(np.pi*t)**2);points.append(radius[:,None]*direction)
 return np.r_[R,np.concatenate(points)]

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--n',type=int,nargs='+',default=[12,20,32]);p.add_argument('--bow',type=float,nargs='+',default=[-1.,0.,1.]);p.add_argument('--gain',type=float,nargs='+',default=[1.,1.5,2.]);p.add_argument('--bulge',type=float,nargs='+',default=[0.]);p.add_argument('--single',action='store_true');p.add_argument('--reverse',action='store_true');p.add_argument('--maxfev',type=int,default=160);a=p.parse_args();out=Path(a.out);out.mkdir(exist_ok=False)
 P,Q,g=load();print('PARENT',census(P),flush=True);print('ENDPOINT_RADII',np.linalg.norm(Q[[28,93]]/(1-Q[[28,93]]@g)[:,None],axis=1),flush=True);records=[];best=None
 for n,bow,gain,bulge in itertools.product(a.n,a.bow,a.gain,a.bulge):
  def fun(c):
   try:return mass(invert(chain(Q,c,n,bow,bulge,gain,not a.single,a.reverse)))[1]
   except (ValueError,QhullError,AssertionError):return (c-g)*100+np.array([1.,1.,1.])
  r=root(fun,g,method='hybr',options={'xtol':1e-9,'maxfev':a.maxfev});c=r.x
  rec=dict(n=n,bow=bow,gain=gain,bulge=bulge,opposed=not a.single,reverse=a.reverse,c=c.tolist(),root_status=int(r.status),nfev=int(r.nfev),closure=float(np.linalg.norm(fun(c))))
  try:
   Z=chain(Q,c,n,bow,bulge,gain,not a.single,a.reverse);X=invert(Z)+c;rec.update(census(X));rank=(rec['S']+rec['U']+rec['S_uncertain']+rec['U_uncertain'],rec['E_proposal'])
   if best is None or rank<best:
    best=rank;(out/'BEST.json').write_bytes(encoded({'record':rec,'Q_about_chart_centre':Z.tolist(),'points':X.tolist()}));print('BEST',rank,rec,flush=True)
  except (ValueError,QhullError,AssertionError) as e:rec['error']=str(e)
  records.append(rec);(out/'SEARCH.json').write_bytes(encoded({'parameters':vars(a),'records':records}));print('CASE',len(records),rec.get('S'),rec.get('U'),rec['closure'],flush=True)
 print('C282_POLAR_CHAIN_SEARCH_FINISHED',len(records),best,flush=True)
if __name__=='__main__':main()
```

**Executed command and terminal marker.** `OPENBLAS_NUM_THREADS=1 python dual_chain.py --out dual27` observed `C282_POLAR_CHAIN_SEARCH_FINISHED 27 (4,268)`. In the stated environment SEARCH.json is14046bytes SHAf7b2d8a84c847ed8a66f50590b12714c9700d6c39bb309b5aaaf643eced1c939 and BEST.json21117bytes SHAd9ac24091a13911f8f9cbc8a9e81909b50df38323ba8ed787b3335f46f50c1b6. These identify reproducible numerical transcripts, not exact-polyhedron certificates; none is a required input for continuation. The full seed, code and finite domain above reconstruct the experiment without them. No new recovery debt for this method remains.

The next upper-layer question is whether C282's remaining bistability is quantitatively forced by a central disk/slab, and which finite non-affine or far-affine shape changes can escape it while keeping the now-solved U1. Do not equate tiny closure residual with mono-monostaticity.

## 2026-09-15T21:35:59.184Z

### Complete recovery capsule — COORD_C138_INTEGER_VERTEX25_OWN211

A new exact coordinator-owned nonwinner has **V25/E69/F46, C138, own strict211/weak000**. It is obtained by genuine vertex deletion from the49-integer C282 body, not by an affine transformation or reference-centre census. All46 maximal facets are triangles. BOTH independent full exact auditors agree on every field, and third centred integer-tetrahedron integration confirms exactly zero first moments. A second cold reconstruction from ONLY the25 listed integer points gives byte-identical raw/A/B/MASS outputs. This is NOT a Gömböc; accepted own110 benchmark remains C622. Its241-edge headroom up to E310 and tiny arithmetic make it a useful different continuation source.

**Exact standalone definition.** The body is the uniform filled convex hull of the following25 integer points. Save the single line as POINTS25.json with UTF-8 and NO final newline:425bytes,SHA1be5293390fbabf8b86b02805771d0fed82fddd2c61678b58d36c7bab9f93cd8.

```json
{"object":"COORD_C138_INTEGER_VERTEX25_OWN211","points":[[-507,187,93],[-503,185,-16],[-491,182,204],[-479,176,-120],[-452,168,312],[-437,160,-215],[-394,146,411],[-379,139,-297],[-316,118,498],[-308,113,-363],[-229,83,-412],[-221,83,568],[-144,52,-442],[-112,43,617],[6,0,643],[38,-79,-367],[118,-41,616],[221,-79,568],[311,-113,502],[386,-141,420],[443,-162,327],[482,-177,226],[485,-179,-84],[502,-184,121],[503,-185,17]]}
```

**Exact moments and mechanics.** Volume102823997/6. Own centroid=(-1510919059/205647994,-1322990120/102823997,-1106176611/411295988). Unique U is new raw-lex14=(6,0,643); stable faces22,45 and saddle true edge(15,22), in THIS object's lex primitive H ordering. Common centred denominator29bits; integer numerators at most38bits. Third integration has46 positive tetrahedra. Do not transfer C282's face/vertex numbers or its old centroid to this body.

**Reconstruction and verification dependencies.** Use the complete exact_points.py already journaled in C282 part1 at21:02:48,2031bytes,SHAe0cd67ba8ee150996c387c03cb91629dea8ce5fb1252fb1af832018cdac980db, and the unchanged core/check_A.py5483bytes/SHAad72cc198140249c1e52a615513354036c04f4c718333a7beed64fba4b43d7f3; core/check_B.py6351bytes/SHAb0cb62d5486b32d020b60f717f3dfe9d07c6c9a978492928f54c3a38f396fc24; core/centred_mass.py1398bytes/SHA5f1afafa0432436bfe953a94d94ca1027c12549504f9452491f0287c2a29d1a8. These three literal core sources are completely preserved in FINCH3 six-part recovery ending20:31:06; no originating sandbox is required. They were recovered, read fully and hash-matched this turn.

Run `python -B -S exact_points.py POINTS25.json exact138 --core core` with output absent. Observed `EXACT_INTEGER_POINT_HULL_AB_MASS_PASS 25 69 46 [2,1,1] [0,0,0]`. Output raw.json1157bytes,SHA5eb68c9a67409dd582d79df1fcdc764d057da979db0e53373c0a7c086221582f; A.json/B.json each5169bytes,SHAb8b614fec6f96fbc7844e1fe3ed3232d62587d1310fdb2c2b6e40f17ab1dabc0; MASS.json216bytes,SHA82e54e84b880d4c233477d50b31af9df0772081d3800f6693f4727ebac3e90bf. Repeat with output cold138; every file matched, observed `C138_COLD25_REPLAY_BITWISE_PASS`.

**Complete finite production method.** The following source vertexbeam282.py is2137bytes,SHA2f82f8938825723be9d531a09e4025199fead8e6d175eb8eadf99f49eade3e5a, UTF-8/LF with final newline. It depends only on the exact49-point input in the21:02:48 C282 capsule and complete numerical dual_chain.py in the21:29:19 capsule. NumPy2.3.5/SciPy1.17.0/CPython3.13.5, OPENBLAS_NUM_THREADS=1. Its numerical proposal classifier is not the basis of exact acceptance above.

```python
"""Finite deletion beam over the standalone 49-integer C282 point set.
Only actual filled-volume centroids are used. Numerical selection is not proof.
"""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import QhullError
from dual_chain import census,encoded

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--beam',type=int,default=6);p.add_argument('--maxsu',type=int,default=3);a=p.parse_args();out=Path(a.out);out.mkdir(exist_ok=False)
 b=(Path(__file__).resolve().parent/'POINTS49.json').read_bytes();assert hashlib.sha256(b).hexdigest()=='c01c8c5eb79a099250ea9f2c8cf8d85a17546abe7ab2b58129a78a6df3e1aaa7';P=np.array(json.loads(b)['points'],float)/1000
 level=[list(range(len(P)))];seen={tuple(level[0])};best={};rows=[];tested=0;winner=False
 for depth in range(1,len(P)-3):
  bucket={}
  for ids in level:
   for delete in ids:
    keep=tuple(i for i in ids if i!=delete)
    if keep in seen:continue
    seen.add(keep);tested+=1
    try:r=census(P[list(keep)])
    except (ValueError,QhullError,AssertionError):continue
    if r['S_uncertain'] or r['U_uncertain'] or r['S']+r['U']>a.maxsu:continue
    r['ids']=list(keep);key=(r['S'],r['U']);rank=(r['E_proposal'],r['min_s'],r['ids']);bucket.setdefault(key,[]).append(r)
    if key not in best or rank<(best[key]['E_proposal'],best[key]['min_s'],best[key]['ids']):best[key]=r;(out/('BEST_%d%d.json'%key)).write_bytes(encoded(r));print('BEST',depth,key,r['V'],r['E_proposal'],flush=True)
    if key==(1,1):winner=True;break
   if winner:break
  level=[]
  for key,rr in sorted(bucket.items()):level+=[r['ids'] for r in sorted(rr,key=lambda r:(r['E_proposal'],r['min_s'],r['ids']))[:a.beam]]
  rows.append({'depth':depth,'tested':tested,'level':level});(out/'SEARCH.json').write_bytes(encoded({'parameters':vars(a),'levels':rows,'best':list(best.values())}));print('LEVEL',depth,tested,len(level),flush=True)
  if not level or winner:break
 print('C282_INTEGER_VERTEX_BEAM_ENDED',tested,winner,[(k,v['V'],v['E_proposal']) for k,v in best.items()],flush=True)
if __name__=='__main__':main()
```

Run `OPENBLAS_NUM_THREADS=1 python vertexbeam282.py --out vertexbeam6`. Observed `C282_INTEGER_VERTEX_BEAM_ENDED 4871 False [((2,1),25,69)]`. Exact retained original49-point indices are [0,1,2,3,4,5,6,7,8,9,10,11,12,13,21,28,35,37,39,41,43,45,46,47,48]; these yield the complete standalone table above. The beam stopped after25 deletion depths with no survivor, not an exhaustive exclusion of all smaller subsets.

**Interpretation and next geometry.** Nearly all retained points lie near a common plane while the retained old input28 supplies a transverse apex. Thus this body may be close to a monounstable pyramid-type architecture; exact planar coalescence is a useful complexity/shape test, not yet an executed fact. Its remaining stable/saddle pair still requires genuinely altered transverse geometry. No proof forbids all such redesigns. The separate support-deletion C210 numerical descendant and two bounded affine searches have also been executed, but their complete method/endpoint preservation is still to be appended; they are not used as accepted parents yet.
