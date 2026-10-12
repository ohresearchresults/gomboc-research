# figure-0410

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Bright Harbor 81 — physical mass realization from literal C252 G6/G8

Branch: `[internal-source-reference]`.

**Status: nonterminal. No own110 construction and no improvement of the accepted own110 record.**

## Strongest results

I obtained two substantive results rather than another free-center certificate.

**First, an exact convex-addition obstruction, independent of vertex count.** Neither delivered body can be filled out to centroid zero while retaining its old stable supporting plane and its old unstable pole as the unique unstable vertex. The certificate also excludes a small, explicitly quantified ball of possible own centroids.

**Second, a genuine finite removal construction.** Each parent has a unique one-halfspace cut whose actual uniform-volume centroid is exactly zero. I isolated and certified that cut using rational intervals. Both resulting algebraic bodies have **V=52, E=112, F=62, C=224; own strict222, weak000**, not110. Their two unstable vertices and two saddles are all on the new30-gon's boundary. Rational cuts and lower-arithmetic companions are also preserved.

Thus actual mass closure is achieved by changing the filled shape, but this simplest successful mass controller introduces a second stable basin and leaves two unstable peaks. The useful new entrance is a localized cap-replacement problem, not continued origin-centered ballast addition to the original body.

## Input authority

I read the complete delivered journal and both supplied source files. The literal G6/G8 rows, not similarly named mutable checkpoints, are the parents. The source explicitly distinguishes their own152538 census from reference110 and describes its original replay as one auditor, not an independent pair. I independently re-established the parent hulls, mass and censuses by exhaustive exact supporting-triple enumeration. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

The later source correction is respected. No missing scout, external archive, research connector or undeclared checkpoint is used. Earlier unfinished numerical `.npy` scratch was absent after runtime replacement; it is not a dependency or a claimed successor here. :contentReference[oaicite:2]{index=2}

Exact input identities, with no trailing newline:

| Input | Bytes | SHA-256 |
|---|---:|---|
| G6.json | 1144 | `63ead46daff5c7c9cd4344699cbe551a7e92b2a2851703aacfa55eb1621b6aa5` |
| G8.json | 1422 | `b2dc9c6ab7a6474932a5fd045ecc3a601dc9a2d6b318ad71a79bc45a8f985038` |

Both parents have V44/E126/F84, own strict(15,25,38), reference strict(1,1,0), weak(0,0,0), and no zero primitive mechanical predicates. Reference U is input0 and reference S is the triangle with input set {5,38,44}. Their common centered denominator lengths are85 and112 bits. The recovery capsule contains all46 rows of each literal input, in full.

## 1. Convex-addition obstruction

### Statement and scope

Let K be either literal parent, u its input0, and R=|u|. Let z(x)=n·x be the near-unit rational coordinate normal to the old stable face, with d=z(p5). There is **no convex body L** satisfying

`K ⊆ L ⊆ B(0,R) ∩ {z≤d}`

whose uniform-volume centroid is0. No restriction on the number of added vertices, unchanged contacts, or a local parameter chart is used.

For a polyhedron, retaining u as the unique unstable vertex relative to0 forces L⊆B(0,R): any maximum-radius vertex v is strictly unstable, since for every other vertex w,

`v·(w−v) ≤ −|w−v|²/2 < 0`.

Consequently this excludes arbitrary convex ballast addition preserving the old U pole and old S supporting plane. It does **not** exclude deletions, moving that plane, changing the U pole, or a sufficiently displaced own centroid. It is not an exclusion of the C252 family or of E<311 bodies.

### Exact separating moment certificate

The normal is n=N/L0, with L0=floor(sqrt(N·N)), so η=n·n≥1:

| Parent | N | L0 |
|---|---|---:|
| G6 | (205212026473,−15672289746,−23677434167) | 207167124234 |
| G8 | (2736161967821631,−208967176792622,−315697634523939) | 2762230003380281 |

Set a=−min_K z. The minimum is attained at **input21**. Use the same exact constants for both parents:

`b=−7/25`, `t=1007/5000`, `Π=355/113 > π`.

Write C_L(s)=area(L∩{z=s})/|n| and

`α = sup_{0≤s≤d} C_L(s)/(s+a)²`.

The cone from input21 to any positive section gives C_L(s)≥α(s+a)² for b≤s≤0. The definition of α gives C_L(s)≤α(s+a)² for0≤s≤t. The outer ball gives C_L(s)≤Π(R²−s²/η) for t≤s≤d. Retaining K implies that the negative moment below b is at most

`m_b = ∫_{K∩{z≤b}} z dx`.

With `F(s)=s⁴/4+2as³/3+a²s²/2`, these inequalities yield

`∫_L z dx ≤ A + αB`,

where

`B=F(t)−F(b)`

and

`A=m_b + Π[R²(d²−t²)/2 − (d⁴−t⁴)/(4η)]`.

The executable certificate proves, in exact rational arithmetic, **B<0 and A<−471/250000** for both inputs. These decimals describe exact results, not acceptance tolerances:

| Parent | m_b | A | B |
|---|---:|---:|---:|
| G6 | −0.2141291879407715 | −0.00188447899155324 | −0.00000344909748827 |
| G8 | −0.2141291549106993 | −0.00188439985588192 | −0.00000344592836654 |

The simpler outer-ball/positive-cap bound without the cone is positive, about0.017853, and proves nothing. Convexity of the added material is the decisive extra restriction.

The low-slice moment was computed twice and matched exactly: by a tetrahedral divided-difference formula, and independently by explicit rational clipping followed by positive tetrahedral integration about an interior point. The auxiliary clipped region has V58/E110/F54 and112 positive tetrahedra; it is an integration substrate, not a110 candidate.

For a positive tetrahedron of volume V_T and vertex heights h_i, summing only over h_i<b, the formulas are

`V_low = V_T Σ (b−h_i)³ / ∏_{j≠i}(h_j−h_i)`

and

`M_low = V_T Σ [b(b−h_i)³ − (b−h_i)⁴/4] / ∏_{j≠i}(h_j−h_i)`.

All active heights are checked distinct. The rational π bound is checked with alternating arctangent sums and Machin's identity,16atan(1/5)−4atan(1/239)=π.

### Certified escape requirements

The same certificate yields the following narrowly scoped diagnostics.

* With additions and the same upper plane, a new outer radius r must satisfy `r² ≥ 2[−m_b/Π+(d⁴−t⁴)/(4η)]/(d²−t²)`. The necessary r/R is approximately1.004054. In particular **a0.4% radius increase is still insufficient** under these assumptions. This is necessary, not sufficient.
* With the old radius, allowing the parallel upper plane to move outward by **7/5000 in z-coordinate** remains insufficient. This says nothing about rotating it or changing multiple parts of the body.
* With removals allowed but input21 retained, a zero-centroid body under the same ball/plane bounds must remove low-slice negative first moment at least−A. Hence low-slice removed volume must be at least−A/a: about **0.14250% of the parent's total volume**. Removing input21 itself leaves this cone argument's scope.
* Even allowing the actual centroid c to move, **|c|≤1/3000 is excluded** for addition-only bodies retaining the plane and retaining input0 as their unique unstable vertex relative to c. Such a body lies in B(0,R+2|c|). Using exact upper bounds R<137/125 and |n|<1000001/1000000, the certificate proves the separating moment remains more negative than any possible V n·c throughout that closed centroid ball.

## 2. Genuine finite removal and exactly centered algebraic nonwinners

I used the physical halfspace family

`K(q)=K∩{q·x≤1}`,

not a density change. Let M(q)=∫_{K(q)}x dx. The convex function

`Φ(q)=∫_K max(0,1−q·x) dx`

has gradient−M(q), with Hessian

`H(q)=∫_{K∩{q·x=1}} xxᵀ/|q| dA`.

Numerical Newton/Armijo solves used q_initial=(−3,0,0), at most60 iterations, centroid tolerance10⁻13, Armijo coefficient10⁻4, and backtracking by powers of1/2 with at most50 trials. The complete discovery unit is included, but the final centering and census claims do not depend on its floating residual.

### Rational bodies, separately audited

The pinned rational controls are

`q_G6 = (−286112322,−83717249,58027896)/10⁸`,

`q_G8 = (−286112203,−83717200,58027845)/10⁸`.

Their exact uniformly filled hulls both have **V52/E112/F62/C224, own strict222, weak000, zero primitive counts000**. Their faces are50 triangles,11 quadrilaterals and one30-gon. There are100 positive centered integration tetrahedra. Their exact centroids are reconstructed as rationals by the capsule; approximate values are

G6: `(−2.6363550e−10, 1.2267070e−10, 3.5627125e−11)`;
G8: `(−2.2005843e−10, −6.3515873e−11, −8.3164493e−11)`.

**These rational centroids are not asserted to be exactly zero.** Their own-centroid222 census is exact. They remove approximately26.82593% and26.82591% of the respective original volumes. The old U input0 and cone apex input21 are removed, so the additive obstruction does not apply.

