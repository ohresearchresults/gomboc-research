# Clear Atlas 56 — coupled primal-star moments and a contact-surgery continuation

## 1. Status and evidence boundary

**No new C<624 own-centroid strict110/weak000 endpoint is promoted by this handoff.** The accepted constructions and completed audits in the immutable parent remain parent evidence, not executions of this continuation.

The retained turn contains proposed searches and audit invocations, but not readable new terminal receipts sufficient to establish their outcomes. I am therefore not counting an invoked audit as a completed audit, reporting uninspected numerical output as an exact census, or assigning new hashes to uninspected files. The scratch descendants remain **unaccepted and ephemeral**. In particular, no new classification of the proposed coupled-star, compensator, relay, or full-contact-search endpoints is asserted below.

The durable contribution is an exact derivation of the **joint filled-volume and first-moment law**, a consequent rational compensation mechanism, and a more flexible finite cap reconstruction. These distinguish actual geometric coupling from an unjustified sum of isolated-star formulas. The complete new method source is included in Section 7. It is an extension to the unchanged literal parent sources, **not a purported recovery capsule for a newly accepted coordinate endpoint**.

The authoritative parent is **asg_hLx0kp6S8DK1LdqokerkVr6R**, tagged SHA-256 `e0df11674e3a73f23bd5f91802800b15773bf62057b91d4a653033c411d41b92`. Its coordinate input `PARENT_S8.json` is the distinct **COORD_CAP_RL_C624_STRONG_G8**, 9599 bytes, SHA-256 `bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2`. The supplied S8 has V177/E312/F137, own110/weak000. The parent also supplies the separately accepted low-arithmetic C624 variants; none is to be relabelled as literal S8. fileciteturn11file2L130-L144

The two relevant parent surgeries retain their exact identities:

- **STAR7:** original physical vertex7 moves to its positive endpoint; original5 loses extremality; original supports4/10 coalesce. The parent reports V176/E310/F136, C620, own211/weak000.
- **STAR111:** original physical111 moves to its negative endpoint; original107 loses extremality; supports135/136 coalesce. The parent reports V176/E310/F136, C620, own121/weak000. Its extra unstable final vertex107 is **not** the deleted original107. fileciteturn11file2L250-L271

The coordinator's 24 fixed-shape affine-metric starts are finite negative numerical evidence, not an affine impossibility theorem. They do not certify the new coupled families considered here. fileciteturn11file1L49-L55

## 2. Exact joint-star moment law

### Geometric hypotheses

Start with a convex polyhedron with an outward-oriented maximal-facet complex. A selected physical vertex i has degree three, two triangular incident facets, and one nontriangular incident facet. Let a_i and b_i be its two neighbours on the nontriangular facet and c_i its third neighbour. Define

```text
d_i = p_b_i - p_a_i,
p_i(t_i) = p_i + t_i d_i,
w_i = Vol(conv(p_c_i,p_a_i,p_i,p_b_i)),
K_i = (w_i/4) d_i.
```

All unselected physical points remain fixed. Each selected point therefore stays in its original nontriangular facet plane. The discussion concerns parameter values for which this moved boundary, or its correctly coarsened limit, is the actual convex boundary. That geometric condition must be checked; moment identities do not establish it by themselves.

For every nontriangular facet, choose a **fixed rational point in its original plane**, for example the original vertex average, and triangulate its boundary to that fixed point. Keep triangular facets as triangles. This is an integration mesh only: its diagonals are not true polyhedral edges.

Every boundary triangle now has affine vertex coordinates. Its determinant and first-moment contribution can be expanded exactly. Thus the actual filled moments, whenever the geometric hypotheses hold, are finite polynomials in the star parameters.

### The interaction formula

Suppose no original triangular facet has three selected vertices. Then the volume has degree at most two and the first moments have degree at most three. More specifically,

```text
V(t) = V0 + sum_(i,j) a_ij t_i t_j,

M(t) = M0 + sum_i K_i t_i
       + sum_(i,j) t_i t_j
           [B_ij + (a_ij/4)(t_i d_i + t_j d_j)].
```

The sums over distinct pairs need include **only original true edges joining two selected vertices**. Here a_ij is rational and B_ij is a rational three-vector, obtained by the exact determinant expansion.

This is a statement about the uniformly filled three-dimensional body. M is not a vertex average or surface moment.

