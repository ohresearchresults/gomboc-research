# figure-0357

AI research report · 2026-09-11 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# Bright Quartz 13 — exact C630 cap-facet merger

## 1. Finite verdict and provenance

**EXACT WINNER: `BQ13_C630_CAP_QUADRILATERAL_OWN110`.** The new uniformly filled rational convex polyhedron, evaluated at its own exact ordinary-volume centroid, has

**(V,E,F)=(180,315,137), C=2E=630<632, strict (S,U,H)=(1,1,0), additional weak equilibria (0,0,0).**

All 137 input supports are active. The sole stable maximal facet is input **3**, the sole unstable vertex is raw Cartesian-lexicographic **98**, whose raw coordinates are **(0,0,1)**. There are no saddle true edges and no additional weak face, vertex or edge equilibria.

Both independently implemented exhaustive exact audits completed, their complete records agree byte-for-byte, and a fresh source-only replay decoded from the capsule below completed both audits, the exact parent comparison, direct centred integer integration and nonvacuous weak-equilibrium fixtures. The successful numerical proposal was also rerun in a fresh directory and reproduced the entire final rational generator byte-for-byte.

The literal parent is `figure-0356`, journal-recorded SHA-256 `a2aa80298e825e32c7069cda22c4274b00a09dacd68c824444e5cc5de4320f7d`, defining `BQ13_C632_THREE_LINK_OWN110`, V180/E316/F138. I decoded its complete 37-file capsule and compared all decoded file bytes with the supplied source archive. No defining-data or incidence conflict was found. The new body is **not** the older `C630_COORD_NONWINNER_OWN121`, even though their f-vectors coincide; that older body remains a distinct strict121 nonwinner. The current journal explicitly distinguishes the actual Bright parent from the coordinator's earlier nonwinners.

This is a further reduction within this supplied research lineage, not a claim of a global minimum or an independently surveyed world record.

## 2. Actual physical change: keep the three-link escape, remove its transverse edge

The proposed cap merger was realized. In the parent's final raw-lexicographic labels, the two old maximal facets are

```text
old support 135: [69,110,107]
old support 136: [69,97,110].
```

They are replaced by one exact maximal quadrilateral:

```text
new support 135, retaining old support 136's identity:
[69,97,110,107].
```

Old support **135** is removed. Every old input support above 135 is decremented by one; the remaining support identities are preserved. Comparing the two independently reconstructed complexes with this correspondence gives

```text
removed true edges: [(69,110)]
added true edges:   []
delta(V,E,F):       (0,-1,-1).
```

The two endpoints remain distinct; the segment 69–110 becomes an interior diagonal of the new quadrilateral, not a zero-length edge. Vertex 69's degree changes **7→6**, and vertex 110's degree **4→3**. No vertex is lost.

Crucially, the saved edge is **transverse to** the three-link escape route. The route **103→107→110→114** remains on the true boundary. Thus this construction does not shorten that chain to two links or purport to defeat the journal's frozen-centre minimum-link criterion. It removes an unnecessary lateral subdivision while retaining the escape mechanism. The journal had identified the 69–110 merger as unexecuted, not as an already certified consequence of its chain theorem.

This is a genuinely distributed physical redesign: exact comparison shows that **all 137 retained normalized support vectors changed**. The only unchanged raw vertex is apex 98. The ordinary volume decreases by approximately **4.340875145898467e-5**. It is not an affine image, a change of reference centre alone, or a changed drawing triangulation.

## 3. Construction mechanism and exactification

### A regular contraction coordinate

In the original 138-support contact generator, support 136 is solved from auxiliary nodes **155,161,180**, representing physical vertices **69,97,110**. Support 135 is solved from nodes **155,180** in axes **0,1**, with its remaining coordinate free. Put

`delta = 1 - q_135 dot p_97`.

Both planes already contain p69 and p110. At delta=0, the additional incidence at p97 forces q135=q136, provided the triple p69,p97,p110 is independent. The final quadrilateral's exact positive fan determinants and maximal-polygon reconstruction verify the required nondegeneracy.

