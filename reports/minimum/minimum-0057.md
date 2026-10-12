# minimum-0057

AI research report · 2026-09-11 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

**Nine additional genuine C34/V9 types are now physically excluded, and the new U≥2 bound is sharp for local type375.** The newly closed local types are **104,329,344,366,375,482,554,578,581**. Every realization of any of these literal face lattices, centered at its own ordinary uniform-volume centroid and equipped with any SPD metric, has at least two strict unstable vertices. The proof covers all **650 terminal-broom automorphism orbits**, or **1,300 labelled brooms**, using only their eight weak true-edge escape inequalities. It needs neither extra absent-shadow signs nor polar inequalities.

The complete new V9 register has **559 whole exclusions and74 remaining types**, with **6,000 remaining joint-root orbits,15,546 broom orbits and17,870 labelled brooms**. This round removes exactly **436** previously remaining joint roots. All20 inherited empty-broom root exclusions in retained types remain recorded. No V10/F9 claim is made; the global conclusion remains **C≥34**.

**Exact identity.** These are LOCAL IDs in the nine-vertex,17-edge,10-maximal-facet C34 slice, not canonical C32 IDs, maximal planar sphere IDs or rooted-tree ordinals. The immediate accepted checkpoint is `C34_V9_FOUR_GENUINE_FACET_TYPES_PHYSICAL_REMAINDER_V1`,391085 bytes, SHA-256 `1145cf687979cac9880e332fb64c0f92ecc63cf715142a2432f7fc93061290e7`. Its83 types,6436 roots and16196 brooms were used as inputs. The literal E17 catalogue remains1111066 bytes, SHA-256 `1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77`.

The assignment's immutable analytical parent remains `minimum-0050`, SHA-256 `025309e66437b608482d58fec0bf719c1586443afdb06f0f4576f4492dbed99b`. Its canonical C32:260 result supplies the inherited method and necessity context. There was no conflict with the literal parent incidences. Local104 has one pentagon and two quadrilaterals.

The complete literal maximal facet cycles used here are:

```python
FACETS = {
104:[[0,1,3],[0,2,4,1],[0,3,6,5,2],[1,4,3],[2,5,8,4],
     [3,4,7],[3,7,6],[4,6,7],[4,8,6],[5,6,8]],
329:[[0,1,3],[0,2,4,1],[0,3,7,2],[1,4,8,3],[2,5,4],
     [2,6,5],[2,7,6],[3,8,6,7],[4,5,6],[4,6,8]],
344:[[0,1,3],[0,2,5,4,1],[0,3,2],[1,4,3],[2,3,5],
     [3,4,6],[3,6,7,8,5],[4,5,8],[4,7,6],[4,8,7]],
366:[[0,1,3],[0,2,5,6,8,4,1],[0,3,2],[1,4,3],[2,3,5],
     [3,4,8],[3,6,5],[3,7,6],[3,8,7],[6,7,8]],
375:[[0,1,3],[0,2,5,4,1],[0,3,2],[1,4,8,3],[2,3,6,5],
     [3,7,6],[3,8,7],[4,5,7],[4,7,8],[5,6,7]],
482:[[0,1,3],[0,2,5,4,1],[0,3,7,2],[1,4,8,3],[2,6,5],
     [2,7,6],[3,6,7],[3,8,6],[4,5,6],[4,6,8]],
554:[[0,1,3],[0,2,1],[0,3,7,2],[1,2,4],[1,4,8,3],
     [2,5,8,4],[2,6,5],[2,7,6],[3,6,7],[3,8,5,6]],
578:[[0,1,3],[0,2,1],[0,3,2],[1,2,5,4],[1,4,7,3],
     [2,3,6],[2,6,8,5],[3,7,8,6],[4,5,8],[4,8,7]],
581:[[0,1,3],[0,2,1],[0,3,7,2],[1,2,5,4],[1,4,8,3],
     [2,6,5],[2,7,6],[3,6,7],[3,8,6],[4,5,6,8]]}
```

Every polygon remains a genuine maximal facet. Every escape edge comes from a polygon boundary; integration diagonals are never escapes.

| Local type | Broom orbits | Labelled brooms | Newly closed joint roots | Integer coefficients | PD blocks | Gap denominator D |
|---|---:|---:|---:|---:|---:|---:|
|104|94|188|48|23455|1788|8347450|
|329|66|132|51|12768|1068|76194|
|344|68|136|45|12936|1073|76226|
|366|62|124|48|11536|891|574606|
|375|74|148|48|19976|1520|768262|
|482|64|128|48|12080|998|77716|
|554|74|148|48|14997|1262|8428010|
|578|74|148|50|16144|1316|7087152|
|581|74|148|50|16240|1328|715816|
|**Total**|**650**|**1300**|**436**|**140132**|**11244**||

The final collection has614 two-fan,16 three-fan and20 nine-fan certificates. Every matrix was checked positive definite after subtracting the identity, by integer Bareiss leading minors and independent rational LDL. This verifies101196 positive leading minors in each arithmetic and505980 scalar quadratic identities. Independent permutation enumeration and DFS agree on all complete broom arrays and maximal-facet automorphism groups. Each of these nine types has two automorphisms.

**Continuous physical proof.** The inherited actual-V9 necessity theorem states that a body with exactly one strict unstable vertex admits, after relabelling, the weak true-edge terminal broom

\[
T=(0,0,1,2,3,4,5,6,0),
\]

with567 an actual maximal triangular facet. The authenticated analytical dependency is `minimum-0032`, SHA-256 `3c4347c3beb52ca549da23ff0b0eb42a85251a52c2a920bbf1deb68b4b73fe4d`, explicitly retained by the immutable parent and the journal's completed coordinator verification. This universal necessity is inherited; the new result is the continuous contradiction on every literal case of the nine types. The alternative obtained by exchanging broom labels1 and8 preserves the terminal triangle and is included in the complete enumeration.

Weak boundaries cause no tree gap. For distinct centered vertices and an SPD metric, a weak escape satisfies

\[
E_{ij}=x_i^TM(x_j-x_i)\ge0
\quad\Longrightarrow\quad
x_j^TMx_j-x_i^TMx_i=2E_{ij}+(x_j-x_i)^TM(x_j-x_i)>0.
\]

Thus selected weak escapes strictly increase squared norm and cannot form a directed cycle. A vertex that is not strictly unstable has a weak escape on an actual incident edge, because those edges generate its tangent cone. The inherited theorem reduces unique-U trees to the terminal brooms enumerated here. A maximal-norm vertex is strictly unstable, so excluding unique U proves U≥2.

Fix an ordered broom $o=(o_0,\ldots,o_8)$, with parents $p(o_j)=o_{j-1}$ for $1\le j\le7$ and $p(o_8)=o_0$. Let $X$ be its9×3 matrix of actual centered vertices and $G=XMX^T\succeq0$, with $G\ne0$. Define

\[
L_i=2e_ie_i^T-e_ie_{p(i)}^T-e_{p(i)}e_i^T,
\qquad \langle L_i,G\rangle=-2E_{i,p(i)}.
\]

Choose the recorded actual vertex apices. Rotate each literal polygon cycle by its recorded pivot, triangulate it cyclically from its first vertex, and cone every nonincident facet triangle to the selected apex. Each fan integrates the same actual convex body. For the sorted union of unordered tetrahedral cells $t=\{i,j,k,l\}$, use the one physical mass

\[
m_t=\frac{|\det(x_j-x_i,x_k-x_i,x_l-x_i)|}{6\operatorname{Vol}(P)}.
\]

Identical four-tuples have identical masses in every fan; no masses are independently fitted. With fan membership $f_{at}$, differences $h_{at}=f_{at}-f_{A-1,t}$, indicator $w_t=\sum_{i\in t}e_i$ and $J_t=w_tw_t^T+\operatorname{diag}(w_t)$, actual uniform integration gives

\[
\sum_t m_tf_{at}=1,\qquad
X^T\sum_t m_tf_{at}w_t=0,\qquad
X^T\left(\sum_t m_tf_{at}J_t\right)X=20\operatorname{Cov}(P).
\]

All three identities concern one ordinary volume measure. Each integer record supplies vectors $\gamma_a$, symmetric matrices $K_a$, scalars $\eta_a$ and nonnegative multipliers $\lambda_{ti}$. Set $\gamma_t=\sum_a f_{at}\gamma_a$ and

\[
Q_t=\gamma_tw_t^T+w_t\gamma_t^T+
\sum_{a<A-1}h_{at}K_a+
2\sum_{a<A-1}h_{at}\eta_aJ_t+
\sum_{i\ne o_0}\lambda_{ti}L_i.
\]

Every recovered block satisfies $Q_t-I_9\succ0$ exactly. Weighting by the actual shared masses cancels all free terms, yielding

\[
0<\operatorname{tr}(G)\sum_t m_t
<\sum_t m_t\langle Q_t,G\rangle
=-2\sum_t m_t\sum_{i\ne o_0}\lambda_{ti}E_{i,p(i)}.
\]

Eight weak nonnegative true-edge escapes make the right side nonpositive, a contradiction. This owns the full continuous geometry and arbitrary SPD metric; it does not infer physicality from Gram feasibility. If pole constraints are considered, their physical metric is the same pair's $M^{-1}$; no independent polar metric or geometry enters this proof.

For $C=\max_t\sum_i\lambda_{ti}$, the same identity proves

\[
\min_{i\ne o_0}E_{i,p(i)}<-
\frac{\operatorname{tr}(XMX^T)}{2C}.
\]

The table's D is twice the maximum C over the complete type. This estimate holds for every eligible broom in every actual body, without assuming the other seven escapes are nonnegative.

All unused-shadow zero walls are covered directly. The proof does not extend conclusions from isolated strict interiors. Zero integration masses are also allowed whenever the same fixed fans still integrate a positive-volume body and $G\ne0$; arbitrary limits with changed maximal-facet incidence or invalid fan chains are not silently included. These are unconditional U exclusions and therefore whole joint110 exclusions, not sign covers.

