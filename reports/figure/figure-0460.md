# figure-0460

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Bright Raven 76 continuation — exact incidence-circuit crossing and reconsolidation

## Outcome

No strict own110/additionalweak000 body was found. The strongest new exact endpoint is **`BR76_C162_CIRCUIT18_DESCENT_G3`**, a genuine changed-incidence descendant of the authoritative `BR76_C162_WHOLEP_DESCENT3_G3` parent `figure-0458` (SHA-256 `ffdd3e223d750c32adce2b7e561c469f8926ada4b6a66b260c61a1ebd3e3eef5`). The immutable payload and notebook agree on the parent: V54/E81/F29/C162, strict121/weak000/zero000, S0, U2/19, H42–44, Qbars empty, one 18/18 physical packet. No parent/journal conflict was found.

The new exact body has:

- `V=54, E=81, F=29, C=162`;
- strict `(S,U,H)=(1,2,1)`;
- additional weak `(0,0,0)` and primitive-zero `(0,0,0)`;
- unique stable face `0`, cycle `[0,13,4,2]`;
- unstable vertices `[2,17]`;
- unique mixed saddle true edge `[42,45]`;
- exactly one positive physical P bar and **`Qbars=[]` exactly**.

Its whole dying physical basin remains 18 vertices / 18 cut edges, but the global-radius-relative bar falls from parent ≈`0.315225930645656` to **`0.312647741291626`**, a **0.817886%** reduction. The primary scientific advance is not that modest depth reduction: it is an **exact, finite, genuine incidence flip followed by exact reconsolidation back to own121/weak000 while preserving an empty polar-bar landscape**. This supplies the requested reusable mechanism for crossing a circuit instead of staying in the old maximal complex.

## Exact circuit crossing

The relevant four-support circuit is rows `2,8,22,26`. At the exact parent, rows `8,22` own the true edge `[20,21]`; rows `2,26` do not share a true edge. Exact fourth-plane slacks at the four triple intersections are:

- parent `(2,8,22)` against row26: `+21000/22047919`;
- parent `(8,22,26)` against row2: `+525/167257`;
- parent `(2,8,26)` against row22: `-2625/1332238`;
- parent `(2,22,26)` against row8: `-3500/3013379`.

Changing **only row22 x-coordinate by +1**, `[523,150,-26] -> [524,150,-26]`, reverses all four signs:

- `(2,8,22)` against row26: `-841000/11028477`;
- `(8,22,26)` against row2: `-105125/417406`;
- `(2,8,26)` against row22: `+105125/666119`;
- `(2,22,26)` against row8: `+420500/4519807`.

The true edge `[20,21]` therefore changes owner pair **`{8,22} -> {2,26}`**. This is an exact circuit/diagonal turnover, not a tolerance merge or local score change.

The raw flip endpoint **`BR76_C162_CIRCUIT_FLIP_G3`** is still V54/E81/F29/C162 and exact weak000/zero000, but temporarily becomes strict **143**: S0, U `[2,19,42,43]`, H `[[23,43],[40,42],[42,43]]`; Qbars remain empty. Its physical landscape contains the original 18/18 basin plus two singleton 1/3 bars. Input: 492 bytes SHA `b3e8a81d56be3b90aa81061b28008d74721f7e6ad9b08a184dea7308922163e0`; exact report: 27647 bytes SHA `f871af1d94cb609be0b5a8a78dbbc3d3de04a5a41cb5dd14175ccb2feb043d22`.

Then changing **only row28 z-coordinate by -1**, `[436,155,-144] -> [436,155,-145]`, without undoing the new diagonal, gives exact **`BR76_C162_CIRCUIT_RECON_G3`**: V54/E81/F29/C162, strict121/weak000/zero000, S0, U `[2,19]`, H `[[42,43]]`, Qbars empty, one 18/18 P basin. Input: 493 bytes SHA `3bff71e2ed37d0f40541724b407646ae7cfab6dcdbcfcf3f51b62ce01a0b4ccf`; report: 14847 bytes SHA `b98ecbcf28ea8c13105e12f4557730212b995f6830bdc5fb1459ab91cf3b6c1e`.

Thus the exact two-step mechanism is: **circuit flip -> temporary U/H pair births -> finite neighboring support repair -> same S1/Q0 chamber recovered on the other side of the incidence wall**. This is the useful result even independently of the later descent.

## Final changed-incidence descendant

Starting from that exact reconsolidated side, retained-support motion with complete P/Q acceptance produced the promoted endpoint. Relative to the authoritative Descent3 parent, 19 of 29 support rows move, 30 of 87 integer normal coordinates change, the total integer L1 displacement is 174 and the largest single-coordinate change is 22. The new owner pair `{2,26}` persists; the old `{8,22}` edge does not return.

The final body is also no longer sitting on the almost-degenerate circuit. Its shortest true edge is `[16,17]` with `minedge/R ≈ 8.10542e-5`, about **48.8×** the parent near-circuit scale `≈1.6601e-6`. So the exact final body is a finite post-turnover chamber point, not merely a rounded point on the wall.

### Literal exact input

Every inequality is `row·x <= 1000`:

```json
{"denominator":1000,"name":"BR76_C162_CIRCUIT18_DESCENT_G3","rows":[[-865,125,-26],[-836,15,69],[-683,-218,271],[-440,408,-262],[-497,-352,388],[-368,-411,441],[-249,-445,472],[-194,464,-306],[-181,-452,479],[-48,-468,475],[17,449,-290],[0,-472,470],[126,-463,441],[171,-449,436],[286,-405,397],[316,-407,361],[387,-371,311],[368,39,-276],[423,-335,304],[421,96,-209],[476,-266,282],[510,-223,248],[524,150,-26],[531,-209,191],[556,70,43],[564,-52,135],[310,-232,298],[-1,-92,-83],[436,155,-145]]}
```

Input receipt: **497 bytes**, SHA-256 `103fbf65246df541ad4c27ddc587b73cb55d333dff30e9a2148c71944872e8e9`.

### Exact actual uniform mass

Exact volume:

`1577144215463124409184115075053041000434901780373932221664592758503516409258734257165757192057813654466243033556240738321322048802349056343291691423622689840361824755057709964795671542776822249279706435858517024283624691447508272794855875507112283999227954064136724828498856118957861837671875/17467209589802472009773085813720037117731270126367188759048515826266954478063448776203313520367826551610652837710949798377744193005370440814481258975645365683722774865003715261898953849047227434551397100073432350483027185107440883800449739917383547621750909600271184781406121324626766723648`

Exact homogeneous filled-volume centroid:

- `cx = -62773409229850712694181742578230844852641905941140048227593802040852856405517177764035941933291679665682273587118623448302609800490860548806395838386162144883948817927493445962444105234871453545166035277924749114750814868143519789619122876873208785778033786640832262148977009282458351532156358017713177925952783304405147808719775805678108589042493386857053507426023114856874316385254984994685869918602645904955608993196601506051557767667862138291391899682880250882912159522315236052298675709893397081037781104646249497945809763940204529422036133659974266580451017764084265945/20317533478677436490109174130557481293140467702291126816379790744777976979814561999499750341101072151260853569004409004372441779710424222104707534968578633773651883972065738305887798421561200338084278133600045964758176059717799088289955056681213758320337373109353860900359986489525027211553004829236538918757722481054033661564657829912847146220638222697018196724607120728906581832138296657852046730191370427855345129392555046476811711559135042401268407110745722479080332411717992915180950918436972436162425211323179798327545380239978008290686448590201078123890838945633372483456`
- `cy = -167946894396160456898943093140561644094150936759888115288330915567570618685978743442172936044151977365312336566311428249614652455772300961530660905940062927591766213314019670790598940803036205340461448244519605849842160297748201648989069594276111141434372164127553238527696081850286253004791429168319842679740973967380300358746566478627721061078658102086317863278231302870788909847293201281957284734784907682149745896116828829753521907684905185351928795332209237444046973561889609393290331788244805595588803736103143207235271656317513218151723884784874359027161915877297279903/1634744072997035119893841596711521483356129585241814801317914197855699297226459011454002901008132242055470976816446701501230947792792753502677617756092533751903025147177703082082926309780786234098735022243681859233416464574995328942869947089293061014280018526039965819569194315249140120469781997754664050934529395027336041735087411602183103718901925964127900885887929254049954860057104328792693415072868884999855355238481440521122781389815463181711251146841609854638647435425585636853639729069641460380884787117956995267733536341147655839480518852085144216864780145050961004416`
- `cz = -18399279077450722326901198129715610632044323915114006564105551097264166462954782859247231308022140861325366194809106291273221205747266138531686658027407015641011402693337242055280883510792575069099446296720247896793919355661512288395529835058683018330533041583836441867898230713064800758732808599449653504850868078570127915513527409993336343661120596638263179750813125687736533705335271011176157323481552614655854646823510128208750260681565866194865438031497429278086947331187295739891621016451240102582540546297024098227764731417797348444725427750368656214993420058576778623399/142222734350742055430764218913902369051983273916037887714658535213445838858701933996498252387707505058825974983030863030607092457972969554732952744780050436415563187804460168141214588950928402366589946935200321753307232418024593618029685396768496308242361611765477026302519905426675190480871033804655772431304057367378235630952604809389930023544467558879127377072249845102346072824968076604964327111339592994987415905747885325337681980913945296808878849775220057353562326882025950406266656429058807053136976479262258588292817661679846058034805140131407546867235872619433607384192`

Numerically `V≈90.29170958044018`, `c≈(-0.00308961761011637,-0.102735894364344,-0.129369465166345)`. The exact audit uses 104 positive centered tetrahedra and its raw/centered volume-moment identities.

## Complete physical and polar landscape

The sole P bar is **peak 2 -> elder 17**, dying on true edge `[42,45]` (owned by support rows `10,28`). Exact birth/death/gap are contained in, regenerated by, and byte-pinned by the source-only report/certificate below. Its exact global-radius-relative value is the rational fraction generated as `relative_Pbar` in the certificate; numerically it is **`0.31264774129162554`**.

Complete strict-upper dying component:

`[0,1,2,3,4,5,6,7,8,9,10,23,24,25,26,41,42,47]`

Complete 18-edge cut:

`[[0,13],[1,16],[3,11],[4,13],[5,11],[7,15],[8,27],[9,14],[10,12],[10,28],[21,26],[24,30],[25,38],[41,51],[42,45],[42,48],[44,47],[47,52]]`

Attaining path:

`[2,4,9,26,41,42,45,21,17]`

**There are no positive Q bars.** The full exact mixed-edge census is already included above: the only strict H is `[42,45]`; all additional weak face/vertex/mixed-edge counts are zero.

For continuation, the death-side cut now exposes a useful multi-carrier block. The last five high-index cut edges have support-owner pairs `[17,19]`, `[10,28]`, `[19,28]`, `[16,23]`, `[17,23]`. Thus rows **`10,16,17,19,23,28`** are a natural next finite circuit/interface block; this is a search focus, not a topology restriction.

## New exact scoped deletion obstruction

All **29** literal one-support deletions of the promoted endpoint were independently exhaustively re-audited with exact Fraction mechanics. Every child is `V52/E78/F28/C156`, additionalweak000 and primitivezero000. **None is strict110 and none is strict121.** Deletion28 is again the only deletion retaining S1, and it is strict `(1,3,2)` with two physical bars and Qbars empty.

The exact deterministic deletion ledger is **6161 bytes**, SHA-256 `98d3be556dc21bbd8cb4fcb5b9d2869706cd0f057d2490f7e0f7d8a2d223a772`. The separately observed terminal marker was:

`BR76_C162_CIRCUIT18_ALL29_DELETIONS_EXACT_NO110_NO121_PASS`

This closes only the 29 immediate literal deletions of this endpoint. It does not exclude simultaneous support motion, multi-support replacement/addition, another incidence circuit, projective/affine jumps, or other C156 bodies.

## Finite numerical nomination evidence — not exclusions

