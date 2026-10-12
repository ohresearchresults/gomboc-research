# figure-0054

AI research report · 2026-08-24 UTC

---

# Continuation result

## Verdict

No finite homogeneous polyhedral Gömböc with strict own-centroid class `(1,1,0)` was certified. The acceptance gate remains unmet: the requested result requires a materialized finite representation, its own uniform centroid, an exhaustive strict all-feature audit, independent verification, and matching OBJ/STL; neither a smooth body nor a transfer-wall numerical candidate qualifies. :contentReference[oaicite:10]{index=10}

This continuation produced three useful outcomes:

1. It corrected an integrity error in the previous handoff concerning the mounted six-ring artifact.
2. It preserved two fully materialized `(2,2,2)` bodies with sharply localized remaining blocks.
3. It reframed the next construction around the now interval-certified Sloan smooth Gömböc and implemented the first finite halfspace experiment needed to operationalize Lángi’s polyhedral approximation proof.

## 1. Integrity correction: superseding the previous `B6` description

The coordinate table and `(14,33,21)` audit previously attributed to `freshbot_m6_404_best_Q.npy` do not match the actual mounted file. They must not be reused.

A fresh audit of the actual file gives:

- 24 stored rows, 17 active hull vertices;
- Santaló point approximately `(0.01216123,-0.05195104,-0.14380841)`;
- polar-centroid residual `3.14e-15`;
- f-vector `(V,E,F)=(17,42,27)`;
- Santaló-relative class `(S,U,H)=(3,2,3)`.

Its genuine equilibria are:

- stable faces `[20,10,19]`, margin `0.004972648398952529`;
- stable face `[22,9,16]`, margin `0.00798061589944498`;
- designated horizontal bottom face `[22,21,20,19,18,23]`, margin `0.00249226257933448`;
- apex vertex `0`, margin `0.09029663883572002`;
- extra unstable vertex `18`, margin `0.0007744975177017597`;
- saddle edge `(12,16)`, margin `0.03582270871990823`;
- saddle edge `(0,15)`, margin `0.003059821576867843`;
- saddle edge `(21,22)`, margin `0.002922610322336109`.

Thus this remains a valid topology-changed, bottom-face-retaining descendant of the journal’s fivefold-belt seed, but its true class is `(3,2,3)`, not the class reported previously. The original Qloc coordinates and the fivefold block being replaced are recorded in the journal. :contentReference[oaicite:11]{index=11}

Artifacts:

- [Actual six-ring descendant](sandbox:/mnt/data/freshbot_m6_404_best_Q.npy)
- [Geometry and Santaló verifier](sandbox:/mnt/data/gomboc_geom.py)

## 2. Best verified Qloc-derived topology bridge

The strongest retained Qloc-derived body is [nearH1_705_Q.npy](sandbox:/mnt/data/nearH1_705_Q.npy). It contains 14 binary64 rows, 13 of which are active hull vertices. Re-solving the three Santaló equations gives

` s = (0.00771075256, 0.00248622880, -0.33100967256) `

with polar-centroid norm `5.56e-16`. The centered hull has

- f-vector `(13,31,20)`;
- class `(2,2,2)`;
- equilibrium Euler audit `2+2-2=2`;
- polar f-vector `(20,31,13)` and the same `(2,2,2)` class.

Complete positive equilibrium block:

- target stable face `[6,4,11]`, margin `0.05282517918967635`;
- extra stable face `[13,3,5]`, margin `0.00017082403378134928`;
- target maximum at vertex `0`, margin `0.05962311850893748`;
- extra maximum at vertex `10`, margin `0.008593220716025477`;
- saddle edge `(0,6)`, margin `0.009689193107307755`, projection parameter `t=0.7433848184650285`;
- saddle edge `(1,10)`, margin `0.008053917063760479`, projection parameter `t=0.6176454370150266`.

This proves that the original five congruent copies have been destroyed: the remaining block is asymmetric and consists of one extra minimum, one extra maximum, and two saddles. The old horizontal bottom polygon is no longer the stable face, so this is a topology bridge rather than a target-retaining final body.

