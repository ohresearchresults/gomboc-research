# figure-0456

AI research report · 2026-09-22 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Bright Raven 76 continuation — exact C162 whole-interface contraction

## Result

No strict own110/additionalweak000 body was found. The strongest new exact whole-interface descendant is **`BR76_C162_COMP20_G3`**:

- `V/E/F/C = 54/81/29/162`;
- strict `(S,U,H)=(1,2,1)`, additional weak `(0,0,0)`, primitive-zero `(0,0,0)`;
- S=`[0]`, U=`[2,20]`, H=`[[36,42]]`;
- one positive physical P bar; **Qbars empty exactly**.

The literal parent `BR76_C228_REPLACE2_G3` is V76/E114/F40/C228 own121/weak000 with one 26-vertex/24-cut P packet of relative depth ≈0.415045835724. The C162 descendant reduces true C by 66 and contracts the whole dying packet from **26/24 to 20/20**, preserving S1 and Qbar-free status. Its relative P depth is ≈`0.438281148548`, about 5.60% worse than C228, so C162 is a topology/complexity improvement, not a depth improvement.

## Exact actual uniform mass and mechanics

Exact volume:

`1700146160438202027373191069691245780797103457814298168425572184341482449112488473478411969772286153548533719072366051666697198039855446951839386361467527467430057148291016935268166117692135824032761415092568236783423064538881731817907524088490894500508962003071096380794849760945704958031250/18911823189725664755944601396525148718533054709323677506487821265082915535765445407612035227904756034201649801600747471499460064683377395758080801941453889742704239827586895317084614859323875081320168420752662683793323129672367777470519092961397323430719000492418924365951535835006247175501`

Exact centroid in common-denominator form:

`c = (383890118666908369120975995898070772081251717981082012799835233586962689093708178850162576129059323739728076703529354973253384623010623985257411728502515793290409213752454190420254960007205819826911906960842131286833604341833006098226738141238073535676241998214779192214683446174388713734842304489968029610784847020584486185396319263984414056246270187008558123502225614676374346055972685905105203306733589997948225945503132326813606165733729181175314805605724170873241546968052493495263684010752465433084829588207792374600730678659125243446976534002875869785828441210075, -1959114314911651262418257305767684998807438182206282107209465447478860565596561002548964108183355706391163053994367753324226504648250765987876417101113741361173154344838302879248273102104356778220384525692226244156791700442085694161733929263003910241742798713204696783548991643903946221118214160431165029407439189788100716357290287681613585146681397139251315927032122418313662226401172419778122980629352193135351489592136929783481984981326921262548989839091895864465873644560714393763302774175301328896001653907284354405606493067240833200664911675262184107125337618229925, -1848920433433741564691134553278860986929324934569257359506363688674450573095955743059126380550447070659224628129845078759132326129410887698081583230800290940470500665662661275010033152087557856476595657926713778482220090527810538796397969552424468380315338355030673635853601654463974481770955681901401984633200315897231878405040773883336098985610372300241141983042006226311248315354301617557391380204947410105574984152285214876337762072374797814133443028442595949376690723716257170940029469589257160557343843362242352493709832051890875708177376639601762218453601862837550) / 29400080105875543164002120436393198350772127940576857488719860210966118514487430280810965288995761060958704002661197661790967209469778407748782937751078597939354498038370225261573933689544197695385355277157951459210285133765249971351279477639632563717136301182396279204192036041281926410106808234051301699660430422372159514333151601501406759762540121153511385852244362209528250895542473610951775664793040833587606672628157815145459609608829479594230672665758517227789448782849135969588331116467055638205896922248810615781118026391799857812943013631540901846681835087100256`

Numerically `V≈89.8985858413614`, `c≈(0.0130574514519839,-0.0666363597601262,-0.062888278765752)`.

