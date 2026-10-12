# figure-0304

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Clear Willow 25 — exact shared-interface bifurcated two-cell continuation

## Final disposition

**EXACT NONWINNER.** I did not construct the requested homogeneous convex polyhedral Gömböc. The promoted body, named

```text
J57_BIPY5_shared_interface_exact_NONWINNER
```

is a finite rational uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid. Its exhaustive strict equilibrium class is

```text
(S,U,H)=(2,2,2),
```

not `(1,1,0)`.

The run’s acceptance gate requires a fully materialized body at its own exact volume centroid with one stable maximal face, one unstable vertex, no saddle true edge, exhaustive positive-margin mechanics, independent verification, and matching OBJ/STL; auxiliary-centre, wall, and near-solution objects do not qualify. :contentReference[oaicite:0]{index=0}

The construction nevertheless realizes the first genuinely shared-volume bifurcated successor to the literal parent. Five new exact supports form two full-dimensional tetrahedral cells sharing a genuine internal triangle, all five are active, and three non-collinear true-edge ports attach the complex to the old body. Row `5003` remains strictly nonextreme. The parent carrier edge `(30001,30003)`, parent extra stable row, both parent saddles, and both parent replacement unstable sectors are absent. A new Euler-neutral packet is born instead.

## Immutable deliverables

**Complete archive:** [Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER.zip](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER.zip)  
**Archive SHA-256:** `41b885ec39c9f36be1b2a0a24315923f0ebdf9e658c93f098a7fe960f9018156`  
**Archive bytes:** `29,465,780`  
**Archive checksum:** [ZIP SHA-256 sidecar](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER.zip.sha256)  
**Final delivery hash ledger:** [FINAL_DELIVERY_SHA256SUMS.txt](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER_FINAL_DELIVERY_SHA256SUMS.txt)  
**Readable report:** [README.md](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/README.md)  
**Verification receipt:** [VERIFICATION_RECEIPT.json](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/VERIFICATION_RECEIPT.json)  
**Immutable manifest:** [MANIFEST.sha256](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/MANIFEST.sha256)  
**One-command replay:** [REPLAY.sh](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/REPLAY.sh)  
**Embedded pristine-extraction transcript:** [CLEANROOM_VERIFY.log](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/CLEANROOM_VERIFY.log), SHA-256 `118f540d6530f0c5f736cbcbad08de2d2184a1927f28ca2456f532ebab60c379`  
**Replay of the final archive bytes:** [FINAL_ARCHIVE_REPLAY.log](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER_FINAL_ARCHIVE_REPLAY.log), SHA-256 `9654d95f3e4605dbc56b90bd01eb3671739c1fe37be03d646c5462b1f03ce4c4`  
**Replay-log checksum:** [FINAL_ARCHIVE_REPLAY.log.sha256](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER_FINAL_ARCHIVE_REPLAY.log.sha256)

Both clean runs terminate with

```text
CLEANROOM_J57_BIPY5_ALL_REPLAYS_PASS.
```

## Literal parent authority

The only parent used is

```text
assignment ID       figure-0301
payload SHA-256     e306ea3586d1ac9a3d8df2102afa79daaa6597ccba437c489562cc245356d8fc
endpoint            J56_TET4_swallow5003_exact_NONWINNER
parent source SHA   be6520630eb583443c59b269c037cba31ad2f0434f409f03e55d591428023d20
underlying J55 SHA  ba6f45ae283e444a4ee92ff14e4987041ca4e442a181892675f6b8af00759fa3.
```

The journal records this parent as a material exact topology-changing nonwinner with 22 supplied rows, 19 active rows, inactive `14001,14014,5003`, primal `(34,51,19)`, and strict `(2,2,2)`. :contentReference[oaicite:1]{index=1} Its obstruction is the true dual edge `(30001,30003)`, whose nonmutual external arrows are all positive at both endpoints; the parent’s next unrepresented topology was explicitly the shared-interface two-cell cage attacked here. :contentReference[oaicite:2]{index=2}

The parent exact reconstruction is included inside the archive and independently rechecked by an all-triples GMP program. No alias, unavailable endpoint rational, or recovered orphan-winner datum was used.

