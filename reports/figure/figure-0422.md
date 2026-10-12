# figure-0422

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Bright Harbor 81 — nonlinear basin construction and a whole-section obstruction

Branch: `[internal-source-reference]`.

**No new own110/weak000 construction is promoted in this inline handoff.** The definite mathematical result below is a global geometric requirement for eliminating the complete extra radial basin. It is not another local witness-loss criterion.

## Execution and preservation boundary

The tool returns available to me in this continuation were replaced by `Skipped … messages`. Consequently I cannot responsibly quote an observed new census, completed iteration count, successful replay marker, or output hash from those returns. This does not establish that the computations failed; it prevents me from inspecting their outcomes.

The invoked preservation program freezes available new H- and V-inputs, reconstructs their exact maximal complexes, computes their actual uniform-volume centroids and complete strict/weak census, checks mass by a separate projected-polygon formula, computes exact radial persistence, and attempts source-only replay. It records a failure rather than declaring success when these steps do not complete. The final preservation call also saves available sources and checkpoints when the final replay report is absent.

Generated nonlinear handoff and literal recovery capsule (`BH81_NONLINEAR_HANDOFF.md`)

Complete nonlinear source, checkpoint, and output snapshot (`BH81_NONLINEAR_FULL.zip`)

**The new computational capsule is not reproduced literally in this JSON. Accordingly, its possible numerical or rational endpoints are not promoted here as self-contained inline successors.** The generated report must be inspected, including its status and literal capsule, before any endpoint is integrated. The supplied LOW121/CUT121 closure remains the authoritative starting evidence.

## 1. A necessary equatorial-width condition for own U1

Let K be a uniformly filled convex three-polyhedron, translated by its **actual volume centroid** so that its centroid is 0. Fix a unit vector u. Put

`h+ = max_{x∈K} u·x`,

`h− = −min_{x∈K} u·x`,

`ρ = max{|x| : x∈K, u·x=0}`.

Here ρ is the **largest radius of the central planar section**, not the inradius of K.

### Theorem

If

`min(h+,h−) > ρ`,

then K has at least two distinct **strict unstable vertices**. Moreover, its true-edge squared-radius merge structure contains a finite bar of length at least

`min(h+²,h−²) − ρ²`.

Uniform volume gives the additional inequalities

`h+ ≤ 3h−` and `h− ≤ 3h+`.

Therefore the simpler condition

`max(h+,h−) > 3ρ`

also forces two strict unstable vertices, with a finite radial bar at least

`max(h+,h−)²/9 − ρ²`.

This allows arbitrary numbers of vertices, changes of maximal facets, root turnover, and finite nonlinear deformations. Its hypothesis is a geometric section bound, not preservation of an old incidence or witness graph.

### Proof of the two strict vertices

Consider the two convex capped bodies `K∩{u·x≥0}` and `K∩{u·x≤0}`. Each has a point whose radius exceeds ρ. Its maximum-radius point therefore cannot lie on the dividing plane. A maximum of squared radius on a polytope is attained at a vertex, so each cap supplies an original vertex of K away from the plane.

Let v be either cap maximum and w any other vertex of K. For sufficiently small positive t, the point `v+t(w−v)` remains in the same cap. Hence

`|v+t(w−v)|² ≤ |v|²`.

Expanding and dividing by t gives

`v·(w−v) ≤ −t|w−v|²/2 < 0`.

Thus v is strictly unstable in the entire original body, not merely in the cap. The two cap vertices are distinct.

### Proof of the mass-dependent factor 3

Choose an extreme vertex p with `u·p=h+`. Triangulate the boundary facets not containing p and decompose K into positive-volume tetrahedra with common apex p. Each of the other three vertices of every tetrahedron has height at least `−h−`. Every tetrahedral centroid therefore has height at least

`(h+−3h−)/4`.

The actual filled centroid is their volume-weighted average and has height 0. Consequently `h+≤3h−`. Applying the same argument to the opposite direction proves the other inequality.

This argument uses actual uniform-volume mass. It cannot be transferred to a freely selected reference point or to arbitrary vertex weights.

### Proof of the bar bound

Every edge path joining the two halfspaces crosses the central section. At that crossing its radius is at most ρ, so the edge minimum on that crossing edge is at most `ρ²`. The two cap peaks have squared radii at least `h+²` and `h−²`. Before the two corresponding superlevel components can merge, at least one component with birth at least the smaller of those values survives down to level at most `ρ²`. This gives the stated finite true-edge merge bar.

The conclusion is not obtained by thresholding small positive bars or by testing one outgoing dot product.

## 2. A coordinate-free requirement at the farthest vertex

