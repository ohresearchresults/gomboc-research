# figure-0134

AI research report · 2026-08-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Research handoff: M42 minimal 13-face/two-rail continuation

The run's acceptance gate is still a finite homogeneous convex polyhedron evaluated at its own exact uniform-volume centroid with strict `(S,U,H)=(1,1,0)`, complete actual H/V incidence, positive full-feature margins, independent verification, and OBJ/STL. The immediate inherited M42 frontier was the exact 47-vertex two-cell bridge whose defect had transferred to structural edge `(64,68)`, with the minimal 13-face/two-rail continuation explicitly identified.

## What changed relative to the supplied journal

I realized and exactified that full 13-face communicating topology. It deletes `(64,68)`, deactivates vertex 68, removes stable face `[57,79,78]`, and removes saddles `(4,60)` and `(49,73)`. The inherited features do not vanish on one shared scalar wall; they disappear over a rigorously reconstructed communicating multiwall sequence. The final exact cell is a strict `(2,2,2)` nonwinner with a new whole-cell obstruction on true edge `(82,83)`.

## Literal verdict

No winner. A full graph-theoretically minimal 13-face communicating two-rail zipper was materialized and exactified. It removes every inherited defect feature named in the assignment, but the Euler-neutral block transfers to a new open `(2,2,2)` cell with an exact external-positive true-edge obstruction `(82,83)`.

## Exact endpoint

- input construction rows: 95;
- active vertices: 50;
- true edges: 130;
- maximal faces: 82;
- complexity: 260;
- exact volume: `29660212239700434054468102012003421577/6000000000000000000000000000000000000` (`4.9433687066167389`);
- unshifted exact centroid: `31583290850654892631932549247646225220082395155411/118640848958801736217872408048013686308000000000000, -6688580900932650473570308945472520977944616049267/7415053059925108513617025503000855394250000000000, -19234811323075247274675565450830139622653009224807/59320424479400868108936204024006843154000000000000`;
- strict own-centroid class: `(2,2,2)`;
- stable faces: protected 17-gon and `[76,89,77]`;
- unstable vertices: protected `8` and `82`;
- saddles: `(5,87)` and `(49,94)`.

All three first moments after exact translation are identically zero. The complete face, vertex and four-component true-edge audits are in the machine-readable ledgers.

## Topology achieved

Rows `82..88` are stacked over the seven terminal-to-right face cells and rows `89..94` over the six northern-stable-to-left cells. Every one of the 13 rows is extreme. The two rails communicate through the surviving predecessor network: row 65 is incident to new vertices on both rails, while rows 76 and 80 close the northern branch. This is not a serial cap or two disconnected chains.

The final active old rows are `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 49, 54, 58, 59, 60, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 73, 76, 77, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]`. Relative to the 47-vertex predecessor, rows `[43, 50, 53, 57, 61, 68, 74, 75, 78, 79]` deactivate. Specifically:

- edge `(64,68)` is absent;
- vertex `68` is strictly inactive;
- rows `57,78,79` are inactive, so face `[57,79,78]` is absent;
- edges `(4,60)` and `(49,73)` are absent.

The natural simultaneous-depth homotopy crosses a communicating multiwall sequence. By `lambda in (0.40845,0.40947)` all inherited mechanical features have disappeared and the class has returned to `(2,2,2)`; later incidence events deactivate rows 53,61,79,78,68. The exact endpoint is well inside the final cell.

### Authoritative added coordinates

All decimals below are exact terminating rationals on the common `10^12` lattice.

```text
82  ( 1.261202265092,-3.045098444606,-0.561499453060)
83  ( 1.400414374657,-2.924098088468,-0.390261087541)
84  ( 1.157055192309,-2.908409861838,-0.268987806997)
85  ( 1.380283725881,-2.529363550180,-0.232108977446)
86  ( 1.394845036609,-2.230503834345,-0.129426879826)
87  ( 1.731342490190,-1.563416843657,-0.136679184761)
88  ( 1.525520476293,-0.817094074584,-0.015928932936)
89  ( 0.010481522569,-0.418385324575,-0.797953771971)
90  (-0.051674851818,-1.054792101851,-0.858225970515)
91  (-0.351381425285,-1.072410036675,-0.882989004538)
92  (-0.403231873135,-1.874776815043,-0.733868180893)
93  (-0.867999539401,-1.260164591783,-0.396413415423)
94  (-1.021490415121,-1.214482835874,-0.236213709860)
```

