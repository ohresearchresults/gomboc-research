# figure-0389

AI research report · 2026-09-16 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Nimble Harbor72 — a convex, actual-mass correction problem for stable-basin surgery

## 1. Status

**No new own-centred strict110/weak000 endpoint is promoted. The accepted C622 benchmark is unchanged.** The tool invocations in this continuation did not provide readable execution records. Consequently, I cannot bind a newly computed coordinate table to completed audit outputs, and I do not claim a new numerical census, completed search, or cold replay.

The substantive result is a different mass-control mechanism for the remaining stable-basin problem: **with all but one supporting plane fixed, exact filled-centroid correction is the minimization of a convex three-variable potential**. An active correcting plane has a positive-definite mass Jacobian, and any exact correcting physical body is globally unique—even across changes of incidence. This provides a mass equation that can be solved together with a finite geometric cancellation, rather than assigning a convenient reference centre or minimizing a nearly collapsed witness.

I also derive a complete, fixed-edge realization chart for the own-centred polar of RELEASED8. Its maximal incidence is analytically118/177/61, and its exact own-centred realization space has180 local supporting-plane degrees of freedom. Its equilibrium census has **not** been observed here. Polarity alone is not claimed to solve the stable basin.

The complete runnable source in section7 recovers the exact selected parent from the journal, constructs this rational own-centred dual, evaluates its full own-centred feature census in one implementation, and constructs exact mass-preserving tangent directions towards facet/edge contact. It is supplied as **unconfirmed execution**, not as an already passed verification.

## 2. Source authority and what remains durable

The immutable analytical parent remains

`figure-0386`,

SHA-256

`d7bd873d68c1e2efeef64349ac7ed55312f7a79b1bfb48dc43a4d8ae95019172`.

The complete selected coordinate source is **NH72_RELEASED8_LITERAL_CORE7_V1**, journaled at2026-09-16T12:35:04.206Z. It contains the entire97-row integer bank with denominator10^8, the exhaustive point-hull checker, independent plane-pair checker, third mass implementation and replay driver. It reconstructs the unchanged **NH72_RELEASE61_OWN211_G8**, actual61/177/118, own211/weak000. Stable facets are65 and110; the unstable vertex is raw-lex60; the saddle is raw edge0–1. These are the parent’s own indexing domains, not S8, K99 or TURNOVER labels. 

The selected capsule is complete. The older CORE20 parts1/3 and2/3, whose third part is absent, are not used as a substitute. The103-file discovery package is not needed for the new method. 

Inherited, completed selected-parent bindings are:

```text
Normalized selected-parent base64:
9672 characters
bc2b3317af3335ca1c828b35228a13d078554721d28b2ef2bcee23c40ce02116

Decoded seven-source dictionary:
20685 bytes
03f631d963a221bc1161ea923021f0ef628d73fc54bedcd61119a19be0a29db9

Parent A=B:
23384 bytes
227315395058e6fe8a06bc1eac26579cd3de2ba512468c10c275fa79d93db91d

Observed by the coordinator for this selected-parent capsule:
NH72_RELEASED8_LITERAL_SOURCE_COLD_PASS
```

Those are inherited results, not fresh executions in this continuation. The journal records that the independent geometry/equilibrium implementations, centred-mass integration and tetrahedron/prism controls completed for that parent. 

## 3. Exact filled-mass correction by one supporting plane

### 3.1 The physical family and its potential

Fix a convex polyhedral intersection H containing0 in its interior. H may be unbounded. A variable vector q defines

`Q(q)=H∩{x:q·x≤1}`.

Only parameters for which Q(q) is bounded and full-dimensional are admitted. The density is uniformly1 throughout Q(q). Define

`V(q)=∫_{Q(q)}1 dx`,

`M(q)=∫_{Q(q)}x dx`,

`Φ(q)=∫_H max(0,1−q·x) dx`.

On the finite domain of this integral,

`Φ(q)=V(q)−q·M(q)`.

The integrand is convex in q. Therefore **Φ is convex**, interpreted as an extended-valued function outside its finite domain. Its gradient is

