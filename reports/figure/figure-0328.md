# figure-0328

AI research report · 2026-09-06 UTC

---

# Calm Nova 11 — exact centre-space obstruction and retargeted reference chambers

## Determination

**This continuation did not produce a new own-centred strict (1,1,0) polyhedron.** The retained exact body is DG138F:

```
(V,E,F)=(138,397,261), edge budget 2E=794,
own-centred (S,U,H)=(2,1,1).
```

It remains a nonwinner. Its edge budget is below1000, but its equilibrium class is not the requested class.

The new completed results are: **an all-reference-centres obstruction to retaining the intended stable13-gon and unstable137 as the unique pair; two exact alternative reference-relative110 chambers; and a separate ordinary-volume-centroid obstruction for both new chambers.** The latter permits arbitrary other material changes while the specified supporting plane and opposite vertex remain fixed. None is a global Gömböc complexity bound.

## 1. Exact restart and provenance

I recovered and checksum-validated `CN11_DG138F_EXACT_NONWINNER.zip`, SHA256 `b3aec85df5279a89bde6c618dfd47de0764cc6dc239c37cac4cc60e12032b719`, and reran its exact boundary, mass and complete feature audit. Its9575-byte coordinate/triangle capsule has SHA256 `a6f61e2e35d9aa0b493235b480fd336d4310af62127c94b1be050c3b0cb9836c`.

DG138F is the previously constructed successor of the lead's STRATUM141_S211_NONWINNER, not the2033-vertex methods parent. No2033coordinates, symmetry assumptions, denominators or apex IDs were substituted. No source-authority conflict was found. The falseJ56 was not used.

All indices below are **DG138F local indices**. Its two stable faces at its own centroid are

```
Q=[0,43,67,11],
T=[17,90,111,112,115,117,119,121,125,127,133,135,134].
```

Its unique unstable vertex is137, degree8. Its sole saddle is[0,11], incident to Q and triangle[0,11,18]. Define the additional triangle

```
Rface=[32,117,53].
```

## 2. New exact theorem: an extra stable face is unavoidable for the retained target

**For every interior reference point c of this fixed DG138F solid, if T is stable,137 is the unique unstable vertex, and the equilibria are nondegenerate, then at least one of Q and Rface is also stable.** Consequently no interior reference point—not merely the actual centroid or a small neighborhood—gives strict110 with sole stable T and sole unstable137.

This is an exact statement about the unchanged finite geometry. It does not exclude an actual deformation of its planes, vertices or face lattice.

### Explicit necessary system

Write the exact own-centred vertices as p_i. For an oriented true edge i→j and an outward face normal n_f, use

```
phi_ij(c)=(p_i-c)·(p_j-p_i),
sigma_fij(c)=n_f·((p_i-c)×(p_j-c)).
```

Both are affine in the three coordinates of c. A nondegenerate nonunstable vertex has a positive phi to some true neighbour. A nonstable face has a negative sigma on some edge of its complete boundary.

The exact proof needs only this necessary subsystem:

```
c is interior to DG138F;
phi_137,133<0, phi_137,135<0, phi_137,136<0;
sigma_T,17,90>0, sigma_T,127,133>0;
Q and Rface each have at least one negative boundary sigma;
each vertex in [0,1,8,19,22,60,89,90,131,134,135]
has a positive phi to at least one actual true neighbour.
```

This subsystem is infeasible. The proof therefore accounts for a **replacement stable triangle**, rather than removing Q's label and overlooking a substitute.

### Executed complete centre-space certificate

The portable program starts with the exact convex centre-domain DG138F, clips by the five base inequalities, and recursively branches over every alternative in a violated disjunction. All intersections, signs and choices use rational arithmetic. A branch is discarded only when its new strict inequality has no feasible point in the current cell.

The completed traversal has **3282 nodes,2840 strictly infeasible terminal branches, maximum depth7, and at most63 cell points**. Every generated cell has its supporting-plane inequalities, convex face cycles, opposite edge incidences and Euler characteristic checked. No numerical linear-programming verdict is used in this replay.

A separate affine-inequality proof independently confirms the retained-target exclusion:1135 directed-acyclic proof nodes and804 distinct rational contradictions, expanding to3142 tree nodes and2710 terminal branches. Each contradiction uses two or four inequalities with nonnegative rational multipliers; the centre coefficients cancel and the weighted right-hand side is strictly negative. Gaussian elimination and a cofactor calculation give identical multipliers. The root has no undischarged assumptions. This second certificate is preserved in the archive; the complete clipping proof below does not require its stored tree.

## 3. Two exact retargeted reference chambers — not own-centred winners

Dropping the stable-target restriction produces the following strict reference-relative110 chambers in the same unchanged geometry:

| Chamber | Rational reference centre | Sole stable face | Sole unstable vertex | Certified closed cube radius |
|---|---|---|---:|---:|
| A | (737553,82268519,9246050)/10^8 | [70,98,80] |84|2^-12|
| B | (-53517649,16728265,17671643)/10^8 | [0,42,44] |137|2^-15|

At every reference point in each stated axis-aligned cube, the class is strictly **(1,1,0)**. There are no degenerate equilibria or zero individual true-edge primitives.

**These are not homogeneous own-centred solutions.** The ordinary-volume centroid of the actual body remains exactly0. Translating either reference point to the origin makes the body's actual centroid minus that reference point. Both translated fixtures were tested by the independent own-centroid verifier and both were **REJECTED at `rational_centroid_not_exactly_zero`**.

The cube bounds are exact affine sign certificates, not samples. For every relevant affine predicate a·c+b, the code derives the distance bound `|a·c+b|/sum|a_k|`; each reported cube radius is smaller than half the minimum. All4E=1588 true-edge primitive signs and all interior-support signs persist throughout the cube.

Every vertex classification is separately checked against all other137vertices:18906 tests per reference. On all397 true edges, the correctly oriented cross-product signs agree componentwise with the two-normal Gram formulation. The same code at reference0 reproduces the actual211class.

ChamberB shows that unstable137 can survive a reference retargeting, but the stable target becomes triangle[0,42,44], not Q or T. This is consistent with the retained-T theorem.

## 4. Exact ordinary-centroid obstruction for both new chambers

Let a compact three-dimensional convex solid K lie in `n·x<=h`, contain a point w, and have ordinary-volume centroid g. Then

```
4*(h-n·g) >= h-n·w.
```

