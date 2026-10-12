# figure-0179

AI research report · 2026-09-01 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Nimble Comet 70 — wall-242 post-replacement determination

The current durable journal identifies the accepted source as the exact own-centred 19-vertex wall-242 endpoint of class `(2,2,2)` and explicitly assigns the next step as one connected cross-linked edge-sharing 2-/3-cell replacement of its complete four-feature block.

## Literal verdict

**EXACT NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained.

The strongest new endpoint is an exact rational, homogeneous, own-centred 16-vertex convex polyhedron with

- actual `(V,E,F,C)=(16,42,28,84)`;
- exact ordinary-volume centroid `(0,0,0)` after exact rational translation;
- strict exhaustive equilibrium class `(S,U,H)=(2,2,2)`;
- all 16 supplied vertices active, 28 irredundant triangular maximal faces, and 42 true edges;
- a coordinatewise own-centroid perturbation box `|δr_ij| <= 2^-36`, applied to the **uncentred supplied coordinates**, in which the ordinary centroid is recomputed interval-wise and the same full lattice, equilibrium class, and forced-edge sign chamber remain strict;
- independent clean-room reconstruction and matching watertight OBJ/STL.

This body is not a wall point and not an auxiliary-centre object. It is a strict, exact, own-centred nonwinner.

## 1. Source and actual topology change

The accepted source was the exact own-centred wall-242 endpoint `(19,51,34)`, class `(2,2,2)`, with residual stable face `[470,1258,2762]`, extra unstable vertex `2635`, and saddle edges `[262,3188]`, `[470,3578]`.

This continuation leaves that exhausted fixed cell entirely:

- old labels `262,470,2635,2762,3188,3578` are all absent from the supplied and active endpoint;
- retained old labels are `0,1258,1371,1614,1618,1725,1975,2152,2369,2515,2732,3290,3296`;
- three new extreme supports are inserted: `A=40001`, `B=40002`, `C=40003`;
- the new-support star is a connected triangulated 2-disk with `(V,E,F)=(11,23,13)` and boundary cycle `[0,1371,2732,3296,1725,1258,2152]`;
- coning its 13 boundary triangles to the exact ordinary-volume centroid produces a connected edge-sharing 13-tetrahedron 3-ball.

The inserted supports are genuinely cross-linked by true edges `A-C` and `B-C`. The complete new-support edge and face stars are in `certificates/replacement_topology_certificate.json`.

The original intended face cannot survive while `2635` is made non-extreme, so the intended pair is allowed to migrate. At this endpoint the retained intended equilibria are stable face `[0,1371,C]` and unstable vertex `C`.

## 2. Literal exact coordinates

Every uncentred coordinate is the displayed integer triple divided by `D=10^12`:

```text
label       X numerator       Y numerator       Z numerator
0           -92912225683       195697913392      -155439213568
1258       -434790439883      3455726662368      -110146979840
1371        888556753127     -3726077394768        78839367296
1614        965539701583     -3532737965648      -201316441088
1618        852357591441     -2948925087248       -29460012672
1725        944843866169     -3416441298912       173858035840
1975       1057746340809     -4256033958688      -182095753216
2152        814886470574     -3161384806848      -391987303424
2369        888639863309     -3687296308624      -221092966656
2515       1027034889688     -4211899214928       -30159597440
2732       1061598812745     -4321113895728       147437992192
3290       -946337090080      3639260562544       136251143680
3296       1103532415074     -4348167653920       181660588032
A=40001    -716593153568      3557895717680      -251884354176
B=40002    -465056957773      1639658805136      1493210625408
C=40003   -2616911632776     10176715650880      1801708094592
```

These are the robustness-optimized three-support realization followed by the exact conditioning map `diag(1,16,128)` and exact decimal rationalization. `scripts/generate_candidate.py` reads only `data/input_vertices_integer.csv`, recomputes the exact hull, exact ordinary centroid, centred H/V/E representation, all mechanics ledgers, and both meshes.

## 3. Exact ordinary-volume centring

The exact uncentred volume is

```text
2044994886865651353412486131236291
--------------------------------------------------
 732421875000000000000000000000000
```

