# figure-0398

AI research report · 2026-09-17 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NC57 — nonlinear continuation of the exact C384 long-way-arc body

Assignment: `figure-0398`; slot Nimble Comet 57.

## Outcome

**No own110 construction is claimed.** I obtained eight new, exactly recoverable uniform-density polyhedra, including six own211/weak000 bodies, and two exact geometric/mass obstructions with explicitly restricted scope. The strongest new own211 construction by true edge count is **C260_COARSEN_COUNT: V74/E130/F58, C260**. It leaves 180 edges within the requested E<=310 budget. It is not a record improvement in the own110 class.

This was not merely source replay or another search in the old affine orbit. The work included independent vertex motions, polynomial deformations, changing support normals, deleting physical halfspaces, adding polar corridors, adding a free mass-closing apex, and a directed polar escape-tree objective. Actual hulls and ordinary solid centroids were rebuilt throughout numerical discovery. Only the eight fully audited rational bodies below are promoted as exact results.

## Source identity and authority

Both complete NONLOCAL7 material parts and the complete METRIC2 delta were recovered and manifest-checked. The starting body was precisely **C384_METRIC_BEST_003_G8**, not LOW_CURRENT: V66/E192/F128, own211/weak000, exact uniform centroid zero, centered bit costs114/114, own labels S42/125, U62, H59--64.

The standalone capsule below reconstructs its original report **byte-for-byte**: 50,185 bytes, SHA-256 `3761fcd1bcc014f71030378a0c3cdce69742e386536ad6c524954003adebdbc5`. Its literal exact coordinates are embedded; no approximate arc is regenerated.

The immutable RL04 ancestor `figure-0395`, SHA-256 `9fc14dd9e08f3f635aaab511cc93ca8219cc1b84ded8926c38cbabee87da3f86`, was read completely. Its 22,965-byte RL04_CENTER.py, SHA-256 `a0af63a1d7de9c872cb35b2c134da0eb788e1f0287fb4ddc33534d6fd83d7ef7`, was independently recovered from its source capsule and matched the NONLOCAL7 dependency exactly. EXACT.py contains the complete generic auditor section needed here. The archive catalog, current brief, and the complete earlier stable-pair result `figure-0328` were also consulted. No C162 coordinates, cells, or obstruction labels were transferred to C384. No unresolved parent-identity conflict remains.

## Exact new bodies

All rows below have **weak000**. Bit costs mean the bit length of the minimal common denominator of the actual centroid-centered coordinates, followed by the largest absolute integer numerator over that denominator. They are not floating-point precision estimates.

| Exact checkpoint | V/E/F | C | Own S/U/H | Centered denominator/integer bits |
|---|---:|---:|---:|---:|
| C260_COARSEN_COUNT | 74/130/58 | 260 | 2/1/1 | 11569/11570 |
| C292_COARSEN_MARGIN | 82/146/66 | 292 | 2/1/1 | 12455/12456 |
| C336_DUALOPT260_G8 | 112/168/58 | 336 | 2/1/1 | 15499/15500 |
| C372_ALT_FULL_G4 | 64/186/124 | 372 | 2/1/1 | 60/61 |
| C378_ALT_POLY_G6 | 65/189/126 | 378 | 2/1/1 | 87/88 |
| DUALOPT_LAST_G8 | 142/213/73 | 426 | 2/1/1 | 18904/18905 |
| C120_TREE260_G8 | 40/60/22 | 120 | 3/2/3 | 5878/5879 |
| DUAL_LONG64_COUPLED_G7 | 156/240/86 | 480 | 2/2/2 | 33934/33933 |

### Main continuation: C260

C260 is the intersection of these **58 exact parent halfspaces**, in the original parent's facet labeling:

`[2,3,6,7,8,10,12,18,20,21,25,28,29,30,31,36,41,43,46,48,49,50,51,53,55,56,60,62,64,67,68,69,70,71,72,74,76,77,80,82,83,84,86,89,90,101,103,104,109,110,112,113,117,118,119,120,121,123]`.

Its own labels are **S14/37, U65, H66--72**. Its two stable facets are the surviving original halfspaces31 and77, not the original stable halfspaces42 and125; both old stable carrier planes have been removed. Its unstable vertex is a genuinely new intersection, not any old parent vertex. Only18 old parent vertices survive at exactly their original coordinates. This is verified feature lineage, not relabeling inferred from a nearby floating body.

