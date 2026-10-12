# figure-0072

AI research report · 2026-08-26 UTC

---

# Verdict

No finite homogeneous polyhedral Gömböc was obtained. I therefore do **not** claim a winner. The required gate remains the exact own-centroid class `(S,U,H)=(1,1,0)` with a complete finite lattice, strict all-feature margins, independent verification, and matching mesh export; near-states and artificial reference centers are explicitly excluded. :contentReference[oaicite:0]{index=0}

The strongest completed object from this direction is a fully materialized, exactly centered rational Sloan-support polyhedron

```text
P28 = { y in R^3 : A_i · y <= 1, i=0,...,27 }
```

with

```text
(F,E,V) = (28,78,52),   C=V+E+F-2=156,
exact uniform-volume centroid = (0,0,0),
exact strict equilibrium class = (3,2,3).
```

It is a genuine ordinary uniform-density polyhedron, not a weighted point model. Its complete exact H/V data, maximal-face cycles, true edges, exact moment identity, exact equilibrium witnesses, independent verifier, perturbation certificate, OBJ, and STL are in the attached bundle.

# What changed relative to the supplied journal

The journal had isolated the original Sloan phase at `beta=0.034` as analytically centered and strictly convex with two smooth equilibria, while showing that denser quasi-uniform polyhedralization does not solve the feature-level equilibrium problem. :contentReference[oaicite:1]{index=1} It also recorded that finite rank-three moment actuation was already practical but that the noncritical support network remained the obstruction. :contentReference[oaicite:2]{index=2} The exact degree-one-moment-annihilating support/cubature architecture requested here was still explicitly absent. :contentReference[oaicite:3]{index=3}

This run adds four reusable results:

1. A compact finite Sloan-flow support architecture was reduced to 28 active supports and exactified without losing its lattice or strict feature signs.
2. Its three uniform-volume first moments were solved **exactly** by finite maximal-face tetrahedral cubature and exact rational support renormalization; the final moment is literally `(0,0,0)`.
3. A standard-library verifier independently reconstructs the full face lattice and audits every maximal face, actual vertex, true edge, and full edge/vertex normal cone with exact `Fraction` arithmetic.
4. The residual failure was localized to one connected Euler-neutral six-feature block, and a structural reason was found for why one-sided support-witness chains transfer rather than cancel that block after the body's own centroid is recomputed.

# Exact finite object and deterministic generator

The discovery seed used three nonuniform Sloan gradient-flow support chains between a dedicated three-plane unstable fan and a dedicated stable plane:

```text
K=3
fan radius rho=0.24
longitudinal step=0.09
phase twist=0.137
phase offset=0.17
stable cutoff psi=-0.96
```

After support optimization and exact active-row culling, the retained source-row IDs are

```text
1 3 8 15 16 17 18 22 25 28 30 32 37 39
40 41 43 44 46 60 61 62 63 64 65 66 68 69
```

The compact generator stores every base row as an integer triple over the common denominator `2^40`, together with all 52 active triples. It then reconstructs, with rational arithmetic only:

- all 52 vertices as exact 3-by-3 support-plane intersections;
- all 78 true edges from exact active-set intersections;
- every maximal-face boundary cycle;
- the exact volume, first moment, and centroid;
- the final exactly centered support-one rows;
- OBJ and STL exports.

The generator imports no hull or geometry library. A regeneration test confirms that it reproduces the certificate's exact H rows, exact V rows, true-edge/face incidence, maximal-face boundaries, and exact volume.

# Exact degree-one moment mechanism

Let `b_i · x <= 1` be the 28 dyadic base supports and let each exact vertex be the intersection of its certified active triple. Triangulate each **maximal** face by a fan from its certified boundary cycle. For every outward-oriented boundary triangle `T=(v_a,v_b,v_c)`, define

```text
V = (1/6)  sum_T det(v_a,v_b,v_c)
M = (1/24) sum_T det(v_a,v_b,v_c) (v_a+v_b+v_c).
```

This is the exact uniform-volume tetrahedral cubature of the polyhedron; no external weights or point masses are introduced. All terms are rational. Set

```text
c = M/V,
h_i = 1 - b_i · c,
A_i = b_i/h_i,
y = x-c.
```

Then the translated body is exactly `A_i · y <= 1`, and its first moment is the algebraic identity

```text
M' = M - Vc = 0.
```

For this object the dyadic rounding residual before the final exact translation was only

```text
c ≈ ( 6.5688790540e-13,
     -1.0143513159e-12,
     -1.7340555046e-12 ).
```

Thus the exact moment solve is a microscopic chamber-preserving correction, not a macroscopic recentering that hides the mechanics. The exact certificate contains the full rational volume, every rational H/V coordinate, and literal zero first-moment numerators.

# Complete lattice and exact centroid certificate

The independent verifier reports