The physical vertex solves were chosen not to use both coalescing normals in one support triple. Polar escape witnesses for rows 135 and 136 were fixed to **row 3**, avoiding a false improvement earned only from the shrinking difference q135−q136. All other retained mechanics were evaluated at the **moving actual filled centroid**.

### Whole-solid, own-centroid-aware motion

The numerical contact model differentiates the genuine filled volume W and first moment M, including

`dg = (dM - g*dW)/W`.

The proposal metric is the SVD-whitened Cartesian motion matrix formed from **Dq/2 and DP**. Selected positive exits, all relevant nonincident support gaps, positive oriented integration determinants and positive support heights are guarded. Only the two intended new incidences—(physical97,support135) and (physical107,support136)—are exempted from the old positive nonincidence floor.

There were **22 accepted numerical updates**, reducing delta from approximately **0.0024765174154331993** to **4.440892098500626e-16**. This residual is a discovery observation, **not an exact contact certificate**. The full source and exact numerical inputs are preserved below.

### Finite rational definition, not an optimizer limit

After the accepted motion, all controls were rounded to integers on grid **10^14**. The finite deletion/reindexing in `exactify_merge.py` then removes old support 135 from the controls and ordered plan, removes its incidence entries, decrements every larger node index and sets `n_supports=137`. No remaining plan node depends on the deleted normal; the program explicitly checks that fact.

The resulting standalone generator has **137 support nodes, 43 auxiliary contact nodes, 180 total control vectors and anchor node137=(0,0,1)**. One of these auxiliary nodes represents a now-trivalent vertex; they must not all be described as nonsimple vertices, and none represents ballast or a point mass.

The final generator has **12,886 bytes**, SHA-256

`8ba157e3f9358be2212c6a8f0a1becf018215b0b042eb7df314549e39ca9771d`.

Its reconstructed primitive integer halfspaces have **20,392 bytes**, SHA-256

`7769aae26fe54d6823ec2cc5786aba56acda90224df9d26bcdecbdfa4c2887f0`.

The discarded, rounded old row 135 need not be exactly equal to retained row 136: it is **not supplied in the final definition**. Every claimed incidence and equilibrium belongs to the newly reconstructed 137-halfspace solid. In particular, the legacy numerical end-print still uses the old 138-face list and emits a zero-Gram warning at the disappearing interface; that print is **not** the final census or true-edge count. The exact A/B rebuild below is the authority.

## 4. Complete final complex and mechanics

The final maximal-facet sizes are:

```text
51 triangles; 29 quadrilaterals; 28 pentagons; 11 hexagons;
10 heptagons; 3 octagons; 2 nonagons; one decagon;
one 13-gon; one 20-gon.
```

Vertex degrees are **138 of degree3, 35 of degree4, 4 of degree5, 2 of degree6, and one of degree44**. There are **356 integration triangles** and **534 triangulated-surface edges**, of which **219 are not true edges**. The actual complexity is 2×315, not 2×534.

The unique stable 20-gon's exact cycle is

```text
[64,104,158,160,163,166,168,171,173,175,
 170,169,156,155,154,132,127,123,97,69].
```

The retained escape-chain owners are

```text
103: [57,71,134]
107: [71,134,135]
110: [71,135,136]
114: [17,71,136].
```

For `eta(i,j)=(p_i-g) dot (p_j-p_i)/|p_j-p_i|^2`, exact integer arithmetic gives

```text
floor(10^9 eta(103,107)) = 190517
floor(10^9 eta(107,110)) = 249929
floor(10^9 eta(110,114)) = 235688.
```

All three links are true edges with strictly positive exits. Moreover, a complete true-edge physical escape forest reaches apex98 from **every** other vertex; a complete adjacent-facet polar escape forest reaches row3 from every other support. Their maximum depths are **94 and 75**. The exact floors of 10^12 times their respective minimum selected relative exits are **147 and 139**. The centred polar vectors used here are `q_i/(1-q_i dot g)`; the polar body's own volume centroid is never substituted.

