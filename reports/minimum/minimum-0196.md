# minimum-0196

Historical AI scientific report · saved 2026-09-23 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# DOUBLESTACK_ALL_POSITIVE_INDEPENDENT_HEIGHTS_FULL253_V1

Slot: Sharp Lynx 54. Branch: [internal-source-reference].

## 1. Main result

**The entire independent-height family is FULL253-excluded for every t>0, κ>0 and λ>0, under every common physical SPD metric.** This includes all affine images, arbitrarily conditioned metrics, weak selected arrows and every finite parameter wall.

The new lower height is s=λt. For λ>1 the body has the unchanged parent10/17/9 incidence. For 0<λ<1 it is also10/17/9, but a genuine incidence flip removes the required dual edge2–1. At λ=1 the actual body has9/16/9 and that pair meets only at a vertex, not an edge. These latter cases are excluded from literal FULL253 by incidence, not by using the wrong10-vertex fan across a wall.

For λ>1, write ρ=κ/t and W=t+s. Three complete, overlapping domains finish the proof:

| Domain | Entire parameter range, with s>t>0 | What is excluded |
|---|---|---|
| A | 0<ρ≤7/5, arbitrary t,s | Actual χ<3/4 forbids the three weak pole arrows65,54,43. |
| C | 0<W≤7/100, arbitrary ρ>0 | A new actual support-ratio guard gives a PD stress forbidding65,54,21. |
| B | W≥7/100 andρ≥7/5 | Actual whole-facet T=Λ05+Λ06<51/25 contradicts FULL253 concentration. |

Every positive parameter is included: first separateλ≤1; otherwise either ρ≤7/5, or ρ>7/5 and W lies on one side of7/100. **B needs the literal fullgraph theorem; A/C need only their three indicated arrows.** No tree-containment theorem is inferred from B.

This is a full unbounded three-parameter actual-body theorem, not a collar aroundλ=2. It is **not** an all-orientation110 exclusion, a whole-incidence exclusion, or a canonical-count reduction. The accepted interval34≤C_min≤622 and all registers remain unchanged. :contentReference[oaicite:0]{index=0}

## 2. Exact authority, construction and labels

The immutable continuation parent is `minimum-0193`, SHA-256 `7331bfed675703cd64d0360fad8dd5462f2bc0c8b40034a9717b6f3d67a4bb17`. Its complete payload is present in the current journal. The prior result closesλ=2 but explicitly leaves independent lower-height freedom and all-orientation questions separate. :contentReference[oaicite:1]{index=1}

The literal general `double_stack` constructor supplies the independent lower height; this is not obtained by guessing which occurrences of2t to replace in a vertex array. Fix its r_base=1/2,alpha=gamma=1/10,e=t²,upper height=t,lower height=s. :contentReference[oaicite:2]{index=2}

In original raw plane order0,…,8, the normals and constants are exactly `planes(t,s)` in the recovery source. The positive projectivity is unchanged:

η=20t/(9κ)=20/(9ρ),
Φη(X)=(ηXx,Xy,Xz)/(1+(η−1)Xx).

Every raw vertex has0≤Xx≤1, so all denominators are positive. The image is **uniformly refilled**, then centered at its newly integrated volume centroidg. Neither the old centroid nor an independently refilled polar is used.

FULL_ORDER=(2,4,8,5,3,0,1,7,6), and

TREE=((1,0),(2,1),(3,2),(4,3),(5,4),(6,5),(7,0),(8,7)).

FULL253 means the complete nonnegative ordered pole-pair graph consists of these eight arrows, with the selected arrows on true adjacent facets. Merely containing TREE with extra nonnegative shadows is a different premise. The accepted input FULL253⇒Λ05+Λ06>51/25 comes from `minimum-0069`, SHA-256 `d0f91982420a008eef0bc169a4c7b9f999710361057096a930facbf9715942ff`; its208-block concentration proof is not claimed freshly replayed here. :contentReference[oaicite:3]{index=3}

The prior limitation concerning the journal token“orbit(1,)” is retained: no unprovided canonical-orbit identification is invented. All claims below use the explicit labelled construction.

### Complete incidence chambers

For s>t, all parent vertex labels0,…,9 remain unchanged, with the exact FULL facets

F0=(6,2,3), F1=(8,7,6,3,5), F2=(4,7,8,9,0),
F3=(9,8,5,1), F4=(1,5,3), F5=(1,3,2,0),
F6=(0,9,1), F7=(6,7,4,2), F8=(2,4,0).

For 0<s<t, parent7,8 are no longer vertices. They are **not silently relabelled**. The new vertices are10=raw4∩5∩7 and11=raw5∩7∩8. The other labels0,…,6,9 are retained, and the true facets are

F0=(6,2,3), F1=(10,6,3,5), F2=(4,11,9,0),
F3=(9,11,10,5,1), F4=(1,5,3), F5=(1,3,2,0),
F6=(0,9,1), F7=(6,10,11,4,2), F8=(2,4,0).

At s=t the coalesced vertex has the new label12=raw4∩5∩7∩8. The facets are

F0=(6,2,3), F1=(12,6,3,5), F2=(4,12,9,0),
F3=(9,12,5,1), F4=(1,5,3), F5=(1,3,2,0),
F6=(0,9,1), F7=(6,12,4,2), F8=(2,4,0).

The recovery source proves all three chambers over their entire parameter domains. Each open chamber has56 strictly positive nonincident slacks,34 strict turns,66 within-facet edge/other-vertex inequalities and10 nonzero vertex-rank tests. The wall has49,32,52 and9 respectively. These are polynomial positivity checks after(t,s)=(a,a+d),(a+d,a),(a,a), with a,d>0. The resulting convex supporting-face complexes are closed, every edge has exactly two facets, and Euler’s identity holds. Their interiors are nonempty and the halfspace intersections are bounded byx,y≥0,x+y≤1 and the two opposing roof supports. Positive projectivity preserves these incidences.

The fixed points0=(0,0,0),1=(0,0,1),2=(0,1,−1/2),3=(0,1,0) and all plane-triple reconstruction recipes are literal in the source. Each retained exact control additionally undergoes exhaustive reconstruction from all84 plane triples.

## 3. The height wall has a short exact geometric explanation

Use raw plane indicesI=(4,5,7,8), normalsn_i and constantsb_i. Define

c_{I_j}=(−1)^j det(n_{I_k}:k≠j), j=0,1,2,3.

For all t,s>0, the signs are exactly(−,+,+,−), and

Σ_{i∈I}c_i n_i=0,
Σ_{i∈I}c_i b_i=t⁴(s−t)(40s+40t+13)/4.       (1)

