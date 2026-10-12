# minimum-0232

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# RELATIVE_FACET_RANK_SEVEN_AND_PRIMAL_DUAL_CARRIER_ESCAPE_V2

Slot-5, Bright Harbor 33. Branch `[internal-source-reference]`. Same-branch continuation of `FIXED_FACET_CENTROID_RETRACTION_AND_MIXED_PACKET_ESCAPE_V1`.

## 1. Main advance

**Every genuine V10/E17/F9 realization admits arbitrary sufficiently small analytic deformations of any one of its facet polygons, in its fixed plane, with an analytic same-lattice extension through that very realization. The actual uniform centroid can simultaneously be kept fixed.** The previous three-anchor and two-outside-vertex hypotheses are no longer needed in this layer.

There is also a dual completion retaining the actual centroid of the ORIGINAL uniformly filled body, not the centroid of its polar. Combined with a relative incidence-rank theorem, this proves the following two genuine fixed-metric escape classes.

**Two-carrier theorem.** Let P be an actual uniformly filled V10/E17/F9 convex polytope at its volume centroid, with M positive definite and N=M^{-1}. Its entire weak packet has an analytic, same-lattice, actual-centroid-preserving resolution, retaining every original labelled strict equilibrium and keeping M and N fixed, whenever either of the following holds:

1. **Primal-facet carrier:** there is a true facet F such that every weak point is a VE whose exposed true edge belongs to F, or an EF/VF whose bearing facet is F.
2. **Primal-vertex-star carrier:** there is a true vertex v such that every weak point is an EF on a true edge incident to v, or a VE/VF located at v. Equivalently, the packet of the same-origin polar is carried by its true facet corresponding to v, in the first sense.

These are alternatives, not a theorem about the union of two separately carried packets. An EF/VF merely lying on F but borne by another facet does not meet condition 1. A VE at the other endpoint of an edge incident to v does not meet condition 2.

In particular, **every actual weak S1U1 first-layer body satisfying either carrier condition has arbitrarily close proper110 realizations of the same lattice**. No feasible S1U1 input is asserted. The accepted internal bounds remain 34<=C_min<=622; no whole-layer exclusion, new attaining body, or global density result follows. The supplied index theorem already makes strict H=0 automatic for weak S1U1. fileciteturn0file2L9-L13 fileciteturn0file1L7-L15

A new exact heptagon/three-outside-vertex control demonstrates the extension beyond BOTH old incidence hypotheses. It has strict (S,U,H)=(4,5,7), four VE points and one VF, and therefore is expressly **not S1U1**. Its complete source-only recovery and continuous certificate appear below.

## 2. Research route and source authority

The unchanged journal, selected atlas, radial-index source, and literal parent hY remain the inputs read in the preceding turn; no new source pack was supplied. The exact literal parent is `minimum-0230`, SHA-256 `daa0643fe164f5e11709744cc9493058547276f9356231fc732b06ef31aef86e`. Its actual flag identities and reduced physical selectors are retained unchanged.

Rather than finding another isolated metric blockage, I examined the relative incidence Jacobian obtained when the ENTIRE carrying polygon is prescribed. The ordinary full-row-rank proof in the atlas does not immediately settle this relative problem: its pinned boundary vertices need not have four incident nonzero stress coefficients. The new boundary count below is the additional argument. fileciteturn0file0L163-L186

A Tutte–Maxwell construction was considered but not used. The checked formulation has a triangular outer face and does not supply the local arbitrary-heptagon extension through the given realization that is needed here. No generic edge-length-rigidity claim is substituted for relative incidence surjectivity. citeturn630684view0

## 3. Relative incidence-rank theorem

### 3.1 Statement

Let P be ANY genuine convex three-polytope, with an interior origin and a true m-gonal facet F in the fixed plane

    H={x:q.x=1}.

Prescribe the positions of all m labelled vertices of F in H. The remaining unknowns are the three coordinates of each vertex outside F and the three coordinates of each normalized pole q_G, G!=F. Impose every true incidence outside F:

    C_iG = q_G.X_i-1 = 0,        G!=F, i in G.

Let B be their Jacobian with respect to those remaining unknowns.

**Relative-rank lemma.** B has full row rank at every genuine realization if m<=7, or if at most two vertices lie outside F.

It follows that every sufficiently small analytic prescribed polygon deformation in H extends analytically through the given P, with the same true lattice. This is a local statement at EVERY such realization, not merely global existence of some realization with the desired facet.

### 3.2 A row dependence has a planar support graph

Suppose omega_iG is a nonzero row dependence. At each unpinned vertex and each unpinned facet its balances are

    sum_{G incident i} omega_iG q_G = 0,          i outside F,
    sum_{i in G} omega_iG X_i = 0,               G!=F.       (3.1)

Any at most three vertex vectors in one true facet are linearly independent. Indeed three true vertices cannot be collinear, and their supporting plane does not contain the origin. The same assertion holds for at most three incident poles at a true vertex, by applying the same reasoning to the corresponding true polar facet.

Draw the support of omega in the radial vertex–facet incidence graph on the polyhedral sphere, deleting the F-node. Every nonisolated unpinned node consequently has degree at least four. The only nodes without that requirement are the b vertices of F incident to a nonzero coefficient; call them boundary nodes. They lie on one common empty face.

A facet-node G has at most two boundary neighbors. When there are two, they are endpoints of a true edge of F: two distinct true facets intersect in at most one true edge, not in three vertices or in a diagonal. This is where genuine incidence is essential.

A component with no boundary node would be a nonempty simple planar bipartite graph of minimum degree four. The usual edge bound excludes it. Thus every support component meets the boundary.

### 3.3 The boundary count forces at least eight pinned vertices

