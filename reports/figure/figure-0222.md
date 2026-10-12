# figure-0222

AI research report · 2026-09-02 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Calm Maple 15 — exact global full-row successor beyond `AQ32-C0-SP2-FP5-G44`

## Literal verdict

**No homogeneous convex polyhedral Gömböc was obtained.** The strongest completed endpoint is the exact rational body

```text
AQ32-G44-GLOBAL-M42-3S
```

with strict own-centred class

```text
(S,U,H)=(2,1,1),
```

not `(1,1,0)`. It is a rigorous finite **NONWINNER**, but it improves the supplied G44 endpoint from `(2,2,2)` to `(2,1,1)` and performs the assigned joint boundary deletion. The supplied journal records G44 as a 25,849-row, 14,424-active-facet exact endpoint whose two independent external-positive true-edge components force `U>=2`; it also requires their simultaneous removal in the next nonrepeating incidence change.

Artifacts:

- Complete exact archive (`AQ32_G44_GLOBAL_M42_EXACT_NONWINNER.zip`)
- Complete detailed handoff (`AQ32_G44_GLOBAL_M42_complete_handoff.md`)
- Independent verifier (`verify_AQ32_G44_GLOBAL_M42_independent.py`)
- Q OBJ (`AQ32_G44_GLOBAL_M42_Q.obj`) · Q STL (`AQ32_G44_GLOBAL_M42_Q.stl`) · Q display preview (`AQ32_G44_GLOBAL_M42_Q_preview_affine_normalized.png`)
- Polar P OBJ (`AQ32_G44_GLOBAL_M42_P.obj`) · P STL (`AQ32_G44_GLOBAL_M42_P.stl`)
- Archive SHA-256 record (`AQ32_G44_GLOBAL_M42_EXACT_NONWINNER.zip.sha256`)

Archive SHA-256:

```text
86205921eb6965e98435262c285c70b87a004c951301855f1660b2f9c8a297e0
```

## What changed relative to the journal

The inherited G44 forcing theorem is no longer the endpoint obstruction. The reconstruction retains every one of the `25,849` inherited source identities, appends `60` new extreme supports, and produces a final actual true-edge graph with **no edge whose two endpoints are inherited**. Since every predecessor true edge necessarily had two inherited endpoints, every predecessor true-edge component is absent. This deletes both certified G44 external-positive components simultaneously, and in fact deletes the complete predecessor true-edge graph.

The residual `R` and `N3` boundary stars are rebuilt at the same endpoint:

```text
X0=25843  inactive
X1=25844  inactive
X2=25845  active with wholly new star
X3=25846  inactive
N3=25840  active with wholly new star and unique unstable.
```

The intended stable lineage survives in a new exact stable 17-gon containing inherited sources `15966,25838,25845`; the intended unstable lineage survives as `N3=25840`. No new maximum-radius true-edge component inherits the unstable packet: `U` is exactly one. The remaining Euler-neutral defect is instead one extra stable triangle and one saddle edge.

## Exact finite construction

All coordinates lie on the common rational lattice

```text
D = 504430238520505397264595409105302418184999427639977218153777058912891456091220736069335483680072249904276829444383339106106085350502825369529856000000000000.
```

The inherited namespace is `0..25848`. Four inherited sources remain extreme:

```text
15966 <- stable anchor
25838 <- N1 lineage
25840 <- N3 lineage
25845 <- X2 lineage.
```

Every other inherited source is assigned a distinct deterministic exact point in the cube

```text
|x|,|y|,|z| <= 31/65536,
```

and is proved strictly inactive. Sixty active sources `25849..25908` are appended. The active geometry is an exact centroid translation of the accepted M42 acute-bridge body after the following three-support joint cap, exactified over denominator `10^12`:

```text
Y265=(-1783777456705,    296371401563,  -515473934704)/10^12
Y266=(-7991994226061,  -9615686876401,  -823980202563)/10^12
Y267=(10881762566603, -26623518783729,  -387324774623)/10^12.
```

The complete `25,909`-row table, all source mappings, and all expanded H/V/E data are in the archive. The deterministic generator is `generate_AQ32_G44_GLOBAL_M42_exact.py`.

## Full supplied-hull and irredundancy certificate

```text
supplied rows    25,909
active rows          64
inactive rows    25,845
Q (V,E,F)       (64,172,110)
P (V,E,F)       (110,172,64)
Euler Q/P       2 / 2.
```

