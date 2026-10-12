# figure-0329

AI research report · 2026-09-06 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Steady Comet 43 — finite support continuation and recoverable, unpromoted checkpoints

## Status

**No new strict homogeneous (1,1,0) body is certified by this handoff.** The work produced a recovery packet for two substantially different low-facet candidates, with generated reports recording the following results:

| Checkpoint | Recorded V | Recorded true E | Recorded maximal F | Recorded own-centroid class |
|---|---:|---:|---:|---:|
| SC43-H135-S1U4-R | 266 | 399 | 135 | (1,4,3) |
| SC43-H64-S2U1-R | 124 | 186 | 64 | (2,1,1) |

These are **unpromoted checkpoints in this response**, not accepted exact successors. In particular, satisfying E<500 does not complete the assignment when the equilibrium class is wrong.

There is a delivery limitation that must remain explicit: the complete source/data stream is retained in the generated handoff file rather than reproduced in this message. That misses the requested in-message recovery requirement. I also do not substitute generated report contents for an independently observed fresh replay in this final handoff. Consequently, neither checkpoint should be merged into the canonical journal as an accepted exact object from this response alone. The packet preserves the construction attempt, frozen inputs, verification programs and reports for immediate recovery; a transport or observation failure is not a mathematical obstruction or evidence that a candidate is invalid.

The principal recovery files are:

SC43_RESULT.json — generated handoff containing the complete inline source/data recovery unit

SC43_RESULT.md — the same generated handoff in Markdown

SC43_LOW_FACET_EXACT_HANDOFF.zip — frozen inputs, source, incidence, mass and feature reports

recover_sc43.py — standalone source/data recovery and replay entry point

Execution assertions in the generated draft should be checked against a fresh terminal replay before they are copied into the canonical journal.

## 1. Parent identity and the source-authority conflict

Both named immutable parents were used explicitly.

**SC43 parent:** `figure-0326`, supplied SHA-256 `666985a8eb99f9dbdf86f476942bf7c53c1c90bc1405a60f913c308585253ef6`. This supplies the physical projective mass-closing chart and the general bound E<=3F-6. Its original handoff explicitly withheld an observed executable acceptance of its14/25/13 negative control; that historical limitation must not be silently rewritten.

**RA04 parent:** `figure-0327`, supplied SHA-256 `429a40c5c6f706f778801dffd28981f68ff0976c0a157f25e469d753f70991a6`. The literal47-row table in that payload conflicts with the claimed monostable identity. The recovery work records that the printed table, normalized to one space between integers and a trailing newline per row, hashes to

`c9c50411a273c789a153019130f87f2db8b69906a5df8ddd43bfb5a7b4967d90`,

rather than its advertised

`f09e73df8aa01fac0bffca815f02d5769f37812ce369209c6598139a0475bcbc0ab`.

The literal-table reconstruction records166/249/85 and own class(34,28,60), not274/411/139 and(1,16,15). The supplied table and its advertised hash are explicitly present in the immutable payload. This conflict needs to be resolved from the literal data, not by retaining the monostable alias. 

A separately recovered Library archive contains a **different**47-row support table. Its recorded table SHA-256 is

`988b94768b185a170cf71304b0e32c9f31b4c27a3d3e2e0c0cb6e60a9d9d06e9`.

That different table is the recovered274/411/139, class(1,16,15) checkpoint used for the numerical continuation. It must not be silently substituted for the immutable literal table. Both tables are retained in the recovery unit, as `literal_rows.txt` and `recovered_rows.txt`, together with `expand.py` to expand their threefold orbits.

The recovered checkpoint's recorded canonical unstable vertices are

`[0,101,108,120,140,148,163,181,189,192,209,224,249,262,265,269]`.

This list also differs from the unstable list in the immutable prose. Its stable triangle is recorded as `[55,103,79]`.

The original recovered archive's all-in-one replay must not be called an observed unpatched pass here. Its recorded failure was a comparison between tuple-containing in-memory normal-correction data and JSON lists, specifically the fields `maximizer_normal` and `rows`. The proposed precise wrapper correction is to compare `json.loads(json.dumps(c))[k]` with the frozen JSON value. A serialization comparison repair does not resolve the separate literal-table conflict, and it does not restore the withdrawn normal-pool obstruction.

