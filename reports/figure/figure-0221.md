# figure-0221

AI research report · 2026-09-02 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Bright Nova 91 — exact terminal-volume continuation

## Literal determination

**EXACT NONWINNER.** I independently reconstructed the accepted 3,492-row second-cross-cap endpoint from `figure-0205`, then materialized and reverified its first genuinely nonserial one-boundary terminal-volume continuation. The resulting uniform-density convex polyhedron is exact and open at its own ordinary-volume centroid, but its exhaustive class is

```text
(S,U,H)=(2,2,2),
```

not `(1,1,0)`. The requested acceptance gate remains the exact finite homogeneous object with one stable face, one unstable vertex, no saddle edge, full incidence/mechanics certification, and a matching mesh. :contentReference[oaicite:0]{index=0} The journal’s accepted parent data and prescribed double-octahedral/prismatic successor are reproduced independently here. :contentReference[oaicite:1]{index=1} The preceding continuation supplied no immutable mathematical result because its envelope was invalid; I treated any recoverable terminal bytes only as an untrusted coordinate proposal and reran every decisive calculation from the accepted parent source. :contentReference[oaicite:2]{index=2}

## Exact accepted parent

Normative source: `source/parent_supplied_rows.hex`, SHA-256

```text
dd1ee566ad43391c8e70cf102a9cda45a46549ba07b9192c6ed0d723aeda131e
```

Interpreting every hexadecimal binary64 coordinate as its exact dyadic rational gives:

```text
supplied / active H rows = 3492 / 1630
primal (V,E,F)           = (3256,4884,1630)
strict class             = (2,2,2)
S                        = {3911,500008}
U                        = {(1836,500009,500010),(2024,2377,500004)}
H                        = {(1802,500005),(2592,500002)}.
```

The exact parent volume is `5.309756377272709531519308992181835355568156230330...`; its exact centroid is approximately

```text
(-0.0647629209856971735936853282463151,
  0.0324510688642930333551318016581467,
  0.0619239720407252745217850123527583).
```

Complete reduced rational volume, moments, and centroid are in `certificates/parent_exact_mass_centroid.json`. A separate 768-bit outward MPFR full-cone audit exactly reproduces every parent equilibrium label.

## Deterministic terminal generator

Starting from the parent, multiply labels

```text
500000,500001,500002,500003,500005,
500006,500007,500008,500009,500010
```

by exactly `1/4`, then append

```text
500011=(-0x1.c84dd5be7e5ccp+0,
         0x1.0438465312602p-1,
         0x1.fd3e15d4c6ca8p-6)

500015=(-0x1.fb97d4bbd6af2p+0,
         0x1.dc081ad8b3cb5p-2,
         0x1.11177ba1fe380p-7).
```

This regenerates `data/supplied_endpoint_rows.hex` exactly, SHA-256

```text
57542467905453bae2a40c33b38a3172a7dc6668ce0b3ec5436e89900c23ec75.
```

## Complete terminal H/V/E object and centering

The exact all-row reconstruction gives:

```text
supplied / active H rows                 3494 / 1624
strictly inactive supplied rows          1870
primal vertices                          3244
true edges                               4866
maximal polygon faces                    1624
oriented mass/STL triangles              6484
Euler V-E+F                              2
exact nonincident determinant checks     11324804
extra coplanar or outside supplied rows  0.
```

The complete raw exact H data, exact Cramer V data, all maximal-face cycles, all true edges, and the active/supplied map are expanded in `data/` and `geometry/`. Triangulation diagonals are explicitly excluded from the true-edge list.

The GMP rational mass engine obtains

```text
V  = 5.335581012298913784930232171921676003186207871972530824909263...
Mx = -0.355799320069729479008522273075091836012506069162027122554169...
My =  0.175800580683603078131938579296438583672651810264030998721936...
Mz =  0.355520537711597844693019650597506667998050328891875019840617...

c = (-0.0666842691076352139425172831578552,
      0.0329487229747556217292679498341422,
      0.0666320194355771906262992151461360).
```

`certificates/terminal_exact_mass_centroid.json` contains the complete reduced fractions and proves exactly `M_x-Vc_x=M_y-Vc_y=M_z-Vc_z=0`. The own-centred body is `P=P_raw-c`; equivalently its exact normalized active supports are `b_i=q_i/(1-q_i·c)`. The raw exact H/V files plus exact `c` reconstruct every own-centred coordinate without floating recentering.

## Exhaustive true-centroid mechanics

The exact strict terminal equilibria are

```text
stable maximal faces:
  3911
  500015

unstable vertices:
  (1836,2775,500011)
  (2024,2377,500004)

saddle true edges:
  (1802,500004)
  (2592,500015).
```

Thus the intended pair `S3911` / `U(2024,2377,500004)` survives, while the complete replacement packet is

```text
S500015,
U(1836,2775,500011),
H(1802,500004),
H(2592,500015).
```

A directed interval audit independently perturbs every coordinate of every active H row by `±2^-100`. It audits 1,624 faces, 3,244 complete vertex cones, and all four cone components on 4,866 true edges, with zero ambiguous features. The minimum positive and closest excluded margins are respectively:

```text
stable    +0.00079616431126718379559... / -0.00038862240539911099334...
unstable  +0.12994530997184396715194... / -0.03532773978448679952617...
saddle    +0.13006977285670492198354... / -0.01160065886494318644573....
```

