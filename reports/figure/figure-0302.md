# figure-0302

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Keen Quartz 73 — exact AX12 mechanics-changing target turnover

## Determination

**USED exact nonwinner.** The first mechanics-changing incidence topology requested from immutable parent `figure-0299` (SHA-256 `2c28fe4781353da1c2fdd2b85cb4f28fc41e59870e8fdbfcfd291e002831fd72`) is realized, reconstructed from scratch, and exactly delimited. The old stable plane and edge are genuinely removed, the replacement band has full three-dimensional moment response, and a later stable–saddle pair cancels with no replacement birth. Nevertheless the fixed-parent two-apex topology cannot have zero ordinary first moment: an exact rational capacity certificate gives `My>1/4` for every realization in the cell. The promoted endpoint is strict `(1,1,0)` only relative to the inherited mechanical centre; at its own exact centroid it is `(6,9,13)`, so it is not a homogeneous polyhedral Gömböc.

The parent result establishes the preceding AX10 mass-capacity obstruction and names this two-apex turnover as the first nonrepeating topology. :contentReference[oaicite:0]{index=0} Its literal robust split2 source has stable `[AT,AY,AX]`, unique unstable `C`, and no saddle relative to a free mechanical centre, but its ordinary centroid is far away. :contentReference[oaicite:1]{index=1}

## 1. Literal exact source

Let `D=2^30=1073741824`. In inherited labels, the ten old vertices relative to the mechanical origin are

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

Their hull is `(V,E,F)=(10,24,16)`, strict `(1,1,0)` relative to the origin, with sole stable `[AT,AY,AX]`, sole unstable `C`, no saddle, and exact volume

```text
4314676606919473104543174179
/7427640235712281649394745344.
```

The parent's exact one-apex ballast vertex is

```text
B0=(-32710630594922633/54043195528445952,
    -3448603418778333479/55340232221128654848,
     176803367644130467/18446744073709551616).
```

Its 11-vertex hull is `(11,27,18)` and remains strict origin-relative `(1,1,0)`, but is not own-centred.

## 2. Exact two-apex turnover

The exact source band is

```text
BP_source=(-513382185,-142086558, -5914964)/D
BM_source=(-351299687,-191515897,-28790723)/D.
```

The promoted endpoint is

```text
BP=(-566452371, -64944888,   6045068)/D
BM=(-357321279,-165773795, -89441010)/D.
```

Delete adjacent faces `[AW,AX,AY]` and `[AT,AY,AX]`, and insert

```text
[AW,AX,BP] [AW,BP,AY] [AY,BP,BM]
[AX,BM,BP] [AT,AY,BM] [AT,BM,AX].
```

Hence `[AX,AY]` is absent and `[BP,BM]` is a true transverse edge. The added region is the connected union of

```text
Tplus   =[AW,AX,AY,BP],
Vplus   =29992583379453228737665153/7427640235712281649394745344;
Tmiddle =[AX,AY,BP,BM],
Vmiddle =3158872076190221170886495/7427640235712281649394745344;
Tminus  =[AT,AY,AX,BM],
Vminus  =1270833098788153905029647/928455029464035206174343168.
```

All three volumes are exactly positive. `Tplus,Tmiddle` share `[AX,AY,BP]`; `Tmiddle,Tminus` share `[AX,AY,BM]`.

## 3. Fresh hull, faces, and true edges

Exact all-triple reconstruction gives `(V,E,F)=(12,30,20)` and Euler `12-30+20=2`. All maximal faces are physical triangles, outward oriented as

```text
[0,H,C] [0,C,AW] [0,AY,H] [0,AW,AY]
[C,H,AS] [C,AS,AV] [C,AV,AU] [C,AU,AW]
[H,AT,AS] [H,AY,AT] [AS,AT,AV] [AT,AU,AV]
[AT,AX,AU] [AT,BM,AX] [AT,AY,BM] [AU,AX,AW]
[AW,AX,BP] [AW,BP,AY] [AX,BM,BP] [AY,BP,BM].
```

The 30 true edges are

```text
[0,C] [0,H] [0,AW] [0,AY]
[C,H] [C,AS] [C,AU] [C,AV] [C,AW]
[H,AS] [H,AT] [H,AY] [AS,AT] [AS,AV]
[AT,AU] [AT,AV] [AT,AX] [AT,AY] [AT,BM]
[AU,AV] [AU,AW] [AU,AX]
[AW,AX] [AW,AY] [AW,BP]
[AX,BP] [AX,BM] [AY,BP] [AY,BM] [BP,BM].
```

There are no display-only diagonals. For every outward face `[i,j,k]`, the exact H row is reconstructed by

