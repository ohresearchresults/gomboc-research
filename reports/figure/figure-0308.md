# figure-0308

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# Exact quadratic-algebraic convex-boundary and equilibrium verifier

## Determination

This submission supplies a complete standard-library verifier, a finite global-embedding certificate, and exercised exact fixtures. **It does not certify a large Gömböc or replay the missing 227,905-vertex table.** The journal distinguishes the reported old instance from the new reconstruction and explicitly records the missing literal arrays; that distinction is preserved here. Its proposed input is the one implemented below.

The substantive addition is an **explicit radial-link winding check**. Positive radial determinants and convex adjacent dihedrals do not alone establish an embedded boundary. I constructed a ten-vertex triangulated sphere with all those signs strict, all vertex links single cycles, and Euler characteristic two, whose radial image covers a generic direction three times. The verifier rejects it. The journal's proposed degree-one ray check would also reject this example; the example does **not** falsify that complete proposed route. It identifies the missing local-injectivity justification at vertices, which the additional exact winding counts resolve constructively. The earlier journal's global argument is therefore treated as a proof route to complete, not as a previously replayed certificate.

Two newly created, small, genuinely quadratic-algebraic, exactly centred **nonwinners** pass the geometry and strict-classification checks. A second implementation using rational pairs, all-triangle/all-vertex supporting inequalities, and explicit two-normal Gram solves independently reproduces their classifications. A third exactly centred convex fixture is rejected for a genuine boundary-degenerate equilibrium. These are software cross-checks produced in this assignment, not external peer review or formal verification of the Python interpreter.

## 1. Precise input and output contract

Place three files in one directory:

* `vertices.csv.gz`: ASCII CSV with exact header `ix,iy,iz,b`, one literal integer quadruple per row. The row number, beginning at zero, is the vertex index. Its physical coordinate is `v_i(t)=(ix_i-t*b_i, iy_i, iz_i)/D`.
* `triangles.csv.gz`: ASCII CSV with exact header `i,j,k`, one ordered, outward triangle per row. Indices refer to the vertex rows. Supply a triangulation of the entire proposed boundary, including triangulations of polygonal facets. Do not omit a cap or supply an artificial closure for a local patch.
* `definition.json`: version 1, positive integer `D`, primitive coefficients `A>0,Bc,C`, and `root_interval=[[Ln,Ld],[Un,Ud]]` with positive denominators. The selected root of `Q(t)=A*t^2+Bc*t+C` must lie strictly between the rational endpoints. The version-1 format requires a genuine real quadratic field: positive nonsquare discriminant. JSON integers may instead be decimal-integer strings. Optional `generic_ray` is a nonzero integer triple, default `[3,11,17]`.

A concrete definition for the nine-vertex merged-facet fixture is:

```json
{"version":1,"D":100,"A":3972,"Bc":-419995,"C":-179300,"root_interval":[[-43,100],[-21,50]],"generic_ray":[3,11,17]}
```

The table must be literally C2-paired: every `(ix,iy,iz,b)` has exactly one counterpart `(ix,-iy,-iz,b)`, possibly itself on the x axis. Duplicate rows are rejected. Because the parameter is irrational, distinct literal coefficient rows cannot secretly coincide at the selected root. Every supplied point must be an actual extreme vertex, not an unused point, face-interior triangulation point, or subdivision point on a true edge.

The quadratic is **derived-data checked**, not accepted merely because it is named in the JSON. The verifier recomputes the raw x first-moment polynomial, requires it to be nonzero quadratic, and requires its primitive positive-leading normalization to equal `[C,Bc,A]` in ascending order. It also checks both other moments exactly. Neither an arbitrary algebraic root nor a translated reference point substitutes for ordinary centring.

Run:

```bash
python verify_gomboc.py /path/to/input_directory
```

Only a completely verified strict class `(S,U,H)=(1,1,0)` produces `VERIFIED_GOMBOC` and exit status zero in this default mode. For diagnostics on valid strict nonwinners:

```bash
python verify_gomboc.py /path/to/input_directory --classify
```

That mode labels another class `VERIFIED_STRICT_NONWINNER`; it is not target acceptance. A failed check produces `REJECTED`, a named gate, and an offending index or other detail. A bad ray is a bad auxiliary certificate, not a nonexistence conclusion about the shape. Supply another ray and rerun. The rational sequence `(1,k,k^2)` eventually provides a generic ray: each of the finitely many nonzero edge-plane normals excludes at most two integer values of `k`.

A passing report contains all equilibrium identities, stable boundary cycles, actual and triangulated incidence counts, the exact volume and moment coefficient arrays and denominators, the root bracket, exact-zero/fallback counters, and SHA-256 hashes of the three input byte snapshots actually parsed. Facet identities are the minimum triangle index within their exact coplanar component. No old expected feature counts, floating hull, or source-lineage alias enters acceptance.

## 2. Exact arithmetic

All geometry uses the unscaled points `p_i=(ix_i-t*b_i,iy_i,iz_i)`. The common positive `D` does not affect signs and is restored in volume and first moments.

For `P(t)=p0+p1*t+p2*t^2`, reduce to

`A*P(t)=(A*p0-C*p2)+(A*p1-Bc*p2)*t`.

Since `A>0`, this preserves sign. Let the selected root be `t=(-Bc+s*sqrt(Delta))/(2A)`. A linear expression `a+b*t` has the sign of

`X+Y*sqrt(Delta)`, where `X=2A*a-Bc*b` and `Y=s*b`.

Equal signs settle the result immediately. For opposite signs, the exact sign is `sign(X)*sign(X^2-Y^2*Delta)`. The root branch follows from the endpoint polynomial signs, which must be opposite. An outward-rounded 64-bit dyadic enclosure supplies a faster **exact** filter; inconclusive filters fall back to the radical comparison, never a tolerance. Zero is returned exactly, not inferred from small magnitude.

The cross product of two point differences has a constant x component and affine y and z components. Radial tetrahedral determinants and adjacent-dihedral determinants are affine. Face-side predicates, directed vertex supports, and determinants of three incident normals have degree at most two. The edge-cone shortcut in Section 6 avoids higher-degree Gram expressions in production; the independent test oracle uses those Gram expressions instead.

Rational-root, repeated-root, and linear/identically-zero x-moment formats are deliberately outside version 1 and are rejected explicitly. This is an interface limitation, not a claim that such bodies cannot exist.

## 3. Global radial fan: a finite proof of embedding and nonoverlap

Let the abstract triangle complex be `M`. The code verifies that every triangle has three distinct valid indices, every unoriented edge occurs exactly twice with opposite orientations, the triangle adjacency graph is connected, every vertex is used, and every vertex link is a single cycle. Duplicate triangles cannot evade these checks together with positive radial determinants: equally oriented duplicates violate edge orientation or multiplicity, and oppositely oriented duplicates cannot both have positive determinant. Thus `M` is a finite connected closed oriented simplicial 2-manifold. Euler characteristic two is checked, but is not used in place of these manifold conditions.

For every oriented triangle `(a,b,c)`, require `det(a,b,c)>0` at the selected root. Its affine triangle avoids the origin and projects radially homeomorphically, with positive orientation, onto its spherical triangle. Across an abstract edge, the two opposite third vertices lie on opposite sides of the great circle: their radial determinant signs are opposite when expressed with the same edge orientation. Hence radial projection is locally one-to-one in triangle interiors and edge interiors.

