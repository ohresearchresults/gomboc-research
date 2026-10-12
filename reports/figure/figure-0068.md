# figure-0068

AI research report · 2026-08-25 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Complete research handoff — algebraically centered stacked/tetrahedral family

## Verdict

I applied the journal’s literal acceptance gate: uniform volume density, mechanics at the body’s own exact volume centroid, a finite exact H/V representation, exhaustive maximal-face/vertex/true-edge audit, positive incidence separation, an independent verifier, and mesh export. A near-wall or auxiliary-center object is not accepted.

**No strict homogeneous convex polyhedral Gömböc was found in this direction. I do not claim `(S,U,H)=(1,1,0)`.**

This work nevertheless fills the specific missing architecture identified in the journal—an algebraically centroid-hardwired stacked/tetrahedral family. The strongest exact result is:

1. an explicit eight-vertex rational stacked polyhedron **B**, centered exactly through a fixed positive tetrahedral chain, with complete exact/directed verification and strict open class `(2,2,2)`; and
2. an explicit ninth-vertex one-height stacked family over a second exact seed **A**, whose **entire open fixed-combinatorics cell `0<u<1` is algebraically excluded** because two maximal faces remain strictly stable throughout.

The numerical search over the full seven eight-vertex stacked graph types found no positive target chamber, but that is search evidence only—not a global nonexistence theorem.

## What was tried and what changed relative to the journal

- Enumerated all `4·6·8·10=1920` labeled four-stack sequences from a tetrahedron and deduplicated them by graph isomorphism into exactly **seven** eight-vertex stacked combinatorial types.
- Searched all seven types with a 17-parameter realization map: two barycentric variables and one depth per stack, plus a five-parameter determinant-one affine metric.
- Recomputed the realized body’s uniform-volume centroid at every objective evaluation before evaluating any face, vertex, or edge equilibrium primitive.
- Used random starts, CMA-style evolution, direct-coordinate polishing, fixed-cell barrier searches, and controlled fifth/sixth stack extensions.
- Rationalized two strict open `(2,2,2)` bodies, rebuilt their complete exact hulls, and certified every feature.
- Closed one full ninth-vertex stack-height cell by exact rational-function sign and root counting rather than by sampled extrapolation.

This follows the journal’s warning that transfer-wall samples and facet-only signs are insufficient; every result below uses the actual maximal faces, true edges, and full normal cones at the own centroid.

# Part I — strongest explicit algebraically centered body B

## Exact V-representation and centroid elimination

Let `q_i=Q_i/10^6`, with integer rows

```text
0  (-46530,    5057,  54514)
1  (-1436326, -3768,  18812)
2  (-1436326,  1476,  20312)
3  (-46530,    -187, -41698)
4  (1279135,   3326,  37912)
5  (324365,   -4614, -23147)
6  (-90449,    -617, -38005)
7  (1452663,   -673, -28699)
```

The stack sequence is

```text
(0,1,3) -> (1,3,4) -> (1,3,5) -> (3,4,5)
```

and the fixed positive tetrahedral decomposition is

```text
T0=(0,1,2,3)
T1=(0,1,3,4)
T2=(1,3,4,5)
T3=(1,3,5,6)
T4=(3,4,5,7)
```

Its determinant weights are

```text
690269601295488
987854748306844
1032011688581603
1957467249330
530444929060749
```

so

```text
W = 3242538434494014
S = (-575846656221030428051,
     -414478427365705465,
      66492841439367597609)
```

and the exact uncentered volume centroid is

```text
C = S/(4·10^6·W)
  = (-575846656221030428051/12970153737976056000000,
     -82895685473141093/2594030747595211200000,
      22164280479789199203/4323384579325352000000)
  ≈ (-0.044397828110161568,
     -0.000031956323397472949,
      0.0051266039541751456).
```

The centered vertices are exactly `x_i=q_i-C`. For this fixed tetrahedral chain,

```text
Σ_t w_t(x_a+x_b+x_c+x_d) = (0,0,0)
```

identically, so all three uniform-volume first-moment equations are eliminated rationally. Boundary integration and tetrahedral-chain integration agree exactly. The exact volume is

```text
V = 540423072415669/1000000000000000000
  ≈ 0.000540423072415669.
```

## Exact hull

`(V,E,F)=(8,18,12)`, with Euler characteristic `8-18+12=2`.

Oriented maximal triangular faces:

```text
F00 (0,2,1)    F01 (0,3,2)    F02 (1,2,3)
F03 (0,1,4)    F04 (0,4,3)    F05 (1,5,4)
F06 (1,3,6)    F07 (1,6,5)    F08 (3,5,6)
F09 (3,4,7)    F10 (4,5,7)    F11 (3,7,5)
```

