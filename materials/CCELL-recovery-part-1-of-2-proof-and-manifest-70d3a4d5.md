# material-70d3a4d53955

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# CCELL-20260925 recovery capsule part 1/2: theorem and manifest

Status: coordinator derivation and exact method demonstration, independent of C622 coordinates. NOT a new class-110 figure, NOT a record improvement, NOT a global exclusion theorem. Part 2/2 supplies the complete runnable centroid_cell.py; both parts are required for computational recovery. No historical novelty claim is made.

## Exact affine uniform-centroid theorem

Let T be the consistently outward-oriented triangular boundary of a convex three-dimensional polyhedron of constant density one, with vertices p_i. All triangles below are actual strict facets, not auxiliary triangulations of flat polygonal faces. Its signed volume and unnormalised first moment are
V=(1/6) sum_T det(a,b,c),
M=(1/24) sum_T det(a,b,c)(a+b+c).
These follow by summing signed tetrahedra (0,a,b,c), each with centroid (a+b+c)/4.

Choose movable vertices I with no triangle containing two distinct members. Rotate each incident triangle to (p_i,u,v) without reversing orientation, and put A_i=sum_link(u cross v). The link vertices are fixed. Allow delta_i with A_i dot delta_i=0. Then, exactly,
V(delta)=V_0,
M(delta)=M_0+sum_i L_i(delta_i),
L_i(d)=(1/24) sum_link[(d dot (u cross v))(p_i+u+v)+(p_i dot (u cross v))d].
Proof: determinant changes by d dot (u cross v), so volume changes by A_i dot d/6=0. Expanding the first moment gives the displayed linear terms and quadratic remainder d(A_i dot d)/24=0. Noncofacial moving vertices have no common-triangle cross terms. Multiple tangent directions at one vertex are allowed because their total displacement remains tangent. This is not a linear approximation.

Choose rational tangent directions d_j and parameters x_j. If B_j=L_i(d_j), actual homogeneous centroid zero is exactly Bx=-M_0, provided the resulting body remains convex and V_0>0. Rational elimination gives x=x_0+Nz. Rank below three is a real limitation of these handles, and full rank alone does not guarantee a geometrically admissible correction. With limits |x_j|<=rho_j, every direction w necessarily satisfies |w dot M_0|<=sum_j rho_j |w dot B_j|, by applying w to Bx=-M_0. Failure excludes only this bounded repair, not other bodies or handles.

## Quadratic geometry and equilibrium conditions

After centroid elimination every movable coordinate is affine in z. For outward triangle f=(a,b,c), n_f=(b-a) cross (c-a). The support margins h_(f,j)=-n_f dot(p_j-a), j not in f, have degree at most two: n_f and its plane offset are affine when only one triangle vertex moves, and p_j is affine. Require all h>0, valid connected oriented spherical incidence, positive volume and origin strictly inside. These checks certify the actual strict triangular hull; flat diagonals are excluded.

For directed edge i->j put r_(i,j)=p_i dot(p_i-p_j). For the oriented edge a->b in triangle f put s_(f,a,b)=n_f dot(a cross b). Both are quadratic or lower, since a triangle has at most one moving vertex.

Relative to origin: a vertex is strictly unstable iff all its incident r margins are positive. A triangular face is strictly stable iff its three s margins are positive. Indeed the perpendicular foot's barycentric numerators are n_f dot(b cross c), n_f dot(c cross a), n_f dot(a cross b), whose sum is |n_f|^2.

A convex edge a,b is a strict saddle iff r_(a,b)>0, r_(b,a)>0 and both incident face-edge s margins are positive, using each face's own orientation. The r conditions put the perpendicular foot in the open edge. For the normal cone, orient e=b-a as in f. If q is the foot, q dot(n_f cross e)=-s_f; strict convexity gives n_g dot(n_f cross e)<0 for the other outward normal. The coefficient of n_g in q's normal-cone expansion is therefore positive exactly when s_f>0. The other face gives the other coefficient.

The corresponding non-strict inequalities with at least one zero identify boundary/weak feature equilibria. A primitive zero alone need not be an equilibrium if another required inequality is negative. Weak points can occur at multiple features, so weak_features is not a count of distinct spatial points.

