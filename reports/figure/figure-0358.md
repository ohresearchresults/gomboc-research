# figure-0358

AI research report · 2026-09-12 UTC

---

# Clear Atlas 56 — primal-cavity handoff

## 1. Status and evidence boundary

**No new own-volume-centred strict110/weak000 body below C630 is promoted by this handoff.** In particular, neither a fixed-centre calculation nor a numerically favourable ascent path is being substituted for the filled-volume, own-centre equilibrium audit.

The useful continuation is a combination of three concrete mechanisms:

1. A **volume-neutral physical vertex/star coarsening**, with an exact linear formula for its change of first moment. This supplies a different C626 replay candidate, rather than another deletion of raw137 or raw150.
2. A **rational, nonlocal moment-compensation construction** using disjoint primal star slides. It preserves constant density and, when its geometric validity conditions hold, preserves the actual filled volume and all three first moments exactly.
3. A **sharp finite ascent-hop criterion**, followed by a five-parameter, genuinely primal reconstruction of the entire face100 cavity. The criterion explains what a repair must change; the reconstruction provides explicit physical variables with which to change it.

There is an important completion limitation: I do not have a retained, witnessed final A/B receipt for the new replay candidate that I can safely promote in this returned context. The independent checks below are therefore **replay-ready checks, not newly claimed completed checks**. The proposed maximal incidence and equilibrium classification must not be imported into the journal as accepted merely because the generator and assertions are present. The supplementary execution archive is useful for recovering logs, but is not the source authority for the definitions below.

The authoritative starting object remains the literal **COORD_C630_CONDITIONED_GRID6_OWN110**. The journal identifies its raw body, independent reports, actual maximal V180/E315/F137 complex, and own110/weak000 audit. This is not the older GRID6, GRID7, CAP, or BASE object.  The two assigned physical deletions are the separately defined raw137 and raw150 losses; their exact replacement cycles and old/new label distinctions are retained in the journal. 

## 2. A different finite primal coarsening: slide physical114 and remove physical110

All labels in this section are **old physical raw-vertex labels of the canonical parent B report**. They are not H-row labels.

Write the parent points as p_i. The local data are:

- Physical114 has neighbours 95,110,117.
- Its two triangular facets are old17 = [95,117,114] and old136 = [95,114,110].
- Its other incident facet is old71 = [71,73,90,100,103,107,110,114,117,120,109,102,72].
- Old135 is [69,95,110,107].

Let d = p117-p110. Let n135·x=h135 be the outward plane recovered from the first three vertices of old facet135. Define the rational parameter and moved point

    t = (h135-n135·p114)/(n135·d),
    p114_new = p114+t d.

Every other physical point is unchanged. The intended endpoint is the convex hull after omitting old110 and substituting p114_new for old114.

The intended maximal cycle change is completely local:

    remove old facet136;
    replace old facet135 by [69,95,114,107];
    remove old110 from old facet71;
    retain every other cycle, using the moved physical114 wherever it occurs.

Thus old17 changes geometrically even though its cycle labels do not change. Old136 is intended to merge with old135, while old110 becomes a non-extreme point of the new edge107–114. When the explicit maximality gates in the replay pass, the resulting complex is V179/E313/F136, hence C626. These counts are the **specified coarsening to verify**, not a substitute for checking the supporting planes and the true vertex set.

### Exact filled-mass identity

This motion is useful for a reason stronger than a small numerical centroid displacement. Let

    T = conv(p95,p110,p114,p117),
    w = Vol(T) > 0.

The direction d is parallel to the fixed base line110–117. Consequently the oriented tetrahedron volume is unchanged when p114 moves along this direction. Throughout the valid local star-slide interval, including a valid first coarsening contact,

    V_new = V_parent,
    M_new-M_parent = (w/4)(p114_new-p114),
    g_new-g_parent = (w/(4 V_parent))(p114_new-p114).

Here M is the three-component first moment of the **filled three-dimensional body**, not a vertex average or a surface centroid. These identities are exact over the rationals.

The proof is a tetrahedral replacement: the common remainder of the polyhedron does not move, the replacement tetrahedron has the same volume, and the centroid of a tetrahedron is the average of its four vertices. The replay also checks the identities independently by integrating the entire outward-oriented maximal surface.

This is not deletion of support114 or support110. Nor is it an affine image of the parent: one physical point moves, a neighbouring physical point loses extremality, one maximal facet disappears, and a different triangular support changes.

## 3. Exact nonlocal compensation without changing density

The preceding identity gives a practical way to separate geometric repair from mass drift.

Consider another degree-three physical vertex v, incident to one nontriangular facet and two triangles. Let a,b be its two neighbours on the nontriangular facet, and let c be its third neighbour. Put

    d_v = p_b-p_a,
    w_v = Vol(conv(p_c,p_a,p_v,p_b)),
    K_v = (w_v/4)d_v.

Moving p_v to p_v+s_v d_v preserves its star volume and changes the total first moment by exactly s_v K_v, while the local realization remains valid.

Choose three such control vertices whose moved stars have no adjacent moved vertices, and for which the matrix with columns K_1,K_2,K_3 is nonsingular. A primary volume-neutral slide with first-moment change DeltaM can then be compensated by

    [s_1,s_2,s_3]^T = -[K_1 K_2 K_3]^{-1} DeltaM.

Every quantity is rational. The compensated body has exactly the parent's volume and first moment, hence exactly its own centroid. No density weights, point masses, external centre, or unfilled cavities are introduced.

A convenient general proof of additivity uses a fixed interior point in each nontriangular facet and triangulates that facet to its boundary edges. With nonadjacent moved vertices, each boundary triangle has at most one moving vertex. The volume and moment changes therefore add exactly. This also avoids mistaking a triangulation diagonal for a genuine polyhedral edge.

**What this does not establish:** the compensating slides may encounter a convexity boundary or create an equilibrium before the primary slide reaches its desired coarsening. The linear moment solve is not a geometric feasibility certificate. Each proposed compensation must still pass the complete H/V, maximal-incidence, and equilibrium checks. The construction is a usable exact control mechanism, not a claim that an arbitrary three chosen stars repair the full finite endpoint.

An important arithmetic benefit is that the compensation can be computed from local tetrahedron differences. It need not introduce the approximately 31,000-bit parent centroid into the control coordinates merely to preserve that centroid.

## 4. A sharp obstruction to repairing a missing ascent hop

Let the centre be g, and write a=p-g and b=q-g for two fixed boundary vertices. An intermediate point x, with y=x-g, gives a strict two-edge ascent p→x→q exactly when

    a·y > |a|^2,
    y·b > |y|^2.

The second condition is the open ball

    |y-b/2|^2 < |b|^2/4.

The maximum of a·y on its closure is

    (a·b+|a||b|)/2.

Therefore a strict two-hop replacement exists somewhere in Euclidean three-space if and only if

    a·b + sqrt(|a|^2 |b|^2) > 2|a|^2.