**What resolved the difficult cases.** Root/first-child fans close most cases. Alternative actual apices and integration pivots inside genuine polygons close many others. The decisive last heptagonal366 case, ordinal39, is

```python
order  = [4,1,0,2,5,6,8,7,3]
apices = [4,1,6]
pivots = [0,0,0,0,0,0,0,0,0,0]
```

It has20 cells and279 integers, reconstructed at power5. The apices are broom positions `[0,1,5]`: root, first long-arm child and first terminal-triangle vertex. All lie on the heptagon, so these three selected fans avoid integrating that incident heptagon. This is an economical reusable choice to try before nine fans. Exploratory extra-shadow, nonfan-triangulation and reduced-coordinate searches supplied no accepted object and are unnecessary for the final proof. Numerical non-success was never used as physical evidence.

An exact type366 control has vertices

```python
[[0,3,0],[-2,2,0],[2,2,0],[0,0,3],[-3,0,0],
 [3,0,0],[2,-2,0],[0,-2,1],[-2,-2,0]]
```

Its ordinary volume is70/3 and centroid is $(0,9/140,107/140)$. The embedded control verifies all ten maximal supporting facets,17 true edges, all63 apex/pivot fan integrations,71 shared tetrahedral masses, actual covariance, one exact reciprocal SPD pair, and all62 accepted certificates' actual normalization and moment cancellations. This is a realized control, not a unique-U attainer.

**Sharp actual result: minimum U=2 on local375.** Take Euclidean metric $M=M^{-1}=I_3$ and the following rational vertices with the literal375 facets above:

```text
0=(0,3/5,0)
1=(-3/50,3/10,0)
2=(3/50,3/10,0)
3=(0,0,6)
4=(-9/100,0,0)
5=(9/100,0,0)
6=(3/50,-3/10,4)
7=(0,-9/10,3)
8=(-3/50,-3/10,4)
```

The actual volume is369/1000 and ordinary volume centroid is $(0,-9/82,363/164)$. The strict unstable vertices are exactly0 and3. Their largest unequal-vertex shadows are respectively−873/4100 and−6237/820. Every other vertex has a strict positive true-edge escape:

| Source | Destination | Exact escape |
|---:|---:|---:|
|1|0|12231/102500|
|2|0|12231/102500|
|4|1|12393/410000|
|5|2|12393/410000|
|6|3|360031/102500|
|7|3|6759/4100|
|8|3|360031/102500|

The standalone standard-library verifier reconstructs the body, checks all maximal facets and strict polygon convexity, every vertex's extremality, all nine actual fan masses and common volume/centroid/second moment, all34 directed true-edge shadows and the entire9×9 vertex-shadow matrix. Together with the whole-domain lower bound, this proves the sharp minimum U=2 for local375. It is not a joint110 attainer; S and H are not claimed.

**Exact successor and recovery.** The remaining74 local IDs are

```python
[17,20,21,23,34,36,42,43,46,70,72,77,83,92,98,100,124,128,
149,152,158,160,166,174,180,181,212,214,216,217,218,222,225,
231,247,280,281,294,303,305,307,331,337,342,359,370,385,412,
454,461,492,495,511,527,536,538,562,563,566,569,586,587,588,
592,593,596,597,599,600,604,605,607,608,610]
```

Every retained map row, facet cycle, vertex label, automorphism count, ordered broom and root array is exactly the inherited parent row. The register contains the complete436 removed joint-root pairs and complete6000 remaining pairs. No failed numerical case or partial cut was removed from a retained type.

| Object | Bytes | SHA-256 |
|---|---:|---|
|`nine_type_certificates.json`|614331|`176256a0cac94125a9faa76b16021e9d88d43eb9968aa7806c341f090f05c9c5`|
|`nine_type_audit.json`|135656|`9972d08aa34c0512bbb6a6fb67de2f718bb2e22b72ae839ffda6c616ec3205b2`|
|`c34_physical_remainder_v2.json`|374971|`c807152b6d7237e0987b54b9cdc207aee8e731f7614dc885ef1e13d09384d954`|
|`type366_actual_fans.json`|20423|`b842e96b3a943607a1f55582eaa562f7dac8e0e754aa5b07a93731ab7c681573`|
|`type366_certificate_actual_body_check.json`|26516|`046932bb46fb8fe890a32594039e69dcc8d3635986480c1cb73b93d764397034`|
|`attainer375.json`|4006|`2aa06ddb67d9648067d86315b1c3cbe8d1d40ba34463c3917a50b69494f7df34`|

The successor identity is `C34_V9_NINE_FURTHER_GENUINE_FACET_TYPES_PHYSICAL_REMAINDER_V2`. It explicitly records `joint110_attainer_found=false` and the separate pinned sharp-U attainer for375.

The capsule below embeds ten complete source units: all three original E17 input generators; exact reconstruction of the accepted83-type checkpoint; the unchanged locator; every selected configuration for650 cases; the exact whole-domain verifier; an independent coefficient/label/frontier review; the actual366 control; and the375 attainer. No attachment, omitted helper or external coefficient array is needed to regenerate the new objects. The original transport programs are included only to reproduce accepted input bytes. The prior four-type proof remains inherited by its exact checkpoint identity.

For A fans and k lexicographically sorted cells, the integer layout is: first9A entries for gamma; next8k for lambda, ordered by cell and increasing canonical source vertex excluding the root; next45(A−1) for symmetric K in row-major upper-triangle order, with diagonal2z and off-diagonalz; finalA−1 entries for eta. Thus each record has9A+8k+46(A−1) integers. The generator verifies exact per-type and aggregate byte pins; the independent verifier reconstructs every quadratic form and proves positive definiteness in exact arithmetic.

Observed runtime: CPython3.12.14, NumPy2.3.5, SciPy1.17.0, x86_64 little-endian Linux, OpenBLAS0.3.30 pthreads with SkylakeX kernels, NumPy ILP64 and SciPy LP64. Each locator process uses one BLAS thread. Parameters are `merged=True`, `cov=True`, `eps=1e-8`, `maxouter=13`; powers2 through10 are tried in order, accepting the first exact-PD integer result. No randomness is used. Full recovery runs at most three independent type processes concurrently. Exact audits and controls use only the standard library.

```sh
python -m pip install numpy==2.3.5 scipy==1.17.0
python recover_c34_v2.py c34_v2_recovery --full
```

Extraction alone is `python -S recover_c34_v2.py c34_v2_recovery`. For a directory with the pinned outputs, `python recover_c34_v2.py c34_v2_recovery --check` reruns all exact audits, unchanged-row comparisons and actual-body checks. Numerical reconstruction was byte-identical in the observed environment; a differing floating implementation must pass the embedded exact pins and verifier before its output can be identified with this successor.

The complete source pack is63099 bytes, SHA-256 `5d28882e10b8f9e9db981820428bf1488cfd9f603c4fafeef1933a8613fb71f7`. The following recovery program is26726 UTF-8 bytes with LF endings, SHA-256 `c1f9c3daea6fb635877fee61f4257858230cc567e6e24ed2cd8de3febc338e10`. Its compressed data contain complete sources.

