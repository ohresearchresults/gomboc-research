# figure-0255

Historical AI scientific report · saved 2026-09-03 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: unreviewed-encoded-blocks-omitted.

---

# Clear Willow 25 — exact twelve-support internally linked M42 continuation

## Final disposition

**EXACT NONWINNER.** No finite homogeneous convex polyhedral Gömböc was obtained.

The previous handoff had only a numerical eight-support split strip. I first exactified that strip, then advanced it to a stronger exact twelve-support internally linked regular 3-ball. The promoted body deletes both residual carriers from the supplied 96-row endpoint, preserves the intended stable 17-gon and unstable vertex `8`, has a full 36-dimensional exact shape chamber, and performs one genuine unstable–saddle Morse cancellation without any replacement birth. It nevertheless retains an independent strict stable–saddle pair, so its exact own-centred class is `(S,U,H)=(2,1,1)`, not `(1,1,0)`.

The supplied journal identified the first nonrepeating frontier as a two-boundary or internally linked prismatic/cubical 3-ball changing both complete residual stars, with active shared volume and independent antibirth timing controls. :contentReference[oaicite:0]{index=0} The construction below realizes the internally linked positive-volume part of that frontier exactly and localizes the remaining boundary obstruction.

**Complete immutable archive:** [M42_slot1_Clear_Willow_25_tri_prism_exact_complete.zip](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_complete.zip)  
**Archive SHA-256:** `95d0e03d0d6ee45f5750be64847aee113c40a34f4af4a97b02582a5dd1ec3ef7`  
**Readable report:** [README.md](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/README.md)  
**Machine summary:** [result_summary.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/result_summary.json)  
**Immutable manifest:** [MANIFEST.sha256](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/MANIFEST.sha256)  
**One-command replay:** [REPLAY.sh](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/REPLAY.sh)  
**Clean-room transcript:** [CLEANROOM_VERIFY.log](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/CLEANROOM_VERIFY.log)

A fresh post-packaging replay reproduced every exact verifier marker and the manifest. The archive checksum file also passes independently.

## 1. Exact deterministic source and topology change

The source parent is the exact 96-supplied-row, 68-active-vertex M42 descendant. Dropping its already inactive rows does not change its convex body. The four active station rows

```text
6001, 6004, 6007, 6009
```

are then removed, and twelve exact dyadic rows

```text
6300, 6301, 6302, 6303, 6304, 6305,
6306, 6307, 6308, 6309, 6310, 6311
```

are supplied. All twelve are actual extreme vertices. The compact source is [exact_finite_source.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/exact_finite_source.json), SHA-256 `bf0cbe2bf7de044dee50d12248fbada564783de60d5d6108971714a52db3a137`. The deterministic builder is [build_exact_tri_prism_endpoint.py](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/build_exact_tri_prism_endpoint.py).

Old coordinates are copied as exact inherited rationals. Each new coordinate is interpreted as the exact dyadic rational represented by its recorded binary64 discovery value. Floating hull code is used only to propose face cycles; every supporting sign, mass identity, centroid coordinate, and equilibrium primitive is recomputed over exact rational arithmetic.

The endpoint supplies 76 rows. The complete full-hull reconstruction finds seven strictly inactive rows,

```text
1001, 1002, 1003, 1004, 1014, 6006, 6008,
```

and the irredundant actual hull

```text
active vertices   69
true edges        187
maximal faces     120
Euler             69 - 187 + 120 = 2
complexity        374
face sizes        119 triangles and one 17-gon.
```

The prior residual stable `[257,258,6001]` is literally absent because `6001` is not supplied. The prior residual saddle `(248,6009)` is literally absent because `6009` is not supplied. These deaths were established from the rebuilt all-supplied hull, not from a transported local ledger.

Exact coordinates and complete incidence:

- [supplied coordinates](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/coordinates_exact.csv)
- [exact own-centred coordinates](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/coordinates_own_centered_exact.csv)
- [single common integer lattice](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/coordinates_common_lattice.csv)
- [all 120 maximal-face cycles](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/face_cycles.json), SHA-256 `99bbbf5d0005c7a48bd863d4696857880d5f23451f9a4bb2986b562c6a8aec1e`
- [exact supporting planes](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/face_planes_exact.json)
- [all 187 true edges](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/true_edges.csv), SHA-256 `ce9630bb9283ba8d890f263a16c165524c466d7d73eaecb9bfe97f06d49f356d`
- [complete endpoint certificate](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/certificate.json), SHA-256 `d198716852b24b0e99b49d5ddbb97e0be99ca000f20f6d7110e5528a5d8fd93c`

The minimum normalized active-face/nonincident-row support separation is `3.869169282446657e-6`; the minimum normalized inactive-row separation is `0.003990653834304637`.

## 2. Exact ordinary volume, centroid, and first moments

