# material-a2b8d8e0d6e0

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# PENTAGON_MINIMAL_FOUR_ARROW_AND_FIVE_SUPPORT_V1

Coordinator-derived analytic theorem with an exact rational control. This answers the local open question in [internal-source-reference]. It is not an E17 realization, a canonical exclusion, a mono-monostatic construction or a new global bound. The interval34<=Cmin<=622 remains unchanged.

## Explicit strictly convex pentagon and common metric

p0=(0,0),p1=(2,0),p2=(2,4),p3=(-2,5),p4=(-3,3), counterclockwise. q_i=(p_i,1). Select the four true consecutive boundary arrows0->1->2->3->4. Every nonincident vertex lies strictly left of each oriented polygon edge; the exact source checks all fifteen determinants.

For physical SPD N write upper-left block H=[[a,b],[b,c]] and first two entries in its last column k=(kx,ky). Then H>0 and
D0=2kx,
D1=8b+4ky,
D2=-8a-14b+4c-4kx+ky,
D3=2a-b-10c-kx-2ky.
The last diagonal entry does not enter the arrows. Conversely every H>0 and arbitraryk extends to an SPD N by N33>k^T H^-1 k. These constraints therefore refer to one physical metric, not independent local metrics.

## All four weak arrows impossible

11D0+2D1+4D2+6D3=-20a-46b-44c=-tr(HQ), Q=[[20,23],[23,44]].
Q>0: leading minors20,351; exact SOS20(x+23y/20)^2+(351/20)y².
Since H,Q>0, tr(HQ)>0, contradicting allD>=0. This includes every weak-arrow wall. For any affine embedding q_i=A p_i+b0 in a plane not through the origin, the stress becomes -AQA^T, a nonzero rank-two NSD matrix. The same common-SPD contradiction holds.

## Every proper arrow subsystem strictly feasible

After deleting one arrow use the following separate witness metrics in the SAME originalq coordinates:
OmitD0: N0=[[1,0,-20],[0,1,1],[-20,1,402]], leadingminors(1,1,1), D=(-40,4,77,10).
OmitD1: N1=[[2,-2,2],[-2,4,-19],[2,-19,147]], leadingminors(2,4,2), D=(4,-92,1,2).
OmitD2: N2=[[12,0,1],[0,2,1],[1,1,1]], leadingminors(12,24,10), D=(2,4,-91,1).
OmitD3: N3=[[1,0,1],[0,1,9],[1,9,83]], leadingminors(1,1,1), D=(2,36,1,-27).
All retained arrows are strictly positive. Thus EVERY three-arrow subsystem passes, not merely the two consecutive quadrilateral windows. Consecutive quad gates are not complete for convex pentagonal boundary paths. The displayed path is minimally infeasible with four arrows.

## Genuinely interior two-matrix-pencil obstruction

Edges E=((2,0),(0,4),(-4,1),(-1,-2)). The nonnegative zero-displacement cone has exactly two extreme rays r1=(1,1,0,2),r2=(9,0,4,2): its general point islambda=u*r1+v*r2, u=lambda1>=0,v=lambda2/4>=0.
For S(lambda)=sum lambda_i sym(p_i E_i^T),
S1=[[4,3],[3,-20]],det=-89;
S2=[[-28,-29],[-29,-4]],det=-729.
Both are indefinite, but2S1+S2=-Q is ND. With S(t)=(1-t)S1+tS2,
trace=-16-16t, determinant=-89+896t-1536t².
The NSD interval is [(56-10sqrt(10))/192,(56+10sqrt(10))/192], strictly inside(0,1). Its endpoints are nonzero rank-one NSD; its interior is ND. At rationalt=1/3, S=-Q/3, determinant39. Thus neither elementary zero-displacement circuit alone supplies the obstruction; the metric shared by their combination does.

The example persists in an OPEN neighborhood of the five planar vertices. Strict convexity and the strictly positive retained-arrow evaluations under the four fixed witness matrices persist. Positive three-edge dependences with supports(0,1,3) and(0,2,3), computed by cross products, vary continuously. At this example their raw coefficients are(4,4,0,8) and(9,0,4,2); one-half the first plus the second gives(11,2,4,6). The resulting ND stress persists. No numerical neighborhood radius is claimed.

