# figure-0188

Historical AI scientific report · saved 2026-09-01 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Vivid Quartz 58 — exact four-control continuation of `E10R`

## Literal determination

**NONWINNER.** I did not obtain a uniform-density convex polyhedron with strict own-centroid `(S,U,H)=(1,1,0)`. The original acceptance gate requires a finite exact V/H body, its own ordinary-volume centroid, exhaustive maximal-face/vertex/full-true-edge-cone margins, an open strict neighbourhood, independent verification, and matching meshes. :contentReference[oaicite:0]{index=0} The inherited frontier was the exact `E10R` body `(10,24,16)`, class `(2,2,2)`, whose one-dimensional central-circuit atlas was exhausted and whose next construction required at least four transverse controls. :contentReference[oaicite:1]{index=1}

This work genuinely leaves that line. It materializes exact connected residual-disk replacements and actual-cell controls

```text
E10R (10,24,16), (2,2,2)
 -> E11S (11,27,18), (2,2,2)
 -> E13A (13,33,22), (2,2,2)
 -> E14C (14,36,24), (2,2,2), exact rank-four cell
 -> E15A (15,39,26), (2,3,3), exact two-support escape
 -> E17G (17,45,30), (24,12,34), exact next two-cell topology
```

The strongest mechanical endpoint is `E14C`. Every original residual feature of `E10R`—stable `[D,1,11]`, unstable `D`, and saddles `(1,A),(11,12)`—is absent in its actual lattice, while protected stable `[8,A,B]` and unstable `8` survive. The packet transfers to stable `[1,11,E]`, unstable `M`, and saddles `(2,K),(11,L)`.

## Immutable artifacts

- [Complete exact archive](sandbox:/mnt/data/vivid_quartz_58_four_control_nonwinner.zip), SHA-256 `d891aded39167da2ff4806022f5290491c5dbb9e24fbeda3c8abdf49986e8268`; [hash file](sandbox:/mnt/data/vivid_quartz_58_four_control_nonwinner.zip.sha256).
- [Full determination](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/RESULT.md), [README](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/README.md), [one-command verifier](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/[internal-source-reference].sh), [123-file manifest](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/SHA256SUMS), and [verification record](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/VERIFICATION_RECORD.json).

## 1. First four-control escape and exact preemption

`E11S` replaces old vertex `D` and its six-face star by internal vertices `E,F` sharing true edge `(E,F)`. It is exact `(11,27,18)`, strict `(2,2,2)`, with stable `[1,11,E]`,`[8,A,B]`, unstable `8,E`, saddles `(1,A),(11,12)`, and a simultaneous `2^-12` coordinate box. A direct exact Jacobian using controls `11.x,11.y,A.z,E.z` has rank four and decreases the four selected residual sheets at first order; see [first-jet certificate](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E11S_four_control_first_jet.json).

The complete exact own-centroid event atlas on `0<=t<=3/20` expands all 216 active support/mechanical primitives. Its only events are:

- `t≈0.1167210975479633`: `[8,10,11]`/`(8,10)` witness transfer, class unchanged.
- `t≈0.1392410386132671`: compensating `U11/H(8,11)` birth, class `(2,2,2)->(2,3,3)`.

None of the four intended deaths occurs first. Exact disposition: `COMMON_DESCENT_PREEMPTED_BEFORE_SELECTED_DEATHS`; [atlas](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E11S_common_descent_event_atlas.json), [independent verification](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E11S_common_descent_independent_verification.json).

A separate exact `E-F` transfer atlas has roots `0.001042888715279273` and `0.002338746250850858`, with class `(2,2,2)->(2,3,3)->(2,2,2)`. The exact identity

```text
[-x_E·(x_F-x_E)] + [-x_F·(x_E-x_F)] = ||x_E-x_F||^2 > 0
```

plus strict external arrows forces at least one of `E,F` unstable; together with protected `8`, `U>=2`. [Transfer atlas](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E11S_EF_transfer_atlas.json).

## 2. Strongest exact four-control endpoint `E14C`

### V-representation and exact mass

Use denominator `D=2^44=17592186044416`. Before centring, the integer numerators are

```text
1: (10093742548992,-9247256281088,-64571988967424)
2: (20254250186752,-38366003956224,-56690476593152)
8: (32221947693056,-104787513012224,-10890450550784)
10: (17592186044416,0,0)
12: (5555380762624,50861491039744,0)
11: (0,0,0)
A: (26205901996032,59257787789312,-72483135666176)
B: (27661354434560,76150386706688,-26439056156672)
C: (8732129723680,85291497297207,-17159176195936)
E: (5597662997369,108963881606168,-33140049786718)
F: (6452271996652,109053996908278,-31958314230539)
K: (17813931395540,23785813497214,-77855104105374)
L: (2769241107264,25428444725145,13480605779)
M: (6020438898535,109032878406198,-32547732532593)
```

