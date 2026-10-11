# figure-0165

Historical AI scientific report · saved 2026-08-30 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Calm Lynx 78 — exact connected two-control zipper determination

## Literal verdict

**NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained.

The strongest endpoint is a finite exact-dyadic uniform-density convex polyhedron with a unique 180-bit Krawczyk-isolated zero of all three ordinary first moments. At its own exact volume centroid it has strict class `(S,U,H)=(2,2,2)`, with 3,481 irredundant H rows/maximal primal faces, 6,958 primal vertices, 10,437 true edges, and 13,912 oriented boundary triangles. The target remains an own-centred strict `(1,1,0)` finite body; an auxiliary centre, wall point, or numerical near-solution does not qualify. :contentReference[oaicite:0]{index=0}

## Correction to the predecessor boundary

The supplied `connected_patch_3644_exact_nonwinner` archive was not exact: its advertised source, root, audit, H/V, verifier, and mesh entries were 77-byte placeholders saying they had not been generated. Its own internal handoff correctly called the 3,644-row state numerical. This result first exactifies that state as `C0_pre`, then certifies four further independently rebuilt actual cells. No conclusion below relies on those placeholders.

## Exact deterministic family

The normative pruned endpoint table is `data/source_rows_modes.hex`, SHA-256 `422733f54163f891047ecf2285c7953d03d5ce0dc014d321e390133881af1a33`. Every hexadecimal binary64 token is its represented exact dyadic rational. The corresponding full 4,324-row endpoint table is `data/atlas_full_sources/C3_endpoint.hex`, SHA-256 `13d288f58f518e4af667a6825cc5a5ea3ffb3c7f14daa42a66fcfa421a018f74`.

Starting from exactified `C0_pre`, the construction changes exactly 101 source rows and leaves all 12,972 entries of the inherited three distributed support modes unchanged. The first control is the stored connected zipper displacement in `data/full_zipper_controls.npz`. The second, independent control radially rescales original row `2594`. The five normative full sources are:

```text
C0_pre                    Q0
C1_lam06                  Q0 + 0.6 zipper
C2_uncontrolled_birth     Q0 + 0.7 zipper
C2_controlled_antibirth   Q0 + 0.7 zipper, then q_2594 *= 0.9995
C3_endpoint               Q0 + 1.0 zipper, then q_2594 *= 0.995.
```

`src/generate_coupled_event.py` regenerates all five tables and the active endpoint bit-for-bit; `certificates/generator_reproduction_report.json` has `passed=true`.

For each actual cell, `u_i(t)=1+F_i·t` and `P(t)={x:q_i^0·x≤u_i(t)}`. The same three entries of `t` are dependent variables solving `Mx=My=Mz=0`; no additional broad moment mode was introduced.

## Support-connected topology-changing event

The changed-row induced support graph has 101 vertices, 245 true-adjacency edges, one connected component, and a 313-row one-ring closure. A shortest changed-only route from the incipient birth side to the old extra unstable side is

```text
2524—2455—2492—2528—2529—2530—2531—2392.
```

The protected opposite-channel rows `424,389,3736,3737,1744,1779,2025,1490,1805` are unchanged by the source-direction zipper.

The 21 monitored exact circuits, in order, are:

```text
{2524,2594,2629,2735}; {2524,2629,2735,2771};
{2455,2524,2735,2771}; {2455,2524,2701,2771};
{2455,2597,2701,2771}; {2455,2562,2597,2701};
{2455,2562,2597,2598}; {2562,2563,2597,2598};
{2562,2563,2598,2599}; {2563,2564,2598,2599};
{2563,2564,2599,2600}; {2564,2565,2599,2600};
{2564,2565,2600,2601}; {2565,2566,2600,2601};
{2565,2566,2601,2602}; {2566,2567,2601,2602};
{2566,2567,2602,2603}; {2567,2568,2602,2603};
{2394,2567,2568,2603}; {2392,2394,2568,2603};
{2288,2392,2394,2568}.
```

At the separately isolated moment roots their determinant-sign strings are:

```text
C0_pre                   --++++-+-+-+-+-+-+--+-
C1_lam06                 --+++-+++-+-+-+-++--+
C2_uncontrolled_birth    -+++--+++-+-+-+-++--+
C2_controlled_antibirth  -+++--+++-+-+-+-++--+
C3_endpoint              -+++---+++++++++++--+.
```

Every displayed circuit interval excludes zero; twelve monitored signs reverse from `C0_pre` to `C3_endpoint`. Exact intervals are in `certificates/coupled_event_cell_atlas.json`.

## Five independently certified actual cells