The derivation is direct. A fixed-point facet fan has two moving vertices only when those vertices are endpoints of an original boundary edge. A triangular facet also has two moving vertices only on a true edge. A determinant with two moving arguments supplies the t_i t_j term. Multiplying that determinant by the sum of its triangle vertices in the tetrahedral first-moment formula supplies the cubic terms, with coefficient a_ij d_i/4 or a_ij d_j/4. Pure one-variable terms reduce to the isolated tetrahedral replacement: its volume is constant and its first moment changes by K_i t_i.

If an original triangle has three selected vertices, the general determinant algorithm remains valid, but the shortened quadratic/cubic formula must not be used without checking the extra terms. The supplied code detects this situation rather than silently imposing the simpler formula.

### Consequence: nonadjacent moving vertices really are additive

If the selected vertices form an independent set in the **original true-edge graph**, all pair interactions vanish:

```text
V(t) = V0,
M(t) = M0 + sum_i K_i t_i,
g(t) = g0 + (sum_i K_i t_i)/V0.
```

This remains true when the stars share a nontriangular facet or a fixed neighbour. The proof does not assume that a collection of intuitively drawn tetrahedra is disjoint. It follows from the complete boundary integral and the absence of any integration triangle containing two moving vertices.

For adjacent stars, additivity is generally false. The a_ij and B_ij terms must be retained. Consequently, choosing compensators from a moment Jacobian and then using a sum of isolated-star formulas at a finite endpoint is not justified unless the interaction terms vanish or are explicitly included.

The literal journal lists 25 eligible S8 physical labels:

```text
0,2,5,7,8,16,21,36,51,61,74,83,87,91,93,96,98,102,103,
105,107,111,113,122,139.
```

These are original physical labels, not support IDs. Their actual directions, isolated intervals, adjacency relations and coefficients should be regenerated from the literal geometry. No common numerical parameter box is assumed to contain all 25 isolated intervals. fileciteturn10file0L8-L10

## 3. Rational first-moment control and its limits

Take a primary finite surgery and three compensating star motions whose moving vertices are mutually nonadjacent and have no interaction with the primary moving vertices. If the primary changes volume and moment by DeltaV and DeltaM, preservation of the original own centroid requires

```text
[K_1 K_2 K_3] s = g0 DeltaV - DeltaM.
```

For a volume-neutral primary star this becomes

```text
[K_1 K_2 K_3] s = -DeltaM.
```

When the rational 3-by-3 matrix is nonsingular, the compensation is rational and exact. In the volume-neutral case it preserves V0 and M0, not merely an approximation to g0. No density variation, external point mass or independently prescribed centre is introduced.

There are three separate gates:

1. The algebraic moment system must be solvable.
2. The simultaneous moved boundary must be the actual convex hull with the claimed maximal incidence.
3. That hull, at its own integrated centroid, must pass the complete strict and weak equilibrium census.

The first gate does not imply either of the others. In particular, preserving the old centroid does not repair a lost ascent step, and compensating stars can introduce their own stable or unstable equilibria.

The source below makes three fully specified **proposed trials**, without assigning them unobserved endpoint classes:

```text
PAIR:
    original7 at its isolated upper endpoint,
    original111 at its isolated lower endpoint.

COMP111:
    original111 at its isolated lower endpoint,
    solve exact moment compensation using original0,16,74.

COMP7:
    original7 at its isolated upper endpoint,
    solve exact moment compensation using original0,21,87.
```

For each trial the code checks the independent-set condition, derives every interval and parameter rationally, checks all moved support inequalities, and can invoke the parent's two independent auditors. It does not assume that the two isolated endpoint quotients simply add their changes in V/E/F.

## 4. A cap reconstruction that spends the edge budget differently

The cap branch should not be restricted to moving the original bad vertex along its original line.

### Three-intercept construction

Consider an independently reconstructed convex body K* with a simple vertex T and its three actual neighbours A, B, C. Write u=A-T, v=B-T and w=C-T. For rational parameters 0<alpha,beta,gamma<1, cut T by the plane through

```text
L = T + alpha u,
R = T + beta v,
D = T + gamma w.
```

If the cut removes only that vertex, its removed tetrahedron has

```text
W_removed = abs(det(u,v,w)) alpha beta gamma / 6,
centroid_removed = T + (alpha u + beta v + gamma w)/4.
```

Therefore

```text
V_new = V_* - W_removed,
M_new = M_* - W_removed * centroid_removed.
```

These are exact finite moment formulas. A prescribed volume can be enforced by solving the product alpha beta gamma rationally, provided the resulting parameters and geometry are admissible. This does not simultaneously prescribe the first moments.

