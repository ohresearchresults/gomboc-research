# figure-0127

Historical AI scientific report · saved 2026-08-28 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Calm Lynx 78 — exact inner-star lens continuation

## Verdict

**No homogeneous convex polyhedral Gömböc was obtained.** The continuation does, however, complete the local task that remained open after the certified outer-star relay.

Starting from the exact hard-centred outer `b=9` cell, I changed only the paired source rows `2184` and `2166`, kept them in exact half-turn symmetry, retained the same three distributed support modes as the dependent variables solving all three ordinary first moments, and traversed the actual rebuilt face lattices along an exact rational path. Two paired circuit events occur before the inherited inner stable primitives reverse sign. At the endpoint:

- outer W1, W2, and W3 remain strictly crossed;
- the next paired outer-row deactivation remains strictly un-crossed;
- both inherited inner primitives `(2184,2149)` and `(2166,2131)` are strictly **negative**;
- rows `2184,2166,2219,2201` are all rigorously nonstable;
- all 4,324 support rows remain irredundant;
- a 180-bit outward fixed-dyadic Krawczyk computation isolates a unique exact zero of all three ordinary first moments.

The exact centred endpoint nevertheless has the exhaustive class

\[
(S,U,H)=(291,305,594),
\]

so it is decisively not a Gömböc. The first directed global obstruction beyond the completed local relay is the stable row/witness pair `(2860,2825)`, with the intended half-turn-index mate `(2878,2843)` also strictly stable. Their positive primitives are about `1.2065592e-6`. Together with the protected target row `0`, they prove `S>=3` throughout the certified root box independently of the other 288 stable faces.

## 1. Exact predecessor reconstruction and deterministic endpoint

The predecessor is the exact source from the earlier outer-star archive:

```text
predecessor_outer/outer_b9_source_rows_modes.hex
SHA-256 a41e2c769f66d2ea6eb0bfb4be09ac77768d88169a13f3eab2500ac5854cef85
```

The canonical continuation source is:

```text
data/source_rows_modes.hex
SHA-256 9034e6598ea08c7eb8119d1b1aa9f146857c04a3c7d0431a6d6bb4776d5ef6ef
```

Every hexadecimal binary64 token is interpreted as the exact dyadic rational represented by that token. The source differs from the predecessor at exactly two rows:

```text
q_2184 = (-0x1.db5ca473a1034p-8,
          -0x1.14ff6bcc5b763p-4,
          0x1.fdb9a87d91e13p-1)

q_2166 = (-0x1.db5ca473a1034p-8,
          0x1.14ff6bcc5b763p-4,
          -0x1.fdb9a87d91e13p-1)
        = diag(1,-1,-1) q_2184 exactly.
```

All 12,972 distributed-mode coefficients are unchanged. `src/generate_inner_lens_endpoint.py` regenerates the source, rebuilds the actual polar hull, solves the floating seed for the three moments, and materializes the normative topology input. `data/inner_lens_generator.json` certifies the two changed rows, the two source hashes, exact half-turn equality, and the endpoint counts.

For the exact source rows `q_i^0` and mode values `F_i`, define

\[
u_i(t)=1+F_i\cdot t,\qquad
P(t)=\{x\in\mathbb R^3:q_i^0\cdot x\le u_i(t)}.
\]

Inside each rebuilt simplicial polar cell, every primal vertex on active triple `T` is

\[
p_T(t)=(Q_T^0)^{-1}u_T(t),
\]

so volume is cubic and every ordinary first moment is quartic with exact rational coefficients.

## 2. Actual path, exact circuit order, and rebuilt face lattices

The exact path is

\[
q_i(s)=(1-s)q_i(pre)+s q_i(end),\qquad i\in\{2166,2184\},\qquad 0\le s\le1,
\]

with all other source rows and all three mode fields fixed. Exact half-turn symmetry of the moving pair holds for every rational `s`.

Every sample below has its own actual hull rebuild and a unique 180-bit Krawczyk-isolated three-moment root. The topology signatures are SHA-256 hashes of the rebuilt active-triple sets.