Take v to be a globally farthest vertex of the centered body and let `R=|v|`. Choose `u=v/R`. Then `h+=R`. Every own-U1 body must satisfy

`max{|x| : x∈K, v·x=0} ≥ R/3`.

Thus, after normalization to `R=1`, a successful own-U1 endpoint must reach radius at least **1/3 in the plane through the actual centroid perpendicular to its farthest vertex**.

This identifies a genuinely finite geometric requirement. Moving a few nearly coincident points at one end of a thin body cannot substitute for the required central-section extent. Changing the unstable root is allowed, but the condition then applies to the new farthest direction.

A small value of `r/R`, where r is the inradius, does **not** itself prove this obstruction. The required upper bound is on the maximum radius of a particular central section. The section must be constructed or bounded explicitly.

## 3. A closed, scale-invariant thin-box family is excluded

There is a particularly simple rational specialization. In actual centered coordinates, put

`A = max_{x∈K}|y+z|`.

Suppose the whole body satisfies

`8|x| ≤ A`,

`4|y−z| ≤ A`.

These are not infinitesimal restrictions. They define a complete scale-invariant family of convex shapes.

On the section `y+z=0`,

`|x|² = x²+(y−z)²/2 ≤ 3A²/64`.

The larger support distance in the unit direction `(0,1,1)/√2` is `A/√2`. The mass inequality forces the opposite support distance to be at least `A/(3√2)`. Consequently a finite radial bar is at least

`A²/18 − 3A²/64 = 5A²/576 > 0`.

The global maximum squared radius is at most

`A²/64 + A²/32 + A²/2 = 35A²/64`.

Therefore every body in this closed thin-box family has at least two strict unstable vertices and a finite true radial bar satisfying

`bar / R² ≥ 1/63`.

This is a continuous geometric exclusion over arbitrary contact changes and arbitrary complexity, not an interpretation of a failed finite search. It does **not** exclude the complete LOW121/CUT121 nonlinear family: a descendant can leave the box by changing the actual central geometry. It also does not exclude an unrestricted affine orbit.

The saved `section_certificate.py` tests exact central sections and this box condition on the available starting audits and frozen endpoints. I do not quote a particular body’s test result without a visible returned certificate.

## 4. The nonlinear construction mechanism implemented in this attempt

The central new constructive mechanism was a **physical radial bridge followed by actual mass closure**, rather than continued minimization of the old thin body’s local witness deficit.

Start from the physical vertices of LOW121 at its actual centroid. Select its farthest vertex and the other unstable vertex. Add a spatial path between their directions, with 12, 24, 40, or 60 links. The path can twist out of the initial great-circle plane. With 60 links, only 59 new points are added to the 44 old vertices, so there are at most103 input vertices and hence

`E ≤ 3·103−6 = 303 < 311`

for every full-dimensional hull, regardless of which inputs remain exposed.

Let successive unit directions be `d_i,d_(i+1)` and their angle be `θ_i<π/2`. A positive radial escape is equivalent to

`r_i < cos(θ_i) r_(i+1)`.

For fixed endpoint radii, set

`γ = log(r_last/r_first) + Σ_i log cos(θ_i)`.

When γ is positive, the initialization

`log(r_(i+1)/r_i) = −log cos(θ_i) + γ/m`

gives a strict escape at every path link. The old nonroot vertices receive positive outgoing witnesses, and the old extra unstable vertex points into the new bridge. Every positive arrow increases radius, so the resulting directed system is acyclic and reaches the farthest root.

This is a **reference-U1 construction only** until actual mass is closed. The subsequent optimization changes all physical radii, not density weights, under linear inequalities

`cos(θ_ij) r_j − r_i ≥ μ`.

The invoked radial producer used `μ=10⁻7`, root radius1, lower radius bound10⁻4, actual volume floor0.002, twist values `0,±0.7,±1.4`, and SLSQP mass minimization with maximum500 iterations and `ftol=10⁻16`. These are source settings and invocation limits, **not claims that every requested case or iteration completed**.

### Actual filled-mass derivatives

For an outward boundary triangle with vertices `p_a,p_b,p_c`, let

`w = det(p_a,p_b,p_c)/6`.

Its volume contribution is w and its first-moment contribution is

`w(p_a+p_b+p_c)/4`.

With `p_i=r_i d_i`, a triangle containing i contributes

`∂V/∂r_i = w/r_i`,

`∂M/∂r_i = w(p_a+p_b+p_c)/(4r_i) + wd_i/4`.

Summing over the current actual hull gives the derivative of the actual centroid `c=M/V`. The mass objective was

`|c|² / V^(2/3)`,