The physical body is `conv{Q_i/D-C}`. Its exact ordinary volume and own centroid are

```text
V  = 1837480292869196496764041411397422590959/63802943797675961899382738893456539648
Cx = 62875560221724170537088731857213847700949370040057323/64650590330205806259399292442555282938761136348069888
Cy = 114748619515096826984389598002879542621701481995072765/129301180660411612518798584885110565877522272696139776
Cz = -118265124036688573413698306725971053631655564298522345/64650590330205806259399292442555282938761136348069888
```

The exact uncentred first moments are

```text
Mx = 62875560221724170537088731857213847700949370040057323/2244866514940266882360859903052210718191512386011136
My = 114748619515096826984389598002879542621701481995072765/4489733029880533764721719806104421436383024772022272
Mz = -118265124036688573413698306725971053631655564298522345/2244866514940266882360859903052210718191512386011136
```

The verifier proves `M_j=V*C_j` exactly, hence translated first moments are `(0,0,0)`.

### Actual maximal faces and every true edge

```text
faces:
[1,2,8] [1,K,2] [1,8,11] [1,11,E] [1,E,K] [2,A,8] [2,K,A] [8,10,11] [8,B,10] [8,A,B] [10,B,12] [10,12,L] [10,L,11] [12,B,C] [12,C,F] [12,E,L] [12,M,E] [12,F,M] [11,L,E] [A,F,B] [A,K,E] [A,E,M] [A,M,F] [B,F,C]

edges:
(1,2) (1,8) (1,11) (1,E) (1,K) (2,8) (2,A) (2,K) (8,10) (8,11) (8,A) (8,B) (10,12) (10,11) (10,B) (10,L) (12,B) (12,C) (12,E) (12,F) (12,L) (12,M) (11,E) (11,L) (A,B) (A,E) (A,F) (A,K) (A,M) (B,C) (B,F) (C,F) (E,K) (E,L) (E,M) (F,M)
```

Thus `(V,E,F)=(14,36,24)` and Euler characteristic is two. [Complete exact H representation](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E14C_H_representation.json) records the primitive integer outward normal, integer support, centred rational RHS, and every nonincident slack for all 24 faces.

### Exhaustive own-centroid mechanics

- stable faces: `[1,11,E]`, `[8,A,B]`;
- unstable vertices: `8`, `M`;
- saddle true edges: `(2,K)`, `(11,L)`;
- strict class: `(2,2,2)`;
- minimum absolute normalized feature separation: `0.01112295059606298`;
- minimum circumradius-normalized nonincidence separation: `0.0001704264077852687`;
- simultaneous all-42-coordinate perturbation radius: `2^-19`.

Every face component, every directed neighbour component at every vertex, and all four components `(t,1-t,alpha,beta)` for every true edge are in the [exhaustive audit](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E14C_audit.md) and [exact report](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E14C_exact_report.json). The clean-room Qhull/tetrahedral/full-cone/Trimesh reconstruction returns `INDEPENDENT_E14C_RECONSTRUCTION_PASS`; [report](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E14C_independent_verification.json), [OBJ](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E14C_centered.obj), [STL](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E14C_centered.stl).

### Genuine four-dimensional cell

The residual primitives are stable `[E,1,11]` component 0, unstable `M->E`, saddle `(2,K)` beta, and saddle `(11,L)` beta. Direct controls are `E.z,M.z,K.x,L.y`. Their exact normalized Jacobian has rank four; singular values are

```text
[4.666808274756124, 3.4907504945146703, 1.6598842288776647, 0.1471711867059291]
```

and the exact dual basis satisfies `A*B=-I_4`. Each parameter ranges in `[-2^-22,2^-22]`, strictly inside the `2^-19` coordinate box, preserving the actual hull, class, `[8,A,B]`, and `8`. The connected external-positive component `{E,F,M}` forces another unstable vertex, so `U>=2` throughout this certified four-cube. [Four-control certificate](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E14C_four_control_certificate.json).

## 3. Rigorous one-support obstruction and exact two-support escape

For each face incident to `M`, the fixed-plane cap system admits a positive integer dependence of required outward normals with zero weighted normal sum and strictly positive weighted support sum. The four exact sums are