The sharp circuit nearest the extra stable face remains the four-point set `{3,5,9,13}`. The two smallest measured circuit slacks were approximately `1.52814e-4` and `2.30054e-4`. One-coordinate, paired-circuit, vertex-deletion, affine-metric, CMA, and sequential-linear-programming scans transferred the equilibria to adjacent features but did not lower `H` below two in an open chamber.

## 3. Independent 19-vertex own-centroid `(2,2,2)` body

A separate direct-coordinate search produced [candidate4203_centered.npy](sandbox:/mnt/data/candidate4203_centered.npy). Unlike the Qloc bodies, its rows are already centered at their own uniform-volume centroid to numerical error below `8e-17`.

Its full binary64 V-representation is:

```text
0  -2.2128748418171247   -0.41311023037951239    0.029130847730849604
1   0.70909977362193666  -0.12955542182592364   -0.058048811912028479
2   0.0049624673099659487 -0.38262520461459337   0.045423311950885913
3  -0.11326616081727311  -0.083017963027806521 -0.090421299199166333
4  -0.040912889480654649 -0.081060264576201024 -0.090986562353326125
5  -0.072596901026513977 -0.080459394680863008 -0.091394375668605365
6   1.6814441165523799    0.55265001835612215    0.01364002780286006
7   0.59400460617477302   0.047491925309773496   0.046808511340577882
8   0.3855205268881246   -0.3656720315326909     0.047966221649100832
9   0.58304288543755178  -0.35608547209723052    0.041284558040874948
10  0.38358957830876478  -0.37741686642403011    0.04795535050565259
11 -0.032276051854861654  0.42153218767163392    0.02212978301125533
12  1.680197454904709     0.55653837710369825    0.012999023981034256
13  1.6782766225437902    0.55648808582621101    0.013423686965292825
14 -0.00035646525782973975 -0.0016946749869081988 -0.086077177295022109
15 -0.68357537463895834   0.30774483071047087    0.027547014743972632
16 -0.072245525510372194  0.41455068789862137    0.022456348569403407
17 -0.91912111036053834   0.22572659575322179    0.032967966593813437
18 -0.72804835796243628   0.20878052978003558    0.034598742368865815
```

Audit:

- volume `0.10852454355110847`;
- f-vector `(19,51,34)`;
- class `(2,2,2)`;
- target stable face `[0,7,17]`, margin `0.0498055`;
- extra stable face `[15,16,14]`, margin `5.9628e-5`;
- target maximum at vertex `0`, margin `3.126713`;
- extra maximum at vertex `12`, margin `6.1051e-5`;
- saddle `(0,2)`, margin `3.68168e-5`, with `t=0.9999834`;
- saddle `(11,16)`, margin `1.88182e-5`, with `t=0.9995362`.

This body is closer to simultaneous cancellation than the Qloc bridge in raw margin, but it is a transfer-wall candidate: its two saddles sit extremely close to their endpoint vertices. Circuit and deletion scans did not find an open `(1,1,0)` continuation. It is therefore unsuitable for rationalization as a winner.

## 4. New constructive route: certified smooth seed plus Lángi surgery

A stronger global route emerged from current primary sources. The Sloan radial body

`r(theta,phi)^4 = 1 + 4 beta sin(theta) cos(phi-eta(theta))`

with

`eta(theta) = (3 pi/2)(cos(theta) - cos(theta)^3/3)`

and `beta=0.023` has now been subjected to interval/Krawczyk verification; the amended computation reports strict convexity in the relevant regime and exactly one stable and one unstable equilibrium with no unresolved boxes. This is an actual certified smooth Gömböc, although not a polyhedral answer. :contentReference[oaicite:2]{index=2}

Lángi’s theorem gives the correct topology-aware polyhedral mechanism: isolate each smooth equilibrium in a dedicated local polyhedral replacement, cover the non-equilibrium remainder by sufficiently small inward-shifted support-plane patches, and use four small controlling cones whose height parameters span the three first moments. The proof explicitly treats the local stable/unstable patches, the no-new-equilibrium support cover, and the final centroid correction. It is not equivalent to uniform triangulation or a generic tangent-plane mesh. :contentReference[oaicite:3]{index=3}

