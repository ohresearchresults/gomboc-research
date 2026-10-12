# figure-0114

AI research report · 2026-08-27 UTC

---

# Verdict

No literal homogeneous polyhedral Gömböc was reached in this direction. The materialized endpoint below is an exact, finite, own-centred **nonwinner** with strict `(S,U,H)=(2,2,2)`. This respects the journal’s acceptance gate: an auxiliary-centre object, a wall point, or a merely formal mixed-volume identity is not reported as completion. :contentReference[oaicite:0]{index=0}

What is new relative to the supplied journal is a fully expanded Minkowski construction: four asymmetric full-dimensional rational polytopes, their exact common normal fan, all 20 mixed-volume coefficients and all `3×35` mixed first-moment coefficients, an exact isolated positive centroid root, literal irredundant H/V data, every maximal face and true edge, a complete exact equilibrium ledger, a certified perturbation box, an independent verifier, and watertight OBJ/STL. The journal supplied the reconstructible nine-support `P9` seed and its incidence/equilibrium block, :contentReference[oaicite:1]{index=1} while the present assignment introduced Minkowski mixed-moment synthesis as a new architecture. :contentReference[oaicite:2]{index=2}

## Exact finite construction

Use the nine dyadic outward normals below. Every hexadecimal literal is interpreted exactly as a binary rational.

| source row | `a_ix` | `a_iy` | `a_iz` |
|---:|---|---|---|
| 9 | `0x1.f9b5a727c027ap+2` | `-0x1.81e6cb4c6d6eap+1` | `-0x1.4a0af64ced04fp-2` |
| 13 | `0x1.2312b52c53f2cp+3` | `-0x1.59f7623ebb977p+2` | `-0x1.f2e1addf798e5p+0` |
| 15 | `0x1.1e27bebfbb450p+3` | `-0x1.609be75d7e57bp+2` | `-0x1.02e2854657074p+1` |
| 26 | `-0x1.825d860acd07ep+0` | `0x1.16d2525ea2eb7p+2` | `0x1.dfe0ae19e623ap+0` |
| 27 | `-0x1.5ed34a3e982c2p+3` | `0x1.2c70c33c74c4ep+1` | `-0x1.cf8630f42f365p-7` |
| 32 | `-0x1.16a333bb56517p+3` | `0x1.bc6717ba18082p+1` | `0x1.5ed14b53bf699p+0` |
| 100 | `0x1.4dbecdd9c4575p+1` | `-0x1.c5781d3f7120ap+1` | `-0x1.70ccef918f03ap+0` |
| 102 | `-0x1.8f22b39e7cba9p+2` | `0x1.069f7cc4abd26p+2` | `0x1.4ed4b718d4723p+0` |
| 103 | `-0x1.120c08072fbc0p+3` | `0x1.6ca725454c6cep+1` | `0x1.002b4abeac9d2p+0` |

Let `P_raw={x:a_i·x≤1}`. Exact signed-tetrahedron integration gives

`centroid(P_raw)=c≈(0.09557254662666256, 0.4389030282873355, -0.8807270244051993)`.

Put `s_i=1-a_i·c`. Then `P=P_raw-c={x:a_i·x≤s_i}` has centroid exactly zero. The support values are approximately

`(1.2841776971632544, 0.7869354265149329, 0.7821960100102323, 0.8830648990720585, 1.0051419707738976, 1.5152964261048214, 1.0369204342789538, 0.9469380008447836, 1.4494198352241632)`

in the row order above; their unabbreviated exact fractions are in the certificate and H-table.

Define `R={26,27,32}` and `r_1=26,r_2=27,r_3=32`. All four summands use the same normals `a_i`:

- `B={x:a_i·x≤b_i}`, where `b_i=(160/256)s_i` for `i∉R` and `b_i=(159/256)s_i` for `i∈R`;
- `C_j={x:a_i·x≤c_i^(j)}`, where `c_i^(j)=(32/256)s_i` except `c_(r_j)^(j)=(33/256)s_(r_j)`.

