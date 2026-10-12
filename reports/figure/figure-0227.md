# figure-0227

AI research report · 2026-09-02 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Vivid Atlas 32 — P9-XG8 exact three-row double-cap

## Determination

**Exact finite NONWINNER.** The requested three-row hexahedral/octahedral double-cap was realized, but no homogeneous convex polyhedral Gömböc was obtained. The target requires a materialized uniform-density body at its own exact volume centroid with strict `(S,U,H)=(1,1,0)`, complete actual incidence and full-cone verification; auxiliary-centre, smooth, wall, near-solution, or unexpanded-generator objects are excluded.

The journal’s accepted predecessor is P9-XG7 with 15 supplied/13 active rows, primal `(22,33,13)`, own-centred `(2,2,2)`, and overlapping forcing edges `X2-Y1`,`X3-Y1`; it explicitly identifies the three-row double-cap as the next unclassified topology.

## What changed

Three exact dyadic rows

```text
Z0=(69965,-12012,5329)/256
Z1=(77082,-17837,-1141)/256
Z2=(48907,-14806,-5116)/256
```

replace the entire XG7 residual disk in one positive-volume communicating event. Both old forcing edges `X2-Y1`,`X3-Y1`, stable `Y1`, unstable vertex `SU/S102/Y0`, and saddles `SA5-Y1`,`S102-Y0` disappear from the actual hull. `T27` and intended unstable lineage `TR/S102/G` survive. A distinct replacement block is born: stable `Z2`, unstable `T27/SU/Z0`, saddles `SA5-Z2`,`S102-Z0`, and forcing edge `Z1-Z2`.

## Exact supplied H-data

For `P_raw={x:q_i·x<=1}`, let `c` be its exact ordinary-volume centroid and set `P=P_raw-c`; exact own-centred rows are `H_i=q_i/(1-q_i·c)`.

```text
T27  (-7125242734162057/140737488355328, 265769074670437/35184372088832, -63255401657691/70368744177664) [active]
TR   (-892363419092795/281474976710656, -235941426090029/140737488355328, -528766574131575/140737488355328) [active]
SU   (-544131479513675/140737488355328, -96790958131853/35184372088832, 118288508214145/140737488355328) [active]
SC1  (-276717838830129/140737488355328, -1302539451900877/140737488355328, -228646779652985/70368744177664) [active]
SA5  (-1735735365091297/281474976710656, -2190132466616797/281474976710656, -2075306589585777/281474976710656) [active]
S102 (-1745325229249529/70368744177664, 5268329269809467/281474976710656, 1934562100355505/281474976710656) [active]
G    (1595031506620615/70368744177664, 69636553284589/35184372088832, 72284311426759/70368744177664) [active]
M    (1529073462/16777216, -268643187/16777216, 58067364/16777216) [inactive]
N    (1529492441/16777216, -268486070/16777216, 58329226/16777216) [inactive]
X0   (1919121502/16777216, -309962234/16777216, 99003968/16777216) [inactive]
X1   (1848158428/16777216, -383623901/16777216, 89362767/16777216) [inactive]
X2   (2073127498/16777216, -414482154/16777216, 17864224/16777216) [inactive]
X3   (1956031545/16777216, -324421554/16777216, 24586561/16777216) [active]
Y0   (1763461327/16777216, -218740469/16777216, 159462489/16777216) [inactive]
Y1   (1040743361/8388608, -206745211/8388608, -2371163/16777216) [inactive]
Z0   (69965/256, -12012/256, 5329/256) [active]
Z1   (77082/256, -17837/256, -1141/256) [active]
Z2   (48907/256, -14806/256, -5116/256) [active]
```

All seven inactive rows `M,N,X0,X1,X2,Y0,Y1` have exact positive support slacks. The active irredundant set is `T27,TR,SU,SC1,SA5,S102,G,X3,Z0,Z1,Z2`.

## Complete actual incidence

```text
Q:(V,E,F)=(11,27,18)
P:(V,E,F)=(18,27,11)
complexity=54
Euler: 11-27+18=2; 18-27+11=2
```

All 18 actual Q facets / primal vertices:

