# figure-0182

AI research report · 2026-09-01 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Steady Willow 02 — exact finite handoff

## Disposition: **EXACT NONWINNER**

I reconstructed the accepted exact P9 finite-thickness endpoint and advanced it through a genuinely cross-gap, simultaneous incidence event. The predecessor is the 27-row/12-active own-centred `(V,E,F)=(20,30,12)` body of strict class `(2,2,2)` whose transferred obstructions were stable sinks `o9,o27`, unstable sinks `(o102,XS,XR)` and `(C0,XS,XU)`, and saddles `(A5,C1)` and `(XS,o102)`. Its exact witness obstruction required a successor that removed `o9` and the extra source in one cross-gap cell rather than another serial band.

The new wall event reaches the requested cross-gap **incidence topology**: one moving row crosses two coplanar circuits at the same exact parameter, and the two positive-volume polar cells share the same interior edge. But the decisive self-check breaks the stronger hoped-for conclusion. In the immediate pre-cell, `S9` is no longer stable and `(SC0,SS,SU)` is not unstable; the actual packet has already transferred to stable `SC1,H` and unstable `(SS,SU,S102)`, and those equilibria survive the wall. Thus this is simultaneous carrier deletion, not simultaneous actual sink cancellation. The robust endpoint has **two** stable faces, **two** unstable vertices, and **two** saddle edges, so it is not a homogeneous polyhedral Gömböc.

## What was actually constructed

All 27 predecessor rows are retained unchanged as inactive-capable `old_*` controls. Eleven new shell/cap rows have denominator `2^20`:

```text
T27  (-28057373, 4186121, -498167)
TR   (-3600752, -1904082, -4267224)
S9   (27405813, -8804245, -101533)
SC0  (28051158, -8326488, 286080)
SS   (28592592, 15930463, 9857195)
SU   (-2882498, -2050973, 626625)
SC1  (-1348810, -6348988, -2228993)
SA5  (-5371631, -6777867, -6422512)
S102 (-30768700, 23219117, 8526199)
G    (104857600, 9155834, 4751981)
H    (104857600, -25407644, 2998021)
```

The exact body has 38 supplied rows. Active exactly: `T27,TR,SS,SU,SC1,SA5,S102,G,H`. Inactive exactly: all 27 `old_*` rows plus `S9,SC0`. The minimum exact raw inactive slack is `26408451247059648709/787740163592138119317 ≈ 0.03352431736708164`; the independently recomputed global nonincident active/inactive vertex slack is `0.018087434929835874`. A strictly positive exact combination of `T27,TR,SS,SU` equals zero, certifying boundedness; every active row has a maximal face, certifying irredundancy.

## Isolated dependent centring root

For raw rows `B_i`, the exact root is the ordinary-volume centroid `u` and the own-centred rows are `H_i=B_i/(1-B_i·u)`. Decimal locator:

```text
u = (-0.030905113612726035, -0.07929335273476126, 0.08189373690283598)
V = 0.0031474797626348874
```

All three exact rational components of `u`, the exact volume, every normalized row, and the exact first moments are in `centering` of `p9_xg2_exact.json`. The centered first moment is exactly `(0,0,0)`. The translated-moment Jacobian is `-V I_3`, with determinant `-V^3≠0`, so the root is isolated; pre-wall, post-wall, endpoint, and every perturbation-box member are recentered by these three dependent equations.

## Actual H/V/E lattice

`(V,E,F)=(14,21,9)`, Euler `14-21+9=2`. Active vertex triples:

- `v0` = `(T27,TR,SA5)`
- `v1` = `(T27,TR,S102)`
- `v2` = `(T27,SU,SC1)`
- `v3` = `(T27,SU,S102)`
- `v4` = `(T27,SC1,SA5)`
- `v5` = `(TR,SA5,G)`
- `v6` = `(TR,S102,G)`
- `v7` = `(SS,S102,G)`
- `v8` = `(SS,S102,H)`
- `v9` = `(SS,G,H)`
- `v10` = `(SU,SC1,H)`
- `v11` = `(SU,S102,H)`
- `v12` = `(SC1,SA5,H)`
- `v13` = `(SA5,G,H)`

