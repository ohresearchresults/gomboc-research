# figure-0088

AI research report · 2026-08-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# High-curvature `k=3` Fourier-phase branch: resolved verdict and topology-changing continuation

## Unambiguous verdict

**No finite homogeneous polyhedral Gömböc was obtained in this turn.** The saved finite object is decisively not a winner, and the strongest topology-changing continuation exactifies to a robust own-centroid `(S,U,H)=(2,2,2)` fallback, not `(1,1,0)`. The run acceptance gate requires a materialized uniform-density polyhedron evaluated at its own exact volume centroid, with exactly one stable maximal face, one unstable vertex, zero saddle edges, complete H/V topology and all-feature verification; a smooth body, near-wall state, or wrapper is insufficient. :contentReference[oaicite:0]{index=0}

The current journal correctly recorded that the preceding Rapid Raven response exposed only worker-local links and therefore supplied no mathematical verdict. :contentReference[oaicite:1]{index=1} Reading and independently rerunning those files gives the literal saved status:

```text
winner = false
saved finite class = (913,759,1670)
saved counts (V,E,F,C) = (781,2328,1549,4656)
saved all_verifiers_pass = false
saved [internal-source-reference] transcript = "./[internal-source-reference].sh: No such file or directory"
```

The missing-check failure was packaging, not a hidden success. A fresh independent reconstruction from the exact stored generator passes and reproduces the same nonwinner class exactly at the body’s own integrated uniform-volume centroid.

## Certified smooth source, kept separate from the finite result

The source is

```text
R(theta,phi)^4 = 1 + 4 beta sin(theta) cos(phi-P(theta))
beta = 1/160,  a = -1/3,  k = 3
P(theta) = eta(theta) - (1/3) sin(3 eta(theta))
eta(theta) = (3 pi/2)(cos(theta)-cos(theta)^3/3).
```

It is exactly centered: after longitude integration, the transverse first moment is proportional to `integral exp(i[eta-(1/3)sin(3eta)]) d eta`; its Jacobi–Anger frequencies are `1+3m`, so no zero mode exists. The `z` moment vanishes by longitude. The radial critical equations force exactly `(theta,psi)=(pi/2,pi)` and `(pi/2,0)`; these are respectively a strict radial minimum and maximum, and `P'(pi/2)=0` gives critical Hessians `+I` and `-I`. This is the high-conditioning direction recorded in the journal, not another Sloan-boundary mesh. :contentReference[oaicite:2]{index=2}

The stored directed interval certificate covers 10,368 parameter boxes and proves strict convexity with lower bounds

```text
B_11 >= 0.42891126735459995
det(B) >= 0.4208148562262843
Gaussian curvature >= 0.4316325731624288.
```

An independent `240 x 480` JAX differential reconstruction finds minimum Gaussian curvature `0.5157510290423827` and maximum `1.4525354331443143`. This smooth mono-monostatic body is supporting evidence only; it is not the finite answer.

## Literal outcome of the saved 781-vertex finite object

### Deterministic exact generator

Use integer denominator `D=10^10`. First insert the 12 cap vertices

```text
c00 = (-9756905368,1888904381,0)/D
c01 = (-9756905368,1643963699,949142884)/D
c02 = (-9756905368,978434181,1694697713)/D
c03 = (-9756905368,0,1989343010)/D
c04 = (-9756905368,-959565890,1662016874)/D
c05 = (-9756905368,-1632138619,942315671)/D
c06 = (-9756905368,-1888904381,0)/D
c07 = (-9756905368,-1643963699,-949142884)/D
c08 = (-9756905368,-978434181,-1694697713)/D
c09 = (-9756905368,0,-1989343010)/D
c10 = (-9756905368,959565890,-1662016874)/D
c11 = (-9756905368,1632138619,-942315671)/D
```

For `ell=0,...,23`, `j=0,...,31`, set

```text
lo=-0.6718914143270506, hi=0.988
t_ell=(lo+hi)/2+(hi-lo)/2*(-cos((ell+1)pi/25))
lambda_ell,j=pi/2-(j+(ell mod 2)/2+0.15450849718747373 ell)2pi/32
rho=sqrt(1-t_ell^2), s=rho cos(lambda), z=rho sin(lambda)
psi=atan2(s,t_ell), eta=(3pi/2)(z-z^3/3)
phi=psi+eta-(1/3)sin(3eta), r=(1+t_ell/40)^(1/4)
x=r(sqrt(1-z^2)cos(phi), sqrt(1-z^2)sin(phi), z)
v_ell,j=round_nearest(D*x)/D.
```

