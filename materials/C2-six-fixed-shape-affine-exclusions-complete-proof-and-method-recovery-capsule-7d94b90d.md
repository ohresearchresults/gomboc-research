# material-7d94b90d561a

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Six fixed C2 shapes: complete symmetry-preserving affine exclusion

## Scope and exact dependencies
This capsule proves that NONE of the six exact LEAD_C2_FINITE_FLOW bodies can become own-centred strict110 under any invertible affine transformation that preserves their half-turn as a Euclidean orthogonal symmetry. It does NOT exclude changing the physical vertices, adding/deleting carriers, arbitrary symmetry-breaking affine maps, or other C2 shapes. No target110 has been constructed.

Required exact parent recovery is the complete three-part capsule:
- [internal-source-reference]: exact_lead.py,11008bytes,SHA6b41211b97ddc5c026736d6a9e5670deb4739cd985fccab7dd40d681224d3923.
- [internal-source-reference]: recover_lead.py,9006bytes,SHA0cb0cd79115afb6adde8fbbdb2f08a3e03d6b56a7143b6947f2646d0086e77f8.
- [internal-source-reference]: metrics_lead.py,1992bytes,SHAa2d991bdda7e43b28948e60b85b69083f0b6d7bd896b871fb9cc6aa54137b4ac.
Save those three complete files together, run `python -B -S recover_lead.py OUT`, then `python -B -S OUT/REPLAY.py`. The resulting OUT/exact reports, including their actual filled-volume mass and maximal complex, are the exact inputs here. No historical numerical checkpoint is needed. Worker use of this theorem requires this material plus all three parent source materials, not a reference to their filenames alone.

Accepted input audit receipts, all reconstructed from those literal parent sources:
C2_CHAIN73_G5.audit.json145159bytes SHAab6144fd3501ee075df3df2926c1a4d9c358d5540154a17aa59524056e7137d9
C2_MASS_FREE75_G8_CONTROL.audit.json230060bytes SHAaad41adac2566705ce74d0007bfd26a6b8b46be83d5c5dcffe48ce3552b7f234
C2_PAIRDELETE71_G6.audit.json157844bytes SHAb6f6685cf5b368567670116fd94ea836afec623fe49b4f9a00cbbb4498182359
C2_S3_PROJECT73_G4_CONTROL.audit.json132962bytes SHAbd9cdb7d3bdaf9093cb49bf6b04b7bb3a5939422a582faae43d31ac2c5712cba
C2_S3_PROJECT73_G6.audit.json160639bytes SHA8745e40d8eee2b1ee0c0172fa939f4c56b4ecf8a13727fb0310e819499c54cc9
C2_S3_PROJECT73_G8.audit.json192624bytes SHA7a3337db25cdc6e73fdd99ea0aed1f201cf1bc204b4b0b7040f495771682903c

## Mathematical argument
Let R=diag(-1,1,-1). Under an invertible physical affine map B, the actual homogeneous centroid transforms by that same affine map. No independently moved mass centre is allowed. Its pulled-back Euclidean metric is M=B^T B. The half-turn remains an orthogonal symmetry exactly when R^T M R=M. After positive overall metric scaling, every such metric has M=[[a,0,b],[0,1,0],[b,0,c]], with transverse block A=[[a,b],[b,c]] positive definite.

For these six exact parent shapes the unique highest axial vertex is T=(0,t,0),t>0; every other vertex has y<t. Therefore T is strictU for every such M: T^T M(v-T)=t(y-t)<0. The bottom rectangle remains an unavoidable strictS: its physical foot is the interior axial point of that rectangle, because the metric has no axial/transverse cross terms. Thus a hypothetical S1/U1 body must have precisely the top as U and base as S.

