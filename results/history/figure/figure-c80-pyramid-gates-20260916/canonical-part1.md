
### Recovery capsule part 1/2 — COORD_C80_PYRAMID_GATES_20260916 — exact body and exclusion methods

Ordering: part1 EXACT source bundle, then part2 NUMERICAL_COMPACT source/checkpoint bundle. This identity names a research capsule, not a new own110 body. The exact body remains the operator's literal C80 pyramid from23:50:25.547Z: V21/E40/F21, own211/weak000. Accepted own110 benchmark remains VQ20_C622_ROUTE88_118_G12/C622. No numerical checkpoint is promoted.

**New executed results.** All maximal supports were reconstructed from the complete21 integer points. Independent exact A/B full hull, true-edge, filled-mass and strict/weak audits agree byte-for-byte; third centred integration is zero. All positive diagonal stretches of this exact C80 are excluded from own110/weak000 by a complete rational metric-simplex cover: strictly stable base13 plus another stable-or-weak face,15 disjoint-area proof polygons on faces0,1,6,8,9,19,20, total area1/2. This does not exclude general shear, rotated principal axes before stretching, moved apex or changed base. A separate complete y-stretch arrangement has159 positive knots/319 cells/17 compressed pieces and two strictly stable faces0/13 throughout; it is an S/U arrangement, not an all-t H census.

Exact reference census at (7695683,168054,-75622586) is110/weak000 with roots13/14, but filled first moments there are nonzero. Any uniformly filled convex3-polytope with z extrema m,M has centroid z between(3m+M)/4 and(m+3M)/4, proved by positive-volume tetrahedral coning from a maximum or minimum vertex. Here the interval is[-31631537,60310753], so that one reference110 point violates the lower bound by43991049. This excludes that target for any convex uniform replacement retaining these z extrema, NOT the full reference110 chamber. Full proof and scope are in the recovered C80_RESEARCH.md.

**Recovery format and integrity.** Remove whitespace from the following base85 block and save as C80_EXACT.b85. It has18184 characters, SHA2560288a5d5270903ed2d68a568c3b7b51df6583dc8629bc6e652f887e3e31cd7a8. zlib-decoded canonical JSON filename-to-complete-UTF8-text dictionary has40141bytes, SHA256aa445774cd849878f912eb8356986699e44d56d4a4f5f61ed4507fd46e16c6ee. It contains11 complete files: C80_POINTS.json, C80_RESEARCH.md, EXACT_MANIFEST.json, REPLAY_EXACT.py, axis_certificate.py, diagonal_cover.py, exact_points.py, reference_gate.py, core/check_A.py, core/check_B.py, core/centred_mass.py. All core code is literal: no FINCH capsule or originating sandbox is needed.

Save this complete decoder as RECOVER_C80.py; it also handles the consecutive second part:
```python
import base64,hashlib,json,sys,zlib
from pathlib import Path,PurePosixPath
spec={
 'exact':(18184,'0288a5d5270903ed2d68a568c3b7b51df6583dc8629bc6e652f887e3e31cd7a8',40141,'aa445774cd849878f912eb8356986699e44d56d4a4f5f61ed4507fd46e16c6ee',11),
 'numerical':(19245,'7dfefaa04166f1a073f11e6854b42111a94adfeb4371f9a1c56e073874319bab',41498,'0c98e0d793ff5c4b916ee37399bda99678c9222bf6acc59ee0b55805ff1f57e7',6)
}
kind,payload,destination=sys.argv[1:]
n,hs,m,hr,count=spec[kind]
s=''.join(Path(payload).read_text(encoding='ascii').split())
assert len(s)==n and hashlib.sha256(s.encode()).hexdigest()==hs
b=zlib.decompress(base64.b85decode(s))
assert len(b)==m and hashlib.sha256(b).hexdigest()==hr
files=json.loads(b);assert len(files)==count
root=Path(destination);root.mkdir(parents=True,exist_ok=False)
for name,text in sorted(files.items()):
 p=PurePosixPath(name);assert not p.is_absolute() and '..' not in p.parts
 out=root/name;out.parent.mkdir(parents=True,exist_ok=True)
 out.write_bytes(text.encode('utf-8'))
 print(name,len(text.encode()),hashlib.sha256(text.encode()).hexdigest())
print('C80_CAPSULE_DECODE_PASS',kind,count)
```

Reconstruction and verification commands, CPython3.13.5 standard library only, assertions enabled:
```sh
python -B -S RECOVER_C80.py exact C80_EXACT.b85 C80_EXACT_SOURCE
python -B -S C80_EXACT_SOURCE/REPLAY_EXACT.py C80_EXACT_CHECK
```
Observed warm and decoded-source-only cold terminal markers: EXACT_INTEGER_POINT_HULL_AB_MASS_PASS21/40/21,[2,1,1],[0,0,0]; EXACT_COMPLETE_AXIS_ORBIT_EXCLUSION_PASS1,positive_knots159,cells319,summary_pieces17; EXACT_C80_ALL_POSITIVE_DIAGONAL_STRETCH_EXCLUSION_PASS (both generation and separate checker invocation); EXACT_C80_REFERENCE110_AND_FILLED_CENTROID_SLAB_OBSTRUCTION_PASS; final **C80_EXACT_SOURCE_ONLY_REPLAY_ALL_EXPECTED_BYTES_PASS 8**. These were actually executed, not proposed.

Expected reproduced files (bytes/SHA256), also bound in EXACT_MANIFEST.json:
- C80/raw.json1430/2e7dab88349ec2f3bd33d78c952985ce18fa4b420d176153e0ba485899f40950.
- C80/A.json and C80/B.json each4571/f17bb48815e8ff86697936d33af34e8e28170808674e9149dbae23c5228a19f7.
- C80/MASS.json216/10053bd03f20833183147082554bab3259acfbb4a5dc627f031ad9571db20747.
- axis_y/CERTIFICATE.json364654/aa7fc21913755fc3323f8d8f1d53f1dc6d7ba887978991126f8c63bd76cde079.
- diagonal/COVER.json19693/fd31ec1b4259c7d37eb2ddec09cbc1936372488a51121f59d86491b91904a376.
- diagonal/RECEIPT.json263/30ecb9c99a1a917b422eaf25822c6d44159e73e3c95c8acf71b53408a0b4cd48.
- reference/REFERENCE_GATE.json2957/0323abc291141ec0c78d238d020c7fec0c46428daef734afbb953731f016d99b.