Finally insert apex `v_780=(10061922463,0,0)/D`. The exact H-representation is obtained by enumerating supporting integer triples and merging coplanar triples into maximal faces. Independent regeneration reproduced every one of the 768 strip integer rows and the apex exactly.

The saved body has exact volume and centroid

```text
volume = 772037768694877707097822417057 / 187500000000000000000000000000
centroid = (
 -211523554708002666503883104516819713057 / 494104171964721732542606346916480000000000,
 0, 0 )
```

and exact centered first moments `(0,0,0)`. Full reconstruction gives `Euler=2`, all 781 vertices active, and class `(913,759,1670)`. The intended 12-gon stable face `F1548=[0,11,10,9,8,7,6,5,4,3,2,1]` has margin `+0.18686859214920773`; intended apex `V780` has margin `+0.05570567263812401`. The smallest positive equilibrium margins are `7.099969276474455e-5` (face), `5.468179165153923e-5` (vertex), and `6.422435075015561e-4` (edge). The closest excluded margins are `-4.480474906058866e-5`, `-0.0031581735865967376`, and `-0.0016634241549729368`. Normalized support separation is `1.3155817945552993e-5`; exact independent H/V checking finds minimum raw slack integer `5962104`.

The residual is not a local four-feature block. It is a wholesale noncritical-strip failure: `24 x 32` nearly tangent level strips create hundreds of stable faces, unstable vertices, and mixed-cone saddle edges. Refining that same architecture makes the mechanics worse:

| levels x points | `(V,E,F)` | `(S,U,H)` |
|---:|---:|---:|
| 24x32 | `(781,2328,1549)` | `(913,759,1670)` |
| 32x64 | `(2061,6168,4109)` | `(2519,1889,4406)` |
| 48x96 | `(4621,13848,9229)` | `(5277,3883,9158)` |
| 64x128 | `(8205,24600,16397)` | `(8721,6405,15124)` |
| 96x192 | `(18445,55320,36877)` | `(16071,12449,28518)` |
| 128x256 | `(32781,98337,65559)` | `(22351,18925,41273)` |

This establishes the exact mechanism used for continuation: remove the offending noncritical strip architecture rather than polish it.

## Genuine topology-changing continuation completed in this turn

I retained exact saved source vertices `[2,7,10,388,582,719,773,780]`, allowed the other 773 source vertices to disappear, and rebuilt the complete hull. The exact source subhull starts with `(V,E,F,C)=(8,18,12,36)` and class `(2,3,3)`. I then ran a full-coordinate homotopy to a new shape, recomputing the hull, own uniform centroid, maximal faces, true edges, and complete normal cones at 5,001 parameter values. The path enters 20 distinct strict signatures and includes actual vertex deactivation/reactivation and circuit changes.

Key cells are:

| `t` | `(V,E,F,C)` | `(S,U,H)` | stable | unstable | saddles |
|---:|---:|---:|---|---|---|
| 0 | `(8,18,12,36)` | `(2,3,3)` | 4,6 | 1,4,7 | (1,7),(0,4),(3,4) |
| 0.0504 | `(7,15,10,30)` | `(2,3,3)` | 4,6 | 1,4,6 | (1,6),(0,4),(3,4) |
| 0.7598 | `(8,18,12,36)` | `(2,2,2)` | 3,6 | 2,7 | (3,4),(1,7) |
| 0.7708 | `(8,18,12,36)` | `(3,2,3)` | 3,5,6 | 2,7 | (2,7),(3,4),(1,7) |
| 0.9198 | `(8,18,12,36)` | `(2,2,2)` | 4,6 | 2,7 | (2,7),(3,4) |
| 0.9792 | `(8,18,12,36)` | `(2,2,2)` | 4,11 | 2,7 | (2,7),(3,4) |

At `t≈0.7598`, unstable vertex 4 and one saddle disappear together: this is a genuine `U-H` Morse cancellation after global topology reconstruction, not a relabelled witness or fixed-incidence sign change. Later cells transfer the remaining Euler-neutral block, and the robust exactified endpoint below is still `(2,2,2)`.

