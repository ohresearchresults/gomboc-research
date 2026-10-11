# figure-0299

Historical AI scientific report · saved 2026-09-04 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Keen Quartz 73 — exact AX10 ballast determination

## Verdict

**EXACT NONWINNER, but the smallest connected full-rank ballast family is now constructed and its failure is proved globally inside the requested preserved mechanical chamber.**

The immutable parent is `figure-0295`, SHA-256 `06aa7cd747bc7a15ec04b67d9998678ab9c12bff418bebe04c25333bb5a80ccf`. :contentReference[oaicite:0]{index=0} It supplied a robust ten-vertex `split2` realization with a strict free-centre `(1,1,0)` chamber, stable face `[AT,AY,AX]`, unique unstable vertex `C`, and a distant ordinary centroid; its previous projective and metric hard-centering attempts were nonwinning. :contentReference[oaicite:1]{index=1}

I rationalized that chamber exactly, added one extreme ballast vertex, proved a three-dimensional moment-response rank, and certified a full exact perturbation box. The ballast reduces the centroid discrepancy while preserving strict `(1,1,0)` mechanics relative to the target centre. However, an exact spherical-slab inequality proves that **no convex ballast with any finite number of vertices can close the centroid while both `[AT,AY,AX]` and `C` retain their strict roles**. A mechanics-incidence turnover is therefore mandatory.

## Exact source

Set the mechanical centre to the origin and `D=2^30`. The ten exact source vertices are

```text
0  = (-444979431,  132716346,  345410525)/D
C  = (-358547791, 1943731258,  345410525)/D
H  = ( 628762393,  132716346,  345410525)/D
AS = ( 732217676,  666787415,  195057784)/D
AT = ( 474380773,  -45871008,  -42488313)/D
AU = ( -81367832,  235950210, -437472690)/D
AV = ( 313340949,  439524973, -216915086)/D
AW = (-955357250,  405612760,  136467183)/D
AX = (-345374236, -103553253, -218759588)/D
AY = (-352238969, -200951160,  190060607)/D.
```

Fresh exact hull reconstruction gives `(V,E,F)=(10,24,16)`, stable `[AT,AY,AX]`, unstable `C`, and no saddle edge. Its exact volume is

```text
4314676606919473104543174179/7427640235712281649394745344.
```

Its exact ordinary centroid is

```text
(-1473813210086390509534743809321315697/18531394919535384289564522118836649984,
  9136681163149509051862738422235609781/18531394919535384289564522118836649984,
  825639602344978981352215841493392229/9265697459767692144782261059418324992)
≈(-0.0795306136686305,0.4930379608670378,0.0891071185876686).
```

## One-vertex connected ballast

Let

```text
Ncap=(AX-AW)×(AY-AW),
B0=(AW+AX+AY)/3+(7/16)Ncap.
```

Exactly,

```text
B0=(-32710630594922633/54043195528445952,
    -3448603418778333479/55340232221128654848,
     176803367644130467/18446744073709551616).
```

`B0` is extreme and lies beyond only `[AW,AX,AY]`. The added tetrahedron has exact positive volume

```text
144508408676502549659240920023842709/21267647932558653966460912964485513216.
```

The new hull has `(V,E,F)=(11,27,18)` and outward maximal faces

```text
[0,H,C] [0,C,AW] [0,AY,H] [0,AW,AY]
[C,H,AS] [C,AS,AV] [C,AV,AU] [C,AU,AW]
[H,AT,AS] [H,AY,AT] [AS,AT,AV] [AT,AU,AV]
[AT,AX,AU] [AT,AY,AX] [AU,AX,AW]
[AW,AX,B0] [AW,B0,AY] [AX,AY,B0].
```

Its true edges are

```text
[0,C] [0,H] [0,AW] [0,AY]
[C,H] [C,AS] [C,AU] [C,AV] [C,AW]
[H,AS] [H,AT] [H,AY] [AS,AT] [AS,AV]
[AT,AU] [AT,AV] [AT,AX] [AT,AY]
[AU,AV] [AU,AW] [AU,AX]
[AW,AX] [AW,AY] [AW,B0] [AX,AY] [AX,B0] [AY,B0].
```

