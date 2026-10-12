# figure-0439

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Quiet Comet52 — fixed-volume gate-opening countercontrols and their remaining physical basin

## Disposition

**No new verified own110/additionalweak000 endpoint is supplied.** The construction entrance remains **QC52_SURVIVING_ROOT124_G9_F8B57E0F**. The attempted full-contact numerical continuations do not have sufficiently reliable terminal readback in this turn to support a new endpoint, iteration-count claim, or exclusion claim. I do not promote their checkpoints.

The mathematical result is an **exact, fixed-volume, rational affine countercontrol family derived from this specific parent**. It preserves the maximal complex and the strict stability of the existing stable facet. Both the retained-chord gate L and the sharper planar gate Psi eventually pass. Nevertheless, the complete physical radial landscape necessarily retains at least two **strict** unstable equilibria, and a nonessential physical persistence bar grows without bound while volume remains exactly fixed.

This distinguishes two different assertions:

- Crossing L and Psi genuinely removes the stated local two-link obstruction.
- It does not, even with the original stable facet retained and no additional edges spent, imply improvement of the complete unwanted physical basin.

The family and its obstruction are proved below. The supplied exact constructor also invokes the existing independent whole-feature auditors and computes both complete physical and same-physical-centroid polar merge trees. **Those new constructor/auditor terminal markers are expected, not newly observed in this turn.** Accordingly, this is an analytical family and a scoped exclusion, not a newly accepted full-census endpoint.

## 1. Exact entrance and source boundary

The defining parent is the literal22-file capsule in `figure-0434`, SHA256 `037b2078e4f89986594472b0f6e0df78ecf3cb43bbfb82dee2eea017099c529f`.

Its surviving G9 generator is10178bytes, SHA256 `f8b57e0f2b61c5c91093b6e989e7bc15486cb69a5e0e1a5458abc9cbe7684241`; RAW is11693bytes, SHA256 `a2a309b2b8ed47fdeeeccc0b30a6eec38ee3e9bb030869fcbb221c0407eb4f2e`; A=B is230639bytes, SHA256 `bf713a4201231250cfb98d45cc35f47f27afee73a7938f700ce51359ef3b19f5`.

The parent has V174/E308/F136, own strict121/additionalweak000, stable input3, unstable vertices94 and124, and saddle124--134. The source-specific star is u124,w120,z134,q109. The complete physical elder bar is in[418537478,418537479]/10^12 after division by V^(2/3). These are inherited certified facts, not newly computed statistics in this turn. The unrecovered8adb/6212 object, own132 DROPFB30 alias, and d<L/16 navigation conflation are not used.

The second literal parent, `figure-0436`, SHA256 `03f411835ef54fbd0de37d4a09ec0580c3c6e84b257141d04d9133166d893ae6`, supplies the coupled-chord identity and its precise hypotheses. I use its definition

`L = 4(w-g)·(z-w)+|z-w|²`,

not a substituted distance criterion.

The complete current journal and literal parents were read through EOF. No exact defining-parent dependency is missing. The limitation concerns verification of new numerical jobs, not access to the surviving construction.

## 2. A fixed-volume family which opens both gates

Write K for the exact surviving body, g for its actual filled centroid, and F for its existing strict stable facet. Let p be the perpendicular projection of g onto the plane of F. Put

`W=w-p`, `Z=z-p`,

`A0=W·W`, `B0=Z·Z`, `C0=W·Z`.

Choose a nonzero **rational tangent vector** v to F satisfying

`0 < a=W·v < b=Z·v`.

The program below selects v deterministically from integer combinations of two rational tangent basis vectors and checks these inequalities exactly. It also checks that W,Z are linearly independent. Under that condition the required open sector is nonempty: take a direction with positive Z projection and zero W projection, then perturb toward W. Density of rational directions supplies a rational member.

Let q=v·v and Pi=vv^T/q. For s>=1 define

`T_s = I+(s-1)Pi`,

`A_s = s^(-1/3) T_s`,

