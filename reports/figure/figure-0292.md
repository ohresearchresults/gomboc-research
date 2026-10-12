# figure-0292

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Keen Quartz 73 — J56 orphan reconstruction and exact determination

## Journal status reconciled

The recovered response was explicitly recorded as source evidence rather than an immutable or accepted completion, so none of its endpoint claims could be inherited without replay. :contentReference[oaicite:0]{index=0} The prose claims that an exact `alpha_star` and three dyadic belt depths exist, but supplies only formulas and says those four values are serialized in a missing exact-source file. :contentReference[oaicite:1]{index=1} The latest journal correction therefore asks for literal reconstruction or precise falsification of this orphan rather than acceptance by description. :contentReference[oaicite:2]{index=2}

## Determination

**The recovered publication does not determine, and its stated proof does not establish, a 21-vertex homogeneous polyhedral Gömböc.** This package gives an exact falsification of `J56_TB9_metric_cancel_belt24` **as published**, together with two canonical independently checkable rational controls:

1. the smallest direct counterobject, an 18-support exact post-wall body of class `(2,2,2)`;
2. an exact 24-support / 21-vertex belt-template realization with the advertised `(21,43,24)` incidence counts, but class `(1,2,1)`.

This is not a global impossibility theorem for every four-parameter shear/belt placement. The four exact parameters that would define the alleged endpoint are absent, so another later parameter choice would be a new object requiring a fresh full audit.

## Source authority

Literal parent result:

```text
assignment  figure-0266
SHA-256    49545ef8d787bb7886f19249253131f72ee0f35f1bb499c3bce73e75cbf23fd1
name       J55_D17R_anti_carrier18
class      (1,2,1)
```

The exact parent archive was independently replayed before this audit. Its archive SHA-256 is `d6f285ed83cd8b330af59796dfb30819d95db1a2d90b16c83deacb032bc9366b`; its exact-source SHA-256 is `ba6f45ae283e444a4ee92ff14e4987041ca4e442a181892675f6b8af00759fa3`.

The recovered J56 prose references worker-local files that are not present. In particular it never prints the reduced rational `alpha_star` or the three dyadics `epsilon_0, epsilon_1, epsilon_16`. Those four numbers are indispensable: they determine every one of the nine inserted rows, the raw centroid, the projectively centred H/V data, and all mechanics. Consequently the alleged 21-vertex endpoint is not uniquely reconstructible from the publication.

## Compact exact parent generator

Let `N=2^24`. The first 17 raw dual supports have `z=-1/140` and the following exact integer `x,y` numerators over `N`:

```text
00 14000 ( 11653197,-13937873,-1/140) / x,y denominator 2^24
01 14001 (  5763878,-16027135,-1/140) / x,y denominator 2^24
02 14002 ( 16793753, -9690398,-1/140) / x,y denominator 2^24
03 14003 ( 20394447, -3554346,-1/140) / x,y denominator 2^24
04 14004 ( 21762407,  3910885,-1/140) / x,y denominator 2^24
05 14005 ( 20408886, 11892808,-1/140) / x,y denominator 2^24
06 14006 ( 16140728, 19400855,-1/140) / x,y denominator 2^24
07 14007 (  9124192, 25373787,-1/140) / x,y denominator 2^24
08  2475 (   -90148, 28809026,-1/140) / x,y denominator 2^24
09  5000 ( -9304549, 25373787,-1/140) / x,y denominator 2^24
10 14008 (-16321192, 19400855,-1/140) / x,y denominator 2^24
11 14009 (-20589485, 11892808,-1/140) / x,y denominator 2^24
12 14010 (-21943151,  3910885,-1/140) / x,y denominator 2^24
13 14011 (-20575324, -3554346,-1/140) / x,y denominator 2^24
14 14012 (-16974741, -9690398,-1/140) / x,y denominator 2^24
15 14013 (-11834262,-13937873,-1/140) / x,y denominator 2^24
16 14014 ( -5944980,-16027135,-1/140) / x,y denominator 2^24
```

The apex is

```text
5003 = (271080,-15609202,360000)/2^24.
```

The canonical label order is

```text
[14000,14001,14002,14003,14004,14005,14006,14007,
 2475,5000,14008,14009,14010,14011,14012,14013,14014,5003].
```

These are the literal finite parent data recorded in the recovered source description. :contentReference[oaicite:3]{index=3}

Enumerate the raw dual hull exactly, solve `q_i·p=1` for each maximal dual face, and integrate

```text
V = (1/6) Σ det(p0,p1,p2),
M = (1/24) Σ det(p0,p1,p2)(p0+p1+p2),
c55 = M/V.
```

Then projectively centre by

```text
q_i <- q_i/(1-q_i·c55),
p_v <- p_v-c55.
```