The independent verifier reconstructs all rows without importing the saved endpoint arrays, runs a full `25,909`-row hull selector, and recovers exactly the `64` declared extreme rows. It then proves every maximal supporting plane exactly and checks the whole inactive cube against every one of the `110` maximal faces.

Strict separation data:

```text
inactive/maximal-face pairs represented   25,845 x 110 = 2,842,950
closest inactive unit distance            0.26771764244228708231772141304174265985...
closest active/nonincident unit distance  0.00000386916928244655319773517928729607825...
minimum true-edge length                  0.23367792955511013
minimum face-normal norm                  8.046398645895219e23.
```

Exact files include:

```text
AQ32_G44_GLOBAL_M42_all_supplied_Q_rows_exact.csv.gz
AQ32_G44_GLOBAL_M42_Q_vertices_exact.csv
AQ32_G44_GLOBAL_M42_Q_maximal_faces_exact.jsonl
AQ32_G44_GLOBAL_M42_Q_true_edges.csv
AQ32_G44_GLOBAL_M42_P_vertices_exact.csv
AQ32_G44_GLOBAL_M42_P_maximal_faces.jsonl
AQ32_G44_GLOBAL_M42_P_true_edges.csv
AQ32_G44_GLOBAL_M42_inactive_separation.json.
```

## Exact ordinary centroid and Santaló certificate

The target body is `Q`. Its exact ordinary volume is

```text
8915375348009246779749105985741965045807599503983131589408321803 /
8318214150531377674026385750000000000000000000000000000000000
= 1071.7895916925536...
```

An exact rational tetrahedral boundary sum gives

```text
ordinary first moments = (0,0,0)
ordinary centroid      = (0,0,0).
```

The independent verifier rediscovers the maximal faces and recomputes those exact zero moments from scratch. For `P=Q^circ`, `(P-0)^circ=Q` and `centroid(Q)=0`; therefore `0` is exactly the Santaló point of `P`, with uniqueness from strict convexity of polar volume. No numerical root stopping criterion is used.

## Certified joint deletion and rebuilt stars

The exact final set

```text
{e true edge : both endpoints of e are <25849}
```

is empty. This is the full-row certificate deleting both inherited forcing components in the actual boundary incidence.

The rebuilt `X2` star is

```text
neighbors       25857,25858,25903
incident faces  0,22,24.
```

The rebuilt `N3` star is

```text
neighbors       25854,25855,25886,25887,25905
incident faces  0,15,16,17,18.
```

The intended stable face is the exact 17-gon

```text
[15966,25849,25850,25851,25838,25852,25853,25854,25840,
 25855,25856,25857,25845,25858,25859,25860,25861],
```

and the intended unstable is the unique unstable vertex `25840=N3`.

## Exhaustive full-cone mechanics

Every maximal face, every full vertex tangent cone, and all four components of every true-edge normal cone are evaluated. Positive equilibria are exactly:

```text
stable 17-gon                                        margin 0.9235192930541258
stable triangle [25867,25883,25906]                  margin 0.11081462246590647
unstable vertex 25840=N3                             margin 0.17056666844922352
saddle true edge [25888,25908]                       margin 0.1928471706750093.
```

Global strict minima are

```text
positive-face component          0.11081462246590647
excluded-face witness            0.11069732441228776
positive-vertex component        0.17056666844922352
excluded-vertex witness          0.0040396750520153716
positive-edge component          0.1928471706750093
excluded-edge witness            0.026420909626831388.
```

Hence the complete own-centred class is strictly `(2,1,1)`. The full ledgers are compressed JSONL files in the archive.

## Communicating interior architecture

The exact M42 acute bridge remains embedded and supplies two communicating rails, two principal shared-interior-edge triangular bipyramids, and an exact 64-cell edge-star atlas. The three-support cap crosses the extra-stable and saddle sectors. This communicating complex is stored in `AQ32_G44_GLOBAL_M42_communicating_complex.json`; the predecessor-component deletion itself is certified independently from the complete final true-edge table.

## Exact perturbation family

A free per-vertex box would incorrectly triangulate the nonsimplicial stable 17-gon, so no such claim is made. The certified genuine shape freedom is the anisotropic family

```text
A(t)=diag(1+t,1,1),   |t|<=2^-20,
```

applied simultaneously to all `25,909` rows. It preserves the complete hull incidence exactly and preserves centroid zero. With `g=(1+t)^2`, every decisive full-cone sign reduces, after positive-denominator clearing, to a linear polynomial in `g`. The proof checks `371` exact sign constraints: all components of positive equilibria and one exact negative witness for every excluded face, vertex and true edge. The minimum endpoint-to-identity signed ratio is

