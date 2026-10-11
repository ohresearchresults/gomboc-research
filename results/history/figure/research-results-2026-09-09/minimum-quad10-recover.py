"""NOVA24_C32_QUAD_TEN_WHOLE_TYPES_V1: complete source-only recovery.
Save as recover_quad10.py, UTF-8/LF/finalLF; use an empty directory.
Default: python -S recover_quad10.py
Frozen exact check: python -S recover_quad10.py check
Extraction only: python -S recover_quad10.py extract
Numerical generation: CPython3.13.5, numpy2.3.5, scipy1.17.0,
OpenBLAS0.3.30/SkylakeX, Linuxx86_64, one BLAS thread, four fork workers.
All other parameters and exact inputs are embedded. No random seed.
The decoder and frozen verifiers use only the standard library.
"""
import base64,hashlib,json,os,subprocess,sys,zlib
from pathlib import Path
assert __debug__
B=r"""
c-q~4`*+$%vheTUU%~7>yC4vRho6wnxx^ufcN{zMV<vMHT^)f0mH~k!z>nN~fBRQe{ZQ+H?aa>Jd(JnzF(7qUcUM<eS5;S4fB)Ms
S}f+y$c_EDv3&Sj_ix|me@Bb?a^|o661-mdUY&}S{Q1!Lyda#!r64S=uKm(72t(g1jofe%1|xS?I_k9H*UFtOCTqXJfqe_d5!7C~
tLs@XECuuBB3hL`!_RM__;C|2Li5^<v49z@{AjgU%wlu2n9cmrDp-W^xA61vDJ%QqVXNux?CtKm2ZybZ*XoS-#(QmVc(~Kr+ZlR0
!%nlg>mN1`ywUEi>-q=#-f(BPdDv-=_nSLj`CI7uV;o6kZgjter2+fCTEkc?zA;`zB_BsNx5~aZ@#C`nqvv`z%!;9pzE}BvQ&MFH
rC?kN@S9H$Z}?Yuc=HPjeh@Hv9l7DeuN)dSH0HVtV7u$pV!nu$*FijoHhPHTn8`NgL0FksfsFtr2*7poz<wCL#d^go1d1;sdWmpw
Or?0`4w*G6X)v&76DzVAi|pQbu?{^J`>Tq9#StUkIIiFf5mHK6dgh1x31bKRVd;*A{{5;FlyV&+WQ2<qKBG#!0zAHxj{%d=emC-0
>nP-}7m?>jjN>0`)vP<);Js_Oo>xI!@V62p)F@Rm)ZlQmhSAdis|mq25wKNn*>+d;=|=BrR}Q^q-Pjx-@Bq3>IBvjz{m`pWr|>Or
rX;2dN*J7^#_q_E9cbC1?p5X{?<TeyY}ogku0Wf~NhMs*{m5PU6<+K|dP2uzL5K);1yn+vA2Tc1=$IIf?cS7)8v%6Tp3pTmc(>i<
lDch8yLN4Cb*Hx0c_;u&Z(MSm(4G5^!&upI=57!=P8k~-GF+XN@~G2xlGTihv}`mY-}Ri~!^)2<M$e67Sgb@VLm-s)PV=yRSaL(J
Bvx}HzINNYd+@e#?caL=EGwWo#$Yu=L!%KxsEyge^<pSvmFMmf*F*{#a~$euL@0n>3)D;GIC1cZYt{ILSslB&Q?qvL>TU_^S>?bh
+kln!;f~op+%>wRMYsyWwU3~DpK(5*Bg_j%tIFzO={teP1OSsy0@J3$BnH6}PGP22b-^+>6Yj};-ylL;MnSl$$W{=E@W!MrXsoYs
1hfY{v9h$9H1$g&Ab??xXY2TyT}Er4X4k!A6~d>to-bo0P7{&kO#O$LN|~|0bb;y?QOqi36aLpN8%C}C?HkUlAC4BD53|Z=U*8+V
+}}mOoW<lrYuG3sL;2$JynlK1$$5KzcJ}F_OoPG2VaDru1%Du_6b4|n)WlLLEP(*c4B6l_op7MVznOm<u7jE9+^$`()zr7GbARH8
w5m$5XiFoxi{Y+>b6WE6M}RRzs!1#WmY_d-D8)YF8aA?3<ilXUg-4$sR@aNL(`a=XyRTrWE+5(r{2Gsf<wL8{+HW+?(iu?9+mrr9
6JB+iuP&w!Gk5BLHNS-?Kx6m!2Yb%mj#*lSehG`gj)`l>1e#t)NZ8ZT9sKbl=nP*+vSY|ry~RBAW9-avxLmK|QhqVgI$MXq20*y8
_Q9@r8u_qB*3rnXM?MgIyo%O9Ny8az$YFmrD;>0&fS(B11?<=~zom7I$Z<z2zy@yYG4O@b>TXejM{6kMF8%xZ*oEnyxgmg&JG<Dw
{csY%DBZX;P|q~-!542|AO>heUmy*TkT74*R>3k_0JDvOlFaxaR@G^qOq!x^q2Nr8<N3q&#Bm5&P`ZKGf)<=0951YH2X@3t$82@X
T|-qOKn=%{MUg?${FgZtY$5ZS(*%eYr~OX@Rz5xZt>4~pfbg6zSN(U+<>1u${o~omz`6Y6^Wehytp!Do-(3L9>X@A!v$b<*wsza_
4?g#xKR`I`1N?UYjH?5j@N@rsaC*tgZai^*JDdJ<^2Pt>@xkst<BQQv^Kp80+&V;<pFgs4XSm<l-`hDHxjX)Dr`0*=j5<4q{+`?M
n+FGDZ@ja6Fx(v;wD<P*+M~{4YrMC+3sTg<_+Y2w9_|2`qmO@ytaXLGahuKI-u~g}@NlQSy9?9db==X=-}O4}PSfvn_PmzgK5P#U
N8^Ko-R8bGYI*I^UTZu$+}SzY12C7&YMM>6Wwy<Zxnu5{duG!Xl3X~dEDRx4lv3R9Pw_qu735mjjU-fyZ*S(4TN?D|r?*Ys3}Y7G
H_fAu0Oe@QmMH4Dvzgp67?UE!JS|cj83`?88@yXNPLb&qcBIvYscv`7tB<x6Yr@L=3)3YzCM}|1o9{2=uI!RLlG<Q3@u}jPW7xgm
&y@buT6_nXCPHM3Hi5BGZy8xpg?9y+84RGZa^op=XC8QFaBm7J5}x+nU$D20tR!}1K|x!HW7zqaS!!6=3G8|W$ctq3M>c4TkQa|1
DwpOsHUXy--{T|%9pGR5Wz1TBecznB_s~UXztu9Ai#zyofNcomKbC@+Hkwn|1k4Js1!wTJe{|^_4bCr*-ya|KF9&6lkAnuy(((ts
K+%q=Va@^|Ha-+HUiu?u;nJ{8s|9~;lZ&|cU#8n`6u9BY=f7dlBY5}ToyETS$R0I(M-tm84p#WA&x08G9J2sPMr}p2PvW!U%?;RU
hp?Rx>#oT8JT%M>Y6h!cSOwSYJ|TFK#;_&9+b>1xB864r$Ruq%0s#ZVfPzR1Fv)fgBo6ldhZG|N4?7K9muQxd7z4ea5Xfl+bPq1+
eTS{;(GO8W8XJn(d7(rI{DJW48RNhZEVZr3UXmzR;owVw>>neJk_H#nZuh`8a5Ygo+Q@O31Rr&>Ruf*_1*_{)W>0KPKq$s_h`L%C
<qTNppJAFRI|gjTOZe7}1SR2*MgSb9B375l;bWtdXt9PF(IrtJ3>O+BBE|YfO8<<yyowcBWkJGa+m@0wtv!59Gc!V&mNk3xYnEZF
M$gMXgR1{gdW&M8AC=<uaybh?tUyU+?yjN$M&9Fc3+M5E35F7k11Rj@FM&d0*tFf53$pWK_7DQe0qHl2>0-|KJogYIkry*DD11gr
m>MsC&(+F8&NDXw6ZEx=wDlz4L2UpQ223LeYV+-^$50w>xG=w@$!XA#*r+TcZ2J+~6&ii%6SJbloz*230={9@FLrMk`5V^ifiSp;
ICB@^Q~G`P6R4f=|2k_WC8ntog7tXp6YzNWzud6AH%$&*saV1|kZlDv1v7z@DDnJlpua;2jd@k-)Qw%I&#7IdmTy$cQ0VV8Jl0ed
MHT4e4UUIFnOCo{kSIarJ^o{U-B>R@L@Y`fNC4V=nuvbDE>P<;rD*V2l4!ohF-QxcSm^`+e~H4G>;?LNHw)0$9By-hO36<r@?r3?
AFhCnZ>R|_!Y`s>0EJ0C75vWF0$gepPOhd{EQTppm3+YW9^7q!bumkbHcC4@dP?JGDUBaD0#RL<cVJ1^ETQ|`wD<7+RS52^Wd<IM
H&{I|6x&VU9q`iu@(Cv49KJFxb;}o=8?nzHO(ovRXGb43lqg9{zP<Wr%5Bc!TVDVWeBK*)vqAxvwn!WHW7x?|&M4_`3NUG~p6@xJ
)wwHJ1qyd2t^Iq4b5{B*ABkQ7J!=9hr%U<HyUwWDa?j!5SPM{i08fF?UB-oOVJ6^exI@}wk(~f*XodpRgpSTWeLfjna%IT5IJ-JO
8aU^JqqEbC%k!(F%j2_C=X3w!qHMwpYIXZ3Cl2g;piP~BIzH{6I7j^pP^QjK2hRKBuY-5a#YdR0cL4vl{`qnL6rg@S=?hpIoU>2I
mzRTg37pHp<$3?(;N3Yiyt@n188oDcXgL7y`j`E(Sw-2JhG%Ryr*Sz-Gg~O)*kZW=={&JqsKQ(Whn)|8`7kR95oz{{5;s_wrPKBN
^FxVLR<m?53gCw{T0C!!0C<<ze&nN+g{3_oc4F!qnM%Y4J0|M^KNx^bYccMj;o`SeGqGiq5K7)yumCwpZ67chp9iPdA?Nh!lXLm;
e9(Uf6AyFrIrHSxuP3P|Mt1>%R=5eGMF@-^bntS4LBdzhGL{5sU?{XGJZq{T8-PiMg8w~RL%)Tp<DS{x*@u4z@bA!U?>6BdsLFf0
@DJYY!Mi<pw+HX`;oUyG+i%0a4*UbwxDVy_q1-;aKY;fK@cy6;+_K*W==)Inpd)M%yZ_^M2%+MGYVQ3T)O<R(sw_#a7+r%ZMf;9J
Cj(N=4YC^Q5+th8wY3E4LCLlO@&<%>=gy|^i=V=%Lmhg0V<?FRst5e2K@6x|Dc8#725!ccn3|1E+QH%&x^9$B5Pyssno=vP%xjZ#
Ye(pZ)Kt^x1>p<M91^vUpRzRRa0JAqk`J08RN25VZ){t2T<Xv`RI-(F4KaNt@|~lVl*Of?4AzOV2#d{I!^T$?nqpw&5PfJE#t+eu
WO{MMb@k>ftKz;$AGNj|SpC9W8#Gi~%Hk#0wYQiWKy_Pk6NBsGUfr@0z&%##w>Y-oX<K{RmQT4+!B;Bp(o7AA1bd__`2ME#XAKKi
r@sx(VYh-!?c@x$th4j7G%0Xok))w)30$6GOVeGVw!mChw-F@0;kJRaIRH8+rd~h&S)xwbKG-9s1=>=3{{XpN&TMD=3rZ_3n5~Md
1#5(p8+@k8eHn}S#$M5K*)9l5)9uyiF`)DUgahDv&gJ=Fpo<m1waS`U_HwyVNxzX+UCDI(v>l71@CWUhO1jIuvp5nso(<w9LzXbg
-gb+hE}9KBktRLfr(`k`=Occyv%6QNpP+pZC5eL_VGl5JBGXGOsV@_z(neNIlp3HQO6L@AR0jf4bbu1cVoYX&(7!7ku}-@*u5bJi
>=mU7+TDTefVh&#Qmq;uE{C2Qc_rv><VFuY?WhLU*6liod=Dy}ufuL>$!pdxO4;6lh$cijJk-JCmKcP*Fr;HAdL(-01@2@4l2v^?
3znrx<SwuARlFpLY=tXyvYv6qrioT0uV|JUDYJ;9LlZWqTQtg2ImISR>f9yamM@Tfq~yfiHcBKgWksNG;VC<mw#3oH2zHmT)ZYb5
qT^~S;OEnUo#oNo8jRGyfq=3ycW0paRmO1!65qYV_QM<FkDz{Hs~*P*upk`aiXZ8~d~Pa4unSPgzW*pGX@K|W)X>Z$Q*)eVG6^93
Ph*W^;|=R5GvyfgBz|(+qLI{~P1bZXKy{e--;j;1%1y0h{G9`{d!-RPx~aG9bV1Pp*dm99ba(L6MSKfh+H6`_aU?4NGAuU(oIkTh
HXHI6+TlcHXu3w?7z0hv4<kXH@K#wBqbpMALKH=SF8XY2+}WCrDUw<n;g5oc<G^fsrI>BtkMD<xa|{3P?mC$HrHvdD7U|Mo@-x{O
y$y@3jh*Yz23l8BhvmiWMMi4er**Q97_VNnYcwyk8>VQ~H(|tTK}d%wjcWK(zKkA9J}~VE-~<srlt#{9LaPsTWVnFMQ?P?Y6mWA5
X9ftRABv|?5t$!|37*f*GVo;h0E<6H+;esaOLyhZd&14D^!EJ)R#3fb=sgpQ1c$*=%ZI-h0`F!hjr8d2IHn)Tq~q2|3SY~tw{)t8
9X-NX8B-C)q&W3`*mZRZiW)G_b0B~pDI&7dD@c-CX4%Z#AwXr{-EQ+ouLP`c?K7ZY;O61zdJ*A^;Sa>aU960tI#`nFs9HB~`PwiJ
#k#i%L=J+4;-tA-gf$GKTWm`MgeZFD-QQ9$86QwEQ78Xp^r*v9M*$)i-Goy2#h{?`vbcgsYXf_lS|3^sWya(@7oO;AG_$%z*BCoZ
7Xkf^srqrIKA-|=3Tcy$e31S653liA0Zxb#;eEjz0969T=4g#KESksF7sEbMuy+)-1R#^0iGvWRySEe48SAjrnh~r4!I&JDWDsba
@f{^0RD8uILO%cn#IBwuOH0yx+{L#**8j~~uU`+9yPF$6RPGzYV8v~N72|a$=^4~edNmyg3b^apj8y>4sZnp`nkqQ%J2lL9Y6G0j
Kx^?B0{Slm<Qnub1U9`|cnc;9{G%?u2*%yaGHooJndJ?`hySSKUk>fRB;)^Ywn>-8xBtx$FB?Ju5a9%5V;GhF57~wPi#3yKNFMOu
7um%E^oS>Da8Of5ve``P#E7t%j!Z%S0WG}=I#3HfTkwg$Q73Aq1d4<??3kx1RGLE*HhEB-7t2ah7a5X+M%?GkDZquI^f@wJ_>@!&
%fW>1B>PTEnt~~rhKsw9eTQ=0ar}dG4n{&_#Tv)90K;b_%Lf54=QPm2nLh>s>-n+i6zvijIuatAA7_~$Qtg{z%9}u2#()dUk4bv5
dlT^s#11>dphjFixYyPpLcW)5m4u_ry7qE)CePM^_keHD5Ua4b*CW84r|}AFB}BeePL53Zs8+;CO)*Bpu36X`bi=H8Fx#$SXZkY*
;dHD`HZ`5^^K>fPpxN)zUu!zG*?64ZJI3QQ$D)#w@I4>(8fWG{fEc!bh7_l|QxY{XKXMy~0!ozACjH+_Fy=%j8FMSa0A*Ryo7OeB
W|I8Q6rQk&H4!g|Sa@P}li$VS_}FUMj15VWo6vVRUGAEZQEOtgsr6RZ&W#hd(QD%urA1sD#+GsWKFPs=t@?MOTa$$IA32an2DvTA
H~t4G`TAwF+XG?}l$jz#c&x~9of4;kpteY=x@x9LBFec*Qk<^%Y1B5<l@8K_kbjO-LSG{6QGpDtj^(lv_%M1yCN!#{21N5pR@!W8
@I~Aly=e_HI&!Swp|FD<WY3_chbxSsO77#2EHZvxdf#-{RC8@^UM{_h!hTlNoi9;BUz@}3=0}gD2aD+0?s*^&a%Hc#m@>W}>opS@
g4Wz(S|Bjqn-3&V(EeH=<`MgcZed$nmIUn_@S4=gd!u)M&*n?i2Ob{q%Y$7Am6QOO_<LI{XOy$yM;C@d!bWcx`R?>7WrAvN*B~A!
j9~eM<^YALgTJtchiBU*>Vfx9!+Q{|CVc)SaQQq#PoN`PybExS#EPgqnD?;m9vH^}R6|sA{8<kVd9JybDm{L_#8uzTt*<$r>154N
r%HyxH6ivN^3%eVCQaZ%caSxNUwdk`YMzXVF&)7IFV$p6?j-`MYP;1Xw>IE@f?>-ObhJT#xH{>hO;)<vL#a$OK$_EG0mgQl$&#KY
V{C(vx|><p*sa{oE;?t;xt_U5Nfn}dpU+PIz@zm3iF4BbV{l$J=TCHz&h2C{4Yt6~D85hC(bY7)sbGZ!A&W6A@0iI538N=8cwiD}
eC7Tp&0g%!#<)MQW=7sdXlY3nI)Tnh#XQmjoQQ2EXDaf@i;TLjy#ty_v0%L|bn&rtPeWbb)Hx$My&wQ)iH!iO3P~fWKgnpEY4ueL
23zZFH^LJqJ@^dZtZnn!8r!0dd5yImgJlJ3nyNDb{#suuNsIEy4{gNSoYaI<5P(sWQ)7T$-5R-BvXo_)8{Sg;2duzxrWBqDK}i$!
niO?%TCp}ubG)=`(vdA|#NY>I9wY3Mw=(y|8ppx~OEkj`t10!Hgiug$GtN;Ppbr1u@%#xMn=x!Z@nT}*rAd^@+w;7vV;AB)4R5>4
79)h}mR9cOhvVxCGR5!Y2w28u%eF1QFh)<&eM<5zwDvQB5P3X?Ar0CR|J48N9Q7~zCubk7_^}ucmkt$A1;Sc;G+=z729i3+5H3r*
O_MlH%$=8F;RD4t$-CGvkx(4$ti#_(!b!m5FX*LoJgca>HCYx-w5EnZQBot#1e#(mmOLzkc~tX9Q^$KAazdyOX&GjyX(|$i6n_lc
q?L@lN?Mxui@Cpw9-JgVi8W1kwStYpj~pJaNjs>N05hRpe6IeaD+B_3B66W1=qus&NDj)K3y49U57LB{F9s*?op)FLld`EMtNhQi
<I_v${Os(~IXi!Qd<j)F^ryj}4?drrUzUF+K1`yAM&vk%eaFefU&x>}I_3On=;@)qJwC<r_TwXTL_7JzIX!dwmzVwH)4@56&pGPs
I7cV_<4<Kee0s^rCLU+I6Tcw9jh}7ufUb3f(OYz?h)2%y01*S<?yeUzzfKWvAg)S^YJ3YXGN+l1(&++EuU7%UqAix9xMSaqM%Taq
;`MA5Q$X1|mdBj>DQB*yJ&Gi&*GJd>XbKFUI*9f8Hibga62z{|!R1R18|kc3kM_#Pm*vkOe=5T2FN%43aTJj1@Xtrj9(~*%C#23W
5+7RfVEHqFvuO`nUH3^vPt0K#9&ZVn(0rItYLgzq!h?YaMl6(X5$&Ocu@Gb2mAKpT_k{?ArFs(LkKSmu04inHEpg*p(fU&!&d}H`
z)~lj0G&5;7ytVMf{T=#pYhI4*ud<;;bV97`utI0Gf7n-(a;OfeLYq8=W(d;SJ+_AA6!Jfm^qJeA}jgSNG}rFRT$gpd<#(-%Sa}|
aR=iqTTO?1tz4mu!uO|71K4#?Kq>Ow<^n}}Q{LvzE+d*T%B86HDIXZx2Q`p6NB~8D#$DgFx_MbeYhRnPCtGzrFF;8P=Q~R%S+KWO
`5DR*P2CnY^$ck}*;+9%KH1#dcPVh7tWuWfyQ2ihcPbw9y}W*iX_p)OZX65)6c~x;;!78p<P3_|$8IoN^L-1*%a0nkeGmVd@cJc7
dCn($xY#8~N+^p>v>ebeeZ!3=8!5vtQ~L-*Ck(R6EOXvnLR8^FhdUkNa9_AIxN{c_Doc?3S>alcFLU!-wv)zx%JU24AMU%Yi#^An
+)rRqG_Uv4Y%xMaH%jke2ZUW|k`h-!JjLaH=_P-|RrtpLf*(40ccXX`E`_Ya9lB?T%83+sh~^6X)bHE~i5vPUzcoOdh1c?Dr5sGc
MdX*ItL(#^^it(09WEQ>MM_U=>KC2@7_ZvW9wmd$mRism4-Q4=RQU}P34oNk;+`EMdk%o~AJCz;*Jr|_-V1@uVGAktx<wn?FD$Ur
QH@juqZ-i@TWd-Cj)DpKcme>kmADL3RRni|opGbceW+ORq>8v0U|IZAA7FA9;R|iX6Ml%TVACPQugucw$l`kU3qsP!O?(VBL0U<f
Ay$T={E{_sh#Pj$=t^iN+f$PL2cR_8Au#Gnb&Q!@#w%@17Oo}@9({$rYmNmp4rQQSDT7hEPog7<-}KlPEj{|tBCb^Wv|2$IGfWS6
Mg}dD?&Gew1&y0M3LN0ZE6WAFwd<~G!at3*dhmnO2Ew>zP^MdN*>(7YkKPA%Snby;JG(U;9}t{jR4e^@%c!-;@fxjpvp9)6&mA+Z
#KFcL8*rg=W!MeeU(gLcpz1Smn2|Zx=_lEasN**(M^I4XZpLEftFC!it+=(80h2PDm1?YHi5f&_zIm6Vj~Wy<rL3#a*!7cb^=mu3
)F6Gyw92biHSz3MTSVXk>Nv=MGPTg}pkuh~(XF&{m&A@1_Dt(q5J>q~c7tZb#eT>)qAUL-sKLE_tOyncW_^Ge)@TT-$GLK|S<R{s
Y(45<V?@Y;%vEfTSLU^OVSd1HYDx{J7O&)Dv?KUvaTyl6(R1(hpMlH}R&UD0YUs`B8%3l|lI8Nj=uME4S-sWh&D=S@L9dreWoph1
v-PSnuTC*7Q|Qyggs?ZyWxxmsBBRR0glgu>U7Oc_ET|cehunDsEwaXI)|4DwI@N7Jg{o7tb*NVbxFFJ2poT%DZwL?wk5BF-(_`6X
dihaX{2yv9^8?acFS?GkI`F6$lWl$GY0GJ4!bF=VCq`;bqP3XNDc#$?&`uGA*ts&Wh~TFFCb%h^6Dt6A3)O4I?_osN$~G@J>8_%O
?m0r@`)6Z>hK_jpQ2D~&`}ZS%3A?T;a1w<5*<=t!iztghL}8t^s~Y;`LOC}yEXwn7LS^do?{}>yw1ro`m})=db$>t6#~s|5?#;CR
#to)r^LHF|@Ar!*3W!lpBG-f2#*ShafjCEg<@XEIy$|9RYtd($wSi&2;^<1MO_(GPQR^gEixU8_NC{uf0`z8h6F_f<(3uPPf5J*+
OVw)IkPs$JG_@7Li6}aGrs#<(`t@rL$Iw;8@@O$z&qF6(xua<X9!^Y*gdtQ(yZ_}SgXfLQ|NQ#3cS1`y2t*GofDqg}NV@RMt}*CS
{qoZ4n%xsy6oGdi>^h^TCwA|n1so#CJir0~3divED?R27z|uj&u8G1m*yr%k2Y8Yyj(JdUEmB#UFsdFaF8TE<@Jvts;=>bbTM?xo
Y@la~kb!o(*ssY%wb`m8FHt0o%gAE_ohB4AK@@|f>$t28+Zm|HsChW!AOu-dvpb9BHJ}fWQUFLYJF|Ed-wJRMtP>9zaBGJ<Ba})&
!HFnSr_p!Cl-U32Ap-bA`K;;@bJL&ITKQviWI<oQ!o<iksyN2LCy~g{A4R|=CjcKYg5!7pbEqHMV2zn)dNV^0#{*27R0Up`2t>vL
u99t2ZY-R?0XefqbGO=P9aO8qN-{@HSln+4PKcI^4A)Q2L-C+`tsGs8SeEHcWUrV!Vh+YM)YrIK(5{E8tI=%2mX{p3!-fI-Q|M2~
aKpUW>!xCF;$Z_lMU5_$L`cw9<M0qyDgHtVvSdN~l{ZU%7>Qh=c{uMil_S`MO=|9}>P>p#i~$__G3#wO9>R$k&Ik|s2?x19XY;&l
UNhv{h-m}?W7Y-;BdoH<F5d`H29`cTpe{Ss#OfYag@$4y<{Oc_@n;nSwjlKa<x-P&MowuoMT|Nq79G8O1L6g$Bg8Q)hqbu@8~kf{
sCx4+HZ9!*R5A|`X&(Qi`~sB{)hsW|fOJj*ILIhzl?>DAfaG2vnDa~vKogJ9{XWS0w(*Aaf?t14#PlKw^Alz(va5$#QsHV;LDrFU
HqTrlkZdxKM+^E=t+XjOD`Pj@7pY~C211g~ufIxG`bp-lS(zgrgzGIT1u0$BDJ)f-*0nTo=W`cyK;SP}oHPSKN)_?r)&e`Hc5H#;
uUsa9Tq_vRdDkvLsljD_KFFrTFZBhGQN07C)cCI({1r&%S<5!@>#yi~MyM=mMpkQAp?}rNodQm%0W=!~UC-)rlNws_VDaf}j*-o%
kQ;&-6G;IvuDblQvI4o&)`?n7{)~Z+Kb!YNVwxIAa<iUH2*dE}4Nq7@EB7JrXI|-(GI)3(s>Rm<XuX^?pG=OEj|A5f;t&{7B%cxI
QKrKY{NquR<&{7A6NzxP6F;WFdEAx)C*}W>%Y*Y|5*#Y|nD8*&$32N*-fk#*DuTJ#inNSafdz`#n?CQod!|%8Y(+I-aEr>l9v_0+
2FiFb7h)>+MgxP>419NwT=q3Xex2T6F-Mfo0Bpq_#+7?AQ-B`yh{Ul*H)u39RyM{fDp+kbt5q5pEobsv<aMNpN3clA;ng>?jVvSV
hEWyYcQB0ibym+4VjgxKX!bTSgzJf(9t|T?P5gQ!dn%>EdT>UacK#?CGowcSa^`XqxX<m-ZuFp1kWg?c$%DOIFl=cN&K|_6usepC
$i=<tF|nzB{K*sGBvq*15E@wLMd!cD58x+HWAWf$p2w;e&o~FLzvT4zTtC(2-WLB+dXEJCnjMw~>zPl<T43f&+@YxSn(dHRSK6nh
QR<5Vb#m-RFx-Jf`0K}bI`68e6|FoagefW;->%)r?;$7`@#MxUo*+iVEaUovg+tB=JU{#b{-E=)=bIRNh>!lch&-3xE+T*4Kwy{G
YYYvbxGQpYgC8o!8p%?=(>q8#<0T?rQ7gckH%{5kw{U8X*}RdsNLQYT#KC<IeICD0yW=0dlJvsd>9&6GV}dZ@!n<Zm3Afl>*yFJd
Akl_;wA7Ok58ReXaXTa9sZip?<$esB9qhaCaZ_t`?HZ5z*@&p0jfnc$WW!UksF*hre{t?!FZ}CmHr69D7zPcjtV)34#vR+}-fZ{t
=ce^c^zup%HTajKIBv`t%R~@78}0*`vj0TL57e7IUyo0UaLE)H7#D^>sNDD!7(^kM8mnX`5lO?NPmd<~U!GK?Zg?VncthQXS5Nj8
Ga`F)7yj*a+va|E*F5O9cFe=>Zu5sKOa2+;RgB-}4b6vHJ9y-Wi~aLIoI%GK>?mKc)4|0Bo}iswefa2{9-oRFTil^8CayQ2Fle4<
iYG!q{=(x_>MBkJxC<_Q9uiIGx^s8gC>@allJAbL5ftAKp|I|QflP{=HHgQcq!Gj`VqQsDb+7amDk1|zjuj#-bksx*0*cHY1jZ<;
noj?rjmkR2D+y-4V4`M8{3KryltA!=6gU-hE{M=6xu-cQC$a0wVfS46_9StIdc>;kH#|u^QVi+CJa0T51VaaJAP1-n1^Ao0A;GNX
15t(Jw&|qk54B4HbgGBh_f(YqR5k6dIL)|AJ_OKvv)(aAx}Um#{UP_SM=-hM1H7DT4KX`YUTRkr6BSkc8p>ZP$c8o@rU%99m5Q?$
;J92&rF@us{hcmoaIJgWbgc*5FiFr<Klv=)n-5|h<rO3>k1O#?X9*a66X#-(?u#;XivJ!maZLAI)K&2m>CyyW>dr0XX%w*pMQsba
kCANFqs^63&>FWQhX5ghbpLCP>i=f+(rN-QwT%Y%pktuMO4d7T4e!=j$8(t2D!xt}$J~rBJY(DZ?2YuSrpb<4r%W64PAO3O>sPO|
_xN@4w7-;$CJ}z{Sr|RR6>3aiB_)`O6cp`4o@hyO5VqUm;Z2;6uy$+jpsgylt5Ck4l-+45{)|4X=(X!W3FquH{|*J5w^!$<7su}g
x}UB?U{x|i4aD*3yTRuH{5ic$bNK%0J6_p2AACOP|Dh@;dP&~P^*G_M{8ECHLn|_NKLQS~-_c;^bQ8QdVI}klv?6Nmt;%%-FGCQi
FDRuI$LUO_HB9cS08~c8iAZG8(7TxA7m9l#c?VCti5nKrKa5)sfd3Ze(h&2_hXzHE-$F}4%)7#YLYb3yCo1!z)VK;%D}~BZ4_&^B
{BS|^_U~bz;|?>3oS$*VeZd6{@p>q-dZoN|MGv)nmT~E-Fm2HPANMEpFaHvCaLdgHr-Kj7BFkC5m9-_d&4Zky3Y5aA@xVMNsL+B6
B0U-wI!K`2qznC9uUtU$YD~GYVP6zk_fq!_<Pt8uzc8M-d_aU(BJ1Cw#Z*DCZ{AFef3&(7=iTDr-TX{RyQ(1NF_YX|5YQhyuQQCo
ypZbV0zK+(z0%S>@rc2EIG~o39K<N|Q8$3`RQ)v2#EL%}(d=JlJfV{0iJ%$+iI86l)fYjzw(+#@kw`9?_YdN(NH6d}BJU>M0g1Nd
*tBd8VT%{eSVdw|6GIRtsDWXDKBajr;c&7i8lw>izM;4MOaopP9cm;6NsffArm`^tRNy&M$h`NMJ^KJ)^6-QAcZ+Y*=dEe<rE3)h
YlD=Gi~7#!ezvd?_`$_Q{9@PG-4jksTTV|B3-YQf;kT<}5pAxHC=6wi-)4~?N{jrETjWQg0S+_(plFZ>`9(BR7Z2pYM)OIpC~^y<
E(yOd_=ZPQI9uor^|B#qM)G8=*K~$rYo|ccTMD{WWB6LMBAlGkhf%AHAznwL&r@6LNRW@dJb%{3r<Vxpvy2Z@K4N&V(*42@8AMJS
T30eL+27kBjrP6>Oa2#O$=|$s)lSYkzNo8H(2v>y(&gT}vAq27;+fkI-(S2Ss-uTNuKD<e^vWAtpvb?cl+5=RO3BQ`ZNi&$Vt3?O
bG-1ulfBhLFpa`aWsdmArpE7$A5u}3VA<f}8(kL2tkfNk7f)aESa`0LF%@?BjMA}^KY#YpltaS|1r1P|14?}-b(}i=^5+IO6Hv4+
mVyCc>Td2uNE(8oSW=SkrM6Nw@@B-f{ST~Or)+q7GCZu1qz&T)E{#6WFeOV!E(lQ<tfZGFf7^gQ3wB5T{@5;X8{805$&-<I(6<bO
(PBOl0YK0DN6Cc!Xud6<u=Wf}twn0Q$|SiglHd!cv<W5BI!qi|6}?a?6JhAgm1j|=Kxp)_#yct5jgU1ml!@;^Q@>Ht0<Sx``0)!6
TS`!o)&V_`TfgGb&@Nm0!Pxr?TyH85!bID+MC14xt#axYVNQf?16R`T@XYS7+7dD-4c3YzsP7YTHhd!t+Wdl3_>x(7b~ehKG~sRW
<xhl{bF{6q-q+*wEvT6GmKd7K_sGw07pvSZ5pXW}3*#58;`dZ%)5&h=;9{!}JBZ3uKUvvvCjWGb{5Y_LwPSJI;`EDA5nM@tN+QzK
tF%d6<aDF5D3a=>>6x89bKlG62;$koD+t^)YFLXNb8P;^<*V*`C9ammZZg6PEmalh_kB@Pv3eZ*wirL4@8s-~2#4Q5600aNxu2nX
t+V2mNgje)nVX<#lZ{gBaVD^Z4g6BEWQhL)14A&mUe$5OtApx_#=uOzV6M=wK%JpdWGUc=78Ov!&B)T(zHl$Kdxe+(s+h*~^}n0k
^}m}O;q#1bh{3CdNDeLXas&Msz2O5sM3xHjtiDKkuxcGjQ8<IGPaGJhmW{ecm^g6pMZ(E!6VLYX*nopqpq0Qkx?aS7_{82vI06Ne
uMlVv7Dx54w-n9bUy+f{QtK|+%Jg(}dX7SBRT@3DY?_>VXU>@Jm|GjxH%aNGb!WeBcJYI4(%I1N4E>H|dS$#mOhc4d0Ex2~%v~an
q~C-~!mjAwZL$>=iMh8Hu0fkk__YJVLyo|vQ`p=Jo3NM?wUBvPL%NRYB%nLlN$FC}A=66|W7LU9e(8ln7HXj(OR>{p7x(}(w=1MX
;jLnQ!fA^yT;NI*84)(h9+A3AL1cu+66xy~Hnu?*D{yaH%&E?<8qnj|=cPFtlX4;zP<is?<kQn%#8J#;hN8lu)HO6A7#b$}Rmp+l
Ys|2r?=rH8aQvW~B5Xa;K2=fXbI!(jmEI<IJ+}r8FiBOBIZ#!e84JxcUF|mRjM!I7`mwQ7zLu#`ZE#2}bm+wI!s9m$P&KX(hHoZP
5m0s#daBM)ZrRJWB3e&I!tRLpZ`E2&cAQ(e<2<k1NM9?|9A(GJ|0c7!U@^{dl_7(+R(^>(Ed-G4hi1r~^Ak&h;LI$uc_sUxTw^8&
FLyv7z6fs&K#vHzSBk5SUqO8`@&2$dMu*UFyg<4Z5wFfTxCfX#=LaSy)ogCf%#C!t7aN9@0fz3muqv(nYGC}m-Kn=)xeHVd&<xqC
1%KbqzB;H*$wb-eVC~jn{V-c%XO}9YEw_YOMp=YAw`O{&tjsU@C=`_Av-UNzP0}CkaV+!!gj!=BhBctsO6b<r4~c8!Q_+AT<b!&p
L1|ZK)yfCqEJ&Ydwv(}lGb#IOcV<3Xt%KS@b=aj3Zf;2%7Gdyw^qKoT)}c6qc4%hV)Vw3{1|G;Td56>~hA_-HxOX-fMuEXu<AqgD
9?&sWHd$F>+HXYbuwr3YvVZT7)^xmWmg^WDn>F+|mJjeWe-nkxgA7uamv6sNES0@wk@b<1E0bHM0XOcQc3r4d7T0`Wjw5kShIt$~
LhvD;ImqX^yF9P}KRn13;eKHB`Xh#|{`B>~#5|u){4vU9{^(!Arfik7NeoDo9F26$jPjQU3j?WkfcS#jgrNdX&^mW3=L@eD)(0Rv
0>E$-*^BaYtC4l9-6E>|9vA!}O4N)Uzq{b~)2<L$(G7da(6JPip$S#j?IHJQX2N9oHMd&)?w`Bow%}&dg;(%wq<C2VMo*n}S>vW{
@?ku}^5NdL+F!xNJP%m@ke?z}z9@`iZndk%IC9Ab?aaKH2%1}@@2`~CS}wfoW6z`KBQDrTw2m0tMH3yRaC-TLu1T62zMDKO)3eL3
VhudJ0#T!b-kgm_{Cd_x1(6k4IyEB;j}P7?8WjNndUz(s3FF;JC8dzUE+%urZBq&jrcn9JjIL)$;Tl0<C2E$wXx9-766BpXdTLxU
f?F!H+Mu*_Dx#n16b(wYQk6xqEh!yzd<nms<Q7|%V}u}x>x^hI>Y`9MPn3a(-%KVqx^z7=rJbvG^$Ua<-iXSN!+}v@mOOmM2P|?R
s;j+q0C+n#Ep`2ZYzc>-fR$~~eQ*PkkCRKVa<BM78a+-tg6NjDjY?IyDZFJ3t>~KWmz6OS4G`~J(=C5C$X2&vh$sSsatE-afO%_8
yLRo?>Q3#{&@Il`0DvWkCS^ht9eG;%d*Y7aj4;J78O}>oVpKoNj0!K^B|JWL->xdaSyVWem+T@>s<CiRf?3MWB9jx36&LuS*-RAe
rc5G50zQg(x8$)zWz{|<7Vy^hithR3DJg$7Vui*n!RJU8*ODWZwB53q?2@aIXfWm@zsuh%FI#ltr5n->V`M#2I=!jcl=P%Mw^mDU
CzI@w`c6Dl41oMeSEGV7M#z!qsgb{DSYmJceZmR}>Go51;D&P=gs3d~!Y9!Xcv0pPytRZ!zmQW?;%nmIrL*V+bwS@g4K69wAJ3@6
eO3vb$!PQeq`L|oN+-aTI|A*U{El6ci}Ya#2A;mWS1%<+Co1L@6w~hc<rc^7*Da4mf9ZY8k{hcAxzLxr#8}&-R8f)Vt2Bz9$(EEB
tw$;4U=*cvgApnR6wRyrozsfIOLK?`kKrOQoJ92Jq}WkPj8$VMErJ^aMr!9D@gtOG&%Xz3B_dN6khr`a#3Q{)kdq=<U*;;>CK~-I
8RoV?f>E#1auQ>CsVm|Wew!6lm{|Qr8s3&PYb>8cP>M+r-@~FPn=CNGG=ZX?W)i%K=u}tB1sK8Z>-)>6it=LVu0ESO4G3^12mgHL
GsdtJJoX-DU-~G?b!*pdl7s0HmkI?1)g&r=ij?@H6+WUy`0txY<3trv+f<cIUKSQkrM0`?1ih)V(>6P;Rx4F)k;@uJq`4(&7``jY
83v7P?Eu;%Qf}*r5abejfKq_>f*g0cdWltDma7hDq0`*kO-?gu8!Q??I!|3s9=q`J`80o8(L~Vag|}cXT}zvQLTw1~xl3M<?Y4Q)
YVr&_1zDZZ0AgxtGiRqv<;B%siKL0oM8jpXKxQ?4w!Su#XQ^$wwZGHaGnF=<dbb#50cXnz@Qd_a_em-J(tFTxpXjohf>aM^uQs#q
1i<trt(DSSO>fb;RuO&yLTaFRi?*r640b(~+Bj%l@UU7*m(4*JD}$%IgzefS&uaQzkff0lmA0^+=5D!k<g`SyT?qZVZB5mZbuC7z
gizRFaZ4%?N6UFZHM>sq^qzU?BiVnmT@^-l&{EbkCvmJ9+*yGM-b|zuZ3%%CqQ59!Kv3u@vPdoh)|i%*6~wYHER$v=nqZMGj)+LC
mgzjQoD2$~7iW*<HR{@IPG*ZC^}!uYebBHvZL`(c-?6vmI0u+6UT7>bn;X3-lQom<%*c^2*j47uEIpGrGs<Sp#Ac+&YLrf&iLbQ#
i&6Lo7V3c5e+Ba3#mD~n0R7T0&-<7P|Lj!19{Ol-etG=<7$m{Lg$jAlAt6V0-hx{3$r*flJ9zi*`1AvhmcZMW&n`a>&PnNjCZHws
cn9bMY%vQ>54}LhAhHge!MhIwS)Z=176BYwUwQGm(V9UA{L{hjDJOi`TAW-mchHQEPOjb+^z>rz8vyCUSn=W#z~R;D#by8PNjk=4
XYXfVW=Fr%an1*y`p2h$&w^y9c*C^}G~6y{6al|D>Ywz_owqRS$0Dxf{du2Xi+%F$L;%fj>O4Qzpr4+BCeft)@bBUC>^w;uukytg
rNJk<%;r(0hd+ObcEMrI6Hz$&l9TD?lYkB&+&U+zIzKN5b~kq$-@>EhLhZsx9iBx1Gtnm@Iy?ugh(XEaoiFHiDR&H!gtg@Is#2he
j9<}XT7X}ea|(E&P#9^TQWs^v7Y{Ic<^5CfGWocczbLTel2vj6A%=>}5ZAx|)v+0gV+7CF!Ie;avkBs0RhgPgms|XlaP9dRdCba{
a&JSM;L_+VrLkq{a(^72xyI;Cg}siuB<Pj9Qzo0(7=;ZOWf@U1t!d{HycVEJ#9vV7ljBlu*IpWld$dCXUeYiqeme5Ql+Vi2&bztt
$d4sD*NG|xZYtD*KdJ;z`KVxll#7Z07bK1<qB53jY8_AfzNqVzd-r>*Yn3YoPr0A*NN%g-1xr{A>N=a)oEn)FHZ3!xM=`fF0AN75
(M#@zBUiiyIuBN0QAg<RFkYG5#kQOHNa1mHQ@?IYA3raRLzJO0MR{)|cqk8@R_0~sG{Xlf;|<<w`I=6*yP{(^)T#QEcdKT_D%1hr
HqEf!qUaPpzR*^eQLR_GLza9r4`H0_ik74@1Y%@x-a?$GlusUKZ?$M8@0f>XyJ_wmn61_>Xlr{|G`W_EFTXfD7l&zI8tl`OB5MHv
Ss0eF)!sjVMRKWSR*gl7y}BT9Hsjs`72w(Tgji8Db0~_hUv@6K-D?(M*k(sYlJQ_jN9D2s(l)u3tHP()bwM~Efo{LV_hnlonRZ>6
uMK~tAK75|GCq5RuS@=wpVeoh5nNZBNcdr>!*B}xab@5SK5f2c?(0J>O4!vcw^)2cfkHz-L>kP!9zS%?<A*Z&t&0*`>tS4EeBv@R
)D#g;dQPM%+uf`7e<I>(TNbxWB$I2p%k;sI>n5QLxfCEe70J~(oGnIE=2mz2YB#;-1E5k7Q1{y+pzeP@)+rU@RGQ70ifF<Ps;DOX
QPa=9a*<H8Svn8dOCq0=)B?F|%kczrB3E3-hDKd{!`E8a({P(ZXmPH!OyCoAqA>DlBkutf>E<eh-7vCoQA4|6EJmh>t6bL#<E4rs
rk)F#dM0LSOVHHML`{jXDc4+?U(EDuOLm!@Wy-X1GHIMh8HZU`TFD-%#T3e{YclQH%N)v{$UN8Dnsv^TS?AP&>zk&DD#z*PvkOqa
ej7L^gFY&q&Zpzkv-7e!H9gwd)wMUqzm%BH+m@KFr{$zWR6UuJ4hjgLW9B9Mk`_6eIYGt_oB$EMuc*|7#!J!>_B@YbkD`Ug-d9?h
h*P}su#})OSOSz+_CyS`+OB$dfn;W0g2b5^rh>caB&epAtIU%{@F(y{JZ2A3LT8+!lvD|W!y<-JkY_gFb95r`SP?WXI(b8#l%3tu
Q{z=Jwmo0y%E%-rZIvc1@bnyk4V+YEjH-_CYa74Thw3YT%2P^Z@Y^wDG<dXtMW$b6VYvy|1XkTmz$WeHph|gTJxs&AuRrKnS7d0H
DDEv*sp2@q`)XkgsVL<<ZOJJYNV0uUt+cDaYTvwR8vkfvthlK?YZW|ei)Z!S?10FPmJ$Q(@??YJJ}MQ7N3-*iU_%j}7&4A<M9^1j
Xq#X0T5FU49EqPs50lPYh!slnP}zv*>Rj)ut)-^M2qmaM85hZY1%JG5zQ)ZQzZ%(aeOU&T1yH@}n<T^|w0Yb5GkBn%y-Bc8TS+#&
MOq}nO@E804i-d>6e`OQ3GVAmcujS5^e~#KV2&;Eh<flB1)d7lc*`o3O~9yO5f#b>djld>pMo32d7!3XDt=;g=$oc)8qNeJ-kP@*
=z2?mu4-xDl42y|UvLWr?9)J$H&IsE;jhW9pJTxq+l)Wt{{8PSq<+HRCxM#1bUflyfxTWrv#XcT>y9upAbp#UY}G?QYlhi6b>{RW
8H=BflB#)hBqdMk%@^~+490@*kH^})3x6u5=N9CkfC_YJ$Ci{5Q~Hynl$aK#l&~`sGahTY3*Hi=ln%tjo2KTSKQ?+eG8KX$Dj>jj
B>7<ty*Q06h~gDbW~`jpzh+$ESB73IvjcT_mt&ujz*`BVN-?OUg{l6yrj@SdU*~!-P4%F-PXdka7-~(xYO5VW9v?DKwbCRiNKl4@
$RvljWekew{#NkQ;NqaQiyA$-8}67b_-w=Py(EN3C)4UDjB(kAiXQ};XqYYvOFTORG6HLu&C1*{GJ<&LWnvCAbhRy{6~`q49bSuQ
g&at(!`~PgW%>%##&#kIq(e~D&AD_X@K<?rA{5c059DN+9Ni9}6A#J+dj|Q3quazga)S~3WXcSCj)Hup;uRv_3qbW>#b^ylvdHve
7g~Z(<Y55BDm3REYC3LS;X=O;&OkASBNOp;%cIsWjovK<hU1PEc#Nk{*5eg3ZIw!T(!Y|5%-Z|{`=B1ZC=%**Ib1p^>uC{LB|U<F
!)~pOoeJTiYFY?a>M=)(q<X$X^iso{`VWj7q7rK<I-~~oY$^S4p^OT*g6FKgf6zs=r{N~KEHs(cLIp9n=NDLsSSX(2=;!hqJ)hiY
OJ<|Ip|8X927OOD0bL|61MfvzKG{{ygo(tU*Vx6xrH$hj?Q*R`v09vFaG&T(l&qbUDGXhzU+i2@HrHk^9U+ydwImwmjBmU>PL#tT
%X{s@LssCkoATJD69|i%$~o&M?}o#apDxBu$efWlc2KI7$qzVTI{N+J7Nr$WGJ#s+3b;Z$&}d6UmYDVNio`T|4aD5cc!s2XK=Pqh
c&NnByX6tK)v`svv3z2@Y0)w&iooe%I28hUdE}HhJNo(PDd{wMb$X2FtNjx?!=__r?MR$5wrNlc<E);}&h~Wtm9lKJ^r=WMiqY#-
g&fEsTS+)Ua&c;mPKCK0vVE{8naKWuoeQ%R${x#Wf3Og}2?preK<sX^6h&h^F~vPgdeTehJ5B7@FfYs40tTsxG1@8ty1@++B$yWc
ZQDjsOao)`=2%$~h=>+M2owrb$+j^gg9cDzp%_xax9?3+SC4F^(Q?NnS_U3VZOc7Pn&MbhYAZ*(?``!}dxG4!Q+EIA-7&xESNCub
w81}eZc*I74ZV4I6*|F=89>(jUi5eD(#-gpyQ?hJVizqc$?@wT<8}m%@DEes$&sh;qX1o(@)tQPYSUbj1mXP&e?3a2!Xz7zPB-}o
zaqbz+^w@k4iv&0<<r&4<?+Sf(ixmyeHxti$$=u1`dK-QaG#6MXD5H0o_#uonLa+f9DEo&>xMxn=9t#~Zn)<TC7XWVKLtK>0$p(4
AD>@b>YNIJ{ysSV@DclajGaHe6p2eoD~nQ&G2Dr#vxAN%$48jw^xg6KfO;g-pPrul;q*@~2j{2#%YoB&F3+5UoFhw`n#tegLZSvh
41}`~cW$|Gr1QvAjv_C(ZTDFhkstr({{fLo*ro
"""
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
b=''.join(B.split()).encode('ascii')
assert pin(b)==[20038, 'bd39c1d965fd9c5e64d34d20a7b98eec55f08497df518319b3c1f3be41f77022']
r=zlib.decompress(base64.b85decode(b))
assert pin(r)==[48676, '94ba86676388c079c531c90afe7c298f7470b8edf13760567d1ae9ea1c45f239']
M={'engine.py': [5298, '682be4236a84ef58bb5162d8007c426b01af23166d5d1d84335e15aee47bbd35'], 'build_universal.py': [2305, 'cefe20bf1a481d0e2aa41598e1ee50a73c30c47f18f360fece390b710f3b3af3'], 'verify_universal.py': [8516, 'e20a18e5fe22e51000c9f6df2eac84fb9a619164f86df2da28513df282c7af8f'], 'broom_cases.py': [1659, '74de2c945c64b8244fcb17a0ab3d3a6bc69de27450bde72624b2beac3cad7df8'], 'build_quad10.py': [4166, '0d7238cd7caabf03dd63c9f44ab7e6d374a79eabda1b05892d1b5b6023e7667f'], 'verify_quad10.py': [12911, '3673cdd939555e37b44891ebe928743e99ee98ec435519cdddcf81497395e556'], 'coverage_quad10.py': [2239, '85cd99ba919aa606639e107c46a285a78e642b91e057a5a6f19dec2e577ebd16'], 'c32_catalogue.py': [7169, 'eb78c9ea5e89db65b791e8ac0298f0a21e6607e97c05cd32be8ecee6e8317d20'], 'verify_c32.py': [3133, '0ccbfb67b413046531801adef23567e2f791396070c3976ad70f201b912570ff']}
D={'c32_catalogue.json': [240929, 'efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d'], 'universal285.json': [1289123, '3a00b679c994255debd3acbe5d3230e336d1e292b9cf88507dc1d2c61fc94496'], 'universal285_verification.json': [41790, '067c8ae69857aece263ccaeb5b1e05e4d401d90f13f5d8ee8d64e3847358acec'], 'quad10_exact.json': [1440946, '2505c724d0d35323d2d67058e32ed1e3af96620c8802d5f3723b21589341334c'], 'quad10_complement.json': [161440, '4a7a7d33f0803cd2496a974933490eb29cca5419947d334c552728ab4d186541'], 'quad10_verification.json': [5815, 'ad0e56bc37cb39281e5392b3573d2d0c05d5d52976602cb80ff4d372cf193449']}
S=json.loads(r);assert set(S)==set(M)
for name,text in S.items():
    b=text.encode('utf-8');assert pin(b)==M[name]
    Path(name).write_bytes(b)
