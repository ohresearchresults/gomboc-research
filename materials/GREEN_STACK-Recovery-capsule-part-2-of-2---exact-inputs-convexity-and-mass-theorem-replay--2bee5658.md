# material-2bee5658963e

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# GREEN_STACK: finite homothetic-section construction, exact own mass, C2 critical patches

This is recovery capsule part 2 of 2. Part 1 is the complete 12865-byte `green_exact.py`, SHA-256 `a5134097f1d329d737884d9feea494e14356c233c84f527ab608e9ef78709a5f`, material `[internal-source-reference]`. Together the two parts are self-contained. No earlier research result, optimizer, browser, numerical hull, checkpoint or originating sandbox is needed to reconstruct either exact body below. Both bodies are useful NONWINNERS, not strict110 constructions. The C472 control meets the edge budget but is strict356; the small arithmetic control is C40 strict558. Neither changes the canonical C622 own110 construction or solves the present C<500 target.

## 1. Finite sections and the actual uniform centroid
Let K be a full-dimensional convex polygon in R2 with positive area A and area centroid zero. At ordered axial nodes x_0<...<x_N, choose section centres d_i in R2 and scales r_i, with r_0=r_N=0 and all interior r_i>0. Interpolate d and r linearly on each interval. Consider the solid whose slice at x is d(x)+r(x)K. For each facet inequality u_j dot z<=h_j of K, its support profile is b_j(x)=u_j dot d(x)+h_j r(x). The solid is convex exactly when each b_j is concave. Necessity follows by taking convex combinations of maximizers of u_j in two slices. Sufficiency follows from the intersection of the inequalities u_j dot z<=b_j(x), since the hypograph of each concave b_j is convex.

The finite volume and first moments are not inherited from any smooth parent. On an interval of length Delta with endpoint radii a,b, the integral of r^2 is Delta(a^2+ab+b^2)/3. Since the section centroid is d(x), each first moment is the integral of the piecewise-linear coordinate times r^2. The exact endpoint coefficients are

    w_left  = Delta(3a^2+2ab+b^2)/12,
    w_right = Delta(a^2+2ab+3b^2)/12.

Accumulate these contributions into node weights w_i. Then volume=A sum_i w_i and actual centroid=sum_i w_i (x_i,d_i)/sum_i w_i. All weights are nonnegative, and each interior weight is positive. At fixed nodes and radii, the first moment is LINEAR in the section centres; translating to this computed centroid is exact own-mass centring, not placement of an arbitrary reference point. Applying positive transverse scale beta multiplies area by beta and the corresponding centroid coordinate by beta. An axial scale lambda is included in the physical x_i, hence in the interval lengths. This gives a finite mass-control chart without adding edges.

## 2. Green-kernel convexity chart
On [-1,1], define

    g(x,t)=(1-|x-t|-x*t)/2
          =(x+1)(1-t)/2 for x<=t,
          =(t+1)(1-x)/2 for x>=t.

For distinct interior knots t_j, choose a_j>0 and k_j in K, and set

    r(x)=sum_j a_j g(x,t_j),
    d(x)=d_affine(x)-sum_j a_j k_j g(x,t_j).

At knot t_j, the jump of r' is -a_j and the jump of d' is a_j k_j. Therefore the support-profile slope jump is

    a_j (u_l dot k_j - h_l) <= 0

for every facet l of K. This proves convexity for every choice in the chart, rather than imposing a numerical convexity penalty. The endpoint scales vanish and all interior scales are positive. Positive common normalization of r,d, positive axial/transverse scales and affine centre drifts preserve this conclusion.

Conversely, in a PL homothetic-section family with strictly negative radius slope jumps, set a_j=-jump(r') and k_j=jump(d')/a_j. Convexity is equivalent to k_j in K. If a radius slope jump is zero, convexity forces the centre slope jump to vanish, since a bounded polygon's facet normals positively span the plane. The chart is thus a useful exact parameterization of this family, NOT a parameterization of all convex polyhedra and NOT an exclusion of other architectures.

