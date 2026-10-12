# figure-0218

AI research report · 2026-09-02 UTC

---

# Clear Willow 25 — complete research handoff

## Result

No literal exact own-centred `(S,U,H)=(1,1,0)` polyhedron was found. I did, however, instantiate and independently certify the smallest exact topology-transfer neighbourhood I could realize around the M42 benchmark, classify its complete codimension-two and codimension-three regular-subdivision landscape, and close the fixed-row one-support/page promotion families by exact sparse Gordan certificates.

The supplied journal starts from the accepted exact rational M42 body `(V,E,F)=(61,163,104)`, strict `(2,1,1)`, with extra stable triangle `[198,224,258]`, unique unstable vertex `8`, and saddle edge `(229,247)`; it identifies the shared packet and core replacement set `{198,224,258,229,247,228}`.

The new exact endpoint **literally deletes both named unwanted features**: rows `224` and `229` are removed, so `[198,224,258]` is not a hull face and `(229,247)` is not a hull edge. The actual full hull nevertheless contains a replacement Euler-neutral pair, stable triangle `[1000,1025,3000]` and saddle edge `(1027,3001)`. Thus this is an exact topology-changing nonwinner, not a claimed Gömböc.

**Portable complete bundle:** M42_slot1_Clear_Willow_25_complete.zip  
**ZIP SHA-256:** `629e7690827f7b677eecaec3bed6e98e7c626119b1a1f53c6087428ca212107b`  
**Human-readable report:** README.md  
**Machine-readable summary:** result_summary.json

## Exact instantiated transfer body

I reconstructed the 61 active M42 rows from the parent common lattice, then applied two exact rational clipping halfspaces. The first removes `224` and creates 26 exact edge intersections `1000..1025`; the second removes `229` and creates four exact intersections `1026..1029`. Two exact exterior supports `3000,3001` complete the cap. The exact planes, crossing parameters, and support coordinates are in construction.json; the complete exact coordinates are in coordinates_exact.csv, and a single 2918-bit common lattice is in coordinates_common_lattice.csv.

A fresh all-row hull computation gives:

```text
all 91 supplied rows extreme
(V,E,F) = (91,203,114), Euler = 2
face sizes = 86 triangles, 25 quadrilaterals, one pentagon,
             one 17-gon, one 26-gon
stable faces = [0,1,...,16], [1000,1025,3000]
unstable vertices = [8]
saddle true edges = [(1027,3001)]
own-centroid class = (2,1,1)
```

The unshifted volume and centroid are

```text
V = 1050.2209976887918...
C = (-0.8998929470452524...,
      2.391135694440807...,
     -0.15345263936534168...)
```

with the complete exact fractions in certificate.json. Translation obeys the exact identity `M(P+τ)=M(P)+Vτ`; because `V>0`, `τ=-C` is the unique centring solution and the moment Jacobian is `V I₃`. The exact mechanics verifier recomputes three zero centred first moments.

Strict normalized margins are:

```text
minimum nonincident support distance       1.3822279301226382e-7
target 17-gon stable                       8.861311762686697e-1
replacement stable                         2.9098653145428115e-5
strict nonstable-face clearance            1.8110143963034793e-5
target U8 unstable                         1.7161831472802694e-1
strict nonunstable-vertex clearance        9.370131758094104e-5
replacement saddle                         5.939874719300841e-4
strict nonsaddle-edge clearance            1.3342352902887952e-3
```

All underlying tests are exact rational signs, not floating acceptance. Complete incidence is in face_cycles.json and true_edges.csv; exhaustive face, vertex, and edge mechanics are in the three `*_mechanics_exact.json` files.

The construction has 12 nontranslation shape coordinates—three for each cut plane and three for each support—plus three translation controls. Exact centring eliminates only translations, leaving 12 shape dimensions in the open incidence chamber. A codimension-two simultaneous circuit therefore leaves 10 dimensions; the codimension-three route cell leaves 9.

## Exact oriented-matroid and regular-subdivision atlas

