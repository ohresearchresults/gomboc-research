# figure-0485

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Clear Willow 56 — exact height elimination for the orthogonal base-root problem

## Outcome

No actual-centroid C48 strict110/additionalweak000 construction was obtained. The main new result is an exact elimination of both apex-height variables from the physical U1 problem, together with a coupled height-free polar obstruction. It replaces an unrestricted height search by a sharp planar inequality with constant **κ = 7 − 4√3**.

For a fixed mass-compatible planar base, the remaining complete physical/polar S/U height arrangement has an additional useful property: **its event values in the height ratio require solving polynomials of degree at most two**. This is an algorithmic completeness theorem for the fixed-planar-base height family, not an assertion that every such arrangement was enumerated here.

I also obtained a complete **2,205-labelled-wheel-tree necessary atlas**, without identifying different incidence embeddings merely because their abstract marked trees agree. Two exact rational nonwinners are preserved:

- **C48_RESERVE_FAIL_222**: V10/E24/F16, strict222/additionalweak000/primitivezero000. It crosses the short-side polar reserve gate, but its entire orthogonal height family is excluded from weak-U-free U1.
- **C90_ORTHOGONAL_BASE_U1_413**: V17/E45/F30, strict413/additionalweak000/primitivezero000. This is a genuinely own-centred orthogonal ordinary 15-gon bipyramid with its sole U at a base vertex. It demonstrates that the orthogonal base-root mechanism is nonvacuous for larger bases. Its fixed planar base nevertheless has an exact all-height obstruction to strict110.

The ordinary octagonal problem remains open after these results. Neither all orthogonal octagons nor any full nonorthogonal chamber is excluded.

## 1. Reading, source authority, and corrections

I read the complete supplied journal, including all three literal immutable parent payloads and their embedded recovery sources. The supplied file has 217,144 bytes and SHA-256 `b64755c7ecdbc4a3e1d79ae14c3711b9895c530d0edea4766ed3bb1bc9bf4274`. The parent identities are:

`figure-0469`, metadata SHA-256 `6d665d17ac5bae24efaf715229c6f9e71cb5d5149171b095c18f6c15a66a202e`;

`figure-0474`, metadata SHA-256 `a03ab041f25c69669ce6f4010d5318f60be3d7c0c7c6dc02b5cbcbd3fad3865e`;

`figure-0477`, metadata SHA-256 `c19dee1682fc20ee8b06d84bd0f00ec14edc7c4e4d940f7c213b440e3b004a8a`.

The decoded parent source units matched their embedded byte counts and hashes. I reran the normal-form verifier, the rational shear control, the apex-root algebra verifier, and the complete shadow enumerator. The latter reproduced 150,528 trees, apex counts 45,192/101,248/159, base counts 89,998/314,104/309, and union309. Its two output hashes matched the parent manifests. No required dependency for the present work was missing. Historical materials merely mentioned in the journal were not treated as separately accessible files.

Two source statements need qualification. First, the third parent's sentence that any zero outgoing dot makes the configuration weak is too strong. A vertex is additional weak-U precisely when **all** outgoing dots are nonpositive and their maximum is zero. A zero accompanied by a positive outgoing dot is not a weak equilibrium. The apex-root theorem survives: the corrected premise needed in its path argument is that every nonroot in a weak-U-free configuration has a positive outgoing arrow. Second, the first labelled representative of an abstract marked-tree code does not cover every geometric incidence embedding. The 309 codes remain an index, not 309 interchangeable labelled systems. The new wheel enumeration below retains all labelled trees in its stated coverage. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## 2. Actual-mass coordinates

Use the parent's mass-closed form, but denote the planar base in the actual-centred three-dimensional frame by

`X = conv(x_0,...,x_(n−1))`, with planar area centroid `c`, and put `p = −3c`.

Require `p ∈ int(X)`. For heights `a>b>0`, set

`d=(a−b)/4`, `z0=−d`,

`B_i=(x_i,−d)`,

`T=(p,(3a+b)/4)`,

`D=(p,−(a+3b)/4)`.

These formulas give the actual homogeneous filled centroid exactly zero. The volume is `area(X)(a+b)/3`. Both the base centroid and apex projection are inside X, so their convex combination `0=(3c+p)/4` is also strictly inside X. This is the parent's normal form with `x_i=c+s_i`; its crossing condition is unchanged. :contentReference[oaicite:2]{index=2}

Define

`P=|p|²`,

`L=max_i p·(x_i−p)`,

`A_+=a(3a+b)/4`, `A_−=b(a+3b)/4`,

and the height resource

`B=b(a−b)/4=bd`.

Here B is a scalar, not a base vertex. If `p=0`, both apices are strict U for every positive pair of heights. Otherwise ordinary crossing implies `L>0`.

The established apex-root theorem means every weak-U-free U1 candidate must satisfy `L>A_+` after ordering the heights. Thus both apices have positive escapes and the sole U must be a base vertex. The work below starts in precisely that remaining chamber; it does not repeat its exclusion proof.

## 3. New theorem: exact elimination of the two heights on the U side

For each base vertex define

`m_i=max{x_i·(x_(i−1)−x_i), x_i·(x_(i+1)−x_i)}`,

`δ_i=|x_i|²−p·x_i`.

Let `J={i:m_i≤0}` be the planar weak-sink set, and `J_strict={i:m_i<0}`. Since p is strictly inside X, `δ_i>0` for every i in J.

### Exact vertex classifier

The base-to-apex dots are

`B_i·(T−B_i)=−δ_i−ad`,

`B_i·(D−B_i)=−δ_i+bd=−δ_i+B`.

Consequently, in `L>A_+`:

`B_i is strict U ⇔ m_i<0 and δ_i>B`.

It is additional weak-U exactly when

`m_i≤0`, `δ_i≥B`, and at least one of `m_i=0` or `δ_i=B` holds.

This uses the complete normal cone. In particular, a planar zero arrow at a vertex with `δ_i<B` is harmless because the bottom-apex arrow is positive.

The vertices absorbed by the bottom apex satisfy the disk inequality

`|x_i−p/2|² < P/4+B`.

Thus a physical U1 height choice must absorb every planar sink except one into a single disk whose centre is fixed by the actual mass relation `p=−3c`.

### A protected strict planar sink

There is always a strict planar sink r with

`δ_r ≥ L + L²/P > L`.

Proof: choose e attaining `p·(x_e−p)=L`. Cauchy gives

`|x_e| ≥ |p|+L/|p|`.

Starting at e, follow a nonnegative planar cycle arrow whenever one exists. Even a zero arrow strictly increases squared radius, since

`|y|²−|x|²=2x·(y−x)+|y−x|²`.

The finite path therefore terminates at a strict planar sink r, with `|x_r|≥|x_e|`. Finally,

`δ_r ≥ |x_r|²−|p||x_r| ≥ L+L²/P`.

This auxiliary nonnegative path is used only to establish the protected sink; it is not being substituted for a positive physical escape tree.

### Sharp height-resource bound

Put `t=b/a∈(0,1)` and `k=a²`. Then

`B=k t(1−t)/4`,

`A_+=k(3+t)/4`.

Hence `L>A_+` implies

`B/L < f(t)=t(1−t)/(3+t)`.

The exact maximum is

`max_(0<t<1) f(t)=κ=7−4√3`,

attained at `t*=2√3−3`. Indeed `f'(t)=(3−6t−t²)/(3+t)²`.

For rational calculations, `f(6/13)=14/195<κ<9/125`. The last rational upper bound is useful only as a relaxed necessary inequality, not as a replacement for the sharp criterion.

### Complete height-feasibility theorem

Let **D2** be the second-largest value of δ_i over J; set D2=0 when J has one member.

**For a fixed strictly convex planar X with actual mass coupling `p=−3 area_centroid(X)∈int(X)` and p≠0, there exist orthogonal unequal heights giving physical strict U1 with no additional weak-U if and only if**

**`D2 < κL`.**

More explicitly, all such heights in the ordered chamber are exactly those satisfying

`D2 < B` and `A_+ < L`.

Equivalently, choose t and k in

`4D2/[t(1−t)] < k < 4L/(3+t)`.

For necessity, the protected strict planar sink has δ>L>B and cannot be absorbed. Every other planar weak sink must have δ<B, including sinks possessing a zero cycle arrow. Thus D2<B<κL. Conversely, if D2<κL, choose B and the heights in the displayed interval. The protected sink is then the unique unabsorbed sink and is strict. Every other base vertex has a positive cycle or bottom-apex escape; both apices escape as well.

