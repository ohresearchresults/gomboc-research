# figure-0419

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Quiet Raven 11 — two larger sparse stress families within the edge budget

Branch: `[internal-source-reference]`.

**New mathematical result:** there is a complete 11-dimensional fixed-z stress face whose uniformly filled, exactly centered members have **true E≤288**, and a complete 12-dimensional extension whose members have **true E≤305**. These bounds include all contact boundaries and all nonsingular affine images. The latter gives 12 physical shape parameters plus the five metric parameters, without exceeding the assignment’s edge budget.

**No new own110/weak000 body is established in this handoff.** Canonical C622 remains unchanged. The new result is a constructive family and an exact description of its full admissible parameter domain, not an equilibrium certificate. In particular, a bound such as C≤610 for a family member is not a record unless its actual own-mass equilibrium census is110/000.

## 1. Authority and execution status

The input authority is the supplied literal parent `figure-0414`, SHA-256 `6837898e4ebf09d5d8228ac8e1de77cc6eff6a2921842bd07360200d99148e00`. Its seven-file recovery capsule contains the exact constructor, integer auditor, stress classifier, and literal original input needed below. The original input is `farthest_merged_G10000.json`, **2051 bytes**, SHA-256 `89599e0825f7075c151639b70d9db5959fcdc058c0be555d1a96d8598ccdea3e`.

The numerical continuation attempted joint shape/metric optimization using true-edge physical and polar radial persistence, and a mixed-integer architecture search over the stress fractions. **Readable terminal census/parameter receipts for the fresh optimization attempts are not available in the restored execution context.** I therefore do not report those job launches as completed finite campaigns, do not assign a census to their unverified endpoints, and do not promote any resulting scratch object into a durable successor.

The family theorem below does not depend on those missing receipts. It is an algebraic consequence of the literal parent’s positive stress rays, their exact individual complexities, and the complete fixed-z complexity law. The new source extension is supplied in full. Its fresh execution is **not represented as a completed audit** in this handoff; the source prints the actual maximal counts and full midpoint censuses when replayed.

There is no missing geometric input for this result. Recovery requires the **literal supplied parent payload**, not an external archive, a Library lookup, or the originating sandbox.

## 2. The new support architecture

Keep the five bridge fields from the parent:

- Upper:1–14,2–14,28–47,47–52.
- Lower:1–4.

Replace the parent nine-mode family’s two upper five-edge fields by a larger collection of lower fields. Use these six normalized positive rays for the 11-dimensional family:

| Mode | Complete lower-cap support |
|---|---|
| Y3–12 | 0–3,3–6,3–12 |
| Y48–50 | 36–48,47–48,48–50 |
| Y3–28 | 0–3,3–6,3–28 |
| Y48–52 | 36–48,47–48,48–52 |
| Double Y3–48 | 0–3,3–6,3–48,47–48,48–50 |
| Double Y5–48 | 0–5,4–5,5–48,47–48,48–50 |

For the 12-dimensional extension, add the positive ray

`0–3,3–6,3–36`.

These are rays from the parent’s exhaustive support-at-most-six screen, not newly guessed supports. Each is reconstructed by the same exact gauge, nullspace, orientation, and maximum-fraction normalization as the parent.

The first family has **17 active original cap edges**: the five bridges and12 lower non-bridge edges. The extension has18. On both supports, the only interior cap nodes touched by a nonzero stress are **lower input nodes3,5,48**.

The long edge3–48 couples the two previously separate lower Y regions. The5–48 field adds another interior node and a different boundary-contact response near0,4. This is not an additional small upper hinge. It is also not a strict enlargement of the parent nine-mode family: the two upper five-edge fields are absent. It does extend the parent five-bridge/two-lower-Y family, up to the explicitly adjustable affine chord gauge.

## 3. Completeness: the admissible domain is larger than a simplex

Let R be the matrix whose columns are the normalized ray-fraction vectors, including the five bridge columns. The exact constructor below recovers R from the generated affine height fields and the original cap-edge curvature jumps.

A simple domain used to construct and verify the initial chart is

`[0,1]^5 × Δ6`

for the11-parameter family, or

`[0,1]^5 × Δ7`

for the12-parameter family. Here Δn means nonnegative coordinates with sum at most1. These domains are safe because the non-bridge rays are nonnegative and individually normalized to maximum fraction1.

