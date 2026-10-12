# minimum-0221

AI research report · 2026-09-24 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# THREE_LEVEL_NORMAL_RETRACTION_AND_ACTUAL_FIVE_WEAK_CONTROL_V1

## 1. Main result and exact boundary

I obtain a whole-shape-class exclusion of the **singular-disconnected alternative**, not an all-E17 U1 exclusion.

**Normal-level theorem.** Let P be any actual uniform full-dimensional convex three-polytope, centred at its volume centroid. Fix a possible root r. Suppose there is a nonzero covector n such that every NONROOT vertex belongs to one of three planes

    n·X=h_-,  n·X=0,  n·X=h_+,

where h_-<0<h_+ are the actual minimum and maximum of n·X on P. The root may also have a different height. Then every SPD weak-U1 metric at r connects, on that SAME actual body and while preserving any of its selected weak rooted trees, to a rank-two rooted metric. In fact the entire trace-one weak-rooted set W_r has an explicit strong deformation retraction onto its rank-two subset.

Consequently **no singular-disconnected U1 component exists in this class**, including all weak-arrow equalities and arbitrary conditioning. This covers every uniformly filled prismatoid, with arbitrary top and bottom polygons, all roots and all affine images. It also covers genuinely three-level bodies whose middle plane passes through the ACTUAL volume centroid.

The centroid condition is not left as an artificial constraint: section4 constructs a complete three-independent-shape family on the **literal E17 graph of the parent**, using actual disjoint cut volumes to force the two cap vertices into that middle plane. The construction extends to arbitrary convex hexagonal source pyramids. It uses a new uniform translation, not the parent's star-projective centring; its identity is kept separate.

There is also a new true-face contact mechanism. Three specified zero primal arrows on a genuine trapezoid force an EF contact on the remaining edge, or a VF endpoint contact on the equality wall. An exact actual E17 control has FIVE genuine weak-unstable sources, five independent zero-arrow equations and a unique SPD ray, but TWO strict U and an additional genuine EF contact. An exact metric interval removes all six weak points while preserving strict424, not U1 or110.

Thus actual homogeneous centring and the count/rank of five physical weak sources alone do not give a contradiction. Rooted reachability is indispensable. Conversely the normal-level geometry can eliminate the entire disconnected-component branch without enumerating critical rays.

## 2. Sources and what was used

The current journal was read consecutively through EOF, including its full immutable parent, and the complete85-line coordinator material was read. The journal's mounted bytes are267749, SHA256151cab1145d46b83665ceb06460ba9f3be1186bd6d60b9e0d9f65e47df199dcb. There is no missing exact dependency for the new constructions or proofs.

Direct parent:

    minimum-0218
    d2708a7da6c6867a9f47f2960251aa8600f88769bc3d919060ca8719add3a723
    HEX6_FULL_RANK_NORMAL_PORT_AND_FIVE_CONTACT_ALTERNATIVE_V8.

New coordinator premise:

    [internal-source-reference]
    3d9a495f54852bbaab9d638b687296cb0d01373bf1c0d62f30e1a6d5d57e89d3
    FULL_COMPONENT_FIVE_PHYSICAL_WEAK_CONTACTS_V1.

I use its definitions of W_r and genuine weak sources, and its component theorem. In particular its five-contact conclusion requires a vertex of the convex hull of an entire U1 component, and its strict-U1 perturbation requires the original metric already to have a sole strict root. Those hypotheses are not dropped in interpreting the new control.

The retraction's continuity at singular matrices also uses the already supplied complete seven-corner shadow theorem: a full-dimensional polygon with0 interior and −Q/3⊂Q cannot have a sole strict radial maximum with at most seven true corners. Its actual exposed-fibre transfer is retained. No old endpoint certificate, vector-cap certificate, or projective coefficient grid is replayed here.

## 3. Complete normal-level proof

### 3.1. A geometric characterization, not a test on fitted moments

Set h_i=n·X_i and

    beta_ij=h_i(h_j−h_i).

The stated normal-level condition is EQUIVALENT to

    beta_ij≤0 for every true edge i→j with i≠r.       (1)

Indeed, at a nonroot with h_i>0, condition(1) says every neighboring height is at most h_i. The true incident edge directions generate the entire tangent cone. A linear functional locally maximized on all those directions is globally maximized on P, so h_i=h_+. Similarly h_i<0 implies h_i=h_-. At h_i=0 all beta vanish. The converse follows immediately from extremality of h_±.

This characterization uses actual true edges. Its middle plane is n·(Y−g_P)=0 in raw coordinates; an arbitrary affine level or a centroid of a projected polygon is not a substitute.

### 3.2. A path preserving every selected tree

For an SPD trace-one M put

    s=nᵀM⁻¹n>0,
    lambda=1/s=det(M)/(nᵀadj(M)n),
    K=M−lambda nnᵀ.

Cauchy–Schwarz in the M inner product proves K≥0, rankK=2 and kerK=span(M⁻¹n). For0≤t≤1 set

    G_t=M−t lambda nnᵀ,
    H_t(M)=G_t/tr(G_t).                              (2)

The trace is positive even at t=1, since K has rank two. For every nonroot true arrow,

    D_ij(G_t)=D_ij(M)−t lambda beta_ij≥D_ij(M).       (3)

Thus every weak rooted tree feasible at M remains feasible throughout(2). For t<1 the metric is SPD, and its selected weak arrows still strictly increase squared radius along every nonzero edge. They force the same sole strict root r. At t=1 they form a genuine weak rooted tree of the singular matrix K; collapsed edges have not been deleted.

This establishes absence of singular-disconnected components already. This basic descent needs only an interior reference satisfying(1); actual homogeneous centring is used to construct the physical families below and in the singular-continuity argument. Unlike the parent's general normal-port situation, no essential positive-beta port exists here. The rank-one descent identity is inherited; the all-shape height characterization and its complete application are the new geometric step.

The SAME reciprocal metric for t<1 is explicit. With N=M⁻¹,

    G_t⁻¹=N+[t lambda/(1−t)](Nn)(Nn)ᵀ,
    H_t(M)⁻¹=tr(G_t) G_t⁻¹.                         (4)

Feet on planes parallel to the level planes are fixed under this descent. Other stable facets, saddles and weak packets need not be preserved. The singular endpoint has no physical inverse and is not assigned an S/U/H census.

### 3.3. Continuity on all of W_r

No trace-one rank-one matrix belongs to W_r: the positive-maximum and negative-minimum endpoint fibres of its one-dimensional projection are two disjoint closed sets. This is the parent's rank-one argument and uses the actual interior reference.

