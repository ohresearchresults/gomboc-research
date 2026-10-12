# figure-0417

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Sharp Raven 82 — finite projective mass elimination and the remaining mechanical construction

Branch: `[internal-source-reference]`.

## 1. Result and evidence boundary

**No new own-centroid strict110/weak000 body is promoted in this handoff.** The durable parent remains `figure-0408`, envelope SHA-256 `453103684cdd65de7d9e14e86546b7b8cce94c0f1fa36ebe32c50273d773ecf7`.

The substantive continuation is a **finite physical mass-elimination mechanism**. For a convex homogeneous polyhedron and a specified interior reference point, the three ordinary centroid equations can be solved globally and uniquely within its origin-fixing projective family. This does not require a nearly singular centroid ray, a fixed stable root, or fixed escape witnesses. The entire maximal face lattice and edge count are preserved. Moreover, every mechanical equilibrium predicate at the chosen reference becomes affine in the three projective parameters.

The useful consequences are:

* Ordinary mass closure can be an inner, strictly convex problem, rather than a fragile constraint imposed on every outer shape step.
* Three common-normal-translation directions are exact redundant directions after this inner normalization. An outer optimizer should not spend iterations on them.
* A certified non110 census at the unique mass-normalizing parameter would exclude **all root and witness choices in this particular fixed-reference centering slice**, not merely an old selected witness packet. It would not exclude arbitrary own-centroid projective images, other reference points, or other shapes.

The arguments below establish these statements directly from filled-volume tetrahedron integrals. I make no novelty claim for the underlying polar-volume centering theorem.

### Execution limitation

The latest tool calls in this continuation did not return readable execution receipts; their visible responses were `Skipped …` placeholders. Thus I cannot substantiate their completion, inspect their current outputs, or safely quote new output hashes or equilibrium counts from them. In particular, the newly issued projective certificate and optimizer calls are **not treated as completed verifications here**.

The complete journal and literal parent had been read in the carried context. The parent itself supplies the complete44-source recovery, independent A/B auditors, separate centered-mass integration, and the exact seven-body inputs. Its source closure remains the starting authority. 

The runnable unit below is a complete durable method addition to that literally supplied parent. It does not depend on the unreadable numerical outputs, an optimizer checkpoint, a sandbox download, or an external research library. It is not presented as an observed successful replay.

## 2. A finite, genuinely homogeneous mass controller

Let the selected reference point be translated to0. Write the full-dimensional convex polyhedron as

\[
P=\{x:q_f\cdot x\leq1\},\qquad 0\in\operatorname{int}P,
\]

with its actual maximal facets, and let its vertices be \(x_i\).

For

\[
\mathcal D=\{a\in\mathbb R^3:1+a\cdot x_i>0\text{ for every }i\},
\]

define

\[
T_a(x)=\frac{x}{1+a\cdot x},\qquad K_a=T_a(P).
\]

This is a finite change of the material boundary. The target \(K_a\) is filled with **uniform ordinary volume density**. It is not the old body with a moved reference point, and it is not the push-forward of the old density.

Because the denominator is positive on the entire convex body, this projective map preserves convexity, supporting incidences and the complete face lattice. In particular,

\[
V(K_a)=V(P),\quad E(K_a)=E(P),\quad F(K_a)=F(P)
\]

when these letters denote combinatorial counts. To avoid confusion, write the ordinary volume as \(\mathcal V(a)\).

The transformed maximal support inequality is particularly simple:

\[
(q_f+a)\cdot y\leq1.
\]

Thus the transformation changes every normalized normal by the same vector, without requiring contact subdivision or additional edges. Applied to `MASS_NEAR_EXACT`, the whole admissible family retains174 vertices,308 edges and136 maximal facets. Its parent own census is35/25/58, not110. 

### 2.1 Actual filled-volume formulas

Triangulate the maximal facet boundaries with outward orientation and cone them to0. For a positive source tetrahedron with nonzero vertices \(x_i,x_j,x_k\), put

\[
v_t=\det(x_i,x_j,x_k)/6>0,\qquad d_i=1+a\cdot x_i,
\]

\[
y_i=x_i/d_i,\qquad v_t(a)=v_t/(d_i d_j d_k).
\]

Then the actual target volume and first moment are