## Exact deterministic support construction

Start with the 18 exact J55 support rows serialized in

[the exact J55 source](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/source/J55_D17R_anti_carrier18_exact_source.json),

whose SHA-256 is

```text
ba6f45ae283e444a4ee92ff14e4987041ca4e442a181892675f6b8af00759fa3.
```

The parent’s four tetrahedral-cage rows `30000..30003` are removed. Insert the following terminating decimals, interpreted literally as rational numbers:

```text
q_32000 = ( 0.23873552257277952,
            -0.25187900084732073,
            -0.22221047251637038)

q_32001 = (-0.18300713880597066,
            -1.4977151246165832,
             0.06755653369173062)

q_32002 = (-0.14413055024285018,
            -0.9365296245588979,
             0.2706921073299099)

q_32003 = (-0.36990954062997916,
            -1.4627320839800093,
            -0.2290655860733275)

q_32004 = ( 0.31097476297928495,
            -0.3280170827018585,
             0.3064243650768409).
```

The deterministic implementation is [build_exact_endpoint.py](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/build_exact_endpoint.py), SHA-256 `fe68f5eb0b4c3745072e7412aaf4c6e627f9e8cbed275037d2142966fa20b203`. The complete endpoint source is [endpoint/exact_source.json](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/endpoint/exact_source.json), SHA-256 `24a090f890189f1e0a80129aeaee9fcb1f5a8c50bb9ffe3403d11217d878817c`.

The construction uses the same exact polar-centroid gauge as the parent: build the raw polar `P_raw={x:q_i·x<=1}`, reconstruct its exact primal vertices, integrate its ordinary volume and first moment, and apply `h_i=q_i/(1-q_i·c)` with primal translation `p_v=p_v_raw-c`. The parent payload records this exact centring mechanism. :contentReference[oaicite:3]{index=3}

## Exact two-cell geometry and oriented matroid

The equatorial rows are `32000,32001,32002`. The two apices are `32003,32004`. Define

```text
cell A = [32000,32001,32002,32003]
cell B = [32000,32001,32002,32004]
shared internal interface = [32000,32001,32002].
```

The exact oriented apex determinants are

```text
 8557543819471886696468012619525273193314153698223
 /62500000000000000000000000000000000000000000000000

-8557543819471885944262235804736452662805778678153
 /62500000000000000000000000000000000000000000000000.
```

They have opposite signs. The cells intersect precisely in their common triangular face. Their exact positive volumes are

```text
V_A = 2852514606490628898822670873175091064438051232741
      /125000000000000000000000000000000000000000000000000

V_B = 2852514606490628648087411934912150887601926226051
      /125000000000000000000000000000000000000000000000000,
```

approximately `0.022820116851925032` and `0.02282011685192503`. Their union has exact volume

```text
713128651622657193363760351010905244004997182349
/15625000000000000000000000000000000000000000000000 > 0.
```

The unique five-row affine circuit has signs

```text
---++
```

on `[32000,32001,32002,32003,32004]`, with primitive integer coefficients

```text
[-7606705617308344205429477465657128973072621078350,
 -7606705617308341607452985332348867872764307186795,
 -7606705617308344374757868434342970962322981570023,
 11410058425962514592349647739648603550407704904204,
 11410058425962515595290683492700364257752204930964].
```

Weight zero on the equator and weight one on both apices gives the two tetrahedra as strict lower cells. The exact omitted-point slacks are

```text
5705029212981257546910082808087241952039977458792
/2852514606490628898822670873175091064438051232741

5705029212981257546910082808087241952039977458792
/2852514606490628648087411934912150887601926226051.
```

The lifting is extended to the complete 23-row supplied configuration by one common exact high weight on every retained old row. The minimum old-row lower slack is exactly at least `1`; hence `A,B` are strict lower cells of a global regular subdivision, not only of the five-row subconfiguration.

The complete certificate is [bifurcated_two_cell_certificate.json](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/certificates/bifurcated_two_cell_certificate.json), SHA-256 `e36e6dbbdf73f96738842f06df034de9d47a9eb04b15e2fdc26b40caba00446b`.

## Exact preservation of row-5003 inactivity

Before centroid closure, row `5003` is the strict convex combination