The maximal facet histogram is 6 triangles,32 quadrilaterals,10 pentagons,7 hexagons,2 heptagons and1 octagon. Hence there are **130 true edges**. A triangular integration mesh would have216 edges, including86 artificial diagonals; those diagonals are not counted. Exact uniform volume is approximately4.762151930593461, and the actual centroid in the parent's coordinates is approximately `(0.0037067123903519877,0.003907362608928886,-0.0014105858888351292)`. These decimals are explanatory only; replay recomputes the complete rational values.

C292 is the distinct margin-prioritized coarsening. It also retires both old stable carriers and develops stable facets on original halfspaces31 and77. Its own labels are S14/40, U76, H73--80. Neither coarsening achieves the net stable-saddle cancellation.

### Low-arithmetic and other retained geometry

C372 is the useful low-bit alternative: grid10^4 rationalization of a fully nonlinear endpoint, followed by an independently reconstructed hull and actual uniform centroid. The non-extreme input slots33 and45 are removed; the64-vertex result is own211 with S0/107, U59 and H57--62. The unstable vertex has deformation ancestry input62, but its coordinates are moved. The pre-rounding numerical screen reported E185/F123 at a near-coplanarity; the exact rational body has **E186/F124**. No numerical triangulation count was promoted.

C378 is a grid10^6 polynomial-deformation endpoint. Input slot45 is non-extreme; the65-vertex body is own211 with S16/75, U50 and H55--63. Its unstable vertex also has deformation ancestry input62. Its centered87/88-bit coordinates are substantially simpler than the support-intersection constructions.

C336 and C426 preserve actual free-normal continuations of the58- and73-support charts. Their tiny negative numerical non-root margins, about9.62e-8 and2.02e-7 respectively, did **not** represent success: both rationalized bodies are exactly own211. The corresponding positive-target objectives were about2.1923e-6 and2.4162e-6, above gamma^2=1e-6. C120 preserves the materially different, smaller, high-deformation escape-tree branch, but its own323 class is mechanically worse. The C480 polar-corridor construction preserves a genuine coupled-center/cut geometry, own222 rather than own110. Its actual uniform centroid is recomputed after rounding; it is not identified with the rounded construction center.

Every body's raw feature labels, strict and weak lists, incidence, exact moments, fraction costs and new-to-parent maps are reconstructed. LINEAGE.json explicitly separates geometric equality from deformation ancestry, including null mappings for genuinely new features.

## What was tried, and the finite scope

Four12-start local-foot searches used the full198 coordinate variables or57 degree<=3 polynomial coefficients, with either the dynamically deepest stable root or the alternative original facet125 direction. Their actual objective-call counts were7991,18718,4930 and5408. The complete sources include the positive targets, physical separation and volume guards, seeds, bounds and line-search rules. These searches can change the hull and actual mass, rather than preserving a nominal incidence list.

Two deterministic90-step physical-halfspace-deletion paths evaluated7515 deletion proposals each. One prioritized the true-feature-count screen after equilibrium count, the other the mechanical margin. The earlier55-step runs were identical prefixes, not two further independent paths. Exact retained-plane inputs from both paths produced C260 and C292. RUNS.json stores the complete selected paths compactly as ordered original-plane deletions.

Free-normal optimization used16 starts on each of the73- and58-support charts, with2874 and3806 calls. Directed polar escape-tree optimization used16 requested starts on each chart, with4639 and3933 calls; the latter had15 terminal records and one aborted start. A shortest-path arborescence coordinates positive polar escape witnesses globally instead of independently optimizing each point's best neighbor. The complete method, initial support labels, random seeds and non-default options are embedded. Its failures are finite-search results, not exclusions.

The polar-corridor scans evaluated360 fixed-center and336 valid coupled-center proposals. The free-apex experiment evaluated480 proposals; all480 achieved a numerical centroid gap below1e-8, but their equilibria remained wrong. Its best retained below-budget numerical example had E309, S2/U3, not own110. A moving coplanar-patch chart completed one step and125 calls before that patch ceased to be exposed. The exact source and complete selected floating apex and patch checkpoints are preserved, explicitly **not** promoted as exact successors.

The loose center MILP falsely reported optimality at a center whose independently recomputed census had two stable faces. It was rejected. Tightened tolerances and a larger positive margin produced the exact reference center below. No solver infeasibility or convergence flag has been converted into a geometric theorem.

