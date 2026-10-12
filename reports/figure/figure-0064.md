# figure-0064

AI research report · 2026-08-25 UTC

---

# Literal finite Sloan–Lángi construction: completed handoff

## Verdict

I did **not** obtain a homogeneous polyhedral Gömböc with strict own-centroid class `(S,U,H)=(1,1,0)`. The acceptance gate therefore remains unmet: a centered finite body with many genuine equilibria is not a near-certified winner merely because its centroid and actuator equations close. The run journal explicitly excludes a smooth body, a near-solution, an artificial reference point, or an unexpanded theorem from counting as the requested object. :contentReference[oaicite:0]{index=0}

What this continuation does supply is the requested fallback artifact in full: a **materialized moderate-size finite local-patch construction**, dedicated stable and unstable neighborhoods, four disjoint moment actuators with an exact rank-three Jacobian certificate, complete H/V data and incidence, a common strict separator for every non-equilibrium maximal face and every complete mixed edge/vertex normal cone, an independent verifier, and OBJ/STL exports. It also isolates the exact remaining failure rather than hiding it.

## 1. Source construction implemented

I used the Sloan radial body

```text
r(theta,phi)^4 = 1 + 4 beta sin(theta) cos(phi-eta(theta)),
eta(theta) = (3 pi / 2)(cos(theta)-cos(theta)^3/3),
beta = 0.023.
```

The 2026 source reports a Krawczyk/interval equilibrium count `(1,1,0)` with no undecided boxes for this parameter value, while also stating its caveat that the centroid is supplied to the interval counter as a point value rather than a rigorous interval enclosure. :contentReference[oaicite:1]{index=1}

The finite construction follows the three geometric stages in Lángi’s proof rather than replacing them with a quasi-uniform tangent mesh: four noncritical moment-control cones, dedicated local replacements around stable/unstable equilibria, and shifted supporting patches on the remaining boundary. Lángi explicitly warns that generic equidistant fine approximations can create more equilibria; his theorem instead preserves the smooth equilibrium class by topology-aware local truncations and centroid correction. :contentReference[oaicite:2]{index=2}

The implementation differs from the failed uniform experiment in one essential way: noncritical supports are laid out along numerically integrated negative radial-gradient trajectories of the Sloan surface, then subjected to an exhaustive feature-level separator audit. This makes the patches anisotropic in the direction required by the smooth radial displacement instead of producing nearly isotropic tangent cells whose perpendicular feet fall inside them.

## 2. Main materialized finite construction

The final actuated polyhedron is supplied in both H- and V-representation. All coordinates are binary64 numbers; the stored V representation is centered at its integrated uniform-volume centroid.

| Quantity | Audited value |
|---|---:|
| Vertices `V` | 145 |
| True edges `E` | 245 |
| Maximal faces `F` | 102 |
| Mechanical complexity `V+E+F-2` | 490 |
| Uniform volume | `7.54257239898242` |
| Integrated centroid | `(-1.1620635830561232e-17, 4.8846428996622075e-17, -6.60205344688524e-17)` |
| Centroid norm | `8.294410029882471e-17` |
| Own-centroid class | **`(15,21,34)`** |
| Euler audit | `15+21-34=2` |

The independent verifier reconstructs the V-set from the H rows and obtains centroid norm `2.9195e-16`, f-vector `(145,245,102)`, and the same `(15,21,34)` class.

### Dedicated stable neighborhood

The intended stable patch is one deliberately inserted planar truncation, not a generic tangent sample:

- maximal face ID `56`;
- cycle `[22,23,14,13,0,5,6,2]`;
- outward normal numerically equal to `(-1,0,0)`;
- strict in-face equilibrium margin `0.11745060165263754`.

### Dedicated unstable neighborhood

The intended unstable neighborhood is a single-apex fan:

- apex vertex ID `139`;
- strict unstable margin `0.019179781936049845`;
- 39 fan-base neighbors;
- every apex-to-base generator has strictly decreasing squared distance from the origin away from the apex;
- minimum normalized endpoint monotonicity margin `0.01540396223575082`.

Thus neither target neighborhood is an accidental product of the noncritical support mesh.