The new exact implementation and the separately executed delivered auditor agree on actual maximal face sets, V/E/F, volume, exact centroid, and complete strict/weak census. The only patch to the supplied auditor changes floating nomination from integer-to-float-before-division to rational-to-float-after-division, avoiding overflow at the large common grid. Exact predicates are unchanged. The complete original auditor, precise patching driver and comparison assertions are inside the capsule. :contentReference[oaicite:3]{index=3}

### Exactly zero-centroid bodies

Starting from each pinned rational q, the certifier performs three exact Newton steps, rounding each new control to grid10⁴⁰. Let q_c be the resulting control. It certifies a unique zero of M in

`|q_i−q_c,i|≤10⁻35`.

The integer numerators of q_c on grid10⁴⁰ are:

G6:
`[−28611232248575408074295619181278652377849, −8371724867635280395964376063642653124071, 5802789597934782868746853801278358858995]`.

G8:
`[−28611220339495819998986259537190608336600, −8371720011925369593394910016079261183995, 5802784495955221747417713092045386416557]`.

All original vertex/plane signs remain those of the pinned rational cut throughout each box. With R_H=H(q_c)⁻¹, rational interval arithmetic proves q↦q+R_H M(q) is a strict self-map of the box, with maximum derivative row norm below10⁻25 and center displacement below10⁻38. Contraction therefore gives an actual unique root, not merely a small residual. The interval Hessian is checked positive definite.

Across each entire isolating box, **all896 primitive S/U/H signs are certified nonzero**. The exactly centered bodies have strict222/weak000 on the actual V52/E112/F62 maximal complex. Their algebraic control is defined by the isolated root, not by treating the displayed rational midpoint as that root.

There is also a **global uniqueness statement for this particular centering operation**. Φ is convex. At an active full two-dimensional cut facet H is positive definite: no nonzero homogeneous linear form vanishes on that entire affine plane q·x=1. Two zeros of M would force a flat interval of minima of Φ, contradicting positive definiteness near the certified root. Hence this is the only one-halfspace cut of the respective parent with centroid exactly0. That unique centering cut is222, not110.

This does not exclude a one-cut own110 body whose centroid is elsewhere, nor multiple cuts or changed outer geometry. A separate deterministic6000-proposal numerical one-cut scout found no S+U<4; that finite observation is not used in either proof.

### Location of the remaining defects

Using the capsule's fixed cut-vertex labels, both rational and algebraic bodies have U vertices18 and22, on original edges **(32,36)** and **(11,12)**. The saddles are cut-boundary edges(0,1) and(30,32), whose endpoints come respectively from original edge pairs **(6,23)/(6,25)** and **(33,43)/(33,41)**. The stable facets are the original {5,38,44} triangle and the new30-gon.

Thus the finite cut concentrates both unstable peaks and both saddles on one cap boundary, while the extra stable equilibrium lies in the cap's interior. This is a more localized physical continuation entrance than the original own152538 body.

## 3. Lower-arithmetic exact companions

The rational cuts have common raw/centered denominator lengths1295/2638 bits for G6 and1518/3090 bits for G8. I preserved two arithmetic-reduction modes, all with exact fresh own-centroid audits:

**R:** round every coordinate to the specified grid, using exact rational ties-to-even.

**P:** retain every surviving original vertex; for each new cut vertex round y,z, then solve x exactly from the pinned cut plane. This keeps the large cap planar but permits changes to adjacent old faces.

| Mode/grid | V/E/F, both parents | Own strict S/U/H | Centered denominator bits, G6/G8 |
|---|---|---|---|
| R/10³ | 50/143/95 | 10/12/20 | 45/45 |
| R/10⁴ | 50/144/96 | 6/7/11 | 57/57 |
| R/10⁵ | 51/147/98 | 2/2/2 | 70/71 |
| R/10⁶ | 52/150/100 | 2/2/2 | 85/85 |
| R/10⁸ | 52/150/100 | 2/2/2 | 111/111 |
| P/10³ | 47/113/68 | 5/4/7 | 139/168 |
| P/10⁴ | 47/113/68 | 3/3/4 | 139/168 |
| P/10⁵ | 51/121/72 | 2/2/2 | 139/168 |
| P/10⁶ | 52/123/73 | 2/2/2 | 139/168 |

All18 bodies have weak000 and no zero primitive mechanical predicates. G6/G8 R/10³ and R/10⁴ point sets coincide; the parents and finer variants remain distinct. Coarse rounding's additional equilibria are retained as controls, not silently discarded.

The useful tradeoff is **G6 P/10⁵: C242/E121 with139-bit centered denominator**, versus **G6 R/10⁵: C294/E147 with70-bit centered denominator**. Neither is a110 record. Complete deterministic generators and exact inputs are included.

## Verification status and continuation

All claimed exact calculations were executed. I decoded the capsule into a fresh directory and completed its source-only replay, including the optional separate audit and numerical discovery. Terminal output was:

`BH81_COLD_EXACT_REPLAY_PASS 11 42`

`BH81_SECOND_AUDIT_AND_FINITE_DISCOVERY_REPLAY_PASS`.

The algebraic root has one complete rational-interval certification implementation; I do not describe it as having a separately developed second interval-root checker. The rational cut bodies have the two separately executed geometry/mass/census implementations described above. None is an own110 endpoint.

The next constructive question is whether the new30-gon can be replaced by a genuinely nonplanar convex cap that removes its stable basin and gives one of its two boundary peaks a strict escape toward the other, while re-solving actual volume balance. V52 leaves53 extra vertices before the assignment's V≤105 sufficient bound. The important freedoms are coupled cap geometry, actual removal/addition of material and root turnover—not more ballast inside the original fixed-pole/fixed-plane envelope. A two-cut or cut-plus-cap family is a concrete next architecture. The uniqueness result explains why merely retuning the three parameters of the one-cut zero-centroid controller cannot change its centered222 census.

## Self-contained recovery capsule

The executable block below contains, losslessly, **both complete literal46-row inputs and every retained source unit**, including all helpers, the original supplied auditor, exact patch driver, numerical discovery settings, finite scout and full byte/hash manifest. It is not a reference to a missing parent or a hash-only handoff. Running it expands readable source files and reconstructs all42 primary exact files. Its encoded content consists only of text.

Save the entire block as `RECOVER_BH81.py` and run:

`python RECOVER_BH81.py --out BH81_RECOVERY`

`python RECOVER_BH81.py --out BH81_RECOVERY --extras`

The critical replay uses Python3.13.5's standard library only. `--extras` additionally requires NumPy2.3.5 and SciPy1.17.0 and pins OpenBLAS/OMP threads to1. No network is used. All construction and verification code is included, not just the decoder.

Decoded text archive:48047 bytes, SHA-256 `4e33784b1a78cb7f671fd73f0adec08f3546553bde5dd8cd51763fcae69faab0`. Base85 text:21885 characters. Executable:23069 bytes, SHA-256 `71ec7c84717184ee8c1299f45a14e2c4ee2c4a83a4096a26c8264dd9c46b3eeb`.

Principal exact output receipts:

| File | Bytes | SHA-256 |
|---|---:|---|
| G6_BOUND.json | 14697 | `a35751db14d2de4084339c6f46b2f57f7fedd3173fb2dcbb9e52a0f57ba8f4b7` |
| G8_BOUND.json | 19774 | `2c04848a90dccf559dfd31166747b9e73a0cf32e103b0eb352cc1b2ead09fb51` |
| G6_CUT_EXACT.json | 14382 | `98f0e3590aff85d884a1d84e68c5dc4a47e582014c74876f670637b863f68e2f` |
| G8_CUT_EXACT.json | 16478 | `ed49b5b3ff92cd3724e291bfb0751848efc1dc1a52a306557cef648196f52252` |
| G6_CUT_ROOT_CERT.json | 1087 | `ad6d05316a59ac658ece570af9685c94197ac88dd1a5f51b98e0dc1b908309eb` |
| G8_CUT_ROOT_CERT.json | 1082 | `04c8c0da4d0c6e377b691ea2d0724e30f5334eba3838d11724f11a108ae0601f` |

Optional convenience copies: [executable capsule](sandbox:/mnt/data/RECOVER_BH81.py) and [complete recovery bundle](sandbox:/mnt/data/BH81_COMPLETE_RECOVERY.zip). The inline capsule is sufficient without either link.

