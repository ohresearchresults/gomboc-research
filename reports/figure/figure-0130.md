# figure-0130

AI research report · 2026-08-28 UTC

---

# P9 shared-multiwall assignment — exact nonwinner handoff

## Literal verdict

No own-centroid strict `(S,U,H)=(1,1,0)` endpoint was found. I reconstructed the exact dyadic nine-support `P9`, built and exactified one genuinely communicating, biconnected three-lobe successor, hard-eliminated all three ordinary volume moments on every audited path cell, and enumerated all four edge-cone components on every true edge after every circuit crossing. The old defect labels disappear, but the Euler-neutral `(2,2,2)` block transfers to new features. The exact homotopy also proves that source rows `15` and `13` deactivate at two distinct circuit events, not at one shared wall.

There is a literal incompatibility in the assignment text: an active unstable incidence `(15,26,27)` cannot coexist with deactivation of support row `15`. I therefore used the interpretation already present in the durable journal—preserve the intended unstable **lineage**—and its final successor is `(o26,o27,A1)`. If literal preservation of `(15,26,27)` is required, row `15` must remain irredundant and only its stable-face status may be destroyed.

## What changed relative to the supplied journal

The journal supplied the exact nine-row seed and a 14-row biconnected `(2,2,2)` successor, but not a literal exact path or a compact rebuilt endpoint for this assignment. New work here is: (i) an independently reconstructed exact P9 fixture; (ii) a new 15-input/11-active dyadic communicating endpoint of complexity `54`; (iii) an 18-event exact circuit homotopy with Sturm isolators; (iv) hard actual-cell moment elimination at every open sample; (v) complete exact four-component ledgers for all 483 true-edge instances; and (vi) a clean-room verifier plus watertight source and endpoint meshes. The new endpoint is smaller than the inherited 14-support successor, but it remains `(2,2,2)`.

## Exact source P9

The nine rows are the following hexadecimal binary64 values, interpreted as exact dyadic rationals, with support constant one. This reconstructs the durable journal seed. :contentReference[oaicite:0]{index=0} The full exact reconstruction is in `p9_exact_data.json`.

```text
9    [ 0x1.f9b5a727c027ap+2, -0x1.81e6cb4c6d6eap+1, -0x1.4a0af64ced04fp-2 ]
13   [ 0x1.2312b52c53f2cp+3, -0x1.59f7623ebb977p+2, -0x1.f2e1addf798e5p+0 ]
15   [ 0x1.1e27bebfbb450p+3, -0x1.609be75d7e57bp+2, -0x1.02e2854657074p+1 ]
26   [ -0x1.825d860acd07ep+0, 0x1.16d2525ea2eb7p+2, 0x1.dfe0ae19e623ap+0 ]
27   [ -0x1.5ed34a3e982c2p+3, 0x1.2c70c33c74c4ep+1, -0x1.cf8630f42f365p-7 ]
32   [ -0x1.16a333bb56517p+3, 0x1.bc6717ba18082p+1, 0x1.5ed14b53bf699p+0 ]
100  [ 0x1.4dbecdd9c4575p+1, -0x1.c5781d3f7120ap+1, -0x1.70ccef918f03ap+0 ]
102  [ -0x1.8f22b39e7cba9p+2, 0x1.069f7cc4abd26p+2, 0x1.4ed4b718d4723p+0 ]
103  [ -0x1.120c08072fbc0p+3, 0x1.6ca725454c6cep+1, 0x1.002b4abeac9d2p+0 ]
```

- `(F,E,V,C)=(9,21,14,42)`.
- Exact own centroid after `h_i=q_i/(1-q_i·c)` is zero.
- Minimum nonincident support slack: `0.011478213633222727...`.
- Strict class `(2,2,2)`.
- Stable rows: `15,27`.
- Unstable incidences: `(9,100,103)`, `(15,26,27)`.
- Saddle edges: `(13,26)`, `(27,100)`.

Face cycles:

```text
9:0 1 3 4 5 2; 13:0 6 1; 15:0 2 8 7 6; 26:1 6 7 9 10 3;
27:7 8 13 12 11 9; 32:3 10 11 12 4; 100:2 5 13 8;
102:9 11 10; 103:4 12 13 5.
```

## Exact communicating endpoint

The raw polar support points use common denominator `2^40`; the literal integer rows are:

```text
o9    6765437898702  -2581316426340  -275959301528
o13   4605263307770  -2736883330069  -986642668900
o15   2581357808180  -1590412860219  -583839025123
o26  -1879167028014   5424423609568   2333983428883
o27 -16987506990962   3636948352501    -21918514707
o32  -6318177561425   2519236572802    994359850935
o100  2764773889779  -3756576306932  -1527587040428
o102 -7241336376554   4764650630565   1518671597103
o103 -6496518748920   2161102387765    759088512384
A0   10843690488563  -6096078707642  -1928810785061
A1    6447454901086  -2033526294598   -776980560215
A2    4992922145117  -3019618419007  -1215126531394
B     1475396860710  -2706792701859  -1005968008466
C0    2528932323855  -3738078041097  -1678492701058
C1   -7210153947534   1222832734528    210007888669
```

Its raw polar volume is `0.37076267580277467...` and raw centroid is approximately

```text
(-0.006258089091537749, -0.11049601892830112, 0.23216971222264050).
```

The exact fractions are in `p9_exact_data.json`. Applying `h_i=q_i/(1-q_i·c)` gives exactly zero ordinary first moments.

Exact endpoint audit:

- Active supports: `o9,o26,o27,o32,o100,o102,A0,A1,B,C0,C1`.
- Strictly inactive: `o13,o15,o103,A2`.
- `(F,E,V,C)=(11,27,18,54)`.
- Minimum exact nonincident slack: `0.024736350632942522...`.
- Support graph is biconnected and has no articulation vertex.
- Strict class `(2,2,2)`.
- Stable: intended `o27` (`+0.4699601338638104`) and extra `A0` (`+0.4215566311903140`).
- Unstable: intended-lineage `(o26,o27,A1)` with cone coefficients `(1.858995...,4.756203...,10.379247...)`; extra `(o9,o32,C1)` with `(4.818311...,4.512737...,1.581662...)`.
- Saddles:
  - `(o9,o26)`: four exact components approximately `(0.9205086392,0.07949136084,0.04842372694,0.07706605062)`;
  - `(o27,C0)`: `(0.05145358723,0.9485464128,0.03467274700,0.1173458341)`.
- Closest non-equilibrium raw primitives are separated: face `-0.09901021268`, vertex `-0.4009338009`, edge `-0.002270969398`. These are exact rational signs, not tolerance classifications.

Face cycles:

```text
o9:   0 2 4 3 1
o26:  5 7 0 1 8 6
o27:  11 12 10 9 5 6 13
o32:  2 0 7 9 10
o100: 14 16 12 11 15
o102: 9 7 5
A0:   3 14 15 17 8 1
A1:   8 17 13 6
B:    4 16 14 3
C0:   15 11 13 17
C1:   4 2 10 12 16
```

The defect is genuinely communicating, not a set of disjoint caps: `A0` touches the `(o9,o26)` saddle star, `A0-C0` and `C1-o27-C0` cross-link the return lobe, and `A0-o9-C1` connects the extra stable and extra unstable sectors. The complete active support graph is biconnected.

## Exact transferred block

```text
source extra stable o15          -> final extra stable A0
source extra U (o9,o100,o103)    -> final extra U (o9,o32,C1)
source saddle (o13,o26)          -> final saddle (o9,o26)
source saddle (o27,o100)         -> final saddle (o27,C0)
source target stable o27         -> final target stable o27
source target-U lineage          -> final facet (o26,o27,A1)
```

Thus all requested old labels are destroyed or made inactive, but the Morse block is transferred rather than cancelled.

## Exact circuit path and hard moment closure

The affine raw-polar homotopy has 18 material circuit roots. Every root is isolated by a rational Sturm interval of width `129/2^80`; full polynomial coefficients, intervals, signs and facet changes are in `p9_circuit_roots.json` and `p9_circuit_path.json`.

```text
 1  o9,o13,o15,o100             t≈0.17854791123343175
 2  o13,o15,o26,o27             t≈0.30012444272230060
 3  o13,o15,o27,o100            t≈0.36791688435064634   o15 deactivates
 4  o13,o26,o27,A1              t≈0.40641781645262115   A1 activates
 5  o9,o13,o100,A0              t≈0.63638279068263381   A0 activates
 6  o9,o13,o26,A1               t≈0.65609633275108292
 7  o9,o13,A0,A1                t≈0.68353015622384894
 8  o27,o100,o103,C1            t≈0.71107446234029126   C1 activates
 9  o13,o27,o100,C0             t≈0.74749712894340103   C0 activates
10  o9,o100,o103,C1             t≈0.75858504689746897
11  o9,o32,o103,C1              t≈0.77691179742910643
12  o13,o27,A1,C0               t≈0.78196501942553787
13  o13,o100,A0,C0              t≈0.80257412980034648
14  o27,o32,o103,C1             t≈0.83543352328016085   o103 deactivates
15  o13,A0,A1,C0                t≈0.83591670857259259   o13 deactivates
16  o9,o100,B,C1                t≈0.86805436471401975   B activates
17  o9,o26,A0,A1                t≈0.92713402399776046
18  o9,o100,A0,B                t≈0.94330981572107708
```