## Universal five-arrow support bound, weak AND strict

Any finite collection of selected arrows among points in an affine plane not through the origin that is infeasible under one SPD has an infeasible selected subset of at most FIVE arrows. This is a local coplanar theorem, not a global graph-count exclusion. Four is necessary by the example; whether five is necessary on convex boundary paths remains open.

Weak infeasibility: the complete tangent alternative of [internal-source-reference] giveslambda>=0 withsum lambda_i E_i=0 and S(lambda) nonzero NSD. Encode each arrow by v_i=(E_i,sym(p_i E_i^T)) in R² direct-sum Sym2, dimensionfive. The vector(0,S) is a nonnegative combination of v_i. If more thanfive coefficients arepositive, linear dependence permits subtracting an appropriate multiple of a dependence until a coefficient vanishes, preserving the target and allnonnegativecoefficients. Repeat. At mostfive selected arrows remain and give exactly the same nonzero NSD certificate.

Strict infeasibility: if weak feasibility alreadyfails use above. Otherwise the strict tangent alternative supplies a nontrivial nonnegative dependence sumlambda_i v_i=0, because any nonzero NSD stress wouldcontradict weakfeasibility. Choose an inclusion-minimal positive dependence; its support has atmostsix vectors. If it hadsix, their rank wouldbefive and they would span thewholefive-dimensionalspace. A strictlypositivezero relation then makes their positivecone theentirespace: shift any real coefficient representation by a sufficientlylarge multipleof thepositiverelation. In particular thecone would contain(0,-I), contradictingweakfeasibility. Thus supportatmostfive. On thissubset allselectedD cannot bestrictlypositive. A zero certificate is used ONLY forstrict, never incorrectlyforweak, infeasibility.

## Actual-realization boundary

No actual uniform E17 body at its ownCOM is established here. To use these gates globally the poles must be q_i=n_i/(b_i-n_i.g) from the SAME genuine uniformly filled body and lie on true incident facet edges. An algebraic segment is not automatically a true edge. A useful next direction is to realize the open obstruction chamber at a genuine degree-five E17 vertex, or derive actual support-height/centroid inequalities forcing it. Independent open sharpness question: can a convex hexagonal five-arrow boundary path be minimally infeasible, or dofour alwayssuffice forconvex paths?

## Complete recovery and evidence level

Save the complete code below as pentagon_joint.py, UTF-8 LF with finalnewline. Python>=3.10 standardlibrary only, no external files, randomness orsolver; assertions enabled. Run `python pentagon_joint.py`. The same source alone reconstructs the report in a fresh directory. Expected marker PENTAGON_FOUR_ARROWS_ALL_PROPER_SUBSETS_STRICT_PASS.
Source3348bytes SHA2562cb253d621a41356871c209332acfc48bb22a7d347ccd7bcdb1d6399232efc02.
Output pentagon_joint_report.json2489bytes SHA256fbf5e8f9d9f71ba4bd6385779443874a7265dabcd8c73eccc9020be9bdf28f7d.
Coordinator executed source on CPython3.13.5 and reproduced exact marker/hashes. This verifies the rational control with elementary analytic proofs above, not proof-assistant formalization or independent worker replay. Exploratory numerical candidate search is not a proof input.

```python
"""Exact minimal four-arrow obstruction on a strictly convex polar pentagon.
Python >=3.10, standard library only. No external files or solver.
Run: python pentagon_joint.py
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

P = ((0, 0), (2, 0), (2, 4), (-2, 5), (-3, 3))
WEIGHTS = (11, 2, 4, 6)
METRICS = (
    ((1, 0, -20), (0, 1, 1), (-20, 1, 402)),
    ((2, -2, 2), (-2, 4, -19], [-2, -19, 147)),
)
```

Correction: the preceding short code fence is NOT the recovery source and must not be executed. The complete authoritative recovery source is the following fence; its METRICS has four3x3matrices. The prose and exact matrices above are unchanged.

