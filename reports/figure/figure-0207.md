# figure-0207

AI research report · 2026-09-02 UTC

---

# Calm Quartz 90 — exact wall-242 simultaneous four-circuit determination

## Literal disposition

**EXACT DELIMITED NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained.

The requested topology was nevertheless realized literally. One exact rational scalar family has four independent circuit determinants `Δ_i(t)=s_i t`; all four vanish at the same exact parameter `t=0`. The central hull contains four strict supporting quadrilateral maximal faces forming one connected boundary subcomplex, and coning those cells to the body’s exact ordinary-volume centroid gives a connected positive-volume four-cell complex. The strict positive-side endpoint is a fully materialized own-centred polyhedron with

```text
(V,E,F,C)=(15,39,26,78),
(S,U,H)=(2,2,2).
```

It preserves the intended stable face `[0,1371,C]` and intended unstable vertex `C`, but retains an extra stable face, an extra unstable vertex, and two saddle edges. :contentReference[oaicite:0]{index=0}

The journal left exactly this finite-thickness four-circuit event open after the exact `D–E` shared-interior endpoint transported its Euler-neutral block. :contentReference[oaicite:1]{index=1} The global acceptance gate rejects an auxiliary-centre object, a wall point, a near-solution, or a theorem without finite H/V data and matching meshes. :contentReference[oaicite:2]{index=2}

## What was actually done

I recovered the not-yet-integrated exact archive from the file library, extracted it afresh, verified every internally manifested SHA-256 entry, and reran the deterministic generator, primary exact verifier, directed own-centroid interval verifier, standard-library-only clean-room verifier, and OBJ/STL watertightness verifier. The fresh aggregate run ended

```text
INDEPENDENT_CLEAN_ROOM_EXACT_FOUR_CIRCUIT_NONWINNER_PASS
WATERTIGHT_FOUR_CIRCUIT_ENDPOINT_MESH_PASS
ALL_NIMBLE_COMET_70_WALL242_FOUR_CIRCUIT_VERIFIERS_PASS
```

The exact archive SHA-256 is

```text
74181c1ae51f2b1a54f7bac0b40f72265317c9531aac837c62563beb01fca5c4.
```

Discovery-only optimization files are included but are not used as certificates.

## 1. Exact common family and four simultaneous circuits

Use labels

```text
A=40001, B=40002, C=40003, D=40004, E=40005.
```

All coordinates are rational. Eleven vertices are fixed; only `2515,E,A,1258` move transversely in

```text
p_i(t)=p_i(0)+t d_i,   -1≤t≤1.
```

The exact deterministic data are in `data/family_parameters_exact.json`. The four independent circuit identities are:

| circuit | source diagonal | target diagonal | exact determinant | minimum central support slack |
|---|---|---|---|---:|
| `[1975,2515,2369,2732]` | `[1975,2515]` | `[2369,2732]` | `4293967333319547117280200707421874583638477/62500000000000000000000000000000000000000000000 · t` | `0.0001036851384156048` |
| `[1371,E,2369,C]` | `[1371,E]` | `[2369,C]` | `-103257025433221487630310068681518870447161123/1000000000000000000000000000000000000000000000000 · t` | `0.001027750696804908` |
| `[A,D,3290,C]` | `[A,D]` | `[3290,C]` | `5201984781962600312717362949044716323198299/100000000000000000000000000000000000000000000000 · t` | `0.0009554274460818358` |
| `[1258,3290,2152,D]` | `[1258,3290]` | `[2152,D]` | `-41145221651896175012318658863394794463000891/500000000000000000000000000000000000000000000000 · t` | `7.042819315536771e-05` |

Every slope is nonzero. Hence all four coplanarity sheets meet at the single exact family parameter `t=0`, while the source and target diagonals occur on opposite strict sides. :contentReference[oaicite:3]{index=3}

## 2. Positive-volume common incidence event

At `t=0` the actual hull has

