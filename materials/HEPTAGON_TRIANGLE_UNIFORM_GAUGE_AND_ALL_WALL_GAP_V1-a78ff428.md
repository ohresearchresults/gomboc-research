# material-a78ff4287c53

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# HEPTAGON_TRIANGLE_UNIFORM_GAUGE_AND_ALL_WALL_GAP_V1

## Scope, evidence and novelty
Coordinator analytical derivation. This gives one uniformly full-dimensional affine normalization for the ENTIRE parallel heptagon-triangle chart, an actual one-vertex-deletion transfer bound, and explicit necessary inequalities separating every possible U1 shape from both rho tails and EVERY basal wall. The inequalities depend on one precisely defined, positive but UNEVALUATED nine-vertex PSD gap. Thus they are not a numerical compact search box.

The only external mathematical premise is the accepted NINE_VERTEX_NONZERO_PSD_REFINEMENT_COLLAR_V1, [internal-source-reference], SHA256 3052074db1f19530ac423145576607e4c86366b7e45a96cf9f17f880f0aee65b, read fully: any finite labelled refinement of an actual uniformly filled full-dimensional body with <=9 true vertices, including coincident and nonextreme labels and its actual volume centroid, admits no complete weak rooted spanning tree for any nonzero PSD metric.

The exact chart and the initial diameter-width normalization are in the fully read result minimum-0226, SHA256 cf8ddaa5aae98ac90b2315d8789415d1d8766915cfed139d27a69ac1201a3539. The coordinator's previous [internal-source-reference] gave an explicit small-rho nine-vertex approximation. Everything needed for the present geometric argument is stated below. No certificate replay, numerical search, source recovery or proof-assistant formalization is claimed.

Unlike the earlier qualitative compactness argument, this proof needs neither EXPANSION7 nor the small-corner coefficient theorem: the nine-vertex PSD premise alone, combined with the uniform gauge, yields both tails and all basal-wall separations. The explicit rho>=7 and corner-tenth sector exclusions remain stronger on their own domains. General nonparallel projectivities are NOT covered.

## 1. Literal chart
Let Delta=conv{(0,0),(1,0),(0,1)} and

 theta=(b,c,p,q,a,d,u,v), rho>0,
 0<b<c<1, 0<a<d<1, p,q>0, p+q<1,
 u,v>0, tau:=1-u/b-v/a>0.

The ten vertices are

 Y0=(b,0,0), Y1=(c,0,0), Y2=(1-p,p,0),
 Y3=(q,1-q,0), Y4=(0,d,0), Y5=(0,a,0),
 Y6=(u,v,0), Y7=(0,0,1),
 Y8=(rho,0,1), Y9=(0,rho,1).

The seven bottom vertices form a convex polygon B contained in Delta and touching all three sides. The uniformly filled solid is P=conv((B,0),(rho Delta,1)). All comparisons use its OWN volume centroid. A sole strict unstable vertex, even with incidental weak contacts elsewhere, implies a true-edge weak rooted escape tree, since a nonnegative nonzero edge escape strictly increases squared radius. We prove necessary conditions even for a complete weak rooted tree under any nonzero PSD metric.

## 2. One full-dimensional gauge for every rho and every basal degeneration
Choose any two bottom diameter endpoints A,B0. Put ell=|B0-A|, e=(B0-A)/ell and choose a perpendicular unit n. Let beta be the width of B in direction n and c0 its transverse midrange. Since B touches all three sides of Delta, ell>=1/2. Also beta<=sqrt(2). Define

 T_rho(x,y,z)=(e.(x,y)/(1+rho),
                [n.(x,y)-c0(1-z)]/(beta+rho),
                z).

Its determinant magnitude is 1/[(1+rho)(beta+rho)]. It is invertible for every genuine chart point. No continuous choice of diameter endpoints is needed; all following bounds hold for every such choice.

Let K=T_rho(P). Then

 K subset Q:=[-1,1]^2 x [0,1],
 Vol(K)>=1/96.                                      (A)

Coordinate proof: before the longitudinal division, bottom coordinates have absolute value at most1 and top coordinates at most rho. Bottom transverse coordinates have absolute value at most beta/[2(beta+rho)]<=1/2; top transverse coordinates at most rho/(beta+rho)<=1.