## Two exact, restricted obstructions

### A. A C384-centered polar neighborhood cannot cancel the two stable pools

Let `q_i=n_i/h_i` be the128 literal parent polar generators, using its actual zero centroid. For componentwise perturbations `|delta_i|_infinity <= epsilon`,

`(q_i+delta_i) dot ((q_j+delta_j)-(q_i+delta_i)) <= q_i dot (q_j-q_i) + epsilon*(|q_j-2*q_i|_1+|q_i|_1) + 3*epsilon^2/4`.

The quadratic bound follows coordinatewise from `a*b-a^2 <= epsilon^2/4` on the square `|a|,|b|<=epsilon`. At **epsilon=1/50**, all cross-pool upper bounds are strictly negative for each of these two disjoint pools:

A=`[0,1,2,3,4,5,6,7,8,9,10,11,16,19,21,22,26,29,31,33,35,36,41,42,43,44,46,47,50,52]`.

B=`[66,75,77,87,89,90,93,97,100,103,109,111,112,119,120,125,127]`.

The exact2940 and1887 cross-pair checks attain their maxima at44->32 and112->118, approximately-0.005861231826698207 and-0.002406415233214659. The exact fractions are regenerated in POOL_EXACT.json. A largest-norm distinct point in each pool has strictly negative escape to every other distinct point inside that pool as well. Thus each pool contains an exposed strict unstable polar vertex, giving at least two strict stable physical maximal facets.

**Scope:** the convex hull of those128 corresponding centered-polar generators, with every coordinate displacement bounded by1/50 and the origin interior. Redundancy and incidence changes within that chart are allowed. Adding/deleting generators, exceeding the bound, or changing to a different own-centered polar chart is not excluded. In particular, this is not a global obstruction to C260 or to the assigned nonlinear direction.

### B. An exact new reference110 cell has a retained-plane/root mass obstruction

For the unchanged exact C384 body,

`c=(95329416,128405814,-64454932)/10^8`

has independently verified strict110/weak000, with **stable parent facet62 and unstable parent raw vertex19**. The entire closed L-infinity cube of radius **1/65536** about c has the same mechanics. This changes the reference root; it does not make the body's actual centroid equal to c.

Write its retained stable halfspace as `n dot x <= h`, and let `w` be parent raw19. Any uniformly filled convex body K containing w and remaining in that halfspace must satisfy the quarter-depth inequality

`4*(h-n dot centroid(K)) >= h-n dot w`.

This follows by decomposing the solid into tetrahedra from w: the three other tetrahedral vertices all lie in the halfspace. At c, the ratio `(h-n dot w)/(4*(h-n dot c))` is approximately4955.646481923435. Consequently every such uniform centroid has L-infinity distance at least

`381782623725265016599786708784719116111695474859175069 / 1060647323692028276606852408278503085530000000000000000`

from c, approximately **0.3599524697769569**, far exceeding the certified mechanical cube radius. This obstruction applies even if geometry is added outside other old halfspaces. It requires retaining this particular point and this particular halfspace; it does not cover moving/deleting either feature or all other reference110 components.

As a concrete necessary scale, keeping c,w and the normal n fixed while changing only h requires an outward support increase `delta_h/|n|_1 >= 4*B/3`, where B is the exact distance bound above, approximately0.4799366263692759. This is necessary, not sufficient, for mass closure. The capsule contains the complete exact derivation and checks, independently of the old C162 mass cells.

## Verification and uncertainty

Every promoted body passed two complete exact hull/incidence/ordinary-solid-moment implementations, every strict and weak face/vertex/full-edge equilibrium test, and a third centered integer tetrahedral integration with positive volumes and exactly zero first moments. The eight third integrations use144,160,220,124,126,280,76 and308 positive tetrahedra in table order. Negative controls with strict446 and weak123 were rejected as winners.

An additional independent executable, importing none of the auditors' clipping helpers, enumerates **every triple of maximal supporting planes**, reconstructs all feasible exact intersections, and matches the complete vertex set and every maximal facet owner set. All eight bodies and the exact parent passed it. Exact feature-lineage reconstruction also passed. All28 expected output files were checked against their byte counts and SHA-256 values after the standalone cold replay.

No lower bound on the globally attainable own110 edge count is established. The remaining stable-saddle pair in the six own211 bodies is real; an optimizer's small escape loss is not a cancellation. The two proved obstructions are restricted exactly as stated. The numeric apex and planar-patch states are retained as unpromoted material, not claimed rational certificates.

