# minimum-0238

Historical AI scientific report · saved 2026-09-25 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# H5_FULL_Q_CARRIER_CUT_CUBE_ALLROOT_NONZERO_PSD_V1

## 1. Result and exact scope

**The entire admissible q interval is now closed, together with the entire two-cut square.** For every `(x,y,q) in [0,1]^3`, all **48,790 labelled rooted primal trees** are infeasible for every **nonzero positive-semidefinite matrix**. Every genuine interior body consequently has **at least two strict unstable vertices under every SPD metric**, without a condition-number bound, stable-root assumption, selected-forest restriction, or weak-contact regularization premise.

The parent fixed `q=1/4`; this result varies it over `[0,1]`, not over another perturbation collar. The supplied parent identity is `minimum-0237`, SHA256 `4eede392385c2ecabeaa3f933476c06a2caf571a5b4b672d4f37bbbd5ae44e4c`. Its accepted full-square result and independent-carrier continuation target are recorded in the supplied journal. fileciteturn4file0L103-L108

The exact certificate has **646 distinct integer stresses**, **1,345 stress/domain applications**, and **48,420 shifted positive-definite Bernstein matrices**. Every rooted tree contains a certified stress whose actual weighted arrow mean satisfies

\[
\boxed{\frac{\sum w_{ij}D_{ij}(M)}{\sum w_{ij}}
< -\frac{3}{6225920}\operatorname{tr}M.}
\]

The proof uses the changing body's actual uniform volume and centroid. No complete one-sided PSD survivor remains anywhere on this cube. There is no global complexity-bound or whole-incidence subtraction.

## 2. Physical parameterization, true lattice and boundary

Set `b=a=1/4`, `d=3/4`, `u=v=1/16`, compact `lambda=1/2` and hence raw `rho=1`. Put

\[
c=1-\frac{3x}{4},\qquad p=(1-q)y.
\]

The genuine raw domain is equivalently

\[
\frac14<c<1,\qquad p>0,\quad q>0,\quad p+q<1.
\]

Thus c is free over its entire admissible interval, while `(p,q)` ranges over the entire open admissible triangle. These are three independent actual shape parameters at the fixed remaining carrier data. In the parent's compact coordinates,

\[
\begin{aligned}
z_0&=(1/8,0,0),& z_1&=(1/2-3x/8,0,0),\\
z_2&=((1-p)/2,p/2,0),&z_3&=(q/2,(1-q)/2,0),\\
z_4&=(0,3/8,0),&z_5&=(0,1/8,0),\\
z_6&=(1/32,1/32,0),&z_7&=(0,0,1),\\
z_8&=(1/2,0,1),&z_9&=(0,1/2,1).
\end{aligned}
\]

The outward maximal facets and true edges are unchanged:

```text
FACES = (
 (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0),
 (1,2,8), (9,8,2,3), (9,3,4),
 (4,5,7,9), (6,7,5), (7,8,9)
)
EDGES = 01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.
```

For `(x,y,q) in (0,1)^3`, this is a genuine `10/17/9` polyhedron. The exact checker verifies 34 incidence identities, positivity of all 56 nonincident support polynomials throughout the open cube, a rank-three incident-normal witness at each vertex, and each true edge as the complete intersection of its two maximal facets. It uses nonnegative Bernstein coefficients with at least one positive coefficient to prove interior strictness, not sampled hulls.

**Every cube boundary is included in the polynomial certificate but is not called a genuine E17 body.** At x or y endpoints a cut endpoint coincides or becomes a refinement point. At q=0, z4 is redundant on the vertical basal edge and two lateral supports merge. At q=1, p=0 and z2=z3. These are the actual positive-volume limits, with at most nine true vertices and retained labels. No zero-volume normalization or artificial positive endpoint cutoff is used.

## 3. Two actual tetrahedral defects and moving uniform moments

The independent q extension has a particularly small geometric description. Let

\[
A=(1/2,0,0),\qquad R=(0,1/2,0),
\]

and take the fixed eight-vertex carrier

\[
K_* = \operatorname{conv}(z_0,A,R,z_5,z_6,z_7,z_8,z_9).
\]

The new body is obtained by removing two genuine tetrahedral corners, with disjoint interiors:

\[
T_q=\operatorname{conv}(R,z_3,z_4,z_9),\quad |T_q|=q/96;
\qquad
T_{x,p}=\operatorname{conv}(A,z_1,z_2,z_8),\quad |T_{x,p}|=xp/32.
\]

For spatial coordinates `(X,Y,Z)`, the two retained halfspaces are

\[
(8q-2)X+8qY-qZ\le3q,
\]
\[
8pX+(8p-6x)Y-3xpZ\le4p-3xp.
\]

The condition `p+q<=1` keeps each removed corner on the retained side of the other cut; the zero cut parameters give the genuine limiting supports. This is actual geometric subtraction, not independent choice of two masses.

The fixed carrier has

\[
V_* =95/768,\qquad
J_*=(2045/98304,2045/98304,191/3072).
\]

Writing `V=int_P 1`, `J=int_P z`, the resulting exact moments are

\[
\begin{aligned}
V&=\frac{95-8q-24xp}{768},\\
J_x&=\frac{2045-128q^2}{98304}
       -\frac{xp}{64}+\frac{3x^2p}{1024}+\frac{xp^2}{256},\\
J_y&=\frac{2045-480q+128q^2}{98304}-\frac{xp^2}{256},\\
J_z&=\frac{191-8q-24xp}{3072},\qquad g=J/V.
\end{aligned}
\]

In particular,

\[
71/768\le V\le95/768.
\]

The q-carrier's first moment is quadratic in q even before the second cut. Freezing its centroid would therefore change the problem.

An independent genuine apex-0 fan checks all these formulas as polynomial identities, including the second moment:

| Tetrahedron | Actual volume |
|---|---:|
| 0128 | `(1-q)y(1-x)/32` |
| 0982 | `1/32` |
| 0923 | `(1-q)(1-y)/32` |
| 0934 | `(8q+1)/384` |
| 0457 | `1/192` |
| 0479 | `1/96` |
| 0675 | `1/768` |
| 0789 | `1/24` |

For any tetrahedron of volume w, vertices a_i and S=sum a_i, the checker uses

\[
\int z=\frac w4 S,\qquad
\int zz^T=\frac w{20}\left(SS^T+\sum a_i a_i^T\right).
\]

All eight fan volumes are nonnegative on the closed cube. The fan's zeroth, first and second moments equal the two-corner subtraction identities exactly. Integration diagonals do not enter the mechanical graph.

## 4. Thirty-six-block common-stress mechanism

For `X_i=z_i-g`, one common matrix M, and nonnegative integer stress multipliers w, define

\[
D_{ij}=X_i^TM(z_j-z_i),\qquad
G=-\sum w_{ij}\operatorname{sym}[(Vz_i-J)(z_j-z_i)^T],\qquad W=\sum w_{ij}.
\]

Then

\[
\sum w_{ij}D_{ij}=-\operatorname{tr}(MG)/V.
\]

The w's are stress multipliers, never replacement physical masses. Let s_i and t_i be their outgoing and incoming totals, and set

\[
e=(-3/8,0,0),\quad f(q)=(1-q)(-1/2,1/2,0),\quad k(q)=(1-q)/32.
\]

The parent's cubic correction extends exactly to

\[
B_1=\frac{k(q)(3s_1+t_1)}4ee^T\succeq0,\qquad
B_2=\frac{k(q)(3s_2+t_2)}4f(q)f(q)^T\succeq0,
\]
\[
G=R+yx^2(1-x)B_1+xy^2(1-y)B_2,
\]

where R has multidegree at most **(2,2,3)** in `(x,y,q)`. The mixed term remains

\[
[x^2y^2]G=k(q)\left(w_{12}+w_{21}
-\frac{t_1-s_1+t_2-s_2}{4}\right)\operatorname{sym}(e f(q)^T).
\]

It is generally indefinite and is retained. The exact checker verifies the cubic and mixed identities for all 34 directed true edges, hence for all positive combinations.

On `[a,b]x[c,d]`, write `x=a+(b-a)s`, `y=c+(d-c)t`. Subtract the still-PSD corrections

\[
(b-a)^3y\,s^2(1-s)B_1+(d-c)^3x\,t^2(1-t)B_2.
\]

The remainder has nine degree-(2,2) Bernstein matrices, each a cubic polynomial in q. On a q interval `[l,r]`, their exact values at `l+(r-l)j/3`, j=0,1,2,3, are converted to cubic Bernstein coefficients using

\[
\begin{pmatrix}
1&0&0&0\\
-5/6&3&-3/2&1/3\\
1/3&-3/2&3&-5/6\\
0&0&0&1
\end{pmatrix}.
\]

The source verifies this transform on the entire cubic monomial basis. **Four q evaluations are exact interpolation of known polynomials, not a feasibility sample.** Thus each stress/domain application has 36 matrices H. Every accepted application passes

\[
H-2^{-24}WI\succ0
\]

using exact `Fraction` arithmetic, symmetry checks, and all three positive leading principal minors. Bernstein weights are nonnegative and sum to one, including on closed walls; the discarded corrections are PSD. Consequently `G>2^-24 W I` on each entire box. Together with `V<=95/768`, this proves the displayed mean-arrow gap for every nonzero PSD M.

## 5. Exhaustive all-root atlas

The verifier enumerates every nine-edge subset of the 17 true edges. Exactly 4,879 are connected. It orients each toward each of ten roots, checks 48,790 distinct masks, and verifies that each primal complement is an eight-edge dual tree. A stress covers a tree **only if its entire positive support is contained in that same complete tree**.

The atlas uses one whole-cube domain, four full-square q slabs and sixteen leaf boxes. The xy quarters, in order, are LL, LU, RL, RU, with halves `[0,1/2]` and `[1/2,1]`.

| Closed q slab | Whole-cube uses | Additional slab uses | Additional LL, LU, RL, RU uses | Trees covered in EACH quarter |
|---|---:|---:|---|---:|
| `[0,1/4]` | 240 | 63 | 70, 109, 73, 125 | 48,790 |
| `[1/4,1/2]` | 240 | 122 | 25, 25, 26, 32 | 48,790 |
| `[1/2,3/4]` | 240 | 141 | 27, 29, 30, 39 | 48,790 |
| `[3/4,1]` | 240 | 129 | 10, 10, 10, 10 | 48,790 |

The 240 whole-cube applications are counted once in the 1,345 total. Every leaf has exactly 4,879 covered trees at each root 0 through 9: **780,640 tree/leaf alternatives**, including all shared boundaries. The retained 646 distinct weight vectors contain 3,050 positive terms, maximum weight 63 and maximum support size 8. The 48,420 coefficient matrices give 145,260 positive leading-minor tests.

For physical SPD M, every non-U vertex has a nonnegative incident escape and

\[
\|X_j\|_M^2-\|X_i\|_M^2
=2D_{ij}+\|z_j-z_i\|_M^2>0.
\]

A unique strict U would therefore supply one enumerated rooted tree. Its contained stress would have a nonnegative weighted arrow sum, contradicting the exact negative bound. This argument allows incidental weak contacts. It also excludes every raw complementary rooted primal/polar pair on this domain, but the 439,110 labelled pairs are not new canonical orbit or whole-type counts.

## 6. Search evidence and meaningful negative controls