\[
\mathcal V(a)=\sum_t v_t(a),\qquad
M(a)=\frac14\sum_t v_t(a)(y_i+y_j+y_k).
\]

These are ordinary integrals over the newly filled target tetrahedra. Direct differentiation gives

\[
\nabla_a\mathcal V(a)=-4M(a).
\]

Writing \(s_t=y_i+y_j+y_k\), its Hessian is

\[
\nabla_a^2\mathcal V(a)=
\sum_t v_t(a)\left(s_ts_t^T+y_iy_i^T+y_jy_j^T+y_ky_k^T\right)
=20\int_{K_a} yy^T\,dy.
\]

Consequently, for every nonzero vector \(z\),

\[
z^T\nabla_a^2\mathcal V(a)z
=20\int_{K_a}(z\cdot y)^2\,dy>0.
\]

The strict inequality uses genuine three-dimensional filled volume. It is not a rank observation at one numerical checkpoint.

### 2.2 Global existence and uniqueness of mass closure

The domain \(\mathcal D\) is bounded because0 is interior to \(P\); its closure is the negative polar polytope. As \(a\) approaches its boundary, at least one vertex denominator tends to0. A positive tetrahedron incident to that vertex has volume \(v_t/(d_i d_j d_k)\) tending to infinity, since the other denominators remain bounded above on the compact parameter closure. Hence

\[
\mathcal V(a)\longrightarrow+\infty
\quad\text{at}\quad\partial\mathcal D.
\]

Strict convexity and this boundary divergence imply that \(\mathcal V\) has one and only one minimizer \(a_*\in\mathcal D\). At that point

\[
M(a_*)=0,\qquad g(K_{a_*})=0.
\]

**Every specified interior reference therefore admits a unique finite origin-fixing projective mass correction.** There is no need to infer this from a successful Newton trajectory. Newton iteration is only a way to locate the parameter whose existence and uniqueness are already established.

For rational source geometry, the three equations \(M(a)=0\) are rational equations. Clearing the positive product \(\prod_i d_i^2\) gives three polynomial equations. Together with an isolating parameter box, these define a recoverable isolated-algebraic physical body. The coordinates are \(x_i/(1+a_*\cdot x_i)\), and the original maximal incidence is retained exactly.

## 3. Complete mechanics are affine in the projective parameter

Mass closure does **not** preserve reference110 automatically. It must be checked on the newly filled body. The following formulas allow that check without freezing the old roots or witnesses.

### 3.1 Unstable vertices

For distinct source vertices define

\[
R_{ij}(a)=\|x_i\|^2-x_i\cdot x_j
+a\cdot\left(\|x_i\|^2x_j-(x_i\cdot x_j)x_i\right).
\]

Because the denominators are positive,

\[
\operatorname{sign}R_{ij}(a)
=\operatorname{sign}\bigl[-y_i\cdot(y_j-y_i)\bigr].
\]

Thus vertex \(i\) is strictly unstable at0 exactly when all its incident \(R_{ij}\) are positive. Testing every other vertex gives an independent complete normal-cone test. It is weak-only when the required forms are all nonnegative and at least one is zero.

### 3.2 Stable facets

For two maximal supports define

\[
S_{fj}(a)=(q_f+a)\cdot(q_f-q_j).
\]

The perpendicular foot on facet \(f\) is

\[
p_f=(q_f+a)/\|q_f+a\|^2.
\]

Its strict containment in the other support inequalities is exactly \(S_{fj}(a)>0\). Adjacent facets suffice for a boundary-side implementation; all other supports give another complete implementation. Every \(S_{fj}\) is affine in \(a\).

### 3.3 True saddle edges and weak boundaries

Let true edge \(ij\) have adjacent facets \(f,k\). Its four strict saddle predicates, up to positive factors, are

\[
R_{ij}(a),\quad R_{ji}(a),\quad S_{kf}(a),\quad S_{fk}(a).
\]

The last two are the numerators of the two coefficients expressing the line-foot vector in the cone generated by \(q_f+a\) and \(q_k+a\). Their Gram determinant is positive for distinct adjacent maximal facets.

All four positive means a strict saddle. All four nonnegative with a zero means a weak-only saddle. An edge is neither precisely when at least one of these four forms is negative.