approximately `2.792099685533903`.

The exact uncentred ordinary-volume centroid is

```text
cx = -3050789435929236853338123628945602210703903189
     ------------------------------------------------
       6543983637970084330919955619956131200000000000

cy =  891382773590775617210181899087770047326599507
     ----------------------------------------------
       408998977373130270682497226247258200000000000

cz =  114797250172493828140869667316354864348542533
     ----------------------------------------------
       255624360858206419176560766404536375000000000
```

numerically `(-0.4661975953343885, 2.1794254335691554, 0.4490857201054140)`.

Subtracting this exact rational vector from every supplied vertex gives the exported centred V-data. Signed tetrahedral integration over all 28 outward faces then gives exact first moments

`(Mx,My,Mz)=(0,0,0)`

and exact centroid `(0,0,0)`. The 28 positive tetrahedra and each exact moment contribution are in `data/positive_tetrahedralization.csv`.

No Santaló surrogate or point-mass centre is used.

## 4. Complete actual H/V/E incidence

The exact rebuild proves:

- 16/16 supplied points are vertices;
- 28/28 supporting triples are irredundant maximal faces;
- every nonincident vertex lies strictly inside every face halfspace;
- all 42 edges have exactly two incident maximal faces;
- `16-42+28=2`;
- minimum Euclidean nonincident face/vertex separation is approximately `0.00537464597038889`.

Files:

- `data/vertices_uncentered_exact.csv` — complete supplied exact V-data;
- `data/vertices_centered_exact.csv` — complete exact own-centred V-data;
- `data/wall242_postreplacement16_exact_H_irredundant.csv` — primitive integer H-data;
- `data/wall242_postreplacement16_exact_faces.csv` and `data/face_primitives.csv` — every maximal face and every exact projection barycentric coordinate;
- `data/vertex_primitives.csv` — every directed edge support at every vertex;
- `data/wall242_postreplacement16_exact_true_edges_full_cones.csv` — every true edge, incident-face pair, and all four exact cone components;
- `data/inactive_incidence.csv` — every strict nonincidence;
- `data/wall242_postreplacement16_exact_exact_audit.json` — complete machine-readable ledger.

## 5. Exhaustive mechanics at the body’s own centroid

### Stable maximal faces

| face | barycentric coordinates of the perpendicular foot | minimum |
|---|---|---:|
| `[0,1371,C]` | approximately `(0.4984445701, 0.2196047243, 0.2819507055)` | `0.2196047243` |
| `[1258,B,1725]` | approximately `(0.5566560062, 0.3560564556, 0.08728753818)` | `0.08728753818` |

Every other face has a certified negative barycentric witness. The closest excluded face is `[1258,C,B]`, margin approximately `-0.06242134550`.

### Unstable vertices

| vertex | minimum exact raw directed support | normalized directional-cosine margin |
|---|---:|---:|
| `3296` | approximately `0.2332683768` | approximately `0.2267774697` |
| `C=40003` | approximately `58.12758808` | approximately `0.9916949185` |

Every other vertex has an exact negative directed support. In normalized directional-cosine scale the closest excluded vertex is `1975`, approximately `-0.1724535592`.

### Saddle true edges

The four reported components are edge-foot `t`, `1-t`, and the two incident full-normal-cone coefficients.

| true edge | four components | minimum |
|---|---|---:|
| `[2152,A]` | approximately `(0.7990563084, 0.2009436916, 0.2108466369, 0.3034106000)` | `0.2009436916` |
| `[B,C]` | approximately `(0.05525743301, 0.9447425670, 0.2555341406, 0.3607426737)` | `0.05525743301` |

Every other true edge has a certified negative component. The closest excluded edge is `[3296,B]`, whose `1-t` component is approximately `-0.04656949966`.

Thus the complete strict class is exactly `(S,U,H)=(2,2,2)`, with `S+U-H=2`.

## 6. Positive own-centroid perturbation box

`scripts/verify_interval_own_centroid.py` certifies the independent coordinate box

`|δr_ij| <= 2^-36 = 1/68719476736 ≈ 1.4551915228366852e-11`

