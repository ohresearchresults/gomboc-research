# minimum-0217

AI research report · 2026-09-24 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# TWO_CAP_PROJECTIVE_TWO_ESCAPE_CHANNELS_AND_EIGHT_VERTEX_EDGE_UNFOLDING_V1

## 1. New result and its scope

**The entire joint epsilon-to-zero boundary has only TWO possible U1 escape channels, at explicitly identified points of a bounded projective chart.** Every other joint degeneration has an all-root, all-SPD U>=2 collar, with no restriction on the relative rates of the actual denominators, the projective parameters or epsilon.

The two points are

```
q_H  = (2280/4039, 0, -1140/577),
q_LR = (280/73, -14/73, 175/146).
```

The first is the known finite heptagonal-cap horizon, c_H=(2/7,0,-1). The second is a genuinely unbounded direction at the side which becomes the L--R face when epsilon=0. They exhaust the possible boundary locations of U1 sequences with epsilon->0; this is not an existence claim for either channel.

More precisely, with the bounded chart q defined below, for **every eta>0 there exists epsilon_eta>0** such that

```
0<epsilon<=epsilon_eta,
1+c.Y_i(epsilon)>0 for every actual vertex,
min(||q-q_H||_2,||q-q_LR||_2)>=eta
```

implies **U>=2 for EVERY SPD**, at the new actual uniformly refilled centroid. This is a whole noncompact parameter-sector theorem: c is unrestricted in size. The proof is analytical and non-effective; no numerical value of epsilon_eta is asserted.

For epsilon tending to a positive value, **all unresolved unbounded projective limits reduce to the reserved eight-vertex heptagonal-pyramid problem**. Directions on the boundary of the actual apex dual cone instead have all-root/all-SPD collars. Thus there is no additional unbounded limiting core in that part of the family.

At the new q_LR channel, a potential U1 sequence must have an affine-normalized limit with **exactly eight true vertices** and a **rank-two limiting metric whose shadow has eight distinct true corners**. If the limit is not a heptagonal pyramid, its maximal facets have a specific hexagonal-base/two-apex form described in section6. Its projected actual-centroid condition reduces to an explicit area equation with a geometrically forced height ratio, not free masses.

A new exact actual control shows that this second residual cannot be discarded by claiming all joint limits have at most seven vertices. An entire genuine E17 sequence with actual denominators bounded below by68/73 tends, after an explicit affine normalization, to a **nonpyramidal8/14/8 uniformly filled body**. That body has an actual eight-corner rank-two shadow and strict -Q/3 containment. The shadow has three strict radial maxima, not one. The full-rank physical control and three finite E17 controls are all446,weak000. They are useful boundary controls, not U1 or110 examples.

**No whole-orbit/all-shape U1 exclusion or actual U1 witness is claimed.** The heptagonal-pyramid area-centroid core is left to the reserved direction. The new nonpyramidal eight-vertex boundary core and the finite positive interior remain separate questions. Bounds34<=C_min<=622 and canonical counts are unchanged.

## 2. Premises, source authority and reading

The authoritative parent is `minimum-0215`, SHA-256 `7e379625c02a74dacfba1f6db9e4e291a8c3e8eecc0e39c90cfd01b879c33242`. Its axial all-root theorem and its literal family are retained, not rechecked or relabelled. The parent explicitly left general unbounded c and joint epsilon0 limits open.

The new analytical input is `[internal-source-reference]`, SEVEN_SHADOW_PSD_REFINEMENT_AND_HORIZON_REDUCTION_V1. I use its accepted conclusions: an actual own-centred uniform body with at most seven true vertices admits no weak rooted system under any nonzero PSD metric, even after adding arbitrary contained labels; and bounded full-dimensional affine-normalized limits of this kind have all-SPD U2 collars. Its rank-three argument uses the accepted universal V>=10 theorem; its rank-two argument uses the completed seven-corner shadow theorem. No fresh replay of those underlying chains is claimed.

The entire updated journal was read consecutively through EOF, including the complete literal parent and recovery capsule; the entire new synthesis was read as well. Mounted input pins are:

```
research-journal(20260923-234831).md
298847 bytes
4671072bfef860a5f7c9d48c1c463d2236be6424bd8217117015c9e2c8c8136a

seven_shadow_psd_refinement_and_horizon_reduction_v1.md
10971 bytes
a371e6d1b8746568424b73e5ed7eac1705dd99cff78d11986a5c785654bab251
```

No source conflict or missing dependency affects the results below. The unproved heptagonal area-centroid statement is a remaining mathematical dependency, not an unavailable file whose contents have been guessed.

## 3. The literal family and an exact bounded chart for ALL c

### 3.1 Unchanged actual incidence

Raw apex Y0=0. In the section z=1 put

```
L=(-1/4,5/4,1), T=(7/2,13/4,1), R=(1/40,27/4,1).
```

For t=(2/5,1/4,3/25,0), in that order,

`b(t)=L+t(R-L)-epsilon*t*(1-t)*(1,0,0)`

gives b1,b2,b3,b4. With s=3/50,

```
b5=L+s(T-L)-epsilon*s*(1-s)*(0,1,0),
b6=T, b7=R.
```

The cone generated by these rays is cut by

```
l7(Y)=z-(2/7)x<=1,
l8(Y)=z+(5/7)x<=1.
```

For i1,...,5, Yi=bi/l7(bi); for i6,7, Yi=bi/l8(bi). Y8 and Y9 are the x=0 intersections of[b5,b6] and[b7,b1], respectively, with exact formula a-a_x(b-a)/(b_x-a_x).

For every0<epsilon<=5 the true maximal facets are

```
F0=(0,2,1)       F1=(0,3,2)       F2=(0,4,3)
F3=(0,5,4)       F4=(0,6,8,5)     F5=(0,7,6)
F6=(0,1,9,7)     F7=(1,2,3,4,5,8,9)
F8=(6,7,9,8).
```

