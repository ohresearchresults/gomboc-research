# figure-0271

AI research report · 2026-09-03 UTC

---

# Keen Quartz 89 — continuation beyond exact `KQ89-DP2`

## Disposition

**EXACT NONWINNER. No literal homogeneous convex polyhedral Gömböc was obtained.**

The requested acceptance gate remains an expanded finite uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid, with strict `(S,U,H)=(1,1,0)`, complete exact H/V/incidence and full-normal-cone mechanics, an independent verifier, and matching OBJ/STL; a near-solution or unexpanded theorem is not sufficient. :contentReference[oaicite:0]{index=0}

The exact `KQ89-DP2` endpoint from the preceding turn remains valid and fully materialized, but I did not obtain an exact strict DP3 child that cancels its residual stable–saddle pair. Numerical DP3 experiments crossed additional local cells yet continued to relay the pair and were not exactified.

A later exact M42 construction from the same shared frontier materially supersedes DP2 as a mechanical platform, although it is a sibling continuation from the 68-active shared-volume parent rather than a literal child of the 73-vertex DP2 body. I recovered its complete archive and independently reran the core proof stack. It realizes a stronger internally linked twelve-support triangular-prismatic station with no adverse changed-edge carrier and contains the first exact no-birth `U–H` cancellation in the M42 lineage. It remains strict `(2,1,1)` because an independent closed stable basin and saddle survive. The durable journal records the exact result and its successor topology. :contentReference[oaicite:1]{index=1}

## 1. Status of the literal DP2 continuation

The exact DP2 source is

```text
supplied/active vertices = 73/73
(V,E,F)                  = (73,199,128)
complexity               = 398
(S,U,H)                  = (2,1,1)
protected stable         = [0,1,...,16]
protected unstable       = 8
extra stable             = [257,7200,6001]
extra saddle             = (1026,7205)
```

Its complete adverse stable component is carried by the three polar faces

```text
[257,6001,6004]
[257,7200,6001]
[6001,7200,7201]
```

and the two primal forcing edges

```text
(257,6001)
(6001,7200).
```

The right component consists of saddle `(1026,7205)` and its incident faces

```text
[228,7205,1026]
[1026,7205,6009].
```

DP2 already contains a genuine positive-volume internal tetrahedral link on `7203,7204,7205,7206`; thus another boundary page is not a new topology. Its exact package and the full `S≥2` chamber theorem remain available here:

- [Exact DP2 package](sandbox:/mnt/data/Keen_Quartz_89_M42_DP2_exact_NONWINNER.zip)
- [DP2 research handoff](sandbox:/mnt/data/Keen_Quartz_89_M42_DP2_exact_NONWINNER/RESEARCH_HANDOFF.md)
- [DP2 residual forcing theorem](sandbox:/mnt/data/Keen_Quartz_89_M42_DP2_exact_NONWINNER/residual_forcing_component_certificate.json)
- [DP2 complete external-arrow census](sandbox:/mnt/data/Keen_Quartz_89_M42_DP2_exact_NONWINNER/complete_external_arrow_census.json)
- [DP2 connected transition certificate](sandbox:/mnt/data/Keen_Quartz_89_M42_DP2_exact_NONWINNER/connected_transition_three_ball.json)

### New numerical work on DP2

The strongest newly tested two-cap placement inserted

```text
8000 = (-16.978943401472385,
         2.2425622040793125,
        -0.7260817896355052)

8001 = ( 10.701005714850105,
        -26.366905140411657,
         -0.5270813331832467).
```

A full-hull replay gave approximately

```text
(V,E,F) = (75,205,132)
(S,U,H) = (2,1,1)
protected-base margin ≈ 0.851303
U8 margin             ≈ 0.163055
extra stable          = [257,8000,6001]
extra-stable margin   ≈ 1.12e-4
sole saddle           = (1026,7205)
saddle margin         ≈ 1.98e-3
minimum topology separation ≈ 4.24e-6.
```

This is only floating-point discovery evidence. It is also an effectively serial pair of caps rather than the requested two-return-belt volume, so it was not promoted.