To prove it, use depth t=h-n·x and maximum depth L. Homothety towards a deepest point maps the section at depth s into the section at t>s with area factor `((L-t)/(L-s))^2`. Thus section area divided by `(L-t)^2` is nondecreasing. Multiplication of the weight `(L-t)^2` by a nondecreasing function cannot decrease its mean depth: integrate `(t-s)(k(t)-k(s))>=0` over pairs of depths. The unmodified mean is L/4. Therefore the centroid depth is at least L/4, and L≥h-n·w. This is an ordinary solid-volume argument, not a vertex-mass argument.

For each new reference chamber, take its stated stable plane and stated unstable vertex. Exact rational checks give

```
A: (h-n·p_84)/(4*(h-n·c_A)) >271,
B: (h-n·p_137)/(4*(h-n·c_B)) >301.
```

The ratios are approximately271.61663656 and301.41431649. The capacity inequality remains violated throughout both complete certified reference cubes.

More strongly, any compact convex solid retaining the corresponding supporting halfspace and point w must satisfy

```
A: ||g-c_A||_infinity >3/10,
B: ||g-c_B||_infinity >1/4.
```

The exact-bound locators are approximately0.30525009 and0.27759593. This permits arbitrary other vertices and arbitrary other material addition or removal. Moving the specified plane or opposite point leaves the scope of the exclusion. It is not a general impossibility theorem.

## 5. Exact body definition and full census

The portable capsule includes every138 preprojection integer triple, denominator10^12, and all272outward integration triangles. Perform these exact rational orthogonal projections in order:

```
base[11,43,67], project[0];
base[17,90,134], project[111,112,115,117,119,121,125,127,133,135].
```

For n=(b-a)×(c-a), replace p by `p-((p-a)·n)/(n·n)*n`. Write the resulting points as J_i/D and calculate

```
W=sum det(J_a,J_b,J_c),
M=sum det(J_a,J_b,J_c)*(J_a+J_b+J_c).
```

The exact own-centred body is

```
conv{(4W*J_i-M)/(4D*W)}.
```

All three centred first-moment numerators are independently recomputed as literal zeros. Integration about the arithmetic vertex barycentre agrees exactly with origin-based volume and all three moments.

The global audit tests every maximal supporting plane against every point, complete maximal-face cycles, closed oriented manifold structure, connectivity, single-cycle vertex links and rank-three incident normals at every vertex. Radial degree1 is checked additionally. There are259triangular maximal facets, one quadrilateral and one13-gon. Eleven display diagonals are removed before true-edge enumeration.

For a true edge a→b, e=b-a, with normals n,m, the Gram test uses

```
L=(e·e)*a-(a·e)*e,
alpha=(L·n)*(m·m)-(L·m)*(n·m),
beta =(L·m)*(n·n)-(L·n)*(n·m).
```

A strict saddle requires **-a·e>0, b·e>0, alpha>0, beta>0**. All four conditions and weak degeneracy conditions are executed. Saddles are not inferred from Euler's equilibrium identity.

The separate radial/winding implementation again returns211, all138 link windings one and4182exact predicates. The unchanged core hashes are

```
vertices.csv.gz be705090105038ce5fc42329c01692771cad4268a228d8c36fca210a7872ba01
triangles.csv.gz 681d152b3cd3cdee5eb12e71217a23ea8309b9b16d736eb62be00afd06d77f88
definition.json ac86a840e2ee23f78acce3670687e488755f007841bff786dd36c50f43ba8de3
```

Exact tetrahedron and clipping fixtures pass; open, reversed and duplicate-vertex fixtures are rejected. These are separate computational implementations within the research workflow, not external human peer review or proof-assistant formalization.

## 6. Construction attempts and remaining gate

I implemented common-direction height fields `p_i -> p_i+h_i*u` with independent controls on all138vertices, including the saddle-foot direction and all three coordinate directions. Actual volume and all three centroid derivatives were included. These fixed-incidence searches stalled with physical side distance about0.24850 versus about0.24857 initially. **No endpoint from them was promoted**, and their failure is not a rank-one-family or topology-changing exclusion.

Reference retargeting followed by actual projective centering produced floating233and222endpoints, not a winner. Further finite metric/projective search did not produce a candidate accepted for exact promotion. A nearest-centre optimization did not complete; the two reference points are not claimed nearest or optimal.

The fixed-geometry retained-T/137 reference-centre route is now exactly closed. A new physical replacement can leave that obstruction by changing the actual supporting rows or vertex stars it uses; the proof must not be inherited after changing geometry. The explicit core identifies Q, replacement triangle[32,117,53], selected T sides and137 exits, and the eleven vertex stars listed above.

The next useful construction should permit genuine stable-target turnover, coupled to the affected escape stars and all three ordinary moments. Any reference-relative110 chamber proposed for later mass matching should first pass the quarter-depth centroid inequality for its intended stable plane and retained opposite vertex. The two newly found chambers fail decisively. Removing a constraint from an exclusion only removes that proof; it does not establish a feasible replacement.

No new smallest body, E<500 Gömböc, arbitrary-coordinate tolerance, manufacturing claim or global lower bound is asserted.

## 7. Artifacts and executed replay

[Complete exact continuation package](sandbox:/mnt/data/CN11_DG138_CENTRE_CHAMBERS_EXACT_CONTINUATION.zip):242209bytes, SHA256 **a51cb7bc4ffd2d80423a27d78832aca696521630937f12ed49e4592368aef9cd**. All46manifest entries were checked against the ZIP bytes.

[Full Markdown handoff](sandbox:/mnt/data/CN11_DG138_CENTRE_RESEARCH_HANDOFF.md), [primary exact report](sandbox:/mnt/data/CN11_DG138_CENTRE_EXACT_REPORT.json), [independent Farkas report](sandbox:/mnt/data/CN11_DG138_CENTRE_FARKAS_REPORT.json), [own-centroid rejection fixtures](sandbox:/mnt/data/CN11_DG138_CENTRE_REFERENCE_REJECTIONS.json), and [fresh extracted-archive replay](sandbox:/mnt/data/CN11_DG138_CENTRE_RELEASE_REPLAY.log).

Fresh extraction and `python -S REPLAY.py` completed with

```
FRESH_EXACT_CLIPPING_FARKAS_CENSUS_AND_OWN_CENTROID_GUARD_PASS.
```

A separate replay from the following portable capsule alone produced a byte-identical primary report. Exact replay requires no optimizer, numerical hull, third-party package or network access.

