# minimum-0237

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_FULL_CUT_SQUARE_ALLROOT_NONZERO_PSD_V1

## 1. Result

**The entire requested physical cut square is excluded, without a metric condition-number restriction.** Every one of the **48,790 labelled rooted primal trees** is infeasible for every nonzero positive-semidefinite matrix on every shape in the closed square. Consequently, every genuine interior member has **at least two strict unstable vertices under every SPD metric**, including metrics producing incidental weak contacts elsewhere.

The certificate uses four closed quarter-squares: 290 stresses are valid on the entire square, with respectively 5, 8, 6 and 13 additional stresses on the quarter-squares. The actual uniformly filled body's volume and centroid move throughout the calculation. No covariance cap, independently chosen inverse metric, or frozen centroid is used.

For every complete rooted tree, an applicable positive-weight stencil satisfies

\[
\frac{\sum w_{ij}D_{ij}(M)}{\sum w_{ij}}
< -\frac{\operatorname{tr}M}{126976}.
\]

The exclusion also holds for genuine same-labelled-lattice bodies within **uncentred matched-vertex distance \(2^{-31}\)** of the family, after recomputing their own volume centroids. An explicit eleven-parameter cylinder with transverse radius **\(2^{-34}\)** follows below.

This resolves the parent's actual limitation: its unrestricted statement covered only T0, while its all-root statement required coordinate \(\kappa(M)\le3\). The result is not merely an enlargement of either sector. fileciteturn0file0L994-L1000

## 2. Exact physical domain and actual moments

The outward maximal facet cycles and true edges retain the parent's literal labels:

```text
FACES = (
 (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0),
 (1,2,8), (9,8,2,3), (9,3,4),
 (4,5,7,9), (6,7,5), (7,8,9)
)
EDGES = 01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.
```

For \((x,y)\in[0,1]^2\), set

\[
\begin{aligned}
z_0&=(1/8,0,0),&z_1&=(1/2-3x/8,0,0),\\
z_2&=(1/2-3y/8,3y/8,0),&z_3&=(1/8,3/8,0),\\
z_4&=(0,3/8,0),&z_5&=(0,1/8,0),\\
z_6&=(1/32,1/32,0),&z_7&=(0,0,1),\\
z_8&=(1/2,0,1),&z_9&=(0,1/2,1).
\end{aligned}
\]

Thus \(b=q=a=1/4,d=3/4,u=v=1/16,\lambda=1/2\), \(c=1-3x/4\), \(p=3y/4\), and \(\rho=1\). The entire interior is outside the old basal box, already because \(q=1/4\). These are exactly the supplied new-domain coordinates, not an incidence alias. fileciteturn0file0L1233-L1267

For \(0<x,y<1\), the body has the displayed genuine 10/17/9 lattice. Boundary points are the actual positive-volume lower-vertex limits with refinement labels; they are not counted as additional E17 bodies. The labelled polynomial tree certificates include every boundary point.

Writing \(V=\int_P1\), \(J=\int_Pz\), and \(g=J/V\), the exact uniform-volume moments are

\[
\begin{aligned}
V&=\frac{31}{256}-\frac{3xy}{128},\\
J_x&=\frac{679}{32768}-\frac{3xy}{256}
       +\frac{9xy(x+y)}{4096},\\
J_y&=\frac{1933}{98304}-\frac{9xy^2}{4096},\\
J_z&=\frac{63}{1024}-\frac{3xy}{512}.
\end{aligned}
\]

In particular, \(25/256\le V\le31/256\). The released carrier loses the single genuine tetrahedron \((A,z_1,z_2,z_8)\), with \(A=(1/2,0,0)\), of volume \(3xy/128\).

The standalone checker independently verifies these formulas as whole-square polynomial identities using the genuine apex-0 fan:

| Tetrahedron | Actual volume |
|---|---:|
| 0128 | \(3y(1-x)/128\) |
| 0982 | \(1/32\) |
| 0923 | \(3(1-y)/128\) |
| 0934 | \(1/128\) |
| 0457 | \(1/192\) |
| 0479 | \(1/96\) |
| 0675 | \(1/768\) |
| 0789 | \(1/24\) |

All eight volume polynomials are nonnegative on the closed square. The checker also verifies the first- and second-moment subtraction identities polynomially, all 34 facet-incidence identities, strict positivity of all 56 nonincident support polynomials on the open square, and a rank-three incident-normal witness at every vertex. Each listed edge is the complete intersection of its two stated maximal facets. Integration diagonals never enter the tree graph.

## 3. Exact stress certificate

Put \(X_i=z_i-g\). For nonnegative directed-edge weights, define

\[
D_{ij}(M)=X_i^TM(z_j-z_i),\qquad
G(x,y)=-\sum w_{ij}\operatorname{sym}[(Vz_i-J)(z_j-z_i)^T].
\]

Then, with \(W=\sum w_{ij}>0\),

\[
\sum w_{ij}D_{ij}(M)=-\frac{\operatorname{tr}(MG(x,y))}{V}.
\]

The weights are stress multipliers, not replacement physical masses. Every row uses the same actual \(V,J\).

Let \(e=(-3/8,0,0)\), \(f=(-3/8,3/8,0)\), \(k=3/128\), and let \(s_i,t_i\) denote outgoing and incoming total weights. The exact cubic correction is

\[
B_1=\frac{k(3s_1+t_1)}4ee^T\succeq0,\qquad
B_2=\frac{k(3s_2+t_2)}4ff^T\succeq0,
\]

\[
G=R+yx^2(1-x)B_1+xy^2(1-y)B_2,
\]

with \(R\) biquadratic. The generally indefinite mixed coefficient is retained exactly:

\[
[x^2y^2]G=k\left(w_{12}+w_{21}
-\frac{t_1-s_1+t_2-s_2}{4}\right)\operatorname{sym}(ef^T).
\]

The cubic and mixed identities are checked for all 34 individual arrows, hence for every stored stress by linearity. No power-coefficient PSD shortcut is used. fileciteturn0file0L1141-L1163 fileciteturn0file0L1222-L1231

For a subrectangle \([a,b]\times[c,d]\), substitute \(x=a+(b-a)s\), \(y=c+(d-c)t\), and subtract

\[
(b-a)^3y\,s^2(1-s)B_1+(d-c)^3x\,t^2(1-t)B_2.
\]

The remainder has nine degree-(2,2) Bernstein matrices \(H_{ij}\). Every accepted stress satisfies

\[
\boxed{H_{ij}-2^{-20}WI\succ0\qquad(0\le i,j\le2).}
\]

All nine shifted matrices are checked with exact `Fraction` arithmetic and three positive leading principal minors. These are positive-definite tests, where Sylvester's criterion applies; the separate semidefinite rank-one corrections are checked with all principal minors.

The Bernstein basis is nonnegative and sums to one, including on the boundary. The remaining corrections are PSD. Therefore \(G\succ2^{-20}WI\) throughout each certified closed rectangle, and for every nonzero PSD \(M\),

\[
\frac{\sum wD}{W}
<-\frac{2^{-20}\operatorname{tr}M}{V}
\le-\frac{\operatorname{tr}M}{31\cdot4096}
=-\frac{\operatorname{tr}M}{126976}.
\]

