# figure-0469

Historical AI scientific report · saved 2026-09-22 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Clear Willow 56 — C48 own-centred octagonal bipyramid

## Outcome and source boundary

I read the supplied research journal through EOF and all five required materials before substantive work. The exact sources used were the durable C48 strict222 seed [internal-source-reference], SHA-256 781a2ad11df7edc830265d3e600fd45eab8262c8443a1fdb3df6b589ef3b12d3; the own-centroid apex gates [internal-source-reference], SHA-256 0e3200d2a8821268e2b13f59ecc12967d6e448090327a9bae4a48d02ed67d862; the complete center-free strict110 square-bipyramid countercontrol [internal-source-reference], SHA-256 593450f718920d7deebc973e15dc34bd4d201c73e99d93220267c3e3131cbba6; and the separate center-free S1 and U1 controls [internal-source-reference] and [internal-source-reference]. No required attached source was missing or unreadable.

I did not find an exact own-centred strict110/weak000 C48 construction. The exact progress is instead: a complete mass-coupled normal form for every own-centred ordinary bipyramid; closed rational coordinates for its full polar perspective prism; a coupled G/G^{-1} reduction of physical U1 plus stable S1; an explicit actual-centroid apex exclusion chamber; and a cold exact reconstruction of the inherited 309 marked-shadow-shape enumeration with deterministic labelled representatives. The latter repairs the prior enumeration source-capsule durability debt.

The supplied center-free controls remain only proof-boundary evidence. In particular ordinary bipyramid incidence can realize exact strict110 away from the filled centroid, so no S>=2, U>=2, or S+U>=3 center-free obstruction is used below.

## 1. Exact own-centred normal form

Translate the uniform filled centroid to 0. Apply an invertible linear raw-coordinate change sending the base-plane direction space to the xy plane and the apex-line direction to the z axis. Euclidean geometry is retained by an SPD Gram matrix G=A^T A, where physical coordinates are Ax.

Write the base plane as z=z0, its planar area centroid as c, the vertical apex-line planar position as a, and the positive apex distances from the base plane as h_+,h_->0:

C_B=(c,z0),  T=(a,z0+h_+),  D=(a,z0-h_-).

The two pyramid volumes are proportional to h_+,h_-, and their centroids are (3C_B+T)/4 and (3C_B+D)/4. Hence the filled-centroid equation is

0 = 3C_B/4 + (h_+T+h_-D)/(4(h_++h_-)).

Its planar and vertical parts give exactly

a=-3c,  z0=(h_- - h_+)/4.

Let S=conv(s_0,...,s_7) be the base octagon translated so its planar area centroid is exactly 0, and put

z_T=(3h_+ + h_-)/4,  z_D=-(h_+ + 3h_-)/4.

Then every own-centred ordinary octagonal bipyramid is, after the stated linear gauge,

b_i=(c+s_i,(h_- - h_+)/4),
T=(-3c,z_T),
D=(-3c,z_D).

Conversely these formulas have filled centroid exactly 0 whenever area-centroid(S)=0. The apex line meets the base plane at (-3c,z0), so its displacement from the base area centroid is -4c. Therefore the ordinary-bipyramid crossing condition becomes exactly

-4c in int(S).

This is the useful mass coupling: crossing and base centroid are not independent variables. In the journal crossing-origin/sheared gauge, if the base area centroid is c_B, then after translating to the actual centroid c=c_B/4 and the crossing displacement is -c_B=-4c.

For CCW rational S one can enforce mass and ordinary incidence polynomially. With Delta_i=det(s_i,s_{i+1}), area-centroid zero is

sum_i (s_i+s_{i+1}) Delta_i = 0,

and -4c in int(S) is the eight strict inequalities

det(s_{i+1}-s_i,-4c-s_i)>0.

Thus an actual-centroid search no longer needs numerical recentering: mass closure is built identically into the variables.

## 2. Closed polar perspective-prism formula

For each base edge normalize the planar support covector u_i by

u_i·s_i=u_i·s_{i+1}=1,  u_i·s<=1 on S.

For rational vertices,

