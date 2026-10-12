# figure-0202

AI research report · 2026-09-02 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Calm Maple 15 — exact post-`AQ32-C0-FP4-D25` determination

## Literal verdict

**No homogeneous convex polyhedral Gömböc was obtained.** The strongest completed endpoint is the exact dyadic full-supplied-hull body `AQ32-SS2-G6`. Its own-centred class is strictly

```text
(S,U,H)=(2,2,2),
```

so it is a rigorous finite **NONWINNER**, not a wall point. It does, however, complete the requested first global topology outside the certified `AQ32-C0-FP4-D25` cell: the old boundary spine is destroyed, the complete `N3` star disappears, and two communicating interior spines with a common terminal are created in one actual all-row hull event. The supplied journal identifies the parent cell and its `U>=2` obstruction.

Complete reproducible archive: AQ32_SS2_G6_EXACT_NONWINNER.zip  
Outer SHA-256: `bb4a9b285d6d5a75cd6581f038d25b0e3c83064e9d24fc49d85caed294a1e2ae`.

## What was actually done

I recovered the complete exact post-journal construction and independently reran its endpoint verifier in the present runtime. The fresh rerun returned

```text
INDEPENDENT_AQ32_SS2_G6_EXACT_NONWINNER_VERIFICATION_PASS
```

and independently regenerated every supplied row, rebuilt the actual hull, checked every inactive-row/maximal-face pair, re-isolated the Santaló root, reconstructed both Q and P, audited every maximal face, full vertex tangent cone and four-component true-edge cone, checked the perturbation theorem, and parsed both OBJ/STL pairs. The archive also contains a manifest-bound independent homotopy transcript returning

```text
INDEPENDENT_AQ32_SS2_G6_COMPLETE_HOMOTOPY_ATLAS_VERIFICATION_PASS
```

after `21,093,600` exact support-polynomial checks. A fresh replay of that expensive path audit exceeded this runtime's one-hour command cap; the endpoint proof was freshly rerun, while the full path is supported by the checked archive transcript and hashes. The exact recovered handoff states the same nonwinner verdict and the global topology escape.

Critical internal SHA-256 values:

```text
parent full-row NPZ  9e0442a1fc4cfa672864d9fdf9a0aeb6f1511c7ba7a35a82a7d0cab16634b29c
final full-row NPZ   6751f94c20b4953f40e32f6c306f0589ed8383236f8b04c3710e812642d71dd0
exact certificate    86ccdd18a9c4963061c67ba40b7d1d50a170107cff6498fc430ae1523e2499f0
endpoint verifier    464915de6d113292ee9f65b6ae715eb0fdf4afa9bb7f8bfacdb4019e54b33a7c
homotopy verifier    9ebedf0ada2171fd866553c4c67d526eecde6f2b8f97db81956b7880466dc070
```

## Exact finite generator

Let

```text
D=2^150=1427247692705959881058285969449495136382746624.
```

Start from all `25,847` exact parent rows in `AQ32_C0_FP4_candidate_rows_exact.npz` and append the following six rows:

```text
G0=(-1217087780834418995847222072407495520454224904192,
    -368746429143485098879212826603067602836698169344,
     1428715665560143588728780111390810645906411487232)/D
G1=(-682206866428539572241003008362291764696360943616,
    -952539967975827076829003646711266296687486828544,
     1205402500835751581633365253604776585073820434432)/D
G2=( 389061354050003184941047449588650031492188078080,
     -79594342300575535185877520536634086257053401088,
    -281288959062878984115871869298856020678014926848)/D
G3=(-216394152464272988256820985345846962393062572032,
     136764718339351374857641612814258434389510717440,
     -83844649247559604561318351566022453557614084096)/D
G4=( 646935308779300111750490143951099883854833385472,
    -173145653383867137574067198312840550896396926976,
    -121355801067410279774106789497118777866195042304)/D
G5=(1213972181570264847174218891208504653982709317632,
     524920916380396334347928680458761992557345898496,
    -825327005143827666980286795927275696149820866560)/D.
```

The complete ledger is

```text
parent supplied rows  25,847
inserted rows               6
total supplied rows    25,853
active/extreme rows          8
strictly inactive rows  25,845.
```

The eight active rows are exactly

```text
X0=(-411963218173226173362348912428614381408845037568,
      98309925876059965672577950816891194891315445760,
     442699183507332620569840873423869801449291513856)/D
X1=(-416335631948478095705394243928134638636701319168,
      99646308596827900299357358577912123797662597120,
     438110495568783025068932977734888971632635805696)/D
G0,G1,G2,G3,G4,G5 as above.
```

Their source indices are `25843,25844,25847,25848,25849,25850,25851,25852`. The archive contains both the expanded `25,853`-row CSV/NPZ and a clean generator that reconstructs them from the parent exact source and the six-row specification.

## Exact all-row topology change

All six new rows move simultaneously by

