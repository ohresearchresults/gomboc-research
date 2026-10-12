# figure-0146

AI research report · 2026-08-29 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Literal verdict

**NONWINNER.** I did not obtain a finite uniform-density convex polyhedron with strict own-centroid `(S,U,H)=(1,1,0)`. I did obtain and fully materialize an exact dyadic 13-vertex Conway-compression endpoint with strict class `(3,2,3)`, then exhaust an exact, genuinely connected lower-plus-two-upper topology-changing family on its declared parameter domain. That family has zero winner cells.

This is a fresh reconstruction, not a transport recovery. The durable journal explicitly excludes `figure-0142` because its immutable body contained only worker-local links and omitted the literal verdict, coordinates, counts, residual packet, and obstruction. No hidden coordinate or verdict from that copy is used here. Because the journal contains no 13-vertex coordinate matrix, I cannot claim byte-for-byte identity with the inaccessible prior endpoint; “reconstructed” below means an independently exactified body in the same recorded `(13,31,20)`, bottom-pentagon/apex, two-upper-plus-one-lower residual architecture.

The journal’s acceptance gate requires raw incidence, maximal faces, true edges, full normal cones, exact or directed ordinary-volume centering, open perturbation margin, independent verification, and mesh data. This handoff supplies those items inline and in a portable bundle.

## 1. What I actually tried and what changed

1. I independently rebuilt the original 21-vertex Conway `n=4,k=5` generator, including the secant correction to ring radii and the apex lift. The journal records the same formulas and warns that omitting either correction produces the false geometry.
2. I searched compressed tall-cap 13-vertex bodies with a fixed lower pentagon and upper apex, rebuilding the convex hull and own ordinary-volume centroid at every evaluation. A robust `(3,2,3)` chamber was found and rounded to a common dyadic denominator, then re-proved exactly.
3. A first connected dual-tree cap construction was rejected: before its inserted vertices acquired cross-edges it was only a set of serial caps; after cross-edges appeared it created extra stable/saddle pairs. I therefore changed the architecture from added caps to a connected deformation of the existing active vertex-star strip.
4. Three tangent modes were built around the upper-A, upper-B, and lower defect packets. A `21^3=9,261` grid over the three-mode box produced 4,344 valid 13-vertex hulls and no winner; 91 samples retained `(3,2,3)`. This grid is discovery evidence only, not a continuous exclusion.
5. I selected a cross-sensitive joint rational direction whose first derivative decreases all six residual margins, exactified it to an integer affine family, enumerated every circuit in the declared domain, isolated every equilibrium-component root, and exactly verified every resulting open cell. This is the closed subfamily proved below.

## 2. Independent reconstruction of the original Conway seed

For `k=5` and `alpha=(66.173,44.519,29.875,19.716)°`, define

`r_i=prod_{j<=i} cos(alpha_j)`, `theta_i=sum_{j<=i} alpha_j`, `x_i=r_i sin(theta_i)`, `z_i=r_i cos(theta_i)`, `rho_i=x_i/cos(pi/5)`,

then place five aligned vertices `(rho_i cos(2*pi*j/5),rho_i sin(2*pi*j/5),z_i)` on each of four rings and the apex at `(0,0,1+h)`, `h=sin^2(alpha_1)tan^2(pi/5)`. This matches the durable construction.

My independent reconstruction gives:

- arithmetic vertex centroid `(-8.09537622e-18, 1.18952467e-17, -0.015354018003813662)`;
- actual hull `(V,E,F)=(21,40,21)`;
- at that arithmetic center, class `(1,1,0)`: bottom pentagon stable, apex unstable, no saddle;
- ordinary volume `0.3275130116095386`;
- ordinary-volume centroid `(-6.93e-18,-5.28e-19,0.3175674749086905)`, or `+0.3329214929` in `z` relative to the arithmetic center;
- at its own ordinary-volume centroid, class `(6,21,25)`.