Every face is physical and triangular; no display-only diagonal is scored. The exact H row for each listed cycle `[a,b,c]` is reconstructed as `n=(b-a)×(c-a)`, `h=n·a`, with inequality `n·x≤h`. The primitive integer H table is included in the package.

The ballasted exact volume and centroid are

```text
V=37496315065100276228106766997744828095/63802943797675961899382738893456539648,

c=(-229148455774016401825380096936223909085942027785662141/2701894248879237111757727915338050598326681414318161920,
    1348590846137541536195431910356025787199230958805777451853/2766739710852338802439913385306163812686521768261797806080,
    244565095295768874879459876530937325010687034841212192669/2766739710852338802439913385306163812686521768261797806080)
≈(-0.08481029776389977,0.48742960562852744,0.08839468864254912).
```

Thus `||c||≈0.5025873337<0.5072983618=||c0||`; the cap moves mass toward the target but does not close it. At its own centroid the body is strict `(5,9,12)`, so it is not a homogeneous Gömböc.

## Exact mechanics and open chamber

Relative to the origin, exhaustive exact face, full incident-vertex, and four-component true-edge cones give

```text
stable   [AT,AY,AX]
unstable C
saddles  none
class    (1,1,0).
```

Representative strict margins are

```text
stable lambda minimum          +0.2761814329784276
closest nonstable witness      -0.07328285654668315
unstable-C arrow minimum       +2.470138260041279
closest nonunstable witness    -0.06898091144220728
closest nonsaddle component    -0.02301969663514523.
```

All 222 external-arrow components were checked. The only all-external-positive edges are `[C,AS]`, `[C,AU]`, and `[C,AW]`, all in the protected `C` star; every nonprotected edge has a strict negative external witness.

For independent variations of the three coordinates of `B0` with `|δi|≤2^-40`, closed rational interval arithmetic certifies the same 11 vertices, 18 faces, 27 true edges, class `(1,1,0)`, no nonprotected carrier, positive cap volume, and moment-response rank three.

## Full-rank moment response

For a variable apex `y`, put `s=AW+AX+AY` and `Δ=Ncap·(y-AW)`. The unnormalised volume first moment is

```text
Φ(y)=M0+Δ(s+y)/24,
J(y)=[ΔI+(s+y)Ncap^T]/24.
```

The determinant lemma gives

```text
det J=Δ²(2Δ+4hcap)/24³,
hcap=Ncap·AW
=123173836514377819053498339/1237940039285380274899124224>0.
```

At `B0`, `Δ>0` and

```text
det J
=17747741770648086857953495400724778100722631179962102239430900448560288258366228836058722575873586822123181
 /307828173409331868845930000782371982852185463050511302093346042220669701339821957901673955116288403443801781174272
>0.
```

Hence the three ballast-coordinate responses span all three moment directions. Rank failure is not the obstruction.

## Exact mass-capacity obstruction

For the retained stable face, take outward normal

```text
N=(1273441246817475/36028797018963968,
  -168171228935025665/576460752303423488,
  -39723224459300289/576460752303423488),
```

with `h=N·AT`, `L²=N·N`, and

```text
R²=||C||²=2012978076269008935/576460752303423488.
```

The base requires positive target-normal moment

```text
A=-N·M0
=1632150066596482385584913174653436603750073663082618927
 /18389946490390666300300164325803710203424869466203226112.
```

If `C` remains the unique unstable vertex, every other vertex has a negative outgoing arrow to a strictly larger-radius neighbour; following arrows ends at `C`. Therefore every vertex lies in the radius-`R` ball. If `[AT,AY,AX]` remains stable, the whole extension also lies in `N·x≤h`. Consequently all positive moment any ballast can add is bounded by the full spherical slab

```text
Bmax=π(R²d²/2-d⁴/4),  d=h/sqrt(L²).
```

Numerically, the required moment is `0.2940423417571676`, whereas the entire slab supplies at most `0.05704918480905592`; the ratio is `5.154190068470386`.

The proof is exact. With `T=2R²h²L²-h⁴` and `π<22/7`, the checker verifies

```text
16A²(L²)³ > (484/49)T²,
```

