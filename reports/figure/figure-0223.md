# figure-0223

AI research report · 2026-09-02 UTC

---

# Keen Quartz 89 — exact M42 connected-route continuation

## Verdict

**Exact nonwinner. No homogeneous convex polyhedral Gömböc was constructed.**

The requested acceptance gate remains a finite, uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid, with strict `(S,U,H)=(1,1,0)`, complete exact or directed incidence and mechanics, a nonzero perturbation neighbourhood, independent reconstruction, and matching meshes. :contentReference[oaicite:0]{index=0} This continuation does not meet that gate and makes no completion claim.

The supplied journal ended with the numerical two-plane-plus-two-support body, provisional `(V,E,F)=(91,203,114)`, strict `(2,1,1)`, and the explicit requirement to span the complete transferred stable star, saddle/cap star, and connector route in a connected finite-thickness cell. :contentReference[oaicite:1]{index=1} I rebuilt that frontier from the exact M42 data, materialized an exact rational post-route body, audited its actual face lattice rather than preserving the provisional count, certified a connected positive-volume route three-ball and two real circuit flips, and then proved two new exact lower bounds on the next star-page topology.

The strongest exact post-route endpoint is:

```text
(V,E,F) = (91,253,164)
complexity = 506
Euler characteristic = 2
(S,U,H) = (2,1,1)
all 91 supplied vertices active
```

It preserves the intended stable base `[0,1,...,16]` and unique unstable vertex `8`; old vertices `224,229`, old stable triangle `[198,224,258]`, and old saddle edge `(229,247)` are strictly absent. The residual pair is now the stable triangle `[198,3000,1025]` and saddle edge `(1027,3001)`. Thus the old component is genuinely deleted, but the Euler-neutral pair is relayed rather than annihilated.

## Exact endpoint and ordinary mass centring

The exact ordinary volume is

```text
52419678057008551886010339718603739997396198491763807914496978287
--------------------------------------------------------------------
49909284903188266044158314500000000000000000000000000000000000
```

which is approximately `1050.2991208687888`.

The uncentred exact centroid is

```text
x = -377501032046963539237421337680560725313623403246403107916823686781314239627541
    /419357424456068415088082717748829919979169587934110463315975826296000000000000

y = 156708573213834589985239853688515824957703331538814516955529381652643748937
    /65524597571260689857512924648254674996745248114704759893121222858750000000

z = -1070500615187637472491525370398071340610369282726049091277265251978835063343926677375823825694093181321
    /6976609724481723033093849137810973586348956618546330753534124993128134610349672049325379364000000000000
```

Translation by its exact negative gives the supplied centred V-data. A fresh oriented-boundary tetrahedral sum over all 164 maximal faces and 178 boundary triangles returns centred first moments exactly `(0,0,0)`.

The literal data and mass certificate are:

- [Exact input V-data](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/vertices_input_exact.csv)
- [Exact centred V-data](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/vertices_centered_exact.csv)
- [Complete irredundant H-data](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/H_irredundant.csv)
- [Exact volume and first-moment certificate](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/mass_centroid_certificate.json)

## Complete actual incidence and exhaustive equilibrium classification

Independent exhaustive supporting-triple enumeration finds 843 supporting triples, grouped into exactly 164 maximal faces. Their boundary incidence gives 253 true edges and a connected closed sphere with `91-253+164=2`. Every supplied row is active; there is no hidden inactive input.

The strict equilibrium ledger at the exact own centroid is:

```text
stable faces:
  [0,1,...,16]       margin 8.863176490427573e-1
  [198,3000,1025]    margin 1.0029434446065215e-7

unstable vertices:
  8                   margin 1.7161533683848745e-1

saddle true edges:
  (1027,3001)         margin 1.1536375626037519e-7
```

Global exclusion and topology margins are strictly positive:

```text
minimum nonstable exclusion       2.8307113006033646e-9
minimum nonunstable exclusion     4.5988594592784010e-9
minimum nonsaddle exclusion       6.2323431101063770e-8
minimum active nonincidence       8.5868878290510730e-9
```

