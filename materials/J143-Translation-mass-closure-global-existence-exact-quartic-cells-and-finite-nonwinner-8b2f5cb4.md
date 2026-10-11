# material-8b2f5cb49707

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J143 — translating a whole subbody: global mass closure and exact finite cells

## Status and source boundary

The goal remains a homogeneous own strict110/additionalweak000 polyhedron with true E<=249. No such body was obtained. Canonical V176/E311/F137,C622 remains unchanged. This coordinator's new results are: a global existence theorem for uniform-mass closure by translating one subbody; an exact quartic reduction on each finite translation cell; and an executed algebraic, exactly centered NONWINNER with V43/E123/F82,C246, strict(S,U,H)=(26,25,49), additionalweak000.

The literal computational parent is figure-0622, fully read from cursor0 through EOF with SHA256 f63d80e0ada03ac98308d1bd82ccb12165bfc671f6f98a9f940ef747fa5d511e. Its selected exact object is QW49J_LOW62_G9, not another LOW43 or a relabelled audit. Its2182-byte input has SHA256 90cc88f1a89396ed5cbe20e84cb4fc8265ae1b4170cc2d5bf245c024d4c4662e. The RAW unstable roots are9 and45; original audit roots9 and46 are different labels. This work uses the RAW rows.

The preceding BASIN142 archive [internal-source-reference] was read completely. Its first-order14-variable exclusions omit relative translation and do not exclude finite nonlinear motion. They were treated as author-reported working premises, not independently replayed here. The new results below have separate proofs and computations. Read/store transport receipts do not constitute mathematical verification.

## 1. A global centering translation always exists

Let A,B be nonempty compact convex subsets of R^d, with A full-dimensional, and define K_t=conv(A union(B+t)). The density is uniform on the entire NEW convex hull, not a transported density on two overlapping pieces. Let g(t) be its actual volume centroid. Put R=max{|x|:x in A union B}. There is at least one t with g(t)=0, and every such t satisfies |t|<=(d+1)R. No uniqueness is claimed.

Proof. For any full-dimensional convex body K and any unit n, set m=min_K n.x and M=max_K n.x. Then n.g(K)>=(M+d*m)/(d+1). For a polytope, choose an apex attaining M and decompose K into simplices from that apex to triangulated opposite boundary facets. Every simplex centroid has projection at least(M+d*m)/(d+1), hence so does their positive volume-weighted mean. General compact convex bodies follow by Hausdorff approximation, though only polytopes are needed here.

For t=T*n, every point of A has projection at least-R; every point of B+t has projection at least T-R; and K_t has a point with projection at least T-R. Consequently n.g(t)>=T/(d+1)-R. In particular g(t) points strictly outward on every sphere |t|=T>(d+1)R. The centroid depends continuously on t because convex hulls depend continuously in Hausdorff distance and contain the fixed positive-volume A. If g had no zero in that closed ball, the continuous map F(t)=-T*g(t)/|g(t)| from the ball to itself would have a Brouwer fixed point. That point lies on the boundary and has t.g(t)<0, contradicting the outward inequality. The same inequality excludes any zero with |t|>(d+1)R.

For d=3 this gives a finite radius4R containing ALL centering translations. It is a mass-existence statement, not an equilibrium-preservation theorem. Plateaus/multiple translations are possible, for example when a translated B stays inside a fixed centered A. A lower-dimensional B is permitted. The full-dimensional A hypothesis is a convenient sufficient condition for nonvanishing volume and continuity throughout the ball; it is not claimed necessary.

This removes one possible misunderstanding of numerical root failures: a finite solver failure does not show that centering is impossible in this family. Conversely, finding a centering translation does not preserve either the primal or polar equilibrium landscape.

## 2. Internal chords and root exits under translation

At desired center0, let the moving group be Y_i=s*O*R_i+t with s>0 and O orthogonal. For i,j in that group,

Y_i.(Y_j-Y_i)=s^2*R_i.(R_j-R_i)+s*(O^T*t).(R_j-R_i).

Thus preservation of any chosen positive internal chord forest is a finite set of LINEAR inequalities in t, once s,O are fixed. A fixed A-point a has an outgoing chord to a moving point b+t exactly when a.(b+t-a)>0, also a halfspace condition. The reverse exit from b+t to a is