This is already stronger than a test on a chosen facet plane or a chosen affine chart. Define A=|a|^2, B=|b|^2, C=a·b and D=2A-C. When D≥0, the exact rational test is simply

    AB > D^2.

If AB≤D^2, no motion of the single intermediate point can repair that two-hop route while keeping both boundary points and the centre fixed. Equality is a limiting non-strict case, not an accepted strict repair.

For the assigned cavities, the immediately relevant boundary tests are old132→old150 for removal of old137, and old137→old151 for removal of old150. The replay emits these rational tests from the literal parent. Their output, rather than the earlier affine-search failures, is the appropriate finite certificate.

### More than two hops

For nonzero radial vectors r_0,...,r_n, every strict ascent step implies

    R_{i+1} cos(theta_i) > R_i,

where R_i=|r_i| and theta_i is the angle between successive radial directions. Let theta be the angle between r_0 and r_n. The spherical triangle inequality and convexity of log(sec) give

    R_n/R_0 > sec(theta/n)^n.

Conversely, when this strict inequality holds and theta/n<pi/2, an abstract n-hop chain exists: use equal angular increments theta/n and a geometric progression of radii. Thus the criterion is necessary and sufficient for an unconstrained ascent chain with those endpoints. It is not sufficient for realizing a convex polyhedron with a prescribed surrounding complex.

The same statement applies inside a fixed affine facet plane after replacing g by its orthogonal projection g_F onto that plane. The normal component contributes zero to every edge dot product in the plane.

### A constructive target on actual facet100

A useful larger window is

    132 → 137 → 149 → 150 → 151 → 153 → 154.

Both boundary vertices132 and154 lie on old facet100. For a proposed shorter in-plane chain, put

    a=p132-g_F,  b=p154-g_F,
    A=a·a, B=b·b, C=a·b.

The exact four-hop construction, when its strict budget test passes, is:

    q=(B/A)^(1/8),  phi=angle(a,b)/4,
    u=a/sqrt(A),
    v=(b/sqrt(B)-cos(4phi)u)/sin(4phi),
    x_k=g_F+sqrt(A) q^k (cos(kphi)u+sin(kphi)v),  k=1,2,3.

All roots are the positive real roots and the angle is the principal angle in (0,pi). This is a complete isolated-algebraic definition. Every ascent dot product equals

    A q^(2k) (q cos(phi)-1),

so there is one scalar strictness test.

For near-unity eta=B/A, the comparison can also be made without evaluating trigonometric functions. Under the explicitly checked branch conditions 1<eta<16, put alpha=eta^(1/4), the positive root. Four-hop feasibility is equivalent to

    C/A > alpha^2-8alpha+8.

Rational isolation of alpha immediately yields an exact certificate. For three hops, under the corresponding principal-branch conditions, the comparison is

    C/A > 4-3 eta^(1/3).

These tests distinguish a genuine lack of radial ascent budget from a failure of a particular surrounding-facet realization. Passing them does **not** permit one to ignore the surrounding facets, the filled moments, or the actual edge count.

## 5. A finite five-parameter primal realization of the whole face100 cavity

The following family changes the actual surrounding escape architecture. It is not a global affine or projective transform.

Use rational parameters a,b,c,d,e and define

    x137 = p132+a(p137-p132),
    x153 = p154+b(p153-p154),
    x115 = p115+c(p115-p113),
    x121 = p121+d(p124-p121),
    x126 = p126+e(p129-p126).

Let A81 be the plane through x115,x121,x137 and A80 the plane through x121,x126,x153. Define x151 as the intersection of A81, A80, and the original plane100. All other physical points are unchanged. Omit old149 and old150.

The changed cycles are exactly

    old44  -> [113,127,132,137,115],
    old81  -> [115,137,151,121],
    old100 -> [132,154,153,151,137],
    remove old99.

All other cycles retain their old labels and use the moved coordinates where applicable. In particular, old80 remains [121,151,153,126] but changes its plane.

The exterior motions are chosen to preserve the other nontriangular planes: x115 stays on the intersection of old44 and old75, x121 on the intersection of old74 and old75, and x126 on the intersection of old69 and old74. The first and last cavity joints stay respectively on the old44/100 and old69/100 intersection lines.

When the strict convexity and maximality gates pass, this is a V178/E312/F136 complex, C624, with four intended ascent edges132–137–151–153–154. At one special parameter tuple it reduces to the already known H99 deletion. That special tuple is only a seed: nonzero physical changes of the joints and exterior anchors are the content of this family. **No own110 parameter tuple is claimed here.**

This family and the hop-budget criterion together give a sharply scoped next problem: realize a shorter ascent chain while allowing the outer anchors115,121,126 to move, then correct the actual filled moments. Repeatedly moving only the original bad root, or treating a tiny centroid shift as the whole defect, misses these coupled constraints.

## 6. Complete source-only recovery

The parent capsule below is the unchanged six-source canonical capsule. After whitespace removal it has 11470 ASCII characters and SHA-256

    ea9b28fc11df79a4f1cfa3e941c2364e8fbda0224dd2453f1f22d1f0796a41e7

Its decoded JSON source map has 27500 bytes and SHA-256

    e9ef5aafee7bbb3f8ab9b2cd8fc39314dde6777cfc0b4cb74934703d295442f9

The canonical GENERATOR.json hash is

    bad64d9593ae98974ec61c52f5443f3423644879709449d5fffd7d80770fb428

and canonical parent RAW and report hashes are respectively

    5145c2ef79fd6da41e14ff5128a60ba6e41ddf6d609ca678c6a7c4c45efde278
    6821e70113afe77353106fe876180836f2bc3638fa7cd02a72a669152a054828

Save the following text as PARENT.b85:

```text
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;A?9mmR$fnh=k-)ll92gT^B#F{iFnoBscK@U`CbUScuJ82TLO(kcMHzPtA9**Y}h0=8|!B
S70$LW`a(cWJu2R()fg_0QrbfJ>*eH74ag|rlKu0RNV7}x~7Gy<x#}5lNxNyBy$xKFQSHU4STdSKS`GZe)G4p-QJO+q}zA)zE!TD
G4bF+|1gu&C2rTpJ};SsGJ|tYpBuOgmu5E|jkdm?LULqLf0F|!;7>GcG2t?BP_$!u_l#lL=4R$aw0K4}^Tfc>sAQ|)&tSr+Hlkxs
t>?uj(bw(65LyqdvTyH%qgmimp<XoDmVtVz=RtA$Wr$tPM0E7YW*>+id?|jaC*|MgLEWa~&YjN|W6sF6qfTz1RpL=1%jICb-r#N)
*L{ZH_V1RIv2xZ>!c+n&XDSqz8i!EO0f{b!<JNq$xB-Rq6Bd!x{Cx4Z%_5<mjVS@GIMKi|X9DtWDZUfVP%_=*lYvIgI2R=t&YcY+
y{sQarBJ>O0daxcZ3Gj5eFjy=pQ5nIvI@)GF-uxAKW9=$guBg%Y<rT}e!zws`E{hz;%4fmuF-v1(oPAt>!xYCtI)zFIYZ6_<%Z{v
O6*-F^1gZW0DXe%dm%<^JUZ}&VlOF6F2*U;gkh1OS`lsA))1i?4@n2WoJqT-`h=_IX00!0_|pu9h1t63WmU**WeW@_V%TKph{_Ns
8mqfqIaWCn60X?v-Q70fA_9HN$;rP=yyn{K0n0h4yJ3<{<KiU-E(LF5+M%o!676&5gt4dTi79I(gOA_87HVxoWf9NHCBwl4>zVCO
z3AgmGERalZ1Zg7P0jlV=SjUhG!-TqB>rFjk2sh~?Wrl+w7ds){0Jy#6<pc<N+>s%(DvRp#C;w$AYm6meB9!<Ug(M6ARMMOVsZ0l
5!rcI67-A@QoCvx!YLOMN)O3hbXu*#sLXeFV=`)qkUFhwMu^H#gGA%h#?Ooj;7n%lRm;nBK@2yisG<0*8d`s9;SoCYBtXnh$s#ou
!Y_(iq+1-OqZ)lER9ohdVgj|V)_}J6oJ<x?dqGTarSZD7evwdDg!{=ADBaM74ygQYAMcG)S(htz_y%1^g&Vc`9613Qdb%N)PD~Gt
mvcVMa6U96Cuf5O@b+}h!z*ff!a#EPmvzxdSI%ycPyA%OpE}MIpekzJ6xqb(Oo?%NCEIZvZ`(2+V>zxnmqLz%s7sqE9pS`-D>2pR
k{RDiVfB?f;8m#QQ-;&y4_Qk=bOFdXlR9;k$t{1AVLYY-gokIhpxX#D8R>xY!x<U{^-qI*jcvxxQnlxc0Q4IH0Waeuhx!_4#IRTC
_2?bx`c%V!o4)y)R9KVH7;|lTbfkxSncn`I+Z4uT*kXKr_i&MX3%CB}t<9nxN^!c<YePcco-l<Obo%IHAhsh&B~nTwbiUPImX^W2
0x-Kg1QQ1BI8b^A@|IdaI}Kx_ec$*35sDO{{~bjcA3C%n*HO+ruA;vnNMlB}#<RK+BI^=zR;`dPA@1Dk{(;LQ79o+U%|FB(o4s3~
Hf*6i{jv<#qCtt<%B_Bge8y{Uhxl>DG+rOQBiPu(K)6Vo?Y^g1)(2xFVsi9W_;tHU+}jL#Z(bw_%Y6?W3ok-C5w%4&Vv#8An-A|6
*^)tzwQI9<<CyI#z_IBNTxYUvuUtM8RPw`y1{iS{hc_ThpfQ2duLewgg)g=WCI_bZevM|L=0L!I4B&dUtKH%nCL8n^iDsv(<f87q
;z^=OU_(07lI5p^SS!{;U05iQa|AnnTQW=hGI}bbqP6jc0;<qYg~ps=Hb?R(*3xR=<zZz0@F+L?O1H3oI#RT6vmic!r;irH%d^Dx
?lgb~e1$|PAuw*?(TA@A*iw8zC*BQU%wu`n8NO3<C1K=Ytw#N{#Ex9sj?g#JdTLKTKo*~(t#y8c;X6722bQgEt@ET77Q^Ig76OPc
^r5c$Jnf#Oz`@P)ZxQuDHy__f8aCu~F%G{xtyO6#w1aq*qRp--Iy~wGyH}YFecYUS+3=SotJjDq4i40o3JI;M5WR;Q$m&$o>a$D=
POEBq$uIt3E53dKvrPF!d*j2K_N_>4T5mXDzLdVwDk$YSaUJd8F6L52=H^O~!$(TrV`O<jOz0lz>IH}6Y@V_xso=XIFy2h|TfnMP
0xUDG7Jb;cruM5CZ~Kpwb6oH+ZHa+U%EcfW+Qd+URvZ3;Z-b^c+QC&mZzJ7?5Wjn2Me;4J!3_$zEYniSbG>LCYPJp?SXA#%pZECt
x5dXKCG#JtRXGxR^73F&pSK7F%NC+Ot&)H)MhuULEeRBCxN2Q_Ev$(};g2?Rl}EZ%U*$`to&_{iM^z_50yj$Q2jq!|HS*#L2K1lf
Q=_2z(yZumTO9T)3FN7At`%v+wC;osiO)66tkKf)W5Ex#cD<-7K=e*x+kS@SYu-U8%;6r%9^<Rn8|fJYlSIf^W_*ta`y;1DQwqRF
gA$K>nK{!1<NFUUyF2XdYLY&&UOL#2!fA5kK1|eYL$%|*Er(#4d3xT4#$yW-QNH-0biquOjnk=(>Bnn40obiT0hbgtVZe#ZA+$X1
rHX7Fc87XXGJXd%T-6=)AFm;z&zIqD>+J#ox|6IZ)b=vJ_$Eh7-_?3>Q)0t_vF16&bX2z~C4)YK!=?~}UV>`t|5*dYuBL#Q;%-I<
_DX_vqB103{wpR(mH9o%ssz-~!LAum;yk_9eWpB$Zcpn}#r)RvB%4G&1r8xIxYp&RhCQo=*w`-3ifnX4{w%Yr$H4dcl=$y~Lp+c5
38RP+*xmMS@K92NdL-R#jtDw=Tid3fSRI|v;YKe|e;*oQaT$O-Smiq0?&Qe+q+4t3LE`@H)A$|hT~0?%zHu4)l7<p%dF0p;y^c|f
f_DT{k=#WoxGf^V8%vF`XYhzoEH;SaGfdJE7(w%0P(Dn|v=6WrNSQ7yz0$GU9$uvX8sX2#vY-$UpL`k*@;yP=#W}Q6BjW^a@lq3!
fk(%4jFjm2{o)|gc#)uSuu>KDPEUidvQI*9RG9%6Yn7{{Pc0|${e}xjIQnIb5x>aqkqu+z>@v&)Y*v%wI?|KFWXL7OadrO)&0vs(
%uR-YxTqVJD`SDkbdb}G4Z<3IqtENBL}SN%pd20_0hb+Kg^cmIpOvP;N@z*y%;&goAx$HDW05P(+MrDiM7o%P8I_9yf-#!qJ;`HT
*#aAS5{*Mp$F32QQMq%&6SZ`zHD5g@;Qy3msMypr{10b+`o^xZHy=|&a&(Tzs(KH%h)%AnjX8<q@i>~@3dIC3BEO?G$rbHU0Z)of
^~@#;=$zt@>W8B&J1rO(KJ-WM(K+qImJ-?B(XwaL%rqU-m%sfTq5C6n$;~yOT`<Z<@3fsA>kPk_ju80`UVc&Zc7KHa#SBJk^P-8{
lKs!2F5v}|5mEyT&c@OhQhW7-o(z+gRw^tmj^`A3;Cv5-=lE^iJg5_%)}U>UfQCEF$gLwcNqN_}_z}mQUuLtG3gu*!Vq(s_-}o;p
vIcFRi`aFt@r%8$T<+UfNIlb~k`D>v-xCfjoShc-%^Cn1LgdG2H=Ji$kX?<Lbu(JKF#68wsrE1*fvOvrv`KVkgfr-+z|R*TQ)(`2
JpdpKtfGz;1}7k{_mXDhQs16y3Xzd(nOs6XmxVWWa;Q{69Z00lV>0$xHK#g}v?8O}Nxo#dyQnqtI1=%;GqBa2r81J{ym(D8cD)iF
3YyS=1x=N;&aOllj_K9;ySGHO+|`r{)RD?vyQeB8=$b;Oin`Ljzh6V|1=P+dg5A2@5a7#Ux-Oxq-T)JFTL_Z~Vx7yEWnF30@vtNQ
EAg=xa#!;QpQMv}8$lkZ;e*<%*eS5i^mN)=tLWjC-Th;!ddO*InfmY@fd?**U~CNK*}dz_#&<fSfx=cdZB&rlO*IIvu^dt@(!_cO
AKKm3IT3Fy-pp?E)K`DEPU_d-YA<y(2dDM{J7PBss1S|DtC!40jiMNUaCA&~@j0pA_R=ULlhlyaL`=7vIz+wYhqsMsFjax(F%q2A
+H&;<RA{8y2!j4oA%QvYp`Eo+Dv31sp94j1#~k-$%p-?`p@rQyDC0q%tu;R^2a|k=dmPC<$b1e4$gI~YxlpvhilW!bjz2T%3x>c)
-kHpzdYabyu$Q~=6m6yo3D6S$^g@(Wvt}|-a~GHEl&3#whQ|G|6Uhwx$JWX(Y-OO!>MMiIlqOipUtb$I1FA`dY`sJ{mB)lPIw=|<
0K()btsn~#vLJ&zN~AWhpIUTX*z!cP!v%%~gbHoX*RhC=(wA^V+x!Vu1;W3Mfqwh-3mKA6LQD!q2FSc~zN?-XVCKliT6uQsk;UGn
5&x!>z7v?GBD%~B-bC37BZOp<OM8blz$K*+IdOMNqVw1wer;sG1pf<?{IUQJ2bdH;0WQ6g)}?Iax$cVg9<1gOH+Y(}Bqz|VvnAK_
aqhkB9|HSYdFu9RH0O%Bd2*?EkjW$jjDOrMVm5n-;l)xUrNNb~5AGt}LgfVhlfjK#h(xG<pSAY-IWSmOb8Sq|LixzO|NO5Cv`|rG
Xub&A$uKUf!4KB$vb|8i7$DWz(;u!!qnHR{di;px95RQ@4H|r2z=5<flWwZbR0Q_1+zHh=$(BWYiqjRLAJX<o>VNKZRq1;~%+bT0
N#<uzv%}jVT8qP+>0=O`3roQ-0XlrgAB_t@Er*FbyU#htM7>9csd1bUzppG(en+5`ob7(%c4a0i!qFVr(9(^XZfte4h~8}LUwgP$
8-X)L@RwFxk0!9-y!wL9(KwVkA!f+m@DsNbeU&B(7JvycMm;mp#ZXFq@XSS%ci>SfNqB2|{EO6%q2YJB)h_JGF+lD_dgx>d*P}_x
AitGJMRw|wU!2`_%J`-w;-7ST_*Sar+Q>sO1>ld~9T@r6wZUyqw9~cKri*&h6N(IlSs`a|eoGD$UwfVHQ9rT~2AZQO*Ad6lVoz`N
Ha#I=BHZD_EqwDTUn!P9S%gtqil0$%J;0*N$TmfmG=JCBKo)K-i7Z+st25bK_Lk;^`6S)RaiCe*)Iubc(P)<gma3(#6F-E|!#8pL
IE41we(b#h5|Uc5l&unl#**xV;%zjlP~>D5drDVw@q-*3N|IiiwiO!?hE5l-PW;m$59C5kG!>!~lcFt~9-}H3<l%l_*k$EmQe1qx
w}$}KgQ0_bv=YihILLp2mv;>J@i`mbpX7~>Il)AZA~_RPw$jhBFRd6BMykb7C)Q@<e8kELH2{WQg<$5dXN}iD#gsU+y5{?-21ShV
C;Vc6S|YC7L?jYTv9LCNXZEvXj;>i@gOxamBp&-rPH4I;-ws>=WT$ZZkyoaj0nonFAvr{l2I%GeM`s*B`wCY^Nbpz8I0`EbjVMPQ
k@Wiq&bQpzOtJ4EjE0Av0ZJKm4>|;CBjqQ`UdiyWk2+_fPf`~C6JIHG6L^th0u8Az4L_mnRwPmGCAu6nZc;{vSf!MZN=4ZMQm<F=
QOAV`G1P+5ee|+tV*5hB$Xe%?TB2b}XA?xnFUU+MN4-fHkd{`*(54;6T&5@c)L|%Q<+FmUz!1pd6NrAC#qUaJhO&@tkkmk5e%P-5
zjDi?d{J0?11eBVkGIvXl15<0U=`k7nrI{J7Q)2{0nqQnAo!EL2OIN^OC^c<M6jl?rf<?6{-RS=Ks7jU8m)ioyR%M}us3#tEiU!6
U*x9QNL2Dy&2T5CWpeXV4O$Tt8dBH;`i&htvx3pKN<Ir*<^Fmd2ty8bbAg3W9<oVZI9hqWEsrs}*!sY((NUUL#wXqdUF)T6!!CVB
@LW?pG#Ez`FmAQp0NvsjrSF;LDlP7%uYdi`#(Vo=giV%!r<>u0y!Zo?t1Xt8ZJn*1FO%r$N|KL`p9+6rUd&ZZvK6SgpKWIh@GXxo
mg~muai=RnR4TghM)X0N$4^IvrjnhM-xPH9XM(9|1To-%L_Jm5yQGB)EV})Mt3s+n(SUV1Gv`yn0io<XS_b5<LZ;F9IgKQp^)j4y
Qj+_!Pn4G0PZ*Tcg_!ACk$b>I1C)lxz=%3kLa}a;;O!tK6OCowt?fD+O~y&Fg38}YaQZkBj>x}6bj5RnZ14Tpkcw?PxI)*GU_SFb
2w9a<$CNHCRC5cCDM4RIIr9#2bMnkGom_Qww7@wCQpitbv>&yI6r|fduMl9iDPPfr@wJOsIQYH|&Q$wkLyofcdzG4k+KLK-qIcpR
<)IQvqk-~QHP{h-o<6Ve@4+XDe!~SC=`E@}{aCZwCJS>0i&^^x$X$13(nkd(bjiAXyfl!CH5N9<SbJf!%-ZHkWsSQCp(E|dBv(K_
e{^+%ZZ*-QlUjdK7|AB~F6Zd*=I$XkCA*puWK4Gm+P)f~hwVjsZU-E6brI~Y_@E%ot}9h*>T;f7p!PR_ksJ8vtREBFb1h2G$RVgY
BF-Jv+owIRFjKQWt{?ac+)GHo<xqmVSf+^o{Znh|os7gsDig1Bv~xlmb49{f*>>^1^cw&|jw)xBY)q)qj7sEZS|;W1@*9AG51AYT
iKqyDgNaE_)+4=Mbx)y4botFmZ^lYyQr*kY>uU6Jkm(A=^NS$$TVVCJAMA*1x!L@!o7Ry|3Ug+WFBK8d?xf@(1i$WM%npm3Vmi|T
U4IO;;*r-N%9kOWVSnzK-)l0MxUihlZzJK<ST1<FNnf`YaFQmDM7BtEcr~kJyS^`;SPZ?-31$r7PpK|F_RBmpHCOoAFA}3KPZ4Tx
`#V45W$iGuVzg;Xy^Kck%L#ZXivK^frvXSUO!$;Cw*w6%0+x8an6flWG_xd2nqT&FEAG8lQ6^hC#tsWe>TrVI+e>y;jAEe);L2+8
UatFNa-Tpa9b5}vy-T0S7S;0Ctw!*UNNuOP_CLOx2C1PHIS99IOx>O?u+Y7=P1B5ja}ppE=UAH%1;D|Xgb!*Sm@vp>kGY{C`x{xX
WxSyKdpTPBJu7fI*k=i4N-l)(&<{|>;~r?)!1*SQf-0*>tlRynW!v(Xr)&YJmCpFumk2RaH*_zs>%m=j&wsRw%u0)Od%=u0sx7Mh
IINt0u-=(&=hrTT;Ud{Kw!sn)1&NjsFk5rWx<8^Qga)*+iy0Uqx%FzK5w5iW7JDUZbd%t#Ut<=UAWP4Hbb(})-=HpKdG^1@YBwCx
)Qg#=rw1oDYlKba+gNvM2TJcku$d-ETz_B>f;cLE@Rl-e%$%_GMN@U(C`3g=Kw-Ix18o)4RqF&cJVU-jeMs9587O)g;V1ls*0Vlg
-%Hcc>&~q?*3`S{jCr4Ru-{sTT{z#1lj0!D&od4-`~2DJmQG|<iYKYNP#BH(wpf4kI-XaA*kY)60I;}=_=G0~<Kr$XqOk0nsMD9}
R~xWE(~tV8p1<{}sS`oJ6!w29{1Q;^KZAGIbQ9Q~ie0$8C+_&d=1Sv8ndXXE-m;qFeE^SlKX>#LSrS@IrQ4;^Vuo)a^GuyrP;uS0
nM%^!9~C3~Fpx@)vs+ExOawfgCWu&7Kz>bDchmmkmt<&~DVfo19r}BLCNt|&z{iwXKN-^u`GkE9orJm!_HvR+@tj2o``Z&yB01}Y
H9QqZn<SlL;HbV22Xu6d@@7P~Mt>7Gohx8)d-jGY{w88gx8Y(dC1*FJCCJ5<Lu25acQWRX-;EraGj>O{xsLa8n+Sxd8%%z4xJ(>q
Jn$UrblT%)V-fqC*Y7qTK5d(OPv096IUYcA*!N)pYYF6K2s6K?S+68VV8H)f)Ww$y%XS-c!3uJ9tI|L+aH60M%6Wm-K#TKwr9I*u
E3NXF<5yV+;&txfNAXs%epnx2NZ{HFhZZU|z%KiQ3w`7-?L1TiqHdxz1N0&pFuI6<+JUongJmiTS_7%^7*rrk{^I530}9<QsN{IL
V%nYojg8z7X(6Rqz7buY2b^bg!+F(VB)e;mBO7Rt9M(U^FHDrzJ!&IM5F(+`<f$;fy(G_oLc%QO+<tN*O-znh6(k+WUAK47(OlFS
58DHJbg2_Or0?I$pw9M;L^Yz=cdh`4k@%?&(-$kmQ4Cm&=Vrp~%}!NCku;7k3gsS=7nB}1ER*dzML^j2+w!?aUc={y1Aqqm4B^$E
UKq!=bFQw}pp3$M!40Ueu0Uuv-7nVIzq@WDbGdbjdq)$|A!=S!aJ6DU!~5QV8QN0m<Nx22_~s>jOYJ(yq$S>YmLSk$J{Hc5LE(G-
75g4y0`$^_`Sgv^%S#Mps-DR}YG5vN45<e@Y)T_A7I(fuJf<Pnn<;L^Woyf#o2Bp??_L5pSh=N<8BUT^o6wX{+j$_*KQO`v-h1wy
CvaRFTJv|KOY_6T<i03;@sE1G(rsGGhHjF5XW+2mx@cf1q%WQG8x82L`mFc_O{q|NUH&^F8E8^Y|B=7-M#MQ4^C|rpT(pjWKdXqw
?R9gOj&v8&589HmhKB;Z-#7M{^N`4KoIa^Ar)-Qdlu&S=bai>P8qqNKR(aP5OKMyFqTG$FzyIxxa5(L>3p<Q++l^Z4!n&`rV7)0H
qP+jxpsbrj-FCom<K;?9*S<++Mx$4)V&oSP$I$n{2d<97jW0m}Aa#`?USIw&G8UO~7`7H*)|2-B9jIq&2njic%)q|akcx2jUlIqe
Od9viZ}QONRDNXY@h}2f#c#!Mes*$uet2O%=g@C!SiQZX^?--eAw^FtuDB|BQO+Bt<oeXZd<>`A`I;dp-zOzg2v_R%o`M<N*_{KG
&amU;oJQ6cBHy@DQmAnzlc|=bJa5|nVr(bmByIQuU#!G@$7jl_PEHpgEooahrt^>T+)(U@M{^sUs8A=~VEzr_&G0w^5-9|(1nR#G
DNFReC}DtPkS4y;^79cMus>qN)rxY%Cp|gLH5D%Mf`VoAqGyHPn3KcQMLDZ(=mTuR!+2u@FK0Xs*Eq!7N34Ln1*<qqMFBk?Fh!v%
H)l&7`v^PxzObU|+=Ypz*g9!eoa)enAhfT?Xn@T9$qR1yU6kJGSeFd}O|RL&Y+ZG>%&mZX1+wvw(+7RoSR76&<TVCz8;FkwRTkvz
Ia%r|az&%jS79UQ?eNMp(aoN4K!eko7!PU2LlSl=dB1F7Y&`%VKa51xF|ZHU*+)Csqinz0nOjYAq=VFJ=<FJzZ9=@tJ`pLOmMqeK
thNFaAd3jG>55cLp$#-(ux9-s`Fx@)0w>MrL0)bl)MpIyMmb{#1c>n;nG;T;##~qa^uk3Dr}GqOSL9<9Wmk*!y2|MEx%0OAMPEA3
wot64+?`R39TOHGn$8lm2$^3e*Io&keH(RSuB#7i4*Ry-AIiG+1W7L{`Rc&`;j0rBvSLEjwAU{3=#r`fYb>e8$wr6DJLKK+!S1^q
<iLcC!=2;4AR&&QsLCy5l|iWrLTcDNfl7Rd)a9OVF3q(RKiPXtckfF{o&PcFJ0phC_IZX|7W}KKH61K#R*qf7vsdb*Z~>m!v~T>|
VQ-uRsRXLAE?3k>Ot=BmKa>4%&#?SdoO@UX&tiMb`s?KYEqB`z<|3$$zie&5qrBm1({s6O1Z$}YB*c`Hr`3)6#<24JOA*~rcJA}R
l*SXBtBhW8d?IT~X_|o4?gZ(zgL|6BDVZ0D_%0}A-4cmG_P8(e^nL!Usmb5=EMrWgj{=shXFJ)nc0Kkgd9G*12W5GSOVYZujXE9W
S+QYCL~vWmoR}J?cJX^>6RLv-@3fqxD|}{xdpKkUWf;f-?=}MKuP$3r#i8ZP0;hi&MM?{sQ+qUnXEkJcM4^Myz&*H!NU+B_joAS=
x>97hw)sM$n?S4c|5jW4uG@actcmeyg9;vmd51gjW~)rN;GZFL1Gxo9h*HNC%TTGERXj5W*V*7y8>x#3K1MS(?B*c%O8@gAP+5F2
1U?qjhTjX^taJ((tc#7G5p%`ei$j26Qg9t!{q(<EV{XM>)%Rb*fjO<s^ONxvw3F>HeNptC#2ZdK1pBFeDNr9o=^%qFaCh+K3NWKB
PVkZRXJ#uAWbajtUPy;c>WIIdtQ{{;KD*}?j&gs(<Wuy#6Kk=uu*PG$e!9=1NH8sSt`|dm^P249cso354?BXwjOe}m32&&mt^36e
R~j+>E?g2^AVrLSF~~(msw@nSKvQfc)+qFFgs$TLnqg)al9se&H>f96tHc|tl$V^hj4`>+2e!)HMOVx5Dd6{?`=T*m;q2sQDclJ~
CwGj)h0^q{V2;7Jvpp9CQxU@8MnM5uejXTRR^XoA6K4pia{!L`5fdSF(w;*>J#(5d(IMLa$ix%NzgCp4yIw-=7QxQnr{+h?;@|5N
v8Ym602hl(@*(1noS05$Ofz;*09g}Zq%37~y5x<L5SEQ2)HkYyx(*sF@G#)Ii#d^{ScNBJ07DIdTxa|YZX;4UyP79t1^|Ylz2vG@
;B{B@XqTJRD6~Sft~6irr%{k#??6-ce5=5J&*7`RIKY?{kMm^mR`LrZ>ZXNnF8|^ud3NO4RlWBf)S1)XKuiHAYw}(Iz0}>ub@i$_
8j&0GMh7v=q=7C>>c9`K&GcVqNu|0~%>p9oqRSW%V*O3eJN}AW_5-AaT8$<{E$34+5rZ&0mj(i=nU72iky0m~C<G_EJwGX;X88m0
D4FvaCKvIGTB=I+u%Fn`M)d|m!K4;mjzWp9wM7h_O{}#c(tHc0ikn3`Gm(A%7;(_ReQsJN8m$xG#?elh8^-$+AEq^*AbFm|-;}4|
s6&~4_XkKh1oiB})h&sq401o~<th#og)R8dTYx&?ZEk(1MVXgx$(^zx{O|khDL&A1?D}Qq_n@SMv=maIst}4(>|EFTd@+3I$?^tS
uwmh2W^FzqZXnEyrI7>KNmwo)bZEZMx4=03LrxEXNs|dR$jIm%LFaexIVxN2NN)pbR_vUH$~NG~LR>K-a!|kj0BOuEx?y04*aZUi
4Vdt?Cs7S8Qs+gX7T3oQAHH}r%;W60=h56P62(t|jx-TbGJSG6pzU2P^q-Rwv6K8%qY(*qL9U|b;Um5cEIyAk-V@F!EN>=L_)$!A
P*LdXG!A>@mJka-^Z~8DAjtY=@eq$?=%<sk_b0fQ8_r?3U~eb5SfRGxj35bSV=dSJS(~9&Hbzr5Cz-{>Q*#bCS}EC+#=ktUuS-U`
R7n@ksPZ!UzHA#V5*_PUb9R+OwMwbbK@~Ykx7<Esj0y!Guk^6<xO)iwF%;EbV%<gyP1NRGl~UaGW3Nn}s22Of=)9t!l>L&-6{rB<
#vw;U;aq0O_?OM$vpN!p%0|vs1dM=P>n6rM5eM@-L50H7wp*r2LFb+QmhBM4(Pm*S?Tz9j&#xaW69t2-NE>RmH=g0fHlY?{*`6bC
OU(R{N6VAc*jZZYzU3;^ozHoWygBh#3CU~;Z33sR9mUreG~_|dG&pD{>d%hlP=IKO)sJB8k!%7LYZPc?u>}nEeI^#sU~;qzB8?mw
jg{LWOYs2!!&d|u+Rzd?l=pUVN-%!#ki4rH;P7K0jJeBdaR?{KXy0&<L|okr)hXnWu~Z%?Zi;J@;_4Lbdp2J&$LoM$-nXy>A|D16
0@v=+UI{!|sX{ToY8JuebD-?RMcGx6cd)QP5Ze5KqbdQ1%cIEng{*qo4OMW$uQ8KyL7*G@n7J$&w;3G5iJb<PComKkx0&3=Nzlqh
l?fCKkQC}(BkfX+C+ICZHYpnyRjE@A@NEp?Uifn%2gNl={}zVPpuVhZdWzFd*X(PEJ*2#y5i?*bu*pB&dv7&CA9TDV{O63#XIVU^
L77Czr$drwS<tP$cLDq6oc|2GvIOm44AnrM1zNRK_e74ccZp4e?;AsxdM#V9x(D2SA)YwTVcc~MiRQs=zr#lmiN#0|bcLOrH9MsM
JVL}ZD!))Dhi&&edgZAka*^H3WdHyGU$cMJ_^Y6800FW`?A8GQxnweOvBYQl0ssI200dcD
```

Decode with this complete standard-library program:

```python
from pathlib import Path
import base64, hashlib, json, lzma
s = ''.join(Path('PARENT.b85').read_text().split())
assert len(s) == 11470
assert hashlib.sha256(s.encode()).hexdigest() == 'ea9b28fc11df79a4f1cfa3e941c2364e8fbda0224dd2453f1f22d1f0796a41e7'
b = lzma.decompress(base64.b85decode(s))
assert len(b) == 27500
assert hashlib.sha256(b).hexdigest() == 'e9ef5aafee7bbb3f8ab9b2cd8fc39314dde6777cfc0b4cb74934703d295442f9'
for name, source in json.loads(b).items():
    Path(name).write_bytes(source.encode('utf-8'))
```

Save the following complete new source as ATLAS56_REPLAY.py. It uses the independent auditors and centred integrator included in the literal parent capsule; no numerical hull, SciPy, old generated report, or unlisted helper is required.

```python
from fractions import Fraction as F
from pathlib import Path
from math import gcd, lcm
import argparse, hashlib, json, sys
import RECONSTRUCT, check_A, check_B, centred_mass

sys.set_int_max_str_digits(0)
PARENT_REPORT = '6821e70113afe77353106fe876180836f2bc3638fa7cd02a72a669152a054828'

def enc(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':')).encode()

def sha(x):
    return hashlib.sha256(x).hexdigest()

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def add(a, b):
    return [x+y for x, y in zip(a, b)]

def sub(a, b):
    return [x-y for x, y in zip(a, b)]

def mul(t, a):
    return [t*x for x in a]

def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]

def det(a, b, c):
    return dot(a, cross(b, c))

def plane(a, b, c):
    n = cross(sub(b, a), sub(c, a))
    h = dot(n, a)
    assert h > 0
    return n, h

def solve3(rows, rhs):
    a, b, c = rows
    D = det(a, b, c)
    assert D != 0
    return mul(F(1, 1)/D,
               add(add(mul(rhs[0], cross(b, c)),
                       mul(rhs[1], cross(c, a))),
                   mul(rhs[2], cross(a, b))))

def mass(P, faces):
    V = F(0)
    M = [F(0), F(0), F(0)]
    for cy in faces:
        for j in range(1, len(cy)-1):
            a, b, c = [P[i] for i in (cy[0], cy[j], cy[j+1])]
            D = det(a, b, c)
            assert D > 0
            V += D/6
            M = add(M, mul(D/24, add(add(a, b), c)))
    assert V > 0
    return V, M

def raw_from_cycles(P, faces):
    used = sorted({i for cy in faces for i in cy})
    rows = []
    for cy in faces:
        n, h = plane(*(P[i] for i in cy[:3]))
        assert all(dot(n, P[i]) <= h for i in used)
        assert set(cy) == {i for i in used if dot(n, P[i]) == h}
        values = n + [h]
        D = lcm(*(v.denominator for v in values))
        row = [int(D*v) for v in values]
        G = gcd(*row)
        rows.append([v//G for v in row])
    assert len(set(map(tuple, rows))) == len(rows)
    return {'H': rows}, used

def star114(P0, faces0):
    P = [p[:] for p in P0]
    direction = sub(P[117], P[110])
    n, h = plane(*(P[i] for i in faces0[135][:3]))
    denominator = dot(n, direction)
    assert denominator != 0
    t = (h-dot(n, P[114]))/denominator
    P[114] = add(P[114], mul(t, direction))
    faces = []
    for f, cy0 in enumerate(faces0):
        if f == 136:
            continue
        cy = cy0[:]
        if f == 135:
            cy = [69, 95, 114, 107]
        elif f == 71:
            cy = [i for i in cy if i != 110]
        faces.append(cy)
    assert len(faces) == 136
    assert all(110 not in cy for cy in faces)
    V0, M0 = mass(P0, faces0)
    V1, M1 = mass(P, faces)
    w = abs(det(sub(P0[110], P0[95]),
                sub(P0[114], P0[95]),
                sub(P0[117], P0[95])))/6
    assert w > 0
    assert V0 == V1
    assert sub(M1, M0) == mul(w/4, sub(P[114], P0[114]))
    return P, faces, {'mode': 'star114', 't': str(t),
                      'tetrahedron_volume': str(w),
                      'removed_physical_vertices': [110]}

def cavity5(P0, faces0, pars):
    a, b, c, d, e = pars
    P = [p[:] for p in P0]
    P[137] = add(P0[132], mul(a, sub(P0[137], P0[132])))
    P[153] = add(P0[154], mul(b, sub(P0[153], P0[154])))
    P[115] = add(P0[115], mul(c, sub(P0[115], P0[113])))
    P[121] = add(P0[121], mul(d, sub(P0[124], P0[121])))
    P[126] = add(P0[126], mul(e, sub(P0[129], P0[126])))
    n100, h100 = plane(*(P0[i] for i in faces0[100][:3]))
    n81, h81 = plane(P[115], P[121], P[137])
    n80, h80 = plane(P[121], P[126], P[153])
    P[151] = solve3([n100, n81, n80], [h100, h81, h80])
    faces = []
    for f, cy0 in enumerate(faces0):
        if f == 99:
            continue
        cy = cy0[:]
        if f == 44:
            cy = [113, 127, 132, 137, 115]
        elif f == 81:
            cy = [115, 137, 151, 121]
        elif f == 100:
            cy = [132, 154, 153, 151, 137]
        faces.append(cy)
    assert len(faces) == 136
    assert all(149 not in cy and 150 not in cy for cy in faces)
    return P, faces, {'mode': 'cavity5',
                      'parameters': list(map(str, pars)),
                      'removed_physical_vertices': [149, 150]}

def two_hop(P, g, i, j):
    a, b = sub(P[i], g), sub(P[j], g)
    A, B, C = dot(a, a), dot(b, b), dot(a, b)
    D = 2*A-C
    K = A*B-D*D
    # The integer enclosure is exact, not a floating sign test.
    scale = 10**18
    floor_K = (K.numerator*scale)//K.denominator
    return {'endpoints': [i, j], 'D_nonnegative': D >= 0,
            'AB_minus_D2_sign': (K > 0)-(K < 0),
            'AB_minus_D2_scaled_floor': floor_K,
            'enclosure_denominator': scale,
            'strict_two_hop_possible': D < 0 or K > 0}

def fourth_root_interval(x, steps=120):
    assert F(1) < x < F(16)
    lo, hi = F(1), F(2)
    for _ in range(steps):
        mid = (lo+hi)/2
        if mid**4 < x:
            lo = mid
        else:
            hi = mid
    assert lo**4 <= x <= hi**4
    return lo, hi

def plane100_budget(P, faces, g):
    n, h = plane(*(P[i] for i in faces[100][:3]))
    gF = add(g, mul((h-dot(n, g))/dot(n, n), n))
    a, b = sub(P[132], gF), sub(P[154], gF)
    A, B, C = dot(a, a), dot(b, b), dot(a, b)
    eta = B/A
    out = {'endpoints': [132, 154], 'facet': 100,
           'eta': str(eta), 'C_over_A': str(C/A)}
    if F(1) < eta < F(16):
        lo, hi = fourth_root_interval(eta)
        f = lambda t: t*t-8*t+8
        out['four_hop_feasible_certified'] = C/A > f(lo)
        out['four_hop_infeasible_certified'] = C/A <= f(hi)
        out['alpha_interval'] = [str(lo), str(hi)]
    return out

def maxbits(value):
    if isinstance(value, (list, tuple)):
        return max((maxbits(v) for v in value), default=0)
    q = F(value)
    return max(abs(q.numerator).bit_length(), q.denominator.bit_length())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    ap.add_argument('--mode', choices=['star114', 'cavity5'], default='star114')
    ap.add_argument('--params', nargs=5)
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=False)
    generator = json.loads(Path('GENERATOR.json').read_bytes())
    base = check_B.run(RECONSTRUCT.recover(generator))
    assert sha(enc(base)) == PARENT_REPORT
    P0 = [[F(v) for v in p] for p in base['raw_vertices']]
    faces0 = base['faces']
    V0, M0 = mass(P0, faces0)
    g0 = [m/V0 for m in M0]
    if args.mode == 'star114':
        P, faces, definition = star114(P0, faces0)
    else:
        if args.params is None:
            ap.error('cavity5 requires five explicit rational parameters')
        P, faces, definition = cavity5(P0, faces0, list(map(F, args.params)))
    raw, used = raw_from_cycles(P, faces)
    (out/'RAW.json').write_bytes(enc(raw))
    (out/'DEFINITION.json').write_bytes(enc(definition))
    A = check_A.run(raw)
    (out/'A.json').write_bytes(enc(A))
    B = check_B.run(raw)
    (out/'B.json').write_bytes(enc(B))
    assert enc(A) == enc(B)
    actual = {tuple(map(F, p)) for p in B['raw_vertices']}
    expected = {tuple(P[i]) for i in used}
    assert actual == expected
    third = centred_mass.run(B)
    (out/'CENTRED_MASS.json').write_bytes(enc(third))
    VP = [[F(v) for v in p] for p in B['raw_vertices']]
    V, M = mass(VP, B['faces'])
    g = [m/V for m in M]
    assert g == list(map(F, B['raw_centroid']))
    Z = [sub(p, g) for p in VP]
    common = lcm(*(v.denominator for p in Z for v in p))
    old_to_new = {str(i): next(j for j, p in enumerate(VP) if p == P[i])
                  for i in used}
    bounds = {'assigned_two_hop_tests': [two_hop(P0, g0, 132, 150),
                                        two_hop(P0, g0, 137, 151)],
              'plane100_budget': plane100_budget(P0, faces0, g0)}
    (out/'ASCENT_BUDGETS.json').write_bytes(enc(bounds))
    summary = {
        'definition': definition,
        'parent_report_sha256': PARENT_REPORT,
        'source_sha256': sha(Path(__file__).read_bytes()),
        'raw_sha256': sha(enc(raw)),
        'report_sha256': sha(enc(B)),
        'raw_bytes': len(enc(raw)),
        'report_bytes': len(enc(B)),
        'V': len(VP), 'E': len(B['edges']), 'F': len(B['faces']),
        'C': 2*len(B['edges']),
        'strict': B.get('counts'), 'weak': B.get('weak'),
        'ordinary_volume': str(V),
        'first_moments': list(map(str, M)),
        'own_centroid': list(map(str, g)),
        'old_to_new_physical_labels': old_to_new,
        'max_fraction_bits': {
            'H': maxbits(raw['H']), 'raw_vertices': maxbits(VP),
            'volume': maxbits(V), 'first_moments': maxbits(M),
            'centroid': maxbits(g), 'centred_vertices': maxbits(Z),
            'common_centred_denominator': common.bit_length()},
        'completed_checks': ['A', 'B', 'A_equals_B',
                             'expected_primal_vertex_set',
                             'independent_centred_mass',
                             'own_filled_mass_reintegration']}
    (out/'RECEIPT.json').write_bytes(enc(summary))
    print(enc(summary).decode(), flush=True)

if __name__ == '__main__':
    main()
```

### Commands and acceptance rule

The exact replay uses only the Python standard library plus the six literal source files. Run without optimization; assertions are part of the certificate:

```text
python -B -S REPLAY.py --out canonical-parent-replay
python -B -S ATLAS56_REPLAY.py --out atlas56-star114-replay
```

For an explicitly chosen five-parameter cavity point:

```text
python -B -S ATLAS56_REPLAY.py --mode cavity5 --params a b c d e --out cavity-replay
```

Here a,b,c,d,e must be literal rational strings, for example numerator/denominator; no five-parameter endpoint is designated as successful in this handoff.

The new receipt is deliberately generated only after both independent audits, their exact equality, the expected physical vertex-set check, the third centred integration, and a separate filled-mass reintegration complete. It records the actual maximal V/E/F, full exact volume and moments, actual own centroid, physical-label map, fraction bit complexity, and hashes. The complete A/B reports retain the full face/vertex/edge and weak-equilibrium census. **A generated receipt must be read before promoting any candidate.** In particular, an exception at a maximality gate is a failed realization, not permission to retain the intended edge count.

## 7. Scoped nonwinners and continuation

The canonical journal already rules out treating the unchanged single-deletion screens as a new result, and it records the finite protected affine/projective nonwinners for the two assigned losses. Those results are not global impossibility statements.  The earlier unfinished high-dimensional numerical iterates likewise do not supply an exact successor and should not be revived from rounded coordinates without their original literal controls.

The new distinction is between three different obstacles: insufficient ascent budget with fixed boundary points; failure of a particular surrounding-facet realization despite sufficient abstract budget; and filled-mass drift after a geometrically successful realization. The hop criterion, five-parameter cavity, and rational moment handles address these separately.

The most useful next execution is to obtain the star114 receipt, evaluate the exact boundary-hop predicates, and then work on the face100 cavity with its exterior anchors allowed to move. A successful fixed-centre cavity should next receive an exact filled-moment correction and a complete own-centre audit. It should not be called own110 before that final step.

Supplementary execution files, which are not a substitute for the literal definitions above: primal-cavity work archive (`atlas56_primal_cavity_handoff.zip`).

No global minimum, exclusion of unrestricted geometry, or new accepted C<630 record is asserted.