Volume proof for 0<rho<=1: before the extra longitudinal factor1/(1+rho), use the diameter-width normalization. If beta>=rho, choose a bottom point at perpendicular distance at least beta/2 from the diameter line. The bottom triangle with the diameter endpoints has area>=ell beta/4; coning to any top vertex gives normalized volume>=ell beta/[12(beta+rho)]>=1/48. If rho>=beta, two top vertices have transverse separation>=rho/2, because the width of Delta in any unit direction is>=1/2. Their tetrahedron with the bottom diameter endpoints gives the same1/48 bound. Dividing longitudinally by1+rho<=2 proves1/96.

For rho>=1, the cone from ANY bottom point to the entire top triangle has original volume rho^2/6. Hence

 Vol(K)>=rho^2/[6(1+rho)(beta+rho)]>=1/36>1/96,

using1+rho<=2rho and beta+rho<3rho. This argument covers ALL coupled basal degeneracies; it never replaces actual solid moments by free weights.

## 3. A universal quantitative one-vertex-deletion lemma
Consider ANY ten-labelled convex hull K contained in Q with Vol(K)>=1/96 and actual centroid g. For one label z_i let

 K'=conv{z_j:j!=i}, delta=dist(z_i,K').

Choose q in K' attaining this distance and replace label i by q, retaining the other nine labels. The resulting ten-label list Z' contains every true vertex of K' and has at most nine true vertices.

For delta>0 put w=(z_i-q)/delta. Convexity gives the ONE-sided extrusion inclusion

 K' subset K subset K'+[0,delta w].

The area of the orthogonal projection of Q onto w-perpendicular is

 2|w_x|+2|w_y|+4|w_z|<=sqrt(24)<5.

