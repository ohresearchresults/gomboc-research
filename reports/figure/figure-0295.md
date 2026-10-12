# figure-0295

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Calm Finch 13 — global AX-star search and ten-vertex two-cell continuation

## Disposition

**DELIMITED NONWINNER; the acceptance gate remains unmet.**

I did not obtain an exact own-centred strict `(S,U,H)=(1,1,0)` polyhedron, and I did not prove that the complete real realization space of the nine-vertex graph is empty. The strongest new determination is instead a sharp separation of three issues:

1. The exact AX9 incidence graph is **not combinatorially incapable** of mono-monostatic mechanics. Robust realizations of the same graph have strict `(1,1,0)` relative to freely chosen interior mechanical centres.
2. For the immutable parent geometry itself, the complete two-target centre-chamber problem was reduced to and exhaustively traversed through `80,960` complementary primal/dual tree branches. Its optimum is the known AX wall; no strict `(1,1,0)` centre exists for that fixed shape.
3. A connected ten-vertex two-cell split of the AX pentagonal cap also possesses a robust free-centre `(1,1,0)` chamber, but every tested hard-centering route remains separated from it. Four complete positive tree branches were identified; their own-centroid homotopies stop at normalized centroid gaps above `0.697`.

Thus the obstruction exposed here is not topology alone. It is compatibility between the ordinary-volume centroid and the mono-monostatic centre chamber. The nine-vertex global realization space and the complete ten-vertex two-cell realization space remain open.

No numerical state below is promoted as a homogeneous polyhedral Gömböc or as an exact successor endpoint.

## Literal immutable parent

Authoritative source:

```text
assignment  figure-0285
SHA-256    cc28de1441e9e1524b0e3ce048648120d01666ef8cd632a74a5a4d0bf8df41cc
name       AX9
```

It has 59 supplied rows, nine active vertices, actual `(V,E,F,C)=(9,21,14,42)`, exact ordinary-volume centring, and strict `(S,U,H)=(2,2,2)`.

Let `D=2^27=134217728`. Supplied order is

```text
0,1258,1371,1975,2152,2369,2515,2732,3290,3296,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AG,AH,AI,AJ,AK,AL,AM,AN,AO,AP,AQ,AR,AS,AT,AU,AV,AW,AX
```

For parent position `i=0,...,57`, the default row is

```text
(8(i+1),-16(i+1),24(i+1))/D,
```

except `B=(0,0,0)`. Apply the active overrides

```text
0 =(  19057904, -50471568,  369374232)/D
C =(-157248112,-100564064, -673203608)/D
H =( -13428904,  95484952, -203825632)/D
AS=(  13481528, 106209064, -370999584)/D
AT=( 215035232, 155090168,  624881392)/D
AU=(  62805192,  67862424, -143066648)/D
AV=(  46873424, 109782944, -360206208)/D
AW=( 100671104,  -9875047,  608489383)/D
AX=( 707139249, 189989663, 4124289023)/D.
```

Active set:

```text
{0,C,H,AS,AT,AU,AV,AW,AX}
```

Strictly inactive supplied rows:

```text
{1258,1371,1975,2152,2369,2515,2732,3290,3296,A,B,D,E,F,G,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AG,AH,AI,AJ,AK,AL,AM,AN,AO,AP,AQ,AR}
```

Exact uncentred volume and centroid are

```text
Vol = 13927739138863031418107597/1813388729421943762059264

c = (8880453107810947224991087343079669/7477398013579490320524078915518464,
     508408188203593583718080615647367/934674751697436290065509864439808,
     21672968208057635806944934654565499/3738699006789745160262039457759232).
```

After translation by `-c`, the three first moments vanish exactly.

Maximal faces:

```text
[0,H,C] [0,C,AW] [0,AX,H] [0,AW,AX] [C,H,AS] [C,AS,AV] [C,AV,AU]
[C,AU,AW] [H,AT,AS] [H,AX,AT] [AS,AT,AV] [AT,AU,AV] [AT,AX,AU] [AU,AX,AW]
```

