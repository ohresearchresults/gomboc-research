# material-9cd7e12952e1

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# TURNOVER_G4: exact exclusion of all one-, two-, and three-vertex deletions

## Claim, identity, and scope
For the 21 literal rational points embedded in both complete source units below, with physical coordinates equal to the integer rows divided by 10000, every convex hull formed by deleting exactly one, two, or three rows has at least two STRICT unstable equilibria at its own homogeneous volume centroid. There are 21+210+1330=1561 such hulls. Consequently none is an own strict class110 body, irrespective of its stable or weak equilibria. Every two- or three-row deletion actually has at least three strict unstable vertices. The unchanged parent has unique strict unstable input20 (zero-based), V21/E57/F38/C114. This is a finite, exact computational exclusion, NOT a general pruning theorem, a bound on all 21-vertex bodies, or a new own110 endpoint.

The input is the literal PARENT in the completely read immutable source [internal-source-reference], named C114_RETRACT20_exact_support_distance_gates.md, material SHA256 541f32aaa6cf7bd8b40292186959fc5335fbe6df677a17827a27b4900bc4c9bd. This capsule embeds the complete input and does not require that material, an old sandbox, any worker payload, or any third-party package for exact replay. The parent's compact JSON in that source is 413 bytes with SHA256 f25bc23f5a3195f5769859866978326cb2ab58123a615c6a8263811ea0845619. Source identity is by the literal rows, not a transferred label or incidence.

Exclusions do NOT cover deleting four or more rows exhaustively, moving any retained vertex, adding points, changing metric, changing density, or another parent. The exact census does not audit all stable and weak equilibria, because its two strict unstable witnesses already exclude the requested class. All retained counts are 18,19,20; no search below the stated lower bounds was performed. The accepted C622 body is unchanged.

## Exact method and executed results
All supporting planes are enumerated using integer triple predicates; coplanar triples are merged into maximal facets. An exact planar monotone-chain hull gives oriented facet cycles. Every retained point is checked to be a hull vertex, every directed edge has its unique reverse, each edge has two incident facets, and Euler's relation is checked. Outward boundary triangulation gives D=sum det(Pi,Pj,Pk)>0 and W=sum det(Pi,Pj,Pk)(Pi+Pj+Pk). Thus raw centroid is W/(4D), physical centroid W/(4D*10000), volume D/(6*10000^3). Three exact boundary-divergence volume identities and nine exact moment identities provide an alternative integration check of these values.

For each vertex i, Ti=4D Pi-W. Strict positivity of Ti dot (Pi-Pj) for EVERY other retained j proves that the direction from the actual centroid to Pi is in the interior of its normal cone. The generated report retains each case's centroid, volume, V/E/F, complete strict-U list, and positive minimum integer primitive for every unstable witness. All geometry and signs in this proof use Python integers, with no floating hull or epsilon.

Executed parent: volume numerator 5982118251795, volume denominator 6000000000000; raw centroid numerator [2407608875004924,-5371749770710239,12147149047639618], raw centroid denominator 23928473007180, physical centroid denominator 239284730071800000. Strict U=[20], minimum integer primitive 1200543029001491254452.

Exact histogram by deletion count, mapping strict-U count to number of bodies:
1: {2:13,6:1,7:1,9:1,11:1,12:1,14:1,16:1,17:1}.
2: {3:50,4:15,5:13,6:10,7:6,8:18,9:6,10:24,11:7,12:10,13:6,14:11,15:14,16:3,17:16,18:1}.
3: {3:8,4:103,5:101,6:106,7:73,8:100,9:184,10:91,11:132,12:63,13:83,14:107,15:68,16:94,17:16,18:1}.

## Exact reconstruction and verification
Save the first fenced source exactly with its final newline as exact_delete.py. It is 4663 bytes, SHA256 adb98e019284ca0b28b9c8d36c86db54918ab99cfaa75eec1a7dbd69b2984f49. Run `python -B -S exact_delete.py` in an empty writable directory. Execution used Python 3.13.5 (main, Jul 15 2026, 20:25:40), GCC14.2.0; no external dependencies. The complete generated file EXACT_DELETE_1_2_3.json is 870204 bytes, SHA256 96b1080caffd436aa70fdd72538006f858b3ff09d4c8887efb17112d2bdd81f8. There are no random parameters in exact replay. All 1561 cases, not selected examples, are regenerated.