Consequently a fixed strict primitive sign pattern, after exact uniform-centroid elimination, is an open set defined entirely by strict quadratic inequalities. This removes nonlinear centroid penalties and does not use artificial vertex masses. Preserving the sign pattern also preserves equilibrium counts; it cannot improve those counts by itself. A mesh surgery or facet coalescence requires new incidence and fresh certification. Nontriangular facets require separate planarity and geometric-face treatment. Nothing here says S/U/H counts alone establish the proper strict class 110.

## Uniform safe-box certificate

Expand a primitive polynomial at z0 as f(z0+y)=c+l dot y+sum_(i<=j)q_ij y_i y_j. On |y_j|<=r,
sign(c) f(z0+y)>=|c|-r sum_j|l_j|-r^2 sum_(i<=j)|q_ij|.
If the right side is positive for every primitive polynomial, the entire real box preserves all signs. A nonpositive estimate is inconclusive. Source code obtains coefficients by exact polarization. Its sample identity checks test the implementation; the degree bound is established by the proof above.

## Literal demonstration and limitations

Start with core vertices (1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1). Add one apex equal to minus half each core vertex over its opposite triangular face; replace that face by the three outward edge-apex triangles. Perturb apex 4 by (1,2,-3)/100. Input V=4 and M=(1/1200,1/600,-1/400). The other three apices 5,6,7 are pairwise noncofacial handles. Use the deterministic two-vector basis of A_i-perp in part 2's source.

Response rank is 3 and the centroid-zero family has three free parameters. Particular six parameters: (-1/50,1/50,0,1/100,0,0). Nullspace basis: (-1,0,1,0,0,0); (-1,1,0,-1,1,0); (0,-1,0,0,0,1). At free parameters z0=(1/1000,-1/500,3/1000), the complete corrected vertices are:
0 (1,1,1)
1 (1,-1,-1)
2 (-1,1,-1)
3 (-1,-1,1)
4 (-49/100,-12/25,-53/100)
5 (-63/125,481/1000,103/200)
6 (489/1000,-499/1000,64/125)
7 (101/200,249/500,-497/1000).

The outward face list is generated deterministically from the four core faces in the complete source and is emitted literally in the JSON output. Exact tests give V=4, M=(0,0,0), (V,E,F)=(8,18,12), C=36, S=12,U=8,H=18, no weak features and no zero primitive margins. This is a regression fixture, emphatically NOT a class-110 candidate or an attempted exception to the known V>=10 target-class bound.

There are 132 primitive polynomials and 64 exact rational-grid tests, totalling 8448 identity comparisons. The real box z0+[-1/32,1/32]^3 has a strict-sign certificate with minimum conservative margin 315033/4000000, for radial:5:3. This is a continuum certificate for the demonstration family, not a floating-point sample.

## Reconstruction manifest

Required code in part 2/2: centroid_cell.py, 15240 UTF-8 bytes, SHA-256 22dec487220bb33a53f12211aa3b08a5cc1869df3184088697f1d1267e2a3af3. Python 3.10+ standard library only; executed with Python 3.13.5. All arithmetic fractions.Fraction; no optimization, random seed, checkpoint or precision parameter.

Reconstruct and verify:
python centroid_cell.py --output centroid_cell.json

Expected output: centroid_cell.json, 49579 bytes, SHA-256 2fa271ae8b5f97124ecea1be6c926756cc539eb2bc4e951b92e60ae42579540c. Contains complete input/output coordinates, outward incidence, handles, exact response/nullspace and all 132 quadratic tables.

Expected terminal markers:
EXACT_VOLUME_PRESERVED 4
EXACT_FIRST_MOMENT_ZERO (Fraction(0, 1), Fraction(0, 1), Fraction(0, 1))
STRICT_CONVEX_HULL (8, 18, 12)
EQUILIBRIA_S_U_H 12 8 18
WEAK_FEATURES 0
QUADRATIC_IDENTITY_CHECKS 8448
STRICT_SIGN_BOX_RADIUS 1/32 MARGIN 315033/4000000
CENTROID_CELL_SELFTEST_PASS

Verify hashes with `sha256sum centroid_cell.py centroid_cell.json` and sizes with `wc -c centroid_cell.py centroid_cell.json`.

## Next scientific use and evidence boundary

Apply this only to actual exact geometry, then select eligible handles, inspect response rank, and solve its strict quadratic region. It cannot repair an abstract word, infer convexity from a positive weighted-moment relaxation, or assert that a failed RSS gate passes. No C622 coordinates were used or altered. Current state and source-read identities disagreed during this turn; the unavailable old methods were not silently substituted or declared verified. The goal C<500 of proper strict class 110 remains open.