| cell | exact `s` | topology | C1 north/south | C2 north/south | inherited inner signs |
|---|---:|---|---|---|---|
| `C0` | `0` | `3d04fa102a60…` | `positive/positive` | `positive/positive` | `—` |
| `C1_pre` | `191/16384` | `3d04fa102a60…` | `positive/positive` | `positive/positive` | `—` |
| `C1_post` | `3/256` | `d63b45524dd3…` | `negative/negative` | `positive/positive` | `—` |
| `C2_pre` | `17/128` | `d63b45524dd3…` | `negative/negative` | `positive/positive` | `—` |
| `C2_post` | `9/64` | `329061511516…` | `negative/negative` | `negative/negative` | `—` |
| `InnerSign_lo` | `39/40` | `329061511516…` | `negative/negative` | `negative/negative` | `positive/positive` |
| `InnerSign_hi` | `49/50` | `329061511516…` | `negative/negative` | `negative/negative` | `negative/negative` |
| `C2_endpoint` | `1` | `329061511516…` | `negative/negative` | `negative/negative` | `negative/negative` |

### Event 1 — paired C1 exchange

```text
191/16384 < s_C1 < 3/256
north circuit: (2113,2148,2149,2184)
south circuit: (2095,2130,2131,2166)
```

The lower directed determinants are positive (`~1.680495e-11`) and the upper determinants are negative (`~-4.87651e-12`). The actual facet exchange removes

```text
(2095,2130,2166)
(2095,2131,2166)
(2113,2148,2184)
(2113,2149,2184)
```

and adds

```text
(2095,2130,2131)
(2113,2148,2149)
(2130,2131,2166)
(2148,2149,2184).
```

### Event 2 — paired C2 exchange

```text
17/128 < s_C2 < 9/64
north circuit: (2149,2184,2219,2220)
south circuit: (2131,2166,2201,2202)
```

The lower determinants are positive (`~5.0628339e-8`) and the upper determinants are negative (`~-9.9519040e-8`). The actual exchange removes

```text
(2131,2166,2202)
(2149,2184,2220)
(2166,2201,2202)
(2184,2219,2220)
```

and adds

```text
(2131,2166,2201)
(2131,2201,2202)
(2149,2184,2219)
(2149,2219,2220).
```

### Inherited inner primitive reversal

Inside the already rebuilt C2 cell,

```text
39/40 < s_inner < 49/50.
```

At `39/40`, both inherited primitives are positive (`~2.9929149e-6`); at `49/50`, both are negative (`~-6.7705705e-6`). The active-triple topology is unchanged across that sign reversal.

The exact order is proved by the rational inequalities

```text
3/256 < 17/128
9/64  < 39/40.
```

The net predecessor-to-endpoint topology removes exactly these eight facets:

```text
(2095,2130,2166)
(2095,2131,2166)
(2113,2148,2184)
(2113,2149,2184)
(2131,2166,2202)
(2149,2184,2220)
(2166,2201,2202)
(2184,2219,2220)
```

and adds exactly:

```text
(2095,2130,2131)
(2113,2148,2149)
(2130,2131,2166)
(2131,2166,2201)
(2131,2201,2202)
(2148,2149,2184)
(2149,2184,2219)
(2149,2219,2220).
```

The complete path certificate, every determinant interval, every topology hash, and every actual-cell root box are in `certificates/inner_path_actual_cell_atlas.json` and `path_cells/*`.

### Root boxes in every traversed actual cell

**C0**, `s=0/1`

```text
  t0 in [-0.0325690799296600801198633760515069780, -0.0325690799296600801198633760494060536]
  t1 in [1.01630428158726372813993029810954184e-13, 1.01630428158726389325807508222133255e-13]
  t2 in [9.25218544727029510653656860635504351e-13, 9.25218544727029516852025270239979459e-13]
```

**C1_pre**, `s=191/16384`

```text
  t0 in [-0.0325690782877014484256310382036528621, -0.0325690782877014484256310381914495550]
  t1 in [1.01630416508889923313063508476765624e-13, 1.01630416508889942568456310533378910e-13]
  t2 in [9.25218595063686626865295416232848111e-13, 9.25218595063686641074203235477528376e-13]
```

**C1_post**, `s=3/256`

```text
  t0 in [-0.0325690782793556820737269837522315046, -0.0325690782793556820737269837492272850]
  t1 in [1.01630416448419665866913159026401103e-13, 1.01630416448419683505448335945831176e-13]
  t2 in [9.25218595332025421858669146752316874e-13, 9.25218595332025430272239330952103656e-13]
```

**C2_pre**, `s=17/128`

```text
  t0 in [-0.0325690668373536895643223925204861848, -0.0325690668373536895643223925151478360]
  t1 in [1.01630306751171842986928774388260809e-13, 1.01630306751171856903441576990763838e-13]
  t2 in [9.25219226518805410080361531218953453e-13, 9.25219226518805425831404173118649988e-13]
```

