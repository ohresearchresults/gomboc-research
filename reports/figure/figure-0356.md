# figure-0356

AI research report · 2026-09-10 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Bright Quartz 13 — complete non-affine U/H cancellation; exact C632 winner

## 1. Finite verdict

**EXACT WINNER: `BQ13_C632_THREE_LINK_OWN110`.** I constructed a new rational convex polyhedron with uniform density throughout its filled volume, evaluated at its **own exact filled-volume centroid**, having

**(V,E,F)=(180,316,138), C=2E=632, strict (S,U,H)=(1,1,0), additional weak equilibria (0,0,0).**

Both complete independent exact implementations actually finished, agreed on their entire normalized records, and subsequently finished again from the decoded source-only recovery capsule. The sole stable maximal facet is **input facet 3**. The sole unstable vertex is **raw lexicographic vertex 98**, the raw apex **(0,0,1)**. There are **no saddle true edges and no weak face, vertex, or edge equilibria**. Every one of the 138 supplied support planes is active.

This improves the supplied accepted **C634_SOC** baseline by one true edge. It is not the coordinator's existing C632 nonwinner, and it does not reclassify the C630 starting body. The journal identifies those two earlier objects as strict121/weak000; that distinction is preserved. There is no invented immutable parent assignment. The new f-vector differs from both C630 and C634, so this is not an affine image of either.

## 2. Exact lineage and the actual whole-basin operation

The capsule retains four independently checked exact bodies:

| Capsule object | Mathematical identity | V/E/F | Strict; additional weak |
|---|---|---|---|
| `C630_START` | Literal coordinator `C630_COORD_NONWINNER_OWN121` | 180/315/137 | 121; 000 |
| `C622_DISK` | New `BQ13_C622_DISK17_21_OWN121` | 178/311/135 | 121; 000 |
| `C622_READY` | New `BQ13_C622_SPIRAL_READY_OWN121` | 178/311/135 | 121; 000 |
| `C632_WINNER` | New `BQ13_C632_THREE_LINK_OWN110` | 180/316/138 | **110; 000** |

For the nonwinners, C622 denotes the edge budget 2E, not a claim that they are Gömböcs.

### Preparation: eliminate the inherited star, then change the complete physical basin

I first used a full point/support contact chart, the actual filled-centroid derivatives, and a root-reaching escape forest to deform the literal C630 geometry. Removing **original supports 17 and 21** from that deformed body produced `C622_DISK`. This removes the inherited nonsimple U star and its old 17/19 saddle carrier, but leaves another U/H pair. I therefore treated it as an exact transfer checkpoint, not cancellation.

Further non-affine physical deformation produced `C622_READY`. Its newly reconstructed exact lexicographic census is S3, U98 and U103, H(103,112), with the saddle between support rows 18 and 72 in its 135-row ordering. The original labels of these planes were 19 and 74.

**Construction-chart labels differ from freshly sorted exact vertex labels.** The subsequent patch uses the preserved vertex ordering in `mechanism/C622_chart/faces.json`. In that chart the bad vertex is 103, the outgoing endpoint is 114, the saddle-side quadrilateral is facet 18 with cycle **[69,97,114,103]**, and the adjacent facet is 72. The construction label 114 must not be mistaken for fresh exact C622_READY lexicographic label 112.

### Replace the whole saddle-side quadrilateral by a three-link escape

Two new construction vertices, **178 and 179**, lie exactly in the retained facet-72 supporting plane. Replace its boundary edge 103–114 by **103–178–179–114**. Remove quadrilateral facet 18 and insert these four outward triangles:

```text
[103,69,178]
[69,179,178]
[69,97,179]
[97,114,179]
```

This is the **second** triangulation option in the supplied `spiral_cap.construct`, selected by actual support clearance. The final exact face lists independently confirm it. No first-option triangulation or provisional label list is used as authority.