u_i=(s_{i+1,y}-s_{i,y}, s_{i,x}-s_{i+1,x})/det(s_i,s_{i+1}).

Set d_i=u_i·c. The crossing condition gives 1+4d_i>0 for every i.

Let Q=K^circ about the actual centroid. The polar vertex corresponding to the top triangular facet over edge i is

q_i^+=(lambda_i^+ u_i,z_i^+),
lambda_i^+=4h_+/(3h_+ + h_- + 4h_-d_i),
z_i^+=4(1+4d_i)/(3h_+ + h_- + 4h_-d_i).

The bottom counterpart is

q_i^-=(lambda_i^- u_i,z_i^-),
lambda_i^-=4h_-/(h_+ + 3h_- + 4h_+d_i),
z_i^-=-4(1+4d_i)/(h_+ + 3h_- + 4h_+d_i).

The denominators are strictly positive because they are 3h_+ + h_-(1+4d_i) and h_+(1+4d_i)+3h_-.

These formulas follow by solving q·T=q·b_i=q·b_{i+1}=1 and the bottom analogue. They enforce bipyramid coplanarity in the dual rather than treating the 16 prism vertices as free. If z0!=0, every lateral edge q_i^+q_i^- passes through (0,0,1/z0), the dual of the base plane; for z0=0 the eight lateral edges are parallel.

For physical body AK, a raw vertex x is strict U exactly when

x^T G(y-x)<0

for every true neighbor y. Its physical polar is A^{-T}Q, so a raw polar vertex q is strict U exactly when