Maximal face cycles:

- `T27`: `[4, 2, 3, 1, 0]`
- `TR`: `[6, 5, 0, 1]`
- `SS`: `[8, 9, 7]`
- `SU`: `[2, 10, 11, 3]`
- `SC1`: `[4, 12, 10, 2]`
- `SA5`: `[0, 5, 13, 12, 4]`
- `S102`: `[3, 11, 8, 7, 6, 1]`
- `G`: `[13, 5, 6, 7, 9]`
- `H`: `[12, 13, 9, 8, 11, 10]`

All true P-edges:

`(0, 1), (0, 4), (0, 5), (1, 3), (1, 6), (2, 3), (2, 4), (2, 10), (3, 11), (4, 12), (5, 6), (5, 13), (6, 7), (7, 8), (7, 9), (8, 9), (8, 11), (9, 13), (10, 11), (10, 12), (12, 13)`

## One actual simultaneous cross-gap incidence

The common wall point and direction are exact:

```text
H0 = (28/1, -3961098442984948906610871865414733/463872380307057912803530858954752, 228987596968734260935777965316805/1855489521228231651214123435819008)
W  = (-14251743068434700702498523228, -117626787336506710264841618472, 101179393702451356888308493506)
epsilon = 2^-86
H_- = H0 - epsilon W/2^20
H_+ = H0 + epsilon W/2^20
```

At `H0` both determinants vanish exactly:

1. `{H,SC0,SS,SU}` — the predecessor extra-source **carrier** circuit.
2. `{H,S9,SC1,SA5}` — the predecessor stable-sink **carrier** circuit.

Both oriented crossing derivatives are exact positive integers, `111850054270825055434693127605019692639253076` and `15583968500236810890290937843112946730318072`; therefore the same signed parameter crosses both walls. Before the event the actual active set is `T27,TR,S9,SC0,SS,SU,SC1,SA5,S102,G,H`, with `(V,E,F)=(18,27,11)` and class `(3,2,3)`. Its actual mechanics are stable `T27,SC1,H`; unstable `(TR,S102,G)` and `(SS,SU,S102)`; saddles `(SC1,T27)`, `(H,SC1)`, `(SS,S102)`. Immediately after, `S9` and `SC0` are both inactive and carrier facet `(SC0,SS,SU)` is gone, but the same equilibrium identities survive, with renumbered primal features; the active set is `T27,TR,SS,SU,SC1,SA5,S102,G,H`, and `(V,E,F)=(14,21,9)`, still `(3,2,3)`. Therefore the actual-equilibrium sink-death gate is exactly **FAIL**.

The removed dual facets are `(H,S9,SA5)`, `(H,S9,SC1)`, `(H,SC0,SS)`, `(H,SC0,SU)`, `(S9,SA5,SC1)`, `(SC0,SS,SU)`; added facets are `(H,SA5,SC1)` and `(H,SS,SU)`. Coning the two wall bases to the Q-origin gives positive-volume cells `(0,H0,SS,SU)` of exact volume `127784667439300259519021461693163574744715267575/680044101268987963210815048546115783267188736 ≈ 187.90644195111648` and `(0,H0,SC1,SA5)` of exact volume `637705228685783407180444256642588831133542621347/6120396911420891668897335436915042049404698624 ≈ 104.19344331995877`. Their intersection contains the same interior edge `[0,H0]`. This is a genuine cross-gap two-page volumetric complex, not two serial relays.

## Complete equilibrium audit

Face-foot decisions against all 38 supplied constraints:

| face | margin | closest row | result |
|---|---:|---|---|
| `T27` | 0.3164598267872699 | `old_o27` | stable |
| `TR` | -4.605458633937466 | `T27` | excluded |
| `SS` | -1.642067015982673 | `H` | excluded |
| `SU` | -6.501666134791222 | `T27` | excluded |
| `SC1` | -0.0800759164058253 | `SA5` | excluded |
| `SA5` | -0.7004795013565124 | `T27` | excluded |
| `S102` | -0.3734256773900992 | `T27` | excluded |
| `G` | -1.213223385217432 | `H` | excluded |
| `H` | 0.5526231479832704 | `S9` | stable |

