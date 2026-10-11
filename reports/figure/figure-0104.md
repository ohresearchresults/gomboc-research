# figure-0104

Historical AI scientific report · saved 2026-08-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Nested two-cycle / sixteen-block Santaló continuation

## Verdict

No homogeneous convex polyhedral Gömböc was found. The acceptance gate remains a finite uniform-density body evaluated at its own exact volume centroid with strict `(S,U,H)=(1,1,0)`; a wall point, auxiliary-reference solution, or strict `(2,2,2)` body is not completion. :contentReference[oaicite:0]{index=0}

I continued the exact four-sheet/eight-block endpoint through the smallest cyclic closure not previously subsumed. The strongest result is a fully materialized, irredundant, exact, open `(2,2,2)` fallback with **two communicating cyclic closure stages and sixteen exact circuit blocks**. It is not a winner, but it removes the complete inherited critical block and sharply identifies the next genuinely three-dimensional replacement topology.

## What changed

The inherited endpoint had stable `D12,E0`, unstable incidences `(C3,D3,D12)` and `(E1,E2,E4)`, and saddles `A6-E0`, `C6-E7`. The continuation does the following:

1. A first exact nine-edge cyclic closure inserts `F0..F8` on true parent Q edges.
2. A second exact seven-edge closed return cycle inserts `G0..G6` around `E0-F0-D0-F4-F6-F8-F2-E0`.
3. Both families cross at exact scalar walls. The combined sixteen-block circuit-incidence graph is connected.
4. The inherited block is genuinely absent in the final lattice. It transfers to new endcaps rather than surviving under old labels.
5. A connected 22-facet two-hemisphere surface replacement was also tested; it again transferred the Euler-neutral system. This is the evidence that another surface ladder is subsumed and that the next event must share an actual three-dimensional cell.

## Strongest exact endpoint

- Exact record: `two_cycle_sixteen_block_exact.json`.
- Record SHA-256: `38115ce8e005f2d5fb53afde56391e42cbc41a46eadc042c1f6166b7e908a20c`.
- Q f-vector `(V,E,F)=(27,75,50)`.
- P f-vector `(V,E,F)=(50,75,27)`.
- Complexity `150`.
- All 27 Q rows are extreme; all 50 P vertices and all 75 true edges are actual and exact.
- Exact ordinary volume is the rational field `P.volume_exact` in the certificate; decimal value `4.1266935106019603e-5`.
- Exact own uniform-volume centroid and first moment: `(0,0,0)`.
- Raw-polar centroid before the projective gauge: approximately `(0.028593887061222192, 0.01594396206223217, 0.0001293008192539674)`; its literal exact fractions are stored in `pre_gauge_polar_centroid_exact`.
- Projective denominator interval: `[0.5251993220915171, 7.3375313222282204]`.
- P inactive separation: `1.3737982645022134e-5`, with exact comparison `>10^-5` true.
- Q inactive separation: `0.016761289383370178`, with exact comparison `>10^-5` true.

## Deterministic exact raw-Q generator

Parse each hexadecimal literal with `float.fromhex`, then convert the binary64 value to its exact dyadic rational with `Fraction.from_float`. Use support constant one for every row and let `Q_raw=conv(q_0,...,q_26)`.