**C2_post**, `s=9/64`

```text
  t0 in [-0.0325690664473738598241113907157872753, -0.0325690664473738598241113907140054975]
  t1 in [1.01630300570956607514923124121312861e-13, 1.01630300570956612143689456915639547e-13]
  t2 in [9.25219272727364640489144276304523628e-13, 9.25219272727364646787602124348038789e-13]
```

**InnerSign_lo**, `s=39/40`

```text
  t0 in [-0.0325690611180893822277637827199761988, -0.0325690611180893822277637827092812084]
  t1 in [1.01630253186317142514020840673701634e-13, 1.01630253186317144219061137354473908e-13]
  t2 in [9.25219930481032623402720983535009853e-13, 9.25219930481032626791510528033916059e-13]
```

**InnerSign_hi**, `s=49/50`

```text
  t0 in [-0.0325690611170236089378731914734747589, -0.0325690611170236089378731914619919380]
  t1 in [1.01630253183412648112881109688139277e-13, 1.01630253183412669277788797565908336e-13]
  t2 in [9.25219930873273304451478835788587862e-13, 9.25219930873273316810018493861330324e-13]
```

**C2_endpoint**, `s=1/1`

```text
  t0 in [-0.0325690611131498102189866006309118316, -0.0325690611131498102189866006286499870]
  t1 in [1.01630253172880780134910470954760551e-13, 1.01630253172880784922724605891048624e-13]
  t2 in [9.25219932367819856915039701748603301e-13, 9.25219932367819858552370499705735043e-13]
```

No claim is made that the whole real `s` interval is a single four-dimensional implicit-function tube. The certificate is an exact finite chamber atlas: every listed rational sample is rebuilt, and every listed moment root is separately isolated.

## 3. Unique exact ordinary-centroid root of the endpoint

The floating dyadic centre used to seed the interval proof is

```text
t = (-0.0325690611131496526864381735322240274,
     1.01617058106212572807178406768642522e-13,
     9.25273340973252695315901458163961045e-13).
```

The first 180-bit Krawczyk image contracts to

```text
t0 in [-0.0325690611131498102189866006309118316,
       -0.0325690611131498102189866006286499870]

t1 in [1.01630253172880780134910470954760551e-13,
       1.01630253172880784922724605891048624e-13]

t2 in [9.25219932367819856915039701748603301e-13,
       9.25219932367819858552370499705735043e-13].
```

A second Krawczyk application contracts the coordinate widths to approximately

```text
(5.44e-41, 8.15e-41, 8.72e-41).
```

The first-box Jacobian determinant is

```text
[41.0879045709012221266154213870035859,
 41.0879045709012221266154213870035859],
```

and therefore excludes zero. The volume interval is

```text
[4.17956168778191018199409389256447985,
 4.17956168778191018199409392923668521].
```

All three moment intervals contain zero only within widths below `1.6e-26`. Strict Krawczyk inclusion proves exactly one root of all three ordinary first moments, so the construction origin is exactly the body's own uniform-volume centroid.

## 4. Local relay inequalities at the exact own centroid

At the endpoint root, directed intervals prove:

```text
inner north (2184,2149):
[-0.00001652300052681037893784561720587546,
 -0.00001652300052681037893784561390367707]

inner south (2166,2131):
[-0.00001652300052022984917582142625794781,
 -0.00001652300052022984917582142295574942]
```

Both inherited inner inequalities are therefore strictly open in the requested direction.

The reverse outer exclusions are also strict:

```text
E_(2184,2219) < -0.0035619
E_(2166,2201) < -0.0035619.
```

Thus rows `2184` and `2166` have explicit nonstable witnesses `2149/2131` and `2219/2201`. Rows `2219` and `2201` are excluded by their own strict true-neighbour witnesses.

The outer circuit state is preserved:

```text
W1 north/south       negative
W2 north/south       negative
W3 north/south       negative
next deactivation    positive
```

The smallest absolute directed local circuit margin is the still-positive next-deactivation determinant, approximately `1.4398287311e-8`. Complete exact intervals are in `certificates/local_inner_lens_root_interval.json`.

## 5. Exhaustive own-centroid incidence and equilibrium audit

Over the complete first Krawczyk image:

```text
H rows                         4324, all irredundant
maximal triangular polar faces 8644
primal vertices                8644
true edges                    12966
maximal primal face cycles     4324
surface triangles             17284
class                     (291,305,594)
minimum inactive numerator     1.468921317915317e-9
```