However, the **complete natural domain** is

`0 ≤ R t ≤ 1`,

with **signed t allowed**. Restricting all t to be nonnegative would unnecessarily discard admissible fields.

The completeness proof is short and exact. On the17-edge support, there are six independent stress equations: two at each of nodes3,5,48. Their independence follows from the boundary-edge pairs

`{0–3,3–6}`, `{0–5,4–5}`, `{47–48,48–50}`.

Each pair supplies an invertible two-dimensional block because the corresponding three projected original points are noncollinear. Thus the supported stress space has dimension17−6=11. Adding3–36 adds one variable and no new interior-node equation, giving dimension18−6=12.

The listed columns are independent. In a linear relation, the unique edges3–28,48–52,3–48, and0–5 first force the coefficients of their respective added rays to vanish. The two original Y coefficients then vanish, followed by the five bridge coefficients. In the extension,3–36 first eliminates its added coefficient. Therefore these columns span the entire supported stress kernel.

The parent’s completeness theorem then gives an exact equivalence:

**Every convex fixed-z chord translation whose nonzero curvature transfers are confined to this support is represented by a unique t, modulo the already removed affine chord gauge, and is admissible exactly when0≤Rt≤1.**

The domain is a bounded rational polytope because R has full column rank. It has nonempty relative interior: take all bridge parameters1/2 and each of the six or seven lower parameters1/7 or1/8, respectively. Every active edge then has fraction strictly between0 and1.

## 4. Exact true-complex formulas and the edge-budget proof

For an original cap edge e, write

`c_e = 1 + 2 d_e`,

where d_e is the number of proper crossings of e with original interior edges of the opposite cap. This is a **topological cost**, not the original curvature weight in the stress equation.

When every active transfer fraction is strictly between0 and1, the parent’s complexity law simplifies to

`E = 153 + Σ_active c_e`.

The sum counts two crossing vertices when both crossing edges are active, exactly as required by the two physical skins. It is not a count of integration diagonals.

The five bridge costs sum to27. The following exact single-ray costs are inherited from the literal parent’s stress-screen data and are asserted again by the recovery program:

| Lower support | E of the single-ray open family | Sum of its edge costs |
|---|---:|---:|
| 0–3,3–6,3–12 | 164 | 11 |
| 0–3,3–6,3–28 | 164 | 11 |
| 0–3,3–6,3–36 | 172 | 19 |
| 36–48,47–48,48–50 | 172 | 19 |
| 36–48,47–48,48–52 | 170 | 17 |
| 0–3,3–6,3–48,47–48,48–50 | 186 | 33 |
| 0–5,4–5,5–48,47–48,48–50 | 198 | 45 |

Set

`u=c_(3,12)`, `v=c_(47,48)`, `w=c_(48,50)`.

The first two rows imply `c_(3,28)=u`. The two Y48 rows imply `c_(48,52)=w−2`. The double-Y rows eliminate the costs of the long connecting fields. Summing each distinct active edge only once gives the **exact open-complex edge counts**

`E17 = 275 + 2u − 2v − w`,

`E18 = 283 + 3u − 2v − w`.

Every edge cost is a positive odd integer. In particular,

`u≤9`, `v≥1`, `w≥3`.

Consequently,

**E17≤288 and E18≤305.**

There are precisely three mixed interior nodes in the open chart. The exact remaining counts are therefore

`V17=(E17−58)/2`, `F17=(E17+62)/2`,

`V18=(E18−59)/2`, `F18=(E18+63)/2`.

Thus the numerical upper bounds are

| Complete support face | Dimension | True V upper bound | True E upper bound | True F upper bound |
|---|---:|---:|---:|---:|
|17 active original edges |11 |115 |288 |175 |
|18 active original edges |12 |123 |305 |184 |

**These are bounds, not an invented execution receipt for the actual integer counts.** The exact counts are the formulas above; the supplied verifier evaluates u,v,w directly from the literal original coordinates and checks its constructed maximal complex against those formulas.

The same bounds hold on the entire closed natural-capacity polytope. At a boundary, an active fraction can become0 or1, removing one of its two skin creases and possibly associated crossings or mixed-node lifts. No new crease appears outside the fixed support. Therefore the actual maximal V/E/F cannot exceed the open values. A nonsingular affine map preserves this maximal complex.