```text
00   A7  (-0x1.d6a812e8ca739p+3, 0x1.3e2eb72ac7765p+5, 0x1.c40990f040dd2p-3)
01   A8  (-0x1.da825b0702fb2p+3, 0x1.3eeb56d666aecp+5, 0x1.38bf5f175a765p+3)
02   A9  (-0x1.ca8dc361008f5p+3, 0x1.2f21813d88193p+5, 0x1.3651c737f2e4cp+4)
03   B8  (-0x1.ace2d9d413430p+4, 0x1.8604ff7855ba8p+5, 0x1.2b43fa075d327p+5)
04   C3  (0x1.ace6474c2bad2p+4, -0x1.ebd57f1c252fep+4, -0x1.4c312712eda31p+5)
05   C4  (0x1.bc64c497f8adcp+4, -0x1.7cdeeda53909fp+5, -0x1.087f10aae2f9bp+5)
06   D3  (0x1.ad2341b988253p+3, 0x1.45baf7a4e0d02p+2, -0x1.4331aa7fe559cp+5)
07   D5  (-0x1.cae4d65190866p+3, -0x1.4feb82996d7f7p+6, -0x1.69a3b9ab289f6p+5)
08   D7  (-0x1.a0b6a535fdb4dp+6, -0x1.6eab32516d518p+6, 0x1.341af9ae0b66bp+8)
09   D8  (-0x1.4375f92b98747p+7, -0x1.5eac766af8ab1p+6, 0x1.ef7f51fbe2ca6p+8)
10  D10  (-0x1.4b31a04af74adp+7, 0x1.298480a5e129ap+3, 0x1.05e702901bd5ep+9)
11  D11  (-0x1.67b705dcca63dp+6, 0x1.24b8dc7e8e788p+5, 0x1.64c6009648530p+8)
12   E3  (-0x1.a1cc5655a0358p+1, -0x1.50034eafe43f3p-1, -0x1.66085ea77eb96p+6)
13   E4  (-0x1.7863a6dfce7e0p+7, -0x1.d18b0e57819b9p+5, 0x1.014d1f0cee291p+9)
14   E5  (-0x1.89d788084f887p+7, -0x1.891c92ccc6923p+5, 0x1.287e92b90c298p+9)
15   E6  (-0x1.3cf8f4861b0afp+6, -0x1.1adc94afdeb7cp+4, 0x1.44bb6b77d0187p+8)
16   F0  (-0x1.b6121c196aa9bp+3, 0x1.28b07c6f649dap+5, -0x1.54cffead0ad38p+3)
17   F1  (0x1.87be76305db3dp+2, 0x1.da3d653dbb2d9p+3, -0x1.096f30f3e6efdp+5)
18   F3  (0x1.bb72a52ea2fcbp+4, -0x1.5af16ca6bbe77p+5, -0x1.19d7794e1d5c2p+5)
19   F5  (0x1.949754a131157p+4, -0x1.0a8730de83473p+6, -0x1.1c98752f58faep+4)
20   G0  (0x1.f5341763dac6ap-5, 0x1.c665c73d6d11bp+1, -0x1.713e447698db0p+6)
21   G1  (-0x1.3cfdd6c28887ap+1, 0x1.f6c11e9b1ea75p+1, -0x1.617cb4c892544p+6)
22   G2  (0x1.852793f974888p+4, -0x1.bfc1933a8c327p+5, -0x1.e3d124d73e403p+4)
23   G3  (0x1.440e7ed64e774p+4, -0x1.b31c9d37cbe4ep+5, 0x1.907b5835a279cp+3)
24   G4  (-0x1.f5693d18961e4p-2, -0x1.add61f5b43691p+4, 0x1.d237f35d692a0p+6)
25   G5  (-0x1.830f23c0ce066p+3, 0x1.f1857e6a40c67p+3, 0x1.0438df95505bap+7)
26   G6  (0x1.c6acc10af47a8p+3, 0x1.329781865b062p+2, -0x1.e628aa7f6fc8ap+5)
```

The exact certificate additionally stores all 81 coordinates directly as numerator/denominator strings, so reconstruction need not depend on a binary64 parser.

## Exact reconstruction, centering, boundedness, and polarity

Enumerate every nonsingular row triple and solve

```text
q_i·p=q_j·p=q_k·p=1
```

over `Fraction`. Retain precisely the solutions satisfying all 27 inequalities. Their exact active-row sets reconstruct `P0=Q_raw^circ`, all maximal faces, every true edge, and the full dual lattice. Triangulate the outward maximal-face cycles and compute the ordinary volume and centroid `c` exactly. Set

```text
T_u(q)=q/(1-q·u)
u=c
Q=T_c(Q_raw)
P=P0-c
```

