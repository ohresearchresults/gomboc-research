"""NOVA54_MP45_WHOLE_GRAPH_ACTUAL_MOMENTS_V4, exact E8 successor patch.
Input: the literal E8 recover_mp45_root3.py (41454 bytes, pin below), OR
research-journal(7).md (3486698 bytes, pin below) containing immutable E8.
Save as patch_mp45_root0.py, UTF-8/LF/final LF, in an empty directory.
python -S patch_mp45_root0.py PARENT_SOURCE_OR_JOURNAL          # build + checks
python -S patch_mp45_root0.py PARENT_SOURCE_OR_JOURNAL extract  # sources only
python -S patch_mp45_root0.py PARENT_SOURCE_OR_JOURNAL check    # frozen checks
Numerical replay: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Linux x86_64,
glibc2.41, OpenBLAS0.3.30, SkylakeX, ONE thread set before startup, four fork workers.
No random input. All six new source/input units are encoded below.
Seven unchanged helpers come from the authenticated, literal E8 source checkpoint.
No old multimillion-tree plan or C32 transport is an input or an output.
"""
from pathlib import Path
import base64,zlib,json,hashlib,subprocess,sys,os
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
old=Path(sys.argv[1]).read_bytes()
source_pin=[41454,'a9e3efea31bb10acbaa769ed2aa9603ba51417b6e4a6700af28da8df1052dc7b']
if pin(old)!=source_pin:
 assert pin(old)==[3486698,'3fb11318fc0cab6a8742f00ff0af47b04490fef13d97ae4df84feb9a5fdad48d']
 s=old.decode('utf-8');a=s.index('## Parent asg_E8jhRERA9v_K8-YHafCvHQXS')
 a=s.index('# NOVA54_MP45_ROOT3_WHOLE_DOMAIN_V3',a);body=s[a:].rstrip()+'\n'
 e=json.dumps(dict(version=2,result_markdown=body),ensure_ascii=False,separators=(',',':')).encode()
 assert pin(e)==[68993,'a8dc9aab660b5e9b5a6b4db109797d548b9562b9dac14a8ca2fa04f55e999eee']
 a=body.index(chr(34)*3+'NOVA54_MP45_ROOT3_WHOLE_DOMAIN_V3: complete source-only recovery.')
 e=body.index('\n```',a);old=(body[a:e]+'\n').encode()
assert pin(old)==source_pin
s=old.decode();b=''.join(s.split("B=r'''",1)[1].split("'''",1)[0].split()).encode()
assert pin(b)==[38698,'4e58d9936af4d3e1afff389806b2fdec3f482dbdbd7ec8353c440a6a71989a63']
raw=zlib.decompress(base64.b85decode(b))
assert pin(raw)==[101132,'18ee40d76bb29a630350dc639999008553fefe1ecad361b01293d6606340b5e6']
parent=json.loads(raw)
names=['nova54_recovery/comb.py','nova54_recovery/locator.py','nova54_recovery/exact_check.py',
 'quad_recovery/engine.py','quad_recovery/build_universal.py','quad_recovery/verify_universal.py','omission.py']
