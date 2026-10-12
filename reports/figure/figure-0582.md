# figure-0582

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# NF93 — physical projective/affine orbit of exact R82

Transaction `711c7648455d7668c880e23b`; branch `[internal-source-reference]`; slot Nimble Finch 93.

## Outcome

**No own110/weak000 body was obtained. No exclusion of the full projective/affine orbit is proved.** The substantive completed results are two rigorously certified finite homogeneous **211 → 312** paths, one creating a stable/saddle pair on each side of the surviving Q merger; a continuous, genuinely mass-coupled projective/affine box in which S≥2 is proved; and five exact rational E240 images. Two images remain clean211, two are the certified birth endpoints, and one is an explicit U1 image outside the certified box with35 positive Q bars. The last image is a fragmentation control, not a cancellation improvement.

Every new body below has **V160/E240/F82, C480**. The inherited substring C434 in the parent's name is not its current complexity. All five own-centroid audits give additionalweak000 and primitivezero000, and all five have **P=[] exactly**.

The complete304496-byte journal was read consecutively through EOF; SHA-256 `5a874d807672babffd7366b6f3b4cb862182bda0c5102a305a90b2bdf0956bc7`. All47 decoded parent source/input units were read completely and checked against their manifest. The required literal parent is `figure-0581`; its canonical version2 JSON payload is83839 bytes with the required SHA-256 `f4d4df1390c5e9bd18047aad823f3cd12e8c85751a66dbfc62ae50f67c779461`. The83059-byte bare Markdown is a different serialization, not a conflicting payload. There is no missing dependency for this result. The earlier NF93 J88 bridge constructions remain separate.

The selected parent is exactly `KH93_C434_R82_G6.txt`,1888 bytes, SHA-256 `9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7`. Its82 integer normals use denominator10^6. Its actual class is211, P[], Q=.11600403115840405; the original stable input facets are7 and18, physical unstable vertex7, and saddle64–104. Facet7 and physical vertex7 are different index spaces.

## Exact rational images and tradeoffs

Short names below have prefix `NF93_R82_ORBIT_` and suffix `_G12`. All facet labels are the unchanged zero-based input-plane labels. Physical vertex labels are the parent's exact canonical vertex ordering, retained by the VF reconstruction.

| Image | Own strict S/U/H | Complete Q depths, except the explicitly expanded outside control | S facets | U1 fixed-surface open cube radius |
|---|---:|---|---|---:|
| DESC | 2/1/1 | .11597156628757335 | 7,18 | 6.112573895818289e-8 |
| BUFFER | 2/1/1 | .11601261582503426 | 7,18 | 9.1552143127765e-6 |
| BIRTH5 | 3/1/2 | .11630796101739801; 1.673801244119621e-9 | 5,7,18 | 5.68731664651741e-9 |
| BIRTH43 | 3/1/2 | .11616939941430654; 6.686788244330881e-10 | 7,18,43 | 5.1337911153237535e-9 |
| U1_OUTSIDE | 36/1/35 | All35 values below | Full list in exact audit | 4.198276032592565e-9 |

These are sufficient cubes for reference-centre motion on each **unchanged image**, not physical-deformation radii, maximum U1 regions, or a proof that all the displayed S/H counts persist throughout them. Compared with the parent's specified U1 radius7.493732680351959e-6, BUFFER gains about22% in this certificate while slightly worsening Q. DESC improves Q only modestly and loses substantial U1 clearance. Neither dominates the parent in all respects.

The exact source returns full Fraction centroids and volumes, not nominal zeros or affine transports. Decimal presentations are:

| Image | Actual uniform volume | Actual own centroid |
|---|---:|---|
| DESC | 1.712679226167314 | (.024970586656380907, .0032128090537140485, −.00679042209322848) |
| BUFFER | 1.7126789018395545 | (.02496860832654284, .0032129804170972776, −.006793490787629793) |
| BIRTH5 | 1.7127060046564813 | (.025095413959664973, .003055954722611527, −.006977692227612054) |
| BIRTH43 | 1.7126935071700207 | (.025035117849723353, .0031224246479577772, −.006921872708231003) |
| U1_OUTSIDE | 1.7405863422077006 | (.08117590383245513, .01207955723738624, −.05013280630287807) |

The parent coordinate fractions have maximum numerator/denominator bit length60; these maps give80–81. Maximum own-centroid denominator bit lengths are respectively22533,22591,21891,22272 for DESC,BUFFER,BIRTH5,U1_OUTSIDE; no coordinate-complexity improvement is claimed. The recovery prints the complete exact fractions.

For U1_OUTSIDE, **all35 positive Q depths** are the following decimal representations. No small tail is discarded:

```json
[0.08476472738855413,0.020737108606429418,0.0026239125802776154,0.0021253224906611482,0.0020685958563856667,0.0017406589238149737,0.0015431220816939273,0.0014587276132103494,0.0012843370717517178,0.001266766681619047,0.001169242737890671,0.0011660671798142436,0.0010779430017384157,0.0003503963767614203,0.0003198684203372162,0.00029914180323535036,0.0002768707323121093,0.00025837087603793757,0.0002520886416865099,0.00020258864486663445,0.00015806632316820268,0.00012064888260583809,0.00010813372750382192,6.531782119988569e-05,4.097896181951469e-05,3.235916542946444e-05,1.4467652858539145e-05,9.170931147579533e-06,7.0483783337899796e-06,5.885240421052415e-06,1.48705583356356e-06,1.3761897162796854e-06,1.0462244395173962e-06,6.568774639270747e-08,1.7627904160552804e-09]
```

## Actual mass coupling and numerical search

For every original vertex x_i, put d_i=1+b·x_i and v_i=x_i/d_i. With the parent's outward triangulated boundary and W_abc=det(x_a,x_b,x_c)>0,

V_b = (1/6) Σ W_abc/(d_a d_b d_c),

g_b = [Σ W_abc(v_a+v_b+v_c)/(d_a d_b d_c)] / [4 Σ W_abc/(d_a d_b d_c)].

The uniformly filled final body is A T_b(K), with volume det(A)V_b and centroid A g_b. Its centred primal points are A(v_i−g_b); its centred polar vertices are

A^(-T)(Y_i+b) / [1−(Y_i+b)·g_b].

The implementation uses these coupled quantities at every evaluation. It does not push the old uniform density forward, centre at the old centroid, or optimize unrelated primal/polar metrics. Positive d_i at all original vertices and invertible A preserve all maximal facets and true edges.

The numerical search used b∈R³ and a determinant-one upper-triangular A with two log-diagonal and three shear parameters. This is the full normalized physical freedom modulo output rotations, translations and scale, not an affine-only slice. Exact freezes round the actual A and b entries to10^-12; their exact determinants are positive but need not equal1. The final volume is therefore integrated, not inherited.

The source preserves all producing and exploratory units, their starting inputs, seeds and nondefault parameters in `RUNS.json`. The five exact nominees were obtained as follows: DESC used actual-U1/S2-constrained Q descent, eight completed SLSQP iterations; BUFFER used common witness clearance with Q-sum cap .2, three iterations; BIRTH5 and BIRTH43 targeted outgoing polar chords7→5 and7→43 while allowing the selected extra S carrier, respectively three and five iterations; U1_OUTSIDE maximized the unwanted root7's outgoing angular score under actual-U1 constraints, eight iterations. The original root7 did not disappear in the outside control.

Broader completed tests included13 of24 originally requested joint-hinge starts,4 weighted-depth starts,6 Q-only depth starts,8 Q-only angular starts,6 square-root-depth starts,80 U1-preserving whole-polar-tree iterations and160 S1-only tree iterations. Additional metric outer relaxations,10 fixed-b witness-cell tests, temporary-U2 policies, and reconsolidation attempts are preserved with their exact scopes. They found no valid110; their failures are not family exclusions. Some SLSQP outputs were infeasible, including an apparent S1/U2 row with negative projective denominators. It is explicitly rejected, not treated as a body. A reported solver success is never an exact endpoint certificate.

The initial eight-variable analytic-gradient check against central three-point differences gave maximum absolute difference1.372345015404619e-10. This verifies that specified numerical check, not global smoothness at witness/persistence changes. The numerical bar helper has a1e-14 nomination cutoff; exact acceptance and all displayed positive-bar lists use the GMP routine without a cutoff.

## Two fully certified finite birth paths

For each birth endpoint separately, define the **rational** physical path

b(t)=t b_1, A(t)=I+t(A_1−I), 0≤t≤1,

using its literal map below. This is not linear interpolation in the optimizer's log-diagonal coordinates. Outward-rounded dyadic interval arithmetic at64 bits, including derivative and midpoint enclosures, certifies the entire interval. Both complete covers use exactly

[0,1/2], [1/2,3/4], [3/4,7/8], [7/8,15/16], [15/16,1].

On both paths physical U7 remains the unique strict U, with no weak U; S7 and S18 remain strict; original H64–104 remains strict; every other old facet/edge is explicitly excluded from weak equilibrium except the single designated birth. The proof checks the full true-edge graph, not just root labels or a few sampled times.

For BIRTH5, the unique event lies in

1260405993/4294967296 < t_5 < 630202999/2147483648,

approximately .293461139. Before it the own class is211/weak000; after it,312/weak000. At the event the strict census is211 and the additional weak census is101: facet5 and edge28–73 are weak, not strict. A strictly negative interval derivative of the event numerator proves uniqueness. No primitivezero000 assertion is made for every intermediate t; primitivezero000 is separately checked at the rational endpoints.

At t=1 the new stable facet is the genuine quadrilateral

5: [28,73,67,33].

Its new saddle is28–73, dual edge5–7. Exact elder tracing gives new Q branch5→7, while the surviving main branch is7→18 at dual death43–55. Thus this birth occurs inside the **junior** stable basin; it does not cancel that basin.

For BIRTH43, the unique event lies in

1741378287/4294967296 < t_43 < 435344573/1073741824,

approximately .405446228. The same211→312 and event weak101 statements hold, now for facet43 and edge55–114. The genuine new stable octagon is

43: [8,10,55,114,104,64,58,49].

It contains both the old saddle edge64–104 and the new saddle edge55–114. The new dual saddle is43–61. Exact elder tracing gives43→18 at this new death; the original branch7→18 still dies at43–55. This birth occurs on the **elder** side of the surviving merger. It supplies a real two-saddle intermediate with a stable carrier incident to both saddles, not an alleged relocation or annihilation that has not occurred.

The preserved stable carriers common to both paths are

7: [16,128,73,28,19,37],

18: [0,4,6,22,42,1,3,13,34,30,43,39,54,97,88,147,126,134,158,137,9,5].

The interval proof uses the actual projective homogeneous mass at every t. For an edge to be a strict saddle, the directed radial scores at both endpoints of the physical edge and both endpoints of its dual edge must all be negative. The two existing/new saddle tests and a positive exclusion witness for every other true edge give the full path census. No triangulation diagonal is treated as an edge.

## Exact finite physical-orbit obstruction

For **every real3×3 A and real b** satisfying the closed bounds

||b||∞ ≤ 1/256, max_ij |A_ij−δ_ij| ≤ 1/1024,

the actual uniformly filled image has at least two strict stable facets, specifically7 and18. Hence no own110 lies in this box, irrespective of how many other critical points appear. This is a physical projective/affine box, not a fixed-surface reference-centre cube or a fixed witness-policy optimizer failure.

The certificate integrates an outward interval enclosure of g_b over positive transformed tetrahedra. Write s_i=Y_i+b and δ=Y_j−Y_i. The sign of the outgoing polar score is the sign of

N_ij = s_i^T H [(1−s_i·g_b)δ + (δ·g_b)s_i], H=(A^T A)^(-1).

If a=max|A−I|, then ||A−I||₂≤3a<1 and ||H−I||₂≤κ=(1−3a)^(-2)−1. The interval calculation bounds the Euclidean part above by a negative rational number and proves that its squared magnitude exceeds κ² times the two relevant squared-norm bounds. All28 adjacent guards for facets7 and18 pass strictly, as do projective denominator and centred-support positivity. This establishes stable-facet persistence for every parameter in the box, using the image's own mass.

Larger boxes tested by this particular interval bound did not certify; that is not evidence that they contain110. Nor is the certified box proved to contain an entire U1 component. U1_OUTSIDE explicitly retains ownU1 outside it, but has35 positive Q bars. The full orbit outside the stated box remains open.

## Why centroid transport is materially wrong here

On the exact DESC body, the proper own census is211/weak000. Evaluating the **same geometric image** at either deliberately incorrect centre A g_parent or A g_parent/(1+b·g_parent) instead gives reference(7,5,10)/weak000. The first wrong centre differs from the actual centroid by approximately

(−7.645909969675402e−6, 3.541008485018762e−6, 7.730341362862718e−6).

Its four spurious reference P depths range down to1.3324635224966783e−13. The complete exact reference P/Q lists are regenerated and explicitly labelled reference, with the actual mass retained separately. These are not additional homogeneous bodies and are never used for acceptance.

## Scope and most useful continuation

The remaining main Q basin has **not** been removed: S7 and S18 survive all five selected endpoints. The two certified birth paths are useful because they demonstrate actual, weak-event-resolved changes to the critical-point structure while retaining U1 and E240, on opposite sides of the surviving Q merger. They also show why enforcing the original two-S mask suppresses relevant finite events. The optimization histories themselves, unlike the two specified rational paths, are not certified continuous paths.

A concrete next carrier route in the unchanged dual graph is7–13–43, ending at the old death edge43–55. The local target13 probe did not complete that transfer. BIRTH43 is a reproducible two-saddle seed for a genuine saddle-carrier exchange; deleting its small new bar alone would merely undo its birth. The full orbit outside the certified box is not excluded. A distinct finite escape, rather than free motion of all82 old supports, is to append at most three new physical halfspaces after a selected projectivity. Any surviving full-dimensional intersection then has F≤85 and E≤3F−6≤249. No such three-plane completion was executed here, and the facet bound by itself proves no cancellation.

## Literal rational maps