Then, identically,

```text
(T_u Q_raw)^polar=P0-u
F(u)=centroid((T_u Q_raw)^polar)=c-u
DF=-I3
```

Therefore `u=c` is the unique exact centering solution. In centered coordinates the residual root is exactly zero and isolated in `[-2^-80,2^-80]^3`.

Rows `[0,1,3,19]=[A7,A8,B8,F5]` positively contain the origin, with approximate positive weights `(0.0007122407964128217, 0.47319275220709883, 0.02144669953397601, 0.5046483074625123)`. This proves strict origin interiority. On the complete root box, maximum P support displacement is `8.483679689396837e-26` and maximum Q control dot is `1.3588901217731582e-22`; hence every projective denominator stays positive and polarity remains bounded throughout the isolating box.

## Sixteen exact communicating circuit blocks

For each stage, an inserted row has the exact family `x_k(t)=m_k+t(e_k-m_k)`, where the wall point `m_k=(1-w_k)a_k+w_k b_k` lies in the relative interior of a certified true parent Q edge.

### Stage 1 — first nine-block cycle

| block | inserted row | certified parent true edge | exact wall weight |
|---:|---|---|---|
| 0 | `F0` | `A6-E0` | `6009150099930367/288230376151711744` |
| 1 | `F1` | `A6-D3` | `6396023106223711/9007199254740992` |
| 2 | `F2` | `D3-C3` | `1627020309477585/18014398509481984` |
| 3 | `F3` | `C3-C4` | `6738557965637843/9007199254740992` |
| 4 | `F4` | `C4-C5` | `123569762293067/140737488355328` |
| 5 | `F5` | `C5-C6` | `6036204291740999/36028797018963968` |
| 6 | `F6` | `C6-E7` | `1700244773841539/2251799813685248` |
| 7 | `F7` | `C3-D12` | `1259684826556841/2251799813685248` |
| 8 | `F8` | `D12-E7` | `20061573384961/140737488355328` |

At `t=-1/1024`, none of the nine F rows is extreme. At `t=1/1024`, all nine are extreme. The accepted `t=1` branch has Q/P `(29,81,54)/(54,81,29)` and deactivates `A6,C5,C6,D12,E1,E2,E7`.

### Stage 2 — second seven-block closed cycle

| block | inserted row | certified parent true edge | exact wall weight |
|---:|---|---|---|
| 0 | `G0` | `E0-F0` | `4648762373628229/288230376151711744` |
| 1 | `G1` | `F0-D0` | `8115488052385275/9007199254740992` |
| 2 | `G2` | `D0-F4` | `8063444375671799/9007199254740992` |
| 3 | `G3` | `F4-F6` | `4931459429263551/18014398509481984` |
| 4 | `G4` | `F6-F8` | `1020431896097305/9007199254740992` |
| 5 | `G5` | `F8-F2` | `1344405703688743/4503599627370496` |
| 6 | `G6` | `F2-E0` | `742978715327595/2251799813685248` |

At `t=-1/1024`, none of the seven G rows is extreme. At `t=1/1024`, all seven are extreme. The accepted `t=1` branch is the final Q/P `(27,75,50)/(50,75,27)` endpoint and deactivates `D0,D2,D4,E0,F2,F4,F6,F7,F8` from its parent.

Final inherited/source rows still active are `A7,A8,A9,B8,C3,C4,D3,D5,D7,D8,D10,D11,E3,E4,E5,E6`. The exact event verifier proves every wall equation, every true-parent-edge assertion, every strict-side incidence, both deactivation maps, and connectedness of the combined block graph.

## Complete exact incidence

### P maximal faces: defining Q row → cyclic P vertices