## 8. Complete portable reconstruction and primary certificate

The literal capsule below contains **both the complete primary verification program and every exact coordinate, triangle and projection operation**. Its decoded27068-byte JSON has SHA256

```
e9d28899250cbf68ad33deb23c4fd438b8e019e95fac9ad2377dc561f49e5fbf.
```

The contained `continue_exact.py` SHA256 is `8f89c5efb4d743466b64da271ba5e9be08e8488875087d82bf315578fbdac101`. The contained `DG138F.json` has the9575-byte capsule hash recorded above. This program reconstructs and globally verifies the solid, completes the exact centre-space clipping proof, classifies both reference cubes, reintegrates all ordinary moments, and proves both centroid-capacity exclusions. It does not require the separate stored Farkas tree.

Save the text block as `continuation.b85`, then run:

```python
from pathlib import Path
import base64, zlib, json, hashlib
raw=zlib.decompress(base64.b85decode(''.join(Path('continuation.b85').read_text().split())))
assert len(raw)==27068
assert hashlib.sha256(raw).hexdigest()=='e9d28899250cbf68ad33deb23c4fd438b8e019e95fac9ad2377dc561f49e5fbf'
payload=json.loads(raw)
assert payload['version']==1
assert set(payload['files'])=={'continue_exact.py','DG138F.json'}
out=Path('dg138_replay'); out.mkdir(exist_ok=True)
for name,text in payload['files'].items():
    (out/name).write_text(text,encoding='utf-8')
```

```text
python -S dg138_replay/continue_exact.py dg138_replay/DG138F.json dg138_replay/output
```

Do not use `-O`: assertions are verification gates. Expected status: **EXACT_CONTINUATION_CERTIFICATES_PASS_NO_NEW_OWN_CENTRED_WINNER**.

### Literal portable capsule