The locator began with the 321 distinct parent weight vectors. On the sixteen quarter-q/half-xy boxes it made 586 calls and found 586 additional exact stresses, with no unresolved calls in that run. The resulting 907 distinct vectors were reduced deterministically by greedy cover and reverse deletion to the final atlas. Linear programming and eigenvector cutting planes locate multipliers only; every retained certificate is rationally rechecked. The locator uses SciPy's `highs-ds` interface with explicit feasibility tolerances. citeturn254784view0

The selected whole-cube stresses cover 42,429 trees. Adding the corresponding full-square slab stresses gives 44,895; 48,246; 48,254; and 48,674. These coarse-atlas gaps are **not physical survivors**. The sixteen closed leaf covers eliminate every one of them. No completeness claim is made for the numerical stress solver, no minimality is claimed for the atlas, and no solver failure is turned into a body.

### A parent stress really changes sign after actual refill

The parent whole-square stress

\[
6D_{34}+D_{89}+3D_{93}
\]

has all nine shifted matrices positive at q=1/4, with the parent's `2^-20 W I` margin. Nevertheless, at `x=y=1/2` and the SAME physical metric

\[
v=(0,1,-1),\qquad M=vv^T+I/100,
\]

its weighted mean is

\[
-\frac{1319641}{18124800}\quad(q=1/4),\qquad
+\frac{1318607}{89600000}\quad(q=3/4).
\]

The two actual centroids and volumes are respectively

\[
g=(601/3776,953/5664,123/236),\quad V=59/512,
\]
\[
g=(1889/11200,877/5600,367/700),\quad V=175/1536.
\]

Both are genuine `10/17/9` bodies with strict `(S,U,H)=(4,3,5)` and all 68 primitives nonzero. This is an actual transported-stress counterexample, not a complete surviving tree cone. The new atlas excludes all trees on both bodies.

### Unbounded-conditioning physical controls

Take pairwise orthogonal vectors

\[
a=(1,2,-1),\quad b=(7,-4,-1),\quad c=(1,1,3),
\]
\[
M_L=L^2aa^T+Lbb^T+cc^T,\qquad
N_L=\frac{aa^T}{36L^2}+\frac{bb^T}{4356L}+\frac{cc^T}{121},\qquad L\ge1024.
\]

The inverse identity is exact; the eigenvalues are `6L^2,66L,11`, so the condition number tends to infinity. At `x=y=1/2` and

```text
q = 1/100, 1/4, 1/2, 3/4, 99/100
```

the respective whole-half-line strict censuses are

```text
222, 222, 233, 222, 222; all physical weak counts zero.
```

All 340 primitive sign polynomials are certified on `L>=1024`: after multiplying polar rows by positive `L^2` and substituting `L=1024+t`, each quadratic has a strictly signed constant and coefficients of that same weak sign. At q=1/2 the unstable vertices are 3,4,7, not a forced pair of apices. These controls attain the theorem's lower U count at four q values, but none is an attainer of the global 110 problem.

## 7. Actual-refill collar and full eleven-parameter cylinder

A quantitative extension, secondary to the macroscopic q theorem, is also available. Let a genuine same-labelled-lattice uniform body have matched uncentred vertices within

\[
\varepsilon=2^{-35}
\]

of a reference cube body, including a labelled boundary reference. The reference diameter is less than 2. Expanding the eight fan determinants gives

\[
\sum|V_t'-V_t|\le33\varepsilon,\qquad V'>1/12.
\]

Comparing actual tetrahedron centroids yields

\[
\|g'-g\|\le793\varepsilon,\qquad
\max_i\|X_i'-X_i\|\le\delta=794\varepsilon.
\]

Every primitive changes by at most

\[
(6\delta+2\delta^2)\operatorname{tr}M
<\frac{3}{12451840}\operatorname{tr}M.
\]

These rational inequalities are executed checks. Thus all-root exclusion persists with half the mean-arrow gap, after recomputing the perturbed body's actual centroid.

An explicit eleven-parameter physical cylinder retains free `(x,y,q) in (0,1)^3`, sets `c=1-(1-b)x`, `p=(1-q)y`, and allows each of

\[
b-1/4,\ a-1/4,\ d-3/4,\ u-1/16,\ v-1/16,
\lambda-1/2,\ \sigma,\ \tau
\]

to vary independently in `[-2^-38,2^-38]`. Form the compact H5 vertices and then apply

\[
Z=Y/(1+\sigma Y_x+\tau Y_y),
\]

uniformly refill and recenter. All basal guards remain strict. With `eta=2^-38`, the denominator is greater than `1-eta` on the **released carrier**, and total matched-vertex motion is less than `6eta<2^-35`. Hence this full cylinder is excluded for every SPD metric. Closed cut/q faces retain only their stated limiting semantics; they are not counted as E17 shapes.

## 8. Recovery, dependencies and observed execution

The complete supplied journal was read through EOF: 331,701 bytes, SHA256 `5e9c75c42807d69c2202277f22263f46d4a4fc9807e815787590279c10619116`, including the literal parent. The new calculation reused the parent's exact arithmetic, graph and 321 stress seeds without rerunning the already accepted parent theorem. No missing archive, connector, old sandbox or unprovided parent data is needed for this successor.

The lossless unit below contains **all seven files**: exact core; symbolic geometry; actual controls; complete numerical locator; deterministic reduction; standalone exact verifier; and the complete literal final certificate. The optional discovery seed is embedded too. The default recovery needs only **CPython >=3.11, standard library, assertions enabled**. Observed execution used CPython 3.13.5.

```sh
python -B -S recover_h5_q.py fresh
```

Independent rediscovery was also actually run from the final compact sources, using NumPy 2.3.5, SciPy 1.17.0 and single-thread OpenBLAS 0.3.30. It reproduced the unreduced discovery, reduction statistics and final certificate byte-for-byte:

```sh
cd fresh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B qlocate.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B qreduce.py
python -B -S qverify.py verified
```

All nondefault tolerances, directions, rounding denominators and tie-breaking are in the source; no random seed is used. The locator uses 80 iterations, feasibility tolerances `1e-9`, congruence `diag(2,2,1)`, scale 4096, and denominator trials `10,30,100,300,1000,3000,10000,100000,1000000,10000000`. Numerical choices can differ on other builds; **fixed-certificate verification does not depend on numerical discovery**.

The final recovery was executed from a fresh directory initially containing only its wrapper. Observed markers:

```text
H5_Q_FULL_CARRIER_ALLROOT_PSD_PASS 646 1345 48420 145260 48790 16
CERT_BYTES_SHA256 27865 7d7d504bbedde84966a63894a6040679bdda0b22af267e6337bb06365fd1b084
REPORT_BYTES_SHA256 68318 d3a8162bd65120f4fcae461ec25b3a19dd44d340531bc9bd5eb4a208430ab147
MATRIX_STREAM_SHA256 e200c98c3677604391ecad0f39a8ef62478253fe829db9eda44122383fe469c7
H5_Q_TWO_TETRAHEDRA_GEOMETRY_AND_340_FLAG_POLYNOMIALS_PASS
H5_Q_FULL_CARRIER_SOURCE_ONLY_RECOVERY_PASS
```

Additional reproducibility pins:

```text
qdiscovery.json       73020 bytes
SHA256 4edbf028360ab45eac8acf32004f5bde65b2ff9758adf5e594925cd37566cce9
qreduction_stats.json   890 bytes
SHA256 dd4ed24bd1194f722407ad123bc18540a93c47884e07b654fe7d717d374b78f1
recover_h5_q.py       30198 bytes
SHA256 273c1922ef35fa30a70cd1030a84b1df35abd47fd3555d4e2567393bf586964f
```

The decoded seven-file archive is 61,430 bytes, SHA256 `ceb3a8b4960c4e61789c1074624b06bee8e05a850ee2431e26ab2a09798d87cf`. Its per-file pins are checked inside the recovery unit.

### Complete autonomous recovery unit