First suppose b>=3. Join consecutive boundary nodes by a cycle drawn in the empty F-region. The augmented graph is connected and simple, with that b-cycle as its outer face. Write n_0 for its number of unpinned nodes, D for the number of original support incidences at boundary nodes, and t for its number of bounded triangular faces.

Every bounded triangle has exactly one added boundary edge and one facet-node. Since a facet-node has at most two boundary neighbors, no boundary-to-facet incidence can belong to two such triangles. Therefore

    D>=b,                 D>=2t.                            (3.2)

All other bounded faces have boundary-walk length at least four. Euler's formula, counting face boundary walks, gives

    e_aug <= 2(n_0+b)-2-b/2+t/2.

On the other hand the minimum degree four at unpinned nodes gives

    e_aug = e_support+b >= 2n_0+D/2+b.

Combining them yields the crucial inequality

    D <= b-4+t.                                            (3.3)

Equations (3.2)–(3.3) imply

    4 <= t <= b-4,          hence b>=8.                    (3.4)

The small boundary cases do not escape this argument. If b=0, use the planar bipartite bound directly. For b=1 or 2, add unused vertices of F solely to form a three-vertex outer cycle. When b=1 there is no bounded triangle and (3.3), with outer length three, gives D<=-1. When b=2 there is at most one bounded triangle: the two active boundary vertices can lie together in only one facet G!=F. The same count gives D<=0, contrary to D>=2.

Thus a dependence requires at least eight actually active pinned vertices. In particular none exists when m<=7.

The count also supplies a reusable necessary anatomy for a relative-rank failure outside this range:

    b>=8,
    4<=t<=b-4,
    max(b,2t)<=D<=b+t-4,

with every unpinned support node of degree at least four. These are conditions for failure of this relative incidence Jacobian, NOT sufficient conditions for a mechanical obstruction or for failure of all genuine deformations.

### 3.4 Two outside vertices

If at most two vertices lie outside F, every supported facet-node must contain both of them: it needs at least four support incidences and can use at most two boundary vertices. But two true vertices belong together to at most two true facets. Each supported outside vertex would then have support degree at most two, contradicting the required degree at least four. The one-outside-vertex case is even more immediate.

This proves the second alternative without assuming that either outside vertex is simple, or that the outside edge is parallel to F.

### 3.5 Genuine extension, and a deterministic local lifting recipe

Since B has full row rank, the implicit function theorem solves all the incidences for the free variables near their original values. Strict nonincidence slacks, independence of supporting triples at every vertex, and strict convexity of each labelled facet polygon persist in a sufficiently small neighborhood. Consequently this is a true same-lattice realization, not only an incidence solution with collapsed labels.

There is a direct reproducible tangent prescription. For a specified boundary velocity let

    eta_iG=q_G.X_i' if i belongs to F, and eta_iG=0 otherwise.

In the fixed ordering of free vertex/pole coordinates choose

    z' = -B^T (B B^T)^(-1) eta.                            (3.5)

The matrix in this formula is only a parameter-space linear-algebra device, not an independently selectable mechanical metric. For an analytic boundary path, evaluate B and eta at the moving realization and solve the same analytic ODE with initial value z(0)=z_0. Then dC/dt=Bz'+eta=0 identically. Local full rank gives an analytic same-lattice lift. Alternatively, hold the nonpivot variables fixed and use the lexicographically first nonsingular square column minor of B in the implicit function theorem.

At rational input, a rational prescribed first velocity gives an exactly rational first lift. No finite-order guess about the later arc is needed.

### 3.6 Consequences for the first layer and its polar

A facet of a V10/E17/F9 polytope has at most eight vertices. Nine would leave one apex and make a nine-gonal pyramid, with eighteen rather than seventeen edges. Thus every facet is covered by m<=7 or by the two-outside-vertex case.

For the same-origin polar, the facet sizes are the primal vertex degrees. Since

    sum_v(deg(v)-3)=2E-3V=4,

every one of its facets has at most seven vertices. Therefore the relative-rank lemma applies to EVERY polar facet too.

This eliminates the previous `|F|<=7 with an overloaded other facet` residue for a one-facet-carried packet. An overloaded four-anchor quad is not merely insufficient to prove obstruction: the complete first-layer polygon extension now exists regardless of such overloads.

## 4. Actual uniform-centroid completion on both sides

Throughout this section M stays fixed and N is that same fixed inverse. The maps below physically deform the body. They are not passive affine renormalizations followed by a metric reset.

### 4.1 Primal polygon: exact affine retraction

For any nearby raw extension Q whose prescribed facet stays in H={x:q.x=1}, compute its ACTUAL uniform centroid g and put h=1-q.g>0. The exact affine map

    C_g(x)=x-g(1-q.x)/h                                    (4.1)

fixes H pointwise and sends g to zero. Its linear determinant is 1/h>0. Thus C_g(Q), uniformly filled, has its own centroid zero and the same face lattice, while preserving the entire prescribed polygon.

The raw pole p_G transforms to

    q_G^new=[p_G-(p_G.g)q]/[1-p_G.g].                       (4.2)

The selected q is unchanged. The centroid is always computed from the genuine oriented boundary fan:

    D=sum det(Y_a,Y_b,Y_c),
    J=sum det(Y_a,Y_b,Y_c)(Y_a+Y_b+Y_c),
    g=J/(4D).                                             (4.3)

These are the actual-volume quantities of the supplied parent. They are not free masses or a formal centroid completion. fileciteturn0file2L1044-L1061

At an initially centred body the corrected vertex velocity is

    X_i'^new=Y_i'-(1-q.X_i)g'.                             (4.4)

The correction vanishes at every prescribed vertex of F.

### 4.2 Polar polygon: centre the original body, not the polar

Let R(t) be a raw extension of a prescribed facet of the polar, in

    H_v={r:v.r=1},