```python
"""Self-contained C34/V9 nine additional physical exclusions, version2.
Run: python recover_c34_v2.py NEW_DIRECTORY --full
Extraction/checking: CPython3.12.14 stdlib. Full coefficient reconstruction also
uses NumPy2.3.5 and SciPy1.17.0, one BLAS thread per process, three processes.
--check instead verifies already reconstructed pinned outputs without locating.
Every input generator, selected fan configuration, verifier and control is embedded.
"""
import base64,hashlib,json,lzma,os,subprocess,sys,concurrent.futures
from pathlib import Path
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
PACK_PIN=[63099, '5d28882e10b8f9e9db981820428bf1488cfd9f603c4fafeef1933a8613fb71f7']
EXPECTED={'c34_catalogue.json': [1111066, '1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77'], 'c34_v9_transport.json': [429422, '39e76083e8340d3941a7197d1ec9e636e612a232448bf1adae2c212e7e136de4'], 'c34_terminal_brooms.json': [393185, '23c58f4864268bdbd2fed94f7a9e9e9062d269cce5ba2e14f10c958edc99d205'], 'parent83.json': [391085, '1145cf687979cac9880e332fb64c0f92ecc63cf715142a2432f7fc93061290e7'], 'nine_type_certificates.json': [614331, '176256a0cac94125a9faa76b16021e9d88d43eb9968aa7806c341f090f05c9c5'], 'nine_type_audit.json': [135656, '9972d08aa34c0512bbb6a6fb67de2f718bb2e22b72ae839ffda6c616ec3205b2'], 'c34_physical_remainder_v2.json': [374971, 'c807152b6d7237e0987b54b9cdc207aee8e731f7614dc885ef1e13d09384d954'], 'type366_actual_fans.json': [20423, 'b842e96b3a943607a1f55582eaa562f7dac8e0e754aa5b07a93731ab7c681573'], 'type366_certificate_actual_body_check.json': [26516, '046932bb46fb8fe890a32594039e69dcc8d3635986480c1cb73b93d764397034'], 'attainer375.json': [4006, '2aa06ddb67d9648067d86315b1c3cbe8d1d40ba34463c3917a50b69494f7df34']}
PAYLOAD=b"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;P!e)KV1Mlh=|72466Jy-mG6@@vRma&^4FN1{NU3ggN9CWeAxu6^+xzm3wV<`zl-L=BeD&
3HBuxD<UBu5Phe*@lqQfbovxHMH4TkaHc+(4PXgd(wk!$oP<&wwXw;IhC=uII{1)ofz{;cOm3T)OADXqYgfzaARP1O_K4LcLdSBS
bf8b=(?1QaE9_lMhfs~w{=wW7{PXo*H<(o-Bf3q(McyrZ-Pqsu&D#A0QIA<_(V!r+tfKJ3Bp&s}d*SUu4M3v)mvr>~>J#TI#Unn!
_*6e(vNVO-QOr}3Ec~yy54_Z*1~;hi8TShOo*B{);F6|+-mJQ)x#H>ey}905I+2d@mAiNodk;8-?62r{F6>8OR5%26Z=*&f$o}fx
YvLQn<=n%&@h+UfEClE@Afj;3xmn$n04f*=2hH&5|G5A&FPNW@T)*VC#SU8>)|{hTB!6E++<}T^qaI%9<|Pi&Jny}%=X1z-i7bPK
Q%1%rO-g1bC8RqQfN94SdEC}_#FZ47yiDftDr#($8HEgW+qz2KM!kQ8o~D||9KeOLJ!YJ;@{$<6oswma?kh2s2TfjYZV-9JF4aLi
##NT-7KBZF2>hXQ?fvS|x+v}qtA3wz?Ll8`_W4{q3TqW+_{CEK#sg+=)zqI(RchWo<k*GjJB=eQ<s&cja>(|^@~^B`$kNsMJ`C|O
R#}bn47nT2Crgtcr8n&SNsSF8f>=2?S-uy+4M4+>PzW`KwQz{_md<H9tPp}in>@e)BBXx*)~R?S&gw^}A#^)LGvhsvi*zO?G;G8t
c+|*?EU{?;H-yi3b_;SnE+Zj~)u09%zZ|zdb-kAkDLI;5(w?Kgdr0OgKwV*JdT)RCqoTtI`<uE`77}ZcT@MB!BkVbqWv1Q9v%D3-
(d0dI2#6KrkXKzMga{JJNg+<xXzbp%8ld%uPb>7epyfcc?e?YEmQL>KzVc7?rlZ4c$tYTcSlD<V{HOLhGWR<IG7HsAOIJ)r{wene
*#M<xe~!PekJx>_!pe}5y@J4$xsSrn%Obo#i~3LdQ+|<$x+){YCpI%bOWxADQts4AU0W|#B&%dq536O+N#G~nFoWO=Ehy^eWdRX>
noGmEbe~RkFA&_b@i64q-2)S56u8NR_$kez90&tRbr)JG@)~4j5O_q)kan4;(tqK|oU}u`znwKfiBv1~+_ZjdDQ_~H8x|4h@V<hw
$PI^=$%1<2c0L(`re|E0bWM8HPh=m5yWg#z4ATuM;&)Hk$Uxvwb?+r)cC0rN!K!+PP8M_hKCq$*(yq;`N%7}92$P>30hY*SZn&z=
Blf$Mp3qj8@*2tZ6&h6#0X>Z4Yl(QZW8kf3i-cY`2(OljTi+R`v$t!G5G_8AQh5o`uurG&&^fb5W;1Ps4_0pAP+~epX~4B&JlsgT
W_|o+sRO@UADWjn)<`myfW^72A-YvZ1co|;{W5Gf!)LGr1L_L%a+HUh0U>z=EK2iK|BSooE4}{;!83?s1dRv9YeDv?FzyR$&<jNC
K0SH@c)^n*^J)q2F<0lj@GblyrD;A0>0O<1i=_npO_KalnxZNU$|qI_nDP+EYk>nUNPe64)B?sI6I#$Pn{L9ZyVS^@P0W@iD9O;H
77GClk>G~C7@7AgbresJ!A@aW4;7bhgF*^Dv5oLe?cf*!4ZeD#Hmv-i`gvIlV&gr|)1-I|<cDu70$_LH8Kjkr4WOE)X;Zsou=2#U
_{M@?yw%(yz;Mo{qxvnf^(Q8mjq&)g;<!O1jiZ_pLo;Bgzcaxo<}wb93KXIB%g@?NOpJ&=K^RjcOCAhT%Ghi>aSz~P2BKzSxVAh3
%%n~V^#9f&u1A1;P!4Grj}mj;IF{+9fBv$UHt1)l&5Tr|qH0l`WWO&Ef%h-!;s$M4_uyHJt}1jUSK7e;urAsfcy}hG1eXH0HQyi<
igfO87p2ZsDAdr{JQaW8uoT{U9%&S3`n*hUR(@R#;1Fh`jynK=^gJC$#YF}cAd_inC`edC$KO(Nt(8sTdO@FL^9o_I#|!xeTQEqs
4Ff)fzUF#<&K=h%CDR<c2g0Yeq0z#r>JmSUjIuMR0oIDrcHfeWVM+r0v!4;I3#748<>f<u%9{|s`+~@>c+{mH6dZ&&^t?Q{F80}2
krDQGepup^pSJUtcDy(Ox}M4`Ig^0$C9WdaB0PC22M0%qC3Jf(rK+kIP}T5)BCDTnk^M+3ap2}Wqhwg%37V6r&3CSn0$L=7o}}ar
W5z@caAX$T$ZQ*H^J`WyLxw$Lf#j5it`{8bYz@E3Eo3I(tYKcQYO@a5;ya4p{)kwc!0MGqGTt%?knLsu=*rj^hhyD;tJXx40(WV2
^*EDt6Frm#@1OD$*r3sB-MMW*3fMl!O)9=d*$BTR>M_qS-Q%^y@H&YbQ&W#TlpYMRrS)v1QTkIahYUEFZtomr?*DMk&6=7D`|8V)
uK6Vnmh0yjB(QxC<1$zRm=_zR3*wD;wGStX%0UZyU)F~Q(vR9C>1s9Kmj$i4a@&0$EmXvvjj?cyAs4@FCUFj3b>*v}vxx>k;`Ta#
o_(a&2LcQWIf9iL1XJE%<4|LY%__fy1K9z5c^wI5A;lAQ6ErR{1H4dRN+!8&G+d@JN%>9$2KBgFR9BGYc~59(>)O^Bkk=i(Q-Y1h
mL-#+lp1q$Cb_N2s0u7Od!+>|WAmswRLNgtFuUNAE#~R-J&(FFud4l5X|MV^Bkpq^r02k`Smu3N)&LkI%_#hZbC=sou*oJ5Q%df<
80S<xsRvJ2sY{%0iWT%UbLLzB=(}4ls3Yo#zmROTDrPVY@y0synX#%x3#09NuwyX<TS2_SM1)2`SU{)Itxr{Ib=sznHsv)=S*b^~
aKbIjDg91Zq>_3HczA~*Os3L<Q8%f+>E)_-P|>a_j;55kU9!C7wP9(YLr0svmMQS`;wV)KZ<c_e??W~fj?@FWDC_bLIG-yluomP|
7xX&W*$gXv#k%(?tufyjJ8YJYbGZwI2HnlQtm6;_*kx-Q+akrig&6<iThgksn}=LH>gSaAWo?x^3N_DkZ;$5Z!x=SOqoo*|_kXNS
B(D)^BU9yf()s>S?!<Dw=MkX;4@hGQEum)@$zKF|ZY6He2E>Gi6|KK@>9=QsRL!MiNa-w@YqHYN!Q*N>jg0FJE^2oPFB3ehrvifu
>sViI)Fq2AkZxg7m*h2{^J3IqGE%d(De~d6XNMfhd(adoq5YdCb+Y(Oux@VcRrnrSvj{O#J0uR+teMjCZC#2iqYF_e&el3h<gFp-
*ZtP({*`18Aei&|>;vZD1ePk4Cu3NrMv_oFtZ3Ci##?;us(;!Evnc<*F`l=!1d~{>&{I0n?Va~oTNYzG?09TNCjU-`nAnSF0D@#|
n!)aK<6~w9!zb+|8=Azui@lgyo0Iu!WT7ds@?dj{4%mG1F@*mE-75N0C$VRv2)LCxEFkxq!V{^#&~RAY(Poq%_-}^7A$#b_a-^Vc
&4l`_bvJKkBtGj8Az>=O)GQ69bvc)FQY5^GE2a;-Cbnp-=p@1r+RRXhGp$*Y-s}A6#jbRY&*<qx!pgTMMUjUa1}4?tRNU&}0x+Si
pBS%fv4*Lx0!Fa2srj3k4xiDs<8)PLUyl%8lGpW<bj3{H`;DU$5AM{Y(3245a~Ym)#G$7t)MA799sS47S9JL|wzpD8@pgP^FWo9|
GV%P0N~>MWRd#_Na*9MpG{NNNTlu*(X+?oD?`&CNP|3?lf(8k*I`KJZ?ydw3K=<TLbIXJHatG)$&B1u*8vr2)CDnokZuX2uO&{_C
*yV1Uk6d1kw!Dup=cJhZ!&Wg6-&(pB<uGAb82Fu%)#CId0IqyqWvMW{@~tbu-EOWX&$;(+*}M0}+U8s>$+9grVs{3xiFkSXc^MsP
PRzUYsyrzO?(?CavRybfoPEwcXY!mrG38IDB)+YaU;dgUdk1)+4Yw><D1Dh*uOQrpyHs8bgO>{fTiEM7{`!i_8SG)p-W@GWzn?Fj
@1|~90g}NC$xQ2cNNXS=hIOx*F>kxdh-TGz5>;ezDX^7;7X)erX5)vJLncGLWe`3rC<4|YW)IDkGtGGlTltj?+Bw`W8iITYVu(yD
Ho~4>+M2@)cDw7I8OwXhL_T<}vNYR*t!RRWWbhy69(H{Yu0A3RyE~&Z?SdDD!pXHK%FHhqw8A-s$_rGAhXz((`<t4Mu5LrsOT30b
_4J-sNrm~uIBY!F(yp>}oICat-U%s2m-~G~>r}HR7hl<26%a8ZSlGwC=~>hrfWGQa5X61x-B0=I*02s9UAsz5ti-?1J-bz4+u(UA
vVQA7t$pYq{PN@e^P+RxErM~iR>ogZIWGfiTkFKbB@)`5&b_SCfGDuceC6A*xh9%yiE&5gG9%*6ali1+XRWK#b+joCKSCFl(hXur
=}}V_`m+3xZe|U-c(!At;pQeJttQ3)h#Q9{ew2m4J&hmWow?<~q=D$!jE;K+tYvO?0+HlDQgUHWKHUpCWfrOc8@2E2uR<}11tRH5
wy9UyiQ2{TJ)avdQyeOpes5AcP8FAvZ^Tr)E~lC@&Wk`XsfSRkr?>*>L^tJq5S6aJv(PvqNkjx&^EE)Ik5|6(!sG}fqMjwagPWK=
{A^o`^2%-6#J8IKHlpa8+F&v`DSLXIIkJYwj;z5>wWdY^$h~eX-TID}V-C;!H*9UMG;nU_d%qo%xwuak88Qa}8sL)Wr)L|nY|#aj
l>z@L971_EYw7~5b3!^PUAMnFKmXYzGUZ|Iq_oCoK>{S_RBP2Zl6;`aQ48c>Df>84%H;~*Dr!J^lsK^HYeC@B#(>&fcL1H0<2ohA
NK=e>0Q+s%p34~2dVd<fS)nwpcEHNocAS18O{u~Hl(0YvAe*EpWhxBBd2;d-P<_VJLq3!>Wl1L**_524o6JQB{o{jCLuq^<+n_e5
t{n!WTo>v;l7Wt@c`S8~tJy}U(Jnq{LzT&xosr=qf8QL8`?DNSSXp`eX#MCo?vdK0is1{ojsAn&1h3v;u=Hp9j^mXfV;=2)k2v2x
51)z?d+-6$4`Sn-_VhcpESw#UEP0`XpXy_jNrE!Exxz@(yv%R$0Y^`fb_(G$_9Es%x-kqq0~HC@_xag{O;iP5s1b)2TIT%DkZwt+
Qjmi2Vl1*$174P-JL~h=XQpanF1hB|CJ!9eq4sqmkd?vp-X7y-#eQ5wslF8ljPZwBY4=Eika#Sa{Iq@-K~X*wt21jAiHOa3$i3VB
R!t+|xYZ3%6FYkkP@bc%HaNexs3g<@^C>@}t?CBYj>VP`AC~}2@XMLR>6;7}ih9!(h1olpGr?5QMuqUh#N0J0sPw9Gj19IRUf(xT
e(Q%|J!i%PiJ*YnLHeK$$A`tD(l(2R9-ok!PuPtbxADQ#^A#r^auEuO>4=?%MGug>d;Aw5W3TzJkMM;V`?+*i4D>`AH0nqU9aC^d
te9n`Fhlg%h`ISgf%J>jX0CO(kS^GYCnGoBz-L6<^5;}+fb+{}t+Xh;Xjl2j=5tb+)xhyi{Z-(}=1lxCb3VHRYsJwiL&tN#g#}S1
m=V^rY-%siEb(RZMC|8<xo61J$O2tGIvcB?cHZR$qxkcvuRhrZCa|1Mtq+JqV*y0aMmDPKDcY#N6t{EY{yLMl5M7ta=rm2}J18zG
c=wdXd!HgG`@*?SoaqfNBXUT8>tf9S#==Vf{Yb?cPVa)xhcfznOV=0^zvN3h>SC~%Vye`}LiUAzY2vJ<!3*lDm+tb!n|KB6C$zY^
FAN_6cNr`c2WV>&AD?qdC{;BU&ZhDX+LCfteHHYw7sAZu=9rN-DqKL|X-sO*`1F?iq`d}ur`FT-q@RBq1MzJ(2LxgC0V4Cwb<|>H
SpWdDy`5W1mB}Ysmx}gZFNoyWdFq5iOfx;n=+C1svAYS*FMC7=&&2he%1jlb1IJB5ZXnsD19GckCf$j_5Uh8-C9j?V@TdFUx5m;a
B_9*}kaM)~cCRl4cztKlgyh|m7VeV;a#gcFAi4Pj5_xWuT`rxZ3&3C0hs!1{HOPtD)s)yQOTscZkZB7yuy0Du0T9$!Ei8~jgB)QW
6a$sQ-u89Wza(pQu0xl$>;dMO@7^vH`K{<1t&v$Ue5ar>bFt#OrIj%})5X>tXg;TPn3f0sJzKJhU$FY|$I7xxxT#jfb*~=g5f;=-
HM*o+i`~}BOZ<zs>0)>3K3A5oabJ=XngsLJr;>sTby=(GchIoY1uX+#_?2)x*!fsglvnARm{T*b^suQ2_49!6U{ra_1)!#u=ps)P
6yT56mh1(j;`3P95CpQk<snGX6o7p8lS2k@6tqU3-ACQ^Kyx+265(GZx7E4X8U)#nmpc5$i)1C{&DBq&Q@or8LS!SX?mq{Fey0b;
9BCp$pshbj#U4Oj<c6I)6V=%!2r4{Zvxi-h;%To#_-uFe=M(g-VWTv0&>t2CzPSk_Ma94Wu+pRBtJ37Xn&p+nhiE`>XSGdn0xOhV
WHQ6<OHP0r0Io%x3ih1mD=>`jJ{LAt7dFa&TgV8K5OKgn6DCyRg^{7H%9*XS!FRA7ess62SESIjj4ww>u}~K|VM!q=HrVHM?}EJr
wX*hx1SkA%#Rig9hLv_ErixAhD@N?Y`^PKcD%Dde42sNJw`$gTxhO?Vd{;n6QwsEVHR$3*uHzDxSh5LF;}bX|BJmcJs_6Irdr1Y*
NFZa9-}Z6mta<esuM{rLtK|Z{+Djlj4M-E-KtE<jhw)_dOHE06wsrmPyKgw}ubAv=@_m%6JCO+6@k+TnduIB&&ApXa{J%PuoaUBR
Eh$Q($Mgv^kvi*513v}em!r>0S|Mg4-#0kNL(5pI1GyR6t;XZuNdw&WEpRfAO`mveUG(=~8NkvxSS5d)<Iu+$hedQ(me&yvlBf+O
RDAC`tU&&I@9K4#BsSWU0;7Z4^ms@n*?ZN{!??4oYE#n2Rc@Hey1Q7G|F;YhoDFpdv2MWK^y$Ms;El+`S^Al4{M}Qd-@rUB=mRZo
?A*n@46p+p{nMJACB>=thQ?o+RTz5bD}QW30*FQ8H+y-OF5K5oS^g(MxVyea&FfJJwuRH#*i*AP&Q;WR3=!t&f1nGxNnc++3RB(M
ybRISIIp?L7Vvmdwi|*IAY6^8%~39U+INPlD{+MjwV7awC-|kzS=<2Y=8BwNsTDP<vQTT6zY(mf5g_>3-sx^cGeDetzuK=u^wnf6
AbkiLI*%G&zv_H8v@;3kgDNQWi6<yG3#LdR5E#|ei74@%Z@zPv8{k4xRR?NMTzQ6d&t`hM1CE$Dy1+*(F+(!U&!UYtla}`M*z>#%
VZY1N2FTr^tZb57AjZ^YUPEkGBAZ(TsmLnD)i`x5z{rcEfO~>`%-b7uo96!j;gkH1=2WCKa@pL@br{1>QAC<Vs{I|u6{;xb&`HZL
)e<+uY!3pwgJcE)iLBbX)cjxIV4AnZ(dIvGUi0#IY(xg)f{JQ!DDVpA@In>!g{=tx4Rwj7cqFz7<`p(#0of40qT+KRzS+FlJHzW@
a-IJUpj7d*pH61wnmokc;Y4R1wZ}+{-oO@2yA#Ld8`rN$;p9twBu0FPPP30l=!xVzJAp`mq@ZOjhD=yi{4X={@F-5E;hv=$AB4@^
8g;sFG7os9^7?AJCyZe8`K5v9_$A#_P!<*V=FC0-@Jl4|$>%(`C~<JAsh_s%{R{*%Pfo(i@WM3t?{VgW8gg!H&HTknJE%P)X^Y9^
jkq~EKKV`pAzg7$nQz0Cd-wJMmk-M(F1{~8$PrZu#b<;$MD`Xc@MJ8K{H-Y58z>k8;QXkBpk3OIwP<6!P|rg*tUWs@u5MLY*4-+`
uU=yPtyr_BA4X4vSpWv3iDiWMHQ!a^dJ~oM2Mny!4wy?BMDqwOosRU@$=0+AhpjFj50}}M5fb3`?_AGkSj_5Jt}zCDW`spDIIpg?
cKjQEwi3g)P;Hq4hif&$H@ZZN6PB`-?HJEEt?Ik7P>B&syslOa52iGdh<^$J`4?0EUF$;i31k#vE*`JXTpPNoWIl}K&8nI3hypND
Q2bYj3eM8=+8d&oS)kZ!eA(e{S0m71)U<vqZZn8WVG?G5UcH@QW`XgKpW}^Ol&#e%P*v+_s@|QmumH~c80m|_saMrTkU9!$$TQ`V
$gc(|b2ZrL5x=+)59qwBBpJUIdrqyJ)rKNZ)W9r*(P1?rI2!`;5w9JuT!~@7(j(RHkq508V3BByCi?i<8qQ4jdMP#M*S(uj&#W3&
W4?#yv}7CG(eTH{s7EE*dKFE$*ZK6ct%s7%@CP+pOKAM~ttIH{xrAg!$FaVb?(QVQ_j+}7v04=6t<CpZm_1ZtX{Ze^>Ee1^IufK=
Qam(gpdKfkAl=u5o3-&Fg854a$O0l}c;m<^bo-uWUfq^N`<IC+Tw%FNLnuN@9;t@${i3kZZtwj;DAy-|d!UJ8{Z5mUuhCGv^V&%>
2>H5-@i<?qh+&ho{Q3w`(m{vdIe+1`JMIfdBIujn<|!Oeu`!!GRcv?;m1noI<2^fD-n!l*k~9x<+(B&A{L==i^6tyu8vXwIAIM44
;C<<meDmkZ8o#DvJ!r$)J&1otlG6KkXI>IB5deFbffTr3%kD1_%**$uJ80V%*Vtg#v+ewVNT2D;v3z(TBu?dDgfaV_23Li(_Goa$
OnR7of06?8Ew>i<MWAX&nR^GA5DD-dYpm_1k8S_dnfaMn6X46zM+f%_O5C0}hhF67eDzilFued<Xcv;^ybPkO)|ULM3}>?U-L$Ek
YNkf$2*++Uu|B!WmK8Kn_(`9{f8S$Mq-3e0zh4HJKo7NdbX`FHM%+Ism`k!V@QV{jqev*)*=7Va8VXa|ah)--*MM(NVe{QhBhC!4
YoF7?HlJ`pbm*mQ#4UdUU)G24Z}%0HpJEeeibZLdD1N=ipZO7ZD-@Oz^PfSQMoz0<_sI`-%-KN*rP}$6P&p>^K3)8MkjySTP0U>f
_qbd)ZrL96DBZ5D8si&wrX5_w{|*18XR@+W!eQ}6j5LT=4wZ>T+_pOsa^*9P;d52&07)^a@2u{Ucct5}B6;MdgQ;JN$EPDHCdHdZ
tR06&Z{}`R_$$2j|ADpjr~0wjnO<E)vOcWO-01+q)0->U#(#I8hyZnjCENQgA6+WP#;c|ARzFkSm5$k<X=J();=i919<PgTsE7sG
t1jT01i9}88R8dKy)o%s5vuzZ7sa$O-fasU@th7i(3G8OZUN^j7#9{WUdJ&C(9_8uK9#;l_S=!sXu9uM6vW=6DbagBvnm@qsLx~p
uSOn`>hmcug$Ursd?HItU3cEbaxiTrgK8;~Bcx{2e#zk%U$WU8Oe2%>?Ma~52u0T4>6+=nJni~|TLbm~Mw)lltYSEmkAl~6m{cxj
=oP2Y<x{H9oZl7|T|k?UZ3M%Rw9Gpz-B|7Q+R6@{@~_t<XSR$UtLftc^anNarY3|P)<**+&?o{eqDIxON-_=|YdDe&5R(Bmiw~<p
4n5-@g?(b<6s{_C8vAJ;tNB2*{7Z+GMUJ2I5Z5VVF!J}gtA#K2g|EyzaD}+n2-UMWLVPnCnqT^#>Z0LJUE)Jh4HW;}N^v2^e0OgH
zENq^S;MH~dXuR}2jH}1;=xm<*WjboD;?@pQH~L#wh8j-CFF&w{bLF`YTED-=noplsU!S%QvGox5KxN;6~UIjtd>&TnIyQAL(YIg
Z%i(7hGDNe{!s<tz+|O9n<?EfePohy2J9x)>I{s!^(IMQrXSn|v=~0n+|u^N56u&R(?!9cr3J}WN>r^oO`7B00OZrJWuD~ipzGXi
=v5&;<a7ETe)l!(@k+tCp9IV-+0M>ancqNN2}4leh(LDT)_qX8(ca~Lc0HVy8d2yYcTR>OP%4LM!@bXU79iz7QsNF6Y}a>2)-^&@
6L=YHVx!;sp?xc~pqY4nQcF1sQXS*k-dJjB#+**j!&BQksoJ8?!kZ|@)ZT0T?3_%!0Aq_NPR*}i`u}P+7H|Q88KXloa+LcGW~7}p
eE?HV+R{3Hvq!OC`u%H}uty?5b*p_OX*5KJ$>l%)WRH=YIlLQCx;VjiuqBDDansS6lczwDPY{5a{0wGz807$)oFwYTHoQp82fyBS
l{24fV8PoVovROM5DvH={-%L%+Dm6}w1{m`^_{RzE~jNL%Il1^vmCSzoQK`ngwUs4qf`ib=b$}%+c+;lo>7pkV-rT+6qEb;)750%
+3F^e(K4v*^gnER$<y&T(O|nt(jB8Ze%Nofl%cD<!>Rbnn=sMtN$92@s}O!u`fWq@JQo)UVe5$8Vk$|FOw~n0)O68lq-lr6YHKq9
Sl;()IDm&YOqSk_*Tcgiweu;;Ox{<eBDfpyJIY?^dLNrzst{x2TaJn9k!->YG=+!(5Jg<Mr!hxK!2^yacxzp5dtKqq#anr|L#(09
L|4twOCvG?x&cC!v6W8u2`pblbE<;Z36#U(m~51gdR$QCAjRgOhrgh0ioU`Z=w(X`&fM+-P6%(vL+-o`@TC+CpZX{R99`j2dpJf8
AalA9n<0I-l!I}ByYJY0Wx-eFZAZfOHF<Rxf?K5yIr_uVykyDWUmd}N8==)FLSE{9jCYIkREMel+?r|Leih<}at@DFhVuBGy|APV
1Yhg_5?D9VNcfAe!bw6;(-pW}Jb-JP_M$iR>fbkTL}$RaB$vJhI7dUe5C*q^3<&o%1wC<CG0>e8L^LRRht!}qMP-NuzGTboCiL=v
+(|dKJGJa-TQtMDoGn9fLpTAVq;Cx?ib)<JEcv%F5dDj={{Cx@`JYeCi6tSCI8xL;>EIH-genGP===*qeix|ZW7_h3qq?s(JcULU
3!P=8jv^dTyZsu|0Tkn}FV;bC@AH%cs{+VYSZ3yDcT+4Cd%I`>w+CGK7R%-%OFY!o^NcD3E|{Ag)UUpym${l@(@4n%E^<*Oqu;0N
>H~i*9M&ddDjkg5VXJ`qt68$=h{0DiReI)9-Q_x4U~=^g1k|EbN&+OcCt1T~wb-}vLt3$*tkw}bxGtnzWk@}p&pet%15vj5YXYAy
Nn_4%b*q2jTguR4+zCC?`29#R{mxC_-+XQR(-6myh2|lEl>JN`C9qagQ`1ECFmo0c08w)Mh@5BT*X^r)%U5fc&alP){}oMqDFKme
oA&s^^2ElOJ8s{yKlNL=bStWKw730!+m%u3>BycOB>?d7JGiM89mQDJ0`La{VHgbUDjAm_#JFrNS};I!f=QjlTSU>1=D56Xaq;}N
6ht^rGH66-E7YBOl@3?<%!KlrT%%rm<vLTJtWr50=|HG?zW^6LD!;cHHPu783Z40$4Rqj6Wi-V1h;@EE#|65|Ld6DEwb@zC;NFad
C>kZ{cUeMlVY|_0Im15EV+@%!F$pso<X()iO41ihxB;k3NsXAuy5dI}vGxnp#p{3^v(F`&#!iZq)Y)+&*|D1SYj^rbH%n*FQT<Cg
duIo~h%M?IVgGfVl-Yyy@g;8+39k*NBu`;fthdMsM}l>id~i;Hn#NA{jgzAJ;&rm%f?fK*1A&osCZLJ5@KRT8<CR|Q0L|^|8TDNL
yq!)uUvief8j_b`Frzkte;^!S>?49!UZ95Gu%%EWrY0i<eCpcDpMV~t2``rIZuEu?s!gneH?2NYs-(ptyR5WI8k=ae&K4J;P5bD;
va*cnRO@xJ<4r^xfH9TofLCH)Fo&wjF~Ax@0$FNu)ez`tv}=I~?dam{H(hV&;mC8u>ehfnBq|sC`dO}U=Z6%aN6S0mKnx0c?t5gI
W*p-Zl91!tj2sJLI0e%G#wqgOV^OsrT)V;09%Fg=>|(QxkV4aBuNkXPj96ga&dj)~ZI&3Vo+nOU(R1vx-1=Cr&O)0bq@oP%^4ied
Hkl%?FhZ0dqhNjz=hb+t{DbWZ8#9uXnX;Qy%H5wo4s|intF<1+aD`j5Ina?iUqp6!g%aTNBiX7i`bPStqPraE&Wlz=FEoY{m06P+
o#=p~M*1sJq+PYiKsl9yk1hUk;oRyj0EVI~63ekXrVZ}bZC+a-zNq1mE^|}f=!spH&j)KSjM*xPSVR{n60~B>d`|k9mw{x=Aj#IU
LgQGuXE#Y0XRG>w@;@-;8NCQuF8BHeXGJjPvukx222u8DoNC-!^3P6I0eBfu4XI|v0Oxn>EdzMN6{cqV1SaPk$_a{iX8H3s0iJH&
FmBs5m3yf~Fu{}vAbV4lni8U}KIlD`{)T@i7EdI>_YeZ#M#>a^0Dk47R0_I2jm3gw5(jBT(j`QGhC-`*1i2kp?m}ecuel&b^I`T-
5{cuijv!mowRCpBN`;8U0`&X+y_aJ$J%mEuCid?u(?Q@dq9GgYq04?&UxT}DzW>CqgFkE2;Kd>CLd2(7TbGoML*#)2o4x?x-TiQ$
o{i0Vct=N5(EUX;C@lNpuoPWs3bQH=DV-!2thsIp#67+*ogI$+Wl?T3o4d&FYcPg9xQgnUHg3j|nr~2F1X*w&uh&q`6%U;y{4BX1
4<uxYP37@#o7o7V*F9yY74siD_+gca-QLTG;p<dBomIo=9l^@65eY?gRpug1&N)jsrp#F4Pt~o}%~(bbNaKMn0uYzx%R{u9@5%^i
*CRO1w8s`Jn%|8-?x3<7{W8tPl0U9brBtHA&M%IDJR0G|v1cxHb429^!Uw$yQbFIQ7@=5Kb-n4Z@QP(bAcoepG^W*wbXe180CjuG
2p+scQCqmzarvW<76ty>ZgmrP&IZX4hG`M4F*HFIV0FNHc>{xjA;^eFpI#r1@hUg)FF_!^(t62xI>9fjzU4m9Uw|`9MDmj%8FA*e
vH|P7?7L&LDE~*i8LSq`H!er&i=r?!^;6NOjiSVu%|!ov^F7b)oU2rgxPuWFqii`q2p<ycA#0{KX=6C6lg{B8pny1o7oc>*Wa_B!
@0~%DD@TM;l&-|0T-WKDGZg@~Rh|-lJ$+3qxJ?3>8$b(s6yrkM2j#O27+90trQD1bSd?u;Gra`2w}3&L+|KEdMw)nkjv6=^EA>G4
Trqq;vsdTomxEF|->PoYMoxIvE7Q&r@(IL*44y<&vW*Jmbw^mbi0;mUU+7C{N)tO;A-gokBkFp#W?)}HZKr7=?Bh;)!)Fr5@XU~9
r~3hFL<GTVG4MMCve%_D_2XndpJgKHcE1Gbe{ScR9x_r*e8YEv=hj6=?3V7ry)bL*Q4FA5kueJcIS$DRAGT2F6W02$&FPXrf!Zt}
?Tb&ny43J<^T`V81$eUWMRqdVGy)DC3t6cB;d%U*lIbHNX|f<7f9^&%@un1)!%mP7tXSaXBnr5wsL|T0s9kIGSGsHnNvUTi4ww=i
xm`v;>JOAo-myoK8=X|JRyZ<e;Q)GUY>~D}rb$U9l0qu#@B=4dCcXkekhYOmj`k#m5&_@dHN8d|Jz3-u#waY6Y+WPMPnN-%d}^QN
k&M+>l6iN_R2Z+61E`i0DM_(JV9y;(p8@kRR-Q0fE_8#5bu1(zsfG=IXY=)Y|2`?PNWLrEab<I+FLeEAZfC9C)9|}{XTOQY_npLO
(!%kP9+!@4s!73m&0&nyll_)!5h(XX=%D(Yl$}Z?SFqwi&B~SZo79}6h=E9@ENC*&4&K+5BY<FTo1}*pgT80-8G8WK3?#uc9{JOD
ReJYSWTiT)p)TTF)+35ng(Fp7ganEHm1$jY&>fLA{GUMPMwV9%e{GI4!6;bwmRP7(EjK->)xsmsqPJlSXoWYR9H1U_za?-tX^z$Y
7rCjZAMOrqMV|F)U44*>f}GPr!aDw{FKL-`Y_tuhF`hPd?=6dc3O-&_a8Q58=ZNw>R;f$#m%wKMFI#JgbQAG`gWESU-c$fP>{R=-
Wn|q}1!<YzZpgQPZo<!+4z43|4ge{|kb@Gjk`FS;h(O;@9=Wp!qin4*R6iao$I`T<m)Qo4=*34nAuG9X<n=*fscZ1&K2|%eTL81D
9&>Y-<LYwt6dculV?ec~OvK#+)|mQ3fMY~rjpPsQ<<c1uTSk-@!tfQABR@<6Ls97jD|UA2656iW2mz_k^>lx-uoo(N>s5KOCIM8K
J|96Il?dxoSUwf!3kd61WJFGyYrPMy`pKA3`QFuNVW6Lk{&KnJm59vu`FEAuIc7c6;~4?w^r3OZ8@!kE*X{1v{E9QyimvgvS25n2
bb*F#(PK?F+NFfN%{+@aatPlh;dz=c{C=k!!`&+V$Y~iTl~UhZemQ}JJMK(c<^J9oK4-cY2mj#j0{9VoXBe{?ob503eP%5RpXau^
EQe5sBWkNn9Fh>_FLSpd2+dF)Qvm4xVvMM7R-}7^sm)Fsu$(iT!-|#c;I$WRuPFkCSh>z=!kTQx#C#o|=fMe2ax$JWDwgK9gQ(JE
a;4u9vSneeL6olzdek*v0<VO$JWUcNnDzk?&JVpQJVyz#-7({w<&#_uY+`xJ@=+V&h~t7VRop4<ecZN2BEYr+r|z($U8d{?j{jr-
J)vbd6%hE~pqA$v)q2IEaerBoqzG&Y!R`7Cni!<*y7E;JC6519P!}hk@KSQZ&0>$KlV^EQIPv|yzGWpqzx=Dceq3KHM7Uz&-E>U-
-J`rz{pp<4$?tQP5SA$ArbYsmU1@`ZrViT)Lr#nKPJvTwM*!%@*bf@14-y*<{!`Zd^ODPIJk~qyxA|1RC+7<BIZFmKCY_MyF>9k;
B%@g1F@SBJa4^t}G48@Z-WW<a-4&7y-gqP~!^4KT5@+znkKksK0dIg`#-Cx9!Txt{tS-%GjT7X~3KQhr*nrwomISpcA6vX_sMjQ|
j+nyo8+W=x!Z-dQ#cq>1{CqOIu!B2%etIUjFc2CYF9+dVgy>@dsBwj>IC}~(f!UcS@<0p`fY+{Ca0(|aCV2yKe^$;)s5K;-n$f2|
jTAggDhm25Jeie)jsa-HE;t;AA$Q(yK3DI?Q5odS9RRKyE=L$^H*?uiRnp1nJJsxp;52TYpTFFM|HByA%Kt=hQlvRH1ePG`7ZB~N
kK$d!DQ`xzhq+qqV9iB{gap54(;_C@QHbTMi7H{3RxcVOd)YPJwf;52JE)el(cD->RB(3wYxZ8vQ!QEYvr|K*e3F_@X8wNX6uK_v
&F8+|+<ghoqI&dK8#5E``#k{ydQvR9{Y<8xM^e=KAi~OCp3aUDyT8#j1XdARXRPv45c0J#t}vC78C-bta^?UJXwW2W(h$;jJ$Xe@
CKa8T`tp1z3B6#lVWg75hW4MRINAhttE_W>xM#Hj<LQ}Jr8-$JAkxZ7h^!0DpqjD8kxo{k#n){$QpMs?c36RVykP15nTkGdk*jF`
QP@$($<qhHO{E8cmfYSSDGu<;WRAX&_|SduONT`8LTNnZOaKX5BJvw-8rh~^`cWXJYM|}nuUQopugcKlr$jgEr(b&;=<%)jW($s)
8(vHC5I1TL_b@h3o@qfJgB@v@ERg0hDO^9rO2$hCw;qRism3l8)nus`^<y=$X1Yq9V+6x84>d+6ZCOPJ7|J3Tf@Z?&$_S{PM#ys|
0<}Be@3k>ERP_@IvWIf?;kI%aE0Nye#ELDtZZVAnTFD~~9_0GKZP5XKdQ*885RyKi7zz>w_<f%xzITDac9QeSg?3h)sixUJM!U<2
yhV(6-Xq_JXgibAA?>d&0D5_J($J-%l*Y#d+}1nNH&TPTZA4*L%Us?YQjRZxyUMd&j}tRP^e9Wy@C>GGmOK)mN$PnQDJBE!+2yfa
RQ;DmIeMht6Z-5C)x7J(H~oJ0xbuCugSKCd*=8`y9^DQq4+S6mO<DzfGyZBX?+eA$wQ8oZP^cmP-sAMpK5}OR(9O6v4L4z%!TNyc
wuyr*T!{3wK`bun<G80t+&H>@W+wF6r&Dm+FS!nw$AE_;m$tG<Rd(Iuz_PJp!r{qO-BKMCOy{_Lz^}hf6Eym;A{t|a2+4Ev1{n7$
^j?qEnd<WAfNa}X2oXz;k!?NMIVuw>(s?^hdzLC-OKQq30_;04g)c`e)*C()%;FGu$=kZ2I@A9H7GzLTC2M8@880H|PDiW;r{Q)W
^hT=yG>*ckh*|Fqt9b=N_Bi{g<0VzCUp9A7Kvd41d3^CULEUdhBo2a<V(6CS?c@0@#r(T7D|*%HJssQti3#0vB7V#pbIWP3CYr1@
CS?4$EVMkM{?_^;H{&z+k!KR)#NZ{$u-xqTG#|a!%qt(>Mh^4UW0Uj*G}*PwlgH~$Mp9$a=!q^y7`0`_C$*Kd$%4=;Cu5PDw;jXD
RjsxNSiofcka=9CKL1s{D&n@NDhHbnN$@E^hx7;)1M=#zXPY!cP%sN>oswLx5KK_J2mNvn6m;@RyBg?+SGaQ@S91`*K=tvogCF+o
Jw<hQQNQla#9i{wmm1ovLVno#cd}2nY7VFbtISm&0on@lF49U3w3kDi;goHBZX^w9SON&NAD5lR_Yp7-v{QuYwmXd%h{P1+FzHC)
>PE0P6)Ae!ORcRH{ddIx2ke1l*=vuxP<^>{m67+~U6yk2b`MU*97mC>IXlsktyg0V^)p36-u`%m8*?L~C)fMyt1#m*m&N`a)Cxvm
WP)Dok}R`&7^IWs96-@%4(2lByl-{VALIRj#kW1t8qxUauPm=)Sj~X(bt!Z|gA|zW2Znq~eq_dtAl&}x0K-`F{9JrQOh0$iBa<lB
B=a1;er?vphTqpPV^^Dl5dCV_eK$$sv%!tudMTiF41u@*C8N_kq7nU7+6H{J`nBTnkn5!~+k>5OT@9kr&LVgAX1A_6E7HCF^bYrz
Z3$BxCgIk0`ie0SLi5l;3VZ`l2e3`O=Ug4MgY3G3ze`CoN!t9Xy6=QtewpmE(28!J7T{%vXQv!w-0pB73X#qOkqRAFS92Y_R9+;Z
_GD>n>R3xaegIAJj(?ND1iI+X1gOXj%sc#@>j1#&B^7EGI3YAkyl=PU%xDL|0IBG(gB*arzpcQ=g=0+O(SSf$Yb&bJ#~s*|FqHW&
U3Ymk%9U95*Kq=HaKVv*nz+6L8XH+(JZ=S^H|5MA?W|s3Q$#LOFWiB<h)bxdM}sn4nS~hzx+ul|O(2A7)}V}|5O!BON&W;jk3CW$
bD@A0YKwkhhwNHE0=<1u^kdl=*Gg%|v0$xS6TWXe#}boCp0dNSADqsS{bf_d>FUVMP*;J<LuKDva)Tv2!pU8iTSREkq#jXOw87Ji
wkDfE#LoTKBtu<a!$!s_L&5`26zQC?g5x-Kc~7q>ldE4yPs(nwqKK^fWH>4`5h0u)NkO?8q|G4GLm>1qUW;I-%voq`1Yu30#%XVB
PK*qGQfVukzA-02$}$Xjw|b18$q5%XmS=Y%5Mp2i-;Z)-G??>}AS2x4`}0xAw7z(8^}R{NW249Jts*;QUOJ}wt93JWS|jqI7cjb-
8DZ3+5EmE%@eVG?{(d4>UyMAES%|>T$pD!FU9rb&(&ND{CDK&=HL7DM2~t+3tWx;NIbP0P8qtUXjs&*}5&u%Fwj(q#CtFX+84vZG
WbZ^$37bE-uxkej&0m5t#}v!DxATP2#=31p(VJ>=;uT538k#<At>gsVu3kqFOC~=yLwSC4m__@8A(jy|+P0PDRYlk!Me0NwE8cl3
J8xYZAKo+}iIHY*T?kVmDDl;7^RZ57kWr5CB=@;|VgdmyM)Kpfc1T}xO3s<!%9;oT%8Q0TZ+{GOAF&`)T6eVXD^!FWarEQ{HrXDW
IRq4vwyG-wPWXe{Xv{9<cIAcP;yYzpxt&0ZqYbhiDD)RM0ZbG&gKZTcX2GftQw`*^8y|6P9i!PR2v=J*#9;9_7gW;1Y_8ayIHY9K
I8}OORDa8&C<qJpnm*fF4>6cwf<aiQ+5OQR%tZLMolOaWj7rctX%_}+8S_dV`F3%D>ZyL19-iwqK}sTF&6j|{Qh=sG<LJt(c(G2(
E3N$sM;pv%&MNYI_A(CqLvT8wk>-)Bx|2r=<3r)zy;NMjYj-zpWrSnEF5(LHP^HtFkvIsQZvGe&svCAQk7>q3E{XZxf?>XfD#wzO
6><YON=NIX0uYY*mz(96u|i%6M`=LEGdc868<eSN!LMF8DAE_A3k{*f^OJ{?PO4ar2TWJ6^~7x<3kCu)0)&cKTT0fCS$FWcqlUD<
6_Us^m^8m}58Qj`4ii>{raX#7J*!U7nCvy4=VJ}kLh~ua>9J>}eY%CV@G9V5e*y>};9e*6@xyUK3^;aac?#I)w}>9=A6uG25Q260
%JUd9YXbUeM)`7Deq%<m4c+-=wFu`Jr)GaU+b`~yCJm7tXf)Swl+UPB0@E_m--=Q6a-Fkm>&yM0(BKFV#C!H|zwsLa1=|l$y(U_=
jLK!Tb;#>08+IHkZR?nXgk5L)(=>H69SwdJVbvy5&p6o=)AtFRvE{0TmPKagy+<0RE+&Gx2G-MmqjO6B;x7>=U;E%H!U0AFSu&5+
0FtePGj-22L#O`)7XpTI2QrH>=J-&+610Df#P`Nf-~|`lyNE4tWE-grs_Vs5!2xQdD<$DR(9sGB1-nv>d^Jx5uA@m%$oHC|Utziy
OleNUGY@UQZRI3@qz(7z0nr>6Vb712zsnt_T7gfssZ5s7ZcSFdGri0^bT2%n_d1TG^64lLgDw31;gIhov5bYx<gF|IhVwE<<WK*#
L5Kjq(RXvewxHaZmr0rNfwRwP8ZvGCDCv8%X2W4uj?{3P4j*@fxcVkzD-^>XuB=y;naUT95U>Wt7ui<(PRVgLnS(Y_5^sKlh(y!3
A}<Y^tH<k-#TG~i<h{w?Oc~<8qzI;n9Mn7!F{WMD4Adh`Sh^C8#F%k9tSl(IST<gP3T&#$Lr&lGq;rizg+(m6d^$B@Ho6{R6TPaI
I!Fl$TDvI|PXnkW1OD?<)BM#(ikyCW!Z+8QJYwHm6JygAk3~U2%EGTZA^ActKzo*1Rd52u7Khz>k_DY++S5===!}t{|Mvb0#i}5*
ck>+Lvhuw2EDktG!jhXW9&eaO_3EF9d@5ift(IHQmZCPMlOnjGt0%OIJJ*+YJl42?=QI?RSG{6jnEJpY6l{EMbKw?3&`Lk0%Ec0T
P#a@!FVBUE6n<<H@-sIaB*|opnt$o#{k|FTxEz`1a&(UY8*K{9Abm>tO$*X*)}ee`t~fpd$B}pB*eqzRufgV3N&3y1qNzp0YcTvh
J<<rj#g^_`mQ7Z1hn^RoKMW;r?V!Rmt1fR4a4w>PGi|m-v2)Xhe8z?yTyvO2E@U~tI4F9*W)mg=Cy+39=Rs(s%7iU)IOC~bsyf@_
o1deU<Io4o2@D_dN^@R{BkLvr5w}cs(g7!pqeFy3tS!0vM*}DFko(fYC?xe0{~d;+<-r8GX&C@CXNZ7+gGF1@c@wnEeg1H|Qi_?%
PwVL5qhh7g_Yo=SpfxFA`M55Tk_xqTuUY5ee58QzN*0H9*<B-=#a|j5zrFLFSkJr>6^%IX@eDHZiDzkJjb#^~1R7qAXy!TRW5(l1
7961Tky?!+Z1SN?gy|guTl7+>@8#K045a%+6jP|hZiyt@cz0_nnUjtGlcw%se9>>|uy0xr_JWNpZAZc?%bc5ByY(gc)}0?%26{2R
q%NVcD03)r_~)}W7;hN=@R7OY^(`cfIf6*L(7W$35;X&<?=Xu2#d6BddenV`S1d+3^_>iS0x2$6!^x0I<XcjQQMjD*AMj$%AK3e9
H1Li6ZjBpnuLMuf;jo5oA8PW_fEiHByLa)-KJ4|7RX*-@OzE^8I8mmn0^`^D1*0>hiI{fiq~`~QT69CextuGlj?WJQ@N{=95hV*j
=jR&qcXJp4+z^FZ<J*xi06Hkq`K={6Z{dt9PE>HloVw23;eb#Hf)cj{CdJ^F;XKIJjYr9J(C4KuQTi<G(y}7D9&}?=4%9{3L>HN|
g(c3&Os<kZ*Ixv(@B6;8NZ4ezX6dtVKEjt#qZk67uZC}<afrIn=v7dsc~KO;G!GSkIti`IP2t>6usJ0yI>2VLN;W*+D0HP~qQW4R
Z#bLN&J!twe%);#sllu6_}@0F8ox%7z!2egvl6JfG-hKb&nJ*?=Ve*1s|I$2Dry_6F*f8TiIr~iso)xIJ)D<q-#R?NuWH0ql$-2D
4PJ|!^6A2-O^OfK-h|Q^q%Lm#6~e_kd3D!NC6!2A+gj+EKg2%I9349AGBB7*MaU@OK74HfOx8@UnmFW5kBSAt%U=#%*G!a2miE{T
Qs7E~&a-~GJg+jO+%W|^hCf%37Ays?04wBg>HoK)pvX1r+D_D5ySfuzl%j7)UYOShi3)(iDaIL!CV8W%ultr=a(Wj)j0<60$pZ`1
fq(zB#j*mvJ}Q|$N@(An5hy;RsA2jo?sbdUdy~NdQq)jbP<I~&heHswTpkKx?NI&<rpqN<>6XLus1q}9<I_bJ>MELCvP&8U1OYTj
*=d{nD&iW!k`29`s5*tEMY9D6BRJq7PfHoMr3U4L(AHX`bKOy8(&_JF2_4={d&geYaOai_@pTD44Y7`HmejaBG#|QPC2RHG@(-4M
-rruYBX`Za$A$m~>5{kMXRtbFd7R`i2u6*_5DITHW}lTV0zh_g<pq?%t12YB3A($*+FYaZr)b4erHQk716rkUvG<f^w3_2D&TEy>
3LMgFuub(mIF-&rqpmL{LYA&}@!^4B$*~}T<M+?gA)0%-55dEckt8&C3|RM-;b|)h-9ZxC+R+S#m2*w{p!+P@Za~=Dl(iN!xAKmz
y~J`f%q>nE^~W?Oq^W68byhp$x29{frY#`JO1GGa6iRe%yZ3waNM0^jc29{G|B9VtEz{H3=_FiF!&7#HAUH+LE19aBWa<`2n1AK2
;E`iqFU9NC9L_&}EN{xw*%n7ZMrdGi`)l!RZ)`@k00Iru*r2OEzxRsKxdLb=uyHb2|2}>IML9Q@hiqx~Nd}Qc%znlP^L%8MF<sBk
AZ+f`pxuz7S3s7DeJdbG50^+M0oy1D3eG_;2orb!1pFhY^U**sjRWiQm0`mQK?FD7cYbo1#E<k)<zU=wV(?d)O`Vioox6L{*CGQN
6|K8r4+~!%0=pNExT0qQ7SbzGRn}D6YDciAK0VDW`b)4|#aX7_lGqz-vnJ~wAl`r76AcG%MkYQtU*z9vCwweOl}D63$C%cl`;HW{
U2`fhZ-!Rya!3`_Cpof=NxBI;z%Cem{j%nYwCVh&W)`gxpx9Dp%FUUmWF)}8ZV(gSLxCz2jN$fGtnSG}BqO#&_q-AGF<d5Yuni)N
^>FMV2~sgjaR)`P0VA9%a$uuRFlQcR25ee7M-(w$yi;NLE0t5vE&3Aohs@7Q8{OF98H-gDbc<28e5~L$8yLtw!u*Uulg5HLR(2QV
Tym$9)odC-#obm~<yKTzndjy-{6b?MDyok@hxWCp+rcT&z~`!_%Wkfr*QLDTYnu76kQs@qDfXb9)pw{3^_T#WL&V*JZJu(g5_Y2*
#FX-=s6VxzSh<K7U4DiUKFlKv27#l~S0&QTzbS5YmP!Fx!~0-JRVd|4Q6Uf7EupZi<YtGi<1ID;dJ@F?$PFB8pFMvb0se-eMP@+Z
!szUor=P`^&!7DR%@+x!`(Wx){cVmw2wY|mK!tWR0W}gy>^c0SyfyL3%U4<wzIsZ|Aetbammjeju_IE_>cb$xgY$2YI&nkHE~<!b
c}6(hx+@dvbF*H2?!DldaW}^277WK5;7Z)Olf~l?qqV%{L|!*Ol9eBM)3t?A8c|aesuY-##qrUyIl=T`i<7uT;K2*+zijbmoaHT(
n@v}L)`aOJw?RcKB6EyH_qG_5T}f{y0B}CENG~nw__Skcnjukzm(Pajuogi|by=hJyCEnq4)I775Q?wA=C!=eWaM7t^gC+#KxwjZ
v*8EsIN0tYoj6xTGQNR<0`H?4?c~c8%)|jh_17c^mpS?ZK)2vy{%ApVz4>DtuS0vjjcy0@3BD0-agdWfM@ci^{4fh&IPR6+_+uy~
!+B9>3G(g$N$WUNBI`!`AW4>^bRF>cAFHPkvV+#XQW^Y~mkqaGo}b9s-xZ2!t8wUWnm(4}P`065E-<BkF|v;p)LAt?is~e`XqnN|
q;Y}sJ|Y20(!eIHOprPTilJr{+wI$gl4@Id{%OLyI(mE+)~3ZykpPEqIxqg~i#BJ7Rmgw))j8l{bIQKtv@9uujDki)g#l;7j*aL9
5{%8n|4ix5%y2JKVvO$SLdv3X(ofj~=mM@`puX#V8Z~pkS#=Y5W4h2s{Cva{W|+)Qq}i5<FceVs9pgcPY=f_zF;YNwA|09zKAhN`
0sQPte_`f@xVoZap03xYP1U_6qc!4#FN>D!r$&NSO}lkWRA_a-*8l;3%8*1{a)F}_TzrM}z{I4ER*1?99<qtOEY7Izbr)jj<wtrE
(bVZs^^Vr2sv8C_Cp2O=y}^I-`CfjDD^+53lkJ%c@E6+VJEYHte5ob_;6e{af6fLptF^GPcnwjgrZUU1(%n`MIEO6f{KMtcH06(6
vUL%p301~SExi-^e;1}?CJAG<PozXM0)lU}s%^$2f=Hjcq@BfxlN$|R<y=K0UbsVWE*naA=$%%(s5pK)PaVZuOmFX@cirdyrra;J
iOH_zSHO2MreQ3a874xoZ89z%ei_Q@{Xf!79!kh*@TKG9P5dEi!Makl#P~^*AB&=sReBR&u%#DngiRuH_>6=v0$6*mR-T1=GyPBG
4Nm3lN)U3e`><9On|(!XrPzi?r}SGGbU}=wWuL&K$|%A}zm50zEVIK|PsL+8crybbmWb6h8O7uBc$u3!zMPfv!74t<p8mwue%BD&
%C^qMxJ~AGey0yA5{4vs^}3szTPBwXD~)P$##sUf`y}d;eKSHu?#XJ^ddNl!gz#i_ouzxixBI6EmiO4TIGT42CHmo70DacI3RU^5
|C0TWd$+U}HSEVLSas+nfju~0#Y<<=npbZaEc&UY|LIrj4A{eFU>&$YsyHQf{Pg<8WW}=}RhkXU<ip=mwIXOl*6vi+j>l4ymQL6<
n2FDP@7TKdyM3vF<H(X7aMBKP9v<4SWg~XYT(Rb&b7ceJLmTH8GulYAxco(n#tV+ZsKl10TQ2E+fZp~zR1Koa&GOK;FrN#+Tr#cm
`rHasvy$QQ@$80+_Frk`Svug3Thft06-8_QSHNyeh);F%0%kyJe7*HPzkM^@`zgq$CdHp=Ih>bE$wzp&gc4VLMzmjug_BZ)`r;w$
+W%)?{&U}FoNCPs9ehQje?K2#3OqJ47G~_^y)iTOBg%GlK)wAG<D8;Rs{&0RMlfAm=SVBtyOZ#YpR)*AD1PenYBm?UcADL@7p}q>
dzs1S)oFnO)E}6BOWffNLI!3&K)b$Jg<*%_*3C-U54OFIi9$;GyxHy<V^sa0iF8}{s021RV0eU)AdFDNe41PTM)POY*;Y66@!wZ-
<{*(W|6UI*M_8HYK*-z=sqVrFLGV$o;u<?2z;aG@iGF^d<t0f3#(O|Mog%u3dItkqiJofzNwiRwa(S+vZEVkd@GW-bHfL`%R^EFY
u%P7InY_c988nMyE~RWAD_%sh)vW!P578nxUYTX2z%H}`xw!RyvIEcL&|={-$?sNuMvEpDsj`veGpAT$=HuAj1X45x5Dmk=Z-UWG
hwAY8yx?)5F3P>?%@A1DdTeebWxlLFEf2J~CHMdUIx7`Lv4xJW00G;M0sHI&%pjHDvBYQl0ssI200dcD
"""
raw=lzma.decompress(base64.b85decode(b''.join(PAYLOAD.split())))
assert pin(raw)==PACK_PIN
obj=json.loads(raw);args=[a for a in sys.argv[1:]if a not in ('--full','--check')]
assert len(args)<=1 and not('--full'in sys.argv and '--check'in sys.argv)
out=Path(args[0]if args else 'c34_v2_recovery');out.mkdir(parents=True,exist_ok=True)
for n,s in sorted(obj['files'].items()):
 b=s.encode();assert pin(b)==obj['pins'][n];(out/n).write_bytes(b)
 print('RECOVERED_SOURCE',n,*pin(b))
print('C34_NINE_TYPE_COMPLETE_SOURCE_CAPSULE_RECOVERED',len(obj['files']),*PACK_PIN)
env=os.environ.copy()
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):env[k]='1'
def job(args):
 name='_'.join(args).replace('-','');log=out/(name+'.log')
 with log.open('w')as f:r=subprocess.run([sys.executable]+args,cwd=out,env=env,stdout=f,stderr=subprocess.STDOUT)
 assert r.returncode==0,(args,log.read_text())
 print('COMPLETED',args,flush=True)
 print('\n'.join(log.read_text().splitlines()[-3:]),flush=True)
if '--full'in sys.argv:
 for n in ('c34_catalogue.py','c34_transport.py','c34_terminal_brooms.py','recover_parent83.py'):job(['-S',n])
 with concurrent.futures.ThreadPoolExecutor(max_workers=3)as pool:
  futures=[pool.submit(job,['replay_nine.py',str(i)])for i in (104,329,344,366,375,482,554,578,581)]
  for f in futures:f.result()
 job(['-S','replay_nine.py','assemble'])
if '--full'in sys.argv or '--check'in sys.argv:
 job(['-S','verify_nine.py','nine_type_certificates.json'])
 job(['-S','review_nine.py'])
 job(['-S','type366_actual_fans.py','nine_type_certificates.json'])
 job(['-S','attainer375.py'])
 for n,p in sorted(EXPECTED.items()):
  actual=pin((out/n).read_bytes());assert actual==p,(n,actual,p)
  print('CHECKED_OUTPUT',n,*actual)
 print('C34_NINE_TYPES_650_BROOMS_140132_INTEGERS_11244_PD_BLOCKS_RECOVERY_PASS')
```

**Observed recovery.** The source tree was run from an empty directory: original inputs and the83-type checkpoint were rebuilt, all nine coefficient groups regenerated, and all650 records assembled byte-identically. The decoded capsule sources matched those executed. The final capsule's `--check` path then reran exact verification, the independent retained-row comparison, actual366 checks and the375 attainer. All ten output pins matched. Observed terminal markers were:


[Encoded source block omitted; the code in this passage is incomplete.]


**Remaining barrier and continuation.** No broom or weak-wall obligation remains inside the nine new whole-type exclusions. The74 retained types remain unexcluded; surviving combinatorial domains do not establish physical feasibility. The next small direct genuine-facet targets are:

| Local C34/V9 type | Complete broom orbits | Remaining joint roots |
|---|---:|---:|
|385|100|51|
|412|108|90|
|454|108|90|
|596|110|48|

Start with literal385 in the new374971-byte checkpoint. Reuse the eight-escape actual-moment method, trying the three apices at broom positions `[0,1,5]` before broad nine-fan searches. Complete coverage and exact certificates remain necessary before removing another root or type. The ten-vertex slice and any stronger global complexity bound remain outside this result.

For convenience, the reconstructed coefficients, all sources, all ten pinned outputs and the full handoff are also in C34_V9_NINE_ACTUAL_FACET_EXCLUSIONS_V2.zip. The complete inline capsule above is sufficient without the archive.