True edges:

```text
[0,C] [0,H] [0,AW] [0,AX] [C,H] [C,AS] [C,AU] [C,AV] [C,AW]
[H,AS] [H,AT] [H,AX] [AS,AT] [AS,AV] [AT,AU] [AT,AV] [AT,AX]
[AU,AV] [AU,AW] [AU,AX] [AW,AX]
```

Exact equilibrium class:

```text
stable   [0,AX,H], [AU,AX,AW]
unstable C, AX
saddles  [0,AX], [AT,AX]
```

The only all-external-positive true edge is protected `[C,AS]`. Every other edge has a strict negative external witness. The parent coordinate chamber of radius `2^-27` preserves all incidence, equilibrium, and antibirth signs, so the desired chamber is necessarily outside that local box.

Parent artifact identity:

```text
exact generator SHA-256  8fbd37ade9de63001afd4af3881b880265baac1f01a67e4992197de552166f0d
archive SHA-256          099616b9ef7ef06ffba713e434d5fbcb2c5e28c07810b6f17bcb215332a6cb67
manifest SHA-256         bb2ea6e2c2c73721b3d608840cc2c74b6fb5170978b4edbf214645508fc8b0ce
```

## Complete fixed-parent centre treatment

For a fixed simplicial three-polytope and an interior reference centre, strict `(1,1,0)` mechanics can be encoded by complementary rooted spanning trees:

- a primal spanning tree directed from every non-target vertex toward the unique unstable vertex `C`, selecting one strict negative directed-support witness at each non-`C` vertex;
- the complementary dual spanning tree directed from every non-target face toward the unique stable face, selecting one strict negative projection barycentric coordinate at each non-target face.

When all selected inequalities are strict, the target face and `C` are the only stable and unstable features. Euler's identity then forces zero saddle edges. Conversely, every strict `(1,1,0)` centre chamber contains at least one such complementary tree certificate.

Both current stable-face choices were treated:

```text
target 0 : [0,AX,H]
target 1 : [AU,AX,AW]
```

For each target there are exactly `40,480` complementary primal/dual tree branches, hence `80,960` complete branches across the two intended targets. In the fixed immutable AX9 geometry, each branch is a linear strict-centre feasibility/max-margin problem because face-foot barycentric coordinates and directed vertex supports are affine in the reference centre.

The deterministic complete traversal found no positive branch. The maximum closes at margin zero at the AX transfer wall; approximately forty labeled branches attain that closure, while all remaining branches have negative optimum. This is a complete determination for the **fixed parent shape and arbitrary centre**, not for moving vertices.

The coefficient matrices are rational because the immutable AX9 coordinates are rational. The present bundle does not contain independently generated rational dual certificates for all `80,960` linear programs, so this result must not be promoted as a global exact realization-space obstruction.

Reproducible files:

- Target `[0,AX,H]` complementary-tree atlas (`ax9_trees_t0.npz`)
- Target `[AU,AX,AW]` complementary-tree atlas (`ax9_trees_t1.npz`)
- Fixed-shape centre LP driver (`ax9_center_tree_lp.py`)
- Target-0 centre batches (`ax9_center_lp_t0_0_20000.npz`)
- Target-0 remaining batches (`ax9_center_lp_t0_20000_37000.npz`)
- Target-1 centre batches (`ax9_center_lp_t1_0_18000.npz`)
- Target-1 remaining batches (`ax9_center_lp_t1_18000_35000.npz`)

## The AX9 graph itself admits robust mono-monostatic centre chambers

Allowing all nine active vertices to move, modulo the gauge

```text
0=(0,0,0), H=(1,0,0), C=(Cx,Cy,0), Cy>0,
```

