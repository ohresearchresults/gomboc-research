# figure-0484

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Calm Raven 68 — changed F9 geometry, a new affine exclusion, and exact coupled C68 surgery

## Outcome and evidence boundary

No actual-volume-centred strict110/additionalweak000 body and no certified open U1 SPD cell were found. Two genuinely new exact nonwinning constructions are preserved:

| Exact body | V/E/F; C | Strict S/U/H; additional weak | Complete residual P packet | Complete residual Q packet | Certified obstruction |
|---|---|---|---|---|---|
| BR76_F9_CHANGED_PACKET2X2_G3 | 14/21/9; 42 | 222; 000 | 2 vertices / 4 cut edges | 2 faces / 8 cut edges | Entire nonsingular affine orbit excludes weak-free U1 |
| BR76_F9_DUAL_PRIMAL_EDGE_SURGERY_G4 | 21/34/15; 68 | 222; 000 | 16 vertices / 8 cut edges | 13 faces / 10 cut edges | Explicit closed operator-norm Gram ball of radius 1/4 retains two strict U roots; full SPD orbit remains open |

Both have primitive-zero census000. Neither is an improvement of the strict110 construction record. The C68 body is retained for its genuine joint-interface replacement and five nonsimple contacts, not because its larger residual packets improve the primary objective.

The supplied journal, including shared memory, branch memory and the literal parent payload, was read through EOF. All five source units compressed inside the parent were decoded, read completely and matched to their advertised source hashes. The inherited C42 mass/mechanics report was reproduced byte-for-byte: 9587 bytes, SHA-256 77355e9ae1d1c84d21ea2acd474a35da4f8acbdd649dcb15418516cf49f146d3. Its fixed-shape affine atlas was not rerun. The source authority remains figure-0479, advertised SHA-256 217144c7d9aa0140fbced4dda3ef7c6b34da2147f1187f3744117a0a571b2487. The supplied parent has nine supports, strict222 and an exact fixed-geometry affine obstruction; moving raw geometry, not another affine reparameterization, was therefore necessary. :contentReference[oaicite:0]{index=0}

Transport qualification: I verified the decoded source hashes and exact report hash, not the advertised SHA of the enclosing rendered parent text. The displayed parent substring did not reproduce that outer digest. No row, class or incidence conflict was found. The attachment itself was 196188 bytes with SHA-256 383ea26b8fe8e17b30b38f1e36adb8ff458c60a458bbe255e97a177a9f578939. No inaccessible historical source is required by the constructions or certificates below.

## 1. A genuinely different nine-support body

Define raw K by n_i dot x <=1000 for the following nine rows, in exactly this order:

```text
0  -147   907  -395
1  -874   265   407
2   614   547   569
3   670   -65   739
4  -773   506  -382
5   777   621  -102
6   -88  -113  -990
7   -91   807   584
8  -310   931   193
```

These are NEW row numbers, not inherited source labels1/4/8/10/14/16/20/22/30. Compute K's exact uniform filled-volume centroid c, then define the displayed physical body by A(K-c), where

```text
A = [[-3748, 886, -283],
     [ -144,-162,-1482],
     [ -103,  20,  -34]] / 1000.
```

The exact input is F9_CHANGED.json, 478 bytes, SHA-256 96c1756b4205d01d7fa1670b990db7e597cdd2645c2c3e2faeef792915326b88. The recovery capsule regenerates all rational vertices, volume, centroid and audit signs. Raw volume is approximately1245.014582549009; raw centroid approximately(-37.99457168107147,-157.6380037680140,21.02601047596179). det(A)=0.004708974, and physical volume is approximately5.862741298844. The physical centroid is verified exactly0, not set to a freely chosen reference point.

All nine facets are active, all14 vertices are trivalent, and the exact maximal complex is V14/E21/F9,C42. Its facet-size histogram is one triangle, two quadrilaterals, five pentagons and one hexagon. The inherited C42 instead has two triangles, three quadrilaterals, two pentagons and two heptagons. Thus even the abstract maximal complexes differ: this is not an affine reparameterization of the excluded parent.

This was an autonomous new F9 realization found after releasing all nine normals. It is not presented as a certified continuous class-preserving deformation from the old C42. Research-parent identity records the direction and starting evidence, not an unproved homotopy.

### Exact mechanics and both complete residual interfaces

Vertices are numbered lexicographically in raw coordinates; maximal facets retain the nine-row order. The strict stable faces are[1,5], unstable vertices[1,13], and mixed saddles[[0,6],[11,13]]. Additional weak and primitive-zero counts are000.

The entire physical landscape has exactly one positive bar:

```text
peak = 13; elder = 1; death edge = [0,6]
component = [0,13]
cut = [[0,1],[0,6],[11,13],[12,13]]
attaining path = [13,0,6,3,2,1]
```

The entire same-physical-centre polar landscape has exactly one positive bar:

```text
peak = 1; elder = 5; death edge = [5,6]
component = [1,6]
cut = [[0,6],[1,3],[1,4],[1,7],[1,8],
       [3,6],[4,6],[5,6]]
attaining path = [1,6,5]
```

Exact birth, death and gap fractions are generated in F9_CHANGED_REPORT.json. Birth-relative depths are approximately0.9442442730 for P and0.9872627630 for Q. The physical packet contracts from the parent's7/7 to2/4; Q remains a two-face packet but its cut increases7 to8. The wells remain deep. This is interface contraction and changed incidence, not proximity to110. Likewise r/R is only approximately0.0143730; minedge/R approximately0.0231586. No improved conditioning claim is made.

### New exact full-affine obstruction, on this new raw geometry only

This new graph has37323 spanning trees and522522 rooted trees. A fresh exact computation constructs252 equal-weight negative-definite arrow blockers:210 triples,37 quadruples and5 quintuples. Every rooted tree contains a blocker. A separate exact matrix-tree determinant agrees with37323.

For a raw centred vertex x and an outgoing edge d, put R(x,d)=x d^T+d x^T. The affine escape sign is x^T G d, where G is SPD. Strict U1 with no additional weak U supplies a positive outgoing edge at every nonroot. Such an arrow strictly increases squared G-radius, so these arrows contain a rooted positive spanning tree. For each enumerated tree, its blocker sum R is negative definite by exact integer Sylvester signs. Positivity of its required arrows would imply tr(GR)>0, whereas G positive definite and R negative definite imply tr(GR)<0. Contradiction.

The executable atlas uses the literal new input, exact filled centroid and exhaustive tree enumeration. It does not rely on numerical eigenvalues or on transfer of the parent's blocker bank. It terminates with:

```text
NEW_F9_ALL_AFFINE_U1_EXCLUDED_PASS
{3:210,4:37,5:5}; spanning_trees=37323; rooted_trees=522522; uncovered=0
```

This excludes the entire nonsingular affine orbit of BR76_F9_CHANGED_PACKET2X2_G3 from weak-free U1, hence from strict110/weak000. It does not exclude other F9 normals/heights, the surgery below, or a whole geometry neighbourhood. Do not spend a continuation on the fixed affine orbit of either closed C42 raw shape.

## 2. Joint physical and polar surgery: an exact nonsimple C68 control

The two small F9 packets make a coupled finite replacement possible. Perform the following operations in RAW coordinates, in this order:

1. Form conv(K union {p}), with p=(-13687/2500,-131173/10000,607/1000).
2. Intersect that convex hull with the halfspace

```text
[-98941600938,-877498460778,-6626654272659] dot x <= 7501152881000.
```

3. Rebuild its actual uniform volume and centroid c_new, then apply B(x-c_new), where

```text
B = [[  1194,-150,  964],
     [-28201,9841,21538],
     [ -1200,1440, 8797]] / 10000.
```

Do not swap convexification and truncation. The added point is outside the final cap, but its induced supporting facets survive; deleting it before convexification would produce a different body.

The source unit exact_surgery.py gives an additional deterministic derivation of p and the cap. With q_i=n_i/1000, old centred polar Q_i=n_i/(1000-n_i dot c), let a=(1/10)q_3+(9/10)q_6, m_P=max(a dot v_i: i not in{0,13}), and h_P=m_P+(1-m_P)/2. This gives exactly the displayed integer cap. Let b=(v_0-c)/10+9(v_1-c)/10, m_Q=max(b dot Q_i: i not in{1,6}), and h_Q=m_Q+(1-m_Q)/10. Round c+b/h_Q once to the1e-4 rational grid, ties to even, obtaining the displayed p.

The generator checks the strict old-vertex/old-polar sign patterns exactly: p violates exactly old physical supports1 and6, removing both facets of the old Q packet; the cap removes both old P-packet vertices0 and13 while strictly retaining every other old vertex as a point. The final hull also retains all twelve of those old vertices as vertices. This removes both old residual interfaces, but does not annihilate the new-centroid equilibrium landscape.

### Exact maximal complex and census

The resulting exact complex is V21/E34/F15,C68, not the V26/E39/F15 generic floating surrogate encountered during discovery. Five vertices, numbered8,9,11,12,17, have degree4; all others have degree3. Accordingly the nonsimple excess2E-3V is5. There are16 defining H rows,15 active; input row7 is inactive.

The body has strict S=[12,14], U=[12,20], H=[[0,12],[6,19]], additionalweak000 and primitivezero000. Raw volume is approximately1449.391881813934, raw centroid approximately(-37.12044240186238,-153.1808618691588,20.41000417077584), and physical volume approximately7.588013128506. Exact transformed mass integration again gives centroid0.

Its full residual P landscape is:

```text
peak = 12; elder = 20; death edge = [0,12]
component = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
cut = [[0,1],[0,12],[6,17],[6,19],
       [11,17],[13,18],[14,17],[16,18]]
attaining path = [12,0,20]
```

Its full same-physical-centre Q landscape is:

```text
peak = 12; elder = 14; death edge = [5,14]
component = [0,1,2,4,5,6,7,8,9,10,11,12,13]
cut = [[0,3],[0,14],[1,14],[2,14],[3,12],
       [4,14],[5,14],[6,14],[12,14],[13,14]]
attaining path = [12,13,5,14]
```

There is exactly one positive bar on each side. Their birth-relative depths are approximately0.9569066652 and0.9550187613. The packet expansion2/4+2/8 to16/8+13/10 is real. This is a material nonwinner demonstrating simultaneous old-interface replacement followed by root/interface transfer, not basin cancellation.

The stable pentagon face12 is[0,20,18,13,12], containing both current U roots. Stable cap face14 is[0,1,2,3,4,5,6,19,20]. The physical death edge[0,12] is owned by faces3 and12; polar death pair[5,14] corresponds to the other saddle[6,19]. These are explicit coupled continuation carriers.

### Exact obstruction with deliberately limited scope

In the physical B-frame, every real symmetric Gram matrix G=I+H with operator norm ||H||_2<=1/4 preserves BOTH strict U vertices12 and20. For every outgoing root direction d, the report records exact s=-x dot d>0 and N=||x||^2||d||^2, and verifies s^2>N/16. Consequently

