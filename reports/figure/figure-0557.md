# figure-0557

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# ROOTFREE_INNER26_G4: the entire affine orbit is excluded for weak-free own110

## Result

**A computer-assisted exact obstruction closes the requested affine-orbit question.** For the literal homogeneous body `ROOTFREE_INNER26_G4`, every positive-definite metric has at least **two closed vertex equilibria**. Consequently, no nonsingular affine image of this body can have strict own110 and additional weak000.

The distinction between closed and strict is essential: the theorem does **not** assert two strict unstable equilibria at every exceptional metric. It allows one of the forced closed vertex equilibria to be weak, which already disqualifies the requested target.

Four genuinely executed rational affine images are retained. All have **V26/E72/F48, C144**, additional weak000 and primitive zero000. Two are strict own121; one is own323; one is own8/6/12. The four bodies have eight completely reconstructed landscapes with **17 strictly positive bars**. A determinant-one shear gives an exact finite interval of strict own121, no extra weak equilibria, and strictly decreasing full P-bar depth. No110 construction is claimed.

## 1. Reading and exact source identity

I completed the supplied journal through EOF, including the branch memory and the complete literal parent `figure-0555`. I also decoded and read all37 files in its embedded source dictionary before substantive research. The mounted journal actually matched **404716 bytes**, SHA-256 `443821a17167a2746daf5bd6ddecce493df0d32c920ea6f626d931c91cc6aa30`.

The parent's advertised immutable identity is SHA-256 `e0dc5597e1a1410335dfc2d509e9f92566c0011685d067534d286cd4cb941a0d`. Its embedded `RECOVER_INNER_ROOTS.py` actually matched **67990 bytes**, SHA-256 `1ff381f89e6b97f4e097c5ec4f71b6e86c0f80c397f1c787aaffa966574c7c35`; decoding produced the observed marker

```text
INNER_ROOT_SOURCE_RECOVERY_PASS 37 221890 8bdb8f3ba1705eedd8629e485116cb87f355d470869cd9e3bc420e543b39ca88
```

The literal26 rows begin `[4555,1456,-2626]` and end `[5718,-2436,-3536]`, with physical coordinates `(999 I + (4800,300,-2700))/10^7`. No old75-point body, polar substitute, moved reference centre, or alternate label was used. The accepted parent has S=[22], U=[3,12], H=[[1,6]], where face22 is `[7,12,19]`, and one P-bar of depth `.8556668615746156`. These are the parent and affine formulation stated in the supplied branch memory.

There is no missing continuation-critical input. The new recovery capsule includes all26 literal rows, all48 oriented facets, the own-volume data, every new affine matrix, both logical cover implementations, two full mechanics auditors, and all required helpers. The advertised outer parent digest is treated as its supplied identity; the journal, decoder and decoded-dictionary digests above were independently checked locally.

## 2. Global theorem and the compatibility mechanism

Let `p_i` be the literal physical vertices and `g` their homogeneous volume centroid. Set `x_i=p_i-g`. For every `G ≻ 0`, define the directed true-edge escape

```text
ell_ij(G) = x_i^T G (x_j-x_i).
```

A vertex is a closed unstable equilibrium exactly when every outgoing true-edge escape is nonpositive. A strict weak-free U1 body would therefore permit one positive outgoing witness at each of25 vertices, with the remaining vertex as the sole root. The proof allows **every one of the26 possible roots**, not just the parent's roots3 and12.

For an actual affine image `A P+b`, the own centroid is `A g+b` and `G=A^T A`. Thus these predicates use its actual homogeneous centre. The obstruction already prevents weak-free U1 for every SPD `G`; there is no independently adjustable inverse metric that could rescue joint110.

### Exact forbidden combinations of escapes

Clear the common positive denominator of the centred vectors, writing `Y_i=D x_i`. For each of the144 directed true edges `e=(i,j)`, put

```text
M_e = Y_i (Y_j-Y_i)^T + (Y_j-Y_i) Y_i^T,
d_e = sum_{a,b} abs((M_e)_{ab}),
B_e = M_e/d_e.
```

Here `d_e` is the entrywise sum over all nine matrix entries, not an operator norm. It is positive. The sign of `tr(G B_e)` is the sign of the corresponding escape.

A positive weighted combination `T=sum_e w_e B_e ≺ 0` proves that its escapes cannot all be positive for any SPD `G`: their positivity would give `tr(GT)>0`, whereas positive definiteness and `T≺0` give `tr(GT)<0`.

The completed certificate has **28831 exact negative-definite blockers: 28806 triples and25 quadruples**. For every one, the recovery clears denominators and verifies the three integer Sylvester signs `T00<0`, `det(T[0:2,0:2])>0`, and `det(T)<0`. NumPy only nominates triples; no floating eigenvalue, tolerance, optimization status or numerical infeasibility declaration is accepted as a proof step.

One concrete nonlocal incompatibility is the set of arrows

```text
9→8, 16→20, 19→9, 20→6,
```

whose corresponding normalized matrices have the exact negative-definite positive combination with weights

```text
3284, 1311, 4265, 1140.
```

They are arc indices `[52,91,106,110]` in the lexicographically sorted144-arc list. The complete runnable discovery example and exact verification of this quadruple are included.

Directed cycles supply additional universally valid exclusions, since

```text
sum_cycle ell_ij(G) = -1/2 sum_cycle (x_j-x_i)^T G (x_j-x_i) < 0.
```

The stored short-cycle bank has **354 cycles**:72 opposite pairs,104 oriented triangles and178 oriented quadrilaterals. Longer cycles are checked during witness enumeration. The graph does admit one-root forests when the geometric blocker bank is removed; both solvers executed that satisfiable control. The failure is metric compatibility, not disconnectedness or a preprogrammed rejection of all forests. The actual identity metric's24-arrow, two-root forest also passed every blocker as a separate exact control.

### Exhaustive coverage of all witness choices

Two independently implemented, integer-only logical searches refuted every root case.

The first is a26-variable outgoing-choice solver with domain propagation and n-ary branching. Its final sorted-bank replay visited **2035370 search nodes**, with2247686 clause conflicts,418654 cyclic rejections and6504177 assignment operations. The second uses Boolean CNF, two watched literals and binary branching; it visited **6418352 nodes**, with35777787 propagated literals,2484133 clause conflicts and725056 cyclic/functional-choice rejections. These are search-node and operation counts, **not counts of spanning trees**.

Observed terminal markers were

```text
ALL_ROOTS_WITNESS_COVER_PASS 2035370 2247686 418654 6504177
INDEPENDENT_CNF_ALL_ROOTS_PASS 6418352 35777787 2484133 725056
ALL_NONSINGULAR_AFFINE_IMAGES_HAVE_AT_LEAST_TWO_CLOSED_U_PASS
```

Each implementation also returned all26 individual root refutations. This is an exhaustive finite cover of necessary escape-witness choices by inequalities valid for **all** SPD matrices. It is not a finite sample of metrics. There is no diagonal, conditioning, near-identity, fixed-root or connected-component restriction.

The exact generated matrix/cycle certificate has **1097265 bytes**, SHA-256 `c77320783cb871f5e814117ef494fae62bdbc6cd5cf82b40cf89221fb3b47500`. Its logical input has **342826 bytes**, SHA-256 `e86b037d278b9319546e8a84bad46b27a44f20b9910f0163d3eafd3493c0cab6`.

## 3. Executed rational affine controls

Every matrix below acts on the literal physical column vectors: `p_i' = A p_i`, with no translation. The matrix is rounded as a whole where applicable; vertices are **not independently rounded**. Invertibility and direct exact support enumeration preserve and verify all26 extreme vertices,48 maximal triangular facets and72 true edges.

| Exact image | Own S/U/H | Positive P/Q bars | Largest P depth | Largest Q depth |
|---|---:|---:|---:|---:|
| SHEAR500_121 | 1/2/1 | 1/0 | .8551321615489923 | none |
| DESCENT1E6 | 1/2/1 | 1/0 | .8546046905155055 | none |
| SIMPLE2000 | 3/2/3 | 1/2 | .8546567733844262 | 1.3775993010545874e-8 |
| SCALE_X2 | 8/6/12 | 5/7 | .6941950752004872 | .5564603416518479 |

All four are exact **additional weak000 and primitive zero000**, with V26/E72/F48/C144.

```text
SHEAR500_121:
A = [[500,0,0],[0,500,-1],[0,0,500]]/500.

DESCENT1E6:
A = [[1000603,-858,386],[0,1000521,-4121],[0,0,999992]]/1000000.

SIMPLE2000:
A = [[2001,-2,1],[0,2001,-8],[0,0,2000]]/2000.

SCALE_X2:
A = [[2,0,0],[0,1,0],[0,0,1]].
```

The first two retain S=[22], U=[3,12], H=[[1,6]]. Their sole P-bar retains root12, elder3, component `[6,10,12,18,19,20,21,22,25]`, and path `[12,6,1,0,3]`. Its complete23-edge cut is

```text
[[0,6],[1,6],[2,10],[3,10],[4,6],[4,10],[5,10],[6,14],
 [7,10],[7,12],[7,19],[8,18],[9,18],[9,19],[9,22],
 [13,18],[14,20],[15,18],[16,18],[16,20],[16,25],[20,23],[20,24]].
```

`SIMPLE2000` is the coarse matrix-rounding control. Its additional stable faces are39 and40, and the additional saddles are16--18 and16--20. It has two **genuinely positive** singleton Q-bars, depths `1.3775993010545874e-8` and `1.996112931907257e-9`. They are neither weak equilibria nor tolerance-removable artifacts. `SCALE_X2` supplies a simple larger-change control: reducing the largest P depth creates many other equilibria and does not approach110 by count.