## 5. Actual uniform mass and the metric freedom

For every admissible field β, the body is

`g(x,y)+β(x,y) ≤ z ≤ f(x,y)+β(x,y)`.

Each fibre is translated without changing its length. The map is a volume-preserving piecewise-affine bijection of the filled body. The physical volume is exactly

`1690203202641 / 1000000000000`.

The horizontal first moments remain unchanged. The vertical first-moment change is exactly

`∫_D (f−g) β`.

Subtracting this quantity divided by the volume gives the actual filled centroid, not a chosen equilibrium reference center. The constructor verifies the entire volume and first-moment polynomial, including cross terms, before using the chart.

Before final translation to0, its constant centroid is the original C306 centroid

`(409355912737/135216256211280000, 855529297349/67608128105640000, 5154137003/270432512422560)`.

The dyadic gauge uses denominator2^20 only for the two longitudinal affine shear coefficients of each mode. It does not round vertices independently.

After exact centering, the full determinant-one rational metric family can be represented by row-vector multiplication with

`L = [[a,0,0],[c,b,0],[d,e,1/(a*b)]]`,

where `a,b>0` and all five parameters are rational. The filled centroid stays0 and the physical volume is unchanged. Thus the12-dimensional stress face supplies a17-parameter shape/metric search space, still with true E≤305.

No assertion is made that the equilibrium census is constant on either stress face. Root turnover, saddle cancellation, weak contacts, and changes of the maximal complex must be audited at the actual chosen parameter values.

## 6. A global architecture formulation beyond this support face

The complete fixed-z edge-budget condition can be represented exactly by mixed-integer linear constraints; no positive epsilon is needed in this representation.

For each original interior cap edge, introduce its fraction λ_e and binary flags p_e,n_e satisfying

`0≤λ_e≤1`, `λ_e≤p_e`, `1−λ_e≤n_e`.

For each upper/lower crossing e,f, introduce binary x_ef,y_ef with

`x_ef≥n_e+p_f−1`, `y_ef≥p_e+n_f−1`.

Together with the exact stress equations Aλ=0, impose

`Σ_e(p_e+n_e−1) + 2Σ_crossings(x_ef+y_ef) ≤157`.

This is an exact existential description of the full E≤310 set. For a physical λ, choose its true activity flags and crossing indicators to recover its exact complexity. Conversely, any feasible flags can only overcount the true fractional edges and crossings, so they cannot admit a body whose actual E exceeds310. Flags that are unnecessarily1 at an endpoint merely waste budget.

This gives a way to select new contact architectures globally instead of restricting every search to a predetermined cube. A floating MILP incumbent is still only a scout: its active zero/one equations must be reconstructed rationally, and its actual maximal complex and mass must be audited. No global optimality or exclusion follows from a timed numerical solve.

## 7. What remains open, and a specific further extension

The inherited C328 control remains important: its own121/weak000 census and improved angular bottleneck did not remove the deep secondary radial basin. Nothing in the new dimensional or edge-budget statements changes that fact.

The new natural-capacity domain should be searched as `0≤Rt≤1`, allowing signed coefficients, jointly with the metric. The physically relevant objective remains the full physical peak-to-merge persistence, together with the complete same-center polar landscape. The safe simplex is only a convenient initial chart, not the whole admissible region.

There is also one especially inexpensive extension to test after reading the exact edge costs from the new family output. Add the parent’s other double-Y5 ray

`1–5,4–5,5–48,47–48,48–50`.

Only the original edge1–5 is new. It adds one parameter and no interior-node equation, producing a complete13-dimensional support face. The parent’s equal single-ray costs for the0–5 and1–5 alternatives imply

`c_(1,5)=c_(0,5)`.

Its open edge count is therefore exactly

`E19=E18+c_(0,5)`.

**It is a below-budget extension only when this evaluated number is≤310.** I do not assume that condition. The recovery output contains everything needed to decide it without another geometric search.

## 8. Complete new recovery source

This is an exact source extension to the **already supplied literal parent capsule**. Retain that parent payload with this handoff. It requires only its `fractional_y_exact.py`, `integer_census.py`, and literal `farthest_merged_G10000.json`; no optimizer output or scratch checkpoint defines either family.