In the following block **every displayed entry of b and A is divided by10^12**. These are complete maps applied to the selected parent's raw coordinates, with no preliminary translation. Their fraction-form serialization in `MAPS.json` is checked by the recovery.

```json
[{"name":"NF93_R82_ORBIT_DESC_G12","b":[-7945055,14507706,10742061],"A":[[999997404035,887104,-8837949],[0,1000009432554,4022518],[0,0,999993163482]]},{"name":"NF93_R82_ORBIT_BUFFER_G12","b":[-4641661,14544682,15933638],"A":[[999999876029,9471659,-318407],[0,1000000829662,-9622288],[0,0,999999294309]]},{"name":"NF93_R82_ORBIT_BIRTH5_G12","b":[-147797014,545857376,311897092],"A":[[1000063128856,304953370,22742840],[0,999957871330,-199814308],[0,0,999979002915]]},{"name":"NF93_R82_ORBIT_BIRTH43_G12","b":[-72670400,326347079,222805411],"A":[[1000040061449,176516264,-5973064],[0,999988291884,-143098423],[0,0,999971647940]]},{"name":"NF93_R82_ORBIT_U1_OUTSIDE_G12","b":[-50594856906,1750709208,48354558430],"A":[[1005188357181,12107170655,-2065155907],[0,996463624128,-461710315],[0,0,998369031077]]}]
```

## Durable source-only reconstruction

Save the complete capsule below as `RECOVER_NF93_R82.py`, then run:

```sh
python RECOVER_NF93_R82.py
cd NF93_R82_PROJECTIVE
python REPLAY_NF93_R82.py
```

Exact replay needs Python3.11+ and a C++17 compiler with GMP C++ headers/libraries. The observed environment was CPython3.13.5, g++14.2.0 and GMP6.3.0. Optional numerical producers use NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, float64, one Torch thread, OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1.

The capsule has39 entries: selected unchanged parent hull/census sources and literal R82 input, every new scientific source unit, all five exact maps, numerical checkpoints, producing/search parameters and expected hashes. It requires neither the originating sandbox nor the old C622 archive. It extracts complete readable sources; the exact verifier is the parent's existing GMP engine with its supplied maximal-VF frontend, not a new independent verifier.

The final capsule was decoded into a clean directory and **all35 exact output identities matched** after source-only reconstruction, including both complete path covers, event isolations, the physical box, reference controls and exact elder traces. This is a same-engine reconstruction check, not an independent physics implementation or a promise of floating optimizer portability.

Expected markers:

`NF93_R82_SOURCE_RECOVERY_PASS 39 109260 d15e74e10dba367e039a9259862ebe900906b217fcb73be63576863393064a11`

`NF93_R82_PROJECTIVE_EXACT_AND_TWO_BIRTH_PATHS_PASS_NO_110 35`

Capsule:39452 bytes, SHA-256 `0535d774fe4b7f3a6ec5915be24d524a7e5f3ca3a940349f30896ae41b191ff4`.

Final exact manifest:4690 bytes, SHA-256 `a7ac436049181e0a832f997c952f95e67577da559f27a7297dc6200a1737b09b`.

The driver also supports individual stages `parent`, `DESC`, `BUFFER`, `BIRTH5`, `BIRTH43`, `U1_OUTSIDE`, `box`, `cover5`, `event5`, `cover43`, `event43`, `reference`, `traces`, `verify`; splitting stages does not change the inputs. The program writes full exact volumes, centroids, maximal facets, true edges, S/U/H/weak lists and every positive P/Q bar. All continuation-critical data and complete producing units are in this literal capsule.