Thus the Conway flow skeleton is real but is not a homogeneous body at its ordinary-volume centroid, exactly the mismatch recorded in the journal. The deterministic reconstruction and full machine audit are in the bundle.

## 3. Exact 13-vertex endpoint `C13`

### 3.1 V-representation and exact centering

Let `D=2^24=16777216` and `p_i=Q_i/D`, with integer numerators:

| i | Qx | Qy | Qz |
|---:|---:|---:|---:|
| 0 | 16777216 | 0 | -16777216 |
| 1 | 5184445 | 15956081 | -16777216 |
| 2 | -13573053 | 9861400 | -16777216 |
| 3 | -13573053 | -9861400 | -16777216 |
| 4 | 5184445 | -15956081 | -16777216 |
| 5 | 42051094 | 28817600 | 417778 |
| 6 | 24543408 | 26610733 | -11452254 |
| 7 | 47848796 | 58066323 | 44119118 |
| 8 | -24046926 | 6156753 | -11843524 |
| 9 | -15959723 | -23586121 | 23797487 |
| 10 | -18390945 | -24540266 | -15149485 |
| 11 | 16396154 | -5769132 | -6616835 |
| 12 | -575692 | 1799886 | 446447126 |

The actual body claimed here is the exact translated body

`x_i = Q_i/D - C`,

where the exact ordinary-volume centroid is

`C = (8927530278674435758346646647585/19580682792453552593699143155712, 46941148293800050264959085443927/78322731169814210374796572622848, 495967542504696380404904555281339/78322731169814210374796572622848)`

`  ~= (0.45593559598009165, 0.5993298189771412, 6.332357606751124)`.

The uncentered ordinary volume and all three first moments are

- `V = 2334199284607595514500039/28334198897217871282176 ~= 82.380987480002133`;
- `Mx = 8927530278674435758346646647585/237684487542793012780631851008 ~= 37.560424624123236`;
- `My = 15647049431266683421653028481309/316912650057057350374175801344 ~= 49.373382313547815`;
- `Mz = 495967542504696380404904555281339/950737950171172051122527404032 ~= 521.66587272066056`.

The exact verifier proves `M_j=V*C_j` for all three coordinates. Therefore the first moments of the translated body are exactly `(0,0,0)`.

### 3.2 Irredundant H-representation, maximal faces, and true edges

For each listed maximal face cycle `f=(a,b,c,...)`, define the integer outward normal

`n_f=(Q_b-Q_a) x (Q_c-Q_a)`

and support `h_f=n_f·Q_a`. The uncentered halfspace is `n_f·p <= h_f/D`; the centered halfspace is `n_f·x <= h_f/D-n_f·C`. Exact strict support tests prove that every nonincident vertex lies on the inner side, so these 20 rows are irredundant.

Maximal outward face cycles:

0. `[1, 6, 0]`
1. `[0, 11, 4]`
2. `[6, 5, 0]`
3. `[0, 5, 11]`
4. `[2, 1, 0, 4, 3]`
5. `[6, 1, 2]`
6. `[2, 3, 10]`
7. `[7, 6, 2]`
8. `[7, 2, 8]`
9. `[8, 2, 10]`
10. `[3, 4, 10]`
11. `[10, 4, 9]`
12. `[9, 4, 12]`
13. `[4, 11, 12]`
14. `[7, 5, 6]`
15. `[5, 7, 12]`
16. `[11, 5, 12]`
17. `[12, 7, 8]`
18. `[12, 8, 10]`
19. `[10, 9, 12]`

True-edge lattice, 31 edges:

`(0,1)`, `(0,4)`, `(0,5)`, `(0,6)`, `(0,11)`, `(1,2)`, `(1,6)`, `(2,3)`, `(2,6)`, `(2,7)`, `(2,8)`, `(2,10)`, `(3,4)`, `(3,10)`, `(4,9)`, `(4,10)`, `(4,11)`, `(4,12)`, `(5,6)`, `(5,7)`, `(5,11)`, `(5,12)`, `(6,7)`, `(7,8)`, `(7,12)`, `(8,10)`, `(8,12)`, `(9,10)`, `(9,12)`, `(10,12)`, `(11,12)`