The true edges are

```
01,02,03,04,05,06,07,12,19,23,34,45,58,67,68,79,89.
```

Neither08 nor09 is an edge. Triangle089 is an internal interface. Positive projectivities preserve this full lattice, because the transformed slack is the old slack divided by its positive actual denominator.

Every actual centroid in this result is obtained from positive volume tetrahedra, never chosen vertex weights. For a cap fan triangle(i,j,k), the transformed six-volume is det(Yi,Yj,Yk)/(d_i d_j d_k), d_i=1+c.Y_i. With Z_i=Y_i/d_i,

```
D=sum d_ijk=6Vol,
g_c=sum d_ijk*(Z_i+Z_j+Z_k)/(4D).
```

The poles are the actual same-origin poles after subtracting g_c. These are the parent’s exact uniform-refill conventions.

### 3.2 Interior reference used ONLY to compactify parameters

Let

```
w=(Y4+Y6+Y7)/4=(451/2280,1741/798,366/665).
```

This is the barycentre of the fixed tetrahedron0,Y4,Y6,Y7, not a mechanical centre of mass. Every P_epsilon contains this tetrahedron. Indeed the section contains the fixed triangle LTR; moreover P0 subset P_epsilon subset P5. Thus the source bodies have a common interior ball about w and a common bound.

For every admissible c define

```
a=1+c.w>0,
q=c/a,
R_c=(I-w q^T)/a.
```

There is an exact affine identity

```
T_c(Y)=w/a+R_c T_q(Y-w),
T_p(X)=X/(1+p.X),
det(R_c)=a^-4>0.
```

The inverse parameter change is c=q/(1-q.w). Positivity of all denominators is equivalent in the two charts. In particular the apex condition is1-q.w>0.

If P0-w contains a ball of radius r, positivity implies ||q||<1/r. Hence **all general c, including unbounded c, are represented in one bounded q-domain**. This is an affine equivalence between the two uniformly refilled images, not transport of the old centroid. Their actual new centroids and volumes satisfy

```
g_c=w/a+R_c g_q,
Vol(T_c P)=a^-4 Vol(T_q(P-w)).
```

On centred vectors the physical metric transforms to R_c^T M R_c, and its reciprocal transforms to R_c^-1 N R_c^-T. No independently centred polar system is introduced.

## 4. New all-rate source/face-label limit theorem

This lemma is useful beyond the present family.

**Theorem.** Let P_n=conv(Y_1,n,...,Y_N,n) be genuine uniformly filled full-dimensional bodies, with a fixed finite number of retained labels, Y_i,n->Y_i,0, and P0 full-dimensional. Choose w in int(P0), and suppose the actual positive projective parameters in the w-chart converge to q_*, a boundary point of the positive domain of P0-w. Let F be the exposed face

`F={Y in P0:1+q_*.(Y-w)=0}`,

and let m(F) count ALL limiting labels in F, including nonextreme ones. There are invertible affine normalizations and a subsequence for which every label converges, the limit hull K is bounded and full-dimensional, and

```
F a facet:   number of true vertices(K)<=m(F)+1;
F an edge:   number of true vertices(K)<=m(F)+2;
F a vertex: number of true vertices(K)<=m(F)+deg_P0(F).
```

Consequently any of these upper bounds<=7 gives an all-root/all-SPD U2 collar. Source incidence may change or collapse in the limit. No comparison between denominator rates and source-shape rates is assumed.

### Proof of the normalization and counts

Write X_i,n=Y_i,n-w, f_i,n=1+q_n.X_i,n, and Z_i,n=X_i,n/f_i,n. The transformed bodies contain a common ball about0. For example, if the sources contain the radius-r ball and ||q_n||<=1/r, the transformed bodies contain the radius-r/3 ball, by the inverse map z/(1-q_n.z).

Choose a maximum-volume tetrahedron among the actual transformed vertex labels. Map its four vertices to0,e1,e2,e3 by an invertible affine map

`U_i,n=A_n Z_i,n+b_n`.

Replacing any one of the tetrahedron’s vertices shows that every barycentric coordinate of every label has absolute value<=1. Thus all U_i,n lie in[-1,1]^3, and their hull contains the fixed standard tetrahedron. The image of the common ball shows A_n is uniformly bounded; b_n is bounded because0 belongs to the transformed body. Pass to a subsequence with all U_i,n, A_n and b_n convergent, to U_i, A and b. The hull K is full-dimensional.

For every label in F,

`A_n X_i,n=f_i,n*(U_i,n-b_n)->0`,

hence A annihilates span(F-w), whose dimension is dim(F)+1. Every label outside F has the limit

`U_i=b+A*(Y_i,0-w)/(1+q_*.(Y_i,0-w))`.

For a facet, A=0, so all outside labels become ONE point. For an edge, rank(A)<=1, so their hull is an interval or a point, contributing at most TWO vertices.

For a vertex v, put f_i=q_*.(Y_i,0-v)>0 for outside labels. Since A(v-w)=0, their hull is an affine image of

`conv{(Y_i,0-v)/f_i:i outside F}`.

This is exactly the transverse section q_*.u=1 of the true tangent cone of P0 at v. Its extreme rays are the actual edges incident to v; its section has deg_P0(v) vertices. Adding the m(F) remaining arbitrary label limits proves the third count.

### Why the conclusion is an unrestricted physical collar

Each normalized body is uniformly filled. Its bounded full-dimensional convex limit has the uniform volume law of K: volume and first moments converge, so the **new actual centroids** converge to g_K. This also follows by dominated convergence of the bounded convex-body indicators, since the limit boundary has volume zero.

