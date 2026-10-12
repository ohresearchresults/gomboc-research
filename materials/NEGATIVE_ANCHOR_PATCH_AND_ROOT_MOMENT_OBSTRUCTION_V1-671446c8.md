# material-671446c88218

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# NEGATIVE_ANCHOR_PATCH_AND_ROOT_MOMENT_OBSTRUCTION_V1

## Evidence and scope
This is a new analytic coordinator derivation, not a numerical search, not a universal mechanical exclusion and not a new attaining polytope. Its exact antecedents were read completely in the present coordinator turn:

- POLYHEDRAL_TRACE_STATIONARITY_RIGIDITY_V1, material [internal-source-reference], SHA-256 8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9.
- ROOT_DUALITY_JOINT_VARIATIONS_V1, material [internal-source-reference], SHA-256 73eb04d63deeab693d29533819d3b95c4e1af3cc01d756987381aaa2bb4c2ed8.

The earlier proper33/at-most-two-free-polygons obstruction is independent background, not needed in this proof. Its exact capsule is [internal-source-reference], SHA-256 3d3bc76d6d6f168971a834abe459ef5623418ab19f10c7820cac33d7d44b4a9c. The new result concerns enlarged protected coordinate facets, which that proper33 theorem does not cover.

All statements below concern a genuine polyhedral local maximum in the FULL marked-body[private-runtime-path] problem. They do not hold merely because a body is convex, because ell is fixed, or because a few moment equations were fitted. The first two antecedents supply the actual shape and frame variation conditions listed explicitly below. In particular, the root moment conditions require all four canonical ell-values to be positive and joint root variation; no assertion is made for a zero canonical endpoint or for a fixed-ell maximum. No computation materially produced this theorem, so there is no missing program or numerical checkpoint.

## 1. Actual optimization class and notation
Let
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0), T0=conv(A,B,C,D).
Let P be a full-dimensional convex polytope with T0 contained in P, P contained in {x>=0,y>=0,ell>=0}, and a true positive-area root facet F0=P intersect {ell=0}. Write
ell=a+(d-a)x+(c-a)y+(b-a)z,
a>b>0, c>0, d>0, s=a+b,
n=(s+c)x+(s+d)y.
The actual, uniformly filled volume integrals are
V=int_P 1, E=int_P ell, N=int_P n, T=N/(6VE),
g=(u,v,z_g)=(int_P(x,y,z))/V,
r=N/V=n(g), q=N/E, G=n-r-q ell.
Let p=u+v, t=6V, m=3p/t, w=(v/(3p),u/(3p),1/3).
Thus q=tT and G(g)=-r. Denote the true protected coordinate facets by Fx=P intersect {x=0} and Fy=P intersect {y=0}. They contain ABC and ABD respectively, but they are not assumed to equal those triangles. A true vertex other than A,B,C,D is called auxiliary. All root vertices are auxiliary since a,b,c,d>0.

The full joint local maximum supplies the following established necessary conditions.

(R1) A and B are true vertices, AB is the whole true common edge of Fx and Fy, and every auxiliary true vertex W satisfies G(W)>0. Also G(A)=-r-qa<0 and G(B)=-r-qb<0.

(R2) Every true facet other than Fx,Fy,F0 contains at least one canonical mark. If it contains exactly one canonical mark X, then X is a true vertex, G(X)<0, the facet is a triangle XUV, and G(U)=G(V)=-G(X)/3>0. This is a whole-supporting-plane stationarity and spike consequence, not stationarity of arbitrary triangulation diagonals.

(R3) Moving the canonical mark C within the unchanged actual facet Fx, and recanonicalizing, yields the supporting inequality
h_C(y,z)=(b+2c)(y-1)+(b-a)z<=0 on Fx.
Equality holds at C. In particular h_C(A)=-(b+2c)<0 and h_C(B)=-(a+2c)<0. Interchanging x,y and c,d gives
h_D(x,z)=(b+2d)(x-1)+(b-a)z<=0 on Fy,
with strict negativity at A,B and equality at D.