```python
# NF93 R82 projective recovery: source/input capsule, no external research files.
import base64,lzma,json,hashlib,sys
from pathlib import Path
DATA=r'''
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;i}7b7+nB8h=iqrocag;lgCWk53KKV?E}0DXg<x1OU)*l#M5Ey(60j9RGxn^SxB5x#mjNv;O^R(!FRW82z|Yr*XE{s
vIWIh0Ilz8k#aU^Hd#6WBC<SAxE)bQt!2dpzqC!O;efv<FVGEQQ;5I{k}eVm%<qJxa!p+Y*oUZaC#+8bj%L{I?zH5R3&>~Dn+?ur2F~&Xps*;IVxn6-)8qMQ
*h0M?>K*`FJb{}ww+~-JykO10MhnPH+78O5nHVvi&L=Y6q)VTHKxm0<H;u0L@)75&W17<F>*e*~U%c=Fv$QdFl@W`gS^$!HmX4M|@e3zS4_oPcuXlrv`xWnd
O^PJ!s@cY37M1Jh4I6v|z|E-)9*|m<iTyNRw>*^J_Ued~8h~A>5@ADCfuvLLbTu~uZW^X6QsY{O%39U}Jt$aYi3($@fGyFKA4Yzk!iyXT!#yw=|NW_T)OAkU
NmVY(9a^!qHi{#ipmcFO8#d^VHD3jKK`@fYO=7<ut0>5TfbG48!npQ7AICOm*EKUCM^ako2A(_4%c8;zm#}r7jKC*H!D!DC`N9^Zka*z*g^2yZd}rs&3+Aim
92yit11|i_V7SpIeQ}{%X6#e-Jd9Bikh22W8DY7Iqob6FfNi=^gDyuS7%r)Y1p!$h&^ed>sRM3-h*4rCAajEKw!`%?yOw_=26t5hdy}K7C{D$24_D=f$7LEH
TG@0i>-4`KCuM_f=A&Mih+~f8Tww{MNtG(^n0bO2BCjf$D+V6A0HP|3fa>3_$>8H_pn@)~OtCrP)B9#eyG?@)?jZjd(1f@`C%VVCv=jSm{B%axDaf@1y?W(%
SC=+N8x?<PcV}(?H9nE_1mT{v6DcrH+h}HC$}K=@^Ac>8btRUrD9xeo4CA}^Hm3gJ!<wVBH0*k}Z;zBw;)uAtE6;32N;*-70Xth^RKlm<*IASt#97R(U}MtX
9J8f*$G33Z>#Y~3j0`Xqslsm{&^*PIZz1Oyt&0Ze@_ZmNiI$6m7bb*I{zffr8vu$h#34dZXOJUQ0vgRW#}Lpy$2n4G@3FT#Hs$4}0z5JfLc1n=*U9NNqn)RM
eH4by<0hk+k;%_F1D9oCV`0fT>V@rD-p8%O(bNCu#X~N!+lcbYj+?n_B5pR<8PbR50Mx;l1eD^6iz-(rdi}n?<7hw45sh$p0kzFh|MM!oLt%RMZFvNx*~~F{
Y6kP5EHpVbER0aj?8D0w+4T8ZxEn_bt;WAW7A^(bnqC<XImetN)t~>p!u4-qUuT=iAS85X#?V9$HTcxIK<c|tkztoCtdd7V*?2|ey`^R384y}H(vc{45|*~^
+1;YRp3~19H-sbCXH3g*GjJ`mn2WheToL}UMseo>_qTIq9wJ#H0;_ls#P@9Lc^_XI+LV>B&FK3a=Aw9Jswl<I+MFz|d9P}K^10>NLVQ51*&MZW1*L7H+}j)m
)|(qLp6EDC7K<Q?X+$h$oD{ZFr)r(3Km&JJNF<n)fv@)(mDzPO4`t=lO$$&FL-{>pi&R3qvmCF{0&U~jV$4zS?nLlHBR)I=4t7CJOGFLX<06D0))btI=i}x?
-({K|`ILAe<+jg@W231moPV+JfFr_Rux=y{kYYi}liw{Uzg<SUw)L}@blr*;=U}Z3fY`J$;LBf94)fYq8RL43y{{COiopSg4(TvfAHqpB<pT{UP2Qxv&zn_0
(v_71D?3B*q~RS~zZlMz0t&t^EDpZ!!LDOypgGDANBP>zQeGpZeC<8yb{|A6CoDaGVLeAsOS9mEZa8BV+3ccw_p51W;X!Bh96P>oHJ`~<ldK6vn)K<G^~vyR
i9UNJ#}MQI95_aJ=lqKFa>&k)fbMs2&us#pWrd-JB<)%u`Rc+?;Ul+=!Yt@Gye+&nh-NK)*W(rD$6aBTbdIP|(P}Z*ZJ`fe+O8<j%Ps*Re#<bl;k0+J_?+7(
WAlrv1iL1Ls5zD1w1NLyGEUoG`u7)e)$-COU32#3W4Z|?qbulo%Ngcocc_lh64?yyTLrKjoA7O_&p;6CmLI}6^V&^*#-Zwf%>!IQjN$^Rr8{yR(~w;5z+k}u
91l^6Otx>ar{X4@FYj^?WFP=%_!|?52q2c0qG5YO7Yq{+zMw61bRk-3o3S2*9wGT7KonS}#<}Hk2$J@H>HN~7d?FmiV7n`xuA_UA_!8!0(55KL2G2KNRiXqd
dB=~8OBKPeFZq03COHS;dkeJjuH!Dl`rLDe{{)*}OA=tx%gOiEgXP2DK`v6AWL_M&*#eN>P82|wph5i0vc$;3*m^S4rT<(M-!SRcFxXO*yMryX)m0`A!e~m1
$zsN+qWz$wa|kWIkOzpxq*<4t1JHW;yxSu2uWKnfJ?|{}hNH@I8kWd{)l}&%+bs`>V<Bts-!77w5LyZ@cqI|c*|cjJ-Y8Bf=o%3|fpRal;&^JM`~NgyWnaM{
hvbp^U1r#C+m|`1*zm%Ca*miiZ-P0-`YTNyi?a`ha5Q6^!Oa{K=L|4Upwj3FS>Y--x3j?Q!3klGCWb8RZy_0?b;u0xj*imbPsFL2JUn{F&P%%K46E@kKmE7A
5N&-q)`k7Dt;xD57{FO~EAvL4n{g)Xc`LWyn;1@}r(q_Rv4B!f!C6g#wOLmnc#&=2NcQv}WGmmWOG9u(l+mo`JsB{37tEB|tA=3p$wMD{Orrwd>wV6WXEJ86
1hYf-`7C08f-nPaam;e;CL8?&LXBXzDi8fYl`v6yyf5hOPf`{RX+@t3jA3S%3o(8%EWY40<RW`EzIjhiw27q<{MAs4|Ih*gWy#!pb&q0GkkwuIV&xxF=5!I2
oM$&-)vMApE3**RXp8VP=OoOb)U>N3M~DOIX}!FyQpn<8i<W25Gj76LR|yb&#+{VQ5CfKw2TS8}$EHE2M1m#=_h<W<b_QdVgcd1H=1Lsua6h56jCRwS(oQ_V
bOM8WDz?T0Wg%vuCT(*7EeRCK1R#3ylfA*)I;)&~hS^o+_~LbsAGWlEP36pCPU-iLamVj%&yo$aMS>vCTw0SN`nnc;%>XJyZ3!v~$M41H0%wMR`HZI*KgCtr
jKkfbOWEG9BOpD)f;_#%qz`zVtRTQef&s(>K;-bGy~%>SGy2_tUvGh{?v`2X!Pt1W(K(Lq!=AAFy5(Hgtkx+t_+P!zKg;0JBFH&H8QevvSK{#&iZvt_jhEK7
%}PE(s_4|9nRZ46rbd3hNgB@%aTBed2SFGzs6CAceGTID?xn%AL^W=cTbxv2_{rZ*l25k(><!7dcdL>(+mD^Vj;w0XL+8C2s+(1e78EoUBSNRjn*=R$Vd`m0
FMFzn$Ldh4sA5t5p=-eM(l+CeeMU1$tkjJ>eJSKAS2cS4B#ja&xvVoyxcK(+Gz9-XCqATh4d=PpXE;+8BWT2uU3d4Kj89eEAxjcRDYb^fye%XZQNS7w4_cq0
x*0*C@e??3I)ZvD;(e5h85(1BysfmVb0QM}ZT6~pNtus(#MmVy)R>lYoWuypn6gJCqkJ$F;a4KEmig7`34DZiRXv)#I>IPedy6#JywQAkV7n6$<)zuO(pm36
vEolsBUs{@rb>_2SD6<bp>}_9pnGsjoBn3xcXg;Ll!-~nx%q<$Pb6$_*3u93`{3F8`^k0*HVX#RVl7rECS{tIyPb-QWF$sM`iUFj3?_N5)sMX7hda04!REm0
S_m%%y9;|yv7!lQbG{(GeMmsD5wd=MlAhe%qqy3T`|O0x9{4gv@bx=H2dVoVxg4L}&ynF*(Qva7{=ZDigidsl&KH~r*v{UEbr0=h&ChcFOh8^Gk-2;~BI}eq
nrq<yA_xcT{;0(*n}${Qn+jwZjJ0MVe<O=FBj+)t9h?#|Nc_8)sEEWRl@WGBR=Q6wpbAN(VqV?^3HHx(wfbVy*<JP8PS<gPjXW3wsYqjAkY=KP*iGtw#R<+(
7!EF|D57uQF$&J#HjN*dbdtriixVGXs(=zkB*;#3?<e<GizsZ_Kn@1>V1=DAorEMKfafZ(oLMcd^=fdqAg9)SkjT|Uu={Zw$xQ5<V!lbQzSnF(SV3mXp^7Z*
fS!T@&TaUnCMj$qI4^-f$CQcZEng##N@@MT=42jDV1a@e#Si*g(kapk+lvPJQZ|LMS=<z4u}%Yh%B^xok9T5iSkw1;=Jm0ux5*6r3{r*H4abwVy+eiq?fm2J
f%1GcfK%b@gg&cwmTUuVn?1y8!N;YgmNuE3HXnZB%ed?~U;pL3%;qfc42gCO4doh!i#`7LrMMl9%GFG4RD-No^m)Mc?avf+9MB$SAl<wMM+hNXfqr$=GESWF
zA-cCb32w<aeGH`fqtOynM_d<8<Oztt21}xj-awk8->zBsrGsTstW@U7wPhIk-wK69cD$0@%$HdlHmVdyX8v+ow)D;)E9Q|8a3;5YcO(bL;`wnZh-aA2VIjr
kdm0|_lpXxcjgQ#cKH=Qg*6HbPlC`3UW2IQDJ40o$-L6;3v2#NjvZ+s2lsxPN=vM953gFW2F1uefEqf1v*~^;65u;Kxr+5*(Q?NWPj*3a?Xj^pxn5`<>fc5F
w6JSZh{;&0Yb?eSWgEBMkC(z>2PPoRimUI=sJK;Sj`1ws8?=XIfw?%oU5ee4pULnhMjx3(Bh{tM=N%Tj2}AyX^x(*q)hXsSqe7*66g7<cEGS57ai3%K&kXJ0
a+beKclmN6DRIY<iAK>b$sLVyhA$yzP{)y89w&V~@MJBxfhdv2T(b#i72)^av?{!td!UHbaC4)M5q1TtQU<YIyQ>Bww=R}8N*V-uXZzXnU`~W5%29tLvpPeZ
3eVyUm#@EXR}mn;)<(m3`rmhVgjm`VF8FpIc6`9ax+@(>U4Ckdj7ad><(I&*xfG}%H+Ik8wrtp=*1@~!lp-R-7r~x_w$@dw6W)A8EHqsmMcmD|Y<Y}V@oF}8
JRHI)*fdZ$cZIuca*Gvin*CG4_KV`{D%x-EpzU}Cb~5@~T?5fHLmT4oFqTDnrF8V%Z3Ev+9pE;+Z5tGsVv9z$XpgsZNL8FMGZJP*l&Gl@lHJ4=u<tSPjMkZY
Nf)NE18bEbF|^zf!CI9~f8RX?fx2AWf}<{KJ3O$3I<uE&VE}^iiR&gVaR5`v6no~`4;;xug_`@&{9Pqbq`-HIm_Hu|t1Uuz^v3K(rAi2Nu+VqV>f?F9?-%uc
ZD9Q9Bl7wu4s0FFbDWR($c5B`LnMvO9@liFt<|+cT~yapdf;n!$~@k*fTnbkTo6RnvGg;Ck%v_jI?rINX4M9RL!|)pHn`=`fvQ2%rDQL-?lnNL9zV(TimNoS
8uDLCWDLxweEEq#D)%3bDAnGTVaX?Ekg>&2WE)q-l-dZYmCR+@FyL8qi&4p2(|Izq8Dm3@8<De)#kE&fF%8wjosch~S3q~CJnuN)=Iyx5s^DugaM51hj(*UN
#^ADo*iOJCGl?~<5v@+CS>lhNgH#ZbadHw+vE{}xh&lt|88}1THp53)=-_I(((ve08|y_1Sc7+E;1^d;s4q8%`Vs2ED;csscv)+&{$|9O|0B)T(X31rwt6m;
Dt8{<#|J>uH*=n7Bq8PVbdWs(5zrCvY?G`xj=KJXY}=S^3vaApLsqIBQ^}3iO~*j~nj+z0_E<5aF+HsaHWZ~<#jpj{=H-B15z>|F%PdR262Iy!l;FScFF@&H
kUI=JlUt9cF4=C*i&4S{E$|9l|2Az`y}-O1?Z+<uQ}{<^k;!byIO`=Lr$+K3LP_qu#+5a9;oR_(3t|#rFrtX4d^Z)_o=sn|ga_-u>TCXyMqDp!HXiG{rM>#z
gyBkKr_`@)?0JK4{8e;y^DYm|*%KsJ4B53lDyh9}iBbdWo+CpeIrY`pI_yaP!AX!i(!hO@{p^uIRp)638Z%TuvL9h83Qi73Rv|a^`tTuvMj_s02-Z|SCPWZT
{w!Z7ZM+PvE%R8(tvxX_K=W-@5YAdFYJ<)to(_-SF!v#UxN=LR*k$J}8fTzFo?#B(=I^>*%G)U#b@L0`T?P7moOWg5UaycJL5NTTz)B1OYn!ff<dDZctXGeZ
vk}GIV~Y!=PMpfPtXgQ!ko{D|MMy+X)%@-*1Je#P=v<?X{KszeK<3*t>dfdze~BRkqyiELIE7HX48b7sh*0<*{+)`Qk>i=Vsjue;1A#V8#BRkR*vTuk{}!^<
)M5QR>b;eP*KyG(L3RJFFUU@0e{qB^flVh=$*&68-T0!`Rg0osRBbzby835Z#xEAr!iDCFe?lh@MQM%E4sC=aCx}7+?p=}t6mCH@#fZn=cWWWD2(TyzcGTHh
64Ez6-3j6kd$b!LwvEk)?0Xg7F#0hDz6nwTELQE>k>8lydl*Dy1?rxK6W*gdId5owRbVf$WGgjyLL`?Glt|xL5J@_Rj8&7FQlbrv^y=QJZfOFbUz*^hFPYsQ
m=VQut8X$enS=t9kxXu@Ve&zAo0K?k0v5cNSlxHLF~d7ZZP!H4DP#lh3;5UzkvHqK@SYUmi1krA2j!u?IwTph8V@q?yuMfma}_b0M>;h<WRxih8@fJTqr^mF
;3VOJN`hBnoZ9x@_<yKwQmUCnkO3LNBN=!ystYR^_Q+sXGBbF(aWd7H+LpwVL-QLpy6CqD&XEB$HoCrMpKp6?5#DMJp*i4c+L`qouK#7(7H5oOc%QH2P;h3;
Upr;;XoQ8Sij;$$HJRhTU8JNqAfd>9MxNFlAU&d)jTp3L_7L`B#FC=hfW%f?gU``v)<&LG80eO@JEC&weMMPK<xn-+Jc@;I;y$|;`8+$jTQ=UWF){s#B|4;A
9Y%RS;aXEYTWnTAR_k62^l%SoJ^a8mvr>9EkX?mI(Qmxuw4%DhTTd+oizvfwagjP!{P?}zuU>3$1vxjdZ?Z}iAk7}`w5rNDz-b_%ngf4$yID<l@*NGkz+o_w
S(esD5K$P9G*48xB=WiWsja~tt65QhNzVW%Zsi*|Gh3d^FG@K?Dz|yV0q#&t_5d7#x6Zr#m~EKx0vs)wPQ)D?k(}~Ap4GHB5`Xr;$dp(Q;KK?s>LTSnvXC2*
)?<4VGHv$!hFqfA`5De72Kf|yQ(TcUZTSuoSEX+d`mr#y&%5Veg4Ba|_2<^k+HlQ5(D2qZ1H>r*^E0LM98#$14guvT?UKEmjau8uK!3tTE<?AY5|iR)(ggWb
J~)WIlR`k^8adCVr~zH;wkMi~XQUvQa;NVgU3A1q7}pDK^3f2XJxeRi7+<|z3G0EiQCBT|Roa<whpOBW4FS#&7=Su;9frMk;*x_+8z#)uW2YvSP8gcL2zvKX
@4#ewOk2%J<_qbR754B+djaR?cK$otk>Z*E?)D-eWjwz)=nz0l1}~hW8p@2Up5)bO9$|)6pjK6*=h8M&HA+7tR}BfVkLF}&`&EoL@7E3LB~|iO;VcuOk~B00
UNUaKb}bdLh@38Dmm+d#eR~>rqN##d7Hf?%nC$SRCt=Fi1$OA@*=$P@ms@`2WzTRogFtnQWoFpwa}^5i_(h8$_Z3I4$NAewYc?It$A_8<6z%-nncPFkw<ftf
57oZZRmoN**(=FV^Cl#3;-E(M4zyc>Se&56{uSo?;B2yt69iE^hr{8TH}`g+I0}Z{c_t1bf${iq4;<bf&wX$AF|jqrpIREhAusIB^-%#`&2|K$l0J4iv~a{d
%*bu`v14g1{f2EgPAfWunn1M9QRlwf6qmwH*!ZBP`|oY4D9AJEnV>S%Vg(bA&yN~-6og(T-k0kXfoKApSdb8MU<oSCD=P*jRU`%@NJ#;!9C(6CqI7T&D7gUV
ue#5%){|y{Q^4sTt1QU#YCFAs+Yxj~#%Lc)Ei}8>wN&~LHbT_wbhpm+HjUP$#t%nI=7@d|!i<wlMBs4RaH5MEZf6DoE}Z7K6BP`vqLlIZWpu#SiF@uD7<x&}
p-{|5Q&=rY?uth{-5$HJlQ9vAVmp*@@S@vSW1`O-O^NP^<-R}PM)Axa;6~dG|2e%|?MeM`jsIGe{~gZO%(8x;TAWp?QLToa^r;Rjrf*596)+~t__6!njU_VD
_o65~S0bN?qz``Yk(&RxUFak%d>>Pv$NA&RNwrA<s$)r~0%Y==H<sA#^<V`j18CZ!07xh{4l8BB0@%!!j!~Sr07gUyLH@s93S6OIY%Qn1?ln18n^@9Heqq7!
AVC<VzXwULpm!M6D~s+=)P!b+w3t>rS_U3h$ZfR=L>pz0*(MpCxMKj`H+N|X-^MUUE~ezkT-GzY1D*)nX;m4TrS8eC(Mu||KLD-C$fRNKY--UWziF#V;`v-o
=IK%WM$^iKZ;ppr*(ixgvkap-Ksodo-`JNwNdYhT*_+vZ-NHH3*}e}CHYvX`|H&-S*}2v|+?m$3{aapOTFjC7?W%s8P3*LUC=^Q%@zSbIEY!1z#Dxf(<D(LO
!U??|CnAUVF=+#;uMDA%5jZ#H>pNMVPv6LTJZUNWueag(590P^Nt`+d#?j=d^{%ggBH`zecK<^B?wgqegqtM%_<-ERg%IX>(zPf$zd)R_e+M|FIR$ZLR$)xO
3tF)(aq)P34~fl|QPr_(r>!>6TB%pt(JI_Wg~SK;l5Yh;*W&=MKfukZ^)koqLn%NVep#|;G}U)uceYifu)r3XvsaYA#qX6jeY`}IcC{;i=m>v2qr>3314&9s
-`9L=4b|a~kek9pn&bnRomr@gUP@w+=Z8jrIJ~_rzD2Y=^_2>>KI>}Tzi@=-rT(ZouH}~Weipk#!2uEC^(%gHYsTN5xM~@FFvjH6{SYvhjwoD56$F3D(zY*>
mzHAZS;^nC;Xp8lEEEq(YYbwH{FL;+gz%olV;j-fx#Ka>im+CMZkz_heN^AYc*~s9<rj0js;<)zWc$~@M~MYDxw$L#n6Ft84unOQV%$ey8MW=F1S((_a^A*x
OsA7Cs`QS6I;`<r>wPHOFt6@SN{i?AuTkl$EW<4Z#|P_VBqcpmt-R5x*ZATdi<YI;4H|`;7Dh<)8muN|#W5Joi4^aA3BiQY?GLr}QTzZzteqFAZ2)7IA>d~M
%JIjAzeZW@$|pqIA<Oojb@1{e0o3gT?yxN|IaKN1;vrcyiL}g)Hp)^qGR8N*r|)FLF)STxrY1q1^_O5(1Y>e3+f=RdV>i-|Dp;Sh1<XdCW?^MfyWB0ae83TN
ZK@^h=;;80D%b|L;v5sllbD)N<{P9nYS=M<7_Z00&+FcPQ7<i(5_ojd0`F-xztoP`qpvV@vvRTPz#yJQuGeOH2&|9S(IZ~bW4!4EXq_4<R57K6(<`)q&ZNm3
=8`ETR?C47BAGUOGt&TC4b7+<IRKCy;oYBV_h{5J<^<0b-v+Qc2+$W?WdG<sKd+dfAPg2k@ETc-(ID2-GUc*MvIFBIEXzR@T}4)Pj0FQ!UdwKfKwO)<4O%gN
Q!on_BWg+7Ri?bfLz79TEwI$H@kresy#_UkmnlkLJ;Ryp+zFjkTYZvTcG~=%7}I<OzMCU*TH-)u?i9d%P?bcWz=6*b!-`B;yM_won)9ucE|D+|Xz3K!unF@i
5U=fLLk|N&OKi+eldv#SP*&VSefy-x)cQhEH9WjvtelZrT4Jd3UM+!uWvqe1`8g2}#Y~{D{y6Qe0&6-$n~85d740}YIM!YNR1>7XanGB6^6@>M5E+nOn@ltD
GpFh&obm!m-7nd<Tz)~=w8BW&pa=3AmyuFSwCQhJM3hWN*JVZ^VYn&kRFfk(<y&(hd2)LkN`g!{jNTc+%N3jni<ynAxa7yj5w1SE%upT#GNN8zqS@Q$%?sI7
14uGPHG}3Ff?F6^6f{ar_Ln~MEH4Juz{4lHl01yQ1aNNmH~KqYqwaUh>miFhq^NuG1l5OnB*|^UJRtFsf~Byq*8JL0#vz1@$tbJ(0TxCmP{=OfDn5)OX=^&S
({Nm}b)2=k6|hB*kQ!d%*|0PX)ap&+hpK(xK0SfO$RBNkxLF%r_g73cK2^r02JM}N{V|w=(Kq*5Ioz*}AvL@Xk(Js3?)zoB1q}rr6U7WDGg#h9Ndk|?_ZYPA
Wk1P~MOoxovM1Gtz?g`|6+#$5DN1h-qz^9?`CF@)2gy2dDWrR&UA&*JV9O|S{t0>_N_=5~eO(#&bFlE<L!anMptTZcTOf(Zwz)?3m4A`0KDb13>BRI{=_ETH
ffsXUsLALYd%Kph{ia5kn*jx<HsPO(h2TCSlk<+YY_m*WB(gQKC#h0#yg4eeF<TrA@d~@$z?Fo`7N<`A9qgsLI9~3p3jLHio)rC`SE*fQ5Cnaf1VbuQJ(ylO
eDAsN7`xUgT!nER-~dxyK*cx9BO=OmJpOlYa8At^55Y8nw1vhv5cwiSHIauMOLZZ>)k8&$_!Zx1PxZ2h#+=!!&uf++de|;7jnT`KwaK3KnW@k|?ClqgNw)Zj
<-ZAR$!9^TQrgo!2r-A6>iqXmxuKTV(?z*GT5BupQ6VOEAv|>V`U7{?+;sBvO5K+bDrt3jeh0y@zg7xCSFv2#8((;&#P_sMrc(jo;qcmkmdcbEDJ;D-Yz?)@
%nzo%RGhZVT1o|`mC>s@t&ulQiD*R1GKd)aq_Ci^4U4usI_sM0$GE}6%e98g%}Mz~7n<#_xMc$>jzjKX|BG9XS}3Ro#<uI%LG7dq1nxOloa~+<m4Qf%_r|6(
2RKG~E2{&UDuzeL_%Q2o`}B}4x@H!hxA)SUGoMUF<9lHkUXZ9pJ#c#sH`%djLP!ElOUiXP=N=oX3M6-Q(@;p#&GQv)58=+MJ>E&#%P0E8M0QSczQLOGUw>^I
dV=5{gD&+EjPils74FW)J=x*x06J&!cSs6L^-20#*~;Wz-!5_kL6ua>1+emLlp?zp9j~3d)l;p?eY#UQp&+et?^d>!|2kV4uAyD_-n2EU{hK}Q>@XwAbSL6V
8R&Tg%I6H2U6(YhRm9!#^Dm&(A|M!jP$K+Hd}sWIVO79dl&8D}7~OT?NOrq>{IC4hhBRePRKaqrzyN=pjG9Mqns6No*Ci3o5h>vBVx!zu&uP2~3JP~&C)=hV
PoeN4&P?R;f;s2j{}?A_gk#gF0T!$IlDlXje<UCwAtcwWYzZs;U*vb>dR#OBb^;2`UJH>+&93;eVpjN7w+oc!aY%{yiN#~v#@KG9z27d7EV_4y>=$nB;#tBS
G=%cc%HDfRjUp><?L`ihK*ixplSuPAsE5!9`<jKN>sRuAa{J}phnRQmC02?J8`%<%_)gSI|0oTOcJ(%pY3)}!i8YC*uNj;@v!Q3mxpwlzfn4C`FHz&Z)Tl%)
gpmE>7k>PA#k;RuymjvC9~JR&lcXi7anAMf3_cfbHA`N=Ks^z+m&qQ{k*=aWkJI1eFF3b3<SuiEgvKh^dMQTq2PGq~ouvs`o+K!L1_vXZ7dhjxLL!Ay@{O3^
>`~UPh}FFH0{X3mG^j%55{U#weF%EtBUgdyLacK#CFAclhybS!``xRy+on%DVvjr3kH5Jhw){1j&_Vp-Xb;x{jkhHj5W>Asg=SQBq3W-`2b~aft1E~6bU^@~
K#6)F0N0bdwJ?AVsLEB`4f~t?8D@biI>3lGg6|x>^;K?)h*!4n)U;7wPFr@K3<yUUkuIlf(Tayt>xG8UpyFvkLqX5(`b__W5=sq(XKW001pDA0sn4x?{TS_Y
Dk6$Rny>5^@J6*^y9!*-Jf9ZRw)Y*>Neo+?1k5b=&hzQ^SzXs>XA#@fjH&@}!My{gjN6iM0EX84`VnjMn>24OY}gV)4Qfo>#@aRzYi*z|UKa#|ZaM_A(BYB4
zt8)=C*fPZl;O6+&2X3Vn=^WN5HsVrVFk9ST`H=>WcQOzV+b1d3-xq`Ova#3q)EnqkGBv?elzohP9TBQrm(AP*^ZatbKvXZzs0|7I)waBRmwJNNq~I<+*yM{
z2>h4$ry}5T%wyUpN2m+LOo?>+Q%+4fMpfG_qZ8*k<C%XoL$0MAM=wErjg(nJV3;O^b7EIHbe1&|BlwmmUyO;H6iqOPS4!29Dl#{pjhYZ`eU$j)f(AkUNPJ~
QoK;u*p$P<o)qw5z3`EKQ^$8qcxcFa-2Ntf8Tl2I6yWtv4oS3sbTxS@Z5r=FHn{EE69Dc7GT_07ONCQ&ulxhQR04(5?bST;<AVrQOsn7Cq1>y?CCSE;PjL4^
L-Am~F&Y_QudW%G0*(fP9gn&bk%#D6Eb$0*s!8GwDR!I+E5SAOWcm3-yHMt3<X;|u5rSi1-(#CKf^O{Ra<z2CQBSXcN4QFcP|<!&&8ucAhp5}O1oXvPVk8g0
c-o7M+)+5<#ht$S42Pqu8aH?gR=gtSc?8|{se2zha<5N})06RSHgZ%_5vt%>I5jhuw6O}nj#6)wbA|`6Yf=Zfu$c6TVG&lG^DbCk#4f)(H<(<{o-B)YcpzA=
TE}|y$m#>OL+!&3&KKaa8F{Q9uOGm;*L%5Qb2((8)&6i9Z!b1NU`-sB;?42o%oq;f!}6t4@DkWo#^7_gG-_jDbr?c-@lniEtIZRxkY*Sx3AG@$n#QJtY@?g~
Dx%V;T?aZg*I<2kQWwg!w=+>P4~&vNWhIQ<cm6c``Qm#w$K!Dv8Hu=DsyiJ&6;l}!W+%FABOj^<nRqvKOibO?Iy8wwj1*^O5?jA>4zy4Ls9q`UlPA7K!1#V)
l<~F+kg7DO|Mv@m<U^P-TFlhg^m$vX&E>2nZ14p4&w8z{IS`Ga-0_ei0<?@>`8TeOkl4u>G;-s7n^c3}O^xcu$D3u9<pwJxAv>@AP{4X-G(4k~q>19wFp^IA
f1y}FkMCZWNk|D^4nYVKRt$DeDpFSvQCIE7fKhwn7sf(qjuPln9R+#=YXz7wHSXy%vPte3a*%0JnG#UmZ`_#ju!9l>1+7ryZvLSmkoFYWx9x7iwWX(OV|;T2
dUmsS@X<|z`Y&oPt&|cb6)T+Z<i<jy+tyF8ve(4R!HiWbnJ;t83>qqd7o*S;+aU6OF#jA10&-FZt3!!3Q-$|fAZ;v>Plz=Odn0azUS2r4<8$DQ<Fwi0QqFzV
QUg(e;tc5;0>g(9q(`o3DRp6jaq{|0Y!k0qRfYVRZgSn{(L(VHB6h8lPpx~#)1<|M6V{ZrSN*jE6Vy8!2*pSYz+`TsfUFWRBL>nHpw~3Jzr9B!izF>+?M<E$
SQClm2f7-@9m_?^GkZ;{z(%zGSW&s`h^fT))cGpT`+oFA;aOtFHOTtC>tTUODo-gn=rYP{hU#gexUC(9dME*JAZm0iQ$yKtOK_%0WqXg5X4P&zGwX%1D|e<(
Oy)S{4MuX@wZEHnSDMK!0i>#>Rw|M*1(^2%Eak{#Hc!-GD2}?QGe!3RjT5Oh=MjWHneoMWk&i;wWizB0vnY>%&TtD%$nZ8)PvAbeKo73r7e_j#@T<tzaJh~~
HVSvO(2K1(g`B3RF{7T1DEqhF=u%pwPR^aOw=ge<u_?-?UJhblR^Dgbo(eOijbyWx1oY|Ke1UM!<C6sY)uQM)(xFYL2q(66qJ2;GASx@@@JL)S^S{;H^(%R3
u8%5nG-3T-(Wwqg7bOENXuVI#Om5Q6^Hf+#h5mzhy~z?_SV90ltkd|p*t>1-#aWClb0TK_6j9jm1}J09kkELZ8X^`*LQubw;RgToIEz<0&X#CHkpv4ydW}C9
=|c9%2`lqJXpxdr+KBB?6ce;=q<!KQ`{%j1H^zs3>v>>^&MPLMgx6|`42($bSv2#%q>{PXH=H#jPf{lM7%;Sv&dXON(lQQS9Sbu5uZ?#i#y&H97FPJ#)n7Kp
%^eFLpT@kG|ElCT*7kM2!OM@#)a>KTnwzjvns1&p9TYB4hGB@5M&NOAwIif&8Abrs(ZFsUmNofvlAlZ7qyPd5S~sMFy{eg0P16bJ66ZUL!Ap1H_UivzH6p8O
-A>smy$3Rx&YA}7GJqZZMCtZ|a@s1a>HYLho{Q6X!&SJ}x>hdgCBm7fr|G^wx+RbJH>HFCq!Mj=#qSo*$UJUDBXuuyZA5vnGg^iIJwRa!q;eYHE^uxSfWU2j
VOr4hPew^<kO*$tT9paK(FEQQHo(i{6snBi>-;IEE3Opt6l2n<y48LjsRV^}&Xqr}`7>f2Z+Ng=kDdCN*7PEAE%PlL*bHzBj<x@IM5{r7+l#$ptp<#Hf3eF-
o9!BIs?J;d1*Z&Yh?Q1K2QWTI!sz4=3V0O+`~b-SV*|Lf8v4lcEek8Ec7k4Cg(sh39{5x4LkZo~4?Uo)PRkb4`b4#sP;tN88f6l{%7^e{%LANjSSmOst-5sY
;yNLzRpWsgM!Iz(YxYQyI}gC{CYzK;PpmlvlRu4S_~a0FWo&6xtDo(yqe38Gm1m&%mJUe0GSj5%jQkYyEM>c5gb_z>J*;y1#|hDAfd(?f?LF%LsE;%xa1O{y
I>EEKUtk9W{6SZEGb|S1yQdTV5mRhxP3cPp2WtwbU2j4=lhP9x<UX?aX=>uFr4CqM(tC|4PYL)>dAhb}Hd${O&tlHBS*#LW^+&nzVF$HSM-4P1?q+#cQezD`
eGfGX_m<X~etTc&=LIDJx#wf;jG+>m^?1A+&*y!o8ArSmg>gI7(G{Xjg0XK~^}7HNIoMG|d;i+FcfEWpw;&|E-iu)b1@emTAk~*6^A=UCRBx9{PzkyjU&;0K
3={U<aD9|-0p4Qevh;E!aB9urK9nCDw`-7iQ}94OW*p9_*h_WbVVLSjw=6wN1rs|9utg740e#_M_q$icR6^3=RB@KXORc3+<naXTFd5cpyee;QOf`*1b@sfc
B<eb;MC$=XCX&96E4mNA*3^D^qK{YTLHx;-xzmoO!L*D$(D!s1`EumbK1_=+Gtv={MD80r!A<Z3hA_tA@ZV{(d@!|7iDzI%#pg7JS>-}#s*YN~$19g^uO*-y
OA|3yZ76r1u&3B=hCL&PQI~OGd)sj!U#Wb3P7exD8jkzwv?xX;RH^lkM>!Vql2^{#a&Xx~{jp{DVW4&A_L$<E&xBc^{|1z$;PozXm25ZwEWjI%LZloU!&|-k
I9gGWqX}BR<)?ahHe{RD{O~a4TF1x{`Wjz<iQ)MDsf;MYnV>Nh;*>~gj@g$HQC5)gR<^0R4dT)XRC(8gBB#RrZI_Jo+M28(jc%*X2eRka0A>^AeqR}%vTcyK
SB~&|(f;?90&IrpWlPK<vfN`C>;Sv|rzipY%&YTmVnB4!nuWD9y5^K=dwP-T6_T8?BLaTCYa`T}T-5D2DOX}+0n#*T$Jv<0*-V=0eSJq_6;%9Jp5qNEt;u)=
a)WV7qHpOojA^hN;~g9M?=M60FFr}4TsE?xc^>?&X@|MPc$3*mf$6*Dk2rR8JsE^YHDcBcinA^<WMLEZ06#G*T$v24T`B_ckI^$kG7vq0zJiFy<y6n=;9mx6
hlo4Xl>{iysn9Irw7^Z<;^l7B)v-^7^gCN(Ogj~p(l$&TT|Q<qxY8?(srzQ53nYg#jCIW!Dbe%MzzHRefH*GGIgpr%Q$7QU^fMgL6TYPBlk$juI=O!cU%iZ+
V)Grs6H2iD1q(Yihstl;XEj$p9*Se{FV2bpREmcqP$3zd^f)jn^6lef3ZXms4V|DmQS%0=hzi4Gwqhw+Zx@7Zo3Pg*5#({qoxp<5t_~~dB~FWxbqQmLnv{j!
6yZ$Kh3ivmF*(_egUQn#&>aW;-3H?CyPA<ZHQFR@qQefF9hAHWq%?F|m?AAmuHZo7v4HUEfk2b{Bh%1>Td{HnIVz2FW|iE3?2s*&O{M??gw5ilm`E6&3OQ?b
cpv5#UE%3YjN^IKScDf=_}1atBuarOxu`O2x9wJzc1)22^D^oHE(8cV%Lw#jaS0x1EKtB6AVWfcVW~wSP#T8l=!w{BBV=SQ+_dg{pjKR3xL1k{54aH$tOq20
ya5KDC<Aqsn11d-iVE1^2?R52sO^qMtl@hSIB?5{BZ@n#t6dPgJT#!+_wAo$pG?qw8^?$P+X<Tshx-M6kyo5a*_hK1%45;!y%p3kvHgr1?k`$klK!2o$Yj3R
W?Y7oO9y0O`8^S2_O_ol9b<)XV{ZDDzUxX^zOpvSuPh{6kj`ThYuf9=>+y_@F*bH`L?iEv(4Y(&Ib=YD*g5T1=a#DqX0`ywyi84_`QnQRRnvel+tMJ=n%(N$
eEY5&b0n(fwaMHq7dx~i#B`hv#&)3Gt<;2Q296Y*+3l|yh$gfavdOX`_YBv|Ou#^eW)T()K*&qSJCB3suz7k6399*%%GDp7L%)tia8@lk2+gR`trWdTn7z7O
41B~4ZCkSRSBY3KLKur;UH_9}NSFGMY;RSJI7esh$=;$6ZT#P+Od-ZqFcW2t60yPVVcV4@YzJOosxmF>u{k0#r~$z^9)m~lPPDZI(=yp3J06?zV}<fPW2yom
bLJ3RWlniYA))?K#LQ$6l^zw1Co${x2Z$$>5U+T_WW#szRRw@w?5X=16(+J70ZjzKxPU@E8qSQB91G4k^$BC>y2G!0&%=;g7x1kT-f7=OYKAY@X<~pan(Kcw
h=agocv~4<;+z0+ed@Z1+0b~#wzTjKr@+J!%-0KRL2*gS@U$Kn2XSyI>-o7-{@8X1Ihn=kK!zQiSVQ10sF+*yLGXqFHY{*w`>12@Q~=))#{vAL0>Qh}hM@zI
Ip3$O>xu*I9W2XF6@;Qkd=VLx7TVBi_Aidx4&#vwaddr0s;zpZekCvP8_H$>wb`(aQQr@&U!sdOEdXPdDfSTi#Y0vjcS_l;051Q+t!{A9EQj&V7T<q%fkw=z
F(gOm4#PuzDjBx`rQys4cXb@-w2j^oe%F3_5Hd4Vc_sNf-Ahe7zCmPJ7FS)&BKA2kfQySJF%Vc!O07YVa#nL~x%9$-of$c6onD7~mTE2@HY62eko3=UUN2_Z
Gd$^M{(+W6<MK-}QA3mty8pzdaAfafH%beJSU&uOcBr4d=79Au1%^O%n)|EU{--Q##6LHzRW93<+Q#7>s}ekQwF6WcR-)kFxkOXnJ5+5CX{973CLwOse)%7M
&NR&$jBX~qPuGpjN$Fa!WX-q6qt#?iLj!-h36tDDiQa1As;3on4SeyE8DG4f{Ech`-C7WDCnZmmoo$rw=}RzBnM{<?b|LWnj>9U#)`<~cH^?bX4Qf&L@F8fS
EZVx6S<(+re5-(wu>UQ1(;mOV%hsAnbqtOac;5?@<^Q4jBIoHf+LZ&v6v~|z3@`=j_<q2yXnx*j)Ebg@jWRu@-scWWZLl|O=aKV-Kn4-U3Dk`mB)%XYff&YC
jz9~B8pyL2pl0|Ugnb<0kJ%hb-58HbstiHixWj40u-0HD-Vzz@L7&PP9tXmt-Rqth&ZCns!(Q6@;fcV`<2EieJ5uazQgl}^stz`I5q*ATBY$WdaD)fiy{tF0
U6CEkAjTAk%Fxbx&S>1<b+HjL?T(9aW)1-=a6Kh61T9zta|fn0T82uTJJ4y=36-I)RvRB}61$+gyn+}qk+VxzWO%?JnPp~^(tDJf04j*n>c*&oaeat3?a4-o
OibbA?cD>^KG(bYRCpAVtn4PQm|}4~lUe&jVn5P^exo6Sd)U?}S}p30@FKvqp2M{VD#S4tE1{DcvWu6bkcEGWKTMEhSMh6Fad$Va?9bacmNyrfPT<lEG?ZIO
F{0N4YSS5hSwl8CU_R57)Ci3k38w$3#kpC!7jOxIG5T10{z1}2ET1YAGQM9B7ry-KrRU$2$6Ahil=hu@2cTdcEm^`-%Wv=!9bc_orquNO#9ugRMVpT!cbp~m
ebv<6Y-y(Lk#$#NOP?2QvPz=PdxQxO9r*WkW{~vpo%REMzPS(Y5O3SHOIu17G{tM*T%l%(y!Cvp94|?lXs$|&kLgknyCQkJYOsQ*C18Wcc-QhIAn-_4&ldBc
&Vp2vmW*a-XIoZQ%|(I3DF16o?I%yPioKh1?6>toRIl)UaBw$6EB68^#h4KpDtlE@s{rKp67x)cE#)BRpPjF&P}2i-Sx7;#zW`lhrZiiz8_2vN$Nv>%B-hYE
C;&kfi~Eap!FER5l3;gWCj!9y2rYde&mnpq(9@EDS&}#PaO8{&D^MQ>6HOy*_fEb;ztNQTPl^W~?Rg!)hG+Y`W33VYngd^s!1C~D)Q?}e*|y2B3kf?j*Ab5i
x%<7Q=ERKnh=I@`2lG|9@8@a0jOG(*hn3nLYljPb%hitdD;^>Ix_O$h;fZ{d5a7c4SQ+WPm-x!KGbK$E%o?o(A)$uZJzijyRuv8fxecz+uy7_{GUnO8>l;nU
%<^>d9^R0S<7U9X!H=mO#|rnm%vl%`?`adhHryXs9DCSdQ$apBCi+i>{<l<w;5AanSf(fZV11}{0+Y0p+oAN`HAc0!2-=&oFJh;3#377Bb8#h)e*&4rGILEL
gH^eqSzrtCNBksN6nIz_KuC=|OySDMWs>+$fA{`ZOj7_{ogEJu73PTH7x-*GBbhWe%k4z(E816lIscBGE(Cr#Jix|JXJdud**OVfn<wF1YKwafEy58|#HIsK
O^RA643<KFtBx0KX(golqO*qm4I65x(8N+Ty9fI$bmGj30UL=&=olR%BJ%aPMguF-(K<;%Pve4kvZU3?>3Yg521d7GI$6q3lZA+TV>It3=OL77vg?B>6jf|T
p{D_k=;Fw0b3#Py!Najur9lcFaTvBF%kv=a@Ap~e4m#xQ>v9L{2nxg!Hga+Fm1K1wrc*8Om1qtdV>FzkKM5yoI}Cn3#y}DA@2(NUuN)`N^8}jX(@FRRh;JwY
y!GM%<bWB095I7h>VEFmiA}`;UlX$U=5jVg+^@+FAvei!L#Ko?=JXyu#jCL>drsSEpd$3=;ow&Snm1}R2v1&qEh@&oa2#M+c;tp>BSo8M=YcH!1~j~?<1sMI
-7aEz^Qlt(dfM(t$Qj;+8DNOQ^fo!hfyW?4nIY0Eze1j<MQ<XA_K=0ZlK{>@2qM<e1x4Y-wG^db5-eHRCguMew4VX5(2F*UfX1N4P+809Yc+G3mH%TDahlnd
B-_#ov1fPB)=q^sPSOD0c?Sb$#LMp$DVqru+HZ=V`5}3k7A*LM_uyyHtyjK(F8}VyGnpr&kuIA#H`(%)#%{49TmP!g7ntQhuL+roI<}g4HHkFuWB{+sbsfON
>C|llNi~sLyDiA}kv&D`oD0qgYR-`VBRGM!yFXgl7HWZ;4k2!%UyVB}^rObz3TXNJ<K2W+BJ@3;V<VqJ8IEjcWg7Ab`J%&8+0<o&nD?aiZ_v#4O=DC{(#nT;
m*v9`eLS@E70W0v!)-xtF3PzKXau!aIVkNWcx{AFWA#o_F7m0ZhF6`7v6>ps@UB0e<s%=58x?-YIcbt%jcgE8Ie^=>4=)C!zvhc9ILuBL4V4H~izKFAY)Eg8
(Ou39r^Eu*L0SeIVj+$jC_KwN%c6E+nbfs}adW3RxX<4_&ck4mKqavE`lHqy1Y#ZK()S_iuX6aKJ1v(mo^D_J-B*@b#)otdGq)&tlJ2=f=w3)-5u7F-G$J`~
leUY-5lScX^Ap?oz_Hr9rXHyw#;U@nm!9(YT&1%9Oq|X~W?01VB9q+~0o1?=M;D(tj5E4z#g;u79G|?M(osGNPJeOfToEmyo=rE4qMx3=!>Pg(_`#|Ro8`)W
`$6ib!n5wJSm5S>oj7^aCB98$zJz3uXUSkVE?-UG2S{XP$O_Z0tg)Zzn<(2C0s%iMiCQJ24-fNxUJ$Nqg;w-I+V&XSQiPSnqOn}O_Lrx^#1_kxLOXOvW_d7c
*bm$`-TCsgVG5{h5G7Gvph|3i@-ZPv@=vfu=Eq8aja{NtdNIRYu5bVGeoE-n<Ahh1OTL8SD)+nul%PEU9ouu7WHH?Db;;<kY#>pGMd8TBQK{+ym2rOej?tK7
$o8L1t*_yd+!3grnMbPXTdzc2P~)&lU3SQ_6w1_xm%`rsZg1PNxmrB(J)qa!cc09;M&0Jt`eZ5^WzaLfQU|YiDzZV`Y;jf{BDTd(39pbFtP6Q|LvJ7!H;C!-
#uzN3n!^BPue8O-Bjk~{73NfCpwDooGSR>Tela91#;cho!Nu}_z{8?V*lS+RqjBNQ&84*Gm!>PzBap~b(3UU|0Uqe7+n768yJL|?>+3Gt!+*DER-d@wL-WGq
qVM30DS@IofX-$=jivlpAD_i>&+U&xQ!=7|a2Z_qRzH3Kt%_~HsHppbD}=&_GNIHwSrxCJ|LZ_k8N9)Z(r?Pyx5<@K;mq$CAKZGGU3IkQMdlPlPKC(47-gDX
f?s8Z<R_?7Jmul0F%}>vsoy{)tgP2Z4F~=76Z0tJ4iCLj%KkVle!F)!WRk{~zaKy*?Luo9D{jC<Kad7CFgfpLz0_3t(r(ibo5k<|m(lSdSm-SNYoaycBBK3&
t^aC04^qF+6ZMBKZ;eB&8#aDl_leu%D)s?B-nrn^qDAj`DCB$A28x6gm;k~&fV^clf=4-{5}@v}0W8AEq4BoPF{#>I#+(UCl$TA14WH45@{2AP&W(YqnakJR
tEY?AOL0~t!|Qnvt1Fp+FZ=K@Ao0FuQ0{PoNY5^luVI_1TpM$Xh@Zu1chc)T;^g!J9kDokHvW{R3yoS~o;Y+LMbeHANuJ4D?koEU!MaVD<>?kolzNdIvoL3w
1QNLmI1qjChKrQ6jDdJ;@ie%JUg<VV<ak6rYu7u;Zg(-?w333%<w5J%wDr<>+kT>RSHr5^tM9G}%lBY6@o29|0Bvo^eFQaX$kidt_1f0x1F40J+^ALxvDMo}
*=-YhBfzXN^bVu<w|BpmF_iIXE(%3m)iAW|#Y6m8+;GIlIZj~=!3eNAm_;*!BYnGJO6W5LSw@`l_@6E6vc53+xM^630Bhfy*KN!}PRtRk&>9R~I=WxWEF6)j
TZ6o+ffhLNE$zjv)Rd_ezJP(LJn17vo}KuTd+ow-YmpgOTZs1qrJ-)ANv3kB8|uX1N}o1|vB%u0nPaCR$a)vBw&lZsJFk;(pqMyF?}cTim`uXfiie7;Sf3#x
A}YiXqzQ8L42LVCR5&kzO(bun<Yl~c5|P_?w12DXSIO(aH@JN_o;z?-;UP`=@p)xE)r(LsW0;8W_Rx<Zp-<Cq2T_G_{4E)OsK<!_UD0k5!v(a94KS6coFm{5
?C&I~JFvY4-oALX*+!S{)iCqCqYdYuoUsVpuS?eabBn~=<`;CK9XwJhBf7_rifo`2fMiGheu!4Xhe-plXN};kS86E+GlG$%?9*+zSPVuNc5mWiF4uZ7DgaE7
sX~*WD|79l(0>0Rg$SH;eJ=2^YCNL+IPspmXj?pudtE~HL`JGyPf>x87~=W-Q=DLr?FlCU#zMgRF`PD)KLnTG+c4*M8(G4@9$*Kaolbv3&m{=m$ZI-xwqDJ*
pWjcN+{Ha`ib9WQIRUwyULATns3jfS|JFFALfAhq*}pbL>vk%yWItr|{E8x7)|w8xA<5=e=Adn;SKTljn;*?4+h2LB=|aXlz08MAGX8s4#N>ssKx-=1ZzvN;
2COpwYXI$QISN?Fr2NU|<`jSSXGV<ZI2;LEYmK}m6w4-wr@d9D)SqiYkdS8PZN*)KY6NG7!-FGntJ@<ByhRsjoTKg*hu?JhP!RoiA?qqWqn;Q#(*Yr8Q+IGK
vwx|$SQ~MOVCX(gy9CtZ2+|u_1JZnNxt!P|wUUzJRAB32%w|A3u3;UL8uv~HGuSgOU8N6n8I;66Zy68O#I7cNgL`25ikSta+VyV|<2N*p1c@^IY^ghHewCZp
_}!)~MQ)m58PSYOqI_OE5+y^aSQ9&O#f~>Wp6kqt8C&P}{7U`3Y1Fql6ra1*B;XJI$d>UEQ^OaEpBzx80G**+ntTp*bV_WH243{R;G({wi4;WWPKsC5tS{>V
fL%xmk5LHobVjTp+cXv0U9V^Xg{HF&H_%cd{*-o1oYBLU(uY`(&bCvsSMJ?xt43eYG4Ik=bA9mAXup_aaN(xnzKe09-A-`#5~5yR*|?+1PZ#7{4eiY!s0Mqb
w#^frz)FDNBcOy-Ww!sYT54OVYS{z1r=X9zl~18?m~$FwHHMeuOdbO*BZ-?Ptm*Z+EJHTg`v%5bZLcqxl27Qvget5BHjl!N+Z_O}>Ph#|Chx6D@|QxnFcx^4
EvEY7P-srtb11DwM3~-o#y@0d`0KX6VdZS>QXis*XU-Yg80fo*0^>Lc`rtO!xQB(B*(1K;PH1rJAUQv+EK_yrhzK8#40?m;Gtx)g%HG8b>qoiI4}tl;MieaF
SH-9qhv`Mo>J+1bk!|wCRWGGa*RK-h9y^$f(GCby39-+>Je!Vgv*|$nSpqZeW|4gzL^T!lH3+nx*c0)cm;v#ux~D<3037aq>b6j_kgmG960ND|1v>obf*y>9
wN1Pg9cs@y<l@Chp|SbqOJW-8fdU_~3}+=xDk&cg<{L=mFU7zlrDufvl~r5fVAn;jT8y!YBIuxNapOPv+Cl6wOeNnN;Vg5?wiUSk)9qwk7HVNtQP8RH!e;F0
PkfB-4<5x4s<g;Nm>P(_ESXow#W5G8DPk?4{{ug_-xe^jM4CS_v-3dHNwwz`?p@Utvx}e9j4)kJdr%a5k;RUy%xpErs2h)6hzzgu0&+}%Ak2^#3t682-y10c
^Jx27T7Qd(ACY+(+b!a*FZ3Xd;XvU!k#HQm^8>91jZ9MRc$K%84WF%`b3Ez;51P5Yf9LE`9yvgWC!(pr<n&XozN=m}<rTER_^vqB4*CRT#+YsSh9H((>Aiec
*rY3tx$RlwN$1-AWQwdb{ked)wnblc+A#<KHa56=JJhY;yrw|=SALsEm!m;O7KZN&9g1>oWTNM1E%$5#e?j3`j$gz?-{E0Bb6}%#e1*L|2yPK~krOC8&F)$W
m6Ev?gr)Rq@v{1u(*RaQEIkptX8UBi`wx!Ctbh9-=dFxwcH7-OzH7l!Z$6|x2{jtTzKOpbAYLFFmEq2d?#vRi^Q_WfmRU=d&wf=$7*@Lc2uF!SWpHg5E%aOr
zlVXn+P*-yPA}pQO@?abc|i=G8@`PQEFdYqY?I$|F&cTaXOsW*;F7X?kOhPaZ<}=#9U#G+MA}k-rc`Q3Bx%r_h^q(k*Ig7;cEGPWR}+4^EWIKmuc%*C`1qV9
EcZ;~6m{~#qy9zLf>ZI7NY8D(7gb0coK;H&#0UF+%q8@y9$7SmXa-+6JoX(I-1qmjsu<l=#K(pfi2nf}>8I$z?>M9%Rjl1yX{%TZyKU}rP%RHBhJzmsL4l?f
Bj~L!eGz@}Yd)W}q)CK3Z{`WZiEr}}C7-als2q-x?onFXs}0{}inp~;w28dC2twnPSc(~az{_N!erftd!8Z)SA}MLUi$qldL4(x;KngLHhT42L6(Dcj(MQ}C
{Q}S{5gBMsLF}dvIRv%V*;Q4wHHdfW1eW>e;APNv-&;?Bp?v51Oh5C>f<P?v8}dy=OODwXWxP#{(3br;wT`~slBlVSaTP7~b5RAwrQ+4`p-2iQSq=J8xqq9R
9A?Y&CGmZJ$~^lo{@zWYv3_2}*QLf-E8Y*<h3^z)U?=d9IYPdMwUUaQ;?UTTn0G#QQqYN8aev`!f}iy@L*$knoVQ6H%7mH!!T!c;pf-&`QABiiSLIa=y<3dZ
Fl^*S)xmV_U6#Z^5REoa-R*YeyuH#mL6N~6h!(%CwHK)50h2$8TgIZioeB#_QOTfKK8pEI;PY0(gZ_x<=uJS)B1uORg{IqH82i!LcyH_*#a_i6n=Z$a!{Tc)
rab6w2KrS{-B56Wq+qW3z=^&r*w63kznyqG8N4kG#fJL`#+5Zp$S5+yV6%^%N4gE{`Jz0V%6+y=Z0e5LMEdfju^IcMU)q%at0~Xc_#`JAiLptphh;}TxpO#U
bjt1DY9m&Hh%L9In|geP?N7br{Qozv1wdCM$PNm+AHM2_STO1m*GL;Y2y@5pz0)NT^5#N3f9_7=DMvyGWSV5@-&%u%^7S58kFA6{ybEKj*r#0Oj{&yHJ+kla
TNR?*)wI3G#|gmHWkrymP%;TDu-fy_JuGXC^1X*cURTYyGPcGH4LOT5pAHqsjE6+LQ|(6H1$r?|i4U{a?(y9kd-;%>{}!Q*u2mD5SIs^+!m!1F3h0za*F664
i$MpmP{V_9x@^_WHPz{CWF5j#eQt>~Udy}>n{_yK4<8knicK)^Fae^6?lZYqq|%khj6U6o$ks-$7gv_n?06rq<2#o+Le~J39~UV}eQ*e~0_e3q*+2M9&h{jt
(5S|zxX*$QMe?09KpxW64CZw1Yso_o{9tlxfFU|$EU99AP5cTVF;$9ssR<!32I=LKmhp!a8il`kvHwImf+Wcn?t*w0-f9E`QSwfJk)Cu90T%_Pm!f%;GNsaH
I?Q~d)H{$ed@&E{N=<w)2CHsRjPpg2ivuWGzn7SAZN%@Ov|et0adEa>;RJRfL4{fbl;zD^%-ex96Mo;?i4c$21(B{74?(mac_)w*!$C4Cd?9}Ios*Y?^4y7^
p{D6QsVOr>N5$zqaaibg@MR{l&p_kj(#L0X;Q0%2`=2+fYK54mJ{hF?Y4u4Tg*5zF_RxdkFgI1zmUAN7%P||To#pPIc@^I>tZ+d7MbR>n>3gf`dkUX_=Qofz
5WS?!UTOmd24*G5DU5|+(1=$QfX!~AQ;9f5C7Q;Bt6=m%3aS%8EBR>vj<+gO_l(hrAQ#FG0A*ps1bWb)(yXLG1!1T<>a$BXXa>DVf-6Fvg5Kt!T^qkKyc+QY
GCl26P*RPJBz<R(TAJ=^y-3wTn%gqm1GQ@RFguBoWc~fj%%&LPn3G(^(?Ak#!^)yQ3#-udhPXq;bs4@K2=mb*g^+deHM^bSz2~W`l{j7NA&UN;Baf*YWn+;)
*OGMWTiCYz1>F+|oCGtIEj{mQeN7U?b7zG@hpiiCcHSZOlLolsw2n(F=IbGemh{pRT8|s^dDk(KKd4sLRxaumE&uaS6-%NH2M$nU_lw><YQVH^w&ougyT7+;
WWew%XZ2WeVsni>l+iIUT(XkQ5pJN;b#xp<lv%0(Mp3HbDoT`Wl^j}}7l>}ap13hGH_(~I$b>VUaWfPovu!Cq0G(c%;c$~tv{<RP{jLtfcF`5z2rz|fUh>iL
5?>B-{X=PDtO*{YeYm0eb?b#jO3G&+Yi{nIGeX5%()Rv(1smOI+lJQdp6%BmAJmUn^i2Dj+elvur?fj@IH;`ps3K3uM{x{5VWrA5#}ih^%li}dvqF<p<-@W4
05Lg>`?QPwr~XR3%uH~)o{UqemWIRYl^6=#hnisx+X-p4_hsR;CKy*D;VfbKUqsRrS}+(GCeW}P06&`(aj%!E$#|0c@grF|qyfKDy<cu%a^JdM6p>569Y+5C
8;<y})fb!#=Tpu-VeZI!yq;y`R(@dCGr$CiuF?uF_Hd?jh7AKL>u6Y?8jUlYw{Hi{CWKB@!Kt3{$_J(f04t{lxo_J73GyrRWc&+|r5<*R>8zN|Uf0wR05zU*
-RI2uG!K5q3z)IoiJe!oWT?)*3+D{n^sYA+olK~&l%ZfSO~-${BJImB`=pw6S0;YiFKGD#G^xtn23k%&LG8E)l+1NS#iD#YbdEpMyU*_2L!0$NW_lT2u%r#P
GgZ+96^nVRJ{<D?|44auKTmy3s%=6=Ka~XQD<GKmN{sTgj)&)}<IkPuSvJLyh+o`dd#`XUDqZ`BlR3Czn6dzvplk-dYN8*lsu&`4Wx?&fgE=4OldvBJ$dT^p
gUcQ8$hG?(Bya1w0_R7v%z`k`gz?}Q@ZR%d)u&WBpQHE?Q&ol1CjA!F^(N}b8<wH4mRPwS%%ei~x*p)gZ20%nIX|qG{7Zj|DSH})3PLhM54h{fYbFN;E>qcz
4+eN}vI_}N`JQ3CiE6j0u1i)*kK<M!{b713Yst2^w=fCW8c7eBk{wUw_-q_#TJReNClud@ovM@r9kb%l|L+-6AFQmm`I6(ST|RX+XU|2mhDU_h`S!oodw6x|
LIz~2b(17^U=_mv8N%2~wVivuF5b6jKqi?BI#OwW5Su|L`-Tr}Zzt(*Z0;Dd3v_sGR9H#9miX|%;9V3)&p3*+0Cd2#*FF9pMt!rdqv%0A4OH2EhlQTPR4W#c
4z&=_2Jr`C-|u;$Y52Pp#s}64pw?dZ$mGvDbThJFP)IOrS>JcZCEoCvAr{1?rGD)d!$)23p!~E84r>eHaJs5n`K@QCd|W%sal1j0y=3G}1Ss(%BWJKz%7>>%
qTmw=kZRdtW`XUHFghkVaPS|O{6)dm@{Y-`k!ZE!K1X6m3r9wMHX8^)4!2dN-CgyKs&;^m+Idom?R?bSicQk}=I3vB#vx0xxr!@J{ioru|C~~jS_nKplAL+l
5KOeWcUjQ7cx4_9$oxh7sVxBPuz=7q28gPA@R$Mn*5E4BQskFD`SK!JS5=rGsDsxS-<rROa)_~Xh?KiFWBfk)M)Jr{O6o<ahCaFp)wHK$r!b4N2WT>!scD>*
6{JK|YdV;a#$@T_>XN&Sxg0sJY&GKfXp0Tm`zNBl&GF2(xLyV1g@X`nn6f`-STFhmI&u0G;|m=MgERvFA7&RJb{?#=EqlHNf#!X0pB+0i9iaf+q+jYcs8#+5
P{-(2###M>UJHa^kH;|D+$q2)HK7O9Wu5pDlvu{awRb21I;(`1o!rO?*cx1*>!6<(%)8QGPbF80k+6AHaL1TO{e`0x;;|%rZ*a|6^KU);*%~RFmY}H3FH^PR
*ud<>1=*BACv^F7E8_-lDG-<VfU}znQgqGw&j6n)b<lx@_l?xS6EWvid3jXF(fr{aVHCzF%GIH^x&5XU!EgXAp<+Q*zMP(DLDh_LV=5tZ8KG>+?OWWM7-7zt
@Y%r24_~AZ&hOwJHB~*$2Mg@ywg`lFE=~+^F;wt(sRWPk=de#y$W<J`_wIlYKx814#BXak!yS*m#cn`&Nv5RBP6Y%qK#||^D5IP#qIIcdV<V7x>bopEhH607
{xJXN#`1gH|1AOb`^-W}XEp0`2bUK@c;CVaR(@$;5QknE3+)z4Y#suJ4z-jF6cK}6+_?xVZ4G$u<9>>Nf}@!Wdn_14zlZaNfjTWX@R1R2JZ7yRCM%6?KR?8p
A=9uYpOZ;wSU=*`aY7Y7A&lJ?T|IQMrq&;IrHW*}W`}-hnf|i~)z2CG-kK!rt-)qtiBOj13b9iy5jtOrvq6D2JC(YT+SYpQ>3^PCue7Bnj3RJ>Tlsw)T)of>
cZ>=0#A2lkId8dl05i(Aaf&+se98jFz7wdbXTi^_|C7yl)zPj}%eI@Lby7{^NU~~pP^c&;H#4={;8xswyMH->gy($ZwGVpwb{vgG%T)FsKZ!bKG{$j438xuP
1<v@p@NFr;NcWQ(-5OE~Ve5sN=zWSC%v+vaRU?@``nUSadO{%y4w4>nt>z;BlDrv@3syL_Y=DwR<)P?|_&;28M!E6BFTR6TMoM)GkU7Chfz-1muo@N%_z{B@
q<pCiSdCI<YXlrg<O}bzrvKh*B#k7X{e$teH%?<8`EAV>YP7t-c89RzU%3<uLX7kGjrEQFB1DvFfWUVf`~0GhVctSm5++Up%z77%k-J@c`qf0rfdlV&y@ml;
egaOqy}yE5CU~PEPr)dkUU+DWwOXv6B7QA_H)*zX9glaN1#<VO;_G>-k{*jkXl9k{2TvECF_FmY*xL$8^uZ=(FT2LxQ3x-hT#sLg4B!l$TCDx})_S%EHw24l
e0ilZq5*{uyJTaAe3IbWHFXqpsA5Izvl2BOSWjY7o1WIQVo!9!{rx-|920mKP}7;vJc(|R0pc1Nx5Uik(1u>X5^|ayRNcAa#zxhvo0{z?svVvWGmjSxiUPai
9v&}}BDqbzD%Zw;TzdG9Kq1jSK5fru1k`>sNkz;=l_ST7u|QskQ3$Hr<P}D+)de%>yZ)8)vnVFC=FIJm_q(yuPh(#-$c$S4>ruokLT!TumW8vDc~wun(eCtY
FjR@?UZNirFnV6+BqDh!%CUB)5cIFbJcjqZ^UK;3f>qM){y}*qliDVI7JM7j&mBy$0ImKKqmt+`uHYfz%2ly3aSpO$MIE!XrXd5PP6juGnCb^nWBdrUrosBb
n{&$R6r{Ifl>A9ptf|{#B&1Q|0GF;G9CH+#QVzU;gOnB%Cyq9e1x@Mj7F(By47ykWw)JVwP!EeJ?%{sotzZK4#NFjx)T6IqJ7!J+A+@aw_F3x}4C??#LW`3U
VAlg3$yG~`KVC(Ud%qMXGujPu5KhT%<@Q>T`ot#Bshb1n$EN%bYfv0NF!0!Vk=>n45gQjeyw!po2I~2^@ItoN-4*Fs0M#}K`x@B~Tcb7a?v)p0gsGY7x`w$(
PjYB;88BudQ%^^tQ}hEioD>#8kZ3{Y-<z43W5Z3yEFtrf3ROvI*K21?4`txZL7TOD;uKN)kMYnZ%0ETPcxPoB*%c_zyhLi)K3YPj#;Ge@R(FmOBr}&bGc`{T
M3Pa3J)C8yMsEW)h1r<K?C>D5s3jtyx$R6*gW?blI5@@~p5KeOY>+D*QfE1QfB1dM8a1Br%M4-5EOcTa0qG|uUaz2QXVKirm9gf#t*dUOfYw0*?Y@fdqvRx)
eVkqgA5oqe@;|b38|w>Y=O?;NyN&<~B(Rdz4g%H{g-TW|pfbNoZkUX^F%vUGAEc(Hva~*K0+JiU)$Gp;2^3`|e~5PjXWACjB7sjBAZ7Q)W(_V$1@V{+_cIPU
>`HcKYr_`EbFJZxkEP@2DyZu0UEYhg(V=3KhE|J3^n!K1tfwT^OKH^@2$X^qgirXHA$GV^F~05Ib;CW{aZ2U{3oR7W1a@0JM~E!7jd9|ELa5%X9^=f{E;M{z
aqtilgrk|;y10_r8b2@RPtV1nDJx(AQC#a(aTYobfXm;B<o9MIgOp?Q2_pq6gPNF~<Uf7MTUR`SbggU(+g4uTko)M0D77Sg)ZcHB^(~EYNfwnI$G<q-e!H}u
RLfJtrepE{%52~7)3{VvTlj{oVrRcaTx+7MOa0qAS!D9o-GNh`;t7M?8$%(FOuqjg*6RQpsO-B5$)77&IHQzb6nDD>=0v(W2VrdMf1O{^%mWk=wMO2m9Ot4n
7M_?o$s!sN?2(=OLnsPM>A|8NrXfJ73h7mPlBrQO_OcQc{wLviO8j1h+<rttSf!uzE*iSj08TO>is$qw5aI2TKeHk}(AHM8TYmaCO8N^aLCJgwtU$BElmE?=
4z4yledzKh<naz-E0@q)bBLeC6}6+cAJ9os5<$Nk2ESUih!k@Nd-w8zRrozsbb`cb$7&jzeT=UM^oA|^dz|wzCpyZz70jsUjmrWvdUJF22g}~~uT;5}X3CuT
mcl1Z3@F1S^jR}nu(U8>;={vC*(c&Q6%n#bxqsoGi0u)v&A{pMlc7KMck-dgJ|wcSN-O~>RD189SrHbUcb7hk<8@R3h@iRf@!go|Gkmm9v1`s_CaUp(o;$U7
lGT}cy4w=-2=9ON?$Vr??=5EBFy@Y5r~mMq1m*(`sUBhyz4x!Qti+nAF8(NUPl*!E4+Wg9T8Av;D_Ruy-k|;&l}61WFIRtB>X;(A`(#uo%9llpDJ754uRn`&
_NIe8gGK0!{6NrZZxoqY67|f-PD&PiSm*u5!iby$N(}6EYrSkpZvg?!zuFQ()&_wVnZ&m;-BPvURx5xK2;2l!{|!$HERTf47auH&=bBD}S?%Fgk+#50gR+CP
MeAoLiUDea2ItW}wX~fh6Q9AoXR^b4%HI#;Gqns!clFF_D47DW*@!7AcP1MN{7hk$cP6bho~U&%nAbLtd^-N|EhSj5uxzTT@N=ftgo&LbNzGjt9Vs^PVdMwX
*~c_%I2-_)IMgws&}!?S<1kF|pLutU$w^2dlrQhlLx8N%J2-GOrr($r<B7yCQ#jNQ6Le&ec?8Uy_&kItlGRZ~-R9-+xT*i27R~J*bo>z*$L1%25wl<SNV8J%
g?yGQZ{f7e5x*eOAyDHD>s_}yddb6rhvSjz>BIdfj_*cXZ47*l9Q&Uuzq*x6fiUasK*QNRYrart!~)VsT5C!b2?{~>Nmqe5pDfeOlVpzPWM*o&Z;{J1eiczq
Y+zB^AJ!i}Dy4S4s5ML1Oyj7+RKgRAJz7;dCWqM->=2lVbV5P~zTDT<P|VlH2bp!N0qOLd-cd>L>~RnO;%Wh)C!>z#D2NmwK+;t7fZML5XvN2Z_bmbZ51H?N
tUh$eCp1fI;(B5pbdGU%z+^`EmH9|F9i6Lq%y47*t&RH!`Gyfs&8mPI6y~u1ftuN_N@+h5`U-ZNL3Zbdvabx7vQ+ms)FN@k)5_EF&#VA4K*4pdmz_^YE;sY4
wFn!E30?rP7S&LJ@FM^+ZpM>UiCr>w30R##RCz*dECT0H1;9VH7LtL&&;cPLYk1n465|bgS|@3oXoWLmxu-VW<wX7~?myM>%`eFLQ3ml!DiAn1n1S_{I4Uz&
vTwfVOt-cn4h|9pMNm7HmDpAEDfN%h#+^biH0c^2@>|Q{uv)(jO<*2vMtS2JVMyYVLYwDM-{X9l<}DC2`xFa5?$|}Dxk_{rDfIFeB0NC&lD@(E1-nerufs9p
4C<JCDaU%ZUTEdF%3o&&#^^#RZ{Y5iOdDhKzlzb=t@0QcsI|{%y3j8T;lc!D@V<SwE*>YJiru2NgkJ)*g-U()06q8%RU$WQVf|Tq=2NMGH+37iwY%vDn8;Tr
yM2J|6Igk=*oBix#OcL}!Ep$pVpWdg7(6k97$6gihb|5H77~c}{sL&<;}fuurehty9t}+wJvt7{YG3#^9JsFBgD|9f^#K`WZCG#etVlB%erV$rx~UdP+uWQ}
jZCgcEs_ScI$=Bki6yEB^Hn-yLqLe)m(^djn_NJ8N0gnNu?w-mY*ne_Be|}m_a%<o*cE#%b7K6~za4HbBiRo%d`<;L2TJa}oc1p+JQ5ZNo!1l2iG5*43KuD_
yU$2IP_O$$yr<anZ%Ap*I3D?#hSQ-nTP?w;a|6O&>>!xT$fcvR*Sc{+P11qXfpM7!B%<eZ<q*lBISYR{rS{UpPQrl}XoR8UX+@N@X^rf%zhnCV-GqCkkcs^q
adBr5GPAertbIh7@bWS*oEG!laTWT0E}!El#o@~qaVbsU=uBdkOO0#)RH0FL^kiJL2Da$4?(PNYT<-6lh`9C{uS;wA;6HAs4xHsNXl)$7o_7#D6?SSJNku1V
^s7>!7^_p-_s8^QqfCGwMGtvAV8U(A9~1R+GSPzaU<K{pX;uwlK$ZCir>lv3X0oo;Lzn1%JA9G{!e^2oZy#zF>3UCv=RvCt491S)Rj1>3G0hz|?ntNLk^oSc
tfN2tO!DdiV=h_;y3gq(ZNeea07zbsTrawLgl(LVVs{08{#ds&BEvjTMKRFiN?o9(_8q^CzF)|*ob^mqSu`5#a6PdKp@MP7U6kii`)04J)Wlm*ZmNLW?XBRQ
_gD$J;l)gK1=zXX=yX&&t(JB_P+G6VNeS{^h*{^4Arz{bj{-2q4S~PGS%U<5*#xArq!eThq|Q0+C=D;0GNBz@R9^cA+KF~swjrDCG498&@M9Uq_o_in7Aahi
GU#+i{j%6AZY6R}T%9Htm_<xlxD!d?g1|Bzz@;m8-4>&X;e?kXKD&|tR4edyBdrrJdd>vrC(M$=m0yX6mGaa+R-ET)>>TyERR44!G-@-Kl~E3T@4_oV3cG6Z
Zi<qtMXCyp?`)jb1=+Vyt4N|~!C~GwWGuF9z~XT9jTwBj<FgJm(VHZSU5nK2y<turkSA;T=|Av01uq}Tc${C6i(H<JL&>$qj!2*PtoZIP?FlMeWj~gvhz@iW
LWxP&Y@m=wz;rfX4e~k+f-giLB7Sfqs=XdeQ6&77^w4PE$WM;rmsVCd5?Kj42MNC=u^JZ1%qgTmKE&G*)4|7)^T#qJn<ffetOg#R4_@1hupl8WC3M--LxTpn
9Oy#A-8w$1WSI<ywIN>xUQOoQ>#s95lmkJ~Th_QB_i~2efCo^=;5}I(nsbGya9wE0lJ+iK1!5TuBV26-ru)vlrKlcDPW<8PktM`0HJ%Rv<%$H!+P}4E$h-@?
v2xt?k0=+CJ7s4%oF+gSt>4cbKt86W1v_oclIG{HS_0K6yjRt?#cL+C{zXcMN8yDQ62H{t{3h*=mX-qmfmt-dko#&)+h&ZQB|G|VZcM84-JM`qErfZ$v)^BE
z@kpf^&{}gcK0I<*UG~$*FO}a(mi3S)UX)1Y-UPRIr*F7-0%Tx(|MOis5WS#eUKN$y_X%5RrMNRfcG#d(DvxZv~igXWB<=d!fcekh70KE@1my~cS{Rem`#JO
X)RLZIf7~M-%ElC;1JzI+?lDv6kOTsQbvY}At=}_JSM%=bE9={lB_Rq;a-~kC%@o!#cQr(+6E_gdwHJgYUWB(0WwP2^eMB&m0<Gju$5Ukdf4ZOE;1o@M!h>d
1BiWOwLV&>U6{zH<OENVF1SwOHQj=Nxh+&ZYR~XX?0?T2#!EV8n%Kh#Sn0M|@f<<p(M)1zjeA1fAhvegR(<8Y!*9W7F)g&n1#7$cX72R$q5sALV7so<W^51~
D0JFNG=u%(==tqH12Ol`NZr|gK1F@q@3l-S&7Sp{1QBeNu)_HPT`H!%<MF=tGF}ZuPXcmD<h8m}f&4ZCZPY?w+zT{XX0{fXrD-mR#>yc!k`mc60CT2C3>TmF
5WNJY+Dv!q|8QUA>fgZJsfk`iGN_AVvgQbFD*~i1t5l-UDW1FlTnze%3TWTcX^B#BB&%}c<*&3zY&n0rp_N@1c#ERdd7m)ok3s?>3WG;q5}{oScl<J|LpR=j
9xJF0xBprDDVk(thxY~la9bPf@QWx=5-FFB2{1p{o`ukXhIN{_k{cG4Ohi~c3HdjsMnzBV-I4}@0-sn_B`kCT;QZSSh{ul3b*3C^O}RSvXmi<s_I+MZNJ)7~
USK+1L-Yf&io5;&xQSVemLLz^^Xe!_`roGNFRH-fOtT8~b1J<7ad7GRX_1)mFAdouK(qOsBQ_x`Eymf8HI3QYS&@p_8!jBN%tG%(6A<=WI9@*8NsRY*wO@jw
TYppXGX~>)Qpvj>mj&l&@~(>cuOWcVGGCJkO@wZ0QjiT)pA?M|Rszm+LI@KYpBoZRYvUaOxB=QkdT6)bWsQ))<#KIuDr&1G*Gzl!ImetgG(y@E40C8K;3HPv
@VGNk<qpLCgj#$wlFUO{E{klz%6ZoK39CeRm^loK;G^nwqGyNGrZr1ZbQ0fc#iMd<b^wLSM%^tPGCza~0BeH)=Nu?N-j?iGZsz-LQ)s-&*;SXSr27^0zY}R7
46{I(>5<nZ&eFVy3a?+PU|&9w1sb2-M?`QsW`zfSoS;DMp|CnFGR8+fu9dJ7AU{3#BUw-8G2Pof^QA~ZxOA_>a&9X}zUk^KOzVr0eIqlL@5S6@JGA#x!A`7+
bR~=|x-E<+(d6aLV1HU``zQ$=xY7?P{0`}xVYT5iDH9lk(&uY3o6~o;hhG}Yu42T>`A0Sr1am@ucMb*%*z_Ekh2TDj_k~(OoqxEP4bCx;v3(^&gc?q1#Y5;)
>P5d0wY>I)n@~P6;}Q#Nd4Pd0xCy`5Yokn5CfshhOF8+J-Q*FCs{fGv3DyQg2YO#1qViI@<xfp?5^BWSbpW1W-W7z56dyy)TQo8lASU3f?Z_bKAd?nEcQ+7#
4~fnEH=)5%J-vyn16k_Gqn28QL*a3I?tpKVVi${V7ov^0HYRqrhY6Z=wrpD;)yRJ$F5>F5^lXHui83*PH(2Ibs9t`QgO(^xs|)an^Z<2#s@5hCB~!S@CaE>=
OB?iLZVK*FU40Pkmp|u3hrczdA#EquIJ#R})4I@(H_RGry+IhSr#~}$g0hVMhT9GRA%eqc1RIYU3C1Aw==Py+EFzl6xj@BEq5)7YA3dTEI{=tePdPmT^=irc
yRfID`FR&lN>bJ=mKQlwj<e*xrnRnTu8cBr(*>-YB9-d}`#{+*NKzDCN>Cur-iIt7f5NhUV*H55bAv7$TXAIeH#*8?BIGc}7vVCq++04xc3l>#ziX<*!sj`c
p87j>9__)rh712xNT3ekw<5f#Qxj{{vct=TNzTJ@C4fFy5NBe_*s0Jh<+5sTCEV63XAWe~b{k%-?bgz^CD#4a3&Fbnanrp<Hc=mRp~m#M!mTic1;y<rs>^+T
`~dw1)ihcq9lZ=W%7ba)_9*(^73qYDkK4xGbzjArxl_m$nn1?vG+ZwDjvhAkq);$a5BXs(6}VG03;2w7iy4AGZZz{euYWqEJDol?<G<>#q9p}za@$es8)zSY
{RZ49LL!_NV8>Q62UJcu@zF$-!-oQS-c3*ycq=SG)oCQ`k9M9vidSuPTKGrqBCcjgvJ{)pU0e|FxkeEU_`L;PihtCHQd9S*2k?H?AH-&L>sG&FiS(-Lbn7Ll
aFu9ch!Ttdm0?<XODrF~K5AlGV{j})nJFkC@DsF%b3%at=|lM}Iil&Ov&L*wP*SeaMX_ZEpS}4skY`+@jNI3F9M{xZxIfn<g#E@&X%`*gjEd~|#VssEPPOM9
b}x!S8g3rlwVG$%z{66vQ7|FFxPB6qHJwWx*9DVE_+4uR!n@!*Rk*J^6v_y-iwzBg%?tnczECoO43RAV)jPMyMD*3$!LfR-Qt-*lb7QN`_N%3M8P@t$tJ<j^
P%4x(CRPpV&Wd}eJ0!Yds7QyWGh3-7z@Uee$r&!C8pbR*hd&C*W!%yfDh#nPrb`il%UfKO-bY7?y9*zHh|vB#_QgZ;;Z&h-2g-20?60R?5>PQXXJ@!#QSHXq
N>bKBa!G3vJzUv=EYdNUbU@-1nv;LOhlcGDtY_%x90q{l9$@i`CH?LXXrz{m`V86CQ<<RKLLDo6$dcZ=0#&58CWe`cQuS8tg$$sQYs@wQHK>e(pLu0SywvkB
_!hw#&p8?=x+<@`_BP-Us~rPktgbduFjyX91c&r3-5)^|;??9uStz76!0>lh@_RK)kTG>_3heK^-cQUR!S48w>)xXzl{f}&S5!r@AeVd4CKe<FMd7C-IXJ*B
s<5*u)F>;_bf!HiZ~64w!4_MdYDJ_SY6=y`e*@8A>V&Z&aphp__hXP!EPl=ogOuRjRqFBqUV5B5Dpa#;xb)nrn?bU<dL?G_!?D*E)$*N$BUHT*Qf78KO$4S&
3oMBjsj!;v;_f1NTUSe7$@w_cq$g)L=299Gsf1uf+M1^bvN}dT&bu=hcZs_u)C!2W9}Kw%^(Z`7)^1=<JNx52?>ZXW)iq?h7z@?f5zjs`DCbj8=7OLgNz4bI
0s_5x9-C4Ca*&nD?<S7hCso4rdHL0Q8eXANyhXnVtKv}-pxzqa;&9&>Fl(IrSt32U*-lX7r}?LlB9T|}`<5THV0;h&dw5gBfy_qg3EZb`oi)GL$llk}SCng~
ZB|EY=-_t`>x<`R+?Jt6Nk7EjK@auhbK)yse>KL?)m)|#^4RK!SbVs!eSzme4X3iu;q%P7|M9i5W8czS;5R3orH(a*EON0s8%-cHj>j{QoSJKqTop1Ng7QTc
UaSmFObb$(-b_Nu+0jlEcKw<1+}BP)5w1#bzp~gmg2_OrC=Md8WR2Lp89vscKYrCfo6j5Mte(1MVUrt4w{)_i;<DNbtPlX9YVK5_(+WGeOEYNj<SGD}nI}7*
PkxVTQedrAT=Z1$Qzd3Gqh2#|Gx_gj7po8mO#$o`Fv%uAqFEhmn`Kt&Km+GrrG;EXG~V8AokY+*DM0sf&7Erb2!uChzCP3;aWJ=_3{)I}gce)6CIxFT&qAM-
VE7SF)Jt-2L3<PpWo~Sf(n+tYl8>tKQjUpWqDaXPp^+Gr$eY-dB9p~op~bsgkrhDrSi~Y);B>?C5N>EqzvBo;B5|Y<r}>N?KC_Wn$XK3BR3{-(<{z5X7cW#{
4fj@P3k_EUsx6yjT&khf?2LG-d-Gzuf?72TU`ntESg4(fF|Y>vrV&L_Qc_g(rL5sWJ_W=m{|}iGpf6ZfG69`;4U9ARzvHwdFr(byFRz**%<UF(fk$V{`UIEo
mBwG4TvF8k;vzdO1opHNAK_eFfL<$KP$}1EIJPPTVQq#<d0xSolMrc0he;h<VhoM(ubw`pfiQifT9$#lW|nhq8olMDg?;T?@xYOt8r39s!vcIiFTp^!C>Ay!
a!?{PB;plgjD#Y2lP{&e)M6mxxWe9s!D}7oo`GwQ8HlkxNT$V&4c_k{s8z6k=6Z<PWmN5I4j2$^0@=I6vhSp=W0ER0c`3j=b>7_*hfkZKHi9IOLl>4pTMa}N
KGUS{V+pF9JVL6zot<=Xc<eSdn5bKT{QK1OOP}#S-1iw2+^V*CaBGWGa9f!RTwo~)4{dVtK9%QVtKcD+G~cvUZRcLW=#ru8s>*4hNQ{(jJi$fdxo<<Zf$ff;
hM)$5-d`s4?5yETksX8OHV0^*nzFCNbRVph*x|Jb2u?*^0w#6B#Ovt~-eTyW766x{%K!?Z&{-z7$>CN=5R8OUYu(RPq4H~!-Yf|Gnuoj8ba~iJ<5&ZpuU!`i
)6~c^FbzFfh}6zi+E%b;9w>iRmT5*4#l2*(hdkR*6n96e84nT2hcWRTR`-l6>0SA`BHRh4fN`HFDCsv6(8Zu2U`TS=X}S%iFga+$^b#*+3BEt(yDqz(xLWSv
t$NVnu8oisQ)VpNm0r8s!{cxh%eA>|v=rdI!xS#QJTdN5?J@<#b1g)1vvEu_IL6<7w5?W4kB$0v)%2RRGauh!b_6=?19Fv=b|ee4Z5|?9BMUnZZ|YdXs+}Kx
ce(i!CH??EsE};j2>Jq`Bp^Nkd64UNhB#WQ$x#{aFE%ngbsxF}B`r$kv{m;pM^_|rC)9jdMqCJK3jyM0ngjEXczQYk;mOQ^ed10kzFwN1CdkbtGFFH{uxb(4
KuAhQlpaB!g%z!j7&XOa<Ovg?r}7|b1FxJ2Ca57c^w<Cw#n2juIuBId^F7<p&Ac!;xUZT2aQ?J!2c6^*(D+Sb=0`S<K!1W@jn9|OmCY5&j%2X_nROn8Hag;c
1|^E6YF;Va_Td{z-3)Y^O_?fMD*yBSzOSw}R)Jr!QYqid2fnwkb-vG1dHa~y`Z=y&Y)cktg|H%5FXM%e0om|$WeQws<1LdRp*|IyaU?G+;%^Au_Kl>x=G90r
BR}LK3P@-TBM_E(w{R4u18tvyElFnYP{j#(S0Gu0n@VGR>`CRr87!=Gm>9_k^T-cue8YAu#R11LWRS(ET^3+=r**1&pF&8O4d$J_d4h)gb?l{x1KfI=Dz#R1
kKzY%ytzj!=AMptyG>7YmuT73pT^N_k<8<VUC;AU!*~!sbI9VIPTi3__);OQye7solu8u4MSXdl5*s!jJWd+-DjzlNUmA;k22+ZO>{O0W``T5lPFkG$r-u!e
0#qSOrpqsmONW7xaOJ-I)n`_XB+T%gElx9Pok|@2BXitHa?hxnoj<`aR$mRM>UihPtqP8t(OlK#RgfHf&$ny@;;SX9{EQdFub-HK82-Rnr>8iM{%g+<sJ<El
0kIDt#%=d>JVivz1SCrQe*2EWaAMn|f|`ICc=4;slAWa7dW&O*hg<idX5#hvk8fDXTVf~h8aby;CB*FHuVu7KsRaZS<d=g*%lmVCdUu~3R=KRYS|b2C<U0_=
)O(l1*pHy?KBqQPwMLV##19iqJ;@3y`HIXawE2Uab!)*IAiRe^>5E_29EoVRvdQ>a1#^209&ryoCp~OI?jGoy@sx{kzcg%D@1Tp5?x09!uz(fI<ci`>Du3<(
5O#uH(;(lm%DB<c^Pc6&7#P^T4%)i8^SLNWP5bSo)ZIH+e9$XCTdhXgb&;uv;A+5%j&RP&!)jNp`JLs<Eah`+8GxBk086i6<hOK2xe3OoKMer5@k&lUcGrlZ
P*CILsX<N)Jd)t`_1s;faICh?E*82RTa9XB#*sBk9YutuGLl^4#Ohpqtg?h7^Z?)BtR!;KvEG!P33cL!eEJYAGOdFFF#G5%_&t~NH$lvTe#6Cu<hrsA7di{~
m+5<NB2mx8Y?u>4PzimTJ;0crUlsVZu*L$K|L2%UtY1*>8r3faR0<-23ortdkS7h1x<)}LF3bW&Y88wIGNbO)@70h%*I|dF^*ZNKry?%jle9^@EGiSG|13MJ
I#h`t7td_MnapO26bhZLM5PsG9KQ0vI^SBdbP_gvnj56-NuY7n{S`#7ny#`%6x{~C@-1_di-nP;gkwT|y4301m}N%1TFQG#{Q`+VbDNKP8=0tD;K@zDO`0z_
9mI+4aC+5_`0<v$kPD?2jrun#?QPO7G1|pYbM|2Ip(EQ&<n!_IjeRwXf_>b@sbxSEfi(xczBm6n5U<Gq!9UA$QM(A}Crt*^{p8S?ots~JAx!qI_u{2=;+S6N
$(ALGFj)~d-tKFyZT^6CD2^uV=SKNn0AJ)HKI&5(dn3A-ftLU=kXG2e8&WjoTK0RRy3Ds{++PNk6O?x^KRotRwW4Z&>HC0Skov>y3pk`@Jt1NfHq>(N|Ba;L
LoF{>JgH?uk&%0=a6Hc|ov+W{R<cGjXaZ4+oo~caL0KE5-pa7}6E^MkDA2ri3f5ccBXvaNW`tug9k~D*p2CFMT@v#d$V@DUD7@s;nejt0uE`7cUeOET_i%b}
iGp;f%^mjgzaoU3YG(2xHvUTc$}EQugX!Y4Oc{vn{FaUHTu~n2d1qsOWb><ZEwIJ?TgJd{a4Ohsy(j6>KXZ)7B#U>ec3My6p6h!b{^zW7;K}S?zzs%w!GBh^
n=qpfBt?CQ%i&NbfUyk>(PUKRA2-J{fZC#M6m^*oL9CovpX>6EFaTCcigz0N4Z=O$>Gg>N^q>Pl<y<IJGdRGg^VA-lDaDoRX@fdUgDLQJ@tS+7+dDn_zpDsD
&vY&tk7<%A^>_t&S}lRUl_1z8VS3w6%KTD7mmRmOYn3?Y@oM=TV<xwh1gg?EZ>m}-+LjbHwKEIKaP~2C#uhfIT1zzp`^T`;FT~k`Nz>X7!#E)p)RNOz{I;;y
!~hKA`O1PN{54j<nkE*7YL5%mzmexdq_39mB57ETafHgV<Fn6AqbD~XD;2QxR$-+Likq~ZK_8M<b}n3ZY$WEl@M+{FpYQy!-XlVE%F3~vv-!P9NkB9E@X_Zh
aL#!aK^#10NEgS>kqHv~LB(*j{zvnWh&naR0=0hO6cIGbyp5UrJaL$2I)YmpeIjSv#^`qzrpJ<+UslgmJY3W!Xay@3`Y($}Ja|Eo2udLMIY{jS1;3hDudWTa
^yY)Roh*Y?aoN07e`y*w-%yV~KYK@T=*=0b{k(_N(~M=9^%IpojD)4}Svdf6U1zc?mOM2@&<=|HD?l{mrDv(j`>PqW$qaZY_YGz6Un&q7Bflkq31#w*ezUMO
u1h6f6=h!UGauk@Dk18=jJK}npd%1(fb;P)vn%+gg44&MU5lQuh14&w*4aCF^i@GK6^!ok$Fu!VXzF36IHrQa%xrW@cxE=`(3o~_Kpo)FRKN8A#TJ{r3oAi7
00Fe_0nF6~E@02#vBYQl0ssI200dcD
'''
raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==109260 and hashlib.sha256(raw).hexdigest()=='d15e74e10dba367e039a9259862ebe900906b217fcb73be63576863393064a11'
files=json.loads(raw);assert len(files)==39
root=Path(sys.argv[1] if len(sys.argv)>1 else 'NF93_R82_PROJECTIVE')
root.mkdir(parents=True,exist_ok=True)
for name,text in files.items():
 p=Path(name);assert not p.is_absolute() and '..' not in p.parts
 p=root/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode())
for name,item in json.loads(files['SOURCE_MANIFEST.json']).items():
 b=(root/name).read_bytes();assert len(b)==item['bytes'] and hashlib.sha256(b).hexdigest()==item['sha256']
print('NF93_R82_SOURCE_RECOVERY_PASS',len(files),len(raw),hashlib.sha256(raw).hexdigest())
```

Convenience copies: source and exact-output bundle (`NF93_R82_PROJECTIVE_RECOVERY.zip`), complete Markdown handoff (`NF93_R82_RESULT.md`), and machine-readable result JSON (`NF93_R82_RESULT.json`). These supplement, not replace, the literal recovery above.
