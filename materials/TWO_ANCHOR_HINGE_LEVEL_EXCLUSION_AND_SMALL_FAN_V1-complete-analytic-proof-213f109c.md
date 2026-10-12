# material-213f109c9edc

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# TWO_ANCHOR_HINGE_LEVEL_EXCLUSION_AND_SMALL_FAN_V1

## Status and exact scope
This is an analytic conditional theorem about a genuine polyhedral local maximum of the ORIGINAL uniformly filled adjacent-triangle trace. It proves a polygonal two-mark hinge inequality, an asymmetric exclusion between the two ordinary facet stars, and the bounds F<=10, V<=11, E<=19. With either entire nonroot star flat, the bounds improve to F<=7, V<=8, E<=13. No equality construction or sharpness is asserted.

It does NOT prove that the global high-trace maximum is polyhedral, does not evaluate the remaining maximum, does not exclude the first open V10/E17/F9 layer, and does not preserve a prescribed f-vector or an equilibrium class under its variations. The global minimum bounds remain 34<=Cmin<=622.

The accepted local-variation source is POLYHEDRAL_TRACE_STATIONARITY_RIGIDITY_V1, material [internal-source-reference], 14798 bytes, SHA256 8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9. Its full text was read before this extension. The independent exact vertical-placement theorem is TWO_ANCHOR_FIBRE_GREEDY_DOMINANCE_V1, complete proof [internal-source-reference], SHA256 29b81610f3eabd674a9478200d167796866dd41458062ef843eec458b0e0b114, and executable control [internal-source-reference]. The present proof uses no computation and needs no numerical checkpoint or generated output.

The earlier TWO_ANCHOR_PROJECTED_MASS_OBSTRUCTION_V1, [internal-source-reference] with erratum [internal-source-reference], supplies the two-anchor geometry at a joint all-auxiliary positive-endpoint maximum in its G(C),G(D)>=0 sector. Here that geometry is an explicit assumption. Once it is assumed, the new theorem does not separately require G(C),G(D)>=0.

## 1. Physical optimization class and notation
Set A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0), and T0=conv(A,B,C,D). Fix a>b>0 and c,d>0. Define

ell(x,y,z)=a+(d-a)x+(c-a)y+(b-a)z,
n(x,y)=(a+b+c)x+(a+b+d)y.

For an actual uniformly filled body P let

V=integral_P 1, Eell=integral_P ell, N=integral_P n,
T=N/(6 V Eell), q=N/Eell, r=N/V,
G=n-r-q ell.

Eell is an integral; the letter E without this suffix below counts physical edges. All integrals are Lebesgue volume integrals of the actual body, and its center of mass is its own volume centroid.

Assume P is a bounded full-dimensional convex polyhedron containing T0, contained in x>=0,y>=0,ell>=0, with a genuine positive-area root facet ell=0. Assume P is a local maximum of T, at the fixed function ell, among ALL nearby bounded convex bodies satisfying these same marked containment and halfspace conditions. In particular, the admissible class is not restricted to the original face lattice, to a fixed number of faces, or to the two-anchor representation below. A joint local maximum with variable ell also has the required fixed-ell local maximality.

The two coordinate facets x=0 and y=0 are protected marked supporting patches containing ABC and ABD. They need not be exactly those triangles. The proper33 subclass means they are exactly the genuine maximal triangles ABC and ABD. The proof is valid in the larger marked-patch class, and proper33 is mentioned only when giving a separate root-perimeter improvement.

Assume additionally that P has the genuine two-anchor representation

P={x,y>=0: hA(x,y)<=z<=min(1-hB(x,y), H-l0(x,y))},
alpha=a-b, H=a/alpha>1,
l0(x,y)=((a-d)x+(a-c)y)/alpha,

where hA,hB are finite convex positively homogeneous piecewise linear functions on the nonnegative quadrant. Thus every noncoordinate lower facet passes through A, and every nonroot, noncoordinate upper facet passes through B. No such free facet passes through both A and B. The coordinate supports and root are three distinct genuine facets. The section on the z-axis is exactly AB, and A and B are true vertices.