produced robust realizations of the unchanged 14-face graph that are strict `(1,1,0)` relative to a freely optimized interior centre. This breaks any attempted purely combinatorial impossibility claim for the AX9 graph.

A representative realization, with coordinate vector ordered as

```text
Cx,Cy, ASxyz, ATxyz, AUxyz, AVxyz, AWxyz, AXxyz,
```

is

```text
(-0.8930416631891912,
  3.1408256798099927,
  1.1461696870331652, 1.3181603330988416,-0.1861864040537829,
  0.6863610681990474,-0.12005563198756324,-0.6840456701280856,
 -0.6043063637139455,-0.033217438000702586,-1.2549413472390272,
  0.26491883111198883,0.6425170792825898,-0.9659359801630599,
 -1.5716108526274564,0.4349686280001319,-0.7385050867498256,
 -0.6397780874140038,-0.4644639098001895,-0.8487226445536257).
```

Its strict mechanical centre is

```text
m=(-0.04613008450698353,-0.07805438966664367,-0.4921366611575719).
```

At `m`, the intended stable face is `[0,AX,H]`, `C` is the sole unstable vertex, and there are no saddle edges. The normalized branch margin is approximately `0.0620025`, the centre-interiority margin is approximately `0.1860`, and the fixed-incidence margin is approximately `0.2208`. The ordinary-centroid discrepancy, normalized by root-mean-square radius, is approximately `0.99494`; at its own centroid the same shape has class `(3,6,7)`.

Eight complementary tree branches are positive for this free-centre realization:

```text
12750,12776,13075,13140,24774,24800,25099,25164.
```

For the independently found `[AU,AX,AW]` free-centre realization, positive tree branches are

```text
10353,12770.
```

Tree-constrained continuations that gradually imposed ordinary-centroid closure were run for all ten positive branches. With retained strict branch margins, their best normalized centroid discrepancies stayed approximately between `0.625` and `0.786`. No branch reached closure. These are complete determinations of the ten identified robust basins, not of every AX9 realization chamber.

Projective centring was also tested. For the representative source above, the moderate root of

```text
centroid(P_i/(1+a·P_i)) = m/(1+a·m)
```

is

```text
a=(0.007756764942902696,2.2894269810557173,-0.8984563341224836),
```

with strict positive denominators and numerical residual below `10^-15`. The projectively hard-centred shape has class `(2,4,4)`, not `(1,1,0)`. Determinant-one metric continuation and unrestricted direct-coordinate continuation likewise approached transfer walls without entering a positive chamber.

Relevant files:

- Robust target-`[0,AX,H]` free-centre realization (`ax9_fcu_tf2_5001.npz`)
- Second target-`[0,AX,H]` realization (`ax9_fcu_tf2_5201.npz`)
- Target-`[AU,AX,AW]` realization (`ax9_fcu_tf13_5301.npz`)
- Positive target-0 tree IDs (`ax9_fcu_tf2_5001_trees.npz`)
- Positive target-1 tree IDs (`ax9_fcu_tf13_5301_trees.npz`)
- Tree-constrained homotopy driver (`ax9_homotopy_tree.py`)
- Projective-centroid root solver (`projective_centroid_root.py`)

## Smallest ten-vertex connected two-cell topology tested

A tenth vertex `AY` was introduced by splitting the AX pentagonal cap into a connected two-apex, two-cell cap. The strongest tested split, `split2`, has ten active vertices

```text
0,C,H,AS,AT,AU,AV,AW,AX,AY
```

and 16 triangular maximal faces:

```text
0  [0,H,C]
1  [0,C,AW]
2  [C,H,AS]
3  [C,AS,AV]
4  [C,AV,AU]
5  [C,AU,AW]
6  [H,AT,AS]
7  [AS,AT,AV]
8  [AT,AU,AV]
9  [AT,AX,AU]
10 [AU,AX,AW]
11 [0,AW,AY]
12 [0,AY,H]
13 [H,AY,AT]
14 [AT,AY,AX]
15 [AW,AX,AY].
```

