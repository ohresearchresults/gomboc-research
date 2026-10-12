# figure-0625

AI research report · 2026-09-29 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# VC47E — metric-aware finite cut gates on the actual H25 geometry

Branch: `[internal-source-reference]`.
Literal parent: `figure-0624`, SHA-256 `986478eff819f6a6a1920f08ce3c1bb2714b9b4e3c4015c8b0cba5ac4b0ab9aa`.

## 1. Result and evidence boundary

**No new own110 endpoint or newly audited nonwinner is established in this continuation.** The new mathematical result is a finite extension of the H25 cut obstruction that allows a genuine common affine deformation, evaluates admissible cuts at the **actual new uniform centroid**, and does not preserve either old unstable-vertex label.

Two concrete conclusions are proved below.

1. For an arbitrary invertible affine deformation with singular-value condition number at most **11/10**, and actual-centre displacement at most **1/200 in the pulled-back infinity norm**, every successful U1 cutting construction must remove at least one of two explicit, centre-dependent interior probe points. Retaining both forces two strict unstable vertices, regardless of the number or directions of the cuts.
2. If every new cutting normal belongs to the convex hull of the diameter balls of the **affinely transformed old polar normals, normalized at the actual new centroid**, then condition number at most **31/30** and the same centre cube force at least two strict unstable vertices automatically. This permits arbitrarily many cuts, retirement of old facets, and unstable-carrier turnover.

The second statement is not obtained by incorrectly treating Euclidean diameter balls as affine-invariant. Its proof explicitly bounds the transformed ball supports. It therefore covers a larger physical family than the parent's Euclidean old-safe-cut theorem.

These are geometric exclusions evaluated at the homogeneous centroid, **not newly instantiated moment-capacity certificates**, not full affine-orbit exclusions, and not exclusions of independent old-normal motion or physical point additions. In particular, they do not invalidate the retained RELAY6 or LOW bodies, which are different literal geometries.

The new theorem is established analytically from the parent's certified exact inequalities and the rational calculations displayed here. **The new verifier below was not observed completing in this turn.** Subsequent computational attempts at free-normal continuation, rooted-chord deformation, and primal-forest mass closure did not return inspectable scientific terminal results here. I do not count their possible checkpoints, stages, failures, or optimizer messages as new evidence, and I do not infer that previously supplied files were lost.

## 2. Reading and unchanged starting objects

The retained reading record covers the complete supplied `research-journal.md` through EOF,2289 lines, including the literal parent and its publication correction. The supplied journal identity is453403 bytes, SHA-256

```
1637e1c882549bbc9dbece109155850cadcd3fee0d0c85c7cd57853c732a18a9
```

The construction used in this proof is specifically **VC47D_MASSFLOW_H25_G6**, not its G5 sibling, LOW, or RELAY6. Its accepted parent census remains

```
V/E/F = 46/69/25
own strict S/U/H = 1/2/1
additional weak = 0/0/0
P = [0.8213375351217899...]
Q = []
```

Its actual uniform volume is approximately12.10563949190349, and its actual centroid is approximately

```
g0 = ( 8.853034480479272e-7,
      -5.266324988418889e-7,
       4.696127000691678e-7 ).
```

The proof uses the exact integrated g0, never zero or those rounded display coordinates. The current parent P component has23 vertices and21 true crossings; the parent's529 negative global outgoing chords are not recounted as a new result here.

The H25 input retains its60 arbitrary-new-halfspace allowance under F<=85/E<=249. The new exclusions below apply independently of that budget. The previously audited RELAY6_H31_G8 remains58/87/31, own121/weak000, P approximately0.6680789798466709 and Q empty. No later numerical checkpoint is promoted by this handoff.

The parent's newly assembled aggregate wrapper remains an **unobserved aggregate replay**. Its explicit G5 assertion correction remains necessary when that wrapper is used. The G6-only verifier in this handoff does not invoke that wrapper or its G5 assertion.

## 3. Exact premises on the literal H25 body

Let K be the raw25-halfspace G6 body and let K0=K-g0. Write its exact own-centred polar normals as