This independently reconstructs the parent at exact ordinary centroid zero with stable row `2475`, unstable features `[2475,5000,5003]` and the residual 17-gon, and sole saddle `(14001,14014)`.

## Exact contradiction in the advertised shear stage

Let `R=(0,1,...,16)`, let `n` be the parent primal vertex dual to `R`, let `a=q_1`, `b=q_16`, and orient

```text
u = n × (b-a)
```

so that `u·(q_i-a)<0` for every `i in R\{1,16}`. Define

```text
p0       = n/(n·n),
alpha0   = -(n·n) u·(p0-a)/(u·u),
B(alpha) = I-alpha u n^T/(n·n).
```

Because `u·n=0`, `det B(alpha)=1` and `B(alpha)^(-1)=I+alpha u n^T/(n·n)`. Use

```text
q_i(alpha)=B(alpha)q_i,
p_v(alpha)=B(alpha)^(-T)p_v.
```

The independently derived exact wall is `alpha0≈191.5535846983706`. At `alpha=alpha0`, the residual polygon's unstable-cone margin and one component of the closure-edge saddle cone are exactly zero, as the orphan description says. But the rest of the description is false. At the same exact parameter the following replacement packet is already strict:

```text
stable    5003
unstable  [14001,14014,5003]
saddles   [14003,5003], [14011,5003].
```

Together with protected stable `2475` and protected unstable `[2475,5000,5003]`, the exact strict-positive count at the wall is `(2,2,2)`, not `(1,1,0)`. The minimum normalized outgoing arrow of row `5003` to all 17 ring rows is exactly positive and approximately `0.9996256927651311`.

The exact chronology is even stronger:

```text
delta= -1/1024: class=(2, 3, 3); source U=+0.000476259973413; source H=+4.62615122504e-06; replacement U=+1.28820491979e-05
delta=       0: class=(2, 2, 2); source U=+0; source H=+0; replacement U=+1.41652508488e-05
delta=  1/1024: class=(2, 2, 2); source U=-0.000476259973413; source H=-4.62615122504e-06; replacement U=+1.54484393269e-05
delta=    1/64: class=(2, 2, 2); source U=-0.00762015957462; source H=-7.40184196007e-05; replacement U=+3.46946859116e-05
```

At `alpha0-1/1024`, the source and replacement packets coexist strictly, giving `(2,3,3)`. Therefore the replacement packet is born **before** the source residual pair dies. At `alpha0`, source death occurs while the replacement packet remains strict. This directly contradicts both “no other primitive vanishes before `alpha_star`” and “the unchanged parent lattice is already `(1,1,0)` immediately after the wall.”

## Canonical smallest exact counterobject

Take the exact rational parameter

```text
alpha1 = alpha0 + 1/64.
```

Apply the same determinant-one shear to all 18 centred parent supports and the inverse-transpose map to all 18 primal vertices. No inactive or construction-only row remains. Local labels are `0..17`; the genealogical labels are the parent order above.

Exact properties:

```text
active H rows                 18
primal (V,E,F)                (18,34,18)
complexity                    68
Euler                         18-34+18=2
ordinary centroid             (0,0,0) exactly
first moments                 (0,0,0) exactly
volume                        6909113482072353555778602280753180589241446206225332077000695168860590740813970504134248327094369898332364381282926954813770733860611109902684809469118159734571590184552224749428749676400676017462475329746552734038062026999745013904571300791073387874697778114375040881590637665372700067144874174233512767205146624/34300728904104142737194633135168094098840707866993768043809909851446743140549110160659356249755284748948767961731727340829955799420943994441614465136670845481088098480432508553600308087384116040518135801303942364551735815924592093728515878152199574323050136830649256501883168349206320114922423308873636391256465
volume decimal                201.4275994363976
minimum H/nonincident-V gap   0.1284317990637424
class                         (2,2,2)
```

The volume is unchanged from J55 because `det B(alpha1)=1`; it is independently recomputed by the oriented boundary sum.

The source residual polygon and closure saddle are now strictly absent:

```text
residual-polygon margin  -0.007620159574615764
closure-edge minimum     -7.401841960065631e-05
```

The replacement packet remains open:

```text
stable 5003 minimum                    +0.9996462711970805
U[14001,14014,5003] minimum            +3.469468591160563e-05
H[14003,5003] minimum                  +0.2192856338294626
H[14011,5003] minimum                  +0.2212099943149191
```

The complete equilibrium list is

```text
stable:   [2475], [5003]
unstable: [14001,14014,5003], [2475,5000,5003]
saddles:  [14003,5003], [14011,5003].
```

Global strict margins over the exhaustive finite ledgers are

