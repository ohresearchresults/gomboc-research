# material-88e816dcd105

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# PROPER33_POSITIVE_OCTANT_ROOT_ONLY_V1

## Status, exact scope and source dependencies

This is a new analytic geometric bridge proved by the coordinator. It is not a computational search, a replay of another result, or a claim about all E17 realizations. The geometric theorem below is self-contained once its explicit facet hypotheses are supplied. The stationary corollaries use the following complete immutable results, all read from cursor 0 through EOF before synthesis:

* minimum-0165, SHA256 078f5b8df8a0c5b0ccb7a22bc3fa7aa26301717b0635893ed1c728e9efffebeb: proper-33 negative-anchor facet classification, ordinary root-edge bases, and negative-z threshold.
* minimum-0164, SHA256 24b1e77ad400149d28a7ab046bbf9f750c5360fde51ae076aeab5565d3a18d84: actual root-only positive-octant bodies with 0<c,d<a have T<203/100, with no root-polygon size restriction.
* minimum-0111, SHA256 64909830719ea325d6660a5d6d081ded07c9b30b980c16c647d4b81ee5d2c822: every actual proper-triangle high-trace candidate T>=51/25 necessarily has max(c,d)<943(a+b)/1352.

These authored results are used as accepted mathematical premises; no independent rerun of their exact certificates is claimed here. The present proof has no software dependency or computational input/output capsule.

## 1. Canonical setup

A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0), T0=conv(A,B,C,D). Let

ell(x,y,z)=a+(d-a)x+(c-a)y-(a-b)z,

a>b>0, c,d>0.

Let P be a bounded full-dimensional convex polytope with T0 subset P subset {x>=0,y>=0,z>=0,ell>=0}. Assume its maximal coordinate facets are exactly P intersect {x=0}=ABC and P intersect {y=0}=ABD. This is the proper-33 condition. Assume F0=P intersect {ell=0} is a positive-area facet. All references to vertices, edges and facets mean true vertices, true edges and maximal facets, not triangulation artifacts.

For stationary applications define

V=int_P 1, Eell=int_P ell, n=(a+b+c)x+(a+b+d)y,
N=int_P n, r=N/V, q=N/Eell, G=n-r-q ell,
T=N/(6 V Eell).

P uses its actual uniform volume integrals. Nothing is independently recentered or assigned fictitious mass.

## 2. Pure geometric theorem

In addition to the preceding setup, suppose:

(H1) Every facet other than x=0, y=0, z=0 and ell=0 contains a canonical mark from {A,B,C,D}.

(H2) Every such facet containing exactly one canonical mark is a triangle XUV, where X is that mark and U,V belong to F0.

Then every true vertex of P other than A,B,C,D belongs to F0. Equivalently,

P=conv(T0,F0).

This theorem does not require a bound on the number of vertices or facets, generic simplicity, a sign condition on G, or a restriction c,d<a. The signs of G are only one way in which the stationary theory supplies H1-H2.

### 2.1. Exhaustion of possible supporting planes

The plane z=0 is a genuine facet plane because P lies above it and contains the noncollinear A,C,D. The edges AB, AC, AD already belong to two distinct coordinate-plane facets: AB to x=0 and y=0; AC to x=0 and z=0; AD to y=0 and z=0. Thus no other maximal facet can contain any of these pairs.

BC is a true edge of the maximal triangle ABC and consequently belongs to exactly one further maximal facet. Similarly BD belongs to exactly one further facet. Their planes can be written uniquely as

p x+y+z=1 and x+q y+z=1,

respectively, with P on the <= sides. Containment of A determines the side. Containment of D or C gives p<=1 and q<=1. Equality in either gives the plane BCD, x+y+z=1. Since P is in the nonnegative octant and contains T0, that support would imply P=T0. But ell is strictly positive on T0, so there would be no F0. Therefore p,q<1.

If a further facet contains C and D, then CD is a true edge of z=0, this facet is unique, and its plane has the form

x+y+kz=1, P on the <= side, k<1.

Indeed k<=1 follows from B, and equality is the same impossible BCD support. If this CD facet exists, its intersection with z=0 gives x+y<=1; together with nonnegative x,y and containment of A,C,D this proves P intersect {z=0}=ACD. If no such facet exists, z=0 may be larger than ACD and CD may be a diagonal.

Any facet containing at least two canonical marks is therefore among the three coordinate facets and the BC, BD, optional CD facets just described. This includes the possible three-mark cases; BCD is excluded as above. All remaining nonroot facets are the one-mark triangles in H2.

### 2.2. An off-root auxiliary vertex is incident only with pair planes

Suppose w is a true vertex different from A,B,C,D and ell(w)>0. Proper-33 implies x(w)>0 and y(w)>0. A triangle XUV in H2 has only the three stated vertices, so it cannot contain w: a true vertex of P lying in a face must be a vertex of that face. Likewise w is not on the root facet.

Thus all supporting facet planes incident with w belong to the list z=0, BC, BD, optional CD. At any true vertex the incident facet normals span dimension three, even when the vertex is not simple.

### 2.3. Case z(w)>0: a five-vertex outer container

Now w is not on any coordinate facet. The three pair planes BC,BD,CD must all be present and intersect at w with independent normals. Put

alpha1=1-p>0, alpha2=1-q>0, alpha3=1-k>0,
S=x+y+z, H=1/alpha1+1/alpha2+1/alpha3.

The three equalities at w read

alpha1 w_x=alpha2 w_y=alpha3 w_z=S(w)-1>0.

