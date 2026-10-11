# figure-0527

Historical AI scientific report · saved 2026-09-24 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# RESERVE finite carrier surgery: exact own211 entrance, not own110

## Result and scope

The strongest new object is **RESERVE19_G5**: 31 vertices, **87 true edges**, 58 maximal triangular facets, `C=174`, actual uniform-volume strict `(S,U,H)=(2,1,1)`, and no additional weak equilibria. It has **no positive P bars and exactly one positive Q bar**, of relative squared-radius depth **0.702484815247952**. The parent depth was 0.8220302331638814, so this is a **14.5427033086% reduction of the single remaining bar without multiplying equilibria**. It does **not** attain own110.

The geometric change releases the protected root, moves 19 material vertices, retains 12 old extreme material points, and is neither an inner nor an outer modification alone. An exact realization uses **13 nontrivial halfspace cuts followed by 19 convex-hull point additions**. The final root addition alone changes an actual-mass own `(10,17,25)` body into own211. This is a finite mass-and-carrier mechanism, not a scan of reference centres.

The accepted fixed-K theorem is used only with its stated scope: it excludes reference110 centres of unchanged K at `cx >= -56057/200000`, together with the retained-p30 inner-centroid bound. It is not an impossibility theorem for changed bodies. No part of that exclusion was re-proved here. :contentReference[oaicite:0]{index=0} The supplied parent is the complete 56-row `H23_CAP_RESERVE31_G5` input, not an inferred 31-row reconstruction from an unavailable archive. :contentReference[oaicite:1]{index=1}

The exact bank contains **45 input names describing 44 different filled bodies, including the unchanged parent**: thus 43 new, nonwinning bodies. `RESERVE19_ADD19` and `RESERVE19_G5` are the one intentional geometric duplicate. All 45 inputs received the primary exact audit and the independent checks described below. Their reports contain 300 positive-bar records, counting the parent and the duplicate input name. These include nonwinning intermediate constructions and arithmetic controls, not just the best endpoint.

## Main exact checkpoints

All four rows below have true `(V,E,F)=(31,87,58)`, strict own211, additional weak000, primitive-zero counts000, P0 and Q1.

| Exact checkpoint | Coordinate denominator | Q depth | Q component/cut sizes | Stable-carrier geometry |
|---|---:|---:|---:|---|
| RESERVE19_G5 | 100000 | 0.702484815247952 | 15 / 17 | Disjoint stable triangles; both avoid U |
| RESERVE19_G6 | 1000000 | 0.702478712590457 | 15 / 17 | Disjoint stable triangles; both avoid U |
| RESERVE9_COARSE_G5 | 100000 | 0.7875256981826589 | 13 / 15 | Disjoint stable triangles; both avoid U |
| RESERVE9_G7 | 10000000 | 0.7867972305647745 | 13 / 15 | Stable triangles share a vertex; one contains U |

G5 and G6 are distinct bodies, not aliases. G5 changes six material-labelled facets relative to the parent; G6 preserves the parent's material-labelled facet sets. G5's largest individual centroid-coordinate denominator has 70 bits; G6's has 85 bits. This is an explicitly defined arithmetic comparison, not a claim of a global arithmetic record.

The supplied FREE_FIRST_G8 and FREE_LIVE_FULLBAR_G8 are two distinct own817 checkpoints, neither of which is a new body in this handoff. :contentReference[oaicite:2]{index=2} The correct supplied recovery authority for the latter is `[internal-source-reference]`; the obsolete unowned capsule identifiers are not dependencies here. :contentReference[oaicite:3]{index=3} The new result is not better than every supplied body on scalar persistence: its merit is the retained **one-bar, own211 census**, modest arithmetic and released material/root geometry.

### Literal RESERVE19_G5 input

The following is the entire exact object. Divide every coordinate by 100000 and take the filled convex hull. Rows are in **parent material order**, not the child's lexicographic hull order.

```json
{"denominator":100000,"name":"RESERVE19_G5","points":[[-95512,1490,25213],[-93489,-4976,45789],[-92617,4591,3048],[-91581,10889,57855],[-92503,-18354,31893],[-88115,-30823,18411],[-85118,19369,72156],[-85037,249,-17306],[-79844,-41955,3163],[-74081,5495,-34866],[-75675,21835,87226],[-64356,-50158,-16879],[-61439,-786,-47925],[-62612,28981,100926],[-48064,-55390,-29772],[-47540,36950,111237],[-38556,897,-61657],[-35827,-69532,-8621],[-29705,-57450,-39772],[-26030,44260,121341],[-13440,-56712,-43998],[-6835,-59359,-43333],[8211,-70177,-5651],[-131,51942,126843],[6953,-17009,-58925],[16594,-41467,-52532],[29213,59427,125808],[67453,43323,-29552],[60560,66035,116440],[96923,71736,93873],[164413,75778,13047]]}
```

The material-to-canonical vertex permutation is

```text
[0,1,2,4,3,5,6,7,8,10,9,11,13,12,14,15,16,17,18,19,20,21,24,22,23,25,26,28,27,29,30]
```

Canonical facets are sorted by their sorted vertex sets, with the outward cyclic order retained inside each facet. In this convention:

```text
S = [face 30, face 54]
S carrier triangles = [[10,29,28],[24,27,26]]
U = [vertex 30]
H = [[25,30]]
additional weak = [0,0,0]
primitive zero = [0,0,0]
```

The 58 complete maximal facets and 87 complete true edges are reconstructed exhaustively by the capsule, not assumed from a floating triangulation.

### Actual homogeneous mass

For density one:

```text
Volume = 2845806044895161 / 2000000000000000

First moment = (
  44630574135387532829 / 400000000000000000000,
  36460091282788126867 / 480000000000000000000,
  138188845239834060673 / 600000000000000000000
)

Centroid = (
  44630574135387532829 / 569161208979032200000,
  36460091282788126867 / 682993450774838640000,
  138188845239834060673 / 853741813468548300000
)
          ≈ (0.07841464497456944,
             0.05338278316054874,
             0.16186257140013550)
```

Relative to the parent's actual centroid, the displacement is approximately `(-0.000138013047208288, +0.000330068396967330, +0.000163859405393438)`, while volume increases by **13.5407437116%**. Thus the persistence reduction is principally a changed-geometry result, not relocation to the old reference110 point. The centroid is close to the old actual centroid but is **not held exactly fixed**.

The new unstable root is `(164413,75778,13047)/100000`, not the old root `(174422,57073,13918)/100000`. Two exact noncontainment witnesses, with integer coordinates `X=100000*x`, are:

```text
New-body facet 51:
(2353478467,-312759728,-4745716147) dot X <= 301324789956578.
The old root violates it by 25272617924406.

Parent facet 16:
(-1358623194,5381182391,-832703864) dot X <= 159786830747387.
The new root violates it by 13748805969081.
```

Therefore the old protected material point is genuinely removed, new material lies outside K, and neither containment direction holds.

### Complete positive landscape of the main checkpoint

P has no positive bars. Q has exactly the following positive bar:

```text
peak = 54
elder = 30
component = [5,11,14,15,16,33,37,38,46,49,50,53,54,55,56]
cut = [[0,5],[5,6],[4,11],[13,14],[14,22],[15,17],
       [19,33],[25,38],[37,44],[46,47],[44,49],[48,49],
       [47,50],[51,53],[28,54],[29,55],[56,57]]
attaining_edge = [51,53]
attaining_path = [54,55,56,53,51,52,42,26,30]
birth = 38376815697493640801/67805075027761636247420475520692915666105242349636447136718025
death = 39897452027/236935038091077657069954769323765300529756722294562102
relative_depth = 6387562560992667172103985579469132597289853270456906655975608375311837027/9092812289099922747476468304053506045877043927034735566503537287975523702
```

These birth/death values use the auditor's explicitly scaled coordinates. For integer hull vertices `I`, let `W=sum det(Ia,Ib,Ic)` and `T=sum det(Ia,Ib,Ic)*(Ia+Ib+Ic)` over the outward maximal triangles. The auditor uses `Y_i=4*W*I_i-T` and `Q_f=n_f/(n_f dot Y_a)`. Actual centred primal coordinates are `Y/(4*W*D)`, and the actual polar is `(4*W*D)*Q`. Scaling changes absolute birth/death values but not any component, cut, attaining path or relative depth. No scaled reference centre is substituted for actual mass.

## A finite 13-cut / 19-addition construction

The retained parent material labels are

```text
[0,1,2,3,6,7,11,12,14,16,18,20].
```

Their convex hull, `RESERVE19_CORE12`, has `(V,E,F)=(12,30,20)`, own `(5,3,6)`, P2/Q4 and additional weak000. Its volume is `356261528864761/3000000000000000`.

Intersect K with the core's maximal halfspaces. Seven of the 20 core halfspaces already contain all of K; the **13 nontrivial cuts** have core-facet indices

```text
[1,3,4,5,7,8,9,10,11,12,13,15,18].
```

The exact integer coefficients of all 20 planes are generated in `FINITE_MASS_LEDGER.json`. Then add, in ascending order, the new points with parent material labels

```text
[4,5,8,9,10,13,15,17,19,21,22,23,24,25,26,27,28,29,30].
```

Each addition means taking a filled convex hull, with the same uniform density. Every addition preserves all existing extreme vertices and adds one new extreme vertex. After addition j the true counts are `(12+j,30+3*j,20+2*j)`, for `0<=j<=19`.

For an outward current triangle `(a,b,c)`, put `w=(b-a) cross (c-a)`. A newly added point p contributes exactly

```text
deltaV_triangle = (w dot (p-a))/6

deltaM_triangle = deltaV_triangle * (p+a+b+c)/4
```

when that face is strictly visible, and zero otherwise. The program sums these visible tetrahedra, then separately recomputes the entire new hull's mass and checks equality. This supplies an actual-volume, actual-first-moment ledger at **every one of the 19 addition steps**.

The aggregate exact mass accounting is:

```text
Removed volume = 6806732018116159/6000000000000000
Added volume   = 7824895076955961/6000000000000000

Removed first moment = (
  102671216205890743723/600000000000000000000,
  202406086721553612811/2400000000000000000000,
  169068091287070103877/800000000000000000000
)
Added first moment = (
  2211026603076596623/12000000000000000000,
  225139785226113219443/2400000000000000000000,
  191206036816959100011/800000000000000000000
)
```

The program verifies `Vnew=Vparent-Vremoved+Vadded` and the corresponding three first-moment identities exactly. This is a constructive decomposition, not a minimum-material-transfer claim: it deliberately removes and later refills substantial overlapping material.

The **terminal root-completion step** is particularly useful. Before it, `RESERVE19_ADD18` has `(30,84,56)`, own `(10,17,25)`, P16/Q9, additional weak000. Adding the new root sees exactly its facets `[51,52,55]`, adds volume `60120538303589/250000000000000`, and gives the own211 endpoint. Thus a finite insertion over only three currently visible facets eliminates 16 positive P bars and eight positive Q bars through coupled geometry and actual-mass change. Whole-basin visibility is not necessary for that observed disappearance.

