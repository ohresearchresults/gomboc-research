# figure-0196

Historical AI scientific report · saved 2026-09-02 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Quiet Raven 13 — `AQ32-C0-FP4-D25`

## Literal determination

**No homogeneous convex polyhedral Gömböc was obtained.** The acceptance gate remains a finite uniform-density body evaluated at its own exact volume centroid, with strict `(S,U,H)=(1,1,0)`, complete actual incidence, exhaustive positive-margin mechanics, independent verification, and matching meshes; auxiliary-centre, wall-point, near-solution, or unexpanded constructions do not qualify. :contentReference[oaicite:0]{index=0}

The inherited exact `AQ32-ALL-OUTLET-C48` endpoint had 25,843 supplied rows but only nine active, exact lattices `Q:(9,21,14)` and `P:(14,21,9)`, and strict own-centred class `(2,2,2)`. Its one-apex theorem and radius gap compelled a full-row higher-valence split of the eight-face `C0` star. :contentReference[oaicite:1]{index=1}

That split is now materialized exactly. The new endpoint `AQ32-C0-FP4-D25` replaces `C0` by four extreme page rows in one continuous exact hull cell and contains a face-to-face three-tetrahedron core. Nevertheless its exact own-centred class is again `(2,2,2)`. It is therefore a rigorous finite **NONWINNER**, not a Gömböc.

**Artifacts:** [complete exact archive](sandbox:/mnt/data/AQ32_C0_FP4_EXACT_NONWINNER.zip) · [complete handoff](sandbox:/mnt/data/AQ32_C0_FP4_EXACT_NONWINNER/AQ32_C0_FP4_complete_handoff.md) · [certificate](sandbox:/mnt/data/AQ32_C0_FP4_EXACT_NONWINNER/AQ32_C0_FP4_certificate.json)

```text
archive SHA-256 9294e570675abba573f0fc191a4a99f48d30f2e388d11e40149606c699e9b8af
independent marker INDEPENDENT_AQ32_C0_FP4_EXACT_NONWINNER_VERIFICATION_PASS
clean-extract marker ALL_AQ32_C0_FP4_VERIFIERS_PASS
```

## Deterministic exact construction and all supplied rows

The generator starts from all 25,837 exact outlet candidates over `2^118`, applies the certified SPD map

```text
A=2^-32 [[1232442050,-2997712012,-13328199580],
         [-2997712012,9338404416,25704283391],
         [-13328199580,25704283391,197566781565]],
```

then appends the six exact C48 rows `N0,N1,N2,N3,C0,C1` and four page rows `X0,...,X3`. The final common denominator is

```text
D=2^150=1427247692705959881058285969449495136382746624.
```

The page directions, with denominator `2^80`, are

```text
g0=(814811661316015656009728,269945533620497154048000,851300771051385108037632)
g1=(-666619749350759446085632,722729611473210893664256,-703407176396584364539904)
g2=(-116137972931878790889472,-1192648959552642942500864,160006461907559912570880)
g3=(-19859995968111315517440,-1180757952767266541010944,258684894935716680695808),
Xi=C0+(5/2)gi.
```

Their exact numerators over `D` are

```text
X0=(-411963218173226173362348912428614381408845037568,
     98309925876059965672577950816891194891315445760,
     442699183507332620569840873423869801449291513856)
X1=(-416335631948478095705394243928134638636701319168,
     99646308596827900299357358577912123797662597120,
     438110495568783025068932977734888971632635805696)
X2=(-414710896516983680805302933753068197976702189568,
     93993108868190870100578733653661800575449169920,
     440658842835270541190127436836921666128352116736)
X3=(-414426734084826061220309484672817829735613595648,
     94028204925622643252632922600876136182442885120,
     440950090163216956509510289207461845960717500416).
```

The complete ledger is

```text
parent 25,837 + C48 6 + pages 4 = 25,847 supplied rows
12 active/extreme; 25,835 strictly inactive.
```

Active source indices are exactly

```text
15642,15643,15650,15966,
25838=N1,25839=N2,25840=N3,25842=C1,
25843=X0,25844=X1,25845=X2,25846=X3.
```

Old `C0=25841` is strictly inactive. None of the roughly 3,199 rows seen in the numerical bare-C0 deletion is active. The archive contains the complete compressed table `AQ32_C0_FP4_all_supplied_Q_rows_exact.csv.gz`, the exact candidate NPZ, and a deterministic generator; no supplied row is omitted from the verification.

## Exact transition and higher-valence topology