```text
G_i(t)=C0+t(G_i-C0),  0<=t<=1.
```

The full supplied-hull atlas contains exactly `37` isolated simple circuit events and `38` open cells:

```text
6  one-to-three vertex activations
21 two-to-two diagonal flips
10 three-to-one vertex deactivations.
```

Every cell is rebuilt using all `25,853` rows at an exact rational sample. At the endpoint only parent rows `X0,X1` survive: `X2,X3,C1,N1,N2,N3` and the surviving coarse anchors are strictly inactive. Thus the old boundary edge `X1-X3` is absent and the entire old `N3` star is gone, not relabelled.

## Irredundant Q/P lattice

The actual f-vectors are

```text
Q: (V,E,F)=(8,18,12)
P=(Q-s(Q))^circ: (V,E,F)=(12,18,8)
Euler(Q)=Euler(P)=2
mechanical complexity=36.
```

The exact Q volume is

```text
288993278621763972562485534358934231034158371302528177 /
2854495385411919762116571938898990272765493248.
```

Using local vertex order `(X0,X1,G0,G1,G2,G3,G4,G5)`, the complete Q maximal-face cycles are

```text
0 (0,2,7)   1 (5,3,2)   2 (6,7,2)   3 (3,6,2)
4 (1,2,0)   5 (1,5,2)   6 (7,1,0)   7 (1,7,5)
8 (5,4,3)   9 (4,6,3)  10 (4,5,7)  11 (4,7,6).
```

Every Q true edge is

```text
(0,1),(0,2),(0,7),(1,2),(1,5),(1,7),
(2,3),(2,5),(2,6),(2,7),(3,4),(3,5),(3,6),
(4,5),(4,6),(4,7),(5,7),(6,7).
```

The complete P maximal-face cycles are

```text
0 (0,4,6)
1 (4,5,7,6)
2 (0,4,5,1,3,2)
3 (1,8,9,3)
4 (8,10,11,9)
5 (1,8,10,7,5)
6 (2,11,9,3)
7 (0,2,11,10,7,6).
```

Every P true edge is

```text
(4,6),(0,4),(0,6),(4,5),(5,7),(6,7),
(1,3),(1,5),(2,3),(0,2),(8,9),(1,8),(3,9),
(8,10),(9,11),(10,11),(7,10),(2,11).
```

There are no coplanar triangulation diagonals. Exact P vertices are deterministically obtained by intersecting the three centered planes `(q_i-s)·x=1` belonging to each Q face; the expanded algebraic/root-box H/V tables are in the archive.

## Santaló root and ordinary-volume centroid

The unique Santaló point lies in the coordinatewise radius-`10^-90` box around

```text
s_x=-69.022749028373512883725680985107673761659483950988680152743384435340823427027349229101827051399746113257065608878776135620738256687492252793547567348666197224883649415267
s_y=-95.943975719334845677865499802680162406453306486383014816878516588759992968968499148409250391175440355365063788554941470036983587202914508106064476411923601495680259859925
s_z=215.75046798326165248243139201709157377334856641867965175643303978911194442174245605781038037909121114384014584846032786205364141409516097505640348307501537227611487286579.
```

At the isolated root,

```text
polar volume              9.7293598144125643280385798306091971755209058294267766208234794412305348573208425e-8
normalized moment residual 9.7214717749915683797171823505515342453623903544294546402502492662301440382077487e-194
projective denominators    [78.6250210639459603951,279.3446052297985868132]
lambda_min(DF)             >=9.8502478380813015972e-12
root-ball radius           <=3.84086566670479248e-189.
```

A second exact rational midpoint evaluation stores the volume and all three first moments as literal fractions; its directed normalized residual is `1.5092717611357316e-172`, and strong monotonicity bounds the exact zero within `5.962996368498263e-168 < 10^-90`. Strict convexity of polar volume gives global uniqueness. Therefore `P=(Q-s(Q))^circ` has ordinary-volume centroid exactly at the origin. The Santaló displacement from the FP4 midpoint is `162.4709808170391444069...`, exceeding the inherited `92.5018` local-centre exclusion.

## Complete equilibrium audit

Every one of the `12` actual Q faces, all `8` full vertex tangent cones, and all four components of all `18` true-edge normal cones is certified throughout the root box.

Positive equilibria and margins are

```text
stable face (G4,G5,G0)  98.4819905771363
stable face (G3,G2,G1) 136.50159422291338
unstable G0             607.4704718504175
unstable G5            1229.4144753273831
saddle G0-G3             74.7236432980241
saddle G1-G4            294.43899976260104.
```

The global exclusion minima are

```text
nonstable faces      1.3087733801763526
nonunstable vertices 31.06935703023223
nonsaddle edges      2.7421557749625203.
```

Hence Q is strictly `(2,2,2)`, and polarity gives the same own-centred count for P.

## Inactive, nonincidence and perturbation margins

