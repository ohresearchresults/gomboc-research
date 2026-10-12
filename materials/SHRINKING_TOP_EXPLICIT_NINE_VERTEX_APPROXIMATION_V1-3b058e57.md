# material-3b058e5713c7

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# SHRINKING_TOP_EXPLICIT_NINE_VERTEX_APPROXIMATION_V1

## Status and exact dependencies
Coordinator analytical derivation, not a numerical search, certificate replay or new global complexity bound. The construction and estimates below are unconditional geometry. Their mechanical corollary invokes the accepted NINE_VERTEX_NONZERO_PSD_REFINEMENT_COLLAR_V1, [internal-source-reference], SHA256 3052074db1f19530ac423145576607e4c86366b7e45a96cf9f17f880f0aee65b, read completely in this turn. The geometric starting normalization is Section 8 of the fully read immutable result minimum-0226, SHA256 cf8ddaa5aae98ac90b2315d8789415d1d8766915cfed139d27a69ac1201a3539, HEPTAGON_TRIANGLE_CORNER_TENTH_AND_SHRINKING_TOP_COMPACTNESS_V1. It is restated completely here; no source extraction or replay is necessary for this analytic successor.

The new information is an explicit, uniform O(rho) approximation by an actual nine-vertex body, including its true volume centroid. It replaces a subsequence-only use of the shrinking-top normalization by a direct certificate-transfer bound. A universal positive PSD gap is defined precisely, but NOT numerically evaluated. The value of an explicit numerical rho cutoff is therefore still open.

## 1. Family and normalization
Let Delta=conv{(0,0),(1,0),(0,1)}. Let B be a full-dimensional convex heptagon contained in Delta and touching all three sides. For 0<rho<=1 let P=conv((B,0),(rho Delta,1)), uniformly filled. No small-cut or fixed-slope hypothesis is imposed.

Choose diameter endpoints A,B0 of the bottom polygon. Put ell=|B0-A|, e=(B0-A)/ell, and choose a unit perpendicular n. Write beta for the width of the bottom in direction n, c for the midpoint of its n-coordinate range, and s=beta+rho. Use the invertible affine map

 T(x,y,z)=(e.(x,y), [n.(x,y)-c(1-z)]/s, z).

The normalized body K=T(P) is contained in the rational box Q=[-1,1]^2 x [0,1]. Bottom transverse coordinates are in [-1/2,1/2]; top transverse coordinates are bounded by rho/s<=1. Longitudinal coordinates have absolute value at most one. Also ell>=1/2: contacts with x=0 and y=0 bound every coordinate of a point of B by ell, while a contact with x+y=1 has one coordinate at least1/2.

## 2. An actual nine-vertex approximation, not formal masses
Among the three normalized top vertices choose t_- and t_+ of least and greatest transverse coordinate. Keep these two vertices and all seven bottom vertices. Let K'=conv(bottom,t_-,t_+). It is an actual uniformly filled body with at most nine true vertices. The omitted top vertex t_m has a transverse coordinate between the chosen extremes. Let q be the unique point on segment[t_-,t_+] with that same transverse coordinate. Both have height1; hence t_m-q is a purely longitudinal vector. Denote its length by delta.

The corresponding pre-normalization q is on the original top triangle and has the same n-coordinate as the omitted top vertex. Their difference is along e. The top triangle has diameter sqrt(2)rho, and T does not rescale e. Thus

 0<delta<=sqrt(2)rho<=2rho.

Ties among extreme transverse coordinates cause no difficulty: choose any extreme pair, and q can be an endpoint. Keep ten labelled points for later arrow comparisons by replacing the omitted label with q; this refinement still contains every true vertex of K'.