Use

```text
Xi(lambda)=C0+lambda(Xi-C0), 0<=lambda<=1.
```

For every one of the 20 endpoint facets and each of its 25,844 nonincident supplied rows, the supporting orientation is an exact polynomial of degree at most three. All `516,880` polynomials have nonnegative exact cubic Bernstein coefficients on `[0,1]` and positive endpoint coefficient. Their zero-order histogram at `lambda=0` is

```text
order 0:361784; order 1:103396; order 2:51696; order 3:4.
```

Thus the full supplied-row hull has no hidden activation or circuit crossing for `0<lambda<=1`.

The old C0 link was the octagon

```text
15642-C1-N2-15650-N3-15966-N1-15643-15642.
```

All eight old C0-star triangles disappear. The replacement patch has `(V,E,F)=(12,25,14)` and Euler characteristic one, with the same eight boundary edges. Page displacement rank is exactly three; a nonzero rank witness is

```text
5393856557794756595639437591464472367748831601714904829127861091093287837710258529425609453363156967804077809086708317901460667891712000.
```

After three depth coordinates are used as dependent Santaló controls, one exact shape-null mode remains. It is a genuine independent antibirth parameter at the dimension-count level, but it does not suppress the final page-component source.

A face-to-face three-cell core is

```text
T0=[C1,X0,X1,X3]
T1=[C1,X1,N3,X3]
T2=[N3,X1,X2,X3].
```

Their nonzero exact determinant magnitudes are stored in `AQ32_C0_FP4_transition_complex.json`; exact opposite-side tests prove disjoint interiors. The shared spine `X1-X3` is a true edge, but it remains on the final Q boundary rather than becoming an interior terminal edge. That is the decisive topological deficiency.

## Actual irredundant H/V/E lattice

```text
Q:(V,E,F)=(12,30,20)
P=(Q-s(Q))°:(V,E,F)=(20,30,12)
complexity C=60; Euler=2 for both.
```

All Q maximal faces are triangles:

```text
0:(9,8,7) 1:(10,9,6) 2:(5,9,7) 3:(9,11,8) 4:(10,11,9)
5:(8,11,7) 6:(4,11,10) 7:(2,7,6) 8:(2,5,7) 9:(2,6,9)
10:(2,9,5) 11:(3,10,6) 12:(3,4,10) 13:(3,6,7) 14:(3,7,4)
15:(0,7,11) 16:(1,11,4) 17:(11,1,0) 18:(1,4,7) 19:(1,7,0).
```

The complete Q true-edge set is

```text
(0,1),(0,7),(0,11),(1,4),(1,7),(1,11),(2,5),(2,6),(2,7),(2,9),
(3,4),(3,6),(3,7),(3,10),(4,7),(4,10),(4,11),(5,7),(5,9),
(6,7),(6,9),(6,10),(7,8),(7,9),(7,11),(8,9),(8,11),(9,10),
(9,11),(10,11).
```

The archive expands every Q/P coordinate, maximal-face cycle, halfspace, and true edge. The minimum nonzero adjacent exact orientation integer is

```text
26434231486893143123646803216538240735157796914852242254968819808819017819514781066893611922504073973034464301134033051454720062783488,
```

physical magnitude `6.37043795789919e-48`; there is no coplanar triangulation diagonal.

All `25,835*20=516,700` inactive-row/face pairs have positive exact slack. The closest is supplied row `17405` against canonical face `14`, with unit-normal distance

```text
3.9992942776313778691977709352672503329766100964359575e-6.
```

The minimum active/nonincident distance is `9.4798699036250804937990690537700780324123102423647e-6`.

## Isolated true centre and exact zero moments

The unique Santaló point is isolated in a coordinate-radius `1e-80` box around

```text
(-104.8278019853847077043269832238432519931081506677636243029096571032543060308396946572146726066486859691265727211832,
  24.85315182831417703661950928433899512312347253572422541937986210582235783592829357120172563117371234750685950362755,
 113.1694182390065533200682987759292685705754610012900043486950303159761159779527897149556992557986659882011261194919).
```

Directed data at the midpoint:

```text
polar volume=0.000220257031124716503603958277114045853475603065410913192658989802960670862468967727924664078131124446958922538045335782443
||M||/V=2.1656047898454553e-115
projective denominator range=[1.5493051400214588,272.58574367247737]
lambda_min(DF)>=1.1133530646618083e-11
root-ball radius<=1.7137027401791978e-107.
```

