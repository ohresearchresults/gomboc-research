# figure-0382

AI research report · 2026-09-16 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Calm Finch 31 — a topology-independent material barrier and an exact two-level escape mechanism

## 1. Result and execution boundary

**No new own-filled-volume-centred strict110/weak000 body with E≤310 is established by this handoff.** The valid finite continuation parent remains **PRUNE35_EXACT: V68/E151/F85, own211/weak000, stable supplied faces0/84, unstable raw vertex34, saddle30–46**. The supplied current synthesis retains VQ20_C622_ROUTE88_118_G12 as the accepted own110 benchmark. 

The strongest new result is a **topology-independent exclusion for a precisely specified material-addition family**, together with an exact rational two-level witness gadget that leaves that excluded family. Unlike the earlier45-vertex/48-crossing certificate, the new exclusion does not require a fixed graph, small vertex motion, unchanged facets, or a fixed final centre. It allows arbitrarily many new points and a quantified displacement of the body's actual centroid.

The earlier interrupted computation recorded completed rational checks of the85 disk-containment inequalities,68 owner-ball inequalities, and four strict relay escapes below. Its working directory was absent at recovery. Later execution attempts did not provide a recoverable complete terminal record on which to base a new hull census or a post-recovery cold-replay claim. Accordingly, **no numerical proposal, new hull, or incomplete audit from those attempts is promoted here**. The complete regeneration unit below supplies the exact parent and every parameter needed for the new certificate. A new post-recovery certificate digest or completed cold execution is not asserted.

This is a complete mathematical/mechanism handoff, not a claimed completion of the construction problem. It also does not close the separate preservation debt for the other29 Finch4 cases or the full historical numerical-discovery archive.

## 2. Exact parent, notation, and checked geometric data

The parent identity is **figure-0378**, declared immutable SHA-256 **df4a24574a48a0ceb04e558fa9a5f21bcd1a1c1f1c9ea5cf9130870c43f94147**. The unchanged12-file core was incorporated at **2026-09-16T03:31:06.357Z**. Its literal source, rather than a complexity-label alias or a different Finch body, supplies the data below. That core closes the exact recovery gap for PRUNE35 and its two named companions, not the complete96-source archive.  

Let P be the raw PRUNE35 halfspace intersection, let g₀ be its **exact uniform filled-volume centroid**, and write Xᵢ=Pᵢ−g₀ for its68 exact raw-lex vertices. Set

    n = (1403/2125, 1596/2125, 0),
    r = 11/25,
    h = 7/20,
    δ = 3/50.

The vector n is exactly unit:1403²+1596²=2125². Two properties hold:

**Central disk.** P−g₀ contains the closed radius-r disk in n⊥, strictly relative to every supporting inequality.

**Old-owner envelope.** For every old vertex Xᵢ, the entire closed ball with centre Xᵢ/2 and radius |Xᵢ|/2 lies strictly inside the slab |n·x|<h.

Both statements reduce to finite rational inequalities. For a raw support N·x≤H, define b=H−N·g₀. Disk containment is certified by

    b>0,
    b² > r² (N·N − (N·n)²).

For an old vertex X, set a=2h−|n·X|. Its owner ball is contained in the slab when

    a>0,
    a² > X·X.

The observed minimum of the second squared-margin family was approximately0.0208309737661261. This decimal is an orientation aid; the executable tests the full rational inequalities, not that rounded minimum.

## 3. New scoped theorem: arbitrary topology and actual-centroid motion

### Statement

Let K be any full-dimensional convex polyhedron satisfying

    P ⊆ K ⊆ {x : |n·(x−g₀)| < h}.

Let c=g(K) be K's actual uniform filled-volume centroid, and put d=c−g₀. If

    |projection onto n⊥ of d| + |n·d| < r−h = 9/100,

then **K has at least two strict stable equilibria about c**.

In particular, the conclusion holds whenever

    |g(K)−g₀| ≤ 3/50,

because √2·3/50<9/100, equivalently2(3/50)²<(9/100)².

There is no graph restriction, no bound on the number of added vertices, and no assumption that the final centre equals g₀. This is global within the stated containment-and-centroid family; it is not a global exclusion of monostability or of E≤310.

### Proof

Work about the actual centre c, and let Q=(K−c)° be the polar polyhedron. Since K has positive uniform volume, c is interior to K and Q is bounded.

For any y∈Q with n·y=0, containment of the old disk gives

    (r−|d⊥|)|y| ≤ 1,

where d⊥ is the projection of d onto n⊥. Thus every point in the separating section Q∩n⊥ has radius at most1/(r−|d⊥|).

The slab containment gives two points of Q:

    n/(h−n·d),   −n/(h+n·d).

Both have radius at least1/(h+|n·d|). The assumed strict inequality makes each radius strictly larger than the bound on Q∩n⊥.

Maximize squared radius over each closed half of Q cut by n⊥. A maximizing point can be chosen at a vertex of that half-polyhedron. It cannot lie in the separating plane, so it is an original vertex of Q. Call the two chosen vertices q₊ and q₋.

Consider an incident edge from either chosen vertex q to a neighbour z. If z is in the same closed half, maximality and z≠q give

    2q·(z−q)=|z|²−|q|²−|z−q|²<0.

If the edge crosses the separating plane, it contains an interior point of smaller radius than q. The quadratic squared-radius function along that edge therefore has strictly negative derivative at q. Hence the same strict inequality holds for every incident edge.

Each selected vertex is consequently a strict unstable polar vertex, with its complete incident tangent cone checked by those inequalities. Polarity about the **same actual centre c** gives two strict stable physical facets of K. No assertion about the polar body's own mass is used. ∎

### Application to material additions with old owners

A point p, measured relative to g₀, has a strict positive escape to an old vertex X when

    p·(X−p)>0.

Completing the square gives the equivalent condition

    |p−X/2|<|X|/2.

Thus every point having any old vertex as a direct positive-escape owner lies in the certified slab. The convex hull of P and any finite collection of such points also lies there.

Therefore, **adding arbitrarily many direct-to-old-owner points cannot produce an own110 body while keeping the actual centroid within the stated region**. The obstruction is not merely a contradiction among a selected four witnesses or a fixed polar graph. It applies to the union of all68 old owner balls and all finite convex hulls made from them.

A successful continuation must leave at least one explicit assumption: change or remove some old material, move the actual centroid beyond the quantified region, or use added points that require genuinely new-to-new witness links rather than direct ownership by old vertices. This statement does not say which escape route will succeed.

## 4. Exact depth-two gadget: the missing freedom is nonempty

Let q=X₃₄ be the parent root measured from g₀. Its raw vertex is

    (5397195983/886193942750,
     −590034857/708955154200,
     675823713703/708955154200).

The following four **relative** rational points are completely defined by q and n:

    u₊ = 3q/4 + 59n/200,
    v₊ = 3q/8 + 883n/2000,
    u₋ = 3q/4 − 147n/500,
    v₋ = 3q/8 − 883n/2000.