Every maximum-radius vertex of a finite convex polyhedron centred at an interior point is strictU. Indeed for a distinct vertex y of norm<=|x|, Cauchy-Schwarz gives x.(y-x)<0; equality would force y=x. Hence a unique U must be the unique maximum-radius vertex. Applied to the polar at the SAME physical centre, a unique S must likewise correspond to its unique maximum-radius polar vertex. Let the base polar vertex be (0,-B,0),B>0. For every other physical v=(w,y) and polar q=(z,eta), necessary strict inequalities are
w^T A w < t^2-y^2,
z^T A^-1 z < B^2-eta^2.
All denominators on the right are strictly positive for the six exact reports. Metric Cauchy-Schwarz then forces
(w.z)^2 < (t^2-y^2)(B^2-eta^2).
A single violating pair excludes the entire symmetry-preserving affine family, not merely a sampled metric. Exact affine_pair.py finds violations for five bodies. Maximal-ratio witnesses in each report's own exact ordering:
CHAIN73_G5:960violating pairs,vertex29/facet16,ratio~5.233681698802294.
PAIRDELETE71_G6:840pairs,vertex29/facet16,ratio~4.927391174467205.
S3_PROJECT73_G4_CONTROL:1268pairs,vertex23/facet15,ratio~5.992403906714801.
S3_PROJECT73_G6:1264pairs,vertex23/facet15,ratio~6.005089977361204.
S3_PROJECT73_G8:1264pairs,vertex23/facet15,ratio~6.005245442116119.
MASS_FREE75_G8_CONTROL has zero violating pairs; its maximum ratio~.8464351109864132 at9/44 is explicitly NOT an exclusion by this pair test.

For MASS, an exact finite disjunctive linear cover supplies the remaining exclusion. Put the closed physical inequalities w^T A w<=t^2-y^2 into a linear system in a,b,c. For every primitive integer transverse direction u with |u|_infinity<=8, identifying u and -u, polar necessity and metric Cauchy-Schwarz imply
u^T A u >= max_q (u.z_q)^2/(B^2-eta_q^2).
There are74physical and88direction inequalities,162root rows. These are NECESSARY inequalities. Positive definiteness is not imposed in the linear cover, so the covered set is a relaxation, not an erroneously narrowed metric family.

Every non-top physical vertex i must avoid being another strictU. Therefore at least one of its ACTUAL incident true edges ij must satisfy x_i^T M(x_j-x_i)>=0. Each alternative is linear in a,b,c, including the fixed axial term. At a branch node the verifier includes ALL true incident neighbours, with no omitted sign chamber. Its finite tree has45nodes,8internal branching nodes and37leaves. Each leaf provides nonnegative rational Farkas weights with sum lambda*C=0 and sum lambda*b<0. Exact arithmetic proves its allowed path system inconsistent. Induction over the complete neighbour cover excludes every point of the closed root relaxation that can avoid additional strictU. Consequently no symmetry-preserving SPD metric can give S1/U1 for this MASS body either. The conclusion does not depend on a floating LP status: the search nominates row sets, the stored literal tree reconstructs and checks every rational contradiction.

## Numerical control, not an equilibrium certificate
The complete affine_order.py below performs four stated SLSQP starts on the necessary global top/base radius-order constraints. On MASS it found a positive normalized ordering margin~.059493458601307725 at (a,b,c)~(1.2728889239190533,.08401587146587872,1.6990956938742128), but the numerical census is S7/U37. This illustrates that correct global root ordering is not sufficient for cancellation. It is a finite numerical control, NOT an accepted rational construction or an independent proof of infeasibility. The exact cover is stronger and independent of that optimization's success flag.

## Recovery and source integrity
Save the FOUR complete code blocks below under their headings. Exact checks use Python3.13.5 standard library only. Optional search/control uses NumPy2.3.5/SciPy1.17.0, binary64, OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. These are observed environment versions, not claims about current package recommendations.

From a directory containing the four sources and the reconstructed exact/ directory:
`python -B -S recover_affine_proof.py exact/C2_MASS_FREE75_G8_CONTROL.audit.json affine_mass_cover.json`
`python -B -S affine_cover.py verify exact/C2_MASS_FREE75_G8_CONTROL.audit.json affine_mass_cover.json`
`python -B -S affine_pair.py exact affine_pair_report.json`
Optional numerical control:
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python affine_order.py exact/C2_MASS_FREE75_G8_CONTROL.audit.json affine_order_mass.json`
Optional proof-search replay (not needed to reconstruct the exact proof):
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python affine_cover.py search exact/C2_MASS_FREE75_G8_CONTROL.audit.json newly_searched_cover.json`
A newly searched proof may have a different tree under another numerical implementation; only its exact successful verification would establish its validity.