The locator's numerical congruence and scaling do not enter this final inequality. There is no eigenvalue-ratio restriction.

## 4. Complete all-root coverage

The verifier enumerates every nine-edge subset of the 17 true edges, retains exactly 4,879 connected subsets, and orients each toward each of the ten roots. It checks 48,790 distinct directed tree masks and verifies that every primal complement is a connected eight-edge dual tree.

A stress covers a rooted tree only when every arrow in its positive support belongs to that same complete tree. Favorable rows from incompatible trees are never combined.

| Closed cell | Whole-square stresses | Additional cell stresses | Covered rooted trees |
|---|---:|---:|---:|
| \([0,1/2]\times[0,1/2]\) | 290 | 5 | 48,790 |
| \([0,1/2]\times[1/2,1]\) | 290 | 8 | 48,790 |
| \([1/2,1]\times[0,1/2]\) | 290 | 6 | 48,790 |
| \([1/2,1]\times[1/2,1]\) | 290 | 13 | 48,790 |

Each cell has exactly 4,879 covered trees at each root 0 through 9. All 195,160 labelled tree/cell alternatives are covered, including shared walls.

The final certificate contains **322 stress/domain records**, representing **321 distinct integer weight vectors**, with **1,420 positive weight terms**, maximum weight **63**, and maximum support size **8**. It checks **2,898 shifted PD matrices and 8,694 positive leading principal minors**. The 290 global stresses alone cover 48,566 trees; the local records close the remaining alternatives on every cell.

For SPD \(M\), every non-U vertex has a nonnegative true-edge escape, and

\[
\|X_j\|_M^2-\|X_i\|_M^2
=2D_{ij}(M)+\|z_j-z_i\|_M^2>0.
\]

A unique strict U would therefore supply one enumerated complete rooted tree. Its contained stress would have nonnegative weighted arrow sum, contradicting the strict bound. This proves U≥2 without any S assumption or weak-freedom premise.

All 439,110 raw complementary rooted primal/polar pairs are consequently excluded as well. Those are labelled pairs on this graph, not canonical-orbit or whole-incidence registry increments. **No complete one-sided PSD tree survives on the new square.**

## 5. Actual-refill collar and eleven-parameter cylinder

Let a genuine uniformly filled body with the same labelled maximal facet cycles satisfy

\[
\max_i\|z_i'-z_i\|\le\varepsilon=2^{-31}
\]

for some reference point of the closed cut square. The reference diameter is less than 2. Expansion of the eight fan determinants gives

\[
\sum_t|V_t'-V_t|\le33\varepsilon,\qquad V'>1/12.
\]

Comparing tetrahedron centroids before dividing by the new volume yields

\[
\|g'-g\|\le793\varepsilon,\qquad
\max_i\|X_i'-X_i\|\le\delta=794\varepsilon.
\]

Every primitive changes by at most

\[
(6\delta+2\delta^2)\operatorname{tr}M
<\frac{\operatorname{tr}M}{253952}.
\]

The last inequality is checked exactly. Thus every covered stress remains negative with mean gap \(1/253952\), and all-root exclusion persists. This is an uncentred-coordinate, genuinely refilled collar. Reference endpoint limits are permitted; the perturbed body must genuinely have the stated lattice.

An explicit eleven-parameter domain is obtained by taking raw cut fractions \(x,y\in[0,1]\), setting

\[
c=1-(1-b)x,\qquad p=(1-q)y,
\]

and independently bounding every entry of

\[
(b-1/4,q-1/4,a-1/4,d-3/4,u-1/16,v-1/16,
\lambda-1/2,\sigma,\tau)
\]

by \(2^{-34}\) in absolute value. Form the compact H5 vertices with bottom scale \(1-\lambda\) and top vertices \((0,0,1),(\lambda,0,1),(0,\lambda,1)\), apply

\[
Z=Y/(1+\sigma Y_x+\tau Y_y),
\]

then refill uniformly and recompute the actual centroid. The matched raw-vertex displacement, including projectivity, is less than \(6\cdot2^{-34}<2^{-31}\). The denominator is greater than \(1-2^{-34}\) on the entire released carrier. All basal guards remain strict for interior fractions. Positive-denominator projectivity maps each raw edge-fraction interval bijectively onto the physical interval, so no physical cut fractions are lost. This whole cylinder is excluded for every SPD metric.

## 6. What was tried and what the failures mean

The exact literal parent unit needed for the new calculation was executed. Its previously unobserved terminal pass was now observed:

```text
H5_CORNER_CUT_PASS 150 216 4879 48790 439110 9 2
REPORT_BYTES_SHA256 9622 4c81cf492b619b919b2ee3677e0482f547276c5290fec2242a9313ef5753bd73
```

The new locator sought common nonnegative weights for the nine coefficient matrices of uncovered trees, using eigenvector cutting planes and `scipy.optimize.linprog(method='highs-ds')`. The LP only locates weights; exact rational matrices determine acceptance. citeturn655463view0

The first whole-square pass produced 633 exact stresses covering 48,734 trees and left 56 locator failures. These were not accepted as infeasible stress cones or as feasible physical trees. The four quarter-square searches added respectively 7, 8, 7 and 14 stresses and closed every remaining alternative. Deterministic set-cover reduction and reverse deletion produced the final 290+5+8+6+13 records. All retained records were then checked with the stronger \(2^{-20}\) coefficient margin rather than the discovery margin \(2^{-24}\).

A fresh run of the complete preserved locator, including a replay from the handoff's recovered sources, reproduced the final certificate byte-for-byte. The whole-square search failures are therefore limitations of that sufficient robust search, not surviving common-metric geometry.

At \(x=y=1/2\),

\[
V=59/512,\qquad g=(601/3776,953/5664,123/236).
\]

The checker preserves two exact nonwinning physical controls. For \(M=I\), strict \((S,U,H)=(5,9,12)\). For

\[
a=(1,2,-1),\quad\epsilon=10^{-6},\quad
M=aa^T+\epsilon I,\qquad
N=I/\epsilon-aa^T/[\epsilon(\epsilon+6)],
\]

strict \((S,U,H)=(4,2,4)\), with U at vertices **3 and 7**, not 8 and 9. All 68 true-edge primitives are nonzero in both controls. The second metric has condition number **6,000,001**. These recomputed controls are not attainers; they show that the unrestricted theorem is not secretly retaining the parent's two fixed unstable apices.

## 7. Autonomous recovery and observed pins

The complete lossless unit below writes two readable runnable sources:

```text
h5_square_allroot.py   19717 bytes
SHA256 0938aa7d4fcc680c84963e489ba623b8468702950d13287cd7c35d767ef69aba

h5_square_locate.py     5774 bytes
SHA256 c3311316cfb7f735e08cb88abc3ee1a815327baa5708b9563ab050a9c98f2e53
```

The first is a standalone standard-library verifier with the complete literal integer certificate embedded. It reconstructs the geometry, actual moment polynomials, coefficient matrices and every labelled tree. The second contains the full numerical discovery, rationalization, four-cell completion and deterministic reduction. Neither requires the old parent implementation, an external stress list, a sandbox file, a research connector or omitted helpers.

Save the complete unit as `recover_h5_square.py` and run:

```sh
python -B -S recover_h5_square.py recovered
```

Observed execution used CPython 3.13.5. Exact recovery requires Python ≥3.11, standard library only, assertions enabled. Both the standalone verifier and the lossless recovery were actually run in fresh directories containing only their source. They reproduced the certificate and report byte-for-byte. The recovery extracted from this handoff was also executed successfully.

Optional independent weight rediscovery uses NumPy 2.3.5, SciPy 1.17.0 and single-thread OpenBLAS; the observed NumPy build reports OpenBLAS 0.3.30. All tolerances, rounding scales, initial directions and tie-breaking rules are preserved; no random seed is used:

```sh
cd recovered
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B h5_square_locate.py rediscovered
python -B -S h5_square_allroot.py verified
```

Different floating-point builds can affect locator choices; exact fixed-certificate recovery does not depend on them. The reported stack's fresh rediscovery matched the pinned certificate.

Expected and observed markers:

```text
H5_FULL_CUT_SQUARE_ALLROOT_PSD_PASS 322 2898 8694 48790 4
CERT_BYTES_SHA256 10349 e5f14ac7c64adc4ad085ac327f74908fbd8f81893dd2a2d15a06d733f565d82e
REPORT_BYTES_SHA256 8718 787b0d2b4c8e89e9742dbf90d39adcfa23cc2208f629fc281bcceca2fb68dd30
MATRIX_STREAM_SHA256 48f8c23b16298055e9adaea14adab088842bef3ba162d4dd6a2f604d415a6bb8
H5_SQUARE_LOSSLESS_SOURCE_ONLY_RECOVERY_PASS
```

The decoded two-source archive is 26,102 bytes, SHA256 `abb4db93e31bf7dcf4fba4e951dca7f81de5ce277ef3030a5414503c48bb43eb`. The recovery unit is 16,570 bytes, SHA256 `fbbfbca3f5802e3aa9966ac9923a8d6ab49e20b4c70ddde5a02724989dfd7d1f`.

### Provenance limitation

The entire 324,327-byte supplied journal was read, including its literal parent. Its SHA256 matches `a122ad4954a2c938df9dce4f31835fa21239d1b661a4f0a5a7b77afb35c6b6aa`. Its metadata names parent `minimum-0235`, SHA256 `0dc44267ff36d88c52f7218626cf8d916041bcd87f5c0a37cf35b35b9af9fce2`. The literal Markdown tail extracted from that parent's heading through EOF is instead 32,943 bytes, SHA256 `d272d7f28fa56a0210d58a38dadd3768db6070bc49df3de47d53f94b41e6a54c`. I cannot resolve this serialization difference from the pack. The printed source actually executed is 13,249 bytes, SHA256 `6e21a670bf70b9ee7598e7deb343afae62d77a59d59c7f5cf981cc8faff93a2b`. No coordinate, incidence or mathematical alias conflict was found. The new self-contained proof does not depend on resolving the old envelope hash. fileciteturn0file0L984-L992

### Complete lossless recovery unit