Their raw positions are g₀ plus the displayed vectors. The strict chains are

    v₊ → u₊ → q,
    v₋ → u₋ → q.

The exact checks are

    u₊·(q−u₊)>0,   v₊·(u₊−v₊)>0,
    u₋·(q−u₋)>0,   v₋·(u₋−v₋)>0.

The recorded values were approximately0.000638098436589493,0.000476097551807227,0.000439800071959094,0.000625071325280027, respectively. Moreover,

    n·v₊ ≈ 0.440497497837907 > 11/25,
    −n·v₋ ≈ 0.442502502162093 > 11/25.

Each terminal point is therefore outside the slab containing **every** old-owner ball. Neither terminal point can have a direct positive-escape owner among the old vertices, whereas the new intermediate point supplies one exactly.

This is a finite rational certificate that two-level ownership provides real transverse geometric freedom unavailable to the entire direct-owner family. It is **not an own110 endpoint**. In particular, the displayed reference g₀ is not silently substituted for the centroid of a hull containing these points. No full own-centroid census of such a new hull is claimed in this handoff.

## 5. What this changes for continuation

The earlier small same-graph polar cut remains valid in its own scope. The new result identifies a different, larger obstruction: even wholesale changes of the maximal complex do not help if all added material remains in the old-owner envelope and the actual centroid remains sufficiently close.

The useful next construction is therefore not another direct-owner cloud with a better selected foot residual. A multilevel architecture must put actual exposed material outside that envelope, while simultaneously controlling all first moments and either retaining or explicitly redesigning the complete one-U witness structure. Alternatively, finite replacement or removal of the old disk-bearing material changes the theorem's premise directly.

The two-level gadget proves available geometric capacity, not moment closure or monostability. Those are the unresolved gates. PRUNE35 retains159 true edges of headroom to E310; this theorem does not consume that budget and supplies no new edge-count lower bound. C<32 was not opened as a search region.

## 6. Complete source-and-input regeneration

The unit below contains the **unchanged literal12-file parent core**, reconstructs the parent's exact own centroid and vertices, verifies its published complete-report hash, and then checks every rational ingredient of the new theorem and both depth-two chains. It does not require a journal, a library lookup, an originating sandbox, NumPy, Torch, or a network connection.

Save it as `recover_owner_gate.py` and run:

    python -B -S recover_owner_gate.py

The directory `FINCH5_OWNER_GATE` must initially be absent. Expected terminal marker:

    EXACT_TOPOLOGY_FREE_OLD_OWNER_GATE_AND_DEPTH_TWO_PASS

The program emits the complete rational certificate, raw and relative gadget coordinates, arithmetic bit lengths, and the resulting certificate byte count/SHA-256. That emitted new digest is not presented here as an observed post-recovery execution result. The unchanged core's known identities are15678 encoded characters/SHAfbf363d7a67bd90383f3c68f7fdab1cac8f4ff2bf5aba56b1eab2058ed3b4cc2 and36611 decoded bytes/SHA05782a9ef9d79ff8aa18cd74afa9abba785532909965b4caefb749fe5c14ff42.

