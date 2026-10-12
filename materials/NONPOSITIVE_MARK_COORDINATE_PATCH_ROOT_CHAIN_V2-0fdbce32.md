# material-0fdbce320bac

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# NONPOSITIVE_MARK_COORDINATE_PATCH_ROOT_CHAIN_V2

## Scope, evidence and relation to V1
This analytic coordinator theorem strengthens, without retracting, the previously stored NEGATIVE_ANCHOR_PATCH_AND_ROOT_MOMENT_OBSTRUCTION_V1: material [internal-source-reference], SHA256 671446c88218396343d2b6a9aef368a0710ad7176eeeae5ad57d400059f83dc4. V1's six-vertex necessary bound and conditional root-moment imbalance are valid but weaker. The new local endpoint argument excludes the nonroot auxiliary-chain edge altogether. The imbalance formulas remain useful conditional mechanisms in settings where the endpoint hypotheses have not been established; no imbalanced-strip exclusion by those formulas alone is claimed.

The other exact antecedents, fully read, are POLYHEDRAL_TRACE_STATIONARITY_RIGIDITY_V1, [internal-source-reference], SHA256 8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9, and ROOT_DUALITY_JOINT_VARIATIONS_V1, [internal-source-reference], SHA256 73eb04d63deeab693d29533819d3b95c4e1af3cc01d756987381aaa2bb4c2ed8.

The theorem concerns actual uniformly filled marked bodies at a full marked-body local maximum, with canonical frame variation available. It is not a property of all convex bodies and is not a mechanical exclusion of all E17 incidences. The only full joint condition needed beyond fixed-ell body variations is the mark exposure needed to make a nonpositive mark a true vertex. The root stationarity moment identities are NOT used in the V2 exclusion. There is no numerical computation, code dependency or missing recovery input.

## 1. Setup and established conditions
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0). The full-dimensional polytope P contains T0=conv(A,B,C,D) and lies in x>=0,y>=0,ell>=0, where
ell=a+(d-a)x+(c-a)y+(b-a)z,
a>b>0,c>0,d>0,s=a+b,
n=(s+c)x+(s+d)y.
The actual integrals are V=int_P1,E=int_Pell,N=int_Pn; q=N/E,r=N/V,G=n-r-qell. The objective is T=N/(6VE). Let Fx=P intersect{x=0}, Fy=P intersect{y=0}, and F0=P intersect{ell=0}, all true positive-area facets. The protected facets may be larger than ABC and ABD. An auxiliary true vertex means any true vertex other than the four canonical marks.

Necessary conditions from the exact antecedents:
1. A,B are true vertices, AB is the true common edge of Fx,Fy. G(A),G(B)<0. All auxiliary true vertices have G>0.
2. Every ordinary true facet (neither protected nor root) contains a canonical mark. An ordinary facet with exactly one mark X is a true triangle XUV, with X a true vertex, G(X)<0 and G(U)=G(V)=-G(X)/3>0.
3. Canonical mark variation exposes C on Fx by h_C=(b+2c)(y-1)+(b-a)z<=0, with h_C(C)=0 and h_C(A),h_C(B)<0. Thus G(C)<=0 forces C to be a true vertex: otherwise it lies inside an exposed edge with two auxiliary endpoints of positive G. The same holds for D by reflection.
4. Whole-plane tilt of an ordinary triangle ZDU fixing its canonical marks Z,D has speed proportional to barycentric lambda_U. Two-sided stationarity gives
int_ZDU G lambda_U=area(ZDU)[G(Z)+G(D)+2G(U)]/12=0.
This is a variation of a genuine whole facet, not an independent integration-triangle motion.

## 2. Existing chain and support reduction
Suppose G(C)<=0. The affine nonpositive vertices of the convex polygon Fx lie on one boundary arc. Since A,B form a true edge and all other true vertices except C have positive G, C is adjacent to A or B. After choosing cyclic orientation, the vertices of Fx are
A,B,U1,...,Uk,C
or the analogous order with the endpoint descriptions exchanged. All Ui are auxiliary. Let Z denote either A,B or C when used as the canonical endpoint of this chain; G(Z)<=0 and Z is a true vertex.

For any auxiliary-to-auxiliary chain edge UV of Fx, its second facet is either F0 or an ordinary DUV triangle. Indeed no other canonical mark can belong to the second facet, since its intersection with Fx is the true edge UV and A,B,C are distinct true vertices outside it. If ordinary, condition2 gives G(D)<0 and G(U)=G(V)=L=-G(D)/3>0.

