# figure-0565

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# RA46 — a strict two-stable obstruction for facet-preserving replacements without overhang

## Result and execution boundary

**No new JOINT56 successor or own110 body is established in this continuation.** The substantive result is a geometric exclusion for a large class of finite, multipoint replacements:

> **Let F be a maximal facet of a full-dimensional convex polyhedron K. If the orthogonal projection of K onto the plane of F is contained in F, then K has at least two distinct strict stable equilibria relative to every interior reference point.**

In particular, the conclusion holds at the actual homogeneous-volume centroid. It allows arbitrary changes to the other facets, vertices, roots, volume and centroid. It is not a fixed-centre, retained-root, local-chart, or complexity-limited exclusion.

This identifies a necessary physical feature of any successful facet-preserving construction: **the final body must overhang the retained facet in at least one direction within that facet’s plane.** Replacing the upper surface while keeping the entire body inside the orthogonal prism above the retained facet cannot reach S=1, regardless of how well the mass is balanced.

There is a material access limitation. Only the first30 lines of the latest journal were available in an inspectable tool response. I could not verify the remaining lines31–2153, extract the complete literal JOINT56 parent, verify the attachment’s declared hash, or inspect a successful computational return. The attachment is declared as418936 bytes with SHA-256 `5cf5709a9fefd25aeb253ff9eba598efcc4cfafddbe2a771a609cef8130b9d1e`; that is a manifest identity, **not a newly observed verification**. The requested controlling parent remains `figure-0559`, declared SHA-256 `e0181e33bc72dfc97e64bd431ef4a23f627e5c083036b4ed931e2393205b22db`.

Consequently, **I do not assert that L18, F18, L30, or F30 satisfies the theorem’s projection premise**. Their vertex/edge/facet counts do not determine that premise. The visible journal also distinguishes the improved F18 body from the simpler-arithmetic L18 control; those identities must not be merged. fileciteturn12file0L20-L24

The result below is an analytic family exclusion with a complete exact predicate. Its mathematical proof does not depend on the unavailable coordinates. The predicate implementation is supplied for continuation, but its execution markers are explicitly **unobserved**.

## 1. The excluded finite replacement family

Let F be a compact convex polygon in a plane H, let n be a normal pointing outward from the intended body, and choose h so that H is `n·x=h`. Write πF for orthogonal projection onto H. Define the inward orthogonal prism

```text
PF = {x : n·x ≤ h and πF(x) belongs to F}.
```

Consider **every** compact, full-dimensional convex polyhedron L satisfying

```text
F ⊆ L ⊆ PF.
```

Then F is a maximal facet of L and **S(L,c)≥2 strictly for every c in int(L)**.

This includes arbitrary finite additions, deletions and repositioning of material within the prism, provided the whole polygon F remains. There is no restriction on the number of moving vertices or on which upper faces survive. It also includes changes of incidence and nonsimple contacts. Uniform mass is not replaced by a reference-centre convention: the theorem holds for every possible interior centre, hence in particular for the newly integrated volume centroid of every member.

The scope is important. The theorem does not exclude a construction that introduces an overhang, replaces F, or changes the final metric. Failure of its exact predicate does not establish that110 is attainable; it only removes this particular obstruction.

## 2. Proof, including why the second equilibrium is strict

### The base facet is strictly stable

Choose coordinates in which H is `z=0`, L lies in `z≥0`, and F is a planar polygon D. Because `πF(L)=F`, every interior point c of L has orthogonal projection p in the relative interior of F. Its perpendicular foot on F is therefore in the facet’s relative interior. Thus F is a strict stable equilibrium.

### A second local minimum exists away from F

Let R be the union of all maximal facets other than F, including their boundaries. R is compact. The continuous function

```text
r(x)=|x−c|²
```

attains a minimum on R.

That minimum cannot lie on the boundary of F. To see this, take any q on that boundary. Intersect L with the plane spanned by the inward normal to F and the direction from q to p. In this two-dimensional section, use q as the origin, let the horizontal coordinate point toward p, and let the vertical coordinate point into L.

The projection premise places the entire section in the half-strip with horizontal coordinate nonnegative and vertical coordinate nonnegative. The coordinates of c in this section are both strictly positive. The nonbase boundary edge leaving q has a nonzero direction e whose two coordinates are nonnegative. Therefore

