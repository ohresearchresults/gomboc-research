# material-3d8b947f80c1

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# FULL_PATCH_A_STAR_FLATTENING_V1

## Status and scope

Coordinator analytic extension of the proper33 negative-z stationary exclusion to the enlarged fixed-triangular-patch class. This is a theorem about a full fixed-parameter local maximizer, not a value bound for every body with a negative-z vertex. It allows expanded coordinate facets and c=0 and/or d=0. It does not prove a mechanical E=17 exclusion, a C=36 construction, or the exact minimum. The accepted mechanical interval remains 34 <= C_min <= 622.

No numerical computation or missing sandbox file is needed for this source unit. The algebra and facet first-variation argument are given completely below. The universal joint first-moment inequality, including its equality consequence, is an accepted input from JOINT_MOMENT_PHYSICAL_REDUCTION_V1.md, material [internal-source-reference], SHA-256 af3f183350504641c42591222857459ee0df0455281a7455943783b3290e5f702, read completely by this coordinator. Its extension and the enlarged-class attainment framework were read in GLOBAL_HIGH_TRACE_ATTAINMENT_AND_ROOT_CUT_FIRST_VARIATION_V1.md, material [internal-source-reference], SHA-256 46e7eb5d8d1a4fcb436cf88716e235020f62d21b07b46d3380ac400a9db96794. The proper33 precursor is the complete accepted result minimum-0181, SHA-256 420ffe89544d6fbfd9ed6301c426209336f6352c0df589d4af045e8423d54beb. The present whole-facet argument does not require the proper33 AC-edge classification of that precursor.

## 1. Class, variables, functional

Let A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0). Let P be a bounded, full-dimensional convex polytope containing T0=conv(A,B,C,D), with P contained in x>=0, y>=0, ell>=0. Thus ABC and ABD are fixed triangular patches of the x=0 and y=0 support facets, which may be larger than these triangles. Put

ell(x,y,z)=a+(d-a)x+(c-a)y-(a-b)z,

a=ell(A)>0, b=ell(B)>0, c=ell(C)>=0, d=ell(D)>=0.

All four heights and the marked points remain fixed in a variation. Interchange A and B, by the affine reflection (x,y,z)->(x,y,1-x-y-z), when necessary to normalize a>=b. Define

h_c=a+b+c, h_d=a+b+d, n(x,y,z)=h_c x+h_d y,
V=integral_P 1, t=6V,
g=V^(-1) integral_P (x,y,z), mu=ell(g)=V^(-1) integral_P ell,
N=integral_P n=Vr, r=n(g), H=integral_P ell=V mu,
T=N/(6 V H)=r/(t mu), q=N/H=tT,
G(p)=n(p)-r-q ell(p).

Then G_A=-r-q a=-tT(mu+a) and G_B=-tT(mu+b). Set L_A=-G_A/3=tT(mu+a)/3 and L_B=tT(mu+b)/3. The class under consideration has no fixed facet-count restriction; admissible small shaves or rotations must preserve the four marks and the three containing halfspaces. A full local maximizer means local maximality under such variations, rather than maximality in a single incidence stratum.

## 2. Universal inequalities and strictness

Accepted joint first-moment inequality J:

g_x>=1/4, g_y>=1/4, 4(g_x+g_y)<=t+1.

The equality case of its final inequality, for actual bodies in this class, has T<=2. Consequently at T>2 the final inequality is strict. These are physical moments of one body, not independent moment variables.

For any p in P, triangulate the boundary without crossing the fixed patches ABC and ABD, and cone to p. The affine cone-moment formula gives

4H-ell(p)V = sum over boundary triangles Delta of Vol(conv(p,Delta)) times the sum of ell at the three vertices of Delta.

The ABC and ABD contributions are p_x h_c/6 and p_y h_d/6. All other contributions are nonnegative. Hence the patch cone bound is

24H >= n(p)+t ell(p), equivalently 4t mu >= n(p)+t ell(p).       (CONE)

This derivation does not require either entire support facet to be triangular. Substitution p=g gives T<=3. In fact T<3: since g is interior, every positive-area boundary triangle has positive cone volume. A bounded three-dimensional polytope cannot have all its maximal facets among just x=0, y=0, ell=0. A further maximal facet is not contained in ell=0 and therefore has a positive-area subset where ell>0, contributing strictly beyond the two fixed patches. Thus CONE at g is strict.

After interchanging x and y if needed, assume c>=d. Then J yields

4r = 4h_c g_x+4h_d g_y <= h_c(t+1)-(c-d) = h_c t+h_d.

CONE at C gives h_d+t c<=4t mu. Combining,

r-t mu <= t(a+b)/4,
D_mu := a+b-4(T-1)mu >=0.                                  (J+CONE)

At T>2, D_mu>0, because J is then strict and h_c>0. The derived statement is symmetric in c,d and therefore requires no ordered-endpoint hypothesis in its use.

CONE also gives a pointwise bound

G(p) <= t[(4-T)mu-(T+1)ell(p)].                            (G-CONE)

## 3. Uniform A-star gap

Put Psi_A=a T^2+b T-3(a+b). Direct expansion gives the exact identity

3(T-1)[L_A-t(4-T)mu] = t[Psi_A+(3-T)D_mu].                (A-ID)

For T>=2,

Psi_A-(a-b)(T-1)=(T-2)[a(T+1)+2b]>=0.

Consequently, if a>b and T>=2, the facts T<3 and D_mu>=0 imply

G(p) <= L_A-delta_A-t(T+1)ell(p),
delta_A=t(a-b)/3>0.                                       (A-GAP)