```python
"""BH81 self-contained source capsule: exact inputs plus every retained source unit.
Python 3.13.5, standard library. Optional --extras requires NumPy2.3.5/SciPy1.17.0.
No network, research connector, unlisted checkpoint, or downloaded helper is used.
"""
import argparse,base64,hashlib,json,pathlib,subprocess,sys,zlib
DATA = """
c-rN?33D4cvM%~pczWUnSyYj#okh{r(QfZ|Y}w;&<~*9gs0Ag_qDYEG$&@<!zuzwtKrJLCxzF7D&VBLJZL)~Ml1L<S0TPKnetGe)
r_Vl5zfPZidH&{ee|7uI$uHmdzZcs$-Lz(ljW`qQUb<Yav)Llvh}QY_e15$AvFP0_=hv5_C9bY#^I5W<U0=51>uk2^e_Om+tgbgF
tv}Azv+Sg`S{Ad->_+I?Or+qkIBAW?_%_wQiP`V>Cx4Dw%hhJKT*UL%TI6Ca7O9w~0!7!~7PF$YIbRFWTE{9+v02X+X9enRt<G<Y
S&Fpl#cWgbTc6U|>b6x}uU7M!C|Y@(icM>=yrh1haM5~y`u0Bo?Ta`)*Xbf_UB=tlC2FDkW-Ff0xr*g_gLcqNI?D*8!fd7UWr6%6
I}@#Vk+p8bdLy>2`D}4fn5g!8F4nDddA->1>k<vi^^CfM0uqDqT2R?pK114%+2*_@>d41?q+N>5ECsNi&w&H{zgz(ITajK<MU3|r
vYan7vvvCZb8GWsiSn6P349O$l%qg-Il92)C3OjPpRM9`fsTGJmJ1V|-<*G2<m=^SD_;W$#*@nXQYEzFqV-Z|x?ZH4<#JwTT8r#D
73yueoX<tGl1$|B^?Z}f(v8YA!^k$ONSBw19-|V_#q}iy6D==Rs$4<C+b>qgh|yBno-G$QV*462imsyTc`I9PI<c7;Cu^~}UN111
mz{0*wv{i}t*v=WgmX7raTY_CD6W%6iOuzDE;`%ZLuJzSvM3s*I`P<^bd#|&>BacKlRYujlSOHkd~2#Fo6>CgR#ln_2Hi}{N@Ztc
W0bBT2Gt9^D0W~jx?2e|K^$vPZ&SRIQ_!4cg}E?JzAajRYrRqQwwlL_c+C?X^q*sRTG@KJS`qyd*)5ifJF#B&7RxowlZrQhyjqw%
MT9BTS;vbr(Qys)Lfl64_%g}j*7uV*DLRYs_laSQ;;ks6@plIBI{~Omv}Sqh`+r1K(*!kcZ=*kECko*4Y%->TK+?qANwOysgKL{n
ZRpvbD9t@ie`q`+rFCuIm_MTJ?Kqy8_)PdSrKVbX>~3g?u4yE?ogXwb*Z44cNY~GluJfQIP$1S(0TL8hhmcCW-rn}l#KsuSm(h4K
I-lVaSxX4H3`6wed^Q)Yxma}OOXF9Y*#!YTUyggA5c&e~%#0_IbuwS}SIbq08g1b@UeOfq%#3=?YXN=&-qhhHjGZ>lXZ1GDXWRyT
m2I5Qsy6UkZ=(=b5#TvN<|CA$?@?S7n8I8)UK_tgE;7#K)RVMIQ%a2%a?nVbwVxPE!`#W@>}N4RsZXpE{Oqd^GK7C?J&Qq-%=wA7
XDNh2EZH^J0C}?(fbfP1_<HjrUT2C4Gm{~*y@<g670v2??2v8^n(q@Hbj?waa&a;_qVJQ7iDo>^ay!f9JLCUVgwphD+$O2mo){W!
uYR@gUe+Fs<;11DTceu0EBU-)vY|R;_V#24`5T2o!-yhEQNK_><XcoR$IfEakJsz?R`Y>ubGs5zK3~Qg<M<U7ATEFj`p2J&upnot
b=1=@z-)nLQ7~c6%<m@97q19v6WNT>BHA1F@3raL80?Gs3uBZ;L^X?A+UP8jLZw5(sehJcW{22F9X|`BMCTd7w1^bbK0ZFH=Ne_l
#}VhaiRaN+HD&a&3ca#n<^~{P;$+Bb{AzJuTdENv7EX>Vv(pCk^=djorDC)R9sSL6J}WjIgQpWfliYe?_H62IFB>r|y&Hz%hG0Mf
1E5<|Ktz$n(^j|sga}6s)EE_J#v~fgBpWcf#{yzgKvxo+pE|TfB~&*^yU_ef)?kcC;{gda1ca&`qjW*6jw`>Qs;L61=o)+`BFd8u
=k$&%s@PF(j7Ui;qMGpU5Kc7H%4cTY1ea@&jEgdWduySaoB7zrY|F<dV8bU|v6?liJ5nwi6V10es9uR`jZtWIJk4)_Q%5Rq=pEG?
Ma1LjX?#M=tr`?=sSi9}ivojbwu|dEfr;_nXkCzM(&}9s&3!drn6G&z5}FK?p12<QD0`_X_iOLP(QClNJniYGMLg~nO5SEIE``=E
p~W$Jd!%M+MUY3#MAmc;rbB!Wdg?jgQ6Q4yS9OFyVa&$a_r{Q56b+4WMxwc1{wS)xLsPp%*X2wAE!}X}XA7D6Bwa2*|JQ<FLrsdP
G@;d+a7Bby3k)m!KHg$*vaEA!@UL6>YirbKUXM`0BSa7}Ajn<~0c9_QSTOk+qs=mdpj`lA9nvW~$O|f{WFNhkuz!!}xsq|LaZvSC
TeBaO!q9z}4fIhx5f#DxebS@Xb+9EHMw;Zm1OgA|mjdmd3+U)EIC$O|RpO+i*~V<lq?`FItN!a5I$hd1F$Q$G9&u$G$f;t^#)`HP
<ZNxlH_I7OA%O#hnYH!Jc?`8Y{y~I!Mv75UR!?N{_li76vJu5QNl~setnZU*K6B=My^Ym_^BEMzEE*GsmyB*@{@pNT&Bh@%i$0@*
IdPs&PPCGfu)xQWt@zCjPpLI(%V}hQl~PsDBWv_78e1m*D^)ELPgJ68N76p&gOLIk9W?dh_v-OtLgJ`Y!u34OSYWrFA4Qp-Et@(X
PTq|-6TIxg1i(W=A1OX0C49t4XtSCO)fU;dYZ|s^$Nw~mNEXV7%39wENpop;U_QqyWf?-B!Gr|?@WlRS<aM8S|2}%A29BGjB#CtV
+K2IwR2~0wax~tRtj{2T|4Bl#tiCBzpRxA)W1&p+X#BFXHUHUt)u=+MgY8{=zOB?59*}jxWsUBuswAsAd!?ZC{4-*x=jmmq+u8PE
;!2rI#G(tYp#_ydvqIJVr_p##T27r(0k~m4tE*ilk=D49QX0lNE2Y0$l3kMYl|qb!6bVODa(BaQwI$#*^N3;Y&2o|yP+60?AUolQ
h%Y|T0~uMLBCC>-9o34_l$E;;o+$kW2<=H=YuXr@J1bZ|hWs=h7O%`b8IGff_`waSAayl`k;saY)JY1`lw@DD_|4gFXo-0v7px5K
XfxL$Ss#)}H5geEogg2eXTF?3-Ndg%{vso{b-id}^NYsjmlB)I$CSRn?5u_~!r6*h0watxSJq7{=0gq6CaO+}nXSgmb`LXBdn?Fx
(U3JvDutRdn?lW(rrm|!RXuvGd-S^OQBz>6t~KPg?4yX9bTG=K$}LO*3Ac%Qviq=&1p{{#)mS+tXCOiOQ<%NYMvCEuZ7!T>Ok_CT
(!{{O+FS!vlhK)NOXVJUq57UVj{NDMD1O>b`IdfW5%PDDsfRaR{3{iF#ec7C^GX)EqWVnrgtBoQUCE+XvSgA({ABki-FB+6-fYkx
^ummRzC_{l(GjiFI**GUsxfMrJV5TR_cH#i^+~K^n#V24CBXJK0ur7Us#t76Ye<)umyqP=%gg1NScv6yQCoFk89-%8`qB4KO2ACY
Hl}n%<rkGzngPpP8;QAl<Qz99WgUbaRYX6iF8O^iQBv<P^H<6v2>{ioguVv8MhO^v1feoY4@j+Ao~HaNb(I=Jr)g`9YDFO0QZfja
*PDo0&esS^d-TG58ND{2MNapHDfx9YX5Egbuhic4WR|}qAs7>r##v@&1}ES0gsvW6Bj0L0yW|DoDG?oLk@>92JcU1Bg9C8`Q)!sV
AEs`0I-^zgsn#GPoo-4<)N5&Y$s|+DX;L>J_%`c?sIR0r^!1(5iZDvFnAO=IN5hos*b&wDvh&;wx_|F>-R>)VK>F!r@2N)ml*t>`
$vS4$v!qJHlyqL@tjYCh0?Q|=4O|}yQ<Oj3oOcY9hItnub@nc0V<aV{q)3eTxJ`r6o|GhaQdi^U;2t%Gx>p-&X{xD3Ak_A4fm)~2
MSLly(<o|Br<d_;F`c$)y2X)RYVSW?p8;Kq%?J9mhT#&E=$ghVxzpx;wD;4|hI+9+E26m1)zNz}_YnptqBZ>fd>Ln*<%+Biyy<gg
(1h0Lezhbu;;b2LgbrSqRd(5i+5UlXB?L}+q2TlST9`B5N{GN<LAnG_WAkYG{_kzGthMO;ad9G7G%m~=xh7c(BEtTKp8n%D4@%o?
9~i^-<WCIU{JJ=25HNDTn7_OV`qa)ZC%^ph?H5{1`}WI;ZSkM^?H8%DA!$7B1%WdN9kb`yo)`FLFZBH3z@3=mo@aZG6Pi8Sw+EhM
`mP&zLwaEcb~p@7$M*tjV1~A1`vKD3z;}HI$w&>&Aan+Ukn0%+u4#K==%5+ju`OqSWN+a3{?POtYZ!*6V><)OL-Jr~1(xXt&d~DE
^uV<Os>HF-C~9$nAhgV$=ehpSp*EeN>)58}ySC?>ffL#cyW_al&^6H$51{yi;b34h<U?!Vn1StC4sxS?j{xsE-f&={hj`%zW-ttW
%V)?v^bF-aCjbHh56Q5-#-WWG%>gO_sGbG15#+r9D71#AH$;C?nU8FoKJbVBz%xD65qhTU1@4gX5)J~#8JM0O`krSJ=nkWIK%GaQ
2L8atYsaw$49zeYT8?X?zd(Z-4qeOPWY<NnO!Of@-+Hzcxc)%Cu$|$+bc2C6v`jk;T-n><(DH+T8Vo`g1MkavKpviL0}$7B0#r0~
gQ2fp3_Y}94}1&ddUj}|hw2T+!82`?bB3sD;Cr%fKw$_J`@z6P6K>$Rp@a#*1-9t|M2w<qgQhqc2o9-&A)&PAgBD#&;>Zgv)PQjW
#q|Qq8~O|_4=HsQxEg|N2NuSf>H;M>AgEqwg$^i)z;GE@-?cmsZMZZEY-AV)VZe2PdWJ)rz;u0|dX5?`Nf^Kx(IIGW=-Z}axvnH>
khY6-7eqW9qW_-jF|Gp38c+`$*YRw8hoR+#Toopd?Yq=z%k}U*wB68QTD1q3jn=)uu{>a9fDXG<843<V+r)tS0}Dj!SPT@1ZvgV^
`FIP|1g<M#wK2*b!D<mSXxc&7CE<h?6#%k<BXi)}wo8O*577Xj7W9qwg8-vTgJfftfWUefLQo(&>0$m;0SEJf7y{sNL76>}xg-$~
($K;S&ju{u00HKSJDL1Rj3~U95#7UzTw60EOnAwT97#OPkOrZrSdu*$D5fN7h1n9JiWw6ag<?&NOv#*VU$UnGA(R-@VCZNT<@%CI
*^FFfQ`~FGsK8w$tHKOtW`znhyP|hAXI&y9W?2J9q-0tcQ^~g6l5sJ2k*v!KB=f?DVqbPxGBAvSWMLQ|$;2F|WMjY+Gcs@BDpuyy
m>DQQvNOk$49!!_m|2=<Nv39lNlLcn4HRPwL(SUkP%<|+2rBl5*&rF57f2T8hHk~=z~LpEbBB`A4Scs`b;P-u*@0gvb|+`1WOx`G
$@0)^W_qZpWP1(>kr^LoQnEfPte78|wq$=q$C3fcnk5SaYa%9y2|rM5&>fbH(DyyX3SCDsLockcLohMP5bZ#*L?#N&6fprMTeOCn
F<MrQHCjW(9IcW)dVa|uL2k?<nPEvLY1<{61ep?}48UL%tCVyunI*9$W|uVQCBt;Wl4TO(mrT<hYPM;472~8y#;lV-P|Q;j9<fir
DH$lbpjoKIie#e1c$tk_;XpG|+b>xu$ymiq-9WKZU&<0@sIG5omI|CRQ?;Fnt%48~W5tYN*6M{$#aw;GUM=R?%wSdJlEu2AX0i}w
ip^RTqxC|~Y6%C-Y-RP#ZV7Z^xB;*vS*{;?CDR2lD7Fi2ff=u3m8{qGL(P00SF>M9EX;tdK(Sz8MloUTHL>B4lp4v1F<%uc=DH;_
CgCdCvFmGw%&(axv&4~18E`4K%$!0pW+DM*%{E9$GG}Wj+4H-nr*B@q`1HAA(y(H`{lZJAQ>o_?b8c}uy?GT(e}Dhw^f?!xH)Hvx
)v`Sx&D6iX{Sspq`gWGsUgl)Nv%nPGVH)IKkT|(N$Ok!W6oBmJiIb&CG8DcOTX>ViVeTaZ^1z{*CT6YeXJ0-~S*1SIK1RCM{xHlf
0Rpz-JP-XW487RSLQe!?>Sw7JdjkQ=#(1TeFoPfu24Eb61pFZnLgD21w*P_T*M9pBNTk+$?xbLtgUqw+6trQvA{~l64j_MG#}}R}
Yyjedl0zpC1lXb_k`x)kL70FP9&Y~e_EX2r(sYoBz>d=Z?Iy03*?I1Sc@T$gmW2VD&#X8WP9l=TPB9XB2BtK~f+QY1(*ENBU~1)Q
lBE#X!^}&F$nD&6^AvnM24`^MJoByCr}v>dOkgw&GqCtLOM(Ql^f3SqL4Zk6gCGgP!P6uhfDQ+l8-{M`4?~cb=R0Ybkl;hFAsH+X
#4yH80mq63&E_!4;_Oifrf*K4zxeP1AE$>160E%rO_Jxsz{<ry*o6HIR2Qd7nt+QWPUr#^fe$PNm?Xmtn#KV50d1tN4aq)C9)spF
V8Hll)ENwH^jhR#n1kFFu|;?Zvmj0_KX($}$`dOa00hg<<17Xj5;^i`VG`2&M}T<@7OM`6AZ^>t2OyV$@G{I0+p?WJ7Jib6*voPZ
SQdM^1J;4L>;p}NFp#nBgjpgUhUGC(pm)`HR+=XmeJd1x0BB%!TUk5^>>T=^FNABS!+{M_4#F(P946a@<RCsEAhO_op7HT8&wyyE
wQgBp1HNz*+etFaP&<bjljH+1bb+A>L=3i{B~WOf@(eI_F}a0^iMM4j_{hVpA7~zOsn$G@>!+zZ1e46rBZ$~xn)(=lBzHj$1CU5Q
1n>3+i5I3A437rLb5e-J%zL!?1MNcw)@O*F4Kbun77QIwUz*rr2-#p;Vi4M~NGu`3L7E7toW4jz3L*hHKnx4?KLlHO41hxrI51x;
2%s1Tv72Om0yYgQjE6onYs`W?cYVN>pqnBef<vcSn#X<$Ga$^<c#zYgN$Ncc!9f^;#&iIWuyZ?w#sK{%&O!nGCk8fxIL<|$#b6_T
ka)RAict*Hz=8^tLE{lQ^i1FX2^b!k6SUe>!Gp;f5LH00bD=t--&W>=N#sM}f@ML8$vjY?Ge~2{17%oN>gV9O;G<yfp7kg^k3a)!
r3OuwqWVD?58Mn>G=#`<A=rW#He#9ySRum%^EHN2;pa(e5B)GiHi-Qg3Zw1jk3sVoFmBjTaY6@dGWG3YW~VeXi6aC+0(ypIqgq5d
p$DRc+DlpS47nde;?nBaBfvZc%b<>!JatmchBS$T)C$0);}CM*MnXF9onbyma?6P^R5{3sG;beM2<$TmU|$8!Bc%Hn#kdVVmO9xW
2of<&07dA5JH`1h&r_&q(D<Ne(LBrD43^apnx3BwA@zx+fU+IufqDG?{pabk7atFSK&D7-WU?T$U{?pRKZN?@hawgJ0IDEt6+a!q
@P+IJ+sL4b<i4E@LxFL`w*^5w6o=$nc(39MTcJJ@P70I63!zUy0fV?2W;uFoL!$@h9EyR9*_?x=+m;KSmbg$x(6S@q%mTmj?SpMU
r1%E3$XS!8nKw-Q1XE+^q!}zJPdGyxv}r*P0$>6Ifxbcqi!pP2e~^kC7A0)g99Dzx+}r+riZ5hhz5Ct}3SSNbH-T{WK=eVDdzKf&
riYCQtsk=na}sP69rlKK27=6l2yzj_XbT^1{_*w)fyk2~)G8|*+5)<iJ#<B!4>G6`7U?`N2^=r*<J`?-*sDR}+8N2RBy+&H>_^&v
9Dw0apsP^vkPfOEKyX+InP-qzLSV2{NHiC-br7WSFhHw8j>ch_$F7|mR6E1R6yGKUz9no>fd#$@#u&IkJapn9$imF>66pLx0l@+7
ROGIJ)h4n*D2RDth(G|T`zQpDaV8kbHN_V?9ERD3J&-s-=4Vj$NsL2sK&XR6U~YIR=oIROGlUN4kRbEy&`xt$N`uFsc?=l4uH-=9
jokpO*$qUN2M%m443KSQi7Nz@Zr33T&`JgZ%7_qT3XoCa2Ptew&rKcy<}q!vF-%Y$JQw&5Vu&Z`JVO{ueh}D@oTTFbPf*h#VY~!7
0Zawxc(nKuI}pbKz<d~%N6}Je+4j(}L>8xMmSN)1sASMQLmTE8K^Vr_!1Bp#j731p6alR&h%^UZO>)P+f71SUDZb%<ui_j2CB-*%
J;%<&7+8fOnWVWGLNvl=b%65_`lmHOgJGCLnx(L#p+C^_fo-KQWkD#90r0ruo1+aII8VU?pyj%D9@tq(OEf-o>!CAnp!>OD430_5
)@ed38xW>07>os@_E89aLh+^U!&-;Y1=Zdi_)sBW>xBc)hM5Xg1|r&lI8C#_riBgYRhFAN#Oon(ED`?%41Y=Sh1zI`{=oNgHw90E
dhPkCk9is=_5i>-kgj%^crg_57`jx*Yx|HZHniU$wjPD&FX?wf%m%1b1CKNX3kVoE!h(_=xW1h`DKslgN(@p6y(UhD3wZ*I8M7K<
NMKSw2F;_2@30OGh93euhLH?w349?;95;i!A9&yqDGY`<voqJDfr7dNmEDKw5`cRQbMW8cBf$K3E570XJ&JGm6N+!0Xe}=dY0<*V
tTYgyhXe|ch@H$LJrL}SmhuHe3C1k5Z6xO4@u(yg78#x;2=w)*DVKu_kuDcmyuQ6}Ntj^#^y1n3)931x>^{eZf>{R>m=h2-VeA80
5P3dWj0Jjjb78q)_dz<ygNzu!5aWgEm0_}x*bZTcTj{-+dKe1Z@)`pM#Uo4yXnly;5`&xrkhP5|A45ZeolAQ~5Q_r`ie#3+j=<1)
9%vc@Lb$Gb7+cHhbt)Pt+C4(t04iu&xB-NpokAA?*@RHdbEvKm{~7EEKZcGPCYVT048HHc5C-Z(U@&%Kh+{kPoP+lEAqnI)8ik6S
d6=L%MByMErWvg+1j8XIYQ7y0AdwO$c0w|0!SreI!xsrOJ)0IL4lO!_hnDD_I<3;WKjc}QfSY;)4{`;@7*teWKpKO=+O#U`WTc>z
0s<%?8$F0bGA^t`mcqvuAKpIw&s_u))ztecpjx=e5XzXHy8&(8i#WE01LP%f>_QRD2lfEd!_8e<iv%zAhhSVDkYmRO)*It2o6$Lf
=`txc>uWyEy9WeKz`D#&QZ$vug9JLc10*DQirJY2gB<Ed?zn+75QA_CR_j6yBtMueNXeveAeQX|ifBr%Y_xH++q7$0b)pxJjW$5q
0v!y22^ZoubD;4-?hjHhrx?nR6M6zOz!4CwP=sjD)Pbmlp>eq7^>VqHrsR{9v)lb1mD`P#*1$;yIdqPpli|w^!XyZXm|2jy2^8;v
7u(RpU?)K59$Ky+4?zOL8iL?pr6$>7Ac_<WYPV&_X^3@~w9O3I4xne!CLYKygB2`7OIXk{(c|0_FrQ$PU`E)mQ35DC0T}~XkROm;
`D`)Uh-rGDX?xh<dQfmOjIl#|+tBM%Xf77aF&p#D9YO=d7&}%v7^b0>fXhMiNG#jRtrRM+6&|2G@~D`m%ga@~prhb>?Sos^X%5|R
JlNW#Ns{ad(NqBLMs#S4fPVQ_3^gx+IR*ql2_1szgmDP9{LspTlnm3gSk2?xJ(Bm`dhhd?`1=qRmkY@gKsSMS90miJ7ohB1K%aql
_J+`*gs_KDansa+u`%>86KvaRGTU#9KiSi*obqK@hG)xprVfE9xLWUZxP)GhP8G!k-mI?|MT<{!(rK`42HN4nWOP1_9Ew#?giJ?l
Xa)sX7G`l<urr@|9vA2HSwg<>tMxJ!MWK%0ui_28&<F27aNvMt(NE8_*}6kNJJV@Cn~Ukx=&wbwoZpC!K|YIOK~DY1Di$}h^>Q(8
zlRd?``f3Vrl()tO+UZ>_~PmFPwh$6w%emdws#-)b9`G|R(_9#Y`ERn`fXGDG5MWt<ta=)6Minziw-*^vR^zOu~?X$Vs<CY;ymUv
7W}$#>@ABoal~!p3sr4$yP?x)^@F&S%ZMVXi&3tS*hjsNAIR7JbFs~4XM#?KBI|i<<_mpvIHhwY<c`UWR;ce|TsvcoO<#t7AeYq1
5oI*FKhjUL*kt6*Tr2kc#n;m>Z{MQpvfG#AwiM)Ta?hr&FQhBxtDtSRUxn=nwaZY9+xG~7wz)WJOZ?JPZ2^%h)uro<d$&k)-EXhh
0j_(fhNk`~YoRV(E;C^g58(q5<4*fy+Z>bHYqB0LKlNAnZCMk;?6f~Tly_oG%9E+o0M*Y8ohaz{IaeKU28^7gDVs5=k4nQgfxDty
ZGV3q+S6z6-#(WJn@Y|w{qXeDr#5?)*N0Rm?AB(mhjLr<2|j*B!~_Dmp$^qUZI~QhqdNJ-iTx>g<`zT@<lyY|-M-&u3YWn+ny>A?
J?LBQYEX9>DjkBa2y#~suSW6^aq2o7@~MVpc?x5_#~L)%ynOrq=|T1|68Dy=(dsTsDGz|I$L*`BI^Rc*<)ZPsN#I(dQ?~*|9PI!E
hA-ClpS}O`Inc`svP=6tI+S&%OBHNHlygC+lK~s$Z=P)<TD#~MkPV<Yvu&tD(Z<o<3wy$`AB<lkuR0Ts2F_>2X1TtVz}AVkZoEvN
;_2m^(>I@AOrO62>|bAe{LcnWOHc26SkF$7BAu(ZT+DA<m*`HbmY<=U(}7@!$Y+l4v|a_rP~g8UKHP53@!sv*AY+qG;1T_0EsACY
I&4vO{nnQvJ`+rFE1CZupjv7OTTL&bpC}iqa*a)x#b=0VITPsIV1_YUUxL<)%`62C>3|pi^V9oNjv0ikt(Z;*&*mJ1K>WbB*bn%_
LY<^L9iY+D{bwTn{Nv}s_55#$3iNI9hE^ore17xdQ}l;zb-Tey``<O<+9p*Lp0xj6!>s-1|3Bgi$*dFvsIyW>{#$z1oyXS&hq98I
sEU129!bT>j!4a<Gw(l^EvfPq9Op`f4w=RCQt70M>%m4^t?JNsowjPxSyqN&x*90@lQBs0X5f+X<fb~vd7%$-*2?9rMHF@T@Xt;F
1OD4TZborV;)H@GQJ9naqKxPuCe&P2+fAWEj%;<v5qT<Y(twCh4bpMZCwwNfI0TqJFv@2TH5|R|4ipqyq}T~9Qq&r&M>C-YWpoi)
Z^S1{)t|W1=cv_*!keAwA_X7nq2s~EUiBRG;tCbIP^_eqBF{mWw9q#3zR|gz&_VYOr3?v_N1d5@VScaG(Ts|cE4q>aPRf`jmE>wh
LQyEvr;to}h>lg2sS2slS()WwvZ|{xsE8_dPq+^tqT_icpL6k=#rb%-I#CY5nKmRuGMk#MTu*5$9E3{Ejr+r{s9ARLK;RYm*PK$h
jNPOTznePIsU=oNNSV|Z#;?{MNmS?PsfKM;_DTKB?W#7O>LBZ1hysJ$jVLe|Ca3Hn{NIcN(<GHgBjGffZ%|9GqL!nITI3-^g#bB&
Re{<V-51EELY;UhluN5N@njcw(zy*Yc_5%mbr_$1)eqzE4?G|GEW^5N4u*A+e?Jx6MgHxEcq#ubc4NKNdt07D<iIawte1=ZST7f~
STB3rZ9n2mHCdZXM9*5b2x!7(yHi$*#Sc1IWOZ1!6(^+R)uYHzaLV0CG7Y&ZgEPqq@fc+)u$T4lF9##P9G3xO4#$AO-`D6L9m}9t
Ec89;x}(KL%abMqCrvuNI2hYyXGmr2mN7wBfu>`}T=2({4qj3H-SBaDse~;h>q_)PiU;F3(46b0&a${aN6`(sa1`0i^u7L{yaT?F
x!YONLrfnDeWVoh@YrjR##d7XY=IctXv&b$7pE!+mkQ2Eo&F1f6@MnIBFV@)X{;I*ZcjSfam<k%On#u?ifV8PN*Uy8M~mzvst7br
`CxQAsVXhgsG6S4*GN<O8f9f`&ESa&=TbbJ>`wn?1Vsg7Gl=4LFNmW2t3oMmjoo&n1UT4Q6-!aI)(oe(-3zBE|Ei#hy0v&w?8a4;
FZPrn<Ybk9L9AGkFFiYDl2VHBs}U!$qPuueX%F)m;3%1pxgblU&WPUBg2;+3>uZ}97!fbk$l|a!O&Molvy|$HTw|sXfrQ1&>v`PN
_LuY9f<`sH-ZX~wAX}i^Wv<6nf#w9IFl1$fi&3$K=^K?Qcw)-OTRiS?7|92U?SH6{d&TX4MAn}8D7L^e!M8h_jXd4r_K9^sqTXrq
0X*xd*dBL^ZLhe+RJbK+L#f6tPjn4qzn(e(cLpJ~`qfaXWkksNEk)>LunV1$Q)`1$rq`JfDkif>i3wU^uDHjx8b7X}nmrIKquDn4
V|#K>WJ1(rXuGcpfVmxSC-q8p>Yt37dM_$5^Bpx=rfEu_FMmv#B&U~44ySN0$v=Dk@;IB_%rcSnvRSUeU6dl5)<fujj;7YzEPFDr
bS0?!va<KI8b#|TkmBcJc6JUE`0h!<W-!f`e(UqOxNTj+ly05JH)IpFvTK@Q9A=wKsH#3<3aW5#I~7u8=kfY-E{Z}%i<uSGoU3(e
M=sOXBlE7N-{fSxRc|n<%)4Frn@>hk!t&eugz34`2#&@z3%Op&?leE2HL2zNfX;e8`!z}q7|BvtEo7{))q0tA&cFB0B^iD<&%f{1
tR&>DvS7qwZ`v18f;#rqgKp97y2mKdeD#i%frQ`o@ZlYMMwP2n1m2YlSuBd{q9o3=Nt!RO=W`W5?3hBAsO+t!j1yEw5eJoA$MZ6j
xm@+#?x}_k8n&aYjExop2pNH^zE-iIK%sxpFx;WF$-eC?Ide0#+M)`pwkTtq$)Y+k&v;_;|1vmM{kICOQw9`L>Wf-}giQ#Y$GmA6
yj+A>@}Y=lg>h)9hGU))C@7{`Cn~Pxt-?W7!JrOi)}h`O2gAHAnnB*=pYDuhqTqhWw=FH6Y<clyTg5TESAc50YmwYzQr1fAU~H&X
$H-iew#z?e_56F`)-=$zsbSvgkZTpdH3LHx=C(>0Iqn%*^*<5!OpQa-Y+)qCe)KbjMASx4uYL*9rFTRen@v|VR*<U5iYgWwl(99@
F=ttqVbE#}mO_r1aZ(G4W>x{w%vvxsJw@VflJw%F8z*(1dT$`KeG+lZG0=snvDuhHP~5XCo9euBP^U?sF@;Er6OCcMzMzodtZs~I
B1m$_e7i3L5qPD+>TJ7lmSi%pbfli_Nl!gFlXB@pFH$od$|)~1$yi&ea#PNA{!}r$ra8ps^_pX6(eH9udo`P~4qL8(@cKNsrzn8B
)5fBH2L@=jd(r&|Xtm>XVOkp9t8Q04?x|>}nmPTg^)61&XNwcG7TG~7-o%TJee4@OPd_{E(CD|`XBn-L^EC!&uxMR_DXe=8pstDv
up$bDe$mVg#YX3D%{Hu6wCIkC&1`c^TSpLlH>^6eXgg3T1>6Ln>Z(rr<`8h{Ux3SWnoCt&;K@HauJ4<+?KU;7da^_?IV!B<9~!;O
q`qxQFGjDTWujxDkBaj++HsPgOm!a#JqajlRBaHAUui0<g-@>&BDHcbS~^EYk0LK%yz2PrI(oVn)R&BT8-!ntR=SaYbZ*R7wT9}U
)XEUzEt2i9?xO<>KBH8zm7C+QRW<Llg8gF=?I{DJwa9l<JETyVM%Qf)7|M^^lI%Ia8Ha~4-EbnUReGy~pYac#H?>e`jmpq$voh00
7Osh3>6-Y*&(>7V&h`ZJp0YQy(r|DW$M+QCmB<MO>ksOf>3PbGIIS&NbNpg|V)D1=Db<93QMjWr`A|Syz1M>&JvuGNO6~RVV4WHb
BmLA=&5`}BOVoE?bpE$eC!G~n>rF?NJgsdg5ox_O>cvK46GwVMUDk14Z6?*Xl16dVBSqt!Hh|6n%jlyN4l7z8qYq=0K>zOzKo5|4
c(g5RVEUG2H7N-2VJ>ewJ@RF8>~eGH96x2K^K-&sgjRsTD9R4%b6Z{n`RME~>#L0D*{_kT-FmWlB5Ur&PZG5sm36Zx$kY9(q`}*-
=G%ACgXWx)T`M!iY&o#PF?#mZeD=<K)|{7|zX{vhuTk{uD}#YH)c`!xQ}jbr$&t}Zy>xbWa>r`^5u|DNj*J5LDCWnzW7UP<qnDkH
(R<k`L5)|@hi>Pi)9s+Uy-jyx96LQccRl>*!er=pT_8crmZ#C%cSk7H0QPr<u%}?tJv$6N-trDgar9Bl<1K93b)3y$Gb{x8hVd%S
av@z4)WR0HdOTZ@8v)r=cq9ZLvjmX)QQ9nZKxk2?_x9cKhoeKlcAew0KMhd1<ga=}(GiJ8jl%WX%(4@p{0K-{uYnZQQbWtVc#&PB
c$u5!8kFr&U^5>UuX-U{Dcd82H;Qz-j+yEC#U}Q2wn%AxeL)jN&61INwO^Z=9qkrtcDxRU8m@X}Pb{sD%rW0d<8ZmbkJl^u<x;pU
OxjcV(~{BNlvmmghObv$`~!};5tQiS-><-x!qhs#YtSe+r8coRj^|YB1|LYn0q&W8@s0npUdBH)(Q+`(Dc?H4PG1`c>KZz@5YTx<
jdL^IdJ7G357xzWEW4+goSN^fho(M>LT$e+r=VV;2I-x3B<B|h2_!@Wv_m@D&#hieYuR-L^fF#w06lGTC7M2c{v2A!`_n01B{qHk
`=`$zzdYjv>82<B^JGj*sn@WlXU)L?`cL%A{2F<l`68k{;g=C6ZY`qfSHmnrw(>n9B$e=jyfi4FD@pGvTq{Z7TJ`dZChdPF%byyi
N~T3F7);SylcWnZM))w}mDtKSoZ$MVe1YVQA2Op>J$q=%oR$eOLm588bV>LrG0Y7=Yzz~OQj!(@{!p(&@#pDR-aboL=&nk6AyXQQ
6Ou>M1x#hOmoi&^sM0d{Y%S(2xV}jwRKxLGAeoXRJ;|hZ_4=3^rce3JQ;Jh7@_d%kg8%e)PW;`_CWpSUK@ncN=MA9f6W_4f^^wus
cdA%IadjQ9MW%2F_Sir)-Lgj!alunao1a!4n6mz_TBE|fr^oTnmen3#hbrmB-LFQyA_(wgMxl47O*TvU8!0fy>pyGN*4f|Ts#(6&
m@bvtW2xp&u38IqZdz|a-i?CZ*JB`06KE-_H<G%EOJQ1F6Ejl4R&)!7S<W5$s=Yd;S2g;R?2M~#a8=4%Pmq&aXJrOTSq`#8qcO3G
P2FIk)|ecXZ16AX$Mrx|ViuV{A`btnJ%MR+sl85=4=FU8b)>C1C7j3yz82|sy&EXFkP*$7>mnj&QL}y0HjF;l(=rnjskqUagVugf
Yd_YrjgY?aYA1rdN7v)FWV!8$SqHK7vo{~}uCKehNKfKwt^+tVxAD}N*7$wj9L1}@I;q<A?L*nI3zOFAW7s%!P6Imsns$5)v)#7`
XKh1zz}DU8OSjkO4QEj4gD3r<>HbET@U-N6y&1LkJX|w6vB7?=-xeQb7mCt3RynX9Ylqa`!y>)eqIZtOWuD*X%)0Myx_6M|XK$GN
M|DT#fwm~e({GDs?@vE}eE+s|6CL-QFtBaMrEtulO93~%q3MT~GYE&lMEQW~Tn<IwmANcS<?{T=pZiM~%f01`vuOEWUcGqQudQF4
@$D$(szM_mdwu01FHladL#%dIA<phwh2X{dtC~^C{jcTL_yZKi=*G;^M9p3*%qwVAHVjj>SwOEF;uu8?zUGS8IG*-v))c)eS2!-!
3df~f;TVzLg1Y2F26F19jYe8yVS}!xtahS{+1UaFsctkXt}jP&=L=M?ZI*&*w^WSOejQmZUoEu@W|i(K`T$VO`+TjuJl?VIkAf_f
OA7fvWYPF$#}fs4*cpYsFZ4INq>O%`kJ|q>tL>8gP`c(<>nQrcPX~NUEOsvWK^F^Yzmlx<E77-zSy3b{R^?n`!CZgG7<{4k68Loj
>z+M`^e$2D3Om|kJ;TH_>B3uerx>AgA$|~!`+T7w$-$z!)3S*?9$#LCdD^EHmzyzTfi{WMBkvP6UOLT}w15F*vCUme-nk^K$}yYp
!bG*1NJGVUaa`ShEgo<B={mMlLH*`ET7qKNRlOD^FFUCmf3t?it-^`k)mbcRSI+4LMwLh3(5QcY(>u!X{DHml74MYK<3teV|7b7g
Dq?>7M3)|KCx7xqfAWe^nb<;p(USRTZ=`)9_W|1UqZC-}6REBLS-bY6yg@`>^fo4o4F9vCHMysqG408i9lIy-dZm1IkM&PE=(U@5
8e39o3ul+r5I<tYzZx)A@e}(=^&7JR(6kx}jSRDiz6Vi`;Yw}jbp8swUH(OG8mjmqPYvmTRvUgfZff9f48EOq@$gMn>*bGX81!8_
m>KC#$<DUN9%c_$@O_t_xU$++ru!DIv}4s-9Xe@r`u_BvZ%$8Nd{oA*^zN@)w^viPYFXBp<>9BOCTq;E3I(RL@#umMX~w~dqf1wG
;=gAHAF}>n{Ha?;Afop#7}>j6<nb#>_KN7MT=y<m0k$WNL7Av)Nyglvde$5YuAJqHXdYDKrH1~X7EjFd|Cr8Ro%O0~>#U*gtLJ;V
xh(m|#mTy{p*n7V1sE^z?<JjwWBvTzfveu$J5tDUfFS6Gk?N!xXsB(X5A;1L?>Q-{ir-bgsvMF|+h(Q8>m=6bHQ~0+vCgqI>Vz?_
vap0xn*V_lusdhp^lC$o?~=O#2VS92PR_w3udf%gt82k74ZZT7L70a<Qk0TqcKg%E;7V)Z9?c)NY28*a<u21gl-7mh6MSH;-#T5k
m<RD0w&iLwyPVz03-V@*o8^Vb9xx>Ss|VK}J9hTCwIQp~y)3VsSA303?Q~A358s@qi^r!^vdX4Y2>y9achE+sK#6feKl`-48yh2j
rVW{x#8N^ypiEMdCY9m9MV>@5ds#nS5TvSKN}Y5WCChDRN%}Oi^fw(@^k~_SO<5X`yzww4yB6gmRZm&#LY%2u%boByot`Xg%J0}H
b3-`RU??xep65qB2}+rBeK4!cbj0<RSud~W_jT+h8cPtmWtZqNQN62D=`op9h+zL4!{h@_hC%?h6RGyf)-muRo88<8LAh4E=`3kb
tS1qnbX4nm_f5w>CZOoEhOG5|)eSTp*RXIIpEU=8ASXv}H3DY&EH5`^Ck9wXs!&6Zr2@ZNq#DTrPw3+6Ygkh$`8ldZ1kFU+d^}yZ
Qa;O8w60*YcdM?L$+c(e{eSArwuF02S!czJZqWkc>}<_9hAi=hU1sHp2<fUEGvJpHpa0kso<~TVMbY;I2M?6}Wh&8HsW`Er4U~p<
#@P8D@qv;(XZZ_Ly31cmCC?aLk{L(8BKk1t=V%kr7d_E;G~OO>DrhNbqK(M!dkrg3!wa=2w24$pBW`27?QQl?l9nxVhZJVV=<nD)
X{Z&K<rVb$ObC=`sYaMraydi$UGv#!dPC)8mJ@Z!Va>KEU!E*0-{RGnlg71te6?Q93lj=`RLjJM$7Cd;U40s;ykGg2CReTDrrLh5
8<w$iH=D$WT=gqJfpUU;J#b_2{wl!t$5#PTj9OzAVBA;*_^!W?U;&e-Y_$rI(kcLXkd{{e#m<S63wfd>riX++QlbJj`u813&qYzp
;sx~(4XOcujp=0FJ82q83JDK)`LFl5Q07*%6ZiPH^Fpk${hP}Oi5crfgA|Vj`gh!MysoB}E5kUjbfae-lY1liHBI3;@XJkhJLLG;
EhvQm?Z)&(&~_7gB9OZ&o@&JPx+E=;p2v$>%EV=Yj<so29q;;E>*<`@KNqAoXDxMoJg)$-D>r5ju}JB~HCuySXId>P%RmX?swB(a
JBo3F3K!yXwSnd~&-5{`*}B-6=>MG7q_b9XEAJImOF6YwoR##kuR*RELcF-`H0CITh+U2TDsRq)rg!)%pNw{wgm%ZWw%h}~Xi+pL
{Eb>`xshuvd|Pmt<*E^WXQ6FuUYz8+l=%u^zBPBV+{AOt`g@MXj_$dFm_|6B&tXAyw7W3yJYSLm%T@Aa^bo$lB?-S9qtBw)XdJzk
tsgOPoVnB)NH>uwzt(SjUhpKk#}in2w$4h(#yyR|CZ->E0VY-<7wE_lm>#4r@X5{v%|BW2XAb0|!jZg4x$+%eH=Kuem=hswdvBlF
X?M4~ha8C4(u4S<dB1YyN}T5pI}+E=MbN<rr<7<-w_*ua=~!HY5-E3o#iN*s&Aeon;(CUhCKX;>nv2VF>MUqZ(c`6gsUMLCO)ktk
o$ap5c87O67%iQH?-t$5%ii5(cX4Ub=c0#{#U+qeU1Ut_h`TFD^&4~51-R<++t=j<xl-hs4F`R*^w%AKGQXIw>zCxpxyAG6pqJ@k
;|w{-cq=#MQ&I&EZ0G!2TR7!T&_v!SU+uS)Z)$9S*4*mqT4R@ImFr!eNA`o5Cq?ys$&RR1qio!kPf)n>Lwie^zIPRkUeP|tw!S&E
ZEOxz{i6;RLS%YR34FI)>+`I8_3UkQNE01FYl-R#85nd;d*K6=$n`POron4<AvvI3vxiaV3UlX(oU}j6lgiz9`nYoQRI<_KSX&$p
%s8y{R4!N48P_*P|BA+MIyXIjVcr}`-+*cyue8X#sScwOk+P8}=hnZ>8&a8+Bp4Cqn2yyfWK43Fx~Ycu-7+T&ga4iA+s+PD_Aiuu
Qx%@6(*L3Y&!IZLkycl)#5B~P*KbI5`hJLC{j{P<+v+nqWpvrO>65klz%+S287=c1(pctyWWW!%r{kUQDQYxrJkjIr_(t=+_WhM@
8dXj=G@3E9$OxCYi1SM_VXwj&em~)#`_NDwq%cM`tr2K9|3zwJUh*1x+i<*gO#C-t{qMCLu2w8#0%%sCd{5Z(Uk4EYuaxcq(EB8N
{B%3N0ap|2e$|=R(xLiS>6WN|bzgHBj7g7w+v<0jOPVp=*HUXy710C$d2o46{3?I_6_Jpt`;D&rjja7ZDc#Z=qk37tx4p4z@#XZ*
Kfb(}{y#51zMnpOL2T^JbKbph9KEIS=JfN6k6)j@y>}bqYveoRlV>~T%P4SYUqS`Bz0#MWH})Z5dYAz8fIAU0E4e8`ALc^**en-Q
pnp|FGH@)J&Dw1Q1YdVAYTL(UY{I?2wysQh3`s(qf+m;q>y7xCDt78C36e>Zf#YRpMMD5EYO7`CD|zCScG*+1RCu5`8ks(Tn9t^O
vRTOdP_{QMP5)i4G!+7r_{UX$`y{geY>BID)}?v1TDr=~b`~IXij}t#QJeOw*8=&jMlI<8MW<YrWk8Mj^zS@<Ez|CyVuQ(Ne;(B4
&Wujc%0so}QgeBI**1RuTKE4C@4V=}iz`Vwytkn#ySB9<9WwZBNgD0i9)%8Kc#n6ILU?VpU+q3{xe>=-!9Yl^6sM_J@e*N+9Nzl(
#je}TE=8Hjkts>ZTddR)y$nWKtYSVSrI+cMT3$o7`nf=MDrOtVVAY{mx4V8oa?tq=x#KKW7@&20+o>sOay!U4t~`a#qY8`;pM#*Y
Y1J|MhQTE2CuYz4DqNNd+9LMCqvfX4SoK<&B}^PZO0QDH1vG5PexX+bi)i)RRnH!6;tLVMYAeS0IDtA&D<S-7PbN=zd5l){C>y^v
)e}dm*b)XXBWaszK}PC$H7=e+mR#aH>J<1q=FeWiVM<Vt_BkeUE1mbz<+)C-NzVKZo}{J+?bI<$j)B6y;3}HI)_CISMP{lEZyG4x
8qj`gr~`znTT<nDje-sub3aY_WS374Yr6S-wu%S_6&SA<n`tjLy61i3Rg87yJ#k4~K_#(`C)Ow*Q>jU$zVRNmjYCzFe0;pwQ3f^;
cdJHee_K^g2kZ-erX|C4vyM7hQQ<K@N{)19i%&-A+!C$Z@p)hCev=-Gf8$^Z(O!3sJH2L_JL&CZ`VAG7gQ#jcFmOmVhxL);Sp{(+
I=9N6UPrgT-S$8CI=9_h-Bn%j2o;eKnP#*2jMSS>yf%ACoGnO8isE&j*u7ofm>{;*iJw@8>b%;OMIrWdLK+6Le2ao#Op@0O6A0#$
S?FH?e%G}96u~l$zL;N&ND`oOT%fGlT|u^YQ*&4VuKJrLs|$w7bw@>Ubd4DpU6n5$bJnFP8%c&#lQqU@y*MMxugNv@vai;zrbz9C
wgsKV7+s|me;W6kzV?yyLVw`;L*MN6m9u0R3<9KtuGv>!lXQKA>$|~_&W(|OGL6gVLWq@&%Y&3Z{v4gsL8`i#g0-`W*PDn~b)P;u
#=d!YS}x{XM3Hp@WTa|_vfCD&nZNiS4$?bU=@B~AmusaQq&sqrE+wVsOAvHt+_%lXYubI&>4Uq_1QOd-hjM@<$<wxjPMZDDP<0mq
_3qaRWBBSAh3DkXBwxbHJyabUbo**YEZSkKs#j~ho7)IZ0ZB@SB`-!4Z;9mgCx{AseIcn!2xZ3+3JEZY=x6^-@RABAfpCx5Tm%L$
bm=2mnkr%9QqhlTKN%xdZYh&7g;Gx_QLfeUfKnO{s9w`qm%{(|7oR>u^kW8H7w4?5lwGSg{3LQ^ea%|*PM6FZMKW^~*(V89ql>!s
PX5$nk7UuQS;i=iE{<%IOyNipvZ;a#GgizCs0tA^NbQsg7Ds|<>P#-_Ol@OV@0zhIY2=ihE#oM&yVIxFFP^tef}lpiJtpcVI-mzN
f>4)=&{L@cD|+ck=D_+7A77A>idpd|&xG~pP{4lWt1W#rq>D!D^!oC{Eyvz&eM)B^Ze^TpcB+s(pvBv9_s9PIcT}hUH`JnoGMm=>
qf#ucwB+oqN@=>%GPFuFDk=V7m)fO1mDi(YDF<op|4u-w(G5AqvQnj&@_D&dZl%=XS?vYlV6h1t<Yv#-aVrjmu%ZSiiNC*3^h7JR
6mIN5K&rhsRCm#~8FH!z$@f?wsRu(yl_SlsIg~$;aX=#|Gvd8r+TH=Rj@~?RPuB6Q5UsBi7xKk=y<B(Ni>0>J$b{g)OKh#hTS;kW
G{<>G=87~-M~(>ojcWu(KTpso2%uDlWZNZqQ5FhCfiGyV^yTPZ#&1`^qOSHt1!`-cg1{erjjaCY9f8G5+#T1b(*oyzV1Idcb2%S_
AitZunF@O{{;i=P()Mu%mGB+Dv>tfuc)amj0?=_yx$bnZMS@wknRC}_4Hi+Zw8|0flUCD^qW<($;6+D10YAJW+qwEpZN|QqyQ^Iq
c|KXyDa^t+%KM*x%Z<h!w)xs@5KP^kV2qWtV)D<D9r5KNB|D;-8P!-6WO_~gar>r4|0`ij@??C#MI^8!G9*|;D1~e^s?Yw>>U<V`
?Opvw9`-F&pQZzrY!}f*L(4P2D*f=QVZMvrRq3U&*m-yS)u^;WJ@usi%EV0>j3>6}*={LHTQ^aqwn&7$Hs2YeGboVJyWegO(3-Eh
*t!CMM>k!k-|cpK-$733^gDA(|J8eYRWg&W=ra2J?n#9H_W+33rFP01DyUe|k`wvk^@60Rn#vTO9&#jJr{|c+v$@FHYI*<aitOV1
%CS2kJLS!3YlsV#YD5Fk_xK?bBO-Z!)s-6_{kYiNu9)7C9C#J#oBI6Mdxxl@m*D#zg@kCa&zE07U)7g^?B7Q5u(DFF_tch@{<t`~
QPG@b$P+MbwPne=^?yX=wG4k64|ozws;S!+tljM2X0m$$!+N$kzZBr4JsCnHYgO5`D=I~Tuhyug`{|6r)i#xzd)!aSZ(<$)kk_oV
Sdi#zkW`(8`3+<u3R*#=AUXZkhaTOuA~P4QTk}qbN#j#2@k%Z&$LU3{xK4`AYy;j@w6_0O-kEUlwx!2CR&{gbwkVRH9f<8;kH4=E
d|doo0RCOCj#{jCozMupe}BmRp9{9%48XFedySOg_R$6hey;+klkL;lkH@kw%w9cP1D?BRTpbMBkJqmPy4~qO{ddjYs0jUcjR5^O
JCOIX(Ook>|6Tp~k*>cCy>h3+^6N7OtMNu|e{FU{^52ya`Jn{e0!Pij!dxDReK<C!Ja4oUO#fhn&Xl=c{xiY#M+c7flzuR!j(sK;
>WoVK!z}M|GUTHBv%cQ?ub+h6aTjfDAFk`W?7W4%e;TrRcaPEuscCS@kL{ECGElXdQ=axv3zgk!kNM!CkJZH3^}xg%v-HBeV{yB#
_V10K^~j_ymm-%X^=+hg%E?XCp44~2L3s6-PV?oKJTkAS$SuC`^3FKEqG0c}_Ee<LzjBU=0+=^XGVLs{F<w!)LMzF-Z5K%o;1tzP
$`x+D(yk+2w(CK`?mt<3Pk68GuKUJ8!s1Y0qgpi0L)3lG8QE3+jO<pOk=?2@vT0f!hh6azS+c3J#;GqAp#7e+UuDSlLmm<L9Qu-*
qpv=y{nBUe-+g#`N&!veHmN+g#UUKavs-+>#ew5noc^;XxPIcCRr8b;$45)=JLC1hxheu)PNQjcYeOwG<s(O};ve$<zq*>#ya<pv
Mr|o{bk<xPbtl#SJ}D@C*6AZu!4GZBujl~dqrobm&>d)*lGXKO?IX&4#5c=9xa>q}SU$GVDC_3x^d(}v$*B6J12e26J;6rFzq7Ad
Yi{oz>Yb*O!@HbR*lbIN_!q)Km~HNWERyWyPnwz6bPSDGR$s`km-35Gh*ho`wImq}&y<&~J$xcfDcHOB;?>k^y5&)@(wd1m$b7Bu
>;yscMmyhmMtj(7r1Vq+qyh5wIN!!cSB1tDt)d?Fp|*-h+C^g}aaXMe@<qlc(4?C(RMm50B-uT>GV95tFjsd_?x@WN_1T|Ns0%p>
+Pl|IH}AaD6KrR2i<16!?%!<xyEjv}zb)dZ4fNNSGHYvMtZrpwXhv%J^Oe!Y47#_-SREC7$zdjITFOd_zLi`?V)0|3D(ybj=V+)M
irHtww%W(l^!GQfh`&pm$$7>|D@x;3T|masm%#-OT)%kWVnt+p?4CrDt_P0w+^eUZ{ghI%+E*!-QB6zR)g{gz*3L$|-O>1Ja3=22
<LuRV^!`@!{?Re-1ET(7?^1a1o}au778cF}qqtx3;aerg_aEDxkjvWL1FtKev3-^rMRx~W-<Vn5RS`$=SosJah&)<VuMgyM8T~_s
Fs&cI<=6EfQSDkae>5C4^16e@x^$@hGm0L_cUR@B&K*B<91jTp@bu%;&o3m(-+!FGd;0m=YdP2?DE|Ck;mAYs
"""
p=argparse.ArgumentParser();p.add_argument('--out',default='BH81_RECOVERY');p.add_argument('--extras',action='store_true');a=p.parse_args()
raw=zlib.decompress(base64.b85decode(''.join(DATA.split()).encode()))
assert len(raw)==48047 and hashlib.sha256(raw).hexdigest()=="4e33784b1a78cb7f671fd73f0adec08f3546553bde5dd8cd51763fcae69faab0"
files=json.loads(raw);out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
for name,text in files.items():
 assert pathlib.Path(name).name==name
 (out/name).write_bytes(text.encode())
subprocess.run([sys.executable,str(out/'REPLAY.py')]+(['--extras'] if a.extras else []),check=True)
```