```text
00   A7: 0 1 4 3 2
01   A8: 0 5 6 1
02   A9: 5 7 9 8 6
03   B8: 0 2 14 13 11 10 12 7 5
04   C3: 15 20 18 17 19 16
05   C4: 21 23 24 27 26 25 22
06   D3: 8 9 15 16 28
07   D5: 21 22 34 30 29 31 32 33
08   D7: 29 30 35
09   D8: 29 35 39 38 37 36 31
10  D10: 10 11 41 40
11  D11: 10 40 42 43 44 12
12   E3: 32 45 46 33
13   E4: 11 13 45 32 31 36 41
14   E5: 36 37 42 40 41
15   E6: 37 38 43 42
16   F0: 2 3 48 47 14
17   F1: 1 6 8 28 4
18   F3: 17 18 24 23
19   F5: 25 26 49 39 35 30 34
20   G0: 17 23 21 33 46 47 48 19
21   G1: 13 14 47 46 45
22   G2: 22 25 34
23   G3: 26 27 49
24   G4: 18 20 44 43 38 39 49 27 24
25   G5: 7 12 44 20 15 9
26   G6: 3 4 28 16 19 48
```

### Q maximal faces: dual P vertex → cyclic Q rows

```text
00: 0 3 1   [A7,A8,B8]
01: 0 1 17   [A7,A8,F1]
02: 0 16 3   [A7,B8,F0]
03: 0 26 16   [A7,F0,G6]
04: 0 17 26   [A7,F1,G6]
05: 1 3 2   [A8,A9,B8]
06: 1 2 17   [A8,A9,F1]
07: 2 3 25   [A9,B8,G5]
08: 2 6 17   [A9,D3,F1]
09: 2 25 6   [A9,D3,G5]
10: 3 10 11   [B8,D10,D11]
11: 3 13 10   [B8,D10,E4]
12: 3 11 25   [B8,D11,G5]
13: 3 21 13   [B8,E4,G1]
14: 3 16 21   [B8,F0,G1]
15: 4 6 25   [C3,D3,G5]
16: 4 26 6   [C3,D3,G6]
17: 4 18 20   [C3,F3,G0]
18: 4 24 18   [C3,F3,G4]
19: 4 20 26   [C3,G0,G6]
20: 4 25 24   [C3,G4,G5]
21: 5 7 20   [C4,D5,G0]
22: 5 22 7   [C4,D5,G2]
23: 5 20 18   [C4,F3,G0]
24: 5 18 24   [C4,F3,G4]
25: 5 19 22   [C4,F5,G2]
26: 5 23 19   [C4,F5,G3]
27: 5 24 23   [C4,G3,G4]
28: 6 26 17   [D3,F1,G6]
29: 7 8 9   [D5,D7,D8]
30: 7 19 8   [D5,D7,F5]
31: 7 9 13   [D5,D8,E4]
32: 7 13 12   [D5,E3,E4]
33: 7 12 20   [D5,E3,G0]
34: 7 22 19   [D5,F5,G2]
35: 8 19 9   [D7,D8,F5]
36: 9 14 13   [D8,E4,E5]
37: 9 15 14   [D8,E5,E6]
38: 9 24 15   [D8,E6,G4]
39: 9 19 24   [D8,F5,G4]
40: 10 14 11   [D10,D11,E5]
41: 10 13 14   [D10,E4,E5]
42: 11 14 15   [D11,E5,E6]
43: 11 15 24   [D11,E6,G4]
44: 11 24 25   [D11,G4,G5]
45: 12 13 21   [E3,E4,G1]
46: 12 21 20   [E3,G0,G1]
47: 16 20 21   [F0,G0,G1]
48: 16 26 20   [F0,G0,G6]
49: 19 23 24   [F5,G3,G4]
```

### Every true P edge

```text
0-1  0-2  0-5  1-4  1-6  2-3  2-14  3-4  3-48  4-28
5-6  5-7  6-8  7-9  7-12  8-9  8-28  9-15  10-11  10-12
10-40  11-13  11-41  12-44  13-14  13-45  14-47  15-16  15-20  16-19
16-28  17-18  17-19  17-23  18-20  18-24  19-48  20-44  21-22  21-23
21-33  22-25  22-34  23-24  24-27  25-26  25-34  26-27  26-49  27-49
29-30  29-31  29-35  30-34  30-35  31-32  31-36  32-33  32-45  33-46
35-39  36-37  36-41  37-38  37-42  38-39  38-43  39-49  40-41  40-42
42-43  43-44  45-46  46-47  47-48
```