The f-vector is exactly `(13,31,20)`. The bottom pentagon is the only nonsimplicial maximal face; fan triangulation gives 22 outward mesh triangles.

### 3.3 Equilibrium conventions

All margins below are computed after translation to the exact ordinary-volume centroid. With `R=max_i ||x_i||`:

- a face is stable iff every oriented boundary-edge projection component is positive; the reported face margin is the minimum signed in-face distance divided by `R`;
- a vertex `v` is unstable iff `-x_v·(x_w-x_v)>0` for every true neighbor `w`; the reported margin divides by `R||x_w-x_v||`;
- for true edge `uv`, let `p=x_u+t(x_v-x_u)` be the perpendicular foot and write `p=alpha*n_1+beta*n_2` in the two incident **unit** outward normals. It is a saddle iff all four components `(t,1-t,alpha/R,beta/R)` are positive.

The exact verifier uses integer/Fraction sign numerators; the table is an independent normalized floating presentation.

### Exhaustive normalized face audit

| maximal face cycle | min oriented-edge component | status |
|---|---:|---|
| `[1, 6, 0]` | -0.017029616405 | inactive |
| `[0, 11, 4]` | -0.233504053952 | inactive |
| `[6, 5, 0]` | -0.101909780039 | inactive |
| `[0, 5, 11]` | -0.297425903384 | inactive |
| `[2, 1, 0, 4, 3]` | +0.00433123469983 | stable |
| `[6, 1, 2]` | -0.260376126368 | inactive |
| `[2, 3, 10]` | -0.0560801444921 | inactive |
| `[7, 6, 2]` | -0.210370043176 | inactive |
| `[7, 2, 8]` | -0.22414305456 | inactive |
| `[8, 2, 10]` | -0.06047159478 | inactive |
| `[3, 4, 10]` | -0.0366318379553 | inactive |
| `[10, 4, 9]` | -0.20400950142 | inactive |
| `[9, 4, 12]` | -0.036147799831 | inactive |
| `[4, 11, 12]` | -0.0167507268813 | inactive |
| `[7, 5, 6]` | -0.0715118738838 | inactive |
| `[5, 7, 12]` | -0.0553643544666 | inactive |
| `[11, 5, 12]` | +0.0247607946777 | stable |
| `[12, 7, 8]` | +0.0688319803097 | stable |
| `[12, 8, 10]` | -0.000527913225456 | inactive |
| `[10, 9, 12]` | -0.0283922091952 | inactive |

### Exhaustive normalized vertex audit

| vertex | min incident-edge support | status |
|---:|---:|---|
| 0 | -0.00813583787213 | inactive |
| 1 | -0.00152974674653 | inactive |
| 2 | -0.000568982561171 | inactive |
| 3 | -0.0367538927143 | inactive |
| 4 | -0.0094825241267 | inactive |
| 5 | -0.084592483571 | inactive |
| 6 | -0.0159299750979 | inactive |
| 7 | -0.0598254025589 | inactive |
| 8 | -0.0570712661914 | inactive |
| 9 | -0.24837856384 | inactive |
| 10 | +0.0823898742597 | unstable |
| 11 | -0.266043195841 | inactive |
| 12 | +0.989018776411 | unstable |

### Exhaustive normalized true-edge audit

