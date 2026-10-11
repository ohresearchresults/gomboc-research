# figure-0174

Historical AI scientific report · saved 2026-09-01 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Steady Quartz 25 — complete handoff

## Literal disposition

**NONWINNER.** No finite uniform-density convex polyhedron with strict own-centroid `(S,U,H)=(1,1,0)` was obtained. The acceptance gate requires an exact/interval-isolated finite body, its own ordinary-volume centroid, the complete irredundant H/V lattice, every maximal face and true edge, an exhaustive full-normal-cone audit, a nonzero perturbation neighborhood, an independent verifier, and matching mesh; auxiliary-centre and near-wall objects do not qualify. :contentReference[oaicite:0]{index=0}

The supplied journal identifies the exact 3,481-face `(2,2,2)` endpoint and its connected 335-row/771-edge residual patch as this direction’s mature starting point. :contentReference[oaicite:1]{index=1} I recovered the completed persistent bundle that had not yet been integrated into that journal, reran its deep clean-room verification, and added an independently verified connected three-dimensional control complex for the whole patch.

**Artifacts:** [complete archive](sandbox:/mnt/data/Steady_Quartz_25_global_support_exact_NONWINNER.zip), [SHA-256 sidecar](sandbox:/mnt/data/Steady_Quartz_25_global_support_exact_NONWINNER.zip.sha256), [standalone handoff](sandbox:/mnt/data/Steady_Quartz_25_global_support_exact_NONWINNER/STEADY_QUARTZ_25_HANDOFF.md), [OBJ](sandbox:/mnt/data/Steady_Quartz_25_global_support_exact_NONWINNER/geometry/exact_endpoint_3481.obj), [STL](sandbox:/mnt/data/Steady_Quartz_25_global_support_exact_NONWINNER/geometry/exact_endpoint_3481.stl), [outer verifier](sandbox:/mnt/data/Steady_Quartz_25_global_support_exact_NONWINNER/verify_steady_quartz25.sh). Archive SHA-256: `409b785a63b9c684ee8e03476153b0483eeaaab95f0a1323ee620626f2acc390`.

## Exact strongest object

The normative exact dyadic generator is `endpoint_exact/data/source_rows_modes.hex`, SHA-256 `422733f54163f891047ecf2285c7953d03d5ce0dc014d321e390133881af1a33`. Interpret every hexadecimal binary64 token as its exact dyadic rational and set

```text
u_i(t)=1+F_i·t,
P(t)={x:q_i·x<=u_i(t)}.
```

The 180-bit Krawczyk certificate isolates one and only one simultaneous zero of the ordinary first moments near

```text
t=(-0.0312097326412240411067188691450639221,
    0.00413487507671882344936376366797188405,
    0.00501990150313157569115587917413372050),
```

with widths about `1.01e-40,1.48e-40,1.42e-40`. Its enclosures are

```text
V  in [4.13641036706639664581866613908251232,
       4.13641036706639664581866632642853293]
Mx in [-2.00147415372090382445455755239009953e-26,
        2.00148084038570361662267446855055984e-26]
My in [-3.28461309373342259659319663333321704e-26,
        3.28463572620397038326430655472743339e-26]
Mz in [-8.23842861474930886687904627134077920e-26,
        8.23841869716845962779876587067677910e-26].
```

The exact moment-Jacobian determinant interval is strictly positive around `38.5506280049554555536`, proving rank three and uniqueness inside the box.

The independently reconstructed lattice is

```text
(F,V,E,triangles)=(3481,6958,10437,13912),
```

all 3,481 H rows irredundant. The exhaustive positive feature sets are exactly

```text
stable:   424, 3736
unstable: (2288,2394,2603), (1744,1779,2025)
saddles:  (1490,1805), (2629,2910),
```

hence strict `(2,2,2)`. The minimum positive and closest excluded directed intervals are respectively:

```text
stable   +3.65287851606908e-5 ; -3.57402567755753e-6
unstable +0.184946161766626  ; -0.001728871479588
saddle   +0.189180741322743  ; -0.000745219765454.
```

Minimum directed nonincident H–V separation exceeds `1.468921317915317e-9`. The exact preserving `L_infinity` radius in the three root parameters is

```text
10375516690492628201447081 /
1532495540865888858358347027150309183618739122183602176
=6.7703405418264811126e-30...
```

The full maximal-face cycles, all 10,437 true edges, interval H/V arrays, and meshes are materialized in the archive; their principal SHA-256 values are `4f2c0f6e...` for `root_maximal_face_cycles.json`, `57df6ea2fe...` for `root_true_edges.csv`, `c88e11f1e5...` for `root_interval_hv.npz`, `737a7611c2...` for OBJ, and `671e8748dd...` for STL.

## Exact 335-row residual patch and frozen interfaces

`endpoint_exact/certificates/residual_successor_patch.json` (SHA-256 `524c5299cddb395003f709c9dacdd3904d02ecb57f7fba6618daa488defe11b5`) contains the complete 335 original row labels and all 771 certificate edges. `prior_shared_event/certificates/patch_topology_certificate.json` (SHA-256 `ec7edd58dfbe18f7cad516e3eae37bc4d7d03d12006b15b91d8d074a65be66f1`) contains all 434 induced triangles, 769 surface edges, both boundary cycles, every mixed patch/background facet, and every outside neighbor.

The exact topology is an orientable biconnected annulus:

```text
rows 335; certificate edges 771; surface edges 769; triangles 434;
Euler characteristic 0; boundary lengths 78 and 158;
99 interior rows; 535 mixed boundary facets; 291 outside-neighbor rows;
graph diameter 33.
```

It contains the whole residual Euler-neutral block

```text
S remove 3736;
U remove (2288,2394,2603);
H remove (1490,1805) and (2629,2910),
```

while the frozen target mechanics are stable row `424` and unstable facet `(1744,1779,2025)`. Exact shortest routes joining the four residual features are recorded in the certificate; the principal routes have 27, 19, and 7 vertices respectively.

## Moment-null control rank and action

The exact local model has three dyadic frame directions at every one of the 335 patch rows: 1,005 geometry coordinates, plus three dependent moment coordinates, for 1,008 variables. Since the moment map has rank three, the local moment-null manifold has dimension 1,005.

Using radial controls at rows `1561,2394,2910,3736` and the three moment variables, the directed determinant bounds are

```text
combined seven-equation determinant:
[-594949.6256380166659744428990970460911,
 -594949.6256369898768878423339436126306]

four-wall determinant after eliminating moments:
[-15432.9425077469266588749638964162523,
 -15432.9425077203186878333675276961659].
```

Both exclude zero. Thus the extra stable, extra unstable, and both saddle wall functions are independently actionable on the exact moment-null manifold. The obstruction is not rank. A high-accuracy formal seven-equation common root exists, but rebuilding the actual hull crosses the U circuit first and gives `(3,2,3)`, so it is not a certified Morse cancellation.

## Connected three-dimensional shared operation

I promoted the exact 434-triangle annulus `K` to the canonical product complex `K×[0,1]`, triangulating each prism by the globally compatible staircase rule. This gives an exact combinatorial and exact-dyadic three-dimensional simplicial complex embedded in control spacetime:

```text
670 vertices; 2642 edges; 3274 triangular faces; 1302 tetrahedra;
connected tetrahedral dual;
boundary f-vector (670,2010,1340), Euler 0, a closed genus-one surface.
```

Every tetrahedron has positive exact dyadic Gram determinant; the minimum embedded 3-volume is approximately `4.008414362932949e-6`. The certificate, complete vertex/tetrahedron tables, and independent verifier are under `steady_quartz25_addendum/`.

