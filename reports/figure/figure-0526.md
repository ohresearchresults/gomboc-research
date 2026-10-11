# figure-0526

Historical AI scientific report · saved 2026-09-23 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# RN44 — exact two-cut access to the complete RN36 physical basin

## Status

**No own-centroid strict110 construction is established in this handoff.** The durable new construction is a two-halfspace truncation of the supplied RN36 body that removes every vertex of its complete P7 component while strictly retaining all33 complementary vertices. The two cuts have small integer normals and rational offsets. Together with the parent’s positive convex-intersection certificate, they establish that the fixed-complement cap-cover number is **exactly two**, not merely greater than one.

The midpoint truncation is a genuinely changed, uniformly filled physical body. Its definition does not use a diagnostic polar or prescribe its centroid. It has at most78 maximal facets and therefore **E≤228**, independently of numerical hull counts. Its own volume, first moments, maximal complex, mixed strict/weak mechanics and both complete positive-bar landscapes are reconstructed by the exact recovery patch below.

There is an important verification boundary. I have the verified parent receipt and the initial numerical cap/envelope calculations, but I do not have readable terminal receipts for the subsequent new exact-replay calls in the retained context. Consequently, I do **not** report new audit hashes, exact mechanical classes, or the proposed mass-envelope inequalities as observed passes. The numerical midpoint census was V70/E143/F75 with S12/U13; that is a nomination, not a certified endpoint class. Subsequent free-geometry optimization attempts are not promoted as exact successors without their complete terminal pins and receipts.

## Source and parent binding

The complete supplied journal update, branch material and literal parent were read, as were the decoded parent source units. The parent is `figure-0519`, advertised SHA256 `0949d6226b6c7e5bc6b8faade6bc3152fa888d44d07ed1cf4620b79ccab87bdc`.

The executable parent capsule is the authority for reconstruction. Its decoded46-unit dictionary has207257 bytes and SHA256 `223ee37c0175e1ea17f27f8a9505be12986827cf2a85571751c3a3577099d8b6`. Its compressed49180-byte payload has SHA256 `61a4fc21d9a8b7deb6c0f56809f1b0b563efd7182ba029be08301bb33aeb877c`. The supplied `RECOVER_RN30.py` is62859 bytes, SHA256 `c830d11b95b555ef670e582c0be161f7c6ee4eecbde106ef68361b2b186a833f`.

A fresh parent replay was observed:

```
RN30_INLINE_RECOVERY_PASS 46 207257
RN30_TWELVE_LITERAL_EXACT_INPUTS_RECOVERED_PASS 12
RN30_FULL_EXACT_REBUILD_PASS RN36_RES02_G1000 40 114 76 [1,2,1] [0,0,0]
```

The matching principal audit is65880 bytes, SHA256 `46b4dda3151d5e6c2be950d4d129a6e6df9c1d731142af1c2b7cfc747f588aa5`. The principal input is2664 bytes, SHA256 `7025e2ba2706047c05ec27dc2ef6ccedf57f67244c5f668ff6feaa01878b9ecd`.

RN36 is the actual uniformly filled V40/E114/F76 strict121 body, with Qbars empty, stable triangle[0,3,12], unstable vertices0/39, and physical component

```
X = [8,20,31,36,37,38,39].
```

The complement is `Y={0,...,39}\X`. The parent’s complete P7/cut35 landscape and actual mass are in the supplied literal result. :contentReference[oaicite:0]{index=0}

## 1. Exact two-cap cover of the whole P7 component

Use the parent’s raw coordinate frame and canonical exposed-vertex numbering. Define

```
n1 = (1000,-273,-348)
n2 = (1000,-611,986)

L1 = 295433/1000
R1 = 402336/1000
L2 = 337411/1000
R2 = 356753/1000.
```

The exact extrema are

```
max_{y in Y} n1·y = L1
min_{x in {31,36}} n1·x = R1

max_{y in Y} n2·y = L2
min_{x in {8,20,37,38,39}} n2·x = R2.
```

