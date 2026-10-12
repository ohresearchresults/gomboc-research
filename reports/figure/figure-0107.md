# figure-0107

AI research report · 2026-08-27 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Literal verdict

**NONWINNER.** The selected distributed three-profile moment zero is rigorously isolated only for a counterfactual fixed-incidence rational map. The actual 4,324-row polytope reaches an exactly isolated four-row circuit wall first. I crossed that wall, rebuilt and certified the next complete H/V cell, resumed the isolated-root search, and found that the selected post-flip zero again lies beyond a second exact circuit wall. No own-centroid `(1,1,0)` object is claimed.

The acceptance gate remains a finite uniform-density body at its own exact volume centroid, with complete H/V incidence, maximal faces, true edges, full normal cones, independent directed verification, and OBJ/STL; an artificial centre or near-wall state is insufficient. The journal had recorded this branch as a certification-boundary problem after independently reconstructing the 4,324-row cover.

## Correction to the predecessor state

The predecessor prose said a candidate box had been retained, but its actual saved `selected_summary.json` contains `RuntimeError: No usable 4324x3 polar candidate found`. I therefore reconstructed the exact source and profile family instead of assuming a hidden candidate. This handoff is the first actual exact/directed result for that family.

## Exact finite family

The source uses

```text
beta=1/160,
eta(theta)=(3*pi/2)(cos(theta)-cos(theta)^3/3),
P(theta)=eta(theta)-(1/3)sin(3 eta(theta)),
R(theta,phi)^4=1+4 beta sin(theta) cos(phi-P(theta)).
```

The deterministic polar construction has row `0` as the stable cap, rows `1..4320` as 120 rings of 36, and rows `4321..4323` as the terminal unstable fan. After exact dyadic rounding,

```text
q_i^0 = 2^-48 Qint_i,
q_i(t)=2^-48 Qint_i*(1+2^-24 sum_j Fint[i,j] t_j).
```

All `Qint` and all 12,972 `Fint` integers are supplied in the exact generator. The fields are `band_r14_p1`, `band_r62_p0`, `band_r108_p0`; 850 protected rows have all coefficients zero. For the first circuit, field 1 is

```text
F548=14922663/16777216,
F549=3873727/4194304,
F583=3440409/4194304,
F584=0.
```

## Reconstructed baseline

```text
H=4324 (all irredundant), V=8644, E=12966, Euler=2
volume  = 4.201080076519372
moment  = (0.1260434949394386,-3.511272882758962e-13,-3.026945761872991e-12)
centroid= (0.030002640426665374,-8.358024171888861e-14,-7.205160831832653e-13).
```

At the construction centre the exhaustive class is `(1,1,0)`: stable row `0`, unstable incidence `{4321,4322,4323}`, no saddle edge. An exact interior certificate uses rows `(0,4321,4322,4323)` with positive weights approximately `(0.4769684200,0.1742050270,0.1743732949,0.1744532581)`.

## Isolated fixed-cell zero

Outward interval Newton/Krawczyk isolates one zero of all three ordinary first moments in the baseline fixed-cell formula. Centre:

```text
(36132610862178361550951/604462909807314587353088,
-17924746438423962051953/302231454903657293676544,
-25230168393735655085611/302231454903657293676544)
```

with coordinate radius `1/1180591620717411303424 = 2^-70`. Decimal centre:

```text
(0.0597763903722337570660,-0.0593080109551729363644,-0.0834796245869851900134).
```

Directed volume:

```text
[3.9058296799350154264775829448963702973590166873669354921002634410449924900028742,
 3.9058296799350155684792539111579444188869301225903580405797775895201586319417424].
```

Each moment interval contains zero, with half-width below `3.49e-17`. The Jacobian midpoint is

```text
[-1.1880899531699640, 0.8124769452975354, 5.3017872603728913]
[ 1.6369905772236827,-2.5226617776593048, 4.5315546924008363]
[ 1.8491889592329661,-1.1783730271194727, 2.8573189757399897]
```

