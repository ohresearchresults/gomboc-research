# minimum-0030

Historical AI scientific report · saved 2026-09-08 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# NOVA24_C32_TYPE139_WHOLE_ACTUAL_U_GE_2_V1

## 1. Determination

**Whole-domain theorem.** Every full-dimensional homogeneous convex three-polytope with the actual maximal-facet cycles of canonical C32 type **139**, specified below, has **at least two strict unstable vertices at its own volume centroid, for every positive-definite physical metric**. Nonroot escape equalities are allowed. No additional assumption on the number or location of stable equilibria is required.

Consequently this closes **one previously unresolved complete type and all 45 of its joint unstable-vertex/stable-facet root orbits**. It closes the full realization space, not merely the parent's two-parameter family or a large-parameter tail. There is **no unresolved root, escape tree, metric range, or positive-volume realization stratum within this type**.

The proof is finite and exact: **12,183 rooted-tree orbit certificates, comprising 104,736 integer symmetric 9-by-9 matrices**. Every matrix minus the identity is positive definite. An independent standard-library verifier reconstructed the scalar quadratic polynomials and checked all **942,624 leading principal minors**, with integer Bareiss elimination and a separately implemented rational LDL factorization giving identical minors.

This is **not** a universal nine-facet obstruction, a C34 determination, an improved global complexity lower bound, or an attainer. The inherited bracket remains **32 ≤ C_min ≤ 1374**; the previously accepted whole192/294/295 and individual53/U3,72/U4 closures are retained. The journal explicitly distinguished its conditioned-core results from a whole139 theorem; that distinction is respected here. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## 2. Authority and exact combinatorial domain

The authoritative parent is `minimum-0029`, `NOVA24_C32_CONDITIONED_CORE_OBSTRUCTIONS_V1`, SHA-256 `07da26de37a7076fae43373e6ecd0c85ba0b45ffbe359ed38b707c462083dd8c`. I authenticated its **36,226-byte compact UTF-8 version-2 JSON envelope**, with the Markdown's final LF included, and replayed its complete recovery source. The inherited 63,296-byte report and 618-byte transcript matched their pins. The transcript SHA-256 was `f7b68bc5984b3186cbfc6c125bf2f88e337f60237ef76cf54204f58f0a37eb4b`. No incidence or alias conflict was found. The parent's older catalogue counts are historical, not replacements for the assignment's later accepted closures. The recorded parent replay pins are also in the supplied journal. :contentReference[oaicite:2]{index=2}

The canonical label is bound to the accepted 240,929-byte catalogue with SHA-256 `efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d`. The new proof uses the following complete literal face lattice, which agrees with the parent, rather than requiring that catalogue as a reconstruction input. :contentReference[oaicite:3]{index=3}

```python
FS = [
    [0,1,3],
    [0,2,4,1],
    [0,3,6,2],
    [1,4,6,3],
    [2,5,8,7,4],
    [2,6,5],
    [4,7,6],
    [5,6,8],
    [6,7,8],
]
ES = [
    (0,1),(0,2),(0,3),(1,3),(1,4),(2,4),(2,5),(2,6),
    (3,6),(4,6),(4,7),(5,6),(5,8),(6,7),(6,8),(7,8),
]
AUT = [
    [0,1,2,3,4,5,6,7,8],
    [1,0,4,3,2,7,6,5,8],
]
```

Facet indices are their positions in `FS`. The nonidentity automorphism induces the facet permutation `(0,1,3,2,4,6,5,8,7)`. The six unstable-root representatives are `0,2,3,5,6,8`. The complete list of closed joint-root representatives is specified without abbreviation by this Cartesian-row rule:

```python
[(r,f) for r in [0,2,3,5,6,8]
       for f in (range(9) if r in [0,2,5] else [0,1,2,4,5,7])]
```

There are 2,703 labeled spanning trees of `ES`; both exhaustive enumeration and the matrix-tree determinant give that number. A rooted tree is encoded by the nine-entry parent array with `p[root]=root`. Its canonical representative is the lexicographically least array under the root stabilizer in `AUT`. All ordinals below are zero-based in the sorted list of these representatives. The verifier independently checks the graph's three-connectivity, oriented facet incidences, automorphisms, complete root coverage, and every parent array.

| Canonical unstable root | Rooted-tree orbits | Integer matrices | Ordinary certificates | Shared-second-moment certificates |
|---:|---:|---:|---:|---:|
| 0 | 2,703 | 25,760 | 2,695 | 8 |
| 2 | 2,703 | 17,635 | 2,691 | 12 |
| 3 | 1,358 | 13,375 | 1,353 | 5 |
| 5 | 2,703 | 26,513 | 2,696 | 7 |
| 6 | 1,358 | 8,406 | 1,357 | 1 |
| 8 | 1,358 | 13,047 | 1,358 | 0 |
| **Total** | **12,183** | **104,736** | **12,150** | **33** |

## 3. Continuous physical proof

### 3.1 Every hypothetical unique unstable root supplies a covered weak tree

Translate the actual homogeneous solid by its actual volume centroid. Let its vertex rows be `X=(x_0,...,x_8)^T`, let `M` be any symmetric positive-definite 3-by-3 physical metric, and put `G=X M X^T`.

At a vertex, strict instability means

\[
x_i^T M(x_j-x_i)<0
\]

along every incident true edge. If there were exactly one such vertex `r`, every other vertex would have a true-edge neighbor `p(i)` with

\[
D_i=x_i^T M(x_{p(i)}-x_i)\ge0.
\]

Along that chosen arrow,

\[
\|x_{p(i)}\|_M^2-\|x_i\|_M^2
=2D_i+\|x_{p(i)}-x_i\|_M^2>0.
\]

Thus arrows cannot cycle, including when `D_i=0`; they all reach `r` and form a true-edge rooted spanning tree. At least one strict unstable vertex always exists: a vertex of maximum squared norm has strictly negative edge derivatives by the same identity. Excluding the unique-root case therefore proves at least two strict unstable vertices.

The enumeration includes every possible choice of weak escape arrows. No edge introduced solely to triangulate a facet is permitted as an escape edge.

### 3.2 The masses are the actual volumes of actual tetrahedra

For an actual vertex apex `a`, triangulate each actual maximal facet not incident to `a` and cone those triangles to `a`. These tetrahedra have positive volume and partition the same actual solid `P`. In the source, `fan(a,s)` first cyclically rotates each eligible face by `s modulo its length` and then triangulates from its first vertex. **Here `s` is a cyclic shift, not the bitmask used by some earlier capsules.**

For an unordered tetrahedron `t={i,j,k,l}`, define its actual six-volume

\[
d_t=|\det(x_j-x_i,x_k-x_i,x_l-x_i)|,
\]

its nine-entry vertex indicator `chi_t`, and

\[
J_t=\chi_t\chi_t^T+\operatorname{diag}(\chi_t).
\]

Write `f_at` for membership in apex fan `a`, `D=6 Vol(P)>0`, and `C=E_P[xx^T]` for the actual full covariance at the actual centroid. Uniform integration on a tetrahedron gives, for every selected fan,

\[
\sum_t f_{at}d_t=D,\qquad
X^T\sum_t f_{at}d_t\chi_t=0,\qquad
\sum_t f_{at}d_t X^T J_t X=20DC.                 \tag{1}
\]

Indeed a tetrahedron's mean is the sum of its four vertices divided by four, and its second moment is `(s s^T + sum x_i x_i^T)/20`.

A repeated unordered tetrahedron has **one actual value of `d_t`**, regardless of which fan contains it. The proof does not assign it independent masses. These equations are used only in the valid direction **actual homogeneous solid implies (1)**. There is no claim that arbitrary positive or signed weights satisfying moments through degree two are the actual uniform measure. The coordinator's stronger degree-five physical gate is not needed to justify this direction.

This extends the actual shared-tetrahedron and common-covariance certificate architecture already recorded for whole295; it does not import that type's incidences or its finite coverage. :contentReference[oaicite:4]{index=4}

### 3.3 Exact quadratic contradictions for every tree

Use the following integer, twice-matrix convention:

\[
L_i=2e_i e_i^T-e_i e_{p(i)}^T-e_{p(i)}e_i^T,
\qquad \langle L_i,G\rangle=-2D_i\le0.
\]

The nonnegative numbers `lambda` below are **certificate multipliers**, not masses.

An **ordinary** certificate assigns to each tetrahedron occurrence in fan `a` a matrix

\[
Q_{a,t}=\gamma_a\chi_t^T+\chi_t\gamma_a^T
       +\sum_{i\ne r}\lambda_{a,t,i}L_i+O_a,
\quad \lambda_{a,t,i}\ge0,\quad \sum_a O_a=0.        \tag{2}
\]

All `Q_{a,t}-I_9` are positive definite. Multiply (2) by its actual `d_t`, pair with `G`, and sum over the fan occurrences. The gamma terms vanish by the actual first moments; the offset terms vanish because every fan has total six-volume `D`; and the escape terms are nonpositive. The result is nonpositive. But it is strictly positive because `G` is nonzero positive semidefinite and all the matrix factors exceed `I_9`. Contradiction.

The remaining **33** certificates use distinct unordered tetrahedra across two fans. Relative to the last fan, put `h_at=f_at-f_ref,t` and `gamma(t)=sum_a f_at gamma_a`. Their matrices are

\[
Q_t=\gamma(t)\chi_t^T+\chi_t\gamma(t)^T
    +\sum_{i\ne r}\lambda_{t,i}L_i
    +\sum_{a<\mathrm{ref}}h_{at}K_a
    +2\left(\sum_{a<\mathrm{ref}}h_{at}\eta_a\right)J_t,
\quad\lambda_{t,i}\ge0.                            \tag{3}
\]

Again, every `Q_t-I_9` is positive definite. Summation with the **same actual `d_t`** cancels the gamma terms by the first moments, the `K_a` terms by common total volume, and the `eta_a` terms by the **same actual full covariance** in (1). It leaves a nonpositive sum of escape terms, contradicting strict positivity.

In the stored integer layout, each free symmetric offset uses 45 upper-triangle coefficients in lexicographic `(i,j), i<=j` order, with twice the coefficient on a diagonal and the coefficient on each off-diagonal entry. The complete generator and the independently written scalar-polynomial verifier below implement this convention.

This proves the theorem for every actual realization of the specified face lattice. Arbitrarily small positive tetrahedron volumes and arbitrarily ill-conditioned positive-definite metrics are included. No compact coordinate box, metric cutoff, positive uniform mass lower bound, genericity assumption, root-closed subpolytope, or deletion-preserved tree is assumed. A collapsed solid or a singular metric is not a member of the stated physical domain; nonroot weak mechanical equalities are members and are covered.

No polar body is recentered, and no moment of a polar is substituted for a moment of `P`. The original body, its own uniform volume centroid, and its one physical metric are retained throughout. Therefore the result excludes all same-reference joint unstable/stable-root configurations without needing an additional stable-root test; it does not automatically assert a theorem about the combinatorial dual at that dual's own centroid.

## 4. The formerly omitted cap excursions are actually covered

The parent's local-to-canonical map is `(5,8,7,4,2,6,3,1,0)`. Its small cap `678` is therefore the canonical vertex set

\[
A=\{0,1,3\},
\]

whose only external ports are `(0,2),(1,4),(3,6)`. The parent correctly required root closure for its heavy-core inequalities and left forced communicating excursions through this cap as an unresolved complement. :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}

For a root outside `A`, call a selected tree a cap-transit tree when some arrow starts in `A^c` and ends in `A`. Because the tree's root is outside, that path must subsequently exit the cap. The independent verifier counts and covers **767, 767, 385, and 385** such tree orbits for roots **2, 5, 6, and 8**, respectively. These are combinatorial coverage counts, not assertions that all those trees have physical realizations. The paths are neither removed nor shortened in the proof.

The theorem also covers the complementary trees, roots inside the cap, all moderate-mass realizations, and realizations outside the parent's two-parameter family. The conditioned volume-gap constants are not hypotheses of the new theorem. The route to closure is to couple the actual decompositions of the whole solid rather than make the inherited epsilon smaller.

A particularly useful continuation test is the root6, ordinal836 tree

```python
root = 6
parent = [2,3,5,0,6,8,6,6,7]
initial_fans = [[6,0],[7,0]]
selected_fans = [[7,0],[6,0]]
```

It has the path `1 -> 3 -> 0 -> 2 -> 5 -> 8 -> 7 -> 6`, with `4 -> 6`. Its complete shared certificate has 15 distinct tetrahedra and 184 integer coefficients; the last coefficient, the covariance multiplier in the convention (3), is **-2404**. The complete coefficient vector is regenerated by the capsule. The differing initial and selected fan orders are intentional: the source records and verifies the exact row permutation used in generation.

I first used depth/first-moment screens to locate difficult trees, then tested alternative actual apex fans and finally shared covariance certificates. **The final proof depends on none of the preliminary screens:** every rooted-tree orbit was subsequently assigned and checked by the explicit quadratic-certificate route. Numerical failure of an earlier template was not treated as a feasible physical control or as an exclusion. The general strategy of locating quadratic contradictions numerically and verifying the resulting finite certificates exactly has a published precedent; the full type139 coverage and data here are the new result relative to the supplied state. :contentReference[oaicite:7]{index=7}

## 5. Recovery, exact evidence, and pins

The capsule reconstructs all source files and all exact coefficients, including the 33 shared certificates; it does not need a frozen coefficient file as an input. The numerical environment used was **CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, OpenBLAS 0.3.30/SkylakeX, Linux x86_64, one BLAS thread, four fork workers, no randomness**. The decoder and frozen-output verifier use only the standard library.

`type139_plan.json` contains all 1,063 nondefault ordinary plans and all 33 shared recovery plans, including original/selected fan orders, exact parent arrays, rounding powers, and integer factors. Unlisted ordinary trees use `[[root,0]]`. Ordinary generation uses `eps=1e-7`, `maxouter=11`, normalization by maximum absolute coefficient, and rounding at `10^8`. Shared generation uses `eps=1e-8`, `maxouter=14`; 32 plans round at `10^5` and one at `10^6`, as specified individually. All integer factors are one.

Both locators use the fully supplied log-determinant/Newton source, not an unspecified external SDP solver: initial escape multipliers sum to one, the initial margin is -1, `tau=0.05*0.18**outer`, at most 70 Newton steps per outer iteration, the stated symmetric linear solve and `rcond=1e-14` fallback, positivity factor 0.99, Armijo factor 0.05, at most 60 step halvings, and decrement tolerance `min(1e-7,tau*0.001)`. These are coefficient-generation settings, not restrictions on the physical metric or coordinates. Only exact matrix tests determine acceptance.

Save the complete code in Section 7 as `recover139.py` with UTF-8 encoding, LF line endings, and its final LF. In an empty directory, run:

```sh
python -S recover139.py
python -S recover139.py check
```

The first command extracts and authenticates the complete sources and inputs, generates `type139_exact.json`, and verifies it. The second rechecks the frozen certificate using only the standard library. Direct verification is also `python -S verify139.py type139_exact.json`; `python -S recover139.py extract` authenticates/extracts sources only and explicitly makes no mathematical replay claim.

Observed evidence includes the initial independent full verification, two byte-identical full clean reconstructions, complete regeneration of all 33 shared coefficient vectors from their compact source plans, and the capsule's authenticated extraction/frozen-check route. The final exact checkpoint is:

| File | Bytes | SHA-256 |
|---|---:|---|
| `recover139.py` | 19207 | `2c74275f2c936d60be3a11d1c49cf1fcfd82015e62a590503ee6a4db45ed064a` |
| `build139.py` | 12235 | `9c4c0fbc877fe938b7caf9c1244f8e9d3594818188d11d1a6880378623166286` |
| `verify139.py` | 10039 | `26c6395546ec80c67fd85e582f76f7285462213f5f2009ccbdf982ced3f3a599` |
| `type139_plan.json` | 27298 | `da2a3e5d1f5d954d03bae824b08a965688fa2102a86dfac37f7ed9b15d5570de` |
| `type139_exact.json` | 9831236 | `1b6cbba383c9421c47d6c723603bf3b6a29ee3b13775eec3d69367e53c478d3f` |
| `type139_verification.json` | 1038 | `7f89e524b0bf4952edee0d784e22e87e5331ca9cba0404bb4629446413499bdf` |