These forest checks supplement, rather than replace, the complete mechanical audit. The final records check **630 face-side primitives**, **32,220 ordered all-vertex support comparisons**, and **1,260 true-edge primitives**. The face-boundary zero count, vertex maximum-exit zero count and true-edge primitive zero count are each **zero**.

## 5. Exact filled volume, all first moments and final centred coordinates

For either recovered generator, initialize each X_i from its literal integer control divided by 10^14, fix the stated apex node, and execute the entire ordered plan. For each `(i,deps,axes)`, solve `X_j dot X_i=1` for the indicated axes, keeping the other coordinates unchanged. `RECONSTRUCT.py` checks the complete prescribed incidence set. The first 137 vectors define

**Kraw = {x : q_i dot x <= 1 for all 137 i}.**

All feasible support triples are enumerated and the actual maximal polygons are rebuilt. For their outward canonical fan triangles define the finite exact rational sums

```text
D6 = sum det(p_a,p_b,p_c)
L  = sum det(p_a,p_b,p_c) (p_a+p_b+p_c)
W  = D6/6
M  = L/24
g  = L/(4 D6)
final vertex i = p_i-g.
```

The literal generator, full rational reconstruction and these finite formulas define the **entire** exact volume, all three first moments and every final coordinate. Both audits output all reduced fractions; no unstated root, reference-centre parameter, floating centroid or missing control is needed.

Display approximations of those exact fractions are

```text
W = 0.48861916878756106
M = (-0.006260619400488132,
      0.0028998027747884677,
     -0.0044911389858421375)
g = (-0.012812881279346792,
      0.005934688935728649,
     -0.009191491600680054).
```

The final centred first moments and centroid are **exactly (0,0,0)**. The raw centroid is allowed to change physically; relative to the parent its change is approximately

`(-3.1053418171632373e-6, -2.6146425181474386e-5, 1.766831762843856e-5)`.

A third integration builds centred integer vertices with a common positive denominator, changes each facet's fan anchor by two positions and directly integrates **356 positive tetrahedra**. Its three summed integer first-moment numerators are exactly zero, and its volume agrees by an exact integer cross-multiplication. This computation was actually completed in the cold replay.

### Actual fraction costs

| Object | Primitive H bits | Raw coordinate bits | Own-centroid bits | Final centred-coordinate bits |
|---|---:|---:|---:|---:|
| Literal C632 parent | 382 | 808 | 78,803 | 78,806 |
| **New C630 winner** | **390** | **823** | **78,945** | **78,945** |
| Retained approach65 nonwinner | 389 | 818 | 79,214 | 79,218 |

Each coordinate cost is the maximum numerator-or-denominator bit length. The winner's volume costs **39,553 bits**, its raw first moments at most **78,946 bits**, and the centred common-denominator export **79,028 bits**. Thus this result improves true-edge complexity, **not arithmetic complexity**. The grid and selected exit bounds are not fabrication-tolerance certificates.

## 6. Two completed independent exact checks and executed cold replay

**A** exhausts all **419,220 support triples**, tests every halfspace, certifies boundedness by six normal-cone decompositions, reconstructs maximal facets by exact planar hulls, derives true boundary edges and integrates origin-based tetrahedra. Its vertex test uses all other vertices and its edge coefficients use Gram expressions.

**B** independently clips all **9,316 plane-pair lines** against every halfspace. It reconstructs vertices, maximal facet cycles and edges by different code; integrates from a different strict interior apex with different fan anchors; tests vertex mechanics through true neighbours and globally; and uses cross/Cramer expressions for edge-normal coefficients. It does not import A's geometry, moment or mechanical functions.

Both test the two endpoint parameters and both incident-normal coefficients on **every true edge**, classify all complete vertex cones, including nonsimple cones, and evaluate weak cases separately. H=0 is not inferred from Euler.

Their complete normalized winner records are byte-identical: **425,307 bytes each**, SHA-256

`b2550e598dd239cd02c369e1f1ba83c409735c852577640fffa2121f582f7bc5`.

