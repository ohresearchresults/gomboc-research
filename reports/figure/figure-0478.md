# figure-0478

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Quiet Finch 32 — coupled C40 raw-chart affine-U1 exclusion

## Outcome

No exact C40 strict `110/additionalweak000` member was found. I instead obtained a durable exact two-parameter all-SPD exclusion in a genuinely new raw chart.

Fix

~~~text
knots = [1/2, s]
kappa = [
  [103/100, r],
  [54/5,    119/25],
  [53/25,   971/100],
  [21/100,  17/100]
]
~~~

with `r=kappa[0][1]`. For every real pair

~~~text
51/100 <= s <= 19/20,
 1/100 <= r <= 1,
~~~

and **every SPD Gram matrix G**, the raw C40 stack has no strict `U=1` / additional-weak-U `=0` metric. Hence no affine member of this whole rectangle can be strict `110/weak000`.

This does not revisit the closed first-knot fibre: that theorem fixed second knot `81/100` and all eight COARSE100 curvatures while varying only the first knot. Here first knot is fixed at `1/2` while second knot and an interface curvature vary jointly. Positive curvatures and ordered knots keep the standard `N=4,M=2` maximal complex `V10/E20/F12/C40`. The rooted-tree reduction is exact: the C40 graph has 31,500 spanning trees / 315,000 root-labelled choices, and weak-free mono-U requires one positive rooted escape tree in SPD metric space.

No source conflict or missing dependency was encountered.

## Exact proof

For directed true edge `i->j`, with actual raw centroid `c`, let `p_i=x_i-c`, `e_ij=x_j-x_i`, and

~~~text
B_ij = p_i e_ij^T + e_ij p_i^T,
tr(B_ij G) = 2 p_i^T G e_ij.
~~~

The verifier clears the positive homogeneous volume denominator and uses `C_ij(s,r)=V(s,r)B_ij(s,r)`. If a subset of required positive arrows has equal-weight sum `S=sum C_ij` negative definite, those arrows cannot all be positive for any SPD `G`, because positivity gives `tr(SG)>0` whereas `S<0,G>0` gives `tr(SG)<0`.

Six exact subboxes cover the rectangle. In each, an exhaustive exact coverage check proves all 315,000 rooted trees contain at least one certified blocker:

~~~text
(s interval)        r interval   triplets higher total residual-after-triplets
51/100..11/20       1/100..1       583      0    583       0
11/20..13/20        1/100..1       618    280    898     496
13/20..3/4          1/100..1       636    317    953     705
3/4..17/20          1/100..1       571    327    898     935
17/20..9/10         1/100..1       488    365    853     870
9/10..19/20         1/100..1       387    202    589     464
TOTAL                                        4774
~~~

The higher blockers have sizes 4–9. For interval validity, the verifier reconstructs exact bivariate polynomial `V(s,r)`, `M(s,r)`, all ten raw vertices and all forty directed matrices. Their common bidegree is `(8,3)`. Each blocker sum is converted to tensor Bernstein form on its subbox. Every Bernstein coefficient matrix is exactly negative definite by the rational Sylvester tests

~~~text
-S00 > 0,
S00*S11-S01^2 > 0,
-det(S) > 0,
~~~

and every volume Bernstein coefficient is positive. Since the negative-definite cone is convex, each blocker is negative definite throughout its full subbox. This is therefore a proof over the continuous two-parameter domain and all SPD metrics, not a finite metric sample or an inference from blocker-bank failure.

Exact replay first marker:

~~~text
C40_COUPLED_SR_U1_EXCLUSION_EXACT_PASS 6 4774 315000 8 3 62654 d4fa55a16707753022533c7beb2bf802105c1d5fb6814274b2a05fc991be4fec
~~~

Per-box exact sign replay also reports zero failures; the six exact `(block count, residual-after-triplets)` pairs are `(583,0),(898,496),(953,705),(898,935),(853,870),(589,464)`.

## Scope and mechanics boundary

The theorem covers exactly: first knot `1/2`; second knot `s in [51/100,19/20]`; `kappa[0][1]=r in [1/100,1]`; the other seven curvatures fixed as above; arbitrary SPD affine Gram matrix. It does **not** cover `1/2<s<51/100`, `19/20<s<1`, `0<r<1/100`, `r>1`, another curvature coordinate, higher-dimensional raw changes, incidence-changing descendants, or C42.

No U1 cone survives, so there is no rational metric to promote and no new S/H/polar endpoint to audit. I do not infer `H=0` from Morse count. The earlier packet2x2 checkpoint remains the exact strict222/weak000 control with `S=[0,9]`, `U=[1,3]`, `H=[[0,3],[5,6]]`.

## Self-contained recovery capsule

Environment: CPython 3.13.5, standard library only. The capsule is source-complete and has no runtime dependency on inaccessible parent files.

~~~text
parent figure-0473
parent SHA-256 3380ab7732af243f6b4f5c5324b8fd086fd9a720766ad13a3940262d9a4db456

VERIFY_C40_COUPLED_SR_EXCLUSION.py
  8938 bytes
  SHA-256 f17f86cca6472b8d47d7e7fb4aca090853ac735b0fc1145ce639b95a677119d4
C40_COUPLED_SR_BANKS.json
  62654 bytes
  SHA-256 d4fa55a16707753022533c7beb2bf802105c1d5fb6814274b2a05fc991be4fec
C40_COUPLED_SR_MANIFEST.json
  420 bytes
  SHA-256 0abc099bd1f1422a6feec47637336d366b37d42ee6703c7890f8da209c877947