## Strongest exact finite endpoint

### Exact V-generator

With `D=10^6`, the eight vertices are:

```text
V0 = (-920688,-194031,34229) / 1000000
V1 = (-726539,-251304,-288092) / 1000000
V2 = (-899782,-407313,-189380) / 1000000
V3 = (262413,293686,296398) / 1000000
V4 = (-504426,333993,110985) / 1000000
V5 = (442586,298878,192436) / 1000000
V6 = (249665,-51378,-150465) / 1000000
V7 = (2096772,-22531,-6112) / 1000000
```

All eight are actual hull vertices.

### Exact H-generator

The body is `P={x : N_i·x <= b_i/D, i=0,...,11}`:

```text
F00: N=(-11187701853,7335004183,-8042227536), b=8601887240673447, cycle=[0,1,2]
F01: N=(-82898588658,74536042373,-63177952551), b=59698914818812962, cycle=[0,4,1]
F02: N=(23476476331,-336943922097,323577641360), b=54838795194278719, cycle=[0,2,7]
F03: N=(-50498159002,9160445961,210843834285), b=51932612128715850, cycle=[0,3,4]
F04: N=(64636974997,-838811948181,1268764717320), b=146673581390615955, cycle=[0,7,3]
F05: N=(16643514549,-81886434143,-100207151240), b=37355104643990641, cycle=[1,7,2]
F06: N=(766801917,359011817857,-526963108950), b=61035638610912609, cycle=[1,4,6]
F07: N=(24889791809,113293819077,-341124157294), b=51720546362697589, cycle=[1,6,7]
F08: N=(3227732038,113128532567,11243661199), b=37403863754820858, cycle=[3,5,4]
F09: N=(34445183674,136199496128,66497757469), b=68748551521589832, cycle=[3,7,5]
F10: N=(33151097479,322762442462,-246291438518), b=63743465644348482, cycle=[4,5,7]
F11: N=(48087411813,591781423273,-733574734774), b=91978520173142361, cycle=[4,7,6]
```

Every listed row is active. Every nonincident H/V slack is exactly positive.

### Topology

```text
(V,E,F,C)=(8,18,12,36), Euler=2
maximal face cycles:
 F00: 0 1 2
 F01: 0 4 1
 F02: 0 2 7
 F03: 0 3 4
 F04: 0 7 3
 F05: 1 7 2
 F06: 1 4 6
 F07: 1 6 7
 F08: 3 5 4
 F09: 3 7 5
 F10: 4 5 7
 F11: 4 7 6
true edges with incident faces:
 (0,1): [0,1]
 (0,2): [0,2]
 (0,3): [3,4]
 (0,4): [1,3]
 (0,7): [2,4]
 (1,2): [0,5]
 (1,4): [1,6]
 (1,6): [6,7]
 (1,7): [5,7]
 (2,7): [2,5]
 (3,4): [3,8]
 (3,5): [8,9]
 (3,7): [4,9]
 (4,5): [8,10]
 (4,6): [6,11]
 (4,7): [10,11]
 (5,7): [9,10]
 (6,7): [7,11]
```

### Exact own centroid

```text
volume = 1046674666521072547/6000000000000000000
       = 0.17444577775351208
centroid = (
 347523014697427219385611/4186698666084290188000000,
 -21025726433183067398741/2093349333042145094000000,
 -5213390974702138187479/4186698666084290188000000
)
centered first moments = (0,0,0) exactly
```

### Exhaustive complete-normal-cone mechanics

For each face, the listed condition vector contains every signed normalized in-face boundary primitive; positive minimum means stable. For each vertex, every neighbor primitive is listed; positive minimum means unstable. For each true edge, the four entries are `[t,1-t,alpha,beta]`, including both endpoint and both incident-normal coefficients; positive minimum means saddle.

#### All maximal faces

