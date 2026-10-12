# figure-0141

AI research report · 2026-08-28 UTC

---

# Calm Lynx 78 — exact paired whole-packet continuation

## Determination

**No homogeneous convex polyhedral Gömböc was obtained.** The strongest endpoint is a finite 4,324-row uniform-density convex polyhedron at its own exact ordinary volume centroid with exhaustive directed class

```text
(S,U,H)=(47,69,114).
```

It is a rigorous nonwinner. The acceptance target remains a materialized finite own-centroid strict `(1,1,0)` body with complete H/V, maximal-face, vertex, true-edge/full-normal-cone, separation, verifier, and mesh evidence. :contentReference[oaicite:0]{index=0}

This continuation advances the preceding exact `(49,69,116)` endpoint through one actual half-turn-paired circuit, a transient paired `U-H` birth, a paired `S-H` cancellation, and an independent cancellation of the transported `U-H` packet. The exact class sequence is

```text
Q0 predecessor             (49,69,116)
P0 circuit-pre             (49,69,116)
P1 circuit-post            (49,69,116)
P2 transport-birth         (49,71,118)
P3 selected S-H cancelled  (47,71,116)
P4 transported U-H killed  (47,69,114).
```

All six cells have separately rebuilt actual hulls, separately Krawczyk-isolated three-moment roots, positive inactive gaps, and complete directed equilibrium audits.

## Exact deterministic source

Normative source:

```text
data/source_rows_modes.hex
SHA-256 f20d2685c4542fea648db79cb13ba28aa9033ad60a16dbd2d04462b4d4332a84
```

Predecessor SHA-256:

```text
560f8a08a41ad37258df5922d988f104427e04d7c5600993541caad843496d6b
```

Every hexadecimal binary64 token denotes its exact dyadic rational. Exactly six rows change, all 12,972 distributed-mode entries remain unchanged, and exact half-turn symmetry under `R=diag(1,-1,-1)` holds for the pairs

```text
(1521,1539), (1522,1540), (1557,1575).
```

The final rows are

```text
1521 (-0x1.cf5c9eda8dbf6p-2,-0x1.2940c396f1b0fp-1, 0x1.63786ee8061ebp-1)
1522 (-0x1.ce1371e5837d5p-2,-0x1.61fe050558c13p-1, 0x1.2d56245d73351p-1)
1539 (-0x1.cf5c9eda8dbf6p-2, 0x1.2940c396f1b0fp-1,-0x1.63786ee8061ebp-1)
1540 (-0x1.ce1371e5837d5p-2, 0x1.61fe050558c13p-1,-0x1.2d56245d73351p-1)
1557 (-0x1.b4f1352b89273p-2,-0x1.6530c54ed69e8p-1, 0x1.3240875b7ed86p-1)
1575 (-0x1.b4f1352b89273p-2, 0x1.6530c54ed69e8p-1,-0x1.3240875b7ed86p-1).
```

With unchanged modes `F_i`, the hard-centred family is

```text
u_i(t)=1+F_i·t,
P(t)={x:q_i^0·x≤u_i(t)}.
```

The three entries of `t` are dependent variables solving `Mx=My=Mz=0`. `src/generate_paired_packet_endpoint.py` reproduces all atlas sources and the endpoint byte-for-byte; the stored reproduction report passes.

## Actual topology-changing event

The synchronized circuits are

```text
north {1575,1610,1611,1646}
south {1557,1592,1593,1628}.
```

Their outward determinants are strictly positive at `P0` (`>3.29045e-8`) and strictly negative at `P1` (`<-1.92227e-8`). The actual paired `2↔2` exchange removes

```text
(1557,1592,1628) (1557,1593,1628)
(1575,1610,1646) (1575,1611,1646)
```

and adds

```text
(1557,1592,1593) (1592,1593,1628)
(1575,1610,1611) (1610,1611,1646).
```

No equilibrium label changes at the circuit itself.

In the rebuilt post-circuit cell, the paired unstable facets

```text
(1521,1557,1592), (1539,1575,1610)
```

and saddle edges

```text
(1521,1592), (1539,1610)
```

become strict, producing `(49,71,118)`. Continuing in that actual cell reverses

```text
E_(1557,1592), E_(1575,1610)
```

from positive to negative and removes saddle edges `(1557,1592),(1575,1610)`, producing `(47,71,116)`. A second independent boundary-direction control changes no incidence but makes the transported facet coefficients and saddle components strictly negative, producing `(47,69,114)` with no added equilibrium.

Net from predecessor to endpoint: stable rows `1557,1575` and saddles `(1557,1592),(1575,1610)` disappear; the transient `U-H` packet is born and then annihilated.

## Isolated ordinary-centroid root

The final first Krawczyk image is

```text
t0 ∈ [-0.0325966378064755431420857757545600330,
       -0.0325966378064755431420857757487139613]
t1 ∈ [1.01615590754802673056424891942176656e-13,
      1.01615590754802693554209178050612863e-13]
t2 ∈ [9.25086249393957389361170980411824959e-13,
      9.25086249393957395388849056686892619e-13].
```

The second image is strictly interior. The moment-Jacobian determinant is exactly enclosed by

```text
[41.0938466148790374571716899980033373,
 41.0938466148790374571716899980033373].
```

Volume and moments on the first image are