```text
x^T(I+H)d <= -s + ||H||_2 ||x|| ||d|| < 0.
```

This is a closed-ball exact exclusion, not merely a sample result. Since1/4<1, every matrix in the ball is SPD. It is not a full affine exclusion, a chart-wide cap theorem, or a restriction on moved raw geometry. In raw coordinates this ball is G_raw=B^T(I+H)B. The full C68 off-diagonal SPD problem remains unresolved. Its graph has39360784 spanning trees; I did not enumerate its full rooted atlas.

## 3. Executed finite work and a rejected U1 nomination

The principal genuinely raw-geometry survey used seed2026092268,2000 nine-normal proposals and64 metrics per valid proposal. Supports were frozen to grid1000 before metric trials.765 full nine-facet raw geometries survived the geometric screen, giving48960 joint shape/metric trials;1235 proposals were rejected. The three proposal modes were perturbed parent-covariance-gauged normals, independent spherical normals, and scaled/noisy gauged parent normals. NewF9 was proposal1444, metric2, from the independent spherical mode. Twelve successive packet-merit incumbents were recorded. No one-sided S1 or U1 numerical candidate occurred in that finite survey.

The coupled surgery scout examined81 parameter combinations, each with193 metrics, seed2026092269. A floating nomination reported S2/U1 on a26-vertex surrogate while simultaneously retaining a positive P bar. That internal inconsistency was treated as a rejection, not as U1 feasibility. Exact contact-preserving reconstruction gives the21-vertex C68 body above and strict222. The erroneous floating one-root count must not propagate to a future memory entry.

Additional finite methods included actual-mass nine-support gradient searches, joint raw/tree/metric optimizations, true convex radial bridges, projective mass normalization, free-vertex repair, mixed-integer escape selections with PSD separating cuts,25 changed ten-support edge-cap geometries, and actual convex mass additions inside a reference escape ball. None yielded a certified U1 SPD cell or own110. The C68 fixed-geometry scout used100000 random metrics and found no one-sided candidate; the three MILP/PSD-cut settings ended at a time limit or the finite separation-round limit without a validated SPD/U1 witness. Those outcomes are not exclusions.

All complete numerical source units, their inputs and non-default parameters are in the capsule. In particular, the saved treeflow best_tree_margin is an optimizer epigraph nomination, not a verified lower bound; the replay wrapper explicitly warns about this. Low loss, a failed blocker-bank test, a numerical PSD outer-relaxation incumbent and an inconsistent floating root census are not promoted as feasibility.

## 4. Exact verification tier and useful continuation

The exact pipeline rebuilds bounded H intersections by exhaustive supporting-triple arithmetic; consolidates maximal facets; constructs true edges; integrates positive tetrahedra at the raw interior origin and exact filled centroid; independently reintegrates the affine image; audits all face feet, all incident vertex escapes and mixed edge-foot/normal-cone conditions; and reconstructs both complete true-edge chord-min landscapes. Every complete-chord bottleneck is also checked against a true-edge maximum spanning tree. No polar is filled and independently recentered.

Additional checks reconstruct maximal supporting planes from vertex triples and verify volume and first moments by three coordinate-divergence surface integrations. Tetra446, cube6/8/12, an unbounded-H rejection and the literal parent222 all pass. This is one full mechanics implementation plus secondary hull and mass checks, not two independent complete mechanics auditors. Source-only recovery and all five output receipts were cold-replayed successfully.

The most useful continuation is the genuinely coupled geometry chart based on the C68 recipe: vary p and the cap normal/offset jointly with retained F9 normals, especially original row3=[670,-65,739], which supplies the current stable pentagon. Track the four-valent root12, the cap nonagon and both complete current interfaces. Preserve concurrence intentionally when useful; splitting the five degree4 contacts creates real additional edges. C68 leaves215 final-edge units under E<=249, so there is no need to insist on this exact incidence.

A changed geometry must first produce an actual strictly feasible SPD U1 cell, verified by rational inequalities or an equivalent exact witness, before S/H and the entire same-centre polar landscape can settle the target. Merely breaking either F9 blocker bank is insufficient. The supplied fixed-polyhedron boundary theorem also rules out treating convergence to a singular metric as an asymptotic110 certificate; it supplies no explicit global C68 epsilon here. :contentReference[oaicite:1]{index=1}

## 5. Complete source-only recovery capsule

Save the following program as RECOVER_CHANGED_F9_C68_INLINE.py and run:

```text
python -B -S RECOVER_CHANGED_F9_C68_INLINE.py OUT
```

It needs only the CPython standard library; observed exact environment was CPython3.13.5. It includes both literal starting inputs, both new constructions, the complete exact auditor, fresh affine-blocker constructor/verifier, independent checks and all numerical producer units. There is no parent-file, library-item or sandbox dependency.

The inline decoder is29272 bytes, SHA-256 4e36e437033767660f35a771836b593052e43c6319916559d2b75b14ab07e293. Its23-unit decoded dictionary is73730 bytes, SHA-256 ff5a063f0d3f39965ef903e66ef67af4ede82cc389458eda7c3043728ac7a3af. Verified outputs are:

```text
F9_CHANGED.json
478 bytes; 96c1756b4205d01d7fa1670b990db7e597cdd2645c2c3e2faeef792915326b88
F9_CHANGED_REPORT.json
19951 bytes; a9e96cc39b55174816bf1a320cd0bababc1258d22f8bb68c35bea45a710647f0
F9_CHANGED_ATLAS.json
3438 bytes; 4c5f1ea19e4a6963036db0f9764ca980c9a992f7d7ce87331e4df4f6f608a7c3
TWO_SURGERY_EXACT.json
1125 bytes; 0edc5af32eab917ea5a192f092b67f591a683c2329eb4fa66693998651b93409
TWO_SURGERY_EXACT_REPORT.json
40302 bytes; c32b1d309d81b156acabdf98e4d5cce95a1bc09e11dd5f22368dcdb9e23a006d
```

Expected final marker:

```text
CALM_RAVEN68_CHANGED_F9_C68_EXACT_HANDOFF_PASS
```

Optional numerical-method replay is `cd OUT; python -B NUMERIC_REPLAY.py`. Observed numerical dependencies were NumPy2.3.5, SciPy1.17.0 and Torch2.10.0+cpu, with single BLAS/OpenMP threads. The individual campaigns were executed, but the entire optional numerical wrapper was not cold-replayed end-to-end; wall-clock-limited MILP outcomes are not bitwise portable. Exact recovery does not call it.

For convenience, the same executable is available as [the recovery program](sandbox:/mnt/data/RECOVER_CHANGED_F9_C68_INLINE.py). The complete bytes needed for recovery follow inline.