The exact ordinary volume is

```text
2855932415518460323048909515887211607962459406282116256121304648213332541803997432470172010135590084286708217558753504852636594023
/
2020584522801619294242937510149060964228824690360543814267060058281410351476639869723213824000000000000000000000000000000000000
```

or approximately `1413.4189306560652`.

The exact uncentred centroid is recorded as three rational fractions in `certificate.json`; its decimal value is

```text
(-1.1542677372552443,
  2.6716095866695160,
 -0.21655499674295087).
```

Exact signed-tetrahedron integration reconstructs the uncentred first moments. Translation uses the exact identity

```text
M(P + tau) = M(P) + V tau.
```

Since `V>0`, `tau=-C` is the unique centring translation. Direct exact reintegration of the translated body gives

```text
Mx = 0/1
My = 0/1
Mz = 0/1.
```

No auxiliary mechanical centre is used.

## 3. Exhaustive exact own-centroid equilibrium audit

The complete exact classification is

```text
(S,U,H) = (2,1,1).
```

The strict features and normalized margins are

```text
stable target  [0,1,...,16]      1.0726739492470592
stable extra   [258,259,6301]    0.006633133123441192
all other faces excluded         0.005520874263666773

unstable target vertex 8         0.1681196268072070
all other vertices excluded      0.0007082620058262195

saddle edge (248,6310)           0.01920404474103255
all other true edges excluded    0.004613412385439099.
```

Every maximal face is tested with all of its boundary inequalities; every active vertex is tested against its complete incident-edge cone; every true edge is tested with all four components `(t,1-t,beta1,beta2)` of its full normal cone.

Complete exact ledgers:

- [face mechanics](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/faces_mechanics_exact.json)
- [vertex mechanics](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/vertices_mechanics_exact.json)
- [four-component true-edge mechanics](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/edges_mechanics_exact.json)

Thus the endpoint is unambiguously a nonwinner. Its replacement packet is

```text
extra stable  [258,259,6301]
sole saddle   (248,6310),
```

while the protected 17-gon and protected unstable vertex `8` remain strict.

## 4. Connected same-boundary disk exchange

The source and endpoint share 63 maximal faces. Their noncommon parts are connected combinatorial disks with one identical 35-edge boundary:

```text
removed parent disk    (V,E,F) = (46,98,53), Euler 1
inserted endpoint disk  (V,E,F) = (47,103,57), Euler 1.
```

The common boundary cycle is

```text
[230,231,232,233,234,235,236,237,238,239,240,241,242,243,
 244,245,246,264,263,262,261,260,259,258,257,256,255,254,
 253,252,251,250,249,248,1026].
```

Both route rows `228` and `1026` remain active. The full certificate, including the removed and inserted faces, shared boundary, carrier deaths, and connectivity checks, is [disk_exchange_certificate.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/disk_exchange_certificate.json).

## 5. Exact internally linked positive-volume regular 3-ball

Rows `6300..6311` form a uniform affine oriented matroid of rank four. The exact certificate [new_cell_oriented_matroid.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/new_cell_oriented_matroid.json), SHA-256 `44716debc448eec49acef99be2cbf99d57ddcd640a3bdd5fdaf5735c84656571`, contains

```text
chirotope bases                    495
minimal five-point circuits        792
convex-hull boundary triangles      20
regular tetrahedra                  17
interior triangles                  24
exact cell volume
  674555935107230786794543598426944385254750221355
  / 22835963083295358096932575511191922182123945984
cell volume decimal                 29.539193623967297.
```

Squared-norm lifting gives an exact regular tetrahedralization. Its tetrahedron dual graph is connected, and no single interior triangle is a bridge. This is a genuine internally linked 3-ball, stronger than a ribbon, inactive arc, leaf buttress, single shared interface, or serial stellar page.

All twelve inserted rows are extreme. In the actual body they have 21 mutual true edges. Two edge-disjoint left-to-right routes are

```text
6301-6302-6305-6306-6309-6311-6310
6301-6303-6304-6308-6309-6310.
```

The nominal station triangles are

```text
[6300,6301,6302]
[6303,6304,6305]
[6306,6307,6308]
[6309,6310,6311].
```

The cell therefore realizes finite active thickness and independent internal routes in the complete actual hull.

## 6. Complete external-arrow audit

[external_arrow_audit.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/external_arrow_audit.json) audits every true edge that is new, removed, star-changed, or incident to a new row:

```text
audited changed/star edges       103
edges incident to new rows        68
all-positive external carriers     0.
```

For every edge `(i,j)`, the exact identity

```text
A(i->j) + A(j->i) = ||Xi-Xj||^2 > 0
```