```text
F00 [0,1,2]: score=-1.02918015206; cond=[-1.02918015206,+0.427417737487,+1.32532770411]; stable=false
F01 [0,4,1]: score=-0.800069391282; cond=[+0.839594179631,-0.800069391282,+1.35071413954]; stable=false
F02 [0,2,7]: score=-0.673168181793; cond=[+9.51160781431,+2.59561158062,-0.673168181793]; stable=false
F03 [0,3,4]: score=-0.694154172238; cond=[-0.694154172238,+1.17213442308,+2.43565225117]; stable=false
F04 [0,7,3]: score=+1.05861053459; cond=[+1.05861053459,+5.05659772244,+3.44485285371]; stable=true
F05 [1,7,2]: score=-0.0212036136316; cond=[-0.0212036136316,+0.471519389196,+2.28037448781]; stable=false
F06 [1,4,6]: score=-0.130112595065; cond=[+6.62966657116,-0.130112595065,+1.54484251649]; stable=false
F07 [1,6,7]: score=-0.861158265239; cond=[-0.861158265239,-0.660860329825,+1.63996610147]; stable=false
F08 [3,5,4]: score=-0.387420341962; cond=[+0.93704376743,-0.387420341962,+0.647325856142]; stable=false
F09 [3,7,5]: score=-0.365851139305; cond=[+0.322932673154,-0.102615238668,-0.365851139305]; stable=false
F10 [4,5,7]: score=-1.43350856571; cond=[+2.07172608748,+2.58878403427,-1.43350856571]; stable=false
F11 [4,7,6]: score=+0.228059596612; cond=[+2.59708705165,+1.37481636822,+0.228059596612]; stable=true
```

#### All actual vertices

```text
V00 neighbors=[1,2,3,4,7]: score=-0.0326512581946; cond={1:+0.503742106448,2:-0.0326512581946,3:+0.950637433519,4:+0.741311375352,7:+0.992033450477}; unstable=false
V01 neighbors=[0,2,4,6,7]: score=-0.662243440216; cond={0:-0.14990061672,2:-0.662243440216,4:+0.657541218776,6:+0.978384549504,7:+0.953628361684}; unstable=false
V02 neighbors=[0,1,7]: score=+0.318647540816; cond={0:+0.318647540816,1:+0.783906943702,7:+0.961250203495}; unstable=true
V03 neighbors=[0,4,5,7]: score=-0.164303186159; cond={0:+0.727179592606,4:+0.495105710309,5:-0.0307955304845,7:-0.164303186159}; unstable=false
V04 neighbors=[0,1,3,5,6,7]: score=-0.116191151537; cond={0:-0.116191151537,1:+0.225830037626,3:+0.813749168988,5:+0.85217971109,6:+0.989207461514,7:+0.917577845354}; unstable=false
V05 neighbors=[3,4,7]: score=-0.526019951028; cond={3:+0.434086100778,4:+0.709228683538,7:-0.526019951028}; unstable=false
V06 neighbors=[1,4,7]: score=-0.676363257668; cond={1:+0.585105725182,4:+0.895832951304,7:-0.676363257668}; unstable=false
V07 neighbors=[0,1,2,3,4,5,6]: score=+0.974109066292; cond={0:+0.99795814645,1:+0.991071006391,2:+0.98907980228,3:+0.974109066292,4:+0.990680419604,5:+0.976333920468,6:+0.996532441645}; unstable=true
```

#### All true edges