The complete machine-readable atlas is oriented_matroid_regular_atlas.json. It records exact rank-four chirotopes, every minimal circuit, integer Gale bases, exact open topes, lifting weights, and lower tetrahedralizations for 19 cells: two apical codimension-one cells, all 16 direct codimension-two octahedra, and one codimension-three route cell. Weight `0` on a promoted cell and `1` on every other point is an explicit exact regular-cell certificate.

### Apical circuits

Stable apical cell `S5={198,1000,1025,258,3000}` has base circuit `[198,1000,1025,258]` with coefficient vector

```text
(+37031495073507327534225716489504196870208501402334454817,
 -70781776867049524765626990757394112116550188889095027253,
 +46884871922176409245866705785487303706313708125553168512,
 -13134590128634212014465431517597388459972020638792596076)
```

and sign `+-+-`.

Saddle apical cell `H5={1026,1027,1028,1029,3001}` has base circuit `[1026,1027,1028,1029]` with coefficient vector

```text
(+14297806508225368872417964601301119694229192620593481568473419559,
 -345680984830889547976467074439753179119128642425159539347465471266,
 -115316756535738581407526748430737737912569979316831679072280285295,
 +446699934858402760511575858269189797337469429121397736851272337002)
```

and sign `+--+`.

### Six-vertex codimension-two cells

The four stable-side triangles and four saddle-side triangles form all `4×4=16` pairings. Every pairing is an exact empty octahedron with affine nullity two, eight triangular facets, six minimal five-point circuits, 12 realizable open topes, and six distinct regular triangulations. The full incidence and all 96 circuit vectors are in octahedron_atlas.json and the master atlas.

Representative `O0` is

```text
vertices [198,258,1026,1027,3000,3001]
facets
 [198,258,1026]      [198,258,3000]
 [198,1026,1027]     [198,1027,3000]
 [258,1026,3001]     [258,3000,3001]
 [1026,1027,3001]    [1027,3000,3001]
```

All 16 are combinatorially valid regular cells, but every fixed-coordinate boundary promotion has a belt facet that places at least one protected base vertex on the wrong side.

### Seven-vertex codimension-three route cell

The smallest cell spanning the actual physical route is

```text
K7 = {3000,258,54,69,228,1026,3001}
```

It is exact, empty relative to all 91 points, has volume `93.90508114536689...`, affine nullity three, 10 triangular facets, and 21 minimal five-point circuits. Its facets are

```text
[54,69,258]         [54,69,1026]
[54,258,3000]       [54,1026,3000]
[69,228,258]        [69,228,1026]
[228,258,3001]      [228,1026,3001]
[258,3000,3001]     [1026,3000,3001]
```

Two overlapping route circuits are:

```text
A=[3000,258,54,69,228], signs ++-+-
coefficients:
  5346880932769533915138345396000799000000
  34244788885153042448332738512977087331948
 -5979562771098079313067604390517016805623080
  6447145168824278802033683135274847664928473
 -507174067544122065329549828666808745637341

B=[54,69,228,1026,3001], signs +-++-
coefficients:
  7580060022821384959138959091215992670432079951050231790283977236359539
 -8335821845670671063914488859026637590807506181571674205601619625493745
  642042911541529441627752763354295804341108164844136918925075872109586
  597943855599105335952498940287041870153614166246491548429276823654620
 -484224944291348672804721935830692754119296100569186052036710306630000
```

The exact quotient arrangement has 282 open topes and 25 regular triangulations. Every joint sign pair is realizable:

```text
(A,B)    topes    distinct triangulations
 ++        33              10
 +-       108              10
 -+       108              12
 --        33               5
```

One exact `++` triangulation is

```text
[54,69,1026,3001]
[69,228,1026,3001]
[258,54,69,3001]
[258,69,228,3001]
[3000,54,1026,3001]
[3000,258,54,3001]
```

This separates the two issues cleanly: simultaneous circuit signatures are oriented-matroid-realizable; the obstruction is protected boundary embedding.

## Minimal surgery families exhausted exactly

1. **Fixed direct octahedra.** All 16 are empty regular cells, but none is base-compatible as a boundary promotion.

