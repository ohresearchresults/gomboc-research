# material-c23ee6747036

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact polynomial and genuine-cube controls for affine-simplex moment rows.
python -S affine_audit.py; no numerical libraries, random seed or coordinates
outside this complete source. This is an algebra check, not a Stokes formalization.
"""
from pathlib import Path
from itertools import combinations,permutations,product
from fractions import Fraction as F
import hashlib,json
import affine_moments as am
assert __debug__
HERE=Path(__file__).resolve().parent

def add(*rows):
    out={}
    for r in rows:
        for k,v in r.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def scale(row,s):return {k:v*s for k,v in row.items() if v*s}
def mul(a,b):
    out={}
    for i,v in a.items():
        for j,w in b.items():
            k=tuple(x+y for x,y in zip(i,j));out[k]=out.get(k,0)+v*w
    return {k:v for k,v in out.items() if v}
def one(x):return {(0,0,0):x} if x else {}
def det(A):
    out={}
    for p in permutations(range(len(A))):
        term=one(am.parity(p))
        for i,j in enumerate(p):term=mul(term,A[i][j])
        out=add(out,term)
    return out

def moment_polynomials(X,t):
    a,b,c,d=(X[i] for i in t)
    D=det([[add(x[j],scale(a[j],-1)) for j in range(3)] for x in (b,c,d)])
    center=[add(*(X[i][j] for i in t)) for j in range(3)]
    JJ=[[add(mul(center[j],center[k]),*(mul(X[i][j],X[i][k]) for i in t))
            for k in range(3)] for j in range(3)]
    return [D]+[mul(D,v) for v in center]+[mul(D,JJ[j][k]) for j in range(3) for k in range(j,3)]

# Generic normalized five-point affine circuit. The first tetrahedron is
# nondegenerate; affine covariance and polynomial continuity cover all inputs.
a={(1,0,0):1};b={(0,1,0):1};c={(0,0,1):1}
X=[[one(0),one(0),one(0)],[one(1),one(0),one(0)],
   [one(0),one(1),one(0)],[one(0),one(0),one(1)],[a,b,c]]
acc=[{} for _ in range(10)]
for j in range(5):
    t=tuple(i for i in range(5) if i!=j);mom=moment_polynomials(X,t)
    acc=[add(v,scale(w,(-1)**j)) for v,w in zip(acc,mom)]
assert acc==[{}]*10

# A genuine own-centered uniform cube with all six maximal facets intact.
vertices=list(product((-1,1),repeat=3))
rawfaces=[]
for j in range(3):
    for s in (-1,1):
        face=[i for i,v in enumerate(vertices) if v[j]==s]
        adj={i:[k for k in face if sum(x!=y for x,y in zip(vertices[i],vertices[k]))==1] for i in face}
        cy=[min(face)];prev=None
        while len(cy)<4:
            nxt=min(k for k in adj[cy[-1]] if k!=prev)
            prev,now=cy[-1],nxt;cy.append(now)
        assert cy[0] in adj[cy[-1]] and len(set(cy))==4
        rawfaces.append(cy)
faces=am.orientations(rawfaces);epsilon={}
for cy in faces:
    for pos in combinations(range(4),3):
        tri=tuple(cy[p] for p in pos)
        for i in range(8):
            if i in cy:continue
            t=tuple(sorted((i,)+tri));s=am.parity((i,)+tri)
            if t in epsilon:assert epsilon[t]==s
            epsilon[t]=s
allcells=list(combinations(range(8),4));cycles=[]
for t in combinations(range(1,8),4):
    five=(0,)+t;cycles.append({five[:j]+five[j+1:]:(-1)**j for j in range(5)})
flats=[tuple(sorted(cy)) for cy in faces]
rels,rank=am.restricted_basis(cycles+[{t:1} for t in flats],set(epsilon),allcells)
XP=[[one(v) for v in x] for x in vertices]
mom={t:moment_polynomials(XP,t) for t in allcells}
assert all(mom[t]==[{}]*10 for t in flats)
signed={t:mom[t][0].get((0,0,0),0) for t in epsilon}
orientation={1 if signed[t]*epsilon[t]>0 else -1 for t in epsilon}
assert len(orientation)==1 and all(signed[t] for t in epsilon)
for h in rels:
    total=[{}]*10
    for t,z in h.items():total=[add(a,scale(b,z)) for a,b in zip(total,mom[t])]
    assert total==[{}]*10
# The cube's true volume and centroid are independent exact elementary values.
assert sum(vertices[i][j] for i in range(8) for j in range(3))==0
report={'identity':'AFFINE_SIMPLEX_POLYNOMIAL_AND_CUBE_AUDIT_V1',
    'generic_five_point_zero_polynomials':10,'cube_vertices':vertices,
    'cube_maximal_facets':faces,'cube_volume':8,'cube_centroid':[0,0,0],
    'cube_actual_positive_cells':len(epsilon),'cube_flat_cells':len(flats),
    'cube_full_relation_rank':rank,'cube_restricted_relation_rank':len(rels),
    'cube_exact_moment_equalities':10*len(rels),'common_orientation':next(iter(orientation))}
b=am.fm.enc(report);(HERE/'affine_audit.json').write_bytes(b)
print('AFFINE_SIMPLEX_GENERIC_FIVE_POINT_10_POLYNOMIALS_PASS')
print('AFFINE_SIMPLEX_GENUINE_CUBE_ALL_SHARED_MOMENTS_PASS',len(rels),10*len(rels))
print('AFFINE_SIMPLEX_EXACT_AUDIT_PASS',*am.fm.pin(b))