## 3. Complete support-plane representation
A concave PL b_l is the minimum of the affine extensions of its segment pieces. On [-1,1], all resulting support planes therefore cut out exactly the intended slices d(x)+r(x)K. There are no hidden additional facets inside the axial range. Outside the axial range, the first or last segment inequalities would describe a negative multiple of K after translation: the first radius slope is positive and the last negative. Such inequalities are infeasible, because a positive balanced combination of the polygon normals gives zero on the left and a negative combination of the positive offsets on the right. This proves boundedness and completeness of the H-description, including the tips.

The verifier reconstructs each support plane with rational arithmetic, merges proportional coplanar planes exactly, checks every input vertex against every plane, computes each maximal face by a rational planar monotone-chain hull, deletes collinear nonvertices, requires every listed vertex to be extreme in a face, checks two oppositely oriented owners for every true edge and V-E+F=2. These checks supplement the support-completeness theorem. They are NOT claimed to be two independent generic 3D hull programs.

## 4. A C2 architecture with a strict S and U guaranteed for every member
Use the exact triangle

    K=[(1,0),(-1/2,1),(-1/2,-1)], area=3/2, area centroid=(0,0).

Let there be m=2k+1 interior rings with symmetric axial knots. Make a_j even under axial reflection, k_{j,u} even and k_{j,v} odd. Set the central curvature point to k_0=(-1/2,0), in the relative interior of K's west edge. Require every other k_j strictly inside K. Allow any odd affine transverse drift alpha*x and positive axial/transverse scales lambda,beta. The resulting body has the half-turn symmetry

    (x,u,v) -> (-x,u,-v).

Its actual filled centroid lies on the u axis. The west support profile -d_u+r/2 is even and concave, with a zero central slope jump and strictly negative jumps elsewhere. Its two central pieces have equal and opposite slopes, hence both slopes zero. They merge into one west hexagonal maximal facet. The point of that facet on the symmetry axis is in its relative interior, so the orthogonal projection of the actual centroid is a strict stable equilibrium.

The east support coordinate d_u+r has strictly negative slope jumps at every interior knot, including the central knot since k_{0,u}-1=-3/2. It is even, hence has its unique maximum at the central east vertex. Every other vertex has strictly smaller u coordinate. The actual centroid has u coordinate strictly below this maximum. Therefore the central east radius has strictly negative dot product with every outgoing true edge: this is a strict unstable equilibrium. No assumption that this vertex has the largest Euclidean radius is needed for this local statement.

The theorem guarantees AT LEAST one strict S and one strict U, not uniqueness. Every other equilibrium is paired by the half-turn: the axis has only the two stated boundary points. Thus generic additional-weak-free members have odd S and U and even H. This parity is not a target proof.

For m=2k+1, before merging the central west pair there are V=3m+2, E=3(2m+1), F=3(m+1). The single merger deletes one edge and one face. Therefore the exact maximal counts are

    V=6k+5, E=12k+8, F=6k+5, C=24k+16.

There are six triangular tip faces, 6k-2 quadrilateral faces, and one hexagonal face. Strictly interior noncentral k_j prevent other mergers. At k=19 this gives V119/E236/F119,C472; at k=1 it gives V11/E20/F11,C40. The exact verifier reconstructs rather than assumes these counts.

## 5. Exact object definitions
The generator fixes rational t_i=(19/20)(i-k)/k for i=0,...,2k and uses axial knot x_i=2t_i/(1+t_i^2), together with endpoints -1,+1. `curvatures` supplies a_0,...,a_k for central and positive knots; the negative side is mirrored. Each positive_barycentric row is normalized by its exact sum and combined with the three listed K vertices. Negative knots reflect the v coordinate. The central k_0 is fixed as above. Finally r(0) is normalized to one; lambda, beta and alpha are applied as in the complete source. All JSON fractions are [numerator,denominator]. The checkpoint-name field in the large input is provenance only: reconstruction never opens it.

Save each following code block under its indicated filename as UTF-8 with LF and one trailing newline, without the Markdown fence.

### GREEN_TRI_C40_RATIONAL_CONTROL_INPUT.json
```json
{"alpha":[1,5],"beta":[5,6],"curvatures":[[1,1],[2,1]],"identity":"GREEN_TRI_C40_RATIONAL_CONTROL","k":1,"lambda":[13,14],"positive_barycentric":[[[1,1],[2,1],[3,1]]]}
```
168 bytes, SHA-256 `bb29c7c5ca76a8a878ed5cc086dcdc8de02ad1834941a08135cfa14f82ca08a4`.