|t+b-a/2|^2<|a|^2/4.

This is a diameter-ball condition, not a free mass correction. These conditions concern mechanics relative to0 and become actual own-centroid conditions only at a genuine uniform-mass closure. They prevent subsidiary U only when the complete required forest remains valid; they do not guarantee S1.

## 3. Translation hull cells are polyhedral

Fix submitted points r_i in R^3 and binary flags b_i in{0,1}; write p_i(t)=r_i+b_i*t. Any oriented four-point affine determinant is affine in t. Expanding the determinant of three differences, every term of degree at least two has two proportional copies of t and vanishes. Therefore the oriented-matroid sign regions, and in particular chambers on which a nominated convex-hull boundary remains valid, are intersections of affine halfspaces in t. Degenerate boundaries require their own lower-dimensional treatment.

For an oriented boundary triangle f=(a,b,c), put k_f=b_a+b_b+b_c and S_f=r_a+r_b+r_c. Its origin determinant has the form

d_f(t)=det(p_a(t),p_b(t),p_c(t))=d_f0+ell_f.t.

The same repeated-column argument makes this affine even when the origin is outside K. On a complete consistently outward boundary shell, the signed tetrahedral formulas still give actual filled volume and first moment:

V(t)=sum_f d_f(t)/6=V0+v.t,

M(t)=sum_f d_f(t)*(S_f+k_f*t)/24=m+L*t+t*(c.t),

where

V0=sum d_f0/6;
v=sum ell_f/6;
m=sum d_f0*S_f/24;
L=sum(S_f*ell_f^T+k_f*d_f0*I)/24;
c=sum k_f*ell_f/24.

These are FINITE polynomial identities on the actual hull cell, not first-order approximations. The linear matrix L need not be symmetric. Centering at an arbitrary fixed g0 instead of0 means solving M(t)-g0*V(t)=0; only m and L change, and the same special quadratic form survives. There is no assertion that a frozen shell remains the physical hull after crossing one of its affine support walls.

## 4. Exact quartic reduction of mass closure

Set lambda=c.t. On the regular locus det(L+lambda*I)!=0, the equation M(t)=0 gives

t=-(L+lambda*I)^(-1)*m,

q(lambda)=lambda*det(L+lambda*I)+c^T*adj(L+lambda*I)*m=0.

The latter is a monic degree-four polynomial. Conversely a real root with nonzero determinant defines a solution of the original mass equation: the quartic identity gives c.t=lambda, so(L+lambda*I)t=-m is exactly M(t)=0. Each candidate must still satisfy the correct translation-cell inequalities and V(t)>0. A root at a zero of det(L+lambda*I) cannot be accepted by this inverse formula; singular solutions require solving the original system together with c.t=lambda. No exhaustion of singular cases or all translation cells was executed here.

This turns regular within-cell mass closure into exact univariate root isolation followed by rational/algebraic sign tests. The global4R bound makes an eventual all-cell analysis bounded, but no complete global cell enumeration is claimed.

For supporting triangle normals, n_f(t) and h_f(t)=n_f(t).p_a(t) are affine. At positive heights the polar vertex is q_f=n_f/h_f. The numerator of a positive polar chord is

h_i*n_i.n_j-h_j*|n_i|^2,

over positive denominator h_i^2*h_j; it has degree at most three in t. Primal chords have degree at most two, and same-group primal chords are affine. Thus finite mass, incidence and both landscapes can be tested in one exact low-degree cell without independently choosing incompatible physical and polar metrics.

## 5. Executed finite20-percent change and its exact NONWINNER

Take the62 rational RAW parent points, subtract the parent's exact homogeneous centroid, and use

A=[0,1,2,4,6,7,9,12,13,14,16,17,19,26,27,29,31,33,36,38,40,59,60,61],

with B the38-point complement. Keep A unchanged and multiply B by6/5. Translate B by t0+delta, with the frozen rational anchor

t0=(-50755961281/500000000000,-415797819/6250000000,-141890391561/1000000000000).