All 14 vertex-cone decisions:

| v | active triple | cone components | minimum | result |
|---:|---|---|---:|---|
| 0 | `(T27,TR,SA5)` | `(-0.006881624888, 0.2935659435, -0.09750282585)` | -0.0975028258533 | excluded |
| 1 | `(T27,TR,S102)` | `(-0.03211876679, 0.1843799041, 0.04119833191)` | -0.0321187667946 | excluded |
| 2 | `(T27,SU,SC1)` | `(-0.01092540793, 0.1776501398, -0.04029439107)` | -0.0402943910698 | excluded |
| 3 | `(T27,SU,S102)` | `(-0.02951627965, 0.1957051414, 0.03182856807)` | -0.0295162796501 | excluded |
| 4 | `(T27,SC1,SA5)` | `(0.0009669410882, 0.01855971425, -0.008223777386)` | -0.00822377738565 | excluded |
| 5 | `(TR,SA5,G)` | `(0.270814962, -0.08147474638, 0.01762820919)` | -0.0814747463754 | excluded |
| 6 | `(TR,S102,G)` | `(0.1676372162, 0.02349845691, 0.05093746487)` | 0.0234984569053 | UNSTABLE |
| 7 | `(SS,S102,G)` | `(-0.07885554843, 0.02707608826, 0.07287274662)` | -0.078855548427 | excluded |
| 8 | `(SS,S102,H)` | `(-0.08908399569, 0.06813493543, 0.05365687839)` | -0.0890839956861 | excluded |
| 9 | `(SS,G,H)` | `(0.00291184468, 0.007423350578, -0.003215607111)` | -0.00321560711128 | excluded |
| 10 | `(SU,SC1,H)` | `(0.17984975, -0.0455511659, 0.01093696321)` | -0.0455511659031 | excluded |
| 11 | `(SU,S102,H)` | `(0.1852679531, 0.03984980627, 0.03230714367)` | 0.0323071436672 | UNSTABLE |
| 12 | `(SC1,SA5,H)` | `(0.01013878283, -0.0001627905968, 0.0003060725768)` | -0.000162790596813 | excluded |
| 13 | `(SA5,G,H)` | `(0.04111337809, 0.06450488365, -0.02244627227)` | -0.0224462722741 | excluded |

All 21 true-edge four-component decisions `(t,1-t,λ1,λ2)`:

| id | edge | faces | components | minimum | result |
|---:|---|---|---|---:|---|
| 0 | `(0, 1)` | `(T27,TR)` | `(-66.0192823, 67.0192823, -0.00259697952, 0.051625457)` | -66.019282342 | excluded |
| 1 | `(0, 4)` | `(SA5,T27)` | `(0.863753824, 0.136246176, 0.00708563614, -0.000321493116)` | -0.00032149311567 | excluded |
| 2 | `(0, 5)` | `(SA5,TR)` | `(-8.13410385, 9.13410385, -0.0679831318, 0.189013471)` | -8.134103849 | excluded |
| 3 | `(1, 3)` | `(S102,T27)` | `(0.497071444, 0.502928556, 0.00170903116, -0.000525399255)` | -0.00052539925537 | excluded |
| 4 | `(1, 6)` | `(S102,TR)` | `(-6.89850843, 7.89850843, 0.000206469446, 0.0369041726)` | -6.8985084349 | excluded |
| 5 | `(2, 3)` | `(SU,T27)` | `(-1.82289498, 2.82289498, 0.0801741961, -0.00494721158)` | -1.8228949777 | excluded |
| 6 | `(2, 4)` | `(SC1,T27)` | `(1.10971925, -0.10971925, 0.00990787645, 0.000258461581)` | -0.1097192504 | excluded |
| 7 | `(2, 10)` | `(SC1,SU)` | `(-9.17585739, 10.1758574, -0.00506293077, 0.0496746869)` | -9.1758573927 | excluded |
| 8 | `(3, 11)` | `(S102,SU)` | `(-5.62571905, 6.62571905, -0.00128375744, 0.0458359238)` | -5.6257190464 | excluded |
| 9 | `(4, 12)` | `(SA5,SC1)` | `(0.76014128, 0.23985872, -0.00221329198, 0.0123824765)` | -0.0022132919831 | excluded |
| 10 | `(5, 6)` | `(G,TR)` | `(-7.08301001, 8.08301001, 0.0136837002, 0.0771587117)` | -7.0830100077 | excluded |
| 11 | `(5, 13)` | `(G,SA5)` | `(2.40779677, -1.40779677, 0.00597362521, 0.0128961447)` | -1.4077967704 | excluded |
| 12 | `(6, 7)` | `(G,S102)` | `(1.27991357, -0.279913572, 0.00595788965, 0.00403536772)` | -0.27991357195 | excluded |
| 13 | `(7, 8)` | `(S102,SS)` | `(0.421036707, 0.578963293, 0.00186595702, 0.0061900679)` | 0.001865957023 | SADDLE |
| 14 | `(7, 9)` | `(G,SS)` | `(1.28767358, -0.287673577, -0.00367186161, 0.0100573839)` | -0.28767357741 | excluded |
| 15 | `(8, 9)` | `(H,SS)` | `(0.901109614, 0.0988903858, -0.00117331009, 0.00798096954)` | -0.0011733100865 | excluded |
| 16 | `(8, 11)` | `(H,S102)` | `(-0.416157606, 1.41615761, 0.00421403183, 0.00725392979)` | -0.41615760613 | excluded |
| 17 | `(9, 13)` | `(G,H)` | `(0.0335769556, 0.966423044, 0.0112313336, -0.00420366027)` | -0.0042036602728 | excluded |
| 18 | `(10, 11)` | `(H,SU)` | `(-1.50180379, 2.50180379, 0.00483103113, 0.0772031385)` | -1.501803794 | excluded |
| 19 | `(10, 12)` | `(H,SC1)` | `(1.00174265, -0.00174265367, 0.000320021234, 0.00996163517)` | -0.0017426536742 | excluded |
| 20 | `(12, 13)` | `(H,SA5)` | `(0.112230607, 0.887769393, 0.00101641992, 0.00808182237)` | 0.0010164199196 | SADDLE |

Exact class: **`(S,U,H)=(2,2,2)`**. Stable faces are `T27,H`; unstable vertices are `v6=(TR,S102,G)` and `v11=(SU,S102,H)`; saddle edges are `(7,8)` on `(SS,S102)` and `(12,13)` on `(SA5,H)`. The controlling positive saddle component is `0.0010164199195995655`; the directed interval audit keeps every other face/vertex/edge exclusion strictly negative.

## Exact witness-chain obstruction

The exact face-witness graph is:

```text
T27 -> []
TR -> ['SA5', 'T27']
SS -> ['G', 'H']
SU -> ['S102', 'SC1', 'T27']
SC1 -> ['SA5']
SA5 -> ['T27']
S102 -> ['T27']
G -> ['H']
H -> []
```

Its sinks are exactly `T27,H`. A strict face arrow `a→b` satisfies `H_a·H_b>||H_a||²`; Cauchy forces `||H_b||>||H_a||`. Hence every witness path strictly raises norm. Here `||H||²-||T27||²` is exact and positive, approximately `208.6071735358797`, so `H` cannot drain to protected `T27` while those centered rows remain fixed. `H` must be deactivated or the norm order must reverse.

The exact vertex-radius graph is:

```text
v0 -> [1, 5]
v1 -> [3, 6]
v2 -> [3, 10]
v3 -> [11]
v4 -> [0, 2]
v5 -> [6]
v6 -> []
v7 -> [6, 8]
v8 -> [11]
v9 -> [7, 8, 13]
v10 -> [11]
v11 -> []
v12 -> [4, 10, 13]
v13 -> [5]
```