At the anchors,

G(A)=-r-qa, G(B)=-r-qb,
LA=(r+qa)/3, LB=(r+qb)/3,
LA>LB>0.                                                    (1.1)

A free facet containing exactly one of the four canonical marks is called ordinary. A free lower or upper facet containing at least one of C,D in addition to its anchor is called special. Let rA,rB count ordinary lower and upper facets, and sA,sB count special lower and upper facets.

## 2. Accepted first-variation facts being used
The source [internal-source-reference] proves the following at a polyhedral local maximum in the full marked class just specified.

(a) Every true auxiliary vertex, namely every true vertex other than A,B,C,D, has G(v)>0. Ordinary cap removal excludes G(v)<0. Its thin-edge cap argument excludes equality G(v)=0 by moving a cut a small fixed fraction along an incident edge toward a negative-G canonical endpoint and then taking the transverse cap size to zero.

(b) On every free genuine facet F,

max_F G + 3 average_F G <= 0.                            (2.1)

This is the first-order condition for adding an arbitrarily small outward pyramid with base F and apex approaching a chosen point of F. For affine G, the integral over that pyramid divided by its volume tends to (G(apex)+3 average_F G)/4. The exact finite-addition criterion has only a quadratic-volume correction, so a positive leading coefficient would improve T.

(c) Every ordinary free facet with its sole canonical mark X is a genuine triangle [X,Y,Z] and

G(Y)=G(Z)=-G(X)/3>0.                                    (2.2)

The proof uses both-sign pivots fixing X, in particular the pivot whose normal velocity on F is G-G(X), giving integral_F G(G-G(X))=0, together with (a), (b), and convexity of the polygon. This statement concerns true maximal facets, not triangles in an arbitrary triangulation.

We use (c) with X=A,B, so every ordinary A triangle has its base at G=LA and every ordinary B triangle has its base at G=LB. We also use the immediate consequence of (b) that a free facet cannot have G equal to a positive constant. A positive constant facet cannot be either coordinate facet because they contain A and B, where G is negative. It cannot be the root because G is nonconstant on the root, as proved below.

These are previously proved analytic inputs, not consequences of a transport receipt. The new polygonal hinge bound starts in the next section.

## 3. Polygonal two-mark hinge inequality
Let F be a convex polygon, let A be a true vertex, and let phi be affine on its plane, nonnegative on F, with phi(A)=0 and not identically zero. Put M=max_F G, where G is any affine function.

Triangulate F as a fan from A. On a fan triangle [A,P,Q] put s=phi(P), t=phi(Q). Exact integration of a product of two affine functions gives

integral_[A,P,Q] G phi
= area([A,P,Q])/12 * [G(A)(s+t)+G(P)(2s+t)+G(Q)(s+2t)].

Since s,t>=0 and G(P),G(Q)<=M,

integral_[A,P,Q] G phi
<= area([A,P,Q])/12 * (G(A)+3M)(s+t)
= (G(A)+3M)/4 * integral_[A,P,Q] phi.

Summing the genuine polygon fan proves

integral_F G phi <= (G(A)+3 max_F G)/4 * integral_F phi.  (3.1)

Now let F be a free lower facet containing A,C but not D. It lies on a plane z=p x, and phi=x is nonnegative on F, vanishes on AC, and is not identically zero because F is not the coordinate facet. Varying this plane to z=(p+epsilon)x gives both signs of an admissible hinge pivot around AC. The other canonical marks B,D are strictly on the allowed side of F; the root and coordinate halfspaces stay fixed. For sufficiently small epsilon the resulting bounded polyhedron still contains T0 and stays within the required protected halfspaces. The first variation of T is a nonzero common constant times integral_F G x. Local maximality in both signs therefore implies

integral_F G x=0.

The usual boundary first-variation formula applies to the relative interior of the facet; changes near edges and vertices contribute only higher-order terms. Simplicity of the vertices is unnecessary. Combining this equality with (3.1), and noting integral_F x>0, yields

max_F G >= -G(A)/3 = LA.                                (3.2)