```python
#!/usr/bin/env python3
"""Lossless autonomous recovery and execution of H5_FULL_CUT_SQUARE_ALLROOT_NONZERO_PSD_V1."""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
if not __debug__ or sys.version_info<(3,11):
 raise RuntimeError('Python >=3.11 with assertions enabled is required')
ARCHIVE_BYTES=26102
ARCHIVE_SHA='abb4db93e31bf7dcf4fba4e951dca7f81de5ce277ef3030a5414503c48bb43eb'
FILES={'h5_square_allroot.py': (19717, '0938aa7d4fcc680c84963e489ba623b8468702950d13287cd7c35d767ef69aba'), 'h5_square_locate.py': (5774, 'c3311316cfb7f735e08cb88abc3ee1a815327baa5708b9563ab050a9c98f2e53')}
PAYLOAD=(
 'c-pOf>0;uz(&+#D6y#*V20^ohKtM^z3R!7F_DP714LE=ew%M}uv)?L7HYQ2;%zWqcbYojfNh+0Ul{9bv>8v-L;YhLdhSKZVmgU9='
 'v;S=VXL;$z$gzK@hWSG`$DzT@?O0~|FY~Ye;C}~GrRj#CLJVt!2JqVoS!T%X=%Mm@s5R>KLW9oCF`7y*<W8(ubL572Gx5;51?3D|'
 'iwzXporN@gpqrX*HVxg0bMSweE!*mcS~j#|Sf&#)`UA^$Lx&<Eq&T5NQOIz0+qJBoU#MyIq1OtlNU&?#sOgHreZ}nr%ZcOxB=-!}'
 '%c;WWU#9p_6-UozNT{PYScZgN9LppjX9mDuApr`uLM9-g(a>~t)NV9FmW|o*v2HuiiH2detWYr|rAaa=Z~kS5Y{hW&P;F$oMqfX$'
 'ZOfLzRfgcu7EQ;K$<V}rekzUwLu2FDO-1eLTF7uhwmuvgwyuTczs$qZ-oYi6q%2t{8ImR`k|YV4NI9}W5+n(48zjq8l8~2^2{g|C'
 'NO_Wjq%>sZp<)J}833|D^6-|0=Q^vLgKuc(VE+i(aYuumE;)b{U6bAxzNFTJ@km+^k`YbHt3BP6TJoceRYTwWX#s*-A;S!@{<BX5'
 'KW)Wq>k_Xme_-uWt#)zqsb$F^FEXp75EZMj-f<}81rsC*a-jbzQDoMMgG2hJZ*nMIR<cW22Xu4P*KNhsCDxVC{e_uT%$f9$hDxda'
 '`_X<Kp3H}!`vds+%j6Rt!V)YAU?w-92O6$4R&fkTDOPdJDjvqiN^hh)5{|N-08-!tkYbY$1i|JNXL+5?aaPQ$AQCqF8(8-yA&`vN'
 'C5KW{^iN>4o`5nHQH1{<N(QB3B3|ahOM4X;lKwL9KUGfr<C>b@3XK&urJJ_yj%;8v49GM(V-==khE-mT0W0KHalWe(`(u^9<N(Pm'
 'R&gRzUIi;CqNHZI3(%cWUz$e#1iNWl&SH-w<stbPQ6Ex|F$I3$E%`{qTLRM(JeP>KB&H>Kt^n%Hz8RyKM+L|f%Dy~CReV$6P5zPk'
 'H%RX*zlDy#J<#y{S5TdAko*m*ZEM1Tz)KMI{r+!zg|onV*2R%`{hoEd_UxZ_cKl6aIQh^iNdK;XnhvDF*t|(`$znP(5)&4)2M1>q'
 '{-P+D(~lHO%8|%Rgk`=wMi9^!oOi#B$dnO!cL~<w_x$H?IZ~3C@>jH&9u5YMCe7yyInlR03sQkG4WJZ0<Sm-`UFWcz$+&is2_#;T'
 'kw8$AOWw?odB^^Bzx<JXMgbyVEAgc-q9MZ^iz%JZho0fM46+<$uN8d#N<cWdUkD9Bgu2w!r>-Z5=GiYec$mrwr(C%(fnS1O6n_YQ'
 'V*Me-H~7m6(1-Dl;annM5-atkL#%CtZvd(A4+hE*pbP*tjSastG0b9(%K?H7q8S#zLwfUZVKq#=1!VPg({-df*8Vj`#$Pz5OaKr$'
 'k}lL!^j@H9t`e~BL01!)(%NiVpedOn-5b|SkaoE|jU~kZUxl2xgI>>(ASFOzCs1s^u%BoWM0Np|Hfa)#zOtGViVGXW2C5B&^K1BO'
 ';ukzMrcC_Eva&)_PdvJI=$r$My_VU8ynfGIpiYef`*w)KzvdM-YZN$djX>_0j78z=D4hV_Kn@-g5L1&M8K@{D_MmJ%MS!bLexwql'
 '#>$KCU2i4kGj>gmNj(J$JewC#t@|*49o<z(PazJQ7~--A!=y@vL?Id(kufwekPZneEElje6y#|V|AL;_G#TqD^R^R3wU}hOOQJaR'
 '-;|;z-bb+9@HrOG(GN8`{-G3;K@ha36e*_Mfo5YzR8VSBbFn`^BST_Gq-1O;<2R>mm~uO!v3z_}M9C4nk3}k1kzok@C4rboG6dc&'
 'Xe)fIuYzs7;w;@^DKJ_@xn$IdyaItmU3erPgXIchG=0Ma24%`@PCWQ9mB}9+B8cRbbi74(N3bk5QlfVNv7l3+!8@ekl3Zx<k2L$J'
 'LxCJF%`S~01?z%#TS&EaD1lV#^`gru_Buh16F?3LI$xl3Qqhd2E8WpMQlcfIQ=PPEi_~eIbZM7dCn&2;1pxR5c!QaeJ=*G9n%<K-'
 '1b7G|C3pf|O=VCkXFfV$a;Gr2f-dOHn`g#TI}hQzFmON|Inq3Qm%@)o_)`M!dKg#l9q2}jnKR66VJ3jO#60}l2R)dVk?~o_Cr|f*'
 'EmoEpqld3<_%Q-nUEvx(t`p(M7+Zr5HhG-jZQ@G2WL4ODz9h_u@aNy_9gc)xkG(DgR{1NE7F6Pk8S_&J9F}y<ThoQ_R<vMrGFe>O'
 'u07HlEv2b@TsL4=I3OYK&{jz%zGu27^%>vYLkl{My++pg$e19$rvhny$IK<l7F2?<s}5tOre6%xL_sE}MJ5PNN;^y@F-9NKdtes_'
 'a*LfWx=KR!>CAC$9lCnQ#y`=GcE@$Nef_;^7@I^S={katAC$+~G5p987!n9m^)beh)yKb8qM{xM6+x&z2t|MZprB{}8H%v12p5&2'
 '=PXtIs+TICM8{udvj@lwRW}(6YK0mN!!+DR17^3^B2$`>J^5)khUvJ9*#ygnROL-95O30Hycus=gPFtzi%9o!-abOYn=$2+@rJW1'
 'Z{qR=12we6n(pgv$I?XWraqCHJ%?z#)mI81l3aL2XkDl{mW9F1q?;BuTpcKzX*%PNf|#mTe<+Hkc_UFdM2+&!1-cvnSd~;6@&wdP'
 '4b>$r-Ud4F5+=-|W2_<Csm8Ip8UkrFY}OVPZTdYh^|t7NuUztKFr3&p*tY1GX!}F<K{z8dFbGe_htFsX`|Fppzb%MGqA^VL3-(97'
 'FIai|@KC`#BHwjs(^oA38$FrR+ZT)((Jpz3_B^~v;#>Cc7n%GPgREav^v~}tav;qZe~$u?(?1R+W*3X%18d?HHF=i>uLzK@Net7K'
 'nY1v4()CKKQd0g#Cj=m`^fe+782UnD`tbXn0mV{|98pwp#galn7O>RDAQd7;WCqsSpYad9yQPA7m}h1)`2m9Kx>WO1QT4!7;U%!7'
 '5<zI+nYUF~O8}eC5w^(YXRbMZwwOzvmtdqiuHlYc9e@YN@&z~y81w%Ok^?mjQ*Wp}tJwu{=y6}7T2rChqYH`nZ(OJRTj_rLC+Uu8'
 '`<DX#HYng1>dVX;@x;22^|ui$^F_oj<oe?Nh<+=7AjcZHpbqs_O#x*d>1FaQ!)FYd(pTmmFq{9h%8RJ7o1}fm>zkC0K&yc0C_qAd'
 'qkS-w_~?D4Vy)EIS}9&D6{ywXwLDbA+S6@Q>Cr!T?F|w?D18ItnK8q*((fzOs~nSf-(rEDruY|YdakL!DmWr(SQr#L8%vViBwzY0'
 'BMEl0pOKP3RZEc+&lO{2eOSbWH!4vL{Tp5b?483DwjtO3fv)9(Hl=DzDQGjQ#hMFdiUP*YT$gQvk;Amv>69u_Z5p{P%x1J1)n=T&'
 'j(~LLOY(?JVa?63P1Q0-4(fo=eW(^mM`kl1yGROcn_C&tfLbBIfvoA2K@++7DkD0$CJHc)jtIvQgBlz#s$fQurdWSpio&5RR(Oql'
 '48-CO`hcs_0N4-fCtLRP!Siv50wUBh_te<>Kv!Iv;!M5F41KQBB<I{3-RN^Ur3P|d{2ZtYBP!#74kh#o0sm6~8SFKMuX03WybyJs'
 '0k8NDYPOPOA52{E?#Gn@#+{@x8_^V9=YV5CCrJU$Il>Y5azUN3Oon2f&k*lpT}%TvpwyAkbA6Wv=hJ1+s{1{L2=5fKW)1<yD_(Kb'
 '>XdnNXXw5t2j|i&PHS_$mxChya`0HTWgB4Xfhg6rw(by&+;RIrd!Y{xk6(RapXQfU+l1247Y}<cU;#kFi=SX%=LU)mEzvh@ViSKp'
 '3LwXuUHX6@2zJsjdU}W@a%GjW_xQjXNQ*L^x95AWUYK@jcx`O*2RgzG-p0IV-0zBJ4=*GyQPUHB=a#8|wiIBp1hj8Fdfd%wEK!Cw'
 '52a1rbVfqa0%@Q-G*Q3;x&|);#jqXf8Ctsj#ihxDJS6X{>tceE38L$uEMT+``?=u%Vy#3OdkJZpa3dTXKIo61;z<Zl_mHLQK^qKF'
 'qG`Y;bAE71G@U1!Mr_tH*2LC1bC@F{FZ=UjFW6;#id>g248!(KMAuyai!EbETo*c$XLUK|U~n9DQI;%fOKjkT7a=Sk>Pea0MxNkL'
 'f@IS9WHJ$OV|=aQO`8{*2F>M+YbL^mrk?NO5Iw-Mc*unXn;In>Wu6<TBp3Ds$HvckN)}ufBu<;O<++7C(4;*fWHjjvft*uxET08S'
 'obwX>zH~;;VSE)Rc6;kNiyY|{Kz?#U?bA2LWj4`nzP&|fZ6Ba=YyIVs8`6u>JRVg=^I>51^Z+COZ=C@h&+r$ykcv3)2H5E^_XTg&'
 'Tc_Lw*5Pjb&`_aXfSE;Jc(+J9`6=8PjQ>g!7LbY5P7)S41~><R6_(1-!Ww*NG0dD}=XgRp`AEDh4@F*ELk013B~WjC<A-3;VOTo*'
 '4}jLkVnTE&fMHgGQbVY#98_zLX>UP!kPaTO^*Jc7Cjw53!6^p<wF|TAuX+SE7C@L5FS<zfA6^KM$H4>e3rq;SK5TBrl8-_$_69Z&'
 'F8h4qV4k)a;3k)H6dzY|3?F5TQh#zMj&UmktRD(Xjl#O2Y`N7_q)ppokM5B(3M5a@`GipROFnr~_Jc8MKBjNzTK-(^z^jJXB?8Hx'
 'XImy$^om^4OH!ug&k$a9+iDDKqYo<Z;w}P)-~9!r2Biu4djM8XvA?T-@TEQzFq~KEpe9cllltt?Ih-4%t_@|rDT1i?OTA&SuDpp5'
 '7rio5--q!H3~nG2G~Hw$)<XaY2N4JkO?~mGn3gGe??t_F`%GLL^#_i`hemM0H@f=Fp><%h#L+<tE3O5yQwkIKZ!;{*(ePh?nPE8&'
 'Re(cF3_p7Z=k;3Ylm?yjQaJe|19gJGY4M)SdJjhCN2Rl~5@j47v^NwSmls#Hy@N)zR0GH~tT^q)aqcu(%DMWvxsiFDTvUIWt((qX'
 'vJ(DOx^Y=9(Qra*W-_VlMyr+1YPno<J=NMsC3D$Sw%N*Q`D8YcNvcgPx6xW}CY1C>vz1;~;cs4P<y%cX6~;l;>W$sI`oSelCeoR_'
 'NMYdh^;R;YG&h>ri~=nwS|YcuG}Eb#)<!0u$hA~0*UBYx`Lw2`l$4fSR}xumBb{!oXV<k{O83F%)~N(j5^lz<z3J-xc40TOWRDwL'
 'HDmX6c={44UX3hzK5HFjqD#@nlbhVVDr}7HSS7l&+cTT?$@6JycvJfI%W-n@>eF5E>gL$cPN<%~sopgvtNVAworaZi27T#g7#rGJ'
 'd5@+_r*_1dO6hiDa(R<8s>`FJt?6>}e0slszkM;dY@L>#5?AZxx_lYic$)35y+1GY4l?HzJ93`AFSIsBC;9W@-TU3kg<Z1W3zyy8'
 'ui51>z1v&f-rdq!LwbLDv=X^EvUc2G?Ttvu%o@9Q@~YI6o|fh1*Q9b#*hrKk@2Tk2Ddq0We!^Pa-df3Sch+l%mDgNjyHU@$C%5PQ'
 'y5=5tckj;z^`z^(D*cVK{N7pQD$?Cy4Ha|ulbgtmH9T#=WUWNovy-jY@^kjMym!-?sF`0krrbHaJ+I8R-KT?%x96XeMD{9q_cYPh'
 'rM8h9miDGQhr3G`rM)dFSHH0*8|TN;Ql)=<lG`p8`#Z~5+pMANz`FU^Ivi~$I-|%h?Y6L5_;qJc?cTLNc5cti!)Kcw*H%-J^N-r9'
 ')!mS8CQB=~X8S!R*GrT2s&jC<)$3keO$>KOdr6r!`J%gfn^mvxFIPHBe|Bw5daR+SJj@QSo!b*DwYqavJ*v0Qa_ZF;oxB|sDn&DD'
 'KPU2Q1Gl_=*G&(fF3yHK(Hm`ee%(L1xy*JN&#~O<du3_sT9;x|^QE|>6`C7o)&5|Zy*=Hvnw_1soi=NzJuJ}Z-uSL`)Y_qGy<iWP'
 '@AvlaQpNJII@u{DGTm<Sx~!#_^VM^0dRSIg%|u`AmnZk@`P#*FX(_)^yoj8vuT_q&D$gl>|01&cu|c~hiJOZ9Yp1fMJttX1h4Rt!'
 '4Xs3Nwd<O98^ziFR^s`iT0Q|oI<nSk=dJYN_+#J>TD@`l?&|gYsK0Vl)s?;SVcq!nIe1kDTj%SSa;}@S3X|d4>v~}|t6ipElNY&i'
 'yYhN7E4{FW-U@Q5qtw^l>A`flZn(C6d@{+ss?p^u=g?4e>P}abEBT-@sTRAJ{l-CV{p#ucV7&jbejO=PGd~A(XRF?<jurK2uvDqJ'
 '`)_MIqx-v;o0E-$^Xb}2@^Ho)O5Ba6yZ1{qV^p#C`q@JC_$|>?*J5L1lsJDr8ox$vifbpYB~xkbU+f=Tj8}&FUztg@RCMLL)6%dO'
 '-JaF9lexG3y!0_zT~9RA$^9<9obAVwxsT)F*-fm-8mcH+Q@@o4*;J(19yBt>ld*Pu_iVS*(aV=~F49VL*WVBB-AHXVdZmp^xjIb!'
 'Y+9}|F1_ESCr6`k;{Lk6chlWhb~bJY8@Ijdt=(8&t8|QIb9>q?n){SBWapPOU3pJVOKXWq`?)e|jiN?A*UCgTvKQyky{osgVsEy;'
 'a=*7+JQ!^pS?9+Yvy!{mzbQR!ofKlR)?k#Zx5ru~scvMCl;n9edQ`Jl)T_g{(t1g2Cue)CA$9q<bvxO+p03!gdH!>Ew-ZSmPug1P'
 'Ff!=%`?cfRuGLw~-L~H9hrd=nKJI6E`CcvT&D^54chsbHIzAfYUvpLM`gS8WRI{1g{PXeBUN(A}Sxq<gq|pf{@3UQpZZ*=~?(x=H'
 'q|mx<^?z2z&mU<g5$SvsGQHd9?RMqoa%SVK{&bpZzpYJjGrL&494o6zZnrq=mal(}e!a?yyRoZj)8(HR_uHnmZy3{!9ZPQSHqO@i'
 'tf3tvU7qf3oQ{(>cOTpLiRTyRPU##jO@6l2;m2xkxL$OUdzH1xc()kaEB3mtYsuD`Qc5p@Xo?-L6-uLeY2&Ee8)S>=%w=;ldNrKP'
 'EImuko|m-yq*5=pSVOhOcu9G-wqI-e*GjjVlk3y&>CXMz;l-rd>1}P-er->GR$|Kj?Q%AAA4w0)?91-QujBgRc#XEIZY%XOF^uh='
 'zF)s|wpwPnvRbYiD}~zN=z8~gkZ>zGoio+y;K-g_|B{#2w3UXP{b?L84c8k>>%X2mmqvu<wvVrdrKXjV>`0}usy;2N<3T64_Pl$X'
 'c{v~D-ja4P=Uirt+4KJRv}^t<M~0U>?(@=fU3Z>dmOI7$4^DL{Yk5}CFS^OrO4+$s86^&mBdxAo>J)Z9a&K3S*MjO?M2;`D>;C)g'
 '-hQ_6Jan6Ho#$0!?Lbd0znyIzZ*)3)iJe*^b9y^E+W+}tsn@@@+>f1)Zsy{+SDe1FhOSCZHCD6o?GH^iFK=oenY!CK$>n|(dunfX'
 '8BNV1tA(eIMAdhz8_QK1*Jfoqe`^j;Z<R^jDx_AP=<4`vDs^*j+lA`V{Y5O1SNEMrx<9N8SMuhvZtw-07?xiW_e-he`+C}1>CCLV'
 '=`eP7)4a-N2DQVNik%&|_O_bFowH=C3H7S6)@_aCjpBR$De|+tRrtAAxk}`e-km;qt8SaAv*88ZdamzXSdB<=e7UkWykHHLU(zS$'
 'ar)%Mj1_OojkBARyL2+uS#CXVr}oQ(3w3>0uHRIm(fi5S$yqkJTS=_CJLk4@Un*t>SHrIEn06_@l)G1B8->>T^Yq1VTa^=erMaA1'
 'r;#oDozKy5FuN|QFZVl|ak^$pa(UQWH4ob-S1)Q}yfb}1EbK>*V`ugJ>}f+uZ5@}@*;%YwZ;ZE36aBTDr-NDYwG>-chH}<=zt?Y0'
 '_LN@pJfp2mN6uNzJh;`SORS;RRcx>9E?-h@oS(h5?X%X^+n_P(8P!Jh<VrfOZzyk1N9EX3-MXlp{OUhl>-#VJJ4Us5GthrF`u+5b'
 'u2;5}F3+0BN_KkaJZ)8K*`L<!PW9}x8twK#vap8kJNiX=zhT90PI85n)##QrI&sZH;#j&m{;*cl5$ELas@z`QZ?Ej%z0~{m{njl1'
 'b7yjMdw9FmQx0P3<??p@0NCL#B_^HqmAmThX!c?hF55BnqbU!c*0=bAog{8^-RtJB{>y$&J-@I{-cNp(3rmIJNYSNYeb;)sZ`+-l'
 'e%&ZumQS?diJH#I>*}erQz)i^eLg$I%F^W5^rCsvzgs?gt|!b}T6;P@U0d2nCN1^-na@#ccl_auPTljudVTlkM&G05@zQXuyQ)T>'
 '?4^7@wX}4;T}Z5&nf>?dvlH1!9{-%AD%Jba%F^JukSM>lb|<6DUDI5y(aUP88ofJMcJ^1!3McY=o<?VDZ7#|a%R5W0m9uE}X1!&b'
 '6J>X8ywu27e!eYTJ-Pkj@@ao3n%DFrdbM&IJyQ>E#`^u+;HY?U*?p_f^?Gu7Ieir?v}5vkR=CebmYtQ_xHHOB+wHqSbNeuJanWH7'
 'Mcm46Qtw_b?^;jo-p|wZ(RA-PDIcttPExJw!BVMO&|(ua{knFUSxcUj>Vs|bXQ86i1}oiIbhTT2e!EiD3u8T+xIg?=>B+lo6*&07'
 '0_Xv^AsE9gqlp{O#fg9k#lr+~O>bKL0gEf~g9mXnw~mQm^mw{^(Ep3(HdF?Kdu})|V_h6qh&vr6wVq{V;vIde8ExHhC9gb~6&UNJ'
 '%qZ(wisrDAp2LRQZ|Et6R0j4?(jLMrrV_@@8_b3ZSo#FY`P(y^3fQ|1RkuxPz(zTs7(*zSQ`%RilIK(r!Gm~HCQwZo^;|H33+9X$'
 'dig`4&kkH3o1I4pL>$1J;?})DfWS+i@$K2)@6X_82*#q>poOj!slkw;7Qfka``dtsIgKV|BHm|F9*y9rYU@^CckNlD+0mO_sl%`}'
 'n=OV*XR|-WOCk5~0;Z;A_mv*H`wCX8MH2-b*g=o}{Z1f&&Aor@#dH6$k5n)fW{o%D`Swh{8_4qt`USt)pz1r2kw`k7m|w$q6m#Tn'
 '6Y?BS=t_pE;lmIvalV^{&xzWki!>PAil;VlQ!@9q0-fP!0@1?ZEQb!px;+c^6jkq`+ggD+GDn7~htQFwPeX3UwnpuaHFDXZCkw{w'
 '9dKgn*$f8A#$U&2m`y{&AjyNb48A>(!aPE3)Q^RhH8M3SA{VTZYa3sJ3LaqMZTbC#hWRFGF<A>6WdWi*$G7x5Ov!l0NfMt$FP9fC'
 '!U%a+0a!t`b)_4KJ+Pc$AfUi-<xvdFmV+|@OF-9H><Mcju8~9bbXVtLX-DTr!Ysg_>)>HC>?XSELg=t}owyf(A+5IXB71vZM4xb1'
 '97Fd*tIg<hZ6O8yqLgBi&bJLzCANnd9z^_OJ8|y|?(co+|F_-DhUU=k_AVD*y?xGXg#<R+YffNa^Z$8cGfriYXeRS5{LUZtI)A&_'
 'xnSFDr?W$xFMFL|Hz5;4o%Y{vcm8(2vu%qSu1`V|;D7`i#llM&+@!-J3{@CbV6Tq+zu8sd?;Pd(MFP9A>3kb0TQA4-w|hxB%6_+*'
 'lt}`@IKID~G>AuUL#b#OkoNt?Qh_`#I>S3h>7kTP5>Ohr*PoAurIKVSw^-qrRgey)>_(oXQybYFi<#xqX_C*S6B+!<LcK&P6Kv`;'
 'd0od2rPMlW(<8Lsl=S-+yZ%&C0_IJaC}4}ob#R-jw4NpD49R`o+ze`s$0r*Ou&Jht-uann^$nDe2ukEP^#&_uxQ6af4*!$L=MtfT'
 'e5^4sToaTxD9YFxaY3vrjj`1Ow!YAW`z5-;cVc_3%^I5CW)Wp6%&VuuB-}D=$4$cva6QY^GU2%nfzi%}rnm~%C=~;bJbJQ4Uz9B('
 'Q1VgWF>6o=My40G{@;eHJ-Gkdh;=Ypomhxg|I5&{F%|t$jD`NVt{h~C*t{{tIJF<Pep}F9UH8L}Vl$lj%m}$;vRE`0&O;GA6E!DY'
 'ANdp`+4IOa0+M-RV&1R|!hlPEF0i4{hga%T@Y}aHETB=PE$D;8ou5$S-vw2r59-X-728&3l4M3V<R3qBoOw3p;Wbabb&1r#aV%2S'
 '9CmQPn<_gf*adix?-bA>byss=)OQf)aXgOQz+RxV3ik}x?djpb)@W7r3Es9Q4R2uVJf5NwJb2EJuTXsT_peOEex^-zjVjoez-}2o'
 '(1vH)=UW<a%h#99<cqr=1BYda%qn<Ovlx){T7bS9t(gQmqh{C)IDe&h;M_|t@MpZ=g<r9AMMTE*DJVk?tINLF{#lq#G`Z-4L0RZf'
 'e!NEn$oyRlU}n%SrUve209AGXY=E&w+`{<~PGG1E{_*D{0o*whn|lbOT?!KCG0H!idavh%5uy5Y0J<2E@q?)UBjrJWw?`686~B<W'
 'zy%-tjKzxcRKMcmeEmE$p;y*4%yHjj`^<xV0}<u*EnqpLZG}NYvG20EiE9BM;ZRYybF82gc}V3GWS!(lmL$`UVyh1gFx-No(ywbw'
 'E+7q3T>joNlR>rni^XeorB6TE=rBRpBqwTQ$^)$l>M&Tk1<-T*d~eaj!Fw7o7eph*NFR{xJx0=k*4qYYE-pzi4z?!sDg8v|!QiQf'
 'M%=Z+Iw9l%=con|TLkBz=h)f|vP&%IZ5RlIl8yNu?m+5fo|*u|x|q(e_lY=;IbXY9II_=zy%NX<nM34LVfd!rwi3)M+$?NlU2H%M'
 '{GI-mzwp_J`c3(>;xT<6)~6Gmd2c&oiGDttGKuI@e!llX!J{RgyB1@fmdH&+QYck_>$La>$45e;g|j#%egKrx5*}hP9=|H^-<+4`'
 'P<&zj`P^;kU!A-C?$m8)(G&sE57xO@4xXhiP^2xABoy7`D+5ooYN%8ApPq)okG3FSKZ|IhRlYRiqk+Z<oH@WAU{L}2cS%Y3A_D8w'
 'n{z=nnC-1!u_BvaR^$S6;xwVs08Ee~@4?Te0XCoKyilnp+CmH+zya9ladm6!MP5sOM!HRW-b0e!ae+nc=rN#Z36S&w)rrRlJ0=!d'
 '7^p8KJZ`~u*fm5&{t%n)cp_Efsv!zUUv|cbKLET3;!Ex64Zf`&)KaGO1w~GDkwY(R;ufrurgC|%BXX8WlbO_9ck&i0@QHLPwdh5C'
 'n{z_G;l*A+mZ<r`stOkoy95U;0@T+*M;_}TNB{#NX6r4Z*8{xuz;KC&>Kz^E4J0{0Vip85CJ0kn9R-~kT8LL+&Wg4&;EvTFzO_@('
 '2adN@C7qND8r{feB9K_n!SKsQv}h`#MFP?dVXz9xR5rgMOgSi9gp404;mQ>zS1g@IP+PpX%;cM5I(U7J?l+q8y=U3TJi7?>7%mPM'
 'Zv25oGcin1mf9gS25hSbqvdznFa#k*DYk+9pU+iC4_%hd4)CNsf<-JSXjZZ_By1mM43w;b&ij*0us?jQaqv_M?CGq?B=7~MFS{p0'
 'VOujn@2|)Ur1LPJc%TD<1a=8j4Ua4SD2M&sflY1{@iu{JK1k~%k4VF7R#GG*KQ3;w#~B6)f&F8kq_9Iw!3^9N7F1rm2DpZdw-8Zp'
 '4;@}8M3Z<H+p_gO4VTv&hgYYkjlHXS<MQWKsdmsPou1Y%F6xc*i}U+~+C`&!x!<@3)rsxAWa=c?m~>(HlGyj$;ED+Sva^W<^h>Xh'
 '7e8QdgZWH*4}>EKKL)}mn)G$WY=DIUvK2`b{;~Re%{OeYYHiKI#Yr^K&%g$E8~lJtV+{Hm>N~Ld$iQ+8TyI_;U+e6bf$J+%k;Q@t'
 'ldtP|LB0ZEKm}(sV5r6#9x?a~Ll$sd+n6>2qjjj@Jo7&FbVUQoZwUP?9q~#q2!?6&M}0t|(LxUSsW5*K(GHhI9>RrW3IuT&#7W0O'
 'rpd4HLPqH;EuTcn0vB%fEC(4h${?<~lAyWX;En;dyZTE?0!@wv_rjvfLIG=n?{()}uo)!J&On2M@KxX7Jgy=9C7e4_;2?y*HW+aT'
 'viOlAe7n2HY8tpJ5J2iS9^5oWFyDS2@!7z_(gCHM$#1@f<bp7<euU?Do&}~djzO@n9G}>RN5w1{29Um~$YFk4hpA_<+5ypjTA#Qs'
 'tEJ1!FhO$nh-6MKVpn?r*nCal!ULKJ6EFTp{wCfRfKofCUVINn{R&3?9h9?Dy;iwxT-Iv`r86JQR~iji`5a|v3>)m6EzD-4L20<r'
 '=qrZVXoNR~fsB`@DRz5|Hz|k{9A1*VmE_u6IF1*f{f7kZuLF|?r|}<LUsuz4Xig6?os7vW;5Td?%n0`cfT(Kf1J{>P8j>C^Utmj3'
 '3>m~&aTpcG_<${g(5j8hkg7X|riZ?}Rxchp_nYHKUofFM3#H=e_&Nz)HVybl#*-WI1V96|AtV?*cO4keoM!3V+a<22(?P02@&KU0'
 'lE<)&J;HnVK-FdVu<W=uYX3?*3uLzC!~rpeZJ7_@i|WDo?rG_=aej5ysFz_z_dx>EFoxb2%AHleEAn65)wg&%-?!KBeYv-<-PHV%'
 'c$f0AJNbY{{0x}a!3>)=2Y#B<GzK#PkiEyPfot@QSKR~MGfe1Fdk+5dBqGF)e^Hw`h&LMEEq_SKY#zgmTzCVE*?eZhc&#1n#JO{*'
 'P=;6TuIa=-J8bqTG@%(vTY5;v3H(jQF?d?LxH{i&Ebd=MKCxe^F|)&uuXq7yJdncfI1%T~(%ydZG4-x(K+0kF5-D@5am=FK@)Au3'
 'eY&sMDefd36V06sblU1!3h>w0AD9J5RC?_=Mi-@57(=DznGUa_kA8jl@SS7ABjLH-^eNzF!B<gc9yaFNLjVp3p-&h35NARGWHAQQ'
 '63m>OGax9NN#wH;sID6(T1{c&g{aC)mvnovEmbjkVX{wDvhVkb^Au^97*hf=86;qiyOVc!>F&cOCU26>N3MxFGyr*Q0Av6^egVj1'
 '1prrSWOo-IavZdsjxx}3UW9L%E3=M^Ane8i{Gx8?NM1IH!Q3NWhI8~i_+`PU4HQkpd5oRuIPTomV*}v!repP}pmqtHC8frQ;kDU#'
 'h~ZF35Gp3f@*`12p?TMM4mavb4d|Rcgi`Q)fbPPCjZ9GI9)QNs?v@`TqL0xB2@^yr;TKBKa0gU2C#E@ESq<UxM6AArHB=v3y5bnB'
 '(Zk?~3rdfTyg9s?)MI%P=Gyh2%CK`m-t`tR{<t#&4(~X@BY{K;pH{=@k&;*mFzZH+Obi|lm{3fdKHyQAg3BpR;z^L=fp?40TJ{rE'
 'hKVq7Jy4*W63}P^>jl+SDL_98BOjn0<0VWcKsmq<`le_U3dhlZA$yJX%`Mbhq2+brM&kK(|D?tQTDQ7k(l_U=GjHyLe@|F<@pejV'
 'YJMX3>jh@4LFmCl7tcLmv)JMW!C`wPfV05xpu{GWVGc5XPe@?#5nLcJMpzwV7$M$rHkO0agcXAWabS*npGV`ZJXi{ha<Njt!7pY2'
 'We*QziQ0TM%%ce~LBc5xd;-?>gpCDJpy|Rrl_2Q^TA%P>Pxiv!#IN`8pCb4)nXn!rVF9!VC})a;Yzu=P!2wSualCO<UI?PK=U&($'
 'J90nSY*P?}QkzlgkfRKmm`r~BXd|}g2c<*-VebsRlgK!}3EN#V^xUER7P$s5<GC=!QLs*Yph=&7mc#FTmVW(MKu-P9bNO!^nDSSr'
 's-QVf%d{qobMNm*(-phfVI~hs8N!c;_7$h=5WGOg0QSLDIw60^E)B?}!pQVo;=dM3i)(2LVoeoVAVucRKiAL}7Z(qZ`7u<Sb06{p'
 'lzv>8d5lkD1(t)?fK3SJNi-msyos9l5m@YlAAy9bq7rlK&w(SId`I>I9P{@74xkifHNkWZ6FK@Vc&ASngP(J6_8gfH5}SZEr;l4~'
 '`j7Nb0quT)VF*&3Pp?D#>I6Hs5ak3*Rh=<MAD>!=>1K0LYVjPQIH;hIdeTxvI2hacyD>DI?{u;E^IkTaK3_reK-lDLODADAcaZwN'
 'hGPF|Kn~%_k5LA(0Jg4XXv`<^2j6or8uU-YI)B2#c>EO!=+6EW%mwtLiJ}^=BaO!do|diYHuXciao6G{<$2gwfWo%bVo`dDm|ubs'
 '8JRJ$ra@_f8-`d?Y8rT%swpBmK4N?lZZd~Hzr>Zzy%(sHGEhs7B?}|wWiK>4ph}t?q5RH*5%<@FamzeK^OZes1{9*MKJzYgF*XBP'
 '$S>26Ya==6jp4Ua&_F2!j|F|F|Jq1&#Tx>afOWJ+f2m@w`JEj)bBJicezAJu3La=?E=!2<Y2JBB|E`7M5*=)+@APx`1%nWgh)vNk'
 'yt-lF-G9R<mplIO)M+Qqq<~D2VgZ|c5d;W45KLffH0W-{qH}#Vuz@Ss-@uG6_7^kJf8#|FK9LK{5uum|B%4Q{_&+hA<<O-IW^fy<'
 '?G~zR=wm0sOQ36^k%R7Tu3|tYbK!w{8M4gY%-e#<#`CwUI?!2I+`$fdG2Abf(Ql%-{vziq++WvxhW``={U1gy#oYh*u}l9N0aQjx'
 '0hs_O^6#EhKr3!pJxz#l{>nF4h~xr){-X^R-09hg2V?z=+XalUvA5}C?C-~U6ru$RjerqmnG=sO|3%3~gF4B#_hv0<DGM@;iweS|'
 'SHLfKQ@%Jo@LY}imCL=0>x0@IcknTB!8Ag@8*!XMXol@Og&xVI)f+h-9|3^?8LLfcHl5}n{BOWex}Ig%MKS$|1_Ux2JePI_vGyMe'
 '=-Cj$3Mdxk*1y>}@-O#_FcP!az0$0)P0tX*IbpM*YYX!cTvMn4%HL^>!A)vHm*Wb&ALZeYd61+x-x}{T0aQiVvd14Fa)uPIlozz*'
 'OWAV+pI%%Z>^JrfPEUg~jDY;|B=P-3a+K2t{9ikO#g;+Lh=uVZJTkeqqBVSH=ywk8PF$P|VM9QMKG$m~*KQVq5{QA34b#gAOn8JH'
 'Ji_r$l%oRfZ}OVt_2giu|E(|o%fT6RyZyVPGol7RJTrIni$!;Ou~({J)Ec#eYVBhGY7eIB;I_0^Z(ya$VFhvz{*~kY_x^Im?f#Ls'
 'oSO^me;V?ikN@}o0e<M-ng'
)