`K_s = A_s K`.

The eigenvalues of A_s are s^(2/3),s^(-1/3),s^(-1/3). Therefore det(A_s)=1. In particular,

**`Vol(K_s)=Vol(K)` and `g_s=A_s g` exactly.**

There is no free-reference recentering or point-mass substitution. An invertible linear image of a uniformly filled body remains uniformly filled, with constant Jacobian. Every face, vertex, edge and incidence is transported. Thus every member retains the true maximal f-vector174/308/136.

For an entirely rational discrete family, take

`s=8^k`, `s^(-1/3)=2^(-k)`, `k=0,1,2,...`.

Every matrix A_s then has rational entries, and the original volume is unchanged, not merely approximately normalized.

### The original strict stable facet persists

Let n be the outward normal of F. Since v·n=0, T_s n=n. Before the final uniform rescaling, the plane of F is unchanged and its perpendicular foot transforms by T_s. Indeed,

`p=g+h*n/(n·n)` implies `T_s p=T_s g+h*n/(n·n)`.

The transformed foot is therefore the actual perpendicular foot of the actual new centroid. Its strict relative-interior membership in the transformed polygon follows from invertibility. Uniform rescaling preserves that membership. Hence F remains a **strict stable facet** throughout the family.

This is not a proof that F remains the **only** stable facet. Additional polar roots may appear; the recovery program counts them rather than assuming them absent.

### The retained-chord gate opens

Set t=s²-1. The planar Gram quantities before the final rescaling are

`A(t)=A0+t*a²/q`,

`B(t)=B0+t*b²/q`,

`C(t)=C0+t*a*b/q`.

Consequently

`L(K_s)=s^(-2/3) * [L0+t*(b-a)*(b+3a)/q]`,

where `L0=B0-3A0+2C0`.

The coefficient of t is strictly positive because0<a<b. Thus L(K_s)>0 for every sufficiently large s. This crosses the source-specific gate rather than merely reducing its negative magnitude.

### The sharper planar gate also opens

The sharp squared expression is

`Psi(K_s)=s^(-4/3) * [(2A(t)-C(t))²-A(t)B(t)]`.

The coefficient of t² in its bracket is

`4*a³*(a-b)/q² < 0`.

Therefore Psi(K_s)<0 for every sufficiently large s. At the entrance, L0<0 and A0>0 imply Psi0>0. The quadratic consequently has exactly one positive root; once the negative side is reached it remains negative for all larger s.

The construction thus passes **both** local gates while retaining the same edge budget and the original strict stable facet.

## 3. The complete physical obstruction survives—and becomes arbitrarily worse

Let r and R be the exact centered inradius and circumradius of the original K:

`r²=min_f (b_f-n_f·g)²/(n_f·n_f)`,

`R²=max_i |x_i-g|²`.

Both are positive rational squared quantities computed directly from the parent.

Consider the central section perpendicular to v. T_s acts as the identity on that section. After the determinant-one rescaling, its entire squared radius is at most

`s^(-2/3) R²`.

On the other hand, the centered original body contains the points ±r*v/|v|. Their images lie in opposite caps and have squared radius

`s^(4/3) r²`.

Hence, whenever

**`s² r² > R²`,**

each cap has a radial maximum strictly above the entire separating section. Each maximum occurs at an actual vertex away from the section. It is a **strict unstable vertex**: a positive incident radial derivative contradicts maximality, while a zero derivative would make squared radius increase quadratically along that edge. The two caps therefore provide two distinct strict U, irrespective of additional weak features or root-label changes.

The same separation gives a lower bound on at least one nonessential physical elder bar:

**`Delta_s >= s^(4/3)r²-s^(-2/3)R²`.**

Since volume is exactly fixed,

`Delta_s / Vol(K_s)^(2/3) -> +infinity`.

Meanwhile L becomes positive and Psi becomes negative with increasing magnitude. This is not a uniform-shrinking artifact, and it is not fragmentation into many numerically invisible bars: a **single genuine global physical bar** has the displayed positive lower bound.