**The vertex step must not be assumed.** At a vertex `a`, project successive neighbour directions to `a`'s tangent plane. Each successive pair has positive determinant, so its oriented sector angle is strictly between zero and pi. As the combinatorial link cycle closes, these positive increments can sum to `2*pi*k`, with `k>1` possible.

The same rational ray used for the global count determines `k` exactly, with no angles or square roots. For a triangle `(a,b,c)` define the three Cramer numerator signs

```text
s_a = sign(det(r,b,c))
s_b = sign(det(a,r,c))
s_c = sign(det(a,b,r)).
```

All are required nonzero. At vertex `a`, the tangent projection of `r` lies in that triangle's tangent sector exactly when `s_b>0` and `s_c>0`: those are the coefficients of the projected neighbour vectors. The cyclic rules apply at `b,c`. Count these incidences over each vertex link and require **exactly one for every vertex**. Because all link increments are positive and less than pi, this count is its winding number. Winding one makes the link map one-to-one and the radial map locally a homeomorphism at the vertex as well.

Now the radial map `M -> S^2` is a local homeomorphism everywhere. Its image is open, and compactness makes it closed, hence the entire connected sphere. Each fibre is discrete and compact, therefore finite. Disjoint local inverse neighbourhoods of its finitely many preimages, followed by a smaller target neighbourhood and compactness of the complement, show that the fibre count is locally constant. Thus the map is a finite covering, without any assumed geometric embedding of the input mesh.

The code counts strict positive **three-coordinate** cone hits of the generic ray over all triangles and requires exactly one. The covering therefore has one sheet. The radial map is a continuous bijection from compact `M` to the sphere, hence a homeomorphism. In particular, the closed spherical triangles cover the sphere completely and meet only along their actual shared simplices. Their positive cones form a genuine complete nonoverlapping fan. This establishes all boundary points too, not merely almost-everywhere coverage.

### Exact counterexample to omitting this step

Take axial vertices `(5,0,0),(-5,0,0)` and equatorial points `(0,y,z)` with

```text
(y,z) = (5,0),(3,4),(0,5),(-3,4),(-5,0),(-3,-4),(0,-5),(3,-4).
```

Give the equatorial points indices `2..9` and cycle `c_i=2+(3i mod 8)`. The sixteen triangles are `(0,c_i,c_(i+1))` and `(1,c_(i+1),c_i)`. It is an oriented abstract sphere with `(V,E,T)=(10,24,16)`, single-cycle links, positive radial determinants, and all 24 adjacent-dihedral determinants strictly negative, lying between `-320` and `-150`. Nevertheless `(3,11,17)` lies in triangles `0,6,10`: the radial degree is three, and the axial links have winding three. The production verifier rejects `wrapped3` at `radial_degree_not_one` after its abstract-manifold checks. Its dummy quadratic is only an arithmetic input for this geometric rejection fixture; no valid ordinary-centroid certificate is asserted for that self-overlapping triangle chain.

## 4. Local dihedrals now imply global convexity

For triangle `f=(a,b,c)`, set `n_f=(b-a) cross (c-a)` and `h_f=n_f dot a>0`. On its proved radial cone, define the linear gauge piece

`g(x)=(n_f dot x)/h_f`.

These pieces agree on shared cone faces because they take value one at every triangle vertex. Thus they define a continuous positively homogeneous function on all of R3.

Across an edge, let `d` be the opposite vertex in the other triangle. The code requires `n_f dot(d-a)<=0`. Consequently the other gauge piece is at least the first on the other cone, with equality on the separating plane; the reverse inequality holds on the first cone. Locally the two pieces form their maximum, so the gauge bends convexly across every two-dimensional cone wall.

For a generic line segment missing the finitely many cones of dimension at most one, the gauge is piecewise affine and its slope never decreases at a crossed wall. Its restriction is convex. Perturbing endpoints and taking limits extends the convexity inequality to **every** segment, including segments through vertices, cone edges, or the origin. This is the complete local-to-global argument; it does not assume the input is already a convex polyhedron. General local criteria for convexity of piecewise-defined functions are also developed by Bauschke, Lucet and Phan; the specialized argument here is supplied in full rather than delegated to that reference.

The gauge is strictly positive away from zero: in any cone, writing `x=alpha*a+beta*b+gamma*c` with nonnegative coefficients gives `g(x)=alpha+beta+gamma>0`. Continuity on the unit sphere makes its unit sublevel set bounded and gives a neighbourhood of zero inside it. Therefore `K={g<=1}` is a full-dimensional compact convex body, with boundary exactly the input triangle union. It is the convex hull of the supplied vertices. Each triangle plane is a globally supporting plane of `K`: at an interior point of its cone the corresponding linear piece is a gradient of the convex gauge, so its global tangent inequality gives `g(x)>=(n_f dot x)/h_f`.

## 5. Actual facets, edges and vertices

Exactly-zero dihedral determinants are merged by disjoint-set union. Adjacent coplanar outward normals are positive multiples because their support values are positive. Their union is a single supporting-plane component. Global convexity implies that the equality set of any supporting plane is convex; its triangulation is edge-connected in its relative interior. Thus adjacency merging finds the **maximal** facets, not only locally planar patches.

For every merged component, the verifier traverses all its noncoplanar boundary halfedges across internal triangulation diagonals. It requires one simple oriented boundary cycle, no repeated boundary vertex, and strictly positive turns. Diagonals internal to a maximal face are removed from the true-edge ledger.

Finally each input vertex must have three linearly independent incident supporting-plane normals. Those planes expose a singleton, proving actual extremality. A face-interior point has rank one, and a true-edge subdivision point has rank at most two. The test rejects both rather than counting them as vertices. With this extremality and the established embedding, each unmerged edge is one whole actual polyhedral edge. Actual Euler characteristic is checked again only as a consistency check.

## 6. Exhaustive strict mechanics, including all edge-cone components

The reference point is the origin, later proved to be the ordinary volume centroid. For a maximal facet with outward normal `n`, the projection of zero onto its plane is in the strict interior exactly when every directed boundary edge `a -> b` has

`F(a,b)=n dot(a cross b)>0`.

Indeed, substituting the foot into the inward planar edge-halfspace test cancels its normal component and gives precisely this expression. All facet boundary inequalities are evaluated; testing triangles separately would incorrectly count display-diagonal boundaries.

At a true vertex `a`, use every true neighbour `b` and evaluate

`U(a,b)=a dot(a-b)`.

The incident true-edge directions generate its tangent cone. All values strictly positive are equivalent to `a` lying in the interior of its full outward normal cone, hence strict instability. No simplicity or three-facet assumption is made at a high-valence apex.

For a true edge oriented `a -> b` in the first face, let `e=b-a`, let the incident normals be `n1,n2`, and put

```text
L = a dot(a-b)
R = b dot(b-a)
F1 = n1 dot(a cross b)
F2 = n2 dot(b cross a).
```

The line foot is `p=a+tau*e`, where `tau=L/|e|^2` and `1-tau=R/|e|^2`. The normals span `e`'s orthogonal complement. If the opposite face vertices are `c,d`, strict convexity at this true edge gives