Components are `(t,1-t,alpha/R,beta/R)`.
| true edge | t | 1-t | alpha/R | beta/R | min | status |
|---|---:|---:|---:|---:|---:|---|
| `(0, 1)` | +0.684485556 | +0.315514444 | +0.01835136641 | +0.3435475213 | +0.01835136641 | saddle |
| `(0, 4)` | -0.1404211717 | +1.140421172 | +0.04081377549 | +0.3495306912 | -0.1404211717 | inactive |
| `(0, 5)` | +1.231994161 | -0.2319941609 | +0.4071247215 | -0.1379551072 | -0.2319941609 | inactive |
| `(0, 6)` | +1.068954135 | -0.06895413509 | +0.3900094421 | -0.04147370763 | -0.06895413509 | inactive |
| `(0, 11)` | +8.746901928 | -7.746901928 | +3.925093828 | -3.785666586 | -7.746901928 | inactive |
| `(1, 2)` | -0.02640279119 | +1.026402791 | +0.3467844705 | +0.02374110074 | -0.02640279119 | inactive |
| `(1, 6)` | +1.238570826 | -0.2385708257 | +0.3449970799 | +0.01098743048 | -0.2385708257 | inactive |
| `(2, 3)` | -0.009820402185 | +1.009820402 | +0.1768492936 | +0.194778155 | -0.009820402185 | inactive |
| `(2, 6)` | +0.8328175813 | +0.1671824187 | +1.068690846 | -0.8715501226 | -0.8715501226 | inactive |
| `(2, 7)` | +0.8979460815 | +0.1020539185 | +1.689848296 | -1.555801742 | -1.555801742 | inactive |
| `(2, 8)` | +2.598183266 | -1.598183266 | -0.04082145631 | +0.370429269 | -1.598183266 | inactive |
| `(2, 10)` | +0.07551876986 | +0.9244812301 | +0.8221291713 | -0.4632127979 | -0.4632127979 | inactive |
| `(3, 4)` | +0.7113164448 | +0.2886835552 | -0.349607266 | +0.7149230525 | -0.349607266 | inactive |
| `(3, 10)` | -0.805370926 | +1.805370926 | +0.1350271625 | +0.2386214331 | -0.805370926 | inactive |
| `(4, 9)` | +2.203372358 | -1.203372358 | +2.635632626 | -2.575005715 | -2.575005715 | inactive |
| `(4, 10)` | -0.1283858984 | +1.128385898 | +0.3640633462 | +0.03926607275 | -0.1283858984 | inactive |
| `(4, 11)` | +4.636188956 | -3.636188956 | +0.6917696225 | -0.5970309671 | -3.636188956 | inactive |
| `(4, 12)` | +0.2672180956 | +0.7327819044 | +0.1718533125 | -0.1248582895 | -0.1248582895 | inactive |
| `(5, 6)` | -1.35401544 | +2.35401544 | +0.26358583 | +0.08127273227 | -1.35401544 | inactive |
| `(5, 7)` | +1.384937469 | -0.3849374692 | +0.2455617887 | +0.0584926419 | -0.3849374692 | inactive |
| `(5, 11)` | +0.4134114256 | +0.5865885744 | +1.02686 | -0.9387684187 | -0.9387684187 | inactive |
| `(5, 12)` | +0.2440472266 | +0.7559527734 | +0.2123005598 | -0.1647645846 | -0.1647645846 | inactive |
| `(6, 7)` | +1.217500323 | -0.2175003228 | -0.115525415 | +0.3359652689 | -0.2175003228 | inactive |
| `(7, 8)` | +0.1733450666 | +0.8266549334 | +0.7274982384 | -0.6489113428 | -0.6489113428 | inactive |
| `(7, 12)` | +0.1770880464 | +0.8229119536 | +0.2450053508 | +0.2321247227 | +0.1770880464 | saddle |
| `(8, 10)` | -0.3357310206 | +1.335731021 | +0.377415143 | -0.06526352243 | -0.3357310206 | inactive |
| `(8, 12)` | +0.2604139692 | +0.7395860308 | -0.000590169576 | +0.07694927627 | -0.000590169576 | inactive |
| `(9, 10)` | -2.166032641 | +3.166032641 | +0.04480890179 | +0.08595399245 | -2.166032641 | inactive |
| `(9, 12)` | +0.2008827567 | +0.7991172433 | +0.03283699015 | +0.09141321875 | +0.03283699015 | saddle |
| `(10, 12)` | +0.2681573481 | +0.7318426519 | -0.06610584624 | +0.1581178647 | -0.06610584624 | inactive |
| `(11, 12)` | +0.2499815853 | +0.7500184147 | +0.1169782865 | -0.07913604364 | -0.07913604364 | inactive |