A simple-vertex truncation changes the maximal f-vector by (+2,+3,+1). Those changes may be used only after simplicity, the neighbour set and the absence of additional cut vertices have been established. They must not be imported from a drawing.

For the proposed S8 cap, the natural candidate T is the intersection of original supports135,73,71, with rays toward original103,117,69. Removing supports17 and136 is a way to propose K*, but **the stated simple-vertex hypotheses and the actual maximal complex still require verification**. No new C622 or C616 census for this proposal is claimed here.

### Releasing the fixed rays

A fixed-ray truncation can have too little angular freedom even after its moments are corrected. The following seven rational controls give a larger finite primal construction while retaining a compact exact definition.

Move the two interface points along surviving facet-intersection lines:

```text
A = p103 + s (p103-p100),
B = p117 + t (p117-p106).
```

Move T in the fixed plane of support71 using two free coordinates. Define a new support135 through p69,A,T and a new support73 through p69,B,T. Define the new physical120 as the intersection of support3, support72 and the new support73. Finally use three intercepts alpha,beta,gamma on T-A, T-B and T-p69, and put the new support17 through their three cut points.

Keep the other original support equations, omit original136, and omit old physical107,111,114 from the proposed physical cloud. This changes real planes and vertices; it is not a global affine metric or a reassignment of the centre.

The intended incidence relationships are gates, not assumptions to conceal: original103 and100 must lie on71/134; original117 and106 on71/72; original120 on3/72/73; and original69 on the specified cap planes. The code checks these against the literal input and stops on a mismatch. It also checks all proposed physical points against all new halfspaces. Full hull/vertex-set binding remains an independent audit gate.

This construction deliberately changes the interface that a fixed-ray obstruction would hold fixed. Its seven controls do **not** prove the existence of a favourable mechanical chamber. No numerical success, exhaustive search or exact endpoint is attributed to this family in the present handoff.

## 5. Finite ascent tests that should precede another repair

### Path-energy test

For an edge ascent relative to the actual centre g,

```text
2 (p_i-g)·(p_j-p_i)
    = |p_j-g|² - |p_i-g|² - |p_j-p_i|².
```

Thus any strict ascent path with at most n links from a to b satisfies

```text
n (|b-g|²-|a-g|²) > |b-a|².
```

If |g-g0|_infinity<=rho, a sufficient exact obstruction is

```text
|b-a|² - n(|b-g0|²-|a-g0|²)
          - 2 n rho |b-a|_1 >= 0.
```

This excludes the specified path length and fixed interface. To turn it into an equilibrium obstruction, one must also prove that a positive route cannot leave through another exterior port, and account for the desired root. The energy inequality alone does not establish that graph-theoretic condition.

For coupled affine star motions, a rational bound on the **actual** own centroid follows from the complete moment polynomials. Set

```text
N_k(t) = M_k(t) - g0_k V(t).
```

If a parameter box gives V(t)>=Vmin>0 and |N_k(t)|<=B_k, then |g_k(t)-g0_k|<=B_k/Vmin. Bounding coefficients of N_k is preferable to pretending that g is an independent free variable. The source computes this bound from the full polynomials, including adjacent-star interactions.

### A stricter test for the three-intercept detour

At a fixed candidate centre, put z=T-g and define

```text
U=u·u, V=v·v, W=w·w,
uv=u·v, uw=u·w, vw=v·w,
x=z·u, y=z·v, zeta=z·w.
```

For a required route A→L→D→R→B, the two middle ascent conditions include

```text
F = gamma*zeta + alpha*(gamma*uw-x) - alpha²*U > 0,
G = beta*(y+gamma*vw) - gamma*zeta - gamma²*W > 0.
```

Maximizing F over all real alpha gives the necessary inequality

```text
A(gamma) = (gamma*uw-x)² + 4*U*gamma*zeta > 0.
```

The last ascent R→B requires beta>-y/V. On the branch y+gamma*vw<0, this yields the additional necessary inequality

```text
B(gamma) = -y²/V
           + gamma*(-y*vw/V-zeta)
           - gamma²*W > 0.
```

These necessary conditions can be incompatible even when a crude hop-count test allows four links. For example, a rational separator c* can certify incompatibility if A is nonpositive throughout [c*,1] and B is nonpositive throughout [0,c*]. Convexity of A in gamma permits endpoint bounds on the first interval; a derivative bound and an endpoint bound can handle the second. Uniform rational bounds on the actual centre must be propagated through x,y,zeta.