`K=(n1 cross n2) dot e = -det(e,c-a,d-a)*|e|^2 > 0`.

Solving `p=beta1*n1+beta2*n2` gives

`beta1=F2/K`, `beta2=F1/K`.

Representative normals of merged faces are positive rescalings, which do not change these signs. Thus the **four** signs `(L,R,F1,F2)` are exactly the two interior-foot signs and both full normal-cone coefficient signs. An edge is a strict saddle if and only if all four are positive. The shortcut is not an inference from Euler counts; the independent fixture oracle additionally computes both beta values using the full exact Gram inverse.

For each feature, a strictly negative component excludes it, even if an irrelevant other component is zero. If all components are nonnegative and at least one is zero, the feature is a boundary-degenerate equilibrium candidate and the verifier rejects the input. All-positive components include the feature. This distinction prevents both false acceptance of degenerate equilibria and needless rejection merely because a noncritical predicate happens to vanish elsewhere. The boundary strata are exactly facets, true edges and true vertices, so the classification is exhaustive. `S+U-H=2` is checked only after all these decisions.

## 7. Ordinary volume and centroid, bound to the actual data

For each oriented triangle, the unscaled radial determinant is `H_f(t)=h0_f+h1_f*t`. Since the radial fan and convex-boundary proof have passed, these are positive tetrahedral volumes of a genuine partition, not formal signed-chain volumes.

Let `X_f` be the sum of its three integer x constants, `B_f` the sum of their x coefficients (the negatives of the input b values), and `Y_f,Z_f` their other coordinate sums. Compute

```text
6 D^3 V(t) = sum_f (h0_f+h1_f*t)
24 D^4 Mx(t) = sum_f [h0_f*X_f
                  +(h0_f*B_f+h1_f*X_f)*t+h1_f*B_f*t^2]
24 D^4 My(t) = sum_f (h0_f+h1_f*t)*Y_f
24 D^4 Mz(t) = sum_f (h0_f+h1_f*t)*Z_f.
```

The first x numerator must have the same primitive quadratic as the supplied Q. The other two must vanish at its selected root. They are affine here, so in a genuine quadratic field that entails **identical polynomial zero**. Positive volume is checked separately. Therefore the true uniform-volume centroid is exactly `(0,0,0)`, with no translation, external mechanical centre or density weighting introduced.

## 8. Exercised fixtures and acceptance boundaries

The complete literal fixture arrays and deterministic gzip writer are in the test source below; no numerical hull generator is required to reproduce them.

| Fixture | Exact result |
|---|---|
| `irregular10` | Actual `(V,E,F)=(10,24,16)`, strict `(S,U,H)=(12,10,20)`; independent all-pairs/Gram oracle agrees. |
| `merged9` | 14 triangles merge into 13 facets, with one removed diagonal; actual `(9,20,13)`, strict `(13,9,20)`; independent oracle agrees. |
| `degenerate9` | Passes convex embedding, extremality and actual quadratic centring; rejected at true edge `[1,2]` with signs `[+1,0,+1,+1]`. |
| `wrapped3` | Passes positive radial signs and abstract manifold tests; independently all dihedrals are convex; rejected because its ray has three cone hits. |
| `concave9` | Radial contraction of one axial point preserves its radial fan but creates a concave dihedral; rejected at edge `[6,4]`. |
| `nonextreme_face_point` | Subdivides a planar quadrilateral with its centre; rejected because vertex 9 has supporting-normal rank below three. |

The four remaining rejection tests are an open mesh, an inward triangle, a wrong moment quadratic, and a nongeneric ray. Two additional gate tests reject a bracket containing both quadratic roots and reject `irregular10` in **default Gömböc mode**. There are ten expected rejections in total.

For `irregular10`, the unscaled volume numerator is `12108000+45000*t` and the x-moment numerator is

`702810000-548124000*t-2156100*t^2 = -300*(7187*t^2+1827080*t-2342700)`.

Four edges have strict interior line feet but fail a normal-cone coefficient. A line-foot-only saddle test would overcount them. For `merged9`, the respective polynomials are `15920000-146400*t` and

`-286880000-671992000*t+6355200*t^2 = 1600*(3972*t^2-419995*t-179300)`.

Both fixtures have identically zero y and z moment polynomials. Volume divides by `6*100^3`; first moments divide by `24*100^4`.

The arithmetic tests exercise 200 Pell approximants on each root of `t^2-2`, including nonzero values arbitrarily smaller than the interval-filter width, exact quadratic zeros, and 729 small polynomials in the nonmonic field `3*t^2+5*t-7`, compared against separate Fraction arithmetic and rational root bisection. Both signs of the square-root branch and exact-zero cases are covered.

The exercised replay ends with:

```text
TWO_LITERAL_CENTRED_FIXTURES_GLOBAL_ALL_PAIRS_AND_GRAM_PASS
TEN_EXPECTED_REJECTIONS_PASS
EXACT_QUADRATIC_SIGN_TESTS_PASS
ALL_SMALL_EXACT_TESTS_PASS
```

The production geometry has linear-size storage: compact integer arrays for triangles, opposite halfedges, links and components, plus an edge hash table and the literal arbitrary-precision vertex integers. Apart from hashing/union-find and sorting the reported saddle list, its work is proportional to the triangulation size, with bounded-degree exact predicates. It does **not** perform an all-faces/all-vertices hull audit; that quadratic audit is confined to the small independent test oracle.

A roughly 250,000-vertex/500,000-triangle run has **not** been benchmarked or executed in this assignment. Integer bit lengths, Python object overhead and input order affect actual resources. There is no unresolved geometric proof step within the stated version-1 contract; the outstanding acceptance gate is execution on the **new actual full input table and triangulation**, followed by review of its literal report and input hashes. The listed tests do not prove absence of every possible implementation bug. The verifier never repairs or silently drops offending triangles, vertices or equilibria.

## 9. Full executable sources

Save the first source as `verify_gomboc.py` and the second beside it as `test_verifier.py`. Run `python test_verifier.py` to exercise the fixtures in a temporary directory, or `python test_verifier.py --fixtures fixtures` to materialize every literal test input and report.

### verify_gomboc.py