```text
 0 T27/TR/SA5
 1 T27/TR/S102
 2 T27/SU/SC1
 3 T27/SU/Z0
 4 T27/SC1/SA5
 5 T27/S102/Z0
 6 TR/SA5/Z2
 7 TR/S102/G
 8 TR/G/Z2
 9 SU/SC1/Z0
10 SC1/SA5/Z2
11 SC1/Z0/Z1
12 SC1/Z1/Z2
13 S102/G/X3
14 S102/X3/Z0
15 G/X3/Z2
16 X3/Z0/Z1
17 X3/Z1/Z2
```

All 27 true edges:

```text
T27-TR  T27-SU  T27-SC1  T27-SA5
T27-S102  T27-Z0  TR-SA5  TR-S102
TR-G  TR-Z2  SU-SC1  SU-Z0
SC1-SA5  SC1-Z0  SC1-Z1  SC1-Z2
SA5-Z2  S102-G  S102-X3  S102-Z0
G-X3  G-Z2  X3-Z0  X3-Z1
X3-Z2  Z0-Z1  Z1-Z2
```

All 11 maximal-face cycles:

```text
T27   0 4 2 3 5 1
TR    0 1 7 8 6
SU    2 9 3
SC1   2 4 10 12 11 9
SA5   0 6 10 4
S102  1 5 14 13 7
G     7 13 15 8
X3    13 14 16 17 15
Z0    3 9 11 16 14 5
Z1    11 12 17 16
Z2    6 8 15 17 12 10
```

All `C(18,3)=816` candidate triples were solved exactly; precisely these 18 are feasible. Minimum exact all-supplied nonincidence slack is `1827008470662835516334986186628192348470989/9653706130739247930971034694417277970339069952` (`0.00018925461847707286`).

## Exact mass and own centroid

The full exact rational ordinary volume, three raw first moments and centroid coordinates are expanded in `exact_mass_centroid.json` and `p9_xg8_double_cap_exact.json#/after/mass`. Numerically:

```text
V=0.001129446301853995
M=(-8.5549567881034233e-06,1.4293702992245017e-05,-3.2673133718537217e-05)
c=(-0.0075744696972847615,0.012655495855608002,-0.028928452521296506)
```

The exact verifier proves `M_i-V*c_i=0/1` for all three coordinates, so the translated physical body's first moments are exactly `(0/1,0/1,0/1)`. A positive four-row barycentric certificate proves boundedness; the minimum exact projective denominator is positive (`0.49492167676360316`).

## Shared positive-volume event and deletion proof

The predecessor/new row hulls have six common facets; a 16-triangle disk is replaced by a 12-triangle disk with the same octagonal boundary `G-TR-SA5-SC1-SU-T27-S102-X3-G`. Exact row-hull volume increases by `271108200196753155956186344892815123868640533953/8362779449448983678075894352243135564742656` (`32418.432392667757`).

The communicating core is

```text
[0,Z0,Z1,Z2] volume 297102460067/100663296
[0,X3,Z0,Z1] volume 22828333192926061/3298534883328
[0,X3,Z1,Z2] volume 29007041539263407/6597069766656
```

with exact total `31378204916022147/2199023255552` (`14269.155561133697`). The first two cells communicate through `[0,Z0,Z1]`, the first and third through `[0,Z1,Z2]`, and the cap pair through `[0,Z1,X3]`; exact opposite-side determinants are nonzero with opposite signs.

After the event, `X2,Y0,Y1` are strict inactive rows and occur in no actual facet. Neither old forcing edge nor either old saddle/source carrier exists. New edge `Z1-Z2` has incident facets `SC1/Z1/Z2`,`X3/Z1/Z2`, endpoint set `Z1,Z2`, and link `SC1-X3`, different from both old endpoint/link pairs; this is deletion, not renaming.

## Exhaustive mechanics

At the exact own centroid:

```text
stable:   T27, Z2
unstable: T27/SU/Z0; TR/S102/G
saddles:  SA5-Z2; S102-Z0
class:    (2,2,2)
```

Every maximal face, every actual vertex full cone, and all four components `t,1-t,alpha,beta` of every true-edge cone were checked exactly. Category minima are

