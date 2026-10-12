# figure-0063

AI research report · 2026-08-25 UTC

---

# Topology-free Santaló-polar continuation: interval-certified asymmetric family, no winner

## Verdict

No strict centroidal polyhedral Gömböc was found. I reject every numerical wall state and make no `(1,1,0)` claim.

The strongest new reusable object is a **genuinely asymmetric 33-vertex point polytope** `Q_raw` whose three Santaló equations are enclosed by an interval Krawczyk certificate. After translating by that isolated root and normalizing dually,

`Q_0 = ρ(Q_raw-s(Q_raw))`, `P_0 = ρ^{-1}(Q_raw-s(Q_raw))°`,

with `ρ=0.019526165427587786`, the origin is strictly interior to `Q_0`, `P_0=Q_0°`, and the uniform-volume centroid of `P_0` is the origin. The exact reconstructed classes are

`Q_0: (S,U,H)=(2,1,1)`, `P_0: (S,U,H)=(1,2,1)`.

Thus this is a robust one-pair Santaló-hardwired near-object, not a winner. It is materially different from the exhausted fixed-normal and fivefold cells: it was built by deleting old rows and inserting two unequal connected 17-link rails.

## What changed relative to the supplied journal and prior handoff

The prior C=104 anchor showed a residual stable-saddle pair but had a very thin incidence gap. This continuation established four new facts.

1. **A connected monotone rail really can cancel the pair mechanically.** Among 2,400 randomized single-rail constructions, 694 were valid hulls spanning 692 reconstructed topology hashes; 54 were strict Q-class `(1,1,0)` relative to the reference origin, with best open margin `5.6421752262818336e-5`. All 54 Santaló points were then solved. None remained target-class at its Santaló point. The obstruction in this chart is therefore moment placement, not failure of the radial witness chain.
2. **Moment balancing by a second rail produces an isolated Santaló root.** A C2-paired rail has a scalar common-shape root near `theta=1.707055612966384`; its centered polar is `(1,2,1)`. C3 and C4 unions proliferated pairs rather than removing them.
3. **Breaking the two branches asymmetrically can be certified without losing the one-pair topology.** The unequal branch powers `theta_A=1.704555612966384` and `theta_B=1.7095556129663838` give the explicit asymmetric family below. All three Santaló equations—not a penalty surrogate—are interval-isolated.
4. **Affine/metric polishing again coalesces transfer walls rather than opening the target.** The sharpest asymmetric endpoint has hard score `-2.22205837065534e-5`, but it is `(2,2,2)`, has condition number `4.661254177315369e4`, and has normalized incidence gaps near `10^-9`; it is rejected.

## Explicit asymmetric construction

The two branches use the materialized rail builder with

```text
m = 17
phi_mid = -0.5423558937657096
phi_curve = -0.7364735384082259
slack_shape = 0.38076121384637673
delete = [0,2,11,13,14,21,25,26,27,28]
theta_A = 1.704555612966384
theta_B = 1.7095556129663838
```

The second branch is mapped by `diag(-1,-1,1)`, but the unequal powers make the union genuinely asymmetric. Its active hull has

| body | V | E | maximal F | complexity |
|---|---:|---:|---:|---:|
| `Q_0` | 33 | 93 | 62 | 186 |
| `P_0=Q_0°` | 62 | 93 | 33 | 186 |

The raw 17-digit V-coordinates are in `Q_raw_V.csv`. The centered normalized V/H coordinates, every maximal face, every true edge, and all normal-cone witnesses are materialized in the bundle.

## Certified Santaló point

Treating the 17-digit rows of `Q_raw_V.csv` as exact decimal constants, the isolated root is centered at

```text
s_x = 0.146025511153385333127178439244923195505032666000136368578353...
s_y = 0.0138778240927478875460999416754941572240796261318949168041923...
s_z = 0.000158379291384364324304002263109616624781800194261960207794859...
```

A three-dimensional Krawczyk operator maps the radius-`10^-16` box strictly into itself. Its coordinate offset enclosures are

```text
K_x-x0 ⊂ [-7.3231e-29, 7.3231e-29]
K_y-y0 ⊂ [-5.9648e-29, 5.9648e-29]
K_z-z0 ⊂ [-1.5892e-29, 1.5892e-29]
```

The enclosed first moment at the high-precision center is below `3.4e-81`. The first-moment Jacobian eigenvalues are

`9.94096909379067e-12`, `1.02941394702364e-11`, `1.73862865390525e-10`,

all strictly positive; its condition number is about `17.49`. The minimum interval lower bound on every polar denominator is `11118.85`, so the whole root box stays strictly inside the same polar domain. The fixed-topology raw inactive gaps are `0.0287395` for Q and `6.8840e-7` for P, enormously larger than the root box. This supplies an isolated solution of all three Santaló equations and excludes a topology-dependent root artifact.