The associated simultaneous operation controls all three local polar directions at 332 nonprotected patch rows and remote guards `389,459,493,529`: 336 controlled polar vertices and 1,008 frame coefficients. Only protected rows `1744,1779,2025` are frozen, and every residual-feature row is controlled.

A mandatory fresh hull/centroid rebuild of the terminal 1,008-control body gives

```text
(F,V,E,triangles)=(3270,6536,9804,13068), volume 4.122367808804907,
class (2,3,3).
stable: 424,3736
unstable: (2252,2394,2637), (2524,2594,2910), (1849,1885,2025)
saddles: (1490,1805), (2524,2910), (2594,2910).
```

It deactivates 211 old rows and genuinely crosses combinatorial walls, but the U–H2 packet reappears on `2524/2594/2910` and the intended unstable facet is replaced by `(1849,1885,2025)`. This terminal body is numerical discovery data, not the accepted exact object.

Two other full own-centroid rebuilds are `(3,4,5)` with 3,329 faces and `(5,4,7)` with 3,459 faces. A 384-sample radial/tangential packet search found zero `(2,1,1)` and zero `(1,1,0)` cells. A separate fresh 17-control actual-hull cross-check in this assignment also produced a transfer cell `(3,3,4)`, not a winner.

## Obstruction and forced next topology

The wall ordering is the decisive architecture-specific obstruction:

```text
S3736 death is preempted by H(3736,3737);
H(1490,1805) death is preempted by U(1490,1561,1805);
U(2288,2394,2603) transfers across circuit (2288,2394,2603,2637);
H(2629,2910) transfers through (2524,2594,2629,2910);
row 529 and edge (459,529) form a paired S–H birth;
large shared motion flips the protected-U circuit to (1849,1885,2025).
```

Representative one-sided birth/death ratios are `0.4796787703` for the S channel and `0.3628815477` for the H1 channel; the remote S/H pair is coincident to about `2.6e-6` relative. These derivative numbers are diagnostics; the exact claims are the endpoint, patch, moment-rank, lattice, and verification certificates. This closes the tested fixed-cell solve, annular surface sheets, local radial/tangential packet family, and the 1,008-control shared operation. It is not a global nonexistence theorem for polyhedral Gömböcs or for every possible replacement of the patch.

The smallest evidence-forced successor is a **topology-first nonannular polar bridge cell spanning both annular boundary cycles before the four equilibrium deaths**. It must couple the circuits/packets

```text
(2288,2394,2603,2637),
(3736,3737,3808,3911),
(1490,1561,1805,1806,1875),
(2524,2594,2629,2910),
(389,459,493,529),
(1744,1779,1849,1885,2025).
```

At least seven independent shape controls are required: S-shell flip, U-circuit flip, H1/U discriminator, H2 discriminator, remote antibirth discriminator, shared bridge depth, and protected-U discriminator; the three moments remain dependent hard equations, so at least ten effective coordinates are needed. After every circuit crossing the actual hull, exact moments, maximal faces, true edges, and all four edge-cone components must be recomputed.

## Verification boundary

`DEEP=1 ./[internal-source-reference].sh` ends with `ALL NIMBLE COMET 17 CHECKS PASSED`; `python steady_quartz25_addendum/verify_shared_control_3d_complex.py` ends with `ALL SHARED CONTROL 3D COMPLEX CHECKS PASS`; the outer manifest verifier passes. Therefore the literal final state is:

```text
WINNER: no
DISPOSITION: exact NONWINNER
STRONGEST EXACT BODY: (F,V,E)=(3481,6958,10437), own-centroid (2,2,2)
FULL PATCH: exact 335 rows / 771 edges with complete frozen-background interface
MOMENT-NULL ACTION: rank 3 moments, dimension 1005, selected wall rank 4
SHARED 3D COMPLEX: 670 vertices / 1302 tetrahedra
GLOBAL OBSTRUCTION: none proved
FORCED NEXT TOPOLOGY: nonannular cross-boundary bridge, >=7 shape + 3 moment controls.
```
