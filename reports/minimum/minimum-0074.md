# minimum-0074

AI research report · 2026-09-16 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# C34_MECHANICAL_BOUNDARY_AND_STRICT_ALTERNATIVE_V1

## Determination

**Unrestricted regularization is neither proved nor refuted.** No actual weak joint C34 body that obstructs it was found. The following new results separate the remaining question into precise physical obligations.

**An isolated degenerate equilibrium can be removed.** Any actual own-centred body with exactly one strict stable facet, one strict unstable vertex, no strict saddle, and at most one additional *geometric location* of degenerate equilibrium admits an arbitrarily small affine regularization to full-feature `(1,1,0)`. The complete maximal-face lattice, true edges and own homogeneous centroid are preserved. The theorem includes vertex–edge, edge–facet, and vertex–facet contacts, including nonsimple vertices.

**All local affine regularizations have a finite exact test.** A linear metric ray has a necessary-and-sufficient five-variable, degree-two lexicographic contact test. More generally, local regularizability anywhere in the full affine orbit is equivalent to existence of a polynomial metric arc of degree at most

\[
L=13074910452538590096000000.
\]

This is an explicit finite higher-order condition, not a first-jet sufficiency assumption. Its coefficient search was not executed; a failed ray test is not a failed affine-orbit test, and a failed affine-orbit test would not exclude non-affine shape changes.

**Strict attainment has a uniform effective alternative on the entire slice.** If any strict homogeneous C34 attainer exists, some attainer with physical radius `R=1` has a complete all-feature certificate and all 68 directed true-edge primitives bounded away from zero by

\[
\boxed{\mu=2^{-2^{175}}}.
\]

The statement is existential about a suitably selected attainer, **not a mechanical gap at every weak body**. Strict attainment is equivalent to nonemptiness of one of explicitly generated basic-closed integer systems with **230 variables, 426 constraints, degree at most four, coefficients bounded by \(2^{19}\)**. The small coefficients include an exact 175-squaring encoding of μ. No positivity was inferred from numerical minimization.

An exact physical C34 control has one edge–facet contact whose decisive shadow is `t²/(1−2t²)` along an actual own-centred affine family. Its first derivative is zero but the contact disappears on both sides. The complete census remains `(S,U,H)=(6,5,9)`, not `(1,1,0)`; it is a diagnostic construction, not a counterexample to the main regularization question.

**No full type or joint root is removed. C≥34 and the accepted 632/52585 register remain unchanged.** The parent explicitly left mechanical zeros unbounded; its positive η concerned geometry and specified positive integration cells.

## Authority and scope

The immutable parent is `minimum-0067`, SHA-256 `2507653be048f3201aff59b4472d22d6c992a622803cb4cbc950b3db0add05ad`. Its complete literal mathematical text and 13392-byte source were read. Authentication uses the literal Markdown with trailing whitespace stripped, compact JSON `{'version':2,'result_markdown':md}`, `ensure_ascii=False`, separators `(',',':')`, and no terminal envelope LF. This gives **48408 bytes** and the advertised SHA. The source has SHA `e85a9b5fb2604aba2ab4b333c0a28c80bf2df3d9a16571694ce6efc452546b4f`.

The current journal is `research-journal(20260916-161111).md`, **4886482 bytes**, SHA `639a79e3e6625f1a470a169f26a2ed39fdbc398515e16cfba550adbc579c1cd7`. No source-identity or incidence conflict was found. The latest quartic actual-moment inverse theorem was read, but is not used to infer regularization: it explicitly controls weights on one already-realized geometry, not mechanics under deformation.

The global alternative inherits the parent's accepted weak-scope `U1⇒V≥10`, `S1⇒F≥9`, and `R/r≤27`, including the explicitly inherited universal285 premise. Those historical certificate families are **not newly re-executed**. The isolated-contact and affine-orbit theorems themselves do not need those lower bounds, a condition-number cutoff, or the numerical value of η.

Define the weak class \(\mathcal W\) to consist of actual full-dimensional convex polytopes with the specified saturated face lattice, constant volume density, own centroid zero, one SPD pair \(M,N=M^{-1}\), and simultaneous rooted weak escape trees on actual primal and polar edges. This means exactly one *strict* unstable vertex and one *strict* stable facet, but permits additional degenerate equilibrium contacts. Strict saddle edges are not silently ruled out by this definition. The inherited saturation argument is valid after label collisions because weak arrows between distinct points strictly increase squared norm; it restores all ten genuine vertices, nine genuine facets and 34 incidences.

Local regularization here means arbitrarily close actual bodies, with their own volume centroid, the same maximal-face lattice, and no equilibria other than the two strict targets. Preserving the full lattice is stronger than preserving its f-vector. Affine regularization is a sufficient but restricted subclass of such deformations.

## 1. Exact full-feature contact predicates

For a true edge \(ab=F_i\cap F_j\), define

\[
P_{ab}=x_a^TM(x_b-x_a),\qquad
Q_{ij}=q_i^TN(q_j-q_i).
\]

The opposite arrows obey

\[
P_{ab}+P_{ba}=-\|x_b-x_a\|_M^2<0,
\quad Q_{ij}+Q_{ji}=-\|q_j-q_i\|_N^2<0.\tag{1}
\]

A vertex is strictly unstable exactly when all its outgoing **true-edge** P's are negative. It is not even a closed equilibrium when at least one is positive. The remaining case, all nonpositive with a zero, is a degenerate vertex contact. The corresponding three-way statement for a maximal facet uses its outgoing Q's. It follows either from its actual normal foot or the tangent cone at its true polar vertex. All nonadjacent inequalities follow from these actual tangent cones; a triangulation diagonal has no mechanical role.

The complete closed edge-equilibrium test is

\[
\boxed{P_{ab},P_{ba},Q_{ij},Q_{ji}\le0.}\tag{2}
\]

For proof, set \(d=x_b-x_a\), \(\ell=d^TMd\), and \(\theta=-P_{ab}/\ell\). The normal foot of the edge line is \(y=x_a+\theta d\); it belongs to the closed segment exactly when the two P inequalities hold. Since \(My\perp d\), write \(My=\alpha q_i+\beta q_j\). With

\[
G=\begin{pmatrix}q_i^TNq_i&q_i^TNq_j\\q_i^TNq_j&q_j^TNq_j\end{pmatrix},
\]

actual incidence gives \(G(\alpha,\beta)^T=(1,1)^T\). The Gram determinant is positive, and

\[
\alpha=-Q_{ji}/\det G,\qquad \beta=-Q_{ij}/\det G.
\]

Thus the two Q inequalities are exactly membership in the complete incident normal cone. All four strict inequalities give a strict saddle. Equality in at least one gives a degenerate contact, possibly at an endpoint and possibly shared by several feature descriptions. If any of the four numbers is positive, the entire closed edge cone is excluded.