and determinant `19.732726948744677241366126768568168627197927629379431038547981...`, so rank is not the obstruction.

## Exact first chamber primitive

On `t=alpha t*`, the first actual wall is the four-row circuit `{548,549,583,584}`. Facets change from

```text
(548,549,584),(548,583,584)
```

to

```text
(548,549,583),(549,583,584).
```

The exact cubic coefficients in descending order are

```text
495149007114004177461671825112711574496323717506372363446335841776929374024450808926973904744506106801408478031696690687266563131
18582300716733662593283786150375302851062676371764581175964387945430185308331330872381548114962210058133569286933588528967649853440
174993446506402034682905697340797336240644272759706631421653492341790460281815733360410815502554448687986531145297501839386814185472
-10716398559883949037960411168562357094924678381058500764021771130450973498109116682394898475672732019442047217356602231301865472.
```

Its unique `[0,1]` root is isolated in

```text
[9703621049662963147932159/158456325028528675187087900672,
 77628968397303705183457273/1267650600228229401496703205376]
```

(`alpha≈6.123845828127031e-5`), at parameters near

```text
(3.660613988014966e-6,-3.631931154623481e-6,-5.112163507606200e-6).
```

The Krawczyk root’s first coordinate begins at `0.059776390372233756`, over `16329.60770186222` times the field-1 wall coordinate. Hence the isolated zero and the true baseline cell are disjoint.

This is exhaustive, not a local guess: `37,350,722` other inactive H/V inequalities were checked; all screen values below `10^-6` were recomputed exactly. The minimum unrelated gap is

```text
1976044857730446312448335921953/
1345230052321984347827656786179996084521
=1.4689270837501888e-9.
```

Across the whole pre-wall interval, interval/exact audits certify stable `[0]`, unstable `{4321,4322,4323}`, all 12,966 true edges nonsaddle, target stable primitive `2.4278889262598243e-4`, nonstable witness `3.9754075256100545e-5`, target unstable coefficient `0.3650071155162056`, and nonunstable witness `0.11597867268977698`.

## Corrected post-flip cell and resumed root search

After the diagonal exchange, the actual topology remains `(H,V,E)=(4324,8644,12966)` and strict construction-centre `(1,1,0)`. The post-flip rational moment map has another interval-Krawczyk zero, centred at

```text
11084197764048582498477790954647392317886127/178405961588244985132285746181186892047843328
-41469169079553611593405234715674796443826261/713623846352979940529142984724747568191373312
-14718529394154625439373125436020098415367961/178405961588244985132285746181186892047843328
```

with radius `2^-90`. Its Jacobian determinant is `17.792812369420333751712452303028865378618206489505816072185829...`; each directed moment interval contains zero with radius below `3.32e-23`.

Along the exact dyadic predictor direction

```text
(8953743648559739/144115188075855872,
-8374632002267397/144115188075855872,
-1486191669938533/18014398509481984),
```

the corrected cell begins just after `lambda≈5.89194971469554e-5` and ends at the next exact circuit `{566,567,601,602}`. Facets change from `(566,567,602),(566,601,602)` to `(566,567,601),(567,601,602)`. The second root is isolated in

```text
[122774593929651469450340609/1267650600228229401496703205376,
 61387296964825734725170305/633825300114114700748351602688]
```

(`lambda≈9.6852077305487e-5`). The entire intervening post-flip chamber was checked against all `37,350,722` nonincident inequalities, all maximal faces, all vertices and all 12,966 edge cones; it remains strict `(1,1,0)`. The local Krawczyk proof does not globally exclude a disconnected moment zero elsewhere in this cell, but it rigorously proves that the selected continuation reaches this second primitive before its isolated zero.

## Strongest materialized endpoint

Choose exact `lambda=5/65536` inside the certified post-flip cell. Its exact parameters are