The DUV supporting plane has equation G+4Lx=L, and the side containing A is G+4Lx<=L. Combined with x>=0, this makes L the global maximum of G on P. Its entire maximizing face is precisely UV: equality G=L forces x=0 and hence lies in Fx intersect DUV=UV. In particular U,V are the only true vertices of P with G=L.

There is at most one nonroot auxiliary-chain edge, since all such edges would have the same value L and be the same exposed maximum edge of Fx. There is at most one root chain edge because Fx and F0 intersect in at most one true edge. Thus k<=3. If a nonroot edge exists, one of its endpoints U is adjacent along Fx to a canonical endpoint Z of the auxiliary chain: for k=2 this holds at both ends; for k=3 the other chain edge is the unique root edge, and the nonroot edge has one outer endpoint. The k<=1 case has no auxiliary-chain edge.

## 3. Endpoint contradiction
Assume such a nonroot edge UV and choose its outer endpoint U and neighboring canonical Z. Let F be the second true facet of the genuine edge ZU of Fx.

F is not Fy, whose intersection with Fx is AB, and not F0, because ell(Z)>0. It contains Z and cannot contain any of the other canonical marks on Fx. Hence its canonical set is either {Z} or {Z,D}.

### Case I: F contains only Z
Condition2 makes F a triangle ZUW with W auxiliary and G(W)=G(U)=L. The global maximizing face of G is UV, so W must be V. But Z,U,V lie in Fx, which would make F the same protected facet instead of a distinct ordinary facet. Contradiction.

### Case II: F contains Z,D
Both are true vertices, with G(Z)<=0 and G(D)=-3L<0. All other true vertices of F are auxiliary and have positive G. Therefore Z,D are adjacent on the convex polygon F. To see the zero endpoint case as well, if G(Z)=0 and both neighbors of Z were positive, Z would be a local minimum of an affine function on a convex polygon and hence a global minimum, contradicting G(D)<0. Thus ZD is a true edge.

The distinct facets F and DUV contain D and U, so their intersection is the true edge DU. Also F intersect Fx is the true edge ZU. These edges ZD,DU,UZ already close a three-edge cycle. A convex polygon with these three edges has no additional vertices; F is exactly the genuine triangle ZDU.

Whole-facet stationarity condition4 now gives
0=G(Z)+G(D)+2G(U)=G(Z)-L,
which is impossible because G(Z)<=0<L. This completes the contradiction.

No general positive-edge polygon lemma was used. In particular, the archived CONCAVE_FACET_ALL_POLYGON_POSITIVE_EDGE_OBSTRUCTION_V1 ([internal-source-reference], SHA256 3def2fc37632f9e60a779bd64de787dfb20988f425dc76202da702efcdcaeb78, fully read here) concerns a level edge joining a POSITIVE canonical mark to an auxiliary vertex when the two marks are adjacent. It cannot be cited as a ban on arbitrary auxiliary-to-auxiliary positive edges. That tempting shortcut would be invalid; the true-facet intersection argument above is what resolves Case II.

## 4. The strengthened theorem
At a full marked-body local maximum with a>b>0,c,d>0:

- If G(C)<=0, C is a true vertex, at least one of AC,BC is a true edge, and Fx has at most five true vertices.
- Every auxiliary-to-auxiliary boundary edge of Fx lies on the actual root facet F0. There is at most one such edge.
- If Fx is a pentagon, it has exactly two auxiliary vertices U,V, adjacent on the true root edge UV, and canonical cyclic order A,B,U,V,C or its reflected endpoint version.
- If Fx has no root edge, it has at most four true vertices.
- The corresponding assertions hold for Fy when G(D)<=0.

Thus both nonpositive canonical marks force both protected facets to have at most five vertices, and every enlarged pentagonal patch meets the actual root in its auxiliary edge. This completely excludes the hexagonal alternative from V1 under the same full marked hypotheses. It does not prove that all protected facets are triangles or quadrilaterals.

## 5. Remaining work and evidence boundary
Proper33 bodies and protected quadrilaterals/pentagons with root-only auxiliary edges remain possible under these necessary conditions. The allpositive negative-anchor >=3 ordinary-polygon problem is still open. Positive-G redundant marks and zero canonical ell-values are not covered by the relevant nonpositive-mark lemma. T<51/25, the actual mechanical layer10/17/9, and the exact minimum are not proved by this result; 34<=C_min<=622 is unchanged.

The productive continuation is now a finite/root-coupled treatment of protected polygons of size at most five, rather than attempting to exclude a spurious six-vertex/imbalanced-strip residual. V1's conditional global support and moment identities remain preserved as reusable methods; they are not discarded merely because V2 is stronger.