The same proof for a facet containing A,D but not C uses phi=y. For upper facets containing B,C but not D or B,D but not C, use the corresponding pivot around BC or BD and obtain

max_F G >= LB.                                         (3.3)

Thus the lower hinge bound is valid for an arbitrary convex polygonal two-mark facet. It does not assume that C or D is itself a true vertex of that marked patch.

## 4. Flat-star exceptions and the number of special facets
There is at most one noncoordinate free facet containing AC: the coordinate facet x=0 already contains that segment, and at most two distinct facets of a three-dimensional convex polyhedron can contain a given nontrivial exposed edge segment. The same conclusion holds even when C is not an endpoint of the maximal edge. The identical argument applies to AD,BC,BD.

Consequently, unless a lower facet contains all of A,C,D, one has sA<=2. Unless an upper facet contains B,C,D, one has sB<=2.

If a lower facet contains A,C,D, its plane is z=0 and hA has the zero linear form among its active supporting forms. Hence hA>=0. Containment of C,D implies hA(0,1)<=0 and hA(1,0)<=0; convex homogeneity gives

hA(x,y)<=x hA(1,0)+y hA(0,1)<=0.

Therefore hA is identically zero on the whole quadrant, and there is precisely one lower facet. This is the flat ACD exception, not merely a local triangle.

Likewise an upper facet containing B,C,D forces hB(x,y)=x+y identically and gives exactly one nonroot upper facet. If both identities hold, the body before the root inequality is exactly T0. Since ell is strictly positive at all four canonical vertices, the root then cannot be a genuine facet. Thus both stars cannot be flat simultaneously under the hypotheses.

## 5. Every ordinary B facet is root-based unless the lower star is flat
Take an ordinary B facet [B,Y,Z]. Its base YZ is a true edge and G(Y)=G(Z)=LB. Consider the other facet incident to that edge.

It cannot be another upper facet, because both planes would contain B,Y,Z and therefore coincide. It cannot be a coordinate facet, because a coordinate plane containing Y,Z and B would likewise be the plane of the ordinary triangle. If it is an ordinary lower A facet, the same vertices would have to satisfy G=LA, contrary to LA>LB.

Suppose the neighboring lower facet is a two-mark facet containing A,C or A,D. Since the edge YZ is a supporting edge of that convex polygon and G(A)<LB, the whole facet lies in G<=LB. Its maximum is exactly LB, contradicting the polygonal lower hinge bound max_F G>=LA.

The only remaining nonroot possibility is a lower facet containing A,C,D, which is the entire flat lower star from Section 4. Therefore

hA not identically zero => every ordinary B base lies on the root. (5.1)

On the root ell=0 one has G=n-r. This function is nonconstant on the two-dimensional root: the coefficient of z in ell is b-a!=0, while n has zero z coefficient and positive x,y coefficients. Equivalently, the root is an affine graph over a positive-area projected polygon, and n is a nonconstant linear function on that polygon. A convex polygon has at most one true edge contained in a prescribed supporting level line of a nonconstant affine function. All ordinary B bases are at the same level LB. Hence

hA not identically zero => rB<=1.                       (5.2)

An ordinary A facet has a base at G=LA. Its other neighboring facet cannot be another lower facet or a coordinate facet, by the same common-anchor plane argument; it cannot be an ordinary B facet because the two levels differ. Its base therefore lies on either a special B facet or the root. Each such facet can contain at most one of these bases: it has at most one exposed level-LA edge, and any special B facet also contains the strictly lower point B. The root can contain at most one such base for the nonconstancy reason above. Thus

rA<=sB+1.                                               (5.3)

## 6. The root shares true edges with both stars
This fact is needed to exclude saturation in the preceding count. It is a geometric statement, independent of stationarity.

Put j=hA+l0 and k=hA+hB. Write (x,y)=s theta with s=x+y>=0 and theta=(tau,1-tau), 0<=tau<=1. Set eta(tau)=j(theta), kappa(tau)=k(theta). The vertical length is

L(s theta)=max(0,min(1-s kappa,H-s eta)).

