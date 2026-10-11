# figure-0124

Historical AI scientific report · saved 2026-08-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Determination

No strict homogeneous convex polyhedral Gömböc was found. The acceptance gate remains a finite uniform-density convex polyhedron evaluated at its own exact volume centroid, with strict `(S,U,H)=(1,1,0)`, complete maximal-face/vertex/true-edge normal-cone audit, positive perturbation margin, independent verification, and OBJ/STL; near-solutions and artificial centres do not qualify. :contentReference[oaicite:0]{index=0}

The journal predecessor was the exact M42 transverse endpoint `(V,E,F,C)=(29,67,40,134)`, class `(4,3,5)`, with the external-positive terminal edge `(46,47)` forcing `U≥2` together with row `8`. :contentReference[oaicite:1]{index=1}

This continuation materializes an exact rational, perturbation-certified **post-relay body**. It genuinely deletes `(46,47)`, destroys the inherited remote stable/saddle witnesses, and joins the terminal, right, left, and northern sectors in one volumetric communicating cell. It remains a nonwinner: exact own-centroid class `(3,3,4)`. The first obstruction transfers to true edge `(47,53)`.

# Exact endpoint

All 60 supplied coordinates are literal terminating rationals on denominator `10^17`: [coordinates](sandbox:/mnt/data/m42_postrelay_bundle/m42_postrelay_points.txt). Active rows are

```text
0..16,28,29,32,33,42,43,44,45,46,47,48,49,51,52,53,57,58,59
```

and all other supplied rows are inactive. In particular `31,34,35,37,38,40` deactivate together. The exact actual hull is

```text
(V,E,F,C)=(35,85,52,170).
```

Complete irredundant data: [52 maximal-face cycles](sandbox:/mnt/data/m42_postrelay_bundle/m42_postrelay_faces.txt), [85 true edges](sandbox:/mnt/data/m42_postrelay_bundle/m42_postrelay_edges.txt), [primitive-integer H-representation](sandbox:/mnt/data/m42_postrelay_bundle/m42_postrelay_hrep.txt), and [full exact primitive ledger](sandbox:/mnt/data/m42_postrelay_bundle/m42_postrelay_certificate.json).

Exact volume:

```text
1015094330553206928275663743246920871468720056115879
----------------------------------------------------------------
500000000000000000000000000000000000000000000000000
```

Exact own centroid:

```text
cx=45637950067620359345146166042828227939634682323666744457461336874583
   /487245278665539325572318596758522018304985626935621920000000000000000

cy=-3166244016010142998792588328089460235297500686569919742366093459306329
   /2436226393327696627861592983792610091524928134678109600000000000000000

cz=-24951738817803041756748845448393461775293445247341518878695857820021
   /324830185777026217048212397839014678869990417957081280000000000000000
```

Numerically `c=(0.09366524841987788,-1.2996509785304882,-0.07681471707475705)`. Exact uncentred first moments are recorded in the certificate and full handoff. They are dependent hard quantities: each rebuilt certified hull is integrated first, `c=M/V` is formed exactly, and only then are mechanics evaluated on `p_i-c`; after exact translation all three first moments vanish identically.

# Exhaustive own-centroid mechanics

```text
(S,U,H)=(3,3,4)
hard target score=-0.0024842304636574645
```

Stable faces:

```text
17-gonal base                                  0.3898445309600076
[57,5,4]                                       0.002021519697303609
[8,59,51]                                      0.0015600910228340283
```

Unstable vertices:

```text
8                                               2.0501268960218741
47                                              0.0024842304636031372
53                                              0.0024842304636574645
```

Saddle true edges, using the complete two-normal cone:

```text
(4,57)                                          0.002484230458203146
(5,57)                                          0.0020390144742924586
(13,52)                                         0.0024842302852622869
(47,53)                                         0.0024842304636031377
```

Every other actual face, vertex, and true edge is strictly excluded. Closest excluded face/vertex/edge margins are `-6.951946449365779e-4`, `-9.924465751260629e-2`, and `-8.561209344200389e-4`. Minimum inactive boundary separation is `7.677672453409298e-4`.

# Topology change and footprint

The connected surgery complex is

```text
42,43,44,45,46,47,48,49,51,52,53,57,58,59.
```

It meets all four required sectors. Rows `(51,52,53,57)` have exact nonzero determinant

```text
958809882526630502896617617357510528161718289590040
```

and tetrahedron volume `0.15980164708777175`, so the cell is genuinely three-dimensional.