```text
stable positive minimum     +0.07615840918874468
nonstable exclusion maximum -0.03134515169811516
unstable positive minimum   +3.469468591160563e-05
nonunstable exclusion max   -0.006388532202031593
saddle positive minimum     +0.2192856338294626
nonsaddle exclusion max     -7.401841960065631e-05
```

### Maximal dual faces / primal vertices

```text
v00 = [14000,14001,5003]
v01 = [14000,14002,5003]
v02 = [14001,14014,5003]
v03 = [14002,14003,5003]
v04 = [14003,14004,5003]
v05 = [14004,14005,5003]
v06 = [14005,14006,5003]
v07 = [14006,14007,5003]
v08 = [14007,2475,5003]
v09 = [2475,5000,5003]
v10 = [5000,14008,5003]
v11 = [14008,14009,5003]
v12 = [14009,14010,5003]
v13 = [14010,14011,5003]
v14 = [14011,14012,5003]
v15 = [14012,14013,5003]
v16 = [14013,14014,5003]
v17 = [14000,14001,14002,14003,14004,14005,14006,14007,2475,5000,14008,14009,14010,14011,14012,14013,14014]
```

### Oriented maximal primal-face cycles

```text
14000: [17,1,0]
14001: [0,2,17]
14002: [17,3,1]
14003: [17,4,3]
14004: [17,5,4]
14005: [17,6,5]
14006: [17,7,6]
14007: [17,8,7]
2475: [17,9,8]
5000: [17,10,9]
14008: [17,11,10]
14009: [17,12,11]
14010: [17,13,12]
14011: [17,14,13]
14012: [17,15,14]
14013: [17,16,15]
14014: [2,16,17]
5003: [0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,2]
```

### All 34 true edges

```text
(14000,14001) (14000,14002) (14000,5003) (14001,14014) (14001,5003) (14002,14003)
(14002,5003) (14003,14004) (14003,5003) (14004,14005) (14004,5003) (14005,14006)
(14005,5003) (14006,14007) (14006,5003) (14007,2475) (14007,5003) (2475,5000)
(2475,5003) (5000,14008) (5000,5003) (14008,14009) (14008,5003) (14009,14010)
(14009,5003) (14010,14011) (14010,5003) (14011,14012) (14011,5003) (14012,14013)
(14012,5003) (14013,14014) (14013,5003) (14014,5003)
```

The display mesh triangulates only the 17-gonal maximal face. It has 18 vertices, 48 display edges and 32 triangles, while the true mechanics ledger has only 34 edges. The 14 display diagonals are never scored as physical edges.

The full literal exact coordinates are in `body/canonical_postwall_H_exact.tsv` and `body/canonical_postwall_V_exact.tsv`; they are not independent hidden inputs. The compact generator above and `alpha1=alpha0+1/64` regenerate them byte-for-byte.

## Canonical 21-vertex belt-template control

To separate “the incidence template exists” from “the missing winner exists,” the package also instantiates the nine-row formula at the fully printed exact control

```text
alpha=0,
epsilon_0=epsilon_1=epsilon_16=1/16.
```

It retains the 15 nonclosure parent rows, inserts rows `15000..15008` by the published convex-combination formulas, moves old rows `14000,14001,14014` to one half of their old supports, recomputes the exact ordinary centroid, and applies the projective centring gauge.

Fresh rational reconstruction gives

```text
supplied/active/inactive H   27/24/3
primal (V,E,F)               (21,43,24)
mesh (V,E,F_tri)             (21,57,38)
ordinary centroid            (0,0,0) exactly
class                        (1,2,1)
stable                       [2475]
unstable                     lower 20-gon; [5003,2475,5000]
saddle                       [15004,15006]
volume decimal               201.5483556002525
minimum inactive gap         0.4975301884739251
```

Thus the advertised 21/43/24 combinatorial architecture is geometrically real, but this canonical exact instance is not a winner. It is only a control; it does not exclude every missing parameter choice.

## Independent verification

Run from a clean extraction:

```bash
bash run_checks.sh
```

The mandatory checker uses only Python's standard library and `fractions.Fraction`. `verifier/verify_belt_template_control.py` is an optional, slower exact replay of the supplemental 21/43/24 control. It independently:

1. reconstructs J55 from the compact integer generator;
2. enumerates the raw maximal hull from every support triple;
3. computes exact uniform volume and projective own-centering;
4. reproduces parent `(1,2,1)`;
5. derives `n,u,alpha0` rather than reading them from a certificate;
6. proves exact pre-wall coexistence and the wall replacement packet;
7. verifies the determinant-one post-wall H/V object, volume, zero moments, all faces, all 34 true edges, and every face/vertex/four-component edge cone;
8. compares the regenerated exact H/V data to the exported tables;
9. verifies watertight OBJ/STL and that display diagonals are absent from the mechanics ledger;
10. leaves a separate optional exact belt-template verifier for the supplemental 21/43/24 control; the mandatory one-command replay closes the falsification and canonical post-wall body.