(R4) With root measure dnu=darea/|grad ell|, full joint root stationarity gives
int_F0 G dnu=6V^2(T-m),
int_F0 xG dnu=6V^2(Tu-m w_x),
int_F0 yG dnu=6V^2(Tv-m w_y),
int_F0 G^2 dnu=6V^2 m(r-n(w)).
Indeed the general affine-h identity is int_F0 Gh dnu=6V^2[T h(g)-m h(w)]. Its specialization h=G uses T ell(g)=m ell(w). Because G>0 on every root vertex, G is strictly positive throughout F0; therefore int_F0 G^2>0 and r>n(w).

These conditions are applied only to actual bodies in the stated optimization class.

## 2. Nonpositive marks are genuine vertices
### Lemma 1
If G(C)<=0, C is a true vertex of Fx and of P. If G(D)<=0, D is a true vertex of Fy and of P.

Proof for C. The nonconstant affine h_C exposes a proper face of the genuine convex polygon Fx containing C, and that exposed face contains neither A nor B. Consequently C cannot be in the relative interior of Fx. If it were not a true vertex, it would be in the relative interior of a true exposed edge. Its two endpoints cannot be A or B; D is not in Fx. They are therefore auxiliary true vertices, and both have strictly positive G by R1. Affinity would then give G(C)>0, a contradiction. Reflection proves the assertion for D. This does not forbid a positive-G canonical mark from being redundant; the sign hypothesis is essential.

## 3. One auxiliary chain on a negative-mark protected facet
### Lemma 2
Suppose G(C)<=0. The true vertices of Fx other than A,B,C form one boundary chain between C and one endpoint of AB. The other endpoint is joined to C by a true edge. Thus, after reversing the cyclic order or exchanging the two endpoint descriptions, Fx has cyclic order
A,B,U1,...,Uk,C,
where all Ui are auxiliary and G(Ui)>0. In particular at least one of AC and BC is a true edge.

Proof. The intersection of a convex polygon boundary with a strict affine sublevel halfplane has one negative boundary arc, apart from possible zero endpoints. A,B have G<0 and share a true edge. All other vertices except C have G>0. A further nonpositive vertex C must therefore be adjacent along the boundary to A or B; otherwise a positive vertex would separate the nonpositive portions on both sides. Equivalently, if G(C)=0 and both neighbors had positive G, the supporting local-minimum property of an affine function at a convex polygon vertex would imply G>=0 on the whole polygon, contradicting G(A)<0. This proves the stated order, including the zero case.

### Lemma 3
Under G(C)<=0, every auxiliary-to-auxiliary edge of the chain in Fx is either an edge of the root facet F0 or has second facet DUiUi+1. In the latter case G(D)<0 and
G(Ui)=G(Ui+1)=L_D:=-G(D)/3>0.
There is at most one root edge and at most one nonroot auxiliary-chain edge. Therefore k<=3 and Fx has at most six true vertices.

Proof. Let UV be a true edge of Fx with auxiliary endpoints. It cannot meet Fy as its second facet since Fx intersect Fy=AB. If its second facet is not F0, R2 says that facet contains a canonical mark. It cannot contain A,B,C: its intersection with Fx is exactly the true edge UV, whereas the affine G is positive on UV and nonpositive at A,B,C. Thus the only possible mark is D. R2 gives the triangle and equal endpoint values L_D.

The line of UV on Fx is then G=L_D. Since Fx is convex and A lies on the G<L_D side, all of Fx lies in G<=L_D. Consequently UV is the exposed global-maximum-G edge of Fx. Every nonroot auxiliary-chain edge would have exactly the same value L_D; a genuine convex polygon has only one one-dimensional exposed face for that affine maximum. There can be at most one such edge. Also two distinct true facets Fx and F0 have at most one common true edge. With k auxiliary vertices the chain has k-1 auxiliary-to-auxiliary edges when k>=1, so k-1<=2.

Corollaries.
1. If additionally G(D)>=0, no nonroot auxiliary-chain edge is possible and Fx has at most five true vertices.
2. If Fx has no root edge, it has at most five true vertices.
3. A pentagon has exactly one auxiliary-to-auxiliary edge, which is either a root edge or a D-anchored triangle edge.
4. A hexagon has exactly three auxiliary vertices and exactly two consecutive auxiliary-chain edges: one is a root edge and one is a D-anchored triangle edge. In particular G(D)<0. The third auxiliary endpoint has G<L_D, since three distinct true vertices cannot lie on one exposed line edge.
5. All assertions have the x/y,C/D reflection.

The six-vertex bound is a proved necessary bound, not a claimed sharp attainable maximum. No attaining hexagonal joint maximizer is supplied.