The final cold directory was populated by decoding only the 21-file source capsule below. No precomputed raw H, vertex table, A/B record or moments were supplied. The replay rebuilt both engines, independently reconstructed the exact parent for the complex comparison, performed direct centred integration and ran the fixture suite. Observed terminal marker:

```text
BQ13_C630_SOURCE_ONLY_TWO_FULL_AUDITS_PASS C630_WINNER
```

The actual complete cold receipt is **1,213 bytes**, SHA-256

`f0e44414cff89e348df6b497b29f20252b0eb720003cc8d6b0ae9d838dc66835`.

The fixtures include a regular tetrahedron with strict446/weak000 and a triangular prism with **strict446/additional weak123**; both are rejected by the winner gate. Earlier combined invocations exceeded their execution window after A/B and were not counted as finished full-pipeline receipts. The later observed replay completed the entire pipeline. Two arithmetic-only performance changes avoid unnecessary giant-fraction gcds in forest comparison and centred-integer export; they do not weaken a geometric or mechanical predicate.

The portable numerical reproposal also completed in a fresh temporary directory and reproduced both the complete final generator and primitive halfspaces, with marker

```text
BQ13_CAP_MERGER_NUMERICAL_REPROPOSAL_BYTE_IDENTICAL
```

These are independently implemented software checks within this research, not external human peer review or a proof-assistant certificate. No continuous no-birth theorem is claimed for every intermediate numerical parameter segment.

## 7. Preserved further attempt: a precise exact nonwinner, not a second reduction

After the winning merger I tried another physical facet contraction from the **new C630 winner**, not from obsolete coordinator labels. The intended merger was **support65 into support36**, across source edge **144–160**, with target gap `1-q36 dot p143`. That search temporarily omitted the to-be-removed facet65 from its numerical exclusion objective; the final exact audits omitted nothing.

Five accepted updates reached the stored checkpoint `BQ13_C630_MERGE65_APPROACH_OWN211`. Its independently reconstructed exact body is

```text
V180/E315/F137, C630; all137 supports active;
strict (S,U,H)=(2,1,1); additional weak=(0,0,0);
S=[3,65]; U=[98]; H=[(145,160)], owners=[36,65].
```

The different edge label is real re-sorting: **source construction vertex144 becomes exact raw-lex vertex145**. The target source vertex143 retains label143. The target gap fell from approximately 0.00352570634685 to the exact value bracket

`1933387665/10^12 < 1-q36 dot p143 < 1933387666/10^12`.

The close remaining support guard is now exact `(raw-lex145, support66)`, with

`6919450/10^12 < 1-q66 dot p145 < 6919451/10^12`.

There is no completed contact or further edge loss. Repeated corrections became ill-conditioned and a tool execution window ended before another saved accepted update. This is a finite failure of that attempted continuation, **not** a proof of nonexistence or a certified ordering of every possible future wall. An actual S/H pair remains and must not be hidden by the search omission.

The entire rational checkpoint is included. Generator: **12,884 bytes**, SHA-256 `faf2f9bd668d190294030c6289d60898f79b79d3e7e67e41f072d0b2ff1cc91d`. Both exact records completed and agree: **426,791 bytes**, SHA-256 `67411bb3d97f3f9702a86ad966d1393878eb0a36252f7bbdda8e460dec38ce8f`. Its source-only cold replay and centred integer integration also completed; receipt SHA-256 `a5c74598e990b9834a6866d1408113b180da07766cdb73efc950fa7f8463e593`.

Its exact volume and first moments are defined by the same complete reconstruction above; their display approximations are

```text
W = 0.4883560853831579
M = (-0.006342825841177847,
      0.002868069221180493,
     -0.004611798801259694)
g = (-0.012988116726755533,
      0.005872905666631026,
     -0.009443516604572124).
```

The useful next baseline remains the **C630 winner**. Further reduction should preserve the working three-link route while removing other transverse facets/edges, or deliberately redesign the entire new 65/36/66 contact region with its actual own mass. Continuing to optimize the former C630 U105/H(105,111) would use the wrong body. The near-contact attempt is supplied as an optional exact branch, not as the preferred winner or a global obstruction.

## 8. Complete source recovery and supplemental artifacts

