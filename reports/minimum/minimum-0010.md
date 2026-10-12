# minimum-0010

AI research report · 2026-09-07 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# C30_REFLECTION_AFFINE_OBSTRUCTION_V1

## Determination

**I did not exclude all 74 combinatorial types and did not obtain a reflection-compatible reference-relative 110 control. The rigorous homogeneous bracket remains 30 <= C_min <= 1374.** The result is a complete, exact exclusion of a continuous geometric family at the requested boundary, not a failed-search impossibility claim:

> For the rational eight-vertex polytope Q0 specified below, every invertible affine deformation, evaluated at every reference satisfying full factor-1/3 reflection, fails strict nondegenerate 110. The true polars of these reference-translated affine images, which have (V,E,F)=(9,15,8), also fail strict 110. The exclusion quantifies over every positive-definite physical metric, with its inverse used on the polar, and every admissible reference. It does not impose a condition-number, aspect-ratio, direction-pool, root, or tree-pair restriction.

The exact certificate covers six pivot permutations, 2,333 complete shear boxes and 35,676 complete metric-ratio boxes. A separate executed result excludes **194 exact realizations representing 57 nonisomorphic C30 types**, each over all positive diagonal metrics and all reflection-admissible references. That representative coverage uses 1,764 complete metric boxes. It does **not** exclude those 57 types over arbitrary continuous realizations.

The durable successor is the theorem, its rational regression pair, and the complete generator/checker capsule below. All 74 types remain globally unresolved by this assignment. The continuous shape variables outside the excluded affine family are identified explicitly in Section 6.

## 1. Parent identities and evidence boundary

The supplied immutable evidence identities are:


[Encoded source block omitted; the code in this passage is incomplete.]


I use their scopes as supplied, not as claims that I regenerated their immutable payload hashes. The latest attached journal file actually read has 2,132,900 bytes and SHA-256 `7c4ad13f5959ea017e95d1351863cf05dee9f8cdc580780281670f683f43ece8`.

The lead's catalogue has 74 unrooted types, 4,372 stable-facet/unstable-vertex root-pair orbits and 1,994,223 complementary tree pairs passing its necessary filters; every root pair survives. My geometric exclusion neither replaces that catalogue nor promotes its necessary tree systems to realizations.

Atlas13's literal eight-point fixture is reference-relative 211, with polar 121; its full reflection does not make it 110 or volume-centered. I reused only its eight XY pairs, replaced the heights by exact coplanarity solutions, and rebuilt both hulls. Thus the new C30 pair is a new object, not a relabeling of that parent. No mathematical parent alias, incidence or class conflict was used. The nine-vector rank-two control is not used as three-dimensional geometry. The inherited joint R/r <= 27 theorem is not needed anywhere in the new exclusion.

## 2. Exact rational family and complete regression geometry

Call the selected input `CR62_Q8F9_75_D10`. Define Q0 = conv(q0,...,q7), with q_i=(X_i/100000,Y_i/100000,Z_i):

```text
 i        X_i        Y_i       Z_i
 0      100000          0      721910395/4119341288
 1       49679      49949     -1185206638675428677565734259/1298053226870709737680861078
 2       15628      58859     -211927521662634622686875087/649026613435354868840430539
 3      -13608      51027      1
 4      -32219      32539     -1/2
 5      -38247      10608     -1
 6      -33400      -8417      1/2
 7       24414     -42908      0
```

Its nine maximal facets, in the authoritative order defining polar vertex labels f=0,...,8, are:

```text
f0  0 1 2 3
f1  0 3 6 7
f2  0 7 1
f3  1 5 4 2
f4  1 7 5
f5  2 4 3
f6  3 4 6
f7  4 5 6
f8  5 7 6
```

Equivalently, prescribe Z3,Z4,Z5,Z6,Z7=(1,-1/2,-1,1/2,0), and solve the three displayed quadrilateral planarity equations for Z0,Z1,Z2. This is input record 75, denominator 10 and free integers `[10,-5,-10,5,0]` in the capsule. Its canonical descending-degree-block graph mask is `6216436`; no parent catalogue ordinal is presumed.

For a mechanically informative regression snapshot, use

```text
Q* = diag(1,1,1/1000) Q0,
P* = (Q*)^polar,
reference = (0,0,0).
```

This scaling does not restrict the affine-family theorem. For each listed facet f, its corresponding true polar vertex p_f is the unique solution of `q_i* dot p_f = 1` for the first three listed indices. These nine exact linear solves completely specify P*. The verifier independently enumerates every supporting triple of both point sets, groups maximal coplanar faces, checks every nonincidence strictly, and reconstructs true edges. It verifies `(Q*)^polar=P*` and `(P*)^polar=Q*`, not merely a candidate intersection list.

**All Q* true edges:**

```text
0-1 0-3 0-7 1-2 1-5 1-7 2-3 2-4
3-4 3-6 4-5 4-6 5-6 5-7 6-7
```

**All P* maximal facet cycles**, using the above p_f vertex labels:

```text
0 1 2
0 5 6 1
0 2 4 3
0 3 5
1 8 4 2
1 6 7 8
3 4 8 7
3 7 6 5
```

**All P* true edges:**

```text
0-1 0-2 0-3 0-5 1-2 1-6 1-8 2-4
3-4 3-5 3-7 4-8 5-6 6-7 7-8
```

The exact exhaustive census at the reference is:

| Body | (V,E,F) | (S,U,H) | Stable maximal faces | Unstable vertices | Saddle edges |
|---|---|---|---|---|---|
| Q* | (8,15,9) | (2,1,1) | {0,3,6,7}, {1,5,7} | 0 | 6-7 |
| P* | (9,15,8) | (1,2,1) | {0,1,2} | 1,4 | 1-8 |

All other true features are strictly excluded; no additional degenerate equilibrium is accepted. Internal triangulation diagonals are not edges. The generated fixture report records every exact face/vertex margin and every four-component true-edge test.

**Full reflection**, checked at all 8 x 9 vertex/facet incidences and nonincidences, is strict:

```text
min_(i,f) [3 + q_i* dot p_f]
 = 871481083334038811/6060555387724792432 > 0.

q_max = 6060555387724792432/17310185079840338485
      > 1/3.
```

The same cross-dot-product matrix proves strict reflection of P*. This is full inclusion, not an axial or sampled-direction substitute.

Actual uniform-volume integration gives

```text
g(Q*)_x =
11752027977937662474367583826548869833733841/
88318356370285421569705020584221617016400000 > 0.

-527/1000 < g(P*)_x < -526/1000.
```

The latter inequalities were also checked with exact Fractions. Approximate centroids are `(0.1330643873,0.1596611861,-0.000069683917)` and `(-0.5269576750,-0.8853334664,92.0244669442)`. At their respective actual centroids the exact classes are Q*: `(2,7,7)` and P*: `(6,2,6)`. Neither is a homogeneous 110 object.

For every outward facet fan, the program computes `W=sum det(a,b,c)>0`, `Vol=W/6`, and `g=sum det(a,b,c)(a+b+c)/(4W)`. Full rational volumes and all centroid components are regenerated inline by the capsule; no point-mass interpretation enters.

## 3. Exact all-reference reduction

Write `Q0={x:p_f dot x <= 1}` and `m_f=min_i p_f dot q_i`. Its complete factor-1/3 reflection-reference core is

```text
C3(Q0) = {c: p_f dot c <= (3+m_f)/4 for every f}.
```

Indeed, `-(Q0-c)/3 subset Q0-c` is equivalent to `(4c-q_i)/3 in Q0` for every vertex i. Testing all facets yields exactly the displayed inequalities. There is no sampling or loss at the core boundary.

For Q0 every right-hand side lies strictly between zero and one. Consequently the core is bounded and lies inside Q0; the exact enumeration finds **14 core vertices**. Every possible reference is their convex combination. Since `h_f(c)=1-p_f dot c>0`, the true polar of Q0-c has vertices `p_f/h_f(c)`.

The relevant escape numerators, on actual adjacent features, are

```text
D_ij(c) = (q_i-c) dot (q_j-q_i),
E_fg(c) = p_f dot [h_f(c)p_g-h_g(c)p_f].
```

After inserting a physical metric M, the first dot product uses M and the second uses M^(-1). The actual polar escape is E_fg divided by the positive number `h_f^2 h_g`. For each fixed M both numerators are affine in c. Therefore a nonpositive upper bound at all 14 core vertices proves the bound throughout the entire core, including its boundary.

### Closed-component obstruction

Suppose either actual vertex graph has two disjoint nonempty vertex sets, and every true edge directed out of either set has escape <= 0. In each set choose a vertex of largest squared radius in the relevant physical metric. Along every internal edge its outgoing derivative is strictly negative, because distinct endpoints satisfy