`∇Φ(q)=−M(q)`.

The moving-boundary contribution vanishes because the integrand equals0 on q·x=1. Thus a stationary point of Φ satisfies **all three actual filled first-moment equations M(q)=0**. It has own centroid0 because V(q)>0. No vertex weights, point masses or polar-volume reference centre are involved.

### 3.2 Positive-definite Jacobian of an active plane

Let F(q)=H∩{q·x=1} be an active two-dimensional facet. Differentiating the moment under its actual normal velocity gives

`DM(q)[v]=−K(q)v`,

where

`K(q)=(1/|q|)∫_{F(q)}xxᵀ dA`.

For every nonzero v,

`vᵀK(q)v=(1/|q|)∫_{F(q)}(v·x)² dA>0`.

The inequality is strict because an open part of the plane q·x=1 cannot be contained in a linear plane v·x=0 through the origin. Hence **every active facet is a full-rank three-component first-moment actuator**. A special cap Jacobian need not be guessed or found by a numerical rank test.

At a mass-closed body M=0, the own-centroid derivative is

`Dg(q)=−K(q)/V(q)`.

The factor V matters: this is the derivative of the true volume centroid, not of an unnormalized collection of vertex coordinates.

### 3.3 Global uniqueness, including incidence changes

Suppose q1 and q2 both give bounded full-dimensional bodies with M(q1)=M(q2)=0. On Q(q1)\Q(q2),

`(q1−q2)·x<0`;

on Q(q2)\Q(q1),

`(q1−q2)·x>0`.

Consequently, if the physical bodies differ,

`(q1−q2)·[M(q1)−M(q2)]<0`,

a contradiction. Thus the physical mass-closed body is unique. If the variable plane remains an active, nonredundant facet, its normalized q is unique as well.

This proof does not freeze a visibility cell, degree or normal fan. It establishes **uniqueness**, not existence for every redesigned H. A design can still have no admissible mass-closing plane, or its minimizer can leave the required edge budget. Neither possibility is resolved by a small residual.

An immediate exact exclusion follows: **moving only one active supporting plane while keeping all the other planes fixed cannot produce a different body with the same zero filled first moment.** A meaningful cancellation must change at least one design plane as well as its mass corrector, or leave that fixed-plane family. This is a finite-family statement, not a prohibition on the coupled design.

## 4. A complete mass-closed support chart, and why the dual is useful

Let P be RELEASED8 translated by its exact own centroid. Form the raw polar

`R=P°={y:p·y≤1 for every vertex p of P}`.

Compute its actual filled centroid γ=M_R/V_R, and define

`Q=R−γ`.

This is a rational, finite construction from the literal parent. It does **not** call the raw polar own-centred merely because the primal is centred. The additional integration and translation by γ are essential.

The parent has61 vertices,177 edges and118 triangular maximal facets. Therefore its polar, and then Q, have exactly

`V=118, E=177, F=61`.

The polar is simple: exactly three maximal facets meet at every vertex. These incidence conclusions follow from polarity and translation; they are not a newly observed full audit. In particular, exceeding105 vertices here does not consume the edge budget: the actual E remains177.

Write Q in normalized form

`Q={x:q_i·x≤1, i=0,…,60}`.

Because Q is simple, its complete supporting-plane parameter space has an open fixed-complex neighbourhood with183 coordinates. The three filled-moment constraints have rank3: the derivative with respect to any one active q_i is the invertible matrix−K_i. Thus the mass-closed realization chart has **180 local dimensions**, with the correcting q_i an implicitly determined function of the other60 planes.

For changes dq_j in the design planes, the exact first-order correcting equation is

`K_i dq_i=−Σ_{j≠i}K_j dq_j`.

This equation is not used as a substitute for finite mass closure. It is the tangent of the actual nonlinear equation M=0; the implicit-function theorem gives a locally unique finite correction, and section3 gives global uniqueness whenever an admissible finite correction exists.

The matrices have a rational triangulation formula. For an outward triangle with vertices a,b,c on a normalized facet, put s=a+b+c and w=det(a,b,c)>0. Its contribution is