```text
(q−c)·e < 0.
```

Moving a sufficiently small positive distance along that nonbase edge decreases squared distance to c. These points belong to R. Hence q cannot minimize r on R.

A minimizer q* on R is consequently away from the boundary of F. Locally it is a minimum of distance on the full boundary of L, not merely on an artificially restricted patch.

### Such a minimum lies inside a maximal facet

A local minimum of distance from an interior point cannot lie in the relative interior of a true edge or at a true vertex of a convex polyhedron.

Indeed, at such a point q*, the tangent cone is generated by feasible directions lying in boundary faces, together with its lineality directions when q* is on an edge. If every boundary direction had nonnegative first derivative of squared distance, their conic combinations would too. But `c−q*` is a feasible interior direction and

```text
(q*−c)·(c−q*) = −|q*−c|² < 0.
```

Thus some boundary direction would decrease distance, contradicting local minimality.

It follows that q* lies in the relative interior of a maximal facet other than F. The restriction of squared distance to that facet has positive-definite quadratic part. Its interior critical point is the perpendicular foot of c and is a **strict** minimum. This supplies a second distinct strict stable equilibrium.

This proves S≥2 even when unrelated features of L are degenerate. The conclusion is not merely “two closed stable candidates” or “one stable plus one weak point.” ∎

## 3. Why a tempting globally mass-controlled replacement cannot finish the task

I considered a whole-body replacement over a fixed planar base, rather than a cell whose interface mass was omitted. The theorem above closes this entire orthogonal-roof route to110.

Let D be a fixed polygon and let u be a nonnegative concave piecewise-affine function on a fixed triangulation of D, vanishing on its boundary. Define the actual filled solid

```text
K(u) = {(x,y,z) : (x,y) in D, 0≤z≤u(x,y)}.
```

Every interface is included in this definition. Convexity of the complete solid is equivalent to concavity of u. With density one,

```text
V   = ∫D u,
Mx  = ∫D x u,
My  = ∫D y u,
Mz  = (1/2)∫D u².
```

For a piecewise-affine direction f with `∫D f=0`, a finite replacement

```text
u' = u+t f,
t = −2∫D u f / ∫D f²
```

preserves both total volume and axial first moment exactly, whenever f is nonzero and the numerator is nonzero. Adding `∫D x f=∫D y f=0` preserves the complete first moment. This is a rational construction when the triangulation, heights and direction are rational; it requires no approximate centroid solve.