If an approaching sequence had U1, choose a recurring rooted true-edge escape tree, transport each metric to the normalized coordinates as A_n^-T M_n A_n^-1, and normalize its trace to1. A subsequence tends to a nonzero PSD matrix. Every selected arrow tends to a weak arrow on the FULL retained label set, centred at g_K. The supplied seven-vertex PSD/refinement theorem contradicts this whenever K has<=7 true vertices.

In particular collapsed labels are not deleted from a putative rooted system. The proof includes arbitrary conditioning, finite zero-arrow walls and extra physical weak contacts. The collar is an existence theorem, not an evaluated radius.

## 5. Complete application to the two-cap noncompact boundary

### 5.1 Unbounded c with epsilon approaching a positive value

Take epsilon_n->epsilon_bar>0, ||c_n||->infinity, and c_n/||c_n||->d. Positivity forces d into the dual of the true apex cone C_epsilon_bar. Also d.w>0 and q_n->d/(d.w). Its exposed face is P_epsilon_bar intersect{d.Y=0} and contains apex0.

If d is on the boundary of that dual cone, the exposed face is a true apex edge or a true lateral facet. Such a facet is a triangle or quadrilateral. The new lemma gives a tetrahedral or at-most-five-vertex full-dimensional normalized limit, hence **all-root/all-SPD U2 collars**, for arbitrary subleading parameters and denominator ratios.

If d is in the interior of the dual cone, the explicit normalization by ||c_n|| gives

`||c_n|| T_c_n(Y_i,n)->Y_i,bar/(d.Y_i,bar)`

for every nonzero label; apex0 stays0. The seven ray endpoints give the true heptagonal section of C_epsilon_bar by d.Y=1. The two seam labels become nonextreme points on its boundary. The limit is exactly an eight-vertex heptagonal pyramid.

For a U1 sequence, a rank-three limiting metric is excluded by the accepted V>=10 theorem, rank one by the two interval endpoint fibres, and rank two with<=7 shadow corners by the new shadow theorem. The sole remaining possibility is the reserved rank-two/eight-corner pyramid shadow with projected apex a and projected base heptagon B satisfying **a+3c_B=0**, where c_B is its actual AREA centroid. This is the source’s unresolved core, not a newly claimed exclusion.

Thus the complete unbounded fixed-positive-epsilon problem reduces to that one geometric core; boundary directions of the dual cone do not create another core.

### 5.2 The actual epsilon0 body and ALL its label strata

At epsilon0 the hull is a genuine triangular prism with true vertices labelled

```
0=(0,0,0),
4=(-7/30,7/6,14/15),
6=(1,13/14,2/7),
7=(7/285,126/19,56/57),
8=(0,83/60,1),
9=(0,25/4,1).
```

Its true(V,E,F) is6/9/5 and its actual volume is55699/51300. Epsilon0 is a limit body, not an E17 member. All ten old labels have distinct limits;1,2,3 lie inside edge4--9, and5 lies inside edge4--8.

The complete facet-label disposition is

|True facet of P0|All old labels lying in it|Limit vertex bound|Disposition|
|---|---|---:|---|
|LR: (0,4,9,7)|0,1,2,3,4,7,9|8|Residual|
|LT: (0,6,8,4)|0,4,5,6,8|6|All-SPD collar|
|TR: (0,7,6)|0,6,7|4|All-SPD collar|
|Heptagonal-cap limit: (4,8,9)|1,2,3,4,5,8,9|8|Residual|
|Other cap: (6,7,9,8)|6,7,8,9|5|All-SPD collar|

All six true prism vertices are simple and carry one label, giving bound4. Edge4--9 carries five labels and gives bound7; edge4--8 carries three and gives bound5. The other seven true edges

`04,06,07,67,68,79,89`

carry only their two endpoints and give bound4. These are all face strata of the actual limiting prism, not a sampled list. An interior q-limit instead gives the six-vertex projective image of P0 and is also excluded.

The two exceptional facet parameters are exactly

```
c_H=(2/7,0,-1),
q_H=c_H/(1+c_H.w)=(2280/4039,0,-1140/577);

n_LR=(20/73,-1/73,25/292),
n_LR.w=1/14,
q_LR=n_LR/(n_LR.w)=(280/73,-14/73,175/146).
```

Here n_LR is the T-coordinate covector in the basis(L,T,R). It vanishes on the LR face. Every face-label membership and both points are regenerated exactly in the source.

### 5.3 Uniform two-point localization

The closed q-domain of P0-w is compact. If the theorem in section1 failed for some eta, there would be U1 bodies with epsilon_n->0 and q_n a distance at least eta from both exceptional points. Take a convergent q-subsequence. Its limit is interior or exposes one of the covered prism strata, contradicting the source/face-label limit theorem. This proves the claimed epsilon_eta sector for **all c at once**.

Equivalently, every U1 sequence with epsilon->0 has a subsequence in one of these two channels:

```
A. c->c_H (finite heptagonal-cap horizon);
B. ||c||->infinity and c/||c||->n_LR/||n_LR||.
```

No other finite horizon or unbounded direction is possible. In channelB the argument allows epsilon*||c|| to tend to zero, a finite value or infinity, and permits additional denominator-rate hierarchies. The explicit example below occupies one finite-product regime, not the entirety of that channel.

## 6. Exact residual at the LR channel

All labels outside the LR face, namely5,6,8, have ONE common normalized limit, denoted *. If there are at most seven true limit vertices, the collar theorem already closes the sequence. Otherwise the eight points

`{0,1,2,3,4,7,9,*}`

must all be distinct true vertices. A possible limiting weak-rooted metric must have rank two and project all eight to distinct true shadow corners.

The inherited capF7 makes the six points

`B=(1,2,3,4,*,9)`

coplanar on a supporting plane. If0 or7 joins this plane, K is an eight-vertex heptagonal pyramid and returns to the reserved core. Otherwise B is a **true hexagonal maximal facet**, with0 and7 strictly outside it.