`K_triangle=(w/24)(aaᵀ+bbᵀ+ccᵀ+ssᵀ)`.

No square roots or numerical face areas are required. Summing over all facets gives the useful exact consistency identity

`Σ_i K_i=5∫_Q xxᵀ dx`.

All these quantities are recomputed from the changed filled geometry. This chart imposes no half-turn symmetry and adds no separate ballast point.

**Unresolved mechanical gate:** the equilibrium census of Q has not been observed here. Recentring a polar can change its equilibria. The reference S/U swap at the unrecentred polar is not an own-centred answer, and I do not label Q as121,211 or110 without that census.

## 5. A mass-preserving direction towards an actual S/H contact

At an own-centred normalized body, the orthogonal foot on facet f is

`q_f/|q_f|²`.

Its inequality against a neighbouring facet g has sign

`b_fg=|q_f|²−q_g·q_f`.

The same expression is one of the two normal-cone coefficients in the direct saddle test for edge f∩g. At a genuine stable/saddle cancellation, b_fg reaches0 while the foot remains in the relative interior of the shared edge and all the other required inequalities stay strict.

Choose a mass-correcting facet i different from f and g. The design direction

`dq_f=q_g−2q_f`, `dq_g=0`

gives

`db_fg=−|2q_f−q_g|²<0`.

Choose simultaneously

`dq_i=−K_i^−1 K_f dq_f`.

Then the actual filled first moment has zero derivative. Because the corrector is neither f nor g, it does not alter this local contact derivative directly. The nonlinear correction from section3, not just its tangent, is what must be solved at subsequent finite steps.

This distinguishes a physical cancellation attempt from equalising stable distances or moving an arbitrary centre. It does **not** establish that a finite crossing is reachable before another contact, a new equilibrium, loss of boundedness, or an edge-budget violation. A stable facet need not be immediately adjacent to the present saddle; in that case the adjoining support/basin geometry has to change first. The program below reports adjacency rather than assuming it from the names of the old stable facets.

For the original, nonsimple RELEASED8 rather than its simple dual, an arbitrarily small support change can split vertices. The same filled-mass derivative applies, but preservation of its old complex and equilibrium census is not automatic. This is one reason to distinguish the simple dual chart from a routine independent motion of the118 original triangular planes.

## 6. What is and is not established

Established analytically:

- The one-plane mass potential is convex, with gradient−M and a positive-definite Hessian at every active facet.
- A finite exact correcting body, when it exists with the other planes fixed, is globally unique.
- The correctly own-centred dual has118/177/61 and a180-dimensional local mass-closed support chart.
- A directly adjacent stable/saddle boundary admits the displayed strictly decreasing contact tangent together with exact first-order filled-moment compensation.

Not established in this continuation: the dual’s own feature census, any finite mass-corrected cancellation, a quantitative correction radius, a new exact nonwinner with completed audits, or a new winner. There is no numerical search scope or seed to report because no new completed numerical experiment was observed. No output byte count or SHA is invented for the source unit below.

## 7. Complete runnable recovery and exact method unit

The following source uses the **literal selected-parent capsule already present in the attached journal**, not an old sandbox path or incomplete CORE20 package. It extracts and hash-checks that capsule, executes its complete selected-parent replay, locates the resulting exact parent report by its full content hash, and independently constructs the centred dual and the exact facet-moment matrices.

It performs one full feature-census implementation on the dual. It does not claim to replace the second independent dual hull audit required for promotion. The parent replay’s independent checks and controls concern the parent, not the new dual.

Save as `facet_mass_chart.py`. Inputs are the exact attached journal and two initially absent directories. Dependencies: CPython3.11 or newer, standard library only, assertions enabled. No random seed or floating rounding is used.