```python
#!/usr/bin/env python3
"""Exact C2 quadratic-algebraic convex-polyhedron/Gomboc verifier.

Python 3.10+, standard library only. Default mode requires (S,U,H)=(1,1,0).
--classify verifies geometry, the actual derived centring quadratic, and strict
mechanics, but labels a different class VERIFIED_STRICT_NONWINNER.
Coordinates: (ix - t*b, iy, iz)/D. No floating-point geometric predicate.
The companion proof explains the degree-one radial fan and PL gauge steps.
"""
import argparse
from array import array
import csv
from fractions import Fraction
import gzip
import hashlib
import io
import json
from math import gcd, isqrt
from pathlib import Path
import re
import sys


class Reject(Exception):
    def __init__(self, gate, detail):
        super().__init__(gate + ': ' + str(detail))
        self.gate, self.detail = gate, detail


def need(ok, gate, detail):
    if not ok:
        raise Reject(gate, detail)


def integer(x):
    if type(x) is int:
        return x
    if isinstance(x, str) and re.fullmatch(r'-?(0|[1-9][0-9]*)', x):
        return int(x)
    raise Reject('input_integer', repr(x))


def sg(x):
    return (x > 0) - (x < 0)


class Quadratic:
    """Sign of polynomials of degree <=2 at one specified irrational root."""
    def __init__(self, definition):
        self.A, self.B, self.C = (integer(definition[k]) for k in ('A','Bc','C'))
        A, B, C = self.A, self.B, self.C
        need(A > 0 and gcd(gcd(A, abs(B)), abs(C)) == 1,
             'primitive_quadratic', [A,B,C])
        self.disc = B*B - 4*A*C
        need(self.disc > 0 and isqrt(self.disc)**2 != self.disc,
             'irreducible_real_quadratic', self.disc)
        endpoints = definition['root_interval']
        need(type(endpoints) is list and len(endpoints) == 2,
             'root_interval', endpoints)
        ends = []
        for e in endpoints:
            need(type(e) is list and len(e) == 2, 'rational_endpoint', e)
            n, d = map(integer, e)
            need(d > 0, 'endpoint_denominator', d)
            ends.append(Fraction(n,d))
        self.lo, self.hi = ends
        need(self.lo < self.hi, 'ordered_root_interval', endpoints)
        def q_at(r):
            n,d = r.numerator,r.denominator
            return A*n*n+B*n*d+C*d*d
        qlo,qhi = q_at(self.lo),q_at(self.hi)
        need(qlo*qhi < 0, 'isolates_one_simple_root', [qlo,qhi])
        self.branch = 1 if qlo < 0 else -1
        self.bits = 64
        scale = 1 << self.bits
        self.L = (self.lo.numerator*scale)//self.lo.denominator
        self.U = -((-self.hi.numerator*scale)//self.hi.denominator)
        self.calls = self.fallbacks = self.zeros = 0

    def linear(self, a, b):
        if b == 0:
            return sg(a)
        # Exact outward dyadic filter, not a numerical tolerance.
        lo = (a << self.bits) + b*(self.L if b > 0 else self.U)
        hi = (a << self.bits) + b*(self.U if b > 0 else self.L)
        if lo > 0:
            return 1
        if hi < 0:
            return -1
        self.fallbacks += 1
        x = 2*self.A*a - self.B*b
        y = self.branch*b
        if x == 0:
            return sg(y)
        if y == 0 or sg(x) == sg(y):
            return sg(x)
        # Opposite signs: compare their squares; all multipliers are positive.
        return sg(x)*sg(x*x-y*y*self.disc)

    def sign(self, p):
        self.calls += 1
        need(len(p) <= 3, 'predicate_degree', len(p)-1)
        a = p[0] if p else 0
        b = p[1] if len(p) > 1 else 0
        c = p[2] if len(p) > 2 else 0
        if c:
            a,b = self.A*a-self.C*c, self.A*b-self.B*c
        s = self.linear(a,b)
        self.zeros += (s == 0)
        return s


def diff(a,b):
    # Internal point format: (x_constant, x_t_coefficient, y, z).
    return tuple(x-y for x,y in zip(a,b))


def cross(a,b):
    # A vector cross product has format (nx, ny0, ny1, nz0, nz1).
    x,u,y,z = a
    X,U,Y,Z = b
    return (y*Z-z*Y, z*X-x*Z, z*U-u*Z,
            x*Y-y*X, u*Y-y*U)


def normal(a,b,c):
    return cross(diff(b,a),diff(c,a))


def npoint(n,p):
    x,y,v,z,w = n
    X,U,Y,Z = p
    return (x*X+y*Y+z*Z, x*U+v*Y+w*Z)


def ndot(n,m):
    x,y,v,z,w = n
    X,Y,V,Z,W = m
    return (x*X+y*Y+z*Z, y*V+v*Y+z*W+w*Z, v*V+w*W)


def sigma(a,b):
    x,u,y,z = a
    X,U,Y,Z = diff(a,b)
    return (x*X+y*Y+z*Z, x*U+u*X, u*U)


def nminors(a,b):
    x,y,v,z,w = a
    X,Y,V,Z,W = b
    return ((y*Z-z*Y, y*W+v*Z-z*V-w*Y, v*W-w*V),
            (z*X-x*Z, w*X-x*W), (x*Y-y*X, x*V-v*X))


def ndet(a,b,c):
    # x normal components are constant, so the 3x3 determinant is quadratic.
    terms = ((a[0], nminors(b,c)[0]),
             (-b[0], nminors(a,c)[0]),
             (c[0], nminors(a,b)[0]))
    return tuple(sum(k*p[j] for k,p in terms) for j in range(3))


def nxt(h):
    return h-2 if h%3 == 2 else h+1


def csv_snapshot(path, header):
    raw = path.read_bytes()  # Hash and parse the same immutable byte snapshot.
    digest = hashlib.sha256(raw).hexdigest()
    binary = gzip.GzipFile(fileobj=io.BytesIO(raw), mode='rb')
    text = io.TextIOWrapper(binary, encoding='ascii', newline='')
    reader = csv.reader(text, strict=True)
    need(next(reader, None) == header, 'csv_header', str(path))
    return reader, text, digest


def load(folder):
    folder = Path(folder)
    raw = (folder/'definition.json').read_bytes()
    d = json.loads(raw)
    need(type(d) is dict, 'definition_object', type(d).__name__)
    need(type(d.get('version')) is int and d['version'] == 1,
         'definition_version', d.get('version'))
    D = integer(d['D'])
    need(D > 0, 'positive_D', D)
    q = Quadratic(d)
    ray = d.get('generic_ray', [3,11,17])
    need(type(ray) is list and len(ray) == 3, 'generic_ray', ray)
    ray = list(map(integer,ray))
    need(any(ray), 'nonzero_generic_ray', ray)
    hashes = {'definition.json': hashlib.sha256(raw).hexdigest()}
    reader,text,hsh = csv_snapshot(folder/'vertices.csv.gz', ['ix','iy','iz','b'])
    points = []
    with text:
        for row in reader:
            need(len(row) == 4, 'vertex_row', row)
            x,y,z,b = map(integer,row)
            points.append((x,-b,y,z))
    nv = len(points)
    need(nv >= 4, 'vertex_count', nv)
    pool = set(points)
    need(len(pool) == nv, 'duplicate_vertex', nv-len(pool))
    for i,(x,u,y,z) in enumerate(points):
        need((x,u,-y,-z) in pool, 'C2_vertex_pair', i)
    del pool
    hashes['vertices.csv.gz'] = hsh
    reader,text,hsh = csv_snapshot(folder/'triangles.csv.gz', ['i','j','k'])
    tri = array('q')
    with text:
        for row in reader:
            need(len(row) == 3, 'triangle_row', row)
            t = tuple(map(integer,row))
            need(len(set(t)) == 3 and min(t) >= 0 and max(t) < nv,
                 'triangle_indices', t)
            tri.extend(t)
    need(len(tri) >= 12, 'triangle_count', len(tri)//3)
    hashes['triangles.csv.gz'] = hsh
    return d,D,q,tuple(ray),points,tri,hashes


def verify(folder, require_gomboc=True):
    definition,D,q,ray,P,T,hashes = load(folder)
    nv,nt,nh = len(P),len(T)//3,len(T)
    opposite = array('q', [-1])*nh
    first = array('q', [-1])*nv
    degree = array('q', [0])*nv
    winding = array('q', [0])*nv
    edge_map = {}
    vol = [0,0]
    moments = [[0,0,0] for _ in range(3)]
    ray_point = (ray[0],0,ray[1],ray[2])
    ray_hits = []
    def vertices(f):
        k = 3*f
        return P[T[k]],P[T[k+1]],P[T[k+2]]
    def fnormal(f):
        return normal(*vertices(f))
    for f in range(nt):
        a,b,c = vertices(f)
        n = normal(a,b,c)
        h = npoint(n,a)
        need(q.sign(h) > 0, 'positive_radial_determinant', f)
        h0,h1 = h
        vol[0] += h0
        vol[1] += h1
        sx,su,sy,sz = (sum(v[j] for v in (a,b,c)) for j in range(4))
        moments[0][0] += h0*sx
        moments[0][1] += h0*su+h1*sx
        moments[0][2] += h1*su
        for j,s in ((1,sy),(2,sz)):
            moments[j][0] += h0*s
            moments[j][1] += h1*s
        signs = [q.sign(npoint(cross(x,y),ray_point))
                 for x,y in ((b,c),(c,a),(a,b))]
        need(0 not in signs, 'nongeneric_ray', {'triangle':f,'signs':signs})
        if min(signs) > 0:
            ray_hits.append(f)
        # At vertex a the projected ray is inside its tangent sector iff
        # the Cramer coefficients of b and c are both positive; cyclically.
        for j in range(3):
            if signs[(j+1)%3] > 0 and signs[(j+2)%3] > 0:
                winding[T[3*f+j]] += 1
        for hidx in range(3*f,3*f+3):
            i,j = T[hidx],T[nxt(hidx)]
            degree[i] += 1
            first[i] = hidx
            key = min(i,j)*nv+max(i,j)
            old = edge_map.get(key)
            if old is None:
                edge_map[key] = hidx
            else:
                need(old >= 0, 'edge_more_than_two_triangles', [i,j])
                need(T[old] == j and T[nxt(old)] == i,
                     'inconsistent_edge_orientation', [i,j])
                opposite[hidx],opposite[old] = old,hidx
                edge_map[key] = -1
    ne_tri = len(edge_map)
    need(all(v == -1 for v in edge_map.values()), 'open_mesh', 'unpaired edge')
    del edge_map
    need(nv-ne_tri+nt == 2, 'triangulated_Euler', [nv,ne_tri,nt])
    visited = bytearray(nt)
    stack = [0]
    visited[0] = 1
    reached = 0
    while stack:
        f = stack.pop()
        reached += 1
        for h in range(3*f,3*f+3):
            g = opposite[h]//3
            if not visited[g]:
                visited[g] = 1
                stack.append(g)
    need(reached == nt, 'disconnected_surface', reached)
    del visited,stack
    for i in range(nv):
        need(degree[i] >= 3, 'unused_or_low_degree_vertex', i)
        start = h = first[i]
        steps = 0
        while True:
            need(T[h] == i, 'vertex_link_endpoint', i)
            steps += 1
            h = nxt(opposite[h])
            if h == start or steps >= degree[i]:
                break
        need(h == start and steps == degree[i], 'vertex_link_not_one_cycle', i)
    need(len(ray_hits) == 1, 'radial_degree_not_one', ray_hits)
    for i,w in enumerate(winding):
        need(w == 1, 'vertex_radial_winding_not_one', [i,w])
    del winding
    # Explicit link winding one makes the radial map a local homeomorphism
    # even at vertices. Compactness gives a covering; the one ray hit fixes
    # its degree at one, proving an embedded complete spherical fan.
    parent = array('q', range(nt))
    size = array('q', [1])*nt
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def union(i,j):
        i,j = find(i),find(j)
        if i == j:
            return
        if size[i] < size[j]:
            i,j = j,i
        parent[j] = i
        size[i] += size[j]
    flat = bytearray(nh)
    flat_count = 0
    for h in range(nh):
        k = opposite[h]
        if h > k:
            continue
        a = P[T[h]]
        d = P[T[nxt(nxt(k))]]
        s = q.sign(npoint(fnormal(h//3),diff(d,a)))
        need(s <= 0, 'concave_dihedral', [T[h],T[nxt(h)]])
        if s == 0:
            flat[h] = flat[k] = 1
            flat_count += 1
            union(h//3,k//3)
    # A continuous PL gauge on the now-proved complete fan is convex from
    # these local inequalities. Its unit sublevel is the actual convex hull.
    face = array('q', (find(f) for f in range(nt)))
    canonical = array('q', [-1])*nt
    for f,r in enumerate(face):
        if canonical[r] < 0:
            canonical[r] = f
    del parent,size
    boundary_first = array('q', [-1])*nt
    boundary_count = array('q', [0])*nt
    for h in range(nh):
        r = face[h//3]
        need((r == face[opposite[h]//3]) == bool(flat[h]),
             'inconsistent_face_merge', h)
        if not flat[h]:
            boundary_first[r] = h
            boundary_count[r] += 1
    side = array('b', [0])*nh
    seen = bytearray(nh)
    stable = []
    stable_cycles = []
    facet_count = 0
    for r in range(nt):
        if canonical[r] < 0:
            continue
        facet_count += 1
        start = boundary_first[r]
        need(start >= 0 and boundary_count[r] >= 3, 'facet_without_boundary', r)
        n = fnormal(canonical[r])
        h = start
        cycle = []
        minimum = 1
        for _ in range(boundary_count[r]):
            need(not seen[h] and not flat[h] and face[h//3] == r,
                 'facet_boundary_not_one_cycle', canonical[r])
            seen[h] = 1
            i,j = T[h],T[nxt(h)]
            cycle.append(i)
            s = q.sign(ndot(n,cross(P[i],P[j])))
            side[h] = s
            minimum = min(minimum,s)
            k = nxt(h)
            for step in range(degree[j]+1):
                if not flat[k]:
                    break
                k = nxt(opposite[k])
            else:
                raise Reject('facet_boundary_walk', canonical[r])
            need(T[k] == j, 'facet_boundary_endpoint', canonical[r])
            h = k
        need(h == start and len(set(cycle)) == len(cycle),
             'facet_boundary_not_simple_cycle', canonical[r])
        # Strict turns exclude redundant collinear boundary points.
        for j,i in enumerate(cycle):
            a,b,c = P[cycle[j-1]],P[i],P[cycle[(j+1)%len(cycle)]]
            turn = q.sign(ndot(n,cross(diff(b,a),diff(c,b))))
            need(turn > 0, 'facet_corner_not_extreme', i)
        need(minimum != 0, 'boundary_degenerate_face_equilibrium', canonical[r])
        if minimum > 0:
            stable.append(canonical[r])
            stable_cycles.append(cycle)
    need(sum(boundary_count) == sum(seen), 'unvisited_facet_boundary', 'count')
    del seen,boundary_count,boundary_first
    # Every listed point must be an actual 3D hull vertex, not an interior
    # triangulation point. Three independent incident supporting normals
    # give an exposed singleton. Zero minors are handled exactly.
    for i in range(nv):
        a = b = None
        rank3 = False
        h = first[i]
        for _ in range(degree[i]):
            c = fnormal(h//3)
            if a is None:
                a = c
            elif b is None:
                if any(q.sign(p) != 0 for p in nminors(a,c)):
                    b = c
            elif q.sign(ndet(a,b,c)) != 0:
                rank3 = True
                break
            h = nxt(opposite[h])
        need(rank3, 'vertex_normal_rank_below_three', i)
    ne = ne_tri-flat_count
    need(nv-ne+facet_count == 2, 'polyhedral_Euler', [nv,ne,facet_count])
    # The following is now uniform-volume integration of an embedded body,
    # not a signed-chain calculation on a possibly self-overlapping mesh.
    nx = moments[0]
    need(nx[2] != 0, 'x_moment_not_quadratic', nx)
    content = gcd(gcd(abs(nx[0]),abs(nx[1])),abs(nx[2]))
    primitive = [sg(nx[2])*v//content for v in nx]
    need(primitive == [q.C,q.B,q.A], 'quadratic_not_actual_x_moment', primitive)
    need(all(q.sign(m) == 0 for m in moments), 'nonzero_volume_moment', moments)
    need(q.sign(vol) > 0, 'nonpositive_volume', vol)
    vminimum = array('b', [1])*nv
    true_degree = array('q', [0])*nv
    saddles = []
    rejected_by_normal_only = 0
    for h in range(nh):
        k = opposite[h]
        if h > k or flat[h]:
            continue
        i,j = T[h],T[nxt(h)]
        si,sj = q.sign(sigma(P[i],P[j])),q.sign(sigma(P[j],P[i]))
        vminimum[i] = min(vminimum[i],si)
        vminimum[j] = min(vminimum[j],sj)
        true_degree[i] += 1
        true_degree[j] += 1
        values = [si,sj,side[h],side[k]]
        mn = min(values)
        need(mn != 0, 'boundary_degenerate_edge_equilibrium',
             {'edge':[i,j], 'signs':values})
        if mn > 0:
            saddles.append([min(i,j),max(i,j)])
        elif si > 0 and sj > 0:
            rejected_by_normal_only += 1
    unstable = []
    for i in range(nv):
        need(true_degree[i] >= 3, 'true_degree_below_three', i)
        need(vminimum[i] != 0, 'boundary_degenerate_vertex_equilibrium', i)
        if vminimum[i] > 0:
            unstable.append(i)
    counts = [len(stable),len(unstable),len(saddles)]
    need(counts[0]+counts[1]-counts[2] == 2, 'mechanical_Euler_crosscheck', counts)
    report = {
        'status': 'VERIFIED_GOMBOC' if counts == [1,1,0] else 'VERIFIED_STRICT_NONWINNER',
        'class_SUH': counts, 'vertices':nv, 'triangles':nt,
        'triangulation_edges':ne_tri, 'coplanar_diagonals':flat_count,
        'true_edges':ne, 'maximal_facets':facet_count,
        'generic_ray':list(ray), 'unique_ray_triangle':ray_hits[0],
        'vertex_link_windings_all_one':True,
        'stable_facet_min_triangle_ids':stable, 'stable_boundary_cycles':stable_cycles,
        'unstable_vertex_ids':unstable, 'saddle_edges':sorted(saddles),
        'interior_feet_excluded_by_full_normal_cone':rejected_by_normal_only,
        'volume_numerator_ascending':vol, 'volume_denominator':6*D**3,
        'moment_numerators_ascending':moments, 'moment_denominator':24*D**4,
        'centroid_exact':[0,0,0], 'quadratic_ascending':[q.C,q.B,q.A],
        'root_interval':[[q.lo.numerator,q.lo.denominator],[q.hi.numerator,q.hi.denominator]],
        'exact_predicate_calls':q.calls, 'exact_radical_fallbacks':q.fallbacks,
        'exact_zero_predicate_calls':q.zeros, 'input_sha256':hashes
    }
    if require_gomboc and counts != [1,1,0]:
        raise Reject('not_Gomboc', report)
    return report


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('directory', type=Path)
    ap.add_argument('--classify', action='store_true', help='classify a strict nonwinner too')
    args = ap.parse_args()
    try:
        result = verify(args.directory, not args.classify)
    except Reject as e:
        print(json.dumps({'status':'REJECTED','gate':e.gate,'detail':e.detail}, sort_keys=True))
        return 1
    except (OSError, ValueError, KeyError, TypeError, csv.Error, EOFError, OverflowError) as e:
        print(json.dumps({'status':'REJECTED','gate':'input_or_execution_error','detail':str(e)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

### test_verifier.py

```python
#!/usr/bin/env python3
"""Literal exact fixtures and an independent small quadratic-field oracle."""
import copy
from fractions import Fraction as F
import gzip
from itertools import combinations
import json
from pathlib import Path
import tempfile
import verify_gomboc as v