is checked, and at least one nonpositive external witness prevents the exposed all-positive-arrow unstable-carrier mechanism on every changed edge. The final failure is therefore not a hidden terminal positive-arrow triangle or edge. It is the independently surviving stable-face and saddle-cone geometry.

## 7. Positive full-dimensional perturbation chamber

[verify_full_36d_box.py](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/verify_full_36d_box.py) proves with exact rational interval arithmetic that all 36 uncentred coordinates of rows `6300..6311` vary independently by

```text
±2^-36 = ±1/68719476736.
```

For every point in this Cartesian box:

```text
the same 76 supplied rows have the same actual hull (69,187,120);
all twelve new rows remain active;
volume remains positive;
exact centroid removal gives zero first moments;
the class remains (2,1,1);
the stable faces remain [0..16] and [258,259,6301];
the unstable vertex remains 8;
the saddle remains (248,6310).
```

The exact interval certificate is [full_36d_box_certificate.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/full_36d_box_certificate.json), SHA-256 `0a5118dadff9a4cfaa9ced29d98283df016f7d96483f95768425b5aefc194eea`. Its smallest raw certified lower bounds include `1.1364e-5` for facet support, `2.21098e-4` for inactive support, `0.00768186` for nonstable witnesses, and `0.004613406` for nonsaddle witnesses.

This is an open 36-dimensional shape chamber, not a wall or isolated numerical point.

## 8. Exact death-before-birth result: one real U–H cancellation

The endpoint is the far end of an exact affine segment whose complete actual face lattice stays `(69,187,120)` for every `t in [0,1]`. The chronology builder certifies 8,746 nonincident support-sign polynomials by recursive exact Bernstein subdivision; 14 intended coplanarity polynomials vanish identically. Every irrelevant equilibrium candidate receives a fixed exact negative witness.

At `t=4/5` the exact class is `(2,2,2)`:

```text
stable    [0..16], [258,259,6301]
unstable  8, 6310
saddles   (248,6310), (1026,6310).
```

At `t=17/20` the exact class is `(2,1,1)`:

```text
stable    [0..16], [258,259,6301]
unstable  8
saddle    (248,6310).
```

The external arrow from `6310` toward `1026` is identically the `1-t` component of edge `(1026,6310)`. Its exact degree-five numerator has exactly one root in the open unit interval, isolated by

```text
2297277102955/2764535482423
  < t* <
487148059722/586232324591,
```

with exact interval width

```text
1/1620660062275136911163993
```

and midpoint approximately `0.8309812326740449`.

Before `t*`, vertex `6310` is unstable and `(1026,6310)` is a saddle. At `t*`, both become degenerate through the same primitive. After `t*`, both are excluded. No other face, vertex, or edge becomes an equilibrium anywhere on the segment. This is a literal exact unstable–saddle cancellation without replacement birth and without a hull change.

The complete certificate is [same_lattice_cancellation_chronology.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/same_lattice_cancellation_chronology.json), SHA-256 `98e2fd7c89c72852925da9f84b4b8983daba2f38c160d2d82c71b5335f3fd9b5`.

The requested final cancellation nevertheless fails because the independent pair

```text
stable [258,259,6301] / saddle (248,6310)
```

remains strict throughout the complete certified segment.

## 9. Exact surviving forcing component

At the exact own centroid, row `6301` is a strict radial local minimum on its complete true-edge star. Its neighbours are

```text
257, 258, 259, 260, 261, 262, 263, 6300, 6302, 6303,
```

and every exact squared-radius difference

```text
||X_neighbor||^2 - ||X_6301||^2
```

is positive. The closest new-row gaps are approximately

```text
6300:   7.481930060460212
6302:  11.250952619499774
6303: 195.71131023664768.
```

Thus every strict realization in the certified 36-dimensional chamber retaining this full star has a competing boundary minimum. The stable triangle `[258,259,6301]` is the corresponding strict face equilibrium.

The shortest dual-face route from that stable triangle to the protected base passes through

```text
[258,259,6301]
[69,259,258]
[69,72,259]
[1,72,69]
[0,72,1]
[0,1,...,16].
```

The internally linked 3-ball connects the unwanted left and right stars, but it does not open an active descending boundary interface through this strip into the target-base basin. On the right, `(248,6310)` remains a strict saddle while the adjacent transfer channel through `(1026,6310)` and return row `6008` remains available.

This is the exact scoped obstruction:

- the endpoint and every point in its `2^-36` 36-coordinate box retain the closed radial fan and the final pair;
- the complete displayed same-lattice segment cancels one U–H pair but retains the final S–H pair;
- this does **not** prove that every realization of the abstract twelve-point oriented matroid is impossible.

## 10. Independent clean-room reconstruction and watertight meshes

The replay suite independently produces these terminal markers:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


