
### Recovery capsule part 2/2 — COORD_C80_PYRAMID_GATES_20260916 — numerical methods and complete optimizer checkpoints

Ordering: this NUMERICAL_COMPACT bundle follows the EXACT bundle in part1. Together the two parts are self-contained; the numerical checkpoint replay requires the C80_POINTS.json and rebuilt exact C80/A.json from part1. The research identity does NOT name a new own110 body. Canonical accepted benchmark remains C622. Numerical states below are finite negative/proposal evidence, not exact constructions or global exclusions.

**Executed pyramid experiment.** The complete43-variable chart moves every20 base(x,z) pair, the apex horizontal pair and log height; the filled centroid is recomputed as three quarters of the planar area centroid plus one quarter of the apex. Convex-base constraints use all nonedge inequalities. The normalized primal/polar escape hinge target is tau=1e-4, with analytic Torch derivatives and SLSQP constraints; finite-difference derivative comparison was within3.4528e-10. The invocation requested12 starts with seed801622 and maxiter400, but ONLY starts0..10 completed before the container execution limit. There is no12-start terminal receipt. Every completed43-variable state and its scalar mechanical/convexity metrics are preserved in PYRAMID_OBSERVATIONS.json. The best valid numerical rank was S3/U1, objective6.340882610449458e-8, height0.0025318015095915016 versus original0.0478675, minimum convexity7.317368878126027e-5, iteration-limit status9. The small objective was obtained by flattening, not by achieving two-equilibrium mechanics. Starts1 and9 had negative convexity and are invalid bodies. The executed source comment about the orientation of the cross product is reversed; the simultaneous sign change of normal and offset leaves their quotient unchanged. Preserve this executable source unchanged and this explicit comment erratum.

**Executed single-polar-chain experiment.** The entire method constructs a directional chain from old polar face0 to gain times baseface13, distributes log radial slack after paying all adjacent-angle costs, and solves the actual filled polar-intersection centre by a three-dimensional chart fixed point. Parameters n=16,24,40; bow=-1,0,1; gain=1,2,4; maxfev100; finite inverse vertices deduplicated at11 decimal places. All27 cases completed. The18 bow<=0 cases closed their numerical moment residual to about5e-12..8.5e-12 but had S3/U2. The9 positive-bow cases were chart-boundary, residual0.02995..0.04437, S2/U3, and not mass closed. Positive chain slack protects only its own successive escapes, not all original nonroot facets after the centroid changes. Observed terminal marker was C80_SINGLE_POLAR_CHAIN_SEARCH_FINISHED27 with1138 evaluations. The original BEST.json ranks S+U and E before closure, so its E30 proposal is NOT a best admissible body and is not promoted. Full chart triples, parameters and observed scalar results for all27 cases are literal in dual27/SEARCH.json.

**Compact recovery boundary.** All optimizer variables and chart parameters are retained without abbreviation. Redundant P/Q and escape arrays from the original verbose receipts are deterministically recomputable from these checkpoints and complete code; they are not separately stored in this compact bundle. NUMERICAL_RECEIPT.json also identifies the original verbose SEARCH/BEST/log bytes for provenance; those hashes must not be mistaken for missing required recovery inputs. Checkpoint replay does not rerun either optimizer and does not convert floating observations into exact geometry.

Observed dependency stack: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, Torch float64/one thread; OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. All nondefault search parameters are in the complete commands below and source. Floating optimizer transcripts need not be byte-identical on another stack. Exact part1 uses the standard library only.

**Recovery integrity.** Remove whitespace from the following block and save C80_NUMERICAL.b85. It has19245characters, SHA256 **7dfefaa04166f1a073f11e6854b42111a94adfeb4371f9a1c56e073874319bab**. The zlib-decoded canonical JSON filename-to-complete-UTF8-text dictionary has41498bytes, SHA256 **0c98e0d793ff5c4b916ee37399bda99678c9222bf6acc59ee0b55805ff1f57e7**. Use the complete RECOVER_C80.py decoder from part1; its numerical specification already binds this bundle. Six complete files:
- NUMERICAL_RECEIPT.json4292bytes/SHA1b72961abe936e49adeb19652a3a05e61faaf67f8d9950f9590641a59283fa19.
- PYRAMID_OBSERVATIONS.json13299bytes/SHAacd5f681bdde0e9ee7775e66f1bde9ee152e0a2bea88afe036507cbfe1c03540.
- REPLAY_NUMERICAL_CHECKPOINTS.py1834bytes/SHAf7fdf2828b1b10425fb5322913e74f6c43c75bb065c3aaebe7926d3daa2d9416.
- c80_dual_chain.py5178bytes/SHA3c7618ea7321a290de7fc86a489fa4b8c17d7c9546340198c72b7ec99434eec4.
- dual27/SEARCH.json9414bytes/SHAe1d2c25ecf3ea3bca7496e1710d2a2acc8ecaa04cc91fbe309cbc1a5bbee0085.
- pyramid_search.py5416bytes/SHA41bb2cb1a3168f464cb616ef2facf5bc617c47219867c8eeaab2f815ef479538.

Commands (output directories should be fresh):
```sh
python -B -S RECOVER_C80.py numerical C80_NUMERICAL.b85 C80_NUMERICAL_SOURCE
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python C80_NUMERICAL_SOURCE/REPLAY_NUMERICAL_CHECKPOINTS.py --points C80_EXACT_SOURCE/C80_POINTS.json --audit C80_EXACT_CHECK/C80/A.json --out C80_NUMERICAL_CHECK
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python C80_NUMERICAL_SOURCE/pyramid_search.py --points C80_EXACT_SOURCE/C80_POINTS.json --out NEW_PYRAMID_DIR --starts 12 --maxiter 400 --seed 801622 --tau 0.0001
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python C80_NUMERICAL_SOURCE/c80_dual_chain.py --audit C80_EXACT_CHECK/C80/A.json --out NEW_DUAL_DIR --n 16 24 40 --bow -1 0 1 --gain 1 2 4 --maxfev 100
```
The first two commands were actually executed after source-only decoding, as was part1's independent exact replay. Numerical replay marker: **NUMERICAL_CHECKPOINTS_REPLAY_11_AND_27_PASS_NOT_EXACT_CONSTRUCTIONS**. On the observed stack CHECKPOINTS.json is2887bytes/SHA **b2cdec7f7ad89826ed101e75b2612cde999f1dee9f0269b1514c8ef5940b4c93**. Its complete verifier compares regenerated mechanical classes and scalar margins with explicitly stated floating tolerances. This is recovery evidence for38 finite numerical states, not38 exact newly constructed solids. The last two commands reproduce the research invocations; do not infer that the originally requested twelfth pyramid start completed.