The operation adds two vertices, five true edges, and three maximal facets: **178/311/135 → 180/316/138**. Preserving the large adjacent facet as one exact plane is essential to the edge budget. The construction is not merely a subdivision of an old edge: the old edge disappears, new exposed facets enclose real added material, and the new complete maximal complex is rebuilt.

For discovery, project the old endpoints into this plane relative to its perpendicular foot from the prepared body's actual centroid. Their projected radii and angle were approximately

```text
rho0 = 0.41159131602742755
rho3 = 0.4150288930983309
phi  = 0.22140175713126464
```

Place intermediate angles at phi/3 and 2phi/3 and interpolate the radii logarithmically. The three-link ascent condition is

`(rho3/rho0)^(1/3) cos(phi/3) > 1`.

The observed excess was about **4.6673573161459814e-5**; all three discovery chord exits were about 0.00853752. Before the whole-body preparation, the analogous three-link condition was negative, about −0.00123086. Thus inserting two points into the earlier unprepared patch was not enough. Trigonometric quantities are only discovery inputs; **no trigonometric evaluation defines the final rational body**.

### The reference-centre cap was not homogeneous; actual moment closure was indispensable

The completed cap had numerical class110 at the prepared reference centre, but its own filled centroid moved by approximately

**(4.0232507552e-7, 9.8153230512e-6, −9.0838212939e-6)**.

At that new own centroid its numerical census was **(59,54,111)**. I did not promote that reference-centred cap.

I then solved the **three actual filled-centroid equations** in the full 319-free-coordinate contact chart, while retaining reference-centred exclusion inequalities and actual supporting geometry. The objective minimized material motion in a Cartesian-SVD-whitened metric. One accepted outer update, with nonlinear repairs, reduced the numerical centroid defect norm from **1.3379769854705618e-5** to **1.4031167972292188e-16**. Its first minimum-motion step had norm approximately **0.0004067370140685449**.

The resulting controls were rounded to the literal 10^14 grid, reconstructed rationally, and audited at their newly recomputed exact centroid. The final exact object—not the approximate moment root—is the winner.

The physical correction is genuinely distributed: comparison of the two exact endpoint H descriptions shows that **all 134 retained supports changed**, and the only exactly unchanged raw vertex between C622_READY and the final winner is the apex (0,0,1). The final volume is about **1.3177912001126215e-6 smaller** than C622_READY's. This was neither fixed density on a surface nor a fictitious polar-centroid correction, and total volume was not assumed preserved.

## 3. The complete remaining closure is gone

In the **final exact raw lexicographic order**, the replacement true-edge route is

**103 → 107 → 110 → 114**.

The respective complete facet-owner sets are

```text
103: [57,71,134]
107: [71,134,135]
110: [71,135,136,137]
114: [17,71,137]
```

For `eta(i,j)=(p_i-g)·(p_j-p_i)/|p_j-p_i|²`, exact rational calculation gives

```text
floor(10^9 eta(103,107)) = 5826449
floor(10^9 eta(107,110)) = 6118904
floor(10^9 eta(110,114)) = 5879471
```

All three are strictly positive; all three links are genuine boundary edges. One exactly checked continuation from this strip to the apex is

```text
103,107,110,114,117,120,123,127,132,137,149,150,151,153,
154,155,156,157,159,161,162,164,165,167,169,170,172,174,
177,179,178,176,175,173,171,168,166,163,160,158,104,98
```

More importantly, `endpoint_stats.py` reconstructs a **complete true-edge primal escape forest rooted at 98**, and a **complete adjacent-facet polar escape forest rooted at 3**. Every parent chain reaches its root. Their maximum depths are 94 and 75. For the selected relative radial exit `z_i·(z_parent−z_i)/|z_i|²`, the exact floors of 10^12 times the minimum are **670 physically** and **632 polarly**. Here the polar vectors are `q_i/(1−q_i·g)`, representing the centred physical body's supports; no assertion about the polar's own volume centroid is made.

These forests address the complete outgoing basin, not just the old U label. They supplement—not replace—the exhaustive full edge-cone census.