The source expands these four determinants and verifies their signs by strictly positive power coefficients. On a possible common point of raw4 and raw8, the weighted sum of the two remaining nonnegative slacks equals the right side of(1). It cannot be negative. Thus for s<t, **F1 and F2 have no common point**. At s=t, both remaining slacks must vanish; rank3 makes their intersection exactly vertex12. Neither case permits true dual edge2–1.

Above the wall the true primal edge7–8 is incident to F1,F2. Below it the new primal edge10–11 is incident to F3,F7. At the wall both shrink to12. This is an actual supporting-plane transition, not a determinant sign of an unused tetrahedron or a metric event.

This also excludes the interpretation using the full all-pair sign graph without explicitly naming adjacency: if q2 has a nonnegative primitive towards any other pole, some genuine edge direction at q2 must have a nonnegative primitive, since its tangent cone is generated by genuine edge directions. FULL253 permits only q2→q1 as such an exit. A non-neighbor q1 cannot be its sole nonnegative exit.

## 4. The actual common moments and the quad domain

LetD=6Vol(P), h0=1−gx−gy. Integration is always over the actual projectively refilled body. For the unchanged whole quadrilateralF5 and whole triangleF6,

x9=20/[20+9ρt²(2+t+s)],
Λ05=5gx/(2Dh0),
Λ06=x9 gy(3−x9)/(Dh0).                    (2)

Indeed F5 remains the fixedx=0 quadrilateral, with area3/4 and∫F5(1−y)dA=5/12. F6 remains they=0 triangle(0,9,1), with∫F6(1−x)dA=x9(3−x9)/6. These formulas use their actual centroid supportsgx,gy and the sameD,h0. They are not a marked-triangle functional applied to a larger facet.

For s>t, the nine positive tetrahedra of the actual boundary fan from0 give

D=Σ_T det(Z_i,Z_j,Z_k),
J=Σ_T det(Z_i,Z_j,Z_k)(Z_i+Z_j+Z_k),
g=J/(4D).                                (3)

Zero-volume cells contribute nothing. The source reconstructs these rational expressions from the planes; there are no independently chosen masses.

At unchanged true vertex1, the cyclic polar quadrilateral is(q6,q5,q4,q3). PutHt=20t/9+t²+t³. In FULL raw-plane labels,

n3+[9κHt/(20t)]n5=n4+Ht n6.

This relation depends only on the unchanged upper construction, although its centered supports depend on both heights. Sety=q6,x=q5,z=q4 andq3=A z−Bq x+Cq y, withA,Bq,Cq>0,A+Cq=1+Bq. Then

χ=Bq/Cq=9ρgx/(20gy).

The exact quad stress identity is

−D43/Cq−D65−(1−χ)D54
=||y−(x+z)/2||²_N+(3/4−χ)||z−x||²_N.      (4)

Thusχ≤3/4 forbids the three weak arrows. At equality the nonzero rank-one PSD stress is still strictly positive against SPD N. Our new actual-centroid certificateA proves

5gy−3ρgx>0 for all s>t>0, 0<ρ≤7/5,        (5)

soχ<3/4 throughout domainA. No fullgraph or stable-root hypothesis is used in(4)–(5).

## 5. A reusable actual support theorem explains the new guard

The following lemma is broader than the double-stack family. It does not require nine facets or this incidence.

### Actual support-ratio/apex-fan lemma

Let a bounded, full-dimensional uniformly filled convex3-polytope have vertexO=(0,0,0), lie inx,y≥0, and have the five indicated true facet supports

x=0, y=0,
z_x x+y+z≤1,
a_x x−L y−z≤0,
b_x x+B y+z≤B,

where1/2≤L<1,B>1,a_x≥0. Suppose everywhere in the body

y≤1, y+z≤1+δ, 0≤δ<1/3.

At its **actual volume centroid**g define

ell=1−L, d=B−1,
h_a=−a_xgx+Lgy+gz,
h_b=B−b_xgx−Bgy−gz,
h_z=1−z_xgx−gy−gz,
H=ell h_b−d h_a,
G_K=(K−1)ell h_b−(ell+Kd)h_a.

Denote the poles in this displayed support order by x,y,z,a,b. If K>1, G_K≥0 and

(K−1)²/(4K)≤4(1−3δ)/3,                   (6)

then no common SPD metric realizes the three weak pole arrows y→x,x→z,a→b. Equality inG_K and in(6) is included.

**Proof.** Positive actual coning from vertexO gives

gy≤3/4,
gy+gz≤3(1+δ)/4,
E=1−gy−gz≥(1−3δ)/4.

This is the true tetrahedral-volume average: each tetrahedron hasO plus three other vertices. It is not a statement for an arbitrary interior reference.

In the independent basis (x,y,z), specializing to (q5,q6,q4), write a=−αx−βy−cz and b−a=μx+νy+ωz. Direct elimination at the sameg gives

β=gy ell/h_a, c=h_z/h_a,
ν=gy H/(h_a h_b), ω=h_z(h_a+h_b)/(h_a h_b).

Since G_K=K H−ell(h_a+h_b)≥0, H>0 and these four coefficients are positive. Set

s1=α/β, t1=c/β, s2=μ/ν, t2=ω/ν,
U=s1+t1, V=s2+t2.

No positivity ofα orμ is assumed. The exact support identities give

U=(E+a_xgx)/(gy ell)≥2(1−3δ)/3,
V−U=h_a(H+Ld)/(gy ell H)>0,
t2/t1=ell(h_a+h_b)/H.

Becauseell(h_a+h_b)−H=(B−L)h_a>0,

1<t2/t1≤K,
R=(t1−t2)²/(4t1t2)≤(K−1)²/(4K)<U+V.

For P=t1t2,e=z−x,C=t1+t2,v0=y+s1x+t1z,v1=y+s2x+t2z, the exact SOS is

v0ᵀNv1−(U+V)D_yx−(Ut2+Vt1)D_xz
=P||e+C y/(2P)||²_N+UV||x||²_N+(U+V−R)||y||²_N.

Its quadratic matrix is positive definite because x,y,z are independent. Since a=−βv0 and b−a=νv1, it equals

Q=−A_ab/(βν)−(U+V)A_yx−(Ut2+Vt1)A_xz ≻0,

whereA_uv=sym(u(v−u)ᵀ). Three nonnegative arrows would give tr(NQ)≤0, impossible forN,Q≻0. This proves the lemma, including both equalities.

### Structural meaning of the support guard

The dimensionless actual support quantity

θ=(B−L)h_a/[ell(h_a+h_b)]