```text
E(0,1) faces=[0,1]: score=-5.37935025613; cond=[+1.35134829894,-0.351348298936,+6.02819187539,-5.37935025613]; saddle=false
E(0,2) faces=[0,2]: score=-0.107638955575; cond=[-0.107638955575,+1.10763895557,+1.45722272038,+1.16965491092]; saddle=false
E(0,3) faces=[3,4]: score=-0.905215034199; cond=[+0.743060482842,+0.256939517158,+1.52450825717,-0.905215034199]; saddle=false
E(0,4) faces=[1,3]: score=-0.118459860944; cond=[+1.11845986094,-0.118459860944,+0.971008647006,+0.674943319558]; saddle=false
E(0,7) faces=[2,4]: score=-2.54330992725; cond=[+0.335109202953,+0.664890797047,+3.31079894415,-2.54330992725]; saddle=false
E(1,2) faces=[0,5]: score=-2.33355555879; cond=[-2.33355555879,+3.33355555879,+0.91585253182,+0.39304006646]; saddle=false
E(1,4) faces=[1,6]: score=-0.920165469892; cond=[+0.790126201726,+0.209873798274,+1.45643049984,-0.920165469892]; saddle=false
E(1,6) faces=[6,7]: score=-2.31795713513; cond=[+0.867680391272,+0.132319608728,-2.31795713513,+2.98196157006]; saddle=false
E(1,7) faces=[5,7]: score=-0.0251599543734; cond=[+0.298864233603,+0.701135766397,+1.01332637196,-0.0251599543734]; saddle=false
E(2,7) faces=[2,5]: score=+0.34191970957; cond=[+0.34191970957,+0.65808029043,+0.427621105177,+0.935624772981]; saddle=true
E(3,4) faces=[3,8]: score=+0.289274815566; cond=[+0.289274815566,+0.710725184434,+0.548165254026,+0.767415818569]; saddle=true
E(3,5) faces=[8,9]: score=-0.877759445301; cond=[-0.0683089319732,+1.06830893197,-0.877759445301,+1.74684560295]; saddle=false
E(3,7) faces=[4,9]: score=-0.0402126354196; cond=[-0.0402126354196,+1.04021263542,+0.309425927702,+0.987767484883]; saddle=false
E(4,5) faces=[8,10]: score=-0.529143441516; cond=[+0.618156034409,+0.381843965591,+1.31910137178,-0.529143441516]; saddle=false
E(4,6) faces=[6,11]: score=-1.36250583519; cond=[+0.770065578836,+0.229934421164,+2.34802428235,-1.36250583519]; saddle=false
E(4,7) faces=[10,11]: score=-3.42855742434; cond=[+0.24088821014,+0.75911178986,+3.90115001168,-3.42855742434]; saddle=false
E(5,7) faces=[9,10]: score=-0.158755522192; cond=[-0.158755522192,+1.15875552219,+1.04674234043,-0.114545345091]; saddle=false
E(6,7) faces=[7,11]: score=-1.57360654372; cond=[-0.0830364423032,+1.0830364423,+2.30813797717,-1.57360654372]; saddle=false
```

Therefore

```text
stable faces      = [4,11]
unstable vertices = [2,7]
saddle edges      = [(2,7),(3,4)]
class             = (2,2,2)
target stable F4  = [0,7,3], margin +1.0586105345888828
target apex V7, margin +0.9741090662921448
minimum positive equilibrium margin = 0.22805959661244204
minimum exclusion margin = 0.021203613631590484
```

### Incidence and openness

```text
minimum exact H/V raw slack integer = 1401246116762310
raw-slack witness = F0 versus V4
minimum Euclidean nonincident support separation = 0.02733869348122545
Euclidean witness = F1 versus V2
normalized nonincident support separation = 0.009032475307346563
```

Directed interval arithmetic certifies the entire independent Cartesian coordinate box

```text
|delta x_ij| <= 1/50000 = 2e-5 for all 24 coordinates
```

Inside that box, every expected face remains strictly supporting, every nonface triple retains witnesses on both sides, the integrated volume stays positive, the own centroid is recomputed by interval tetrahedral integration, and all 12 face, 8 vertex, and 18 edge classifications remain `(2,2,2)`. Certified interval safety lower bounds are `0.00696845` for topology support, `0.00700308` for face mechanics, `0.01023241` for vertex mechanics, and `0.01501722` for edge mechanics. This is an open fallback chamber, not a circuit wall.

## Independent verification

Fresh checks produced:

```text
PASS_INDEPENDENT_SAVED_NONWINNER  hash=af655f95c298d3f72b3969927f59839279cbc67822347bfb2bf09c152a6560bf
PASS_SMOOTH_SEED_RECONSTRUCTION  hash=6973ed4d75068328e05d4498a9f74fc167b3feae5fc1f84ba01fe34d1532bd36
PASS_EXACT_RESOLVED_222_FALLBACK  hash=a872ded1d843e1a18dd44e9746589f79ddf9f37796820f6aff57aeac5910eceb
PASS_INTERVAL_COORDINATE_BOX  hash=a978835c668e5c9a3fa816499704140906b3a961ff07b411204e474a70e2e8eb
PASS_EXACT_HV_OBJ_STL_CORRESPONDENCE  hash=327b9a872ba028ad11e0977c7ace1c3e901fa787846154c60a6877599e9409fb
PASS_ALL_CHECKS
```