mode=sys.argv[1]if len(sys.argv)>1 else'all'
assert mode in('all','check','extract')
def run(args,log):
    env=os.environ.copy()
    for k in('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):env[k]='1'
    p=subprocess.run([sys.executable]+args,capture_output=True,env=env)
    Path(log).write_bytes(p.stdout+p.stderr)
    sys.stdout.buffer.write(p.stdout);sys.stdout.buffer.flush()
    if p.returncode:
        sys.stderr.buffer.write(p.stderr);raise SystemExit(p.returncode)
if mode=='all':
    run(['-S','c32_catalogue.py'],'catalogue_build.log')
    run(['build_universal.py'],'build_universal.log')
    run(['build_quad10.py'],'build_quad10.log')
    run(['-S','coverage_quad10.py'],'coverage_quad10.log')
if mode in('all','check'):
    for name in('c32_catalogue.json','universal285.json','quad10_exact.json','quad10_complement.json'):
        assert pin(Path(name).read_bytes())==D[name],name
    run(['-S','verify_c32.py'],'catalogue_verify.log')
    run(['-S','verify_quad10.py'],'verify_quad10.log')
    for name,want in D.items():assert pin(Path(name).read_bytes())==want,name
    for name,want in M.items():assert pin(Path(name).read_bytes())==want,name
    print('ALL_QUAD10_SOURCE_COEFFICIENT_AND_REPORT_PINS_PASS')
    print('TEN_WHOLE_TYPES_PLUS_SEVEN_UNSTABLE_ROOT_ORBITS_RECOVERY_PASS')
    print('NOVA24_QUAD_TEN_WHOLE_TYPES_COMPLETE_RECOVERY_PASS')
else:print('QUAD10_SOURCES_AUTHENTICATED_NO_MATHEMATICAL_REPLAY')