### GREEN_TRI_C472_MAX_G9_INPUT.json
```json
{"alpha":[-393062283,1000000000],"beta":[218764871,250000000],"curvatures":[[110281,100000000],[294739,500000000],[1079541,1000000000],[150467,125000000],[352997,250000000],[45051,25000000],[646097,500000000],[3543297,1000000000],[286237,250000000],[146091,1000000000],[840223,500000000],[740549,500000000],[5121,8000000],[4257957,1000000000],[1576047,200000000],[1176211,62500000],[19166927,1000000000],[33203861,1000000000],[205027801,1000000000],[1,1]],"freeze_denominator":1000000000,"identity":"GREEN_TRI_C472_MAX_G9","k":19,"lambda":[101746673,125000000],"positive_barycentric":[[[388103,3906250],[900508779,1000000000],[136853,1000000000]],[[41481,250000000],[17881,500000000],[499899157,500000000]],[[31591,200000000],[42203,1000000000],[499899921,500000000]],[[39833,200000000],[6973,125000000],[999745051,1000000000]],[[121921,250000000],[123159,1000000000],[999389157,1000000000]],[[5075699,1000000000],[1442249,1000000000],[993482051,1000000000]],[[23345207,250000000],[905011541,1000000000],[1607631,1000000000]],[[39981,200000000],[499821787,500000000],[156521,1000000000]],[[604037,1000000000],[199811981,200000000],[336059,1000000000]],[[14321719,50000000],[128549,500000000],[356654261,500000000]],[[991757127,1000000000],[115361,1000000000],[8127513,1000000000]],[[974126397,1000000000],[1116343,1000000000],[1237863,50000000]],[[6203243,1000000000],[2541467,1000000000],[99125529,100000000]],[[3502453,1000000000],[3751317,200000000],[488870481,500000000]],[[116587,12500000],[75926709,1000000000],[914746331,1000000000]],[[649837581,1000000000],[159451027,1000000000],[5959731,31250000]],[[54171399,125000000],[18920009,62500000],[32988583,125000000]],[[64069889,250000000],[45122783,100000000],[146246307,500000000]],[[121867153,500000000],[459692621,1000000000],[296573073,1000000000]]],"source_checkpoint":"metric_3_19_max.json"}
```
1853 bytes, SHA-256 `9f00de5d6efad1be2e5366dc65be1fc699f02529d8712e7570320b3a8fb4a816`.

## 6. Reconstruction, verification and exact receipts
Python 3.13.5 was used. The exact recovery uses only Python's standard library and does not require NumPy/SciPy/Torch. Execute in the directory containing the complete part-1 source saved as green_exact.py and the two exact input JSON files:

```sh
python -B -S green_exact.py GREEN_TRI_C40_RATIONAL_CONTROL_INPUT.json
python -B -S green_exact.py GREEN_TRI_C472_MAX_G9_INPUT.json
```

Each command reconstructs the entire maximal complex, calculates actual volume and centroid by the slab formula, checks it against two tetrahedral decompositions with different interior origins, and checks three separate directional divergence volume/first-moment formulas. The output lists every centred rational vertex, every maximal supporting plane, every face cycle, every true edge and its two owners. The full mechanical audit checks all physical strict/weak vertex conditions, polar strict/weak conditions at the SAME actual centre, a separate direct face-foot membership criterion, and every mixed saddle condition (strict interior of true edge and strict interior of the cone of its two adjacent outward normals). It also records all primitive zero arrows and edge equalities. The Morse count is an additional consistency check, not the proof of the census.

The exact physical P and same-centre polar Q superlevel landscapes use minimum squared norm on true chords. For A=a.a,B=a.b,C=b.b the chord minimum is A if B>=A, C if B>=C, and (AC-B^2)/(A+C-2B) otherwise. Equal event levels are batched before elder selection. Every strictly positive exact bar is retained, including tiny births. The output gives every dying component, complete boundary cut, attaining path, and exact death-attaining edges. These are graph radial landscapes; no claim identifies all-pair chords with mechanical saddle edges.

