# material-e8693671fe6a

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# TREE253_K2_NATIVE4_SHARED_ACTUAL_MOMENTS_V1
## Recovery capsule part 3/3 — proof, exact coverage, source map and reconstruction

## 1. Determination and exact scope

The two previously open near-end primal-root positions 1 and 8 are now excluded on **native TREE253/K2 incidence index 4**, for every genuine convex realization, at its own uniform-volume centroid and for every positive-definite physical metric. Each exclusion is an exact common-actual-tetrahedron first-and-second-moment separation certificate. Together with the previously accepted six interior positions 2–7 and the simple-endpoint theorem for positions 0 and 9, this closes **all ten primal-root positions of this one literal TREE253/K2 placement**.

This is not an exclusion of all 17-edge polyhedra, nor of the same unlabelled face lattice with a different full pole-shadow graph. It is one complete placement removed from the native 55-incidence TREE253/K2 cover. The accepted universal lower bound remains C>=34, and the whole (V,E,F)=(10,17,9) slice remains open. No construction or upper bound is authenticated by this result.

The old native register was 148/550 closed, 402 open. The two new roots are disjoint from the prior 148, giving **150/550 closed, 400 open**, with native index 4 now the first fully closed placement and **54/55 placements still having an open root**. In the W06 subregister the corresponding update is **60/200 closed, 140 open**, with 19/20 W06 placements still having an open root. Do not decrement the independent global 632-type/52585-jointroot catalogue without an explicit label map.

## 2. Literal physical incidence — no alias or remapping of the parent object

The source is the native index-4 row of immutable result `minimum-0078`, SHA-256 `2a0d3544bfb7f0c3b6366bdda3555bc650eede67a1444d51a2d7207a0079eecd`. It was read completely during this coordinator turn. Native vertices are numbered 0 through 9, facets 0 through 8. The vertex-to-facet incidence row is exactly

```
0:013   1:018   2:0237   3:078   4:1245
5:1278  6:134   7:2356   8:346   9:456.
```

The full nonnegative unequal pole-shadow graph is TREE253 with parents

```
p=(0,0,1,2,3,4,5,0,7).
```

Its eight true dual edges are 01,12,23,34,45,56,07,78. Deleting the corresponding genuine primal edges gives the complementary Hamilton path, in native labels,

```
(3,1,5,2,0,6,4,7,8,9).
```

The starting endpoint is the smaller native endpoint label. A root position is a position in this displayed path, not a native vertex label. The new positions 1 and 8 happen to be native vertices 1 and 8; the endpoints are native vertices 3 and 9. All matrices in the new certificates use path-position row coordinates. This explicit bijection is the only reindexing.

The genuine facet cycles, in the deterministic orientation used for selecting integration triangles, are

```
F0=(0,1,3,2)
F1=(0,1,5,4,6)
F2=(2,5,4,7)
F3=(0,2,7,8,6)
F4=(4,6,8,9)
F5=(4,7,9)
F6=(7,8,9)
F7=(2,3,5)
F8=(1,3,5).
```

Cycle reversal is irrelevant because the integration uses positive tetrahedral volumes. The verifier reconstructs these cycles from the literal incidence, verifies the 17 true edges, their two incident facets, Euler's identity and the complete complementary path. It does not assert geometric realizability merely from that combinatorial check; its theorem is conditional on any genuine realization with this maximal-facet structure, which is sufficient for exclusion.

## 3. Common-actual-cell moment lemma

Let P be any full-dimensional convex polyhedron realizing this incidence, translated so its actual constant-volume-density centroid is zero. Let X be the 10-by-3 matrix of its path-ordered vertices. Let M be any real positive-definite 3-by-3 matrix and G=X M X^T. Then G is positive semidefinite and nonzero (indeed rank three).