Consequently a complete strict `(1,1,0)` certificate consists of negative outgoing arrows at the two roots, one positive outgoing arrow at every other vertex and facet, and one positive member of the four-tuple (2) on **every** true edge. This criterion includes all active contacts without using a complementary matching, Morse counting on a degenerate stratum, or independent primal/polar metrics. An unused primitive may vanish while another strictly positive witness excludes its whole feature; such a zero is not a degenerate equilibrium.

## 2. Necessary-and-sufficient metric-ray and metric-arc tests

Use actual physical coordinates so the initial metric is I. Every trace-free symmetric H gives an actual affine family

\[
P(t)=B(t)P,\qquad B(t)^TB(t)=I+tH.
\]

For sufficiently small t the metric is SPD. Actual tetrahedral volumes all acquire the same factor det B, and their first moments are transported by B. Thus the **ordinary volume centroid stays exactly zero**; no unproved moment correction is required. The pole geometry is \(B^{-T}q_i\), and the two metrics in the original coordinates are exactly \(I+tH\) and its inverse. Trace-free H loses no affine direction: scalar metric changes have no effect on signs and can be removed by positive rescaling and reparameterization.

For a pole arrow multiply by the positive determinant. The exact identity

\[
\operatorname{adj}(I+tH)=I-tH+t^2\operatorname{adj}H\qquad(\operatorname{tr}H=0)
\]

gives, at an initially zero primitive,

\[
P_{ab}(t)=t\,x_a^TH(x_b-x_a),
\]
\[
\det(I+tH)Q_{ij}(t)
=-t\,q_i^TH(q_j-q_i)+t^2q_i^T\operatorname{adj}H(q_j-q_i).\tag{3}
\]

Form an **active clause** for each nonroot vertex or facet with no initially positive escape, and for each edge with no initially positive member of (2). Its members are precisely that feature's initially zero primitives. Strict target root signs are separate guards. An empty clause means a strictly wrong feature, such as a strict saddle, which persists in a neighborhood and cannot be removed locally.

**Ray criterion.** There is a full-feature regularization along the specific ray H if and only if every active clause contains a primitive with a positive first nonzero coefficient in (3). For a primal primitive this is a strict linear inequality. For a pole primitive it is

\[
\ell(H)>0\quad\hbox{or}\quad[\ell(H)=0\ \hbox{and}\ b(H)>0],\tag{4}
\]

with the explicitly displayed linear \(\ell\) and quadratic b. The zero polynomial cannot serve as an exclusion witness. This gives a complete Boolean system of degree at most two in the five independent entries of H. Previously positive exclusion witnesses and strict root signs persist, so sufficiency concerns the entire body, not only the chosen active row. Necessity follows because an initially negative primitive cannot turn positive for all arbitrarily small positive t.

The same assertion holds for any supplied finite polynomial metric arc

\[
M(t)=I+\sum_{k=1}^h t^kH_k,\qquad\operatorname{tr}H_k=0.
\]

Primal coefficients have degree at most h in t and determinant-cleared pole coefficients degree at most2h. Replace (4) by positivity of the first nonzero coefficient. The exact coefficient-convolution algorithm is in the capsule.

This is quantitative. For all selected guards, flip root signs so the desired polynomial is positive, and write its first nonzero coefficient as \(a_k>0\). Put

\[
\rho=\min\left\{1,\frac1{2(1+\sum_k\|H_k\|_{\rm entry,1})},
\frac{a_k}{2(1+\sum_{j>k}|a_j|)}\text{ for every selected guard}\right\}.\tag{5}
\]

Then every \(0<t\le\rho\) gives an SPD metric and all required signs. The finite polynomial tail is at most \(t\sum_{j>k}|a_j|\) after division by \(t^k\). Formula (5), the unchanged lattice, and affine transport of actual moments complete the proof; a first jet is not being substituted for an integrable shape deformation.

### Completeness for the entire local affine orbit

There is also a finite degree ceiling, so arbitrarily high-order affine behavior is not left unspecified. The strict metric set near I is a Boolean sign condition on the68 shadow polynomials and the ball \(4\|H\|_F^2<1\), in five variables, of degree at most two. Basu–Roy's quantitative curve-selection theorem and its Zariski-degree corollary give an entering algebraic curve of degree at most