satisfies t2/t1=1/(1−θ). ThusG_K≥0 is exactlyθ≤1−1/K. For fixed supporting planesG_K is an **affine halfspace condition on the real centroid**. It limits the relative contribution of two genuine support heights; it is not an assertion that the old six signed coefficients are all positive.

The originalC1 wasK=4. Independent lower height makes that guard false on real bodies. The correct successful replacement here isK=6, coupled to a smaller total-height region. The lemma also shows the tradeoff between allowed support ratio and actual vertex-height boundδ, rather than treating4 or6 as a universal magic constant.

### Specialization to the entire domainC

For the independent-height double-stack,

L=1/2+20s/9+t²(1+s), B=1+10t+9t²/2,
a_x=(9ρt²/20)(1+s), b_x=B+9ρt²/20,
z_x=1−κ.

All these are the genuine transformed raw supports of unchangedF2,F1,F4. For s>t andt+s≤7/100, one hast≤7/200,L<1 anda_x>0. Every actual vertex satisfies

y≤1, y+z≤1+20t/11≤117/110.

The source proves the second inequality symbolically over all s>t>0,ρ>0, not merely on the small-height strip. Takeδ=7/110. Actual coning gives

E≥89/440, U≥89/165, V>U.

CertificateC proves the full-strip guard

G6=5ell h_b−(ell+6d)h_a>0.                (7)

Consequently1<t2/t1<6 and

J_signed=R−U−V<25/24−178/165=−49/1320.    (8)

The displayed lemma therefore gives an explicit PD stress for65,54,21 throughoutC. This is uniform over **every** positive projective ratioρ, including its unbounded tail. The scalar margin(8) is in the stated coefficient normalization, not an ambient-coordinate eigenvalue bound across geometric degenerations.

## 6. Complete exact polynomial coverage, including all tails

The source uses(3) to form the three actual rational functions

fA=5gy−3ρgx,
fB=51/25−T,
fC=5ell h_b−(ell+6d)h_a.

It reduces each rational expression and proves its denominator positive by nonnegative power coefficients with a positive term in t,s,ρ. LetpA,pB,pC be the resulting numerators. The following are complete global coefficient certificates, not adaptive samples or feasibility-pruned boxes.

**A.** Substitute s=t+v andρ=7u/5, with t,v>0 and u∈[0,1]. The polynomial has degrees(29,9,9) in(t,v,u). In powers oft,v and degree9 Bernstein basis inu, its3000 coefficient slots contain2084 positive entries and916 zeros. Every coefficient of the t⁰v² row is at least731161600000000000000>0. Thus pA>0 for every physical point, includingu=1 and arbitrarily large t,v.

**B.** Setx=2t/(t+s)∈(0,1), W=t+s, so t=Wx/2,s=W(1−x/2). Then substitute W=7/100+v,ρ=7/5+u, withu,v≥0. The degrees in(v,x,u) are(42,34,12). In powers of v,u and degree34 Bernstein basis inx, the19565 slots contain12278 positive entries and7287 zeros. All35 coefficients of the constant-power rowv⁰u⁰ are strictly positive. Therefore pB>0 even on both finite walls, for every unbounded v,u. This proves the actual whole-facetT<51/25 onB and supplies the only fullgraph-dependent part of the cover.

**C.** Use the samex and substitute W=7u/100, withu,x∈[0,1],ρ>0. The degrees in(u,x,ρ) are(26,22,7). In Bernstein bases foru,x and powers ofρ, the4968 slots contain3534 positive entries and1434 zeros. The coefficient at(26,22,0) is exactly

102413732580182204830224400455732166919/400000000000000000000000>0.

Its basis term is u²⁶x²², strictly positive at every physical point ofC. HencepC>0 for every finiteρ>0, however small or large. The nonphysical edgesu=0 orx=0 are used only to certify polynomial signs; they are not asserted to be E17 realizations.

Total: **27533 coefficient slots,17896 positive and9637 zero**, excluding separate lattice and denominator checks. The source stores every coefficient and original numerator/denominator, and independently expands every Bernstein basis back to the transformed power polynomial by the binomial theorem. The specified positive rows/term resolve all zero-slot boundary issues. No missing coefficient table or old sandbox input is needed. Singular semidefinite metrics are not substituted for the physical SPD condition.

The maps cover the full unbounded region s>t>0,ρ>0. In particular, simultaneous limitsλ→∞,t→0 andκ→∞ are not replaced by one fixed normal-fan limit. The earlier two different macroscopic limits remain distinct; this proof does not interchange them.

## 7. Exact actual controls and failed stronger implications

Seven controls are reconstructed from their literal rational input parameters. All use their actual uniformly refilled centroid and one inverse pairM,N. The source checks their entire true lattice, volume/centroid from two distinct apex fans, whole9×9Λ identities, and all68 edge primitives for10/17/9 or64 for the9/16/9 wall. Every primitive is nonzero; all controls have physicalweak000 and none is110.

| Control | (t,κ,λ) | Metric | Actual(S,U,H) | What it preserves |
|---|---|---|---|---|
| PARENT_CALIBRATION | (1/1000,2,2) | N=M=I | (4,4,6) | Exactly the previous SIGNED_INITIAL_ESCAPE geometry, g, Λ and metric, not a renamed new construction. |
| SIX_RATIO_BOUNDARY | (1/30,1/30,11/10) | N=M=I | (4,4,6) | W=7/100, high actualT>51/25, old G4<0 but new G6>0. |
| OLD_C1_HEIGHT_FAILURE | (1/50,1/25,4) | N=M=I | (6,4,8) | OldC1 fails even at its old t=1/50 cutoff onceλ is independent. |
| OLD_QUAD_SECTOR_FAILURE | (1/5,2/5,10) | N=M=I | (3,5,6) | χ>3/4 despiteκ=2t: the old quad-domain inequality does not extend unchanged. |
| THREE_ARROW_HEIGHT_CONTROL | (1/5,1/10000,3) | ParentG in actual pole basis | (2,4,4) | High actualT and strictly feasible65,54,21 remain possible at a new independent height. |
| LOWER_INCIDENCE | (1/10,1/10,1/2) | N=NGEN,M=N⁻¹ | (4,3,5) | Genuine lower chamber, new vertices10,11 and no2–1 adjacency. |
| INCIDENCE_WALL | (1/10,1/10,1) | N=NGEN,M=N⁻¹ | (4,3,5) | Real9/16/9 coalescence at new vertex12; not an E17 body. |

The exact metric data are

G=((100,90,104),(90,86,96),(104,96,115)),
NGEN=((10,1,2),(1,11,3),(2,3,13)).

