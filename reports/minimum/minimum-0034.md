# minimum-0034

Historical AI scientific report · saved 2026-09-09 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# NOVA24_F9_FIVE_TREES_25_ESCAPE_FRAMES_V1

## 1. Determination

**Every actual nine-facet monostable homogeneous convex three-polytope has a pole escape tree of one of only five rooted shapes. In fact every weak pole escape arborescence has one of those five shapes.** The complete nonnegative pole-shadow graph has at most **11 unequal directed pairs**, hence at least **61 strictly negative pairs**, and at most **eight weak escape arborescences**. A complete explicit cover consists of the 25 maximal directed graphs below.

This is a new universal nine-pole restriction, proved by **281 exact rooted-tree exclusions, 51,912 integer symmetric 9×9 matrices, and 467,208 leading principal minors**, followed by exhaustive exact directed-graph closure. It uses the actual original body's uniform-volume centroid and one physical metric with its reciprocal pole metric. It does not assume that the polar is uniformly centred.

For joint C32, this gives a whole-continuous-domain filter on the lead's at most two genuine complementary cotrees. In particular, the forced terminal triangular facet567 cannot be at cotree distance **three or four** from the unique stable facet in any sign-compatible complementary pair. All remaining possibilities are explicit below.

**No F≥10, V≥10, C≥34, new named whole-C32 type, or attainer is claimed.** The five residual shapes and the 25 graphs are an exhaustive outer cover, not claims of physical realizability. The global bracket remains `32≤C_min≤1374`.

Both a clean source-only numerical reconstruction and a separate frozen independent exact check **completed with exit status0**, matching all source, coefficient, report and directed-graph pins. The complete executable capsule is in §8.

### Authority and exact parent boundaries

The physical trace parent is `minimum-0024`, SHA-256 `b578a01ead261c6f7745122c22f4bb4767884e46ac46e1531b4e749a19332f95`. Its literal version-2 envelope was authenticated as 57,975 bytes using `json.dumps(...,ensure_ascii=False,indent=2)`. It supplies the actual simultaneous cap, not a theorem that arbitrary capped rows are physical. 

The other literal parent is `minimum-0032`, SHA-256 `3c4347c3beb52ca549da23ff0b0eb42a85251a52c2a920bbf1deb68b4b73fe4d`. Its original compact envelope was separately authenticated as 17,651 bytes using `separators=(',',':')`, without adding a final Markdown LF. Its original unobserved-recovery boundary is retained. The subsequently completed coordinator universal285/quad-ten proof is a distinct accepted dependency; it is not attributed retroactively to that parent. No mathematical parent/alias conflict was found.

The joint application uses the journal's necessary-existence matching theorem and the later exhaustive one/two primal-tree theorem. Neither says that an arbitrary prescribed complementary pair is mechanically valid.  

## 2. The complete five-tree complement

Write the actual facet poles as `q_a`, with `q_a·x≤1`. If the primal physical metric is `M>0`, set

`A_ab=q_aᵀ M⁻¹(q_b−q_a)`.

After relabelling the poles with the unique stable facet at root0, the only remaining parent arrays are:

```text
tree ordinal 253: (0,0,1,2,3,4,5,0,7)
tree ordinal 266: (0,0,1,2,3,4,5,4,0)
tree ordinal 272: (0,0,1,2,3,4,5,5,0)
tree ordinal 278: (0,0,1,2,3,4,5,6,0)
tree ordinal 285: (0,0,1,2,3,4,5,6,7)
```

Here `p[0]=0`, and each nonroot arrow is `i→p[i]`. These ordinals index the lexicographically sorted canonical preorder parent arrays of the 286 rooted nine-node trees. **They are not canonical C32 type IDs, primal vertex IDs, or original facet IDs.** Any use on a literal C32 lattice must transport the actual facet labels through the rooted-tree relabelling.

All 281 other rooted shapes are excluded with weak chosen inequalities `A_i,p[i]≥0`. In particular every nine-facet S1 body has a true-adjacency pole ascent path with at least six edges. No subtree is deleted or contracted when a secondary row is used.

The exact certificate plan is:

```python
rows01 = [246,247,248,249,250,251,260,261,262,263,264,265,
          267,268,269,270,271,273,274,275,276,279,280,281]
rows02 = [277,282,283,284]
remaining = [253,266,272,278,285]
```

The 253 other excluded shapes use row0 alone. The 24 entries in `rows01` use rows0 and1; the four entries in `rows02` use rows0 and2. The source variable called `apices` means these **coefficient-row indices**, not a tetrahedral fan or a newly chosen physical centre.