Both complementary maxima are attained at old vertex23. Thus, for **every** pair of offsets

```
L1 < h1 < R1,
L2 < h2 < R2,
```

the uniformly filled body

```
K(h1,h2) = P ∩ {n1·x≤h1} ∩ {n2·x≤h2}
```

strictly retains every old complementary vertex and removes every old packet vertex. This statement concerns actual halfspace intersection, not a changed reference centre.

The midpoint body is the exact finite object

```
RN44_MID = P ∩ {n1·x ≤ 697769/2000}
             ∩ {n2·x ≤ 173541/500}.
```

At this midpoint, the first cut removes old vertices31,36,37,38; the second removes8,20,37,38,39. Their union is exactly X. The minimum retained-point slacks are `106903/2000` and `9671/1000`, respectively. The same numbers are the minimum excesses on the designated subsets used to prove coverage.

Every retained old vertex remains extreme: an old exposing functional still uniquely exposes that vertex in a subset of P containing it. The truncation is full-dimensional because it contains the full-dimensional hull of Y. It is bounded because it is a subset of P. At most76 inherited supporting planes plus the two new planes can be maximal, giving

```
F ≤ 78,
E ≤ 3F-6 ≤ 228.
```

This is a genuine final-edge bound, not a claim that either operation adds exactly three edges.

### Why the minimum is two

The parent supplies the positive convex intersection between packet points8/36 and complementary points14/23/26:

```
W = 82014183
left numerators  = [37944418,44069765]
right numerators = [33455325,14592729,33966129].
```

Both sides sum to W and give the same point. Therefore no strict single affine cut can remove all X and retain all Y. This lower bound applies irrespective of centroid translation and invertible affine reparameterization while those material locations and side roles persist. The two explicit cuts above give the matching upper bound. The parent’s stronger independent-cube statement remains a separate result; it is not needed for this cover-number proof. :contentReference[oaicite:1]{index=1}

The nomination stage examined all127 nonempty packet subsets with bounded-normal linear programs. It produced49 positive-margin subset nominations and18 complementary partition pairs. Those finite LP counts are not an exclusion theorem. The exact extrema and positive convex identity, rather than solver statuses, establish cover number two.

## 2. Actual-mass envelope suggested by the complete cap family

Define the exact nested bodies

```
W = K(L1,L2),
O = K(R1,R2).
```

Every member of the open two-offset rectangle lies between them:

```
W ⊆ K(h1,h2) ⊆ O.
```

The numerical calculation suggested that **old vertices0 and10 remain strict U throughout a much larger class: every uniformly filled convex polyhedron between W and O**. This would cover arbitrary extra cuts, added intermediate material, topology changes and root changes elsewhere within the same envelope, rather than only the two-parameter family.

The initial numerical mass estimates were

```
V(W) ≈ 0.6035673146988497
c(W) ≈ (-0.32852930667468455,
         0.10884506707957982,
        -0.1897395930371612)

V(O) ≈ 0.6238873247128164
c(O) ≈ (-0.31126915578135933,
         0.10341042139618,
        -0.18423407506048822).
```

For the midpoint:

```
V ≈ 0.615112197690355
c ≈ (-0.3186970006517885,
      0.10579998797085086,
     -0.18688913012450295).
```

These are floating nominations. They are not substituted for the rational mass output of the exact replay.

### Exact certificate to test

For a retained candidate root v and another vertex w of O, put `d=w-v` and

```
ell(x) = (v-x)·d.
```

For every uniformly filled W⊆K⊆O,

```
V(K) ell(c(K))
 = integral_K ell(x) dx
 ≤ V(W) ell(c(W))
   + (V(O)-V(W)) max(0,max_{x in O} ell(x)).
```

Because ell is affine, its maximum over O is attained at an explicitly reconstructed vertex of O. Strict negativity of this bound for every w≠v proves that v is strict U for every such K. Applying it to two distinct retained vertices proves U≥2 without assuming that no additional weak equilibrium occurs.