where v is the corresponding fixed primal vertex. Put Q(t)=R(t)^circ. Its actual uniform centroid need not be zero.

For a covector p in the positive-denominator domain define

    T_p(x)=x/(1+p.x),
    V_Q(p)=integral_Q (1+p.x)^(-4) dx,
    g_Q(p)=integral_Q x(1+p.x)^(-5) dx / V_Q(p).            (4.5)

Here g_Q(p) is precisely the uniform volume centroid of the PROJECTIVE IMAGE T_p(Q). The exponents four and five are mandatory; transporting the old centroid, or uniformly centring R instead, would be wrong.

Use the actual-volume projective centring mechanism already recorded in the journal, with the following explicit linear finish. Choose the unique centring p=p(Q) and set

    Q_hat=(I+v p^T) T_p(Q).                                (4.6)

The linear factor preserves a zero centroid. More importantly, its induced map on the polar is exactly

    R_hat = { r + [p/(1+p.v)](1-v.r) : r in R }.            (4.7)

This is an affine map fixing the entire plane H_v POINTWISE. It leaves the prescribed polar polygon unchanged and preserves the true lattice. The polar metric is still N=M^{-1}; no polar volume centroid enters. The journal's actual projective centroid law is used here, not a new independent-polar density assumption. fileciteturn0file2L342-L347

For completeness, the required centring exists uniquely. The positive domain is bounded because 0 is interior to Q. Its volume functional satisfies

    grad V_Q=-4 V_Q g_Q,
    Hess V_Q=20 integral_Q xx^T(1+p.x)^(-6) dx >0.

As p approaches its domain boundary, take a fixed nonzero tetrahedral cone at a vertex where the denominator tends to zero. A portion of linear size proportional to that denominator has volume of order its cube and integrand of order its inverse fourth power. Hence V_Q diverges. It therefore has a unique interior minimizer, where g_Q=0. Also 1+p.v>0, since v belongs to Q, so the linear factor in (4.6) is invertible. Formula (4.7) follows directly by applying (I+vp^T)^(-T) to r+p.

At an initially own-centred P, the centring parameter is p=0. For the actual primal covariance Sigma=E_P[xx^T],

    D_p g_Q(0)=-5 Sigma,                                  (4.8)

an invertible matrix. Thus centring is analytic along any sufficiently small analytic raw extension, and is the identity at the original body. If the raw primal centroid velocity is c, then

    p'=(5 Sigma)^(-1)c,
    r_i'^new=r_i'+(1-v.r_i)p'.                            (4.9)

Again the correction vanishes on the prescribed polar facet. Equation (4.8) can also be read directly from (4.5), using the actual initial centroid zero. It retains the real moving-volume law at all orders, not just its first jet. fileciteturn0file2L279-L281

Accordingly, the local image of either a primal or a polar facet-restriction map is unchanged by imposing the actual ORIGINAL-body centroid condition. On the primal side x -> x+b(1-q.x) fixes the carrier and has centroid b at an initially centred body, so the centroid map has rank three within the fixed-polygon fibre; on the polar side (4.8) gives rank three. Where the relative-rank lemma applies, the fibre over a fixed m-gon and fixed carrier plane is smooth of dimension E-2m after actual centring. This is a count in vertex-position coordinates with the carrier plane fixed, not the atlas's affine-normalized parameter count.

## 5. Simultaneous mixed-carrier escape

The following construction works for a carrier in either body. In the primal use its metric M; in the polar use N. Denote the chosen body's metric by A and its inverse by A^{-1}, and write its carrying plane as q.x=1. Put

    s=q^T A^{-1}q,
    p=A^{-1}q/s,
    y_i=X_i-p,
    r_i=y_i^T A y_i.

Prescribe the carrier polygon by

    Y_i(t)=X_i+t(K r_i y_i+a),       q.a=0.                 (5.1)

If there is no EF/VF borne by the carrier, take a=0. At a bearing EF, choose a=z-p with z in the relative interior of the carrier polygon. At a bearing VF v=p, choose a equal to either outgoing carrier edge e_1 or e_2, according to the desired paired selector. There is at most one such EF or VF on the carrier because its perpendicular foot is unique.

For all VE rows i->j in the carried packet, take for example

    K=1+sum_VE |a^T A e_ij|/[r_i(e_ij^T A e_ij)].           (5.2)

Every denominator is strictly positive. At a VE the equalities and inequalities are

    y_i^T A e_ij=0,
    r_j-r_i=e_ij^T A e_ij>0,
    r_i>0.

If r_i were zero, that point would instead be a VF borne by the carrier. Differentiation gives

    P_ij'(0)=K r_i(e_ij^T A e_ij)+a^T A e_ij>0.            (5.3)

This opens arbitrary consecutive or endpoint-sharing VE chains; disjoint endpoint footprints are not required.

At an EF borne by the carrier, let r be the actual neighboring pole across its foot edge. The radial parts of (5.1) are along that edge at its two endpoints. Differentiating the actual endpoint incidence equations and using the barycentric expression for the foot gives

    Q_qr'(0)=-s(r-q).a>0.                                 (5.4)

The last sign follows from a=z-p with z in the carrier's relative interior.

At a bearing VF, choose a=e_1. In the literal parent's notation v-p=E u and G=E^T A E, this gives u'(0)=(1,0), hence

    P_1'(0)=e_1^T A e_1>0,
    Q_2'(0)=s delta_2>0.                                  (5.5)

These are the complementary CROSS-edge exits. The proof works for acute, obtuse and right corners. At a right corner it succeeds at first order and therefore does not invoke, discard or weaken the parent's higher-jet threshold. Choosing a=e_2 realizes the other paired choice. fileciteturn0file2L903-L944 fileciteturn0file2L991-L1042