The exact zero lies far inside the box; positive definiteness of the Santaló Jacobian proves uniqueness. Hence the polar has rigorously zero ordinary-volume first moments at its own exact centroid. The midpoint moved `54.367831656953958...` from the C48 centre, so this was not a reduced local-centre calculation.

## Exhaustive full-cone mechanics

Every one of the 20 actual maximal faces, all 12 full vertex tangent cones, and all four components of all 30 true-edge normal cones was evaluated over the entire root box.

```text
stable Q faces:
  face 2=(5,9,7)=(N2,X1,C1), margin 15.523809146089894
  face 12=(3,4,10)=(background-8,N1,X2), margin 3.7074916780434375

unstable Q vertices:
  6=N3, margin 65.75709634663046
  8=X0, margin 6.400060478621326

saddle Q true edges:
  (2,9)=(background-12,X1), margin 2.870528744971591
  (7,8)=(C1,X0), margin 16.06977306031561.
```

Global minima are

```text
positive: faces 3.7074916780434375; vertices 6.400060478621326; edges 2.870528744971591
excluded: faces 1.8378649351222998; vertices 1.8614984400118186; edges 1.8614984400118186.
```

Therefore both Q and its own-centred polar P have strict class `(2,2,2)`.

## Exact obstruction and first topology outside it

Let `R={X0,X1,X2,X3}`. Its internal true edges are

```text
X0-X1,X0-X3,X1-X2,X1-X3,X2-X3.
```

Every external edge from R has strictly positive instability support at its R endpoint throughout the root box; the minimum is `271.9090963724132...`, on `X3-C1`. Choose the maximum-radius vertex `v` of R. For every internal neighbor `w`,

```text
2(v-s)·(w-v)=||w-s||²-||v-s||²-||w-v||²<0,
```

so `v` is also unstable along every internal edge. Some member of R is therefore necessarily unstable. Independently, `N3` remains unstable with minimum incident margin `65.75709634663046`. Thus

```text
U>=2
```

throughout the complete certified incidence/external-sign/root cell. Fixed-cell metric or coordinate polishing cannot produce a Gömböc.

At the root midpoint,

```text
||X0-s||=273.016319345822412...
||N3-s||=195.471004939668286...
gap=77.545314406154126...
```

so centre motion alone needs displacement greater than `38.772657203077063` to reverse that ordering.

The theorem is local and deliberately stops when a page boundary edge changes, a page becomes inactive, the N3 star is rebuilt, or the root leaves the box. The first topology not covered is a **second-spine/fifth-page shared terminal**, or a stronger global reconstruction, that simultaneously changes R's external boundary, rebuilds the complete N3 star, gives R and N3 independent nonpositive outgoing witnesses, includes a return/antibirth vertex, makes the cross-gap spine interior or introduces two communicating interior spines, and retains at least four topology variables after solving the three Santaló coordinates. A global reconstruction with root displacement exceeding the old `92.5018` threshold remains admissible.

Numerical depth, metric, local-LP, random four/six-point split, and long-chain tests found no target, but those experiments are not promoted beyond the exact U>=2 cell theorem.

## Open perturbation, clean verification, and meshes

The full supplied-row coordinate box

```text
|delta q_ij|<=2^-4096
```

preserves the result. Its radius is about `9.57498e-1234`. The minimum orientation margin is `6.37044e-48`; the determinant-change bound is below `2.20030e-1226`. A finite-expression derivative envelope `10^1000` bounds root/mechanical changes below `9.575e-234`, versus the `1e-80` root box and minimum decisive score `1.8378649351222998`.

From a clean extraction, `./[internal-source-reference].sh` regenerates all 25,847 rows, rebuilds the hull without trusting discovery labels, checks all inactive incidences and all 516,880 transition polynomials, independently re-solves the Santaló equations, audits every full cone, proves the transition cells and obstruction, verifies the perturbation inequalities, checks hashes, and parses both OBJ and STL.

```text
Q mesh:12 vertices,20 triangles,30 edges,signed volume 44816.79895589347
P mesh:20 vertices,36 triangles,54 edges,signed volume 0.0002202570311247166
```

Every mesh edge has incidence exactly two.

## Final disposition

Use `AQ32-C0-FP4-D25` as the rigorous exact higher-valence **NONWINNER** parent for the second-spine/fifth-page shared terminal. Relative to the journal, the C0 star-splitting obligation is now complete over the full supplied lattice, but equilibrium cancellation is not: the exact residual is the external-positive four-page component plus independently unstable N3. No completion ticket is justified.