Let M∈W_r have rank two and kernel spanned by k. Necessarily n·k≠0. Otherwise each of the three level planes projects to a line, and its finitely many vertices contribute at most the two endpoints of a segment. The exceptional root contributes at most one further point. The actual shadow therefore has at most seven true corners. An actual positive tetrahedral fan from a vertex a gives −a/3 as an average of(b+c+d)/3 from its opposite triangles, hence −P/3⊂P and −Q/3⊂Q. The shadow has0 interior, so the accepted shadow theorem gives two closed maximum fibres, contradicting the limiting rooted tree.

For rank-two M, adj(M) is a positive multiple of kkᵀ. Hence

    nᵀadj(M)n>0                                     (5)

on every singular member of W_r; it is also positive on every SPD member. Define lambda by the cofactor quotient in(2) on the ENTIRE W_r. It is continuous, equals0 at rank two, and is positive at rank three. Equations(2)–(3) define a continuous map W_r×[0,1]→W_r. It is the identity at t=0, fixes every rank-two point for every t, and maps all W_r to rank two at t=1. This proves the claimed strong deformation retraction. Each individual K_T is preserved as well.

For a fixed nonempty W_r, compactness and(5) also give a positive minimum of nᵀadj(M)n. No evaluated numerical minimum is claimed.

The conclusion is NOT that every rank-two rooted point has an SPD lift, or that rank-two feasibility suffices for U1. A component containing only singular points is allowed. A complete rank-two exclusion would, however, finish U1 exclusion in this normal-level class: the separate full-rank disconnected alternative is absent.

### 3.4. Exact full normal-height fibres

Fix K≥0 of rank two with n transverse to kerK. Every M_delta=K+delta nnᵀ, delta>0, is SPD. Write d_ij=D_ij(K). For each nonroot i define

    L_i=+infinity, if some neighbor has beta_ij=0 and d_ij≥0;
    L_i=max_{j:beta_ij<0} d_ij/(−beta_ij), otherwise,

with maximum of an empty set equal to−infinity. Then

    M_delta has sole strict U at r
    ⇔ 0<delta≤min_{i≠r} L_i.                        (6)

This is an exact weak-escape criterion, not a strict-row approximation: the finite upper endpoint is retained. It follows by solving each inequality d_ij+delta beta_ij≥0, taking its union over the actual neighbors, and then intersecting over nonroots. SPD norm growth supplies rootedness automatically.

The resulting upper bound, when positive, is finite. Choose an extreme level not containing r and maximize the K-radius over its true vertices. K is injective on that level plane, so every same-level outgoing primitive at this maximizer is strictly negative. Every outgoing edge to another level has beta<0. Its weak escape has a finite upper height bound. Thus the whole positive normal-height ray, including its tail, is accounted for by(6). This does not restrict the remaining tangent metric or kernel orientation by assumption.

An additional source-only filter is worth retaining: if all genuine weak-source vectors lie in one LINEAR plane through the actual centroid, every selected zero row annihilates both M_* and nnᵀ for a normal n to that plane. Their rank is at most four. Such sources cannot be the rank-five set in the component theorem. An affine plane not through the actual centroid does not give this filter.

## 4. A complete actual-centroid family on the parent's literal graph

### 4.1. Arbitrary source hexagonal pyramids

Take ANY strictly convex planar hexagon B_0,…,B_5 in cyclic order and an apex A outside its plane. Let l be the affine height with l(B_i)=0 and l(A)=1. Let V_0 and g_0 be the actual volume and centroid of the source pyramid. Put

    rho_0=Area(B_0 B_5 B_1)/Area(B),
    rho_3=Area(B_3 B_4 B_2)/Area(B).

The two corner triangles have disjoint interiors and leave a positive-area central quadrilateral, so rho_0,rho_3>0 and rho_0+rho_3<1.

Choose INDEPENDENT y,z,v∈(0,1), and define

    kappa=rho_0 yz+rho_3 v,
    s=1/(2+sqrt(4−3kappa)).                          (7)

Then0<kappa<1 and1/4<s<1/3. Use the parent's literal cut map with x=u=s:

    Y0=A; Y1=B1; Y2=B2; Y3=B4; Y4=B5;
    Y5=B0+s(A−B0);
    Y6=B0+y(B5−B0);
    Y7=B0+z(B1−B0);
    Y8=B3+s(A−B3);
    Y9=B3+v(B4−B3).

The facets and true edges are exactly

    F0=(0,4,6,5), F1=(0,5,7,1), F2=(0,1,2),
    F3=(0,2,8), F4=(0,8,9,3), F5=(0,3,4),
    F6=(4,3,9,2,1,7,6), F7=(5,6,7), F8=(9,8,2);

    01,02,03,04,05,08,12,17,28,29,34,39,46,56,57,67,89.

One simple corner is cut at B0; the opposite cut at B3 passes through the retained B2. They occupy disjoint corner subpyramids, so the entire open parameter cube retains the actual10/17/9 lattice. These are true maximal faces, not independently moved integrating triangles. The supplied parent has the same raw construction and literal incidence.

### 4.2. Actual volume and complete centroid formula

The removed tetrahedra are

    (B0,Y5,Y6,Y7), (B3,Y8,Y9,B2),

with ACTUAL volume fractions relative to V0

    w0=s rho_0 yz,  w3=s rho_3 v.

Let

    m0=(B0+Y5+Y6+Y7)/4,
    m3=(B3+Y8+Y9+B2)/4.

Then the whole new uniformly filled body has

    V=V0(1−s kappa),
    g=(g0−w0 m0−w3 m3)/(1−s kappa).                 (8)

These are actual removed volumes and first moments, not capped free weights. Since l(g0)=1/4 and l(m0)=l(m3)=s/4,

    l(g)=(1−kappa s²)/(4(1−kappa s))=s,             (9)

where the final equality is exactly1−4s+3kappa s²=0 from(7).

Consequently, for X_i=Y_i−g and n=grad l,

    (n·X0,…,n·X9)
      =(1−s,−s,−s,−s,−s,0,−s,−s,0,−s).            (10)

Every vertex is on an extreme level or the true central level. The normal-level theorem applies for ALL ten roots and ALL SPD metrics. In particular the two cap sources5 and8, which supplied the problematic normal ports in the parent, have beta_5j=beta_8j=0 for EVERY true outgoing edge. Their essential normal ports disappear because of the actual cut-volume/centroid relation, not because a reference was fitted afterwards.