Observed cold reconstruction in a separate source-only directory reproduced:
C2_AFFINE_ALL_SYMMETRY_PRESERVING_METRICS_EXCLUDED_EXACTLY C2_MASS_FREE75_G8_CONTROL45 37
C2_EXACT_AFFINE_PROOF_LITERAL_TREE_RECOVERY_PASS58458 ed5b9d0c95caa19aa902cfd4032d1ff85d327e33d36e1d1c46f1b0c96f4f6397
C2_FIVE_FULL_SYMMETRY_PRESERVING_AFFINE_FAMILIES_PAIR_EXCLUDED6739 dcf9a5117902c8147118dd4da81d0aa816b71726adb8ed8c2c55f4ef7d452e90
C2_AFFINE_ORDER_FOUR_NUMERICAL_STARTS_FINISHED

Exact source receipts (UTF8,one final newline):
affine_cover.py6086bytes SHA6cacc1c64039675677bf87f29f8d760e3aab389ef25378733e4842c9e1c2f1bb
recover_affine_proof.py3329bytes SHAec46f3fae92aa01d73d8077ed130d032fd5f96dac889182a37713660e51179fc
affine_pair.py1885bytes SHA53a56ab98a615679ad9a36498d878a918b21beceabc5af8e9cce824ea769f217
affine_order.py2471bytes SHA343dac25168f8b005d757af2ec7626fc19704b2b5c8b65ec44c8cfbbe829d51e
Exact literal seed plus newline1611bytes SHAc2322a21481671577ba041c3cdc44f185a2032a7eb3c0b8cdf6e9e596e6d0efc
Reproduced affine_mass_cover.json58458bytes SHAed5b9d0c95caa19aa902cfd4032d1ff85d327e33d36e1d1c46f1b0c96f4f6397
Reproduced affine_pair_report.json6739bytes SHAdcf9a5117902c8147118dd4da81d0aa816b71726adb8ed8c2c55f4ef7d452e90
Numerical affine_order_mass.json6124bytes SHAd42db05e68f8a42ee2dfc43198b7bcab49af261d28abd1232003cc58ae27fc53

A transient compact context had inconsistent unstored source sizes/hashes, pair counts and proof-report hashes. The actual complete files were read, copied into a separate directory, and cold reconstruction and optional numerical replay repeated against the matching accepted parent report hashes above. THIS literal capsule and its reproduced receipts are authoritative. Earlier unstored variants such as a58635-byte proof or differing source hashes are not asserted byte-identical. The source correction does not change any of the six accepted parent geometries. Hash matching and transport are not independent mathematical verification; the equations and complete exact checks above are the scientific evidence.