If a=b and T>2, the same conclusion holds with some positive delta_A; for example delta_A=t Psi_A/[3(T-1)]>0, since Psi_A=a(T-2)(T+3)>0. Thus every point of P satisfies G(p)<=L_A-delta_A whenever either a>b,T>=2 or a=b,T>2. In particular this is a uniform gap, including zero-height vertices.

## 4. A and B are true vertices at a full maximizer

For a boundary variation with outward normal velocity v, differentiation of T=N/(6VH) gives

T' = (1/(6VH)) integral_boundary G v dS.                  (VAR)

At an unmarked true vertex with G<0, a sufficiently small inward shave preserves all four marks and strictly raises T. Such a vertex cannot occur at a full local maximizer.

The set P intersect {x=y=0} is a bounded interval on the z-axis. It contains AB. Its endpoints are true vertices, and G=-r-q ell<0 along this interval because r,q>0 and ell>=0. Any endpoint outside {A,B} would therefore be a forbidden unmarked vertex. The endpoints are exactly A and B; both are true vertices and AB is an actual edge. An edge of a convex three-dimensional polytope belongs to precisely two maximal facets, here x=0 and y=0. Thus no other maximal facet contains both A and B.

## 5. Legal whole-facet rotation and flattening

Let F be any maximal facet through A other than x=0 and y=0. It does not contain B by the preceding edge argument, and cannot be ell=0 since ell(A)>0. Suppose F does not contain both C and D. Write its inward halfspace as f>=0, with f=0 on F. Choose the affine nonnegative function h as follows:

- if C belongs to F but D does not, take h=x;
- if D belongs to F but C does not, take h=y;
- if neither belongs to F, take h=x+y.

In all cases h vanishes at A and at every other marked point on F, while h>0 on the relative interior of F. The marked points not on F have strict f-slack. Therefore replacement of f>=0 by f-epsilon h>=0, for sufficiently small epsilon>0, is an admissible inward rotation preserving all marks, coordinate supports and the root halfspace. It acts on the entire facet, not on independently movable artificial triangulation pieces.

Triangulate F as a fan from A solely to integrate affine functions. For a triangle Delta=conv(A,V,W) with h(A)=0, the elementary simplex integral is

integral_Delta G h dS = area(Delta)/12 * [h(V)(G_A+2G_V+G_W)+h(W)(G_A+G_V+2G_W)].

By G_A=-3L_A and the uniform gap G_V,G_W<=L_A-delta_A, this is at most

-delta_A area(Delta)[h(V)+h(W)]/4
=-(3 delta_A/4) integral_Delta h dS.

Summing the fan gives integral_F G h dS<0. The rotation f-epsilon h>=0 has outward normal velocity -h/||grad f||. VAR therefore gives

T' = -integral_F G h dS /(6VH ||grad f||)>0,

contradicting full local maximality.

Every free maximal facet through A must therefore contain both C and D. There is only one possible plane, z=0. A true three-dimensional vertex needs a third facet besides x=0 and y=0, so this facet is present. Since B has z=1, its inner halfspace is z>=0. We have proved:

### Full-patch A-star theorem
At a full fixed-parameter local maximizer in the enlarged patch class, if a>b and T>=2, or if a=b and T>2, A is a simple vertex with its three maximal supporting planes x=0, y=0, z=0. The ACD triangle lies in the z=0 facet, and the whole polytope lies in z>=0.

No positivity assumption on c or d is needed. The conclusion is not restricted to proper33. A deformation in a fixed combinatorial type need not detect this ascent; maximality in the whole patch class is essential.

## 6. Reflected B-star obstruction and height-ratio consequence

The affine reflection (x,y,z)->(x,y,1-x-y-z) preserves absolute volume, fixes C,D, interchanges A,B, and leaves n,T,mu invariant. Define Psi_B=b T^2+a T-3(a+b). The corresponding exact identity is

3(T-1)[L_B-t(4-T)mu] = t[Psi_B+(3-T)D_mu].                (B-ID)

If T>2 and Psi_B>=0, then D_mu>0 and T<3 make the right side strictly positive. G-CONE then gives a uniform positive B-star gap. The same legal whole-facet proof shows that the BCD plane x+y+z=1 supports P from above and is the only free maximal facet through B.

For a>=b and T>2, A-star flattening already holds. If B-star flattening also held, P would lie in x>=0,y>=0,z>=0,x+y+z<=1, and since it contains T0 would equal T0. But

T(T0)=(2a+2b+c+d)/(a+b+c+d)<=2,

a contradiction. Therefore any full enlarged-patch local maximizer with T>2 and a>=b satisfies

Psi_B<0,
b/a < (3-T)/(T^2-3).

The function on the right is strictly decreasing for 2<T<3. In particular T>=51/25 forces

b/a < 100/121.

Thus balanced high full maximizers are excluded, and every possible high full maximizer, including root endpoint degenerations, lies in the octant and has a>b with this quantitative imbalance. This is a necessary condition on actual maximizers, not an unconditional balanced-family value theorem without an accompanying attainment argument.

## 7. Consequences and next scientific gap

The accepted high-level attainment theorem in [internal-source-reference] allows passage from a hypothetical value at least 51/25 to an enlarged patch maximizer. The present result removes every negative-z full-maximizer sector at once, including expanded coordinate facets and zero c/d endpoints. It should be combined with actual octant polygon-star and endpoint results, respecting their exact hypotheses. Existing proper33 and expanded-family names alone do not establish coverage. In particular, one-coordinate-expanded two-nonpositive-anchor cases and endpoint limit classes require an explicit coverage argument or fresh inequalities.

The worker minimum-0181 also preserves a distinct exact U_D nonwinning deformation and root second-moment inequalities; neither is replaced or discarded here. The new theorem is not a replay of that construction and requires no computational recovery capsule. The physical common-SPD bridge and all unresolved mechanical realizability questions remain separate.
