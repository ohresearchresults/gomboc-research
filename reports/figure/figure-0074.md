# figure-0074

AI research report · 2026-08-26 UTC

---

# Complete research handoff — coupled two-region continuation from exact body B

## Verdict

**No homogeneous convex polyhedral Gömböc was found in this branch, and I do not claim `(S,U,H)=(1,1,0)`.**

The strongest finite result is an exact rational 11-vertex endpoint **X** that crosses the two residual Morse blocks simultaneously. Relative to an exact pre-crossing state M, all four selected defect witnesses acquire the desired strict sign at the body's own uniform-volume centroid:

- extra stable face `(0,3,2)` becomes nonstable;
- extra unstable negative-cap vertex `V1` becomes nonunstable;
- saddle `(0,3)` becomes nonsaddle;
- saddle `(1,2)` becomes nonsaddle.

However, complete reconstruction shows a fourfold **transfer**, not cancellation:

- stable face transfers to `(0,2,10)`;
- unstable vertex transfers to `V8`;
- saddles transfer to `(0,7)` and `(2,6)`.

Thus X remains strictly `(S,U,H)=(2,2,2)`. This is not a transfer-wall sample: X has rational coordinates, exact volume and centroid, exact zero centered first moments, positive inactive-incidence separation, a complete H/V representation, an independent V-only verifier, OBJ/STL exports, and a nonzero exact rational perturbation box preserving every feature sign.

## Paired architecture

Starting from B, I deleted old `V2`, retained old vertices `[0,1,3,4,5,6,7]`, inserted independent truncation points on old edges `(2,0),(2,1),(2,3)`, inserted a nonradial stack actuator over old `F04=(0,4,3)`, and coupled the shape to a rational positive-determinant linear metric. New labels are

```text
new 0..6 = old [0,1,3,4,5,6,7]
new 7     = cut on old (2,0)
new 8     = cut on old (2,1)
new 9     = cut on old (2,3)
new 10    = stack actuator over old F04
```

The retained target stable face is `(1,4,3)` and retained target unstable vertex is `V6`. Every accepted numerical state rebuilt the actual convex hull and recomputed its uniform-volume centroid before evaluating maximal faces, full vertex normal cones and true-edge two-normal cones.

# Exact endpoint X

## Exact rational V-representation

The following are uncentered coordinates; the mechanical coordinates are obtained by subtracting the exact centroid below.

```text
0  (-8325794604513/10000000000000,
     29846474793/5000000000000,
     13214362629/2000000000000)
1  (-257067853849971/10000000000000,
    -6987123489/5000000000000,
     20198907883/5000000000000)
2  (-416410257243/500000000000,
    -5356298923/2000000000000,
    -9411474863/2000000000000)
3  (9157304590573/400000000000,
    9174010281/2000000000000,
    2645780329/1000000000000)
4  (58052803369953/10000000000000,
    -92479199/25000000000,
    -8517299749/2500000000000)
5  (-8093770712813/5000000000000,
    -1683227467/625000000000,
    -265412423/62500000000)
6  (64997558808779/2500000000000,
    -3042591067/2000000000000,
    -27331476487/5000000000000)
7  (-123813769709901/5000000000000,
     16037615287/10000000000000,
     46126581931/10000000000000)
8  (-257067854003603/10000000000000,
    -10845119431/10000000000000,
     10239452799/2500000000000)
9  (-9294133502307/625000000000,
    -908801329/2500000000000,
     2538940227/5000000000000)
10 (-47378143330979/10000000000000,
    -2805126829/2500000000000,
    -4602400337/2000000000000)
```

## Exact volume, centroid and three-moment closure

```text
Volume =
820429548426377772852259148265670651 /
1500000000000000000000000000000000000000
≈ 0.00054695303228425186

Centroid C =
(-54656350515551878839131074638814171506768351011797 /
  65634363874110221828180731861253652080000000000000,

  37935965616048995687530237968269600380919688141 /
  131268727748220443656361463722507304160000000000000,

  21206642541209401897272942426269009964822342079 /
  32817181937055110914090365930626826040000000000000)
```