```text
stable support        73.04171804117037
face exclusion        3.7000532521031477
unstable coefficient  0.017128299067622105
vertex exclusion      0.00037384782043663189
saddle component      0.00039555435343013271
edge exclusion        4.1875291182430359e-06
```

## Shape rank and open box

The three dependent centring controls have exact Jacobian `-I_3`. Five independent post-moment controls `SA5_z,Z2_z,S102_y,SA5_y,T27_z` act on the shared-cell determinant, stable death, source death, and the two saddle deaths. Their exact `5x5` determinant is nonzero; decimal `-0.00090313397992592022`, with normalized singular values `1.770783778, 1.008883033, 0.8137057899, 0.4192386524, 0.09274522406`.

Directed outward-rounded intervals prove that all 54 raw coordinates vary independently by `2^-25` while preserving incidence, inactivity, exact-centroid enclosure, `(2,2,2)`, the communicating core, old-component deletion, and the new forcing theorem. Selected lower bounds are: nonincidence `0.00018893971102140747`, nonsaddle exclusion `2.053335820261874e-06`, inactive slack `0.13511800070031474`, core tetra volume `2951.4473232773025`, forcing external support `905.06143533773729`.

## Exact obstruction

`Z1-Z2` is the unique non-`T27` true edge for which every external directed stable support at both endpoints is positive. The identity

```text
A(Z1->Z2)+A(Z2->Z1)=||H_Z1-H_Z2||^2>0
```

forces at least one endpoint stable throughout the certified chamber; at the anchor it is `Z2`. Since `T27` remains independently stable, `S>=2`. This closes this exact endpoint chamber, not the full three-row realization space.

## Search and continuation

Exact/full-hull discovery campaigns tested 20,000 three-row, 20,000 four-row, 20,000 five-row, and 120,000 corrected three-row proposals, obtaining respectively 1,213, 573, 250 and 3,125 valid full hulls and no `(1,1,0)` state. These counts are empirical only.

The smallest genuinely new successor is a **four-row closed octahedral/hexahedral two-cell** that deletes `Z1-Z2`, source `T27/SU/Z0`, stable `Z2`, and both saddles in one common positive-volume event with two communicating interior pages, while preserving `T27` and `TR/S102/G` and retaining at least five post-moment shape controls.

## Verification and artifacts

The clean-room verifier imports neither generator nor exact-core code and ends `P9_XG8_INDEPENDENT_CLEAN_ROOM_PASS`. OBJ has `18/27/11`, Euler two, and every polygon edge twice. STL has 32 triangles and every triangle edge twice. Clean extraction ends `ALL P9-XG8 VIVID ATLAS 32 VERIFIERS PASS`.

- Complete exact package (`P9_XG8_VIVID_ATLAS_32_EXACT_NONWINNER.zip`)
- Archive SHA-256 (`P9_XG8_VIVID_ATLAS_32_EXACT_NONWINNER.zip.sha256`)
- Complete handoff (`RESEARCH_HANDOFF.md`)
- Exact rows (`input_rows_exact.json`)
- Complete exact ledger (`p9_xg8_double_cap_exact.json`)
- Exact mass/centroid (`exact_mass_centroid.json`)
- Shared-event certificate (`shared_event_exact_certificate.json`)
- Deletion certificate (`inherited_component_deletion_certificate.json`)
- Obstruction certificate (`component_obstruction_certificate.json`)
- Perturbation certificate (`perturbation_box_certificate.json`)
- Independent verifier (`verify_independent.py`)
- Verification report (`independent_verification_report.json`)
- OBJ (`p9_xg8_double_cap_centered.obj`)
- STL (`p9_xg8_double_cap_centered.stl`)
- Clean verification transcript (`P9_XG8_VIVID_ATLAS_32_CLEAN_VERIFY.txt`)

Archive SHA-256: `c5387e767c7cd7a26979caab789c5e21be8832f7dcf1560af6d39e3b9cdc53ab`.

## Uncertainty

No strict `(1,1,0)` body is claimed. The exact result closes only the displayed 54-coordinate `2^-25` chamber; other three-row placements, coupled old-plane deformations, and the stated four-row successor remain unclassified.