Since j and k-j are convex homogeneous, the angular function

D=H kappa-eta=(H-1)eta+H(kappa-eta)

is convex. The positive-area root has a nonempty open angular shadow where D<0. This shadow includes an open subinterval in 0<tau<1. On such a ray boundedness implies eta>0: if eta<=0 then kappa<eta/H<=0, and both affine length branches stay positive indefinitely.

The root along this ray begins at

r0=(H-1)/(eta-kappa)>0

and ends at

RK=H/eta>r0.

At the inner endpoint the root meets the nonroot upper graph; the lower inequality is strict there. At the outer endpoint it meets the lower graph; the nonroot upper inequality is strict there. Because the gauges are piecewise linear, choose a nonempty angular subinterval on which the relevant supporting forms are fixed. The endpoint curves are then straight segments on the appropriate pair of facet planes. They have positive length because their positive projected points lie on varying rays, and they lie away from both coordinate planes. They are therefore genuine root-upper and root-lower edges, not merely contacts at vertices.

This proves that the root shares at least one physical edge with an upper facet and at least one with a lower facet. Degeneracies at the finitely many angular breakpoints do not affect the argument.

## 7. Saturation rA=sB+1 is impossible when sB>=1
Suppose sB>=1 and equality holds in (5.3). There is then one ordinary A base on the root and one on every special B facet. Each special B facet is contained in G<=LA, because it contains its supporting base edge at G=LA and the point B at negative G. Every ordinary B facet is also contained in G<=LB<LA. Thus all nonroot upper facets are contained in G<=LA.

The root contains the ordinary A base at level LA. As a convex polygon on which G is nonconstant, it lies on one side of that supporting level line.

Case 1: the root lies in G<=LA. Every true vertex of P other than A lies on an upper facet or on the root. Indeed, otherwise all its active planes are coordinate or lower planes, all passing through A; three linearly independent active normals would then force the vertex to be A. Consequently all vertices of P have G<=LA.

There are at least two distinct ordinary A bases at level LA, since sB>=1. They cannot be collinear: a common line together with A, which is not on that line, would determine the same plane for both ordinary facets, contrary to their being distinct maximal facets. Their convex hull is two-dimensional. Thus the exposed face P intersect {G=LA} is a positive-area facet on which G is the positive constant LA. It is not a coordinate facet and not the root. This contradicts (2.1).

Case 2: the root lies in G>=LA. Section 6 supplies a root-upper edge. Its upper neighbor cannot be ordinary, since the latter has G<=LB<LA. It is a special B facet, and the edge has G=LA. That special facet already has an ordinary A base at G=LA. Since it has only one exposed edge at that level, these edges coincide. The coincident physical edge would then be incident to three distinct facets: the ordinary A triangle, the special B facet, and the root. A physical edge of a convex three-polyhedron has exactly two incident facets. This is impossible.

Both cases are excluded. Therefore

sB>=1 => rA<=sB.                                       (7.1)

This argument uses actual maximal facets and does not count diagonals of a triangulation as edges.

## 8. Facet count in the nonflat case
Assume neither star is flat. Section 4 gives sA,sB<=2, and Section 5 gives rB<=1. There are exactly three protected facets, so

F=3+sA+sB+rA+rB.

If sB>=1, (7.1) implies

F<=3+2+2+2+1=10.                                       (8.1)

If sB=0, (5.3) gives rA<=1, and F<=7. In particular, the general bound F<=10 holds.

The argument is asymmetric in A and B because a>b implies LA>LB. Interchanging the geometric anchors without interchanging this inequality would be invalid. The equal-endpoint case a=b is not covered.

## 9. Flat-star count improves to seven
First let hA be identically zero. There is exactly one lower facet, containing A,C,D, no ordinary lower facet, and at most two special B facets. An ordinary B base can meet only that one lower facet or the root. Each can host at most one base at level LB, so rB<=2.