## Most useful continuation

Start from **C260's own-centered geometry**, not from inherited C384 root or facet labels. It has a genuine new unstable vertex and new stable carriers31/77,130 actual edges, and180 edges of remaining budget. The observed failure is replacement of the stable carriers, not a lack of affine parameter freedom. A further construction should change an entire stable basin together with opposite-side moment geometry, with positive margins and exact maximal-feature checks at every retained endpoint. The directed escape-tree code supplies a reproducible whole-basin mechanism, but its existing finite trials do not settle that task. C372 is the complementary low-arithmetic starting point for fast exact nonlinear experiments.

## Self-contained recovery

Save the complete code below as `RECOVER_NC57.py` and run:

`python -B -S RECOVER_NC57.py NC57_SOURCE 4`

The decoder reconstructs37 files, verifies every source/input hash, reproduces the exact parent, constructs and independently audits all eight bodies, runs both restricted certificates, and verifies all expected output hashes. No attachment, Library, network access, optimizer rerun or third-party numerical package is needed for this exact replay. The optional discovery programs use CPython3.13.5, NumPy2.3.5, SciPy1.17.0 and PyTorch2.10.0+cpu, binary64, with one BLAS/OMP/MKL/Torch thread. Every non-default parameter is literal in those complete sources. README.md supplies all discovery commands.

All newly claimed exact objects are defined by the embedded rational inputs, not by the optimizer's platform-dependent path. For the point checkpoints, rounding was exact Fraction(binary64)*grid with ties to even, independently checked against the stored production endpoints. For the support checkpoints, literal integer polar rows define exact halfspaces. Actual uniform centroids are recomputed in every case.

The uncompressed dictionary has146068 bytes, SHA-256 `8f6e206a6c8e7163b76623200840b024bd13643ed66b435d8e6358a48da4dacf`. The XZ stream has41032 bytes, SHA-256 `4136f82b7bc00ede74d1ac64da1fc8360ff7dcf71e88a21677db3439201abd91`. The whitespace-free base64 payload has54712 bytes, SHA-256 `a347fbba8aaf00075d4415c2482f6ae7235add79b1031271c1ce1642f99357b5`.

| Checkpoint | Report bytes | SHA-256 |
|---|---:|---|
| C260_COARSEN_COUNT | 113928 | `2894aaa74771ebd7e735eb42baec96f81208562970178b1ca9154cac1f25f973` |
| C292_COARSEN_MARGIN | 124147 | `2ed8c8a23c092841855be2462837c884242c7465a08625a9183418798413b78a` |
| C336_DUALOPT260_G8 | 115800 | `0fd305a77caa0ca389fd22f8538db9fc85e33229c7789b715e4e2644f46acecd` |
| C372_ALT_FULL_G4 | 14190 | `639b7dd56caf48ee99f1175e20b1f305100dc0fb3f75440dd20aba8df57b4cb5` |
| C378_ALT_POLY_G6 | 18534 | `fc46fb08252486d5c2474d70c6834b2f4849f8de25bcf18ccb059a7aa9ced661` |
| DUALOPT_LAST_G8 | 141858 | `e99c68aab019bc65622678fa749275924ec19858b1ed385443c637e6475c0e19` |
| C120_TREE260_G8 | 44165 | `8792789cb24e3d44b1efae2e7c0ff0a563aa5ef553d44fb18bfea382373494c8` |
| DUAL_LONG64_COUPLED_G7 | 339016 | `82286a4d4f65f812c725b97e9d40fbbfcc803d8ab73e4bc74572dda3df38b544` |

Expected final markers are `NC57_C384_NONLINEAR_EIGHT_NEW_BODIES_AB_MASS_TWO_SCOPED_CERTIFICATES_ALL_PASS` and `NO_NEW_OWN110_CLAIM`. The exact source-only replay was executed from a freshly decoded capsule; its completed verification log is included with the convenience archive.

### Complete standalone recovery program


[Encoded source block omitted; the code in this passage is incomplete.]


Convenience copies, not dependencies of the embedded recovery: [decoder](sandbox:/mnt/data/RECOVER_NC57.py), [source and exact certificates](sandbox:/mnt/data/NC57_C384_NONLINEAR_CAPSULE.zip), and [complete Markdown handoff](sandbox:/mnt/data/NC57_RESULT.md).