Every true edge is audited through all four normal-cone components—segment parameters `t,1-t` and incident-normal coefficients `beta1,beta2`—rather than through a single edge label.

Incidence and mechanics files:

- [Maximal-face cycles](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/face_cycles.json)
- [True-edge list](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/true_edges.csv)
- [Complete face normal-cone ledger](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/faces_full_cones.json)
- [Complete vertex normal-cone ledger](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/vertices_full_cones.csv)
- [Every true edge and all four components](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/true_edges_full_cones.csv)
- [Principal exact certificate](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/certificate.json)

## Complete eight-sheet anti-transfer ledger

All four inherited stable alternatives and all four inherited saddle alternatives were checked, not only the currently positive labels.

Stable-side sheets:

```text
[1000,1025,3000]  actual maximal face, decision -3.564994179470045e-4
[198,3000,258]    not supporting in the actual hull
[258,3000,1025]   not supporting in the actual hull
[198,1000,3000]   actual maximal face, decision -2.8307113006033646e-9
```

The replacement stable relay is the distinct actual face

```text
[198,3000,1025]   decision +1.0029434446065215e-7.
```

Saddle-side sheets, each a true edge with all four exact components recorded:

```text
(1027,3001)  +1.1536375626037519e-7   saddle
(1028,3001)  -6.2323431101063770e-8   excluded
(1029,3001)  -2.0600458708839534e-1   excluded
(1026,1028)  -7.6582412605279880e-4   excluded
```

The complete exact numerators, denominators, support status, incident faces, and normal-cone components are in [the eight-sheet ledger](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/eight_sheet_anti_transfer_ledger.json).

## Genuine topology change and connected finite-thickness route volume

Two actual regular-subdivision `2↔2` walls are crossed. The source and final exact four-point determinants have opposite nonzero signs for circuits

```text
{1001,1002,1004,1014}
{251,252,1018,1019}.
```

The face changes are

```text
removed:
  [251,252,1018]
  [252,1018,1019]
  [1001,1002,1004]
  [1001,1004,1014]

added:
  [251,252,1019]
  [251,1018,1019]
  [1001,1002,1014]
  [1002,1004,1014]
```

and the true-edge changes are

```text
removed: (252,1018), (1001,1004)
added:   (251,1019), (1002,1014).
```

These flips lie in one connected route disk spanning the stable star, saddle/cap star, and connector route. The exact route disk has `(V,E,F)=(34,66,33)`, Euler characteristic one, one 33-edge boundary component, and a connected dual. Coning its 33 boundary triangles to the exact own centroid produces 33 strictly positive tetrahedra:

```text
minimum tetrahedron volume ≈ 1.6660268902832887e-4
total route-three-ball volume ≈ 2.7652688590353375e2.
```

This is a genuine positive-thickness three-ball covering

```text
stable star:     {198,258,1000,1025,3000}
saddle/cap star: {1026,1027,1028,1029,247,228,3001}
connector route: 258-54-69-228-1026-1028.
```

The exact incidence change and route-cell proof are in:

- [Regular-subdivision atlas](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/regular_subdivision_atlas.json)
- [Connected route-three-ball certificate](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/connected_route_cell_certificate.json)

The decisive negative finding is that this connected volume contains two adjacent flips, but not one simultaneous stable–saddle annihilation event: the residual pair survives on `[198,3000,1025]` and `(1027,3001)`.

## Nonzero exact perturbation neighbourhood

A six-dimensional symmetric affine family is certified on the exact box

```text
|control_i| <= 2^-80
```

with exact centroid preservation. Throughout the whole box, incidence, active rows, maximal faces, true edges, stable/unstable/saddle labels, and strict exclusion witnesses remain unchanged. The interval proof includes positive lower bounds for every active component and one negative witness for every inactive feature; its smallest edge-normal Gram determinant lower bound is about `2.511991531996357e-19`.