The decoded source/input JSON has **52,775 bytes**, SHA-256 `98f918281f28abddaf27b2f9e31ecc5236456e97d9d6b9abc895e624983083ae`. Its whitespace-free base85 payload has **16,354 bytes**, SHA-256 `ad72cf9510826fa3ed6af1d6b8605d63ecae1f18066db3a6012968e5262733fe`.

The independent verifier's complete scalar-matrix stream has SHA-256 `2da16293c70f19c6d43fab9cbc1f18797879a328b2838565da0c6696c0f90133`; its corresponding leading-minor stream has SHA-256 `22507169b12c9093056c4385e70e6ee340d2a21ae86d5c20d1bbeba0b1712638`. Both streams have an explicit reconstruction recipe in the verifier, including labels and ordering.

Expected terminal markers include:

```text
DETERMINISTIC_ALL_ROOT_CERTIFICATE_RECOVERY_PASS 12183 104736
ORDINARY_PER_FAN_AND_SHARED_PHYSICAL_SECOND_MOMENT_PD_PASS 12150 33
EXACT_ROOT_TREE_AND_UNIT_PD_PASS 0 2703 25760
EXACT_ROOT_TREE_AND_UNIT_PD_PASS 2 2703 17635
EXACT_ROOT_TREE_AND_UNIT_PD_PASS 3 1358 13375
EXACT_ROOT_TREE_AND_UNIT_PD_PASS 5 2703 26513
EXACT_ROOT_TREE_AND_UNIT_PD_PASS 6 1358 8406
EXACT_ROOT_TREE_AND_UNIT_PD_PASS 8 1358 13047
CANONICAL139_ACTUAL_FACETS_AUTOMORPHISMS_AND_ALL_45_JOINT_ROOTS_PASS
INDEPENDENT_SCALAR_POLYNOMIAL_BAREISS_AND_FRACTION_LDL_PASS 104736 942624
ALL_TRUE_EDGE_WEAK_ESCAPE_TREES_COVERED 12183 REMAINING 0
WHOLE_CANONICAL139_ACTUAL_U_GE_2_ALL_SHAPES_ALL_SPD_METRICS_PASS
NO_C34_V10_F10_OR_ATTAINER_ASSERTION
TYPE139_COMPLETE_SOURCE_AND_CERTIFICATE_RECOVERY_PASS
```

## 6. Unresolved complement and useful continuation

Within canonical139 the unresolved set is empty. At the whole-catalogue level, after the previously accepted closures explicitly named in the assignment and this result, the types not wholly excluded are

```python
unresolved_whole_type_ids = [i for i in range(296)
                             if i not in (139,192,294,295)]
```

namely **292 types**, retaining the existing individual53/U3 and72/U4 root exclusions and any already recorded proper-subdomain/tree certificates. This does not assert that any surviving domain is physically feasible. No new whole or root closure outside139 is claimed; no global lower-bound change follows from eliminating this one type. There is no physical counterexample in this handoff.

The remaining uncertainty is outside the stated theorem, together with the ordinary implementation-review caveat of a computer-assisted proof: this is not a proof-assistant formalization or an external peer review. Floating-point generation is not the proof; the regenerated integer coefficients, complete combinatorial coverage, and exact independent checks are the proof-bearing objects. Byte-identical numerical reconstruction is tied to the documented environment, while checking a frozen certificate is standard-library exact arithmetic.

The useful continuation is to port the same full-tree, actual-cell/common-covariance test to a genuinely different remaining face lattice, preserving physical tetrahedron identification across fans. Use the complete three-cofacial-apex degree-five gate when lower-moment certificates fail, but do not reinterpret such failure as feasibility or silently contract cap excursions. The 33 compact shared plans and the root6/836 example provide fully reconstructible tests for that extension.

Supplementary copies: [Markdown handoff](sandbox:/mnt/data/type139_handoff/NOVA24_C32_TYPE139_WHOLE_ACTUAL_U_GE_2_V1.md), [recovery source](sandbox:/mnt/data/type139_handoff/recover139.py), [exact coefficient checkpoint](sandbox:/mnt/data/type139_handoff/type139_exact.json), and [verification report](sandbox:/mnt/data/type139_handoff/type139_verification.json). The full executable recovery follows.

## 7. Complete inline recovery capsule