The exact V-only reconstructor builds 18 positive tetrahedra from a rational interior point and independently integrates the oriented boundary. Volume and all three first moments agree exactly. With `x_i=q_i-C`, the three centered first-moment numerators are exactly `(0,0,0)`.

## Actual maximal faces and true edges

`(V,E,F)=(11,27,18)` and Euler characteristic is `2`.

```text
Maximal faces:
F00 (1,3,0)    F01 (8,1,0)    F02 (0,3,2)
F03 (0,2,10)   F04 (7,8,0)    F05 (7,0,10)
F06 (2,5,1)    F07 (1,9,2)    F08 (4,3,1)
F09 (5,4,1)    F10 (8,9,1)    F11 (3,6,2)
F12 (5,2,4)    F13 (2,6,4)    F14 (9,10,2)
F15 (4,6,3)    F16 (7,9,8)    F17 (7,10,9)

True edges:
(0,1) (0,2) (0,3) (0,7) (0,8) (0,10)
(1,2) (1,3) (1,4) (1,5) (1,8) (1,9)
(2,3) (2,4) (2,5) (2,6) (2,9) (2,10)
(3,4) (3,6) (4,5) (4,6)
(7,8) (7,9) (7,10) (8,9) (9,10)
```

The complete exact centered H-representation is materialized as primitive integer rows `A x+B y+C z≤D` in `halfspaces_centered_integer.csv`. The independent verifier reconstructs the same 18 maximal faces and 27 true edges from V-data without trusting the declaration or mesh.

## Exhaustive own-centroid class

Feature margins use the complete maximal polygon, every true neighbor of a vertex, and both incident outward normals of each true edge. The full exact fraction and directed-rounding tables contain every individual primitive.

```text
Stable faces:
(0,2,10)  +[4.229977390220537492141227E-7,
             4.229977390220537492141227E-7]
(4,3,1)   +[5.595921905077143511196708E-5,
             5.595921905077143511196708E-5]

Unstable vertices:
V6  limiting neighbor 3
    +[9.999953543263795315182048E-1,
       9.999953543263795315182048E-1]
V8  limiting neighbor 1
    +[1.840529286496933265348541E-5,
       1.840529286496933265348541E-5]

Saddle edges:
(0,7), limiting primitive t
    +[6.766582010313336599025690E-6,
       6.766582010313336599025690E-6]
(2,6), limiting primitive t
    +[3.005303855276192397677695E-6,
       3.005303855276192397677695E-6]
```

Every other maximal face, vertex and true edge has a strictly negative limiting primitive. The full report prints all 18 face, 11 vertex and 27 edge feature margins; `face_primitives.csv`, `vertex_primitives.csv` and `edge_primitives.csv` give every constituent raw exact primitive. Therefore

```text
(S,U,H)=(2,2,2),   S+U-H=2.
```

The minimum inactive support separation divided by body diameter is

```text
[2.602077387108479430313086E-8,
 2.602077387108479430313086E-8].
```

## Certified boxes

Exact rational interval arithmetic, with the volume centroid recomputed over the whole coordinate box, certifies:

1. `||δ||∞≤1/10^15` independently for all 33 uncentered coordinate components preserves the same 18 faces, 27 edges and every individual feature sign; the class is identically `(2,2,2)` throughout this box.
2. `||δ||∞≤1/10^8` preserves the hull, target `V6` remains unstable, all nonmutual supports at `V1,V8` remain positive, and edge `(1,8)` remains true. Hence every body in this larger box has `U≥2` and is not a Gömböc.

## Exact obstruction isolated by the crossing

For centered positions `x1,x8` on the true edge `(1,8)`, put `d=x8-x1` and

```text
a=-x1·d,
b=-x8·(-d).
```

Then identically

```text
a+b=||x8-x1||²>0.
```

At X,

```text
a =
-58390312660042913671236202198598799424706808983131562361 /
1312687277482204436563614637225073041600000000000000000000000000

b =
191037809815361293499454576019398162748183880736312682089 /
1312687277482204436563614637225073041600000000000000000000000000

a+b = ||x8-x1||² =
10105034110617913533/100000000000000000000000000.
```