def sha(b):return hashlib.sha256(b).hexdigest()
def main(dest):
 raw=zlib.decompress(base64.b85decode(PAYLOAD))
 assert len(raw)==ARCHIVE_BYTES and sha(raw)==ARCHIVE_SHA
 files=json.loads(raw);assert set(files)==set(FILES)
 dest=Path(dest).resolve();dest.mkdir(parents=True,exist_ok=True)
 for name,text in files.items():
  b=text.encode();assert (len(b),sha(b))==FILES[name]
  p=dest/name
  if p.exists() and p.read_bytes()!=b:raise RuntimeError('Refusing to overwrite '+str(p))
  p.write_bytes(b)
 subprocess.run([sys.executable,'-B','-S','h5_square_allroot.py','.'],cwd=dest,check=True)
 expected={
  'h5_square_certificate.json':(10349,'e5f14ac7c64adc4ad085ac327f74908fbd8f81893dd2a2d15a06d733f565d82e'),
  'h5_square_report.json':(8718,'787b0d2b4c8e89e9742dbf90d39adcfa23cc2208f629fc281bcceca2fb68dd30')}
 for name,pin in expected.items():
  b=(dest/name).read_bytes();assert (len(b),sha(b))==pin
 print('H5_SQUARE_LOSSLESS_SOURCE_ONLY_RECOVERY_PASS')
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'h5_square_recovered')
```

## 8. Scope and continuation

This is a complete unrestricted all-root exclusion on the entire new two-cut square, together with the stated actual-refill collar and eleven-parameter cylinder. It is not an all-rho theorem for arbitrary basal parameters, not the whole positive-projective domain, and not a whole H5-incidence or whole E17 exclusion. No universal S≥2 statement is asserted. The accepted global interval **34≤Cmin≤622** and the separate attainment problem remain unchanged.

The most useful next enlargement is a macroscopic independent carrier parameter, such as q or lambda, while retaining the full cut square. The recovered 321 weight vectors and exact shifted coefficient matrices are reusable seeds. Their moving carrier volume, first moment, edge vectors and cubic corrections must be recomputed or enclosed jointly; neither the four-cell proof nor its collar licenses freezing the centroid. There is no complete one-sided survivor on the domain settled here that would justify a reciprocal calculation.

The evidence is an analytical reduction plus executed exhaustive rational certificates, not proof-assistant formalization. No numerical feasibility failure is promoted to an exclusion, and no feasible physical body is inferred from a library gap.

Supplemental copies: [recovery bundle](sandbox:/mnt/data/h5_cut_square_allroot_recovery.zip), [exact report](sandbox:/mnt/data/h5_cut_square_allroot_report.json). All continuation-critical source and data are already contained in this handoff.