The exact P bar is peak `2` → elder `20`, death edge `[36, 42]`. Its exact birth/death/gap fractions are byte-pinned in the generated exact report (15807 bytes, SHA `2d82057c3001d4fc32dc2ca5da33c3588df824da8b646e6c5ea3fcdf96019c0e`). Complete dying component:

`[0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 24, 25, 31, 32, 36, 38, 44]`

Complete cut:

`[[0, 19], [1, 20], [3, 9], [4, 11], [5, 9], [7, 14], [8, 26], [11, 15], [12, 14], [12, 17], [16, 25], [24, 26], [24, 28], [31, 35], [36, 42], [36, 43], [38, 40], [38, 46], [44, 46], [44, 53]]`

Attaining path:

`[2, 4, 15, 25, 36, 42, 21, 19, 20]`

There are no positive polar Q bars.

## Finite support rewrite from C228

C162 retains 26 of the 40 parent rows. Removed parent row indices are

`[5, 10, 11, 12, 18, 25, 27, 28, 30, 33, 36, 37, 38, 39]`

and the three new active rows are

`[[279, -231, 294], [29, -88, -78], [445, 173, -158]]`

(all rows use denominator 1000). This is a changed maximal support complex, not a root relabeling. The numerical producer used active-support replacement/pruning with actual filled-mass rebuild after every candidate; exact acceptance is independent of that path because the final 29 literal rows are embedded below.

## Exact scoped pruning boundary

All **29** one-support deletions of C162 were separately exhaustively audited with exact Fraction mechanics. Every deletion is V52/E78/F28/C156, weak000 and primitivezero000; **none** is strict121 and none is strict110. Deleting row28 is the only deletion that keeps S1: it becomes strict `(1,3,2)` with two P bars and Qbars empty. The other 28 deletions have S≥2. The exact 29-signature ledger is embedded in the recovery source; the separately observed ledger is 1213 bytes, SHA `0d9955a62996a93d283183458d52606d121bae70709bb85806bad2dab3f84f93`.

This is only a finite adjacency theorem for deletion of one of these 29 literal rows. It does not exclude simultaneous row motion, multi-support replacement/addition, projective/affine change, or other C156 geometries.

## Preserved C156 compact alternative

A distinct support replacement gives exact **`BR76_C156_REPLACE_G3`**: V52/E78/F28/C156, strict121/weak000/zero000, S0,U2/17,H35–40,Qbars empty, one P bar, complete component/cut 20/20. Its relative P depth is ≈`0.618111128926`, so it is more compact but much deeper than C162. Its literal 28 rows and full exact mass/bar audit are recovered by the same capsule.

## Executed finite negative campaigns — scopes only

- C162 support replacement: 3,000 nominated one-cuts → 347 S1/U2 cases; 160 selected add/delete replacements → 23 unique F29 own121 cases; no U1; a further single deletion from every one of those 23 produced no own121 continuation.
- 10,000 deterministic-random pairs from those 347 cut directions → 9,905 S1/U2 cases, no U1. A subsequent 6,163 one-row deletions from 200 sampled pair-add states left 392 S1/U2 states and no target.
- 5,000 coordinated integer perturbations of the five principal packet-carrier supports → no U1.
- 500,000 random determinant-one SPD affine metrics on fixed C162 incidence → no U1 sample; **not** an affine exclusion.
- 20,000 projective+affine metric samples, each recomputing the transformed homogeneous volume centroid → no U1 sample; **not** a projective/affine theorem.
- From exact deletion28 (S1/U3/H2), 5,000 targeted cuts gave 321 S1 cases, only two S1/U2 states and no U1; second cuts from those two produced 156 S1/U2 outcomes, no U1.
- 1,000 free physical point-bridge trials between the two C162 roots found no S1/U1; low-P-bar bridges typically birthed a polar/stable packet instead.

Numerical nomination environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0. None of these finite searches is an exclusion.

## Continuation