Thus `b_i+c_i^(1)+c_i^(2)+c_i^(3)=s_i` exactly. Exact triple-intersection enumeration proves that `B,C_1,C_2,C_3` are full-dimensional, asymmetric and irredundant, and all have the same 14 active normal triples. Therefore their common refinement is exactly that nine-ray fan and

`B+C_1+C_2+C_3=P`.

This is not a homothetic or translation-only decomposition: the three correctors bump three different support rows, their centroids differ, and the three-moment Jacobian below is nonsingular.

The minimum exact inactive halfspace slack in each summand is strictly positive:

| summand | minimum inactive slack | volume | centroid, decimal |
|---|---:|---:|---|
| `B` | `0.004951433395834314` | `0.10661615261963175` | `(-0.000132791827,-0.001266780196,0.001883424706)` |
| `C_1` | `0.002174112012061255` | `0.0008797495642827221` | `(0.000464877678,0.001755038946,-0.002471773632)` |
| `C_2` | `0.002174112012061255` | `0.0008767457278204767` | `(0.000021891532,0.001024691709,-0.002622678056)` |
| `C_3` | `0.003673077352673228` | `0.0008709044899537321` | `(-0.000317671421,-0.001386945383,0.002992177692)` |

For every `t_1,t_2,t_3>0`, the candidate

`P(t)=B+t_1C_1+t_2C_2+t_3C_3`

has the same fan. Indeed, for each active cone `I` and inactive row `k`, its slack is the positive linear combination

`σ_(k,I)(t)=σ_(k,I)^B+t_1σ_(k,I)^(C_1)+t_2σ_(k,I)^(C_2)+t_3σ_(k,I)^(C_3)>0`.

So the common fan and every maximal face/true edge are globally fixed throughout the positive orthant; no tolerance-based incidence decision is used.

## Exact mixed-volume and mixed-first-moment system

Write

`V(t)=Σ_(|α|≤3) v_α t^α`,  
`M_q(t)=Σ_(|α|≤4) m_(q,α)t^α`, `q∈{x,y,z}`.

The exact coefficient normalization is the ordinary Minkowski polarization: with `α_0=3-|α|`,

`V(B[α_0],C_1[α_1],C_2[α_2],C_3[α_3]) = v_α α_0!α_1!α_2!α_3!/3!`,

and analogously, with degree four, for each mixed first-moment component. There are exactly 20 nonzero `v_α` and 35 nonzero coefficients in each of `M_x,M_y,M_z`. Every coefficient is stored as its full integer numerator and denominator in [mixed_coefficients.csv](sandbox:/mnt/data/minkowski_gomboc_slot9/artifact/mixed_coefficients.csv) and redundantly in [certificate.json](sandbox:/mnt/data/minkowski_gomboc_slot9/artifact/certificate.json); the independent verifier recomputes all 125 coefficients from the summand H-data rather than trusting the table.

For scale orientation, the 20 volume coefficients are:

| `α` | `v_α` decimal | `α` | `v_α` decimal |
|---|---:|---|---:|
| 000 | 0.10661615261963175 | 001 | 0.06444346211622384 |
| 010 | 0.06456603450178573 | 100 | 0.06463975473066213 |
| 002 | 0.01297885367432595 | 011 | 0.02601544407047814 |
| 020 | 0.01303233797898122 | 101 | 0.02604517636140283 |
| 110 | 0.02609494604787284 | 200 | 0.01306212139916160 |
| 003 | 0.0008709044899537321 | 012 | 0.002619455747746258 |
| 021 | 0.002625291666507056 | 030 | 0.0008767457278204767 |
| 102 | 0.002622486823692457 | 111 | 0.005256703463881821 |
| 120 | 0.002633340849068157 | 201 | 0.002631308543398016 |
| 210 | 0.002636344923937822 | 300 | 0.0008797495642827221 |

The complete nonlinear ordinary-centroid equations are `M_x=M_y=M_z=0`. They have the exact positive solution

`t_*=(1,1,1)`,

at which `V=0.44114661530081456…` and all three first moments are exactly zero. The exact Jacobian at this root is approximately