ROWS10 = [(-90,0,0,10),(130,0,0,10),(0,80,30,11),(0,-80,-30,11),
          (20,30,95,13),(20,-30,-95,13),(50,80,-45,12),(50,-80,45,12),
          (-30,55,-75,14),(-30,-55,75,14)]
TRI10 = [(8,5,0),(0,9,4),(0,5,3),(4,2,0),(0,3,9),(2,8,0),(9,3,7),
         (2,6,8),(3,1,7),(1,6,2),(9,7,4),(6,5,8),(3,5,1),(4,1,2),
         (4,7,1),(6,1,5)]
ROWS9 = [(-80,60,60,10),(-80,-60,-60,10),(-80,60,-60,10),(-80,-60,60,10),
         (140,0,0,10),(30,90,10,11),(30,-90,-10,11),(20,-20,100,13),(20,20,-100,13)]
TRI9 = [(1,6,3),(0,5,2),(2,8,1),(3,7,0),(3,0,2),(3,2,1),(3,6,7),
        (5,8,2),(8,6,1),(0,7,5),(7,6,4),(4,6,8),(7,4,5),(5,4,8)]
DEGROWS = [(-80,120,60,10),(-80,-120,-60,10),(-80,0,-60,10),(-80,0,60,10),
           (140,0,0,10),(30,90,10,11),(30,-90,-10,11),(20,-20,100,13),(20,20,-100,13)]