```text
n=(v_j-v_i)×(v_k-v_i),  h=n·v_i,  n·x<=h,
```

followed by denominator clearing and integer-gcd reduction. These 20 rows are irredundant. The minimum normalized nonincidence gap is

```text
6661894133668764764154293/60336325858574764360583975
≈0.11041265835914339.
```

## 4. Exact mass and own-centering

The endpoint volume is

```text
V=4357994727165421785691963003
  /7427640235712281649394745344
 ≈0.5867266842316989.
```

Its first moments about the mechanical origin are

```text
Mx=-129283623573576945558313992714273453
   /2658455991569831745807614120560689152,
My= 570676723834719916411078553549181967
   /1993841993677373809355710590420516864,
Mz= 550901870345123515855724240192456793
   /10633823966279326983230456482242756608.
```

The exact ordinary centroid is

```text
c=(-387850870720730836674941978142820359
    /4679361207328982337898225456981737472,
    570676723834719916411078553549181967
    /1169840301832245584474556364245434368,
    1652705611035370547567172720577370379
    /18717444829315929351592901827926949888)
 ≈(-0.08288543105269688,0.48782446881074765,0.08829760825296218).
```

The own-centred V-data are exactly `v_i-c`; the own-centred H offsets are exactly `h-n·c`. A separate oriented boundary tetrahedral sum returns the same positive volume and all three translated first moments exactly zero.

## 5. Exhaustive mechanics and arrows

Every maximal-face barycentric cone, every incident directed vertex support `sigma(a->b)=a·(a-b)`, and all four components `(t,1-t,beta1,beta2)` of every true-edge cone were recomputed exactly.

At the inherited mechanical centre:

```text
stable   [AT,AY,BM]
unstable C
saddles  none
class    (1,1,0).
```

Readable strict margins are

```text
stable positive minimum                 +0.18987740266646644
selected nonstable exclusion maximum    -0.07328285654668315
unstable-C directed-support minimum     +2.4701382600412787
selected nonunstable exclusion maximum  -0.04290997024348679
selected nonsaddle component maximum    -0.02301969663514523.
```

The complete external-arrow audit leaves only `[C,AS]`, `[C,AU]`, and `[C,AW]` all-external-positive; all belong to the protected `C` star. Every nonprotected edge, including `[BP,BM]`, has a strict negative external witness.

At the exact ordinary centroid:

```text
stable:
[0,H,C], [C,AV,AU], [C,AU,AW],
[AT,AX,AU], [AT,AY,BM], [AY,BP,BM]

unstable:
H, C, AW, AY, AS, AU, AT, BM, BP

saddles:
[C,AW] [H,AS] [C,AS] [C,AU] [H,AT]
[AT,AY] [AT,AU] [AU,AX] [AT,BM]
[AY,BM] [AW,BP] [AY,BP] [BP,BM]

class=(6,9,13).
```

Thus the endpoint is not a homogeneous Gömböc.

## 6. Positive exact chamber and moment rank

Vary all six coordinates of `BP,BM` independently by `2^-50`. Closed rational interval arithmetic preserves all 12 extreme vertices, all 20 faces, all 30 true edges, positive volume, origin-relative `(1,1,0)`, and a negative external witness on every nonprotected edge.

The exact first-moment Jacobian with respect to

```text
BP.x,BP.y,BP.z,BM.x,BM.y,BM.z
```

has rank three. All 20 maximal minors are nonzero. For columns `BP.x,BP.z,BM.y`,

```text
det J=
-21184607465227647552154758025799611272435530142103358128689926108008503074525
/121416805764108066932466369176469931665150427440758720078238275608681517825325531136
!=0.
```

Moment-rank deficiency is therefore ruled out; three local topology controls remain after three moment equations.

## 7. Complete exact chronology

### Parent one-apex to two-apex source

Let

```text
BP(t)=(1-t)B0+t BP_source,
BM(t)=(1-t)B0+t BM_source.
```

The unique topology wall is

```text
t_flip=553160724732211548230517264180606529
       /736793219476084971505969160270411329
≈0.7507679361185627.
```

At `t_flip`, `AT,AX,AY,BM` are coplanar; `[AX,AY]` disappears, `[AT,BM]` appears, and the stable feature transfers from `[AT,AY,AX]` to `[AT,AY,BM]` without a saddle.

A later root `t_birth≈0.8140750794113056` is the positive root of

```text
3883162284720576660001223842529655206355916764573985409 t^2
+3724447064036675081156114567500549461722366817020422910 t
-5605421994651062516829280497534560126612346123988112767=0.
```