Further tiny stable-side caps appeared to remove the named stable face under a loose coplanarity tolerance, but exact-topology replay exposed a transferred face `[6001,8003,8000]`; the apparent improvement was therefore a verifier-tolerance artifact. Topology margins had fallen below approximately `5e-13`, so no candidate from that family was admissible.

Other completed discovery tests were:

```text
all 256 deletion subsets of
{257,6001,7200,7201,1026,7205,228,6009}:
    no (1,1,0) body

six-parameter affine/metric search:
    best score remained negative; representative class (3,3,4)

single cross-belt bridge points:
    broad points generated several new U/H features

fixed-incidence linearization:
    the stable face and its adjacent relay face have nearly opposite
    response rows, reproducing the exact transfer mechanism.
```

The numerical two-cap data are retained as [two_cap_candidate.npz](sandbox:/mnt/data/kq89_dp3_work/two_cap_candidate.npz). None of this is an exact exclusion of the full DP3 realization space.

## 2. Strongest exact M42 successor recovered

The recovered exact triangular-prismatic station removes active rows

```text
6001,6004,6007,6009
```

from the 96-supplied/68-active shared-volume parent and inserts twelve exact dyadic extreme vertices

```text
6300,6301,...,6311.
```

Its actual rebuilt hull is

```text
supplied rows            76
active vertices          69
inactive rows             7
true edges              187
maximal faces           120
Euler characteristic      2
complexity              374
(S,U,H)                (2,1,1)
```

The inactive rows are

```text
1001,1002,1003,1004,1014,6006,6008.
```

All 119 nonbase maximal faces are triangular; the remaining maximal face is the protected stable 17-gon `[0,...,16]`.

The exact equilibrium classification is

```text
stable maximal faces:
  [0,1,...,16]
  [258,259,6301]

unstable vertices:
  8

saddle true edges:
  (248,6310).
```

The old shared-volume pair `[257,258,6001]` and `(248,6009)` is literally absent because the relevant rows are removed. The older T37, row-54, active-pair and DP2 labels are likewise absent from this body.

### Exact mass data

The body has exact positive rational ordinary volume; its decimal value is

```text
1413.4189306560652.
```

The exact unshifted ordinary-volume centroid is approximately

```text
(-1.1542677372552443,
  2.6716095866695160,
 -0.21655499674295087).
```

The archive stores the complete rational numerator and denominator of the volume, all three exact first moments, the exact centroid, and the own-centred coordinates. Translation by the exact negative centroid gives translated first moments

```text
(0,0,0)
```

identically.

### Strict endpoint margins

The exact builder reports the following normalized decimal margins:

```text
minimum active nonincidence       3.869169282446657e-6
minimum inactive separation       3.990653834304637e-3
protected base stability           1.0726739492470592
extra stable stability             6.633133123441192e-3
minimum nonstable clearance        5.520874263666773e-3
protected U8 instability           1.681196268072070e-1
minimum nonunstable clearance      7.082620058262195e-4
extra saddle margin                1.920404474103255e-2
minimum nonsaddle clearance        4.613412385439099e-3.
```

These margins are substantially larger than the near-wall margins of the 67-vertex DP2 source.

## 3. Exact topology-changing three-ball

The twelve inserted vertices form an exact uniform rank-four oriented matroid. Exhaustive circuit enumeration gives

```text
rank                         4
affine circuits            792
regular tetrahedra          17
regular-cell volume ≈ 29.539193623967297.
```

The regular tetrahedralization has connected dual graph and no bridge interior triangle. It contains two edge-disjoint interior routes, rather than a single serial tip chain. One explicit active route is

```text
6301 – 6302 – 6305 – 6306 – 6309 – 6310.
```

The complete source/target face-lattice comparison produces an exact same-boundary disk exchange:

```text
removed maximal faces       53
inserted maximal faces      57
common boundary edges       35.
```

Both changed patches are connected disks on the same boundary, and the exchanged volume is strictly positive. The construction therefore supplies genuine finite thickness and internal communication.

## 4. Complete changed-star arrow result

Every newly inserted edge and every inherited edge whose incident star changes was audited. The exact census contains

```text
changed/star edges audited       103
edges incident with new rows      68
all-external-positive carriers     0.
```