Therefore the endpoint has strict class

`(S,U,H)=(3,2,3)`,

with stable faces `[2,1,0,4,3]`, `[11,5,12]`, `[12,7,8]`; unstable vertices `10,12`; and saddle edges `(0,1)`, `(7,12)`, `(9,12)`. Euler checks: `3+2-3=2`.

The residual packet is literal:

- upper-A `S-H`: stable face `[12,7,8]`, margin `+0.06883198030967437`; saddle `(7,12)`, margin `+0.17708804644558052`;
- upper-B `S-H`: stable face `[11,5,12]`, margin `+0.024760794677662578`; saddle `(9,12)`, margin `+0.03283699014659213`;
- lower `U-H`: unstable vertex `10`, margin `+0.08238987425965262`; saddle `(0,1)`, margin `+0.018351366414630865`.

Target margins are bottom face `+0.004331234699828685` and apex vertex `12` `+0.9890187764114383`. Closest inactive margins are face `[12,8,10]` `-0.0005279132254560024`, vertex `2` `-0.0005689825611708741`, and edge `(8,12)` `-0.0005901695760013298`. Minimum nonincident plane distance is `0.020812839908690015`, or `0.001025775567109439 R`; the exact smallest integer support slack is `132563791390238002800` in the stated scaled H-system.

### 3.4 Open perturbation certificate and mesh

Exact rational interval arithmetic certifies the same face lattice and the same `(3,2,3)` equilibrium class when base vertices `0..4` are fixed and each of the 24 coordinates of vertices `5..12` is perturbed independently by at most

`epsilon=2^-12=0.000244140625`.

The exact volume interval over this box is

`[2332858465187491188990919/28334198897217871282176, 778513406787852374371309/9444732965739290427392] ~= [82.33366588728768,82.42831317856258]`.

The centered OBJ/STL has 13 vertices and 22 triangles. Independent Qhull reconstruction agrees on `(13,31,20)` and `(3,2,3)`. A separate Trimesh read reports watertight `true`, winding-consistent `true`, Euler number `2`, volume `82.380987480002133`, and center of mass `[4.4922299775971235e-17, 4.312540778493238e-17, 3.953162380285468e-17]`.

## 4. Exact connected lower-plus-two-upper family

### 4.1 Generator and connected support

Define, for rational `t` in the declared branch domain `[-2/5,3/5]`,

`P_i(t)=(Q_i+t W_i)/2^24`,

with `Q` above and integer direction numerators:

| i | Wx | Wy | Wz |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 |
| 5 | -2090163 | 5056085 | 301657 |
| 6 | 10088330 | 2505936 | -438124 |
| 7 | -17668977 | 28044696 | -3888116 |
| 8 | -151346 | 5495350 | 1872153 |
| 9 | -1040775 | 290294 | 1690171 |
| 10 | 3037458 | 800309 | -3480465 |
| 11 | -8361149 | 979894 | -2064892 |
| 12 | -2181471 | -1199693 | 5741250 |

The base `0..4` is fixed. The moved support `{5,6,7,8,9,10,11,12}` is connected in the true-edge graph at `t=0`. Its three overlapping subpatches are:

- upper A: vertices `{7,8,12}`, stable face `[12,7,8]`, saddle `(7,12)`;
- upper B: vertices `{5,9,11,12}`, stable face `[11,5,12]`, saddle `(9,12)`;
- lower: vertices `{5,6,10,12}`, unstable vertex `10`, saddle `(0,1)`, attached through true-edge routes `1-6-7-12-10` and `1-6-5-12-10`.

Thus the lower route is coupled to both upper routes in one actual connected support, not by three independent caps.

In residual order

`[F(12,7,8), E(7,12), F(11,5,12), E(9,12), V10, E(0,1)]`,

the values at `t=0` are