The core and all 19 completed addition bodies have full primary and independent audits, including all positive P/Q components, cuts and paths. The 13 successive **partial-cut** bodies were not mechanically audited; only their precisely defined common endpoint, the core, is used in the mass ledger. There is no claim that the construction stays own211 along its intermediate stages.

## Useful failures and arithmetic controls

**Straight interpolation is not a certified own211 path.** The exact material-wise midpoint of K and RESERVE19_G5 has true `(31,87,58)`, own `(2,10,10)`, P9/Q1 and additional weak000. Its single Q depth is `0.7629897040429378`; its smallest positive P depth is about `3.231855925082381e-9`. The analogous exact midpoint for RESERVE9_G7 is own233, with two positive P depths about `2.7079845302401505e-6` and `1.8633359030239337e-6`. These are exact positive bars, not tolerances to discard.

**Coarse rounding changes the census.** The direct 1e-4 freeze of the nineteen-carrier numerical endpoint, RESERVE19_G4, is own `(4,7,9)`, P6/Q3. Its Q depths include approximately `1.037335891393556e-8`, `4.990429643974315e-8`, and `0.7024663009537327`. RESERVE9_COARSE_G4 is own323, P1/Q2. The full bank preserves all tested fine/coarse freezes, not a denominator-minimality claim.

**Covering a whole Q packet does not cancel its equilibria.** For RESERVE9_G7, the exact point `(2,-3/5,2)` sees exactly all 13 faces of its positive Q component and none of the 45 complementary facets, with no zero visibility tests. The resulting body is `(32,90,60)`, own `(6,6,10)`, P5/Q5, additional weak000. The parent control using `(2,-9/10,2)` sees its whole 15-face Q packet and gives own `(10,5,13)`, not own110. Both exact bodies, their full landscapes, and the max-margin LP nomination code are included. These are finite failed constructions, not exclusions of all additions.

## Producing method and verification status

The numerical construction moves a selected block of actual material vertices, including the old root, and recomputes filled-volume mass at every objective/constraint evaluation. It uses the supplied actual-moment/full-bar modules as complete source dependencies. :contentReference[oaicite:4]{index=4} The new `Surgery` subclass protects physical U1 and deliberately keeps both current stable carriers while forcing other faces outside their stable regions. It minimizes the sum of `log(birth/death)` over positive Q bars. Consequently this run is a **better-own211-entrance search**, not an own110 search: keeping both S guards prevents an own110 endpoint until the junior guard is released.

Numerical acceptance tolerances and even successful SLSQP status are not exact certificates. The rounded bodies were re-hulled exhaustively, which is why actual facet changes and coarse failures appear in the reports.

Exact verification used one exhaustive integer point-triple hull enumeration, an inverse halfspace vertex/edge crosscheck, and two different equilibrium computations. The second computation checks face feet by barycentric projection, U by all-other-vertex inequalities rather than only neighbour inequalities, and every mixed edge by **both the primal-edge and polar-edge foot parameters**. It verifies the exact reciprocal-foot identity and all closed boundary inequalities. Three different tetrahedral origins independently reproduce volume and all three first moments. Complete-chord bottleneck domination and equality of all-pair versus true-edge bar birth/death multisets are checked, together with every reported death cut and attaining path. This is not a claim of two unrelated black-box hull implementations.

All 45 reports have `additional_weak=[0,0,0]` and `primitive_zero=[0,0,0]`. In the report schema, `weak` is the **inclusive closed census**, so the main body's `weak=[2,1,1]` is consistent with additional weak000.

## Recovery, commands and hashes

The literal executable capsule below contains 44 complete source/input units: the full 56-row parent, all 25 base input files, both exact audit routes, the finite mass constructor, every producing numerical source module, and five numerical pins retaining complete coordinates and solver metadata. Only redundant floating landscapes and iteration histories were removed from those pins. All 21 direct numerical freezes were regenerated and byte-matched. The three exact midpoint inputs are also regenerated and checked.

Exact reconstruction requires **Python 3.13.5 and its standard library only**. Numerical reproduction uses **NumPy 2.3.5, SciPy 1.17.0 and PyTorch 2.10.0+cpu**, with `OPENBLAS_NUM_THREADS=1` and `OMP_NUM_THREADS=1`; the supplied modules set one torch thread and float64. The exact literal inputs, not future floating optimizer convergence, define the accepted objects.

Save the literal program as `RECOVER_RESERVE_FINITE_V1.py` and run:

```bash
python -B -S RECOVER_RESERVE_FINITE_V1.py RESERVE_FINITE
python -B -S RESERVE_FINITE/REPLAY_RESERVE_FINITE.py bank 0 14
python -B -S RESERVE_FINITE/REPLAY_RESERVE_FINITE.py bank 14 25
python -B -S RESERVE_FINITE/REPLAY_RESERVE_FINITE.py mechanism
python -B -S RESERVE_FINITE/REPLAY_RESERVE_FINITE.py check
```

The phased cold replay completed. Its terminal markers were:

```text
FINITE_13_CUT_19_ADD_MASS_PASS 13 19 [2, 1, 1] 2845806044895161/2000000000000000
FINITE_TWENTY_STAGES_INDEPENDENT_PASS 20 206
RESERVE_FINITE_45_INPUTS_44_BODIES_300_BARS_PASS 137 325756 98dac55c0b19ac763cd52649d578712662201834a208e60eee2d4e9f6da153b3
```

The last digest covers a deterministic 137-file stream: each sorted filename, a newline, and its file bytes. `MANIFEST.json` gives every individual byte count and SHA-256. Complete maximal facets, true edges, actual mass, strict/closed censuses and every positive landscape are in the generated `*_AUDIT.json`; independent receipts are in `*_INDEPENDENT.json`.

Important identities:

```text
Full parent input: 1339 bytes
4b1bed14b6174e65850f72f54a597e0dc284c3cf65fa3962d75a27c796017d5f

RESERVE19_G5.json: 715 bytes
7b27a2242e8418bcdabfab0257f0e6542dbc751db2cad736866ee6c761a4d74b
RESERVE19_G6.json: 809 bytes
ab99ca30370f8f2321672ce058629f085fee4c394190e96a52c41c0d43e223eb
RESERVE9_COARSE_G5.json: 726 bytes
91617bb8b7a3c84c171bb9043364892d955fd2dc84a2582cfc663d25ee4424bd
RESERVE9_G7.json: 907 bytes
5f519984fca1c1e0d74380c3f115fce5e7264af4db2b0e005017e72d17964d55

RESERVE19_G5_AUDIT.json: 3214 bytes
c970df2709b331e9dd3ba295f98527115e1b9c40d4ad92ab915deda513a7bf04
FINITE_MASS_LEDGER.json: 16514 bytes
087badbabd51d22a1f1855ffb23f86ac249f48fef62c276996c0e2f8d8b062eb

Recovery dictionary: 73054 bytes
fa30f9bf3b18c0f76c912ac5205934ac5c77510d9084262a5182c73e3c589e6f
Standalone recovery program: 28725 bytes
6b4e1675f8e2e48584aeef21a811880b12c36f7a7e727f65e851bdac207522c3
```