on all 48 coordinates of the **uncentred** input table. For every point in this box it:

1. retains the same 28 outward supporting triangles and all 42 true edges;
2. integrates interval volume and first moments over that fixed exact sphere;
3. encloses the perturbed body’s own ordinary centroid as `M/V`;
4. translates every vertex by that common centroid interval;
5. verifies all stable/nonstable face witnesses, all unstable/nonunstable vertex witnesses, and all four components of every saddle/nonsaddle edge;
6. retains the exact forced-edge external-positive chamber below.

The body’s RMS centred radius is approximately `5.37084`, so the certified radius is about `2.71e-12` of RMS radius. The certificate is deliberately fail-closed and is not asserted to be maximal.

## 7. Exact broad-component obstruction

The true edge `[2732,3296]` has external-positive endpoint stars. With

`σ(v→w) = -p_v·(p_w-p_v)`

at the exact own centroid:

- `σ(2732→3296) ≈ -0.22960685787003174`;
- `σ(3296→2732) ≈ +0.23326837677265763`;
- every support from either endpoint to every neighbour outside this pair is positive;
- the smallest such external support is approximately `0.3295373774896295`;
- exactly

```text
σ(2732→3296)+σ(3296→2732)
 = ||p_3296-p_2732||^2
 = 732303780525181327741 / 200000000000000000000000
 > 0.
```

If both endpoints were nonunstable while the external supports stayed positive, both mutual supports would have to be nonpositive, contradicting the positive identity. Hence at least one endpoint is unstable throughout this complete sign chamber. Since `C` is independently and strongly unstable, this chamber has `U>=2`.

This is an exact broad sign-cell obstruction, not merely a rank or first-order failure. It does not exclude topologies that delete `[2732,3296]`, deactivate an endpoint, or reverse an external support.

The literal certificate is `certificates/forced_edge_obstruction.json`; the clean-room verifier reconstructs the identity and every listed sign independently.

## 8. Attempts to break the endpoint

The search did not stop at exactifying the first `(2,2,2)` sample.

- A complete topology-free 16-point own-centroid/full-cone search found the all-active A/B/C patch, then a 32,976-evaluation robustness run thickened its relevant feature and incidence margins.
- Eight determinant-one metric searches used 21,900 full hull/centroid/cone evaluations; no `(1,1,0)` metric chamber was found.
- 238 explicit fourth-support probes around faces, edges, vertices, and the forced edge produced only classes `(2,2,2)`, `(2,3,3)`, `(3,2,3)`, `(4,2,4)`, and larger Euler-neutral packets.
- Ten all-active 17-vertex CMA continuations totalled 176,400 evaluations from forced-edge, face-bridge, face-far, and stable-side initializations; none reached `(1,1,0)`.
- Direct probes of the three key adjacent four-point circuits only transferred or enlarged the residual block.
- All 240 fixed-ledger first-order exclusion branches of the earlier near endpoint were solved; nominal positive directions occurred only at macroscopic trust and actual hull continuation created births or support collapse before cancellation.

These computations are discovery evidence, not a global impossibility theorem. The exact theorem-level output is the finite endpoint, its positive box, and the forced-edge sign-cell obstruction.

## 9. First genuinely new successor topology

The next admissible move is no longer another support-distance polish or one-witness rail. It must leave the certified forced-edge sign chamber and couple three actual adjacent circuits:

1. forced-edge circuit `{1975,2732,3296,B}`: delete diagonal `[2732,3296]`, insert `[1975,B]`;
2. saddle circuit `{0,2152,A,1258}`: delete saddle diagonal `[2152,A]`, insert `[0,1258]`;
3. saddle circuit `{1258,B,C,1371}`: delete saddle diagonal `[B,C]`, insert `[1258,1371]`;
4. simultaneously move the perpendicular foot of extra stable face `[1258,B,1725]` outside that triangle.

The three events must share a finite-thickness edge-sharing 3-cell—triangular prism, octahedral cell, or a four-support replacement with one common interior edge—so that the forced maximum, both saddle routes, and the extra stable foot cross before a compensating birth. Sequential circuit probes are already represented by transfer cells and are not the successor.