\[
D_c=4dN^2(N')^2,\quad
N=(2d+6)(2d+5)^{k-1},\quad N'=5(k(2d+4)+2)N.
\]

Here k=5,d=2, so N=65610, N′=13778100 and \(D_c=6537455226269295048000000\). The exact statements were checked on the primary paper's pages3 and12.

Take a primitive real analytic uniformizer on the selected irreducible branch of this curve. A selected strict witness polynomial of degree≤2 is not identically zero on that branch. Its vanishing order is at most2D_c: that order is one nonnegative summand in its local intersection multiplicity with the normalization, and the total curve/hypersurface intersection multiplicity is at most degree(curve) times degree(polynomial), by Bézout. Truncating all five coordinate series through degree2D_c therefore preserves every selected leading sign. The trace constraint is built into the five coordinates; SPD is open at I.

Thus **local affine regularizability is equivalent to existence of a polynomial metric arc of degree h≤L=2D_c**, with the finite coefficient test above. Conversely any such tested arc is already an actual affine regularization by (5). At most5L real coefficient variables suffice; testing a primitive requires at most2L coefficients, each polynomial of degree≤2 in those unknowns. The displayed L and5L=65374552262692950480000000 are computed exactly in the source. The enormous coefficient system is not materialized or solved. This theorem is an exact affine-orbit criterion, not a claim that every weak body satisfies it or that all shape deformations are affine.

## 3. Complete isolated-contact regularization theorem

Let P be any actual own-centred polytope with one strict stable facet and one strict unstable vertex, no strict saddle, and at most one additional geometric equilibrium location. Then P is regularizable by a **linear** metric ray, preserving its entire face lattice and its own volume centering.

To prove completeness of the contact cases, let A be the smallest face containing a contact y and G the face exposed by its radial normal. At equilibrium A⊆G. A strict equilibrium has A=G. Otherwise the dimension pair is exactly(0,1),(1,2), or(0,2). There are no other cases on a genuine three-polytope.

For a vertex–edge contact, let a=y and let u=b−a be the direction of the exposed edge. Then a·u=0. Choose

\[
H=(au^T+ua^T)/\|a\|^2.
\]

It is trace-free, Ha=u, and the formerly zero primal escape has derivative ||u||²>0. This excludes both the vertex contact and its closed edge cone.

For an edge–facet contact, let q_i be the facet's radial normal and q_j the neighboring pole across the contact edge. Put v=q_j−q_i; then q_i·v=0. Choose

\[
H=-(q_iv^T+vq_i^T)/\|q_i\|^2.
\]

The formerly zero pole escape has derivative ||v||²>0. This excludes the facet and its closed edge cone.

For a vertex–facet contact, let a=y, so q_i=a/||a||², and let u₁,u₂ be the two actual boundary-edge directions of that polygon at a. Set w=u₁+u₂ and

\[
H=(aw^T+wa^T)/\|a\|^2.
\]

Since a·w=0, Ha=w and tr H=0. At least one w·u_k is positive because their sum is ||w||²>0. Across either of these boundary edges, the other actual facet normal q_j has q_j·w<0: it vanishes on that edge direction and is strictly negative on the other direction. Hence both corresponding pole escapes have derivative −q_j·w/||a||²>0. This removes the vertex, the facet and both closed edge descriptions of the same contact. Additional facets at a nonsimple vertex create no omitted active edge: q_i is an extreme ray of the full normal cone and cannot be a positive combination of normals of an edge not lying in F_i.

Every other wrong feature already has a positive exclusion witness, and both targets have strict negative guards. These persist. Apply (5) to obtain the whole interval of actual regularizations. No new vertices, facets, nonuniform density, or fixed artificial centre is introduced.

Accordingly, any genuinely nonregularizable member of the weak target class must either have a strict saddle or have at least **two distinct degenerate equilibrium locations**. Several zero feature labels at one vertex–facet location do not count as several locations. No actual weak joint example of either obstruction has been produced here.

## 4. Exact actual C34 second-order control

Use the following literal parent data; the new construction gets no new catalogue identity:

```python
FS=[[0,1,3],[0,2,5,4,1],[0,3,6,2],[1,4,8,9,7,3],
    [2,6,8,5],[3,7,6],[4,5,8],[6,7,9],[6,9,8]]
RAW_N=[[-1,-1,0],[-1,-2,6],[0,-1,-3],[-2,2,3],[1,-2,6],
       [1,-1,0],[0,0,-1],[-1,2,2],[2,2,3],[1,2,2]]
RAW_D=[8,22,5,14,22,8,2,10,14,10]
```

Let raw vertex a be RAW_N[a]/RAW_D[a]. Its actual volume is19903/677600 and centroid

\[
g=(0,-662559/245204960,-1515121/61301240).
\]

Set x_a=raw_a−g and reconstruct each pole q_i from the first three vertices of its listed facet. Put d=x₁−x₀, m=(x₀+x₁)/2,

\[
w_0=d-\frac{d\cdot m}{m\cdot m}m,\quad
w=\frac{2w_0}{w_0\cdot d}+\frac17(q_1-q_0),\qquad
A=\begin{pmatrix}q_0^T\\(q_1-q_0)^T\\w^T\end{pmatrix}.
\]

Take the actual rational body Y=conv{Ax_a}. The source re-enumerates its complete hull and all maximal polygons, recomputes its own centroid, and checks all ten actual vertex-apex integrations. It gives det A>0, centroid0 and volume543400816160384/55041286768905. Its poles are p_i=A⁻ᵀq_i and

\[
y_0=(1,0,-1),\ y_1=(1,0,1),\ p_0=(1,0,0),\ p_1=(1,1,0).
\]

Use

\[
M(t)=\begin{pmatrix}1&0&t\\0&1&t\\t&t&1\end{pmatrix},\quad
N(t)=\frac1{1-2t^2}
\begin{pmatrix}1-t^2&t^2&-t\\t^2&1-t^2&-t\\-t&-t&1\end{pmatrix}.
\]

This is one exact reciprocal pair. Equivalently, use the Euclidean actual body B(t)Y with

\[
B(t)=\begin{pmatrix}1&0&t\\0&1&t\\0&0&\sqrt{1-2t^2}\end{pmatrix}.
\]

Its determinant masses scale by √(1−2t²), and its actual centroid remains zero. At t=0 the only zero among all68 directed true-edge primitives is Q₀₁. The only extra degenerate equilibrium is the foot(1,0,0) of facet0 in the relative interior of true edge01. Exactly

\[
Q_{01}(t)=\frac{t^2}{1-2t^2},\quad Q_{10}(t)=\frac{-1}{1-2t^2},
\quad P_{01}(t)=2(t-1),\quad P_{10}(t)=-2(t+1).
\]

For every0<|t|≤1/10000 this contact disappears. For each of the other67 exact polynomials a₀+a₁t+a₂t², the source proves

\[
|a_1|/10000+|a_2|/10^8<|a_0|,
\]

so no other sign changes anywhere in the closed interval. The complete persistent census is

```text
U = [2,5,7,8,9]
S = [1,2,3,4,7,8]
H = [[0,3],[1,3],[2,5],[3,6],[5,8],[6,8],[6,9],[7,9],[8,9]]
```

At zero, degenerate facets=[0], closed-zero edges=[[0,1]], degenerate vertices=[]. Away from zero all these degenerate lists are empty. Both geometries' twenty apex-fan volume/centroid checks, all68 rational primitive identities and both exact reciprocal matrices are reconstructed. This verifies why a specific tangent ray cannot be rejected from its zero first derivative alone. It does not assert that no different first-order direction works, and this multi-equilibrium body is **not** in the weak S1/U1 class. The full-feature target test correctly rejects it as a local110 regularization candidate because its other strict equilibria persist.

## 5. Entire-slice effective strict-attainer alternative

Retain the parent's physical coordinates and normalization. Absorb a starting reciprocal SPD pair into an actual affine image, set the unique unstable root x_r=(0,0,1), and rotate so one other selected vertex has second coordinate zero. There are53 free x/q coordinates. These are physical orthonormal coordinates, not a new independent metric relaxation.

For any literal V10/E17/F9 face lattice and any two true-edge rooted trees, use the parent's34 incidence equations,3 actual first-moment equations, and closed geometry inequalities:

\[
1-q_i\cdot x_a\ge0\ (a\notin F_i),\quad
\|x_a\|^2\le1\ (a\ne r),\quad \|q_i\|^2\le729,
\]
\[
\Delta_\tau=\det(x_a,x_b,x_c)\ge0\ (16\text{ facet-fan triangles}),
\quad4096D-1\ge0,\quad
\sum_\tau\Delta_\tau(x_a+x_b+x_c)=0.
\]

These are one actual determinant/moment family. The inherited closed saturation proof restores the genuine body even at initially allowed geometric degeneracies: the oriented boundary cycle covers its convex hull with constant positive multiplicity; actual centering follows, weak trees descend, universal V10/F9 prevents lost labels, and34 incidences prevent new contacts. No altered facet lattice or fake positive weights can satisfy the closed model.

Add a variable0≤τ≤1. Require each of the17 selected tree escapes≥τ; every outgoing root shadow≤−τ; and, for each true edge, one selected member of its four-tuple(2)≥τ. All four choices are allowed independently; no complementary-tree restriction is imposed. Root degrees total at most17: a vertex misses a facet, and a facet misses a vertex. There are at most181 constraints, including37 equations; pad with zero polynomials to exactly181. The set is compact, and every point with τ>0 is a complete strict attainer by Section1.

The τ=0 projection is **not asserted to equal the original weak class**: for example the extra edge guards already exclude strict saddles. Nor is that projection asserted to be the closure of τ>0. Boundary-only components remain a genuine unresolved possibility.

To certify a witness without any zero raw primitive, add all68 inequalities \(p_e^2\ge\tau\). This gives54 variables and249 constraints, still of degree≤4. Any existing full-feature strict body can be moved infinitesimally within its already-open affine chamber to avoid all68 zero sets: each primal linear form in M is nonzero, and each pole form is nonzero in N=M⁻¹. Their restrictions to the trace-normalized SPD domain cannot be identically zero, since scaling recovers the whole SPD cone. A finite union of proper polynomial zero sets has empty interior. **This argument applies only after a strict all-feature chamber exists; it is not a regularization argument at a weak point.**

For these integer systems, coefficient absolute values are bounded by \(H=2^{19}\). Indeed a determinant has polynomial coefficient ℓ¹ norm≤6; a moment coordinate≤16·6·3=288; the volume constraint≤4096·16·6+1=393217. New squared shadow constraints have much smaller coefficient sums. Constant coordinate substitutions do not enlarge these bounds.

If a connected component contains τ>0, apply Jeronimo–Perrucci–Tsigaridas Theorem1 to g=−τ at its minimum. Its exact nonzero-minimum lower bound is

\[
(2^{4-n/2}\widetilde H d^n)^{-n2^nd^n},\qquad
\widetilde H=\max(H,2n+2m).
\]

The author-hosted primary version and its printed page2 were checked; the theorem requires no nonsingular active-set assumption.

Here n=54,m=249,d=4,\(\widetilde H=2^{19}\), so the base is2¹⁰⁴ and the positive optimum satisfies

\[
\max\tau\ge2^{-B},\quad
B=5616\,2^{162}=351\,2^{166}
=32831172781001403154527576082138581753550868645412864<2^{175}.
\]

Therefore some attainer has \(\tau\ge\mu=2^{-(2^{175})}\). All its selected sign witnesses are at least μ; all68 absolute primitives are at least √μ≥μ. This is a consequence of a **positive maximum**, not an assumed positive minimum across the weak class. The positive optimum has algebraic degree at most2¹⁶¹; this statement concerns the optimum value, not the degrees of every witness coordinate.

No enormous integer coefficient is needed to encode μ. Introduce176 variables z₀,…,z₁₇₅ and relations

\[
2z_0-1=0,\quad z_{k+1}-z_k^2=0\ (0\le k<175),\quad\tau-z_{175}\ge0.
\]

The resulting exact count is230 variables and426 constraints, degree≤4, coefficient bound2¹⁹. All z's are uniquely determined positive numbers. These new closed systems are nonempty **if and only if** a strict attainer exists in at least one original face/tree/witness branch. No nonemptiness decision is claimed.

For a catalogue-independent finite exhaustion recipe, enumerate ordered nine-tuples of simple cycles of lengths3 through9 on labels0 through9, with total length34; retain only tuples passing the source's `topo` checker. For each tuple enumerate every root and every choice of a neighboring parent at each nonroot, retaining only arrays passing `tree`; do this separately on the primal and dual graphs. Finally enumerate all17-entry arrays in `{0,1,2,3}`. Apply `build` to every resulting input. Duplicate relabelings may be kept. This is an overcomplete finite cover of every true face lattice and every strict certificate, with the same230/426 bound; no inherited catalogue bytes or unobserved canonical alias are needed. This exhaustive generation was not executed.

The computed decimal exponent of the conservative clearance is

```text
2^175 = 47890485652059026823698344598447161988085597568237568.
```

The full denominator2^(2^175) is not materialized. Its compact exact definition and the whole finite integer circuit are recovered by the source.

## 6. What was tried, and the remaining mathematical barrier

The normal-cone analysis was pursued before any perturbation claim. It showed that positive tree arrows alone must not be confused with an all-feature exclusion certificate on a zero stratum, and yielded the explicit four-primitive edge predicate. Exact reciprocal-metric expansion then gave an integrable affine test, the isolated-contact construction, and the rational second-order control. Quantitative curve selection bounds the entire affine-orbit local question, while the actual closed mass model permits a separate effective *existential* mechanical-clearance theorem over all realizations.

Neither a universal feasible contact direction nor an actual jointly weak counterexample was obtained. No density assertion for the strict set in the weak set is proved. Multiple distinct active contacts may impose coupled incompatibilities; an affine failure would still leave non-affine incidence-preserving shape changes. The full higher-order coefficient test was not searched to its enormous degree ceiling. No CAD, optimization, or negative sampling result is presented as an impossibility theorem.

The next decisive input would be an exact actual weak point with its complete contact census. Its singleton-contact case is now resolved outright, its affine germ has a finite necessary-and-sufficient condition, and any eventual global strict existence has a fixed positive-clearance witness alternative. The untouched problem is to prove that every remaining multiple-contact weak germ reaches such a strict chamber, or to produce and obstruct an actual counterexample. C34 attainment and C≥36 both remain unresolved.

## 7. Complete recovery and observed verification

The new source is self-contained; it contains all literal vertex/facet inputs, sparse-polynomial helpers, topology checks, exact actual integrations, full cone census, arbitrary finite metric-arc verifier, the54-variable models and175-squaring circuit. It requires no old local path or historical source download. The optional authentication mode checks the exact current journal and parent; the default recovery needs neither attachment.

Environment: **CPython3.13.5, standard library only, assertions enabled**, no randomness, floating-point optimization, nondefault solver tolerance, or external package. Save the capsule below as `recover_boundary.py` and run:

```text
python -S recover_boundary.py NEW_EMPTY_DIRECTORY
```

For a different literal branch, run recovered `mechanical_boundary.py branch.json`; the input keys are `facets`, `vertex_parent`, `facet_parent`, and `edge_choice`. Roots are `null`. For each lexicographically sorted true edge(a,b), its adjacent facets are i<j, and the four choices0,1,2,3 select P_ab,P_ba,Q_ij,Q_ji. All choices are supported. The default uses a primal BFS tree and its dual cotree merely as a complete **schema input**, not as an asserted physical realization or a restriction on the theorem.

The360 schema controls are90 BFS root pairs times four uniform edge-choice patterns; they are not an enumeration of all4¹⁷ choices or all catalogue types. Their full generated stream SHA is `31a4a4b9d8743cf9a9617682948538ff5da906b3a3271f4ada3638b7fd20d27c`. The observed default polynomial maxima are degree4, coefficient4096, ℓ¹ norm253953, below the universally proved bounds. All three model counts were checked. The actual control was independently integrated from each of its ten vertex apices before and after the rational affine map; every one of its68 true-edge shadows was compared with the determinant-cleared polynomial at0 and±1/10000. Exact coefficient inequalities certify the whole interval.

| Object | Bytes | SHA-256 |
|---|---:|---|
|mechanical_boundary.py|21459|fcf7f75b9ad42d7f246cf52f1ee71591b0877816182de0d415a7b616a6006711|
|strict_core.json|27835|5a08ebd31ee81ca4cb9a8bb7af4b10214920c588765a3c8012bab96d4103c597|
|strict_generic.json|53037|e100ccfc35458429a5f545ee1e78e537c5a18636273073ee95bf5220e2b17dfb|
|strict_integer.json|63635|35139841353a2e657edbdf9027dd4603220b51069ef04c3d836c1377716cb810|
|strict_alternative_bound.json|1220|e33c87b7904df8b9089e96ad25fa269de2a116a29086cda5a17fa7695dc2e467|
|quadratic_actual_control.json|44251|9178738e9d675e62e6e0d256093d0e494fcc8a311e17331d09b00a28922416aa|
|strict_schema_audit.json|312|ad1aa4f089351da6f86c02aee2cd4dfac6d616af5311082ddeeb03efb3a86371|

The source was cold-replayed and all six JSON files matched byte-for-byte. The recovered source asserts every output pin. Observed markers:

```text
PARENT_AND_COMPLETE_SOURCE_AUTHENTICATED 48408 13392
ACTUAL_C34_QUADRATIC_ZERO_CONTACT_CONTROL_PASS 68 67 3
C34_54_VARIABLE_FULL_FEATURE_STRICT_ALTERNATIVE_PASS 181 249 230 426
MECHANICAL_BOUNDARY_AND_STRICT_ALTERNATIVE_RECOVERY_PASS
COLD_BYTE_PARITY_PASS
```

The arithmetic does not purport to reprove the inherited saturation theorem, quantitative curve selection, Bézout, or the published minimum theorem. Their mathematical use and scope are proved above. The code establishes the advertised exact constructions, polynomial identities, parameter arithmetic, census, degree/coefficient checks and reconstruction pins.

The literal recovery wrapper is **10917 bytes**, SHA-256 `21cf611f655be8cf39fb90e157553919ffbc8afc687b7b4b339b5a45f770a5ac`. It contains the complete21459-byte source as an XZ stream of7732 bytes, SHA-256 `69f26fd36a97a1aa91788a49cb0adca2960e2d45f678e2deceef234e0c455de6`; its base85 text has9665 characters, SHA-256 `7cf833b4a51e618ffd7ac7609a17645106ea4da9b534e8a37460e0c97a3aeccd`. A second clean run through this decoder reproduced all six pins and ended with `BOUNDARY_COMPLETE_LITERAL_CAPSULE_PASS` and the source pin.

```python
"""Complete mechanical-boundary recovery. CPython3.13.5, stdlib, assertions.
Usage: python -S recover_boundary.py NEW_EMPTY_DIRECTORY
All actual inputs, verifiers and integer generators are embedded. No network.
"""
from pathlib import Path
import base64,hashlib,lzma,subprocess,sys
assert __debug__
assert len(sys.argv)<=2
SOURCE_PIN=[21459, 'fcf7f75b9ad42d7f246cf52f1ee71591b0877816182de0d415a7b616a6006711']
XZ_PIN=[7732, '69f26fd36a97a1aa91788a49cb0adca2960e2d45f678e2deceef234e0c455de6']
DATA=r"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;8W5a^j!cEXbi?<Lm`Fv)ajRVAiqqPrJ7guC)|$a3qmx1VD&0K7%^X|>F_f;39hbKZ>S4e
en8M7`{oe<W6*ZvtH$Ay#fs)vv~WVy1h(H7g8&x;)l7NGS1S`}w7}4g&Vs{NtH0?PQxC9ENfv@->-YZYP)y3)A<%NzwxT(eJL!04
?`XRC4%8%j?1&P7jhM`jNay2(Biw-Nm+etl78eVd!rYmx{}j!<+9=Q;S48bt*ODC5z~lf9Xycnam)P(J(<4yHELxrtN*U3lJRV^A
y^r0`F(7lPu6wvuA#hwZcf0i8$h-+nRxh?OLdvlF+q#6+bLFmb8@2Ll<WJRbygnlF@;^pOPc`ak%zPt!mu5PUZuD9nwAnQ^WlgdO
(V8kPz~|%%Q!eAG7n}bl^)<c~!VAE7$|JJ{jkX)l28chdfov-M5Y6x^-qqTEn79Wf_%BGS5BxK^LJPa4y(r0ePW0vR!R}Y%JclOl
`O-H@3i`X`cGT-o0491T{_1GokOv?>3GI5BB`z)@kdp!dMv!Rgf`inUfY8l~3<Wm!@qOG;9!@nfI*0Pm@#E6}nTmbBxSFmph^mki
DHYKEvq}ekafWAJeE&D|eMTl|BwP^vZmzLo|9<R#a9?<CsN1^()7JVwA;^g?eaka+ny@d6<C@Ceb{2#saW5j+idGzXX;T4R)1gu(
nL6g8rfMeGXkY^5`oD$?O+9jTLH*VX*onxc6J`$g0Z;neu;m1E0sz*c83o{0>j0!?3^i84DSk8X>@5dk+_SgVd1tt)HP-e*l-e1~
RftQ8k>-^LB#U;EkatNbmz?H=>z-dB(wwMA!EVg0AojS9cH&UHSK#DHf-5Vru7YkF?-dR>okiq_1IXzoPX9*PCiit9Wd`FVL-&Ix
Y&BR|5eM6PTznuIS}&!FZaPm+{r?hrh*P>iIM%c>b&~~c%1>j6&eG2jeWc$yF|hO48*dUfpA=%6yt)D?Iz>lhLESbXIEbU#-67a=
%Zc1_>%1+h?&i^K=OwO3!Ot;UE%Us*Mq;Ne1;=G$aVPy@v^_0Kq#1TN1EPG8Auwfqv4&8O=1q|fyUD_041=Yps6f~Ol$#ppSFfc+
*SH4%pc4pOCczB9alnZXkJQ%<2qE3ZL9D-ca3<W7FXjA3Kt{bK!&I{j^3kYJ@;n^SzI$BHO?>7;w1HOf$innj4Jzmt%xi3R5$|~C
qu@c8gM%!6LP2EU+fvi!(goz2p~YNZ?{hr3T{(}9F|M8I9sTyQz}yrH+=2rJm7``4g!c;}GoIKma_o3*uRVV$Qh^U;TWkm0Vtgw$
IX+k0fW#v5#hVs7suF=}1G2*>(BBq)c{=#P8x()e)2l0sD1!Ji-vf8JOJSQYSHxf9=J`GNSW#nH@%O?ujLbMHtP(eaC_*Kzu{44@
$uwW9ARLYcMDaVmJS>SC#_V`nvcS?^szv;F9byPGIYzzFa0*~5>5*-<EIY2VK+$Lc5fHRLN4Zp-0*(Zl=_%TrXtw`jRR{3G#3d|?
b<^*nT=^YbpqjRs4F-A=OniCD!B)jY=Nmz_dhCaew8;he^OYhWoJIgkP=I0{@IwR^bm|=_Q|Je8hmtBT9=Z4)IAl|Ki8?Wr3tTOn
#m#VaY^%uiP@(rw5XCjbnDO;6yp*{Jm_TL|1YdHz&=VyU!kDG55a~LM|2VZt8^qn}2!*xhvf2=%`w$ZIGxxs{?;~2#)D)RADgRIp
E}tF7Xw3m`DA%IY2m3UL;TG9MpEB0^EU$z~a9YQ)(p?J7E@J9@sgxJ8d!Ho?+rej0qDTZDt??HcFPAST!4HNa9$NU+>w}h@Lo4dQ
QEVlU-NN(NRO}MA5i?pgTb>`gw^<;3G7)-+79}!n_sN1!lnAb1N3uFqk%m7BVMScs%9i0jToMITQuY_oYRJQKB)lwst<jc^k-vL`
Gf<=CvM%ajHp<TM?2&CBb>f>u7{e|+zKu)06t=o^V<&m0gdw+E32Ctx<mB#tHn9HU#I9&3GF-rgv>lG%s)8;SZ?T{+{c!}#W#zVn
`DGnEwFWs&pj(^z#5_sE-4^?)aeSq$EXmyNO_hE$ptL4MueMTJo~kNQ?I<|}8QRs=hEZ8C*tEJRQA(?qp#&~uNKD{=;K*CXf?RAe
3xoeitCi7Jb9O`UL8tL8;3!O2!_-Kce93xG{?Tp6YQYR%h@b|ArrLI<R_RyPLnt0HIO1876#aRm5S0(}{cK1ws!KYsrA?&9pJx~1
>pI%lB7_`@7FeVnK$=qPqrDnR5AOr*XNBiNP*q7HT?CcPwh^xoyJrDeDMDl^ZbeF?fsXM*wzZ;pOR@^SoEsZZ#!ehttiF@n=!+7&
^Bj|Cm4<)O-A*eO9A3VtFCj{c-Ks)K^e`H!@vTWAOh^aN0MiSzQSyI#tL{`EiQpEvPlvf6%A`624&p-|nn9b6y`Y(l6;VZ>+n%xV
w)jv%U2%^hPfCY)(4U_qkg5fiGBIr+8di&LgJ)O<!djHf&EoTBicMz6nxKsK7Yc@lL#&pl#;@ajE2{nXNMmyEQxT;A_M}!?lv{uU
>=%O2Irgx5dA`o6#G@oSn)qdfY6X6({JRefabs*7nG7A&IZ!LF@Tn)$CEWn<%3>J>3pZg8^C7XbZV5s2#2%Jl0#i*tP8RL;1M;ID
F0ZYhNtlTLv`pq~$^XX!_l?#jdODK$pvW6a<zq>Xr-Otx1d%t!^5s|2G!;byQK&^bzT}z1?-y?wnytOk$KiD&u<4qa8R2tnR(T^b
I-5%{sV#@DUy^58V=m43&<_+=>V<agxBa24`+gubzjtce;22g`Di{?@jBIj*xX_jcF{!a}B@%+ZOlbfYN?b7sC>A;~3_=p8CFRCO
o6e#~#}HS6)@(CGx@UxqA3?bH4a$^ydWCve9=%P}I}~ltXbQrO)AubkdWl(&Ad>uvI$gyya%_Ohx$Zep6}APD4Bx};EmO^nyaHa;
tF7#J9=Y=+57bVDBE0vicst0%SGk@qSOrDeVq;UR$H3<K58ISNEc%+gYm!cTuE3cIyqa7nsY5W6fAu>mpS@zPqi^%i=n-c~E`n?0
iDCN9m6ggu)Z!ySKJ6ykqmOw1F1QM^M9y>5X`pPpvC9uD-z>YcR1OJbPtuqzPs?AsnbCn=+<xcPz9fLNfFD-C=w^IEp^x+3CJW+v
Se_t9+w!9}3wGDrJMIq<MF9fV8%_z4)uw{-n#eX%>)xH@`Ib>l*AU*~UWfq62}t92^b94M7%W?{en(xucs^q{iRwCQ#lWQ)ob_lt
Ld9>;SSY?8lVle1fI$~A^vvvsL49fT3UR`JfBU{3o$jJ3KsxT7&^hiYLTM=kb`2VZaA{Gk13s(%wNN&L^R_mD5QjNanF%pKrC^ij
`AiD>jR_!!Iag759hiJ%9fG#im^~k5jcLf~&OOl;%np&1(%}IGf@>qhomrqA@toIo6u!hWHR&m|nZYIFqwj&pVlbch7Fo`Pe&hz}
eeU!zA=uky(K<vo-4oJu4KC|YUGBW{Y+6V4w`=Syp>yyY_G#{^_E<_s!F%dG<1@1^X134)0%)Q)Rx3*EHQ7KASlJL|g#<3F3@Yw&
FRMurrx9zM%A&xD#l+V}i#mQ0DHC6ye5fzxv76ih`#0GbJ5&~xF%W6e+gOJE`&13fae}FCKQbZ9N|yrJ`T>q-<Sl7IhM4LV)2%Hf
p(*MMC{AP4xKH3RPAT7=SJ(yomw)%O9ybP3sP0;0g%};msWv*YJ7r;3?f<p?(n$`@rT~-*crUjsifKrVMclcX95f{;y+s%8rx5QF
<(A2z8X3krV4&+Ql{{>eowHTrrT?P3mE%n_160dZRNYcxaQ;ULwmCk*#zTJ5YyDs@*5IjlWZZ%+7WrhS!=V)DGOm}y*uSTGTLlR4
$=f)ZlAvxqvqY}F=wWIp&WpB-cdaOb<C9+4`-huqeQvM}mg_x*-m}~{@=4wS96-EY7o~ku-Pr3B%>sU27fw|As+prv$f2fqb=lls
h@gtSVCWLY$~5gLN*U1l4VU%cJtY**RtAkyX^|~3r6=jZAk`~hR&YM%a%0R%zj~hBYB`zS4fkQE>|l^HAp1PC$~_Sh-q`=Rr|sAM
r9*XDj0%-GL|<)JnECSV2S$O3*If5+O>KB>9p>!tnqNS$?;GYKiTl%#PP|Xp#<Z11Y1!@hf3hShdgq<ZB3kmZ*<NCq4U}BSZV6)v
y}@&N8-SD?OX~;hB-2?n7|YS>3jlbHf^@$r2itZ=+d9!oeGrxC?C>lTFrX9tgG@QQ<!C@ANmETZK0taauE$yVqp{4ajZdy`5WF&4
deT1uZxTx?LfrhL!^3ALz;J@9k$$?Nzgsb(+g!XGH#Q8frq<%fMj9}8r!thA1(#0HTP2GMGmLcX6B`B`{Vk=58FzB>JiOo53|b<u
YwGHj%It=Ecpx+yc?y2<a(buwS2z1(eDzqF6gi+R2j>KQttQ`7Znf#_+qbW?2Cyu2#Ye~Dp=we&7!`+SO`5BO0%plW7MTGI5<Q}f
*E`w;fGc|#Gnn#7Z~V2gm~eZynqS&a#r*Yz?sKFKD&v3H;_H6kouPUJfE*F{6n7&i4)S)WiVR>PB7|f075qrynwZ^sPuAl-=ir5U
Q~Z{OQAxgvos-8@-!G`hdM6}^{V)R$gv8bH_C>TO>H<nL>8V0OixKz0VPuNr^J1J!jwVsS9RKJVg#Ica2{lIxDW-yBz^WE}Uus=(
_Xr9Uqr_ZeaPP&m?&dbUcwDA2u;1a*RenISR>((&K5#PZ4Stw<3{Ey{wrmqrBn(ViNRU2PeE|`;1_FkL?&Ua)L=|)LZW(B;dJsec
scq$!1)X%3<lY9uPv;2-Q!_4w$qPFLA+b~wE+}0E6=Ko%kWmLsz`??~cEuh+2DhtSpM)cDR+8|v+|e^wyANRIungfg5O0>pH{aSu
JuD6BX^7Eig3I5z)1|Uk^I7PpKDNC{%AvyFz6Me28)kd>!C$(#4===v+|bZsHCW{pxJT()a8(pjw$B3%p7S7v_xYo|NTpwDXW2TA
r+2u1Jcr$~8^&dKw*V@D%&Cj<)*oWqvis09{IO_mS4Jx$H5P0=`7T?$zai>0bpV@<L&r&&lH-3BBxfE1QU6ASgx<wOxM6LSYMrL3
-lfk;fB?x#>phTW&=h8Bg<em)J^iG-@@DdI!V}TguV(7N+83XL@E76m_sRbbE`47B;c$cHRCjR%ReMJqL6%7AX;HWQTEpwYi_@Sk
d6pRO0j!cutLhZJ;Jhs60Kc;G*(ZOV#}fW9GMQ`d6^DiU$kkvjmW!bOKpZ;wsp^H;rf_PBWGH7lBZwH*Y}w`;y2Rtqqg(H(l)mZ(
z9`oUP~De-F1ZAPkd|iJgp8R=%7ijmbxfMZ)MJJYx+Q9aE;WRmc6(+`f@5Sv?zP7_qVqVL!wpyl)FS8CZM}k&Y$f+7mZ%8MmY9|N
&Xro;Q~bjHJP$<%i%$uAyV+;25&s5++o(u2g;T98{9IZ(q__qGFVZuV;rB}^Bg?~?aB*qzH_8{#Ri4g-vgLP^Kw=Jh()?cN-AX42
h18)fI{Dp_-vnMuoKLlSoQ)`aA-?9*bH9T5U<FT-j7WgSUJ%4J+2~|F)dvC$va9&VdgZG?#<({}>+AmJ75;N}zut=T)EE%}<L{|G
y7S7}XIB*fRihjk(yGknyf|%1y1S4S0Alx-pxsz+5(Yolul^kkTU8w~RO5)LQ_xMPt+A+B;T}#FIWlmi1&<}~oP}x5?R|dtF=~Lk
yt=jTEwI{CSI3^FjQr?4G6aYMg!g>IFRe&2X?I+vT<w2#b_@e#RD)p4_zZrDR3X@~Z&=Nm#<pJ7oX#|}!p$8@a?yD(5UYQhvMYwN
s@{+X@#(3ID<7Atvz<-k#@*_~==(cLlh{K-079luD#fFC`VEDBqo)|eFwOq6VW6P<c;&(vn-JY*#n%wBwvz~E;)2^RqI|?>a?IV9
`L_Ku4SkdvBAeqF%!idk_;u{|kUDIGjMaUNiB5RH{q5Z?Jx9*eFi!l79z7+EO@Oj58%!xpo%{2<0Q+Niqn4g}fmrOb-c^ZoD7wlG
q5x@n#b&EWXI+$5Vd~7{+zKDuvfH!Ib0-LeML6Rq_P+qbeoSLDHnIO8{`!3uaSYk+X?*F>Yn!+`T3m>;UV?CO^U7MPDbp0P)u^0h
b0PCJyfm3yu)DwTi8ey%A>OxR<5ery47C6KIBse4S~CNA`@>ZMxxYGKy<M6V7($P_{gek{X~(Kd^1_MRc6{@19aYJQY~L#W0|^=W
mhF__uvV(G?k+}ocLEg%n@v;9+=mv%t5SkA*nd;lfpw=){axR3DmnY#DYSg^>$_!#8_TrCLbtPZhdq~a#aKike|`~}4Mn<>;yyWY
LuWwJM($@Rt-AL<h!)x)9^bZ@UiN_BnT5owGuCqHP)Zz6pzdHCY*FWsano_Tg{i^^uEo_rH6_KvC!m87EYU=`fEjATfBn3wFKI<c
x1RWoWX+6|ep9hw>9u{~0as>5Kq!*_Xmsl3{@zX?zxkwQ;f-h^!K$Um@jTm!Ikory;(vWwX>RmSia-7fBnzMoUFhjBu!o77djJ$S
&DHo5=RpbVtcr;zs!wx{-9Yp2k*!OP9F&djhmt2UkaQcav%R~u2DLC$UMMi+2WIw5@c7Gm!D)KO4pqSNYg}=7oPVzrBE?O*mdFkg
m<6L2o<vw)(=+XR!}KfXVGslduNdJRp{Si<WRQttmRup~Q95$B2;e7Gyi}l`$hShbF9Jqp6L{abVyg-nuynfNe!ime=-{Kqmrm|W
VRWg;BPV%Y`RDlOAHO1Ov+8+1%GPh=i>jCbt6SFi-YM$i(+kBH{$9`1%!(vvpxP{38cQ4_?T`Uggl^@{kp#>F6fA-3|CRo99C}VD
`zN}NKt`Tm0kHxRHcdtG^VS^>IXy=7c>#Pm<}3g7)+7X{GAQ~69h5Rhq(u3ON;GJ<Tg)8J&>B2oJVUCQAf;`uYEaLYb`NOJx5Sxn
k7J;8O{ZHdj}=?WUTg<!8mK>++2qF#zL2j$X<Ww`g_5`4USce_KQ?@l32L>Sp!iz9;;-Ka$dd&Ayfu_s`zyF+O^h(J{|LqgE{i30
8v!8jVY%FDpw)fs(U8I&?o;>qODdme?i6V9IDyf^J?`zAIk`=kx-5oN$4BfP9#}Tc5|qH&2q+c<j`seCZY!2#W%(k}AdzWV%g?Sw
XS>E^uVvO_Sx|pjsl7)t?IYd}V9oZe;6%foNX(*9RkXu1SP1^<c9XME01@)DvB|F%@}N*UjR`_~3?(E)Ve@Q+wcIikW&6`~NEg#J
3Q)p?l!DK=vL2=lM23`9aCQSTch#MLVXv9a9sUflH<|$PfaDyjh89vdDID~g<PwqvbKE8(1fFm;eGeQo7*P=BV_adJI(qn$2-M7~
VoxfAlG0T@bP@Fag6*{@vA^??I#k>K=6P9}=_5%UI={32KI~@Y7bx=ryiPxvmiOvM)II0~%;|i)NTVu;SY)XMmggQgt)$|T%iK|&
)%r%G##x@X9|6bL-z{1sj*#d^-$e*EU@fC%Z2HhrQ(YIyOJ;`4czJqxul^Yt6aQCH`4pBXsr2O*_>_2kd<W<JC=oynZRq+4>AqxB
Dyps72aulmq4ge1W)2xuU&ybyY{M;vnVr(K-#(1k>-NmxLFLPb=d3=;K*S=v;~)oVs1ffm+-*!J4|?TfOzeQ0<OU%@T>k?VP3{lZ
F3pW{fOrLaDIq71D&j2B#7Ky-H^63U26q?9WymS)q+*b%*~7h1`e#E_10=t{@?_7EgVgoZIj>pMDfYdU1Nz$r7*(>W0<iF;{&dgt
<Jd2lB@0JYLbxTcne4j;3H0(sSZvXTy=T2dpC<l}&8FSSnVa2|Iw-Xs=ah&LGQSK#6#K=U6G%i{Omk6m^Gj!RbtnGX_Am_mwDRY~
^c_Z!Bxn4sWHz*XWGNvn1Z1FejbORLy}i*-5%yY3)v478UX>iRz6n^#&Dxhs)F}R=`)QiT7X;Dlt3x>U#XtXdcK`Y+@C(au${kL4
sb)?!C1tD_=KRO8(+xqKgo9x}iC6mlwVEsbiep9dc?D%8h2$)-!s^%YjB4lTmSl2J7?)>5@NAdpz(reGR+L_q7g^~n^`rsW_QCiy
)^Ld!b@OhlNfZDRtX9e(kP6mF)%fp%Y0#n>3S%)=lT7l7ER_T>@2MS1*?w4?yuLZ<>jTJ31uW%=zBGu&Kq#0w|2?U*=~c4y4q54w
8`<gmfe0V_K>EP*f_WBAL`^o+WY|v6K@dngn5=++0V}Mo^=AeMsA~F{lB}umi*-!>&+srLJjV0j_%A=*Qk|N{?J{T4)zOy*dk^>Y
cq*$V8gcBHDYHb!zp-&UI8Vb0Kcf4V%Z1tPcz*#wSPriZYn9<*vDeiw0O8|=dXl_*qIXpet}zec9Ja;Y!xrZHt%EgG`UVq>P29-0
qQ>K>j9?=L;SYPzwTE(Qzp>$$@tGJy^*UM$jpq766hSmFBiaT#YX8|PBU`RU1|+F(dn;GnoPRvhyIQ$$q@cz2IT#+T5F8Vm<X{}X
zx9@ld412tJEW@UhwZkO=a*vS^u4o>!U&X-<IW%#@AH$GtDRzRf^n<jK=}RW7#Om$(`PONWI8gF!Q2K1(5(&NU0rV<jm)xg0P-`R
@PaYh=a(R8rPw6<+MwxcsHn}ef;LsS;o54(**V<d#1N+|BTZz>zN^ZFZtEHD<k-|g=mws-w`_fM<DH{&8%|b(kajd@z(kh<xx&!w
krL=F)rPR!n)NdlpwKE1h_=;h!WZe|X)l}|2cGH3*hB(udRRQ>CRKbO*#c2*u*5x=f~anNbP+iVY`(BCYBQa!gCsJd_%3n;mOh(}
Yv%nAI}CQ`ip<IrVOdAj0M89gD}%;j{`Ppe8H5@SRT41i3=@>LY?t&&LN4$AIZ|!d`OOYF{$U5cG+2PA%sPZKyC>Fd_K1n@&K5Lg
72QyrYEy$sv^|YJag|F<Mdal3`xHicU^>{(7VEMrJw%l0Lwhw=ObHNUW&ybQ2ZO0CGLD{TgAI9bL)kEGoDO`y=BDQlK)<kLU!wf`
A|q`t=Y+tKK$Y76ib`Ck6>%9YcG6f?Z@a*yc!)IpJAdWxw|thlOsk4RcQ7{qIx|r1)%NXOwVe7e#$`(is_^Kg0M7^uCQO8NtCkNK
DnD1fEXH_mR1w^cRHafhWofeSGp>8x?Oefxr%<~p_NXgitNs|3(AN?xQ*11pl{P7Algbr*GCN@fpO532iPW3~vL**MK21~l;paBd
0m$J)Z@5x+vDCY>>tKxuhs9Y%$}wSmn=4c&(78tn05g~s@9oe{CC+08at}l5a<(RuMx7vjF<<3RywXY$xO`Nv7%dD_4Zf`1Hnb4c
+vSH2uN*Uen)mv%qr$4sf%n22%cODnK7?8*O{X3^ribf%k8DqICjm!h&CN#`e)!qS)^&0G2bVXzrm^fM0~wgl-f_L5o%W5vJ4q8;
LeLAD>Bb<NEU1>igE`i?%}s*~!QD*Xwqdk{7(N>C-Q^7Z5A^6ssGMlkl0^Lnxsn<tEYoK6&34K9>_5&>8DnPUr((eS!)dS<ePwCl
noY1oY<%Oq3Iz3|)g~vgJdzp$NPHuY`rvVnK@v1HQV6=(4`YDE7t;mhu8VMzw`CdD#yY|-P>d5k%w*;wmHSe)8uyPK-S++)^yo;y
BMy163inFuUjK>&VDIM--<aBhiD`TlMzsjf8r6IUyV-QhtD>{NvDkFtw6rbx>{C#fL_z4+NLV+{3N)Py<OcP?B1sFjc?XTjye9+V
EP1Rz#^DS6bH|VM)-ld6QVFhr_l9Sy4<Rf~G}kKt5*sU+apVF#s()+EW8#`shEZ1_?l*w|?P&e@_ZNoKMm$rW?^d?Wq=8K%(R6{x
*h>`ZtV)rPE^3^ovz-*kxS@{#k2!D7tZs}s00EFZ)29Id%KI-%vBYQl0ssI200dcD
"""
def pin(b): return [len(b),hashlib.sha256(b).hexdigest()]
z=base64.b85decode(''.join(DATA.split()))
assert pin(z)==XZ_PIN
src=lzma.decompress(z)
assert pin(src)==SOURCE_PIN
out=Path(sys.argv[1] if len(sys.argv)==2 else 'boundary_recovery').resolve()
out.mkdir(parents=True,exist_ok=True)
(out/'mechanical_boundary.py').write_bytes(src)
r=subprocess.run([sys.executable,'-S','mechanical_boundary.py'],cwd=out,
                 text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(out/'replay.log').write_text(r.stdout,encoding='utf-8')
print(r.stdout,end='')
assert r.returncode==0
print('BOUNDARY_COMPLETE_LITERAL_CAPSULE_PASS',*SOURCE_PIN)
```

Supplementary complete source, output, and proof bundle: C34_MECHANICAL_BOUNDARY_AND_STRICT_ALTERNATIVE_V1.zip. The inline capsule is sufficient without the archive.