C162 is now the preferred **small-interface** BR76 seed; C228 remains the shallower-bar seed. Pure one-row pruning is exactly exhausted at C162. The next substantive move should therefore combine the two mechanisms already seen separately: (i) a finite multi-carrier/bridge/circuit event spanning several exits of the 20/20 component and allowing temporary roots, followed by (ii) support replacement/pruning and actual-mass recomputation to reconsolidate S1 while seeking U1/H0. Root identity and the death edge should be allowed to change.

C162 has F29/E81, leaving 76 support slots under the sufficient `F≤105 ⇒ E≤309` bound and 229 true-edge slots below E310. A useful carrier region for the next finite event is the support set around C162 rows 10,17,22,27,28, which jointly control the current extra root/saddle interface; this is a search focus, not a fixed-topology constraint.

## Standalone source-only recovery

`RECOVER_BR76_C162_FRONTIER_BUNDLE.py`: 8876 bytes, SHA `27ea97f49be19beaa70f487dac5524c9cc64b22dd0e133857be83f27bbcc14f7`.

It embeds:
- `exact_hpoly.py`: 8946 bytes, SHA `54e4c8f2f6f1b45955f42b6518c4a1586d94cccc8f4dfe3ae866cf5b22f3aca6`;
- `RECOVER_BR76_C162_FRONTIER.py`: 6682 bytes, SHA `175255a14b8c4e7dd62983b27bed645d6d2b69c8c794e7a5f8ac8643a52449e4`.

Generated receipts:
- C162 input 489 bytes SHA `72eb9341b22d166eca2ac0059cce7977f89f476462381bd3d6f62f59c51606fa`;
- C162 report 15807 bytes SHA `2d82057c3001d4fc32dc2ca5da33c3588df824da8b646e6c5ea3fcdf96019c0e`;
- C156 input 477 bytes SHA `fc3a60acdd300d4e400db0fb3a28e44395882d02505261479a2dcf562228ee00`;
- C156 report 14715 bytes SHA `e2f8ac3dbdff8671fde829c102a4483d45ea89668518509a3c9b96b47111d6c8`;
- certificate 14142 bytes SHA `ae276a26286821de187d158de014b5e7b4ba15cf61704de7d06d40b810b14e80`.

Run:
`python -B -S RECOVER_BR76_C162_FRONTIER_BUNDLE.py BR76_C162_FRONTIER_REPLAY`

Observed markers:
`BR76_C162_INTERFACE_FRONTIER_EXACT_PASS`
`BR76_C162_FRONTIER_BUNDLE_SOURCE_ONLY_PASS2`

Optional exact all-deletions verification after unpacking:
`python -B -S RECOVER_BR76_C162_FRONTIER.py EXACT_OUT --deletions`

