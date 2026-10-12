"""Complete literal exact construction, Python standard library only.
Run: python -S EXACT_BODY.py OUTPUT_DIRECTORY
The compressed capsule contains every raw coordinate and oriented triangle.
The ordinary volume centroid is computed, not selected independently.
"""
import base64,zlib,hashlib,math,gzip,json,sys
from pathlib import Path
PAYLOAD = """
c-l>O30zy(mG?XMy{9L5!or3ar8t4so<d7vJFzo%Yj>Q+o;csw)AXC9lgzLACh4@lCi68j$+T&cHknp{5StL2*u*A4fB*qP2oN9;h)rVO4Pp~w6FXuNJA6+#
>3sZty6@h5&OPVcv)upTCl9Z`#OE&tmrY*GK;U4nCQfdI={Oia{7+bhXj^M1wu43kT_ht}3#i$2H29mn)R6q=>f7@|gkWo_R{QN)wxva&+>b9N+siYn>`0^;
wxzNhgS+|ZR9J3rx*ZzQyX*#6&0brt8rm~O$|$0~A}_KPt&GLA8eHNMLPK1|hKA#gi=z76_H=SKFt1ohrIn{_AG0^Db#c4UkR4o+>((jhnO3lBrfc|F=kofe
67q3nZpT0scQSV}u9R}5nNu^tP!YbH2thp)n|4lrL3-NvbSKqA2`DdhV?XS?P`R-=P9$b&Es5XSNQs)c>Ie=Jjk|0*YHDVoUML<fM(s&m!He9bM2%kRV(XiT
?0i;y+_8OtHlr%nBZ#zxu3;%|RI0Q#vQlcPjvz$cTKo8Sh5H+2_4x4I(##-x&1^l5Ar5jiO)bRmNEyGub4_5;XMl00X?>1Rm-WvUxg~cNNXB@r%h`QXxTJ45
u!4#Ssaccb!b8hmtcz}Od*a>Rj!ezbb8C6)@tZ8;T3CIJpRsA!FaVZCM{YE%Oh{$%grw41WAc^>i}zD0g}5cA<2&6wvfVj!Fwrn4CUl1CqfE$ChM$g5{J3aS
$G3YIrx)cc$5wRn5<2MY&Tb_8`wB-Cu0hKcibj{bw#e!!y8dKAGJVmZ<L751(Rxir+_NR}^2mLTw8px+LPyk=rB9N*lE|Hm=WNw2NeVQ)l4{)cloaU9{v~S`
UDNk#RGZdz_IzSwgPM{lsuLnuVNu4O6FexTa7{+^ZdIPX=P;K~E_qu_VY4UayZaqamY=H`oD)>Khc!%eZoBEs-D#s#f4M=Jg!9WZ)xFPWtK+)bTuS-}4oaU(
?zHneQQ>CK%+Lk??nu-csf$&g@ShRwowTNXJEF`u*G6vkR=4hR#v4U-1)Pl<O;MZ+U$PNh<<UDSk!3#9S`uQYK4%`@uZ?5HXcCt@ILWoO4WphmWyyN}^Oo#^
@mRJjQyX@|PK%dJHUCJSrZS}yim1f0vR6u)!$XtKAH?n-rg`-TZFW_<p7b@O#s6R<b+p#bl_sfFOTKxct)`=A)&j$7>fHLbri3Z3+k3@|8mj&1AV_^aY<Jw4
?iVprV$8-j6t<p2BsQow^IWZaI?EEZ7us!z$HN+$#)n?C#B>DiKhqwp=*_&AH#8rTb)nuAn=$+RQRl??CTnvxB0u?@AiF9u$t_!%X<nt9`HtOKu3(}{P>U;0
v-Jg+N)E<Kbre6zIBR!J+nl%exyboj0y8^1D0;T~2i+r0yQg?(f^1QS#{?EDBc91qlsm@1m6#{B*eGk$(f$#gS7qQ^Kohx{b>wzbZOO@HZ>$S)0)a1g$kZHj
OL2TEYArGMB@nGyQNw1>{+Ufp=Swz8<dMu*RyH{u#Fi_cSPGwsGub*#=PDPb6mi_6v`EeHxr_|EXvlTAYPK>2loECDIF+Ue8EPgq5jzJ;m*lar0>#Ddy`|ng
QfP}98{o)SiZ$`>oAHMWZMZ^SmbT2K65pHwD-}V9F+BOvhTP$5I4N3hIalAlAnJA#>t|a|&&@8X9c`?mUPDNcYj1Ew3`@JTn)&aF&Li<}dsB+V?R3df-HC;F
po&Tzzi3&Dly*@ktJc^PT)os`S|x;$>0$HGA0t<cqCstPHr2XeGldf7spd|*izKQcvJ}j{HnI2GuIV&{FjP)y5^1%yWhjf)YOzO4U`?KoDRkAf1q%wjbm_WP
ty}Zr%))C20^!128x1ncbG=pN#aho!vEj&oHs<oCl2F5LZRQiCiENyUCI**-mL>S0cEl0xI-eu!S8^Q2zCIhLCN3zcg3{#IHjJ^A{CPz^ib$SYjel9SuMJ*)
X{kG5vGT?K<nj2^7mh4NS*I@?JW1SBzc>=1t82er5?ZpVyegkLK90F6I?a%+UKQ8u>gsRgNv5L1U(9x-SQUPnkmbR`??i-0_J#Shj%{s<pOq{7l-<u56L<2q
&(Eh@BG<hfkq*c1vy%1v*aR<SZpy08tFXS?vhloay(O*VTT6>w<``FN<3zBP?hhPo(s+n=iULRIn7Md<7ALPouNk6ryQ0!XcK^_}#KBT^90>A=!o|_zPF%RL
T2+EeGq&4jkYpizF_8=!I*l>;l`dI3QdW@66cWDH16|2oDP;qAzh*RUs)U#s3Y<=UYcw)(dR2(z(z+FWJk*Ux%_N24z3Z952eD9k6v4Nafg#prJ^oK=YFB#M
GzwW2j&A*@A~$2K(RZO}uIoUKr_UwNnE!^qpE^F!M;_0QAC>hGL5bU2E5Z13;>xkCf{@HgbJzG}aO7Zmm6}xBGKQ8`$zn~zYE2Q#5u7uxmw>c3f4)@;+v}#*
#4eOOo!BF-B6W>>meqWeWNIJn7(jgGkaQsw1<%AK7&WLlVmUjSPo$2|Z0+k|vD`FLwTwzEw%zJ}vO^N9u$ALu;<zG73+islj<5>xRApyMVIjUJuPsZeMk&Yg
6!mu&5(TZA8q}R=Sq$$XHQJ^_y%Zm+9ZDDwyT~&8=9NR}FhRbn*+oKa{8V}xVY2Gu1wzzOJ~${gprG*1Recv(Al!dqsz+<eprT>{b*Nn1uQR%)o2J@So=2sJ
v#Kz(DGXI7zfs(BxEwQw+SiN4y;f46X*Luek?r-%mZ>AOvQSlP+M=4;g6b=4*dy!J?PW74E<9x1rY8Gjn&LS=Eo$166;D9-dX9DS&neaWGm;2gnv<4RxPj96
iP8`YvIs^GXS2w<K;2SqHhr{uY80#><Miq19GS3bY#+ThGrBL!wIe31k+B(cU$i1<NX-sA%@|+&ND`br6L%>*DOVd5PdFArgC%>YWYbod^lo!Qrm0;+?I!PT
8dKRRt$C%2P<$*_Xef3YvuJY$-0Mww3DrVe)R#K8u|pN)nbe2-RBlUlT~;=pJtOKHE+AtZ21{5wS!ZgF9A2SJlY7adN<8Q&wzabe-<9Olq+hXA374yHDz+DF
wkaftOgSCz2EJG~KO2N+?ko?g)98(@<keOY&exi2Lcc4k);mf9cIC3<EzS)8WM=h!qcAsB(?hj5G6!1@TsMQHW1Ho8NS-;egWVj_ICJuY-4xNLLP(TE<Swi>
;=+-G)RH*p(wp*ap<vI+O6(iM!y`Kl`)(&Itrh%MTptu@R`uWqNjqhY2l!mUPT0XQo|_sQH$%>@SPv2!(R5N+pS2yuR78ZQ81eS*v4WPzWzpKi;cQ|%E!>nA
N6ZcdMyr38l|Q5^+#-f@+m<w(<R_W=l6kzv_(Wmbz?1EzHZ7kJIAp8x*G;zQf{`9#VkdU%h^0Lg4X$a4(Vn@<<$A&(YK)v&AnMwiBr*Rmzn;8%@M_Lxe$T3v
Xcgz_6D&kyO-zSlj;NU|U3bXIPNU3zc<efnS2gk^f|KziG){GhcSw_~rNj8tNVzCVPlyi(8-wD>t`MnlB94@ZP4!zsGF!ZGIPa=$Kdj6B!Q7K<OH~`Wz1dq=
DC9Inj;F8jSviK<#KeDBYXuU!-@uIYI8jd)R*#Egcib|~=A-^DT;Gr<tC}LTds`s|qojS-uo9vs2iA5~$~(d()lgq8YD~!MPgzGy=QGtPfb=#;_Q(z?9UoaS
*;%TDmekn_Vt;*NJtdo#+E(-1$2pd+gj~ay_N=|CzEmPN_V~1>$|bINBTaQg2G7qf+a2VHcDAa3V^CF2l`NmjoGg}B{CdAcEos<st6VG()y7ln`<Y8E5tL>&
xwc<IS7g~5l0<aFMpJ63o{DRqw&zSkRH`X;BnWkk%I13$C~^3zy}W~a*c2EgZRB<rw+w1BsoKbhN}Ys?kROYqLpgj=Nnm~}%pH%H#RZc+vjdd|9b354B`vF<
__~TX{f%5n>568AQU~SEPad-55jCNaLMlmHI3`(yw(_|By;w--iHM2Zb3Iv_jGnMjy+h?|TfZ*bj_Fs_v*+W~mBCSL`BqtB={l@5HKacYLCaP1*3@;np-ta?
TIJH)m($zG$NAgAs{DG0E-a}D6Ob`ub0V<}_=W4^A|akxDagtQI80n9<d1_gtD;g-jPmR1HdhPWWQhYQiN$QKrLnj&n+(daPH(<cWnalEwYd%JCUfg`ZUb8r
8k-Dh#!hPwnjkVSWp{2Hjw&0)q6&O=sC%#KT#jY0Am#+pqqX^21!%4OxN12LPns>AUO(k%r#3sYgE*>n_0h;Ml=e81Y9CgZl4t6NVR}2Gb1jQ*PD!rVdtR3A
*oyu3c;iZ)$akf?!zldDTKc{?_e#w|kiPW0YWq^v%J<dAqZ(DfimEwRbu}$DVxZ_{!H~SE=!bhDRf4r!5j}iS(oI2@B_{6rN<pTe`f7<{@~Fdae!x(Be0j}W
q{;A^73&?f0hP)5)uS(&Pj-r0u62es_2u8l6AFqZ9xhpzl(P@k<~94tmy*{f8a3b9F72My{pcvmU{Cv=MKL<saJ9d+r*76~(w-wJ^@|u9I-2_S@JxJR;YDRj
xk%!9pxCi)dFTd3<yq&Y(}s|^?@SIVgIn`Z%EIz;{F1A=Z?!e#`3i$nBDuO78(7fwnLevyzyx7IYn?;i*KeD;4bK${gP-($T0L&9TDrYiSUOzz`ZCkhmt4<X
O;8TJlQ*|qk$gcqFEkC>&ewJoW-hO~SN4zb8|fOkIk0T}V)29^b-a(e)ES!=+RAN->J1F<xF|Ep24^NN_SLVKM|WSWVOllO<i&F9P~2Sa#hv-eO!LpXRTcIT
rv2M*nO$6QNm*W4XzRPU5*}v|=W}MJ&0AY(oIFF<Kv*apk~a~!z3X~n8y${I@fbQuZ<a-|B4vR!ieR_2&e4+Lo{Pc7o#IV7J#bt$(~?4OR}Clw+ug$FhF1&p
Zv2$>;KMD~Jn3Ra+m%{=^o}isRtX)o)jb!@e0|>B8@0WK>f&H8YrkW}Cgnu04bS$*b4J@W6Nfu!yR+%o*y*+~5*cLcaLw4(tp}<urc^F84UMv8+4)VfK9_={
s+@&<uVkriwbHXN(-5paV)u`&6~)%0miQCpsfHd*YTX*wUThPN#Ad254(>!0)oVG2j@HUK-T9y=mUy+^ooS|b>lR%nRGGc9I&W!1wfr!HbVM#!4v$dV3%Pkw
Aw+dlM!v~JCuSTJR@-UopmDcG@4C8Baj+J9sd-`UsAH3?8EBi&uA~L6MpgGGDSgc?9b=FnDUew!T>B1X83TDNt0rr2y7_$SR!Y)>{v3a1DA!hXVQfLuD-m;t
JLF}ho%BZdoT68cmJ8PUXSzKHn}!0z!!I0$9n4f$(5+InT1@Ymi%mOJW$R4slAMm-77XuXUD)ni3~N}puyvepkYS;Fm&%X%3m5cDOJ)7X&vpt2NA<@SLc2#p
1cUTsdaY?>mtL&g?wq`)uotUCs$gSKa#Gd8R#&GD>m#7JBE2<1^t@cNJQp-Z)sKXy@dsVoGaTh7a!6B6M2yH_f1@-n6P>Qdgc=i2@rFLSyyt?vN;EXIOyy<g
@9d=0agC|#6E4QnHD!A><cBUs7qxSQQG&R!blRL%6Jl?}qt*SjQ8D;od|#)ihc>PXBGhg&>&#$&6rHkHJKi2hiwkQ@!z7%=w5^@V1dck&Ryjxr4%Io;M^u6;
?=*FXYJal7F4}V4n92{Hv_MEyglXBp8IBChm{W2ri%Z5W8|Z_QTerf`h0V*dO&r_a)MVD7YwA>}NxkZ-3mZ%?E})f-#o?kVsFpu5wD)n0dR6xUr(JHYsXU<@
?XmXhbvmY-pD@tDu?r$Il8ZssnLf}XfyMdw1a&T_UOT6rmvV;eMa3Z@9Ba$0Fk0x=I2mCQNS<-nqBpwC7se|Ns>OC{H6zK`BBMfAW<nJa^uc(hFjUFukY!hw
By*Oun%c&BdblfN_?YTXY)Di8$HZwwP;@(IduV%n({Uliau^fYMNSEWRV_WB8&b}v{zJ%Kcj>g4Q#;dHAX=pO{h0+RC(lNe)t8ngvD!9_aSNjt2IT_&&h~|g
mDQs9k0s#?3TZHrqimcW*dWZE2_cRrFt)YTwz)u8CbS;KX1OU_(gk5f#OT68RzuVITwQ(NLOP|A3?7U`Kbut`b)?mMt(ZdFWCP^V{9brkGd-GM)NSf$!(c}4
qU)@6yt!9#K4hk)tF@KaT~ZRAUq&T2GN7vBlowcLq7|GuWk|g~mK77bcbb~SGS?PmkGFBG(w(J&MF^eV?zLp1=-Qx=b`dA9)P7(nb+1;%l>`^Khh-cj%&gGI
_VR+_d3xxuIiWI(HNX#(?%q&HQ~Kv^9+^VJT1=E%f3z`LI!f#GIiX?S?~<1ehaS?3<oVe+hik!NL_}}?`R&8}g_GoGQj_<}Y_A=fb&Zbnb9+g0d$*NNTy3=$
yxldFVc9L=XjMgK0h5_=6H28POo>Ci`>hvR<L0KrO=O;3AW-yhmWL#U-s}sr>2cec0?*ii{PN`t6cl-++WYlM`O(~n6q-6V5*KGZmWG8fPkt27;9>0FZB~sf
Rg97I`$-{+8aioPrF#;7UNv8rF?vC>zJAczPMYhqQMo#|<Ky1tmN&bH3zOIXE+j*nRP=G7Idu2<H+3Pq^7XC@^O}_%t9M-Cgmp=9zHon{d^Q%=t<zaMfo|H4
wzc^V&gOy8QR$ttTh&%Ie%{Ql64ZyDpNUttRs?Z2*Tv#R_ZqQdz{pkF9ZMbOmNI9;!rcs6G1@53O32jUgxi{Outs-&Z6vjL=)62?H6+~Ks?E$=;u@BA8@D_Y
_j@v$xSh*AIq~P_gW}4boZFsoXy-W1($>IAdSrZXI^AV9L%40E%;LD!I+uv3SW_F_JiXLB?Xr1rT$SQ#8`PT*-3@8=O|j?3Q}wM4teVb{jWjB;K{D>(%$Ij2
6|-x4G%1O$o8qyNCTe6YA|shSKA;YZp%m@QxmH&9>fC{ju=Ne{8;G>ARil|`*G|-CveldGVW~eHXX$YTo{z`D`3{(eHYCFDa|C!F@lZ=t!22VhLIY3+`6TCv
FvE+1C>mXFgjSZGWyRn4$5^757(zb_xSmYz68=GugFDENG6^CFHKX?_J`6z(Sws;L#3+t?tKr^#A^x(0*hk^$4;n_U_p7&a(HcRlvczOGP_IltGP=X|E`$d+
2VosXSvR%N0S37DPaXnvO9e&575WkWLtYFU?_;xEq?E4!4&fBIB~Xqe$j^bM;B5hvlksQ`J>Zpq0<m*(N&;Iz-#tKC<UJxCEELrQ%Wwnl!rASl%O2Vxc$pwV
*KXvXzo`bwMkGTW)S=5>A4NhZx<*|~1y2Hb(Z6-SVZoDtHH1D-B&*S5_Oq}4`FqKbz`DFawvma1UjgoI#nXW2l?v{}=RW>E57_L_;(@yIrU2cvK?~t~c?bD>
P&UX$BFF)*2>xXmRkGTkACe#qIQS}y_K=c#!2gwZB^0@Lp}*(y*lXyOk9mIFM=gkG#oHhYF5Tl19udU-UEH0b=`hw;oEfk{D3J#7@Wp5EaFswW5)Zs?d+}~i
+)M2USAe@u8~MZUd9i)N2=^;hgu5DN|3w8}@BHA_EnXu2j(-dUJPHGUcmF8r1pU!F9dQWihm?_ZyO`vo`!58-ZQivnWhmgz^;WpfN1nk@igVQ<hiI6^yPy?f
!Q;LS*d}0K%7+!8cY%*S6oDQ-{OKTLRt&Te9^5Z2gbY6X^y+h*Bou<<*Ssqr22oz`wiBU@Lq3~9L%64f+y!cw@y0QELx#NA0w_j$_*NW~OJD4R`~3#SRqij~
86<wQ8-fx0)mxv^<#1&i0(=Vye}B*W-}1k+jqZe@eDv5W6ZcyOns+&j{Cy(`kbgJh^)&GK#jn0gq!TwEygvpSc*8dyJh<Fo;QXG)CJx9qR^elxFvRIVeYm@T
oW{LwQYx|>)^T@_yY~w5M94>!64en6!1J_#XEEt5fWOdQHKYxQe7L)SQ=XhE{55y#Ch>@O$>W^2h3bOK1L*T@XkgM=2e~Z5$K!<{f*qg)zfT_b!voJ>+z=tW
1BzHmu(E35iZf;Xo1qqYzc0Y6Sj30EYrrc42l13o1iS^fb192#X2L_Y;WzwgulsM__M!ZKdqso4^SA%%oeX8T4yH)zae$|QWdsz$zQTU%HgN=x{Q^9H$Y$Sv
m-6J}*TJ6`&bpk<`ivcl7I3dz<ik-iS%2Mwe$04?7YKxciSVmA5C)O(?)$U_r|>6G1z(Jz2bbRAS%KXET_o@Fwf8*k-e8x&+qb-wi0h?+ci8MA6o!JC2j$jR
msg+`JiR&r4=3F{7;)$>m*58YdpznV{#fUXOdW9>r<(C(@X;c?7QA^D=pfxMb;3h09iD@Z;MF2jK=}H%z{~zz2mWTjy|3_BdE7Mc;y4for<0%xe|&?sA}z3M
sVhD-&o`0v_k5HCVz9G#w|{xVm*yk)`&<XQ9SNK<<l%pV`}l^9jD%Z$2E^Q|jVuC%vw|EXj=Q(PjqBm$pZ-1`_|zD1n!yCkz~vMXK7=RTjVwR~!}TA}11}4v
39dJfkM4TD{Q-XCK@sDrW5W0PdpB;duQ&)5aEK&EYBk|aUw8NOymx(#++u12Z$p3HfMxRL9lyI#@QFJw4rd1p;jVo0${yU!NAEb`)fiwiuK2JOdf?MLk5u6P
(8sd~{C`9l!RP0B!1*K%e1qYmb-2<D*INh!jKQ71>_IcZ9zYL*2_McH3qORLfAc0I5`U=_DNq;jqSqT^kOJ=4SQjV`+lOj^2kSt1MzBknQYZoy44~V-SGJf8
iw6OCvVY!-h+>NUtG9f(IG64vn9K{fRK$=MahFCQHsJlwZ}Q&o^hpMsrf+*ZzM~;iP(O-?pShO9Jjy|{aObOLIL6<KVO8J(D%8mco?v3j-Jt&64sY1ebrZA`
9fTSGAYhp=;vvlA%kw-UN{P?SkcuZVdAZ9xBS}buPXXP_6yFM~gG~<NS-3Z+m8oX|9Kf$vP&Jx^VfZQ6<NBp8R7iF}8M#5co)51)_rZN{Is<+9Km;F_u|5q3
ZyUJ4Jry!CDDVW)UboOs>0~yik?q4uBh&CtJf@J>pMUpw8G`T;U`Ij{^E#>V4<D@I>{9gK5~dD*cb5>OBEsz+QN!}SUXDM!eT?(k$w~NZl(-+tppGBA1JMf%
a%JPhi=)Wvqk!Mdq5x_Je7O&POtb%V<Ew2{4lo1%XNj!F*^iX)M+v+YgC<y<W~zs>5|>wT%8Ii+W#9yp-%z|;Z?pAGba3vq7ewe1XAWH^%J9b&EkZ$v?Z@?f
y%ZOd-v2BIn&2F>JbbfBKRx^##ajnX3wnj}WG|t82t&TtKlGbJo<U3khvRJAhwXlX+aQU>3!vSN<aGg1Paq#Yr#|}lA-#=i!9)c7%8T+~V8m06l9|xS!99n3
<`uRtS3z9i9pZ1bqc3iIdENT&yYKk65~pze?cdzfg1f)_F{=`f1*#FTImGv0Qd3`bu`EFU^cOr%6}&eNUbi@A@VPER>`cO=6-9%`2A&I2xUdc{Fg0U`6NmzT
e1QSBUHE|b@TadP14T>`+%I)7jz81_70o1U6)2&Fy!qzMpMB=#?tXyyi2Y?KD!|=GaOy25SS}K5J_9Yk<HIWQErOrixL*M`=`TKXzd}TiH!syN2yz5(bujq!
%iEz$6Y%JTY24HQK7KXelAL+HI)Lky$)p_b5NI!skT?SoP7VD2-{^DS=W+^&Fz~tT{nlOPESF3FhWC3mac_zB=CcpJeBn_83S=?uQ9AD7^{E#Bo(U%?o_{y`
J%b&Dod`pozp)?{?6asVALRfQM@2He{qVCMg68>T;{U|K-x0ty`c<!I+#TfQO(qb;ryS-9C}UBCw?`!r;OQO)kFE&OJ4aBB?ouOwcd(McK@qiZhe3`=25H`Z
<7N@@@WC&8(T^FBKjVo;y>KO-xmg`GLQ%WS^)K<R-T&w>407;ZXYk-}U-QwzmtBZgL_GEi;8`e?3$-k^mxtf&PUPoBQ~%87c;BXI9o`EC3?iXGf{;>QMlvtj
DM{5K20W5r8)s?&USQjC-lLa1y?ROScwiI1`tsv1HsA@&LOFv>P3Y3SYrG&NW72Jvc{=D<ecpVRIDuPUxDL_W>mNVl{=63O5%jLl1CFN(C_QvSEJ;wW`pp2>
)0e*H`^(!h{0uudu>_yFu-6FAv~Ch6YdKsC5PI@b0Mp`pu#N8d$0P1O?!*q>&CA*N11EYInG-y23~=TV!O3@aGQ<s<E+Lra>y%`>-}`_bC*Kpp#cG%)J$d)O
2nG*1y3eI5aX;=`waDYrqf0n7OI%h#6NnLq%Q<CvGU#>5N>a?Dt!4188zx8wKR#$C82BJua6NEm5Zi}Cl@L$hZ4soyd(X;&7tg{y18nF`Ir#f>*hCxn+i{%1
kN4d#Ww4%t$Hx^6!rt^^aK@vMLGU)ziRi0rJ?TeNevRPHd!ru(T-n0O67nf__=`~tFp1E>r0!3D;{VC#_l)3w--q+b^_Me&di>Q7eihBMK`#*0`=Lz7P4A*i
`1TOfnA~Y5qn%lgrf`m@ncy?|Z)7@Qrnzckyg$bP2z!8d`1&YQbrmQ8xw_+Q+M94!GBNZVfgqBtU=V8;-udc&6|lc@fAj4lAa<dSWb?Q_xVM~14JE;ofV-C$
v5UX#*8viye|*e)qyQhzS1;V+z55oAD<dD)!vuQmpBKOkS!fvD!bHRziCM@j{I(V~0k#Ew1hz;0=)WqM{^({G7+AH;KO?VU`@|rz54nJ0<Ak2T`k@VvU}L*D
wuNi(0l-Ai2a~KRHr9>X5r+K)!xGUSWGDs7kQsb2412GFdFQb@a)fllj^XMc3dS+)fRT4M4T{)UGc&_nFclI2R!(5pBkXld&c^!K2peSHHq5E&HHPJc5ssCT
3m|2V4>P}5=J!hs+e8T@Ln&mA7BSpW1a?AJ!e`S2*2X{vhSf3zY>>p#Vbm$%6CE=$e#Ee6FzgQ)CPEllfv|ouf#Dl*+9HM&7Pd#~$v6TFConUPDV*DkgP6hH
Ib#%WGm92RQm#`bRzqOr%*Ic0@L?8q(YdqF!Y~74*Z;+^F`VK0-^|_``VS}RZX?1raV!vbE-*2U4V=wpS<Z2nk#~vt8WCo9UJJW&CjX41lzjPrF`s6}&`c%}
XL~<)?x@d<IQvT><M0H)ik|MM*jO2h&&>bp8@l-HR1?BV7<-rSuXpW$eQ>7ecV167GM$tL=Wx>-!$O=c{PDZY5aF~b5--59afWCH?3ln}oNU!7<jhH<@U_T!
hI5ixG<~yyO`O@pEH%u8KGPBJ+)_BDV}@_|&Xj%gmk-!4oEKzaSqxppu*b46IXU4}DIu`XGhQoE?Ud7noY~ThW8u`<*)>w-lsQ10nf$G9L_UudGM>)IF^Q8J
d*)=}*E;7JIsf9E#Ivx2r&6#Pr|cpp!zOc}^2}wLGh<EEIKwlAe`6`;%zn$$<v(I=XOagQT{CBq#bVCx{|`^4@(Ju56D<}NK|NKM?xb#<9cH|Xy~1QB`L)GH
Cy8-Y$C&_U`qzC!a)toI!u}`zM(0}ebRBrcHS^a1JhlDIcO%Swl;~;2Y%v?j%vX0tE`Dk(*8fz-_|wy8#fSAcy^zfesZV_)KjWSH+L*H{>2@+Me{GMB{QANj
XN<#VV=7?j&V7M%#nj+g(LWXY)b|t4nG*l&mHwI#g-;b#{PprDXS1u=*4cN+sXvi9x6D-RQ=a~>@16_)UrznnIh^~Sb<tB*vraWhj8SIiS!dQ^5zMjmGwrMY
<KeS95uZ6A$tm{Q(+A<3R62|F*R$29k~0}L=5fQc-&pbg02HlBLj
"""
EXPECTED_STREAM_SHA256 = '8635b3ede16d4cef1ead64da8629a8c94f4f97f50fa4ffd6bf300bd3ca47eed1'
def construct(destination):
 raw=zlib.decompress(base64.b85decode(''.join(PAYLOAD.split())))
 assert hashlib.sha256(raw).hexdigest()==EXPECTED_STREAM_SHA256 and raw[:4]==b'NG01'
 cur=4
 def uint():
  nonlocal cur
  n=0;k=0
  while True:
   b=raw[cur];cur+=1;n|=(b&127)<<k
   if b<128:return n
   k+=7
 D,h,a,t=uint(),uint(),uint(),uint()
 def table(n):
  out=[[0,0,0] for _ in range(n)]
  for j in range(3):
   last=0
   for i in range(n):
    q=uint();last+=q//2 if q%2==0 else -(q//2)-1;out[i][j]=last
  return [tuple(p) for p in out]
 reps=table(h+a);I=sorted(reps[:h]+[(x,-y,-z) for x,y,z in reps[:h]]+reps[h:]);F=table(t);assert cur==len(raw)
 def det(a,b,c):return a[0]*(b[1]*c[2]-b[2]*c[1])+a[1]*(b[2]*c[0]-b[0]*c[2])+a[2]*(b[0]*c[1]-b[1]*c[0])
 V6=0;M24=[0,0,0]
 for i,j,k in F:
  d=det(I[i],I[j],I[k]);V6+=d
  for q in range(3):M24[q]+=d*(I[i][q]+I[j][q]+I[k][q])
 assert V6>0 and M24[1:]==[0,0]
 g=math.gcd(4*V6,*M24);C0=4*V6//g;B0=[x//g for x in M24];Q=D*C0
 P=[tuple(C0*p[j]-B0[j] for j in range(3)) for p in I]
 out=Path(destination);out.mkdir(parents=True,exist_ok=True)
 for name,rows in [('raw_vertices.csv.gz',I),('vertices.csv.gz',P),('triangles.csv.gz',F)]:
  txt=''.join(','.join(map(str,row))+'\n' for row in rows).encode();(out/name).write_bytes(gzip.compress(txt,mtime=0))
 definition=dict(raw_denominator=D,centred_denominator=str(Q),centroid_multiplier=str(C0),centroid_subtract=list(map(str,B0)),volume_numerator=str(V6),moment_numerators=list(map(str,M24)),literal_stream_sha256=EXPECTED_STREAM_SHA256)
 (out/'definition.json').write_text(json.dumps(definition,indent=2)+'\n')
 assert len(I)==573 and len(F)==1142 and D==100000000000000
 assert V6==849588708163932468424639279843994138590536
 assert M24==[-23339931433899394640026494473429689835978, 0, 0]
 print('EXACT_LITERAL_NO575_BALANCED573_VERIFIED_RECONSTRUCTION_PASS');return out
if __name__=='__main__':construct(sys.argv[1] if len(sys.argv)>1 else 'reconstructed')