Expected terminal output:
EXACT_DELETION_LAYER_PASS 1 {11: 1, 7: 1, 16: 1, 14: 1, 17: 1, 2: 13, 12: 1, 6: 1, 9: 1}
EXACT_DELETION_LAYER_PASS 2 {10: 24, 11: 7, 12: 10, 7: 6, 6: 10, 4: 15, 8: 18, 9: 6, 15: 14, 18: 1, 16: 3, 14: 11, 17: 16, 13: 6, 5: 13, 3: 50}
EXACT_DELETION_LAYER_PASS 3 {7: 73, 9: 184, 10: 91, 11: 132, 12: 63, 8: 100, 13: 83, 6: 106, 5: 101, 4: 103, 16: 94, 14: 107, 15: 68, 17: 16, 18: 1, 3: 8}
TURNOVER_G4_ALL_1561_DELETIONS_U_AT_LEAST_TWO_PASS 870204 96b1080caffd436aa70fdd72538006f858b3ff09d4c8887efb17112d2bdd81f8

Verification command after replay: `python -c "from pathlib import Path;import hashlib,json;p=Path('EXACT_DELETE_1_2_3.json');b=p.read_bytes();assert len(b)==870204 and hashlib.sha256(b).hexdigest()=='96b1080caffd436aa70fdd72538006f858b3ff09d4c8887efb17112d2bdd81f8';d=json.loads(b);assert len(d['cases'])==1561 and all(len(c['strict_U'])>=2 for c in d['cases']);print('EXACT_DELETE_RECOVERY_PASS')"`.