A useful false-merit-resistant identity used in this direction is

`sum_cycle eta(i,j)|z_j−z_i|² = −(1/2)sum_cycle|z_j−z_i|²`.

Thus a collapsing closed witness cycle cannot make all its chord-normalized exits approach zero: at least one is at most −1/2. This improves diagnosis of the journal's shrinking-cycle failure, but the actual success here came from a new three-link physical patch plus full mass closure, not from a residual score alone. The older journal explicitly warns that small shrinking-edge residuals and finite guarded-forest attempts did not prove cancellation.

## 4. Exact definition, filled moments and arithmetic cost

The complete defining `objects/C632_WINNER/GENERATOR.json` has **12,964 bytes**, SHA-256

`5078c5ca7efa595074368e3a456dc8697407fe95c3ae7e697e1f9a41ee171da5`.

It contains every integer control, every ordered contact solve, every coordinate-axis selection, and every prescribed contact group. There are 138 support nodes and 43 represented nonsimple-point nodes. The grid is **10^14**. Initialize the control vectors exactly, fix node 138 to (0,0,1), and follow the entire plan, solving `X_j·X_i=1` for the stated dependent axes. The first 138 resulting vectors q_i define the filled intersection

**K = {x : q_i·x ≤ 1 for every i}.**

The remaining contact nodes are geometric construction variables, **not masses**. `RECONSTRUCT.py` verifies all prescribed incidences and reduces every H row to primitive integers. Both checkers then independently enumerate the actual maximal complex.

For the reconstructed raw vertices p_i and outward canonical facet-fan triangles, define the exact rational sums

```text
Delta = sum det(p_a,p_b,p_c)
L     = sum det(p_a,p_b,p_c) (p_a+p_b+p_c)
W     = Delta/6
M     = L/24
g     = L/(4 Delta)
final vertex i = p_i-g.
```

Together with the complete literal generator and the included exact algorithms, these are finite exact definitions of the full volume, all three first moments, and every centred coordinate. The programs emit their entire reduced fractions in A.json and B.json; none is replaced by a floating centroid or a checksum-only reference.

Display approximations from those exact outputs are

```text
W = 0.48866257753902004
M = (-0.006259658127330545,
      0.0029128371717480755,
     -0.004500171822649659)
g = (-0.012809775937529628,
      0.005960835360910123,
     -0.009209159918308493).
```

The final centred first moments are **exactly (0,0,0)**. A third integration, `centred_mass.py`, builds an exact common-denominator centred integer table, uses a different fan anchor, integrates **356 positive tetrahedra**, and directly obtains zero integer first-moment numerators and the same volume.

Maximum individual numerator-or-denominator bit lengths are:

| Exact body | Primitive plane coefficients | Raw vertex coordinate | Raw centroid coordinate | Final centred coordinate |
|---|---:|---:|---:|---:|
| C622_DISK | 337 | 706 | 65,133 | 65,139 |
| C622_READY | 396 | 830 | 79,861 | 79,865 |
| **C632_WINNER** | **382** | **808** | **78,803** | **78,806** |

For the winner, the volume costs at most **39,485 bits**, and raw first moments at most **78,804 bits**. A common-centred-denominator export uses **78,869 bits**. This improves mechanical complexity, **not every arithmetic metric**. The control grid is not the final coordinate bit length and is not a manufacturing tolerance.

## 5. Full maximal-complex and mechanical evidence

**Implementation A** exhausts all **428,536 support triples**, checking their intersections against all halfspaces; proves boundedness through six normal-cone certificates; builds every maximal convex polygon; derives actual true edges; and integrates origin-based tetrahedra. It checks vertices against all other vertices and uses Gram formulas for edge-normal coefficients.

**Implementation B** independently clips all **9,453 plane-pair lines** against all halfspaces; rebuilds vertices, maximal polygon cycles and true edges by different code; and integrates using a different strict interior point and different fan anchors. It checks vertex mechanics through true neighbours as well as globally, and uses cross/Cramer formulas for edge-normal coefficients. Neither checker imports the other's geometry, moments or mechanics.