q^T G^{-1}(q'-q)<0

for every prism neighbor q'. Polarity exchanges stable physical facets with unstable polar vertices. Thus the coupled physical S=1,U=1 problem is exactly

- K has one strict-U vertex under G;
- the explicit Q above has one strict-U vertex under G^{-1}.

For fixed rational geometry the primal signs are linear in the six symmetric entries of G. Since det(G)>0, each dual sign may be multiplied by det(G) and written using adj(G), hence as a homogeneous quadratic sign in G. Positive scaling of G is irrelevant, leaving a five-dimensional projective SPD metric problem.

This is a search reduction, not an acceptance shortcut. A promoted endpoint still needs the complete weak census and explicit mixed-edge cone audit. Morse may recover H=0 in a fully generic weak-free S=U=1 chamber, but it should not replace the required exact H audit.

## 3. Apex gates in the own-centred normal form

Write

G=[[M,r],[r^T,gamma]],

with M symmetric 2x2, r in R^2, gamma>0. Define

y_T=-3Mc+z_T r,  v_T=-3r·c+gamma z_T,
y_D=-3Mc+z_D r,  v_D=-3r·c+gamma z_D.

For b=(c+s,z0), exact expansion gives

T^T G(b-T)=y_T·s+4y_T·c-h_+v_T,
D^T G(b-D)=y_D·s+4y_D·c+h_-v_D.

Equivalently, for the crossing-centred planar polygon R=S+4c,

T strict U iff h_R(y_T)<h_+v_T,
D strict U iff h_R(y_D)<-h_-v_D.

Equality is exactly an apex weak event. This is the supplied support-function theorem rewritten in the mass-closed shear-plus-SPD gauge.

A nontrivial own-centroid subfamily closes immediately. If the apex line crosses the base area centroid, c=0, so

T strict U iff h_S(r)<h_+gamma,
D strict U iff h_S(-r)<h_-gamma.

Hence the entire open chamber

h_S(r)<h_+gamma  and  h_S(-r)<h_-gamma

has both apices strict U and cannot be own110. Equality is weak and also inadmissible for weak000. The orthogonal-axis case r=0 is a strict interior subcase. This is an actual-centroid statement, not a center-free combinatorial obstruction.

For any weak-free U1 system, root identity fixes the gate signs: if T is the root, the top gate is negative and the bottom gate positive; if D is the root, conversely; if the root is a base vertex, both apex gates are positive.

## 4. Durable C48 seed in the new gauge

For the supplied strict222 seed, h_+=50, h_-=1250, crossing q=(-10546,-85308), and

C_B=(102613703651380/29718409009,-100925661844464/29718409009).

Take S_i=b_i-C_B and

c=(C_B-q)/4
 =(208012022530147/59436818018,608573093473827/29718409009).

Then z0=300, z_T=350, z_D=-950. The original apex direction per unit z is

t=(-121/10,-13/50).

Raw-to-physical centred coordinates are

A=[[1,0,-121/10],[0,1,-13/50],[0,0,1]],

hence

G=A^T A=[[1,0,-121/10],[0,1,-13/50],[-121/10,-13/50,184347/1250]].

The exact verifier in the recovery capsule reconstructs all ten vertices and proves by Fraction arithmetic that K has strict-U roots [2,3] under G, while the explicit Q has strict-U roots [1,10] under G^{-1}. The latter correspond exactly to supplied stable facets (8,1,2) and (9,2,3). This cross-checks the supplied own222 seed inside the coupled formulation.

## 5. Exact shadow-tree durability repair

I reconstructed and cold-ran a standard-library exact enumerator for the inherited shadow-depth reduction. No floating point is used. For a_k=cos(pi/(k+1))^(k+1), k=1..9, it rationally brackets the largest root cos(pi/(k+1)) of Chebyshev U_k, certifies each bracket with exact Sturm root counts, raises the interval exactly, and certifies every depth triple before the graph enumeration.

The replay gives exactly

TREES 150528
APEX_SURVIVOR_TREES 45192
APEX_SURVIVOR_PAIRS 101248
APEX_MARKED_SHAPES 159
BASE_SURVIVOR_TREES 89998
BASE_SURVIVOR_PAIRS 314104
BASE_MARKED_SHAPES 309
UNION_MARKED_SHAPES 309.

It also emits deterministic continuation artifacts:

C48_MARKED_SHAPES.txt — 9027 bytes, SHA-256 4956367e17bf655b7db2b780668bd1abfeaa13dc4e2c7c1ac35fba822895e2fb.

C48_MARKED_SHAPE_REPS.json — 49716 bytes, SHA-256 f5dac48eb2b3b9a4b2d9d516fe3f97ecfa908fb3db8aeaa5a81231ac0142424e.

The JSON contains all 309 canonical marked-tree codes and the first deterministic labelled apex-root and base-root representative whenever present: root, marked opposite face, and the nine spanning-tree edge indices. Thus the abstract 309-shape result is now directly usable for exact semialgebraic continuation.

Recovered source identities:

ENUM_C48_SHADOW_TREES_EXACT.py — 6652 bytes, SHA-256 64e0822a5b7e61a406e947d9ecd26ea649c0ccdb28ef1fc5180140befc18f4b9.

VERIFY_C48_OWNCENTRED_NORMAL_FORM.py — 6696 bytes, SHA-256 8fb4113d173beed6149b7bb0a02a3c0dbd2ca8f4ea25f66d97f86d3dffc628cf.

The complete compressed source recovery is below, so no sandbox file is required.

## 6. Stronger finite reduction

Every weak-free own-centred strict110 C48 realization must now simultaneously satisfy:

1. Its physical positive-shadow tree and a centroid-witnessing opposite face realize one of the 309 exact labelled representatives. Orient the nine representative tree edges toward the root; positive child-to-parent dots plus negative root exits are already a sufficient U1 sign skeleton because each positive edge strictly increases squared G-radius.
2. Geometry has the exact mass-closed form b_i=(c+s_i,z0), T=(-3c,z_T), D=(-3c,z_D), with area-centroid(S)=0 and -4c in int(S).
3. Root identity satisfies the corresponding exact apex-gate signs.
4. The 16 dual vertices are the explicit q_i^+,q_i^- above, not independent variables, and exactly one is strict U under G^{-1}; this is physical S1.
5. G is SPD, projectively normalized. For fixed geometry, primal constraints are linear in G and dual constraints quadratic through adj(G).
6. Any surviving rational open cell must still pass the complete exact mixed-edge and weak audit.

This does not exclude C48, because I did not solve all 309 resulting semialgebraic systems. It is nevertheless a materially stronger durable reduction than the inherited marked-tree count alone: the continuous systems now include actual uniform-centroid coupling, bipyramid coplanarity, apex support gates, and the dual S1 condition.

## 7. Construction search and evidence level

I also ran finite continuous searches directly in the complete mass-closed normal form, varying the convex octagon, c, h_+,h_-, and all five projective SPD metric degrees. No robust U1/U1 sign cell was found. Runs tended toward sign-cell walls with extra adjacent primal or dual roots. This is finite numerical evidence only and is not an exclusion. No numerical checkpoint is promoted as a durable nonwinner.

The useful correction from that search was recognizing that c=0 is an over-restricted gauge; the exact normal form above restores the missing mass-displacement degree of freedom. No exact C48 strict110 candidate was produced, so there is no new full H/weak acceptance capsule.

## 8. Best continuation

Do not repeat the 3003 inherited-apex coarsening. Drive the next search from C48_MARKED_SHAPE_REPS.json.

A useful first ordering is the 159 apex-root representatives, because the exact off-centroid strict110 control proves that an apex-root/bottom-stable suspension pattern is topologically realizable; this is only a heuristic priority, not evidence of own-centroid feasibility.

For each representative, impose the nine positive physical tree arrows and negative root exits; exact area-centroid and crossing constraints; the root-specific apex gate signs; construct Q from the closed formulas; branch on a candidate polar root and one positive escape for every other polar vertex; normalize G and use adj(G) rather than numerical inversion. If an open rational cell appears, freeze a rational interior point and run the complete maximal-hull, filled-mass, S/U/H, additional-weak, primitive-zero, and same-centre-polar audit.

For a proof route, seek small exact infeasibility certificates combining one apex gate, a subset of physical shadow-tree arrows, and a few dual-root inequalities. Such certificates would genuinely use the centroid/mass condition and would not conflict with the supplied center-free strict110 countercontrol.

## Recovery capsule

CPython 3.13.5 standard library only. The following base85/lzma payload reconstructs both exact source units. After decoding, run

python -B -S VERIFY_C48_OWNCENTRED_NORMAL_FORM.py
python -B -S ENUM_C48_SHADOW_TREES_EXACT.py

Expected source hashes and terminal markers are listed above. The enumerator must end in C48_SHADOW_TREE_EXACT_REPLAY_PASS; the verifier must print C48_OWNCENTRED_NORMAL_FORM_POLAR_APEX_GATES_PASS and C48_DURABLE_SEED_NORMAL_FORM_U2_DUALU2_PASS.

```python
import base64,lzma,json,pathlib,hashlib
B85=(
'{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;5F0~=3M|ih=io#(fm^A5G|0CZ6{WyS|(N}zzAyYqToO>Us!EgpiA>N3>t`x1fk6C41`R;BBRSJOR((M_Au56qBS;-B}KLTx!_?P#uBXDLl7gW42v8i4^)d-^ZmDO*;k|l@=aHK*wO?F#r3qVuObQv$PI_!<J<SQHn0N{lruuZw3_=yT)@r!n*KSztV1bdOG)7PhHr=97NQ+Pnj4`!xnt2#u1yhM4vdYv=vVky(PQML>)F|!Zogrj*I!igMKsPmg$X#14F-fbZNg{b`BnKkKKpDr*ww*tt6{SY{b|f!GNHpB2zg0ABZ2l!?1ZbQ5>go*$`YWd+@_OYX?^_vIKpAfdaZm?lHxi#YZMV=2=G&REOx6v4@aw1jju{M*TpGH6c-HkP<E+O@4s6Eur&**y|U=Q?;AG<=;KpyknHc65RJ#`zyOR);LM*zW^)EdnuU|D+F&k~p?X1{K`ATW*Zc}q%zcgiaj+irXq*Kv9-GP&$_?eZ(8F15H}{?uY;59v1Hb)Ee|$h(TY``cG;CSs!oaUX5)?{u9*Z}wlV6iSr1x2`S0gGy=<v!{)U-sI$Uwi5-p@}AFUfZozYTd1$$K%?2_W%%NtXWLk$!3l1fpV&o9jSj&i6UXzW6zl#|{X3hv)5_tJX0;<vQ57iO*>{<a&;3fN|-ze;W$j_%ni*!iTVC8!`F+k*)jQc%S=HP<TE?O_N@8YApIEz%>}-H0bb`_mJSxg{%ZEEV?PDOP5zv?=n#_O2<(?RgI%B8^iy;!CLgHIy<@<g2PRFaL#blMQ4D{FHCF^8^tV@9ey!A)t3s>yvZVZ+Caaq3BR$W2t5<TsuDR=<bJE*w$QJys(c^C6UK?N=A$`!@eGQ>USy;bZ*<+(S!HXii_W|&G^ZA)jar66>~}EAppGZiEZvA9YQ+yd!<y7QTSo(F1ae^lj2?1n^jhdm!;hXMY!S#|c~?JG9btgsf4uL&dJb?YVwa_#M(p9o'
'bkpL8jGhVsG+fU-lOEXXPc`Zs+0Uk$$-^?R=M3}K`s>Z^jv&k+{n1eo+9xoi;HUsI?Lr<|F5kH1UeGTiI&E|)C1X5(Q80Q)8xRNVRz~yc=dh?;+mqyP&hSJgt79sHMj|5jT4w=Q#EMQKqDlN1pE6<mfQ|dVA1{Er?)I=Uv;@106Wdf;Uu#R(7JfPnqxL;scMj5XP!c1Z%uY7IN|!-S)oU;U32|yxGlR0Z4RIUdvx$I}UezX3oLW#tJ-ullFG6D4!z{avqfIw4L(2z96GM<87VW|Qo_NDwfv;P=aVfC}*(8^%osrh=6j18d#m2Vvrq3!gnq;)`cBY^0oXj?-Eq~v<l%rmalygBZWmX@fLd5lRd$w1sT{REw7TtV1{M^EIl9o)!eEgDm3JQp(!@9#l^|Z@E($wQy9EHUwLf71eDiI4YH+xcb5my5tV{8v;(`K?vYj1yMrr35=R+%*pMBBm&$5B@Su6YcPh)gbmC$$cDAxFuYTNC$_w(GH6N_8V3W4*__O`>$D@l5RP!3TfRb!5eYI5OOzjfU5_*Z)=-0<kdrdxWNm?Skq|33HO^7%_I&z;^_C6_ugkF!3QjVP*DSS$UGK?EO2U7LJP4I%ufvo_8CLAWgTX#aLbNooHbd{F3ffqER@MN41@i-ZWn3GMyT7Z^{*hjohZd1VP6E_vn3yk13TRKv~RtRsORsOW7Z>{+@^b%W7gvwEiaTwLX?W{0Z_=18a?)-kRS)817PV?9@2(xsyF%!(`bb@oty+9jJCBj2}=sRUoI_u#=rvVU3If8H?ZVV6OS${%w-maww*U1Qc*~RMrwlxp&G~ozI4WIIj`+G~oeoidh7dK;G3Jf2SQ*K=~y+Nq3Z1mpsUC;7oW~c;VgRKpy|uY>xrtuw9Ue9brj=7uc$UQ;isI%-d*qj0mk+zu)uFS!S%DGmuh8$>#F+rV(|$QjDN0uX6p1WDeh`e<zmZh{U#*moZ*<hF<OL9O2LMQ`N4IR%saBG~sio(=M8-GW1rx'
'<3sseF1lv5YCvnA)%(V6cUZsKcf7)pmgIzs?(r{Xn}T!p_68Jt$5n~sx*S#OdqjW6J9o+zFmv%H24}M!GAewvXJd8#8ykaQn!`z`W;tz>4>Z9wehsHM``6*$u#(S(i-4yXdC1z?J~X6>Rqp$Io^VR2N0y6qgujMT(WgGFk%H(n5FQ}B2PT}ORI=alYNh{N5X^uNi$7?Mi0?&g?st@#)po0Ppy)b?aP~SF0C(e^|5)CMG>ycfuXxLt4mS)3A1AulMRbD+CZtkn{3Ctwx*qBl6s9a|K(4irSczb@^_a*=oU}4{X@EK<%z|oswhCds!D%#@C1}BMwrTq4g%BfSe>#FzQWc@05%G>Kms1J{pcj@vTkN?h>uetLikXcKsZXv0_d{o$i4+l8wl?pc<7l%_-ST|@FYj?fj(4;^J%`5dv~a_8KFV3q3lEm!w*BMmzTMxNFOe;Kn0f9Q*3WguK42QMt1(yB3r4&k`<|SqYXsP~c91mzLdbyFJtC*3g5>?ex|976Vq7(&d9FF@3ujF};Po_0^*p&NQe>sHCwf@Ztw*t~0f+)*b#1jCq541pwvd}WZD3}q1p7#L)$EmWyubbvJO>t^_NaU&AEdzZB6xt<r569pCEmgX2p14}6?ihtp+a6N5HoYD{<qc^HTG|?L6nO^IKD61&Kt+j`vOir0V@>P4G}MTZ<CM)kga!WEA3*+ONP6y-Xv&9tJPXdlc#08^ZzwVM=Yp{4P3q)7OXegHu=<&IQU-b7eIEKX>L$Vm}-IlFX5cO!#DhH?BOneTe;^_E%2g*U5k=m+^yv78Ah7)XS2&^U8=N2=4Zy_*k4fC-W(7UN6S!xbrsfdc_McstxsWPab4;vKmZ<H$LPcc9v1&jpYU+EG<>@SlCJaTr=ay_e({K%C`*16%F_D#vW|VCi9X#tm8MpojqJ9cXkf8YS`rf@LU_fvx{)C}vPwLI46n>jqij|T1VoYLOWvpv@`{%!m$U&`bjquHLx$~8dAZ{*tTT6Pm2f2u'
'jhD=IUQURX3rq2-rVT7ASR7QrM`O%jTD!GmsTWXz?@!lrYH2r5F43C&4<>~m6dF6+1kPmT@H$jxA5uSP&j*+!r7pp>I^7YLe@g$E7yPQ6N_rWfbz8tr)v23lX8(@UqChQOkrLdgmY!nML25~(9Rn+4oBQW+9I~nddpq=1JQwFvM_|I6BxL<qxIv;HrB1ZNJfH=DWuvu7E9gnBVqURFS$BC1KQ@W8Q-l6BX_V)B?A$xRq-BYGOrn`tCpY}G<}pZ@7GeT3caYZM^P=$4>R>ow-wEZlsHlbEELvo+IE;lUZ$ntJCr>w%NMIYYV|aS}we$cA09v1CB)p{xt%?umI7a0@W0-%GmTasU2#ZM4@Nzrc5wNOgL<ym4QVyhh;{G{=@>?6kq{4ts@^HNV3(N1LObTIvq;Nh~mk2-YSwZbUDcev$ed(W>R-hT{xASV{9MgNKIOkaFfS?Yk_zG8;ij}XJYKnA_LBZXTGG_=L;K3ouf0>Z#p#}Y2)lU;t`n0U`>EyvQbhF$reL73&2b<J%Y=tWTV&WP(bL;#L*|H(CqP;qB+hZrpoVERQ`4BeuAb3zkWtN^V9&&L!Zh&fybZQ08acilj2wyI%>!U;UP{p!G$@`RTy_|rcmCn&KCIv#%b*<k8acQAyV<-tc&9KM1p^J1zRkK(gxSoLuqD>qfKg{1q5W=SgsqC_24d>(9G#DDeaPncot9-L@x-csybyr49>)p!?7auk_=h`BTCSH>7XM`3jwgGt?DZ7AA2OvXZjJ-<Q?(@(7o_LGVq*_yM*SsOhaXMh6FW~6=pEywM*C@<<+6d=!CJ`)03!r09J~hgI-!KI^8-1JNBmYaE4v!nIx37H1t#o|BS=L{qjDToK=!xCTYsZgmoTIy1d?`siNsVXd@6!r-zi}gZ);zI8OGNn~1W74QBgCFrqs*!d2h3$m?45qP$tE?*-2JM;MiDlvbnNvfdi5xRBq~rq{NAVhiPSmeY-*GnTe0;B{X8GQpaZTWqB35UY>b=$'
'n5hIMG0t;ip!v#9U=X()=7AeMoODn~yGkN*ahc2ic7WB>aCjSbMg-bWNS0G8Jfui>r*kK9zFj*DDAAq-kZVI~J^_9lwmMG;e;{&p152T3VulaaBlTKp2cvJoR=r9-tIbA=FXr4zTknLM&9qk0$7HMNJ{x;{lCD$NKYVsl9VpX~98R?j<UO0jl{;b7PLP7wkV~{5t`q-eY&E{mnBu-)8({*hiQw7~g0Djj$5_aPE5KnS1#)ygcuQJ^XLKO~(@XC!s=uaC?CrPK_cjPLN%rwqlP_%gZM4T5gp+^X2nz%_EhoW!gUbnj_Eu6!ymVijv6st+x>jR|8}QsL+`X(WO_ll9_^)d_@e)g%a7Q_2l<-TCKu!DC&#lPiu)zj8>FKH?Tfq!j$BO87Q_<IYCs<fH?B3G59ZfE_*!#<(nJH;J_E5)F^e-VMFv&m;J)ysF0h<XIIwI3|Y>Q%odo*0SuAdaqeR)wfFs2$&ODU-5<;qoWRFq#b9H-5Wn?GR>uP`4Lh`igct&qHz>;kdD>zmiVGOgFF<h)-Rlo&&8H?e;n|1IDaT7D$6x&5>Mq_~i#IWtfFN@9mz5T)VSI2g+Ib~_8R7T@<(1Y>@8(Ug~9J+=_VU=Jn<OU8awUR7~sN6~Zm+rb^1J%A$_a>U7iMcZc5Xq>Rq-RYGh1|{SZ&R(g*!spbk!^p{Op@J4TS<rL?R7T$kbQ0{_gSm~Jg%Zm$*NOtZmi_(V_NjSavV{WPPlOfY-&qZ?OEh1&dlCKPE~Spcoulc(Z*E4uF38Gd@f*2+pltCf+LaD3?s)`?qbRty$|{e$>ygNYqO5M}+7OdpJuxCb?dP$EtUm6n;3GSiQ2%AAo>Kp}f5Yu^w7s<_Do~8Iyix>mLf3w*s{wn{Ty2~KX;7t6-~<=|L<Ba8@q;Lvjl97_gLFVqEHET@T91G<<3kM+rF(zt+CcZ;&oXx5hMY%%?dD?)PwAzF;5j`Hd8KUJQo^Uau8>#OAuh=v1njUQ+YF;4DdFrl_Ka6Q'
'K9>+@unf+y(=_BTS5*^0k6OfpcCNt=WR3)|ee3TL!Y>@&=tpACyf%`9|C#~Vw8$L6eazI;VjzO1sku!izgIpe{Gw)%;<mUAtFF<{o8JdlS<}xG`R2O~SgEh|5Fi+y82O$gU?>t(iwoWJI9~a5P+B9{VG3<u6=HnX5Llr8E*WDDNUG=nwL1e%e-#c+gx#XE=S8x&Y9j|UA1Zk6I9>|Er?2|`={k70RaCZsP#b{?#bi@3!F))63{xdgu&baBd)fGYz&NWQ4wW7^f;jjE?xg2`h*Eghg<d4iA#q^Sv7!hAz!E;O#ocaTy)#~Cq7cH)B6`7T?|nc3vL9fQgM!HiQv<+{!^5<l_xgKBH`_NT6`QH<aMfkYqrq3jn+UoGY$$2&6pY*u>2T$DyX9c0&zA;LDg{0>C<%!3we$hGqKZI8xze~ruzl6|OLoP(iQ_pB4$D<;ndENw#v#Ce#P?SRU~&KU%w8-ozc8#-LtwF8=56BgY~^|UjUE$KpPb`YHg#7GHitbxE`5%@@D*UVUKQV$ctEXdeTS}!!BnGT9dCYU2NY>rLf}n6M|61-7&YfSK)k0Ygl+}(cpE8&_?<V_&r!C!teE*VSI8oK46M77>B2f{zz`KKyk0243q*gJ?wD`~^!0>oQA^4~CCagHMajSjm@3Zd;F>@BIk$BB8XoZ}5p^daprvweZ45xp;kc_P2>4nBU*?dSr9YUc*`SGbj%wLOtO_0{fDD4Z`%o^E&C5nFhVbUfm@cZO4-9^Qly76eWK9(?%r2G{70>9RF#<K-VWTT%9!EutfJWvJ2m@hGbI_|}ok~_tzkd2U?#?62zVrooa7LZb=W)z~7frZ=YcrTzhzf3Y8$ev59}#Jm;aw8o(hqTt;M^Fr2vF`g1T(J{JDmzGcnDo`MBWsX?|S~?x9?4ym49)Jsn0rah6g2k6Nq-p=fRzv^|swC06X++zIxK<#Oja%8M=-t9o`ksZWfvz|4xo*-LL|$%PBRnI)k@n?v{Ui1}Vn&xx@7H'
'5wavEyXO}%ZvhHJgn)skyPos7S#C+U2c_|+bRxk-G}E1=>j=h=AtmQaa7RJOwVA_DGG2BICCg}Ei-spO7w128;w<(5yv!zDge1WNiyP%SXf|BFucXd>j8h}==3o-1-2}4`4$|QubNnZ|-%FF{=S!Ng*Yqzi-sWIh9eU8`@tu>5+F^u08OD*?TYmG1owEkRxm!ZU)SF<@%bfpQliEe5Y?Yc};(0Il1|Tu`f}hP4wV;b4Q;(6her64r^?g=t+poncyk+n5|FYyW5p5m7yu9?|#}{idhLy$tT9{C4b%%;H2hHqL^>OaiA3+K+3gf-392S+<$BWf)y6$EMR2{XI9b<~SA4XsAFl}E>BoamH0RD5QE+UMUZGes%C=dCdV<*kKelXRxtV~>0uyN2LM1}bzHlMQJE_K;|6lUnaie$!@ssBIa!%<5&$BqhAI)oAqiHJ|qcuMMop)vW>biUX;<JxAY%J&-u2g2{2b$W9px8?3=etN_;3r7{RS*C6hc<<VAFqM>Eu&e=Y)`pC9iYhadNyxIu+pi8xVo`cGl?RU;;#}SaW?0~q4ub)yJ>FYDXcH%l5(*76SX0|IEVX;HTpU7*R!t;jyTb_A&xVWL&9)6R2}hiWtUy*KP6jBe!vqK!V6U^VOmh7DZe=L?J0ZJ&!Fu^MFhkB)p~_@j*@h_f_BHg50fws`lGlREB!IH^V$0Z^ARCWqQcAYOc>3q@0!expdgi7fiNb)xUH||9*UuO^8rKhn00Dw3)oTC%!8=q=vBYQl0ssI200dcD'
)
raw=lzma.decompress(base64.b85decode(B85.encode()))
d=json.loads(raw)
expected={'ENUM_C48_SHADOW_TREES_EXACT.py':(6652,'64e0822a5b7e61a406e947d9ecd26ea649c0ccdb28ef1fc5180140befc18f4b9'),'VERIFY_C48_OWNCENTRED_NORMAL_FORM.py':(6696,'8fb4113d173beed6149b7bb0a02a3c0dbd2ca8f4ea25f66d97f86d3dffc628cf')}
for n,s in d.items():
    b=s.encode()
    assert (len(b),hashlib.sha256(b).hexdigest())==expected[n]
    pathlib.Path(n).write_bytes(b)
print('C48_CLEAR_WILLOW56_SOURCE_RECOVERY_PASS')
```

Evidence classification: the normal form, crossing constraint, polar formulas, G/G^{-1} coupling, apex chamber, durable-seed normalization, and exact replay are exact. The optimizer failures are finite numerical evidence only. Existence or nonexistence of an own-centred strict110/additionalweak000 ordinary octagonal bipyramid remains open.