```python
from pathlib import Path
from fractions import Fraction as F
import base64, zlib, json, hashlib, sys

if not __debug__:
    raise RuntimeError('Assertions must be enabled')
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

CAPSULE = '''
c-rlKYjfMilJ;NW$$lUygA(o+(r}e5%g5O|wiC&Yy^&d5+$d5aK^}sXCA<9J->16=AVATwlQ+qxwzg6hfk97CPfy=xfPDVp^!-n#CvQ%l9bOfS{D=MzpFjNY)7k0s(b<Xh&(SkO*Yy$o`S3#@PvYsikgFH?F?8+24@s7<S6Mo`$yV!WlF?(!_Ji`tVwy^eO)ZQ0e36gJE@_r8=F>b{FIL-L<LRnckLHUxfCO3KqIng4tPf%OXuDa=HuH=K@m%AJj96^w@r3~ZBQQ1B)eOzVKb`&?0%oyUFE`~Zj(OH<Zg*>;UUw}6fW;&-9TyEBesB!WaK=vL2V=)~gV?jic3{Lwk|n9FyRmNjp6NKg??-76rH-4Wi5ppgohH7S`sRlph`OhL<zO$5&(HUaXPP^srG^_tS?1ZPlj-_cPn^hbY~44VacriEH8#y8^)lNuV#myU%k^wWk4@c<f;95XM2&WO^5Xc_kLNG<3~3mK>l%J@ST_dIwi%>`?Z;yf?|Fum*r{%NahzJFuUpnQc2hex1ISKfTE3Tg<IMB?F<>(p_U!oGz5z|&YK~?`u50OjX82~3Ilg6E#yCwqKXRSK)*aKx;=tCyOWU#?H%NWoF!jV7N0#Sj<H*2hG+eP>O_TK~iB_v=wyG(@#f1}So;M`<I;VRxpv$)+i5id%8Np9yZ(p5S&gk_0@yVNg8fCisHOep@tEo|FF~6lzs@JYYp?Qx+*<M|vT+3}LlnZ@w49#~~n|_Nv8D8M(&Gi^3W;!+k$W`WgW6R3)Ahx0)viz~(nzoxInV+Pw9|VDwm`M~HSP3hRbx(J^Xq<jspZ>JLPTs!RH=Ju(yZRd^(AY#b6W!4hFU@QyjAdq4lKP2nU~DgN95WjGZjxG26eW6KJ62>zmOIvUFaB-%YueU0vt8Xy0w?yzCgd3cY&k#=y|auo9Xp0$M=tc-vl7q4vncRP-|$^@i@vSD;E}bXPj;M*UB`}6Gqn@jjlrx`9|vY+fQ_-`CVJ+k78n{Bew@N~IYE?U<`^WU9#sD!?KM4jXEe)7V&6_Mr7ZOv*NHvbFx@OmW7h+5k#CR3sq4C_XWN));y~3CKTU(oGU7NhzpcHNuG#KZdv(pXEB&=>(cLr4QT}kR;`;j)*VdbAEB6m6Eko?8tnJ)aSoXe^!dm8zzCuYoPcvY6f3w0ugm!euGULQ|$XUS|nL&)D2om2<ve+^LNVt(^kT)mJV%Lh&I7r;sN_}{zOwZs;9#YspYp|~=km2npke6h(5B-Ut6S@zDb<I?VdC*NKF`X<Jk1cqr)N(V3xnV)OqBM!1VP=%sp80JBvV47KOvkYeKQJ=i&LY<~5=ZxA+lnJAjgnv-xPBVBX%y+68H_zQ)#3OoG{&CprMhE#59yBu-s~78+klbsG84Yca~+@$Qev3{gPuATbjfuiJ#*~9vC<$8QaiJq2v*BXl4xvO-_{?~(JX(fKM*&=s}#uepg>=K(0=&w)lYBVj9!9G&ri?a)Z)!X2)eUe5P;@vg0TxL=UL_$vq^%?G;9YE$~cBJn3$*TIPlvrO|ZItiaBLLoMwpyJ7^jH*cIOG3vow(VK}iH42=FlW7sfeqrXs!XyDW1XD?3==jjfQ0}k?Q!(|z$&h#Yl64Q?ZjNy+R2SbnH>ufml0Nln*t;Dk7^q{60qEvev**bzm(=Uhn>0ihHb-29SjS}>oc+|ID4-shsM(QTC4$*)G?`b9&5H8JRD}z8`Oezm^;n`yk@v`m*p6lthBg4g_8>3{izBi_&>pN5Qe0Oa7aQ{)}nVxUhiRr<SMn-1hf#E}lF;_n_$B2E2Bm>3{l4hhvWa!CQ#w@+aJSvL&6Sab!i8^B=8sk6Rw&2&@c${IqA|wxiod7GWA;Lqfp>B^6mYB#q#=7Za5h4oKBgNNbk|o!p<9p*d_O7l(DUyW52rxYz*b*Z{>;voVK$?(eP^@5&?Zm@$Ei3Y3EP!i|<H&|VgjQSi@t)or&$XOgG1Ze81{{PyIAO?5J$Ci6X8=`-xx$uWl><aTz8#o>38AtRi()}5a1klmGTuB(CQ&{u<|7{Y-nceWn&!B=mH1vfHk=^H40sgRg0a?J5+E`WUTPY?6C{>z#ip6Uas(072DD-3HZmGAvapd4+9k1;Vsd+k>X6}jnh*C5prM8)JwOvOUcJ_2qY3{Ur)skU%8d=J=hoVM#0vOln%=gJ;s>l}4^D5}=$af@m_ZHD20{-AP2Jiy5++zLIL~bxQ3gtSrn?2Sd;lQ8vCZu$7Uk`hr}ZqO)@T6`uEwrS85W6S9P}`%M$@B-S(;;Q0S$!dAhQQcqd5u;9Q1JKZD}!eNAqkA#BW(cv?15REbUsGp*gk&^{kpO3xtt9gz{ArCIKe6@L(0WHf2zbUz-yyF(9JxEfKaB5TfmH0Kzg59@C+FngaTm)l>{11*>Zmx-<~jQ*i(o3=M%yd5@8MG*hdhE})ghKi$;eJgE!#MT=!xY8+Y-hx+N&;@h}&X`!|g02RG}SZ!9U01Fv!&v5m6o5w3xu>&1?#A*nq42Yx@{fGvmS`cZoNr=pPTR`*O&W4)+W!aTr_%xb9E9o={!^#=u6k(=70|8kTStQ0i2P>&p#Iyc*#ER`CO~OsfyOnsuBupM@MmZ%jprtd2*sb810Wltnh2UYkKt!9xv#Ln3ScajGwp-2A@?5kz#F4F1!kkf~uh~Y0(dOl4MYXqlvIr0wZQ0vJWw!YAAlNP|Ei={BOs~ddgW8y;?JCM@6Yu?U(xm`Uvos+*qh)1*D|@Oo5NtWyHew&vs9f!#*vWmtQ^P>o@VGuYXk@c6Cax$z<X<=*m={*9AV2~_P%d0Xz*h$R6J6MzZ~A^9V6fQy(DIRk(-q+9hvH25GBHMu=g5c#Kg39m7s$v6m|Pwaw$IQ7mFvSl5e_q8DARY{z+_yeY3nvanfMi~rsea60W0kp1}i>79ZQIY*hvS7Fk=f4m+F?72gguTg9$bjyyMY@Z~KlDh*9$t0}$bOhFk?YL&0I0wjp39(s)5(_(s`*emr8dkfl4ma5eCR<yb<O2X-CDH-i#L(T+&gS12tt#Q^f?i52w}#V{TUmu@gPqBKQ20#c#GaZFt?OV%*(5g{{(WlL`i&j>x13J?@nvd9iaBn06(A}_Y|aNxOJOI)Jwc@9Gut^&n#hgdDo)jWKwWToqKiw7Z*Y1@|K2(ml5K!`39g&@fkJQj0{gwiA468~j3$gG4C(;}$=gl{YM$nwMEo5DEAuHZ*pp!jTwOrf)D1>yr;MS~%HGaQjf$eiPegdwdUqi6&U<uT;I8PN6|OUa<EgvD_cDZc0w6hc=50f~}Ffv2R@Gi4;-F@#=Bz;t9Lig~V2V?h`o0t!So9FZn3FdY#X9tsY^uz5;Ubu!7^I99;D5sJZ@pr7a;atSqxFDS5P3}?Hp2$SP;NBpY65C}VD4g%MZ=gO{#A?R7mIoCCGSzz5_8F7?hu^pf8Au^(k2yS>>TX73$=pG4`@DmA*%V=TsScPcqH7uDf7Ryqj+9Hau4-Q)zUlvSOl5CJ6?P7miPn6EF7^$t6gM>$e2NAggGabfhk_izgFwm5~f$u0wBl7Djff0)pxXP{wW?p4TtIvp$F$&GTQcl(htc)<+;1#oVFpAcef;?qyOeLObMQFxmAUG8@hSGa>&TNQTib|`<mxPKen#O-@)_RMBB3=1(W~59fU_UFm#CBAf8iPF}EtO-*Y;;~XgH5sPi3w~-gikBt1w=J0nk<)S4-yD^W*|7{TUs>0@Qv%SAW()R@~h02+y$%(NHjzX>kI`pmJ#4GnNb0WJ}fp#Bs48BU4F{UG{rj#8ehmkNaC>F6WhYX;TD2T1UWn?86kP9i}3hfK)i$nwtQlT4Qr#p%bBDy1`C!e2FP`US`mEP_gQ1zfEUlxd2EY8T;1nI4#X0G6*Bw4mLE7V8WW2m3uq|5i!FpBSKPH-QEgL%#kCbW$MXchb4=mCNG&`o=^m^+ivc{GS_47U^GYiT8^ZvKndJEeKtcytBcael1jXET#AT@n1V0vY&4hjD=OD}xL(jLSXRw7fJ!SbF6$BWza0o_1oDx-KSXfO{c`spx?Krjo*c4TeB?!p6V+hBGL5G*nS#puginO~jl&3`5u{_pn@)m4Ef<Q=cRBS_1#Q<1HMqo)#OW<rsyeV?yF<0$?V;V9|q$e5~8=pl7{>~@8a&>YgAkDGK;94+YtU=&~GAGKWnx0J7&_N?FCHTg&0Gn-<0RU4&bunf&0zK{nYL#IY_l`i$lC`o_@BoWuDS6N(Rxn%ya?C9VqI82yNz4J8;Hzi>{+~IDCHKT%TjDL@ta)riaG0paFoC#daz_#)5|dcn;M`z2IMCfwscS^JSW(ATv7O~BC*Bizr{E6ZLZCv5?+J$?3!+k#<H@ocDsThK15f|sgJ!Ix0>UCIQzvp{f&^1svW3t>(FF`jyezW}vCClIRE7o&aBX3{Cjkwqn=XOi|Apy)Mwkw(5lFa#aKWc}8Kf2(5i5wut%=Z-F@hltP+*tsz+V~bLq{b_bHsdtndCDescJ&s&IS-ldCH%OmOJ9#pc7)e|Db$91r>;WRpMX^!JZ+a`uEBx*og5=WOWTuT#V=I#@{dJkg<D#Jn0GFOda;h`U8^^L@1aG7wsI1%PCZ&GG!2WGS2^e*5XRm;h3Cm*fx7?U0IXAbxvcJL4i|dGyK%F{<md3aEL5JzWm5|;`;tx$&e@&ydT%m`7Z?3{{3l^u5*~q29}uOv*-tGx&CfBl*Ot5|3V#DL_m=+^8Y8jLMY^t_n}xCp|L0FmBi0tjeUuH4HdHbmhj;J60?1Y8O29FFQMbwGIvp6FpK>MP>U~cEoJjW4-hm<)&jSp09+OoOGFn85vyecK8F-=>8$34srthchzv>420|n!)K&5U(-eG9>gc!<J_WKgFc}tGKKOb&_}`LSnj+K=LIYMShrJqr`HacmBlpCt93}1sJ22?3p?)DX!5@>JLKnn`VFoH}Hx>IR3pB*wd6k&zVr9!P$e<9zW!>;~F|Tm5W>Dr0@(bH!i150S0-GRH!FUqXKtKcIZ<{Zd2TYJ9|3~ZjG*2dWYdu+ISub9scdhI;O4hAamMm_v)m<xDtg;XJhx~0$8~&GB+FHa{S+Xu#<JDr`n$G8&brjFCR#aS$PG07V`Pt2{`s*Ycoj$#B&fk09)7wj}b^hWQ+Sp3Rb_A94?8x>bJ;`F-&LC#vD2SY~X~YSg+(?YEkpx-fBxA4<mO)Q!YaAdK^$v-Y#@1H9^^5Btox*AzJ@*~0C5Ny~!#MhwMc0`9ptY?K5U>GY&pUcfo8tSR_Z=`mKjdoY7??-TUAOE94^j3zY`t3KS!-IfqSikb^LUXQw%$y#)@-`YR?)1rTutZG_4EcH`8vDIR;?GU)#78(nq;d?cs{#p&7*ZP!D3{s#cFyv&CxN<#?yS7U$$1!$JTf{%L+lfoZJ=D1OT!eG&1!g?5hF|(?#BTar-!&Xw;s!)~hHlX3-i87~i#~Sif@6WHDcEs2$j6S=y5mldbYh=3(pEqLnY!f?+v}@-@-Yn`O7H?BAQ|Y#Ohon|Z4|_STBC^~Ve&Dmgi99nWT<E19NQo<L4=h|tHpMaOYk5hlL^J901yB=GW{ZE}&V^#qejrx3;U0+RS~x}HGF3OeAq$U%Qja+fl~C~rk^0g794cyrsW{~`bH<=uJ$cJ!XMdgra`#8a!+12BfliphwX@!ucv)7vHb0qZO()}V29ovr$<=RdwWd0~&<yf`~O9X);h?7v3muiu`XoQ__<`qzJremXusA3=urA7o<m>h+t^KVQFm`uYSDdXp7|@8l;Y!a6jpLkChOBo%8=AFVJPxENuQi+pycf!(cFoB2<;I!~tb^JcMvU@TUx@oW*TNgOV-#XMWD?haf3dH(uUi_hIKJKw%}-t$|<Vnw4~XLkiNh)&c-N6BJ_L21EB$BS$kt>{o~p)qrb8(3tlDDdamNBm|iY`{vGK@~(GC9TitfGp9IFLFp|w3)3-il#|xy_jJ=X|ZVlG(s$RY4;p(Y>`;3r{gKe&)DJ=i_J>O36BFoO|s>hWHy_P2d&0o$ot(>8g34qDb^rml`U6`bd!+XV#zpcJzYSKrXYKn<<z+~-atS}y(YLgD&_vDF5J;3C6y6zT}NO{+S=svMM@(>MUF{WS81u-J$2?xgq#~;1T+~5!k?{<mf#6UWR<86Q}Lvgc~gdXxtK+(RsuH2;H9>T72x*eaz@i9(E;nlh+ymjobO@W<%EW;ND_prESgO}MWRX5oDBkmkz^*%rk9f#i!fO%L?hpjB9bG38Oxx5H(4PbqeZr9omDP@$cMF=t`zZD5HKj=VU9jdAQrtiDli;mVzNkK8-9eUE`W{<Ofrk6bDBXpidaI}O(H9u7Rn_pmTMT(PZ`NAL*UQK3`k_vxJguGco@xQfx9)OO0d|7Y9zcOFpC*X-z>Tmj#ki0=S9&EKTVh5*&HiR7QWbk=NX+nht5*9#y5MUfmowtLPlQP9a4dDn!>4Nfo?_SIC5jtitQ|pGtbYAC~;jQ^W!+kJlz{}8V+}EQ&}R8qSP2bU{*9a7Mz}<UvY<-TG5o<LI{%Sy7h6fy2hfhqgRFwj{XDxch1&kMviL7%P+=iK{u6~SCIi?0tnXt!jVE5Sjd3>xYU?vHZEXHl<g_Ko!Ex~Sq#Nbwpj&+j~BP(t5&34E3x=OT|S*JVYGnf5>}(gG*WME5)~7Ss}*;}hn&5_GFnqhOM(A{+p4cRb*ZV-kXrrdr?zusQLCLr{g4CyVUevz&{aU+j^N-&DJWkT9liS@e{p(t8q!dm(TL<{H0mB=85XmftkXRNy%^{NSweWFq;uQt!%A#cd5h+7m~Q6FqI0W}O&*a&4&SUcnYJ~*VW+L(zka*hJw*RS3Z#N<nvWNqxI*{2&33-spJh3kwYHqEZ1)wL4&@$?4ky_y=!fs=biW8L5|mCC{;(B=C6f=2SC<=-<Dckm)#(nR!zfKhk!tR=*-5swa=n;zK!wpEBOu6vs0I3bI>vY*&lzqiEjk_I+fjRu*>4m7qI9&*Zb2dSACouHveN%fw-^s0RdWo|7w0cb5!AUt!)yVbFf0*hogC~DjS&MpUEj57pb}yap$*rvL*f8@5D|zDamn|G^J@ee9a(?1tl2Hh`e<<-K96QaR?dtpl17wN!&kEcL@Nz}?TCN|sY2QvK*8?Q*dd@t?P{-!WTru8Cp~I!A0B?hyfeigl1(6GcDIhh@{IColXLUnX;>a3u9_6fkHhdObyBw%#~1Bi+CvRLr}Fb0KL_|t78`Iv-B4`Y9uBc6c)%~-w1+h;HSm9g7yJs&kX=aCH4HE0tsLql0s>b<T)gPC<;|S7cHGrE?WgMIDcw|WwzL}-fM<2wWr)VxDD7R_P(luQaav$$exH+|L^wGex7y{~Z*5-Ui?(`)s6Fh{dQ?yEW2v8rj}dUBG;Vi0-^nh*{o0W3QH6=d!lFSD?u9|D36zzPjw@FuM+G^&Jv%*l{p$S9*;~>EaFL~VyNKF&wkalJ3xKDI=C?=5?Iu3(b2Q2ky^Ka-*dC3@aE(Uoz8Em}ZO!)xDhGGUUTr+RMH&MuKAlH16#=b3E_(HVP9c!Mw>4kfkbgqtgn%VdF<?f)J0gNcJVd^0o<+rmLMixPia%bRzS|RFl`o=c9NPdiVh8pqBd0w^OihuW8VK=Y>2|k?k`RvZuwn(;c&ucRC*T!a|9#KN4ik<{!#pNhY2qJpoBU+FiV_tE%CqOH0eaecu7GwFqy()+v0A!VYsDtk=9`%YAM#C~Dqcy+yv9ru2_U6Q!u19rR%ae9JI~3$(7SzQXx<*e&b<#WFj}V$wuEjcT~?eWsg3GZt^`cc;559D9+|*p3NA}88302={FoTleT;(nbd00U^UkE(!yFqU<~(9o+iC08l^3C72P5Q*6~wU+bGaCg!5Q3ihXc+BitzK7Qt7X?<c_sIhYzN_n7WT6o`JXv2AgVECHmwJT`r9N@DYCc2A~8fv0tTUifqXXI~{ZencBs$dx-o2iBRXdTQkjwoI4a_+`x>OJlYM7rLf*avkluAuu~!Y+(3V$IIyqN7a9lZSA;d;>AcrYD`!Iw1tx^pkcBKXgiYZrn#XC>iu=zy@kKkHA~YVYqI9|`OfaU$t!WlDTDt>=3&}tMk?MvAgEV|DExTO?artC-h{0vF4C7u}5{la=Iw;MH@Zw^~Gak{5-wy{f<Q6kD4+m@dtD*q4WT(7{SxEBx{^Dw=y}y_O`<kcw9Lk{~f5nB-)mY-_v6gj@=o)qy3pcn6p<?oY<a14}gE$Te<W9TmDgw&Ijbos%?$)K-isL6~KQDl#e00?v;Qp$*pAzUv2suJPvR<T%@PfHQGx|6|B;2A#p3hB4mxs&6vQy%}VcUlppY%^Cu7qGPl0(EQgdIcO3<-F(Sjg;GWCdCD-a|ZVt3HJzEm^_r(x%-?VyJsH6o(K3OYH>CzuhNcOqOM}C~8Y`t+6gN_3c#D3^V9V8E5w&VdqM&O1~=%zPKJf4$}c6EqQhUgc^)pXHAd0d|5$vdA<q<cf;+O$&)9dZ?#*|om-Zq?%*sWbAC82{=HgvI%npgqH?i%gqzx{(LJMkbkuC>ia9$wID33%_Rk)L2F1VYD1_u5b^L>~?jTzhp?Pq2fYwL&N55P8&YtMZO(1v@o|$|NfX7gfGtKYH{jzvW=uBG1GEL!}5D5)*zj}+CjcU6xuPyK+Yc(NO<gt+nsj#qL4=CGI`9SKLuiJfPW=<#r%CfZGXPMO6TnQLS6Ro*Ct~9t$D?w=!^L<1%f5Zy|3b^Ve5Gf!;>g2u?KT5ktW}_d7;~T9FQ^_7CyB(2<A0bl6G5nd<2B!o8F1ma>qHMbXrXC-i?FSg8S;9Q&bK$Q7E&jcUR@KZ#Hxa@Xa@h^E%YsOzq6${xR8{lyo9wn;{gD8OORZEeYN@cPMUzw^2(5BiR4QYf(x+1BBqin3O)^8262TmTd{rTz-9b+Zsuo2oc&d6<v?5X<DzPFkYi;sE_7Ezp(_E26ax|dZW^l#r0&+Q}a#RDK!d8{Y$#=r~wZD8lw)~A*G1mjz_uDB~-j_p{k}ZK%*e;-)*=UVur+q(}9vs)xK9zFvh&!p?DlDTXvVB0pqjU$gELG(j+@n^ESbbM9qB~HLy<`T@e|&%XZ1m5w<DXuP-n@G~Iyw9C&5tL?{~95^;qbn#t!fHOMx5_UwS_4x+iH4*R<t}M`#b3d!vCFDdaL;V&9(@;V(IQz+b!#Cy^0{gD+Cb8W>S(EE*^5}vaPm5)E>xo^J6E(rs$f(?Dce>mBp#w6h}u?e3s|4Wd2Za{*CaNf@g9Vk+!W56`OhI_TWzZhjv$nhXkT}Fy|Y6I?;tOJcuvMVK2fTTp2@6UFp=O%TrBV8PsOTQ-zeW<%nJ8vJ9^!6kaVpsz?x5L``%*BEM`z`q7?9e-eUIorBIz-L=)RF1NuZji~Jd<)@dNS-&rd>`ac18j#(Co2`58(c`4~IN3fHtXfhs86#_#&Dky~$oRz#^}$QiE=w5$U<mcHEOe*1qQZL)JCeH)VZ5oLd9x~hZ~!6!lEIpk+;!pfB_qIcYoEdk3XLSxBw#>bl_)p3lE04($~e+cA`KA+^xH;K=@WhMi~9&64ak&uK_w;I!L4o|^Fb^Fu!GJmUEI;1PZZv4g9n;(t$y<kK?5ebSfya*>TV?4j1*NX_+Q+EcXe)up?fenIIz%KF})FEtfTd&AlJs$>E!g)n={y_A78yW{pab~=*{Vyv*Q=1&(4mOZE9~#K)Vl&98rAbGczOlcul)MIm9nQg!~c)wR^9FvMr-zA+v&^B}J9K6wpO+fsnU>q%I%tcjUG$)@RiCxJ|pSc&N37WuxeFm1V_<9QWvW1n)e0+U}EaeAvG&rFuzb1%BoRI@}!;A?a?-+bkO%rgQ)`&ry7z=MXbpeFOm(`ulApZ6d4}i&+H(w#U4OfR20Y=w*^>Y)f~H^fyiDuVIH-tIQZBD0RyyM&kC-L-v$XxIKM(5A~sht<a*KKE=W9Htvu9UIsqRm<%nckP2Zk7`2z|m|o_!?T^mw6TRE(+&(T@tadkU*=Rvlr^S?FKdJ!SYR|XRMEH8!-2)<33~e?o*4+yFLSenB6&-GedwQpcNVj__*ZpR{YfXBV1=cTHV{=<ps}OzOT`rKEYSXmPUde9C?X;-nu2v&$z3P(<cm?}QHdc$ni>qB*Zgq*!tAB)qXgC1kvZz91G*e(Q?-!9|z!x#$oGqxxFquk5OEeP2l+$Y0+jXES1N!w;|Ly@=t_ef0#MBd*T8o0I^-@l&$o{R-SphD?6OFS)SEGxIe!mCVnoL#Uyz)cnAzn&K2IRXaIDKNsjxiC8`->igkbi+>+I<}AecEHG3JO#RZPX>;C})cc8uQU)%D=Mc$~Qi?DhW{!NNQgxsg>djmCc64Pxh3Qte4GZy}8?ctoM^U7{?nrUc>ZU!%H91IfB~`m1{5{B61lIy{?t}z8;pcQ|_q{CtlR!Bv>bHRYndX7auR$FDN*wY7KekMfXW)%V8H)oLhB6)v~&<hDg;b1TVVvo>aVfK^p>s2E)G!FIE?QYgp?s96Y1OowhPiQw1Q7%d=GOwlyt{gM+%2uGMicvSvw;!X_kqMI{{42>iJo4mRP|iVSYlO#<^c_!w@D*&vmmCDJx!afx!CH0>j$T~G5(My>zRI-lNd_rmi<o@bX4AG=Cu*E{9o6N_RhJ}9Btjqh4&S~)V+!%}WZ85<!_6$x=OWK=WM_7D+6Yf>DnFIa~U()39v%fVXG*=RQ!BH_Loh)ZD|0@VuH>sfL+kN%N!ct#xBbTzpKqi(w8&Gk_GSnWEcDWq~4(i4!gWG3~f@-8IhcU)1*@#M(_H0>6pUun-kQ=Na8mm!>K=U}O&X}4N@CRfCDeROnrxt-Xu`>2zq)TVW7kst3)%TytCE{EL8qzRhmowc@vtaWRsNFHmo`*QGxB)=yepm7pfQ!;!UH*c$X<0<X?PIk(9+sQI(U|=t%N_KCXkng*tnaH(U+Cm!+U}TzBKkt?{26rIHl1diSKu?mpzR*|Ns`0cdbe0V;6(6Kb5>bu#RU>AXzQcjqA_y;@?S0J2bNKnoV7;0)8L+!~z(Xqq6jqY@f`%~s{B1S}kr!h~Br!x$MfcTy#e*9WOy_UehXA`YZYA_Ixw2TiH<@`TG1`&H_uU@-FhSi%bSa#n9gezLy{TGmFdj`N3@KWsEAepKFhgcn?T65S=@qc%keUm&lJ#AI<}LvD?N{(zgipBwziqpcHuiQ!mgS8?yuPOhKfPaspO%$zLeQr_3TLAfU#Fu-Ks(&yCUGI}>5=3jA?;QSBvT20-Sr5xdTMKcB1l!c=lu?3ibrm#+BZl#1>d9aro_g^kT2Qv-5l9kX(KB{UBSeRm!vF|-8#XhN&m`(kZ-S}6d>tH{_$7d>yTo@?Y#=Z?Y0aFPybStEhs&@Jviy!0~y3n%dZtKB+~5GEB$cxQ5h8w(wl?09?vRJEiP5<y%rb9<v)FreNdXv3A`rHEY@Bs+|jl}6mbs~B~o|^E!!p*f+D8PAT5fRxvJrc8>T~M^Z9c!yXWud@7rJaFJGU&;J<u5=8dl#{>#>RF#Z(kgX~jP_juS$-LP5QH9ryzeEP(jVX3kl-!wqOL2(HVQC?Ed4`>J?w6r?KC2aJkM`3Y!$OTN!4_SREw!_mWdjI@+&7$)T-mLZ<(dzlTCO~Dh8@pOO#j9dZCZGURIxrm$uEMJVYCeeRTov)7Is0nEm{0%`)0T(?v)cu~hRi1OWr#-yyrw-uN|)E{xY%>emxv;PutSic?EPFnfs|Z@*Fprk6Et|rETuLC3frx(E3LR3maHo-5ud#Mr4h3W)6gIMdi$>Nh^E35)0WYcBT(ff#LB9)tgALp6%z(o7MA;>gHKs~+TFo24@<$$GL4%>sz32I>LAzV;YBH9D~j~D(J#?39OQW@(LfF}H|OiQHb>97YR7e&&DK$v=Lhq7FP|Ue^QxFe4|s=IiFEH%Cd}7P4zlb~bw{X{xmMCTpJO<tGpE7eA9nz98n*<X^9Bz}dDh&SJfIbVGCnNqr!VTAhI{4x^xZv}+WCPpRG1DAPI|(umtB>mOtrkJ{b~_drj<!j**PWconMsW(N4py57(ZDTQ9CjU^L>Rr}&$4+9Hiwz2+Rg*Cc4<zna8RbwTTDWn`v)wK5b_zuHa>GgOX*MroApLgj4g741;mLv=8%+2Pl!y@E#*@2J3;V6x}WWfSG?FY<f(qKk|mi>}q<cj~eFJ$;AAvK=;}`Hm>~J%6s1J8oO9y!}Nh;9Joo965c#Xh*`U^LKK$1y>CU_#N|fL;?uL7Mj`+rJ7q-B+;^bbR!H`cVItvt6q*7eacpg5zjXqf2w1tJt*hLi1v2PKJ7k~cKe_vJhfe-5dsw$;8|81fnpa9EFP$+etqwzwR3j!Ugh=v(bDS3WfRsMer*pAoxZmgTb|H6ZgYKw&u;R?X?gLyyr{PC_)d;t-rs+#zBc<^h25WjXJPmE6?IR~UN`HyOHjXC5!Hu}sJ^LDrSnl$5q(5;(6UO4q<BxaUe&Evb?eo-(Z(QkD|So52gUvJ?ljM{RbvcQg9Ul225ZojDHU4jgoWAZ^v6_q`K_5K->vkPG|I5`TJL48(rb|SxP^7+T(~E<kJYXI9mU_D|Nh0_dI68#-TUn|JnHpe84t;2y^hE5yQMsCRH+zW*J}woWj%U698CB@nYh*-EEiMqERs~x>t4zm*2;S-f%r;sPiWCh3Cbv(Dx;}rSh~@Rn06dRd?a2<LlLS}OCKoaEkjmZQ7Gv?M+a>}$h%s-J*9YQQj`_(k0HH`Ihaf@Cvug|m+Lz@kYAmw&b3KZ2`e4_L?s}YZZ;k(Dgl{x2P-gfLRGY0)w=9ffir<4Xp(Z^I{di<aE)8LLdKfF=!y>X@~fg$_<GDOtRr;A-8snOu8+ThkS56ZX0(l1L-&Ll7#l9O$j}w2ga>592Qi$_bxFHILJPo%NDxax8;t;bLJ#(00wQkSDaRh?txc{<f&A7KOgWvjCRuBJTx@1(D<<qUC=$V=Rdjb)D_DIGjRbxhid3-RER~3)+Ki4NXg_xhDr?f&$-Pj7uns25!L^dx#@$^hw7|<N*soNlRw^wkT({a?x2w(_s5ZfMzp^>t-GuP-vR~Hamb-PiF9XU;RM_=-r<O*&FK&mLT-*)I{8;T2R#bke%BF*=l3FjIvNouwcTXv`rY(Cas>^+)M5Qx=cv;mE%aUnXOnq!M<fqsqN$p(pK2t;mS!I2Y6N=A%4?Cc}CnG`0p$yIGq15TZ&(nT`9<d>rR`#B%-eq-x-;YeeH3~7SiK<pU=E``{4@oVI>S}Q%FJKc_)adtcZ;=qzDg~$Ps)nHZnDcSkU97i0$+8Bc%AP{VwjTLJ<?z)1-ZQ;V`~@+5EVj(<_CP)^vFsV)vBDA$!>DG;sjWd_-G|{Bm(2+$xf*T=!}79ryd2JZwGKJsB$z>Rm&_on+&mn_ArCEgG>Ftf<9~$QR36lg%laqx797>N=x&K69`2CIaLUap3QIBFt>zQp;9kw2-14ecU-(LqKfIU}->mR+b|MO!UVXi?{BT+APps7wS<M1=qjcS>rcf{D(>CwJ)%>!SZ`N!1G<nJ4!f<O02j5reAMAa>;rAB%ZxCUw%l**7zc<+?Yn0`=Mb+i`dVgVFq3NsNvOF(6w)J_c%qx(c;(Xa!tIw|{3s#(;I}`e1)j`L2M2ANxR*m9<i$?d}QmGsE0iBWz5q2yz^ML+Z^tW5*pE9BvL3STc9>n%*cp)b6R=^vDZ&gP5nf4N9izJ$r8wyC}wqd9owW}m)yRlFuF27RL`72rfUoVocZ!pw{;25CRpw&YI`cvWT3R3On$gb}<Fc3{i^{nG6_aVB~7Ky;95|DaW5-I#?kkJIB9SY&dN%-K#!ro1alY@GS^xc~j%WiE`_TDB%+(5cipnEqdWO`+Kd{PGRFX`ygx3(%^3hJ8`4OFyMq4BmwiIO)fG_I`vWm^_`2wP9v6oW}Z!3|v=oRqnO_OeTr<nk`B)_jtXWOC*<{4NvCo_ZP9Igrcj4<<>;0I7fH&~e6H71`DBD&8r%O0UhaNs^-61@ig_cS;CKZI;mG-V!pyJiKKhAir(bWEQRHm3BUDC9^4aIMiHf9z+Z#Vul%bU44Zj#OxH7lHex5*LEy+(A?j>Xz~6Cr<+&R<({Lv_4)8lPZ&;{!5n*-aR2<uUNk~I_v1din?O&7Pr`C{=W5t5H*Pj1WmomH0GG0f6Nb$hHa2w#LMtJMzh|#T(Z3Urf7+QQ(yWGPtLCf}>`eQ#-L`?g-BepPH`^_nMy;WGNxG~ze9v}_Kns>7?X;xbMjNI6Xd4b5(wKX@E(BX{ynIt}9^QVbbZ5^F%-?7CWHqnvocx))Ch&@THcq(p|MpJ)NA^x6M*Cl~fl|H(_4E(gKDqxt&)fNeL9tn8D}FPv{)WAL$cx3iSAHQ$jxdtV<}W~1ukZ1jdvu!d)uMr7`)MvXk4+)pk)p3V5h3(xBlSfm`V^pixgeq#j8vLd`$ImC=F{07xtyqVIa|aSYqt29t>h4;d_#!}d8^qS75a{kp329w<eN#;Og>Ym$o!Dgc})6}92dls^#<rBi}`}S2)Ec2)q7ZjRuakkhYM)mY9m`q!VCHIkbM5F_ECiIdf#B@%L#wdOIN?=C4t}bGJ?DbzWZXqdf$r$f68kD%@_K`R*;&X$zh(ISDS}}r(bzLUQWjCeMi1_+M^c4WSO}2Z@xjFQTQ<4_wM}D(vcGQSQ~fmy)X~U5YpaL^Bwi_0|Wb>kX5RV<wLP3QtWRFRX_+D{(<mMu0r~e%i&-e$`yf^J8|VJ>$PxeJEE|=@$$iSztek4M~3+spOlkggmx8{O@k;@lnr9Jx+(*bC=BC9WJ>SDpUM0G$cm9-sjKdjsyVKjkumq_g@;&+BvUV;5#s^;X2_&<kLa=t)0R&--Qst|`?b^lpVem@`ZpSXsiWOzc30EVc0Sd>?>`e_JZXO3fuB5;KBaMx#${J<kE(ALO1r$o|3!{zV@XuKv{rrjtQh!}%;gJWYhxRjE$DM&qA$uvqZ@svOKFToFRt@C<?-%kCHARF9`Ag<A>RFb!-}F-DkLhWL0U(Cqpo-N4gj;D$S$Y)E<vS<x9UJrt)cnws+NW^d1ak{8iq7G$$e^-q?^aOdYy76Q!Dp1N%ooMvJ7@}aC6i_EYkfNd|h7ovAmjt=XK3k^*eOj>u5zrZbdOdw_YnM&u_8ixKd|LpOiLizzijYy((E+^1C9h%N)M<MTi^qHHd8zCGtWDnJcwJzBl1?Yb$R4A)G6Tte@!}RA+i`sFzT8Lp)!ZTmw`@Za<e{vbn6@q$JGc2NR+d@v7Y?^0l^j*ilR$IcTWRiav*+zCM6St`@iDCkpW7;NZ~tQVO{WmK6=1W9|J`!Y?<`D&=a+Ry50U%QruQ^J@1KLDd&_F2=N;BD}w$ta8uUMCt{UOnXI)t-n2_9EyxmmBVi|2@ay}_6R$~ejGLyk0t)eR^q2M86G5)#iGbUx{;i(5W#4bZ?c3JHFwUR5T>IR5a!2vWk*Zc659poK-t*T15$&7N*B5nyK009lK$64U6!#D_OZ5K+;^pMulxzFc3*z~5DAozx&7|1O5JY1Ds}snuS!WK_wbjc20#C`pOX4MCHfOSBsHeBe)hY*3^n+TpPzag?h82w=Z)r{wP&Y0`z3F?kBl&^eO(5kFJ~O64sh?`L!Tw281M7`57x-%I7amSs&@Y^?&;Gd>h@e~BM*Y(r*E^!w^CG6L?6{g7G&_Twe4qA<gGPie6`$=P?aB{yZ_x5`rHZGhUPR8i}X1+eXHUQOlN-_f`0c(9n6gGeY`s3C4pkxGSjb)Kr2G%cZw^5e83pa)l2rJ-vEw1j^t}NcA~A{SAjVG4fTh!P>jrX*B;J(&j(mu9>4$b<?+ANCs=+uJv;yL{LSgBlhe`ht7oIL*RS7<&Q8xy&we>opFB9;`5epHMMEgn2U*T8>Y|CpX1(Ie{{w-V3Hk
'''

stream = ''.join(CAPSULE.split()).encode('ascii')
assert len(stream) == 15678
assert hashlib.sha256(stream).hexdigest() == 'fbf363d7a67bd90383f3c68f7fdab1cac8f4ff2bf5aba56b1eab2058ed3b4cc2'
source_bytes = zlib.decompress(base64.b85decode(stream))
assert len(source_bytes) == 36611
assert hashlib.sha256(source_bytes).hexdigest() == '05782a9ef9d79ff8aa18cd74afa9abba785532909965b4caefb749fe5c14ff42'
sources = json.loads(source_bytes)
assert len(sources) == 12
out = Path('FINCH5_OWNER_GATE')
out.mkdir(exist_ok=False)
for name, text in sources.items():
    p = Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    (out/p).parent.mkdir(parents=True, exist_ok=True)
    (out/p).write_bytes(text.encode('utf-8'))

sys.path.insert(0, str(out.resolve()))
import check_A

raw_bytes = (out/'PRUNE35_EXACT_RAW.json').read_bytes()
assert len(raw_bytes) == 2763
assert hashlib.sha256(raw_bytes).hexdigest() == '33cb84c5f8ed7565b74126eedb67624a84ffd666d7444a6c5308c8dd9e31bbe2'
A = check_A.run(json.loads(raw_bytes))
parent_bytes = json.dumps(A, sort_keys=True, separators=(',', ':')).encode()
assert len(parent_bytes) == 17960
assert hashlib.sha256(parent_bytes).hexdigest() == 'fc2df19d7ee67f33e09b3a9a38f16246ece8cdb89993c2cab1a373bb07057afd'
assert (A['V'], A['E'], A['F']) == (68, 151, 85)
assert A['counts'] == [2, 1, 1] and A['weak'] == [0, 0, 0]
assert A['unstable_vertices'] == [34]
(out/'PARENT_A.json').write_bytes(parent_bytes)

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))
def add(a, b):
    return tuple(x+y for x, y in zip(a, b))
def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))
def scale(s, a):
    return tuple(s*x for x in a)
def encode(v):
    if isinstance(v, F):
        return str(v)
    if isinstance(v, dict):
        return {k: encode(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [encode(x) for x in v]
    return v
def bits(v):
    v = F(v)
    return max(abs(v.numerator).bit_length(), v.denominator.bit_length())

g = tuple(map(F, A['raw_centroid']))
P = [tuple(map(F, row)) for row in A['raw_vertices']]
X = [sub(p, g) for p in P]
n = (F(1403, 2125), F(1596, 2125), F(0))
r, h, delta = F(11, 25), F(7, 20), F(3, 50)
assert dot(n, n) == 1
assert r > h > delta > 0
assert 2*delta*delta < (r-h)**2

disk_records = []
for i, (normal, offset) in enumerate(zip(A['normals'], A['offsets'])):
    N = tuple(map(F, normal))
    b = F(offset)-dot(N, g)
    tangential_squared = dot(N, N)-dot(N, n)**2
    margin = b*b-r*r*tangential_squared
    assert b > 0 and tangential_squared >= 0 and margin > 0
    disk_records.append([i, b, tangential_squared, margin])
assert len(disk_records) == 85

ball_records = []
for i, x in enumerate(X):
    a = 2*h-abs(dot(n, x))
    margin = a*a-dot(x, x)
    assert a > 0 and margin > 0
    ball_records.append([i, a, margin])
assert len(ball_records) == 68

q = X[34]
relays = []
for sign, beta in [(1, F(59, 200)), (-1, F(147, 500))]:
    u = add(scale(F(3, 4), q), scale(sign*beta, n))
    v = add(scale(F(3, 8), q), scale(sign*F(883, 2000), n))
    e1 = dot(u, sub(q, u))
    e2 = dot(v, sub(u, v))
    height = sign*dot(n, v)
    assert e1 > 0 and e2 > 0 and height > r
    # Direct old ownership is impossible for this terminal point.
    assert all(dot(v, sub(x, v)) < 0 for x in X)
    relays.append({
        'sign': sign,
        'relative_points': [u, v],
        'raw_points': [add(g, u), add(g, v)],
        'strict_reference_escapes': [e1, e2],
        'signed_transverse_height': height,
        'relative_coordinate_max_bits': max(bits(t) for p in (u, v) for t in p),
        'raw_coordinate_max_bits': max(bits(t) for p in (add(g,u),add(g,v)) for t in p)
    })

certificate = encode({
    'status': 'EXACT_TOPOLOGY_FREE_OLD_OWNER_GATE_AND_DEPTH_TWO_PASS',
    'parent_raw_sha256': hashlib.sha256(raw_bytes).hexdigest(),
    'parent_full_report_sha256': hashlib.sha256(parent_bytes).hexdigest(),
    'parent_V_E_F': [68,151,85],
    'parent_own_strict': [2,1,1],
    'parent_weak': [0,0,0],
    'parent_actual_filled_volume': F(A['ordinary_volume']),
    'parent_actual_filled_first_moments': tuple(map(F,A['raw_first_moments'])),
    'parent_actual_centroid': g,
    'parent_centroid_max_bits': max(map(bits,g)),
    'unit_normal': n,
    'disk_radius': r,
    'slab_halfwidth': h,
    'sufficient_actual_centroid_displacement_radius': delta,
    'anisotropic_displacement_threshold': r-h,
    'disk_records': disk_records,
    'old_owner_ball_records': ball_records,
    'minimum_disk_squared_margin': min(x[3] for x in disk_records),
    'minimum_owner_ball_squared_margin': min(x[2] for x in ball_records),
    'depth_two_gadgets': relays,
    'new_own110_polyhedron_claimed': False
})
cb = json.dumps(certificate, sort_keys=True, separators=(',', ':')).encode()
(out/'OWNER_GATE_CERT.json').write_bytes(cb)
print(certificate['status'])
print('CERTIFICATE_BYTES_SHA256', len(cb), hashlib.sha256(cb).hexdigest())
print('PARENT_RECONSTRUCTED_OWN211; NO_NEW_OWN110_CENSUS_CLAIMED')
```

## Final status

The delivered advance is a **moving-own-centroid, arbitrary-topology obstruction for the full direct-to-old-owner addition family**, and a complete exact two-level mechanism that leaves its geometric envelope. It identifies a necessary additional freedom without excluding multilevel material, scaffold replacement, large centroid changes, or the unrestricted construction problem. The remaining stable–saddle pair of PRUNE35 has not been eliminated, and no new own110 endpoint or complete new-hull audit is claimed.