### Exact scope

This excludes the sufficiently stretched tail of this particular tangent-stretch family from own110, including weak-boundary cases because two U are strict. It does **not** exclude the entire affine orbit, smaller parameters, general contact deformations, a changed stable interface, another exit from120, or radius-order reversal.

The underlying section argument is established shared background. The source-specific addition is the simultaneous construction of a fixed-volume, E308, stable-facet-preserving family in which **both of the proposed local cancellation gates pass while the complete physical obstruction can worsen without bound**.

## 4. What was attempted numerically, and what is not claimed

I attempted a full-contact gate continuation with physical/polar guards, a phase releasing physical-root guards while retaining the polar conditions, restoration of the physical conditions, and a movable-tip/facet-splitting construction. Reliable terminal readback sufficient to bind a new defining generator, rebuilt maximal complex, actual centroid, and complete P/Q census is not available for these jobs in this turn.

No reported numerical checkpoint from those attempts is used as a premise of the theorem above. I do not supply an invented new f-vector, gate value, solver success, iteration count, or whole-basin improvement. In particular, a numerical two-link point cannot be treated as an exposed polyhedral vertex without checking the actual supporting hull; and a gate-passing checkpoint cannot be called cancellation without its complete physical and polar components.

The analytical countercontrol and the exact program below remain usable without any such checkpoint.

## 5. Complete deterministic constructor and verifier

The only input dependency is the already literal22-file surviving parent. The program below:

1. Finds and hash-checks the exact surviving A report in the supplied parent proof directory.
2. Reconstructs all supporting planes from the actual maximal polygons.
3. Selects a rational tangent direction by exact inequalities.
4. Chooses the first s=8^k for which both gates pass and s²r²>4R².
5. Constructs the exact determinant-one affine image and its integer H-description.
6. Invokes the two complete existing auditors and the separate centered-mass implementation.
7. Checks exact affine covariance of vertices, volume and centroid.
8. Computes all physical and same-physical-centroid polar elder bars, with attaining paths and strict-upper cuts.
9. Checks the global physical-bar lower bound and emits all full-census files and exact construction parameters.

There is no optimizer, randomness, floating point, hidden checkpoint, or originating-sandbox dependency. `--extra-k` defaults to0 and selects a later rational member when positive. The full input matrices and every output receipt are written by the program; no unobserved output hash is asserted here.

Commands, starting with the complete recovery program in parent `figure-0434`:

```sh
python -B -S QC52_SURVIVING_RECOVER.py PARENT
python -B -S PARENT/RECONCILE_REPLAY.py --case ROOT124_G9 --out PARENT_PROOF
python -B -S QC52_TANGENTIAL_CONTROL.py PARENT PARENT_PROOF TANGENTIAL_CONTROL
```

Dependencies: Python3.11 or later, standard library only, assertions enabled. The inherited parent was executed on CPython3.13.5. The new program's terminal marker is **expected, not newly observed**:

`QC52_FIXED_VOLUME_TANGENTIAL_GATE_CONTROL_PASS`.

The newly generated A.json and B.json contain the complete actual strict and additional-weak feature census. Their values must be read from a completed run rather than inferred from the two-U theorem. Until that run is observed, no instantiated member is promoted as a newly audited endpoint.