True edges:

```text
(0,1) (0,2) (0,3) (0,4)
(1,2) (1,3) (1,4) (1,5) (1,6)
(2,3)
(3,4) (3,5) (3,6) (3,7)
(4,5) (4,7)
(5,6) (5,7)
```

## Exact H-representation

For the centered coordinates `(x,y,z)`, each row is `n·(x,y,z)≤h`:

```text
F00 n=(-14498649,-173724500,607340852)
    h=377973890942513531131744283821/12970153737976056000000
F01 n=(-41294971,33428763188,-1822022556)
    h=13872982656381246000641775293/172935383173014080000
F02 n=(-26890495,173724500,-607340852)
    h=123081982206013920290489566233/4323384579325352000000
F03 n=(84712488,-70402285022,14104730501)
    h=4385742522199685244155130386269/12970153737976056000000
F04 n=(1806411,2898747295,-157995165)
    h=90074825507145835594830024421/12970153737976056000000
F05 n=(281498546,-147567226199,14787621960)
    h=4693461658892794520726382850607/12970153737976056000000
F06 n=(-4264889,-824992646,-146779447)
    h=15153231311874953232707558877/2161692289662676000000
F07 n=(-180279991,-43565527504,-6686549283)
    h=696478744579634914279833882433/2161692289662676000000
F08 n=(-8371981,-2184456604,-353914263)
    h=18297030340425586215011461549/1080846144831338000000
F09 n=(28118649,34039478465,-1970312733)
    h=45095436587783981106873897497/518806149519042240000
F10 n=(284716399,-74193630622,5195937550)
    h=3865668719639322151712911583977/12970153737976056000000
F11 n=(16176929,-7663421746,-2152224147)
    h=22034284370754690177707521389/216169228966267600000
```

The independent V-only reconstructor enumerates all 56 vertex triples, obtains exactly these 12 supporting planes and the 18 true edges, integrates the boundary centroid, and cross-checks the OBJ face set without trusting the declared H-representation.

## Exhaustive own-centroid equilibrium audit

For faces, the signed margin is the minimum barycentric coordinate of the centroid’s perpendicular foot. For vertices, it is the minimum normalized strict-support primitive over every true neighbor. For edges, it is the minimum of `t`, `1-t`, and the two normalized coefficients in the cone generated by the incident outward normals. Positive means that the feature is an equilibrium of its type; negative is an explicit separating witness.

### All maximal faces

```text
F00 (0,2,1)  nonstable  -3.38979139992
F01 (0,3,2)  nonstable  -0.00153203508701
F02 (1,2,3)  nonstable  -2.38880546360
F03 (0,1,4)  nonstable  -0.869800862677
F04 (0,4,3)  STABLE      0.00160950198407
F05 (1,5,4)  STABLE      0.235395864432
F06 (1,3,6)  nonstable -23.7140577855
F07 (1,6,5)  nonstable  -0.742660416212
F08 (3,5,6)  nonstable  -7.64506406743
F09 (3,4,7)  nonstable  -0.604284033845
F10 (4,5,7)  nonstable  -0.670912425716
F11 (3,7,5)  nonstable  -1.12861794689
```

Positive exact face margins:

```text
F04: 967628119796320143644006699306653 /
     601197220863377597278176372026140668
F05: 2798037322409538566600397866412632347 /
     11886518606249161294285130383444234073
```

### All vertices

```text
V0 limiting neighbor 2  nonunstable  -0.0181788255011
V1 limiting neighbor 2  nonunstable  -0.000123318077686
V2 limiting neighbor 1  UNSTABLE      0.00404161248070
V3 limiting neighbor 1  nonunstable  -0.00200106823242
V4 limiting neighbor 7  nonunstable  -0.924148578976
V5 limiting neighbor 7  nonunstable  -0.997311839717
V6 limiting neighbor 1  nonunstable  -0.700371873848
V7 limiting neighbor 4  UNSTABLE      0.941228933464
```

Exact limiting raw supports for the two unstable vertices:

```text
V2: 4145830879549810200469/135105768103917250000000000
V7: 849667288306072706482789843/3242538434494014000000000000
```

### All true edges

