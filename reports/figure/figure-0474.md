# figure-0474

Historical AI scientific report · saved 2026-09-22 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Clear Willow 56 — C48 continuation: canonical metric gauge and exact stable-ring exclusion

## Outcome and source boundary

I read the continuation journal through EOF, including the literal immutable parent `figure-0469` with SHA-256 `6d665d17ac5bae24efaf715229c6f9e71cb5d5149171b095c18f6c15a66a202e`, and retained all earlier C48 materials supplied in this same chat. I found no conflict between the literal parent payload and the journal synopsis, and no required source was missing.

I did **not** obtain an own-centred strict110/weak000 C48 construction. I did obtain a new exact scoped elimination that is materially stronger than the inherited 309-shape count: the full joint shape+metric problem admits a one-scalar canonical metric gauge, and in that gauge the explicit mass-coupled polar prism yields sixteen low-degree vertical-edge reserve polynomials. Positivity on both eight-edge rings forces at least two strict stable facets and therefore eliminates every one of the 309 shadow systems in a relatively open full-dimensional chamber of the mass-closed family.

I also froze a new exact rational Euclidean C48 nonwinner/control with `V/E/F=10/24/16`, actual filled centroid zero, strict `(S,U,H)=(4,8,10)`, additional weak `000`. It is only a reusable control, not a record candidate.

## 1. Parent mass-closed normal form

Retain the parent normal form exactly. Let the planar octagon `S=conv(s_0,...,s_7)` have area centroid zero, let `c` be the planar base-centroid coordinate, and put `a=h_+>0`, `b=h_->0`. Then

`z_0=(b-a)/4`, `z_T=(3a+b)/4`, `z_D=-(a+3b)/4`,

`b_i=(c+s_i,z_0)`, `T=(-3c,z_T)`, `D=(-3c,z_D)`.

The actual filled-volume centroid is identically zero, and ordinary bipyramid incidence is exactly

`-4c in int(S)`.

For each CCW base edge let `u_i·s_i=u_i·s_{i+1}=1`, put `d_i=u_i·c` and

`w_i=1+4d_i>0`.

The same-centre raw polar `Q=K^o` is the explicit perspective prism

`q_i^+=(4a u_i/(3a+bw_i), 4w_i/(3a+bw_i))`,

`q_i^-=(4b u_i/(3b+aw_i), -4w_i/(3b+aw_i))`.

## 2. New exact theorem: global SPD freedom reduces to one scalar

Write a general SPD Gram matrix as

`G=[[M,r],[r^T,gamma]]`.

In the **joint shape+metric** problem, unlike a fixed-shape affine-orbit problem, we may make an invertible block-diagonal raw coordinate change preserving the horizontal base-plane/vertical-apex-line splitting. Choose real planar `C` with `C^T M C=I` and scale the vertical coordinate by `gamma^(-1/2)`. The transformed Gram matrix is

`[[I,v],[v^T,1]]`,

with

`|v|^2=r^T M^(-1)r/gamma<1`

by the Schur complement. A planar rotation and reflection send `v` to `(rho,0)` with `0<=rho<1`. Thus every real configuration in the full joint family is gauge-equivalent to

`G_rho=[[1,0,rho],[0,1,0],[rho,0,1]]`, `0<=rho<1`.

Area-centroid zero, crossing `-4c in int(S)`, ordinary incidence and the shadow-tree graph survive because the change is block diagonal and invertible. Hence the global shape+metric existence problem needs only one essential metric scalar rather than five projective SPD variables.

**Scope:** this does not reduce the five-dimensional metric cell of a fixed raw octagon, because the gauge transforms `S,c,a,b` as well. The parent's fixed-geometry formulation remains unchanged. The canonicalization may introduce algebraic coordinates, so rational endpoint recovery may still be performed in the original rational Gram representation.

## 3. New exact polar vertical-reserve theorem

Let

