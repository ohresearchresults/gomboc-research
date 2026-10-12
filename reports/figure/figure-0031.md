# figure-0031

AI research report · 2026-08-22 UTC

---

# Verdict

No already-published **finite homogeneous polyhedral Gömböc** was recovered from the accessible 2026 repository/archive surface. I did, however, obtain the strongest concrete substitute the sources permit: complete coordinate and facet data for **five independent 25,600-triangle rational polyhedra** reconstructed from every smooth-family parameter point that the May 2026 amendment labels verified, followed by a fresh exact audit of the uniform-volume centroid and every face, vertex, and edge equilibrium. This directly tests the transcript's unresolved proposal that one of the reported high-resolution meshes might already be an explicit homogeneous polyhedral Gömböc, though it does not replace an audit of byte-identical official assets. :contentReference[oaicite:0]{index=0}

All five fail decisively. The strongest and most extensively cross-checked finite candidate, **Phase-1**, has

`(S,U,H) = (2296, 2302, 4596)`,

not `(1,1,0)`. Here `S` is the number of stable face equilibria, `U` the number of unstable vertex equilibria, and `H` the number of saddle-edge equilibria. Every decision is the sign of an arbitrary-precision integer expression; no tolerance or floating-point threshold is used.

## Concrete coordinate assets

- [Five-mesh coordinate, facet, OBJ, exact-audit, and regeneration package](sandbox:/mnt/data/gomboc_2026_five_mesh_exact_audit.zip)  
  SHA-256: `94e515ea768edb5d830ded443a4ebc8ef18420788a7cdbc70867a11af9e17bbd`
- [Standalone Phase-1 exact-audit package](sandbox:/mnt/data/gomboc_phase1_exact_audit_bundle.zip)  
  SHA-256: `9711f1357d12ff5f45080bd54664a9ae9473096c0b1f79cd78ae5a57418ac591`
- [Machine-readable five-mesh summary](sandbox:/mnt/data/five_mesh_exact_audit_summary.json)  
  SHA-256: `0976ed0bda7a735150570a024dc9724195f5104f41fc9fd31c102674697a4977`
- [Independent exact verifier for stored coordinate/facet tables](sandbox:/mnt/data/verify_mesh_exact_from_tables.py)  
  SHA-256: `0d4c21a1a46cc91292fb76c6b22af5a6ee2da0495de7a9f1bcabd07fe5c847f1`
- [Deterministic Phase-1 reconstructor and exact verifier](sandbox:/mnt/data/reconstruct_phase1_audit.py)  
  SHA-256: `323cf2e8a6f363de0d219f8722b0679ca9dd28f9dd2d2fd1d5b0c70274dfb9b8`

Both ZIP archives pass complete decompression tests. The five-mesh archive contains a `SHA256SUMS.txt` manifest, all integer coordinate tables, zero-based outward-oriented facet tables, decimal OBJ files, full exact audit JSON, equilibrium index sets, regeneration scripts, and a one-command rerun.

## What was reconstructed

The May 23, 2026 amendment gives the smooth radial family

`r^4 = 1 + 4 beta sin(theta) cos(phi - P(theta))`,

with

`P(theta) = eta(theta) + a sin(k eta(theta))`

and

`eta(theta) = (3 pi / 2)(cos(theta) - cos(theta)^3 / 3)`.

It identifies Phase-1 and four further interior parameter points as smooth mono-monostatic bodies. Importantly, its classifier explicitly uses analytical Gaussian-curvature and radial-critical-point calculations and says it uses **no mesh-vertex computation**. Thus its smooth claim is not an equilibrium certificate for any particular finite STL or triangulation. :contentReference[oaicite:1]{index=1}

For each of the five published parameter points, I used the same deterministic finite convention:

- north pole;
- 80 interior latitude rings at `theta = i*pi/81`, `i=1,...,80`;
- 160 longitudes per ring at `phi = 2*pi*j/160`, `j=0,...,159`;
- south pole;
- high-precision evaluation of the closed form;
- rounding each Cartesian component to 12 decimal places;
- interpreting the printed decimal **exactly** as an integer divided by `10^12`;
- taking the convex hull to select the outward triangular combinatorics.

This yields 12,802 vertices and 25,600 triangles in each case. Qhull is used only to select combinatorics. It is not trusted for the centroid, topology, convexity signs, or equilibrium classification.

Independent high-precision reruns produced identical rounded coordinate tables and positive separation from every rounding half-grid. Therefore each supplied decimal table defines an unambiguous rational polyhedron.

## Complete exact audit

| case | exact published parameters `(k,beta,a)` | exact-centroid x-coordinate, approximately | S | U | H | `S+U-H` |
|---|---:|---:|---:|---:|---:|---:|
| Phase-1 | `(1,0.023149,0.234433)` | `-2.696210169236485e-3` | **2296** | **2302** | **4596** | 2 |
| k=2 near boundary | `(2,0.0321,0.025)` | `-3.317751533410527e-6` | **926** | **870** | **1794** | 2 |
| k=2 deeper | `(2,0.025,0.050)` | `-2.325176550813410e-6` | **1452** | **1396** | **2846** | 2 |
| k=3 interior | `(3,0.025,-0.025)` | `-2.353576520464517e-6` | **1454** | **1398** | **2850** | 2 |
| k=3 deeper | `(3,0.020,-0.050)` | `-1.923983023307160e-6` | **2652** | **2644** | **5294** | 2 |

Every row independently verifies:

- `V=12802`, `E=38400`, `F=25600`;
- Euler characteristic 2;
- a connected face-adjacency graph;
- exactly two incident faces per edge;
- cyclic vertex links;
- a closed combinatorial sphere;
- strict exact hinge convexity;
- zero degenerate face, vertex, or edge predicates.