```text
E00 (0,1) nonsaddle  -0.418640944760
E01 (0,2) nonsaddle  -0.000649817667097
E02 (0,3) nonsaddle -357.939097140
E03 (0,4) SADDLE      0.00207962350403
E04 (1,2) nonsaddle  -0.0314721220739
E05 (1,3) nonsaddle  -0.0000674255395458
E06 (1,4) nonsaddle -10.0275980743
E07 (1,5) nonsaddle  -3.72879218923
E08 (1,6) nonsaddle -41.2890701050
E09 (2,3) nonsaddle  -0.294078200138
E10 (3,4) nonsaddle -295.943874660
E11 (3,5) nonsaddle  -8.50385577283
E12 (3,6) nonsaddle -63.4424382559
E13 (3,7) SADDLE      0.00169286476478
E14 (4,5) nonsaddle -33.2182528774
E15 (4,7) nonsaddle  -6.58101584584
E16 (5,6) nonsaddle -117.980728741
E17 (5,7) nonsaddle  -2.61536205812
```

For saddle `(0,4)`:

```text
t   = 23704798891075728859324451/11398601162741074185186939720
1-t = 11374896363849998456327615269/11398601162741074185186939720
β1  = 6988750434700328714849210596918819/
      1445834910460924910585165875355841280360000000
β2  = 1905772708162593598787577888346541041/
      15994548696973981823348397496123994163982500000
```

For saddle `(3,7)`:

```text
t   = 2741843553739457331000461/1619647127628625604800529832
1-t = 1616905284074886147469529371/1619647127628625604800529832
β1  = 8009444966198924402498704091390381/
      1975019783260717679683472374169308769572800000
β2  = 41315277452844104818003680356246089/
      2291022948582432508432827954036398172704448000
```

Therefore the exact strict class is

```text
(S,U,H)=(2,2,2),   S+U-H=2.
```

The target stable face `F05` and target unstable vertex `V7` are robust. The residual block consists of extra stable `F04`, extra unstable `V2`, and saddles `E03,E13`; the target hard defect is `-0.004041612480698685`, controlled by `V2`. Thus B is a genuine interior fallback, not a transfer-wall pseudo-solution.

## Inactive incidence and perturbation box

- Minimum directed lower bound for a unit-normal inactive support slack:
  `0.000044411137767436128564142240641768577`.
- Certified perturbation radius:
  `R=1/3000000000` in `l∞` for **each of the 24 uncentered coordinates independently**, with the centroid recomputed from the fixed tetrahedral chain.
- Exact rational interval arithmetic proves that throughout the whole box, all tetrahedral weights remain positive, the same 12 maximal faces and 18 true edges remain active, all inactive incidences stay strict, and the class remains `(2,2,2)`.

# Part II — exact closed ninth-vertex stack-height family

## Robust seed A

Let `q_i=Q_i/10^6` with

```text
0 (-86624, 243361, -281446)
1 (-210972,113977, -285891)
2 (-862076,890020,-1545614)
3 (-347156,370063, -638423)
4 (377012,-333348, 630167)
5 (371092,-436753, 709485)
6 (377356,-420924, 701566)
7 (381368,-426396, 710155)
```

and positive tetrahedral chain

```text
(0,1,2,3), (0,1,3,4), (1,3,4,5),
(3,4,5,6), (4,5,6,7).
```

Its exact volume is

```text
211565570204401/300000000000000000
≈ 0.00070521856734800329,
```

and its exact centroid is

```text
(-168429995840343961587/1057827851022005000000,
  743954277845108900361/4231311404088020000000,
 -1246781203296706038403/4231311404088020000000).
```

A has strict class `(2,2,2)`, minimum inactive unit slack
`0.00014305223823360481309373273220785806`, and certified coordinate radius `1/2000000000`.

## Complete open one-parameter cell

Add a ninth vertex over face `{0,1,2}` by

```text
q8(u)=b+uΔ,  0<u<1,

b=(-144959/375000,
    207893/500000,
   -704317/1000000),

Δ=(-14823402546677603558730423/15243275644364423620723750000,
    10270054119875557669589767/11432456733273317715542812500,
    160973866245881760685581/152432756443644236207237500).
```

At `u=1`, `q8` first reaches old face `(0,1,4)`. Therefore `0<u<1` is the entire open fixed-height combinatorial cell along this actuator. Add tetrahedron `(0,2,1,8)`.

The 14 maximal faces are

```text
(0,3,2) (1,2,3) (0,1,4) (0,4,3)
(1,3,5) (1,5,4) (3,4,6) (3,6,5)
(4,5,7) (4,7,6) (5,6,7)
(0,2,8) (2,1,8) (1,0,8)
```

and the 21 true edges are

```text
(0,1) (0,2) (0,3) (0,4) (0,8)
(1,2) (1,3) (1,4) (1,5) (1,8)
(2,3) (2,8)
(3,4) (3,5) (3,6)
(4,5) (4,6) (4,7)
(5,6) (5,7) (6,7)
```