### Actual volume and first moment

For exact reconstruction, the literal parent's unit-density volume and centroid are

```text
V0 = 112995444835506046059/2000000000000000000000

g0 = (2587845511183317747/6800106616460000000,
      -484384410377236407/6800106616460000000,
      -2961358936402431501/13600213232920000000).
```

Both included auditors independently integrate each new filled hull. The results exactly satisfy

```text
V(A P) = det(A) V0,
g(A P) = A g0,
first_moment(A P) = det(A) V0 A g0.
```

All four displayed determinants are positive. They are, respectively, `1`, `1000603*1000521*999992/10^18`, `2001^2/2000^2`, and `2`. These formulas and the full matrices give the exact mass, centroid and all three first moments of every control without a virtual-centre parameter.

For example, SHEAR500_121 has volume exactlyV0 and centroid

```text
(2587845511183317747/6800106616460000000,
 -481423051440833975499/6800106616460000000000,
 -2961358936402431501/13600213232920000000).
```

DESCENT1E6 has volume

```text
14140197779323921849891321147938091383/250000000000000000000000000000000000000
```

and centroid

```text
(1294625020787969643579477/3400053308230000000000000,
 -957069789133171474120473/13600213232920000000000000,
 -370166905691367535193499/1700026654115000000000000).
```

The recovery regenerates **all17 positive bars**, including exact births, deaths, depths, complete components, cuts and attaining paths. None is hidden behind a numerical cutoff. The two included auditors agree on full strict/closed-weak mechanics, mass, equilibrium carriers and every exact barcode endpoint pair. A third, general-hull auditor from the literal parent also agreed during this run.

## 4. A finite constructive mechanism and a small independent subfamily check

Consider the coherent determinant-one shear

```text
A(t) = [[1,0,0],[0,1,-t],[0,0,1]],  0 <= t <= 1/500.
```

Throughout this entire **closed** interval, the physical own-centred body remains strict own121, additional weak000. Its own centroid is `(g0x,g0y-t*g0z,g0z)`, not a separately chosen point. The unique P-bar depth decreases strictly from `.8556668615746156` to `.8551321615489923`.

The interval certificate verifies the signs of all144 directed primal and144 directed polar edge predicates using rational Bernstein coefficients. It also verifies that vertex3 remains the elder of vertex12. With `a=x1`, `d=x6-x1`, `n=a cross d`, write

```text
G(t)=A(t)^T A(t), H(t)=G(t)^-1,
B(t)=x12^T G(t) x12,
L(t)=d^T G(t)d,
N(t)=n^T H(t)n.
```

The death is `N(t)/L(t)` and the relative depth is `1-N(t)/(L(t)B(t))`. The exact Bernstein coefficients of the numerator of `(N/(LB))'` are all strictly positive on the interval. Thus the improvement is a certified finite full-bar descent, not merely a favourable local escape derivative. It does not overcome the global weak-free U1 obstruction.

Observed interval receipt:

```text
EXACT_SHEAR_CLASS121_NO_WEAK_AND_STRICT_P_DESCENT_PASS 288 1/500 193782 99e488ff2854d91592de72246b821ec0b60558c38f633fc80c711c6b460ecb9e
```

A separate standard-library-only construction covers the entire positive diagonal metric cone by28 rational polygons in the trace-one simplex. Every closed polygon has two forced closed U vertices. It uses55 tree nodes, maximum depth8, and a separate coverage re-traversal. This small certificate is useful for sanity checking, but the main theorem is not limited to diagonal metrics.

## 5. What was tried; finite-search limits

Before the structural result,32 BFGS starts were completed for a fixed-normalization joint escape loss, followed by64 starts with true current-metric cosine normalization. Both consistently used the linked primal `G` and dual `G^-1`. Several very small scalar losses came from nearly singular matrices; one cosine result even lost numerical positive definiteness. None of those outputs was promoted as an exact body or used to infer an orbit exclusion.

The preserved commands are

```sh
python -B numeric26.py --runs 32 --steps 300 --seed 260926 --mode joint
python -B cos26.py --runs 64 --steps 400 --seed 260926 --mode joint
python -B constrained26.py
python -B learn_nd26.py
```

The two BFGS searches use five Cholesky coordinates, identity first start and the exact Gaussian scales in their complete source units; tolerances are `gtol=1e-11` and `1e-10`. The constrained P-bar run started from `[1,1,0,0,0]` with `G22=1`, allowed primal roots3/12 and polar root22, used escape margin`1e-5`, eigenvalue interval`[1e-5,100]`, SLSQP`ftol=1e-13`, and requested at most500 iterations. It actually completed **13 iterations/59 function evaluations**. Its unrounded full-P log ratio was`1.9282992225842077`. The code's callback was not attached to the optimizer, so its saved history is only the final record, not an observed trajectory.

The structural direction then replaced nonlinear joint optimization by exact compatibility of positive outgoing witnesses. A25-weight triple grid produced28801 exact ND triples; adaptive positive-weight searches supplied the remaining five triples and25 quadruples. Their final exact integer weights are literal in the recovery. The final proof does not depend on reproducing an optimizer trajectory or trusting its status.

Tested environment: **CPython3.13.5, NumPy2.3.5, SciPy1.17.0, GNU g++14.2.0, C++17**, one BLAS/OMP thread. SciPy is needed only for the optional discovery methods, not certificate verification, full mechanics or bar reconstruction.

## 6. Scope and useful continuation

The affine-orbit exclusion is stronger than the finite screens: every nonsingular affine image has at least two closed vertex equilibria at its own homogeneous centroid. It is nevertheless an exclusion of **this exact geometry and its affine orbit only**. It says nothing about all26-vertex polyhedra, a changed centre region, independently changed density, projective images or freely moving support planes.

The next constructive work should therefore change actual geometry rather than continue SPD sweeps of this checkpoint. The blocker bank is reusable feedback for such work. As long as the same true-edge graph remains the complete graph of allowable outgoing edge witnesses, a successful weak-free U1 deformation must invalidate some part of this finite ND refutation. A combinatorial change can instead introduce escaping edges absent from the present144-arc list; then the witness cover must be rebuilt. Losing one blocker or changing one edge is not a sufficiency result.

## 7. Self-contained cold recovery

The complete source below is `RECOVER_AFFINE26.py`, **24820 bytes**, SHA-256 `c652adc000869a1dfcac6ebb08024e8489ee5530091375da672e0e00ccbb9b39`. It contains18 complete files in a54441-byte dictionary, SHA-256 `6975ea6cffe6333e24626a5681a5ca5a1ddf5312a3a884a9795f73baa8650232`. The source manifest verifies every file. No prior journal, parent archive or network is required after this recovery.

```sh
python -B -S RECOVER_AFFINE26.py AFFINE26_SOURCE
cd AFFINE26_SOURCE
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B replay26.py
```

A fresh directory was actually decoded and the full replay executed. Its observed final markers include

```text
AFFINE26_SOURCE_RECOVERY_PASS 18 54441 6975ea6cffe6333e24626a5681a5ca5a1ddf5312a3a884a9795f73baa8650232
ALL_NONSINGULAR_AFFINE_IMAGES_HAVE_AT_LEAST_TWO_CLOSED_U_PASS
SECOND_FULL_MECHANICS_MASS_BAR_ENDPOINTS_PASS 4 17
DIAGONAL_COVER_RETRAVERSAL_PASS 28
AFFINE26_COLD_RECOVERY_ALL_CERTIFICATES_PASS 15
```

The15 pinned generated receipts include the entire matrix/cycle certificate, both logical refutations, all four full audits from each mechanics implementation, the interval certificate and the diagonal cover. Convenience copies supplement, but do not replace, the inline source: recovery program (`RECOVER_AFFINE26.py`) and complete source, observed certificates, audits and finite-screen records (`AFFINE26_COMPLETE_HANDOFF.zip`). The ZIP is336548 bytes, SHA-256 `e03b1993164575cca68ae0876798af867fef03dbaa33adcc0af3196f6ee2e3b9`.

