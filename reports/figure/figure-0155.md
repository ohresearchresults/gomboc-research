# figure-0155

AI research report · 2026-08-29 UTC

---

# M42 graded cross-linked volumetric witness sheet

## Literal verdict

**NONWINNER.** No strict own-centroid `(S,U,H)=(1,1,0)` homogeneous convex polyhedron was obtained.

The run’s admissibility gate requires a finite uniformly dense body evaluated at its own exact ordinary-volume centroid, with exactly one stable maximal face, one unstable vertex, no saddle true edge, complete positive-margin face/vertex/full-edge-cone audits, independent verification, and matching OBJ/STL. The supplied M42 frontier was the exact finite-thickness crossrail whose remaining task was a genuinely cross-linked volumetric continuation rather than another serial rail.

This continuation materializes that next topology: a direct 32-edge witness rail and a 76-edge return rail, joined by many actual cross-rail edges, followed by a full invertible metric and five graded radial fields. It is exactified to a rational open endpoint of strict class `(2,2,2)`.

## What changed relative to the journal

The preceding exact crossrail had transferred its extra maximum through `(96,104)` and then `(104,111)`. The new sheet:

- has `218` exact input rows;
- has actual irredundant `(V,E,F)=(129,367,240)`, complexity `734`;
- contains `44` actual direct/return cross-rail true edges;
- contains a connected `227`-tetrahedron centroid-fan communicating complex;
- deactivates every earlier local maximum route: `(95,96)`, `(82,96)`, `(96,104)`, and `(104,111)` are all absent;
- preserves the protected stable 17-gon and protected unstable vertex `8`;
- transfers the Euler-neutral block to extra stable face `[120,102,200]`, extra unstable vertex `148`, saddles `(127,128)` and `(177,178)`, and a new exact external-positive true-edge obstruction `(147,148)`.

This is not a surface subdivision and not a longer version of the prior zipper.

## Complete exact generator

Let every pre-field input row be `q_i/QS`, where `QS=10^12`; all `218` integer triples `q_i` are supplied in `source_rows_pre_field_lattice.csv`. Rows `112..142` are the direct rail and rows `143..217` are the return rail.

The authoritative exact endpoint is

```text
y_i = (m_i/FM) · (R/RM) · ((q_i-c0)/QS),

RM = FM = 10^12,
common denominator QS·RM·FM = 10^36,

c0 = (65804153790, -475931061715, -613321833967),

R =
[ 755420658406, -541077269903,  -55209727151]
[-541077269903, 2478569258690, 613169139200]
[ -55209727151,  613169139200, 794468831485]
```

Every exact integer multiplier `m_i` is supplied in `field_multipliers.csv`; nonfield rows have `m_i=10^12`. Their geometric provenance is the five Gaussian log-radius fields with coefficients

```text
(0.025796, -0.02980131, 0.02585619, 0.00338601, 0.03124567)
```

on `(rail,centre,width)` equal to `(back,148,6)`, `(direct,128,5)`, `(back,176,7)`, `(direct,120,5)`, and `(back,200,8)`. The rounded integer multiplier table—not floating exponentiation—is authoritative.

`generate_exact_endpoint.py` uses only integer arithmetic and reproduces all `218` expanded rows exactly. The full expanded V-input table is `coordinates_all_exact.csv`; the exact own-centred active V table is `coordinates_active_centered.csv`.

Active rows are:

```text
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 54 69 72 73 86 88 102
113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130
131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148
149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166
167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184
185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202
203 204 205 206 207 208 209 210 211 212 213 214 215 216 217
```

The remaining `89` inputs are strictly inactive. Complete exact H data, all `240` maximal-face cycles, all `367` true edges with their two incident faces, and the full V table are included in the archive. The clean-room verifier reconstructs each supporting plane from its cycle, proves strict support against all 218 inputs, checks the connected closed Euler-2 boundary, and thereby proves this is the complete actual hull rather than an inherited active-set assumption.

## Exact ordinary volume and moments