The preliminary floating maximum upper bounds were approximately−1.49238 for old vertex0 and−0.00171325 for old vertex10. The exact Fraction test is included below. **I do not label these numerical signs an observed exact obstruction.**

The patch also tests a full-dimensional metric neighborhood. For symmetric `G` with entrywise `|Gij-Iij|≤epsilon`, write

```
A = V(W) sym((v-c(W)) d^T).
```

An upper bound for the fixed-inner contribution is `tr(A)+epsilon sum|Aij|`. For the variable material, maximize

```
tr(sym((v-x)d^T))
 + epsilon sum|sym((v-x)d^T)ij|
```

over the vertices of O and zero. A strictly negative combined bound proves the same root statement for every metric in that box. The condition `3 epsilon<1` guarantees positive definiteness. The supplied program checks the proposed box rather than assuming it works.

### Scope of a successful envelope test

Such a certificate would close **W⊆K⊆O in the stated metric neighborhood**, with actual uniform volume density. It would not close arbitrary two-cap orientations, removal of material from W, additions outside O, moved retained carriers, or unrestricted metrics. Restoring the old centroid would not itself be a constructive escape: the family is evaluated at each body’s own centroid.

## 3. A broader retained-material test prepared for continuation

A second inner body is

```
CORE33 = conv(Y).
```

A broader candidate outer body is

```
BROAD = P ∩ {n2·x≤500}.
```

The patch reconstructs both and tests every inherited triangular facet whose three vertices belong to Y. These are genuine retained material patches, not merely labels.

For an oriented supporting triangle, let `n` be its outward normal and `e` one oriented edge starting at a. Put `t=n×e`. The Euclidean face-foot inequality is simply

```
ell(c) = t·(c-a) > 0,
```

because t is tangent to the face and hence is unchanged by orthogonal projection onto its plane. Thus

```
V(K) ell(c(K))
 ≥ V(CORE33) ell(c(CORE33))
   + (V(BROAD)-V(CORE33)) min(0,min_BROAD ell).
```

Three positive edge bounds preserve a strict stable equilibrium in that retained triangular patch for every intermediate body.

For a metric G, set `J=adj(G)`. Clearing the positive denominator `n^T J n` gives the affine-in-centre expression

```
(n^T J n) t·(c-a)
 + (h-n·c) t^T J n.
```

Its coefficient matrix is explicit in the patch. The bound `|J-I|entrywise≤2 epsilon+2 epsilon^2` supplies a rational whole-metric-box test. This is an additional exact test prepared here, **not an asserted completed RN36 exclusion**.

A positive result would identify which retained material triangles must be released during S1 repair. Moving a source label would not suffice when the old material triangle remains contained in the new body. Conversely, leaving a certified envelope would only remove that obstruction; it would not establish cancellation.

## 4. Recovery and verification boundary

The unit below is a **complete exact patch to the supplied literal parent**, not a standalone replacement for the parent’s46-unit capsule. Its only inherited code dependencies are `exact.py` and `verify_new.py`, both present in that supplied capsule. The parent replay reconstructs the required RN36 input and audit. No archive lookup, research connector, old scratch directory or missing optimizer checkpoint is needed.

Use the already supplied `RECOVER_RN30.py`, then save the source below as `RN44_PATCH.py` in its output directory:

```sh
python -B -S RECOVER_RN30.py rn44
cd rn44
C92_GMP=0 python -B -S REPLAY_RN30.py lead 1
C92_GMP=0 python -B -S RN44_PATCH.py
```

Exact replay uses the CPython standard library. Optional nomination uses Python3.13.5, NumPy2.3.5 and SciPy1.17.0, with one BLAS/OMP/MKL thread:

```sh
python -B RN44_PATCH.py --nominate
```

The patch writes the full exact geometry and audit of CORE33, INNER, OUTER, MID and BROAD. Every audit includes actual volume/moments/centroid, maximal facets, true edges and owners, all strict/additionalweak S/U/H data, every positive P/Q bar with complete component/cut/path, and all-pair chord domination checks. It also invokes the parent’s separate support-foot mechanics and additional mass calculation on the reconstructed incidences. This is not a claim of two independent hull implementations.