No incidence or equilibrium primitive is ambiguous. The directed global extrema are

```text
minimum positive stable primitive  [0.0000012065592191764564951443610304435, 0.0000012065592191764564951443722321006]
closest negative stable primitive  [-0.0000010503991983975240407890809131187, -0.0000010503991983975240407890703805244]
minimum positive U numerator       [0.0010090022298881810933536998675892, 0.0010090022298881810933537177507889]
closest negative U numerator       [-0.00012010742850521686745489772745948, -0.00012010742850521686745489686592968]
minimum positive saddle component  [0.00096506731006830129515930956337514, 0.00096506731006830129515931021850751]
closest negative saddle component  [-0.00011731445014298523496679376070113, -0.00011731445014298523496679361236023]
```

`certificates/root_full_interval_audit.json` contains all 291 stable-row labels, all 305 unstable-facet labels, all 594 saddle row-pairs, the closest excluded labels, and the complete directed margins. The full four-component normal-cone system is evaluated for every true edge.

## 6. First rigorous obstruction beyond the completed relay

The protected target stable cap remains strict:

```text
row 0, minimum witness row 7:
[0.00094628108434300158446425605302502488403893992,
 0.00094628108434300158446425605302502488403893992].
```

The global minimum positive stable primitive is

```text
row 2860, witness 2825:
[0.0000012065592191764564951443610304435027277671611,
 0.0000012065592191764564951443722321006314730553884].
```

The paired indexed mate is independently strict:

```text
row 2878, witness 2843:
[0.0000012065592483270281898360580657845144350663514,
 0.0000012065592483270281898360692674416431803546116].
```

Every true-neighbour primitive of rows `2860` and `2878` is positive; their complete ledgers are in `certificates/local_inner_lens_root_interval.json`. Hence rows `0,2860,2878` are simultaneously stable throughout the full root box. This exact obstruction survives after both inherited inner primitives have been reversed and after all local outer relay conditions have been preserved.

The obstruction is therefore no longer a lack of local incidence freedom at rows `2149/2184/2131/2166`. It is distributed equilibrium transport: the exact moment correction generates remote stable bands, consistent with the endpoint's full class `(291,305,594)`.

## 7. H/V data, cycles, true edges, interval box, and mesh

The archive supplies:

```text
geometry/root_interval_hv.npz
geometry/root_midpoint_hv.npz
geometry/root_maximal_face_cycles.json
geometry/root_true_edges.csv
geometry/root_midpoint.obj
geometry/root_midpoint.stl
```

`root_interval_hv.npz` contains outward binary64 enclosures derived from exact Fraction evaluation of the dyadic source and the `2^-180` root box. Its arrays include all H rows, all primal vertices, active triples, face-cycle offsets, all 17,284 surface triangles, and all 12,966 true edges. The maximum exported coordinate width is `4.44089209850062616e-16`.

The midpoint visualization has

```text
vertices       8644
triangles      17284
watertight     true
Euler number   2
volume         4.1795616877819102
```

The mesh is only a visualization of the extremely narrow isolated-root box; the exact centred body is the interval-defined root.

## 8. Independent verifier and perturbation information

`src/verify_inner_lens_cleanroom.py` imports none of the construction or interval modules. It independently:

- reparses the normative hexadecimal source;
- proves only rows `2166` and `2184` changed from the predecessor;
- checks their exact half-turn relation and unchanged mode table;
- rebuilds the 4,324-row polar hull;
- matches all 8,644 active triples;
- reconstructs all 4,324 maximal face cycles and 12,966 true edges;
- integrates volume and all three moments;
- recomputes every stable face, unstable vertex, and full edge cone;
- checks the first inactive gap, local relay signs, remote stable pair, H/V data, OBJ, and STL.

Its stored report has `passed=true` and independently reproduces `(291,305,594)`.

The exact L∞ clearance from the entire second Krawczyk image to the boundary of the fully audited first image is

```text
311641993641198405130721/383123885216472214589586756787577295904684780545900544
= 8.134235574091518889745598336264503332601118906333357593357891085381071e-31.
```

This is a fixed-source parameter-box radius: every incidence and equilibrium primitive remains unambiguous within it. It is not advertised as a free source-coordinate perturbation family, because only the isolated moment root is exactly centred.

Run the deterministic smoke verification with

```bash
./[internal-source-reference].sh
```

A fresh root/local recomputation is enabled with

```bash
RECOMPUTE_ROOT=1 ./[internal-source-reference].sh
```