**No particular S8 separator, centroid box or exclusion certificate is claimed to have completed in this turn.** The expressions above are the exact tests to evaluate. They do not exclude moving the interface, changing the rays, adding a genuine escape vertex, changing the metric, or leaving the certified centre region. They are independent of the separate K99 obstruction in the journal.

## 6. What remains unresolved

The important unresolved computational questions are the actual joint hulls and mechanical chambers, not whether a formal moment matrix has rank three. The first exact checks should bind each proposed H-body to the moved physical cloud and compare its independently integrated moments with the joint polynomial. Only then should its actual maximal C and strict/weak census be reported.

For STAR111-type repairs, evaluate the fixed-interface path and detour conditions before spending another large optimization run inside that same architecture. For STAR7, a corresponding polar analysis would need to control **all** exterior ports; it cannot simply borrow the primal cap argument. Moving a neighbouring support can open an escape that a prematurely frozen path model would miss.

The scratch labels PAIR, COMP111, COMP7, KFULL, TRUNC_NEUTRAL, TRUNC_RELAY, NL111, NL7 and RELEASE7 refer to exploratory definitions or invocations, not accepted new records. Their uninspected files, if retained locally, are supplemental scratch only. No new arithmetic-cost table or terminal SHA-256 receipt is supplied for them.

C<32 was not part of this work. There is no global-minimum claim, no unrestricted-geometry exclusion, no claim of a continuous no-birth path, and no resolution of the pending original-proof applicability of the two nine/nine bounds.

## 7. Complete runnable method extension

This source requires the **unchanged decoded 26-source parent capsule already supplied with the assignment**. Its normalized base85 identity is41775 characters, SHA-256 `9372158b106c03f1804a225bf3636814fe72535cdf690bfdd24ba1cf2d61eb9d`; decoded source-map JSON is112244 bytes, SHA-256 `75670b87e53f119fa26c5127589e0dfb63d5a4ac986cdb755de7e67d5b5d9360`.

The source verifies the parent manifest and the literal S8 generator. All new algebraic helpers are included below. The optional full audits explicitly use the two complete independent auditors and third-mass implementation in that literal parent; no different or unlisted verifier is substituted.

Save as `COUPLED_STAR_METHOD.py`. Intended environment: CPython3.13.5, standard library, assertions enabled. **Execution of this new source is not claimed witnessed in the retained turn.** Its printed terminal markers are expected outputs, not reported completed checks.