```
q_i = N_i / (1000000 - N_i.g0).
```

Use the following rational constants and vectors:

```
B = 23/10
H = 1573/1000
R = 351/250
L = 13/8
ell = (345,-853,392)

a = (-656511,1136725,-921033)/1000000
b = (897794,-973423,849384)/1000000.
```

The parent's exact cut-gate certificate supplies these premises:

- Every q_i has L1 norm strictly below B.
- For v=a and v=b, every old q_i satisfies

  ```
  2-q_i.v > 0,
  (2-q_i.v)^2 > |q_i|^2 |v|^2.
  ```

  These50 strict rational tests say that the support of every old diameter ball in either probe direction is below1.
- Both probe lengths exceed H, and ell.a<0<ell.b.
- Every point x of the complete old-body strip

  ```
  x in K0,
  |ell.x| <= ||ell||_1/32
  ```

  has |x|<R. The certificate checks all42 strip-vertex candidates obtained from old vertices and true-edge intersections with the two strip boundaries.

The additional upper bound used here is

```
|a| < L,   |b| < L.
```

It is elementary exact arithmetic, not a numerical nomination. For example,

```
|a|^2 = 2571452205835 / 1000000000000
|b|^2 = 2475039582821 / 1000000000000,
```

and both are less than169/64=L^2. Both also exceed2474329/1000000=H^2. The source below checks these identities directly.

These premises concern this exact G6 body. No corresponding premise is assumed for G5, LOW or RELAY6 without a separate check.

## 4. Common affine deformation and actual-centre normalization

Let A be any invertible real3-by-3 matrix, and let z0 be any translation. The affinely transformed parent is

```
K_A = z0 + A K0.
```

It is filled uniformly. Its own centroid is z0 by change of variables. Let P be a full-dimensional uniformly filled convex polyhedron contained in K_A, with its own actual centroid c. Define

```
delta = A^(-1)(c-z0),
kappa = sigma_max(A)/sigma_min(A).
```

The centre hypothesis below is on delta, not on c in arbitrary world units. It is invariant under a common dilation of the affine image.

For ||delta||_infinity<=epsilon with epsilon<=1/32, the old polar normals at the displaced pulled-back centre are

```
q_i(delta) = q_i/(1-q_i.delta).
```

All denominators are positive, since

```
1-q_i.delta > 1-B*epsilon.
```

The corresponding old polar normals in the physical affine image, centred at c, are

```
q_i^A(c) = A^(-T) q_i(delta).
```

This is the correct physical normalization. In particular, the subsequent cut conditions are not imposed at the obsolete parent centre z0.

### A separating section in the affine image

Consider the plane through c defined by

```
ell.A^(-1)(z-c)=0.
```

For a point z=z0+A x in K_A on this plane, ell.x=ell.delta. Thus x belongs to the old certified strip whenever epsilon<=1/32. Consequently

```
|z-c| < sigma_max(A) * (R + 7*epsilon/4).
```

The use of7/4 is the strict rational upper bound sqrt(3)<7/4. No sampled affine matrix or sampled section direction enters this argument.

### Two retained probes force two strict U

For any positive lambda, suppose P contains both

```
p_a = c + A(lambda*a),
p_b = c + A(lambda*b).
```

They lie on opposite sides of the separating plane. Each has distance from c strictly greater than

```
sigma_min(A) * lambda*H.
```

Therefore the sufficient condition

```
lambda*H > kappa*(R+7*epsilon/4)                 (1)
```

forces a strict unstable vertex in each half of P.

Here is the strictness argument. The maximum of squared distance on either closed half-polytope cannot occur on its separating section, because the corresponding retained probe is farther away. Let u be a maximizer away from that section. For any other point v of P, a sufficiently short initial part of the segment u--v remains in the same open half. If (u-c).(v-u) were nonnegative, squared distance would increase on that initial segment, including the case of zero first derivative because the quadratic term is positive. Hence

```
(u-c).(v-u) < 0  for every v in P other than u.
```

This is exactly the strict radial-maximum condition used by the equilibrium census. The two halves give two distinct strict U. No old U label, old unstable star, current saddle label, or stable-facet label is required to survive.