This is decisive for the requested shared event: `o15` leaves at event 3 and `o13` leaves at event 15. They do not deactivate together. Mechanical sign walls also occur inside some fixed-incidence intervals; the exact source and every reported audit sample are open, and no wall point is accepted.

For every rebuilt open cell, I recomputed the actual raw polar face lattice, exact ordinary volume and first moment, then made the three support coordinates dependent via

```text
h_i(t)=q_i(t)/(1-q_i(t)·c(t)),  c(t)=M(P_raw(t))/V(P_raw(t)).
```

Consequently all three centred first moments are the exact rational vector `(0,0,0)` in every recorded cell. No topology or moment formula was inherited across a circuit.

## Four-component edge-cone audit

There are 19 open audit samples (before the first circuit and after each of 18 circuits), containing 483 true-edge instances. For every instance the exact four-component vector

```text
[t, 1-t, alpha, beta]
```

is recorded in `p9_edge_four_components.csv`, together with the exact list of nonpositive exclusion components. The independent verifier checks that each sample has exactly its reconstructed true-edge count and that all four rational components are parseable and sign-consistent. The companion face and vertex ledgers contain every primitive, not only the equilibria.

## Smallest new shared event

The smallest untested event exposed by the endpoint is a connected four-circuit double-Y/prismatic replacement, not another rail:

1. cross the complete `(o9,o26,A0,A1)` star to remove `A0` and saddle `(o9,o26)`;
2. cross the `(o9,o32,B,C1)` / `(o9,o100,B,C1)` sector to destroy extra facet `(o9,o32,C1)`;
3. cross the `(o27,o100,A1,C0)` sector to remove saddle `(o27,C0)`;
4. add two transverse cross-links so `A0,o9,C0,C1` can become non-extreme in one rebuilt cell while `(o26,o27,A1*)` and stable `o27` remain protected.

A practical minimal parameterization is four new extreme rows arranged as two coupled forks plus one shared quadrilateral belt. Three branch-depth coordinates must be eliminated by the exact moment equations before any mechanical score. All four edge-cone components must be branched independently; tree/cotree shorthand is insufficient. This event is smaller and more specific than another 10–14-row annulus because the exact endpoint has already compressed the old block into one 11-support biconnected hub.

## Reproducibility

`verify_p9_transfer_independent.py` is a clean-room standard-library `Fraction` verifier. It independently reconstructs all triple intersections, irredundant rows, maximal face cycles, true edges, exact volume/centroid, all face primitives, all vertex cone coefficients and all four edge-cone components; it also checks OBJ watertightness and the 19-cell path ledgers. Its recorded result is `OVERALL PASS`.

The complete artifact bundle includes exact JSON/CSV data, the 18 exact circuit polynomials and Sturm intervals, generator and verifier source, verification transcript, and source/endpoint OBJ/STL meshes.

## Artifact links

- [Complete ZIP bundle](sandbox:/mnt/data/P9_shared_multiwall_nonwinner_bundle.zip).
- [Exact H/V, centroid and full endpoint/source audits](sandbox:/mnt/data/p9_exact_data.json).
- [Clean-room independent exact verifier](sandbox:/mnt/data/verify_p9_transfer_independent.py) and [verification transcript](sandbox:/mnt/data/verification_report.txt).
- [Exact circuit path](sandbox:/mnt/data/p9_circuit_path.json), [Sturm-isolated roots](sandbox:/mnt/data/p9_circuit_roots.json), and [19-cell audit summary](sandbox:/mnt/data/p9_path_summary.md).
- [All 483 true-edge four-component audits](sandbox:/mnt/data/p9_edge_four_components.csv), [face ledger](sandbox:/mnt/data/p9_face_ledger.csv), and [vertex ledger](sandbox:/mnt/data/p9_vertex_ledger.csv).
- Meshes: [source OBJ](sandbox:/mnt/data/P9_exact_source.obj), [source STL](sandbox:/mnt/data/P9_exact_source.stl), [endpoint OBJ](sandbox:/mnt/data/P9_connected_transfer_nonwinner.obj), [endpoint STL](sandbox:/mnt/data/P9_connected_transfer_nonwinner.stl).
- [Standalone Markdown handoff](sandbox:/mnt/data/P9_RESEARCH_HANDOFF.md).

Bundle ZIP SHA-256: `f340fd644f2e753d39e656f5f73fdb76b8ad60fc4416686391328abfb9e511d3`.