The exact all-supplied topology theorem preserves the full H/V/E lattice throughout that box. Exact inactive-row separation is greater than `4.6086039101879198905893571962756910424e-4`; exact minimum nonincident primal slack is greater than `1.4689227575116868179486308837739759907e-9`.

## One-boundary transition and genuine finite thickness

The exact parent/final Q-facet symmetric difference is one connected disk exchange with one common boundary component:

```text
removed parent disk  (V,E,F)=(21,47,27), chi=1
added terminal disk  (V,E,F)=(15,29,15), chi=1.
```

Their common 13-edge boundary is

```text
1738-1807-1838-1802-1801-1836-2811-2775-2774-2592-2485-2449-500004-1738.
```

The removed disk contains the full required forcing wedge `{1836,2811,500009,500010}` and deletes every inherited unwanted carrier: `S500008`, `U(1836,500009,500010)`, `H(1802,500005)`, `H(2592,500002)`, and true edge `(1836,500009)`.

The terminal active support configuration contains two exact empty combinatorial octahedra:

```text
A={1738,1802,2592,2775,500004,500011}
B={1801,1802,1836,2775,500011,500015},
```

sharing the full triangular face `(1802,2775,500011)`. Their exact positive volumes are

```text
V_A = 8536230835377668325337479267857879957867464933253 /
      11692013098647223345629478661730264157247460343808

V_B = 1379796561615450563680979988815141144032973361101 /
      17538019647970835018444217992595396235871190515712.
```

Their nonshared vertices lie in strict opposite open halfspaces; interiors are disjoint. The union is a connected finite-thickness three-ball with boundary `(V,E,F)=(9,21,14)`, boundary Euler characteristic 2, and exact volume

```text
28368285629363906103374397781203922161668341521961 /
35076039295941670036888435985190792471742381031424
=0.8087653623037804843130794969694191560276....
```

Every other active support has an exact strict outside witness, and a lower regular lift exposes both octahedra as adjacent strict cells.

## Incidence-order verdict

The connected operation deletes the entire inherited packet, but it does **not** achieve the required ordering in which all stable, unstable, and saddle deaths occur before any replacement birth. Along the natural actual-hull chord—old terminal rows scaled by `1-3t/4`, new rows by `t`—fourteen stored open hull signatures all remain `(2,2,2)`, and the first stored post-parent state at `t=1/100` has already transferred both an extra stable and an extra unstable carrier. This chord is discovery evidence only; no claim is made that every path has the same order.

## Exact terminal forcing theorem

The replacement unstable carrier is the triangle

```text
T=(1836,2775,500011),
```

whose three Q edges `(1836,2775)`, `(1836,500011)`, and `(2775,500011)` are all true. At the exact ordinary centroid, every nonmutual endpoint support on each edge is strictly positive and the two mutual supports satisfy exactly

```text
sigma(A->B)+sigma(B->A)=||A-B||^2>0.
```

If the common owner `T` is unstable, the component already supplies the unwanted maximum. If it is not, the three distinct opposite endpoints are forced unstable. The protected vertex `U(2024,2377,500004)` is disjoint and independently strict. Therefore `U>=2` throughout every terminal fixed-incidence chamber retaining these external-positive signs.

## Exhaustion scope and continuation

Rigorously exhausted:

1. the exact accepted 3,492-row parent cell;
2. the exact 3,494-row terminal endpoint and its `2^-100` open coordinate box;
3. this exact one-boundary disk exchange;
4. this exact two-octahedron regular-subdivision terminal volume;
5. the whole terminal forcing-triangle fixed-incidence/external-positive chamber, where `U>=2`.

Not exhausted: all other double-octahedral/prismatic coordinates, all paths between the endpoint cells, or the global polyhedral Gömböc problem.

The first minimal topology still capable of simultaneous cancellation **within this architecture** is a one-boundary-component triple-spine prismatic/cubical finite-thickness three-ball, or a smaller strictly stronger higher-valence equivalent. It must independently destroy all three channels of `T`, kill `S500015` and both saddle carriers before any replacement birth, preserve `S3911` and `U(2024,2377,500004)`, and retain the three ordinary moments as hard dependent equations. At least three connected new extreme supports, or equivalent coordinated old-row motion, are indicated. This is not claimed globally topologically minimal.

## Reproducible artifact

The archive contains the exact sources, expanded H/V/E data, all face cycles and true edges, exact mass and interval mechanics ledgers, transition and 3-ball certificates, independent C++/Python verifiers, integrity manifest, and watertight OBJ/STL. `./verify_all.sh` ends with

```text
ALL_BRIGHT_NOVA91_SECOND_CROSSCAP_TERMINAL_VOLUME_VERIFIERS_PASS.
```

Archive SHA-256:

```text
80c395e780dd971e650c1ff7f79bc9b210c08588b3227434bbcdbf3d23fe878c
```

Manifest SHA-256:

```text
93bc7f2b096329844bfb4fa327a9737cb52a87648d0351497941d086f88b4c18
```

[Download the complete exact archive](sandbox:/mnt/data/Bright_Nova_91_second_crosscap_terminal_volume_exact_NONWINNER.zip)

The terminal branch is therefore a rigorous exact adjacent endpoint and topology/obstruction result, but it does not supersede the run-wide M42 `(61,163,104)`, strict `(2,1,1)` benchmark as the closest known object to the target.