This is a whole three-cut family, and the base hexagon and apex may vary freely as stated. For a fixed source pyramid the three cut parameters are genuinely labelled shape freedoms: a projective equivalence preserving the four retained base vertices fixes their projective base frame, so it cannot change these three base-edge cut fractions. No unlabelled projective classification is asserted.

### 4.3. Relation to the fixed-six-pole atlas and exact calibration

For a literal specialization retain the parent's source

    p=(1/100000)*((60401,−32565),(80000,−20000),(0,60000),
                  (−80000,80000),(−483861,−325040),(−447814,−355009)),
    A=(0,0,1), q_i=(p_i,1),
    b=(2615613/500000,816129/250000,−3),
    B_i=[q_i;q_(i+1 mod6);b]⁻¹(1,1,1).

Here l(Y)=(1−b·Y)/4 and n=−b/4. Equations(7)–(8) define a NEW family

    HEX6_ACTUAL_MIDDLE_LEVEL_THREE_CUT_FAMILY_V1.

It is NOT the parent's fixed-six-pole star-centred body: I do not apply its c-equations or transport its old centroid. The parent instead uses X_i=A+(Y_i−A)/(1+c·(Y_i−A)) at a specific actual-centroid root. Those different final geometries must not be aliased.

The source includes an exact rational new member with

    s=x=u=17/64, y=z=1/2,
    v=2680376424327059260614486446879690306335764640 /
      4004088109076414984081685955398073699141236697.

Equivalently the last fraction is recovered by

    v=(((4s−1)/(3s²))−rho_0/4)/rho_3.

The code checks0<v<1, both actual volume fans, equation(8), every actual support and the complete same-origin polar. With M=I/3 its strict census is

    S={1,5,6}, U={0,1,2,4,8},
    H={01,04,12,17,28,34}, weak000.

All68 primitives are nonzero. Its normal heights are47/64 at0,0 at5/8 and−17/64 at the seven base vertices. This nonwinning356 control validates the genuine centroid construction; its census is not the proof of the full-family theorem.

## 5. Full prismatoid coverage and a separate rational E17 family

Any prismatoid has all vertices in two parallel supporting planes. Its actual volume centroid is strictly between them, so it satisfies the normal-level theorem without an additional moment condition. Thus EVERY actual uniform prismatoid has no singular-disconnected U1 component, for any vertex count and every root. This says nothing automatic about the existence or liftability of its remaining rank-two rooted systems.

For the independent exact contact control, use the following entire four-cut E17 prismatoid family. Let

    H>0, p>0, q>0, p+q<1,
    0<a<1−q, a<b<min(2a,1−p).

Its vertices are

    Y0=(b,0,0), Y1=(1−p,0,0), Y2=(1−p,p,0),
    Y3=(q,1−q,0), Y4=(0,1−q,0), Y5=(0,a,0),
    Y6=(2a−b,b−a,0),
    Y7=(0,0,H), Y8=(1,0,H), Y9=(0,1,H).

Its nine exact defining inequalities are

    0≤z≤H, x≥0, y≥0, x+y≤1,
    x+y+(a/H)z≥a, x+2y+(b/H)z≥b,
    x−(p/H)z≤1−p, y−(q/H)z≤1−q.

At level z=tH< H these give the same strict seven-edge polygon with cut parameters(1−t)(a,b,p,q). At t=1 it is the true triangle789. Hence the complete parameter domain has the following maximal facets and true edges, with no missing intermediate-height vertices:

    F0=(6,5,4,3,2,1,0), F1=(8,7,0,1), F2=(7,6,0),
    F3=(1,2,8), F4=(9,8,2,3), F5=(9,3,4),
    F6=(4,5,7,9), F7=(6,7,5), F8=(7,8,9);

    01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.

This graph is NOT the parent's six-pole graph. The identity is

    HEPTAGON_TRIANGLE_PRISMATOID_FOUR_CUT_V1.

The all-metric component theorem covers the whole open parameter domain, all unbounded H, and all affine images. Its underlying prismatoid conclusion also survives cut mergers whenever the resulting actual body remains full-dimensional, but those merged boundaries are not reported as10/17/9 members.

### Exact uniform moments for the whole family

Write

    A_A=(a²+(b−a)²)/2, A_B=p²/2, A_C=q²/2, R=A_A+A_B+A_C,
    J_A=(a(3b²−6ab+4a²), b(b²−3ab+3a²))/6,
    J_B=(p²/2−p³/3,p³/6),
    J_C=(q³/6,q²/2−q³/3).

These are the actual bottom-plane areas and first moments of the three missing corner regions. The first region can be nonconvex; it is the polygon(0,0),(b,0),(2a−b,b−a),(0,a) and is integrated by its two positive triangles, not treated as a convex facet.

At height tH, each corner region is homothetically scaled by1−t about its respective triangle corner. Direct integration gives

    V=H(1/2−R/3),
    J_x=H[1/6−(J_Ax+J_Bx+J_Cx)/4−A_B/12],
    J_y=H[1/6−(J_Ay+J_By+J_Cy)/4−A_C/12],
    J_z=H²(1/4−R/12),  g=J/V.                       (11)

Thus the actual centred levels are−g_z and H−g_z. The source independently matches(11) to two symbolic complete apex fans over the entire parameter family.

## 6. A true-trapezoid weak-contact forcing lemma

Let a genuine maximal trapezoidal facet have cyclic vertices

    x0, x1=x0+e, x2=x0+e+f, x3=x0+u e+f, u<0,

with e,f independent. Use ONE SPD M and N=M⁻¹. Suppose

    D01=D12=D32=0, and D30≤0.                       (12)

The last inequality follows when source3 is genuinely weak unstable. Put

    m=eᵀMe>0, k=eᵀMf, n_f=fᵀMf,
    V_f=n_f−u²m.

The three zero equations force

    x0ᵀMe=0, k=−u m, x0ᵀMf=u m,
    V_f>0.

The M-orthogonal foot of the actual origin on this facet plane is exactly

    p=x0+theta(x3−x0),
    theta=−u m/V_f.                                (13)

To verify it, pᵀMe=0 and pᵀMf=u m+theta V_f=0. Since

    D30=−(u m+V_f)≤0,

one has0<theta≤1. If D30<0, the foot belongs to the RELATIVE INTERIOR of the true edge03. For the actual pole q of this facet and the actual neighboring pole r across03,

    qᵀN(r−q)=0,
    rᵀN(q−r)=−|r−q|_N²<0,
    D03=u m<0, D30<0.                              (14)

Thus03 carries a genuine weak EF point. If theta=1, the same foot is x3 and the conclusion is instead a VF endpoint contact; it must not be counted as an additional distinct EF point. This includes the weak boundary rather than deleting it.