This is stronger than DP2, where two nonprotected all-positive forcing edges survived. It proves that the remaining stable equilibrium is **not** forced by an overlooked changed-edge carrier. Row `6301` is instead a strict radial local minimum on its complete closed face star.

This materially changes the M42 diagnosis:

```text
DP2 obstruction:
  adverse internal edge component plus separated saddle timing

tri-prism obstruction:
  no adverse changed edge;
  a closed stable drainage basin remains disconnected from the
  protected-base basin at the boundary-flow level.
```

Thus external-arrow antibirth is necessary but not sufficient. A candidate must also provide a real descending drainage path from every nonprotected stable star into the protected stable basin.

## 5. First exact no-birth cancellation in the M42 lineage

The exact same-lattice affine chronology isolates a single degree-five normal-cone primitive root in the rational interval

```text
2297277102955/2764535482423
    < t* <
487148059722/586232324591,
```

with

```text
t* ≈ 0.8309812326740449.
```

Immediately before the root:

```text
vertex 6310 is an extra strict unstable equilibrium;
edge (1026,6310) is a strict saddle.
```

At the root, both degenerate through the same degree-five primitive. Immediately after the root:

```text
vertex 6310 is nonunstable;
edge (1026,6310) is nonsaddle;
all 370 other protected negative witnesses retain their signs;
no replacement equilibrium is born.
```

This is a genuine `U–H` Morse cancellation with correct death-before-birth chronology. It demonstrates that simultaneous no-birth cancellation is geometrically realizable in M42; the remaining problem is now specifically the independent `S–H` pair `[258,259,6301]` / `(248,6310)`.

The surviving right saddle uses incident faces

```text
[248,6309,6310]
[248,6310,1026]
```

and the adjacent `1026/6008` return channel. The stable face's shortest dual route to the protected base is

```text
[258,259,6301]
→ [69,259,258]
→ [69,72,259]
→ [1,72,69]
→ [0,72,1]
→ [0,...,16].
```

That route currently crosses a closed fan boundary rather than an open descending channel.

## 6. Positive exact chamber

The twelve inserted vertices supply 36 independent Cartesian coordinates. An outward-rational box of radius

```text
2^-36
```

in all 36 coordinates preserves:

- all supplied/active and inactive statuses;
- all 120 maximal faces and 187 true edges;
- every face equilibrium component;
- every full vertex normal-cone component;
- all four components of every true-edge cone;
- the protected base and U8;
- the strict class `(2,1,1)`.

This is an open endpoint, not a wall point.

## 7. Recovered exact package and verification status

The complete archive is available here:

- [Exact twelve-support triangular-prism archive](sandbox:/mnt/data/kq89_cw6300/M42_slot1_Clear_Willow_25_tri_prism_exact_complete.zip)
- [Endpoint README](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/README.md)
- [Exact endpoint certificate](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/certificate.json)
- [Exact input V-data](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/coordinates_exact.csv)
- [Exact own-centred V-data](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/coordinates_own_centered_exact.csv)
- [Exact supporting planes](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/face_planes_exact.json)
- [Maximal-face cycles](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/face_cycles.json)
- [True-edge incidence](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/true_edges.csv)
- [Complete face mechanics](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/faces_mechanics_exact.json)
- [Complete vertex mechanics](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/vertices_mechanics_exact.json)
- [Every true-edge four-component cone](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/edges_mechanics_exact.json)
- [Connected disk exchange](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/disk_exchange_certificate.json)
- [Exact rank-four oriented matroid and 17-tetrahedron cell](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/new_cell_oriented_matroid.json)
- [Complete changed-star arrow audit](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/external_arrow_audit.json)
- [Exact no-birth cancellation chronology](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/same_lattice_cancellation_chronology.json)
- [Exact 36-dimensional chamber](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/full_36d_box_certificate.json)
- [GMP all-triple verifier](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/verify_exact_hull_gmp.cpp)
- [Exact mass/mechanics verifier](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/verify_exact_mass_mechanics.py)
- [Watertight OBJ](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/body.obj)
- [Watertight STL](sandbox:/mnt/data/kq89_cw6300/tri/M42_slot1_Clear_Willow_25_tri_prism_exact_final/connected_tri_prism_endpoint/body.stl)