### Every true Q edge

```text
0-1  0-3  0-16  0-17  0-26  1-2  1-3  1-17  2-3  2-6
2-17  2-25  3-10  3-11  3-13  3-16  3-21  3-25  4-6  4-18
4-20  4-24  4-25  4-26  5-7  5-18  5-19  5-20  5-22  5-23
5-24  6-17  6-25  6-26  7-8  7-9  7-12  7-13  7-19  7-20
7-22  8-9  8-19  9-13  9-14  9-15  9-19  9-24  10-11  10-13
10-14  11-14  11-15  11-24  11-25  12-13  12-20  12-21  13-14  13-21
14-15  15-24  16-20  16-21  16-26  17-26  18-20  18-24  19-22  19-23
19-24  20-21  20-26  23-24  24-25
```

## Exhaustive own-centroid full-normal-cone audit

The exact independent audit tests all 27 maximal P faces, all 50 P vertices with their complete three-generator normal cones, and all 75 true P edges with both segment conditions and the complete two-generator normal cone. The final equilibrium block is:

| type | feature | positive margin |
|---|---|---:|
| stable face | `D11` | `0.0023008998925923632` |
| stable face | `G6` | `0.009385920909069926` |
| unstable vertex | `(B8,E4,G1)` | `0.0034066227740471118` |
| unstable vertex | `(C3,D3,G5)` | `0.037168954266409031` |
| saddle edge | `F0-G6` | `0.0038053663250213871` |
| saddle edge | `G3-G4` | `0.0036703054678251692` |

Closest excluded face: `A7`, margin `-0.0010428248764370264`.
Closest excluded vertex: `(D5,E3,E4)`, margin `-0.0011868766884522699`.
Closest excluded edge: `E3-E4`, margin `-0.0011868766884522699`.

Thus the class is an open strict `(2,2,2)` chamber, not tolerance dust.

## Directed perturbation certificate

For every rational `s∈[-2^-20,2^-20]`, set

```text
P_s=diag(1+s,1,1)P
Q_s=diag((1+s)^-1,1,1)Q
```

Directed 70-digit interval arithmetic fixes the signs of all 1,302 face, vertex-neighbor, full vertex-cone, edge-segment, and full two-normal-cone primitives. The condition number is at most `1048577/1048575`; the class remains `(2,2,2)`. Conservative inactive lower bounds are `1.3737969543460926e-5` for P and `0.016761273398574226` for Q.

## Search scope and attempted falsification

New continuation campaigns evaluated `43,943` valid strict bodies:

- 8,000 perturbations of the residual stars of the exact eight-block endpoint;
- 2,000 first cyclic-closure samples;
- 6,000 second closed-cycle samples;
- all 2,048 selected deletion subsets;
- 4,000 determinant-one metric states;
- 6,000 twelve-facet nonannular two-loop replacements;
- 9,999 direct residual-coordinate perturbations after both cycles;
- 3,896 generic random-Q controls;
- 2,000 connected two-hemisphere 22-facet replacements.

Together with the predecessor exact eight-block campaign, the finite evaluated total is at least `126,709` strict bodies. No `(1,1,0)` body occurred. This is finite-family evidence, not a theorem excluding all possible fifth-sheet or nonannular constructions.

A separate 12,000-point reference search found an auxiliary-reference `(1,2,1)` chamber at `r=(-0.002097406174379195,0.012706970671186047,-0.007266890015883778)`. It has stable `G6`, unstable `(D5,E3,E4)` and `(C3,D3,G5)`, and saddle `G3-G4`. Since that reference is not the body’s uniform centroid, it is diagnostic only. A 24-branch affine LP screen over all choices for breaking the extra unstable and the lone saddle had best normalized slack `-0.08850601839208377`, so the fixed geometry does not contain a first-order target branch.