For the G control, with B_pole=[q5 q6 q4], use N=B_pole⁻ᵀG B_pole⁻¹ and M=N⁻¹. Its stable facets are{4,8}, unstable vertices{0,2,3,8}, and saddles{0–2,0–9,2–3,3–5}. It has T≈2.066518083542823,D65=D54=4,D21>0. Its tree-arrow signs remain(+,+,−,−,+,+,−,−). Thus the designated three-arrow bridge is still false; the new whole-family conclusion does not declare those three arrows universally infeasible.

### A concrete failure of the old support bound, with genuine aggregation

For SIX_RATIO_BOUNDARY,

Vol=15205745814761294020314172/59059227022610182870632669,
g=(989857565366327385354252708508502507327839564955/3887617290571826441193019492039238687875202540628,
249000771699777992461941556758611349767472269/747592570124997217809223705682172398983029054,
19061025264061133201118703581189184966904953308523/155504691622873057647720779681569547515008101625120).

HereT≈2.044690835964648,χ≈0.3440059853543743, and

G4=−1313022210204257116814780744043061280614687/56737167432634903705185344931964468800000000<0,
G6=20575661641250331669060409567905588658175839/170211502297904711115556034795893406400000000>0.

The normalized ratio is t2/t1≈4.3213632708410525: the old 4 bound genuinely fails, rather than only its proof method.

Moreover, the affineG6 functional has mean−9281808643/37200000000 on the **actual positive-volume tetrahedron(0,1,5,3)**. The total actual volume average is nevertheless the positiveG6 above. Therefore a proposed term-by-term nonnegative fan proof is false. The successful inequality uses the coupled actual determinant weights of the entire body, not arbitrary fan weights or a free first-moment completion.

The separate OLD_QUAD_SECTOR_FAILURE hasχ≈0.8022223880472418 andT≈1.2146760386812139; it is excluded by the new trace domainB, not by the old χ test. OLD_C1_HEIGHT_FAILURE hasG4<0 andt2/t1≈4.300923277337392. Neither result contradicts the immutableλ=2 parent: both change its independent shape data. No failed inequality test is upgraded into feasibility of FULL253 or110.

## 8. Why the added freedom is genuine, and what remains open

The four fixed labelled vertices0,1,2,3 form a projective frame in the planeF5:x=0. Any labelled projective equivalence must fix that plane pointwise. The traces on it of the true supportsF1 andF2 are respectively

B(t)y+z=B(t),
L(t,s)y+z=0.

These trace lines need not be mechanical edges; no such incidence is assumed. SinceB(t)=1+10t+9t²/2 is strictly increasing, the first line fixes t. With t fixed,L(t,s)=1/2+20s/9+t²(1+s) is strictly increasing in s, so the second fixes s. Thus varying the lower height is not absorbed by a labelled projectivity or affine metric change. The result covers two independent labelled projective-shape invariants and the entire positive projective/refill pencil.

The strongest reusable mechanism is the actual support-ratio/apex-fan lemma, together with the exact incidence-wall circuit. The full-family coverage additionally needs the actual moment coupling in its three global polynomial certificates. No shape-independent universalG6 inequality is asserted.

The broader problems remain: other realizations of either incidence chamber; all-orientation110 on these bodies; other FULL253 incidences; and the globalE17 layer. The separate implication from strict F0 stability plus65,54,21 is not settled here; the earlier λ=2 own244/323 controls retain their original meanings. :contentReference[oaicite:4]{index=4} The natural next actual construction parameter is **independent e>0 instead ofe=t²**, with the same two heights and genuine refill. That changes the remaining roof-bevel shape relation; it requires a fresh incidence and actual-centroid analysis. Repeating searches over the now-covered positive(t,κ,λ) family is not the outstanding FULL253 question.

## 9. Recovery and observed verification

The following source is autonomous. It contains all raw planes, exact vertex reconstruction, both incidence chambers and the wall, all global coefficient transformations and inverse checks, the analytic support/SOS identities, and the seven actual controls. It needs no previous report, serialized cache, library, network or numerical optimizer. Dependencies: CPython3.13.5 and SymPy1.14.0; assertions enabled. All proof arithmetic is rational/integer; floating values occur only in diagnostic printing.

Save the full block as `height_full253.py`, UTF-8, LF, final newline.

Commands:

python -B height_full253.py build
python -B height_full253.py check

An optional `python -B height_full253.py controls` reconstructs only the seven exact controls; it is not a substitute for the global proof commands.

Expected terminal marker:

ALL_POSITIVE_T_KAPPA_LAMBDA_FULL253_27533_COEFFICIENTS_PASS

Final source:18622 bytes, SHA-256 `aa42e8719389ecc068bfbd9456af45357a2165f073aeb6788323376f53e64a2f`.
Generated full report:6087741 bytes, SHA-256 `7142b6ba576668831830cd09c927c9dfcbbb67cdbe56d15b4ef5f8f26edba14b`.

The normal build and check completed. A fresh directory initially contained only the final source; its build and check also completed with exit0, the terminal marker, and matching source/report pins. The exact control computations and lattice/identity checks were additionally run separately. This is observed author-side exact execution, not a coordinator replay or proof-assistant formalization.

Convenience copies: [complete source](sandbox:/mnt/data/lynx54_v3/height_full253.py), [full exact report](sandbox:/mnt/data/lynx54_v3/height_full253_report.json), [observed replay receipts](sandbox:/mnt/data/lynx54_v3/replay_receipts.json). The literal source below is the durable recovery capsule.