```text
Cell                       H      V      E       class      extra S        extra U                 extra H
C0_pre                   3644   7284  10926    (2,2,2)      3736       (2288,2392,2394)       (2594,2735)
C1_lam06                 3544   7084  10626    (2,2,2)      3736       (2288,2394,2603)       (2629,2805)
C2_uncontrolled_birth    3525   7046  10569    (3,2,3)   2594,3736    (2288,2394,2603)       (2524,2594),(2594,2910)
C2_controlled_antibirth  3525   7046  10569    (2,2,2)      3736       (2288,2394,2603)       (2629,2910)
C3_endpoint              3481   6958  10437    (2,2,2)      3736       (2288,2394,2603)       (2629,2910).
```

Stable row `424`, unstable facet `(1744,1779,2025)`, and saddle `(1490,1805)` remain strict in all five cells. Each cell has its own exact source, actual hull, pruned irredundant row set, rational fixed-cell moment map, Krawczyk-isolated root, exhaustive interval equilibrium audit, and positive inactive gap.

The actual lattice changes are large:

```text
C0→C1    removed/added facets 526/326; removed/added true edges 598/298
C1→C2u   removed/added facets 119/81;  removed/added true edges 109/52
C2u→C2c  identical actual incidence
C2c→C3   removed/added facets 234/146; removed/added true edges 228/96.
```

Complete lists are in `certificates/actual_face_lattice_changes.json`. This is a finite actual-cell atlas; it does not claim that one inherited moment polynomial remained valid through every unlisted intermediate wall.

## Exact anti-birth result

The critical primitive `E_(2594,2524)=u_2524-(q_2524·q_2594/||q_2594||²)u_2594` has directed values

```text
C0_pre                  -1.201516377847389e-3
C1_lam06                -7.307327227209291e-5
C2_uncontrolled_birth   +1.939342437916339e-4
C2_controlled_antibirth -2.963508406767595e-4
C3_endpoint             -3.794837114319844e-3.
```

`C2_uncontrolled_birth` and `C2_controlled_antibirth` have exactly the same actual face lattice. Without the second control, row `2594` is stable and `(2524,2594)`, `(2594,2910)` are saddles. With the independent row-2594 control, row `2594` is strictly nonstable and those birth features disappear; the extra saddle is rerouted to `(2629,2910)`. This rigorously proves that the coupled second coordinate suppresses the observed S–H birth after the actual post-circuit hull is rebuilt.

## Final isolated ordinary centroid

For `C3_endpoint`, the first Krawczyk image is

```text
t0 [-0.0312097326412240411067188691564854055,
    -0.0312097326412240411067188691333242584]
t1 [ 0.00413487507671882344936376366120154350,
     0.00413487507671882344936376367485109877]
t2 [ 0.00501990150313157569115587916668901393,
     0.00501990150313157569115587918147571700].
```

A second image lies strictly inside. The moment-Jacobian determinant is the positive singleton `38.5506280049554555535975748762901518`. On the first image:

```text
V  [4.13641036706639664581866613908251232,
    4.13641036706639664581866632642853293]
Mx [-2.0014741537209038e-26, 2.0014808403857036e-26]
My [-3.2846130937334226e-26, 3.2846357262039704e-26]
Mz [-8.238428614749309e-26, 8.238418697168460e-26].
```

Strict Krawczyk inclusion proves one and only one zero, so the origin is exactly the body’s own uniform-volume centroid.

## Exhaustive final incidence and equilibrium audit

All 3,481 H rows are irredundant. There are 6,958 maximal triangular polar faces/primal vertices, 10,437 true edges, 3,481 maximal primal-face cycles, and 13,912 surface triangles. No incidence or equilibrium primitive is ambiguous.

Complete positive labels, in original 4,324-row indexing:

```text
stable rows       424, 3736
unstable facets   (2288,2394,2603), (1744,1779,2025)
saddle edges      (1490,1805), (2629,2910).
```

Directed global margins:

```text
minimum positive stable
[3.6528785160690828631601146395279e-5,
 3.6528785160690828631601149192281e-5]
closest excluded stable
[-3.5740256775575323714711330433430e-6,
 -3.5740256775575323714711264656011e-6]
minimum positive unstable
[0.18494616176662618700997012869730,
 0.18494616176662618700997012992617]
closest excluded unstable
[-0.0017288714795879999867599213834909,
 -0.0017288714795879999867599194992409]
minimum positive saddle component
[0.18918074132274324464736371431239,
 0.18918074132274324464736371498917]
closest excluded saddle component
[-0.00074521976545412218991905914308680,
 -0.00074521976545412218991888869381050].
```

The exhaustive directed minimum nonincident H–V numerator is greater than `1.468921317915317e-9`, so the endpoint lies in an open incidence cell. Every maximal face, active vertex, and all four components of every true-edge normal cone are recorded in `certificates/root_full_interval_audit.json`.

## Rigorous transferred obstruction

The original extra unstable facet `(2288,2392,2394)` and extra saddle `(2594,2735)` are absent at `C3`. The replacement facet `(2288,2394,2603)` has minimum positive numerator at least `0.1849461617666261870`; the replacement saddle `(2629,2910)` has minimum full-cone component at least `0.1891807413227432446`. Extra stable row `3736` remains strict with minimum primitive about `0.0014094162485642894`. Row `2594` is safely nonstable, with `E_(2594,2524)<-0.0037948371143198441`.