This formula follows by summing the projections of the three visible box faces. Integrating line sections in the w direction therefore gives

 DeltaV:=Vol(K)-Vol(K')<=5delta.

If delta<=1/960, then Vol(K')>=1/96-5/960=1/192. Write g' for its actual uniform centroid. Exact mass decomposition and diam(Q)=3 yield

 ||g-g'||<=3DeltaV/Vol(K)<=1440delta.

Let x_j=z_j-g and x'_j=z'_j-g'. Thus

 epsilon:=max_j||x_j-x'_j||<=1441delta.

Both actual-centred row sets and all pair differences have norm<=3. For any PSD M, with D_ij=x_i^T M(x_j-x_i),

 |D'_ij-D_ij|<=9epsilon tr(M)<=12969delta tr(M).    (B)

Indeed D'-D=(x'_i-x_i)^T M(x_j-x_i)
 +(x'_i)^T M[(x'_j-x'_i)-(x_j-x_i)],
whose two terms are bounded by3epsilon||M||op and6epsilon||M||op. This uses both bodies' actual centroids and requires no quadratic approximation.

## 4. The precise universal gap and vertex robustness
Define Gamma_{9,192} as

 min max_{(i->j) in T} [-(z_i-g_Z)^T M(z_j-z_i)],

where the minimum ranges over ten-labelled configurations Z in Q whose hull has at most nine true vertices and volume>=1/192, over PSD M with tr M=1, and over all labelled rooted spanning trees T on the ten labels. The labels may coincide or lie inside true faces/edges/the body; g_Z is the genuine volume centroid.

The accepted nine-vertex PSD/refinement theorem implies

 Gamma_{9,192}>0.

Detailed compactness justification: the ten-label space is bounded; having at most nine extreme labels is the finite union of the closed conditions that one label belongs to the convex hull of the other nine. The volume threshold is closed and retains full dimension. The actual centroid is continuous on this set. Trace-one PSD matrices form a compact set, and there are finitely many trees. The theorem makes the displayed maximum strictly positive at every point of this compact product, so its minimum is positive.

Define the single constant

 xi=min{1/960, Gamma_{9,192}/12969}.                (C)

It is positive, universal and NOT numerically evaluated. It is distinct from the previous material's gamma9 defined with volume>=1/48. Those two gaps must not be identified.

If K as in(A) admitted a complete weak rooted tree for a nonzero PSD M and some true vertex had delta<xi, then the actual nine-vertex refinement K' would have, by the gap definition, a selected arrow D'<=-Gamma_{9,192}trM. But all original selected arrows are>=0, contradicting(B). Consequently EVERY true vertex of any such K satisfies

 dist(z_i,conv{z_j:j!=i})>=xi.                      (D)

This is actual geometric robustness, not a metric conditioning bound. Trace normalization includes singular matrices. The estimate rules out small vertex-deletion distances directly, not merely after choosing a convergent subsequence.

## 5. Lower rho bound from the top deletion
Take the two top labels with extreme n-coordinate, and project the third onto their segment at the same n-coordinate. The difference is purely longitudinal. Before T_rho its length is<=sqrt(2)rho, the diameter of the top triangle. Thus its normalized length is<=2rho/(1+rho). This supplies a legitimate point in the convex hull of the other nine labels. By(D),

 2rho/(1+rho)>=xi,
 rho>=xi/(2-xi).                                  (E)

The finite denominator is positive because xi<=1/960. Equality is retained as a necessary inequality. This treats all beta/rho rates and every bottom degeneration.

## 6. Explicit basal-wall deletion witnesses
The horizontal linear part of T_rho is diagonal in the orthonormal basis e,n, with singular values1/(1+rho) and1/(beta+rho). Both are<=1/rho. Hence a raw bottom replacement error of length<=s becomes a normalized error<=s/rho.

The following ten raw errors are valid upper bounds for deletion distances of actual bottom vertices:

 c-b;
 d-a;
 2(1-p-q);
 2p;
 2q;
 1-c;
 1-d;
 u;
 v;
 min(a,b)tau.                                     (F)

Here are all witnesses, so no basal wall is inferred from an unexamined limit:

1. Replace vertex0 by vertex1, giving error c-b.
2. Replace vertex5 by vertex4, giving error d-a.
3. Replace vertex2 by vertex3, giving error sqrt(2)(1-p-q)<=2(1-p-q).
4. For vertex1, use w=(1-t)Y0+tY2 with t=(c-b)/(1-b). Its horizontal coordinates are(c-tp,tp), so the error is sqrt(2)tp<=2p.
5. For vertex4, use w=(1-t)Y5+tY3 with t=(d-a)/(1-a). The coordinates are(tq,d-tq), so the error is sqrt(2)tq<=2q.
6. For vertex2, use w=(1-t)Y1+tY3 with t=p/(1-q). Its y-coordinate is p, and its x-error fromY2 is(1-c)(1-t)<=1-c.
7. For vertex3, use w=(1-t)Y4+tY2 with t=q/(1-p). Its x-coordinate is q, and its y-error fromY3 is(1-d)(1-t)<=1-d.
8. For vertex5, use w=(1-t)Y4+tY6 with t=(d-a)/(d-v). Since v<a<d, t is in(0,1). Its coordinates are(tu,a), giving error<=u.
9. For vertex0, use w=(1-t)Y1+tY6 with t=(c-b)/(c-u). Since u<b<c, t is in(0,1). Its coordinates are(b,tv), giving error<=v.
10. For vertex6, both points(u+b tau,v) and(u,v+a tau) lie on the true bottom segment joining Y0,Y5. Their errors are b tau and a tau. Use the shorter one.

Each replacement lies in the convex hull of the OTHER labels. All the listed t parameters lie in[0,1] by the literal strict chart inequalities. These arguments use only actual coordinates, not a projected boundary path or an assumed arrow packet.

Combining(F) with(D) yields the necessary inequalities

 min{c-b,d-a,2(1-p-q),2p,2q,1-c,1-d,u,v,
                         min(a,b)tau} >=rho xi.   (G)

In particular c-b<1 gives rho<1/xi. Let

 eta0=xi^2/(2-xi)>0.

Equations(E),(G) imply

 xi/(2-xi)<=rho<1/xi,
 c-b,d-a,1-c,1-d,u,v,min(a,b)tau >=eta0,
 p,q,1-p-q >=eta0/2.

Since a,b<1 and tau<1, the product bound also gives

 a,b,tau>=eta0.

Thus every U1 shape in the ENTIRE strict nine-modulus parallel chart lies in a compact subset specified by explicit inequalities involving only the universal constant xi. There can be no approach to any chart wall, rho=0 or rho=infinity. The accepted explicit EXPANSION7 theorem further improves the upper rho bound to rho<7, but it is not needed for this compactness deduction.

## 7. Limits and next use
Neither Gamma_{9,192}, xi nor eta0 has been numerically evaluated. Consequently the inequalities do not supply numerical endpoints for a finite parameter-box search. They provide a concrete interface: any valid numerical lower bound for the nine-vertex PSD/refinement gap on Q with volume>=1/192 immediately yields a uniform numerical compact box for all parallel U1 candidates.

A normalized intact ten-vertex shape can still have a singular rooted metric limit; no U1 metric condition-number bound is asserted. The compact non-small-cut interior may contain U1 shapes or may be excluded by a further actual geometric mechanism. Arbitrary nonparallel positive-projective moduli remain separate. No E17 incidence has been eliminated and no new110 construction is produced. The accepted global interval remains34<=C_min<=622, with lower prohibition and attainment distinct.