```text
0.9993378916001512.
```

Thus the incidence, centroid, joint-deletion theorem and strict `(2,1,1)` mechanics persist on a nonzero genuine shape interval. This is a one-dimensional certified family; no high-dimensional post-moment perturbation box is claimed.

## Independent verifier and watertight meshes

Fresh execution of

```bash
./[internal-source-reference].sh
```

regenerates the endpoint and returns

```text
INDEPENDENT_AQ32_G44_GLOBAL_M42_EXACT_NONWINNER_VERIFICATION_PASS.
```

The archive was extracted into a clean directory, regenerated, independently verified, and checked against all recorded SHA-256 values. The compressed exact ledgers are byte-for-byte deterministic.

Mesh audits:

```text
Q OBJ/STL: 64 vertices, 124 triangles, 186 triangulation edges,
           every mesh edge incident to exactly two triangles,
           mesh volume equals the exact rational Q volume.

P OBJ/STL: 110 vertices, 216 triangles, 324 triangulation edges,
           every mesh edge incident to exactly two triangles.
```

The polyhedral true-edge count is `172` for both Q and P; mesh triangulation diagonals are not treated as true edges.

## What was tried and how the conclusion was challenged

A deterministic `3,000`-seed three-support triangular-prismatic scan was run on the exact M42 parent geometry. All `3,000` samples produced valid hulls. It found:

```text
strict (1,1,0) samples    0
samples with S<=1         0
samples with H=0          0
strict (2,1,1) samples  237.
```

Seed `519` was exactified because it preserved the intended stable/unstable pair while deleting the old extra stable face `{198,224,258}` and old saddle equilibrium on `{229,247}`. A further deterministic local differential-evolution run used `3,652` evaluations and reduced the replacement stable/saddle margins to approximately `0.0322/0.0399`; line probes then switched the active stable or saddle carrier before simultaneous death. These scans are discovery evidence only, not continuum exclusions. Their complete records and scripts are included under `discovery/` and in `DISCOVERY_SEARCH_LEDGER.json`.

## Exact first obstruction outside the G44 cell

The old external-positive unstable components are gone. The first exact obstruction in the reconstructed actual cell is the strict extra stable face

```text
[25867,25883,25906]
```

with margin `0.11081462246590647`. Together with the preserved stable 17-gon it proves

```text
S>=2
```

throughout the complete certified anisotropic incidence/centroid/mechanical family. The associated sole saddle carrier is `[25888,25908]`, margin `0.1928471706750093`. Fixed-cell anisotropic polishing is therefore excluded.

## First nonrepeating continuation

The next genuinely new topology is one connected finite-thickness **stable-saddle shared terminal** spanning the complete stars of `[25867,25883,25906]` and `[25888,25908]`. The evidence-supported minimal architecture is a double-prismatic, octahedral, or equivalent coupled `2↔3/3↔2` interior circuit with a transverse return tetrahedron. It must:

1. delete the whole extra stable triangle and the residual saddle edge in the same actual full-hull event;
2. retain the stable 17-gon and unique unstable `N3=25840`;
3. prevent any replacement stable, unstable or saddle birth before both target deaths;
4. retain at least four independent shape variables after the three exact ordinary-moment controls.

This is a construction target, not a proved global lower bound. Sequential treatment is disfavoured because the finite line probes repeatedly relay the carrier before annihilation.

## Unresolved limitation

The exact `AQ32-C0-SP2-FP5-G44` row archive or generator was not contained in the supplied journal and was not available among accessible artifacts. Consequently I cannot certify a literal continuous event atlas starting at its unavailable coordinates. The delivered object instead uses the task's stronger-global-reconstruction allowance: every inherited source identity is present, the complete final supplied hull is rebuilt exactly, and the no-inherited-inherited-edge theorem certifies deletion of both predecessor components. The final endpoint and its obstruction are exact; only the path from the unavailable G44 coordinates remains uncertified.

## Final judgment

`AQ32-G44-GLOBAL-M42-3S` is the strongest exact reconstructed endpoint obtained in this direction. It meets the central topological objective on the complete supplied hull, preserves the intended pair, eliminates the unwanted second unstable component, and reaches the independently verified exact near-class `(2,1,1)`. It is not the requested Gömböc because one strict stable-saddle pair remains. The archive is complete, deterministic, independently reproducible, and includes all exact rows, H/V/E incidence, full-cone ledgers, moment/Santaló certificate, perturbation proof, search record, verifier, and watertight OBJ/STL meshes.