In this nonpyramidal case, the only possible maximal-facet lists are

```
(0,2,1), (0,3,2), (0,4,3),
(0,*,4), (0,7,*), (0,1,9,7),
B=(1,2,3,4,*,9), (*,7,9),
```

or the single cofacial merger of(0,*,4) and(0,7,*) into(0,7,*,4). The first has8/14/8; the merged possibility has8/13/7. The unmerged case is actually realized below; realization of the merged possibility is not asserted.

To justify completeness, normalize each inherited facet’s normal and pass to a limit. All eight points are extreme, so any three distinct ones are noncollinear. The hexagonal cap is a genuine facet. Its intersection with any other facet is a true edge, so no other base vertex can join a listed side triangle. The quadrilateral(0,1,9,7) and triangle(*,7,9) remain distinct. They and the supporting triangle(0,7,*) make07 a true edge with its two incident maximal planes. These incidence restrictions leave only the stated merger. Limits of the original finitely many boundary facets cover the limit boundary, so there is no additional unlisted facet.

The retained source graph contracts to the fourteen pairs

```
01,02,03,04,0*,07,12,19,23,34,4*,7*,79,9*.
```

If the merger occurs,0* is a diagonal in the limiting maximal facet, **not a mechanical edge of K**. It is still a permissible limit of original true edges05/06. Thus continuation must test the retained source-label weak system, not silently replace it by a smaller limiting mechanical graph. The seven-vertex/refinement argument was deliberately formulated on all contained labels to avoid this error.

### A forced-height actual area equation for the nonpyramidal residual

Let the rank-two projection send0 to a,7 to b,* to z, and i to p_i for i=1,2,3,4,9. All eight are true corners of Q. The projection restricted to B is bijective; otherwise its six vertices give at most two shadow corners and the entire shadow has at most four.

Choose a vertical coordinate which makes the actual base plane B height0, and rescale the height of a to1. The true quadrilateral(0,1,9,7) forces

```
r=height(b)/height(a)=ell(b)/ell(a)>0,
```

where ell is any nonzero affine function vanishing on line p1--p9. Its denominator is nonzero because all eight projected points are true corners. There is no independent second height parameter.

Let A_B and c_B be the actual planar area and area centroid of the projected hexagon B, and define

```
J=abs(cross2(b-z-r*(a-z), p9-z)).
```

The true fan from a has exactly two pieces: the pyramid over the full hexagon and the tetrahedron over the true triangle(z,b,p9). In this affine lift frame, at height H>0 their volumes are H*2A_B/6 and H*J/6; the constant Jacobian back to the original frame cancels from both volume fractions. Their volume fractions and projected centroid therefore satisfy

```
lambda_B=2A_B/(2A_B+J),

2A_B*(a+3c_B)+J*(a+z+b+p9)=0.                 (AREA)
```

The actual height centroid is

`H*[2A_B+(1+r)J]/[4(2A_B+J)]`.

Equation(AREA) is an exact necessary condition at the physical projected origin. It uses the full hexagonal AREA centroid and the true common volume fractions. It is not an equation with chosen masses or the area centroid of Q.

Conversely, planar data satisfying this equation can be lifted as(B,0),(a,1),(b,r); if the complete support checks give one of the listed true facet lattices, its actual projected volume centroid is0. A weak-rooted claim still requires the full retained arrow test. This gives a concrete actual-height completion problem for the new residual, not a solved U1 construction or an all-shape exclusion.

## 7. Exact joint-rate body: why the eight-vertex exception is real

Let B0 denote the3x3 matrix with columns L,T,R:

```
B0=((-1/4,7/2,1/40),
    (5/4,13/4,27/4),
    (1,1,1)),      det(B0)=803/40.
```

Its T-coordinate row is n_LR. For **every0<epsilon<=5**, take

```
c_epsilon=n_LR/epsilon,
A_epsilon=diag(1,1/epsilon,1)*B0^-1,
K_epsilon=A_epsilon T_c_epsilon(P_epsilon).
```

All actual projective denominators obey **d_i>=68/73**. For the three bowed LR rays, the T-coordinate is -epsilon*a(t), a(t)=(20/73)t(1-t)<=5/73, and l7(b_i)>=1. Their denominators are1-a(t)/l7(b_i). The seam9 is a convex combination of b1 and R in z=1, giving the same bound. The T-coordinates at5,6,8 are positive;4 and7 have denominator1. This proves positivity on the entire stated interval, hence the full genuine E17 lattice throughout, not just at the sampled controls.

Nevertheless c_epsilon is unbounded, and

`q_epsilon=n_LR/(epsilon+1/14)->q_LR`.

Thus a lower bound on the original actual denominators does **not** compactify this orbit about its boundary-vertex origin.

For t=(2/5,1/4,3/25,0), put

```
a(t)=(20/73)t(1-t),
f(t)=15/14-(11/140)t-a(t),
v(t)=(1-t,-a(t),t)/f(t).
```

The exact normalized limit K has the following eight vertices, in NEW indices0,...,7:

```
0=(0,0,0)
1=(1095/1778,-60/889,365/889)
2=(30660/40897,-2100/40897,10220/40897)
3=(32120/37707,-352/12569,1460/12569)
4=(14/15,0,0)
5=(0,0,56/57)
6=(73/795,-8/795,146/159)
7=(0,1,0).
```

The complete old-to-new limit map is

`(0,1,2,3,4,7,7,5,7,6)`.

In particular new7 is the common limit of old5,6,8; it is NOT the old degree-seven label. Exact symbolic limits verify all ten coordinates. K is the unmerged true8/14/8 body, not a formal mass or Gram object.

Its actual volume and centroid are