2. **Direct octahedron plus one existing adjacent connector.** All `16×11=176` combinations were rebuilt; 175 are strict seven-vertex ten-facet cells, all empty, and zero are base-compatible. Incidence is in heptahedron_atlas.json.

3. **Direct octahedron plus one arbitrary new connector.** All `16×64=1024` visibility signatures were enumerated. There are 37 nonempty strict local chambers. Under the exact global local-star contract—every new horizon triangle supports all 91 old points, all remote old faces remain protected, and the connector is genuinely extreme—zero are feasible. single_connector_global_farkas.json contains one exact four-constraint Gordan certificate for each of the 37 chambers.

4. **Fixed K7 plus one arbitrary new page.** Of 128 visibility patterns, 15 are strict local chambers and six have local base-compatible witnesses. Full actual-hull recomputation of those six witnesses deactivates the entire target base and `U8`; classes range from `(2,2,2)` to `(2,19,19)`. Under the same exact global support/remote-protection contract, all 15 chambers are infeasible. K7_one_page_global_farkas.json contains 15 exact four-constraint Gordan certificates.

Each Gordan certificate consists of positive rational multipliers summing to one, a zero weighted affine coefficient vector, and a nonpositive weighted constant; therefore strict satisfaction of all defining inequalities is impossible. The independent verifiers reconstruct all identities without invoking an optimiser.

These are scoped exclusions, not a global no-go theorem. They fix the old rows and prohibit deliberate remote replacement. Moving old rows, deactivating row `54`, or replacing a larger neighbourhood remains outside the proved scope.

## Independent reconstruction, equilibrium audit, and mesh

The portable replay from the parent source, not from a cached endpoint, returns

```text
CLEANROOM_SOURCE_RECONSTRUCTION_PASS
rows=91 first_crossings=26 second_crossings=4
canonical_sha256=97c0f024fe598013f05c6f4a89a589832ed6f436ede86a3038f47f865f90277d
```

The independent C++/GMP verifier checks all 121,485 point triples and 2,284,696 exact signs:

```text
INDEPENDENT_GMP_ALL_TRIPLE_HULL_PASS
rows=91 triples=121485 nondegenerate=121485
supporting_triples=3476 facets=114 edges=203
```

The exact mass/mechanics verifier reconstructs every face, vertex cone, and true edge and ends with `INDEPENDENT_EXACT_MASS_MECHANICS_PASS`. The oriented-matroid replay ends with

```text
INDEPENDENT_EXACT_ORIENTED_MATROID_REGULAR_ATLAS_PASS
cells=19 octahedral_topes=192 K7_topes=282 K7_regular_triangulations=25
```

The Gordan replays end with exact passes for 37 and 15 chambers respectively. A clean extraction of the ZIP was independently recompiled and reproduced every marker and every packaged SHA-256.

The watertight meshes are body.obj and body.stl. The mesh verifier reports 91 vertices, 178 triangles, 267 mesh edges, Euler characteristic two, volume `1050.2209976887918`, and centroid norm `1.688×10^-15`.

## Smallest unclassified realizable complex and continuation

The exact exclusions close every fixed-row one-support/page local-star promotion based on the direct octahedra or K7. The smallest remaining nonrepeating family is therefore a connected finite-thickness **two-page extension `K7+{X,Y}`**, or equivalently `K7+X` with row `54` moved or deactivated in the same full-hull event.

It must replace the three K7 facets `[54,258,3000]`, `[54,1026,3000]`, and `[54,69,1026]` without forcing one macroscopic point to see all three; preserve the full base `[0..16]` and `U8`; couple route circuits A and B; and give stable-side and saddle-side diagonals independent controls. With two new support positions, the chart has 18 nontranslation shape variables; exact centring still consumes only translations, and the three K7 circuit equalities leave 15 before any additional page-gluing equations, conservatively at least 12 after up to three such equations.

The next constructive test should enumerate the two-page oriented matroids in six connector variables, impose the complete 91-row horizon and remote-support inequalities, and permit row `54` to become nonextreme. A successful chamber must then be instantiated and the full hull, centroid, all equilibria, and mesh recomputed exactly. I do not claim this family is feasible; it is the smallest one not covered by the exact certificates above.
