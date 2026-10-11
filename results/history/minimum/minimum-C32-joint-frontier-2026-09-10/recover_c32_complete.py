"""C32_POLYHEDRAL_MAP_CATALOGUE_V1 complete recovery and finite verification.
CPython 3.13.5, standard library only; assertions required.
Save as recover_c32_complete.py (UTF-8/LF, final LF) in an empty directory.
Run: python -S recover_c32_complete.py
No external files, seeds, numerical solvers or downloads are required.
"""
from pathlib import Path
import base64,hashlib,json,subprocess,sys,zlib
assert __debug__
B=r"""
c-p->4RfQol7EGrt6RfH@!HPEPVCXE@?^Zbd6jiiN#?4i2#*p**u)t806S)~x!-=>k^q67nSJ-_E>mNS)ZJ>e`dfZ^H#-@)GnTU`
nQwS^UA!B<dldgBJ2uOWb;M$p9<SKi;PGa~Q<jHGY$Sn^FSrr&XXBEd42<A-%V&9#8s-J*pOXu#`xxIA`2s*sy8Zr<k>xD*S?U{6
=%p+zMh43=o+7c#NclfEVak0#y4%D<V=Xa{?~OKhkMU))T1PzRG0!q%lkv=$C2<Ukb6*T8&is(glbA)vK@_fydCJxcoXXY<o^m5k
Ll)0Bk=RTI%gQZ3#zC5_fM65>LBU$MS|@34Tqc`1=P5CKV3jMl5JvJOi7KdBvhu=M5>+s3mM>t-CB!YfKE~>0!7`j9##5HW#K;Oj
l2S2T*XQ15?z)fhlwJUTvCjizR?H%92G;N~HsCMi`6i8xRT!Ir9S)tNz#fK<5x_BoMi?6@?2(%hhiS{QN+NNRu2>X)1wvViQoaGv
ni=rMeN!$bhX7xY4UjCLRm8%07WzD%>BKmFc~xYSoZ2t10@bZKnp%#W$MGc*L`&t;3E`iThup;9=!pSpq~0jSXU216uf{;4PlUCI
>NN4sqk(Nc9rdmMl*F8oF@vF}<G#}bR1BDmcoxVm7j&B-+=fYqE)OEkN+b}5&056em_2i-CnppViz3tX2(!d$VoR`uc(H2HrHbrf
aix{GP(&$+OFX+<7HxQD>LT0HnD25E^%(%Ik&)3Yd~hBM91Ze$5k}nDmU}{wq4?}F-#53`XiHOj>+CVKh1IL0LwI$1snyu`^cV-Z
_4ChzBXKSnzzrHY$_ebaG6)tYaX4d<rZv)(AJW3$TMnN-coy^yASqy)`*SWB@sfN|x`QMQd7M|y0I7^)H42F6{K5=OALIkZ1|wbp
#-E|=r8@-E&G~91mVoJxzuqH4#a&nDOc@DogEq`ZPIx@a=`@M?NPG=4@lqdp7S3Z7z1b(neO;^5l%{wpfdHYjZ}2GNhW+9VnXW-;
7tVPF3h>%cBByCVrMk7uCSo2?r7vvQdmS0z3OAgB27@<`XNx4o3GWr<@SIV*rR+#{heQQhi?CEfNyXkdg2Wz$l8W2(ZYg3|)&Yw6
2Lh?|RkHsEV7))kV4<Dz%^C@YyKKGYu~2fwCP3{DlLF>T@QR|a4dk?89~wqhqDY?$Bf5>YtXr{0>9h&5<OQwpvlc#x0(A;?6P3z9
_sfe9ICelLLK9*Bz!`v6g2wLYnp{{dkJgt#961m>4y^<v>&PTYDADblT6F@QR%J8FH6R%xX_XElU!<J7Rfb^l%1y*Pq;}8wX<D0B
sq@(oXF;w1r2P*clxK#$vbZpJT`$amAfyAP_2H!E3^1&rV&qo_(ol3aQAAB3GqsNUdrRpFgINYgGH3+AC`z8WPm$0+kPx%P!vi;+
Cw@W|z>ml3i*nq(w$n!7)+ui(4*qzIpOV@?O2_{v-8Nxy_D_m(*$NSW63+953A=KBELr$(#H`U!Jz(I6lEnk!Q6mp2CROUlL~a&g
h*Io=YS?Cv^g%ELo+qRa&ptfyeE`p1BcZ6B!zr0IL`ggXK|brQleO8?Q--Vy@efVU#5hluKo>y8b4D0EORWWSAiz!?cN*Cg9LX|H
o@4p~aKj*bm7ar&q|vm4%u!_IiM0J75SE?>_=|V|3O3>yaSug_mL92;jc08qh+6wMZwLmEhw-MBw*(*yn`a_>aYl3X25E=Wa!@mw
AM7+cM9RC;t%~HRW!L^5&iuPLFc0$fEoFs=xt@XSe9c$bxk~x+y*v^LK2-~<of5T2%Q>=fHDH67KAbkQoEASzNKOOou*K5*JTI5!
8shYa;?rI(9U279*bxLxk0l^W#rHYZHEzTTNW&6XsPa_LRYonGUxrHoK$XgAhyH)7Fl4T)40%&wK(p+i8^X4BCbMK^Qopx==X7q*
)ue~Ob9-37A5O;uyYEoyiA-)TzOyFWf`WosKx!aX?+=~5ePS40SU*%%!~#-?!~5o3<iQ}V;}@Z~L?q|0dn8c}_CgM~{vR}X@z->B
1j?i|v!RGET&dxvkxqj`y^*QvrJ0tAB%8cS+=RyIg`cKvo?di_Itcw|&`A2~WKRIJbTuf=O3A|-c~n(Yo<;;1YGzhdxu`aO$eRO_
WkG&WN`-Cm#Dzj2`;KTvXkipfa*i);Vf^da`*yeym>aVF>)E>k=IvB>wZ;s6L%iYkbtJL}Tj;Yh@*y9T#oj1cQW=kR%sPh<HkT|9
B#b*!h=fAK*8^#uaR0y-uJwjVh{yrcqMY1Wquq|K)>sb|1%4@<gH%Nk00$3MfHY^!v*Be3TM@~|$V)j}eyf-e*l$-51p=+s->4h_
NHF*VEsF21E3^mZzfG@DtJZ%0uh5m}44eQXhatonDT^=*vIDy-sFVPpp{S+&?4sEBn#r=N<5z36`r)2^!Rq^MsA-i$p-rgxg9;}s
ZKRxusvSxU5$HB~!&=3=G|CkNJ1eaS0wUFN$C1d<p;R68hsZ1jROPVOX$aYS=i%;ZJpJwS_4wiHW_sTtB@_vwO|}p=u<z**fYP&G
ZPKfHj{`_j&sv6!Z0$vM#hks8b!O7YDinLSH`iZ&pM1I-U%S`iFO$0tS$%^=NI0`ns$vBZKOqqvhVmrHvKdqmp%zFIfO%(BwK+k0
s)7e6fz8(xGX9MAMj4L+j1RQe%D0hPGm`}-?4>h0>?3`Ui3&4&ts>t?f`WZ*4s@pBg7vjH@MZ^T@|DN38>rWtx@TlFo+ANjt3ZIL
D$}U(=dFsfS-y&wIlcft8u65`s{?pJ{||IF4q4cNqj1OqvA%|D6EI1|jH18MO{HG39C_7ttewe`ba$|}RUOU|1@Y?L$nBaoI=iy*
)`%Zqfk6ujctc2nbxlJ%rLNf9H3`<v5$$U-(3%*2ID_EsQz2c@1i9f1@<)O_xJp*CvDzrVMG^`HE@@S(pdEbY`g{%vRz`7sB<W@l
uYvBG2+fr1`MyI?Usg%FUWC~yL+xqNdrH90Tx{97Ai$JovIn>YVnU#Lr!{$&f_lz|N=@;*4Ig#~m+d%C`Grz38u}fl^jp~Nr%E8O
NSGJ2b9pjwH5311eCuA0AI8@=zkQy#|JCmh+-^7nW~NGD{d2Kl9H=(ZxX6%g32;tCcp4~Eg_j|Du?8#|B%d>jprW|QtSe_q#i_~S
8*u3=!#6A3qY@Tdv_zAjg49&ArdGKZTgX73V|9Mw=p^T{R0LC~mPKN%QYmSa>5t_QVado<z0#Z~E1su?%Xc&Ikl0qCJ;L%F0tHXq
09Ns31T8Z__DoH@e(Cy~6?hhTRs<Jyg-b;j3j$j+aGD8-)a(%WH|$u}QRne7?pR&$YKhOwd<QRh%ue&#3h4vja|*n>UXgR`^*mdR
V1(*$dGp8Z_2glK%An$rJh0CF<oZ|l)93MZhg65v`TNb)^ufKmxp{DJ?mk{U0E#C5Ci%O`?akeTq6upgb@$ZG7Hn{KF2=eGzVk!S
w7j|;K=Ftjxh_iIb*(NW9=_UyHB!{?Z$95$PX1-;&8>gDnvNfC?yfHH-J9w47k7H&jvpSzSJTNI?9aVCIdw0u$5(%J#N`vX2-l6-
3V5Ql<GPp%xNc`CQ-a6%9eD?O76ye2XR&{+32UNVf}MzL2IBJytv@ZWC0E}s&K7*O9PM3R8c7@#^0Lxk0R+swdrJKdv%yE}s`0N}
52E^1gN=nCWE!hOcZSuu9o9ts3@h~V@F*Re_AUk&)x>uW6U5I0uis;*=V!mL_ZR({-#-b?gY$v!U7YsMPd)$CJL&b#_(ku%KRY{P
jKBZI_fF4x7bm^om)@!00Z~$6g;B!%(mMXb_!XQ%{DEE=lT8Fd2Hybg&yWGY_&`rZ6mI&!t}#{s$D$BNGScCw{z?YnvqFlv1`pmL
JqVlqbHh?TLQ)Ln#IoGL_IY{7jQw=xVfcVyar>OW2NruiCwNzcLw`?FpNZKd<*P0ddsu9+l_UD(A~}JV>P{ThvYgWy6r4$jlvmmc
^j6&|J$;O!?5C@4UDBH0>71f5VvY)#V(>aL%B=Zx*oWj0y>VQpA!nrDD|1_1E*{C=)M!g%y}SL*4wY<ih(7Dg`qtHN-69Dxd-&uW
!Q<(uKXi^{mv*bVv|H7s-L~6_ZBeYcb$u_}A*vtZ&_M5?QEc+$wi)8}@ClTWPjB~SWNzKMZO--9(7)Yvdm<5Sb$q_to&`xc|BDta
;6>lZlZT>GXeEK*V9P43$iOBJk~yMg>kv^jeDU<fA^+QlirNh$Wz7}qHCK5_FSTB%JvoE_=feT{Wq3y35BsO&VtCejtzbpXDyl&I
w(4p%ClFLIZE`*NV={dh-+gf>C+_65itW?M{k{9}``yjw-+p(e5Zv6`@jXOt$${{C6LD=Fgy>o14_DB?$iCun)mH@Xf~GI8uu&3t
P2DvvF=82<%@#;XmdpUG=fdcuL`Erm3=qu1EEmqJz6Ku|9{~{^7<#N2X<=fGnLU6+g_4-K1qa8*Q&_{?#1JSw{C$9MqQp?IBF(c5
nU{d40_MULi^!2ySk}Kas0yq*yMsAi$Eoju^czOK&YRmEnM`&ZtE@R!-ETK7IW{dJ52$`og6|jN6;5^k;!qXZ#BJyw*0YM}QvX@R
sQOjJvRazwQfHvD5?dg^cB4uG?wfq-{g4aU4?!|}KNgX2%=YZi*=xOMh;>J{dh^P+swpah4%II)b)>_;Ho<){3kA40{bFJ{%%G|!
%q|=Y68D|<Do=4o3U!V`H9O8L-ItY`(p>^}OS8S6@lM}-%hwjIzBB%GVDz=_e>I^6{j#R*qfZkZW&m|;WFK!H?5~dO)*kn*H-#ez
p@8&yS&I5kDkkk75UavyxZ^&}HY*eVGkXJbn|7lB4)!OUu6q}()w`hdt-grWJk_S!iPgm~qr@C7`#t*f&p&JP_!SQ5?UK4v-cOW$
i#Cms@(M>(Nu`mPs-FxEF3yF0mL7zj^<_I+`Vl(lpT8eeh=ZR1{<wxc?N|O8YYwckT!3(IZsm6Xa6f*&o8Di2n&@?vE67SmZ8b<-
O+QU;C-4D<Si{4Qr=KLU3zgUP_)CTS?)85Fof!+P
"""
r=zlib.decompress(base64.b85decode(''.join(B.split())))
assert len(r)==10611 and hashlib.sha256(r).hexdigest()=='3a783a1fdbd6c771c0db30d2f567f14779458e299913ee787dde876e3207c05b'
M={'c32_catalogue.py': [7169, 'eb78c9ea5e89db65b791e8ac0298f0a21e6607e97c05cd32be8ecee6e8317d20'], 'verify_c32.py': [3133, '0ccbfb67b413046531801adef23567e2f791396070c3976ad70f201b912570ff'], 'c32_catalogue.json': [240929, 'efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d']}
S=json.loads(r)
assert set(S)=={'c32_catalogue.py','verify_c32.py'}
for n,t in S.items():
    d=t.encode('utf-8');assert [len(d),hashlib.sha256(d).hexdigest()]==M[n]
    Path(n).write_bytes(d)
for n in ('c32_catalogue.py','verify_c32.py'):
    subprocess.run([sys.executable,'-S',n],check=True)
for n,h in M.items():
    d=Path(n).read_bytes();assert [len(d),hashlib.sha256(d).hexdigest()]==h
print('C32_COMPLETE_SOURCE_AND_CHECKER_RECOVERY_PASS')
