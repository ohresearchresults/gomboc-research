# figure-0095

AI research report · 2026-08-27 UTC

---

# Result: exact three-sheet/two-band Santaló annulus fallback

**Verdict.** No homogeneous convex polyhedral Gömböc was found in the tested family. The requested new topology was nevertheless materialized exactly: a finite-thickness three-sheet communicating annulus, a true 13-edge C-sheet ascent, two transverse two-cell closure bands, two separated interior circuits, and one exact wall at which all four blocks cross simultaneously. The strongest gate-valid endpoint is exact own-centroid `(S,U,H)=(2,2,2)`, not a wall point and not a winner. :contentReference[oaicite:0]{index=0} The journal’s unavailable two-sheet endpoint was therefore reconstructed and strictly advanced rather than assumed. :contentReference[oaicite:1]{index=1}

## Exact finite object

Positive/gate endpoint: `Q=(V,E,F)=(30,84,56)`, `P=Q^circ=(56,84,30)`, complexity `168`, all 30 Q rows extreme, all 56 P vertices actual, exact uniform centroid and exact first moment `(0,0,0)`, P inactive separation `3.4506256306799736e-5`, Q inactive separation `0.048049583353331746`. The negative strict side has the same f-vectors and exact centering, class `(3,2,3)`, P/Q separations `1.903490389483464e-5` and `0.03565070087309026`. :contentReference[oaicite:2]{index=2}

## Deterministic exact Q generator

Interpret each hexadecimal literal exactly by `Fraction.from_float(float.fromhex(h))`; every support constant is one. Let `Q_raw=conv(q_i)` and `P0={x:q_i·x<=1}`.

```text
00 old17: (0x0.0p+0, 0x0.0p+0, 0x1.dd07bb4ca6c00p+5)
01 A5: (-0x1.9a6c00fec77ddp+3, 0x1.0f962ae3eb09fp+5, -0x1.0e993f9931a1cp+4)
02 A6: (-0x1.c0da14979312cp+3, 0x1.2dd52f4d73205p+5, -0x1.19e3a756282b3p+3)
03 A7: (-0x1.d6a812e8ca739p+3, 0x1.3e2eb72ac7765p+5, 0x1.c40990f040dd2p-3)
04 A8: (-0x1.da825b0702fb2p+3, 0x1.3eeb56d666aecp+5, 0x1.38bf5f175a765p+3)
05 A9: (-0x1.ca8dc361008f5p+3, 0x1.2f21813d88193p+5, 0x1.3651c737f2e4cp+4)
06 A10: (-0x1.a47f7af9b439ap+3, 0x1.0ece3fe1786f3p+5, 0x1.c99ed1d9b1cfbp+4)
07 B1: (-0x1.441a13dbc191dp+2, 0x1.513f0c9c08774p+3, -0x1.612fdd64ce9ecp+5)
08 B2: (-0x1.39df6f48a95d0p+3, 0x1.3a08c99acbdb2p+4, -0x1.3409004139f51p+5)
09 B3: (-0x1.d17cb6350e159p+3, 0x1.c20101a007d0fp+4, -0x1.d17951b66949ep+4)
10 B4: (-0x1.2f266f6e28327p+4, 0x1.1cf25ee3c42c7p+5, -0x1.0c9a6012a4162p+4)
11 B5: (-0x1.6aa119d4f22b3p+4, 0x1.4dd8181db4436p+5, -0x1.61865c0fedbeep+1)
12 B8: (-0x1.ace2d9d413430p+4, 0x1.8604ff7855ba8p+5, 0x1.2b43fa075d327p+5)
13 B9: (-0x1.948f03050a098p+4, 0x1.74be7ad0b3ac6p+5, 0x1.7940c0a45dd89p+5)
14 B10: (-0x1.64f689655dc14p+4, 0x1.4febb8aed1d9bp+5, 0x1.b42f48e4d74d4p+5)
15 B11: (-0x1.173d9c7194816p+4, 0x1.0d2800aef8cddp+5, 0x1.d566bb92adfddp+5)
16 B12: (-0x1.8f581682c7051p+3, 0x1.8f5b56efff245p+4, 0x1.f6cb8292dcee6p+5)
17 C0: (0x1.38295c9fad18ap-8, -0x1.22da72743bfcbp-12, -0x1.7db3c1535cf89p+5)
18 C1: (0x1.85a9eef58e27ap+3, -0x1.1c1280ca8cf6fp+2, -0x1.856811ed8e941p+5)
19 C2: (0x1.5b0e828dc4308p+4, -0x1.ef98c1bbb5124p+3, -0x1.74ef73f427f97p+5)
20 C3: (0x1.ace6474c2bad2p+4, -0x1.ebd57f1c252fep+4, -0x1.4c312712eda31p+5)
21 C4: (0x1.bc64c497f8adcp+4, -0x1.7cdeeda53909fp+5, -0x1.087f10aae2f9bp+5)
22 C5: (0x1.9ab4ebef0798bp+4, -0x1.004a7f22c8480p+6, -0x1.497ec7d271a54p+4)
23 C6: (0x1.52383dbcb1867p+4, -0x1.39240f36b3ecdp+6, -0x1.c70228e9aed85p+1)
24 C7: (0x1.bde655ddbc317p+3, -0x1.5fbb33c25578ap+6, 0x1.1d9244e869391p+4)
25 C8: (0x1.cc10d1d5f981bp+1, -0x1.689f5baea65b1p+6, 0x1.4f736c10d0a0bp+5)
26 C9: (-0x1.1bea652a4a984p+3, -0x1.49b52f00b013ap+6, 0x1.05a5630f5a9f4p+6)
27 C10: (-0x1.3a67f7bb62ba4p+4, -0x1.0181282101a2cp+6, 0x1.51605a093dbf0p+6)
28 C11: (-0x1.73856dff0f01bp+4, -0x1.3d27cb9aeb203p+5, 0x1.7f1dd40e2bd1dp+6)
29 C12: (-0x1.01ddf43f72df9p+4, -0x1.f486615315eb1p+3, 0x1.8bfa7e7bb5415p+6)
```

