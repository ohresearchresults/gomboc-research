# figure-0033

AI research report · 2026-08-22 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Result: exact shell obstruction and a rational threshold corridor

## Verdict

No homogeneous polyhedral Gömböc is claimed. The proposed high-shell strategy has a sharp geometric obstruction: retaining the original positive-side support while preserving the original reference center and unique unstable vertex forces both a very long successor chain and a convex-hull volume several times larger than the entire original Reshetov body. The useful replacement regime begins only after moving the positive support inward to approximately three quarters of its original radius.

The constructive output is an exact rational 15-edge radially monotone corridor, an exact closed 32-vertex prism moment module, and an exact 45-vertex disk patch spanning the existing 15-point separatrix. The latter has complete local combinatorics and strict fixed-center successor witnesses, but its global convex gluing and true-centroid audit remain open.

A consolidated report and complete artifact package are available at VIVID_ATLAS_RESULT.md and vivid_atlas_corridor_package.zip.

## 1. Exact source geometry

The original rational Reshetov polyhedron has `(V,E,F)=(24,36,14)` and volume approximately `2.631109788037206e9`. Its exact uniform-volume centroid is

`C_R approximately (-104.1014775785565, 8.465022473324968, -47.56244776570032)`.

Relative to `C_R`, its mechanical audit is `(S,U,H)=(1,2,1)`: stable face 11, unstable vertices 9 and 16, and saddle edge `(17,18)`. Vertex 9 is the desired global maximum; vertex 16 is the maximum to be cancelled. Their radii from `C_R` are approximately

`R_9=8922.291...`, `R_16=8485.537...`, `R_16/R_9=0.951049...`,

and their angular separation is approximately `Theta=3.089` radians.

The exact separatrix has 15 boundary vertices labelled

`q,A1,A2,A3,A4,A5,p,B9,B8,B7,B6,B5,B4,B3,B2`.

The existing 27-vertex replacement proves cancellation at fixed `C_R`, with `(V,E,F)=(27,58,33)` and `(S,U,H)=(1,1,0)`, but its own centroid is approximately

`(-2589.6385146523567, 10.129056745597389, -50.441025273326)`.

Thus it removes far too much positive-side material.

## 2. Sharp successor-path lower bound

Translate `C_R` to the origin. For every strict successor edge `x_i -> x_{i+1}`,

`x_i dot (x_{i+1}-x_i) > 0`.

Let `r_i=||x_i||` and let `theta_i` be the angle between `x_i` and `x_{i+1}`. The successor inequality implies

`r_{i+1} cos(theta_i) > r_i`.

Consequently radii strictly increase and every `theta_i` lies below `pi/2`. For an `n`-edge path from original vertex 16 to vertex 9,

`R_16/R_9 < product_i cos(theta_i)`.

The spherical triangle inequality gives `sum_i theta_i >= Theta`. Since `log(cos t)` is decreasing and concave on `[0,pi/2)`, Jensen's inequality yields

`product_i cos(theta_i) <= cos(Theta/n)^n`.

Therefore the necessary condition is

`R_16/R_9 < cos(Theta/n)^n`.

Directed interval evaluation of the exact rational endpoint data proves that `n=95` fails. The scalar obstruction first ceases at `n=96`. Hence any fixed-center construction retaining original vertex 16 and having vertex 9 as its unique unstable vertex needs at least 96 strict successor edges and therefore at least 97 distinct vertices on that path. In particular, no 27-vertex or 31-vertex replacement retaining vertex 16 can work, independently of convexity or centroid correction.

An exact rational 100-edge witness chain from original vertex 16 to vertex 9 is included in corridor_chain_certificate.json, with an independent checker at verify_corridor_chain.py.

For a start moved inward to `C_R+t(v16-C_R)`, the necessary condition becomes

`t R_16/R_9 < cos(Theta/n)^n`.

At `t=3/4`, the exact interval audit proves that 14 edges are impossible while 15 edges are feasible. This is the first low-complexity regime compatible with the 15-point separatrix budget.

## 3. Convex-volume obstruction to retaining the high positive support

The original exact halfspace list certifies that the entire ball `B(C_R,200)` lies inside the Reshetov body.

Let `a=v16-C_R`, `b=v9-C_R`, `r=||a||`, `R=||b||`, and `u=a/r`. Write

`b=beta u+z`, with `beta=u dot b<0` and `sigma=||z||`.

### Retaining vertex 16

Every successor path from `a` to `b` crosses the plane `u-perp`. Let the crossing point be `c`. The squared radius increases along every point of a successor edge, so `||c||>=r`. A direct cross-product decomposition gives

`Area(conv(a,b,c)) >= (r/2)((r-beta)-sigma)`.

The exact certificate evaluates this lower bound at approximately `7.18e7` square units.

For every triangle `T` and centered ball of radius `rho`,

`Vol(conv(T,B(C_R,rho))) >= (2 rho/3) Area(T)`.

For `rho=200`, any convex body containing the certified core, original vertex 16, and a successor corridor to vertex 9 therefore has volume at least approximately `9.5e9`, over 3.5 times the complete original Reshetov volume.

### Retaining the original support without retaining vertex 16 as a vertex

Assume only that the body contains the original point `a`. A support vertex in direction `u` has the form `w=alpha u+s`, where `alpha>=r`. Because vertex 9 is to remain the unique unstable vertex, every vertex has radius at most `R`; hence

`||s|| <= sqrt(R^2-r^2)`.

Following successors from `w` to `b` and repeating the crossing argument gives the conservative exact bound