`[0.06883198124,0.17708804684,0.02476079379,0.03283695155,0.08238987744,0.01835136003]`,

and numerical derivatives of the exact affine direction are

`[-0.06847034163,-0.17664882827,-0.02447833303,-0.03283768785,-0.08238633757,-0.01829751046]`.

Every original defect therefore initially moves toward cancellation.

### 4.2 Exhaustive circuit and equilibrium analysis

For every 4-subset of vertices, the affine family’s oriented circuit determinant is an exact integer polynomial of degree at most three. Every actual circuit root in the declared domain was isolated exactly; after every event the hull, maximal faces, and true edges were rebuilt. Within each fixed-lattice cell, exact ordinary volume, three first moments, face components, all incident vertex supports, and all four edge-cone components were expanded as integer polynomials. There are 1,428 unique primitive component polynomials, 31 real root clusters, and 12 feature-changing clusters. Exact rational samples prove every component nonzero and `M=VC` in all 39 open subcells. No subcell has `(1,1,0)`.

### Exact circuit/topology events

| t (decimal locator) | exact isolator | topology change |
|---:|---|---|
| -0.387557491441016 | `-542577/1399991` | V- [], V+ [3]; E- [[0, 10], [1, 10]], E+ [[2, 3], [3, 4], [3, 10]]; f-vector (12, 30, 20)->(13, 31, 20) |
| -0.387523942805732 | `[-7096085/18311346,-5730644/14787845]` | E- [[8, 9]], E+ [[10, 12]]; f-vector (13, 31, 20)->(13, 31, 20) |
| -0.341424338586254 | `[-3548037/10391869,-5349653/15668634]` | E- [[1, 7]], E+ [[2, 6]]; f-vector (13, 31, 20)->(13, 31, 20) |
| 0.152007077807521 | `[1021426/6719595,3347597/22022639]` | E- [[7, 8]], E+ [[2, 12]]; f-vector (13, 31, 20)->(13, 31, 20) |
| 0.290042409669552 | `[2029492/6997225,7503273/25869572]` | V- [8], V+ []; E- [[2, 8], [8, 10], [8, 12]], E+ []; f-vector (13, 31, 20)->(12, 28, 18) |
| 0.470290851198847 | `[2652423/5639963,49266713/104757966]` | E- [[0, 6]], E+ [[1, 5]]; f-vector (12, 28, 18)->(12, 28, 18) |
| 0.500626694542663 | `[10297007/20568234,11073077/22118431]` | E- [[5, 12]], E+ [[7, 11]]; f-vector (12, 28, 18)->(12, 28, 18) |


### Exact equilibrium-status events

| t (decimal locator) | rational isolator | class change | simultaneous zero components |
|---:|---|---|---|
| -0.227012462562473 | `-4715114/20770287` to `-168421/741902` | `(5, 5, 8)->(5, 4, 7)` | `['V', 7, 6]`, `['E', [6, 7], 1]` |
| -0.197493818842144 | `-343233/1737943` to `-3449903/17468410` | `(5, 4, 7)->(5, 3, 6)` | `['V', 1, 2]`, `['E', [1, 2], 0]` |
| -0.184135695434448 | `-479252/2602711` to `-823425/4471838` | `(5, 3, 6)->(4, 3, 5)` | `['F', [0, 1, 6], 6, 0]`, `['E', [0, 6], 3]` |
| -0.146212733689281 | `-329330/2252403` to `-1186203/8112857` | `(4, 3, 5)->(4, 2, 4)` | `['V', 6, 1]`, `['E', [1, 6], 1]` |
| -0.00616550392729614 | `-20893/3388693` to `-31119/5047276` | `(4, 2, 4)->(3, 2, 3)` | `['F', [8, 10, 12], 12, 8]`, `['E', [8, 12], 2]` |
| 0.0259105716561282 | `26844/1036025` to `321953/12425546` | `(3, 2, 3)->(3, 3, 4)` | `['V', 2, 3]`, `['E', [2, 3], 0]` |
| 0.215799397956564 | `312779/1449397` to `2131887/9879022` | `(3, 3, 4)->(3, 4, 5)` | `['V', 4, 10]`, `['E', [4, 10], 0]` |
| 0.397256432275012 | `182732/459985` to `9385909/23626827` | `(3, 4, 5)->(4, 4, 6)` | `['F', [3, 4, 10], 3, 4]`, `['E', [3, 4], 2]` |
| 0.431411655841512 | `6887409/15964819` to `6839389/15853510` | `(4, 4, 6)->(4, 5, 7)` | `['V', 3, 10]`, `['E', [3, 10], 0]` |
| 0.442538309303334 | `2003328/4526903` to `1172615/2649748` | `(4, 5, 7)->(4, 6, 8)` | `['V', 1, 2]`, `['E', [1, 2], 0]` |
| 0.541469981950571 | `3746009/6918221` to `4295000/7932111` | `(4, 6, 8)->(3, 6, 7)` | `['F', [3, 4, 10], 4, 10]`, `['E', [4, 10], 3]` |
| 0.578809931020169 | `1425463/2462748` to `4938694/8532497` | `(3, 6, 7)->(3, 7, 8)` | `['V', 0, 4]`, `['E', [0, 4], 0]` |