```python
import base64
import hashlib
import json
import lzma
import re
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

assert __debug__
sys.set_int_max_str_digits(0)
PARENT_REPORT_SHA = '227315395058e6fe8a06bc1eac26579cd3de2ba512468c10c275fa79d93db91d'


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def det(a, b, c):
    return dot(a, cross(b, c))


def matvec(A, v):
    return tuple(dot(row, v) for row in A)


def solve(A, b):
    a = [list(map(F, row))+[F(v)] for row, v in zip(A, b)]
    for j in range(3):
        k = next(k for k in range(j, 3) if a[k][j])
        a[j], a[k] = a[k], a[j]
        s = a[j][j]
        a[j] = [v/s for v in a[j]]
        for k in range(3):
            if k != j:
                s = a[k][j]
                a[k] = [x-s*y for x, y in zip(a[k], a[j])]
    return tuple(row[3] for row in a)


def positive_definite(A):
    assert all(A[i][j] == A[j][i] for i in range(3) for j in range(3))
    return (A[0][0] > 0 and
            A[0][0]*A[1][1]-A[0][1]**2 > 0 and
            det(A[0], A[1], A[2]) > 0)


def edges_of(faces):
    edges = {}
    for f, cy in enumerate(faces):
        assert len(cy) >= 3 and len(set(cy)) == len(cy)
        for a, b in zip(cy, cy[1:]+cy[:1]):
            edges.setdefault(tuple(sorted((a, b))), []).append(f)
    assert all(len(v) == 2 for v in edges.values())
    return edges


def moments(X, faces):
    V = F(0)
    M = [F(0)]*3
    J = [[F(0) for j in range(3)] for i in range(3)]
    for cy in faces:
        for k in range(1, len(cy)-1):
            a, b, c = X[cy[0]], X[cy[k]], X[cy[k+1]]
            w = det(a, b, c)
            assert w > 0
            s = tuple(a[i]+b[i]+c[i] for i in range(3))
            V += w/6
            for i in range(3):
                M[i] += w*s[i]/24
                for j in range(3):
                    J[i][j] += w*(s[i]*s[j]+a[i]*a[j]+b[i]*b[j]+c[i]*c[j])/120
    assert V > 0
    return V, tuple(M), J


def facet_matrices(X, faces):
    result = []
    for cy in faces:
        K = [[F(0) for j in range(3)] for i in range(3)]
        for k in range(1, len(cy)-1):
            a, b, c = X[cy[0]], X[cy[k]], X[cy[k+1]]
            w = det(a, b, c)
            assert w > 0
            s = tuple(a[i]+b[i]+c[i] for i in range(3))
            for i in range(3):
                for j in range(3):
                    K[i][j] += w*(s[i]*s[j]+a[i]*a[j]+b[i]*b[j]+c[i]*c[j])/24
        assert positive_definite(K)
        result.append(K)
    return result


def census(X, faces, q):
    E = edges_of(faces)
    S, U, H, WS, WU, WH = [], [], [], [], [], []
    fzero = vzero = ezero = 0
    for i, n in enumerate(q):
        values = [dot(n, n)-dot(n, m) for j, m in enumerate(q) if j != i]
        fzero += sum(v == 0 for v in values)
        if min(values) > 0:
            S.append(i)
        elif min(values) == 0:
            WS.append(i)
    for i, x in enumerate(X):
        m = max(dot(x, sub(y, x)) for j, y in enumerate(X) if j != i)
        vzero += m == 0
        if m < 0:
            U.append(i)
        elif m == 0:
            WU.append(i)
    primitives = []
    for (a, b), (f, g) in sorted(E.items()):
        e = sub(X[b], X[a])
        n, m = q[f], q[g]
        nn, mm, nm = dot(n, n), dot(m, m), dot(n, m)
        assert nn*mm-nm*nm > 0
        values = [-dot(X[a], e), dot(X[b], e), mm-nm, nn-nm]
        ezero += sum(v == 0 for v in values)
        primitives.append([a, b, values])
        if min(values) > 0:
            H.append([a, b])
        elif min(values) == 0:
            WH.append([a, b])
    return dict(counts=[len(S), len(U), len(H)],
                weak=[len(WS), len(WU), len(WH)],
                stable_faces=S, unstable_vertices=U, saddle_edges=H,
                weak_faces=WS, weak_vertices=WU, weak_edges=WH,
                projection_halfspace_zero_count=fzero,
                vertex_maximum_zero_count=vzero,
                edge_primitive_zero_count=ezero,
                edge_primitives=primitives)


def recover_parent(journal, source, proof):
    text = Path(journal).read_text(encoding='utf-8')
    heading = '## Recovery capsule part 1/1 — NH72_RELEASED8_LITERAL_CORE7_V1'
    section = text.split(heading, 1)[1].split('# Immutable parent result payloads', 1)[0]
    candidates = re.findall(r'```text\s*\n(.*?)\n```', section, re.S)
    chosen = []
    for candidate in candidates:
        u = ''.join(candidate.split())
        if len(u) == 9672 and hashlib.sha256(u.encode()).hexdigest() == (
            'bc2b3317af3335ca1c828b35228a13d078554721d28b2ef2bcee23c40ce02116'):
            chosen.append(u)
    assert len(chosen) == 1
    raw = lzma.decompress(base64.b64decode(chosen[0], validate=True))
    assert len(raw) == 20685
    assert hashlib.sha256(raw).hexdigest() == (
        '03f631d963a221bc1161ea923021f0ef628d73fc54bedcd61119a19be0a29db9')
    files = json.loads(raw)
    assert len(files) == 7
    source = Path(source)
    source.mkdir(parents=True, exist_ok=False)
    assert not Path(proof).exists()
    for name, content in files.items():
        p = Path(name)
        assert not p.is_absolute() and '..' not in p.parts
        target = source/p
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content.encode('utf-8'))
    subprocess.run([sys.executable, '-B', '-S', str(source/'REPLAY_RELEASED8.py'), proof], check=True)
    matches = []
    for p in Path(proof).rglob('*.json'):
        b = p.read_bytes()
        if hashlib.sha256(b).hexdigest() == PARENT_REPORT_SHA:
            assert len(b) == 23384
            matches.append(b)
    assert len(matches) >= 2
    assert all(b == matches[0] for b in matches)
    return json.loads(matches[0])


def exact_dual(parent):
    assert (parent['V'], parent['E'], parent['F']) == (61, 177, 118)
    assert parent['counts'] == [2, 1, 1] and parent['weak'] == [0, 0, 0]
    g = tuple(map(F, parent['raw_centroid']))
    P = [sub(tuple(map(F, p)), g) for p in parent['raw_vertices']]
    pf = parent['faces']
    assert len(P) == 61 and all(len(cy) == 3 for cy in pf)
    _, original_M, _ = moments(P, pf)
    assert original_M == (0, 0, 0)
    pe = edges_of(pf)
    Y = []
    for cy in pf:
        a, b, c = (P[i] for i in cy)
        n = cross(sub(b, a), sub(c, a))
        h = dot(n, a)
        assert h > 0
        Y.append(tuple(v/h for v in n))
    df = []
    for v in range(len(P)):
        incident = {f for f, cy in enumerate(pf) if v in cy}
        adj = {f: [] for f in incident}
        for edge, pair in pe.items():
            if v in edge:
                a, b = pair
                adj[a].append(b)
                adj[b].append(a)
        assert all(len(a) == 2 for a in adj.values())
        first = min(incident)
        cy = [first]
        previous, current = first, min(adj[first])
        while current != first:
            assert current not in cy
            cy.append(current)
            nxt = next(k for k in adj[current] if k != previous)
            previous, current = current, nxt
        assert set(cy) == incident
        if dot(P[v], cross(sub(Y[cy[1]], Y[cy[0]]), sub(Y[cy[2]], Y[cy[0]]))) < 0:
            cy.reverse()
        df.append(cy)
    V, M, _ = moments(Y, df)
    gamma = tuple(v/V for v in M)
    X = [sub(y, gamma) for y in Y]
    q = []
    for p in P:
        d = 1-dot(p, gamma)
        assert d > 0
        q.append(tuple(v/d for v in p))
    for i, cy in enumerate(df):
        actual = {j for j, x in enumerate(X) if dot(q[i], x) == 1}
        assert actual == set(cy)
        assert all(dot(q[i], x) <= 1 for x in X)
    de = edges_of(df)
    assert (len(X), len(de), len(df)) == (118, 177, 61)
    assert all(sum(v in cy for cy in df) == 3 for v in range(len(X)))
    V2, M2, J2 = moments(X, df)
    assert V2 == V and M2 == (0, 0, 0)
    K = facet_matrices(X, df)
    assert all(sum(k[i][j] for k in K) == 5*J2[i][j]
               for i in range(3) for j in range(3))
    audit = census(X, df, q)
    directions = []
    saddle_set = {tuple(e) for e in audit['saddle_edges']}
    for f in audit['stable_faces']:
        neighbouring = [(edge, g if f == h else h)
                        for edge, (g, h) in de.items() if f in (g, h)]
        for edge, j in sorted(neighbouring):
            i = next(k for k in range(len(q)) if k not in (f, j))
            v = tuple(q[j][k]-2*q[f][k] for k in range(3))
            compensator = solve(K[i], tuple(-x for x in matvec(K[f], v)))
            assert tuple(a+b for a, b in zip(matvec(K[f], v), matvec(K[i], compensator))) == (0, 0, 0)
            derivative = dot(tuple(2*q[f][k]-q[j][k] for k in range(3)), v)
            assert derivative == -dot(v, v) < 0
            directions.append(dict(face=f, neighbour=j, edge=edge,
                                   edge_is_current_saddle=edge in saddle_set,
                                   correcting_face=i, design_velocity=v,
                                   correcting_velocity=compensator,
                                   gate=dot(q[f], q[f])-dot(q[j], q[f]),
                                   gate_derivative=derivative))
    return dict(status='ONE_IMPLEMENTATION_AND_EXACT_MASS_TANGENTS_ONLY',
                accepted_new_body=False,
                primal_raw_centroid=g, dual_raw_vertices=Y,
                dual_raw_volume=V, dual_raw_first_moments=M,
                dual_raw_own_centroid=gamma,
                centred_vertices=X, normalized_supports=q,
                faces=df, edges=sorted(de), V=118, E=177, F=61,
                centred_first_moments=M2,
                facet_mass_matrices=K, census=audit,
                mass_closed_tangent_directions=directions)


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise SystemExit('Usage: python -B -S facet_mass_chart.py journal.md absent-source absent-proof')
    parent = recover_parent(sys.argv[1], sys.argv[2], sys.argv[3])
    report = exact_dual(parent)
    target = Path(sys.argv[3])/'CENTRED_DUAL_MASS_CHART.json'
    data = json.dumps(encode(report), sort_keys=True, separators=(',', ':')).encode('utf-8')
    target.write_bytes(data)
    print('CENTRED_DUAL_FACET_MASS_CHART_PASS', len(data), hashlib.sha256(data).hexdigest())
```

Command:

```text
python -B -S facet_mass_chart.py research-journal(20260916-123559).md absent-source absent-proof
```

When running in a shell that treats parentheses specially, quote the journal filename. The terminal marker `CENTRED_DUAL_FACET_MASS_CHART_PASS` is **specified but not observed in this continuation**. The code prints the actual output size and SHA only after successful completion; none is supplied here without that evidence.

## 8. Continuation frontier

The next finite gate is no longer “find a centre that makes an old witness positive.” It is: change the support geometry of the stable basin, solve the unique admissible three-variable **actual filled-mass** corrector, and then reconstruct the full physical hull and all equilibria. The simple dual offers an initially fixed177-edge chart without symmetry restrictions; the original RELEASED8 remains available when its particular S/H geometry is more favourable, but its contact splits must be counted explicitly.

A completed finite cancellation still requires showing that the correcting facet remains active, the body remains bounded and convex, the actual own centroid is the one used in every predicate, the target S/H pair really disappears, and no other strict or weak equilibrium is born. This handoff supplies an exact mass-control structure and source-defined next input, not those missing endpoint checks.

The last fully audited durable coordinate parent remains RELEASED8. No own110, new accepted nonwinner, global impossibility, or C<32 search is claimed.