Key recovery input identities: C80_POINTS.json599/ecdb3cb61947d33650d7e79dd190daab2cbd35737ac5d5ccf76caf932b5cd3eb; diagonal_cover.py4814/5c3b8d8444e06e0497f4327969b54b9883bfb7a5d6dc10b46e5146146320cfe7; axis_certificate.py3848/8ccaa0a9013cb8d7333452bd98848db97e0f812d771e795354c62b1b80267dc1; reference_gate.py4624/26457eba8900b41d8e6ad3619efa6828f5483438fcde9ec9181cdef61305d603; REPLAY_EXACT.py1513/fd0fc9135df4fbf04cb847602c54778451293d47797a36c9488aa947d568eac5. Remaining source byte counts and hashes are literal in the manifest.

```text
c-rlKX?NQ=w%}h;SAURbLoyfb3UiL**p<vnY{zy|=~DFgxXGd|k%}nUk~8`5a~FV%EW48GuAV+~=2W*sfxrcDarX-X-+npj>dyJu+taJd#!Z^Uzx03k_T`s(
62;5(%P;-mu-<N)y{6IAg=u!+L6~j5+wOHn0$;VPUQ6$&S9Qa*T2Pf=T4v8Q&8~WBbo6G|=rs9V$LJW%R@Tt$v<(D|FI%0iX?0pn_0rOt&`Y<&?^;I7YUMpP
&6c5e%r?E$jh@-<Sn4Ib)6Hf_$9GL=*ll+69$RgzXBY;*1PEp;A5P2cwR={NhH6>Ow$W~7)2O$*F#l%Hz?Vi#@AZtXnZ4|^b)(fYsHNF!^}1#|8&2EkwDfKd
d+b=c*)p4XGiYbFyC%G{Ov~&v+wBZ(dfV(8-5#Q*XBq8Y*MeEMTHUVR!~S3?S}knYftAoZ-E5%Eb_;ORMa*=YRud3tWEk!BItI)hLFzh;*T`l7GjDbbT8Lgp
Z}+gfY;^&_MyG4xyC&dOx3U=+U8C34TP<p4b<L)gb=I`3PE&7<M&ExCL~R$xm&b<}M{gRl0I2Qnm7}w>i`Nd(;Xf`8-@kqB{CaqGeCe2g61``%zr<hSt4Wkr
(qy&p!-}_xgDLzI#X(wGPQpqu4;St-Sya=?G+M&*v;xp7^UcDYMM0%zTK$&ZH(QNXv-5i;jF*dzR#_$$w-Sf<(@iB@hyH3A29@MKK3Ig~a1qAPPxy5eO(Sm+
t!5QJjMG(GapRz}yicHo>o1{Y>O<c_#T}2M7#gho=_-wqIBis}U|b%6nate9ZDkS8+$c^fpFWtnbJR9X=i=<+)p57$7)ICm70_S7QXBw~<iUOD-s-yEplQIw
PtUGku#;q#T!(R(z(9UYW?teq5H)}Qd*v91Q}L2u!?+3oRa2OG#Q5=(_%2*mCadYRl8h@Z{9_sw;PCJ|TvV9X;b&z_6jbh`<pdk2OE+Ft#?f>Na}59!(Q?zM
90Hh`yN+gn?sPSuCyQkiUsvW+Hx2<)3&2Obn&HZXfvCjE61td#iwF@tUL-S^(Q*;F@%3uzE&*wc%3B!5a<K|4pAL=>P6&i)95nR<(-<IXDk(I8iTcS3M~v@l
rU2s8Xkid*^(2O6krisXfd4dD3|KOtmT(@zAD9X)AK~L*=BDWZV5B|{-Q@}(Mzi@eoIx!bR9cxYl3)eY5Mj&6hsll+kB0}ZD*x;9>=f_-IF1$plE`uabCY<j
FT>@+orJ*xFiB+#f>^nZ?f^fEf*!&}qEI`I7U{AwOR#q!p);5<0Zk%8doqh+B=gF|O)IS~Fu*buyaY_4#qKK-_fWmtq^i7PezFK9BQXY}7>G82hLUxrn*l5q
Ogp@bkkU@xo*uoaq<~;ASyvLImo$w$7<%B&+-qof1JGi?i|@|U6)+}H-2!<BMxzK6dxmz=66RhBBKJDM2C$sr(w``5S@S@!$qDoW3tm@~8oPeDtOP4)bQc1h
;o!eIksUkHL2cqhb$Do8YXWF0gFc^ZQd%$BP35(X?`l(b<^`^^7V=@E9v-yHCJLt@RLUK_{_pw~_J&Ihtl&+<da|e^waIZsIAtHJk0ThYx53)~eT5ATYF+#4
+|;2=dtvL9G0ZIl;G0SU%(;*-ZW@)-WC6SsJ%q%x%gG`PcOVTh62Yi|ku&%x%<jYJdICg$@2vOloeli|!8RI|W9kW{(^r@i@GS@>9|$Z}GHVKd+y!z!G!)RV
Q8~c@85T~884d*<&6~!4`0iakEZJ+n@|7E8FXqTg8{*62WWN&erZCSb{6bEh&661B)KHQOOQzvcftE6Y$;wXv6l2(ERs3m^!VhLEq(2sO^JKaKQ~_%MYe&~H
Q~~rLmeYz3(xNT8q9=@=Fm)EwK!N@(jAntDnS&xoNkp=c$S{XEC$WW#<E{ddV<>V314!jOL0%-|x*P-%QMeXrP;!j04p8Jqi~A@INd(k^16<<WMH>1nc}UqL
OPCqGR1(8DFp&~r^<W5<Rg5wPhyjKLup~|t4l2{oMQP*4s3c>cqVyJ^fp`R^6>p%mLMe3}B~l#>0Gx}07KqIafCN~PFiKGV@pu8;4OZucL2RxvG(5%aL;whE
o3=a`#y_8umStj*FJMr_Yz2Lcx&q`)j9SH0pg?o7%F5IySq)OIq@e600_#>#i=vf~PLTHF1j`l)OMHn-SVxeI(HybAhQ_asPtGomLE!@}#Mgov&5}FRctjBM
kc6W@0b*5!I3rjp!1E%y1{pp}sDs0ktK$oW4pNy5Sh@wS(=r<{nh{ER9x0Z{kh-ZWY$AojiY}mA(puQ$9mtdAOFhGQCJ8slIqBEMvbNNeXn=VFH`bX@D<Mp9
PP``N0|<tts)}N9tKw`mT}Jb%6nokDmX9D@W#m&BtWrM2a9}s*0BBmkNlRh_%jhv(9v~IhiB|8B<HP9``Fxs!eg~5WO$|vacc?=v_Y+_TWi~9rYeYX{cs5rS
41rKIvSoh(V4(7Vuy%RyQA!I~3|KGZvZ8^Qu4Z8AZIHT+PGug2AZ}QcraDdm#3LJlJ7p^K46K=?S;QXO8PIPLV{Aydz~^o>L&b=7Qa3<@SlXxsc#44jD@N-n
vuu%3ShHeB3=k#?s)q-})`+YDVt_@<17K;1b3mYnfKI#CY4=)fa1adeiNIg0cUoY?wz_Rl#B!|*hSe-Y=7{_>S1biw3uaw~6RCnw1g>IP$dqR^*-+eNGm#w;
CoxJ?W;_s&fRCBd4HgOJB~TG}m(8g%qrTpgbjpk_Sgm2rn(e>W4w|Ai+qdvx)GyertgAf~sJQwF1G)mdE|ra|>@yzypc1;skr|`pMq(A0ZnaPhHVa*%Rlq+8
ahPN6{k}DW{$XNJ1uU-$2nm!PJ787rk}24KK!Ha|jFr@2KxyQIk)|ll0PJ^=j5H4-nl~Y?n4LMM;=P?YqM|Zk|A>ezUBP@Zj3N3S2yb=pRW0z<JEE;y;G(yz
5i=01CbDVnXAx)PRK0MT+|zL2Uo{+HK5+kghTiOL3v|*^i0!4jxCWWWfRO&(eCdJF6hSi$EJAQme3m~TAAu#MyiP+!4WwRzBxKJ^2?rb)2o#{iGAB*Ie1y>^
iz4W>tO^Q%(Ts3?X|sS&0%Vv^T=}e|45PHw>vlT_%}%%7Y3T#jH2xB;)1ot|8s&6LWJ9pQe^OH56g>jc1G8{BNdmSoq#Y55*Dg^JnEe4xE%PM9xr;s=I~3F$
4JBH8>4`HI)7*4ppNW*6bTtG^s>CBj7Z8X=kfNLb?coEvU@tH(uzzS+393x8>d?62l|?zYNzqV_Sw+QC%zzsYc5%S9NSj|z6Az8$OqD{T!VF-5z&7x3?~;cH
nprw45|>U2mVrNM%r`VbaGFR*nYyAPS|H^jh|C56CZ531AHZ;OmCFNIz!^=G>-vOjS|K^th52m&fF#g*wtm+k$g`!CCt0nl1V&W3MuUtU#LF-Yy1D@}7Y5+2
jIiDm$X<(OiV+2rJb=$8T0&<rD;#*GHyS{-xa?s50HuXvbP3tyNnkR-SD;#w6&Zmc>xk1ckS+`KKc|LSCpfr-VKiUjFz(2jLK+71GnM`v$hj!IW5Zw!qH-C=
Jn7&dL5BkrI7~I8yUa4Kq`*VBDuM!nk1K)-yhXx+PGCTn*1<=El_BeFDO)%~1cXTJ?SceZvatz7U60AZ0*iFPCN_JjcW8140*HAjqa^`at;hz-n3WA-A`von
vH)@bw<Uo2AX?eUNXFwdgtY}*1i_FG=_f$t=(Q6T!P-Wd5C($^GF{|KC!>yT1aXhMh*C)|%$M~b8Y?-eR-Rb`7zT|HWm(AxmP7!0V$!G#@@|R1{jTod*c>Q~
;u3)aTh;GfG~=c&nX<^#q&bplKq^`1uo+sxp%hXyPvSh#*Q8XXgpx#!0Ty^(!{c1~3JZyUvcSv^81hIn7$q4RZDBS=Qy;;4;7Z5Cx*@=8gWuO^JYf}Kisp#O
dmP>wV5Z$8l`7!_7&$JfSl~NA>vA#!7NR-9N(ZPe&|Jc4^P0vfq7WM(nrUh91yTiR0wgtHkY&hbO)j9y!2;>rNaKkS&*4C$3j+mvNV;e+J&XqM+$U~OkWNV4
CJ{Fg_9<G?P<`K!wcR-k1m=j5N9<y;%q<X(*+Ca*a)paUg7OsEprKoOy`eXoL|ui>%!7{>QxU8fh<O+7%2&siSHyBDnwlxg<Pgxtu{Grm$&Lj3swgc;m?(t+
0vd>q=X-4Fnb;kmeH0ZvGVtZVP{HvK%d<-+#UQR52UmPxB&E$R!d%N>5ywF9lf`Yna&*1{1s7Wl!)mlhBqDM!#N{mzNf;!g@Bo5EH#v;a!UWPeQ69czB$gEk
v{|g;%Kyv>Zl(UJQopQR9G|~C{D*V=`S9op`RMfcH|Ol*)%nLO=k?o*{{cE&&!I6HsYoao35LnSyfM&9&78}#j~7SB&e`d^e>f7};k$S6^8EPd>iD(u>K_;h
KR>*@?D87Tz=R$nia7i&Z7?1zX^ZK!E43ml`h2yNvFH?*HCNEwKm|*u0b4E`$+}R;!i9Xd2?buH9D{WMW1c<J+@3(JgHD46P<FmC8;JHxKRVwS4WrZ01*t9*
^iD(H_vb57IXgc-ef93}(mDP3-nn{naeVmt(l*4|`}1-MXcrl)Ov7bnq_N2`-Jp33ZdWW#nasLK!NO-dlT}eJ3t>V4|M=qV(cwEl_|fs(^D7E=ld_8zps5m<
;@A><)Sl@X*)7dGQHBz0q3adcFW{FVXGcql>ntRNMqWgbH`iZ)b}X<SjL^SL0hhmsUzi-;AD+HF0oE&|;==eY0*jt}`(OHBev!0Y`Dx<*@{9QL3rDe+8wT}9
i5F}k@c<2AFi`j4kOs%Uy$zrk9-FO>0d>=fYqr`1du(((ui5Pyt*|>DcQH-Xv)X}Wxnrvtc0+I_Iyz?3I?b?WG<$*PhNk7WOtb46y>aKuFW&|C_v+u=-+N%T
9bKBBno2!_=4n}8pj%^8?^>48wTvcoVYXUL&-E;`)pPwZjLB^Ue%tJf!3%PO9t=G2Ouf@A^tf>EcXVhpExp{M8Fm8K>vpYXFZ9hZbZ%Ker|b7xX0O`<Z=^eR
n_kn@1EbRh*DKULx7lrVd%bZ}@3nO95v;=0*&G}lUtGOC0Y11o-qE?$ZnnXrFLm#_ow08kJ;Um>T4Ud`Ol#Z?x?>|~S@6ei2OZA^f2G%f9u326kGp;w2H9!*
L8y0n+`Wni9vq#0I=<L7Z_K@JEpA{Lp>M#{T0OrLSe?)_gCO+vp6~evth3cIVeQ=(^lFS-y?_$5UeD<1P1owQw|Xw}{njG4w|chp(D!<Nujd+W4@j(OnxQ*3
TV2zH`8JzIs~2{x(1JDayRhCJ!)sYhz3b{;(+`?m?m6=pq3e_5i{n!e`M>T)ya^Oi9)b>dc0Jz&lr{kiy5H#rrqvB}6CTG{&}=u&Zs3OFj@5L5<a*$BTgDhX
gP_;*U<fz{>4;@~T+H;9htTTv$|DH<z_Wa>ZS<Oee5>8kgHG7#1p(kUa9z*zff8FCtK<5upydM=+P*vPS*F+W11t10N-w5<%YC-3_SUqUMh7T52wEYMk>Oc-
tJQ0@eJdOXz;0u|XMwN{#(F?mZ>tx2KxAzbSljP(j23sgrK7hftz|qSG#vmNRx21c$KF_P`d+t*ArQaS>~y-#mSOg+03LfC*J}GcBsv$d(rR}@n0<l6iYCi;
$5yx5EqC1Yeb?39o^Al5yFtgYtY*vf0`UKv-N5U0LVesd%m8Kvm~UCFCdd@e@VX$XJArR-$C%tZkU2944e!TOwt8DVx5kD$hX3@YWj3w0Hx2<j%qi$Keb>;<
j&GQ)CP<IwxCcW5z8dRhx8s|x*$WJ}TkIMA66f$yr>$mp3(s!QF@50NuF=#1q;G^R(*=<Q3j$Nq0kzOw)9-*#1qt5qV5QrzASm5H;*G6GoxXb1Y1?XTsR&O8
8a4wMO&i2B@{iZnfnxz)0J9GCjt@)fg7|9o%%0gD1ClM*>W-~m8w6joEJYm7d2Dyvgeh$y*tcLsyUk`Z)Z3xn>~+R~>JCUb4>ScVu;q=t4rqxstRskxcGxnS
ZTO!B3_cE}o*<LX;avTrPEF7)TP&;lK^w(!7}6dU;2T&o9f%9`IxJl1cKxt5_F!#I`0I|l(3{cq1K00$^}ySbTh8?^GHwF5ZE2`BXyy>Q?ddQRBj|>0H?Tl(
gk!heC6t2p0+fPA03Fsdx&}Or+XirV(AIHXzvDKMEw%+q=nMUKS+HBB$(oF5mxKzL2o>#{WnN2puSQ{$2E+UkM>E{K0G8f0IN)h0CT=<bYf7MK6zR&7aS@Sj
(l0Uj!*h3uH7c^@Is8P67^YIe7=KOce~Bw|TS06bF0NN-!JXr;MNJ#b8*UIdt}L!q!OE&?1J|B6r~$r7p&DjDY=mBO9Q4i{M{9sBn@sP*nub-O@c`O#9k&6G
g$nqlF}npHrp8rM`)aWY1$egU(n)UZ6L*@18Vq%2<6IkH`vz&PhP@tCcUYuV1nve75kO7DmKbeCmr+m-c{Z#{JyRVuqGdQs85I@JW~f-T3}nETYGoS6HBYnc
#jr|msv}xGxfTs3GN{p*gzF#zr+QiA+We+E5(xWCOu-*?3GCspy2UkBkuDc<dRr>6s?j^Z7`=j@)p{KTOtB69)<$Aj-67(uB>>V)E`nvliy`B4RaA{C0(&G<
{t%RE!Grl{+S4>qgwjYJG5jAw%38osMv@*P;Uh6*+ka|mNthNEcFt1`aI0%WV5|m*u+US1A-w|J)GrID_lNpO6MO#9=#NHX8LpR1%Dy|t<dVZ)iY&wF&?6FP
g~nN{LPt(@9|1<%eicalx~gf7d)$xYAiUb5kuC$MD_}MWhW700YB{cVfiE!^oL6Y1;D0W0;{=c|j7y9`piHt3A8~~ApdNDs4(#8+5E9<wRV;OD+j)goyDFeW
BRo|9O!%TIa6UzBXl1-b<BH?ph#kkatB!+m)N!hPmZ#(+?_j!2GjRAP3vgt+4lt&P?PNB(o-DvUr>rW)wHOlT+Hunnrp+k<#oJ<L?wo_2X)%;b@QRuAt32Yz
TkgKZ<sc}h<FW*es4N$5oML(k6V@2A<1}Khp+v<S8D+yva18t<cT)Y3y2^Bv$}*)&OP$C9jAEQTr^t{U({Sm)V#6}59bg&<C@fm0HC<yZ2Ru?+YyCxt(Vz+`
k6<;Mr?s_60g!VWZlto2`J-f!+BM*6QSBq&5s!s62`xyLHCK2UymU3It@k#>N^61Jmnsj@oT|tcoXbyZp9L<4polf`6)3;ebZHNBSu`)pqR-5J)5Jc3*$gI;
jp?KTZ3$q7IG`<$3m26J10qN_;_FUG6`<V6wr~2lTPBKEAr-owJs;xOMtild{7{z#pw@v|ZJgwMcuVhZ@#XDEqmFK|8_M|CEDfRG{>{dQ8Uq%nO96mzJ$lR0
`Va<QskxrOS6Xoj4R?<F9zn{2>~mRkdz!czX=?PYZR<Q0{N=rbUyKf1Kq^P*vW9Qhy#qI^?Y`9efI}ajC$tfcvU4<?8F20dlmU0dKmhMRQnhI!i?e1JM5Cr8
<f0e$G}#&jFRhx+w<_-FTvz*%s8YJP+Q*qq6HsZC&93%2PxyFTSZ@+RJ>G@jP&ZZX4S*5rgHA|6O7#nf{H_sw5ry(tm=<~8MNN{VSQ1$<Xds^fZg9xyk(7e0
N*KMfhbOQsd&~V3SQgG+3t(odH!P2aG%U^tQFy1l(EHqt!U@!8r108?)2u44Fb-sQO~rNuOkll##+Iecan+}6-0f0j3oSSE&;~RM=-5RTHb9Xlm{YNbxNXlI
?XZtMW%yE`TYB`cXw-Vz;M$&o-CF~hUON$oVC=Z}j*`fL2W{{fOvV#HR^6v%xMMR0CC^-3Ya=QoX(Ah|qz|mi;6uK|v6!fKP?2+oPzSr@93d({TKhOI4k?Bq
OeP?fCR!aOVjM%S${LtVUh0Dn886=*OeQ=?>?)3F887T_)yryM$;J-?@Pg8jG_0t8%wK(0uh;|l4vlYt0aN=M3Pt?+_sUz|o0aY7TVmuGqt>`Ji}qK^omaHs
2zjTx(JJj{d$I^#c@LjknXM?%LmT*J5v3b$u*eI2ca?@R9#7jAvkhO_-YvyVv~T^Q0q<6!vaE78V-BMNUj$F^l#**A0Mz@MIH?6%Cf<A!NA=*q2RTP5Lh`L)
ftDc+HC`Ch=m&^i+)>8VfINh~)Ry8F*bPje@lq^s3jmK4ead@V%8!d7EFRdl+F-R3t77p-Dkc$_+`}3ptZJVimP8*we=Pi{yT|g6M*$+xMT?06;BTNG7!}eA
jG}t!;Ho+3Z$tS#lotzD_uu89(9`1G+YYDW9l5QmI<nF3OH=J{wt-tS@YiaketAhUt)=%`_Pn~Mc@hpYS(V&tnKoaRbui<+FU2BQZ+(gHs>+ChWRb`NST@xk
M*GHy)b_sd0tduU7&&AO5Rlq(ADU<fCRT-~l9r;n%Y8#skwUQ(teacg?sQu7pFs-~B~FIssu7DE$-RXYH^6<hl!hXsbHTd|<ZeYW81wHDirWxToM1*t?MEyq
9!jS(1i}}XX!f_;KCa&FC^tNi3UU3*i(g*((RYb(wd)a?L_QDe#%Ne&;)T_>p__i`6`0*ictKRdv^p9*s^Acf%Ub+A*y>=4LUrFZSkr-NA>Zc)0__c~(hMb^
j0AVzFZM3DB6ry@^e75LDVNLX^<i>C4yA99eXtdb`SB2p^uD&TGF9cGvQk5{8x0@upd9Ju^`CVJ1w|dIeJSp%QZ!fl7umRZ6Kz#uud2`p?{SYQnCqu!&e?CL
NWH%uAO06muk-fQIXZiP{_gnd*f~GDe0%lw)3I~-`R%21d3AAob@awLyLk2Xs`_0kc#Z5aX6>jtRReeN=-tQ5w`Zr)Q&fXhTR0rzPxc_0RqKWtJ{2+xWpi+N
`z^ndWm&LljYKXBi4Pv^b;D2Q8?YE2hLRL$hXoi%Hl>4WC$+VFLw3T0q|vOFlC^6^-DP=O0K%^|6;dcTP7m6SIKmhQizI{_xsZsozGsiiW)4FdHz?-7K?CtD
P5hX%y(^cHdD~a?#Z%#{rhfL_QML=!rTsyH+(2AOyqnNpR#Wv6L1B|I*k9YRSa3nvpT)gsYC1pT*v?#(k^Fw@&;Chw_val{%JrAp)ZC#l+Vh6ysP4iacrr#p
KIvGd^IIXG3@kJFt@3(TF}MnBj}MnCP~6gVL=~wO#k~92LcO+&E!-XU@5Ba7)%I$4jpEm41*r4f<isAuuB!C*n%M2L8f0y9a8RnL?cFu957g@T+AqKM^Vi$9
IP?s5acQ=5RC1r%wmx`oHql*x|3(9VVC#~R{Efs4eFr3sK7V8To1xhs?ZZEPGxzj!2i#!!vH^)By?t12@n8=>4<lBZ5mts87zl*FH~be23~e+BY$TkuU}AuF
T4v7&V9tMP@7n<mQ);ot-hUtF1KJs??Sb@whYkLDz)(SMYT%sJq@naTFk@k&%5ZQv_Ea5ZU4Lrt{Z_=bZMXL(dwUj?W=PMS!f#dFNQ25wN$}%S5c01<30xij
dVJwr9ba7>zBzt<aVW)iH5UQZK0pLfoy=xQ>?mnc=-a_B6G4YH;9mz&eGQsZd(=S67AKFv5u<WjbZ}iS1;4EXq(~p1x9GOY(#K(8FFzir_9YHQl~Lxn*NZSr
9W=L`LkDae=T)_j;`#g25|nt83;+}>;HKUI4{L+eM&2#>qjMJG6nWNm>4Wr#0%=8Aon>D^O#ir`M9s1U(>tpKxc3mp*l>q1z4pP6L4mp@ssB)p{%*_faaoq3
8&wpKEGgFe&k5CZ<?U)yf3D4J1s;ZQx7wt8>)aY}|Ffig5YjM&p8@58ac5Yr&;c$%AqrbtztpvQZT+GUq{SfXnj{yxJ84AUa{EvwPV#Aj>$lc+RH+fJ1o{+O
R(mL+-f1~gtw%dr<7b0eD{wT*?QR9PR5_9Fxx`tkRI2=nvG!R+K`KsZ8fY0(1W}1dfqo2s!CSfMqaZj1A&i1nc=qsSTcC49^@by=qX7U`?mPBTfED#?DC39j
NYK9?!ki`;(VIjC_Z~)Ei^Pq%&DY^G3;^2IWqWN8N^TKCT|ugIokEGMQ)neMR~mj5xQm^>MZz&+gcBcz{XTd?ViIYiEbKwb2wJeJx}V^NUQ}S{io7&<mo5$%
eh=$Fg!C@}p)ZsBXlTxpd5yy#_)EG{5te|qoF+r;bAJ-izr5&DLB6mu3Xw06YELEABIkY{f@U;Eh)+_NBTZz*X0ceq$fmz($i4YAo?B4W4GLM-Fsuw6Vi=wJ
gI2dvhu@AA?Vz{?1BYnlP0?7w5aU9b4@?)}*u6musgQVkqrJ47YC~-eOBR|fOBO?G^it0OyeXyZKmtN*sLWuX`%`<k81}7Ep~YzM8Vk3|l(l9f3~fLWj4<F|
SpWnmjr{n6l$N}}9csd2ONB&;eG1ehkR#yF?P##Fb15>olRtbAkAr(V7iNQiEf-g;RFED6A3;#cas0h<8LjgVc;X~3e#{X9d(hY2{0WTuKz>t^(~2?stLT<8
YDK#zGlx?Cn9LByC{Iz~nxuP6nO_Nlm-4fE;*#1*+zBv;`?4bn*wx6ROvx<8U^Xfr_&+L#*NCB&Cioc;b*HHxw<823F%Semm2(^4z;Nb-q<Rp@w{E<tQP39N
yqv(8wnM?E;x&w^h`;M=8<c5nZ!UsB%NC!8%jCK|IJmyfCpOpiYe9fzLMxbm<nr-Uf$G|1cT17RU`}dFF$Y@H3ZRf4wLGA$IxkW3XXF9w$Hz5A!AHh(9#R@d
0_Ho>$|1RYvV<Dkh!IKJU2iAQl$eOc8pb{u4M510rGBg_83VsyKo+~yLzM~fH+>$Tl2zkK<8i725EW2YhT-kuX~}TswxfXz%-h4)J743M52^j_`(U|<$_QY`
BA*j=Eg6teiR=qwu<dVuj0PU$a10cQ2$7@0-`_J4&tYuDvcExJ!;rEM%*;NG6OAyLM3EFA$pQ5g2v;#2X$m=jE<vRT9w*lTgOpzE@@Ss(j<zWBvsTA{Xh7ON
J~C!(+boIIyR766`oqcCHk!=%#2PL)GkA6?)=wP<HvlyTsu_}$q`D57{CNWSCTrWz>cc7%qul_-XJt2BM%pe7!&u7UWfFkeC*O)SDi$zt+xVF4Of-SyNjC(b
kAEag0;8~797i21ZDEg!ScQDXSL~2*#+uy~`}b{)fU74nifBQi86nWh5NKFv2W`dLci?$4ynXvlK_g*Ek0ko;4w^#A$PAFikO=YYnUOFw4j7u?_L&Gl-ChLA
mAE15N1VWsj5w?xg%Q>qtmevt_cC^YKGJ&cNPARe-~n4c6}@0fQ!BLk49ebBRsjON+w+R{tgI?L#cH30mx4q80G>b13np{~T9anxiT7HTxXqjdms&_G5zR~B
vfQy?5MGM7bzMTPEV!Y9XhdkfJVCL0`5XTI_=*0~^YI({OV48zNP|22OVW8Tez5gH_>cuZo)=ShBo?>D4;upy4>&+MdO6AG1kh-ZUIT{EFDd#5*aZ$$NuBf>
Wc0(nonAL+qYL?moY)524&J`h`<EvLiJoV(<$JJJFMlgn$b@!o4SkkM=qBCa3CIf49f(GQ8~Y{&HXq;@Xk`ABXRib>F&or`X|qKFv)itI3pDG`<~F?AqcyD~
P<*@{sa+TF9;`?JSi_n&of1*GeF;=@W8d;1pgE-puWdr9M_W7Y@*N#FBE23d)TP&8pM3mOve_AF&>ryh@wd_|oC-}$;6XGbu~<v6l$CB7<1e%&5(Z&NQw;^M
+(THLwl<i@wj%5>6jaPq{eacAK`dtWP|?@|E&bg3#W9Qqacr|S5QCVT(eq5qpyf=K!*dW$m#!Vhd$U<Rp6$i6ETV=lUg|kX*B?SgzBt+o!~N_Rf|}FDUK;Cc
2Hnv(W9$s{<5q<j`&AWUsPHV6=Z41+Me`o65HREO#D4sy*l4tq-j9EKRHu+@RHi~S+B@Ri10a>8mlBD%%>8l^w8GvG>7Ap~Ui%~!k2tn-9WGAnT#E}fj2zBH
fm=py3m1xF;Mx8x*l47`g6*gxp=m-{X7XR5OfmVd*a~FYQjuUUrTCpKl}$0MZL@k1Dv(%i@OxIC)rTTFI}VfyO!o3bBMax_C;s>NjW!azpNC%mCSS{ckAH*L
d{~Kt^L5bpy*v@>1d|*qA3q5`w8deJ9KRv34&&<bH~y7Zmj$x&Z-i3^2@nvQ3O>z)Vs3mak9>8<2$#PA{nQK({Nc139+TqGeC_c=5lZ2OnjZn$*))9Ee#zy{
y#nzRQbmqB(W}q{+Ai92i76CVPbP5Cg)i>)c@%yv#ad~<yb2Et%5}|AX-jY+9E%%+e=s1c5}t=uimy~ZRXNa7Jys7V>Vb(({lYb_Zfz$nM|WTSXmt0(pN#JQ
xybJE#aTJHi^q6vheh?#J_b1jhCBDOu;@MpLsh62JmVeB>RGdT)~sG=hABd9mTt#|_tM8P-YAa4MX3)Nh=t+FK&*jJCWmRc5v<Nuqkm19mygtlx5K?^jNEN8
;Co#N_ZpOO1`$sVah-p@kU#YwhyZ{1&yN5Xqj-ztKK=PX9=3WmmIoeYF_=g7x8r$KDE%>dE(R2~Vte?0G?>r}<-HbO@V6+^v&4;PQY98*eA0_}BErXG5vJTh
2sV{6soas$r9%&Mk4!#nGzB&jRUm?AB6@S17?&A}o6n$um>_UX6w3oNnkK0Vi{JAu>Pd7xd9<He8O~rwO|o#9()JVSg}`*f@mP)$Y6jY10Z5!+D6O8A&a*ws
RQ;vew!E}I)S$YcQjLeP<gLHglWa2vM!#NA3GoO%$=%Hg;EN{!;sgoal#iduz`eu*f(8#cFlhRsxQTk;Eof6Mk6i-U+VRW-Efqq=m-u2QB;1sS#al7iLp*as
#siDz@*=HO?vvFNkNn}2IaDnq!GncMyDGCN#1D)StFLXQ3L>1jB#}T&aYKUmP%|*LsSP%}Yazg5HTj_yMjh6rUmHcV0GC#<pRrCMUaG=eYq8NZxdTC#F|5bo
%>ktp>~Hga^wj49-v{WNNZae%RzM9~57#5X51Wy4l4ZIu8|C*bb~?zysl_NNaf38{cf?Z*+_EFAI^Pvflsv<L=UFgO#Z6U2^@UZUpLFH>_O~q9xJwjaR8~qK
a12>ze+D@qKBJI850SejACZG~_P3~C8V}2mP^i|CY^_2J*eUe$eSmgmHc?rM!)LhA4m?{Bs*B`Co|+1kW$%w*=Rgo@=7*z;RREy9Ag3HtjK$KIVOajaL$>6B
<Uz@o(vhca_uKFEKH?V!V|%%**j4j|g0iEB7ZQp$vfY9x$FkB0i#iP6QS6-dX@aVu0^3%PIq(6U?PZhOiFF44#-9SQQt@cu+0-@v!cI6K>ix~8qQ30YQ$bK_
%`lYn>S+p!H`*E|)st#gj!=>5c1Ry94ju*mQ7tbDL53$H{q}H@{$ZG(Toh*5;O6P@^7FB^zc65r!zxFyOY!UM+~iV3A9KCWhxAoI-z*07aq{fQ*>)}r2R|0>
9~7b#|9r&%4lK;2N{SA?uEJGVip^7r49?T@?&!P()0h9M7(KVhgY+1lmsPeR^s2NFq+d)DVw?}Pi7<41uV(Dy4idCgT`#4`k+z)`EDH7k?w7Q|>_~*Uhkq^n
s}=Dlg{Z)q+Kb7v(0;dvECSbDy%hbHv6K&(P?#pZJ5^Z)aOH9{lsDaFl$2)|GRNh2v^sxB>HquCe>%%h?1F57LV+ln2KXm~sWDJ-chD>*9jFpcNwzG)QppG{
%ad>&83&Rt)gT!^rD2pSVw!?6a%4Z7UD%naINB?^NI#sZm}`a1?4wMDR{}bhRd;48czVh`K2iq!d)&YDNBIg61;va-2^8il1m!LiNXl3U3a|d#@)ofTvL164
gNcvE4L<H2DPKXn*D#!{e#QBRR6bIsJ1u_N`K*X0O+B}Z7>IfHdlO$FfP>&Me!_*Yvq-z_UfMeft6-0DK7k{1L-6aLO_yLTnK8k~opEHU^L*ZftNdK*WQs@Y
rc2s##j{aq4mp>C24R5-Hbd#lYCFX{7YK?PaJj-$X^Sl|k5d?QRv^2ZH`(KkO}xeVP`byqqp~qa8phr|Kh=s3CM@`V)P_<D_-6FdRw<sFQD0?mR%&E7#SH=1
oXN56@(fFv9jqZ#&C#Dp*vRp38RQRJ(*!rGMB1`ARD>Ohhdg%!{C1b+ZSL~CO)1tOXPL(vek3QuwHeAB(=CBkDnr*F%0`3dIOb961?#Hp%O5h%^EsG|cXp&<
{&P|&i&-&!@>ix#Kr8OZo>1xkPoVr?NuaQe_Wwv0Mec{MzWNvCP#ztTvvqKYJO!QJ(r1@^P1fUEO!z=rKK_I60z#Ug4Uf2;@rsYphUV&483Z`S%VP@Hr98T_
27KqJc=-r^+PMJLB+t&3SK*{|H`SUCk*C9#sqZK5>Dju6g<<?f$B69wK;Tb*aixxrv8(^=sh-s@@!7@e;|u&e#>7(udZLS0|FnhC5k^bkanr&QO##2)wIK{s
7)@bxMQij|9CQMDs^)_#Q}FOuqrExio_x#>%`x}nXK5$AW2bgr`Wyl4?tR5{64r$$T^>uohm)WMdoIq&emy7iRervVGU8l&X>zRkB>S+<pN1~J>B~=7v#2CF
ALso-fC)FD<BPx9a@TmjutR*V<(t6^o6TiSo0{mO(hl=TP7tf3aaY_uu3TRAo=gZ?0e-8o(`<c}+`>Vgm%x-~^c0F{l54TC)#?a-_^Ql=wb~qCoGiWA+q@{f
k)OM5_T2h<&(jWSoBH~Zs|5qmid!#u4RD$&MM+;f)p%mTA2^;E3BsT!?qLgx?k0ZmNBfK2LSHg7dT?-EOpW4PuH`4~R6%7+fk{^|U|?Dri#%?Fe(yZ9>JJX5
Qj86te)@2ZfAIkuPkh@$XKp-o=*C(dy0I=Cx*@B67#h|HNZhvh$sDOIUHlufjO86WAMgthWAsA3-{rM@$o8ih7IsEQR&abi^Vvwi@%N0+9#{0?IR{97)%XFw
J;{zFlD~GGO2ol)zu@OG$=25O2eE<wKS&3c28>~PKP?a;7J{z4cxw-9D2oLC(F8mjg=Z=^G;O55wF+?>)L0(%G~>%#>>+>}4dhj37)e-yjw+;Bw(t~#RpJy{
XE;0O!+GQji7q^Q#6Hgt5}}ZooK~OTk|d%>b=Z*<M^x4?_or}nPNy{GOK|aIC!CT50fDzzaAy~S8MR*cjLp~bb4z69C%TqzW%UaM($CxD;4k`l)>6{#g>BQ6
WX6{8T{v$6kWS|@WuG1Qhji*xDPmPPM~7gIzVp#0*?N@6%xk%$6WP7`*uPJaYcA99paYm8UUN}=odGRYKqbTHpJdTmC=rFaM3LI}V&Xg}5``m)q0&oHJ;DLu
HD~f*x<1~mnH@n&=h=|SMt8APOJCj6Ihqa~Y?Ph#paiI>vK{Kk`xn91$PB&gg3JG|o7o+gh35x&)`Z-@5Iykqh%j|LDi5p{cY5z`Qb!(*#n?71QB`=9C>B*(
mujE>`7T)$ZQdGw=p%AAm59O8;m%o&a>c+GXi?1_<A92Wh5M_L>4pM^bUUKW)=a+9g4@gSj*6dREcpBH>ImiO;Jo||eJSh;HH+WQy9-+yV_7tQ0jh!e--lO9
fE27I)hAkPDk+FIn|dZ|PJ1E0{4VGPWre7_LJP7W8$U-U@W2>#X^ynE?(rr7x~F5}PRHpS{R6y*AWYSbw&-H;9c1LD$ggcE^*<@<kLS&$if`94GgROl>u8IL
uWZoL3u&pA5*R$WyKHhK5&)}{Jhzu^w8krFMKTSX34H`ctNx5k=9*7R<N|+kdG(wTKy(7=y36lZ<l8Ng(5LRaN;_k)^DGB<P8pV*wwVrr5Dj7SNj@iAw{vda
%SqSFaT$vS46D=^;gr9hQ->Ed2pDbYP#1N|+tOln^L4D;Lb<tvCgK)bWH)~f2wK6XrOQBJrn~R?%-q%7J*C=s0qJw+19Wvd1T;Gs=JngdU(Zet-(`oxY@hd1
Ey`%ZG=8E_2Q~C%po?~4De8ZU)io{G3M|#DFjjz%caJ&QX);oD1_?@O{-9q}(VbSp1`|w<yoA(|k*8$gWC14CCQckWBgcX9IPy+Whwc=`>hjVh2O($22K@U@
)#F2b1^enYEK;%v9lTw8*E!Q{SF*LQ4%6E{S6aGk4FcRp%$E+0=HrX9I~{f$6-|dU{n&X(0|H;N_y#+A*ghHwTS?D~?k2MzDWu#}R1;ya#Va9p0G9CbX-LL@
gn%tLB^21U1e0wMmcNIJg+`(fU{HNNbu5tNjMC{q|Gwjawoca0!fDxEwJbyO4QO?`7(VkyP@3?ilyUhcdK8PRpz)JYsy}gx#lQVXpg(hZ#b0v31jnR;e_>o}
=H7;Cj~xoObGsn7%UgC!W|nNC4c=_;faR?RrHyCj>dW@n&JPvv@GCrgz>nB73*A=R(Mw+LM1Do&;@(152J*yT_2GJX!|J+V%{|!aJLUQ$YyH3N2e1NFWBBz#
SKeQyW$CsxS)*Uvyt%u^jvZWCMGSq&dRs91vD|i0U*;cq$9SSseNuold8v!)8C_h*$8UOJcJcRs&!o=ow57ZhhPfq!=9hyv$RY|jxP;$-58jkNS`Uh2*vHeI
0#OWjeXG6!&yWH$i^BeGNiuJ=(LbdqnWlb5Q_?B_3p_><!v`d2AFIeeeXw8PF5O3Y6}KTtzpNs_C&B7NHHpyxlQP6z=Sl;r+oB$;DPn5O$7ll-U?|xdQH(1O
+<*?Q>>4LrxF!OsE1}6p2nqSIi6|cbhSsiYt3!se%#Y{U>eH00OxgRcZF{)UaXz>IKn}p<ekj>c^plFd+nq+6X6J<i%G^gspp_2iPrMsGQl%<S!xt_Hl3G<B
eJ?x@e`R-pRZF;_sX~2i)Gr+3ziTz1o5yD$s*|(m`U&UFM=+KTUpd&9Isnn-j2HfUEdM=`|7Phf{IM(B_19YnKYeijqiZF$vTt~SOID|@?#|@v%=rp%d5gEY
AQ!}xhd1$oJ?qQU`{|NHEC%5P^i5ZOgW*TFP;OMB?a`gk+ZTc_<yDDb0?b1n6L*2SyO}PnEZjXE(S@mnd#q)`oL$UiDwBBXe(0aiy!i<XvCIx~mneE_fAuN<
|I#Gf#qo(feCoFN(SOF30{=1Q*&iM2B@c!^RA(u$!S!@3YsYEjpZOSrxdKs;#3Mejs0b}q`&K2iEaRe1ggMO4RU9Pu;0C95flzDo^;lVUvn?e%e}M^^$H(QA
vN?1l2YKQc_e<~bui6zt&s4%&LMSvix!<|RP>ILqHWsEow>6MwJlwT$dz5Xn1C3nT&PNzH9gfvO3-p-+F3CCWhB~M7A7l!pun#aTZCs*VON@fNpYpDylrpR7
ed+xZhtTlc`J@5d?Z-z~GMVszWL|0ObCdJz2nDTpI6*d6{1Qqn)vm({aD=P-(i^o=PU<g0Fw8{aSdwcfsgX9wRI|&6c#GV)qyPy(d52tKEBAOz+tfq5jQ`SE
2Wx)*%zNe#z*k!dh%nk)hX-LO<wO`|TXDIz+&zb@o$KcDc*F@xf#(m*vU3lFI`lwfCmyKCWq#xV@2CSh&61nAYGPPl!(hXG_=}Cd${f*bw&!9yZ#xkk=f@qW
y3mP-b=}={F%kP{mt8vAL6*#k&+VvV+ML`!wVm#pGIjd2SBwdW_lYTT;$N~aZ6w$plJ)OpUHR|i9xHIWs$?5cRgkI~iQ<v?1h1+l!C)N~ki3__^CZ_w6)`Eo
oH%^R`^KvMamp#NaIH%2pd{Z}R_%xBUl<!i2j;1ZGvL?GyEFd!d_FLxooTXbJj`#L|1Puz(?Ki7+M!);1ly>3@*hJ};6ZVm48eMAA5$&$m>-l|1Xx%uu3jw2
;gwbqf#Ip}>LXu1YxXd!wY{AXWK<5Ru=?C#u^=BDV5Kxcm>vwCKV8OGk7xDCKEYiPJC6T-zhg<tC*Y3gP({v*+QV7>(;n|Mnekm_C<ortf@Ggq<FR+Dh4%Ay
$dtdB!7YR3bWlVa&L5T2DgJiN+M6c(lSn&g4(JSjy9U3lJt`@Drh}DV*w+B$g-!JcZznaF0q#+JK@}(`@+$}LIVaZV;|pE+;meAyFi{?a%FM{%Wrf!o4>^Yc
N3+$8;7xe5UFEpE2QNDq8O(Fc0L?--mUSyH?V5xDGXbRF6HJFQK)B&AgTgCX=hQDAunwKL*J0%vUUL41CdNa>E7D;yJX(S!VXKi-s0P|Ff@GU3^lm1}6hF2E
xrFi=2xPk9{fT%XJaH-xjy_sCshMV{*EB$I%)>SOtT$V&ZddQ&c|G&x#Ku~6e3vf|6<rT;cNo<<;4kv2nAZqQEZc7Ny4_BGvDeOYQ+BH|UQ%#)`r0{p`|jQG
Yd)&_?Copk@*OzXXRj`=E<PSz6%tQ>kYvyORyI|ueduYcnC^jq5>W-d&I;gp_bJnk3n<3z4eHv&ey+op3z6}XCaMpP^gOrf45x{hM3n6UTN;)+aHL<GNm%FM
aT_2BL5oZ+^Eo^?UI=d;1&eBeB2f2f!LPdHm|`>Kc)C-EmXE8`cUg70cn9=CW6V6RUo{SzxCVGHEBqpw%f0TbCs<RJ8E|8HUl0+j3<_-BB!DD(c>0fQYprtc
!K&a*8Q3@tD-XF}A19T2Aoj2>UG;o}Mx*+@bf*WZ%b$q;4aT<23O%~@yE+)}$TA^`XPck-XPz9&HbnzEtD>X_MM2vY773%81^pokDkB4y$1m`r%~Up#R*`Iy
SxI@b2No50$wp3DqPoNneU?=r38oxd8aHq%H4Xj&P4^IPN14iTsh>_teg8igr9eR
```

Part2 follows with the complete numerical production code and compact exact optimizer/chart checkpoints. Do not interpret its low objective values or E30 BEST filename as a positive construction.