Its 24 true edges are

```text
[0,C] [0,H] [0,AW] [0,AY] [C,H] [C,AS] [C,AU] [C,AV] [C,AW]
[H,AS] [H,AT] [H,AY] [AS,AT] [AS,AV] [AT,AU] [AT,AV] [AT,AX]
[AT,AY] [AU,AV] [AU,AW] [AU,AX] [AW,AX] [AW,AY] [AX,AY].
```

Therefore

```text
(V,E,F,C)=(10,24,16,48),  10-24+16=2.
```

This is genuinely outside the nine-vertex graph and is not a serial one-plane transfer. The two new cap sectors communicate through the true edge `[AX,AY]` and the shared AT/AW/AU boundary structure.

The initial split realization is reproducible from

```text
0  =(0,0,0)
C  =(1.69847040407687,0.5553725011502907,0)
H  =(1,0,0)
AS =(1.2750370212826108,0.026077014414937188,-0.07554037883623145)
AT =(-0.34999828357722196,-0.5265987785329982,-0.12686982306207648)
AU =(0.8822075947188457,-0.026661159407639433,-0.12111883969523701)
AV =(1.2558019005415872,-0.003963596908819264,-0.12322049405239077)
AW =(-0.38124935634145823,-0.19747454194987446,-0.047576183648278675)
AX =(-6.0966472204108655,-2.1248956961263166,-0.048285800357527914)
AY =(-6.097356754342121,-2.125041378566523,-0.048223204563894874).
```

The near-coincidence of `AX` and `AY` is only the entry seed; all ten coordinates were then allowed to move globally.

## Robust ten-vertex free-centre chamber

For the same 16-face graph, a robust strict free-centre `(1,1,0)` realization was obtained with target stable face 14, `[AT,AY,AX]`, and unique unstable vertex `C`.

In the same gauge, the 23-coordinate vector

```text
Cx,Cy, ASxyz, ATxyz, AUxyz, AVxyz, AWxyz, AXxyz, AYxyz
```

is

```text
(0.08049573786652404,
 1.6866390702805718,
 1.096350240685115,0.4973924428706211,-0.1400269020496062,
 0.8562209117433688,-0.16632243432204374,-0.3612589450086501,
 0.3386396906393339,0.09614402785298115,-0.7291168118886224,
 0.7062408883310288,0.2857378004542323,-0.5237065361962073,
 -0.47532638404340727,0.25415459085354924,-0.19459365104878465,
 0.09276456622182017,-0.2200432110640593,-0.5254243622245154,
 0.08637128542774775,-0.31075208087166695,-0.14468088542523463).
```

The corresponding mechanical centre is

```text
m=(0.4144193893262541,-0.12360172886899513,-0.321688619671476).
```

At this centre the graph is strict `(1,1,0)` with normalized branch margin approximately

```text
0.06983835131848139.
```

The normalized ordinary-centroid discrepancy is

```text
1.0414164978306302.
```

At its own ordinary centroid this same realization has class `(6,8,12)`, so it is not a homogeneous candidate.

The complete complementary tree enumeration for target face 14 contains `193,776` branches. Exactly four are positive at the robust free-centre source:

```text
branch 152668  margin 0.04437757...
branch 152698  margin 0.06060228...
branch 153280  margin 0.04437757...
branch 153366  margin 0.06060228...
```

Tree-constrained ordinary-centroid homotopies, with retained strict mechanical margin `10^-3`, give best normalized centroid gaps approximately

```text
152668 : 0.6972
152698 : 0.7310
153280 : 0.7205
153366 : 0.7311.
```

No branch reached the ordinary centroid. This closes the four robust free-centre basins generated by this source, not all `193,776` moving-shape branches.

Files:

- Robust ten-vertex free-centre realization (`ax10_fcu_s2_t14_10001.npz`)
- Complete target-14 tree atlas (`split2_trees_t14.npz`)
- Positive branch ledger (`split2_fcu_positive_trees.npz`)
- Branch 152668 homotopy (`ax10_hom_152668.npz`)
- Branch 152698 homotopy (`ax10_hom_152698.npz`)
- Branch 153280 homotopy (`ax10_hom_153280.npz`)
- Branch 153366 homotopy (`ax10_hom_153366.npz`)
- Ten-vertex tree homotopy driver (`ax10_homotopy_tree.py`)

## Ten-vertex projective hard-centering tests

For the robust target-14 free-centre source, the projective centroid equation has at least two finite positive-chart roots.

Moderate root:

```text
a=(0.5523031628496072,2.4585908614594443,-2.2619715784095042)
minimum vertex denominator = 0.6109549586815474
1+a·m = 1.6526495732078568
transformed own-centred class = (4,4,6).
```

Second root:

```text
a=(-0.35225145339099195,1.66637143497371,0.7353683525362479)
minimum vertex denominator = 0.15558...
1+a·m = 0.4114941472182879
transformed own-centred class = (4,3,5).
```

Thus exact projective mass closure by itself destroys the free-centre mechanical chamber.

A subsequent eight-dimensional search over projective parameters plus a determinant-one upper-triangular metric used `4,096` simultaneous initial states and `3,600` annealed gradient steps. Its best complete fixed-graph hard score was

```text
-0.003948817512513151.
```

The best parameter vector was

```text
(-0.6832576303983937,
  0.15948931138627997,
  0.8996138433252521,
 -1.9620622036049005,
  0.08136810731219807,
  0.5657661326878165,
 -3.1547655557336465,
 -1.9530687424119084).
```

Fresh hull reconstruction gives strict class `(3,2,3)` rather than a wall or hidden winner. Its stable faces are

```text
[C,AV,AU], [C,AS,AV], [AT,AY,AX],
```

its unstable vertices are

```text
H, AV,
```

and its saddles are

```text
[AS,AT], [AU,AX], [C,AV].
```

Nonprotected all-external-positive edges `[0,H]` and `[AU,AV]` are also present. The run therefore fails both the equilibrium and antibirth requirements. This is a finite search result, not an orbit impossibility theorem.

Files:

- Projective-centroid root solver for ten vertices (`projective_centroid_root10.py`)
- Stored second projective root (`ax10_fcu_t14_projroot.npz`)
- Projective-plus-metric search driver (`ax10_projmetric_global.py`)
- Best projective-plus-metric state (`ax10_pmg_fc14_11001.npz`)

## Attempts that were deliberately rejected

The following did not qualify and are not promoted:

- fixed-face states that satisfied selected mechanical inequalities after the assumed face list had already ceased to be the actual hull;
- topology-free CMA states that improved the hard score only by making `AX` and `AY` nearly coincident or flattening a face;
- projective roots with very small chart denominators and multiple replacement equilibria;
- own-centroid states with apparent small residuals but cyclic vertex witness assignments that cannot be extended to a rooted tree toward `C`;
- any free-centre `(1,1,0)` object, because its reference point is not the ordinary-volume centroid;
- all wall points with zero or unresolved face, vertex, edge-cone, incidence, or external-arrow margin.

## What changed relative to the supplied journal

The journal described the residual AX packet as a joint metric-cancellation problem but did not know whether the nine-vertex incidence sphere itself forbade the target. The new free-centre realizations answer that question negatively: the graph supports open `(1,1,0)` centre chambers. The obstruction is therefore geometric and homogeneous, not a graph-level Morse obstruction.

The journal also proposed the smallest tenth extreme vertex as a fallback. The connected two-cell split has now been explicitly realized and globally moved far from its entry degeneration. It too supports an open free-centre `(1,1,0)` chamber, and its complete positive-tree basin has been reduced to four branches. However, neither projective hard centering, determinant-one metric freedom, nor tree-constrained direct closure connects those branches to the ordinary centroid.