Three ordinary-volume moment variables must remain dependent exact equations in each rebuilt cell. The actual hull, maximal faces, true edges, and complete edge cones must be regenerated after every circuit crossing.

## 10. Verification and mesh export

- `scripts/verify_exact.py` reruns the exact primary reconstruction, H/V incidence, centroid, class, perturbation receipt, and forced-edge theorem.
- `scripts/verify_independent.py` is a standard-library-only clean-room implementation. It imports neither the generator nor `exact_core.py`; it independently enumerates all supporting triples, integrates the centroid, rebuilds all maximal faces and true edges, classifies every face/vertex/full edge cone, verifies the forced-edge identity, reconstructs the 2-disk patch, and checks the mesh.
- `scripts/verify_interval_own_centroid.py` reruns the exact rational interval box with the perturbed own centroid recomputed.
- `scripts/verify_mesh.py` verifies 16 OBJ vertices, 28 oriented faces, 42 edge incidences of multiplicity two, and 28 STL facets.
- `mesh/body.obj` and `mesh/body.stl` are matching watertight exports.

The combined script is `RUN_ALL_VERIFIERS.sh`. Its stored transcript ends in:


[Encoded source block omitted; the code in this passage is incomplete.]


## Final determination

The assignment’s requested **post-replacement endpoint topology** was achieved literally: none of the six prescribed old labels is extreme or even supplied in the final generator, and the replacement is a connected cross-linked three-support disk/3-ball complex. I did **not** certify a single continuous source-to-endpoint homotopy in which all six old vertices cross their loss-of-extremality walls at one common parameter; the exact claim is the material endpoint and its active-lattice certificate, not such a path theorem. The endpoint is exact, homogeneous, own-centred, open, completely audited, independently reconstructed, and mesh-exported. It is nevertheless a strict `(2,2,2)` **NONWINNER**.

Its exact forced edge `[2732,3296]` proves `U>=2` throughout the current external-positive sign chamber. The first unexcluded continuation is the shared three-circuit finite-thickness cell specified above; anything that retains that edge and its external-positive stars cannot be a Gömböc.

## Portable artifact index

- Complete exact post-replacement bundle (`Nimble_Comet_70_wall242_postreplacement_exact_NONWINNER.zip`) — SHA-256 `0a7a7ade6e80bc4254efe2194039986680d88fc595ef54eff80a36db6d7f103a`.
- Standalone report (`REPORT.md`)
- Machine-readable candidate (`candidate.json`)
- Deterministic exact generator (`generate_candidate.py`)
- Primary exact verifier (`verify_exact.py`)
- Independent clean-room verifier (`verify_independent.py`)
- Own-centroid interval-box verifier (`verify_interval_own_centroid.py`)
- Complete centred V-data (`wall242_postreplacement16_exact_V_exact.csv`)
- Complete irredundant H-data (`wall242_postreplacement16_exact_H_irredundant.csv`)
- All maximal faces (`wall242_postreplacement16_exact_faces.csv`)
- All true edges and full four-component cones (`wall242_postreplacement16_exact_true_edges_full_cones.csv`)
- Exact centroid and mechanics audit (`wall242_postreplacement16_exact_exact_audit.json`)
- Forced-edge obstruction certificate (`forced_edge_obstruction.json`)
- Replacement topology certificate (`replacement_topology_certificate.json`)
- Perturbation certificate (`own_centroid_perturbation_certificate.json`)
- OBJ mesh (`body.obj`)
- STL mesh (`body.stl`)
- Combined verification transcript (`RUN_ALL_VERIFIERS.txt`)
- Fresh-extraction verification transcript (`Nimble_Comet_70_wall242_postreplacement_exact_NONWINNER_FRESH_VERIFY.txt`) — SHA-256 `820b97b5179105ce952a6214bedd7cd776286f42f4968f7c54ed736301c21792`.
- SHA-256 manifest (`SHA256SUMS.txt`)
- Accepted 19-vertex parent archive (`rapid_maple42_wall242_handoff.zip`) — SHA-256 `fe92046adee61f4d6e706d541df55c387b38933119c5aa81997b954369747ee9`.