The exact verifier uses `fractions.Fraction` to reconstruct all supporting triples, maximal faces, true edges, volume, centroid, and complete normal cones from the eight V rows; it does not trust the stored audit. A separate exact H/V/OBJ/STL verifier proves incidence and mesh correspondence. The saved 781-vertex verifier independently regenerates the structured strip before rebuilding its complete mechanics.

## Exact residual block and continuation boundary

The remaining block is connected and explicit:

```text
extra stable face F11=[4,7,6], margin +0.22805959661244204
extra unstable vertex V2, margin +0.31864754081636348
saddle E(2,7), margin +0.34191970956980478
saddle E(3,4), margin +0.28927481556632678
```

A finite-difference Jacobian of these four residual scores has full row rank, with singular values approximately `[11.94068245,4.17312081,1.42008961,0.24462712]`. Thus metric rank is not the obstruction. Its least-norm simultaneous negative direction immediately enters `(3,3,4)`, creates new equilibria, deactivates a vertex, and loses the target face before all four old signs reverse. The obstruction is again a coupled topology transfer.

The next nonredundant operation is a single connected two-region bistellar surgery that simultaneously replaces the `F11-E(3,4)` stable corridor and the `V2-E(2,7)` unstable corridor, while retaining target `F4` and apex `V7` and solving all three uniform-volume moment equations as hard constraints. It must permit V2 and at least one boundary vertex of F11 to deactivate together; isolated vertex insertion, fixed-cell metric motion, and further quasi-uniform Fourier-strip refinement are now directly exhausted. Because this endpoint already has eight vertices—the rigorous known lower-bound frontier—the smallest useful search is a 9–12-vertex communicating bifurcated patch with complete adjacent circuit enumeration.

## Reproducible artifacts

- [Complete branch bundle](sandbox:/mnt/data/fourier_k3_resolved_branch_bundle.zip) — SHA-256 `7d5cacd0bee16c93c7aa50292a0e07e4f66ec0c39a3b1dba9ea01ec1f89e20ce`
- [Bundle SHA-256](sandbox:/mnt/data/fourier_k3_resolved_branch_bundle.zip.sha256)
- [Literal validation status](sandbox:/mnt/data/fourier_k3_resolved_bundle/FINAL_VALIDATION_STATUS.json)
- [SHA-256 manifest](sandbox:/mnt/data/fourier_k3_resolved_bundle/MANIFEST.sha256)
- [Exact resolved V generator](sandbox:/mnt/data/fourier_k3_resolved_bundle/tower_fourier_resolved_V_rational.json)
- [Exact resolved H generator](sandbox:/mnt/data/fourier_k3_resolved_bundle/tower_fourier_resolved_H_rational.json)
- [Exhaustive exact audit](sandbox:/mnt/data/fourier_k3_resolved_bundle/tower_fourier_resolved_audit.json)
- [Topology](sandbox:/mnt/data/fourier_k3_resolved_bundle/topology.txt)
- [Exact verifier](sandbox:/mnt/data/fourier_k3_resolved_bundle/verify_resolved_exact.py)
- [Directed interval verifier](sandbox:/mnt/data/fourier_k3_resolved_bundle/verify_resolved_interval.py)
- [Saved-object independent verifier](sandbox:/mnt/data/fourier_k3_resolved_bundle/verify_saved_endpoint_independent.py)
- [Smooth-source independent verifier](sandbox:/mnt/data/fourier_k3_resolved_bundle/verify_smooth_seed_reconstruction.py)
- [H/V/OBJ/STL correspondence verifier](sandbox:/mnt/data/fourier_k3_resolved_bundle/verify_hv_mesh_correspondence.py)
- [Perturbation certificate](sandbox:/mnt/data/fourier_k3_resolved_bundle/perturbation_certificate.json)
- [Homotopy transition graph](sandbox:/mnt/data/fourier_k3_resolved_bundle/homotopy_scan.json)
- [OBJ](sandbox:/mnt/data/fourier_k3_resolved_bundle/tower_fourier_resolved.obj)
- [STL](sandbox:/mnt/data/fourier_k3_resolved_bundle/tower_fourier_resolved.stl)
- [Complete verifier runner](sandbox:/mnt/data/fourier_k3_resolved_bundle/[internal-source-reference].sh)

After extraction, run `./[internal-source-reference].sh`; the expected terminal line is `PASS_ALL_CHECKS`.
