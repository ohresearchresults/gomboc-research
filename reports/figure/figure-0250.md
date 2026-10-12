# figure-0250

AI research report · 2026-09-03 UTC

---

The durable journal requires a finite uniform-density polyhedron evaluated at its own exact ordinary-volume centroid, with strict `(S,U,H)=(1,1,0)`, complete H/V/true-edge mechanics, an independent verifier, and matching OBJ/STL; auxiliary-centre, wall, near-solution, and unexpanded theorem objects do not qualify. :contentReference[oaicite:0]{index=0}

The accepted source is the exact seventh-cage `(V,E,F)=(12,30,20)`, `(S,U,H)=(2,2,2)` body whose remaining packet is the external-positive edge `[0,1975]`, stable `[G,L,M]`, unstable `1975`, and saddles `[1975,H]`, `[C,L]`; the journal identifies a closed three-support/eighth-support cage changing that whole star as the first nonserial successor. :contentReference[oaicite:1]{index=1}

# Calm Quartz 90 — exact eighth three-support carrier cage

## Disposition

**EXACT DELIMITED NONWINNER.** No strict own-centred `(1,1,0)` polyhedron occurs in the exact open chamber materialized here.

A genuine closed three-support cage was realized. New supports `N=40014`, `O=40015`, `P=40016` become extreme; old packet rows `1975`, `G=40007`, and `M=40013` become strictly interior. In one connected same-boundary positive-volume full-hull replacement, the source forcing edge `[0,1975]`, stable face `[G,L,M]`, and saddle `[1975,H]` disappear, while `[C,L]` remains physical but becomes strictly nonsaddle. Protected stable `[0,H,C]` and protected unstable `C` remain strict.

The exact endpoint has

```text
26 supplied dyadic points
11 active vertices; 15 strictly inactive supplied rows
(V,E,F,C)=(11,27,18,54)
(S,U,H)=(2,2,2)
independent coordinate radius 2^-25
```

Its new packet is stable `[N,O,P]`, unstable `0`, saddles `[H,O]` and `[L,P]`, and the unique nonprotected adverse changed edge `[0,N]`.

## Exact generator and own centroid

Every coordinate below is divided by `2^24=16777216`.

```text
0     (   2382238,  -6308946,  46171779) active
1258  (   1581882,   9403814, -20847988) active
1371  (    105592,    109668,    616980) inactive
1975  (    456217,   -193326,    129442) inactive
2152  (    510389,  -7271935,  -5924598) inactive
2369  (    135538,     76357,    619136) inactive
2515  (   5028442,  -9339607,  26833667) inactive
2732  (     91562,     46167,    611979) inactive
3290  (    661958, -10721838,  16427750) inactive
3296  (   3876214,  -1521484,   3638813) inactive
A     (   -351024,  -8978438,  25844631) inactive
B     (         0,         0,         0) inactive
C     ( -19656014, -12570508, -84150451) active
D     (  -2672244,   3411514, -42213909) active
E     (  -6361824,   2058745, -51264980) active
F     (  -4952003,   7634514, -41535864) active
G     (     42366,   -252135,    270818) inactive
H     (  -1678613,  11935619, -25478204) active
I     (     37357,    237671,    -70651) inactive
J     (     -7462,   -116421,     97771) inactive
K     (    203987,    180925,    827032) inactive
L     (   -481137, -21134611,   5046486) active
M     (   1914800,   2008366,   2982633) inactive
N     (  12461339,   1825560,  42485908) active
O     (  12441885,  14051181,  26217773) active
P     (  -7709040, -16724117, -56733771) active
```

The minimum exact inactive-row slack is attained by `2515`:

```text
60597491885547796945/2361183241434822606848 > 0
≈ 0.02566403607401705.
```

Exact ordinary volume:

```text
15878309222000815978555/4722366482869645213696
≈ 3.362362764431622.
```

Exact uncentred ordinary-volume centroid:

```text
cx=-74455368710633678861050241309/799181470596898925545405808640
cy=-337020330037256275122487640065/1278690352955038280872649293824
cz=-434858453204963337956161243595/639345176477519140436324646912.
```

Subtracting this single rational vector from all eleven active vertices gives exact first moments `Mx=My=Mz=0`. The physical mechanics below use this own centroid; no auxiliary point or point-mass centre is substituted.