All nonmutual supports at both `V1` and `V8` are exact positive fractions. Since the two mutual supports cannot both be nonpositive, one of `V1,V8` is necessarily unstable. Together with independently unstable target `V6`, this proves `U≥2` throughout the corresponding semialgebraic sign cell. A continuation must therefore remove/deactivate edge `(1,8)` or change a nonmutual support sign; merely pushing farther through the mutual transfer wall cannot work.

# Exact simultaneous transfer M → X

M and X have the same 11-vertex simplicial incidence. The following exact directed intervals show that all selected old witnesses are killed while adjacent replacements are born:

```text
old stable face (0,3,2):
 M +3.416377096763623725559352E-7
 X -4.229590065457426431957093E-7
new stable face (0,2,10):
 M -3.415939168691444605050925E-7
 X +4.229977390220537492141227E-7

old unstable support V1→V8:
 M +1.278867117288931228348917E-5
 X -5.625539814285621562826492E-6
new unstable support V8→V1:
 M -1.566245163078995901657282E-9
 X +1.840529286496933265348541E-5

old saddle (0,3), t:
 M +4.194903638399231045565987E-6
 X -6.704343726529584839782190E-6
new saddle (0,7), t:
 M -4.039675075549174023171742E-6
 X +6.766582010313336599025690E-6

old saddle (1,2), 1-t:
 M +1.763202630665523534082203E-6
 X -3.161021100067370545761908E-6
new saddle (2,6), t:
 M -1.559580457986528312337118E-6
 X +3.005303855276192397677695E-6
```

This is the central new finding: the requested coupled crossing is geometrically realizable with exact centroid closure, but in this cell it is a coordinated transfer of four equilibria rather than two cancellations.

# Materialized topology-changing endpoints

Six rational bodies were rebuilt independently; all have exact centered first moments `(0,0,0)` and exact class `(2,2,2)`.

| Endpoint | Cell/architecture | `(V,E,F)` | Minimum inactive separation / diameter |
|---|---|---:|---:|
| J | paired truncation plus stack; two exact quadrilateral circuit faces | `(11,25,16)` | `1.7528158796687439E-7` |
| O | adjacent mixed circuit triangulation | `(11,27,18)` | `1.8814306715162601E-8` |
| M | exact pre-cross simplicial cell | `(11,27,18)` | `3.2338051607759776E-10` |
| X | same incidence after four-witness mechanics crossing | `(11,27,18)` | `2.6020773871084794E-8` |
| W | stack-side circuit crossed; edge `(0,2)` replaced by `(3,10)` | `(11,27,18)` | `1.4155267686163950E-8` |
| D | independent connected 12-vertex six-cut double bridge with five maximal quads | `(12,25,15)` | `2.0631259509733719E-6` |

The exact circuit map is:

- J has maximal quads `(8,1,0,7)` and `(1,8,9,2)`.
- O resolves them with diagonals `(1,7)` and `(2,8)`.
- M resolves them with diagonals `(0,8)` and `(1,9)`.
- X retains M's incidence but reverses all four chosen mechanics witnesses.
- W crosses the stack-side circuit, replacing faces `(0,3,2),(0,2,10)` by `(0,3,10),(3,2,10)` and edge `(0,2)` by `(3,10)`.
- D is a separate 12-vertex connected replacement patch, not a perturbation of the J/M circuit complex. It is the most robust topology-changing fallback, but still has two stable faces, two unstable vertices and two saddles.

Eight additional sampled offset-cell signatures—with complete numerical maximal-face cycles, true-edge lists, centroids and equilibrium sets—are preserved in `observed_circuit_cells.json`; all eight were `(2,2,2)`. Only the rationalized endpoints above are used as exact evidence.

# Search performed

The branch explored:

- paired three-edge truncation plus a nonradial stack actuator, with and without deactivation;
- a five-parameter determinant-one metric coupled to the shape variables;
- four independent transverse offsets spanning adjacent circuit cells;
- all-coordinate fixed-cell branch optimization, linearized separator branches and deliberate simultaneous wall crossing;
- temporary `(2,3,3)` states and controlled topology changes;
- an independent six-cut 12-vertex connected double bridge;
- 30,000 one-apex/circuit-ray samples, producing 27 observed topology signatures and no target;
- 5,000 broad spherical bridge samples, 10,000 focused large-transverse negative-cap samples and 3,000 thin negative-cap bridge samples. The thin sweep produced 2,998 valid added-vertex hulls over classes including `(2,2,2)`, `(3,2,3)`, `(4,2,4)` and `(2,3,3)`, with no `(1,1,0)` state.