The exact endpoint claims above are independent of numerical discovery. The finite discovery work used CPython 3.13.5, NumPy 2.3.5 and SciPy 1.17.0, always rebuilding the H hull and actual filled centroid before numerical S/U/H and P/Q evaluation.

- Around the raw circuit-flip state, all 522 one-coordinate moves `29 rows × 3 coordinates × {±1,±2,±4}` were screened; the simple row28-z repair above emerged as an S1/Q0 reconsolidation. This was nomination only; its promoted status comes from the exact replay.
- From the exact reconsolidated side, deterministic retained-support coordinate descent used integer scales 16, 8, 4, 2 and 1, accepting only numerical strict121/weak000/Qbar-free states with a single basin of at most18/18 and smaller complete relative P depth. The final integer patch is embedded in the exact recovery source, so continuation does not rely on replaying the optimizer trajectory.
- A separate 826-normal one-cap truncation screen aimed at the younger peak found **zero numerical strict110** candidates. Many candidates remained own121 and could lower the bar to roughly0.304 while increasing complexity to C168 and the dying component to roughly20 vertices; they are not promoted over the C162 endpoint.
- Taking one such cap `[-28,-70,-96]` and screening 554 second caps around its transferred younger root also produced **zero numerical strict110** candidates. This is finite negative evidence only, not a two-cap exclusion.

No search failure here is upgraded to a family theorem.

## Most useful continuation

Do **not** spend the next pass merely polishing the old 8/22 circuit: it has now been crossed exactly and reconsolidated, and the final point is well inside the new incidence chamber. The next high-value construction is a **multi-exit event on the actual 18/18 death interface**, preferably using the carrier block `{10,16,17,19,23,28}` or another circuit found from the full cut. Temporary extra U/H and even Q births are acceptable; the demonstrated repair mechanism shows that temporary births can be reconsolidated after a genuine turnover.

A practical route is: force one or more cut-edge circuits so that a high-chord connection replaces the current death interface; allow the P packet to fragment or exchange roots; then use active-support replacement/pruning and actual-mass rebuilding to restore S1/Q0 while testing whether the extra U/H pair actually annihilates. C162 still has enormous complexity headroom, so topology rather than E is the bottleneck. Preserve C228 as the better-conditioned alternative entrance if the compact C162 chamber becomes too fragile.

## Standalone source-only recovery capsule

The endpoint and circuit mechanism are fully standalone. No sandbox, Library object, parent attachment or numerical optimizer is required after saving the bundle below.

- `RECOVER_BR76_C162_CIRCUIT18_BUNDLE.py`: **13107 bytes**, SHA-256 `e6df20b6d840f4dd4facc5c48e4164d813a42587572779711ee8af6a71eca892`;
- embedded `exact_hpoly.py`: **8946 bytes**, SHA `54e4c8f2f6f1b45955f42b6518c4a1586d94cccc8f4dfe3ae866cf5b22f3aca6`;
- embedded `RECOVER_BR76_C162_CIRCUIT18.py`: **12438 bytes**, SHA `f211b475fad3ebdf8bf0a92e38f697c3adb7bc6b1ee6cb6fd2d76de323748c00`;
- final input: **497 bytes**, SHA `103fbf65246df541ad4c27ddc587b73cb55d333dff30e9a2148c71944872e8e9`;
- final exact report: **15952 bytes**, SHA `9e98c58c755a53dd73b0ab201483dad03b51b9af37ba63898c5a4ab8b38a6b94`;
- exact certificate: **16839 bytes**, SHA `098f025129950f86856769f39e692cf8c2dc635d712ab540f02f5128d7511141`;
- exact all-deletions ledger: **6161 bytes**, SHA `98d3be556dc21bbd8cb4fcb5b9d2869706cd0f057d2490f7e0f7d8a2d223a772`.

Run:

`python -B -S RECOVER_BR76_C162_CIRCUIT18_BUNDLE.py BR76_C162_CIRCUIT18_REPLAY`

Observed cold markers:

`BR76_C162_CIRCUIT_FLIP_RECON_EXACT_PASS`

`BR76_C162_CIRCUIT18_DESCENT_EXACT121_PASS`

`BR76_C162_CIRCUIT18_BUNDLE_SOURCE_ONLY_PASS2`

After unpacking, regenerate the exact deletion closure with:

`python -B -S RECOVER_BR76_C162_CIRCUIT18.py EXACT_OUT --deletions`

The exact deletion routine was also run separately in this environment and produced the observed marker and ledger hash stated above.