## 3. Four disjoint moment actuators

Four pairwise vertex-disjoint triangular truncation faces were selected from non-equilibrium regions. Their source vertices are `[7,17,27,25]`; the new base cycles are respectively

```text
[26,25,24]
[48,47,46]
[31,16,30]
[29,28,27]
```

The balanced truncation fractions are

```text
[0.005,
 0.12534779,
 0.02114109,
 0.00570975].
```

Before adding the four cones, the truncated base has first moment

```text
(-3.578086518971768e-13,
 -8.004415393663003e-13,
  1.8119324876180293e-13).
```

For a triangular base with area `A_i`, support `h_i`, area centroid `w_i`, and cone-height parameter `tau_i`, the added first moment is represented as

```text
J_i y_i,
J_i = (A_i h_i/3) w_i,
y_i = tau_i + tau_i^2/4.
```

The full `3 x 4` Jacobian used in the solve is

```text
[[-3.4818355535409663e-08,  1.8125272746123025e-07,
   1.4868454571084966e-07, -2.9270144694959940e-08],
 [-3.0095557034279200e-07, -2.0580003196300604e-08,
   3.7393184071362845e-08,  3.0365008656729690e-07],
 [-1.0001565483421597e-06, -1.1482034625364096e-08,
  -1.3748174654060832e-08,  1.0061389518578057e-06]].
```

Its singular values are

```text
(1.481789641922986e-06,
 2.391234084045283e-07,
 4.119630375044582e-08),
```

so its numerical condition number is about `35.969` and its rank is three. A strictly positive null direction is

```text
(1,
 0.2772117974138427,
 0.09280577015319062,
 0.9984857577381363).
```

I retained one actuator degree of freedom as mechanical slack by choosing `lambda=0.0002` along this positive null direction. The positive moment variables and corresponding cone heights are

```text
y = (0.00020081515328448487,
     0.00004451250601893124,
     0.00003462521297007403,
     0.00020042214303841690)

tau = (0.00020080507261521774,
       0.00004451201068933486,
       0.00003462491324901507,
       0.00020041210178600720).
```

All four apices remain active and each is incident to exactly the three vertices of its own base.

### Exact rank-three certificate

The binary64 coordinates are exact dyadic rationals. Recomputing the four triangular-base columns with `Fraction` arithmetic gives four exact nonzero `3 x 3` minors. The best-conditioned minor, using columns `(1,2,3)`, is approximately

```text
1.011536060301534e-20
```

and is enclosed by

```text
[1.011536060291534e-20,
 1.011536060311534e-20],
```

which excludes zero. The other three exact minors also exclude zero. Full exact numerators and denominators are frozen in the incidence JSON. Thus the actuator Jacobian has certified rank three for the stored finite body, not merely a numerically guessed rank.

## 4. Complete common-separator audit

For every feature that is **not** an equilibrium, the verifier solves and stores one vector `d` and strict margin `gamma` satisfying

```text
d·q <= -gamma       for every point/vertex q of the whole exposed feature,
d·n_i >=  gamma      for every incident outward unit-normal generator n_i.
```

Because every vector in the complete normal cone is a nonnegative combination of its incident generators, one common `d` certifies the entire face–normal-cone pair; it is not a facetwise surrogate. The final body contains:

- 87 certified non-equilibrium maximal faces;
- 211 certified non-equilibrium true edges with both incident normals handled together;
- 124 certified non-equilibrium vertices with their full incident normal cones handled together;
- 422 feature certificates in total;
- minimum certificate margin `gamma = 0.008607256874061803`;
- worst independent inequality recheck `-2.688821387764051e-16`, attributable to binary64 roundoff.

The features lacking such separators are exactly the genuine equilibrium features returned by the exhaustive audit.

## 5. Exact remaining failure

This body is not close to passing by tolerance choice. Besides the intended stable face and intended apex, it has:

- 14 extra stable maximal faces;
- 20 extra unstable vertices;
- 34 genuine saddle edges.

The smallest positive equilibrium margin anywhere in the body is `0.004687859918180459`, while the largest extra stable, unstable, and saddle margins are respectively