```text
q_5003 = lambda_0 q_32000 + lambda_1 q_32001 + lambda_2 q_32002
       + lambda_3 q_32003 + lambda_4 q_32004,
```

where

```text
lambda_0 = 1629033481599335002081971407397253444465295717687596165
           /5988249683230498833386126826017859412532072503234151688

lambda_1 = 5714745301082138214731607442312056210470211121367675281
           /11976499366460997666772253652035718825064145006468303376

lambda_2 = 238049592896383242529788283312938311780718466073589899
           /19960832277434996111287089420059531375106908344113838960

lambda_3 = 1/20

lambda_4 = 942513490883045674591757392641502832225710049899111107
           /4990208069358749027821772355014882843776727086028459740.
```

All five coefficients are positive and sum exactly to one. The projective ordinary-centroid gauge transports this relation to another strictly positive exact barycentric representation. Thus row `5003` is supplied but strictly inactive in the final own-centred H-representation.

## Exact ordinary volume and moment closure

For every outward boundary triangle with vertices `a,b,c`, the builder uses

```text
V = sum det(a,b,c)/6,
M = sum det(a,b,c)(a+b+c)/24,
c = M/V.
```

The resulting ordinary volume is a positive reduced rational whose numerator has 2,887 decimal digits and denominator has 2,886 decimal digits. Its complete literal fraction is the field `ordinary_volume_exact` in [endpoint/certificate.json](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/endpoint/certificate.json), SHA-256 `91b6502014344bc9d1844ad8e4d528b04d9609ced1b2f5b9304be2d1da78a869`. Numerically,

```text
V = 10.22323320091809...
```

The exact raw centroid is the three-fraction vector in the same immutable certificate; numerically,

```text
c = (0.014307631806471597,
     0.034510568969609384,
    -0.2911740491269681).
```

Every denominator `1-q_i·c` is exactly positive; the minimum decimal diagnostic is `0.93794190947448`. Translating by `-c` after the contragredient support gauge gives the exact identities

```text
Mx=0,
My=0,
Mz=0.
```

The independent verifier recomputes the rational integration rather than trusting these stored values.

## Fresh exact actual hull

All 23 supplied H rows were reconsidered. The actual irredundant hull is

```text
H supplied      23
H active        19
H inactive       4
primal vertices 34
true edges      51
maximal faces   19
Euler           34-51+19=2
complexity      102.
```

Active H rows:

```text
14000,14002,14003,14004,14005,14006,14007,
2475,5000,
14008,14009,14010,14011,14012,
32000,32001,32002,32003,32004.
```

Inactive H rows:

```text
14001,14013,14014,5003.
```

Every inserted row is active. The minimum exact active-face/nonincident-row separation is positive, with decimal diagnostic

```text
0.003707845003880884.
```

The minimum exact inactive-row separation is positive, with decimal diagnostic

```text
0.05703106538952026.
```

The complete supplied-versus-active ledger is [supplied_active.csv](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/endpoint/supplied_active.csv).

### Complete primal vertex incidence

The 34 maximal dual facets, equivalently all actual primal vertices, are

```text
[14000,14002,32001]
[14000,14002,32003]
[14000,32001,32003]
[14002,14003,32003]
[14002,14003,32004]
[14002,32001,32002]
[14002,32002,32004]
[14003,14004,32000]
[14003,14004,32004]
[14003,32000,32003]
[14004,14005,32000]
[14004,14005,32004]
[14005,14006,32000]
[14005,14006,32004]
[14006,14007,32000]
[14006,14007,32004]
[14007,2475,32000]
[14007,2475,32004]
[2475,5000,32000]
[2475,5000,32004]
[5000,14008,32000]
[5000,14008,32004]
[14008,14009,32000]
[14008,14009,32004]
[14009,14010,32002]
[14009,14010,32003]
[14009,32000,32003]
[14009,32002,32004]
[14010,14011,32002]
[14010,14011,32003]
[14011,14012,32002]
[14011,14012,32003]
[14012,32001,32002]
[14012,32001,32003].
```

### Complete maximal primal-face cycles

Vertex IDs in the following cycles refer to the preceding 34-vertex order:

```text
2475 : [18,19,17,16]
5000 : [20,21,19,18]
14000: [2,1,0]
14002: [0,1,3,4,6,5]
14003: [9,7,8,4,3]
14004: [10,11,8,7]
14005: [12,13,11,10]
14006: [14,15,13,12]
14007: [16,17,15,14]
14008: [22,23,21,20]
14009: [26,25,24,27,23,22]
14010: [24,25,29,28]
14011: [28,29,31,30]
14012: [30,31,33,32]
32000: [7,9,26,22,20,18,16,14,12,10]
32001: [5,32,33,2,0]
32002: [5,6,27,24,28,30,32]
32003: [1,2,33,31,29,25,26,9,3]
32004: [8,11,13,15,17,19,21,23,27,6,4].
```

The machine-readable cycles are [face_cycles.json](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/endpoint/face_cycles.json), SHA-256 `0e61dd6ba12927953385f12332e02e11f7cfc66a19ea750377984cb2cebc5e84`.

### Every true edge

The complete true dual/primal edge pairs are

```text
(14000,14002) (14000,32001) (14000,32003)
(14002,14003) (14002,32001) (14002,32002) (14002,32003) (14002,32004)
(14003,14004) (14003,32000) (14003,32003) (14003,32004)
(14004,14005) (14004,32000) (14004,32004)
(14005,14006) (14005,32000) (14005,32004)
(14006,14007) (14006,32000) (14006,32004)
(14007,2475) (14007,32000) (14007,32004)
(2475,5000) (2475,32000) (2475,32004)
(5000,14008) (5000,32000) (5000,32004)
(14008,14009) (14008,32000) (14008,32004)
(14009,14010) (14009,32000) (14009,32002) (14009,32003) (14009,32004)
(14010,14011) (14010,32002) (14010,32003)
(14011,14012) (14011,32002) (14011,32003)
(14012,32001) (14012,32002) (14012,32003)
(32000,32003) (32001,32002) (32001,32003) (32002,32004).
```

The exact edge-to-face incidence table is [true_edges.csv](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/endpoint/true_edges.csv), SHA-256 `40da1b26d49a2d2ff79379fa7843995d39420875da2171a513467aac1271b8a5`. Display triangulation diagonals are absent from this list and from the mechanics audit.

## Exhaustive exact own-centroid equilibrium classification

Every maximal face, every complete incident-edge vertex cone, and all four components

```text
(t,1-t,beta1,beta2)
```

of every true-edge normal cone were recomputed over exact rational arithmetic.

### Stable maximal faces

```text
2475
32003.
```

The minimum strict stable component is at least

```text
0.11302718520297596.
```

Every other active row has an exact negative row-star witness; the minimum exclusion magnitude is

```text
0.003350576013726449.
```

### Unstable primal vertices

The two strict unstable vertices are dual to

```text
[14008,14009,32000]
[14008,14009,32004].
```

Their minimum strict cone component is at least

```text
0.05529524688862481.
```

Every other vertex has an exact negative complete-cone witness; the minimum exclusion magnitude is

```text
0.032511384304328095.
```

### Saddle true edges

The two strict saddles are

```text
(14000,32001)
(14012,32003).
```

All four full-cone components are positive for each. The minimum strict saddle component is at least

```text
0.062368473890994085.
```

Every other true edge has an exact nonpositive component; the minimum exclusion magnitude is

```text
0.025238523131479937.
```

The complete feature-by-feature exact ledger is [mechanics_exact.json](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/endpoint/mechanics_exact.json), SHA-256 `62d0a2014ca0d0ebff871de1dd091cdabb4fd71928b2bb8cdf6d569bd1e2c77a`.

## Physical connectivity and outgoing ports

The new-new true edges are exactly

```text
(32000,32003)
(32001,32002)
(32001,32003)
(32002,32004).
```

Thus the active new-row graph is connected. Three certified old/new true-edge ports are

```text
(32001,14000)
(32000,2475)
(32002,14012).
```

Rows `14000,2475,14012` are non-collinear; the exact positive cross-product norm is recorded in the cell certificate. The two tetrahedra therefore form a genuine full-dimensional communicating support surgery with a two-dimensional shared interface and three non-collinear outlets. It is not an inactive sheet, a disconnected cap collection, or a disguised scalar-port attachment.