For rational X the criterion can be decided without floating square roots:

`D2<L` and `D2²−14LD2+L²>0`.

Rational heights exist whenever the strict criterion holds. Deterministically enumerate dyadic t in (0,1) until `t(1−t)L>(3+t)D2`, then enumerate a positive dyadic a whose square lies in the corresponding open k interval, and set b=ta. No irrational coordinate is needed for recovery.

**Scope:** this is a necessary-and-sufficient theorem for physical U1/weak-U0 over all orthogonal heights above one fixed planar base. It is not yet an S1 theorem, a full-SPD exclusion, or an exclusion of all planar octagons.

## 4. Combining the height theorem with the explicit polar prism

Let `S=X−c`, and let the rational edge covectors satisfy `u_i·s_i=u_i·s_(i+1)=1`. Put

`w_i=1+4c·u_i>0`,

`F_i=w_i(w_i+3)/(4|u_i|²)`.

Geometrically, if a unit outward edge normal has base support h_i and apex-to-edge planar gap k_i, then `F_i=h_i k_i`.

The parent short-side reserve becomes

`R_i^−=w_i(w_i+3)−k t(1−t)|u_i|²=4|u_i|²(F_i−B)`.

The top reserves are always positive for a>b. Therefore the top polar ring always supplies a strict U, hence a strict top stable facet. :contentReference[oaicite:3]{index=3}

For physical S1 with no additional weak-S, at least one bottom reserve must be **strictly negative**, not merely nonpositive. To see this, choose a bottom-ring vertex of maximal squared norm. Both of its cycle dots are strictly negative. Unless its lateral dot is positive, that vertex would be a strict or weak polar U. Since the unique stable facet is already on the top side, a weak-free S1 body must give this bottom-ring maximum a positive lateral escape. Thus some `B>F_i` is necessary.

This argument does not say that an isolated equality `R_i^−=0` is automatically weak-S. At a nonmaximal ring vertex another outgoing dot may be positive.

### Coupled height-free gate

For a selected bottom-edge branch i, put

`M_i=max(D2,F_i)`.

There exist rational heights satisfying physical U1/weak-U0 **and that strict reserve failure** if and only if

`M_i<κL`.

The allowed height interval is

`4M_i/[t(1−t)] < k < 4L/(3+t)`.

Therefore every orthogonal strict110/weak000 survivor must satisfy the purely planar necessary condition

**`max(D2,min_i F_i) < κL`.**

Passing this test is not S1: it only opens the required vertical escape. The two polar cycle directions remain coupled to the same base and must still be checked.

### Complete remaining polar cycle numerators

For j=i−1 or i+1 define

`g_i^+ = k(3+t w_i)u_i + 4(3w_i−kt|u_i|²)c`,

`g_i^− = kt(3t+w_i)u_i + 4(3w_i−kt|u_i|²)c`,

`N_ij^+ = g_i^+·(u_j−u_i)`,

`N_ij^− = g_i^−·(u_j−u_i)`.

The polar vertices are

`q_i^+=(4u_i/(3+t w_i), 4w_i/[a(3+t w_i)])`,

`q_i^−=(4t u_i/(3t+w_i), −4w_i/[a(3t+w_i)])`.

Exact identities are

`q_i^+·(q_j^+−q_i^+) = 16N_ij^+/[k(3+t w_i)²(3+t w_j)]`,

`q_i^−·(q_j^−−q_i^−) = 16tN_ij^−/[k(3t+w_i)²(3t+w_j)]`,

`q_i^−·(q_i^+−q_i^−) = −16w_i(1+t)R_i^−/[k(3+t w_i)(3t+w_i)²]`.

All denominators are positive. The symbolic source verifies these identities universally, not just at the two controls.

Hence S1/weak-S0 is equivalent to selecting one top index r for which both N^+ signs are negative, requiring a positive N^+ cycle sign at every other top vertex, and requiring

`max(N_i,i−1^−,N_i,i+1^−,−R_i^−)>0`

at every bottom vertex. Zero primitive signs are retained correctly by these maximum tests.

## 5. New fixed-base height-atlas theorem: only quadratic ratio events

For fixed rational X, every height-dependent physical or polar S/U primitive, after multiplication by the positive denominators above, has the form

`A(t)k+B0`,

where `degree(A)≤2` and B0 is independent of t. The base-cycle dots are constants. This includes both apex rows, both base-to-apex rows, the two polar cycle rows and both vertical reserves.

A zero curve is `k=−B0/A(t)`. Its poles and changes of sign come from a polynomial of degree at most two. Two such curves cross only at roots of

`B0_i A_j(t)−B0_j A_i(t)`,

again of degree at most two. Thus the complete open S/U sign atlas over `0<t<1`, `k>0` can be generated by the following exact procedure:

1. Build all these rational coefficient pairs, retaining identically zero primitives as zero signs.
2. Isolate and sort all real roots in (0,1) of A_i and of the nonzero pair-crossing polynomials.
3. Choose a rational t in each interval. Order the positive k zero curves there and sample every intervening positive k strip. A rational a can be chosen with a² in each strip.
4. Label the cells using complete outgoing maximum tests, not primitive nonvanishing.

Only degree-two algebraic event values are needed. Coincident curves are deduplicated without changing their recorded signs. A strict U1/S1 point with no additional weak equilibria cannot hide only on an isolated noncritical primitive-sign boundary: its strict root signs and positive escape witnesses persist in a parameter neighborhood. Equal heights are separately excluded from S1 by the parent theorem.

This proves completeness of a much cheaper fixed-planar-base height analysis than unrestricted nonlinear height optimization. **I did not enumerate this full arrangement for every planar octagon.** The two exact controls below have simpler scalar certificates closing their entire height families. A promoted 110 sample must still receive the explicit maximal-hull, mass and mixed-edge audit; the S/U arrangement is not a substitute for that audit.

## 6. Complete labelled wheel reduction

There is a second useful reduction specific to the remaining U1 chamber. If a base vertex has a positive arrow to T, it also has a positive arrow to D, because the latter dot exceeds the former by `(a+b)d>0`. Select a positive cycle escape whenever one exists; otherwise select D. Both apices can select the same base vertex e maximizing L.

The resulting positive escape tree has T as a leaf. Removing T leaves a rooted spanning tree of the wheel consisting of the eight labelled base vertices and the hub D. By a cyclic relabelling the unique base root may be fixed to 0. No abstract-tree isomorphism is used to identify the remaining labelled embeddings.

The complete exact enumeration gives **2,205 labelled wheel trees**. Counts by the number of base-to-hub parent arrows are

`{0:64, 1:336, 2:672, 3:660, 4:352, 5:104, 6:16, 7:1}`.

Counts by the hub's parent are

`{0:987, 1:378, 2:147, 3:63, 4:42, 5:63, 6:147, 7:378}`.

The recovery source emits every tree, its eight selected edge indices, and the complete parent array. These are necessary labelled skeletons, not 2,205 feasible geometries and not an elimination certificate.

Actual planar mass supplies an additional exact constraint on this atlas. Triangulate X from the root x_0. With positive normalized triangle areas ω_i,

`p+x_0+Σ_(i=1)^(n−2) ω_i(x_i+x_(i+1))=0`.

Therefore at least one nonincident base edge satisfies

`x_0·(p+x_0+x_i+x_(i+1))≤0`.

This is a planar mass witness, not a freely chosen centre constraint. It can be combined with the wheel inequalities and the disk bound before any polar branching.

## 7. Exact rational controls and complete recovery data

Both controls use all of the following maximal facets, with base labels 0 through n−1, top n, and bottom n+1:

`face i = (n,i,(i+1) mod n)`,

`face n+i = (n+1,(i+1) mod n,i)`.

The verifier independently enumerates every supporting plane from every vertex triple and proves that this is the complete maximal hull. It then reconstructs all true edges. Face normals, the same-centre polar, all outgoing dots, all face-foot barycentric coordinates, all edge-foot/cone coefficients, and both mass decompositions are regenerated in the reports.

### C48_RESERVE_FAIL_222

Take the following complete planar rows divided by 4000:

`[(9100,-19),(5100,781),(-2900,1181),(-10900,781),(-14900,-19),(-10900,-819),(-2900,-1219),(5100,-819)]`.