If rB=2, one ordinary B base is on the lower facet and one is on the root. The lower facet lies in G<=LB because it contains A at negative G. If the root also lies in G<=LB, every vertex except B lies on the lower facet or root: any vertex not there has only coordinate and upper active planes, all through B. Hence G<=LB on P, and the two noncollinear ordinary B bases force a positive constant-G facet, contradicting (2.1), exactly as in Section 7.

If instead the root lies in G>=LB, Section 6 gives a root-lower edge at G=LB. This must be the lower facet's unique level-LB edge, already the base of an ordinary B facet. It would have three distinct incident facets, again impossible. Thus rB<=1 and

F<=3+1+2+1=7.                                         (9.1)

If instead hB=x+y identically, there is exactly one special B facet, no ordinary B facet, and sA<=2 because both stars cannot be flat. Formula (7.1) gives rA<=1, so again F<=7.

## 10. True vertex and edge counts
Let FA and FB be the numbers of genuine noncoordinate lower and genuine nonroot noncoordinate upper facets. Then F=FA+FB+3.

The facets incident to A are exactly its FA lower facets and the two coordinate facets. The facets incident to B are exactly its FB upper facets and those same coordinate facets. For a vertex of a convex three-polyhedron, its vertex figure is a polygon, so its number of incident facets equals its degree. Therefore

deg(A)+deg(B)=FA+FB+4=F+1.

Every other true vertex has degree at least three. Hence

2E>=F+1+3(V-2).

Combining this with Euler's identity E=V+F-2 gives

V<=F+1, E<=2F-1.                                      (10.1)

The theorem therefore proves

F<=10, V<=11, E<=19,

and in either flat-star case

F<=7, V<=8, E<=13.

These counts concern genuine maximal facets, genuine vertices and physical edges. They do not assert that every two-anchor body has small complexity; local maximality in the full variation class is essential.

## 11. Root-perimeter consequence and the proper33 distinction
In the nonflat case the root can meet at most two special A facets, two special B facets, one root-based ordinary A facet and one root-based ordinary B facet. It can additionally meet the two coordinate facets. Thus the marked-patch root has at most eight physical edges. In the flat case the general F<=7 bound gives at most six root edges.

In the proper33 subclass the root cannot meet either coordinate facet. Indeed ell is strictly positive at each vertex of ABC and ABD, hence throughout each of these genuine triangles. Removing the two possible coordinate neighbors gives at most six root edges in the nonflat case, and certainly no more in the flat case. Thus

root edges <=8 in the marked-patch class,
root edges <=6 in proper33.                            (11.1)

Do not apply the six-edge bound to arbitrary enlarged coordinate supporting patches.

## 12. Meaning for the research and remaining gap
This closes the previously open polygonal two-mark extension: the ordinary B-to-lower obstruction is not confined to triangular AC or AD facets. The flat ACD exception is genuine and is treated separately, not silently discarded. In the nonflat lower case every ordinary B facet is root-based and there is at most one. Together with the saturation argument this yields a substantially smaller conditional stationary fan.

The theorem and TWO_ANCHOR_FIBRE_GREEDY_DOMINANCE_V1 control different freedoms. The latter exactly optimizes vertical placement for fixed actual projected body and root, retaining both convex gauges and all actual projected moments. The present theorem uses additional full-class local variations and distinct G levels to constrain the actual incidence pattern at a local maximum. Neither replaces the actual uniformly filled body with an arbitrary moment completion.

What remains is the value of the original trace on the resulting compatible projected geometries and small stationary fans, including root coefficients and canonical mark reactions. Polyhedral attainment of the global unrestricted extremum is a separate premise, not supplied here. Sectors without the two-anchor conclusion, one-zero endpoint limits, and equal-anchor endpoints are also outside this theorem's stated domain.

A discarded possible shortcut was to try to force a suitable G-weighted root mean below LA using only scalar root-duality data. The available scalar completions do not justify that inequality, so it is not an accepted step. None of Sections 3-11 uses it.

In particular, F<=10 still permits F=9, and V<=11 still permits V=10. The variations can change the physical f-vector and do not preserve strict or weak equilibria. There is no E17 registry decrement, no new lower minimum bound, and no replacement of the exact C622 own110 attainer.