A second verifier reloads the stored coordinate and face tables and recomputes everything from scratch. It agrees with the first pass in every case.

## Phase-1 exact data and robustness

The exact uniform-volume centroid of the Phase-1 rational polyhedron is

`Cx = -135405543809271403483271749439298431998215671627 / 50220693236097257964612347280157035744000000000000`,
`Cy = Cz = 0`.

Its volume is approximately `4.18505776967477`. Its smallest positive raw exact hinge slack is

`115358436054007095743794`,

and no hinge or equilibrium predicate is zero.

Its coordinate/facet identities are fixed by these hashes:

- integer vertex table: `0c22400853e89657fca8e43d1dc26f7e1d5f774e15e85ce91c9150473658d0c9`
- face table: `b4176ff2a5baf3dfa1480d48b2a19d0dce5f0bc0e6ccadff3031e372456422f0`
- OBJ: `028067c14641fa3ff3508b68cc623233d58ebffb4a5b783722890612218a9361`

The failure is not a fragile resolution artifact. Exact rational audits of Phase-1 at five resolutions give:

| grid | triangles | `(S,U,H)` |
|---|---:|---:|
| `40 x 80` | 6,400 | `(1720,1676,3394)` |
| `60 x 120` | 14,400 | `(2274,2214,4486)` |
| `80 x 160` | 25,600 | `(2296,2302,4596)` |
| `100 x 200` | 40,000 | `(1886,1840,3724)` |
| `120 x 240` | 57,600 | `(1846,1800,3644)` |

At the 80-by-160 resolution, rounding at every precision from 8 through 14 decimal places leaves the exact count unchanged at `(2296,2302,4596)`. Three naive fixed-diagonal latitude triangulations were additionally checked and were nonconvex, which is why the package uses the exact convex-hull boundary rather than an arbitrary diagonal convention.

## Exact verification method

For outward triangle vertices `a,b,c`, coordinate denominator `q`, and

`D = 4 * sum_f det(a_f,b_f,c_f)`,
`N = sum_f det(a_f,b_f,c_f) * (a_f+b_f+c_f)`,

the exact physical centroid is `C = N/(D*q)`.

The verifier then clears every denominator and evaluates only integer signs:

1. **Stable face:** the orthogonal projection of `C` onto the face plane lies strictly inside all oriented boundary edges.
2. **Unstable vertex:** for every adjacent vertex `w`, `(v-C) dot (w-v) < 0`.
3. **Saddle edge:** the projection of `C` onto the edge line lies strictly inside the segment, and the direction toward `C` lies strictly inside the cone determined by the two adjacent face normals.
4. **Convexity:** the two opposite vertices across every edge lie strictly on the appropriate interior sides of the neighboring face planes.
5. **Topology:** manifold incidence, connectedness, vertex-link cycles, and Euler characteristic are checked combinatorially.

The equality `S+U-H=2` is recovered in all five audits without any zero predicate.

## Provenance and the missing official bytes

The primary repository release is tag `v1.0.0`, commit `fdcfe9a9b3a203152d1fa83a144ecf62556d929d`. Its release notes associate the Gömböc and catalog work with version-specific Zenodo records `10.5281/zenodo.20674391` and `10.5281/zenodo.20674394`. :contentReference[oaicite:2]{index=2}

The currently visible `main` tree reports 21 commits and does not expose the paper-claimed `gomboc_family/v2/` directory or a visible `meshes/` directory, although the README's schematic repository layout mentions meshes. :contentReference[oaicite:3]{index=3} The DOI redirects and archive bytes could not be retrieved in this runtime. Consequently, the supplied meshes are deterministic independent reconstructions from the published formula and parameters; I do **not** assert byte identity with an official STL.

The amendment itself retracts the old “thirteen verified mono-monostatic bodies” framing, leaving one Phase-1 point from the original catalog and four new smooth-family interior points relevant here. :contentReference[oaicite:4]{index=4}

## Exact recovery path for official assets

On an unrestricted network, query:

```text
https://zenodo.org/api/records/20674391
https://zenodo.org/api/records/20674394
https://zenodo.org/api/records/20674391/files-archive
https://zenodo.org/api/records/20674394/files-archive
https://zenodo.org/api/records/<record-id>/files/<filename>/content
```

Then inspect the complete Git history, branches, tags, and unreachable objects:

```bash
git clone --mirror https://github.com/gyapaganda-a11y/substrate-geometry.git
git --git-dir=substrate-geometry.git log --all --name-status -- \
  gomboc_family meshes '*.stl' '*.obj'
git --git-dir=substrate-geometry.git fsck --full --no-reflogs --unreachable
```

Any recovered ASCII decimal mesh should be interpreted as an exact rational polyhedron. Any binary STL should be interpreted exactly using its IEEE-754 dyadic coordinates. After orienting and validating the closed boundary, run the included verifier; an ECS drainage-basin score is not a substitute for the finite face/vertex/edge equilibrium audit.

## Bottom line

The actual coordinate data are now available and exactly audited. They establish a strong negative result:

> The five natural 25,600-triangle finite polyhedra reconstructed from every verified 2026 smooth-family parameter point are **not** homogeneous polyhedral Gömböcs; all possess hundreds or thousands of stable, unstable, and saddle equilibria.

This does not contradict the smooth-body classification. It shows that a high-resolution inscribed triangulation does not inherit the smooth body's two-equilibrium structure. The only unresolved asset-level possibility is that an official archived STL uses materially different coordinates or combinatorics; such a file must be recovered and audited separately.