Set `a=1/10`, `b=3/65`. Then

`c=(-29/40,-19/4000)`, `p=(87/40,57/4000)`,

`z0=−7/520`, `zT=9/104`, `zD=−31/520`.

The base area is `12/5`, volume is `38/325`, and actual filled centroid is exactly zero. The common coordinate denominator is 52,000, with 18-bit maximum numerator. The minimum strict crossing determinant in the declared planar coordinates is `1/1000`.

Exact census:

`S=[4,12]`, `U=[0,4]`, `H=[(1,2),(6,7)]`;

`V/E/F=10/24/16`, `strict222`, `additionalweak000`, `primitivezero000`.

Its scalar data are

`D2=910361/4000000`,

`L=868917/4000000`,

`F_min=1801/4160000`,

`B=21/33800`.

Thus `F_min<B`: the short-side reserve obstruction has actually been crossed. Nevertheless `D2>L>κL`, so **no orthogonal choice of heights over this fixed planar base can have weak-U-free U1**. This is a whole-height theorem, not merely the audit of the displayed pair of heights.

### C90_ORTHOGONAL_BASE_U1_413

Take the following complete planar rows divided by 1,000,000:

`[(1000000,0),(673388,468902),(434067,632935),(195008,699505),(-34746,687830),(-241725,605072),(-408167,456011),(-509376,248025),(-509376,-248025),(-408167,-456011),(-241725,-605072),(-34746,-687830),(195008,-699505),(434067,-632935),(673388,-468902)]`.

Set `a=1/50`, `b=1/100`, and compute p from the exact planar area centroid, not from a rounded approximation. Explicitly,

`c=(132007207880392961/784793205759500000,0)`,

`p=(−396021623641178883/784793205759500000,0)`.

The heights are `z0=−1/400`, `zT=7/400`, `zD=−1/80`. The exact volume is

`1569586411519/100000000000000`,

and the actual filled centroid is zero. The common coordinate denominator is `1569586411519000000`, 61 bits.

Exact census:

`S=[0,14,15,29]`, `U=[0]`,

`H=[(0,15),(0,16),(7,8)]`;

`V/E/F=17/45/30`, `C90`, `strict413`, `additionalweak000`, `primitivezero000`.

This body is **413, not 211**. A provisional filename used before the class assertion was checked contained 211; that alias is rejected. The final source, final report and all manifests use 413.

Here `D2=0`, so the physical U1 height condition is genuinely feasible. But

`L=1478428058350296467348384085484887/615900375806272903971840250000000000`,

`F_min=4244648781772978893/1751770548570312500000`,

and exact comparison gives `F_min>L`. Thus every base-root U1 height pair has `B<κL<F_min` and both polar rings retain strict U roots. The other height chambers are covered by the apex-root exclusion or the equal-height stable exclusion. **This fixed planar base has no orthogonal strict110/weak000 height choice**, even though its physical U1 chamber is open and nonempty.

The larger control was nominated using projection-chain geometry of the kind described in the Conway-spiral literature, but its acceptance here is entirely by uniform-volume exact arithmetic, not by a point-mass argument. No minimality or priority claim is made. :contentReference[oaicite:4]{index=4}

### Verification level

There is one complete exhaustive rational maximal-hull and S/U/mixed-H implementation. It uses two different positive tetrahedral mass decompositions: coning maximal boundary facets from the actual origin, and the common-apex tetrahedra `(T,D,B_i,B_(i+1))`. Both give identical positive volume and zero first moment. The polar census is checked independently against the face-foot census within the same program. This is not two independent full mechanics implementations.

## 8. Nonorthogonal continuation: an exact two-disk formulation

The height theorem suggests a concrete extension rather than transferring its orthogonal bound to an oblique body. In canonical `G_ρ`, set `Δ=1−ρ²` and use the effective planar coordinates

`Y_i=x_i+ρz0 e_1`,

`P_T=p+ρzT e_1`, `P_D=p+ρzD e_1`.

Completing the metric square gives

`B_i^T G_ρ(B_j−B_i)=Y_i·(Y_j−Y_i)`,

`B_i^T G_ρ(T−B_i)=Y_i·(P_T−Y_i)−Δad`,

`B_i^T G_ρ(D−B_i)=Y_i·(P_D−Y_i)+Δbd`.

Thus a base planar sink can escape into either of two disks:

`|Y_i−P_T/2|² < |P_T|²/4−Δad`,

or

`|Y_i−P_D/2|² < |P_D|²/4+Δbd`.

The first disk may be empty. The original mass relation remains `p=−3c`; the two disk centres are not independent controls. Both apex gates and the full explicit polar must still be checked.

A useful rational next slice is `ρ=3/5`, realized by the rational physical map

`A=[[1,0,3/5],[0,1,0],[0,0,4/5]]`.

The symbolic source verifies the two-disk identities. No nonorthogonal feasibility or exclusion is claimed. In particular κ and the orthogonal apex-root theorem must not be reused unchanged in this slice. Canonicalization remains a joint shape-plus-metric gauge, not a reduction of a fixed raw body's full SPD orbit.

## 9. Finite attempts and what they do not establish

The supplied numerical sources preserve the attempted methods. A 12,000-case actual-mass orthogonal scout found neither U1 nor S1. Six completed joint P/Q optimization records used 3,460 iterations and 6,324 evaluations; four Q-biased records used 1,895/3,690. Twenty optimal-height-ratio P runs used 734/6,034. No C48 strict110 candidate was promoted. Near-zero local objectives often accompanied nearly coincident vertices or multiple roots.

Relaxed wheel-matrix experiments produced floating negative-definite nominations in 87/120 initial cases, 89/120 augmented cases, and 564/756 further tested branches. **None of these floating nominations is promoted as an exact blocker bank or finite geometric elimination.** The durable wheel result is the exact labelled enumeration and the analytic necessary conditions, not these solver success counts.

The 7+7-angle projection-chain nomination produced the exact C90 control after a strict radial contraction and rational freezing. The stored nomination can be replayed without rerunning optimization. Smaller or larger exploratory chain runs do not establish a minimum required number of base vertices.

One stale comment in `probe_mass_freeheight.py` calls its reference arbitrary. Its implemented formula uses three quarters of the exact planar centroid and is the actual horizontal-mass choice. `probe_s_geometry.py` is the separate centre-free experiment. No theorem or exact body relies on those exploratory comments.

## 10. Most useful continuation

Search planar geometry first, retaining the exact area centroid and crossing. The immediate objective is to find a strictly convex rational octagon satisfying

`max(D2,min_i F_i)<(7−4√3)L`.

A failure of this inequality closes all orthogonal heights over that planar base; it is not evidence against every octagon. A success gives explicit rational height windows and a selected polar reserve branch. On that base, use the quadratic-event height arrangement to decide the complete S/U problem, rather than launching another unconstrained height optimizer. Retain all labelled wheel embeddings if a tree-based proof is attempted, and use the actual fan-area mass identity. The two-disk `ρ=3/5` slice is the natural separate continuation when raw planar changes fail to enter the coupled orthogonal window.

## 11. Source-only recovery and receipts

The complete decoder below reconstructs 13 source units. No parent file, sandbox report, external library item, or numerical optimizer is required to recover either exact body or the wheel atlas. The exact geometry auditor and wheel enumerator use CPython 3.13.5 standard library only. Universal symbolic checks use SymPy 1.14.0. Optional numerical methods use NumPy 2.3.5, SciPy 1.17.0 and Torch 2.10.0+cpu, float64 and one thread as set in the sources.

Run:

```text
python -B -S RECOVER_C48_HEIGHT_REDUCTION.py OUT
cd OUT
python -B -S VERIFY_ORTHOGONAL_HEIGHT_REDUCTION.py
python -B -S ENUM_C48_WHEEL_HEIGHT_CELLS.py
python -B VERIFY_SYMBOLIC_HEIGHT_CELLS.py
python -B NOMINATE_ORTHOGONAL_C90.py
```

The final source-only recovery was executed in a fresh directory. Expected markers include:

```text
C48_HEIGHT_SOURCE_ONLY_RECOVERY_PASS 13
ORTHOGONAL_HEIGHT_REDUCTION_TWO_EXACT_CONTROLS_PASS
C48_ALL_LABELLED_WHEEL_HEIGHT_CELLS_PASS
FIXED_PLANAR_HEIGHT_ATLAS_ONLY_QUADRATIC_T_EVENTS_PASS
SYMBOLIC_HEIGHT_POLAR_FOUR_EDGE_IDENTITIES_PASS
NONORTHOGONAL_TWO_DISK_IDENTITIES_PASS
C90_LITERAL_PLANAR_ROWS_FROM_STORED_NOMINATION_PASS
```

Expected exact reports:

`C48_RESERVE_FAIL_222_AUDIT.json`: 6,701 bytes, SHA-256 `0ea35355e5ae4f6051736c89aead0ad20c6473bfa15907795dc420ee28f1b160`.

`C90_ORTHOGONAL_BASE_U1_413_AUDIT.json`: 45,585 bytes, SHA-256 `93413f932d0e628e41edd7cbf3c2279d21376561e6d587401379a298ab855952`.

`C48_ALL_LABELLED_WHEEL_TREES.json`: 94,240 bytes, SHA-256 `f04cb459fd1dbca7819751e3cffdc3141b3e0f62fdc614a38c132911b6a5d427`.

The decoded source dictionary has 36,275 bytes, SHA-256 `059893836ba9e6857bd0a410cfaad915f9b92c28675d119e67a3a8cdaa4cb067`. Its XZ payload has 11,436 bytes, SHA-256 `049d6baadfe1491346c44870fff84127687214085a0c25f9840bd94d6187dba1`. The decoder file has 16,634 bytes, SHA-256 `3cfca31a93e2108fe08d088d254f2f49a3a81f2151b1b941988289b72de05eb4`.

Optional finite-method invocations are `python scout_orth.py`, `python search_orth_torch.py 6 both`, `python search_orth_torch.py 4 Q`, `python search_p_optimal.py 20`, `python wheel_sdp_base.py 120`, `python wheel_sdp.py 120`, and `python wheel_inside_probe.py 10000`. These reproduce the prescribed methods and finite windows, not exact exclusion certificates. The optional C90 numerical rediscovery is `python NOMINATE_ORTHOGONAL_C90.py --search`; exact body recovery does not depend on repeating that floating trajectory.

A convenience copy of the same decoder is available at [RECOVER_C48_HEIGHT_REDUCTION.py](sandbox:/mnt/data/RECOVER_C48_HEIGHT_REDUCTION.py). The complete source recovery follows inline.

```python
import base64,hashlib,json,lzma,pathlib,sys
out=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'C48_HEIGHT_REPLAY')
out.mkdir(parents=True,exist_ok=True)
B85=(
'{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;El2@YFz+5h=io#(fm^A5G|0Dl`E;+9a5gU?#OHv?lO!hW<~hm4wTJG(0x4-$A{0YIBbzd'
';sr5Dz#*6}ia)l}#7{g%QLf?Z+LLq{gvo;o*yAcPq@NSpSSDYo0B!Iqd|Y>jE-rC}FuwJ0Q%u1=-;_h>W-6+PVL}`2mVAm~;Ku*d'
'j78y^UffOJGj_CAyQ?~K3ope+s&cNjOjHRRE2HIJ9DxUnv`7jrEkOT64O_D*5@0Nx8`ui5@^1s2xn`?7UU?woLqv(b0D}1WtJvGE'
'j%l@0|HU-T781r<M!@0gm~i3<jsy_FH3RG#w=SobZ}v$o_h(6z5UvD(#b;6bSliT*N9-VU#V;%(?rDBeb7<!0Ovp1yZF@#18@dJO'
'#>L*~s!FL2yRKQ-{{P$i=<&F3?*Mz7RSt6$oA^B*)cBbtu7JTw9B`@T>)lawcH&oqWV8qPudHMy{{9<|yk+Yr^wX-jCST95$%<9_'
'd*|Zp4LO2YM>xX`?p~zABpC+iLDDHA;zVy#U9O4dE>V1$t^p|w4jA`6T@E6YU(B6=(TQixO(^fc%wubZ_#5^L7BQ8-<Xn0KsQ`>%'
'%>eRFpgOl5(OEnYR%1c|Lawk#Tx-_t=(RHSBsMd>@21I#`r>l3^iT|?;a`aY8Y~j|^3+n&0dV{Afy{r9Ro!VWjqr$e_ymgla29g+'
';seY1E_B#xVxLOm(Jz59l(drsXJusHQ;Dga-KZpPJTh%5d>YU3^kSy(GgYG;trYZzE6K4ieFdim@MB1EJb#^y;@=^eLlo!ymN;La'
'jv?2i_W9tloaQFFy=Y%|kFs2H`U$l7q7-J7(3vcHp@?dnoZt8RxL(uN+fb*Xhbiu%Bu`Ctl-7G<#skN|x$CUY3Ft~l*r@c556}U_'
'K!AOo{o#R?WILY@NIaf1swP^n1&&<u>r<0Rt`fGENr1nW(_YLZ{eXR*A5jn00o_ntI|hsUyQmeNt(F^@InaZI)3kMww*8)eu4LD3'
'fJQ6c*Fk_4$hdK}5C_|rJHQn%^tlm4KqT?ZtA8UjW}F-c&l;b2!{I<0_=g`7W)(<?kz6F}{-TTWtahogY~3t1?dY2}Zdi-nr^fcR'
'h6%&R8cm3B!<_*3-G%VloX5JP&4HQ|E%^E}<>-sjLA+rPcIc4vYd1B1A@m%kj88q2HgD|Zo*ucER*6&O5rQ^F&$!?2ggcaE2&$BA'
'tY<=N>r-wzL+TK>PnkFz`0zzED~DO|pT)moWaLKGJ=1id=0H3h)PBb{Ocf~JfHnbi2|(7SgDF1o9Yut?yYtZtP$LV*{tUp-mwqeo'
'3?@juyEg0zYF@dwqQeczC92|s=`fbNS{O{09fV6tfvUo>uDvM6yL-+uQk(riuxUf`ud0UiQjdg+>xav4SYdJtgvirv@SV1BIRe(0'
'^~QxwZ@@Bo<kcjI-RhYau-0^QIfr>%?TY=3eB@8|gTj$%s3*bDu|BJ)l`^&i*BRyv@xOduF#*NkUHn9><zL=L4F2Jb;iD4gwSXpD'
'@xG_`LvZ7d<S%3;Fk%-1x3+>`nDX{$rM^|(dO+ea)l#Y^86Xwum$qT;5&%{coRv4U9kbOopOlhipOhHNKw7VG{5vYvztgHi`oj79'
'{m`P*xX1IuDQ{AHsCgM2U<PX9t{=I&af}n1dzg_zC7lxGSQ^CfFO{Y!O*GUs^ZU9Rzs=1>WLp`(obzG{Q#!j%XdcNuM4feLyB-IT'
'L=dW^As9JtM$0pka2NiSKjGmE*>wq`55`NZEi!w!vt_w$4&EViV=8(g+mf<n9q#iEuxC}Vm^%`!7C8Ag+@S6f%1gqxFFhT*Xn>aT'
'9>m9h^$!fq<q|QBI<7z8-);KVHfizijO=L;WY<~{;>kYM0OE+I_6zQr$L=ljS|Mf{Yid+r=$60FdP>-D8F}NVlm3MT!$lun>&zfI'
'bVh%r^g>ATHRk+W7xdL}t)Q9`Oxfjd&b5SX3$Rj!He0o0Zn~5KKBmOAD;X??C;vq8(q=|~pJHg$J=F>g%108fP^1_u1d$}kq^XB('
'*Ye*?4fhIdjY>{P>n&I#-{509nd?BO`LpWpC3T-cCO9mHT!Xd`3$ZN0KiooJ?E=jSRRk)7`JD#_NqCEx-4US+@=gZFSHwkl2mz3_'
'4Hes#bN4o0pdyEjP7iPUNuWUxf_x$U8lX>)#qX9z5I(_;;qD|0-TR>lrGZSZkC9Qjs5aNS#sOG91d-`;_W(LkdFc?U>Y4&r+~<UZ'
'xIW*;9vX7j{Kq*(UfFYCahV`1`?7vY3K>3sqa0MC_++7JJwk{E@a5<tUVg9@V4j7X4umWNd^dU!g(K3>VQRMW2SWLisbLc$vRuGS'
'z*;O{4!+S?yBXs`vKO}vXAPX24eGXe3E{Pw{!Z`$ga?tSk-gnj`U(tG(k*$WXqgo7WM=5kK0gg7@4Ke{o16Cq!fHZm|KlY&m0U3%'
'@j?3e{^(83R1MEqqOZ7~xQLW>i*6h9L3Q1r`B;9u&HJ<IwtNcn@mxhK{;!tesV1OLxbku2SNJMK{8BfkM{HE(aD3WShJ?|-S}|*A'
'*6IMWn<J0#D_U_B9Fe^q;*#1uifE@oyZw2UiCKdcTAT4au7J8bkU|xd>WT3!Ovla@n9eB+v1k^-1S8fZ-<>(+XYApgBam}ba1Y7~'
'vKELVY`R6)L{$?5&~8C1!%Gp2S7u`=gY66<KLLrXMx~WuJK=fJmI@Yw1+fF^RzT7tyRl|O9_!q_q22v(;?=GcHNl)q7e{mki4Z^W'
'ei(U3L6loTtJaiYBRO;V2tVy1)|!F0$h&SUk%AJq>NaF|RNka>`cVJWcfYh*rY1*@6NUT0Oa(uSSK;ujXw8QCkemU3y@%FJbOUM('
';&deV92sg?laV267M*v#zmGSsPVJka(shLP-2gt`O+yj+Wr`x3aIC3{gl*V+SZADcyEf?Fph<oIp~*OJf|=w>ApGib4@qMtSyTDs'
'1ef=Z+-iUwI(Pw;!#$5VL^CR7k+lUzs1vQS1*A3-;^y=eRDd2OV~aC9Gf`iOQhQI%uMY{YyVKXMgcZC>`GrEO=*BN|n|73TxY<6('
'GcfyCn+Xk4;hT3d-QGS)aPv&I`^p*2da`E+)eMv#jBRWqG@$-=TJ}=ObwC|=n}alezqKr_D3j~`9D4+Ivi8^Kt%ndZJ^3D`9&aLd'
'r)w+F5PK@Pdk<fg&IPSBh~Hlz|A=kSMthxn0Ujf<-$!-88?T~WRBBA+<YT+yD`tw1{0z@%AD52srw={5Sh2+8z!hHHUiI}1sce6s'
'I`ns1V*u&BI2v05_i_DaR&+V^xU3*GNb{Xt=tuj@laNQ3<SOgg`evKmA=H(!!ewSn-ayf)=AD`~l=n3!0uUrRZ{sNqP}nzrtbPXW'
'c($zj^tmD~Tp`o632Xhk*^_Cat|3!AqSm)i1JQI(R;6{04Y%E)w(Jk}6;Qjmay-4#RlrzYydaORJah;xoF7@uHhLp<YYc-Fe5oe>'
'py<SWh+gw65P3)~+`h=I#CH^^dL8Z#-p!SQk2sTV_ABc0h6q#p2W&*u6hi<06*&x-BZJlOC@$##$<Sei7{GZ6wVrUlkGOsRfo$MU'
'MOXJbZ6lIjnxao7!4<>+dt^`pA2`=*hLOl<2}>ZOSk}&K*bExz{89gOdz~@8Y_>Gr$}{TB?G4kntoBAf{AxUX^B^ls#dZ3Aw}ng4'
 'tVf61cr{`2s4D3h&zl##L*ewzk@m~P{6SB&0(mbW)T!V^i;9tT=o#Ou)WacF5SpHl$q;+8ITcBQeCzGD0A0<Lg)K}DGrC-O30xbX'