```text
c-qZ<Yj@j5vh82t&G{hGhG_H)Xh_3Z<A-wMbu)g+&hb5p78gi@5@U)~_^{>4%74FmS2rk<q9kYRa}sC8Ccy^KsIK0%tGcW3+jlSC{qyL}^QVu0?7lgAdi4C&
+x9Q>>EyeE?|%FFyFqnXO$ODZKdR<Ge|LZ*FaP<fi!-`!e|U5B_}MWI{`{T#`MU(aygGXE<j2RyxBNU=UR-{b@49W;PL5rEUYt)Sa?rF@eRSR*#g?kA@^&f*
7t>k)Jf5!7cKWb?x%~ON-|@?EG_E_>_i1;qEXUpcc{!T2<tjMb`@E1APUW80KQFb*!d?4$rhHZAMypa6>7dGoeV>)q7sJx_d|%~*yk9t*8JnuY_jBFLtA0^f
W2>rfLl1aMowvu+v(5Xd)Mn}C4a>Z&1}^XCsm*(Z>-U`M_jKR6To;4Pm8MtbDpR^FwdxJCGVND|HhFK*8z`LT)^GUe$<c8btj*in+~%8iwc6+*4yzvSkyk^f
ds_Q`S@li7?0b{j)Y~-AvR*kbm11YSu3S%L!`^UUHy-oR@zLWqPk-2P-@+=pdEZJ6bYHuwKQt8{tzYK0$SReqbf8OJ_WQo-mt|`E{Xz|Ul}U?!udhni>s3{n
`uMb$pJ(O8XwaQkC3N8Cs9Ke6J+A6Orae^}mHDB~Y`>SOtQzWJ*&n)IKT~<%<{IOf<>*3HmOVZ6%2kk2;fxQr4YyPJ=D0eQZ3);7GH6bgn{<drfbR7BnZ=h}
>pbVcnre`xI?c*q&z9v7T^pi>u55)HE4z8eTL%`px_RG1r}?1r!>TAuPvyf>`(B=E4^7s+LKj(?=LVYW`_5}`^UU~R&uA#2FKp`c)_rdsT9@YAx7NxHRDS^J
V=h=s2n}r=lm(`dF_>tjGg;;awouTpp3lAO>%8xZewtS0uo&Rhy!Qy`vKTGGe1H1#<(p^Sr<ldB{@<I&|9t+e`=5{B9vydes<X6ES@#;NUL4`4=RX}C3p$J@
m&--BTn<KyEs?ogZT5Sp@?Ot+4!0i;eU=q@VX}cS<q&h)SK6yQ^(j=tR)w;~pjTGf^c^NlsfuA9L>6v%IUP+F^DR*o#nvR~4|;|gSlAr5$y_?fD=5W4VU(zP
{ocU1+~j574P3uJ%(FfOWOUE<F&lev5=_VCEZ|zaUo~HJKb5n|XmTd^d3#<p`qM$xn3a<c^TzSRca3r~XjFqU9$!utjb1gJ&hTYCoiAtAL1U$6jajw8h37b-
v7GStYS1_`Y2$J>y`0X=al7$+(HPAeFJ8WF^vlU~GU}J(2D^|ns;jcUXjC6LlKm=aOlOVhr-=ec%h2@8xyVIx%Jiof7wDAqH-LZR24*+*_hld((1S;hL;v>o
r^`j-#nFFtpS{E2KYRWLhb9e`HMDKm6kmGNPmO)mNE-@Y&Tu7s&<%?(7v<Hk`q)ruFeKH-a=a`Tqv>ScomKtmY*4X3N*OBnv^TG2AFDxkQOzz!lX4vN5`8>=
{^CD>JnFuB`Qzg^-KRf1e*U5xrc3wx=P#Zg|8VrIq4NeW(`dS+VbY`lGi8e0=S2pca(V7EWn0pTTFBj6I@Fm@)fiF;$B)fBz4}r4H5d$|50O)5^TqU1did(i
%cn=j$KAKj|9SNC-P`Wt@82H1=_=KI3WNRQ(c7bE-Q%~9-@H9OY)qz&A)l;KKVsveoPDTfNn^e!XA7m!VnK~q&L$L15_N4fmpi>!UQ{y~e)Lf#Y>cs%%LYxD
RG%6k4Kg>PV#Uks82uaAjsXj^sv$7&^7)Im$J;tkgF{dQ>Giy!bQtRq9t$c#otRfpW1p%_^S4F0<cOrHsylNzt`?AWxBz-}k|rwAiAikYk}Sy+pA?BoPjA;6
Q)t?r+4Pf~kAWfOF*tM#c5*=D|BeI5f9nJN>EvT|)xD63oVS6MCiB2Y1&q^qwVygPI<H1&=fpDhSUaQe7%nYbfxpGv@i9Yxh;k_}49($}tPQT>z0N>CfXmL~
l7iiQ%-9EfUMxlLeot=ew7Ip@`&k?2L!nRF;`&*dS==Mr>bA13@RYvy0MAtA_w*VhD~FlENfwjHZS`91?zP+QwY#;~MY{-pa%WQfU&K4C`mEb9bC6h(<uJ+C
>l<=bVgzH4eH$DOra}ycQ!;exJ=W_zPX8S_uX<eAEVDkf+dWR(I&+2b&_bw&u@K>Qm%X{}vBjWd3Zy7iK8KOE*;bd$?k@iuLe5=kagRLP?lM$IsXX&}2HNJ0
bZ?`>c$9S+>(u8i^VS(KkbJwt_6ueF1zLeF>&$C?Q^rshs3vDpnrU@&_Nmmb>v3vzX2FRJpVR5B9=mTQVo*Ng6*{-w<GigjK?Rd3GewrE`_vffi=lEPY>@U=
hqJHlup;QjKdQ(v^>B-Pv&Y&4<h0hAcF<yVr-;#GKATBlU4bEXTg3S{RSKo>&yI-)NOo3RZ?r?38){r+8#<8_S>R!L=dMSr?y&#D4%@pBSsUnGo@)y{+JzLU
!fY&@^4b_UBH*ES;;|@Efeyn<$h|J|IA(R9i!ZbyUnFGso`qLC`dp-*3T#zc_!La)re2uMsb?|`M?Iy@_r<meNjK$8yFQ;TXZ@;6W&%H?Tg`Co<;99m&p~SU
C)3#l=+1ODLKC@lBeo|co>d>K87LbW5Zld#bx()Gc?DKdf^YYxi*vA|vl3)Oeq7)YXN_N%)5R!WWH~8^!>W%4?Z(kn)nBq{=vzY^3%StctP1RuB>lXcoS}K}
4rbM_%h3#6MkpAF<K=uguD;BtdIegjx<~IHKYbg*FSUez{*KJ{?a|8D>K^^{{Mpfqr#SKw6!S&*<(ntZ-{RD#KfXJD{*vFrb-G6{o(XkB@4idEt8e`B$??&f
pKz&{FOJuOOypMcYcjRz5w7(+((U!Dkm0_0`Cq{aoL-FP^QahL#Iq4cjq;{@0Rhg+&+|3;SD=ckqmV9X-DJL)EjbL0;cR-rhK-shuBdF|s`0U$jmq8_!_xcQ
coisY`>etlynKD2nqwTQHD<hG#TfDaxEx)`_>tO|I0N^XMPD+~*wvf_@s($KbTL^x8kCFj(Hze<?nd_fsCMAP#cHSY_V!!UIt+Uyj5g5ade+Ds<2R7!NJdi?
6pkGD2I=jN!ZFfkEyVdI53bu}r|ZzrgRj%=W8`O3@o`Q7vA}k~PhoNxU+rC%q;1ecaNDBrjM!yhKc{~pqrRx-^YScAv*-2Mjq&JWM8~J>pGUuEH}l4qtMH(B
Iz{-#O;Z4_P4?4vo@R<jO)8wDmx+Qra_!RsZ8HZulCzm{nNwK-dkB<<L1HtHS*=sRs!?DFHX-&qS7=XZz{CSn9ot!(7S<9laWzfp!a{&(8eO0pURjS;N;|-_
oTYprSIcx^$#^q^K5K^~)@8~;-hdR?6_c_XHn+GGj2_67HeU1c)-tvU)bYj`=`6&V<+wd8xyr!&IO?!a7?nKZvu9wmY?b5Qsm3$H)IuTg<PPk{Dwl!%!nzi`
KDrD6szP)a_YgVeR{4wpDP@hz`IHu{$U!1_*c?)^j_n|2SPz>*F^VEnne@bvLBV%{d4hyPJFjhqQ?+$4ikV2)fVOCb@1QrZV={got^pV}IT{RTE`5QFz{hYL
Cao|<u0umSD!dJwJC8d`JKRorhzk1Yt<R(xhTVBvI1iqm*)aGRa%wRC@st{mLHr<6=ouc+m{j_lSssLnz@mdQNjnU_$?+H5I8(sXhlkUcY)V@=GZr3@3K|Aw
!^O4Y(?uD8XJCwS2hNOP3D0J6QU)H0r**2}u_A+Z=3pJL;NHmmg?eOAP8f6zMFtm=cHq^p?y%hshds4`R7ufAfyx$SPSUPODSOR`BL;lmwfX4iF0>J<?DXj-
54i`8%sLufx49dVFsvXW>;~MZlv<afk8q_5xPll<Xz}Tv=`a6LOj5UC666X_jz2&K+(dL*r<mtn16MeFm=Sn-=rN!IQy$|5frzeRiaUnyivp)Jv`HK>Ku>KM
5QhY;mH7pc6pU75Ovy<JN`=G8XbXoL%vup{KtmN8L4{S8>(C1H8xuUua0iS9TXDX@AQ;ResGmt>W;rM%utXJ@!^FItJ%GAPr{SW8R+t6o0YD<f?24@lOlmYK
05_hk_!xvl!Y$zetqf-cunl+y7ge5IdrWHu-^3eWQs}<TfR%J43V1PI=9Ej>eTzHe5q!oQK#4KMq4Ft3;9P(>P<s4@=Sqp4oIhv)9in&X@vF>k;GIK<bEqRa
%x8jYB1=|4W8fk5LVysKjsllS9u?O?hCokZkSYRh;Ux5wra}{?WIQo<H3k!1wwUDsE<Fx8JT|(c3+afl9x4MJ!F3B-58f4K*c7;jcj$)`AvqW$pe-gdoK6*C
tAHz&duR>D-p6zCRB%+_xNw0gbj4wwVKmV_8e%wE`}8hxF*;%Zjfi*#2nC&izr!^@pfs9+Mp)hxJ%-JYaexd#1qxyqfSS`8?a)=m{o%qZ*xO)c3m7b}7(t(9
ZYKL0$6z}EivVEsozk;yElT6XGQjekZo11g)-cS-@Zt_ka_gAHKqOTy{{m#<{K2@v*g^gn9F8wZ5Y1Wc1xxeOKPx1*4oWXC7XYJw1zd_DXz_NI{XUuvm*es0
4TRc^qg^8uOh1Vb#yHPlkAoWJ7Ayod2MVJCHvy2*^rf6k@Gxx9RL(um#UYG5c?dWqv<%~!l4@uo8#E1E1dk570<0j2!H&a#VZh;)(h?K@M3p_Tq@Y2q8`%PL
2vDJ9KC%(y=V5%I&6<-BxW~u>BxM11p5O$tk7)%>hyKuw4-g44VhoI<`>P0RxIJhW=0BN09&iW!l)HiTf%-bn{!=EYA?b4*kuXJJ>_KuYV}F>Hf=`?h03qBJ
1S3ozXV8@#P;U**nvf=R!;+Dr6Hs^U0!gL%lU1NMkSTktm7ov+(+kc7T0!lBac6(D5&KRgBmcx)#3A7eo-2l$91PP3=0~0k0)SlsE-2!vjVz3uohB81wq(b`
n)qNCRI~vghdYDi0px&#z+>xV(u1bJKOnorh`Cgb0fQaJ9>yulNq0mD;Fow#+>`6ND!`tGWS|Qkx&-J`#0v$L2d4$&qFB|c83-_K7KY8On!z%9p;I~x2dN{G
8qWiK&IPBmfIV0jRLJLI$zV=B%^htqSCIs#IIgfG^pe1_j1ADr1x;F{l%A3tQ>3I&ZLlohxaD9Lio90_69z8LZ{bY}K&9?wP5>yVy}KKrIFdsCxfBM+0k&HF
5)whj7`7tmE!^p!76bn(j54=i6jTx%8MFlR9E2&bBMd}AyO~ihg+q~7urow5CoYA?$YkWwDICL$6IwBX2Rdb-1YAwDS`0nowiZK-10*YK29$#lz>EjQ_cD2D
kDwTUI=CZ%a<-zWax(crb(G9-OMe(sj}ErcY?Lw}49g0`42qD8^8|8aiLiVoK@dzi`sAdFh6)-;6<r}Z=nhZo0!C$mn$FUa@*vtl?cu`EqAMbdcqW-39`qCF
k^xi&i!nRl?Kuve3aFB?zw~=CU%)aGS_H@sT?PVyPUSLV84AFpqopPnH1eQ$sDg{Jj1)Q(phr27HcVmoyG99+F;tCt4Zh2HCSynD0g4a4K;J9)))rz1;Nc$J
<WS^+k^t-+qwpScJJ2J#liY&g;h&*<GS?-H?Zw^VTnwZS{$hc73S-OJzG{{i98N%R#Axxoh=Op2@^A}=Yhk4eauBFpd@>F&y*Nu~kb79VsW4DV2z7MUNYV&V
M5pL*X;L{(l#H8$OcA&cyk~U61L2`^0mu}MZYoel&(;WlLM{-JNF6SwD5590p%;$J;W~J+jC}|Uk<;RNM1T+x)DU9jEi!)#k>WZnS7;Me+|8uOwt(Q^D)%ud
Dk>}nU=@rH)(Jx@bCkLWN5zI90py}j|D?6AuL3H28<~Q+W^@7*Bdu8gj1$Z*=nn7()W&n}00rQo!|XCJ2hA6b0@T&C??5;hS`ITH33%>E#^_baq;o_-2Td(#
hQxIQumIa&bW_TUGZ-KMw~536#3clEz~wUG9vR$$oUDij9diLj14=^ok`btsK_yHS8VYeQJ>5E74*nP5%XpcqAV7F5PlkXQpvl)jjxfZYF$s>mj_m*i1qc;9
93$LMnh^`=6Du1f1pW7%lyKQiL}`E$tTCM)SmDfv7z(BfZc^~!$tU;_6d>>ym!wcbP$s8~Oiv5oV+G+g3?vS6ZjwI*h=B7AhyWSN=|(Ey`V7j!HzLD?yPgL&
0K>we0@Z~&%af%5YDWW%zxjlL>OkCh0OB}q5r`KA0A~lo?6?^)3mgk339N#Ui2LEzGJoj^LHIxodeK?n;ilm10U~(vt>E+$g)l9YL>vQu1gdeF3D|`H!ZF}7
=`u75Jqol7P(WBmzcUPn7KG5^kvj&FX!v~H4&<DRMM{Ewt9CSo3{3evP(|Pj85~hJiw8kN83WK121Y^nKD3MU1a1W>d<ZC7I?aV}DMBNf5!@WHi`-6Sx3DRC
bN6|C!7~I*1wgyY;e&1!H2e~Ep}`PV4O75C9mpdF(`KiC)^hh(ft1?`Qk+_txmJ8A%>59rfbG}tWdH^kKWLalkwQas3KKYwam>&V)1Sfd3<4kmffP#=8FMSf
kntOD0qWu~jhqk$#&s>GAjTViMAFazTL8j=4>&WG*rumVgS$Yl3|33RHH_Fp=X1}Pr}(2eBcb5t8A%ktfZzp}lMxM&fPxf?-GHr8fk7~&oe59@Jse{-@RHyq
h7d4#4qQIVSXv&YIDQ3Eg5P8Q+C1pC!2~6WW(+84;Wv;1m>4)kMmI0SrGVjJ5Dbem=#mCR2E!~EgC#*oV-N;&4ipQl63`<4oM9jzvTzI%gBoUaEE;NNr5je_
Xb=xLLQY`D^Xd>g&KSGVv?`ijiXe@|eQ|ZpEzORHNH(}l#>HaLU(m_m-&n3{(4Dtj9LasWwGMG{IFga|fYoR|nxPTmN%AaUC|ohX#AU=z2QlPO3n#%TfLEkU
p0kZ1YDTaF4g+b>-5h2Kpb>~9R06Eh15Z7jw*VQM<88zyrh!PN+<r_gk!z?l#?={>#|#D)rRT6}NM8_xMD4b#hTQrffe#aCvrt}|El)@dfjcg$<eZin!=w_n
VuXPRu0mw=wiuO5g7>$=qI<~I7lo;08d}3pC<YcTOChlkC^#GeSUg5&&E2r|Kf34Tt57Su%?ET~N8lawOu;4OfjvN)owZpAiOAv=Sd_yE=d>d>EOs&k58x;m
?A9TuU2uXKXggdkuxMfh7XrAPRR~$}fm_kbfq%_e9+tf@A806GxfNGva%tu{TMI@*=miQGF~W?qa4m+@1yOP%YhZ>zm&+<$PGZH|d0Ees-ZEMOYRfnxW>+C(
sGzgM@G2~&bT+h7!g~yv?Wz^zL=x&$Sau@a%V6?pf+X(cxh4tc2@{5EJz4Y>3%Xd)9M~TvXo{&X=tuAbjD=ZVa2_aG+m6BoN*gC@YD6uJkiZ6I!zeuP4h==P
P%Op8Os+<|uo#yy7A{U4!60xHegg3TmRU|UU~8EAJdJTcaT`L^nV}vC0H6R15ZD%A2B4I4VHX#Ppv`zxSd8U@OI*%`M}YqeF2UlN0vv<BW?U9yoG3Pfvq=GS
hFK#{Bp0tWU13p(AeYciNspC_@hoX)=%E?m&4f;f6iyK^Op7ZgFi8dAq5@Y3QVtu5F3^RPzewo}gn);URRJ!A0^Yg(i7Pn9koN+_1l@UG@NsC8kyQ~QHh2~2
7$m8=E=D$T3sjL<1uxKl0Z=(&)t3O3V@L^bl`&SCqbK4Rz@{2z4A3)#ojCooHoJWlROPop6;v?gN*c^*=4(o6xxU3{B6LpXFsvnJowKqxEEm+^;ttd{%fz^Z
=pJS(^q%yH-mB0AE>wbkWF*X{_R~21Ik_?N3_*+2!%58OEclS86ToTBC>qXEGEc;(<cb;9o9QW}UBaapW7KpiVc$|g1kfv*Y3^miph<9C)8iuxP_)*$@GF2U
5EFhH9h5>A2c?-O>2Sp6e7zM1HxKrh!^5x>L}n-jfh*1Mm*Pw{TsRACjXVloBv3dF3*E3*Cddc#FAWP{Ao1|`6op)HO9nea#3p@VOa<;~pdUaXAe$nffSbrL
q#5@mkUtbIat+4d7;)uNhmC<OU<#%(*W2int3Z%s!w4oW;Dxj}hJd{EjO%Ii;KOEwRASwLS;p>zUqt^+;ZBn2z=(DrDs;7S?$LnrYGah&8Y(hyJLOniw_{|l
P;|If?Z^{CgfH}v9EWZ?Jwu&_7#c{Z;~EW@53{gx3b8YQim~8Qp%0ybK_hpD1i4~SP^^wuCOP8zeO8ku+4q5-0Tqdb0j@Cf(KuB$tct2Oqn(c1Jm8jMRK*eW
q`FW%>0xee@dUqQ?T?8FUldsv?SouWS_`g0$*ME`63^W;4E4d?E>8cXJ+5DcQ~nm5g7@c1ixs_uEI16L88Aqxq}ef;EHN8CI@OsVE||f6D)6m5mz}ta%&nSP
?%#p@gl4fBRgrW{b4QS@;&DF@)H@YBCOevB<5t1t{ESgiaTaq1vor%TFlQ2+0))b2qwgUr<6%Dm$UkN?@ZWn`BxF`0-8)>9AqUwD1qW0dO2fSq!bhOj<Q;S=
V1hy<937{ZL;0h*gxk3Gr@83GpTKTphT<bQvZVu@G88B7T>%ge3;FDG2-GO@D>|8=of3uO{v<CC3T8$03lV5~#Fjx?#vNpLLMCgHj2{E6BUy5MZmw=H1TRbx
S_z(td7D#p17qP#<7yfBBnC{Pb($e&*da!`^R(X3g@+;{z!(vL!_uFn<$@$3229mJv$%Ak>D_~2fJp>oO{p%H?jyh;GuQ37DUFsYdV54c^g|3$^u(9}Xc=;m
4Qqk)$sl;zd5&7xn8uxL++fD7AsH8GgX0Rr2YbVXAMOnZ+hjO0)ErP>Z^8;K1_7)XG%e$5nGj!<iVft_2~JHTbK_PQE~PMLm`j)ft_)Gt;;xDz$*?1Z0SX2b
#l!Yipvy9%kjW}IGjjbO!zsItQ&!TX?%$t4#;=(|%>Zm3tt;3fq)YYX7V{l!>VI!v`ybsmRot>~iXI#01w-FC-FwjzJR>)0aib2jJ8%sKNI`sPC<-AsT#L@A
OC%T|1bNu#M5W|rfn4H3j*DQPn*zDtF1F!nF{ZQPV!e$)8|Y=hSPmQjSrydeWk#`kU<^jKcFMjyT0ibNON+WyN=I6AKWE(tCIqY~i;Fmnv|tYSTo&nk;PaMf
<Kfsqq(z7(DTyO$xR>O2TCUHCGW*4VepYWB#N!hCnCPw<Z(y@r_J2C`-v{*aN)`!-1L%fuCt|2)Bnd=>k(IEWlDh~pVmnvcivTxVcjvB8ZWxU_dT?K^*(<IX
sv<=Ft(PrpTs|~$X9aZA5t-3pOuc|rDZ_c(G{G$nbl2p@@V>dfl}rS849}K31~xL;2CJ-%dlEQy4Bo@!*huAyg48Lc+luKQg7Oew%HW&}@u|R*U<qV@4Hr{%
j8+xYea4LFe1;`D$L#_}n5_wvi1J1Ux#ypVVZ+loI&+4Im~*`*tWO(ysz6baEb(I%S2<~xpw;B6CR;Uxp(<pD0Y+ri&cNX2j2Z|L=GIn?wi#DOv;?7YiPizI
O(4y(cZvwf{Cg+_l<F(EQ;ecBeswP_k*P{_6dXSzg3G#>V>Fp62zFFtckN2}AI@F*D*CjQ@NykUmtBB56*JAPa>0fgy15L1q~cAingPw^m+NL3xiJG+MmA4D
3%KPBmWcbhbMj9>2shYg`0BXjSojln_i(>57puGk!$BvYXt<c?N~16r3_X2rIxO0RZRun?hG7_BAoNX)UCxCqMiLpT@v>Qp8@l7}J7A*t>)g|)WV<lQzZ1$+
FylYtLO!=8g-9;g35+MBV4#cIiUS81f}4+WQxxKu$|RDYJmwJETbB#F!*|OEqSFw!9XY_9V#N^dN5>@RGcer45NFEZTkv{hr<NjDO?gjQe&9+S4>B&8+v`?>
8QklZ*R8mT37Ud=8X`@K4wiT>&W1g)sf1+=1Lc;Ral@iM7fU=N5LPy6MF-Y!Hz<0+eL_W8>&v*&8n|h_tSQw@)6$9ME@+sT7+WKGE4V-jIfS^J(JZck8O}v?
A3a3EHq<C5e*$#Y@%Nlz1qu%=JjDJKZ3G=P=opDloe%+a;@Yb(Y}oHWzdOx@NRz+?h-6rt@l~?HLiUA7R~caBb~{XMA9s968i=g+XMqemuAGtgGSC_DpBs1>
0bw8_lU;_oO+${3&@>m^6L-3vO2%?D-EUeaLnd*|^B+wx@n_3RNhKRH)qR!69@6*cX}cZM@yF$S5whc1lOg2%&#Hbkx?F_3tT#umeti7@){1I8{o&~8|BZ=3
m!H2o`0i)<?@e_%E<dlOpG{UZ0Kkj-A7aA(r_th^Df+W&ww$mmMWezIba5JhtD3ccp1eID%^M%f@n}#otu54B2$05{qL0<=v(yxbDN{_Usur`)e1dX<gZ=Sx
F8Fs|O=r~wt{D3G^JH{!Ih`@1>+G_e&8tK*n<kRSby+UX$D>{&HhG1wtM*cts8P-vlgqmGMoog%NwNGwXtP<hqHgog>7W{;N0UJ{Y+T@nX6xYRN#n9pcdGq(
cD7{Z;46NcHCu<5?Q$^amho_NuP%SEm()3Zowu`PwX302$@qeH7?T^V%Fbn5dc>A<^kX)iE;<xUvl~>n+iGLHr{j-Rv&E*k7#?Nbp;+7FX*rlTn>^{!-mU3<
d%Q$B=t>4-v(-8r>^S>oRiPWFVL&=j{LQi*<de)#_O8?B_D)as7Ugp96!*aOIx-MwD<a~<eVTVpPSO7%tCNfe4U8Es5VP3!PB}^}T+zX;aB~i3a{@^+JFtoN
Cwo`8c8jgbIR*}DHXb)|!pVozPKOOXoXWL7@X9B9$9u`%JN$pV<OlvG1cqPa-_z|&mA!eq+<v%P>u=x`O0Qq^nt|Xtfoa4G@%h^2C2Msxf7^pd&ZmRDgT1K8
Xe}tPcOXv^KA)mXdk4HF{yk-H!<Tn^r@yy01vS_uD2jQvq%b3R{Z=C1Cb+nK=uJP>A6cH|rU<@3n%(83kLIOF;N8ZzpSpFe8hrVF{maqymoF82x*_&ZE(cfY
EeB^6=F;BB=@_%?ZsAivXgY~fryN8E2W!#@k~mls%I%|)tU3}7)!)K!#b+8<ljgc!w>llABq^1@3^sq!IZgyPglS*4@v(J?zuFfc2BTRs%=x(hMp9jk=8Nw1
L+AT)Jg<1iCR#q)Telc-?tYqq=5`m=)uJi0eE@)+Lo$JgLNYt;O*a}NrMiz_JnQPb`|9!Wu_PLYl;WpAmA7x+Jr#I?VCyG2p!|PN=1|1$hw5|e@4O;7ET*%0
r-{Z1ZrhUidpR2s6~9RzhOkBF0Z?I1hK+7_0zB$=JDt65m+;^1?i~a(@bd)r_C~3rm4*F&G=b0>(@C}eiI$edp7w)jiB^clHQ2=c>8Hv51qOWG3<qU^HGJF%
r=7#1LFq?}(MMK<8jR428P71elkw-qr}GL{3*YE9G{)1j5~Fs0G3qyhk~2m5?<ubLG+deXx1L4~ni81P*=TtYDocd~YFcfv(d;B1;q!Slm@!!%nmHPxpNs0I
xt`8{o=oTMYVvV}wkLbLstE3#cJ|cX;YPE~GK8VUO%4Dl(C{a8ycW~xcrL6UnSY)~J3gGDvvkO66aIZXKt}NWzeOLUd|`WzlPL4p?5SY)4-j_p`W$~B&1Tct
#tAh^s?Qi#pl{vzuS<w_UUQ0S!U|u5=CpMX3N$s=rr7k0CP6z~gDNRkq)s&73r~60d4KW(I+z?J2dDe*PY#ms?euU^O*%mNF*)Q}n}rUV?~@Xk&{3_}?DWA_
gJ+?E=B%q0CC{HPao+W1AFP@@!jDXPzd!@rD-jS*TZcFdGBWN$eb1)2bQ2d!_En`)UNwpU$9Qrx_9r~o2=az$dMyt|iFdAt07nlaV21lP*`N)z4$e7xxUXOe
Qk?pJ?YRRRdVM0T=NPB)2#)t@f);onFdBmF=8vt!BnrrbOCBUC8OVP$-c%Rhxofi*W|Y)A7MH*b9ZKbaIl!dBr>L$1B_05SM-#B(`SMb9L`+ZJ$>n79>$0LT
o?%W7FhGN<&l(62ifRQ(i`dRD*Jbg(b@(3Rety~Jt>l3Yw_DJ_^!lOI^>ZIS<87<agu}Ww`Xw3tvj6wdUV^44d|1k*Kby|y&2U7W#-B8(6i%k`eYR%2p0zIs
m4Bz$&uVpfwo)&gD@Wom*AMilX&*e3A6jcV@jf{NJWtC-Gye7{!>|1@VN=K<)q;A`?Gk#s-R8U+4-?LG(U?XrSVcLoK}T!NiO|vxu3od(YM)nEgV9+vUo>G{
_rA8y;GR&Gb;8_h9kP?{SDh8%Iyngs`F-=M)e_QjMbdH^=+h-XmoWO}r*1vCd#9(ZN2>C?x?JsS?P@zO7B5i8&2C)a*Xs+QX)J;Qz9JWkUH<jaMx$6AW!0!2
<BjVs6Zz+3Cry+Imyt>#oiq*|B!5|jaqB0O1e7WviAvD(eiey|jOBSp?T2psqtEX!)#pLi{?<tkX60yJHGV3`%SuqW85k^?5zD`@?#r3@&Y1pqeBperJMpp3
>#iRzJFibdzfTW8cG!^z@xaH^!&$lwpG$ZpYWv_vI%dm9v-Ggn`S@t24*OF!>5oU3&GH{Tpc263@bY{Vq}lIJ=gt09dbH>?d;9(AgHo_`{i5;kq0E=-DVcC=
Vh3QX`c;!*)5$|6mjeL|jd2Iu@4@^U=F5kinvmYs@x?=oz=QZ3{<+*d3wJ-{RUd6XG!Jgu5_SQ%9syN%V+>C^IRHwBPwL=wH8JCPYhVJ01&;4N?>jwf#@}0q
f$4PO;hBQmTl;Jp5JR{<h|{PuOZiyU)un)I_aqf$TVAjk+dm9fdNgUF7ec=}?9~G~d;O9An>YIiBHaJbY`#vUsq`Hf48Z!S6Rp;NhnrtR*-y!TM>q?&YQ=9+
jazX>L>hQ=PK0@IJ%=84lqk*YbIl{<w=knNPCQZ4^XjT!T`n5U>uHia7IDL1g|FA6`r~NwczhO)UXz^_V`=uoWISs<Q0c?kcAEMbqEC6tBLrc*PJ$Q`FxE-u
wyqz7D0klPp9zrmNrX2!z{=nqzI=_z8=9OxYO4L!mw%jXsN}rr1ithV3}RV-!EM&Z>$m6uAN1P`AO_9Bn(r3IZEFggwOT9h@*qB1xC*`fZuIpJ__X36(uJY&
&8xqG4DEZK{_gtla_#WC&%A0t%L{P)TW59hZLOB;t=4?(15%y$tqoUOjs?NBHr(#m_~F{``+DU?AN-W;!Ht_&YvNk&9W2+s$C%hb^ZmnqYvVYp;+8#NbvH`=
_3G!}zb+2<HQ}|JttNZPgrT<1-ow3Q@%ggCTwj2p4a?<t(K+FsM4Q<3bl15I7Hpp_dUSn0ECb+s=h+fixaV~4HnKa<4%KsabXmJ}M;P(n3nv^-d%xTgvpZz%
*$!u53`$*3aFUaiW7meZ4VL`{E-*>THrtf#Yuxyc#t$-y=+}Zne@<Y{!Ko*M5gwEQ<#J5li?n+=`7pthZY<{vVXv%ze>$BFWW^1>_+W7^#5;Z@tY0oJn|O@&
tD2Y|4wsY8xV-2M%ErGA_)`tf{CxH>ociEj>yRZd(%EqRnz#(X^<Ne2HeeD4Z#eAE7u6-_rAw}$?);=wGQ9qHcKs0}*qvYuJK`nb18h`hqYJb4RSaaoZb5|b
_1L9O-7R4=iClx&Fl+N;D+vLecqn`cAyS$Z{tG+@qKxHc5!N>W8h30jFS!!X{O!ZR#}IW(K1$G0PHkg+FQ8YXY#+o2l8_t&sSK*tq4FI#5W->&DTdu?hO0?X
?P2}--P-4Mlw51Eel)3%uE!Hs2UpR!a94DfdMhQfp}LHoup@ut!2{7~emx8^v{f1IRq!mh8nv_k+j^jz;jZMtgK*#9TdUixJz=M__K2NMi2v<;(zTYGhtrL7
)}Q!q9i!3%>3DPR)ti^EULHUGvAg$hzL<&o%W2zcJ=}{A^lv`VH=rAg$yB`d$zH_+cr5m@x)HO*=T;nv%|(d&d;Ss7*DPCG!N_D!IM$xbdHMJ|7coNM@#*8^
qrGG$se})|5l5^elwVeJeEm|Z+a*$%{f|Z`Z!W}amS>C=(zk0B)<yU4tTq_yxQAlm(@(O+K3FUqI14rHqY+A^{2>5FHZXA0Lin*ZkY7*^F+53K8FRf*;k71n
cPTfGe7}Cga6{|$mXp<#Slei#WuwXVFF&nc#i`X(?#o9ZbYVxW=Z*_*ympS;iny=jJZ#noB{EW0fZ)DP*_RU%OO!E==|WDD(u%OJk6XMo%eG{hF@-m$^`+Jr
W7vnnv!y&4lku(QqeZl0U)z!q=~CmE4{T-8>3U356u<Oz5(Z@>&xs8JkE_c=GPzH(XqjMZ@=zM~uOfFQ1+bFLw%n!q3is$5rmLH<4L{YgIVm+v$Yy4Wi}}B-
vXF5X0`o&}7d&^0Sg&Pwur8F{l)U9OvVwc#RK@}bn}XMWT=0sexL90(+rXd^`mZH<Q3_qGOI~E;ARKOF(VFR=AvuA&#f(($O1Ysd?8IPQjMQa?&YgAI-Y$3M
c5`D^E*pJvyCHVdW`Q3jGa06`IlC!$`-kLi+g?j*uVvbNAtf5zpCa~jQ|eOhk{c_FqTu%6d{gX(<y*Y$<SJw@rN9i|62uCdvb8#-pgGIB9NaI@gq{2jp)(bP
JE}D`nwb|HQfD18=5;X1x3C!U{A+Or(^Rp3Wo|NVnatE*OYF?XEA*DsS*Xc*%dKJfE2cR^<d!>z6_hm(sSJ*lpNy9xS~*7P4yh}S3PjEg{H(074epBD!<jJv
jL*IrVwi#q!CS?;Rd|ZOlFV7CHupkN)?}__A7R1Fom8iB%Q4e<SgOYf!gIr1$WvgV9rMdsg3PHq00uKfl6p;0=`Dca4q0x3_AH8&7y5pLDeggbrr@L*%VDti
T;^}e-K5)cmwO&Z>F$=hxnJ%&UCDh5*jcog$+-ngJ+~ol%ANHywQQCwSW`H_I+O62=U^clre%e}$Sm{ieJFQ?*?f!Ki#E&Xg7p|?*cNFKH|}3cUh1}R`(Ca!
E3SZmxVs_7Y$O<&oBGbw5EhS8+$#<f{#Ot@OI3MhQ5zO<%C;;jtC=v{hy}n{jJAgMjD}V@mZ>R%;1x4Ajb{cfi#O|A<nG!aM69;MvOTO^6-(D{$o<A^j_!sT
tL~ONW=&z3{=$5AR(9AScXLDT=9|b}-zs<58YWRfO|3Os`tF#{q@dPCL0)JgwmW8<85ZV<g$B8iIwRt<j17LjMd+H!4oFk1H(VGgP;f)&AUO`>!j1NdMQQxq
AY<~oh0glK+~_QoXql68Q|O=u+fujoTfn=#Pj5GYgs%j{>6pgHVp5Xcv*j}x?qz1RaVV*aWX6yqTFttgG{(_o@>F2fDavuJyIdx2n#TQ{6n5JZy>D}3rIO`P
;ICV_jJAKkXM#Op`fSdUQR!b!@~o`IO7b_nCT2>o7M=}R!_jNv#&-}JR>6{dtl%}}%o%q~Pz9vk<uxf*QHFVj$z#>uEk={&iba;BvTd$+Q<^^@dc`Cy*5#6n
^y053dKUU&q4;gDiDf(rXeW~ZV?jWscc&SApUmYrs$vagmj80(K&$|!@A8`XBFda)N{Iz}o4{*L(WjDwi0R{ZvzjlHylumpvgQVB=W?3v_M84UB)`Qbnck_b
VeLWYq^TQz6KlA8vP4$@TKP?e#i3Y>y>KzD!SX!?Eb>Hzj+u?OIZj#%EN3jToolxhC16Dma2e(W@f890V~xAdZ(=?nY>;E3qPBl6u|xlubam5llGJ*(DMIRp
I8H=N%R>CBPRA`&0emO<WXj^5juWdrNtTUN`P@QyIBx~>T(V5Em+prdbq}Rs;RVcBbd9y>|5{QnSiOs>z&Cv-jD|LhQaNK+t`h`er1-K8xs>8LG4C~FiIVhg
&q+yzW#*HouGqqug6|f<<ykX~O#W*yruLke1kWB9d{4*@9(hCR%6$_aneFD0Op#=jLO61ce7f-4j+6GRaR~0`^E6~<(QzWBXKI*bIZhuPC*}YXsSI;qvs(!~
3-3t1I@Tp%7~m$Cw3f`z!^LE(?oP*PUF^o(>o^qzL!)Vs^e%n>-xfTxVp%*%OA1=XcMNPhP7FA*0A?O@?5VB=OWLxwRzYP7eiN&@vqDlvexq))sjAKFWzB*k
G}Ts0V%!uwYn#(U<|`7=!MjoBJ`T?}8AuABXWa;&nVWLA`i9)IZz6YptK9hl2eLotFkce0?K!dVH;JS({8M{Qe0vAq)Wi2sgv4ZCg|Dq<o*+}$Z}pu#8732*
AyJmD+3B&SQrnfaF2GT3n%|8xU*<f~>mW0Qf42kRB?`MCd3ihhR|CA5%iTPZ)sw+QScE%g?V}wFPAL~DGI<q9EMdsnsXz>7JLasumc`;gAR#K}>sw$E?qcwO
8@@J$8LLu-X+!iyn~9-Ji)WsuPKoj6CfL~YTK4&U&XZ;_Jj={r%{<({mgrd@1rTU%I8T{Wy-Qj5F00=|kV@D%<=dnj*D&JB2Rs3vro=Cn@w_Vv?^v4#lZoXq
joFS&LiDhPoEt1@a0{#X1EN<@nvCztVO97n^ZqZV^(+mXZ+lOfW_bwKY2s_QQd4_Rtd_u+WD&1IA~)S9FKe1o{vf~0ePWU{YcjG>4i~bv)<5_nA(m2Bh9wSm
Gn;kM-|0PRt6h%gW3lJ(hPyvU@>_(G70g)8!*lUk`5oR93r(ebPn!xa@(A9O&G`DY!kYL(F!7#Xsu|U%Q*fvEq(G>E0fd44#u6*5_sHwaG^;V}cAnOyexLJX
`QA3Z5R2?p{k4Rih4TG3d?$G?pZ8p$izHrrCnq!>)W)UR%6YQTUl3ESmfYn$S-zvncqzteUA_e~o&|?ksZH~h9bW)5#eK_8d})qiL1+3S#a~P8T<X{~tig41
Qrm=;gtNL@JbkB}(HNFy4P_hXJ9)lRCpQ^d`a6B6loOw?mLZ+Ywsf6Uhgj@a@kM=Ec0a=SdwnOzYEnuTW{O>0(%EgP>-1Z2Npq|7q*y|cb@%wbL$w_k%UPv?
9AEQ|lA$~ft5z%Vs#pbrHJ)qdiM70><|qp_-b&)(hVgYhoIHG;)@~Bdnp^UU5x$Vhy1OyPWcN8wR^E>ROV5YhA@&=}uGKdYyT8?E)yl{VlUVC;d+md-!&F>J
WsMe{#@9B<S}|V-!V0_bZEHXSur$7+iBNjm;)h{D8CId<3wl_?aJS!tD|2;`?^6W8-3>6t-Rn2Ws=Om7!!*1p^X$etpZ+H6eD?MQR=)0%uXNzf3ZE7?+$Q|S
qF5}(nz`C-V$EE`;wL5+R|l6Vv~2WnEcBk<uIV(D;1r(h#hUCEuZa?3=~mD8XZX7j#uWE?P22*-P#fzZW-zFytV^<4fMZvl^ry*wxYB-|mR9FUk0$Z0%}n%Q
BK2oU9NmxCYz*=D_%jow$KzE-bIf0^6EfS4m&}ol>9bWVMZ&G64cYBDk15TcCEYo`)cKA|By|?D<Q{+9gy(OcpL}OhGBifMuP(osLg+tF<e&DuT6A&0?&6#Y
lk=u(9bW$s^9H&DW)d{Ramhl+Z0mm_xjE!|#<C%|XL}}#a><SI_P(^wI?JeYXX5AKT5{$_>gGwkS-sAAtaBaLDmT1hQHHQxoB21dBxm;jbY7iEYDXvJY)L=L
%j!xt-s5JU&Z}9q-S{LuJz+A*6Lx1%u|QDsRkAv_&QZWgXs=IC(eTO1T6WZv)>=BSoHpsOi%(W*cJW|GONO0v=+(*U2Js|H8(P*0d2>(Nv+`p#ZnhFOISF@8
V*Xv|_`dvt2Z$Ho=<wa+^@ESA;UY-5oScP3xAr6s&WuPVx0>P!R?U-r)!IlO4PRsz{%^m>Q^PLdP$Pzl!n#92Nv?uo#5A)B1a)<CpdU<5Ssq7{&L)XwCd}0d
j`Ej>`t<O;6EvJjgI6caCO>={4@vKyFqbn8sg~6OvS-5dgQqfx`%mN_`Iep@0-8$Ajrt)i@vz_PG@DNzK5cQ!e4U-vk{_83Z63%8a%tv_#Jh&{kqH$v9O##e
W}JpGAu)6!Vap_Rp_QmsveBl5RweuANy#y4#cBbuGR|3NqbYjQ@1glap3`~+wtJ4h!coPeibt9H*m)I_^!}sq^yz;!uKrcS_CX`$s#dUxqB8re;MZ!zdQ*$3
K)sa28ck=1jY)MDYD{3bLK<>sKXfUk3WUo=H5GL^-H+d>DW}OR4%Nn?)?t0AHL=A*Q8bHc0&HqRpWBIQCu#fiG}Ibt#60IteZqsaYrGHXtN4eK4C4nyecg#|
AH|c`^AD@e)BPuh&!8^XWg4EWm1&rdA^A?Tst-Y>o=N2aJk;u-st=|iS>>Xff9R}A7)+8$E9p(A<JKX6xRyk6Et8P7we$BN)X-ofhxK(Lojc)4r-`U&5}z>X
_Y&BU#y`juM*UDhC(gra-scnx^(pQtP_Z%8AFDpTcVnrF!RTVWQpK$;pGnIwc>orj&1w~4kaX)&9L8~ZaVh00n1x!Gtl(+*KPq1JxoU>&$JPT?Wosfq8!0^z
y4L>4OqY3l>S^znO7bK(AZR0f_i)kK(7vlW1##Xzo0WAQ;!5r!@hEVScYrg2xkc-68NRNheK_AZ@Hzn1va|l+H9qez<@xdGgZb_T^VlF>WUyo=+yqvdXAI`o
-<Bugd@v{GH7{GIK<mML^XQyMc`268>@)|<2M=@@nbyPRV1E7WkPX^BJpHF~HfXNr=!Ps@`JH)3{qtrEK-Z?^+QOKctCZ^LWWJb{1e}e*ka|3!Uz4ebyxBVV
GI4JV8}P5rz~+hd-I>3e-{?a3m$JXn3;sM@PB4TUdE9YWPxNVho%+F}B$tb+JS)zXYB$hDTzc9Yl@rM~-0EWz<_L&i(5o#Ot*30?B_7FDqm24dKKF`dTMg?Q
-%!}q5AQqgSD#;ZUa$4E7J;NVUUei#_@caQhE!PGEjjM2600SFy1=n_t7FU6vEyZDBa=F$NK5O@UzXRuNd33Yimuf+fN8u=XMVTYX1S{kBy#;_*;!tHxh@YE
vU{8TSR5b;K3+U}4tQU$gWKu%uCEa+YZv}i_`MoHoU31@cGdcC*SXfM?Of~fu4L=-i>n@%Us%rYX0uQYb4TK`(mUI;{1Ax5juR|leb*hTYOtfZm$wY<JcA_)
cjaG;{{aeFZe~-nJX`OVo23s+qUyh$YdxDt$rljl!SteCyJa|v>+q2XNHrVY$i9w=iLV~NIePJSFImg#<;O_%TU*(TSDm#V4~NN_e7`nuSFOY9a!v_khoh?w
oq#kkMPk#$s>FgyV+OC4sA+DU{t#zNb&hCgF^^A1;{WV#wcNk8C0Mh5fL}w=n~~&|UtJdzk=jx$6u7+DKRe+st-opZHwxrG-#mWy93qiwaeK**=36pZ6&DOn
OxX^)8US)bVD0|2MlWVSA2i@g81lx49Sm4IP{rn)z^q#j+QuD<vmrk&C!--b%|1&syO>&DJMf!gOs*2Ze^8e|zdC!zKOVn+wFfG=oKO{-`zA51(+5#>@Tnf+
SPs|cG+DEeos-}8sNnF%N0aJTxaBY>Arp43RkDZMZ6Bp^`~5Uw$N|SXzwOmC@<0;T`4LwG;OreJSv1}ojOLen2cp)$*J-`$$>y{6)kcoFh`IA&XX1JiD{XgX
?f5AXei1-(MoZaBuIqQ#iSVOEYc*fi6N*Fe7^a>}1~T)`<-@!B!|`%;2%i%9#2fCNO0v6rUn}@|`uDU^;W-;kzNL1fc~p*D^Ua~)A?3WuL&;jY^L>fuY$})k
%IxUT<Z`)SP2@1-_^_Ta9X@<P()5R<mSs}QGFizo*(u8;%5X2aAy9Nn;9dqXsjE{awL)x7+0~dxetmuWI=Oz;i~6VKbrSuKkvzCjgi@)rTPM?R)RjE!fhc`g
1K(I{m-*jskLqmjqZiLsso+7J+u7iB+y7WX`0xK8>1W(D
```

The two-part recovery capsule is now complete. All exact methods and preserved numerical states materially used in this coordinator continuation are recoverable without the originating sandbox. Finite negative searches are retained with their invalid states and termination limitations, not converted into exclusions or winners.