Its sinks are exactly `v6,v11`. Every arrow follows a true P-edge toward strictly larger squared radius. The exact gap `r²(v11)-r²(v6)` is positive, approximately `0.015351765003439263`, so the extra source cannot drain to intended `v6` at fixed positions. The residual transferred block is therefore exactly: stable `H`; unstable `(SU,S102,H)`; saddles `(SA5,H)` and `(SS,S102)`.

## Open perturbation box and independent verification

A directed 180-decimal interval calculation permits all 114 raw support coefficients to vary independently by `2^-100`, then recomputes the ordinary centroid and projective normalization. It proves the same 38 supplied / 9 active / 29 inactive rows, the same `(14,21,9)` lattice, and the same strict `(2,2,2)` class. Certified lower bounds are: expected-vertex nonincident slack `0.018087434929835874`; nonvertex-triple violation `0.020684620828846676`; oriented tetra volume `2.8149258036083904e-06`; projective denominator `0.5285148868898722`; positive cone component `0.0010164199195995653`; negative-exclusion clearance `0.00016279059681313315`.

The clean-room verifier is standard-library `Fraction` code independent of the constructor. It enumerates all feasible triples, reconstructs every maximal face and true edge, integrates exact moments, recentres, audits every full cone, checks both exact circuits on `H_-` and `H_+`, and proves the two norm/radius obstructions. It passes. The mesh verifier passes: OBJ has 14 vertices, 9 polygon faces, 21 manifold edges; STL has 24 triangles. Main exact-data SHA-256: `ddfb44e17e2d2789f9e0dcb15d63b3abaaa2c07134aac5196de08ed2a100029f`.

## What changed relative to the journal, and what remains open

The journal only had the predecessor and the demand for a one-event cross-gap removal. This result supplies a literal synchronized cross-gap **carrier** event and then proves, by auditing both adjacent cells, that it misses the demanded actual-equilibrium gate. It is an exact NONWINNER. The obstruction has moved from predecessor `o9/(C0,XS,XU)` to the compact residual block `H/(SU,S102,H)` with two attached saddle channels. Numerical one-cap, two-cap, three-cap, radial, and common-metric searches were used to locate this event; their failures are not claimed as global exclusions. The exact wall, endpoint, interval box, and witness DAG theorems are independent of search exhaustiveness.

The smallest topology now forced open is a **three-page shared-interior-edge cross-gap book**, or one stronger nonsimplicial cell, synchronizing circuits `{K,H,SU,S102}`, `{K,H,SA5,SC1}`, and `{K,SS,S102,G}` on a common new row `K`, with all three cone cells sharing `[0,K]`. It needs one common event coordinate, at least two independent anti-birth/diagonal controls, and three dependent moment controls. It must deactivate `H`, destroy `(H,SU,S102)`, cross both saddle channels, and protect `T27` plus `(TR,S102,G)`. A macroscopic support-norm/radius reversal is the only comparable alternative.

## Reusable artifacts

- Complete exact bundle (`Steady_Willow_02_P9_XG2_exact_NONWINNER.zip`) — SHA-256 `24c4c2e870aa8e4ec7b20b08eb3cbb23fd4cb5f0a066e9682dee711a1e66efe6`.
- Full handoff (`STEADY_WILLOW_02_HANDOFF.md`)
- Exact certificate JSON (`p9_xg2_exact.json`)
- Exact source rows (`p9_xg2_source_rows.csv`) · vertices (`p9_xg2_vertices.csv`) · all edge cones (`p9_xg2_edges.csv`)
- Exact witness obstruction (`p9_xg2_witness_obstruction_exact.json`) · directed perturbation certificate (`p9_xg2_perturbation_interval.json`)
- Clean-room verifier (`verify_p9_xg2_cleanroom.py`) · interval verifier (`verify_p9_xg2_perturbation_interval.py`) · verification receipt (`VERIFICATION_RECEIPT.txt`)
- OBJ mesh (`p9_xg2.obj`) · STL mesh (`p9_xg2.stl`)