- [Perturbation certificate](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/perturbation_certificate.json)
- [Independent exact interval verifier](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/verify_interval.py)

## Attempts made to break the residual pair

The linked-support deletion square was rebuilt exactly. Full, drop-`3000`, drop-`3001`, and drop-both cells are all strict `(2,1,1)`. The stable and saddle witnesses migrate, proving that independent support deletion is another relay rather than cancellation. See [the exact four-cell deactivation atlas](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/support_deactivation_atlas.json).

Discovery searches then tested 1,105 stored candidates, of which 1,096 rebuilt as valid full hulls; none was `(1,1,0)`. A separate 6,000-case connected-page search produced 5,599 `(2,1,1)` and 401 `(3,1,2)` bodies, again with no winner. These are empirical exclusions only and are not promoted to theorem status.

A naive materialization of the later relaxed T37-R6 witnesses—deleting the six released rows and simply inserting the two exact page apices—retains only 53 of 87 supplied points, gives `(53,153,102)` and `(2,5,5)`, and destroys both the protected base and `U8`. It is explicitly rejected as a candidate.

## New exact theorem 1: frozen-boundary cyclic star pages require at least seven apices

For every one of the 33 cyclic start edges of the exact route boundary, I solved the longest feasible frozen-boundary apex fan. Each maximal arc has a strict rational apex witness; the first longer arc has an exact positive Farkas contradiction including all old vertices and external maximal-face halfspaces.

The exact maximum feasible edge counts are

```text
3,2,7,6,5,4,3,2,5,4,3,2,6,5,4,3,3,2,6,5,4,3,6,5,4,3,2,6,5,4,3,2,4.
```

Independent exact dynamic programming proves the minimum cyclic cover is seven pages. One minimum cover is

```text
(start edge index, edge count):
(0,2), (2,6), (8,4), (12,6), (18,4), (22,5), (27,6).
```

Therefore no frozen-boundary cyclic star-page construction with six or fewer apices can span the complete route. This theorem does not cover moving/deactivating boundary rows, changing page diagonals, or non-star prismatic/octahedral pages.

- [Exact 33-start page-cover atlas](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/frozen_boundary_star_page_cover_exact.json)
- [Independent exact page-cover verifier](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/verify_frozen_boundary_star_page_cover_exact.py)

## New exact theorem 2: the fixed T37 pages need at least six old-row releases

For the fixed two-new-support central-triangle assignment `T37`, I reconstructed the complete necessary halfspace systems for the stable and connector pages. Releasing an old row is modelled permissively by deleting every page inequality involving it, allowing arbitrary motion or deactivation. Constraint generation produced 197 exact four-halfspace Farkas alternatives—77 stable-page and 120 connector-page certificates.

Their nonprotected-row support hypergraph has exact transversal number six. Consequently:

```text
No choice of five nonprotected old rows can release both fixed T37 pages.
```

One exact six-row transversal is

```text
{69,198,251,1001,1004,1019}.
```

After deleting every necessary page inequality involving those rows, both page systems have strict exact rational witnesses. Their minimum normalized remaining slacks are approximately

```text
stable page:    0.001589389214941763
connector page: 0.009245115023509028.
```

An independent branch-and-bound verifier finds a different six-row transversal `{69,198,228,231,257,258}` and proves that no five-row transversal exists. This is a necessary-support relaxation, not an actual convex-hull realization; the naive realization test fails as described above.

- [Exact 197-certificate actuator theorem](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/minimum_old_row_actuator_certificate.json)
- [Independent exact actuator/hitting verifier](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/verify_minimum_old_row_actuator_certificate.py)
- [Frozen T37 page Farkas certificates](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/t37_frozen_boundary_farkas.json)
- [Independent frozen-page verifier](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/verify_t37_frozen_boundary_farkas.py)

## First sharply delimited nonrepeating topology

The literal next fixed-page topology is **T37-R6**:

```text
new extreme supports: 4000,4001
fixed-page old-row release lower bound: 6
one exact relaxed release set: 69,198,251,1001,1004,1019
raw geometric coordinates: 24
independent coordinates after three ordinary moments: 21
protected features: base [0..16], U8
```

It must insert the two linked supports and move or deactivate a connected six-row boundary subsystem in the same actual full-hull event, while making negative:

```text
current stable [198,3000,1025]
current saddle (1027,3001)
all four inherited stable alternatives
all four inherited saddle alternatives
all replacement stable, unstable, and saddle births.
```

The exact relaxed apices are only feasibility witnesses for the necessary page inequalities; they must not be used as coordinates without a new full-hull construction.

A potentially smaller and genuinely different escape is a **changed-diagonal/non-star coupled prism or double-octahedral three-ball**. The seven-page and six-row theorems apply to frozen cyclic star pages and the fixed T37 assignment, respectively; a non-star cell with shared interior diagonals may evade both. Any such successor must still span the complete route and retain at least three independent mechanical controls after the three moments are eliminated.

The exact combinatorial specifications are in [the next-topology atlas](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/next_control_complete_topology.json).

## Independent reconstruction, mesh, and reproducibility

`verify_independent.py` does not import the constructor or replay asserted labels. It reads the centred V-data, independently enumerates supporting triples, maximal faces and true edges, reconstructs H/V equality and irredundancy, recomputes exact volume and centroid, audits every face, vertex and four-component edge cone, verifies the eight-sheet ledger, both circuit reversals, the connected route volume, all four deactivation cells, and mesh parity.

The OBJ and STL use the same 91 vertices and 178 boundary triangles. Independent reconstruction finds 267 triangulated mesh edges, each with multiplicity two, and Euler characteristic two.

The clean verification transcript ends with:

```text
ALL INDEPENDENT EXACT ROUTE DOUBLE-FLIP VERIFIERS PASS
ALL EXACT INTERVAL PERTURBATION VERIFIERS PASS
ALL INDEPENDENT EXACT T37 FROZEN-BOUNDARY FARKAS CHECKS PASS
ALL INDEPENDENT EXACT FROZEN-BOUNDARY STAR-PAGE COVER CHECKS PASS
ALL EXACT MINIMUM OLD-ROW ACTUATOR HITTING CHECKS PASS
PASS SHA-256 manifest 98 files
ALL_KEEN_QUARTZ_89_EXACT_NONWINNER_CHECKS_PASS
```

Primary reproducibility artifacts:

- [Complete exact bundle](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER.zip)
- [Bundle SHA-256](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER.zip.sha256) — `dbb6e76a10a0573f5239b21c0297e2f5e90a33fac3114b3baa41e5d56d18f990`
- [Full research handoff](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/RESEARCH_HANDOFF.md)
- [Clean-room exact verifier](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/verify_independent.py)
- [Run all builders and verifiers](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/RUN_ALL.sh)
- [Verification transcript](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/CURRENT_SESSION_REVERIFY.log)
- [SHA-256 manifest](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/manifest.json)
- [Watertight OBJ](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/body.obj)
- [Watertight STL](sandbox:/mnt/data/Keen_Quartz_89_M42_route_doubleflip_exact_NONWINNER/body.stl)

Reproduction command inside the unpacked bundle:

```bash
./RUN_ALL.sh
```

## Honest scope and continuation

What is proved is an exact, fully materialized, own-centred connected-route successor with old M42 defects absent, two true incidence flips, a positive-volume route three-ball, a complete eight-sheet audit, and strict class `(2,1,1)`. It is the strongest exact post-cell endpoint obtained here, not a Gömböc.

The new exact obstruction is also finite and nonrepeating: frozen-boundary cyclic star fans need at least seven pages, and the fixed T37 two-support star assignment needs at least six released old rows even in a permissive necessary-halfspace relaxation. What remains open is an actual convex T37-R6 realization, or a changed-diagonal/non-star prismatic or double-octahedral cell outside those theorems, whose single rebuilt far chamber has exactly the protected base and `U8` and no other equilibrium.