```python
"""Self-contained exact affine-orbit exclusion and four rational affine controls."""
import base64,hashlib,json,lzma,sys
from pathlib import Path
DATA="""\
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;MAx|o?QSvh=iqrocag;lg9<J7gS9q;sk*a$2Kr^C}`pX_P}(}z#*Cs$>oy!V-v>=-<uOx
cBZ<NVK9sfWSU+-X~Cw0CN~G4U=ljSjtzHRvIN8@g+uXeVbY~Wun)EGn_U0Ib_&~G<9K967sxXoRS6<%IVqR=oY>A4ckw{u6<QMq
NOvlVtR+_2lz!_r&m$_ovn6oyj$lBK;KKI)vavD&v<W<<X>aN7#iN1bhC4SKnm7|d)gDS6v8=vU$?6}DS`|6O3thz9iz+6pO6ee+
EW^3Xgc!w0LHKKE<#K;{JR{U6gV5W(5)eNZ!AptiO&Z5I1Mt}u=~$1{qn!5`gkWMx9vD-?E<5E`XNk9X$~Es}P=p{nJAR!&OW)#d
NpOh-sRs5gtF3@WN=Wn<{P?grHa6@Ai79P8M!2cLk*+7DsAb9hoNTP0VR_@e(`n5w=y~}zrtLncfbQWkp$fIM;77GYqv^jDHAX_B
HYH`i7dQq7#wHJlqt0MW>bVX{({XP&W0CPdbsbXz3ev`!$v<^vap>TX3cBp8>Ey?rhW+1X0cM<{Z^?t&kVo70NV}MIkb@mDMEa}D
1}|TyW6aqMRE1bQQJu=#5a(_47=nwI59I@&h&`ovka9W8bwDZ&h<QUakZP~{odS+P**EnHOUouxZ$1j(GOC2mmTAmSGK};;lR7w&
^MIE4G+C5kdzavkt(q@D*@Bw(!`HVyR>rVymBMzh0P`&>m%fh5EzLK^gN%C=EB$C%Ax4%sngd$V-Yf!=UO!(MG*d{xvBlmBTE=>y
FxT1k4=lx#Y>6Ky!QTTrWxqe)2j^{nktcmK4W^ZBvR5)3sbq`f`EVPl@O6}IWp3zURlE2V*ch5yuvzO~WG0KWH%XtO>oScEK8*4*
PLH+OMtZ`t1alMN&AZ5e`IAlTBxnUVE1<LRC&KWKVG6oa^F~4o@M~w%q%IFQ?^-xzI0ub{^g^pJd4p;!KBP9?>8&nsQm^E9l<O&U
m~%M@|5CHjt@l0n?4|ec*~)%wrvibbs}*~>SU(>T(~(&X6t`(>QU-#^Pazyr!Drx~o*lvXNCV)c^Xhg8bZ#2wIEV$oe)cS*P){1C
5%^0lUw9pU{RDo6F9ypo`g<TgJlKma``1OTr_+1_n-i6A8PPS=0@Wvd3x}4QAX;}|9LXc*M!ZyI4cW|Wytl`a0Ka+wh27lk53>*+
l8)?seOnjc=q-@vd?@^(U_mE<1HUTAQoVwiWTM>;G2~n+xA647!`Og)O}m_o6Q(^uUZ3~S1b2vHuzf7tTq~*CREK}eKxz%Au$7fD
gWoq&NIko{m}5!M{N8)_sf)Fr!w4U~)86ZJtc&%_tw?9!JA^ax`1iSc-U-j3FNtK26zSGddvlTc7&tN>S`BS0L8MRt`3X|8OVRnC
izvQCLW!T7>1OTJt1m;2sjMUqy0(DP@*c)79pSb@T-;)bm;!{*h!bz`!!JkzVh@pom<^-dn8*4+uhTbSlhkfMQIffu((r};W14xT
U|QIMY(;9p20M-=C;|^-dS9w_TlozAn5DN_K5GPt4r1Bf$Ww)-Sdp36ulwXnPSp!b1!Z~MTVw7QgmkfWn{Pe7V|q0@-Qit}Ypr!(
cqJk2;(O+uC<?HcuI{2YVIMjKbvL^1*iMqyGZR;m#u5@Cou?y5J*H?w9r{B*&h(0~;7`U!=aY{}PtY7~CC<AE6({pZ4*sa51jH{|
VBj9lRg@d`mE#R2oVS6K*GOoD2ql27Pswws>6f$pfsc3&M(9Z+avN{FnB#l>yY|g0=_*^@%b$WFP@sWx`15@h9~&??34$ZkkE}Ts
v<*LE>~V)YZztQ#`AnX;WBN2$81klS?gt7s#`dTe6x<SD&-2IycaY}sOM7JiJ;01F%#WIiSFy0)<y4kiRiZi8sU$Q!^Bfdk@~knY
tkb=JM)Cr$Xx}krL{syEyz-DEqb*Wt!n+dz0DV>97$>t>0S_0gO%D=-SM~sYV$_(U(~~CnV~9dr_2uBaZ#1jdk15%O5WIv>gj<Z&
C^5kj*Vu1-6BlfJVG%C2_tUm71xAJG4B6`Klbwu?dGvHm*N8l#lM16D^tnw@nXslmH)0GLa7c86+x*Gdq7f2zkL|yl<&k_G&Q=UL
u@_{{PWf}CepPeY+>oWC7(jq?dw6?uj+xj0u5dkBtqSv?ht}k#I?O*Gc<)AD)cv4cG8#U<`@2OFq3=#MCOiU`<vh9D3ZMNT?KDb0
h@UKS3Lb-s0%zV8y#?<wKSl9@>hQ>$Wit6hseIF_PY~-Q>4lFj#bwHOeu#Nf2OnR1)>Fa^w4MPR?U{V6=s4eZ!&I5s0!?WRuf-R@
=z1(Y57Hvb^ar>I?WEXA9Y>YDdU9IzR|T{7By$oaO^m88D+w&doxn0)I8(ab`2eagB{782deXG#dL<hu74X#Th>spghUGGXd)+4K
a1U)YcOF4?IEW$AkTm=vdH~0S?!(hr3lO^Qq)Ex9RSAx~5ih}Ln3jkFg1RT)sfvI+;U2h0X+kRC8%Jy{m6C=LoLe#PV({Nd;O27@
lzztn2=^6W4YkK*E=pSi5t8461$)o!QOsCW6Qx*Z*}Z;+wpPNvl^rP&c*F*>7(9xZlst{31(urEfG*t8qJIfz%zRkfr~w?zyr-<#
j=3i(>HI}D_Iaj3fKl)#$Fc+6Ew=gn%wk$GdbL(Su}Oo!!-?2zJs#ko@&UN<Hy}M<1|f|Jh>OTl`>Mc9qA{lxDf9E>R{8>7Xj7u>
lNfjT;Kv==<yC`7YkAB)qceXv<XTN*tYqhg_hn|EmDr1{t{kX3G}*$zAoEBryh}Za6(h|*k-HYpy;UE;Q!B_fOd+zO@$g|x&L$;^
)7a*sr#1_!MI_0IvWq9c8o|`;0CD)&b&XhxbF`A#XP!GTHu!0ITIyU(9zyNFNtw{!lNH;O-5-LO<)*TcNbjnB8d`7uA`GFbc3U4^
em2>R+7h3n1F1$qwXh9+B@tFH%Sqe=FbqS_=P=A=q)s~;7MKtR`gp-Ydg<$Yigetud&!*E8eku7M)faK!3DB!>_+|9!B>sI8eVev
fjZbknLUzDhaUnzVxg1O73K#vla_(%V3{K#@1aVR`+zZD8iO4V8ipc{{&!f%tGIsWtbN=sVHDTC;H!l{V7P*cIzI>|mcS?;&OKn|
wb>;w0jmgo(P0}T{~SFd)b2il0vkLW&R2i>+oR)ZH$N5HTs0)5<Xrx5Esb4vFzGKQdQLHwy)rs9&~U^at+&zk{k@YS@>Zrg>0j!E
f}EAzw0GwjaFJ8Eh^KyYpfTDl1CkCn;`81AQnCQ}w(>TmMhsZ<nP2=~N8a;4bHGm8UPIlP{0nZSDP{FDQks6I+$aKy<8hE2vs}jb
rDEb9_z`*_$v)Ruu`GG-e=f&$I4Hhdf~!zChXfp`;-y(q_$bw=UwuxR!pH76YQfVSf&imuaL>R`#07(nT3zey!&Wta?<oN`gD#5R
(AdKB!<4R~kkuxVuXzYU`r14;YfYzX7Hu5rsXsf9l5=V`HTrkGqCO^wFI8IJS(xn54=&(=?I102c01r`C2U#-(Ah#2cM0t&U~K3q
-<lJ1VFD2L1t=Z`aaKn)FK2$VWb7}jnXLldHjHCbLmqI0!jb2JwsWd@cG~^#iD0Nv+fUzGK5%Hexm}N@cCF-UvZI{Lm!&%dU6V8>
5ExuJV&Uz_^6tG}mJF*NQQ;rh7G`eN{$QZRC6KNxmY)AxThJzLAdCAm!wqRU1SSXx#f-tC6^h2<yp3}vCe%=Zv`@u0aIYW!but=v
PceTy2Sru_TIA$M%YG0?3TdBwiz0BzTSgjg3;N-fNgs?L)>ac|-JwiW=Nd*s)(6I1u+KMy2MerEJod9Aj8d)NH0KaUAzZ*;Wh}aR
t@bW4+Hyn~0~Z_#W5kXRnTg%a%<w}!Q5&KhTEfv@ekTNsa1G$eda?#tb>l#}Kr9;<Baa#>O4A(`#L!fZp9ZI6z#$_^C4At3N)My(
idmcTSR97Q*Y~I#m?Kq4nzSB0x_QBpttfea4$Ix<Yn9Mld3^wihd=)!yUvVkc{eFhGYd9W^T401<}g2_DZn-18>SEq_F#;Qm<*eB
oLFhns3#Zn3r2%$Len_ce*V4kY~e7Mh4FtP5ypEx*D6z6o0!`kLdBojAEk2(JR)*CZMsX_-U){UC_zFUMk69R511c<<*+&#gs2h8
psT$^oE>zPZU*?4-XYE^AZNUU59hn)Awq>Zn@fyLyd=r&z!@&03f<K#GHCs?e<`F)7gyh>B)@+{qNUUcOmuw3A?mFMAEI!iluwXe
^R4nv^!pBMyA(BtvUVS^8irgk-2h2-`LX7hQEE06RA()#i=jm>>&8MF$TRCi2|y@M6$JRN)Q}3nfURVgP$=-*GQ&+0uUy_~Q{SWc
cXQG!rB#%87|Ij8*8OR{Yh~2mGD-j7D=R{G5cSflTYhQZF-;fauK^%WUKx3FRD#5#V=W!(O=$uj>Dat$vLCop=5XofZ5UcmaUwHQ
g54f3X`ce`<LoXCvb<&TzohtgE_#YT!u{{wxpi+^$lSWtrlZ#ixVfZ0k8mdY>pwe${b|cJv8TqGV#%!dtnHzdVXO-6#`{<;@JfQw
cd6e*F?(&T?K>}ctpb%lmTi_N9}LPE+kR0huef^(h)U`&|JYJQE11U_p)A9{$lmln5(*CZp-8i6GEqzBK=)K(#~JV<J+H;7USA}*
t1AX4@rj8|97q}}3vZigabt}-2nMaT4AEjBC7Zh7l;R)jTIk$6gydz6dl(PfXFb0XaX<zEMh9ehfAIlRs||3}GW8LE?xv%Fn+0!8
BnJ3@+tTpz*1Yra4gP9f1cT>fr~liXwD^WwMV#{&u<`#NA0#Y)Aq$I%MNg`0m@Sc|{w9k`W&k?2Z{8u%l2DNgvl;&+Gl>h{ua2xj
hO7qS6J2>Ppj|CJ;nnN^DS_(m55&pgmVI0K$tf=RBMQQYzQ&~Ya!1Ds(tH2JMZET#;5M)ocktu7?gRNM$LY3ua^)jpZ+w6R7yQU<
w_3(*$hGI&5t3P~#J2yKExnh2hSK_zKOj<L@a)P+@o(tXBlF+d2dL)UAheW&L}A`%Rya4Tw{ZtQQ51WC;qV*G+tUz!tmZVfG?DR_
JM<py15#s6){^r3HLUif!5NPH?=(PH@iyfFxjFlYBxtmCjdy<|GXIvK8=7!v!!jAR?V=~mhs-<#pY1X->&}#1QK!-t8Zw~#*<Ei)
6s2*o_DMvCH;JGuoXJxCsZVF>TI_&gb>z9?JirhB=L<(@Rdd-B@gH3_J%cT_5Ho}6>pZkiVC@O-VjFfbE$=|dk0ZC#QwdpxDJ)cF
fK35V;Uq67`t{2_-=@$o9{}jpWJopTs@lAl5RLQ}C*>tpkN%-ER$5`7B61ZD)PW0K$w^7zMA)<i-M`$O9FI^<S8CA+x$zI?XG8{;
x&A1kQk>*nJr1p9F|Dcax@HF<r?GkJAd;mbo3U`8FK-79{B8=TZn{fg9}CcY1Al5v|A%46=2LZ!e*Y4mx?QMBoEX7@52^=B#F3<u
b{cAJ9;=4mJ+%`vd_E*&`ZbbR*yrg)!j5>CN1a0CfS}WtFB>>*kc9M+S{MTN1N6@@=88^K#>9~#-i2j~LxYE8%4H=0e)_pc$?uQT
_~0D?MpzqxV=(#|yB?8OXzr~1B-wf?883p8ANVO1uscHmZjB#;1Z2-omZ+7j=eLh0+aYIw+*4p0t=^slWAkO8-!e|!XR%iT51Q+8
<>z@|YOKW&#WJ@2O~R^~N3gn-Gvdx)nF~uso5aKw%>w#33x?%fnOjBw@4|tpF0{W5PCQjq^&XhKe5Qzor2IFeuJ*s6;gKP6&Yz{v
$hDrGK}HukZSf1SQx`mW`|N2F(pMmjH}TP`gX+FSQ7!GC<=g%mF4J^3)uh!si5SdpMSGi#jL7tt#)&s5uz8m><htw;F8JIYTr-`6
n?h(2bOHW*w_R|q;wOd=JD@E-z9$dsdsUURy-YiFw#A;+E{#8%a+8DUx4DIT0!NG6OK#p^M-rcMcP(9jb#h2#xbN{z?ZBJYER2t3
QtSu}@t8eQq3rcRK}CC9w8)gX>LGA&Esf;b_{qSN8G6Y<{x{X)GiR+wBMO0sd_y)-=^LFI*lHm#@`JFYHRqlVeZ{nUk9oATd}dj<
e#dnC2>w+nO20zS9U;k42?#9<e{h~eA)7O}w<T{Q9?pLOd&ipuG9w`Gppng{V;38-PCj0PzHFI~J(Bcs#vQm<6TK_KagNVETuv5=
G~bgDpGlxVWJes*>*ijhB$Z?UDU=!>N-nqmP4_PUh^4>V9!c57=BkDCtXnzr*o`h8p*;<B2$sVuuh2c*o~4a4ypekgcJ2|4TooJ^
<B3`AB`QKScKcx<CXv7hpwt+8s^1ySrvLf+*r&<WZKcA~t#W?+(v64zFaaX`A&8Znr=T%Tmq=;Hlq2KE%2lkx%M^@F|C7j^72qd<
f-#rGPQ#j+Zccc<1jB2;$qpw{-EiAoEuZU(gVWHv1c{`ZZnPDp>1V-g`ofiTD?MAj+<2QXJeO`MnouV9Esyr3EL6V1RjGO-&xk-8
yoOTs7x950Hlnuq=2mCCeg=fbxY*uL4u`|(xt)gHF51rT4lgNq*ppghFFbYAf?!girl;iP&Ze}j4Fk9rg58P5s4D#<*LmH0*Ol}{
rwQ_LN$ec~{PrG4S;cv}knU_Vl-C3gtOV?dk4s#XM;;ka3h3>yIQ_|Z>v3peEjVG7jO^vXIJffS4n-ak<%HeebROryb5}{x6N7Aj
tCFHe3kmLcGhx9L>k`NI<py`K3qe%c(FgBivLl0lyQh!O8e<VMDK028G2zX>9{-0k#G7cUMfu=$+y!iy)g9GvHEh+o1n&1D^re81
Kr5e?$DUlWps0}`YVz?86ZIs2OCC<s1!3s|nlxPNMaOwLsteulDUKo-Er9FWU}z|-q-90?biKV^O^HPczLWP8WQB;88~6yW`}7DA
tJ_Y{t;PF-Vt^xde_oz>eL$IALjut32Fr7tnJ`3K&FcCpPgwls-RTRDb77FPhKJsUs%p<NiN&v<HS17Fh}Xm$pS~XEUu^3B-heNw
5J_$_K>x%}(x)MHkY~G-5{9tYXXNf<iu^=)@DWB2q_O&F4A&JZmCc3)PZ>`a%~v+eVK#b5uJucV&k!i3Htbs((`KeX2^><Hc~k~R
Tu5_2d5w3ED2(^FTFHiPaj}hOj$VQmPk!ga4`~Xpg3KLpH#PvGN$d`9_LnRwW1`u#*HCcb2X(C_28CH|>@t7Zw_1QPVL~+6zio8#
s}zp0Zg3vPcd;IVtdccf<UhmWji{Mv?E^Zn^kT~ahNIWLv#GySVVl}eEOR!+lUjy-T|mA~n?H~aCt2>IHlm8z>|ui%ivM@fAe}~8
UdPdD2eI@{>I{GA03%5+dBK8)l4OQn4$@~fkL+U>-`P_@>&5W0XZ&*3F!cF7z0UF3iY2}OLxWrC5lzapQ;0I`A2y56*)!~kzuaLl
e{p-(TPewFgP20_18LBJl{}fuoHfA`SB6_lkalqS#$l&zxIwsfV)fCuAjQ-to{8oE3-zw2-Xy?1*3O>l=*Cs&vx@j1z%zaWC^_sy
nY(|-`0XeKrO!F0Yxy~&!eGpIvRbdRYrukz+Vg@Tj^>^p%;A(8j&TIDO??-<?u4YjNRDLKG%|bO<CmSt5nEw<jpQS1%joI6)&h5>
>?6&66?Des4Pt+LPKtuK(Yx8X#RjXoU*N<qeQ8;qs<MX4wxTLVm3&*SZJTE>9WCq96FQRek$zQoSP>i`Wln()BOBYdkC<|g#<0g0
CHwal2cg1GJM~)hUj@p2g;9;?tT}Rapv=Iz^2BUN(hc1@G@FeqRs}T~6gCQ?l>*p^r%kh$slPSN{<Z;TuIu_N)WDpGrQ$d*aMJTl
K6-Fkv3N3**o9@3%c~4cX*q6IMF~7j<R0-IkU`}<3*0NGjD5f^LJ#8&H!tAvi>yCd@rN)3{eeY3q|8xZF>kHqec-P(JRs{_tgy2h
dqc!ri{Vf`4cjMWJo~#A74u>VSWZXQSM(Gjy$JRNDf_5CfiH-d+vQ7`Wu<8#TEMzxu)`LgyV`XR6i2GgAJ9&(uro+sTV_6Itsxv&
XNdtT^un0%ok8VVUWB+}>hOwincvt9xsq9t&FE;|tX^_Bk(&6O<d~Fj>82)i@ls29LJ>E~`$4!<%Mq5zZ0DT)l*V9^ZH)BrNO@+%
|EM2U{rw0;;Qc$i)_eU$H$ZJImC_yFg_eu2GxlKt^ii5M<~Rd(2bmAbktOz6=t062pbu$104d^^sG_K+<JyEZVGi4tL$@I_Q05x2
aG~tc$YUg*cA&uHIT+RW*$+_(hb>&UKR=(qa>S7ahw^oByDlb8zl`(4(|y<^KP_vDXZwgwy9t`Mz8Hj}c`+t=wL-oG!aFAy8Ch|;
6|q`&gOCU30oeYRmpzm*0ZsqWtJGEp%U4i+Lf;|)m)E2+hu8dcg#A&h2u^2pbUXO<xo7p0pNT>u)dtFsrRB^HLT{MH+|YZlWH!Qq
)RKjeA3+_Qnv;ZxKtKU+rKX)G%<hI~q5D9*Ugj`tG|goC@z-(}Cz=^_BE(dr2OM{7lcHEoW(G)_UiKG^rma9K6;~L<CX0w+%ag?>
n&UKds1|n+n+Em!wIr}X8L$zx5nlq+S1p!(Ui0<qP;R!~=p?PF`I;tuAE=K<m<g3+Z?(+F)sxWR(ZgS*9xpf>0D${ay8GSQ{i2@-
@v0#BYYg}`A*tz?>k!)@6@kl3-8d_DQ7iN~^0V}y0dfvHvOn^oU|1|Z`12z8hNwzmtk{NX{;QsxV1zgf$EG51C1Xxh?-qv+0cRvJ
H1dTRGx;%q*Aip<l8)cD_yt@<Ini_{senemufIi1C?2b6)|sCHrSd{`os5c(f5iJap#xk*k&=E8RukEVN{f?E;cr#ca)xtPFF3Cb
LDAxl2weI!8^543<Yx8CkfI!u>~vw6X_Hn;h-_*YS9|3NI;a+nfbG#NgO-4+d!X&9>GA3u6f_5}qd`A+T!5w4ZRH_8-$G~on)YB;
VpR3K(b=6wEzz+b3gNxV1tqM5-U+IR#$4%q)6*j+NZ*W>RL8?6EMsW%`X{p>xEB_Pa#Y`yMN`NJUVq~drng$C?R*0XjqH+0@_2yG
>lF-G1aB{_82CV3P=-IL`t5}TvgFym_$yLdq@p`c$_ya^ytH(1iAUrC^b9}LIaiz|26%)zs|x;-OPB2x42^S8*mTb)p)gavb%5<8
5%X%=!>msWqWJQ~k^%Q}2Z2h|N41%d?|#R7n6$&GuPO}{bLIsQDiH87#2<Kq>?kzGE7}yVjZ3fxbu#4h5*$f*&;`M>A#z|Ib_omo
#A6e?{1E#ny#H!j1VhS|jih0WB0O%<=YmGqDWCPIa64q4bfgR>UkuXe`z`+x!G>$#1jJzTv@`={^KBe;!ePF!Grii#`Du5d?nIw~
abRf8<KhZ3aOfFH<otJ&F!~Kfp-Tp|fn$m02-0bkRQO{HX4ydxQwb19ijf?m=102dXiwlE#{tq<LTHU=EkA~Unp^uS%27Hb>lC=D
4)Qh-j?}v!IZG$)y1a~%vyad$om_^G%{+$S>YSe_acHIcr9>>xvwR)&HpA7B-Kz^9;z0a+OWswpQKpzumBbveh_XGrzTukBv^fnO
ZHIwHaA_*16D;yax60X`O(989qUL~(p?JYqT+7F0v$mgZ9PcE?L@LM}1F07cw$76^%a*(~>+^C%nEDyrr~Er?`A&@5QtL4#xzLa=
Azxo<$m)K1u;h;%UExhd$WkJrvw(qY6kx9>&k2#ai`!#b6zzZmo)=i3<pQD5kJlP6L$AP#d~$t+33Nc`k5iwV-{HiBm>F&(?z?iL
HLZ84ZwF&Wqr^P6lEgjI+k+)>qJQpn0oEjlUf|(&U(_#F-=X&!B@oSXgTgMUOASc~NndMsCkox+vqFWlniHzs(G>ZPC@eFOvOSlJ
+@x_{%{xS3r;3(HAAu?W{KUT<+H+81J`#pJbvkg5)AP|-{-H>i&569M$T1^@x@{c2R|2EEFLvtOnHVZ<m=oGgOfVD$UR`?*=~P}s
YwK~+?KomXnX%CwDCLdI5^mvx$Z*gi@9OHZ*<M2i_O^Bl=S1SIj@L5<kvBSD!pk`AX;m*7BGst0{GF8G6uQ6=W-;;Fz?!U-D#Q+Z
W6yf$Zg%1QvCqOJ*zr7biY})Y9#hwNm|LwZ!Csn#^$Oi7+p@4yqI7bgC8#^uJNkYO{3uV5hDU!9`7>5LSyPHdh%MP6{>K6<?q~aM
9PM3^TQ@lC1i6#`_b2{cG!i4lT*Z}A+0UOrZpYr=84BGSkHk3qNKiztj1hM7{1)o>!7e1Ora6N?`YaHt6~kAPRTX8)V#?GVY`-FS
0>r=3^n%#;8DZOT#8bQXZ1ZxQl^4$#>CZAFywO5YQKd*3nVP36*`rj4Es)*!0Fbfd7Mpuj@lqJ&nv|1>1<diGI4Yvb*`b#up@N?m
G9OVSAG2e*7LZo4ighpO4Rx1m>63oA{N3ZXh<f_Opg!!IuI!^O)!4Ly6|bf|QcuY)8@4`IFHbn=T%l7#yz}RO9mMtuil<5iIe(fS
!U#J6!(kQRh!m1T{o8`W^D(AO{4z1J?zzAa_@eL_itep(?&#fUi+MPY<L$dZ^#=KFill4a+E>?v*nZ4@1!^i36$0=>>a;oXo6oXl
F?K&J@|K|Jxwse%B^!6%eth+In8BQz^f0xl+iFuxA<;F=u7cQBDx`|5pKcfH{fqu3y?luq5dd<?)K5>9(ze6mJ5F!p?=pm(6{CZF
^I8Iy23pKA5=fznahVbz&BRoMdJrdMKT58i_4U51Oh|TygLwgO`jpUTMgu7->odXEj8wx4<YHypu(>vY1UpaFaa>Yn($#>+*gy-8
p|fdAKR`(RCUhXs%dmrIISV(huPoGTi5IgE4PuO*x|mvoQ;5vkL5FQ6pboxc1hyP$4fO7~V0-SYRv9D8jM#U-8(?GMlS52%JTHM4
1l@#e%Uby>#19sgXCMt_xpJ04sD=Z44jhND=jpCiSk!3YH1FO<|5&2ii@NPG>n22ZCAZG3&EnjbnHhQV@DVEx6oir>!0l*v+Dvf7
H!-!)gLd@JLKhYqyGn7_5Jgnf4QN#w4rY@2@ad!dmKT`zxMi}i{=LgS`~F_3dJ*)r_V3Yt@o%T-)4+9W5>hZj;n+A$Wm3bn8z<M@
9hG03Oh9XA_5db8lLN7@&3ei9-kHCoA#d5WriI+C-giz8Ucbw-CB*^wGdQ(QpT-zM#<&oDh`0nL@^c6$ktYT>wV#?t(GvR$K2w0I
!zM0gV&0uba6Q(iw2fYR<oDco1jko!9l7q}Bkw1AutjvtfuI%bO(oFFf)*n+NjOpn#N*K?xXGx`jssnYjzfc9MHS|=ssnD`f>%vs
m?6Jak<>3lOpB8;fFY0`g}qE^a}_aQ!1k+KYCaQL=)rWCWM5de3kS7uuc0<>Dubn|Ujtv70Q`{)GJw$yM4*~?=ec?BRQ>+$GY+}d
mN^UrN4v5?a3EoPEbNsui72GV<KqaGQ)HZ_*G$#JeP%7cc2FEiAy+j0x3&(z;ks*g>ywOc6;`5(vcDl?baeKSuS-iJS_@0#A62W_
6!O;B*4*id_X5PYJ9-NN4ecw&VsqGK#P?dq$$;+9&!;+!CADzL?sSFqUOSzUgeKgNPl|!51oFGvY`(@}C8A{Kr+^mAFqy_hr>>dz
45C_m!i$cU#_>F77)wH&j=itulp&y2;`HY27)6rWmbOy(E+2WhuG<Vxo#h2<eZ_D=R;9gKN>^$<J4cU1rO!{M?W>EkuFbmZB-xA#
Xf28|(U>H1gcJu*!sLr*4gLgzi$_^0axfmy_}T4xjn9Myr~P=O7CnVLu-;RQ$(~IKBEaZ4-B37W=(Ad3m;#|J!(Xawwxn}8Zwc8i
uGI#S`*3w&5T4KsrTGKKp3xKgy9nqXB^|Mt`4&P){#^w!FPk-^!=Vv(+J#N^sI;`%nmy?312i&Y!;LwCvFT4+prbQDBZ-cxH{h>Y
2B#hQ#^}>2mTZYCRR(uQkE(%Gl~amav)N2(_jaVOm<TQC5Ku+xL_=!KU9pcUqk?UR&c#Z9a@txdQ8#^-O45_B9C#*pH`=@Noc*ZD
GFKFI6ALJV>O{ex;ZT<*Suw9JOR|6b=84N%y)D%)#S@wo!t`&{9q-yGv=CHG#%IxGAwCbjg+>v$j~P5_V3l8(vVlbW+wEJby-_PE
^vg{IyFaNx#O=S&r=EpQ)lmNS6*e}Gaj?uK>hWC3UH0+0n=A7!GlAZbR{BNWUf$F%E4)dcIA3NyYg2VCO3qLz*v1BER`ckf{p}T9
<lP5QX$G?|g4rFj7xL{DO;Kdv;k>pH)%Fr~x1gtmf!%P?R$=uWauKdr{{P)iIh*V|E=O>|jE)|xp0d@^0J3OlrCV=J55+H%0ayE{
)olE8+zDrV`&wX6`b2%+@KjO#C#OmxjpAEE4IxfrC(Z?tGpXmF9%DzhHa}2vU4n_L{M0&Ix^L6FK?GKhWZ`d0bujP%5;-Yo-OXu}
=0|I855=+E?%o@OdT2C%+$5S#A`)Fm0mpqu?=y-TR8R1XM@GpD&NWQ;dY8Bq>it_yQZ4|TN&iXI0W%XLs)UUV1*^H6BJ$Pq38gav
OAh9aFQ<ympz*n<k?XV@l-`YYjx42NFGy|i&Jn~K$vIZ;AuXq4oFbNfQMk7H9WCTiidsqytloJurow5!3n4BP*SwCI7rdHJqwaOv
V|+(g$*7!>{Zg+5;g0{PQuyx8t32rvb`n{6o<(G+aIaaI#;8HLzEkt8+9+lJbW<LvWHs)xT?=}h4L&&0Ur-=5#X^=JBDsl4guLTq
sP#^t(}^#yn-kNb9MfPS9j|?@*jD-EM|&XZcm<qx)TfI|FN?(Omq>g@zYz-iZ7Mx86OpG$-nZ?DfwLH#$n5J~P{<lvVi4>jCSicD
UY87QIu5B&SuKcsJp*VZ@Kz5&iD-B*EGj&Br45^6aKm)>`eW@L0Ra<dkHAg-g}Y?K_Bzy}0wya%tY2`2oB=uslK32Mgf@!4uC&=h
cT5DA=IyzGDac2uio&>Y27Ykp0BOv|Y5>1aga$N%@p(O;H-^Evz~5ZExuyo$@y@Z=XL<-<=kBEGgf~zaa!(=UF$G{t7ZWs*_*JRA
5<s)c$<Y?`1m)a-#@DoC2Ka;jkmQtNC4GLcCXFX$F;i)@muCA6L4!5EN67Tq=?7gu*mHk59>9Ys7^hfnpqk(>5Et6ue=hluXDUC$
tYf$+K)1~OSf%nJ1L|pk&0?p=p1o=~^y9-tG_U>;OBiGBXX0R?n&z&5C{WmC_{T7}dJSRI?9g3*fQk$g?-0*8iVeI((4{nyB&T#;
nWz@gjCZ2sD@NW>qrQ7=(AjpT3Mz2XQ=TFo(n`2?HRl99HTu_Qqp2uK>d9d5ZYfF&pb(Q;Y%@B)u8s`5Zb1w|P7;QaQfU<Rw`Gi8
UX9x99PMHj&U;Rz+33DB>Q1k(I3rMPclOo5a1em{{<oB!s1+q~H!1-NPZ_3;l3b+*sgxm+b^(aTPeigjZu0Ki^X`Y%x+b-ze)86r
lY)!kQJ;IE%=%61{g7@Iq(BD_9V5#%98s{KN)~jg3H9T3`Bn|^JuKEOAqAlh*63IWi(aPsmprtzAww$_^W#7dbrYJ(M+8WeMDa$M
Rz07FF~yXIPH{5HYv1RGOtZ-0LmMRHs)x81d>F^m(RUHUbQUHzg+@!A^ib=Ve0UEuIs(QQ0`0CPM&2Yc00c97=tjh^`j7eSQ5&fd
1gJZMJFjJL;l&01Dg%t$=_zaBYN-ZLZq%^!4BajmSv=`?Kb~gJlh~(EO$o>xlD3o$X#oC|!>e~_xznVRLg6(eeOx&-QOG>ep;=7J
<LJu+M<mj~wV647mFP(AmnYa;z9Zf|Sdjjyzda4>y3`!ca#lI!9oCBJsbpe-{P5t{=<@L|;8hF`pu6~`Z+L$d8cUe_I$U$+?OS@j
;seqF$um+zR2}CXu179p2j70rz^YQ;$Nh$E@m)ePY?>Z)jS)*4aQv0vXSvYS8g1<IfA*T3T^fadfaQ#tA|zFU?(f^2YY=G41D;>!
R^nF_wngmh>c{K9-iMk<yt4JJs0^cJS0;bVHGod0t@FUU1Uk2~3ANXO220=Z056f6xi8`kWEk%F@vG((wVS@2HBrs@vj9Ge)(bpx
??LsnMR^OukdSXI?DNKAJTfBhBK1I`3hn(PQeuZfX0oKCcZM&G(KST7A@ABohN9lw%DTa#nZ9A_qO89xV`N@Gb;)d3Cen>eiQlvJ
a{3pWD&g*<C*3b5rxI%=HwLzq-WQNJPTGr155oc@{T%<-&a90ug`b#7!t%H7mOyidUB?cHiQ{M;QL=cq60HAjp@-^;5zr%|x~gSZ
B`u-a4Z|5EnXdvyY{VP%ZkU5CaL<5%)=zqWaPW+q`RD7oV*D`fLyUnp4A({+mSh)TWcLduTzMzy224a0X1ihuBF0>D25w?2f*9*Y
sRCuR&c~D|@ITZL-ll;uM;I=(BjF&2hYX2}FV-%!<gepp_m+B{%~38uspOEm&UiNbjkTy&2x6c-hsQG9^it~fB&av}^$j2a>N**2
PlB{{y&^3qrnIxG?|6BY8bE1~*_{kJme}<?cmceGvV3L4RQ4DTrI|~dcjXl%@~RHR^;LV>jL&s^2}F-jNjEsU*eaybrW5L%`k4C_
bnm^0AFWdwhJACA1<4@?j{CA39et{p(>L?{V;pdU@)tKJYw{!PauWmB>$@td@G|(pJ<_h|e-a&M7@RihQ5-DwJbZxTNN#%nV^*Mx
fdAJ&OX-@B8*hW(+~_A5cJ|Y0Vp;LOL{H6WifX;c!3i)QO9(tX7g`ClxBsvO&wve%0RwBvayTEetq7eaG~Mw%H_dYd>z?UT+_2#U
WftX;mLTd0tP7~MRdgn?OvjOSd$Mv{q4Y}@A3e4xyGdNqczSNFYaUW@^SW;Dai(dvPn5b!>Qb#tXhuHJqOEAwww=Ll_$mKZoaAJf
;INl;J^slx0D$AnFH=Wp)~M{iM6DE-w}Ue28sA$m;F<)i705fyP}5&91xHrwwot{Tz%wNdC2xM4D!SqIkseY4?cY+S;GjaPHp38g
5Dv?i?&Waw&&0m=@=Fs_kk~)-L2V*ma|G4Be6KYTZds?h$7Mk8i!v!cq8V1;DXLLSEdol10$)27Xn)2DBI`r7rzds<`VAHLw4oOB
QVtaSj5t;JX3X));YQ@(UvIx_XBY^=TDLfKQhCr}pFbPNthnW;&HZu&u-pVOtb3aH_&5<^+{u|KpwO1*7c^>6nqZ0JLI*)g+iLoD
T#a)`r1ncX)MhgvMc1FTw|a7}S!y)~h?-gubOhKX6}Q9$`8`)|7hD1i=>CcYc*z3t{}8Er6u)LHGWa3BvFUeBi{AHbg6-3QPda<f
tfw|EcbJ&W6Xw2$JdU%HH=*o;P?qdYYLFSF32)bm8YxxN;fgpfkmawNo{*&I7fVfhhfWv_`4y4!`Dr_y4H<)i0Yhw`S)#MtmZd-7
&P_e*M_eg7922e^*agQOPx#n^5=2LPXlJSl$-4Fs8l|mN@Xz1ly&o2zT0R;55{s#~^IPUu7p$QI?3I%XpEbk~JS|E26Ri^z;z)Yl
<pd;sSC5*iv`wIHEAWbuUWDMYN0-_)_eT|egI*_JB7@fq^ywbD@n;iV1$G@D?`tu=v?Scx>&u?q)`~a@yjit6k3>krOqRMyv^{|4
$~G5G*Pff~P;GmnJd9Br6ASuBz@>HUXWIN9?B1kbJx3V5fc-fm>iFBJW}$gNaGe9i#yO6JaXCnH5-@+yja<Z2(;+#dzQA%eGV5<F
@-=Yt=5xVxd>D9%!BC4v;v#9qs5G0nW4H})h5mfQencD_m(^!^Eg+~Y(PN6LDiOd$H7D%O<H_wd8Y<<+vhIsG$;_U!wUcQ1zM_!B
*)QZ18Gr>HZR}l-hclcWwp1hYjX-<^&bLV<0_rl43w_9O#_))=-s=1Y7c)!e-WjneJs88kPPG9<LI_m`GjgMbZP8{ZQZj#=Kzo2=
fb1_PJ|6w`t3Fzoz1(5M1n4;Fz*>4G%!TOs8t9}MK?YRMJweTpUHSLf;+?Fkk|8piW`Eh_)#kM!SZL&YjQV_(SY6s~E?|Wz1Jhbn
6o<@AZhBnyb4j1#(`*98DkbAbJWZnq_e$};@*+USB<q(Bc@OY?EH-7j^Kv12&AJsCfnBDRUkIIg^xo9-6uvQ;IU(x;oeKu90p^xA
-1hVm*-9Fz=Noe!rSW9<<9Xkl0H_krK)y9<(KBs5mXJpiUHot7(08`(xY7AY7k@%!>TuiFJ%>Eqs8Ry9X$(eN;2+gVEb*BK)9=l>
G9{f8BSCEF=Gtg`gtev>cZ3iQD!7T&vh;L@Gye&EU5|sT%&pI<)Mw>knF#GrobBlvZPsOA{H#zKMK~1re#8(z=G%m)I|QhogJnb4
>t*ZS30Kht^Yw{X?6%kX1QaU5CKnRQsFu3Oe$p!sz*u(xAZi|Nan!~#kP;vBT)zpVO2qtB4O4KBcs1xxlXskl=xi)2zPFmtiqHg2
7;zIj{lB)BiBC8(LWCEK6>Y|?fSz&s?3HIU7$1O59lv_A3duVwg)uU6D1cYd@M#qmwDytisNG2FNoga#rt5{p8Cl*Exc)`Qi0lj`
M8fpWU5g!}q>P)N99|-S#IrhUdFUyWg&}t%rUNvg05{(IdYr%k>(VFHee#?xw}crKp1&m8xn70m*jVP8Fp&nMvbb#*qC(@Xt`6j{
Dr&p8BdI9Hqc>n_1EpGLRh>|FQbKxWcCKcG#YLliM*1c;NYezlbOjvIYFh%vJuq$$>x6F46k_YtxxQCpq>IBT9>q*ha%UKPn~b+g
f&F`2z!*H|d)euJ>46In`>VPH8M!&`!LtZajlO`fB3_3C)IJl)@h91y>8w{T94vmgJ99r%n5@VVZAWl$qkHsA)%buf=)(z;HREJf
dhKNMKy_mi0{l;&?}MavbZ+4gxEi_B>lTQgsBW-zk=8^dGbQ3_CMt>=O{>QK{WQO_+%8*?qOCz1&f@bE*3-!|8+Z@T_RYdtzAR+6
yQ^gTKDSf?asibjZ*u}0q({rtOP|S0cmeB28H`B0TD=XUxPAv!rvQ%?0z#z-$P!8uqVCcIci)F=7sq0U5zB@ueev-?D$?Tx<BJ42
Y~|I^Xz}l2%-78_qw7l420m)Ss?(pyN)J10kako6uaOy4OyJ<Dn>D`SNQk*d6gqORIIhl@7<<93xQxTRU9{ozDlWu2>>Ri@^T#0u
0A1ByBmy`@p5RKk)jw41pge?-HeT=nE{gd?E6%MYW_$1v*?ySw>vBx*A6hjK9KClZ!2g-@FnGkF2E33$`y!^2$SjU5`t<JPA?m1@
O@NGt5?gh4SHmGqd_v31*JK;E1a{O!$PtwmDp4HK_1NTkFHx*jAj5^VC^(NVfS?`-2D(|$NIi}$aXss%5o>JFv#QFj%P)#1PFT}R
ATro(B`ANwwsz~4Rjlkn)u1;hb|ur@iPU}Th}q=~8W$ET47$W;yBzi8=cpJJ2HuXhZsqA+%%14B)bCqkET+&I>l=hwm3Qds*V;_k
Z_@gXJOX+JL%)uenh`P|uuNNzzau<w?vu0}bpxb=HwH*ps1%2C3b^bA@E#X<Oj5XOZ-$*r8CdyYjk48#AS=}4DDP9ZB6JTk;<bVO
MtOH_Q&49A#aBYbxUYeC8h3<!DMdg2y9Y*8K}l0TYJ0P)!~3-{8E?KsE-2iN%H1>DD(%u46fbdq(|s4^W39e`F5g%bpNonut7r2z
ssq(m%T%{vs-2&i-zhe7^aE|+5y%u;il!kM3w_%wie<81uh1}Chggirx_tFsAxaZXdT=VC@j;t882vX<)l8j6MLIw~1Jd1$otr0n
jag#L5zwQyACu8h%l+p9R_D*6LWS&v3qALK!M|(K)vpj668sr3E;{xfE!c7A@04x}@TLg&m7XSdRD9kV?DU{cH1Ci}{1pv=kZG#w
7M|B(`;mTN=?HO+cRHydNNvX+e%`YGXs@8Lh$?e5#PY=mW3jPTYE2780F!U8ETSlFPVcMIbu{V2Of+^IrH&Ey2hj7^7E6mwRwI&i
B}_MVcKA}BOo4>Dq;Lie@C<4vZXC9El^D7O+?!~?#)k3%4%}SBahjT7@ez%Im-I2EhbTGQJ*+GCGK<f15KrqrZF@Uy!C{w=ltZmB
wIOYKT0kJEY5RLOJO?j?Y-*a%@5I8y;-K?e_Y5Ub%1i_&K6%?z!X8>nj@MXw8Uz9Fs$`kW>w2(V_B6*o&_)4kAKOT7%yG3S*_sRo
-44#E@yJzZY1GS^(8`B?+uBit7oI=ln<4o@jHd8-a^o2HIamDqS?iZiYuiK>jeiP4>0C(+z^f(0Ul0P>`rW+pi!QMtT^8jP6s5a)
CeixStT{%q$LY2z-^;womp*zFBZ&AAIeZv-0lgr&gad(2kAxm4VOc)$7<@7=uLLnE2@=D)y;$(FL+<uVJHZyaSk^(ozbrm7M(Ree
1uPY>F-A6mSEkBEw6J#I{#W@wGU}jQ1{^`*+OLmRqlv^-pOe=IO-|Za=8Oxei-1}}SiaUw?LLzeetC@5Qi)OmCD~HH4#N%25xAl1
1UnI8LtV;W_|mD{1^Y>{7L0n|{g0-a_`<WOl7E?+Lq;1|4$Qhb#FRP#Gx{JQ-DT||M1teil!xiOAP?tspRi>OJ28twXEbJD<Ju7r
eC-LCZ|@*3QL|^by}9YwcHGZBAB}HjnE!csu3G0m{*Wax0Er>r^k@u`E$|jMetSYUhKY(-IicRD7N_gufvJ+F?c#wxOnb7Sro*)$
!aAS7hsetN(;3zcHCS)Twp#66ZVId^E8$?3UijeetjG<aQ7$G`Wj92e9t$2nA=!-10_`*^H2}FMp5Po^aiw^AbijiNzpukco*4cl
XP4ta!^^g2vbyW13@(}gMn^hbwszG^l2>_+$K7xf2yj_N_G|bi*BfyHge|QZG=&&VJ6r97!wBpKec##`no{&a6B-=8k4c7HE%Y^Y
^+oIa2$bZS*+i<kOgA^r0Awg+dXJ&B{LbAGp39JdPzlx7zSIXzwl0aN^ej{wZEAD*jyXL^iz}{&TEj36(qs!gQUH?tZJQR?xD|;1
hHS@p#@}{>12NSGb-_m0K;J{N<xkShXVUHMlU|#z74M}qs7FsIWg4&BMd^9O_MWP>rfbDhN^i>#t%f7X2a%}7w%&#uj<4cWj1}14
-Dh^|q7G7i8Oup5<K~a_b0#zGa8MNAZ=!eUI>01X$Accm#lUy)HPz(JNfbQL<F^_53(23VTMx)i6mH;LcYASQ_ZHlbNT%-g%<_-&
!Sg>{gOjs8lcOUaz6q&MO)e$2!V0Y|IGh~K#`m)_@|FR3Vo;e}_ZtVdDWn~3QBJP$=CYM>X9Uj5!576`wcvxEg~>0kT3B$AvYJwj
bVp7Ouj6_xMSosxd1*oU3kJvAy#p?q(2rBk8;_DW$QaPLCSuCvVIJD4%j4u3)(PF`WleI$?^P=ZAnQ9<Ev8&;R#*>^)@_vuFatKW
4s^9uw+{@BR7fQ%XsqN{8Gy_28)>e%&9v08#V6Zk7y84}GTA{F9zJ>!R3VW-vg3)cWR?U#wl1Lj_XGBvtD7T9@A9?uEW9_L01=}0
-lyO79o3@(=O5+kfB&-LA1i3t@@mRexfzi;5m!^sk-}WS-6Yy>Kr$TdtBXpqZsj3yJ}SuD#X1}+$xTUaE5Q1O(V@7KJAZx#@VRny
bW5V-(!$GFI)?QDm0<V@-ZeZ@44L)gW`V4WmLafRR$Z&z%p+P&3{R?$5WXLz)GZ-@s-EI5jmU!Pb(e*O#aJp%eoopgx+8~Eq+ukg
f`kL|UP4-tulj(at=kSU5)Thl83<ZXc9{qfXdoRv0rtMgb8uir8<f<P#`R`t8#jp6U9q;Ppzwkq=&Z38gZ-jL^v_2@&kI!gBKibt
kNDfjyjoMM;{`L<rho5`)ERABFO*<Kqv_7q{*=9YdP;b9S}|WQi2(BU$tXd;pOy4=uNw7utO*Z+BT6mIpQT#&7Qdpz52JuJuutSp
be+p+g;B~H&eyQf-2)?n0taS5UKvRv(g3pLityrz@0J`pcvt+p0zchy>}L~E6_4wVf?R!y7#eRb@R$qKwGEy9KxmCDm;KpQ`bsxB
*@qxE0B4u}<`PJ|hUY;rd8AvdpNvG{*;_LsFpUzIr}>~V06gA0;CK<4(9Vtq*kv_w?#_SuN+<e773FHe=}L=Jg0SOok%7btSDm1M
)sTD$=K!1Tih-G=qZE(F$@EZGwl&XEa_|1A2I7<O`Fz_)*YCFO=LmPkku*{%t}n4e25fJo0cP>rVQ!Iqm-6}1UP#2D#@*Ps{8jE6
g1_SAa{Ffhi2f{T+}+zYd_t`D6UR1I;_+X7=eJDQD&s^V70VPDQON3NnF_CoYv_KR1e70V*1F_)QkJ7S{}1I|q0ATRNC*iHr}C!I
!{AYeD!WFB<zRM@zbE|PXNZD03*-1qS#95U10Oec2YlhfDRBGDZ3$OeCE`2-dgCHwx4G-N=wA%~Jn3GWBH=Rx0lB8dy{5Xlf;}+F
Z4lhm+?o;T$g1bQVLUbwLMFU6;ncIMDDh6HzWU$_^a#7vNKErEa=<B?r!vn}(0I{NufU}k1((sZ0(;{~6U>5jPLs$^#4YC#hUg<+
o-aF)d<dx=1KxI`4u8nENQR(Rp0W6Avg$1ZRtCl|H{jE3w9|c{2J}qJMcc0j?_XURp!;B!kazBwC$9FxU4WGrT_;)e58L=?<)Vxi
%bWqeAMqNmKai#OJIXN!vmXu)TrWT(CG=fi1Af||=hlPLR0St~OxOWx5)qEBo3<RHkom34GbA8a(zx=q-eUi|YNu=49TBD~WmXJ9
{&cvNi6fR8-IWRk&Jilp?tzcsq@bPXDm*JB0P)d0Zc01=hOtsPHSXJ`+eU=BAU@$O(?D-f7dVhp!TjsvS+W}D(4?nb&YGP7>Azi(
g~U-oR?Ykm!hOrDJ>WY6@PggP4YP6a^6QhXFo#g;M|VCK#eWm`>Pl&w3rAaxpEMpUY_tDKfzbuG{3_*t;O{y^0^GmBY(mZ<9iOw1
n%T2hxcHSLgc`pC*a5@)*Z623C4A^BMElhq0|JRe&$#=@#V#imq|D10U!x<rV6upi>L^-Mam^Jp;8TSl3Xvq5>TWl*zXwEBu;{tL
n;<3W>PD4c?y83=-8jh*L6IG#ap}05T7V%6B)q|<I9EaCidVZnJJP5#hymrxQhv`<^V?!>VzvdPu31I^Ze?Tz{iV!Of%mVERJ&~H
?#LH2KVGUpYDRgtKJBL_G9y(glRDrFzl+?}(w`A;)y9rL9Yq$&SzNiQpc|Ov>FGq*vl$L!98zr!c6wIMjw*|?2~T#t$SExY-d5Ry
61OCX>XO&&?v9URU!4L%)u@c&IvU(-4xVTzTc+C^x<J_P^o2V(js4mxXs^!Husdj}zFh@@0Dv$=flBNXQJDncZN>nB+SVjP=i8yP
7mkzFnFxd{kz1Lc7Z;6_LRFd;fwR=I6||zsmv`znYL-rW;vIIX-7J!eGy|!cAv>W1q6$-0H0>Z63=f8+BM#i~8E`03%g!pivQvB^
=%kzyc3?XTslEKhjnX0fdVc(LuciW}4eb`|4g(RvI~8`@4Bf128zJQR;Xozfhgmy<*D=hxZ~4-0PWgaH$y$;tU*uUf7{Q$}B}$56
>PD!;^4?#ev;N|Oe60RDlOVp9Q@a#ONf&pJ`F;bZP?LyuJIkSr;2q=J^*@Gp)>t+vNAC?u|La>zJ`-B49i_9yl9Igh#TqQCUwdZM
$*;i%U9{%7i-*OuT_yyzC`W<^68()g*|-4T1gVQOZnGS<=^bv2YgV~rwRuBa05z{n2H*HR3-H)-l2aoA$9i{36XbmvH5;Aw6x^jE
cN68+QwIjT{3Tw??y<gy<1f%;)dAJzqt7Nt{tDq&>@XE1)yYPEmW;cRPjf+qt(G}CE-svz9Wz^u3RS70cz^#3A|R<4Hy|*Y{&;R(
v7tOMK!0SdY-y<-rmY}6N`sRE4nlNInA}+aR`yj2COW3RRZK};_e!YV-nrZMa^(P2rQhoa+xeFrhZ-V-J62>H`2$%9ctffh%)Ciy
)9w%CPI?7$dL)x;b_$;NClS}S+=g>osa;Vx54A~B#9JE6)j8>60j;TOiEi$kg>LPgZs@>>?Mb4%YSw@<>zSFtq{5NM-LeruMh}%R
`x;>dV_&7rTagfk;LuS-e!PG|?$G4GFrq>u2|ule+CSPmTHQeXM@&wUjOb5}*tFIxe=L~%v<}K@q-3vggb{#_GlCZW7}U_v+)j9`
23t&qbMbH|0%ulW_5lKHH&KWewZc*6Ki<A@lP4088tD%Chsc;aJI8rVAPU=CRt&MG+qaL~eeO1)RTln#O_erUTjkLuk|LtsJWr4V
51dZ%aOy+A{Vxzu>I~eD;>iAyx?nd#2z~r1#GrTVp4}bgdYU+hC1QJ^-*6w|oZAj+wZa*_z5X|6ZmWNfKi|_JDvY+2vN$1XQ8}wf
wZ2ZfboI55P(P>f4a^Fx)vpZh1cOgfW@}5!SZMff3`A2zujEa{Wrf#Rcz7&Z3bYAPQX_Zs!u-^oaO!7=CC`pZfp2zrEYttT>PU|`
^IZWHLB`=0^waS-tl}f_Ufo6#xI6nF4(h+ri+y90ueY54SFU?&y2NxLvMfOFwU8ou4&>@ytJ6tA5^g;E&rR80`eSQE?ZU@X@_Gpc
(-Q{m5e|}e2bd=N&LdrTh#RbT(=a5vCdysx*qJ5=qM3Ps{j=-ajVB$;C!3g8<%}ZtDEpaan-uNS)Bjkb%tlmYTEZAhYvYiKHn{(j
E<+0Dp5wdE%la2tab2TJpog^ge-b}?xXKa8WBAd08QdJji_0@FZR08S2js0I!dDp9%X|ZA)+ys!LKd+zQ;MfevMK{@*8#ZvDvY-?
@3Kcx1*gVGgz$o>9`*))W{!Y!CpIa>fodoaPw7MbIIesr%gUUz!CoUo<`?==WnDQB9`v9{Lntd3^4FTwC+*`5;k%I$6OYWV%Z2(s
ykYawA!&)utc}AjM0oI^h-1j4dR&K(jvs0!%iSKhKwMePsA??zV#NZe{#7XC7KvDUYr8^o<XTUeoewx4&r^0dyKZHv0%|Qh>WfJ;
q5nvH=QOI3FCnbZ-#)xZl<)Z-32IL?nVj7|GG*^TauU|x_|@AmDPspn<*Nf$aa%rl4G$rLvtM~Zl&l5V`Ka+F);S@?5Yi>xyLFiA
umbR{s8Y8Kh_<fsDZx1vzi!$MgQZ~bRk<&K;EAZ(>V6LGm--lpkzMB}u1b|aeKz%<4U?RFCdzZ2Ryt}f>uYrppHU=S`orxF4^c*3
Oen$uxtG&d%DwdKjENvdrmnORWTHsX8dE>A(JCB$t1*U(zAZCRB-vJ~?~HWfsINHDC!BTNwffM!0_Uy9{Y^^S=w47@i8OY#O2p8P
1F`?rc%Ep>HRHgj`kgNt)8A%Qi{$RxZ)y%j8`gt12<lv5Bw+f^f&zIM8(qOff+;-ijIDS&uk?rrqAg|aZ*TUac{es)dy2)LN=FDL
dUbEKr=n>dT%$0`gnHP90cN;N-vcg2I!}#%jrOj1#p3T^HJ-2C!fng-LntQ6=|U|K*dq&n(oqh!HoUBNfw(y|ut$=bDGG&mAfTkY
wejUqoN6qqVb_9juF}ExD=o@fDLKu|z!f{k>u&5=-OuZ!`c=_gSpM+rLGvDX+6A!~TYT=CEm8G`Nhs*-dxyf`%?}UG#F1Qsby|f4
|GU7@O8G`Bdy2^f1LGS<R&l=FS}Jlixss__Zko2UgSyu9DX@KvXYWPp*5h?lY66GkmpB(9*nGc<Dnv&+Z0(QPO=<2iDn;@pNsXfT
E%FMa*mU{eZa=Pq`ydy3kbG`dPbN`V5!x0fk(l_lI2^X!czjGS&wcTb)-FzxmF;#6_POo$L2Gbok1q!rYYUnM-vDEHSDpnD0*2Sk
v;DtW;5bn=rL-(9xheW5EAq}IZ7CWdZ_G~$cYai8rBfXN6%YIDKq_3JtaMM_b+f7}xEz<}?^%pW8u{|7ndP`6$&WodO7~f;LZE&S
`GsTRRPzr6DjGj$o^p{s3^gE(l2cVw$EL7QqT_h6q`x!V>~;v$w<}Oi@;tlgrJC8`CKoy1wK{m9k>*fVnqbt(r@-pEvxvD!+O}n&
<fSJyKs7`<>+Yxxs$VVm3YIE!)EaHyK&X%CCfH4Tk@m3`m)3Gvk5I~R<1*TCmcYHsZmd)z6v`@vQcur^p9T~2ni~U!^%#;$yZ`_I
LZl7!iWnBA00Fv_0ja42p6+{QvBYQl0ssI200dcD
"""
SIZE=54441
SHA='6975ea6cffe6333e24626a5681a5ca5a1ddf5312a3a884a9795f73baa8650232'
def main():
 raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
 assert len(raw)==SIZE and hashlib.sha256(raw).hexdigest()==SHA
 files=json.loads(raw);manifest=json.loads(files['MANIFEST26.json'])
 out=Path(sys.argv[1] if len(sys.argv)>1 else 'AFFINE26_SOURCE');out.mkdir(parents=True,exist_ok=True)
 for name,text in sorted(files.items()):
  assert Path(name).name==name and name not in ('.','..')
  b=text.encode('utf-8')
  if name in manifest:
   r=manifest[name];assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
  (out/name).write_bytes(b)
 print('AFFINE26_SOURCE_RECOVERY_PASS',len(files),len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```