## Unresolved uncertainty

No rigorous global obstruction was obtained for either:

```text
A. the full 20-dimensional affine-gauged realization space of the AX9 graph;
B. the full 23-dimensional affine-gauged realization space of the split2 ten-vertex graph.
```

The complete branch counts are finite, but only the fixed-parent centre atlas and the locally identified free-centre basins were exhaustively solved. A proof that the nine-vertex graph is empty for the homogeneous target would require exact branchwise semialgebraic infeasibility certificates, interval branch-and-bound over the moving coordinates, or a new invariant linking the ordinary centroid to the two AX-star saddle circuits. None is supplied here.

The ten-vertex free-centre coordinates have large enough margins to be rationalized, but rationalizing an artificial-centre nonwinner would not satisfy the assignment. No watertight ten-vertex mesh or exact H/V ledger is promoted because no own-centred qualifying endpoint was found.

## Strongest continuation

The first continuation that does not repeat the exhausted searches is the **complete ten-vertex target-diversity plus hard-centering sweep**:

1. Run the global free-centre search for all sixteen maximal faces of `split2`, not only faces `0,1,2,14`.
2. For each robust chamber, enumerate its positive complementary trees, solve every finite projective centroid root, and seed the full projective-plus-metric orbit from each root.
3. Run direct own-centred tree optimization on the complete `193,776` target branch set. The prepared batched driver is ax10_tree_global.py; it was created but not completed in this determination.
4. Freshly reconstruct the hull after every putative crossing. Require ten actual vertices, sixteen actual maximal faces or an explicitly accepted adjacent topology, positive raw separation, `C` as the sole unstable vertex, one stable face, zero full-cone saddle edges, and a strict negative external witness for every nonprotected true edge.
5. Only after a positive actual-hull chamber appears should its coordinates be rounded to dyadic rationals and the exact AX9 packaging pipeline be rerun to produce irredundant H/V data, exact volume and moments, exhaustive mechanics, perturbation radius, independent verifier, manifest, OBJ, and STL.

If the complete ten-vertex target-diversity sweep remains separated from centring, the first genuinely larger topology should not be another AX/AY serial split. It should add an eleventh vertex forming a transverse communicating band between the two cap cells, so the stable-face, unstable-vertex, and two saddle witness systems can change across different but coupled circuits while two vertices provide independent negative exits and three remaining coordinate combinations close the ordinary moments.

## Reproducibility index

- Authoritative exact AX9 archive (`Calm_Finch_13_AX9_exact_NONWINNER.zip`)
- Authoritative AX9 handoff (`HANDOFF.md`)
- AX9 exact manifest (`MANIFEST.json`)
- AX9 clean extraction receipt (`Calm_Finch_13_AX9_clean_extraction_receipt.json`)
- Generic actual-hull evaluator (`generic_eval.py`)
- Nine-vertex affine-gauge model (`ax9_model.py`)
- Ten-vertex split generator data (`ax10_split2.npz`)
- Ten-vertex actual-hull evaluator and optimizer (`topofree10_cma.py`)
- Ten-vertex free-centre optimizer (`ax10_freecenter_unbranched.py`)
- Prepared complete ten-vertex tree search (`ax10_tree_global.py`)

## Final statement

`NONWINNER`, honestly delimited. The exact parent remains the strongest fully certified homogeneous object in this direction. The main new fact is that both the nine-vertex AX graph and the smallest ten-vertex connected two-cell split admit robust mono-monostatic **mechanical-centre** chambers, while all completed routes to their own ordinary-volume centroids remain nonwinning. This converts the next task from speculative topology invention into a finite, target-diverse mass-centering search on a concrete ten-vertex graph, but it does not yet supply the requested homogeneous convex polyhedral Gömböc.