with exact left/right ratio `≈26.54430282781873>1`. Thus no number of added ballast vertices can centre this source without first changing the target stable plane or the unique unstable carrier.

Within the one-face cap family, centroid closure has the unique positive root of

```text
Δ²+4hcapΔ+24(Ncap·M0)=0.
```

It is isolated to width `2^-100` at `Δ≈0.9612340857009457`; the corresponding apex has `||B*||²>61.6824>R²≈3.492`, so it becomes a radial maximum and leaves the unique-`C` chamber.

## First nonrepeating continuation

The smallest robust architecture that removes the theorem’s hypothesis is a **two-apex target-face-turnover band**. Replace adjacent faces `[AW,AX,AY]` and `[AT,AY,AX]` by

```text
[AW,AX,B+] [AW,B+,AY]
[AY,B+,B-] [AX,B-,B+]
[AT,AY,B-] [AT,B-,AX].
```

The old edge `[AX,AY]` becomes interior or disappears and `[B+,B-]` supplies transverse communication. Six apex coordinates leave three independent topology/antibirth controls after the three moment equations. The event must transfer the stable plane or unstable carrier before closure, retain exactly one stable and one unstable equilibrium, eliminate all saddles, and give every inserted or star-changed nonprotected edge a negative external witness. This is distinct from the exhausted fixed-graph tree sweep.

## Replay and artifacts

Run `bash RUN_ALL.sh`. The clean verifier uses only Python standard-library rational arithmetic, reconstructs the hull rather than trusting stored incidence, verifies the `2^-40` box, moment rank, root isolation, slab theorem, mechanics, arrows, and mesh, and ends with `KQ73_AX10_PACKAGE_ALL_PASS`.

- [Complete exact package](sandbox:/mnt/data/Keen_Quartz_73_AX10_ballast_rank3_EXACT_NONWINNER.zip), SHA-256 `d3cc19b884b0c59b731f5aea570396ea708fc9160560d8637b631c6629b341e6`.
- [Standalone handoff](sandbox:/mnt/data/Keen_Quartz_73_AX10_ballast_rank3_EXACT_NONWINNER/RESEARCH_HANDOFF.md).
- [Exact source](sandbox:/mnt/data/Keen_Quartz_73_AX10_ballast_rank3_EXACT_NONWINNER/source/generator.json), [V data](sandbox:/mnt/data/Keen_Quartz_73_AX10_ballast_rank3_EXACT_NONWINNER/data/V_exact.tsv), and [H data](sandbox:/mnt/data/Keen_Quartz_73_AX10_ballast_rank3_EXACT_NONWINNER/data/H_exact.tsv).
- [Mechanics and arrow ledger](sandbox:/mnt/data/Keen_Quartz_73_AX10_ballast_rank3_EXACT_NONWINNER/data/mechanics_exact.json).
- [Moment/root certificate](sandbox:/mnt/data/Keen_Quartz_73_AX10_ballast_rank3_EXACT_NONWINNER/certificates/mass_response_and_root.json) and [slab obstruction](sandbox:/mnt/data/Keen_Quartz_73_AX10_ballast_rank3_EXACT_NONWINNER/certificates/exact_spherical_slab_obstruction.json).
- [Independent verifier](sandbox:/mnt/data/Keen_Quartz_73_AX10_ballast_rank3_EXACT_NONWINNER/verifier/verify_cleanroom.py).
- [Watertight OBJ](sandbox:/mnt/data/Keen_Quartz_73_AX10_ballast_rank3_EXACT_NONWINNER/mesh/body.obj) and [STL](sandbox:/mnt/data/Keen_Quartz_73_AX10_ballast_rank3_EXACT_NONWINNER/mesh/body.stl).
- [Clean-extraction replay](sandbox:/mnt/data/Keen_Quartz_73_AX10_ballast_rank3_EXACT_NONWINNER_CLEAN_REPLAY.log).

## Bottom line

The ballast idea succeeds locally in the strongest possible sense—smallest connected cap, exact positive volume, full three-dimensional moment rank, robust strict `(1,1,0)` mechanics—but fails globally in the preserved AX10 chamber by an exact capacity inequality. The next construction must be a coupled incidence-and-mass turnover, not more ballast inside the same stable-plane/unstable-vertex cell.