If both u and u' are nonnegative and concave, then every interpolated roof `(1−s)u+s u'` is globally valid. Along that path, volume is constant, transverse moments are affine, and

```text
Mz(s)=Mz(0)−(s(1−s)/2)∫D (u'−u)².
```

Thus even when the endpoints have the same complete mass data, the intermediate centroid generally moves. The changed material is a genuine deletion and replacement: equal-volume distinct members do not contain one another.

The finite mass law is useful, but it does **not** solve the mechanical problem. Every such solid lies in the orthogonal prism above its base D and contains the entire base. Therefore every admissible member has at least two strict stable equilibria, including when transverse moments are allowed to change. Freeing the upper stable triangle, all upper vertices and all unstable roots does not remove this obstruction.

This is an exact exclusion of the whole geometric family, not an unsuccessful search for a reflection direction. It also explains why an exact mass formula alone is insufficient evidence for a productive replacement architecture.

The available edge budget does not rescue this family. For a generic triangulated roof with n vertices in total and a b-sided base, the counts are

```text
V=n,   F=2n−b−1,   E=3n−b−3.
```

For b=18, n≤90 gives E≤249; for b=30, n≤94 does too. These are substantial budgets, but every orthogonal-roof member remains excluded by S≥2. Coplanar mergers can lower E without changing that conclusion.

**No assertion is made that the literal L18 is an orthogonal roof.** Establishing that from its exact coordinates is a necessary check, not a consequence of its75/204/131 combinatorics.

## 4. An exact, inexpensive certificate and a necessary escaping carrier

Suppose F has an outward-oriented boundary cycle

```text
a0,a1,...,a(b−1)
```

and outward normal n. For each boundary edge ai→a(i+1), define

```text
ui = n × (a(i+1)−ai),
σi(v) = ui·(v−ai).
```

Each ui lies in the plane of F, so

```text
σi(v)=σi(πF(v)).
```

For a body given as a convex hull of finitely many points, the projection premise is therefore exactly

```text
σi(vj) ≥ 0   for every facet edge i and every input point j.
```

Redundant input points are harmless. No tolerance, normal normalization, volume approximation, or equilibrium surrogate is needed.

Define the current overhang set

```text
OF = {j : σi(vj)<0 for at least one i}.
```

For any proposed final body retaining F, **S=1 requires OF to be nonempty for that final body**. Consequently, a surgery that removes every old overhang and adds no replacement overhang cannot succeed, even if it eliminates both old radial roots and exactly restores a chosen centroid.

This is a statement about the final geometry, not about preserving particular old labels. A successful construction may move or replace every member of the old overhang set. At least one final vertex must nevertheless violate one of these lateral prism inequalities. One overhang is necessary, not sufficient: it does not by itself cancel a Q bar, preserve U=1, or guarantee an admissible volume centroid.

The theorem also must not be applied automatically to every newly created cutting cap. A cut face need not contain the projection of the retained body. Its actual lateral inequalities must be tested.

## 5. Complete exact predicate implementation

The following standard-library program verifies that the nominated polygon is a true maximal supporting facet of the supplied convex hull, constructs the complete rational guard matrix, and returns either the strict two-stable exclusion or the complete set of overhang input labels.

It is an implementation of the proved predicate, **not an executed JOINT56 producer or auditor**. It makes no equilibrium claim when an overhang exists. It does not need to count edges or integrate mass for the negative certificate, because the theorem holds at every interior centre and without a complexity bound.

Input format:

```text
{"points": [[...],...], "facet": [cyclic input indices], "denominator": 1}
```

Coordinates may be integers, finite decimal strings, or rational strings such as `17/23`. The optional denominator divides every coordinate. The facet cycle must omit collinear and redundant boundary points.

Run a literal input with:

```sh
python projection_obstruction.py input.json report.json
```

Running without arguments performs two fully specified predicate checks: a cube with its bottom facet, followed by the same points with an added overhang. These are regression inputs, not new candidate constructions. Expected markers are `PROJECTION_PRISM_SELFTEST_PASS` and, for a certified input, `PROJECTION_PRISM_STRICT_S_GE_2`. **Neither marker is reported as observed in this continuation.** The program prints report bytes and SHA-256 after an actual run; none is invented here.

```python
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import sys


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def determinant(a, b, c):
    return dot(a, cross(b, c))


def certificate(data):
    scale = Q(data.get('denominator', 1))
    if scale <= 0:
        raise ValueError('The denominator must be positive.')
    points = [tuple(Q(x)/scale for x in p) for p in data['points']]
    if any(len(p) != 3 for p in points):
        raise ValueError('Every point must have three coordinates.')
    if len(points) < 4:
        raise ValueError('At least four points are required.')
    origin = points[0]
    if not any(determinant(sub(points[i], origin),
                           sub(points[j], origin),
                           sub(points[k], origin)) != 0
               for i, j, k in combinations(range(1, len(points)), 3)):
        raise ValueError('The convex hull is not full-dimensional.')

    cycle = list(data['facet'])
    if len(cycle) < 3 or len(set(cycle)) != len(cycle):
        raise ValueError('The facet needs at least three distinct indices.')
    if any(not isinstance(i, int) or not 0 <= i < len(points) for i in cycle):
        raise ValueError('Invalid facet index.')
    a, b, c = [points[i] for i in cycle[:3]]
    normal = cross(sub(b, a), sub(c, b))
    if normal == (0, 0, 0):
        raise ValueError('Remove collinear consecutive facet points.')
    height = dot(normal, a)
    plane_tests = [dot(normal, p)-height for p in points]
    if all(t >= 0 for t in plane_tests):
        cycle.reverse()
        normal = tuple(-x for x in normal)
        height = -height
        plane_tests = [-x for x in plane_tests]
    if not all(t <= 0 for t in plane_tests):
        raise ValueError('The nominated plane is not supporting.')
    if any(plane_tests[i] != 0 for i in cycle):
        raise ValueError('The nominated facet vertices are not coplanar.')

    rows = []
    edge_data = []
    for i, j in zip(cycle, cycle[1:]+cycle[:1]):
        inward = cross(normal, sub(points[j], points[i]))
        row = [dot(inward, sub(p, points[i])) for p in points]
        if row[i] != 0 or row[j] != 0:
            raise AssertionError('Boundary incidence failure.')
        if any(row[k] <= 0 for k in cycle if k not in (i, j)):
            raise ValueError('Facet cycle is not a strict convex boundary.')
        if any(row[k] < 0 for k, t in enumerate(plane_tests) if t == 0):
            raise ValueError('The nominated polygon is not the maximal facet.')
        rows.append(row)
        edge_data.append({'edge': [i, j], 'inward_in_plane': inward})

    violations = []
    for j in range(len(points)):
        bad = [i for i, row in enumerate(rows) if row[j] < 0]
        if bad:
            violations.append({'point': j, 'violated_edges': bad,
                               'negative_values': [rows[i][j] for i in bad]})
    excluded = not violations
    return {
        'dimension': 3,
        'points': points,
        'maximal_facet_cycle': cycle,
        'outward_normal': normal,
        'height': height,
        'support_tests': plane_tests,
        'facet_edges': edge_data,
        'projection_guard_matrix': rows,
        'overhangs': violations,
        'projection_contained_in_facet': excluded,
        'strict_S_lower_bound_for_every_interior_center': 2 if excluded else None,
        'own110_excluded_by_this_certificate': excluded,
        'scope': 'This convex hull; and every full-dimensional convex body '
                 'containing this facet and contained in its inward orthogonal prism.'
    }


def selftest():
    points = [list(p) for p in product((-1, 1), repeat=3)]
    face = [0, 2, 6, 4]
    a = certificate({'points': points, 'facet': face})
    assert a['projection_contained_in_facet']
    assert a['strict_S_lower_bound_for_every_interior_center'] == 2
    b = certificate({'points': points+[[2, 0, 1]], 'facet': face})
    assert not b['projection_contained_in_facet']
    assert [r['point'] for r in b['overhangs']] == [8]
    assert b['strict_S_lower_bound_for_every_interior_center'] is None
    return {'cube': a, 'overhang_predicate_control': b}


def main():
    if len(sys.argv) == 1:
        report = selftest()
        destination = Path('projection_prism_selftest.json')
        marker = 'PROJECTION_PRISM_SELFTEST_PASS'
    elif len(sys.argv) == 3:
        data = json.loads(Path(sys.argv[1]).read_text(), parse_float=str)
        report = certificate(data)
        destination = Path(sys.argv[2])
        marker = ('PROJECTION_PRISM_STRICT_S_GE_2'
                  if report['projection_contained_in_facet']
                  else 'NO_PROJECTION_PRISM_EXCLUSION')
    else:
        raise SystemExit('Usage: python projection_obstruction.py [input.json report.json]')
    raw = (json.dumps(report, sort_keys=True, separators=(',', ':'),
                      default=str)+'\n').encode('utf-8')
    destination.write_bytes(raw)
    print(marker)
    print('REPORT_BYTES_SHA256', len(raw), hashlib.sha256(raw).hexdigest())


if __name__ == '__main__':
    main()
```

## 6. Consequence for the next JOINT56 replacement

The useful next distinction is **not merely whether the large facet survives**. It is whether the final material still lies in that facet’s orthogonal prism. The exact guard matrix separates these cases without freezing roots, supports elsewhere, centre, volume, or edge count.

For L18/L30, the first continuation-critical datum is the overhang set of the actual large facet, computed from the literal parent. If it is empty, arbitrary multipoint reshaping confined to the prism is rigorously excluded; a successful facet-preserving replacement must cross a lateral prism boundary. If it is nonempty, those negative guards identify material that must not all be silently removed or flattened inward while retaining the same facet. A construction may instead replace the large facet, but its final stable facet must satisfy the corresponding necessary overhang condition too.

That geometric requirement does not resolve the opposite radial landscape. Added or relocated overhang material still changes the homogeneous centroid, may replace the unstable root, and may create small positive P/Q bars. Any proposed endpoint must receive the complete own-centred maximal-hull and strict/closed-weak audit requested in the assignment.

**Handoff status:** a proved, unrestricted-in-height retained-facet family exclusion and a complete exact predicate are preserved. No JOINT56 premise evaluation, numerical search outcome, new body, full-bar audit, execution receipt, or artifact hash is claimed from uninspectable tool output. The current literal JOINT56 parent remains the constructive entrance.
