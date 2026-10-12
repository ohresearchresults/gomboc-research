# minimum-0208

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# HEX6_DEEP_INDEPENDENT_BAND_GLOBAL_PSD_NONAPICAL_U_V4

## 1. Main result

**The entire deep equal-cut trajectory is now excluded from sole U at apex 0, together with a certified narrow band of five independently varying cuts.** The exclusion holds for every SPD physical metric, crosses the virtual-pyramid horizon, and controls lower trapped maxima rather than assuming that the highest nonroot cannot escape to the apex.

More strongly, on this family **no true-edge arborescence rooted at 0 is weakly feasible for any nonzero positive-semidefinite metric**. Thus every possible rank-two metric boundary of this family is excluded as a limit of genuine rooted-U1 systems. The theorem does not confuse this with counting strict unstable vertices at a singular metric: a new exact countercontrol has only apex 0 strictly unstable in that singular vertex test, while a collapsed nonroot edge carries a closed two-cycle. Its positive-definite regularizations have three strict U vertices.

The proved completion domain is

    there exists t in [1/4,1] such that
    max(|x-t|,|y-t|,|z-t|,|u-t|,|v-t|) <= 1/10^12,
    with 0<x,y,z,u,v<1.

It includes every equal-cut body with 1/4<=t<1 and a genuine five-dimensional independent-cut band. The width is conservative and small; **this is not an exclusion of the entire five-cut cube**. Closed t=1 strata are used to certify the limit, not counted as ten-vertex witnesses.

Every actual body in this band has a nonapical strict U under every SPD metric. The conclusion extends to every actual own-centred realization of the same labelled true-edge graph within Euclidean vertex distance 10^-11 of the band. No stable-facet, saddle, conditioning, chosen-forest, or local polar-arrow premise is needed.

No full-U1 or110 body was constructed. No other possible U root, whole combinatorial type, canonical count, or global mechanical bound is closed. The interval remains 34<=C_min<=622.

## 2. Source authority and literal geometry

The new journal was read through its actual EOF, including the complete literal parent:

    minimum-0207
    SHA256 acb40dcb4bb79552340ae90405e0af1c37fd8044f44a91bebd1b501309d079ef
    HEX6_GLOBAL_FIXED_POLE_ATLAS_AND_COMPACT_METRIC_BOUNDARY_V3.

The supplied journal has 288178 bytes and SHA256 c6fd5dc21a2f52d30587196753ecbbbe6f7e593fc2e2f9d11aae00fcac0b8d47. Its embedded V3 source contains the transcription tokens `ndef ps`, `ndef pd`, and `ndef pe`, whereas the earlier same-chat handoff has `def`. This is a source-delivery defect, not a mathematical alias. The new computation does not execute that fence or depend on a repair; its complete autonomous sources are embedded below.

Use the CHANGED hexagon, not the original integer hexagon and not a degree-five pentagon control:

    p = 1/100000 * (
      (60401,-32565),
      (80000,-20000),
      (0,60000),
      (-80000,80000),
      (-483861,-325040),
      (-447814,-355009)).

Set

    A=(0,0,1), q_i=(p_i,1),
    b=(2615613/500000,816129/250000,-3),
    B_i=[q_i;q_((i+1) mod 6);b]^-1(1,1,1).

For the five independent cut fractions, the source vertices are

    Y0=A;
    Y1=B1; Y2=B2; Y3=B4; Y4=B5;
    Y5=B0+x(A-B0);
    Y6=B0+y(B5-B0);
    Y7=B0+z(B1-B0);
    Y8=B3+u(A-B3);
    Y9=B3+v(B4-B3).

The true maximal facets are

    F0=(0,4,6,5), F1=(0,5,7,1), F2=(0,1,2),
    F3=(0,2,8), F4=(0,8,9,3), F5=(0,3,4),
    F6=(4,3,9,2,1,7,6), F7=(5,6,7), F8=(9,8,2).

The true edges are

    01,02,03,04,05,08,12,17,28,29,34,39,46,56,57,67,89.

Thus (V,E,F)=(10,17,9), degree(0)=6, degree(2)=4, and the remaining vertices are simple. The partial cut through B2 is retained literally; it is not replaced by a generic truncation. The parent’s global atlas identifies every open-cube source with its unique uniformly refilled star-centred fixed-pole completion.

Write U_i=Y_i-A and

    d_i=1+c·U_i,
    X_i=A+U_i/d_i.

Here c is the unique positive-actual-denominator parameter for which the NEW uniformly filled body conv(X_i) has volume centroid 0. All six actual apex poles are exactly q_i. The same c is used in every vertex, pole, moment and physical primitive. Removed virtual vertices are not assigned positive-denominator constraints.

## 3. Uniform all-metric theorem on the deep independent band

### 3.1. Actual volume and centroid, including unequal cuts

The seven positive apex-fan tetrahedra have nonapical triples

    (4,3,9), (4,9,2), (4,2,1), (4,1,7), (4,7,6),
    (5,6,7), (9,8,2).

For such a triple T={i,j,k}, its actual image volume is

    v_T=det(U_i,U_j,U_k)/(6 d_i d_j d_k).

The displayed outward order gives positive volumes in the actual open-cube domain. The uniform tetrahedral formulas are

    V=sum_T v_T,
    g=(1/V) sum_T (v_T/4)(A+X_i+X_j+X_k),

    E[XX^T]=(1/V) sum_T (v_T/20)
      [(A+X_i+X_j+X_k)(A+X_i+X_j+X_k)^T
       +AA^T+X_iX_i^T+X_jX_j^T+X_kX_k^T].

Thus Sigma=E[XX^T]-gg^T is the actual volume covariance, not the covariance of the tetrahedral centroids. Independent cut changes alter the same determinants, vertices and denominators simultaneously. No tetrahedral mass is a free variable.

For fixed actual source geometry, differentiation of the uniformly refilled star image gives

    D_c g=-H,
    H=5 Sigma+(g-A)(g-A)^T.

This identity is used to validate the actual centroid, rather than treating a rounded Newton locator as exact.

### 3.2. Complete continuum certificate

The proof uses 330 consecutive CLOSED t-cells covering [1/4,1] exactly. On each cell, every cut is t plus an independent constant offset in [-10^-12,10^-12]. All five offsets are enclosed simultaneously.

At cell midpoint m, the source deterministically constructs rational c0, c1 and an invertible rational preconditioner R. Put

    c_pred(t)=c0+c1(t-m).

A literal positive error eta is supplied for the cell. Exact interval arithmetic proves that the Newton map

    r -> r+R g(c_pred(t)+r,t,offsets)

maps the whole cube [-eta,eta]^3 strictly into itself, uniformly over the t-cell and all five offsets. In detail, its enclosure is obtained from

    R g(c_pred(t),t,offsets)
    + [I-R H(c_pred(t)+s r,t,offsets)]r,
    0<=s<=1.

Brouwer therefore supplies an actual zero of g for EACH admissible completion in the cell. The unique positive-domain star-centering theorem identifies this zero with the intended fixed-pole own-centred body. Predictor convergence alone is not used as evidence of centring.

All interval endpoints are outward-rounded integers divided by 2^90. The successful verifier uses no floating arithmetic or numerical solver. Interval jets retain values, first and second t-derivatives, midpoint values and midpoint derivatives. For fixed offsets and r, the scalar enclosure is

    f(t) in f(m)+(t-m)f'(m)+[0,(hi-lo)^2/8] f''([lo,hi]).

Taking interval coefficients makes this valid simultaneously for all offsets and all centroid errors. One does not differentiate the unknown true c(t): it is enclosed by the validated predictor cylinder.

The verification also proves d_i>1/2 for every ACTUAL source vertex throughout the band. Some interval expressions include nonphysical cut-boundary values as a conservative enclosure; the theorem is restricted to the actual fractions in (0,1), whose stated fan is genuine.

### 3.3. Positive-definite stresses against every rooted tree

For each true directed nonroot edge define

    D_ij=X_i^T M(X_j-X_i),
    A_ij=-sym[X_i(X_j-X_i)^T].

A stress row consists of positive integer weights on some directed edges. With W=sum w, put

    Q=(1/W) sum w_ij A_ij.

There are exactly 4335 true-edge arborescences rooted at 0. The recovery enumerates connected nine-edge subsets of the seventeen true edges, orients them toward 0, and independently checks the count by a Kirchhoff determinant evaluated with Bareiss arithmetic.

The complete literal certificate has 389 stress rows and 1415 terms. Their support sizes are 179 rows on three arrows, 174 on four, 34 on five, and two on six; the largest integer weight is 1000000. These are certificate rows, not combinatorial types or canonical orbits.

For every t-cell, each of its assigned rows satisfies

    Q-10^-8 I is positive definite

throughout the entire independent-cut and actual-centroid enclosure. Every one of the 4335 trees contains the support of at least one assigned row.

The matrix test uses the two affine Taylor endpoint matrices with a common interval second-order remainder. Both endpoint boxes pass all three Sylvester principal-minor tests, so their convex interpolations pass throughout the cell. There are 35416 row/cell applications, 70832 endpoint matrices and 212496 strictly positive interval principal-minor guards. These are interval-Taylor certificates, not a sampled metric sweep or a Bernstein certificate.

For ANY nonzero PSD M, contraction gives

    -(1/W) sum w_ij D_ij=Q:M>10^-8 tr(M).

Therefore every rooted tree contains an arrow

    D_ij < -10^-8 tr(M).

In particular, no rooted tree can have all its arrows nonnegative, even at a rank-two metric or a finite weak-arrow wall.

### 3.4. Forest-free interpretation and nonapical strict U

The certificate yields a genuine cutset conclusion. Form the directed graph consisting of true arrows satisfying

    D_ij >= -10^-8 tr(M).

Not every vertex can reach 0: otherwise choosing routes gives an arborescence and contradicts the preceding theorem. Let T be the nonempty set of vertices that cannot reach 0. Then 0 is outside T and EVERY true outgoing boundary arrow of T satisfies

    D_ij < -10^-8 tr(M).

For SPD M, choose v of maximum M-norm inside T. Every internal true neighbor w has

    D_vw=(|X_w|_M^2-|X_v|_M^2-|X_w-X_v|_M^2)/2<0.

Every external true neighbor is covered by the cutset inequality. Thus v is a nonapical STRICT U. T may change with the body and metric; no single fixed cutset is asserted for the whole family.

### 3.5. A genuine actual-realization neighborhood

The inherited actual support argument gives ||X_i||<18 throughout the fixed-pole atlas. For an actual own-centred same-graph realization Z with ||Z_i-X_i||<=epsilon,

    ||A_ij(Z)-A_ij(X)||_op <=72 epsilon+2 epsilon^2.

At epsilon=10^-11 this is less than10^-9. The same normalized stress rows therefore give

    Q(Z)>9·10^-9 I.

Consequently every such realization still has a nonapical strict U under every SPD metric. This neighborhood need not keep the six poles fixed, but it must be an actual own-centred realization with the same true labelled graph. Arbitrary independent coordinate perturbations are not declared convex bodies.

## 4. Rank-two limits: the collapsed-fibre obstruction

The following analytic lemma is independent of the finite stress catalogue.

Let P be a full-dimensional polytope at its actual centroid, and let M0=L^T L have rank two. Write y_i=LX_i. Its projected mass is a positive constant times the ACTUAL fibre length of P; it has centroid0, but is not generally the uniform area measure of conv(y_i).

A weak projected arrow satisfies

    |y_j|^2-|y_i|^2=2D_ij(M0)+|y_j-y_i|^2>=0.

On a directed cycle the sum of the left sides is zero. Hence EVERY projected edge of the cycle is zero and every vertex of that cycle lies in one kernel-parallel fibre.