## affine_cover.py
```python
"""C2 affine necessary-root-order LP cover: search and exact certificate check.
Search uses Python3.13.5/NumPy2.3.5/SciPy1.17.0. Verification uses only stdlib.
Input is a complete exact_lead.py report. No floating inequality is evidence.
Usage: python affine_cover.py search audit.json proof.json
       python -B -S affine_cover.py verify audit.json proof.json
"""
import json,sys,math,hashlib
from pathlib import Path
from fractions import Fraction as F

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def load(path):
 raw=Path(path).read_bytes();d=json.loads(raw);k=int(d['physical_coordinate_multiplier'])
 X=[tuple(F(v)/k for v in row) for row in d['physical_landscape']['nodes']]
 Q=[tuple(F(v)*k for v in row) for row in d['polar_landscape']['nodes']]
 t=max(range(len(X)),key=lambda i:X[i][1]);base=min(range(len(Q)),key=lambda i:Q[i][1]);T=X[t][1]**2;B=Q[base][1]**2
 assert X[t][0]==X[t][2]==Q[base][0]==Q[base][2]==0
 assert X[t][1]>0 and Q[base][1]<0
 C=[];b=[];ids=[]
 def insert(c,r,name):
  scale=max(*(abs(v) for v in c),abs(r));assert scale>0
  C.append(tuple(v/scale for v in c));b.append(r/scale);ids.append(name)
 for i,(x,y,z) in enumerate(X):
  if i!=t:insert((x*x,2*x*z,z*z),T-y*y,['V',i])
 for u in [(a,b) for a in range(-8,9) for b in range(-8,9) if math.gcd(a,b)==1 and (a>0 or (a==0 and b>0))]:
  options=[]
  for j,(x,y,z) in enumerate(Q):
   if j==base:continue
   den=B-y*y;assert den>0
   options.append(((u[0]*x+u[1]*z)**2/den,-j))
  lower,negj=max(options);a,z=u
  insert(tuple(F(v) for v in (-a*a,-2*a*z,-z*z)),-lower,['Q',-negj,*u])
 root_count=len(C);adj=[[] for _ in X];escape={}
 for i,j in d['edges']:adj[i].append(j);adj[j].append(i)
 for i,xx in enumerate(X):
  if i==t:continue
  for j in sorted(adj[i]):
   dd=tuple(y-x for x,y in zip(xx,X[j]));c=(-xx[0]*dd[0],-xx[0]*dd[2]-xx[2]*dd[0],-xx[2]*dd[2]);r=xx[1]*dd[1]
   escape[(i,j)]=len(C);insert(c,r,['escape',i,j])
 return dict(identity=d['identity'],audit_sha256=hashlib.sha256(raw).hexdigest(),X=X,Q=Q,top=t,base=base,C=C,b=b,ids=ids,root_count=root_count,adj=adj,escape=escape)

def solve_linear(A,y):
 a=[list(row)+[v] for row,v in zip(A,y)];n=len(y)
 for col in range(n):
  r=next(i for i in range(col,n) if a[i][col]);a[col],a[r]=a[r],a[col];v=a[col][col];a[col]=[x/v for x in a[col]]
  for i in range(n):
   if i!=col:
    v=a[i][col];a[i]=[x-v*z for x,z in zip(a[i],a[col])]
 return [a[i][-1] for i in range(n)]

def verify_leaf(D,leaf,allowed):
 rows=leaf['rows'];weights=list(map(F,leaf['weights']));assert len(rows)==len(weights) and all(r in allowed for r in rows)
 assert min(weights)>=0 and sum(weights)>0
 assert all(sum(w*D['C'][r][j] for r,w in zip(rows,weights))==0 for j in range(3))
 v=sum(w*D['b'][r] for r,w in zip(rows,weights));assert v<0;assert str(v)==leaf['negative_bound']

def search(D,path):
 import numpy as np
 from scipy.optimize import linprog
 C=np.array(D['C'],dtype=float);b=np.array(D['b'],dtype=float);X=np.array(D['X'],dtype=float);nodes=[];counter=[0]
 def farkas(rows):
  cs=C[rows];bs=b[rows];res=linprog(bs,A_eq=np.vstack((cs.T,np.ones(len(rows)))),b_eq=[0,0,0,1],bounds=(0,None),method='highs')
  assert res.success and res.fun<-1e-10,(res.message,res.fun)
  sel=np.flatnonzero(res.x>1e-9);assert len(sel)<=4;selected=[rows[k] for k in sel]
  # A basic Farkas ray has at most four nonzero terms; solve its exact independent equations.
  from itertools import combinations
  mat=[[D['C'][r][j] for r in selected] for j in range(3)]+[[F(1)]*len(selected)];rhs=[F(0),F(0),F(0),F(1)]
  for eq in combinations(range(4),len(selected)):
   try:w=solve_linear([mat[j] for j in eq],[rhs[j] for j in eq])
   except (StopIteration,ZeroDivisionError):continue
   if all(dot(row,w)==v for row,v in zip(mat,rhs)):break
  else:raise AssertionError('no exact null ray')
  leaf=dict(rows=selected,weights=list(map(str,w)),negative_bound=str(sum(v*D['b'][r] for r,v in zip(selected,w))))
  verify_leaf(D,leaf,set(rows));return leaf
 def visit(rows,guarded):
  counter[0]+=1;assert counter[0]<=20000,'finite node budget exceeded'
  res=linprog(np.zeros(3),A_ub=C[rows],b_ub=b[rows],bounds=[(None,None)]*3,method='highs')
  if res.status==2:
   leaf=farkas(rows);nodes.append(dict(leaf=leaf));return len(nodes)-1
  assert res.success,res.message
  a,beta,c=res.x;M=np.array([[a,0,beta],[0,1,0],[beta,0,c]])
  candidates=[]
  for i in range(len(X)):
   if i==D['top'] or i in guarded:continue
   mx=max(float(X[i]@M@(X[j]-X[i])) for j in D['adj'][i])
   if mx< -1e-10:candidates.append((mx/float(X[i]@X[i]),i))
  assert candidates,('closed escape cover found feasible point',res.x.tolist(),len(guarded))
  _,i=min(candidates);children=[]
  for j in sorted(D['adj'][i]):children.append([j,visit(rows+[D['escape'][(i,j)]],guarded|{i})])
  nodes.append(dict(vertex=i,children=children));return len(nodes)-1
 root=visit(list(range(D['root_count'])),set());proof=dict(identity=D['identity'],audit_sha256=D['audit_sha256'],root=root,nodes=nodes)
 raw=(json.dumps(proof,sort_keys=True,indent=2)+'\n').encode();Path(path).write_bytes(raw)
 print('C2_AFFINE_CLOSED_ESCAPE_COVER_SEARCH_FINISHED',counter[0],len(nodes),len(raw),hashlib.sha256(raw).hexdigest())
 verify(D,proof)

def verify(D,proof):
 assert proof['identity']==D['identity'] and proof['audit_sha256']==D['audit_sha256'];seen=set();leaves=0
 def visit(k,rows,guarded):
  nonlocal leaves
  assert k not in seen;seen.add(k);node=proof['nodes'][k]
  if 'leaf' in node:verify_leaf(D,node['leaf'],rows);leaves+=1;return
  i=node['vertex'];assert i!=D['top'] and i not in guarded
  assert [c[0] for c in node['children']]==sorted(D['adj'][i])
  for j,child in node['children']:visit(child,rows|{D['escape'][(i,j)]},guarded|{i})
 visit(proof['root'],set(range(D['root_count'])),set());assert len(seen)==len(proof['nodes'])
 print('C2_AFFINE_ALL_SYMMETRY_PRESERVING_METRICS_EXCLUDED_EXACTLY',D['identity'],len(seen),leaves)
if __name__=='__main__':
 mode,source,out=sys.argv[1:];D=load(source)
 if mode=='search':search(D,out)
 elif mode=='verify':verify(D,json.loads(Path(out).read_text()))
 else:raise ValueError(mode)
```