## Actual irredundant hull

The eighteen outward maximal triangular faces are

```text
[0,H,C] stable
[0,C,L]
[0,O,H]
[0,L,N]
[0,N,O]
[1258,D,F]
[1258,O,D]
[1258,F,H]
[1258,H,O]
[C,F,E]
[C,E,P]
[C,H,F]
[C,P,L]
[D,E,F]
[D,P,E]
[D,O,P]
[L,P,N]
[N,P,O] stable
```

The twenty-seven physical true edges are

```text
[0,C] [0,H] [0,L] [0,N] [0,O]
[1258,D] [1258,F] [1258,H] [1258,O]
[C,E] [C,F] [C,H] [C,L] [C,P]
[D,E] [D,F] [D,O] [D,P]
[E,F] [E,P] [F,H]
[H,O] saddle
[L,N] [L,P] saddle
[N,O] [N,P] [O,P]
```

Every edge has exactly two incident maximal faces and `11-27+18=2`. Every active vertex lies on its incident support planes, every nonincident supplied point is strictly behind them, and the minimum Euclidean nonincidence distance is `0.002196560979591234`. No display diagonal is counted as a true edge.

## Exhaustive own-centroid equilibrium audit

Exactly two faces are stable:

```text
[0,H,C] barycentrics
(0.43913917304459016, 0.27336830262109996, 0.28749252433430990)

[N,O,P] barycentrics in stored order [N,P,O]
(0.27787825566062785, 0.51525211239602870, 0.20686963194334337)
```

The minimum positive face coordinate is `0.20686963194334337`; every other face has an exact negative Cramer witness, with closest excluded decision `-0.165831266975022`.

Exactly two vertices are unstable:

```text
0: minimum raw outgoing support
1491201214102505255046493710720063841/2234673359233637034007198509867991040
≈ 0.6673016474380401; normalized minimum ≈0.241527714216487

C: minimum raw outgoing support
829449155551465105998643991990850627277/107264321243214577632345528473663569920
≈ 7.732759093965135; normalized minimum ≈0.9478444660739065.
```

Every other active vertex has an exact negative outgoing witness. The closest excluded one is `N→0`,

```text
-12870572030687781596418672619832049/558668339808409258501799627466997760
≈ -0.023037947765398054.
```

Exactly two true edges are saddles; their normalized four-component tuples `(t,1-t,beta1,beta2)` are

```text
[H,O] (0.24135986022555095,0.7586401397744490,
       0.7216294328126710,0.9728595218265330)

[L,P] (0.2824467929241528,0.7175532070758472,
       0.9679141019285831,0.18499842762740762).
```

Every other true edge has an exact negative full-cone component; the closest excluded edge decision is `-0.03575856869959289`. Complete exact ledgers cover all 18 faces, all 54 directed vertex primitives, and all 108 components of the 27 true-edge cones. Therefore the endpoint is strictly `(2,2,2)`.

## Connected positive-volume transition

The seventh-cage source is augmented only by strict-interior seeds

```text
N=(1,-2,3)/2^24, O=(2,1,-1)/2^24, P=(-2,3,1)/2^24.
```

Remove the common protected face `[0,H,C]` from both boundary spheres. The source remainder and target remainder are dual-connected disks with the same boundary triangle `0-C-H-0`:

```text
source patch (V,E,F)=(12,30,19), chi=1
target patch (V,E,F)=(11,27,17), chi=1.
```

The source patch consists of all source maximal faces except `[0,H,C]`; its packet-bearing faces include `[0,2515,1975]`, `[0,1975,H]`, `[G,L,M]`, `[1975,2515,G]`, `[1975,G,H]`, and `[C,M,L]`. The target patch consists of the seventeen target faces listed above other than `[0,H,C]`.

Coning every patch triangle to that side’s exact own centroid gives a positive-volume 3-ball. The smallest exact source and target cone volumes are

```text
9838798125694068769193037747058038093416273/
379361788725630789265606649693735665191092224
≈ 0.025935132156417236

18159432430971033099758323858903918746904801/
719838674636319801314651807134721609551577088
≈ 0.025227086388690666.
```