The independent full clean-room reconstruction, exact interval H/V export, and exhaustive directed audit are enabled separately with

```bash
FULL_CLEANROOM=1 ./[internal-source-reference].sh
FULL_INTERVAL_HV=1 ./[internal-source-reference].sh
FULL_DIRECTED=1 ./[internal-source-reference].sh
```

## 9. What changed relative to the preceding handoff

The preceding outer-star result had crossed W3 but hard moment closure left both inherited inner primitives positive. This continuation supplies the missing exact geometry:

1. a deterministic two-row exact half-turn lens control;
2. two actual paired circuit crossings with full hull rebuilds;
3. a third, topology-preserving exact sign reversal of both inherited inner primitives;
4. separately isolated three-moment roots in all eight path cells;
5. preservation of outer W1/W2/W3 signs and the pre-deactivation gate;
6. a unique exact endpoint centroid root;
7. exhaustive H/V/full-edge-cone audit and independent mesh reconstruction;
8. the first rigorous post-relay obstruction, the remote stable rows `2860/2878`.

## 10. Strongest continuation

A serial repair of only rows `2860/2878` is mathematically well-defined but is unlikely to solve the global body because the endpoint has 291 stable faces, 305 unstable vertices, and 594 saddles. The smallest exact local continuation is to replace the complete stars around rows/witnesses

```text
(2860,2825) and (2878,2843)
```

in one paired event, retain the current C2 inner-lens and outer-W3 inequalities, and again eliminate the three ordinary moments as dependent variables. The immediate stopping rule is the first actual circuit in either complete star.

The materially stronger continuation is a distributed multi-relay belt: introduce several separated tangential/incidence controls across the newly stable band, solve the same three moment equations hard, and cross the remote wall set in one connected event rather than chase hundreds of equilibria serially. Any accepted continuation must rebuild every actual hull cell and preserve a directed inactive gap.

## 11. Artifact map

```text
RESEARCH_HANDOFF.md
RESULT.json
MANIFEST.sha256
[internal-source-reference].sh

data/source_rows_modes.hex
data/inner_lens_generator.json
data/root_topology_source.npz

certificates/root3_interval_certificate.json
certificates/inner_path_actual_cell_atlas.json
certificates/local_inner_lens_root_interval.json
certificates/root_full_interval_audit.json
certificates/perturbation_region.json
certificates/cleanroom_verify_report.json
certificates/root_interval_hv_metadata.json

path_cells/*/certificate.json
path_cells/*/topology.npz

geometry/root_interval_hv.npz
geometry/root_midpoint_hv.npz
geometry/root_maximal_face_cycles.json
geometry/root_true_edges.csv
geometry/root_midpoint.obj
geometry/root_midpoint.stl

src/generate_inner_lens_endpoint.py
src/certify_root.py
src/certify_inner_lens_local.py
src/build_inner_path_atlas.py
src/audit_interval.py
src/export_root_interval_hv.py
src/build_geometry.py
src/verify_inner_lens_cleanroom.py
```

## Downloadable artifacts

- [Complete exact/directed archive](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner.zip)
- [Archive SHA-256](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner.zip.sha256)
- [Standalone research handoff](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/RESEARCH_HANDOFF.md)
- [Machine-readable result](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/RESULT.json)
- [Integrity manifest](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/MANIFEST.sha256)
- [Normative exact source](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/data/source_rows_modes.hex)
- [Endpoint root certificate](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/certificates/root3_interval_certificate.json)
- [Actual-cell path atlas](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/certificates/inner_path_actual_cell_atlas.json)
- [Local relay and obstruction certificate](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/certificates/local_inner_lens_root_interval.json)
- [Full interval equilibrium audit](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/certificates/root_full_interval_audit.json)
- [Interval H/V archive](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/geometry/root_interval_hv.npz)
- [Maximal-face cycles](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/geometry/root_maximal_face_cycles.json)
- [True-edge ledger](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/geometry/root_true_edges.csv)
- [Independent clean-room verifier](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/src/verify_inner_lens_cleanroom.py)
- [Clean-room report](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/certificates/cleanroom_verify_report.json)
- [OBJ mesh](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/geometry/root_midpoint.obj)
- [STL mesh](sandbox:/mnt/data/inner_star_lens_own_centroid_nonwinner/geometry/root_midpoint.stl)

Archive SHA-256:

```text
f76ad66b009ba3789683316a043685a15ca06cb2eba7a31a29ec267a40b600c6
```
