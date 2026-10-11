# Universal base-vertex lemma and the half-roundness obstruction

This is a mathematical result for homogeneous filled three-dimensional pyramids. It is not an assertion of historical novelty, not an exclusion of all pyramids, and not a new own110 construction.

Let B be a full-dimensional convex polygon in z=0 with its area centroid at 0. Let A=(a,h), where a is a planar vector and h>0. Reflection handles h<0. The pyramid P=conv(B,A) has volume centroid g=(a/4,h/4): at relative height t its section is (1-t)B+ta and its area scales by (1-t)^2, giving mean t=1/4. Every equilibrium below is relative to this actual filled-volume centroid.

## A base vertex is always strictly unstable

For any vertex b of B, a triangle fan anchored at b partitions B into triangles (b,c_i,d_i), with nonnegative area weights w_i summing to 1. Ignore the zero-area boundary triangles. The area-centroid identity gives 3*0=b+sum_i w_i(c_i+d_i). Therefore -b/2=sum_i w_i(c_i+d_i)/2 belongs to B.

Choose a base vertex b maximizing |b-a/4| over B. Such a vertex exists because B is a finite convex hull and norm squared is convex. Comparing it with -b/2 gives

    |b-a/4|^2-|-b/2-a/4|^2 = (3/4)(|b|^2-a.b) >= 0.

Thus b.(a-b)<=0. Put v=(b-a/4,-h/4), u=(3a/4,3h/4). For any different base vertex v',

    2 v.(v'-v) = |v'|^2-|v|^2-|v'-v|^2 < 0.

For the apex,

    4 v.(u-v) = 5 a.b-4|b|^2-|a|^2-h^2
                = 3 b.(a-b)-|a-b|^2-h^2 < 0.

The radial support plane at v strictly separates every other vertex. Hence v is a strictly unstable base vertex. The apex can never be the unique unstable vertex of a homogeneous filled pyramid.

## Necessary apex balls for own110 with no extra weak equilibria

Since a strict base unstable vertex already exists, the apex must have a positive escape toward a base vertex b. Otherwise it is another strict unstable vertex, or a weak-only vertex equilibrium. Its escape condition is

    a.b > |a|^2+h^2,

which is equivalent to

    |a-b/2|^2+h^2 < |b|^2/4.

Thus the apex belongs to the union of open three-dimensional balls with diameters [0,b], where b ranges over base vertices. In particular, if |b|<=Q for all b, then h<Q/2. A vertex capable of witnessing this escape necessarily has |b|>2h. The balls are necessary, not sufficient, for own110.

## Low height gives two strictly stable facets

Suppose B contains the closed centred disk of radius R>0. The section of P-g in the plane through 0 parallel to B is (3/4)B. Consequently the support function s on the unit sphere satisfies s>=3R/4 on the equator. The lower-pole value is h/4 and the upper-pole value is 3h/4.

If 0<h<=R, the lower pole lies strictly below all equatorial values. The upper pole exposes only the apex. Choose a unit tangent direction d with a.d<=0. For a sufficiently small positive angle, the apex remains uniquely exposed and

    s = (3h/4) cos(theta) + (3a.d/4) sin(theta) < 3h/4 <= 3R/4.

So each closed hemisphere attains a minimum in its interior. The minima lie in disjoint open hemispheres.

A local minimum of the support function of a full-dimensional polytope containing 0 in its interior must correspond to a facet with relative-interior perpendicular foot. Indeed, if its exposed face has dimension 0 or 1, take a nonzero tangent direction perpendicular to all affine differences of that face, choosing its sign so the common derivative beta<=0. While inactive vertices remain inactive, a small spherical rotation changes the support to s*cos(theta)+beta*sin(theta)<s, a contradiction. If the exposed face is a facet but the perpendicular foot is not in its relative interior, tangent separation gives d with max_{x in facet} x.d<=0; the same strict decrease again contradicts a local minimum. Therefore the two hemisphere minima are two distinct strictly stable facet equilibria, not merely weak contacts.

Thus monostability requires h>R, including strict exclusion of h=R.

## Half-roundness theorem

If B contains the centred radius-R disk and lies in the centred radius-Q disk, with 2R>=Q, every nondegenerate homogeneous pyramid on B has at least two strictly stable equilibria or at least two strictly unstable equilibria.

For h<=R use the low-height result. For h>R>=Q/2, every base vertex satisfies

    a.b-|a|^2-h^2 <= Q|a|-|a|^2-h^2 <= Q^2/4-h^2 < 0.

Hence the apex is strictly unstable, as is the base vertex proved above. The theorem excludes strict own110 even without requiring weak000. It strictly strengthens the earlier sufficient ratio R/Q>=13/20 to R/Q>=1/2.

Any possible own110/weak000 pyramid must therefore have R<h<Q/2 and its apex in one of the above open diameter balls. The base must possess vertices with |b|>2R. This does not prove that every pyramid is excluded.

## Quantified base-deformation exclusions

Let B and B' both be translated by their own area centroids, viewed in a common Euclidean plane. If their Hausdorff distance is at most delta, support-function comparison implies that B' contains the centred radius-(R-delta) disk and is contained in the centred radius-(Q+delta) disk. Thus every apex on B' is excluded whenever 0<=delta<R and 3delta<=2R-Q. This is a bound for area-centred bases; no bound on centroid displacement under uncentred perturbations is being silently assumed.

For a nonsingular planar linear map T, the transformed base contains radius sigma_min(T) R and lies within radius sigma_max(T) Q; the area centroid transforms linearly. Every apex on T(B) is excluded if the singular-value condition number is at most 2R/Q. The same applies to the restriction of a three-dimensional affine map to the base plane after an isometry; the apex is arbitrary.

Exact applications checked by half_round_certificate.py:

* C80_BASE20: R=66612792, Q=100852489; all area-centred base perturbations of Hausdorff distance <=32373095/3 are excluded for every apex. Base-map condition number <=133225584/100852489 is excluded.
* C96_BASE24: R=58972, Q=78849; Hausdorff radius <=39095/3; base-map condition number <=117944/78849.

The script includes every source coordinate, recomputes Euclidean distances in the true base plane, proves area-centroid and fan identities with rational arithmetic, and verifies both bounds. The C96 base is obtained from the literal C138 point list excluding index15 via Y=137p-(n.p)n, n=(4,11,0); no non-isometric 2D radius approximation is used.