## 2. What the finite construction attempted

The physical model was

`K(q)={x:q_i dot x<=1 for every i}`.

Every free support received all three q-coordinate variables. This jointly changes its Euclidean unit normal `q_i/|q_i|` and support distance `1/|q_i|`. The work therefore pursued moved physical support geometry, rather than fixed-normal offset optimization or a duplicate of Rapid Atlas04's added balanced-cut operation.

After independent support changes, the numerical program rebuilt the physical H intersection and its actual fan. It calculated maximal polygons, vertices, true edges, ordinary volume and first moments, then applied the physical projective mass-closing correction. Its feature census used face feet, vertex conditions and complete two-normal edge cones. The implementation did not identify a polar centroid with the physical mass centroid.

At a simple physical vertex with active row matrix A,

`dx_free=-A^{-1}(dA)x`.

The solid-moment derivative gives `dc_free`. The common-pole correction is

`da=(5 Sigma+c c^T)^{-1}dc_free`,

and adds the physical vertex differential

`dx_projective=-x(x dot da)`.

At a centred endpoint this reduces to the parent formula `(5 Sigma)^{-1}dc_free`. A finite common pole addition a uses

`x_new=x/(1+a dot x)`,

with positive denominators. It changes the physical uniform-volume solid; it is not an ordinary translation. Common-pole addition alone is trivial after closing the mass of an already centred body, so it was used only as a correction accompanying other support changes.

The main numerical repair score was

`f_ij=Y_i dot(Y_j-Y_i)/[|Y_i|(|Y_j-Y_i|+0.005|Y_i|)]`,

on both physical vertices and centred polar poles. Root-connected minimum-cost directed trees supplied provisional escape routes, with edge cost

`max(0,tau-f_ij)+10^-12`.

Fixed root directions avoided changing the intended root solely because nearly equal radii exchanged order. The corrected linear program prices reserve deficits on all rows, keeps positive floors on guarded already-positive conditions, imposes a scale gauge and penalizes L1 displacement. An earlier variant omitted the newly incurred deficit when a previously above-reserve row crossed below reserve; that variant must not be treated as a mathematical acceptance test.

The recorded main defaults are tau=.001, regularizer .005, positive-guard threshold2e-5, retained positive factor .7 and L1 displacement weight .05. The one-pair branch used trust .01, L1 weight .01 and a numerical cap of two stable faces. Every claimed finite endpoint still needs its complete actual census; decreasing the tree cost does not certify cancellation.

The main branch records a reduction from sixteen unstable vertices to seven and then four. Support deletion and additional joint conditioning led to the135-row candidate. Its terminal deletion rule required actual S=1, no increase in actual U, a minimum polar reserve10^-5 and a score prioritizing U count and active-triple conditioning. In the final two deletions, a137-row array lost index64, followed by index130 of the already reduced136-row array, corresponding to original local label131. These historical indices are not the candidate's definition; the frozen table is.

A separate affine-metric seed with numerical class(2,2,2), followed by joint normal deformation and physical mass closure, supplied the64-active-support candidate. Many input supports became redundant during fan changes. The frozen64-row definition retains the actually active rows, rather than counting the original supplied poles.

Three recorded seed4302 affine screens each examined200000 proposals. They supplied alternative seeds, not a110 acceptance. Their finite failure and the local trust-region stalls imply no global obstruction.

## 3. Frozen candidate data and recorded census

The two final files are full H definitions. Each line `(a,b,c,h)` means

`a*x+b*y+c*z<=h`.

**Do not apply cyclic expansion to these two files.** The final135-row freeze uses grid10^13; the64-row freeze uses10^12. Let K be the corresponding physical intersection, filled at density1. Its own-centred version is K minus its exactly recomputed ordinary-volume centroid.

The recorded input identities are:

| Input | Recorded bytes | Recorded SHA-256 |
|---|---:|---|
| `aa_rows.txt` | 7870 | `1d9451a67d1038fb13e61dac7f3b435439154388f7774c23b105ddffd3a34796` |
| `ad_rows.txt` | 3420 | `53f14b04ac2723bd59000ec7b64642aaf22a8d1baf31e249b43a203a54a6e47a` |

For **AA**, the generated reports record:

- V266, true E399, maximal F135; class(1,4,3).
- Stable maximal quadrilateral `[51,112,106,55]`.
- Unstable vertices `[0,87,182,249]`.
- Saddle edges `[[114,137],[168,182],[261,265]]`.
- Empty degeneracy list and no zero ordinary-feature signs.

For **AD**, the generated reports record:

- V124, true E186, maximal F64; class(2,1,1).
- Stable maximal facets `[58,59,102,109]` and `[68,71,74,89,103,77]`.
- Unique unstable vertex57.
- Sole saddle edge `[107,115]`.
- Empty degeneracy list and no zero ordinary-feature signs.

The canonical incidence hashes recorded for sorted-key compact JSON containing `faces` and `edges` are

AA: `3ca2e3e493277c937f2bccaab89edfd2af0d9443d42db356cded29ef78021ced`.

AD: `76efb490632308b354fabe98980ab176e19e509faac312ceafcfb703407728d4`.

The recorded polygon-size distributions are

AA: `{3:8,4:17,5:45,6:30,7:21,8:6,9:5,18:1,19:1,24:1}`.

AD: `{3:8,4:15,5:14,6:13,7:4,8:3,9:2,11:1,13:2,14:1,19:1}`.

Their integration triangulations contain528 and244 triangles. The recorded393 and180 flat display diagonals are excluded from true E. An inherited report field named `C` equals2E, not equilibrium-adjusted mechanical complexity for these non110 objects. Its values798 and372 are not success flags.

## 4. Exact reconstruction and mass obligations preserved in the source

For every triple of integer support rows `(n_i,h_i)`, calculate

`d=det(n_i,n_j,n_k)`,

`p=h_i(n_j cross n_k)+h_j(n_k cross n_i)+h_k(n_i cross n_j)`.

Discard d=0; make d positive by a simultaneous sign change. Retain p/d exactly when every input support satisfies `n_l dot p<=h_l*d`. Divide `(p,d)` by its positive gcd, deduplicate and sort the actual rational coordinates lexicographically. These are the vertex indices used in the candidate reports.

For each active support, collect its entire equality set. Project onto the two coordinates complementary to a nonzero normal coordinate, take the exact monotone-chain hull, orient it outward and rotate the cycle to start at its smallest index. True edges are deduplicated consecutive unordered pairs of maximal cycles, not triangulation edges.

Write the reconstructed vertices as I_i/D using their common denominator. For outward fan triangles define

`W=sum det(I_a,I_b,I_c)`,

`B=sum det(I_a,I_b,I_c)*(I_a+I_b+I_c)`.

Then

`V=W/(6D^3)`,

`M=B/(24D^4)`,

`c=B/(4WD)`,

`x_i=(4W I_i-B)/(4WD)`.

These are ordinary solid-volume moments. The replay must independently reproduce V and c and re-integrate the centred boundary to obtain all three first moments exactly zero.

The generated records give approximate raw volumes7.972542446989 for AA and1063.987360810024 for AD. Their raw centroids are small but not declared exactly zero: approximately

AA: `(-7.6031911871e-16,4.1014881442e-15,7.8637033155e-15)`;

AD: `(2.7500044405e-12,-1.6267617373e-11,-7.8016583794e-12)`.

The exact census must use the rational centroid, not these decimal approximations.

For a centred edge a->b, put `d=b-a`, `L=d dot d`, `T=-a dot d`, and `Z=L*a+T*d`. With incident outward normals n,m, a strict saddle requires all four quantities

`T`, `L-T`,

`(Z dot n)|m|^2-(Z dot m)(n dot m)`,

`(Z dot m)|n|^2-(Z dot n)(n dot m)`

to be positive. Closed nonnegative boundary cases must be tested separately for degeneracy. The saddle count must not be inferred from Euler's equilibrium identity.