```text
24727761304018579161045912530837408195668732160256086179121234347180518432433127743154820129713723392
3563565021212408388409891179511429135782110480249400843317979348192116024914400297806105384872351744
7104690780744204745884892812452823906466010301822625168324650017802741175606317052540582768670154752
1035228257188886394340634831459418012156157657265942969792934579469901037062411547631758428630286336
```

Consequently one new visibility-cap vertex cannot simultaneously delete `(2,K)`, delete `(11,L)`, and attach to `M`; demanding stable `[E,1,11]` death only adds an inequality. This is a rigorous fixed-source-plane lower bound, not a global arbitrary-motion theorem. [Farkas certificate](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E14C_single_vertex_cap_obstruction.json).

`E15A` realizes the minimal two-support alternative in that model: `K` becomes inactive, new vertices `N,P` are extreme, `(N,P)` is true, and route `M-N-P-8` crosses the gap. Both old E14C saddles are absent. Exact endpoint:

- `(V,E,F)=(15,39,26)`;
- stable `[1,P,N]`,`[8,A,B]`;
- unstable `8,M,N`;
- saddles `(2,N),(E,N),(L,P)`;
- class `(2,3,3)`;
- minimum mechanics separation `0.011761716914411552`;
- minimum normalized nonincidence `1.4933679776531778e-05`;
- simultaneous perturbation box `2^-24`.

See [exact report](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E15A_exact_report.json), [H representation](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E15A_H_representation.json), [patch complex](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E14C_to_E15A_patch_complex.json), [independent verification](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E15A_independent_verification.json), [OBJ](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E15A_centered.obj), [STL](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E15A_centered.stl).

At fixed E15A planes, one further cap deleting all three saddle channels is again infeasible: the exact positive weighted support sum is

```text
11292940902961509670967631941816435349282570656859557826618041883466132490638151891739817766969746565282415517528592
```

with zero weighted normal sum. [Second obstruction](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E15A_one_cap_obstruction.json).

## 4. Next topology materialized

The smallest supplied fixed-plane successor therefore uses two new supports `Q,R`. `E17G` replaces seven faces by eleven connected faces, adds true edge `(Q,R)`, and provides route `M-R-Q-P-8`. It is a strict exact dyadic convex realization with `(V,E,F)=(17,45,30)`, exact own centring, complete H/V/E reconstruction, and independent watertight meshes. Its first realization is mechanically poor: `(S,U,H)=(24,12,34)`, not a candidate. [Exact report](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E17G_exact_report.json), [H representation](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E17G_H_representation.json), [patch](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E15A_to_E17G_patch_complex.json), [independent verification](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/E17G_independent_verification.json).

## 5. Search scope, uncertainty, and continuation

Dynamic actual-hull searches explored 23 E11S incidence cells, six E14C cells, seven E15A cells, and 87,344 valid two-cap-pair trials. No strict `(1,1,0)` body occurred; near-zero objectives lay at support/topology floors and are not exclusion proofs. Hash-bound receipts and exact/empirical separation are in the [search ledger](sandbox:/mnt/data/vivid_quartz_58_four_control_final_result/search_ledger.json).

What is proved:

1. Exact source reconstruction and exact own-centred endpoints `E11S,E13A,E14C,E15A,E17G`.
2. Exact connected disk replacements; in E14C all four original E10R residual features are absent simultaneously.
3. A genuine full-rank four-control E14C neighbourhood with complete actual incidence and `U>=2` forcing.
4. Complete exact endpoint H/V/E and exhaustive face/vertex/full-edge-cone audits, positive perturbation boxes, independent verifiers, and meshes for the strongest endpoints.
5. Fixed-plane Farkas exclusion of one cap at E14C; exact two-support E15A escape; fixed-plane exclusion of one additional cap at E15A; exact realization of the next two-cell topology.

What is not proved:

- No global exclusion of the full ten-vertex central-quadrilateral realization space is claimed.
- Except for the explicit E11S event paths, the disk certificates compare exact source and target lattices; they are not a single certified polynomial homotopy through E13A/E14C/E15A.
- The cap lower bounds hold for the displayed fixed source planes; coordinated motion of old planes remains open.
- E17G is a topology anchor and has no all-coordinate perturbation theorem in this bundle.

The smallest evidence-supported continuation is therefore a nonlinear multi-control chamber that moves old planes together. Starting from the exact E15A/E17G patch, it should independently kill stable `[1,P,N]`, merge the forced `{M,N}` unstable component into protected `8`, delete `(2,N)` and `(E,N)` in one left cell, delete `(L,P)` in the right cell, and use the shared `(Q,R)` circuit to overlap the deaths before a replacement birth, with the three ordinary-volume moments imposed as dependent exact equations.

**Explicit disposition: exact materialized NONWINNER.**
