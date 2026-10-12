# figure-0518

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# RESERVE31 whole-Q15 continuation: retained findings, verification boundary, and exact recovery patch

## Result status

**No own-centroid strict110 construction is claimed.** The retained working record contains a consequential result on the assigned RESERVE31 geometry: an exact obstruction for its **entire unbounded Q15 one-point visibility cell**, using actual filled-volume moments and a protected set of possible old unstable vertices rather than one fixed old root. It also records several genuinely changed numerical and rational endpoints.

There is an important execution limitation. In the currently available resumed context, subsequent container, Python, and image-tool return payloads were not readable; they appeared as skipped messages. Consequently, I cannot confirm the contents of the latest generated archives, the later proposed modifications, or a final aggregate cold-replay marker. I do **not** count those later attempts as completed computations. This is an evidence-access limitation, not a negative geometric experiment and not a missing-input allegation against the supplied pack.

This handoff therefore separates three things:

1. The exact parent, whose complete literal recovery remains authoritative and available.
2. Results recorded in the retained execution summary, with their scope and provisional recovery status stated below.
3. A **complete new source-level recovery and verification patch** for an explicitly defined changed point body and the whole-Q15 cell calculation. This consolidated patch is not represented as having an observed successful run in the resumed context.

The additional frozen deformations whose integer arrays are not visible here are **not promoted as durable successors**. Their filenames and recorded receipts are identification aids, not substitutes for their coordinates.

## Authoritative parent

The required parent is `figure-0512`, SHA-256 `86003740903626b3e1cd767af400b37ddb53d9b8da28dd88eeedbe56ff374cde`.

Its standalone `RECOVER_C50_RELEASE_EXACT.py` is 58240 bytes, SHA-256 `97c31b8950406aef6b03464f2a0daa80a21a7f5d9c85cd5de68358b458ddb48a`. The decoded 33-unit dictionary is 178649 bytes, SHA-256 `c941398b256df8adae1848b23d6764441d35528e013c187744863add108e4683`. That literal capsule, already supplied in this conversation, is the only external source dependency of the patch below.

The geometry is exactly **H23_CAP_RESERVE31_G5**, not RECON31 or its Q16 insertion:

```text
V/E/F/C = 31/87/58/174
strict S/U/H = 2/1/1
additional weak = 0/0/0
primitive zero = 0/0/0
S = [28,52]
U = [30]
H = [[25,30]]
P positive bars = []
```

Its stable triangles are `[9,29,27]` and `[22,28,26]`, disjoint and avoiding U30. The complete unwanted polar component is

```text
X = [12,13,15,30,35,36,37,44,46,49,50,51,52,53,54]
```

with peak52, elder28, fifteen cut edges, and the attaining path

```text
[52,53,54,51,55,56,57,28].
```

The exact raw volume is `2506418358615227/2000000000000000`. Its actual raw centroid is

```text
(118131494510284423633/1503851015169136200000,
 159566757909381027703/3007702030338272400000,
 48634154436966925429/300770203033827240000).
```

The retained record reports a fresh match of the parent input, full audit, and full radial report:

| File | Bytes | SHA-256 |
|---|---:|---|
| H23_CAP_RESERVE31_G5_INPUT.json | 1339 | 4b1bed14b6174e65850f72f54a597e0dc284c3cf65fa3962d75a27c796017d5f |
| H23_CAP_RESERVE31_G5_AUDIT.json | 298254 | 90cac819511f140ccee447022f3f3e20d43c4a5244e128597559a7f939baed98 |
| H23_CAP_RESERVE31_G5_RADIAL.json | 54916 | 189f96ce705831655c659569f6e8aad5b6db8ad3deeb1fda7fafe1cc98d66245 |

These checks concern this one exact parent, not another replay of all 75 receipts in the preceding result.

## 1. The consequential whole-cell calculation

Let P be the raw uniformly filled parent. Write its maximal supporting planes as

`n_f dot x <= h_f`,

using the canonical face numbering reconstructed by the parent auditor. Consider **every real point p** satisfying

```text
n_f dot p > h_f  for all f in X,
n_f dot p < h_f  for all f outside X.
```