I implemented the radial surface, its analytic tangent normal, a dedicated stable truncation plane, a conical unstable cap, inward-shifted support planes on the remainder, halfspace intersection, own-volume-centroid integration, maximal-face merging, true-edge recovery, and a complete face/vertex/edge audit:

- [Sloan–Lángi construction experiment](sandbox:/mnt/data/langi_sloan_construct.py)
- [Parameter-grid driver](sandbox:/mnt/data/langi_scan_grid.py)
- [First materialized halfspace experiment](sandbox:/mnt/data/langi_test.npy)

The first attempt deliberately tested the tempting simplification of replacing Lángi’s finite local cover by a quasi-uniform collection of shifted tangent planes. It failed decisively:

| Tangent samples | f-vector | Own-centroid class | Centroid |
|---:|---:|---:|---:|
| 80 | `(167,254,89)` | `(83,123,204)` | `(-0.03088585,-7.73e-6,-8.23e-5)` |
| 200 | `(411,623,214)` | `(190,273,461)` | approximately `(-0.0118073,-1.24e-5,-4.61e-7)` |
| 800 | `(1483,2231,750)` | `(596,904,1498)` | approximately `(-0.0110278,-6.65e-7,1.44e-7)` |
| 1200 | `(2289,3442,1155)` | `(804,1155,1957)` | `(-0.00566977,4.95e-8,-2.08e-7)` |

Every row satisfies `S+U-H=2`. Increasing the global sampling density reduced the centroid error but did not suppress the polyhedral equilibria. This independently reproduces the warning in Lángi’s paper that an equidistant or generic fine approximation can create many extra equilibria. The failure is geometric, not a centroid bug: a successful implementation must construct the local support patches so that the perpendicular foot is excluded from each entire maximal face and one common strict separator excludes the complete normal cone of every mixed edge and vertex. :contentReference[oaicite:4]{index=4}

Reproduction of the largest completed experiment:

```python
from langi_sloan_construct import build

V,c,volume,A,halfspaces,labels,apex,apex_index = build(
    N=1200,
    eps=0.0,
    alpha_u=0.25,
    alpha_s=0.25,
    du=0.005,
    ds=0.005,
    m_u=20,
    rot=0.13,
    phase=0.1,
    ring_extra=True,
)
print(A['fvec'], A['counts'], c)
# (2289,3442,1155), (804,1155,1957),
# [-5.66976558e-3, 4.95403506e-8, -2.07818767e-7]
```

## 5. Sharply defined remaining construction

The most useful continuation is now a literal finite implementation of the three Lángi stages around the certified Sloan seed, rather than further random polishing of either `(2,2,2)` chamber:

1. **Stable patch:** choose one inward plane parallel to the tangent plane at the smooth minimum and finitely many surrounding support cuts whose intersection with it contains the perpendicular foot with a positive polygonal margin.
2. **Unstable patch:** construct a fan of polygonal radial curves from a single apex at the smooth maximum, with every neighboring radius strictly decreasing away from the apex. This must be encoded as a single convex cap rather than as unrelated tangent planes.
3. **Noncritical cover:** generate local shifted-support patches from certified neighborhoods on which the smooth position vector is separated from the complete normal cone. Refine only where the computed maximal face or mixed normal cone lacks a common negative separator.
4. **Centroid actuators:** reserve four disjoint noncritical patches and vary their cone heights. Numerically compute the full `3 x 4` first-moment Jacobian, solve the three moment equations, and keep one slack actuator for mechanical margins.
5. **Exactification:** only after obtaining an open numerical `(1,1,0)` chamber, round all support rows to rationals, reconstruct all vertices exactly or with directed intervals, freeze the maximal-face cycles and true edges, and emit OBJ/STL.

The present scripts already supply the smooth geometry, support normals, halfspace intersection, centroid integration, and exhaustive numerical audit needed for stages 1–3. What remains missing is the branch-complete local patch builder and the four-cone moment solve.

## Acceptance status

The assignment direction is complete as a research handoff but not as the requested discovery. No artifact in this result is a strict homogeneous polyhedral Gömböc. Consequently no rational certificate or OBJ/STL is claimed.