Old edge `(46,47)`, stable faces `[4,42,43]`, `[10,11,43]`, `[13,14,49]`, and saddles `(4,42)`, `(4,43)`, `(13,49)`, `(14,49)` are absent. Rows `46,47` remain active but nonadjacent.

The exact centroid projection remains strictly inside the intended 17-gon with in-face margin `0.3898445309600076`; the first failure is not a footprint crossing.

# Exact transferred obstruction

The new true edge is `(47,53)`. Every external directed support from either endpoint is positive. With `d=q53-q47`, centred integer vectors `X_i`, and `K=4T`:

```text
A=-X47·d
 =6013971996459967690356470250990438280132187070432333574650057288290061641781654475

B=X53·d
 =6013971996587030636391984532988190866382372184713738988613903034328553989732084901

A+B=K|d|^2
 =12027943993046998326748454783978629146514559255146072563263960322618615631513739376.
```

Both are positive and the identity is exact. Hence at least one endpoint remains unstable throughout the realized incidence/external-sign cell. Row `8` is independently unstable, so the cell has `U≥2`. Flipping only the mutual sign transfers the maximum.

All `256` deletion subhulls from rows `46,47,51,52,53,57,58,59` were rebuilt; none is `(1,1,0)`. A complete fixed-geometry reference-centre MILP gives optimum `-0.0024842304636312207`, so no centre makes this fixed polytope strict `(1,1,0)`.

# Perturbation and mesh certificates

A directed interval verifier certifies

```text
|delta x_ij|<=10^-11 on rows 42..59; rows 0..41 fixed.
```

Throughout the box the actual f-vector remains `(35,85,52)`, class remains `(3,3,4)`, `(46,47)` stays absent, and the `(47,53)` obstruction persists. Worst nonincident support interval upper bound is `-4.0697876240957756e-7`.

OBJ and STL each weld to 35 vertices and 66 triangles, are watertight, and reproduce the exact-body volume and centre of mass.

# Smallest new continuation

The smallest unexcluded operation is a finite-width `2×k` zipper or genuinely three-dimensional two-cell bridge acting simultaneously on

```text
terminal: 45,46,47,49,53
right:    4,5,42,43,44,57
left:     13,14,48,49,52,58
north:    8,9,43,51,59.
```

It must delete `(47,53)` or deactivate an endpoint, create two independent terminal witnesses, cross the right and left circuits in the same rebuilt event, allow obsolete rows in all four sectors to deactivate together, and eliminate three branch-depth/cross-lobe variables through the exact moment equations before scoring. Preserve the base projection and require inactive separation above `10^-5`.

# Artifacts

- [Complete exact bundle](sandbox:/mnt/data/m42_postrelay_bundle.zip)
- [Full research handoff](sandbox:/mnt/data/m42_postrelay_bundle/m42_postrelay_handoff.md)
- [Exact verifier](sandbox:/mnt/data/m42_postrelay_bundle/m42_postrelay_verifier.py)
- [Directed interval verifier](sandbox:/mnt/data/m42_postrelay_bundle/m42_postrelay_box_verifier.py)
- [Mesh verifier](sandbox:/mnt/data/m42_postrelay_bundle/m42_postrelay_mesh_verifier.py)
- [Reproduction source](sandbox:/mnt/data/m42_postrelay_bundle/reproduce_postrelay.py)
- [256-subset scan](sandbox:/mnt/data/m42_postrelay_bundle/postrelay_subset_scan.json)
- [OBJ](sandbox:/mnt/data/m42_postrelay_bundle/m42_postrelay.obj)
- [STL](sandbox:/mnt/data/m42_postrelay_bundle/m42_postrelay.stl)
- [Exact verification transcript](sandbox:/mnt/data/m42_postrelay_bundle/exact_verification_transcript.txt)
- [Interval transcript](sandbox:/mnt/data/m42_postrelay_bundle/box_verification_transcript.txt)
- [Mesh transcript](sandbox:/mnt/data/m42_postrelay_bundle/mesh_verification_transcript.txt)

Bundle SHA-256:

```text
48dc42b56a6acfa15b70e4aaf0b1b8317f573031370a5a3ac502c0f039426d90
```

# Uncertainty

No Gömböc claim is made. The exact theorem excludes the complete realized `(47,53)` incidence/external-sign cell, not every larger branched or annular surgery. The deletion scan, fixed-centre MILP, and metric search are finite screens, not global impossibility proofs.