The opposite channel is preserved with margins: row `424` greater than `3.6528785e-5`, facet `(1744,1779,2025)` greater than `0.3324547815`, and edge `(1490,1805)` greater than `0.4080759026`.

Therefore the first rigorous obstruction for this exact two-control endpoint is an **open transferred U–H pair plus the surviving extra stable row**, not the incipient row-2594 birth. This proves transport for the realized family only, not a global impossibility theorem for higher-dimensional replacements.

## Perturbation, H/V, verifier, and mesh

The exact fixed-source `L∞` clearance of the second Krawczyk image inside the fully audited first image is

```text
10375516690492628201447081 /
1532495540865888858358347027150309183618739122183602176
= 6.7703405418264811126e-30.
```

Within that support-mode radius the entire 3,481-row incidence lattice and class `(2,2,2)` remain fixed. This is not an arbitrary source-coordinate radius; only the isolated root is exactly centred.

The archive supplies outward interval H/V arrays, midpoint H/V arrays, all maximal-face cycles, every true edge, and watertight OBJ/STL. The mesh has 6,958 vertices, 13,912 triangles, Euler number two, and volume approximately `4.1364103670663965` (OBJ) / `4.136410367849423` (merged STL).

`src/verify_coupled_event_cleanroom.py` imports none of the construction, search, Krawczyk, interval-audit, or geometry modules. It independently regenerates exact sources, rebuilds all actual incidence, reconstructs cycles and edges, reintegrates volume/moments, recomputes every face/vertex/four-component edge cone and inactive gap, matches interval H/V endpoints bit-for-bit, verifies the anti-birth comparison and connected graph, and audits both meshes. `certificates/cleanroom_verify_report.json` has `passed=true`. The packaged archive was freshly extracted and `./[internal-source-reference].sh` completed with `ALL CHECKS PASSED`.

## Numerical search evidence beyond the certificate

A finite 50-sample structured continuation from C3, with actual hull rebuilds and numerical moment solves, found no state below six equilibria. The histogram was `(2,2,2):3`, `(3,2,3):17`, `(3,3,4):3`, `(4,2,4):17`, `(4,3,5):10`. The first worsening near scalar `0.58` birthed stable row `2805` and saddles `(2524,2805)`, `(2805,2945)`. This is discovery evidence only, not an interval exclusion.

## Smallest genuinely new continuation

`certificates/residual_successor_patch.json` gives one connected 335-row/771-edge support patch spanning extra stable row `3736`, extra unstable facet `(2288,2394,2603)`, saddle `(1490,1805)`, and saddle `(2629,2910)`, while protecting row `424` and facet `(1744,1779,2025)`.

The evidence now supports at least three independent incidence controls: an S–H cancellation sheet from `3736` to `(1490,1805)`, a U–H cancellation sheet from `(2288,2394,2603)` to `(2629,2910)`, and a shared relay coordinate making both deaths overlap before another birth. The same three moment modes should remain dependent variables, and every crossed circuit must trigger a fresh actual-hull rebuild and interval root isolation.

## Reusable artifacts

Archive SHA-256: `09f4e6047eafa23112f36b27da30bb5829667de62f34b43227909489bb934e0b`.

- [Complete exact/directed archive](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner.zip)
- [Archive SHA-256 file](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner.zip.sha256)
- [Full standalone handoff](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/RESEARCH_HANDOFF.md)
- [Machine-readable result](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/RESULT.json)
- [Integrity manifest](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/MANIFEST.sha256)
- [Exact endpoint source](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/data/source_rows_modes.hex)
- [Deterministic generator](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/src/generate_coupled_event.py)
- [Five-cell exact atlas](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/certificates/coupled_event_cell_atlas.json)
- [Actual lattice changes](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/certificates/actual_face_lattice_changes.json)
- [Connected event graph](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/certificates/support_connected_event_graph.json)
- [Local anti-birth/transfer certificate](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/certificates/local_coupled_event_root_interval.json)
- [Krawczyk root certificate](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/certificates/root3_interval_certificate.json)
- [Full interval audit](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/certificates/root_full_interval_audit.json)
- [Perturbation certificate](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/certificates/perturbation_region.json)
- [Interval H/V data](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/geometry/root_interval_hv.npz)
- [Maximal-face cycles](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/geometry/root_maximal_face_cycles.json)
- [True-edge ledger](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/geometry/root_true_edges.csv)
- [Independent verifier](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/src/verify_coupled_event_cleanroom.py)
- [Verifier report](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/certificates/cleanroom_verify_report.json)
- [OBJ mesh](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/geometry/root_midpoint.obj)
- [STL mesh](sandbox:/mnt/data/coupled_zipper_3481_exact_nonwinner/geometry/root_midpoint.stl)