## Literal parent-carrier suppression

Rows `30000..30003` are absent from the endpoint supplied set. Consequently all of the following parent features are literally absent from the rebuilt hull:

```text
stable row 30001
forcing edge (30001,30003)
saddle (14002,30001)
saddle (14013,30001)
unstable facet [14006,14007,30002]
unstable facet [5000,14008,30000].
```

Row `5003` remains strictly inactive. The operation therefore passes the parent’s incidence-death gates. It fails because different strict equilibria are born.

## Exact replacement chronology

The canonical shared-volume ingress uses both parent and endpoint support labels:

```text
q_3000k(t)=q_5003+(1-t)(q_3000k(parent)-q_5003),
q_3200k(t)=q_5003+t(q_3200k(endpoint)-q_5003),
```

followed by exact ordinary-centroid closure at each rational sample.

At `t=1/1000`:

```text
class (2,2,2)
stable 2475,30001
saddles (14002,30001),(14013,30001).
```

At `t=3/10`:

```text
class (3,2,3)
stable 2475,30001,32003
unstable [2475,5000,32000], [2475,5000,32004]
saddles (14002,30001), (14013,32003), (30001,32003).
```

The strict coexistence margins at `t=3/10` include

```text
old stable 30001                 0.07762594156502842
replacement stable 32003         0.002689995207035527
old saddle (14002,30001)         0.2956332941450256
replacement saddle (14013,32003) 0.06566898756878672
bridge saddle (30001,32003)      0.031054246301571036.
```

At `t=9/25`:

```text
class (2,2,2)
stable 2475,32003
saddles (14002,30001),(14012,32003).
```

Thus the explicit connected ingress is death-after-birth: the replacement stable and saddle carriers are strict while parent stable row `30001` and an old saddle remain strict. This is an exact finite chamber witness, not a root-complete exclusion of every path in the entire abstract bipyramid realization space.

The certificate is [exact_replacement_chronology.json](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/certificates/exact_replacement_chronology.json), SHA-256 `84cda3575fba42cc5690f6adffe6c454237c6716cedc0be976b1dcd9545c790e`.

## Exact surviving forcing component

True edge `(32001,32003)` has every nonmutual external row-star arrow strictly positive at both endpoints. For adjacent support rows define

```text
A(i->j)=||h_i||^2-h_j·h_i.
```

The exact mutual identity is

```text
A(i->j)+A(j->i)=||h_i-h_j||^2>0.
```

At least one mutual arrow must therefore be positive. Since every nonmutual arrow at both endpoints is already positive, at least one endpoint is a strict stable face throughout the same incidence/sign chamber. The endpoint selects `32003`. Since protected row `2475` is independently stable, every strict realization retaining this carrier incidence and sign pattern satisfies

```text
S>=2.
```

The complete all-edge audit finds exactly these all-positive-external true edges:

```text
(14007,2475)
(2475,5000)
(32001,32003).
```

The first two belong to the protected sink sector. The third is the adverse replacement carrier. The exact audit is [external_arrow_audit.json](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/certificates/external_arrow_audit.json), SHA-256 `ecd77c8f7ff3d6669fd53b10d178c088c6cc4eaf6f571fea1ee5776c41916856`.

The smallest connected residual component has ten named rows and 18 induced true edges. It joins `(32001,32003)`, both surviving saddle sectors, both unstable branches, and protected row `2475`. Its exact graph and connecting paths are in [residual_forcing_component.json](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/certificates/residual_forcing_component.json), SHA-256 `a352fc69deba7398e4f0dec4517dbad1fd23ad07d2565bc8dd68eee6aaeed2b2`.

## Exact perturbation certification

Two linearly independent determinant-one shape families are certified after exact moment closure:

```text
L_xy(s)=[[1,s,0],[0,1,0],[0,0,1]], |s|<=2^-16
L_yz(t)=[[1,0,0],[0,1,t],[0,0,1]], |t|<=2^-16.
```

Primal vertices transform covariantly and supports contragrediently. Incidence and inactivity are exact invariants. Determinant one preserves volume, and the zero ordinary centroid remains zero. For each family, every one of 125 guarded incidence/mechanics primitives is expanded as an exact polynomial and bounded by its coefficient sum.

