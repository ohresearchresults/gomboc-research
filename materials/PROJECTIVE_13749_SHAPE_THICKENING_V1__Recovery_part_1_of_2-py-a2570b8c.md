# material-a2570b8c8d10

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

"""Exact finite checks for PROJECTIVE_13749_SHAPE_THICKENING_V1.

Python 3.11+ standard library, assertions enabled. Run:
    python -S verify_shape_thickening.py

This checks the full eight-parameter source cube, exact facet/edge identity,
all potential additional supporting triples, the seven actual fan tetrahedra,
and all rational constants used by the analytic perturbation proof.
The inherited K >= I/8 theorem is a separate explicitly named dependency;
this program neither substitutes a sample for that theorem nor reruns it.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys
assert __debug__, "Assertions must be enabled"

IDENTITY = "PROJECTIVE_13749_SHAPE_THICKENING_V1"
EPSILON = F(1, 2**24)
SHAPE_RADIUS = F(1, 2**27)
CENTER = tuple(map(F, ("1/2", "3/4", "1/8", "3/4", "1/4", "1/8", "3/4", "1/2")))
FACES = ((0,1,2,3,8,7,6),(0,1,4,5),(0,5,9,6),
         (1,2,4),(2,3,4),(3,4,9,8),(4,5,9),(6,7,9),(7,8,9))
TETS = ((0,4,2,1),(0,4,3,2),(0,3,4,9),(0,3,9,8),
        (0,4,5,9),(0,6,7,9),(0,7,8,9))
TREE = (0,0,1,2,3,4,0,6,7,8)
ALPHA = (9,4,1,38,22,8,4,1,15)
MOVING = frozenset((1,2,3,6,7,8))

class Interval:
    def __init__(self, lo=0, hi=None):
        if isinstance(lo, Interval):
            self.lo, self.hi = lo.lo, lo.hi
        else:
            self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, other):
        other = Interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __neg__(self):
        return Interval(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + -Interval(other)
    def __rsub__(self, other):
        return Interval(other) + -self
    def __mul__(self, other):
        other = Interval(other)
        v = [a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return Interval(min(v), max(v))
    __rmul__ = __mul__

def sub(a,b):
    return [x-y for x,y in zip(a,b)]
def dot(a,b):
    return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def signed_tet(a,b,c,d):
    return dot(cross(sub(b,a),sub(c,a)),sub(d,a))
def vertices(u, interval=False):
    a,b,c,d,e,f,g,h = u
    v = [(1,0,0),(1,a,0),(1,b,c),(1,d,1-d),(0,1,0),
         (0,0,0),(1,0,h),(1,f,g),(1,e,1-e),(0,0,1)]
    cast = Interval if interval else F
    return [[cast(x) for x in p] for p in v]
def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, Interval):
        return [str(x.lo), str(x.hi)]
    if isinstance(x, dict):
        return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x, (tuple,list)):
        return [encode(v) for v in x]
    return x

v0 = vertices(CENTER)
u = [Interval(x-SHAPE_RADIUS, x+SHAPE_RADIUS) for x in CENTER]
v = vertices(u, interval=True)
assert SHAPE_RADIUS*8 == EPSILON
# The four nontriangular facets lie IDENTICALLY in x=1,z=0,y=0,y+z=1,
# respectively. All other facets are triangles. These identities follow
# by direct substitution in vertices(), not by interval zero containment.
assert [len(f) for f in FACES] == [7,4,4,3,3,4,3,3,3]
nonincident = []
polygon_tests = []
for fi,face in enumerate(FACES):
    a,b,c = face[:3]
    n0 = cross(sub(v0[b],v0[a]),sub(v0[c],v0[a]))
    n = cross(sub(v[b],v[a]),sub(v[c],v[a]))
    outside = [i for i in range(10) if i not in face]
    base_signs = [dot(n0,sub(v0[j],v0[a])) for j in outside]
    assert all(z>0 for z in base_signs) or all(z<0 for z in base_signs)
    side = 1 if base_signs[0]>0 else -1
    for j in outside:
        z = side*dot(n,sub(v[j],v[a]))
        assert z.lo > 0, (fi,j,encode(z))
        nonincident.append((fi,j,z))
    # Every other polygon vertex lies strictly left of every oriented edge,
    # with orientation measured against the first triple's normal.
    for aa,bb in zip(face, face[1:]+face[:1]):
        for j in face:
            if j not in (aa,bb):
                z = dot(n,cross(sub(v[bb],v[aa]),sub(v[j],v[aa])))
                assert z.lo > 0, (fi,aa,bb,j,encode(z))
                polygon_tests.append((fi,aa,bb,j,z))
assert len(nonincident)==56
edges={}
for fi,face in enumerate(FACES):
    for a,b in zip(face,face[1:]+face[:1]):
        edges.setdefault(tuple(sorted((a,b))),[]).append(fi)
assert len(edges)==17 and all(len(owners)==2 for owners in edges.values())
assert 10-len(edges)+len(FACES)==2
assert all(tuple(sorted((i,TREE[i]))) in edges for i in range(1,10))
# Completeness independent of the closed-surface argument: every triple not
# in a named facet has vertices on BOTH sides over the entire input box.
other_triples=[]
for tri in combinations(range(10),3):
    if any(set(tri).issubset(face) for face in FACES):
        continue
    a,b,c=tri
    pos=[j for j in range(10) if j not in tri and signed_tet(v0[a],v0[b],v0[c],v0[j])>0]
    neg=[j for j in range(10) if j not in tri and signed_tet(v0[a],v0[b],v0[c],v0[j])<0]
    assert pos and neg, tri
    p=next((j for j in pos if signed_tet(v[a],v[b],v[c],v[j]).lo>0),None)
    q=next((j for j in neg if signed_tet(v[a],v[b],v[c],v[j]).hi<0),None)
    assert p is not None and q is not None, tri
    other_triples.append((tri,p,q))
# The fan is the cone from v0 over all facets not incident to v0.
# The only quadrilateral among those facets is triangulated along (3,9).
assert {frozenset(t[1:]) for t in TETS} == {
    frozenset(t) for t in ((4,2,1),(4,3,2),(3,4,9),(3,9,8),
                           (4,5,9),(6,7,9),(7,8,9))}
fan_checks=[]
for t in TETS:
    z=signed_tet(*(v[i] for i in t))
    assert z.lo>0, (t,encode(z))
    fan_checks.append((t,z))
assert signed_tet(*(v0[i] for i in (0,4,5,9)))==1
incidence_occurrences=sum(i in MOVING for t in TETS for i in t)
assert incidence_occurrences==11
print('FULL_EIGHT_PARAMETER_SOURCE_CUBE_TRUE_F_VECTOR_10_17_9_PASS')
print('ALL_SOURCE_FACETS_ALL_OTHER_SUPPORTING_TRIPLES_AND_SEVEN_FAN_TETS_PASS')
# Analytic constants; no finite sampling of the projective or metric domain.
R=F(15,8)
gamma=F(7,15)
assert 1-gamma==F(8,15)
assert gamma*F(5,3)==F(7,9)
assert F(1)+3*F(7,9)==F(10,3)
assert F(8,15)*F(3,4)==F(2,5)
vertex_lipschitz=F(5,2)+F(10,3)/(F(2,5)*F(8,15))
assert vertex_lipschitz==F(145,8)<20
assert 2*(3*R/F(4))**2<4  # diameter of all tetrahedron-centroid atoms <2.
volume_lipschitz=11*R**2
centroid_lipschitz=F(3,4)+2*volume_lipschitz
matrix_lipschitz=2*R*sum(ALPHA)*(3+centroid_lipschitz)
projective_shape_lipschitz=20*matrix_lipschitz
assert centroid_lipschitz==F(2499,32)
assert matrix_lipschitz==F(1985175,64)
assert projective_shape_lipschitz==F(9925875,16)
loss=projective_shape_lipschitz*EPSILON
assert loss<F(1,16)
remaining=F(1,8)-loss
assert remaining>F(1,16)
assert sum(ALPHA)==102 and 16*sum(ALPHA)==1632
print('UNIFORM_PROJECTIVE_VERTEX_AND_ACTUAL_CENTROID_LIPSCHITZ_CONSTANTS_PASS')
print('INHERITED_MATRIX_MARGIN_TRANSFER_TO_1_OVER_16_EXACT_ARITHMETIC_PASS')
report=dict(identity=IDENTITY, proof_status='conditional_only_on_named_accepted_projective_matrix_theorem',
    inherited_source_material='[internal-source-reference]',
    inherited_proof_material='[internal-source-reference]',
    source_center=CENTER,source_coordinate_radius=SHAPE_RADIUS,
    relative_component_radius=EPSILON,facets=FACES,edges=sorted(edges),tets=TETS,
    tree=TREE,weights=ALPHA,nonincident_count=len(nonincident),
    polygon_test_count=len(polygon_tests),other_triple_count=len(other_triples),
    minimum_nonincident_lower_bound=min(z.lo for fi,j,z in nonincident),
    minimum_polygon_side_lower_bound=min(z.lo for fi,a,b,j,z in polygon_tests),
    minimum_fan_determinant_lower_bound=min(z.lo for t,z in fan_checks),
    moving_vertex_tetrahedron_occurrences=incidence_occurrences,
    vertex_l1_lipschitz=vertex_lipschitz,vertex_l1_bound_used=20,
    volume_D_lipschitz=volume_lipschitz,centroid_l2_lipschitz=centroid_lipschitz,
    matrix_operator_lipschitz=matrix_lipschitz,shape_lipschitz=projective_shape_lipschitz,
    maximum_matrix_loss=loss,proved_matrix_lower_bound=remaining,
    simplified_matrix_lower_bound='1/16',forced_arrow_bound='-trace(M)/1632',
    nonincidence_ledger=nonincident,polygon_ledger=polygon_tests,
    excluded_supporting_triples=other_triples,fan_ledger=fan_checks,
    new_whole_index_exclusions=0,unchanged_global_lower_bound='C>=34')
raw=(json.dumps(encode(report),sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
Path('shape_thickening_report.json').write_bytes(raw)
print('REPORT',len(raw),hashlib.sha256(raw).hexdigest())
print('SOURCE',len(Path(__file__).read_bytes()),hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
print('PROJECTIVE_13749_SHAPE_THICKENING_EXACT_FINITE_CHECKS_PASS')
