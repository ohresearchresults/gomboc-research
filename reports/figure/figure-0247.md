# figure-0247

AI research report · 2026-09-03 UTC

---

# Vivid Atlas 32 — P9-XG11 distributed seven-row target-star split

## Verdict

**EXACT FINITE NONWINNER.** No strict own-centroid `(S,U,H)=(1,1,0)` homogeneous convex polyhedral Gömböc was obtained. The run requires a finite uniform-density body at its own exact ordinary-volume centroid, with actual maximal faces/true edges, exhaustive strict full-cone mechanics, independent verification, and matching meshes.

The exact P9-XG10 source is the 27-supplied/12-active, complexity-60, own-centred `(2,2,2)` body whose only nonprotected obstruction is the singleton all-positive row-star `G`; the journal identifies a six-row target-star split or distributed seven-to-nine-row prism as the first nonrepeating frontier.

I realized a **distributed seven-row closed full-star prism**. It deletes old `G,V0,…,V4`, preserves intended unstable `TR/S102/GT`, and has six independent controls after exact moment elimination. It remains `(2,2,2)` because target and return descendants are joined by a new external-positive true edge `GT-GR`. The obstruction genuinely changes from a singleton sink to a two-row connected component; it is not merely renamed, but it is not cancelled.

## Exact source and transition

Embedded source files are `parent_p9_xg10_edge_carrier_free_exact.json` and `parent_xg10_input_rows_exact.json`.

```text
parent exact SHA-256 = 071d50fa7aa8ef2f4e9f5f6faa3e87df7266e32c5d081f93e58dcd46fa1a7758
parent rows SHA-256  = 22a2cfc94f49f6df3636f40c25e811340eaf2d9fd4fd59afb68b59c512540773
XG11 rows SHA-256    = e48c1f30d264608bbee3bcba13b852d4e83b74863b1290e7609012796d7bfdf8
```

Exact XG10 reconstruction:

```text
supplied/active = 27/12
active = T27, TR, SU, SC1, SA5, S102, G, V0, V1, V2, V3, V4
Q:(V,E,F)=[12, 30, 20]
P:(V,E,F)=[20, 30, 12]
C=60
class=[2, 2, 2]
stable=['T27', 'G']
unstable=[['TR', 'S102', 'G'], ['G', 'V2', 'V4']]
saddles=[['SC1', 'G'], ['S102', 'G']]
```

All 2925 source triples and complete source H/V/E are independently reconstructed. The certified event starts from a `1/4096` homothetic XG10 row hull with all seven future rows strict interior. It is a stronger global full-star transition, not a local path inside the unscaled XG10 `2^-23` chamber.

## Exact successor supports

The endpoint has 34 supplied rows, 11 active irredundant rows, and 23 strict inactive rows.

```text
active   = T27, TR, SA5, S102, GT, R0, GR, R2, R3, R4, R5
inactive = SU, SC1, G_old, M, N, X0, X1, X2, X3, Y0, Y1, Z0, Z1, Z2, W0, W1, W2, W3, V0_old, V1_old, V2_old, V3_old, V4_old
```

Active exact raw supports `q_i·x≤1`:

```text
T27   (-5795/16384, 3447/65536, -379/65536)
TR    (-2609/65536, -1381/65536, -1545/32768)
SA5   (-2667/32768, -6827/65536, -6309/65536)
S102  (-14495/65536, 2571/16384, 1223/16384)
GT    (31649/65536, 2723/65536, 183/8192)
R0    (-5673/65536, -127221/65536, 28553/32768)
GR    (55345/65536, -6483/16384, -16749/65536)
R2    (-2453/32768, -158223/32768, -10479/65536)
R3    (-43523/16384, 142555/65536, 183911/65536)
R4    (24157/65536, 1333/32768, 59327/65536)
R5    (9719/32768, 10639/65536, 6855/65536)
```

All inactive historical rows remain in `input_rows_exact.json`; every one has a positive exact support-slack certificate. The smallest inactive slack is

```text
SC1: 15468675933629/44532596475973 ≈ 0.34735625491711286.
```

Boundedness is certified by positive weights on `T27,TR,GT,R0`:

```text
T27=1751210610851/4818428682400
TR =791261934007/2409214341200
GT =2847893304101/9636857364800
R0 =121495102969/9636857364800,
```

whose weighted row sum is zero. The exact minimum projective denominator is positive; decimal `0.47241241545910184`.