Suppose the weak-arrow digraph has a sink strongly connected component T not containing apex 0. All true outgoing boundary arrows of T are strictly negative. If T is nontrivial, all its vertices project to the same point. In an actual open-stratum three-dimensional polytope a line contains at most two true vertices, so such a component is the two endpoints of a genuine edge. A singleton is also possible.

The linear functional y_T·LX is maximized exactly on this vertex or edge: all its incident directions out of T are negative, while internal collapsed directions have zero value. Thus y_T is a strict radial maximum of the projected polygon, with an actual vertex or edge as its exposed preimage. This is a geometric obstruction, not a choice of fictitious projected masses.

Every sufficiently nearby SPD metric, and every sufficiently nearby actual same-graph realization, retains the strict boundary signs. Maximizing the positive-definite norm inside T then produces a nonapical strict U. Therefore such a rank-two configuration cannot be approached by genuine sole-U0 systems.

More generally, any genuine sole-U0 sequence has a subsequence with the SAME selected rooted escape tree. Its limiting PSD metric must satisfy all that tree’s weak inequalities. Counting only singular strict vertices or requiring one weak outgoing arrow at every nonroot is insufficient: it admits closed collapsed cycles. The new family certificate excludes the stronger rooted-tree relaxation itself.

This lemma does not assert that every rank-two projected body in the full five-cube has such a nonapical sink. Rank-two systems outside the certified band remain a substantive question. At merged-incidence boundary bodies, several old labels may coincide; the two-true-vertex assertion applies to the actual open stratum, not to those labels.

## 5. Exact actual-centred rank-two countercontrol

Take all five cuts equal to1/2 and use its EXACT algebraic star-centred fixed-pole body. It is not the earlier rational star approximation followed by centroid subtraction: the latter has a slightly changed pole hexagon. Here c is the unique positive-domain zero of the actual centroid equations in section3.

Let R have rows q6^T and q8^T, where these are the ACTUAL poles of F6 and F8. Define

    G=((917/1000,1/5),(1/5,83/1000)),
    M0=R^T G R.

The determinant of G is36111/1000000>0. Both q6 and q8 equal1 at vertices2 and9, so ker M0 is precisely the direction of the TRUE edge29.

Exact validated algebraic evaluation gives:

    A is uniquely globally farthest;
    all outgoing apex primitives are strictly negative;
    every other nonroot except2,9 has a strict positive true escape;
    D29(M0)=D92(M0)=0.

The complete weak functional graph may be chosen as

    1->2, 2->9, 3->9, 4->3, 5->0,
    6->7, 7->1, 8->0, 9->2.

Its sole singular STRICT vertex-U is0. Nevertheless T={2,9} is a closed nonapical fibre. Its entire true outgoing boundary is

    2->0, 2->1, 2->8, 9->3, 9->8,

and all five primitives are strictly negative. There is no rooted escape tree and no inverse physical metric N0. This is an actual-own-centroid countercontrol to the false rank-two relaxation, not a U1 body.

For the entire positive regularization

    M_epsilon=M0+epsilon I,
    N_epsilon=M_epsilon^-1,
    0<epsilon<=1/100000,

the strict primal unstable set is EXACTLY {0,2,9}. Both Euclidean primitives along29 are negative, so the collapsed pair opens into two strict unstable vertices. The five boundary signs and the other chosen positive escapes hold at both epsilon endpoints and hence on the whole interval.

At epsilon=1/100000 the complete physical census is

    S={1,4}, U={0,2,9}, H={04,29,89},
    strict(S,U,H)=(2,3,3), physicalweak000,
    all68 true-edge primitives nonzero.

Only the primal U={0,2,9} statement is claimed for the entire epsilon interval. Full233 and weak000 are verified at the specified endpoint, not silently extended across every polar wall.

## 6. Preserved deep and horizon controls

The recovery also supplies exact algebraic fixed-pole bodies at t=1/2 and t=99/100 with five rational reciprocal proper-subsystem metrics each. The actual body at each t is the SAME across the five metrics.

In the exact fixed-pole apex chart put

    H=((a,b),(b,100000-a))/100000,
    f=(u,v)/100000,
    delta=1/100000,
    N=((H,-Hf),(-f^T H,delta+f^T Hf)), M=N^-1.

The complete input rows are

| Omitted arrow | a | b | u | v |
|---|---:|---:|---:|---:|
| 0 | 35160 | 36716 | 69799 | -23125 |
| 1 | 38769 | -30216 | 490 | 58684 |
| 2 | 40711 | 48169 | -78055 | 78750 |
| 3 | 19798 | -19530 | -125873 | -136772 |
| 4 | 42456 | 33756 | 55139 | -32565 |

Every retained four-arrow subsystem is strict and apex0 is strict U. The fixed five-arrow union remains weakly impossible: retain weights w1=1295,w3=2413,w4=9599 and solve the exact zero-displacement equations for w0,w2. All weights are positive and -sum w_i sym(p_i e_i^T) is positive definite. This is the previously settled local chamber, not the new global proof.

The complete strict censuses in omission order are

    t=1/2:    222,323,222,323,222;
    t=99/100: 323,323,222,323,323.

Their labelled unstable sets are respectively

    t=1/2:    {0,9},{0,3},{0,4},{0,9},{0,9};
    t=99/100: {0,9} in every case.

All ten are physicalweak000 with all68 primitives nonzero. Full labelled stable facets, saddles, actual-centroid enclosures and every primitive are regenerated in the report.

On the exact t=1/2 body, the additional rational matrix

    M=1/10^9 * (
      (431719526,435572152,-234354122),
      (435572152,440501457,-236815216),
      (-234354122,-236815216,127779017)), N=M^-1,

has n0>n4>every other nonroot radius and D40>0, yet

    S={1,3,4,6}, U={0,9}, H={01,08,17,34},
    strict424, physicalweak000.

Thus the new full-metric exclusion genuinely covers geometry where the highest nonroot escapes to0. It is not an extrapolation of the earlier highest-nonroot theorem.

At t=99/100 all actual projective denominators exceed1/2, while

    1+c·(B3-A)<-3.

The actual10/17/9 body is bounded, but releasing F7 and F8 gives an unbounded virtual pyramid. At t=1/2 that virtual denominator is positive. The continuous trajectory therefore crosses its virtual horizon INSIDE the newly certified domain.

Including the regularized rank-two endpoint, the report contains twelve complete physical censuses and816 nonzero true-edge primitives. All are meaningful C34 nonwinners; none is110.

## 7. Evidence level and remaining problem

The continuum exclusion is an exact validated proof: true geometry, genuine uniform moments, centroid-root inclusion, positive-definite matrix bounds, and complete rooted-tree coverage. Numerical discovery of stress rows and predictors is not an exclusion argument. The final recovery uses only literal rational data, integer arithmetic, outward interval operations and standard-library code.

The geometry-wide collapsed-fibre lemma is analytic. The new fixed-pole controls are exact algebraic constructions specified by a unique actual-centroid root, with rational inputs and validated sign enclosures. They are not misreported as rational-coordinate bodies. There is no claimed proof-assistant formalization or external independent audit.

The remaining full-atlas question is now concentrated in genuinely unequal completion sectors outside the stated band. A rank-two candidate there must satisfy a true rooted reachability system; isolated singular vertex counts are demonstrably unsafe. For S1/U1 or110, the parent’s nonsingular common-metric envelope remains available, with the additional genuine reciprocal polar constraints. Merely perturbing the metric or rerouting a collapsed internal cycle inside this new band cannot produce U1.

## 8. Complete source-only recovery capsule

Save the entire following fence as `recover_hex6_deep_v4.py`, UTF-8/LF. It contains all three autonomous input units, ALL389 literal stress rows, ALL330 cell assignments and error bounds, both exact body/control constructions, and the complete verifier. No old report, parent source, solver, floating checkpoint, external package or network access is needed.

Environment actually used: CPython3.13.5, standard library, assertions enabled.

    python -B -S recover_hex6_deep_v4.py part 0 build > part0.out
    python -B -S recover_hex6_deep_v4.py part 1 build > part1.out
    python -B -S recover_hex6_deep_v4.py part 2 build > part2.out
    python -B -S recover_hex6_deep_v4.py part 3 build > part3.out
    python -B -S recover_hex6_deep_v4.py finish build > finish.out

Replace `build` by `check` to verify the corresponding stored output. `extract` writes the three readable input files without running verification.

Exact pins:

    recover_hex6_deep_v4.py:30266 bytes
    SHA256 ef7344bbc4119f8672335b8ef2d840fce693c8b58223940c2aac43355ab9d9bc

    decoded source map:196955 bytes
    SHA256 18d553869283194862884142139c3cf0ec38f4bcf2215bd6c93caa447affe85b

    hex6_deep_core.py:7722 bytes
    SHA256 7f22548ba7aeaf3af170afaa339f8f3c1c26610719690301dc5dd2b3118bdd5b

    hex6_deep_verify.py:14118 bytes
    SHA256 b9cfa61b273e886fca8eb98a1bdf6695306015ec10f97dceb2cbbbcc20690893

    hex6_deep_data.json:169963 bytes
    SHA256 521d4e769392e75fa2483c6976b03a565977a1edd94e63eeec08b967b04df05f

    hex6_deep_report.json:535691 bytes
    SHA256 df9d7e4bffd025f004ec114c683002ef38d5c418ca85036c6ba66a6d553d9b13

    finish.out:809 bytes
    SHA256 946ffda1680cb6cea423d1f6161dc38adcadaa8459d0314eb0fd7850cc72a2f1

All four part-output byte counts and hashes are embedded and enforced by the wrapper. Expected final markers include

    ALL_4335_ROOT0_TREES_EVERY_NONZERO_PSD_METRIC_EXCLUDED_PASS
    ROWS_TERMS_APPLICATIONS 389 1415 35416
    SYLVESTER_INTERVAL_GUARDS 212496
    DEEP_HIGHEST_NONROOT_ESCAPE_AND_VIRTUAL_HORIZON_CONTROLS_PASS
    HEX6_DEEP_FULL_PSD_SOURCE_ONLY_RECOVERY_PASS

The complete build was actually executed. A fresh directory initially containing ONLY this final independent-band wrapper then ran all four part builds, the final build and the final check. Every part, the535691-byte report, and the809-byte final stdout matched byte-for-byte. These final pins belong to the independent-band certificate, not to an earlier tied-curve draft.