## recover_affine_proof.py
```python
"""Rebuild the complete rational Farkas cover from its literal row-index tree.
Python3.13.5 standard library; affine_cover.py and exact audited parent required.
Usage: python -B -S recover_affine_proof.py parent.audit.json proof.json
"""
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from affine_cover import load,solve_linear,dot,verify
SEED = '{"audit_sha256":"aad41adac2566705ce74d0007bfd26a6b8b46be83d5c5dcffe48ce3552b7f234","identity":"C2_MASS_FREE75_G8_CONTROL","nodes":[{"rows":[6,29,82,347]},{"rows":[6,27,82,348]},{"rows":[7,125,144,349]},{"rows":[8,125,156,350]},{"rows":[8,83,105,351]},{"rows":[8,155,218,352]},{"children":[[32,0],[33,1],[43,2],[44,3],[45,4],[70,5]],"vertex":34},{"rows":[23,78,162,219]},{"rows":[22,75,162,220]},{"rows":[27,81,112,221]},{"rows":[22,74,75,222]},{"children":[[8,6],[10,7],[11,8],[69,9],[72,10]],"vertex":9},{"rows":[25,112,163,347]},{"rows":[24,112,163,348]},{"rows":[8,83,163,349]},{"rows":[8,83,163,350]},{"rows":[8,83,163,351]},{"rows":[9,163,352,223]},{"rows":[12,119,352,224]},{"rows":[13,119,352,225]},{"rows":[103,113,352,226]},{"rows":[93,101,352,227]},{"children":[[9,17],[11,18],[12,19],[69,20],[70,21]],"vertex":10},{"children":[[32,12],[33,13],[43,14],[44,15],[45,16],[70,22]],"vertex":34},{"rows":[8,25,164,223]},{"rows":[14,74,110,224]},{"rows":[15,74,110,225]},{"rows":[30,103,113,226]},{"rows":[26,93,101,227]},{"children":[[9,24],[11,25],[12,26],[69,27],[70,28]],"vertex":10},{"rows":[6,29,82,347]},{"rows":[6,27,82,348]},{"rows":[6,7,165,349]},{"rows":[8,9,165,350]},{"rows":[9,127,165,351]},{"rows":[9,165,223,352]},{"children":[[32,30],[33,31],[43,32],[44,33],[45,34],[70,35]],"vertex":34},{"rows":[14,74,110,224]},{"rows":[15,74,110,225]},{"rows":[30,103,113,226]},{"rows":[26,93,101,227]},{"children":[[9,36],[11,37],[12,38],[69,39],[70,40]],"vertex":10},{"rows":[8,123,154,166]},{"rows":[10,152,160,167]},{"children":[[1,11],[49,23],[50,29],[51,41],[71,42],[74,43]],"vertex":0}],"root":44}'
assert len((SEED+'\n').encode())==1611
assert hashlib.sha256((SEED+'\n').encode()).hexdigest()=='c2322a21481671577ba041c3cdc44f185a2032a7eb3c0b8cdf6e9e596e6d0efc'
def main():
    D=load(sys.argv[1]);p=json.loads(SEED)
    assert p['audit_sha256']==D['audit_sha256']
    for node in p['nodes']:
        if 'rows' not in node:continue
        rows=node.pop('rows')
        mat=[[D['C'][r][j] for r in rows] for j in range(3)]+[[F(1)]*len(rows)]
        rhs=[F(0),F(0),F(0),F(1)]
        for eq in combinations(range(4),len(rows)):
            try:w=solve_linear([mat[j] for j in eq],[rhs[j] for j in eq])
            except (StopIteration,ZeroDivisionError):continue
            if all(dot(row,w)==v for row,v in zip(mat,rhs)):break
        else:raise AssertionError('no exact normalized null ray')
        node['leaf']=dict(rows=rows,weights=list(map(str,w)),negative_bound=str(sum(v*D['b'][r] for r,v in zip(rows,w))))
    raw=(json.dumps(p,sort_keys=True,indent=2)+'\n').encode()
    assert len(raw)==58458 and hashlib.sha256(raw).hexdigest()=='ed5b9d0c95caa19aa902cfd4032d1ff85d327e33d36e1d1c46f1b0c96f4f6397'
    Path(sys.argv[2]).write_bytes(raw);verify(D,p)
    print('C2_EXACT_AFFINE_PROOF_LITERAL_TREE_RECOVERY_PASS',len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```