```text
0.3726298942510635,
0.18990960256636794,
0.7276683032310252.
```

These are open, robust equilibria. Reducing an incidence tolerance or increasing arithmetic precision cannot turn `(15,21,34)` into `(1,1,0)`. The failure is geometric: the finite noncritical support network still contains multiple radial-foot/normal-cone intersections even though every other feature has a strict common separator.

## 6. Smallest reproducible local-patch body reached

A separate compressed literal construction has only 13 vertices:

| Quantity | Value |
|---|---:|
| f-vector | `(13,26,15)` |
| Complexity | `52` |
| Own centroid norm | `1.06e-16` |
| Own class | `(3,3,4)` |
| Target stable margin | `0.013952995555351271` |
| Target apex margin | `2.4655391740443555` |
| Minimum non-equilibrium separator margin | `0.004893065468104613` |

Its remaining block is exactly two symmetry-related cancellation pairs: two extra stable faces, two extra unstable vertices, and four saddles. The largest surviving score is `0.03850204357876843`. Full-coordinate evolutionary search, fixed-topology finite-difference LP, exhaustive deletion of non-apex vertex subsets, and randomized one-to-five-vertex truncations all transferred these equilibria to adjacent features rather than producing an open `(1,1,0)` chamber.

This 13-vertex object is the smallest clean finite failure from the literal local-patch route; it is included so a later exactifier or topology-changing search can work on a 52-complexity block instead of the 490-complexity full construction.

## 7. Reproduction and artifacts

The self-contained bundle includes the construction code, complete coordinate/incidence data, independent verifier, exact Jacobian minors, and meshes:

- [Complete Sloan–Lángi bundle](sandbox:/mnt/data/langi_sloan_literal_bundle.zip)
- [Bundle README](sandbox:/mnt/data/LANGI_SLOAN_README.md)
- [Main centered V coordinates](sandbox:/mnt/data/langi_balanced_actuated_V.csv)
- [Main centered H coordinates](sandbox:/mnt/data/langi_balanced_actuated_H.csv)
- [Complete incidence, equilibrium and separator certificates](sandbox:/mnt/data/langi_balanced_actuated_incidence.json)
- [Independent verifier](sandbox:/mnt/data/verify_langi_balanced_actuated.py)
- [Main OBJ](sandbox:/mnt/data/langi_balanced_actuated.obj)
- [Main STL](sandbox:/mnt/data/langi_balanced_actuated.stl)
- [Small 13-vertex V coordinates](sandbox:/mnt/data/langi_13_base_V.csv)
- [Small 13-vertex H coordinates](sandbox:/mnt/data/langi_13_base_H.csv)
- [Small-body incidence and separators](sandbox:/mnt/data/langi_13_base_incidence.json)
- [Small-body OBJ](sandbox:/mnt/data/langi_13_base.obj)
- [Small-body STL](sandbox:/mnt/data/langi_13_base.stl)

Reproduce the main audit with:

```bash
unzip langi_sloan_literal_bundle.zip
cd <extracted-directory>
python verify_langi_balanced_actuated.py
```

Expected headline output:

```text
centroid_norm = 2.919504018463291e-16
fvec          = (145,245,102)
counts        = (15,21,34)
separators    = 422
rank(J)       = 3
```

## 8. Most useful continuation

The literal construction has now separated the mass-control problem from the mechanical-topology problem: the three first moments are solved with a well-conditioned, exact-rank four-actuator system, while the remaining failure is entirely in the noncritical support network.

The next search should therefore keep the four actuator bases and their positive null direction frozen, and replace the noncritical network feature-by-feature. Each replacement should be accepted only when:

1. all newly exposed maximal faces, edges, and vertices obtain a common separator against their full normal cones;
2. the target stable face and single apex remain strict;
3. the four-actuator Jacobian retains rank three;
4. the moment equations are re-solved after every topology change.

The 13-vertex `(3,3,4)` body is the better topology laboratory; the 145-vertex body is the better actuator/certificate reference implementation. Exact rationalization or interval isolation of the complete body is not justified until one of these searches reaches an open own-centroid `(1,1,0)` chamber.