```python
"""Exact finite deletion exclusion for literal TURNOVER_G4 (21 grid vertices).
No floating hull, external files, or third-party dependencies.
Run: python -B -S exact_delete.py
Covers every deletion of one, two, or three of the 21 specified vertices only.
"""
import itertools,math,json,hashlib,sys
from pathlib import Path
P=[[-4900,9375,-4701],[6421,-82,-5296],[8443,2535,-3041],[9412,3109,-333],[10072,1807,1751],[10477,-562,2414],[10351,-2920,2709],[9618,-4801,3839],[8474,-6312,5048],[7021,-7226,6513],[5205,-7986,7728],[3072,-8650,8530],[723,-9005,9035],[-1739,-9104,9120],[-4279,-8878,8818],[-6795,-8218,8188],[-9218,-7095,7194],[-11421,-5456,5840],[-13241,-3217,4121],[-14541,-218,1839],[-14946,5442,-2355]]
GRID=10000
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def polygon(ids,n):
 drop=max(range(3),key=lambda k:abs(n[k]));a,b=[k for k in range(3) if k!=drop];ix=sorted(ids,key=lambda i:(P[i][a],P[i][b]))
 def turn(i,j,k):return (P[j][a]-P[i][a])*(P[k][b]-P[i][b])-(P[j][b]-P[i][b])*(P[k][a]-P[i][a])
 def half(seq):
  out=[]
  for i in seq:
   while len(out)>1 and turn(out[-2],out[-1],i)<=0:out.pop()
   out.append(i)
  return out
 cy=half(ix)[:-1]+half(ix[::-1])[:-1]
 if dot(cross(sub(P[cy[1]],P[cy[0]]),sub(P[cy[2]],P[cy[0]])),n)<0:cy.reverse()
 j=cy.index(min(cy));return cy[j:]+cy[:j]
def audit(keep):
 planes={}
 for i,j,k in itertools.combinations(keep,3):
  n=cross(sub(P[j],P[i]),sub(P[k],P[i]));h=dot(n,P[i])
  if n==(0,0,0):continue
  ss=[dot(n,P[z])-h for z in keep]
  lo,hi=min(ss),max(ss)
  if lo<0<hi or lo==hi==0:continue
  if hi>0:n=tuple(-v for v in n);h=-h;ss=[-v for v in ss]
  d=math.gcd(*n,h);key=tuple(v//d for v in n)+(h//d,);planes[key]=[i for i,s in zip(keep,ss) if s==0]
 faces=[polygon(planes[n],n[:3]) for n in sorted(planes)]
 assert set(i for cy in faces for i in cy)==set(keep)
 directed=set();ef={}
 for fi,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):
   assert (i,j) not in directed;directed.add((i,j));ef.setdefault(tuple(sorted((i,j))),[]).append(fi)
 assert all((j,i) in directed for i,j in directed) and all(len(v)==2 for v in ef.values())
 assert len(keep)-len(ef)+len(faces)==2
 tri=[(cy[0],cy[k],cy[k+1]) for cy in faces for k in range(1,len(cy)-1)]
 ds=[det(P[i],P[j],P[k]) for i,j,k in tri];D=sum(ds);assert D>0
 W=[sum(d*(P[i][a]+P[j][a]+P[k][a]) for d,(i,j,k) in zip(ds,tri)) for a in range(3)]
 # Independent boundary-divergence checks of all three volumes and nine moments.
 for axis in range(3):
  bv=0;bm=[0]*3
  for i,j,k in tri:
   a,b,c=P[i],P[j],P[k];nn=cross(sub(b,a),sub(c,a));ss=[a[z]+b[z]+c[z] for z in range(3)]
   bv+=nn[axis]*ss[axis]
   for z in range(3):bm[z]+=nn[axis]*(ss[z]*ss[axis]+a[z]*a[axis]+b[z]*b[axis]+c[z]*c[axis])
  assert bv==D and all(bm[z]==W[z]*(1+(z==axis)) for z in range(3))
 # Ti/(4D) is the vertex centred at the true raw homogeneous centroid.
 # Ti dot (Pi-Pj)>0 for ALL other supplied vertices certifies strict unstable i.
 U=[];mins=[]
 for i in keep:
  Ti=tuple(4*D*P[i][a]-W[a] for a in range(3));m=min(dot(Ti,sub(P[i],P[j])) for j in keep if j!=i)
  if m>0:U.append(i);mins.append(m)
 return {'deleted':[i for i in range(21) if i not in keep],'V':len(keep),'E':len(ef),'F':len(faces),'raw_centroid_numerator':W,'raw_centroid_denominator':4*D,'physical_centroid_denominator':4*D*GRID,'volume_numerator':D,'volume_denominator':6*GRID**3,'strict_U':U,'strict_U_min_integer_primitives':mins}
def main():
 parent=audit(tuple(range(21)));assert parent['strict_U']==[20],parent
 cases=[];hist={1:{},2:{},3:{}}
 for k in (1,2,3):
  for deleted in itertools.combinations(range(21),k):
   keep=tuple(i for i in range(21) if i not in deleted);o=audit(keep);assert len(o['strict_U'])>=2,o;cases.append(o);n=len(o['strict_U']);hist[k][n]=hist[k].get(n,0)+1
  print('EXACT_DELETION_LAYER_PASS',k,hist[k],flush=True)
 assert len(cases)==1561
 data={'scope':'All 1561 proper subsets obtained by deleting 1,2,3 literal input rows. At their own homogeneous centroid every case has at least two strict unstable vertices. No metric changes, moved surviving vertices, additions, larger deletions, or global exclusion is covered.','input':{'grid':GRID,'points':P},'parent':parent,'histogram_by_deleted_count':hist,'cases':cases}
 b=(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n').encode();Path('EXACT_DELETE_1_2_3.json').write_bytes(b)
 print('TURNOVER_G4_ALL_1561_DELETIONS_U_AT_LEAST_TWO_PASS',len(b),hashlib.sha256(b).hexdigest(),flush=True)
if __name__=='__main__':main()
```

## Preserved numerical discovery method, distinct evidence tier
Before the exact census, a Float64 scout tested 3493 distinct subsets: unchanged parent; all one-, two-, and three-row deletions; all contiguous interval deletions retaining at least ten rows; and 2500 seeded random subset proposals with surviving sizes10..20, deduplicated. No errors or S1U1 candidates were recorded. Only the unchanged parent retained U1 in this finite scout. This is numerical discovery evidence ONLY for the additional sampled/interval subsets; exact coverage is strictly the 1561 cases above. The scout's stability tests and persistence scores have tolerances and are not a complete weak-equilibrium audit.

