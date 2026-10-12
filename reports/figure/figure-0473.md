# figure-0473

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Quiet Finch 32 — complete first-knot C40 affine-U1 exclusion

## Outcome

No exact strict `110/additionalweak000` C40 member was found. Instead, the fixed-profile obstruction has been enlarged substantially and exactly.

For the raw rectangular support-stack family

~~~text
knots = [t, 81/100],              0 < t < 81/100
kappa = [
  [103/100, 7/50],
  [54/5,    119/25],
  [53/25,   971/100],
  [21/100,  17/100]
]
~~~

I prove:

> **For every real `0<t<81/100` and every SPD Gram matrix `G`, the resulting C40 stack cannot have strict `U=1` with additional-weak-U `=0`. Therefore no nonsingular affine image anywhere on this entire first-knot fibre is strict `110/weak000`.**

All eight curvatures are fixed positive, and the ordered interior knots keep the standard `N=4,M=2` support-stack maximal incidence `V10/E20/F12/C40`. :contentReference[oaicite:0]{index=0} The starting `C40_PACKET2X2_COARSE100` is the exact strict222/weak000 checkpoint with the two-node physical/polar packets and shared interface carriers described in the parent. :contentReference[oaicite:1]{index=1} The earlier generation had already excluded its fixed raw profile and the unrelated one-coordinate interval `kappa[0][0] in [99/100,103/100]`; the present theorem changes the **knot geometry** and covers the complete admissible first-knot range instead of revisiting that closed region. :contentReference[oaicite:2]{index=2}

No supplied-source conflict was found. The required tree-reduction material and both literal parents agree on the C40 graph and on the criterion that any weak-free mono-U metric must contain a rooted positive escape spanning tree. :contentReference[oaicite:3]{index=3}

## Exact proof structure

For centred raw vertex `p_i=x_i-c` and directed true edge `e_ij=x_j-x_i`, define the symmetric arrow form

~~~text
B_ij = p_i e_ij^T + e_ij p_i^T,
tr(B_ij G) = 2 p_i^T G e_ij.
~~~

For the variable-knot family it is more convenient to clear the positive volume denominator and use

~~~text
C_ij(t) = V(t) B_ij(t).
~~~

A required positive escape has `tr(C_ij(t)G)>0`. If a subset of required arrows has equal-weight sum

~~~text
S(t) = sum C_ij(t)
~~~

negative definite, then those arrows cannot all be positive for SPD `G`, because their positivity gives `tr(SG)>0` whereas `S<0,G>0` implies `tr(SG)<0`.

The entire open knot fibre is covered by thirteen closed parameter intervals. For each interval I preserve an exact blocker bank, and an independent combinatorial verifier checks **all 315,000 root-labelled spanning trees** against every bank. The exact bank sizes are:

~~~text
interval                  triplets   higher   total
[0,1/100]                    251        0      251
[1/100,1/20]                 264      708      972
[1/20,1/10]                  347       71      418
[1/10,1/4]                   410      540      950
[1/4,7/20]                   553       60      613
[7/20,9/20]                  573       51      624
[9/20,11/20]                 615       66      681
[11/20,13/20]                577      208      785
[13/20,7/10]                 588      138      726
[7/10,3/4]                   574      153      727
[3/4,4/5]                    562       36      598
[4/5,161/200]                545        0      545
[161/200,81/100]             531        0      531
~~~

There are `8421` interval-bank blocker entries in total. The exact coverage replay reports `315000` covered rooted trees; `5197` rooted trees require a blocker of size greater than three for at least one interval bank. This is an exact exhaustive graph check, not sampling.

For every blocker, the symbolic verifier reconstructs exact polynomial `V(t)`, first moment `M(t)`, raw vertices and all forty directed edge matrices. It then proves negative definiteness throughout the associated closed interval by the signed Sylvester polynomials

~~~text
q1(t) = -S00(t),
q2(t) = S00(t)S11(t)-S01(t)^2,
q3(t) = -det S(t).
~~~

After affine normalization of each interval to `[0,1]`, **every Bernstein coefficient of `V,q1,q2,q3` is strictly positive**. Across the complete certificate the maximum degrees of `(q1,q2,q3)` are `(8,16,22)`. The first and last exact sign certificates also remain strict at the degenerate endpoints `t=0` and `t=81/100`; those endpoint checks are used only to close the proof intervals. The actual C40 theorem is for the open ordered-knot range `0<t<81/100`.

Thus every putative strict-U1/weak-U0 SPD metric would yield one of the 315,000 rooted positive trees, every such tree contains a certified negative-definite blocker appropriate to its knot interval, and the trace contradiction excludes it.

## Search path and useful negative lesson

I first moved outside the already-closed `kappa[0][0]` interval and tested several rational raw-profile changes. For example, at first knot `t=1/2` an exact fixed-profile three-arrow scan leaves only 25 rooted trees, all of which admit exact four-arrow negative-definite blockers. Other single-coordinate changes likewise retained small exact blocker covers. These fixed tests suggested that the first-knot degree of freedom itself might be sterile.

A broader common blocker bank over part of the knot range initially failed on a handful of rooted trees, but exact interval splitting restored complete blocker coverage. That is an important methodological point: **failure of one chosen equal-weight blocker bank is only a search signal, not evidence for a feasible U1 cone.** Feasibility still requires the actual SPD sign system to survive all exact dual/blocker tests.

The resulting full-fibre theorem is materially stronger than a finite checkpoint: changing the first knot alone, by any amount compatible with the two-knot C40 architecture, cannot create the required weak-free mono-U metric while the second knot and the eight curvatures remain fixed.

## Why there is no new S/H/polar endpoint

The requested workflow was to rationalize a surviving U1 SPD cone and immediately perform the full face/vertex/mixed-edge and same-centre-polar audit. No such cone survives this exact family proof, so that branch never arises. I therefore make no unsupported claim about `S` or `H` for arbitrary metrics in the family. In particular I do not infer `H=0` from a Morse count.

The literal starting checkpoint itself remains fully audited strict222/weak000 with `S=[0,9]`, `U=[1,3]`, `H=[[0,3],[5,6]]`, and complete P/Q landscapes. :contentReference[oaicite:4]{index=4}

## Self-contained exact recovery capsule

Environment: CPython `3.13.5`, standard library only.

The capsule reconstructs two complete verifiers, all thirteen literal blocker banks and a manifest carrying every file byte count/SHA-256. No parent sandbox file is required to replay the new theorem.

~~~text
parent packet result:
  figure-0466
  SHA-256 7939f2aab5f6b71911d2546a87ee7e3888f045b957e7fec261e0531f15272b63

parent atlas result:
  figure-0470
  SHA-256 4cbe7d503594c8444a82e37d267031c6d2b792c1ee5abb4e486ae8ed9d261922

recovery payload text:
  19,815 base85 characters + trailing newline = 19,816 bytes
  SHA-256 8440046a73971d50b3d0833644bc0e694779dcfd0243cb6c70af222a19d2ef87

compressed LZMA bytes after base85 decode:
  15,852 bytes
  SHA-256 843af2686ec2206c177b6eddf34c9b2fce39f32079a6d3f49c33836dde526307

uncompressed source dictionary:
  146,378 bytes
  SHA-256 c8f3e51634303a9a0c7a6656337471df40a66414983b94a2c93814bb4fc3ab32

MANIFEST.json:
  3,009 bytes
  SHA-256 3454e0fdf116315ea27c795db99faa372f4ba6c7451c52061bc503ac4517204f

CHECK_C40_KNOT_BANK_COVERAGE.py:
  2,925 bytes
  SHA-256 7ace185f905710756f55a344b6b74a5cfeadf6cc44daef97242c26ef24633823

