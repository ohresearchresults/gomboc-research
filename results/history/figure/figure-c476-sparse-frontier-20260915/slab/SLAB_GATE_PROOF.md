# A central-section/slab obstruction to monostability

## Statement
Let K be a full-dimensional convex polytope and let c be in its interior.
Let e be a unit vector. Suppose the central disk

D = {c+x : e.x=0, ||x|| <= R}

is contained in K, while every x in K satisfies |e.(x-c)| <= h,
where 0<h<R. Then K has at least two distinct strict stable facet equilibria
relative to c, one in each open hemisphere e.(x-c)>0 and <0.
No density assumption is needed for the theorem itself. To apply it to a
homogeneous solid, c must be that solid's actual uniformly filled volume centroid.

## Proof
Translate c to zero. Since zero is interior, the radial function rho(u)>0 of K
is continuous on the unit sphere. On the equator e.u=0 it is at least R.
On the two poles it is at most h<R. Therefore rho achieves a minimum strictly
inside each of the two closed hemispheres. The corresponding boundary points
are local minima of Euclidean distance to the origin and are distinct.

A local minimum of boundary distance for a convex polytope about an interior
origin lies in the relative interior of a maximal facet, with radial direction
parallel to that facet's outward normal. Here is a proof also covering possible
combinatorial degeneracies. Let p be such a minimum, r=||p||. For each maximal
support plane a.x<=b active at p, b=a.p>0. If a is not a positive multiple of p,
put v=a-(a.p)p/r^2, so p.v=0 and a.v=||v||^2>0. For sufficiently small eps>0,
x=p+eps v-C eps^2 p with any fixed C>||v||^2/(2r^2) has ||x||<r and a.x>b.
Thus x is outside K while tending to p. The segment from zero to x intersects
the boundary at y=lambda x, 0<lambda<1. By continuity of the radial function,
y tends to p as eps tends to zero, while ||y||<r. This contradicts local
minimality. Consequently every active support normal is parallel to p.
Distinct maximal facets cannot have parallel active planes at the same point,
so p is in the relative interior of a unique maximal facet. Its orthogonal foot
is p. Squared distance on that facet has a positive definite tangential Hessian,
so it is a strict stable facet equilibrium. Apply this to the two hemisphere
minimizers to obtain the claim.

## Rational certificate for the exact C476 body
The exact body is COORD_C476_AFFINE_DELETE42_63_83_OWN222, not an approximation,
not the original untransformed BEFORE body, and not any C486 algebraic body.
Its complete reconstruction and independent audits are in its separate journal
capsule. This gate reads its exact own-volume centroid and raw H table, pinned
by full SHA256. Choose

n=(19,-98,-8), n.n=10029, e=n/sqrt(10029), R=1/3, h=1/12.

For each exact raw vertex v it checks

h^2 (n.n) - [n.(v-c)]^2 > 0.

By convexity these vertex inequalities prove the slab inclusion for the whole
solid. For each maximal raw support a.x<=b, let d=b-a.c>0. The maximum of a.x
on the radius-R central disk through c is a.c+R||proj_(n perpendicular) a||.
The exact strict inequality

(n.n)d^2 - R^2[(n.n)(a.a)-(a.n)^2] > 0

therefore proves that disk lies strictly inside every support inequality.
The projection norm can be zero without difficulty. Together the checks certify
the theorem's hypotheses about the exact actual filled centroid. The executable
also proves a convenient explicit lower bound 34 for the squared vertex slab
margins and 6/25 for each squared disk margin divided by (n.n)d^2. All these
comparisons use arbitrary-precision rationals, not numerical singular vectors.

The disk-to-half-slab ratio is 4. Thus this is a robust geometric obstruction,
not an equality or zero-margin event. Any proposed successor still satisfying
these two inclusions about its OWN actual centre necessarily remains at least
bistable regardless of its new incidence, number of edges, or mass distribution.
The theorem does not claim that all coordinate changes or projective/affine
changes preserve the inclusions. Escaping one of them is necessary, not sufficient,
for a mono-monostatic successor. It imposes no global bound on C.

## Execution
Python3.13.5 standard library only, assertions enabled:

python -B -S slab_stability_gate.py C476_A.json C476_raw.json OUT.json

Observed terminal: EXACT_C476_SLAB_FORCES_TWO_STABLE_PASS.
All115 vertex and125 maximal support tests completed. The ordinary full own-centre
census222/weak000 is provided independently by both full hull/mechanics auditors;
it is not inferred by treating this two-stable lower bound as an exact census.