Removed source true edges:

```text
[0,1975] [0,2515] [1258,G] [1258,M] [1975,2515]
[1975,G] [1975,H] [2515,G] [2515,L] [C,D] [C,M]
[D,H] [D,M] [G,H] [G,L] [G,M] [L,M].
```

Inserted target true edges:

```text
[0,N] [0,O] [1258,F] [1258,O] [C,P] [D,O] [D,P]
[E,P] [H,O] [L,N] [L,P] [N,O] [N,P] [O,P].
```

Inherited edges whose incident stars change:

```text
[0,H] [0,L] [1258,D] [1258,H] [C,E] [C,L] [D,E] [D,F] [F,H].
```

Thus `[0,1975]` is absent, `1975,G,M` are strictly inactive, `[G,L,M]` and `[1975,H]` are absent, and `[C,L]` is nonsaddle. The predecessor packet is destroyed rather than relabelled.

## Complete changed-edge arrow census and residual theorem

All 27 target edges, all 14 inserted edges, and all 9 inherited star-changed edges were audited over every external directed support. Twenty-one of the 23 changed edges have explicit negative witnesses. The all-external-positive changed edges are `[0,N]` and `[C,P]`; `[C,P]` lies in the protected unstable-`C` star. Hence the unique nonprotected adverse changed edge is `[0,N]`.

For `[0,N]`, every external endpoint arrow is positive. The exact minimum is

```text
101710026682760213776958560407059637011/
35754773747738192544115176157887856640
≈ 2.8446558605113332.
```

The mutual arrows are

```text
sigma(0→N)=1491201214102505255046493710720063841/
           2234673359233637034007198509867991040

sigma(N→0)=-12870572030687781596418672619832049/
            558668339808409258501799627466997760
```

and satisfy exactly

```text
sigma(0→N)+sigma(N→0)=||N-0||²
=90672054930439/140737488355328 > 0.
```

If neither endpoint were unstable, both mutual arrows would have to be nonpositive while all external arrows remain positive, contradicting the identity. Thus one endpoint is unstable in addition to strict unstable `C`; at the endpoint it is `0`.

## Exact birth/death chronology

Along the exact coordinate chord from the seventh-cage source to this target, with the ordinary centroid recomputed in each active cell, nine primitive/circuit polynomials were derived over the integers. Sturm counts give one root in each coarse interval; 100 rational bisections isolate each root; an independent verifier rederives all coefficients and every before/after mechanics ledger.

```text
replacement unstable 0 birth                    [49/1000,1/20]       ≈0.04941770377239711
stable transfer [G,L,M]→[2515,G,M]              [153/1000,77/500]   ≈0.15324701733217116
source unstable 1975 death                      [177/1000,89/500]   ≈0.17790334938198477
carrier diagonal [1975,2515]→[0,N]              [97/200,243/500]   ≈0.48573434313034786
replacement saddle [H,O] birth                  [493/1000,247/500] ≈0.49398141417602437
source saddle [1975,H] death                    [249/500,499/1000] ≈0.4986058925723638
stable transfer [3296,O,P]→[N,O,P]              [351/500,703/1000]≈0.7022188276952538
replacement saddle [L,P] birth                  [189/200,473/500]  ≈0.9454420196526493
source saddle [C,L] death                       [977/1000,489/500] ≈0.9776091008037687
```

Therefore

```text
unstable 0 birth < unstable 1975 death
saddle [H,O] birth < saddle [1975,H] death
saddle [L,P] birth < saddle [C,L] death.
```

Both stable changes are strict transfers with an extra-stable face on each side. The exact side ledgers contain `(2,3,3)` or `(3,2,3)` overlap chambers. The canonical connector has no death-before-birth `(1,1,0)` interval. This chronology certificate is scoped to the decisive packet events, not advertised as an atlas of every mechanically neutral root.

## Positive open chamber

Every one of the 78 uncentred supplied coordinates varies independently by

```text
|delta r_ij|≤2^-25=1/33554432.
```

Directed interval arithmetic recomputes the physical volume, all three first moments, the dependent common centroid, the full incidence, all face/vertex/edge-cone decisions, all inactivity gaps, all 21 negative anti-carrier witnesses, and the `[0,N]` forcing theorem. It preserves `(V,E,F)=(11,27,18)` and `(S,U,H)=(2,2,2)`.