## 3. Physical and algebraic proof

### 3.1 The coefficients belong to one actual body

Let `V=Vol(P)`. For actual facet i let `A_i,h_i,c_i` be its area, its distance from the actual volume centroid0, and its uniform-area centroid. Put

`ω_i=A_i h_i/(3V)`, `Λ_ai=3ω_i(1−q_a·c_i)`.

The cone over facet i has actual volume `ω_iV` and centroid `3c_i/4`. Consequently actual uniform centring gives `Σω_i c_i=0`. The divergence identities give `Σω_i=1`, `Σω_i q_i=0` and `3Σω_i c_i q_iᵀ=I₃`. Therefore the **same** actual matrix satisfies

`Λ_aa=0`, `Λ_ai>0` for `a≠i`, `Σ_iΛ_ai=3`, and `ΛQ=−Q`.

The imported actual trace theorem gives, simultaneously,

`Λ_ai≤c₃<10/9`,

where

`c₃=max_{r≥0} 3(1+2r+3r²)/[(1+r+r²)(3+2r+r²)]`.

These are actual facet areas, centroids and cone volumes, not fitted masses. The pole metric is `M⁻¹` from the same primal metric. No volume centroid of the polar is substituted.  

The numerical program searches separating quadratic forms; it does not optimize physical Λ rows. The proof below remains valid in an independent capped-row outer relaxation, but its application averages only rows belonging to this one actual Λ. The stronger identity `Λ²+Λ=12·1ωᵀ` and the reciprocal two-facet-volume losses are **not used** in the accepted certificate. They remain additional constraints on the physical complement, not properties assigned to arbitrary outer-relaxation rows.

### 3.2 Every capped row is covered, including its closed boundary

The eight off-diagonal coefficients in a row lie in

`K={s: 0≤s_i≤10/9, Σs_i=3}`.

At a vertex of K at most one coefficient is strictly between its bounds: otherwise two such coordinates can be perturbed in opposite directions. Thus every vertex has two coefficients `10/9`, one `7/9`, and five zeros. There are exactly `C(8,2)·6=168` vertices.

For row a and distinct non-apex indices i,j,k, use the integer vector

`w=9e_a+10e_i+10e_j+7e_k`.

There are nonnegative convex coefficients `ρ_a,w`, summing to1, representing the actual row, and hence

`Qᵀ Σ_w ρ_a,w w=0`.

The ρ are an algebraic convex decomposition of an actual row. They are **not tetrahedron volumes or a fictitious fan**. Different decompositions need not encode any other physical moment. The certificate covers every extreme row, so no selection of favourable physical coefficients is assumed.

### 3.3 Exact quadratic contradiction

Set `H=Q M⁻¹Qᵀ`, a nonzero PSD matrix, and for each selected tree arrow put

`L_i=2e_i e_iᵀ−e_i e_p[i]ᵀ−e_p[i] e_iᵀ`.

Then `⟨L_i,H⟩=−2A_i,p[i]≤0`.

For each selected row a and each of its 168 vectors w the stored integers define

`B_a,w=γ_a wᵀ+wγ_aᵀ+9Σ_i μ_a,w,i L_i+9O_a`,

with `μ_a,w,i≥0` and `Σ_a O_a=0`. For one selected row `O_a=0`. For two rows the offsets are K and −K; its 45 stored upper-triangle coefficients give twice that coefficient on a diagonal and the coefficient on each off-diagonal entry.

**Every stored `B_a,w−I₉` is positive definite.** Multiply by the corresponding `ρ_a,w`, pair with H and sum. The γ terms vanish by the actual row equations. The constant offsets vanish because each convex decomposition has total1. The escape terms are nonpositive. Thus the weighted sum is nonpositive.

But every matrix exceeds I and H is nonzero PSD, so the same weighted sum is strictly positive. This is the contradiction. It works for rank-three H and, more strongly, without a rank-three restriction. It includes all weak escape equalities and imposes no metric cutoff or lower bound on any physical cone volume.

### 3.4 Exhaustive rooted-tree coverage and physical S1

Two independent tree enumerations agree: all 40,320 increasing parent arrays, canonicalized by rooted subtree strings, and a recursive multiset-of-rooted-subtrees enumeration. Their counts for sizes1 through9 are

`[1,1,2,4,9,20,48,115,286]`.

Every rooted tree admits a parent-before-child labelling, and the vector certificate is permutation-equivariant, so this covers every labelled actual tree, not merely selected graph automorphisms.

A unique strictly stable facet is a unique strictly unstable pole at the same origin in metric `M⁻¹`. Each other pole has a nonnegative escape on some true dual edge. Along any chosen arrow,