Verified full bundle: exact H/V data, centred integer coordinates, maximal faces, true edges, both audits and actual receipts (`BQ13_C630_CAP_MERGER_VERIFIED_FULL.zip`) — **7,311,732 bytes**, SHA-256 `9c6b728a204dfaf99eb78d391cb6cefd5a6bd008037f718e0b06334041f35ad3`.

Source-only archive (`BQ13_C630_CAP_MERGER_SOURCE_ONLY.zip`) — **46,861 bytes**, SHA-256 `3c5ec7c666d33bb607a166067a2fbb5f4366f26618edef53c726e07ee3543b25`.

Markdown handoff (`BQ13_C630_RESULT.md`) and v2 JSON handoff (`BQ13_C630_RESULT_v2.json`) are supplemental copies. The full archive's exact coordinate table was read back and checked with integer identities. Its OBJ is explicitly display-only. Both ZIP manifests were actually read back and verified.

The capsule is the complete source authority for this continuation: **21 UTF-8 text files**, comprising 20 manifest-bound payload files and the manifest itself. It includes the literal parent generator, both new complete generators, exact reconstruction, both independent verifiers, centred-mass and forest/complex checks, the successful numerical source and all required helpers, the explicit deletion/reindexing, the additional attempted continuation code and its saved trace. No unseen library attachment or optimizer state is required.

Exact replay uses only the Python standard library; the tested version is **Python3.13.5**. Numerical reproposal additionally uses **NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1**. Do not run with `-O`.

After restoration to `BQ13_C630`, execute:

```bash
python -S BQ13_C630/REPLAY.py --object C630_WINNER --out exact_winner
python -S BQ13_C630/REPLAY.py --object C630_APPROACH65 --out exact_nonwinner
OPENBLAS_NUM_THREADS=1 python BQ13_C630/REPROPOSE.py
```

Both exact output directories must initially be absent. The winner alias `C630_WINNER` refers only to `BQ13_C630_CAP_QUADRILATERAL_OWN110`. Frozen literal generators remain authoritative if another numerical environment proposes different rounded bytes.

### Decoder and entire literal capsule

The whitespace-free Python-base85 string contains **39,745 characters**, SHA-256 **`bc9fdd179951b201df3f79aa56dc3a2a06a7465607ca8256bfc7bfebd79f677a`**. LZMA/XZ decompression yields **106,633 bytes** of UTF-8 JSON, SHA-256 **`d76805ced6a616683131d178b5f649ce4cb4fc014252a3a3104ec3934a2b011c`**. The JSON maps relative filenames to their entire literal text contents.

Save this Markdown as `result.md` and the following source as `restore.py`, then run `python restore.py result.md BQ13_C630`:

```python
import base64, hashlib, json, lzma, sys
from pathlib import Path
md = Path(sys.argv[1]).read_text(encoding='utf-8')
s = md.split('\nBEGIN_BQ13_C630_CAPSULE\n', 1)[1].split('\nEND_BQ13_C630_CAPSULE\n', 1)[0]
s = ''.join(s.split())
assert len(s) == 39745
assert hashlib.sha256(s.encode()).hexdigest() == 'bc9fdd179951b201df3f79aa56dc3a2a06a7465607ca8256bfc7bfebd79f677a'
b = lzma.decompress(base64.b85decode(s))
assert len(b) == 106633
assert hashlib.sha256(b).hexdigest() == 'd76805ced6a616683131d178b5f649ce4cb4fc014252a3a3104ec3934a2b011c'
files = json.loads(b)
assert len(files) == 21
root = Path(sys.argv[2])
root.mkdir(parents=True, exist_ok=False)
for name, text in files.items():
    rel = Path(name)
    assert not rel.is_absolute() and '..' not in rel.parts
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(text.encode('utf-8'))
manifest = json.loads((root / 'SOURCE_MANIFEST.json').read_text())
for name, expected in manifest.items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected
print('BQ13_C630_COMPLETE_SOURCE_CAPSULE_RESTORED')
```


[Encoded source block omitted; the code in this passage is incomplete.]