```python
"""DOUBLESTACK_ALL_INDEPENDENT_HEIGHTS_FULL253_V1.
Parent minimum-0193,
SHA256 7331bfed675703cd64d0360fad8dd5462f2bc0c8b40034a9717b6f3d67a4bb17.
CPython 3.13.5 / SymPy 1.14.0; exact arithmetic, no input files or solver.
Public parameters t>0, kappa>0, lambda>0; internally s=lambda*t,r=kappa/t.
python -B height_full253.py build ; python -B height_full253.py check
"""
from fractions import Fraction as F
from itertools import combinations,product
from collections import defaultdict
from math import comb
from pathlib import Path
import hashlib,json,sys
import sympy as S

ORDER=(2,4,8,5,3,0,1,7,6)
TREE=((1,0),(2,1),(3,2),(4,3),(5,4),(6,5),(7,0),(8,7))
PLUS=((6,2,3),(8,7,6,3,5),(4,7,8,9,0),(9,8,5,1),(1,5,3),
      (1,3,2,0),(0,9,1),(6,7,4,2),(2,4,0))
MINUS=((6,2,3),(10,6,3,5),(4,11,9,0),(9,11,10,5,1),(1,5,3),
       (1,3,2,0),(0,9,1),(6,10,11,4,2),(2,4,0))
WALL=((6,2,3),(12,6,3,5),(4,12,9,0),(9,12,5,1),(1,5,3),
      (1,3,2,0),(0,9,1),(6,12,4,2),(2,4,0))
INC=((0,1,6),(0,1,3),(0,2,6),(0,2,3),(6,7,8),
     (3,4,5),(2,4,7),(4,7,8),(4,5,8),(1,5,8))
G=((100,90,104),(90,86,96),(104,96,115))
NGEN=((10,1,2),(1,11,3),(2,3,13))

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(c,a):return tuple(c*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def solve(rows,b):
 a,c,d=rows;de=det(a,c,d)
 if not de:return None
 return mul(F(1)/de,add(add(mul(b[0],cross(c,d)),mul(b[1],cross(d,a))),mul(b[2],cross(a,c))))
def coords(columns,b):return solve(tuple(zip(*columns)),b)
def form(A,x,y):return sum(x[i]*A[i][j]*y[j] for i in range(3) for j in range(3))
def outer(a,b):return [[(a[i]*b[j]+a[j]*b[i])/2 for j in range(3)] for i in range(3)]
def arrow(a,b):return outer(a,sub(b,a))
def matsum(*terms):return [[sum(c*A[i][j] for c,A in terms) for j in range(3)] for i in range(3)]
def minors(A):return [A[0][0],A[0][0]*A[1][1]-A[0][1]**2,det(*A)]

def planes(t,s):
 N=[(-1,0,0),(0,-1,0),(1,1,0),(1-F(20,9)*t,1,1),
 (1+10*t+F(11,2)*t*t,1+10*t+F(9,2)*t*t,1),
 (1+t*t+t**3,1-F(20,9)*t-t*t-t**3,1),(-F(20,9)*s,-F(1,2),-1),
 (10*s+F(11,2)*t*t,10*s-F(1,2)+F(9,2)*t*t,-1),
 (t*t*(1+s),-F(1,2)-F(20,9)*s-t*t*(1+s),-1)]
 B=[0,0,1,1,1+10*t+F(9,2)*t*t,1,0,10*s+F(9,2)*t*t,0]
 return N,B

def chart(t,s,kind):
 N,B=planes(t,s);ii=dict(enumerate(INC))
 if kind=='minus':
  del ii[7];del ii[8];ii.update({10:(4,5,7),11:(5,7,8)})
 elif kind=='wall':
  del ii[7];del ii[8];ii[12]=(4,5,7)
 else:assert kind=='plus'
 X={i:solve([N[j] for j in ix],[B[j] for j in ix]) for i,ix in ii.items()}
 return X,N,B,dict(plus=PLUS,minus=MINUS,wall=WALL)[kind]

def image(t,s,r,kind):
 X,N,B,faces=chart(t,s,kind);Z={}
 for i,(x,y,z) in X.items():
  den=x+F(9,20)*r*(1-x)
  Z[i]=(x/den,F(9,20)*r*y/den,F(9,20)*r*z/den)
 NN=[(b+F(9,20)*r*(n[0]-b),n[1],n[2]) for n,b in zip(N,B)]
 NN[0]=(-1,0,0)
 return Z,NN,B,faces

def triangles(faces):
 return [(i,(f[0],f[j],f[j+1])) for i,f in enumerate(faces) for j in range(1,len(f)-1)]
def fan(Z,faces,apex):
 ds=[];J=(F(0),)*3
 for fi,ids in triangles(faces):
  a,b,c=[Z[i] for i in ids];w=det(sub(a,apex),sub(b,apex),sub(c,apex))
  ds.append(w);J=add(J,mul(w,add(add(apex,a),add(b,c))))
 return sum(ds),J,ds

def rational_polys(expr,*variables):
 n,d=S.fraction(S.cancel(expr));p,q=S.Poly(n,*variables),S.Poly(d,*variables)
 if q.LC()<0:p,q=-p,-q
 return p,q

def positive_poly(p):
 assert not p.is_zero and all(c>=0 for c in p.coeffs())
def positive_rational(expr,*variables):
 p,q=rational_polys(expr,*variables);positive_poly(p);positive_poly(q)
 return [p.degree_list(),q.degree_list(),len(p.terms()),len(q.terms())]

def lattice_proof():
 a,d=S.symbols('a d',positive=True);out={}
 for kind,t,s in [('plus',a,a+d),('minus',a+d,a),('wall',a,a)]:
  X,N,B,faces=chart(t,s,kind);X={i:tuple(S.factor(v) for v in x) for i,x in X.items()}
  slacks=[];turns=[];edgeguards=[];ranks=[];edges={};inc={}
  for i,x in X.items():
   inc[i]=[j for j,f in enumerate(faces) if i in f]
   for j,(n,b) in enumerate(zip(N,B)):
    q=S.factor(b-dot(n,x))
    if ORDER.index(j) in inc[i]:assert q==0
    else:slacks.append(positive_rational(q,a,d))
   ix=next(ix for ix in combinations([ORDER[j] for j in inc[i]],3)
           if S.factor(det(*[N[h] for h in ix]))!=0)
   q=S.factor(det(*[N[h] for h in ix]))
   if q.subs({a:1,d:1})<0:q=-q
   ranks.append(positive_rational(q,a,d))
  for fi,f in enumerate(faces):
   n=N[ORDER[fi]];m=next(i for i in range(3) if n[i] in (-1,1))
   for i in range(len(f)):
    u,v,w=[X[f[(i+h)%len(f)]] for h in range(3)]
    turns.append(positive_rational(cross(sub(v,u),sub(w,v))[m]*n[m],a,d))
    edges.setdefault(tuple(sorted((f[i],f[(i+1)%len(f)]))),[]).append(fi)
    for j in f:
     if j not in (f[i],f[(i+1)%len(f)]):
      edgeguards.append(positive_rational(cross(sub(v,u),sub(X[j],u))[m]*n[m],a,d))
  assert all(len(fs)==2 for fs in edges.values()) and len(X)-len(edges)+9==2
  assert sorted(set(tuple(sorted(fs)) for fs in edges.values()))==sorted(tuple(sorted(fs)) for fs in edges.values())
  assert (any(set(fs)=={1,2} for fs in edges.values()))==(kind=='plus')
  assert [len(X),len(edges),len(slacks),len(turns),len(edgeguards),len(ranks)]==(
   [9,16,49,32,52,9] if kind=='wall' else [10,17,56,34,66,10])
  out[kind]=dict(incidence=inc,slacks=slacks,turns=turns,edgeguards=edgeguards,ranks=ranks)
 # Exact four-plane circuit: signs negative,positive,positive,negative.
 t,s=S.symbols('t s',positive=True);N,B=planes(t,s);ix=(4,5,7,8)
 c=[S.factor((-1)**j*det(*[N[ix[k]] for k in range(4) if k!=j])) for j in range(4)]
 for cc,sg in zip(c,(-1,1,1,-1)):positive_rational(sg*cc,t,s)
 assert all(S.expand(sum(c[j]*N[ix[j]][h] for j in range(4)))==0 for h in range(3))
 cb=S.factor(sum(c[j]*B[ix[j]] for j in range(4)))
 assert S.expand(cb-t**4*(s-t)*(40*s+40*t+13)/4)==0
 out['circuit']=dict(raw_planes=ix,coefficients=[str(x) for x in c],constant=str(cb))
 return out

def fcoeff(p):return {ix:F(c) for ix,c in p.terms()}
def removezero(a):return {ix:c for ix,c in a.items() if c}
def shift(a,axis,lo,sc=F(1)):
 out=defaultdict(F)
 for ix,c in a.items():
  d=ix[axis]
  for h in range(d+1):
   ex=list(ix);ex[axis]=h;out[tuple(ex)]+=c*comb(d,h)*lo**(d-h)*sc**h
 return removezero(out)

def total_height(a):
 # Substitute t=w*x/2, s=w*(1-x/2), giving coordinates (w,x,r).
 out=defaultdict(F)
 for (i,j,k),c in a.items():
  for b in range(j+1):out[(i+j,i+b,k)]+=c*comb(j,b)*(-1)**b*F(1,2)**(i+b)
 return removezero(out)

def bernstein(a,axes,expected):
 degrees=tuple(max(ix[d] for ix in a) for d in range(3));co=a
 for axis in axes:
  n=degrees[axis];out=defaultdict(F)
  for ix,c in co.items():
   b=ix[axis]
   for k in range(b,n+1):
    ex=list(ix);ex[axis]=k;out[tuple(ex)]+=c*F(comb(k,b),comb(n,b))
  co=removezero(out)
 full=list(product(*(range(n+1) for n in degrees)))
 assert all(v>0 for v in co.values())
 assert (len(co),len(full)-len(co))==expected
 # Independent inverse of every Bernstein axis, expanded by the binomial theorem.
 back=co
 for axis in reversed(axes):
  n=degrees[axis];out=defaultdict(F)
  for ix,c in back.items():
   j=ix[axis]
   for k in range(j,n+1):
    ex=list(ix);ex[axis]=k;out[tuple(ex)]+=c*comb(n,j)*comb(n-j,k-j)*(-1)**(k-j)
  back=removezero(out)
 assert back==a
 return dict(degrees=degrees,axes=axes,positive=expected[0],zero=expected[1],
             coefficients=[[ix,co.get(ix,F(0))] for ix in full]),co

def analytic_identities():
 gx,gy,gz,aa,bb,L,B,zx=S.symbols('gx gy gz aa bb L B zx')
 ha=-aa*gx+L*gy+gz;hb=B-bb*gx-B*gy-gz;hz=1-zx*gx-gy-gz
 ell=1-L;d=B-1;H=ell*hb-d*ha;E=1-gy-gz
 assert S.expand(ell*(E-bb*gx)+d*(E+aa*gx)-H-L*d)==0
 assert S.expand(6*H-ell*(ha+hb)-(5*ell*hb-(ell+6*d)*ha))==0
 assert S.expand(ell*(ha+hb)-H-(B-L)*ha)==0
 # Coordinate elimination at exactly the same centroid, not five free poles.
 x=S.Matrix([-1/gx,0,0]);y=S.Matrix([0,-1/gy,0]);z=S.Matrix([zx,1,1])/hz
 a=S.Matrix([aa,-L,-1])/ha;b=S.Matrix([bb,B,1])/hb;C=S.Matrix.hstack(x,y,z)
 av=C.inv()*a;bv=C.inv()*(b-a);alpha,beta,cc=[S.factor(-v) for v in av];mu,nu,ww=map(S.factor,bv)
 assert S.cancel(beta-gy*ell/ha)==0 and S.cancel(cc-hz/ha)==0
 assert S.cancel(nu-gy*H/(ha*hb))==0 and S.cancel(ww-hz*(ha+hb)/(ha*hb))==0
 U=(alpha+cc)/beta;V=(mu+ww)/nu
 assert S.cancel(U-(E+aa*gx)/(gy*ell))==0
 assert S.cancel(V-U-ha*(H+L*d)/(gy*ell*H))==0
 assert F(1,2)+F(20,9)*F(7,100)+F(7,200)**2*(1+F(7,100))<1
 assert 1-F(3,4)*F(117,110)==F(89,440)
 assert F(89,440)/F(3,8)==F(89,165)
 assert 2*F(89,165)-F(25,24)==F(49,1320)>0
 s1,s2,t1,t2=S.symbols('s1 s2 t1 t2');U=s1+t1;V=s2+t2;P=t1*t2;R=(t1-t2)**2/(4*P)
 x=(S.Integer(1),0,0);y=(0,S.Integer(1),0);z=(0,0,S.Integer(1));v=add(sub(z,x),mul((t1+t2)/(2*P),y))
 left=matsum((1,outer((s1,1,t1),(s2,1,t2))),(-U-V,arrow(y,x)),(-U*t2-V*t1,arrow(x,z)))
 right=matsum((P,outer(v,v)),(U*V,outer(x,x)),(U+V-R,outer(y,y)))
 assert all(S.cancel(left[i][j]-right[i][j])==0 for i in range(3) for j in range(3))

def symbolic_proof():
 out=dict(lattice=lattice_proof());analytic_identities()
 t,s,r=S.symbols('t s r',positive=True);v=S.symbols('v',positive=True)
 Z,N,B,faces=image(t,s,r,'plus');Z={i:tuple(S.factor(a) for a in z) for i,z in Z.items()}
 N=[tuple(S.factor(a) for a in n) for n in N]
 assert N[2]==(1,1,0)
 out['height_bounds']=[positive_rational((1+20*t/11-z[1]-z[2]).subs(s,t+v),t,v,r) for z in Z.values()]
 ds=[];js=[]
 for fi,ids in triangles(faces):
  a,b,c=[Z[i] for i in ids];w=S.factor(det(a,b,c))
  if w!=0:
   positive_rational(w.subs(s,t+v),t,v,r);ds.append(w)
   js.append([S.factor(w*(a[m]+b[m]+c[m])) for m in range(3)])
 assert len(ds)==9
 D=S.factor(sum(ds));J=[S.factor(sum(x[i] for x in js)) for i in range(3)]
 g=[S.factor(a/(4*D)) for a in J]
 h0=S.factor(1-g[0]-g[1]);ha=S.factor(-dot(N[8],g));hb=S.factor(B[4]-dot(N[4],g))
 T=S.factor((5*g[0]/2+Z[9][0]*g[1]*(3-Z[9][0]))/(D*h0))
 L=F(1,2)+F(20,9)*s+t*t*(1+s);BB=1+10*t+F(9,2)*t*t
 exprs=dict(A=5*g[1]-3*r*g[0],B=F(51,25)-T,C=5*(1-L)*hb-(1-L+6*(BB-1))*ha)
 polynomials={};denominators={}
 for name,expr in exprs.items():
  p,q=rational_polys(expr,t,s,r);positive_poly(q)
  polynomials[name]=fcoeff(p);denominators[name]=fcoeff(q)
 # A: s=t+v, 0<=r<=7/5. Variables (t,v,u), r=7u/5.
 aa=defaultdict(F)
 for (i,j,k),c in polynomials['A'].items():
  for b in range(j+1):aa[(i+j-b,b,k)]+=c*comb(j,b)*F(7,5)**k
 aa=removezero(aa);out['A'],ca=bernstein(aa,[2],(2084,916))
 assert out['A']['degrees']==(29,9,9)
 ma=min(ca.get((0,2,k),0) for k in range(10));assert ma==731161600000000000000
 out['A']['strict_row']=[0,2];out['A']['strict_minimum']=ma
 # B: w=t+s>=7/100, t=w*x/2, 0<=x<=1, r>=7/5.
 bb=total_height(polynomials['B']);bb=shift(bb,2,F(7,5));bb=shift(bb,0,F(7,100))
 out['B'],cb=bernstein(bb,[1],(12278,7287));assert out['B']['degrees']==(42,34,12)
 mb=min(cb.get((0,j,0),0) for j in range(35));assert mb>0
 out['B']['strict_row']=[0,0];out['B']['strict_minimum']=mb
 # C: 0<w=t+s<=7/100, t=w*x/2, 0<x<=1, r>0.
 cc=shift(total_height(polynomials['C']),0,F(0),F(7,100))
 out['C'],cv=bernstein(cc,[0,1],(3534,1434));assert out['C']['degrees']==(26,22,7)
 mc=cv[(26,22,0)];assert mc>0
 out['C']['strict_coefficient_index']=[26,22,0];out['C']['strict_coefficient']=mc
 out['polynomials']={k:[[ix,c] for ix,c in sorted(p.items())] for k,p in polynomials.items()}
 out['denominators']={k:[[ix,c] for ix,c in sorted(p.items())] for k,p in denominators.items()}
 assert sum(out[k]['positive']+out[k]['zero'] for k in 'ABC')==27533
 return out

def audit(t,kappa,lam,metric='I'):
 t,kappa,lam=map(F,(t,kappa,lam));s=lam*t;r=kappa/t
 kind='plus' if s>t else 'minus' if s<t else 'wall'
 Z,Nraw,B,faces=image(t,s,r,kind);Z={i:tuple(map(F,z)) for i,z in Z.items()}
 Nraw=[tuple(map(F,n)) for n in Nraw];B=list(map(F,B));verts=set()
 for ix in combinations(range(9),3):
  z=solve([Nraw[i] for i in ix],[B[i] for i in ix])
  if z is not None and all(dot(n,z)<=b for n,b in zip(Nraw,B)):verts.add(z)
 assert verts==set(Z.values())
 edges={}
 for i,f in enumerate(faces):
  n,b=Nraw[ORDER[i]],B[ORDER[i]]
  assert {j for j,z in Z.items() if dot(n,z)==b}==set(f)
  for a,c in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,c))),[]).append(i)
  for j in range(len(f)):
   a,c,d=[Z[f[(j+h)%len(f)]] for h in range(3)]
   assert dot(cross(sub(c,a),sub(d,c)),n)>0
 assert all(len(fs)==2 for fs in edges.values()) and len(Z)-len(edges)+9==2
 D,J,ds=fan(Z,faces,(F(0),)*3);assert D>0 and min(ds)>=0
 g=mul(1/(4*D),J);apex=tuple(sum(z[i] for z in Z.values())/len(Z) for i in range(3))
 D2,J2,ds2=fan(Z,faces,apex);assert D2==D and mul(1/(4*D2),J2)==g and min(ds2)>0
 Y={i:sub(z,g) for i,z in Z.items()};h=[b-dot(n,g) for n,b in zip(Nraw,B)]
 assert min(h)>0
 Q=[mul(1/h[i],Nraw[i]) for i in ORDER];weights=[];means=[]
 for f in faces:
  dd=F(0);mm=(F(0),)*3
  for j in range(1,len(f)-1):
   a,b,c=[Y[i] for i in (f[0],f[j],f[j+1])];w=det(a,b,c);assert w>0
   dd+=w;mm=add(mm,mul(w,add(add(a,b),c)))
  weights.append(3*dd/D);means.append(mul(1/(3*dd),mm))
 Lam=[[weights[j]*(1-dot(q,means[j])) for j in range(9)] for q in Q]
 assert sum(weights)==3
 for i in range(9):
  assert Lam[i][i]==0 and sum(Lam[i])==3
  assert all(0<Lam[i][j]<F(10,9) for j in range(9) if i!=j)
  assert tuple(sum(Lam[i][j]*Q[j][a] for j in range(9)) for a in range(3))==mul(-1,Q[i])
  for j in range(9):assert sum(Lam[i][a]*Lam[a][j] for a in range(9))+Lam[i][j]==4*weights[j]
 assert Lam[0][5]==5*g[0]/(2*D*h[2])
 assert Lam[0][6]==Z[9][0]*g[1]*(3-Z[9][0])/(D*h[2])
 eye=[tuple(F(i==j) for i in range(3)) for j in range(3)]
 basis=(Q[5],Q[6],Q[4]);co=[coords(basis,q) for q in Q]
 if metric=='G':
  ci=[coords(basis,e) for e in eye];N=[[form(G,a,b) for b in ci] for a in ci]
 elif metric=='NGEN':N=[list(map(F,row)) for row in NGEN]
 else:assert metric=='I';N=[list(row) for row in eye]
 M=list(map(list,zip(*[solve(N,e) for e in eye])))
 assert min(minors(M))>0 and min(minors(N))>0
 assert all(sum(M[i][h]*N[h][j] for h in range(3))==int(i==j) for i in range(3) for j in range(3))
 neigh={i:set() for i in Z}
 for a,b in edges:neigh[a].add(b);neigh[b].add(a)
 stable=[i for i,q in enumerate(Q) if all(form(N,q,sub(qj,q))<0 for j,qj in enumerate(Q) if i!=j)]
 unstable=[i for i,x in Y.items() if all(form(M,x,sub(Y[j],x))<0 for j in neigh[i])]
 primitives=[];saddles=[]
 for (i,j),(a,b) in sorted(edges.items()):
  pp=[form(M,Y[i],sub(Y[j],Y[i])),form(M,Y[j],sub(Y[i],Y[j])),form(N,Q[a],sub(Q[b],Q[a])),form(N,Q[b],sub(Q[a],Q[b]))]
  assert all(v!=0 for v in pp);primitives.append([i,j,a,b,pp])
  if max(pp)<0:saddles.append([i,j])
 assert len(stable)+len(unstable)-len(saddles)==2
 alpha,beta,c=mul(-1,co[2]);mu,nu,ww=sub(co[1],co[2]);chi=9*r*g[0]/(20*g[1])
 assert -co[3][0]/co[3][1]==chi
 L=F(1,2)+F(20,9)*s+t*t*(1+s);BB=B[4];ell=1-L;dd=BB-1
 guard4=3*ell*h[4]-(ell+4*dd)*h[8];guard6=5*ell*h[4]-(ell+6*dd)*h[8]
 gate=None
 if min(beta,c,nu,ww)>0 and alpha+c>0 and mu+ww>0:
  U=(alpha+c)/beta;V=(mu+ww)/nu;t1=c/beta;t2=ww/nu;R=(t1-t2)**2/(4*t1*t2)
  stress=matsum((-1/(beta*nu),arrow(Q[2],Q[1])),(-U-V,arrow(Q[6],Q[5])),(-U*t2-V*t1,arrow(Q[5],Q[4])))
  gate=dict(U=U,V=V,ratio=t2/t1,R=R,J=R-U-V,stress=stress,minors=minors(stress))
  if kind=='plus' and t+s<=F(7,100):
   assert 1<t2/t1<6 and U>=F(89,165) and V>U and R-U-V<-F(49,1320)
   assert min(minors(stress))>0 and guard6>0
 # Test the tempting but false term-by-term version of the volume support guard.
 def fg(z):return 5*ell*(BB-dot(Nraw[4],z))-(ell+6*dd)*(-dot(Nraw[8],z))
 cells=[]
 for (fi,ids),vol6 in zip(triangles(faces),ds):
  if vol6>0:
   mean=(fg(Z[0])+sum(fg(Z[i]) for i in ids))/4;cells.append([fi,ids,vol6,mean])
 assert sum(vol*mean for fi,ids,vol,mean in cells)/D==guard6
 vals=[form(N,Q[i],sub(Q[j],Q[i])) for i,j in TREE];T=Lam[0][5]+Lam[0][6]
 if kind=='plus':
  if r<=F(7,5):assert chi<F(3,4)
  if t+s>=F(7,100) and r>=F(7,5):assert T<F(51,25)
 else:assert not any(set(fs)=={1,2} for fs in edges.values())
 return dict(t=t,kappa=kappa,lower_ratio=lam,lower_height=s,projective_ratio=r,chart=kind,
             vertices=Z,planes=list(zip(Nraw,B)),faces=faces,edges=[[i,j,fs] for (i,j),fs in sorted(edges.items())],
             volume=D/6,centroid=g,poles=Q,Lambda=Lam,M=M,N=N,
             counts=[len(stable),len(unstable),len(saddles)],stable=stable,unstable=unstable,saddles=saddles,
             physical_weak=0,primitive_zeroes=0,primitives=primitives,tree_arrows=vals,
             coefficients=[alpha,beta,c,mu,nu,ww],T=T,chi=chi,guard4=guard4,guard6=guard6,gate=gate,fan_guard_cells=cells)

def clean(x):
 if isinstance(x,(F,S.Rational)):return str(x)
 if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [clean(v) for v in x]
 return x

def main():
 assert __debug__ and sys.version_info[:3]==(3,13,5) and S.__version__=='1.14.0'
 assert len(sys.argv)==2 and sys.argv[1] in ('build','check','controls')
 out={} if sys.argv[1]=='controls' else symbolic_proof()
 specs=[('PARENT_CALIBRATION',F(1,1000),F(2),F(2),'I'),
        ('SIX_RATIO_BOUNDARY',F(1,30),F(1,30),F(11,10),'I'),
        ('OLD_C1_HEIGHT_FAILURE',F(1,50),F(1,25),F(4),'I'),
        ('OLD_QUAD_SECTOR_FAILURE',F(1,5),F(2,5),F(10),'I'),
        ('THREE_ARROW_HEIGHT_CONTROL',F(1,5),F(1,10000),F(3),'G'),
        ('LOWER_INCIDENCE',F(1,10),F(1,10),F(1,2),'NGEN'),
        ('INCIDENCE_WALL',F(1,10),F(1,10),F(1),'NGEN')]
 out['bodies']={name:audit(t,k,l,m) for name,t,k,l,m in specs}
 for name,d in out['bodies'].items():
  assert d['counts']!=[1,1,0]
  print(name,d['chart'],d['counts'],'T',float(d['T']),'chi',float(d['chi']),flush=True)
 assert out['bodies']['PARENT_CALIBRATION']['counts']==[4,4,6]
 a=out['bodies']['SIX_RATIO_BOUNDARY'];assert a['guard4']<0<a['guard6']
 assert any(row[3]<0 for row in a['fan_guard_cells'])
 assert out['bodies']['OLD_C1_HEIGHT_FAILURE']['guard4']<0
 assert out['bodies']['OLD_QUAD_SECTOR_FAILURE']['chi']>F(3,4)
 a=out['bodies']['THREE_ARROW_HEIGHT_CONTROL']
 assert a['T']>F(51,25) and a['tree_arrows'][4:6]==[4,4] and a['tree_arrows'][1]>0
 if sys.argv[1]=='controls':
  Path('height_controls.json').write_text(json.dumps(clean(out),sort_keys=True,indent=2)+'\n',encoding='utf-8');return
 text=json.dumps(clean(out),sort_keys=True,indent=2)+'\n';target=Path('height_full253_report.json')
 if sys.argv[1]=='build':target.write_text(text,encoding='utf-8')
 else:assert target.read_text(encoding='utf-8')==text
 print('ALL_POSITIVE_T_KAPPA_LAMBDA_FULL253_27533_COEFFICIENTS_PASS')
 for p in (Path(__file__),target):
  data=p.read_bytes();print(p.name,len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
```