## 5. First finite gate: arbitrary cuts with mandatory horn retirement

Take

```
epsilon = 1/200,
kappa <= 11/10,
s = 1-B*epsilon = 1977/2000.
```

Both points

```
p_a = c + A(s*a),
p_b = c + A(s*b)
```

belong to the interior of the uncut affine parent K_A. To see this, the old normalized normals at delta are positive radial scalings of the old q_i by factors below1/s. The original strict diameter-ball support tests therefore put delta+s*a and delta+s*b inside K0.

For these two probes, condition(1) holds with the exact positive gap

```
s*H - (11/10)*(R+7/(4*200))
    = 1771/2000000 > 0.
```

**Theorem A.** For every such A and every full-dimensional homogeneous convex polyhedron P contained in K_A, if its actual pulled-back centroid satisfies ||delta||_infinity<=1/200 and it retains both displayed probes, then P has at least two strict unstable vertices.

This permits arbitrary cutting directions, arbitrary numbers of cuts, old-facet retirement and all other incidence changes. It imposes no S or H count and no edge bound.

### An explicit necessary disjunction for a candidate construction

Suppose P is obtained by additional halfspaces, normalized at its actual centre as

```
w_j.(z-c) <= 1.
```

Any ownU1 endpoint in Theorem A's affine/centre range must satisfy at least one of

```
max_j w_j.A(s*a) > 1,
max_j w_j.A(s*b) > 1.                           (2)
```

The old parent inequalities cannot cause these violations, since both probes lie inside K_A. Thus at least one genuinely new cut must retire one of these two high-region probes. This is a finite, label-independent necessary test on the complete cutting construction. It is stronger than asking whether the old U4 or U8 point was removed, but it is not sufficient for P cancellation: replacement maxima and new positive bars can remain.

The condition-number restriction is intrinsic. It allows arbitrary rotations, reflections and common scales. In terms of G=A^T A, it is the eigenvalue-ratio bound lambda_max(G)/lambda_min(G)<=121/100, not a bound on the entries of A-I.

## 6. Second finite gate: diameter-safe cuts after the affine deformation

The affine image of a Euclidean diameter ball is generally an ellipsoid. Therefore the parent's Euclidean theorem cannot simply be transported while continuing to call the transformed controller region a union of Euclidean balls.

Define the actual image-space controller region correctly:

```
Gamma(A,delta) = conv union_i D(q_i^A(c)),
D(q) = {w : |w-q/2| <= |q|/2}.
```

Every new normalized cut normal is now permitted to lie anywhere in Gamma, including convex mixtures of points from different diameter balls.

For v=a or b, its support in the physical direction A v satisfies

```
h_Gamma(A v)
 = max_i [q_i(delta).v
          + |A^(-T)q_i(delta)| |A v|]/2
 <= max_i [q_i(delta).v
          + kappa |q_i(delta)| |v|]/2
 < [1 + (kappa-1)*B*L/2] / (1-B*epsilon).       (3)
```

The last step uses the exact original diameter-ball support inequalities, |v|<L, and |q_i|<B. It also uses positivity of the radial scaling factors when the centre changes. This is the step that accommodates Euclidean safety in the **new affine image**, rather than safety only before deformation.

Set

```
C = B*L/2 = 299/160,
alpha = (1-B*epsilon)/(1+C*(kappa-1)).
```

Equation(3) proves that every cut with normal in Gamma strictly retains both

```
c+A(alpha*a),  c+A(alpha*b).
```

The same is true for all old inequalities, because each old polar normal is an endpoint of one of the diameter balls.

Now take the concrete rectangle

```
||delta||_infinity <= 1/200,
kappa_2(A) <= 31/30.
```

Using the worst corner of this rectangle gives

```
alpha = 23724/25495,

alpha*H - (31/30)*(R+7/(4*200))
  = 2380529/611880000 > 0.                     (4)
```

**Theorem B.** Within that affine/actual-centre range, any number of additional cuts whose actual-centred normalized normals lie in Gamma(A,delta) leaves at least two strict unstable vertices. Therefore no such body is own110, with or without an edge-budget restriction.