These searches are empirical evidence only. Exact closure is claimed solely for the rational endpoints, the two X interval boxes and the common-edge semialgebraic obstruction.

# Closed subfamilies and remaining uncertainty

Exactly closed here:

1. the full-class X box `||δ||∞≤10^-15`, identically `(2,2,2)`;
2. the larger X box `||δ||∞≤10^-8`, with exact `U≥2`;
3. the common-edge sign cell retaining edge `(1,8)`, positive nonmutual supports at `V1,V8`, and unstable target `V6`;
4. all six rational endpoints J/O/M/X/W/D, including full hull, moment and all-feature audits;
5. the predecessor isolated one-height family over seed A, whose full `0<u<1` cell remains exactly excluded by two persistent stable faces.

Still open:

- the complete nonlinear realization spaces of the J/O/M/W complex outside the certified boxes;
- paired replacements that deactivate `(1,8)` while keeping both replacement vertices nonunstable;
- longer increasing-radius rails or bifurcated patches with more than the sampled 12 vertices;
- arbitrary bistellar sequences and nonsimplicial cells;
- the global existence question.

The strongest continuation is a connected asymmetric patch that spends its topology budget on deleting edge `(1,8)` and supplying both negative-cap endpoints with independent larger-radius witnesses, while simultaneously replacing the stack-side transfer strip `(0,3,2)↔(0,2,10)` and `(0,3)↔(0,7)`. Another one-face height or isolated apex actuator is structurally redundant.

# Reproducibility and artifacts

- [Complete coupled-research bundle ZIP](sandbox:/mnt/data/paired_B_coupled_research_bundle.zip)
- [Full standalone report](sandbox:/mnt/data/paired_B_coupled_research_REPORT.md)
- [ZIP SHA-256 record](sandbox:/mnt/data/paired_B_coupled_research_bundle.zip.sha256)
- [Combined verifier transcript](sandbox:/mnt/data/paired_B_coupled_research_bundle/RUN_ALL_VERIFIERS.txt)
- [Bundle SHA-256 manifest](sandbox:/mnt/data/paired_B_coupled_research_bundle/SHA256SUMS.txt)

Strongest exact endpoint X:

- [candidate.json](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/candidate.json)
- [verified_summary.json](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/verified_summary.json)
- [exact V-only verifier](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/verify_exact.py)
- [independent exact verifier](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/verify_independent.py)
- [exact interval-box verifier](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/verify_interval_boxes.py)
- [interval certificate transcript](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/verify_interval_boxes.txt)
- [exact centered H-representation](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/halfspaces_centered_integer.csv)
- [all face primitives](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/face_primitives.csv)
- [all vertex primitives](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/vertex_primitives.csv)
- [all edge primitives](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/edge_primitives.csv)
- [all inactive incidences](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/inactive_incidence.csv)
- [OBJ](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/body.obj)
- [STL](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_X_codimension4_transfer/body.stl)
- [exact M→X transfer table](sandbox:/mnt/data/paired_B_coupled_research_bundle/critical_transfer_table.csv)

Independent 12-vertex endpoint D:

- [candidate.json](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_D_connected_double_bridge/candidate.json)
- [verified_summary.json](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_D_connected_double_bridge/verified_summary.json)
- [OBJ](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_D_connected_double_bridge/body.obj)
- [STL](sandbox:/mnt/data/paired_B_coupled_research_bundle/endpoint_D_connected_double_bridge/body.stl)

Run from the extracted bundle root:

```bash
bash RUN_ALL_VERIFIERS.sh
```

A fresh ZIP extraction passed all 195 manifest hashes and every exact, independent, interval and symbolic verifier. The final ZIP SHA-256 is

```text
c5667ad4d11191e60d13785c11f78d70b8f8dbf704a73bc9dd4daaf55ee1d06b
```