```python
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
from math import gcd, lcm
import argparse, hashlib, importlib, json, sys

sys.set_int_max_str_digits(0)
assert __debug__, 'Do not use Python -O'


def encode(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'),
                      default=str).encode('utf-8')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def save(path, obj):
    data = encode(obj)
    path.write_bytes(data)
    return {'bytes': len(data), 'sha256': digest(data)}


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def sub(a, b):
    return [x-y for x, y in zip(a, b)]


def scale(s, a):
    return [s*x for x in a]


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


def det(a, b, c):
    return dot(a, cross(b, c))


def solve(rows, rhs):
    n = len(rows)
    assert len(rhs) == n and all(len(r) == n for r in rows)
    A = [[F(v) for v in r] + [F(h)] for r, h in zip(rows, rhs)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if A[i][k]), None)
        if pivot is None:
            raise ArithmeticError('Singular rational solve')
        A[k], A[pivot] = A[pivot], A[k]
        a = A[k][k]
        A[k] = [v/a for v in A[k]]
        for i in range(n):
            if i != k:
                a = A[i][k]
                A[i] = [x-a*y for x, y in zip(A[i], A[k])]
    return [r[-1] for r in A]


def plane(a, b, c):
    n = cross(sub(b, a), sub(c, a))
    return n, dot(n, a)


def primitive(n, h):
    assert h > 0
    vals = list(n) + [h]
    D = lcm(*(v.denominator for v in vals))
    row = [int(D*v) for v in vals]
    G = gcd(*row)
    return [v//G for v in row]


def edges(faces):
    result = {}
    for f, cy in enumerate(faces):
        for a, b in zip(cy, cy[1:] + cy[:1]):
            result.setdefault(tuple(sorted((a, b))), []).append(f)
    assert all(len(v) == 2 for v in result.values())
    return result


def owners(faces):
    n = 1 + max(max(cy) for cy in faces)
    return [[f for f, cy in enumerate(faces) if i in cy]
            for i in range(n)]


def mass(P, faces):
    D = F(0)
    L = [F(0)]*3
    for cy in faces:
        for j in range(1, len(cy)-1):
            a, b, c = [P[i] for i in (cy[0], cy[j], cy[j+1])]
            dd = det(a, b, c)
            assert dd > 0
            D += dd
            L = add(L, scale(dd, add(add(a, b), c)))
    assert D > 0
    return D/6, scale(F(1, 24), L)


def load_parent(root):
    manifest = json.loads((root/'MANIFEST.json').read_bytes())
    for name, spec in manifest.items():
        data = (root/name).read_bytes()
        assert len(data) == spec['bytes']
        assert digest(data) == spec['sha256']
    data = (root/'PARENT_S8.json').read_bytes()
    assert len(data) == 9599
    assert digest(data) == (
        'bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2')
    d = json.loads(data)
    faces = json.loads((root/'FACES_S8.json').read_bytes())
    n = d['n_supports']
    assert n == 137
    den = d.get('denominators', [d['grid']]*len(d['controls']))
    X = [[F(v, D) for v in row] for row, D in zip(d['controls'], den)]
    X[n] = [F(0), F(0), F(1)]
    seen = {n}
    for i, deps, axes in d['plan']:
        assert i not in seen and all(j in seen for j in deps)
        assert len(deps) == len(axes)
        free = [k for k in range(3) if k not in axes]
        if deps:
            rows = [[X[j][k] for k in axes] for j in deps]
            rhs = [1-sum(X[j][k]*X[i][k] for k in free) for j in deps]
            for k, v in zip(axes, solve(rows, rhs)):
                X[i][k] = v
        seen.add(i)
    assert seen == set(range(len(X)))
    assert len(X) == n + len(d['groups'])
    for i, group in enumerate(d['groups']):
        assert all(dot(X[f], X[n+i]) == 1 for f in group)
    q = X[:n]
    own = owners(faces)
    P = []
    for oo in own:
        p = None
        for tri in combinations(oo, 3):
            try:
                p = solve([q[f] for f in tri], [F(1)]*3)
                break
            except ArithmeticError:
                pass
        assert p is not None
        assert all(dot(q[f], p) == 1 for f in oo)
        assert all(dot(q[f], p) < 1 for f in range(n) if f not in oo)
        P.append(p)
    assert P == sorted(P), 'Do not silently reinterpret physical labels'
    ee = edges(faces)
    assert (len(P), len(ee), len(faces)) == (177, 312, 137)
    V, M = mass(P, faces)
    return P, q, faces, V, M


def star(P, faces, i):
    ee = edges(faces)
    oo = owners(faces)[i]
    tri = [f for f in oo if len(faces[f]) == 3]
    large = [f for f in oo if len(faces[f]) > 3]
    neigh = sorted({b if a == i else a for a, b in ee if i in (a, b)})
    assert len(neigh) == 3 and len(tri) == 2 and len(large) == 1
    cy = faces[large[0]]
    k = cy.index(i)
    a, b = cy[k-1], cy[(k+1) % len(cy)]
    c = next(v for v in neigh if v not in (a, b))
    direction = sub(P[b], P[a])
    w = abs(det(sub(P[a], P[c]), sub(P[i], P[c]), sub(P[b], P[c])))/6
    assert w > 0
    K = scale(w/4, direction)
    lower, upper = None, None

    def constrain(alpha, beta):
        nonlocal lower, upper
        assert alpha >= 0
        if beta > 0:
            bound = -alpha/beta
            lower = bound if lower is None else max(lower, bound)
        elif beta < 0:
            bound = -alpha/beta
            upper = bound if upper is None else min(upper, bound)

    for f, fc in enumerate(faces):
        n0, h0 = plane(*(P[j] for j in fc[:3]))
        assert h0 > 0
        dn, dh = [F(0)]*3, F(0)
        if f in tri:
            test = [add(P[j], direction) if j == i else P[j] for j in fc]
            n1, h1 = plane(*test)
            dn, dh = sub(n1, n0), h1-h0
        constrain(h0, dh)
        for j, p in enumerate(P):
            dp = direction if j == i else [F(0)]*3
            assert dot(dn, dp) == 0
            constrain(h0-dot(n0, p), dh-dot(dn, p)-dot(n0, dp))
    assert lower is not None and upper is not None
    assert lower < 0 < upper
    return {'vertex': i, 'a': a, 'b': b, 'c': c,
            'triangles': tri, 'nontriangle': large[0],
            'direction': direction, 'w': w, 'K': K,
            'interval': [lower, upper]}


def eligible(P, faces):
    result = {}
    for i in range(len(P)):
        try:
            result[i] = star(P, faces, i)
        except AssertionError:
            pass
    return result


def pa(a, b):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, F(0)) + v
        if not r[k]:
            del r[k]
    return r


def ps(a, s):
    return {k: s*v for k, v in a.items() if s*v}


def pm(a, b):
    r = {}
    for i, x in a.items():
        for j, y in b.items():
            k = tuple(sorted(i+j))
            r[k] = r.get(k, F(0)) + x*y
    return {k: v for k, v in r.items() if v}


def pc(x):
    return {(): F(x)} if x else {}


def pdet(a, b, c):
    result = {}
    for i, j, k in [(0,1,2), (1,2,0), (2,0,1)]:
        result = pa(result, pm(a[i], pm(b[j], c[k])))
        result = pa(result, ps(pm(a[i], pm(b[k], c[j])), -1))
    return result


def peval(p, t):
    result = F(0)
    for key, value in p.items():
        for i in key:
            value *= t.get(i, F(0))
        result += value
    return result


def moments_polynomial(P, faces, stars):
    X = []
    for i, p in enumerate(P):
        row = [pc(v) for v in p]
        if i in stars:
            for k in range(3):
                row[k] = pa(row[k], {(i,): stars[i]['direction'][k]})
        X.append(row)
    VP, MP = {}, [{}, {}, {}]
    for cy in faces:
        if len(cy) == 3:
            triangles = [[X[i] for i in cy]]
        else:
            centre = [sum(P[i][k] for i in cy)/len(cy) for k in range(3)]
            fixed = [pc(v) for v in centre]
            triangles = [[fixed, X[i], X[j]]
                         for i, j in zip(cy, cy[1:]+cy[:1])]
        for a, b, c in triangles:
            D = pdet(a, b, c)
            VP = pa(VP, ps(D, F(1, 6)))
            for k in range(3):
                total = pa(pa(a[k], b[k]), c[k])
                MP[k] = pa(MP[k], ps(pm(D, total), F(1, 24)))
    V0, M0 = mass(P, faces)
    assert VP.get((), F(0)) == V0
    assert [p.get((), F(0)) for p in MP] == M0
    for i, s in stars.items():
        assert VP.get((i,), F(0)) == 0
        assert [p.get((i,), F(0)) for p in MP] == s['K']
    triple_selected = [cy for cy in faces
                       if len(cy) == 3 and all(i in stars for i in cy)]
    if not triple_selected:
        ee = edges(faces)
        assert all(len(k) <= 2 for k in VP)
        assert all(len(k) <= 3 for p in MP for k in p)
        for key, value in VP.items():
            if not key:
                continue
            assert len(key) == 2 and key[0] != key[1] and key in ee
            i, j = key
            for k in range(3):
                assert MP[k].get(tuple(sorted((i,i,j))), F(0)) == (
                    value*stars[i]['direction'][k]/4)
                assert MP[k].get(tuple(sorted((i,j,j))), F(0)) == (
                    value*stars[j]['direction'][k]/4)
    return VP, MP, triple_selected


def polynomial_data(p):
    return [[list(k), str(v)] for k, v in sorted(p.items())]


def box_abs(p, radii):
    total = F(0)
    for key, value in p.items():
        term = abs(value)
        for i in key:
            term *= radii[i]
        total += term
    return total


def centroid_box(VP, MP, stars):
    V0 = VP[()]
    g0 = [p[()]/V0 for p in MP]
    radii = {i: max(abs(x) for x in s['interval']) for i, s in stars.items()}
    deltaV = dict(VP)
    deltaV.pop((), None)
    Vmin = V0-box_abs(deltaV, radii)
    if Vmin <= 0:
        return {'status': 'no_positive_volume_bound', 'Vmin': str(Vmin)}
    rho = []
    for k in range(3):
        N = pa(MP[k], ps(VP, -g0[k]))
        assert N.get((), F(0)) == 0
        rho.append(box_abs(N, radii)/Vmin)
    return {'status': 'formal_box_bound', 'Vmin': str(Vmin),
            'coordinate_bounds': list(map(str, rho)),
            'rho_infinity': str(max(rho)),
            'geometry_condition': 'valid moved boundary still required'}


def proposal_planes(P, X, faces):
    rows, origin = [], []
    index = {}
    for f, cy in enumerate(faces):
        if len(cy) == 3:
            n, h = plane(*(X[i] for i in cy))
            if not any(n):
                continue
        else:
            n, h = plane(*(P[i] for i in cy[:3]))
        assert h > 0
        assert all(dot(n, X[i]) == h for i in cy)
        assert all(dot(n, p) <= h for p in X)
        row = primitive(n, h)
        key = tuple(row)
        if key not in index:
            index[key] = len(rows)
            rows.append(row)
            origin.append([])
        origin[index[key]].append(f)
    return {'H': rows}, origin


def coupled_trial(P, faces, stars, primary, compensators):
    selected = set(primary) | set(compensators)
    ee = edges(faces)
    assert all(tuple(sorted((i,j))) not in ee
               for i, j in combinations(selected, 2))
    t = {i: stars[i]['interval'][side] for i, side in primary.items()}
    change = [F(0)]*3
    for i, value in t.items():
        change = add(change, scale(value, stars[i]['K']))
    if compensators:
        A = [[stars[i]['K'][k] for i in compensators] for k in range(3)]
        sol = solve(A, scale(-1, change))
        t.update(dict(zip(compensators, sol)))
    for i, value in t.items():
        lo, hi = stars[i]['interval']
        assert lo <= value <= hi
    X = [p[:] for p in P]
    for i, value in t.items():
        X[i] = add(X[i], scale(value, stars[i]['direction']))
    raw, aliases = proposal_planes(P, X, faces)
    return raw, X, {'parameters': {str(i): str(v) for i, v in t.items()},
                    'original_face_aliases': aliases}, t


def released_cap(P, q, values):
    s, t, tx, ty, alpha, beta, gamma = map(F, values)
    for i, oo in [(103,[71,134]), (100,[71,134]),
                  (117,[71,72]), (106,[71,72]),
                  (120,[3,72,73]), (69,[3,73,134,135])]:
        assert all(dot(q[f], P[i]) == 1 for f in oo)
    T = solve([q[135], q[73], q[71]], [F(1)]*3)
    drop = max(range(3), key=lambda k: abs(q[71][k]))
    free = [k for k in range(3) if k != drop]
    for k, value in zip(free, [tx, ty]):
        T[k] += value/20
    T[drop] = (1-sum(q[71][k]*T[k] for k in free))/q[71][drop]
    A = add(P[103], scale(s, sub(P[103], P[100])))
    B = add(P[117], scale(t, sub(P[117], P[106])))
    Q = [row[:] for row in q[:136]]

    def support(a, b, c):
        n, h = plane(a, b, c)
        assert h != 0
        return [v/h for v in n]

    Q[135] = support(P[69], A, T)
    Q[73] = support(P[69], B, T)
    p120 = solve([Q[3], Q[72], Q[73]], [F(1)]*3)
    L = add(T, scale(alpha, sub(A, T)))
    R = add(T, scale(beta, sub(B, T)))
    D = add(T, scale(gamma, sub(P[69], T)))
    Q[17] = support(L, R, D)
    X = [p[:] for p in P]
    X[103], X[117], X[120] = A, B, p120
    X = [p for i, p in enumerate(X) if i not in (107,111,114)] + [L,R,D]
    assert all(dot(n, p) <= 1 for n in Q for p in X)
    raw = {'H': [primitive(n, F(1)) for n in Q]}
    return raw, X, {'parameters': list(map(str, values)),
                    'removed_original_support': 136,
                    'changed_original_supports': [17,73,135],
                    'omitted_original_points': [107,111,114],
                    'new_points': ['L','R','D']}


def audit_binding(parent, raw, cloud, expected_mass, out):
    sys.path.insert(0, str(parent.resolve()))
    A = importlib.import_module('check_A')
    B = importlib.import_module('check_B')
    C = importlib.import_module('centred_mass')
    a = A.run(raw)
    save(out/'A.json', a)
    b = B.run(raw)
    save(out/'B.json', b)
    assert encode(a) == encode(b)
    vertices = [tuple(map(F, p)) for p in a['raw_vertices']]
    assert set(vertices) <= {tuple(p) for p in cloud}
    for p in cloud:
        assert all(dot(row[:3], p) <= row[3] for row in raw['H'])
    if expected_mass is not None:
        V, M = expected_mass
        assert F(a['ordinary_volume']) == V
        assert list(map(F, a['raw_first_moments'])) == M
    cm = C.run(a)
    save(out/'CENTRED_MASS.json', cm)
    return {'status': 'two_audits_and_mass_binding_completed',
            'V': len(a['raw_vertices']), 'E': len(a['edges']),
            'F': len(a['faces']), 'C': 2*len(a['edges']),
            'strict': a['counts'], 'weak': a['weak'],
            'report': {'bytes': len(encode(a)), 'sha256': digest(encode(a))},
            'disposition': 'not_promoted_pending_source_only_cold_replay'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--parent', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--audit', action='store_true')
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    P, q, faces, V0, M0 = load_parent(args.parent)
    stars = eligible(P, faces)
    VP, MP, triple_selected = moments_polynomial(P, faces, stars)
    save(args.out/'FORMAL_MOMENTS.json', {
        'eligible_original_vertices': sorted(stars),
        'stars': {str(i): s for i, s in stars.items()},
        'volume': polynomial_data(VP),
        'first_moments': [polynomial_data(p) for p in MP],
        'three_selected_triangles': triple_selected,
        'centroid_box': centroid_box(VP, MP, stars)})
    trials = [('PAIR', {7:1,111:0}, []),
              ('COMP111', {111:0}, [0,16,74]),
              ('COMP7', {7:1}, [0,21,87])]
    summaries = {}
    for name, primary, comp in trials:
        out = args.out/name
        out.mkdir()
        try:
            raw, cloud, definition, t = coupled_trial(P, faces, stars, primary, comp)
            V = peval(VP, t)
            M = [peval(p, t) for p in MP]
            assert V == V0
            direct = M0[:]
            for i, value in t.items():
                direct = add(direct, scale(value, stars[i]['K']))
            assert M == direct
            if comp:
                assert M == M0
            definition['formal_volume'] = str(V)
            definition['formal_first_moments'] = list(map(str, M))
            save(out/'DEFINITION.json', definition)
            save(out/'RAW_PROPOSAL.json', raw)
            save(out/'PRIMAL_CLOUD.json', cloud)
            summaries[name] = {'status': 'support_checks_only_not_a_full_hull_audit'}
            if args.audit:
                summaries[name] = audit_binding(args.parent, raw, cloud, (V,M), out)
        except (AssertionError, ArithmeticError, ValueError) as error:
            summaries[name] = {'status': 'rejected_or_incomplete',
                               'error': type(error).__name__ + ': ' + str(error)}
        save(out/'STATUS.json', summaries[name])
    out = args.out/'RELEASED_CAP_PROPOSAL'
    out.mkdir()
    try:
        values = [F(0),F(0),F(0),F(0),F(8,15),F(10,21),F(3,250)]
        raw, cloud, definition = released_cap(P, q, values)
        save(out/'DEFINITION.json', definition)
        save(out/'RAW_PROPOSAL.json', raw)
        save(out/'PRIMAL_CLOUD.json', cloud)
        result = {'status': 'support_checks_only_not_a_full_hull_audit'}
        if args.audit:
            result = audit_binding(args.parent, raw, cloud, None, out)
    except (AssertionError, ArithmeticError, ValueError) as error:
        result = {'status': 'rejected_or_incomplete',
                  'error': type(error).__name__ + ': ' + str(error)}
    summaries['RELEASED_CAP_PROPOSAL'] = result
    save(out/'STATUS.json', result)
    save(args.out/'SUMMARY.json', summaries)
    files = {}
    for path in sorted(args.out.rglob('*')):
        if path.is_file():
            data = path.read_bytes()
            files[str(path.relative_to(args.out))] = {
                'bytes': len(data), 'sha256': digest(data)}
    save(args.out/'OUTPUT_MANIFEST.json', files)
    print('COUPLED_STAR_METHOD_FINISHED_READ_EACH_STATUS', flush=True)


if __name__ == '__main__':
    main()
```

Commands, after restoring the unchanged literal parent capsule:

```sh
python -B -S COUPLED_STAR_METHOD.py --parent exact-parent --out formal-proposals
python -B -S COUPLED_STAR_METHOD.py --parent exact-parent --out audited-proposals --audit
```

The two output directories must initially be absent. The first command is not an equilibrium verification. The second invokes both complete parent auditors and the third mass implementation, and binds the audited hull to the proposed physical cloud; its actual per-case statuses must be read. It still does not supply an already witnessed source-only cold replay in this handoff.

**The proofs and complete method extension above are the durable result. The uninspected scratch coordinate objects are not durable successors to the last reconstructible parent.**