The theorem does not assume preservation of the original stable support, either original unstable vertex, or a particular positive witness tree. It does not require every controller to lie in one particular old diameter ball: the entire convex hull of their union is allowed.

### Further exact tradeoffs from the same proof

The general sufficient inequality is

```
(1-B*epsilon)*H
 > kappa*(1+C*(kappa-1))*(R+7*epsilon/4),
0<=epsilon<=1/32, kappa>=1.                    (5)
```

Its left side decreases with epsilon and its right side increases with both parameters. Thus checking the upper corner certifies the entire corresponding parameter rectangle, not only a single affine map.

Two additional exact choices are:

| Actual pulled-back centre bound | Affine condition-number bound | Retained probe scale | Positive normalized radial gap |
|---|---:|---:|---:|
| epsilon=0 | 26/25 | 4000/4299 | 46163/13434375 |
| epsilon<=1/100 | 41/40 | 31264/33495 | 1199363/107184000 |

At kappa=1 and epsilon=1/32 the same formula recovers the parent's scale297/320 and gap401/320000. The new result is the simultaneous metric/centre/cut extension, not another claim to have discovered that original gate.

These rectangles are sufficient bounds from the displayed estimates. They are not maximal affine regions, maximal centroid chambers, or attained physical mass-controller capacities.

## 7. What this changes in the construction strategy

Spending H25's60 available support slots on old-diameter-safe controllers cannot be rescued merely by a modest common anisotropy, a rotation of coordinates, or a small physically realized centre shift inside Theorem B's range. Safety must be evaluated after the affine deformation; inequality(3) shows why this larger interpretation remains obstructed.

Theorem A supplies a broader early test even after abandoning that safety policy: an arbitrary-cut candidate in its range must actually retire at least one of the two explicit high-region probes. It need not cut both. Freezing two opposed first planes by default is therefore stronger than this necessary geometry demands and can impose an avoidable mass burden, as the parent's separate mandatory-two-cut theorem illustrates.

A useful next finite construction is consequently **one-probe retirement coupled from the outset to free old-normal or mass geometry**, with the second probe permitted to survive and with all new P/Q recomputed. The goal is not to keep the old U labels, nor to restore an obsolete centre after freezing a severe two-sided cut. A candidate that passes the probe test still needs a complete exact own-centroid census; the disjunction is necessary, not an acceptance test.

Independent old-normal motion, point additions, condition numbers or centre changes outside the certified rectangles, and new cut normals outside Gamma remain legitimate escapes. The retained RELAY6 and LOW geometries must be evaluated on their own current boundaries; this G6 theorem is not silently transferred to them.

## 8. Complete exact verification source

The source below contains all25 literal G6 rows, reconstructs the bounded H body through exact polarity, checks the complete maximal supporting surface and uniform mass, computes the full baseline strict/additional-weak census and every positive P/Q, re-establishes the parent's finite geometric premises, and checks every new rational constant.

It imports only these **unchanged, already supplied** source units from the original VC47 parent:

```
exact47.py
12245 bytes
SHA-256 14431f428ffce4d3c19bfae1671529790bd41a4d4bf06cdb2117a2e4edffa473

corridor47.py
literal6837-byte variant:
SHA-256 3cadf6a06219fb30f53cf08fad459b4ef57b9bfb289d61347e99f7c1d9b7c3a7

or its6836-byte descriptive-newline variant:
SHA-256 5d5187a462c9b8bab978772b284ba6180ea4a187d619c7b6db4e288071e2130e
```

Their complete source authority is `figure-0617`, SHA-256 `d9a82a95edfca7994e63592a49a9c42dd4113255ce843f8920fdaf699e717f36`. No VC47B optimizer, later numerical checkpoint, NumPy, SciPy, Torch or C622 material is required for this verifier.

Save as `VC47E_AFFINE_CUT_GATE.py` and run, with assertions enabled:

```
python -B -S VC47E_AFFINE_CUT_GATE.py VC47E_OUT
```

The intended terminal marker is

```
VC47E_METRIC_AWARE_TWO_HORN_GATES_EXACT_PASS_NO_110 50 42 4
```