```python
#!/usr/bin/env python3
"""Self-contained BR76 C162 interface-frontier exact recovery bundle."""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
PAYLOAD=(
    'c-rkdYg60EvVTR(R$U|*gC+Uxom3G5o75(R1wwMls8q5fV-Z_&B-vn6{P)}4GoyzwIqW&#Zru><QBO}#Prs(8NBrCgA3Q&Ir;B8^K3J@G20Oq1cDT&a!*LWJ'
    'hVe>Utn+CS+c$AEUnFU+MR}O!NixgWU6#ab?&VXKtur?Dvgs@u-^7zNnQN02s76VgX>!=91ZZBSohqbd>=P-4l!n354{zd|I0z?NkmS0@#>OBG^JN-q*>bKw'
    '?5(v)l4=iZtwpi+7%d3J5F@-GsEx>%i&>~Y?Eh*^wj6I8)A-ex`Emx2`R16tT#UgHo<#N2B+F_O=-$Y5_QoU2X?XAfEz@DL)kIiR^fK8p5oU^BNi+yaGR!ZC'
    '3R#KC5H1maWO=GTloG_JgLpX)Q!h_aLyIQb!$A<n$vlb?!nvu1vn<pmyFV+4PlrEiXivLxaWgN=qRCo+$c({FtieB^=*?#O!<%L)3+$B~>;emspYLuU^B1u1'
    'L+`u9RiHSLlV{0n720}ive;s=%>u>3JC5>EaHE*&9p_C&`7DV;(eb->1oLuD4;cIyOgm0JSoUtFrOR2U`N?cK2QyB?#mw`=KpU^Mbec(?rWu#x6tM^Q4u~NG'
    'NA8_*_)fc@hH0p!$$h59ZZy=wAIoUv&B8dJtx0V_L@EyEvKV~W1`Z5!Ul8?7lX<2Ezc!D}p=ZIP1&<ayT0_r<M;jh(c(kPi9(b^)>wvWf;09pAw`DYRAR{2A'
    'fb0v1B_Wn&$c4OH3ks%L!8ehDWmagKNC6?HgqUVQ;jyG(Sq(7{Q6QQUQc^&OB_Kvk<NB%o?t#5C7<{kg_al5OpI-)1t_NQ3DgA??@+cOt(Qd_TcO7F$n&2bh'
    'v2$;s113uigX}Lw`xC<uZP#&z5U(-_ct{jX+KU4XRHtLF@rJjQ)+vZ;D?p6=Fw-cyfn{r8>@W{dg`k;*G9qSP9%Ykt6yItg3|VVaZ#KymU|m{#@Sy#H<`WCb'
    'tBn7A5>4a}$RUSC2tM$W`54!RboJDWZ$rIc&tSHa2>x4e=`h$i0!k2099BG-)dve6fCr--4eqnhqKy1z;3sh&#mlhPjgE}w9J7V-2Y6si9LLBnu`^g@qlLpw'
    'G3Xk&N%Jt!SDBne${E?eu8J17ja8`4y@zP-%^+Ma#8v?`rC>mCuF$G8oMd5+jZ$W5#E6MdMzc^zry`jN2st9$h%M@<*AybvvN$g5skUllcY>y1R|pEmVH(&d'
    'vRoU7ptvP?yW|}dKP2l|Bw!dBDjb3e2o+-El5C_-s#xHGw^)R6pr?@`7ODV~tcX9tqR<k<2QbS#4d>xNi<1<Dmubla*5^mCjGV}VF)qAVyRb`nt;obmTe>!?'
    'vWh{tWF`euqe<jAG;$KLNmiF1aY-^1WG9(Z(vlkY;<b+PaxXW2llwsa3oDN^uxo?quo1*^eY<QG6#@VmhFTch!rD9tybCW%?<3sN(7)=Acpv3c;kuxl{5~lh'
    'SkOWuE=j58gb}-Yl@p4!8_cT8?~xOD6gmGR8h6e!dwK*zvj*ktGFVB6c{B`%kAR8Fz;IR!ePaz$57&D{(gmJQ(lkkReb-N52aCOwB+)?YjIwMA!UI}N3|5hs'
    '#HT#8WTcQW$<kl@GZpI)N4rhE#Z;h(zM3DtXdM;lc)=aG;$S4~Nm@+B;Sd_K<UR%^5~+f<15n32(~S);1hGtrj2N@gOH;Bj4~H=E$a9oCjST{f3xH=lv)a<}'
    'X;Z-HSLlxTe55QexI2K&ei;I5XtQH4Kz4T-NaN@C0ghOSt>-&isR42+PnAitoWmZ56At|~A7!~ST%_TOV>llA%amt%iF`keV9&V%KiF7r{6JJz!q4S&BN*<G'
    'hyKQqrtwUIFbwDq#wjFY^-d{^_yGb8`K-ULBlv42!uY`;mKkyjzbt;(DpP+A5|qNNgdM&m=nN?Z=A-M;cVRH!1q-8r?bN*r1Gq@BFxww9&tTZ_p<%Gt_@g;M'
    'slrIu68C3O21yyl(G08~fabt4jJgrh%<5p^ubIHw$GIVyhc8P$S&lJK8AOeVYcMZ%4MrzexgPoWIChAkH_dW7;Yv!3ARf_m#zk-*exe3>tTFtH3mM`NFk&(B'
    'S>x0GUtpF@KVzTRUxgRLjuT@jTt&H58~Wb}oKhDy>Ea5nD?SX%R&JLKl+Oe;hY3n=$wElPem0+mS?>AYIS5z4g?$pRVxSQx$iX66=o`|$Q>Gd@4J10i51Q)E'
    '5X6;u?w%(ThzlllrdGYegg!j<VGB%?C=l^0Nh5fM>|UlB4T^A(3PChq&O~Tehl^9aX$-$|9lu%eVGIGg9`XFOut!wJV9SccR$($}_6>70dTq6DVWwzfcj9v&'
    'Qa5K91iU;ID$NH$)sl$)eI5kBJqqtDqjM~3OrD!zC<_9)79~@C%Y;T<&hOqdheEFW-C<{_WXqBMR}hcMT6>VN56{86z}O)ONDQM4Mas^=E>RUJC}WXi5hZ^)'
    '>=U4x41zwUE``0mv!phxXX>cz*B*<;EFyQsbyfEp67cyb@*D=AWBT-8CCqo0kfbF<X}u`Rx}Yr1-_eEv1G(O0@FOu~iYC*mG;(D2N}HgHd(IF}oTF16lk<j1'
    'OY5SfR9BL6YE$D5HI=9GDPm1kfc=7r^H=)3q$Yj7rzU+qh7h*Ef00|Knh0%V%jZ=C&R_(wxS#-cj@Gk~=d6lDOX_g`*ymK>;ni9|mZ5|5qRx<I^)m_daaB?n'
    'd{Gt~85^k)p;0Yi@bwv%OiqNimWz==w3_>JDOlWnhLa@8$-rYaCCH)BM+|n3Yp;j<^AQ=B3imizJYu-7#@1~cilKzm{O^TyS)3VuDW&IV&*FbMI#}`g8p(lR'
    '{lSU_D~KkX3<10F`4Ieuq=&9TKole3<{&yu6YqE>`6Xv^hB2F0#m|a%H4lyfYtG_1SE^vxn6tTPK(8^p<#D_>pEu(9UOZR6eOq<ynaSxSOG=6jL@plZ28=Qe'
    'Z-+Chf`rhxQ5_?Yl<UDdg{90)gBCkyGs}Qo3DN5=lQXlC10EnKty}-S*5502jzF5uuN1!(^KU*9{F{eU8E4p3S*z3pc!A-l0?b77r%4*<OSY<d&=DzS$(F|O'
    't!#pM98+_J%^;lR9zWVYZdiM7i@=M(s)A%;=m?kj_6<K0CCg*^cq|_EqrKzC+r777ZaBW=Z0x0({;kT^I7;)WblC^?V3b1s<_u?1{Jq@Q|LGy{n>YXxk#a*N'
    '*?fcO$G$;WH1Gsg%`g{U%0(7hr33jhs3;RXfMN`jWnN<pSC@iCL1^2^Bt*&ugJ90zcr*|#j$fkb3?nXD^?_2<QGNCIOs-!Z5ovksd${H^Z$1t@?Qx(t9x-cp'
    '#NzfNn6R-Wx#5yoM&EbOPaYoU<1N)D*{ch^jYupIMjX~qP2-Px=eX<~V@3{h!zrLnah#+v-yEfE5If)S`)525{C)tMP}&W^;dC6&6%iKBf-vQZH-^DYoZuNv'
    '$Eiw>lpsuno&ww(?ABY9osE0L*botFZ0vCFnQH()0=5{lAFx(5`E!HO_upkj98YanexW#198}QWE{%Qs`eHQj>ph)nRq=B%mPa(`H4Equ1-%4ltr$af0dTtv'
    'v*BdEfHP~HXNUe0k~%ukd;YY{^?=8kue#+B{Tmyj^)sUAiZf5etTz1ti30^RR2sKofkM`&I-p>g7#^@d3^L96PlBPwcAcl8KSe(bI3B6D`IYS7Qe99ZPa!~t'
    '&$}y;q_U(fbd<&Glnx?`#&2A|D;^9|!)9E0LyLNWoV1^u&QXzAw>ne3ykH+iOc5v)VKUrcUa%R0?^ihuAq<qvI-8|ZFVDRw#)9|)7=}mf4HxRs#$kRBCpZmt'
    'L5n13(pHhDy*<6eYUXSi;7EavJZ!|7*(|w-wQSUtYN7RMqu}~lwM3KWGUr0*a$10wXVakq-Z|S+RniDnb*k1kz!J~X@W&56sz9A>X87X=35d{0O1qA#%OKe;'
    '{4e>BA9Ubu8rzLi6p19)OXp?FT-9d6kI~BEOW<3rboDHDf%A===MlBa{;ycCB0ldIB3a^{1#(9B7C5D12U3tF)w^I>&qot;^+FJWHskMR*e^nrs-2R(GjtjW'
    'fTqES`X;^2$o;z(EWKH!oITKhbR}S>bRU9UOqMsP;4SOiL0QK}I&Q6`TPrB9jLIpzQc*4HmbKeBT4(IRNgwaY4sPL?yo-;!kj2D{WiD=Fic2VV&Cl2g|HMxD'
    'U+kD$d!LxdNg;~RUctmh!o)V?Fib;5-&fiBRrY?xZd^6(6E5yqoHi~dOAoYDindW4i-i{Pq7S>v)3U)-v7e7d@|wKN`xYWnEJR^~l~+tfi(q-i#W9fy@jj1?'
    '1b1M~-gp-BOSX(<^9#!$*kY0VJ+0Z5@UNHRu|WL#MfOYdukYD8?&BP`_P?p|V@weDHcaMWp04@Eu6fP?Rcw|t;zh*2Ay;6fwSb|@P1#i?88?S<-ZTtSk93Un'
    '6gbg%>32wQc2B+?9bdWc&p&_smwR>b<-|QbIlB6CadPQ?{(9zqI=Z}cPrrQp=zcmmet&fK;rP-$2iUHGFMNRKyDl1%>%w8gb?2}lxb7}`J{lUwmrV|4i5KX}'
    '0;_s!NT<`=)d*`*!<1KUfnkKa4N*vVDMI6e<$R&1tWLpl*zP@;FS>&ZIc!GT9?L>-Uc5EVxW3EaXRu4I02UZSvZ}~s`p@r!v|gbT4#9S>;r9f7PvQ3%e&uP5'
    'iL(~lts64{gz-W{nJF}da3KxB*>~8^#mVvK>yr!j?M1ia9-AG@J-zsRcJ<-p;@7Y5-0a}b30+iY$ujlBMiS4~;MaaacZSG664j6>#Lr|FHt4>LBFZGiG(1cX'
    'ZsH4kg&~ElzW(ZvxK3L{aU2HP<@=)p?f9G~*X#q+K4`-+GnhqV4QD-2{1mSh$=8R(OGTiYfASs?hEk*~QO@B}_Eb1jy<{mjv9MBLli%#LTVc!ZO{__0Vvbww'
    'e!D$sS>sOI?D;LvZ1*}rzvaWf-lP>wLfZ>_osK_gk1cCrd%oAfWsoK=K4a}{)adowOfxO`XjpBBX#i<=00MwcpPoDY7Is=qrdeH+K&@VnX?DMl@UBgub`wT5'
    '>^6+EdmRGVJs8qxnHJMpwxDITEd;dyx7BSD$V9AG2jRA92`tk_tab~rdV&dLu+=pYA||x4-RdC=eZiGQw7W>VL!(Tyix3>!vIV3~kT!7MvWO+%A0ar_?h$3%'
    'CP)*PXm<(HM~IEH+f8E8?)Fgtw0=Tqkp%4)pjf@WfB^eF;?E?(!h(re09kF4P`gQD?;xZpAZ80?k4##`Oxw1oZ6R1d+P0j!MUNfSj@bfALNHdB*h2AGeL}Gi'
    'K%59+wh-B*b%VuVf_7}SJO6JH|5q(yL*GhNpa&e+GKB>|OgR4h=^Sh48uAQXAQGmb+JO>q4sh(liEUvIxFB36l0$~<4$2I*P>}p`1vZ7lNCZfjlnexfOrVE!'
    ')s_I5$fRYU2s%P%I2pAp)k!T9v)MrwNN+7Qf?BjtVvKr`wU$-1gkF)=X3^>hVO3jgyAaO#(baoCvPdSh_O@7W3qTgK*r&BgXZp1$l^n@~5Chw`lqcFz6WNB}'
    'F0ra;7P9P0S(+Uw%bt{FUy72RJ4&{FoQ;Mw6^L3wlr%4ityzfDuC+QUir7MI?LutrLa1HTylS<GUdyhw+GY`H3Q-FAw4^XvV$m&xqOo;or7-5`^5l~L#C^ET'
    'Bv8Os)BV%F*%|11tJh~YJ6$Ur_raiHw+qZpC-gnb^PA0f-}l3AzuTSk`V)u-5L)b>IS%ZgGwE0p=x&>xW@qBv>=;Z37io5Zm=*M_X1nX#&88W&CcbS2zU6!E'
    'z_V@NZufe@q-V7PuQvvQVaIQWo;~q{Nx#!H`+hS7Vg{@5j1l(a{NvH_Nx^g%=K;!Ir|J1Y05b)!y~F3YIT_oY)eBn?CSfWoXj%{&td800_B~)^((YIm^oPx+'
    'U>X8p8;FJ0r04l|Fb*b@UZ-nLg0N@xeY0tK5E<>D1zh&}olXxDhIX^>*?xcA?~GxzX$Bp?hfF`+#P3c%o?LzSeCA$$`14HU#bkL9tGhjB^%&Tk#lRTkMO*Q0'
    'GOz})%n}jMwjo*!%n&-Oh!zcgMiCM13St)!yW0@KOu+|UNwNJ}#LjCGyRQ{b@3n~i*G_F#Rnq~?&Nj?8Vw$g}`D*2u_Ny^ptsb-eYGZq~g3PLh`e2u4bDLrI'
    '5ViMeqWxDJ`>XxOdbN_Qs**suFjH$QF3x4yuV&!Yda_=vC#&;n%&MMnO<R{lE2^pqK->7V;KPxx;ZHri{No0Bj5`1*WM9y6FbyAq=r+u9UB0lLhBG*XQ{CR@'
    '<$KttEFInKsDtm#4xa0;t1oJwvRb7Iv5WULcN}MUVez^5pyN%cz8c**4Ik^VdwbUA8#i{9%(XF;te@&gl4>hJZ`5?)>DF5yCx;i7<b4^tzL$km0i*Y&S+dNH'
    'qDt}eW~cJLIc!K~v)P0#1kvG%M&0btyURNR{CXNjV_qpHAeCQLB5rmV{U6|_auCLT5`?-j)T8W?MN`<cQfQ=8gVX*#!U>BzEG&sccuNDwR4GQ)3BYuy!#WOW'
    'S^GCT2gni4aGyqb=#JNUm?3Jt(lShHyr=&G;}zBt<Rq=ICIB0(;eP-5;%YmG$+*yFD*sZ)i((wlt7(oZn26lrUqA*Gh*(%UKy<oWJ(zzFq7-YmSRE5f3Ll~@'
    'ca!h*WDKVZF~oHz(JXXbU?<9_RL6o9*XtuNjan|QZn`)~Lobk=<I4a=NdlNjd0}cVBxtOtIFJb{(xY_r;FN_-u;FWx`w4xX(&sVy3+E#^`Sl<=^chfcNbKkV'
    'qDloQfMHUYExNF7B|1bLC_3tutgR@boGH6Xu&Q&44hV|XA)@3dy6}hrX|YrO4MxRV4gA9;HSBK*<oNE=EmwF&*;9CT@#+Ug9aRIRQH7+5BK0q;JzuVh4y-(t'
    'J(z-HBnW32-;(W#!sN|PqX8J9c&BiOZqa2alCC*!6LpEX<*usGxw=jdq(A<fz%v1*<51wr{TV%x704)5kQ@ynXTN-k_RWFwWDK+D7B8y<VMz`(PE_MmH43Al'
    'Cut|ter6g}%nz!{D<Dd92Iws*u2z79@+G{NtT6cZR#@Xx-B;<-#&N4NSyR06qD%u+@q!{{8Mx}3M;||0eZV^V^W%xDMqRq1D2|102mt8WaA?`$+#4quR#cBR'
    'yc@v(z`@l%4x^-7;rN$*T=Z^tbJ6$jJYCU$?(Cvx)8FARS{qn*`8I<yamD2Y(sQpD@J+`rvHyYZ%R0jr-xt+_ZN4v$-<Z*a`1Zifj;Pwxc2`=+hqJ4bi&Io_'
    'u>)1Dg9#^vK|tWz1uPd7IjDzeRw{3xOjl`apwhGFYN~WW{^d~*3I=-c?n~xmaJH_>V^BmwCgm_t5s<0%4~obKAaQ?zsm-W-z&XpbZm^N%;d-L@7B){66kYIl'
    'h+@kW&0w&_{hmlr?ap&SRn2|7pk7`)jM=h&X$_V23oEFuUuwU$eqnkqi9qyLr0|4qAo#Ux3N7hB$pkT3+M4VfpIlshIQ?*ZbakS#r&{vlkMS=wFsk9yqtb>Q'
    '1qZPM4VabQSRWe<^BDN9^wain@)2+*v&72_!>XcCsM|y#@f#cWfROIVi$GW>rE-;fzvs7n@^6=ao$B4hJ5T=$5LL6*'
)
MANIFEST={'exact_hpoly.py': (8946, '54e4c8f2f6f1b45955f42b6518c4a1586d94cccc8f4dfe3ae866cf5b22f3aca6'), 'RECOVER_BR76_C162_FRONTIER.py': (6682, '175255a14b8c4e7dd62983b27bed645d6d2b69c8c794e7a5f8ac8643a52449e4')}
def sha(b):return hashlib.sha256(b).hexdigest()
def main(out='BR76_C162_FRONTIER_BUNDLE'):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    data=json.loads(zlib.decompress(base64.b85decode(PAYLOAD)).decode())
    assert set(data)==set(MANIFEST)
    for n,t in data.items():
        b=t.encode();size,h=MANIFEST[n];assert len(b)==size and sha(b)==h;(out/n).write_bytes(b)
    subprocess.check_call([sys.executable,'-B','-S','RECOVER_BR76_C162_FRONTIER.py','EXACT_OUT'],cwd=out)
    print('BR76_C162_FRONTIER_BUNDLE_SOURCE_ONLY_PASS2')
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'BR76_C162_FRONTIER_BUNDLE')
```

## Evidence tier / limits

C162 and the preserved C156 control use one exhaustive exact rational H-polytope maximal-complex/mechanics implementation with exact mass identities; replay is not a second independent auditor. Endpoint claims are exact; search campaigns are finite nomination evidence only. No global minimum, affine/projective exclusion, support-family exclusion, convergence or path-existence claim is made. Canonical accepted own110 remains C622.