This is the exact fifteen-visible/forty-three-retained partition of RESERVE31. It is not the distinct RECON31 Q16 partition.

The retained execution summary reports the following conclusion:

> Throughout this entire unbounded strict visibility cell, the uniformly filled body conv(P union {p}) has at least two strict unstable equilibria at its actual centroid. The recorded computation also covered a full-dimensional entrywise Gram neighbourhood of the identity, reported as radius 1/128.

The mechanism is stronger than preservation of one named old maximum. The inserted point is strict U. Separately, a maximum-radius member of the fixed old set

`B = {2,7,9,12,16}`

is strict U because every outgoing edge from B to its complement has a strictly negative radius derivative. Internal edges are handled by the maximum-radius identity. Root exchange inside B is permitted.

The recorded certificate used homogeneous compactification of the **whole unbounded cell**, not a bounded point sample. The summary records eleven finite vertices and seven recession rays, a finite tetrahedral subdivision of a projective section, and exact coefficient tests after actual-mass denominator clearing. It records 31839 checked coefficient matrices for its particular subdivision and protected cut.

I cannot currently inspect the original coefficient bank or its terminal log. Accordingly, the stronger recorded 1/128 statement is **not treated here as a newly cold-verified theorem**. The complete patch below reconstructs the same mathematical test with a conservative explicit radius **1/256**. Its completion is an exact, independently inspectable acceptance condition; its failure to complete would not be an exclusion proof.

### Exact actual-mass formula

The full visibility partition fixes the visible triangular facets. For each visible oriented triangle `(a,b,c)`, put

```text
n = (b-a) cross (c-a)
h = n dot a
s = a+b+c.
```

The added pyramid has

```text
delta V = (n dot p-h)/6,
delta M = delta V*(p+s)/4.
```

Consequently, throughout the entire cell,

```text
V(p) = v0 + A dot p,
M(p) = m0 + L p + p*(A dot p)/4,
g(p) = M(p)/V(p),
```

where the complete rational coefficients are obtained from the parent by

```text
A  = sum_visible n/6,
v0 = V_parent - sum_visible h/6,
m0 = M_parent - sum_visible h*s/24,
L  = sum_visible (s*n^T - h*I)/24.
```

This is a finite material formula, not a differential approximation and not a freely prescribed centre.

For homogeneous coordinates `z=(x,w)`, define

```text
Vh(z) = v0*w + A dot x,
Mh(z) = m0*w^2 + (Lx)*w + x*(A dot x)/4.
```

For finite points, `p=x/w` and `g=Mh/(w*Vh)`. After clearing positive denominators, an old directed edge `u -> v` has the quadratic numerator

`(w*Vh*u-Mh) dot (v-u)`,

and a new-point edge `p -> v` has the cubic numerator

`(Vh*x-Mh) dot (w*v-x)`.

Their symmetric matrix versions give the corresponding Gram-metric signs. A coefficient matrix C satisfying

`trace(C) + delta*sum_ij |C_ij| < 0`

is negative against every symmetric Gram matrix with `max_ij |G_ij-I_ij| <= delta`. With delta=1/256, such matrices are automatically positive definite.

### Why the protected-set argument is whole-basin evidence

Choose a maximum-G-radius vertex u in B at the actual centroid. For an internal edge to v in B,

`2*(u-g)^T G(v-u) = |v-g|_G^2-|u-g|_G^2-|v-u|_G^2 < 0`.

The certificate separately makes every boundary arrow of B negative. Thus u is strict U, regardless of which vertex of B maximizes the radius. The inserted point is another strict U. This avoids the invalid inference that removing one old root or changing one outgoing arrow eliminates a whole basin.

The scope remains narrow in the right way: fixed original material P, one inserted point, this exact strict visibility partition, and the certified metric window. It does not cover moved old vertices, material removal, multiple inserted points, another visibility partition, or arbitrary affine metrics.

## 2. A source-complete changed finite body

The exact point

`p10 = (10,-159/100,10)`

is the recorded strictly feasible representative of this RESERVE31 Q15 cell. Define

`K10 = conv(P union {p10})`.

