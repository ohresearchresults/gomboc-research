# minimum-0002

AI research report · 2026-09-07 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Historical, mathematical-priority, and prize handoff

**Evidence checked through 7 September 2026.** The public literature, the current journal’s new mathematics, and prize eligibility must remain separate records. The strongest public homogeneous vertex theorem I located is the seven-vertex result of Bozóki–Domokos–Papp–Regős, whose identifiable status remains a submitted preprint. The journal’s six-point reflection theorem supplies a different argument and a stronger facet consequence, but its publication priority is unresolved. A previously unidentified official 2026 conference announcement prevents a responsible assertion that no competing polyhedral construction has been announced. The documented prize concerns determining the minimum, not producing an arbitrary example.

## 1. Global lower bounds: what is actually supported

Throughout this section the target is a full-dimensional convex three-dimensional solid with uniform volume density, evaluated at its own volume centroid, with nondegenerate equilibria and `(S,U,H)=(1,1,0)`. Facets and edges mean actual maximal facets and true edges, not triangulation pieces.

The following separates publication status from mathematical consequences. The edge and complexity columns are elementary deductions from the stated vertex/facet restrictions, not separately quoted theorems.

| Evidence level for the homogeneous target | V lower bound | F lower bound | E lower bound | C=2E lower bound |
|---|---:|---:|---:|---:|
| Refereed tetrahedron exclusion directly verified in the literature examined | 5 | 5 | 8 | 16 |
| Including the publicly available 2024 homogeneous seven-vertex proof | 7 | 6 | 11 | 22 |
| Including the current journal’s new six-point reflection theorem | 7 | 7 | 12 | 24 |

The first row follows from the homogeneous tetrahedron exclusions; the second uses the 2024 theorem; the third belongs to the current research record, not to an established external publication located in this search.

Here is the combinatorial calculation. Every three-polytope has minimum vertex degree three, so `2E≥3V`. Euler gives `E=V+F−2`, and the usual face–vertex inequality gives `V≤2F−4`. Thus `V≥7` implies `E≥11` and `F≥6`. Adding the journal’s independent `F≥7` yields `E≥12`. None of these deductions assumes simplicity or simpliciality.

### The seven-vertex source and its exact scope