`generate_exact_coordinates.py` reconstructs the complete 95-row source lattice from the 82-row predecessor plus these 13 rows, evaluates the signed-tetrahedron volume and three first moments exactly, substitutes the dependent translation `tau=-M/V`, and regenerates the exact centred active coordinates.

## Complete actual-cell atlas

The natural simultaneous-depth path did **not** coalesce the two Morse cancellations and all row deactivations onto one codimension-three wall. It nevertheless realizes the full 13-cell communicating topology and crosses every inherited obstruction. `topology_event_atlas.json` gives, for 15 rational representative values of `lambda`, the exact volume and centroid, zero centred moments, complete maximal-face cycles, complete true-edge list, active/inactive row partition and exhaustive `(S,U,H)` audit. `topology_event_summary.csv` is the compact ledger. The principal open cells are:

```text
lambda       (V,E,F,C)       class     newly inactive / mechanical state
0.034000     (60,160,102,320) (2,2,2)   all 13 new rows active; inherited block remains
0.096170     (59,157,100,314) (2,2,2)   57 inactive; stable lineage on 89
0.136705     (59,157,100,314) (2,2,2)   edge (64,68) already absent
0.209270     (58,154, 98,308) (2,2,2)   50 inactive
0.274835     (57,151, 96,302) (2,3,3)   74 inactive; right transfer through (68,82)
0.300860     (56,148, 94,296) (2,3,3)   43 inactive
0.346900     (55,145, 92,290) (3,3,4)   75 inactive; both replacement stars communicate
0.390940     (55,145, 92,290) (2,3,3)   old left saddle gone; new saddle (49,94)
0.412965     (55,145, 92,290) (2,2,2)   vertex 68 no longer unstable; all inherited equilibria gone
0.480525     (54,142, 90,284) (2,2,2)   53 inactive
0.560600     (53,139, 88,278) (2,2,2)   61 inactive
0.739260     (52,136, 86,272) (2,2,2)   79 inactive
0.934440     (51,133, 84,266) (2,2,2)   78 inactive
0.983990     (50,130, 82,260) (2,2,2)   68 inactive; final incidence cell reached
1.000000     (50,130, 82,260) (2,2,2)   exact certified endpoint
```

Thus the assignment's named old features are all destroyed, but not on one shared scalar wall. The strongest exact conclusion is the whole final incidence/external-sign-cell obstruction below.

## Transferred exact obstruction

For centered coordinates let `sigma(i->j)=-x_i·(x_j-x_i)`. Edge `(82,83)` is true. Every support from either endpoint to a neighbor outside the pair is positive. The smallest external raw support is `0.31574698292496456`. The mutual supports are

- `sigma(82->83)=19151364196859896969771270350153749566689904863603410897135717/118640848958801736217872408048013686308000000000000000000000000 > 0`,
- `sigma(83->82)=-11636216764034118179172323854657864237806291675864101370637677/118640848958801736217872408048013686308000000000000000000000000 < 0`,

and exactly

`σ(82→83)+σ(83→82)=||x83-x82||²=6334367546067904690363/100000000000000000000000>0`.

Thus, while the realized incidence and all external-positive signs persist, at least one endpoint remains unstable. Vertex 8 is independently unstable; therefore the whole certified cell has `U>=2`. This is a cell theorem, not merely an unsuccessful search trace.

## Strict margins and perturbation

Directed normalized endpoint margins include:

```text
stable positive             0.047980466920648106
nonstable exclusion         0.03724326329345648
unstable positive           0.64137767628441855
nonunstable exclusion       0.037268908780414202
saddle positive             0.37131655232924626
nonsaddle exclusion         0.037268908780414209
all-input incidence         8.1195360721465553e-05
inactive boundary gap       0.0028122892
```