This is a genuinely changed uniformly filled body. The retained execution record reports V31/E87/F58 and strict **5/2/5**, with additionalweak000. Old vertex22 becomes redundant; the inserted point replaces it in the extreme-vertex count. The inserted point and an old vertex in B are both unstable.

The patch below reconstructs K10 from the exact parent, reintegrates its volume and first moment, rebuilds all maximal facets and true edges, performs the full strict/additional-weak/mixed audit, and emits both complete simultaneous-level radial landscapes. It also verifies that the independently derived finite mass polynomial agrees exactly with that rebuilt mass.

No new numerical coordinate is needed to recover K10. Its exact first moment and centroid are the values of the displayed rational mass formula at p10, and are printed and stored by the verifier. I do not invent unreadable mass fractions or a new observed output hash for this consolidated replay.

## 3. Other recorded finite work and its present recovery limit

The retained summary records free-vertex whole-Q descent and reconsolidation from the literal parent, followed by physical-escape midpoint enrichment and actual-mass repair. It names the following endpoint families:

```text
RES31_WHOLEQ_RECON_G4/G5/G6
RES31_WHOLEQ_RECON2_G4/G5/G6
RES31_ENRICH_RECON_G4/G5/G6
Q15_LONG_APEX_U1_G4/G5
RES31_MIDPOINT_U1_G5
```

The recorded scientific tradeoffs are useful: a compact low-arithmetic detached-triangle continuation; a shallower compact continuation that reintroduces stable/unstable incidence coupling; an enriched, thicker continuation with a larger Q interface; and a thin introduced-apex U1 construction with a small but very deep polar interface. None was reported as110.

However, their complete integer input arrays are not visible in the resumed context. They therefore remain **ephemeral relative to this handoff**, not accepted reconstructible successors. In particular, the following recorded input receipts are not sufficient recovery data by themselves:

```text
RES31_WHOLEQ_RECON_G4_INPUT.json
833 bytes
SHA-256 d5c9cf4f7f4adf0e2c311b5205e33e3101a1fa2479c6f00fd80e21dcbcaf74cd

RES31_WHOLEQ_RECON2_G4_INPUT.json
834 bytes
SHA-256 f6f0d1629679608d8ac7a0da004c2059af49e68bf7b3009d019d89c6b3ec2b117

RES31_ENRICH_RECON_G4_INPUT.json
1426 bytes
SHA-256 e60f7a062fe8d61a8ad64edb242f4b9f005a89537bfb9e3a5259b7da81b2f9a4e

Q15_LONG_APEX_U1_G4_INPUT.json
1076 bytes
SHA-256 ce6e68d61215ce7f8c037cebaa40a6e202ad01e704cef449f938987f5378cbaea6
```

The exact missing dependencies for promoting those bodies are those literal arrays, or their original complete binary64 checkpoint arrays together with the recorded ties-to-even freezing rule. A successful future retrieval must verify the bytes rather than infer coordinates from these names or receipts.

## 4. Complete recovery and verification patch

Save the following as `Q15_SOURCE_RECHECK.py`. It requires only the exact parent decoder already supplied in the literal parent result. It does not depend on the inaccessible new sandbox files or numerical producers.

Run with **CPython3.13.5, standard library, assertions enabled**:

```sh
python -B -S Q15_SOURCE_RECHECK.py RECOVER_C50_RELEASE_EXACT.py Q15_RECHECK_OUT
```

All nondefault parameters are literal: p10, X, B, the Gram radius1/256, projective section functional `(1,0,1,10)`, longest-edge bisection, and maximum subdivision depth12.

Expected logical completion markers are:

```text
RESERVE31_LITERAL_PARENT_INPUT_AND_AUDIT_PASS
Q15_POINT10_FULL_ACTUAL_MASS_AND_LANDSCAPES_PASS
Q15_COMPLETE_UNBOUNDED_CELL_CERTIFIED_U_GE_TWO
```

**These markers are not asserted observed for this consolidated source.** Every generated file receives a byte count and SHA-256 at execution. The code aborts rather than interpreting a failed sign search as a theorem.