The complete82 oriented triangles and this anchor are the1017-byte TRANSLATION143_EXACT_RECIPE.json. A numerical mass solve nominated them; subsequent exact claims use only the frozen rational recipe, literal parent and exact arithmetic.

The exact checker verifies5084 supporting inequalities, all62 points against all82 triangles; checks that each plane's zero set is EXACTLY its three triangle vertices; checks all oriented edge cancellations and Euler; and derives the full affine-volume/quadratic-moment chart. The true maximal lattice is V43/E123/F82, not a triangulation count of larger polygons. Its certified translation-cell L-infinity radius is approximately .006568882106346947. Seven nonzero rational translations inside that radius also directly reproduce the finite volume/moment identities; these are supplementary executed checks, not the analytic proof.

The quartic has exactly one real root in[-1/10^8,1/10^8] by exact Sturm counting. Exact interval arithmetic excludes a singular denominator and bounds the reconstructed delta by approximately

[-3.70155047377005e-14,-3.7015501089157374e-14],
[-1.1715413474563667e-13,-1.1715412529165702e-13],
[3.743726842693806e-13,3.7437271342391616e-13].

The interval lies strictly in the certified physical hull cell and gives positive filled volume. The ACTUAL first moment is exactly0 by the quartic identity, not because a floating residual is small. The resulting construction is an algebraic polyhedron specified by a unique isolated root, not a newly rational-coordinate body.

An exact rational-interval census on that isolated algebraic root classifies every active vertex, every maximal facet and every true edge. Global positive chords exclude non-U/non-S features; strictly negative chords certify strict U/S. Edge-foot and two-normal cone coefficients classify strict H or a strict exclusion. No feature remains ambiguous. The complete outcome is(S,U,H)=(26,25,49), additionalweak000, with26+25-49=2. This proves that this finite exact mass repair fragments both landscapes; it does NOT give110, preserve LOW or exclude other finite translated shapes. Complete positive persistence bars were not computed exactly for this algebraic example, and no P/Q list is asserted.

## 6. Recovery and verification boundary

The companion complete exact recovery capsule contains input143.py, exact_translation143.py, quartic_census143.py and TRANSLATION143_EXACT_RECIPE.json. No originating sandbox or numerical optimizer is needed for its replay. The exact replay uses CPython3.13.5 and SymPy1.14.0, with assertions enabled. Commands:

python input143.py
python exact_translation143.py --replay
python quartic_census143.py

The final executed source adds explicit maximal-triangle zero-set assertions and makes numerical nomination imports lazy; those packaging/check additions do not change either output below. They were executed before preservation. This is one coordinator's exact method, not an independently developed second verifier.

Expected and observed outputs:

QW49J_LOW62_G9_INPUT.json:2182B, SHA256 90cc88f1a89396ed5cbe20e84cb4fc8265ae1b4170cc2d5bf245c024d4c4662e.
TRANSLATION143_EXACT_CHART.json:9554B, SHA256 b8b1fb689110989f75e970b465bc95c7b7b6b06dc6e85acd59f47e43da6651f7.
TRANSLATION143_QUARTIC_CENSUS.json:2039676B, SHA256 19eefb0ed2297772a0f8485e3bf246274531b848123c7092475ccb342e9661d4.

Observed terminal markers:
TRANSLATION143_EXACT_FINITE_MASS_QUARTIC_CELL_PASS 43 123 82 5084
TRANSLATION143_EXACT_QUARTIC_OWN_CENSUS_PASS {'S':26,'U':25,'H':49} additionalweak000

The larger census is reproducible from the complete compact generator and frozen input; its hash alone would not be recovery data. This proof document must be paired with that source capsule before a descendant computational use.

## 7. Consequence for the next construction

The missing relative translation is now a genuinely finite mass mechanism, not just three extra tangent directions. Yet it is not free equilibrium capacity: the executed20-percent subbody scaling has exact mass closure but25 U and26 S. The constructive question is to select or change the whole-basin geometry so that a quartic mass root lies simultaneously inside its actual support cell and the complete strict primal/polar guard region. Cell changes, alternate moving subsets and actual stable-carrier replacement remain open. No repeated small-descent failure or finite sampling here excludes that broader problem.