Therefore the complete strict/weak census at0 is determined by a finite rational affine arrangement in the three projective parameters. A rational interval enclosure of \(a_*\) can certify every feature, rather than just a selected escape graph. The program below additionally checks the same census using direct transformed-point projections and two-normal Gram-cone expressions.

### 3.4 Exact obstruction scope

Suppose a complete certificate shows that \(K_{a_*}\) is not110/weak000. Then no admissible \(T_a(P)\) can simultaneously have its filled centroid at0 and be110/weak000 there: mass closure forces \(a=a_*\).

This covers every root and every witness choice **within that fixed-reference centering slice**. It does not exclude a different \(T_a(P)\) that is110 about a nonzero own centroid. Nor does it exclude changing the source reference point, adding/removing material outside this projective family, or changing the supporting geometry in other ways. Replacing this scoped conclusion by a claim about the entire own-centroid projective orbit would be incorrect.

No such new body-specific exclusion is claimed completed in this response; its required readable certificate is presently unavailable.

## 4. How this changes the constructive architecture

Let an outer shape parameter be \(s\), with a full-dimensional admissible source \(P_s\). Define

\[
F(s,a)=\nabla_a\mathcal V_s(a).
\]

The inner solve is \(F(s,a_*(s))=0\). Wherever the outer description is differentiable, ordinary implicit differentiation gives

\[
\frac{da_*}{ds}
=-\left(\nabla_a^2\mathcal V_s(a_*)\right)^{-1}
\frac{\partial F}{\partial s}.
\]

Thus a shape step can be followed by a **complete finite mass restoration**, with a positive-definite three-dimensional inner Hessian. This replaces the earlier imposed direction \(Dg\,dz\propto-(g-c)\). It does not assume that a first-order centroid equation survives a finite topology change.

There is also an exact redundant direction. Since

\[
T_b\circ T_a=T_{a+b},
\]

replacing every normalized input normal \(q_f\) by \(q_f+b\), and then applying the unique mass normalization, yields the same normalized physical body. The new normalizer parameter is \(a_*-b\). These three common-normal-translation directions should be removed or fixed in an outer normal-coordinate optimization; they cannot improve mechanics after exact inner mass restoration.

For the explicitly released H61 family, outer changes can use its61 input supports and up to44 added supports under the sufficient105-support bound. Projective normalization adds no supports or edges. Retaining all98 old rows is a different family and does not have the same44-row allowance. 

The next substantive construction should therefore change the released supporting geometry or the selected reference, normalize its actual filled mass with this inner solve, and evaluate both complete mechanical landscapes. It should not merely repeat the already-crossed22→62 near gate or move in the three common-normal directions that normalization cancels exactly.

## 5. Recovery and verification status

### Authoritative input

The default reference used below is the parent's exact near point:

```text
(-290787037/1000000000,
 -270371541/1000000000,
 -68565859/250000000)
```

The default source is the parent's `MASS_NEAR_EXACT` report, whose exact A=B identity is:

```text
309669 bytes
SHA256 a6b1d7c7e83105113c4a385b9a8730bce560c56e17e649647fc2c1595d485cbf
```

The literal parent contains the complete source capsule with these identities:

```text
Normalized base64: 72364 characters
SHA256 1a443c8775608800a4ab12a288f8c88ae6888f0291611126c503eab9d39dff74

XZ: 54272 bytes
SHA256 39b6e511f77109f860dc79f5c7cea95c712f63b8004884dd4f65c5f5280a7888

Decoded UTF-8 JSON dictionary: 206113 bytes, 44 source files
SHA256 1b19dac3308a9bdb41921797bbfe8cfbce67a377525e8efdc82dc37613355414
```

### Complete method addition, not an observed output receipt

Save the source below as `FINITE_PROJECTIVE.py`. Its recovery closure is **the literal parent already supplied in this chat plus this complete source unit**. A fresh executor must receive that literal parent, not merely its ID or hash. The unit accepts either its base64 block or a Markdown journal containing that block.

The default command reconstructs and audits the exact parent mass body before performing the new inner normalization:

```sh
python -B -S FINITE_PROJECTIVE.py research-journal.md NEW_PROJECTIVE_WORK
```

For another explicitly supplied rational H-body:

```sh
python -B -S FINITE_PROJECTIVE.py PARENT.b64 NEW_PROJECTIVE_WORK --raw EXACT_INPUT.json --center cx,cy,cz
```

The three center entries are literal rational strings. The source body is independently audited before use. The output directory must be new. Assertions must remain enabled.

Dependencies are the Python3.13.5 standard library and the verified auditors decoded from the supplied parent. The new inner solve uses no NumPy, SciPy, RNG, numerical solver or external service. Its consequential parameters are224-bit outward dyadic intervals, a rational rounding grid10^48, at most80 Newton iterations, at most64 dyadic backtracks per iteration, and an isolating radius10^-32. Failure to establish a required interval sign or contraction is an unresolved computation, not an exclusion theorem.

A successful future replay writes the parameter box, exact mass-root equations through the source geometry, complete affine/direct feature signs, a separate changed-fan mass enclosure, the rational projective input, full parent A/B and centered-mass audit outputs for that rational input, and byte/hash receipts. **No terminal marker from that future replay is claimed observed here.**

The exact zero first moment of the isolated-algebraic representative follows from the certified root equations \(F=-4M=0\). The changed-fan interval integration is an independent enclosure check; containment of0 in an interval is not itself an exact-zero proof. The rational nearby representative instead receives the ordinary exact filled-centroid A/B audits and the parent's separate exact centered-mass integration.

### Other interrupted constructions

The carried interrupted-work summary records a changed19-support body with V34/E51/F19, own435/weak000, obtained by actual support deletion from H61. Its reported defining input is `PRUNE1/S4U3E51_a12380.json`, with reports under `EXACT_H19/`. The complete19 rows and readable current receipts were not recovered into this response. Consequently that body is **not exported as a durable successor here**; those exact rows remain a specific recovery dependency. A filename is not a substitute for them.

Later numerical orbit searches, rounded point descendants, and newly issued certificate calls likewise have no readable completion receipts in the present continuation. Their counts, completion limits and output hashes are not inferred or promoted.

## 6. Complete runnable source