`‖q_p[i]‖²_(M⁻¹)−‖q_i‖²_(M⁻¹)=2A_i,p[i]+‖q_p[i]−q_i‖²_(M⁻¹)>0`.

Distinct actual poles therefore cannot cycle, even at equality. The arrows give a rooted tree. The 281 certificates exclude all but the five literal arrays above.

The certificate itself does not require that a chosen pair be an edge. This is why the following restriction also applies to nonadjacent pole-shadow pairs, while the later complementary-tree application still uses only actual edges.

## 4. Complete nonnegative-shadow graph closure: 25 maximal frames

Fix one of the five base arrays p and its eight required arrows. If an additional nonnegative pair `i→j` points to a descendant of i, the norm increase would form a cycle. Otherwise replacing `p[i]` by j gives another weak rooted tree. That tree must again be one of the five. This leaves respectively **7,6,7,8,4** individually possible extra arrows.

Coexistence matters. The independent graph checker exhausts all **592 subsets** of those extra-arrow sets, checks every parent choice, independently checks acyclicity, and compares the rooted-tree counts with directed Laplacian cofactor determinants. Exactly **82 base-tree-labelled graphs** are retained; they are covered by **25 inclusion-maximal graphs**. These counts are not claims of 82 or25 distinct graph-isomorphism classes or physical bodies.

Below each inner list is the complete extra-arrow set of one maximal frame. Add it to the eight arrows of its base p. The actual nonnegative graph is a subgraph of at least one such frame and contains its chosen base tree. Extra arrows may themselves be absent; every pair outside the frame is strictly negative.

```python
FRAMES = {
 253: [
  [(1,8)],
  [(2,8)],
  [(3,8)],
  [(7,6)],
  [(8,4),(8,5),(8,6)]
 ],
 266: [
  [(2,8),(5,7),(6,7)],
  [(2,8),(6,7),(7,5)],
  [(2,8),(7,5),(7,6)],
  [(7,5),(7,6),(7,8)]
 ],
 272: [
  [(2,8),(6,4),(6,7)],
  [(6,4),(6,7),(6,8)],
  [(2,8),(6,7),(7,4)],
  [(2,8),(6,4),(7,6)],
  [(2,8),(7,4),(7,6)],
  [(7,4),(7,6),(7,8)]
 ],
 278: [
  [(1,8)],
  [(3,8)],
  [(2,8),(6,4),(7,5)],
  [(2,8),(7,4),(7,5)],
  [(7,4),(7,5),(7,8)],
  [(8,7)]
 ],
 285: [
  [(2,0)],
  [(3,0)],
  [(7,0)],
  [(8,0)]
 ]
}
```

Every frame has at most11 nonnegative arrows, and every frame has at most8 rooted escape arborescences. This proves both universal numerical bounds. All weak boundaries are included: a zero chosen shadow still gives a strict norm increase between distinct poles.

## 5. Joint C32 consequence and exact continuous complement

For a hypothetical strict nondegenerate110 C32 body, the lead's primal theorem permits only

`T=(0,0,1,2,3,4,5,6,0)` or `T_alt=(0,0,8,2,3,4,5,6,0)`.

The second requires the actual edge28 and its appropriate escape sign. Necessary radial matching selects **some** sign-compatible complementary pair, so its actual cotree must complement one of those two available trees. Both cotrees must be considered when both are available. 

Each selected actual cotree, rooted at the actual stable facet, must have one of the five new shapes. Terminal facet567 has its edges56 and67 in either primal tree, so it has exactly one incident cotree edge,57. It is a nonroot leaf with the forced positive exit across57. The complete allowed pole labels and depths of that leaf are:

```text
253: label6 at depth6; label8 at depth2.
266: label6 at depth6; label7 at depth5; label8 at depth1.
272: labels6 or7 at depth6; label8 at depth1.
278: label7 at depth7; label8 at depth1.
285: label8 at depth8.
```

Thus **cotree depths3 and4 are impossible** for the terminal triangle. These are tree distances, not shortest-path distances in the full dual graph. The pole labels in this table are independent of the primal labels5,6,7.

This excludes the entire continuous joint domain of any rooted actual lattice/broom placement for which every available sign-compatible complementary candidate fails the five-shape filter; the terminal depth rule is a particularly small corollary of that filter. It covers every real realization and every SPD metric at the actual uniform centroid. No named canonical type/root is counted as newly closed here because I did not perform the lead's catalogue/cotree sweep.