DEGTRI = [(1,7,3),(0,8,2),(2,8,1),(3,7,0),(1,6,7),(3,0,2),(3,2,1),
          (5,8,0),(8,6,1),(0,7,5),(7,6,4),(4,6,8),(7,4,5),(5,4,8)]


def definition(A,B,C,lo,hi,D=100):
    return dict(version=1,D=D,A=A,Bc=B,C=C,root_interval=[list(lo),list(hi)],
                generic_ray=[3,11,17])


def write(folder, rows, triangles, d):
    folder.mkdir(parents=True,exist_ok=True)
    (folder/'definition.json').write_text(json.dumps(d,indent=2)+'\n',encoding='ascii')
    for name,header,data in [('vertices.csv.gz','ix,iy,iz,b',rows),
                             ('triangles.csv.gz','i,j,k',triangles)]:
        s=header+'\n'+''.join(','.join(map(str,r))+'\n' for r in data)
        (folder/name).write_bytes(gzip.compress(s.encode('ascii'),mtime=0))


def check(ok, message):
    if not ok:
        raise RuntimeError(message)


class Oracle:
    """Fraction pairs, genuine field division and rational root bisection.
    This does not call the production sign, determinant or cone routines.
    """
    def __init__(self,d):
        self.A,self.B,self.C=d['A'],d['Bc'],d['C']
        self.lo=F(*d['root_interval'][0]);self.hi=F(*d['root_interval'][1])
    def c(self,a=0,b=0):return (F(a),F(b))
    def add(self,x,y):return (x[0]+y[0],x[1]+y[1])
    def neg(self,x):return (-x[0],-x[1])
    def sub(self,x,y):return self.add(x,self.neg(y))
    def mul(self,x,y):
        z=x[1]*y[1]
        return (x[0]*y[0]-z*self.C/self.A,
                x[0]*y[1]+x[1]*y[0]-z*self.B/self.A)
    def inv(self,x):
        conjugate=(x[0]-x[1]*self.B/self.A,-x[1])
        norm=self.mul(x,conjugate)
        check(norm[1]==0 and norm[0]!=0,'oracle division by zero')
        return (conjugate[0]/norm[0],conjugate[1]/norm[0])
    def div(self,x,y):return self.mul(x,self.inv(y))
    def sign(self,x):
        a,b=x
        if b==0:return (a>0)-(a<0)
        while True:
            l,h=a+b*self.lo,a+b*self.hi
            if min(l,h)>0:return 1
            if max(l,h)<0:return -1
            m=(self.lo+self.hi)/2
            f=lambda r:self.A*r*r+self.B*r+self.C
            if f(self.lo)*f(m)<0:self.hi=m
            else:self.lo=m
    def vs(self,x,y):return tuple(self.sub(a,b) for a,b in zip(x,y))
    def scale(self,s,x):return tuple(self.mul(s,a) for a in x)
    def dot(self,x,y):
        z=self.c()
        for a,b in zip(x,y):z=self.add(z,self.mul(a,b))
        return z
    def cross(self,x,y):
        return tuple(self.sub(self.mul(x[(j+1)%3],y[(j+2)%3]),
                              self.mul(x[(j+2)%3],y[(j+1)%3])) for j in range(3))