```text
15 active vertices,
35 true edges,
22 maximal faces = 18 triangles + 4 quadrilaterals,
15-35+22=2.
```

The four quadrilateral maximal-face cycles are

```text
[2515,2369,1975,2732]
[C,1371,2369,E]
[C,D,3290,A]
[2152,3290,D,1258].
```

Their incidence chain is

```text
{1975,2515,2369,2732} --2369-- {1371,E,2369,C}
                              --C-- {A,D,3290,C}
                        --[3290,D]-- {1258,3290,2152,D}.
```

The exact central body volume is

```text
24112489551970965201276617674628917246864516868315636864813/2000000000000000000000000000000000000000000000000000000000000.
```

Coning the four quadrilateral cells to the exact central centroid gives the following strictly positive cell volumes:

1. `8367990826715100609768671121754691211299106057686877245730104144702854290658599734463980620588910436938625416959314599491408900153/10850620298386934340574477953583012761089032590742036589165850000000000000000000000000000000000000000000000000000000000000000000000000`  (approximately `0.0007711993044267797`)
2. `54917911498042739730190558832074482422738193490284805963133868775965216385994779226157173564074575851345121426963649060087371543641/41335696374807368916474201727935286708910600345683948911108000000000000000000000000000000000000000000000000000000000000000000000000000`  (approximately `0.001328583193569064`)
3. `1510633913025437250601542905769109967765858755114632886312076780713536047756925851852430531422166529410059247156436796622025836067/1157399498494606329661277648382188027849496809679150569511024000000000000000000000000000000000000000000000000000000000000000000000000`  (approximately `0.001305196619654901`)
4. `5875764420227437455983765507892332879432613940560789074896563540448691689584608626088717324890456080256468029437313511892428035457/7233746865591289560382985302388675174059355060494691059443900000000000000000000000000000000000000000000000000000000000000000000000000`  (approximately `0.0008122712239457318`)

Thus this is a genuine connected finite-thickness common event, not a comparison of unrelated endpoints. :contentReference[oaicite:4]{index=4}

## 3. The demanded death-before-birth ordering fails exactly

The four **incidence** sheets cross simultaneously, but the desired mechanical cancellation does not. The exact strict chamber ledger is

```text
t=-1: (S,U,H)=(3,2,3)
 stable   {[0,1371,C], [1258,B,3296], [3290,A,D]}
 unstable {2732, C}
 saddles  {[2369,E], [3290,A], [3290,D]}

t=0: four simultaneous circuit degeneracies; no strict Morse class asserted

t=+1: (S,U,H)=(2,2,2)
 stable   {[0,1371,C], [1258,B,3296]}
 unstable {2732, C}
 saddles  {[2369,E], [3290,D]}.
```

Across `t=0`, the exact face-lattice changes are precisely

```text
[1975,2515] -> [2369,2732]
[1371,E]    -> [2369,C]
[A,D]       -> [3290,C]
[1258,3290] -> [2152,D].
```

Only the pair `[3290,A,D]` / `[3290,A]` disappears mechanically. The accepted parent packet is already absent as such on the exact negative side: replacement features have appeared before the common incidence wall. Therefore this realized four-circuit cell rigorously fails the assignment’s required “all four deaths before any birth” ordering; it cannot contain an open `(1,1,0)` chamber.

## 4. Strongest exact adjacent endpoint

The strongest strict endpoint is `t=+1`. All 15 supplied rational points are vertices. Their complete exact uncentred V-data are:

| label | x | y | z |
|---|---:|---:|---:|
| `0` | `122087729062261/500000000000000` | `-617779949586061/1000000000000000` | `-358414888093981/1000000000000000` |
| `1258` | `5555015990558838925497692189/62500000000000000000000000000` | `-152449172646166002388864932911/1000000000000000000000000000000` | `-92649705450733507248213133967/1000000000000000000000000000000` |
| `1371` | `-49910366436597/250000000000000` | `361257841988199/1000000000000000` | `222025227694451/1000000000000000` |
| `1975` | `174320195389057/1000000000000000` | `-465416325850301/1000000000000000` | `-216447024181553/1000000000000000` |
| `2152` | `63619753053057/200000000000000` | `-5302599530519/8000000000000` | `-429489791290981/1000000000000000` |
| `2369` | `15832318204359/50000000000000` | `-336447936149581/500000000000000` | `-233865593990357/1000000000000000` |
| `2515` | `481840557472817633101402423383/1000000000000000000000000000000` | `-1017950478752681040783069786381/1000000000000000000000000000000` | `-6322582780668025894586013497/15625000000000000000000000000` |
| `2732` | `13093687754213/31250000000000` | `-503577509778657/500000000000000` | `-509052513798609/1000000000000000` |
| `3290` | `64131102549597/1000000000000000` | `-13079219914451/125000000000000` | `-7969427888159/50000000000000` |
| `3296` | `25169318095397/100000000000000` | `-101868082985683/200000000000000` | `-14254068223119/62500000000000` |
| `A` | `-54267329386994946547828646207/500000000000000000000000000000` | `13729326906585295798135225501/62500000000000000000000000000` | `411853870079897231146450321/15625000000000000000000000000` |
| `B` | `-110740957405963/1000000000000000` | `289589920917369/1000000000000000` | `160634338103907/1000000000000000` |
| `C` | `-349620093410123/500000000000000` | `381177942750651/250000000000000` | `381954026448907/500000000000000` |
| `D` | `-666688809768091/1000000000000000` | `378740400063701/250000000000000` | `3029025235883/4000000000000` |
| `E` | `-294399909347750551083510559621/500000000000000000000000000000` | `1311862072315080156230686823489/1000000000000000000000000000000` | `670338452463338683498032107727/1000000000000000000000000000000` |

Its exact volume is

```text
72136555598763768587657899953850359989174045855946910594439/6000000000000000000000000000000000000000000000000000000000000
```

and its exact uncentred ordinary-volume centroid is

```text
cx = 213567047625117712096304585944994500826427802329811364577999853428282527860837437532963/14427311119752753717531579990770071997834809171189382118887800000000000000000000000000000
cy = -2241712190949162309907909364297372441622936991691038141521652769453644739576243039470517/57709244479011014870126319963080287991339236684757528475551200000000000000000000000000000
cz = -6306797716837920451761866044050744497572567499669504933872211508958177672602685418910401/288546222395055074350631599815401439956696183423787642377756000000000000000000000000000000.
```

After subtracting that one exact rational vector from every vertex, exact signed tetrahedral integration gives

```text
Mx=My=Mz=0,
centroid=(0,0,0).
```

No Santaló point, point-mass centre, or auxiliary mechanical point is substituted. :contentReference[oaicite:5]{index=5}

## 5. Actual maximal faces and true edges

The 26 outward-oriented irredundant maximal triangular cycles are:

- `[0,2732,1371]`
- `[0,1371,C] — **stable**`
- `[0,2152,2732]`
- `[0,3290,2152]`
- `[0,A,3290]`
- `[0,C,A]`
- `[1258,3296,2152]`
- `[1258,2152,D]`
- `[1258,B,3296] — **stable**`
- `[1258,D,B]`
- `[1371,1975,2369]`
- `[1371,2732,1975]`
- `[1371,2369,C]`
- `[1975,2732,2369]`
- `[2152,2515,2732]`
- `[2152,3296,2515]`
- `[2152,3290,D]`
- `[2369,2732,2515]`
- `[2369,2515,D]`
- `[2369,E,C]`
- `[2369,D,E]`
- `[2515,3296,B]`
- `[2515,B,D]`
- `[3290,A,C]`
- `[3290,C,D]`
- `[C,E,D]`

Every nonincident vertex is strictly behind every supporting plane; the minimum Euclidean nonincident separation is

```text
3.262799691873261e-05.
```

The 39 actual true edges are:

`[0,1371]`  `[0,2152]`  `[0,2732]`  `[0,3290]`  `[0,A]`  `[0,C]`
`[1258,2152]`  `[1258,3296]`  `[1258,B]`  `[1258,D]`  `[1371,1975]`  `[1371,2369]`
`[1371,2732]`  `[1371,C]`  `[1975,2369]`  `[1975,2732]`  `[2152,2515]`  `[2152,2732]`
`[2152,3290]`  `[2152,3296]`  `[2152,D]`  `[2369,2515]`  `[2369,2732]`  `[2369,C]`
`[2369,D]`  `[2369,E]`  `[2515,2732]`  `[2515,3296]`  `[2515,B]`  `[2515,D]`
`[3290,A]`  `[3290,C]`  `[3290,D]`  `[3296,B]`  `[A,C]`  `[B,D]`
`[C,D]`  `[C,E]`  `[D,E]`

Every edge has exactly two incident maximal faces, and `15-39+26=2`. The H-table contains the 26 primitive integer supporting planes; the full edge CSV records both incident faces and all four cone components for every edge.

## 6. Exhaustive exact own-centroid mechanics

### Stable maximal faces

| face | perpendicular-foot barycentrics, approximately | minimum |
|---|---|---:|
| `[0,1371,C]` | `(0.4687112491049312, 0.48887590309553114, 0.04241284779953762)` | `0.04241284779953762` |
| `[1258,B,3296]` | `(0.7171092310311493, 0.2795279877866304, 0.00336278118222029)` | `0.00336278118222029` |

Every other face has an exact negative Cramer witness. The closest excluded face is `[2369,D,E]`, margin `-0.0004541463741315883`.

### Unstable vertices

| vertex | minimum raw directed support | minimum normalized support |
|---|---:|---:|
| `2732` | `0.01501271303305021` | `0.1060746576259891` |
| `C` | `0.04371474183882475` | `0.6680060586108739` |

Every other vertex has an exact negative outgoing witness. The closest excluded vertex is `2515`, normalized margin `-0.0003277053383571703`.

### Saddle true edges

The four entries are edge-foot `t`, `1-t`, and the two incident full-normal-cone coefficients.

| edge | four normalized components | minimum |
|---|---|---:|
| `[2369,E]` | `(0.3090438928186847, 0.6909561071813153, 0.09043995491206387, 0.9248653257033084)` | `0.09043995491206387` |
| `[3290,D]` | `(0.06721044874482289, 0.9327895512551772, 0.04141798324281368, 0.9904481531385757)` | `0.04141798324281368` |

Every other true edge has an exact negative component. The closest excluded edge is `[2369,D]`, margin `-0.0001197998415007222`.

Therefore the exact endpoint class is

```text
(S,U,H)=(2,2,2),
S+U-H=2.
```

## 7. Positive own-centroid perturbation certificate

Independent perturbations of all 45 **uncentred** input coordinates by

```text
|δr_ij|≤2^-40=1/1099511627776≈9.094947017729282e-13
```

are certified. On the whole box the verifier interval-integrates volume and all three first moments, forms the common perturbed centroid `M/V`, translates every vertex by that interval centroid, and proves the same 26 maximal faces, 39 true edges, all face and vertex signs, and all four components of every true-edge cone. The class remains exactly `(2,2,2)`. The larger radius `2^-39` fails closed at the interval face-Gram stage. :contentReference[oaicite:6]{index=6}

## 8. Exact residual forcing component

At the endpoint, true edge `[2515,2732]` has every external endpoint support strictly positive. The minimum is

```text
119159158367392336095298397549688530068764146847971815524436161717765057165665319378841858218524818599297/288546222395055074350631599815401439956696183423787642377756000000000000000000000000000000000000000000000
≈0.4129638481430156.
```

Its two mutual supports have opposite signs and obey the exact identity

```text
σ(2515→2732)+σ(2732→2515)
=||p_2732-p_2515||²
=7483297332566443473545639014736977851768269427521393251357/500000000000000000000000000000000000000000000000000000000000>0.
```