```text
2 v dot(w-v) = |w|^2-|v|^2-|w-v|^2 < 0.
```

All its outgoing external derivatives are nonpositive. It is therefore an unstable or degenerate equilibrium. The two disjoint sets force two such features, contradicting strict nondegenerate 110. This certificate does not preselect a root or a complementary tree pair. Zero primitive values are treated as nonpositive; boundary ties are not discarded.

For the regression audit, an actual edge i-j incident to facets f,g is a strict saddle precisely when `D_ij,D_ji,E_fg,E_gf` are all negative. The first pair puts the orthogonal foot inside the edge; the second puts its normal inside the two-facet normal cone. This supplies the complete true-edge audit in the same metric as the vertex and facet tests.

## 4. Complete coverage of every physical metric

Every SPD matrix has a pivoted LDL factorization, with some coordinate permutation Pi,

```text
M = Pi^T U^T diag(d1,d2,d3) U Pi,
U = [[1,a,b],[0,1,c],[0,0,1]],
d1,d2,d3 > 0,     a,b,c in [-1,1].
```

Choose the largest remaining Schur-complement diagonal as each pivot. The PSD two-by-two minor inequality bounds each elimination coefficient by one. All six coordinate permutations are covered, so no off-diagonal physical metric is omitted.

Normalize d1=1, put `u=d2/d1`, `t=d3/d1`, and compactify

```text
x=u/(1+u),  y=t/(1+t).
```

Every positive metric is represented with `(x,y) in (0,1)^2`. We certify the closed square, which also covers arbitrarily ill-conditioned limits.

For a core vertex and a fixed directed escape, write the coordinate products after applying U Pi as A0,A1,A2 on the Q side, and after applying U^(-T) Pi as B0,B1,B2 on the polar side. Multiplication by positive denominators yields sign-equivalent expressions

```text
A0(1-x)(1-y) + A1 x(1-y) + A2 y(1-x),
B0 x y       + B1 y(1-x) + B2 x(1-y).
```

These are reciprocal metric weights from one M, not independent primal/polar Gram choices.

For each shear box, every coefficient has an exact rational upper bound. The primal transformed coordinates are affine in `(a,b)` or c. The last dual coordinate is affine in `(c,zeta)`, where `zeta=ac-b`; after splitting at c=0, the image of the shear box in these variables is a trapezoid. A product of two affine forms on a convex polygon attains its maximum on the boundary: independent gradients give an indefinite Hessian; dependent gradients give a direction along which a maximizing point can move to the boundary. Each edge restriction is one quadratic, whose endpoint values and possible interior concave maximum are checked exactly.

The integer upper-bound checker is separate from the maximum selector. For `A s^2+B s+C <= 0` on `[0,1]`, it checks both endpoints and, when `A<0` and `0<B<-2A`, checks `4AC-B^2 >= 0`. Positive integer rescalings preserve all signs. Coefficient upper bounds may be rounded upward to integers; this only weakens the exclusion.

All compactified metric weights are nonnegative. Substituting these upper bounds therefore gives a valid bilinear upper bound, tested at all four corners of each metric box. Whenever two closed sets are certified, the complete box is excluded. Binary subdivisions are exact; separate prefix-tree checks prove that the shear and metric leaf lists are complete and prefix-free.

**Observed complete affine coverage:**

```text
permutation   shear boxes   metric boxes
012                 645           9869
021                 272           4412
102                 686           9388
120                 347           5237
201                  64           1651
210                 319           5119
TOTAL              2333          35676
```

Every leaf passed exact closed-component verification. Thus for every invertible T and every `c in C3(Q0)`, neither `T(Q0-c)` nor its true polar is strict 110. This includes all references of all affine images of Q0 satisfying reflection. It should **not** be expanded into an independently quantified all-reference affine-orbit theorem for P0: translating Q before polarity induces a projective, not generally affine, change of P.

The verifier separately reloads generated certificates, checks every partition and every outward closed-set edge inequality, and reconstructs both geometries. It shares geometry and coefficient-bound routines with the generator; this is not a claim of proof-assistant formalization or a completely independent clean-room implementation.

## 5. Additional executed coverage and reflection boundaries

The capsule contains 194 literal exact input records. Each consists of nine face-cycle strings, an integer denominator and five free height integers; the three coplanarity equations reconstruct the remaining heights. Every resulting Q and true polar was rebuilt by exhaustive supporting triples before its certificate was accepted.

All 194 have strict full reflection at zero and topology Q:(8,15,9), P:(9,15,8). All were excluded over **every positive diagonal physical metric and the complete corresponding reference core**, using 1,764 metric boxes. Exact graph canonicalization finds 57 types. Their P degree-pattern coverage is:

```text
(6,3,3,3,3,3,3,3,3):    3 represented types of 3
(5,4,3,3,3,3,3,3,3):   22 represented types of 24
(4,4,4,3,3,3,3,3,3):   32 represented types of 47
```

These are finite exact representatives with continuous metric/reference exclusions, **not** universal exclusions over the represented realization spaces. Numerical exploration helped choose inputs and partitions, but no floating-point infeasibility result is a premise of either exclusion theorem. The accepted source needs no numerical optimizer or external geometry library.

A useful analytic boundary fact is also available. For a nonpyramidal convex three-polytope, its actual volume centroid g lies in the interior of C3. To prove it, let a minimize a facet normal n, with `n dot a=l`, while the opposite supporting facet has height h. Cone the other facets from a. The actual positive tetrahedral weights give

```text
4 n dot g = l + sum lambda_T n dot(b+c+d) <= l+3h.
```

Equality requires every positive-volume base triangle to lie in that opposite facet. All other facets must then contain a, making the body a pyramid. Both C30 endpoint vectors here are nonpyramidal: an n-vertex pyramid has `2n-2` edges, giving 16 or 14 rather than 15. Hence any strict-110 reference on a reflection-core boundary could be moved slightly toward g while preserving strict mechanics and making reflection strict. This uses g only for the perturbation argument, not as the mechanical reference. The new certificates already cover the closed core directly, so they do not rely on removing this boundary.

## 6. Sharply delimited remaining geometric frontier

No new global C32 lower bound follows. The exact advance is that **metric change and reference change alone cannot solve the displayed Q0 family**. Any successful successor within its face lattice must change affine invariants.

For this specific nine-facet lattice, all strict realizations admit the following global nine-parameter affine chart. Normalize vertices 0,1,3,4 to `0,e1,e2,e3`; they are always affinely independent because 0,1,3 lie in one strict quadrilateral facet and 4 is nonincident. Then

```text
q0 = (0,0,0)
q1 = (1,0,0)
q2 = (a,b,0)
q3 = (0,1,0)
q4 = (0,0,1)
q5 = (u,v,1-u-(1-a)*v/b)
q6 = (r,s,t)
q7 = (r*z/t,y,z)
```

The nine variables are `(a,b,u,v,r,s,t,y,z)`, with necessarily `a>0,b>0,a+b>1,t>0,z>0`. All other actual supporting-facet and strict polygon-convexity inequalities must still be imposed. The formulas encode exactly the three quadrilateral planarity constraints; they are not a sufficient convexity test. No arbitrary finite bounds on these shape variables are licensed.

To reuse the reference-core machinery in this chart, translate by the arithmetic vertex mean, which is an interior auxiliary origin for a true convex vertex set; do not mistake that auxiliary origin for the volume centroid. Recompute actual facet poles and C3, and extend the same simultaneous metric bounds to variable-shape boxes. A complete type exclusion must cover all nine shape variables, core-vertex determinant changes and all relevant incidence boundaries. The other 73 types require their own complete realization charts. The fixed-shape result here is not a substitute for that work.

The most useful continuation is therefore variable-shape certification or a rational reflection-110 witness search in this explicit chart, with the true polar and the reciprocal metric relation enforced together. The supplied exact pair is a regression fixture for this continuation, not a 110 starting point.

## 7. Durable recovery capsule

Identity: `C30_REFLECTION_AFFINE_OBSTRUCTION_V1`. Executed environment: **CPython 3.13.5, standard library only**. Assertions must remain enabled. All 194 inputs, all 2,333 shear-partition paths, geometry reconstruction, mass integration, equilibrium audit, coefficient bounds, metric partitioning and certificate checks are inside the following complete source capsule. No journal file, graph library, former checkpoint or downloaded artifact is required.

Main source `c30_reflection_affine.py`: **25,495 bytes**, SHA-256 `16a4cf17e523e69b4535cf5c53362976a11be8ed0b9ee4ab7f0b4a878155b864`.