Use the relative-rank lemma to extend (5.1), then the corresponding actual-centroid retraction of Section 4. Both corrections fix the full carrier polygon. VE primitives on its edges are unchanged by the correction; the EF/VF exit signs are determined by the same carrier foot/edge data and their strictly positive genuine incidence factors. Thus (5.3)–(5.5) remain valid.

All originally nonzero primitives retain their signs in a sufficiently small neighborhood. The supplied extremal-selector equivalence therefore removes every physical weak point and preserves the exact original strict S,U,H labels. No weak-edge group or demand that all algebraic zeros disappear is added. fileciteturn0file1L78-L102

For a polar carrier, the same-origin polarity simply interchanges the two primitive families: its primal rows are the original Q rows, and its polar rows are the original P rows, using the SAME N and M. This proves the primal-vertex-star alternative without ever refilling and independently centring the polar.

### Consequence for positive full-realization stresses

Consider any fixed paired VF selector, or its valid compressed version. A nonzero nonnegative dependence among its derivatives on the full actual-centred realization/metric tangent space **cannot have all of its physical support carried by a single primal facet or by a single primal vertex star**.

Indeed the corresponding flow above can be chosen for just that supported subpacket, with the selected VF branch, and makes every supported selected derivative strictly positive. Evaluating the alleged dependence gives a strictly positive number rather than zero. Derivatives at contacts outside the support do not enter this contradiction.

This is not an isolation theorem: such a flow may affect other contacts on other carriers. It does not justify resolving a multi-carrier packet sequentially while assuming that all other weak rows remain unchanged.

## 6. New exact heptagon/three-outside control

### 6.1 Complete initial geometry

Start with the seven raw base vertices, all at z=10, whose horizontal coordinates are

    (0,0), (1,0), (1,1/2), (3/4,1),
    (1/4,11/8), (-7/16,3/2), (-1,1/2).

The three raw top vertices 7,8,9 are

    (-57/16,-1,-30), (5/2,-1,-30), (-6/17,80/17,-30).

Equivalently their horizontal triangle is cut out by y>=-1, 2x+y<=4 and -x+(9/16)y<=3. Its sides are parallel to the true base edges 01,23,56 respectively.

The labelled maximal faces, with outward orientation restored by the source, are

    F0=(0,1,2,3,4,5,6), F1=(7,8,9),
    F2=(0,1,8,7), F3=(1,2,8), F4=(2,3,9,8),
    F5=(3,4,9), F6=(4,5,9), F7=(5,6,7,9), F8=(6,0,7).

Apply (4.1) once to this raw body, using q=(0,0,1/10) and its exact actual uniform centroid. This leaves the seven base vertices unchanged. The resulting own-centred top vertices are exactly

    X7=(-126008631/40491688, -93613087/40491688, -1653110/297733),
    X8=(238944455/80983376, -93613087/40491688, -1653110/297733),
    X9=(7903647/80983376, 137427721/40491688, -1653110/297733).

Use M=N=I. The exact volume is 22334348535/161966752. The strict labels are

    S={1,2,4,7},
    U={5,6,7,8,9},
    H={1-8,5-6,5-9,6-7,7-8,7-9,8-9}.

The physical weak packet consists of VE rows 1->2, 2->3, 3->4, 4->5 and the single VF (vertex0,F0). The VF is represented on two weak edges, 01 and 06. There are eight zero primitives:

    P01, P06, Q02, Q08, P12, P23, P34, P45.

All sixty other true-edge primitives are nonzero.

### 6.2 Why this is beyond both previous incidence hypotheses

The vertex degrees are (3,3,3,3,3,3,3,4,4,5). Thus all three outside vertices are nonsimple. The old anchor set is the ENTIRE vertex set. Its three quads F2,F4,F7 all contain four anchors, violating the old three-anchor condition, while three outside vertices violate the old two-outside condition.

Only F0 is completely plane-movable. There is no second private centroid-corrector facet. Nevertheless the relative Jacobian has 27 rows, 33 columns and exact rank27. The source returns the complete matrix, pivot columns and a nonzero 27-by-27 rational minor.

### 6.3 The actual continuous curve

Use (5.1) with p=(0,0,10), a=(1,0,0), K=1. For this control those values already make every required VE derivative positive.

An explicit same-lattice raw extension is available. Keep the initial centred top height fixed. For each k=0,2,5 let e_k(t)=Y_{k+1}(t)-Y_k(t) be the moving base edge and let n_k(t)=(e_{k,y}(t),-e_{k,x}(t)). Keep the top-line constant n_k(0).X_top fixed, using top labels 7,8,9 respectively. Define the three top vertices by intersecting these three moving lines pairwise in their unchanged horizontal plane, in the same cyclic order as above.

This preserves every real quad: its two edges remain parallel and lie at the two distinct heights. The two polygonal horizontal faces and four remaining triangular side faces are exact as well. Recompute the ACTUAL raw volume centroid and apply (4.1) at each t. This is not a frozen-centroid calculation.

The four VE first derivatives are

    1/4, 9/64, 113/1024, 4361/16384.

For the VF the paired derivatives are

    P01'=1,        Q08'=15743496/7830870125>0.

Its exact mismatch is u_1=t/(1+t), u_2=0. Consequently

    P01=t(1+t)>0,
    Q08=s delta_2(t)t/(1+t)>0,
    Q02=0,
    P06=-t(1+t r_6)<0.                                    (6.1)

The zero Q02 is harmless, not an unremoved physical equilibrium. The raw centroid genuinely moves; for example its raw z-derivative is exactly 80557840130090971755/14886199969243886336. After the correction the actual centroid is identically zero.

The planar projective velocity matrix has rank8; adjoining this prescribed polygon velocity raises its rank to9. Therefore the resulting actual motion leaves the labelled projective orbit already at first order. This does not claim that every projective direction is blocked on this control.