## Complete actual H/V/E incidence

All `C(34,3)=5984` candidate triples were solved exactly; precisely 18 are feasible.

```text
Q:(V,E,F)=[11, 27, 18]
P:(V,E,F)=[18, 27, 11]
C=54
Euler: 11-27+18=2; 18-27+11=2
```

All actual Q facets / primal vertices:

```text
 0 T27/TR/SA5
 1 T27/TR/S102
 2 T27/SA5/R2
 3 T27/S102/R3
 4 T27/R2/R3
 5 TR/SA5/GR
 6 TR/S102/GT
 7 TR/GT/GR
 8 SA5/GR/R2
 9 S102/GT/R5
10 S102/R3/R5
11 GT/GR/R4
12 GT/R3/R4
13 GT/R3/R5
14 R0/R2/R3
15 R0/R2/R4
16 R0/R3/R4
17 GR/R2/R4
```

All 27 true edges:

```text
T27-TR  T27-SA5  T27-S102  T27-R2
T27-R3  TR-SA5  TR-S102  TR-GT
TR-GR  SA5-GR  SA5-R2  S102-GT
S102-R3  S102-R5  GT-GR  GT-R3
GT-R4  GT-R5  R0-R2  R0-R3
R0-R4  GR-R2  GR-R4  R2-R3
R2-R4  R3-R4  R3-R5
```

All 11 maximal-face cycles:

```text
T27   0 2 4 3 1
TR    0 1 6 7 5
SA5   0 5 8 2
S102  1 3 10 9 6
GT    6 9 13 12 11 7
R0    14 15 16
GR    5 7 11 17 8
R2    2 8 17 15 14 4
R3    3 4 14 16 12 13 10
R4    11 12 16 15 17
R5    9 10 13
```

Minimum exact all-supplied nonincidence slack:

```text
4899222464615/143324954983498 ≈ 0.034182619943464006
```

at facet `GT/R3/R4` against `R5`. Exact centred H rows, all exact vertices, face cycles and four-component true-edge data are expanded in the linked H/V/E files.

## Exact ordinary volume and centroid

Exact ordinary volume:

```text
217268181552219662767120308332964781076301265737572632504483692229496079054529619859780655470748172956861129333885736356069190737443264984699299728356299932102383331798788543200960369442140198532615087688669978197731537816626659328/508996465842147390217473213210708572843055618198557519693389896726434610819064737983701698837015289749482953708703022580762862266408050476022825849725068633765411904438903158490720452040001792425141963724475459771816799752120875
```

Decimal mass data:

```text
V=426.85597274775574
M=[-15.795415098769992,3591.4121871033694,-5311.947283014226]
c=[-0.03700408593814865,8.413639298484554,-12.444355056859525].
```

The full exact three moments and centroid rationals are in `exact_mass_centroid.json`. Independent reconstruction proves exactly

```text
Mx-V*cx=0/1
My-V*cy=0/1
Mz-V*cz=0/1,
```

so the translated uniform-density body has exact first moments `(0/1,0/1,0/1)` at its own ordinary-volume centroid. Exact own-centred supports are `H_i=q_i/(1-q_i·c)`.

## Connected positive-volume target-star event

The seven new active rows are `GT,R0,GR,R2,R3,R4,R5`. Their exact row subpolytope has f-vector `[7,15,10]` and supporting triangles

```text
GR/R2/R4
GR/R2/R5
GT/GR/R4
GT/GR/R5
GT/R3/R4
GT/R3/R5
R0/R2/R3
R0/R2/R4
R0/R3/R4
R2/R3/R5
```

A face-to-face tetrahedralization has eight positive cells:

```text
GT/R0/GR/R4  52584599800169/422212465065984
GT/R0/GR/R5  2618422874909/211106232532992
GT/R0/R4/R5  12541679510357/211106232532992
GT/R3/R4/R5  4899222464615/844424930131968
R0/GR/R2/R4  59309164356979/844424930131968
R0/GR/R2/R5  621988455475823/1688849860263936
R0/R2/R3/R5  1501083076177159/844424930131968
R0/R3/R4/R5  839074536422147/844424930131968
```

```text
exact core volume=1920779890866809/562949953421312≈3.411990496123723>0
minimum tetra volume=4899222464615/844424930131968≈0.005801844888508138>0
```

The 11 interior communicating pages are