```python
#!/usr/bin/env python3
"""Self-contained source-only bundle for BR76 C162 circuit continuation."""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
PAYLOAD=(
'c-p0W3v=7XlJ#F<lG=}iJ(7UIo4iPsBTH-7b!^4Ye8sR>cu|5)fiytMl3o7qd(I3%f)wTC?#2-X%(JKa^ywa8sBb^#w{g0fUM&~%yW{2E&%>X8`RQa`S0_nPp5*0CZ+W-6T9o!*WpTY+'
'RI6UG%B$64F|WnPdQpn&cy%S}yINeu_0_yc{winH;<`7hFlw<V>t56Cyea6#b?>}wv@TOMRNJV^vvr#PRsL0G`K*^MR)bh1#<0p)>#FS4>+8Yoqr2X0QT1-cU9Tv6UyG$`V(1=mmhJRd'
't(WtBaQpa2ed={`sL#=l`dqK)xLxh{d9>1f*duP5rq!aZcP1FbV{7s#8OzC0j1OE{6VY6mEHibjXs#@lS-Q3vG|QD{M7kMN>q<|?@}}YEdQ}Z>w;JT#ak;+Et9Z4jj9xM8-5zIoxwtM$'
'mPC=&%jb38oAtkS8h$_dw$to;zggTouIplUH@K~h;a_DB|6#;<J|EovYHoGG+D3vtL@3f#f3I=$K<h7g{HbZ%7L|);@_I49$?ZXDiBgKv7FjF8(}?<M%Z<%cPov0eM}D~|b6xRE?+NCO'
'dV@^hpCNjuRg7i#>t3~<=e=|>Uta^pRlc0ZX`c0xyIyrwH!@w-QPZy->~{JQgHeDd(~ri<)83b>yvlpk;!E8tr^Tq3e_j_i@jNeA^E+iW4AK}5b4h^@+hE6hmFhub%M!6A@nc7&HHsx}'
'C2l2d<tVmsYvb0&t=(wgHp(6i259vN#Ybp~-_kf5U>IFu>5|8~L^dT-8qGqU-sur6tJB`%2-50|X>kOWSWSs#ZASRI9YM+?J&zhejoFlJM_`H6CB}}$2j_#Qx8kWG@cXX${T07kpI>Li'
'YLLaNxV1lk8Wp838}~b~?N5x6vP3l29(x@x2WTlO!%+CEh(Fzp&H9tc2z*t8@Hi+S9hX@TrW>%<_%(7`t1A-i-JoHS=5<f88<5=t*f9@A1!>lK!-#dfD(cx?QC{|Pbh+zY#q(Lc1iE_V'
'@on#4gionQzNw>c-}NQs!*G;vL&3-C;yU5lIPRc|%gcPQ5zi2Is}cUUj2eew<rpJ@P9|b=V|8yNZXkoP?G5)?_KI5h%`jb*tD;=zJJob#!nqVn<6rQ=Qb}A=UM0@(rXDXRk)=DmhcwkH'
'&jvSjGfSgqivPZ=T853AymuYn7T56{biLG}0%JCcf#Rmxs*};I&R4wH>Z~e+5+ZNdEZ5rUXl4c_7piR`mb*>gD~fEF6>(YLcUDbtXM}>?8Bhz3X%HytRWHe5xHY`JksXE~DRe9s07gxN'
'gH)hYaN}BGWOt~|0*~Y6GB2}1RTz4qZNaSG@Q+3mk(l2Cma8hi&WF8nQ9*fiZ!yFA(gMp^sbK-eWnA`N+gp9zD2Q#b^xo*|s)TYCOg2J|XT@Zqdd><lt9SLMq*OZ8!_Ml-cC5zYad|f&'
'Up`tHKQ(b+^#hcbHE?Z+0RlnUtgkO_ij4xG!@QSgmsnd2;$6l?^`&4$qkru>;+JA|rCk@sS$$b-99WOVL8eMeJ5E@LkN?OC_1X;~yZZYYsp4@l`G5N2<K!Nmz5-}+xShQrtHxoz8pb3V'
'Lx@hte7@=Ws~lD_*ZV|i7c!ky)uI{<`so4@tc)wAi6f%3sOvS9hp~k2+%m6HU+bY;K{h&8x=ioVdCPTd)4QzV<&|!t>vsI`L3DJq6K5acio>zSQ-hd}!?83Mi!UXNsD|2zb_{b|*8^kE'
'3!#>o8b<fot5s8qB+5sacpOh!cS;OZkZcNK;~r|aj<13O*>7VzCFfU_1!f<Q5$xAFL?dRCIHS0I0d0KyG-Qt(9eO^Ao3=x<l<%EM>s5pp#tBF1T{Ny&lhLxuZz9t1C|y@kz1lYZa#bMa'
'yoDd^t+%{YqugjeZ>Afg`$T!@PZ7s7?r9L+F#a&9kc{nCHo7QpK`_c^)4SaU>0PVB^43ry3rdS0QQjWZX?h0@Hp=bLPIQ2DMk)o4#_z|UG+;hy5ynG%vg=hOaGhc?+fPJn2wtSPFhptm'
'%N$ax=!uZ{cwW><%E+TN(2qiEI5CV}5UQEmjX`=RbgRdl8_7I=$>vT@jA5HW><IB5@DlF<IxWikamw3dq6GTY+)k%msZ}G?qpMy<nw&?!s|)3^#^~RX)*-t9#CqbFN54P*H()6SFU9ZT'
'-y1JR#3@OIH^r(k8~tw#ryOWZPPxMO9UsQBTequ+t<PjT4wG%YrOuIveKWt0>Q$V6ilAIwuJNe~I{+;rRdT#sEC+kq{@6mbm>hA?AwSeq9}PWttDcYdlL@v3q+YhGzF|V2pQH$Z)uPBW'
'e=Vv4_sH&>G~-Ay98w{$`FgIYz1>`#4@_h9AsX<v*nAixwBBXB^iJcE#uy%0kq#A>XkdS2?X%ZGd~28zV;}YBW2A1AQI<v9U14kaEbAgkiT^mtGDuJ5eGqCNON%x8W^@%<)~uz~>EOVG'
'#;%^9{%Vf2UZbZc-l)}W#PL5sJ(h4DAz>d~09^n(NT6w9Y^kWl8E{EcR4~SJQ5P!tTOm%sG&M+{smlhhPi12bdCwf3cpZx(5ruMBuB#hwl!7nDMLZGsOw?!kkCgdTYE4S5O8KBJcNHb0'
'=&1@A=ok%5fqzYlCPiz~tE!kZ*{ceIE$>Z6*l~`}2Tab7bXvNrN|ow1Lrr$3W`w$GcI8)Wb=4B=J0{K_)aM&@sXm{nOZE9R2W`QBDea`22<>Id7hM3?=%GYhDuTNpdX~*TtK-nk=-7We'
'j?@F5sQWCSuIb>><~c)M@9s%Z7qyQRhVNR$7RFv`q?)N`3BwQfS~bau_SWrU8WQd1zEPuCMxW7au~;d9m*Ps5oM?NLz&Y2xOZOLJ1+JFv*;(I`?z`N2D4-avlFa|RlHP3g3_sM;{bu+0'
'f7?5|iFVhh90=>rZbWtiHi;AvSjGDj_>IyYT}2gAjcB`q>X;^ej5^7$a;C|s6xUt#i_LX64=&N_T9nsOYYM@OYjLeFP-~1Xqq2N-eSK73KPs<V-@fd+_S}lpPF5MIG}w4^du^bXadJ7D'
'%T6PfmPg$_x>4(TSf@tH+%nW+uf<#%h)Qg}>oO~09j(v~4O*+q|GU+nwdNc{o0A_I{$R^LqOq3WI=O0iMqIUMZ7cyVFedE-m{~8qT2$F!EpECV^h6nEE!M{9x8@S?I8~Q7yv*|XDvq8!'
'K0T6;e%lZ)3%dqt9t=I<GJpFudZHg$o;J6q`gZW-(dp4|kA4H(*ncZo5?A%$&#qWWQLU~Tm%SCY##YIHPDb;h{Ireh|LG?1PrU(DgKPt;(#@Y>Kk+AM(cliOn_({FD$-eKcO2x;Fj1{*'
'(8L%m)~g-CxVj360=4aB5<2BVC(QX%R1Ec1#9#VyGAbf{wcD{#b+NnpFQQq0vqe<P6QA<CXdYiDS={?N92|XR*6@`Nx4#0y#)0G}YJ?T)_s9D?k2s2w15cZp+JUy)Sg8dxG7(4ZrSY%b'
'%4A!aFeAs@*ahs4m@KL?+V9n3kd?niU+&4E%D)U@iPpLq9B#n=Q9Fpp=UHAwt!#qirg!i{O&6)B^c)E^mB($t7eide%WdV+7sJ?75iOQXqWGR`KptJTOvGobm5{$Mg!=u*_K7%mZG8Nq'
'cxJOvA>Q5?kNNAJal~KG)ULLD__<7)EgEXAP3h;h^bJaP9>%EW0&u&U+3@0ei9Kt%s!!52k~+1ckJGDdt_K-+e093*GWb&@M88lYPW7Ir1FL<1;NTd6Kvn(r5U6#1K0p&bCdLgP5JRV{'
'=$k5|#rl))qx6b?m_^)DAM&fF{=n0Pw&ytrGQVHlVUo_04vf<xexTApifH^44L)ve3}uFWUinom>Ve@J{H)YIs?h6h_f!urIHige1Lc|~^F86Um^pmED`^fI*a|z@e^eT;R&i1Cf%p;v'
'<F@x}q|MVy^3@mY;Ci%$TBLHO-c1qremj4|r<wD0#-6%4W!U4H`F!yOYuS6Qv_q}m_a3<ZQ?nGa`#O)b(wk{fzTKOS+QN^ML#e8=2%qY7(KqBHp6{d2pQCZ7baDuWpFb-Fsb)$`{Ym>='
'hQl6^e;s}PtTx=HaTuKXAyFgsdh#$bZ+2$l$M|Lvts!^2(wlqS1?L-2?lWpv{2z(lZFs+4t7Of07L-iAx8RhmI7mU(>UkHIb-%X~ZudbDi}v|<pY}IY)jm5_co%e<rT~|QP^0gUx6j<a'
'^s;q4?>x>P_AqpZFe~*wgjJ$>yr~{|H_y4V?Q?97Gu?TlyYoQ##^~(AJ5N+M&n<V}#;J9dF?RZVPj-BXZE~NtePl7^a=p@TVm2?K#QW%_IE#K4=h45#X(S*0E_6-`7E!T6=s+TLn3)Ks'
'p}OuvQ~9B({lIFjTE&SeV^*XBmuMb6s7R@=jm@@LTahpNSiRjX8=`&KAC1S&Yw~U0x719r)DI@a_7&6SN|mkZNN*E`R_}dgROJ(_IZozz^hT`9=JK7WLAHEI{!FcT+LV8Iqi;72KfG(|'
'o8}*$i3`T@2%-HCb@4e-CDY4%ah<QKyJ#<JUI;YR!BX{ju;Cxb6~q=T0BRGIr|lz|=?eYgt30b>Wn(^1!Hy=bJ|V&BpZ)pd^zHQ7#j6+pfBN?IyR+%}*^{^LUZ1_0zWVTT`umeNZ>Hz('
'Uc8w8es=oo$;;=bZ>AS0>l-}q0neXK38d*1n~~}C8UbNC?bGuKw1|gIj^~Rw8!VQ5s&|KUy1Kj>^I6oWiaKwB(W7}A(l+8t5!F9iUoQuh*d0MmME?umOLv$ehpkoE6Lk*f<y+%A8uSJJ'
'4g1O!fWQ*TYCBv#`1Wa7?LMK?4k7yQ@pFcsbNrm*r`e4Oz1I@`T`;3SgBKSqOmV4|i!_9@|15rfeRlfl{n_j3Z?AoCdTM!cdiwnJ>AUA|t>DM!cmDdB|IXB#>Uy!R()?&q&hPZe27TIP'
'b(QxxZja;k(xOV&#p*~s#bAhSGI6!ZIsU6Wy--8<>|@J5cKJZJ%;E~!V3AaDb=TwQ$GzTbo_MH`8SI`k(r@1|<6q^nD9b$S@dOd#J%SB-y<GIvqnIM)OW!=MNO^JkDZb3f>6IQdJ8svt'
'IiJ*=L(->{crXbBfz9ixSXK*oyIM$G_pX=!$w?)WH3n^)T;R5;=`5<PRag}IZ9AVk2+|8Nu07+;vnNsCb#f;SW^(4uti*9c*PS^s@mwoNo!D{%FAJR%{{=HAo8@+#2cDPC+(gQm9jCF^'
'|Es)s^7`!M+v)39d|o#`3cOHQ(iKP2n+V+6fv{ZRg}m_s8|79Yq;K)w@uYCffNiC^4}EcDyHeOez<b+6onu+Taa4Qhgt&KH;rOb(G)>`n4*HmCGK=Fo=<oPyK8M{ghU2@qg%}P8kRdjN'
'V-r<ATk^(|9$VVYM3xse<JcTm2AIMzLt%#;$5xF^U)T<3u|o?2_?ECupSKv)<}5zDIua7ujwNL1t6NKiCUs!*&d0bikWdGg<0?(qzL2)VTXeNtvr(jLTkK{DE2M<3>j@u==P)ic0AVeg'
'HMYerHU<rq4$&=?0(Rhpwud2M8_RK+yZzGBZphcsm&j%TFTh)$8d<}qs$vzZ&Ct`lCKcFBocYdvwE+Jtt`~e&fviIvAUGxz-kv^-zL~?Zqn^<UYdDtr%Enc5=?}-Az6v(gmbtxTQ(>!1'
'hnJ3kb}V;@weZoe#XApooCAuo{N|b+Frq1-8eE3@5-p?}+``(?L@Jpq2mj+n4#$@6Ds8rx>e3ymhs<mc=*uH(g5>=C`O7CSrl+rdzj*Z$nCGKtSQfH6!sV<Y5CA_$v4w=xt^iVCdxtQa'
'Y`VWgNA{#eU{6{XmZt3-UFhmNAB)B>dJBGqO5m}j6~Nz;_6496J}{q6Bx6#W<(Sr0Lt<{X`K`(w%0lc3S57uU!E(<crR%UGG!_5>Df-!;7iXt$&z?r#5PJF=1yhx1^@jr|bVXlgG1wvW'
'ZD}V-YPz#5NKM;v?cB{hCrsdje(XB2lV+Kd=dNu!VVWd<5N0y9lMIoML(k^LvNNz0{lw0LIIuF;OL992%@{YPXC*Q)%^>sP#MaEuy*LXKGl;Fg!N$k8%^;N0^6cE~4vZKBX2i(wPH3P%'
'3w$e{StPl{Gs7e|6E_ZGKgh5KJF~OgbYeGltTb`6%yKN>P18iq^2BuPOv+~LDo04_NNtP0oy=ywmCHP{{mh&>ri;$fNx&PP<Hfn3&f>(&(kw}5>CB$FR^rJtH?7!Az__!WkvC#nPC&7f'
'FvwGMltCT`Dg54ab4$(~*Y&Y-X~`rE-5J={OtRFSB^H=HPC^S4C0=UftxAd#Io4KejBJ_qESY((bi8Z^k>kusrJrGxz)yS|YH%~#wzJvHHuEr+5GeJn&~XA^=0P6rjJy>afd!Tf^Dw|b'
'sqeb6YiF5nCuW>T6NA`UoSAk4ErjvR_LJDN12&GGI0+Ivh`l6qn!&Sto~uZSkv+?^FmRCBNe)iTQfVa#ke4_!$eI9Kh)2HZrLckN`WYgK3AErR3t|Zi+OhA$j2q{E|LVoN-_N4H1yzD2'
'rR5?lSkeLg16mdc*>_EX*D_6D0K-{+VA{SN+LD0tpla#6fos~X<)N2^=4?m0zU8@a0V|Y{Bd~1GbsW!=j&0gDB$oh&9oPsAQkqT>n37|=p6%E&L_D$(Njxb%XvHyY&k7_Q3X=G~8HT`e'
'=z2b6mA>x<5Cop%bKQ;&Q3BWUP3g!0BRCuiUCjVN#}A#rg?t#uw=9VUVF<UuU=F%MMj$po^b3Q)^(-q0AvvbDeawYkCzkJ^i5a?(3KQVc42eKYY1zC(ShP@JN#8_>wb>2*LM+fla)GGt'
'd6>(A2C-0J$oC}FVIc*;8htcyp+tDQ3(;T?GXzLOUit{sp>4tvz6sj|SW|$k1N?(%=t8*wzmJvpPT;vp4p&0*5KFMJ9@AkZ%!l#q(5EeZYT9-o8axPcx|Zp4WF#;!H0FhFESku5ASH;v'
'49(Cp*%rWnMWHf_=0j5B`5yFQdrr{bus-6&>sQa8M&tgG2f1uQ10kB4mtN>t0h9@p1QP1QVjwP7Xu7Du$dC&1x*=o%I-p+(gMd?DSm+mw0<?wHhysfrdQ<><!1@%=lhiKO1&-rtLNo9{'
'NCDLj<6%)SD;9-DfB-%$ANT=}A=e6l87SLCIsyZMNuU52#lwtPMhL4rAw(pi;Kv?50Q?ZN?jchFq<}}n1T*jhU=^NX1457&P?ww$7W07`WI+xD0V?1EK)oBluY52YryzUyfo;>$u0^y!'
'5cESMpdQfxc!Nm+dK(MDJb(rC>R`FjhHTJP0AnK>Kyfb6?1UlGLS(lvDKsJJw9pFN5Md*<E$GjLr$a{;DOH&hO0?_%>P5bXMo=%E6su;LR1Am7pe6L8VLdoIv<;EqhmaAV4J^w<x(bCV'
'9Am+77g)fdQC%52lCZaIz&8vjzK0f2HdR5Dp#)ZTPtXeZvu$X?1Hyqbun_pkhsy#JK3xH;a4;E^3t`~fFpOt|5<;RHkio=sCD;>of;uoEC<|c2NQkH|dO)qV>xD$W$xk>GfWWR6l});X'
'AAt|SRMdLl!MMK7%>z&b_XpttTBZx1$5iA}cnF*kD8?O05X!>9E(r{j;X`#H0Ud@^E3{08^B_7@j|Mi$!N)%=)`lN@6brzIvVkL*7S4zi*#$k*VM5pftwK^2NFG!M6vI<&&x0h6M`r^7'
'z;A#xxE0Po>SVltH-;oXkKPG=0A8?#rT7`0JoW`gLBF;Mn3IIC9!v~tLG^$vB!{U1eh?r<LL--2BM*YXQ3gY}lnN%HTS$j3v2>UV8U(4Th+{(>1PQt)=mDz(Nm;&PK@bAGk&yz%V={z|'
'jR#c#?;#L{37|NvAHEg<Hn0vY7(hl3`}rgC1iT=0Y`CfiD=@a;&Q#EWsXW@<fggn6Viz$0YXR}l5h0?h01i%t=`lUY6c+ZedW?l$bWrLaB9M+fIwHLslR3;U=vd%7a43A<^k_?f+cZ7N'
'_z5t3bU2DaQ<y%hAs%%FCqWRkiEmOCP>I=q9R@1M0EZ4q{7?aLLED8G8Y!QJ{~Qn$p^Q3&C74W-72plPJ6PXD!XOoZe8ya`X#hT;>p|(z2f_f1P9aQ^tHY(y55a|!X(^OWq(J|02a7%-'
'$?0%RP$4QI4MwAyAf5!wfC1dom*K?>-WIq4)BwF$ie#`D_@T5^Epq~keu+FHK%BOjE&%9oYN`X`!El%a>SRU|GMZvis0dui?LDl>Yz2ZswKlO$9!G9MX%P&uJBRI18Zf9iv@6ks7Qi_c'
'49S@{VBixFio+0zBDf4hvPgGGlHkw8JlWl*JQ6Vm7PlB6OmaFj%Mbw!5$<pTMZmBP+!MwFbYTmu%z>E^Zpo4X;RqZ6jzAP}$-uz>N%b%ejEjKaG2a5rp&nRBGFUJ^;u>fmBY5ZvU-4B)'
'ge83TmUJ*0ABqG8f*RnNU_@X8h+_tc>A0al#sS3<$0jHOA=-rN(cH+sLS(_@e?&t%xiSVS7^WNsJh~A{9sw8XB=dnwF*`JD5wai`1_{I#0A7+30Z;H7QZMi)=0@Z)DHMV%@*Z-qO$dOm'
'Y&t1m<iWUT5t4{pL?W2aV#t)t?MSz92A$6aBqgW^t_XWED_}9WgXRX$z+TAKfHRLoP6vWGU_&xDaly2XYX<2;^)NCTGEwo7u&E4!C?!K8jUp|OmY{YRn0kN?NfDZbm~(QW@K`QF+E|cD'
'C;>J;BL-+0+GKJ@Vq`J|ureV*_5))wPx2U4p&57@jR^Om!+{wALHHq{<dXC$S7?!8pjyDoVk(Ztr~(Jrl#&q_nU6`JaT3l)4J+y-8YMMgGdYAo5HcYw(81}M31e#bo)04<7X!RK22xTc'
'JP$bm%#EZ2A<-g<y3A-Sm3{%+AX4;Y`iHa!**75ObL+qfT}}a@sq_?(@rYoTIkitFX1+{r3MnUd449W|L!3gi@>INFdIm0LCZuTDW|E{_A8Q2JV!vZE!^3b=F|<oa03MQy1yeDFqo*On'
'Ks8u~(kFH?BtyknByI?cWEO}()(PNXP;dfMOL8%E0oQ<A2E?*UrEy;Z^f6NhLTpRt7mx#d=1aAoL0SUCxJ(wYKo|i!bdi%O9|m|%ET$ro`MXN`NEtSF*>EXlYlx2?SyM$!7zQZznUQdj'
'fnrvsxv&Bp4Ju{A2DC#adXVp{{T_1|_#{XH#<NN7_(XC5x&c+tMG#_uKQJy$L9C+_GcyKC_!|lU5-0&4iEIY*1q|?@eu@V{n30Cu_n5X+$sL)QoCyUX@Ar7YEQ{fXVZbA$aZd<hhWRiz'
'ROu<s139})9u*5ZDp^)J7meyOnE<|^e!u{^6zxk=B$?4YY$m`UVbB2i)>Y&~ccCV@uMC)w0x2FDhv6JpMD)f5Tok;3n2l&FnNpJ4!0YreDA!iZ3<ZSrLXd>Z1;LwqvKH(tX<ASs1R@JS'
'<0eyo$jW^pogPdCc}zmrVq(O7FLn`<dt9<RQ%H|_P2eycKt4+%au{>q(g0k*Z5hlg30`ur&v+F|zPW9_&3P3Mw%?I$9^xOP6t07c<E#8OD=zbTHE6$BySQG)&AUjUztYuo{<ia-zacl7'
'Lcfw3s>b@eeM5eJ*JI^ny2$cuut+{`M(MoaLGeF&J9Mna8En6etRC#DH=#mZs?#d!m`XJsPPX4URA+ntDw~rBnLa9k_B&r|*}P!VXBTXP$BxFuWc+FJILh#eM%}l_S_*yvO25w=RHBMS'
'm8j8XRaA}po7b7@6?!ql(Cv%-S=FO-$@ae0jCyImimS_f6@8mk#|7rO9aOO)wl|6KeS17@^EQ+(>?uiKpCr(4t)p@K<-6J5_w=-UD>PSMA!`qn%=9^s=19p*y}suu#(Xu<BN|bp#p|BS'
'%8i5SspoO}Nn2=D6=Jcv$}6Rya`P?G^TAhR`;{JbJiC|}+oL4tHyPcwU#~2AOjndV(acXd;rVw!(CEzHl&BM<56+=PnHb{MXk|^W^7PX*xm&@O^Ek=pLff(wS5f<*c&sWm=hpZdln1j)'
'r8DhhQFJAm{<>P|^36Q@jo^UxYu@R;diS=krn*{2eEBt)PG`kDpH7WqzQ$88ZU_C{7kvHA$$1WcwLGr!IBTTm+1Jh6FuFvhhsBh}XptRXf69t#pdWWP9+%%1^=i8Kr0&#<SXCRfJka01'
'5dHA%)r+%>>C>|}eEMTg|J&}1J%{VOJmZ<KBx)%@kIExZTV3xycNfb<zXxt!I=4NV#g3QN_;#{AN-*Ag4Lq4d(b#oFz;{yu;!c!l(5rnv%m#eDVQp*F3uBgV&fqt*b-a67i9kpR&5p;?'
'6w;bB{dby3Aw4$X7)wB0<G-U0F_3y3HWUY{S*hye!D`i;wGUM{y#u4OjNL;T%bNHY_a(jLgwJIW3PWhml`eKa$WMHxu!umo<xb2Fc#ky1JVB0!Xcy|h(&Nhq{ng-y%|B`zjisEZBlcF)'
'^ANV0m+jN@7tb#gu-e|nXtqTW3->V8dBGxP30k-K(QRjoPVeea-{z^lKucq*x!FE$9ARs_&+g-9Q@(fd;6Mv?v_w@LM%!$QwtFy}ZDH0Tks95gtyS3}sBP=+<7}_r4#>K7e~++PgRrAO'
'y-zr?kXm7XrC@~}4)XOAWW-2-`g}E`?mZ^=1R*nBbm6lPq(lwS)cc}CNNeSqj5bZiGMMnMe<+-((jNhh=RIC3q-_Q;M%5N9s&o%8-S=V)_@k-?ThqGgpslJ7_HN-;?ZB;ikfy2!;8y)D'
'+^Su;ZU4vu$}e;|jAb2!Vf6zTRtI6&35@Lon*&jO`v17UITEEO4(>^Gufw`+s#%9`;S?A)DPWfa)!TZ0(*>=5V0kNOBberyc2Hwfbf|)*`)tv9y(o%gdpxRX+_n9|uC3{{<p+!GM0aft'
'HccM)kC`1a<NZ=0Lv4C<szZ$d;fq(V-yZC<1FrFZ8aX?-d=Qoopz;Tx+#8jr@O15_YkN3P6-&OUZ)=)Uda9y11F)$(i17y?j`HR(7}|H=khX(uPKa&l+c#Z1gWN}J6n*Oee7JYCLMSW`'
'Hzy`UpGTkC0-jd*e%KH9+)#Z_pj)jxu~}pL_fjtBizJ>ORdH6V>!T{4>q9TgtGikq`{LPsm9`ewOZBICN}#w{sDt8J5nq;zdR3%6<(fuq8r?m`xuYgy!~>t5q`uqorgH?As&9^l>Vwu7'
'ZJ!(Lv5wN6vwrPXtkYjjGa0>>(RF+~(BFVu8r$=v7jVdY9-Vh=uSn!FUP8)~*Ai1=^P1}~_w!0AF>3x~(L<Z5&+0p312y}YTP5xbkJ?*H-5QS`$pf-C8z@fI{*4#z{XYMTB||04=Z+wh'
'BF*_NiS}^f@Q3WBwh)%I^l4AgWYasH4rT29=KP`FpYrfflMzhB=G1hXnYT?<F2Kh3PxRIkq4TJ}Z#%2IQ>aeu7wNj`mS`enTUYJWX)4{+-LKMLxZChkTdc@vcz~a}BB_?|r)Sgi=_yvQ'
'LyFs}6-5m@B-U1K_-nXBW}BW3i4D7i)|sBDRh3)#ian+o9^@WsOgs5hkD*kLGD9@%INb7NXTpXGhaFbzoRJ;w__^o<sS2q5;RdtY!fE|^x`0<qU(05CHiFj~it18uor=$-xpW&SiFX~{'
'4nqC(?DgB{=g&`{ygh5e+)k8BlkLgjhxQUW&(quO_E>b&g_Dmr2Z8x_G}J)PUtVBauJ-Unvx&#=O|_1?x_;5rFFN&<S=XjbZJKl+Ql!b|5Aihzf2JUYL0nzxFI^Qvr#QGD^=`L`%+s?M'
'|CROsOIMGF#pJPmWb&AQM`M$V+;(RA)-U?Qg6E}a%J;P4nYujV<+-{%=jExoJmuv<$GYcI|G=4u=l*an76Xo(vOhLu2R-URU-}y_;=GseUG*KL%iW|?v}G!<)Xa3*aQ>cGO}_8is6P1E'
'=5LeHkBbDMaiEQ6?0-#4hH5MI3(G(CmW#!laU#oCc?It&7=?RDp2q7s*I!OiHfEdUy2?8zs^Jq?5WGl_F`PO8e!V=tz<BgR?D!V-ak^Yj)5W^vA0dGh7QfquafV1K;J#I~JmxO03rRuY'
'38$^Q>b85y?e_edK&HBR-t_kmn?{38<C6y>-HWrg&tJWKbIAF-87`ltj=ydn^l3R6e827`uvVL?e!Z8#PX0IJZ4%<c<2}SpSlp8rFJ!n~Vnb0cUt!P8&rMw4f0p=zZ*&l%oo{g5|Gq}^'
'S13C$9&H~=HsA2*A02His=kcebRX{c0>3r!{eJ+fq6Fv'
)
MANIFEST={
    'exact_hpoly.py':(8946,'54e4c8f2f6f1b45955f42b6518c4a1586d94cccc8f4dfe3ae866cf5b22f3aca6'),
    'RECOVER_BR76_C162_CIRCUIT18.py':(12438,'f211b475fad3ebdf8bf0a92e38f697c3adb7bc6b1ee6cb6fd2d76de323748c00'),
}
def sha(b):return hashlib.sha256(b).hexdigest()
def main(out='BR76_C162_CIRCUIT18_BUNDLE'):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    data=json.loads(zlib.decompress(base64.b85decode(PAYLOAD)).decode())
    assert set(data)==set(MANIFEST)
    for n,t in data.items():
        b=t.encode();size,h=MANIFEST[n];assert len(b)==size and sha(b)==h;(out/n).write_bytes(b)
    subprocess.check_call([sys.executable,'-B','-S','RECOVER_BR76_C162_CIRCUIT18.py','EXACT_OUT'],cwd=out)
    print('BR76_C162_CIRCUIT18_BUNDLE_SOURCE_ONLY_PASS2')
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'BR76_C162_CIRCUIT18_BUNDLE')

```

## Evidence tier / limits

The promoted endpoint, the flip/recon intermediate states, and all29 deletion children use one exhaustive exact rational H-polytope maximal-complex/mechanics implementation with exact mass identities. Source-only replay is not a second independent full mechanics auditor. The circuit-sign change itself is an independent exact four-plane arithmetic certificate inside that same source unit. Numerical coordinate descent and cap screens are nomination evidence only. No global minimum, convergence theorem, affine/projective exclusion, multi-cap exclusion, or path-existence theorem is claimed. Canonical accepted own110 remains C622.