For each vertex apex a, triangulate every genuine facet not containing a from the least native vertex of its deterministic facet cycle, and cone those triangles to a. These tetrahedra partition P with pairwise disjoint interiors up to measure-zero boundaries. Facets containing a contribute only zero-volume boundary and are omitted. Because each selected facet is maximal, its polygon is strictly convex at its genuine vertices, and a is strictly off the plane of every nonincident facet, every selected tetrahedron has positive volume.

A tetrahedron is indexed by its sorted four path-position vertices t, irrespective of which apex fan contains it. Let d_t be **six times its actual volume**, and let D=6 Vol(P). The same four-set has exactly the same d_t wherever it occurs. No volume or centroid is independently fitted across occurrences.

Write chi_t for its length-10 indicator vector and

```
J_t = chi_t chi_t^T + diag(chi_t).
```

For the actual fan F_a at each chosen apex a,

```
sum_{t in F_a} d_t = D,
X^T sum_{t in F_a} d_t chi_t = 0,
sum_{t in F_a} d_t X^T J_t X = 20 D Sigma,
```

where Sigma=(1/Vol(P)) integral_P x x^T dx is the same actual second moment for every fan.

Proof: a tetrahedron's uniform-volume centroid is the average of its four vertices. For its barycentric coordinates lambda_i, E(lambda_i^2)=1/10 and E(lambda_i lambda_j)=1/20 for i!=j. Thus its second-moment matrix is X^T J_t X/20. These formulas follow directly from integrating monomials on the standard three-simplex, followed by the affine map to the tetrahedron. Summing over a true partition gives the three identities. In particular these are necessary identities of one actual body, not a realizability conclusion from arbitrary positive masses.

## 4. Exact separation theorem

Fix a path-root position r. Orient the path toward r, with parent p(i)=i+1 for i<r and p(i)=i-1 for i>r. Define

```
D_i = x_i^T M (x_{p(i)}-x_i),  i!=r,
L_i = 2 e_i e_i^T - e_i e_{p(i)}^T - e_{p(i)} e_i^T.
```

The required weak mechanical path arrows are D_i>=0. Therefore tr(G L_i)=-2D_i<=0.

Use any selected set of actual vertex fans. Let T be the union of their distinct tetrahedral four-sets. Suppose there are vectors g_a, symmetric matrices C_a, scalars k_a, and numbers mu_{ti} such that

```
sum_a C_a=0,   sum_a k_a=0,   mu_{ti}>=0,
B_t = sum_{a:t in F_a} (g_a chi_t^T + chi_t g_a^T + C_a + k_a J_t)
      + sum_{i!=r} mu_{ti} L_i
```

is positive definite for every t in T. Then this realization cannot satisfy all D_i>=0.

Proof: weight the trace tr(G B_t) by the actual positive d_t and sum over distinct four-sets t. The g_a term vanishes separately for each a, since

```
g_a^T G sum_{t in F_a} d_t chi_t
 = g_a^T X M X^T sum_{t in F_a} d_t chi_t = 0.
```

The C terms sum to D tr(G sum_a C_a)=0. The second-moment terms sum to

```
20 D tr(M Sigma) sum_a k_a = 0.
```

The remaining sum is

```
sum_{t,i} d_t mu_{ti} tr(G L_i) <= 0.
```

But every d_t is positive, G is nonzero positive semidefinite, and every B_t is positive definite, so every tr(G B_t)>0. This contradicts the nonpositive sum. QED.

No bounded metric condition number, coordinate box, lower bound on a tetrahedron's fractional volume, strict mechanical margin, spherical model, fitted mass, or common orientation of integration tetrahedra is assumed. The proof includes arbitrary affine distortion and all weak path-arrow walls. Triangulation diagonals are used only for integration and never counted as mechanical edges.

## 5. The two exact certificates

For r=1 and r=8 all ten vertex fans are selected. Their union has 80 distinct positive tetrahedral cells. There are 1324 coefficients per certificate: 100 components of the ten g_a; 9 symmetric C_a matrices with 55 components each; 9 k_a values; and 80*9 nonnegative arrow multipliers. The final C and k are defined as the negatives of the sums of the first nine, so both cancellation identities hold literally in integer arithmetic.