In the prismatoid family above, the true facet F4 in the order(2,3,9,8) has

    u=−(p+q)/(1−p−q)<0.

Consequently the exact zero pattern2→3,3→9,8→9, with8 genuinely weak, forces the described contact on28 for the ENTIRE family. When8 has only its chosen zero escape, D82<0 and the forced EF is a sixth distinct physical weak point.

This is not a U1 exclusion: extra EF/VF contacts are allowed at a critical weak-U1 metric. It does explain why counting weak sources is not the same as counting ALL physical weak equilibria.

## 7. Exact five-genuine-source control and a complete weak-removal interval

Set(a,b,p,q,H)=(1/4,3/8,1/4,1/3,1) in the prismatoid family. Its actual moments are

    V=1583/3456,
    g=(25691/75984,49717/151968,3311/6332).

Use X_i=Y_i−g. The five frozen TRUE zero arrows are

    (0,7),(1,0),(2,3),(3,9),(8,9).                   (15)

Their five symmetric arrow rows have rank5. Their unique SPD ray is M=M_R/T, where

    M_R=((5506935648192,7652542645440,−450019288488),
         (7652542645440,13253085616320,413714704920),
         (−450019288488,413714704920,1190407054187)),
    T=19950428318699.

The integer leading minors are

    5506935648192,
    14422480688775417460899840,
    10692581907624194651534124556035686400.

At this SAME SPD ray the complete exact classification is

    genuine weak-U sources={0,1,2,3,8};
    strict U={7,9};
    strict S={0,1,6,8};
    strict H={12,45,78,79}.

Every outgoing true arrow at each of the five listed weak sources is nonpositive, and each has exactly its one zero from(15). No harmless-zero source is counted. All five contacts are simple VE contacts. The only further zero among all68 true-edge primitives is the POLAR arrow F4→F3, producing the sixth physical weak point on28. Its exact edge fraction from X2 to X8 is

    theta=993776784/1153223143∈(0,1).

The six weak packets, in the order(primal i→j,j→i,polar f→h,h→f) with i<j and f<h, have signs

    01:(−,0,−,−), 07:(0,−,−,−), 23:(0,−,−,−),
    28:(−,−,−,0), 39:(0,−,−,−), 89:(0,−,−,−).

The true-face lemma explains the extra EF without a numerical coincidence. There are62 nonzero primitives and6 zeros. This is strict424 with5VE+1EF, NOT a U1 critical point: its full rooted test fails because7 and9 are two strict sinks.

### Actual metric germ, with all reciprocal signs certified

Solve trDelta=0 and D_e(Delta)=1 for the five rows(15). The unique exact solution is

    Delta11=−48633806591766968/30025394619641995,
    Delta12=7235239311808216/4289342088520285,
    Delta13=83126269492593301/30025394619641995,
    Delta22=1968013292350976/857868417704057,
    Delta23=4165808818779010/6005078923928399,
    Delta33=−20246658640517192/30025394619641995.

On the ENTIRE interval

    0<epsilon≤1/1024,
    M_epsilon=M+epsilon Delta, N_epsilon=M_epsilon⁻¹,

the actual body has strict424, weak000. All62 original nonzero primitive signs persist; the five primal zeros become epsilon, and the polar zero F4→F3 becomes strictly positive. Every one of the68 primitives is nonzero for epsilon>0.

This is proved by71 exact univariate guards:3 positive leading minors and68 sign guards, dividing each originally zero primitive numerator by epsilon. The source verifies all173 Bernstein coefficients strictly positive on the CLOSED interval[0,1/1024], and reconstructs every power polynomial by the inverse Bernstein transform. Primal degrees are at most1, reciprocal numerators use the actual adj(M_epsilon) and have degree at most2, principal minors at most3. The least coefficient is

    369287344331896801/737904098172321669120>0.

The zero endpoint is retained as the original six-contact body; weak000 is asserted only for the positive interval. No density, support or centroid changes along this metric germ.

This is a precise limitation of the contact-count strategy: even true uniform E17 geometry with five independent GENUINE weak-U contacts is realizable. The sole-root hypothesis of the coordinator's strictification theorem is the missing condition in this control, not a defect in that theorem. Opening five weak escapes cannot remove the two pre-existing strict roots.

## 8. Remaining domain and interpretation

The whole normal-level class, the full centroid-aligned three-cut hexagon-pyramid family, and all prismatoids have no singular-disconnected U1 component. This conclusion is complete over their specified continuous shape domains; it is not inferred from failed finite searches. It includes all weak arrow walls and all positive metric scales/conditioning.

What remains there is genuine rank-two rooted feasibility, with an actual SPD lift when one is needed. Feasible singular kernels must be transverse to the level planes. The retraction does not by itself exclude those systems, preserve S1/H0, or convert a singular weak system into proper110.

Outside the normal-level class, the fixed-six-pole STAR-CENTRED atlas and general E17 bodies may still have singular-disconnected components. The new translated three-cut family is not a silent all-domain theorem about that different star-centred atlas. Arbitrary positive-projective refills need not preserve the level/centroid condition. The true-trapezoid lemma leaves its VF endpoint and nontrapezoidal facets explicitly outside the strict-extra-EF conclusion.

The useful continuation on the new middle-level family is the actual rank-two shadow problem together with the complete normal-height window(6), not further enumeration of a disconnected component that cannot exist. Beyond the level class, a targeted extension is to keep the actual cut-volume/centroid coupling while allowing one cap height to leave zero; that restores only the explicitly identified normal ports, rather than an unrestricted set of independent moments.

The exact five-source control was located by exploratory finite calculations and then reconstructed from the frozen rational geometry and five rows. No optimizer status or finite candidate failure enters any exclusion. No canonical registry entry or bound is changed; the working interval remains34≤C_min≤622.

## 9. Complete executable recovery and actual execution

The new source reconstructs both exact geometries, their true maximal facets and edges, actual volume centroids, the physical five-source SPD ray from cofactors, all primal/polar primitives, independent direct edge-foot saddle checks, the sixth EF point, the complete173-coefficient interval certificate and the exact translated literal-graph middle-layer control. It also verifies the whole prismatoid moment identities symbolically using two distinct apex fans. It imports no old source or array.

Observed environment: CPython3.13.5, SymPy1.14.0, assertions enabled. Author build/check completed. The final source was copied alone to a fresh directory; build AND check completed there and gave byte-identical report and stdout. This is source-only replay of this implementation, not a proof-assistant formalization or an independently authored verifier.

