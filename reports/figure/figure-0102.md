# figure-0102

Historical AI scientific report · saved 2026-08-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Coupled post-ladder surgery handoff

## Literal verdict

**No finite homogeneous convex polyhedral Gömböc was found.** The strongest endpoint, `postladder62_optimized`, is a genuine finite uniform-density convex polyhedron, evaluated at its own exact volume centroid, with open strict class **`(S,U,H)=(1,2,1)`**. One unstable–saddle pair remains, so this is **not** a Gömböc.

The journal’s acceptance gate requires a materialized own-centroid `(1,1,0)` object and excludes walls, auxiliary centers, and unexpanded generators. :contentReference[oaicite:0]{index=0} The inherited `longstrip_rec0` was `(2,4,4)` with two verified fourteen-edge branches and a four-rung ladder. :contentReference[oaicite:1]{index=1} This continuation replaces that ladder and advances the exact frontier to `(1,2,1)`.

## Complete exact source and generator

Every hexadecimal literal is interpreted as its exact IEEE-754 dyadic rational:

```python
from fractions import Fraction as F
Q_HEX=[["-0x1.09f4aad8ab584p+1","0x1.14cd853496415p+1","0x1.78b431c98866cp+8"],["0x1.5c138aab1e3dfp+5","0x1.9f516ddb8f9e6p+6","-0x1.ddcd5c3ad1479p+7"],["0x1.9f7d59ff2d96ep+5","0x1.0f1c177c5a12ep+7","-0x1.c139c5229398dp+7"],["0x1.8b328a063acd6p+6","0x1.5adaa4fb67e19p+7","-0x1.8b369faee98aap+7"],["0x1.d4afbcbca6050p+6","0x1.9ebd297f62048p+7","-0x1.433bd06584df4p+7"],["0x1.053c704dabae5p+7","0x1.de69e1e5c152cp+7","-0x1.d2d0c4c64bffep+6"],["0x1.09a983920e7bdp+7","0x1.09f938e982ff1p+8","-0x1.cde412b251d3bp+5"],["0x1.fe4c3e50d06a3p+6","0x1.17ebeff326052p+8","0x1.7fd31ba932dbcp+1"],["0x1.c94ab32715246p+6","0x1.1a4b723c45934p+8","0x1.fede21b84a58ep+5"],["0x1.94eddd05ca9b4p+6","0x1.10e6be04e020ap+8","0x1.eefdf78e1dc9cp+6"],["0x1.6a1ba17827a70p+6","0x1.f81b83d371343p+7","0x1.6c7ead079fa5bp+7"],["0x1.4a85193bd7084p+6","0x1.b252db418ffe6p+7","0x1.da7360689573ap+7"],["0x1.22aa1fa3c53bep+6","0x1.5876461944cdbp+7","0x1.20cd8ba6ec1d4p+8"],["0x1.a41847d80c9b1p+5","0x1.e044653ee3096p+6","0x1.46e5702e1d9cbp+8"],["0x1.9054f3c8ce4d4p+4","0x1.fbc754e8b12c9p+5","0x1.65cc09a8fe7ecp+8"],["-0x1.09987c1a1959cp+5","0x1.6c57be38e0b62p+6","-0x1.f02b9e181f51ap+7"],["-0x1.979e42143d356p+5","0x1.1809c2973e613p+7","-0x1.c88faf5d579eep+7"],["-0x1.3ab886801e51ep+6","0x1.6d6e760676db2p+7","-0x1.960ad50c030b3p+7"],["-0x1.5f7de95bcddd3p+6","0x1.c22e028405685p+7","-0x1.4ab33a75ae452p+7"],["-0x1.895a4cebf2c0bp+6","0x1.fd25c552b7047p+7","-0x1.ce20e79b1a26ap+6"],["-0x1.b1fe1e9dcbc9fp+6","0x1.1256236e1ebc3p+8","-0x1.c8d95f428c01cp+5"],["-0x1.c0ca5861b9c7ep+6","0x1.1faf17f244ad7p+8","0x1.7c5ab9c500298p+2"],["-0x1.c3786e1e2a4fdp+6","0x1.1f94e65be1a02p+8","0x1.e6441c84cb22ap+5"],["-0x1.b16c2dcef58efp+6","0x1.14257e932a651p+8","0x1.eed58a252dd63p+6"],["-0x1.881e61c98de27p+6","0x1.fcc602dad6f25p+7","0x1.6e0416bbad007p+7"],["-0x1.4c73207036bd8p+6","0x1.bc6ef601a86efp+7","0x1.dcf6704a81f9fp+7"],["-0x1.0470f0820cd46p+6","0x1.65ff208659580p+7","0x1.204ae4bf6f7ecp+8"],["-0x1.5ae372d945c7ap+5","0x1.f987fc1abbf52p+6","0x1.49b748f185d23p+8"],["-0x1.5542f511ecff3p+4","0x1.0804752f01d9cp+6","0x1.67c0bf1869934p+8"],["-0x1.e0bcf9e6c765ap+2","-0x1.673e7509a4ef5p+8","-0x1.acca0ce14b397p+8"],["-0x1.4ef5fd657bf0dp+3","-0x1.672b84e42a2b6p+8","-0x1.acca0ce14b397p+8"],["-0x1.fbf641afc76b9p+1","-0x1.9c5b56447bdd4p+8","-0x1.6197599cc1e92p+8"],["-0x1.678ac0169a236p+2","-0x1.9c566dc553d79p+8","-0x1.6197599cc1e92p+8"],["-0x1.8b1097d87a6f6p+0","-0x1.c0800baa2a53cp+8","-0x1.1b38dbfb7dc09p+8"],["-0x1.ab298cf3cb602p+1","-0x1.c07d8bf9f9b9ep+8","-0x1.1b38dbfb7dc09p+8"],["0x1.55258e6388789p-1","-0x1.d7e83b3eced26p+8","-0x1.a10d0a908ca5ap+7"],["-0x1.0663f5aade481p+1","-0x1.d7e736483aad5p+8","-0x1.a10d0a908ca5ap+7"],["0x1.7590e68530f81p+0","-0x1.e30a33ac78314p+8","-0x1.08aee6c94ff46p+7"],["-0x1.26116b81ed2dap+1","-0x1.e3095e133fd1cp+8","-0x1.08aee6c94ff46p+7"],["0x1.26a6b88ebbf84p+1","-0x1.e2ceccf667847p+8","-0x1.d0329f12fb232p+5"],["-0x1.3f4cc92f578bbp+1","-0x1.e2ce8e464c15ap+8","-0x1.d0329f12fb233p+5"],["0x1.6bbbe4a284ddfp+0","-0x1.d7877fe6d89cbp+8","0x1.e11ada13b52e2p+3"],["-0x1.0df61891e57a7p+2","-0x1.d78337b368424p+8","0x1.e11ada13b52e2p+3"],["0x1.4d68123e74f69p+1","-0x1.bf9e0768755fep+8","0x1.6bf2e5ff8fa87p+6"],["-0x1.c4006dd2a79eep+1","-0x1.bf9c673892b3ep+8","0x1.6bf2e5ff8fa87p+6"],["0x1.133be6abdabdep+2","-0x1.a4ad942f859f2p+8","0x1.3af73c98cdb8cp+7"],["-0x1.8720aceb0cccfp+0","-0x1.a4b27eeee997fp+8","0x1.3af73c98cdb8cp+7"],["0x1.4c3b55b7b6e53p+2","-0x1.7febcc613aa07p+8","0x1.b2dad0425020cp+7"],["0x1.cdf0d37f27c65p-2","-0x1.7ff4b6eb9eaddp+8","0x1.b2dad0425020cp+7"],["0x1.1d0b4f3761c16p+2","-0x1.53f92484027a6p+8","0x1.0c7a079b03dbbp+8"],["0x1.c8d3e75a11de7p-1","-0x1.54004fa0fb799p+8","0x1.0c7a079b03dbbp+8"],["0x1.0f8bfd56cc91ap+2","-0x1.1c9f4e7e43eafp+8","0x1.310a370b84c8ep+8"],["0x1.dbd2fd7175d07p+0","-0x1.1ca5d9425db90p+8","0x1.310a370b84c8ep+8"],["0x1.3423311f5d208p+2","-0x1.c49b3fa235d1fp+7","0x1.5062ff3dc63f2p+8"],["0x1.8f42f0f08e0a3p+1","-0x1.c4aa76c5a572ep+7","0x1.5062ff3dc63f2p+8"],["0x1.102f1482a7705p+2","-0x1.4bc07ed0c6663p+7","0x1.667416e7e61e6p+8"],["0x1.9b9e4d441d502p+1","-0x1.4bcc72e0c59ebp+7","0x1.667416e7e61e6p+8"],["0x1.046670706b9fbp+2","-0x1.a6998136cdcd1p+6","0x1.74772aaba924fp+8"],["0x1.9c996b1326a8cp+1","-0x1.a6b75faa130a3p+6","0x1.74772aaba924fp+8"],["0x1.4ea43f2a5559cp+1","-0x1.995f4b7e0474ep+5","0x1.7aaff959a8640p+8"],["0x1.4c4432a732044p-2","-0x1.99e5e0c85d173p+5","0x1.7aaff959a8640p+8"],["0x1.81d51e386d4a4p+4","0x1.491c1389b14e8p+7","-0x1.a27e96792cc59p+7"]]
Q=[tuple(F.from_float(float.fromhex(s)) for s in row) for row in Q_HEX]
# P0={x: q_i·x<=1 for all q_i}.
# Compute P0's exact uniform-volume centroid c by exact supporting-triple reconstruction
# and oriented face triangulation. Set B_i=q_i/(1-q_i·c).
# Then polar({B_i})=P0-c, hence its uniform-volume centroid is exactly (0,0,0).
```