## Strict interior and polar/centroid certificates

Before polarity, strict containment of the origin in `Q_0` is certified in two independent ways.

- Every oriented Q supporting plane has positive origin slack; the minimum normalized facet support is `1.0000000000000004`.
- The origin is in the interior of the tetrahedron on Q vertices `(17,0,13,30)` with positive barycentric weights

`(0.22196524308739782, 0.2364248016708335, 0.2712165911212656, 0.2703933641205031)`.

The minimum weight is `0.22196524308739782`; the reconstructed weighted vector has norm below `2.4e-15`.

The independent binary audit gives

- `centroid(P_0)=(1.10e-16,1.67e-16,9.26e-18)`;
- `max_{q∈Q_0,p∈P_0} q·p = 1.000000000000001`;
- minimum positive polar nonincidence slack `2.059885166612041e-4`;
- positive normalized Santaló Jacobian eigenvalues `(0.003502223853855916, 0.003626646503719676, 0.06125224500001418)`.

## Global incidence and feature audit

All incidences were rebuilt from raw point coordinates after each insertion, deletion, active-set change, or metric transform. The final standalone verifier does not import the search code. It reconstructs each maximal plane from its listed vertices, checks every equality and every inactive inequality, rebuilds true edges from polygonal face boundaries, and re-evaluates all face, vertex, and edge normal cones.

For the robust normalized asymmetric anchor:

| audit | Q | P |
|---|---:|---:|
| minimum inactive slack | `5.611727727714566e-4` | `3.525528292319669e-5` |
| largest face-equality residual | `3.55e-15` | `1.03e-13` |
| class | `(2,1,1)` | `(1,2,1)` |

The P features are:

- unique stable face `1`, an 8-gon, margin `0.04682230152339957`;
- unstable vertices `21` and `30`, margins `0.6126893155826213` and `0.6134332902958782`;
- saddle edge `(11,33)`, margin `0.010483442695824274`;
- largest non-target face margin `-0.0011747260086762`.

The dual Q features are:

- stable faces `21` and `30`, margins `0.11089462399643873` and `0.11103237781734428`;
- unique unstable vertex `16`, margin `0.3112803714285749`;
- saddle edge `(1,18)`, margin `0.030919179213933223`.

This is an open, tolerance-independent `(1,2,1)` / `(2,1,1)` cell. The complete per-feature edge witnesses, cone coefficients, incident facets, and residuals are in `P_equilibrium_audit.json` and `Q_equilibrium_audit.json`.

## Complete topology-transition graph of the materialized family

Let parameters be `u=(α,β,γ,δ,ε)` and

```text
L(u) = [[exp(α),                    0,               0],
        [exp(β)γ,              exp(β),               0],
        [exp(-α-β)δ, exp(-α-β)ε, exp(-α-β)]] .
```

Define

`P(u)=L(u)P_0`, `Q(u)=L(u)^(-T)Q_0`.

For every finite `u`, `det L(u)=1`, the centroid of `P(u)` is exactly the origin, and affine covariance gives `s(Q(u))=0`. Because every `L(u)` is invertible, the full face lattice is preserved exactly. Consequently the complete combinatorial topology graph of this five-dimensional asymmetric Santaló family is

```text
T0: Q=(33,93,62), P=(62,93,33)
edges: none
```

The full cycles and true edges attached to node `T0` are `Q_incidence.json` and `P_incidence.json`. This one-node graph is not an omission: invertible linear maps cannot cause a circuit crossing.

## Sharpest asymmetric wall checkpoint—and why it is rejected

The best metric parameters found in the asymmetric cell are

```text
(-2.12267066987848,
 -4.04286081163493,
 -1.3896872724507914,
 -0.7778685468127202,
 -0.6233433927436839)
```

They give `det L=1`, `cond(L)=46612.54177315369`, and P-class `(2,2,2)`. Its hard score is `-2.22205837065534e-5`; the relevant largest witnesses are

- retained face margin `4.17417260903587e-6`;
- extra face margin `3.73337634692349e-7`;
- extra vertex margin `2.22114589107606e-5`;
- largest saddle margin `2.22205837065534e-5`.

The minimum inactive slacks divided by circumradius are only `1.5989592011e-9` for P and `4.0867306098e-9` for Q. The state is therefore a highly conditioned multi-transfer wall, not an open candidate; it fails both the target class and the incidence discipline. I assign it no perturbation radius and do not exactify it.

## Search census and attempted falsification