Consequently S(w)=H(S(w)-1), so H>1. Consider the outer intersection

K={x,y,z>=0; S-alpha1 x<=1; S-alpha2 y<=1; S-alpha3 z<=1}.

P subset K. Multiplying the three pair inequalities by 1/alpha1, 1/alpha2, 1/alpha3 and adding gives

(H-1)S<=H,

so K is bounded. Its intersection with each coordinate plane is exactly the corresponding canonical triangle: on z=0 the CD inequality is x+y<=1 and dominates the other two; on x=0 the BC inequality is y+z<=1 and dominates; on y=0 the BD inequality is x+z<=1 and dominates. All other vertices of K must have strictly positive coordinates and hence satisfy all three pair equalities. Their unique solution is w, since the coefficient determinant is alpha1 alpha2 alpha3 (H-1)>0. Therefore

K=conv(A,B,C,D,w).

The affine function ell is strictly positive at every one of these five points. Its minimum on their convex hull is consequently strictly positive. But F0 subset P subset K, a contradiction.

### 2.4. Case z(w)=0: another five-vertex outer container

If the CD facet were present, the z=0 facet would be exactly ACD, impossible for the noncanonical true vertex w. Thus CD is absent. The normals spanning three dimensions at w must come from z=0, BC and BD. Hence

p w_x+w_y=1, w_x+q w_y=1.

The determinant is nonzero and the exact solution is

w_x=(1-q)/(1-pq), w_y=(1-p)/(1-pq).

Because w_x,w_y>0 and p,q<1, we obtain 1-pq>0. Define

K={x,y,z>=0; p x+y+z<=1; x+q y+z<=1}.

Again P subset K. Take the positive linear combination with weights 1-q and 1-p. It gives

(1-pq)(x+y)+(2-p-q)z<=2-p-q.

All displayed coefficients are positive. Therefore K is bounded and z<=1. On z=0 its section is

Q={x,y>=0; p x+y<=1; x+q y<=1}=conv(A,C,D,w).

For completeness: the first-quadrant polygon has its origin, its two axis endpoints C,D, and its sole possible strictly positive vertex, the intersection w. Boundedness was proved above. These four are true vertices; in particular w_x+w_y-1=(1-p)(1-q)/(1-pq)>0. At height 0<=z<1 the section of K is exactly (1-z)Q, and the section at z=1 consists only of B. Hence

K=conv(A,B,C,D,w).

As in the previous case, positivity of ell at these five vertices contradicts the existence of F0 inside K.

Both cases are impossible. This proves the geometric theorem.

## 3. Stationary proper-33 corollary

The result minimum-0165 supplies H1-H2 for a proper-33 full marked-body/root joint local maximum in the all-positive unbalanced regime when at least one of G(C),G(D) is negative. In particular its ordinary one-mark facets are triangles whose auxiliary base is an actual root minimum-G edge, not an arbitrary nonroot segment.

If such a stationary body is contained in z>=0, the theorem therefore gives

P=conv(T0,F0).

This eliminates the previously recorded proper-33 positive-octant residual consisting of positive-ell auxiliary vertices. It does not eliminate expanded coordinate facets, the negative-z sector, or general all-positive endpoint regimes without the stated stationary classification.

## 4. Trace corollaries and their precise force

### 4.1. Positive octant and sub-a endpoints

Add 0<c,d<a to the stationary hypotheses of section 3. The literal root-only result minimum-0164 applies to the very same actual body and density. It gives

T<203/100<51/25.

No change of centroid, density law, f-vector or incidence is made in this implication. There is no limit on root polygon size and no need to reduce to ten fan classes.

### 4.2. The former b+max(c,d)<=9a/8 stationary residual

Suppose a putative full joint local maximum in the proper-33 negative-anchor regime has T>=51/25 and b+m<=9a/8, m=max(c,d). The negative-z bound in minimum-0165 says that any such body with a point z<0 satisfies

T<3(a+b+m)/(2a+b+m).

For (b+m)/a<=9/8, the right side is at most 51/25 (it is increasing in that ratio). Thus high trace forces P subset {z>=0}.

The actual high-trace endpoint bound from minimum-0111 is

m<943(a+b)/1352.

If m>=a, the assumed b+m<=9a/8 would give b<=a/8 and hence

m<943(9a/8)/1352=(8487/10816)a<a,

a contradiction. Therefore m<a. Section 4.1 now contradicts T>=51/25. There is no such full joint local maximum.

This is a stationary-candidate exclusion. It is NOT by itself a universal trace bound for an endpoint-restricted body class: maximizing within an artificially restricted endpoint sector may produce boundary conditions different from full joint stationarity.

### 4.3. Sharpened remaining stationary map

Every proper-33 negative-anchor full joint high-trace candidate must now satisfy b+max(c,d)>9a/8. If it remains in the nonnegative octant, at least one of c,d must be >=a. The universal endpoint inequality then forces b>409a/943. The other possibility is a genuine negative-z body. These are necessary conditions, not actual realizability claims.

## 5. Global boundary of the advance

This result makes no subtraction from FULL253, the 632 joint graph types, or the 52585 rooted orbits. It does not identify an actual E17 obstruction, improve the lower bound to C>=36, lower the exact attaining C622, or prove the requested minimum. The global accepted bracket remains 34<=C_min<=622. Its significance is that a nontrivial actual-geometric residual is reduced to an already proved root-only value theorem, rather than being closed by a scalar moment relaxation or by sampled f-vectors.