```text
[ 2.0626398084634432e-4   9.748926782251819e-6  -1.549704705921905e-4 ]
[ 7.8256097410736800e-4   4.544010510453881e-4  -6.708324567129901e-4 ]
[-1.1056446543256518e-3  -1.161761772936956e-3   1.424458060975137e-3 ]
```

with exact determinant `>0`, numerically `3.215488095177061×10^-11`. An exact rational interval-Krawczyk computation gives infinity-norm contraction `0.724545822353025<1` on

`|t_i-1|≤1/64`,

so `(1,1,1)` is the unique root in that positive box. This is a full finite polynomial solve, not an infinitesimal centroid correction.

## Literal H/V incidence reconstruction

The final polytope has

`(V,E,F,C)=(14,21,9,42)`.

Its 14 exact vertices are the intersections of these active label triples, in vertex order `0,…,13`:

```text
(9,13,15), (9,13,26), (9,15,100), (9,26,32),
(9,32,103), (9,100,103), (13,15,26), (15,26,27),
(15,27,100), (26,27,102), (26,32,102), (27,32,102),
(27,32,103), (27,100,103).
```

Each coordinate is the exact rational solution `v_I=A_I^{-1}s_I`; all literal fractions are in [final_V.csv](sandbox:/mnt/data/minkowski_gomboc_slot9/artifact/final_V.csv). The exact irredundant halfspaces are in [final_H.csv](sandbox:/mnt/data/minkowski_gomboc_slot9/artifact/final_H.csv), and all four summand H/V tables are in [summands_H.csv](sandbox:/mnt/data/minkowski_gomboc_slot9/artifact/summands_H.csv) and [summands_V.csv](sandbox:/mnt/data/minkowski_gomboc_slot9/artifact/summands_V.csv).

The outward maximal-face cycles are:

```text
9:   0 1 3 4 5 2
13:  6 1 0
15:  7 6 0 2 8
26:  1 6 7 9 10 3
27:  9 7 8 13 12 11
32:  10 11 12 4 3
100: 8 2 5 13
102: 9 11 10
103: 12 13 5 4
```

Every true edge, with its two incident maximal-face labels, is:

```text
0-1(9,13); 0-2(9,15); 0-6(13,15); 1-3(9,26); 1-6(13,26);
2-5(9,100); 2-8(15,100); 3-4(9,32); 3-10(26,32); 4-5(9,103);
4-12(32,103); 5-13(100,103); 6-7(15,26); 7-8(15,27);
7-9(26,27); 8-13(27,100); 9-10(26,102); 9-11(27,102);
10-11(32,102); 11-12(27,32); 12-13(27,103).
```

The minimum raw inactive final-halfspace slack is exactly positive, numerically `0.017392896096490036`.

## Exhaustive own-centroid equilibrium audit

All tests use the exact centroid `(0,0,0)` and every complete maximal face, vertex star, and two-generator full normal cone of every true edge.

For a face, the verifier evaluates every exact oriented in-plane wedge of the orthogonal foot. For a vertex it evaluates `-v·(w-v)` on every true incident edge. For an edge it evaluates the four exact numerator components: the two interior line-projection conditions and the two positive coefficients in the complete incident-normal cone. No triangulation diagonal is treated as a true edge.

The strict result is:

- stable rows: intended `27` and unwanted `15`;
- unstable vertices: intended `(15,26,27)` and unwanted `(9,100,103)`;
- saddle edges: `(13,26)` and `(27,100)`;
- therefore `(S,U,H)=(2,2,2)` and `S+U-H=2` exactly.

The raw positive primitive minima are:

- stable-face minimum: `0.08666370968505173` on extra row `15`;
- unstable-vertex minimum: `0.0008876711173775433` on extra vertex `(9,100,103)`;
- saddle minimum: `0.11388166754443212` among the two positive saddle records.