```text
V  ∈ [4.17990888046179390662825647573819766,
      4.17990888046179390662825656937761668]
Mx ∈ [-1.8385548779224351e-26, 1.8385645491198908e-26]
My ∈ [-1.8223503008133012e-26, 1.8226397020896466e-26]
Mz ∈ [-1.8645294701689032e-26, 1.8644277185683475e-26].
```

Strict Krawczyk inclusion proves one and only one zero, so the origin is exactly the body’s own uniform-volume centroid.

## Complete final audit

```text
H rows / maximal primal faces   4,324, all irredundant
polar facets / primal vertices  8,644
true edges                     12,966
surface triangles              17,284
class                      (47,69,114)
ambiguous primitives                0.
```

Directed margins:

```text
minimum positive stable:
  row 2939, witness 2904
  [1.9075875189109965385774526962651e-4,
   1.9075875189109965385774529633084e-4]
closest excluded stable: -1.74487911067e-8

minimum positive unstable coefficient:
  facet (1579,1614,1615), component 1
  [0.070556431431797070678050680878179,
   0.070556431431797070678050740831834]
closest excluded unstable: -2.77181426021e-7

minimum positive saddle component:
  edge (1579,1614)
  [0.042977755278138354196142486530207,
   0.042977755278138354196142569120203]
closest excluded saddle: -4.18483045086e-7.
```

The directed minimum inactive H–V numerator is

```text
>1.468921317915317e-9,
```

at inactive row `4316` against the vertex active on `(4280,4315,4281)`.

The completed equatorial gates remain strict:

```text
E_(2184,2149)<-4.36378e-5
E_(2166,2131)<-4.36378e-5
E_(2184,2219)<-3.16996e-3
E_(2166,2201)<-3.16996e-3
E_(1575,1610)<-2.69627e-6
E_(1557,1592)<-2.69627e-6.
```

Outer W1/W2/W3 remain crossed; the next outer deactivation remains un-crossed. Protected row `0` remains strict stable and the terminal facet `(4321,4322,4323)` remains strict unstable.

## Rigorous obstruction

The paired remote stable faces remain strict over the complete root box:

```text
(2939,2904):
[0.0001907587518910996538577452696265081,
 0.0001907587518910996538577452963308377]

(2921,2886):
[0.0001907587519408761065563709807452312,
 0.0001907587519408761065563710074495607].
```

Together with row `0`, they prove `S≥3` independently of the other 44 stable faces. Rows `1522,1540` also remain stable, each with minimum primitive about `3.75298804e-4`. The smallest residual local packet is

```text
U facets (1561,1596,1597), (1579,1614,1615)
H edges  (1561,1596),      (1579,1614).
```

Thus the two-coordinate event is a real cancellation, but global incidence transport survives.

## H/V, perturbation, verifier, and mesh

The fixed-source `L∞` root-box clearance is exactly

```text
2133581486885337858558173 /
766247770432944429179173513575154591809369561091801088
≈2.7844537618423661e-30.
```

It preserves the full `(47,69,114)` incidence/equilibrium cell. The complete interval H/V archive contains all rows, vertices, active triples, face cycles, surface triangles, and true-edge records; exact `Fraction` recomputation matches every exported endpoint bit-for-bit.

`src/verify_paired_packet_cleanroom.py` imports none of the construction or interval modules. It independently rebuilds all six hull cells, integrates volume/moments, reproduces every event by row labels, recomputes every face/vertex/full-edge cone and inactive gap, checks H/V arrays, and audits the meshes. Its report has `passed=true`.

The OBJ/STL has 8,644 vertices and 17,284 triangles, is watertight, has Euler number two, and midpoint signed volume `4.179908880461794`.

## Strongest continuation

The smallest new local architecture is a two-parameter half-turn packet replacement spanning stable rows `1522/1540`, excluded rows `1557/1575`, residual U facets `(1561,1596,1597)/(1579,1614,1615)`, and residual saddles `(1561,1596)/(1579,1614)`. One coordinate must move the remaining stable pair while a second independently retopologizes the U-H packet so no birth precedes cancellation. The three moment modes remain dependent hard equations.

The stronger global continuation should couple that local packet to remote stable rows `2921/2939` in one support-connected multi-sheet belt. A local cancellation alone cannot reach `(1,1,0)` while 44 other stable faces, 68 other unstable vertices, and 112 other saddles remain.

## Artifacts

- [Complete exact/directed archive](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner.zip)
- [Archive SHA-256](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner.zip.sha256)
- [Full handoff](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/RESEARCH_HANDOFF.md)
- [Machine-readable result](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/RESULT.json)
- [Exact source](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/data/source_rows_modes.hex)
- [Actual-cell atlas](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/certificates/path_cell_atlas.json)
- [Path/obstruction certificate](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/certificates/paired_packet_path_and_obstruction.json)
- [Krawczyk certificate](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/certificates/root3_interval_certificate.json)
- [Full directed audit](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/certificates/root_full_interval_audit.json)
- [Interval H/V archive](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/geometry/root_interval_hv.npz)
- [Maximal-face cycles](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/geometry/root_maximal_face_cycles.json)
- [True-edge ledger](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/geometry/root_true_edges.csv)
- [Independent verifier](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/src/verify_paired_packet_cleanroom.py)
- [OBJ](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/geometry/root_midpoint.obj)
- [STL](sandbox:/mnt/data/distributed_multi_relay_belt_paired_packet_nonwinner/geometry/root_midpoint.stl)

Archive SHA-256:

```text
056cb0c2519f13141d87e6efffb97679248f12a20e68b8b33a48a14ea80598d4
```