Expected stdout includes:

    GREEN_EXACT_CENSUS GREEN_TRI_C40_RATIONAL_CONTROL 11 20 11 [5, 5, 8] [0, 0, 0]
    GREEN_EXACT_PQ_PACKETS [(1, 3), (1, 3), (5, 4), (10, 4)] [(1, 4), (1, 4), (2, 6), (4, 8)]
    GREEN_EXACT_OUTPUT GREEN_TRI_C40_RATIONAL_CONTROL_AUDIT.json 4780 55f885caa431496a8d2e9538b4f296910043f45390ebec272eeb2003f2e49dda
    GREEN_EXACT_HOMOTHETIC_MASS_MECHANICS_PASS
    GREEN_EXACT_CENSUS GREEN_TRI_C472_MAX_G9 119 236 119 [3, 5, 6] [0, 0, 0]
    GREEN_EXACT_PQ_PACKETS [(1, 4), (1, 4), (45, 48), (23, 48)] [(41, 73), (82, 78)]
    GREEN_EXACT_OUTPUT GREEN_TRI_C472_MAX_G9_AUDIT.json 161876 0a6bc7b0881c7775429b8a1cf6f41df8fa3e1bb940fe61f82f8f099288036040
    GREEN_EXACT_HOMOTHETIC_MASS_MECHANICS_PASS

C40: S=[2,3,5,7,8], U=[3,4,5,6,8], H=[[1,4],[2,5],[3,6],[4,5],[4,6],[4,7],[5,8],[6,9]]. All additional weak lists and primitive zero lists are empty. Maximum bit length across all centred-coordinate numerators and denominators is37. This preserves a very simple exact control of the geometry/mass mechanism rather than a good equilibrium count.

C472: S=[31,59,87], U=[35,38,58,81,84], H=[[22,25],[33,36],[35,38],[81,84],[83,86],[91,94]]. All additional weak lists and primitive zero lists are empty. Maximum bit length across all centred-coordinate numerators and denominators is624. The central guaranteed U is58 and central guaranteed S is59 in the exact output ordering. Both outputs have exactly one hexagonal face.

The C472 P landscape has small one-point bars at peaks38 and81 (birth about1.23018828405, death about1.22924990201), but also a45/48 feature at peak84 (birth about1.23026235778, death about0.74289806392) and a23/48 feature at peak58 (birth about1.10007093628, death about0.73206156581). Its Q bars are41/73 and82/78: birth about3.66979709046, deaths about1.36600532893 and1.34607969594 respectively. These Q death levels are DIFFERENT. The two symmetric off-axis stable components first merge with one another, then their union merges with the central stable component; nested components are legitimate. These decimal diagnostics are not substitutes for the complete exact rational landscapes reproduced by the commands.

## 7. What this changes and what remains open
The new resource is a finite convexity-by-construction, exact-volume-mass chart with a built-in strict stable face and unstable vertex and known edge budget. It is not an ordinary mesh claimed to inherit the smooth POLYSECT14 equilibrium theorem. The C472 body is mechanically far from110 in its large complete P/Q features despite a small local numerical arrow loss. The next useful problem is genuine whole-feature deformation, inter-track escape and exact finite mass compatibility, not reporting only a root-dot sign or suppressing small positive bars.

The family allows moving knots, curvature weights, interior curvature points, axial/transverse scales and affine drift, but the exact part-1 generator fixes one rational knot sequence. Adaptive-knot numerical experiments therefore require a separate exact recovery extension before promotion. Failure of those scouts is not a family exclusion. Breaking this C2 symmetry, changing polygon shape/cardinality, adding or deleting carriers and using other incidence architectures remain mathematically open.

One useful finite-chord caution is independent of any search: a positive escape p->q requires p.q>|p|^2, or cos(theta)>|p|/|q|. Along a path, sum log sec(theta_i)<log(R/r); since log sec(theta)>=theta^2/2, a path changing direction by angular distance Theta needs N>Theta^2/(2log(R/r)). This constrains a chosen path and is NOT an all-polyhedron lower bound without further assumptions. In an off-centred unit circle p=(a+cos(theta),sin(theta)), U=(1+a,0), one has p.(U-p)=(a-1)(1-cos(theta))<0 for 0<a<1, so a long direct chord to the smooth unstable point can fail even when the smooth flow approaches it. Alternative 3D routes and changed curvature are not excluded.