The negative strict endpoint differs only in these four exact rows:

```text
10 B4: (-5588822532037637/281474976710656, 4978724158821695/140737488355328, -149764222007065/8796093022208)
11 B5: (-5716241160715033/281474976710656, 1580082967738511/35184372088832, -6221405673234697/2251799813685248)
14 B10: (-3234053786108739/140737488355328, 2965833570056087/70368744177664, 7716614018238199/140737488355328)
18 C1: (426723160908739/35184372088832, -2545053414823561/562949953421312, -859787525066859/17592186044416)
```

For moved rows 10, 11, 14, 18 define exactly `q_wall=(4 q_negative+q_positive)/5` and `q(t)=q_wall+t(q_positive-q_wall)`. The certified sides are `t=1`, `t=0`, `t=-1/4`.

## Exact reconstruction and hard centering

Enumerate all non-singular row triples, solve `q_i·p=q_j·p=q_k·p=1` over `Fraction`, and retain solutions satisfying every inequality. This yields all vertices of `P0`; active-row equality and the true-edge graph yield all maximal face cycles. With each outward face triangulated into `(a,b,d)` and `Delta=det(a,b,d)>0`, compute exactly

`V(P0)=ΣDelta/6`, `c(P0)=ΣDelta(a+b+d)/(4ΣDelta)`.

For the positive endpoint `c≈(0.023697032965585074,0.0145120547324014,-0.0007527364585345451)`. Set

`T_u(q)=q/(1-q·u)`, `u=c`, `Q=T_c(Q_raw)`, `P=P0-c`.

Then `(T_uQ_raw)^circ=P0-u`, so `F(u)=centroid((T_uQ_raw)^circ)=c-u` and `DF=-I3`. Thus `u=c` is the unique exact centering solution; in centered coordinates the root is exactly zero and isolated in `[-2^-80,2^-80]^3`. Rows `(0,2,18,25)` positively span zero; all projective denominators lie in `[0.6756503497606984,2.463374558613933]`. On the root box, P support displacement is below `1.3788577408045493e-25` and Q control dot below `1.0511485658633125e-22`, proving origin interiority and bounded polarity throughout. :contentReference[oaicite:3]{index=3}

## Four-block event and deactivation

At `t=0`, Q has `(30,80,52)` and exactly four supporting quadrilateral faces; all four determinants are exactly zero and all 30 rows remain extreme on both strict sides and at the wall. The swaps are:

| block | quadrilateral | positive diagonal | negative diagonal |
|---|---|---|---|
| root closure | `B2,B3,B4,C10` | `B3-C10` | `B2-B4` |
| return closure | `B9,B10,C11,C12` | `B9-C12` | `B10-C11` |
| lower interior | `C0,C1,C2,C3` | `C0-C2` | `C1-C3` |
| upper interior | `A7,A8,B5,B8` | `A7-B8` | `A8-B5` |

The final input genuinely omits `old2,old10,old14,old24,A0-A4,A11,A12,B0,B6,B7`; in particular the requested `old2`, `old24`, `B0`, `B6/B7` relays deactivate rather than survive redundantly.

## Exhaustive own-centroid audit

The independent verifier rebuilt the complete P/Q lattices and tested all 30 maximal P faces, all 56 P vertices with complete three-normal cones, and all 84 true P edges with segment and complete two-normal-cone conditions. :contentReference[oaicite:4]{index=4}

Positive endpoint equilibria:

- stable `B10`, margin `0.0026987614091573664`;
- stable `C2`, margin `0.0046712776971201825`;
- unstable incidence `(A10,B12,C2)`, margin `0.017498454290926595`;
- unstable incidence `(B2,B3,C10)`, margin `0.003116280846426087`;
- saddle Q edge `(B2,B3)`, margin `0.0019643545900745857`;
- saddle Q edge `(C8,C12)`, margin `0.0015495773494503212`.

Closest excluded face/vertex/edge margins are `-1.3609733867968337e-4`, `-2.0735688855884796e-4`, `-2.0735688855884793e-4`. Hence the `(2,2,2)` class is open. On the negative side, `B5` becomes an additional stable row and `(B5,B8)` an additional saddle, giving `(3,2,3)`.

The complete literal positive and negative maximal-face cycles, both true-edge lists, exact rational H/V data, and all primitive sign witnesses are embedded in the exact certificates and reproduced in the self-contained handoff linked below.

## Perturbation and independent verification

A new exact noncongruent family `P_s=diag(1+s,1,1)P`, `Q_s=diag((1+s)^-1,1,1)Q` is certified for every rational `s∈[-2^-9,2^-9]`. Centroid zero, polarity and incidence are exact; 1,542 primitive face/vertex/full-cone/edge signs remain fixed by directed polynomial bounds. The condition number is at most `513/511`, and both inactive gates remain above `1e-5`.

Fresh standalone standard-library `Fraction` verification, importing neither the generator nor stored topology, passed for both endpoints. Positive SHA-256: `052905e3dadc281d660e6a231e5fba6d489c8990f31cf2053dbd2a24ffbd0d66`; negative SHA-256: `e6c070a0f68c7b45010f693d492c165a56b88ef717f96eda04462f2a082e10f0`. The rebuilt OBJ/STL meshes match all certified cycles and edge counts. :contentReference[oaicite:5]{index=5}

## Precise obstruction and next topology

The old relays are gone, but the positive side retains two new Euler-neutral relay blocks: root unstable `(B2,B3,C10)` with saddle `(B2,B3)`, and upper/return stable rows `B10,C2` with unstable `(A10,B12,C2)` and saddle `(C8,C12)`. Crossing all four blocks creates the new `B5/(B5,B8)` pair instead of annihilating the old block. Searches covering 4,000 tubular/spindle proposals, 971 valid direct C-sheet continuations, and 19,200 topology-aware local proposals found no `(1,1,0)` state.

The smallest architecture not subsumed is a four-sheet communicating annulus, or a three-sheet annulus with a third genuine transverse closure band and nonannular two-cell replacement. It must replace `B2,B3,B10,C2,C8,C10,C12,A10,B12` together, likely deactivate `B9,C3,C9,C11`, and cross at least six coupled circuit blocks while retaining the exact `u=c`, `DF=-I3` centering identity. :contentReference[oaicite:6]{index=6}

## Reproducible artifacts

- [Complete self-contained handoff with all face cycles and true edges](sandbox:/mnt/data/three_sheet_bundle/SELF_CONTAINED_HANDOFF.md)
- [Portable exact bundle ZIP](sandbox:/mnt/data/three_sheet_annulus_exact_fallback_bundle.zip)
- [ZIP SHA-256](sandbox:/mnt/data/three_sheet_annulus_exact_fallback_bundle.zip.sha256)
- [Positive exact certificate](sandbox:/mnt/data/three_sheet_bundle/three_sheet_two_band_gate_exact.json)
- [Negative exact certificate](sandbox:/mnt/data/three_sheet_bundle/three_sheet_four_block_negative_compact_exact.json)
- [Independent exact verifier](sandbox:/mnt/data/three_sheet_bundle/verify_three_sheet_independent.py)
- [Fresh PASS report](sandbox:/mnt/data/three_sheet_bundle/verification/independent_verification_fresh_combined.json)
- [Perturbation certificate](sandbox:/mnt/data/three_sheet_bundle/metric_perturbation_certificate.json)
- [Positive P OBJ](sandbox:/mnt/data/three_sheet_bundle/three_sheet_two_band_gate_P.obj) / [STL](sandbox:/mnt/data/three_sheet_bundle/three_sheet_two_band_gate_P.stl)
- [Positive Q OBJ](sandbox:/mnt/data/three_sheet_bundle/three_sheet_two_band_gate_Q.obj) / [STL](sandbox:/mnt/data/three_sheet_bundle/three_sheet_two_band_gate_Q.stl)
- [Negative P OBJ](sandbox:/mnt/data/three_sheet_bundle/three_sheet_four_block_negative_P.obj) / [STL](sandbox:/mnt/data/three_sheet_bundle/three_sheet_four_block_negative_P.stl)
- [Negative Q OBJ](sandbox:/mnt/data/three_sheet_bundle/three_sheet_four_block_negative_Q.obj) / [STL](sandbox:/mnt/data/three_sheet_bundle/three_sheet_four_block_negative_Q.stl)