```python
"""Exact RESERVE31 Q15 point-cell recheck.
CPython3.13.5, standard library only, assertions enabled.
This is a complete patch against the literal asg_vsws parent decoder.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
from math import gcd, lcm
import hashlib, json, subprocess, sys, os

sys.set_int_max_str_digits(0)
if len(sys.argv) != 3:
    raise SystemExit('usage: Q15_SOURCE_RECHECK.py parent_decoder.py output_directory')
assert not sys.flags.optimize
source = Path(sys.argv[1]).resolve()
out = Path(sys.argv[2]).resolve()
raw = source.read_bytes()
assert len(raw) == 58240
assert hashlib.sha256(raw).hexdigest() == '97c31b8950406aef6b03464f2a0daa80a21a7f5d9c85cd5de68358b458ddb48a'
out.mkdir(parents=True, exist_ok=True)
subprocess.run([sys.executable, '-B', '-S', str(source), str(out)], check=True)
os.chdir(out)
sys.path.insert(0, str(out))
import exact_cap as e
from freeze_new import verify
from BATCH_RADIAL import landscape

NAME = 'H23_CAP_RESERVE31_G5'
X = {12,13,15,30,35,36,37,44,46,49,50,51,52,53,54}
BLOCK = {2,7,9,12,16}
P10 = (F(10), F(-159,100), F(10))
DELTA = F(1,256)
SECTION = (F(1), F(0), F(1), F(10))
MAX_DEPTH = 12
RECEIPTS = {}

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(a,t): return tuple(t*x for x in a)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def det3(a,b,c): return dot(a,cross(b,c))
def matvec(A,x): return tuple(dot(r,x) for r in A)
def sym(a,b):
    return tuple((a[i]*b[j]+b[i]*a[j])/2 for i in range(3) for j in range(3))
def matrix_sum(items):
    items=list(items)
    return tuple(sum(a[i] for a in items) for i in range(9))
def trace(A): return A[0]+A[4]+A[8]
def norm1(A): return sum(abs(x) for x in A)
def put(name,obj):
    e.write(name,obj)
    b=Path(name).read_bytes()
    result=[len(b),hashlib.sha256(b).hexdigest()]
    RECEIPTS[name]=result
    print('RECEIPT',name,*result,flush=True)
    return result

def rank(rows):
    A=[list(map(F,r)) for r in rows]
    r=0
    for j in range(len(A[0])):
        k=next((k for k in range(r,len(A)) if A[k][j]),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        q=A[r][j]
        A[r]=[x/q for x in A[r]]
        for k in range(len(A)):
            if k!=r and A[k][j]:
                q=A[k][j]
                A[k]=[x-q*y for x,y in zip(A[k],A[r])]
        r+=1
        if r==len(A): break
    return r

def integer_row(row):
    row=list(map(F,row));D=lcm(*(x.denominator for x in row))
    z=[int(x*D) for x in row]
    g=0
    for x in z: g=gcd(g,abs(x))
    assert g
    return tuple(x//g for x in z)

def kernel4(rows):
    return tuple((-1)**j*det3(*[tuple(row[k] for k in range(4) if k!=j) for row in rows]) for j in range(4))

def complete_radial(r,name):
    P=[tuple(map(F,p)) for p in r['centred']]
    Q=[tuple(F(x)/F(row[3]) for x in row[:3]) for row in r['own_H']]
    QE=sorted({tuple(sorted(z[2:])) for z in r['owners']})
    pp=landscape(P,r['edges']);qq=landscape(Q,QE)
    for a,b in [(pp['bars'],r['Pbars']),(qq['bars'],r['Qbars'])]:
        assert sorted((F(z['birth']),F(z['death'])) for z in a)==sorted((F(z['birth']),F(z['death'])) for z in b)
    assert len(pp['bars'])==r['strict'][1]-1
    assert len(qq['bars'])==r['strict'][0]-1
    return dict(name=name,actual_physical_centroid=r['raw_centroid'],P=pp,Q=qq)

# Parent recovery and exact identity control.
f=Path(NAME+'_INPUT.json')
if not f.exists():
    definitions=json.loads(Path('DEFINITIONS.json').read_text())
    e.write(str(f),definitions[NAME])
assert [f.stat().st_size,hashlib.sha256(f.read_bytes()).hexdigest()]==[1339,'4b1bed14b6174e65850f72f54a597e0dc284c3cf65fa3962d75a27c796017d5f']
d=json.loads(f.read_text());D=F(d.get('denominator',1))
original=[tuple(F(x)/D for x in p) for p in d['points']]
r=verify(e.extremes(original),NAME)
assert list(r['VEFC'])==[31,87,58,174]
assert list(r['strict'])==[2,1,1]
assert list(r['weak'])==[0,0,0] and list(r['primitive_zero'])==[0,0,0]
assert put(NAME+'_AUDIT.json',r)==[298254,'90cac819511f140ccee447022f3f3e20d43c4a5244e128597559a7f939baed98']
P=[tuple(map(F,p)) for p in r['vertices']]
assert set(r['Qbars'][0]['component'])==X
assert len(r['Qbars'])==1 and not r['Pbars']
print('RESERVE31_LITERAL_PARENT_INPUT_AND_AUDIT_PASS',flush=True)

# Simultaneous-level control for the separate radial implementation.
cube=[tuple(map(F,(x,y,z))) for x in [-1,1] for y in [-1,1] for z in [-1,1]]
ce=[(i,j) for i in range(8) for j in range(i+1,8) if sum(a!=b for a,b in zip(cube[i],cube[j]))==1]
cc=landscape(cube,ce)
assert len(cc['bars'])==7 and len(cc['simultaneous_edge_levels'])==1
assert all(z['birth']==3 and z['death']==2 and len(z['component'])==1 and len(z['boundary'])==3 for z in cc['bars'])

# Exact finite representative, with fresh uniform mass and all landscapes.
H=[tuple(map(F,row)) for row in r['raw_H']]
assert all((dot(row[:3],P10)-row[3])*(1 if i in X else -1)>0 for i,row in enumerate(H))
material=P+[P10]
newname='RES31_Q15_POINT10_RECHECK'
put(newname+'_INPUT.json',dict(parent=NAME,points=material))
rr=verify(e.extremes(material),newname)
assert list(rr['VEFC'])==[31,87,58,174]
assert list(rr['strict'])==[5,2,5]
assert list(rr['weak'])==[0,0,0] and list(rr['primitive_zero'])==[0,0,0]
put(newname+'_AUDIT.json',rr)
put(newname+'_RADIAL.json',complete_radial(rr,newname))

# Whole visibility-cell volume and first-moment coefficients.
Vparent=F(r['raw_volume']);Mparent=tuple(map(F,r['raw_first_moment']))
v0=Vparent;A=(F(0),)*3;m0=Mparent;L=[[F(0)]*3 for i in range(3)]
for f in sorted(X):
    cy=r['faces'][f];assert len(cy)==3
    a,b,c=[P[i] for i in cy]
    n=cross(sub(b,a),sub(c,a));h=dot(n,a);s=add(add(a,b),c)
    assert dot(n,P10)-h>0
    A=add(A,scale(n,F(1,6)));v0-=h/6;m0=sub(m0,scale(s,h/24))
    for i in range(3):
        for j in range(3): L[i][j]+=(s[i]*n[j]-h*int(i==j))/24

def volume(p): return v0+dot(A,p)
def moment(p): return add(add(m0,matvec(L,p)),scale(p,dot(A,p)/4))
assert volume(P10)==F(rr['raw_volume'])>0
assert moment(P10)==tuple(map(F,rr['raw_first_moment']))
assert tuple(x/volume(P10) for x in moment(P10))==tuple(map(F,rr['raw_centroid']))
put('Q15_FINITE_MASS_POLYNOMIAL.json',dict(parent=NAME,visible_faces=sorted(X),v0=v0,A=A,m0=m0,L=L,point=P10,volume=volume(P10),first_moment=moment(P10),centroid=rr['raw_centroid']))
print('Q15_POINT10_FULL_ACTUAL_MASS_AND_LANDSCAPES_PASS',flush=True)

# Homogeneous cone of the complete closed visibility cell, including infinity.
rows=[]
for i,row in enumerate(H):
    s=1 if i in X else -1
    rows.append(integer_row([s*x for x in row[:3]]+[-s*row[3]]))
rows.append((0,0,0,1))
assert rank(rows)==4
assert all(dot(a,P10+(F(1),))>0 for a in rows)
rays=set()
for ids in combinations(range(len(rows)),3):
    z=kernel4([rows[i] for i in ids])
    if not any(z): continue
    signs=[dot(a,z) for a in rows]
    if min(signs)>=0: pass
    elif max(signs)<=0: z=scale(z,-1)
    else: continue
    rays.add(integer_row(z))
assert rays
ell=tuple(sum(a[j] for a in rows) for j in range(4))
generators=[]
for z in sorted(rays):
    assert dot(ell,z)>0
    generators.append(scale(z,1/dot(ell,z)))
assert all(z[3]>=0 for z in generators)
assert any(z[3]==0 for z in generators), 'the recorded visibility cell was unbounded'

# Fixed material graph in the strict visibility cell.
Z=[tuple(map(F,p)) for p in rr['vertices']]
material_index={p:i for i,p in enumerate(material)}
edge_material=[(material_index[Z[i]],material_index[Z[j]]) for i,j in rr['edges']]
new_id=len(P)
assert all(P[i] in Z for i in BLOCK) and P10 in Z
cut=set();neighbors=set()
for i,j in edge_material:
    if i in BLOCK and j not in BLOCK:cut.add((i,j))
    if j in BLOCK and i not in BLOCK:cut.add((j,i))
    if i==new_id:neighbors.add(j)
    if j==new_id:neighbors.add(i)
cut=sorted(cut);neighbors=sorted(neighbors)
assert cut and neighbors and all(j<new_id for i,j in cut)

# Symmetric polarizations of the finite homogeneous mass polynomials.
def vh(z): return v0*z[3]+dot(A,z[:3])
def mh2(a,b):
    x,y=a[:3],b[:3];wa,wb=a[3],b[3]
    t0=scale(m0,wa*wb)
    t1=scale(add(scale(matvec(L,x),wb),scale(matvec(L,y),wa)),F(1,2))
    t2=scale(add(scale(x,dot(A,y)),scale(y,dot(A,x))),F(1,8))
    return add(add(t0,t1),t2)
def new_numerator2(a,b):
    return sub(scale(add(scale(a[:3],vh(b)),scale(b[:3],vh(a))),F(1,2)),mh2(a,b))
def old_matrix(a,b,i,j):
    t=(a[3]*vh(b)+b[3]*vh(a))/2
    return sym(sub(scale(P[i],t),mh2(a,b)),sub(P[j],P[i]))
def new_matrix(a,b,c,j):
    def term(x,y,z):
        return sym(new_numerator2(x,y),sub(scale(P[j],z[3]),z[:3]))
    return scale(matrix_sum([term(a,b,c),term(a,c,b),term(b,c,a)]),F(1,3))
assert all(vh(z)>0 for z in generators)

count=0;minimum_ratio=None;worst=None

def accept_matrix(M,label,record=True):
    global count,minimum_ratio,worst
    tr=trace(M);n=norm1(M)
    if not (tr+DELTA*n<0):return False
    if record:
        count+=1
        ratio=-tr/n
        if minimum_ratio is None or ratio<minimum_ratio:
            minimum_ratio=ratio;worst=dict(label=label,matrix=M)
    return True

# Global quadratic coefficient check for all outgoing old-block arrows.
for i,j in cut:
    for a,b in combinations_with_replacement(range(len(generators)),2):
        assert accept_matrix(old_matrix(generators[a],generators[b],i,j),['old',i,j,a,b]), 'old-block coefficient not certified; no exclusion is asserted'

# A compact projective section of the entire unbounded cone.
assert all(dot(SECTION,z)>0 for z in generators)
G=[scale(z,1/dot(SECTION,z)) for z in generators]
q=[(z[0],z[1],z[3]) for z in G]
section=verify(e.extremes(q),'Q15_PROJECTIVE_SECTION')
Q=[tuple(map(F,p)) for p in section['vertices']]
assert len(Q)==len(G)
def lift(p):return (p[0],p[1],1-p[0]-10*p[2],p[2])
O=tuple(sum(p[k] for p in Q)/len(Q) for k in range(3))
assert all(dot(row[:3],O)<F(row[3]) for row in section['raw_H'])
tetrahedra=[]
for cy in section['faces']:
    for j in range(1,len(cy)-1):
        tetrahedra.append([lift(O),lift(Q[cy[0]]),lift(Q[cy[j]]),lift(Q[cy[j+1]])])
leaves=[];maximum_depth=0

def leaf_ok(T,record=False,label=None):
    for j in neighbors:
        for a,b,c in combinations_with_replacement(range(4),3):
            M=new_matrix(T[a],T[b],T[c],j)
            if not accept_matrix(M,['new',label,j,a,b,c],record):return False
    return True

def visit(T,depth,path):
    global maximum_depth
    maximum_depth=max(maximum_depth,depth)
    if leaf_ok(T):
        assert leaf_ok(T,True,path)
        leaves.append(dict(path=path,corners=T))
        return
    assert depth<MAX_DEPTH, 'subdivision limit reached; this is not an exclusion certificate'
    i,j=max(combinations(range(4),2),key=lambda z:sum((T[z[0]][k]-T[z[1]][k])**2 for k in [0,1,3]))
    m=scale(add(T[i],T[j]),F(1,2))
    left=list(T);right=list(T);left[i]=m;right[j]=m
    visit(left,depth+1,path+[[i,j,0]])
    visit(right,depth+1,path+[[i,j,1]])

for k,T in enumerate(tetrahedra):visit(T,0,[k])
assert minimum_ratio>DELTA and 3*DELTA<1
certificate=dict(parent=NAME,visible_faces=sorted(X),strict_visibility_domain=True,
    gram_entrywise_radius=DELTA,cone_rows=rows,cone_generators=generators,
    finite_generator_count=sum(z[3]>0 for z in generators),
    recession_ray_count=sum(z[3]==0 for z in generators),
    section_functional=SECTION,section_vertices=Q,section_faces=section['faces'],
    block=sorted(BLOCK),block_boundary=cut,new_point_neighbors=neighbors,
    mass_coefficients=dict(v0=v0,A=A,m0=m0,L=L),
    initial_cone_tetrahedra=tetrahedra,leaves=leaves,maximum_depth=maximum_depth,
    depth_limit=MAX_DEPTH,coefficient_matrix_count=count,
    minimum_trace_to_entrywise_norm_ratio=minimum_ratio,worst=worst)
put('Q15_COMPLETE_CELL_GRAM_CERTIFICATE.json',certificate)
put('Q15_RECHECK_RECEIPTS.json',dict(RECEIPTS))
print('Q15_COMPLETE_UNBOUNDED_CELL_CERTIFIED_U_GE_TWO',DELTA,len(leaves),count,flush=True)
```