```python
#!/usr/bin/env python3
"""Autonomous exact recovery of H5_FULL_Q_CARRIER_CUT_CUBE_ALLROOT_NONZERO_PSD_V1.
Default proof uses only the Python standard library. No downloaded inputs.
"""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
if not __debug__ or sys.version_info<(3,11):
 raise RuntimeError('Python >=3.11 with assertions enabled is required')
ARCHIVE_BYTES=61430
ARCHIVE_SHA='ceb3a8b4960c4e61789c1074624b06bee8e05a850ee2431e26ab2a09798d87cf'
FILES={'h5_q_core.py': (13123, '4e6de4c4076326e29b9c8d38e5e756131e51a94d338e67f6d91e09d804884985'), 'qgeometry.py': (5122, '58c805f748a4b07d498d4a6a7fd531feea9b53f91037ee57e426dac8d0442e30'), 'qcontrols.py': (2656, '15bffa1661bd560042316dae8da53656210f528a9ab4a997b921fa3862b75038'), 'qlocate.py': (3811, '0440f2735426b12f9666afbb7cdaa9af64d7e81bf8ddce4664cf78a4cdd86341'), 'qreduce.py': (2245, '78d8a6dd3c4d82ce5f936950e424ec3098c6e3277e56c3d07a78c02fcdb5c747'), 'qverify.py': (5405, 'd995f0f5ae7a7c18fab6d2d4c7fa8664b74b6e9e49d02c44af412d1438efa737'), 'qcertificate.json': (27865, '7d7d504bbedde84966a63894a6040679bdda0b22af267e6337bb06365fd1b084')}
PAYLOAD=(
 'c-p<aX+zsQvjF=2{)+Tz3wGjA?@kD&1<F#&4sD^7rcUC3Asg8PrN8~oXt5>7bUEkT`@C<7ZAqii>@$*+$Nz4e>V37|?T1Uf*?-Ib'
 'y?pUzH0ZynMV&WcXPoQJhBw`g^{w;mKm6a0le;h0N3}2)PJ{X|7xbgyO*<S$bu9<?qo9>*ciUlSIM8y}{h)V~3p$Nlzgrs(hPht1'
 'HS2WS5p=4xy7jxk(znj1VbqF-Q8)llVXhwzgQycWa?O6Xog3bSxxuK{Yenz`&>Y;4pi?zywff!e5YS!z)-lSS;pJ+xVK}JdPIuN!'
 '$Ia<ws}uxY!*15=Zb`3~?6PZxcBxzoT+^zRY`5g;X4%mjhGmw#dc&(*PQ!D(u<4eAS^#LB!PGsNtTRL`fH>`3G{|+jLqM@V>X22j'
 '2c0l%0Di-6F6uPHKJ>?iaFVNs{bAIM>cKEv;`IC0AuDV4fml(uGss2lUbjEYZLtTrV36BlouVNC=yqFir+T*yYzfFft=I21M)e`<'
 '+YW{|Vz+M{c2f%mp=)aot*EBm4!RxfCK%k{&0scwPEE3eYPAv8M%UG9uG`N+!_qkH4`7xmtf;%9Sejv|K<ivThz4QqWYif(?QpZ-'
 '@Aj3&BO)NVRo_}NjNAmo0oE|UrQ`C#PEczBb^77`DC&oeMfF=}Yi(om)K?T&b2MACG*dG)UDcG5=4rZSz?G-D<cR@oB~^o&>3>RD'
 'E5RcRn#wTHhEE%Scv=~*T=;az;1b-!Jl{H-@3&#5;i%UNl>tyAY$%V?ozlFFuC(T*5)};fbt~*BP4!B}!MTk8nn0Z<a5+a-KyD+v'
 '?FXIfP@$vMCpz`o$;siD)Z9v>-Ku0*pw)07!H>exZt;PlKntv)rUk0X*0AM2hRYPr9qD_g5hTLSs2%n}xD<j;8fRc_(3vTJwOrp1'
 'pI`C(5>>j0FkZqFBKm<Xmj2yRBHw4Ly-grkY-}Vw!r@<2!}Wg{+X$PvaX@Id3?^jM@8l?$X<<f&Otl#fdWd?YQ!;3fHK_Q9L2YFK'
 '{E-I@@>4nphXiroMt3O9Fc`I!Y5w={>;3LP#!Cq<jjMd^(!44L@CUApD~(<0_)Mp*8oM&^nL%4)u!C8~TIpYaA7Ss?t3nO00=QD&'
 'nE%FrcJM5G1kZuP=Rd+7WRN?9=>6`5f`JQ}3GMc?m?1w1c6Ye`yBNE>dF=ik;c>=vC<uTUJkQ3l5rUu)Bir#&&9DV^xa0c<hlJdP'
 '|Dz#Jq)90nYCeCPCylpPc?2{^`@6YSbyS3Y_X2b@TlN2F3=FNK&XcB-(4jYIC<))dYb%+!iSiIl1;WCOy6WrCp@;oC#Aq7CC(waJ'
 '6hud<aQ<i_YX6K`yt*_QkO-^#95(S(QD@8;JMk}D(O^hms|9lT0War830XWRatI=K=Xb*CkUN5;`4$NP44qIJRx1<utKprGe>A+s'
 '@%KJn!T(7I|8o51o`4!7D11bE%^^hQM)(m3480+sA_gh~P}Ac5ykWy8GPx><tw?B4giCArO45o+qDnNDR4xbxpM7)-m0h2>2Tjde'
 'l{3@-%7~SCW`ZCftK*aAa=i=jN@o=EmEDRmOkG;hU`u>pUg!ewPRO9>;52pgoVVmp!2qvW0VUV!TEl-JBPTwpI5-sa-5Rywa977W'
 '_-qi5{>CMJX@HcQaOocSi8UJYnF&iCvJDN4Iq|`u53~WjO9m{T_+W`oAih(^+L(3zT<|AAH}H|W8n~~?8yg0yNImF#W@=z#CvQw$'
 'J0blUdY@PIglC_%UG2<F_|gbl%8dq`CWM1e;LTLkwv-tVhK|=){OO8skXRY6XK)Q&FMJ~TH<ybSiy)^L;HMBTxL;emLgc0zT!)KD'
 ';S2C-a^nmeo7f1TPO%OD--ZyC_EGWk3_t1f7??a*CF%%wcZ*kf@W++Uc=K6byebkp4RFd`oz98WIweC0%}+HFYazuSh;T6Ma3vaI'
 '%ux_H@t{2r0F>a^ZX$3Xdy&(<l0|hUjH)J+f7l;|)n-r+xn{7jD9i(}WEU9H8G5#2bo^L2FD{#aG-8e7eMJNnuT9}uj9BM|4|)Lq'
 'BO-M}#Jv-D!)L4`v8SvN%$x7u5X(W7F&DNVgAiI*Zsz=oo*2);upa`d7i9gDFuJ}O4rnHl?aGUjyrO*0Bjn5As<;b()I2N+OkVA('
 'NFLX&{^;-u97GL4)M5|;0|7uGI{G~n7SwChpfSwJ)7pF-5zNIA^%f8_cZ5qtI#eMOi-y%IaJSXeroOIn8y5|t&R`gH>JYbTN9r<m'
 'SgQNerTS96+nXt5u}E~@^7xcvS>Kd0;}N;4E~ENF9G`nfriPUMrrTh%Lo%z>TLY~@XMOPDMo}vd2<;9Aj#ZYI5DU~;g2WXhoA{&g'
 'Q-!hWAzn(*Xz-QPD8z<OkrPlB03Ind71|io<pw&n#?m#&`JIN2KrM`M1e@n*3DIpJkZQG0=JMH`F$SIRnqd$J0dyEFr#KepW_Yo='
 'pVSz{U{n(p!Q(NwEff*oxL-fBBX%hi@nPJtJ!;KS<?)G=f~1aFC@sh4AE?n%sl3fmEGpb-w}lp`o5Jo@PQU!*Sqc)oe1>0)En1*P'
 'G|nbLUNPQmDI}v|-Fw{$@7kd#Gg~2uZ%2zdLzQ@o4s(nT{*hv+8GajpJopcJM!?*hh=uprn1RIllsK$wFk~u)j!cNE$KVz6QGN!I'
 '_3!CVwDsI);-g?CW7&8jPcJ^Nox}}T*x(H$$?Ga>8UoGAN{&FKU<%4AoS3jFaq{U@XDu<9quO8?4M)Qez>ABT0}m_5_P+tzi8^7G'
 'R_ws%Gh?RJx>FX2Z2^<C_(~-V{-c{e|DBsh(*2{SKNmf{G+rg4Blqvj>7VDZ&z!H9T4TSz?Poe7Xz7lIek*9#8UaLJC^(Z$%TFw|'
 '?>~^Fu2cWpA-8PEy5YA695=<v!>mB)0zg7~V=y;U=;~vl;wW=|lu1XK!l))4#YqiH81_3s%l|!UkMQux_a7nKAy)A^Xtx8O4=ySc'
 'x1xZlN$<$iNyq|vu&r6396lmjG_-Yt+5pmEKw1+wm}+X6shPBut&!j$(}J&x4a1a_Pe86IOcuzugPyX5a;;VxQ@>UWDvg=nDAtql'
 '5XJ^8H6f_2uQX^_JDvJLp)t*$S7tN6UTDmyd~Jj1Br3VBO+n{oIA^Wf84WNP1oUB8-pbErAa;2ZjA!v&MKWM`2ymcjIwjCpD_*Kd'
 '4jPgIjO}fW(uhD67mTr3wBnlt-&?#8H2j3z^qBICb;u*72L_1XNz~rI<S8lZz^czla@`MmVKDSfYTb88Rz_nRBQe`pc1#>rO=!7|'
 'TVO1#Xa^UxrC=ft7BB!}kV_LU)jVss)oMutT;esv+kruDh~HrQ3_-6Kb{fhKSrM2mLSrDOW&+JA!IAcAr8Xmtgv7L+5I&|lV}nXU'
 '(Ap?!4deWiTIwC1`94n}jUt7nnL>c|vP)cbZAyx9Gt4!2L|*dl{z(!5Q&3v04%}pS`w=A0;8VlKbvV#)zl0_Vja&cn@@l?_k>W2I'
 'whX-i7f!ufNCn`*ZTuiY<mfJm|A<p8<DaJrIQ06Re~C8;c5)N7!W?->qgJ0>FZH@TMRx9VzPQ+MOTyHM&#_EDux=62ITFlhu?+Jc'
 '+DU!kcev|2=yt+%$^gt_&@u`zv^EyK@Cn)Cn$gW{5Y+=rd-th}V_BKcv*9hQ{iy6itw>oKnn)iUjPV8rsg(_;`gnV0s!V;sbX{xL'
 'YLavH8p;N<Rt;qzfgJc)P}&!J9MB%^wz97sfI<8K-OkThNdes31At7@Rf5WU|B;C6GG=1u=UAj^15}#--CohujMuuTM9>Wl3`l$3'
 'Rw!76|807C!&6Dt3Qv&+e1SJNBq64=a)uK^-rUfVUhY2d`R)#>yi&BZYhqtEx0c31YZPKaB5b`V3U*L6<=W85t_{H11gemyge+vj'
 '%O;`B0U}2qTtk-6n>dO1T=xOe=My7+l#$tzZ5go1?=OL@S1US0NuV(4;rkJbdnl-8LTL)B97Ec?#Mu*291{koN#N}GvDn{AT%|iu'
 '4AhtbA>klHQG0)RtATiIUT$uY2g2p$@^aC*Vi6W!SWImyl?27)*|JcnI8_Vy@kuS>#|}uYnW$+a0^2#pZA8!?A5_f;z43{<otfIT'
 'f30o!8`{1PBJUqihWO;KmdeZD3rpANnlj{CO%L1T!;rcfBXXMCs`knMq@DVw+K#`IhVT&fyVYJlYC|j~Z{HF6zL(NuA5!{k0Nqy5'
 '&l<luH$JvhAw*kKVxrOof~_RU8TO%1Mi(S}-0Km$-Kon6QO@$GaZa28gXS3;W&mmo>rwzhK?o(`X`B}Yoo<I=&v(CY-+HMrYWD^T'
 'U7CjKUcC!v1OE(+tTqV2m<Pjdf8Z;N8vJj05whCFZ{IqL>JkhA`>d!*@hl9hjbIqi<T;3Nf0gN~7Ro!TOgNq@I0$WCWz<2Z5H@^X'
 'T?@mx9S5RRS~;%KFlTJ&S{Q0*0|vw=Nrh<+w?LxFT%*Bw4yqPjrM6oUX2^YG7>czw)TBlORH;O?kIh`x8Vxovj$#gxhJuoLqONy1'
 '^d*%0Y9*R7e1b^AXE;>FiZ)IkO=0>nnI3N+BT?Ii!zXN|(;!W`MJMGuV`U|h_J1_o14<&GnE1Y3@{%bCAeBDUlZl7mN(eMUC(`MO'
 '_Y&d(e4b?GU~+<MCLa`TvL{FHE47+`i3d)Cem|HgN~hqdZ{C!sU{@29!u{i&rc`kqvScN&#RV_d$QJ1xz`OeC138qt*CjO_yg-(<'
 'gr`2L<k*W+(-vFNaM%hLg#u%(77IMY_Eo+xvIiN|wC1SQBD2?gyo`gt2}=f+YYTpWxCo&p!V~yRL=o%EUTo;`@fhuRqU3`6RVg~n'
 'e$Wn;dougIzXeyqhQU4GBoONrG%tHlg(yZ*Fv=>aq#ms)Eb_{@xqoA75WU~4@QL?2gl85R$ZiaNgO?Ty-|&-mpa)W7kVZTTZdsDC'
 '=3{lE68a>7(XX^MwbG<F7P&ct4yCKgolg<5(9M0;wOt*&neHchT*B6i?)ysFDVFlk-*Zbz%PzJkrfxe$!-Qt+P%c@zt<i^eNzdOG'
 '(oII$ps+06Gu4!ry#V*R=C5g?A8Jj%sh#;}+MR!=0TKjDpCJnWv{vA=@D`=vc-<$AAjBpFD{d){=Bkj<7m?1KoGPcU8b2pJurDLC'
 '&WcB|6T|amyy}EG`Ert}Yb~uWX6uRkv{w35f<WlNUJoZ-4uXnZtDy9YEj2%UgNKM1I3`%b#1z`kZC9o@9FEs<V_<ld$NAusZnj?r'
 '#?@ubxS9v6&Sk#w9ze#kTkUQ>*|s5-WHDgIF$6oIps@HGjZ;uslU&%NArj$&rjh~NfXboLx6bM2=KJdU#o6YmZ|H{UvL~lIYyP5T'
 'IZo56Tb^wiCD*hXUcFp$8@go#M$>B448sfSmRqjrO`~iz>ZNkcX_iW!8wOsp6gCz)_>$u*fbe3y*xi^O41O4QraEorS5N%&?dsN6'
 '@6*qZYvYN2ZM-_DUXPBwgM9RH$F<Klwm-I3&I%t-zL)p%A6_2pPjAOxuZ#I#?~Kvb;MGRiAOAS|@pM?++IB}b``-&E#j{16Xl3v2'
 '%r5HVS>?h!oETfBu&_OQxmSxS_s)y2`A_Q0!^0oNt?1{*_C;&;yL~=0zVGIr);=gJvlsV`_WKR{<LjQi@Z#Oua(nh}boX>Rd9v<1'
 '_S3#qe7)L!Ro>Vl6Yai!R~;>k20w2X-o5|%sa^TFd$RWa!}j&s+tr?P@@V@9kB{y{WoK9Yu~Yw`oOSMY$2Y}F<Huod|HbZ?gX!Tx'
 'C8&;+x1Tnmofl`HUs<n9^_$IO_tUnghd;jm&<kXu?(F3k^XvO?Rat#k>bn=i@!QD1dAVTDj@*^O<M?KMWz&yp?T7xSFURH6a5ew('
 '?q~Vr;bXVddv#WN`uV=}W8G{-uU0np&K}oP_5I8Hm$kyXwY8IRx3#x^c)z(qCi=c-Pp$1&H?LMsoiClQ!-xLU$zF5i_~7GrZ}P(X'
 '9Oli@>G^~5Wx<~;w7=|*E9d%M;Hmj&@>*HFb<W<_K2#^_`@&lN<M`ry<gGvTKNjsT=W9O>UTuEaeLZRR$wWP;G07L+|MZUE-j!Yj'
 'Z%@tgd2n8eeqBe!#*gykRrCAz@9$qcO<#VsCtn)n!7oSOE*zil99hMiSLIq{zCKxbce`pis<XGT^2*w-pKZI}9sSq#&pl`1XyESF'
 '$wd06A0Izg-daEFh1Z8iA3v?FoL3un<%{y5c7L|%Za?iDhYMc&eD?Km;pcn%q?rHk{zdcGmyf4TVD3J=noN&7*IyK%=&|!ye{410'
 'f2xOt>(w>mV8c1~r(3nP7i6N>v%S6V{{2F0qyG5%QMp#Pt1D-(HyQ_>cFX9Lcm37K`}DH1>t9b_uh*M(f89S@c&go9tpEDnb)&C-'
 'Z|kJ-{`Qsc?R|F-8|%};`Q-cVV0`-_`Ze4yyT3*%C0%~E(AdBIxUL?l?_YmBc%hH0XP<k6FGr_4Uy854wD#Rm%`26T&R>Q1r>^;W'
 '_ttf{C;LiK^}iHeg3>kjpStzeKVROte)RdF`)K@h$N9tWtDCKxx1rzH&7Ue2?+<!(cJ|`M{n?9Bp!WCotA+L8#g2Nj`B7~&x8CpG'
 'w;p~t*G8j#a5`MOcvTv|-2QTN(K$G-RIZJq58E|!YkhUWzA3-#dN<a6rMKSMJ}$lvAI#p={;^`deY_?USrA;_{P=pjab9@c-QTu?'
 '{N7IVxi{<IE;#<rLN}^7)BW?+y)SR~-t8+l`N{g8Qw?_x+D&KeKH4u{SjO2=?Z#2Q?_3}KydNAru7%@wPX~qRyT(Vi{qg=wDIgQQ'
 '==Ex!rYq-0)p@8D-mf)|ORtV^_I9`KyWyj``ttnY$NE;!S&atyjmNj^XTM&*o1T9#Up(!dJxz}`K(3<$<@U?^4{NRa<?|%p%2$n('
 '_owd~PXGJYVE3doxTeBz{{7RAyRBF5rW;=m`jxHg@aX%tRo@B9FW#Pv>{?~;@p^4NKfCoB{>sM5>t^plsT@Z4g>LU<BV6BA7QWQG'
 'XE%e}ccUMr@2|hSvKC$pTE>n4x%#7C3|o2k>4{8qV;uThr!z-A*xY<~s2^{A-TK^V9Jhv(JM*k^t&jH`t=2(x<D{|kcp41ee%}1J'
 '5Vm$Vy7!K<{<4y9N0sXL<Aa;G2an~8;`K(mYdEWuHLtecsZ3v4Q+I#io=kLcT3l<GR$H;pW~J*N#=`r%b*FRpv~|96lz(@y_4WGa'
 '!uJd3)7Sm|uTkN!^?hYfx%+i;@v(KWa=t&?c=0$@4muaA`>wzKSl<|~PxHT4_QL8@XL!8&<AYxOrJs_C7M`5;W?|!Ft@-1zHaM(U'
 '%I){PUGGQbm45vG-E`rj8Qk5Lw~hx<>GR9eGj;dVs`I^Zu(@xZ?3Blas&Q@>f9!e}=fz&_<L$!xx9>&=X6^Pwy)JKjFLd*(gDSNQ'
 'A4ZY)(^zSj?ycFo=*9H$rm+3FJ39My(Fn!|z5Q7<+rPc-?#@2FwXC*Tn0#%&nBG;(r!VyF>D|Wl`oi|7^TV@^<IlIVtq;f3jx&0@'
 'T?#(E+BZ9c{mq5y!TAZ9Xz#$g?v$Qh-+BuNQRCx%ajT~5>g?&^{kFYw`{+j-J3qazmBQVx)7O>p)|cDswZZDf&%mDS*7K|3)97Hm'
 'bUgXIe^dE+xAF1(?(V2-y<7QyK3gb7E7PqN@AJz$sz=wG;k(0~g7vlfzIgrWQ|Wa5`^|Q1`lETYQ`&uBReznFegAOdZ?1iPY!-uG'
 'Uv#TJI~wlp8`jZeyY;2+PJ_;?`$p%}R$KpBbcT1;^|jgU^xi($`SnnGakRIhlZlM`%HgZ&?Pqgi<J`9V)m7`bQGD9i{4m};zL^Fm'
 'O7-Je;dt2lad2C=XG-(^sAEoV{PL%j*X6bAqfgbzLinq?u(9zlt%Uo{hj*X1UxwHAwDH<(Z?8YSvYu{sD35l{SA)*=;X*BcyYaK)'
 '^rugg(b4^jm&db<?Trt!=2m2kKCIqs>$A?Uofn0ldke=8U&a&l=cDuDUHSEg>ssq}PkCv(+wXREAI;631EbN3lt#W>&>xQ;yOC~_'
 'iDuLA^{@45_rhP<d>f5+hrPSd4-Oyfw?BizbT}I~Mu&d)Wp5`uDip?BorZ7MpE};PdA>U<HXiSObl1+Ohp)}UmACudkLA(p2k*r}'
 '&G6i_=J$((?_uND(Jh&%aQf<CWx96s;#0l*<>$)UuiJ$q{q?)U(!q;jbhG=eeL4zXoIK_))XLUZ(>Zv(fAjP0M86vxoWK13>y>jK'
 '96wwi`-Rov*HO(KhpU}vx9NZKd#i^B?}Hb`yW@aP^dlNHAKOnGwY6D)D?Dj6c5em?54+}8f3xxG<mJ=JxVUa_g<lr#7EXU22fIgy'
 '{-b-gy|LNQPon!TuO_FyQ`#xD)?RNqCBLg~RJ*gcul(-o*B_hir;nAN{wcL}>dE7a;l6Tk_AUy)zCCnag@cRQdw1(1*zz{MZ2k0J'
 '9T%?m?CaV?qrTwVpZX^+e}29Fcz+O{7tT7}`?ssbz3tk5W8l9YU2k}evkwm&M(g$UL%5-D{{*lL4>a7en#Y~fvq`h?Yu|mGzCZGh'
 'w!c)@KK6cg9#_JnokzX+bMpGftKqEM`f#%GQ1zm~UtjRIMi=9$_3>owRq5m8bG5Ml_;b7a;pNy|S!jKF{FGlmKRzhvuiG!~>suF;'
 'bi2*R*Nxub;`&p+zrAr_Z=5!R7xhouufL89FQeAsNV$90oPPP(K6?FWB|2`yD3%lt!mv?=yqlfq=m!%YU)fk{g!OK_NA{lSn;c8E'
 'l7kN$p~Aytu|k3wI1GjyJc-dsdd^<^SQ^{}rsI-6OE=-P5nYFap~Cw^1pkfX{{x>C-CEtCF(93Jjz#Np*aOBuLtJiQk1W$jvW&|l'
 'f2S2eJYygoGQd%gYW=7EcQ3v!gOmTa{NLlZ{~FzP5OoIM{#(9;J4j0K>f3+%xBs+n{~6?O=JgePAaLyNn1*K9nrS+k0XeKuDr<&o'
 'YnG)MWm_v-TFKK4&xU_x&9v~^)eOhcV3-3V%erR52ow6j^D<<=7JPaD%qu}ZX!1PG)J@HCpi2pcxiA;N*LBTx;R7ajHGJCz#yXY_'
 '|11rrf{Apz0U#!fvdfxlX^yGcy5{H(Obv4zC9UjeB@^a^`AP^1{sC65r&%z{hJSznOl-oHg|Kj#?r9Dp2moO%Wq=7-I3CiVjPKm&'
 'WzBIB82|>o02f?i85&?^rl*x4RX1Q1bb)auJakRXuz)<asku6|+8QDQ>vlC82;|tX8VA;G!!2Cml(0m%1haaY4XbexP3R9mYzt@z'
 'WVZpB;lj*-HuSPcH^3aJ0Ur*a0|=M^3J7N)C|II_ON1GKnHEk8D~E*w-mZ<LgH{{4fgHy=j;ocRqk{|usIYDjP|bo#ZIA#1`3<Xp'
 'fq<HgL@>1yK(wJR(A@?Qb_pj0<Pkhbk?jHUuyi1#sUv70C&-Tt)N`PV<07H49i}9pkSMS?ShwXmnhVpLz(Wfe?cg(@gNb}caw4$-'
 '9zOSw;K*-e8p1%dVf`SnHnP_;VP5D5(oxoc1BQ#7MBzo^!h|3+HcW2VC<iFa77T{fg78{^s0C}Z0k{qAHUPFkI&47L1|hcqA*%$4'
 'lyPC$AFfejP%cUc2e=NhOL&TU1CLN3J!}S0W#kQX0il6MwyR$~Y5$<TZ){nAQA|+gK(BzxAlH_GclZhaM>IjCKny@jKwNE<N&{F4'
 'oWNxPn}B>MHqc%I9Rq|7<UJA@o`Ou6W#|ZWF;U$OWC+j<C~LaNK)i?NKyU+SW)Vif!VRQ3i~(ktCejJofxZ?>qz<1bw;<Ry@CC?c'
 'Sg39Q0ZE1;4<dk+1}tna9VSrIM2+)Ge@QDsCGu&etQ|l?HPDf2DA8yS05~oUc!ER%96)qIlE4*!-dOMtTTKmB7by)_fH`Qm=^(cO'
 'd*};R%QSGI79lqPMYS><LTOY*6RGMDMxZ(&ZFIsCpt`LQV+q56+=wE`JK%weW|RmQZB$fbFkp#{F-?mw#6k-Lb2yrZ1{<gizzvX2'
 '0|p>>fXJ>vc<7>WhmnXa%;+G`(GXaK%YX;+!6K|REbNCWQl_jexrB{qMGeAK8-~NAhGSAbqX)qzuuBd|lmiM%jG{r<?ZCgXOZf}h'
 'WRwu3NB9gpg=XYPiSXD&GN4-9NIDn}U~DuYCA7-sU-RE2pH^C182=rlmMjA){@c#q2!Lr)?jsl`0cMFv04&QkkPt3myW>)>JCwgb'
 'He>->S%*joiU;9-%y|b0<-(nbj3kZ|W(EZXlLny5jPnkXwPX{nx;VRy){?LtCBZ?*08DVv8)El_>1YWY1I-)dyufu>or7?Iu`b}{'
 'qO~@t{J2!|P!`AnP^F28IA9eV^oOuSr-X~}h%^vEL2C$8ae*PLp#tNeqJSB6yhK_oM3hJk;88Y+Ac<0g;zz9k%!q*n&J5SE45#e;'
 'R+22eBuW#E@c=XTFQv-jR%K46TnLO@`&rpS8;x;~gQ{90@`bX6nuR6-IpLv9p$u_BvurA2CBz)YdMFMS5j7Ml2V5)?z-590^P^2A'
 '#>Dg-DmDg2O)eKILMXU(Fu;L1u?1(LrrrT-;=oc+wp=jNE-(}&*u{to`He9kk{FS&Z6a0<EZZqLM7%8I0Fe$NKY%*29p#D067m>q'
 'Dv>@6#6XgWXjmxI7*GI2#9n9Wh7t;xA(M%Wq2}NR$~g3~kpw6sB`zblRG8D^CdMO-rvd_4f?Y=8a53yeVFoI@Mv2H4x<-%>%d!&L'
 'Kq`YuIJi(ETR;d5ql{;~HM2L_cPSfWVRVATM=iE=DiUbdO^31?9H?bbGvr#-^td<%qachPP)|HGoftWR?=T5VQ8K6}u`obH*N*`w'
 'Xbo@)$xDR_Id7B<!b{x#ve1=dI9&D!18v5nGI1OhLIYIFE@7pmQ%8d?4mho&MWPx<j0Y-p8GD&b(LJVx4v~Ee(+4yml-j?gWc>L%'
 'N+Jb0#S9W}dQ_u;IvBSi#;_&}wI6j4SAp|;_#A~2Zs8KGxq(3rO1vIhbekwOAt;8sm>i&fy7*4MfdM8)DGs49ilPllL*h?rBau`V'
 'Mg+)75-wtH0>(`z-UC>~Jhn~5nDD^DupZ+@kZ7A=fbp(Dm|~N-8nwqG%z+OZl?3AfmuMfx@0eO(c#jO`Jj2)(MBYYYZ(?^eNG5Xv'
 'W+oE}(J+ifTOjcfd1#>}MRYxk&k(Ae@KyJSCRv`B;%_!b|96@~a-KhH%5SxVFch`G^0<yz$P%U}<q~0^XNy{5lWb4Y6dUuF5(%OH'
 '|I!$lqJO6`Wuh4vq!2FzcyOg5+JH&|Yr$X~T?11flQ<%eIx(h1s3~ZnMeRYQGGpCA*M(l6P@Ag`&;p|wR2H*j6FW|oiH2OLJ*Z4b'
 'P+%~DP4x$(Bvchab1Y0~97Gr8(L)|twyZtKDAXX7TE|Iv#*~O^5KfK%T+Tog6cUl49wT2f)GARa+@2>&<x!<V#@U#;qKcq`a)!H<'
 ';kJ#c3zHM{sivV0qqdR2#>GexeV>&f6eX&HO#M=7_YcnL*%S$lsZFAe5>YY~7sLqbIHX)*2`M76en?HCNl4K$wM0lJ8v|34?gI$S'
 'b<qpy`ajtHXOYAR$1RIEQvCE7H^h@r%Oi@*@id9-ln6c~q|s@>LNZoh3gQhp=s(!5e<dU*qJxDB%%_R}uq7%wx*1avspuHk2QhXD'
 'H609%Fw)lbf3OL^qb4GU6*$yUv;s`yMQ)?MVqBdNmE<}YJ|(0z7<o$u$u2M@K>w4bux@2g`S;@bOh!k=fCj{btOgYe2kUbfSz|pC'
 '-7H3esEk-o!pIac#MsuMk*9+ZGGOmu)QB2}nF;3b2;0Kw+50EK{abX)CPCLOWur?8ZxALBbW09F8E8!~25hlbiFGGdb79ER(75FO'
 'lO+Em(jtvT`np)O;q+w)a~iwEw^}jg#3qypsbkDB@-CPDNwWVE^XDXkh`m7(D`6EEF(^}KP@;$mL@!}jge4S;zl->jP|1ub?}B!_'
 'dWj?(WIbT09a4q)*DT_>th0=nOqtM}(q5-DC0V6M;vpdDKgjI==|sPiv;V<FC{cei(f@8m_)nY&2a)&YU=+eOT+j1N!zDmDw988{'
 'CRf@eL=^BBLwxwaLN<PYSY5&ArA`{Lx=x?s2NsN2Blg7*hk#+@J=)VHT>wcOL7=##dzt(-ux^hnzzfomcEQDEVqwFFLm#rXG8+hx'
 'yyS5V&m==ARMX+$EO9QK%w@1X6gw==v+-6u-eBWRP6Y{NgUrNfV=|O!UxTinAV3%55Q>#Vg5eF;K?I;KU#dmhvOt$OXpW6Z2HJ$i'
 'q^ZQ0#3#4N<W|gdPRkNsv_T)2$cI2nldgp{+O*M{8)J&HK|Ax+STW-{Y)hgu0Cgx+O%Bwe_cleuro6Ve@VEjdoMkS#EmP`H*-pAp'
 '&KowL&Xxt)CX~S;B~BSblrl;Jz8oeLh9DH4v~EM^h&m!6u{=d-V2O+YsrNFt!GSP2W3c#Y4JzTH-jc_RawV>+w#Y(@i;m5SBjIe&'
 'KDNY9+NaEsumxq)B`e_w=7g`sWAm3dJv<R;tcaeVf%1%uRfN96j3vfvn+hi5wWPr%W^Qar6-24?_zaeaYMDb5=QWrBl|&hfWtVk{'
 '+2#r(tr#6^4xN~36a_9)1{V*DTR4kKnjx<*OWaLqq(dodrc7p;+MJY(bHvLjouM|23mUgVHY2Y{LYE_Ma9K1com|0+Iui4_ZIErS'
 'B`LHm5!*;<0keXZERddHXKiYx4Q9n$i;i%Gb$F7YxA<~QP8dtj9*?U6(|BgPQVzgj_E<7~l8bT#Yf|PW))v^9bc_kdpk&Nz{c&C{'
 'iPWrQ&TeKIct>(@7GsV$52st1wMjn4<ipK52Pd=LU<ydBi3B6X5UQK8`esBdJSs5dwNU>XyK__YIn?gCG@2m+3>jF?fNK2)swL|h'
 'C$=T1NjZa6iK{atlWGa^3n#B(h;C5yE{5P89j+-Rw<2zWUoyz%BFCiHlA<b8?k$Q=;*4!UYM$w7%=hHfGw3RKq-KaAmLWuONfah`'
 'ai|)Y-0zt}IK)kwD=)+2lZoM#Y;|x8iZ&Yao{q1?lD!JnCTR?&C#D{2U<`sSOl~l(G7}s!ygFBEPl{t1!dzd(AX9WIkQ)%<Sp+9H'
 '(Q_<-P&g&Yl6bNVlvpfj2=RoO^1tT1A2d^T!;|d><$j6V4NKrU*Nd_k@Nf|{B*hS|Hn%WdBI%C69V2CUEXl3gQYK^0nH(=RIV{WJ'
 'BCJ0fwOgsEoeKx$gJJW5geab1FiR;rZ*%Ts(UGHUB{8clo1Rk2u$Xg8l_xA`^q_PyXjX@MEb=QBT1&K!a|Aaf9!W&OvUDmxG}6jx'
 '^PYA(0(WT`qw`hBfw+@Of-H%e<y4Gih#?&h#BAAd@_2?pwq^ezG9(sEQ?yAu0TTj_Qpyz>&t+<soEvaD*ol`fr!CcUlUaY7jIEOy'
 '>bRpEuvtPf$2sn1M#qMzzA3gC*=#YAd`&c#DT=d3n_D$ILzu1ka7fRL#(4Cjr;M5PJQyP@pVcLQYDpyrDcCK`=1F3Jow5YhGZMz='
 'lh*us8<~O_=h<dv!at9#;bjsnk#PI@)rwjjQ;V5uPs&?jMe`&doLXI?EtXguNEs0`BdAK4YfDtHxTQ=1qyb?m;hD|{8oDSQ+|{L}'
 'H%=IY=r2iKSfZ^bt<Uhz5aTVuny^MW3d^)ua!4pA0;#EFF_BPBEyPGk3zIWjk`r@2j<d!3iBXmUzminTN%CTeU%ZOr$Wq6-<0KUj'
 'CQNdK8;c$T;-n-}NGKB#(f?-3ax$e!*JfuVZW6t89(tLn%-KrvK^FOnxdCOIlSEP_$<3DIxF%iLGD_T^$Q+j4t0~k+Q;wJl8n2p`'
 'WPi?u*GT63ZI*x=?dfR^iRZEZHzdDdCVtzNRM(O!YL+ZjNkz?)Y?7=qa$Q(Yfv{5kOXO)u&T8#H)X0RGD2Whh@EXIQh6eZ1q*T*Q'
 '3dj~+s>d=_M=otiRX9tCy*YlCw1ULs8uLlJVPuZvD`WC(OSUQ_8x+b+5^RAryx3q!2^$;9Ipd{DL7I`+F?kuDltyt;^3pcS75E)f'
 '?zae-nMisPbdH@9>qJ?~XH%As*9kpVa@VDZ)0Rt$0yI;q#5l4{TXNEs6)2VDijh=PO6;&H6(TK}s`fl{;v7|mV5RDmwpi!Dw^~vr'
 'nmJB8WsBwBghp}%t4q!$P7ocj6q5FGX)kX5MU=?}!%M8H7<R-Zbt%5!VMi)>;`*Uy!qPdnZJ|<Zr1r@Kf#9WjOCB#(>65a!E^e_U'
 'n&nB44Y}ULePD{!rXlZr#1mV*v(zXc?nzZ}IauKVuP%X+7Z-1y8B*G8&g~1jsjABSW{|v@QBLhG((tfM)Q0WrIPyl_{2rJgl}k-w'
 'bB5zll6GY>ww#P|QXG=-wqoC#aLmfsZz+rQk+_g%ibd5_GVMr3TT60)hLDSSsr^=|$RZ^!cqpItaYV;01*1BR4nWRIf?T+9pgfo0'
 '!Xs{jJX#>ISgPi6zm>){*}lyvbf!Y%GJ|c4Xm~tWGI%&Eg-dY(#bK??IXHiys~*?>EkSx*<`hgpic(I&5e)<{WTe~y=LAE|Fr<BO'
 'n=-A;y{bE39uUlOOjVQVO|~3}36;&oPAW@@X^$<ax)YDKlF?o|VNJYi!b*9wz>+Y^AcUSW2O?-!@@i%(XSW2GlN#=%<TImu=E#+{'
 'bfs66SSLjnVJVK#Wqu9jT-;~IB#;nv<nlWU&nXF<%;C0(yeSp&&3Sdxld?LU!Ai&fWo~+698AI5mIT-6Wv?Uy71@q?bE((dL?yo1'
 '()>o;Gc#DyftL~$8eP~+GBXXk#3<e*6ldMEr?loa>{5Q&6~e;g2#FN3Wgf_}C7<s|M=etOXjVq7l~U+9EH&p(7o{S1c}K*M3F`gs'
 'C=8${>|~26oIJ>$Kem+KWRNh@MQ>e7#jIK9ZL*dnm+NF3VWjFtQaH>N#u7ZalN4N^@lTdiXtU###}v{sJ2R%VBwwK?(TKR&7&FpI'
 '6_~87Eg)$VPA;35(_D8lf*Fq=Hpt?-m%Yy-rmFF#znNjSxp<f<@kpg{k{QxjT5e_@e-TqxBRM5DCk)9M8*@HN(<LKNPLVw;t&@<l'
 'WTfQ1xzyeuFC)moL296xalFWk!zIZom3eS3BAZ&4gi!i4NoHfR`{^Xi6b@KCbAaI)VwJh~<ic)9ieJiHh%IdQCzQ1_j+}6%6@0^7'
 'vM72HBfYmT%96OM<S=B$PPDZA66aM)@{)X}oI1{#>Szch3R60el#PLz?w`g$%uG^8wrtwJEToD&QIO94lvv1Ya{pvy_K_n}Q{<_%'
 '^mG^NIjUPJ8qFt%VgfZs#uQ^@ITGU)!;}oX``aBg2F-9Kop!m$wo?ZZ=diNHijlm(uBXmZSkHhl=fPMR?s4vLg`M?S=D2)lhg)q+'
 '-V(?@f+Kq4B;}VQ_>6rhGgV0ws_ikEO?d^WuB`ZO2sE4P>aaexRJHO1-AJD${f(a4;)JnMI2nqTDWmg+qO!EXoEgKEWPWD}a~$p&'
 'sk6!RGF{4+X)i;j>3La0&&<AbexgEzmQ~i8*Y0N`=Zuba3gUBCI#spOrE|j>S{w&x8CLW;<m@za|A-aeD*dhRNGHaUU37(xg5?%Z'
 '^${FP&-b^oN<xP5oPFcFltzlprdR=CcA}hFy0PYuXS-QPAf*%~W$@)fP!f@3LrV){I%G(~9ohOBlI6BiXOoO)1Z0k@R)+un4ObmG'
 'RLMG+BMY0GoZ>Z2=|r6oTOKzx_p^*QpFK!D7o>^{_x{NEgvfT*223WA<=R0x^(stOl$7O>g*Q`#b16>hU6u@QmJT;%6Y{*dOih@i'
 '&Q|uy-TCC(O8I*uNx+_8t-K4ATCMz!j3tLU#<N=V7gJf;(U9@Hh`Sl@2RO2|OjUtRp)&4f)W%X+%g5k<TT8Yj*O;c0nc2t6IQ8tx'
 'k-3#R3@fdkN^?m%L*YsJjwiun2lPvHT3gz`_MUsYCSi|c?Eb>9q<|R`dosFsnO(~K7@#9H${P|ct3WW#@TB*NGDBu7r8icl-jx2V'
 '8KviQQ!87!jSM+0&4(j~BcERU3!7j1GdT^hMrFkBkQq{0C8L_;W*r`5)hk`v6n2xUktuCarhJc^<XAeZp|V|yxwA`F%I;;^Un}cu'
 'oHdsYm$K3`UhtSZ=_u@$+nGU@ytiY|zhEIts`!$kkVE_tO0oe*OR}ECAUC7_%wLNsOFiYvy(1YnOL(O%wQCqRTJtqXFSP?xN{&bH'
 'b7FDz+?5QM7!K;vYloTM!jr0xdTMtjqgr2jKD|!OXGl9m{G@YyY*7-etkA&AgqEDkbEH#I=G>-8LfO=d5stJ^nswOWc?OyK@A}wM'
 'Bw%I*EM{sK-pWV?-BceZYk$>vz6?5Fu}JOu>&Y9awouhJq*o5hsR~xA?328>lQNLZbkO5hy7Xp}GaqN`ypCnahs}kZo}~1f>C`RB'
 'x@WvynL3b=s#S}Jo(!3}bDJUQ^YE7B?dSL5O<R^d`M|j3&h*q4zmTkW>EK@6y|<)}M%FP&d;Z{+o_e3rOrKXb#lwuoy!@xCK#7U7'
 'rA`?KXq>E9$Wz-YY34XmZOfGVnDgnOp6(+b-Y_!Hr#a6bkV`q{j5BDS6x$>R42+C@8|j_M^eIVGektBah1`~O;Lnt5MDp8(8E+(~'
 'w|m9qNJop)C+m3a)-Yp7$;{I4MB9+1Qas6M8q#3|xeO!j6(=ewz0PGz`%k*OV<)Eqw!A4SZYr9#yme;Gop4IMIp<}(T<1#Bsh73i'
 'ZKe)JO53yYQjF&*VanTTj%WbpKs%`oP&&d%;(B)KCXruHI-tdhQ5HXP^Xw}QLijBl=d_;Rm7d?*jcv004FFc^*s_s24(ZIF&oT|^'
 '9LwCx@)@zWHFp>(m5$7pmCWa@LCO%9r6Y&7RHHUhFWaZL4%wSEMph(kOK%y9GL{OqMUN&iNZwtxQ;U_DA)ZPurw;zcagQZAg><X@'
 '^%Zu8Zx-=Mm3i$ylH1KX#-gX*OP5dV#fgU_+Rlt~2eB(Q{?H?RLd;6#H|f|-e$mZMztUvPk>xMeZ2WG`^Kk<|RAFX*&577UKI)#7'
 'ur2u{zYsNKJ12Iy;I}SRj9#S#>bZ^*(@m)^Vm$X+rk;8UEd6y3vd|l{mysngD*{W)pe+R+=A1vwj^pN?fGBK|SIp4ox#>LN{RdZK'
 't|htvD=SKIWfN#=hEzk7t3UB~rI<pID>1m@kwzgrWe2_tBm0$-tQxC);3PX-mg7XZB4wn{;T!XZTa5G@5SE0G1ScVy{rrw;O1gCE'
 'oklYW1Lb#cGtS?}-}ofww>m$qA%FFeDV?N`lNc-YEiYEaS7Bt;c#`)QWrt&Bx~h42a}G=Pt@iWBN;BT&)Ftol{qgnOxsD}4HEcm#'
 ';*O=cE$7TP4CerwsW+GAFtDC^#VI2P{3{I1zs11JKD%G09d(Haw(LiYXS{@w@ftio1DHNdnFY%hft2KpMqvXzwZE5TAC2_kRXM(}'
 'r1y+dL2Gu_V9tr9ohG1}N`O+Fu~Qz~mfjbaU|Hg8faPS{P}DG2J_jOx<%D6Tz8z-%O}oUd+w(E4k@>X%oLBbTk!vGe<uKBe&{M&V'
 '@f<|izx@WH@wX5S>5zu|r;s4q2iw2%!M}O$Asb>6w#ccxQA&NO#=PaSWLPP@tW@xmk;1#lX?R`S<w{<}&8k(DQ#I#5#@j~rq1*Ye'
 '*^twXRP3KR^;wd>S;k5STb7h%Nzs~-O17=vEWpTkjWY}N)Ym6vN8&Ot>)Dqd<}w9w!@^9zHtrE`>Lq8S;x7tw<hoVz`hlEb#vz2^'
 'JaZ=7Fw-?KC;1kZviLql>JU}dOBtzHR7%KGQKXsflM#jr8K#}GRPxu!8L66{9Hg09FCNN*Cl`iYIfP3ci8PYfEvqmrh9ly8aT!5X'
 'YJWdf5pm;vURPoQJjJgs9f$ov)a`uxZ`pWaKPA`g4Ex>IV5v9zZ~4D(<bRv^d*V6xHws$CdWapOMvnJf&IP$)Kj;j4-Tp9a6bD26'
 '%{^!yb%tR-oCfV)D<r>lH|o^jVIyqh+TpMt)pN~Oa6MR}lYHwm``tGF#C?4TC=GH^8v*9F*n?a!$ZfGs5da=`VQ$`u{ml2b4!gf`'
 's`u4;w;$rDo9xH;@sEAO3}LkwM15sVTUVFaFYw`Sl&|5BlHXqC*XgJDi{A1ti(9JJ4|`!S^vUnLBUoHql@p2nHeui=zv{Q8;g7*<'
 'Mf~CRN=<I?w4%*g>ggfmC*g&kExcK3bcgtJ?5gkc>w0`$BiA~158%;Y2CV_iSEDyI7*?s*=}jH_CU6xFEKoHLtHv*}E5KD;{FOe#'
 'z+rp7p__JPA7Hfuh5s2STgqO3Pt^hfhTf}Mt){A4olMv1_`D<jV3pL<z~2pUN%!QDVH#vC4(8<bFRv<t=(^MEwq|e*Ey$_+dt?+H'
 'r0c3i0MZW=KP-BO-{cI<ghROpz`u7h8$|V>rQ9!pIJQIO{$ADg)yjqcaJe|f-&(APgT<@LIpfXE(s-bZHE6tEyrRF+IL4VT)CwRJ'
 '4saN`fHC9;A_<0^(4Fou2OS>5ez)4|N9~}sctzAjYUs9t{-QVxS`HSk{CRR48X<V6bE#hmWTTIaE0uhjS4cilo^O`uZ`2bi<U*e;'
 '>H>sby8z(_De1<mMF}{EhX{PEtZO0rVajzv?s^^gg<K>vke{hs3VOY;(@>PfqeTto)9PJSoL?j4f)#BpUP<#4sv!>aA_EWJkcmsD'
 'lZC_aJPw1X5t4^WplgAl1*Xb>Vw2)CxbdN>u$K=E_yZp%bSs$b%2X?Z>yB^aq9*hNy07ZFur&yCMT3lHEF(=Xe4TJNXtfj=lpn6b'
 '1H@s7GY)Pj#$1?Vtncr&7|Fqn1|uo<vAt#;AE;V@?FBJQOh+s1XbKScbny!1^b`Hq0dZyYdcfH^u&cxjFi`%bf?wnhY9oAtqm}OQ'
 '^Gg0fRlW}Vc~e_Ye%`bZf$6-jj)T?+^yBg`RrE^RtG1(#zo!u*CI1CegaSrTt6yo<xm3gGI_&TX7Tx^bcXLr&bm0O%3<D^T0umb&'
 'egTAzn&8r^xC&IkS*P2M0_YJhi~ErJO<2F9Mt&??Z2Xx}YRY5N2)1^tjYX4&OTStAKv)Vw=PS5yShow>s^HI*LNB~51I>Xb2<?jx'
 '&vdmi4ygGPOd$ZNwYv4YfmVenJ5eXB()-w;Q8KIKM`aU+p-6)DYfy8tPVp;#$rEnm^Cm}9&@c*Doj15P=iZ;q>NdI`5;Q21eMJfV'
 'Oh0zvgW(FXL(uVyg45pDw$(QZ?VSIj3O4fZ<RAPPL|U4o{x6L3yc!b5@LR-LAT&0CDOk~0$dz%GYBIpC0}(Bwgg+EeD!V%Vr>4|L'
 '2)cj}eTd7dl#G6ccE$W4gdF(rhs!_J7k^)yfXdt;G(>mcBP!aQQm7h<+Wb^_1IU5#t5!R}*lN}H7pqnL_2FuD5%~`!><mGy=uaRs'
 'Wl@*duQ7u((+-O}PW8CDwsH1pZLhj<cyM-dxK~{}cwb%H+pF$XxAxYyPpe03r>Bc5jaIM2E@D5Mk5&h>cCFij7?XD)+#621ERM|$'
 ';bCwSHu`YghAy394iq`84+qp5--NjxCwHH#k80unMTlDOwrf!*AOp2HUL}3o!SF`x_HSWqyW9BIskcCWaz|j2klbjIs@13y4XagU'
 '5Vo4y*w?8d;@wi+A1~FH>fPQ<QPF2bgQznY2Az5ch6#bF)O{(B3jTZ%4Bb-3>JxSy)0W34l*V^tS|INY;y|YDgcGHXa>Mn$j?z(i'
 'fH@!U2pB@%JL>Z5OF$<uG6ak9Q-z85L%fEd(cnv{QHXV)E`g!XJval1$SXB<DF(b;zr4Hh>r2<+P`LvYfH<!(#zAZ<9I!-?Mo`si'
 'pUmj9nPWUU;Wfh}&JW^|u&&}*M1mp6Fd&qoPzIx#uo|9cz-^((5Rbd|GyAe$g(5zW`?g1|IU+qir6?mKMWY&QZfTQj!cprmWZo<&'
 ')JS*mu_RWDdO*$=CMcIfPTwJ?Z+`MS3KMjFhIYJ&VSf}hqH#8T@`~|h3(!mG)9X%n*AB&%8Bjr%I~o`jm748Uk_3S~l7$+v+*C=N'
 'M{+oT^WZ<^8EJEKvKZcHBL|}G$K+$ZgCXsi5Bk>wDWx2fM_~Q)`G{T`aCu8FO}M-xcqtg@-Kkl;i-V3@*zYJkvicsypr=+E;dLB<'
 'Ocmu0*h9sDB&|zzRfD0ys5JzOki?xlixqqf1wv8YQqV2|PLP|CE0_hA0Jkb{yT$A<ZZodnHg3BEbC9%|S6ZDV2dV$a!budz7T#Nu'
 'EJU#4M}(cV75|o8)K~nwIZ!;SxD)gAJj>J@1%s};fvtd#$`f`B=&Fri7$8j<5iXThGyuy1_(+CpK-{jvh%WHviq#atVU>Cn<>5h_'
 '5FQQugrpC=nn2?2hX)G$R$@ivgy!WChw=c6^<F-qq2!51Iy`6(BI73Tblg@ZZ)_MygSg2XQ`b(|I?=KLZlq?w*BJme3pHdZj1824'
 'Fc7mvjZ73E(`qzpL=XcA<3a*t05TAZcRpYc$a6k?KyKo(La03T6C(;S3h^|?lUkXH&oO{z&+p~u&_bX0e8ni<tN9tgynx^t1D=vf'
 ';AslYC5l#l`liGlLGPaW#?*T75AW~clR%*NRGwf0jF=FPs*xLm-;h#;Nz)Ykq#Y0)J{`N!c_w2J23;@-pnr+*jD>o^gOG|{klIMM'
 '-)7-`x7qadN_Y>U3$bL_u?ZnCP2IQFHa2PI-T}#|_qz~FvjiSHU1DvJUFuhaD@mIvx2Y92E00}i4qamfrH<G)PT>=|HCUX%Ep4rs'
 'jDz%@>MDjDI0OMLixKxyoi4H9)5IBL4d#eyb)VQfh^*NN$OM&IU0r1fHJUrT)sa>d0HAa?Na{i3c{G8lmk~1<O>7Q3qjuO2hFD)9'
 'RHdN_!S<@s#QLRw(CvhL=@2^8%sGkflx7nWV~RG%8i;@nlJK3;7s!zi55TAiah_XQ4!X0O72Za>uIS4YHvm+r^~2y!aEYV^93!DI'
 'B3~hd;S46t+`@#K($ub1Dps3YaWue77~zl;=CXOEE{ONnSCC5KgAjp%aqy{#gC4L?HE)6FeN`(>Na13(WQj2lL60Q_vy7-SifJyG'
 'NkhXb1NKrO$)+@q8Ur6Rk4Y*0yyc$-FiMq&2d0P@5))t`2p75^t>HgB5MUD~_e5iAv=}PrSDikAs|Gql^^GeQd<b)p{Sy_LiOY@)'
 'Ixv}*c$^96K9Y?aX!xh49SQbY^Od+jqSHU<EEIMZw_slgh5A0`2yy0*oom4$^c8G_tXYR-m|pHCmuDtiBY^w9FW>+!=i<^rgJI*J'
 'GT4&)H)WUPwsooF8Z;Z&$HYG+=s3;y-hj1)uHm!?iB{N%SIR#TFD-E{MMJyqtE&7YsEg%qq?ga(!Q;=`u6Abn@Hpx788ZB`Q!M50'
 'i>93iG}JeqTT0q@p<OX`+bJ3*bjpJtD3>hVE+WRRT>#gCquyYFy8st(i9gUThaD7vUDEUSg?TV+h+>ot2@gy6OmQ__U_KYO6wlBA'
 'O;t_o0B_xb<&d`GXVQu!<po=i_%%>4eru82JL({T{LuAfZUbE~NpaiJG{mi(u-T025hlSTO@<asl_B?q3>q@ce#kQ3px^IKa<v(~'
 'SYjHSRYDf3Iu{ypMIj+AEo4z)UpIUb9^65kXyuj2_YJk6+~Nn;D@be;Vnvs9Hq)I=+SyDxH?=11T<dm513#&X&j<&B22)jAH&|3M'
 '&ClR}@NfnXO*-&|MONFa_+@AWlq%MSuuKM#sL3NylSiT!AqEl%h;ed~ICFf&k|(VmXIl>tH`0n$G@T0!gdhh}>G6DM9D|SoWZ$m='
 'MV?e?ZdJr<n@mZ5x6t2G9)TxMzW)d|<4FaXqtq`7yfEn<p|U^(#F;aM0ORbU9C(>K>UYN>k)#Os0kKwwB2*l9i|Zi6gJDSAUeFl;'
 'a_t;ePtc3P`iCJCJg^4QfXi4rG5R+1-LflSPjjuCfsY|JF?z@AVEQ2i0-+g#Q_knx>72*r`xG!NPG#CGU9sSb5Vnm82dR9Z0TpdL'
 'PUpj5Vdo6u4~>K|%sF*PjS+u9+J*=+RmF=s^{5d-x;pUbm;qMfhSg5D!<vRt=^25e`>sx+VF$De#u0Cxu4bc)g@4+(+k%M3Ph8Ds'
 'Rcl850k_l;A0=&KG`c%iARmO_i5tl{Vc>%-aaW?motblxi1nxvE?3DCqhSOK0s8bqEE_h$eic%)eu(8u+*klJc3<ONXH}9z41B}='
 'ec6%K%WenV&c7BR&%PX1&o<9a)^;}EpRAE0<d>bpz0K;zr}fS1_U7R}G+s!>$X2%waU(57vYERe7Tv*8*cnItZs&6G@M!a3eQ)iw'
 'dhlt#dbV@2x%U2a@ycH`7AsP>{iFFF|2G@ta|OridV@Xf!P8b$;|)h}8<!lBgxX*>(1uYvjGscR+?(ONogRZRs7JloQnv@)qKA-!'
 'YDFDD;QC*;=h<Td^IM1K3B9Fim7QB495<J&C1;V?U^=_pY%Cexk`C0{UfbVa^Z8zeO{ysGeE`>pf@|f{T+-nG#u5fS??0T7@HEy1'
 'UPM5LKr%bF*-yiKOb~pZl}a&2?}XE#5>S(m!^gxnt1o;*jAb8ia?peTw}TqPSugaPt!^-c`1B1n0o8)m^%ABFnDqcs;wB&B7>|b='
 'mR(aJRMxd<s(~Q^{VCB@XMNpYzg))0%i8i4-8&y31hB(sE*Hm<RtutAZG2l?t&M|44S;Iv>-eEAfgisKdLgbKZCW&C+wX%Rg6LN-'
 ';V<rq3>4n16@iu*nA|65UdDYP2@$&LOEj4zv4mio$pTp2y4&)Z7%4cdwpJb05OTeGS;VDiB2;{!s#jW#bxKg9Ez};ZRROv19(uv&'
 'C7`R3^C@6*fR~sjsaJW1W8qT42kfavOWywCO>})TC^iO*6d=kyQuT4M0hYYl48eibq83`LVYdZoC7AieWg{$>wMDwC^t(Q!aEy|J'
 'X&bD6X)vmTn;7tN3qeR(+`~O}uv?_ZFc?C#qD4b8cH-m1>E&|KxT*}PbSd-^JmKJnD=?dzf=Vc{s0}%&FuK;pVO@|*+$>TA`3Z>l'
 'fb2xKi`oPv2P|s4!zP8!OBlYYeA0Gj6*F0w+0lmirLq%OktQ&E_ij;ZcaqtKQxkD5lZpuP2d7F3+ENjX6%SxSz~J&uyS-Y$X>mqR'
 '!)5axpuw;_=&=laD&m0wVTqB33Ib~c?HI!fFYm6ju`05OoEQ)mG5{X8(yQT`2dY3M7YAJ>VFBX++HhJ>V56xv@Zv8z(C(cQPRYh7'
 'uHp*`dnPO*pYY%>0UYn|ioqrslMknO!s+hnGPt^|U8O-3iS5jP$txIOQdeJ-YL$ttiyx_3tb%#;tGMFYM<Jum92Ww%iLQi{XTuKJ'
 'OvWR4`1KU{K|aX^y<&g)NBqf(JCg~aGAai^%TLs$V1Q;;!EFJ7X_LuP(3#<0kx*#3rW*#a3z$rnuYGWq$~Dn8#&+DSr*wquhCYAu'
 '=2~S09P_ObT-k(HlK8|a{xKH8wJZoRyGM}wb*JG#>yC!nAPoBT8~?073dvH3Lx{y8*$Qbird9&1*VQ2c?+4fH;Sd~4bJS`<D!8(O'
 'ynqKPIiNzc>wakvhK(v-D|pHVeW-tVvqS<l21w~^K}|y-ET!OwWT^BGMy(+!R<^p=<a4O|7%wd0AB7uuSOqybfQun)3a2o6h`YA@'
 'm;$t^mG#7L0FgxhxWsn82O%jMLv%>fs9*@9)S!nU0AaY)lS4)<7)|PXh&R*zHL5vzbdYy!yF`$FYQl&PsQE<4gf4kB5;GKgUc!^?'
 'B<`f&C~GP;fvYr|pI6{qyasN2B9$-Yr%zb|YKlEssCv4&`F>F&TNHT80a6DIX{Qn=&0t|FLqIImqG6Ss=TTHm;7f6+Yt7bZz~qS}'
 'c|*u4d%#SrSw$^ode;wpTQ9qL(IVc0)xW*d?pk2@p(jKQ8iWj7$f=wrws{yeG^GlPuFAXsQA{kg!th;Ph3@Kt6f@-#+zP%?nP}AG'
 '`8@17K-e*)2^Kw3i<WT}ap?`QV4hN~$iPvbv#e4Kl8DiBK$S%@HtJk2YHH#6DPrG(oTnW2)0)<u#Ja|`kq;tw;9F%;L5>rVE*fc}'
 'p}UzxJ9%%CdV;9<8L~sn0fWwE$Ip-<Y5`H#{|0I-Qv5<Al7)XLAj~%uFmCG7qz}HYTAK~SL7c7;(6nkn6fr)<GSKQ_3-V&NK#kZQ'
 '{KN2LnzFIEw^x0Cc(D0DQ<ud~IDy=#AM|I7T1;wfkuPR3UZ1wuBzizoe^}h_RgK$yiv91iS*)Yb<6g=ZxEpe$Cn}JWT<L8Xn;gU='
 'HWqrbnzq)``YPM>C#E}wC~oa5@vc>}n`N*W0LX8;5HAq>DaaPVd|!_*jVn|favG35QdbRHOj*2dL<2(a*%GFhJe3CWkLv$lrqW_s'
 'i>%RZf&nJK|B__?E?<^1<A2L~32atO;IOH$(1_&ohybf2jhRAKfEWl3SP51L&;3L}iv|Wj?r`X{M?A$MIVtvCrtPwG8Ts_-!Y?+g'
 'f;%e21x#+DR+t;nEgByqX*%UyIP+UUyVigZa9N3gEsRvjU{vBmrEv!WsWA{7-e|%9C8C2E_v9!NH)@J_tWx8fKHN+t3uP`kk{u0>'
 'T;@Ld?uFl5&i1d+%0V(}EF+e^Zcph6YKxmVw3%}S^_6aJH++<?C5Rmw1BDp3d1;5dI%rgfSS|qS5R=xpT*S{sh@MFK>(6l=c1wqL'
 '<Qa|b{s*BPvm2LuLn+>960fe}p1Fdbd#<x&rmlWtrU;POG;eA3OUOZ|ctDd{9&%daa*-JOMKbqj5C?nY{6Dx`8g*s_op%}wI}=eL'
 'v#S565hzgxAy57LsFR%rx&3q0dHX+(I+qE0iKY=b2YvB%q71&z4y^+{AxR_8RvhusPy8?n%3aZcEXTfLx=XE(|66;M-anCoUvjWt'
 '-iBp5c(>|1%c9ZneH2-2MehG~G=m^XR3yhxq_BiyBLSjZL^UE;Dr8$Nx?Ra_k2dOnFQ67<J|dzK$6Z#OK_<i6iyRcBVuA=lNZb!#'
 'hm0PhL<4Zu38m`XRy=|62s{2`w0z5iByIO7NcD;7Lkw&=hT&fV2x&h&ZbD8&WJb>wv*N06Xfzyy)iEihw7z5<6&Ok<ztS3AG>-!x'
 'Cni=j!0mM!;9=xfVP>+9XTX~gDW@|-DaM2_3`euhBvwG*T&1kc7{KQs9SD<HRCrunJHr^_Wb^%}jk6Dj2Q+R2T=>#~XP|ndau`37'
 'DM+J7#EAzHOM{!hbX@Xm=_Z^uqU&&gQKZD?=OR7oL1-KVw2qqWbo0v>Z$^Xun_AR)1JO;cHyhq`I~MpI;neevlSBO|-oGIq!%4ST'
 '9}$f!_PbrsA%U>D(;=jxLBEk>fo-naY0drzN1Zd{puc=ij}lDd+YA509fJ5AxE8;^Na%~joocla)<)OWDi-E30OgwlQK#8mQ7n9Y'
 'ZJEeo1cvSe^ca+Kv)}LbmBk}M<J_umEg6Q!>=z+N*a>PaP{n?DKZ-yCF>pOvJJ~!q^B04`b+t7+uU%}M+jq6DcY9(vZLi~9jL$}k'
 'yj%5jXU$)<!DNP3*|bVd-3;qNEeryyS+*?ObL+YrnDwCPct+sV?3(MD4ZCT1wOXy=1fgw*b{)WNY@VD|*DuaCPkqxXxej|mz<Uj^'
 ';pld)7B(7T$u7HY;98}!9k{x!yI#50XasuAG=rw;dZB9}aNV_Br`a%Sddbe*HNhx{AGoLzCraZTeq!=ZQA6PpjpY9{TwtSlM)T(p'
 '+!x2$jc`gP$zI5@gt%{<=KQ8FJLpL@6fH(0>a*fys{xLRr?dFDLZ2<Q@8C|M?`jN)9niulcnNTYNkRxVk%o)aY7?UEYE@mLBi>{h'
 'MiN0%GpEY$UZMH%{X{-U)#(o=iuDKS!3Y+@OEHMW&XxGJQ<j%Q9~cEq1pF3xaJfia!y+CCV>t^gGSWsC-*Rt2AF?}mPNUDXh$U-7'
 '2@^M}d8BwH1d0^cmG6_$DY{??=KHSg5|r`LWAdgDxq>`76&63y5zKwEur7W-kU_`CthDEI?@i8M#PdX{(mH}=IHf}*TB(M1a)GRj'
 '*zp{F#gA4jn_N#;^^AhQa9S@C4m(q-Bsvo38tmX+l3@`V5rqKL>L>5nuw8SKoBUmBl98GG4-=D$KpZ-j9&iH<X!|L-#$b=UxTsek'
 'v}>WpV9cUdAQtZ8q*%ba%3C~npronxL-Z%f(ZoiiVO)uUOR8dtRef6LU{qD5w-89R11JiOF^w6k#YewMJ_JDFl)OF}zcz}`Q0Xi;'
 '*>(x1s+b4Ig>QO1RhV;GJiJ0gs~^d-)sI$U5#X=Sl1kfUKf0<sv&$rs87s5tw7O68>hzwF6>q?;`TxsZspnoO_~S+uD=Vio?*WLi'
 'MM+3Ra7{Si(w`s0zA3=>*YLnm^!HyCfN&Z_3z8GU^zWMRr31I(YbtZqz7F4QV_Rk<A-$4t#2gSZmsOoU751kRna0`()eo52AG4Fl'
 '^p+RBX+DV1##-FSmO)hxxlfgHY1C`blho8#KzgP1BkfLGQ~ArwazaM4f}Es`b2%Q7Wn%C(dcLqKh~8jM#k4HBNd5zd3~na2KF`*<'
 'TVXH`g|p<X2*UoLnNd=>be6BEP`87@9W_9L9fGh?s1N`}epi?v=SD!f;1Q5{#m6a;8RX<4J}VektL!OUCUT)*QG&mGOEDp;c-a6I'
 'MuZBSP-wgGX-qHy(S-KW(LY>PoQGpxQROe3quMIizPfs=E*NRi?Q5|M&<tI2vHVp2mE=wn(Eg=e^2%3vg9tF?MwV!h<v4{FE{F;V'
 'LV+-XR?`qSsjx53AzVKvH3@C1JbXzWWy&KGTRgBVx+CAPY=@p6WvjGHwn>ij_69uYwj8w*4ukl%gztE@;DJ}R^Ux1{bkL)5)|>cb'
 'a3$>beK${f7EJm{|0by5FdyG>aZS@Hn>vkCVBiY0yfKrG@mb`eW#N>o^m{mjRaquJFVGK26bb+qjS#)HR_M5-znh08t-vGZbnuQW'
 '&=!E2dHQy|s}`VLeZyWXFXGLLA%6Ww^0hTAKq2`E@#U$S#qcJC^s(*ZDZi~xdwbR6>c-m1$%oC8>c*!tdb)3IZ|~&r@T_`pc<^=e'
 '<gj{l`o8+vpl5v8i`G%Yr+J*l-@GPqho2;Onh>kg_*@9ZrA9WC2i{s@0{z9Q201M%2>B|o3PfX_Q3O`F6%6q$c|10YFG#81txB%u'
 '2fp#f)*8MAe@Ffp?hIF>b$Pfp=?WlJuX6CveWku)RC2vlUAu>Wy}~`-)_sG#FlB4;t5tOH2-50qzg?xLN~`?5R4gD`EPz*<aH_o8'
 '4*J(HA>F#e*UPK)2q=mm{9~{sRYiT*=AP){qbgdys&Imq^vE0ZY<>eWD`?|y#fJkw*|_U<2hlJZhgJH{dvzH0+w|Bl|F!@c0c+Hb'
 'Pgy^*<uQ@tQYkD^HS9bX^@!|Y?+kd%OfWZ>wif&*ML#?h9O7&E#5~3L0|juuxys^N+MKs2-ccuNkJ?rKH5RG9^g|<{r&a2*xiB&Z'
 'E*7s6u^jl4ht}$??tp@CQb+1j`>gS_!H0|aZxSF7>D%}K33A<5b<`nWF9pEr-Bv5;`(Pn7dP%;NfXmAplME(Rc+~B%O4$g?7{H8S'
 'AK&ASMvz4g0}W5wQDQMjAy#+%kcM&nT3mvp%TX%|P1oNn(sI+Ei;<}jEO5!{Toa0q<eV|FLEHjy!-EEgoGcc$nq|o#LSW_D1yu}k'
 '8amnU=C%fH3b1tXugjDIl#|V)!)!RUc`&u-pzN=moqRa2o}Qg-uI<NQ=0z+`o75TX_|P>T#<pyod>=&h=y31i;Bf!L+FtV25Xr7O'
 'GUEACD=Xgo)lT&i*_(d)fBs*X$peu'
)
def sha(b):return hashlib.sha256(b).hexdigest()
def main(dest):
 raw=zlib.decompress(base64.b85decode(PAYLOAD))
 assert len(raw)==ARCHIVE_BYTES and sha(raw)==ARCHIVE_SHA
 files=json.loads(raw);assert set(files)==set(FILES)
 dest=Path(dest).resolve();dest.mkdir(parents=True,exist_ok=True)
 for name,text in files.items():
  assert Path(name).name==name
  b=text.encode();assert (len(b),sha(b))==FILES[name]
  p=dest/name
  if p.exists() and p.read_bytes()!=b:raise RuntimeError('Refusing to overwrite '+str(p))
  p.write_bytes(b)
 subprocess.run([sys.executable,'-B','-S','qverify.py','.'],cwd=dest,check=True)
 expected={
  'h5_q_certificate.json':(27865,'7d7d504bbedde84966a63894a6040679bdda0b22af267e6337bb06365fd1b084'),
  'h5_q_report.json':(68318,'d3a8162bd65120f4fcae461ec25b3a19dd44d340531bc9bd5eb4a208430ab147')}
 for name,pin in expected.items():
  b=(dest/name).read_bytes();assert (len(b),sha(b))==pin
 print('H5_Q_FULL_CARRIER_SOURCE_ONLY_RECOVERY_PASS')
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'h5_q_recovered')
```

## 9. Scientific boundary and useful continuation

This settles the entire q carrier interval, the entire two-cut square, all rooted primal trees, and all nonzero PSD metrics on the stated class. It does **not** settle arbitrary b,a,d,u,v, all rho, the whole positive-projective domain, the whole H5 incidence, or the global first E17 layer. No all-family S>=2 assertion is made. The global accepted interval **34<=Cmin<=622** and the separate attaining construction remain unchanged.

The moving-carrier mechanism is now two explicit actual tetrahedral defects rather than a frozen nine-vertex background. A useful independent continuation is a macroscopic d variation while retaining this full `(c,p,q)` domain: it changes the R-corner tetrahedron and its genuine moments, so the current 646 vectors and 36-block construction are exact reusable seeds, not automatically valid certificates. Lambda remains separate. On the domain settled here there is no complete one-sided survivor that would justify escalating to reciprocal coupling.

The evidence is an analytical reduction plus executed exhaustive rational certificates, not proof-assistant formalization. Every numerical gap is kept distinct from physical feasibility. All continuation-critical source/data are inline above; [the recovery bundle](sandbox:/mnt/data/h5_full_q_carrier_recovery.zip) and [the exact report](sandbox:/mnt/data/h5_full_q_carrier_report.json) are supplemental copies.