```text
V-E+F = 52-78+28 = 2
exact first moment = (0,0,0)
exact centroid = (0,0,0)
volume ≈ 9.32256501656886
minimum raw inactive H/V slack ≈ 9.900138154927962e-5
certificate SHA-256 = 2221ede59575c76a712dbb3d31c632af41d3e69794761149f83d3a45afd1bd11
```

Every vertex is checked against all 28 inequalities: its three reported active rows vanish exactly and every other slack is strictly positive. Maximal-face cycles reconstruct the same 78 undirected edges as the supplied true-edge table, and every edge belongs to exactly two maximal faces. The volume integration uses those maximal faces rather than triangulation-piece adjacency or tolerance merging.

# Exhaustive equilibrium audit

At the exact own centroid, the strict class is

```text
(S,U,H) = (3,2,3),  with S+U-H=2.
```

## Stable maximal faces

| Face | Source row | Role | Normalized strict margin |
|---:|---:|---|---:|
| 11 | 32 | unwanted | `0.013871756006739733` |
| 25 | 66 | unwanted | `0.013855551802533506` |
| 27 | 69 | intended stable face | `0.7904421746594743` |

For every other maximal face, the certificate supplies a specific support row that cuts its perpendicular foot with an exact negative rational witness. The closest face witness to zero over the complete face audit is approximately `-2.467011912576698e-4`.

## Unstable vertices

| Vertex | Active maximal faces | Role | Normalized full-normal-cone margin |
|---:|---|---|---:|
| 15 | `[2,18,27]` | unwanted | `0.0020411209100710845` |
| 39 | `[9,25,27]` | intended unstable vertex | `0.979616883426868` |

For every other vertex, a true incident edge has an exact negative radial derivative witness. The closest vertex witness to zero is approximately `-2.751257070734403e-6`.

## Saddle true edges

| Edge | End vertices | Incident maximal faces | Normalized strict margin |
|---:|---|---|---:|
| 46 | `[31,39]` | `[9,25]` | `0.02089562220938679` |
| 56 | `[36,44]` | `[11,27]` | `0.04418205518296625` |
| 76 | `[39,51]` | `[25,27]` | `0.03936188598192747` |

For every true edge, the verifier computes the exact line-projection parameter `t` and both coefficients in the complete two-face normal cone. A saddle requires all four quantities `t`, `1-t`, `lambda_0`, and `lambda_1` to be positive. Every nonsaddle edge has a recorded exact negative limiting component. The closest edge witness to zero is approximately `-4.532019622088206e-3`.

# Certified perturbation radius

A separate outward-rounded interval verifier proves an actual open coefficient box. In the final support-one parameterization, perturb all 84 row coefficients independently by

```text
|delta A_ij| <= 1e-11,
```

keep every support constant equal to one, reconstruct vertices from the same active triples, recompute the body's uniform-volume centroid, and audit equilibria at that new own centroid. Over the entire box, not merely at sampled points, it proves:

```text
same complete face lattice and true-edge list;
minimum inactive-slack lower bound = 9.900077806257455e-5;
minimum oriented tetrahedron determinant lower bound = 3.958108186431774e-5;
minimum equilibrium-sign lower bound = 1.110826943112857e-6;
class remains exactly (3,2,3).
```

The next tested box, `2e-11`, was inconclusive because interval dependency made the weak extra-unstable-vertex witness straddle zero; this is not evidence that `2e-11` is actually unsafe.

# Search performed and failure modes

## Dense tangent supports

Own-centroid audits of ordinary Fibonacci tangent sets reproduced the density failure sharply:

```text
N=32:  (S,U,H)=(32,53,83)
N=64:  (64,100,162)
N=128: (121,189,308)
N=256: (214,284,496)
N=512: (377,463,838)
```

An adaptive separator-cut loop also grew the number of equilibria while adding supports. This confirms that the missing ingredient is not surface accuracy.

## Directed Sloan-flow supports

Replacing isotropic sampling by three directed gradient-flow chains changed the topology qualitatively. A 70-row seed reached `(4,3,5)`; support optimization and inactive-row removal produced the 28-facet `(3,2,3)` body exactified here. This is the first compact object in this branch for which moment closure, lattice reconstruction, and every feature sign were all carried through exactly.

## Fixed-lattice cancellation

For the 28-facet lattice, linearized programs can simultaneously point toward cutting faces 11 and 25, reversing the weak extra vertex, and reversing the three saddle components. Nonlinear sequential continuation does not realize all six sign changes inside that lattice: its raw inactive slack collapses at a circuit, and full hull rebuilding transfers the block through `(3,3,4)` and `(3,4,5)` cells.

## Row deletion and insertion