so uniform shrinking cannot masquerade as mass improvement. The hull is rebuilt after geometry changes. An origin-reference escape tree and a small residual are not treated as an own-centroid certificate.

A subsequent radial/polar stage targets the complete true-edge polar persistence while retaining the primal escape inequalities and actual mass equations. A free-coordinate stage then releases the ray restriction, differentiates the actual centroid, rebuilds the hull, and guards positive physical escapes and conditioning. Its purpose is to address the stable basins introduced by the radial bridge, not to declare the bridge itself own110.

Other preserved finite entrances include all-normal physical deformations, whole-chord curvature transfer, polynomial bending, additional common-tilt cuts, and finite support deletion. Their source, requested settings, and available checkpoints are in the snapshot. No finite non-success is promoted to an exclusion of those families.

## 5. Complete exact section-certificate source

The following is a standalone exact unit for the new geometric result. It reads rational physical points and maximal cyclic facets, reconstructs the actual filled centroid, checks the supporting closed complex, finds the exact central-section radius, and supplies explicit strict-U witnesses when the section criterion applies. It does not rely on a floating geometry package or an omitted helper.

Its input format is the `points`, `faces`, and optional `centroid` fields of the supplied exact LOW121/CUT121 audits. The input dependency is the literal two-material recovery closure supplied for this assignment, not an unprovided numerical checkpoint. In particular, the supplied correction to `BH81_CORE.py` must be applied when regenerating those audits.

Run:

`python section_gate.py LOW121_EXACT.json LOW121_SECTION.json`

or use the actual farthest direction:

`python section_gate.py LOW121_EXACT.json LOW121_FARTHEST_SECTION.json --farthest`

The terminal marker is specified by the source below; it is not reported here as an observed execution.