```python
# FINITE_PROJECTIVE.py
# CPython 3.13.5, standard library only. Keep assertions enabled.
from fractions import Fraction as Q
from pathlib import Path
from math import gcd, lcm
import argparse, base64, hashlib, json, lzma, re, subprocess, sys

sys.set_int_max_str_digits(0)
BITS = 224
SCALE = 1 << BITS
GRID = 10 ** 48
RADIUS = Q(1, 10 ** 32)
PARENT_A_SHA = 'a6b1d7c7e83105113c4a385b9a8730bce560c56e17e649647fc2c1595d485cbf'
B64_SHA = '1a443c8775608800a4ab12a288f8c88ae6888f0291611126c503eab9d39dff74'
XZ_SHA = '39b6e511f77109f860dc79f5c7cea95c712f63b8004884dd4f65c5f5280a7888'
DICT_SHA = '1b19dac3308a9bdb41921797bbfe8cfbce67a377525e8efdc82dc37613355414'


def sha(b):
    return hashlib.sha256(b).hexdigest()


class I:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None, raw=False):
        if raw:
            self.lo, self.hi = int(lo), int(hi)
        else:
            lo = Q(lo)
            hi = lo if hi is None else Q(hi)
            self.lo = lo.numerator * SCALE // lo.denominator
            self.hi = -((-hi.numerator * SCALE) // hi.denominator)
        assert self.lo <= self.hi

    def __add__(a, b):
        b = b if isinstance(b, I) else I(b)
        return I(a.lo + b.lo, a.hi + b.hi, raw=True)

    __radd__ = __add__

    def __neg__(a):
        return I(-a.hi, -a.lo, raw=True)

    def __sub__(a, b):
        return a + (-b if isinstance(b, I) else -Q(b))

    def __rsub__(a, b):
        return I(b) + (-a)

    def __mul__(a, b):
        b = b if isinstance(b, I) else I(b)
        v = [a.lo*b.lo, a.lo*b.hi, a.hi*b.lo, a.hi*b.hi]
        return I(min(v)//SCALE, -((-max(v))//SCALE), raw=True)

    __rmul__ = __mul__

    def inv(a):
        assert a.lo > 0 or a.hi < 0, 'Division interval contains zero'
        return I(SCALE*SCALE//a.hi,
                 -((-SCALE*SCALE)//a.lo), raw=True)

    def __truediv__(a, b):
        return a * (b if isinstance(b, I) else I(b)).inv()

    def __rtruediv__(a, b):
        return I(b) * a.inv()

    def mid(a):
        return Q(a.lo+a.hi, 2*SCALE)

    def maxabs(a):
        return Q(max(abs(a.lo), abs(a.hi)), SCALE)

    def sign(a):
        if a.lo > 0:
            return 1
        if a.hi < 0:
            return -1
        if a.lo == a.hi == 0:
            return 0
        raise ArithmeticError('Unresolved interval sign; no census promotion')


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def mul(a, t):
    return tuple(x*t for x in a)


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def det(a, b, c):
    return dot(a, cross(b, c))


def inv3(m):
    a = [[Q(x) for x in row] + [Q(i == j) for j in range(3)]
         for i, row in enumerate(m)]
    for j in range(3):
        p = next((k for k in range(j, 3) if a[k][j]), None)
        assert p is not None, 'Singular nominated inverse'
        a[j], a[p] = a[p], a[j]
        z = a[j][j]
        a[j] = [v/z for v in a[j]]
        for k in range(3):
            if k != j:
                z = a[k][j]
                a[k] = [v-z*w for v, w in zip(a[k], a[j])]
    return [row[3:] for row in a]


def encode(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, I):
        return [str(Q(x.lo, SCALE)), str(Q(x.hi, SCALE))]
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    if isinstance(x, dict):
        return {str(k): encode(v) for k, v in x.items()}
    return x


def write(path, obj):
    path.write_text(json.dumps(encode(obj), sort_keys=True,
                              separators=(',', ':')), encoding='utf-8')


def recover_parent(source, destination):
    text = Path(source).read_text(encoding='utf-8')
    candidates = [''.join(text.split())]
    candidates += [''.join(s.split()) for s in
                   re.findall(r'```base64\s*\n(.*?)```', text, re.S)]
    matches = {s for s in candidates
               if len(s) == 72364 and sha(s.encode()) == B64_SHA}
    assert len(matches) == 1, 'Literal required parent capsule not found'
    z = base64.b64decode(matches.pop(), validate=True)
    assert len(z) == 54272 and sha(z) == XZ_SHA
    b = lzma.decompress(z)
    assert len(b) == 206113 and sha(b) == DICT_SHA
    files = json.loads(b)
    assert len(files) == 44
    destination.mkdir()
    for name, text in files.items():
        q = Path(name)
        assert not q.is_absolute() and '..' not in q.parts
        p = destination/q
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode('utf-8'))
    manifest = json.loads((destination/'SOURCE_MANIFEST.json').read_text())
    for name, wanted in manifest.items():
        b = (destination/name).read_bytes()
        assert len(b) == wanted['bytes'] and sha(b) == wanted['sha256']
    print('PARENT_CAPSULE_RECOVERED_44_VERIFIED', flush=True)


def call(script, *args):
    script = Path(script).resolve()
    subprocess.run([sys.executable, '-B', '-S', str(script),
                    *map(str, args)], cwd=script.parent, check=True)


def source_report(parent, work, raw):
    if raw is not None:
        out = work/'SOURCE_AUDIT'
        call(parent/'audit_raw.py', Path(raw).resolve(), out)
        a = out/'A.json'
    else:
        call(parent/'REPLAY.py', 'prepare')
        call(parent/'REPLAY.py', 'MASS_NEAR_EXACT')
        matches = [p for p in parent.rglob('A.json')
                   if sha(p.read_bytes()) == PARENT_A_SHA]
        assert len(matches) == 1, 'Authoritative parent report not reconstructed'
        a = matches[0]
        assert len(a.read_bytes()) == 309669
    assert a.read_bytes() == a.with_name('B.json').read_bytes()
    assert a.with_name('MASS.json').is_file()
    return a


def geometry(report, center):
    r = json.loads(Path(report).read_text())
    X = [sub(tuple(map(Q, x)), center) for x in r['raw_vertices']]
    N = []
    for n, h in zip(r['normals'], r['offsets']):
        n = tuple(map(Q, n))
        hh = Q(h)-dot(n, center)
        assert hh > 0, 'Reference is not strictly interior'
        N.append(mul(n, 1/hh))
    faces = r['faces']
    edges = [tuple(e) for e in r['edges']]
    assert all(dot(n, x) <= 1 for n in N for x in X)
    for n, cy in zip(N, faces):
        assert all(dot(n, X[i]) == 1 for i in cy)
    T = [(cy[0], cy[k], cy[k+1])
         for cy in faces for k in range(1, len(cy)-1)]
    volumes = [det(X[i], X[j], X[k])/6 for i, j, k in T]
    assert all(v > 0 for v in volumes)
    return r, X, N, faces, edges, T, volumes


def integrals(X, T, volumes, a, hessian=True):
    ds = [I(1)+dot(a, x) for x in X]
    assert all(d.lo > 0 for d in ds), 'Projective positivity not certified'
    Y = [tuple(I(x[k])/d for k in range(3)) for x, d in zip(X, ds)]
    V = I(0)
    F = [I(0) for _ in range(3)]
    H = [[I(0) for _ in range(3)] for _ in range(3)]
    for (i, j, k), vt in zip(T, volumes):
        v = I(vt)/(ds[i]*ds[j]*ds[k])
        ys = [Y[i], Y[j], Y[k]]
        s = add(add(ys[0], ys[1]), ys[2])
        V = V+v
        for p in range(3):
            F[p] = F[p]-v*s[p]
            if hessian:
                for q in range(3):
                    H[p][q] = H[p][q]+v*(s[p]*s[q]+sum(y[p]*y[q] for y in ys))
    return V, F, H, Y


def isolate(X, T, volumes):
    a = [Q(0), Q(0), Q(0)]
    history = []
    for iteration in range(80):
        V, F, H, Y = integrals(X, T, volumes, list(map(I, a)))
        C = inv3([[z.mid() for z in row] for row in H])
        CF = [sum(C[i][j]*F[j] for j in range(3)) for i in range(3)]
        residual = max(z.maxabs() for z in CF)
        history.append({'iteration': iteration, 'a': a[:],
                        'volume': V, 'Newton_correction_bound': residual})
        if residual < RADIUS/100:
            box = [I(x-RADIUS, x+RADIUS) for x in a]
            VB, FB, HB, YB = integrals(X, T, volumes, box)
            R = [[I(int(i == j))-sum(C[i][k]*HB[k][j] for k in range(3))
                  for j in range(3)] for i in range(3)]
            lip = max(sum(z.maxabs() for z in row) for row in R)
            slack = RADIUS-residual-lip*RADIUS
            assert lip < 1 and slack > 0, 'No root self-map certificate'
            # inv3 succeeded: C is invertible. A fixed point therefore has F=0.
            return a, box, C, VB, YB, history, {
                'contraction_bound': lip, 'residual_bound': residual,
                'strict_self_map_slack': slack}
        direction = [-z.mid() for z in CF]
        accepted = False
        for backtrack in range(64):
            step = Q(1, 1 << backtrack)
            trial = [Q(round(GRID*(a[i]+step*direction[i])), GRID)
                     for i in range(3)]
            if not all(1+dot(trial, x) > 0 for x in X):
                continue
            try:
                VT = integrals(X, T, volumes, list(map(I, trial)), False)[0]
            except AssertionError:
                continue
            if VT.hi < V.lo:
                a = trial
                accepted = True
                break
        if not accepted:
            raise ArithmeticError('No certified descent; this is not an exclusion')
    raise ArithmeticError('Iteration limit; this is not an exclusion')


def classify(face_signs, vertex_signs, edge_signs):
    S = [i for i, s in enumerate(face_signs) if min(s) > 0]
    SW = [i for i, s in enumerate(face_signs) if min(s) == 0]
    U = [i for i, s in enumerate(vertex_signs) if min(s) > 0]
    UW = [i for i, s in enumerate(vertex_signs) if min(s) == 0]
    E = [e for e, s in edge_signs if min(s) > 0]
    EW = [e for e, s in edge_signs if min(s) == 0]
    return {'counts': [len(S), len(U), len(E)],
            'weak': [len(SW), len(UW), len(EW)],
            'stable_faces': S, 'unstable_vertices': U, 'saddle_edges': E,
            'weak_faces': SW, 'weak_vertices': UW, 'weak_edges': EW}


def mechanics(X, N, faces, edges, box, Y):
    adj = {e: [] for e in edges}
    for f, cy in enumerate(faces):
        for i, j in zip(cy, cy[1:]+cy[:1]):
            adj[tuple(sorted((i, j)))].append(f)
    assert all(len(fs) == 2 for fs in adj.values())

    def rf(i, j):
        x, y = X[i], X[j]
        xx, xy = dot(x, x), dot(x, y)
        return I(xx-xy)+dot(box, sub(mul(y, xx), mul(x, xy)))

    def sf(f, k):
        d = sub(N[f], N[k])
        return I(dot(N[f], d))+dot(box, d)

    fs, vs, es = [], [], []
    for f, cy in enumerate(faces):
        signs = []
        for i, j in zip(cy, cy[1:]+cy[:1]):
            pair = adj[tuple(sorted((i, j)))]
            k = pair[0] if pair[1] == f else pair[1]
            signs.append(sf(f, k).sign())
        fs.append(signs)
    for i in range(len(X)):
        vs.append([rf(i, j).sign() for j in range(len(X)) if i != j])
    for i, j in edges:
        f, k = adj[(i, j)]
        es.append(([i, j], [rf(i, j).sign(), rf(j, i).sign(),
                            sf(k, f).sign(), sf(f, k).sign()]))
    affine = classify(fs, vs, es)

    NN = [add(tuple(map(I, n)), box) for n in N]
    fs2, vs2, es2 = [], [], []
    for n, cy in zip(NN, faces):
        p = mul(n, 1/dot(n, n))
        fs2.append([dot(n, cross(sub(Y[j], Y[i]), sub(p, Y[i]))).sign()
                    for i, j in zip(cy, cy[1:]+cy[:1])])
    for i in range(len(X)):
        vs2.append([(-dot(Y[i], sub(Y[j], Y[i]))).sign()
                    for j in range(len(X)) if i != j])
    for i, j in edges:
        d = sub(Y[j], Y[i])
        dd, z = dot(d, d), dot(Y[i], d)
        pn = sub(mul(Y[i], dd), mul(d, z))
        f, k = adj[(i, j)]
        n, m = NN[f], NN[k]
        nn, mm, nm = dot(n, n), dot(m, m), dot(n, m)
        assert (nn*mm-nm*nm).lo > 0
        vals = [-z, dd+z, dot(pn, sub(mul(n, mm), mul(m, nm))),
                dot(pn, sub(mul(m, nn), mul(n, nm)))]
        es2.append(([i, j], [v.sign() for v in vals]))
    direct = classify(fs2, vs2, es2)
    assert fs == fs2 and vs == vs2 and es == es2 and affine == direct
    return affine, {'faces': fs, 'vertices_all_pairs': vs, 'edges': es}


def third_mass(faces, Y):
    V = I(0)
    M = [I(0) for _ in range(3)]
    count = 0
    for face in faces:
        cy = face[1:]+face[:1]
        for k in range(1, len(cy)-1):
            y, z, w = [Y[i] for i in (cy[0], cy[k], cy[k+1])]
            v = det(y, z, w)/6
            assert v.lo > 0
            V = V+v
            s = add(add(y, z), w)
            for j in range(3):
                M[j] = M[j]+v*s[j]/4
            count += 1
    return V, M, count


def rational_input(N, a):
    rows = []
    for n in N:
        row = list(add(n, a))+[Q(1)]
        den = lcm(*(v.denominator for v in row))
        ints = [int(v*den) for v in row]
        common = gcd(*ints)
        rows.append([v//common for v in ints])
    return {'H': rows}


def main():
    assert __debug__, 'Assertions must be enabled'
    ap = argparse.ArgumentParser()
    ap.add_argument('parent_payload')
    ap.add_argument('new_directory')
    ap.add_argument('--raw')
    ap.add_argument('--center')
    args = ap.parse_args()
    work = Path(args.new_directory).resolve()
    work.mkdir(parents=True, exist_ok=False)
    parent = work/'parent'
    recover_parent(args.parent_payload, parent)
    source = source_report(parent, work, args.raw)
    if args.center is None:
        assert args.raw is None, 'Supply a rational interior --center for another input'
        center = [Q(-290787037, 10**9), Q(-270371541, 10**9),
                  Q(-68565859, 250000000)]
    else:
        center = list(map(Q, args.center.split(',')))
        assert len(center) == 3
    r, X, N, faces, edges, T, volumes = geometry(source, center)
    a, box, C, VB, Y, history, contraction = isolate(X, T, volumes)
    print('PROJECTIVE_ROOT_EXISTENCE_AND_GLOBAL_UNIQUENESS_CERTIFICATE', flush=True)
    census, signs = mechanics(X, N, faces, edges, box, Y)
    print('PROJECTIVE_FULL_AFFINE_AND_DIRECT_CENSUS_AGREE', census, flush=True)
    V3, M3, nt = third_mass(faces, Y)
    assert max(V3.lo, VB.lo) <= min(V3.hi, VB.hi)
    assert all(m.lo <= 0 <= m.hi for m in M3)
    certificate = {
        'source_report_sha256': sha(source.read_bytes()),
        'reference': center, 'a0': a, 'radius': RADIUS,
        'inverse_matrix': C, 'contraction': contraction,
        'VEF': [r['V'], r['E'], r['F']], 'census': census,
        'complete_signs': signs, 'volume_enclosure': VB,
        'exact_root_first_moments': [0, 0, 0],
        'mass_zero_authority': 'Certified root of the exact equations F=-4M=0',
        'third_volume_enclosure': V3, 'third_first_moment_enclosures': M3,
        'third_positive_tetrahedra': nt,
        'third_status': 'Independent enclosure check, not a separate exact-zero inference',
        'parameters': {'dyadic_bits': BITS, 'rounding_grid': GRID,
                       'max_Newton_steps': 80, 'max_backtracks': 64}}
    write(work/'ROOT_CERTIFICATE.json', certificate)
    write(work/'NEWTON_HISTORY.json', history)
    raw = work/'RATIONAL_PROJECTIVE_INPUT.json'
    write(raw, rational_input(N, a))
    audit = work/'RATIONAL_AUDIT'
    call(parent/'audit_raw.py', raw, audit)
    assert (audit/'A.json').read_bytes() == (audit/'B.json').read_bytes()
    assert (audit/'MASS.json').is_file()
    ra = json.loads((audit/'A.json').read_text())
    assert [ra['V'], ra['E'], ra['F']] == [r['V'], r['E'], r['F']]
    receipt = {
        'source_unit_sha256': sha(Path(__file__).read_bytes()),
        'source_unit_bytes': len(Path(__file__).read_bytes()),
        'isolated_root_census': census,
        'rational_own_counts': ra['counts'], 'rational_weak': ra['weak'],
        'rational_raw_centroid': ra['raw_centroid'],
        'rational_ordinary_volume': ra['ordinary_volume'],
        'rational_matches_root_counts': ra['counts'] == census['counts'],
        'own110_with_E_below311': (ra['counts'] == [1, 1, 0]
                                 and ra['weak'] == [0, 0, 0] and ra['E'] < 311),
        'files': {}}
    for p in [raw, work/'ROOT_CERTIFICATE.json', work/'NEWTON_HISTORY.json',
              audit/'A.json', audit/'B.json', audit/'MASS.json']:
        b = p.read_bytes()
        receipt['files'][str(p.relative_to(work))] = {'bytes': len(b), 'sha256': sha(b)}
    write(work/'RECEIPT.json', receipt)
    print('RATIONAL_PROJECTIVE_BODY_A_B_AND_MASS_RETURNED',
          json.dumps(encode(receipt), sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
```

## 7. Continuation priority

The constructive question is now precise: vary real supporting geometry or the reference point so that the unique finite mass-normalized representative lies in a complete110/weak000 mechanical region. On the released H61 side, retain the explicit input-row budget, remove the three normalization-redundant common-normal directions, and allow genuine root, witness and incidence turnover. On the E308 contact side, preserve the exact projective incidence when testing this inner solve rather than rounding transformed vertices and unintentionally splitting maximal facets.

A successful inner mass solve is not the desired body. Acceptance still requires the exact actual filled centroid and the entire strict/weak maximal-complex census. The supplied parent remains the last fully reconstructible authority until a readable new receipt and complete new recovery input establish otherwise.