### 6.4 Verification scope

The source certifies the WHOLE interval

    0<t<=1/1024,

not a finite sample. Exact rational interval arithmetic proves 224 positive guards, including actual support slacks, strict facet convexity, all sixteen boundary-fan triangles, centroid and pole denominators, all sixty protected nonzero primitive signs, and the positive exit quotients in (6.1) and for the four VE points. Every interval division has its denominator certified away from zero.

Planarity for all t follows from the explicit parallel-edge construction and the final affine map, as proved above; it is not inferred from interval boxes containing zero. The source additionally checks actual incidences and centroid at the full first jet and at the exact endpoint, and independently audits the endpoint's complete strict/weak census. Throughout the interval the strict labels remain (4,5,7) and the physical weak count is zero. The sole algebraic zero at the endpoint, and identically along the positive arc, is Q02.

This is a genuine first-layer geometric control with more than three physical weak points and with all three outside vertices coupled through overloaded quads. It is NOT a first-layer S1U1 witness, exclusion or attaining construction.

## 7. Recovery and actual execution status

Save the complete source in Section 9 as `relative_facet.py`, UTF-8, LF line endings, with a final newline. Dependencies: CPython3.13.5 standard library only; assertions enabled. There are no random seeds, external data files, old parent workspace dependencies, or floating-point solvers.

Commands:

    python -B -S relative_facet.py build
    python -B -S relative_facet.py check

Expected terminal marker:

    RELATIVE_FACET_SEVEN_HEPTAGON_ACTUAL_COM_INTERVAL_PASS

Expected summary line:

    RANK 27 GUARDS 224 STRICT 4 5 7 WEAK 5 TO 0

Exact pins:

    relative_facet.py: 14797 bytes
    SHA256 7a9bc1e64dd0694d89b1b0bdc4c860b84cde496320411bc2ee2286155bc3e317
    relative_facet_report.json: 192862 bytes
    SHA256 311285d2246e06f56931aabb4971323bd407627e0624d7380ede1d89361e979e

Build/check and a fresh source-only build/check were actually executed successfully in this continuation. The fresh report was compared byte-for-byte with the original and matched. The general relative-rank and centroid-completion theorems are analytic proofs, not conclusions inferred from this one control or proof-assistant formalizations.

Convenience copies: [complete source](sandbox:/mnt/data/facet_relative/relative_facet.py) and [complete exact report](sandbox:/mnt/data/facet_relative/relative_facet_report.json). The report includes all exact endpoint coordinates, poles, rows, labelled censuses, interval bounds and the full relative matrix. The source below reconstructs them without these links.

The preceding four controls and their `facet_anchor.py` recovery remain unchanged and useful. Their source SHA is `93b928295fccf90bb58a6d5309dcc0d7acb8805c3ce7440ef769c6f10447ac36`. They are not discarded or replaced by the new control; what is superseded is the need for the old geometric hypotheses when proving a one-carrier first-layer escape.

## 8. Precise remaining first-layer obstacle

The completed step is local extension and actual-COM completion for an ENTIRE individual carrier, on either side of the same inverse pair. The previous overloaded-anchor residue is therefore no longer an open obstruction for a first-layer packet carried by one facet.

I have not proved that every actual S1U1 packet has either carrier. A genuine all-orders counterexample would have to have at least four physical weak points by the previously accepted <=3 theorem, and its complete packet would have to fail BOTH carrier tests above. For every paired selector, first-order failure would require a nonnegative full-tangent dependence; the physical support of that dependence must also fail both one-carrier tests. The four-point requirement concerns an all-orders counterexample's COMPLETE packet, not the support size of an individual first-order stress. fileciteturn0file2L299-L302

No implication is proved from failure of a carrier test to nonregularizability. Likewise, the present flows do not isolate a carrier from other weak contacts, so combining or sequencing them requires a simultaneous sign argument. The remaining issue is a contact packet not carried by any single primal or polar facet, with its actual centroid and genuine incidence still enforced. That is the useful continuation, rather than further tests of the obsolete four-anchor obstruction in a singly carried first-layer packet.

## 9. Complete runnable recovery source