Exact ordinary volume:

```text
10760006162177599325868264840854081298115529552088631967903982749784243361117737927802258837343537902574725601
/
600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

Decimal volume: `17.933343603629332`.

Exact unshifted ordinary-volume centroid:

```text
Cx =
-2435938198584302680037254150535935435982708750245992212015277971429148028498786497337638551502735533172104241
/
107600061621826000004146950013505514282993139849335574015009462665837362578000000000000000000000000000000000000

Cy =
2122452929821832423778123727512746089591597288764217036531898539832118146473611280427755141053676654532621621
/
215200123243652000008293900027011028565986279698671148030018925331674725156000000000000000000000000000000000000

Cz =
-1523869958175776012898053078622754110451992125958690358563987795503938615962829507198850146888535808342594543
/
215200123243652000008293900027011028565986279698671148030018925331674725156000000000000000000000000000000000000
```

For each component the independent verifier recomputes the exact unshifted first moment and proves the identity `M_k−V C_k=0`. Translation by the displayed centroid therefore makes all three ordinary first moments exactly `0/1`.

## Complete equilibrium audit

The exact own-centred class is **`(S,U,H)=(2,2,2)`**.

Stable maximal faces:

- protected 17-gon `[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,0]`, normalized full-polygon margin `0.18055899621229862`;
- extra triangle `[120,102,200]`, margin `0.039313118172319854`.

Unstable actual vertices:

- protected target `8`, minimum adjacent-edge support margin `0.37714873931077003`;
- extra vertex `148`, margin `0.0679918018240675`.

Saddle true edges:

- `(127,128)`, full four-component margin `0.05971339095274934`;
- `(177,178)`, margin `0.012632026269789669`.

Global minimum normalized margins are:

```text
stable positive        0.039313118172319854
nonstable exclusion    0.0019763253586835743
unstable positive      0.0679918018240675
nonunstable exclusion  0.004129555104960055
saddle positive        0.012632026269789669
nonsaddle exclusion    0.01343436264319396
topology distance      0.000017422150325849892
inactive separation    0.0017049186592543591
```

Every component of every face, every neighbor support at every actual vertex, and all four edge-cone components `(t,1−t,β₁,β₂)` at every true edge are stored exactly in the machine-readable ledgers and independently regenerated.

## Exact transferred maximum obstruction

True edge `(147,148)` has all nonmutual endpoint supports strictly positive. Its mutual supports are

```text
σ(147→148) =
-823195517938840910245849766842138445886887763457093928651095178263169178881097178661985227040228540896774830417100218325596689158025965189763979
/
21520012324365200000829390002701102856598627969867114803001892533167472515600000000000000000000000000000000000000000000000000000000000000000000000

σ(148→147) =
978327162641691916036178485622507150965279243945466414979629122910647540631199802660645847171972292018583738247927807682614008006382961631819719
/
21520012324365200000829390002701102856598627969867114803001892533167472515600000000000000000000000000000000000000000000000000000000000000000000000
```

and exactly

```text
σ(147→148)+σ(148→147)
 = ||x148−x147||²
 = 144174308420083210462197840193793422480114170965554710541307486482283
   /20000000000000000000000000000000000000000000000000000000000000000000000
 > 0.
```

Thus the mutual supports cannot both be nonpositive. While the exact incidence and external-positive signs persist, at least one endpoint remains unstable. Vertex `8` is independently strictly unstable, so the entire certified cell has `U≥2`. The minimum external raw support is `0.17002422701828107`.

The obstruction is stronger than the edge identity alone. Both `147` and `148` have exact squared radius larger than target `8`. A nonpositive-support witness step strictly increases radius, so no fixed-centre monotone witness chain of **any finite length** can drain either endpoint into target `8`. Exact squaring further proves that a pure centre displacement with fixed geometry must have norm greater than `3/5` merely to reverse the endpoint/target radius ordering.

## Genuinely volumetric coupling

The actual hull contains `44` direct/return true cross-edges, including the long crossfoot fan through row `200` and repeated cross-links through rows `202,205,207,210,212,214,216`.

There are `227` maximal boundary triangles incident to at least one new rail row. Coning each triangle to the exact own centroid produces a nondegenerate tetrahedron; the shared-edge adjacency graph of these tetrahedra is connected. The minimum exact absolute determinant is

```text
25662539244358793428001027167764377436153899033324548810243907526333856983452983465751097144572205992610383501541634273466004456499210952458144199466926393679611534192383072247937
/
10760006162182600000414695001350551428299313984933557401500946266583736257800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