'@ArwdU;T>rWqA_dGP{ORBkhxnZsDAxruz9+#{ks6_$uAv&OiGm@EX#MRG~I0MPr|@34OT-NPozkn%3fy(pg_XK*mdk*TM!*K~!(;'
'$;UTlu%CpkvjfOW^Q99d{!Tmia{Fply`7PItS-o(hSV#5=S(~LEd#3w-?SUV0oF;+%NQU~ZeXCCbY=pg!KRrQPcw4Rv*G=DzJ+<N'
'dv<6qp+AMFl7^Tl^wlx2!69|kZr)oUrn|Fq6yaUbAmfkQ|D3Az!D>?gP9%VsnFQ3Tznp*34;p})x<$E$p_hT(*l<+@Eyj*rH820a'
'Y%7K<$M%T+-H(NMv=^U5*(25`zJB2-Iuhk9=2ll=w|pplR2LF1E?a_@%Hlg;Ty6Lq&L1}0`UCox$hSk-Lri*9Q}K4Y1S6GbQKmP@'
'#EbLS5>~O(jY_xLk3!c6;a<#CN|dT%ZvGKSq}e&43~FFNUcHQR^7rV9pzWrlNbc8*-K!NZS94?IqBsjz_i%rZz_ZWdGKY^?jtC0l'
'(5_VDy%ve6q#n}-UGrN97b{~X!OdBQ5N5nm;Uc5`;H*Z^ZYybWg;rxSQh`bv+9<7l!e(jPTknf)Zik*)<lfFQi+~K-`ui+;5Q5U;'
'SZx8{*L(Fyi>-18({aV>v<z#oSywgki^%8lWYC%C;4l4S(Tk6GQ#-9p-^;;YlQXi#1)Z|cVAj}MKNYBk<qgrIIz4@L|FP`)^h1KT'
'HGyQjb6$V1;S$e)qiuI5->4$gsIG=4#Lzu<sbGC7Ct>&sw2C^gD3vgQmQ`abr&#x145Zq#Ap@>}*U@c@9L!WYVGT<fn#fUDVIaQK'
'!Ku#E=A1Rxc5T5rb}n$D5Jn8Gh+B9k)vT6&%!}hjIt{-aJybE$(o$VO<*Ou6H3VkL%W7bU0R`G|%J*xi#g@)~BgyksXoDrv4LPjO'
'4=4j}Rj?WylG+@zHE_qzID}b21R&ojW(z2~*HHfz2+x|eBcge=;9(9xqQMd;#P=IFLK7q$H_q0+YXsneLk?DH&<&IdHigiAR9e4h'
'|09^Uk@{F+iI%0>bZ$)Nbg)Zw%<rToTHQ^%i?xr|I}>a)H|leEvdd=EgRPamLP0t;#K6odDIv+rMSLF<*gQC#b3pS)Ac`s!&kcfv'
'MFv(x`Z+Dd!->UqIWQXKJ_jnQHLM0ork~=jFg^8+C(v(8*~?9zEq?KvaaxqKYi2mhOjCs}KxeINO?nB|0;n?Hs83E37dHvi+dDHk'
'SqV^YRq8Nup3ABsv{$uJ^P$(dFl)!d^H`m1D+oSN%a;9+3^mn`eaFn<z;jVl9t|$U$OTR}jq>IsdXG3edXt}xRGSEljrts^5ruEC'
'=t%HOonUlwG}q*W>fJ34t;r2!{LQd8m2`-6HF(4%!kYvM5l>)n<en$qO;m_+quT9%pm!N(uBAprV>kqZ3W$#xDS7>?TNgTpRZ#DL'
'QxGkGEUKT;&z&dnbp*ddm>AauxX|ezn#l<vq}9*<N-4L}ZWh6pj;>J3t|5(Edbn75rIl!+P0}7zy`T-8&sP<dX*ZxIo|`jLu+Q~s'
'u`U1f-J1Kv_@sP6%zIK`=hT)M2CLb@bN7ck7-Fy`KQ9NoX6G#+h|;1+#1`P<8FxO%UDD}tjb%4ie31Cz5$8c_5N16u0kY8r;Sc=_'
'z9orSBsBXtysn0{JR5z9M+CP<WU&@T8_Z<z0`In!D0Ua@RvjlkKOI)j|MxwdUQOopi>92;Y*cpodUR^!rDv{Q{T?nC45M)}m(iD<'
'cFeqZ-UZ%ixCh{>w0ZJt^FYP|qAhM&%}f?N85RMJNQREZo0m!%t92qb4iL}Kf(Fi#8JCP4gxUlCz6te|NgVAtD<b?rp)eB)>)4S~'
'Cl=#(m*o=E8KnE}j|U|!&afrM)FAqugg}(AefG{r^ql*oO|T>O=zr1d*I!9KiIK16UBE;AzYXNNpEhm}BB@@W)*;>3Ne*`r>l$3k'
'Q6Y6XjNYnAFmRxI?}vfx#f^jw&M_i2___Q8*GzDiQxkS6_0XCl!{+>Z^(EaG&~?YK6XP#7wJ(dwKBF_Q5<un$tg(6e*ag#}kGs6@'
'!Ek7~)llZ(S4eqEl)eaH$*f3vB2V6ZD&;Y#AAl(^)9pFYD4o$x!o9L$cSjVcLm2W-xVjLM5l-ZA<9aiK{>*OR@BgS`rM|eJ<sZ%Q'
'Ia))c3r;nv6I_mtPEqu|E}A<lJj{HlKFaiKR~n}2ZLi7K&f-GG4&EQsbGN!G_6qFl{U$VbJ?>Nr@tjfjnGxu+hOIIUX9YJY#)_>r'
'S?a4A4>4?t;6H*Qgs!Mh(Br6TsS1xN_K7Ky0m&i$85GU%(^@<S%iq+Ag*KFk#!Z1l9GXm3#=2^!3&DA8sDi(@la5KYI)QyxKeH^*'
'nxIW6C{pC-O#+D*Y0}T@$?HJvddPOOJG8){8$7c~AfYGuo&cjerTe--{Q24ofl0uXkoxquoV+vgDyS_>^B~jYz1qh^cDk_32~+bB'
'%BGQ6don;@*{;LZM4!oqut9v`R&(byhRyZ&W&}34d<R-37mKL;YNPbC=I)FzB0jo$mCYV-Oh*zE%Kv+$J{nhr-V706U|WB3I=l%%'
'#xnLVcdiZq|J!M7+3Yjl6#1I@rRQxbqXs~Vl9~;fszH}i=7<BwjKIl%P`|^(oiLDt2t@ZeF=GfRw_3u5ESRL$)Ortabt-nzPZt|8'
'f_o|3oNAWPCg~F{z=CLiB5(+tUk(0EeFrm`yXaXUVUwhNT-5X<GjT5-0Y)e5r-SRz_}HFOffn-qHi8F$qFOx-QoRc<m5FSoNyOvm'
'F#k_j$byGvR0<Pk3lJdZR|`&3pLbFw4gmc8H8yOFT$D82k|7QfwmsajQG$LTSC5KS*F(lJt0b&b<Ch6k_6Gc92e=YGE$_kzB}#GL'
'_sUf@*sR@_<^n<vXV1zoA(RGGF%shyI#h$=chfk4${-5eyTp9Lf2-i{U#3*SY~P@FOV={}zIt>ld>X!^W8Z(IA$?~oMCB`r_9K#v'
'{BFc?3-bQSBs9<Z%(1_hx{IL(gSr;)2LVRVj_9LWFp*7u0zbBO2m9bZNeNzc#W!?f6CU6)P854hzEbnXDm9~0{awW!lTC;uVw34c'
'k~?A4B%`Fh4eO3T(5p?oLbnp$(pwMLk+|fA#<B9}F+07blShgb){6rJAqNb8Aj{8$j#NyqM(|=id84m7%ibu)vC|d?^<HzJ=kQ3R'
'NouCo{32ovzKb}`s(0x|JIz^ewB)3oRjpcda{&h}^iTEbKx18R_Oaew%gsdDCa8e66*ZW!sUwilR|sE|zVff432_+|P5l>9syj?q'
'0<Hus#6rA<a&g&VJWonK58@yFqZO#&(MiOxT`T=<vb5`UKyA@xRshhxbUO)KP?Xb5flOY0p(hQH1-y-svp5UgXxa)FogxNQUcQ|}'
'pPKV85oRqbm%kgqDz4F-T9%e7<VEH5h5&+sX2x%fEB;Yj9!=_j&diKgEY#a`-SXP4w{102w$<EDl#{=66z38l_Q-Nmh1}r+vp9>J'
'e7DUnRqlrU#-mpyMnfm?54WBmEOL(D)jWfZ+j?)U7$g)Q+<xuCYiO@NNPH!`65<xdKHkJAm62xi=9heN8ewd45nZjW_twg0VRK>Z'
'2ye-UtSr>WgTX|3aJ;?pIbG3<_Rl<ibM8PHiDd-7(gxVs3hK8gP=&vL6U9YnSN(-He?mB0GSZskzvoksH?9P`Md~bzVKM1tMyTAZ'
'8~;3<anV-K&;>IU5g6aUmEu}RGfkw;<E*1w<uHII@<0u!$Z?S{z*@0aZNK8VOR3imZTsHW8}4qm?c`H2mgM^o5lv~3%IpZSF2oiL'
'I~8V^c%eGBtOA3rmX~0R&7%LrsE=83@@qbw+os~lbs#h<e+w=cK{!%Dl#&rQd9_-uoX{p_3BaZ`!=UF3Y||31wy8@va0&~__Lf1)'
'dZ93en4wniIck*nHl&`y;Qybhn$$q%s)k6jz0O}=%n|Xh1&Zv<2EFC+4{mMwyMsk+dBzm;aGO^5$I;mrB?7KHJk27$6Dw!Z`?m}D'
'i?dB<Ze4(_{Pm+C0n_2CDGL+jK83txu>128(AEF1>QqJ=S3Jlj^w2hm5U`yJ?wqv$UW-WOGM{#sr&rW*5ez7Vq-QvEdvcB}2%_H%'
')KW){9n@PD?Y1$A+JMTMgBwrWU?7g=AS$TNjG#(f2q4*t_ygE`5WB+2%N5EjbA;8y0j)xgS`5`Y{otmvcJ#sbU9Il@9_F}P3lG2Q'
'OgY)RB)#IavLN5w9beC`H^`!ZA|6*nDES9v-tqPW$!~6kdVRFfl_#s^<_Y;>D#!>Bb=Nb-xRkW*7@EDYiJ6{LTl2XtZtC(aj{Q2~'
'GNnw=bc5godH}B~xACw-P^l#X7bgf+ix$L-B$($XE?Mhv)t=$hZ=yuT8e^EB5DWVzUv>;SRF;n!?-2*@s8OpC0lE@jCrq+kr={RO'
'xz#hg_N>jey2Tj?6@Ew0<4Q;Wezp}dJ3J&sUi$8oMho{Wdn=MInL5ps-Unn9Q30kQ8xGSj_kVa3(m8-ty@&9)s|*;wCs)m&^ZK4W'
'HB?sBG7tc|?b-NGM=j$B`*w)^61cJzd`2!QBn5ccWo@@i1DaV=WW%=Anac7XVcmB%LW2_o6cS76)y~o_J^6Oo&tyX~Q%%N{j60nC'
'`WgA{G<J#BO|_Ryd>1cDp-B0}xE!#H@YA(Uf`nKqR<Pj1hna&pEniNifcWGg<43X1X<@ID6TVew|AMZ}@}jQymdZGGg$!-h&zjNn'
'CN#ljn2)SB#9GQ?b_nSrVet!I0@xn9=?|Kk@+0p(m-`wip|86<v17f*9i28EuAil7j=3X-9&p@FnRhD18ESg5Ki2)p=^yiMT~3}g'
'Y4fA2Tto;}kZlC|g&+ad)~M<Q0PuM0fQn1g2Z^xdA#`f-ea}bT2GrVZgLA%_gCJdeHJyqm^uXzVJZ5MdC67f8I@tQ!)?}1^jiZwO'
'W4=){wmQm5Zqic;fCjTcsIjCzE&!GwR;5k;WNS<gJ)XlI{d6FKn8|AsX;ToXr=!2$qhzZPbqN)xU0!JoQH6J3)=yfHSI5co;!Q?o'
'5(-fWXOG;~9aww(5YKzpw@aJ~*z+iWu{)uy&-mveRXP@w>Q%g=^tWh>fYNpgj>^}2a9M50j=VKo_jxLqogm)0=iH8x$J5%9Kc0ik'
'ES4^l2?Ikf)hfIywPmgep>7Y2Z^GwPjdOXTqg(p8Bq~O*Z2sOgGbNg;SFO!)V7Hn?`tYqzYB$MLJh)<^9G0(Y#3}cDWhO(;P+HtE'
'u=KikeJOjQ7)y)tAUjx{xU;T*?4xPLQbvILa({)VZNGHZD&TIL;9Hau)T8A{Np?r_f2A5Hu-}S^?Nfr5n9ZD9tgvOi(|J?XeqqIw'
'%?wm$^J2z43>3(5y{4J2d5h+-M$k&dLu7OmGa;M_J^#^2U|2SSs=P23CFA#*dl{kImZWU3(6(ZAKWUii6)e`PESht*3(y4D|Jmli'
'Y83lWh?jK@Co}y0A?~ELMI#s1Lfrj1!CkcpcF%F}G(?K$N|+~3SlSJc3g=Ge-I4?}u7q~twPDHg=!Dcgq4a&xDF+~cIRZNxeZ_J#'
'Ki$>h7;pW!Hy437wgLKHGxTqd#xaGRg2mn|raN(hQ)lksBifA=o+_D-L{G!ZiMq~*VFOfGVB=239%7E+#;SvSwN>{>jtHCYm`Ko!'
'Qjr%R-X7o*a3eTPpPiJnvfI>=wSk-?#cbbidMj7nLvStg?mT@@<@f~~3;~q)1CY}tkRx~kVX7RI^L{m5k_IrvC(2mNEzUJ{dkE~z'
's^H*SYyqo!Kod>7ko{>FZQ%p|a?V_1<3u4Kre9%5_0(z&-Oiqy*^Na}oXb)d4s*7Ta{*yzDWLoKP!Ejrs4LeA^RF8r5!qO$^lYE3'
'69a25c5D9-Xm_gLo-IkFmgEjHp$F+>`47^7>5P|i;|8(UKz<j|AHEF?^^efwvM66`ed}iuDf1l5lTv`@&x6i)N9aCxj$l|on@<q-'
'd4Fp;{vIBPE_TeFnG;4D)MHi#T@RMn?kHQS&HJupT*Y_(AOWZT;GHYJcple5J{s~ElChfR_!z^<falWznpPC95w|GaDIX*;svgaS'
'4$bYcS3z)4+ok>X5e`b-L~BN-g`-to6$fwmr?wl%{f6gGXSp7fGIykcG0o601n_@)0X|xYK2Vf!6?^XXN)4KCP14Dk1JpDRO;h0k'
';wZK~s7JS>9)0bjDD3dP+ygH0x&-4c8!;mtqkknL1eL_IF_o!`6zbSC17Tmz`Bgm?jiqj7a<Hb6O8VowK%DMro`v@IVJosrjg8T('
'UC#DPRNwNz8I^{8lM&BE3tzgWOrfLf!Bw4ocd#2bguu}37RH`jPuC<;MnHf-lT7yYvs2T|oExQR<fPyS#kO_w`xVykHvWcl0fUCr'
'-`h&(eULqkX(R*<&?$)&fZ&;RJ?VY_;KjWC-5Jv!=Cr?0Lz*#&@}<0TkCOX-&$%DA;(m}fq^CW_Pel}uu;#5P#VB^ti>P0xNl_8f'
'SsDNd;cLuzEj)O?d4idbUfd2Gm$|5?n<D+?#Z~wgi~Ju2a<Xdpgiu6=lkKGdZ&n@)Bc;SnGxfAsLekqz{3Xo<7}{-a7el^;%kuGk'
'_>(?k)_aqfO?vO1FBXjCqrKt5OT4aK<xDld{vBY^^@Gsajq#Bb`-~<qWE!^@e$j<?^m1~cpKZl6CI?zO>Omp2!qDi-9k7e|-;un('
'rwW_tK2Gghjh-O&wHCLTBw^@?(`q7?soL}}?U1Zkp#v<MzUE}>&D#JJGHM<0CI;COXnJg@VMSb-^9&i%z66TISY)e@9!bl|=BYZ{'
'8a@QPnIai29|behr-@SBl1q$yPcT1|H>PCvh-JCwpQn+(wPRU1-?N06(7zvUVQF18G;G$&xPUQRw<A798YU62*RoStKr_#VY38`D'
'jKuUP6lJHTO{&_SZ<~JHBAX-z%;r|a;zKk-+v~RG0v-U<SR{{Uvx+H64}6ZDadq%DBRXmLQw-^q;fbko#e2T!{+{p=vKx=&Nkn1h'
'az)YUUmc9RSkBtGiVlMZbt_Lym1$duo#YHb><m!&H1;XtA0#o3;9R%(mmjl>k%;ZNJ^qy&lNByN9Lfj|8$ibN)H2^kw>^yYMD*yy'
'O=x5ks-MOdArTnk63YY7h)kk+Z{4F-t5+>{64)UIiX)q5@?*CErDOJE|593NX|`HSv9M6?GMLM00L}6VNqDe&pFFZ1cRDpO$9se5'
'NIQEVoed{jO+kM-own<%%+dq;13HoZ;82?wlm|k08FkAWcm`QKJvfEDsU{<GpyUHvFeJ<!JSY?P0D32yx=Xr(A@x$H%}{a?2kI?z'
'8YN=S9oA31Du;zJ&Sg(#n;D8g@0&aDeQmii>F#Zm3CiCL?4lY7$Tptl^=t<h?~EfR%E*q<cjOb&RdkB3>obzFQ4Puwf)R&!v|Xr5'
'XbbuG2zy+tqbtef^}l~o>r#4|xp|*|>nPI;#Cy*oP;71)U1Q_mW6OO_e2+4KFf^zl<x3*|t{yWrFqk{aJB{Q>nW(l~hTAp7WN6d>'
'r}sdRu4hTa3yj-aRCi2LO#r^YOoGkjC<+caEZc5J@S36yD45{goSxT$eWh?a=m};ORw)w`LDP(~$l@RuU_IyYz7=veWzB>D2Ax|*'
'>iRD(7o$lgtUMS7k~2mxGIBfOGY(V4RFg*YHPK=?H@ROeb72_B+wsQK`?6pRwpPPlX+yc*1VVO2>uu!c+Y~<-Hv>pJQsO@6#TuG3'
'K3hXZA-%t6QzJJY4@#e_g^;{<oj>#_%JM*;h|=wTQD~d6WB)cy4azP=3d(M*#7JbL!Iz9_PaGIpaFo2s7&TQ}l3?<;kucNsg+eT3'
'=aWC)4L>6eG4WKoOK9WogxHpLq_d_9JtlKA$5h)p1Rpk0OLRtl<tp7l_i+gKCC5nquFcG^F@N5tPpxc;?M&rez1Nl6b9RxBCkaa@'
'fg`7Iz40y=eE$2ARnhe=Tnu5XxKeE*@qO?v112aF+7f+I&htx`Z61O!{;6K-W|Fx%;R>he|M)O`LeMUEa+dSTV^4Ax(^7wrn|F89'
'hPf@ntgK?=+QRN;LCmA;e9y(;#=$O`YlQuNBlY?)V>eFPzo@Hmszq|H;euOg>3v*7R>qxhK?169be+W&zjGfSghjqXW>R4j+cco6'
'EerY2@K8QoMan5&7{tyI;d6S>)T5;h;)nOGekZC+*rKAw;CNUsWFN{bzWd*J-iaRNWtV!$PBcH5=$A}&OXb2n%d-ZPuz$VabzsWN'
'=Io(_iC@<LI&ia(BN{O0d^O|~sTH#<RC3Q*ZAJ}7y?&%(aGXx+FAx0dM6wgqCN02iK<mL|n=z?FSL1Z*l4SxX5|Mr8b%$&@AY88U'
'dA($o91k<5xXtggBr%aMPd<Xt0z2d)@;qBSNPHJ)Y#5p9#&bEiR}p7ux}Ec02x(0`v2uO^qKea%S#v%g_p$$>(+(CkC`*_cMGVW{'
'@=xZYDUTNr4X^TK+AWG`-^67+C(_Bjfch;M#I&M4u(!Nbrc|b(Aq_ju-rTVS+AhiKbPovV_G%1hLla7VUJ^9tZ`oyEca^*e)Hz5p'
'BRYH;cwbPrABy>r+ySPV0@&Ho0=y=C;$lG1JrgRkKSSOuEh=yT6R@^1nW<P(u**NxR{Y*g022kgsS;9}6^n&ZJX==ZI-ARzDS+z*'
'(=l^)b9r#gydpC;<@}fYQ)9Ts5{_}ZnsA0!!w>MBBs@7DbU=P5rZ#g9uo4Vc2C@XJKAQsF?g3@=As74eIOdw;$+R=rKv(-r7GGvQ'
'0b6u9jzI26igz3tAL)PYMIP}MlX_%uhP`zUk{|iYQwT7WOixd8fTX2r2v~JOe2UTKe|}rvbNpgGUGR}?-fF?KDXQI#21snN0HlHM'
'K80_eF^P8z=KWA!mjnBA`~I|))U(_exYHN4>|}Dn`^@)Z#Cm!ZgqC-DvbIMW2!w!Tz=Z40NT%m&$k46dQOMpre|gKG;(!}JWJe&P'
'n^Ut=cOlMee3k4V^$g5|kGCY;RU|jY1<VG9=72adP@e|olllZ7bBQU-9CezN%!k2YK?ar+SId&?-g)U|3Ke0+eIs0!kvM+<T;?VS'
'e6u=7mqYcw)qd4pK^eU$Cg)eR3_icS+EC;EKYH+ko}eJ=ig>i-=Xi6tWUmtp)tM*7S6_8%0(ps*vk;Hx8BOL(&rnT}B77DAOP!aY'
')$`O&8wYwTaW?tp;l=6@H0t}AIHdHcil&N>*y(Q$OB;{0;XO?F_jhUA`;yqa1Ea|4J%s=oc3^u|J5ZD{9yy3%IR&rNn>C0WCO$N?'
'*MkEs(C>iaDD7db+}p$I@@~E6e&ydTK~rQkFu*{-T?6vs8wdL>j4aKu9O@pBrY6H6`tTlj%ba~}A!M9JIV_B4yp<J2oHF@x7~`+Y'
'K7FFCtF5phOA?dbIkRfNb`enIa2&xG$SjS(twHHL7tAVu$xfR_Uhqx3^;rcarh-bVOspfBFA#hoFR&_eUayWLtEMzDWI*{efF*&1'
'mYfr!AMxnWR;P#B|3&kSh)03jy`GopBK(-#{AYch)VcU#OUgctY5#|Ici(Uh$F7gUBA1&m=mzhrhbGHXSui<{MgFEB{$uaC-15XQ'
'I<M<abSPO#745*Vr?-ZZ2h{l^9gj-YG)gS97h(4hlqLnRrF6S8vw7|Y6YmbO1`Cz_*|rWJex3g<-mHWHn29U#CmE7nR*&cH8^R3$'
'<f?sKtYtYHDA7H@36lTV4zc^3=;;6@jHmH-DsBx6(UNV({4)9}&g6uxu}tRz{VvQ@KD2oh=tz>#!rxp){PU+0ELVm~Doy+K;Ok|$'
'xhK(8XnsgRCN7!ptD5Kc?bNV5@6=?q5pv+V-2y=0Lvigwy@4=;?s;pt`4<nB2Cba)48PjA$UnTHq{w8+dME<aZntKOU?@`3dWRpJ'
'_G%hssCLqAb7j+WafxUdoq&nlJX#1~Dl>^>PERE-5c6&w<jsi$Tz^N0G})dCZOK`nO(>dyr~oHOF#BJ`CLhe@S%EVClLpNfqP*i7'
'Av*dmk?5Iz|8?+p5b5P1+Id2yb+3aKd%=mieg3O(O1|^--G*gDHKW5UUCkJBtkvMG$q|d>k_gU81QP*q|Bs>JBTKQfvE~&GkE_(f'
'{{{d&64YRt$z5AI9(|%s{8pef(?)V|@?bf;4dK+HS|66p;9)3<pY?$e$pb(yOp{Kh-LQo~7F)Njwz&O2TD<(zzsw8q1wc2$`ci3E'
'lV6+tU%x-LFXhuIp7>V-<F5h;*?T95!q*(6q$tg`SyIHp`*pX*L?Jr6ga%msI89au7uGw=D%N8Es(kdey?>B%QK>2wF+9EN`wAQf'
'>G>d@FlV=KXLx@iClbr!=QLnacsm+8jGqVmklO>Dc?}H+C|qjS2Ps2B&TBIw>Y;H{(8w`T5QcUszTce^+Abad>_zOmUyi>p=<z{i'
'>x2vD9&K1GyYxA25ie9E47WX+PhHGXS8;<DBU$NcKomwQ;N~Fdm1iZRfwFogCwN_L@4ZcSVzt|CSjMaQ67A=@(yjg2Ww3%4o*XJV'
'q;sYKQL?^cUPgE7;o~5nW6p5+ZZxa41yYFR9-GcK!ZN#87H@q}{NU+>gfrBM9^HFz^>ad1+nlhIFE~#5#B4dhs`xbdE^P!v;THb='
'`jf=H#T&eXvi4j`?9lk)QE4q$Yc+nM?hp>CqVm9yl$wU*28sdP#v3RR6&l6t`_BLjy=O%1$9nK%dsQcabwl3ga`<;*?a)2dT|&)^'
'dr2`~A8i^Bnl*AW!$Ds%N&j(!O-A0HY#GA;t~7e}#|d9r=-rgXe&H^M-0Zl@h@`aVpDO0r<$`*&k?|QxZzYk`=yu+M#mTAkE`vcz'
')m7bKgL)LrJd_mu=YXyF8=Gy0MAFq^j*WFtoO5qM&+FB<hd!|8S^xk5%p{<K-dR(s00D+svzr0{MOp~*vBYQl0ssI200dcD'
)
raw=lzma.decompress(base64.b85decode(B85))
assert len(raw)==36275 and hashlib.sha256(raw).hexdigest()=='059893836ba9e6857bd0a410cfaad915f9b92c28675d119e67a3a8cdaa4cb067'
data=json.loads(raw)
expected={'VERIFY_ORTHOGONAL_HEIGHT_REDUCTION.py': [9940, 'c17b1bbe95bfab3496c0002cbfc7ac5598daf239b3c96cf39a720a1c9658e8fd'], 'VERIFY_SYMBOLIC_HEIGHT_CELLS.py': [2589, '1432e7cca794d37ad5254ae5c0b689bcb07c6f755b72c330da5ce8f6bc7a1a26'], 'ENUM_C48_WHEEL_HEIGHT_CELLS.py': [1454, '84578a46a125c65e3d0ba37223aee3965819dc701e2f0acf67b583aedb28241c'], 'NOMINATE_ORTHOGONAL_C90.py': [2129, 'c19077071a3710b96912b4a336b626fbaabd2912dd75018701aeae16b4ccb031'], 'scout_orth.py': [2141, 'e7fad0f762b360801576b3c754e6abab7e7984e19dcc793dc171d1bf920bf823'], 'search_orth_torch.py': [4124, 'bda53924d508b68567e32caf4374422c09576e26a36a3b25e4d0d87dffade5fb'], 'search_p_optimal.py': [2709, '7548258ee4f9c4245b6a9210543650eec39d81211284ff376553ee2a8f64ef67'], 'spiral_planar.py': [1087, 'c2d74df9c9fbc25d6b6001ebebf4009664e8a5e10f8c92f7663e37aee2d6ce42'], 'wheel_sdp_base.py': [2287, '0ea6c651ff95fafaf995ff74b95413c9c06d2ab20fbe2aeeb8bd4ef8deba3123'], 'wheel_sdp.py': [2858, 'ca37adfe06c2ae59a1b3f7232c0e63c857dd94d3b8e801afd0b70f17b87d937a'], 'wheel_inside_probe.py': [1110, '26b4a54b34049677560b6b41c45a299a3a75bfbea5f981a4b37e36d681e92df5'], 'probe_mass_freeheight.py': [1359, '9d6ecbbc7c20269d741c6da962e7fded93a6238c68ac708252dd145e89a42bf2'], 'probe_s_geometry.py': [1285, '6596a16465f06572c3f04247b9b90235f4bfadb7d7310bccae71807d8f80a11a']}
assert set(data)==set(expected)
for n,s in data.items():
    b=s.encode()
    assert [len(b),hashlib.sha256(b).hexdigest()]==expected[n]
    (out/n).write_bytes(b)
print('C48_HEIGHT_SOURCE_ONLY_RECOVERY_PASS',len(data))
```

The new durable conclusions are the sharp physical height criterion, the coupled planar reserve gate, the quadratic-event height-atlas theorem, the complete labelled wheel enumeration, the two exact controls and their scoped all-height obstructions, and the nonorthogonal two-disk identities. No finite search failure has been upgraded to an all-octagon exclusion.