At this root `[AT,BM,AX]` and `[AT,BM]` become an extra stable–saddle pair. Hence

```text
t=0              (1,1,0), stable [AT,AY,AX]
0<t<t_flip       (1,1,0), stable [AT,AY,AX]
t_flip<t<t_birth (1,1,0), stable [AT,AY,BM]
t_birth<t<=1     (2,1,1), extra S=[AT,BM,AX], H=[AT,BM].
```

### Two-apex source to promoted endpoint

Let

```text
BP(s)=(1-s)BP_source+s BP,
BM(s)=(1-s)BM_source+s BM.
```

The hull stays `(12,30,20)`. All 440 primitive sign functions reduce to 128 integer polynomials and were Sturm-counted. A noncritical witness exchange occurs at `s1≈0.5745834063261627`. The only mechanics-changing root is `s2≈0.5792339532898435`, the positive root of

```text
1637235186645253007111446258273451 s^2
-6153435042236110187775305501868661 s
+3014966498673519880266222928025452=0.
```

At `s2`, the final positive face component of `[AT,BM,AX]` and one incident-normal component of `[AT,BM]` vanish through the same irreducible factor; immediately afterward both are excluded and no other equilibrium is born:

```text
0<=s<s2  (2,1,1), extra S=[AT,BM,AX], H=[AT,BM]
s2<s<=1  (1,1,0), sole S=[AT,AY,BM], sole U=C, H=none.
```

This is an exact no-birth stable–saddle cancellation in a genuine incidence-changing connected band.

## 8. Exact global obstruction for this topology

Keep the ten old exact vertices and all fourteen parent facets except `[AW,AX,AY]` and `[AT,AY,AX]`; allow arbitrary `BP,BM` realizing the same two-apex band. Both new vertices must lie in the bounded rational intersection `R` of those fourteen retained halfspaces. Exact vertex enumeration and a Farkas dual give

```text
y >= ymin =
-24319977376994409927066681050406628063433486920722026843945
/76537955871201268020612157430232116907562112808277323546624
≈-0.3177505474266948.
```

The dual uses exactly `[AW,AU,AX]`, `[H,AY,AT]`, and `[AW,AY,0]`. Bounding the negative y-moment of the three possible added tetrahedra then yields

```text
My_total >=
896424379186937811114315808836412703445054375148336083815984246698145386554251258170275051497413372351350679980850126896401466786852127613483319029732264807388212399624929395819465250495858053737061740480772293141000632285604752874681563997941
/
3398902865118551107135881163605987477302250214131826624728670067451501461536290783557916479886591192537252173990911914473988678677042443386453384193894990342097285245540158718157617144450185572689844727954960484863530202809070282242867891011584
>1/4.
```

Numerically the certified lower bound is `0.2637393343559617`. Therefore no realization anywhere in this literal fixed-old-vertex two-apex topology can have zero ordinary first moments. This obstruction is new and applies after the parent spherical-slab hypotheses have been broken.

## 9. First nonrepeating successor, realized exactly

The dual certificate shows that a successor must change at least one of `[AW,AU,AX]`, `[H,AY,AT]`, `[AW,AY,0]`. Add return vertex

```text
BR=(117950357,-138535356,124670127)/2^30
```

and replace `[H,AY,AT]`, `[AT,AY,BM]` by

```text
[H,AY,BR] [AY,BM,BR] [BM,AT,BR] [AT,H,BR].
```

Fresh exact reconstruction gives

```text
(V,E,F)=(13,33,22),
origin-relative class=(1,1,0),
stable=[AT,BR,BM],
unstable=C,
saddles=none,
nonprotected all-external-positive edges=none.
```

Its exact volume is

```text
4379457137575473520768921763/7427640235712281649394745344,
```

and its exact centroid is

```text
(-384173210340146219234009075651670803/4702406295030107875854123936316915712,
 1140526691341047471863680578517303093/2351203147515053937927061968158457856,
 1664225728894608659623748022284911859/18809625180120431503416495745267662848)
≈(-0.08169715380531288,0.485082155723741,0.08847734672849836).
```

At its own centroid it remains `(6,9,13)`, so it is a successor seed, not a candidate winner. The next finite problem is to solve the three exact moment equations in the nine coordinates of `BP,BM,BR`, leaving six topology/antibirth controls. If this family remains capacity-limited, coordinated motion or deactivation of one old vertex on the three dual-tight facets is necessary; any further apex confined by all fourteen old halfspaces repeats the proved obstruction.

## 10. Independent replay and artifacts