```python
"""RELATIVE_FACET_RANK_SEVEN_AND_MIXED_HEPTAGON_V1.
CPython 3.13.5 standard library; exact fractions; assertions enabled.
No external inputs, parent files, random seeds, or numerical solver.
python -B -S relative_facet.py build
python -B -S relative_facet.py check
The actual 10/17/9 control has strict (S,U,H)=(4,5,7), NOT S1U1.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json,sys
EPS=F(1,2**10)

class Jet:
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    @staticmethod
    def cast(x): return x if isinstance(x,Jet) else Jet(x)
    def __add__(s,t):
        t=s.cast(t);return Jet(s.a+t.a,s.b+t.b)
    __radd__=__add__
    def __neg__(s): return Jet(-s.a,-s.b)
    def __sub__(s,t): return s+-s.cast(t)
    def __rsub__(s,t): return s.cast(t)+-s
    def __mul__(s,t):
        t=s.cast(t);return Jet(s.a*t.a,s.b*t.a+s.a*t.b)
    __rmul__=__mul__
    def __truediv__(s,t):
        t=s.cast(t);assert t.a
        return Jet(s.a/t.a,(s.b*t.a-s.a*t.b)/(t.a*t.a))
    def __rtruediv__(s,t): return s.cast(t)/s
    def __eq__(s,t):
        t=s.cast(t);return (s.a,s.b)==(t.a,t.b)

class Box:
    def __init__(self,l=0,u=None):
        self.l,self.u=F(l),F(l if u is None else u);assert self.l<=self.u
    @staticmethod
    def cast(x): return x if isinstance(x,Box) else Box(x)
    def __add__(s,t):
        t=s.cast(t);return Box(s.l+t.l,s.u+t.u)
    __radd__=__add__
    def __neg__(s): return Box(-s.u,-s.l)
    def __sub__(s,t): return s+-s.cast(t)
    def __rsub__(s,t): return s.cast(t)+-s
    def __mul__(s,t):
        t=s.cast(t);v=[s.l*t.l,s.l*t.u,s.u*t.l,s.u*t.u]
        return Box(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(s,t):
        t=s.cast(t);assert t.l>0 or t.u<0,('interval denominator',t.l,t.u)
        return s*Box(1/t.u,1/t.l)
    def __rtruediv__(s,t): return s.cast(t)/s

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))
def mul(s,a): return tuple(s*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a): return dot(a[0],cross(a[1],a[2]))
def solve(a,b=(F(1),)*3):
    d=det(a);return tuple(det(tuple(tuple(b[i] if j==k else a[i][j] for j in range(3)) for i in range(3)))/d for k in range(3))
def vec(x): return tuple(map(F,x))

def moment(x,faces):
    d=0;j=(0,0,0)
    for f in faces:
        for k in range(1,len(f)-1):
            a,b,c=(x[i] for i in (f[0],f[k],f[k+1]))
            w=det((a,b,c));d+=w;j=add(j,mul(w,add(a,add(b,c))))
    return d,mul(1/(4*d),j)

def orient(x,faces):
    o=mul(F(1,len(x)),tuple(sum(v[k] for v in x) for k in range(3)))
    out=[]
    for f in faces:
        n=cross(sub(x[f[1]],x[f[0]]),sub(x[f[2]],x[f[0]]))
        out.append(tuple(reversed(f)) if dot(n,sub(o,x[f[0]]))>0 else tuple(f))
    return tuple(out)

def center(x,faces,q):
    d,g=moment(x,faces);h=1-dot(q,g)
    return [sub(v,mul((1-dot(q,v))/h,g)) for v in x]

def incidence(faces,n):
    fs=[tuple(f for f,ids in enumerate(faces) if i in ids) for i in range(n)]
    edges=sorted({tuple(sorted((f[k],f[(k+1)%len(f)]))) for f in faces for k in range(len(f))})
    assert n-len(edges)+len(faces)==2
    assert all(len([f for f in faces if i in f and j in f])==2 for i,j in edges)
    return fs,edges

def primitives(x,q,faces):
    _,edges=incidence(faces,len(x));out={}
    for i,j in edges:
        f,h=[f for f,ids in enumerate(faces) if i in ids and j in ids]
        for a,b in ((i,j),(j,i)):out['P:%d:%d'%(a,b)]=dot(x[a],sub(x[b],x[a]))
        for a,b in ((f,h),(h,f)):out['Q:%d:%d'%(a,b)]=dot(q[a],sub(q[b],q[a]))
    return out

def audit(x,faces):
    q=[solve([x[i] for i in f[:3]]) for f in faces]
    fs,edges=incidence(faces,len(x))
    for f,ids in enumerate(faces):
        assert all(dot(q[f],x[i])==1 for i in ids)
        assert all(dot(q[f],x[i])<1 for i in range(len(x)) if i not in ids)
        for k,i in enumerate(ids):
            j=ids[(k+1)%len(ids)]
            assert all(dot(q[f],cross(sub(x[j],x[i]),sub(x[l],x[i])))>0 for l in ids if l not in (i,j))
    assert all(solve([q[f] for f in ids[:3]])==x[i] for i,ids in enumerate(fs))
    d,g=moment(x,faces);assert d>0 and g==(0,0,0)
    rows=primitives(x,q,faces)
    us=[i for i in range(len(x)) if max(rows['P:%d:%d'%(i,j)] for j in range(len(x)) if tuple(sorted((i,j))) in edges)<0]
    wv=[i for i in range(len(x)) if max(rows['P:%d:%d'%(i,j)] for j in range(len(x)) if tuple(sorted((i,j))) in edges)==0]
    sf=[];wf=[]
    for f in range(len(faces)):
        vv=[v for k,v in rows.items() if k.startswith('Q:%d:'%f)]
        if max(vv)<0:sf.append(f)
        if max(vv)==0:wf.append(f)
    saddles=[];we=[]
    for i,j in edges:
        f,h=[f for f,ids in enumerate(faces) if i in ids and j in ids]
        vv=[rows['P:%d:%d'%(i,j)],rows['P:%d:%d'%(j,i)],rows['Q:%d:%d'%(f,h)],rows['Q:%d:%d'%(h,f)]]
        if max(vv)<0:saddles.append((i,j))
        elif max(vv)==0:we.append((i,j))
    assert len(sf)+len(us)-len(saddles)==2
    vf=[(i,f) for i in wv for f in wf if i in faces[f] and x[i]==mul(1/dot(q[f],q[f]),q[f])]
    physical=len(wv)+len(wf)-len(vf)
    return dict(vertices=x,faces=faces,poles=q,volume=d/6,centroid=g,edges=edges,
                stable=sf,unstable=us,saddles=saddles,counts=[len(sf),len(us),len(saddles)],
                weak_vertices=wv,weak_facets=wf,weak_edges=we,VF=vf,physical_weak_count=physical,
                zeros=[k for k,v in rows.items() if v==0],rows=rows,
                degrees=[len(f) for f in fs],M=((1,0,0),(0,1,0),(0,0,1)),N=((1,0,0),(0,1,0),(0,0,1)))


def inter2(l,r,z):
    a,b,c=l;d,e,f=r;den=a*e-b*d
    return ((c*e-b*f)/den,(a*f-c*d)/den,z)

def fixture():
    xy=((0,0),(1,0),(1,F(1,2)),(F(3,4),1),
        (F(1,4),F(11,8)),(-F(7,16),F(3,2)),(-1,F(1,2)))
    x=[vec((u,v,10)) for u,v in xy]
    lines=(vec((0,-1,1)),vec((2,1,4)),vec((-1,F(9,16),3)))
    x += [inter2(lines[2],lines[0],F(-30)),
          inter2(lines[0],lines[1],F(-30)),
          inter2(lines[1],lines[2],F(-30))]
    faces=((0,1,2,3,4,5,6),(7,8,9),(0,1,8,7),(1,2,8),
           (2,3,9,8),(3,4,9),(4,5,9),(5,6,7,9),(6,0,7))
    faces=orient(x,faces);raw=x;x=center(x,faces,vec((0,0,F(1,10))))
    a=audit(x,faces)
    assert a['counts']==[4,5,7] and a['physical_weak_count']==5
    assert a['VF']==[(0,0)] and a['weak_vertices']==[0,1,2,3,4]
    assert a['weak_facets']==[0]
    assert set(a['zeros'])=={'P:0:1','P:0:6','Q:0:2','Q:0:8',
                            'P:1:2','P:2:3','P:3:4','P:4:5'}
    assert a['degrees']==[3,3,3,3,3,3,3,4,4,5]
    assert a['volume']==F(22334348535,161966752)
    a['raw_generator_vertices']=raw
    return a

def arc(a,t):
    x,faces=a['vertices'],a['faces'];q=a['poles'][0]
    p=mul(1/dot(q,q),q);raw=list(x)
    for i in range(7):
        y=sub(x[i],p)
        raw[i]=add(x[i],mul(t,add(mul(dot(y,y),y),(1,0,0))))
    # Three top sides stay parallel to genuine basal edges 01,23,56.
    # Each line has its initial support constant but its moving edge normal.
    lines=[]
    for k,top in ((0,7),(2,8),(5,9)):
        e=sub(raw[(k+1)%7],raw[k]);e0=sub(x[(k+1)%7],x[k])
        c=e0[1]*x[top][0]-e0[0]*x[top][1]
        lines.append((e[1],-e[0],c))
    z=x[7][2]
    raw[7]=inter2(lines[2],lines[0],z)
    raw[8]=inter2(lines[0],lines[1],z)
    raw[9]=inter2(lines[1],lines[2],z)
    rq=[q]+[solve([raw[i] for i in f[:3]]) for f in faces[1:]]
    d,g=moment(raw,faces);h=1-dot(q,g)
    xx=[sub(v,mul((1-dot(q,v))/h,g)) for v in raw]
    qq=[mul(1/(1-dot(v,g)),sub(v,mul(dot(v,g),q))) for v in rq]
    return xx,qq,raw,rq,d,g,lines

def eliminate(matrix):
    a=[list(map(F,row)) for row in matrix];r=0;piv=[]
    for c in range(len(a[0])):
        k=next((k for k in range(r,len(a)) if a[k][c]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];v=a[r][c];a[r]=[w/v for w in a[r]]
        for k in range(len(a)):
            if k!=r:
                v=a[k][c];a[k]=[w-v*z for w,z in zip(a[k],a[r])]
        piv.append(c);r+=1
        if r==len(a):break
    return r,piv

def determinant(a):
    a=[list(map(F,row)) for row in a];d=F(1);n=len(a)
    for i in range(n):
        k=next((k for k in range(i,n) if a[k][i]),None)
        if k is None:return F(0)
        if k!=i:a[i],a[k]=a[k],a[i];d=-d
        v=a[i][i];d*=v
        for k in range(i+1,n):
            t=a[k][i]/v
            for j in range(i+1,n):a[k][j]-=t*a[i][j]
    return d

def relative_rank(a):
    x,q,faces=a['vertices'],a['poles'],a['faces']
    out=sorted(set(range(10))-set(faces[0]))
    cols=[('X',i,k) for i in out for k in range(3)]
    cols += [('Q',f,k) for f in range(1,9) for k in range(3)]
    rows=[(i,f) for f in range(1,9) for i in faces[f]]
    b=[]
    for i,f in rows:
        b.append([q[f][k] if typ=='X' and j==i else
                  x[i][k] if typ=='Q' and j==f else F(0)
                  for typ,j,k in cols])
    rank,piv=eliminate(b)
    assert (len(rows),len(cols),rank)==(27,33,27)
    minor=[[row[k] for k in piv] for row in b];d=determinant(minor);assert d
    ns={i for i,dg in enumerate(a['degrees']) if dg>3}
    anchors=set(faces[0])|ns
    overloaded=[f for f in range(1,9) if len(set(faces[f])&anchors)>3]
    movable=[f for f,ids in enumerate(faces) if all(a['degrees'][i]==3 for i in ids)]
    assert ns=={7,8,9} and overloaded==[2,4,7] and movable==[0]
    rr=[];rhs=[]
    for i in faces[0]:
        u,v,_=x[i];r=u*u+v*v
        rr += [(u,v,1,0,0,0,-u*u,-u*v),(0,0,0,u,v,1,-u*v,-v*v)]
        rhs += [r*u+1,r*v]
    assert eliminate(rr)[0]==8
    assert eliminate([list(row)+[h] for row,h in zip(rr,rhs)])[0]==9
    return dict(rows=rows,columns=cols,matrix=b,rank=rank,pivot_columns=piv,
                nonzero_pivot_minor=d,nonsimple_vertices=sorted(ns),
                overloaded_anchor_facets=overloaded,plane_movable_facets=movable,
                projective_velocity_rank=8,augmented_velocity_rank=9)

def interval_certificate(a):
    t=Box(0,EPS);xx,qq,raw,rq,d,g,lines=arc(a,t)
    faces=a['faces'];guards={}
    def pos(k,v):
        v=Box.cast(v);assert v.l>0,('nonpositive interval',k,v.l)
        guards[k]=(v.l,v.u)
    pos('six_volume',d)
    for f,ids in enumerate(faces):
        for i in range(10):
            if i not in ids:pos('slack:%d:%d'%(f,i),1-dot(rq[f],raw[i]))
        for k,i in enumerate(ids):
            j=ids[(k+1)%len(ids)]
            for l in ids:
                if l not in (i,j):
                    pos('corner:%d:%d:%d'%(f,k,l),dot(rq[f],cross(sub(raw[j],raw[i]),sub(raw[l],raw[i]))))
        for k in range(1,len(ids)-1):
            pos('fan:%d:%d'%(f,k),det([raw[i] for i in (ids[0],ids[k],ids[k+1])]))
        pos('centred_support:%d'%f,1-dot(rq[f],g))
    pos('centroid_denominator',1-dot(a['poles'][0],g))
    rows=primitives(xx,qq,faces)
    for k,v in a['rows'].items():
        if v:pos('old:'+k,(1 if v>0 else -1)*rows[k])
    q=a['poles'][0];p=mul(1/dot(q,q),q);aa=(1,0,0);x=a['vertices']
    for i,j in ((1,2),(2,3),(3,4),(4,5)):
        yi,yj=sub(x[i],p),sub(x[j],p);ri,rj=dot(yi,yi),dot(yj,yj)
        e=sub(yj,yi)
        z=ri*(rj-ri)*(1+t*ri)+dot(aa,e)+t*dot(aa,sub(mul(rj,yj),mul(ri,yi)))
        pos('VE_positive_quotient:%d:%d'%(i,j),z)
    delta=-dot(sub(qq[8],qq[0]),sub(xx[1],xx[0]))
    pos('VF_P01_positive_quotient',1+t)
    pos('VF_Q08_positive_quotient',dot(q,q)*delta/(1+t))
    y6=sub(x[6],p)
    pos('VF_P06_negative_quotient',-dot(aa,y6)*(1+t*dot(y6,y6)))
    assert len(guards)==224
    return guards

def clean(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,Jet):return [str(x.a),str(x.b)]
    if isinstance(x,Box):return [str(x.l),str(x.u)]
    if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [clean(v) for v in x]
    return x

def build():
    a=fixture();rr=relative_rank(a)
    xx,qq,raw,rq,d,g,lines=arc(a,Jet(0,1))
    for f,ids in enumerate(a['faces']):
        assert all(dot(rq[f],raw[i])==1 and dot(qq[f],xx[i])==1 for i in ids)
    _,cg=moment(xx,a['faces']);assert all(v==0 for v in cg)
    jr=primitives(xx,qq,a['faces'])
    keys=('P:1:2','P:2:3','P:3:4','P:4:5','P:0:1','Q:0:8')
    coeff=(F(1,4),F(9,64),F(113,1024),F(4361,16384),F(1),F(15743496,7830870125))
    assert all(jr[k].a==0 and jr[k].b==v>0 for k,v in zip(keys,coeff))
    assert jr['Q:0:2']==0 and jr['P:0:6'].b==-1
    endpoint=audit(arc(a,EPS)[0],a['faces'])
    for key in ('stable','unstable','saddles','counts'):assert endpoint[key]==a[key]
    assert endpoint['physical_weak_count']==0
    assert endpoint['weak_vertices']==endpoint['weak_facets']==endpoint['weak_edges']==[]
    assert endpoint['zeros']==['Q:0:2']
    for k,v in a['rows'].items():
        if v:assert v*endpoint['rows'][k]>0
    q=a['poles'][0];p=mul(1/dot(q,q),q);x=a['vertices']
    assert endpoint['rows']['P:0:1']==EPS*(1+EPS)
    assert endpoint['rows']['P:0:6']==-EPS*(1+EPS*dot(sub(x[6],p),sub(x[6],p)))
    delta=-dot(sub(endpoint['poles'][8],q),sub(endpoint['vertices'][1],endpoint['vertices'][0]))
    assert endpoint['rows']['Q:0:8']==dot(q,q)*delta*EPS/(1+EPS)
    guards=interval_certificate(a)
    return dict(version=1,name='RELATIVE_FACET_RANK_SEVEN_AND_MIXED_HEPTAGON_V1',
                epsilon=EPS,initial=a,endpoint=endpoint,relative_incidence=rr,
                first_exit_keys=keys,first_exit_coefficients=coeff,
                raw_centroid_jet=g,centred_centroid_jet=cg,
                vertex_jets=xx,pole_jets=qq,interval_guard_count=len(guards),
                interval_guards=guards,protected_nonzero_count=60,
                incidence_scope='All t: fixed-height basal/top polygons and three pairs of parallel true edges; final affine map preserves every incidence.',
                uniform_scope='Actual volume-fan moments followed by a plane-fixing affine centroid correction; M=N=I throughout.')

def main():
    assert __debug__ and sys.version_info[:3]==(3,13,5)
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    sys.set_int_max_str_digits(0)
    report=build();text=json.dumps(clean(report),sort_keys=True,indent=2)+'\n'
    path=Path('relative_facet_report.json')
    if sys.argv[1]=='build':path.write_text(text,encoding='utf-8')
    else:assert path.read_text(encoding='utf-8')==text
    print('RELATIVE_FACET_SEVEN_HEPTAGON_ACTUAL_COM_INTERVAL_PASS')
    print('RANK',report['relative_incidence']['rank'],'GUARDS',report['interval_guard_count'],
          'STRICT',*report['initial']['counts'],'WEAK',report['initial']['physical_weak_count'],'TO',report['endpoint']['physical_weak_count'])
    for p in (Path(__file__),path):
        data=p.read_bytes();print(p.name,len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
```