```text
44768718242798695/9444732965739290427392
-41873160011336985/9444732965739290427392
-7430958349692665/1180591620717411303424.
```

Every endpoint row is `q_i=(n_ix,n_iy,n_iz)/2^145`. All 4,324 integer triples are supplied. Given an active triple of integer rows `(a,b,c)`, the exact primal vertex is

```text
x=2^145*(b×c+c×a+a×b)/det(a,b,c).
```

Thus the supplied H table plus 8,644 active triples is an exact finite H/V expansion. Counts:

```text
H=4324 irredundant, V=8644, E=12966,
4324 maximal-face cycles, 17284 mesh triangles, Euler=2.
```

All `37,350,724` inactive incidences pass; the exact minimum is the `1.4689270837501888e-9` fraction above. At the construction centre, singleton outward intervals certify `(1,1,0)` with minimum primitives

```text
stable target 2.4278889262598243169e-4
nonstable      3.9754075256100547474e-5
unstable       0.36500711551620559918
nonunstable    0.11678661260292817402
nonsaddle      0.11622879031163948892.
```

A nonzero exact ray box centred at `5/65536` with radius

```text
22024729645686869123641737/2535301200456458802993406410752
```

is wholly inside this same incidence/mechanical chamber.

Directed ordinary mass data:

```text
V [4.20108775659362263220023354852406610227129980434297968778125097013612777821204506520459087,
   4.20108775659362263220023354852406610227129980434297968778125097013612777821210445573092386]
Mx[0.126049477848369965387459005376849855299266571843302596454540065333209815126684779627582281,
   0.126049477848369965387459005376849855299266571843302596454540065333209815126697200445198995]
My[-2.1420386373135030657622671370557466380843179418460232209573906416811080088713659e-7,
   -2.1420386373135030657622671370557466380843179418460232209573906416811079866532841e-7]
Mz[-8.5678815534241434143784810832763470817401553010990182210524589102323794361804207e-7,
   -8.5678815534241434143784810832763470817401553010990182210524589102323794139147801e-7].
```

The centroid has strictly positive x:

```text
x in [0.0300040097116597595220198891047362286360543108648563746104160818690528287428906102,
      0.0300040097116597595220198891047362286360543108648563746104160818690528287428939910].
```

At that exact own centroid, two distinct actual maximal faces are interval-certified stable: row `0` with primitive lower bound `2.3539115990588503159e-4`, and row `543` with lower bound `1.3377209337313511192e-5`. Therefore `S>=2`, a rigorous nonwinner certificate.

Independent clean-room reconstruction regenerates all exact H rows, the Q hull, all active V triples, maximal cycles and true edges. OBJ/STL are watertight: 8,644 vertices, 17,284 triangles, 25,926 mesh edges, every edge incident twice, Euler 2; signed OBJ volume `4.201087756593621` agrees with the directed enclosure up to export rounding.

## Smallest continuation

Do not restart the family and do not introduce pyramid actuators. Both proven walls lie between rings 15 and 16, in quads `{548,549,583,584}` and `{566,567,601,602}`. Keep the other 4,316 profiles and both critical patches frozen. Replace only the inherited `band_r14_p1` values on the complete one-rings of these eight rows by two exact dyadic collar variables, one per circuit; retain the three distributed fields as dependent moment variables. Cross both diagonal events in a certified order or one two-circuit event, run interval Newton in each resulting cell, and stop at the next exact primitive rather than a floating residual.

## Artifacts

Complete handoff (`COMPLETE_HANDOFF.md`)

Full reproducible package (`distributed_profile_certification.zip`) — SHA-256 `96f8bf25b27baf6ee92eb39d9baa1ea2979d23d80565372a06b39817d83e8577`.

Exact row/profile and active-V generator (`endpoint_generator.json`)

Watertight OBJ (`endpoint.obj`)

Watertight STL (`endpoint.stl`)

SHA-256 manifest (`SHA256SUMS.json`)