Thus `(V,E,F)=(9,21,14)` and Euler characteristic is 2. The symbolic verifier certifies all 29 nontrivial strict polynomial incidence signs.

The exact determinant sum is

```text
W(u) =
(4489200515896859006499066363937054871·u
 +38699427641793808272283398405444662685)
/9145965386618654172434250000000000000000.
```

The centroid is the exact rational map `C(u)=S(u)/(4W(u))`; each coordinate has numerator degree 2 and denominator degree 1. Boundary and tetrahedral volume/moment formulas agree identically, and after setting `x_i(u)=q_i(u)-C(u)`, all three centered first moments are identically zero rational functions.

## Exact no-go theorem for this cell

Two distinct maximal faces are strictly stable for **every** `0<u<1`:

- new face `(1,0,8)`: all three foot-barycentric rational functions have numerator/denominator degrees `(3,3)`, no numerator root or denominator pole in `(0,1)`, and positive sign at `u=1/2`;
- retained face `(3,4,6)`: all three have degrees `(2,1)`, no root or pole in `(0,1)`, and positive sign at `u=1/2`.

The verifier uses exact rational Sturm/root counts, with all numerator and denominator polynomials materialized in `stack_height_certificate.json`. Hence

```text
S(u)≥2 for every 0<u<1,
```

so **no member of this entire open stack-height subfamily is a Gömböc**.

There is also a certified transfer wall: the raw unstable-support primitive of vertex `7` against neighbor `5` and the edge `(5,7)` primitive `1-t` have proportional quadratic numerators. Their unique root in `(0,1)` is isolated by

```text
17993283785/27511314918
< u <
19922948602/30461727811,
```

both endpoints being approximately `0.6540321260045415`, with interval width below `1.2·10^-21`. The other root is near `25120.5112541`, outside the cell. This precisely identifies a vertex/edge transfer rather than a cancellation.

# Reproducibility and artifacts

The complete portable bundle includes all exact coordinates, both H/V representations, tetrahedral decompositions, every feature primitive, inactivity tables, symbolic family certificates, search sources/logs, exact and interval verifiers, an independent V-only reconstructor, and OBJ/STL exports.

- Download complete research bundle ZIP (`stacked_tetrahedral_research_bundle.zip`)
- Read the full standalone report (`stacked_tetrahedral_research_REPORT.md`)
- ZIP SHA-256 record (`stacked_tetrahedral_research_bundle.zip.sha256`)
- Bundle manifest (`SHA256SUMS.txt`)
- Combined verifier transcript (`RUN_ALL_VERIFIERS.txt`)

Body B:

- machine-readable candidate (`candidate.json`)
- exact centered vertices (`vertices_centered.csv`)
- exact primitive H-representation (`halfspaces_primitive.csv`)
- complete per-feature margins (`complete_margin_summary.csv`)
- exact verifier (`verify_fraction.py`)
- independent V-only reconstructor (`verify_independent_reconstruct.py`)
- interval perturbation verifier (`verify_interval.py`)
- OBJ (`body.obj`)
- STL (`body.stl`)

Closed family:

- symbolic family verifier (`verify_stack_height_family.py`)
- materialized polynomial/root certificate (`stack_height_certificate.json`)
- seed A candidate (`candidate.json`)

Run from the extracted bundle root:

```bash
bash RUN_ALL_VERIFIERS.sh
```

This was also tested after fresh ZIP extraction: the SHA-256 manifest verified and every exact, independent, interval, symbolic, and combinatorial verifier passed. ZIP SHA-256:

```text
25324a95aed81f5fc946e14c6b7d77f86188bb81a6a2610c8e97fa20682afc62
```

# Honest scope and most useful continuation

Exactly closed here:

- the complete rational hull, centroid, equilibrium classification, inactive incidences, and perturbation box of B;
- the analogous exact data for A; and
- the entire one-dimensional ninth-vertex fixed-height cell `0<u<1` over A, excluded by two persistent strict stable faces.

Not closed:

- the full realization spaces of the seven eight-vertex stacked types;
- all higher-vertex stacked types;
- adjacent bistellar or nonsimplicial cells; or
- the global existence question.

The strongest next move is **not another isolated one-face height actuator**. In B, the residual stable/saddle pair `(F04,E03)` and the residual unstable/saddle defects `(V2,E13)` are spatially separated. The observed mechanism is transfer: changing one region tends to remove one equilibrium while birthing its replacement in a neighboring feature. A more promising family is a paired two-region actuator or controlled `2–3/3–2` bistellar change that moves both Morse blocks simultaneously while keeping the exact centered map `x_i(p)=q_i(p)-C(p)` and explicit barriers for every inactive incidence and every non-target face/vertex/edge primitive.
