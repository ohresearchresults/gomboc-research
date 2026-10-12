"""Complete literal exact construction, Python standard library only.
Run: python -S EXACT_BODY.py OUTPUT_DIRECTORY
The compressed capsule contains every raw coordinate and oriented triangle.
The ordinary volume centroid is computed, not selected independently.
"""
import base64,zlib,hashlib,math,gzip,json,sys
from pathlib import Path
PAYLOAD = """
c-m#Vd0b=Hl_##dyhVDVq$;q%u1Xh9l~a{eIpuUYDNox;Rom{aO3F#xWB1R_*xi-
1ow&No9cS8}Nv7@JSRk<r5c`e<2uXlIV&4P^5FmDe*f$9f`zBVgGfz;HnP30j=fitX_uYH$x#xV(Ip6aKzqtSM4@9B`apA<XMg)#MQer2Z!3I7@6!Pz!KVOc
3E=3_~>&V`yMP)OE&U`x9+2PcoohiT2XOa!24Y{y3vuUrNE(k2F=)$`ZMuQk7=S20DLhXP(E{fMX5H&JME-
M4FLV>X*B6*QNW;)K#_E_v#Zi(eNreo6ouB~t_UPFflsnxo3%9vG`2^n4fM@nJE(M0?{=m?1$wQ{GH*B2+4*zB;}A!wM$%q#(+QTb&Da44mJYKk0)YuK#Diz
9u5{&=T*dGwe+rH?$GBD++6v*XlA)KvBUg|Vfi={(9(l@R!AV`61V+_SSg_V{IxXr3CF2APW^^Qz|tN-
7RSXkKC1h$HrEr#qS{gCXrC07Vzp7mb6^u$J5coIaD+F268et*wZ9W+K24ZRI-sDwkxGv3_yqZtYCo(x&HBUi$77Xr32av$*r7jLJqjS8EMw1skrC&CK(?X<
^Ml^iF!XR)$206S_{SFUzk?MJSxPGy8;7H#6Q33{6wJwX`g2bVmM+HnAm0Mh%_lV;ax(no_gEL6vi|v5=eFaZp@K_G)d((I~cMYPXO~4pJNYh~@m{4KbS4)>
#`aEH~;4LMZd5t6-
a)5ACflg}Z(c2T2#Y<Qpq_WYJ<yQ9jpxqMeGsrmilz26QBc+ANeJbu!Ay7xm<oHG4WwwhELy`<Q%}XVDx+ydw&(Oqs=7>r;geRG>AgOyt14YOx#Z<MY#kg!a
zkup!=V!eGeux!?_T;9th?wyaGG8*<E=V@eiVJ5os(?6~xG*k3ZSSIE`x^{Dkwv^c#mPZ;Zuc0|0b+~pB}YT3M(u0(p9TH>Phii6R4;LK~QzN<-
Vi5&uo`HF^dQq$~gpW}yChaBipx}@(oUf}Gpn?uhP>4MV!C9$rnxti*5bi}uV(5>yMHo9%B%TkBqH!IdQpk7+6%qN^Ff$JZ2Xa<U_3DbUWNIeQJ3oX<^O~i8
V$~jAL%}6INx!p0Bh$7lz3wrpw6_H)B(3rm>uHsuNjQPE^WvN4DqeZ&CL^+g|r|u2|{rXJ2l6JN@#uBk{v~x6_v@2rP`zcXl(oPCx@88z;A!olhB7<ki%Gj8
o^xDWu3tz8wND_f)esK98Wr+i$7E0e)Ya2y@5@lSLN7YF}Q7~m0YU|sgj0s}@B517jx0*flQEd^UP~;j4UnOKyHHF1o<9d}z_PlYbVP8gCin5PFNJ~&sO&~v
dAt_}O7f6-KzmNsSE{7qfGoW*Uai+H|TcEKgOOpcab3qX~q-
fM874wW+BlcpRY|LaS<|$^IT|Umb<%JID+*bvSP_n&2RU9;~I8$SwtTD{khb^Ox@s*@#uQoJ~3U(yd?ZIHnL0&Icv0di>kz(yA$I4SU^XJmAQJ#~f;9B;qU5
h|eu&?ao$+WriiCCnVNp0lXGp%D$wEtTE;xa6ls_YI0vf-nxH0X5fuczM9*QLq|o>4fr7E{Rym9smHUhQfv7on}}VpA`7wx=MemYZ8s5?U-
&^i=q_G4_Rw(J0a=%iNqLjFD9*4mPU9sz~JAklGE<J|$ntAdJV$aUY8u1<pQFKW?_V1p11uk_AR4Kgu)_#^`xf3F)->JA+A4^yExB-
+0uN(#$t@m2ISx3d3?@7O7BAj|F+?W0!kE8GC8@>Io3(8<YQsGq5SSm@leRhXim%DQT6pShTPxI-
#A`A^SMCqy?#}38%|{=|`fB<&<=RKB7{Yz!jNS+x!T9r+P=uC?+>k<B_N)#4>-
*X|aoANoQ7~Eetv}^W6tf5ni&P;)%3Hvoc`u3)vqgo%Z&I7_>T;)Kv&G<BrzjkX~+xsszr^nx1$<re5!fKW~xC5<3}@q@;TUiy|dUy+XTROT3EEuSrs77+Ht
4xq`G$s8oK8v2e=X;bEz1oGZq%#jQ{~WofmF{?!<pv2W#CTyx=8u02{FoZx9OiGufmD5yF;opg@o)xM`t<!w2<WMK=Y8l<l;*pniKRz9-ASSpsL;-
SS)lF&%%5B!hINm;T%QjHWl;jMkxS&}#~@Qi+Ju)B(@4~^Q@VT-hUxt=tRPh}NCWwn2og3=cC)}%wdI<uvkG#;$fn=d$X*YgRPW-mL@N0D3BWj!aVXmp(*d$
VFefkdkt4%XMDH7)z+WdqUK6O{A#D9I_bNaf`b&^X+cR!Hch+Z)QErTTd9kg>$qi|oL;x|eb2VH_CB%BG!bk}N-9>FlrHftE7K-
~zB$7RL1xqS?ibLtu0S&FD$RiCWr!&R(#-
*+toxhjOx>)t9d%*gY&6WsYp2y>Bpc{+uPg#%~o^+Uy1;qbQu1^rxNWhQWGT)UlEhjf|qMiZOw4r_s+uI}Hv^v_O;^cbqPewTw4Nd9uQlvH&28DHe}W2Cbyu
L`XJVV|v1pb)0sHoIMq7eq3j0rcLExj~r?50O@@x_7kChZTn(4PhWAY7ek{fZ?K;<Zg-Sq0+Dhe-hxH3*@+g^JTzb0PaXEkRVzNL8+{?&=c12H8zztAetWr;
2~Il<-$WH<)jKVuWm4-
Hg!Yz*3@fEi+}eL4n~<#S0ey+V90z5a^WF74S;~N8AM49|dy_92ZIY!RkMx1{@kL&AUO{drOpP8Y^`~NMM#@A`mVUggf%<}i77gef94h?HaZ0-
7h_Rd$+iHPi{W$tXZOEd-37ip?l1X3>EgF}flf@gN|FhjS*YX`jc-
M5IS7!IFV~gmGD6j439m)$_@yIe#WBkmq=C_c_EU(o1*`c$0C#4d|)O%@RND(66i=#tT*7<cD-
P%`^M4POm+FZDEWHtRNS6@}dLSU^_*NH6kJ<YLjB&4V4je*Pxd(nlyiUI2}r9GH-
W)m`LL`MrxHtcHE!stR>i$6HtSXs@uI<y)Wy7XiFYV1PUOO8ENZq`+MiJ`jacDg(yGU|oc(7IaX?XER>X5?Q<YZA51FGgf*29K}qYb1VK-
!5rbD`~$HUpSi?ay_#=q`Tn7)QqgggUg8{t){MT1uI*IkDjk}4Y*w14caML#JS^y1#ys%%&#}%<hc!NmtEr>ub58SJ>T5fzL$4hxo+Rf6C@VdBd5-
(YShymq_iYrsGeD!%}eXxiz?crCp?9=V>q3T)eTIfP}<;VM+@m(RPQTD(N42|4apKW2GWS=(O&;ZBD1X8x&g}MYeDH)640H~iE^8pTMCeIuQu8al`FEM2^ed
rZMA=2w>Z_Fv<wxk0U@j1U~RmkV9bgXEoq{J^NJK(bk@&}1<7%eVBj>Qts7qx%?!k9Zj16avr;`}`$dw-
>$0|NXZk~9)bME6UD<qIb@I<`@{QGkU_u@pBvJU*B`!8LeY-9=dwS$Wd-
|TfzYSUD_p?hjL7hq#(lJCRHVi9fDG^y_8+EW}$jwNp>PGVUjFEu1Y}%6T`UG6)NKC2!x3uxV_Tv|fW1+dZ$Jn-
6JD$}IyB+B@Ez3}*jI6R|LdRa^=r|>Ak6)XZg7!Rz<RBid)I}PMX4o$_D)PNboYu^u9PI4vNDoy3U2>(|e-2vxi@PFzTQeLzSycv&@>$h%7aU8Buyy`*b-
yK~svN0GB4pdmP`uSVp&W;@@ty%?6|`sAv-)F^Z7aMr<A8A5HS(-+Xpb3e46Y#6O=-5GDsF4&eBtp6(X-~f95Wu=-
%>~dVd9EbRmfIvRfu)E38z%dj2xekx}BrR*<$1hYY7kc=|1cpS6ot9TBiqMVM+OHQo{Y#CTE!53A3_u((1ffr26HY5Zeh;Su4A+y>uixGYL)k4fo5W%*kx_o
=eU+Q`_=e=3)9_#Bt~*tj#FO9a0fT#=d}wWM(RNFDzmmRFzLm4*LO{|DsYVM%A^gOEu3Z4h`bK6KIqBo0DRZGO5XQPy%%)McXB{aCS^SZaOAT`uYpD0!g!Yd
^|wO40m=+>=!U?^V8FgU6|3IzZfA!=8?+6yjYZD%4r<FSGhE5&6tFH)$_}Hf@qgy(XSt=vg($4TBy>s#^i84U2IET&>TZ;&~~Cc5YIVACW903^!Sc=N#Hn+m
g=Wbz3Wh{{%EjuVY=mSo!V%PqnBQq35egxWVF&G@pcGGTTC0WN29d8-
GXCga&TaElB#VN*E9s7{Q9gO75k+zsJE9HQ!EVXqnMWX;x=<C6R4O>(q^Njk`4cbe;f>}H>dVMeZMw+*+6Wz&uaIZiIXn#uofq`#DzuAKx5WGa=3<;Pe*H;s
)?ngr96EBj9HK!C*`AQrzlQ>6K#zP#d@^2QMemYh17bhbDJJ1c4cWKXf$=zyd_2Jc|Ec$>_24b2+Kpgmfo4eS4KtSoyGGg*;pSX8zwF41kqv@9t@dI=!iwdI
kwKyAlkIHW{rqKYgLXFbu4Nh8J8YV@kLqdjs_IfCtH`bp*mOCU>#`=j%)2ZK-*(64Kgv-
jRx<kaMwX(XV^aKE^Ql@%D{N0dPU)cNm7O12HII0(Jp48x|%5Uga-
Lntu${P^86A;oZDh1G;pY}vjVA;8n$<8QA_Gta2c9#R*&{oqMV$>9%~(v^bg3Bcgebf-ow-
r7_JG>1stQekfXRFA}U&~T7&Uhx!K|dwCN~YOl(HOjhWV3qHAs?`pAasmb4isAwbqKI2bKPA$~zI2aDv%NOE~Ptjf@dii(iYQJ&u9X&qflk#`~M==kdM^Fwo
yQ`0CRWx#5gM-3CMW<@AWFEZ^6ZvnCGFvjGM)q8Qn5lFt}F3Mq(CEF25FOGLjbs@buJ5Tc~bz1gHR328;H&+z3L9w<bu)7_0#0*=yk|=RieA!qk<wyz$F?S-
r8m+k0f_lxxw!t(U6gb{jqrmOk`$-NM&=*k>3aU1WtgdmCom1Inw<Bxe-byE|GaOcZlk1pCm`}p8zBEJ5-w)R0=j?9cx{>Be-
=XYyW9|s58#&(7k#@N<q=K{zPDIwelCZaau#|~)iCL`=D*D=O^VQ_s)<|Sj9T_*Ashxr$BiZF!z?2wcO%KHNLGqUPV7zlM+bBKe_K(gkZq5+po2$#mNm%YzG
x$kn$b=%K2aBW9reb>WUU+;>8uZ)W$!`IfV<q!*CY)ogIm&Iu-KOq}f5<8gZ7v0kE2Bd?P_Ur$o2<e4wR0{>9j;$&TvLK$dvd!xh*lrwS<8cIO>=L_dgQsL3
WZe?buPEbR4G})VI}$~*)m>?&ni#I!mgZRb*d7_HUwrSI&i>HP<^KZ=M*pP1%QH{q4tnzT;4cq+MmYKPFH41CfVYUo%m&u`7<r?kD?|VvoGj1L*=1LB6x0DH
FeBO3K>1@3gNdFTS_;QuyW;KDJhorJ67bh^rOP6rft`y&CT7o)J#0D?kQ<1WUQsuhM__xp)g?XCF!I~8PQ0`ScZ++jda*ZMJ8b>2(`~g6Iq$*9mCN?U*xubz
m_+>)Of7d@?ukEhjIJV`a*Zd$R4$^ytr1|#h=MNoR96|s}!rE>_B2WJZQK!fN-wc4F9t%#Id7{Br1dTj_C-Zz_hZI(?Y})$V2v;2vL6BsAEB(D+!IxbD)sqI
#;qk89A0^8t^0c+xlmkt%8{}M@VHQPj<B4opLQZt<Y3cM>LEoN}}O@XKmETric6}!9RZ=i?V70MzlaY8du(w#gokR#BMecS<T^X6AeVH%M@CY!YE8#E3N5xJ
0)+_UM5hCrb@C=Ur)o}<`i*MFP;ths|`z_%uoS)nidq5<5X37Zb#AvPMa`gAFN<gMe?|7mEY7p*Bf+9=FH?oO})@mGf}2&BYHy?7guLVM~zFBSdM$D8p{R~8
5Z@cK~}!KGcLQ~tEQcqIsXn1m9^I<whPuI^|2{7Am7VMDYxK&;I4qMYP6Y?P}#Rigyux`lt=P&#`{K#g83!2>cdJ@R$M9z59f7fs5k3+(UEA)DJmjsOT!j)W
9Q@(`N^ff)Aed&MN*J$5I6RwkS%jLyCL=DNdBBz97r7;%iDU6N#n9KP8Y(QSaeNdKgQm@v^-Qqi6o-
z*(oq?arIA&VeR1V$y^)RT^|>o)8}EgEh>Ua_@cmqB8?PfIa;;{%LV$z+ThqYD&LtMv=mAeb+1YyYM8pDsK#g=VHpp$Dx8E!THvQ{25Uj%h0$UnNa+|AmDA?
f=DkWCW%tW<t^VbbByu~ogIbn%SF}`mL=NWHcAH6iWc|1;fGR&6Ihb4W7+T+NF#GXO>|-gbGSFS86BR@vQO9P}p_<Zl*9-
>NlS?Dwiu7u_D5@<i!y~kRL^gCtIYs5Ux;2n*w@xT*+}f3exzT*CMVcF%S`I~(M@t<+@MKf0SJ#5I=-
klBCS(bpl}0FlD1EVdbp#d%)g1Ts^ZRP*<?AAkx~`@6^dP8ME|L}-QFrT6e`pM-
J02ezJjBlO()_YaLax|T_gFyB;DIE|#uSYYM9fWkL`s^*Gfl`oWYxC*(U}rp*lz@i#EIRNkLpI+*bW%VUF{|7MZmthRvz04EIrPYvQku6FgdiBh!rK3J%ws4
m-
*+)j)6UXHhr!EL~bY|(tb5woLAbk#ZPZpQ0(q7{V|(j^&B(1m@5+1dg#_Nn&SqbNRd}C5&_pL)2C|(fUdE<U3JWxm55@8uOAmLwk7$__C`8uE`}Bwi<hs@XO
F~+E{%i+jfh?vD@YyH{%CPilC}4uWVE=(@f}g0c`xld#{B5wyzj~uETIQK5bZA+D}G=xWw=~76{hhLznk{MY)9$$>?ONt<JT0k1&e(?itf6d>KpdCtjggZ*!
6pPO}F&@w#?1%SgO*GVn5o?Sgnh^vJ;~&+55I7x;tY1f=p+xFZs4Uza}K(nrv>lrQ?cBG3U2@Q4upW-
u}EjY`AIvIhlNUbK*JKLf1~J&=Nn87VT|c3et*vEU}#y8&@_Plbidj(^eym^^(=>Pi=Y{BZG=F&O4V<+afPG$IZ3oGPt(Y-
r~2x)7v^TH(x9cZXR5H(6gBz9ZwE7PgVs!S6FV{a$L!et`3R!5Df)e<@$4b>tQX`hI8Zcm4r27yF21Ag9;lQ7_3A4DMy*A7Xodrmi+f(t5Pk8yufX#tDH*T7
;do$HY(Q-j$J}~fJj;>A$7S&>Zbi?%l6Y{DnIXlgIMj{lwelB+U;-%bVVhr-
aTvaCCVJ{*~a9R;Gab6(-+&Rz{8@&?Sp5d?6T?ob#C6VIH}-(zns+9z8lV1*3{Bj9XJ^e*RL1yjqOK~fvHSSa-GT&!l)u+TcgP_YevzS(o+>KUT?FYnef!or
E#uKqFhzPpcKQfD0!PZRvpm4qhl0R8LicNcydtOderA3D(bRzg)r-({?pA8W-4OIFCvG@)of%hHZyW<pTafuY<xy<#Bm`%xpF3TXP0-
BTiVr};jPTssVJoTHOA1?BRD(QS6goPDB2c9C%c%?gXrMA-&C91ouV$Tx++i<KjTr-
xDail0*B|rvUmma=^LftT*as}FRB)Xr1jKgHZkc7x|Uf=(!01>+Wo9cX-PQ>;;qf)7bltcIT^;Tq+MLny}cQ5jAv70_f?I|{O(%Fjvup77L}1YbTL9*Wr|KF
WF0fj{o_<$ty&cxfCCotCbZ*B?CgPYhT4!xGs=&cxcNDqWt)i)pByi);p!Hr4eBaxL`rspy#Cp=G<B=B_F0!z8|pVnShg$L17?WC5=Ci212dd45qea`<QkOK
?YVqiazj)5D5w@`2J_l@%}(k364`W^CqBwRN4oiV!!|UV0vod%&&ww_j<rh0f4m^PAXRWO<jVAm6U0tL2WqM1fGU+S?A%(&jK)$2yIn1P&4*xIwU!VaC0va;
NULZiMf)e&@wLpt){LgDk`YOoh9`)EzM9PmbSN*?)fX{)1<g5?`OLomT38=3J+%@vv`f}@)nsKHlg+_PC9`vke6`D_FM@La`YxHCtM4f&%v!im7c=aa>9}AC
Hi%=OGj*rZ;o{o%`!}3X=Pd<`uFbONZT^y^r79|>X0jk^oH1l)Dg&UwsOYjEGYe6*k+wZ%qI7C!8t<wmidH6gwy>1s=n<Z!bH~3L+O_%mz*@#BDkusl2PbT%
PjT{{;bZ02(r3hn{bOmOZ`BrrrUgg+MNXq4sIUH6z05uoKfz0hRXXHjyteMb!D-yEHE*msWKwbqHWposQrw#rh&86lVMDCP@J>#PCDLO=JyWy*?YhX-
mQat#jG3O&IwW6T-P>#CHcu2))WNo+IH_ipH&fNK6R^Y+hYhVcs;I?^Ow~XgWpwWEYZZ*R+p@ox!i>~z<QK!X*}ZCI7UOEjH-yO<O_rvzblFS35N5H(&;jDj
@u+^jX>?`AhDyeZ%1*#U?@HrTCNr6-?pu>H4qJHHJW8LkX6;U&i!AD`4woTILgA*onqF{C#t-
>>6<EV8CZJtA(7HN!#*q4o*0&lhdF69qOmp<qnD_cbsv>0!raP3z1Uqc-o12=hBb^n)x%neRVRu@4Xac`Ym0C6cGeg#bMq!D=mNEmULK<X}eV(x=cP~-
|!=xF>B`&_SH)giMMYTwKyNY+Hd2xikJl$(kx7Xj6;$@l%n<-!CE%Zj0kFN4YimIwAyZKFlb%C}Heuuqda1{2AwW>lv@b2Q4J&Li;M~-
YnFeBoIvOzdyn{1YV;C@AuM$5M^ESfjxL0GiSKUsEeB*$;_1%GR3ar8RRS(U{0=+3gt!kp*q=E333aA1>$YKA2IohoDRhjFTqsXhzd2^<Q~>c^U<4tpFP3Dt
~;AhX}WY@CV-QJZr&GnuB|zS*!j(q5H*;$L>5Q=hYGZ)f%^=cdbnQofp7*w6P1Ud`8A`DK35HR;$eQo9n3EXfriiY&e^Iy%))!8aaBIxN7b*3Qe3y=ZJG2Py
j1-
P(Odmy(qm=wd_}?Fti8=z`^yNuEuOdlS2Ho&#y7*xhcgNUgOvyTdCm${<yk`EkQl`$iLA)~*}VBrqo>xeJvsjKa@s2+{C$>mlMo6<^=kZ79Wk+hGn}0)M(Cx
F$J<-`%4Olb2$BcC&wdCDzY{>{VfBW^d>!aMm=Y42O6`mPuPBvCrr$qnw>17i_bYRhjKPOIFF2-
f&?hJ;B_hpe8%IDjNP;J`gw2+Ru~M?(F*MD5F|s7Zp;X{^I~SVd*;5WScJ}1Zz9AjTb619aagUFdJOmYJPWK%|dM^-|08ec5-
;(B(Gz1%5|YVQacb;MC>+puho?kc_Y1Tc_Y-2ac6E}jM|-BYBEnVCp%-
S+v7}MSYBW!p^Y4^RoR)i%J{OKab{p|pjXq*k1RJ>4^4dgV6M);#M4$K@ymSUWaUs6)=8WgGLPEQJ=QAB+2et<Lb<dt)$i$4<jki0tS%*CFD!<y&ze)K$;g4
lppYdhSTR)^B!atzHJee#-gRx=qbBJE=Wd)fZkx%j>MJPOU_zop)#d=oxnVNTJD<~~4#kH$E{GD33-
c*sQLgRyn9)tG<kfyA+nv=Ui}BHMY)?akpkUa#wwlJ<&fDM1i092pk95Ys3n#%VdQBp^7Lezc`jfS>xu$3hqd0OLbjm&S^=XpeJRI3l*4W%|UY8u26QZG<J*
%6dq~{_xQnK?`&g%+N7NoP3C8ka$d)_pfWDT$ZX{9N^RD3=%IaIb(!&ve<?9!t1dD?*F?ws?>xwSpJC{7pN)-NV^4gzeFjq{O)`e@k<V-
fjfji;a2Rmz%|TYN-iikzS<pYGhsg^3Vit!}R0KFwJ67ke!E{I$KA$yzl(f6$qhq9VJxR0^Y(bndO#8k+g~dTDI@8dwXH?q_DhlhzUGPOPWJ9=;bDN*Qy<_Y
)$7ma>V6mdhE1oyl^Ia6@0}f3n2%Pox-wXPN%+Hb0}13@l93$p&C#UD43w3=Bz$(Ph0XGiYL3U7jJ<ZrM_}$6~j&aBG+`MyY~=zh}!cuS@qBS(hdDNGUj3w#
Lrrv2D0#a#DXjeMRr+t0#+=YDTK<=OSk{y9+;#+@1?j8KFKeHlwQyoftc7l~b^8#nCXL=gT%D3|XXQd`e_$V-
ykNT5Sb5>8eO>Jml|Jb?Oc}`NdrwEsm@Up{f(fYOt5iK2;Nx;AK1tIGNl!FN;6a@BXgGFQapK_(EXxbl2iMVMwfUw1k~YIE;6ORC?}i4ag$vJi}|ovr@M`SL
cVeE%NgxJuIFg&l@LOb`7DPx{{e}quS$Sq(?i^OV}Ip16HFh*mtVN%`aJ0>cq95I2%>g0pWOmX`#8`!f~P_&F^pZV;h>LC8205$aVCjZaBXqBOln3t4$+{^X
6@FMA$P4t;dzALgPt{(vp8+&974Ccf!{%rjKu!`Qf6HzCj~DLOilHZ{y2X8eNhnws>8(YDZ|#?$-?lpI-=CYM$O=+N8;`U7q%$jm|K^)<)-
HDwAlRbPfrm#+DchFV;9*WjL?g4%waeiXX|(8ueHVUD@2^>*ZUjHO81R)~M!(s*3hD&NWZu1@4}67Wv8a9+u&)iW$D8+dMqXDAt12<vgdeZy=0xu4dT6c*gA
Ar9GZv$K^`mS?Y6~dRiJDwdC+DG4B=BQ;NE!89ilOC{peseTi-&g3{Yk{Ss-
>>cl}K)z`MT8AzJegVT2j&2Cl69wD+?j0c3JbIRyIGM#j_h%nX$C|U?v?u;T0D%xZ^F=5Ov9H_ze^2X{MtQeE7_o3e0uCxhMP!iR;a(9cHh;m>Gmw73X_`6D
6fjdwn=puf;h8_(9>Paq@#-yTh=u-
&(+N%Rx^`e_;B_Lwp8x<giOeY_$QE4a?{qfaH$Wu?`U@6rEld+r|2SvOm)x0Z#I2nIqAzGOhFaURfzzLdx44mM2<NyaC7zPn}V1Ty<5<xlqO)yf!Uj+gk`r1
X^yo@SHG5E3p;&gaGQEga^?^^I1!feXxkPf043GvUxs1I)f!7*3{)c+IC1oF)Q)p_KCZ1CM^ek@o53lzmrw@^8t-+A|~RCt?@Zm7W`{h<i-
f<LOci(J$VoNx`ygBI|s1YR%q(>^fBbMh`d=LAi>`}Cz(7m0B2@RN^&@hb@c-
6?^OM!^L5^iK(d8q{O9E|K`xx8jLn*w4LzExasl3A%qw264Z2`R40NvXkEBQ<y?=$lKRNNXeH|=&yZc)CyGt?ffu4<8{efgMD1kLVfhGALwBa83ca(*a}t=<
p<&k8%Usi{<Q(*QX04km=5@97}UTNxBxBC1oo&|`hgyFg9c!QuOx9jUlDq#7`l_MB)l*CC;)!4MWS%{PzK(wp+3PG$j1cnH_hli{W=qm{b2*h@DTAv0A0@Y9
wMHI042jZ7y!Q-1Lf2;6Q~9b-Y77_06yhKdzqmRAK&c)LNWM*kMQFa&`ghlE7!h|q3i9;B`1*b^0|w|hhGnp4|Bk!LqsukzyPKI6^A-
t1%;3wR{>u&;JdyrH6bPV`Vf56Nbo;KRfGcwPrw4cF0jKO;3Q(GFCsx1)ejRu4zWXr&|lwUUdtujSQ)_?9*hKs0VBSq1_B>XBN+r;-
0QDVxy<WyBq|1<NpK}4qz7RmFae-|pZ@x#MZ#N%8{wr6TnAYLd^-}}#lH%nyy-w{5FCPsaaaQmi8%f-NP$-
k@U1()&&BPa5#nj&0hG8Ju$HHVZ{JpN``82Bo(5|0ha_;PmEb2r{7Nl+j3>EM@Eb(g@gW#P_r>6kmH2mpTRA|1LqG{=##Uef)1a7%pf=H)-
~mP5$mFrG_4?vo9S8$Cly@?7Eg8;1CAf7XjWB~BzP!r<cMX8+BkcBiAXE_-Tevj;2KC^g*F4aH%lt0-
N*MXk#RTw>FCo4<0e|mV0{%G>&Ea0~+WkeKMU{jM@!w3QbVyEL%LFfVp+}$H5;E6ZKmx;n&n%??bQmlp?g;KE!R2}C1Y~pPsVj$I2+V;nxJF*Q{P?vlvJcRa
@Q~I11ph%820k;8k&qF@f=};1OeJs%<d@QK?a)33)+k~e3)L_ailH6MVFCII27o?Z7MRAL*uY~n1nvl9fUm&ES9s&qG8P!#V<3-
z6=gDmAO#>9vcYgN7+l12z{$#@`ykCwH|{8a_nWVK-yER6(1Xiz{KoHZJ_^HwAeD7R01N~w?Byk}f=JK@N5Kg~0!m8z+!e!1!SICrJqH}%gbkGk8vqM}0N?k
&^WPVI?-
Bpk{0QRt$BY$K<EyV1BR>DX&BAVQ_k9_<vIMXR)Ik~S<No}a2l>=v>J>pX<kL6uKq6NITj1xF)R)WH444B}xC{IjHJiHlKg*`xd*XYefsNlv@HHI+ZcbuvuR
|b|F^I-
CkjK5^>lF_^;MWqt@NO~k$4?%1fI|2$zqNuvFa#g5f&Au|_oILYHqye&4x)v{432?P;FAdF+2|1b>GC518bl@76H{KS_oyY{{o6}=_UKCD>KCY<^tmqh{I!c
3=yQ7j#DG8e3h%wf1_htK`}p!Tgmma57S%&QjC^lgy^CJ+rG05FeO(T45xSiU=pcyXNWhnaB0L0qZ14sOpl|zD@!P=(<wRM)h3u#hQfly;paqD4l0kCld-wk
P9pJVGqCA@aq4!(wZ&586F?ay~g8LH<kOL(MBQRqFJ`e9>?+0IEEU1E8Kn*{e2ld1+Ke(zSI@kahCU4<Vc!e@B)!?}hK6r+@zzk6ICh`5d|3(afY4}fqRMM0
G%7@pbke&my6kY!6IwJ;6T=<3rc>hsK3qEhB_&>SmHAXP^se81~rMq%8K~vRS-
((~ueeatgng(p~8YRB|`XMcR%j<?G^9RpT%#ncGH>m*paTkMy42@QpF7);?xa1YamO&f*uaB;MiJaukZJI42dT=cmc%nS~t?yGlH!`Vve0NYVJ_0>R=H64X*
)pGvn>V%4vjKQMdikya%E3BUAfT=Zy#zQB39nzhW5(C`Z{Ecc^wE{~eH5@A3}P2tW}$q29KY#%MMi$`r4wK^w9yKX3(B}z;HPf{03E*aN*(h2B#WK+u?*uZu
#LTi*Cv1z@b4<YXI@`?;vGnT_3(sZUh!6v8c18=YX#5%FlI)XEBp^r$qFds$G|~?xh&)U#bc(Q_CdA0um02s{vnMJ_`Lr(2wY4BXcK*Ong2k-
7UNxjY%GXA8pNoN&4F|y?f_U1ZBKDZ@56F%O%M##%rCD{65vBelb&+$u3!XS)*>7a)_|`WY@%YAMtpGNwK1lfMV=0%L28<XHS2#JD919&=k{l>mOvJkucm+t
KRQCM@I70=&mw^tTrsj)#tN?Ra|q#0PoEn&m_b&+Pat3ZTmmv!9C^QUSr|cl_1U}q*z?jX6$6=nnr7qho{jLm>-
qBK>;L1!i~M8w>B}EbcW1d2rpv+QDhRiMKm={z6Bg~l86E?k%Ooy;Y5~4iZ%fhrhld~>+|wc9m;4O)wO|nTK_3J80bLBeOQEoZ1vAzG4QRkuKa7X1;E9ipV3
5}(F<UCUU;X9VcDxJd1n50S;L8fohJCX@EC^tU2~Eeqd%wFWfkLJmepXK4TW>v7v4QmDCTl-
v#@|%1@#B^rhEG@?f<Ax0hhl^#&_LZtg$F>%8u@!X<ndxG_r_a75xl1YR?q>0fD5x#S4hVo;q8~ZkWdYqpakTBN5SZp@RQpjd@-
0+0KdqlAGU}XfsIYkKl%$42IBC$Qa}l=jpIK&xy8bsK^-I|@V@%_Ew4`^0rJU1g1?Uk+#&W{_qu`CWiKyA2C#??=MJ73P<bE@-
X_2D_+*`U^MTiES1S1LgyTAj{%HmAH#2w{OYr;t=syi2P73_;;wtXpn%G*5qQDQ?wE8-
Iw}D;;L^~XT({K>Yq7pbqhoeCB&0D^n$Vl}NcCrcYqiozxRB#`cGhWB&7%D&smNPE}BEcLmqA2J@7k@Yp7~edwh6=b$5UxPy)ld(kAX!O9qi*ubcfYSEz7&?
hFt~_{DY}8M60gXJ7lb(!qoU(T%0Vu$B+~>xmOy}(S-M!tUGzXGiq8_q@0j_;Y-aE0G8DQ+Rf91Y1n=Kdu-uWlrUS{eh^<dAs9_d2nhr*d(0R%oEiAYbcoXz
x6RP7^Fwb4`tmJ;=dG}Hv@#9aZs|NIe4&K`Zj~-J|Ec}glj%;Mv;}*|`pQM6V_=6Hu%EvF3G37iFrsL^q-
ap@b{l+dS=caqG^wA0`A<NFf$RSb+^SD>#z|0HaRl+{Ln2#7AWWsl=p`L#D%YTxAL8=?<vj~|75s>AO6J!cY0GJ!s1G!I5Ipj4re-yzG!igI}6Pe2f`*mLx$
bt%(!Fa#ybvK?TjAFFJZJ$^md~!=ep=|KP^G*hd>p&~;(Zg?~pbY+!|0*>>{_D$w%n<jdCTQcn+=u@(%35s*RKRicNDJmjEAXK#OgW?qxt>14i-
(Y<k3P)+d*iDgUxc${3e>aPrh-
%`kTWcjE0`Q^8@{ZCI&Kbl@p%J!?8Z4W0PdcfhJBPCq7_;LFYO{<1sulDumqC%N=JMu%mZE2*C*i8I2L?vhF=F0DYUl&B%=j3KTZ<8WE1iFZR)`+@|3|~RLl
sZ=$&AeY9TdXkO7wfG4u8po)Zkc$s#BQJ^1<vV<8=c4WJgrfL|v-
*hbN8TVi1A^fIo7MwSBnPX`EscekM*L0=6e^x!%b$7V+fYN1_#_?8mgd5iQ%TCjv}7qT3(0ew=8gx;UrzB0u1XSe<Qn+KP|KoShVI1$n}j?wRayTXltmnGnv
3Q}l6m)hauaWWd-x~Bzks12iL%#xyaM|ttwMw0p2-B)kCzR0zKG0+X~`7S{XSfPa?k0dkzZsQyG!x8PlW}-<hxGn<e@bL$zfaPArT-
xjYcWc4B-tTyt*p{J;9%S?L-S<mac6-l^J}bum_=gYE!EeETx_>1QRe(usL~p)YgnZ}dKj4Q|=xs0l4U_^CS%&`j8x>a#*vMI@1b2Ktxs^!nf^KG?XM-BHXb
4k5B=6mu!khc#mrE=h_@hvcrQn-i3uSDA41$-
0_aFXSftxu>;R^3&Akz+5_E<+4!DA0v3=<Ig+zQPQ=F&H+@voUrDVAUegMgR7*O$KhY8&`328dYHqb{x!cyGd+x7P8KKhSIgkq3Po@Wxe?0RHe6tK>~j-
vaJ5xD*Lu;8$<Vf`^Tyn={fq$OIJBCU{k_3187e7fWme)TMcf&SRT{yEZ@_ApF&v55geJ&>o9{fS(EI&+q)6dGx0zZR9Wi`-
d^;0KJ|EA|cKHG!}S@0W3mS5+Iw^-hJ80YX?7nCV+fY4h-<(&2o6-wJ)T!0ihOHO7k@o%NRZ1Q-UVQ5=Q)sY>ImCkNg7S>q<a>dQnir>f)_nGghL9m9-
mg0n=PxFF_l)_i-+Lw*@4?bS!*ggh9yTLpAc2!3UqcD*`@V|B?a|$TwdZBU0E9wu0Bcl7cO^-HAffuc;3Op53e}o|y4s;YhKR@i)|U39z7d!dMQsPO^;g-
fMTA;1bgSrcoaZ2Ew;q7lYR^pT7SAbp=uF@RT$@aRJKv({}`yX)hrfqc48*Whfg#pR*0I1gZ(_u5=N^8u<LyF5HAQw6Ac2X989t3wRg9JfLFx{Y@x%I|f`fa
wQPeLEk#IR^Oe6XbtGd54}A<@$R4w+zc$5c+(%yEFDE+!re8oh5eP!FMF{a8vg1_6+UH-zQY7{^Q$c?2Hb5Wv9J@;S0=avtbHb#=RLU3eruPym_P=C8_*y2f
dBfJe>VlC_~wU~5>L6~Z6ljWzj$vNJkI02!Q3$eZwd9e2&B<3@qa{{3F`hdR3Ll_-
+Frozu!oEHKS$XzLO={^QTo8PqRH<5Rk($K))rt!7z^n{a6dWk^sS#eEjw-@03O!F;)2eKFG4jA-
3BRG$EEo`belPki&bIy7bwX4<GnU;tPCVf%hWyFoCu2G)c2k<Y1rY=8;q(ng>_!B(M;?=J~l$%G#=wxhW8MdwU@tBf9g^9Zw^^^yn^T$>IlhsP}{hprhCh3|
Y|oei+@yN-
6=IGRbP*Lj@S);XFY9G=X?U49d~h@3JKFZ8M^oG?KpMGr@M*AG|UK@W;#t*QdybEIZ>~6JB)EI(X%^U{ufcBW#^802kx)#XEMQ1hO=ezeZfXS;GD0zkfJMp*
N3tnEK-3CPDF8<f*~e*Qsjs+JgtT4Lsy72y9RN%?V2)?>O)#{P;-+aKZz02Hls-Sc?kRfFOZ;`^uGAK;LP=@0GBQl)xzz#&(1{G{E*gbT`Ptf>OfgHQ^!GO(
Qj+kXUB3u?2W8!M8Ti5c%X%F!($cvNUB5{O~`2ybbTBxWV(!o)v5tNXJ5E5RCz!LV~`Iu6bVH;;~e+0~Axfzr34|E>QyhC80n5?A=c~iA&T7!LXH(&6xa$C-
~wWA@*ep$)BDG16ka7UwiQW23H5PfVKiV_$Yuaq-
$Uc{P9T&5IVsmA3R4oh;9%J9$&rvM+18J`|mvei#;f2@&C;apDeLGst;07kF3Dk1Q*x<_cQ>ZHx9(FzW;R<%OBo5ArNyD-O!;|(ZyRz%FQNUjv-
k#DF&;AKp<udJI(HV&AXR{6`p2!NFBUUj=j8Z(>sJ2TxMP4t3knlssIeekt9ndTUZx_fl`{~lPzF^J|mO~aE4Z~?aGBaxPp7_Mjy-
b*uLG(DP`aQg~3$F5@a2?%Eu#Y;Y)<W=<RNB?a@4ZS@2c|aRM$XSk(MJ59rwrW00*wxCgq4<?GqRmzQ6?`)WRM3EjdpVw6COzh)R=B)H-
8bpr7Dx*Y$#@82GSPVmE<Y%E@6E>WrA@+Apa=G6hO5;hfoKL>bx;u}sPpVzM7L&kdrswvJt3=!EN0GqKAak}u|Sh1Wfwj53ynawEJzK$~t{+eS391drLzV-
s=dv8YKbdobim%?Ol`p;&ubR{uCuCd|NLhKPr9%q!{MBsGH>0_xi$Ba3gJ`l<Z41iAd-iSF36z44tm%|x{Kg(k!Ay!5O$>HQePBUz$-
^(P#1V@8Q0VjZc(qf9Er1n@Us%Is=$l?6eCN1N0IDYIOr-
A<}r<BL}4_7nI;e4N?<2BHn>wRwNe{;fQayd>Y=iA+@>P}bG;=kl@uF4?i8i!+K72~ZT2X;}MajfANQyd54EJDsWJ3p1Nafc8mf*$3aXV-
0!LEJ#M7)~p@YMNN4IVtR6Ox#Ld6gcE2oC@DUoO0-750wc%SfV)p#Nh-&&VOTVlE6;oOq|XUuz%~g1K-
`FdffvHtT{W~pE*+ur<1QGnA6i}2+nue$2co21aZvlo?WMQk0;UrCz6Tf$3f0C#W54?SSsfDu~urN*!LlJ`O&F}UFg35<C$@u2_(;6(%3z#JPNtB?1DPhVoW
l2503!OPdN_uwUq5@Id=Btx9g|-O}js*k^$_GLiW`GIeKD{-6)f2f}C}tiVmSQ?uiquA|+^v;Ybk2e!4TKgyg8*noLorKmRo278S!bEa~p=-
|fYJcHQaGSTwQ|H{5z=U=tj|DQ<HIvz~lr3UgX8r;vSBv9?5~Yo@r%kP`+uUvW79Z#KzEh3=0xIU&47aJKiddzU2g-
&vXNkumqOJZ>hDf;p%9b)Bh|1vsrVr+{ezp{EC)M4V?h9JyN!m3v7M!5QT~)$;?l187dM+vqmH*~OeSc#d=GsME{6bs*+gS-Wyp&(wU)eM@!^M7eMGIENI+#
bh#^2OQ1`oIBN_h^;K{r})$&O84D8?hZ#z8qGO{344AH>v>KBySI*g2J<*!<bQ~OTv!XvaNczWqJ^^~#$b-
}^vG|Y%{z5S<LOAdd$SC{86!A@r#hf8_lV<cAxF$^5eCk7X0N|s|NhqfVsTp_2o?WF4LF=c-c!`FmzCWj1_ZmUS5LFyd^%X_78M6N-
4ZyNBq!%okHOQU$DamRj9bJ$JFSgf(T+k{Lz-a|dmlv{1^P2$mRNgg-OJu#BN=n@iT{rtLiW!OaP)w4=w8xKKJ|4hyIleJ|EV2zszovSKO-
e>ch#N^oH{)4Y=bn`v;}<5iTg9>c}}-GxdD#iG`7DvozZx9dIcThUZH)eSIpV-
$y4#Qr$5t9!<Rj#A1iK#71hBS>lF8=K1d*c^mKaW>Gaf7#WiQ)m2s8<rSwy1aYX;e0tKu)Y0eZ|7df1FpF-gOx;o*Rq!r9bKa*0!%fy`6GrQ!U%CDd}8E(%l
pAJ@^t)FoF(0Y14m0Qcb)2aXBzS#k%p82!!PVFW;Thwu;FGqc<pWBg~<uemiv*Prp!R5z(+eDm1_htrmM!tJOuY2LxnNq9l)H?UnzSFb**nNw1@25N!Wn<S@
ai2!n&gm5OpTW6ws=yF^_A7-IFFO<Z%GroNW?{;D`Dsa+JzW^#o-
*rJmdypHeloeY>wjwGVyr)%*6|ce!>1?y)t^l~{?y=3?*B$az|)ajw}evmc1*Yn7JKfeBKzH<;?EGLI#c#1?%T`m+X?@yD4bsAvq{@$Y4Z$ir_ojU^vnZKC$
^kD^G@eGP8CRSPZ@EK|K{{t=+gtNoqk<C6Oj7UW$kCrJoh1jPrW;RW+c&BN<2++w$n{cQ`i*yJL=C+8$12*#?xQzryKR3eU17vR%QQp+^+oZ0F<9;C2>D?-
5b}Ot@At6?|%UauKR}
"""
EXPECTED_STREAM_SHA256 = '8852ef13b26a06d9e724b35e22193c963dae10751f9a3bac165b6c53d382d6a9'
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
 assert len(I)==897 and len(F)==1790 and D==10**14
 assert V6==855681799493322778657557419455421981804886
 assert M24==[558840496445428043429906853565356143483254,0,0]
 print('EXACT_LITERAL_SHORTCUT897_RECONSTRUCTION_PASS');return out
if __name__=='__main__':construct(sys.argv[1] if len(sys.argv)>1 else 'reconstructed')
