"""C32_CANONICAL217_BROOM_REDUCTION_V1: complete append-only recovery.
Dependency: the journaled and corrected recover_quad10.py; run its full recovery first.
Then python -S recover217_broom.py all; or python -S recover217_broom.py check.
Extraction-only: python -S recover217_broom.py extract. Not a mathematical replay.
CPython3.13.5 NumPy2.3.5 SciPy1.17.0 OpenBLAS0.3.30/SkylakeX,
Linux x86_64, one BLAS thread, four fork workers, assertions enabled.
All six new source/checkpoint files are literal here; nine upstream files are pinned.
"""
from pathlib import Path
import base64,hashlib,json,lzma,os,subprocess,sys
assert __debug__ and sys.version_info[:3]==(3,13,5)
B=r"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;Fpad&0PRJh=?bAf%7fGH<}x+N`IlF`z08Qixys}ooK~ALl`{XyRHXTjXZW}av2o4dReTr
bqcVi?S&Qefbn(kJ(CqgFC-5ANP4?a!y^G4mfXKam5SP{KRxv1__Hf(?2KgswP%S>hU}m0X;e<4S8!vhoU&4af4NEy{yyB<cC}j2
TIGV2x6C=GLfxYc{);wHu_?m;_*+(;IaDj?B=T}@E<i65w^?r6OgS*zI@6HA?rl+2;VZK9#rwLeLm~UJ%=L>)cd}?_uxF{%63Elf
KYrziGgIbmnr^N}S)G+tCXV|k>9wte+oRt6wuO>8>EJ7EQ?qya$p?bhTAw<55|r*a$DQKb|H6ygO7Gj8y$M0tu*{X`#E#yZyJ*Gi
JG>1a{LcRu<PrxNJ}yG=3U|xys3|}!T+W4PtieQ!pgy8D9n?<?Y(Gg9T$9|s<|pSK!&n`eLC)T>p?z){K??Y(y`MqNU<MYrI9&(!
)8zEhAHv^-G6YBIQ`(iDX4f7BuXrUX^L<|7I#B2Y9_lyYKU6i}#0|!~eMr9Z2<1P)-oHKHpG88uJe%8fa<=!j<s1f9lv*Er&`xNz
M0Nm69Odn&<F*axXn!)mS5&SZVZT3+reIWkaHSw-R+ohG@<1*b)Vyo@&+k7w!JW<elgesGA&=y4`UQ4kq|Yjp;^u0Ju?w!XVhXtw
Sm%^;yxGT9v<9@$>$sAGEX=8?nIWm?y{O}pWU@)HDl9W^H&Oj!TJd>O@6fcmFpr>VoR*XMhbrI`1msST9+3zp8)z#Q<f41WQN+aL
ESLyZf^jt*N1>I$`D8A@LUMn`KC2qgrmujbga69nx99;>WiZ}YVeOySzzgN`oUpABE%OFkRTFG`^!T#*ygRYM+j->_(-_u6S1h@=
x^LO#43`%Tri#g_c1hrahM60kKSD?zIb7^!qYZI%HTfZUZT3sg1}UCO#s-w^H;z#uG*i_`vFDgi^fMgTEIULxVX|78n%%T3g7Ic=
HerN7;p^|p3nvjy*m_jGZT6cFqVJzpB)W!#f{juO!#`p47tI&{$PSa=bgCL%q9B{{#jRCeP5>qv>7Hz2QjsyS>?ko@AX(MB?J^uh
FOy<2dCGSAaAnRRVT)8jf?F5<=<5a;=2CWaw_@&IdPBxIPFMgt7UaX;bPg`WgK{%6_rf>?7LhncW6DEBPDTZ?fssFoUzj@(7pm1$
6JPLsMZU7$jkhp+NR@Yf2DJDBmnkG>5#;~V_gpQgqD-kwffgJ|8>M;efD^~nT8lkA7B!z0rtV|PAaZRY7}t1dh6dHq%bMiwggSW9
<S`sQHO9P~!R+>z(<O_^-tBvzf$3Tgd*bfQezow{D*z8vAd(SO#}*h*ETD4Qi*es@x;Mm!`wOn7F4}GT{xQ8VL%1N&=*=-<m>HEs
!Z9bRPd1WtCP&YDU1DsyR8x~oUW{T}$++n2aJZ*SLvx+9rbu2K6?6&mb>vAfnlIj=_8eh=ph4qeWL&+APGo}^hj6oO2e2cCy?%B3
9lPC|PnSQo!h}!(K8&Az6JwbIuW#7MfB;NR`4oejxr0txq;L_z$gl%!P(zz>9dN$|DQmbKh2JC9T-OPXKyVdnihxZ!x_;P=XiYzK
G@q`AF^*(8nD&hsMB*bCp4?DaYY@LAD|YscI*fq_u|!XuX;9<~)(*=8PUE&W1J+_y28wo#H&(V(y#D{3rUI4vXOBft;#Af?OZS%M
L{f~HH7*Oa;Zz<UDKK{V^iZ{y%~Kdql2GJYs`chjZRQ#JGWKZHF_0-<f7{SJf7M^EE$>SNvBIUqJ-|3<@dGyshOk-E44tt%D%t`H
uCz++f@?0<70@rO>>2uDhF+mcp0O@-84SaH3AZ>X?UY*VgVdiy-x%ZeQ^`$qZS8IUQxZpRY&k2vwq|lk`px`14)KK%7VFnwx|5ih
{r`v}Be<9hKiuZe6;-8L;^v3E3gmsixcKbv^bNND?NGzQg<6zCpHQU{a%T2+b_zHUjJaqoS>F$M?sUAh!<0H6r5g&ep<8~p^_ReA
*usEN;{JvlATL>}WC5z355}N20V`*R8R-21msqoC(y6Mh7?`Jq3=X$hwK+V91f#>9*9XK8$d?NcpRbpKWUm@GfO!hvjZ-BZim5K1
YFUbkW%u}w7d>7ui71^aQwR-s`R%7wvgQd}LC0stPaOqalH(n!T7m%FwaYu7c|cPpyZjZ=5x}bfD|`bSIGv>OFG?C<FY3GiyVG1C
slFf+rP)V3HM{0|i^#rgVZn3<g{Qqv^K}2Z`dc~%I&`>bssA0D1KUV~wlei}@Qg=lC`Pw~tN{*vEE`|W{U^RAP|$DS5_DdvK~!;j
7be)QBI<vIh4p6Y>Pmb)8Hf-kt8H}$0J+<-_4m8i1=lQzpfX1tC`GD#%Hl>^lBPUyo?%X{OnK$xmq8Il&8y`_2dQ4x(shPx?4+^E
1Pv{s<^8l-seI&Trgb*gdWFL|9_|hl&;}0zccQR^n`{xs`!GMzT5UigEu;>mSUdlBpeh=5-@{Sy&8dMiiPIqg8bj?_I<@#ETz|7m
f*`B+L;T5K()mekr!JZ9&V>rC8ed)8Y47v_xg_-Lo$lo=&A83>qFxM8e-Kri(Rgfdg5Ha~jB;SSbs3TEkI3~OebOSL`Rh9s^?o1{
XV(&K8Ey@9Fqh)&W9z}Ph>=ZrXCb5Tkgh38f~-y!YE2j_XgurzF6F_UX{rBScL1qaO#uBgVXHQr=a8d|rxAhlapAeSX}JhTR^&>{
sHCJ1#6~d~tBHan!m=pPKBR>ok;9>468ExZ%WQ_{J%cf^wM$R>i7qcrL1ImvDCc_FK!)LA57NGD-ZjJXXw-2H@9R=I0OH*f>^3=%
Gg_6R0j^eL{i7%}{RTL|VMFyrqcA-;s@=^#`s9Aybo)~&MorHa!=<WiglV9!dN)~oz|=XyKUq@3cE|Hu4PrLSVK4$N_Pd{rmL;o<
)#<V6UTsUQX{pw84YjB5DH`%YSwuiW<Oz8AGDSxMsqWaF?)8bouIkR+N7hxUgp>g_^GX3B;~U9>ccg<QRPh<S>SsDl_m&OwiEx68
*&~l3f=4>bTG8&g(wI@jxrb4qc(&B}PR4}B!{U@$`GS6%s$TQiip1`IKEYy&lvTgJ=vZ_=k-HwT5h|qZdPA2n<@kbuG~;soV$k*a
<In}TB|Tm;e2?F#)0gg)n~F@JrTET#ttGSl-9F!HGBm`D`H+@l4oxgGqyrw0;x5+Kec&gI(9CBaWez4Pj5Kq}up%$G;|(y<AId$r
N%%QREJRVkBsCa@x<;fRxZ0L{cpKux(<j*q>3}w2`18xw(xR0#plVGQ5}DtE+Cb;a5DcFIOh+TWZ7R%q6#Ba<>xXxK4}j1=dNj|1
>r*%D_O+t9xwWZtTgkyh73LLyjn*<d!)t}}g(Rddk<?!X^)v!)Xw!SQ-NC$|F%+)36g%oftf9v1C{Cve)OPpHyhI^eY+yZ8XfYG(
KWZ9Fx`)CCrGRj<_1XfTxMoclJaH&{-zc)`y)#5s#Gr#($|z(lOD$J<ua+tbvIb4(tYrM|uj6ZAR=2uRrh5H9zB48x50^dft0dAK
!h|kyX+Y6pNIxo1#nuU^meef#!TS)D+fh9x)i#Q{9QTg6I@KFDM{bkr!1A5UaMiW#LBmx7{srQ!40{w{FOq~^*XzUD%23JV8`Az5
xMUC_k`ZfSaAM452-1G-2_@zKYS*4;*{G~I2Eo8m(rxz`D%pEA`Y1>3G)r^i4_hTzc3_~Rc7VD+@wr3)^*W9S)k|$4Ex<d!bFkNr
*{_$x8DyQVu11{yrF&QFf;H{-_0M}#XrV7^?VNe8zn~ufP6P>@DO1UDvI)jUut~no>Zl^7?`fnTcKH5{mQ}jd@$N4GwTkK63f_6D
@?Of%u>dTw`#dW~h^mXofe-R1g0m-O#2wpVvWZQ@EQrHoku7~sV#|63tL~LNXhE}Sh7Zc*BM{|BA8kxc5g=pi#R%#DW$hZ%Cqk?h
&HLdk{^BPg8ucED2ou#5A!@S6=av^KQF~4ty%E;{v%L<#7u;b0?JS<+S~~U6@CQ0TC#h8^P1buZWe%2mnueituD||WnVBrfQLicS
+bO`6OF{gHO5igszsSd&j_ZLo0bXhm$v67RD8R1!D*$RfVPFt<D5jyP+G{}5SW&)o5EB>rZ?_^z-9Ai(YwJ*ma&Y#dI0XjFqP_9{
Wt4#y;W>$`W#AasE$!iE4WorgnAk2y)?d$_e1=?TV|?Ug0%=g#1={FQ`n<g@B^3ESG5YfYPj3T`RWaL3T$$SIVUk$B$&Fz)(NCN%
#O0z(^5|?p6ovJQ8gsmzrgZT1wj|l6Mz5EC7_#A+$oRw}etw{^Tq21OIB?o;EVQvjTy+O2%ICS#i`$iC&iW?Hb*jaXz|$707@Iez
c0!VRkBdnqJz=5cwUtRI{U5<rNz66EMtm)T-Wb19>ALn+8K`*h@$1H5;R1%lYGgG8(~fqKk#3u4u&5+E9pWEy_^!x6lg!U_v4lOc
qSNg1moR)6IPI8S?JxS6<b@H6?{X}f94uu6T<w?!ZQBUK;{p;I&F$|9G)^j_fExoC=*t_lCBUbo6&vjdE-F&~og$)bsK`IxvHrm5
vE1da{PIoXX{J*O*j_NPJ=Ye^ep21&!jYp%mUEnS^{|dOH53^^aVBCa2U2>G1ib_!4^l2mH5Xw~QwH<0TOocjGFoH<>=M5;q{&Ag
ScNNUFHci$2Bcksov&yow;?kvqY?8%;Or9LYb+AwO+ZfNE!;%j7Uw)h>60t*_Gk8loz4H;7?SXV^#1!S7yKzym37aU@7Sr*as~(5
<V1CK2~_QTV{TJ-JW^oT>NetSXk`qEKTb|ax_2ObZE;PzNKoOVIFd2ndL%zZ9X-!`$xY8olR!BY?z)=I;f5v~biu*Ra3ITCV0bX1
kk~Vq=Zh*XG}L)Y$a5-+0qnkERU4*@w^+vJ5}PTt9j5PKVs#ZI8WcpMO5jdMMMARf>OSTmdXso`MkX4|oZtk#<c;#<*AZPCSu^c~
`2O~P%v%w+wV>3d;QSx7X}$*DbL5D=r@z~z%j8Wt2W1D!Z@>Yq%3>N$aC+u6SzgK<9Q5J5EL5WN8#oI_ec7=Dr{1Tf>E4M?jYr6^
j47_BQ}k`$qB>Nj!CC=M$|-m4<et7;_+vi-POf`Oyung^c-09>yp>{8E4kl8QjcB^?YeM*v!VgLM>#_pWN4tZr5ePV-8}@xt0z##
l@FJvuBKrcHDpf)k9g$NNf7ll!#jp=3>Q>}<~dp#C&wtV(FsSc$34%=4?(A)S{kqjrI;SS6A>;THbweAj3)z*`H)hRk3hlWL#qYz
jz27lF0L|&Yq0=yK%L9G-qG-d!L_d1)4uh$NkV56XVl0W{EQ}a;$@nGtYPzPbJOx&);t&GKNfpISD%AkDIqj?W9@SOMc+-S0Y#$z
cNzih9hDXqlBdZaKB~lGv3uVpKkYaAwOeV;tfwxQfdo$YGADWEbj_ToQ?`Py5Jsv%4tl@Q@e#;}Y*RtES>L<_4|G}q^&6Z!VUAhg
_q}hsFsbB&n6)<WU4u)bJjJskg!<9JwXk`no0jh!8yw_|;r28oQoeu2dLx$c+S6I&2f9bS;Dxw_L0!Dg{I8+YJw>Oo&fz&IrjxaZ
vJHKn?BNQj`<`+`lh;W@o2|R&utQY|ff7<BYVa!fJ@BtgqM#urgTuZ~9aCc+xAL3RJCR16O=kaj+*jNPOHiKhfo5izB0hFa;~vdo
TYat!&T{RRo-9El+3UcIvR#dz3oXyKoil9Ge+HQl7w=NfPgOdzh)H=hJ>-XbJK|&KW|QGSrO(wci5(=g$=f1DJ~Kk>w8PjT%b@g-
7dy(Xkoh7s^eVr;Aa(%Opy2|?*g!wFd~PfzWpGie1grAGM%F>8MmLIxY8xScedYoy;DV+|45*$3fA_s2oy%YEF@=>#zjU?XOm#3#
9X1QZ?}RrZNUM85*}2M>CpW3<T;2C;JSdh#M<9TL8Wzn<ViHz{hXuee9d-TVjhF_3FOrr5Vp3oYU?)iHhA&>9@UNA?8{WxxUK{~>
(O-<zdS*Kza0$VO#Od6d)@7<lG5ag1{!4nI&py2<GQZXA%ZjoF3ko3`iU#FU$k$HCbUmd`*KT7r_jP_S;;GqJx*3_!yp}nbE^k3s
to6CZmdiQk@vrMbdvd8k$fuB3E_?e{?364&`VD~ageSaVT!p2FzZBc{Cy9N#+X@p|#_Vjs2uDE^5%Pw1)iaWzroS#ryIejhtv}WP
VAGyv-}sVV?h!sGV0)dI@ijSwkJIM=J|jBxtFF`;JF6j$juI^FW)f(CM_WwhQ_fp$f-Lfq<vqzAC9KlbAC2@bXp;A`=jip7tM&o9
@LgiiwZngDetaWc1?0wb+2~fGKUF0O0ZagW;`o)mZ^F=&-ss{6i=%sREEMhcrIyB|KtfonotW{Bw8eN-^KoXxxQm)9K$Bs&W6-ei
M>#QgkJ9?PeR>rFjWEj}7)UM=8^C}`E-63CE5A~wCbhz~)n7gnE=PL_w`_?JRn`3jb$$LXm9P=&%wE^$$G1AY=#6(E;{r`3g%&^B
0Vv~!CwxxC<1xTSlt);$CO|MJ9wG1{ld6*U-!c5ROB<HR2`DOaD^#uzhcJ#(3OnXJN6y%rbhWo-hHAhnPL1&bI!|iu$*Zx9Auyp^
(atxl9DOm~@j~5MvvtuA^RZ@W{7T!cIQ<-%%s81z3gp8^N~1K7^NcN6(OIopjW9|X(CgB}sC75uMEUz)W0Bdty^l2NUR<%QnUcuy
+vAO}LuP~mVggoxZlH$(yF47XCk7=C<~76~X0*0zR1}-q&Ic`1aW|AeR2IkBgybu$a~%qAxs}5dAqx~`6gRh^_h0ppMgFi^o5{#2
`@_q2@$9u$>h_d<ij>J?*&)m3pQ#BaZGd+Y<+NJqf_cK1NeK~_HvX|Mtd)aDYwR4te;O)v{Jl{#AX$)k*~$%w$AH}L>W~q}G1Dp%
D#peIho9YVekMw0OGb|h+4Ou*{;kEYkdxT4SA#AoSNJj-Un!}3mRx;o&62{3Q0$hLHkM_j6)7SG@)PcC&5z&QTuy!%grH(gt*3S%
xsx)MR)X0J0`y5uBg2hBtq!eOOOn&*N<eS0bN>)&BvWemTy0#q;QBNXI?jfiEHNSZ;7;q07VuTeg{t7fESrn>>t{m=97|a@1g%BC
=8uvpmQUq)l)+kBJ?|v_WGCz>XAQ17@R7zCrx92P)gE<Ki632YR$goby{BnY&@zT29#{keH&U1d^DuDuOvIF?3U7-G$Sa|?pqGsa
kjsF#6wML?3U1wvQ_P)kx4!zgFnH+`ogHzvo!!YopK@Od80d0~O*p0-t(N%&?6<M!rJ^{3s3Y$tf+wf@7VkkLd1nc)Iy-wicUg(n
&{HTHJu%v{`rEx4`Wt|`#0J2@kus+H<9x5}cyZ<_{GEu<NpLUYLqqlh_A*PLE7{^Yl2Jnzgw!P){0s`iiybaMydk4Pa2r|Z=G8K0
t7Bg6GPZ6&hsnghNx*NZ7`o-$tm?!~_}IKz2KVciaZzNx_Ag&JhS<fNstg?>l*2nUxR-A?1iAo&9IwbvVQq@yT6DO~bG>cEF-Xa&
JDWu;4&3J52nhBSc}4^KSkbPKQ=K*NT~OeiV4028!92Fsc%};7DMiW2xt>XNlXI%?tA<g1sDoJk5>9q_8Jk{G;F|OuWl1NndMewS
#P|{7sp}dTU<{%hywOhVq|2{u>}iU{mDMC#ns9%Cj*{uxN}^;Oki#?gAd==Zs75;|+K%jN4YT7=;hMyfKtm~68rzTSlA&FaO)!c4
TQmyh89VPRA87bd=0GdxD3Bf=bv{~+Le@_kq}+r&)7QeLdbfKBys%vYjLQwezt6BmAQUc_wn_y*3cn$AV0~-ELHkyZud)3z;~8Vm
(dNqGf#j=E?wMawAb$4(LW}BfOj^8ki(Zr6twd%Zgi4*Rnw+btArPkd008{4j~~c-^e@W;q$q^*gH2ky@28F7<0fr+)(46gT`737
e9b~);wwEK9c5%dkVW)NS0<IZu9<;$EoKcLD#d9Iepp{LY5!L%6<f2Vox095GXj53G?tm<V%i;MrG#+WZw$P8uJ5n+sqO~;(|50m
30Ww}4`|nCdLdvHqva(bjRj`YA{mmSp*-6pOsCM(Ajr%9Ph`RPK@A*k#?RVLD?wj8Y=#-;C)miUs0auiI%dcr8$3TIO=`R!8j0_h
@c==VY~ZuTs7DL$>A)65zlNlmfvB?ZH$M5f-IY+-zSuWVdi6>2^Ia9e4%u$g&&ziAm7pHgj04+Ggzz6maOjuL;3Q6c*dnWyG#0Bn
E!gb#)11}6!Dzu}Lql!7Rb2h~PpBOm`q-#b3stn2ih_>Ec+u_l&h4%AH!|901B85}-2%y7`tTY}z1BeEjEaRotBqEO`=>@xCB(So
&)Rv)WA>f1Jl#tue`<sBD@@nt@jjcEdt)A-&%->{zFYPDlQGFKJ7huY#M4<$AhuN(xCgJ-h6PkLJdyZ2IJTXUs&4W2Q<hC0R!}|C
jTp$%?HK!ypuQ?%%a3@7tWR=Lr#X!b@>Mm`O6Hu^3a4^T;5c*U==zIDIt*Cdjzm(za-*&9owGJ6Ox?yXqV{Sa{wI~CmGm#lXZ^Iu
ixVSZX<?E9?Ks95&t=OAK|YC~k1AUvta0}$=TKy^y%Vbs3?l65R1arirGO!`5H|t_B>R_4D?H@cVqRr~TVLWQ<0!LHM^W@Zo%YSJ
wpa(3$!#+VaQuWCudZ2aGaTtlv`+nnQ}OCKpGmmw2GhAIueKQ-%V9^m5-V_7r7v~GY%gTaC_3;OJ4k`GG^&z)Vek2Hv}K13b*)+#
-3UWW79aq9SpR^aqi?>8ZXhMd<I6o);~5>Si;wlJQDROD2&p8I%AfH96gm<}@*;=8u56KoX{>Up*kQT)Zp3<lsyh=2Ib3yX;+9zd
r%mIq+=5@s7E0MJ2C_RA-4aOibHfG!9eH<w9ns|pxjxXaUhpqy!8h`WGdqnX>F838(`S6rmyy=kVD}xM+M6_!f>dm?d*GvjDFz1!
3k5Z2r2$f1KfnoS&6JE_s-j-pB@J3$*uq9))zm+L$mM?MO)fc^B(^KeW?^^~Dg6ng3nyv`6}@@EOb}!DPS<tVR9H7^=XK2xhISF@
W3d6*ojmB7{CJj@lyNO^ydj_^YJ?hp{$0okGsCj^BD7f``j+f=N^*+0i)1}PwicJ$bYVH)AIb3^@t<y)RG}{iy(cnPN?h%0Eyu7I
1V2=GaNcD2U+CwVJlf1a2ju2IV`SWmPpf)Sg-|)x4YU!U@b@wgDJn3GIO5Q<kx-w}aVR3H%8CsPSS*|bujRAio6L=qJ@^|v0HKgS
&PTv*J@kY$uKFNj8+)q4!{cQJCf^oXcMMML(;}q4y^*qCNslObWX+(drzC}rM~QiAFK%7?Z;ch&kqOO_(l!x1l;5aHa;}FZ!CL{{
5zY$fJco(B*}l<rF#O;8u9I+>_79<sbw;JvEyJ45zm4q9?+O`#{aP$-(4zmT6+f;lzFQTzJExM{5kwmmW%Z7wXUjKhJ57q$X#F83
E2R7L5*bECyHAcm2%d`#*zP%M`S-9<k1biG-2NlY64Jl2r$`(IA1FJ$hk|}pTZ(dprqfHVF+6+Io`ffXL{6*9>yb7WQWt~{7`S~r
JR@I8U8v@CV+w${cFUfM^WFH9QR}iqIigH!-`%nnp=Cn~gQU90S=N4=mLnh0zscAXbq`njSINId<X+m4caQF=Z-Sz(WOdK)+5vy_
3{c=x3wxBYe0^4Bo7Tg6)39UUHh*2u-jEXc+{0Xb(DFnR^NU65)jr8Rf0JboLyyplm+30@%e05E$F5IJ$_Srsr6j~Zz{W_szV;<Z
0q$f7rlHMHBbvV^m{mICn@|>Q8}t6+Y5Ba?%im%6O$p%Qnk}*VgJ0W%U5U|posHAs6@K~{$@thS$CGkI8FMxQ9Geb`-^_MX?g-Y)
6;9v`q8Cf_Y$XJBty4g|%qghRrr67Evd$`}a(Vo1@mX8<+!w7ddYQr9N1g_f7>vZlPfT##(~VOuCpTS2t1bi7APCfLV8!ZK?AtTX
VdP(c8fA1^o4YnE(8QPHGxh3%^MOq5M4Eibx)8pJT*fh`Mct=LKJTJLk_hkq4!t(QpHK55>$L9hjR=dW5PNMS!6-n3GRJsXeh*kf
?3paL+K&akBpE;cI1T%oWMI<1MT{S{@5j>scyD$@KyDQYG@z$?MHlY5e<dm1pj~8Z*$||2M~*w}!?OE?n#iR-b|!3RGJ4utSmK?T
+$;?}|5;=vrAwNeLoMnn>f$Hj%Iy&OfC^df3i5a~>a{~F{n=tW`|uuRhkTvqp^0_d%q>hbpyayGkFJ*kGPn0_Te^+asC!S_N(yVY
x5&8M(Jj#1Z2o(pgs+B|dGWvEtTZhQ8r-pxIW_6&ZJ^06or|LX!H)F7^HJ?csIXGntVKfMzhpGdtQ%DyE5Av_IW|^)ItfXub-y1?
r2ztipa|$Lr&*%hHA3)llwP<fgZq%cs264+!dD;>V2g3Dlm8~F&UfsMrpLWsqxQy8HLs!q?sN$weQ72W-|6D=k*J19MJbJ$4M?OX
i_Cl=E{41ns)#knfUpaaPNG)Wbk@x9y8i1@YOSMF^=1$Lx4}f9)+lPEhbi{$P%)}>&1^7)k=-De`#Y!06BcvQAmsr3?#HFg;!4#B
3>-t1<1>`Wc|v>52?*!^q7&x6du@s=cU;Rk)kP8or2i?z;}(Smk|RNO`lckPGH|+S67a`(tvl>U`L0{Kn$2+RY&*#>sKJ4i0}mU!
Go2d?7zRs0I@vjMgYrV2l-&=LAqpxf#HJRGL%U;$v^3%M|LS_N*C3bF1*zyx`zoZ=7eW0BpR^;bhK|3`ggqG$@fyQq@JAP(;YDw*
0S<m}u3)}jbg^>&nfyLb0X}m6jk(#$q+evaZ5Ix%zAmBD9H?>;TRk=*h@$!?&W*bb-|sn@k<2kw-5ego@g6w5geNfYav@;xr@B-i
oiopU(-j2x#WL<i@GW?)>a?*SXuwuhJr%ZdF_X_+T~m7D53YG1Ts;?z@WZpxGX$gOhPD$!$0MSN>6|9o{G#{Ya0ZQ!^JYh7L=g`U
-;zjR?{B_szAy*&;K3HRK7B~<frXgs97UQPT|CJpF#Om9kZ-*mU&R0b00000ev+aE@?va}00HSkj;{g$*#+4EvBYQl0ssI200dcD
"""
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
b=''.join(B.split()).encode('ascii')
assert pin(b)==[10900, 'bffd392d3751bf90b8bca9eccd58c0b690719e1fe13345572f87a31431458f2e']
raw=lzma.decompress(base64.b85decode(b))
assert pin(raw)==[38798, 'c5b26fc7f75f6b0b31720f69c196679c051f1659884294136d987a7442071a6f']
M={'build217_broom.py': [2534, '0b5f7c0708cdb8720efe050651bf736f142cbc77327655ee5146192cd51f1fd8'], 'finish217_broom.py': [3031, '95f57f2585b0f409ba8c914627aa62bb58ba4ed4522e188e348d4c665dd9efb4'], 'assemble217_broom.py': [1279, '33218bc0d19cfc46373029a1cb5b9a16d26c2a0355fbb9afa9fcd600cfc33f62'], 'verify217_broom.py': [10689, '6cab2deaec9cc2a089f95d9f51130122728e95348896f478e44d13ded1400fe8'], 'reconstruct217_broom.py': [2575, '15e15ef54f8c51aa1a22d6fe8dc8953009d4ca965ebdd520473617ec5f834f06'], 'type217_broom_plan.json': [16396, '0c0900f3b842bded53401e6a438589e9a0aac63d9d9df6579859613dc85ca204']}
U={'engine.py': [5298, '682be4236a84ef58bb5162d8007c426b01af23166d5d1d84335e15aee47bbd35'], 'build_universal.py': [2305, 'cefe20bf1a481d0e2aa41598e1ee50a73c30c47f18f360fece390b710f3b3af3'], 'verify_universal.py': [8516, 'e20a18e5fe22e51000c9f6df2eac84fb9a619164f86df2da28513df282c7af8f'], 'broom_cases.py': [1659, '74de2c945c64b8244fcb17a0ab3d3a6bc69de27450bde72624b2beac3cad7df8'], 'build_quad10.py': [4166, '0d7238cd7caabf03dd63c9f44ab7e6d374a79eabda1b05892d1b5b6023e7667f'], 'verify_quad10.py': [12911, '3673cdd939555e37b44891ebe928743e99ee98ec435519cdddcf81497395e556'], 'coverage_quad10.py': [2239, '85cd99ba919aa606639e107c46a285a78e642b91e057a5a6f19dec2e577ebd16'], 'c32_catalogue.py': [7169, 'eb78c9ea5e89db65b791e8ac0298f0a21e6607e97c05cd32be8ecee6e8317d20'], 'verify_c32.py': [3133, '0ccbfb67b413046531801adef23567e2f791396070c3976ad70f201b912570ff']}
D={'c32_catalogue.json': [240929, 'efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d'], 'universal285.json': [1289123, '3a00b679c994255debd3acbe5d3230e336d1e292b9cf88507dc1d2c61fc94496'], 'universal285_verification.json': [41790, '067c8ae69857aece263ccaeb5b1e05e4d401d90f13f5d8ee8d64e3847358acec'], 'quad10_exact.json': [1440946, '2505c724d0d35323d2d67058e32ed1e3af96620c8802d5f3723b21589341334c'], 'quad10_complement.json': [161440, '4a7a7d33f0803cd2496a974933490eb29cca5419947d334c552728ab4d186541'], 'quad10_verification.json': [5815, 'ad0e56bc37cb39281e5392b3573d2d0c05d5d52976602cb80ff4d372cf193449'], 'type217_broom_exact.json': [359444, '6ee902854e04f73217d507ac2d701d0cb22f8bd66e1c81c86f82a19adaaa4a0f'], 'type217_broom_verification.json': [3733, 'e842290e4de81ec042466cfe4988ba0294869a445441c3e4c1a8876e66986fd0']}
S=json.loads(raw);assert set(S)==set(M)
for name,text in S.items():
    b=text.encode('utf-8');assert pin(b)==M[name],name
    Path(name).write_bytes(b)
mode=sys.argv[1]if len(sys.argv)>1 else'all'
assert mode in('all','check','extract')
if mode=='extract':
    print('SIX_COMPLETE_217_SOURCES_AND_PLAN_RECOVERED_NO_MATHEMATICAL_REPLAY')
    sys.exit(0)
for name,want in U.items():assert pin(Path(name).read_bytes())==want,name
for name,want in D.items():
    if not name.startswith('type217_'):assert pin(Path(name).read_bytes())==want,name
def run(args):
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    subprocess.run([sys.executable]+args,env=env,check=True)
if mode=='all':run(['reconstruct217_broom.py'])
assert pin(Path('type217_broom_exact.json').read_bytes())==D['type217_broom_exact.json']
run(['-S','verify217_broom.py'])
for name,want in dict(U,**M,**D).items():assert pin(Path(name).read_bytes())==want,name
print('ALL_217_ADDITIONAL_AND_UPSTREAM_INPUT_OUTPUT_PINS_PASS')
print('C32_CANONICAL217_BROOM_REDUCTION_V1_COMPLETE_DURABLE_RECOVERY_PASS')