New byte counts and SHA256 values are produced in `RN44_MANIFEST.json`. They are **not supplied here as observed matched receipts**, because the corresponding terminal outputs were not available for reliable transcription. Likewise, the final combined patch below has not been cold-replayed as one packaged unit in the retained evidence. Its pass/fail messages must be distinguished from the observed parent replay above.

Expected geometry markers are `RN44_PARENT_HASH_PASS`, `RN44_COVER_EXACTLY_TWO_PASS` and five `RN44_FULL_AUDIT` lines. Envelope messages deliberately distinguish `PASS` from `NOT_CERTIFIED`; a failed bound does not become an exclusion proof.

The most useful immediate continuation is to run this exact patch, retain its complete new receipts and landscapes, and then release the actual material responsible for any certified envelope obstruction. The two-cut cover has already removed the original fixed-one-cap access problem. The remaining question is simultaneous own-mass mechanical repair, not disappearance of the seven old labels.

## Complete runnable patch

```python
'''RN44: exact two-cut construction and nested uniform-mass tests.
Required inherited source: supplied RECOVER_RN30.py, decoded dictionary
SHA256 223ee37c0175e1ea17f27f8a9505be12986827cf2a85571751c3a3577099d8b6.
No external packages are used unless --nominate is requested.
'''
import os
for key in ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS'):
    os.environ[key] = '1'
os.environ['C92_GMP'] = '0'

import sys
import json
import hashlib
import subprocess
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from itertools import combinations
from math import gcd, lcm

import exact as e
from verify_new import independent

PARENT_AUDIT = 'RN36_RES02_G1000_audit.json'
PARENT_SHA = '46b4dda3151d5e6c2be950d4d129a6e6df9c1d731142af1c2b7cfc747f588aa5'
PARENT_BYTES = 65880
N = [(1000, -273, -348), (1000, -611, 986)]
PART = [[31, 36], [8, 20, 37, 38, 39]]
X = [8, 20, 31, 36, 37, 38, 39]
INTERVALS = [
    (F(295433, 1000), F(402336, 1000)),
    (F(337411, 1000), F(356753, 1000)),
]


def receipt(path):
    b = Path(path).read_bytes()
    return dict(bytes=len(b), sha256=hashlib.sha256(b).hexdigest())


def put(path, obj, manifest):
    e.write(path, obj)
    manifest[path] = receipt(path)


def load_parent():
    p = Path(PARENT_AUDIT)
    if not p.exists():
        subprocess.run(
            [sys.executable, '-B', '-S', 'REPLAY_RN30.py', 'lead', '1'],
            check=True,
        )
    raw = p.read_bytes()
    assert len(raw) == PARENT_BYTES
    assert hashlib.sha256(raw).hexdigest() == PARENT_SHA
    a = json.loads(raw)
    assert (a['V'], a['E'], a['F']) == (40, 114, 76)
    assert a['strict'] == [1, 2, 1]
    assert a['additional_weak'] == [0, 0, 0]
    assert not a['polar']['positive_bars']
    assert a['physical']['positive_bars'][0]['component'] == X
    v = [tuple(F(x, p[3]) for x in p[:3]) for p in a['vertices']]
    D = a['vertices'][0][3]
    assert all(p[3] == D for p in a['vertices'])
    H = [(tuple(p[:3]), F(p[3], D)) for p in a['planes']]
    print('RN44_PARENT_HASH_PASS', flush=True)
    return a, v, H


def solve3(normals, offsets):
    a, b, c = normals
    d = e.det(a, b, c)
    if not d:
        return None
    z = e.add(
        e.add(e.mul(offsets[0], e.cross(b, c)),
              e.mul(offsets[1], e.cross(c, a))),
        e.mul(offsets[2], e.cross(a, b)),
    )
    return tuple(F(x, d) for x in z)


def construct(a, v, H, heights, name):
    cuts = list(zip(N, heights))
    all_h = H + cuts

    def inside(p):
        return all(e.dot(n, p) <= b for n, b in all_h)

    # A vertex uses zero, one or two independent new planes.
    # Zero: an old vertex. One: a point on an old true edge.
    # Two: intersection of both new planes and an old facet plane.
    points = {p for p in v if inside(p)}
    for i, j, *_ in a['edges']:
        p, q = v[i], v[j]
        d = e.sub(q, p)
        for n, b in cuts:
            den = e.dot(n, d)
            if not den:
                continue
            t = (b - e.dot(n, p)) / den
            if 0 <= t <= 1:
                z = e.add(p, e.mul(t, d))
                if inside(z):
                    points.add(z)
    for n, b in H:
        z = solve3([N[0], N[1], n], [heights[0], heights[1], b])
        if z is not None and inside(z):
            points.add(z)
    points = sorted(points)
    assert len(points) >= 4

    D = lcm(*(x.denominator for p in points for x in p))
    integers = [tuple(int(x * D) for x in p) for p in points]
    planes = []
    for n, b in all_h:
        ids = [i for i, p in enumerate(points) if e.dot(n, p) == b]
        if len(ids) < 3:
            continue
        noncollinear = any(
            any(e.cross(e.sub(points[j], points[ids[0]]),
                        e.sub(points[k], points[ids[0]])))
            for j, k in combinations(ids[1:], 2)
        )
        if not noncollinear:
            continue
        L = lcm(*(F(x).denominator for x in n), F(b * D).denominator)
        ni = [int(F(x) * L) for x in n]
        hi = int(b * D * L)
        g = reduce(gcd, map(abs, ni))
        assert hi % g == 0
        planes.append(tuple([x // g for x in ni] + [hi // g]))

    data = dict(name=name, denominator=D,
                points=[list(p) for p in integers])
    audit = e.audit(data, True, planes)
    audit['construction'] = dict(
        parent_audit_sha256=PARENT_SHA,
        normals=N,
        heights=list(map(str, heights)),
        vertex_enumeration='zero/one/two independent new-plane cases',
    )
    assert audit['F'] <= 78 and audit['E'] <= 228
    return data, audit


def raw_vertices(a):
    return [tuple(F(x, p[3]) for x in p[:3]) for p in a['vertices']]


def sym_pair(a, d):
    M = [[(a[i] * d[j] + a[j] * d[i]) / 2
          for j in range(3)] for i in range(3)]
    tr = sum(M[i][i] for i in range(3))
    norm = sum(abs(x) for r in M for x in r)
    return tr, norm


def unstable_envelope(W, O, parent_vertices, epsilon):
    assert 0 <= epsilon and 3 * epsilon < 1
    VW, VO = F(W['volume']), F(O['volume'])
    assert VO >= VW > 0
    delta = VO - VW
    cW = tuple(map(F, W['centroid']))
    outer = raw_vertices(O)
    inner = set(raw_vertices(W))
    rows = []
    for root in (0, 10):
        p = parent_vertices[root]
        assert p in inner and p in outer
        for j, q in enumerate(outer):
            if q == p:
                continue
            d = e.sub(q, p)
            A, B = sym_pair(e.mul(VW, e.sub(p, cW)), d)
            values = [sym_pair(e.sub(p, x), d) for x in outer]
            extra = max(F(0), *(t + epsilon * n for t, n in values))
            upper = A + epsilon * B + delta * extra
            rows.append(dict(
                root_parent=root,
                outer_vertex=j,
                inner_trace=str(A),
                inner_matrix_l1=str(B),
                extension_upper=str(extra),
                moment_upper=str(upper),
            ))
    passed = all(F(r['moment_upper']) < 0 for r in rows)
    return dict(
        passed=passed,
        epsilon=str(epsilon),
        roots_parent=[0, 10],
        inner_volume=str(VW), outer_volume=str(VO),
        rows=rows,
    )


def stable_patches(parent, v, H, W, O, epsilon):
    assert 0 <= epsilon and 3 * epsilon < 1
    rho = 2 * epsilon + 2 * epsilon * epsilon
    VW, VO = F(W['volume']), F(O['volume'])
    assert VO >= VW > 0
    delta = VO - VW
    cW = tuple(map(F, W['centroid']))
    outer = raw_vertices(O)
    # These checks concern inherited material triangles, not new caps.
    patches = []
    all_tests = []
    for fi, cycle in enumerate(parent['facets']):
        if set(cycle) & set(X):
            continue
        assert len(cycle) == 3
        n, h = H[fi]
        assert all(any(p == v[j] for p in outer) for j in cycle)
        rows = []
        for i, j in zip(cycle, cycle[1:] + cycle[:1]):
            t = e.cross(n, e.sub(v[j], v[i]))

            def pair(c):
                ell = e.dot(t, e.sub(c, v[i]))
                s = h - e.dot(n, c)
                M = [[n[u] * n[w] * ell
                      + (t[u] * n[w] + t[w] * n[u]) * s / 2
                      for w in range(3)] for u in range(3)]
                tr = sum(M[k][k] for k in range(3))
                norm = sum(abs(x) for row in M for x in row)
                return tr, norm

            A, B = pair(cW)
            extra = min(F(0), *(a - rho * b for a, b in map(pair, outer)))
            lower = VW * (A - rho * B) + delta * extra
            rows.append(dict(
                edge=[i, j], inner_trace=str(VW * A),
                inner_matrix_l1=str(VW * B),
                extension_lower=str(extra), moment_lower=str(lower),
            ))
        test = dict(parent_face=fi, triangle=cycle, rows=rows)
        all_tests.append(test)
        if all(F(r['moment_lower']) > 0 for r in rows):
            patches.append(fi)
    return dict(
        epsilon=str(epsilon), adjugate_error=str(rho),
        inner_volume=str(VW), outer_volume=str(VO),
        certified_parent_faces=patches, tests=all_tests,
    )


def nominate(v):
    # Optional finite nomination, not an exact infeasibility certificate.
    import numpy as np
    from scipy.optimize import linprog
    Y = [i for i in range(40) if i not in X]
    z = np.array(v, dtype=float)
    bank = []
    ledger = []
    for mask in range(1, 128):
        B = [X[i] for i in range(7) if mask >> i & 1]
        A = np.r_[
            np.c_[-z[B], np.ones(len(B)), np.ones(len(B))],
            np.c_[z[Y], -np.ones(len(Y)), np.ones(len(Y))],
        ]
        r = linprog(
            [0, 0, 0, 0, -1], A_ub=A, b_ub=np.zeros(len(A)),
            bounds=[(-1, 1)] * 3 + [(None, None)] * 2,
            method='highs',
        )
        ledger.append(dict(mask=mask, status=int(r.status),
                           margin=None if not r.success else float(r.x[-1])))
        if not r.success or r.x[-1] <= 1e-8:
            continue
        n = tuple(int(x) for x in np.rint(r.x[:3] * 1000000))
        lower = max(e.dot(n, v[i]) for i in Y)
        upper = min(e.dot(n, v[i]) for i in B)
        if lower < upper:
            bank.append(dict(mask=mask, packet=B, normal=n,
                             lower=str(lower), upper=str(upper)))
    pairs = [(a['mask'], b['mask']) for a in bank for b in bank
             if a['mask'] < b['mask'] and a['mask'] + b['mask'] == 127]
    e.write('RN44_NOMINATION.json', dict(ledger=ledger, bank=bank, pairs=pairs))
    print('RN44_FINITE_NOMINATION', len(bank), len(pairs), flush=True)


def main():
    a, v, H = load_parent()
    Y = [i for i in range(40) if i not in X]
    manifest = {PARENT_AUDIT: receipt(PARENT_AUDIT)}

    # Exact cover upper bound.
    extrema = []
    for n, B, (lo, hi) in zip(N, PART, INTERVALS):
        assert max(e.dot(n, v[i]) for i in Y) == lo
        assert min(e.dot(n, v[i]) for i in B) == hi
        assert lo < hi
        extrema.append(dict(normal=n, designated_packet=B,
                            retained_max=str(lo), packet_min=str(hi)))
    assert sorted(sum(PART, [])) == X

    # Exact one-cap lower bound, independently of any LP status.
    left = [37944418, 44069765]
    right = [33455325, 14592729, 33966129]
    assert sum(left) == sum(right) == 82014183
    for k in range(3):
        assert sum(w * v[i][k] for w, i in zip(left, [8, 36])) == \
               sum(w * v[i][k] for w, i in zip(right, [14, 23, 26]))
    put('RN44_COVER.json', dict(
        parent_sha256=PARENT_SHA, packet=X, complement=Y,
        extrema=extrema,
        lower_bound=dict(left=[8, 36], right=[14, 23, 26],
                         left_numerators=left, right_numerators=right,
                         denominator=82014183),
        cover_number=2,
    ), manifest)
    print('RN44_COVER_EXACTLY_TWO_PASS', flush=True)

    D = a['vertices'][0][3]
    core_data = dict(name='RN44_CORE33', denominator=D,
                     points=[a['vertices'][i][:3] for i in Y])
    core = e.audit(core_data, True)
    bodies = {'RN44_CORE33': core}
    put('RN44_CORE33.json', core_data, manifest)
    put('RN44_CORE33_audit.json', core, manifest)
    put('RN44_CORE33_independent.json', independent(core), manifest)

    specifications = [
        ('RN44_INNER', [p[0] for p in INTERVALS]),
        ('RN44_OUTER', [p[1] for p in INTERVALS]),
        ('RN44_MID', [(lo + hi) / 2 for lo, hi in INTERVALS]),
        ('RN44_BROAD', [max(e.dot(N[0], p) for p in v) + 1, F(500)]),
    ]
    for name, heights in specifications:
        data, audit = construct(a, v, H, heights, name)
        bodies[name] = audit
        put(name + '.json', data, manifest)
        put(name + '_audit.json', audit, manifest)
        put(name + '_independent.json', independent(audit), manifest)

    for name, audit in bodies.items():
        print('RN44_FULL_AUDIT', name,
              audit['V'], audit['E'], audit['F'],
              audit['strict'], audit['additional_weak'],
              len(audit['physical']['positive_bars']),
              len(audit['polar']['positive_bars']), flush=True)

    Utests = []
    for epsilon in [F(0), F(1, 4096), F(1, 1024), F(1, 256)]:
        test = unstable_envelope(
            bodies['RN44_INNER'], bodies['RN44_OUTER'], v, epsilon)
        Utests.append(test)
        print('RN44_U_ENVELOPE_' + ('PASS' if test['passed'] else 'NOT_CERTIFIED'),
              str(epsilon), flush=True)
    put('RN44_U_ENVELOPE.json', Utests, manifest)

    Stests = []
    for outer_name, epsilon in [
        ('RN44_OUTER', F(0)),
        ('RN44_BROAD', F(0)),
        ('RN44_BROAD', F(1, 1024)),
    ]:
        test = stable_patches(a, v, H, core, bodies[outer_name], epsilon)
        test['outer'] = outer_name
        Stests.append(test)
        faces = test['certified_parent_faces']
        print('RN44_S_ENVELOPE_' + ('PASS' if len(faces) >= 2 else 'NOT_CERTIFIED'),
              outer_name, str(epsilon), faces, flush=True)
    put('RN44_S_ENVELOPE.json', Stests, manifest)

    # All byte counts and hashes are generated, never filled from estimates.
    e.write('RN44_MANIFEST.json', manifest)
    print('RN44_PATCH_REPLAY_COMPLETE', len(bodies), len(manifest), flush=True)
    if '--nominate' in sys.argv:
        nominate(v)


if __name__ == '__main__':
    main()
```