```text
xy minimum guarded lower bound 0.009826890715939516
yz minimum guarded lower bound 0.009839357244149059.
```

Certificates:

- [XY shear interval](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/certificates/one_parameter_xy_shear_box.json), SHA-256 `c58de019b08b6795ca7192be59f448519a8a71dfdd9e650cae1efd13c5902a8e`
- [YZ shear interval](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/certificates/one_parameter_yz_shear_box.json), SHA-256 `fbe1f6667f2f03a7ccdeac7daa8fe54ea5cba27a288f2b4fcfe39de678fc272e`
- [Independent-direction summary](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/certificates/two_independent_shear_directions.json)

These provide two independent nonzero physical tangent controls after ordinary-moment closure. I do not claim that the full Cartesian product of the two displayed intervals was interval-certified. Pointwise strict rational margins imply some multidimensional open neighbourhood by continuity, but no explicit all-coordinate radius is promoted beyond the two certified axes.

## Independent reconstruction

The final archive replay performs the following without trusting the report:

```text
1. verify the immutable manifest;
2. verify literal parent ID, payload SHA, and exact-source SHA;
3. regenerate the endpoint from exact J55 rows and five rational additions;
4. regenerate the chronology and both shear certificates;
5. recompute exact volume, centroid, and zero first moments;
6. recompute every face, vertex, and four-component edge-cone decision;
7. verify the affine circuit, global regular lifting, shared interface,
   barycentric swallowing, connected graph, and non-collinear ports;
8. audit all changed-edge external arrows and the residual component;
9. compile and run an independent C++/GMP all-triples hull verifier on
   both endpoint and parent;
10. verify watertight OBJ/STL incidence and mass parity;
11. recheck the immutable manifest.
```

Terminal markers include


[Encoded source block omitted; the code in this passage is incomplete.]


The endpoint GMP verifier enumerates

```text
C(23,3)=1771 triples
23155 exact support signs
34 supporting triples
19 active rows
51 true edges.
```

The repaired parent audit enumerates

```text
C(22,3)=1540 triples
21672 exact support signs
34 supporting triples
19 active rows
51 true edges.
```

This supplies the independent all-triples parent reconstruction missing from the previous handoff.

## Watertight display meshes

- [J57_BIPY5_shared_interface.obj](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/mesh/J57_BIPY5_shared_interface.obj), SHA-256 `0893e288585e0061f3d3a4be6ade86df5672f4b1d7fd3874316b10331ab166a6`
- [J57_BIPY5_shared_interface.stl](sandbox:/mnt/data/Clear_Willow_25_J57_BIPY5_shared_interface_exact_NONWINNER/mesh/J57_BIPY5_shared_interface.stl), SHA-256 `9260c9642c2295ace645be7505a03fc6efbc098fd7623e68c0bd5b21a2324acf`

The independent mesh audit gives

```text
vertices             34
display triangles    64
triangulated edges   96
Euler                34-96+64=2
edge multiplicity    exactly 2 for every display edge
OBJ volume           10.22323320091809
OBJ centroid norm    1.03e-16.
```

The STL has identical float32 triangle incidence. Display-only diagonals inside nonsimplicial maximal faces are not counted among the 51 true edges and are absent from the mechanics ledger.

## Empirical realization-space screens

The package preserves, but does not promote as exact exclusions, the following full-hull numerical screens:

```text
5,000 broad cages
8,000 targeted cages
120,000 attempted swallowing triangular bipyramids
584 valid full structures in the swallowing-bipyramid aggregate
metric and projective continuations
tetrahedral cages with one and two scalar ports
bipyramidal, prismatic, octahedral, and cubical cages.
```

No sampled body was `(1,1,0)`. These are finite empirical observations only and do not exclude the full continuous realization space of every possible shared-interface two-cell architecture.

## What changed relative to the parent

The parent result established that a standalone tetrahedron can swallow `5003` but creates an all-positive carrier edge and a strict `(2,2,2)` replacement block. This continuation resolves the next topology exactly:

1. Two full-dimensional cells can be realized with an actual shared triangular interface.
2. All five new supports can remain extreme.
3. Three non-collinear physical ports can be present simultaneously.
4. Row `5003` remains strictly nonextreme.
5. Both endpoints of the parent carrier edge and every parent replacement equilibrium carrier can be deleted literally.
6. Exact ordinary-centroid closure introduces no rank or mass defect.
7. The topology still transfers the packet: the canonical ingress reaches a `(3,2,3)` coexistence cell before the parent block dies.
8. The far chamber has a new exact forcing edge `(32001,32003)` and remains `(2,2,2)` throughout certified nonzero shape intervals.

Thus one genuine shared interface and three outlets are not sufficient. The obstruction is no longer inactivity, lack of volume, lack of centroid freedom, or a missing port. It is the closure of the new support graph around another all-positive external carrier.

## Smallest genuinely nonrepeating successor

A single triangular-bipyramid interface is now represented. The first materially different successor is a **three-cell branched Y-cage**, or a higher-valence regular cell carrying the same freedom, with at least two noncoplanar internal interfaces.

Continuation-critical rows are

```text
{14000,14002,14012,14013,2475,5000,14007,14008,14009,
 32000,32001,32002,32003,32004}.
```

A successful far chamber must satisfy all of the following in a freshly rebuilt actual hull:

```text
1. keep row 5003 strictly nonextreme;
2. make at least one of 32001,32003 nonextreme, or give both endpoints
   independently certified nonpositive external-arrow exits;
3. remove saddles (14000,32001) and (14012,32003) before an adjacent
   replacement edge becomes saddle;
4. destroy one of the two current unstable branches and deliberately retain
   exactly one strict unstable feature;
5. leave row 2475 as the sole stable sink;
6. use two noncoplanar internal interfaces so carrier suppression and the
   two saddle sectors have independent circuit timing;
7. solve all three ordinary first moments exactly while retaining at least
   two independent physical controls;
8. audit every new or star-changed true edge for an explicit nonpositive
   external witness before accepting the chamber.
```

A second isolated tip, one scalar port, another convex-combination belt, a second copy of the same bipyramid, or one-dimensional motion of `32003` repeats a represented mechanism.

## Exact scope

Exact and independently replayed:

```text
- literal parent identity and exact source;
- five rational new support rows;
- complete 23-row supplied and 19-row active H data;
- all 34 primal vertices, 19 maximal face cycles, and 51 true edges;
- boundedness, strict inactivity, and positive incidence separations;
- exact positive ordinary volume and exact zero centred first moments;
- exhaustive strict face, complete vertex-cone, and four-component edge-cone
  classification;
- positive-volume globally regular two-cell complex and shared interface;
- exact row-5003 barycentric inactivity;
- complete external-arrow and residual-forcing audits;
- exact three-sample death-after-birth chronology;
- two independent exact determinant-one shape intervals;
- parent and endpoint GMP all-triples reconstruction;
- watertight OBJ/STL parity;
- pristine and final-archive replays.
```

Not claimed:

```text
- a strict own-centred (1,1,0) body;
- a root-complete exclusion of every path through the abstract bipyramid
  realization space;
- a simultaneous explicitly certified Cartesian product of the two shear
  intervals;
- a global impossibility theorem for every two-cell support surgery.
```

## Final conclusion

**NO GÖMBÖC.** `J57_BIPY5_shared_interface_exact_NONWINNER` is an exact, independently reconstructible 23-supplied-row support polyhedron with actual primal `(V,E,F)=(34,51,19)`, complexity `102`, exact positive uniform volume, exact zero ordinary first moments, five active new supports, a connected positive-volume two-cell regular cage, one genuine shared triangle, three non-collinear ports, strict inactivity of `5003`, and watertight meshes.

It literally removes the complete parent replacement block but does not annihilate it. The endpoint’s strict class is `(2,2,2)`, with stable rows `2475,32003`, unstable vertices dual to `[14008,14009,32000]` and `[14008,14009,32004]`, and saddles `(14000,32001)` and `(14012,32003)`. The smallest surviving forcing component is organized around all-positive external edge `(32001,32003)`. The first genuinely unrepresented continuation is the two-interface branched Y-cage specified above.