### Complete open-cell sequence on `t in [-2/5,3/5]`

| cell | open interval | `(V,E,F)` | `(S,U,H)` |
|---:|---|---|---|
| 0 | `(-0.4, -0.387557491441016)` | `(12, 30, 20)` | `(5, 5, 8)` |
| 1 | `(-0.387557491441016, -0.387523942805732)` | `(13, 31, 20)` | `(5, 5, 8)` |
| 2 | `(-0.387523942805732, -0.341424338586254)` | `(13, 31, 20)` | `(5, 5, 8)` |
| 3 | `(-0.341424338586254, -0.227012462562473)` | `(13, 31, 20)` | `(5, 5, 8)` |
| 4 | `(-0.227012462562473, -0.197493818842144)` | `(13, 31, 20)` | `(5, 4, 7)` |
| 5 | `(-0.197493818842144, -0.184135695434448)` | `(13, 31, 20)` | `(5, 3, 6)` |
| 6 | `(-0.184135695434448, -0.146212733689281)` | `(13, 31, 20)` | `(4, 3, 5)` |
| 7 | `(-0.146212733689281, -0.00616550392729614)` | `(13, 31, 20)` | `(4, 2, 4)` |
| 8 | `(-0.00616550392729614, 0.0259105716561282)` | `(13, 31, 20)` | `(3, 2, 3)` |
| 9 | `(0.0259105716561282, 0.152007077807521)` | `(13, 31, 20)` | `(3, 3, 4)` |
| 10 | `(0.152007077807521, 0.215799397956564)` | `(13, 31, 20)` | `(3, 3, 4)` |
| 11 | `(0.215799397956564, 0.290042409669552)` | `(13, 31, 20)` | `(3, 4, 5)` |
| 12 | `(0.290042409669552, 0.397256432275012)` | `(12, 28, 18)` | `(3, 4, 5)` |
| 13 | `(0.397256432275012, 0.431411655841512)` | `(12, 28, 18)` | `(4, 4, 6)` |
| 14 | `(0.431411655841512, 0.442538309303334)` | `(12, 28, 18)` | `(4, 5, 7)` |
| 15 | `(0.442538309303334, 0.470290851198847)` | `(12, 28, 18)` | `(4, 6, 8)` |
| 16 | `(0.470290851198847, 0.500626694542663)` | `(12, 28, 18)` | `(4, 6, 8)` |
| 17 | `(0.500626694542663, 0.541469981950571)` | `(12, 28, 18)` | `(4, 6, 8)` |
| 18 | `(0.541469981950571, 0.578809931020169)` | `(12, 28, 18)` | `(3, 6, 7)` |
| 19 | `(0.578809931020169, 0.6)` | `(12, 28, 18)` | `(3, 7, 8)` |