Save the next source as scout.py with final newline:4991bytes SHA256 23db9c74d24d04a844c597d8544c0113fac9166ee8f1199a327869b442351410. Run `OPENBLAS_NUM_THREADS=1 python scout.py --samples 2500 --seed 20260920`. Executed dependencies Python3.13.5, NumPy2.3.5, SciPy1.17.0. Expected terminal marker DELETE_SCOUT_FINITE_DONE3493 (with a space before3493), zero candidate_or_error_trace entries, histogram S2U1 count1. The unchanged parent's scout J is0.5048831862357483 and JP0 in THIS implementation, not a transferable canonical metric from another family or normalization. Original DELETE_SCOUT.json was130219bytes SHA256 fa2000a42d3ab034b4cc2b0a5f99e27a2d12f154a920bf6e34968687a28fb4ed; this identifies the original supplementary output only. Its seconds field varies by run, and floating numerics may vary across platforms; byte-identical regeneration is claimed only for EXACT_DELETE_1_2_3.json. The complete discovery source, exact input, seed, nondefault parameters and dependency versions are preserved here rather than relying on that supplementary file.

```python
"""Finite deterministic vertex-deletion scout. Float64 discovery, not proof.
Rebuilds the actual convex hull and homogeneous volume centroid at every sample.
Run: python scout.py --samples 2500 --seed 20260920
"""
import argparse,itertools,json,time,sys
from pathlib import Path
import numpy as np
import scipy
from scipy.spatial import ConvexHull
PARENT={'grid':10000,'points':[[-4900,9375,-4701],[6421,-82,-5296],[8443,2535,-3041],[9412,3109,-333],[10072,1807,1751],[10477,-562,2414],[10351,-2920,2709],[9618,-4801,3839],[8474,-6312,5048],[7021,-7226,6513],[5205,-7986,7728],[3072,-8650,8530],[723,-9005,9035],[-1739,-9104,9120],[-4279,-8878,8818],[-6795,-8218,8188],[-9218,-7095,7194],[-11421,-5456,5840],[-13241,-3217,4121],[-14541,-218,1839],[-14946,5442,-2355]]}
P=np.array(PARENT['points'],float)/PARENT['grid']
def geom(p):
 h=ConvexHull(p);s=h.simplices.copy();tri=p[s];n=np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]);flip=np.sum(n*h.equations[:,:3],axis=1)<0
 s[flip]=s[flip][:,[0,2,1]];tri=p[s];ds=np.einsum('ij,ij->i',tri[:,0],np.cross(tri[:,1],tri[:,2]));v=ds.sum()/6;c=np.sum(ds[:,None]*tri.sum(axis=1),axis=0)/(24*v)
 x=p-c;ns=h.equations[:,:3];hs=-h.equations[:,3]-ns@c;groups={}
 for i,eq in enumerate(h.equations):groups.setdefault(tuple(np.round(eq,10)),[]).append(i)
 fn=[];faces=[];ef={}
 for g in groups.values():
  n=ns[g[0]];support=hs[g[0]];vs=sorted(set(s[g].ravel()));cen=x[vs].mean(0);ab=np.eye(3)[np.argmin(np.abs(n))];u=np.cross(n,ab);u/=np.linalg.norm(u);w=np.cross(n,u)
  vs=[vs[i] for i in np.argsort(np.arctan2((x[vs]-cen)@w,(x[vs]-cen)@u))];fi=len(faces);faces.append(vs);fn.append(n/support)
  for a,b in zip(vs,vs[1:]+vs[:1]):ef.setdefault(tuple(sorted((a,b))),[]).append(fi)
 assert all(len(z)==2 for z in ef.values())
 return x,v,c,faces,np.array(list(ef)),np.array(fn),np.array(list(ef.values()))
def landscape(p,edges):
 r=np.einsum('ij,ij->i',p,p);a=p[edges[:,0]];e=p[edges[:,1]]-a;t=np.clip(-np.sum(a*e,axis=1)/np.sum(e*e,axis=1),0,1);z=a+t[:,None]*e;lev=np.sum(z*z,axis=1);par=list(range(len(p)));birth=list(range(len(p)));bars=[]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for j in sorted(range(len(edges)),key=lambda k:(-lev[k],k)):
  a,b=edges[j];u,z=root(a),root(b)
  if u==z:continue
  if (r[birth[u]],-birth[u])<(r[birth[z]],-birth[z]):u,z=z,u
  b0,d=r[birth[z]],lev[j]
  if b0-d>1e-12:bars.append((birth[z],birth[u],float(b0),float(d)))
  par[z]=u
 return bars
def metrics(p):
 x,v,c,faces,edges,q,qe=geom(p);dot=x@x.T;r=np.diag(dot);scores=r[:,None]-dot;np.fill_diagonal(scores,np.inf);umin=scores.min(1);u=np.where(umin>1e-10)[0].tolist();ss=[];smin=[]
 for fi,vs in enumerate(faces):
  n=q[fi];foot=n/np.dot(n,n);vals=[np.dot(np.cross(x[b]-x[a],foot-x[a]),n) for a,b in zip(vs,vs[1:]+vs[:1])];smin.append(min(vals))
  if min(vals)>1e-10:ss.append(fi)
 pb=landscape(x,edges);qb=landscape(q,qe);J=sum(1/np.sqrt(d)-1/np.sqrt(b) for _,__,b,d in qb)/v**(1/3);JP=sum((b-d) for _,__,b,d in pb)/v**(2/3)
 return {'V':len(p),'E':len(edges),'F':len(faces),'S':len(ss),'U':len(u),'Sfaces':[faces[i] for i in ss],'Uvertices':u,'J':float(J),'JP':float(JP),'volume':float(v),'centroid':c.tolist(),'pbars':pb,'qbars':qb,'min_abs_SU':float(min(np.min(np.abs(umin)),np.min(np.abs(smin))))}
def run(samples,seed):
 rng=np.random.default_rng(seed);seen=set();hist={};best={};trace=[];t0=time.time()
 def examine(ids,label):
  ids=tuple(sorted(ids))
  if len(ids)<10 or ids in seen:return
  seen.add(ids)
  try:m=metrics(P[list(ids)])
  except Exception as e:trace.append({'ids':ids,'label':label,'error':str(e)});return
  k=f"S{m['S']}U{m['U']}";hist[k]=hist.get(k,0)+1;z={'ids':list(ids),'label':label,**m};obj=m['J']+m['JP']
  if k not in best or obj<best[k]['J']+best[k]['JP']:best[k]=z
  if m['S']==1 and m['U']==1:trace.append(z);print('FLOAT110_CANDIDATE',json.dumps(z,default=int),flush=True)
 examine(range(21),'parent')
 for n in [1,2,3]:
  for drop in itertools.combinations(range(21),n):examine(set(range(21))-set(drop),'all-delete-'+str(n))
 for a in range(21):
  for b in range(a,21):examine(set(range(21))-set(range(a,b+1)),'delete-interval')
 for _ in range(samples):
  size=int(rng.integers(10,21));examine(rng.choice(21,size,replace=False),'random-subset')
 out={'seed':seed,'samples_requested':samples,'unique_evaluated':len(seen),'histogram':hist,'best_by_class':best,'candidate_or_error_trace':trace,'seconds':time.time()-t0,'versions':{'Python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__},'parent':PARENT};Path('DELETE_SCOUT.json').write_text(json.dumps(out,sort_keys=True,indent=2,default=int)+'\n');print('DELETE_SCOUT_FINITE_DONE',len(seen),hist,'seconds',out['seconds'],flush=True)
 for k,z in sorted(best.items()):print(k,'J',z['J'],'JP',z['JP'],'ids',z['ids'],flush=True)
 return out
if __name__=='__main__':
 pa=argparse.ArgumentParser();pa.add_argument('--samples',type=int,default=2500);pa.add_argument('--seed',type=int,default=20260920);a=pa.parse_args();run(a.samples,a.seed)
```