K' has a UNIFORM positive volume:

 Vol(K')>=1/48.

Proof: If beta>=rho, a bottom vertex is at distance at least beta/2 from the line through the diameter endpoints. The resulting bottom triangle has area at least ell beta/4. Its cone to either retained top vertex has normalized volume at least ell beta/[12(beta+rho)]>=1/48. If rho>=beta, the two retained top vertices differ transversely in the original coordinates by rho times the width of Delta in direction n. That width is at least1/2. The tetrahedron formed with the two diameter endpoints has normalized volume at least ell rho/[12(beta+rho)]>=1/48. This proof keeps actual solid volume; the normalization has determinant magnitude1/s.

## 3. Volume and OWN-centroid error
Choose the sign of the longitudinal unit vector u so that t_m=q+delta u. Every unchanged labelled vertex belongs to K', and the omitted vertex belongs to K'+delta u. Convexity gives the one-sided inclusion

 K' subset K subset K'+[0,delta u].

For a convex body, extrusion by a segment of length delta adds delta times the area of its orthogonal projection onto u-perpendicular. This follows directly by integrating interval lengths along lines parallel to u. The transverse-height projection lies in [-1,1]x[0,1], of area2. Therefore

 0<=DeltaV:=Vol(K)-Vol(K')<=2delta.

The use of a ONE-sided segment is essential to the constant; a symmetric segment would unnecessarily double it. Let g and g' be the genuine volume centroids of K and K'. Both K' and the removed region lie in Q, whose diameter is3. Exact mass decomposition yields

 ||g-g'|| <= 3 DeltaV/Vol(K)
           <= 288delta/(1+96delta)
           <= 288delta.

Indeed Vol(K')>=1/48 and DeltaV<=2delta imply DeltaV/(Vol(K')+DeltaV)<=96delta/(1+96delta).

Let z_i be the ten original normalized vertex labels, and z'_i the nine retained labels plus q in place of the omitted one. Put x_i=z_i-g and x'_i=z'_i-g'. These are centred at their respective ACTUAL uniform centroids. Then

 max_i ||x_i-x'_i|| <= delta+288delta/(1+96delta) <=289delta<=578rho.

There is no transported-centroid assumption. Both centred row sets have norm at most3, and every edge or pair difference in either body has norm at most3.

## 4. A well-defined universal nine-vertex PSD gap
Let C9 consist of all ten-labelled configurations Z=(z_0,...,z_9) in Q such that Vol(conv Z)>=1/48 and conv Z has at most nine true vertices. Labels may coincide or be nonextreme. Let g_Z be the actual uniform centroid. Let M range over PSD 3x3 matrices with tr M=1, and let T range over all labelled rooted spanning trees on the ten labels, with arrows directed toward the root. Define

 gamma9 = min_{Z in C9, M PSD, tr M=1, T}
            max_{(i->j) in T} [-(z_i-g_Z)^T M(z_j-z_i)].

This number is strictly positive under the accepted nonzero-PSD contained-refinement theorem.

Proof: C9 is compact. The box and positive volume bound are closed and bounded; among ten labels, having at most nine extreme points is equivalent to some label belonging to the convex hull of the other nine, a finite union of closed conditions. Actual centroids vary continuously on these bounded full-dimensional hulls. The trace-one PSD cone is compact, and the tree set is finite. The accepted theorem says that for every point of this compact product, no rooted tree has all its selected arrows nonnegative. Thus the displayed maximum is positive everywhere; continuity and compactness give gamma9>0.

This is a precise variational gap, not a claimed numerical value, independently reconstructed certificate or conditioning bound. In particular it includes singular M and all coincident/nonextreme refinement labels, which are necessary for the argument.

## 5. Direct physical arrow transfer and an effective interface
For any nonzero PSD M set D_ij=x_i^T M(x_j-x_i) and D'_ij=(x'_i)^T M(x'_j-x'_i). If epsilon=max_i||x_i-x'_i||, the exact decomposition

 D'_ij-D_ij=(x'_i-x_i)^T M(x_j-x_i)
           +(x'_i)^T M[(x'_j-x'_i)-(x_j-x_i)]

gives

 |D'_ij-D_ij| <=9epsilon tr(M)<=2601delta tr(M)<=5202rho tr(M).

Here the first term is bounded by3epsilon||M||op and the second by6epsilon||M||op, and ||M||op<=tr(M). No unnecessary quadratic error term is needed because both actual-centred row sets remain in the same diameter bound.

If K possessed a complete weak rooted spanning tree for M, all its selected D_ij would be nonnegative. The corresponding ten-label refinement of K' has, by the definition of gamma9, some selected D'_ij<=-gamma9 tr(M). This is impossible when 5202rho<gamma9. Hence

 0<rho<min(1,gamma9/5202)

admits NO complete weak rooted spanning tree under any nonzero PSD metric. In particular the original uniformly filled P has at least two strict unstable vertices under every SPD metric. A sole strict unstable vertex would give a true-edge rooted escape tree, since each nonnegative escape along a nonzero edge strictly increases squared radius. Affine normalization transports the metric; it does not replace it by Euclidean I.

The same argument retains the slightly sharper threshold gamma9/(2601sqrt(2)), and the unlinearized centroid estimate can sharpen transfer further. No claim is made at equality.

## 6. Consequences and limits
This gives a concrete reusable route from ANY quantified nine-vertex PSD gap on Q, volume>=1/48, to a uniform small-rho exclusion of the ENTIRE eight-basal-modulus chart. It handles every coupled bottom degeneration and every beta/rho rate without extracting a subsequence. The exact geometric approximation and constants stand independently of how gamma9 might be computed.

It does not evaluate gamma9, close the compact non-small-cut interior, extend to arbitrary nonparallel projectivities, or imply that the U1 metric condition number is bounded. It removes no whole E17 incidence and changes neither accepted lower bound nor attaining example: 34<=C_min<=622 remains. The small-corner all-rho theorem of the parent is a separate, already quantitative sector exclusion.