`Area(conv(w,b,c)) >= 1/2 [r(r-beta)-R sigma-(-beta)sqrt(R^2-r^2)]`.

Its certified value is approximately `5.9e7`. Together with `B(C_R,200)`, this forces volume approximately `7.9e9`, roughly three times the original body.

The parameterized version of the same inequality shows that, if `B(C_R,200)` is retained and total volume is not to exceed the original Reshetov volume, positive radial support must be reduced to about `t<=0.758`. This removes approximately 2050 units of radial support. At full original support, the largest compatible inradius is only about 66, far below the certified radius 200.

Thus a shell preserving nearly all positive-side support is not a moment-efficient replacement. The old low disk moved too far inward, but the opposite extreme is rigorously excluded. The viable design window is near `t=3/4`.

Exact data and checkers are in support_volume_obstruction.json, verify_support_volume_obstruction.py, general_shell_volume_obstruction.json, and verify_general_shell_bound.py.

## 4. Exact rational 15-edge corridor

Set

`s=C_R+(3/4)(v16-C_R)`, `p_0=s`, and `p_15=v9`.

A real guide path uses equal angular increments in `span(v16-C_R,v9-C_R)` and geometric radial growth. Its 14 interior points were rounded to exact Cartesian rationals with denominator `10^18`; both endpoints retain their exact source rational coordinates. Exact arithmetic verifies for every `j=0,...,14` that

`(p_j-C_R) dot (p_{j+1}-p_j) > 0`.

All 16 coordinates, all strict successor numerators and denominators, the 14-versus-15 threshold audit, and the convex turn and chord determinants are recorded in corridor15_certificate.json. The independent exact checker is verify_corridor15.py.

### Closed prism module

Let `w` be the exact rational vector perpendicular to the corridor plane listed in the certificate. For rational `epsilon>0`, define

`p_j^+=p_j+epsilon w`, `p_j^-=p_j-epsilon w`.

This is the prism over the certified convex 16-gon. Its complete face audit is

- `V=32`;
- `E=48`;
- `F=18`;
- two 16-gon caps;
- sixteen side quadrilaterals, including the chord side;
- Euler identity `32-48+18=2`.

Because `w` is perpendicular to every corridor edge, each nonterminal cap vertex keeps the same exact successor witness. The certificate contains exact rational volume and first moment. Under transverse scaling,

`Vol(K_epsilon)=epsilon V_1`, `M(K_epsilon)=epsilon M_1`,

so its centroid is independent of `epsilon` by reflection symmetry. This provides an exact tunable moment module, although the untapered prism duplicates the terminal endpoint and is not itself the final mechanical replacement.

## 5. Exact separatrix-spanning tapered patch

The exact 15-point original separatrix is used as the inner boundary. The outer high loop consists of two 15-edge rational rails sharing the single start `s` and the single terminal vertex 9. It therefore has 30 vertices rather than two duplicated endpoint pairs.

The loops are joined by an exact annular triangulation, and the high loop is filled by the tapered corridor strip. The complete local audit is

- `V=45`;
- `E=104`;
- `F=60`;
- 45 annulus triangles;
- 15 high-strip faces;
- Euler disk identity `45-104+60=1`.

Every one of the 15 inherited separatrix vertices has an explicit exact successor witness. Every new nonterminal high-loop vertex has an exact strict successor toward vertex 9. Both rails meet at the same terminal vertex, so the patch does not duplicate the desired maximum.

The exact rational vertex list, all 60 face cycles, the deduplicated 104-edge list, all successor dot products, and the signed tetrahedral volume and first-moment sums of the open patch are in corridor15_separatrix_patch.json. The independent checker is verify_corridor15_patch.py.

This is a complete exact surface replacement and discrete-monotonicity certificate. It is not yet a complete convex polyhedron certificate: after gluing to the retained Reshetov region, the proposed faces must still be proved supporting and the absence of unintended hull faces must be audited.

## 6. Exact centroid residual and reachable correction bound

Define the central first-moment residual

`Q(P)=Vol(P)(c(P)-C_R)`.

For the old 27-vertex low replacement,

`Q_0 approximately (-3.286331659622633e12, 2.200155712869e9, -3.806002588931e9)`.

The exact rational components are contained in parent_patch_certificate.json.

The previously certified eight remote controls have maximum possible positive-x correction

`Delta Q_x,max=4.372543409026824e9`.

Therefore a new basin replacement must first supply a necessary x correction in the interval

`[3.281959116213606e12, 3.290704203031660e12]`

before those controls can possibly solve the remaining exact moment equations. The old residual exceeds their entire x reach by the exact certified factor `751.5835...`. Exact polynomials and endpoint bounds are in outward_moment_polynomials.json.

The new tapered patch has exact signed open-patch volume and first moment, but those quantities cannot yet be identified with a global convex-body moment change: convex-hull gluing may remove intended faces or introduce unlisted faces. Consequently the post-gluing residual has not been proved to lie in the remote-control box.

## 7. What remains

The remaining problem is a finite exact gluing calculation rather than a search for the appropriate radial scale:

1. vary the transverse widths and, if required, move selected high-loop vertices along their certified successor directions;
2. prove all proposed patch faces are supporting after gluing to the retained Reshetov vertices and enumerate every resulting hull face;
3. recompute exact global volume and first moment;
4. use the already full-rank remote controls to solve the three rational moment equations;
5. audit every face, edge, and vertex relative to the resulting true uniform centroid.

The certified obstruction sharply restricts that search to the neighborhood of `t=3/4`. A near-original-support shell requires at least 97 path vertices and excessive volume, while the old radius-300 disk loses orders of magnitude too much positive first moment.