```text
GR/GT/R0
GR/R0/R2
GR/R0/R4
GR/R0/R5
GT/R0/R4
GT/R0/R5
GT/R4/R5
R0/R2/R5
R0/R3/R5
R0/R4/R5
R3/R4/R5
```

and the tetrahedron-adjacency graph is connected. The complete pre-event row hull is strictly inside the endpoint hull: 612 exact tests pass, with minimum relative slack `205762404713646649231497/213371616355441583325184≈0.9643382199949254`.

```text
pre-event Q≈2.953661073138865e-08
endpoint Q=9019462130455469/1688849860263936≈5.340594414382042
positive shell=1860925540392833776024513752319990448768267/348449143727040986586495598010130648530944≈5.340594384845431.
```

Thus this is an actual connected positive-volume incidence event before moment closure, not a same-incidence metric move or serial page.

## Literal predecessor-packet deletion

`G_old,V0_old,…,V4_old` are strict inactive supplied rows after the event. Therefore old stable `G_old`, vertex `G_old/V2_old/V4_old`, and edges `SC1-G_old`,`S102-G_old` are absent from the actual hull and mechanics. `TR/S102/GT` is actual, while `GT` and `GR` have distinct complete stars.

The predecessor obstruction was a singleton `G_old` star. The successor obstruction is edge `GT-GR`, incident to `TR/GT/GR` and `GT/GR/R4`; its endpoints and link differ. The old packet is deleted, not relabelled or transported along an old page.

## Exhaustive equilibrium audit

At its exact own centroid:

```text
class=[2, 2, 2]
stable=['T27', 'GR']
unstable=[['TR', 'S102', 'GT'], ['R0', 'R3', 'R4']]
saddles=[['SA5', 'GR'], ['S102', 'R5']]
```

Every maximal face is tested against every true neighbour; every actual vertex is solved in its full active normal cone; every true edge is audited with `t,1-t,alpha,beta`.

```text
stable support         0.26975038979409033
face exclusion         0.0025618948068103975
unstable cone          11.85956003732908
vertex exclusion       4.979798317439422
saddle cone            1.5825571831035405
nonsaddle exclusion    0.5776387581748196
```

## Complete directed row-star graph and exact obstruction

`directed_arrow_ledger.json` contains both mutual arrows, every external arrow on every true edge, every full active-row star, selected negative ascent arrows, and all new-row vertex cones. The all-positive row sinks are exactly

```text
T27, GR.
```

The unique nonprotected external-positive edge is `GT-GR`. Every other non-sink row has an exact negative outgoing arrow and an increasing selected path ending at one of those two sinks.

For `GT-GR`, all external arrows at both endpoints are positive. Exact minimum external arrow and both mutual arrows are fully expanded in `component_obstruction_certificate.json`; decimals are

```text
minimum external=0.09292208792175335
A(GT→GR)=-0.0824530182288083
A(GR→GT)=0.3261004334010867
||H_GT-H_GR||²=0.2436474151722784.
```

The exact identity `A(GT→GR)+A(GR→GT)=||H_GT-H_GR||²>0` forces one endpoint stable; here it is `GR`. Protected `T27` is independently stable, so `S≥2` throughout the certified incidence/external-sign chamber.

Residual block:

```text
extra stable=GR
extra unstable=R0/R3/R4
saddles=SA5-GR, S102-R5
forcing component=GT-GR.
```

The requested unique-`T27` sink graph is not achieved.

## Shape rank after moment elimination

The three dependent centring controls have exact Jacobian `-I_3`, determinant `-1`. Six independent controls remain:

```text
u1=T27_z, u2=R0_z, u3=GT_y,
u4=S102_z, u5=GT_z, u6=SA5_x.
```

They monitor two core-page orientations, the `GR-GT` stable wall, the `R0/R3/R4` source wall, and both saddle walls. The exact `6×6` determinant is nonzero; decimal `-507773092.64868176`. Normalized singular values are

```text
[1.422027114484215,1.146436810872023,1.0003789476294918,0.9300192647438228,0.6958252410894219,0.5600490037105705].
```

## Directed perturbation chamber

Outward-rounded intervals certify all 102 raw coordinates independently for

```text
|δq_ij|≤2^-42=2.2737367544323206e-13.
```

The box preserves actual incidence, inactive rows, boundedness, centroid enclosure, strict `(2,2,2)` mechanics, the connected event, deletion, complete arrow graph, and the `GT-GR` theorem.