```
V_K=1488190557267134/8874811505660895,
g_K=(129734023844794881073516883/529015888818803968594157355,
     490554351878457488063841593/2116063555275215874376629420,
     172015029197184492686704244/670086792503818360219265983).
```

Actual normalized centroids converge to this g_K. In the unnormalized projective frame,

`Vol(T_c_epsilon P_epsilon)/epsilon -> (803/40)*V_K`.

No transported old centroid is used.

### Genuine eight-corner shadow

Project K-g_K by

```
Lproj=((1,0,-27/10),(0,1,1/5)).
```

All eight projected points are distinct true corners, in counterclockwise NEW-index order

`(7,5,6,1,0,2,3,4)`.

Every nonincident convexity determinant is positive; the minimum is584584/1542103179. Strict -Q/3 containment is verified with minimum edge determinant

`2151653625942844060731884/861540161790623605996199121>0`.

The rank-two metric is Lproj^T Lproj. This shadow has three strict radial maxima, new7,5,4. It is **not weak-rooted** and is not a singular U1 witness. It shows that neither a seven-vertex count nor a seven-shadow-corner count automatically closes the LR channel.

For this same actual shadow the forced height ratio is7/285, and

```
A_B=5840039707474/3459965499283,
J=25112/75525,
lambda_B=1325590408275/1456155144097.
```

The source verifies(AREA), identifies c_B with the projected actual full-facet mean, and matches lambda_B to the actual three-dimensional cap-fan volume fraction.

### Full reciprocal controls, not merely singular counts

Use the SAME rational SPD in the normalized coordinates,

```
M=((13,2,1),(2,11,3),(1,3,17)), N=M^-1.
```

All four controls have strict(S,U,H)=446,physicalweak000. Complete labelled censuses are:

|Body|S facets|U vertices|True H edges|
|---|---|---|---|
|K, NEW indices|3,4,5,6|0,4,5,7|04,05,07,16,47,57|
|K_(1/4), old E17 indices|4,5,6,8|0,4,6,7|04,06,07,19,67,68|
|K_(1/64), old E17 indices|3,5,6,7|0,4,6,7|04,06,07,19,45,67|
|K_(1/1024), old E17 indices|3,5,6,7|0,4,6,7|04,06,07,19,45,67|

All **260** reciprocal true-edge primitives are nonzero. Each body has its own actual volume centroid, full maximal-facet hull, true edges and actual same-origin poles. Two positive volume fans agree through second moments. The original projective-frame physical metric is A_epsilon^T M A_epsilon, with its literal reciprocal. No continuous weak-free mechanical census between the sampled controls is asserted.

## 8. What was tried, what failed, and the useful next step

The main change of formulation was to compactify general projectivity by a fixed interior reference, while transporting the **new uniformly refilled body** affinely. Maximum-volume-tetrahedron normalization then converted arbitrary rate hierarchies into a count of all labels in one exposed face of the limiting source. This avoided both a new search over the already closed axial metrics and an unsupported assumption that source-shape and denominator limits commute.

The useful failed simplification is now exact: the epsilon0 prism has only six true vertices, but its long side and one cap each carry seven retained labels. Projective magnification can preserve the bowed chain and produce a genuine nonpyramidal eight-vertex solid with an actual eight-corner shadow. Simply applying the six-vertex theorem to the untransformed prism, or discarding its edge-interior labels before passing to the limit, would be wrong.

The next concrete connection is the all-root weak-arrow problem for the hexagonal/two-apex residual with its forced r and exact(AREA), retaining the fourteen source-quotient pairs even at the one allowed cofacial merger. The reserved heptagonal-pyramid problem separately controls the other residual and generic unbounded limits with positive epsilon. Neither result by itself excludes finite-distance SPD components in the original positive interior. No unsuccessful numerical search is offered as an exclusion.

## 9. Complete runnable recovery and author execution

The single complete source below reconstructs the actual family inputs, all limiting label memberships, both exceptional chart points, all ten symbolic limits, the true8/14/8 control, its actual eight-corner shadow and area/volume identity, and the three finite own-centred E17 reciprocal controls. It imports no parent source, stress table, cache, optimizer or external data.

Executed environment: **CPython3.13.5, SymPy1.14.0**, assertions enabled. Fraction arithmetic handles all geometry, moments and signs; SymPy is used only for the ten exact one-variable coordinate limits. A floating planar projection locator was used to locate the displayed rational Lproj; its output is frozen literally and all claimed properties are proved again exactly by this source. No search-success rate or failed-search inference is used.

The author build and a source-only fresh-directory build/check completed. Reports and stdout matched byte-for-byte. These checks concern the new controls and algebra, not a computational proof of the all-rate analytical collar theorem and not an independent implementation of the supplied seven-shadow theorem.

Save the following fence as `twocap_escape_channels.py`, retaining its final LF:

```sh
python -B twocap_escape_channels.py build > build.stdout
python -B twocap_escape_channels.py check > check.stdout
cmp build.stdout check.stdout
```

Do not use -S: the symbolic-limit check imports SymPy. Do not disable assertions.

|Object|Bytes|SHA-256|
|---|---:|---|
|twocap_escape_channels.py|11658|7f0f2b7aa4991ac85ef5bf07ac1c39b4d566dc7eb71f92e2344769220ff72eed|
|twocap_escape_channels.json|113426|164fec5747183eebe78fd6f9582c1d3766db9d5a5d297c80e6032a39ab2f1d78|
|identical build/check stdout|965|2d7356330c4f7ed730cfa47e73ee23a8f1975c2d70be5c28c0124df8a3c5a200|

Principal observed markers:


[Encoded source block omitted; the code in this passage is incomplete.]


### Autonomous source