This is the complete irredundant 62-row raw Q source; all rows are exact hull vertices. Source SHA-256: `c7bc9001542a75095e1b1a9a00e5ef181f886b36bb8957d3c2f38ba8aa806aca`. Exact reconstruction record SHA-256: `9926307abd4f5c4e7ca0f491d7202dc1d9625bea409bd1d9b6ef63bb6baf0ba4`.

## Realized body and centroid

- P: `(V,E,F,C)=(120,180,62,360)`; Q: `(V,E,F)=(62,180,120)`.
- Euler checks: `120-180+62=2`, `62-180+120=2`.
- Final uniform-volume centroid: **exactly `(0,0,0)`** by the projective identity above.
- Exact volume is independently recomputed as a Fraction; decimal `2.5756203370543456e-07`.
- Pre-gauge centroid approximately `(-0.00047662631296887701,1.9718307714492013e-05,6.3191977162742512e-05)`.
- Minimum projective denominator `0.93509232132148479`.
- Exact integer-orientation rebuild proves all 120 triangular Q facets supporting, all 180 true Q edges two-sided, all 62 Q rows extreme, and the complete dual P lattice.

Complete active data: [exact record](sandbox:/mnt/data/postladder62_handoff/endpoint/postladder62_exact.json), [P vertices](sandbox:/mnt/data/postladder62_handoff/endpoint/P_vertices.csv), [Q vertices](sandbox:/mnt/data/postladder62_handoff/endpoint/Q_vertices.csv), [all maximal face cycles](sandbox:/mnt/data/postladder62_handoff/endpoint/maximal_faces.json), [all true edges with dual incidence](sandbox:/mnt/data/postladder62_handoff/endpoint/true_edges.csv).