The unresolved domain remains all genuine C32 realizations for which at least one of the two actual complementary choices survives the five-tree and 25-frame conditions, with the terminal facet on an allowed leaf. It must still satisfy all true incidences, support convexity, actual uniform-volume equations, the same physical Λ, its full matrix-square and reciprocal-volume identities, and one reciprocal metric. An admitted frame or a capped-row relaxation is not a physical witness. Nondegeneracy is needed for the joint matching invocation; the new S1 nine-pole theorem itself allows weak escape boundaries and degeneracies elsewhere.

The useful continuation is to intersect the lead's two literal cotrees with these five templates and terminal-leaf placements first, then apply the stronger actual Λ and common-volume constraints only to the retained labelled cases. There is no remaining large universal rooted-tree search in this certificate layer.

## 6. Reconstruction, exact checks and pins

The first single-row stage supplied253 certificates. Coupling two actual-row equations with cancelling constant quadratic offsets supplied28 more. The residual five are **unexcluded**, not declared feasible. The accepted proof does not rely on numerical failure in any attempted strengthening.

The independent checker imports neither the numerical engine nor the builder. It independently enumerates every capped-polytope vertex, expands scalar monomials to recover each integer matrix, and checks all positive leading minors by both integer Bareiss elimination and a separate rational LDL factorization. The complete graph closure is exact standard-library enumeration with independent directed matrix-tree counts.

Executed numerical environment: **CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OpenBLAS0.3.30/SkylakeX, Linuxx86_64, one BLAS thread, one process, no randomness**. Both NumPy and SciPy BLAS backends were checked as single-threaded OpenBLAS0.3.30/SkylakeX. The decoder and frozen matrix/graph verifiers use only the standard library.

All plans are literal. The locator starts with margin−1, zero free coefficients and escape multipliers totalling1; it uses `tau=0.05*0.18**outer`, at most12 outer rounds and70 Newton steps each, decrement tolerance `min(1e-7,tau*0.001)`, positivity factor0.99, Armijo factor0.05, at most60 halvings, symmetric solve with `rcond=1e-14` least-squares fallback, and margin threshold `1e-8`. It normalizes by the largest absolute coefficient and rounds at `10**8`; acceptance is exclusively the exact `B−I>0` check. These settings are not bounds on physical coordinates or metrics.

Save §8 as `recover_cap9.py`, UTF-8/LF/finalLF. In an empty directory run:

```sh
python -S recover_cap9.py > full_recovery.log
python -S recover_cap9.py check > frozen_recovery.log
```

The first regenerates every coefficient from embedded source and plans. The second rechecks the generated frozen coefficients. Both commands actually completed in this turn with exit0. `extract` authenticates source bytes only and is not a mathematical replay.

| File | Bytes | SHA-256 |
|---|---:|---|
| recover_cap9.py | 11977 | 5b568871fbf047909ed0c738c8f4df4fc61985d99492bfb14e5f7358d18e8c14 |
| cap_engine.py | 4681 | 74bd7575284f8729c038c8e9aaa3946e7c4f562448a760bd9a8010031840bbfe |
| build_cap9.py | 1839 | fa9f62d0e506330bb71751d8b42c9115f39944a6ce862a2674fbe34485289340 |
| verify_cap9.py | 6162 | 108b099264c362fa80a69362528266ec223e7a4407ed9011b7f951367957b5da |
| dual_frames.py | 4595 | e885a097ca6c2e69979b9a57900a52ee136fb95cc9821891350cc328f3095a6c |
| cap9_exact.json | 3737691 | 6ece23fec81293b1f67e0b7474c8bd7f91908e5c8fec879738dbc6f443b75bc7 |
| cap9_verification.json | 3701 | 471103e6b93d245a0320b5b0a747cc4ddee2025f7be368bf16ed23921319c9ed |
| dual_frames.json | 7688 | b174fe2cf9a941ef168acb553ef9bf5d95595a637e6844e5185b688f6bd84680 |
| full_recovery.log | 1906 | a7875bf243088527f497dab1e9e2b6a4acabd7187f0dfa6576dc099574437516 |
| frozen_recovery.log | 1448 | 0ad986b4f93604487de999070088d234cdaca4259177e372637f6ed472b4e61d |

The independent weight, scalar-matrix and leading-minor stream hashes are respectively

```text
bdbf7468726e5a46bb20673ceca19a6ff02e9ce1a6e1cd3d1a900297a78562b5
adf162e147077136fc064e3a438885af2a5228366f457f1947e1f1f157618fc2
3c26b93641ba6ddc53ed3aab4fbe4220fe9130573e4693a59b7ac21305d5fae7
```

