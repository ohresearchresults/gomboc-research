# material-8da7ecdf4424

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# ACTUAL_ADJACENT_TRIANGLE_PAIR_STEINER_CHART_V1

## Theorem and scope

Let P be a finite full-dimensional convex three-polytope of uniform density. Suppose two adjacent TRUE maximal facets are triangles ABC and ABD, sharing the TRUE edge AB. Let F_a be another true maximal facet which contains C and D but neither A nor B. Write every coefficient Lambda_ai using the actual uniform-volume centroid and actual uniform-area centroid of facet i, as in the accepted physical Lambda definition.

There exists a finite convex polytope P* symmetric under exchange of two affine coordinates, with the SAME two actual triangular facets ABC and ABD, the SAME root supporting plane F_a, the SAME volume and the SAME value of Lambda_ab+Lambda_ac. The two selected coefficients of P* are equal. This is a reduction of this specified actual pair-trace problem to a two-dimensional concave-fibre problem.

This theorem does NOT assert that P* has the same true vertex/edge/facet counts, the same mechanical metric, the same S/U/H, or FULL_TREE253. It does NOT reduce a general root facet disjoint from C or D to this class, and it does NOT prove the still-open universal two-adjacent-triangles bound51/25. It gives no C improvement. Historical novelty is not claimed.

## 1. Affine coordinates and the exact trace formula

The four vertices A,B,C,D are affinely independent because the two triangular supporting facets are distinct adjacent facets of a full-dimensional body. Choose the affine coordinates
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0).
Then P lies in x>=0,y>=0, its x=0 face is exactly ABC, and its y=0 face is exactly ABD. These affine changes preserve the dimensionless actual Lambda coefficients when the actual centroid is transformed with the body; they do not imply metric-independent mechanical equilibria.

Since F_a contains C,D and avoids A,B, its nonnegative affine slack can be normalized as
ell(x,y,z)=1-x-y-hz,
with ell(A)=1, ell(B)=1-h>0, ell(C)=ell(D)=0. Thus h<1; there is no lower bound on h. Let V be actual volume and g=(g_x,g_y,g_z) actual volume centroid. The actual pole-normalized root slack is ell/ell(g), with ell(g)>0.

Both triangular facets have area1/2 in this coordinate chart. Their physical cone masses are d_b=g_x/(2V),d_c=g_y/(2V), where d_i=3omega_i. The affine ell means on both triangles equal (2-h)/3. Therefore

T(P):=Lambda_ab+Lambda_ac
     =(2-h)(g_x+g_y)/[6V(1-g_x-g_y-hg_z)].                         (1)

This derivation uses actual area means and the actual volume centroid, not free weights or independently chosen rows. Only V,g_x+g_y,g_z occur in (1).

## 2. Fibre construction and preservation of the TRUE triangles

Put t=x+y and let D0 be the projection of P onto the (t,z) plane. At fixed (t,z), write the nonempty fibre as
x in [u(t,z),v(t,z)], y=t-x.
Convexity of P gives a convex lower function u, a concave upper function v, a compact convex projection D0, and a nonnegative concave length L=v-u. In the polytope case these functions are piecewise affine. Because x,y>=0, we have
0<=u<=v<=t and 0<=L<=t.

Define
P*={(x,y,z):(t,z) in D0, t=x+y, (t-L(t,z))/2<=x<=(t+L(t,z))/2}.
The new lower bound is convex and the upper bound concave. Consequently P* is a compact full-dimensional convex body; the finite halfspace formula below proves it is a polytope. It is symmetric under x<->y. The Jacobian of (x,t,z)->(x,y,z) has absolute value1, so Fubini gives
Vol(P*)=Vol(P), integral_P*(x+y)=integral_P(x+y), integral_P*z=integral_P z.
In particular g_x*=g_y*=(g_x+g_y)/2 and g_z*=g_z.

It remains essential to check that symmetrization has not merged either designated triangle into a larger facet. Set
Delta={(t,z):t>=0,z>=0,t+z<=1}.
Since conv(A,B,C,D) is contained in P, its fibres over Delta are the full intervals[0,t], hence L=t there. Conversely L=t implies u=0 and v=t. The x=0 and y=0 endpoints then belong to the corresponding actual triangular facets of P, forcing (t,z) in Delta. Thus
L(t,z)=t if and only if (t,z) in Delta.                            (2)
In P*, a point lies in x=0 or y=0 precisely when L=t. Equation(2) proves that its x=0 and y=0 maximal facets are EXACTLY ABC and ABD, not larger coplanar polygons.

The root slack ell=1-t-hz is constant along each fibre, so it remains nonnegative on P* and has the same zero projection. The root face stays two-dimensional: the original root facet contains CD, a full fibre at(t,z)=(1,0), and has a third point with a different (t,z) projection. Convex combinations with CD give a two-dimensional root face after centering the fibres. Thus the specified root supporting plane also remains a true facet.