All single-row deletions and targeted combinations around the defect block failed to reduce the saddle count below three. Thousands of one-row insertions did not improve `H`. Two-row insertions reduced the sum of positive saddle margins from roughly `0.1044` to roughly `0.0306`, but did so by splitting old saddles into new small-`lambda` saddles; the two extra stable faces survived. Those near-wall bodies were not exactified because the 28-facet object is smaller, more robust, and fully certified.

# Localized topology obstruction

The entire unwanted set is one connected Euler-neutral block attached to the intended critical features:

```text
extra stable faces: 11 and 25
extra unstable vertex: 15 on [2,18,27]
extra saddle edges: 46=[9,25], 56=[11,27], 76=[25,27]

Delta S + Delta U - Delta H = 2 + 1 - 3 = 0.
```

There is also a useful exact obstruction for one-sided support-witness chains. In support-one gauge, the perpendicular foot of face `i` is `a_i/||a_i||^2`. If row `j` cuts that foot, then

```text
a_j · a_i > ||a_i||^2.
```

Cauchy-Schwarz therefore gives `||a_j||>||a_i||`. Witness arrows strictly increase row norm, so they cannot form cycles; every finite directed foot-elimination network must terminate at sink faces. This explains why a directed chain can eliminate chosen faces relative to a fixed reference point.

The decisive failure occurs after uniform-volume recentering: the inserted chain has a nonzero degree-one volume moment, moves the body's own centroid, and changes the face-foot and normal-cone inequalities globally. Companion chains tried without hard moment balance produced new stable faces, unstable vertices, and saddles. The obstruction is therefore not “centroid calculation” and not “insufficiently many supports.” It is the absence of a **topology-changing witness network whose three volume moments cancel identically while the target normal fan is preserved**.

# Most useful continuation

The next nonredundant construction should replace the whole connected defect subcomplex, not add another isolated row. A concrete continuation is:

1. Preserve intended stable face 27 and the intended apex/unstable vertex 39.
2. Replace simultaneously the neighborhoods of face 25 with edges `[9,25]` and `[25,27]`, and face 11 with edge `[11,27]`, while also removing the extra vertex on `[2,18,27]`.
3. Use a paired asymmetric double-Y support patch whose two tetrahedral volume-moment contributions are algebraically coupled; retain three additional mechanically inactive support variables with a full-rank moment Jacobian.
4. Solve the three exact first-moment equations as hard constraints **during** each circuit transition, instead of translating only after topology discovery.
5. Enumerate the adjacent active-triple cells explicitly and require raw inactive slack above `1e-5` before any metric polishing.
6. Exactify only a strict `(1,1,0)` chamber, using the generator/verifier framework in this bundle unchanged.

The exact P28 object is a useful seed because it is compact and fully reconstructible, but its certified `1e-11` chamber proves that no infinitesimal arithmetic polish can alter the class. A successful continuation must cross a genuine incidence circuit with moment balance built into the patch.

# Reproducible artifacts

- [Complete bundle, including exact data, generator, verifiers, transcripts, OBJ and STL](sandbox:/mnt/data/sloan_cubature_fallback_bundle.zip) — bundle SHA-256 `d83a5ac7bc092ea7db9e135ee4fecc0314275ec1cfb417c301a91ec1198ba00e`.
- [Exact full certificate](sandbox:/mnt/data/sloan_cubature_fallback/fallback_exact.json)
- [Compact deterministic exact generator](sandbox:/mnt/data/sloan_cubature_fallback/generate_exact.py)
- [Independent exact verifier](sandbox:/mnt/data/sloan_cubature_fallback/verify_exact.py)
- [Directed-rounding perturbation verifier](sandbox:/mnt/data/sloan_cubature_fallback/verify_interval_radius.py)
- [Exact H rows](sandbox:/mnt/data/sloan_cubature_fallback/H_exact.csv)
- [Exact V rows](sandbox:/mnt/data/sloan_cubature_fallback/V_exact.csv)
- [Maximal-face cycles](sandbox:/mnt/data/sloan_cubature_fallback/faces.txt)
- [True-edge list](sandbox:/mnt/data/sloan_cubature_fallback/edges.txt)
- [OBJ export](sandbox:/mnt/data/sloan_cubature_fallback/fallback_exact.obj)
- [STL export](sandbox:/mnt/data/sloan_cubature_fallback/fallback_exact.stl)
- [Exact verification transcript](sandbox:/mnt/data/sloan_cubature_fallback/verification.txt)
- [Interval-radius certificate](sandbox:/mnt/data/sloan_cubature_fallback/interval_radius.json)
- [Bundle README and reproduction notes](sandbox:/mnt/data/sloan_cubature_fallback/README.md)

Reproduction commands from the extracted directory are:

```bash
python generate_exact.py
python verify_exact.py
python verify_interval_radius.py
```

`verify_exact.py` imports only Python's standard library and independently returns `PASS_EXACT_FALLBACK_NOT_GOEMBOC`.