Their ordering and canonical JSON-with-final-LF serialization are fully specified by the independent checker. The capsule authenticates its 17,810-byte decoded source/input JSON and its 8,965-byte whitespace-free base85 payload. No coefficient checkpoint, catalogue, journal or network file is an external reconstruction input.

This is an independently exact-checked computer-assisted restriction, not proof-assistant formalization or external peer review. Byte-identical numerical reconstruction is tied to the specified environment; frozen verification is exact arithmetic.

## 7. Actually observed full-replay transcript

```text
CAP9_RECONSTRUCTED 0 168
CAP9_RECONSTRUCTED 25 168
CAP9_RECONSTRUCTED 50 168
CAP9_RECONSTRUCTED 75 168
CAP9_RECONSTRUCTED 100 168
CAP9_RECONSTRUCTED 125 168
CAP9_RECONSTRUCTED 150 168
CAP9_RECONSTRUCTED 175 168
CAP9_RECONSTRUCTED 200 168
CAP9_RECONSTRUCTED 225 168
CAP9_RECONSTRUCTED 250 336
CAP9_RECONSTRUCTED 275 336
DETERMINISTIC_CAP9_CERTIFICATE_RECONSTRUCTION_PASS 281 51912
DATA 3737691 6ece23fec81293b1f67e0b7474c8bd7f91908e5c8fec879738dbc6f443b75bc7
INDEPENDENT_ROOTED_MULTISET_AND_40320_ARRAY_ENUMERATIONS_PASS [1, 1, 2, 4, 9, 20, 48, 115, 286]
EXACT_CAP_TREE_PASS 0 168
EXACT_CAP_TREE_PASS 25 168
EXACT_CAP_TREE_PASS 50 168
EXACT_CAP_TREE_PASS 75 168
EXACT_CAP_TREE_PASS 100 168
EXACT_CAP_TREE_PASS 125 168
EXACT_CAP_TREE_PASS 150 168
EXACT_CAP_TREE_PASS 175 168
EXACT_CAP_TREE_PASS 200 168
EXACT_CAP_TREE_PASS 225 168
EXACT_CAP_TREE_PASS 250 336
EXACT_CAP_TREE_PASS 275 336
ALL_168_CAP_POLYTOPE_VERTICES_PER_ROW_EXACTLY_COVERED_PASS
INDEPENDENT_SCALAR_BAREISS_AND_RATIONAL_LDL_PASS 51912 467208
UNIVERSAL_NINE_POLE_CAPPED_ROW_TREE_RESTRICTION_PASS 281 REMAINING 5
SAME_PHYSICAL_LAMBDA_ROWS_AND_ONE_RECIPROCAL_METRIC_NECESSARY_ONLY
NO_F10_V10_C34_OR_ATTAINER_ASSERTION
REPORT 3701 471103e6b93d245a0320b5b0a747cc4ddee2025f7be368bf16ed23921319c9ed
DUAL_ESCAPE_GRAPH_EXHAUSTION_PASS 253 7 12 5
DUAL_ESCAPE_GRAPH_EXHAUSTION_PASS 266 6 20 4
DUAL_ESCAPE_GRAPH_EXHAUSTION_PASS 272 7 26 6
DUAL_ESCAPE_GRAPH_EXHAUSTION_PASS 278 8 19 6
DUAL_ESCAPE_GRAPH_EXHAUSTION_PASS 285 4 5 4
ALL_OPTIONAL_SUBSETS_AND_DIRECTED_MATRIX_TREE_COUNTS_PASS 82
UNIVERSAL_F9_AT_MOST_11_NONNEGATIVE_PAIRS_8_TREES_25_FRAMES_PASS
JOINT_C32_MATCHING_MUST_USE_ONE_OF_AT_MOST_TWO_ACTUAL_COMPLEMENTS
REPORT 7688 b174fe2cf9a941ef168acb553ef9bf5d95595a637e6844e5185b688f6bd84680
ALL_CAP9_SOURCE_COEFFICIENT_REPORT_AND_FRAME_PINS_PASS
NOVA24_F9_FIVE_TREES_25_ESCAPE_FRAMES_COMPLETE_RECOVERY_PASS
NO_UNEXHAUSTED_JOINT_C32_DOMAIN_PROMOTED
```

The separately executed frozen check reproduced the independent matrix/graph markers and final recovery marker, again with all pins matching.

Supplementary [accepted source, coefficients, reports and completed replay transcripts](sandbox:/mnt/data/NOVA24_F9_FIVE_TREES_25_ESCAPE_FRAMES_V1.zip). The complete source below is the durable recovery, not that archive.

## 8. Complete literal recovery capsule


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