`verifier/verify_cleanroom.py` uses only Python's standard library and `fractions.Fraction`; it does not import the materializer or trust stored incidence. It reconstructs the parent and turnover, exact hulls, true edges, tetrahedral cells, volume/moments/centroid, all face/vertex/four-component edge cones, full arrow audit, `2^-50` chamber, rank-three Jacobian, both Sturm chronologies, the global moment bound, the AX13 successor, and OBJ/STL watertightness. Clean extraction ends with:

```text
KQ73_AX12_PARENT_TO_SOURCE_SPLIT_CHRONOLOGY_PASS
KQ73_AX12_CONNECTED_BAND_RANK3_MOMENT_RESPONSE_PASS
KQ73_AX12_FRESH_HULL_MASS_MECHANICS_PASS
KQ73_AX12_SIX_COORDINATE_BOX_PASS
KQ73_AX12_COMPLETE_STURM_CHRONOLOGY_PASS
KQ73_AX12_FIXED_PARENT_BAND_MOMENT_OBSTRUCTION_PASS
KQ73_AX13_FIRST_NONREPEATING_SUCCESSOR_SEED_PASS
KQ73_AX12_WATERTIGHT_MESH_PASS
KQ73_AX12_ALL_EXACT_CHECKS_PASS
KQ73_AX12_MANIFEST_PASS
KQ73_AX12_PACKAGE_ALL_PASS.
```

Artifacts:

- [Complete package](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER.zip), 96,066 bytes, SHA-256 `a16e71337fa99566e6c0957e48d862f300d820860de75290dc9e0cb790a27ad7`.
- [Archive sidecar](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER.zip.sha256).
- [Standalone handoff](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/RESEARCH_HANDOFF.md), SHA-256 `b31680684204808a717ee07328462e0f7c8d4e580a3ca0988518713ea6758013`.
- [Exact generator](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/source/generator.json), SHA-256 `e8d6927fcfd382c721621fad114cef9c9f1993a29407f10843597e9f6e5e2333`.
- [Exact mechanical-centre V](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/data/V_mechanical_exact.tsv) / [exact own-centred V](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/data/V_own_centered_exact.tsv).
- [Exact mechanical-centre H](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/data/H_mechanical_exact.tsv) / [exact own-centred H](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/data/H_own_centered_exact.tsv).
- [Parent-to-source chronology](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/certificates/parent_to_source_split_chronology.json), SHA-256 `90baf149b62c9e5e754b9d01315fa3adc86a4906041feddef9fca8d2e32d8961`.
- [Source-to-endpoint chronology](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/certificates/equilibrium_chronology.json), SHA-256 `b80c47eb47d4cbce9215081e89b2a9ea4d144017ddaae8cf2bf5afc6bb4a69da`.
- [Global moment obstruction](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/certificates/fixed_parent_band_moment_obstruction.json), SHA-256 `98d670af656c7bdbda6189dc7d976234462d12f951b3821d0c51df5275220af3`.
- [Moment rank](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/certificates/moment_response_rank.json), SHA-256 `0d03b52f1178e9243c7af6d453c3c6aec745846cdc3bed13b8978e3f5fc8ff70`.
- [Perturbation box](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/certificates/perturbation_box.json), SHA-256 `f4655f5065239281b1cfd2c3d388bcec05d9ed248b1bcff57140351a5c9ea043`.
- [AX13 successor seed](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/certificates/next_AX13_F11_return_seed.json), SHA-256 `f9252b950e4f5cb92cc188d84193418e566f502930a966d37747f650a911a62d`.
- [Independent verifier](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/verifier/verify_cleanroom.py), SHA-256 `642e30654d5206924081e79e34227138e6f401a382d8755d540f9460a69a15cc`.
- [Watertight OBJ](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/mesh/body.obj) / [STL](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER/mesh/body.stl), SHA-256 `6ae69b4deff3670f3cbc86a3c78962482ac483b685f9f54f63f8875670f0753e` / `6a2f7f3bc0ee28645a7b220ddd7d3ca3d6524b0c9c2b3deba4288bcb370b87d7`.
- [Clean replay transcript](sandbox:/mnt/data/Keen_Quartz_73_AX12_target_turnover_EXACT_NONWINNER_CLEAN_EXTRACTION.log), SHA-256 `ecc62a5670d738b5440ff2863b496c19629034f31a67b10e99c9db14cdd03fac`.

## Bottom line

The first AX mechanics-changing turnover is real and exact, and it contains an open no-birth `(1,1,0)` chamber relative to the target centre. It cannot be made homogeneous with the ten old vertices fixed: `My>1/4` throughout the complete two-apex cell. The exact 13-vertex return-cell seed above is the first genuinely nonrepeating continuation because it removes one of the three halfspaces supporting the obstruction.