All coefficients in the persisted `certificates.json` are integers. They are not regenerated by a numerical solver during reconstruction. The arbitrary scale used in their discovery was 2^12; scaling has no role in the theorem. The checker rebuilds every integer B_t and proves **B_t-I positive definite**. For each of the 160 matrices it computes all ten leading principal determinants with fraction-free Bareiss elimination, and independently runs rational Fraction LDL elimination, checking that each successive product of LDL pivots is exactly the corresponding Bareiss determinant. Every determinant and every pivot is positive. Total: **160 blocks, 1600 positive leading principal minors**.

For root 1 the smallest leading determinant and smallest LDL pivot of B_t-I over the 80 blocks are both 58. For root 8 the smallest leading determinant is 108 and the smallest LDL pivot is

```
350691951248392485624173 / 6861190482065941005627.
```

These pivot values are exact check outputs, not asserted uniform eigenvalue lower bounds. All nine independently stored k coefficients are nonzero in each certificate. This demonstrates that the implemented pencil includes the second-moment channel; no claim is made that removing it could never yield a different certificate.

### Literal generated-stream pins

For root 1, compact JSON/LF serialization of all B_t has 34659 bytes and SHA-256 `bab37cc4414b2b17f307e063913cbae397d504720049785cfb6ba76e83e9c079`; its determinant stream has 12953 bytes and SHA `b162fce09356eb4c98d54a4202dc2d38a54eb5769b9b14313a7584d597d958670d` only if copied correctly from the report. The authoritative value in the persisted report is `b162fce09356eb4c98d54a4202dc2d38a54eb5769b14313a7584d597d958670d` (64 hex digits); use that exact report value, not the preceding deliberately untrusted prose transcription. Its LDL stream has 24570 bytes and SHA `4be69600bfd5f78bd4bbc32781047a4a1e0c73935e18c2b7366441ed45888336`.

For root 8 the corresponding streams are 34883 bytes / `f6bfb6e53cbd69762b141861ba6e8608ec78bcac943c32f7982386d6063abd37`, 14400 bytes / `1bdd637fc3544050130d05ddc38433a61779c74096e5fd74838e007d828871c4`, and 27369 bytes / `9a3c84e80dbbf976adc0d6a1036bbb7a3be90f0dcb8257ba0d997350028478fe`. The common membership-mask stream has 350 bytes / `b0397a07091e99d520f301a20e357eae9586f31f20226612bf9092703470e54b`.

The literal report in the recovery source remains authoritative for these optional diagnostic stream hashes. The actual reproducible inputs are the full integer coefficients and complete checker, not any hash.

## 6. From two roots to a fully excluded TREE253/K2 placement

The immutable pZ result cited in Section 2 proves that, for an actual strict (S,U,H)=(1,1,0) body whose **full nonnegative unequal pole-shadow graph** is literal TREE253, the genuine complementary Hamilton path must be the weak mechanical tree toward the sole unstable vertex. This is a necessary geometric conclusion, not the assumption that an arbitrary spanning tree captures all mechanical arrows. Additional off-path positive vertex arrows are not forbidden by the new certificate.

Positions 2,3,4,5,6,7 of native incidence 4 were already excluded by checkpoint38. Its complete immutable capsule is

- source part 1 `[internal-source-reference]`;
- source part 2 `[internal-source-reference]`;
- source part 3 `[internal-source-reference]`;
- proof part 4 `[internal-source-reference]`, SHA `cddbc642172666458e2f050d2ad5707116140b069d779360f69127c5e84ba200`.

The proof part was read completely during this turn. The previous full exact acceptance of all 38 certificates is inherited; these old source parts were not cold-rerun solely to distrust the prior result. In particular index-4 positions 2–7 are a literal subset of checkpoint38, not new numerical guesses.