### Interpretation of a successful run

The cone enumeration is exhaustive: the signed system is full-dimensional and pointed, and every extreme ray of a four-dimensional pointed polyhedral cone has three independent active constraints. Its projective section is compact. The audited section hull and its interior-star triangulation cover that section; recursive edge bisection preserves coverage. Strict coefficient inequalities therefore hold for every real point in the original strict visibility cell, not just the enumerated vertices, rays, or sampled parameters.

The endpoint audit is a different part of the computation: it supplies actual volume, first moment, centroid, maximal complex, all mixed and weak tests, and both complete landscapes for K10. The whole-cell obstruction uses actual-mass polynomials and protected outgoing arrows; it does not infer mechanics from Euler alone.

## Continuation boundary

The useful next scientific question is not another point-location scan in the same fixed Q15 visibility partition. The retained record says that entire one-point architecture is blocked by actual-mass root transfer, and the supplied patch makes that claim exactly checkable. Once its completion is observed, a constructive continuation must change a substantive premise: move or remove original material, alter retained carriers and the visibility partition, use more than one inserted point, or leave the certified metric window.

For the separately recorded compact and enriched own211 deformations, recover their literal input arrays before using them as exact parents. Until then, the authoritative reconstructible search parent remains **H23_CAP_RESERVE31_G5**, and the fully specified new finite test body is **conv(P union {(10,-159/100,10)})**. No missing log, failed retrieval, numerical root count, or unobserved aggregate invocation is being converted into a broader C<500 exclusion.