```text
V∈[426.85597220502285,426.8559732904891]
cx∈[-0.03700408702829257,-0.03700408484800426]
cy∈[8.4136392699435,8.413639327025605]
cz∈[-12.444355098056922,-12.444355015662126]
```

Rigorous lower bounds include nonincidence `0.03418261993900162`, projective denominator `0.4724124133293452`, stable support `0.26975038186252454`, face exclusion `0.002561894741840363`, unstable cone `11.859559571593886`, saddle cone `1.5825566131146256`, inactive slack `0.34735625491173744`, core tetra volume `0.005801844887934714`, external component arrow `0.09292208522222317`, and edge length squared `0.24364740189078612`. `2^-42` is the largest tested accepted dyadic radius.

## Independent replay and watertight meshes

The clean verifier imports neither the generator nor `exact_core.py`. It independently reconstructs all source/pre-event/endpoint intersections, H/V/E, exact mass, every full equilibrium cone, event geometry, deletion, arrows, controls, interval box, and mesh multiplicities. It ends

```text
P9_XG11_INDEPENDENT_CLEAN_ROOM_PASS
```

with report verdict `P9_XG11_INDEPENDENT_CLEAN_ROOM_EXACT_NONWINNER_PASS`.

```text
OBJ: 18 vertices, 27 edges, 11 maximal faces, Euler 2, watertight
STL: 32 triangles, 48 triangle edges, every edge twice, watertight.
```

A clean extraction followed by `./RUN_ALL.sh` ends `ALL P9-XG11 VIVID ATLAS 32 VERIFIERS PASS`.

## Empirical scope and next topology

Completed full-hull searches tested 60,000/50,000/40,000/30,000 random six-/seven-/eight-/nine-row systems, more than 6.7 million fixed-topology centred metric states, sampled MILP screens, and 120,000 coupled old/full-star proposals. No winner appeared. Interrupted jobs are excluded. These are discovery observations, not global impossibility claims.

The exact theorem closes only this distributed seven-row endpoint and its `2^-42` chamber. The smallest unrepresented topology is an **eight-row annular/antiprismatic full-star collar** with no boundary edge `GT-GR`: target and return descendants communicate through at least two interior rows/pages, with two vertex-disjoint boundary routes, negative external arrows at both descendants, and at least seven post-moment controls. An equivalent nonsimple `2↔3/3↔2` collapse may internalize `GT-GR`. If that still creates a forcing component, the next escalation is a distributed nine-to-twelve-row target-star disk whose directed ascent graph is constructed with `T27` as its unique sink.

No strict own-centroid `(1,1,0)` body is claimed.

## Artifacts

- Complete exact ZIP (`P9_XG11_DISTRIBUTED_SEVEN_ROW_TARGET_STAR_EXACT_NONWINNER.zip`)
- ZIP SHA-256 (`P9_XG11_DISTRIBUTED_SEVEN_ROW_TARGET_STAR_EXACT_NONWINNER.zip.sha256`)
- Standalone handoff (`RESEARCH_HANDOFF.md`)
- Final summary (`FINAL_SUMMARY.json`)
- Exact rows (`input_rows_exact.json`)
- Complete exact ledger (`p9_xg11_target_star_split_exact.json`)
- Exact mass/centroid (`exact_mass_centroid.json`)
- Connected-event certificate (`shared_event_exact_certificate.json`)
- Deletion certificate (`predecessor_packet_deletion_certificate.json`)
- Directed-arrow ledger (`directed_arrow_ledger.json`)
- Arrow table (`external_arrow_table.csv`)
- Residual obstruction (`component_obstruction_certificate.json`)
- Rank-six controls (`control_rank_certificate.json`)
- `2^-42` box (`perturbation_box_certificate.json`)
- Exact H table (`H_supplied_exact.csv`)
- Exact V table (`V_exact.csv`)
- Maximal faces (`maximal_faces.csv`)
- True-edge cones (`true_edges_full_cones.csv`)
- Independent verifier (`verify_independent.py`)
- Independent report (`independent_verification_report.json`)
- Watertight OBJ (`p9_xg11_target_star_split_centered.obj`)
- Watertight STL (`p9_xg11_target_star_split_centered.stl`)
- Packaged verifier transcript (`RUN_ALL_OUTPUT.txt`)
- Clean-extraction transcript (`P9_XG11_CLEAN_VERIFY.txt`)

Archive SHA-256:

```text
aaa902290fee38d48721f77dbf05a2b0c33f3e94335ad6d446ad6ccddf486054
```