Save the full source below as level_prismatoid_weak5.py, UTF-8/LF with its final newline, then run

    python -B level_prismatoid_weak5.py build > build.out
    python -B level_prismatoid_weak5.py check > check.out
    cmp build.out check.out

Do not use -S: the verifier imports SymPy. No RNG or floating tolerance is used in this recovery.

Pins:

    level_prismatoid_weak5.py:17212 bytes
    SHA256329faaed5a718314436ceefb72da31b760454a1a91d71baf29d484cd5a254108
    level_prismatoid_weak5.json:110501 bytes
    SHA2568456d7865f62a9dd923d400d208a5f243a6635052265b715261d4133629db0d6
    identical build/check stdout:419 bytes
    SHA25681246e25e5eb46e1cf970b07375245bd68fdc7d013d3f7a0df9a2d6cc9b5dce2

Expected terminal lines include

    ACTUAL_E17_TRUE_VOLUME_COM_FIVE_GENUINE_WEAK_U_RANK_FIVE_TWO_STRICT_U_PASS
    TRUE_TRAPEZOID_THREE_ZERO_ARROWS_FORCE_EXTRA_EF_CONTACT_PASS
    WHOLE_CLOSED_EPSILON_INTERVAL_POSITIVE_EXACT_BERNSTEIN_ALL_68_SIGNS_PASS 71 173
    LITERAL_HEX6_GRAPH_NEW_ACTUAL_MIDDLE_LAYER_CONTROL_OWN_356_WEAK000_PASS
    THREE_LEVEL_NORMAL_RETRACTION_ACTUAL_CONTACT_RECOVERY_PASS 110501 8456d7865f62a9dd923d400d208a5f243a6635052265b715261d4133629db0d6

Supplementary copies: source (`level_prismatoid_weak5.py`), complete bundle (`THREE_LEVEL_WEAK5_bundle.zip`). The entire executable is included below; the handoff does not depend on either link.

### Complete runnable source