## Required realized branch architecture

Both inherited ascent capabilities remain actual strict Q-edge chains:

- `[1,2,3,4,5,6,7,8,9,10,11,12,13,14,0]`, minimum normalized ascent `0.003754217372457106`;
- `[15,16,17,18,19,20,21,22,23,24,25,26,27,28,0]`, minimum `1.763612928820534e-5`.

Two independent complete counter-moment channels are also actual Q-edge chains:

- `[29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]`;
- `[30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60]`.

The independent exact verifier checks every listed link against the reconstructed true-edge set and proves every main-branch ascent numerator strictly positive.

## Exhaustive equilibrium audit

The complete directed audit over all 62 maximal faces, 120 actual vertices, and 180 true edges/full two-face normal cones gives exactly:

- sole stable face: Q row `30`, normalized margin `+0.0004712160788141544`;
- protected unstable vertex: Q-facet incidence `(22,38,40)`, margin `+0.1806149049130755`;
- residual extra unstable vertex: incidence `(6,43,45)`, margin `+0.029878571258108777`;
- sole saddle: Q edge `(17,30)`, full-cone margin `+0.03404474554677195`.

Closest strict exclusions:

- face row `26`: `-4.834656625561157e-8`;
- vertex incidence `(16,17,30)`: `-9.949538113072635e-6`;
- edge/full cone `(16,30)`: `-3.3281489765277794e-5`.

Every other feature is strictly excluded. Exhaustive signed tables and exact/raw limiting witnesses are [face_audit.csv](sandbox:/mnt/data/postladder62_handoff/endpoint/face_audit.csv), [vertex_audit.csv](sandbox:/mnt/data/postladder62_handoff/endpoint/vertex_audit.csv), and [edge_audit.csv](sandbox:/mnt/data/postladder62_handoff/endpoint/edge_audit.csv).