Sándor Bozóki, Gábor Domokos, Dávid Papp and Krisztina Regős, [*The smallest mono-unstable, homogeneous convex polyhedron has at least 7 vertices*](https://arxiv.org/abs/2401.17906), arXiv:2401.17906: **v1 submitted 31 January 2024; v2 submitted 5 June 2024**. Theorem 1 concerns uniform solid-volume mass and requires only `U=1`, not `S=1`. Its reduction covers general polyhedra rather than only the displayed simplicial types. The proof excludes 5,943 necessary quadratic systems using exactly checkable positive-definiteness certificates. The mass input is a root-coned tetrahedral decomposition and a necessary sign condition on at least one tetrahedron’s centroid. **Section 6 leaves seven-vertex cases unresolved; this paper does not prove V≥8.** The [author repository](https://github.com/dpapp-github/mono-unstable/) contains separate point-mass and homogeneous materials.

I did not locate a refereed version of that homogeneous theorem. Papp’s research page, which also lists 2026 publications, still labels this particular work **Submitted**. That is a verified bibliographic status, not proof that no unindexed acceptance exists.

For **monostability alone**, `S=1`, the strongest independently documented general facet lower bound I located in published background remains tetrahedron exclusion, `F≥5`. Regős’s 2025 doctoral **brief summary**, *An algorithmic approach to the mechanical equilibria of convex polyhedra*, explicitly describes tetrahedron exclusion as the known lower-bound result while giving the 14-facet upper construction. I inspected the summary’s printed page 8, not the complete dissertation. This makes the journal’s standalone `S=1⇒F≥7` consequential, but does not certify its novelty. [BME thesis summary](https://repozitorium.omikk.bme.hu/bitstreams/163f0c28-9286-4dca-93b2-1568ef9af8c4/download).

The inherited claim `V≥8` remains outside this literature determination: its certificate recovery is another assignment, and the current journal itself distinguishes that unlocated claim from the reproducible public seven-vertex theorem.

## 2. Explicit homogeneous constructions: existence, coordinates, and the unresolved 2026 lead

### Established existence is not a finite coordinate record

Zsolt Lángi, [*A solution to some problems of Conway and Guy on monostable polyhedra*](https://arxiv.org/abs/2008.02090): arXiv **v1, 5 August 2020; v3, 18 March 2021**; *Bulletin of the London Mathematical Society* **54(2), April 2022, 501–516**, first published online **17 March 2022**, DOI [10.1112/blms.12579](https://doi.org/10.1112/blms.12579). Theorem 2 gives equilibrium-preserving, centered polyhedral approximation under its smoothness, nondegeneracy and curvature hypotheses; Corollary 2 yields homogeneous polyhedral mono-monostatic existence. It provides no numerical facet bound or expanded coordinate object. Its proof uses specially treated critical neighborhoods, a finite noncritical cover, and reserved centroid-control regions—not an assertion that every sufficiently fine ordinary mesh works.

The Lángi–Várkonyi survey, [*Centroids and equilibrium points of convex bodies*](https://arxiv.org/abs/2407.19177), **v1, 27 July 2024; v2, 14 January 2025**, still says in §3.6 that no explicit estimate for `C(1,1)` is available. Its suggestion that the minimum might be roughly at least 1,000 is a conjectural expectation, not a proved bound or contest threshold.

### The exact 2025 lattice paper does not contain a Gömböc

Krisztina Regős, [*Homogeneous, Monostatic Lattice Polyhedra, or the Magic Pyramid with 17 Sides*](https://real.mtak.hu/229740/1/096-article-p203.pdf), *Építés–Építészettudomány* **53(3–4) (2025), 203–217**, DOI [10.1556/096.2025.00142](https://doi.org/10.1556/096.2025.00142): **received 25 March, accepted 10 June, published online 8 July 2025**. Its tables give integer coordinates for these homogeneous examples:

| Example | (V,E,F) | (S,U,H) |
|---|---|---|
| P2 | (18,34,18) | (2,1,1) |
| P3 | (18,34,18) | (3,1,2) |
| PB, Bezdek-type | (18,34,18) | (1,3,2) |
| PC, Conway-type | (34,51,19) | (1,4,3) |

The first three are **17-gonal pyramids**. None has `(1,1,0)`. The saddle counts here follow from the paper’s stable/unstable counts and Euler’s equilibrium identity. I inspected the construction passages and coordinate tables, including their continuations; the title is not evidence of a mono-monostatic construction.

Reshetov’s 2014 14-facet construction is likewise one-sided: the survey places it in `(S,U)=(1,2)`, not `(1,1)`.

### A material priority lead remains uncleared

The official [KIAS AI–Math 2026 Algebra, Combinatorics & Topology program](https://symposia.kias.re.kr/AI-Math2026/page/ai-math-act-2026) has an indexed abstract mentioning **“the construction of a polyhedral Gömböc”**, alongside folded statistics for symmetric Dyck paths and Harer–Zagier factorisability. This is a primary institutional announcement, not a secondary headline. However, repeated page retrievals returned no readable body, and searches did not recover the associated speaker, construction, density convention, coordinates or proof.

Therefore the defensible determination is: **I did not retrieve a public, complete construction establishing the requested uniform-volume polyhedral object, but a relevant 2026 announcement exists and has not been resolved.** “No such construction has ever been published” and “our construction is first” are not justified conclusions.

The journal separately records the lead’s fresh exact replay of `FUSION258_PN03_C1374`, with `(V,E,F)=(258,687,431)` and strict `(1,1,0)`. That is internal mathematical evidence for the upper bound, not evidence of its external publication date or priority. This historical investigation does not create a successor witness.

### The two 2026 analytical papers do not close the polyhedral question

Vincent Wesley Couey’s [arXiv:2604.17120v2](https://arxiv.org/pdf/2604.17120v2), *Sloan’s Analytical Gömböc at Published β: A Strict-Convexity-Constrained Reanalysis*, revises **v1 submitted 18 April 2026** with **v2 dated 23 May 2026**. It retracts the broad negative interpretation of Sloan’s family in the small-β regime and withdraws twelve of thirteen earlier mesh-based catalog certifications. Its convexity gate is dense-grid evaluation, not a uniform interval proof. There is also an internal wording conflict: §1.1 says the original negative claim is preserved, whereas the abstract and §§3.1–3.3 explicitly revise it for small β. These qualifications must travel with any citation.

**Independent logical check:** immediately after its Theorem 1, the paper infers that one minimum plus the Morse–Euler relation forces only two critical points. That inference is false: `(S,U,H)=(1,2,1)` satisfies `S+U−H=2`. This does not refute a separately proved two-critical-point example; it prevents using that inference as a general certification rule.

Couey’s [arXiv:2608.11213v1](https://arxiv.org/pdf/2608.11213v1), *Static Equilibria of Perturbed Spheres: A Single-Harmonic Class Map, a Parity Obstruction, and a Certified Counter for the Mono-Monostatic Regime*, describes an interval/Krawczyk smooth-equilibrium counter. Section 7 explicitly conditions the reported certification on a point-valued quadrature centroid rather than an interval enclosure of that centroid. Its identifier begins `2608`, but the retrieved submission metadata reports **16 July 2026**; I preserve that anomaly rather than silently changing the date. Neither paper supplies an audited finite homogeneous polyhedral solid.

## 3. Results that must not be transferred between mass models

The sharp **eleven-vertex/eight-facet** result is for equal point masses at vertices. Dávid Papp, Krisztina Regős, Gábor Domokos and Sándor Bozóki, [*The smallest mono-unstable convex polyhedron with point masses has 8 faces and 11 vertices*](https://eprints.sztaki.hu/10537/1/Papp_511_33771781_ny.pdf), *European Journal of Operational Research* **310(2) (2023), 511–517**, DOI [10.1016/j.ejor.2023.04.028](https://doi.org/10.1016/j.ejor.2023.04.028): **accepted 14 April, online 19 April 2023**; arXiv:2302.04252 **v1, 8 February; v2, 14 April 2023**. Theorems 3–4 establish the vertex result; the facet result is sharp as well. Its centering equation is the arithmetic vertex sum, `Σr_i=0`. That equation is not the centroid equation of a general homogeneous solid.

The 2025 survey’s 0-skeleton discussion still repeats the older eight-vertex lower bound. That paragraph is outdated relative to the 2023 EJOR paper; it must not be used to overwrite the sharp eleven-vertex result.

Gergő Almádi, Robert J. MacG. Dawson, Gábor Domokos and Krisztina Regős, [*On Equilibria of Tetrahedra*](https://d-nb.info/1312637218/34), *Mathematical Intelligencer* **46(3) (2024), 247–254**, DOI [10.1007/s00283-023-10294-2](https://doi.org/10.1007/s00283-023-10294-2): arXiv:2304.06984v1 **14 April 2023**, accepted **23 July**, online **19 September 2023**. In the journal numbering, Theorem 9 excludes a tetrahedron admitting both kinds of one-sided weighting, even at different centers; Theorem 10 and Corollary 11 give the one-sided weighted classes. Theorem 15 realizes every legal three-polytope f-vector except the tetrahedral one by **some weighted** mono-monostatic polyhedron. The arXiv and journal theorem numbers differ. I read the published proof of Theorem 15 through its continuation. None of these weighted realizations is a uniform-density existence theorem.

The practical inference is important: a proposed global homogeneous lower bound must use actual mass information. Excluding only a face lattice or an arbitrary-reference equilibrium assignment cannot substitute for that obligation.

## 4. Provenance of the new reflection/escape proof

### Classical component: centroidal central reflection

The inclusion `−(K−c)/d ⊆ K−c` at the volume centroid is classical. A precise modern primary reference is Szilárd Gy. Révész and Yannis Sarantopoulos, [*The Generalized Minkowski Functional with Applications in Approximation Theory*](https://journalofconvexanalysis.com/articles/jca11020/jca11020.pdf), *Journal of Convex Analysis* **11(2) (2004), 303–334**, received **26 June 2003**, revised **26 January 2004**. Theorem 8.3, printed page 329, states the centroidal asymmetry bound; Proposition 4.7 and Corollary 4.11 relate its notation to reflected containment. Its historical references include Minkowski’s **1897** convex-polyhedron paper and Radon’s **1916** convex-function paper. I inspected the modern statement and references, not those two original historical texts.

An essential terminology correction: the journal’s `16/5` concerns **asymmetry about the prescribed reference origin**. It must not be called the translation-minimized Minkowski asymmetry of a three-dimensional body. Moving the reference can change this quantity; the centroidal inclusion specifically uses the actual volume centroid.

### Established component: projection criteria and rooted falling trees

The escape inequality is not a newly introduced mechanical primitive. Dawson’s *Monostatic Simplexes*, *American Mathematical Monthly* **92(8) (1985), 541–546**, DOI [10.1080/00029890.1985.11971676](https://doi.org/10.1080/00029890.1985.11971676), is the relevant early source. Its method is described directly by Dawson and Wendy A. Finbow in [*A computational approach to stability problems*](https://www.cccg.ca/proceedings/1999/c09.pdf), **CCCG 1999**, both pages of which were inspected. It uses facet-area vectors summing to zero, a projection criterion equivalent to `x_i·x_j>|x_i|²`, analytic chain-projection bounds, and elimination of every rooted falling tree. Here “Minkowski’s theorem” means **facet-area reconstruction**, not the centroidal reflection inequality.

A later explicit shadow formulation appears in Bozóki–Domokos–Flórián Kovács–Regős, arXiv:2103.12769v1, **23 March 2021**, published as [*Mono-unstable polyhedra with point masses have at least 8 vertices*](https://doi.org/10.1016/j.ijsolstr.2021.111276), *International Journal of Solids and Structures* **234–235 (2022), 111276**. Definition 3, Lemma 2 and its corollary give strict vertex shadows and increasing radii. Section 6.1, Proposition 1, explains the special simplex bridge between facet-area vectors and projection feet: their length product is `d Vol/(d+1)`. This bridge does not give the same zero-sum condition for arbitrary polyhedra. Its discussion of homogeneous eight-vertex exclusion is not a proof of that claim.

Also, the “face vectors” in that discussion are perpendicular projection feet. The current journal uses **facet poles** in inequalities `a_i·x≤1`. These vectors should not be identified without the reciprocal-distance conversion.

### What is genuinely different in the journal theorem

The exact new statement recorded at **2026-09-07T05:21:20.636Z** is:

> If X contains at most six nonzero vectors in R³ and admits a rooted parent map satisfying `x·(parent(x)−x)>0` for every nonroot, then `−(5/16)conv(X)` is not contained in `conv(X)`.

This is a statement about a finite configuration at a reference point, with **no prescribed density and no arithmetic zero-sum equation**. Its potential novelty lies in the quantitative **full-reflection obstruction**, not in the escape inequality, centroidal reflection inequality, or rooted-tree language individually.

The comparison-critical proof ingredients are all explicit in the journal. A five-point separator lies within `φ=π/18` of the negative root direction, bounds every configuration projection by `61R/200`, and gives the reflected root projection greater than `49R/160`. Two deepest sibling leaves are collapsed using

`y·(p−y)=t a·(p−a)+(1−t)b·(p−b)+t(1−t)|a−b|²>0`.

The remaining six-point tree is a chain. Full containment first controls its initial edge, and then a separator for the five-point tail excludes the reflected **second** vertex while also excluding the first vertex. This use of a second reflected point is the crucial difference from testing only the root antipode. The journal supplies a six-point counterexample to that weaker root-only relaxation.

The facet application can be checked without making the invalid assertion that polarity preserves the solid-volume centroid. Here is the algebraic bridge:

`−K/3 ⊆ K  ⇒  K° ⊆ −3K°  ⇒  −K°/3 ⊆ K°`.

For `K={x:a_i·x≤1}`, the perpendicular foot on facet i is `a_i/|a_i|²`. If that facet is nonstable in a nondegenerate configuration, some inequality j strictly excludes the foot, giving

`a_i·(a_j−a_i)>0`.

Thus the actual facet poles form precisely the escape configuration required by the finite-set theorem. Their own uniform centroid is irrelevant. Applying the reflection obstruction to these poles yields `S=1⇒F≥7`; applying it to ordinary vertices yields `U=1⇒V≥7`. This is the journal’s legitimate dual route, distinct from applying the published homogeneous vertex theorem directly to an uncentered polar.

**Priority determination:** I found no inspected primary source stating this six-point `5/16` theorem, its sibling-averaging/tail proof, or the resulting general homogeneous `S=1⇒F≥7` conclusion. Nevertheless, the projection-chain ancestry is substantial, and the full 1985/1998/2001 simplex papers were not all available. The appropriate description is **an independently recorded proof with identifiable prior ingredients and unresolved publication novelty**, not “the first central-asymmetry proof.”

## 5. Two useful mathematical findings beyond the headline survey

### Joint projection bounds are an existing method for the seven-point continuation

The 1999 Dawson–Finbow account identifies a concrete improvement over bounding each chain projection independently: **bound the sum of two projections jointly**, because the position optimizing one term generally does not optimize the other. It attributes the analytic advance to Dawson–Finbow–Mak, [*Monostatic Simplexes II*](https://doi.org/10.1023/A:1004941706441), *Geometriae Dedicata* **70 (April 1998), 209–219**. Subsequent work recursively bounds whole-chain sums, with angular mesh `0.001` radians and derivative-controlled errors, leading to [*Monostatic Simplexes III*](https://doi.org/10.1023/A:1010339220243), **84 (February 2001), 101–113**. The journal articles’ metadata was verified; the detailed method here is supported by the authors’ full conference account.

**Proposed adaptation, not a proved extension:** the journal’s seven-point difficulty is simultaneous control of two prefix vertices outside a five-point tail. A joint attainable-projection bound or angular dynamic program is more promising than adding two independent cosine-power bounds. Its terminal constraint must be the present **full reflected containment**, not the older zero-sum facet-vector condition. The high-dimensional simplex nonexistence bounds themselves do not become three-dimensional global facet bounds.

### A published Conway-family exclusion is stronger than numerical non-discovery

Domokos and Flórián Kovács, [*Conway’s Spiral and a Discrete Gömböc with 21 Point Masses*](https://doi.org/10.1080/00029890.2023.2241336), *American Mathematical Monthly* **130(9) (2023), 795–807**; inspected preprint [arXiv:2103.13727v4](https://arxiv.org/pdf/2103.13727v4), **9 August 2022**. Section 4.3, Theorem 2 and Corollary 1, exclude homogeneous mono-monostatic bodies generated by the paper’s Conway `(n,k)` construction. The mechanism is the nonzero axial volume moment forced by meridional radial monotonicity. This upgrades numerical failure to a theorem **inside that specified family**, not for arbitrary twisted or asymmetric ring stacks. The 21-point positive construction uses equal vertex masses.

There is a harmless normalization error in the inspected v4: equation (12) has prefactor `2/9` and uses a pyramid-centroid distance `2r/3`. Direct radial integration gives instead

`∫_K x dV = (1/4)∫_{S²} r(u)^4 u dΩ`,

because `∫_0^r ρ³ dρ=r⁴/4`. Replacing the positive prefactor does not change the sign/nonvanishing argument. The theorem need not be discarded, but its printed moment normalization should not be copied.

## 6. Exact publicly documented prize conditions

The decisive source is Domokos, Flórián Kovács, Lángi, Regős and Varga, [*Balancing polyhedra*](https://amc-journal.eu/index.php/amc/article/view/2120/1567), *Ars Mathematica Contemporanea* **19 (2020), 95–124**, DOI [10.26493/1855-3974.2120.085](https://doi.org/10.26493/1855-3974.2120.085): **received 18 September 2019, accepted 20 May 2020, online 10 November 2020**. Section 4.4, printed page 118, offers

**`p = 10^6 / C(1,1)` US dollars**

for establishing the class’s minimum mechanical complexity. The opening footnote, printed page 95, names **Otto Albrecht** as backing the prize. It requires submission to the corresponding author, **Zsolt Lángi**, as an accepted publication in a mathematics journal of worldwide reputation, with general mathematical-community acceptance two years afterward. Both pages were inspected visually.

The same essential offer and footnote already appear in [arXiv:1810.05382v1, 12 October 2018](https://arxiv.org/pdf/1810.05382v1); v2 is dated **17 September 2019**, and the cited latest preprint v3 **17 November 2021**. The later preprint date is not the first announcement date.

The current [inventors’ Gömböc wiki](https://wiki.gomboc.eu/) also expresses the offer with denominator `F+E+V−2`. This agrees with `C(1,1)=2E` for the target. Its wording about minimal feature counts should be read against the precise class-minimum definition, not as a requirement to minimize vertices, edges and facets independently and simultaneously.

Consequently, a construction with complexity `C0` proves only `C(1,1)≤C0`. Determining the minimum additionally requires excluding every smaller admissible complexity, or another argument establishing the same exact minimum. A nonconstructive existence proof at the proved minimum could be mathematically sufficient to determine it; the examined prize text does not independently impose the research journal’s coordinate, mesh, or manufacturing deliverables.

**There is no C<1000 eligibility cutoff in the examined primary offer.** Nor does the public documentation examined settle escrow, continued funding, payment timing beyond the stated acceptance condition, tied claims, or the treatment of a particular AI-assisted submission. An online offer is not confirmation of those matters. No author or organizer was contacted.

A different historical statement should not be silently merged into this one. Réka Alíz Francisck’s original interview, [*Hungarian invention Gömböc*](https://dteurope.com/culture/hungarian-invention-gomboc/), **21 April 2010**, describes **USD10,000 divided by the minimum number of planes**. Both its numerator and denominator differ from the later published offer. It is evidence of an earlier description, not a basis for replacing the 2018/2020 formula or asserting a present payment obligation.

## 7. Handoff determination and remaining evidentiary gaps

For the internal mathematical ledger, the lead’s recorded theorem and replay support the interval **`24≤C_min≤1374`**, without relying on the unlocated eight-vertex certificates. For an external literature statement, the strongest retrieved public homogeneous vertex proof gives **V≥7**, with the derived target bounds **F≥6, E≥11, C≥22**; its refereed publication status is not confirmed. The facet improvement belongs to the current research proof until its prior art and publication history are resolved.

The most useful mathematical continuation exposed by this investigation is **joint projection control for the seven-point full-reflection problem**, informed by the Dawson–Finbow–Mak methods but retaining the correct mass relaxation. The most important priority continuation is obtaining the actual construction behind the KIAS 2026 announcement. Before claiming novelty for the elementary proof, the complete older projection-chain papers should also be compared against the exact finite-set statement, rather than only their abstracts or later summaries.

This search inspected theorem contexts, relevant coordinate tables, and prize pages in the cited primary materials, but it is not an exhaustive bibliography of every thesis, announcement or unpublished manuscript. The KIAS announcement remained unreadable beyond its indexed abstract; Regős’s complete dissertation and several older simplex papers remained unretrieved. Those gaps prevent a definitive first-construction or first-proof priority claim. The prize documents establish the published mathematical demand, but are insufficient to confirm present funding or a particular award decision.