```python
#!/usr/bin/env python3
"""Autonomous exact recovery. CPython 3.13.5 standard library; assertions enabled."""
import base64,hashlib,json,runpy,sys,zlib
from pathlib import Path
DATA=r"""
c-rl~30E7()-L>4IJxV7NVqXwa}`8qEuX|gavj^pLxxMZS^~*NHXtksY$tF2`}gb`TCG+K@B}vQ#DKcHx`w@<{p`J~s#|}5w?BBR
yZyo7xVtwR4{jd6`)>2QKmGr=-}d&VEB)bkus0p_*L&k#6qxJ{j`jvCy`%ohY42dz@6jckn~q1r{)(?+<;fJ6d*lAf!Ekrn8^605
>ihHP`FM1=@_dYHhohs(%JA@bG@h>9i6>Tila)KM&~Q2!Pe-GJqR`&xaCdmr^EbvahrQ{3x_mqy_5VD2)R~?f9}HUI_nlTRV>$iT
UU@zmuk==iM=QtS^D%vHwRA3XmaPk}v}$K9ONFy_?(fN3d8Xs1^>D?eLurN8;YQTp&q!mL#2KaX+_l^7KaXy8&;?wKzgWAy_21aR
;~OnHk(E002zTt#9b7Y|naEV=I_|VgGww33(us9J_20SmL#KsK%1md<cUNU5WBwD%xc|#D>;Kx!Wx{_FnZ#d-zo-%AOr~+HP=~=^
hmxEsza4uzfpiD`*57kSt>@dXcCzQ&tyec#`+pw{j#|&#I~cPc&2t(J`sNQ_(ZRTP^kUEo#oGUP(L9dTw}#ovsGV$=%HH+|I2#m%
v*^`s)<fk()cmhbj@zH!e)<GM_k-|*aelax2IT)TKNz`eaQ(samHuezYu_9XrYGa0mC4Cr>+RY*-~8L`9X0>g@YokgcMNbxQNFjG
@8I8BtGCT|@NccR&3Eu`-5>LK%y!!Az9dT}^Cczoo%Ri1l2=QzSdz_3h7JvnPN_qG9<3a8NV>iD)|<}u_MO(-Akw#9_&YanX4vUO
Ilr7~<fy$9r9GyTgQJtf!59XOigr+GMSn-WrInYRqruy0YZ&gFU4E4vc@@3c9_|1g=n7%v&GyTk4*kmLknTV2&?o%!1v=YrH%@1r
rBl9CrSjNzguttC;Hw(Os)kh6`stzq>5^~Uk0~mzOcUenqs^Tl8!v`8knVrxh=iaqE|nm;xBg4@{&%}IBooj(1e12P+nS&gbTu6h
29uT_Mt|7(ySEtynDypGf9rAkpRLi!w6mR5Fqlw@GXJ$g?F^W9K`_1kODKM)+CIzMg*3e;2a_nr>}BUR2@W@695;K%$AhDO>t)-Y
cv+knwyF4Wud}@l^s#*Fm>}B8w<gox-m4Bi&ne5F4J{N<3oS&AL4T;><<9r{rvKX+hMHy_pmHchaQ0W)oes-4A&^uA)c@DuXaZa8
54VRIsu}Jq4jjbqIT$`=0#D-WLnWw93ZcCF@=c%`Ivvkf0YaBZf&Xje*1-X4hf{*ngSPs|BOFaudgFmV{bDelK(D96{-D3I`)-A=
t-1UraP$+1%H>;6I_&%J>EO?!y#sV<<tGwIw>vo)O()%Mr?q-8TFqAXhpW_Q!b`V1JQ_~BU3Br_dDiRX*>2~-=xC6Qdv7{-dIyt1
&^%;?Gn-WE=D{fQfA@zS&=y@Cpj;4ruXBg^VYkzxTR^pw6{^mcSh>^M^@3lC)pU9{BOpiPwI>@Jy_@~P(ddxyHyY0hqMh|tYkjv|
xV^ElTQ2SEjY^2Mf8U9B7enp!`xvQb<2a_H(G*=A9svUgH{bw%YH#j#ev18!O8TkQLv=THY2ZE7hfn*%?CJPq(Du?D`+7UE{-U*`
!3%1wVDg_@>vVUvPPG-chq9BC-PE(h`#08mlh~0^W?WOqmq5v)(Ba8Jd5F-1FS2#o@q<{4gYciw7wXVjF))8_e&i5u>lDI%l937y
dv9?>hwbwCeWRV&c<c(Ix#%>KTBy~3=PTrc(aiUG=6mEDo^P}D#OpT*3$6NNf8t=&t_W_5BN#+gE^A@fH>npT2`(w^%dYk2O80gr
G}@W^{L${D6?zdqq35amWI8St-loGlVSwm+mJTr@9PR|Jrglq?-g})H7JI;AFdHgG^bkz?XOd}%bbm@rfuEDXWaIg8Jeh7x274p$
PJb{So`T3vLF~r|CzF-KVW5*xdSiCIh@0n_;uJ(N!A~DQJ^bu0;fzyo#soio{PY5M1PTet_cnMM2xAid^gSp~Aw>L{gg^auQMeZ_
lQ??w`~hO|B?77^H4IZSmx{5|JwKBrL~;KNZJffAPXWLQ{!Z|>kH3BV?cr|^e|PbB_q}ZVXR`5AGVuxh>eH_t{n|a()_*?N)_*?V
)_<O7E<eb%I7s??BOLp|`eVKpu1w+;Km4^geENGM9PeJt)c*pdp9VYH`YXr5%&2C4`pe5_?XR`Jve0}yTKkJc=Fk6?d!eoUmE+$<
to`Tru=bzltUXxb&u3cV&(RWpj+W>ResnU%#i<{7?_hNFqI1wY-0k-$>e&pA{XZdYyfIyCy~N-3c-*eWygtuL0&3mL{(~SKzc~Gp
^h@nzz6m5&x7x)=I$u6w#gUj56TXgi3@}2ny?3%Z+*>&wy%~%V@eQ6oAMOnY6ljbPLGBM$ULa5$!luF)SEhsMxVJy(kBMqV2k^p^
n?VSNy;p-SPIZq*2k&CsIh}M;Vmw4LSdEz^^3z}E;@;`n+RJLrAY+s}rBl-hZW(qc9{!aCH5a!I`#x}`T+Kr;aACM!t|G)Ie{>4H
Z9SXo#p!y_7e5W5GR5@oAjQxPALjoNf|t-hiW4bY3l%(ra%Y1@x8Sq1zoisbhN6@dj<ZlvDd7KgSjIs)HvIMB{qCcO_y2g(sY;yG
`kz}5e(X^CAM>@t9wa!;_PjdgMm+tHA@7aGG&e&jL1#PM`Ex5yc68@JTs;*NgFgIHC$@Pj*g;NqP-6yJG90yY!Gi2!1!KG7yz1o6
*#+APcG>BCMn!|nRC}`|Ey@;?yb%47nlk#;Zm+$aC8MWQ<vbQokh9#FuLx(VHj)HB%ueRJ@@yKyl4OYN1_AB_fbivg>1U;^g@U}d
;O&FatXF{VzjGA%eXe7-sAJT-js7IT{X#t|1N--^KgpgY9z7f#67>{#4Ocre5Q8lUZd-Rd+Xd|A+T7Xt4O!`uYl|u@5l2Qwl%P)x
k`;y){22_bLuG(2B60tb%|3Ga=syY1us)|C4M(z>ew6J^1K)V-`CDyX%zpIdg)PWzUf720=EbbYZC=!l{t06n987zizlWPk%p}a&
cuONO+<XDH9n$n7{-2u&finLoCIk+9lUL;=-NtF1mGS6JvI*ZZK^Piq(GCCp_sjPG$AX`KHZ8!N4d;>Ud3_7GxX~f%ry4=?2`l*7
pgH2!%sdKj;LDsQ9z5(Fw|*vtXYCu|%<r{#Oj3twcIY(8(o5v@v@Vd?`t=5NBYD3$YY1YvOGZp()+Q4&WmyPruBOf3aFL=HU$o`R
(j7Px`hvrS4z)LUJ|mW2J*jvexf_S^V&hkT!wb6MZX2dswu(3L>KosY(VOTTNB;OX63D%|@@lOWd$~@dTDwcp)r}T?UMH?<ueIpZ
`mH5VR}F!cdFpO<FZ(qS)yn}`3i%vzxILshd)Z(-_7X*6)xm`u$Obp~)|*aif4Ghuaf4GZ)FDj!yV@B8Y*9F4?X79=q%&Q|0r}UG
lQ>;Rt=Z`fs=IxozlL&=Ci;mceB*P0LbjK^Nxh^slEJvU2k{RP))8dOeSTc@+TYb#7!-vO?X7P1BI{<|PMMrzU_FKEi%|I#2?9*^
P4))1ihSuOnC6?cHyfM|`@V~lVgICekhFH_ar`(qw6z!YUTq;}3~HescRRIeK!>}et7?bG;|{t<BK4()hlmTeULTdB#|85M*k+ym
Im~FU7oC2!vv!Z>m0#Az2K8`4K$gP4Bo0&+jA(5<p4krp-rw;0DBa)--HekF?Zu+WgVV%JO|ju&`+JOh?Mc>JeKqdA+579=tJUm`
(i=~*=Le(Sv_<mr1z#WGWC?BYT;^wnW<f)&08YExKRG;n=QYsIzyJxE)r$#3GfxjclnVF87-4s*$t?k|SF#Tvx}^YOA!7)uKDQow
eGfW`eglvE9@Jc)qAiB<;rF^{@9pu<+F*OKb7MfC{F%uPc)-^+StOqELSz|5f>vf0ecbP+DdE;He)K6({3Wang?TlaYffj@ehCXX
>%YV`p<lv6PkUCBoYybmxJYUJN^2K_M+*8T!{2POKYTt#YC#j-YiqXcoByrjQ5htZ6>!9r|1PX&oURe|LL87p^@fe#E+&|$w#m@@
jO}%FCQS7IGS}Q&a1qL^y;*xZ&qQx;_Sai}BtEf+K?g6N;>GOkyo)F5O$%0)6|4UiQ69}4S2PpV;%CigTB7;NKaal4N-N;~-n4h~
<z#g9-R5_H|M?xo5PyERxxKxe$A#p4C);M3aF#QC;+f2qkrE#TPI6&(@Nup%&jfc`D13Ao6G~|9%OLi#S{fdTh+I1=!c@jA<BraX
qL!LEHFKJW8<eqJ#5(872&R>#k1SKDpM^@Du$HTZIx#54a~lUGOzy&+R_06<J?2L0P<igOp&}~d#u+x>VI0Ve;ew5KIwK4>sar<T
oebSFlCj0HqP&K5lK8Aqrlx+W6}JoH78#e?`GGKec9L09Q%G3DoS;II1gKS#NLXW!3YE<3$6zc%7DAJPb1uC?RUtlf4&te4iyE-d
Rv}N^Yho!tgG&*hQNDpg=yp*@F0)DtXF{K(0Z@3V$*NrF*b#|-=l~93^f_RnjRuN2uUDo?-=wKnt7BZUSgRJ=H_a?0V6?1NoIvAo
5a^NzGRl|qCP<cCi=y9-GZFgAl~Qs+(I(@$1ZWmJt}@9r7qQ>M3M0Y|3f(hl3{r}m>mYn-gv;w%P};gA??R`zfk{m|4TS_(G8wPT
tqi76L8WjiH|Yju;tlAx2UajIl!%mJwedE@l&&>%RK`^(YK*sFU@;d~y1LR9@-v~d(n0nnBVZ)pD#w_YFtllS!2g_f7>zQQwTuJ#
7P8|e)FU&?bGE1(^nf|;I|C#brCc55$PA~A7NKQBTxydUGBn~UHU>^{j?ENha-(uD6Id8aK;=@hoYjF|!$gw|%av*)jS4qtpkF27
8YXff>!=OJ5VUWgBgi62n1KRJ<Q@Ye*ERU(8f=_I#%*qGv=_;}fT1(atgN{cRvmAgXL>HJaN3KV<t{M?n{gS>v>+1-KFB&D>->cT
2u*ZCFh!dzNK-ulHE=pA;sj<as_lSEK#ox`R!En6qKtqISBVbYHHP>i6f!msm~`{j3H!B0XW$F8r!+<=M}K&*|BC+r`ts->nUqS3
`BH&EwS*NcN`iPIH(JHkg-liq0Z7Zeq`^IgCy8=pLjwhQgwj?s>3lDEdDzslCHst}00&(`rOhBP-vbO2gN*)9T5Y9`_dx@B9>{^i
mwEWxIXQ6he@=;r40x5i+8GQGEy)NOaFbBR2PLS~a^C|GGnhF*Ij__&gpx88mx>4E=ksG_G!m1_Lw9k2^F*FI6^#geuvP}2z~@V`
oFE#Nr(7;mH&_mKl)hRu$7SID)U@OP0$UhAN@18HViu7A7fBXMGh-L;fO`giYa8KVfnk=~0OzR%RSJlg2Vo$@QqdnPviH!r`QkDU
krkEEd4MjNli@N!29PvLEC?GCVuH`4A_GEE2!TfO-6e#QQwO;7g^Cbdarjo3O67U*o2(Kz0D@AbQicW3$I31=a9N~vLFB`^jUt74
Xcpx%>(sn3f`cTI2Epq{(h|zfiz-3IYEkHjj$Ei6UIwIIjMxgsVh@~#zl`E7<J!!R5>b$h3K5C{z{Oy|6JoJtIE`ewu%;M2qc|da
$0{H-h{u%;HM$JJnn`w+;sx)~Y>ZFKvZXi?2v31JYFAptig-~7H7R&*8E(*E0T#=^om(yz6$XJOl3^5nbL%n9%)Hqk!azLai<Nm5
w}1z1B43J<lEuQ8#xTyz8UztIn@g8s=;*pB^l~nRTOdgXphee%TBLQ0YSVL}GS|quVvi)m>P6tgW+ND@fto@r!ctr!xQM9}*ef>y
;}y~}puE%%Eo~mDrV>yo#A|s18RCzWvs6rpuoNNzSTQ1}5Oq=%VQ^RdEyyKw%o?RMF@T3f+nl8v41!kgvMCKA|6Ui)2y$S>Ens4o
S^(kNnm_~z19OXjM1+C>C5Ce@Cy}Q*HJn)DC^$T4YNBvBki-;KUUS?Ar>`+0hQv1Nk|BBE#T`gcV!|<te8^0Bf}l;o<6QluWRcqx
wj&_1CIS!q&Qy>_MFcLV{LvSxTmd!lhzjRyiVQ79W+WO(xw9~Q5x*#eNIAsq$lQ=7+c;zvQ>ld;cuDpeZX?Q`XkDkw!{jipnCfcj
tV;$q7ctFc(8zOS41W-Bk+H=I006=xj<Rp0AvN5|W_W-NBAevA5bJCv!6A+kDLx|{t1wc^2kICZq>^i!hY1IXDA9V_6$r3=_+cqD
GF4Q?JCO~BGET)wh&0^fwzcNI2<4!;@{=_S2o%x#f=&#|@H$Lr^5~)S<f2mjh^19@IrQ9spF1GXG0vT;9V`-TKdS^{aSFU12nw+r
OEV|ZRWp<5^g&!K`jEm3fMbVvK7~S{cb}RO8FJ&h0Fz;WeaiKXO0t{_XhF|{vnYCGN70)pEp%)~i<n`~_e)V|WEZ1cc)4Qo2nng3
IZLBLaG($<<#O>(xC0jn7q%jhb;Z~N(Y{bMU7$K`Naqwy?I^|;Bic&u7&3>Logs|&a3?pYwMf|_D@7I%rdsT%pNmL=2+g3yh6E(f
Ld+_19Y9xQM5#rtSgc<-6+~z&@jFcenM7-#4I^Syg@l?(Q!k1*oluSYK;SZ@?HC2Z6)ltgELWmta4IMVaMoZi9mv>E&M{SqEhv)7
5n=08C8ARAKdWpE=LhD9H6gcgHijt{F?^VKH5GUvM$3838IbAbVdAbbJH@FlapsmdA7jeTj{XP(=t`VeL$;GbP?aO)tBc;@ouJNC
-sCZgkj@9=HRYuZGfV^zq)KVR);SSFTnm^1T5g`T13sj1rWhQe!RYHLzH)I2w<3d_oRUj3GxM36l(~s97NTSu6EZTd7)n<I5CZ~^
{0QyKz~S)Xxh?SMka?&S*W}UKQHtUvT|<5}ZwzizHO)yR_4P8$xz$PLNb=HbA6Q+g+RzDd3x1G#1;ne=bucws5}(PO#XA5nk;gj#
^ISza!SD=Q<TwO|X_gz=rDMD<&w(`3tcJ8H|07SwY?2Gylx0<$g3q*p%6u{^oz52nGmvP`WelKb(m9XO1nk$@G^dGRR>e?Jq(r1T
cguh(Sr_>+%28q|B;6{6A|MoIcnTkoQL>nb2%7q@Z2%FSt_$apErw+SSTRkti$sxtR51~SAdaWmw3xduG@xizBz1@t9TH*nW1&21
jD|4ZA%SQ{M#e!f6ar<RUr-E_8sL^i?kCKc+6HKaBb7HQz_+>}0GydPB?xz-^FpLNPBNklC}T+jDkeOY5x{zxNpXo1nxzrsRxe38
v?(lJg%pYA-gCu^&`v93!)h0dm3t)9e1Z)VYRp!mMNV_caR7*oYC~<uiwG2vi_hL2rL~dq2~FCFy4nF(8OtET<F+=Crx3M9Ixs6g
)klEiOxu(mAjoscWSBK9%vd7o(6J?2;NZ2rQIR)jg~tg|H^mDIPALN{le4HPjM^j*O%zpAy9uGT?*Ply+-y%wOhhr)ikQJg)xc}i
0@D~CEpZNv2r)F+GwKYe<gA#R4a-iBrgrk!7a14(<|dw)mys$aF<f0VjSR-790t*ZADpAmSm|i9O55rRQ=A`zE!(g{XRQ^=EJk{j
F@ap-Bpp$iq}9?SRUO8}5$Gf^7YkczX@yD{o6=N96V+*HSccw{c0&&ltt4q`rEA8cOGN8eZmhR+O59DJRs$I#0jFnap@@qo$llU2
hvB*gIEbp84kpE2oG_GdWyUTHk+N8(k_<#mSIOa1zL@BOD=Uh$Uu#x3SFhuW2`$7#$6uXppvW>IA=reUqBJ$bA!1<G#hGX%28kn(
k>z=9j{)ZdMa^8DgftV;`e;OTB|t{Wb>^nF1UIP;WEHH&BzQ<$2nJl3Me{{A$C4CiZY*}$a8YLh3;<-dI=cthA$N{3ESKD>G^LEN
HBJ#%RzPXtD9y~n=fzklr^Tp{f>PwDxK?%RWX8LTwED<xB0o{jU}>_~3R&j}XlYW$42EV|a#fST!0{thOS(nA9j)5b;uR`SYH@iz
pp`L+sPx?IQVfoz4kSIxwt+k32Z>FXiHmlsLOJkF!DaY83&NP1O&MI9umC`_o?&hjyeB0u)+iM%UWWxdq$)KL04--BIjUKsg`04B
O!=imI?YllQC=5B9>BuPBu&xTBBZ9}KwhN6bD0EK#|c}z7lwz`JLdyKmi(xpb-=I}1`!QoE=>(NKMlgFvsD&DQn5U69$aa)kfPZq
7B`C+<rV;nEF{la9><0t!{{U?h0I^qEm&G@SV85q0<9MpEa6<4UKF?@hy~~6=fk8*bC+N>D^q+<NsCMCuuN5k78-C$=0(^p<znQ@
NbAv07+Oavwim$N@ailD2WvAO?^90YVsW+J5Q9k-JLWh2s31gx#H84ez`4xB%$1U1qKjg`MgI=jyV;%x3a>;>8J)8{E}hY`b?qJk
q{`Cjxak04Qn8Z<nV_jI3^9^5GP#&N7-vnfb;Tf1a6uY~h54Lb<FqAGoCs66ap!X!Rq@qGe_051=O++3`FS0Oj+^6#h`F^BvTTv|
Y{7|zeNU(p9>XrK*;B0!7G-0tln6$1hRNo2E89Y+sbuZb`egnVG@sWt0PT4yqXv-d@<{mvh9U`p&l7slShTYyl@WO!){$Iw_Dbqh
M$_bsoRewDQo(R_2?_TL-=0tW(vgcvh@CG3!;WR38ynVj6zCW6eL?a7qY77GAx6f~Y~H0xTF8!506-k~5hkD4|9sPovbnU5L<<Qj
+yR4S$$se_GhA7d_|d9FegLzTwNp5T=5XTHK`=yEgp#zjnQK#f#~kg07-ZTYmm{z)W{_xsPK50O&=*(v{JP(Qb0C}{+KY^a2wFu(
H<eJHUSN|LG&d%ub7rn82+Jjr3ZViLe9kH30+_c~CF<6W7*|rJ^*7|xIn!|ygAOa@yn-o46UfCH7PmG`=~vMy)08wx2W)K9+`U6&
D;LF6Sqk-={dCHgRhqk`DY7_?Qdw2y<Wus{Ujzj+dlvbuBlFH(SS`{jBxp49AFWTqr-X@~sy)F6+hi)r>gbbb>4xjv)=3NMb9^Q(
kd%s;Lw=-0okr-@N;=J8Y7kY#HO;Blst^e*OID<m4U_3;!o;0qH8-TtG^b_HJcN2^K)Jx<#wn5ZYyews!Iu&qT`8ENt&=PSUMe_b
lC}y74JBN;h*Q>VKH}j3VA|8=;2C_tMB;&L^#bjI(VfXtz6p%z#aM~DtOSqcMNX^Ju`OwNU38&TnuPTmUoB^KAxOa&h5}kGd6DR<
=z}W)lJI(IatHRubmAu+x7<~N69gN@ZcRyy5SE(2{#r$<P77bvrl2onifx!CWaP9f$1=GnL&R9QEwT$ZW?`z{p0;UO?{(1>?1ZO{
28ghXEB5oc&<;E)uL-1Vp0*Y$m7K6bBrKwTA+MD$L;|$(&uxqrAlw8YCb-LW4TKo2E2Wu6TEq`|M@HK>VkCuNh)bD}r7Tm6aqoOU
0h}4XLP{|(+&7D&Lp+=&x@lBlhk~l??xC5Xyx8#SjN^;GnNfz4CTziQGQ{q*MIcOYP**ihs~V`#(v?Z9=8!~&wZMv7Fy+k##_6!e
N*1cTnW?ISat!`WRBG~j7M<Y*i*nF}7HPku4s!-_UiA({EoWH~l1UwXEfU_an7qgYDs9KF?p9W`Zz~42f<l0rkcQUiCHEmT(FDAp
nr(uiz4$V&LBJ`hSZZ$gG}o`gbm%;bgG7*V2~p>#5c4yhXon`uQv6LOR=cf*YriQow$DVAE8UNbRp^>zOOUo_VCS;rSWTKHqSdzW
WCN?JmG<ey{mtAtX56{a2_lNH0h4?q<y*QY?w|!m$<x}4)~bXxo9jBez?E6#sKIc$&M=&Ca@Kd?%cR)B@VeN6QV<g|)=G;E_L^WA
))Y)J{VIf6umM^r<$;uFol_`Q(?7s;mVd*RSd3E;P)Jil&NMxrax0pfRgqSd)=bNq8<e2Er_m?Elj(Q^EoX{4I=}@jYZ6aEJ6KpU
dJ}i08rs%Uw-25pjb}V<PY<(d%BP9i)zr@DVTPiN5GqZ{aGs~}inz0$`SobIFv&vepLyX>9CJGQBG9JD>xAzL;pen9Cajq(sNJLm
PrtIy!WxjOlBms#maTJ%AsnyeYea66&ElOfp-aBch514XDQTZiT_`~NnTuJfxEQ|h0D)66UG$++1UBuVj5!fExwbWlGd*<_GLDQM
U@>uyoAPO{YvCnQtV_E~!UkZ9(MU|Jj+rguj^e?SoQM5F75TuH)yxU=xL!@W9a-8O$UtNX%aU2{Ts>VOmzVM34b6<nYfF`xh?X-<
<aB3w+FC-ocPe*Deuy;lI=9D>DRGh3zCo~hu|<C=@&~7!M8+_*DqO2weZE0E19+UrK%6V<a&8uaq9T((RuS)jW74y+8+uNqihDy#
BRWkSP#BD;JkUOaQL_474PaE8)+QKyvv!LjA~5AHB|9_?U%O3&7{S`KX;L_DYJxlD=C;_;7#>ioST7`7qGLS^+~xudViu7CZLRIh
GQ%DgnwUne>1yt^r107P2HLh6XAv;`NCJo#6|eCRf&9ZXoeVi&wfkT{J=<D|qqOQKg;I+WK_TQ8Dm|2_b-q|9WzEIT5Ju5^+Jhm(
Hlm6#LS_Y5fq;Vu{p<^`vt8Po;EDxC9-c&_hYl1=dkvBE^BV49Aa4;T?I4c$aHpVsNKx?4h*}uHGpB7KfDNm0w9rx!bQvYWTrI89
hL4osDk<v*Z)c$=5+<o)5<sz!ShO0{$DEznRvw=Itnxqe4}Qh&7-iFbbBwQe>Wn8YMKo^~4T;8N!y=Zax%B8NXwEJo!_ND1B&Nme
Ha)h*i`nX8*DVjvxS7Q<N_yHNO`J*+c-rHxIp=9Nv&(B7A6Qcs!9@)GY4*aV6o7}Iq-rV5<$fZ9c?=}EIA>}i!(wYm?w32$>Xc58
>M|Zya~9jMaf>6cy6^}TZ7ib4o?;ua*!;oZU{dcz@DEjBo2Wp)wS?Ej7&gXGv~xVbo%y}<HN4De&t+l0EVSr{6_z8bjcbZ}(^k~5
Jz}9o8B=Q7#l<wUF(iwtGRiZLt`phZ6MP7JOr%KUILhd{<qO8c9&bPGX{9oClP<{6c-l_IcoD(QXVuVGd@d&=3o6!J;S_WXTNEv#
)OeRlMar=>Wur@*XqYud6p!M#Vm)<vMU=p?^gvg!M+>279<~p&ir!IvwnTt*Mle;~VCaKjrDpSvK(~ueWs|waCsUVpDzBFlRb(iN
2@fX9_$Vb?h-d1W<Ls>IRxOx|iNAk|dXau1u(Tq2bXs`S=G?B=YbJkh)#S@`v!qviAw(>s#j3GtkX_9*GJ>J7GlY6?<SYQ9{W^wK
g9+LO1u~vJXL1qP%o)qVbbMhs{-Hm!5MYpp3OkL7vgxVAnniMY?nk6eO)PG{^&hRBJwPGqZe&_Zk!IX-mLBe~IWNp!Tf0C>6iCKM
$3IaK`JQr3z0eFjEgv*X_qnhj6jDc7QyBCk(-TrE?$bq3!|ZHAFF7bdt5Y!vmw=2i>3Om!?-Jm4vOmAu8yp<?H&y)o=XVDqeE9P_
wjuxg4wv?a;ZU#*z|fx>jK}_*HI{aGyN&Q{X!_5WNw2=}-y}fa8Ibvx==<*x@a&(FkZH42=I4Slia_XLE^sTNm5eesgrBq?ih)Bq
;CHxYs2YR7_%cCDx(EjlC&QCtl$oT!4z4v*$hXMRfka`_05IeaUe62^K|xDqEGP@{FXW$DXu%<l&KxBU2$o4QG$loO2L%%J*eFfn
lOv`;4?h%=IPze$$VSuA^x!1Las(}!o1!p@=$!VzQ=m%W8ikYuY|27ty@{qi$)n?k9%P^=tNrpixh&c?L(d0NmQ2qjQEa&LPgc@S
NgYu`+H7#8ud{;G$Li=q^;4&tdcBmCP#BK6T*DEcM>XO~wNuv2`)j4FgQymvHeh#Ov{v}%Qp_@?e27BMqp*5~l%$``M2auoObUgV
tJBFv^znYWC`&#n!-&guC6}xVHm?r$UK;rjZPaRl(o{<`S997ZiN3H5_hncH`#6QD57)_6DWfd<qz$*BWuuEL&_yBmqzR?IPP@oI
kvep(Mv^wz5-pT8@IKNn2|GCn_hmSVPa=N(nKbZeq+b$s0>5V02>f4~^w~W2^+K*K*_V+$T&DEZXH>v);g=*`K;L{l(3h7d|M!)B
MegYNBJdZ|W~;s)(*Jnb=L_ODpGpHI=}UUmnwXP(Nz4iLMqDG*%g-<TB=qxzT^4PUHro)_LDq^k#eGhRe}J?L(H6*d*96&LqO{FI
2J6^0q428|cMvr_>QDQ?=0skSZ$h|L*9+nN6G>gx3;sO?UKVeP&&}5ppMR+WuNQVnvc-%TyXNTD?i0)V0&*@(H4*oc1>U&2^$lZs
5zx94cBlD9K3i2^M&FAoxNb?pd0hnmQTSde`}dT4S;|rHT-DCCH)8*UVxP%42|X7L+CRV8^TnJq7uTELKSc2PN6Ws#GWo*#D$m_D
0ldDj=+*m6zb=juyjI9%iAEtSQ6G?hEi&d`pqNWCO;Bd)>xS}siJ5&SNmszk)FM;6FN>+=7a(cz-ojp>=7m*G&e@lR=Py~%e7UUW
0nHaOOXT$51e)z-%DE6~0p?3gBiS_+bv>BP;@XY6Ja+z8<XjeN!m|+963@zdQL|4iZTo(}77GcYa+eoFU#`5B`w~Q6l5YWVcU>X=
Wr(~i;6&e?eU<dBzf7^uvp8Q^o8(e`l@R|L#9fwcdhCc@+LZP;ChVDHi`4_xAp3J6Td_snHVtooHr`%Xl;p}Z=>BZzUPvmn`YL1Z
uR+>+;aO0w7c)yqU%4mQC*4x=A;SJrC0!M>4$ENDzpHf~-Fk89Q7kS!HUht>z|WL+S+oVbT?6kkq<t|_(|%WaT*Otty_is%>R#?f
*dHQn`evlcLxHBUm75#&Eg<_dNt#A`hP2DVEqL2~3%q?b@-7QE;oGtX-=9R@ir$dM=kaY9*CiJpvuwouLE>f$;x-EpR&r|^bbl^!
mxWur*h4k!{b}Uwzpt?J>W;+)OD7t9e=d2Kg`4KOO?9rjk#>!=&k?o%auNC#llj?hQ=RR0t^xOF6L(p<#p`ES!``1j;9l7Dy4=e9
W)@Z|McyQrpHJXr>89x0G|~5GlebxTj#98Dx%`Ck)~vETytrbiOvB)xK;T~3^d)T-247gS6zmI1Fu!JL)9cCo*VI%XzK~+74ckcj
Q%IY}JHKq1M4Pb9KUZ@3`9%F`<@|9%&P#%(V>=IRzK~s}w+k#v+|UyaGI#om#P?MRT@`X)0QS7B=LB24b8X22@kh)0+6!8qDeSUf
i>)T=a{>Ds7xtWF(+lk+J*`S#7-Z(jTWe{R5>jYq-G(+Sw^m<c691%P$58#(^Uc51t}5#EvL4P!!VtD@H1Jt9P?dCH1CCzn)7Zde
*g!?p#gp5DyA8pOwv7fpJfuNm=V_oS>Egwv+N#C|E<*zgqE3E*zEijH1DBwIs-%+*(D(l~HsCeziN#Of@jGt>RaqDBmavq6X<=of
g3qghs;H9{7<%D*V+EID1yxxWuE1#3xPr@2K~>a+6<F8g#h*e2BzjgBKYmQb3M#TL-WZZ=(<B9-Mg?=?$B(VNM`T{q$qK9%O=f&K
Dp-(p@&!`mqVWZnp@OQYlNC5&mgmOI(RXVrSdUOjO2IE(1z(!{m#uG+0`l|ipepUOmaB8OVVP@G@Yz)`FY5IA?VK^uSiy&?;B4_@
xbypU7NniLf#Q-a^9GF)E~<n&1>~dz{LJs;sS3QX28g?{hD%h$g2am~!RBgNme45TJVl82Rzy|c#rNtc>l%x=L`5t}yzmjuxW-3Z
o+7FOPZq&pB#lLUj3Ulf0)FP-r?(*S**j6KS+=UsDB{yAqAKuY5hB-3CVi<EQI&Y|5!x`*_=wM`h{`%cMc{=+*u2TAFH;c<5-(nM
tE6c1h|5z%Rp7}Y=$V1WA}-S+suC~0MN%r&_=rpN5fy<ai%{G&nf0YwL{;L&TLzGD(-R1d8a{~{3KihkR^DVcC+cJgI%iEreOW44
kaqG5mO0V*h09SwRoI0k7}aFbmuCqTX&2ufKyPhpa)!(C2o+%$Ukfc=lR>|i5-zTQjNwLxJ3&H~uZgZmz3>fAH0#rstc<GAlVw;g
noRoAEu$*+;tL`KSIrv4<tn2p^x0S1EA2M8=1eYXL-SloW$F86h2&_C+eRJln@=xS$%5<)x^jByG)JS8kJHI{oK+EhVJBAPrm>T&
(8;3gQ;6lXUbelXQOW02NmcTNmAIT<x7%3BRai+?_Q{(#lbgnyT!}ZSihgD%#)`&HuE<U*vM;_!EoaN#ywRxSbE>2&`J|9MSM)ul
jg@>VmAH$mWI^`DYYB2GRpU;sLMe-~FD!*|)nxHkWGPkIr^obinVTj%xdN3`B|ozg`2J;9@&!CWd_89#7sXz<62|P8{F<R_IupDg
_F`V%S)9csZNNyZ`j%IamUBWIZG_5c;?hWKjKfFS=%%b2_Yt%7bt)*{2b(LMvkfa?4Y_T!bJ^OdQ$X<rjJagFV~y=xo$b`Bpm-}g
P9k=e%t@4Mv~$_osZ&5<J4kFSExR<fb7i(ur-H)oXeEqm{LV*dr_hY7*Un5c_)!(Vv#5ZX?dV+7n}ok1+qqiR;73=Dr$z_G7bZw+
8PcEJ8K!unp37HHjRp$q;XIdqUrb{?S7tqRI!LZZb4A}D^$oe6FHAjk8kkv+&3P^w>-kvqTv#>uF;(lS(LqXj1UHI{Zz<{d!qiiz
fx>!(aL%&EdalxX>U2=}9xI(tjqf>AJ?H3#^rA1S8~jwhr>RB-GxKrIDA$<J73!y63F&3A0;+>!%B5ANQO~DR&vMn^XZ|^{8VwZI
Bb8I4nKrme_0%gNc^@OCVWROqSErvk6%_WPPy=fw4zAXI>XcCAKGukwHM!5{)X#F=)QNv)JCL+%rVXx2H}wige#hogI@b7|tI<uJ
_zSzyIBA**gR8TfIt3){nA{?oYu0(LNH;a&pV^JG{=3W@yZJEP(3gjm_4EFAQ=@>w-)PCTYy8dC=%!Bmh20osC2!^kKAmo8c1^s8
-P9={<u}MpbK{!)=4y0PC;s%9fzi39ho{mTOcr#5#;jnuRLUVmVo;T0=n#~w8|7S>)Xtt9sMkV4ZO{PE&zQbxRP^~(RIi1Z6=}_#
Ypm#st*Ax|DRgsO=5qPwoJK*PUqN*`C@jcuog33w(A8Q{ofc+(2vM08jUT#VKUAZInH5=Om1?Z$imj+d3&nTDOK4$3(Q8o~FZ4lA
j(og^7L`yKkd;ac(HPLjXh`Wr4J}VqF=&iBXB8W&Q$*p3oPfMp<B6_VOZAE<Y{}(HvSw=G>TRh`5k+2vXq?w?93=(i$~ciTBb;Uk
3^~2Ijo!|R|9BHI)M`k)w}$GJFtZ}9m|Zfp&}itAG*qvKnLlzyi6x76jgBr!NA+q*c4Tudoi>dfU9BC}sv#{Csa#uSYL|%`4ZW|1
K0rHl3P^dYbP5b8#fB2vn%uE@3t~(m6ck#beXE3JXwz&c&7DM8NAC?2tWnaUlJt8kX_+Px(Q(B%#7=M5wNfagQH`QLfuhX&bKMe6
6yNurJDKMs{KlfLR8h+`QG5+Kci=_ZOPAh%*eL4b6m>BrVU(4}@0VzzuqZB=q%YNJEb9FfHLoS<-d9T)W7VYURZ%!8t?12uu5nVI
MpO2KHML9?g-t<!jwUA>oBCKyT~tfBr{1RORgqrds|{@@p1p#!(bLuFsa_F<Jt=zq5_63`z5nd^XE3RHZ4_?GSfg|Q4GfK&TCOa9
A$__0qja@Q8HHhKNfSfO1jQGit7Xb4GAjB~Sff>wQC+>RmMNpKD`Ocl<Yt=Ui?FMDWfcC(ag{ro8*lv8$Lp%BCmD5hQD0TBh{C2E
5-yoH6BSpir)7#L77dN$B44r{tkKeCSyQbVk}c^R!3NE;H@0-OwzNbM$(BT}xuUt-#y4H9H7!v@5t}Qmw5Io@EsxE$lV~!hHw^gK
LTxaa8)2liuu$=_-w*Yb&LX+WI>+Mdd7+vdV`4N$42ij*Dhwm43qKgPqCumKrjg?uT8D9A@EAA5B_J2UD-Q=O(OqGJWIz<@pJ9TH
YR^`!pK`x^)h^Rrn*2ou$8%_F`Q-1nu2_D)Zm&SE^@=MDRtTfCa*e@$ZF*g%y28tvTrgGsPQ^yEUx#LwsjjeDX;e;^&$3xd3q(vy
T(#V~4OEG962Y(0AN%EjU%!w2Tw3)SEwqZkn~KfWt1j8BG)!8v<V6f$nO?s<rRM6hDYjm7g~4jZm6Yas80<Ht*k!tlsx=C(l1uuI
N~^4M^bX_7#(yQPHj=}=T4xy)Xqi=-ZBS5Vl#{tI4!sc{@I=}t)Nfg{!t2y4bf(QSRXNk+mq59w1J@xMPLd!|kSs_TkOR^j{NS8K
{eUmW;JBe593vp$fFif^AXu*D^jrZHE0|$WtEA~9ZMf5y34;a$p8*57pU*$NuvE>74z$8~DFnMBI%sfk88}$3<`l>|noJhTstt|-
ODnXr4Gyjw4wkDq;XuipL$Mn19C*Vxs~xkl1_|0PKNu|-lR8J#fwbOQT9Y!GDcsA<hrFw>fx=}$;S5bD=YZ3+Ye~AZokIhKuiQH<
)$@!MK>fm++%&9k-C1F&ri;|UNGIsp*{MSVg|9t#Sf=NK6_h~iXAOP%Yr_iHniZC7x`-7l$0?yr6DwTrSYer-XRP3~HXsktu)=j`
g{7K~U~ooTsL>&q@XNH!@&*al4+%@vTyTQcj63V!i`Q_%wdRE7nojux6H2<=D8V*_6v`Q4g|3-wwDjs7&aFeGC}cFf5s@kG(CHlL
&{pDnGu`+Frx0hTI>n7pqRo+Usx#xp1`A((;J8%L1usbE6gNOj!wc7)7nZBK2pN!U!gUyP&O$_khOa+nSgz_BH&}_WDtb*~!wuJ*
8<wg%p}`5Klwrs>&YFR4u<+GmVX2}EUVx&FHngDK@WLfv;nHvbkyUwNxvFO|gUgk$ej=iY8Ll%L&Qf*34Vux{*lT)9y5WZF%?-;{
o#q)Fz0^g@Tr~3x*BT4U6`j7`LkKQRuDB2z^bCWO^fkMS@guHirL2+Q8JDAJpkPC4#<T@0=!<=ce)48E`pd<_S*o6S31jIgVt)2)
bc2TL;3bx-dd3a(;Dkb#8*aGv+^|&DMLuDb!Y|9t-r&@r;Tq%<%T--)gQSNj6xXidhU?A^%T-;(4Mw6$qlIhYhU*?TELU~G4T`qV
D^$^N!*%C|<*F_ornAZkL9-EOJWSVM;p>kYmMVJ23$$HUiCi_jaP4_vsj7>Z!RChJyfRJ9aNT2u<*H6z0(EI7@>~nE!2~^ZMKAR<
i?h;JS(K8B=ATiiL}%Fsa6pf0`PX0N4#|sV&9w9v>?+RGcHu5GZIV-hpFK6*0OC6Mi{-kWF@)gC@f_ZuVTf;lA<octF(v7kGsaqR
_S01jAg;rl<Z@k?7{cXBLdl|Gh;M-*mTS9+Aq*{m<2?JSV~7R~=LQhV6+NQ|NlMH?9A7s*G-x=V8_rPmYy!eCddkwAy<N6J!`DCk
uvF1AZcqp>Yz}2M+;H8w;S5#J;s&F0sf2Q0Tinn<;VdZNzJ<VHsisThVCg}7!@s_{$p#MZ1&6bBo!$tp6vo8ptqfuVp$0vyhfqT<
%se=WGC3}5%WTeaXL5QqxG<LXO>-x$upEHVvH`>w3W&3HUF@eP4uQR&_2S?L3|~DMmg~913|bj_Y?C$2aQ&HKxvpoigO)DmITF${
V}}M1*CBQ|L)SBg5F!_fN#`1dxb_TjhOUcL)5=_H`f}5=Qq2Yq*C5qguIUmxIOz<%-K}AV>(36$bv=t83=`0z(V~eTu6_J)hOTD}
LErW0m=daCh-=RfXXv_E#&WdL+Guy?n;jZBeD!cROVcxUP+X!D{!1zwcDUy3aE7ka_kJ^$+uR6&VjEDqQOYu5ZIvGs(_H0%0)0Qc
V9GG<r!^ds7kar2GfpV<N?Fw`UVN#DI9u7Jh|*ZDb7Rlk2GbzonuL_gl^qcwa|azNdaJk<8&Wu%OARcsyy7<K;TuWcZwJSbTUy4n
nikVVjtmCGBMrtxQ=*Q$oF2?^d?_+61s9(X6z>fP`vE}sWFSC)sBbujx?!Ryi(?Fqqwn0=Igp&E{}fx~3PA(6xMY#AGUsyiOpzD5
)-d^2F@n0-e86!I03uE-`h{XhS^%XDYn;xZdNi2Z8k`73p$cIOeMv9Z3IV5w%7!4~a)Ma|qvU%S?VZrJ0m@eZl=Bdf{0?KrS}oBn
t<Lp34N$HhP|ia@!6*{?7Yd;)t-Lpk@(nV|*$7CvO%C-U*dRT-4VF73D@bFYc-;Wyn*hpr2q+kZlr0^XoL-IDFv>T`C}$&}h*5+=
wKlg%TbdZ<n~YJ;MnJ(R)-T*avGk=r4WoR6jB+*tifI&sv`BK5EBZdabEZ)mpj^j!l(P|#7)9hlIHUbneKd^nEi%eE2q<C{dIO)s
=q<e(tBFy*!5HOi1Qd*dPBE9;T*zi-_S<BXvk{PX4WLdVj8OKhT?32>$4#zGZmm*+=Zb5_CB5klA2x84GFA)!eRfiCAt6<vuN)^0
NEShYI`#Zkf-@0N@ClM<NmOIRS@W_DP_8df&ci?vqtJJi0RoOQc1DcSK;`;E<va`&tfHY(X6cG(Smm3*39j)9t(*;lVlo8~P)ZBs
6gy)wrNPQI#>#mhD0s!@8Ue7-(y4}5zExg18w5qT0w~d&$E9+j30J;Ntegje#4G+038^`KX?w#fUprPVgcF>vq(SF^pxB_I7)~(_
1+z0Ys9X=MECA&jL<x@3hBTF3Drdu>U=|31YkC=#a@UMm8mL?hD(7J!1uUFN>4cEZ8FkG9mIf*pgUWdrC|E^UE$OKXEm^}VUoTWH
1QV3QxVg0zRyi93X?le*S_jBE6GB|G>6Hd57lX=q7${gp0YwOYEiN~#a>Y=&I85FPA^{#aM|~nG;uvERqO!_-4i<`-MF<NS359`N
r<kR|%ei>LIZ+8-&IUt4GsbY2Gc9C(ttN5Lz|2Pg=K6pI<>`m|O>L?Q;hc?%6wYV`X>k8NA<N&6@(n;|Ic~lX%v=;NC9EvL3F@TS
hC~Tj<`#XXerx>TGtcK^oihPaP>|D_G5Ts!Yrbs?YH(DKqw^qA1VBpADmQHich@KYiZJ@hF?6~3!F7};!3(M<uLMVD10^w&V#;Cc
0D!(u^TnSYPu~`nP`{h!r*nW(O#c9Nj$T@8n7T&OKUajOPlTn*#L+y4FlO?rr~~2?7(aB0AKU{O3#lseMrVVk;4GmqT*2s@aT?BQ
F!nweI}bcXoCTQB`>24J3v527H&r<e{L*_#=ph&-!aFxV{ev$b0I&~4R~1<wimGLZ`dBm(dOjtJ2sI`2P!l;$GkQ-S{!08c_;J)F
sun}c4djhm2zVNwAy{G19EJn{;0MRHvPI||WECW*sFcZRdG36YYXJBS0r0)RhjLX0JR4cXz9YC!h*LU~i}Uv#H30lJ0eC+6AOgCE
G8l@0n1z*<txabmtzbkWEQ+`s<7gPM0pw=`<atOdVnl}s+*-#}E}9teiv;8qg7L$Eh&rmPoM)q~U`Ho7v(hN-%(Z97ZySl1gF-Zg
=5%Ej*f}sOrU6xMm@^K2Gv`kOHfa3ZXuK9kM6<3kVR$yo()Z<AYnTw)vRo;*fhbd3BPD26>&p9Xth5Z!Q<^c{1W0ngPfA5Aa|TV|
CaahRY9U%>1$`?D6v7)wHjum^*3y?S0aecOoT261YzPHbrPl^pYXxsW*?{sBg7SQ<6-?>0akwUo)D2TMp!}>%c^=l%Or(Lta?KF;
altm2Q4S%f|5kOT8&Ec&{Dh!9A8UyzU9P24Ik1ZM8m4SO`5Bq=T&xu_rBYfVp$3>(6H_*z{H!tMc~~o$lF`OiFe&4<Vaf)SpOq=k
!&;gyrzv#HwII}<^<LWsk_{w33X<m`tzb#6fKmX<GS{%=6+!Y^!Vz6D6_z{?YehV%m4BhU%Pnu>$p)045tQd+tzb%_aK(cwZ<z9P
gYx2l{JO!2I%S0=&%;?UKPf0Tw+4ci&HUtt0I~t&A{a4*$~Uv0i?f0urOKVLM4zl-$g2S4bp#{s(G`X~4`)RjX{6IKr=4t~i6bu#
$ZrLV?+-*YOGBZuq#9j`CC|fK!IVIivI;VCykW`)nC}D3^FfL0d4)00!&};04*VF2E+S1o^9$M<Sboj0yc$TN`;|TB=b)`%OAV|7
Nd%;ZE#Cu{4J0oBN&Ky5;OF73h%c?wTpBCsD+inSvH|89z>J{0ARtkWj_IXx^fCcni8If`UBR42=Egau(ESTAr!vyeLlH_VXKA&_
<dT++koBW>0wy%f&^97mX>tune-eP|55i>wN&@A_0@8!A0>mXCMB6kJDv!EIO@f{UM;VE(W7tAhGxhWESIlKfX}AIIWUekSm-(du
wL$6Eg;Jc;l}XO?09a6}6#%scthM?IDYZfBRU`HNP>LTMi|T%(^FUZcs7`WAAtqDm0ugG1*2_Taha&YVP<nBMLZc7?X_mxDeafp_
H_roO!Ld%roIy-l=`WsRzf8zpGq`?!sA4!YBoYs)lYU62szSWyAv10C1kj9iN?D`M-{{!@xE{dQg=?<_xad31JJbjL3pGFWdLBL_
j7^>kz|GNjHJOHqKRJ-UAP}Dg;Pb%y34vP%EmzbgKBElqhac)EftkjF@-!|xzn|}X#HJ|+@ObW&gmvbUi47dnBcX^z=%uYSENvxH
1&uOJxI71V=|y%5a1a|fjoY<?Phe;f<E0f1ncD{34Y)rcxG#d)l=-P#IH?&@MXArv{2FjK;J#vTpO4rXb8}F<%F!dptYPj3++PE8
pNrWd=4RYLRaWQX0uQb>;BLTu<uUhph@CMvl0syOgj&%scLVOPg1OJdY_W=s(A-)m1E9UYDz*~_sLd5qQlg+UPAX`YyA6rj0cspb
Mf-vf6Im{4GNl1`1MW`<?sE}aVs7VzmJI*N3ov&B?grdn0CS&**&^oVP%1iZ4Zp~15E^hd;J)gZ`#i+Xm|HsK3`1<5tA@G1WpG~@
*p~-te5U@3Ds!KU*<zlXzB~`9Csb-Ku*0bVcLVNE4DLlR<1Z;Vugq_shtwHkEB~q-r=`=^kFgs>f4zuCSrR?bIE}$pY5QE@76CV8
DRG_A4BvGNxEq9jG{Wo9eW}PsdpHkq38N~J_j%Br@wm1QEKk2o!{grw%FjUfmw@hhWc$7CLND<6xxh^rZ&3WnQ2d1;`2Ep)5#%mG
Z9?q(p*15(LT5tJ4|RivL&gUn@BH)U(RbN*`-8W-+aC;$yQhQk@cFx&$M3$|{O*7KYvW`x-q;-;Z48c1SB~FJ_eV$K&!a!TqyKNe
?d?rheEH#CZ#o<ut&ENi-fgZNjaDY316;^fjt0{=qw%Y3<@vz~MUGyq^v1*K{^4Lc+*=uqS4Ic@mFL5Q!Oc+RpGU*P<I#A!@^Ugd
%JzGc{e$6dHhDMs^XU0_bhvWdo6?z;Sn3fD<CW)QbOv3Rq-%HLiIv`D<xWxWY@B<e@qn(q#&C`v-Fkfc!PCxaZ}Osh{DP_9{&@a>
yT1+o`tQlBAGG-W=<(?1zgGV|dUEd;%IxjRypLbIyT&QSh0J>c2dh+ry!V{#3G=*f;qsnK*>h}nu-j+5igv-fes0|0IqJD{|KY>O
ojWa9PQJFrOq=@9A3R?<9QKb#!=q{Iw7oeVOi#u~D|cF_HxEWPPH*lHGrsov=96|PIzH;R-e$YQ>7=7&d-Knum7@;({(CyHb=rBm
cC=Mg(Bf;SH;+yZ2jkv!G)7hZ!O`e&ctl6-jSYXfd@4JNZG^r|v%Rc8?c~0ZSn2DVhoi&6(R9*!ee-9O=ug|(^yK(p;Ezw+E6<_a
)0N@T%3ix%S@$QZ&e!xu=k?9W=w!S%XieK&&pP4uRLM`R)Ae4gChJi}e+`dY@3Pl7Z?(hecXaX(RKC*h$D7%W$;n~sWc%gL+8%!S
VlS!KxOeno&=T>^6FT*b?(9t_1E2x}_fnqqy5DdAJ4b=vE8V(<YHv^j8~y(FaA^y}%(pR!LLaoAkrY;b?a;vT_SW6bcKGB=cgq#*
Z2i{RUVgRa6e{*@_9xl#=-^$F)$5y2Z$Etkf&KdMe)rMC`+q#~VqZBO9r$ig+3kGi#&j)wWV4T)KKf5$r|o+lTA-@Y%qCTVpCAKY
=V>R3=&(mE{}l9;wQq#8zb9FxD%x9<Nfa%q>@;c13;#6YXI`*dzuurmQ)lKb`hl(7CFM|=waJ83B>h<`{A#Z7Z@9SqDi&?|vUCT|
q`s`3;%Kfz?F~+NxEnity7BAm^4&IcR>sNP)o~cim_GkTvb;A}R;{&Sf7Yr0Yj^RfeWOL6*8|?#Yb`qIk8o{qKy}iZnd<M^-RxfW
YoeIr@t{B4BdZ=B4X4B2ffwFh>{B|IFg2Z3Y61bQbh8&!U#D!(TQ6S33Q7z%6Tu4)q5b{2f!CHS3+rBc>oJfzJUVUd@B12tV94Iv
R&RIGdK(J9_0_*<fA1-Eb9X%Gy`qwnX(yR%e>824GnARt{J6dK9Nu9xCJrv(U6QGeV_n%xf+4y+y%FwOn<QeIBxBplCevUjE7S42
a4#f9|DW=*sP;mkmHyyh+KY9+U4It_lNH9hx0mh3`c`&FCrACxDc|^Yovq6?e<zt}7}|>$nLiT?pCzK`Z)}@9udfwO<@<alwUxo!
y}|Kx<(8*KIM3VT@o2nx44Mq4<cGh};dC@Om<%?@z2Rg~Dc@R+7(*)u!=u5<WY8P$?XUVC?sfL|@b^MD52r+)<kbDW0eIcc%qw}_
C5+T#>t=5$y1eTs>o;L#p^n`-EVt*7H1i_3eK2i3ZvU&3&#Vuwb1!?G4X4Tec6;N&a58E2Ji>aN?StWD>S+^gW#e+?y`8P2&cWaa
Ww-hrwl#SH7auLN1lFT<7SIaa_rMVN*XiT|gD*QrgSXSx%PK>>y20S(!yTS{+FNvMMn@g`mC>PZaUH*?uH#Oue9j$|tJ^I2_GSI0
m6Oi#S`WT}$j$$KwX^1HeYvw0rFinc`{?~vEY&&L*yz)}{m$|7c4Jj#xuesld7bUhPm=v~JQ#HM_6K{fT2FnK?!(pQJ8LYjx>c6X
{A%V$^ZMrP&HL2O5RQXw-6yfVj32{*(%B(>oWUX~e0#jjHg{&)y-$Zb?M_D`X76}CKP{oDcW}_6b5oRX{w~kOPkpTT<E^K+I<1yK
R+v+of;>kfb9C7{7mTZR)<RZ`%wk>SloLrr|H^7Bae<~{kmgxNmyOMlni*?Uj!X0<tu|X{PKg|UkaZ!+SZAo;aJmzz79}tSzm;Nw
sz+*~Qh+xZ_6J==_T%AR3pr`Pceb0IWTzb*Z{0(W@3ea0Ao{PJ-D&Nn&#1k0ge&3GdQlke|9J;xPD*7?i;HOJRkY*vWW>+sJqd_B
@SndUa_94G-bp-P;D-mD);$W6TCeasYiIW;Ou_-9gK*LxfY;kwMQluT^q`$RnEBk{Veg>3e*&FOYl7e55y`F;54}tAPz-W6B0?(>
(eXj=XfWw)mqNe*)jPL-@D@kn-|MvgsD@wLn+WW-PL}(h-K>ZDPtR~rRDhZ|>LB1|6fyCg^%MNUCkP~d%IRDlu4eHQqjM}=ZEx*&
g7lBFUh?tjL=a2+-}{?KNxN@nF71f!UElY^3?_5*uTCq^@c%4g4IQ4v;eUWE3byu*yla2o*<a}$^;cT6Q=QH}ep*Ge>iN$L`)2R>
cmQ94V*Bk7CXsiZfcgCq<)Y-brlZk8k&Et)4tFWHB3CxAs`8aqP^@cbF`%W1ojCB&I1x==38ZH-Ll@|dHj)3{=m^>N$-q~$zgP>a
hU0H5@e*z-8AE`yuRS$L{FDUt*2|DeLn>50G}PYo!nxV&BULR?TM(I-*&h|gi+J1EFYCF}dHvcSd!c7Ih#(BjAlLYBIpF;x3+I#d
ku1iegCg-PTykd?3nPRbjK{N-TvC0nZ|)(*9gMqs6rlJ?4w!4^^I@t1cTlk+Mx@j?WUjc9o!+49bD8kg@4r(>NCC@X??t!)iSr&^
nNJ{Yp4LY#zyD4xrV)1LiDe5ZTbT~#l;IKeS7(1cDUC9;EyU#eH~w1N+k<`HJT2MM{yy?yp8~J=S`+R=|5``n`}}<`abJ65f4_#G
sH?#rpi`~Y(cy5qdSfyjw}zA%R^3H3SbUr}S@Lz>83T0Fj#m*6_VLS{%z{H$TXRbSzE(>LX5id79HLOlaHcppOdLqYy@xAKOPQ;j
NoA;jwm8K!3d~BE&S#7pV_eQm%$4Jq3#wS%AHLWhOs3tV(b0G`nsx`1z25O)HTxwChV@Ihk-&=X9=3kTz_i5-5IKamFxs_WLZGo$
c!yzG-1SM|=ww;~MDK8bMjue2*vZYBs7lmFa-!f)>d`MTe0vbWx0<Z9)1l~j*y+41`1r8rgBT3(L5YZu``sbg*=g^fwJ-~`M4PB7
2>W=_`TL)(*Z%jQkKZ%yFXFZ^nk?n0uR>?D@jTGH+w?JUkcD>&Vf<i+{x&My=^$nZ*{rVv{xv`g*8q=~*|6Q-Jf3Xh{7xsT^7rlD
PPWvK{=U7t<BLS>%vVc|Wvv$oOxl~T%hf)}yj7lAbtr-AQ_<K&lsg5N$K);O!)y8=Wa%=o@u}wk$`((3rZ`iDPg;&AH=(kV!KBr0
-|%N%m(KXMo^`f|Rd^w`P7b70Eds;ccIGQby>Ow2sKl28j=cS^JgKS7om1EAC3W2cBazZV`Jg_MwueN2?w<L&eXSU}heL+HQ2I^=
<=}4r7utfPcPf&80tw;Iv-Uduxd&-;kFVU%MMj@W_IYzM?Tx3CH^b?Eq|9iIqeE{`REBbz_Et$zuc<r38*C>itRf>7K>e@I=&<b@
Me)&LHaesmXkex0JDp{06?$<5Dla&yJj3vNk-@c&CKUJKx7=xm4pF1j&z3()mtLkz6_O$U>%05%UmY2G3mMBS-zoeNC@oRz->cN;
)lE-qtG}#nZf}!+nInx-%Js`mw))__LJv^r$?E2lZ1vgd=Cf?|-s<MPZ1v5c_X?TA>gLn&37QIycXjh`s_9jG^YkWth;wsQ6#s+r
ql4b~%;Gbk{__u+&grh`g!$~~WY<7Y|JfEhrHR3M%1?gM(E?yz@GL4MWv>fbM3_ZOf3HqgH>o!WL{|5@yQ8-dP&JAvbvJ}EkkRRI
JUv11@gK3eNp<@o+3I+(HyZaRtD8{MKPd!ze$bnC_Yn4h<x@E3VLgrhe5)=fgG)!E*IpB8I&v}{9M488i}}bG*}Y<7D9uPdK6_rM
to-CxLf(hOZ>u~jv_}~~>EZF?=zoh^Uc6YMh0Ln<qF1G1l%q_<99v&(jM-fhV?O$b_;PD8xP0`Xf#qF4o8Xx7IlZ4V$W)j}pbt2<
B3x=0RCyP?gnyBc;?de&WJ8pc`eWp!YutD3(W6f5(YD^n9&KB&?JxP9^av1l;ZxyX*B(8h4@3W9w+M!Mvo7->-QDt;_R_VZ1;`-8
Da~DM&4<0e<N=j8S}5mv9s!r1UtP&B-i9|)B6aed<-oI74m@|?Bk=q&r-<xF=6~O&-^aZ%tr&Lx=9?~aoBW@xr}&&XirC;By1j8J
;hj0>7z`nfD~ENh;N!zYMSFg#ZdREG<)Hr}&8_?%S6Y4#!D~&>y7glo0zHyOo>9S!D!>I6E(Cm+FWe3n;+;33hqYK3&HH)w-uPWP
-dN~o5p+I{LFdsZ%=Ycf(ql@OQ)LJr{%-M%Chd5}{BMijE))K@ZT~Z$R-<c!;Oc$-=y5uv?hL4@qUtEiL69=^<EsQ<y)ge5DK=lZ
{rjySp5Fgs6SqzGS9*Ko2|}W%GrKZ)jYGDAVBcScd3(N`+^ocxyqK-pe!k;-=H|{&Kc4%3pw_wI74nTE*z#jb3#)!)ov499F)ub3
e5SebAx)Ib3yE|#C#Knn0L2=;`Is^+h<Gg~)x`;T#7i&FzB#lN8!y78)Ht0eLaUdPWJQ2qhnB5h`WYY}m3hD}3(8XTm7gDd%`It^
bF*JOQyg}}T+=TFt@aNSo%i}LOS6#+86`#?E-zcb9e1{SRq_-e3jbH<<qj<xpHU#JMN=z9>b=g|Yiq6HjhF2;WUONhe`k9_QXo<r
gYEqx{;Zd-viYkx8?o1anJT6U3qL(vrsB67{ll5;i#d%rqk+5WmjC`pTzIb}rujUT($wu&<;ZYphI%^7P)`e~*5;1?{W0c_lsP^+
GixLl=8LrFruyE_tiX@174ezjug`$cgwKHRH)KGY_X;f#@l_`J-WI84wPv44{&>5ZTK@OPQfis4Y`0b)t!9u=h&$&(Y1~}O-zbUw
zLS67p(JkS25$WCvK!IH(i_qJbCTJ&)dckIVrPm3^z2-=zN-1|6;(y4KI?S+7C;x6bV<@#3H(>t24D5*$)LO2n+y@RZ-Z+Q-rr4m
QkhT6dD2}JLcd>e)PmsX@&9|ea(Cr%=4Y*GQC9!Ir`c=!|DJBGyc&#GenFx;S()w+R;EaxyiewCr9VWvK$G7$S00Q|>FHpMxCMR#
3_d&<9pyJyGxT_MZ**|bJDv>s-Q(U6dDJ!yGh2Q1<j3xWrm?29ZEZSu+eOMoYcl={rEJ~ln^AY~-5!P)iF0)`e#lnitw>Z}z&*X_
?wvp)$q#0$u@7EIA@+i#a3}iQJswSl)8Xl$8w-Voz4U#D$AcFq$oPhTq07%{Q^f!Q{?X(F&HsH~cKOeH<zdtsG>0yopOXHVmr~Ny
^NZYfyY9YoQ`#9`|0y!TN$(VN*&DwYOtbM|a&j=u4oCfg=YN{3Y|+lYoBfl+<4G%CpNz)S?yJGONyq2jlK~V+`_v|#78H^}Kj4Vf
KmR;hZQmRm?V+|-dy94oc4&WKY%C_m)K;gnx_dG_=o1pA`#0Z=Njtmmrl1z|pq+LnM6>c`#)Doz7J(6=6beCZNCEw2Km9-^M)#*}
i#I3xJ+8DrcXNO6wm*C^0FRYdDttw8=U)%bJS>@pcDvpFVE5!jw@atSFD9MIyU9&_IHhIdEk6!AO;bUh4e&WkvlJ&m(s7^w6fJtM
wnJVJ&yq9W4KiAt?ThU9roEe_1W2<y>@B*`@!B~U_4<=me;4PF-p!8|XUl_40q}%Y=4_tPdNr3hJ-$$c4<tCMe0z0oaBwhLr8RL}
4+@(fSH1(~LH*M(8%3Y|q?o^0niB(Q)3xvYgyvHOEVS}ZgP7X^uyxp*yqc6ElIW>JXNbpEcS2ketEKCSTPYk*Zu(8~_i;AWyZ$ui
g}%J{-p{e#y!AMo9!`cwlWFg0Z_s*^q5t9Rn;4Ik>hq0HPL4Z&SDX4LbUwLQO4Zo+-^YC(*>pZ`c<LPn>iNDCXU+FI#pKG?ctDGk
B!?~3Hu1YCLVka8ICD-xjoT#Fovd_l17eSRrJ%jeoFcbT!_L;hDBB-qgK>v8x!lQGba8w2V6?iEg^&Bg;v+~7`Y-fIX|HU5-+?2B
L-e~UR%+JoS_h*W`@{AI&*Ju~*Ej!j>%ot+<vbov`>Cg}EjXJT^!C70elujv6in!JF$vQy!@%GA@7Fh<Y;5?QP%F1yW^Yi959_-x
2h&OUcHF$RH-di(f{m-c-kpXqmw~o212D>X*myn1d0PsBhW#$?Xi=M48L8X2VFwW(WS)iQaU$*t^X>mn$5-Xcc}?Gl0*!5kPId@K
v?Zmz&gNwqmep4xTxL_SLl7986}3xR^^=JQqjpAm^#@Q57zpmH8cxtOV!!S}pRN!V{QZz1&A1MrzW$Ju2VEfp2^Z6@D-<~zyqUr=
m9~v-4yR~&ruD7|Zn*JIs|*L)SdA(|CfhCThVCAW-VDa+mVlaA7~p}075ULB?Tam@K}jc@Wd-|L-QfR9bnD5?FN)G9__4sf+25<A
+iqah)y@8X7I}|;qo2pe2XWIqnjvLo(dag#e*Ou5)zhT+RI5H`@BVQ6!PCbNfBLZtrFL)Kzu%=$>DJ@_JbZln39kKcyZh+Y<EQxb
<jHF08}p17Ds5-fRB(~?<V?ZNWIxdJ0<mmCiKm@l)QM!MiG?}cmGQXjYN|eJiO{0Mn$nK98HbF=+jFu+FZ*G`2VL=1;S~KX8w1k6
2<%eGOE*Mn!!157IiDP7%X-y1qRH3r=B)7|fgcCT>~v=I83qyfGo7c;>AWY?bip5_D*=(|QaGC9pF6GC9y}T;?R$TMDsLwxrsFwM
faraCJR4*?QVpG&Lv4A5%vafAg>y}C^MOD>7y+n5Zq8p%oi0sVr+d763u_F3-fZ*7Y&BuFo30gBAF^VxB&^$oz_SBt>r=cxeTNwH
-tFIY_s83}A9a6v@Z;@AxAE)2(=JhC_wN0N|G5<m>A}MXw;uiU1CE|`f0e7=Xi>%LW_ZFR9T#@}<le1p(bD@P3J1Z9$ULYL2LI>*
L5xecBU9;)d;KBh6Ge6s|3mr7{_y#9{>my*5^za*4m~5Xx(QzY=_&FM%E!8tkNI=A!7bxJUKFontIvCTgK0>i{JA@~en{*#3*4eI
P}yL7h%1GjO8TjkoM)?gM)OhI>Lz)kNaG{ACw&U}XGrnp)|OT`YZsjUsUzUffylb$jHJYzzuvn4(~q~F-Ud<r@bnp!Taf4v&mRAJ
+tcU|_a8n%fgf()zyBn%XBo-m>Zmx4sr&fh!>4)o>EqkCpLB2kdi(JogrEO=`|(4MrC)A8ef-l8-P^zaaR1qlsM=RruIKT?-=1`z
-hTYclkTlYkM09@Pk(y&;7J-r5_WMIl(SQCc&g{gANPN~{R9;O+W3vpcJDsB_4r5BL`B#1eCO}p{?FrE=-8c~ey3hNynnm<!$XqC
ecZ6!dW(k8$Tk_NU!C2_qRBoX#mCRjN}umh$TtHDDoBfnJ3HlQA*y|++#PR`_kOy24+9|Skx0AnWVasO_8#unpB{US-Fx`>r~mu#
LDAD1Y2JG9f4Wb9d)U2m>;9A5-Dk`n{P4#Q7~kXDcc0zAg&MquA3S+h7V;7d?rfhi3oti^8MWMb79H}FhtD3v6+e7%{|_|&!$S{_
qRXY-^H1JQkYe9{J48LtCcPJf&G?w!%KCp+)}O4@JlGdpZvH>)fB6516`u?Kk57rVXgV%9@bYPD63)KcC2e-QaPr+Q@l&_Ex*5{e
Kaalq=l=)Keepa
"""
raw=zlib.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==196955
assert hashlib.sha256(raw).hexdigest()=='18d553869283194862884142139c3cf0ec38f4bcf2215bd6c93caa447affe85b'
PINS={'hex6_deep_core.py': (7722, '7f22548ba7aeaf3af170afaa339f8f3c1c26610719690301dc5dd2b3118bdd5b'), 'hex6_deep_verify.py': (14118, 'b9cfa61b273e886fca8eb98a1bdf6695306015ec10f97dceb2cbbbcc20690893'), 'hex6_deep_data.json': (169963, '521d4e769392e75fa2483c6976b03a565977a1edd94e63eeec08b967b04df05f'), 'hex6_deep_part0.json': (92082, '70cbc033673a502416f9372480f1957b5e8aced1884bca78816ec157ac710d0d'), 'hex6_deep_part1.json': (94651, 'bf60a81d42d57a5cb3b419b972c0a8e946d21b7f669ee74fefd122cb821913a4'), 'hex6_deep_part2.json': (101577, '81011e4ba2c43012b2ca4e8101f5d1ac933154e8090251fb67a1a4e69c8d5ec8'), 'hex6_deep_part3.json': (126501, '39782096932dd6e6cb878253345d8e45d5e2b7e2a0020e92fba526a91f579fb7'), 'hex6_deep_report.json': (535691, 'df9d7e4bffd025f004ec114c683002ef38d5c418ca85036c6ba66a6d553d9b13')}
for name,text in json.loads(raw).items():
    b=text.encode();assert (len(b),hashlib.sha256(b).hexdigest())==PINS[name]
    Path(name).write_bytes(b)
args=sys.argv[1:]
if args!=['extract']:
    assert args and (args[0]=='finish' or (args[0]=='part' and args[1] in ('0','1','2','3')))
    sys.argv=['hex6_deep_verify.py']+args
    runpy.run_path('hex6_deep_verify.py',run_name='__main__')
    target='hex6_deep_report.json' if args[0]=='finish' else 'hex6_deep_part'+args[1]+'.json'
    b=Path(target).read_bytes();assert (len(b),hashlib.sha256(b).hexdigest())==PINS[target]
```

Convenience copies, not dependencies of this handoff: complete recovery wrapper (`recover_hex6_deep_v4.py`), readable mathematical core (`hex6_deep_core.py`), readable verifier (`hex6_deep_verify.py`), exact report (`hex6_deep_report.json`).