For completeness, the simple-endpoint exclusion has the following short analytic proof in the present setting. At either endpoint v, its three incident poles q_i are independent and satisfy q_i^T v=1. Write r2=v^T Mv>0, sigma=1/r2, N=M^-1 and G^q_{ij}=q_i^T Nq_j. The relevant triples are {0,7,8}, with middle pole 7, and {4,5,6}, with middle pole 5. Each forms a directed two-edge pole chain. Cauchy gives G^q_{ii}>=sigma. Equality for one incident pole would give its weak shadow arrows to both other incident poles, contradicting its at-most-one outgoing arrow in the full literal graph. Thus all three inequalities are strict. If m is the middle, the two required chain arrows imply b_i=G^q_{im}-sigma>0 for all three i.

Let e_i be the actual edge vector from v opposite incident facet i, and h_i=-q_i^T e_i>0. The other two incident poles annihilate e_i. Therefore, by the independent three supporting forms,

```
v/r2-N q_m = sum_i (b_i/h_i) e_i.
```

Its M-inner product with v is zero. Hence

```
sum_i (b_i/h_i) v^T M e_i = 0.
```

All coefficients are positive, and the three terms cannot all vanish because the three simple-vertex edge vectors span R^3 and v!=0. Consequently at least one edge has strictly positive radial derivative. This endpoint cannot be an unstable equilibrium, even on weak walls. Thus positions 0 and 9 are excluded under the stated full-pole premise.

Now positions 1 and 8 are excluded by Sections 3–5, positions 2–7 by the literal checkpoint, and positions 0 and 9 by the endpoint theorem. These exhaust the ten vertices. This proves the whole native placement exclusion claimed in Section 1, while retaining the full-pole qualification.

## 7. Complete recovery capsule and transport correction

The canonical new source is split across two immutable materials. Concatenate them **without inserting any byte** between them:

```
Recovery capsule part 1/3:
[internal-source-reference]
5722 bytes
SHA-256 67820abe26d92ae7f50500dcb515c1572a3c075560e0a0155bf1875bbf252db8

Recovery capsule part 2/3:
[internal-source-reference]
9860 bytes
SHA-256 dcb085f0f1efaddbef357685e22070e8c65f2aa2ae037695d7365a885ec47fa3
```

Their exact concatenation is `recover_native4.py`, **15582 bytes**, SHA-256

```
14ca6e44721923fc7662496ebc5698571b63bb20b28c2132d74ce5607b9d310e.
```

The split falls inside an encoded string, not at a Python-line boundary, so adding a newline there would change the source bytes. The program itself decodes a compressed JSON bundle containing every exact verification input and complete source file. It verifies the decoded 27887-byte bundle against SHA `d1eab0e4e3ba4b5289f71042de4814ddf63b01c017629357e01b2d54953ac75d`.

The earlier material `[internal-source-reference]` is **excluded as a standalone recovery program**: manual transport inserted one extra ASCII W at zero-based byte/character offset 5722. Its 15583-byte hash is `8868216133866e78b820e91c72041d0275936b9c0642de806f1c1909f2ec14be`. The canonical two parts were extracted by the immutable store from its exact intervals [0,5722) and [5723,15583), respectively. This removes exactly that known transport error and reproduces the locally checked source hash above; it does not alter any certificate. The transport-corrupted predecessor is preserved as historical evidence, not silently treated as runnable proof.

Save parts as `source_part1.txt` and `source_part2.txt`. Reconstruction and verification commands are

```sh
cat source_part1.txt source_part2.txt > recover_native4.py
python -S recover_native4.py
cd native4_recovered
python -S verify_grouped.py certificates.json
```

The six exact reconstructed files are