For every true edge, both endpoint line-foot inequalities and both incident-normal-cone coefficients are tested. Every face foot is tested against every true polygon side; every complete vertex cone, including nonsimple cones, is classified. Weak equilibria are tested separately, not inferred from strict counts.

The actual final ledger contains **632 face-side signs**, **32,220 ordered all-vertex radial-support comparisons**, and **1,264 true-edge primitive signs**. There are zero face-side primitive zeros, zero vertex maximum-exit zeros, zero true-edge primitive zeros, and no weak equilibria. The normalized complete A/B records are byte-identical: **424,620 bytes each**, SHA-256

`8efd0cdab878c395f8af85ae320869590d6707ff062e70920e448779fa0e2c9b`.

True facet sizes are **53 triangles, 28 quadrilaterals, 28 pentagons, 11 hexagons, 10 heptagons, 3 octagons, 2 nonagons, one decagon, one 13-gon and one 20-gon**. Vertex degrees are **137 of degree 3, 36 of degree 4, 4 of degree 5, one each of degrees 6, 7 and 44**. Integration triangulation has 356 triangles and 534 triangulation edges; **218 diagonals are not true edges**. The actual Euler check is 180−316+138=2, not the proof of H=0.

The unique stable 20-gon has final raw-vertex cycle

```text
[64,104,158,160,163,166,168,171,173,175,
 170,169,156,155,154,132,127,123,97,69].
```

A fresh directory was populated **only by decoding the complete capsule below**. A, B and the finalization stage actually completed, yielding `BQ13_EXACT_TWO_IMPLEMENTATION_REPLAY_PASS`; the direct centred integer integration also passed. The final source manifest checked 36 payload files. Earlier combined tool invocations stopped at the execution-window limit after A/B; they were not counted as completed pipeline receipts. The later three-stage cold replay finished completely.

A further exact raw translation by **(1,−2,3)/2^30** was independently rebuilt and checked by both implementations. Exact recentering reproduced every original centred vertex; `BQ13_EXACT_TRANSLATION_REPLAY_PASS` completed. The positive/negative fixture suite includes a regular tetrahedron with strict446/weak000 and a triangular prism with **strict446 and additional weak123**, exercising the weak predicates nonvacuously. Both are rejected by the winner gate.

## 6. Reproduction, finite scope and continuation

Exact replay needs **only Python's standard library**. Do not use `-O`. In the tested environment Python was 3.13.5. Numerical discovery additionally used **NumPy 2.3.5, SciPy 1.17.0, OPENBLAS_NUM_THREADS=1**.

After restoring the capsule to `BQ13`, run:

```bash
python -S BQ13/REPLAY.py --object C632_WINNER --out WINNER --phase A
python -S BQ13/REPLAY.py --object C632_WINNER --out WINNER --phase B
python -S BQ13/REPLAY.py --object C632_WINNER --out WINNER --phase finish
```

`WINNER` must initially be absent. The phases are the same replay as the unpartitioned default. To audit the retained nonwinners, change `--object` to C630_START, C622_DISK or C622_READY and use separate output directories. C622_DISK's generator is followed by its complete literal support-deletion list [17,21]. Their expected exact record hashes and censuses are in OBJECTS.json.

The numerical mechanism is also fully recoverable:

```bash
OPENBLAS_NUM_THREADS=1 python BQ13/mechanism/REPROPOSE.py
```

I actually executed this portable command. It reconstructed the cap seed byte-for-byte from the frozen C622_READY checkpoint, reran the guarded full-moment correction, and reproduced the **entire exact winner generator byte-for-byte**, ending `BQ13_COMPLETE_CAP_AND_MASS_REPROPOSAL_BYTE_IDENTICAL`. The frozen generator remains authoritative if another numerical environment proposes different bytes. The complete source units, helper dependencies, exact checkpoints and portability patches are all in the capsule; the numerical optimizer is not needed to define or verify the winner.