```python
"""Exact fixed-volume tangent-stretch countercontrols for the surviving QC52 body.

Input: the complete literal 22-file surviving parent source and its pinned audit.
Output: a rational body, full A/B/mass audits, and both complete radial merge trees.
This is a negative-control family, not an own110 construction.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import deque
from functools import reduce
import argparse
import hashlib
import json
import math
import subprocess
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

PARENT_BYTES = 230639
PARENT_SHA = 'bf713a4201231250cfb98d45cc35f47f27afee73a7938f700ce51359ef3b19f5'
PARENT_ID = 'QC52_SURVIVING_ROOT124_G9_F8B57E0F'
SCALE = 10**12


def rat(x):
    if isinstance(x, (list, tuple)) and len(x) == 2:
        return F(x[0], x[1])
    return F(x)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def sub(a, b):
    return [x-y for x, y in zip(a, b)]


def mul(t, a):
    return [t*x for x in a]


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


def apply(M, x):
    return [dot(row, x) for row in M]


def determinant(M):
    return dot(M[0], cross(M[1], M[2]))


def primitive(values):
    values = [rat(x) for x in values]
    den = math.lcm(*(x.denominator for x in values))
    nums = [x.numerator*(den//x.denominator) for x in values]
    d = reduce(math.gcd, (abs(x) for x in nums))
    assert d > 0
    return [x//d for x in nums]


def plane(X, face, interior):
    a = X[face[0]]
    n = None
    for k in range(1, len(face)-1):
        candidate = cross(sub(X[face[k]], a), sub(X[face[k+1]], a))
        if dot(candidate, candidate) > 0:
            n = candidate
            break
    assert n is not None
    h = dot(n, a)
    if dot(n, interior) > h:
        n, h = mul(-1, n), -h
    assert dot(n, interior) < h
    out = primitive(n+[h])
    zero = {i for i, x in enumerate(X) if dot(out[:3], x) == out[3]}
    assert zero == set(face)
    assert all(dot(out[:3], x) <= out[3] for x in X)
    return out


def mass(X, faces, interior):
    D = F(0)
    N = [F(0), F(0), F(0)]
    for face in faces:
        h = plane(X, face, interior)
        a = X[face[0]]
        for k in range(1, len(face)-1):
            b, c = X[face[k]], X[face[k+1]]
            if dot(cross(sub(b, a), sub(c, a)), h[:3]) < 0:
                b, c = c, b
            det = dot(a, cross(b, c))
            D += det
            N = add(N, mul(det, add(add(a, b), c)))
    assert D > 0
    return D/6, [v/(4*D) for v in N]


def exact_bracket(x):
    x = rat(x)
    lo = (x.numerator*SCALE)//x.denominator
    return [lo, lo+1, SCALE]


def cube_root_bracket(x):
    x = rat(x)
    assert x >= 0
    target = x*SCALE**3
    lo, hi = 0, 1
    while hi**3 <= target:
        hi *= 2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid**3 <= target:
            lo = mid
        else:
            hi = mid
    return [lo, lo+1, SCALE]


def dump(path, obj):
    data = json.dumps(obj, sort_keys=True, separators=(',', ':')).encode('utf-8')
    Path(path).write_bytes(data)
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def pinned_parent(root):
    for path in sorted(Path(root).rglob('*.json')):
        if path.is_file() and path.stat().st_size == PARENT_BYTES:
            raw = path.read_bytes()
            if hashlib.sha256(raw).hexdigest() == PARENT_SHA:
                return json.loads(raw)
    raise ValueError('The exact surviving parent audit was not found')


def tangent_direction(n, W, Z):
    # Two independent integer vectors in n-perp.
    k = next(i for i in range(3) if n[i] != 0)
    other = [i for i in range(3) if i != k]
    basis = []
    for j in other:
        e = [0, 0, 0]
        e[j] = 1
        basis.append(cross(n, e))
    assert dot(cross(basis[0], basis[1]), cross(basis[0], basis[1])) > 0
    radius = 1
    while True:
        for i in range(-radius, radius+1):
            for j in range(-radius, radius+1):
                if max(abs(i), abs(j)) != radius:
                    continue
                v = add(mul(i, basis[0]), mul(j, basis[1]))
                if dot(v, v) == 0:
                    continue
                if 0 < dot(W, v) < dot(Z, v):
                    v = primitive(v)
                    assert dot(n, v) == 0
                    assert 0 < dot(W, v) < dot(Z, v)
                    return v, [i, j], radius
        radius += 1


def graph_edges(faces):
    owners = {}
    for fi, face in enumerate(faces):
        for i, j in zip(face, face[1:]+face[:1]):
            e = tuple(sorted((i, j)))
            owners.setdefault(e, []).append(fi)
    assert all(len(v) == 2 for v in owners.values())
    edges = sorted(owners)
    dual = sorted({tuple(sorted(v)) for v in owners.values()})
    assert len(dual) == len(edges)
    return edges, dual


def landscapes(X, edges, volume, polar=False):
    r2 = [dot(x, x) for x in X]
    levels = {}
    adj = [[] for _ in X]
    for i, j in edges:
        d = sub(X[j], X[i])
        dd = dot(d, d)
        assert dd > 0
        t = -dot(X[i], d)/dd
        if t <= 0:
            h = r2[i]
        elif t >= 1:
            h = r2[j]
        else:
            h = r2[i]-dot(X[i], d)**2/dd
        assert 0 <= h <= min(r2[i], r2[j])
        levels[i, j] = h
        adj[i].append(j)
        adj[j].append(i)
    roots = [i for i in range(len(X))
             if all(dot(X[i], sub(X[j], X[i])) < 0 for j in adj[i])]
    par = list(range(len(X)))
    elder = list(range(len(X)))

    def find(i):
        while par[i] != i:
            par[i] = par[par[i]]
            i = par[i]
        return i

    events = sorted(levels, key=lambda e: (-levels[e], e))
    bars = []
    for edge in events:
        i, j = edge
        a, b = find(i), find(j)
        if a == b:
            continue
        ra, rb = elder[a], elder[b]
        if (r2[ra], -ra) < (r2[rb], -rb):
            a, b = b, a
            ra, rb = rb, ra
        death = levels[edge]
        if r2[rb] > death:
            bars.append((rb, ra, death, edge))
        par[b] = a
        elder[a] = ra
    assert len({find(i) for i in range(len(X))}) == 1
    assert len(bars) == len(roots)-1

    def walk(start, h, strict):
        pred = {start: None}
        queue = deque([start])
        while queue:
            i = queue.popleft()
            for j in sorted(adj[i]):
                lev = levels[tuple(sorted((i, j)))]
                good = lev > h if strict else lev >= h
                if good and j not in pred:
                    pred[j] = i
                    queue.append(j)
        return pred

    reports = []
    deltas = []
    for peak, root, death, edge in bars:
        cut = set(walk(peak, death, True))
        assert root not in cut
        crossing = [e for e in edges if (e[0] in cut) != (e[1] in cut)]
        assert crossing and all(levels[e] <= death for e in crossing)
        pred = walk(peak, death, False)
        assert root in pred
        path, node = [], root
        while node is not None:
            path.append(node)
            node = pred[node]
        path.reverse()
        delta = r2[peak]-death
        deltas.append(delta)
        normalized_cube = delta**3*volume**2 if polar else delta**3/volume**2
        reports.append({
            'peak': peak, 'elder': root, 'death_edge': list(edge),
            'birth_squared': exact_bracket(r2[peak]),
            'death_squared': exact_bracket(death),
            'delta': exact_bracket(delta),
            'normalized_bar': cube_root_bracket(normalized_cube),
            'delta_over_R_squared': exact_bracket(delta/max(r2)),
            'strict_upper_component': sorted(cut),
            'complete_crossing_cut': [list(e) for e in crossing],
            'attaining_path': path,
        })
    return {'strict_radial_roots': roots, 'bars': reports,
            'normalization': 'delta*physical_volume^(2/3)' if polar
                             else 'delta/physical_volume^(2/3)'}, deltas


def run(script, *args):
    subprocess.run([sys.executable, '-B', '-S', str(script),
                    *(str(a) for a in args)], check=True)


def main():
    if not __debug__:
        raise RuntimeError('Assertions must be enabled')
    ap = argparse.ArgumentParser()
    ap.add_argument('parent_source')
    ap.add_argument('parent_proof')
    ap.add_argument('out')
    ap.add_argument('--extra-k', type=int, default=0)
    args = ap.parse_args()
    assert args.extra_k >= 0
    source = Path(args.parent_source)
    out = Path(args.out)
    assert not out.exists()
    parent = pinned_parent(args.parent_proof)
    assert [parent['V'], parent['E'], parent['F']] == [174, 308, 136]
    assert parent['counts'] == [1, 2, 1]
    X = [[rat(x) for x in p] for p in parent['raw_vertices']]
    g = [rat(x) for x in parent['raw_centroid']]
    faces = [list(f) for f in parent['faces']]
    H = [plane(X, f, g) for f in faces]
    V, gc = mass(X, faces, g)
    assert gc == g
    u, w, z = 124, 120, 134
    common = [i for i, f in enumerate(faces) if {u, w, z}.issubset(f)]
    assert len(common) == 1
    fi = common[0]
    n, h = H[fi][:3], F(H[fi][3])
    nn = dot(n, n)
    height = h-dot(n, g)
    foot = add(g, mul(height/nn, n))
    assert all(dot(row[:3], foot) < row[3]
               for j, row in enumerate(H) if j != fi)
    W, Z = sub(X[w], foot), sub(X[z], foot)
    A0, B0, C0 = dot(W, W), dot(Z, Z), dot(W, Z)
    assert A0 > 0 and B0 > 0 and A0*B0-C0*C0 > 0
    L0 = B0-3*A0+2*C0
    assert L0 <= -F(488499, 200000000)
    assert (2*A0-C0)**2-A0*B0 > 0
    v, basis_coefficients, shell = tangent_direction(n, W, Z)
    vv = dot(v, v)
    a, b = dot(W, v), dot(Z, v)
    assert 0 < a < b
    gate_coefficient = (b-a)*(b+3*a)/vv
    psi_leading = 4*a**3*(a-b)/vv**2
    assert gate_coefficient > 0 and psi_leading < 0
    centered = [sub(x, g) for x in X]
    R2 = max(dot(x, x) for x in centered)
    r2 = min((F(row[3])-dot(row[:3], g))**2/dot(row[:3], row[:3])
             for row in H)
    assert 0 < r2 <= R2

    def parameters(k):
        s = 8**k
        alpha = F(1, 2**k)
        t = s*s-1
        A = A0+t*a*a/vv
        B = B0+t*b*b/vv
        C = C0+t*a*b/vv
        L = alpha**2*(B-3*A+2*C)
        psi = alpha**4*((2*A-C)**2-A*B)
        lower = alpha**2*(s*s*r2-R2)
        return s, alpha, L, psi, lower

    k0 = 1
    while True:
        s, alpha, L, psi, lower = parameters(k0)
        if L > 0 and psi < 0 and s*s*r2 > 4*R2:
            break
        k0 += 1
    k = k0+args.extra_k
    s, alpha, L, psi, lower = parameters(k)
    assert L > 0 and psi < 0 and lower > 0
    M = [[alpha*(F(int(i == j))+(s-1)*v[i]*v[j]/vv)
          for j in range(3)] for i in range(3)]
    Minv = [[(F(int(i == j))-F(s-1, s)*v[i]*v[j]/vv)/alpha
             for j in range(3)] for i in range(3)]
    assert determinant(M) == 1
    assert all(dot(M[i], [Minv[k1][j] for k1 in range(3)]) == int(i == j)
               for i in range(3) for j in range(3))
    Y = [apply(M, x) for x in X]
    gy = apply(M, g)
    Hy = [primitive(apply(Minv, row[:3])+[F(row[3])]) for row in H]
    for fi1, row in enumerate(Hy):
        assert all(dot(row[:3], y) <= row[3] for y in Y)
        assert {i for i, y in enumerate(Y) if dot(row[:3], y) == row[3]} == set(faces[fi1])
    transformed_foot = apply(M, foot)
    row = Hy[fi]
    actual_foot = add(gy, mul((row[3]-dot(row[:3], gy))/dot(row[:3], row[:3]), row[:3]))
    assert transformed_foot == actual_foot
    assert all(dot(row1[:3], actual_foot) < row1[3]
               for j, row1 in enumerate(Hy) if j != fi)
    Vy, gcheck = mass(Y, faces, gy)
    assert Vy == V and gcheck == gy

    out.mkdir(parents=True)
    receipts = {}
    definition = {
        'parent': PARENT_ID, 'parent_A_sha256': PARENT_SHA,
        'axis_integer': v, 'basis_coefficients': basis_coefficients,
        'basis_search_shell': shell, 'first_admissible_k': k0,
        'extra_k': args.extra_k, 'k': k, 's': s,
        'matrix': [[str(x) for x in row] for row in M],
        'determinant': '1', 'volume_unchanged': True,
        'stable_source_facet_index': fi,
        'L': exact_bracket(L), 'Psi': exact_bracket(psi),
        'physical_bar_lower_bound': exact_bracket(lower),
        'normalized_physical_bar_lower_bound': cube_root_bracket(lower**3/V**2),
        'lower_bound_is_not_an_enclosure_of_actual_bar': True,
    }
    receipts['DEFINITION.json'] = dump(out/'DEFINITION.json', definition)
    receipts['RAW.json'] = dump(out/'RAW.json', {'H': Hy})
    core = source/'CN63'/'core'
    run(core/'check_A.py', out/'RAW.json', out/'A.json')
    run(core/'check_B.py', out/'RAW.json', out/'B.json')
    assert (out/'A.json').read_bytes() == (out/'B.json').read_bytes()
    run(core/'centred_mass.py', out/'A.json', out/'MASS.json')
    child = json.loads((out/'A.json').read_bytes())
    assert [child['V'], child['E'], child['F']] == [174, 308, 136]
    assert child['counts'][1] >= 2
    CX = [[rat(x) for x in p] for p in child['raw_vertices']]
    CG = [rat(x) for x in child['raw_centroid']]
    assert CG == gy and set(map(tuple, CX)) == set(map(tuple, Y))
    CF = [list(f) for f in child['faces']]
    CE, QE = graph_edges(CF)
    assert set(CE) == {tuple(sorted(e)) for e in child['edges']}
    CV, CC = mass(CX, CF, CG)
    assert CV == V and CC == CG
    CP = [sub(x, CG) for x in CX]
    CH = [plane(CX, f, CG) for f in CF]
    CQ = [mul(1/(F(row[3])-dot(row[:3], CG)), row[:3]) for row in CH]
    physical, drops = landscapes(CP, CE, V, False)
    polar, qdrops = landscapes(CQ, QE, V, True)
    assert drops and max(drops) >= lower
    assert len(physical['strict_radial_roots']) == child['counts'][1]
    assert len(polar['strict_radial_roots']) == child['counts'][0]
    receipts['PHYSICAL.json'] = dump(out/'PHYSICAL.json', physical)
    receipts['POLAR.json'] = dump(out/'POLAR.json', polar)
    for name in ['A.json', 'B.json', 'MASS.json']:
        raw = (out/name).read_bytes()
        receipts[name] = {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
    dump(out/'RECEIPTS.json', receipts)
    print('QC52_FIXED_VOLUME_TANGENTIAL_GATE_CONTROL_PASS')
    print(json.dumps({'k': k, 'strict_counts': child['counts'],
                      'physical_bars': len(physical['bars']),
                      'polar_bars': len(polar['bars']),
                      'definition': definition, 'receipts': receipts},
                     sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
```

## 6. Consequence for the construction direction

The coupled120--134 gate remains a valid necessary design constraint under its stated retained-star hypotheses. The new result shows why making L large and Psi negative must not become the next standalone merit: an exactly mass-preserving, E308, stable-facet-preserving deformation can improve both without bound while worsening a complete physical basin without bound.

The next finite construction must control the whole physical component and the same-center polar landscape during or after gate crossing, or deliberately change the actual local graph/exit assumptions. This result neither closes that broader direction nor supplies a new accepted successor. The surviving C616 entrance and the canonical C622 own110 incumbent remain unchanged.