```python
#!/usr/bin/env python3
"""THREE_LEVEL_NORMAL_RETRACTION_AND_ACTUAL_FIVE_WEAK_CONTROL_V1.
CPython >=3.11; SymPy 1.14.0; assertions enabled. No external input.
python -B level_prismatoid_weak5.py build|check
The universal geometric proof is in the handoff, not inferred from these controls.
"""
from pathlib import Path
from itertools import combinations
from math import comb, gcd, lcm
from functools import reduce
import hashlib,json,sys
import sympy as S
assert __debug__ and sys.version_info >= (3,11) and S.__version__=='1.14.0'
R=S.Rational
HERE=Path(__file__).resolve().parent
PARENT=('minimum-0218','d2708a7da6c6867a9f47f2960251aa8600f88769bc3d919060ca8719add3a723')
MATERIAL=('[internal-source-reference]','3d9a495f54852bbaab9d638b687296cb0d01373bf1c0d62f30e1a6d5d57e89d3')
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=((0,1),(0,6),(0,7),(1,2),(1,8),(2,3),(2,8),(3,4),(3,9),(4,5),(4,9),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9))
SELECTED=((0,7),(1,0),(2,3),(3,9),(8,9))
PARAMS=(R(1,4),R(3,8),R(1,4),R(1,3),R(1))
MR=S.Matrix(((5506935648192,7652542645440,-450019288488),(7652542645440,13253085616320,413714704920),(-450019288488,413714704920,1190407054187)))
TRACE=19950428318699
EPS=R(1,1024)

def pin(b):return (len(b),hashlib.sha256(b).hexdigest())
def zero():return S.zeros(3,1)
def vsum(vs):return sum(vs,zero())
def family(a,b,p,q,H):
    return list(map(S.Matrix,((b,0,0),(1-p,0,0),(1-p,p,0),(q,1-q,0),(0,1-q,0),(0,a,0),(2*a-b,b-a,0),(0,0,H),(1,0,H),(0,1,H))))
def family_moments(a,b,p,q,H):
    AA=(a*a+(b-a)**2)/2;AB=p*p/2;AC=q*q/2;loss=AA+AB+AC
    JA=S.Matrix((a*(3*b*b-6*a*b+4*a*a)/6,b*(b*b-3*a*b+3*a*a)/6))
    JB=S.Matrix((AB-p**3/3,p**3/6));JC=S.Matrix((q**3/6,AC-q**3/3))
    V=H*(R(1,2)-loss/3)
    J=S.Matrix((H*(R(1,6)-(JA[0]+JB[0]+JC[0])/4-AB/12),H*(R(1,6)-(JA[1]+JB[1]+JC[1])/4-AC/12),H*H*(R(1,4)-loss/12)))
    return V,J,dict(origin_area=AA,origin_first=JA,B_area=AB,B_first=JB,C_area=AC,C_first=JC,total_area_loss=loss)
def fan(Y,apex,exact_positive=False):
    D=S.Integer(0);J=zero();cells=[]
    for fi,cyc in enumerate(FACES):
        if apex in cyc:continue
        for k in range(1,len(cyc)-1):
            ids=(cyc[0],cyc[k],cyc[k+1]);v=[Y[i] for i in ids]
            w=S.det(S.Matrix.hstack(*(z-Y[apex] for z in v)))
            if exact_positive:assert w>0
            D+=w;J+=w*(Y[apex]+vsum(v));cells.append((fi,ids,S.factor(w)))
    return S.factor(D/6),J.applyfunc(lambda z:S.factor(z/24)),cells

def all_hull_faces(Y):
    out=set()
    for ids in combinations(range(len(Y)),3):
        a,b,c=(Y[i] for i in ids);n=(b-a).cross(c-a)
        if n==zero():continue
        d=[n.dot(a-v) for v in Y]
        if all(t>=0 for t in d) or all(t<=0 for t in d):out.add(tuple(i for i,t in enumerate(d) if t==0))
    return out

def body():
    a,b,p,q,H=PARAMS
    assert H>0 and p>0 and q>0 and p+q<1 and 0<a<1-q and a<b<min(2*a,1-p)
    Y=family(*PARAMS);vf,jf,deficits=family_moments(*PARAMS)
    V,J,c0=fan(Y,0,True);V9,J9,c9=fan(Y,9,True)
    assert V==V9==vf==R(1583,3456) and J==J9==jf
    g=J/V;assert g==S.Matrix((R(25691,75984),R(49717,151968),R(3311,6332)))
    X=[v-g for v in Y];Q=[];rawsupports=[];slacks=[]
    for f in FACES:
        n=(Y[f[1]]-Y[f[0]]).cross(Y[f[2]]-Y[f[0]]);h=n.dot(Y[f[0]])
        assert n!=zero()
        ds=[S.factor(h-n.dot(v)) for v in Y]
        assert all(ds[i]==0 if i in f else ds[i]>0 for i in range(10))
        for i in range(len(f)):
            e=Y[f[(i+1)%len(f)]]-Y[f[i]]
            assert all(e.cross(Y[j]-Y[f[i]]).dot(n)>0 for j in f if j not in (f[i],f[(i+1)%len(f)]))
        hnew=h-n.dot(g);assert hnew>0
        Q.append(n/hnew);rawsupports.append((n,h));slacks.append(ds)
    assert all_hull_faces(Y)==set(tuple(sorted(f)) for f in FACES)
    ed=sorted(set(tuple(sorted((f[k],f[(k+1)%len(f)]))) for f in FACES for k in range(len(f))))
    assert tuple(ed)==EDGES and 10-17+9==2
    EF={e:tuple(i for i,f in enumerate(FACES) if set(e)<=set(f)) for e in EDGES}
    assert all(len(v)==2 for v in EF.values())
    dual_expected=set(tuple(i for i,f in enumerate(FACES) if v in f) for v in range(10))
    assert all_hull_faces(Q)==dual_expected
    assert all(Q[f].dot(X[i])==1 if i in FACES[f] else Q[f].dot(X[i])<1 for f in range(9) for i in range(10))
    return Y,X,Q,EF,dict(parameters=PARAMS,vertices=Y,faces=FACES,edges=EDGES,volume=V,first_moment=J,centroid=g,raw_supports=rawsupports,all_support_slacks=slacks,fan0=c0,fan9=c9,actual_deficits=deficits)

def row(x,e):
    return S.Matrix([[x[0]*e[0],x[1]*e[1],x[2]*e[2],x[0]*e[1]+x[1]*e[0],x[0]*e[2]+x[2]*e[0],x[1]*e[2]+x[2]*e[1]]])
def matrix(v):return S.Matrix(((v[0],v[3],v[4]),(v[3],v[1],v[5]),(v[4],v[5],v[2])))
def primitive(v):
    d=lcm(*(int(x.q) for x in v));ns=[int(x*d) for x in v];g=reduce(gcd,ns);ns=[x//g for x in ns]
    if sum(ns[:3])<0:ns=[-x for x in ns]
    return matrix(ns)
def leading(M):return [S.factor(M[:k,:k].det()) for k in (1,2,3)]
def edges_directed():return sorted((i,j) for a,b in EDGES for i,j in ((a,b),(b,a)))

def census(X,Q,EF,M):
    assert min(leading(M))>0
    N=M.inv();dp={(i,j):S.factor((X[i].T*M*(X[j]-X[i]))[0]) for i,j in edges_directed()}
    dq={(i,j):S.factor((Q[i].T*N*(Q[j]-Q[i]))[0]) for f in EF.values() for i,j in (f,f[::-1])}
    U=[i for i in range(10) if all(z<0 for (a,b),z in dp.items() if a==i)]
    W=[i for i in range(10) if all(z<=0 for (a,b),z in dp.items() if a==i) and any(z==0 for (a,b),z in dp.items() if a==i)]
    St=[i for i in range(9) if all(z<0 for (a,b),z in dq.items() if a==i)]
    assert U==[i for i in range(10) if all((X[i].T*M*(X[j]-X[i]))[0]<0 for j in range(10) if j!=i)]
    assert St==[i for i in range(9) if all(Q[j].dot(N*Q[i]/(Q[i].dot(N*Q[i])))<1 for j in range(9) if j!=i)]
    hs=[];weak=[];direct_h=[]
    for e in EDGES:
        i,j=e;f,h=EF[e];z=[dp[i,j],dp[j,i],dq[f,h],dq[h,f]]
        if max(z)<0:hs.append(e)
        ee=X[j]-X[i];tau=S.factor(-(X[i].T*M*ee)[0]/(ee.T*M*ee)[0]);point=X[i]+tau*ee
        Rq=S.Matrix.hstack(Q[f],Q[h]);coeff=(Rq.T*Rq).inv()*Rq.T*M*point
        assert Rq*coeff==M*point
        if 0<tau<1 and min(coeff)>0:direct_h.append(e)
        if max(z)<=0 and 0 in z:
            typ='VE' if tau in (0,1) else 'EF'
            assert 0<=tau<=1 and min(coeff)>=0
            if typ=='VE':assert min(coeff)>0 and sum(t==0 for t in z)==1
            else:assert 0<tau<1 and sum(t==0 for t in coeff)==1
            weak.append(dict(edge=e,type=typ,primitives=z,edge_fraction=tau,point=point,normal_coefficients=coeff))
    assert hs==direct_h
    return dict(M=M,N=N,strict_S=St,strict_U=U,weak_U=W,strict_H=hs,primal=sorted(dp.items()),polar=sorted(dq.items()),physical_weak=weak)

def bernstein_positive(name,p,t):
    p=S.Poly(S.cancel(p),t);d=p.degree();a=[p.nth(k)*EPS**k for k in range(d+1)]
    b=[sum(a[j]*R(comb(k,j),comb(d,j)) for j in range(k+1)) for k in range(d+1)]
    assert min(b)>0,(name,b)
    back=[sum(b[k]*comb(d,k)*comb(d-k,i-k)*(-1)**(i-k) for k in range(i+1)) for i in range(d+1)]
    assert back==a
    return dict(name=name,power=[p.nth(k) for k in range(d+1)],interval=(0,EPS),bernstein=b)

def family_symbolics():
    a,b,p,q,H=S.symbols('a b p q H');Y=family(a,b,p,q,H);V,J,deficits=family_moments(a,b,p,q,H)
    out=[]
    for r in (0,9):
        v,j,cells=fan(Y,r)
        assert S.expand(v-V)==0 and all(S.expand(j[k]-J[k])==0 for k in range(3))
        out.append(dict(apex=r,cells=cells))
    return dict(symbols=(a,b,p,q,H),V=S.factor(V),J=J.applyfunc(S.factor),fan_identities=out,deficits=deficits)

def hex6_middle_layer():
    # Same literal source pyramid and graph as the parent, but NEW uniform
    # translation, NOT the parent's actual star-projective centring.
    global FACES,EDGES
    old=(FACES,EDGES)
    FACES=((0,4,6,5),(0,5,7,1),(0,1,2),(0,2,8),(0,8,9,3),(0,3,4),(4,3,9,2,1,7,6),(5,6,7),(9,8,2))
    EDGES=((0,1),(0,2),(0,3),(0,4),(0,5),(0,8),(1,2),(1,7),(2,8),(2,9),(3,4),(3,9),(4,6),(5,6),(5,7),(6,7),(8,9))
    try:
        nums=((60401,-32565),(80000,-20000),(0,60000),(-80000,80000),(-483861,-325040),(-447814,-355009))
        poles=[S.Matrix((R(x,100000),R(y,100000),1)) for x,y in nums]
        b=S.Matrix((R(2615613,500000),R(816129,250000),-3));A=S.Matrix((0,0,1))
        B=[S.Matrix.vstack(poles[i].T,poles[(i+1)%6].T,b.T).inv()*S.ones(3,1) for i in range(6)]
        def cross2(x,y):return x[0]*y[1]-x[1]*y[0]
        area=sum(cross2(B[i],B[(i+1)%6]) for i in range(6))/2;assert area>0
        r0=abs(cross2(B[5]-B[0],B[1]-B[0]))/(2*area)
        r3=abs(cross2(B[4]-B[3],B[2]-B[3]))/(2*area)
        assert r0>0 and r3>0 and r0+r3<1
        s=R(17,64);y=z=R(1,2);kap=(4*s-1)/(3*s*s);v=(kap-r0*y*z)/r3
        assert R(1,4)<s<R(1,3) and 0<v<1
        assert v==R(2680376424327059260614486446879690306335764640,4004088109076414984081685955398073699141236697)
        assert 1-4*s+3*kap*s*s==0 and kap==r0*y*z+r3*v
        Y=[A,B[1],B[2],B[4],B[5],B[0]+s*(A-B[0]),B[0]+y*(B[5]-B[0]),B[0]+z*(B[1]-B[0]),B[3]+s*(A-B[3]),B[3]+v*(B[4]-B[3])]
        V,J,fc0=fan(Y,0,True);V9,J9,fc9=fan(Y,9,True);assert V==V9 and J==J9
        g=J/V;X=[p-g for p in Y];Q=[];slacks=[]
        for f in FACES:
            nn=(Y[f[1]]-Y[f[0]]).cross(Y[f[2]]-Y[f[0]]);h=nn.dot(Y[f[0]])
            ds=[h-nn.dot(p) for p in Y]
            assert all(ds[i]==0 if i in f else ds[i]>0 for i in range(10))
            assert h-nn.dot(g)>0
            Q.append(nn/(h-nn.dot(g)));slacks.append(ds)
        assert all_hull_faces(Y)==set(tuple(sorted(f)) for f in FACES)
        assert tuple(sorted(set(tuple(sorted((f[k],f[(k+1)%len(f)]))) for f in FACES for k in range(len(f)))))==EDGES
        assert all_hull_faces(Q)==set(tuple(i for i,f in enumerate(FACES) if k in f) for k in range(10))
        original_V=4*area/9;og=zero();dw=0
        for k in range(1,5):
            w=-S.det(S.Matrix.hstack(B[0]-A,B[k]-A,B[k+1]-A));assert w>0
            dw+=w;og+=w*(A+B[0]+B[k]+B[k+1])
        assert dw/6==original_V;og/=4*dw
        m0=(B[0]+Y[5]+Y[6]+Y[7])/4;m3=(B[3]+Y[8]+Y[9]+B[2])/4
        vr0=s*original_V*r0*y*z;vr3=s*original_V*r3*v
        assert V==original_V-vr0-vr3 and g==(original_V*og-vr0*m0-vr3*m3)/V
        n=-b/4;hh=[S.factor(n.dot(xx)) for xx in X]
        assert hh==[1-s,-s,-s,-s,-s,0,-s,-s,0,-s]
        EF={e:tuple(i for i,f in enumerate(FACES) if set(e)<=set(f)) for e in EDGES}
        cs=census(X,Q,EF,S.eye(3)/3)
        assert cs['strict_S']==[1,5,6] and cs['strict_U']==[0,1,2,4,8]
        assert cs['strict_H']==[(0,1),(0,4),(1,2),(1,7),(2,8),(3,4)]
        assert cs['weak_U']==[] and cs['physical_weak']==[] and all(z!=0 for _,z in cs['primal']+cs['polar'])
        assert all(hh[i]*(hh[j]-hh[i])<=0 for i,j in edges_directed())
        print('LITERAL_HEX6_GRAPH_NEW_ACTUAL_MIDDLE_LAYER_CONTROL_OWN_356_WEAK000_PASS')
        return dict(identity='HEX6_ACTUAL_MIDDLE_LEVEL_THREE_CUT_FAMILY_V1_CONTROL',source_pole_numerators=nums,source_pole_denominator=100000,source_base_pole=b,source_base_vertices=B,fractions=(s,y,z,s,v),height_covector=n,heights=hh,corner_area_ratios=(r0,r3),kappa=kap,original_volume=original_V,original_centroid=og,removed_volumes=(vr0,vr3),removed_centroids=(m0,m3),vertices=Y,centred_vertices=X,poles=Q,faces=FACES,edges=EDGES,volume=V,centroid=g,all_support_slacks=slacks,fan0=fc0,fan9=fc9,census=cs,not_parent_star_centred_body=True)
    finally:FACES,EDGES=old

def main():
    assert sys.argv[1:] in (['build'],['check'])
    symbolic=family_symbolics();Y,X,Q,EF,geo=body()
    C=S.Matrix.vstack(*(row(X[i],X[j]-X[i]) for i,j in SELECTED));assert C.rank()==5
    minors=S.Matrix([(-1)**k*C[:,[j for j in range(6) if j!=k]].det() for k in range(6)])
    assert C*minors==S.zeros(5,1) and primitive(minors)==MR and S.trace(MR)==TRACE
    assert leading(MR)==[5506935648192,14422480688775417460899840,10692581907624194651534124556035686400]
    M=MR/TRACE;base=census(X,Q,EF,M)
    assert base['strict_S']==[0,1,6,8] and base['strict_U']==[7,9] and base['weak_U']==[0,1,2,3,8]
    Hexpected=[(1,2),(4,5),(7,8),(7,9)];assert base['strict_H']==Hexpected
    assert [(e,z) for e,z in base['primal'] if z==0]==[(e,S.Integer(0)) for e in SELECTED]
    assert [(e,z) for e,z in base['polar'] if z==0]==[((4,3),S.Integer(0))]
    assert [w['edge'] for w in base['physical_weak']]==[(0,1),(0,7),(2,3),(2,8),(3,9),(8,9)]
    assert [w['type'] for w in base['physical_weak']].count('VE')==5
    print('ACTUAL_E17_TRUE_VOLUME_COM_FIVE_GENUINE_WEAK_U_RANK_FIVE_TWO_STRICT_U_PASS')
    augmented=C.col_join(S.Matrix([[1,1,1,0,0,0]]));dv=augmented.inv()*S.Matrix([1,1,1,1,1,0]);Delta=matrix(dv)
    assert S.trace(Delta)==0 and C*dv==S.ones(5,1)
    t=S.symbols('t');Mt=M+t*Delta;adj=Mt.adjugate();guards=[]
    for k,pv in enumerate(leading(Mt),1):guards.append(bernstein_positive('M_leading_'+str(k),pv,t))
    target_signs=[]
    for (i,j),old in base['primal']:
        poly=S.expand((X[i].T*Mt*(X[j]-X[i]))[0]);sgn=S.sign(old) if old else 1
        if not old:assert (i,j) in SELECTED and poly==t
        guards.append(bernstein_positive('P_%d_%d'%(i,j),sgn*poly/(t if old==0 else 1),t));target_signs.append(('P',i,j,sgn))
    for (i,j),old in base['polar']:
        poly=S.expand((Q[i].T*adj*(Q[j]-Q[i]))[0]);sgn=S.sign(old) if old else 1
        assert S.sign(poly.subs(t,EPS))==sgn
        guards.append(bernstein_positive('Q_%d_%d'%(i,j),sgn*poly/(t if old==0 else 1),t));target_signs.append(('Q',i,j,sgn))
    controls=[]
    for ep in (EPS,EPS/1024):
        data=census(X,Q,EF,M+ep*Delta)
        assert data['strict_S']==base['strict_S'] and data['strict_U']==base['strict_U'] and data['strict_H']==Hexpected
        assert data['weak_U']==[] and data['physical_weak']==[]
        assert all(v!=0 for _,v in data['primal']+data['polar'])
        controls.append(dict(epsilon=ep,census=data))
    # The extra genuine EF contact is forced by the three-zero trapezoid.
    x0,x1,x2,x3=[X[i] for i in (2,3,9,8)];e=x1-x0;f=x2-x1;u=R(-7,5)
    assert x3==x0+u*e+f
    mm=(e.T*M*e)[0];nn=(f.T*M*f)[0];kk=(e.T*M*f)[0];vv=nn-u*u*mm
    assert mm>0 and vv>0 and kk==-u*mm and (x0.T*M*f)[0]==u*mm
    theta=S.factor(-u*mm/vv);assert 0<theta<1
    foot=(M.inv()*Q[4])/(Q[4].dot(M.inv()*Q[4]));assert foot==x0+theta*(x3-x0)
    ef=next(w for w in base['physical_weak'] if w['type']=='EF');assert ef['edge']==(2,8) and ef['point']==foot and ef['edge_fraction']==theta
    print('TRUE_TRAPEZOID_THREE_ZERO_ARROWS_FORCE_EXTRA_EF_CONTACT_PASS')
    # All nonroot rows, for ANY root, improve under this normal descent.
    n=S.Matrix((0,0,1));N=M.inv();lam=S.factor(M.det()/(n.dot(M.adjugate()*n)));K=M-lam*n*n.T
    assert lam>0 and lam<1 and K.rank()==2 and K.det()==0 and K*(N*n)==zero()
    assert all(K.extract(ids,ids).det()>=0 for k in (1,2,3) for ids in combinations(range(3),k))
    beta=[]
    for i,j in edges_directed():
        bta=X[i][2]*(X[j][2]-X[i][2]);assert bta<=0
        assert S.factor((X[i].T*K*(X[j]-X[i]))[0]-(X[i].T*M*(X[j]-X[i]))[0]+lam*bta)==0
        beta.append(((i,j),bta))
    assert sum(b==0 for _,b in beta)==20 and sum(bool(b<0) for _,b in beta)==14
    assert n.dot(K.adjugate()*n)>0
    half=M-lam*n*n.T/2;Nh=half.inv();assert Nh==N+lam*(N*n)*(N*n).T
    for fi in (0,8):assert Nh*Q[fi]/Q[fi].dot(Nh*Q[fi])==N*Q[fi]/Q[fi].dot(N*Q[fi])
    print('WHOLE_CLOSED_EPSILON_INTERVAL_POSITIVE_EXACT_BERNSTEIN_ALL_68_SIGNS_PASS',len(guards),sum(len(z['bernstein']) for z in guards))
    hex_control=hex6_middle_layer()
    report=dict(hex6_middle_layer_control=hex_control,identity='THREE_LEVEL_NORMAL_RETRACTION_AND_ACTUAL_FIVE_WEAK_CONTROL_V1',parent=PARENT,material=MATERIAL,source_pin=pin(Path(__file__).read_bytes()),new_family='HEPTAGON_TRIANGLE_PRISMATOID_FOUR_CUT_V1_NOT_LITERAL_HEX6',symbolic_geometry=symbolic,geometry=geo,centred_vertices=X,poles=Q,edge_facets=sorted(EF.items()),selected=SELECTED,rank5_matrix=C,integer_metric=MR,metric_leading_minors=leading(MR),base_census=base,Delta=Delta,whole_interval_guards=guards,whole_interval_target_signs=target_signs,positive_interval_controls=controls,trapezoid=dict(cycle=(2,3,9,8),u=u,m=mm,n=nn,k=kk,V=vv,foot_fraction=theta,foot=foot),normal_descent=dict(n=n,lambda_normal=lam,K=K,beta=beta,rank2_transverse=n.dot(K.adjugate()*n)),scope='Whole-family absence of singular-disconnected components follows from the analytic normal-level theorem. Controls have TWO strict U and do NOT pass rooted U1. There are five weak-U sources but SIX physical weak points at epsilon0. No finite failed search, all-incidence exclusion, U1 or110 attainer is claimed.')
    def enc(x):
        if isinstance(x,S.MatrixBase):return [[enc(x[i,j]) for j in range(x.cols)] for i in range(x.rows)]
        if isinstance(x,S.Basic):return str(x)
        if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
        if isinstance(x,(list,tuple)):return [enc(v) for v in x]
        return x
    data=(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n').encode();path=HERE/'level_prismatoid_weak5.json'
    if sys.argv[1]=='check' or path.exists():assert path.read_bytes()==data
    else:path.write_bytes(data)
    print('THREE_LEVEL_NORMAL_RETRACTION_ACTUAL_CONTACT_RECOVERY_PASS',*pin(data))
if __name__=='__main__':main()
```