```python
#!/usr/bin/env python3
import base64,zlib,json,hashlib,subprocess,sys
from pathlib import Path
P=''.join('''
c-rl~`*+$%wlMnp{VSO6)q{i!jKEJwWwnzy-I<d(j-6zZAuN^<!pH_8B!MwK{lDM+sFF&69jDKnv+n&qukIMBRPV=r*WQ2p^!m8>^7oUo-%elE
u9Io_Q|qTczWsFa?Wb0!^X;c<^KkEI*QwX*-+mI`emXij$X}|Bqo#W63e4;5?HOO4gNFIGcho3mt~c|~jk=MwscY$W;Wcz8K6K{WPcJSG4|;iL
d*>%F|LgQ)<4dFWTayY#ZtRCC<#m&*-f{Zw@Lw;c&Wm@G)!To5JbiaP{_?6Ce=zd)l9AikKcFHF=Mehu9S)9Nx9;rKhkef<><tEP(;pss2mR*W
z->5theO9XIvm2Z>^aV%TX**loql8Q=#Z+7M+r_Gc3(X54~{XO-cq>^Ow*w_t{;kO^LQWTsd{v{CmIL)Vy}J(uLsVa*oPeZ2gmq!SQl0JcG$$X
>fvEi?AH&V=urdS4-XH;LBkO+(G9BU2p*lLs2(5J@%`8lN6^sz(H_1vow_(~I>I?_cDsLm3x5(noqc+DdhzCE@8b0Q?a9|#bO$@*=fCaFlX$lu
gu8yYC`EVaXc{)Zh2MU{|K3MwFb&;tX&8h->Q^T|d>)iyKN`Dt?UKKAy|gs#U;FSA``&cn$9JW{)K5y`G%b1Vcw9<HK?23ce(hWMdyu5lIPkE-
@zhO&@Cq_cg3yKJq%`oyLEn$v)F0oKU^%H0*Yo@+bwkfDd48M*Lnxm53Dov+<U_?ve^B*CZk(1b-(G$=FZHL>n;YMcu<nH$2X24tm->E^_R`q*
dlNUl3c?cnkFU^+TbPGZkbDc>ur!6?PJ)#mm!SMr>_#KqJ(vZ--6_Esp%ea~1Z5#-e>x8bZKyDba28-f=I;1g7*8Q{5?qA|eoB3JP%B}F)7xn^
na5W+QP~`Pa*TGMGccDprO-zI4kpn57V=CtoGP@Q`pc3#9|UQw^zO~u^Ahygua2SPuoUyun@(W*_3ZV7^fpNRQZ$WIoQaxV*>7Pm!Nk%u5y>6=
oA;x5>iG%G#4w&tN|Bq6U^z-E+c~_#muXzO!O82C-=CkJy?A?a*@Iox`}q6C>B+0hvM9fQcfOYL?!Vp^Qo5~aQiHt~#M7{I)0JhX{4IoDPuy^j
$WEu6_-^ctj(ZCSmZl7QS*Pe%y>h*Ae|VLwr|S2991N}sDKNlmPSq(3*vW1X>(}dP5T=RehL|AA4LHn{4%;4ft>=%&MyK*bo#I2yo*VUa4b-dK
sakHGLR+@SrL%s}-b`kZPPm%8@c^^A2@kLf3pOnEdI&swJt@mQ_!fk{Ub*!xEaAGq#>Tx?(o>1)r6`6GS>=mQXJt{r9AY@0CnNbWp8Gat$k)9V
&qJ#Nd!gnpeQ!?NMU<;A%H16*=-mz^?gFdV!{glR*|peDrsIWg*)@i~!W;SCO;)*TT!EdFx4n0#AAf)UO2MDr>o;d_E`JBOfA;=k@8qm^`sL-@
PnU1rpOtL_SLY`er)M8~Z_ds?ecXb`oI^q}3UTcn<}c2ElV1ogDSXt-b2l4D8{bu~1NC7OPrcl0^v+=(Pxqn!FW;Xv8i1x6>o|fjz~lcGam7({
uPy)w93B!t-#=<JM0L+;G{xTj9$^pX2*7%EZ@*C&dxr$}o#O+s-#|3bY*L=a(E(<u@7G21m@3*ka*iS8017pa4x5;Ah<O?Z@V9Z)pgjBg2f}GK
F}aS|Xa9H~(97|0ga2wA;-+Ia>4pC7W6;MbK`nO(*u$>^kn4}9-VMM^ZweqWo_hrDaPI<)E1jMGvjl)VyaKTI`nVLkw<SR4kzbmI<2!&`ZxF?#
^B5rNJS0>D8S&gCC1?`>{1`A2<^{Aga_31JEc_C{@@X~C4re18``9dk9Oy)l&Qk=JAr$i9WWbkN>1<l!{ak`YSKTksz!^5fK{4PcK}&+q#~N5x
R4PJdorcd)C>;31QZjK<Ybgdco>3lD$!b)VoqD%2fIkAC9ej59xq;7s^i>Y0yQ99>v$O`LHL^6PnC5hCZaVa@tP5(_6@B4}f$+spUgZ67pVeVH
1|_%BuMR4M=lad+SG?-5GPEJp8o;v;&pSRo53Bu(Z$GQ+;Y9#dt$~}m)XrydCPo6LM<9Gmgg+GCodD>Uh{bdaU6|g6ew@hBd_1O7oid&X0E6mf
1kVUgzQ_(hE0{OWrcJX%X!p6>ekI4=#Hv`U+Q84Ki9E*_dR*b-(ze_GlAUx8o4`WYw5q(a&Cf=uE>2O5J&_$N5ZC+-CJn#RNGJim5I(fvi!H3a
aP4ll4eJZVXqo@j3A%_~;o-U~@XfZ(lH5i&Uw|)ap7?{ns>CZjwLnqPmbW-hXlv-7_+th9`-+Z8tQZfIHTFZ!ZQCNOIyU14H<n|d##ElrCS-su
#Hkf<p3?0I;5=r9PXA2?Eq;>t!;jr|Ao+>%s{sV~vT(=2fG`2RWpo2{lk0}jOX?Mn0Bx8%N$m>wdu?+D7_5~27FYDz9VdRfAN%eNeZ^M$UFqTr
<fKfkyTBh0un9d|{dq7R(4G=N8PTYc6i7vhhtaazTc=v)+qWG`oV_o0dqNMK5Bt}5!yDP@w)=Om-+*Z8(hz&bg0?*%3}F}i@n<`OKUjh=J$;k)
Hd2ZD1!|=g9t;RfTEQUUbpRURMke!#<ve>9@Ycb0@OvBkQFEin4+oao){ty-zdG=b-n%*rR%NT6b#O%VRdPb@%1<qwDC+i(qq+obPy7LQNUbrq
g`L7lgAD-7SnOK9=DfuYXp2#nL2}Plo!FwuV}>=wp8Ua+iS^fu_5W#0*(A_}5Y6bJ-73srPKJEEcys>t6ev=x80XCv<yXBIZ$3iOs~Ql>J@{}1
^o_knBe@edl7F}@HTS|L2oTOE#H#2`@n`WMZat`_eDQar({=~f#jQg?XUk#1^N}Bx!F9*YR<v(ZLO)AzZCyv4Prhnip)~+aRlo{iTfKJTuB<xk
+1!`#NEx%KhD0t(Ner=|y`Za7aiw%M*Ig;Ajh68mV5Pce>R=B70QL!>L|8DKT7<5;2mnW8nRVZ>jo@!GhGV$>C}5Rb`6x)G8{W}I|9gJ|0Ay0k
MsJV^uY5*=ZU%3VVS);b@g~3w5_ktLT^wX%zHb*}0|Lv~Iww{8;0A4DmvO5Z(2a^=Px7RV?qxtlPwyb`0GtCrk+GnCMmt7!^u{UdtFF+vEjwYw
dFnDo$WCI`oc&BTTk1%CI(zy4^XbLutFp+x1C82UXEI7ToP&L@&Ubzme%S{~SjxJt_Wa`gZx^SRa4z#aBCkR)xDv%~L54X3L4xd60`sD=ew2Y>
nU7ORQ`Mgi?j(~KNa+K;K@(D-K!Em;1{K2SLYhcJD%_z++a4^bMBt)2sX(hpA~y_y)h8iDBG<+Rj2@>OgUpde_5^iK;{onAzxS#K5G#>ufGhE)
kuS@qVH%JCAWWdm`Phv$6+4alC?*&Z#XSyE0AXXIyph}v!f2in30($U7{hR68NQ*2?&R&;-pOm=*iL(&9Ol$sk;D#GN$<^^%=Q6Umvqr=lk`4b
oSt3+_w?@M4e@xTzJzJ(Tf8cE8~PqvfT%_JwqLeuw=wh&0UU1&&INoo^$Zq6P3`tQQqFo)Uf(F?7hgX@KQ4biY3v^;bYP2-o1na-#sWl0sg3;Q
Ab^!lt<7yjNRWGUKV#112Xd~p@zfnyG(KdofuCL=Np6emt<hzsw;;9nE`#-&#B#__E&OHG4`HRR{0VX{Tu&*2ewT(oSu4R*)q{`mG#HeIFl}0z
q@*APjz-B`43>szs>PMHB=9zpFR9tzk#1iC?VY+F?7<o!#^}xh8U#V42K1vEHWhe4g|<sSBX%q$(|PQnWC~?2IHfRauy<U19>7s{VH6|=DS2?l
0$>roq0lanqgn!;8e?TO*zeGm=4Rxw0~tCkQSTxT#LtfL+(0=BO37}aUZ}{Q%^7sVw^kFsp~y~#Q4N1B`~_qKKVCdd63gmWU3+7s!t%By+ZEN0
aF;<Mos9l5h$7s3&@($Ddazl5)z9iJ?C=eAUhqSsEA@lWpP<aorFo*}ur%?3jYS?cO#Q2vWr@H)FH7&w-hNfm%Y+X8#79P(<gj`_;IzcS6%ez_
8de18WFqT!dt+X!oXwox^`u6Ygajl&yD97>nn}09&tm{$<100*(10zlImZTGF3-%=8+1@|Wjp34Xyy#K{%*x`cltZ3g1WtH?Ey;%#m?mt_c}a<
a!Z?L@3(E5Mll_09F2^=g_U!ol<NEk8Saiox@WXHS3dBzfrtCnB}j}yUF39IrNJEcFeJe8A%s>30VTI1H=d0Bgozbznjqwc1sjY}SPZ)asT&`c
jPa2=V+oM&iZ17b4uVZ!s_^I9)_iBm!tbESzNRQPND(Lr3xD9b!Oyti;G@kH!9Y<JIZLdnKwOeer(-;mTX|60=YWzmMM2$#DFg!S@A~-~8j-SL
aKq=~gLt)jAYd&8oI`*F?wz8kVOVyaHZT&QDgnSJlSg<xK#TybtuF!)D4;b2<botV179*roUwZ0G@cZ<%)<BJy@wy52DR9OU?{(IaHR#nj&Ajf
T6cJc+MurF{z{-MRnt%uE#}^UAJ3ecUv=u0iMzB&Q($4)8ouVh#ul8bPDjN&YDRx5d3(E5Np^UsVQ=hCA`AIghpWQ6V3BC5TG+vVOKN((hidfQ
XZL*04+8YeOKQArQF=VKxT7hwKaH6!71c(KkSic@JrEQ;!(OINi-DiOE&%%HiV<<ArB<-pW+4HWL0O;`ia~k@q);Drq|Ki@RB@L@3Hb)2el0Ct
)f(iS1GP*AfWpYO&_d~V6z;nX(ou<<3#UB*wgZbnIBr*#YWdJ#y%8lK&BB0D5EaRDJyY$O{Ggw)mY+-Sd_d%I^rNvG0&Ez%o{~4k{+Lx-hQbJD
C7Gi}3<zz+T}%nj#IfD(iC~FI^DqET%!(No)ddf}7r@|_Je%zgvHZ|MjE55*ENx;0y-4P#=ez@B=?a=a8(>7+n;Bm}#Q7KM3ePXm+Mi`6S9nd2
A7Wd4k_edc9qUD#EAgyKdlL5f<$CVfL%Gj!JM*bo@4pSetcH>i$o64dHt3s?1y&O{eU%AbY@t!6^lIspglM){0@~Csb|!uz8q8XXxmbu$xGUNt
5n$7K7nXe4S#;ZRgv+B~1ObQ0ZpX9r#2H{>8STbVyDw+E@eE0!5u7(k@XrGrK~%~(h%EQlzNk6^=#6$Nfnvb~yW+yz?s~02b0;#RZd{StgtSgd
Ni_0VPkRL%Xj=7x*h4ic4X9mmSHWbCCm<N7OmD=%-3E-y5Q~Wt98`tSfbwRkK5o#J>~s|wbe)qyP9`5o<@IjZhD1rjtE4F<W3DizuEI#&RfQ-t
BG94$G6Aub?x?h_UlS5<0#oE=m4sI?D_J3YQ_W!3mFBABsA9!1<B?r~nkrO<!2;lE>vfhn8d~AGQ7~f~0lcV-+eqBb1mZ`a0#Wgkx^r2p*Y`yf
`$IUN<wd`2BBsd{uu>U1Sr()$1iFSqm#`lG`VvC@io9gZ(2nYIS>L6+h}DMvLe|^BCBR?Qf=fK&K{#a4Oi7=LX-eof?O$8GVUdpn?iMx!)<y~N
s~Gv!N){m73YCJWwy|IjHi0V#5*y|$At0Gc1eQxx3<w~rQ>Y=TcUm-TAU{^Ct|IIZAyFzbm#Y<v)9zRrazEHzE?EN6k3?@1l<}m~U%TC(6|#IN
e5Fdpk%3_O3E=VEf(5PiafbjxAI~1hGow6OphN2{%Y8Ra%1WvOEda_NM+U7M!M*{w0(};KUR+WB1NahzUYZe_OiOBJt4*|~L46{+n7DVuQr(q8
;PI*%lF10tMD=AxeVJ|R%Lka|yff)2@NOh5!0x>y&$*(Tc$ZcxO)3arTi!-E-rE_r1mL?_F(-|yo35cxI6QU7-lb-3?1m{K<D5alCMy;+VYgxz
jUYZFk~ocHsG$sdnlqGb-IH41^=^=1gHtrr03VVwTC05(%hjreJ6U7vTI??TG5ltXDD`9b3=bAykrw^7y0SAA%S|R(6|2y3?PjH^>3+m0C~yBc
(s~CZ^yVz%S^kk){G^-w#BFZmdSoXQbQ_AR7~g@;@}snLN<XlLv=+eeow{gLtW^~bEuGF*SI>y8;E31X1S0{#Soq1Mf$;K+!%{%rQgF0mnUP&I
jli5JSr7wG0fhv@A`y4Wmng35lt1wg;(vbnz)xyDHYAf9LyKHAfkD}hgpy<qWC1J`n<Et0uBQMtnMKL++v<zgzg<>elm(hT;dYW<Uredugr$zK
{SgyLLI(og#))k1iy;sXM1JpyEB#o<&j5>LgGutGRI`Bdl|8bl6+&)?j7wA`88f#8a-uem2B@mIjU*u>3HS(+5d1TN93vk5qwo&>#aWgx9W_1M
lBXO1JM;nQdB$u!pd@wEIdG(DjPknL1ejR&%D2TB2n?y$fOT-ox=AsSfstC*oidqwXc1s9^_MA&(FU+%fu|HmqxNq6yM*UI@gp}T8!~B?1^m}4
+xAZR+qbZ+co{wu#rbL#n(TdY9&WX;7e5iF{A1lv((Ti;S7n9yAF*%Y3Fcirz`U2c+hvhZ*Mk;9TRD~-ZKm?dpQ26DT@lhMtI8Ry5pThqXPM5^
oR}kvy3T<(60mJy6Qij~o%JQ8HYfc$lP*aF%#2lSil%7nD@93PX0&oc>;tXLkP9eg*u4f6F!pjNk)oDHM(9vRwPia>nSmivhtCf#FiM{P(u!Wb
eE;bq3zAXIER^`g%9m9wvRY7gWiGazE9<ayr{y%(*O(4WCg;I^LKh{l?frpUid(v&Qnj#ypivvDJJM@(BjTdwlB?w<AYwJ6VxjaBN()ESHQ{;$
glkT({!(uY%D>zgR4a?GJvTaL!Sy{tWKQ;i=&q)%E%jH}8&N#H%A_`trS$XEL!cPHY@jaShLntUxvVUgniK|JX}MI2FOtx;Ju|_91lQFi-HMx)
^E{pERlF><-_P^rskfMT3w)Aq_507I3$?hSkmPv+{<mBx<yHIrO22RK!rKnKHSmRw)S4v*ZX%#rQ9f|P>5#!VY(*1|AGFXg3^a0OAaAO?^;@74
jO}&PvZ}Y8n=VNal`avc)GoZEE<?$%O}h@@d)Mtc07T8DT(rDt2!tzJhd`Ru??gAi7I#IJe(h(RvQR0DuHC}g7GkbS=+D%-=ZG&I5|#B8NckfF
pbUSu75kYPqo`R^$%^pSnY46BX?gvzuoB>liw7s)l}bZ;+wsTU=hzdX&Mb>`!(Z&bNh{?iyY;2!4hB|YxA_5h?~RUmxXQHX6E{KwC7}2jJovfQ
5zdz7qdkOf!Y9N=tuXm!KtduqBHz7{G#kPn<AJ3)ro$!Igv6pB#OX+8lRp6Ve<W!Gpz$1_P2j`Tp3$9zb_I4F{;}2=cif^Y=Q(<U9_e!(ySHf7
YR&A2@zMiWX=WRkFT+SXUZ#=BpA;Eyi}XSCIFmW1Yd@m-HZpAzK-4)4$`xH&esOYfSr+(l4TOJ@m<X%ZDQELo?vfC21E^iVqO4m%;K__^HiaMx
Mw^RFT#}2#J!Im&UZ)y$zH|`|ksOp|+BPM?$Eb4w=gItd0Ut?V9Z3a$5euN%WMb{v;-ok4OK3v$@u5%>dLzjA9kl@@3C2Hmx3ZVf!=vD8loT-K
={ev@gry#u9OL71ZK6;+kY%7F=1R=gX*B_AZ-}s5;JBv}4?d3VR~PLmkZ`wf8h&MC7`&MfV>gTDH9WBmWf4~z$?<f@8U@wy)UH@JJGFg#x8Z1>
Z1fB`6BB5aR%+U30O5B>nJ`>2Q0^_l{>1_|k>2ntyS<XDPTJYinWQFcRt8~%7UVcIV2#~ez=)|MMeU4iG^Y#}evdTvJ+eb6fDLQ|afljufh<yV
5n}4cP(`YWAEb=*g1<aDhx5=ug5q_76#7&kd{iTAbPv)KQ<Sxi6N9GMZfZ-ZJ$<u6eO#bq!_S2HDDB31fTK6Q>yfSc7Bf|t*W6N-1n+;vST%~I
YTf$Gz)G8Q{Gsghl=5s@L@l4`h!3V{%5#f*UMy`X@wurdY>Ji|&;VMT!M^h2)TmuouR!!r;SU@<YZ3k=5%0%Q?4y1`+mloWFl?ARyk-+m(I%P|
#xVc>pu{rp5-JY?8oDEYfMz3;DOnoa`f$oqQa`L6EoIBMSjg8_-EL1NvV#v@7XB#Rp%^QDWRlssiGlo#R<obcV)k=q4Cg+Ullj<UIW-#7qMa>S
)ehjn7OyQwG;EY+BWk68XpTEjvYo|_1dMdktsqsh+srK7t_yvgOrSlT(@Ho$q`3Ix;!_`=`uH@!rvd6KcP*z;v78<2TFM(H>GZ0=z)>hhBmu9=
WCDvxBf;%tATcHZc$>1_U}(_3?_>v!yu;j5P@BeS+TOHFZoTWcUHBhO4BvJ7UHG3LU3{$SR2Lt)^0?EgI^Fy@zN7bUn~Wix_Sj8Q%DT3`VYQJN
F5qT)2a^K-^EzJ3kRZwWMBnT<WQL4|-oXSy0lSSQ1-?oABk+|Qui{^VC&5Ch`m@cmS!rwA(iT4g+<u4lq}SaF)LDJUwyPDY`x<r{FWu@F8nmpp
Rc5)`-NhuVgFZpwhdQF_C9__&#yAvc2WA%k;c7oXkibD>ff0U|Wjc3dwovPI9AL~Gx(-5`9)7}SybmHMwadn9cn@HYbi?z$Z&rx!MtyZr=UVuo
j+`I;R`o-j+QHvK<p<iTWgwD7nG*P^=<JC-aexK{*pOh!0MJRiIbuoo*Q|l9=Nm9Wf)}EICXzBq=*U3YEfB7lLhaUpnb`)xZL$lxYY|M&2a}JX
PBuVl)-bmc`kheQ!89b9u$KIx6io??iy5r)JS2h#AR?Q}VF`aw)>AOdrl7oWcL|VSL%@GHCFQjXx`l5a|M|Xm`RU@f(~GaY(=R74*NgKE4&<6y
*^ne9e{EWIGT`h<Ky(Gte~+5?49~wm`*`vGZCMOOxoGRiMw|&!0G}E46Obw^15*@t!`@$?k(L_3ePyL=9yS}zoU(j#_UiQf6#l@hfA0PM>Fry(
aCq8#{r1zB-n)~_%ihV^tKPd)Z060&%bx1-CEGAEwXt@APg5NEO}`CmIJ`5*$~oWPSd;QU-oJtFyg0p7i)f>!KNGTGkxqFAqiGYlC`@8;#<GDR
mYnUp+}&Uv6fI(!|6m?0)j^}BzZa9>5ZKwyAYm1iM}wPu9?wtST$Bao7v=Z=JUc~phVyO69Sx$IarxMt6p5Km%@MW6zNo?fhw$&XYb%Q0a;lKq
uFN`IIreu4Qt||ciDX6G!?bid8@L1q0biIcy4GwFcD}1=e=32(?)9G4p+61k*%5SXziV;<kiCLEoFc{k5S1?g5#YYCR)Q}Uqu~Bf_))?SbSqcx
BX^w0qq;JNju{Zca8byTN#fT?{Fz+k<i9dpj&lL~CULKnlsV=7^7Jj7NTjjKpBysNjkRg+`?J$Bo+q?RcjG(QTu7K3S!kSOriB8{l(1Hr8!vBa
QJAGTef8TZG~2^=FaHO)iu=$d9YQ|9#2Y;RY9eZ5fYB=bUPa^~N^@ufST8iN0|Hpx7W7LDLw6BuGBF2zts<}}{a#mBvA=~c&#8q{v*t8w`zW&w
2WY)I4*D@najkSo2Cr2EmbR76Woa@`(o$bH#1<97G=^GF0O(*p<|!N0l?J{SBzUzkox)O2CsWetqAvJ#?DCCDJd9`q3dd;up5jpDNi-zO3b{$?
waS#4^65;bMW4zuffdgLx86itc>@t7vpCHzmg8#E)pBK7twAR8Hb|XoB_c_0D|dYLPTb)+U7;BZWKnk(H9cRve6-wos0{K3Tgp@)DuaYM8o{iU
sigU}Kv!ke7BhJRmW$+2ztiYeUA%MIM<Yu0RL8VBe--M<!8C`zs!9hw&5ZD}N_nnwGg;lyh4l{j!eT#(XB10=tA1x|hQbXK>)l#@9DL=St}+N0
m?N{Ke%F2_^Zsb8@hYcgxzbL~mXR5+v-`>xd76i8+FBZMW|*dj&3DM(iBZ-;7$5fs(uf^~jzCv)$fPBS+8z(3VhQ?LKtB=IQoPQ0SBlnlTe2Vs
&T{>M*>2EI0A+<rTe6@#p*1)Slf<I?UF&tQxvfALZD)0Lj7qo)!<==gEW_~HL%x6o$Vh|w5x`gju6;W2Exk2?JxPM$o#kfrH|RDcn(05Un|qlj
)XBffEuXV%y+mKrWfvg+Y1+^9U0Reoy%w=;igf4_<S3U*y{2N>R@&&!$j;>%c!diW{S3tbXUGzsA)lDZ3~nB{>w0G6EkbR{7NP(tSOfs%$sWx|
?<FW&B*RJ6n%_?6<3VZU0!XE6;6QRteArueC3i9nuh7m8W`XvupGi3szg_6UnNaNTK;}DL(YQ1qTT`_tpTy%Dih-T0PtWXU^=D+$xaE_`nU6Bm
xmZXf?lkA|=DYJj9a~C1Yn`*geXlpb9F5jebjOzk3j?|ej*>6x;nIF4*(wzPy@sb}aAxh+VnIp{I(eTpg}PW2$j{IAbGe6WPBJ&V8#^qJlVOo$
JL55|<R6L-ykB${lF$r?^rvx|bOr4-TUww?8tGwDl<6AV5C7%zrq7)|ilW>uOPxM<JoRd4_ris@u?Q=*5ld=}np6vH7^;3*5l1?dfBcz^{Q80A
942H%ujXQiH~0QNL^+iqc;eAMBf35xJ<$0rf7mI=2UoV;m1N7mew)A_+HLR78~etZ3<I$$&iPQO!Q6rTBWQJuEwuVmliv*Sfvl&ZLk&=~l^9Zf
_}+2{>o;3BF18xb14p&MQRSf49Vkm+wkaujcaknauk3C+iv5MeUEKEOvGnc$@8&901hU+raG8?+U}4tUfg(g5FaCzt!x#CLQOM188Fw{RAK{y3
NxVDO@7?Laz&D$EB&aj<SU`#~K0Mss9Sn}_92q5dJ{Qg?wAyMiBcitb7V)S@;?c7X@4wD403PsJy@m5az3%Q{HT71NZMJ#Abtj<%IY{OcTg|-*
?BF98P%I=0ab?G%iUs_==D$0Rg52I6_Zy3BngDZkcGa=9o|_oq&%9Ayu?+d2(!yV17iGvdn=)jtAVa?Cwg+42nZffq6?nBH2T(VHtbY=zQV=8K
?IPPY6zF&%1#|tA1kZTm2)~koK&no+&)HkWLVK%NC~p;zt0BAw=R41Og2}nG7`{u3WG`5;;`2LND<}ZKC2K0_4D=RZVA3^RW#n|oc5MeQ&8E6T
Qvluwm^P+*p{f(f<f&`7Ur0^Ww_nm@A0J=Ilbx5<M&(6DK0Y_Zp(ohW7tiGhlNm47>q~yMPAV^}FDftW-OTsJ7`+;KXj*LAg*<!(YEyrXax#Ec
9qi>&6kUF_Z{;6;i%0pTgF5!Ez+aS{tX1=8J95|UHog?iHk6Y10ke(FYJ-h7I`qIM8`~{5e8XacSIw~0@X1oc@1oH_Zi}(axrX+wv2KI`6N7qx
R~cQnXojKE`YNs81u6z=1PG%_<r$u1>n$AgR_lYlVSV5#>jPie8yKx<ivt+Ql^YpfcyO_gX3Pt}#|5pm@Aht<pp6l<rx3dO?-F&2on%^#T7%b4
nI2ImkJgEQP*OyKQf)$#8ETjYBn)v>hTM9@K;*2H$!^o%b|Ag`oLW=XA_0r7;uNhpuCo^#?RnCF17;Q18+{;K5&uEs5M86T58+C?CIyaD_DphL
vZ~OILm~Bh+*53hEFT!xhPXWF=B^(QmtS{t0*GbDfRW9KZXtU9lO0hQ$wiG%=8?j1NRj)aC<p?f{uchZ#}$Q|2Wp9SX1S}2wbA_@lB9t&Kj(`d
6f8+Gw?W(mL?oyqOyA%Y;3)c>f$B0%|GGg9Es!>)5!40zV|ErvliMN<N93EW9cS>$AUeRJR7uBa(Y;Dq7~+dwD#=!rU>&kJQ{Z}-$*GcfzXU8(
$z=iAd{WXfeG<r*`qMN8fCt%X-`J5NPStjR_?IA;f?2qc32gc7z=|Q)-vDx{Lrvav^u)8XmTi01m>4YZh`qVR`sR!38x9_cUEZtdbTE}_rLhpn
nK3cnqnd`C8+&x2_bArZ!ary*wZ5=(v7m)Tb2rQ~C;R2x)*Cm2`XKHpYf}&P*cQ1=JRe-J!^9U3Q0+2}0t3W<*MJ5jHFIrH5C}mtuT-pddf1fW
uQ~lXc|gQ~S;=Wp`J^oFRr~?K8@NRKRZeok&m~giE3gL(>qKb3VnxSdCvQGV7IUFA>cm!egQ>`yj{=!!JKrfh-fnvYa06M-DpD9E!0@)@GGK6`
q#(pXk48#zfm;S<mEEsWFHkb=52{EwmiUYsqGavUgX={<3heMB_xAv$=VKQS>{eQOJ1Nc97+-M|Uy+jjN|ba?O6RJ^0npNIq@y1oqzCXnQ_`9s
+&v(ow*o)_QQ<#LvUmL`f8J{B@O_?<h3Z(Bp#Oo)LyE+BCv&$<+4-qQep{I#CrjjcYTXD_JcvZ`yHo<^Vu!pDEu<2h(NTvyZEq|yIb4!x&;_Z$
gL8kNaK;Qm&6LF-t4vM{ySOFGR-2)(+@}QnIx$&``<d2jskU^ECjm~wa2yc`vtM~vv4?5~kSgtTuEmy0g(jaX_+We~<m#@sos9rZk&1%=){k!q
(PeVT+#aGYBiuuw7~z51Wws_nA{&NKhaq%|Z0}d3F~4R~8mxd{Z75}K9Yl}V1?mT)#~pfTIbD)UZ|*V{>lNE*r;=s{Utnuf_Xc<(BHI6yjNKmy
pt{;bj1N0dYquSWi5{h(UzXm4Ft~}BOr##D;D-r6z$Y8eUKmy;lWI7rgcI}dk+xKlXfA@Xn1`PyHsplv4cg=EJEn!zEH8gI<ts1%p87G%?k8eA
Mj9d_k_M)~A^1#pQsGonF^2CnbsuDh3p%^X37jDuq<j1T;sA#D_wsCj8q}`MWk#7)2WGb~b58K9;so0>GnH;9vb>(Wo`iQ6o~I1Gv0jr-ArKfl
#w%=qs`1+BD$&NzrPC$ejtl@dj;9I0*J<RFK)#A&D*YC_6F`aN@7hg~goK6`K#=?765E@{<WE%T_db!6gBpRCaq3DoUqfqXqAgka4Ie7}Hyk{d
$yFt}()NEepX!iiQ^SB#Bv&FFXaT(4q8fH-3?|CCQhq(D+ULc_e!LaBah4kw6`X3ZUA4?{H7As9QSjKlkwK-G?MJxfI*}$R043bpp1uMrKWkb;
nK3AFvm#H(CQ<@zV!HOizdioaVS9YM!bZPC<T1NzY*$yXgM-huIF-4CO!+zh$R=LOM#cC*9c0G>NDkp^?o~h-*xtwmII{31E1>X}P<Sp=xIlX<
4d5T4yuv3s5wHpcqaR6#4Xq6NV_#-xM9jltk^{{Fj6msdc2vZ<jQZk(ob?6W^Xz@<;fdgl!5f|a3P!JLXK9~hzsWZ{zYCx)f!s;%CTw$4f)stw
N_5bkNj@`eb+T|sa2h|A^wnfoe(k%A%%^(qPQJW(ht8+b1}L}xIscGZ{$&2V9<<2AEhZmw=9SxDk?&CL+)Nv_8`<sWjaIQd%wEyyS!R(F8y?T%
+*Ms>5p~Kx%DP%xdx^}-OKdUh%C0M%qir^62MU%&w$N#Fd^23+#$<^Eo&E3^N`8Qn`Avx*cEV<uc=U3g>i3$3D<=$@5jOeWpchu1Dd(=A?RDaJ
i{d5BRA^x+O|1|KmxD|zbfaEv!zvb`c^KLSVH@xWgxW*Sjt*)P7D<LEx2=vwYhqjW`n1IR=!vahH)$#G{aJlol4oRXL5~R`hob7($elp#2Bsg4
m~;TpDj5w!XLqd8NZ1c}R$eLC54(P~;yXk|U&`>U+rE-l-oUD?R<P<c^L+D(%@1~Wuk!4W#W;vs971I>cPg3J@a?{(|2mI}$Q`YL5NmsJ&_}=G
x6>+F;Six3O%vk8l6EN?-6iB0g?+BY${uuzhV$vP<oMOSnz~Li1H67L9N@IlNTK+4I-@6t7#zOkkvv2&p-8{mHfSm<sWMUMY1QL;Zp8F5qu;oR
PO}SC+BjlbPA4981ti(+$yjQ&v&$QDUH;+h6>lCPkKKfQJBs9Fypu*~EjJmnOGn)_p9s_h+1U1s+vZe<Qpb3aYBI|j2jsD>@#D3&9W*R%kD%Oa
C!JB#Y%NJmd(=!HrfM`JFH5}LUR&%HX;mTT`!@UFH#Tg<JK+Lzp`eQ$60*O%%n)ok9<T>RzciR5q5=$t0zTL%=n~!}u{2*4;Yev*&z*c^Jc#d=
c;-B6E;g%C%lLd08BOw<-JAKDnfbwG|Hfore!*p@6Tymv{;j&b7^7x#!xn^0#$(uuYah5ewN5U=p6EXdd*WDj*1=5|yPKO%QirjJMp9D?pgM45
o#Q>VWyEW%>g?C^x8no-sVhp5w~8SZ9OL`Zp7GXj_M1n={7$28ROjsN8E;32$A>z%@?B|~@#_#uuRZ~VbACaD4w_+RCgi{El}!?SjV#y1_d4E1
!i9ir(F-cAI?Njp;P4L!Z!}jrAzB{lrJLfI(iul^x<wj^bVgT&St!*bph-C*zS4#ZAIAa@Q!jG88$Xq_r-g>IS!%xZj2orjBiC}2v2L2ZZg7sA
C4afk0KY(=<r8!t)puWQ82#k^#nwviCHnp^CH2-K<veJPzl8=Q*GDd};P{}42&xm8>N^1{wkyJ=|6O9@JU8&~C<i>K395SAP+L>6lFB%MT!^lh
UhY~Wpfjr|Xhc&usHfr;EJ1W#wkf~Htfu_UOQHIKZ(KjPNBmN_GFTA3kaNwVYtC&hInjMg<}DBB{pZrjz>QLNJxc+*lzB308ZiJ?l@Lh@{ch2P
a5&pYHs=AdXenc#94f<mEi*FC!fqv{9zK5ylh~8=h~fbDF>K*p!DvO$47`<zm_)1nnPIiRudVj?mDT=Hjm`F(b-M)zl{OER!g2F(VWf|(z~-L8
zq}vYZhf@R@uljuFO8ed-e?Nj@#fAtuYLUWd>2p9IY6E-^8D946Y3}~?b=7^>t8Rst(z<vK@PvIe4axS`e{pnZ$Hgua<*3c3j~z<y7LU^H4L1T
Bw{`n%cZ!x6Z45kCbI9Q-bfw!q&U+ra%Zbp7a>7*3YjFNCuDz;^Etji{abrRq88{~cC!MKN@yQ%D-e=}0Mk&U&?5}Q=6e>@nQ<jRn{Yp|k8}&D
QEwd7j~k7{x;T><L(K4;^7_q}(^m&ay^E8xSMT4IIRH?2MVCx~r<<Y|)uB5dr#(oe8$$MDcEaTwxxSdnWe7X{J3iLYDbVFh4l|&K0(;23t>K#`
0irf=$F)r0q^ILz$`=tZ|Ao|Vs`D1sCHT3AmqmOD!?0^^0+<;l5d9M-<YL8NMizXkF)LzW%mm4$0gP1|HOxnM{iApaFe>x9l6kHLvVXTpZ1xMP
54IM-$MQ`8O#Jm&j3?FSH^HPV5)WN_t3r@54Uofy0(S^81-D7wGR1|se8Vx(cw34GHYIJyqB1pe{Q~<@LRbF{TM>WJnP_XPTMqWVN=vfC?l(lX
p|8yijV~wi1uCgCmsuHhrK>zp^|rtZwD_bYh6i%-5wcggB-xqI?H_f#MZKmyj(=cxp9ypa5dd02r$kV3FNGa3CQn~KWW%lp!{?&+iUxH?UfXiN
N`=Awprr0Tvd(6AAGDx=ujCqiKwP?Uz|Y8oC%aqbTLKn9eZ&H5_IMo&MF9fQ0qipPIl$*bem=tIV_V%hqg!MKYBA6X{18^bHVSvifB`XlIcTVY
7q5O9@W6h#d2kgsFO+2s<!%3^CFEOYHzHoUKDOc8VJ*fXkav7l=>kQ-9MT}ufm0Ms*k^2_kHVT{J{$&KfLaxwv_7PMX_L_?T1mL$TlX%}H@b?k
4e}rh8}dRjkngFkS)n`<<0-&rGVIErIDIbvb^kSMUe%`Kf#FweF5w-KEx-wS+y~ZqzV7#Aj`#o86QKn9zMAjGb6`Z^Z8!F}cnU^`!0prxW#$|h
-!{DiyP=j{!xXf*mPUoV>Q?EEDyhOBykI_p187jM@w@_?40>V%tiIk2?TV#5@3LoKO3M828fn<<HV467j=Pok>P99^ji5%mZT5^C`)&NZE9td8
*AKCNg7Q~T$`7UGP{Xr0wf1d$7qw#)mMHH&phlqoE1ciX?K9}6eK&Wc&+pxxj+JK@^~V*+vZI5k?-gL08vV}4$;MJq;Gs1X$*~jA*W`S+0R$6F
L!(kVCQ{(%(kpaioR(e!?g0P}rwR^AS|tr8GtDkXBUqsANPwEA!Q7+p0}~gZgNt!~VKWEm9bPv~=KVBgjT#+5l!e{aC3Xv%+;5{h%;W(-#LCcO
I7jzmMQ5Q@lnfs60UcS~-WFXB-+tfaFv+G0g?MW0ow#y)tGw3Ic5n=Dx3{<OQTeSkr?qsy^J3h9wt&{O-{Oaz!Y@hmZ#WG0DxSTI%D#%#Q1s23
XWGSLn`>Gf2XC?Icy_T6n?7F+XRnHzgKW3A-|=m${JGx#m_OGIm#wst_jqJ2_+5qlAa3jb5r3;h=druhy?X9$b$^Sy)#jSJRg@nV+^H6PP!f8;
KZ0pl=y$H0ZDc-AH=L;QB;4mOl>}ufG9bAGv;}Uh-g-LiH<ny~#+U`@f}PlGpbLEXL#hgxd7w*CL-EPMJHwG5r+1>HkU0k1R@Z(LvbZ2?AUweZ
=l^T*3ydfLaoj0qP4qsMyN~hfUq{JVp&(=N9=WgF@X3Eq>zSMWA9Nra{}sZ9iBj#kRlBm%PCnNsA=}@2)p^0U2a<}v8{PRvkS)$Sk$I$MLckMM
3iM?oOM^#B1VVF-t`TEVzMA}kK0KKiGecizl-TQI?H94C37I^iR8^_y*^M@!fOz5GwE-&V;JL~I5tV9CZGiwo=VRNQf<A)rR99&4W6E0OZO`Bd
7r+t**T4@hg0eVgw(Z3_!~DW-e_bzh9jHPd#EUl?{!tVW>tDhjC{txu`UCPZihe@r5zYighxr#g_WRu`{<<!~TH4K-=TY^6!m|+aZXnwWIoQ*l
&H{CqStukZ1@*vHu>Mse+}CL}*s~wt)Qm5MO+#UN)|^+`t;rJV4Z2u~vhcQ4lHe}FGx}ws#Ouv`*D7D1^BHJF^?R~>mIWpdlO<&M1kAML$@?Mz
BVQtC&F^28xt6NpQhX9$#8+m%O-C!te2I7RVDCGE6D@){IKp~ob<?}!mvxz2{T>mE^`+|BwU58j@2;|tZqG(;DrfayFR@~Zli^ED+g*>?0cl%E
GK30f`EEI^^U?o+ZuihB5eJFY@nQQwz|`ANG{1vs_}@Cqyl>t7(nL(VlB!2L8?u#S60Fpk`<b07m2q0im*MsT?bQaUx!N))_L;Pzc|c!iTPky?
b^G3q)ekuE&07_dkmHx3igg|-NiTX_BE}B(=YVk5%Et*EqS!cbF(e$)r+~$j%7CxPW&v?n^=o5<_j)0E#Byy%tg`E!6t@a}DgI3!w_q`l{4`B1
HoV7g$rE8Dvi3}_b}gs6`qj%OuI;l>b%4JVd=AEcJAw%ajp*lUd;>_q;VFRErVx6Vh*t;(fsax15M_{W5=7%lPfbRhFSl*)2)1^#t2}wOUjh(Z
1Box~?LxkH4@>wM&beqBcAuc{9j&=jJG7Z~OH5H8zW+DGeOUZqk>9&a-iL!WBz}lQwn_XVG1JJUt%8`oyGQiLBENqt5uhRZ>t8cHTJY+_7_unX
dq4z88$#X)?w4edp^e}{ixr_6Q!aS<=G7^RVy*>MC#arv8R0zw%!d7U8co9(ML$B9w*^}4oO<SC^puTnAL!e_FC3?S1c%8%rjg!e_*T4xe-nwD
8B@2>y3Z?CI`(H9>Fs_rfHOFfx)5CtEO)EwRbB40cZ;8)+q&4SSZuadtniupiD3LD+PRsDo2UYR%`THpbjR#0r3lr{9o23&HBi|zg&Wi@A&n{E
U;78P&(=-Cm#r`ZJlNt~_9O8@_GdauZO7Ph`G)J}NXgt_+&z{&Zg@Dm&$oX6`bRy;W}d9DcHYHMSfC;scF4wDlb%{HLSf3+_B)|I=bnJWDsC?@
TLYmMV6D74?#q`aXOESb=OhWq&ELs)BBl5lQpK+IuYtb=-ceE70MaG)A|ng*LoRX;efvM>K#O*OVa~c~v+5{!F)aQDo*`Gnn@q#Yf=;)n@4Y;K
Wd^Q;|F3{Bg-r}RsNytA`S>5pGpq*^m;~cUydc-q;%$IIj$URWElp2e#qQ+5y2@PS7;5(`<l3&#WbO)GHH(gVcJR+WC+zVv{AqN%+L6(a0&<DL
mP(iC^l5+<FVX4K04rOfb10Pb3iZ|L?x?TzEUkfQjbhn6&B@ySF@5&8u=GEpe9kW9o9g0@Rq!!yZ(Oe_h9aeFCFH__ES|E!oD+KBI#CWfkq0}I
9h5y^7=l|`gzV;G6`wHbWs!)b)XGMp&R+;@$_?gLZ$O@pr?>cn?#+$s{nJ~^oBG3{7*D0*#Kb6&iYIGf;morJ=0nfrnF$*D8pQha`-rZg606A0
*kQZ?j?qpH=u2$NB{F97u4<@#EUp*D*#e%=F}Op#BwFMS)%0eUx`6@+T3Gf*l`J&9wUO4=9^Qy}E&RyEeI0EbbY&d3Rjbves*Lw`wJCBgmu}}J
18e?JRkS1K0yQR751fmNHUD*P8x=h^kZnl5cd$v?LshyRySrs~@fTh7yjXEW()85oR2wx>b!wts6Y#fDLupY2B!^Vi=JR}G&rO?hObsz@-SC@y
F0XP^tU0+lTDK7ADMK^mzEY-iU{bo3rsz~_`}mv9BOEZh+n)FH7y}dl0O;sWmXlH_BdUuy`t&$R@A5KS*MVKk4O{~TX|<GDk&=bN!BWae_VmVU
V;C(U6jPd05*CjmtFY|C?1J&EqZKe_u*Q8cN9QiNwnMHX3nL&79tt?vw*n8TU6e5c_VIfRWa+P%1W_;c$36640ZWT^<tTn*8iE-P8f(ECKn-7o
y07u8EtE)Dn&M%-6)<h7uY~6gh<=ld-RLtO0lr`$799OjZB=yJZvB>N4$vUH-hGaTqqfh-pF}+J;@7MmvMJGmC%jMKAKTeA_pQPv4NlNL0bmcx
f%%c;M;#?RqR{8S(80H7vTkQ`3Fh|J5z%ibm08C<oc}SFN0d=*F`D_`<ZmYXb-77l=P9{z93!4<l{pD5ct-^3j+2Y^@kb~pt1{lOJ_5EyFWPqB
`PtIkbe};(1bJW?GqIZ%Ak%16vyTsSa*x|#^qV(!F#z!`PI>hlX|EQ*mRkTS&t<7vuQ|$}2r^%Zc|E<P#180bbmG@kuz>)@6J&#xl-MS(Sr_m`
x(W{Ki4qSbIK~bA{-X*Wh4IpXDW%}Cxij8Qr%q6_>eOpMfNdEG8h%58RUU9dMbYZ4R$0_C=%V45f=T-t5c5}P!&^>fQAJycD8J>IRY^hy*fkVI
G0~qL%JQsC%h=-fvK!n+Y^_;2M-3Y;)y$||ia+^y@fH2}=Fvh}_h7z%+VsjB1J|#;6Ek#bDiTn|3)hiAAPWWbQidbJj~R|6_Fs(+qTCag{yW}@
vGruDc}dQl^cKz&gYv|nJTWLw49fqn8I*gu2+cwKPq7c{BHAbZ;fa5E;vb&)hbR8w|1SPvUr}g{b@t)^JnjLI>ouE+8#fOhup7txY*PvZwl+F+
)Xka)jl|b&Lf1^)_&_Z=L<k~bRPrOT;sAXiIkR`;02mZQ>t8FqM*CqrIKaRt2P%LB2UGT8ZxABQ%(BxRdzPzQ*!w`E?<{}SPF~fu5wwNIK$sjJ
>oc12snA%!9K|Uw(4AcFLdML@A(eL>7+<$NNKD;*a4pa(D=3SU%%><sDY@22$%cxO8|YW%l^i5wRm7-oB2x~=tb;a7Ymj7?0?EYAzt(}WM)%BA
&WG6>NXzVkz)sv$pI_gU1xBMm<-fgC%yENR#*k-Bc~bP|wQDu%s#*m>?*ux9_5`=Gh3Zgyf~WV6Rz8tx%JWG!$$ig$hIXlqbvEEmTSt&trJdvL
B=sW$-?6X%{YoM{Y9W<QZHxQILv{O$>|yRgu?U41iX>E>+es@}FQYwW?~*TkYY{5`A;UJ|vjuAR*9QX|r*>S~7^2}eJ*~(ZnJ2kBk{kUNZkefU
!YSHzv9{fZr%D75-x)82wBHDqzJ8-<OJsRlFE0@BaSY8#11_vbSGNm>#doG*vA&&;Rm&TJmG~U-)hz^trHX-6Oai<?FR@L)vgtJJan$x8rF($I
5K#=ajXJjs<UTe2JpDm%tpoqQeE;cVIls!Ky_9O}*(@%sIdV?P1KO_*w-7-VYwffe8}{T1X=~SV(0{}4Y~0cvsAdhJrT@Xbdq5-C1rYEX3yOY6
1y8)QZ(RC}79?IP|8gUyF*?A`(G1flkBV6J4{|u8{UYo}Qy{VMS~tu@Ro!x`X5K!v)g0Gf1C+;Pk~Z3P)3KY2uM{$yVsIx-Ms~{Y&ri=@ygj+>
oqc*o!SqgEUBddle|Nr?^6tOh7E-#cX;Om`1o1S)7?@?JoV7uB3-G#j7zsv+f`w!v4;YoPxB@w&ZRWum{l27IV!zY<{s-l4e4*e+f?%QJ<Z;l~
S<cCIvNCG-(;keYmyVEpODw=arTmMwLmd!r%IRdzet>~E-=4fUeS3*cF7_}aW?eXY!Z{F)x@a^+6GKv5y#ME==>?#A)ZD9!L-_xYVs!2wLC)%)
(`bsl{k?q(+j#^PRrmIxmc7Gc%;g*(i2a7s6xC*v@-&VPFiU;EE}F+w(cY1B3@HatsCjhQ#FRtK(>Q>?=)we3_V*8j(`;gL{TLGVkN1IQK0a>n
-|Sivbo+O+*K|v=TRGaHr##n*IWp%E>)ktqy7rsou(ts%H5*6Dd2iz&s~?Rvv-r4E*!$C~I~75GB=cRs{D-1f0OF5o{%p>S6%YtO=h@F?)v4ia
k1aGz9$^P-`MBXKq2MMVRYEvI@v!m%+Mjyp+)s%kzHFf4S?6OOnVmdpe6&RqZ4qs<Sfqd?$~~cKWmMCC3}KJ4;Ih+gW4M@3_XpJ0+?EkH2E9If
L`mY``RO`yuWiJN!R9pTAm8qG+aKzLJb=tM9n%B5#xX$hfHAqxV~z#wBQ(w|4V573qm;uyqiVX<p;26WGq4O*kq4JSnSl;2gFdjd5087|%Y4r#
y^a_|tx(h$*f4Ex{y@MOe`~y$JX}m3EXLoA6+_7!7G)b%jq|F^;f&xhJ{oxn?9^P4h)YF0`O+x{g@NfMXJMMK?pIymRb5-mFcQp<27)24(4`$&
>U6e*c<FvGqKl4no%;+S_bTKvWSbk2JZ;Dc%3~*YEmM=|3$`->aDhaAwDKQ`rOF(-WMyRzJvJ`Ik<A-?FFIL=1Uk(O$u|!)r$2nA)#^Z(h}A*S
KR-LhbA#3mn56vblv^pZY6RNj+f=|B<(UWMh!seHLR!Wc0V&_#Q6&w&=v;n5vZ4J!&Qz43E*h$5FTcV^)7IZ_m>^umwIWXjs6Z*aUl(H%_`~iN
4>H6y`Ju21E7r(YEc3LXu7auHFSOJqJ=HQ*G32PdFn0?ecBgTV6)9@^G6%e0a^E7=FKV#xj1q3(!=-UQ)R@}bX)aaQu+`O3v@;JGEKbeEG%79>
+a-s5**am1Sa{+lH&U6chk~dH*`IRMc-W^Z-iHx{f-VNBLcATxhqNw3-#S!``EC6Odywz9w+lI(JV#yU;HGKPTbQ}@Z&{+=Z=59^DEFD%{#lJy
&l3ErVTJynHw*xe^Q^f^Psu^>n+?Q5%~p44REf1~g`@(Trp5(CH@?DL*a>vPy_7nLlBtg(CwG6N+el`F1H8Z&EP?evKjPjrgE`vOY#|O&w)ODR
v9ahCW3!PD@NEmwb}7zH&~1D4aNTY93p*$1R#5w=kNrTpJ6^R>>7#H-Wn_%ne=c3%KG%{w;GqGSc-4NTZ||}T{@YOAZmdf?4zUB9>BZn4p%LgP
Px+6BJGwE1t2rT~!Z?|X+zkd0L0*G2xB;pKSeJ`WiYcFq1;s(q87Qzwo=Kt1xs;2|xJV&J6q>6LNOKB{L`e&kwCLI`tbZZq<aWgffuw-Y^h!r6
f-<|e)FezQM*Wx@K~;IlVeW4%tR#bdnf~E^d17|ce4FEm{3M}MOh1wen4Syr+^nwCqSJ|){`5iMt)%>uu|6cq{j_$?*T3hQue#7;WSrfTk=<o~
u$4FMb6Y6y*XqJM3q06Kb}j@#wq51WgEB4#iw_&0KbW6S&(+7gf7$Wo$+0Vy24?(le@31vmC@ACXt!~xNz-PFnrl*8?0b|QoRLxk)fvp(XCXY=
tS1?}=<wQ9ne?ZFyV3}FSH<-wrCE(sHONZt0%K;N?;rD5QrI^6Hnl!zxUi-xJIM#9d2nl17q^jgYT|Z=e<#y{FUtT;%M|#$R<G|XnaP16G67P+
9hcdk7Ni0(K9BpT3x#ESEsr1LHw%S7<QD|;^y8^J@Z2QrrBft_lXQUnQZizVtHi9%muU@`2dlcA)pxb~kbr<c_N4_MR`reRj4NG3MdhPOqgdz2
9nsBy?Er(fQ#lBSWm}2L@x!NWUldH8_OF5CTJydDby5QSD*p?sRnghS>Jc6?W^%Qvtgkwa+b&#|%$->nyJc3m;`PCPhRd{tpMjl1WSwGZ`jO~~
UJi?xnq!F5?$6AR9||9-^f)q5BtOOecy7VAs`eu~jqUO5fjl$HqkB#pQ<f3zmX-DxT5#%>akTR=aKKhD-)!e$*g%#3T%s`Y2^@~G8wcrK6%GzO
xFM-`*xeD{^rXA`tmJVKqueRS!^ym#q(M4Q`L<j-3cMSP53qYLxqGh21{Q)>ICLg#%PX|LYF5l?$&giH|G*)wJN7O$W#dq&0`y#R8{zca&T#Nh
VaC!zr@4k8VgCT=uEgH5BVZeI2DK&DyqyfUIXh|7wq32h<E@05|4oM|L$S&FsZ!mn7`57Gt(ToQ{TziyN92B;vyAh)Y-;LLc3ZN<uhis5-tYB6
LE53fF&bBmt$gyt#XLj-DZk`^_-zoLjIStF2|-k4(D#EK?uxpmZ>_4U%)g4lUyVvJHTV0n%I=%vDOX_4{$-!8(q$^7+*o1_?6A)neLq$C(J*Tw
$0&v_;M2MS-~&Ic>8UqwVaFW1NkiUDZZhP^y#*gLcr$VJpYbt6XiPboY3@JlWTwGRW<1zQ+RqGydDD+Z&~1`J%qVhdHnms|i1kcg#As8^DM2#)
gNXMwLd1JJBWw%*MDD*&qgC}wXo0RIX4)eh4|=ZAMn&+<t0ZZu#?vIpJlx#p$_4`;=5xhL4T-l3)dxY_AF*_=r;>U-L4thA;(Rlmpo)U&Mmjo~
!?2xz!3{F&hkU~Ppkhlc)~B`AQg(NGopctvUFb^hlk;$I=6_Aic6#<I_fYfQa|BPgf-0~`p!99HvgPh}M>V+ZMEqz2q1<;3?Lyj^wCgsVC5pOW
qOgvBYtSX9@rrMRm-AQp2zaSM3H3aoNeQ*A1m#hl7IT_Z<Q?LZq6yFBxZl&ty28EP{rb*L;lyZ7Uv?c<>GCpb^CxxQlREE7o%f{9ds62;sq>!H
c~9!RCw1PFI`2uH_oU8yQs+IX^PbdsPwKoUb>3f9=N0^{*0(q$ebU<f?`iEeG<8qfxhL)1lXmV&JNKlWd(zH5Y3KgGtDVcjvz}a@zI}t2rgOGr
t%3hxE#8_E&skUDIX|Sp+pfQ>uj}tvX$Lr)E_6ReW%pXSit>U1MN_%v5b*A8RZ;4@N*#xlA_ltE1OhAT*rEGoGz_IUyf+|5ocJ{_0aO!>be?2{
Y;=<LB2r}KF%p0rCi#XUwHZ|G7f5m6FJ}``t3Q(V-p**$#fQ44E2q&t(avTJOe1+-&*Tr6-}gvA8`UY!0zPa+A%L{}YOn8xL{i)*Bqn7>E+`(=
ZRJ+N*WuwxGh!|%en5gT=7Ja~E`Q+~Dq4dmM0V^qc?sRUZ2v}m!{}GO^_$(k*Wn2AFTqtv+7f&)JU#)bfxYT{L?HqkevU)dPwva|SHsTX$kBz?
`LBiK7qyReo5Xfo4e@}E*2|X3#m><Yev<ogVbSDPcdE1;Ev?^CPPIC$=drFuV0T+sRi`i9E^J3<2g%?nBy}Kf7eEEjJ;bo7rLyV(F!qV=0Yrk^
dLav^!NTf*rjE&-HpAxtD0dGw0UZs7mOUsrAm<4PwKbrF!-jZzVY(J-2Z13Y|Bk%TZeL#`jO_#@0_#UcQCv<S-d~_Lv`f>)uNdFWcx|B91A)1m
?k;Dhw}$cN@Eb*jQ)a5lwaF-_mike*y{dOwjl=HFMu3mTp~>y83z~6}X}hqznMKJo5;bPcY>SV%ESdLrVQ*2A-5w+;wkdpJj}jbG2DW?!7F94O
!;}{XjANd=YQ~CFLF7E3&V8mNGv^hG1O}#<23;g@+b$$G4qF_sM2B$0_!Q){%x?cnC9zu!m_HWMuWIzGf=`$ty-wl9M~8TV{#INRwduz_SRzr#
`Y-(Ebonpj*x!<a@-(_#j(hk>g;ltrt17v0jQYZRtiEbZVYOXjh4nq4vwBEr<?i(RJKmb!3Sg2&YAgHK7X&F`N#%Lx`np>^$Ai@N%uZ2K1yDYB
VAr~zwZ@z(TjkzdSxq*#oF>J&CfJLRw?ezQN}HJgn(qR==TyJ^Is*{e!86h&bA&^V<#Ikv0t$)9a!&vpW1tBV6~Hv7BMcW}?V^-{3>Xk4A&HZu
<i3MN3f8OL12rUyo8m8R`v+wVnrci04n*L<1ywF);zcgHVkZ$B0<4X=j9W!m+k{qHFhvcM^P3U2$Syus9DGMHjV2GReO5X?TGuceZ1Y4DVa8M!
1*}Yn_^*=lu-)`_S|u8w<WBm*)f^_5ec+Uep%)E73)+lTy@XiqokqQ~HB)uye<#C0Wq|6ON6K-46y8loHE--rB7}>`mLfB%#X3a+3~j>gGMEhk
OfGoIod9OypP@}ITa;@+bk1gcyt3`W+-uK4y>W2kt6)jUZvmpPtfBwBO2Lh(8rvpe41XH<&+9sw1rih0cQ09&<YZ#M=Nkf|iCCGkm|PUIAqx3#
2B<7!ljVEjRQ_DLe0%xfyhLHq0G|@os3rW<$z&Sxeq={)N@sTC`w<>%A2{PX4EsygFaDAsNzfmYm$I#-9h}m-sPy=Z6pt8F*Q<#l09JLOC$+A$
B2^%($WbW*8d=x#G~Apg%s?slpwD#r$TLlqdOA92Y3uR6?Vw4DZOXljP^w;1y=8A)T(E#^M^!o?j>d?YY#Wa;w7W{VT9gqfiTFI7(is@eLyyCW
)!^&29{|JPd193c29ih*<pL}8xnrKDjA{9Ygwh+yrc~8DHt3Otce`=6vakP8-yR`!1@;;!p7lk|PDns5bvj6~1%chlY~olBy2AO~JVaa@eYC}j
7G;}&6aD4<!<26pgqnG$i;_&u6{s#zY<onG?8A$rB7L-X9CQH5K0Ou5_1yw&&BhcW6M$@(U}{@n>l(69&IV)8tbhzahh%vVO$yP)U6#{ssYjeB
4Qm7)7Zc*BOiq^#$*5`4^Kb{+8`+#(AB5S|_bM%dSaWsC1FbqXhKJ~GN=3zLvMCHDh*Z{YN;?(`G@ZKLtuzjI;Oz*A;BKXfkBC9**$W9+3XV)W
?3WbD-*OQ8v$B9ABq0Yi>Rm(j2V|_7Xti$VVp*lyU$qcEGZe@PeGPcXQ>aw_LdkXwnMtH)r1Di-5W?mHSe1Am_}mJM3Q&z2L8$}kd$(&tUu1@5
7*o9<OJ}#B_er`lL2zcwf)BP}QCx!Tq7lFAUI8#WzC{0@b;AXi3*Z996Fntj9T^{&sO`*OX^cITRKkuyxez7f-*FOqh_!mkOX+ul7jKtHlh~Qz
3zmV6lRKeZ7eD_GOM$n^U29i9`Xejb`teiQ&SUlFGS^2$?fubv5Qfme*|RC?)=UHiG38#pz7uSb+9k7yrJ6xeY}p(4hgZpy@bXD``6Rr25?($D
FQ0^$Pr}P5;pLO?@=194B)ohQUfw6XTsN`eQzBONhYYNKM6B?A3#`3*E+*L9Vu95(Wd~m0ev$(`$pQWklmj%5GC9C6a1KmSK+_NfI1Q5t9u`Fb
x6@=EU-|K!8RV|$UZ9GM4D8i;=y6~>1Z)ZPSH+8{lKX-6T!3eg%^bTabOO&AUW)c7=!JcNck6SFN5*ElgMqKL8g2bmF+blz46K6nq$3|^53fh0
<jeps7@`p<MsHzH2zYG_i3q%PjHprHny6`chLSUo7z3pe>jDU(Q!=r{2pB!=vOgl{0xWV^^wMc>WPRSecm5eI>x;L|fy&;ss>L)Qyp2l-d_xy6
K(FU|4#eUXLH{%k;B?Ur?Fm>}C=F8uX9+P_jNlgb1qxBwPnqWZ=r-p1CY*KD#j0S5sO5nT2@uGY>#+=8ANOAVescEP=_?({puG^49$n>BmtJV<
EG*qAV^AhI9O`8R&o)QwGcS|!*<bR#`X%o9JH9}ANB6$F7`ej;i?@**+V0{yWO>ZC$%O!_vOdTeU2y%?%hsaZcN70)vn#JLoJw9lRK)#>F`f%g
Os9NO2DYVrzf4Kn6CNDf#akl8?ODgi$3p$H+c%_a!zRX&7|%o+iF9^P5Vx8mYQRLISBCFA>QHhp>TzUOX27oPj3f9x=(Z<gijf5?(b;77ojvCE
iB>{E2H^2#x7+>IwcDdePR2WFRDoJ2e8IF&EzIl+Rafs;J$q+7<2MK2+LIZz_F+p~$7@YF;s9IfLrYL-wv*1NrJ3E1q_@-G9nFaO9VtnGI-2}~
!I>g`0~MG}%iSGC*_G6;Cdrq;*pWQX2uC$SQ5+yc4&v0_p2eWqbDV8n8a$WFs^_&oz+M~CW*hzL8Qbj<!6;t>;UKq#9J`Pg)0CktZ#K(0ZU}xv
RG#`M{IKzM&%^~@7dW6cS?Y5von>UL%SNbzCJ^0D&Cz*D%tx#izpr1Js=#9GHkFjX2!C@ET#K9Qu^3OP&u@ZBS#WXU(77Or4}&p5EWFuF-glsV
jH_si3xVTSaz$83I+yv~Z1IBDE=k0EF1~ybU%!euM&OZsH}yt6mPeyR@52Ya*GM-QU)Y5pHktDYD@mTohW&SIKF41>yXn!7WE2&tye|};o$m;>
`?HPjU%#sFC|bdbsdTe6Ng#D+KBsRuKe)R6PT89Rk_j=CnTkk4V#0p3)1MXd&9~*q*ac{Z?x+~|QzWFdV`ZD4(`y|AoOA`@+#cgx8JQ$uv=%M~
5=M$7g9DUBr$et9d4M{ab%kU&9xC2}9GMaBvdORoUmI0(axVLk_#peU{K}`g1o}bU@5LJ60b}13Z+|Ga8Y(!=$A7->U4FXw?eyYn@5Slm$NwNX
m|49;wPkT5uCZgnm{3uE&4FsL)8)_ne7<fGU%Fv#Y_q?YFHg=M?k|UHG>y{_js;zjOyrGPfTRcHevcBRbKDdf(PX!A{t^ZJ`pwy!%im95;lOc!
ZG=5r#86KVe=p|Q1LOsBC$LA$i++6%Is!k3@DssrgI^ovJibo27GH-;Gm2a0D141x2{R7C=FmG^;#%z~J{@R%N#S~y>+yNig;gh`ta0?e40^u+
ac$j@Bbr>5pl-U-jfCvT^7Rc2H>q5};1m+)l+2><O(Hw5Lg|kJb^05nAvN+>b!h;Mtfiq#(@alxG50Zgv-Z~Ow##}kq*fbv%cZ(%+h+aBvTi@9
<ROjQ!%^>0)q^^n$m?Zl9i`B5Ooa~VaZvBV4x&gPkLs6uG%pRo7!nmeb{q9Sz-9CXfqR9vL9BaG`Za{<V}Q0LK<F`x=R^s3K;V>+vEsO-rDP5u
)bnZUeR9yQ3s|Bda!bT;aK!M0==*zgJ++U2RonC9iXG?y%9Pi_=4RTLWv+Zdffj19&`Xr54?~Yk0X$zTqq4SEb+B4vi^7A{A@>;SkjPXFrdsIq
Jt1xT(GuF9br5%-Zr>|Dl$pSk!y>YLutX5H4Fq|jBM%dQj9X?tc9B^f1jC_^9DIN`^@-R_O<qx1Pib{ch_qMkKTJvc+RLTflCjOMgqF)rnkwyv
es+v!rQPsnX1mL!z0RPvQO0lTXp#8Xa2HkaXPI-ZEs<mK2&bu?JKVy`Fn(;k1)aH}$c*^g=t}h~RC;Cvh@Q%{8Q@ahZW;GfE?M=>nv`}baj4zu
v~7A@;W^o+#VLk}%(XcKHW_Q95@%{$_#R}GF2|1K0_%F5C5l7Xrm(2NK~dJa4rlS7QsFF24UW=~yxKkZ@f+hC=9JKFWl*_hN(oJnHDzW@xsbGI
81(kB_LGobtXAt5l<kFFJl1luJ#k}2j*`nY+9x|~l$gbpCi_KMCy5p0-y%|X<E=vV1z9c@EnU$d@NxElI-5X)zAe^(tg$WF1Kwv2I5e#Rw-^In
f7cqYSqU>k!2dlh0g1LZFJnK#?yyNJ0qV9gFhn1$kFhWu<_3n3ywGhJ8*Y=mlhAM3(h}f{i}x3~4A_ri)IFNx#@O*XaQx~~cfVKl_Ey-=7wX$a
h|i^QC!ACOxv>*bX)L)1>POwh&snZaL$GGu@kp6{w%|%&uP%er7&r`kQH%1wDW2E-*eeR#y!CdpF_gb9haYUnJWZzU^vlW1kD2Hb$y6dxfmW3n
HEsb-{1>E(TBNv?=f9qifxsHVZ8$nQIMMCEnrXK1(Al{Gjwv(#yHOPU-hN%f$4w68&;RHD1r~DFY5
'''.splitlines())
EXPECTED_DICT=(73730,'ff5a063f0d3f39965ef903e66ef67af4ede82cc389458eda7c3043728ac7a3af')
CHECKS={'F9_CHANGED.json': (478, '96c1756b4205d01d7fa1670b990db7e597cdd2645c2c3e2faeef792915326b88'), 'F9_CHANGED_REPORT.json': (19951, 'a9e96cc39b55174816bf1a320cd0bababc1258d22f8bb68c35bea45a710647f0'), 'F9_CHANGED_ATLAS.json': (3438, '4c5f1ea19e4a6963036db0f9764ca980c9a992f7d7ce87331e4df4f6f608a7c3'), 'TWO_SURGERY_EXACT.json': (1125, '0edc5af32eab917ea5a192f092b67f591a683c2329eb4fa66693998651b93409'), 'TWO_SURGERY_EXACT_REPORT.json': (40302, 'c32b1d309d81b156acabdf98e4d5cce95a1bc09e11dd5f22368dcdb9e23a006d')}
def sh(b):return hashlib.sha256(b).hexdigest()
def main(out='CALM_RAVEN68_CHANGED_F9_C68'):
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 raw=zlib.decompress(base64.b85decode(P));assert (len(raw),sh(raw))==EXPECTED_DICT
 files=json.loads(raw)
 for n,s in files.items():(out/n).write_bytes(s.encode())
 commands=[['exact9.py','F9_CHANGED.json','F9_CHANGED_REPORT.json'],['atlas_new.py','F9_CHANGED.json','F9_CHANGED_ATLAS.json'],['exact_surgery.py'],['controls.py']]
 for cmd in commands:subprocess.run([sys.executable,'-B','-S']+cmd,cwd=out,check=True)
 for n,receipt in CHECKS.items():
  b=(out/n).read_bytes();assert (len(b),sh(b))==receipt,(n,len(b),sh(b))
 print('CALM_RAVEN68_CHANGED_F9_C68_EXACT_HANDOFF_PASS')
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'CALM_RAVEN68_CHANGED_F9_C68')
```