I invoked the archive's clean replay. Within the available execution interval, the following stages completed again from source:

```text
IMMUTABLE_MANIFEST_PASS
EXACT_TWELVE_SUPPORT_TRIANGULAR_STATION_BUILD_PASS
EXACT_CONNECTED_DISK_EXCHANGE_PASS
EXACT_TWELVE_VERTEX_ORIENTED_MATROID_REGULAR_3BALL_PASS
EXACT_COMPLETE_CHANGED_STAR_EXTERNAL_ARROW_AUDIT_PASS
EXACT_SAME_LATTICE_UH_CANCELLATION_WITHOUT_BIRTH_PASS.
```

The current replay transcript is [TRI_REPLAY_CURRENT.log](sandbox:/mnt/data/kq89_cw6300/TRI_REPLAY_CURRENT.log).

The replay process reached the runtime boundary before rerunning the final 36-dimensional interval, GMP all-triple, mass/mechanics and mesh stages in this session. Their previously produced verifier scripts and successful logs are present inside the immutable archive, but I do not represent the interrupted current invocation as a fresh end-to-end rerun.

## 8. Strongest conclusion

The exact triangular-prism endpoint proves three facts not available at DP2:

1. A substantial internally linked M42 cell can delete the old pair while leaving **zero** all-positive inserted or star-changed edge carriers.
2. A strict `U–H` pair can cancel through one exact higher-valence primitive with no replacement birth.
3. The remaining failure is a closed stable drainage basin, not moment rank, internal connectivity, or a hidden forcing edge.

It therefore supersedes further polishing of the DP2 forcing-edge chamber. It does not supersede the original compact M42 benchmark as a complexity record, and it is not a Gömböc.

## 9. First genuinely unclassified topology

The next topology should no longer be described merely as DP2 plus a second internal return edge. The exact evidence now calls for a **two-boundary annular/prismatic drainage three-ball**, denoted here by `KQ89-AD2`.

It must span the complete left and right components:

```text
left stable star:
  [258,259,6301]
  adjacent fan through 69,72 and the protected-base basin

right saddle star:
  edge (248,6310)
  faces [248,6309,6310] and [248,6310,1026]
  adjacent return through 1026/6008.
```

One full-hull event must satisfy all of the following:

```text
make at least one of {6301,258,259} nonextreme or reverse the
complete stable-star radial order;

make at least one of {6310,248,1026} nonextreme and replace both
incident faces of saddle (248,6310);

open an actual descending boundary route from the 6301 basin through
69/72 into the protected [0..16] basin;

retain an internally communicating second boundary component or
annular core, not merely an interior route whose ends remain closed;

keep every inserted and star-changed nonprotected edge free of
all-positive external arrows;

preserve [0..16] and U8;

reserve the three first moments as dependent equations while retaining
independent controls for left stable death, right saddle death, boundary
drainage, and replacement antibirth;

certify stable and saddle death before any replacement feature becomes
strict.
```

A robust implementation is expected to need roughly 14–16 connected new extreme vertices, arranged as two staggered triangular-prismatic belts joined through an annular core. A smaller construction may succeed if it simultaneously moves or deactivates old rows `258`, `248`, `1026`, or `69`; no minimality theorem is claimed.

The following are now repetitions rather than new tests:

```text
another one-boundary strip;
an isolated stable cap;
an inactive connecting arc;
a serial station chain;
same-lattice motion inside the certified endpoint chamber;
a purely internal corridor that does not open the closed boundary fan;
independent deletion of one left and one right row.
```

## Bottom line

No exact own-centred `(1,1,0)` body was reached. The literal DP3 construction sought from the 73-vertex DP2 body remains unrealized. The strongest exact reusable successor available on the M42 frontier is the recovered 69-vertex twelve-support triangular-prismatic station. It has exact mass closure, complete H/V/E and mechanics, a positive 36-dimensional chamber, a genuine connected regular 3-ball, no adverse changed-edge carrier, and an exact no-birth `U–H` cancellation. Its sole remaining defect is the independent strict `S–H` pair `[258,259,6301]` / `(248,6310)`. The first topology not represented by the completed atlas is the two-boundary annular drainage cell `KQ89-AD2` described above.