All `25,845×12=310,140` inactive-row/maximal-face pairs have positive exact integer slack. The closest inactive row is old `C0` (source `25841`) against face `(X1,G0,X0)`, at unit-normal distance

```text
0.992623854061474228677535087284294591304920521229992224959460288274348462853413758052039796.
```

The closest active/nonincident distance is

```text
1.79070482063365377470400555997293119955772898868888277333407903843350230409755650923106694.
```

Further exact/directed minima are

```text
adjacent orientation magnitude 514352.54101851939200699
true-edge length                   4.538562038609557
face cross-normal norm          4237.088328813356
full edge-cone determinant         0.4703293087532414.
```

All `25,853×3` row coordinates may vary independently within

```text
|delta q_ij|<=2^-4096=9.5749774609521853579467310122804202420597417413514981491308464987731504822633223383301355e-1234.
```

A deliberately oversized derivative envelope still keeps every incidence, root and mechanical change below `9.57497746e-234`, versus the `10^-90` root box and the `1.30877` smallest decisive mechanical score.

## Communicating three-dimensional complex

The endpoint has an exact positive-volume tetrahedralization by the following eleven local cells:

```text
(0,6,2,3),(0,6,7,2),(0,6,5,7),(4,6,7,5),
(4,0,5,3),(4,0,3,6),(4,0,6,5),
(1,5,3,2),(1,0,2,3),(1,0,3,5),(1,0,5,7).
```

The tetrahedral boundary equals the exact Q boundary and the tetrahedral volume sum equals the exact hull volume. Interior tetrahedral edges are

```text
X0-G1, X0-G2, X0-G3, X0-G4, X1-G1, G3-G4.
```

In particular `X0-G1` and `X1-G1` are two communicating interior spines sharing terminal `G1`. The old cross-gap boundary spine is absent. The six inserted rows supply `18` scalar coordinates; after treating three coordinates as dependent Santaló controls, `15` genuine shape/topology variables remain.

## Rigorous first obstruction outside the old cell

The inherited FP4 component theorem is gone. The first exact obstruction in the new actual cell is instead a two-source theorem:

```text
for G0, every incident true-edge instability primitive is positive;
for G5, every incident true-edge instability primitive is positive.
```

Their certified minima are `607.4704718504175` and `1229.4144753273831`. Thus `G0` and `G5` are distinct strict unstable vertices throughout the complete incidence/sign/Santaló-root/perturbation cell, proving

```text
U>=2.
```

The residual Euler-neutral packet is exactly

```text
stable:   (G4,G5,G0), (G3,G2,G1)
unstable: G0, G5
saddles:  G0-G3, G1-G4.
```

This excludes every fixed-cell coordinate or metric polishing of `AQ32-SS2-G6`. Its scope ends only when an incident star/sign of `G0` or `G5` changes, one source becomes nonextreme, the metric cell changes, or the Santaló root leaves the certified box.

## Most useful continuation

The next genuinely new topology is one connected **two-source/two-saddle shared terminal** spanning both complete source stars and both saddle stars. `G0` and `G5` must change in the same hull event; sequential treatment is predicted to repeat the observed transfer. The smallest evidence-supported architecture is a two-ended double-prismatic or octahedral cell with a transverse return tetrahedron, at least two communicating interior spines, three dependent Santaló controls, and independent antibirth variables. It should permit `G0` or `G5` to deactivate and simultaneously cross both saddle channels while rebuilding the complete external boundary.

A complete fixed-geometry mechanical-centre MILP and finite full-row append/metric searches found no `(1,1,0)`, `(2,1,1)` or `(1,2,1)` endpoint; these are discovery evidence, not continuum exclusions. The exact obstruction above—not those numerical searches—is the rigorous stopping boundary.

## Reproduction and mesh

From the unpacked archive run

```bash
./[internal-source-reference].sh
```

or regenerate in a new directory with

```bash
python generate_AQ32_SS2_G6_exact.py --output-dir regenerated
```

The watertight meshes have

```text
Q OBJ/STL: 8 vertices, 12 triangles, 18 edges; signed volume 101241459.38321796
P OBJ/STL: 12 vertices, 20 triangles, 30 edges; signed volume 9.729359814412563e-08.
```

Every mesh edge has incidence exactly two, and the Q mesh volume agrees with the exact rational volume.

## Final research judgment

`AQ32-SS2-G6` is the strongest exact reconstructed endpoint for this assignment. It advances beyond `AQ32-C0-FP4-D25` in exactly the demanded sense: all parent rows are retained in the supplied hull; the complete external boundary is rebuilt; the old `N3` star and boundary spine are destroyed; two communicating interior spines are materialized; the own centroid is isolated exactly through Santaló polarity; all actual features and inactive rows have positive margins; and independent verification plus watertight meshes are supplied. It fails only at the final count because the Morse packet transfers to strict sources `G0,G5`. The next work should therefore begin from this full-row endpoint, not from the old FP4 reduced active set.