def all_pairs_oracle(rows,triangles,d):
    o=Oracle(d);Z=o.c()
    P=[(o.c(x,-b),o.c(y),o.c(z)) for x,y,z,b in rows]
    normals=[];groups={};edge={};V=Z;M=[Z,Z,Z]
    for fi,ids in enumerate(triangles):
        a,b,c=(P[i] for i in ids)
        n=o.cross(o.vs(b,a),o.vs(c,a));h=o.dot(n,a)
        check(o.sign(h)>0,'oracle radial determinant')
        for p in P:check(o.sign(o.sub(h,o.dot(n,p)))>=0,'oracle non-global support')
        normals.append(n)
        key=tuple(o.div(s,h) for s in n)
        groups.setdefault(key,[]).append(fi)
        V=o.add(V,o.div(h,o.c(6)))
        for j in range(3):
            total=o.add(o.add(a[j],b[j]),c[j])
            M[j]=o.add(M[j],o.div(o.mul(h,total),o.c(24)))
        for j in range(3):edge[(ids[j],ids[(j+1)%3])]=fi
    check(M==[Z,Z,Z], 'oracle centroid not zero')
    G={fi:key for key,ids in groups.items() for fi in ids}
    true=[]
    for (i,j),fi in edge.items():
        gj=edge[(j,i)]
        if i<j and G[fi]!=G[gj]:true.append((i,j,fi,gj))
    S=0
    for key,ids in groups.items():
        n=normals[ids[0]];h=o.dot(n,P[triangles[ids[0]][0]])
        foot=o.scale(o.div(h,o.dot(n,n)),n)
        signs=[]
        idset=set(ids)
        for fi in ids:
            tri=triangles[fi]
            for k in range(3):
                i,j=tri[k],tri[(k+1)%3]
                if edge[(j,i)] not in idset:
                    e=o.vs(P[j],P[i]);towards=o.vs(foot,P[i])
                    signs.append(o.sign(o.dot(n,o.cross(e,towards))))
        check(min(signs)!=0,'oracle degenerate face')
        S+=(min(signs)>0)
    neighbors=[[] for _ in P]
    H=0;normal_only=0
    for i,j,fi,gj in true:
        neighbors[i].append(j);neighbors[j].append(i)
        a,b=P[i],P[j];e=o.vs(b,a)
        t=o.div(o.neg(o.dot(a,e)),o.dot(e,e))
        foot=tuple(o.add(a[k],o.mul(t,e[k])) for k in range(3))
        n1,n2=normals[fi],normals[gj]
        aa,ab,bb=o.dot(n1,n1),o.dot(n1,n2),o.dot(n2,n2)
        det=o.sub(o.mul(aa,bb),o.mul(ab,ab));check(o.sign(det)>0,'oracle Gram')
        r,s=o.dot(foot,n1),o.dot(foot,n2)
        beta1=o.div(o.sub(o.mul(r,bb),o.mul(s,ab)),det)
        beta2=o.div(o.sub(o.mul(s,aa),o.mul(r,ab)),det)
        signs=[o.sign(t),o.sign(o.sub(o.c(1),t)),o.sign(beta1),o.sign(beta2)]
        check(min(signs)!=0,'oracle degenerate edge')
        H+=(min(signs)>0)
        normal_only+=(min(signs[:2])>0 and min(signs[2:])<0)
    U=0
    for i,nb in enumerate(neighbors):
        signs=[o.sign(o.dot(P[i],o.vs(P[i],P[j]))) for j in nb]
        check(min(signs)!=0,'oracle degenerate vertex')
        U+=(min(signs)>0)
    return [S,U,H],len(true),len(groups),normal_only,V