CHECK_C40_KNOT_BANK_SIGNS.py:
  3,260 bytes
  SHA-256 a07e5efe25e4ea9895b730ae573def413d41f19dd037991a52ba423c99f0daf6
~~~

Save this decoder exactly as `RECOVER_C40_FIRST_KNOT_HANDOFF.py`:

~~~python
from pathlib import Path
import base64,hashlib,json,lzma,sys
RAW_SHA256='c8f3e51634303a9a0c7a6656337471df40a66414983b94a2c93814bb4fc3ab32'
XZ_SHA256='843af2686ec2206c177b6eddf34c9b2fce39f32079a6d3f49c33836dde526307'
PAYLOAD_NEWLINE_SHA256='8440046a73971d50b3d0833644bc0e694779dcfd0243cb6c70af222a19d2ef87'
def main(payload,out):
 p=Path(payload); assert hashlib.sha256(p.read_bytes()).hexdigest()==PAYLOAD_NEWLINE_SHA256
 s=p.read_text().strip(); xz=base64.b85decode(s.encode()); assert hashlib.sha256(xz).hexdigest()==XZ_SHA256
 raw=lzma.decompress(xz); assert hashlib.sha256(raw).hexdigest()==RAW_SHA256
 d=json.loads(raw); out=Path(out); out.mkdir(parents=True,exist_ok=True)
 for name,text in d.items(): (out/name).write_text(text)
 m=json.loads((out/'MANIFEST.json').read_text())
 for e in m['files']:
  b=(out/e['name']).read_bytes(); assert len(b)==e['bytes'] and hashlib.sha256(b).hexdigest()==e['sha256']
 print('C40_FIRST_KNOT_RECOVERY_DECODE_PASS',len(d),len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':
 main(sys.argv[1] if len(sys.argv)>1 else 'C40_FIRST_KNOT_RECOVERY.b85.txt',sys.argv[2] if len(sys.argv)>2 else 'C40_FIRST_KNOT_RECOVERY')
~~~

Exact decoder size/hash:

~~~text
1172 bytes
SHA-256 2dd96105a0932f9d83c13880725d55b4e1d6758b6c914ca039bb75abe4b2c0f4
~~~

Save the following **single uninterrupted line plus one trailing newline** as `C40_FIRST_KNOT_RECOVERY.b85.txt`:

~~~text
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;ycMbs$Bp*h=fEElo?gSaoh~W;Fsn*4hwQp5dz6mz!)fIszG%}UMqqZ;3i)ZkjcbBdKv?*$W1A)+mP_6ZyJq3kX(5OF5ATW2~sAycN>#67Zn{C3iCbh?KN@kE6$p>oMZT>J8q_zIV4SULe`-~Z$6y1U(4~h^GuxQ_HWvrnTtYv+1C=^9F)SLxPEWIzHuN`G%PA?v9}BXHjKOmnbl~Dd#<1Fj@cIQD_5J*splrN0s!`>jY^7+7}HirH>SGJUu5EZ9pZUM#BQ$+&*i0;f0Y4}W!`E<(8&w9{voDk`-K~e*S|YRFan0yFwWxKW@AH(D4vEnB(jjXvj?86HM9lO@oEG~{?ymzfajT?v<Xj)dgr}^yD9Zpr@oViSa!b2H+rFCVZri2HsLsJAQ;B2%x)PCextD7k>Q@<7~P^~B+Mw#G?*@q-e$Nd!}L3#IRi``0}%fIo~&qA1cTu_0mo%x2$pXP_A&4~k=Be4F0UBAH3&&jGE|1Fbn5^_IU80%+N$K1f()$-7{WYhA&B#PRhU&uV2oKMe3#Kt+<}r~BjIW#49mOgI#|vVOi;z#=j;CD={-LkrtCW(2yG9!2Kg)#Ktu`p%7t9rgBZxCZ8tdv7QtuI+5z**>C-rhB)*Y}eGEv@bqo1)i-v)gvhy=~9)&%h(R5;a2Ba{hYN|fBH5};h>BIVBrU%2mcd*<`iI4`y)4(aHECJ6x2=>fp;|5($^A#WjP#TVVxeb)oR!UZD=e1l;(_rynzk^E*DJAADT{_rrg)4hsL?6hw0B}Sy?~Sl6HR*#fo?4CXXijNk7FUS;$Y~xVsaN{7Eddt)pV)rC@<Z|~xybDvl+gX$M}Cs5Psr!+q)*Fd+aX3h2VnQ<V?N3#1|bjRqnjUgl1{{B<f;kfdW^o&q^elAITe?&g|N;1dc%z>ghkr^-y!uR8xWL|Q0GS@UkHepSp|{9Dwdm8_uGBvwsFi-Rk0K-iCLLpeGy~Dyd&=e_}nsZuidu)nzu<sRLcEfs`2tiops&7HEb}qOHV#Exc57}xby|`r+OFQnOp;2c6O|JUyXI``H0N%t_X2ZhP(kT1r`p=`x@1Oa1qvVQi{}V-5xVq=WG%E;4Xf^<1emf4LJ^xd4S_nGL#X?e3c1IR$|8?pT?9IJC1@dEI1HdeOp?+k=0P|8C+V>6tBS?y>2FCX;DS|+UzN8B^6_whH>DQ26?4TqyWbd=BZ>!Tb=d5pSNqj8%#Jj#lsG>rDskQYP@kzEII2R!>`w!V?>qjc!NHqVtGo5vD3jL;%QUZ3HO@Lqbt5CvrTeZ<XEOH@bW8<Z~}tQFDXFRkx@fxfmkkZ$sO&WAj(>b-nIutF?!Y+yVabh=cKG7ss|F(&6Du`XX0oNQprkHNQDy$E{OZ3P+SDShm1T*a@8vWoAlWIqcKe({i_LFUl8EIAPvfDK%%>lKNx<hGkg)%=LgWK!X}KQzskK>TZxcp9g<+F%IiPfKr97hQ&fu2ugT#Tr|>XvZ1T?{NC%-fgRnQI!=FA@#~67JT4LfTe0}{yz@V86PvHenyazf6=1v`@q;}*8aE>ory%Tcr0swbe(S?ACv`Ibw+aj<LB|N}lWv5q0hU#ETDb4IZJ`vpk6;(M-dd@sHfuv%q<8yTKN^$hSiSA3!>G)JcUC+f`Pd2^LkEFO<&0S$;4SvReVpM@bDi?Etjps+ZwYM(r8fk=@DOSVJ5J{!2mzZ!7^wP#gE5Sc}ZqXTEedhz|)7$^(HiU(*HJ`UJWWCDFz{$p0A1Pq(<lM*gr3~^972_0zy>M?Hg?q7OEGA^8gu$C1kWwpX#?@4ohBGN&o(Fi<>qKJQ%tQWuPjI3gM*xmF;39y@K;iv94U{KDv^qypSF8_*FTY25?d^ti&#G0e3Ci`igRR=^j*yw@EU>9~-H_YQwc}N?tE0s%DPKKL^14KO7w>IH@fj5I)JVJ{V(?D7i6}Q+&La~cL=CG_L4b>698Gu8XRjbGy3fiFnk4MW{xxt~4c8K9{<UWZv+A)kX^@72Jh-1P^Y9D8u?|W(+8He2m^UabScA8(QHD36+qFzL2dRBismEy2mNygzv~i9mKy-AB1|!1b+7FbS*0*Ajn&n+NsHV?>e4<df2)USsS4tahrT|sF*wWr=gg(FO7cjY+3+<(nN}8as8MxT917+UMUhAps<_}T`_O@>~w4iKR@oUCRv)+K*j)_^{OsEoA9mPcZ;*cQN_GPLJ5u}bqkf}&pcjJ->inO{ew9mNE38Wa!2M6fgAFk0{kYsaB-hi@6gfJXw!JXi+xJ@bqyA5#1ZN8cGpW;=449#3s8Gn(o*{><Nzot{MkNdONo_S<v$f4R-EX&jO0(-p>ag#+T7`H;x6w`f3L=<qne;pb$yEt=>8>FW1(ttX;0ReV_?jzG=Jl)gv2TXd0PrUuS9o9S*rpaL88g>b*Oi%dQWc(os=kF)JhJ!VW%OLr5HZOtuRE=w=*&Wu-E>(b*_SPMiA|hJY6EVcc4Hc!HyuUZ`S062+tN=ivvbv&rnJ9eN=o#`_!{5{MSzNU|yfp@gg?`X4&g4dLmoIEutSFE#iSVE1o9`B+{8vr*RkWvy+BwvF{|VW)-v61h{^O@uNPbiyBRdN1r>fC$kn*>R8^oC9?E>oy1W`5M-AmcorD$`%>|5BoT%<j)UGv=lq^*D_HAof~sRh~V#P=Tod_w;-sFMd_dO%p$9<5nN!?YQV7SPW|0SRv%wEWHxe_+Clu#=E8tp_EmIfx~#`AepFvFjMzIuVpsM6OEjSeyaEE+hd~wuVY683AE6&l<iEeMf92??PhAs}@$vBRn|xWE1+1&qHM*m+-hWuJ&k`)qne&j9fxqOa46R6T8NOEQ*>16Mr(6(jiSauFE)2I}w8t0H)MChsaZ|DC*1r(a^#fB9l$;+>De%rBko2XBTT75q=Bm9TmU~eVg^93@w$i!MnX0*lsvc5Edxu-N+XyhQFcfR0eL4uacfB?EEC%IdeKR*d80W|MV&(JMdPrLePn2sg>;(+U%U5*1Ny_0BgU~RVorE(l->EFm2XI0Jw4E{T#&&f$A>aRiY+{Gxo)IE<+lkA@fv%`sO%c9Dw85F^N>=Hb!pszEJqCJ>lr*77>Y+m#zKfZQ*l>M?*kB=G0sS+(if@EO{Vpmj;|SyW;LTQxf{vwjr<rg`uR_o3idn{`Alpgdv*E(qEx$@0s5aC%qDZ7?th}7}{$YN|*8dfy)2}7r}v|{@0^U{T3QpQT)qx)jDwyOra2aQ`lN?MMd@Z)Sy);2bWoHmvmI4?>`G*)s2v!HADiHcCPR#-2Op0L1Se6Qt#DY*85@1b+L>pfa9r`aA^;(LY|>v4Khl+&L@QtF?H6ynxl$yfUt=~8xso!B5Cotm@Yr1J3WV4*th<j@@2j5l<CapC$@J*n2MDVQj}}qm@R^Z2dZM0>!eJgInsXVINYW~`ji*;qB!+LrM>>x#2*wc_DnA%Ls=-YQewdIDMHf0NQSzQsIZaW8Ft0S7CT9x3zYTmqA1`I=>{J^k8jgJi4zw;UL-o6yOX>+^LPQ!e6P;e#U0bng$JJ7?U|W;xC=JYq|ov6geGg9C0n>~L{;f->rBAb#+SFDLU!Ss*bK=HX{Z6)Ao8>%uAF(tTf0a*erJ}H+`BV=pYng|(amrJXu*Iz*On#5Rcm;L0JGNiD^wpk_z<-Bn-xEH)-GQX0-2q((m;6tTZ^F#XwFIgmG2Z1>rqgf?gSVWWNk>or6a}^+8TuzbMxyI&5PwGyI(6qbUE(z-CC$Opt{7b^Xu{aGrv^hugJICLLn4b$7F+afg{;FJN9yIMn#3Ue&9{fd{y$lqlX*-#7WpBt9?mk9E}?N*V>RNQd+4y&nQY46;0>8GnnVhnCGyQ7L`uj-Y)$X^lwP$$O8w!+ri$J2_3eO?}}y{EkEEwQjt@&`R+wgMw80RhyCDYq6A%bq)t1QWT7zKS(r~9Ce+;(;+5FqtTXHLk^xQ|&4ALej`wbv7MKcGeJi9Rl2JFV54DT`Usy?PM~0_X=UGi)(VYIBamvs6!zXj?3KyjrqCA_1e@S&A7+1M{BnEWA^Lq`ykSYZ0(O57c&S+XP3tf>-cO8#TI=Ddav!_Y4GU>S8(b^QlT>aX@EhwP~%%O*R9OF;`+(U9w?{LR1fl{X#RYRNM1Jrq2xwq*$U#u#a1|mzMt%D668k((=eUWPFQDNxFpNRqHfuv3VBFBw>{L}Vtq(F`r!Yo;Y*>&v$03VXhg5x{%+s@<4udYE`mnrT760rF#ma|2s7_Lpl-u<wxuUlc#d#z6`$sg)9Yrv*16Y85|y$5490yh<m_%m~|G%1_g@*IOr3rUd_$`$i2vJi~3q~s^6LMwwGGX8qUTFAAv8!lBZBqL<}GyKSJn!lJ&#d3o1CTHleX2{C#Rwgp~i*j@;A(jAHK}PT>sv7|^!U2wO#9L;K<N-H-yG7~3VC5Qj%Z8TBgcd&aBI~6_Ua7}VosY)jq2*8>ggwC^0ZPP|>J{}~y~>zo%ad88IW)8$J0aeAed=zxA)C-}RrH!vW$Fc6<7Gojmy=a|ElZWC@o4e5#vaC`6~Uc<Sz&j--Im5tJ0hr7W)5_SV=u#Q-vy@-z*6s+83m(nnCz(!B;+Y$>I|I4)fn84hORvG2)jtkh&16Y#LPKZ5Z0gFR+Ei{{|`r)6b2cHZUh3a8Faj7+CREpRH(hsJ4-1m<EOW6@UGmfe=*#2j?D{BCSAO1kM7}0pT0tuGSFsc|Meg7mG)Zz=6bVH?_R`^&CVh3<E2ueWR;&-R^SXR1n?X)wm|w`pVR8GPXd;5Po_Gnt*BJ#$rPGce<(^;NFMkRG2^jadl;8qa|D)O9EUf=T^2Oy)O>OtGi3-3l^7Eb8woHdY*iW)kxm9lAn3NW2_V0I{_}i#wiH9wT=;r#su@)G2^EPX0uo;vtPWLr6@T)4KK;Q5hH5Y2H*SSQ!L&J}p?#nH%>LB7q350MoSoi5la6HSVlnD+2%mq|tP59kL=xS(jdS@_CTz43DyuDN&x|_oT!&YH!MCd~P{nL8t5xi@rp*xu7pB9BqJIJtmv#8ilQD^hN+qfn!&X;<dRZzRAd7QC#eev^9sp#)?AsNNcQ4hb<Z-1n+a;>UEf~4{(TsdGmPi+!GeAeeCsO0|#&Wp3m*w6t_|#BCd58mbEkF2R#{IXIijFwI3^%h1y>Na1`|20n?#kG^d#IO}T@B?Waq2feqDAZPg}4!1mgObZ8$!3;f8rU5CMnS*;4z2g&wS>@%XK{o`Q+Xad@I;Pk$w#`0&s*oSkLsAHE@RJbU*C-%10QugO=esnXH>N`nz%gY8l)wHHwu=S@Tn1*qL?x6Ns7ZJ+SJRG!VAQ{W^^!8|A=~#A(q7VvgT^B?gbc_$Zbg7}3JrBSW2t3Ww$m{z{P#vr6eAGXRK19oTUxpbG@8pa|8n)TQrDgwcu0ieW3#%+!1wQzWO<*$y-afiyHvUn@98N{~CZCfjVqDNN@ts0aCQ+e789md(fMQfVN!I%E@u+r_0O!lvtgM~p;B*4^y;$jjjq`nxqZ&r>7!IaDNB37KDq2CUv_h?S9nkDT=*+)_U8I8bMq5^H6z(h~eW+R1H|O<vS(wuMrgXRA>J@OohDWPiyyb#^%%Z0{@k7^RSdB0s~i0y#n3yCFw8j#};}4OQDrU(ASSg2n2~m8g$b6a3n2+$<|X{ICBp>3NkOjxg+qP&jmP@dBAz7bQD=HVU<yXDVVbG(&TZ%u<OZI}!^yh1oa<Xj}6*AV35eV3IZI7>)%1c>QQOZ02p*oG>jmtQ8BSA#y{~f2@O_ao4r6He3kZkUNU_YgC8cF3y4&otgJoR8-atXqc$dla~l1gc5TPR3(5@u+Z8C-0{+2hf}7tjy3Sd4IxF?TOK>l?cS`SIrDYgk8E*bilV+B%!ZPB59idkREXS6!QnprX%<1na<D4kiN0B7V<6qc&j6y~eaMT3G2#k)UNc4cG7Cl;hYXBmoomxsrGCauK;Hp;hOD$kzb)a3q56QuZTyj&E?+7kAJSSr;M!jh1R_QRCY`t}45!#I0ch!?6TO*MGa3vz3DH;$%;GK3X3sNKb!s(zXQ)RfG(~2WEG^z)_x*l~E0SFC2V|<>?V;nzN{(BfWG)tdCoXHx*OPb!sh4+A$Csb~I#EJSA*`)Ci|~WRMpA%&D$&#q-teOceH6|}@#~LIX(A_1WmNXBN7kkf&{lUDiYXBPf3LRSagY5j`{n7Phe-K0SqcUbw6Sql;mby>YrCn#F^>iv#~cU->Jlfj-iz}{C8va+>bx(uXX3BZpO#tF&{TX_eW6yz3Kf@R*8X^na1A$GpCFGoobm~TWD+`6A~O${!0RipcOv1O^8r;Bf8!+HW}&cYeb?wUz{eZ%R;?G#Muqd*P;n<W|LT4kA*ET?6&{Kk@IyD!)=66B7BD9@6{C&(Tvvbu<*g9V>mM+|7Gc}r2e3%{bfdZ(=CMeRJ!sVn1BW!~)>s1UC#%0ALU#i)bG|~8?5obi0V^RQnL0?cKkxU>xXpVonU+an!g}q%tJu#s(~7-vExD&olpa3$=<@gaA1$kkNViFC8!&sBW=`yIt}$pPY#YU7$H7t-X@LXb^G^K2cRBqlqPqAGDL#Z>S8P`&8T!I0<w~XNAo!c<%%w7G9NDL=>&E{Cb{{)%1<~4Y-vskFKMJFd3#eTZ*HUYt%0dj|+bH1Sl)C)a_R(sfTivl$**U3br&<Tkp|6qGv!X(YU;43QW`sux=4fos(MnF(kfb&c?45)py^Q4X=}d~Z8K1fuk?Zl2t3K;Jq@(J4j4Rb#sVmCD>{@q_W3;oQHL|-(BtBr+ec(0?_Oi0l@LgwYPq@%}-q10PRTJeztkxD_xQgk-X+~U-j~b6AgY>22$o=impm3+IYd=UJ%-G+!`QVfj>H<1FKy!Ss84QQxEJ$-M+ikp6iGw`Jq_qH8V^A22waJ@pdKkk1bSST3!qwI++V5O{>I5mJx91d5fkcF;A9agFlDeh2!_C<ktIEDXcL4dSpHFG#16XrUm{m@a<z43A4Ca6InVKZG9rmn$4kM6e`kf6?>nGM~1t-QZMBL#(;@8p7_`$e3Tku(+dM3ma<qsy(73z*d&v0?+4fb23eJ8<D$=(}B29%Iwm@)jNY5K_lKkTR#LlYk7vuWT=wpe9|E{~MXcntbX=`&p8ig=xiM}6|DRc-rE81JJ?35JmwRS8A=g9ThSxWKRK&ZhupcvOYP#t}st+Y8!|9dbk$wM*N1c2^dVo7GRpUS}t_RKyKFG8v@T$o609aOa4X!j@UKhyw8J!mwy`SV~~TA$ywCwA-DBi|y5&`v|nB__IkFDBZNf=6h_$6PdL^ju;SkIH3->e_9wwMbdTi(QG=8Z+L9}<=*7nN$LzNQ}pd*wiK*p&meVFFpPt8D+BDDNwMOXhpm$HQ=}B}Qjhj@kW0wU=@we)u{*aAWUy!uA?~9bt`g<~I@sV>ldjf*(!fv3_dq^d!opw-$S46M3_DZaSrC4H?xE^Jkf*v3f1DEQIKKT3WG8>SF3rRLYJZ4R;K{}9cTDyWSaBJ5Qo8uxE7Wu0Uct+A03{2C5KRultT@Ki?(Qa$A(tIDY#9|@?ZlGwmE}d8@IIZRq86Cy`&ifhh#+i?f{!r+(`MH0M&v+{b3H{rVh~B?DKmqP+~!7D8f$@qWZYoYYJtlXC}pM=oDdAK#P=x+ORz<)Y3*H9nQG-1{^W)LQ0JEox#98>1mazuO=hH1;o{2u<RB=p*A-z6sdAcKLZXM1z<___Is6Jc^1i#W!v$)CwaVIG#}s8>a%;cZ#w(D6>_lO)*$!_?_CubM@tmYg5{sI}&ueB<fHC;3L1pla?KK6tdMdCCV~_V)gYZjGC(rJh%?z&b45mbE2X8L_VoPD>%Q~FaXq~N00PbO`$-awq7zrm5nLEU#qlxdz?aV5?!VAPZpLkx=jIlRwrZ2wGF{(vwI=V-cc#-5snME@w!q!ljk}XcUn6X2O^X^|!-%7TaJ|Cz$>s=r#3?-;#uATcn)xC8sjMm3am$9(eipo&Cj`Rz`yU!bjL&NVCe9beg=CK&Hp*Dh<icS()Q8G!iwPpo2ew-A23po8*?CRr<Z;@MlUijsC)S>Nbs(oam_w*wWSjQ96zrG^*S<hD<NlAC(5Klc$hCqzR4M0`p$v<hGxR|-XH{9lG_=Vc$ZL;=c;ejr6iEDv1=W_Mz32u$S-y*M+UMEs2J7drGG|dR;%4M%cgMURI%Uvfr1kh?&+JbaL)l4e^@1k@>ww*7@A{>aD2+;?{1UWVdZC_7fm>f8+u3xV%99p)@>JNlgoztnI^Sp0{;A*wVE574ff4=c@U?u*k3LnYj|DtF8O)Iro3Iow8M8yKe)NJhv5to;h8PMiPO=a%HV8)B@)W+F3ME4?usY;G|iIa^4sNZ`0{<6gmlz7f@$>YP?W<j7IhHn$}eCdqgXjxnCB3j0%i?+$sito-g*}Pm#p05Ac*lcgycCrMVrTAF-3@+gTA{u9ce?v~n)pGfLAr#YNb|%YYmFmrkbj1&Cjb-QfcOq5O%$K|UPB?-uVjImC$aua`<?vs!Nx-D#ogsOdM|}gTCi+%IjvnxWpw)X)mTb7F$tS!ma2MW}-(thU7?qk1b3q}_<TwJgUj-hTYxlojX`!`TickRQ&I@Hx$c~+~JF4`3hm&Qokm4?HGvpfoNWJ_<NA0yWkl|Gehy8TNl8aVSS>PLz1p3IX@sJqX15$2n?K<vH6%ljgGRVwG;eE=>_2`=YJfL==@Rzm<K)DgR#jF>}Pu5)Qe967)4KnOPUsbT=1Mzk0-nkGIE5rc^<K2~P<gB=N7i@6t4^5xNgzTQ{1NVQVkTjp4tp9cyKTmmD$KsJR$=i_ZRtWSx!0d+QV-zC=H1TpMt$qce`e)g(en@r${Zz9=C6GOE8&mfdx|NKhcgwjG`-^UwjohPe>M-f$hejQ-TD{bMo&B5K(3~!!19dLY?K>O4_gZj28=F8CyCMmI*>1l2hslShl%D`$fogD~Y4bvvt4uWTc)<}QD&SQ#gjIyIE)R!%@-<Jbl?ahktf1OD-j&WOS%_cQUf$X@K6Vu-o&+bXTGq)$20&yB{-3s{rH%nWOO{!C9s=+~<r{MvH}dd>>72SAHCI2bh5|!1&1}e#gXJS&1=*Y8#^jw};o^wZ$w`B5h$)Moe`gE$ih5(^(a~&K_=cKq@Pw^5pW>HlKWz&KieVprv3F;rPn+ggcamPy{Lt@6W8Go>mHqix6toG;{n~N_l}GIfUv%%J>k=GZCCk2Q4d_a#>L-g$UKCS(ydfEj_9}tIoMiB>9a<N$b{OBEGd9uIrYBedSc~hIC&IFZU&`kEUHJ3i+z9e;Hl<=)!0`8G(3LVWj>99J-fDo&ZjRY+5N@s8?&E+1zkcE0_GlO0rv^ZNw;5Go=JEPR4prDORUtmAchP?(cpV>d%s-}o_<ak>T$3msE;%fT{&t}w2ZR6#{>JO@2#+`ej*jVCseL?$QmO1tL<5nevk-PElNS1~=}=?Y>Jx9zD)qCGVNR+cnjgb4{!dLgh3p;8Z$0R+Yqp?Ta%$ADF24C-`Lj6?JQ>7m&|W_SfjRA%C2tt-qt{j8@#FXClZf}E5Madn);ZoW9`pO6lRx_nQV^GXQtn}YE`x@)XYxTxdXb0wQ{^FS6Xu%-e!d=Q!pK|jx2o)aS5ZI-S=IrvSUgoE1KBe5WaLBn)@1t)Di()oMf|s7k4eKWc65;*7X!doxnXY3B|g8^k3NP)d1XpsT_{n>%;dx05NE2&C#?fRwNTB;geS3ul|GkIq3iI0W=<6<UI>1x^Vio-`X4dGwbY%yRA1X4ShNeG4V=^9H_D?|CRig_A?TX`C72n^<mOec`<1APF`$+Oo0J=e3}uQ=vW>zTWOgih&V~<Xd$jl>F%O=xWqbbmsd8t;fbcdYT<+>v?CKaK3U;+M!k*scD*QrXPw%pvlp9Z(H+^{+)fL9&g}%SrBcjX}k->T>GQ2VdV0+{+Qc{tM`?Kht$Aa$0FSSuxBe;|&<?{M13cSlP80*a2k(HJSr(ut-4^cu<57_Fg)e30N^$g5SvuxzR8({AOa#LN;lgAgbCT=oQg<wG-g(68}%_MZl8@^dHbu=769HKkOJS5~9N~Cm$?mWs40yq40kx0>6>|+9Ys`c^?S8dGBkuP#q!)Nkaw4(z~Em#nXerd)>`eDp&TEm{wuX%xw+B4x}y$ziRU!Q7ioIf*DRUxfHq63i6jN2e61}K<$C!wvj|HZ|p_&1nyC{>wFe~czJR|P)tefitUZ?m_2+;cDjgmANVt&KIgorAB5&f`3eh%7LOATJOWFUpFA4ujX}tY4eq|2V-yz0MP)ReestVeNPRJkm>#B_h3u!_FDZJF#<;&ZjkMLT%)_S%I3-jxaPU`YxOaHphH2)VRM9N>d)$T^N`bu)pIRtYJv_zvMoE2NWl>9K1t=)f-==oMo6$4D~Ph&7RRvjQR)6Y*Fb^ku|<Uc&*l|?qt|DJKmy4uvo`XGw7+rKo@$4TUqWuEJ^R>eZ@caG<nqtKO?^fP$ln>kns`sMuje$BDZ`*{_;dpZmxI6{c;n*ynY16QB}Kjlt&$)5^iqyUCxprtt$JEulIW6j&}y3&*qN9ZTof?BY#bQW3(Qqt7Uir{Ce0I{dHHoZ{&S*wYIzK_CrghqvJuCMOPVIXb(;ZwI0c6&vmewYwr42X{Uy+27^$m+dM^28gy_f*~8vJ!Q77u!sH|6MjaCqc;{nPKZ05PZKp`}t`MYc$LO2xs9FZc{@V70G=2(n)z_A}&iqOT-?J|bRsP0Mjk5ah)aOlDk8OTP*DO!W;=<#j%w4TKxm^8wq5$2ox`Zv+s>v8B;x#e7hc=?$wp=qDtYtO0{{-R&3Q&S5zT96PTjDUkADu1JiHnf;f;dKPbIsnzcfh}tXq*~|Q1%s10A3SY5Zmj}4kL?QXKN#6`@0I|(+LAvI*q3EN*G+!Z2GfL{JXgXb5yVV6Ovd~8#fCqZZ&{6&pSX`=Yp6YjeNl3D)j&?37fE4ba?xvfJ1kz0OC^L&pTQPE1HK_#><VRp+Ra>h4HGr@*dx?@o}Ss?;VhwDPL0o;Uwp8zw8JDTe+deGStj_j}LBr8>Ai6QeTYhHium?*sm2q0;=1A;j~4Cl%QBWi~~oVUCL#Amnro9goq6UA?7N)02m%D`M;N;6o2Wl^Gw)}3Rr2}+C~?6r_z%bX^@J*24lUQpY|HjR%w1-UeZ8c3J)yxie;!|C*`PWRwxYL7(;kC%D;KYJSQH1KcU2$V4NV<=;G*^2LO4f4h!po3e^iet*wseXM|PI_hHwpJjUcqJ%um2CY7xQ&u%?=4;p5+GNJ9DKhvXCGRdgqPW3rBfLaid$JJ0JTCiHuMBa$fyRqK<dK95)Fq3P`vdZ!A_mjjGTS81S&iC<z>ibvU8YV5&v#hg}js^b5vek83se~|ANsPWpKfj1-DRiuN+g9!u3p1$G()Ff+Mblac14`#AnRD*>Eu1y0)KiW=)_QsmH~_5)C=>{Dqj|w-H|U1dvUH<ba_*dPa6j!;N=vMRbhTQXL-b6~5aK}8ACZHD`w3xjv&|)08_rv56g$%%k-icduCt|gN0a6{G9_}#z_0{>i>vBKxI~EHb7N{qqi#VyuXxucBZ8>AQy?ZRI#B1M0g_*mU+*oj3sd6J$&ieK<L1lo-uDo9L}g5Y3_jn*q1!ScDpEqscLC`o5o?os-yo3|V5QE<;6T|p<h|a_m$IcgqHD&b=<-O|Y!(KiEGJ6f(0TbJ9!*r}<j@p}<%j$I8Ot7DikI-VGm~@Ph1T>~l#V~m(kbk8MMCqp4$X7p*w~5k;4Y|~JN4ylkkw^rxS%oViyJ%}v%SMXU?r8TqU8x8-l`^{Zax~3Uc3@Tg0&&t`MQMy3}40pYAH%@>-`IMgT%S(rq*AlXB>WxY9JCY6ZzC+vqv4H8Bs09|3DJv?5uYO42Rk0;DPYBw6$U#FPGZg1$6unC|D`Qsol;CFs*msyeqqaWTrlrCP-*RQr^>=oUH+D+P+>qPJ2{AL}*Sc4?U-+4XopVxoesrIGXdM_t*b#24GR2$8s=9LvkaXBEMWpuuEF2=dy*zpxA}f#|XHHR2&0mQ@=t#?=?Y`krA@7v|$f-UJttXk^%FR_CMDaq7gCXY2ultt_RL6V$4qUDHch^t!j;zO+(@>w~lcqlN1-b*qDh4kZ$#Hr5JGWYh^Qq+X&Z}Be(u#HzJrK>~Bcp9&rw>U6loIz*f=`+&y@<7|s)TpBo!*$SQBx_3b?65msK7KO19vkR>J}IxT^W4KUq9R{DhnOmY&jP|2gp(23HbrU`{r<>`&-1O9xfDU%4L=kD6G7k^lF^C0pHsqmHABMvq;;sC%quTxu{WNYjcRUjZ=<br5Xyrzol{10tgZ;Y!}G4A}-bt|qwddhd7`bB%=KFrkjEefLo;6CrJs_rz-w!4B}oA~<s_CkZbpqDV2Flc)?tKR^@g{7P#NRYuSKOOcgpyqQ0&tS3m(Nx3iO;)yFTxgv)RW_hx793kqW1a76`$Ize0i5ycnUMbdT$@Eb#sVwaW@>sK+${^DkI&Q0(TK&N$hjJq6|FPYkVSyw%wk4xI&<1T>1sz%bH*vdY*4BQKXeIvxmUa_2%zk7wJ7+sNz0pJo;+b@hV1e06c((HEKL*`+xP8~6_#i<5S={vmTA*<37yqV-@_wrpZL`llQZvp+HNUFSwL09IEObzWOK!A>gwQ9($ziVh;<HtmQ7JBLjqxO<3MDF^Y@K$6KJwTn`ja(oIf94AHJ-g``Qs<*~i=U5xJZ=2dP3jb^pxoDce}>G5AWRTb3;b^99NBbm9ez_~K?ZqO(cf0kzKD9AYm)(i9G-P{XD_1<*rwBkXJNJA1^LrhXRCqyt3pyd-vHJJbf<#?Fp9mvVwWModz?(iMNuEmzOPa4t#VfIERJVbG&%{c5E8GkR#Il7?me!^L&5tgwHd5DaIh1NO`9Cj;2Hm(LK0_B@$TvW=LE)z3(FQoI_T+MZDu#QMeyYwT|u%e?$Q<&{>=NM5XO$3EAjb*2PdQOCXQK>Z(flx5jVab_3c*%2b!m*TC~f8D$BIcdR&Y=BT~*%FwWux5=ZwSG{|=c;{`X#!snK$WB1aO~FQADZDsYkf}H6z&HOd(diE9F`kQ@gh?LAA%oWof5QFST1L?d%#>dzZ@b$K|ox0^hi=8?AnVinMaDe%q4|fHv3vsy9g?mA6CId)h(__VqV#TKEI54awJrbc)d`@ZRr{i?3U4~*QUT<)l@UQz=aLd0G5Y_IIP8XrDIryn_6?QCi7#_zN-&EYprARoamz%wrd@5p+ZjhMpyTXXiyQQg<;0St09UN*&vWGLM}fvZV~_nj?I@v%mzQ}F>WXK<Og#55V<Favlm=F{KiADDLCS>qr*Swj)1%*(*R(Fce=S63z2V`a^azg$LW!Q=X^BGWxaJ!Y!9fuU}U{;%$D@4UG(dYI|G&*cb^ho>_M#ngwpAUxm$FW>o1B1nf(l~s|z~NX9I;(6{#DCMTBjrHAc~o&?F7Wn+K(9<s(B_b@Tq`8nEOzRNFBGL#1o@+5bXyjN3HeXz(n&<u^vT(8mg&_mGTxkkvlnp!`I5=RJ9b-j6~2O!#YwrQSXT-f9APZSCdU*Jd)=@2{A#_sz^wMAxMQ%C3kkhwgRWh;`>h!f?j@b20Pks(-%4o?~ZBSIwfG|1G1n7v_r2p5yWHh0+H1Qgkw12rUn6JQ;>k%{l6O(+Ux!9~t^Bb$hceCHNC|)mYZDb3<uqxG*BF3tgxIh?O{YuuVJLHOT8u_w<>*wz4?n_5=8|xEL_1vS0UwWsde-*+)AvY+^G<F}c(>Ev_z;#}%xA@CC3;1$lAjW<rZ4kxUCo&S(D{lV(k*So17iTFTwG;fjJ5;tUe_IjaL$qmKdDSB8HK3!NnB{fqjU0ALFfof|jo>4Kcq2XTXS!F@cOaRBLwxp#wl7fcDFa~bXcfizsl-mJ<^78Xu;p-oVy{N3UAPdn8+%L|ySLlqeJV<_E)_E6)P#xg!+L}awICZ1#LWzWg1ld{5=yd1DpsE3cnAh3Ui`RjAcC(0g7{k>y>{943VSmS?6&o=07x6&<XJ5%^H{1Ps`c57d@YgY|DNn_g<DK+y-lGdH_QH||D-;?`0n2;LJVXr%@g>)FoXf3K+5|4^J{h_<hSCr%(U%;U^jJ}$Su^i1R#_9W;xSkFdn~8OgE61`Ybdn~1TYlfpc{QOV?2+2V9IT8awau?GcejbIEAQY2@a3r;7b%GQ^3jF0Z-nb@nLM!@ygA@gYKVSS?fz#!%?Ja|OffHHV+Y`_R-ySe>0n&Dz9wrciO(yxviu!%qLyhEJ0!nO9)heiLh7n8xGf{RP}^V-I2wwukeAa%A|pCy7o}Ww13RUlBDLbB)U{#|(WukeV|#7GjT{JlRk)0?taIifyE*oT;QwZq(!+UUdrb0+L@$nZGXsw~@f8)r(@d3cu|{9ljC%d_bnWTWw2=<74GLI0Blji3Y+uWAL$OkN`L>N!MAP+VSHwkZaL^vf-l>~SOks1Gw@!?JOq9eCy0SgpZf+dXhOmLdk1-H8b6Pd4zuw5~aXx8V;){M|RdIL~-JCf6L2*OO9BT_NVW{c+M}3|>|K4ad4E=p>9#6}7`60Z&sD@HA)y5+$P%KO0{Rt=70mB_qvOr6P!UJM%_DqnVr#Z(YJ~!dw{b|8I##9f!vRD25PvGw;2Vo!^2VBKiGjtzR$Zh#QcdjBF2mkLRANdCBBr?v>i3#Uo@LZ(NrIu~gES;i@$$L_ee02Sz<G7m1gQoy>jo%NwxT8Ufo-iDH+(0SeOGPVg<H+wHNsfiabT<(uk4Gjj=mACCrfRe93u6$GBXQk;m||H7sWYOn0hk*r%Dx+*ocFgH-A2WraX6J`S9nCktufsgP~xeUG4BpjBXw{xYqRBkxGp8&J4RNDH<c4)9q1*QyIk7p>e>|=tbO8%Iv65%oAu1kR_xomUX!bN@OL%a|6tU{pWh<MVU;MN%qTJL3<z(mF?1P*k;XNAONqwsFkKQyAFN_l`7IzL{VP*egNrh1-OJ#QF6*RV$0l>qE<o<uZ6#O&2>>SWoUk@VdWTuNo0j77>yER_d1aLxr3$d6&Cs*!QWA?pOJr$in5`j*hBkN9Ls9Xviyh{=vlv8f<Tt=U69eVmI)$UCAC(&kVA5z$2QPx|S@_jnryk~t@W{O-bnmQw_AUe<<Oge(Q3@6Zpz)camMzWxnbah{2+R}WswCxnH!MWEvs5RbPD~K($@g@X^kAcKCM0<E#_SI}e~Hz|Uhf917G`3?HGQK<utVeffZEtP(Ca)&&`f)$uO)QjxsI(RDD3U%$L@n&{gI3wSO5-soZ|5lqpA=XRI>lfqhXrd*ecv2<w;%tU4dS&f8hi%ZahaN3j^mKRN?~-N`ZFT0jo!x!ab2j;DPCN_Ip^i&fTIpQ!VgCbDsZl+B7&nO2=EFM#bWCcxgS!DJKNn3aWe3*_t!QFdxJFtBmB|MxDF$#9gZvVYN}&{CWtWx`}FQ4>(+=u6Oo!ObL(jdHGD}T@QGZBoncL5G!Th1DsC?Q2j=A4$7+?Hp?#|WX?zxlh?=QPBQPo5aUXpL?uO=(*?WYX^OO2i>?oVyEbfMKaV=;;c^K5;5n|VGLbB5LUn-u4`^wro5rQCXL{)l7tC%6U0J`Kp8_jpwb4+s0_au$DAoTKWi!Jg))b3yfAOf3)&Nt^NCG5ahg|1Vnqk5Sf#{_L+Q71%=KACJA)?OW=I*=~noW`!jMXvc`h4%X*VP%ONqK-BD(Aiy3<nbY>e7D#GHh!yEn?lIZ9%c~bDUE9a}Idw4#v50#SShip-6!sAL!?PT2!pM`++qw@LGU8ChQk(uk6c)V1p+|Z@JQuH#pTW4nTrfiQ)zj!Va#~$&`I(77f&$dV@)l#qv%c|IA~W%vSjQ==?Kjm1hTemA9#Jk<$Rz7KMt1OD$z=@TvHB`{ZKyVND_hF)8^kP52E5&bw{bMYr%6H!!Bp{yK{D2otOGnx`|r7&D>pS`U%s=8<3B>E|~>WgRV^s0`hf(eh+GrFCM;wsZ^h?pn=s0%J8Cs?A+71#Mu$FUnNFe)`%|9=)iBPwZ8o6q`MB)wJP0ci?YlqD(nb@#IE_UE5JxUmR2WnGBc}uL_D6e((a6e}(lQ`j|nL1xX-S_|J(s8=(Kh)+Wj(42)*kZ}oxN=~9nUHY((mTUDc)D{R!PE#>%@r?-WVfJKIp34q*}Ry*$qi;Lu1q40=_G0xnVwFO4>7vGA-H$VODhzG3Zu&2c=$MEXX7j$GRe-5ynUps+a?$DN6yZnK)($FWC111!wF8c401M(W4w$$moN-()A8cB<#DbRQzzV)jQ1--=hPB-x289Dq^YiAykfAhK_$KkjXcoqcU0GGbjp;z35iwaO>lnS*`J4sYS#Own~jtv)Ek~STkHs#|I;?eE$_RaArQRBMBK0DvD4ICosh|EQBphoH?a<oJ!9^R?Z+(4p|9IWJ7xV^(wEBftg$MQ!o)%=uAV)_JuQKh<RK_(x;JBGf4a3pR2qUykz^qq3=>=}l{L~vJSp{;4qy6IFPM34NjmT_9QI~o91Nm4o@mw|Cam3|?E{s`W`kisBEF0N#{x9tUs&!1nFqoSD+Ig8OwOyK#H1q|TJ(s^3(#Iovi+gZ-Cc)bhKAU1?}(gy1_e&7JaC^N{!1<RyppLE`MW<vb^=w)5?&=}0xdlRK!=g5{w^9+ji8VHi3fG;U=Jwg?>zIDaFqVof^-nmD#E$)=&vmSGJLcq0=kq01ri{muTBiuf<<z^K_gCPt=!KoCwLgIQJ_ojyznxwc=PT>HVu+B+zWcn*PEtw9f0Q71%RCJz}#}5aJonwfMFQdrF1Pfrmlznlk0YW@ZKnKz-M1wJ~SvHgjwQnzFAl61woUSb=ag4R)%Gha8U#+BvgzxDA$2C~1D<ik`jE^FK$Um!$o$k5B?JrVa#U)(b-<HhlO$jA1f$$=GWM@+4+5-YF^#B&x?g2%)#iKPStNcJ7RsEe)z7dL8yY#i!q5$BB$@%;03ZAP1*%nS2e_&pP3&lK`nAeI$5siP;JYDOIY61~nKk56Krw^8-URIi|`rqv~BTR}2@;KptUg2#!{ng?G&kkWY+UxP=F2T_4NR;1;Z*`i-B70R2?2B|WgAj`eX@UfdF4Q*yyj|0p_96-71=<P<nufF-3V~H?W(`}yFb4^QeyL)j)vu||#_32rOQ<8vl7d0_-#)(cl8?0oYlw5TMr#RY>|8Qv1RNX9R8Gq|!^yHn>vP1|cWxa~S)+p1oz0)ILF(-7VJzLEp%}k~zy>mQys;uW!z(&Wv^WtAc2EuP7C=jnvK(M$F3GScaw28Wd($^N=LxE;Sh{6^)G?Hwn1`8nQL4PR)O~;oJHl=UE=nV%e{T2}5Hvw?*;9_+{rTY#S?EGCM(3m3TN?~xg8B1}z4D30ObJx#9jQAp+7vCzRZJt2_(MZ~5?#Cac%y#<c9sOX*x?*yqqM;=vM*stIJ%z<PURnH3@#;3xNjiJ&W=t6P~ij9jx+p<U~W9pB>lQZS#u6OkO?xGgp2b6K(Ntw9N`ykS$oByx2X;Y7dBtH6vP}w!<ig<PPdXGCbx-w33LP~{$6i<U(gj0A5g7mz%BAQp>nMZzE>ZbqSs00?Si<rQGU~-7XVsGZ!%fbqCWz~$Zi%*Hy9HupeT0f-ZyAWeUme!Jp(5tgB4VS$zT{mIaRJj5waSQLy!U#EAaCMh}aBrrg5Sf)7U~CFe&hohb0%lRl)W9*q^TKE6bPv9M^q@FKGdvfOQc)ogEn!{GOGVZO`i8V1nZ4<ytD;%;c+QRBQB+^xxH_KghH(0X-5^kARU=Swbsi``E<IS+~2cD_(>&a6(jx_e6_fQv#&39r6GzuD0@0MR?ff?os!{vJ;jhz1+C)mo;c|C_UF?^fQ6MZXhbbY_4tPOy~#2Yg1xoc`oVe-|^K+?dd8YUMR+tlKf<Wc;kCgbp69`V=}sxr)vBphvB_~-<g}rVQcjM#je91j~8R@OS3s|G9odHTB{n}j}F3Abz~Eo=nUa~ht<6sG6e${*&j`_|0;QT(KROJIwc_px*zXWSb4Eqiu+F{soJwiA?aX`7)Fp);Lho32N>xzii4i*!PJI_gF!3B$W87m<!3evMU0@kvl#v+i$q_wHZ0kcNh?pOCczJD<BLl{IUH~pt0aQ^^Hi<7;C&IkkbmHdhyzm@7@DoMOX!8#{~Et2A4R2fpa?)Fbq!@?Zm8&f6DJwxW1n`A{ke7JTP)lvrude_)dEA0Z@`?pR3W1UVxyKpf(O2d?YeuyCmiq$O{E~zVW0lyd+6NFW2PC(jQHF2m*!%5`d;gZe^c(;i3~y&ICu>G=G3~S=B)iD28yYX?3j=jy@U)_v96^N(+Km<d4rhmu+6m9w5OMH*4v=j)MvMGtQ~L-@Hiv6%P&fe1*#&gEowq~2V^gn`SnkW@Y66h{G|j|j&ZafN$YzZEv?(`UZj#STqbiSVrQy<@9~8Dsvh(HWcyI?KTa$1gOEe9zH94l-o#-`MbF<@={@*k{&Q{&kalmgrymoIhUtow^tll@$Ge=R&9o2#xya_li*mmo33>?218!)_ExV@NFg6Bc%7I$X<@paqE-?;`!urkNfI>gDETM=GU9pob+`#=CdW@@y?FFXehN|Lt60J$fUrm_t*|PX*X{hl8^!S_Qy$IQ8VMKf<9<9rdvT4b$2P)AQ>FKzF{ohANq!!a*e7r0z;(BVs5%BH?503P=OGE*-uE0`~L0dL~c_9X-&RI=1V49*zeX+ge)PgYN;?M9glt@P|CZ@<utIlmtQZ>aC)h%jl-Z>D?>=_f}2Y|zvU{d=9%A!CG>n|<{Uex$8-|g9}CCr5n-z%3;+;hW{*nT&F5X4j8K;X+3gEr)lQD+pr;1Wz%Hs<+>prsZd&TFLM9F^3Hnx}2B9ne1a0p3AVnHjrs_oH-*qG|))upC>>u%=V_44D1FY@cLQT;=+UnVLvFJP%dQ)Sejt_<w}IkU<DeJ?R77U|Gm7?3)doZC7kFAa2RBVa`ImT0np+#s&*H^e1s_gy$p!a0rZ0&ijpHO9<Yn^Fkc3cT|M<It$FHD?HFD2_)~eS&;X3O94tepxv^)ouXuWU3B_0yHE+fOYeM{L7BaVmC!T1kjoEMeBYv9O8!;!tv4nT#^Oy7L_{vDTzWE+=ACm5>n1hEL=b6z_q@T(6_I>QW%og~Z8aHPB275d{NG!rx>^Erv)+g<9XNtDFje?3yzBQj{z>`op^4Ih^AzYb-QonNf%)av7SW=VrMPtJdxmWfOA^1Mn4_|v%a%R$x#!F3khHntk+;!gF+=6t(~shFA`|HlT7Q&kDYKd`qhj3-%x;-XY7?ZFT?by0iFzWatRw|g<`V#XH1^rm+%M`W|1W4%?~<c<W96tKFg89_&nY4^CwBWG-@?awbHk*%jouqj*WH|F)MOBZ5VfbB^8yWjQM*)o*{rpP6zR1xqUcTGBCF5S%=yN$z<8ZBr<RoJGATn*VD-iih%-=T7EeF^!LK%ygW?3NPmPmaH*rpE9s6}H;@BRJqrnW~1ms9Gw^o4so)WgZ=ic)Y^Wl87vSQz!{Ie~@tXCoI!PPqPh}^IPv=#M7of1anL!j?leIKHx#?3#S<Qfn=;$Jj_{U5Ulhq_gpBgcE#SthZ_dyF<}$lP#n{v4k~BBJF|xV|lJQtEZJ#Fg$M3!J9)_@rKp8H#RCIS#RcQUmK3pWge&BZOkKJQar#=zc1@>+>T2WS=aE%}F(Mxa`5&{FINuM)7vN(<wz<=Oo(+`)0i*?QK>oT0Z_iy}>b{OP+yOg{?pNR&J|5XCI1acW8g}<3K%3y_xLUu3_-e>brje`i_vSi!p9Gs_y%O+eJgNb42MHdu6VS^bQQhZA<kaEm<eGa7Xd4#7_lER9zITo5LhG*?A_%l!J%(!550%;p}&*w>?(h>P9a4>BB&2Yb61m*4a4d*q8|!$Pi@8k)0<Rq@@Xp3q+-H9fMm!?TcAd*|*K71bP-{xU-@qHyI^L)o@_d59^BbLmQxe^H&f+GE+23dNLkM2p%rnGtel_1s%&XHleNvH725YUMD1`t0J5IfNlAEg6>f2kW~&|!#D_OrP}uZ000009LCRv?wW4f00G8(%J&EWl^I0qvBYQl0ssI200dcD
~~~

Recovery and exact replay:

~~~text
python -B -S RECOVER_C40_FIRST_KNOT_HANDOFF.py C40_FIRST_KNOT_RECOVERY.b85.txt C40_FIRST_KNOT_RECOVERY
python -B -S C40_FIRST_KNOT_RECOVERY/CHECK_C40_KNOT_BANK_COVERAGE.py C40_FIRST_KNOT_RECOVERY
for f in C40_FIRST_KNOT_RECOVERY/BANK_*.json; do
  python -B -S C40_FIRST_KNOT_RECOVERY/CHECK_C40_KNOT_BANK_SIGNS.py "$f"
done
~~~

Observed decoder marker:

~~~text
C40_FIRST_KNOT_RECOVERY_DECODE_PASS 16 146378 c8f3e51634303a9a0c7a6656337471df40a66414983b94a2c93814bb4fc3ab32
~~~

Observed coverage marker:

~~~text
C40_FIRST_KNOT_BANK_COVERAGE_EXACT_PASS 315000 5197 551 b05715f0647b2dff0760806cd2196b8a50d93ac1f0911d9a249a6f83885b0d47 [(251,0),(264,708),(347,71),(410,540),(553,60),(573,51),(615,66),(577,208),(588,138),(574,153),(562,36),(545,0),(531,0)]
~~~

Every per-bank sign replay terminates with

~~~text
C40_KNOT_BANK_SIGNS_EXACT_PASS 1
~~~

and its preceding exact line reports `fails 0` plus the positive volume/Sylvester Bernstein minima and degrees `[8,16,22]`.

Convenience copies from this execution are [payload](sandbox:/mnt/data/C40_FIRST_KNOT_RECOVERY.b85.txt) and [decoder](sandbox:/mnt/data/RECOVER_C40_FIRST_KNOT_HANDOFF.py). They are supplements only; the literal recovery data above are sufficient.

## Scope and continuation

This is **not** a global C40 obstruction. It closes exactly one complete raw fibre: second knot `81/100`, all eight COARSE100 curvature values fixed, first knot arbitrary in its full admissible interval, and arbitrary SPD affine metric.

The first-knot degree of freedom should therefore be retired for this curvature profile. The next useful C40 search should change a genuinely independent raw variable, preferably a coupled chart involving the **second knot and one or more curvature coordinates that control the shared packet interface around vertex1 / face0 / carriers0-1 and1-2**. A good entrance is to keep a rational first knot such as `3/4` or `1/2`, then vary the second knot jointly with `kappa[0][1]` or `kappa[1][0]`.

For each new rational raw checkpoint, first rerun the exact rooted-tree/blocker test. Loss of the present equal-weight blocker coverage is only a principled nomination signal, not a feasibility proof. If a rooted tree finally survives all exact blocker/dual checks, solve that strict linear-plus-SPD cell, rationalize an interior Gram matrix, and immediately run the complete actual-centroid maximal-face / vertex / mixed-edge / same-centre-polar audit. No metric-only rescan of the now-closed first-knot fibre is justified.

No C<500 strict110/weak000 body is promoted by this handoff.