## affine_pair.py
```python
"""Exact necessary-pair obstruction to every C2-preserving affine metric.
Uses only Python3.13.5 standard library and complete exact_lead.py reports.
No numeric bound, solver or unrecorded input is used.
Usage: python -B -S affine_pair.py exact_directory pair_report.json
"""
import json,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
from affine_cover import load

def main():
 out={}
 for p in sorted(Path(sys.argv[1]).glob('*.audit.json')):
  raw=p.read_bytes();d=json.loads(raw);X=[tuple(F(v) for v in row) for row in d['physical_landscape']['nodes']];Q=[tuple(F(v) for v in row) for row in d['polar_landscape']['nodes']]
  top=max(range(len(X)),key=lambda i:X[i][1]);base=min(range(len(Q)),key=lambda i:Q[i][1]);T=X[top][1]**2;B=Q[base][1]**2
  assert X[top][0]==X[top][2]==Q[base][0]==Q[base][2]==0
  rows=[];violations=0;best=None
  for i,x in enumerate(X):
   if i==top:continue
   a=T-x[1]**2;assert a>0
   for j,q in enumerate(Q):
    if j==base:continue
    b=B-q[1]**2;assert b>0
    lhs=(x[0]*q[0]+x[2]*q[2])**2;rhs=a*b;ratio=lhs/rhs
    if ratio>=1:violations+=1
    if best is None or ratio>best[0]:best=(ratio,i,j,lhs,rhs)
  ratio,i,j,lhs,rhs=best
  out[d['identity']]=dict(audit_sha256=hashlib.sha256(raw).hexdigest(),top=top,base=base,violating_pairs=violations,max_ratio=str(ratio),witness_vertex=i,witness_facet=j,lhs=str(lhs),rhs=str(rhs),difference=str(lhs-rhs),excluded_by_pair=lhs>=rhs)
  print(d['identity'],'pairs',violations,'witness',i,j,'ratio',float(ratio),'EXCLUDED' if lhs>=rhs else 'PAIR_TEST_NOT_EXCLUSION')
 assert len(out)==6 and sum(d['excluded_by_pair'] for d in out.values())==5
 raw=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode();Path(sys.argv[2]).write_bytes(raw)
 print('C2_FIVE_FULL_SYMMETRY_PRESERVING_AFFINE_FAMILIES_PAIR_EXCLUDED',len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```

