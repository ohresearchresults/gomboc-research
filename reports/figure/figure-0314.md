# figure-0314

AI research report · 2026-09-05 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# NH13-NO575-R1213: a new rational 1,213-vertex Gömböc

## Result and scope

**A new fully verified endpoint has (V,E,F)=(1213,3630,2419), strict own-volume-centred (S,U,H)=(1,1,0), and C=7260. C<1000 is not achieved.** These are actual true-edge and maximal-face counts. This reduces C by a factor 3.596694214876033 relative to the parent P50-4355’s C26112, and by 110.7807162534435 relative to the inherited C804268 body. The parent counts and source/body distinctions agree with the immutable payload; I found no mathematical conflict requiring a substituted parent.

The parent is figure-0311, SHA256 2e32e75e0d7968fe4238ef9c894ddf1cb491de3e42947626a34f91a761492173. P50, G50, P50-4355, G50-8287, the new curved source P575, and the new finite body NH13-NO575-R1213 are distinct objects.

This direction did **not** start by contracting the parent4355 table. It generated a new normal-offset point family from the polynomial source, used actual-centroid-aware completion and redesigned critical collars, then simplified that new mesh. The final body is entirely rational. Its complete literal coordinates, triangles, exact ordinary-centroid calculation and an executable standard-library verifier are embedded below; the archive is supplementary.

## 1. Source conditioning and the new finite construction

### An exactly centred source P575

Use the parent’s P50 polynomials, but change the amplitude to e=23/400:

```
f(t) = [1,-241163387/28875000,644213/125000,
        127043/6250,-106768/3125,44096/3125]
g(t) = [1740161/500000,-533263/125000,-1007773/31250,
        1493996/15625,-1627536/15625,135632/3125]
```

These are ascending power coefficients. Put c(z)=e(f(z²),z g(z²)) and

`K={ (x,y,z): -1<=z<=1, |(x,y)-c(z)|²<=1-z² }`.

P575 has exact ordinary volume4π/3 and centroid0. The horizontal moment identity is `sum_k 4 f_k/((2k+1)(2k+3))=0`; the other two moments vanish by the half-turn. Its only equilibria are S=(-377/400,0,0) and U=(423/400,0,0).

Here is a reconstruction of the new source certificate. With derivatives in t, define

```
H=f²+t g²; J=(1-t)H; L=-J'-2/5;
Kc=(1-t)^3[(2f'+4t f'')²+t(6g'+4t g'')²].
```