`delta=1-rho^2>0`, `u_i=(x_i,y_i)`,

`U_i^rho=x_i^2+delta*y_i^2`.

Then

`G_rho^(-1)=delta^(-1)[[1,0,-rho],[0,delta,0],[-rho,0,1]]`.

Exact expansion on the polar lateral edge `q_i^+--q_i^-` gives

`q_i^+ G_rho^(-1)(q_i^- - q_i^+)`

`= -16 w_i(a+b) R_i^+ / [delta(3a+bw_i)^2(3b+aw_i)]`,

where

`R_i^+ = a(a-b)U_i^rho + w_i(w_i+3) - rho*x_i*[a(2w_i+3)-b w_i]`.

Similarly

`q_i^- G_rho^(-1)(q_i^+ - q_i^-)`

`= -16 w_i(a+b) R_i^- / [delta(3a+bw_i)(3b+aw_i)^2]`,

where

`R_i^- = b(b-a)U_i^rho + w_i(w_i+3) - rho*x_i*[a w_i-b(2w_i+3)]`.

Every denominator is strictly positive.

### Double-ring exclusion

If `R_i^+>0` for all eight `i`, every top polar vertex has a strictly negative outgoing dot along its lateral edge. Choose a top-ring vertex of maximal `G_rho^(-1)`-norm. For either cyclic neighbor `q'`,

`q·G_rho^(-1)(q'-q)=(||q'||^2-||q||^2-||q'-q||^2)/2<0`.

Therefore that top-ring vertex is a strict polar U, so the physical body has a strict stable top facet. The identical argument applies to the bottom ring if every `R_i^->0`.

Consequently the exact family

`E_S={area-centroid(S)=0, -4c in int(S), a,b>0, 0<=rho<1, R_i^+>0 and R_i^->0 for every i}`

has `S>=2` and contains no strict110 body.

This is a relatively open full-dimensional chamber of the mass-closed family, not a numerical neighborhood or fixed-seed result. It eliminates **all 309** labelled shadow systems at once.

Therefore every strict110 survivor must obey the finite necessary disjunction

`(exists i: R_i^+<=0) OR (exists j: R_j^-<=0)`.

This reduces the stable side to at most sixteen low-degree reserve-failure branches before one even branches over a full polar U1 tree. Equality is retained as a boundary case rather than silently discarded.

For balanced heights `a=b=H`, the reserves factor exactly:

`R_i^+=(w_i+3)(w_i-H*rho*x_i)`,

`R_i^-=(w_i+3)(w_i+H*rho*x_i)`.

Hence `w_i>H|rho*x_i|` for all eight edges is an immediate exact `S>=2` exclusion.

## 4. Orthogonal slice `rho=0`

For a physically perpendicular apex line,

`R_i^+=a(a-b)|u_i|^2+w_i(w_i+3)`,

`R_i^-=b(b-a)|u_i|^2+w_i(w_i+3)`.

Thus:

- `a=b` implies both polar rings contain a strict U, hence **every equal-height orthogonal own-centred bipyramid has S>=2**. All 309 systems are excluded on this entire subfamily.
- If `a>b`, every top reserve is strictly positive, so at least one stable facet is incident with the taller/top apex.
- If `b>a`, the corresponding bottom statement holds.

For `a>b`, an S1 survivor therefore requires

`exists i: w_i(w_i+3) <= b(a-b)|u_i|^2`.

This is an exact short-side polar-escape gate. If the reverse strict inequality holds on all eight edges, the body lies in the double-ring exclusion chamber.

### Coupling to the apex gate

At `rho=0`, define

`L=h_{S+4c}(-3c)`,

`A_+=a(3a+b)/4`, `A_-=b(a+3b)/4`.

Then exactly

`T strict U <=> L<A_+`,

`D strict U <=> L<A_-`,

and

`A_+-A_-=3(a-b)(a+b)/4`.

Suppose `a>b`:

- `L<A_-`: both apices are strict U, so U1 is impossible.
- `L=A_-` or `L=A_+`: an apex is weak-U, so weak000 is impossible.
- `A_-<L<A_+`: top `T` is U and bottom `D` is not. Thus an apex-root U1 candidate must use the taller apex. Since a top stable facet is forced, an S1 candidate must also place its unique stable facet on the taller/top side, and it must satisfy the short-side reserve-failure inequality above.
- `L>A_+`: neither apex is U. Therefore all **159 apex-root** shadow systems are impossible; only base-root systems may survive.

Swap top/bottom when `b>a`.

These statements use the filled-centroid coupling and explicit same-centre polar. They do not resurrect any center-free obstruction refuted by the supplied strict110 off-centroid square bipyramid.

## 5. Effect on the 309 durable labelled systems

The immutable parent remains authoritative for the exact list: 159 apex-root marked shapes, 309 base-root marked shapes, union 309.

The new reductions are:

1. `E_S`: zero surviving systems, because `S>=2`.
2. Parent simultaneous-apex-U chamber: zero surviving systems, because `U>=2`.
3. `rho=0,a=b`: zero surviving systems.
4. `rho=0,a>b,L>A_+` or the dual case: all 159 apex-root systems eliminated; only the 309 base-root systems remain as necessary combinatorial candidates.
5. `rho=0,a>b,A_-<L<A_+`: the 159 apex-root abstract shapes remain possible, but the physical root is forced to the taller apex, the polar root is forced onto the taller ring, and at least one short-side edge must satisfy `w_i(w_i+3)<=b(a-b)|u_i|^2`.

No feasibility is claimed for any survivor.

## 6. Exact interior witness for the new stable exclusion

A literal rational canonical raw/Gram witness is

`S=[(3,0),(2,2),(0,3),(-2,2),(-3,0),(-2,-2),(0,-3),(2,-2)]`,

`c=(1/5,0)`, `a=101/100`, `b=1`, `rho=1/1000`.

`S` is strictly convex with minimum turn determinant `3`, area `24`, and area centroid exactly zero. The minimum ordinary crossing determinant for `-4c` is `22/5`.

Exact reserve minima are

`min R_i^+ = 328852786633/120000000000 > 0`,

`min R_i^- = 3282176267/1200000000 > 0`.

The two apex-U margins are instead both negative:

`a v_T-h_R(y_T)=-601629/2000000`,

`-b v_D-h_R(y_D)=-638211/2000000`.

Thus neither apex is U, while the new theorem still forces at least two stable facets. This proves the double-ring exclusion is not merely a reformulation of the two-apex-U chamber and persists with unequal heights and nonzero cross metric.

The exact canonical control itself audits as strict `S4/U8/H10`, weak000.

## 7. New exact rational Euclidean nonwinner

Using the same mass-closed raw geometry and the rational shear

`A=[[1,0,1/1000],[0,1,0],[0,0,1]]`

gives a literal rational Euclidean C48 body. Its vertices are

`0=(1279999/400000,0,-1/400)`
`1=(879999/400000,2,-1/400)`
`2=(79999/400000,3,-1/400)`
`3=(-720001/400000,2,-1/400)`
`4=(-1120001/400000,0,-1/400)`
`5=(-720001/400000,-2,-1/400)`
`6=(79999/400000,-3,-1/400)`
`7=(879999/400000,-2,-1/400)`
`8=(-239597/400000,0,403/400)`
`9=(-240401/400000,0,-401/400)`.

It is an ordinary octagonal bipyramid with `V/E/F=10/24/16`, volume `402/25`, and actual filled centroid `(0,0,0)`. The exact same-centre polar/mixed-edge audit gives

`U=[0,1,2,3,4,5,6,7]`,

four stable facets corresponding to polar U indices `[0,7,8,15]`,

`H=[0-1,1-2,2-3,3-4,4-5,5-6,6-7,7-0,8-0,9-0]`.