Expected markers:


[Encoded source block omitted; the code in this passage is incomplete.]


## Precise scope of the falsification

Proved exactly:

- the parent is authentic and reproducible;
- the recovered text omits four endpoint-defining exact values;
- the advertised shear wall is reproducible;
- its stated post-wall `(1,1,0)` chamber is false;
- a replacement stable/unstable/two-saddle packet is already strict before source death;
- a robust exact post-wall body is `(2,2,2)`;
- the canonical 21/43/24 belt template is real but the printed control is `(1,2,1)`.

Not proved:

- impossibility of every shear value and every positive dyadic belt triple;
- impossibility of a different 21-vertex polyhedral Gömböc;
- falsity of a missing worker-local file whose bytes were never recovered.

The first continuation is therefore forensic, not geometric: recover the literal original source/archive containing `alpha_star` and the three epsilons, then run this package's independent checker architecture on those exact values. Without those bytes, the recovered prose cannot support an accepted `(1,1,0)` object. A fresh search over new parameters would create a new candidate and must not be called reconstruction of the orphan.

## Reproducible artifacts and immutable hashes

- [Complete exact falsification archive](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION.zip) — SHA-256 `70483d3611d8d4d4e34e42c57486505aeb8244261c9b724a1970ac6bab299362`, 2,489,165 bytes.
- [Archive SHA-256 sidecar](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION.zip.sha256).
- [Standalone mathematical report](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION/RESULT.md) — SHA-256 `1a518ad0366c3d47a3e48fff9228e63d138a50bfd198596b95cf30784734614d`.
- [Compact exact source](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION/source/compact_source.json) — SHA-256 `6b517290b553e5654c91c2c52bd3052054023379dfe7890b06b9c9a6ed53b89d`.
- [Independent rational verifier](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION/verifier/verify_exact_falsification.py) — SHA-256 `84418c2dc1d65d8d142e8ede25b53a5b9bc19f3639cf43f6f6b9c44a9c02f6b3`.
- [Exact shear-wall contradiction](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION/certificates/exact_shear_wall_contradiction.json) — SHA-256 `c5565b13fea5e55e3b762ca3d3c5817e63db0a4767746c829807097bf8cb0b33`.
- [Exact shear chronology](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION/certificates/exact_shear_chronology.json) — SHA-256 `dbcdfed5996b23adcef9a8426a491ec3c2ddd342b7d549cba52e0dd74ea57eb5`.
- [Canonical post-wall H data](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION/body/canonical_postwall_H_exact.tsv) — SHA-256 `f3133fcc6849a863ab6fb49fcebf39a569f860790c3e659708b0716213828aa9`.
- [Canonical post-wall V data](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION/body/canonical_postwall_V_exact.tsv) — SHA-256 `2710561abf2506427fcf69adad2d6582abea208fae98b4b0693add3b920e5be3`.
- [Canonical post-wall OBJ](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION/body/canonical_postwall.obj) / [STL](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION/body/canonical_postwall.stl) — SHA-256 `ecfe2c7b8a31ac99555ab96a553c9bfa9ca94f63fc6b0b259af41baddc63addf` / `917d48787bf8144cb82ef1cb757af9fd4ef16c30fa915134f78918fe98a79eb1`.
- [Exact 21-vertex belt-template OBJ](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION/body/belt_template.obj) / [STL](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION/body/belt_template.stl) — SHA-256 `2da4f57dd5caadca2d29aef42452123724887b9e4b5b43508aca66e015487583` / `38afd884038890bafba1edacd581f9a3a6dbbe2ebf4a1a9fdd6641bafd10c569`.
- [SHA-256 manifest](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION/MANIFEST.sha256) — SHA-256 `70f38f8cc1f7708c4438e303403bcdd3eab9e58033e105b1d3230e3592966389`.
- [Clean-extraction replay transcript](sandbox:/mnt/data/Keen_Quartz_73_J56_orphan_EXACT_FALSIFICATION_CLEAN_EXTRACTION.log) — SHA-256 `2518e243dfc30703e569f1d1dd90d93a153d369296c1efde54a9135da38cdb7d`.

## Bottom line for continuation

The orphan cannot be promoted. Its exact endpoint-defining parameters are absent, and its central Stage-A theorem is exactly false: a replacement `S/U/2H` packet is already strict before the residual J55 `U-H` pair dies. The smallest canonical exact successor supported by the available data is therefore the 18-support determinant-one post-wall body above, strict `(2,2,2)`, not the advertised 21-vertex `(1,1,0)` body. Recovering the literal missing archive could still expose a different final belt placement, but it would have to survive a fresh audit and could not restore the false death-before-birth chronology.