Exact volume interval:

```text
[23817454450364912867137/7083549724304467820544,
 95269892862550017947923/28334198897217871282176].
```

Box-wide lower clearances are approximately

```text
topology/nonincidence  0.0008198925677918007
inactive rows          0.025659593866719524
face decisions         0.08124508923742217
vertex decisions       0.023031154303436902
edge-cone decisions    0.023029321819325408
forcing external       2.84464844517573
anti-carrier witnesses 0.3648280723191656.
```

## Verification, exact scope, and successor

A clean extraction reruns deterministic generation, exact chronology construction, independent Sturm/side-ledger chronology verification, directed own-centroid interval verification, primary Fraction reconstruction, a standard-library-only clean-room reconstruction, and exact-to-OBJ/STL matching. The aggregate and package markers are

```text
ALL_CALM_QUARTZ_90_WALL242_EIGHTH_CAGE_VERIFIERS_PASS
CALM_QUARTZ_90_WALL242_EIGHTH_CAGE_PACKAGE_PASS.
```

OBJ and STL agree with the exact own-centred hull: 11 vertices, 18 outward facets, 27 edge classes, every edge of multiplicity two.

Closed exactly: this `N/O/P` cage and release of `1975/G/M`; its full `2^-25` chamber; predecessor packet deletion; all inserted/star-changed arrow decisions; the connected same-boundary volume; the nine decisive chronology events; and the `[0,N]` forcing chamber.

Not closed: every three-support placement, every release set/common boundary, a closed four-support cage, or global existence.

The endpoint exposes

```text
[0,N]→[L,O]       forcing escape
[N,P]→[L,O]       death sheet of stable [N,O,P]
[H,O]→[0,1258]    saddle exchange
[L,P]→[C,N]       saddle exchange.
```

The first two share the same opposite diagonal `[L,O]`; serial use would repeat transfer. The first genuinely new topology is a closed four-support carrier cage, or an equivalent two-cell hexahedral/double-octahedral volume, placing `[0,N]`, the complete `[N,O,P]` star, and both saddles in one communicating positive-volume complex, with release of `0` or `N` permitted and anti-carrier arrows imposed before moment closure.

## Artifacts and integrity

- [Complete exact archive](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER.zip)
- [Full handoff](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_handoff.md)
- [Structured result](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_result.json)
- [Clean verification receipt](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_clean_verification.json)
- [Exact generator](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/data/generator_exact.json)
- [Own-centred V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/data/active_vertices_centered_exact.csv)
- [Irredundant H-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/data/eighth_cage11_exact_H_irredundant.csv)
- [Complete face ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/data/eighth_cage11_exact_faces.csv)
- [Complete vertex ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/data/eighth_cage11_exact_vertex_primitives.csv)
- [Complete true-edge cone ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/data/eighth_cage11_exact_true_edges_full_cones.csv)
- [Transition certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/certificates/eighth_cage_shared_global_patch.json)
- [Chronology certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/certificates/source_to_target_death_before_birth_obstruction.json)
- [Arrow census](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/certificates/external_arrow_design_certificate.json)
- [Perturbation certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/certificates/own_centroid_perturbation_certificate.json)
- [Independent verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/scripts/verify_independent.py)
- [Watertight OBJ](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/mesh/body.obj)
- [Watertight STL](sandbox:/mnt/data/Calm_Quartz_90_wall242_eighth_cage_exact_NONWINNER/mesh/body.stl)

```text
archive SHA-256  a753e0783f1ae01527b5f3fd5004cca60610ff6c54ed9a74e1dafbadc3adc535
archive bytes    1910668
manifest entries 51
manifest SHA-256 9b4b36d3bf8351e74c5475a8c98cc177cd5a6fdf6ffbef13bcc8652d478c7d62
clean extraction PASS
```

**Final statement:** `NONWINNER`, rigorously delimited. The three-support cage genuinely annihilates the seventh-cage packet and deactivates `1975`, but inserted edge `[0,N]` becomes the unique nonprotected forcing carrier; every replacement unstable/saddle feature is born before its source counterpart dies on the exact connector.