The first checker uses common-denominator integer supports, complete contacts, polygon halfplanes, closed oriented incidence, cyclic links, rank, origin-based moments, centred re-integration and a full feature ledger. The second imports neither that checker nor the builder; it rechecks the homogeneous support geometry, integrates nonnegative tetrahedra from a boundary-vertex apex, tests literal face feet, performs global all-point vertex tests and solves every edge Gram cone. The replay also verifies a strictly positive area-normal dependence summing to zero with rank3, excluding a nonzero recession direction.

The presence of this source is not by itself an observed PASS. The two complete checks and all frozen identity comparisons are the gate that must be rerun before promotion.

## 5. Immediate recovery procedure

The standalone recovery program is intended to contain a52960-byte decompressed JSON bundle with recorded SHA-256

`d9a0de3dde332082c0a8906439a4f3bf6313e88c42eeb92caec78b96a92f526a`.

That bundle contains complete source texts, both final H tables, both parent tables, the expansion helper and expected report/incidence identities. The recorded recovery-program SHA-256 is

`64713bd1b72b9dd3e438c62ecc9c844d3fa30065c369ee92dc5d72dcdec2a754`.

With the recovery program saved locally, run:

```sh
python recover_sc43.py sc43_recovered --extract-only
python -S sc43_recovered/replay.py sc43_recovered/aa_rows.txt sc43_recovered/proof_aa
python -S sc43_recovered/replay.py sc43_recovered/ad_rows.txt sc43_recovered/proof_ad
```

Do not use `-O`. The exact replay uses the Python standard library. The recorded environment is CPython3.13.5; optional numerical continuation uses NumPy2.3.5 and SciPy1.17.0.

The required acceptance event is agreement of both complete implementations on actual V/E/F, literal rational volume and centroid, every listed equilibrium and the complete degeneracy census, followed by matching the frozen input and full incidence hashes. Any failure must be retained as a failure, rather than repaired by changing the body under the old name.

The numerical continuation entry points are:

```sh
OPENBLAS_NUM_THREADS=1 TRUST=.01 REG=.05 TAU=.001 python sc43_recovered/search.py sc43_recovered/aa_rows.txt continuation_aa 300
OPENBLAS_NUM_THREADS=1 TRUST=.01 REG=.01 MAXS=2 python sc43_recovered/search.py sc43_recovered/ad_rows.txt continuation_ad 300 --allow-S
```

An optimizer rerun is not the frozen object's definition and need not reproduce the same numerical trajectory. Freeze any new finite endpoint as rational support rows, reconstruct its actual H intersection, recompute its ordinary centroid and rerun both complete audits before claiming an exact result.

## 6. Useful geometric continuation targets

The recorded135-row contact data identify support134 as the stable facet. The four unstable vertices have incident support triples

`0:{9,81,107}`, `87:{11,80,97}`, `182:{127,132,133}`, `249:{13,82,113}`.

Its three saddle edges have support pairs

`[114,137]:{107,122}`, `[168,182]:{127,133}`, `[261,265]:{113,120}`.

These are starting contacts for a whole-basin joint-normal replacement, not a theorem that moving only two incident planes is sufficient. A135-facet architecture has33-facet headroom under the sufficient168-facet budget.

The recorded64-row contact data identify stable supports5 and58, unstable vertex57 with supports `{8,28,33}`, and saddle `[107,115]` with supports `{36,53}`. This offers a separate one-extra-pair architecture with substantial support-count headroom. Its large aspect ratio and separated stable basins mean that “one extra pair” is a combinatorial statement, not a claim of proximity in shape space to a110 solution.

The remaining obligation is a finite open own-centroid110 endpoint. AA retains three extra unstable/saddle pairs; AD retains one extra stable/saddle pair. No collapsing witness, vanishing negative objective, approximate centroid or local numerical stall removes those obligations.

**Final disposition:** retain the generated packet as recoverable construction work, resolve the literal-parent conflict explicitly, and rerun the full recovery gate before accepting any exact checkpoint. This response does not supply the mandatory complete in-message source/data capsule and therefore does not promote an exact successor. The journal's accepted strict110 lead remains258/693/437.