The family’s strongest interval is cell 8,

`-0.006165503927296... < t < 0.025910571656128...`,

where the class remains `(3,2,3)`. There is no winner cell.

### 4.3 Precise obstruction

The first forward equilibrium-status event is isolated in

`26844/1036025 < t_* < 321953/12425546`,

with `t_* ~= 0.02591057165612822`. At `t_*`, vertex `2` and true edge `(2,3)` simultaneously cross zero, activating a **new lower unstable-saddle pair**:

`(3,2,3) -> (3,3,4)`.

Immediately before that event, the six original residuals are still robust:

- `F[12,7,8] = +0.0670557873`;
- `H(7,12) = +0.1724677631`;
- `F[11,5,12] = +0.0241213265`;
- `H(9,12) = +0.0319882762`;
- `U10 = +0.0802741320`;
- `H(0,1) = +0.0179115361`.

So the connected deformation does not reach any intended cancellation before a different U-H packet enters. In the negative direction, the first feature event is the activation of face `[8,10,12]` and edge `(8,12)`, giving `(4,2,4)`. This is a two-sided transfer obstruction, not a numerical failure.

A guard tangent that forces `V2` and `E(2,3)` farther inactive merely moves the first incoming packet to `V4/E(4,10)` before any original residual vanishes. The genuinely new successor is therefore not another one-dimensional retuning. It is a two-parameter connected **guarded Y-patch** that adds an independent branch across triangle `[2,3,10]` and edge `(2,3)` while retaining the current upper-A/upper-B/lower support, then enumerates the resulting 2D circuit arrangement. Its hard conditions should be: all six original derivatives negative, both incoming-pair derivatives nonpositive, exact three-moment centering in every cell, and deletion of obsolete vertices only after cross-links enter.

## 5. Reproducible artifacts

The portable archive contains source, exact reports, event isolators, verification summaries, SHA-256 manifest, and a `[internal-source-reference].sh` entry point:

- Complete portable bundle (`conway13_connected_three_patch_nonwinner.zip`)
- Exact integer/Fraction endpoint verifier (`verify_conway13_exact.py`)
- Complete exact endpoint report (`conway13_exact_report.json`)
- Independent Qhull/mesh verifier (`verify_conway13_independent.py`)
- Exact perturbation certificate (`perturbation_certificate.json`)
- Centered watertight OBJ (`conway13_endpoint_centered.obj`)
- Centered watertight STL (`conway13_endpoint_centered.stl`)
- Self-contained exact connected-family generator (`connected_three_patch_family.py`)
- Exact verification of all family subcells (`family_exact_verification.json`)
- All equilibrium-component root clusters (`equilibrium_cluster_report.json`)
- Exact circuit/topology event report (`circuit_event_report.json`)

A clean extraction was tested by rerunning the exact endpoint verifier, independent verifier, perturbation verifier, exact family verifier, Conway-21 reconstruction, family generator, and SHA-256 manifest. The acceptance gate described in the journal—full H/V data, exact or isolated centroid, positive margins, independent verification, perturbation radius, and OBJ/STL—is met for the **nonwinner endpoint and the closed family**, but not for a Gömböc.

## 6. Reusable conclusion

The branch is now transport-complete and mathematically explicit:

- literal verdict: **NONWINNER**;
- strongest exact endpoint: dyadic `(13,31,20)` body `C13`, class `(3,2,3)`;
- exact residual packet: two upper `S-H` pairs and one lower `U-H` pair, listed above;
- exact connected family: `P(t)=(Q+tW)/2^24`, `t in [-2/5,3/5]`;
- exhaustive family result: 7 topology events, 1,428 primitive component polynomials, 31 root clusters, 39 exact open subcells, zero winner cells;
- obstruction: before any original residual cancels, `V2/E(2,3)` enters; guarding it transfers the incoming pair to `V4/E(4,10)`;
- successor: a guarded two-parameter connected Y-patch spanning both incoming lower walls and both upper routes, with exact moment equations and full 2D circuit enumeration.