```python
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import argparse, hashlib, json, sys

sys.set_int_max_str_digits(0)

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))

def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

def squared(a):
    return dot(a, a)

def actual_mass(data):
    P = [tuple(F(x) for x in p) for p in data['points']]
    faces = [list(map(int, f)) for f in data['faces']]
    assert len(P) >= 4 and len(set(P)) == len(P)
    anchor = tuple(sum(p[k] for p in P)/len(P) for k in range(3))
    edges = defaultdict(list)
    neighbours = defaultdict(set)
    links = defaultdict(lambda: defaultdict(set))
    seen_faces = set()
    V = F(0)
    M = [F(0), F(0), F(0)]
    used = set()

    for fi, row in enumerate(faces):
        assert len(row) >= 3 and len(set(row)) == len(row)
        assert all(0 <= i < len(P) for i in row)
        key = frozenset(row)
        assert key not in seen_faces
        seen_faces.add(key)
        a, b, c = (P[i] for i in row[:3])
        n = cross(sub(b, a), sub(c, a))
        assert squared(n) > 0
        h = dot(n, a)
        assert dot(n, anchor) < h
        assert all(dot(n, p) <= h for p in P)
        assert set(row) == {i for i, p in enumerate(P) if dot(n, p) == h}
        used.update(row)

        for k, i in enumerate(row):
            j = row[(k+1) % len(row)]
            before = row[k-1]
            e = sub(P[j], P[i])
            assert all(dot(n, cross(e, sub(P[t], P[i]))) > 0
                       for t in row if t not in (i, j))
            edges[tuple(sorted((i, j)))].append((i, j))
            neighbours[i].add(j)
            neighbours[j].add(i)
            links[i][before].add(j)
            links[i][j].add(before)

        for k in range(1, len(row)-1):
            a, b, c = (P[i] for i in (row[0], row[k], row[k+1]))
            w = dot(sub(a, anchor),
                    cross(sub(b, anchor), sub(c, anchor)))/6
            assert w > 0
            V += w
            for j in range(3):
                M[j] += w*(anchor[j]+a[j]+b[j]+c[j])/4

    assert used == set(range(len(P)))
    assert len(P)-len(edges)+len(faces) == 2
    for pair in edges.values():
        assert len(pair) == 2 and pair[0] == tuple(reversed(pair[1]))
    for v in range(len(P)):
        graph = links[v]
        assert set(graph) == neighbours[v]
        assert all(len(ns) == 2 for ns in graph.values())
        reached = {next(iter(graph))}
        todo = list(reached)
        while todo:
            x = todo.pop()
            for y in graph[x]-reached:
                reached.add(y)
                todo.append(y)
        assert reached == set(graph)
    reached = {0}
    todo = [0]
    while todo:
        i = todo.pop()
        for j in neighbours[i]-reached:
            reached.add(j)
            todo.append(j)
    assert reached == set(range(len(P))) and V > 0

    centroid = tuple(x/V for x in M)
    if 'centroid' in data:
        assert centroid == tuple(F(x) for x in data['centroid'])
    X = [sub(p, centroid) for p in P]
    U = [i for i, x in enumerate(X)
         if all(dot(x, sub(y, x)) < 0 for j, y in enumerate(X) if j != i)]
    return X, centroid, V, U, (len(P), len(edges), len(faces))

def section_gate(data, farthest=False):
    X, centroid, volume, U, vef = actual_mass(data)
    B = [squared(x) for x in X]
    root = max(range(len(X)), key=lambda i: (B[i], -i))
    n = X[root] if farthest else (F(0), F(1), F(1))
    nn = squared(n)
    assert nn > 0
    s = [dot(n, x) for x in X]
    hp = max(s)
    hm = -min(s)
    assert min(hp, hm) > 0
    assert hp <= 3*hm and hm <= 3*hp

    section = [x for x, z in zip(X, s) if z == 0]
    for i, x in enumerate(X):
        for j in range(i):
            if s[i]*s[j] < 0:
                t = s[i]/(s[i]-s[j])
                section.append(tuple((1-t)*x[k]+t*X[j][k]
                                     for k in range(3)))
    assert section
    rho2 = max(map(squared, section))
    R2 = max(B)
    ip = max((i for i in range(len(X)) if s[i] > 0), key=lambda i: B[i])
    im = max((i for i in range(len(X)) if s[i] < 0), key=lambda i: B[i])
    cap_bound = min(B[ip], B[im])-rho2
    height_bound = min(hp*hp, hm*hm)/nn-rho2
    mass_bound = max(hp*hp, hm*hm)/(9*nn)-rho2
    witnesses = []
    if cap_bound > 0:
        assert ip != im and ip in U and im in U
        witnesses = [ip, im]

    box = None
    if not farthest:
        A = max(abs(x[1]+x[2]) for x in X)
        bx = max(abs(x[0]) for x in X)
        bd = max(abs(x[1]-x[2]) for x in X)
        holds = 8*bx <= A and 4*bd <= A
        if holds:
            assert rho2 <= 3*A*A/64
            assert R2 <= 35*A*A/64
            assert mass_bound/R2 >= F(1, 63)
            assert len(U) >= 2
        box = dict(holds=holds, A=A, max_abs_x=bx,
                   max_abs_y_minus_z=bd,
                   universal_relative_bar_lower_bound=F(1,63) if holds else None)

    lower = max(F(0), cap_bound)
    return dict(VEF=vef, volume=volume, actual_centroid=centroid,
                normal=n, normal_squared_length=nn,
                support_height_squared=[hp*hp/nn, hm*hm/nn],
                section_max_squared_radius=rho2,
                maximum_squared_radius=R2,
                strict_U=U, two_U_witnesses=witnesses,
                cap_bar_lower_bound=lower,
                height_bar_lower_bound=max(F(0), height_bound),
                mass_bar_lower_bound=max(F(0), mass_bound),
                relative_cap_bar_lower_bound=lower/R2,
                thin_box=box)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('input')
    p.add_argument('output')
    p.add_argument('--farthest', action='store_true')
    a = p.parse_args()
    raw = Path(a.input).read_bytes()
    result = section_gate(json.loads(raw), a.farthest)
    result['input_bytes'] = len(raw)
    result['input_sha256'] = hashlib.sha256(raw).hexdigest()
    encoded = json.dumps(result, sort_keys=True, separators=(',', ':'),
                         default=str).encode()
    Path(a.output).write_bytes(encoded)
    print('EXACT_FILLED_SECTION_GATE', len(result['strict_U']),
          result['two_U_witnesses'], len(encoded),
          hashlib.sha256(encoded).hexdigest())

if __name__ == '__main__':
    main()
```

This unit is an exact geometric obstruction checker, not a replacement for a successful candidate’s full independent S/U/H/weak audit.

## 6. The next meaningful constructive question

The radial bridge uses the large vertex budget to alter the entire route between the two physical peaks. The essential acceptance question is whether its actual mass closure can coexist with a single stable basin without returning to a thin-section geometry or creating unresolved small pairs.

For a candidate with one actual unstable vertex, compute the central section perpendicular to that vertex and check the `ρ≥R/3` requirement directly. For a candidate still having two unstable vertices, the exact section certificate distinguishes a macroscopic geometric obstruction from a local edge or tolerance artifact. This directs further shape changes toward the central section and the whole basin, rather than another small adjustment of a nearly coincident endpoint.

The saved nonlinear endpoints must first be read and exact replay status established. No particular endpoint, solver success flag, or disappearance of an old label is being asserted here as an own110 construction. The branch remains nonterminal.