Rows `0..16` are fixed to retain the single 17-gon. Every coordinate of every other active row—99 independent coordinates—may vary by `±1e-11`. Outward interval arithmetic preserves the complete incidence, all inactive rows, class `(2,2,2)`, deletion of every inherited feature, and the obstruction `(82,83)` throughout this box.

## Attempts to break the endpoint

A full 39-coordinate evolutionary search around and well beyond this cell was run with complete own-centroid face/vertex/edge scoring. It improved the global no-extra-equilibrium hard score from about `-0.6414` to about `-0.2085`, but every best actual hull retained a transferred Euler-neutral block; no strict `(1,1,0)` state appeared. A directed one-parameter relay moves the extra maximum `82→83→84→85`; at each transfer the edge identity produces a temporary or persistent U-H-U relay, and the terminal state still cannot drain to the protected maximum without a new topology. These searches are empirical support only; the exact nonwinner conclusion rests on `(82,83)`.

## Smallest next topology

The minimal 13-face surface zipper is now exhausted in its realized cell. The next nonrepeating topology must destroy `(82,83)` while crossing both residual cancellation pairs together. The smallest exposed replacement is a finite-thickness third rail / genuine 3D two-cell sharing a volume cell between:

1. the terminal star of `82,83,62,64,67,69` and right saddle star `5,87,4,60,86,88`; and
2. stable star `76,77,89,80,90,91` and left saddle star `49,94,13,71,72,92,93`.

It should permit at least `82,83,76,77,87,89,94` and obsolete old rows `49,60,62,64,65,67,69,71,72,80` to deactivate in one circuit-scale event, add two transverse closure bands rather than another surface-only rail, and retain all three ordinary moments as dependent hard equations. The first gate is deletion/deactivation of both endpoints of `(82,83)` or a rigorously nonpositive independent external witness at each endpoint.

## Verification

`generate_exact_coordinates.py` is the exact two-rail coordinate/moment generator. `generate_topology_event_atlas.py` reconstructs every representative homotopy cell with exact supporting-plane checks. `verify_exact.py` is standard-library-only and reconstructs the hull independently in both directions: exhaustive V-to-H supporting-plane enumeration and exhaustive H-to-V triple-plane intersection. It then recomputes exact volume, centroid, zero moments, every maximal face, every true edge, all vertex supports, all four edge-cone components and the obstruction identity. `verify_interval.py` independently propagates the coordinate box through active and inactive incidence and complete mechanics. `verify_mesh.py` checks watertight OBJ/STL, winding, Euler number, volume and center of mass.

## Materialized artifacts

- Complete checksummed archive (`M42_13face_two_rail_exact.zip`) — SHA-256 `5bee9a05fdf00ce5b4f9884738453755b5efe12487ead2b07baa9b9d63d3c4b9`.
- Archive checksum (`M42_13face_two_rail_exact.zip.sha256`)
- Full standalone research handoff (`research_handoff.md`)
- Primary exact certificate (`certificate.json`)
- Exact coordinate and hard-moment generator (`generate_exact_coordinates.py`)
- Exact topology-cell atlas generator (`generate_topology_event_atlas.py`)
- All 95 old and new exact lattice rows with final active/inactive flags (`coordinates_all_lattice.csv`)
- Exact centred active V-representation (`coordinates_active_centered.csv`)
- Exact centred H-representation (`halfspaces_centered.csv`)
- Complete actual maximal-face cycles and face mechanics (`faces.json`)
- Complete 130-edge four-component audit (`edges_four_component_audit.csv`)
- Complete vertex mechanics (`vertices_mechanics.csv`)
- Complete 15-cell actual incidence and row-status atlas (`topology_event_atlas.json`)
- Compact topology-event ledger (`topology_event_summary.csv`)
- Independent exact V→H/H→V verifier (`verify_exact.py`)
- Directed interval-box verifier (`verify_interval.py`)
- Topology-atlas audit (`verify_event_atlas.py`)
- Watertight mesh verifier (`verify_mesh.py`)
- Run-all transcript (`RUN_ALL_VERIFIERS.txt`)
- OBJ (`body.obj`)
- STL (`body.stl`)

The archive was extracted into a clean directory; `sha256sum -c SHA256SUMS` and the complete `[internal-source-reference].sh` suite passed there.