- **Single connected rail:** 2,400 parameter sets, 694 valid bodies, 692 distinct topology hashes. Fifty-four were strict origin-relative Q `(1,1,0)`; every one had its Santaló point solved, and none yielded centered target P.
- **Rotational unions:** 123 materialized C2/C3/C4 bodies in 123 reconstructed topologies. C2 supplied the balanced root; higher fold unions generated many extra stable-saddle pairs.
- **Unequal two-rail continuation:** all three Santaló equations were solved after each asymmetric split. A split of `|delta|=0.001` already moves the Santaló point by about `0.0587`, showing why “break symmetry, then recenter” is mechanically destructive unless moment neutrality is imposed during the move.
- **Circuit/deletion cells:** all 33 single-Q-vertex deletions of the C2 root were materialized and re-solved; none won. Seventeen deletion-plus-metric cells were additionally searched before the branch was deprioritized; the best remained `(3,2,3)` with score `-2.7482e-5` and a sub-gate P incidence gap.
- **Metric minimax:** multiscale random, cross-entropy, smooth continuation, and branchwise SLSQP moved several witnesses onto a common wall but did not make the minimax margin positive. I explicitly tried to break the near-wall conclusion by enumerating alternate active witnesses; the best branch improved only in the eighth decimal place and retained `(2,2,2)`.

The negative conclusion is local to these materialized cells. It is not a global nonexistence claim.

## Sharply delimited open cells

The surviving robust defect is now localized in explicit dual labels. On P, preserve stable face `1` and unstable vertex `30`; cancel extra unstable vertex `21` with saddle edge `(11,33)`. Equivalently on Q, preserve stable face `30` and unstable vertex `16`; cancel stable face `21` with saddle edge `(1,18)`.

The nonredundant continuation is:

1. replace the connected Q neighborhood of face `21` and edge `(1,18)` by an **asymmetric Y-shaped two-rail patch**, rather than taking a full C2 copy;
2. include three mechanically inactive but linearly independent moment actuators and solve the three first-moment equations as hard constraints at every step;
3. permit simultaneous deletion of old vertices incident to the residual basin, so the operation is a true replacement rather than an additive cap;
4. enumerate the resulting branch-specific circuit flips before applying any metric polishing;
5. require both normalized P and Q inactive slacks above `10^-5` and a positive target hard margin above `10^-6` before exactification.

Still-open combinatorial domains are branch-specific double/multiple deletions combined with insertion, Y-patches whose counterrail is not a complete symmetry image, and nonlinear nullspace controls of the moment map. The single-rail cells, pure C2/C3/C4 unions, all single deletions, and the tested affine/metric orbit should not be repeated unchanged.

## Reusable artifacts

- [Complete continuation bundle](sandbox:/mnt/data/santalo_asym_two_rail_family_bundle.zip)
- [Root report](sandbox:/mnt/data/santalo_asym_two_rail_family/root_report.json)
- [Family and complete topology graph](sandbox:/mnt/data/santalo_asym_two_rail_family/family_and_topology_graph.json)
- [Independent binary verifier](sandbox:/mnt/data/santalo_asym_two_rail_family/verify_family_standalone.py)
- [Independent interval/Krawczyk verifier](sandbox:/mnt/data/santalo_asym_two_rail_family/interval_certificate_standalone.py)
- [Normalized Q V-coordinates](sandbox:/mnt/data/santalo_asym_two_rail_family/Q_centered_normalized_V.csv)
- [Normalized P V-coordinates](sandbox:/mnt/data/santalo_asym_two_rail_family/P_centroid_normalized_V.csv)
- [P H-coordinates](sandbox:/mnt/data/santalo_asym_two_rail_family/P_H.csv)
- [Q H-coordinates](sandbox:/mnt/data/santalo_asym_two_rail_family/Q_H.csv)
- [Q OBJ](sandbox:/mnt/data/santalo_asym_two_rail_family/Q_centered_normalized.obj) and [Q STL](sandbox:/mnt/data/santalo_asym_two_rail_family/Q_centered_normalized.stl)
- [P OBJ](sandbox:/mnt/data/santalo_asym_two_rail_family/P_centroid_normalized.obj) and [P STL](sandbox:/mnt/data/santalo_asym_two_rail_family/P_centroid_normalized.stl)
- [Prior exact rational C=104 anchor bundle](sandbox:/mnt/data/santalo_asymmetric_nearobject_bundle.zip)

Both standalone verifiers return `PASS` after a clean unzip. Bundle SHA-256: `e367b454b81ed826f4c217059e4cc7f38f82b1878826eb3a7194ffb171ef3b7d`. Manifest SHA-256: `e161ddfbbfce37b94b81b5e1919f17a66d7b95b4c5895c7740934785f483531e`.