Run the parent’s unchanged decoder, place the following file beside its decoded sources as `LOWER_FACE_EXACT.py`, and execute

    python -B -S LOWER_FACE_EXACT.py

The source uses standard-library rational arithmetic. The parent’s reported exact environment was CPython3.13.5. The program constructs both families, recovers the complete signed natural-capacity matrices, verifies their stress-space dimensions and exact maximal-complex formulas, and audits each explicitly defined interior midpoint with both the inherited integer auditor and a separate Fraction census. The integer audit also emits the complete physical and polar radial-basin/path/cut evidence.

Expected terminal marker **after a successful fresh replay**, not claimed as an observed receipt here:

    QR11_LOWER_FACE_SOURCE_AND_FULL_MIDPOINT_CENSUSES_PASS

The midpoint parameters are literal: bridge coordinates1/2; lower coordinates1/7 for the11-dimensional family and1/8 for the12-dimensional family; identity metric. Generated JSON files are supplemental evaluations of this source. Their byte counts and SHA-256 values are written to the receipt by the program rather than supplied here without a verified run.

```python
import json, pathlib, hashlib
from fractions import Fraction as Q
import fractional_y_exact as f
from integer_census import audit

ROOT=pathlib.Path(__file__).resolve().parent
INPUT_SHA='89599e0825f7075c151639b70d9db5959fcdc058c0be555d1a96d8598ccdea3e'
BRIDGES=[
 (0,[(1,14)]),(0,[(2,14)]),(0,[(28,47)]),
 (0,[(47,52)]),(1,[(1,4)])]
LOWER=[
 (1,[(0,3),(3,6),(3,12)]),
 (1,[(36,48),(47,48),(48,50)]),
 (1,[(0,3),(3,6),(3,28)]),
 (1,[(36,48),(47,48),(48,52)]),
 (1,[(0,3),(3,6),(3,48),(47,48),(48,50)]),
 (1,[(0,5),(4,5),(5,48),(47,48),(48,50)]),
 (1,[(0,3),(3,6),(3,36)])]


def caps(P,T):
 out=[]
 assert all(f.side(*(P[v]for v in t)) for t in T)
 for ci in (0,1):
  ts=[t for t in T
      if (f.side(*(P[v]for v in t))>0)==(ci==0)]
  edges={}
  for k,t in enumerate(ts):
   for a,b in zip(t,t[1:]+t[:1]):
    edges.setdefault(tuple(sorted((a,b))),[]).append(k)
  out.append((ts,{e:ij for e,ij in sorted(edges.items())
                  if len(ij)==2}))
 return out


def crosses(P,e,g):
 a,b=(P[i]for i in e);c,d=(P[i]for i in g)
 return (f.side(a,b,c)*f.side(a,b,d)<0 and
         f.side(c,d,a)*f.side(c,d,b)<0)


def fraction_matrix(P,cap,full,specs):
 points,B,cells=full;byxy={}
 for p,b in zip(points,B):
  if p[:2]in byxy:assert byxy[p[:2]]==b
  byxy[p[:2]]=b
 rows=[];labels=[]
 for ci,(ts,edges)in enumerate(cap):
  for e,(i,j)in edges.items():
   t=ts[i];v=next(v for v in ts[j]if v not in e)
   original=P[v][2]-f.val(f.plane(*(P[a]for a in t)),P[v])
   assert original
   row=[]
   for k,(mode_cap,support)in enumerate(specs):
    if mode_cap!=ci:
     row.append(Q(0));continue
    lifted=[(P[a][0],P[a][1],byxy[P[a][:2]][k])for a in t]
    jump=byxy[P[v][:2]][k]-f.val(f.plane(*lifted),P[v])
    row.append(-jump/original)
   rows.append(row);labels.append((ci,e))
 return rows,labels


def second_census(P,faces):
 normals=[];edges={};D=Q(0);M=[Q(0)]*3
 for fi,face in enumerate(faces):
  a,b,c=(P[i]for i in face[:3])
  n=f.cross(f.sub(b,a),f.sub(c,a));h=f.dot(n,a)
  assert h>0
  assert all(f.dot(n,P[v])==h for v in face)
  assert all(f.dot(n,p)<h for v,p in enumerate(P)if v not in face)
  normals.append(n)
  for i,j in zip(face,face[1:]+face[:1]):
   edges.setdefault(tuple(sorted((i,j))),[]).append(fi)
  for j in range(1,len(face)-1):
   b,c=P[face[j]],P[face[j+1]];d=f.det(a,b,c)
   assert d>0;D+=d
   for k in range(3):M[k]+=d*(a[k]+b[k]+c[k])
 assert D>0 and M==[0,0,0]
 assert all(len(v)==2 for v in edges.values())
 assert len(P)-len(edges)+len(faces)==2
 strict=[0,0,0];weak=[0,0,0]
 def add(k,tests):
  if all(v>0 for v in tests):strict[k]+=1
  elif all(v>=0 for v in tests):weak[k]+=1
 for face,n in zip(faces,normals):
  add(0,[-f.dot(f.cross(n,f.sub(P[j],P[i])),P[i])
         for i,j in zip(face,face[1:]+face[:1])])
 for i,p in enumerate(P):
  add(1,[-f.dot(p,f.sub(q,p))for j,q in enumerate(P)if j!=i])
 for (i,j),(a,b)in edges.items():
  p,q=P[i],P[j];d=f.sub(q,p);dd=f.dot(d,d);u=-f.dot(p,d)
  r=tuple(dd*p[k]+u*d[k]for k in range(3))
  n,m=normals[a],normals[b]
  nn,mm,nm=f.dot(n,n),f.dot(m,m),f.dot(n,m)
  assert nn*mm-nm*nm>0
  nr,mr=f.dot(n,r),f.dot(m,r)
  add(2,[u,dd-u,mm*nr-nm*mr,nn*mr-nm*nr])
 return dict(strict=strict,weak=weak,volume_grid=D/6,
             centroid_grid=[0,0,0])


def evaluate(out,full,R,parameters,matrix=None):
 t=list(map(Q,parameters));assert len(t)==len(R[0])
 lam=[sum(a*b for a,b in zip(row,t))for row in R]
 assert all(0<=v<=1 for v in lam)
 M=matrix if matrix is not None else [[1,0,0],[0,1,0],[0,0,1]]
 M=[[Q(v)for v in row]for row in M];assert f.det(*M)==1
 pp,unused,faces=f.maximal(*full,t=t)
 pp=[f.sub(p,out['centroid_grid'])for p in pp]
 pp=[tuple(sum(p[k]*M[k][j]for k in range(3))
           for j in range(3))for p in pp]
 rec=audit(pp,faces,grid=10000);other=second_census(pp,faces)
 assert list(rec['strict'])==other['strict']
 assert list(rec['weak'])==other['weak']
 assert Q(rec['volume_grid'])==other['volume_grid']==Q(1690203202641)
 assert list(rec['centroid_grid'])==[0,0,0]
 return pp,faces,rec,other


def run(include_third):
 raw=(ROOT/'farthest_merged_G10000.json').read_bytes()
 assert len(raw)==2051 and hashlib.sha256(raw).hexdigest()==INPUT_SHA
 z=json.loads(raw);P=[tuple(map(Q,p))for p in z['points']]
 T=z['T'];cap=caps(P,T)
 specs=BRIDGES+LOWER[:(7 if include_third else 6)];K=len(specs)
 out,full,unused=f.build(specs=specs,
                        simplex=tuple(range(5,K)),gauge_bits=20)
 R,labels=fraction_matrix(P,cap,full,specs)
 active={(ci,tuple(sorted(e)))for ci,support in specs for e in support}
 assert len(active)==(18 if include_third else 17)
 assert all(any(row)==(label in active)for row,label in zip(R,labels))
 assert not f.kernel(R,K)
 costs={}
 for ci,e in active:
  costs[(ci,e)]=1+2*sum(crosses(P,e,g)for g in cap[1-ci][1])
 def cost(ci,*es):
  return sum(costs[(ci,tuple(sorted(e)))]for e in es)
 assert sum(cost(ci,*es)for ci,es in BRIDGES)==27
 assert cost(1,(0,3),(3,6),(3,12))==11
 assert cost(1,(0,3),(3,6),(3,28))==11
 assert cost(1,(36,48),(47,48),(48,50))==19
 assert cost(1,(36,48),(47,48),(48,52))==17
 assert cost(1,(0,3),(3,6),(3,48),(47,48),(48,50))==33
 assert cost(1,(0,5),(4,5),(5,48),(47,48),(48,50))==45
 u=cost(1,(3,12));v=cost(1,(47,48));w=cost(1,(48,50))
 E=153+sum(costs.values())
 if include_third:
  assert cost(1,(3,36))==u+8
  assert E==283+3*u-2*v-w and E<=305
 else:
  assert E==275+2*u-2*v-w and E<=288
 I=len(active);X=(E-153-I)//2
 counts=[56+X,E,102+I-3+X]
 assert list(out['open_counts'])==counts
 A=[]
 for node in (3,5,48):
  for axis in (0,1):
   row=[]
   for ci,e in labels:
    if (ci,e)not in active or ci!=1 or node not in e:
     row.append(Q(0));continue
    ts,ed=cap[ci];i,j=ed[e]
    a=f.plane(*(P[k]for k in ts[i]))
    b=f.plane(*(P[k]for k in ts[j]))
    p,q=(P[k]for k in e)
    d=(q[0]-p[0],q[1]-p[1]);perp=(-d[1],d[0])
    rho=abs((a[0]-b[0])*perp[0]+(a[1]-b[1])*perp[1])/f.dot(d,d)
    other=e[1]if e[0]==node else e[0]
    row.append(rho*(P[other][axis]-P[node][axis]))
   A.append(row)
 assert all(sum(a*b for a,b in zip(row,col))==0
            for row in A for col in zip(*R))
 active_idx=[i for i,label in enumerate(labels)if label in active]
 AA=[[row[i]for i in active_idx]for row in A]
 assert len(f.kernel(AA,len(active_idx)))==K
 mid=[Q(1,2)]*5+[Q(1,K-4)]*(K-5)
 lam=[sum(a*b for a,b in zip(row,mid))for row in R]
 assert all(0<lam[i]<1 for i in active_idx)
 pp,faces,rec,other=evaluate(out,full,R,mid)
 name='LOWER18_DIM12'if include_third else'LOWER17_DIM11'
 out['natural_capacity']={
  'labels':labels,'matrix':R,
  'definition':'0 <= matrix @ t <= 1; t may be signed',
  'dimension':K}
 out['exact_open_complex']=counts
 out['edge_costs']=[(label,costs[label])for label in sorted(active)]
 f.save(name+'_FAMILY.json',out)
 f.save(name+'_MID_EXACT.json',dict(
  grid=10000,points=pp,faces=faces,parameters=mid,
  source_parent=INPUT_SHA))
 f.save(name+'_MID_AUDIT.json',rec)
 f.save(name+'_SECOND_CENSUS.json',other)
 print('QR11_NEW_LOWER_FACE_EXACT_PASS',name,counts,
       rec['strict'],rec['weak'],flush=True)
 return dict(name=name,dimension=K,open_counts=counts,
             strict=rec['strict'],weak=rec['weak'])


if __name__=='__main__':
 records=[run(False),run(True)];manifest={}
 paths=list(ROOT.glob('LOWER1[78]_*.json'))+[pathlib.Path(__file__)]
 for p in sorted(paths):
  b=p.read_bytes()
  manifest[p.name]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 f.save('LOWER_FACE_RECEIPT.json',dict(records=records,manifest=manifest))
 print('QR11_LOWER_FACE_SOURCE_AND_FULL_MIDPOINT_CENSUSES_PASS',flush=True)
```

## Acceptance boundary

The durable new result is the exact support architecture, its complete11- and12-dimensional natural-capacity domains, its true-complex formulas, its all-domain E≤288/E≤305 bounds, and its actual uniform-mass parameterization. The source provides deterministic midpoint definitions and full audit machinery, but **no fresh midpoint census or optimizer endpoint is accepted without a successful replay receipt**.

The useful next construction is a joint search on the full signed12-parameter capacity polytope and the five metric parameters, with exact rebuilding at saturated contacts. The additional1–5 field has a fully specified one-edge cost test for a possible13-dimensional continuation. Neither the old nine-mode failures nor the unavailable fresh numerical endpoints exclude these families.