S={n:parent[n]for n in names}
B=r'''
c-qx{YjfK;vgr5oD>&KOqG;1zz905-s~lTNJQLfAC1*BAR&hZRvYAMfhNPU=$$!7y07#LPY-Td&emIrHCW%I)(dZW*jeL7XKd)$9
(nLG_P%N`&N6)_9K3gu*qDYq+`*i#4XkzKMrrthtv^b)UWziX#5i_Q-;m11BiSOyINoKL`ISJKl$0WMvdWlcs*fI2(?NQ(NG&{b1
HU%uJ`!7Wrlere=bhXUOx)sxQeJGz%)ASNew@oLuqS*CxJMs+8)HHi$6VLY}D5k!nQGe!=n9{^>9V0Pq-HaXAjYKPRk`>yf2d;0x
*Vv~7P*{ZOu50^Atm!k&GIZ+BlE{xD-Li<`%#6r$jbxU1vjp&(#J3&8up`6gxc^v_1c;B94>bSsk9C&9?}E$?&#v3k4bRsN6M#*k
X_4dlvF}@kZ6`EJOagqg6Vos?=&O_H)bNeSk7u4|Yi<(ji4i;cEcPwSclw$P;VGQ~L(BGvxjqh==D4v(sN;LKOK40D$Bbh_BRkSz
q^Olxnx6RDOgCqC;!)})jzvw+a!uO<-ijg1m&;NMW15$|C0cA6vV6<;00u}gA~Pl$F?0*6S|)*B*p_c3hVIV{suM>`=*)|46eBw#
z*y5IiRJl(IBv5gnynW!Z}-S_O~ZEpBr>R>S#d<7*ou?LfPqiU$cVj}o9KoEEOQdWGIhuF6Eh)>0b{Efo*BiyX+W)JLmde;02upX
5lshn*?Q!9zUjq;P%8pfX@)h6Tx$A;;~TD>7&LMn({XIuN^IS?>>2QsXecJ%Z?k7AYS(<3Q|)l|1yt*n{TY+|j)KNXj09=E1com2
L+O&<L60A(M9PvbR%IcPoJ!fUl+tWQNs&hBJT1RS@tmZK;*cY|&C&&SL0T5K*=(6h9|2k#$X9QMm(O3HjKa&Ci*WqvdU$d+l2!TY
;!Wqv#c!`$UzDR|aY(a=G+$<ukJCWbWk8%S7t)H9_wzK8M1ybOwQjxmQmDv8b+Mk8=_+5w6f8(~cbh@UA=W%hvjXI2ps8}Ud?2<}
OS7!hXyWA}Qt4+BmtlNQ<Bt+4q|@8%EI{0c^Cd}&0k%7kcgu;a9Oe`hCHev)I#873m%-UYzRSt#UY_1&w;9Nv^l6!Y9OTPS%F%6B
bw&&Veo$8d6i(z6fIrJqmA$NBD6&$X9#>-%OaPz6j7%_@$jdxQGXi~4C)#v6-S2!-$#jZ?LvV0%lHJjPuKEgtEA9bz(g*dhoI_V-
b)FXGfS37-GF2yX{3V`m7a(;^98|*4F-oz+Qkj2Yza`**Pzm3He57nZ@?`K*)zp=W6;)5YTxL{Z;F)?KoF1}ap~(PX)t3`_28v!5
@|1%t*JY5TaXHxA1FoqYUx1(sQsybhM3AWkn0}In(Cy$}MY4hkZ)>X7%&i_c+UAIJoW(!>&MlDq_f$Fjl&2*XV~!F8;u|j$AQI?N
IEq!CX5~P>zPcJ~;ft%A%QIO`c^@-%HeVO_!8l)wp60Y%=Na|}U+L$Vu1e{oK=B1Z8|FEVQ6W*z#){TMvRctB8Svf|Wj>$^<4cDt
J3IME7uVUxZ22ks6J2d}^yc!n%d6inv8(MqHhT!lH<Q9JBMTaaK_G|Wf}~j(%168D0v%g?Oj79HXArq?`LV|ODJ}1%jsZ9XQy0d|
tfZfTERe{LQ2)(xIUiUG@NflBjE%sVB49F%pAORnSq)H8RnXs(<_l1zIfz-8SKPj~48Wr-!X~zPG(Ne0IUEnq!q-=)C*!N@@WuJ%
`RLUU1Y}M#UP&$13uuw`Uq;<zs+BV}W#ujIg4wS_oTlAB2ZMqV0)|8a{z23wF}3)Nnz+nBV%9NsL?T%tfeBob`2kmZ2^p9#=V0`+
Q3=H)Pb4tKIhYq|na#hT^8n`4Tw(?ho32b6IFMX;nmd}Iv4r=u5QdK?fO33KrCItJM1mF)x4S7)nU*OnROW#eG`=Sp!`pO4%b7$$
pH~#D3Z+P1<&_@y7_0<_C@*24D>|6vhcU+f7XoIM6UL7k=7sox%J*X1_1u#JTT|oZd`@G5>3_rhych-LdNrp5{u4zL1V{y8LNO>%
3}j8WB+bwz%`_y<G9}%xCEd0ph)yKaawXG&->xHBwkKJhE7^`GIj$!k7AxT70Oj%m9Eq*!ssUDAS1nbC-v+!p)7o_v>u5mKNI4P;
JXs$+Fj-uy4@kz>bj8Z296ZjKMbWN6CWCZeSN?8J_ab~W@bQ4ukNhhGK)mV36`2**WLdUwqH?VFcG97U8kE&g<GK#V!Rf>A0+5UQ
;GJ4B=gjJ;NicagNjKz_)8h&Y;6;{1DnT8M266R}z=Kk8O~^J_18`R<nKRt)7`F}ezyUVfs?8sa>Oli1sNp~u;z3jKQGoC|hFaBS
LnMJ6t(ph|otZUk#oGJKc=H*Fe_;J!OnNsxeh1M)Fwu4O0REaLBBApZ8sq5Q#GFoyX>i~`>0Q2DuZrN?_hV4&1)1Zc@bn*43>2j*
B%*^CBi2zV3pk&VFYhMhM4wJo{0)H$XBNH~jgQJPVa`s<ehCC45YGe9Gr@t&SgnT*e6vfU>VkY8Km{cTG-l7hfV201YKUqk6e?wu
r(9?@lp`Q;;Q=Zu$Gppj1ubDL33!*mOr1=X%H4iYDppKp(;!2sna_Dx5<s1SBG|*2)3h>mu%wzl%O|V_bY?-trXw`eX||?6%rAjr
!=8UuoNM8#`*cW>WbnhxLkh)!Y`DVM!ns;8r=jM)a#YpGz6?;q_Oe3x1%?p;vto;llMVY3Vuk=5J9dm=o=t(r*cP}rn6BSZF*L_4
b``NSs|=PLD-_H%2_g@{Su8M`XQM=ehJ8OgU9KUt$Om9d%E{m(H(ZRr9}o{<tHyrvVl?@{<7)`e+AI@MVg&A;=D~!SE*6NZ5d*}I
&<VUv|3xPehUsifIGZp^;59+m@nxnk2R@$<c%1`Y2TX$0Kq{&rA_&9omJloPC{Yv~H_%rAbptGp4<;xzGldcJ={}v)8WRZG0f_G}
0SX)sQ_D(WIxww<O68x87DNFKRjF{X;RRdW5Rq^#X#*7drZz>WHKf*~SiCCgMtGEeaS@A|#4uwjCcl*{!Cq7X)X)PVEF6l%ak;8`
Tq@iugk1E#wX2md%WVn|S5IaxUW}xAN?kd@?;DlcNOMqQKNx%)7$EK6+s**YdO@Xc5Ple)B7+w(ePHUyXO!KpDf?xcFhD{Cf50Pl
rj0%mikQy9K?oe*O0Ho{Ke3UGRh-Sfx1@m8g8_F;K#~Bzj!0At8oqf$2m@`fWKv4)GG-rv%4AYbK?MdAWPxg`wldwtAuQGrpi?Zk
G?}(7+J-2>qJIfH)#AmYY(r#c0md&#-i9B*9nc%)_<1m?3it2<!w?YLO(ddh)#)_Of+p!bivrH}ME!&30!bTi%MfE#6xSn0#rvI&
Z=-0B%df2dq<}6!<vsR0n(j9c?y=ud7jd+OxUZ?jasiWurZul+?Wk!^w%9!bSv!*|qq*TYr@0NcHN4!hRE^h@@Xf&e%F&1(R+xUI
iyc{e8w8>i7-)oki_qc|v-!+hUI3N8%er#`fbe(k0%8gHd%)iH>E50J0`CL%m%*etwgAWog(3M+5!@nai|UQ5tA%E#7}aYKwMtbF
YEC}k5^~9wXWprN;u%5|0(0<rC}IX~P*t>e!ioyBQrkd9<%>%xv<jeMx$NSYWVi<KK?JL_whQJBVBo^t%|C^^X)5oOHBqFWL$3D0
Sw(G3aekb_Oaa$jUciI^)J@s2>-khg5Sr5@jF)_6uB0JftC*+Y^Z}k>Ur=1A3NBzuPhb|vEa=llt)c<xTA;W<g_eA?DxCIpmcr*n
Sm1;|2}_y*8$-c_W!{jl#wraPw<Ji^_rZJhW$;o3=BvL3zp6N>xb9QUbNHeHF3qt}X@x6qjit-4{QWCDeoV83zu^;nC{{G)A5dN4
!wHK6@H2Btv!8THYRJMlK*Nj~Tj~t3&0m7e0_m|BPW+DUzFzDUYnv=iWTinMKJnQW$H$DzPG84$z2WG<&&^Wk3a<a~FCAAlZPc3{
r&$3})&SQ))v^mIB6pzY2yxC*jP3Us4|6)_!Ew#VS*ozPT|tioQX(*tt|rVHG|jM;EN3XXm|2j|mxq{dJUP&hi<0DJ;P0IrgAoka
+rGDlwXxNPJ;P65!B7F%zGd%a`ThXvZ+Oa4YDzVA`#NFBjsSj&P8KlzwlVY#la%E=On(bp2FvHO@~~x&j!9Xy8&%O{dji5jy^du|
RVa9icJjkCc#HNiod#bg1T6f(U^9&%_`u25A(|=o10B))R(XWC)m&$-GTyg%&bY(n=pM!r#iQX0x2&mj#{&Zx^JqF*Pxrn~{Jm(O
uTeCZaiZ*~-{CP<B}edY-)E@r!F)u3bAzfg?$ge=Pbw-7-~l4~R$WfUfxgu&>mvz*NI4Ks2(_ysn{<@~cwGz25&QTDi=3bcJyw@W
PSUn;C|qSk(7UNW*zUzHYLu>oR<d>n;;;vU2ZFJG2S3<z$^)JIz2CXqAi{g~_iBaezEFQtlzn6GkG%m0uP`tH0C`dbnjdwu64)T2
Dxi1kqv~m}-WQx~Oxcly%`T4$Avc$ApgJ)29*)_|3Vuuv0(@hS@DJV))0dRa6RA|+Le0tp;L81g339cbi-w7>ex=Ixg5EJ(c7J4Z
ZEL%?ySv6*6fT@ThM}>$y0tUcFhpz(9U>yrLLX5A+#(Q*xrZ>=hV2ZL<7^RV$JM&}c5y9w;9F_dTKTEh>G?(jI=V@<m|w3~arp(R
<!QBK)$*PJR;pf@o^I1nqzN({*Mg?C*{cR(dK}G{@kg=Aae64W!K#fhwxRZ71dK@pNW+`AxW&<krGNw<fU*jWTnpKNONOHUQOR0T
sG@Fbx(;FOAIDJ?oE}Edy%eVGZ|nBpGkl*XbNqIHxLzeJR%`C6Ox~(dglmS`LYQ2!k^`DoR83b*P#KFv`w~V=!E7SKFhIO?{1TsE
!jN<V7Y>Z*z@zL3Sc}cZgfrNCxl!)4JMC-ftkS@wH!*>>?G0XX-8*<$tDW+svNo4UaC(5oluu&BLWWo&;ax`HN_uzmG2d)Cvnq{s
*!#nK`Z-A<$_A-s<GtBL<^17V(~DS$jM_rDS;%Y{aPD~cKy3wwonY&+xUdoZNsq>f-}$I~q+eQ_ERpi41LPF|3Dn``P1SELn|8|B
q7l?mYB7z#{p@N(Na!XS6ap;1H|Mesd$kC&PHyCdu}Q@y6r8!Xt5#FpMs<8D*i$v_eH7Otv*2FzzgFn0>F}RuVSDnqi6_B22i)3E
gzev0B-9BZpKUP~@RckxkdRwbxix7OyOCc4`SR-BiEV{^>-PNeZ1`pfKQ71N#mV^k{NLfp<yrXV)%(%;>B(#OHX4N|H)rSL@SQG;
;|K-%nZ|j91)o&zpdr{MTCG$#tVrrqsa3pLso{$!GIUCwZpjs&?~zZz)~5b3cc?oL&2@IWq5jtPc9TbE=hws2npN<8bvYVe-<*!m
uP(zkz${rs-T+J5rv+LFPfo`-z}vIoczAtret80TPhP(cUz}Vr=D)asm(%yBuZQ7ycsaVd4$rae^YQs`B-(fa`OD$u&H3dpJiU5x
a(WKUXohKr|2@3E3QvcC7^oeF!?Tye&@iC`7gz6wXFr2ghw2RL%aa>Gwn3{IKZ3TBFb#m;TwRZ4b&rkP3ZgF@gm$gR4_NSUjh`6U
99MjH^lUQGEe((FRdeLqXSf4tOjVEn#+^w^Gy5R)UI;_)gRrbV2)h@D<Mlzfb`OMOXuS|dFNEI*VfMCS>Aet6FGMdLHgb&5ba=Tf
%57fm=ueirW*^60t4}suyN^oO=^HiI?Hd!<>xby=i*I(g(Jgm-FnDfX8=luU?w<ejnE9ICQ{G3VuUk*{(>J$AOcxM3hp>!32uJIK
aC;%VKFRU@o>4b6UF(A|dLc~fX-WaY>4WIAe*oe1LD*VfE4JAO;plx3ZZAJvvk#(A$_>3wf&jwpgXpsg0MVlh1`K~sE5Ot~2(yn4
2tWEDY_G2s$M1va<%i*!y%4>0_&u_2>aN!Z;h~K2<wsG@wsS2!1f{xoh}WyWvUgr4>bf24)y3`oG;UMx>ziqGt*<M}T~=<{&QG^)
F;Dq;&m712Y1|I;u|HYY?a=_!@ysVFckQ32+}(;%I=FkK&GoFGZQZt+xBc0=f1zC#g+AJA+ctabmZLK}{wM~AThE`O&as^yKLdfM
{gj@#p4MZl0K)2n(Dh!3zE*ro>xJmC-Ja%Yy%0Ti*E39~7sBs@uzDfv9)IY0PB%8RM7br(-KWbv<Ee7r(0^JdpsxGVb#1L@6n$H_
dLe$=w(FYfxPPIttNn$_p7)d?006(og6a^@^-U@?uXkn*THy79Sp6V7rWP$BLlCnc#P4m$b^1ZPo`wwF{Q0qi%I42kwshm?D?6_B
S1P-Ip|ZCvYo@4R3J|~RUD^Pay~9|x$HlTOy$6S7_TsRu9vn_DfcsP<Q@*N~FCS<|vbdcAdbPrB1~Qjeu8Bm}<vp$@^Aui8s!11%
bxEQ*m4+VMQ%XzROS`AI+M7tla-GK%PZO1xb90`p*5#3u(}I#bzCZW?#ejX_Du;_il}yWX9N&}JBC#rsUY!`WBSmz+{KS%f(n1n7
FfR!AWk?2%0Zyr0N<dm8si>2ww9G{pc!CjhcRBl^B%sG~cfR6}h!oVZsy%I7RBa@%uq{wU?QFhAN^3{!Hp8`awsMXMKqS9=nCR2?
7W8c<_AaVb+aQ<-R;jW%i*y}kB(qqHN#qdEwTzjj&1M>zS#G3Rmaom|Og9tXCDcl0o;9P9PwZKO3C#)aUlajgJxnOB<qza_IXm!V
<(LG;A={1{$bb7Aa0B-^B~sjlL+``=_3-+{e+Yl`4&J{av(txHZ~r~Q{G?_jN$i1Kys>Py5n_hFzq)!o49~7EPR=jGcc!co<v3a<
UxH#nj;4n>3|P7vDEsp5Z6@DlG>iF;eX?GxiUHeV!E|yM(ZEnajMnoqT#)=@viy_<h)7XsR;+Uxk|Ivi;02i%R4wR=uw!dQFpyRF
b0jN@*t@9v+u|~mA(tJ`_f1tMUK0BRxa(+<P5sCwPGlvKuKBL-Cbs28n06oe35j)!crh_%M6+f#!1_L=6nRV-d4f0beLgTPWzXD~
dwFz(NertwEve9^1I(k7s-&<(q?|U9Bk%t6pZ_r4@*2Sai-E&*$~pUV=XoXUzlA0W`tMVd&L}bU2s%yTh!EHDX<`uKJDM302yApW
a;QZdR|CN_yaaeQ(>2>jVmHG6V_IdvF>gs)6v*=7hb1(PP$JRn_Sy3wmt`3Ymac$K)Sv5b+O*C|tNX)-z0;qFDU8R|#iF*Cz@R#y
9f?VGGMmjz&-XMZGG;)RIkP+?iQtb*W6!kB*s?U@5EqvUiDP0{R^$twAPLX}u)Zu-Ad1C+TZ6;MvqcA4E<l42Q4z_}HPBi^m35C&
OG{iQiVVcBnYNb1jtPR}Ynlg>Fi>8q)0iZtqeq%<_+|of=$IDDBHMl(HBYrvZQN$KjZ*}ZZWiG`_y*7yc`Lv0A61U^&ca5vAp^M0
B)NUp1I_NzjPly;l4zaIld!%EViyRz8{$hBroP_;-lqK80PGfSNV4u#89>Z{;+MAN41&=FzfQaIt`6k$%U8qebIhk5UEN%t4#U$|
CzmfVo0j2$Vdh(C=NA_@<CEv0l0z?ib8?OQlguuJ&)<)SBes{w^n|^$&B}Mf>-XWw&G;4WC!U^+t3A36($VnU@G{&Y;pXyuJQDkm
xGy}u;*GZIUS0`9aXozV`s6($0KUCCAC0fB`F8Tn>+$)^>ytOHLV&<_-rS63zJ161U(>}m4G=dyyr$Sby|}snYDVEZOBKEo<$VdJ
xdi_?<Y56g`}+ljxPT|+(p>mZbkf_2zK7D~QUYfVkL>fs8=q(W|0RdqNVZbzq}}c<517>>-qhv)t)$y=Fu>HkW|XVJXD*R}{G?+B
uvfufcVktcLl;03YKgjxKCm-VQRg@Sd_HdIWOMI7QmUlbdM7%n4~DY~F!;GZO4WQ>a=d94<1vPqrHUSJ&h&5Pzp(^3^3RAJ_*e%M
c0P@4@=q8xh+^@`KLiwjZQ4kkSO-A`5T=_P_yOff6RfPf&nd-w0y1_P(E!iyQOZu3%*je*Nu)d(51VDSisuV#&i%5JtnJfCsro@t
6b{=t59V#1;q(~U8K)L=IiTrHE^H8(;7GL2xqOk^@M5I$v<Qf>p`QU+t1Kfv$m&6eK+hM06&r>49=fzSBe<##QUkf|!{8j89dG_6
_;3{8Pd-em6U}MoJU0|-Q!vg3GL4d1!1689&G~8uAW|3LIh`uU503%~fGC)->|dT=h$k8tK~Y7-L!AW6kv>e1BJdR-I|-7k1kZRv
i|m<WZ60fcQa;zgv5%Dh`G$S?&eIN?C-~~7vAiCh$!Zc+`JL^9x&fZ29`7#O3}#eo;pR#it}%CkP@m&f!9{}~Obpoo5AMKTR73!P
&{&X#MmhEh`?zAqTs_^^ST1ZDd;^306+&y4^3pgW_x(7EIVR>`$I5YxiLS-Y+*jqex*#K%Opn30mmvC^!}+PY>c~`43)QBHmGVmv
#YemujBYX}ukv&s#;kdyE($6^#>2znd=^H?0W`!IBd+mKR0bGCm4s~i8cpmYZ;EOOOgO5juf`Rx<~gni+1&jhPM5MA3em}(HL$FL
7ULo^pRgPTfW1{640P9rsea8tJOG6l0^2~k|0cowI8T~VaU@anU|^SE3O$F}_<Wh&f#{Qz-`tU;1qR*VOYhmuLLjAwXn1+fGx{-R
qSU*I%uI&N4tkPcLN-V4pp4)-F*Lh)ML?iUkE2o~O_TXNst-6<MwSHZ;PKXK4X${pc$<U?-#qx{)K>$QB%NbpwOc=20T<R~D?J`h
yK-@f&{Hb=SgWD(c+RkGa#0Ocp>dV%?Iv?@tWB|61uR{pI=$Rd(<7nVfxya>54a0k5Mbe8r4qs!!;X0V(I;|Ixq+*WI+sC}8QeJO
t<(p|D+&2tDKoal)Y)mJ2}TEfn1t|tZ=P^uCMLL3F%}Fop-4rrDmIc?J*X^#f^G**v2OIF4gj_<2*Mc~zeY{|tGB4J6Phe!dF(DO
mFK2)uG@KaJ%pJ5^5y~}Dm-{N3Yl9CU!Oc5zJ3isJF}1B)%9}>+JU>_bEtU%kERuhGl#Et9?sibYNQGl*RGdMlpwkul%)8$``$0S
nu*;;g&@bwqN$j2rsDBsb+!CNbG4vz7M=tMxM4Uqf2~`?P)JxEaB7US-B)c1&jJBx>z1)c8^&&K-@^s*RwpVE2AOq280B^Ytf%<n
2QKNVBbX8tvS1UC!5w2Fif`>_m~0OkOT*l3tnSkQGsvE@Zu}aA+2ZLGQRt>f55+{_Z!4CWv&mZi-bxkanWA@D5q#4(o(^*dg}Lfh
N9AY$y%<eq3ueN2XsJJX$IACksKZ)ip-yoZu$RNtay96t3;Z-e$b-8&VP4o7bV&t>!-i~;8oYzxCMBK2`<w=K#j>CT3K5fT+?9yQ
c6%~$pGD=FnKUw^maBD=F`!pP+&o*TFkJ<iWOgGc?wW?IN-$vJGs&l00<^KIm8<x!u)A2y>DDD@D8OW$fW1mcNh%8=B0T(5-xIhA
r}*bh2!atH|0WEyytxE$D+Q`?qIWC#>93|;HN=fIBeH=uiBv2SftZ*lBCYBh05KZg<b!NEw?<5kU|6LAh3EkRL)4e4wV>twGI=au
ouj<u4co!RlqK0fBem00o=n-Q`w;|X%kt*Uysfg8#MMkJs*}9xyf17meBA8UEU8Ek8Oze3aob~kq2pE>bH^#58GyGW_{IrPE5cNs
m96r08&&=)fB&Dsw?=vj-XQX5vUK}8k>({Xm`cX3D#2DaDQ-LkJmBfq^;e$igHa_B>1<5(Dqb)HyVDg3-VC4+S{t;I)6`DtlJX~V
mjGXtW|mdrH9?x$6opGvef>kXUN;QEU_va#oer<Z=P%fT;wXH6ay>jBjl$PwRg94>RDTbCFiR$y?HurzcC2@`mSJV(Si~FM^;lf&
x&aL9ZEMhT$?%p<Vbe`D3~mllnrI^CpGrrih3wZ#y{;4sQ;P$!w$qr5GA!sp%U^;qj{4nl2_n0hIqr;cn^?a$vlp>8u2Fb)`*Mxu
Of=<<;O=7cbI_U*Z|oXNuB&dr6)W4w*DH)rw)xt+-1@P!)Me9XFqVv&`Y!qW64=XhL*o;zhS|J2<U>4IvYQrw=;c<nUimp_g;JY5
+TGbs{fo%5i1I?90wNB)L?Ylzm{ozuPkQr;r8{+3tu`JUSFe_fWez^NSg-=-X;to<ijv^Xk6+PtKRsP#%~VrlE{c5pOklz<;WCd>
AcIBxjcE<@u+=NHy*&l07CFRkmER!RxTKWL<J*a7nCiv9z?2+}^<4<KaPyL>H`nY?EVHzgT@0UaTKw0a${MS>T#b29eiq+i@D+G9
3KKDY@xyGBC8<?ek~7ZF`UF52&zBJHg@^=d^D`J~Mn8258qqk6?0nuXZeJPPVj^ZH;f-XIsru=DIj13ujoJk<$(HO&(D2kWn!THF
Y8w;65T>KS?s+MWHZ<OddfLE$Dl}s4qKn>z<B5Q*x}1fZ*j<(Xq%~G6E3*sNlNM;pRn;kG&B=B%2~g!P%2O$DZ1?Qs<uGK+UE!P8
H>1!t_;2)u!?$2iMq=*$MCMy}UtMF#f2UWM<MYd#s~f&=x0P?lcil%nfS6l3hW`2c@N)Qj)e4|(Z5i^tIz))ObSQx1>yyh7XVuPi
0nVjrDv+<m^6mnpFlZbS0kvbZIPpdK7oTX!Yz;xKueXF+Ec)V~A^5@|2!7WyEer(NaU9(0lA3dlptZ!zZ?a)j1dZC_yi2Q8;Ny$8
+}~CA%OC%#i<*D>rsiF@G}l+$v+J6>QzjmSw$_QdS2n9`+QKyV|L4Wb$2&O6M~~ktnLTi`zq$Ti-F1mRUWl)DuF+@TIv444xC+7P
)%9@v{>?CuM<2h;$w&HcxxPuUBzJ23DN#Y(*tX_mAlLS#yP+?u6M4tB{}i|0E3*Q14rNuEw6^(G(buUWa@&~*ELV8xBe~m`Lskrd
(j9<)l5xc0`DnATdx#n{LA9WtY0OWjP4|&zBtF0n6lH=dLQoGMX`Tm->Z9@5)y-H%Hp4%a=}Y6z^=jxhNy#|S$ePaW?0<f?-IxXa
_>8zK$J769wW-%6RdzQ=r#Y2R>y?&TG<g%&^O%lj*!Gd?jyuX5!@m(WaSY|p$$%;!;C~~r`=H6TpPVvj=?e9aNKRW~1W#@*&%v>c
z{lYKgfbd~pE$V&lX3q1`sDh3c=~F1`dc{s_we+F$y1vLJC=iRGWR3hZC>z>eQMDL_Js>&`~TL#^I>R-3+{NN>e!9C!c7>wthOW5
Th&`)U0sWN)Lr&}<kSvKMW7Vy1Tgc>%{Y8>ei>ezk1kHer?2YMInvXP{>Amxe-AIi4ThaQ{qcl%=5=qgXW#$p{{aaP;`s
'''
b=''.join(B.split()).encode('ascii');assert pin(b)==[11093, '128d93032dad8e79c65f408b6927f06134576806ef4156262dc8cb0e063c82b2']
raw=zlib.decompress(base64.b85decode(b));assert pin(raw)==[26745, 'e4cd21e7c6f62f39bdaa4c21b8698a7fb0e901f538a57f84c24e142889e47af5']
new=json.loads(raw);assert len(new)==6 and not set(new)&set(S);S.update(new)
raw=(json.dumps(S,sort_keys=True,separators=(',',':'))+'\n').encode()
assert pin(raw)==[80530,'8a3421f9f44b1a0851fd4f6c116388d7d330bffd4de9bb1fcf7b7505975a1d02']
root=Path('mp45_root0_recovery');root.mkdir(exist_ok=True);manifest={}
for name,text in sorted(S.items()):
 p=Path(name);assert not p.is_absolute() and '..'not in p.parts
 data=text.encode();manifest[name]=pin(data);p=root/p;p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():assert p.read_bytes()==data,('SOURCE_CHANGED',name)
 p.write_bytes(data)
m=(json.dumps(manifest,sort_keys=True,separators=(',',':'))+'\n').encode()
assert pin(m)==[1252,'25a365649e6b00fd696eaef11de7cc3dfbe574d8b0ce1fcfc02b9ec3ef9c87eb']
(root/'source_manifest0.json').write_bytes(m)
print('NOVA54_ROOT0_THIRTEEN_SOURCE_AND_INPUT_FILES_EXTRACTED',*pin(raw),flush=True)
print('SOURCE_MANIFEST0',*pin(m),flush=True)
mode=sys.argv[2]if len(sys.argv)>2 else'build';assert mode in('build','extract','check')
if mode!='extract':
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',OPENBLAS_CORETYPE='SkylakeX')
 args=[sys.executable]+(['-S']if mode=='check'else[])+['root0.py',mode]
 subprocess.run(args,cwd=root,env=env,check=True)
 print('NOVA54_MP45_ROOT0_RECOVERY_ALL_SOURCE_OUTPUT_PINS_AND_EXACT_CHECKS_PASS',flush=True)