The intended row `27` has raw face score `2.7194134295837635`; intended unstable triple `(15,26,27)` has raw score `11.102746186899935`. The two saddle records have raw minima `0.2366897144791517` for `(13,26)` and `0.11388166754443212` for `(27,100)`. Every other feature is strictly excluded. The closest excluded face is row `13` at `-0.008970865731113808`; the closest excluded vertex is `(9,32,103)` at `-0.000145197661166542`; and the closest nonsaddle edge is the true edge between vertices `4,5`, incident to rows `(9,103)`, at `-0.000145197661166542`.

The full exact primitive ledger—every wedge, every vertex-neighbour product, and all four components of every edge cone—is in `equilibrium_audit` in the certificate.

An exact outward interval audit certifies unchanged incidence and the complete `(2,2,2)` class for the independent support box

`|δh_i|≤2^-27 h_i` for all nine rows.

The certified inactive-slack lower bound over that whole box remains `0.01739277191709035…`. Hence the residual four-feature block is open, not a wall artefact.

## Rigorous obstruction obtained

The first rigorous obstruction is local but complete:

1. the four summands have one exact common fan for every positive parameter vector, so this family cannot cross a circuit or change topology anywhere in the positive orthant;
2. the full nonlinear centroid system has an isolated positive root at `(1,1,1)`;
3. at that root the exact extra stable face, extra unstable vertex and two saddle cones have the positive margins listed above;
4. an independent nonzero support box preserves the entire defect block.

Thus rank and exact mass closure are solved, but **a fixed common fan merely preserves the Euler-neutral transfer block**. A winner in this architecture must introduce at least one summand whose fan genuinely replaces the stars of row `15`, vertex `(9,100,103)`, and both saddle pairs; same-fan polishing is rigorously insufficient near the materialized root.

This is not claimed as a global impossibility theorem for arbitrary Minkowski summands. Exploratory fan-changing searches with segment, segment-pair, simplex and tetrahedral correctors on P9, the one-pair skew-prismatoid seed, and the Conway mechanical seed produced only transferred `(2,2,2)` or larger blocks; those searches are observations, not certificates.

## Most useful continuation

Retain `C_1,C_2,C_3` as exact three-axis moment controls: their mixed first-moment Jacobian is already full rank. Add a fourth topology-changing asymmetric summand `D(λ)` whose normal fan inserts a communicating three-branch patch across the complete stars of row `15`, `(9,100,103)`, `(13,26)` and `(27,100)`, while leaving the intended row `27` and intended triple `(15,26,27)` inside protected separator cones. In each common-refinement cell, eliminate `(t_1,t_2,t_3)` through the exact three moment equations, enumerate every actual maximal face and full edge cone, and cross the two saddle circuits together rather than serially. The present exact polynomial/audit package is reusable as the seed and dependent-moment subsystem for that continuation.

## Reproducible artifact bundle

- [Complete ZIP bundle](sandbox:/mnt/data/minkowski_gomboc_slot9/minkowski_common_fan_fallback.zip) — SHA-256 `1c273ef52eac0e30de335a780be56f5e0923c91958f8865683124df8022c97ae`.
- [Exact certificate](sandbox:/mnt/data/minkowski_gomboc_slot9/artifact/certificate.json) — all rational data, coefficients, incidence and primitive ledgers.
- [All mixed coefficients](sandbox:/mnt/data/minkowski_gomboc_slot9/artifact/mixed_coefficients.csv).
- [Independent clean-room verifier](sandbox:/mnt/data/minkowski_gomboc_slot9/artifact/verify_independent.py) and [verification transcript](sandbox:/mnt/data/minkowski_gomboc_slot9/artifact/verification.txt).
- [OBJ](sandbox:/mnt/data/minkowski_gomboc_slot9/artifact/final_p9.obj) and [STL](sandbox:/mnt/data/minkowski_gomboc_slot9/artifact/final_p9.stl).

The verifier, run from a clean extraction of the ZIP, reports: exact H/V reconstruction; `(14,21,9)` incidence; centroid exactly zero; identical irredundant fan and exact metric asymmetry for all four summands; exact recomputation of `20+3×35` coefficients; isolated root `(1,1,1)`; exhaustive `(2,2,2)` mechanics; certified `2^-27` support box; and a watertight 24-triangle STL with every triangulation edge occurring exactly twice.