The numerical producing commands, from the recovered directory, were:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MAXITER=160 OUT=SURGERY9.json python carrier_surgery.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 EPS=0.00003 GAP=0.000001 MAXITER=90 OUT=SURGERY9_ROBUST.json python carrier_surgery.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 EPS=0.0002 GAP=0.000003 MAXITER=90 OUT=SURGERY9_COARSE.json python carrier_surgery.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 EPS=0.0001 GAP=0.000001 MAXITER=65 IDS=4,5,8,9,10,13,15,17,19,21,22,23,24,25,26,27,28,29,30 OUT=SURGERY19.json python carrier_surgery.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 ALL=1 EPS=0.00005 GAP=0.0000001 MAXITER=70 OUT=SURGERY31_STAGE2.json python carrier_surgery.py SURGERY19.json
python freeze_pins.py
python cover_scout.py
```

Observed SLSQP iteration counts were 45, 30, 31 and 61 for the first four runs, respectively. The code contains all other parameters, including the coordinate bounds, regularization, witness construction and exact best-feasible selection rule. The later 70-iteration all-31-variable continuation retained the nineteen-carrier best point; lower-objective trial iterates were infeasible. That finite failure is not a body-family exclusion.

## Most useful continuation

Start from **the exact RESERVE19_G6 or the simpler RESERVE19_G5**, not an old reference centre. The new constructive question is whether the terminal root-completion mechanism can be coupled with finite motion/removal of the current junior stable carrier and the saddle carrier, while retaining the elder stable carrier and actual U1. For G5 these are junior face 54, saddle edge `[25,30]`, and elder face 30; the relevant current landscape is the **15/17 packet listed above**, not the parent's 15/15 packet.

A continuation must explicitly **release the junior-S guard** in the producing program; otherwise it is still constrained to S>=2. The released material/root, the exact 30-vertex pre-root body, its three-face visibility disk, and the full finite moment ledger provide concrete geometry for that step. Endpoint audits must still test every small positive bar and all closed weak cases. None of the finite trials above establishes that such a coupled cancellation is impossible, and no own110 endpoint has been verified here.

Convenience copies are the [standalone recovery program](sandbox:/mnt/data/RECOVER_RESERVE_FINITE_V1.py) and [expanded sources and exact reports](sandbox:/mnt/data/RESERVE_FINITE_V1.zip). The complete literal recovery program follows; no download or external library is required to reconstruct the exact results.

## Complete executable recovery capsule

```python
"""Self-contained exact RESERVE finite carrier-surgery recovery, version 1.
Python 3.13.5 standard library. Run: python -B -S RECOVER_RESERVE_FINITE_V1.py OUT
Then: python -B -S OUT/REPLAY_RESERVE_FINITE.py all
The compressed literal contains every exact input, both audit routes, finite
mass constructor, complete producing numerical sources and retained pins.
"""
import base64,hashlib,json,sys,zlib
from pathlib import Path
PAYLOAD = """
c-rl~33nPvwl4Zt=(?*PASF0wKvdQ`E?cg0-x_2|ZdX0bVkM9WYy_A=gX`6Qf8X9aA~KRemfgd-
w~xEp2qGgQW7zxKLqzQO<D2iFUYzz`{&M#E@}mB3HJ^QR@=fRMH|M7pr{{k^^;*3jLQa1BjZ;XC_NVrKe);_D*O$Ls?tL8ZO>OL?
2A;I&;Dg?qAAkMn^i}WKuYW&1-^tZN`qOiCYfszrXVF8?4)-I^6z_TVgXiu|_4lPV_9i~`YCQc!&wps{Nj(4c`_~tj`-
ek6iyn9uKk#f{CobLn^<8=g()|PJL7v`yJNw4@=JdC-
(`T2b&wCe_=ciA9))f24+iymbX|{U%&50K@P{nGT`caIZZ@+0Zhv^`S25#SLrGrKs42F>(hpl1MXf`}Qj(y+tnn9TQZZnJBEX(|1
n6*anF!iFKA8?aa>t&W+_xks1eo5d*jVS(;n{<A9_S4hfd#cgB7cYN#d3jo2+@o1<`M+oL>9DlS7Sr^;G#{1L<E%8A%qHusq{@`~
%XBsvJEgPx^>{uj1$8f|N2S#|oek6Fur!?@!}7lVcJ^$3eT~G`NhzI9+ogUwdtbV^e0qL~&tK2lrR!`kPG^(Vb-OeeXM^|k(l49q
Y&jXEQ{95esx)7$C-Yf4MTOGBx3kf5eqCCm>oML{np`jD%XR4tKh=}bG96Hvm45a@C6v-
t>HO_XrH<1TRp8L9IIH`WGhe9+vODDOE#}jET|>GVPS)z_4VpN*@2OEy86?peq_g>qI`DRO{_C%o3AL)y>(O-
gde!<OU1l@X^L94OMm!)DjN5XZxXx-
lUnIZGXIb^+?W{CQud`J`EvrxG>2Ou4P<2nr+xS<m)-lz?-a5NmSE^N%9L<+px-?O>bodP?RDYMME-ezSiypT7$wDe%TB%gq%k<W
MZNJ)16YhKkPw=Btp3D}Tbx%mP+)dOd)+GT2>f`KgIJwGJXb`<lT3%VySL^KhxZHdC`uWRC)%a@tc8Nih=9{srq*XK|ks+n`I%&1
NUCqm1o}Zqb;^UW3RJP<{DJ_<h*}9?!(3I_+J-xUnJ5sHK?tynEgLS#<jHa8_IJsPIvZ|gi-
7OkM=HR5$RYSg@@m_%vvLUy$el?x<D`mwqN4kkT0h3Xw%!t@~@zbwQFUwSPQK$Jh8O&$v$!wERwmW+w7Tfd8wJhf7)QT&(D^V-
BmU;%JyPbgYile<h$L>I$aNp|bVu5UxMOF9qI4O063<WlNKV$5AKb=1RL4kYODLe-
1y?%E2`utQLcH2@fjZ)=(cAres>;5n;El#9S^d3;rHbqt2>-
jpJCT<&GG8th4l0W{mN1bcsf!(3z#UvYKiRtrTKFliB<9_+=+gbUz-^Ls2o5e6)XBEz=UUi&IvzboOFYQPz-
K0Yg`&H*b!Y8sAW~;$+vRKcT$q*z}5sIPG{H^NPFrDz59jPp#hFP`I$Skw<W@%UI=$2{fWDFJJ%<dN10HnAFLH5a{Efi@Fo$Exuy
Pd99831mWB)V3oGIaEJYMQF~=cm8Cd~tfAsc1hpUZeV}Y<``A&Cu&rMz0vmH?wupPnWC2-
GVU1QrCuaX7hFFAtEoZP`Wz+OligL^6QTiuT3qG$p;Xe_2_50TRm0@uXF;{ocE!g4u_TXW--mw=XvFZfMl4>=GT*1im5^w?$ix)d
Nn6qWK%5M6{c2$jdavH5y98H&C>Tk+N9$;_^(@nOy!cx$u+XvWWA5sa&BdKJJa=4xN8n|Aa8Khp?*}8q!LC>7&?LL(z_Kv7Bz!j7
%6en3&Y;`zdnC?deK9H-uKWd6?P6gWhQ7~=8*Bz5VcBCqGBJSUZ<0pknDU_AB=~SCC?Jr4y>9$DA&{F)lJ9i($rHobW-
&@uar$!S*Z-&qKxu*PGx9RE1c$(Nxp(0Sj<x2Om#lyW2Zh}>T{h!)?i=OK(ey5-
v4T&+LVQGS#elqSJ^CE0&aTOlc7w!)*omfNIlUHOd(M-dZxmi0{Vd|ff?8g02bMnilR%H=Tt(!4_s(!!grIWa-f3@HpFcLI#8-
crCyJitJh1Ca<4~k>-EYfGQ&#u+%nTd7q%FMG-
4P3gAPkou|{l{V(nH24$nHBS}Te?#|vAIANgL_K|+8ZwXoH6!l=>W6hHRyqXjyT__r4|9nWpH9H`W><cM6S2CX`B0<X!1noZAhYJ
uDI9j_U3&CSTej}{d6hVR9a;)ZxJiZ%ky(r7h9yxeQWsED&PLbvHe)TAJ6HaI1U8;*~cIn9P2P)ZyIu~Um&51(G#Y;u|h#zcLnt<
my1#g9G5Z?>rIZi@?sO_vHr0kZk623H?8B5-
uviX6}L{E(7@W)wRu^f2~fZd4HA?KR}VXEWy7Q5+ef1`weZsH*(f4S)}R?0CKxa8>w&W}ycdoG^4<ZW#4BYEd7;AfSddeLQZ!Orf
lilyf4l6`~^KMgp}Dqvj%C)a1^1aYUW<!UmH3h?4vk>WNxmfMQXT1~{hn;UzxxH=>$j7k!Ik%!B8}AywUqTfWoq8llq)c*H5)a~h
az$0HKx{<%$z(Zj@eh#I54)aVmAx=fFOBFH9FWFsb$Y-
*bH8bp*Hs4{G7vh;{9g)pN?Q)VEf88U4Knm8k&&Vb2N(<eq81RA%9LL*J0AXuLW5Jc+6no5OCBO>@X(1hv{rAADuLMTM55ff`f)a
u8ITqB`Z@DUNLuo)<p=nyO=G#hE6^_gltCR?e2=r$C>b%k<$O}Z}AuFJ$5G!*sXb<I|T={IU90`?n1!9J6)r)fA6B6fv}eNDzL)3
Gar>}g7Ng_M0F+*V8Yj=D<J%+weddKQ9iG?=1Q1s>D1FGL*(RR>JgZj0%f$AAc%M>~uaY5R({10rtpgQ(kWD)J7Pz5^j}Us1SABp
yUU<E|p|fT$c?M`RvoIuD4@h0?>uK2k6GYlP<a61U07R9<8YU$ccx{9em*ec)lM={f*LnQE^Yx6qtgs}=bUNW9UM)W{FOpdR2gc3
UbZND;K+ar2SWb0rz0OC*K#7KTCkk3kMyAU}u^BjW^-
7pY{|$B@v7ppq~QJYOZd00fc>AnsTtMh!Pc&CRgs5hD9i1DMyvoOle!Kx4n9k^!EmxCw^vK;A9M?KhczK-&T34}wM{J@oN}*duD-
aVu)7_W9^7_&WwEJHCs|OwTPei86a`qe(>BiWtg3*`R*RC<{0cM3XCNG(19?29XuGB=AC^T#u;V3j#NwZn{y(;|dz{NV;*yNTjH`
L+}^4x`nv}KH$9y^P5f19fX+68hBgHPS~Qc0{=8xG-
d%nfoQG~#?*bk70}qCF$`vCAKvMKWT|qDGYdnn#p4~IQ_>(epk%a^@T3KxqGW;<>Lxxz!U13c)e*!js4##rh^7%XSWq-
V7QEmfAK-
&QjG9dcq!qEu^idZ{kD%FVksNQJ7xY5RA~92d>=3DOE8Zs*;!g;LLsB8$FBM!zCV=IFYXpNUlED?x;2PQBvT$%&I=DtWxFR215fH
AC5L!e8A|rewBwQsWTox0e|FE2JMNqgRDO@8eh!&_(EG%3jEnFooe3loX5g05nly(E&)G{L!4JV9QY6xbt*l?BHaFyV2jpT4ybht
`(xLSBXqOtS{mG}sa{BV^3(GtWpB7|i~*lLLoQ7R8f5tqb>tK^8Q1xegglEf2HV)UU%X+*A;Caw}EK3IU|iKhgL(T!X!Qd}idTrE
^Qkt$84C26?=s1d=!YE|Smm1q%t$yXW^V-VWt$0A;+7M3r*5-
^bQB4I)iG0bl)V_Xq3u97l=7Bjxc8Kp^a*I3eoB5GVEYkVziB9=CgiX?87V1v9ti&)@<EOFv}BB${wMmoevjRTydSV{Ae#Y~!;G&
@=Rq!>zZl*Lk-r!-SpT;*xDiWFaknz2NZFlYISwJhG!%%!=@VlUw@!(fKP7(SWBK=I6De$Hfy%UsQ7Ue0HpVl-
bkO|)%cHN$I$*(`2T>}L2aXSjyuxJa{{m-C!qI>U9E?Lh3Y@LjW^7%#FoPgu|JUe0`E;xPA-DZ}iS>vFDPK*NC+3kHe@wN|GT1Li
`*hK3IfBf3q+iIHYSzoB?BjubNnqUX7y*%CWyevC9jDt!;&rdTqH6i<3B&6IIdbERR+Nbx25rx;UnChJSWno0-
sU13hI)zI7tN)+}~_6{1W88lQJ3IQlAn)4|1bYW6Yap|_aE39BXXa`*_Cqw*>Y?l4e4|>m@p7rv|9%~xyv4UuEixi0vb~XAGHiUQ
ByoBJ!%y@AlXdSd|LR9Ji(8ziZTFSNoYmk!fH(6P6!{D&Nf;vOeQCyUWph_JwL7+a72nw2HyrXdQ0n;e(ebNPE%p0Eio_f~-
GYAqZCga1W=Aj+L4@6c(wm$XCYs4*W29ZsH31u9QmBAFU{T;?^<$;%l4S{13!6PZzAk>%}45Dum0gEJvVwiuN++d;ZMJ=$WkA8>|
4}PT@L5EP=n=;@L(IRo3%c@;uiO(HV41DU5sseFEy#ZE=;Yy|yz$YZO0}!gW?KRLmm$agq4|9NQEKN2b8loE14h@uPCWgTb-
5DgqGSveuP&EMhfJQ;ed11pPqatP~Xs}-9HwbXSG-
x9LhCLBrD%1~*LC2wtvjK?g=$qdPiGHBDvnwf%BXTssJb;oP$Y_G0eWZD;P=gSdCSs_h<a}*4P;W~FY9k~NgyixGNdb+N2C!_xaB
(Ru47e|_3Sfu=bIE-
7#mfanJS2*3xD8TxTVC_9?_r;#VXyO`fgT`dgA{St38H*Oz))~qBPJCZ3VrMei!?!ALDOTk3lfPLhvXRdk~DdrY&A9xFpwC=C}K0
!W8>9tl0}cfqvm6fBK8u6BpzZwSwNL~qV52|fQ&K5jBH;tL}aK>G=<kg_lzMIIk8DYRD+!b)&;b-1PsU-
0a^jAI_O&1?E<Qn^UZ8HnO!lU^?`fKd+=syG8<;J2$s#(rCF9Pv(>t^o@A@qdS1(JGT8vIns1f^fkF!g)kc85IJ>(o;<KDjd#m}1
xL*<XE8>1d-
2WR8ms~T9ZM7EvkzZR%>Gr<3&si+8%KnR%jCgf}K$9?2O(;3!K>i^CX8718qlN}b#z{`{$RFfUWeqWEh%A^Ym?$2<W(3NKiEu)pn
?q|xL`t9}@=*~X?O!wUeF0QY@bu84kw;WY^vC4aIJ9WgBv=9fg@Qjqq=fbX`OX2lEk(CPwy{txkxfLf8_0?ir!-
nzD~%SgiH6jtOi}2Psn!&SM+g)V-
wW(Uj}am!#|UgC4}yx`)p9ZakVPK5Efs^Kd$4F}1q8Eqh&sPu^~fsxZ&*Y6ECK)6HKe@)z5)3a6X_B`pvveVrhU#L(ti9qB+K{0;
@(B1{W`*dRiwSZdT14CuY4r}_k_X&A#wL0HnTQGbgl^96H51))XBY1w62NWWoi$Y+}W2w^d2$6M@;c<OOZS+r(&d;=y~OVs6HUFr
zH=UN+_p3F#{++WYYHz)Ba<YllEo*?_N}L1J*#GXAz6LE%D$sye2Kz#0_$!La$L3f7YT>7}BIQp;M6ZAxcWk3*!j<(qg@*;RR}uh
{l-
&h}#qgz2E$zMJ2E=@DD0Dx$nIIg#FN>Qlr6s|Cn5k<Q{Lv4=gH$yfy><z!d^luROG<6!=tkvqg(YpiH$Cad1&7_GR@bY&KYOHP|Z
;jPN<x4?HCw82f!%`2m%Bw00K5YG7gwV=^DYz^5f~G{|rA(vQbgwt$SJq`1Dzm>!`Cytqf&9n_haw-tCERGW|#970)ez7j}HpXS8
}8-s*GU>u8u7Wv_5^$6-
epfZ*n6a;cULj$G(yhpynLtOJEOG{SifAazpi4RxF4_5?;Yb1!PM2IUg#Ql;5CK4sCk|nMP6W2(SfW!%{^|3t31&S*YMTr#m%T}0
JvbZ8zTqRrFhgX<bzPKV_l)e<W53MkflyQ}qah05LA6{Z&S>uYZ(bC3!c!`N5j;lnDt7MK6FJ#V$)Df}MY(-
k`xFUF5C3##WdO{_80wsJxC4C|hKMgH^d=Wq%`Lam@X%XZr83c`iL`v8cDa2gGVki(f6e>aFX-Ooa2pB1{DAd9T#urN?SH#h-
rJxV8JhaMmh_6ug&_a`I)|#y4CbzKS<mQV`Zocm17M7k|v-
;$k1t_<$2Ic0<P;R~wrSmWc%A14>r5@%)ok_S+G6_dYrOcIiCSIO$^A##LU!-
yi>r}2@s&cK>DwRbzR&|}ZR^=kjHJJ#D8xiUAA!rDeRLm9)rZt8DZ{(aT?O|@_ufox~9<`X|TI*S^wWQ@1R<&HSu;p57TPlxmyY!
4XUJW~Qz0Rc8xm;_h%U<nLxda7d8W;(rDnWxhQ>0tYi(js_{-v`pI;ba%5bAB7-
Eg%S=347v_L7*&C8#09#>gRU67(>cWO>Y9A#<%oGS|(~M74?$MZb?wMP<VD#!!?(npM2H#cOh;wPMm^khrnnR84|3(k4M0RT0QGX
vTran8*c*HfT`|{6edqLMhEwNIDtW3NU<q5Ek3)psomJYm@C1S^|T>_FECqD0HFFkbwY1LibT4%ZM174aO{LGBVLZZZjke%WcH0t
}sGDqXVjuZi#-7=0-
{(?R@dv7Ql|JMTmJ&b_~lQ#xS}~(mOy(P+7tT?JHsAqOtZoS{RKnx)>6djjL9RmIU2>DCR!~#SY?_{{W8JNLIkIZ8R(3Spm_uG0j
Fb8`rjxt$=L>blb+aBEl6gZX4x_I9EWrZLBMxT><a55zoTBBI<49UJ>~U*tdm#%~oLWFCaTSM?kUda||q?U;ziWk+6t`MKs*TLmL
r`n7ECK1zap5<2E)H(Xoh++Xz{}$RbK^<D`X@MXcOL%OYMD5px?ei>O(|&28i?U}q6MxAC)xphXPbLeV0Q7Ll}wr9lx*851?0He1
aCq82c<h^jWO`n)GSM^;{T(AXL`3+PJwPIG*vy-
5aPqgD}PT^nWHW{$JyT5KaN)J+R(y_Su(Y*6KR8@6)9^<=lM##~m64eHWLL5{m*`sB#V3Ve>ev}etrZvz4<$KN2>Mc^;mtn}Z!S4
rU0Ag2aR3oi{+YLxu)y-
EUs2K_YfS(qnq=V_$#Es)drrlIX0*{q~+OGB1Ht50rLQplu1$>7l^HY*AC7}zn0^U2*x3SBg?7)<%(ZY9AF104o6a=_475onmmEj
t4a1{Vw@Xf!ZD5E%?G?5{cB%b8yDyJq#A%LB#Wk>>5duyw3BIyTI#`54BhVqwF*IpZ3h)$F>5Qy=GgwDKMFIUevj5^*u0i|0|z82
cW1=?aKNq)h%t{fs=2oYtgA<b~8v$PY;sk|&ahj(m}><&EUYk69{+M^ZgxpCpq(gHcQTlCHJgooTrdaJB56G!I=a5Vp9z?4wkV*h
@)??5AXEcAL7bA=Fyh=FZ#7=->l-(-
1xuk0oP_%OfLROV`>AFPK1{OTnE+WFC|Ek{?IXBlcjrmJgGLn!K2<_G2o9i}@Yem+5M6riLU|?Zl%=CE2Ix=3C_%ci5GpJewMLgx
8gKQ<%>*h&`OH@o^e2r$z&LCwn?w?d#OL6D3XgJ9(7J<EhcWSGdVuPpP-jkhl771N6ZTS0CSa;oJ=)S%qZ(Cj%XMK<TCI0~I^~HO
VmvjB(7)V_<O{wWJ`(iFlhf3^$0kLEV5$X6^`YBIi1W78FGLN$G$~*pPK&j1UBdgMYva-
ryLA9<w)OE8v#ThCx$lfWdu|{JuDsT6hg{xCiwE%_cU6ICPoCiF|3FC#^a|lH*|zv^;-5kAKESnS-MF5!+<G%IU9i`m3D&XUJ*2w
SxylTb0@<*<tYJr~MuKnYww<)uG)S#>HW~H;ik;xHW8-hIVIYSBCAzFfI(^zOY>vx!c0HENpj0?y4|u3fo0t+!Mw%VY?-
iOConi*sh4&4Pjgmw);W39%AEmXxT0Y<8Cmn2HVY$yBKo!g6&$+ZiU>XV7n8HD<O9y*e-
<JeUQ5jY`1}N8RYH)+f|_41i6dAb`RvPf!r-%y99D~K<)~#-
2lb~kemOu>7SeZxyf&t`?;x~oB25sL<R~h)7~=cjY*%I^SLQ+%=o4;;adh0qTF;hW_v3~g+RlCmz(OjnI0PxJvYyDY;d(%-
ZJRmTjsbi#SK8%2;my@+nC-vI8coE^?4h;Oxgb%H+s<q9*-
9{o5BB_jb5P$#3pk<xObx$?f4;TSF(?(++zxtjb7r6Lf@h=5a*Mk=BC={1uFK1g2|1~c|3ksi|IL{wR;#(+F8^hDh)|e#RsYLi#B
?h!vA3#y^w)O*A?0gzi#xhH+qGUqHv!{oOg-u-RKqYP9CCj+33Z%3QAX`?h2Aeir7P@_DIOxQ}pgK!Mj57o{+rPVw#VH=mXi#E<h
a!O1Jb16=sYm-)GWy57PdZZCNp;|L1I3@fv{7P;7VNj3EBHW#x0XtjMM_<{#0Lg7~2=E5t;ea1mh&u@TE);-
f$@lIA2|v67M;VM{SnsJY1#c2fN0wlqVz%u%6|BfL?Mcq(cNQ)#Zs*(wme@`$k_pv581`oa|lQ~aw#LvfwQZ0ARs@4h-
T{xuGbC{l}*?2T0H8GOQ_K`a_*9`!VnhMG%x2WQM@$c0b&Gz~Lqv#B^$%e^q?)le~Oq`0-
I_HTI2R!i}#s~I*l9P25T)jS)v4Ac5e;aaz;*mhSU=Fx&bQxoKZ|5;jKKu7n~78*3{s}^W$fiB08iaq}0gVGLaftWh7g}jh=_BTA
SpNZ3GNyz7Zd#=Pp!;sM;2?-
=ntHf5Jv;A}qFOE2FR3K_#tBF>{wCe8ALO5HYEjr0YQIuf*psQM3wJ0Z86Jr>+qFoCpkA(fXH1GY#(Y#OI0T2sqWPm;1`bzUQ&9{
`fPo8O?f@U3}`KS@_X2Gz*hhqiRX`ep(4q6g1!<CJFA;p}+q_$XF3wb9$P(KD$h%+2QhU2BsE<f^Qw^*-
p#Vrnk4moTFa<=e4Mf0>=7RR*J&}-6i*AC75UrO`-
f1b5Z;mSfeehq83@s;LnYu{t{na{_aeP4oZ?xlIu&OR?XcgRbryp=SfgDN3uC>$h)d*M^m7LYujH1V5ajm8Ay(0BrJ7JxQ5I8zi;
T+NuHqCwN~xdW|`+@3LBfzfi&LPhiB^@^Kx49%mEPP;T8d@0Qb|A8K^P?k?*?d0oG#-
fKSZm5+EwTyAl!$l#*WZgovezl0HcXF$>3bjxns}yQCq4IEvOSkFC%7j_6<TVNLaCx3yjo_sSwNRPw!R8f+h?gG>&0oAe|Karfcd
uoU`<alfTNlE0>n^d8TQ|guCqlk>#1!n-4GrTNQ!zavLdIWB%Xq}p?AC>z-MXP@Dn+5jU~ABp;DFBDAR9*=3tJ!-
>J~u2t*Z!Re!y{{SeZml6^tyTjgMhO5Q3Z>mkgBOglQHu=zS8Rj5hC}C9Vn>i_**^c+6bl)(xM~BjOZvf{*b~n>4>58wV_FV1_Vb
5ltn=L1LG=E}436+=_Vsh}2MJ6#96tunUSyP%{_FZj&Sna!P<R3XXva_?#^IA;Hd|Q_x<PMnk_{0-yQKAZ}oYBbp$Nf#yN*H-
L_<7ByVOLqkcRMXbsyUd03mx1w8`U-
3{lmio+Gi%x02#Y2vb)}XKubP|wW%2ConvT(`8L~Ac~6)=sQ7_eqzHA#xU@zzLQU|5`9L7~$kpfYW8qREgTYUnRG$!quxs#nER!>
EDB8=mToKmoOv;edLe00GZ9xLOkoLxkY^{Fvjck;M$+CF24`CFB|gxaDHvd_}JcIfzh0{u|^iR?*ieh$c9X7MIZr-XDi<L^Mtm0j
|z5*)Rr>MI`Xl+{+RX>J^wlNewh;i-
c!G@dm9SdOTDrRGS|IG@EYAlQI;wjSO`XZM;%RJ>dv$m<zyp>`C`jG&hQb>4zNpjcAP`yEVZLVUwsu4VddvoHtAX$Pdqa<{Jt6Mq
U#L8{$Lsi^IS9<PX8r@t{!CDHI$&S~MiF%!UdJ2UbKjI{wD};Sg~cj|Qsq8PbUeIa(a}#i!$Ltw=bEBgbJtV&)bu%|Ya#7Bn$L5@
&`ci{r^*o}m&0FR9%US`J#VM=?=+YPSTL3+Oyb%)vfD5E5=Kq$te<qz;cQMV=!tK_44Jtz>V;L{CJ9s;GpcBdm$hb3#iMnT{p}L&
iiPG3sJwcc?~ERE4X9NeuLf7)4d&Iv-<-(dRBm5IYPzx`{rskESl+>;MH#-
UUYumdJMKdB8|YwMmdW+Q!)O8w7zI;%PEuwIp;Rr|FPh1R>>+1VKY7=8gj`zz-asmu=~IFa&kep+GV&6`%LtWdpixfixjdH|@})-
JY~_5!n9r8z@SH`E0dbrWC&ao0D1qTqXMk0;)mG8)nchC|=ZNFvwQanDug#@pVn<dPBeI>10he1kmk8NQk|Hv<kf5#pTl<PW`V!>
#NZEDzv@|t*=7se}>S4ta5w@_9%o`>@<u3qs?3_#zK~4F$=RM%QN>&MH-Ay;%|SCNNd(%LIFrIdgP+>T3O9)6eQXxovsQZt+g%E8
g4<P{rB5n;#0s|*sDMYuKWrlPuR17H1;hJ%`5N1my03sHlX3+Z=g;pmjh9hIW<aBu*IFp50BEW0w!+j3@La^cT&6)%)%kjqIOXHB
N9X$78o3HS=5cs;$Z<Ht_%9h&WpP7UVH-o#gBnB@nn#YG);L3-o>RskWTy2>c*+@3G5c<2Fb}#4Xko-pqzCildhVOrkazP95kI9m
><t<&>0V3l_pmRK`}c+>e?GZL}`v?27pu<xcqRY*J_3eHLWw6nCno<3v*PH?k$J|>5)0H$tQNWsrJFm(Bm*SOycJFCP<nl);`4Pv
UjU)pX3Zxv#sNtfaaKWJL^zq07@4|vCeiv2@D17?IWI$U^M;qK~D<NMEH{*_JndN18E=mq_a&_(mMDFPGPFFPJafxf6%L2CqTg{Q
qnpHil>aa)@e{~kBz!5#?MEAComr~7}K2^q+vDo*#jYwLyM#Vlo`xe{Q34k7!|=&1qJ$wp*DtMjG;SI#8EI`Bp6C6FDRM{xUr}z9
8d_H1f>$V*NTF#DEcozQ5Y3a8a+B>)`-MVlvqSSR+sK)@dQOFED;3`Y&M&~rsk(ml*yUYQe-FI7viIsMHG7!ie#)B%<+rR|A5fP6
Bu+Um=Tn{0D3r(MbQ#RHll3|7`<i?DiEdRorr=QHCjBr)K*q32{Buw(fW*{1gLIADc}ztJ&J?`vml1H*pLnAL_$Q)U@BNiE#XfNb
OddX_3hXbHlk=rjkrY-gk9NOO^u<*NiH?TB`uUSX3$>%a6`|1-tAtOfJ%@dKB@IhrMyybB|ZfRG{rYYQP-tyFmxspFDLSnm`k+G3
Wy8?1)~&x38aM?g?wO<A)%O{mw=xM_SlvsJ651NroB2}45Ll5DbR5;N8^1uXstn<1yhdf9-vbz_<R@*ye$}&-
E?1Jw4jR8o;t8di<F2^siH)F<h7s!r%k1b1_3Nrs2C{Q^uL1Wzd{v7JE2bzYhx5tvv~g<%xvQQSgE441t^65O|BfJdp)Fz@~%8Il
<r_`i2q9M&;uGq4N_9HDvE9ae#na%d0G`k)fDi(6*n4gs8vyN3=yO>BfbYysiK6R6#AJ!PN|~2x6h@GrgW}FP?Yxhkzo@7S^P+JQ
BwS%8@h3<HBs96=g}o>p)1ZO-UJ9zi3mkGXe4W*v>_19K_|VIQA8<@O6&u!L9`(&qP$Iz4Buvx@6D{M4TB&?a+Im}s=b4}Pp}y<7
^rQ8KKWzffPG%Fp%B)8lk9sw)Z^9F)<VDKw=j$?rHY1h{~LKbAPm_bNE;5(hlm^n6pQ7{RZ$AkO)i%ZL%vrPjcA_vem07S9){5uV
5qX=2kCM-
$(Fs<W_gt@@9T?uAn05E@9AK@NvE~zbhRqYCbO)j@|ILyr!<<}Wy8{XIZ0<%n<>}Lw;NyhPhNYa!8pC{XUqEA*?IP1Gg)S<(qMkQ
m}ct?RV)_M2@20P*V&S;mZmFeH`8p@E@gM=U|kw5v+Uz!c2%0JN~>&<(!IN=N}Bd|CYS4Orqh19?5WF<@AXx=M|3~&U`h?YkhWG{
AnW((lCSfnn~Qrrx?H!{tE{r=$T@Q`QF7HUT9z#<)w;=W=8RFca#pRj|LzQu#rS?T8LW^@CF`SAZ?>qm2diX|%~qRYx-
+nEg&wRr<%`#R(K8IDZkzL6Ea&qz3e&SP(nd)KpYQoo-A~W=O;4N=-
QSz>c+rjL*4w$=rCBmt)CbG?3T^0&I$pP1qrWcbkpBAlZ*COb3OwN}y7Oj8Mf|?^^k|8B%_>3lWHr*)$xo_io&ND2Kg>n*UR~;?y
OmW%S4qdTX~wOnyg&A;e+^Vy-lHx5RT-G?Pmp^$nWfXK`fR?uu6(j^b+@fudG-
5*Zbe1~>GBHvQ@O(QJ*F2m)eRmM%*J}Y9E|I0%<X(xS&gbPYnY(ogZKKuYU{x&uMH%YaD$fVeTC>vihN%zaaJG97x#3pIX}%7t7J
5tr|ZgmRnKNOljVF?zslB?x8IzeUGSbAFRR6GztIJ*(#4?yKRi9t1t@4{HE-IxQSvSwjBbZQR;%lDI_>3{qnkQN2ji@Fm(b1GijT
6p1vp-~=uRl{ERlZI2UFy$RNH4A-T!WKR|gJ^(?y1nc7keqnXNa=S?R34OmDI&Usp}l?zEurh7a-
v_3pcByPvMIM02iHs>efH`M^DW&sW29$;C#Mk)a=8v^w;=bMn6H@R#=|?~hIP`Dj$_)+%~@YdnBem9d!ZM6uVIlRC4FGg~@0u`_V
S&MRrNhAP#jO``a?qX^DX^wn+O?mSYHqqu-
4Pjx^sjbfIKE<v1sOWd;QR@+yJqR^uX{y&h^YJIi2t_&yFiC2A6sOttYX};_+AFdq9QPU(z?^ZLnHG<AnSI^;1IyJMVGViCZN`V3
H(5PXy2B~2#0e8d<sz%W0-
WuPH9$m#|F{BIJjm$036(G^3a}qtX`I;|^XSt@iw+DHK&fPh7ZrvoR=)TC)cg|8tz~0p|9VVBM&ee92itnrKT@vZkASV{-
WVw<@{I&9Gr*lk8Q%rtRseGsv5s1p2xthPK)uSU{X1#g@I&MAjwTM}QWcviA{1$=mVe+ce@77**(r$aLxn-
JOFDkVPB_0h`T~8`Q^Bvj{bg63lV?tSu*GEIHi`z#Z$BNMAR~1yU>>kmFspsR-NA*3&Ck;Gz3LFKFFo_E4s8%y58VG5m<xS~kJ*S
_X#+jY_DkR|^B6&L_Dv?|7X$Y3-Z9;Y>T8pA{$cRdL-
?e*Xy!I@IcZ~cxBUoHluG2+jy@A@}psr3?c376ddR2!TUwy*q)@DuU0cQz7Q|fp&pWS44KZ*_lwp^|!Q1V#LfnFJW?pGw{ZmQpTC
srG_nyqs|GpJTO<+Cy~DhZ_r)KhuMmLw@Z{pqK2HA%`|`Gm?(C#!Wu<S#V`no?EDm0v!;C=*5H732kITrd<){;b3KyY&@RL%hW)O
GVd-R^miW6XZVYkUY_3-R@_rb;1awNW{6W=S)uN)oyz{p-
f!`1%rM?@%>G5T_?1HB$+36IV4aStsHcydz7H2t}@qOZtA3DRI391=(<Yyj$}oP!DId{wGpF#!hcV?Nk@~jGw-Tm<^_NC+$3>N7E
4lN%F5HxdwF?!UUn!0A%jz<n#zu<7fso$#sV%xxd~b@xt@H?Dpr?RXgL5<^pm(@l3@w}H{<y*DPR0_@#?JXSkRpOQC{CKvhqn82E
YeQ$!IexpYUioWz<67@#jycPdBisnf*9f@QBxZe%rARQip~QRekV28T6g`f~^qLeVyKsRRS`a?dU7zpP&9F{VjX33tGU-
*Yj!lgru+Ml!uemqI~j#RxJOd{+^*n3QG$B$fM(S_lSfoRb;+dC&S5LT><me@h0j@l_)O3KgWz<qKCU+mMI_-
I?}IHM8Oj_U*0G5*HK1V(x1<#m1SN1tU6+=vD%7M{(-
j}n@v4{O;UBH=;UgEmM7*LaUBgpx*qQg<gc$UF^Gi~TMTFYc8S`1>+EhVP%*@)tST4<N7-
9*h#g`>2h(4z9+%&~MY;ACNuK`lyzG?zcz<#uy0~-048K{|QTz3(QYEr}&vF#$72u9jR^w5w{#m5i3E5?|J-
ychy7YPk!@VA8jNw@9)%guss{?w0Wvjj*V=V)2-@#s8Ug1r*<M}kJy(%%@mK3(qK-NpYXq(gFW@UE+Gy;$6+PG9^Bwqn2mgWNEI-
T^jfl0$`vN1Km$b)*Ia<2xH#eJQ~oY+qnf?~B;&aYG+wsL!m`P5jgl0wF&lWvBSHSFeJf4xk2N_)N0WQt*_LIqfYWp@P?4L%K>10
DdO!nDR9basSQ+3EOor&b5#*Sl56Jf}!&`dQ4+x(tm4`M0W6s7X&M^rGXkp`>M&4uy~)1z$QZoYN%l3?##CwVfv1C;9O#A;Fk-
%CCAb-ysaaES)kr2cT)q){so?r(^;5Ed%(yLpGB$bH>%8A^gI&e?{`moFSo>@FdiMWZSN+wvqeEsy$Y0JKiURpRBZ<%m(JOlcz=w
9MxvfaL~-
Yu^Y#h^=oC^&L`QHi6Vwd2fC8{AC_m=dD`3blc!Ff{`57db}BW@i(jvHkAmY)h15}pKB`@V+~djBcm?KEt_A}u^s)tYe<|>B*EtE
gM=)NVc&^U8rPVGB1#wdqyK@k}-
m4ym;_O{KV@zRsL!~)dF3i`*v2)G^HaDNL2S|V~otBt#O7l@EEv>*S)5&0hRP%Vi3Q{SkQ8nXiNVxZQ_H;TWIGDiLD2-
B#MG1_Plg+RV-k%xQ)zZ#$$FEp}Gnd&r9tqU<41~FyPljX^tjDki*gIANTTa1i<N5XcDw}2V&8l=WpW-
E@fhquy$$(jCyrL~+XHeSqW)aq}Arw{`5Wo<9jatUzH5(N2EVJQekg2EFfC~NKYB1DgmS`*0p&z|a34~cM9szK~<_^?HXPmAmlR(
dK4i<L$xg`db{qE?Vnf1=OCzc^afU;Dj#A?$olwhs6a#wq(%q+XAq+2CwcT#||rz)SAzIN@v7q5HN@A%zXiVu8)%vRrAN^|9@qrQ
2R=E+l4DQN$C!ipeQtesji<`s;vQ%U<PXo-1yDo5OS#}zoxzP~H^RqXhaCs%eyoIVmXuy5g~dN-7)Me-
=yqD>xFWQ3OWXYSRTIPV+=Gn=$5)t%}`;{*M^6630jEzcgFciv&h=<fvb!z8}X6RUYyAOK0&bOubWo`6x;li4QApN|uwqM0e$CbW
~JMYT5OHZOQ|kfB?smsBel1K+yeg3IaKp6V%^Jp9f*0pf#}0R7{nHs%-AL}g)x1-
8V#>PZLRQ!h%(98T1*4vR7gC8?4jid&=cze)mZa^o;Nwhf%M71mHs_aGC%0Gjlwo>!&_i)L-
Y4Gr>VdhXdoN^&YD;VHSO2NoSkH`v3h%Sy*6Wdv%vUL=1^PTq0iJ7-
etExlh6*&^wvxy;K`Bih^v?a&rt961#&&Gk#Q&S;U}NVoI4SnH@rW<)eOoi4-
y?ktqU+tG=>l~{FVAfJ;Fn@)I=(1$}mt+#WtweYTtSpQIOR?nz;mG{{_bn)x{FfENvRD(xsb+ohLRaWFes4}BHij34}_g&2~MzkV
KaZ~*^8RtaH>}oX@>B@yeC_19PoOF*zofDY+C)|!YW*hL5Zl-Gi4(+KB%&j^dSS`jcUVt!a1yS1#XwA>tAl1U^*<`CqwOE9*gOBM
CXRETWRP__J6hLv|$ODJ7Y8)gJ6-vo(lBx&iTu|c9v7z_3ZksOk-
l8%!AY9xU+F?Q@@mr_gb$;ulggn`d!D#3Vw<rq_fCB5}Ma5=jR`k{h;R`(=YY<<&s`H{!qk5=TROO&})rQ1{LJoQkf+p`+fv)vBM
pbpj&>mH~04zF6I&x*{w)5pT!u~~;zE2iu=cL=d&S(t|L-NPu&-^8e6v}l<$=&vPnPo|*BTeYZKuYa2{-
X&mmslfrJBB5K8qn&$B$E^VLNDVl-S#BmFL{17y_0-O#@f-SXiqxoSUi-SRB9R6$H|B}Gw@~AZo<a7Nw{GUn*6t4oU%=l-
0T+zmGce_PG>_nAYZEA>cktJcmsB!cicFeyflpy=1k8=zse&A0@5j|)rkINxgIBZy@f{b!|%pchgh#z&Nquh%@@jOSLZTOm9(?zF
jK!aw0sD{{9}1SmcXCw^?W!_I?HacPKIk5X?nc%KGm3aNy7D>^kK!l-
_2qc*toavx_fFVX)8$?`P8x#`hZrDyyK>AV~XJh=$T1}8?e=MO=jycxw`(6EKlgWu7_*a54(FRg-
r^jdqvAn!)$?<RCv^3raj>=#S+8|x@vX-F$XOj8FBt}WJ*`-rPM^6ovH-
>u~0wwn@Z@hd8v#{^}v|9TCnlNBYm?@I?T<PfLdm7iz%1*fl?&<Uy=&(MxFruYrTeHHJM%Ys1O9P)3+0OsOh7CMkxp@*=U#mUHyL
+2^R2~#z>=bZp$ljc&WjA*Yba!?D22EN!<3&Nyl~YUqK~+SY+wWwb`Q3={tj@^RlP|blby3>=2Rt$OHI$bDRu|Qn9$2{WItiS&m>
K;7gxA2KXq-
t~cMg?cbA*fOUBE=I91lYE*Q$#%eAOU#i~B`bmd0t7;CbFL$NV>B+3mm@;HQ!H>TD&{%Ro2z~K}K40?(fBlg^`0K}PIoIRZepQfs
k5)6r+2m@xR;u{#N;}ft0eOhQc%>OchU5jLuROCv@XV&ID-qIq1)t>YOEMl_vXS7BHvT(*)uzdQ#l^w}>MR;}oRF<~1F4*k`&D&E
eZL~D|6(8V<QX8?FWzit*^<R1R$mt6kLnq<e!E*a<SOpQoFZK&3Jm+0wnL@3BF*%5zFlEo2DJV4o9!%AX$50hby%ab8gi<Y>*|gg
^gFem=c4_SQG(i+NzL>UKR?Wr=0XWzgQK60FQL2a<%jkx5i%ns$AcE4fA+ft_4=tII#^}jtFPDO9;C0=^mUl6lcz_|YTqAyuL%-
K-?<hrq{*`*%Kw3?K}Pi*h5LP!H9zx5v+9nDEj{~igvz-)AE-MYW>8Y)Ntzzb7%cin*ZaF%ppHxDr`n~HVg~wZ=Kas2+8>Pr5mVV
cM7ck{*_RD62ofw`V*~j*oeSr+^CMX!w<OrMp1pBizj1ziLyv(y6LG6Se$@KgCIyvt<OP~9(ITsmhN2TSu9BB{R(<ojHT4Y!m$m>
F{Y2^c9Stt`!b$8By0P%}cW|7dXEgVNDfr4!MO9|C4zWY~dX$t<V_{D&N)l4CT0+0dPWkmOzdZf<^m)1J{5=r_fNY~Lr%>?|%Z_o
LCH|3mU<tY8xg+kF<fS7XLDmjlRNgr8(etCDfELA+ix8rMA6+{nXr3z+xuy>M42yKKT&;W8^J~%>Oin+fTEeZoYVzfe!;{T(mQPW
S6Z7AWaS!xZme7ZDk$_+lkWBI;3w9U^qkRIpD`uI}Ti#pSvCJfOoildwCyTx#?*8OMf6qcYn?}6WVJ}p-
Y5id#3k?1HHJO<0J9|NbRSa6W6P4tSe{{-|*<!Qqt;VSz#pQ0I9G7)T;6n9rb~l`$@oU;nkZiAjq4_-
+Br9H;dT2qcy+&JsQj7ZS1PUKfPi0YGf!vPEy{E6AztsB!R7QK*ZKcgP@v)!&_Vn3h@9fu~ewTv1v!@pqWrsV&RM~YZ{NwNV#$Qh
Lmlx%3Rldp8BfXr@F-^IuXNwRhpCJI6dX=q66qM`i$tzx~afsA8&zV}hspd(qOj7w3(5~z-
<dO1cl;LtWXXav=!eFSu;uQwo<516LgZVJy<<#PAT952WecS@Xh!+lf*V$m4&L*qtJ&TH7P=jv%#B0^`-~m0-
>Exqqc%6?*Y7Nb6^?ryPwSSej%}$9umTEOZR_@42pDk$tW3no-
>z!5;s7tlMI2*jrhWRepD6TE%x5{6LS}u_jO@T5ulx0n|7D383wS&HUerYqK&Rn4;5ZN-
j&dfVk?b2kuk`}(5jnnC9wcvG+D@=7Motd?dl8g%`X-
!tt!0I*a$z6}<D{jh4waRN5DIkj|YEgz;mOmk%)e5LLq)O(?$rUZi<s&j*4tcbSn|vQyzBqsE@`YKtc;w=%16_f1J25O&F<6w7(S
1*kjasEiXY(1aCd=cuv$Ln?r?g1+<I|)Z_Pu^K^um7ZHNq^WE7L{|e-
wpj)M{kzaNsw?K`<D_(I^dCu|I4?soxmTVN|a%j7H_RvzO0d1$<H56Sayl-K_SlyBt5X?y{a-
18mpM_S(z(XwTvc(R$^jBP+3F+Fd3U)&r_)VcLj|7Yy}c%vH9Gx#~e<4)t*-E*)vs&{2KjKb()zL$&mcbGc_D*L=R-
zn0!!ERza7esW-ES5f?EyQm04i)8_Pk|ZaBw=>21w%kJg_Fz1j4hyU6g;p?}6q=xy*q<j7%<t_?>#y>HEh{@o_zgR$&rxn?m0oHv
-4m53Ndga<pXrM90+XHVna-usI+Gn|rpK!xLO{>R%=k+}bC0Hgwo&qZmMxNl<tEy%gv{NxQmVE*0aODiq=We~OLC>o8p>zCo}YSt
dB2J#e~5(s=KKJy#~K%^u`nusLw`L|T<6o_8wVekiJ|}Y8`rsX<u_^)n!KLhWJ76`r3ju^sC*3tj5@fh=y9e?ay(qRw8U0a`ilGB
>1AfoPZY9Q^|&+c7CG<-9wsP9yz}q<L!N>ks%8ak&yw6r7%JU-+G%K1wKPCM{v=<%SeWID91!vf|0ctQ0Uxqs8s%sb`TJs--Av{i
s9!um8dsoZE%HI|-
FzD_9*9;sP5arD=&VC&yq`AFl*rGZWXh!LceH^Y`4qN?w*a)^S|eKfX0n>}r<r!OJUD)O*;erGZ`*ixYb~wz0k!N*7~qSB!dqFmq
7-9o4PhTDgK&6D;E1*{4i48vcwFp5Nz?u<r-
wGKZ@+UDi|Gt%g=w3go<4v6SJxkw|4PG3Ie0<j0N3fAL^)@&V)p<qc1|!a?6PD`Ebchs2M6}A;WZELU!$h%FgaThvp3G{vcS8g9k
xGailgnEl=dS*pL-
k}6;gkor7ic^Khh&p*!z@z$~aNp>s;a#O_hp09t8uVu%pjtB^5<G6UalFPr?>aRCuV;?HXVH^8EDd6d%8QqF$>)c>`2cnPBR7LLW
{()nY{dO&ifaY9soGs<w_XF!Bx7hB1thsK1xDEMYvdf0vE%n_5QDj@`S@0$R*hV(Xl7lTzEXG0$G<XGMFZfHitU)te-Fb3DA2GXs
~2R$hi{VI>SyUCtp?wCdXvnBq@i1aZ<VFg(JqJ+*?aep1h}VXq)ihPSyak;nTa%6dzRuxK5w#WAAbSMxqvS~WPV6X{2FA0p$SqI6
aljMVJlLBVNe6bYxy-Ua++KLY+L5^(ZqcZ$>On8~Gsbm_mM-duE@SE%WRF2UF$w)HsI&MQj3TbYi@=sl;gV`4M2ghz7D0w&$WNIL
R#YjIXwrYN?dNb9s*p&D~(D+YFhc1!HGY&XvXO<ZQATnLYgy4bU!%u;zBXyVYk@q!|OuM$$!@N_Z7{Omr3n083v>XF?E%ej}EsEO
8X9N8UnL&aF(fHg_amGS{;m(H>t+n+Py^Q1hZ-65rl=**?NYU$ggG%h=8pn8P(iTdFXGt)2bICWa-
<S$<S^78Vu_w&<>i{4MC&wo(&8J7=$qYM>8gmUhv3cR5A?Db_&1gKOeULIS2;vc#VHP2xJFql>($(=V`zQH8?E|DfLY&f@Gr0Zt?
%#zqfBVf6EZ2x|x+%-#!93JagA#YF5Y)}`+%E2wuw1ILxU)=AU<z<sx9lCYojP1_ekW*H)&XdY-
N59G0q4aLDO1x@eLr7uWjlgc0(Eg9wZ*sVa4x3J41oQ9z8a}BE|7%!<%IDFJF+8MddDjMQ+2B)D+dDMIW^2Yn`!e=D_~b4Pb!0_t
df?WZeHdx?FG+gBU(`N~v<vMy;V;%ny;P0Cf$bM+!Cdy@^BWFqv)H%60%`fqif{9M5B4?+s0)d;)q<AdiyI_(v(4f=I^PkT>|c^s
*`2~x2(|cbR@wKgvFB^rRYz9GiDl3)`qQr}VgAY0@I6c6_6ZE$hrdeHdGW2|;-
giyeJcCF#Aet!&^=OXvOBxDX!rIUHIAH`SFN6$9^S)M=+nO4T*WiuP_i9$Oq{-
|lj8K%FQn4R#2KB<&L%VBg7V~@GkI70Zc=t;PM)ncsNxH4N1>t0*L2Qm18`_zt>!e}FxIwLVnj<kvzA({#T8-
x{G9y=cu;lD%;JJtTX4?MMqX>{E620KFge@UuR5<D%J6|Qz~<$hU7h_oy2l;2-
hBuM>HJ%9^E6F+el`R$ZOuMl$&{b*L$<r*p_6;|DZ@KH#>Xe^&iI_&9a~|gyWCTw&KRomc(x;m^PikON$$2BM0}R&F~<)@?pU^$%
?r*%Yz@Dv!~w-~$a)KqknLkX&jzq{)>(<r=bnb>V+LfR^F1Y2E@ae<OI#}!CEC8cypO{Y*Z6jJcE29aXQiO-
1@*|GGd^ecCBKdz_0r{dvLau33Q;|VbeRlDms!q-
8+If+YLjwFpV(Qxow5F~yvk;StTdRWlk0lv6f$K^j%#u7OY7K1D_w6^?ARZSOZ^OlLca9-5^DzA?(9!_svkI3^pMy3F^7fF-io%n
m9=foxH9|M_BiFq&9@ytSwHz4quZ>|v=_;q6GTFtz!w@}+WxD(ngu&JN&4I(qCBN_$&-
D{iMt+GIlA<qi#I>Q)N^|KoTC=+z0{|7jVqRSXeXV@)=4|Z9I+}p9g6)*E_|QQUhNBDW#w1ND5e6(77JOy1MNbRtP9yiyzLfwExT
^<pKdT}u98t;EjcfGwS-
#A=LV>cET&%VIcTg08Rd#2$~dJCWuX|4TpU)lxVw^VY<R~B(I_7pE%$yX)24ySRTU$4badtDQ%tXpDx6S-Y+F&46y^gDP+@-
hsLee&PRKF+P*b;$MLx3GBEi>13Elzl)EoHMY(#wQi+hvL%;jH)y&t0TU*9|GE*{;ZO2w<Kt4C+hEMHZR<l$pG$6|@*Xi+@yrw{b
Wc|QB7pM4ZiP6Fz~es_D0`pIPMKkD~<M|QMtM6+7b$+gPb>}BAQk`o-
(4D+F~SD@Ix(=p%YjwQE_NmaA^sf?Vnm%sF0oS&Zlzp!n-|D7$e%V$3-(}uG@(mL4+9keI#k(gLDb{Ih5kN_*`>`pF`Uey-
R4>2(;E6g!r5=oP6kljvJS#5O<BXUfh@ETr9N2S^vyogOIIzlXh=*fV@>j)O4T5qKWuSzO-
1f4?rWv+#kWU<B6Xqs}gq%{lFA&HK(B>E>Em&;aA7`LU-L9^>fuf7(oICGX&C*+ZqRD`9<&j9-
A!8l7=%iYzD_XJ*I4Nqu>7XfZKEYg)77OA*R?@VuQdj}wXm+!?Z<ltS;e@WCHby{FbB)Z0HGWD$(NcJ{9&LDgFz|~e9p~a2<@eX~
s+KwY+heLYDI_0~<PWN{w(8MRCJO3BHyd$-
HvKt5~e}Wf2;_Y@2BaB_)JUqp|kq0+h4{r2>?I1?7P0c>YB5OG7<z&ANvu(s6qcLOXI~y{eIFRy?F*C}$_d%Lv5MFjr7Z0VVer-i
L+KCfng<OIS+SrYGBq_`6ik~YAH{n`}F_7{=M_lL^iZGBSDio47ncDqA3XHM#U{FYcCDxwpi}KU2rOsebORMeKGC3HzXQm?ev}YT
baCZEb*-
{&8baaI}<V98Sid530eJ{l83h{#4H*qqQNG<I_QW@&{jw<PK|G1FZtv;!QM>jFKQYy0za@4l!f{fl2+Be>5o?o?`8N2b7bX1R>=u
d@t`BYe@J45Pv8WuOidWx00ZHg+B|Evw#3l&&tu{vV9J3@{<VU?s;2PX=J)KncE%tN)SOxBzgf-=dro5aL`nonpt%y-
?9`MYB1Cy8jaKdRH>%8^=~F=dM}c=Af<#Ay%ha4I+PlUUOJ?jF_sJg|mWHPN6XbP><RE18S)1ghMtqQCAmv6veC@~U&HIAy55lfx
pl-
F3<}mmUorRSTgfAN}5N2s!R%{?tJy0#|wVrrAwW0llsb@ecC<NveQ&hPM57udIVs`lyaXY7*(Rb9m}A&P~}zrnYxf<}Ek{CR&o@{
Yj;U?$Bz00O={Y^R+<ay~qhAwR5+g@$2<XNWk5rQ(t^)D)$MJw@;eJ&b{!+auD*E85gSd?=kpm^zZ8fbjm+x(J7byw}$rm@R-
nE|Mo~;S}^^yqIucR?8sgUc9?&*gM78+gw#$*uXY~zOC7?pV|?YuvHnGozCP@Y^d%)zCX}Aci%m<rM8x@bNbJt|FLgV$R-
j@leO`Gg^;uijw!^c0dK;Uz-TqGvR;D{)J3aRp<;JaP`P;7(ZG(tKA#uV!KSUUXY9d2poi4#8lk2R0JqK9O(w>PUsN-
2ZCWIInkf>3|_CocC<A>=6Xhh_)`+|x!KR>7#z4))b9arqd>z{u5{^_}jD|W;$`#(RbSY3q`s~6&msV`p;UCiB%F6Qn=7kibcpk6
!iOL<K^_k6$7^DSFp{_$X6^xob-5`An%J_d?du|>%>CU7g5nDoUtOJ3yxeeBR>bD>1`3h$3Grs?U~kEhT6H-
`$+JGO+WdF#l5jax!|j|e?xmDvtE#&tX{@R(Vi`0Nm5J3f<Q=%PiooX~cPbXtfCWE?EIc)j$3CXIK(&!+dK4Ro%l9sD}u$l0T8$=
;ohy>%&3QHRuqlAhkn0`NN)7h>h3Tgy{jDEV(^PuHb&;;97|QdXvu{&KRRBSWn0OxE|jII_0m8f^tJviwH&y4HNfae;`k{((Sg4=
jc~5Kc|wkg1+E098b^0g9Gn*5TOle>;;WkaayYr?(!HXj#EfY3C1=KcdHuUuCl8zF(2fO6Cyuk2gs{?6p}W)m3blY^Cs6`D!PJ)_
o~f&Z5p6Wgi>I+revS3K=sx6Xzu8azqpQ-towHkjQt6H{KOtxh?fatDM>QMlmUDtsj|n?}GD=Iv|@|ch{1=!m={#xV;O>sbhLA`~
GjVZ{bPYCMw)@FjOroO&kovJZ`LN?+tGy)NQtxjz4mvi^sItg?`rMkS+O2{p3qm>JOgn<`;aK=ZnwzUYPUXD|U%)Zt@*26IlqzTP
s9bx?<;JWl{U6J&g<Nu(EhIQIUSnmDV|~b`ByxI3}MNh5m}viOM$J)2@O(WlTZiALZ|-
MjIOap2piJz$X@6uyEF=94}sra&{pbuU=PKy1wS7QG74MGMgKk4J2ReK3m<$Ar$QnXE*p^FSzs3bylp{b2z_@C2)^|TP`QVj1$#;
1nfOj`y$$T)PHcc{#CR{QMasE=_t#yD^>3AuCi*~ZP&YsUJi;Z)&*&zN~la{ZgN(z%=R*n@euPq_tjpP@D8_V54&O+Mg96Mnt6mb
czy@Py&xZ5v*A?Vv;gu;60e;*_xYZM*Bo!sx_&|5zQ6%CMkSsWl8Eda;0+a=w7n3qSnXekkQq~cmw)Q=!eaH{@`4r8%hc9>Xwd;f
_K&YRELQ)TRfmPTI^oebVwlB;FS!Xr&C$iy9Q{+S!B`PTclLqYzB?^I$p4NDF{n|p7Pf^whVq%JmHND$hq+=a5rp#JeZ>YaELU(k
90%hdt!%FjDz@d-
LEY_9SA*ju+4aTYZLI3(Jns(X@r2T74wFMu`Z*i&v@g3|aKsm1PqiP_T|Xb4b>h|wOI)%1g1lPW3tXRECwtsd%a<>KeZ~sdzjp!b
@cP$78ftL`>?297HQ8%2Dav^(;`g7jh6ClA5JxSvecZ_vvm|@u0@p{*Y^`zO`OzZ#*Q{_YKDEB}58Rj1=0SP<eJLyZ!W0yRZGG_0
luvY>ihrVGd)M7oX6a3)^b42X4qe2u%fJ7gi&*{x{o8HJ4gJxzWDxDXs=H06Ru6m-)iqfK3EKunYkkXsF!HmG<sX0j`Pa)|&-e_-
rP|;}hkMtMT=r<FQiXo=bsZ{QZ>JP#%_a|t0H<)jfgE`0bkUf^@&#0RBXT~3^lrH{#Q4+aQ@mAq9@TRW-
L3+ns0WrCf6o$tG>vOIuDg+p4+NFeLHkU}hi?{x$hEv#ZCCB@tJ;^U>yeDyeowyT%~q=MhZ9<N<Hdk{dF_es+_87tWRfhO@8ag}S
#ECrz1P)k)-7t%X~!fSO9Dvtvt8ZMBRt(`-
6}B+rI_)wo=H*Oi=OYB`IMY1#*}<TrsP}YgB9;Lx#B<~JiU%03;FYTw_sf3QF<lE9G7+V>yW>EpJSZ*q}}1UD_x!~$xZl4FS$99i
Z40yV35gMs_oEMykjk!u``zYSv``G6zOgjc^&bxZkID>VQFk_H+*&9Zu?I=zyFeeV-LEz`QpZ@I$xcG&gJ>br$6;%@2%=YT^-
n~l<Od(Ub&i|#O6A_*rPAYg8A&o%9i*&2vPJgSwl93L1`=0VF)XmIINEy7Y-
Hmz)5nh{S(c9#B#whqa^^cIv}x!>TJEWVsJU8jiowhker9C(XP?_h67WME-jEPnS3)Q1?O4J<>JlHy}aa~a-!g0yx-os)<ll?7WO
u8Z+WM^)lMOJO1Z193;etrOr9qnwp9S-SbF|f*_@s57WtC7F~}U0I4<{oe)*hNzKWqn{38?Kpu@3CI`5#>KYyZ*4^)po<l2Zl-L_
9*$?pk}B8Fx0G{&c{@Yy|$VTBm84`n>^R0dlJJ0~*qj_u1I&reT#65C9VjnINR`uaFFl1<W^Wv0R}?cNunf?nxsYUxx@jdn7j4qA
_Mc)^^H&rf*GE8lEQf%QLmM(0t%sCJp}aiOLj6=3S$%8>`c13gdnh8p4!d}hUDhhc>q3(OgRf`OUGzw{2G{Q*9P`yvtB!8zz<*Nd
d{w>pW;JGCscs9MhLg4xh*E1F9_5%lQ1a^noGD3*m<Bp_0r@wpvNn1jbMi}Sg%<d4Eq(MUBd52y2II~_qPY~{ONs2)wKg?k;gLId
&EZfI+4kaa5W9SPg>vJ<%7>d~+^K6+mLbikluq3=+LJ21;`x9Tm90%w1YcMKnV#|!Hn`zpZuhFvRmi|USS@{=ZLxAG62_w4gGF4L
5k0lMuC#R+*0;^<F+*W^DxhbddP2&axGJs2EUU_~qbaUonuRf&iWQEFENg`$_8zy~V*aNLAXN5@iCbRAQ4J?|OpNUj%-
>;cSxr1N|G6)Libq7@;u8j}%4X}&#_k#p1}dzAuV^=NQ==rQ>!dQ|duvYwHauO@*a`crZtpNb@*v#L3wtg>xZ(tDd3%|&^5^ju=o
@n!`Rrn1ISAM(>KtI5@j;~$b$Q6{TGhfqQDN6u!ZQnUr1YzldLFpA!B6c!9FI}TQSo5%m7zS2S5VuADqbKZNM=<9AM<4E#vs@Cl)
BN!;@o!Pn3vuLWv)J7k+;^V;Ly4!cO3p5Fh{=8BPoQVGV<iyx>$jjuT;DI{hKNnaF0gm>@d$$hcf8yph-
hR*1mUPJYrm)LLGzRqd`JTYbwefa<Gj%nBzME(3l%7;B;QXEYrv(*UEHRB?$e`e5>%XX&%~F$;x0!qUD4Sw-YPCe&u_G8$YS%>d*
@;v@jgSBa(~Q)Xo*c=PSV=XxYnpQ85n6Su6bXD{#*WOl>UOhve3c%c;)PsXp1*!}`TG3y!GI>{YSrBRxLvaM^q1$o%QwIF^eu5b4
0dD_F8(Mzub=|iO5V#n-jsFs8-+|=QS4KtGb!>fDJ8J9;;UmPe09>r8Z(+Mhb7tomC_-
;!lChc>GdjG*$Nx)%VHv0ujCZCiOzcWc1GmE@pI%lgti@G3*}VPCNmDJQTnl@vBoLUuA{6b@lQE;CZLXBgaS+4Gc-
&FrBRlV&N`jes30)lb-rP1LbVVDq|+xu+O9<#N~8qsKbWu3P6}>SD8clsk1f^)<2goR$UHh5WKZyFG73t1OV}5MVSUUMb`R|kQ=!
nDJZQofg==*r(1f|If;QcJX8hCZ&GfO+Plp*_gy#%Q=A9^}YWtDlrrd3AnQeEU5p`Nsc*_?spya)^1xw$I<j9wM`Eu{vD|bu(yCg
laV!}w$Kqn3IT{7pD^k`7)AN8H|cu@0?@`Ltf(`b*$T;I>+5U6ugR9x_a7MfMJFE;76r3b6zkL*PE=C@A9YxVS(E_c}~^Ji|`><g
uH;5wu2<2d>>4%;&NM2`BQO&pUTr*qT~Yqe%lj4GtN$s@6Kn~~~gC+j*{^|Qn4sF!cL$xZul_Yi531_`PI{ZqCo#U?ybqgCUxO)B
cNIrN_v56u3iS}PX}QADEodOd|9lFH3PdOJqHc+C(c4a~JceSK{ZI>)I}$<`fBw}~F5;(j;@U8&#P8FZ6dCR+K~?-
uv!kR#DNa&D`I`-cYGVIAoq#zcBr=!*<Ndh9v&FzB*5v8F_+{ciQ!#Jshw#?(Hc&k?kUJ!Cf?U-m@05R$g8zNL$R{>Z-I3LsmTp-
Q%lzykZpYd3h|pK@A_mY>e0HT;8GqHeL0RQ^%cQ8_uOc)3v7HoM4Z%4t4-FJ6h^<~LZm`6ef~n@F__4$H{mN?-
A$o^aTw;(IXLd#MJ!wO&i;PIWn4A;q)X(+cTsBDc3$E#V2aepYwO=pebj(Pb(0VcFR-Iout&`D^>VX4pB<5E`bANpZgXfRq;9iHU
p0_;=tcPY|r*S5-
7JI^Lwf=zG1f7j{8EpH=5vq9Mu5S93P_zG_FArbBDG9cZW|FzDw}LlM6g6;`lO)>xJztM*?Lz1Mh{sS7wz>VK79Dt*dC1~jTY=^_
;8$I=s_7fPUf6+Dn**Doh%K3}D2tUunt*j7&r5{^=5)OSXMoeNW6=o?Z+;Eqy0C&L%ajs|q!4PPc`)B?S`drp_v%nG1~rYEeP;2)
_RBf6m0)*Kv8?dPc+9#|z0@?^Qb(L_<3ee0f3BS1s5Hob)M*E|PbbtbY>*^RQ~RPvi-CR+Paxs!^ws_OCLotTzq3-(BE-
%w>{ECm4-
`IzD6@#gtd+Huc{Eno@M1El?eN&7_h%3NR1XIq!CZf$^mX*@<R<T@f}0n+8~zMzae>s!zI^sH)~pOP1m^gJoFxg!s{a^0GVgKP)I
mXhDvBT?*ja>|r_nXQ*8-Cv#Zs`pS%WYFT!a5Ca!AZvAJ0+jy=)cg%!qX3<f?&#2uh^{%JrP&ca7w>_DuXbLNXXPbdo5v%#9j;%-
kZxLE+9CV*$LyzIl@zL)ydr$L^IT$B_w|<nzE~HsT{5v>GW8BAMr~#8h<47q<W-1jcEhImhQZ1k=dx<S5ItjQ!CyT6#qXNP-
L$_qzsHTRQ!n3Ys$J7nJC=ETY1MB6<=VILNG`lfftc;-v-B-
4nP2f^W!Diq_q=CMK;FWeicwlo!SCc7=`&)WjdUsKrRAgMi{@Tw<(oNF`22Ue5LoWMwfJ>e-
JNr)fdj9vZux)#fAH7wm_KhND!cMQSU348*R8H?$9v1vw4lSudx<Gagpd~1_9zijS}3xdubFzxz3SBa^UAoUI;YdCy0_?9l|R}`u
8C?;l|6O7cjT6_4C=TeUq<p}<c#Dt*qwXFW^(UXI$exYXhm}E*b)_}tHqXF1;DV~&(@UVsYy0DGRa{{f9li1(E@-
gr(E=ds&VK5PLhn2-<o%4bR-
u)_G<j2Mn9|>IdDxL71yvvsuTbI&OKQb!@(DxCU|^Xc)sO{o~a|S+_b{Qc#FcVc>96bgyK<m4e(1LzBa|H?FvuPq|I&ddERsH!Je
~9NP#rww=-by;S2I6&bx#%wuw|Fb9?8yyftRoz9rAmx95TA7EG@EK)eY<fwmj2gihi+ulVZWkGc~2>D)*qH~4}|K5!-
cfGYV&sTT3zc_Mt^ajE6PS<(&eOQCa_k~N5A?R>=NN1H<Y&!UjAxqH<_*s1QNmGSNVj0W_ajWZro@NSK7#Sq>Xbom<o{aA>^UA(e
xb?a<yo$+nAfUpwI-Fg*!OK+9eR1WuS)X$Cl9IKz>an%Ogofz?!4s0;b0=>l|+4hM1p5IgFn0ifId6fCETjtT1*yT08vTEFSr=7V
uOsgE?OtiepW)q_`%2IJkizivD!|JcIb&CKiFIGJTorYF9R;!-
UNs>Uv=I_{3p{4*s&vkFd>i^8?+rG%o{N&1&QPMl>vEy@<EEbMVd!^GpEVl0g*qyoU8v%A_V&4u|bF0bL3VFUg@<h}zHm-SvU&8G
7lb!n@wl~H0w-
#VNdBa4%aHE9Y$RazT@;mJ4=e}#~koUohCYD>*OX&OY4p+Z><;0%5@~qhE95lFiPk|Nz*6PG=<a3)HmR3OZtpMoGRsi&^U2|J&Ag
4c_KD#`9-h1}z&u2fKBITbIW&JbHrT_W=1H!FY9s
"""
def main():
 raw=zlib.decompress(base64.b85decode(''.join(PAYLOAD.split())))
 assert len(raw)==73054 and hashlib.sha256(raw).hexdigest()=="fa30f9bf3b18c0f76c912ac5205934ac5c77510d9084262a5182c73e3c589e6f"
 files=json.loads(raw);assert len(files)==44
 root=Path(sys.argv[1] if len(sys.argv)>1 else 'RESERVE_FINITE');root.mkdir(parents=True,exist_ok=True)
 for name,text in files.items():
  assert Path(name).name==name
  b=text.encode('utf-8');p=root/name
  if p.exists():assert p.read_bytes()==b,('refusing different existing file',name)
  p.write_bytes(b)
 print('RESERVE_FINITE_SOURCE_RECOVERY_PASS',len(files),len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```