```
verify_grouped.py     7956 bytes  c1a8bb624a41a04573b56a83ed859288ec005f351c0120fc90a969b8e0b3d04c
certificates.json   11403 bytes  96cf99bdf9ce8c095b1e0484c7cc7ca04fa5a2fd85148ab0a9c083be869eb841
grouped_search.py     5136 bytes  cc27c361c7dea443e9af83621383e6c2516bb6f724ceea21846d1a0a685a4bbe
quantize.py           1147 bytes  6ac24f7a00d798f15938fa70cd7dc589257060de8acd0de1d9cbde83755192b2
exact_report.json     1378 bytes  72707b48e737fdf86f787cb9796a224bbd341db41a6de26c1d132557f84f48d3
exact_check.log        245 bytes  c4923e175b86802fcce54fda29cf453a8b621c0f1a5839226ac1529c93a59a64
```

Expected complete recovery transcript:

```
NATIVE4_SHARED_ACTUAL_MOMENTS_EXACT_ROOT_PASS 1 80 800
NATIVE4_SHARED_ACTUAL_MOMENTS_EXACT_ROOT_PASS 8 80 800
TREE253_K2_NATIVE4_SHARED_ACTUAL_MOMENTS_EXACT_PASS 2 160
REPORT 1378 72707b48e737fdf86f787cb9796a224bbd341db41a6de26c1d132557f84f48d3
TREE253_K2_NATIVE4_SHARED_ACTUAL_MOMENTS_COLD_REPLAY_PASS
```

Two fresh-directory cold replays of this exact source, one with PYTHONHASHSEED=173, produced identical transcripts and reconstructed output hashes. Verification used CPython 3.13.5, standard library only, with assertions enabled and no numerical tolerance. Bareiss and Fraction LDL are separate exact determinant implementations inside the verifier; this is not claimed to be independent external peer review.

## 8. Discovery method, exact inputs and disposition

The optional complete numerical locator and quantizer are preserved in the same bundle because they materially produced the certificates. Their exact geometric input is the displayed native incidence and its deterministic fan rule. Commands were `python grouped_search.py 1` and `python grouped_search.py 8`, with all ten apices by default and second moments enabled. The starting vector is exactly zero; there is no random seed or stochastic step. CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1 were used. All optimization bounds and stopping parameters are literal source: g/C/k components in [-1,1], mu in [0,1]; L-BFGS-B temperatures (0.1,0.03,0.01,0.003,0.001,0.0003,0.0001,0.00003); maxiter 2500 per temperature; maxcor 30; ftol 1e-15; gtol 1e-10; maxls 40. It stops after the first computed minimum eigenvalue above 1e-5. The found minima were about 0.006784493175228304 and 0.006875130131975623. They are discovery diagnostics only.

Quantization tries scales 2^12,2^14,2^16,2^18,2^20,2^24 and accepts only after exact checking. Both accepted at 2^12. A fresh floating-point search is not promised to reproduce identical bytes on another BLAS; the exact accepted object is regenerated from the **literal integer checkpoint** in `certificates.json`. No originating sandbox file, candidate float vector, unrecorded solver state or parent numerical output is needed for exact reconstruction.

The earlier `minimum-0059`, SHA `181126150bab95649617ee4032b357af29b06e5588f018e9c5cc4afb7dd9b465`, was read completely and supplied the methodological direction of sharing actual four-set determinants, common centroids and covariance across fans. The new locator and checker were authored here and their proof is given above; they do not require extracting or rerunning that worker's large TREE312 capsule. The pZ result is used for the literal placement and forced complementary path; checkpoint38 is used for the existing six interior roots. The separately read four-triangle physical negative-control result `minimum-0038` is a boundary warning against unjustified larger principal-minor positivity and is not a dependency of this theorem.

## 9. Next useful mathematical direction

The common-actual-fourset/covariance pencil is now a demonstrated way to close near-end roots that the prior separate-per-fan first-moment pencil had left open. Native indices 8 and 9 already have positions 2–7 closed, so their two near-end roots are immediate meaningful targets. Other native indices may need both near-end and additional interior roots. Success on index 4 does not imply success elsewhere. A failed bounded numerical search remains UNKNOWN, never a feasibility proof or an exclusion. Any new exact certificate must retain the literal incidence, exact integer data and all shared-moment assumptions before its coverage is counted.