## affine_order.py
```python
"""Numerical C2-preserving affine root-order feasibility nomination only.
Python3.13.5, NumPy2.3.5, SciPy1.17.0. Reconstruct the exact audit first.
Usage: python affine_order.py audit.json output.json
"""
import sys,json
import numpy as np
from pathlib import Path
from fractions import Fraction as F
from scipy.optimize import minimize

def load(p):
 d=json.loads(Path(p).read_text());k=int(d['physical_coordinate_multiplier'])
 X=np.array([[float(F(v)/k) for v in row] for row in d['physical_landscape']['nodes']])
 Q=np.array([[float(F(v)*k) for v in row] for row in d['polar_landscape']['nodes']])
 t=int(np.argmax(X[:,1]));base=int(np.argmin(Q[:,1]));return d,X,Q,t,base

def metric(w):return np.array([[w[0],w[1]],[w[1],w[2]]])
def constraints(w,X,Q,t,base):
 A=metric(w);det=np.linalg.det(A)
 if det<=0:inv=np.linalg.pinv(A)
 else:inv=np.linalg.inv(A)
 R=X[:,[0,2]];Z=Q[:,[0,2]]
 pr=1-(np.einsum('ij,ij->i',R@A,R)+X[:,1]**2)/X[t,1]**2
 qr=1-(np.einsum('ij,ij->i',Z@inv,Z)+Q[:,1]**2)/Q[base,1]**2
 return np.r_[np.delete(pr,t)-w[3],np.delete(qr,base)-w[3],w[0]-.00001,w[2]-.00001,det-.00001]
def census(w,d,X,Q,t,base):
 A=metric(w);M=np.array([[w[0],0,w[1]],[0,1,0],[w[1],0,w[2]]]);N=np.linalg.inv(M)
 pe=np.einsum('ij,kj->ik',X@M,X)-np.einsum('ij,ij->i',X@M,X)[:,None]
 qe=np.einsum('ij,kj->ik',Q@N,Q)-np.einsum('ij,ij->i',Q@N,Q)[:,None]
 np.fill_diagonal(pe,-1e99);np.fill_diagonal(qe,-1e99)
 return dict(metric=M.tolist(),U=np.flatnonzero(pe.max(1)<0).tolist(),S=np.flatnonzero(qe.max(1)<0).tolist(),top=t,base=base,root_order_margin=float(constraints(np.r_[w[:3],0.],X,Q,t,base).min()))
def main():
 d,X,Q,t,base=load(sys.argv[1]);hist=[];best=None
 for initial in ([1.,0.,1.,-.4],[2.,0.,2.,-.4],[1.,.4,1.,-.4],[1.,-.4,1.,-.4]):
  r=minimize(lambda w:-w[3],initial,method='SLSQP',bounds=[(.00001,1000),(-1000,1000),(.00001,1000),(-100,1)],constraints={'type':'ineq','fun':lambda w:constraints(w,X,Q,t,base)},options={'maxiter':1000,'ftol':1e-13})
  row=dict(success=bool(r.success),message=r.message,iterations=r.nit,parameters=r.x.tolist(),minimum_constraint=float(constraints(r.x,X,Q,t,base).min()),**census(r.x,d,X,Q,t,base))
  hist.append(row);print(row,flush=True)
  if best is None or row['root_order_margin']>best['root_order_margin']:best=row
 Path(sys.argv[2]).write_text(json.dumps(dict(identity=d['identity'],runs=hist,best=best),sort_keys=True,indent=2)+'\n')
 print('C2_AFFINE_ORDER_FOUR_NUMERICAL_STARTS_FINISHED')
if __name__=='__main__':main()
```