```text
c-rlJYjYDxw(VchFdy_FZR-7yx`^Na2Kvx6?WQpiLZQ&3EEl#*LXwS52mk%9wRcvjWDN7TalhR&XK+?k=FXk_xpro1{(f+suQ$cAe9(8zgVW+7-#qC5{b05%w?%oCkMo<!Y<sx6eb9gK&wo6++N>W<i}F!kUbj}a+p}fqe=I*f;D4U8V{1Lxg4X1s1p?Rk&B1heRn8~tThp49v$N$opC4Q=FRm_gJkMJ%)|1Nv^vqjeqBt$`_2I`->9!93Y{}f?#ble0<@+u8Xw4?8&DBMI_-TVq%d73`YCE16>wLCdu5Uk<PcAN6lg%bylaEbnvc^oaS-#q0{=7w6n?Y;7Y?aGx>uQs?s@Z-&tQPXIEG}2e^|rOS-5AbdE+^YFv-n!9%xrUQilsT5Y|bu<>BsVPy}WF#@EK1nJM1kU?U&Ov79f1sZ%6h8SZw`aJI$6C7x{j-d44*%y4cQ(+15OT1h@GbT%EQs?_|4OcgWet2b+95F3Rora&j}?Y}b&&qS$UeKIrzz`r-YbJ5Co1EinV6u<cCDwA)|j+pBfi+FV_BZhE(^)8)E#V{ThT*}|HoOIJs1uBLk<wpXi*ymNE#voW*va<kbR)tL<4QExi*Mh6r8gO)oow&n1hqhF0}xqRp9S4(uB3+rZ96V=7&WPD%EzAQ@!H=lPV^G{~8ovgRr{zt4e&&%v@dHy!QpV@gfl&29saxn#$A|KdYUVY*#kQo*udDntQK8Ya}O0ds=4kz<@=TldS9!^%PyyP<mRANS_N(C@msC~P>nr%BXVeD--RH^>axiPb0`&oO`Rq1k;Yi(b%jgPO|ql(|<O5PnVAer`Zm8&Ce+GaQsx-E)po(<oE``rSUt6_UO+2o)zC^MBFl{__*u3=-2Mt4w_8Rc7=vO7@cYL(?<rxHv}YPDW|g0$OKK3f?@GMtqp%kHDH9PlaARkAreA02FaCH@Gtb5dJR%0=Gssm9i`j1G8sF}v*aIyZ;&yj)%u<pln|6UN)7jJktgD=ESOVAIcjAi}q!!BN%oRNtRk(H^O2PcmolTQ+nI{!@usB*|_^vP`TJGXHfr8JS;)Q~om_bq6O8vu!1xy%qI;!$R?~CqvlgDE&L<UoP1S`Q))Pc$o#gXT6ibam8rRJLz3hX20DpvEA~19Ss)QOUt#qIj)UaWzk=#Y!|b6XJKv{R{E<sGS7^i^5)T_#r+aI9+{W;Xim&;l}&4?w&tv4j?GK<$o9>B@IJf9%g(Re!8>Uj)yBoA4Tak6X4(6lJSG<xo$A{uzxk3zU=4VDoH_b5xxv#f?|16_p0F-!gIJ5maN6xQ`-1E{OqtKKMi}l~6q{{#a8Z=!n{3$p0CGBfY(<U;fmnh`8n2H=gVn{P%rSN}nBGeJ9`gTdy@HYWy3($yvU`uF2Ty38Pip%dJmvG#yY_l&Bv#J59GsU(z6cIE#4X0qbbD*RlaV?<4N@PwgNC8>c2Qsf11+=rj0AnoY|s!2cKuaA#AhppA?TU2?x^~5+O5Ni`DA3lL(9KGTw*{n3`<BTqkcXg?y0haG2QNtSm)Hp8&w=*&8LwB=<~*_^O23&;?4QCa<uooUu|^y-=BDz1V76ll&{gC2QsygCR<492?E082NB_khJ*=X0%v;o{>QOFc%11Z#|$~gRN1kF96Q~N(>=v>vmZ?NRHvI^x??-dv7P4lyAT8u%ii~Te(yw_3&xfW@f`GScDnv;RL%XApVj!J`_mJ|uAZM|C%u>WyCeJlfUcO&yAR)GnP&|(FU3OVhu4#ft9;Y3iEHP&c?swA23D&EA?wp8Qxx4SFDnkj0<x@A;4iW;)Agz9ccD)UeL8Kdk)-#5f>T8SvPDB7V`4D<Y7Ad;iB(McO4g+R*Q#^9j;{3FpN1Vwncr+X1>l`L!g4``-Q)?=FV@Se)h4snZ9S$YYtHlA48gBESbiz<b@umZUp;VPPB;6`u7nzK?sW5QFuR>yXh<rT>&wZ7G>dYU4Tqy<NV9TS6h9(s1Btr$@N@&9Hfp&4k$uJg!tbY;rlD90P<!5Vf62~vX7y_w2`tBoDip|orVyzjMI9$JN@$GeS|HL|ZqFbek@gl`$e^tn+x-EA*p5B_k!d^<uqRR;3N3tC6#eP64m2`O#Bc-eWJsS*_tFmDTjlb@>{et=?a3F8{Bnls3-QDv%Gqsyc3aUey6B9K2uKal6<IdB9a>)#^Sa&5QNKLh*q8Wv;5CLbNy&)63oFK(ef1*i6j~=xIazl0Ez3BlXli8_1*wx}^ya(iwEvx+n+fL=GfYt@oOAow?LKyPp=)+aKF%x2?1cT#)+=BRN+>V47q?)2bA^g;bG2Gs6#2ZhT^ERYFmkOW(E}CkMGG3V1!`-xytrK~%R>>1+sMDlB$+YfvRkEqdR_Ns<caqk30)XvgCb^RY?H2F8lSxVPxW+G$oEfX1?y(n#M=YoupRg@c;Dq)NgU$v)jO!Za{Rq+q*98bgNAkOk`6q$R2RD5;S%<%YP`~1cmI)fB>XqHD{ni@Rw$#*Iled4T5dQU3Z>~qPItH}ckK;=w6^B?0<{_%z>V_aYrb9r=WL33eyu^P20F9beFN47SMkX%7BU``RdhNYiU%PsmEQM7&KXka>2kTXN-fWtX-{RUEZjBhV;c6c7`81hK!s4E^m@mND(=x}1u4|TSV+%qv8JKhA3emMzB>ZMsMcNSjBVirieNaA=f_T8Ww{Tl@{4AtEOYuI-Kx{DeL9)tZKG~nTa)tlUd8w|Bf#c*xel|x*zT@St_De!{Ew`tSp52n)2|f0i*7Y@U+-ZG6~#8cX`7;EOCo@Q&##MIEY*f@U<YK=OQu|5wsTsTu^AI8Xd|;@2B&6`X*@s0DzvrG;0i8Ivux3?_Q1q=%w@xTOx0YB26?tGf<dl!l$#u&H>(AOr-mivwHX|&dinj<0E;x2o+&SDyEJTEnoDhfC*bn+1e|%jOYfk(?3I@_GRJ$Z&?gtGvx$)4{Gh_V_2XrigQoem(S`3CT}tVqc7Cujx}r~9krCR4qtz`RW>UIj*2^VCh^dM5)*2<UhXO|Tnyol~v+L;JGu?c?fazBK&x&m$GMxXk1p1tHeB-*tjk^P>?zWxJ4Pb3*u>JY&3+eQ^TjSr7`T>u^U|o%JUCpJ+I>}(g{P`U)%5R|H3I&DAlwbFuW^svW3Y*tCHw?4C+i<Au)u!EVKmYLL>AUfhH&0*we*FB|`2Fv%|N8Cu_{Hnr|L4i;@t=Raef#_IyYY+TC%=uKK7aG)Uw@9@KKb*{wrRg__urfL^LD?U&9sm7$<Am*#N+7|{@so}boF|T&a(@wpxqxzjV<ooHEdVTu1~7o?#Q(D?O2IpoHpQHyS%4e(6^$&ec){|WB=+E2noqCnZtX1GHtOAQS&(ed{tZ&Q(%F%8jWewSjS{shK;!qJzlMg%VJwxlM26^b`2le{dZX4k^pzYoz%&Ko7@`}52~1hh8!3|$D877j(!_Zm|k%w4l@%J+TGmF<z&UG!C29DF%I}>yqXm2G0_W@I^O1+Ev9(i+tUHNX+Yd{=)6C0yA3H}k?UN9N_UhP{&m>*M!WJvc-=+#Y9vIB@N+)io?(1L*zfrs%f7Irb>U*BrY&+VX5;nbc3erUE%uGXYTC>7ynxhh$1}#>Wii(?1u&<DB9>&22F91LpmDK7bmM~m7Ta6M9}JuJ3G};NcTO<tZ{Pv)6-nZq`HeDs#vN~HcnxO0Xy0de{ZgAR(bUrieg30!Vj?L}yWMZQtuOT{*|a*c3Nn;ewZZjejT|%ETz9zfZ_e_`JYSpj@{8h(FU9sujsy;uSVgD(W!mm?yB`cmu#xXPOgMaje~t=b1N^g`e#+3rTrTH%#zE$CTU_RuWB9e4pxIVJi?3SL2%%zm_zsZl)$b>3#*%es@fB%twuHzRS$ndX6-66W<`)!{HG%Dot%|;^Gc4m!*0b(xZwz~(X?It%_Q#K9yF2)@wq2HAI=b4ucbkr^y^_x51QE_2(wO>SMnp54W;`6JzIG4Spf;Y~ZduF@W*HA#4lkCI`KB{NjkK;+VDfoZZz~Sg!?vX`-keRmFlvu7dm?kFFF5@0EWeo-2nk!zUS4f=>K#LTcX)Y@7oGeDhBRKDXJTZl$r?ttkq5@*THP4%s9pKQAtkr?+BU;>0cg@LZut+M+tc>Q3_HDRfZ*mnDP`6qRL7PkB@F+B|DJ=y5$D#f5NlBuj3RRC)$Xe7;r{^RBDDF{<!aOUyKT?%+I^SdN<EJqZ&xt+c6B(18J_JtqT#;qNt*~q-%KGcn0eiYY6mqtgcf6UlArUl{*J~#DKJECem)k(N!42d`_FqL1OsfXx!d2A$9aFf2d#!xnq<0TvSW&?GS}UVbYIrFC&u2%KR-%5<~y5hNVs;M84Fk}9tg#J&RnP0OT=?n=So~daJrZ<M;&aJ2kZPahpo<7%vQSIXk3^rFE5v6t9e%PviF%)?uTl7^Ru2JyzFtde|3~_JR1DlbsBT$1_c@>M$*XMEK5RYjScGsqQioRfr6@+<;8L~xoBxuzPb<uIhk%cH;qG^MFpQOG<2=AKcvqTprTt%w6^#P?N+gAabBRtO)i*A-<x&Uva(rpu6HMr*8pe-o$Ftms=z?qP|P=Xi^-~xe8Zxl-r)K$L|3gLErvT&<ZYMB?d^dDqj&2&jO0X8;qfm^JYC{-)~qQ%u!Q))eF$#F@9NCmdzP)We6KNKT_1i2J?|7>^UXfMz875sBAyoam4yTXA8ffLfJBSo4^?qU<|v|jibFfJst`wdnnuJdglcg@SKK?ppQ`lyIrTCx7H9I#u6+CRnsa;4djD#co3>uj4MTW&-_qrN6!$kKSyl*EpJv&o>Wpw#!n0zOf2%?sEh@U(2jT3KDeU=dR%>&>dh-p(z1h{6Je1w5E+<;EP1v4JGpX37d=UF6K4rVJcg}Ei)ikN%Q+IHEt%ELiuU2amd6S7bm`=^rmASsQ{(N6$w-Rq^z24Qd6GoKD<R=yFZja?s+bm}Xb&V?(?fv!a-D>uAqm+Gpw~l??C}Ll01>4;CTy%tv8rAi+?v<j+@%r-Ws@oVKMIDxlFp*{QPz$M10#{|;ok5V<Pe<{4!$oD9e_aME;k#!0a#sOY;U_nfNgWz;Go3byO&YLJ5CQN>lr0(ODK|*hywWo-t~M>XtHO;_i?CZCc)jH^Z*7;Y)!FT)U>x6NB-B2rmS*`Su@v(TBeVwLM;)Z1?%+J5LUq&okB)1+Uhlm7IAaH|fBrCY1(73Vvb?Pck8L<!u2Ggqo@{(;q`P+iGYX5@_6jx2@=IA4AC0m@(*Ag|9oGc@`|7o-MgOk~)gM)-cMH=EK<4shtcn@WZ}E4AqH2YNSE8;u*Uz)Fe0C1hhk~&cJa0`-0V4C(j+WXyVCZZsI$am=*G;h~H?0+6<Yo)d0%?wQq*SxKL^YN>U5X#ULYHOoRlO=Lh!=NDRf#W_BMtjK8~&wo6-X(4#uLJ-OIgT{)?Rf+lc+DypeCu{#AYVBg9Rb5fmtBl?A=qkezckGg4d#Jrg))bPPwV7$BJgP+=zgLW;55yC6>36YZ;mmb0ySBnATpq9*vt6WKkJ7xZa;$GG8^FLKR)l!PH(~$~Qobx$Jh58_ffpz`T{c#>N!6Y|OpYt;QXoyg&xx83({-{#l5;H%A%Y3?R3RZwEGI6E+-7cPzeVLT+Tan_rwABHPs9NpRLb(W^41(|ociVDK&Rxx57&x;+CRo32^tD^1-N`vn2aQXxn9bg^8XU#+sgzYR_ZC0{6N;!2A74H26Sl-Jc+kPhhUpW*dL4!TadgOh#uV`r(mRWJ_`YIl=|RpPxUjol3YkpwP{9Z&-|yhgyau%xupz8@-lsK56%P#bWFmfqWp?;dsd?*YGPJ!%Kr`v<x~{BYYt^ONiq+gJCU2FYa0Wn%%NL{QZ!&oh-^#S`VXT()?1Y&kq|NB_vq`^)9tj-&u?h;zB@KGwZRbah5qrX$#WwOn=XcFp|$i;51O_qR4r@IAn*Ww|rDENfWZ32KU~*$gIdM@KLE|Al6jCGWcl>m_7prEmG!UEafllm!2x7tq|GY8LzK^EFpU-Z0tj5LZ6b`K&&~Wv4#>**nM;;(~W~2f4y~<0zNU_S{xz4{Djp7fI3YWlu!1vh1meyRY&&JP$#CnnPINWy@;lYQy7Dr0Vq*+!Zw>GPpWqF6o)yt9u4_j(A_}Apa?1>LuK>=qt<xcHOU$NJgSH-1lVfsv*CKLk}-kdmow`zAr`}6=HvXIqF_(C`&0XiG)vvR)V8@ZoRms7Af+LT0!&TlO23M8WAj+=BtOUzN{Um0<e8dUJj<~d~)6ZePu~$Q~S2=ZJpUVu@oG3_b{A?roUuoXAKAF{-<_Mf&GhnQ1yv<>w5;8VnAj&sgL7NcpQIXkK>yMx0MCnxt6D=5@NymMgj%?xTtmdh!%RoXH(TsySp)W<HJFf_Vu{qMSapC5&Xow_*gc!OORjyeP$O|-1pKOL+|vIy1LVFUmahCE7rbQ=K5sfkE4HYoOp+f``h7WS>T%}{zeK%|2YNU1Buv#z7XJ5+})v--f3}t-?)B=|3(_Vn6@o0aQzs19dKB!>3gBZfn3Mlzbk`jQ>SY>t`~#2-yQXvbQBT26GS9Cp&Spy3^&#rLxBFxqj#bC$B{WYQZ8-Rx-w}ZtfL8_&OJxnKdO^?IM3<s9#cz?{XGeQd)Fk!O^xT7$T3NZMPhj_{u@w^_jA|4Sv%2NUn=v0F7Q1Q`^VA*Fj?m<n5r0B%RLduv@hRwP;6a?0Y2V|7c-s^A?!~8(TQj0`D%N{2B+h;+U#t($yrn2sX9)ocD3fG8#_hLefXkW7#V+OyG`aWI)|y|Fx4C)Aof5FHfVCtsk<uC`o<wU|Kd9QKZ^ybg>g}Roru)biP@({q4mn_1o9x^`n|pF_`^%F@4Jt*-+fyRQ`DOcFee`?p=j8=lqshN3PWaHdv#7WZmfYcLEI$~9;nuyc4>-kv);!y(|*FkGzmy^BwWqPb$xkY5%D@-@JAqDCcHd_V(PF>GGn7q0(81fErSWIhIdxAW3Nw@H%-e7KQ;E*sukCJY^u74u2@WEEpm{y+mo}@c`E5N!gJ^6X2U%W-%C8>C4pmN6ZwrI==%fe*ROd1{qFerpX1}_@1DGR^ZeQP-S{trwDI!~PhbD_=d0h}*t2N`ZSsHZaye(2sjRfM;<&gS=a;MP?YIIoZEJF<UoDsIe$8)_8h;x@tTbLNQ37wIml|MOg)pWd?AdKYCEe;fzDZR0R;Q%NYBDRfx3Y)7k(6!zGAPcCoW6`tQG%>ZT}#WOc&Gh+#_>Kj!tkH|GGlS)UUu^`_MO|<)pj*Nh&@`^&*1v?E*d!&L)m11bUyda&JJGo>=q(d*EOGeFS~=yYEt4mzE)SN{sMq_Dfd?=tBjuyg5G>Hkd1>3?;dr69^JVr)ypnx^|NJW_kkd;hTY9KkM%AEDLrn8u}7-9?@G##_occcU^(c_HxKX3+QXz>*;s7aDfe$A!w7Qc2GbT^l+VY@l~n7w-PLIK|Jt)AVNEwiI3-t!EZ;TyVXVeFzF2<A*VQIU(<qvxApdDGpXcTHby1$$tsW&UBfCH7ZTE!kn~G!a*xeqHFK0`vd$*Z3yP8^Pg-ABW6yxts^7UB0wtbWq^~o>l&UvAhy|`FTk#rh|xeK`FTl2;swHn#1-|1>Rp6Ao6#dvJm&-7P%;F%h+KM|Zw?C<BQpZH1aTu;9I<Y;+E{mwBlhV7jbXIXm^okni%<$gF%ClhBHq`v2e(;#t9=e{4!1K)Kfr;!KLG)sf2JI$TYnfX&^Hcb;hnvt8mlWfj0&@*MTFM{2X_Kv}!_Pldy`Tb$#2;dsfFfo1_8!vLr5J1wnQvB41-Bt&UlkVo(w%I%O?%w_F*~`Z9+j{v$pU|+Ufp2!$&%)f<ZS!|#`*BQ;w)~&}$m~ued$Ye8a`)FI<QJy%-7jsxnphN&c+oh$8JqF$^hOa~^+P>A*<Xbe4NcgiSi4)?9p1NHOeLt?S+>GevhOPrV4hP!%rs3E+H4{qx-*RZI1GK0cwUr*z^thkL@=k38ODxD6O*8s0Jb8h#;*B;x73_&(`!4!gU}D%I0{nZMlrH)gi0ZfVmAtWka0}lnIIS$Rtj!te1~LEv!FJte%&yc<`<^Z%vR_7x$3lALG)q!2`un`+JNa?f}+axI<vBpoKS(n_4<b*gTVCHNv%fT{S9??ljJAio!`ITS!bWWnq>ayu;Y)ntVi9)UavlCxHJDxcGNM^xo#q!*6@D~zoJI#%hXlg|EVDDrS<1G@-tt+@mpTVnS75BPm3GmqkPaRwj2KLpjCz3s#@SVz@c7Vlw3a8JJ<ijbA57x*4<OryXX4PK4dR@p9d!&_*2IZjo*&l_hZM_d@jE|`oP<dA9(xmL-V&s^Z8>3lpbdDdHv&zPy4@q<nboI_k;!?NJjt8`M0SU@RJRZx=%jzUhZAJ#?sU@e*5r`Cd-qnn~ax6I*n7I_Cv98FnM)z-;E#r@kMnx2c7=wTRtB~_t5&cF8Z{z@Bh1-KF>b<XIFhJLnlv;-@JPB;&6Mj-Djr#=J$84CvRH6pS(Fx9RI9!^6Jf-=f{VwCvxnzXR>h0tBq__uGT2F*Todo(eAWR;P+uQ_y50fRjc7g_j{lI{^s4QH-9~O$13UR^W%4~j$S=|^6t4_=N-TKef;M6$r#G9Mb@*iDrdi#QaI4=TX@n&)B)66<jc!^3z)Z^ta;P7PG;>soBNQr_A&;u@$77JIn8-A%UF5e-Onmc?x?bwLm>TD3;*~z?<oI^t7Upe^B#$Pe+#UZoerumfsKq6z}Q}0w%DtJSj~mD?h0-E{`nD<*MMLkr~iW$tj5Q-PUR|xwrKqk!3N~!#By)<2g!4{13>xyh+vt2*`0Yqp<jv;2G{P(zT5t_v*Hwpn-%PM4DdT1bGu+XhNuALd;DLKfC*f4I}Uvxm<P{ZV8KVCng{&{e}8<yp&uXgKiV%J9~d<8LN|l#|KZ&$yc-S=V$X5YfN;h4%z>YzsqZI#7<mq!{50~SzzLj)2<Ra46VC-SLXQ+*120Z6IEe$-9E6_l#;y|vkt=;YHw}G1NW;X9&4CyAP68^f8#yKf#BxF}1-6RWHH`cecq?^6-xU^s@1q19gdiJxY2bQc2>2vq(*z8Iu{cW1f$Lz9i?$yGCQ7~3as0>uq|&ag?*W4ONeDu205IkzaS}M(9rnC1Ky?r(2a%ITaS+E?2^NOs`VK_mkl6#w?8jaZl6UsSr_}NMB!Do?L6pW$5JoB3GqH=hBnAWENP4<%;5dPsI9!RBgp^PaC!vXbCrrX9NfWnPRp`aBgOvwhHT4p3;5tB{CIaJ00<{FOtSUsA6GIJNkWyHbTH+*R2h4bYnQ7otWx@bEC9xX@0HX(<lR&Y)52>UE0tG1bptVRP5O`Ro<0eTIK>}Xlc%hpFfk$~jq*0hc$g!vE0yF3w&`6*P*n<;>304&WG)H*tiKIL*6+z1hn82zM&-Y?#4(f<P2g{AZC|1jY2%%$W9#W=dIhX+&@M)7#oB%|7sUIdnHu5NF&<Z^C4MGSRYK&lS!YX9vhH>D?vOGVIXi92KJ`4?lgA6D;ECC9LK{xWPx?ud^L>3Jz!%E;PuyO+<#;mbNfeE`XIednppb$9lLhzl0fg8HQZVH9LlHgIQ1X!RC?ZfB{I7n!t3B?t#B!E<~4mCoUMT*XetR!|ZD)fUW^0+RTAas(Zu9_A+3#A22mcmRUC-M?M_F-8;2;HSokR)OPkXh(?E*M2f1mBp_qtpYLf=Y+7;HyG3NMHf*V=qDagQcQ$ap8Wxp{Tfc&{iXa{(=NjhT+mf9Qb#fV1CY#xFL)qh8v1%v1AXL4w4jex-e%7&GlgtF|_0QDVHINg#_VwbP5Ka5Gspct8h}<Aj1rNErI6>RTu|GV&*6{u<S5QLl5c#RZJFh5EQ2l6GbjYxnbgyY8r*`ya@Us=OLU4s)3{{U8N8qyf`(m83-e$gGGj>0MR0z`GHyhv<>%wBuUlB;++KX)`|FpzyWQ*57YvZ#6g&a?YoYF5Ti7tPeZTd18RjiI*Cw?V85`y&=c<13swd9cI7E`QYtG@=SKK~NFXI2UI^xBzHp7iz+wW3GENcDget<g??UhB06GvA91M|&at*<0h^0BP##d+uYILyl7-^IXh8j`OLL7)4@KCH+R~0~q4p?&GL8JpE#&C2jRiZZLq#FFl_C@e#Qb}SYXUtFkg}a-GK|gf@yiprWAOR!@@Xj^I0gX9~BH<OGAE^hqBMy~n>_I&Uu&}}aF#ypU+J<jqekh1Si8N-1a4Luz^e9&ZTMUDkd}bJY0qa<dMmG@geXJbv_6^(!hMZs;@EXEz!DxV#qfQ9nz|eez9B>C+`V2Qnf{8dRqM{3vj4ZG4Ttuc6Y=98nrcgU<+|aU-<kBQi4Inr{IiBa?E2uiKR2UGJOu0h3aCrod#Off55u5069u|!iq;X15H39Q3G9qk0v@ttoG;=vW69sb^$OV#P$xc9nwc0{2qzx=BhJu)n69&=PFsMNz$bg#UVH=PTMMte8UNSjDSw8(29vR2T$&qU<D_}kenFbAYflPzWh_ybGC{5P2i5n}5+=S5vl8mAV9b5;=lT^Vb2qUT`3Nzpj2=TCW#y9TSAc@1)0`_HOWhz4^(`4XqN^lj$2ongd^ye@J2NYFI*~V&xkUfH705gpM77*GHrh#;PgK!Dqdz6q^3u0FSHvqemQXIepgk(2n;zD#u+=Rd*b=9^JCS1r53owk3F4IZ^W{}GeHR-*IM}SW7!DU_t9XJ!<2m*{RaS_81J%N8T#W8C;6bB|lpk}y5q(<5@paQc2fQ!{yJV*tRGA0k83Ofc71T>Gi0QyB5LHe~+VPpZ~c0eD2?P1YmgIix93G+d=4n(TR>#%ux4}A+=5&eP?l9zPMY>zY^#ugF5P#K=!7lu#_4=_O}3uz&tMZnuc0{~qJ3qUN8KB&g@V6X>`O3HUqSO8Y4_JXv4FdB%oAQhkvgaru1Krj$9twOPz8$jj!50nO~2nuj^cu2?$1L-pMB5He92jajUgk}%{e1?Dc1Tze*0gs5lLKLnVfg3<HkU=!3ieccAw_Rok2767%2v86uVk|JMLHtI(1Mq`Q8DtaSEx3oSU-q~WVG$NV6ImECWgzqkPd%n|kcbsK`HWFid1BBLNf|&5k~6@O$PYkaunL9m@Vb;rg-Bt;FcWa*5$*UC1QIi*cU1hqGvL9C0YNETq-1agSAo5zP$GRoGbWcE5{{5&%0LD%;sgZpa40AYfZNImk-=d;0mvp?q8q2o2nS4@zyzK`Tv`a(A#4X?jrrsN5enQTAOLDnD2Q+aF+czaxiAmdT1c1Wf;`6o(ngf$(gBqcq!btm<cE}s<pl^B2}#mmVLJ>(YWN5b05d*jM|Nf&cj0g$gJwXlix8dA5rTyC2!tU?L|_CSutS)M%!;T2|4pfMfC%JbLIW%toFg?O-x24+;R8h4RO<z1GI}U1hZN}@sFPBm2un{1S+GEvoBV-jK#K4ZR0|&C7-S4-;2)SSWzG_U#)w%VppZt4xniaOMDh@p05cOsx~z?m<pB7oNFV?tL6{!}2Kit;FafNOT~lxdzd(L-gwaUYN%@4liY(_57fII;0gvNgGKNqlAn*?vD43mK7!D&THRQ6YL#YJYHOyc_67nVz7q|kMiMunUxu{#POi?B*DrU5D*_9~{_<&(e&6p@QWwAmuLDK+jAXi7qikNjABtR2^LSpJPCfb7_2qj=VQoJ&}U>&e#VE|!)V4k^6RF4!1RfnvC;V%e{FbhxI80bA@5ePd%6h(ZcH)47)?h-E$r@BHE3IwYRm%v@HdX&-NN1YSk8cZRH07J7Y^bSu0e#0^l=vWJ)K66Qw&cUn^il|&cU?H78Ql&z86fU0NURXS(E^rcoDqyYV%S{1zE?iowRgA+F7zkVR#iW3`h;CBC9KsktTN)U{Jq8g>B6YJXLm(26OH6O%1O%d!GKio&hW!yJb45NEhaR3pJ22_9)IkEq;xRKyO;jN%yFvtTWf~Y_HX=PiMjG%&)&WQGpaqDLTH;cO>tabDh_xw^cOq+dnSDdoMo<6}2F8#$7ezdx6#OET`r0Kr4qy$EL1}34Aw)EKFOqlav5J-$&FUJ$21t-dPXvl!iU10E66U82jXs<im<yU`wimOf-FZ}sE7FA70VKHuP(b$yIdwI8!XOB~kO~OKLrJ8_`B*u!F{Y+`CDySLMiB9(JdPP1feHMG?n%}GBZy+@9}#Phka^7kNdy3ox<dXiNFdx-ptVrw4$)#NP=*<fnGeH6>ICmn2c`ma0~W=MFd=JxxCjG2Y`_<ncj<btFrkV-3dk8t_+o_})4`ErfH_fIdBpk=gBXD*I)Miw`+!v$!#Y9(i+Lt{Pxdg7)Zw>qhls!#JS42G8TBzW*g>s`l0!fXGb?})J<um+;qDKra*wqflP>I(<qH=Cu3#(_A*>Nt9Z3{O-sj;RLl?p#{g5=_>r&-PM&Jg7C)+7}0z6{kAUvjV0PiDGA^pH|fz%OLSj!_E^I9AR5l#pchi!YTK0L_+F=BVZutdj)Tf(%lDp$%DSQX*Fly<1F;IYV(Fl^sIlyGt>ITC9|B*)s0+gB06A_mdZSp~r(k-y1h!hJxvE91NIx$Q&%L|DVRi#ZfvNzKToNu<CzG-8Bmpo56m4<R97d_<0og(RRn@E$8TRKh@Bs3n+bAWV1<%p>I<7)ip@0B~V|6dxvF+2=9}!qZ$j9T!JGhlCO0J*FKX9)dEIfy6e3(qf)v$RWuTU$8iU9+Grf3J?j(-W)ZG2qZoU;mL*~(wonnWWY>-^Dr>PhbcD&1Mwb68vzuIxWqolbRp{pP^Ey7d6-VZ$R>6lSj>~HP?(}@hdA73g06vVz)T!#PlOcNrDR9}Js1FNB;^(dt1J*e^yA!!<tcYv0_O6NyJwIycd}4T5uK*KrT}hfCJfgBYbkgYN=wKX&SpYZRw#)R*(YI@M_|cf1_JTn!7<kkpzd;S12r;MOZnh6@*j8WSokBDg#;>0@(A*Xxd<S-Ny9^Q<UANGgDwIC0=mx)S{J~akO=;mNP*7U7m|fT(OH>VFb;Nyyy0@&BIE|Klx8#%SQY}L!|iIHkP@W<N+2V_g<E?FkfV|L_+a<Hxy!BYzdt_U%}+L~E5ht#{|9pU+8KQ_&0euyR1NNQb9p#KC8NUOO<`~iE?shJ?9E-d*7}X(j%1geS71eUDECb)e?t?<U!WcN3**)60U)MdIE{YeWRbQI?Hz4Ff!c_SXd11=q|!i{=;>@=%Tuy|b)M2ic=vQDB7moK!MeSj09AQ9tCyhKl@^LwU&kVh`#J)Jv9JC7#01Jyz{?HII}U8|Fil&CpE?!*H_)*tSwbC)kQVBQkfy1v$b{N2OiZNxXpe*;1`3qFkxG^}WqfTwgpPhgX8{8gm*i!Sw>JbFq7@n`%+Z46BzNKk9<=3~RL7!PPjo~|%Gwcs@n1_E>C=@dX%*C*?Zfcv2DXjTS+vMDn06D}hUPsx)}yXH+vb1mSSU)!__9cWA_ndjNyCSZQ*H5qnb7cZy5vN;X2MoT5$MZ^HX}l#>8NQ%VivBpVl|qGb4YNAg$x-cvskQDi8NV9%{Ec17d{fb+9GT+!il4yh1e~NpnyUnoUn;5p*DfOeBU;aapZ07sce#hlr_H0tkp=s*HLPlh(WG4WA297rf(#dvk8P3+a?5KhoN*z?6AaDL!q=Nc5x7Spv;o$fs3>w^eVeoJ$M>2^g%DU+Xwx{fPILpG8ja-v1Xg8aqU|_HB|?o1SuyNY`|%(&4lsEHd9MMLzW6O)(EA{#KLn@Q6bB^nAo!HRu4h7n3V1lRZY*x_9UASb7Y$+m23x~`q*|rZi#INfV4QVO}#wDX2J~>+l2G^w&|P14nqkhtE4~pHkgS&_!`8d&1maa4_sepA83?fw(K5juoG3f8t$Y`YZd1Y*(XrsEU{eVBHCu07Y~o=3EC%-J|ZD*UAp?(mmnEd%|JW&8YTnVOf+`-5-25j`Wh)6+YB^(`WhkaFoej!4htQPn{4_TE`5!cLcwJKP<E={uvBfvr&ua2dYSg2585U-<&A(EzCwrCHmeS_FYSQ8iR~Ns(jm3Y)P$}!L*R7JHX#+;Hw;Y}+a`Fk!&uDNVZdcl!LW({x5J`P{U2;`VnzDW6bdPuGI1!J$;6yB)``*NTM2=_WR$=*6HPN{!nh^Ruo<YyqX~!_*}hEowp6rf->V*C>u#a&B&%Yw@-$zC!k#P;tBdUd+4MC~MZ&ZMDy})zWk<gBO$A&FBNC%S=^!CILQ$!{M;~N~DHRo)@|J&tT{BYWWHV9cL^E;JId?Z3*#tB*X;QVB-0BYjUsMkfUsMkXU)TrY7N;U0I7xu0FAG)hDosf&A~gxav4~2-aH0$eh7|coL`JAcBaIepB4rD7M4ApXaIlG@Q2GY)J0s4P$ZV46neammf`~9c?Gj|z1SXK#V!oBA$_+DSdso}U1zK+KouUPjjV&NxyY4P1LD7S>LyHLH0aL`b&GhHg55C0^@<8c^)k9*DgTP_OLI-*9EOwBG$btuXNNnmtK1e;Qs<cvKR6RsiRjE~?s4BHe6uYK8D!mJ#nwYPW;3_G<$Xbf@cB&B(6=grfvU&wg@=&2El~7=%q)(AWPBKIUCAn*dz2&J!;Pq2#<GMU4DzBeHn-}z{!YG<0{VG$-Q=K=3f?rV)c}EtPY0^n6Dnie(7)a^G6-}WROZwMhBA@58e6v}u$EWM%*Ss7Tb170-C;)65BDjdP0m}g`1(?_b!-WFh2!-TFbqex5!EXV9yr&2*Va{UOaRtBol9fV9NU`LiRPeeh8OWF96H4BRCFP`o$X!h|61yXbsfk2vM}oB{aXOF?9SICe1c5mMzB~zX3b`UdTZsTIM=+Kr`92^Bmuzp;;b^X|IHCA8?I#vrPpwtC)&zZP%AvL5*hV4iR<)h@*0L&_img9cR}%etR>y(0k;npy8thgW&)P{1<_s^JxpI8vj=nwk_U-=w%lh4q
```

**Final outcome: no new own-centred110 winner. The new completed results are the all-centres retained-target obstruction, two exact retargeted reference chambers, and their scoped ordinary-volume-centroid exclusions.**