The encoded stream is base85(zlib level 9), after removal of ASCII whitespace: **17,460 bytes**, SHA-256 `97d3113791dca88f81074daa573320a287d9cb763a8a5bf8130493699b8e244c`. The embedded raw input table is **12,980 bytes**, SHA-256 `f8a616a9f519b6768bda94525005af08bf45bd8fd8d578de93942b35dbfe1602`; the embedded partition table is **29,639 bytes**, SHA-256 `f5146ca3081f0c1ea041478e38833bcbe2b3256f876c9023c6499e6e4777792e`.

Nondefault parameters are fixed in the source: affine input 75; the six lexicographically ordered coordinate permutations; shear domain `[-1,1]^3`; metric compactification domain `[0,1]^2`; widest-side midpoint subdivision with first-coordinate tie-breaking; diagonal search depth 20; affine per-shear metric search depth 16; regression Z scaling `1/1000`. The literal partition table, rather than any hidden discovery heuristic, is the affine checkpoint.

Save this complete block as `recover_c30.py`:

```python
from pathlib import Path
import base64, hashlib, zlib
PAYLOAD = r"""
c-p1C=bGxc5-9qgr+`gp8_XI^rorT#bL!iG6JRj5u}u!oek7aNYpuQK+%xk{V@st{sd7nz`Okm;lk&L6%}lnONwo{L>Nt_j7OI(X
E!k=}J9<+W|7A?o59(YLjGkY(=a&yNDk>>3q|6w3j*?0FU=#)Z@XJsYjWb@PNZv?`D~c0HRg^iBcd7@8HL`n}-zXfwBFe_OxDscq
z=|8ih~qBfj#C9zQH-2oBo&2~RhIc>$m~g4HPUmIUP>Y-sGml4&KmKM7fh?NGMGjtRe%sYaDuc^jWSD%GNTyT6~!_P%NQw^7k9r5
?K#WI#{R%4$>M^g;TT9Es~D%UxH2YGo>Xwp2N=lB=BiVh3?Q4bGAq!m(T(HADYsWQGK(1mQ8jX^VjKbtU^2K!RtZDO6xK+}tWjWh
#>OWS#Bd)LLNR0g6A8iRAPP{DJa^P+R(=`&^Pm41wE3qpsnG<Mzmh~*HD+%OfEUKB4g(jgiX#7jxpNqf!z5N-ZPfdVEHWEf)yJ(!
b$%bh(<^L7GkS*vI)L=<eRc3^xII&(!uq|~5p-j7Qh{LDLJ<W_IVc8QJjU^uVX4h*JT@58iFSg3i=mz3A=+|yA~kQux?UG*1ew6i
$%e%`=jmCV&ty{W1ebCv(|##Ywni13l{YnN1v<_j5?1e#E6p#<`Jz)ASwa~+oEyi1RwnX?T&}*)1iR#1ma>L*Hnt+;?#pqoIEil0
uznqH)Tz}}Eai`+Ef()NGmH|==8LP=Ae32}BkmLGwk;~-@=4A1P3URh=4V^V>gl)9V$^N+B*p@lh?km|@JaO-vMUdLHMnAz>M<IM
?b;OGUaQ{D+MSMxYhSu;y|w~qycbeJZMl(6g<3;fOU3!kG+V$;PWM5{(TDVKI@>19rL8CrY=cQ$Zlf-BYw={u=3Q}guKT8BNyZKP
jd%|ATKLL_Bu}Vgh8Oq2Q~*sxv))VKluifTk*)R6BP*p~w$==nHmd1zKJM7W+*B814M%g9oaTsQGi{5H^R6hux*I!BPdQHnw=1^^
my<+%Wl*>Mt<9^LIu#_;*p-7c+H(dhu6Ug67yM`P;*KWkrMQ`1WN9VHq4lKTxeiS{TU^D{iF~oWuN`W8vK7I{9G{On9PR_n^y_%{
a3Nxw{<eZrTg6a4mpo2!-tv0umGz_--{jE@MdqAqJ5opp85Qa7tkI=EH5|rEG3%_fs;YIXwU*0HdcH~^RB+D&bfiL(?a6jt-J7Ux
VjQ7*z4+;jREEWIt*{8s457B*Kg|!Vny|2rs8ui-9omDL;)=-~?UiDy#{^VYGRz*9p00a7om?i!G?ULt+(AAzy$Q8?A#A1!S09br
*^#fZaVMNYbZ4($i?v8JV)2I39@S~sw`TQz?o`6*P8}CKKndAh-;oIBeK>htP@%lPQ?;Q?iVlrV7qKv62aGLQJNsyxrRH~*CjB1k
V9%pL(-%z#Nh>eU))kMBa{6t!-!}~H_s4X?U@PS%$=-;j2h5ZmT}Q3Jxv?&pA`U_jk%V_9s?Mr^02Ep+B8x54Jy`7r&$)Cw)QD&+
8l1=M8GGMmGrQP%&=(vkax&H!9j=j1c`6kejvh-4EQSf=s(1=ZG1yy;2A35*u~Sobq`2AC^SSEL<DaLxanU<$)!S03U+XNIwOL@2
;SUI%5Bu7dQ3bc~JH=#=OGlTbR~*zYiZg!{+C%rgd}-tg(M<7b7ze4OB$|nB!xV|E+T+WzZpBSW_n;db_ooiD91Sgyr6^E=>p2pw
^hK^a8y&kX5f3+gsaQQK^*ljpCgVr<!fIWl%)a<#If~QXeQ#4pdfk~(FlHE^*UfWgXwHlV%Wf6*rjmQ#*mlL6JBq5Bk+T^;^)8oe
ChsEfQ@C0$M>A^0UMagx>%6-&J~a=Vm>3OW14fE_Mkr-tL%xeSDQ9-|La#GfuY>un!BJI|FbHCY?tC^((A!9{5-)E1jk=>ytxpGd
)@&X|X@7i0qz0&YoRgf@UDULUo$3l|ow~#xovKLdX{OsNE||4A9E7iEz3tD-&9QlVYS+4j(!s#vIn<#P%{6m*Ya-Gr)y2!*!Jbsa
Q!5_#apqYKjm%xwcKYn_3S@UG&a1w9O-VSe&Ga=%qvbeXpy&81+iy0j;U*=_J29j!i_`g#jy1cfLa%C&TTN*%u-(SQI?b;FCtq<F
C!&IEmGgFPWZ9OZhv9ZS%9m?r8`3?kdn4dqTA6ZzNtEn60bkI*a!*VI=u_K^n<y^1^VM32n<%MFDK0e0UTu^z<mS`h#=Z{v9Z9K6
w;8^Fv>sAtvLGiIX5njCf@yQFqS&M7;bd4nFJ^7d<wobtO?GWA4ovfH$r0w8QQu6eQJJDpY{w?!S(6UW+eMCXCI^-^;xPCcC$n>$
5{8|jecKfJ6RV?HJNcA$a!(I&7oM%xxEa8oEZ0?Me;N!#cLj4O&P79kdZ6AB)M1znH&YEVeJSQ<OksCiyBgg2+$3h_eg$=}2`O$U
?iswA^ZL@EoKvw{X5Q6c9T_^;(xAAjJ6yzUU@pu}(TnUGi=(W%?evsJHj7x3wtUZ16CFV_lFCPHK`wWdHr>>$*-5kI*|8!nd|98n
(VK0v0|OP^4+~1X)y4;G*ze1%QrSwhG`6OwWxKK=vzN<uIU2?alXI?NcgmqlD!@CrER~YRJ~b1xo^z#Lt&nsf>N;|mj`JmJC|<50
{5X|fG0q`A4qy5Pe{(@M*Yp}>ZECG~ZPYqQfM3^Dzsb+q+-2G9>hR<V$xn*4b2-ipPDdv%gg2JfIyqrVr<27$N|AEa=Ju4b7L+WW
x<cN@j)Em|+8<@@^BvtT8Iav(PEC70BF>$;x}|>zT`k@9YO~Jeug+8i_a?|7Q$Am}N^D+U7pP@A={s4vr8Q-XGPX*09BH~s&W12r
HBI=o%kNKhgqY-N+iZ-Z_I5F{t9A^nOSO!n7o?N!3zc?kkQ=T~r;*1&`jM2!)?!op?()cn8X`*Lsq*-=S*Gw3HR{s)h?S!+Ia4xD
)*|gposU`V+w#WUOl+tGW1bxdW)dDo_~>M2p!%iJX)-89-E&8^YYlnMnYd7@98n>DE(J#6;JFmF6gEe(ma7yQIb3bYY|>SbR)Wbj
laNq>zNEa9(LTJH#RlY7Y+J1>D$Rz>&CF)w7?Fb`o-qi4dd2Li^wud(LNA4UF)^vP6CAqVjLX|LncXJIzOu5_V>Z7hQOtRd)aep)
P67i<z%LN0FVD@olw~8WdFPr%^Wj`j_E;@Ud_?B0<7AkMBLUPfJQcUuMCMo@H6q&{YD(7XUdJ*<c#id=+8K=2WOBdj`5c1ChD|Z+
D(doVE3-y5c?`A=R+m3cvu4Lyom3~`^09sCl~F=C?&WhZ9YyzNykBC(nn5W?ZKquvPj%11)Gps#RBLVjro7B?<k4lNq`*n(=JVrb
Rj9~CYu#Pw1gM$2O<P@?L2sM(+m4l7?9w0ZsY8<W2Fzly))3sYwU|>^<$ScaZ8a~3Y_%rY^PwRcU(n{A5MY-p*Ze%Hi>cY7COBhm
B;LuyT2e3G_C<0F5ns;Cw5u{bh?{i)4duMs_@?c1=aPI@GB=tFU$E!1coL!DsU<Hxg*Xb<W*BV)=d+j%UHq-W78&f*-6PXUkDL+2
Ne5lwzUd_A&g-zB7)!W|o0(e9dZ|T@gYCeXrpmcOq@1+*o33Hj(e^hl!{d0I%>?GHLwVqz3L9x7bebE3J;xz_u6UxET{kpQrHE4K
*-vAT08>7aWxU~#y&KqNW$UF$DW%kGKN3%;c6AUrdryPTG&ZrOlGk27k{qg1j}L9q$>4ssr+QmC8lu9MYTa&M8N!WJw-KoK65bPg
*yPhQ`=H;OIn>s8pJ#loHI6frwpM2tWO7Hqg#H%;YNVAUgJKKO^ZZ{_&<7hC7Ww%2wE(pb0yFwwiUg`G1O@-xbAFx`5P%0I2;3bC
x{RO(G~ViiU&@?x`}|t>uQ|JCxEZT}(FE}^4U&G`Pll#GJVf~e{vgGWA+OKvbGdxv)D@(rULVB-r%aIX1%eD4@`Su@%Hw0GDU17E
?hgZqz@2uBfF;N;UL+Yso5s)|5MK!Hg8yJH6hpire;|Z;Lm@9HyAa&xcLy<FFzADCPTb>nfmht+4!~EB+l_}XkK5<bdObn6H-O<T
0HeKnya1;&=*1zh+v~->nA7VHf!=R}p`K{AUuvH9m8{jo=GaFBr`1KMeMzzVgll_tdmX99_Hw%V96hDf6zl$(ujx(Vo|Y;*L$NSA
Iu~ibm9=LGz9$7!R*xw#!p#nLI4W-vx&F*Y*c+?bs74sPp;dN|^OqInLz9GTis0w+-d^5&24bx;SsezZ4C&7bWTt;`xQ^GkYd9g<
ewrn-sZFa?EVWE#H;!(yvk_SgwAGV)f?BGB7(4X3BWBxrG_Ly7h8bnbtg>!$EJpL;c&1Y|Raey`l}bzDp)D&|?DbGT!=lt`=0sVw
ysr2{Y+%|@@Td*3<eW4!oy2elEtE*A<4}^`jo=9Q7+Z=F-MowGmGg2$H2AX9-e_ey4)(jt5J~Wrpy#;tR1+J!EK}=+r)Q#Co>Ng=
;kKSLTA7&Ei}5wkC$l58e4KDp`A~DtmZ8OF)Wg@QVX)QpuSc}hDIDT-knY3^p0LwU8m>v)7mS51vthY@J^HS;XhMvoSf{f(CK~xj
YCBFd5p&YF3|SjRJMT%&^60MII-XpKewk_$V~f0~nTE|aZ6B?=2vf{jlgHX{+4q%#leBsyu7+raL4xx`C4lB*h_K2XuKp2M$mXj%
dAE+*Cnn0($z;swO~=~l^rP*ZTAr)hR>p<)GYyM^xZ~TsP_)W;ZGb0*^2u56%l3AXi8%6Hxf*O&*kRJ(sKwjdI7hOoU>zl=JkQv(
p@=2a-W(&V-B8%|#87yYJ0EhJ%y>C>ERRYiSWJjhdVI;Rlk#Bc-bOfUSxCsW^r3HARgU&l$m_{BH=zEXMYvv|Y3RjlW!2}Q%AKV*
!5<^RV<VRya3^cJSF!d?{=IZO?E1h#`H8$I=(zS)c(ZGvkJd{ov$ylXYa(8$cgwuT-{~^`K<~I`y#0~I)+HKeyFYI6Gn<(~9IDnR
n?6qn)~?2?_Q5IYJX-tpQtr5I7f<qbi1%%^21hwmW<O86a-Ga@9TA6Dx$I;6u4;YKR&8P~U04oI=gwj1ib|%|LG~BPL_S8h{hgLH
G>D;#G*9*gvSvaOm4J6rOjbN;A1G|PsZGsVa*vz`dXnHxVvw`?1D>+87f$XMr%<KhnTCV;i-kI@yrLH^_mZ`8Yi3o}*^^U6`t4(p
LAy@I?70~1ZicJ`uPi9i4lSlM%N6Gire9lCSHpG3AK9j*jfmFVRZrt=b-8AO9BP!~sY4OpgW`<|&Ae{4)yb8Sv!B@Dfn9@XaM$ZH
*qK}`1t(F9XQR~GkT@3C%lNQ6iU)F5f3i`WEVF$FN>N+8s}my{hfsVU&n!&+V`#6kr8B$RXArTetU}=|p`;cyCb0!YY@u807P~p;
EIYML2K6GyEO!1~=eUT()Rn<<N+!<{yfjSGmryJ{4qH6a^(Ga_A$FUa-(-2bWpPz<Rc167$$}WAkmAm(N@d9zUwe-ok|0aYnbXtZ
O&y^<I;ifQ6!z?n;R3SXb-5aKOf$G4VD`FCzzwWz^;MUWNKcz}to!wmEnq?Hwb<fnzcBR{+gf{5;g~%aN`}Uf%_(t0dY4fRZE!YG
b}@)=ab5?u6)Kby&e`QSdGJl;;XKlgrO)Ty$<XN4=O*WtIMX~uyW|uoh<llN*P2M7tFF!BU$B{-SZA!WF_j+8TNG0=mAKO~yGoYn
tlADZ%3kku*G<gB8#139Al+1{Q7rWKr+k1YR$ASRK-3Jg!K{$<`OaIHKa)h&R6#uVT8-n1=X$eLC*&UwmYbrzbUEd_Y><{#{f4zz
+*Kx{a(CUF+iP-pW3|a-c5*0Ioa0N-WXX?W{F&RB<MXJW%-OEltD%z*3bg%fajnX1XT9;X*X>#Sm=yX_rM>M}L$MOO+zpCBvU74c
l3TxAwU6VibRDG0UAZ2MR4j{-cT`~0l#=15D&8!Pw|u?HALmEP++F7*jq}Nnp&J$^S&g#ISey*Sgtm+@B9ZK><>Au8`_y`%CXEC6
rKdb9S<%)i62Z|<@5D3;LA=K;kDZLWmQRYyq{<Z*NxBhf4a?JV#kL2fQgvuXi`zoX5b`JNlY&@IjYTq_+w{bA^SnHA*=k1;1DjCX
BW+6ch2$@w7j@>K=JsB{>{LdDjx|r&$b&eH*F(s7<~{CeK_u_@X8nFsX|ckcmgQ+RzZ4D|r^#R&<44ofR!uitYsW!dsicEErwUR%
J?~BWO+V+%$B}X<2Iz<s-SzrXS-EGUT4X}Sa_)8WdO2)X*X#JuWBi@;_&6<esrb^{Bm-i(S|K*uu(bv3<Z=y#>gH0S=xLc#{#A5@
R7#d;hjUqnvj!1ctjKV~b*2)*iKlCcT9=nd*xj1VsOk)v+fpb0@#4=O0{(I^Bea{UTv4;**d~)Xd&o_<zBUc2g`$Biv)hxsXlYjy
<f$XhSCN!bo{$+~fwKcgW>za(B&Rza*%xP=H`#JCYD0|6{uEzJ&+4mmB5x<X#XwfHNJ?C-PG&oyXfl(Ts4Y#MkD-C7K*$S&H))ju
{!((E!yALk+Aa2S-qJ?yMt#{K>+2>bjXAxf@MsH}Pn~A#YS&-zekSXbPwuM?UGJjtfOQ+k@r$MCsMk*2lE<=+xaVygcSLtvJRC3h
@`hof5JqhoPdu1&;w#ITmAtDM9SqfK!@)sdeD$4FYaPd<)tVfeOhY?m@3zXGtkY(_B&%k0o6V`c8M~YK`{>@>aAs{Ab0V~B#7q7>
SE?NBp|nXgtWoDd5$RPw(G55Ywm>Ut+soTPsC;rug3at3)#jonswS62SE=Rgl|E0Iw_=Z+I(MZ+be&4pPJ`m8#8Yc3Q+ICyX3FI4
9t*QnO>%^|Lw&YuR19h*5NU1WbgXXel$S{960kJpheCOCLN9B=OGQrMJlXMdC1K(ivz?HcMiJ%ec16=Cb)OW6M7voO=m68McNNuH
Qeq9!D%o@4En1g$yF)MTbOjCDRnE@@$`UKv7l~}yVRoQw)gAY_J0N_sE^9P%>YaV7RZQB~>myk>DpbK&XU)#s=3KLw<$5lBm^L%v
b^BC`pE^_acqIy4MyQv^S1Vgy<h?z`pgKE#G!ml8+~8V5Cdp%YHZ6O+4r?rV=(zVLKiOx1iM0dAvEP#AnuCmYc<oMv3$2{Eh3PD_
{G7LK8&zwz8EB{lX-_DY&XM2xx5acxY2u;G(%>9O1)I5|%$BZd#^v@V7ZPe;H0n_o8YP^x$A4@M{59)vvk4J&|60ixrjdAePzyE5
+BwmyhH*mbDeT0m6kQc(W*g<={t=$cHwPv2#gR=HO8%GuU~;%h^0eP<v0Gcr+a;={$@Sc8q(+-cDri>M=X%293siljV%Kx(U#03~
!PH8dX1ZFKdem!jYQFG|DqWe@_s3cO5ZaeFkt?<C4<ho3tDPE=ilJzqx=$8lbM`L+0<%<Pe`cTSHkHPJV7tLqoY?lVs+yUXTz$S&
ZSTeAByr_>pjNW?gN4|^Ka|C`)n6}Lcfo7KWL;)#jSzLg$NX$%pEsFulJyu`dyCtdUW%=vzYrw|)Mmp)cT_eXr@mT-=W>~BY>HRA
e4uc#1dk+s@@4G%1Raj7m7GwoDSr2fW31K?o^YHT60z<E%puA-Zy%GV-i*nH1k++@Aa=)Ob$%VSw&}V(mE!{ej*LYTYH5xhvgESd
cO`OsJhCcS#R_%Kl>H}a?{*W_{XP-yn&?W{YD?tPw$`XU2{zTxip}=9vBSGU4~rg7&=zqZxeWaaRUaSc-b5_w7%@O!SEllDsT`>=
F+Aa7sAh5m+c9gc=C6k;1nmg<T8-$znHx7xQptwTEgnK<%cl^-2xPD~sx~RJqwb1d^5)V$m$bEO=h)IP80~m(C2Ma6CzYv<J!e)_
j})ZHysFIV1Rt_)k-RtW_oPpLk1KncTS9KmGOVWK*&=H8)&dF|ca(Rir`3zi)=@sq3#%lpRB#unID7pW+Dzv|h7CU0`v*8H)K-OF
&(B6jq4a?>(Z_)wITu)0O)$?Sb7yVh*$By2XW6|1RH02o<zBUXHd``w+|BGMxiV%@B0_cZG)JVXo6r&AM<p)pAv%MZq2!p<i#F*z
YnDi&;>q`~M5h}}qC;E8Vu_k&6W{LG^f-GKd$pfVihPE!%BL+kOr=hW67evuxo_&7n$|5v@l4_%b5M3J*JiUUyZiA))L!t!&k=)I
SE!+j+>~;aPO@uOXp1T1DzwT=S?P2#q3q?-61Fw8AL-eA<|0?G&@?G~>^U`;9SBuf4taaFOWcv%s~0LeoP<^_D^R^Y*Ud&^*Xv|i
r#e+bIu(=FGxw;;3H+p(Umg#^Zt|FFp9&Ky9L*&{jbjckbP&XbZf1+>P)TG;z3d{lE@qwa2%a1!rBjvjySgDyJzq}^TPb&tZJ2{K
|9r(>akXXlrVQs?e7Pedo{VBG_fLzAb0lY`?J%#@m~E3?GV4);m&yUem9+=M`7NLFkI1^yzPH6U{bcQ!LMOs#7Cc_P!(1#}t0MB{
G6}`(+)R`z-tjs>^Nprqvlo%E6d0H7<T=#NMaN6zx=s6oC3fxRoY_SI4LBTo@1fd`C{_|N9fs}3t~Rye*I+EMZ_K-bcf9Q>j+o%G
nMxCPli~8V`Ob6kS!?@xw`wkmIYTZ<UMj&}rg>HpLB8l=Ok&1YxTbr7(0NhHyC@TjkJ(y(+7`lyYwDgSL)QMD!|m#NH9{6aHJPFd
L|j(e)3$SXYG<~)M%5H>O;)vpjo*uG6%80B4XHj1hYR7OnX{6a<f*z;MjfI@Y?7B%w-!E(XtZY!9+nCo5s!or^ZF|GT3xp1gSfXb
$Pee!P+&6ZSt8};$zJeT<|;!obIx*fpSx*uYPX4J48pF(bQS_%*pV50zFzcBU49?#DCgtx$gB!Y@0_wT*Bui@eg1WRRkN|SP#r1f
&HamD!vn>B=Gd6*#p-aS?3RatY6;C9$+16VZSFd_U_G(tXw_hrBB==F93;^^5kc#zR<_i1QXp}mgImTF@#HS`Q$`LQw^@(NZsYvn
=`qvs?4y)vQjF0FRfq)Z5qadM_UBVI$s?v=GFaN;3LCa((@0@4a2FkhN@o)usfXs+9i7#E`C|Rr<oC6Zv<q{Bt$M0wPi-VgDMTn~
-H%+|NfJGYn}vOND7s^V{$A~GyB<Y4NhyC>IUy&}cL+>9)5<cCh?mw0P%9)`C&RH(X2NyfvEe;#gP>fJx1)1GYOIF)a(a;)GUzlg
-nXVxa<Wpc%~5SdXVdMx$&&QA`ysEKo0!LqN`Y9b4z@5m*EX%F!$hU4thp55kt=hIC`aN3F`J2GTpQOR&Y$erysc3jo{{_{*9k10
vhCy{(7rE0k<RWQ-NBn`myX)z-YH!n=?vmH?6^WQ9Wkdk_B{3X6I3TBUUM{XEcQ^4UCF6NM2LwCLpVegdTNC$pxNnqZH{Gw_<$^W
)J}MT#C^eSb}hxmc(QjOT&G4}OiM|eAC`rU=TfoeXK0~{I`_?7%U$k8ExR&(viYjBy%cC$6?<n>YmCfmu4k|^;gbWDS8dv#MrQmj
-Kd%+5<hm#Y-#QN|FNNY-?IC!o0{&B-xK<`o0>k{>!(SND~L~BG|rMPFYXNlSx+$N@lZ6yx+xDBIt>Q=bjaoQ(0*?y#QIrp0Q?hj
vme?nVgX*T`F&&4z_3#zBdQ3AQRt`4svB7_Dw`F8?Cl5RRFsW->|o>s<B^jz7!=DQF7!4~*-&o-)s4in$lm$qk@^^tVg5A6@!!U*
HavJ$e~z)M`WQHZyn)iP2&D5m0YZM^-*)QD{p}>dAMk{KW49+4Y;)<o*zF02ZMfchXAr9~2%{fJb(ZOq!S*{tM1IR62{^mK$PjRx
J%JjG+|&p!^Dy_}RZ(CK#@mawI>;69AAHuaCLoy!Ko^Q>lwhx2ZrJ70y6|uGz0U>vaIMb``|y958+EeGPLTv8EkS(o9MCTr)i@|a
4ko_CMv2=JU*BPla2d3Y1?-SXVa6g*d9^v=c;k`~*u9D%OAT!K1miFb5Jlmd6JN{kuLU3lt{1QYwk_esEBO9Ni-O7t8^8zv$U&-?
-vs=F!PhWJzz;Ay3_ppl{XgVW+_32z4E!<sZEi@RHkXOuv}Yqp+-M1FvwZEH<nQ|Zm>Y$t0WW@$lEexOvOvR}gTVC#a0H=G^GV4p
xqOH*fq@Y^qp1zYGsslIrZUT7X-LohKz!+Hn??4Rew2VdmLqA85`63rzQeM(Q;09g0bp?yd-m-Q-{BMxkS?4lNwctZs=zg>GDpCc
uTKwHB=H4tfTch{4nl!`xGJ;pIOd!ZPYSG&R6!Tv3L7a>KG3WHK<L-2X2vZ?f^npvNTR~(%6;RxhEki(^ZBi@m?CuL*YpZ<6DU54
-KaprGVui+$2Z8EWGGI^Obyc(Bk%kN^J{kdwf%MyBm_v^B_IRsNkIk^ni8kb@QY6c&A?H5494Sg5>8+^ngv|sp7iQE5=5a8HG71d
=eFOkxS+%UGM~<3?n&GYp(axF^9a|F1uh_s>X0%f-61tPA&B%%IH50v3$`C$g>gd$#&&@&9zd4^fdIO!--!JV*NHEkwO`#=98)Oi
Zw$dP@Gq(joa*ZESP;qchy?8oE*9FH@u5m}F!u`-^k-X4g6D0Tj_ZiNrr$=E2co}sNAMe4wh(|7HY-*Jnu2uo>2)4Fo9pOvmKBJN
9>*P#CV2?leI+UCdRS8zt3U0D7G*F8R)>a^B)$M1i0yY=DEg201>bjg3uY!xmzyxPRlQzjM4ny)kcxRU$FaXD@>l&$Vn8@w$sa8@
m$rXnF^uYWmP*(jjS!Sh6Gq)Nq>d$llY+#3?Y{{<7`*5p>_DT0_rVO!rnFWpsdI#7Kz;x`%rj<-@FFX6(tXVBO^>0ks-aOrJ}H@E
(=Yt<+X0jbgpA8QjB&zp3{xFInV>3&fB{_vylE0&U%>q>e#Qm?{r;i10{VToAPtUHKAXBXC)zS}`9B=Dpt1fpBzH%yja}-F=J(0(
sLw=Gck%`(Wl4ddOlDUkCvd`yP(U!gj{t((%{iVmKDr@ll7MRUXhOp@anfa{@$1o{Q$&7$QQw-ho8SSwUY?UV2|BEiaQ9y{`Vi*V
O*phB7y71?l5$THNa29!nyMjR+&vZj&QEwe3}rRn0A1@sPH9eEd8oUVu>2Q|?>;nMAoSb;rgL4e7OV?agJSwCeS5v>x<C+!3xlWN
ukm|MKy4Rv$gnaazV!Dk>YN*&_W7;jSdn`~nE}IaeM&&>K_kn<X25*V90kn+0W%r_bK+=tPB`Zpi1L;)-0WozeTGrG!Q=nT(eRe!
6`cSH5b!=b3|WM3Be%eS9p8Nx91SDH5x7D$tn>5>4*Mn~z*vR2iBIoAp?AImeZTqO4Dm;sglafNZSZ4uw@qyJo18%M;D%&CNxcsN
)x!m-=7Hv6c)RBU&+r3AYL3zfyLFGRr3o3xdWeGsoYzr;K*21C6Zd(eZE?$Qmb%y1le-1B)HUuN7!c5cJ_FVC@)~X+y(FYj*Fh~c
XBNKzS2w_6p&H@D7Zmjr#X!&P@f&28P(Hd<LL>kVjc5^B_X0qj3DEZCbbo$BBzMcw^3azc4{=i8kW>>vYFhi^S>duFVpPxJrl@9O
5UuO`HddPh|GufJu0^lr0sBEWrau9yABF;6-ESQz8gYGU>%Fx&;OD376X3sjyBAjs`Y;Xo=M4@xWPRoDVfvk%AJ)3OTPujAPag}=
>8ZEwN^Yf<(WooY!$%!x^eql`Q78P!pbm{$3KZ)D0J0MOwGn`}BKDh#zUV(>@zdkp{LOpL0aGJggKmyadwj)lSEHNL%RHT^PC3XC
GPep5-~}1NR0~r*0%n2X3W2~+47Ga<uV{5w-~F22bnZvg!7*JmfbY>0Ta4C#IZd|U(*eXE){8s6D7@=G6Lp1q4uSzQ!&<I_y;gRR
=KvOC(B~?8|M)eS3UFMA*WSCAksudWHu`$t5&;2^mFVmHg3{h%^s9FZH-KFMWD-P%J8!CTb1}DsNUQwrxzkS5nH_f2K^8wfVGq@<
XrbFWw)@%rtz~0(bdrWn!qz&v8Mc0hZ$NZY6EXX9uGoO+UbJIxB3v)^o+Am^mWL5N11b~s;rQ;Vp`{NP2s}3p!Ze+KonWe<_skad
JyZ_7KrK+XnQ#jmJ(!8Z#q>Zffx$NrD)o-Vy@P`ti+e`{IDf69@iqI#;M=2PcJG+Njv46qe)=RB>-W)@b!t?g@M}vN4<f&H>2B#S
ouB!;Eq?*NXz8iOt$XVoMe9)(Vf%L`B_WRhMc?7hUttmtm=|Bs(w#&{cNuxzRopjAI2yQJaU%e+>9Cj%i|Md{Ln=w}EYZR?!tJqx
DZpxAh|6Oz^JVwr6)Dd+0qDLeBl~CVocP9Icvk<`pZvyPwmhDS8+ptsG%2wljr{>cem}yM#<Ba(&+WTd&srW+fOEmM0$$r^xYa4d
&yqh33cKysryCS@Te#PxU~jfMU1QQ3W7otjeS4_>X)23HVE#Y+>H0ztf9X;l@%QFtHLkL2{d2m8p7{P1F$1XoE2K)#frfE_StM@+
=_;#lCGaE#!oHDW0dANvFf3FWPyp};?dxtpH1dX4VFC=l94Co9DgQDU|L@CFV7b6eNEj>W%dewvE2!UAAl+6VX)CyWvF$DXtfgC&
>4L0pjm_4?Jr1lvgM`f_y`hc)Bw>0@JRR$e|DaX6w?ZhLtmiEB`s+i}+>dVpgmLNd26yLPUtRC7ZWvkCz%>$ou2f&E-uvPqc+~09
JQIA5xb8i(wdtO9YrQk+@ooT&kO`h#Q4DF+zD=ln{-)j1_hUL8<on$=8)Il<+I|VZ234prhAN>DfKQFFR%{aN8mqs<0YTO8a1waD
!AW4q;~R}*ow)=JNB`a`VW5rIzb82cYaV;X62DQ#fMWz)gvS9nfxbemLHVHdIq`q=PC&lM1Mj4@Zr6~i*9HkfXxm#N$Nc6VX6tVN
|MzYQxb3mH6CNc0R3V^taK_(3p85n7@v;3a%i<2Okyb?+VyWM9mJ&859@`vn|L#Zq{HXWe6UQ$E0H7F1$vO1<GjVtHKsjJ)@^woR
$#0l>yeEv$>a(O5chl)3c)o9_!es7kPw1Jg!MA$~b*o~&rc-PRj2|Ysdcppr3daBtpsIckmoQ(c!w{+GD_T2!+t1cs?(H+J{WqfT
Tdz8Afo8KaR(^0-+v*lK&tyU27#0Hz0}+K*wAcX&+-^01+is+m<-mT8_A<fKE0Evre*s4*uJrF2Kf~@86g1nd>t0a`Dzdki(U<OU
j+oI5Vh2F4ko$lB$-Q6!oq)kPz3KvQ|6=AHn0dGR+r+!a#Jk-K-21ek>pAOg2PfS=w!9HQ1_mIYW&jpGnx8D(z6bz7+%s2>UxPxN
K|f!T;v19`L7W2m&*MBo*+>dIL%>8^9NU5Ea15*!3XLSTxO3|YQ^XE;?!YHZ`E=ZH^I+?;@8BT&4o9^iz+gx_6;6V`JC}p9Ll(mG
hlu{o0aqj$ak}k^PYn;m03R?NVbY#-dhH3jj#PVuD4&aius4F)*$Oy{F+-{(aOgXX689M72&6gvSAj_+r=73>=qLAKBamU*O{DE<
gApNljGO~Yrg)5kpEQrrbM$^_pi4N7z7PL_94IlQ5(MVM3{+*1K;7Nn*{Z4f7Q`yY7M^hJ9a?Jgb`J804?rV`uN{Ql>9D*10(;-u
0$KwzWAGONWfE%Db~Cpi!Q1U%JNWyf9TN7V{<`(SG#PGK0PYfm3lgumi2KqIxCnb1gUi6S+94UT)0-f**iLKuf=s1&&_~XnpOCqv
#^i4-?S}fT-~^x?t}^YQc{{|1-CyVW>+aFJdwrejuK>*}7Zew!;Mf;(L*&-!(f{BmbeLc%U)mZl?a%J<2ZxAW=y8&e9@m{7Cpov@
M%;UMudj3cRi{T64=kDJjr!QPI%$e^IU^_61@M>VBd!R@2Q??4)$}N8_-$(fjK|;~xH+LI5-;xVNeBH2Qyf4E4HVc;qfTlL71}uG
X7d*qV05oAyauC__$XRHkqi(cBns_7d!+P7h)aJa^=AO`{XAE_<vsTWe?jB96UA#Y@;X_%UEOJUb^&U1xws#(0;<|m$v+jh<5l~B
DWu()Q<sV+L`?&4&AK==iJ}-B1tenEbnRV56!&ctcT4gdGp0cD$RHgIx);c0v$60@!tc>d|B(u#I5n~)klT7gGVrG<Xrm}-X*t|W
=2?}!JF8#%a(*~jxH32mlx2cIG;fRA5zX78z>nTrfH%E0YChGNA~ZMY>_8v+tYcFVLie<qPu6=Q@DTZrUidZ$dfJo|xZfy%)Yz~A
dLYB&b8-LI&<*|FGj{7Ir9Yy#2BL*;xJ2UbUK<{?>ZA2JbU@{mIYwhg3mCUpWmhzJrGebRwH@ad@jcrC`nzs-prg^qeH>|uyT1lk
2=}M(s@*98<Rdo@Ej8MneiJsM*pfZm4R84gn&6=b{_VUy0i6uP%~bt0ydn_NL81SEa-C<VDxsY<K|Em@{zA#iJM4ys=fDP6w_fda
g;7sZArPkZ=@i4?{(uC-PfQC!;0?I9EJ)wsT@p|le%poH$%037Ltpx4*S$}dKgH?CwE)fMQ}1rAA1?eO4Dr74=L-f+0D(TM9ngFy
3)C^NoX`l<(rQ)a*vH|Cr2UqOKA)ya3<3LZdiH~uJ2f9bh#$Ap8V2qV{sIma%tmf_jS%c~dD)NFE`)@cFKv`|Ag(1)(7F*ubFzRb
S|>#JNT&$mq&0rxms?)-L<#*jgF*<`2ljz~T*5bWU!Vbq{qcr>K<}x)!gbvevYqy$Gz#*X*616T2n|v?s4`(a%^_ct9E^H>L&F&j
gnk2I-atTxM-rNRNa&O`K|vQBrYOCcwrBKa20XlH0(Tesg`}N(;IlH$1B&f$p9j0v`u*J4(Jzf?uAHKtn(+0tw;%4{_u+pZrYnu8
C>+JJx`)E<hxmX=TCViMJfOa>uOO<2;c3j*H}>^?Ka+g8w&lx>04>jX^#a<xmD{GDaM1S5|8O%4Kw`beo<Dfg(kU=pd++Jl{ue}i
J5yj4{q5m;U>S+tD7!Z<;qC&ch<}_02Qe@jMz)_FA=rU`qc1M|nbx`QDy^Nv+-Qjs?z=qosWGhsyY<6d=KiQ1$-KjA2j}|sKMU`!
09v+M`~X2yox}MQm86%z+kAXr?_R}?>Gz*rZw-O=@JtjLm@!c#qsd1<kJ8XU@-;8^B6~vX`6Y=Ga%Uc>DrA-Ti>l}xfDo@&20r1e
k0c1r@$G;x=>23=yW|3zfoW??`vm0O;kEYr`6v|a(*wV|L)fR2dzU#J>VU37AEJ>Dl;BT5_=k@20rijtq#XnF+!7g9=B9_SE)TGH
xD3rgo(}hG55)Q~G!5VzeR^HZ@nC&y@aTQ<_kAsq7-)Y1_q1cDzJ4+~0F(=Gqceo+8uRWJ`;Niw*z<7*0M^BKD}4)7ZdCVvH*Y_L
l-#DmZc}|ea)yVcK5`OG#tK1b`VT49iksp4Y5q`${COVsciWB-|JAtfCr6|p3LH)Hx4j~`A9vq63N!2so*dmy-CmA{S>+G+jts_`
EN<W}insIf9~Y?rPIwiHU^EPjmKQw_x<N18y8~LGu-e5Bh!#Xbg*dUFcqDSWK8UgJCk%hMu@FRoSkQ~U6QJLi(KJTi)YN~53>4q5
zfOkeCr#R}l)e;QZlcVvG6DG@Nf<nmUP;7h`^o+JYLf<yg0ujhF)p=XZ~<TM7j0G&tZ%_zcqDYY4fD9E0mj}o9+V~24ft}u1*sQa
uvpQyBp}G2b{=M|s{QU9@X4R>76O*m4jKsk_X=PhH&t$TI#(pTtfpeqw@vr^b>#2=a%6Fv6|?}5n?Au5VLW3+Xwe5m@6t&4aexv2
xuyUAbfWRMU4G4m;G?v@wY^OAZ;n6yFU}cCSn_2@_Qg(J5$bjiPAia;@2A?&lh<1`)_3`h&z;NHWLZE;_dCX$m4pc7ip4}~0XYnB
og><PZP=wCpc#YeHU{avq8Sr#M!>DYgi0Y0knmw2pC2gd`1t>X5A+u+=-1Loh32>qFem)kJ#7N?*G}eCc1#^qR=)-wmSmV~X|vxi
sbl}+W;!<IH_BW$>StgkcemAW<P82=BBHH?RX_%;yeB-*(5vgPZkxJ-5ijZ<7M8@HwNNWvfA0DIaeo~RcZhp!`N#uYFc0uREcXyb
yrmHx%<X!}9eQm55q^(v9SjadwXGj*iT9|fovLUnAeNd<6K{?ggL?HmOA(e@oaCmUUu6jm=le~J8+v#>Gvw8b0JfgwuMdd)<NI-m
`v!P{S6Bm2D*{eSL-Y0VG7+c&evX3^1pHouu8kkG$2Go7a{My#7gS4-5!?oW=&tF{N4k*6)vAf|7*IKGW)kJXFrj_#VC)Nw+k<+h
HHPTN$yy&g))TGP$D0}%Zodhds&%UE7RcNDUSPICKm6eocfgH#y*P-?h(GAZLY^S}{S=Qkfce}W_}eLdFNXVlIBdj2m=DK8z}aa>
F4HL|un5dRw7q4WC$0zqTOxkLZ%P;NJ>-7#uL0jT-1;JjFWiN}|C~O|2|j$7c7^1ASolXZ1uO*&g@H-0rQbr7ZUr6?Grk}--`a&>
J+y3JPgCKbw*%z*9ZdQo*voy7e`z7QFf|)}=4#Jxj_Bl}@73|oZfL<zOMA<yz!JlMvoqZP)6U>l^`9*5M&(<sto1<3UQ$erz(+=@
=i7HB*D7D_G6M26EqFSn+lZEU|79rppi@Ucyy@#*f=}DgHE#^t#~%)OvZyJc<Kt#Pnwx-4nkv5jv?>9g-@L+|f`_r)=7uu(z_jrn
t$ZfY)UE3S(@2CB)JG-LZWdDS?Ko)vg8^z^6JclYD^8G+w`60Cjo+<9CZ2{7hTC*6_atPv%`L+^@L?DL;_Ku0L*b9_*TZ!;yeRPf
KBoRZ#^9Lyw=u7$wLfPFU;+Kg?hX6jApHQZ|4*X4t@9>7faNKVcC!PdF>bv6#&Ne+?o=}4M7cc9W)kgA6Fhg)h4vqv-%I_ZkXv}g
^yaZReZR^?eB7P!hhB^V#eq|6aN*zm+8-U;Ut=kZ{=~mg+c3yPUcX58l32(r$&6KaBU3v#{FhGePCCH*_3;7;Me!I7@pb>LbNsj7
@qfEVz?_?dq-jDU@GXLdU!BhFn!kSOn*P4mk8h5Ira#|3+uyt;cHaSb@l`ba;-}EJ+5Vktx^EIZW&QW?u73;Zf6Mvx7MQkgttBb<
?`C20dpV^+=+*P@soo6}NK>>XDF3Bqu8%~Acu%BWHeX?G^O{v@uz%C_e;*eAEUceNB=%co^?vX8PnjBE#63-Wi${<_*uTiwv?GEa
LPr4SF_>a$DLKt@l1gYnX3Fs_q2>2_I#2w_?tjWwuMN=mj9;5XA+!(l)j4WR;#lU7LGDJ!(@_?x=}bKX{#4uJM+PxYRMX>Bxz@^n
k6NW(tHSP7K9eflquXCxCh%39GS@?uW^KBmeYr3g9Xyy9WNA;wspTm0Z)*KNm+_l#d#atzLa1+lVk!WD%m<?TJ7?kc-ChE!$1*P>
yt#ei#qDdG1%I^cJ3YGFlW)NcSOHM6JMKrE)HZ?kH`l0NqI|{qb2G?|YSGi<@n9aGKL7(GR25Lr{jUn)uc7nX@%5Kb!#!C3g9<--
AM`^`e;DyM;RDK7q`*z#Zp;a;;Zw5?O(xnm0{&(P{|{!PaTCHo!Zf~JUTx=2&y8dE*QdF_|7}9H12Tx4j9@YWQjAP9Q%z-FlZ{M2
RqnLl(;qAaDARZhXCIG&LXF387k51Vc-BMDU)eXVM201l1E^-@89d>>Z`$8l&?v42k`I#SKeX&b8}OQ)Jj;K>?YliXgf8xn&s#|b
*Y}vmt=;H)g?=WYAD^#D={uC}p+7#~Qm0p}@8G(-`1riLjUNQ^dT#YxK=^&;Hy?9X%+J>n^9Rgd{m}2J9vt~X6$sTb$pM3J9Tb&a
W%eA<h7SB+Kkz*Epb&e>*RflzYjpjB|LY8W2JPjaCpg?@(`Nbgfg1h~4Qu7S
"""
b = ''.join(PAYLOAD.split()).encode('ascii')
assert len(b) == 17460
assert hashlib.sha256(b).hexdigest() == '97d3113791dca88f81074daa573320a287d9cb763a8a5bf8130493699b8e244c'
s = zlib.decompress(base64.b85decode(b))
assert len(s) == 25495
assert hashlib.sha256(s).hexdigest() == '16a4cf17e523e69b4535cf5c53362976a11be8ed0b9ee4ab7f0b4a878155b864'
Path('c30_reflection_affine.py').write_bytes(s)
print('C30_SOURCE_RECOVERY_PASS', len(s), hashlib.sha256(s).hexdigest())
```

The recovery script itself, with LF and final LF as printed, has **18,175 bytes**, SHA-256 `c5738036eed3478d7d288a30e9521568c36b261f219669c708608e0f077d9c34`. I executed it and byte-compared its recovered source successfully.

Reconstruction and verification commands:

```sh
python -S recover_c30.py
mkdir audit
cd audit
python -S ../c30_reflection_affine.py diagonal
python -S ../c30_reflection_affine.py regression
for p in 0 1 2 3 4 5; do
  python -S ../c30_reflection_affine.py affine "$p"
done
for p in 0 1 2 3 4 5 diagonal; do
  python -S ../c30_reflection_affine.py verify "$p"
done
python -S ../c30_reflection_affine.py finish
```

Alternatively, from an empty output directory, `python -S /path/to/c30_reflection_affine.py all` executes the complete sequence. The separate verifier calls must not be replaced by running `finish` alone.

Observed verification markers include:

```text
C30_SOURCE_RECOVERY_PASS 25495 16a4cf17e523e69b4535cf5c53362976a11be8ed0b9ee4ab7f0b4a878155b864
DIAGONAL_194_REALIZATIONS_57_TYPES_1764_BOXES_PASS
TRUE_P_Q_REFLECTION_VOLUME_ALL_FEATURE_AUDITS_PASS
AFFINE_PART 0 SHEAR_BOXES 645 METRIC_BOXES 9869 PASS
AFFINE_PART 1 SHEAR_BOXES 272 METRIC_BOXES 4412 PASS
AFFINE_PART 2 SHEAR_BOXES 686 METRIC_BOXES 9388 PASS
AFFINE_PART 3 SHEAR_BOXES 347 METRIC_BOXES 5237 PASS
AFFINE_PART 4 SHEAR_BOXES 64 METRIC_BOXES 1651 PASS
AFFINE_PART 5 SHEAR_BOXES 319 METRIC_BOXES 5119 PASS
INDEPENDENT_PARTITION_AND_CLOSED_COMPONENT_CHECK 0 PASS
INDEPENDENT_PARTITION_AND_CLOSED_COMPONENT_CHECK 1 PASS
INDEPENDENT_PARTITION_AND_CLOSED_COMPONENT_CHECK 2 PASS
INDEPENDENT_PARTITION_AND_CLOSED_COMPONENT_CHECK 3 PASS
INDEPENDENT_PARTITION_AND_CLOSED_COMPONENT_CHECK 4 PASS
INDEPENDENT_PARTITION_AND_CLOSED_COMPONENT_CHECK 5 PASS
INDEPENDENT_PARTITION_AND_CLOSED_COMPONENT_CHECK diagonal PASS
C30_FULL_AFFINE_ALL_REFERENCE_REFLECTION_EXCLUSION_PASS
```

Additional executed exact nonzero-mass check, after `regression`:

```python
import json
from fractions import Fraction as F
r = json.load(open('c30_affine_fixture.json'))
assert F(r['Q_centroid'][0]) > 0
assert F(-527,1000) < F(r['P_centroid'][0]) < F(-526,1000)
print('ACTUAL_MASS_NONZERO_BOTH_SIDES_PASS')
```

Observed: `ACTUAL_MASS_NONZERO_BOTH_SIDES_PASS`.

The represented-type pattern count can be independently replayed from the same recovered input records, from the `audit` directory:

```python
import sys
from collections import Counter
sys.path.insert(0,'..')
import c30_reflection_affine as c
patterns = {}
for fs,D,free in c.INPUTS:
    faces = [list(map(int,f)) for f in fs.split()]
    patterns[c.canonical(faces)] = tuple(sorted(map(len,faces),reverse=True))
counts = Counter(patterns.values())
assert counts == {(6,3,3,3,3,3,3,3,3):3,
                  (5,4,3,3,3,3,3,3,3):22,
                  (4,4,4,3,3,3,3,3,3):32}
print('EXACT_REPRESENTATIVE_TYPE_PATTERNS_3_22_32_PASS')
```

Observed: `EXACT_REPRESENTATIVE_TYPE_PATTERNS_3_22_32_PASS`.

Expected output identities, with compact sorted-key JSON and final LF:

```text
c30_affine_fixture.json 151788 da2060b6d57aebf7863f8683573464defb543fb095743ba61dcce4bbc1560ea6
c30_affine_part_0.json 243463 f94d105fa829a1956f5845dbf219ca22f2274df9a8c80597c004c969c239cfd7
c30_affine_part_1.json 108092 65adfadb215ae72e77bd49a9140e53537b0c77a6cb9995923490d06f57012b54
c30_affine_part_2.json 239021 47d99a2f8c6e56687f5837f2debff14144fbb4e9957ecaab898a40ce1aa3cb12
c30_affine_part_3.json 132798 d064baaf3f43fd197e7e0da73c3c31c90a8b64ea54e7b0165b1046c1b94ed63c
c30_affine_part_4.json 41247 01a73437ebe53f76311b02e17cfead279253ef59260a86de9f18da91092825bd
c30_affine_part_5.json 124788 2cc3a28ef8d0853bbbe9a022ca13df7d5367a56956a155a603247f320ced286e
c30_diagonal_certificate.json 48704 a36bb9127b478fd8798e68e8fb772996724e3ae34c5a28a74a82659b9031f68e
c30_verified_0.json 130 4d8c9ce45230da217ad2909ff71cc2b04d4a41f903241ec3832fd4039e192b7c
c30_verified_1.json 130 59f42b684005a38b986c30ccacd2a099f2aeed867b200d38b5dc381bd7be08e8
c30_verified_2.json 130 ab2a0c30eb0324db3a2108259f2234fa0a680c763474261bacc736298e845dbc
c30_verified_3.json 130 c8d5af413d4ac7061076a1a3ea843738a7bedceba8a567678d8ca0aa4c9511b8
c30_verified_4.json 129 b6905a4772efcdcb5d374ed89af73139283127be18c7892f1a3c4d5e9725425d
c30_verified_5.json 130 26c76ca022df86b979956906c12230fab2619b4e7a0ef8f79de1f099a77034bb
c30_verified_diagonal.json 137 1102a4994a42d44f4459eb166c49c858c70b9dd1d455ab2795a77bc72200db44
c30_manifest.json 1743 c29740130777ab76386283d1017e3c5afca11129dbb4134b2370e8d3e1614513
```

Convenience copies supplement, rather than define, the inline recovery: complete main source (`c30_reflection_affine.py`) and certificate bundle (`c30_reflection_certificate.zip`). The bundle is 160,528 bytes, SHA-256 `12cc1ba6b897677b9fd7f027840ff6b4fa6c092e1da74f1ac8f297241093eb46`.

**Final scope:** a complete all-reference/all-physical-metric exclusion of one exact affine family, plus 194 exact diagonal-family exclusions and an explicit nine-variable non-affine frontier. No homogeneous C30 attainer, no reflection-compatible 110 control and no universal 74-type exclusion is claimed.