If neither endpoint were unstable while all external supports stayed positive, both mutual supports would have to be nonpositive, contradicting this identity. Hence at least one of `2515,2732` is unstable throughout the certified sign chamber. Since `C` is independently strict unstable, this chamber has `U≥2`.

The theorem ends if `[2515,2732]` disappears, an endpoint becomes non-extreme, or an external support reverses; it is not a global obstruction to larger complexes.

## 9. First genuinely unclassified successor topology

The exact endpoint incidence determines the next nonserial event:

```text
[2515,2732] -> [2152,2369]   legal forced-edge escape
[1258,B]     -> [3296,D]     legal extra-stable death sheet
[3290,D]     -> [2152,C]     legal saddle sheet
```

The fourth residual saddle `[2369,E]` is **not** ordinarily flippable: its opposite vertices are `C,D`, and `[C,D]` is already a true edge, so a simplicial `2↔2` flip would duplicate an edge.

The first unclassified construction is therefore one higher-valence shared terminal complex coupling the three legal exchanges with a support insertion/deactivation or `2↔3 / 3↔2` event around the nonflippable core `{2369,E,C,D}`. It must solve the three ordinary-volume moments and preserve `[0,1371,C]` and `C`. This is the first topology forced by the exact endpoint chamber, not an exclusion of every larger shared complex.

## 10. Independent clean replay

The replayed package performs:

1. deterministic exact generation from `family_parameters_exact.json`;
2. exact reconstruction of source, central, and target hulls;
3. exact volume and ordinary-centroid integration;
4. complete maximal-face, vertex, and true-edge/full-cone mechanics;
5. exact verification of all four determinant slopes and central supporting slacks;
6. directed interval verification of the `2^-40` own-centroid box;
7. a standard-library-only independent reconstruction importing neither the generator nor `exact_core.py`;
8. OBJ/STL watertightness, Euler, orientation, and edge-multiplicity checks.

The OBJ has 15 vertices, 26 faces, and 39 edge classes; every edge has multiplicity two. The STL has 26 matching facets. :contentReference[oaicite:7]{index=7}

## Reusable artifacts

- [Complete exact NONWINNER bundle](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_exact_NONWINNER.zip) — SHA-256 `74181c1ae51f2b1a54f7bac0b40f72265317c9531aac837c62563beb01fca5c4`.
- [Full Markdown handoff](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_handoff.md)
- [Structured result](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_result.json)
- [Fresh aggregate replay transcript](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_replay.txt)
- [Fresh manifest check](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_manifest_check.txt)
- [Exact family endpoint V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_input_vertices_plus_exact.csv)
- [Exact own-centred V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_vertices_centered_exact.csv)
- [Primitive irredundant H-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_H_irredundant.csv)
- [All maximal faces](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_faces.csv)
- [All true edges and full cones](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_true_edges_full_cones.csv)
- [Exact common-wall certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_common_wall.json)
- [Exact transition atlas](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_transition_atlas.json)
- [Own-centroid perturbation certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_perturbation_certificate.json)
- [Forced-edge certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_forced_edge.json)
- [Next-topology certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_next_topology.json)
- [Independent verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_verify_independent.py)
- [Watertight OBJ](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_body.obj)
- [Watertight STL](sandbox:/mnt/data/Calm_Quartz_90_wall242_four_circuit_body.stl)

## Final statement

**NONWINNER, rigorously delimited.** The literal connected four-circuit incidence event exists and is exact, but it is mechanically pre-empted: replacement equilibria are already present on the negative side, and the positive-side open endpoint remains `(2,2,2)`. The residual true edge `[2515,2732]` forces a second unstable equilibrium in the certified chamber. The first new topology is a higher-valence fifth-circuit shared terminal around `{2369,E,C,D}`; another fixed-cell, deletion-only, cap-only, or serial-flip continuation would repeat an exhausted mechanism.