**That marker is prospective here, not an observed execution receipt.** The mathematical proof above rests on the parent's accepted exact premises and the displayed rational identities. No new source-file byte count, source hash, output hash or cold-replay claim is invented. The program measures and emits those identities when executed.

```python
"""VC47E: metric-aware finite cut gates on literal MASSFLOW_H25_G6.
Exact arithmetic only. This publication unit has no observed run receipt here.
Requires the two unchanged original sources exact47.py and corridor47.py.
"""
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import exact47 as E
import corridor47 as C

if not __debug__:
    raise RuntimeError('Run with assertions enabled; do not use -O.')
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

PARENT_ID = 'figure-0624'
PARENT_SHA = '986478eff819f6a6a1920f08ce3c1bb2714b9b4e3c4015c8b0cba5ac4b0ab9aa'
INPUT_SHA = 'e325553cfe5c21dfe121045e50794b1d368846df67f15e97b47aabe6534825ae'
ZERO = E.ZERO
D = 10**6
ROWS = [
 [-706475,-1007381,-557299],[-108094,233930,-210708],
 [529867,458284,-491462],[672649,143839,-630916],
 [850650,-77402,-334849],[-136148,-859574,-809840],
 [225327,-675131,-859774],[699823,-220640,-685199],
 [502490,-457091,-810768],[753457,258215,-287910],
 [398517,551217,344455],[465203,389617,654277],
 [260202,653664,642937],[-47259,801671,617053],
 [-209307,694247,744382],[-380429,551246,829788],
 [-545673,377410,869656],[-699725,205615,847693],
 [-844114,38064,769303],[-961841,-143308,649279],
 [-1029979,-335126,506222],[-1062491,-497530,332853],
 [-1053085,-615922,186367],[-1010792,-745264,-1264],
 [-916205,-873384,-230293]
]
HORNS = [
 tuple(Q(v,D) for v in (-656511,1136725,-921033)),
 tuple(Q(v,D) for v in (897794,-973423,849384))
]
ELL = (345,-853,392)
B = Q(23,10)
H = Q(1573,1000)
R = Q(351,250)
L = Q(13,8)
CBALL = B*L/2


def encoded(obj):
    return (json.dumps(E.encode(obj),sort_keys=True,indent=2)+'\n').encode()


def authenticate_dependencies():
    allowed = {
      'exact47.py': {
        '14431f428ffce4d3c19bfae1671529790bd41a4d4bf06cdb2117a2e4edffa473'
      },
      'corridor47.py': {
        '3cadf6a06219fb30f53cf08fad459b4ef57b9bfb289d61347e99f7c1d9b7c3a7',
        '5d5187a462c9b8bab978772b284ba6180ea4a187d619c7b6db4e288071e2130e'
      }
    }
    receipts = {}
    for name,module in [('exact47.py',E),('corridor47.py',C)]:
        data = Path(module.__file__).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        assert digest in allowed[name], (name,digest)
        receipts[name] = dict(bytes=len(data),sha256=digest)
    return receipts


def physical_from_normals(normals):
    dual_faces = E.hull(normals)
    vertices = []
    for f in dual_faces:
        n = E.normal(normals,f)
        h = E.dot(n,normals[f[0]])
        assert h > 0
        vertices.append(E.mul(1/h,n))
    assert len(set(vertices)) == len(vertices)
    active = sorted({i for f in dual_faces for i in f})
    pairs = []
    for i in active:
        ids = [j for j,f in enumerate(dual_faces) if i in f]
        assert len(ids) >= 3
        pairs.append((E.cycle(ids,vertices,normals[i]),i))
    pairs.sort(key=lambda z:tuple(sorted(z[0])))
    faces = [f for f,i in pairs]
    assert all(E.dot(n,x) <= 1 for n in normals for x in vertices)
    for f,i in pairs:
        assert all(E.dot(normals[i],vertices[j]) == 1 for j in f)
    volume,moment = C.check_surface(vertices,faces)
    audit = E.audit(vertices,faces)
    assert (audit['volume'],audit['first_moment']) == (volume,moment)
    assert C.flux_moment(vertices,faces) == moment
    centred = [E.sub(x,audit['centroid']) for x in vertices]
    assert E.mass(centred,faces) == (volume,ZERO)
    audit['active_submitted_normals'] = active
    audit['face_to_submitted_normal'] = [i for f,i in pairs]
    audit['vertices_exact'] = vertices
    return vertices,faces,audit


def strip_vertices(points,faces,width):
    heights = [E.dot(ELL,x) for x in points]
    candidates = [x for x,h in zip(points,heights) if abs(h) <= width]
    for sign in (-1,1):
        for i,j in E.edges(faces):
            a = heights[i]-sign*width
            b = heights[j]-sign*width
            if a*b < 0:
                point = E.mul(1/(a-b),
                    E.sub(E.mul(a,points[j]),E.mul(b,points[i])))
                assert E.dot(ELL,point) == sign*width
                candidates.append(point)
    return candidates


def safe_case(epsilon,kappa,expected_scale,expected_gap):
    assert 0 <= epsilon <= Q(1,32) and kappa >= 1
    s = 1-B*epsilon
    denominator = 1+CBALL*(kappa-1)
    alpha = s/denominator
    gap = alpha*H-kappa*(R+Q(7,4)*epsilon)
    assert s > 0 and denominator >= 1
    assert alpha == expected_scale
    assert gap == expected_gap and gap > 0
    # The support inflation and radial separation are monotone in epsilon
    # and kappa. The upper corner therefore covers the entire rectangle.
    return dict(kind='image-space old-diameter-safe cuts',
      centre_infinity_radius=epsilon,
      singular_value_condition_number_upper=kappa,
      metric_eigenvalue_ratio_upper=kappa*kappa,
      probe_scale=alpha,normalised_radial_gap=gap,
      probe_offsets=[E.mul(alpha,a) for a in HORNS],
      scope='Any number of cuts; no retained equilibrium labels or E bound')


def main(destination):
    receipts = authenticate_dependencies()
    output = Path(destination)
    output.mkdir(parents=True,exist_ok=True)
    manifest = {}
    def save(name,obj):
        data = encoded(obj)
        (output/name).write_bytes(data)
        manifest[name] = dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())

    input_object = dict(denominator=D,normals=ROWS,
                        inequality='n.x<=denominator')
    input_bytes = encoded(input_object)
    assert len(input_bytes) == 1473
    assert hashlib.sha256(input_bytes).hexdigest() == INPUT_SHA
    save('MASSFLOW_H25_G6.input.json',input_object)
    normals = [tuple(Q(v,D) for v in row) for row in ROWS]
    vertices,faces,baseline = physical_from_normals(normals)
    assert [baseline[k] for k in ('V','E','F')] == [46,69,25]
    assert baseline['strict'] == [1,2,1]
    assert baseline['weak'] == [0,0,0]
    assert len(baseline['P']) == 1 and not baseline['Q']
    assert baseline['active_submitted_normals'] == list(range(25))
    g0 = baseline['centroid']
    points = [E.sub(x,g0) for x in vertices]
    q = [E.mul(1/(1-E.dot(n,g0)),n) for n in normals]
    assert max(sum(abs(t) for t in n) for n in q) < B
    baseline['global_directed_chord_zero_counts'] = [
      sum(E.dot(a,E.sub(b,a)) == 0
          for i,a in enumerate(z) for j,b in enumerate(z) if i != j)
      for z in (points,baseline['poles'])
    ]
    assert baseline['global_directed_chord_zero_counts'] == [0,0]
    save('H25_BASELINE_EXACT.json',baseline)

    expected_squared_lengths = [
      Q(2571452205835,10**12),Q(2475039582821,10**12)
    ]
    ball_tests = []
    for k,a in enumerate(HORNS):
        a2 = E.dot(a,a)
        assert a2 == expected_squared_lengths[k]
        assert H*H < a2 < L*L
        for i,n in enumerate(q):
            t = 2-E.dot(n,a)
            gap = t*t-E.dot(n,n)*a2
            assert t > 0 and gap > 0
            ball_tests.append(dict(horn=k,normal=i,
                                   positive_term=t,squared_gap=gap))
    assert len(ball_tests) == 50
    assert E.dot(ELL,HORNS[0]) < 0 < E.dot(ELL,HORNS[1])
    width = Q(1,32)*sum(abs(t) for t in ELL)
    strip = strip_vertices(points,faces,width)
    assert len(strip) == 42
    maximum_radius2 = max(E.dot(x,x) for x in strip)
    assert maximum_radius2 < R*R
    assert CBALL == Q(299,160)

    epsilon = Q(1,200)
    kappa = Q(11,10)
    s = 1-B*epsilon
    retention_gap = s*H-kappa*(R+Q(7,4)*epsilon)
    assert s == Q(1977,2000)
    assert retention_gap == Q(1771,2000000) > 0
    arbitrary_cut_gate = dict(
      kind='arbitrary cuts, conditional on retaining both probes',
      centre_infinity_radius=epsilon,
      singular_value_condition_number_upper=kappa,
      metric_eigenvalue_ratio_upper=kappa*kappa,
      probe_scale=s,normalised_radial_gap=retention_gap,
      probe_offsets=[E.mul(s,a) for a in HORNS],
      necessary_U1_disjunction='Some new actual-centred cut strictly violates at least one probe')

    safe_rectangles = [
      safe_case(Q(1,200),Q(31,30),Q(23724,25495),
                Q(2380529,611880000)),
      safe_case(Q(0),Q(26,25),Q(4000,4299),
                Q(46163,13434375)),
      safe_case(Q(1,100),Q(41,40),Q(31264,33495),
                Q(1199363,107184000)),
      safe_case(Q(1,32),Q(1),Q(297,320),Q(401,320000))
    ]
    source = Path(__file__).read_bytes()
    certificate = dict(
      source_parent=PARENT_ID,source_parent_sha256=PARENT_SHA,
      input_sha256=INPUT_SHA,dependencies=receipts,
      source_bytes=len(source),source_sha256=hashlib.sha256(source).hexdigest(),
      actual_parent_centroid=g0,actual_parent_volume=baseline['volume'],
      constants=dict(B=B,H=H,R=R,L=L,ball_inflation_coefficient=CBALL),
      horns=HORNS,separating_covector=ELL,
      old_diameter_ball_tests=ball_tests,
      old_strip_width=width,old_strip_vertices=strip,
      old_strip_maximum_radius_squared=maximum_radius2,
      arbitrary_cut_gate=arbitrary_cut_gate,
      safe_cut_rectangles=safe_rectangles,
      conclusion='At least two strict U in each stated family; no full-family S/H count asserted',
      exclusions_not_claimed=[
        'independent changes of old normal directions or offsets',
        'physical additions outside the affine parent',
        'arbitrary larger affine condition numbers or centre displacements',
        'different literal G5, LOW or RELAY6 starting bodies'
      ])
    save('VC47E_AFFINE_CUT_GATES_EXACT.json',certificate)
    (output/'MANIFEST.json').write_bytes(encoded(manifest))
    print('VC47E_METRIC_AWARE_TWO_HORN_GATES_EXACT_PASS_NO_110',
          len(ball_tests),len(strip),len(safe_rectangles),flush=True)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv)>1 else 'VC47E_OUT')
```

## 9. Handoff boundary

The new durable mathematical content is the metric-aware support bound(3), the arbitrary-cut two-probe retirement gate with condition number11/10, and the actual-image diameter-safe-cut exclusion with condition number31/30 and explicit positive rational gaps. Their full hypotheses, exact starting input, proof and verification source are above.

No uninspectable numerical run is reported as a successful construction, a completed search family, a negative experimental finding, or an exact audit. No new H31/H39 or later relay array is inferred from a possible file. The accepted VC47D bodies and their existing exact evidence remain unchanged.

The remaining constructive task is still actual whole-P cancellation with S1 retained or restored. The new gates isolate a concrete necessary geometric departure without claiming that departure is sufficient, and without converting the old safe-cut policy into a restriction on all admissible research directions.