## 4. A nonroot chain edge determines a global supporting plane
Suppose the nonroot auxiliary-chain edge UV on Fx exists. Put L=L_D=-G(D)/3>0. The true facet DUV lies on the affine plane
G+4Lx=L.
Indeed it contains U,V, where x=0 and G=L, and D, where x=1 and G=-3L. These are three affinely independent points, and the displayed affine function is nonconstant on their ambient space. A has x=0,G(A)<0, so actual convexity fixes the global supporting side:
H:=L-G-4Lx>=0 throughout P.
Every auxiliary true vertex has G>0, hence x<1/4. This includes all true root vertices, and therefore all of F0 lies in x<1/4.

Nevertheless the actual body centroid obeys u>=1/4. To see this without introducing abstract mass weights, triangulate the actual boundary and cone it from D. The positive-volume tetrahedra cover P up to measure zero. Each has one vertex D with x=1 and its other vertices have x>=0. Every cell centroid has x>=1/4; their actual volume-weighted mean does as well. The same argument coning from C gives v>=1/4. Zero-volume cones are discarded. This remains a genuine integral argument, not freely chosen barycentric masses.

## 5. Root moment imbalance
### Theorem 4
For the nonroot auxiliary-chain edge on Fx one has the strict identity consequence
v-3u > q(4u-1)+(3p/L_D)[r-n(w)] > 0.
In particular v>3u>=3/4. A nonroot auxiliary-chain edge on Fy analogously forces
u-3v > q(4v-1)+(3p/L_C)[r-n(w)] > 0,
where L_C=-G(C)/3>0. Such nonroot auxiliary-chain edges cannot occur on both protected coordinate facets of one full joint maximum.

Proof. DUV and F0 are distinct true facets, because ell(D)=d>0 while ell=0 on F0. Thus the supporting function H=L-G-4Lx is strictly positive on the relative interior of F0. We already know G>0 there. Hence int_F0 GH dnu>0. Substituting the actual three root moment identities R4 yields
0 < int_F0 GH/(6V^2)
  = L[T(1-4u)+m(4w_x-1)]-m[r-n(w)].
Rearranging, multiplying by t/L and using tm=3p, tT=q, 3p w_x=v, gives
v-3u > q(4u-1)+(3p/L)[r-n(w)].
Here q>0, u>=1/4, p>0, L>0 and r>n(w), so the right side is strictly positive. Reflection gives the other inequality. Since u,v>0, v>3u and u>3v are contradictory.

This derivation is the new cross-branch mechanism: true whole-facet hinge stationarity fixes the DUV support, while actual root stationarity and the actual coned-volume centroid force a directional imbalance. One must not use the root moment identity at a merely fixed-root extremum.

## 6. Consequences for enlarged protected patches
If G(C),G(D)<=0, both C,D are true vertices and both protected facets have at most six vertices. At most one protected facet can contain a nonroot auxiliary-to-auxiliary boundary edge; hence at most one can be hexagonal. The other has at most five vertices, and any auxiliary-to-auxiliary boundary edge on it must be a root edge.

In the centroid sector u/3<=v<=3u, neither protected facet can contain such a nonroot auxiliary-chain edge (assuming the relevant nonpositive mark on that facet). Therefore each has at most five vertices, and a pentagonal protected facet must have its unique auxiliary-to-auxiliary edge on the root.

Even without assuming the other canonical mark nonpositive in advance, an Fx nonroot auxiliary-chain edge forces G(D)<0, making the reflected protected-facet result available. The case with Fx and Fy interchanged is identical.

## 7. Remaining scientific boundaries
The imbalanced strips v>3u and u>3v are not excluded here. The root-only case and proper33 bodies have no auxiliary chains on protected facets, so the new theorem does not resolve them. It does not prove the general T<51/25 target, does not prove every E17 incidence impossible, does not promote a new mechanical registry count, and does not change 34<=C_min<=622. Positive-G redundant marks and zero canonical ell-values remain outside the corresponding lemmas. The full proper33 >=3 free-polygon negative-anchor problem remains separate.

A useful next question is whether actual volume/first-moment or remaining fan geometry eliminates the forced imbalanced strip, or whether a genuine convex stationary configuration realizes it. Merely fitting the displayed scalar inequalities would not settle that question.