The active complex contacts all four required sectors:

```text
terminal: 69,102,113,114,143,144,145,146,147,148,149
right:    4,5,86,88,120,127,128,129,173,174,177,178,179
north:    102,120,200
left:     12,13,72,173,174,177,178,179,200
```

This is a literal finite-thickness three-dimensional communicating sheet, not a surface-only refinement.

## Exact first outgoing chamber atlas

The first two plausible fixed-sheet exits were exactified as four complete rational representative cells:

| chamber | actual `(V,E,F)` | class | new paired event |
|---|---:|---:|---|
| `C22_no_birth` | `(132,376,246)` | `(2,2,2)` | neither birth |
| `C23_vertex_edge_birth` | `(132,376,246)` | `(2,3,3)` | unstable `128` and saddle `(128,129)` |
| `C32_face_edge_birth` | `(132,376,246)` | `(3,2,3)` | stable `[178,179,173]` and saddle `(173,179)` |
| `C33_both_births` | `(132,376,246)` | `(3,3,4)` | both paired births |

Every cell has a rebuilt exact hull, exact volume/centroid, complete face and edge lists, exhaustive full-cone mechanics, and the exact `(147,148)` obstruction. No chamber is `(1,1,0)`. The direct saddle cannot be pushed out without the `128/(128,129)` birth; the return saddle cannot be pushed out without the `[173,178,179]/(173,179)` birth.

## Perturbation box

Rows `0..16` and all inactive inputs are fixed. Every coordinate of every other active row—`336` independent coordinates—may vary by `±10^-10`.

Exact outward `Fraction` intervals preserve the complete `(129,367,240)` incidence, inactive ledger, strict `(2,2,2)`, all four old-channel absences, and the `(147,148)` obstruction. Directed lower bounds include:

```text
facet determinant           5.166634095350333e-7
inactive facet determinant  6.673569780835833e-5
stable component            0.014280095437095854
nonstable witness           0.00013599587139552648
unstable support            0.045460611021739025
nonunstable witness         0.0020185802428531996
saddle component            0.03741238399450631
nonsaddle witness           0.0006045515622986836
obstruction/target support  0.17002356565764645
```

## What was tried

The unmetricized sheet had class `(5,23,26)` because its own centroid moved substantially. A full five-parameter determinant-one metric reduced the actual sheet to `(2,2,2)`. Five graded fields then produced the robust exact endpoint above.

Independent radial changes around rows `120,200,127,128,129,148,149,174,178,179,102`, local face and edge caps, further metric motion, and the two-dimensional outgoing field sweep transferred or multiplied the block. No open `(1,1,0)` state appeared.

These searches are empirical evidence only. Exact conclusions are limited to the endpoint, its interval box, the four exact adjacent chambers, the edge obstruction, and the radial-order theorem.

## Sharpest genuinely new successor

The present sheet already supplies long witness routes and extensive cross-linking. The remaining failure is **radial/moment ordering plus two paired-birth gates**, not lack of serial resolution. Another point cap, scalar rail, metric polish, smooth radial field, or surface refinement is subsumed.

The first topology not represented by the exact sheet or its four adjacent chambers is an edge-sharing **two-nonsimplicial-cell volume replacement**—equivalently, a triangular-prismatic or octahedral `2↔3 / 3↔2` complex whose adjacent 3-cells delete a shared interior edge in the same event. It must jointly absorb:

```text
terminal obstruction component  {147,148,149}
extra stable foot               {120,102,200}
direct saddle/birth packet      {127,128,129}
return saddle/birth packet      {173,174,177,178,179}
```

At least rows `102,120,127,128,147,148,173,178,200` and obsolete neighbors must be allowed to become non-extreme together. One cell must prevent the `128/(128,129)` birth; the other must prevent the `[173,178,179]/(173,179)` birth; they must share a true interior edge so the terminal maximum and cross-stable foot cannot transfer independently.

Because both obstruction endpoints currently lie farther from the centroid than target `8`, the replacement also needs at least two noncritical interior return-lobe actuators that perform macroscopic radial/centroid reordering, while three selected coordinates solve the exact ordinary moments as hard dependent equations. Every `2↔3` or `3↔2` wall must trigger a complete hull and full-normal-cone rebuild.

## Independent verification and meshes

All of the following pass:

- deterministic exact integer generator;
- independent standard-library exact closed-boundary reconstruction;
- exact volume, centroid, and three zero centred moments;
- exhaustive face/vertex/four-component-edge audit;
- old-channel deletion and exact `(147,148)` obstruction;
- exact `±10^-10` interval box;
- exact four-cell outgoing atlas;
- exact radial-order obstruction;
- matching watertight OBJ/STL.

The OBJ/STL have `129` vertices and `254` triangles, mesh Euler number `2`, recomputed volume `17.933343603629336`, and COM norm below `7.6×10^-16`. The 14 mesh edges beyond the 367 true edges are triangulation diagonals of the protected 17-gon. The aggregate transcript ends with `ALL VERIFIERS PASS`.

## Artifact integrity

- archive SHA-256: `32503cb60367e21c32cf35007ce4abc2235ded11e35cbd3667cfc2950d254cb4`;
- handoff SHA-256: `e46320e0758c1b6fcf30002cf837df1b006a0e56a740084424974a78068d1031`;
- certificate SHA-256: `f89eb6b8d7a053285159d99c4210357bf27e60705a844db948d9f3b4129bb9fc`;
- exact generator SHA-256: `a38ee1b99ab8cf2b7dfdc11425a1f2ae63e66f8f05e0ff2f2517d82e7cccb853`;
- complete H table SHA-256: `0c000a309f06c55213460d390d88cb53561cb72ddf862562f2df5f703f5333a0`;
- face-cycle table SHA-256: `34a803b22d2cc5cb9764eb84b448f5068ef013f3de046ac1833bc94d95014201`;
- true-edge table SHA-256: `e7e22164bd8307e3fffbbec22284c0434d44bcfc160802ee8b5a0a88ebc3acec`;
- corner atlas SHA-256: `06082caaa90569bef136247d3423e1b621150ab5f124ebf7c296cab3887313b6`;
- OBJ SHA-256: `6913bcb931474c1cc089b356355b1fcd1eea7d6f417ad1e43c5181f333db7282`;
- STL SHA-256: `00901716ddb0a5d6ad7c0130fc090ad1f38a7e29d50da14158743ae5831b19ab`.

Complete self-contained handoff with all face cycles and true edges (`research_handoff.md`)

Deterministic exact archive (`m42_graded_sheet_exact_handoff.zip`) · archive digest (`m42_graded_sheet_exact_handoff.zip.sha256`) · all per-file hashes (`SHA256SUMS.txt`)

Exact generator (`generate_exact_endpoint.py`) · certificate (`certificate.json`) · clean-room verifier (`verify_exact_cleanroom.py`) · interval verifier (`verify_interval.py`) · corner atlas (`mechanical_corner_atlas.json`) · verification transcript (`RUN_ALL_VERIFIERS.txt`) · OBJ (`body.obj`) · STL (`body.stl`)

The negative result is exact for this graded volumetric sheet, its certified coordinate cell, and the four first outgoing mechanical chambers. It is not a global obstruction to the larger edge-sharing two-cell replacement.