## Precise obstruction and smallest topology not subsumed

The inherited critical labels are genuinely gone, and the new events are true cycles rather than serial rails. Nevertheless both cancellation channels still meet only along a surface seam. Every tested edge ladder, closed edge cycle, deletion, metric deformation, unrestricted local move, twelve-facet two-loop patch, and connected two-hemisphere surface patch transfers an Euler-neutral pair to a new endcap.

The smallest continuation not subsumed is therefore a **fifth communicating sheet or two-hemisphere nonannular three-cell replacement in which two cross-lobe circuits share an actual three-dimensional cell**. It must replace together

```text
D11,G6,B8,E4,G1,C3,D3,G5,F0,G3,G4
```

and may deactivate the adjacent one-ring

```text
A7,A8,A9,C4,D5,D8,D10,E3,E5,E6,F1,F3,F5,G0.
```

It should retain the exact projective elimination `u=c`, `DF=-I3`, include a fourth noncritical actuator, and require both inactive gates above `10^-5` before exactification. Another edge ladder or surface-only bridge is already subsumed by the observed transfer mechanism.

## Independent verification and reproducibility

The standalone verifier uses only Python’s standard-library `Fraction`, imports neither the materializer nor stored topology, and reconstructs the polar and both complete lattices from the raw rows. It independently returns:

- Q/P f-vectors `(27,75,50)/(50,75,27)`;
- exact centroid and first moment zero;
- class `(2,2,2)`;
- all 27 face, 50 vertex-full-cone, and 75 true-edge-full-cone audits;
- both inactive gates;
- positive tetrahedron and root-box boundedness.

A fresh extraction of the final ZIP passed its 56-entry manifest, every SHA-256 entry, the independent endpoint verifier, exact sixteen-block history verifier, directed perturbation verifier, deterministic mesh rebuild, and cross-file/mesh integrity check. The mesh audit gives Q: 27 vertices, 75 true edges, 50 maximal faces, 50 STL triangles; P: 50 vertices, 75 true edges, 27 maximal faces, 96 STL triangles.

Final ZIP SHA-256:

```text
eb6984c20d9e61e7d4f7d516b47c328528d4b8973f297513cf664ceeb9011004
```

## Reproducible artifacts

- [Complete self-contained handoff](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/SELF_CONTAINED_HANDOFF.md)
- [Portable exact bundle ZIP](sandbox:/mnt/data/two_cycle_sixteen_block_exact_bundle.zip)
- [ZIP SHA-256 record](sandbox:/mnt/data/two_cycle_sixteen_block_exact_bundle.zip.sha256)
- [Fresh-extraction verification transcript](sandbox:/mnt/data/two_cycle_sixteen_block_FRESH_VERIFY.txt)
- [Exact Q/P certificate](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/two_cycle_sixteen_block_exact.json)
- [Exact deterministic generator and both wall families](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/generator_spec.json)
- [Exact sixteen-block event certificate](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/sixteen_block_event_certificate.json)
- [Compact exhaustive full-normal-cone audit](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/full_normal_cone_audit.json)
- [Directed perturbation certificate](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/metric_perturbation_certificate.json)
- [Finite search and obstruction summary](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/search_obstruction_summary.json)
- [Independent exact verifier](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/verify_two_cycle_independent.py)
- [Exact circuit-history verifier](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/verify_sixteen_block_history.py)
- [Directed perturbation verifier](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/verify_metric_perturbation_iv.py)
- [Deterministic mesh rebuilder](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/rebuild_from_certificate.py)
- [P OBJ](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/two_cycle_sixteen_block_P.obj) and [P STL](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/two_cycle_sixteen_block_P.stl)
- [Q OBJ](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/two_cycle_sixteen_block_Q.obj) and [Q STL](sandbox:/mnt/data/two_cycle_sixteen_block_bundle/two_cycle_sixteen_block_Q.stl)