```python
#!/usr/bin/env python3
"""Exact controls for the joint epsilon/projective two-channel reduction.
CPython 3.13.5, SymPy 1.14.0, assertions enabled. No parent source is imported.
Run: python -B twocap_escape_channels.py build|check
The all-rate collar and maximum-simplex arguments are analytical, not sampled.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json,sys

PARENT='minimum-0215'
PARENT_SHA='7e379625c02a74dacfba1f6db9e4e291a8c3e8eecc0e39c90cfd01b879c33242'
FACETS=((0,2,1),(0,3,2),(0,4,3),(0,5,4),(0,6,8,5),(0,7,6),(0,1,9,7),(1,2,3,4,5,8,9),(6,7,9,8))
LIMIT_FACETS=((0,2,1),(0,3,2),(0,4,3),(0,7,4),(0,5,7),(0,1,6,5),(1,2,3,4,7,6),(5,6,7))
CORE_FACETS=((0,1,5,3),(0,2,4,1),(0,3,2),(1,4,5),(2,3,5,4))
TIMES=(F(2,5),F(1,4),F(3,25),F(0))
OLD_TO_LIMIT=(0,1,2,3,4,7,7,5,7,6)
I=tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
B=((F(-1,4),F(7,2),F(1,40)),(F(5,4),F(13,4),F(27,4)),(F(1),F(1),F(1)))
M=((F(13),F(2),F(1)),(F(2),F(11),F(3)),(F(1),F(3),F(17)))
PROJ=((F(1),F(0),F(-27,10)),(F(0),F(1),F(1,5)))

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(t,a):return tuple(t*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def cross2(a,b):return a[0]*b[1]-a[1]*b[0]
def det(a,b,c):return dot(a,cross(b,c))
def tr(A):return sum(A[i][i] for i in range(len(A)))
def trans(A):return tuple(zip(*A))
def mv(A,a):return tuple(dot(r,a) for r in A)
def mm(A,B):return tuple(tuple(dot(r,c) for c in trans(B)) for r in A)
def outer(a,b):return tuple(tuple(x*y for y in b) for x in a)
def ma(A,B):return tuple(add(r,s) for r,s in zip(A,B))
def ms(t,A):return tuple(scale(t,r) for r in A)
def inv(A):
 d=det(*A);assert d
 return tuple(scale(1/d,r) for r in trans((cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))))
def minors(A):return (A[0][0],A[0][0]*A[1][1]-A[0][1]**2,det(*A))
def pd(A):assert A==trans(A) and min(minors(A))>0

def source(e):
 L=(F(-1,4),F(5,4),F(1));T=(F(7,2),F(13,4),F(1));R=(F(1,40),F(27,4),F(1))
 rays=[sub(add(L,scale(t,sub(R,L))),(e*t*(1-t),0,0)) for t in TIMES]
 s=F(3,50);rays += [sub(add(L,scale(s,sub(T,L))),(0,e*s*(1-s),0)),T,R]
 Y=[(F(0),)*3]+[scale(1/(1+a*b[0]),b) for a,b in zip([F(-2,7)]*5+[F(5,7)]*2,rays)]
 for a,b in ((rays[4],rays[5]),(rays[6],rays[0])):
  Y.append(sub(a,scale(a[0]/(b[0]-a[0]),sub(b,a))))
 return Y

def supports(Y,cycles):
 out=[];edges={}
 for f,cyc in enumerate(cycles):
  n=cross(sub(Y[cyc[1]],Y[cyc[0]]),sub(Y[cyc[2]],Y[cyc[0]]));assert any(n)
  h=dot(n,Y[cyc[0]]);v=[dot(n,y)-h for y in Y]
  assert all(v[i]==0 for i in cyc)
  if any(t>0 for t in v):n=scale(-1,n);h=-h;v=[-t for t in v];cyc=tuple(reversed(cyc))
  assert all(v[i]<0 for i in range(len(Y)) if i not in cyc)
  for j,a in enumerate(cyc):
   b=cyc[(j+1)%len(cyc)];c=cyc[(j+2)%len(cyc)]
   assert dot(n,cross(sub(Y[b],Y[a]),sub(Y[c],Y[b])))>0
   edges.setdefault(tuple(sorted((a,b))),[]).append(f)
  out.append((cyc,n,h))
 found=set()
 for i,j,k in combinations(range(len(Y)),3):
  n=cross(sub(Y[j],Y[i]),sub(Y[k],Y[i]))
  if not any(n):continue
  h=dot(n,Y[i]);v=[dot(n,y)-h for y in Y]
  if all(t<=0 for t in v) or all(t>=0 for t in v):found.add(frozenset(l for l,t in enumerate(v) if not t))
 assert found=={frozenset(c) for c,n,h in out}
 assert all(len(fs)==2 for fs in edges.values()) and len(Y)-len(edges)+len(out)==2
 return out,edges

def moments(Y,faces,o):
 D=F(0);J=(F(0),)*3;T=((F(0),)*3,)*3
 for cyc,n,h in faces:
  for k in range(1,len(cyc)-1):
   verts=(o,Y[cyc[0]],Y[cyc[k]],Y[cyc[k+1]])
   d=det(*(sub(v,o) for v in verts[1:]));assert d>=0
   S=tuple(sum(v[j] for v in verts) for j in range(3));Z=outer(S,S)
   for v in verts:Z=ma(Z,outer(v,v))
   D+=d;J=add(J,scale(d,S));T=ma(T,ms(d,Z))
 assert D>0
 return D/6,scale(1/(4*D),J),ms(1/(20*D),T)

def audit(Y,cycles,metric):
 faces,edges=supports(Y,cycles);o=scale(F(1,len(Y)),tuple(sum(y[j] for y in Y) for j in range(3)))
 V,g,T=moments(Y,faces,o);assert moments(Y,faces,Y[0])==(V,g,T)
 X=[sub(y,g) for y in Y]
 assert moments(X,[(c,n,h-dot(n,g)) for c,n,h in faces],(F(0),)*3)[1]==(0,0,0)
 pd(metric);N=inv(metric);pd(N);assert mm(metric,N)==I
 assert all(h-dot(n,g)>0 for c,n,h in faces)
 poles=[scale(1/(h-dot(n,g)),n) for c,n,h in faces]
 P={};Q={};pack=[]
 for (a,b),(f,h) in sorted(edges.items()):
  p=dot(X[a],mv(metric,sub(X[b],X[a])));pp=dot(X[b],mv(metric,sub(X[a],X[b])))
  q=dot(poles[f],mv(N,sub(poles[h],poles[f])));qq=dot(poles[h],mv(N,sub(poles[f],poles[h])))
  P[a,b]=p;P[b,a]=pp;Q[f,h]=q;Q[h,f]=qq;pack.append((a,b,f,h,p,pp,q,qq))
 U=[i for i in range(len(Y)) if all(v<0 for (a,b),v in P.items() if a==i)]
 S=[i for i in range(len(faces)) if all(v<0 for (a,b),v in Q.items() if a==i)]
 H=[(a,b) for a,b,f,h,*v in pack if max(v)<0]
 zeros=[(a,b,j) for a,b,f,h,*v in pack for j,t in enumerate(v) if t==0]
 weak=[(a,b) for a,b,f,h,*v in pack if max(v)==0]
 assert not zeros and not weak and len(S)+len(U)-len(H)==2
 return dict(vertices=Y,facets=[c for c,n,h in faces],supports=[(n,h) for c,n,h in faces],
  edges=sorted(edges),fvector=(len(Y),len(edges),len(faces)),volume=V,centroid=g,second=T,
  M=metric,N=N,poles=poles,S=S,U=U,H=H,weak=(0,0,0),packets=pack)

def limit_vertices():
 out=[(F(0),)*3]
 for t in TIMES:
  a=F(20,73)*t*(1-t);d=F(15,14)-F(11,140)*t-a
  out.append(((1-t)/d,-a/d,t/d))
 return out+[(F(0),F(0),F(56,57)),(F(73,795),-F(8,795),F(146,159)),(F(0),F(1),F(0))]

def convex_cycle(Q,cycle):
 guards=[]
 for i,a in enumerate(cycle):
  b=cycle[(i+1)%len(cycle)];e=sub(Q[b],Q[a])
  for j in cycle:
   if j not in (a,b):guards.append(cross2(e,sub(Q[j],Q[a])))
 assert min(guards)>0
 return guards

def area_centroid(Q,cycle):
 A=F(0);C=(F(0),F(0));z=Q[cycle[0]]
 for i in range(1,len(cycle)-1):
  a,b=Q[cycle[i]],Q[cycle[i+1]];w=cross2(sub(a,z),sub(b,z))/2
  A+=w;C=add(C,scale(w,add(add(z,a),b)))
 assert A!=0
 return abs(A),scale(1/(3*A),C)

def shadow_check(K,record):
 Q=[mv(PROJ,sub(y,record['centroid'])) for y in K]
 cyc=(7,5,6,1,0,2,3,4);guards=convex_cycle(Q,cyc)
 reflected=[cross2(sub(Q[cyc[(i+1)%8]],Q[a]),sub(scale(F(-1,3),Q[j]),Q[a])) for i,a in enumerate(cyc) for j in range(8)]
 assert min(reflected)>0
 local=[i for k,i in enumerate(cyc) if dot(Q[i],sub(Q[cyc[k-1]],Q[i]))<0 and dot(Q[i],sub(Q[cyc[(k+1)%8]],Q[i]))<0]
 assert len(local)>=2
 base=(1,2,3,4,7,6);A,C=area_centroid(Q,base);a,b,z,p1,p9=[Q[i] for i in (0,5,7,1,6)]
 ell=lambda p:cross2(sub(p9,p1),sub(p,p1))
 ratio=ell(b)/ell(a);assert ratio>0
 J=abs(cross2(sub(sub(b,z),scale(ratio,sub(a,z))),sub(p9,z)))
 assert J>0
 balance=add(scale(2*A,add(a,scale(3,C))),scale(J,add(add(a,z),add(b,p9))))
 assert balance==(0,0)
 faces,_=supports(K,LIMIT_FACETS)
 v1,g1,_=moments(K,[faces[6]],K[0]);v2,g2,_=moments(K,[faces[7]],K[0])
 assert v1+v2==record['volume'] and v1/record['volume']==2*A/(2*A+J)
 capmean=scale(F(1,3),sub(scale(4,g1),K[0]))
 assert mv(PROJ,sub(capmean,record['centroid']))==C
 rootmetric=mm(trans(PROJ),PROJ)
 assert det(*rootmetric)==0 and min(rootmetric[0][0],rootmetric[0][0]*rootmetric[1][1]-rootmetric[0][1]**2)>0
 return dict(projection=PROJ,rank2_metric=rootmetric,points=Q,cycle=cyc,strict_radial_maxima=local,
  convexity_margin=min(guards),reflection_margin=min(reflected),base_area=A,base_centroid=C,
  height_ratio=ratio,J=J,cap_volume_fraction=2*A/(2*A+J),centroid_balance=balance)

def symbolic_limits(K):
 import sympy as s
 e=s.symbols('e',positive=True);Y=source(e);BB=s.Matrix(B);nn=BB.inv()[1,:]
 A=s.diag(1,1/e,1)*BB.inv();lims=[]
 for i,y in enumerate(Y):
  v=s.Matrix(y);z=A*v/(1+(nn*v)[0]/e)
  lim=tuple(F(s.limit(s.cancel(t),e,0)) for t in z)
  assert lim==K[OLD_TO_LIMIT[i]]
  lims.append(lim)
 return lims

def core_data():
 Y=source(F(0));ids=(0,4,6,7,8,9);Z=[Y[i] for i in ids];faces,edges=supports(Z,CORE_FACETS)
 face_labels=[]
 for cyc,n,h in faces:
  face_labels.append(tuple(i for i,y in enumerate(Y) if dot(n,y)==h))
 assert sorted(len(v) for v in face_labels)==[3,4,5,7,7]
 edge_labels=[]
 for a,b in sorted(edges):
  u,v=Z[a],Z[b];d=sub(v,u);k=next(k for k in range(3) if d[k]);hit=[]
  for i,y in enumerate(Y):
   t=(y[k]-u[k])/d[k]
   if 0<=t<=1 and add(u,scale(t,d))==y:hit.append(i)
  edge_labels.append((ids[a],ids[b],tuple(hit)))
 assert sorted(len(v) for a,b,v in edge_labels)==[2]*7+[3,5]
 w=scale(F(1,4),add(add(Y[4],Y[6]),Y[7]));n=inv(B)[1]
 ch=(F(2,7),F(0),-F(1));qh=scale(1/(1+dot(ch,w)),ch);ql=scale(1/dot(n,w),n)
 assert w==(F(451,2280),F(1741,798),F(366,665)) and dot(n,w)==F(1,14)
 assert qh==(F(2280,4039),0,-F(1140,577)) and ql==(F(280,73),-F(14,73),F(175,146))
 V,g,T=moments(Z,faces,w)
 return dict(vertex_labels=ids,vertices=Z,facets=[tuple(ids[i] for i in c) for c,n,h in faces],
  face_labels=face_labels,edge_labels=edge_labels,fvector=(6,9,5),volume=V,centroid=g,w=w,n_LR=n,q_H=qh,q_LR=ql)

def construct():
 core=core_data();K=limit_vertices();lim=audit(K,LIMIT_FACETS,M)
 assert lim['fvector']==(8,14,8)
 lim['old_to_limit']=OLD_TO_LIMIT;lim['all_ten_limits']=symbolic_limits(K)
 lim['shadow']=shadow_check(K,lim)
 finite=[]
 for e in (F(1,4),F(1,64),F(1,1024)):
  Y=source(e);n=core['n_LR'];c=scale(1/e,n);ds=[1+dot(c,y) for y in Y]
  assert min(ds)>=F(68,73)
  A=ma(I,ms(1/e-1,((F(0),)*3,(F(0),F(1),F(0)),(F(0),)*3)));A=mm(A,inv(B))
  W=[mv(A,scale(1/d,y)) for d,y in zip(ds,Y)]
  r=audit(W,FACETS,M);assert r['fvector']==(10,17,9)
  r.update(epsilon=e,c=c,denominators=ds,normalizer=A)
  q=scale(1/(1+dot(c,core['w'])),c);aa=1+dot(c,core['w'])
  R=ms(1/aa,ma(I,ms(-1,outer(core['w'],q))))
  ZZ=[scale(1/(1+dot(q,sub(y,core['w']))),sub(y,core['w'])) for y in Y]
  for y,z in zip(Y,ZZ):assert add(scale(1/aa,core['w']),mv(R,z))==scale(1/(1+dot(c,y)),y)
  zfaces,_=supports(ZZ,FACETS);vz,gz,tz=moments(ZZ,zfaces,ZZ[0])
  transformed_g=mv(A,add(scale(1/aa,core['w']),mv(R,gz)))
  assert transformed_g==r['centroid'] and det(*R)==1/aa**4
  r['compact_q']=q;r['raw_projective_volume']=r['volume']/det(*A)
  r['raw_projective_centroid']=mv(inv(A),r['centroid']);finite.append(r)
 assert 4*(len(lim['packets'])+sum(len(r['packets']) for r in finite))==260
 return dict(version=1,identity='TWO_CAP_PROJECTIVE_TWO_ESCAPE_CHANNELS_V1',parent=PARENT,parent_sha=PARENT_SHA,
  core=core,limit=lim,finite_controls=finite,limit_volume_over_epsilon=det(*B)*lim['volume'])

def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encode(v) for v in x]
 return x

def main():
 assert __debug__ and sys.version_info>=(3,10)
 if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):raise SystemExit('build|check required')
 r=construct();raw=(json.dumps(encode(r),sort_keys=True,indent=2)+'\n').encode();p=Path('twocap_escape_channels.json')
 if sys.argv[1]=='build':p.write_bytes(raw)
 else:assert p.read_bytes()==raw
 print('EXACT_SIX_VERTEX_PRISM_AND_ALL_LIMIT_LABEL_FACE_MEMBERSHIPS_PASS')
 print('TWO_EXCEPTIONAL_COMPACT_PROJECTIVE_POINTS_QH_QLR_PASS')
 print('ALL_TEN_SYMBOLIC_JOINT_RATE_LIMITS_AND_TRUE_8_14_8_HULL_PASS')
 print('ACTUAL_EIGHT_CORNER_SHADOW_STRICT_ONE_THIRD_CONTAINMENT_PASS')
 print('HEXAGON_TWO_APEX_TRUE_AREA_VOLUME_CENTROID_BALANCE_PASS')
 for d in [r['limit']]+r['finite_controls']:print('CONTROL',d.get('epsilon','limit'),d['fvector'],d['S'],d['U'],d['H'],'weak000')
 print('THREE_GENUINE_E17_REFILLS_ONE_LIMIT_ALL_260_RECIPROCAL_PRIMITIVES_NONZERO_PASS')
 print('NO_U1_WITNESS_NO_GLOBAL_BOUND_OR_CANONICAL_COUNT_CHANGE')
 print(p.name,len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```

Convenience copies: complete source (`twocap_escape_channels.py`), exact report (`twocap_escape_channels.json`). The embedded source and proofs are sufficient without these links.