def run(root):
    root=Path(root)
    d10=definition(7187,1827080,-2342700,(127,100),(32,25))
    d9=definition(3972,-419995,-179300,(-43,100),(-21,50))
    dg=definition(1887,-222125,-119350,(-27,50),(-53,100))
    records=[]
    for name,rows,tris,d,wanted in [('irregular10',ROWS10,TRI10,d10,[12,10,20]),
                                  ('merged9',ROWS9,TRI9,d9,[13,9,20])]:
        p=root/name;write(p,rows,tris,d)
        r=v.verify(p,False)
        oc,oe,of,on,ov=all_pairs_oracle(rows,tris,d)
        check(r['class_SUH']==oc==wanted,'class mismatch')
        check([r['true_edges'],r['maximal_facets'],r['interior_feet_excluded_by_full_normal_cone']]==[oe,of,on], 'incidence/oracle mismatch')
        check(list(ov)==[F(x,6) for x in r['volume_numerator_ascending']], 'oracle volume mismatch')
        check(r['status']=='VERIFIED_STRICT_NONWINNER','false target acceptance')
        records.append({'fixture':name,'class':oc,'oracle':'GLOBAL_ALL_PAIRS_AND_GRAM_PASS'})
        (p/'report.json').write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    def rejected(name,rows,tris,d,gate,strict=False):
        p=root/name;write(p,rows,tris,d)
        try:v.verify(p,strict)
        except v.Reject as e:
            check(e.gate==gate, name+': wrong gate '+e.gate)
            records.append({'fixture':name,'rejected_at':e.gate,'detail':e.detail})
        else:raise RuntimeError(name+': unexpectedly accepted')
    rejected('not_gomboc',ROWS10,TRI10,d10,'not_Gomboc',True)
    rejected('degenerate9',DEGROWS,DEGTRI,dg,'boundary_degenerate_edge_equilibrium')
    concave=list(ROWS9);concave[4]=(14,0,0,1)
    rejected('concave9',concave,TRI9,d9,'concave_dihedral')
    centre=ROWS9+[(-80,0,0,10)]
    subdiv=TRI9[:4]+[(3,0,9),(0,2,9),(2,1,9),(1,3,9)]+TRI9[6:]
    rejected('nonextreme_face_point',centre,subdiv,d9,'vertex_normal_rank_below_three')
    rejected('open_mesh',ROWS10,TRI10[:-1],d10,'open_mesh')
    wrong=copy.deepcopy(d10);wrong['C']+=1
    rejected('wrong_centroid_polynomial',ROWS10,TRI10,wrong,'quadratic_not_actual_x_moment')
    unisolated=copy.deepcopy(d10);unisolated['root_interval']=[[-1000,1],[1000,1]]
    rejected('two_roots_in_interval',ROWS10,TRI10,unisolated,'isolates_one_simple_root')
    ray=copy.deepcopy(d10);ray['generic_ray']=[1,0,0]
    rejected('nongeneric_ray',ROWS10,TRI10,ray,'nongeneric_ray')
    flipped=list(TRI10);a,b,c=flipped[0];flipped[0]=(a,c,b)
    rejected('inward_triangle',ROWS10,flipped,d10,'positive_radial_determinant')
    star=[(5,0,0,0),(-5,0,0,0)]+[(0,y,z,0) for y,z in
         [(5,0),(3,4),(0,5),(-3,4),(-5,0),(-3,-4),(0,-5),(3,-4)]]
    cyc=[2+(3*i)%8 for i in range(8)]
    st=[tr for i in range(8) for tr in ((0,cyc[i],cyc[(i+1)%8]),
                                       (1,cyc[(i+1)%8],cyc[i]))]
    sq=definition(1,0,-2,(1,1),(3,2),1)
    # Before testing the decisive global gate, independently verify every
    # radial determinant and every adjacent dihedral of the wrapped sphere.
    oo=Oracle(sq);pp=[tuple(oo.c(t) for t in row[:3]) for row in star]
    ee={}
    for i,j,k in st:
        needrad=oo.dot(pp[i],oo.cross(pp[j],pp[k]))
        check(oo.sign(needrad)>0,'star radial check')
        for a,b,c in ((i,j,k),(j,k,i),(k,i,j)):ee[(a,b)]=c
    for (i,j),k in ee.items():
        n=oo.cross(oo.vs(pp[j],pp[i]),oo.vs(pp[k],pp[i]))
        check(oo.sign(oo.dot(n,oo.vs(pp[ee[(j,i)]],pp[i])))<0,'star dihedral check')
    rejected('wrapped3',star,st,sq,'radial_degree_not_one')
    # Pell approximants exercise arbitrarily small nonzero signs through
    # the exact radical fallback, on both roots. Test field-zero multiples.
    plus=v.Quadratic(sq);minus=v.Quadratic(definition(1,0,-2,(-3,2),(-1,1)))
    x,y=1,0
    for k in range(1,201):
        x,y=x+2*y,x+y
        check(plus.sign((x,-y))==(-1)**k,'positive-root Pell sign')
        check(minus.sign((x,y))==(-1)**k,'negative-root Pell sign')
        check(plus.sign((-2*k,0,k))==0,'quadratic exact zero')
    check(plus.fallbacks>0 and minus.fallbacks>0,'radical fallback unexercised')
    # Nonmonic field: compare all small quadratics to independent rational
    # bisection/Fraction arithmetic, including an exact multiple of Q.
    dn=definition(3,5,-7,(0,1),(1,1));qn=v.Quadratic(dn);on=Oracle(dn)
    for a in range(-4,5):
        for b in range(-4,5):
            for c in range(-4,5):
                pair=on.add(on.c(a,b),on.mul(on.c(c),on.mul(on.c(0,1),on.c(0,1))))
                check(qn.sign((a,b,c))==on.sign(pair),'nonmonic sign disagreement')
    check(qn.sign((-7,5,3))==0,'nonmonic exact zero')
    records.append({'arithmetic':'PELL_BOTH_ROOTS_AND_729_NONMONIC_POLYNOMIALS_PASS',
                    'pell_radical_fallbacks':[plus.fallbacks,minus.fallbacks]})
    (root/'test_results.json').write_text(json.dumps(records,sort_keys=True,indent=2)+'\n')
    print('TWO_LITERAL_CENTRED_FIXTURES_GLOBAL_ALL_PAIRS_AND_GRAM_PASS')
    print('TEN_EXPECTED_REJECTIONS_PASS')
    print('EXACT_QUADRATIC_SIGN_TESTS_PASS')
    print('ALL_SMALL_EXACT_TESTS_PASS')
    return records


if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--fixtures',type=Path)
    args=ap.parse_args()
    if args.fixtures:
        run(args.fixtures)
    else:
        with tempfile.TemporaryDirectory() as d:run(d)
```

## 10. Frozen artifacts and completed clean replay

Portable verifier, literal fixtures, proofs, manifest and runner (`portable_quadratic_verifier.zip`)

Standalone production verifier (`verify_gomboc.py`)

Standalone fixture generator and independent oracle (`test_verifier.py`)

Complete handoff with both sources inline (`portable_quadratic_verifier_HANDOFF.md`)

Machine-readable version-2 handoff (`portable_quadratic_verifier_result.json`)

Actual clean-extraction replay transcript (`portable_quadratic_verifier_replay.txt`)

The archive contains 46 files, including a 45-file SHA-256 manifest. Its size is 35,876 bytes and SHA-256 is `1463c4692ab4458c2478641156f82de24612b922d083c4014097482d2db9093f`. The exact production source above has SHA-256 `91628f5d51ef956ccf55f80eec765501184023a55842e0af14bcae137237ac78`; the exact test source has SHA-256 `a3e5623971c21e31dd23eabb25ff5fc0482e65e206f201fc4867625afa67e6e5`.

From a fresh extraction, `python -B RUN_ALL.py` checked every frozen hash, executed the complete small-fixture suite in a temporary directory, then checked every frozen hash again. The completed transcript is:


[Encoded source block omitted; the code in this passage is incomplete.]


The fixture suite also passed under `python -O`, so disabling assertions does not disable an acceptance gate. The two sources embedded in this handoff were extracted, hash-compared with the packaged scripts, and replayed together separately. All continuation-critical arithmetic, global checks, feature predicates and fixture coordinates are in the immutable text itself.

The next acceptance step is to run default Gömböc mode on the lead's **new literal input files**, preserving their resulting hashes and full report. A failed convexity, extremality, mass or equilibrium check must be repaired in the input and rerun; it is not a reason to waive that check. No verification claim about the missing old large table, and no successful large-table run, is made here.
