# material-e543dc7cf552

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact physical facet-cone Markov countercontrol, version 1.
Requires CPython >=3.10 and sympy==1.14.0. No floating-point input.
Run: python physical_slack_obliquity_v1.py
Writes: physical_slack_obliquity_v1.json (UTF-8, sorted JSON, final LF).
The polyhedron is NOT a class-110 construction: it has S=5,U=5,H=8.
"""
from itertools import combinations
import hashlib
import json
from pathlib import Path
import sympy as s

if s.__version__ != "1.14.0":
    raise RuntimeError("Reproduction requires sympy==1.14.0")

raw = [s.Matrix(t) for t in [(0,0,0),(3,0,0),(2,2,0),(0,1,0),(1,1,3)]]
faces = [(0,3,2,1),(0,1,4),(1,2,4),(2,3,4),(3,0,4)]
zero = s.zeros(3,1)
reference = sum(raw, zero)/len(raw)
# Exact boundary integration from a strictly interior reference point.
triangles = [(f[0],f[k],f[k+1]) for f in faces for k in range(1,len(f)-1)]
relative = [v-reference for v in raw]
dets = [s.det(s.Matrix.hstack(*(relative[j] for j in t))) for t in triangles]
assert all(d > 0 for d in dets)
volume = sum(dets)/6
centroid = reference + sum((d*sum((relative[j] for j in t), zero)/24
                           for d,t in zip(dets, triangles)), zero)/volume
assert volume == 4
assert centroid == s.Matrix([s.Rational(21,16),s.Rational(13,16),s.Rational(3,4)])
x = [v-centroid for v in raw]

# Rebuild every supporting plane from every non-collinear vertex triple.
# Group all vertices in a maximal plane, so coplanar triangulation diagonals
# are never counted as physical edges.
actual_faces = set()
for a,b,c in combinations(range(len(x)),3):
    normal = (x[b]-x[a]).cross(x[c]-x[a])
    if normal == zero:
        continue
    values = [normal.dot(v-x[a]) for v in x]
    if all(t <= 0 for t in values) or all(t >= 0 for t in values):
        actual_faces.add(frozenset(i for i,t in enumerate(values) if t == 0))
assert actual_faces == {frozenset(f) for f in faces}

poles, means, weights = [], [], []
for f in faces:
    tris = [(f[0],f[k],f[k+1]) for k in range(1,len(f)-1)]
    ds = [s.det(s.Matrix.hstack(*(x[j] for j in t))) for t in tris]
    assert all(d > 0 for d in ds)
    normal = (x[f[1]]-x[f[0]]).cross(x[f[2]]-x[f[0]])
    support = normal.dot(x[f[0]])
    assert support > 0
    q = normal/support
    assert all(q.dot(x[j]) == 1 for j in f)
    assert all(q.dot(x[j]) < 1 for j in range(len(x)) if j not in f)
    # In a common face plane, cone-volume ratios equal triangle-area ratios.
    c = sum((d*sum((x[j] for j in t),zero)/3 for d,t in zip(ds,tris)),zero)/sum(ds)
    poles.append(q)
    means.append(c)
    weights.append(sum(ds)/(6*volume))

n = len(faces)
Q = s.Matrix.hstack(*poles).T
C = s.Matrix.hstack(*means).T
D = s.diag(*weights)
one = s.ones(n,1)
w = s.Matrix(weights)
J = one*w.T
M = s.Matrix(n,n,lambda i,j: weights[j]*(1-means[i].dot(poles[j])))
expected = s.Matrix([[0,s.Rational(9,32),s.Rational(29,96),s.Rational(23,96),s.Rational(17,96)],
                     [s.Rational(1,3),0,s.Rational(1,4),s.Rational(7,24),s.Rational(1,8)],
                     [s.Rational(1,3),s.Rational(1,4),0,s.Rational(5,24),s.Rational(5,24)],
                     [s.Rational(1,3),s.Rational(3,8),s.Rational(5,24),0,s.Rational(1,12)],
                     [s.Rational(1,3),s.Rational(1,8),s.Rational(11,24),s.Rational(1,12),0]])
assert M == expected
assert sum(weights) == 1 and all(v > 0 for v in weights)
assert Q.T*w == zero and C.T*w == zero
assert Q.T*D*C == s.eye(3)/3
assert M*one == one and w.T*M == w.T
assert M*M + M/3 == 4*J/3
assert all(M[i,i] == 0 for i in range(n))
assert all(M[i,j] > 0 for i in range(n) for j in range(n) if i != j)

# A nonzero directed-cycle imbalance rules out EVERY positive diagonal
# symmetrizer, not merely the natural cone-volume diagonal D.
cycle_forward = M[0,1]*M[1,2]*M[2,0]
cycle_reverse = M[0,2]*M[2,1]*M[1,0]
assert cycle_forward == s.Rational(3,128)
assert cycle_reverse == s.Rational(29,1152)
assert cycle_forward-cycle_reverse == -s.Rational(1,576)
assert D*M != M.T*D

# Physical regression residual and its exact rank-one obliquity.
B = Q.T*D*Q
G = (3*B).inv()
Z = s.simplify(C-Q*G)
P = Q*B.inv()*Q.T*D
R = 3*C*Q.T*D
K = s.simplify(R-P)
assert Q.T*D*Z == s.zeros(3,3)
assert Z.T*w == zero
assert Z.rank() == K.rank() == 1
assert P*P == P and P*K == s.zeros(n,n) and K*P == K
assert K*K == s.zeros(n,n) and R*R == R
sigma_squared = s.factor(s.trace(D.inv()*K.T*D*K))
assert sigma_squared == s.Rational(184,1479)
H = s.simplify((M + D.inv()*M.T*D)/2)
t = s.symbols('t')
expected_charpoly = (t-1)*(3*t+1)**2*(13311*t*t+4437*t-46)/119799
assert s.factor(H.charpoly(t).as_expr()-expected_charpoly) == 0
assert s.factor(M.charpoly(t).as_expr()-t*(t-1)*(t+s.Rational(1,3))**3) == 0
# The quadratic factor has negative constant and positive leading coefficient:
# exactly one root is positive. Thus the stationary-weight symmetric part
# is NOT negative semidefinite on the mean-zero space.

# Exact mechanical classification at the actual solid centroid.
edges = sorted({tuple(sorted((f[k],f[(k+1)%len(f)])))
                for f in faces for k in range(len(f))})
stable, unstable, saddles, weak = [], [], [], []
for i,q in enumerate(poles):
    foot = q/q.dot(q)
    slacks = [1-r.dot(foot) for j,r in enumerate(poles) if j != i]
    if all(a >= 0 for a in slacks):
        (stable if all(a > 0 for a in slacks) else weak).append(i if all(a > 0 for a in slacks) else ['face',i])
for i,v in enumerate(x):
    dots = [v.dot(u-v) for j,u in enumerate(x) if j != i]
    if all(a <= 0 for a in dots):
        (unstable if all(a < 0 for a in dots) else weak).append(i if all(a < 0 for a in dots) else ['vertex',i])
for i,j in edges:
    e = x[j]-x[i]
    parameter = -x[i].dot(e)/e.dot(e)
    foot = x[i]+parameter*e
    dots = [foot.dot(x[k]-x[i]) for k in range(len(x)) if k not in (i,j)]
    if 0 <= parameter <= 1 and all(a <= 0 for a in dots):
        if 0 < parameter < 1 and all(a < 0 for a in dots):
            saddles.append([i,j])
        else:
            weak.append(['edge',i,j])
assert (len(x),len(edges),len(faces)) == (5,8,5)
assert (len(stable),len(unstable),len(saddles)) == (5,5,8)
assert weak == []


def vector(v):
    return [str(z) for z in v]


def matrix(A):
    return [[str(A[i,j]) for j in range(A.cols)] for i in range(A.rows)]

report = {
    'object': 'PHYSICAL_FACET_CONE_MARKOV_OBLIQUITY_V1',
    'sympy_version': s.__version__,
    'raw_vertices': [vector(v) for v in raw],
    'faces': [list(f) for f in faces],
    'edges': [list(e) for e in edges],
    'volume': str(volume), 'centroid': vector(centroid),
    'centered_vertices': [vector(v) for v in x],
    'facet_poles': matrix(Q), 'facet_centroids': matrix(C),
    'cone_volume_weights': vector(w), 'markov_matrix': matrix(M),
    'cycle_forward': str(cycle_forward), 'cycle_reverse': str(cycle_reverse),
    'cycle_difference': str(cycle_forward-cycle_reverse),
    'regression_metric_G': matrix(G), 'residual_Z': matrix(Z),
    'residual_rank': Z.rank(), 'obliquity_sigma_squared': str(sigma_squared),
    'symmetric_part_charpoly': str(s.factor(expected_charpoly)),
    'stable_faces': stable, 'unstable_vertices': unstable,
    'saddle_edges': saddles, 'weak_cells': weak,
    'scope': 'Universal physical-operator countercontrol; NOT class 110; no complexity bound changed.'
}
path = Path('physical_slack_obliquity_v1.json')
blob = (json.dumps(report,sort_keys=True,indent=2,ensure_ascii=True)+'\n').encode('utf-8')
path.write_bytes(blob)
print('EXACT_HULL_AND_SOLID_CENTROID_PASS')
print('PHYSICAL_MARKOV_IDENTITY_PASS')
print('NO_POSITIVE_DIAGONAL_SYMMETRIZER cycle_difference=-1/576')
print('RANK_ONE_OBLIQUITY sigma_squared=184/1479')
print('POSITIVE_MEAN_ZERO_SYMMETRIC_EIGENVALUE')
print('CLASS_S5_U5_H8_WEAK0_NOT_110')
print('OUTPUT',path.name,len(blob),hashlib.sha256(blob).hexdigest())
print('ALL_EXACT_CHECKS_PASS')