Exact positive Bernstein coefficients certify H-1/2, 25-H, L, L²-e²J(H')² and (483/500)²-e²Kc. Their complete interval partitions are:

```
H-1/2: [0,1/2],[1/2,1]
25-H: [0,1]
L: [0,1/8],[1/8,1/4],[1/4,1/2],[1/2,3/4],[3/4,1]
L²-e²J(H')²: [0,1/4],[1/4,1/2],[1/2,3/4],[3/4,1]
curvature: [0,1/8],[1/8,1/4],[1/4,1/2],[1/2,1]
```

For p(t)=sum p_k t^k on[a,b], form `q_j=(b-a)^j sum_{k>=j} p_k binom(k,j) a^(k-j)` and Bernstein coefficients `β_i=sum_{j<=i} q_j binom(i,j)/binom(n,j)`. All are strictly positive using Fraction arithmetic. The actual replay ends EXACT_P575_SOURCE_PASS.

Thus |c''|(1-z²)^(3/2)<483/500, and every horizontal directional support has strictly negative second derivative. The angularly stationary squared-radius profiles are `1+e²H±2e sqrt(J)`; the L inequalities make the plus profile strictly decrease and the minus profile strictly increase away from z=0. H>0 excludes pole equilibria. This proves source convexity, exact volume centring and its two equilibria, rather than a sampled screen.

### Normal-offset coordinates, not an assumed convex-offset theorem

Let X(n) be the P575 support point for unit normal n. The new coordinate proposal is

`Y(n)=X(n)-(1/2)n`.

The identity Y×n=X×n motivates this conditioning: subtracting a normal component changes radial distances without changing this tangential numerator. **I do not assert that the entire image Y is a regular convex inner-parallel body at offset1/2, nor transfer the parent’s unactuated gap certificate to it.** Its support optimization can encounter competing branches. Every final convexity and mixed-normal-cone assertion instead comes from the exact finite certificate below.

The numerical generation used80 C2-paired Fibonacci normal samples; source e=23/400; offset1/2; initial cap8; and critical cut/apex increments both1/250. The raw stable plane is x=-877/2000 and the raw apex is (1123/2000,0,0). Cap proposals solve Y_x(n)=-877/2000 with `n=(-sqrt(1-r²),r cosθ,r sinθ)`. Support/ascent completion uses directions measured from the **current actual volume centroid**, not a fixed construction origin. Entire ascent paths connect to retained witnesses or the apex.

A branch-aware support search used30000 paired normal seeds, then a two-dimensional tangent-chart SLSQP maximization of d·Y(n), constrained by the cut plane. This is proposal generation, not a global-optimization proof. The ordinary finite centroid was recomputed after every hull change. It produced2695 actual vertices passing the floating class screen. C2 deletion removed683 vertex pairs, yielding1329;57 paired edge contractions yielded1215; one final paired deletion yielded1213. The raw coordinates were then rounded to multiples of10^-7, and the **new** exact centroid and complete exact hull/class were recomputed. No continuum certificate for these numerical search paths is claimed.

The literal packet below removes dependence on SciPy, optimizer convergence, floating rounding conventions, missing masks and source regeneration. It is the authoritative coordinate generator for the accepted body.

## 2. Exact rational definition and physical centring

Decode raw integer rows I_i and oriented triangles F below. Let

```
D = 10000000
V6 = 2936986753449982560844
M24 = (-56752729877257941979637814,0,0)
C0 = 5873973506899965121688
B0 = (-28376364938628970989818907,0,0)
Q = 58739735068999651216880000000
```

The exact vertices are `v_i=(C0*I_i-B0)/Q`, with Q=D*C0.

V6 is literally `sum det(I_i,I_j,I_k)` and M24 is literally `sum det(I_i,I_j,I_k)*(I_i+I_j+I_k)`, over the supplied oriented triangles. Hence volume=V6/(6D³), approximately0.4894977922416638. The raw ordinary centroid is

`gamma=-28376364938628970989818907/58739735068999651216880000000`

on the x-axis. This is the unique root of the **linear** centring equation `4 D V6 gamma-M24_x=0`. Subtracting this computed centroid is only coordinate normalization; the mechanical centre is not chosen independently of the homogeneous body. The verifier independently reintegrates all three centred first moments and obtains exactly zero. There is no density alteration, nonzero parent bump parameter or quadratic-root ambiguity.

The primitive signs remain unchanged throughout `(gamma-10^-6,gamma+10^-6)` for the reference-centre x coordinate. The common strict primitive-sign chamber contains gamma between

```
-69918379/142975000000
and
-2564638902550719287/5353638012638865000000.
```

This is a sufficient sign chamber, not a claimed maximal class-preserving interval. Its proof uses16942 exact affine guards:2422 radial face-plane guards and four guards per true edge. For raw I and normal N, the guards are `a-D*x*b`, with `(a,b)` equal to `(N·I_i,N_x)`, `(I_i·(I_j-I_i),(I_j-I_i)_x)`, or `(N·(I_i×I_j),N·(e_x×(I_j-I_i)))`. Exact comparison proves `|C0*a-B0_x*b|>C0*D*|b|/10^6` for every guard. This supplies an actual mechanical neighbourhood of the exact centring root instead of assuming centring preserves the chamber.

### Critical features and global conditions

The stable hexagon has canonical boundary cycle[0,3,4,5,2,1]. Its raw rows, in index order0..5, are

```
(-4385000,-869668,-1771623)
(-4385000,-688191,-2451964)
(-4385000,-193975,-2394995)
(-4385000,193975,2394995)
(-4385000,688191,2451964)
(-4385000,869668,1771623)
```

Vertex1212 is the unique unstable vertex, raw row(5615000,0,0), with eight true neighbours. The centred stable and unstable x coordinates are respectively

```
-25728997462817718087612061093 / Q
 33010737606181933129267938907 / Q.
```

The centred inradius is approximately0.4380169136376714; maximum radius approximately0.5619830863623286; r/R≈0.7794129828228812. The stable plane is **exactly the unique minimum-distance supporting plane**, and the apex is **exactly the unique maximum-radius vertex**. Both global conditions are explicitly checked. The old near-roundness exclusion does not apply; this is not a proof that E<500 is feasible in this coordinate pool.

## 3. Exhaustive acceptance evidence

The table has2422 outward triangles and3633 triangulated edges. Exactly three diagonals are coplanar; they triangulate the hexagon. All other maximal facets are triangles, giving1213 vertices,3630 true edges and2419 maximal faces.

Two distinct implementations passed on the same centred rational table. The new standard-library verifier also executed **2934247 exact maximal-plane/vertex support comparisons** and checked that every plane’s zero set is precisely its maximal-face boundary. It checks connected closed oriented sphere topology, every vertex link, positive radial determinants, exact hinge convexity, maximal-face cycles and rank-three supporting-normal cones at all1213 vertices. Its ray(5,7,19) lies strictly in exactly triangle1495. The second implementation is the parent’s independent quadratic verifier adapted only to bigint rational CSV, zero moments, constant sign arithmetic and reporting; its geometric/mechanical formulas pass with the different ray(3,11,17). This is software-independent replay within this research, not independent mathematical peer review.

For oriented true edge i→j and incident outward normals N_f,N_g, the full tests are

`p=v_i·(v_j-v_i)`, `q=v_j·(v_i-v_j)`,
`u=N_f·(v_i×v_j)`, `w=N_g·(v_j×v_i)`.

A saddle requires p<0,q<0,u>0,w>0. Stable facets require all boundary sides positive; unstable vertices require all outgoing dots negative. Weak cases detect degeneracies. Every true edge was tested using all four conditions: zero saddles, zero degenerate equilibria and zero primitive true-edge zeros. Absence of saddles is not inferred merely from Euler’s equation.

The full script below was run from a fresh extracted archive, producing SELF_CONTAINED_NH13_NO575_R1213_PASS. The regular tetrahedron fixture gives(4,4,6); six deliberately invalid/nonwinning fixtures are rejected. OBJ and binary STL are materialized and read back for counts; they are display approximations, not the exact definition.

## 4. Failed directions and the next gate

Physical-gradient flow strips with independently chosen longitudinal spacing left transverse hull faces poorly controlled; a representative construction even violated the intended global inball requirement. Tangential mesh optimization reduced numerical residuals without closing all equilibria. Wider critical collars at otherwise fixed parameters caused significant ordinary-centroid shifts and new equilibria. More aggressive normal offsets needed support-branch repair and were often larger. G50’s better unactuated gap was not promoted as a smaller finite construction without evidence. These are algorithmic diagnostics, not global exclusions.

The useful new mechanism is normal-component removal with **actual-centroid-aware finite assembly**, followed by exact rational promotion. P575 is worthwhile here because it produced the smaller finite endpoint, not merely a larger continuum margin. The remaining gate is still an actual E<500 incidence design. The1213-row body supplies a smaller, seven-decimal raw-coordinate starting point for simultaneous moment-feasible strip replacement or reciprocal-height/cavity methods. Further motion must retain the global inball and maximum-radius conditions and recompute the ordinary centroid. The original source radial identity or gap is not an automatic certificate for modified bodies.

No minimality, prize eligibility, manufacturing tolerance or formal proof-assistant certification is claimed.

## 5. Supplemental archive

Exact tables, both verifiers, source certificate, centring interval, construction scripts and logs, display meshes and inline replay (`NH13_NO575_R1213_VERIFIED.zip`).

Complete Markdown handoff (`NH13_NO575_R1213_HANDOFF.md`).

Archive:202218 bytes; SHA256 `aee1bb875537bf029ce40a45ffe38f8d47f02dad87cd7a26525ba12842fb99a3`. All41 manifest entries passed. Canonical raw little-endian int64 hashes:

```
I: 053094d59b4d4e6229ad592d9b50aa2ad54ad001d2b99dd03a040fae79f192c6
F: e9b1d5dd6c9c58e2e1fcf7d24861909b2e6be64b1bd5f9d8bdc9d348aef97e79
```

## 6. Complete literal reconstruction and exact proof replay

Save the following block as a Python file and run `python3 -S`. It contains the entire coordinate and triangle dataset:606 half-turn representatives and one axial point. Vertices and oriented triangles are reconstructed in canonical lexicographic order. No optimizer, numerical hull, source file, external package or prior sandbox is required.

```python
# Complete exact geometry and standard-library proof replay. Python 3 only.
PAYLOAD = """
c-p0R2V7Lg_J7W~cXu!AiVH3T6cntWs9@BnQKQBZ6H81q(ImzgV~UCKMPJ_2l;5LE@4boi4k99D=^g3P1*CUr(nQLCE{Fm#@ALBc-`z7ackbLXGv9O0cg{U}
P+dbaxSp<|VNg2X)1H3qHO+sH1W?5lP;Z4{1K_hy91jr}!X*7Vu}2q@y|Em__z_q7`8i9PWrt4$pxde8rNtk`I6&9Yu6J5LHJazA)ZYPptAg~wO^~MrsXFNN
dF1wR+2J9Gxe0dbY?hQSj<1G1dk{}R&)VS#NVcL3mZkEWqhZ*Xvbom&1jdIrZvV*sYJ~1_K?^r<knTGY?gS1uP`uU4iz;2DdoZk$HZg;|Owixbyrp=(ofhL_
4;Js)#iB<&^nC3;#3}wfwTTL^fpB-M&4*S4s!L3Hs5%%?PU}h^P$t2U=s=sD(KM&6(xG$!YR%{#Q>tFpBM_>RsQx8`Baqz+1)5aIAl;J!9><-6=z1H7oNw1o
*#vUj&UamjddH=e4u1^or?r*CC%`=vV&b^v$7}gU52#vaN;3h?V!=zj+?N}qT#$*)HQ+G<R_;{!g&IHXO2pa<$}X95@_}YIh#y7$Fo^oL_yN`2g^_PI%DC%r
e6%=&3LeUCwODEhRk|SF9aazHVyZn4Ba^Tw8B^ma2QiG?L3eumN|ms+o~k@&FiaJFG1x_gd7zh=jz4DQ2=$p*Z-bh~Fm6YA?A9-*JjSV7p=LRhi}D<Cbd0Lf
N3U+M8iv+(%Bls+e|M^;9PFSf5l0KCs{IA$TOWeM0fTf(e6rXW5;MSN2=c1IFBo!+u=x&E><xV(5cZkh1ZuCVDMpVIecn{(5W1{QE&yE(mo5x{3O@ged42c^
HZBNpq!LFU!WD`hLyQ@CEpoA?S|KtMx~wU8Ys%}}^gv8JWRZnFSx{+3)yAXG35!(7<mm6~%*UJnw7J-5OX>ep-xHmNF+|DBiR#P+4_7MY3%B!)^XuKI_)zG3
0$x6pM=^xeV!?ZfA(UG<<*>qlsB43m{|oxiB!LR41B(E(+URz%^*&{AHKYdhmqc8SKjT(_?nW?NOIfr-!5CCkqnjlp4pL(2oCJ&sf-Zg9W^q^?*xW-q1F+Bm
i%$yDsTyCp>ynu!x~D>V09`DtTMIpVwFjW40$W=#s1G8-(V`wq-VgXJq#1ffX)g!L?Fsbw&@Nv!N)_Cvygv6(cKSSr(;Umm`!RA^ObO(ba$<g|JkWoO7SHoC
fX*k7Yy<{lw0;Hp>0v}XgqT9@2(|}cvLmFY(b_*mp3>Lmh`$I^b?JmsUXTU&ZK?MJCqpXlA^KQw9jqaFVSF<T7D1FNSd?H<6;F3<X9wgoP%)aQDbbez?)RZ;
7+lty$T?)7k0U+kO%aqvKgsk&{i{JC+>jhd{;Kw9jTO~cK$*}5ob<bNrxm0}b8ME!?DFCyZqK`>xnNi$Je=cGiH!+VjWtvnQ00lx-+={#pxFy9B~)KDR5@dS
6DAkK;MvA|R7eD6cFg7pjHIGbDuy#%&Y*8Zm7Z@r+^>u6Ms&Ch81zH(u~Ip+JWhHWbjjO1p+|P7H$dd+jUMl&M$mn~+gvDjgw{CP;wBZf%%h$z@}x!+smc#^
?J;q6>z<gS1*#!_9L>#Eug8qR;L@0JNdCR*7S{e+GXX*4kmrvU#@MG^`*G`%@Z+hAOIJG?(lupZv!Ol*QVlU|LyR>RHA8$4<fz2U7aR+ZK>a;LOY<Ar+hPt!
zT2}T*#L@H4E9i(rZ9SH`1Hsj1AnlPwovT(-76ZjFBtrqTm|93B|iY&MMf#0`RRBi74HnC$Gn!At%x*(o@eN#3Bv@NJH%f(rMh587*|QRgJY-1ZEk{2A3DO6
F0hc)e8w}f<BtzuwlSl5YhKPE80ky&)kq}%U}r?zwD3v;<^?%Qh?|(&7%Hrlw#ekTbwK(AU8=|P@j$0L94`Z&T`VV@AJfm#j^&iQ(p3YL%Uui)qOvonct>g^
8eQD6SQ|$>A=3h)(joFLMEw*(NY)6fe)Iar=y{XR^p7_lig+r~Rr<O`z>aKdS<ewSsJ9M-=(0*^PiO$o*a=9D`P{eUv`&w7fL%7^<`zQoxT0;kYF<JsL=0c|
Z#ZR?z91!OY2@%4ZO?fQ8EOw7HDZ8Q3byrpZuI#3ax2~=18oTQsQ}kFepqr3W@qyAd;OrJvkC$-LMW|bg$nx&&~|(PB^5qYluIn-8^|B>j-{NUO`$R?0vkF8
VJIjKB1S$QjTk|lTTN6|TN-5C%m97=eyYt>4BbzH(J0>!8pt-|V;yOGr#37Jy92g&WWpaM)3?g?DbtAML5}+qysDrwd2_yat&4F6UGF?U)~=IwC~T(9wKb{U
gf*jqF_72!7`lw4T-~%eeJ&Q9k}w}mP||{^Y*&u=uo3iDSKwe;FXh{v$|-Qk0Mptih|Eal*rr5L54+qkD(Z*Q$fvZU_5{b~;WJKXQ#Z$KaE#Mx$4N6tq@R+L
tfz`srD??ts-aVC{J2(k!XPBY6MDR>sR^Cc30me{?XVbbgI5lfnN>{b>E7oK_qWpd{S&lyiY`R?HF0cesEO_(j<b_3^u-)ZulMEVY8F!7mTr_+?*R9<mo6{H
+lcq50UzEgpz`udsgmJH&h5g7;1=n?>y2{f_Lq5bd%LxGJuWwR&K^-bZ6nFihB7KsTt>wuM)3MPMUC3tJpcA$swk|23QX|gy5@R-&E5OFdPDT|<TO3arpjH4
DW5@jJYLGnN)hS1cJrKLJ$XjAq9~J^E-KA^fLGP+M?Z^mqElVldG~U~5YU<cY4^H$?FoIn^f;)~)nWXe=rO)gF}&=ySYEH`eah7T9&KZ$$5aoG@We@DJb!yD
Cb7tdsds<?KYTi5$&7ns(?z{ml${ZzX`3>mX6B54To_ZH5Y8mDy7K($Zt@27f|#nVg+@1=n6MVO-yOmX=7ll!Kk64loJS-R-+hk>N{1Uo!Hm9DC^Hfb#<7w*
cW;wO)5e^(cy40|v^8Z@?y>i&Tg^#~pJ@tHc|7>3598+O$AmaTOG6QpIm+`Izt80MjxedZqs%~GA=9VzfUz@%N29SkAKf@!%wB7QTqe~hkBN>M=G6o~<#l&v
GQA-S^&P4ix9bzBqfAij81pnGhlw}2%^3`Ep{oAj{iJ~@4rpW=e{{d7CoW;SJWH7y*-cDhXfxBPF@7$zA{eZqLtw(PnlVVKW+s|CnbhRROqpQ?W6@Z_gq-p=
$z_V`bD1Q=UZ$tImkIw+tP+20;6X2wscQ>igH^nO!z}?VOzJ=j)B0}Z@}VwIZhwRq*I=L3-dx{4rn#k$nXoaI=+jgPDC%b1c7!P2%xYkUY@~wh2N;7lv#PWt
#Fp9;H;bM!X1Sx>dbcsS^{ka?4r*guHdKs{GKqm>1dmR}#q}{$x!N{#oGJEQ7$4NZSS;&J=*NcJ#@tp5O^Lwt2Bx;SfoXcy&)C@wFq*F$XEZa$=91ZM{Y-32
Gh;H;%ydK*aBLC^IBlKTJiozg-rewFCh^`d^IbxJ31i)~)T){rGt$Ml@&eO3nCz$yCa|mzZZ`FEhy7a^>(+j{-8YA}_Q+*i{1<t+KV+Jg#<jIEKAloI?Pbi+
n!=&Sy!hl4I;Am*lh@qAnClgB16m77Y?L#Rq2-L0O&epSFUm<NX2uHB8SOqBFf+c*)9duZiM(j2t*oPl!b+K(QpVg#vHeCnV_0I!ZE*9#F@LF?`eeqj-GY;E
BBtsG?lTR(MRcWoA?=uu!?d>Z66={8j;clN4a~r8Ff7hO%iF0?*A`6c2E;Jkndywh$YQe!XR7v259AufQx(bOP;~bWqxZ}0mIx+CZ=O-2#JIN`b3dexQ#~;V
@s6cDL(4JVfW?ty(=4Vs!-na|S{SZ3zu;*NS`|lgd;`nzw%riKMW<1%0oIJ3xR8o-jHXR$8o|ic8IyAi=!8<q=-PTtj8!+MWKfF<9~746bnzTLp7DnBZ*UCE
doe-3o|oG-ugI<o9gN55n`YYd6LA*h(UQq~CQjyLMBG9vONo4)E!y3tj9!%ul~oi=+uT-uG$hFGisEIM_QLH9L)6mFr7Yr8dCqn<++Ne8k>2%a@*thIAM>Kx
jJ>h6#}u3FZE5%3TwZYbJzk?<8Wr0-iUUtqImB7<?uF~{9Q);B5*&C*j{dwLS8tx>6MbG-)9XIgkI_D52*VuWxGlF6=<u{5T8m^BLxDD!p7=#jwHxIVkb%Z=
m0Tn50La($g0uo*Pe3g<SWl@V!J2aRx1t<+L#c;%yD%g&7TtYQslo{_ZeEe7COZZ@B5E+zwHfM7vgo>sHjYoi1l(-Ugd($DA??2OkhKTbD`tU#-7SnybA_y=
aH{Rm+aos)_eBqbN6xjIw{KvTw=u`n=sxF}*7Bg6hujm+TE{8h3($m`M|GSI$1qM^^Zo$emGMoMm{xb*Ku;zzPx@AgDHR_Vixs(%5b|i0lcAN&sZaPw*XEu4
CzpaeV!<FZ9PJ$*QguFRUE`-qbMxtEw%xS8_^f$OIOWn2&8xnZ!EqQZhfb|)PW|opz%qbtv3)zerIt1g6a@S59@k2^4#^~r@^yOVIj6USQDhDHTIX||>XJEa
)}>e@&cGYplCd3v?k<60pS-62{1zi`I{Str{V1ME%N7i|*i(HC22`%KWJ&gaVrs7@`Ocp(nqSt;&rRSPH*tHrB$ABg<>v6?ikX%`=HXM`?IK=UAMLEqORD2q
`_q=r+_a}0!$Qu$ZBB*>r?;EV%B8*U&~e5eGzWX3)d<&L|D%qQkK+tvZ`UYlH7h=O#P<je#XCdKpsC|vc(x98Ke-qCqAZ}I)*M;`hSB`do`B#To)c8WQ(i|G
-@6NQyCTukbzP}<9p;$HnRhHIbit@c%2|#TI1stM$f5yVi!k0qE!x_G8YJ0TkIQe`5u18%zZt4oh)xqmAdX7`y@^r`>oTSs)3*3|?0NFA7CQ%g@wUYR(~KPS
%W<NbY@c9jI{A1TIDFIK4vKB!u))`n8jViC*2J^k?R99K@JUQWDLRFJT~WqVMJ#9twx{y!Dxpx{9^zY?z|-PX{^JsG2@S&92ft<Xa&8=}Xn2hM;sJ;ayNNme
E@<8okE4zI;!}p9c>L7JqxBg@MquCKiV>P2)KFP5T9qY1#0?+Fy6;9gnABpl=f#qVcntTqhi>=dnZAQ?&l5_kydf^smGX06Y1W?)I?j-v-T?s<=2WB3>U-_E
pk*jVv-~rCKGl$ZuN0n?l*1#P0;rF8jG+z@RPqgXDmTIy^7Wx6(FX?nMlnWv7&6>f)O&ZslQ=)B(diy|=C?r@`I?H!XL81d!Lw@wEFvF3w}(4rpnD%i%iZ8^
)lDcX{Is+G)GhA;(9PLyqnk#RX_}y8Ni?*Zz3Vr0xiZWOgP&Ss{mo3cQ!$DLL*Zb2_I~rfbK<NiElXE?_NjlI8>GY@Y)o$iix`!N8{<&e<%`z&dEj+>ka{|p
NJVuLgtKqKoh}b(ARk{A<|g2M)LJ(L#O*;K4m{91ctA|P3Zk1bs7^O4c+~K{!GrGx47?!unFl28Z!my|8NcNi#!z(`2{^FF*7V~5<CB4&F`&zSA4C+uldwXF
&M}8{%UvFcAH-erHqeAF%m2h}&$?>a^J~cXb<=;O)Ew3AIWqBMNuwi##H<QyH>L^$9r5NxkNy%I@GHf*u=8e_U)8;F-%X<b9`oRW@5HbAgL2tk=So7lp(ncw
9P7SwAOF_&E2GdZNVDjMIQ7`7{Uguzm3G_$<0KDADPDg|yxHgWd7ZOa1yRu7dyjOjHt~6kZK3Hnb|xYC%e?Wkg=b>V^y;lm_gj-6_EErt5A)Z1o{7ltgE}vN
xT~*LS+>?c`egIN6Q*U0!k@}NJLBdih#M6I_a3XYIyUh|$%eACccb?E42yA~dkB)gtf*R%`D}UHIa`hLCn=a;nu>MjAAEh&QKR^ddP2%&ud+iqdMh7(>$&N^
FB+z<b<ke-=we#Vd*a$d3At~KK5$08xK?-^$>e16S}xx&++tO`dElX-wsqdbKg%*VjYMx~wx^$7GwZ*DSq5zw?zm~BQW)qc^)yB<M*RAKCWve2l{`|edM4_$
oTud=7=KiQre2RQxz`%Up4nhozJf#Y;-Q1_4>y|UylZi1flVN%#TEvy2Akq&T`k15m%&3De%DwlKGYS{?q0Fr<+pvPd3m%q7`S3&@2bc3s`f!p<l6?tm1k2X
^3f-UV{kVO@0h2fI7?Yed%3MSZ56LN(7CG8cyCx`Ih2t|t<~2>&9M)CbIUP2WpT}zWJBtX_B+CW$_IEqq96SImpy9UX_eH7ZAEctn5kmp+JIwYji@=Q<lrIc
)3cz?^FyOxsb}5LrEP;A?Fa5u_+f+brr~>w#jbC-L|LG@!>ZUp>PFHiq{MH}(t(^C>V7`bM*hOF#uEm*5AasBJ>0C1gPssAxK)1xG`%=E)gL+cDhHLyM%*{V
*ob1(jJ3jA&39~V%`hwUP<BBIHt0QufXD{u43!DCC`9|la}IXiRE13%jx>E3<}4rGa!FiuvOgsabc|flqU>t#<Au7x9gw1vi<<GNcq>y3)y;;GSd@tVaSdQL
z`xsa@`1gmx!D5)M<XDnbM1owsUa^Ta0q21^kQ!7eMsv6DXP349*RFLcD@6KQE?bh=Z04I`M!~yB;QJie(-)*+V`!4sqonOmxkfB6Jh31U+4tYElQ3<zttq4
vn)P89H0fw4f37QhHx{<9_+0Si_2=s&ONcK&J)|RFXugd=YbvniFFScIJiK;v&+_zmwGj&>qgAL-t9N18wQk~{Uy8X^Ul#5916DIE3rVQ+$iW9Uf>scpe*iU
)WaY0qpi@PxD?Wjw|e*U-1|7T2IiPu>k00;f@HJLs`Xa3)u~t5ZTAS-9oh0;sPV$;ax`>%Lgp)h>TwyL@#Plv^1T+kmb7iRO5!1?gZN708lQ5xoa8sM`yo<&
?BZBf3z+0r!&v>P$67AXej^#G2A224^Pl=C_30}c*MBo&a=7}DjAq%=`!S86YfuiEkA(L5Wf&3mLqV@IgloP#q$Bn0W*Ibl5pH*vH+PK&`vh7i8?#)g;Lvwc
v);~sOvT?c0e?da2=te>OOq5^n?hisCFpq26`7P}0(Cb=!_Q!S-L~jrY;wjx14{qdy5KmCj8Lj}_>G~8Ep7T#;ZuwY#}pro6@#-mCIzFnD|R$PcNIJ-Abbfo
{}UPs&LQyRrw%tLw1*q!kYoVWn$YrV-POB41tu+cZSum&|5Sy~@1A$OxFbKD)1JO&HSy(}IAavf8Zmvn966;KUp$?>=RO}bOXu{+Dcv|j=ZuM7u64%$#l?Lw
3(gsYGjy@S#W_#rZ0CiR>7C-7UA~-wop<h>FL8R+dS`2#fyGRn)3f8OIl2GMjx&FAY>IQO`?7(r7&FsmbMA1qrExBTuXLZ+X76=|rDx;y(mVd7gxxuR5`mZ9
e4OD~FIK~yyVn2q``<>r_V=#8KmHZbg|n<PyYD4ZbA4$x8u;hv!MRqL?R9^OU@p#z_y4a=b0@7cWy$F{l%8AxA0<gC`NDdVFXrb@Hu$qy1-Y|!^5>|Zf#-{;
!Pn+S5dKy4%(6SqW`r4D^LKFg%lGhAzA%XZyYHDRcy1-`R1{1;oo>zE*^B)m_f<&DW|u!9h%;t-C5PfGxnVYI&ta#T8n`n(ZWim$VS)bw(<>~Gv%GlD*)q#+
GnpOd+U8HuHv6QR?Hw=dF%#pNnz(b%ioe{_%n`GY`|CB%(1x%5=^UQn7c)+RX>@1f|I#!591}R_<a{L(IDMw$E0`6ze|1veT#HV{HGf*)9B!Za4u6h{DPEbw
Rx?hISHmv(7ybX0^Zxn)jWn(P7QJFQ(jpm=<ZGf0>Ke3?GOeVjBDd*hBEQg#1kIrOI&}@?UlZ!VHK8pq9A*_NGBmk_0+Ddh<rhuat4fMW$}8md{Xyg$@=;14
5Yj?Mpz!^4;}-+a0|Nm38Gk~+GeTOll87ow{dgh{emoHk7zsoRU>e|jp-5RM3IH<jE+C&wEGrbLA1AUAoq@UX8}qLvcnffmf^dc01-AIZ0c^p6Oo0*t5t(x5
WceOy!B(Y{Tb0f*0x3oS>R($DS&82xhv4=NelL&^a9CrWIDX=|3azR_Zx%7~B8D%L5-D!oy!8kk6^J$+Ct^qzwMpT~CWZY9@(S{5s%q;*4B48HIsLpof{SqF
?wz~kQSJnPg`ArD5S)-?>sz>E+YSw!kNn@S|NgTQt*k_^BoJJ}i+F}iFD*yQ%h5YUq7Qx{qKL|<fgcMPDFJhCUk;ceDI8Ixq#;sTM-wDJ__741>Rdo=Bmnio
cNf09B%Cjl5($+>!aNqVCLpVnMB$R9%T8871ysQ{v?MzyhC(QYBuIofB3Ur`#!o8hDt{1Z1NBYk)Hhw<q_Js_7@|Q8!4L%gME)RMCs9KElpe6+4z5IQ04$V~
k(06kOR#}UsLBW!Mkrte$EO>+@CN*J`HCza8ioNF23Mqk{stAd9wt^f{5^h87X2}vSs~iILbMI}1aDc~&pHxW{3?`3Sz;kmKzSBF))Q$0G{evgtDmL?^a%pR
+^!@buK}){G-C*$KXC}5%4VU;e3ftbwxIHrWE`OM;dd?J@VmBvGRS9NR{F=aO%*uZDnVj?NtKl<8Y&7Zn|4>jWK{tef_NLrqTLV;5%pR0fwV}^AfPFlkhTdv
B{=J%7V2UW5P$e%6rRE;Tp}tRp$8rlX=5$MZeFI7v^${*8ljGe7T~#Bs0LQ1tX2Y37K;Od!SMpfg#u!=Oh_XV2LyfPRAS9kxC;?*o5)?DSu|+DWJ$I|vwxcH
Br*vU&BDaq((JRl_%~m$MAm1+KtT+8)MVw#!tiAT>{Z+P5F_A#+SWLVn2nfPe-a)L$_eF;u*DW~s|C!~oy^u<s12-IK^T-wH>wej5aqkbsMGi{DUaZLxJ_xt
cVF&n!pZ738L>ing*>ujB)@BfEF=YaPnAFs30u7gXr$1i*vBX}X&xy#hFM8Oe)5hblRs~YZBOl=v;<$r;r}v*IO%(MgqRhCN`h@fILK1i2S+|2zTpA?{P~}b
NERCpm<wcE^F;!IDiLK|A~GQXM2bIf9de0k86t{=g~*SnlPC144S1dS2itT45`1?-Y3oU)t(QJO{rPFK4jEQh$|95P-?wMqArdq)#6whtw3LumCNJ#WCp^AS
m<EKXHj>aW1hNuIVv@~dq!jCU0>au`f1WIlkaa7wL`a@XqYNQiX|hEURsu4OkOZ=b7Ag>$cR@q?FCN&^M5hG)&Yve~2-9Q8D4~G(B+lt@M6%>F#9|<1WP}V~
?eGc#6AY8pEjXcY>4d^LRMdn&GzqiNDyp=K1X+^=IjLyTzoz`%5T_W0AbiacR$NO0LLQ35B2MIdAzS=KiI&?&M1w4AJqhF^#2Gey{K==+kwXTtZm^4lrY-9w
k_1B}i@7dR+bL30MUH@;FQEA=PF-JdY7c=<RhPu2E}=tQNk&T(oB%mAP5$z@ov1%_LL^$@3T){J7K8;@QBe>aAtHa6L<y3Dutq1L0aEC(+``8HA!4unf*j)h
q#)Xb+@mM?@4bP?k+VZ-hb@p|Kdupdeo6Fs9a%8pIe|zd6pBOwMxk)_?QuLn!VEW))da8shuo>dP#%LpfmT$Yk(@qOfZxk5lzvml2v-vM3J)DVbl4Q$-TyA&
l_?&&MZ$|9jksAsg=UVh#UA27TTpiDc^Q)PWIhQ#joq6Bv=*?XDabL3a*UAAER<yC<NhhM){&*0{_*=Cj}OD{yTn$ziE0S~^d&hp<`667ISEh#rp%Nf*)3uX
dvFoRm%b-DdsK9VBmyD@Igy%znw*e$+bx`V=ZZUohjs{0;$D%o=uMHN=<?(lDZgSjBl?3a^w_PPM$XsgzLq4jDdSNj_J&CfDng-x7QSd2vd2F;pYhOcxs&97
?U!r6OrFzh+$!TTRNkj_Zl98>P^c&r9>PU(YJ23=q_`9wJazIE;BjKj3pSt@M~*=?TQ-N0m_oso_!o((`Q&|(@B)z|D-?FFP}q+g;;r(;4_IeB^yQf^6^U={
LRFL?QTm$X0%>xB5E%9l$6bRviR&)Gb>v=(xUA|V9Ziyx#>?hTa*j!nb#k`6v5`k~C=z1f5U!BI{m-*i_FN#ur8-r~2&edc^YeNo%3ZnoPivSOI!Sq?P@Qf7
{qj<s(f+Ic3&fUO`Y*0Cf6<S--{jC-T4D8$&9sQ{$ja?+l1`<C5=sl_U%R?{50RaWP=*o8Pv&fPU<&^yZ3)`&2U!OP7g5YS;X+D<5ZeBi&2!}0GP!;986xKh
MAFZb(Kl458wZTR42*%xQZ6}v`Gg=;URNa|gA!s$04`fx#48V>1|EVWIhT%z6xN9pwh=Pei|gh|&f6$bzsiaPDqQ(!>AybGKxvdxP&oY7ezwq9AiaQ#dk>O8
6>=xbZMaK`zgmg=nP9QBVDWojUzYs(GBFo!Bo4qwE^!G7V$M}dmn~htT#36}Ns*y|p*XC&P+UqHLFL3j4I)Qyqk>RXLAZ_Jv5qC}sXX+3?sU!S+_q!q4m`2`
CPaanx;@O>INh>jvw1f4)rS9&KW8d>2v10p*EmGw_QlKhE?zDx`rxWG5hN6|6F+@ZP4Z2(lMZN(9JW}qLAY##P+~G24TP1?Yek|(60e;9=DZA>D+ra=36&0!
o+Ym@di`TOzH!5P;X4Q3kwyvJ^46}mwy$2ZnlGFO!g(H`uJXPFk-H$LzF$sViacGieAV)03uPC6_4eMk6><Hkv;0$M6?uG~B=Sj6uO#M`Bnkgiy2%`$Zk)s`
?;m|%k>qP^qLc;4h?zKq0S|}5H$+rXmL*@5*!L#+BQ9IKWHH$^L3j~aum(vW=VKQjN%*7);>c3s+%)q(aQ@sSOOkg!O0rD2kT?=9QduaavQSms0WP0p3qtJ*
hc74`CalCp8N;~1wN0_O@@1359&}`5OW1_d7v@h@+elnWlU_xlU4pdvlTdQ-L$XO(+(^LGhJXM1Zx+qHgw#)N*tmhUpd=Cg+VyMK5DfV!OB`wm+2|sICYLDV
5XY1xNG>CzRM~Bk8vkA{sDtbN?h7l)Nt*}dkVYAyd^u!MW@yQhj+ol}bvG47T|O{bdDAFM*2ntiB9b^RRb&hDi9iBLxc#7zL%w{baz<w=8>U;EQJR==C3z=c
GVkZI(Tv;K#IXZTPgUe|VhOu(Wb-ZQt>3xA*6+yBB?JgrKiFCgq%dU{L}GZ74VN(s6r_k~OcN>d>fA5_0zojH9oGF%qvC*=LK>xsQPwCCULbOWgh>dJ$O#5?
!{7ezx9hCcP>RjW<ka7iATpml!&K!&zmlOO%U+-&Pvob`)b={r*<{Xr9a+n=ouB^j(+{U7BXA38Ni*}*Rf()2GkkUStFvEx^zlcFh$|f>j<k&CacSNf;!H6h
G=$%UL^*LNGaxJ2{Kl3ywh&KRMLcUgx#zNJ<JxVL<spKy?6hAY8!Qr{=Lug9l|Tt*<cV7NS5Ml2M5qLbP%_c+>1<JWSrbUQ_yErQxrfaj$%JbJ3;BYDyAH1q
1%ek`e_pFzJ+<WOsh`mdKKtS`iKV<XOL<)K0*a{lA}StRpdDJE6i9wjhu6-^Tsx~uHp*spi|{>yk}NGJSV?3ZL4DqqH@9n`4@r>810(i`Ai;!$A-Lo)X1_vK
nt&mgz|Um;>)sNse@l1~&rN2BYfc@Sck0Lv!dvS|x_c78AcHp(t|Or=;z@{jTM!AF+ezA}aDgqZlQpbS5bzX<3_>hwLi}WTL2k9Q+-g3Xi4gDplx%vxNT4VZ
e1UR?u;Z{E5F(Srjh|oLsz~GzRzd?9z!z*moLzcmo~YIfvu?A1<Ozt9B>LG%O9ma#C$bHt=>?MX0zPgh`NM}~!!mLUX$}!7)Q3+#{Y09$izGTxkFXvep$6$B
{zSf2)HZCLw~{R+h>u8+hdSgNSqC>0x8#%0`7d_AwR?dETbx-a;4dV0lUlb|<_-LnJpsrY8;S2+R~iOeBnA0~`iZ=^UyXTPo`~|KcgYg3ZijB@BSPqv(DZtO
`+LiUvde|*$T$B~f~W}}k*v-iXWgd3`4iITPprdTtJcabShiN~pwc`krFpWu6>bvq?VqYtf4}~FAqkpqFMfM~BwQEpLp+1)r_;m@(eR?F$GX-cT!VbMch<|j
^9}J^WqR!zdhHgniS2k2w<w+6t915&aJj5-`6`rG+rU-Zu;T4qZ+}2^^YIEX{TFJVtXKQwXY#S;1SHaT;(C&~tw+^kUoMv=!cjQ5Ug4kw?jn|#A~x7g;%_gR
bUm4rq!1{xXW#x4$38r^4384OSV#P9Jt4Kp!+|X3E8<O(Y<9R}DN98fFPmrBJdya~CbF2%i6NH|6c4DXty9B8&%cnllR4sIiK%MW+9^KgKd)s-#_;WT7gkPv
Oh3;MS97NuYhGq_?<|?oKJe;X5r3FWPXA`ENdG?;8k4p
"""
import base64,zlib,hashlib,struct,csv,gzip,json,math,sys,time
from pathlib import Path
from collections import defaultdict
from itertools import combinations

def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))

def decode(payload,base,expected=None):
 raw=zlib.decompress(base64.b85decode(''.join(payload.split())));assert raw[:4]==b'NG01'
 if expected is not None:assert hashlib.sha256(raw).hexdigest()==expected
 cur=4
 def uint():
  nonlocal cur
  n=0;k=0
  while True:
   b=raw[cur];cur+=1;n|=(b&127)<<k
   if b<128:return n
   k+=7
 D,h,a,t=uint(),uint(),uint(),uint();assert D>0
 def table(n):
  vv=[[0,0,0] for _ in range(n)]
  for j in range(3):
   last=0
   for i in range(n):
    k=uint();last+=(k//2 if k%2==0 else -(k//2)-1);vv[i][j]=last
  return [tuple(v) for v in vv]
 v=table(h+a);I=sorted(v[:h]+[(x,-y,-z) for x,y,z in v[:h]]+v[h:]);F=table(t);assert cur==len(raw)
 assert len(I)==len(set(I))==2*h+a and all(0<=i<len(I) for f in F for i in f)
 vs=0;ms=[0,0,0]
 for i,j,k in F:
  p,q,r=I[i],I[j],I[k];d=dot(p,cross(q,r));vs+=d
  for x in range(3):ms[x]+=d*(p[x]+q[x]+r[x])
 assert vs>0 and ms[1:]==[0,0]
 gg=math.gcd(4*vs,*ms);C=4*vs//gg;M=[x//gg for x in ms];den=D*C;Q=[tuple(C*p[j]-M[j] for j in range(3)) for p in I]
 base=Path(base);base.mkdir(parents=True,exist_ok=True)
 for name,rows in [('raw_vertices.csv.gz',I),('vertices.csv.gz',Q),('triangles.csv.gz',F)]:
  data=(''.join(','.join(map(str,row))+'\n' for row in rows)).encode();(base/name).write_bytes(gzip.compress(data,compresslevel=9,mtime=0))
 def sha(v):return hashlib.sha256(b''.join(struct.pack('<qqq',*r) for r in v)).hexdigest()
 definition=dict(raw_denominator=D,centred_denominator=str(den),centroid_multiplier=str(C),centroid_subtract=list(map(str,M)),volume_numerator=str(vs),moment_numerators=list(map(str,ms)),raw_I_sha256=sha(I),F_sha256=sha(F),decoded_stream_sha256=hashlib.sha256(raw).hexdigest())
 (base/'definition.json').write_text(json.dumps(definition,indent=2)+'\n');print('EXACT_LITERAL_RECONSTRUCTION_PASS',len(I),len(F));return definition

def load(path):
 with gzip.open(path,'rt',newline='') as f:return [tuple(map(int,row)) for row in csv.reader(f)]

def audit(base,allpairs=False):
 base=Path(base);st=time.time();definition=json.loads((base/'definition.json').read_text());raw=load(base/'raw_vertices.csv.gz');P=load(base/'vertices.csv.gz');F=load(base/'triangles.csv.gz');D=definition['raw_denominator'];N=len(P);T=len(F)
 assert D>0 and all(len(v)==3 for v in raw) and all(len(f)==3 and all(0<=i<N for i in f) for f in F)
 assert len(raw)==N and len(set(P))==N and all(len(p)==3 for p in P)
 vol=0;mom=[0,0,0]
 for i,j,k in F:
  a,b,c=raw[i],raw[j],raw[k];d=det(a,b,c);vol+=d
  for q in range(3):mom[q]+=d*(a[q]+b[q]+c[q])
 assert vol>0;g=math.gcd(4*vol,*mom);C=4*vol//g;M=tuple(m//g for m in mom);den=D*C
 assert C==int(definition['centroid_multiplier']) and M==tuple(map(int,definition['centroid_subtract'])) and den==int(definition['centred_denominator'])
 assert P==[tuple(C*p[j]-M[j] for j in range(3)) for p in raw]
 cv=0;cm=[0,0,0]
 for i,j,k in F:
  a,b,c=P[i],P[j],P[k];d=det(a,b,c);assert d>0;cv+=d
  for q in range(3):cm[q]+=d*(a[q]+b[q]+c[q])
 assert cm==[0,0,0] and cv>0 and cv==C**3*vol
 occ=defaultdict(list);links=[{} for _ in P];neighbors=[set() for _ in P];normals=[]
 assert len(set(tuple(sorted(f)) for f in F))==T
 for f,(i,j,k) in enumerate(F):
  assert len({i,j,k})==3
  n=cross(sub(raw[j],raw[i]),sub(raw[k],raw[i]));assert dot(n,n)>0;normals.append(n)
  for x,y,z in ((i,j,k),(j,k,i),(k,i,j)):
   assert y not in links[x];links[x][y]=z;neighbors[x].update([y,z]);occ[tuple(sorted((x,y)))].append((f,x,y,z))
 Etri=len(occ);assert N-Etri+T==2
 for pair in occ.values():assert len(pair)==2 and pair[0][1:3]==pair[1][2:0:-1]
 for link in links:
  assert len(link)>=3;p=start=next(iter(link));seen=set()
  while p not in seen:seen.add(p);p=link[p]
  assert p==start and len(seen)==len(link)
 seen={0};todo=[0]
 while todo:
  for q in neighbors[todo.pop()]:
   if q not in seen:seen.add(q);todo.append(q)
 assert len(seen)==N
 ray=(5,7,19);pre=[]
 for f,(i,j,k) in enumerate(F):
  ss=[dot(ray,cross(P[a],P[b])) for a,b in ((i,j),(j,k),(k,i))];assert all(ss)
  if min(ss)>0:pre.append(f)
 assert len(pre)==1
 par=list(range(T))
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 flats=[];hingemin=None
 for edge,pair in occ.items():
  f,i,j,k=pair[0];ff,jj,ii,l=pair[1];h=dot(normals[f],sub(raw[l],raw[i]));assert h<=0,(edge,h)
  if h==0:flats.append(edge);par[root(f)]=root(ff)
  elif hingemin is None or -h<hingemin:hingemin=-h
 groups=[root(i) for i in range(T)];gf=defaultdict(list)
 for i,g in enumerate(groups):gf[g].append(i)
 normalsG={g:normals[fs[0]] for g,fs in gf.items()};boundary=defaultdict(dict);true=[]
 for edge,pair in occ.items():
  f,i,j,k=pair[0];ff,jj,ii,l=pair[1];g,h=groups[f],groups[ff]
  if g==h:continue
  true.append((i,j,g,h));assert i not in boundary[g];assert j not in boundary[h];boundary[g][i]=j;boundary[h][j]=i
 cycles={}
 for g,link in boundary.items():
  i=start=min(link);cy=[]
  while i not in cy:cy.append(i);i=link[i]
  assert i==start and len(cy)==len(link)>=3
  nn=normalsG[g]
  for a,b,c in zip(cy,cy[1:]+cy[:1],cy[2:]+cy[:2]):assert dot(nn,cross(sub(P[b],P[a]),sub(P[c],P[b])))>0
  cycles[g]=cy
 inc=[set() for _ in P]
 for i,j,g,h in true:inc[i].update([g,h]);inc[j].update([g,h])
 for i in range(N):assert any(det(*(normalsG[g] for g in tri))!=0 for tri in combinations(inc[i],3))
 fmin={g:1 for g in gf};vmax=[-1]*N;H=[];degE=[];primitivezero=0;minp=None;mins=None
 sign=lambda x:(x>0)-(x<0)
 for i,j,g,h in true:
  p=dot(P[i],sub(P[j],P[i]));r=dot(P[j],sub(P[i],P[j]));u=dot(normalsG[g],cross(P[i],P[j]));v=dot(normalsG[h],cross(P[j],P[i]));primitivezero+=sum(t==0 for t in [p,r,u,v])
  fmin[g]=min(fmin[g],sign(u));fmin[h]=min(fmin[h],sign(v));vmax[i]=max(vmax[i],sign(p));vmax[j]=max(vmax[j],sign(r))
  for q in (p,r):
   if q and(minp is None or abs(q)<minp):minp=abs(q)
  for q in(u,v):
   if q and(mins is None or abs(q)<mins):mins=abs(q)
  if p<0 and r<0 and u>0 and v>0:H.append((i,j))
  elif p<=0 and r<=0 and u>=0 and v>=0:degE.append((i,j))
 S=[g for g in gf if fmin[g]>0];U=[i for i in range(N) if vmax[i]<0];degF=[g for g in gf if fmin[g]==0];degV=[i for i in range(N) if vmax[i]==0]
 assert len(S)==1 and len(U)==1 and not H and not degE and not degF and not degV
 stable=S[0];unstable=U[0];n=normalsG[stable];assert n[0]<0 and n[1:]==(0,0);rn=-P[cycles[stable][0]][0];assert rn>0
 assert P[unstable][0]>0 and P[unstable][1:]==(0,0);R2=dot(P[unstable],P[unstable]);nearest=0
 for g,fs in gf.items():
  n=normalsG[g];d=dot(n,P[F[fs[0]][0]]);assert d>0;gap=d*d-rn*rn*dot(n,n);assert gap>=0
  if gap==0:nearest+=1
 assert nearest==1 and all(dot(p,p)<R2 for i,p in enumerate(P) if i!=unstable)
 paircount=0
 if allpairs:
  for g,fs in gf.items():
   f=fs[0];n=normals[f];d=dot(n,raw[F[f][0]])
   zeros=set()
   for pi,p in enumerate(raw):
    gap=d-dot(n,p);assert gap>=0;paircount+=1
    if gap==0:zeros.add(pi)
   assert zeros==set(cycles[g]), 'maximal facet has missing or extra vertices'
 assert N-len(true)+len(gf)==2
 report=dict(status='EXACT_RATIONAL_GOMBOC_PASS',vertices=N,triangles=T,triangulated_edges=Etri,true_edges=len(true),maximal_faces=len(gf),C=2*len(true),coplanar_diagonals=len(flats),class_SHU=[len(S),len(H),len(U)],class_SUH=[len(S),len(U),len(H)],degenerate_equilibria=0,zero_true_edge_primitives=primitivezero,centroid=[0,0,0],volume_numerator=str(vol),volume_denominator=str(6*D**3),centred_denominator=str(den),stable_cycle=cycles[stable],unstable_vertex=unstable,unstable_degree=len(inc[unstable]),stable_x_numerator=str(-rn),unstable_x_numerator=str(P[unstable][0]),radial_ray=list(ray),unique_ray_triangle=pre[0],all_vertex_links_single_cycles=True,all_vertices_rank3=True,global_insphere_unique_equality=True,global_maximum_radius_unique=True,all_pairs_exact_support_tests=paircount,minimum_nonzero_hinge_numerator=str(hingemin),minimum_vertex_predicate=str(minp),minimum_face_side_predicate=str(mins),elapsed=time.time()-st)
 (base/'verification_rational.json').write_text(json.dumps(report,indent=2));(base/'maximal_faces.json').write_text(json.dumps([cycles[g] for g in sorted(cycles)]));(base/'true_edges.csv').write_text('\n'.join(','.join(map(str,sorted((i,j)))) for i,j,g,h in true)+'\n');print(json.dumps(report,indent=2));return report

BASE=Path('NH13_NO575_R1213_reconstructed')
definition=decode(PAYLOAD,BASE,'881fd33984535cbd2bd181c8f0cd4d437b6e63770ddfc0380126c9f8b47b1657')
assert definition['raw_denominator']==10000000
assert definition['volume_numerator']=='2936986753449982560844'
assert definition['moment_numerators']==['-56752729877257941979637814','0','0']
assert definition['raw_I_sha256']=='053094d59b4d4e6229ad592d9b50aa2ad54ad001d2b99dd03a040fae79f192c6'
assert definition['F_sha256']=='e9b1d5dd6c9c58e2e1fcf7d24861909b2e6be64b1bd5f9d8bdc9d348aef97e79'
report=audit(BASE,allpairs=True)
assert [report[k] for k in ['vertices','true_edges','maximal_faces','C']]==[1213,3630,2419,7260]
assert report['class_SUH']==[1,1,0] and report['zero_true_edge_primitives']==0
print('SELF_CONTAINED_NH13_NO575_R1213_PASS')
```