```python
"""Exact minimal four-arrow obstruction on a strictly convex polar pentagon.
Python >=3.10, standard library only. No external files or solver.
Run: python pentagon_joint.py
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

P = ((0, 0), (2, 0), (2, 4), (-2, 5), (-3, 3))
WEIGHTS = (11, 2, 4, 6)
METRICS = (
    ((1, 0, -20), (0, 1, 1), (-20, 1, 402)),
    ((2, -2, 2), (-2, 4, -19), (2, -19, 147)),
    ((12, 0, 1), (0, 2, 1), (1, 1, 1)),
    ((1, 0, 1), (0, 1, 9), (1, 9, 83)),
)

def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))

def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def det(A):
    if len(A) == 1:
        return A[0][0]
    return sum((-1)**j*A[0][j]*det(tuple(tuple(row[k] for k in range(len(A)) if k != j) for row in A[1:])) for j in range(len(A)))

def form(A, a, b):
    return sum(a[i]*A[i][j]*b[j] for i in range(len(a)) for j in range(len(b)))

def stress(lam):
    return tuple(tuple(sum(F(lam[k], 2)*(P[k][i]*E[k][j]+P[k][j]*E[k][i]) for k in range(4)) for j in range(2)) for i in range(2))

E = tuple(sub(P[i+1], P[i]) for i in range(4))
q = tuple(p+(1,) for p in P)
assert __debug__
# Every other vertex lies strictly left of every directed polygon edge.
slacks = tuple(cross(sub(P[(i+1)%5], P[i]), sub(P[j], P[i])) for i in range(5) for j in range(5) if j not in (i, (i+1)%5))
assert min(slacks) > 0
rays = ((1, 1, 0, 2), (9, 0, 4, 2))
for lam in rays+(WEIGHTS,):
    assert all(x >= 0 for x in lam)
    assert tuple(sum(lam[k]*E[k][j] for k in range(4)) for j in range(2)) == (0, 0)
S1, S2 = (stress(lam) for lam in rays)
assert S1 == ((4, 3), (3, -20)) and S2 == ((-28, -29), (-29, -4))
assert det(S1) == -89 and det(S2) == -729
Q = ((20, 23), (23, 44))
assert stress(WEIGHTS) == tuple(tuple(-x for x in row) for row in Q)
assert Q[0][0] > 0 and det(Q) == 351 > 0
# Explicit sum-of-squares: x^T Q x=20(x+23y/20)^2+351y^2/20.
assert F(23*23+351, 20) == 44
witnesses = []
for omitted, N in enumerate(METRICS):
    minors = [det(tuple(tuple(row[j] for j in range(k)) for row in N[:k])) for k in (1, 2, 3)]
    assert min(minors) > 0
    D = [form(N, q[i], sub(q[i+1], q[i])) for i in range(4)]
    assert all(D[i] > 0 for i in range(4) if i != omitted)
    H = tuple(tuple(row[j] for j in range(2)) for row in N[:2])
    assert dot(WEIGHTS, D) == -sum(H[i][j]*Q[i][j] for i in range(2) for j in range(2))
    witnesses.append(dict(omitted=omitted, metric=N, leading_minors=minors, arrows=D))
assert [x['arrows'] for x in witnesses] == [[-40, 4, 77, 10], [4, -92, 1, 2], [2, 4, -91, 1], [2, 36, 1, -27]]
report = dict(identity='PENTAGON_MINIMAL_FOUR_ARROW_OBSTRUCTION_V1', points=P, edges=E, convexity_slacks=slacks, weights=WEIGHTS, stress=Q, stress_determinant=det(Q), circuit_matrices=[[[int(x) for x in row] for row in S] for S in (S1, S2)], pencil_determinant_power=[-89, 896, -1536], witnesses=witnesses)
data = (json.dumps(report, sort_keys=True, indent=2)+'\n').encode('utf-8')
path = Path('pentagon_joint_report.json')
path.write_bytes(data)
print('PENTAGON_FOUR_ARROWS_ALL_PROPER_SUBSETS_STRICT_PASS')
for p in (Path(__file__), path):
    b = p.read_bytes()
    print(p.name, len(b), hashlib.sha256(b).hexdigest())
print('Python', sys.version.split()[0])
```