The GMP verifier [verify_exact_hull_gmp.cpp](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/verify_exact_hull_gmp.cpp) enumerates all `C(76,3)=70,300` triples and performs 1,218,350 exact support-sign checks, recovering 120 maximal faces and 187 true edges.

The independent rational verifier [verify_exact_mass_mechanics.py](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/verify_exact_mass_mechanics.py) reconstructs the complete incidence, exact volume, exact centroid, zero centred moments, and every face/vertex/four-component edge-cone decision.

Meshes and verifier:

- [watertight OBJ](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/body.obj), SHA-256 `39011b2ced584d71ee9f488aa9547a26c62ee770c2ae3d2db21ce22c3970abba`
- [watertight STL](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/body.stl), SHA-256 `36b79d9f71aa784511b243233e1549a6f1f4ee8d9df2557d684a21dd63914135`
- [mesh verifier](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/verify_mesh.py)

The OBJ has 69 vertices, 134 triangles, 201 triangulated edges, Euler characteristic two, and every mesh edge has multiplicity two. Its reconstructed volume is `1413.4189306560654` and its centroid norm is about `3.02e-15`. The independent float32 STL has identical watertight combinatorics; its separately reported mass drift is the expected float32 export effect.

## 11. Intermediate exactification and empirical scope

The prior numerical eight-support split strip was also exactified completely. Its exact archive is [M42_slot1_Clear_Willow_25_split_exact_complete.zip](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_split_exact_complete.zip), SHA-256 `e830c4c3fecdd0f2656138ac2c57271094e2507eb7e8c5c62f53b4e80b9568ce`. It has 72 supplied rows, actual `(V,E,F)=(65,175,112)`, strict `(2,1,1)`, a positive-volume rank-four eight-row cell, a 24-coordinate box of radius `2^-26`, exact external-arrow and visibility-Gordan audits, and matching meshes. The twelve-support object supersedes it because it has two edge-disjoint internal routes, no bridge interior triangle, 36 independent shape coordinates, and an exact no-birth U–H cancellation.

Finite floating screens included in the final archive are explicitly empirical:

```text
aggregate distinct candidates rebuilt            2,447
valid complete hulls                              2,446
preserving protected base and U8                  2,231
strict (1,1,0)                                      0

local deletion subsets of size <=4 touching
both final carrier sets                           1,736
strict (1,1,0)                                      0.
```

These screens do not constitute continuum impossibility proofs. Exact claims are limited to the materialized endpoint, its complete incidence and mechanics, the regular 3-ball, the external-arrow ledger, the `2^-36` box, the exact affine chronology, and the radial-fan certificate.

## 12. Smallest genuinely nonrepeating successor

The twelve-support cell has already removed the previously cited defects: it is positive-volume, all new supports are extreme, it contains two edge-disjoint internal routes, its regular tetrahedron dual graph is not separated by one interior triangle, no changed edge has an all-positive external-arrow signature, and one Morse pair cancels without birth. The remaining obstruction is at the **boundary interfaces**, not in the internal linkage.

The first unclassified successor is a two-boundary annular/prismatic 3-ball with a second active drainage interface, robustly requiring about 14–16 new extreme supports or an equivalent event with coordinated old-row motion. In one full-hull operation it must replace

```text
left stable carrier: [258,259,6301]
left closed star:    neighbours 257..263,6300,6302,6303
left dual strip:     [69,259,258] -> [69,72,259]
                     -> [1,72,69] -> [0,72,1]
right saddle star:   [248,6309,6310], [248,6310,1026]
right return route:  the adjacent 1026/6008 channel.
```

At least one of `{6301,258,259}` and at least one of `{6310,248,1026}` must become nonextreme in the same connected event. The inserted active graph must include a genuinely descending route from the left page into the protected-base basin—not merely another route between the two unwanted stars. After solving the three exact ordinary-moment equations, at least three independent controls should remain for

```text
1. left stable death;
2. right saddle death;
3. external-arrow/antibirth timing at the drainage interface.
```

Another single cut, isolated cap, serial station, one-boundary strip, inactive arc, or same-lattice motion repeats an exact or empirically exhausted mechanism.

## Final conclusion

**EXACT INTERNALLY LINKED NONWINNER.** The strict own-centred `(1,1,0)` target was not reached. The strongest promoted object is the exact rational/dyadic 76-supplied-row body with actual `(V,E,F)=(69,187,120)` and strict `(2,1,1)`. It realizes the first internally linked positive-volume M42 continuation, deletes both inherited carriers, supplies a complete all-row incidence and equilibrium audit, retains a full 36-dimensional open chamber, eliminates every changed-edge all-positive-arrow carrier, and performs one exact U–H cancellation without replacement birth. The final S–H pair survives because `6301` remains a closed radial local minimum and `(248,6310)` remains a strict independent saddle. The two-boundary drainage 3-ball above is the smallest genuinely nonrepeating continuation.