```python
"""NOVA24_C32_TYPE139_WHOLE_ACTUAL_U_GE_2_V1 complete recovery.
Save as recover139.py, UTF-8/LF/final LF; work in an empty directory.
Default: python -S recover139.py
Frozen-certificate exact check: python -S recover139.py check
Source extraction only: python -S recover139.py extract
Numerical generation requires CPython 3.13.5, numpy==2.3.5,
scipy==1.17.0, Linux x86_64, OpenBLAS 0.3.30 (SkylakeX).
One BLAS thread and four fork workers are fixed in the source.
The frozen verifier and this decoder use only the standard library.
"""
import base64,hashlib,json,os,subprocess,sys,zlib
from pathlib import Path
assert __debug__
B=r"""
c-rlKYjfL1vgr5wE4V(jMS_A9ydPwcy0T5Ly_O}fq$InCVxd3+q##isML@FTl>htfo&mrCFzs~`@0VMf#1hcm)6?(i86d`QFXj*F
I@V49X#4zP^x}&B`)YHyT_;7-i{Z!aF3r-sNEf|N*PC_Hdu1BEMU-u_bP=r&i|1_uqkD^FSENe-!KhV|CA+BD?2fLoS0A5?>rK`(
k970MR(q!pcORd7#u2-@Sfp^HAL;IqHtwCI*~3%s$#X)-f{|z2Bzt*se9_Z@*wlK1i`(aQbesHBQG1&#=`mb!y-T84?JYMCJNU7?
?R|nD$u0*5$Ln=32lyiSA<ecAMQ{FGBzZ5|CB6J%yIrSA3?N{U^mfT&^O)?OL9uQAuufp~`9n79ZMpD*je6q>czDr+A?fnDM3j~Y
lc#7=9Npxb>?-5tyvowM?Pgc>Hu+TsLiTQx=U$ri2K}>-lT*|qJpK7Yc=`5xa{T(DulCPAd~88Jygz9`l+h+XO0vgvx5=i!ZWi?Q
em&21lwYsYxtfCaip^%7t0<0o_pmO~?QXM3@;uE}YW|$7pQ2p`*C^O-bJtt$K=^c%<-L;Cn-b8A^4^=0Xd4yCz9RVuxAoN7!yVWH
h_h`C%NObPxg5)`kJf1xtydL;e6xN`uCgf4LEK&##>xC)6^6Yii+dpB5tum#5yBLVHyxR?AQ+gcZmPCY56ZSjVOY_HLC|Lr*5@qP
lua~`Ij~rz|IspCgSD#LK|ft(n_bd}DNc_+OoIOD*)PY26+-lfm;d@WK~Mks_UvR59>2Q$`S>LKIsDrsG{Rrd4IhusC#RP|Kgw5O
9R8ZE&;Raj-<vnT`q`mw-(}I;=M2f-27S$qBg2Uk(~Vrsb(T?LnWk$dPO^x#g=fzrZEo4i<vcNMKZ#9m4rB|<F*MJNV{ZX$UICkA
IoGwwa%?y9e0>4Ix^$L~5zl=~cdU7A%}q_S6JPV<g>6Ss;<+*K)qGQ1x|$UOn>QE1bgHSkYR**nZK#&2vnx||R0FPbfH(|msJ7~<
u4>KHtE>nA0K`#kz*qov;I|F;9{hIT-kZ&?vdKk|gRhf#@LTZ!#br?5C5nO>vBZ3MbAc(`OYr)0x*aUl<y0Td4wloAK2yGcE6&f(
E<sF`4&2Y?0R7K?K1HbEYNpD5=%(!nSNH=(_~*yTtINsjVCs9OZkUeR*XPb+K95Y#T=<ruFDy597A~MPbG|g^PGtB=V$OBbb?qcs
n6cxVj+@vfP<pYs>;v16C&#DZ$9JbFfZ=;;uMZxL%*2lMr5*dW6$3LcxM9sTFY+DR@w{bZ=$a9EPP~j3rn_{L*q`fmY}>9DC&)EU
mc1lfY+|s{Mj7pr;$a6B1M~POh8)WW8x>6$Lh|Rq<?bO-^JE*bvYQ73C>d&h)K`>){?%31SB^NZfx<b*=_<*K!MtWXT_+jbs%7Ok
%C95Cb^vm8ojjG)3W&9fJ_VTXgML-+w(BTk)ea`XS{$+}J5a`DW|o6tpb`X?t*)}y$Ct+e(`LPi;+)~DA&8sy%XIBSx*Oce7Xim?
b}`hC-E#<w5NH!YSz}`4Xt;~FkbJL$-v*0mf4A8b{h10^DG)yOXUb^7LTrH{#+iYpyCkm0f2k`98iY*>V(Xe?vQmOTJ^?^Y6AC;t
=Q7F$k(w(b$cD{B5llgjo)Fdu@1@ILgtyDlVv`lH)+GqN3G%-p*QGLE2FvLU5BD2nfUJ&^ry|MX0kB_AwHf@lWj_ueA=nJJ$Z{8D
t7M?7oYA4KfSY@zXMss2X7o^O?l!yab(-IShfu0GSq0Pl;ck#3pJbnZlMBv2-ShV`0HFBqiX19M+C`&^z;K#^%i<Zs$A~XeJx_`O
pcTfZVW!3PCWS=_Y3n8H2o|dNVNnc*0|5rz$U_ma6>6~M5^ixAlS*MK^;W?;Wf8}vLR)Y`^}ebsj9e|J<)gSd>P=0e-YX-f%T4LM
X5ktjPF+oJW{RSSgC`eXf&g^|6OPb@(RPb2TnSDoc>q?aoU@Gw5tAeercD03XgheL?n>r6WF1uoyA{pO#E*jrLIeIQg^hm<v?{sZ
MC&}MtRQ#{qDb`x?Qiy|6cG_9hX#n?2V7Ra583bA*^uFHXFtSy#jp@n8s*P-5VrdoGk`@JG){I5dQjiZ)ksl(Fsfne4K|VJq9iL+
NUdB=wt1i@hpu`TJ+U!?ZZNsC07IUWD&u2zha;5nBmn-&b27-3@w@#sj)6J|0o;k-OaZfTR-oTsf)q^&%L=M7L0{vK!^yNJnJF~~
#&b5lV**^@EbkiwZv@(EwvNR!Wj2l(hxf|(Ho&aJ7ytmX0t@799UKp{@j6G9qLS5G&DICE!#ic10i0cqPlGH!7#u?_7{&+s`0gP%
J=B506At{G>^Aw}R2e@_*ZC~ae;BaQPt&`HS#YS2Up9zdav~Uf7h&qp#`6?^7HRwxXk|o3YQge1fd&wp|AhNtRE1rE$Rg*#_9>X~
7%!CB5$dTa<Mc^P+h~}ngXjRH&tMG`5TG8;JG?`k2Y87@cRb5`C*10Z`bpVWvf04}ll6e<zzgw@V3|=0Adz)`5DjA$?Z#$~6=i&K
5WHuD5=bE~d^=Up#u8RHC94~O)%5TmZ1g{H^m~@7y?I&{2<FjU^gIA&=m{8u2JfIx4yK3iW=vzu7uba@22W}cJ*d~v*t1?hsa71=
yA7C=6`>xS!uE;zB{+PV9_q707&`>^>&>bpW=>H`9>|rezG}q93ddr&tXO~`mmk=0M*DV8J2+KOL7BIJQ<1VJ91e}TEIp|wRq36l
Dk@%9rhl;PO*0g!AE{A#bNEww(^sFS>C;R-;f^nM&!clB<U5O_1#VUI+vmYQI6iq=BwMykC<$P*dAwdtcDv24ZI<5hFffLKP2g9Y
MytWOA{eG=nclC$<ZM4P_=oyV8UK1BN}t}S(ar7QPf>c?SAVT!@2yai!=Rk8fE`yd`1M4Mp3+<oboSc_jFR~66ll_?5TZm)pOo1_
HLf-h%rd`8VU{^easvOckyR01sw?%aQVP$)y0<KII4$;3T~%7{1ehW?((K`p?hS`&Q8`V>0#_^Dg$w&WBx_RvxR>V4#$9`(NC8lc
|5pqeSe@Vx1kV3XN2luObQZjYOMdl|1M!Nn*j=-VxC^I;D^)*y`G22gbzE!%?vVdgfl7t;4k}a_1%0R#edqy_#cjAuGiWjbwood-
cqRtTg#Ch+132xSyv~dKzT~-sjxNR(O1Bi~(rN~Ave*TOtN**Ltbl+YF(=t-hK@VZG$<c)=$vmEQM3;9qj8o6TTGB2wQ6LR9YxtQ
G;KhD45GDq<ooD%ygOv+G|jTv58LXhEQ#o+aPKFl@>B2WDR?@F*2C?1xhy@#s|dFOCxV%mOLSbeDVW1p8@ycp7%UGkAYl9e^b<7z
6^6l)y|0?3yPp^YCVeXF3adRo!P?%#^#N=Ft5C+)u^$0gbKDOvyV&)**d?&V!0x_oxv}9=#*58ERs`BOf+lLkR9~U$$3I`<gsUkI
f##I`DuX_WSMAPovALUrlX;gpxllcBvM9cRzIP^Xi^UF*u^a(8EdEvXzJc8h0B&kP$}GGM&<I0+ye(zJpW|W^Z-Qwh<$gkhx7sy6
%c%C&7N+=78{w}YWsLR`ly=7s0};w!0>7~rVb+6Ha=h8i)3QC^8!?LbEcd0z`=+_kjNVVNF`fmh=@x(Unt=Q&Id~U+&%=}T$8kKs
AZApGyh~P@Y*h$Ahq1yv+io*oCwI`QFQG?#g2EZ@l68P#T6Ty2xF<G(y?4O`yt{=w8u!X>G5_~H;n&+iStt018^9}Uk^*7F)Yx+r
!ePlW-}hBZD3V1H{8o%g4b-C9i@{?01>?OC>gzGvF5<39se8C(tA%SfaLduMm_n;pOxtqJc!&5uz1`+hzJ(R6w}I9K8s*(4jeE)c
15YOiVel^O>tNM^B<?*%yEFnP<|qPnK6t+aY^d&b>UJC4?*_}_=u+LLj~j^G6+ip91G5MH1fqF!moECscy}w*YUn0*uw;UrZwI@b
!Yu)sY`4?V?shh-g8{c=m?CvB32W9GM~tvtg5U59D9iG;4r+RC0<Pd4EH#i*Sq``~D{{^n=K(@)SV1X({b{XwC=2|l6$999P`VlR
7M4B!>JGx&?;t$BgQ%qa#!ZBWcV$=jO`C`^@(Q&`x*^L<wBIWv&D{d9I1y@8By{BE5{HWy3)fk@KW}U=SZ7`m4kg<MRyJGxJ?uh;
9^Zl>7mstfsDy!*ps7vmaTIDd?Mei;&dVJ`Uhf!s2SIO&)Wdtm_I|%__*2`4YDraJLO-sS?Y0UgSC@r~qSjk@emGWb$)Vm>dvQ<L
i(5>!7Pl}!@-eLURmDAJk@y5L26b83laG0bvX=k9dz%05Y5u#X`R|_Q|F1m_mbW!DT3_GS#PMSD$ck*cp5`h(`s4+*F46(QfNt^F
YD|Pe3pl)7Ji_(oeH;QDZSl`Cyq?%-HT$eG@n_?gFH6kJ8uOB2V9?8#?C|fyhyCjPppt8Mz4}a{1L6-E3Z=V&QpSG|>hs`Fu>2lW
_30C@*yZ8iJe@wwm`sgBLFh_U_;Y}IDF@T?lEo{lRS?R!fMqD#^e(S>sC(%a02}^&|7-|GD=Mcv)JM?ZBQH>0vgkrGfA~<rPlV<5
pXy8IK^Uff_@HukU1hKt4O&lP>W5B<E06!{#~1kERZ}h1R1JK%ijQ8=5j<$Xs>v$Zg{&7`;HEfPFx%ti5n93eA=r4!@A&C8+<)fx
pW!m!CJTPIEFYr5?gCn(@~IZz8n8VwQqIQp&S}j113vaP&0>65S3Xhe^LCft@PeDm9|4oQnlJp(O@U9FAbJ?EIrM=KeJII=gXWpQ
l6P>>hez20w|N6hdbMbfSKYiw7L_!zebHXZeUn{}Wo@)SJU;M-nCZe3#m`ExKbRj_&fY|P*|PARhH5~xUJvjw>)=sI(fkFo%_D0m
6jrpbPJW)kOrs1soS)cf{Cn12N3hk)%lr&mht+6~_xP|McJXZj@ie3JkV*QK=zaNg=zaOL=<_s!hIL?|YH1MMaK&^5L@H0<-`CCQ
`)cc1q$)Fa!_0eomeu6zMWigjLd5mThnr9r=d)>%&W32L`9aE}V=nF(2!6fmob3(x@Up<-Wt#!ml@C}f*pr*b;WhV`dR?`EXqeGV
z2;AHc(|<slqed(p96n3#@SHEC<x}tVR?nTWz&seDz=v1gD>&WW%vnPaDa~_;VPXSpd8o3(m%-IT76#$11tRdQV{&-z!)wT!@;MT
3$rwMPhqUuXBA)_`V?$^r>1+Ic^VYyh+hnf6#Ac;Dtms60rMArI9JBoO@PNM<9k#A6oM9ZeaG)^pt)q%Ea>nW2Rx_AI_}+9)v<i7
Yfwb_ZCw?i!&J8cf_Q}*lt7F<{%oJkz1Rl)Zd&4J)$0ko0xh=tVhTyk+99H9A}KawX|xV`g=MzF<vb`?eaVRytSe8!w{F1L`6L(b
sngo<ri6_d^iR)1u2*<+_UicZ>^yumIlp}O<{jKj`f6niUa+fH11Dy!1v@u6igH$#AV!p<V#AgzWn7*;NRiAqX;sIW{aCL5;cA{I
>tq3Af@#;d(`9<Z-uD2{e&T@&7i=&;Pc02q^9Ybfbr;raU`2<Df#?s1k7c*>SVcFmRe4EhO~cv?E+}-NNdT@IMDu*GTyLTR%DGY(
a^8C}1AVTP;Y<25S`?dIe>U809-vfKLw{f#hq^W#A~i#%*(%&_J|#fi<~-y3q(u;?i(<gL0_I{gP=KkxVwksATSdiHyk5fDbLXJ4
jQTnFtW@hH(+&Fu_KwWaDk%nevEyg*2Yt1FfOil_>Xhe?R`yWP$d$3Ik`0FJdB6URA@1@J|F^OI`}{(>!23S-uHI;>EDlzvtX)3R
DA!4L0z@`_m3_AHU^;y~tZO){-aKrDBdIDmQnifRJ?<V_a%RZO@aNNam*L0PP3u)p3iiz|h|oHtkDxbUQemmh_qzqg=TnpwRTi<A
`c(cFA6H|$Rf|mlyTazPp1J@tT!1h5)o*2Ow@`$UE8p6~jP<Kib<tPKLz!(;Ss1D`yEHZ)-}^Fj&ji$`w7BlI-k!yf5Ao><Of%@?
tH*ui=;LOy9#~40_qK2ayTlv@mA(eRQHn2gl&g};XW<)$1w;VYsC+w3&DgTYM$g6|=p0f2SM#ik7ep@!16{LR(?N5`!Eejm=5vza
qlBeWKOSiHvu`fg<AIx9-JoM*Iao~}XX-MZ?pa`$Q7_wXE~ZN;e2Vy(ZJ!R+qFz_-3h<?6?3*1}+QPl{h9^z=;$NVvX$+~77S92`
f?H-z2t(6Vc85vC-?Oa{{GG+%<69L9Otjvt9+C?7>aALJIz9HHc9_P2Zu*dJiv;#1Z!T2!(5~EjCBpIV#Y}DN)&kH{V0N>CEDJHj
!d<cjmw+Tukv`VEgl)#nZpN}G#F!3Qw&Veidx7IRnkVZuEJS-M7V2tw-p?W2*Q)T^eIAryg!Y{W`<F*sZ(`2D+|{eFY7K)i&G$O@
udzd1f7+!*Qoh;AXtz5oF8$Y&%gOnNcc<?zF5kThk55iQOlGm_hUb%4XTMC&{}p~bzPRYC{DA_OQ{_qs{Lao_zdJof;>mgV=J+%`
K7C!aD<9wf>jGGwgcraOz#q;&fb*d=m7F12ZA~>zf!+D!<JtLTUmezJ0uoxjFwCO6guMtJhFGY=us`Aj>neMpzUaK$`eO9rx2qTA
d#6_~Mu65-T{BI%X0K7tW@-ttyCA0v@=B1#-n7>C2%kV$UWbXT5wy16r8Nm!$LP?yT^0O}qPnJcK@uvf3v%S5z{CVX?@pyVU64l&
_dB$PPS6@gm$s{wVNt`qE^T*qQ*@jm3^yyWj6KL8rmAC4pzRvF8+*E?bwMT}kX40(S%d8E@NT^6b-W1!t&YG>cc9a?w$oM1p<>9P
V#w`I<(d?2cS4t%P?8ybceqasH}uYML$|shYPjK2h)y6HCQ&X-trPQRH<L}xCWd!Y#_XnyX;8yWheEg=CRBAaZNd(wTiL;?K^`TE
--&FiYX_@a(JZQ>S$e0ETHV5BQH9H*%8X@n`BIVKHma&2B8X|-ZaTYm#}00Hm2f?$3+hxquVF1gAkPp5vIT@`5hE<Zm7e8L2$w>5
6oQC3k6L~`Tc;32E%&IZ<vG;kE;YGJP3}^YQ)SR|Eeb)IovM<aODX75W_KygJxX(r(%hpo_bAOhN^`1qcpjy>M``X+ntPPyKBc)&
Y3>u6`*l$;_8?+fU)LyvP9dmib(2C^6vCzu4uv2L?i)^fDew)CqNR*MEuy|j8KYY|eW$a~_->b~+lBbun(Mn=t?FbGKwcN*cR+P&
2_Q->Dye)bseCG_d@8AYuhRkezTO2<lGLr)ULBv3!MD4#RD}6dg!xoB`SNfwG_BpH8JeMYK$hMT4nRhi%It!y?m)W>a=IXw5ZLm%
w3Kqh0%>T(0tpC%Ksa5aI9&@kT?;r}3pia1I9&@kZWq+m-Jx`MDcxO4cbC%L?Z$}fcR-!o1yDC^>Z}z&CNVFOuYj;Aggj#mqf-M7
!<T?MTA4(-1%yr^2z5+i%LoXULJ-b1Dd(D$b4|**rb~(IQ>=V)ghe3;e_4%F5JNyT&I4=_VG#&hBUstg9F1HT5H@ibVc3o>pWJqd
Ih@Y+&2V(B12Vc)onsT%lKb4XbOLS=aFc*r1YEwRxI_(gi4y8{mKCpaMBq7c9X&@U;KW>xNx&@vF4vLT%TQYx-)PrB-!M85vjb^2
Rr^k{&A)B2eLJ{^SRF`vCGpL6q4O<y1p9RqnKi`hK;%~S8<8XO^jp2ZU&m6-vyP&ghO#+Pz<gr!=o5QKpV&J3#CDHrGv!^Tu|GgJ
7(x>e<zm`F=;cwq1mRE!mqHMe>lQURHFsHPB?z5D7;=Q+>lDJG5QKi!IxRuy6vChoCWWvlgiRqF3PI{2`pFa#K7p__3ZWAS${(gp
X>L=R+mz-urMWF?u8RmtbK56II2wTvr*QXhi%?G#)f2#Vgy=O$B((%m*Xoe^a?)zID3DhB#68H+<SsHalYrX<+#%pD0r#XPH8gpZ
Fm%1GxS?Be^BcNvN=;%Ijap+02tyR#77>IzhD9iBI36)MVF|;v2m~>;DUU{g>vDS#mB}z01{6d!9eE8fOiv@G@J#s#OOw}2XvqyZ
E6b3tAkZ!oBkV@L=_10SSP@}tJ0^v&h{+vW9y+$;P^?@EL22Ibhd2k30k%t6z1l!XI2qIklN#Yt2uckSP6Vh;WPn3x=QxDF9goOw
$0yXLbZE3tg2fw&AxuE2<`MIHMErRc!Ji0ZN@0(PJ<pTVH|!(A2|0av&{Ji=YSb)UfExt8eBNq<--XL-hGod3x_S`V<zo|YLSMrr
_<IDsJi{%b-Ly=dptlJ)A*U%%G24*azgbcD{B5FHw~1ceF{CSxLzvki%<K@0szaFBAr=IOSPvXxm3J)pyp1f~uY#T@7pHmv)`9yP
0he3TC%P<O^9Z<n-s%BZ2X0G~$d@(JrdqumWj45&`&YiY2#bK*1l%FuE&=xlI3Z7IhAvzu;06IF451VH>V&>Jp|4Kpt9ulj63C+@
@+gr!N+!alhDN~+3Sm+Ri$V~>8id~rYHDg`lVW6&oG4b54wMRnxh;afMew%>{uafb2r-KYF^h1&O}O7CENT-5wF!M~LSLKE%OULG
Q1pZy9KsF`VF#D6gG<=KCG6l5cJK-QKEdB7`1=%p!p=TnPoJ=-PuSBZ?CHzxX=oY&m+NZ~<%!B{!}JI^!N(%xu?YT_LBLG{ZV_;s
fXnS~5cz1x-C__{AdJumLS2CC1l%CtCIPnyxF?01a$QYLC&=aE5Fuj9El&gv5jSR?4|)ypTM(;`^*ux`sinycXVr~L%|W*aO1nep
$|;?;<W^l1Yltfk2+Qk?^*UpTV6qAC*;-piTa)W(J8gSbr#~X3${(wOczT=06J2fB{GCSIA;3+m#lbP{4n)jbR~Xy2m}9rOxmp*}
jwP3<N3JE0DAzIxxJAHi0`AM<HZiX)pVu?m8hKVbay(n>K=clT;NR#cj6J*)Azq`C5GkDwrMx^<FM#eTeckIoIy8nn{(ZAE*6fV6
h_MYXSOUDQwQtM(YpdnX$u0>Ipj99-(h#AO2%SP$1i~jq=xu4Ly=j-SEO-)xFCa_-VNfH=-0dRD5bYuyjY5bTTLQwRMtGDde6wwg
>S0TVwt5^QLAVscqY%^_q9Y6uu2BeGZi{O3B^hB-b6XU`rVuVQxkpV-DQ*!1EKMG0hDC7_h1ErPCkqW*?}CgD$gv6894a6@LS~OL
q;F6N%2__iiW15vg3;7S1Yu%RC&ab72DK=8Y-(ED&?tl@x2tVZBdm@*w%y5iTa?fhMmxUT@wP|l<ac7s_PZkZE;XDmxI=lu(L35W
^?I-eQ5JO!!jVp0t!pN((V5EaLM$TtT+5*lo*Yr<O3l3bA2~YGdcH*=h#2#!h0UjGxla{Zzb-_zpgtw2PY6o*r`oT#1KwzM36_8$
#IN5DZ^v@|j(B&3)7A@CMwejXdlW(*xJElE@B>M5UG+wCy8^-@bk*&S<hpAU+&zK^QIU=I@?ca4uU$$*?jyq>oYz?V8*oBV!zP?+
*z!tgR8ML}`3VoTa~oO^!u!nyq=E1Wgig$<6G32FL=aRjG>LL{1K0Ej_gfm_=Ia0H>`Z8B@}36}@<L`<gtC@yQV5$s7!<-LWU`6y
Zd7A&fYXU@%Q3qkB4#X?($$mqP|%dQa;w>tIqgR66A^?fZ6ZHyTbH}owry&JLm^xWL0HOm+MPoEY7D1!L|RYot$n{xGjXVL?pQX3
a3}<!ltY=pafmE+9C8E^ppNTxR3ofFG-F1m7c&|gVj&2Le#{^iFRCv#JI$Ec>BUTWkeWmXU=j_Q+3C+rTb?gwBLW4uyaJexE+uak
N>_l(t=}w@B3$lpi#YeNI;R!Yk!w3mtj3YVUL&iq-xV}!Y<EStyi>JYS8f5~Y{4R$K+7`;xJ|&@uC^MziC_U=elB9mC$!tKY1<t@
do{4zve?9ti%qNq)f;tPI3Xlq#pV`l?+u&i+iarqb~FlZ6L5!s%j4bA33{RlbPS4Ko;Qw3zzO?1g#8`D{?)71UATNfcU*^ny9At)
UtVJ!Pb1*+ZrkzXEwbYgdJ&x>aTMTCVMQFzIK*j)Lo7iKv9WS|d9iclr)91tKR$Fdd6c+BTkH}C#ja)(;yA>-F2P5>#=AN}Z^&14
msmDk;;h*v4ijCQun*B|x<s$(IuzU{;Bq+$sN)iFf}W_^9#JzqqBeN0O~4%jPRS#;zDKOAo=?FI0xp-c-8}n558@M#UVLH$=M#;y
Peh+@$%~8MUXOj75ReE{pIG^QSDrRLu{iiH#fLB~Q5Aj45k&R#rN?&;zS77AbsBZf!6#X^98o@Za7tS`s!{4BK+2`XX*`*Bpxt*`
lvShOq3q0Jy1ty!6To}Ls#g)(;#d24r{OS!`*OG=s^ST7T~6<MQZX%`p!W>|ZW4SfDZQ=hQhM8Ho7`@25GZ}QfgOv0+j2gRBXvmi
*1%p6x8b_Ii>h}7+9t2w5pWty8p0hZAFp8&cMmt@rmg;RtPZ^;SJboZhDIPMyZ7pQy$h%yqW2J9hK<*-npZtx7C6Wt7BSZ7keVGx
8TZ}6jz%H65|q`eLu-gy=>puBo53W^W9lTrpb!p$FmwW8$>DZe+wz1;fcPzdVRit%)DVW%CbTqy&>-Lr0e9u_wl;<>cb(z12^&5Z
IJ%CUfh+fY^?xRH;ieq!>r(!vu1o1n-6Y_0i<m^5o4#DHw#O_}o_*E-Dbs}$d`(vxf0orwH_I|QkaoaTe~X9+kte!E=x;glJgH8s
y+#!VxJ%f9sBBil-y)pg;}Q1s<cVIr*C$xO?^x3BSkiCja&>y%p4Zmo_OyvoW$W^MunoB#Y{Qkq&9=<d|7<Ei971LyS8Y!t;1&V5
3Ao%BwnymFHg<I;)DAAEk?bN|uBby8)gg@PwDZR?b%M|!;HFe_ho}yYEw56JEsqk%kz3qpuSK=zYe3t^ZaXhrqJMA+<5oukUARfW
<twXe*mAhpk+2i<E@4;KY#YS2<gx8`YNl)11SMgIPK~V&Ekuadfpi?=bog{yEZ39wIj%34tv#!!$#wHIhk&~s4xUs3Pm}j@UZ?r>
h&c0fc_sA-&v}+hzzJJeZHs$0!NDdtIP%E$<XxTTx6R)cz?ZMBzC0m(Vrlh>rPXf)3#*o208xGtsrrler@vjjU>{e3YaLcX6>s;S
1Csm&Va*Th;4lF4Z%81uro!F}{?%33lc|<!;~4yG10XeaDSmMWfHn#xem$r?=NGjpqe;tX{xKPyKO>_llhOL_GP>VgM*F+^+WWII
N_=hW`gfEOI*tE`jK+7B@lVI2RL1X_Gv0qB9&O$Ft}=SxUq(lhNm%_Q1^Ty0sI%{oI`9X-M(Q=Hqw(z$;%w#G(6plC(jr>lW<(tf
2LqUhCKjJRCZZuOJA#OY>wX6-auHo7<af8CWqifa=I^nh{_P?<QW1s!->2zlL%viu|4xN}Bcs8B5!1y0X{|r%X^ocA{?0Nw-(5yi
`${-^zhB07`TiX;dbEt*ceSJYAMmv)U#kDG9lbv;BV|WJ_w_$rdQ4Us|6>K*FfIFQGHTx@<9AwQ2s_%2@g3~=JL}``TnG(QTEorX
vl5!DoiLdt+jca+T}G2w33bE$elohOKK>_UbZ8m1-!J2zwxcGK(fzJ6dia_6?=GYFon`#)c62;xd9;6D3D+PDu`{#b-=>K6?=3xE
M?_b%<Ra?d-kEU`^*=A7F5M*fmP1?7_;wL(wyU;Pvvr1I|M>zA#nJf=W;DN#r{!kEzfJi&*wF;pu%WP7gZtg>=v%am?jMoS`ExS5
-`wE-VHw>&YsapPo;)0#KO&;Ts&{jr;C#D??*0|<FUX<%m@YOYU)Z-z0gx`Ab<;oEKED{fxMKfK@MEvNPuH7ua#()+w8se3WH;`;
`uJR2Z?c|wq?<>!+RKY5i=$oKTc`6~w0rJtvi0-PRd)VRekz%Na2BS`N4+f{dw9_kXYO@BGkcX?UMIc9b+WikcD?j&yV(`^mG2(=
OmVu1*1h>dx{d*fAAMc`_hR?302=%pceLwmH|ytYa|bTSK^U&sRmK?s`5H}yGO5>5ehs3lX#rAhHtSr)`PKY6zsi=o&0TM~i#Ta1
M(<4t0L^-DN}_F4AeV{+zn*)Qm7m%T!#J5gtitdr!%r6n{nN8wjtwh(Wg6k-zdlY-^IzYdolL^xSC>B@pM*b$f189x_>11Z%J^4}
gMO5+!Z`djTc7{k-M%+(e)Y3M-M-7Bx6c`py$$-B8%Kr{C#D;@n(Hj1#4=6SOq^s9YYWewN7~%7m&<u#+I|w7-W<plmV+O8iDPd8
Y+eDIWI5Nh$Z~8q@_c;}>*mr~Iz~MAE#0x^u{Ad}%}#vHix;*XMTzIez*qB4Z3!z{3~b(91nm0-s>zmS?B#TJ#kx=STmg%N$?A~J
kKktISC6L#FB{Olxw!X)JcBG?VGP|Ceo}pMQGc1bc-XF!L3x)b`|nG?x#-njZN|@vFV*E#AI%Py(~&-7U!7(j8V{Ism}@u(=+C~t
98B3Kme~*dtIvfi{4uM(YQF!f@~Hgq`2b_*D1Nxx=7Wuja)r0aa~@po9uhTAAi*O@_dFQ%Rrq(*SCoVP)fIkJne)O=4kPFK6U7zd
DSj$>u2j)_#6M*XkfZD5sianF!5ZJF=HFe1f8t~nO!33v?1SA&Px!30Qh&$0`Y`v5kD0GG3;bUD^s(3Zn0LBFmea>s5X9_5;4xxL
XW$3I0jpGuHV*~=>O1_yK3jgh!LQY`FW6U^ceLGYVo2h_a3H{v-Q5FzMH?~@^u@7r9K|J5D&_E>E&sTBC7-g#uu<xwiUvMbEoBf{
RK%%zQxmHTWwf29v*2b=2f8<dZ?K(4Gj%(i&lDbpkviwL{qmOpjR8g;;TPi5>>=6nDNBU#VfL-~RrRG9(O-h*2i!%}o+B9gDB5oE
WB1$A0%Z)9k^+HJ1q%DB_+~dxi+q5~iyB3hHS#3M8XjZcL~r_QvALV4S?Qa}h3YlEF+J30Lw~%TBI{XzKgY!;-UJ-bbPo$H#7ewT
+LB4oLYK~XgtY-bt3CiynVqYDJ_XUi{P0oAV>|sc`%xR=ui%jhS{d?_((pXyBBGTb@JDE;ijGIbwu(IAyY}cYq*P!GzlZC9eagM^
(KcssqU<fcW%&e@g3jq(#6C^mvfc_wqo`#Zkafjv{TF6^!Z7!xrzB}0=KJV=x`N=G1*<6r>8v#u6Rc^8doc%5!=osU2Y28mPOV4-
6bb7Hg<b}HTIXnKQfwFok&<FO7OVr%ehi`?eRj!^c?+5UXv+%`bYKZjqEW-i5z9Y7N{n_B<bOpkB3c<g2Kak=gUbtEjBZ-ax!qe)
XWzVkR1S4zBxEY6_&9}L?Qwd`ejLCe)eNF&y&hD7RA3ZYj5Wr5k7sl%;+o~D;6<q-|5An_j{He$H~~PF?RhH|-bKX@>m)d4QTd_j
6t`&JvYG8&!=kfFvSjm+_wFB}7#6#9A$DS8Y}6hT)`2C<Wx7bA--Z6H?9P}J5T*f4H0|S6e>UFoJKh_^{bzpv87}i}vfy{v@%CpO
gRw|>sv-dm@WiUR!lFX|k*6YXQGN_e(t^x#tnwjgWjZ#j45MW*t>ToItD1T?K4#R*Wl76lSm09M!j_>At7o4B`wa;=tOx9xw3{6?
{?KQa)DWqhQi$F~vR>!%9;py|q~&rSLd!4WYMH`<4;C9RREvRDMv_(zt68vFX99O23(^d?2@5P-gVRlxs6~4mr%l#*G7^cSk}^^m
(}cDEQIViQ_rjN>Z<(p<;mQ~;c17S1kH?T?0lPc!hPNG0e+Hid#eroH2gi__2Ltx2wk?yZr%5vMr$A#yT(h{EvMENuYF5%_(A0q*
X}6jJ^ORR*p%@jZ%2aNsx>rbCT_LLiVIOk@2^&4Ei#Ub;34ABGlXZkpccG_YtqhEuvKp-3DC%AG#4ctB!J<+BI#GrHtRmh)E>mc9
rbRj%exCZn`2lZP=6n5)6|$wQ{S3@-bTooL2Y#z&HdmhR%Ea2UVpQp63|A4XNv)PIRo8b_8^=7MmM(%QDAG}NIVjQtU759~;k;Ae
y}nb%{0<jB^^ieY-KC&A7WXErd=>0%b_iFn-r{9D#L#ntC<x}tVR?njl$KmY6|D1rw_<nuoZ5DrCRKrIZ^V2B4vmT#s9PKa`o9l|
q(CQ%xif0@1&aU!2IxThq1*@(`zeHG#n)64!(pLx3HJ^avG=%Fh3<#(35kG398Vb5r(zBrK_4vat^`Y^L2v`jQaYR7KquKU7)HKC
G+t94|7rw*Hm=6r!w=keJpS;5u^;oCChNF&U#-$}a7&u!A*3{HEeH2%ew{9hppL-^+wD)&5ld0HLiz8zYh_f<8AN>2PB671r`}(6
qmHox7Y9rdPPN@7kAXgJcVD+exW*vH?F{}KiydDqHg)k&nmXveJboR%JU*YiySNBHygNNR@2j_JtVs7mu|n1u=(tq6&Iq~Ebsf~{
ARd<HJ7m9aXG13b&5ZOkjQT6HNuWt+N?(+&2!Qy9ACOw8|2Q_LI=AY~>T5wUeKUAuRR+UV88QOyWFF)D1qgyh;qjoB@w3O>S6Onx
IM)2S;nIz$**Jz^7~`%#cr(zIPIOSkY@0qpmso`v)|Zpg>_cN1!|zsTrD8oP9l&_hA$0QkB>ed9m$S=0)CYzV7tne`%@9oBVZd&x
@I(+S!Pw_!c*GO%Sg!`6S&*cCCLu<bECNr;02q{!Q0jWabggujE3Ev$1f(KlwTrgbAv<8**D#?adUJuhTb5{eJHcDsDG!oh*~}Zw
$E(c)>;ZNIRwCPnaKc$i^BAt#Pq7mt<b3oPtsh{!fxDdF^e+t}KDB)A8#Psg`50+)3jeUw<)Bv4kk%qobObxvO4bRqzh622sKQje
Z9DN7wy&?N<{>{CWBi~+#bcJ=upRqF`GO7W;+CIcu@eGf6=Y<@N?4yeN$}PB^o@rle5;EGCMn5_nfezNCpRTqeq_PVMPS9fQMg)F
F5I-+nacfOh~SsfUs2FH!)&fs&=^gdXMOBlb=6|;in#1iqc>|Va@BqaZH=dv!m)|cIorft9y=i}!y|4Uy^YF-zP&4fkSgQ#W*3MP
vKiH7Jl%6yiHq!;i|KNv@K&f2s$=txly#=<#qK2X%?=L>>;@c!gT2*G<$I_da$w5#Dux4LmxAa49+TS&HZOzf?KN9<>(kx;>Ai!h
g6@S)dXF6#JRRcUA|wu^3l_z4172Jwy>&E)Js)IKzKyah%~qUrfr)&?8Lp!(tS7`_b=hL^mYFSK&7)W>LW;s^MI*K<uGd+Tyh<P5
tw>9Q+g*r2*k-d*t}S2fHoSk+ZAfXVeuGUg#CdtwQC`7fP|EUcoyWN5K(-jdB2onvjKR(w{xlCT*%A{)>dmfNWbPseok|CML>AzK
u|fWvA4R*><5ZuOr>PZ0`AKJ9?RTFD_N%kP=u?2Kj&?~Dhx6wGSBmi_U{7Awn<&Oo{7I=?v42Jr1ORVnvYGZ%4A``I#-kN{IL8Xv
raEp4fiPWVckJXT2>7$O772e6!_aTr+!s+1tv9QOM4)>0wqk%fhABJM!AGnmw0uU(pj9yhlLpNNyFC*gJQg_)f<?FF)Tp3{ilPd|
PSO#?t7xJK={0Nf#xshLJt<%r%Es{rWfi+Bp#`dbBRKZVZZ?pwA!E5qAi{F6A*`T}qBz3g(9NzAr+{$fg@sRmw|UTd9;S?A35?IS
`LsVaze|eiO)T$WlyLzWn5RXlZlfb*4@nrjYH3*ERJlDGrC}S$p013A(!AX&*vbI2{jltgX<APGRr!K;fq7E5&E*ItXcdrMvIsCR
@rnF0h4@6f<Bq?*;TOC%5RPM2cFkUOfE!+R8|Smwv~guo9BQdA*jX~Pcbu(Sa#SleDnIX3`N6K*|J?u5I#poynF>dvvyS+<b^-UQ
*<sJ4Wd*e~=Rpu<&x5o{jscD(vIcavC6XTPK2`6Vj*y+C%S7SZwV=JFucM~K2c7+$<h0{1KYG~4ID1tCr<Gq&K=2eK%hyOa@0lXw
EhHk?eT-4tuz#I$RoBNEmr<`Gy;}Nkf1*9BLFIw?OgzwQW@VFaiIcmWwF!9YEOIL=K&3xts)&mp_7(lfKaXEshM42w<@sb19-qDr
e?EP88Gd{nemuUo=&N15mg|T7nmzJwb*)AD(50P!kO<i6lr;qEzJVVd6o)nnA11H}s2+SkJ%t7+;3vT4y2chYRhTYZrt2gq-x$D!
Qr%a_`bzz}#{=;ObdT7pNM&sL!v?m?Nz8?(a$yW0ScMlEnmj9-xJlFHyok186(vIL4VsaoR>hwgs=Sf1TW@k$)94jTx?D*ZJ!CLy
vwp+{vg~W>H5Hc^HA_B)?0qYS2M~~Os4#h{jAfTmH4mz!<&KASZp-_tx_jbpZ7tXiwb4XDp7ak7Su@dRJGQd_8kO<3+cw&(Aeal!
X8`$W2fN@BJ6EcnnPtqY<I}U#cdw35P=NA<rZ>m0CYKlC@z0lMAI{D{zI}J`;ew^o@ySVO+2P;M-ktI+yWm;XWclv&_2lCOegM%0
a6Uc{Kc1cZ>-6lyJ78X&{vp3N=P={Dvr~Sa!}7Bcjm_X}&VsUBp8q@vC$IlD34fg&zYixc+s6sZ{EP6_*)Nmx$?LufDc(Pyd^mo0
`tI~^eN}6+;cs%utWdtzh4Wmz1-=*j5-Q1u$>sUGS5n<i&%#%x75<`Y;T!mKb{-yIUc%H9xVX5OoTIj_A+Hen1}49p^wpt|>UeU+
C_oWTfP-t2IaYdzj4;fiyCe*QpdW_V!iQmh#9R5R?8TS=^Zx*38HK6
"""

def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
b=''.join(B.split()).encode('ascii')
assert pin(b)==[16354, 'ad72cf9510826fa3ed6af1d6b8605d63ecae1f18066db3a6012968e5262733fe']
raw=zlib.decompress(base64.b85decode(b))
assert pin(raw)==[52775, '98f918281f28abddaf27b2f9e31ecc5236456e97d9d6b9abc895e624983083ae']
S=json.loads(raw)
M={'build139.py': [12235, '9c4c0fbc877fe938b7caf9c1244f8e9d3594818188d11d1a6880378623166286'], 'verify139.py': [10039, '26c6395546ec80c67fd85e582f76f7285462213f5f2009ccbdf982ced3f3a599'], 'type139_plan.json': [27298, 'da2a3e5d1f5d954d03bae824b08a965688fa2102a86dfac37f7ed9b15d5570de']}
D={'type139_exact.json': [9831236, '1b6cbba383c9421c47d6c723603bf3b6a29ee3b13775eec3d69367e53c478d3f'], 'type139_verification.json': [1038, '7f89e524b0bf4952edee0d784e22e87e5331ca9cba0404bb4629446413499bdf']}
assert set(S)==set(M)
for name,text in S.items():
    b=text.encode('utf-8');assert pin(b)==M[name]
    Path(name).write_bytes(b)
mode=sys.argv[1]if len(sys.argv)>1 else'all'
assert mode in('all','check','extract')
def run(args,log):
    env=os.environ.copy()
    for key in('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):env[key]='1'
    r=subprocess.run([sys.executable]+args,capture_output=True,env=env)
    Path(log).write_bytes(r.stdout+r.stderr)
    sys.stdout.buffer.write(r.stdout);sys.stdout.buffer.flush()
    if r.returncode:
        sys.stderr.buffer.write(r.stderr);raise SystemExit(r.returncode)
if mode=='all':
    run(['build139.py'],'build139.log')
    assert pin(Path('type139_exact.json').read_bytes())==D['type139_exact.json']
if mode in('all','check'):
    assert pin(Path('type139_exact.json').read_bytes())==D['type139_exact.json']
    run(['-S','verify139.py','type139_exact.json'],'verify139.log')
    for name,want in D.items():assert pin(Path(name).read_bytes())==want
    for name,want in M.items():assert pin(Path(name).read_bytes())==want
    print('TYPE139_COMPLETE_SOURCE_AND_CERTIFICATE_RECOVERY_PASS')
else:print('TYPE139_SOURCES_AUTHENTICATED_NO_MATHEMATICAL_REPLAY')
```