All equilibrium boundary tests are nonzero, so its complete class is strict `(S,U,H)=(4,8,10)`, additional weak `000`; Morse is `4+8-10=2`. This is a reusable nonwinner/control only.

## 8. Strongest next exact question

Do not repeat the 3003 inherited-apex coarsening or a generic affine scan. Start from the immutable labelled representatives, but in the joint shape search fix the canonical metric `G_rho`.

For every representative:

1. impose exact area-centroid zero and `-4c in int(S)`;
2. impose its nine physical shadow-tree arrows and root exits under `G_rho`;
3. impose the root-specific apex support gate;
4. branch first on one of the sixteen necessary reserve failures `R_i^+<=0` or `R_i^-<=0`; without one, the system is already excluded by `S>=2`;
5. on `rho=0`, apply the complete chamber partition above, including the 159 apex-root elimination and short-side escape gate;
6. only then construct the explicit polar prism and impose one polar U root plus positive escapes for all other polar vertices, clearing only denominators already known positive;
7. rationalize any surviving open cell and run the full maximal-complex, actual-mass, strict/additional-weak S/U/H and same-centre polar audit.

The sharpest theoretical subproblem is the orthogonal unequal-height apex-root chamber. For `a>b`, combine

`A_-<L<A_+`

with a labelled shadow representative and

`w_i(w_i+3)<=b(a-b)|u_i|^2`

for at least one short-side edge. A certificate that this is incompatible with area-centroid zero, crossing and the marked opposite-face shadow-depth witness would eliminate the entire orthogonal apex-root family.

For nonzero `rho`, the natural exact proof objects are the mandatory vertical-reserve failures together with the polar root inequalities; these low-degree systems are suitable for rational interval/Bernstein or Positivstellensatz/Farkas certificates.

No C48 own110 construction or universal C48 exclusion is claimed.

## 9. Recovery capsule

Parent dependency: immutable `figure-0469`, SHA-256 `6d665d17ac5bae24efaf715229c6f9e71cb5d5149171b095c18f6c15a66a202e`. Its embedded recovery remains the authority for the exact 309 representatives and parent mass-closed/polar source.

New source units:

- `VERIFY_C48_CANONICAL_METRIC_CHAMBERS.py`: 5741 bytes, SHA-256 `05df5601dc15b0ee5bef7f145dbb96c8d32de3136880292627db4a3d2dc62034`; CPython 3.13.5 + SymPy 1.14.0.
- `AUDIT_C48_RATIONAL_SHEAR_CONTROL.py`: 4346 bytes, SHA-256 `3447ef213a03c590dab5361844fc552b4cecfc539bf196314108cfb3ab1b8629`; CPython 3.13.5 standard library.

Decoder `RECOVER_C48_CLEAR_WILLOW56_CONT.py`: 4982 bytes, SHA-256 `24904ff690a17fb544a0619968f864a8871a249ab403123d98724e474e91c387`.

Commands:

`python -B -S RECOVER_C48_CLEAR_WILLOW56_CONT.py`

`python -B VERIFY_C48_CANONICAL_METRIC_CHAMBERS.py`

`python -B -S AUDIT_C48_RATIONAL_SHEAR_CONTROL.py`

Expected markers include `C48_CLEAR_WILLOW56_CONT_RECOVERY_PASS`, `C48_CANONICAL_METRIC_CHAMBERS_PASS`, `RATIONAL_DOUBLE_RING_WITNESS_PASS`, `RATIONAL_WITNESS_FULL_CLASS_S4_U8_H10_WEAK000_PASS`, and `C48_RATIONAL_SHEAR_CONTROL_V10_E24_F16_S4_U8_H10_WEAK000_PASS`.

Complete self-contained decoder:

```python
import base64,hashlib,json,lzma,pathlib
B85=(
'{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;3%*SL0tenh=#;cx16(qhW7m79hjN_Sq@J5udfG{FY^`S7&&S9?5?u?t~a>3ooyY!66J}uo>aP;B&dO*CeTWmZQNQ}'
'AM5+PzLl}#s@o@j+H?Z&B%Mxs9}5Y<<AzB0;<<oLPyY`!OIvnSi(yKwUyr8-&q3|Wf20Ne9G9z3jKkc0PV@InUg^6SQbPjXojK9V`<wtKh0p`mUEPkE{78+P'
'`R?()hbIw(Vjd`z8ghy6TF$0b8_|Lf7oF}@<Z78&==n<ROHM6X_lcQs%F*Z1)d7T#?o$9#D+{<GD~U_&2hI^f<3Ke&44|zM;`_)jGxg8vPFT~s2?ED5tRfRJ'
'LdTW6!6y@xh6;l@QEM~kWU`VLTY6Wn*6o~6J$f&f<Ai*-JM-*vKm9aNH#}}VB<ZNm!t56^h$HwWfg0fNjurJlHdwhHzsuu4M=0c>LlCi@g%%JfJ(=rgX5*}w'
'NVg}KsywHGz^a1fcAnGC7F?FT_EwNst`9irhw)_FoBOKVWs&-#lGQ1k*(KZoQ9L+z%grOGx5TG1@)|QE6aL&X*ZLurU#>=~lj5BAy2L|#)dXg)29HuEy&bu7'
'Q}+eT2>s#c)?EVaMnHs|xFPnvlKqB))4wR|A`xvoINERoD6YsJ-f|-KG7PmAigGZV)4JFS#7d;Ewlh_CdhS5b6{%thZtu54a(YaVW$E1IZXm*ux2_3W`W>o0'
'83_B?4_pxC68!Txll+VV|Kiq^JuZDg45V2%fDsK_hoysLEQ#J$`f*$RMHc+(qyC(21uvlsl91q;G+x%Z33=ae9pX0{(fC9DqZXC?U={GzVz?m9<;({k!gytH'
'mKoMPJQ_TBqbFs8A@=*9J#cwA<KEq={;g@5Q&KC$M|z9VZ#}<PP-0|custbdiITcl&YM5%I21e4PS*1tmdze|B(8?EVB)q*>!l#`r}gnnrYszmwyTzb<w{ok'
'Zef5#)R*dy)SyK4jh1O(Zh&KFG<L$H;kkNWycR(IpHFvupL_o#o&{-;#Ztpdaaa^Qr-zl5Th7KSv5IhtS%4bwTxO7!o}biKdw8UHR-!2&GU);v?atv#xS!tF'
'M%yFu&yz&*(AkiA_W!*9pfwzrf4lp^DbJ5`)wb;-Finx>Zf_T__8x-&p)G*ATCwR{%9f!LGek+7gM|?3_&&x-=SAe1bF$a*pp+Q)CKy&q3j_pp>JQmL16vCA'
'dU%IlEy7>#X5cSYjNnrImZ&+hcL?nGUL&*io?{@l@Sj>&KX$Sx#O}p?(B{L6{URjpE8fv6e|u-HXJAKS<SS7hg=;$CE5i$_%o(mIFCiHjp=vI7U)TA6$3oZ8'
'N3BwLv8j@zF6AA<=3*rx46E<^V9F*4)QFwhTDU7Fu?U5-K#(0)z^)|ruy?~E^yRu2B9w#D`>vbkeU8^aAVb#ztE(#Ri4HhjO^RhDl2!UdMnEi;2-Rv8h#2Q_'
'HN295mIh?7r^K1;I^2XztJL`A*?R-)4w&39*;y0V?egUF0i9At@O5KVjeyK}aBhyCpT*6p)XdnlCO3q5j6>pwOY!`W0>8wagFHzizu`(Nh>~pLEcw486vOC-'
'2kll%-7#^C0{X($SH>uz)&vkECq{Lc-;&OHEhxW5gRVUJL+x@-&>ub-i8iko{KavEO2cyotj-nHZ-W|Y8lf`?5|K=12D)*mleC6#!K`1yGir6E`@5&1c%L;('
'sHvFSi}qaJ_kI2<B6d_XzUWBy2M%8(PQIL-TFofBp}dBjxi3a@4kLvG3YpYW6@O4uiT|?CH&{9ufh<8%Nh@N>14Rp3yHW&`qnhRFY_N35<?sg-`&d2`hzYU^'
'aW?v{T`Y%K27RLSGlIZi$Mh&7Vjx+%X>l~yFeQv7|1LYb_Fc7z917qFh9OcDS<TU+$v30t8tB2+vFGZu5wzw+^a*bIJ951wmg8$UcUtDU2gbZqj<MgU%X-=c'
'w_EV|Ps(GdrDn8Cb)uq;1T-{&9Z$%<b`2imnNdb>@7u6Ub^|2F4HC9-oF;HV?Zwf*zZ~?!kAIx<*L}4h|KN54O~(H*DV781QMD*N+{%&DT=Jy&x{9+?>Nb7A'
'hI?jbhsH(*)R2j}SLl+xXdGVNS@w|=#mz~L$Yjx5xB|QbHm~&Vf)=67KBS1$d*#%qm*Kw#PfyM6Xcai)P1oZ55g8l?GaluYGE&}1o<)|)>dkVQ<2h-F)bBy&'
'ZVREdCSbz&T2JKanV+qU_(@22TMfEpXDJik`gCsH$>g|vkXMt{nIb`4J8{Lf$V*p0jHz7QN7SDRRd~?6Wl@du33YUV&P1kedK$b2Q7)Cb6K;b4M<rx4YViAU'
'e?e4XTxG~Y1x#N3GR*Nt|1PcLGC(>dnPC-KW~IMSfiVNZScMr;1>DUOD2!S>I#3koH{3nN`@R7K6w${ujsaD$DeR;Qg9s8lQeKN-rW=7RI`+J`6$H!3$BbC-'
'p?;qT1L8J^N#4MGGvnNYI;V$foj!0Tw)Dbx$y^Em@mOEd>y%%P?r&gP>vA7lODHDSh`iV0b_q@Icjl|4`6{%K9{|kvwmHTe=o5b(M<jfSp!@#1oo4~#Hmvbz'
'v4yKHW=3VuLuIM!dV8_;`maE5OBLq5kHj6W|4U9?jxMG(`*DX?2qoONRkPi_v$<JKSSzvI;hieqhv675{a9`b$lDi9i1E1rsVuOXM6zuDIct@vRbFmXuI<zV'
'm`Q{prWhj!YzB!mTKK^IOaF=MJekFTa(OqmxjgX?ZKP-^BUdS5$+_LrcQai(qhRE#lAL@gOnxUT?8#_NXBwG@$!(A0tCfG;%Wzw<=ETjk{KSVvn2TVbn-j~-'
'1ltoVg8)R2M0!rKtXoXR<0%8d@0!Tj?OcbrUQ7f0OHMV!agHYR5ni?02{#^4+DfF9Ik;;piAx>5VNgQGCm9k9GNY_fKF4wQ<k*3-yf$1;0;eIqW?nZK$l>C0'
'9OZ@gMJ=DoT|X-Dsc11hN28H8EiuFDvH(1jNZ@K_YNMEBnr!npg60(8%5&u-GX3-G-0Cr;YJO$!nGlz6Z-wU{#vcNPk}DtAsELl0M-$vyc9}(l$E~Soz0IUR'
'y>*ec)))`?cc>{yud8?R3F2=ZLONpAN3?mtfoJS&u46w(Kk|b91q=RoHw7^db?_X&0l+xn$pDvudE9iYC$YHgA?p<#pKMj%!qC~ShA<`K1jx;&Xx;M0^1M)('
'iYHFkqso-l-b^%$Pv{;e+H6H@#g^nS?Lf0)80Uo~dYZevFP-U*n4z9(ny*rJZvRbW`NcD}gn)=iNm}%ratWZAVYWhVm#yFTizhh+Bo%uJU^;@95e{seo%Bzy'
's^+rpu_(WM(9^RoVvEJ#eq!pqb3<G?SLAM7H58;Rsx;d=u^Z7>PWh~K3>up2qLhfUhVR{FkzHHc9|-g{82oyXQWBuZMv(es-A}4}yO`?U?m5|&Ke_4b@q9S{'
'DruUZZ|NdzMmYnfFn<GBcA&OGvB5n0WXe|Pg@+0{FO_<Tok~00kT+{v9}H?}ADs-~!2r=cV8EEdaYkEV*6g6%lZ=SLLZquT@?84Eh}wAv5`%#RjFZ6h1NpTs'
'hM8CD`ou~Q6E~dF)##@>-AoT-)faM=GZTdBN^v!wQAss;^}qkq=;hKAUOnY3PP))_OO1MBnn&!Nl2o$jB-SyLDixya&B5>(n-B_6#2(e?id4kWwxdCz$WHM3'
'G}>!kk!2D(+%b!}6vSpA^pH$(2jHU1<3FD9o4^(yDzbA1ZvsSZc}x}BU$0+IXrFs?c-bum;?=6vQz}^j1KgqSeMk|?i31>OIWL<&6Zl53LIl?26V3m<ay#@m'
'ct|!N5Z`1|^{Y?ZY;>8CoRk4|vWn@49KKgxyWIGnv5R31NUcH4FYG#0MY$f^CUr7C@sX3s=Vh5G>MNfO%}rDm#)w};(%gcij_7F+vC?6ZxLhtDF$<UdT>S@l'
'48)^v%L*UdK>v;s?UZpi5JrPYNlR>Ae;(@#6>jF}A<Dt$gPuR)7(>+w;?sPu20QwkPIJ62YQB;}Z$v9qA}`@vb>=klZVK`Q|H8lt0{46;>BJipaso+cB4Vj%'
'2#gtFul(oWC(r6lpia+UEmf<PVI-!yw^g=2{yBMvInb2+hCI^AjjBg=0hk_yGi{EA09Vk@pPRTpywiR?(XbVWd`q-v`b%0-npqxMHtyt0CAQ5}+pLC|;y~UU'
'*l(MJRt@WSa6dQi2875%bf2DEkT^u>tmU}_4Z2{(@RM_-8qm$lW$EW-*~J7=JUmdkQcZ}x`r#5q(RpYM3b&J(XwkubJ#V6&vEei&@Kcb4xQAWu&HOY&b&o{d'
'V7eAX4dS03L}`^s{n$w3D8*vsMzQ$hc`%{`FL5N_FuBJ{&)G~~0Y4!k6C~vWH~j9JQoD-$&sTxZ*!lcU00000k$!;*7JPw000G?^u~7g3cR3Z0vBYQl0ssI2'
'00dcD'
)
raw=lzma.decompress(base64.b85decode(B85.encode()))
d=json.loads(raw)
expected={'VERIFY_C48_CANONICAL_METRIC_CHAMBERS.py': (5741, '05df5601dc15b0ee5bef7f145dbb96c8d32de3136880292627db4a3d2dc62034'), 'AUDIT_C48_RATIONAL_SHEAR_CONTROL.py': (4346, '3447ef213a03c590dab5361844fc552b4cecfc539bf196314108cfb3ab1b8629')}
for n,s in d.items():
    b=s.encode()
    assert (len(b),hashlib.sha256(b).hexdigest())==expected[n]
    pathlib.Path(n).write_bytes(b)
print("C48_CLEAR_WILLOW56_CONT_RECOVERY_PASS")
```

No sandbox file is required to reproduce any new exact claim in this handoff.