Apply(1) to P and P*. The volume and the two relevant centroid quantities coincide, proving T(P*)=T(P). The selected coefficients of P* are equal by its symmetry and the identical ell means. No statement about other entries of the physical matrices is implied.

## 3. Exact finite H-description, with no geometric approximation

Suppose P is given by its actual rational inequalities
alpha_i x+beta_i y+gamma_i z<=delta_i.
At fixed t=x+y this becomes
(alpha_i-beta_i)x+beta_i t+gamma_i z<=delta_i.
For alpha_i-beta_i>0 it is an upper affine function U_i(t,z); for alpha_j-beta_j<0 it is a lower affine function l_j(t,z), with the SAME division formula
(delta-beta t-gamma z)/(alpha-beta).
For alpha-beta=0 retain the projection inequality beta t+gamma z<=delta, without division.

The actual fibre has upper end min_i U_i and lower end max_j l_j. Hence
L=min_(i,j)(U_i-l_j).
An EXACT finite halfspace description of P* is given by all retained zero-coefficient projection inequalities and, for every upper/lower pair,
 +(x-y)<=U_i(x+y,z)-l_j(x+y,z),
 -(x-y)<=U_i(x+y,z)-l_j(x+y,z).                                   (3)
These inequalities also enforce nonempty fibres: their left sides have maximum |x-y|>=0, so all U_i-l_j are nonnegative. Conversely each nonempty original fibre gives exactly its centered interval under(3). Thus no projection cell, sign sector, recession condition or limiting fibre has been omitted. With rational data, every new coefficient is rational. Redundant halfspaces may be removed by an exact hull computation; their intersections do not become triangulation edges.

## 4. Two-dimensional remaining variational problem

Writing all integrals over D0,
V=integral L, A=integral tL, B=integral(1-t-hz)L,
we have the exact formula
T=(2-h) A/(6VB).                                                  (4)
The geometric constraints include D0 compact convex, L nonnegative concave, 0<=L<=t, Delta contained in D0, L=t exactly on Delta, and 1-t-hz>=0 on D0. This is a genuine reduction for the root-containing-C,D class, not a proof that extremizers are bipyramids, strip caps or bodies with a bounded number of additional vertices. In particular replacing L by t outside Delta would enlarge the designated triangular facets and needs a separate limiting argument; it cannot be silently treated as another admissible triangle-facet body.

Formula(4) and the convex-fibre formulation may help a future universal pair-trace inequality. No optimization or claimed extremal solution is part of the theorem above.

## 5. Complete exact non-record audit and recovery capsule

The complete self-contained runnable source is [internal-source-reference]. Save literally as pair_steiner.py,6243 UTF-8/LF bytes,SHA2563b4be12cda6d7297e7c3f6a1f04be3f2c04db5a7d06832ef28fe5683b2534a54. It contains every hull, halfspace, true-edge, facet-centroid, volume, centroid, physical-Lambda and symmetrization helper. No other source material, data file, external package, random seed, floating tolerance or optimized checkpoint is required.

The exact original six vertices are
(0,0,0),(0,0,1),(0,1,0),(1,0,0),(1/100,4/5,19/80),(3/4,1/50,23/80).
The root plane is5x+5y+4z=5. The source constructs P* using ALL inequalities(3), enumerates every feasible triple-plane intersection exactly, reconstructs both maximal face lattices and true edges, and integrates the actual bodies. It checks the full physical identities Lambda1=3, LambdaQ=-Q, Lambda^2+Lambda=4*1d^T, sumd=3 and both actual mass/centroid balances, rather than assigning a candidate coefficient row by hand.

Observed original f-vector(6,11,7), image f-vector(7,13,8). This explicitly demonstrates why the operation must not be used as a complexity-preserving transformation. The exact preserved pair trace is
1799763200/887522067>2.
This is a non-record control, not a sharp value or a Gömböc candidate. The complete original and image coordinates, maximal facets, true edges, volume/centroid values, physical matrices and H-description are regenerated in the output.

Environment actually executed: CPython3.13.5, standard library/Fraction only, assertions enabled. Reconstruction: `python -S pair_steiner.py build`. Verification: `python -S pair_steiner.py check`. Both commands were executed, including equality to the full existing output on the check run.
Output pair_steiner.json:5617bytes,SHA25685919b3cc6d98f239382d3ba1bcd31831f9705236078059389c8d5cbf0688ef0.
Observed terminal marker:
`ACTUAL_TRIANGLE_PAIR_STEINER_EXACT_PASS [6, 11, 7] [7, 13, 8] 1799763200/887522067 5617 85919b3cc6d98f239382d3ba1bcd31831f9705236078059389c8d5cbf0688ef0`.

Disposition: accepted as the stated continuous symmetrization lemma, its exact finite H-construction, and a fully reproducible non-record physical control. It does not alter C>=34, K2/K3 exclusions, the open universal51/25 triangle-pair question, or the unverified Figure650 boundary.