uncompressed dictionary
  72528 bytes
  SHA-256 bd6e95ee52e413809ce7469f2cbeb517271f863d5352b5f4457554c6649a0cf5
LZMA
  11196 bytes
  SHA-256 28e523156d5b369e6e528e6788d3d93d8b35dd102c41a44017cefefb4bc14b01
base85 text + newline
  13996 bytes (13995 payload characters)
  SHA-256 b89c7729d80379b47f44fb2687b30e5a8cf16d2f54d004da083c185f27fc44a5
RECOVER_C40_COUPLED_SR_HANDOFF.py
  1149 bytes
  SHA-256 d66b27076ec15b3e46d353b9dfcaa4f3751a07b6f4d472a213258e6b33164b96
~~~

Save as `RECOVER_C40_COUPLED_SR_HANDOFF.py`:

~~~python
from pathlib import Path
import base64,hashlib,json,lzma,sys
RAW_SHA256='bd6e95ee52e413809ce7469f2cbeb517271f863d5352b5f4457554c6649a0cf5'
XZ_SHA256='28e523156d5b369e6e528e6788d3d93d8b35dd102c41a44017cefefb4bc14b01'
PAYLOAD_SHA256='b89c7729d80379b47f44fb2687b30e5a8cf16d2f54d004da083c185f27fc44a5'
def main(payload,out):
 p=Path(payload); b=p.read_bytes(); assert hashlib.sha256(b).hexdigest()==PAYLOAD_SHA256
 xz=base64.b85decode(b.strip()); assert hashlib.sha256(xz).hexdigest()==XZ_SHA256
 raw=lzma.decompress(xz); assert hashlib.sha256(raw).hexdigest()==RAW_SHA256
 d=json.loads(raw); out=Path(out); out.mkdir(parents=True,exist_ok=True)
 for name,text in d.items(): (out/name).write_text(text)
 m=json.loads((out/'C40_COUPLED_SR_MANIFEST.json').read_text())
 for e in m['files']:
  q=(out/e['name']).read_bytes(); assert len(q)==e['bytes'] and hashlib.sha256(q).hexdigest()==e['sha256']
 print('C40_COUPLED_SR_RECOVERY_DECODE_PASS',len(d),len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__': main(sys.argv[1] if len(sys.argv)>1 else 'C40_COUPLED_SR_RECOVERY.b85.txt',sys.argv[2] if len(sys.argv)>2 else 'C40_COUPLED_SR_RECOVERY')
~~~

Save this single uninterrupted line plus one trailing newline as `C40_COUPLED_SR_RECOVERY.b85.txt`:

~~~text
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;TumYd|d!Nh=gN7jZNOEvCa&Pm(89+o?N%!Y9c7B7G8(PJN1b^)WFu~^ZQ9S3+a*}z?E(*hIWiFSsslF3d_vpu8cD%y2+4*i1S}seDhi%XVk+J_cd`?6^2MIsUzq|KYg3mMjTfN!ImaTfFEXC2!=jxvZjz}icHtN7^)yFKX?TxC(plBVa2&0@*&Nvg@F!M_;puBidS*IP@CP$BRc&~UET=9Fb7mZEPxN`x?8zzJA2(Es{UFOfZeWGt@SQPT40lP^1CP)>b5krYJIkt13}ivl?**&tDF*xdT<?V!kiX!__h5SvwrBpq6`WS_{8!X94-CoNFg#Chc*9a-Dg>rOB)vrZYu=d-}pPpq?s-2P^DM+47Xb@5+U8Y`W(|iDG#psmPZ&zp=MP;<bI1~qPc)*s~O5Uv};$sIf&LI$gg)3b73$I^Il1xkN(p;M8+4`vc1a|nyyZIeATl=n;RwlWG<{@t8R?|-LeJ9_gbOuMJO2(A<?HaDSdwu4lK9w(x4ogxe(x$%_4b@A3tJJKf#OX>VX^<h`=FB_Bm$D1tbhZSP6SGxLenw+A7qv>H057c{OAOe;svW{ru=^#{n4T=i>nm1;~xi;W{)(YeQhGO+MrE)cZ9$MBWxVwhYc8a(>ZoJWO-20R|P?a(St+(Xqr8=Ie_1TQh6DtNy+NpfzEfcM!Vgp|?gDHvf}ZFjlv=p|^%UEk9M8?Z-z#t-3@~?iB(mM?raQQIW$Q{RsJj0md1Mf#>iqacS@fU?PX{+D^Y7tKpMR8{W6i;tI`jA39*TNB+v1;OA<VP&>-fzO?hjhAuP#mo?tUtiy+o9Leq)NS?uSDHytG60VM7piK-c1SS2{`}+gP6fiHF$%!(ej#yx&s&J^xU;?CAclt_kVIvxH3E<y^4REn4Nac7GX*6+R{J185=j`4C#ikrP<=*jX>GmDZyM!l4@rWWeiL_>l6Y}tGXsNaFOz_@hV=4H-VnTgPxnI|SRHhr9y${W~gQ$h$K&rjdkr5EO*?oxPjrJm4uTn$XMDdj&qfs*2@*n3dPf?m2s3#;m4YGMxa+37IPftwPFcIp|DE?8<iAF1Ei;s6z+wMqFi4jU|xuPM5({MkVog=u4(L68Grwb|9(Ywx1C2r;e7^oMA#n!%vhhD?q0NOTvuZwjL4Mj!;!ey^x7cHV|d_79X5|{2NozWMkn&ELYAF$HEC!1#(sy`J&0bw`x-9qtlr->kVq}HS$HVs3$Cn6EO3sD;8h>A_JK1&KQ>KliAU^Qi}TNp6YFHhS)ApO^WIq^{g*w1;t{({JFR9HP}AZy0SyV0H-n<z3lZZo4+uVeZTKUhOEmz1%2q;<c}RQ1Oi%h+XHcC)mx7!~((Eq(xu6GgBF_)-wb-;~2l48T73k7${M8>(^mS{{|4gAotCShz->o|$IC%|WWQZpt<jiExS%ESpKHdjhF%V|@-<oyP6b?s%iSOU%(1T3dMUVGY{FvFOt_D_eCrgA4ZJe3!Y)EIPgsOQ@#QRE2H=sGj&#)?oSN!8O@fVMi4h90hF6=y4^olh>ywmoD3(0u3xS4C`iC))tx*jQQv9*{{P>9W^6wIGJ^2{ge-bbusbUu;;Y~I%<Mo4j6uCGOur<jJRx#NQ6-}u)%HBmC>4Hp~W+iF7hV2rduaYbGb+iqFr?nr2(}9^a+4;j#lFng8_g)Za$NRAipqaWonkTe<uEFokYBZYA5<7A+3ZK5H`bk*me6|s3gT4-FcpyimEIGY8CuLa-pm*HOFE4yo-p6qd>-~l!>)WE>Sh+YGk-=|6lL+5_0$QerJp+D3J0QxS^N>Tf-a}_+R#QSXeP3s0?)I<}UXA*s^E0SX&&Kh6HV`akjhMZzxW8^L#RSf%T8gnI&!lMfEh^%sCNo)Q>cH1UaG#<D76|!{}EO5>0PYKVky4$VIrK0zr1Cqwy=k;r0&Zl5zlT1>p~RdKagP9zp&8lc20PNdl^k_Vs|#j_wSysVecEUcZokCBvlX_aJm+W@`v^T|ak_1R{ea3QPoCT}9j!`^iSZFUl_K`jHhCxsZr1JuTXF&%WK<Zlt?(r?i36oKhs&w^LJL&Z`vKMOJs{fNb>)j{LqE3f>$!(tKbC6Z)`2)-+;xnXRsm8#`6exHq+L*B~=g!udG8H8wl?%^n1hu?H;Tx&$e{1N+I`C)aeJD;cZSEw8MTpE-(3)6FFsyUbL;KD<I6n&(T!ATC!Ui6(SA>O?cy$qAgd-0f;6OL(xZ+hZi^ED?Z>5R>T4DlaRTZbY}zJI|Q^89vWWAk`k`p=_R{W?wP=;W_J2%6=~;<#1V3^;`$}bgD^yh0F&wZD9I>z55Y28u}#uVo+ydKL1Pb*2~uYA3W&Fr1B_Fgms2LX&P5LF)aaC3zm3KE>JTrdi4`9he%WH2mIR(JD529Cjg38G&TkOKw?!6Y_j|Fw7eEvv#3H`GJ;2y&)$?e6E^}<xO6%R&FSR$JK~j62!nK%D1^C2R8G_GJBm8Sk*45LVkzS0S~{9ceKvP`o%oRNLm0&kgLglC7F+ekA`<F1f_<%avBHx8(0)W5%v=6fygu&AA=K%1Z>`5Q2lsL@GLKnV>&KHV$3~meS`FqX0p_<|OwUeI!>&~uV_d9#NcqKqD94hSEQ3`I`aJny`@~g>vH+bM=cpStskj#`4m1)KzeIXc`L18s1ls&%T00Q=Ai604AA3=K<Y3vUh=mgIefw*N;6M!s=sHI&U{kN{Dcfaw1>6MN-HDgdU6gk7ZF^fzMiVg2$S|U3RHm$)?06Tw>E7-OO`8@$TouYC!>siMeaaCfib)thW$5c=Bj{#B%v-Mia02CXCAEB`p3`woWYNUGSzM=rP{f(rskpKGN;NLr?47b+oMoMMTYy>!tf|NO2z-J1?2L+X^ZHRTpCZ;8yN`-3?wpTLQE+H<LUOz7Vcz8PteX&g<ONF^)^#6^xBtfP&s56FAC)Lw!x#fjCHZ~BFGBv%D9P)m-Czxh1`S7Y$|RCEE!VWZr>|6wJb0Xrde2(Mdl925ze_2Ppq)&i6Z|h1jhiH9MUh}wvaL^!bV-iM72id|nu`A9ML{a6&H7*r(p*^asETrt2QPs)V>^pnR39W{T*oPACune-UWnGarofS`1dgcI(oWk^+>;@VU=hYFaW$-{HT1lQI~XGmq@O2!*`!sCB6?O>U3bHyYgm_LoUXiG^p+@GZTTel%m*1#LEMU=w~OtHFpgFY`g59Y7X176#6}=byHu6NnDSmi-PbwZJ@pL?(hfCt_F4F6^lb=QB7*QG;Ii?irGSpJU{|dhDmUK+otY*vCE)fQdB}$dxJGH+BssURg9h_O@2trG6JP(K^Mp)TC1Wg?f9H>jP#@#1xeJn2nG9zORH~cx6iEmW1icpxXy7MzwvDq6tP9Lgt@=~(w>krB*j>4nX1njuE+w!<*xkE`kX9|^fwppAPiav`?@7b;KrMG>y=U}6r2znmpO73;`g~Y7^!f;k+p_51H<c|dxv=i>YbhTgmWN|lO`ENRUI0r1iXEZJQJ>0=oqqY1;fgryWxZjonH<6$WvY~hv3;;ZV9b<W$ZXK)ffZWYrqw9RPs}t1oM0b0x2+Tqx-o;*FNN|la`MQ*8;KcU%saH2Gls}ca4>}GgR)I<Y_eKT1RPdGm5bLi9=Hhet*b$99RJQN$#;Hk0v3f9a**I}r}@35bOCTm?{L7{VX$}=B#g8#Q=jqI3H(nDQ>_}-FoyP=)Y7xqp7%8}s={;KL=8z+*gP(bj|v#_RmSe%-J6lbmym)ePBimk>(}Z*P1d4j_%`35YK?3pxv+Rc<b@BTZ9Pe3Q=C7zkx@8b?pZweAksb|N)fP->I3Rv92q_%k#_-Bj=xSz_sD%_ZL0FDX6W+3*>${Rv8gJV(@p=EO#d-R7dLVTpuk0}`$6egKEx66Lfw^BSv#L54>|4poS+V?VgW#n*=-nK#iYOJ=Z3+!000$Y?2%#zi@3JC7nP~n3q#T-T8H*!vq+1H6zQ|(nTmz6f3Q{bcTebE7@4ZwM90ua@Yqc)btHlJ;!)B8$%Hik>N0rC9znsoKCkugGM`0W?zNM-x?|;$7(;eKw6NFxfJ{|N*v=ZLhN--frO>a_7veWII9d`jK+o4&bHs<c>ox;Dq|ACSwP<7;<WSO~4@qyf{<iXb)#+caFlLD9Q_i5bN7GC`?Pk1he~R~{;&S05%15A?phv9wV|=;B2doC#d?WtDZB--t5YK(Vi-9RUHA2$-j$)M*eEe`19(4CQq3ozIc!@hdFHo)@5F7)s{k%B0+Eb~9rqajzCyB9LtXy@CT&s~+9rzr5rq^lw<{?MZa8=@_$PI?o#CAk1_zS1uZqk=OwfFZTV9UISbWexEOUSIsa>^LOprEy(A9TL@)z><3<w}&E5{_2IO#nNDxE=xMYQB~hztvxrjmFKVM6Qui)sH#*UV5Gj!zy@+qfFVyb@-mwhp-}o*(_j><ow_MqnFoq99!PIoH~=k_1|O2s8^3URa-&;w;}pCd}gDl_%ewi22Ep#d|cTU)|ZqkgAQgB#AfBaaB&5nKEXAp9gmPUJtlpCy!BLR=EZdrr^bgHuwifl8My3Gu57Ct2jmu=p6DW<8{GL6yJ((TP#~N%Mk=(v67l)ygFtORxEv3Tx*Mc(rbEXm`j9UM=BE@3@gz}p#~C~5;e=(SMuXNwS0QaN+<p%yo>1Kk&v6M?S)_Uh$`0z2_x_H?z0ySl05O@)M3_VM$X0p;c~*5l^7?_2nT1nznyc$*8AHG8#{dsN-mK>2mSw|FVMji4{>hv~nWDzkrB2v%$$O5lT2b{7G*<mBIE}upd?lo*Bh2a2_P1nTpHvm-&OX&T_N>O&z@&B+86dlXt@+>TsXuxJ6WCWyEHAmG_`~NpGiuz`1lTN99rKsjObKe+uex&N5wO9nN7X_u#m8qB>aJcB<cBh1cj6=bn2g6z&p5xG91lm2;QVK>LISP+a1AS15~kLpIsTvN?5Gm2xF+qdcUo`n4f597mguZDA~BTEpG%)Zy+*xqq4P%-?fZnvHFHa{Fd$8Dh?9ZYx#(?hkzr|nxpidQnoD*Xsw^fS-PTJ*=;r7p4z-HkHjvg34jS0sl;eP3QV=S8usR$ugvWx78*vMlaffltQ+r%E_mf*93A2YOw=$^xy{4Wqi#?^|S+r`B$p=-Dg;85Dl$V~EjD;$U=~w++{<IkG+ogmmXvuUw;&c(8`jR{tRF=%;R^E;`Jz>#e43}LRr9LC;{VF2P(+cRan=u4q_oif4&1<Z(b4=AuQvbiBPc5hi3aIvVmFU=@Kv{I`G7wSR#onsXZ)*Wahl2_|`7#ShisHWhj^SWv*B~fuS%C%tkk8T%;@e1hM@((jv-?5R-M27b0A0r_E*}0UlQ<uj>Me_?b0Bur8nf0f(<4maFJXM1zU+QO0p{W?R(zjTrjKmZH4!=Q7FpEU#nud39C~B;R4t>Hcbjjo*xBB-!4mCulDkv9VAvaD&T#LUo)_wU%|1aBH2g>tlelEJJCrO8)xWJ1h%>3bILP@A0c~U1e0uqLSW|BLT3vjjRv&43{XZ(QpRjMLv#(NjgD))xcW!PkZBeSI5Dshwa5{og_xhl3CAgP3RmW0&56s6QHkxSW^W4zC?vJ|89_G{kM&HLHX5qiC+(6#vZ7Bs2{2W(OZ8|32vFsR8DBsOtgW|qDuMC;a^%%k^Y!gT<Yu%c4yC7fY!w@7@scilJ`?VRt;0V+?@u{d{9(y7?vo}u@?Mbxha8+Mi!@PW&6i3ztvp6Bd{2R5VY}{V-KI#Q;LA^8mx#yu2hICJ4EB?3*AzeJ{Nr-zHoY^%YP1-SizmOi^75*}5nQ3_%kIAG|VXR&Q5*bLK`veOd7N~sBQi$_Zaz=~@%4<Cm5G5cm*Q(w%dT}0XuwDZLp&#%TAwXNr2em}LOEm<@UH;aw92OF`j`}sJ3f5qrdF5)M>T}Kn>6Yl8EU&dQ2MkK<M0taYAI8zYd3wFcX<TO%$SMim1mOb0zEEXjM~Ed`zwe9%6Vg$;pm=R4{=B8u4nYoaJGKc?U@~=6;qG*42x#j*{M2BC;#9hZ`!cUs!;0H-qT3O}cI$DhZgz<%RIkVaxOt<@io^wO@L3+0)pMH3SMEPO*~cB>0bG}XS~2VQJK<y`IjNMKe)+;_EorF5FUXY;by}G#IhHU3%Gdj>FKbeOCsw#;*h4Z<ea|93FX#Ycu2-$Z%@=5P_NW{tX(&ydj_ds%I7O$Zvk<wo$jtc){4o~zJ#M=&)j1UuH_IOD+j!y2gv(Gp0voXerh+h;K*sg)tUY2n`0+I7JeQ2%a_f!BDb|Q3!|HHCV;C=z<L*kpgRjbCz22@0L0MEp#ZB=pP4Go^cmL(Bf?-{s)a(~i9TOb#G)V0~oYGx#$eHv4#&5aHgWk@oJhCTv!}4d^r8B#AD#QU>V}=CZXm(=kAh8i%dVTldl8xgTKAQc=KM2}3*Dos)MAM}<M3Bxbgf!Ce?<Or0CB*~Fc!cF@Y-=NM4EAmoF8neRB;$^-B_PT%z+U%?9~SM@7*#CPZIDRCxD?Gs-1l^V@cB<#Ce)HB^m<VIM7gw=BdJ#Fkdl66R>kKuDwz3gb|QYrBMuJ^fLs;>XL~nYk~Tt6!`By1OH^Q^+0eIOt5ES;S08aPzx3$B_&vVfYFyz9lh5-}fXCKQ;RKY;Ei5{4beVIqrA`Myo_GjNE1%8ssZ@zr2QmzPLb#~DvF+&M$|p|&Z%7<$8Qon&XrU}kZPP#PZrp<%A}J%e>YOyw8NZ;JaiOOVRI)s<fd*1~ctC571W(nb1RJjZniAzynVbyWLAIev?Q~9nywX)(5Hqt0Zd|1z`zT_~nOZ%%_W=nOeES<|YI;XN5w+vmSsC(&pyh>bUS);JrIefRF1T6!5!#*_8Jl5H^h9#--m7}%c^kRpvf_za8(@YUuL21K9uwR9U|nSXGxJL7VM=c>Wr&`pS(9r}B;E1zt0sLI;2b&Vtx+$kp9$V@p<7P5YvvgN&*t>FN4EBO<FY|(^lQw+Zaq|8-H|i#e{S}^_Re;Bj6z1fLi@~Hvu7a5Q=7Y!bh?EPpYow+4I>1?uHDe5$tm3{Nm8O^UP_31gM*;#miR0cQ13c)d>3Gi*|XBOYgU0N_%>FO$30`1A<v1|>|T3MV;CaG+1Dke;F4?wBhIik>!KDm_WRb1%)$|<z(sGYWiO@9UB(V1%e*GDTjBN4k)#SJ{#j^^yx&OTqJ%8;=_&U>Gy?Z_eM!vmblUiKg7R7`X@33bD~__q7dPh*=&9mdB*CyX=mBO`WGZK|Td5I5U$W!TQNu}q&g{>Qspu#@F8Hc;v3K><y8<D&3xP;Etrn3}#J!pQC)U-H=}~7Mc`{{+{ZlOP&v_MZUVDWRPV=?g0AEw~I_`4JO@R{al}u-0%kKX6Lr(!zz8S@czm7!oOai2@w@8Izg2Bpxg*%?EoX4vTmOx&@#4o@V<iQtNNYX#qiQl6Nu196~qQ2oTiSqy$>y4u%9C(;lJ`H{L_y@=5KsDnDGR&YO9!!mX3kkCJ-yUs+{CJ(J=JLEH#P{-I`EAcFju0!GiqZ^yxo-2a6UZb{TzPG4ty9@MyExSBq419fHu+d$TjOB5&w(dF$*2#06lKZZbv4!LFB8X@onxEM24!uH8c-U3SOpgHPx(rRC{<?*!nwT)ceFe@9J;Cw*>gBQibx+syMc}?H2Kfs`NrXWqNn$Ny=FnGC*HBMhZwLjIEG|&u+fAhbTaMkr1Cz2xNK{<#SpJ|b+YOG$8`SAq8A1Ue05~HD=4$KmUI&J-*yq2^Lsj;8R|RAH6j9I|6(Q+_#M;~Y8gdlttGL(#Nxt=-BYQsaI#jFrtag0M$Z(A$a?LS@LHHS;i||Y5PNXNNZ<%%24dQS$=Ft5fJYqRZud#X@x;kX<3)X}fl~W3Tbqe*%d0hVY^u)uxBR{rIIEyK@M{-R$Ynf6GDqa!!F%m_)q=OWpjce3i2VmgeI;wSvJ-^iPJLm35^f+2+&s(ml{S{kA-AaXp>=_dd|+8LNX0eQ%|_{b@{d<`>w~0;-@fZ}s67AEjpTSi{~*5qM=-}F6a^9#x}iA9Wcl#vqN@Sh?ar1v|2W($0>Hi^*4?B%q|pd~kdd=L!jR3%CH}RKw7y^R$6;Fcj%xepn8UHE*BUiVX+ItRE0=2jT~1IcFfU%TSk4R#OF7Z~Ny{W~s0Fr4+icwz%`f4OCf^9-XUPE~!Q8A{@?hB81ewN~NAkM~(YP%CV|j!>#-M+k$N{$Zuj!6~wFZPhDNL5TxaJ}huUyxNNV*<${JN%3n^+5RyN)rEuyj3;6c{~m3|5~&{E=hx%Ja1EOhYXNF1pf35gz!S05M2Cmg5q5^Zug1b+0RGjZ>pxztBHDzOSny(C@Vf1!9!%$q!M$cV~8{#FC+)B(^}}HAn!Y<GSrXK4=k~>M@wZUcEKU<8We5g8QD?dP6aSnIJ)IzDR;I!lk3F;0ey~+_c3tUPHGrOn2t1)u7jh*SX(S^+`}AXGg+F2pOvuA;sXsaKb`d*{9PBnOP|RE$Io4+y#Ad+?saOPN#KC`RO_i^zrRUL5_Rdv_(wEt^Wp-<Qq=Zv$nQv7Z>XCX?HNHcz5QvHIvvj$?9-vIz=K7ZH_f=OvWfu9Hdf)H_a#J`PlN%lm5<haTp-E+y!s1Bd-^}RtSSLxyxNc>NCkpCRqlCN>9gQx9<U=ZieNT9mkNJoo9?;!Dr?&;MH_OrOTw2e~=&kcqV?5go4KuS)&Yfci2-ZKC{I*e5d6q;^<Gn-d;?~k;~PL!*Zi#gx~&M8G*QwGa`sf762ikP?VaK1S>~qS$`?ix#G`skRAN9n!8IjTk2Y>^>^rS{ZUlYYKbV^=Q?p8DT28p&4pB=%wpI*irw9`tC$mOGjhcB4@yyNs{gD86*dD$mbNPxd4NTL;;s=|p3-Si8{unE(Nsnq1W(4rfah7ji9Sbu@Q8$(uZc?nq~P7)Jx5ayKL>l|GR#&JYeCI~*SlZ_R<xV+pl%*LBOC89-WLsc6?SGiIZoC!o}PWw-XUasHspm%lD*-Sx%77dDjoFI2Bn>*8h-g(sK|3vwyW~t=#4je6juHpcsK+6<E*=KX=Wf8>7fS&eLU+ZoC-e<ug>)MP_^U+R6Krq#sI87=oH?EGc}ppXh1G?ahp@PyTV0f-veYA9&Ip~v!UW}uaHJsYxqFO+tgjK@_}z5B`MK}G2T|c&y{QdQ@ZQQD$__|2m(c5kovlTYMb*fRdCAt+6VXR6p^J`PkWjbj59;-$v3R_&(1L~mur#)typ(e;<sodC;CcGsA#ILz!ekZF~w&*^@0#z$HrpFB`ic5RttC=Ds*$nKFn#CMi@dljH%2HeP9nog;Zu%wd7<J+@5wAF3*fj-gp@j?vgS^gyJCF)ARk6))@wU?|n5^)I-<f<d3b6_BVDw)kS{im`8bGL5i}p(^!WtH6wl~qjJVA1=@3}sx-K=cre0Yn7v{PLfT~t?$MINQY^mFYfOHqd1!g~vz6WFI&ubE_+r#0M{J8iOLreNLqdb4M8k7vu~v`4P-XErx=zS%<?&1uPeF$H8rkOMf?mCz)rFX1cEdnn9J4_tKV+p4XDazl)3AC_m}TStpGgP#7XafmlnN96OHF(v;G=ow7?rhOKwD{mhtUwQG_P%(L1N}AOh|QoYRym>UHZ<S1)>H&hiusat}by{N2i4N_^(intP7$zqe4CE!>K^SLSZ$=*o|Mt>G(rY#%K>G5bh@W%D@iW)5`@z9KJtCI7WJXk;`I%GRkJ;n4_?a74RN4bXi05Owujkzs){kQA@RcHQ6Gp=v77cGJHCNfxl_D`?Mmm(;fwI>PmGMP9&ydng?xsD-;wjE*YduChn9$7~p*hu`6IP$d|6L@K|vMOXMKvX)^4ikgWx-%-~0C*eVVq7iM85g-n9wTVww|G>geg^?05+p&lI_)u=mkb5G{0*hEXqCUQm(#ee+vzfr*w)^A?x+u_Sxg4D4XQxIDPe#2mXnxJE#wb(6q;Uk5S(2+U(NU5=Mi0we4|J-epWnzkekD$0$j+rrhpRNkt#@hkBPW85`B`*<pHbk77a3oW1d)F#_%MN_7%xiU%c+IlawBO0g%G}dgF)6hMmbmT>zhBSREFFmKIp7duh?Ti=kSE7q==KP9st5(P<fo>MdKL$~W+U9+5LH?W|01|RL##}@n!IE<L16qSSo6+=`X$Fcd%xgi))C{n<hq!L3zt3*<YTJ1^?CY+=;7MXAi|qJ=b*Xw{umfM4Pym9_9zd@2w3=_8&iE2dq4L8rq|Nj!x_H(;!kB%*)$mRIBcC}U6zbyy@Ab43o-7@4Fx;lmqujaAM4UXWUXZRo1=7A1nO<n0|o9gDm{D~V07?b@ezBQ<|n%utb5&L3&2*#Yx0J4IakIhoFPw+RlC!`IblWmRY&nIeDK61agBK3fq3+3X$5lMp*P(E;*Ld;;Y3<_Iy!tV!XEAolpIrI47`dHBvgXt+<)kv6`R$Oe+SYecXz@M1y3Kn1~CHN{u017)iP1++sHeFypK+xGHDFR4L9eH;;>^}W~Zqhh@~b4&)zxvwC{e?M|otBI8Jt0B{Tl3Vn@S`s#c%+7SyvWK70IyCn@;gIBy6nZr55QmSRmN!VDGE=nUm6dL6G?bBk`a<Nb|%l7LdhyF1_JF9a&@nP4k>NXmI#4cQZ2p)cv@=D8oyf_An)u)Vg#bMwbKc{m>~4dV1nRqx&P;wBs&9kBY9;8cI>*XV~uwNUZXb&Ag!!zPELR9@~whM63Ymbm?&N*ws$hO?l=>i`#(+N!ND%C4Weh|g`7v^#Cii{{w7I1epv*(A^*&`GZM=|~!@LGWN!Cy~@;o??j}$R8h4KW)PY#tz30lwCI37UR~4?2?&098Li7p`npqRSAho?_D+>msXN9Bg0MO`WE~TDpoI>A^{Oo)T{C+{J(_KVcEfD=9WoD1xDYm!C694bOoR)HX=F(b;_qyY_N;px3c8L4+cKN2;k7VN{6BY^BvSzJfajJETa1ONO;8k5|6*tpuYMjcdmTnRoZV+|9>^^)eU(q-&uu?a{N7d9Rt+r{oSrIdQXm^j`Z7(>V8(2in++}SSXI_hc~`#TRQf-^`?x8rK(|uD{C2z*C!@D5av;r7bL|$Pt{Ofa04uB+4+F8L8-8QW6F}ZiXX_dy7=dfX}%W<7e0L)4^5o~KcVcI7C(qvK;|`xR!J9P>U4k~&l4|54l?+GH-VAX3om>}H^#~T*x_uIa=-iVP5Z6r43>Tp939~?HcG#^^kaj*$hq#VrS{j0#si-OS9=i;Fl3DipdhCbJ7w6>vR&GjAbNFBT;%-s<bz@AQ9o}sL{dyzYWCx@J4dkCV`dN;)ho`rE;`<;Mc5I-SOXFNJzI^oro#=y8reQsKc{{Q0lK!$XEBvIBBmJ~5b2^p%a1RNkIkBjOMXA$7F&u8*7x%;*em=mDa4seG}IN3&Wg3(*gVaGj~^>8$Cb_lwVl(<$RBr>Nov}El9}##T=5IU=GR<HL#X=ns3?LHtM+MrGdAc>gSsILL*9yl&K`p9(|kyi<sTX%sef+-RINZP?IYR!fgU+M#cB%&gQ6S<xy8I{ttm$cQ&otPHZ85w3gniz6ajDwchM~**KiPL4&-FL+}Q4U&xd)u!;9X=GL(k~M|kFY66uDJc=!QAA(qTU=lN8+r9mDFtXgUDTaltzxIl{^1F3<}(A}MgNzqqj`O=i;rJSu<%+0$SKIHHG|M--8aMZiX@dH}{Qh^qvyMaa)lpW?~znlN8&xH}tYv5)YAFA>Gl#l$Bu46uoONYNdM2kYrAh@~8!>@D6eL;sgA-q6AO@1HB%lX?c*A}k^Y1g*F*MM@wIM><Qww62?&5iAvIU2Q<6JbCs?PhzX9A1oC?6Q7(W#VDf<*#Q#@}s}rM3}`2M0L%?eJ1N+Zog!%kR9u@LtXl*^!%oMH#;cEN6N621MJR{cI<~<uZ!P?Dh`*cCLI@gd)#knGu)DH;s|fmFZ$jEZF>kBbf~Ms@P>M6_L;7UbC;nV_8u)YvvzQC5OS+jdhqf-Hdbmelw<imYaLgzE;HRooka?CWC8t_Ax(Uj+Tp>9Gi0>>Gxr6XC9AtyTWR-zzevk8EtO}Cs%x^N0P=8}^8jLxJFOn_utT0C7(-wq2n#L-7?9@a@x6{woh~Q4w@IeV#>Gc|SWTB$yHwlY$Iq2QC5rMn8=}AuJ+Y`Yq-P0zkPY=_DqJ?v^AMCDEyh;p_gIupXi=Xhl(>}pivwN7Z*7eSs9=9Lpukm?Z*QO_I{y%0;3^$z7b$HVhG!iV>cZ>j31zS)_9%`#{^EUZrtm~RTgjSY4lnL;Hg{CW_s9D(caN5waab5TIOee)kg(jXQd1)N#*^rsDIc*wfF$$yb1<t!Q^>94VnAYUVvu=Ky%sWGD3o{Ds2KN)5D=EGX{%%S4La=fWaq<nVNNUC_gBUU4xK=Kw%5Tiy*O?DHfD#inm1JepV}l(&dCy@&2Qg<dDrOh7qS49M3iTU1`$FNBzm*gT%-)fk6+@)zfNv?kg$@ZN31T5iEE9>PhRyzR5-RvwQ+Yljw3mPU&UxZnMeMe`zjVg>TVU8lzwijK9nny9!GZf!8l8G<9>{^covzcMw+uEMx#+V1&yGex7_X0V8_Yk!epdcRd<1hI$icuh{!<gP(2(SiM^Q_P1@_I>m|aQ5<7T9#u@ZNodj{4sF=#bw;>uX&FSQo`BDdzS3DWaeByy$=6{#cL;oJ|U4IATW%6M@Tsuy2@wzfGDV}JBdK7FcOb7Ejitan2!)<vy;iThFfLeSi<qan@U?H}B{UwFzRN@W-af7%V)e(#1Gd_GBhg^Op6((oh!rBrmuZJ~|>xl_28p(COU8`YMNuyqPLDj18F?=bzxt--I>L-T~1WtRBD?2$8(z~unnl*{Dbyr$<%nJteH1+H-^vCd^mo59^r9zVw@!Jvh@)$bw%obq+JwZ5?Xs<yqtB2GP2>K~{(-GH+XNTaYv=Au6-PkV;LKZPm>O-k3Y$)S}dr|w`FZ;rC_01Ko66m_eYLRPbG=HqCB4ZK4_r~8KhsS{xJboEtkOfpB|HRe{NeBePrcZ#bmDuFba3T&}oO}R=waXE@;D=_e7+Y?2>JlU&2?7)>-3fqa7nk<B_|%$4U;BniUu)!`xXTTS!C@>5Nz6!2fMgTl7DVVW=!3wRWFpTtEW`Loi140Lp!M15otjPMdZ@<ShObsRdYZQH;HbQeS_73D_YbWK)1P!ZUjzwaquN0Tb7)O>C-hFmLy}o!x`RO$XfOS0g$*?m4{-zSS)AQiw0+k)iFTu<Ws_xmW$Xw`Tp6O!RlnML%<<-v^Y!N5c^OOO3#soh5ytK809hI|7f$dBA|t`>*N;y~pQzv<U|w5irZPO114k>zS{wn8!b{2WDz3-02L^sNYafO#;H(d9wFG~+dKwe22d0B6A(cm?`q%)E-}~x%S*|yoJN|FF)`_H4?-f})cw(E%xh;J7>JWfZWO}m1F;A!PUv=Uc9O0iXsz7XdW8yU+`D&!$Ot^F}x_dV*r4xW5Opxe+`C=yztM1xOb!9DP+n;&8x+E?rjfyl(_7Y$d6Q<k&&<P;vfU`ibQYE`1q~G7SfE3EF$bATw-o&0ho@fve$215;l)j@>Dt@DWn_irR4a#yvf+pQp`40o;h0=cd1Cu4xXbKp+x918S$=!b7)DxJ%PH=OGo#lT!2s<q0)u#biut#_cQ$Q-^y$9>pSB#;&(b+u0+;e3^EK1(fSsSH$DQ5=Ce79~|>9<N9bUMa+#{>tr%q-di`LEpspeYk$JC8E;B_L!fXk*}LpEtp@AJ0z4N&JrURNw`jqU|FCN?L4AgOGBgBT3m6_7sLn3J^v>ZXD2S?RRBcRtf95$tJZKp((6R?v#U}JQw1ktay6^9&m-L4@2TBgnUXg*O%&)+D~v1$P%kWr;6&8kUgu58VfL>0etxE*E3I<*QM5eIGhvr&&P7(fpx63GJj_(b$m!uYC><$35;TH-DM6*6wB&AXx@<cY`QlwCXj~Cb<dPjmR!+?b*L%vPJ-Hdmo&hHw}H-j1((sM4#-L7b(V=Y$3d^{n(z(a`6@#*kX(R&+)wsWUB$L+tnh%T{8}4OaVdh-%rg+_eiy6eq{@2wan-k?SPtcHQV`}a!S}Nm+0wH{go^B&UaBt~=aBU2lZxWWo^+@gyRtx?M<N*WyGtDnoL^;Cc7ev}JuVCf6#vBfh8P7*)%rwj<i?-?<)+Or5;bJ>00Ed+(6$5s7p=HEvBYQl0ssI200dcD
~~~

Replay:

~~~text
python -B -S RECOVER_C40_COUPLED_SR_HANDOFF.py C40_COUPLED_SR_RECOVERY.b85.txt C40_COUPLED_SR_RECOVERY
python -B -S C40_COUPLED_SR_RECOVERY/VERIFY_C40_COUPLED_SR_EXCLUSION.py C40_COUPLED_SR_RECOVERY/C40_COUPLED_SR_BANKS.json
~~~

Expected leading markers:

~~~text
C40_COUPLED_SR_RECOVERY_DECODE_PASS 3 72528 bd6e95ee52e413809ce7469f2cbeb517271f863d5352b5f4457554c6649a0cf5
C40_COUPLED_SR_U1_EXCLUSION_EXACT_PASS 6 4774 315000 8 3 62654 d4fa55a16707753022533c7beb2bf802105c1d5fb6814274b2a05fc991be4fec
~~~

The decoder was executed and reproduced the source/data byte-for-byte; the exact verifier was executed successfully on those literal bytes. Convenience copies: payload (`C40_COUPLED_SR_RECOVERY.b85.txt`), decoder (`RECOVER_C40_COUPLED_SR_HANDOFF.py`), verifier (`VERIFY_C40_COUPLED_SR_EXCLUSION.py`), banks (`C40_COUPLED_SR_BANKS.json`).

## Continuation

Do not spend more search effort inside this rectangle. The next informative C40 move is to cross a certified boundary: either push `r<1/100` or `r>1`, or more promisingly vary a second curvature such as `kappa[1][0]` or `kappa[2][1]` jointly with `s`. At each rational checkpoint, run the complete rooted-tree feasibility layer first. Loss of the present equal-weight blocker cover is only a nomination signal; if a rooted tree truly survives, solve its strict SPD sign system exactly, rationalize an interior `G`, then immediately audit actual-centroid maximal faces/true edges, strict and weak S/U/mixed-H, and the same-centre polar landscape.

No C<500 strict110/weak000 body is promoted by this handoff.