## Incidence separation and perturbation certificate

At the central source, normalized inactive separations are `P=3.7635120400972648e-09` and `Q=0.00055671339335943391`. The P normalized value is below the preferred `1e-5`, so I do not claim that stronger scale.

A 120-digit outward-rounded proof certifies an independent source-coordinate box

`||δq||∞ <= 2^-28 = 1/268435456 = 3.7252902984619140625e-9`,

throughout which the complete P/Q lattices and strict class `(1,2,1)` remain fixed after exact projective centering. Directed positive lower bounds are:

- pre-gauge raw nonincidence `0.0000014251853869115413101565`;
- post-gauge raw nonincidence `0.0000010340419797552774394188`;
- oriented six-volume `4.31133871274602449002436775242359184766100629202743451166579907879331864565635280583830267081447974006299268791836820111E-13`;
- projective denominator `0.93509205851728477583491789856`;
- face sign `0.000002489643275614915124701`;
- vertex sign `3.393454881547169909533056030E-11`;
- full edge-cone sign `1.254201291316080672872272111E-10`.

Certificate: [interval_certificate.json](sandbox:/mnt/data/postladder62_handoff/endpoint/interval_certificate.json); directed verifier: [verify_interval.py](sandbox:/mnt/data/postladder62_handoff/endpoint/verify_interval.py).

## Complete topology-changing continuation

This assignment adds **69 material incidence changes** after `longstrip_rec0`; it does not double-count the inherited 255.

### 1. Two-channel replacement — 64 material crossings

The old 16-row counterbranch is replaced by two communicating 16-row sheets. The complete compressed class sequence is:

`(2, 4, 4) -> (2, 5, 5) -> (2, 6, 6) -> (2, 7, 7) -> (3, 8, 9) -> (4, 8, 10) -> (5, 8, 11) -> (6, 8, 12) -> (7, 8, 13) -> (8, 8, 14) -> (7, 8, 13) -> (6, 8, 12) -> (5, 8, 11) -> (4, 8, 10) -> (3, 8, 9) -> (2, 8, 8) -> (2, 7, 7) -> (2, 6, 6) -> (2, 5, 5) -> (2, 4, 4) -> (2, 3, 3) -> (1, 3, 2)`.

All old counter rows `29..44` deactivate. Decisive deactivation events in union-label coordinates:

- t=0.25457: [44]; circuit=[0, 14, 43, 44]
- t=0.501236666666667: [43]; circuit=[0, 1, 3, 14, 16, 17, 29, 30, 41, 42, 43, 45, 46, 47, 48, 71, 72, 73, 74]
- t=0.50457: [30, 42]; circuit=[13, 14, 15, 16, 29, 30, 31, 32, 36, 37, 38, 39, 40, 41, 42, 46, 47, 48, 49, 50, 51, 52, 61, 62, 63, 64, 65, 66, 69, 70, 71, 72, 73, 74]
- t=0.511236666666667: [29, 31, 32, 41]; circuit=[1, 15, 29, 31, 32, 33, 34, 35, 36, 39, 40, 41, 45, 46, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68, 69, 70, 71, 72]
- t=0.51457: [33, 36, 37, 38, 40]; circuit=[17, 18, 19, 33, 36, 37, 38, 40, 46, 53, 54, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
- t=0.517903333333333: [34, 35]; circuit=[34, 35, 55, 56, 57, 58, 59, 60]
- t=0.52457: [39]; circuit=[5, 6, 39, 55, 57, 65, 66, 67, 68]

### 2. Stellar U-H cancellation — one crossing

Facets `(2,3,17),(2,16,17)` are replaced by `(2,3,61),(2,16,61),(3,17,61),(16,17,61)` across circuit `{2,3,16,17,61}`; the strict class changes `(1, 3, 2) -> (1, 2, 1)`.

### 3. Reopening/polish — four 2-2 flips

Circuits `{20,21,50,52}`, `{23,24,62,64}` in union labels, `{5,6,55,57}`, and `{5,6,57,59}`; all retain `(1,2,1)`.

Every checkpoint contains its actual rebuilt incidence, f-vectors, active/deactivated rows, and reidentified complete equilibrium set. [Full topology ledger](sandbox:/mnt/data/postladder62_handoff/search/topology_circuit_ledger.json); [independent replay](sandbox:/mnt/data/postladder62_handoff/search/rebuild_topology_circuit_ledger.py).

## Smallest surviving connected obstruction

The old counterbranch stable source and four-rung ladder are gone. The final residual is one U-H pair:

- extra U facet `(6,43,45)`;
- saddle Q edge `(17,30)`, with endpoint facets `(16,17,30)` and `(17,18,30)`.

The shortest actual Q-facet path to the nearer saddle endpoint is

`(6,43,45)->(5,6,43)->(5,6,19)->(5,18,19)->(18,19,30)->(17,18,30)`.

The complete two-separatrix disk has boundary cycle `6-45-43-5-18-17-16-30-20-6` and triangles

`(6,43,45),(5,6,43),(5,6,19),(5,18,19),(18,19,30),(17,18,30),(16,17,30),(6,19,20),(19,20,30)`.

A one-sided strip leaves the alternative `6-19-20-30` route. Patches reaching the saddle without replacing both endpoint stars create a new unstable facet on the inserted cell. The next nonredundant operation is a finite-width `2×k` zipper/annulus replacing both separatrices and both saddle endpoint stars together, allowing `(5, 6, 16, 17, 18, 19, 20, 30, 43, 45, 61)` or descendants to deactivate. [Residual mechanics record](sandbox:/mnt/data/postladder62_handoff/search/residual_obstruction.json).

## Search delimited honestly

Beyond the inherited 12,000 complete evaluations, this continuation performed conservatively **more than 8,000 additional full hull/own-centroid evaluations** over two-channel profiles, stellar depth, two-cell and basin-depth patches, free supports, insertion/deletion cascades, determinant-one metrics, channel widths/twists, and sequential all-feature directions.

No own-centroid `(1,1,0)` state occurred. A sequential direction reduced the worst residual from `0.03404` to about `0.02453`, but the full class expanded to `(9,5,12)`, directly exposing transfer rather than cancellation. Several raw-origin apparent `(1,1,0)` states were rejected because exact own-centroid gauging displaced the center by about `0.54–0.86` or the intended chains were not actual strict hull-edge chains. These nonhits are empirical, not a global impossibility theorem. [Search report](sandbox:/mnt/data/postladder62_handoff/search/search_report.json).

## Verification, meshes, and reproduction

Independent result:

```json
{"verified":true,"P_f_vector":[120,180,62],"Q_f_vector":[62,180,120],"exact_final_centroid":["0","0","0"],"class_directed":[1,2,1],"stable_rows":[30],"unstable_incidence":[[6,43,45],[22,38,40]],"saddle_Q_edges":[[17,30]],"all_required_main_and_channel_edges_true":true,"all_main_ascent_numerators_exact_positive":true,"interval_box_power":28}
```

- [Exact independent verifier](sandbox:/mnt/data/postladder62_handoff/endpoint/verify_exact_independent.py)
- [Verifier transcript](sandbox:/mnt/data/postladder62_handoff/endpoint/verify_exact.log)
- [P OBJ](sandbox:/mnt/data/postladder62_handoff/endpoint/postladder62_P.obj) / [P STL](sandbox:/mnt/data/postladder62_handoff/endpoint/postladder62_P.stl)
- [Q OBJ](sandbox:/mnt/data/postladder62_handoff/endpoint/postladder62_Q.obj) / [Q STL](sandbox:/mnt/data/postladder62_handoff/endpoint/postladder62_Q.stl)

```bash
unzip postladder62_handoff.zip
cd postladder62_handoff/endpoint
python verify_exact_independent.py
python verify_interval.py --power 28
cd ../search
python rebuild_topology_circuit_ledger.py
cd ..
sha256sum -c SHA256SUMS.txt
```

Complete archive: [postladder62_handoff.zip](sandbox:/mnt/data/postladder62_handoff.zip)  
SHA-256: `3753435c02fdd833591483feb78d7ba9c43fa811da9907077d8e08e78d596b06`  
[README](sandbox:/mnt/data/postladder62_handoff/README.md) · [manifest](sandbox:/mnt/data/postladder62_handoff/MANIFEST.json)

## Final determination

The requested wide coupled surgery was realized and certified, reducing the exact own-centroid class from `(2,4,4)` to `(1,2,1)`. The last U-H pair survives. **An actual homogeneous convex polyhedral Gömböc was not constructed.**