The mathematical result is an **exact endpoint construction with completed independent software checks within this research**. It is not external human peer review, a proof-assistant certificate, a global minimum proof, or a production-tolerance guarantee. I have **not** certified a no-birth continuum chronology along every parameter segment from C630. The completed final exhaustive census, rather than an unproved path claim, establishes the net removal of the entire unwanted U/H closure.

For continuation, use **C632_WINNER as the new finite baseline**: no residual U/H pair remains. One concrete new reduction wall is coplanarity across final edge **(69,110)**, between facets **135 and 136**, potentially merging those two cap triangles. This is an unexecuted next target, not another claimed winner. It must be approached with its actual support guards, full filled moments, rooted escape forests and rebuilt true complex. Do not continue to optimize the obsolete C630 U105/H(105,111) labels or impose the old H213 requirement.

## 7. Supplemental files and complete textual recovery

Complete verified data, exact raw/centred tables, both checkers and actual receipts (`BQ13_C632_VERIFIED_FULL.zip`) — **8,439,215 bytes**, SHA-256 `ee655d1b3d6a3f67343d7813f8e9d01671fb189165688f684548bf01835b0593`.

Small source-only portable archive (`BQ13_C632_SOURCE_ONLY.zip`) — **95,907 bytes**, SHA-256 `23278c4b4740139abbddc820c6dcecf2044c61cc908ef11d0587295ed7e64c0b`.

Complete Markdown handoff (`BQ13_RESULT_MARKDOWN.md`) and complete v2 JSON handoff (`BQ13_RESULT_v2.json`) are also present as supplemental copies.

Both archive byte sets were inspected and their complete internal manifests checked. The full bundle also includes an exact centred common-integer coordinate table with rational readback, all true maximal face cycles and edges, full exact mass fractions, and a separately labelled display-only OBJ. These archives supplement the complete defining capsule below.

The capsule is a **37-file UTF-8 JSON source map**, compressed with LZMA/XZ and encoded with Python base85. After removing whitespace it has exactly **63,500 characters**, SHA-256 **`fd17b83e231c8e9b3f4ef4dbc9acceeee583a414235012e8b8f0ff9c9e848b1f`**. Its decoded JSON has **223,423 bytes**, SHA-256 **`e0d7ce4dea29c19075bc37fe667f005d186644296b618be5340c1437b020ea2a`**. It includes every defining rational control for all four exact endpoints, all reconstruction and verification code, and the complete successful numerical mechanism with its inputs.

Save this Markdown handoff as `result.md` and the following complete decoder as `restore.py`, then run `python restore.py result.md BQ13`:

```python
import base64, hashlib, json, lzma, sys
from pathlib import Path
md = Path(sys.argv[1]).read_text(encoding='utf-8')
encoded = md.split('\nBEGIN_BQ13_CAPSULE\n', 1)[1].split('\nEND_BQ13_CAPSULE\n', 1)[0]
encoded = ''.join(encoded.split())
assert len(encoded) == 63500
assert hashlib.sha256(encoded.encode()).hexdigest() == 'fd17b83e231c8e9b3f4ef4dbc9acceeee583a414235012e8b8f0ff9c9e848b1f'
raw = lzma.decompress(base64.b85decode(encoded))
assert len(raw) == 223423
assert hashlib.sha256(raw).hexdigest() == 'e0d7ce4dea29c19075bc37fe667f005d186644296b618be5340c1437b020ea2a'
files = json.loads(raw)
assert len(files) == 37
root = Path(sys.argv[2])
root.mkdir(parents=True, exist_ok=False)
for name, text in files.items():
    relative = Path(name)
    assert not relative.is_absolute() and '..' not in relative.parts
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode('utf-8'))
for name, expected in json.loads((root/'SOURCE_MANIFEST.json').read_text()).items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest() == expected
print('BQ13_COMPLETE_SOURCE_CAPSULE_RESTORED')
```


[Encoded source block omitted; the code in this passage is incomplete.]
