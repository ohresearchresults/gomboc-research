# minimum-0003

Historical AI scientific report · saved 2026-09-07 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Clear Atlas 13 — seven-point full-reflection obstruction

## Result and scope

**The seven-point obstruction closes.** I obtain the following elementary theorem, with no restriction to planar chains, prescribed coordinates, simplicial polyhedra, or a selected graph family:

> Let \(X\subset\mathbb R^3\setminus\{0\}\) contain at most seven vectors. Suppose its elements admit a rooted tree with root \(r\), and every nonroot vector \(x\) satisfies \(x\cdot(p(x)-x)>0\). Then
> \[
> -\tfrac13\operatorname{conv}X\not\subseteq\operatorname{conv}X.
> \]

Consequently every nondegenerate homogeneous convex three-polytope with one unstable vertex has **\(V\ge8\)**, and every such polytope with one stable maximal facet has **\(F\ge8\)**. For the user's strict homogeneous Gömböc class,
\[
E=V+F-2\ge14,\qquad \boxed{C=2E\ge28}.
\]
Combining this with the lead's already executed upper-witness replay gives **\(28\le C_{\min}\le1374\)**. I did not rerun that upper-witness audit in this assignment. Its replay and exact identity are recorded in the attached journal. :contentReference[oaicite:0]{index=0}

The full-reflection relaxation is **sharp in point count**: below I give an exact, full-dimensional eight-vertex polyhedron with a strict positive-escape tree and even \(-qQ\subset\operatorname{int}Q\) for \(q=1/3\). Its origin is neither its ordinary volume centroid nor its Santaló point. A separate exact seven-vertex fixture satisfies the lead's weaker factor \(q=5/16\), so simply extending the six-point theorem at that unchanged factor would be false.

The proof below is independent of the inherited, unlocated V7 certificate collection. Its conceptual parent is the lead's literal six-point proof, not the older V>=8 summary. :contentReference[oaicite:1]{index=1}

## 1. Projection estimates and a tighter near-antipode lemma

Write \(h_X(w)=\max_{x\in X}w\cdot x\). Along a positive-escape path from a root of norm \(R\), let consecutive directional angles be \(\alpha_1,\ldots,\alpha_k\). The escape inequality gives
\[
|x_k|<R\prod_{j=1}^k\cos\alpha_j,\qquad 0\le\alpha_j<\pi/2.
\tag{1}
\]
For a positive projection onto a unit vector \(w\), append the angle \(\beta=\angle(x_k,w)<\pi/2\). Angular triangle inequalities give
\(\sum\alpha_j+\beta\ge\angle(r,w)\).
Padding with zero angles and using concavity of \(\log\cos\) proves, for depth at most \(m-1\),
\[
w\cdot x_k\le R\cos^m\!\left(\frac{\angle(r,w)}m\right).
\tag{2}
\]
Nonpositive projections need no estimate. In particular, every node at depth at most three has projection at most \(R/4\) onto \(-r/R\). The two-step radius-angle consequence used repeatedly below is
\[
\frac{|y|}{|x|}\le\cos^2\!\frac{\angle(x,y)}2
\quad\text{for a two-edge descending path }x\to\cdot\to y.
\tag{3}
\]
The actual positive-escape hypotheses make (3) strict, but the weaker form suffices wherever it is used as an upper bound.

### A bottleneck version of the near-antipode argument

Suppose a tree has height four and all depth-four paths pass through one common nonroot vertex \(z\). Put \(e=r/R\), write
\(z/|z|=\cos\theta\,e+\sin\theta\,u\), and choose
\[
\phi=\frac\pi{56},\qquad w=-\cos\phi\,e-\sin\phi\,u.
\]
For collinear \(z,r\), choose any unit \(u\perp e\).

Every node of depth at most three is bounded by
\[
R A_4,\qquad A_4=\cos^4\frac{\pi-\phi}{4}.
\]
Consider a depth-four node, whose path contains \(z\) at depth \(k\ge1\). If \(\theta\ge\phi\), the prefix angles sum to at least \(\theta\), while the suffix angles plus the final projection angle sum to at least
\(\angle(z,w)=\pi+\phi-\theta\). Applying log-cos concavity to all five factors bounds its projection by
\[
R B_5,\qquad B_5=\cos^5\frac{\pi+\phi}{5}.
\]
If \(\theta<\phi\), then \(\angle(z,w)=\pi-\phi+\theta\ge\pi-\phi\). The suffix and projection use at most four factors, and \(|z|\le R\), so the \(RA_4\) bound applies instead. This proves the claim for arbitrary spatial paths; no coplanarity of the path is assumed.

The exact scalar checks in the recovery program establish
\[
A_4<\frac{1331}{4000},\qquad B_5<\frac{1331}{4000},\qquad
\cos\phi>\frac{624}{625},\qquad \tan\phi<\frac2{33}.
\tag{4}
\]
These checks use Machin's identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\), alternating arctangent sums, and the alternating cosine bounds \(1-x^2/2\le\cos x\le1-x^2/2+x^4/24-x^6/720+x^8/40320\) on the argument intervals used here. They give \(314159/100000<\pi<3927/1250\). Machin's identity itself follows by rational tangent addition and the angle range \(0<4\arctan(1/5)-\arctan(1/239)<\pi/2\). No floating-point trigonometric evaluation is a premise.

Thus such a tree has a unit separator within angle \(\phi\) of the negative root satisfying
\[
h_X(w)<\frac{1331}{4000}R
<\frac{208}{625}R
< w\cdot(-r/3).
\tag{5}
\]
The middle gap is exactly \(R/20000\). Height at most three is covered by \(w=-e\), since \(1/4<1331/4000\).

**Counting observation.** In a tree with at most eight nodes and height four, all depth-four paths share the same first child of the root: two disjoint root branches reaching depth four would require at least nine nodes. Hence (5) applies to every height-at-most-four tree with at most eight nodes. This replaces the earlier leaf-by-leaf averaging argument by a bottleneck argument that also covers branching below the bottleneck.

## 2. Every non-chain tree on at most seven nodes is excluded

Assume henceforth \(-K/3\subseteq K\), where \(K=\operatorname{conv}X\). Normalize the root to norm one.

Height at most four is already impossible by (5).

If the height is five and the root has only one child \(a\), removing the root leaves at most six nodes of height four. Reflection of the original root implies \(|a|\ge1/3\), since every other node has norm at most \(|a|\). The first escape inequality gives
\[
\cos\angle(r,a)>|a|\ge1/3>\sin\phi.
\]
The separator (5) for the subtree rooted at \(a\) therefore has strictly negative projection on the deleted root as well. It separates \(-a/3\) from all of \(K\), a contradiction.

The only remaining height-five tree is exactly a **broom**: a five-edge chain
\(r,a,x_2,x_3,x_4,x_5\), together with one additional leaf \(b\) attached directly to \(r\). Indeed, the chain already uses six nodes. Put
\[
t=|a|,\quad \alpha=\angle(r,a),\quad
T=\{a,x_2,x_3,x_4,x_5\},\quad
\mathcal B=B(r/2,1/2).
\]
Both \(r\) and \(b\) lie in \(\mathcal B\), and \(t<\cos\alpha\).

### First, the broom must have \(t<2/3\)

Use the near-antipode separator for \(T\). If \(t\ge2/3\), then its projection on the ball is bounded by
\[
h_{\mathcal B}(w)\le
\frac{1-t\cos\phi+\sqrt{1-t^2}\sin\phi}{2}
<\frac{83}{400}.
\]
Here \(\cos\phi>99/100\), \(\sin\phi<1/10\), and
\(\sqrt{1-t^2}\le\sqrt5/3<3/4\).
But
\[
w\cdot(-a/3)\ge \tfrac13t\cos\phi>\frac{11}{50}>\frac{83}{400},
\]
while (5) excludes every point of \(T\). This contradicts \(-a/3\in K\).

### Reflection of the root now excludes the broom

If \(\alpha\le\pi/5\), take \(w=-a/t\). The tail support is at most
\(t\cos^5(\pi/5)\), which is strictly less than \(\cos\alpha/3\), because
\(t<2/3\) and \(\cos^4(\pi/5)<1/2\). The ball support is
\((1-\cos\alpha)/2<\cos\alpha/3\), since \(\cos\alpha>3/5\).
Thus this direction excludes \(-r/3\).

For \(\alpha>\pi/5\), put
\(\psi=(\pi-\alpha)/4\), and tilt \(-r\) by \(\psi\) away from \(a\). The angle between \(a\) and this direction is exactly \(5\psi\). This equality uses \(\alpha>\pi/5\); the preceding case is essential to avoid an antipodal angle-wrap error. The tail support is at most \(t\cos^5\psi\), while the ball support is
\((1-\cos\psi)/2<\cos\psi/3\). Therefore \(-r/3\in K\) would require
\[
\frac13\le t\cos^4\psi
\le f_1(t):=\frac t4\left(1+\sqrt{\frac{1-t}{2}}\right)^2.
\]
The last bound follows from \(\alpha<\arccos t\). The function \(f_1\) is increasing for \(0<t\le2/3\), and
\[
f_1(2/3)=\frac7{36}+\frac1{3\sqrt6}<\frac13.
\tag{6}
\]
For completeness, with \(z=\sqrt{(1-t)/2}\), its derivative has the sign of
\(2z+4z^2-1>0\), since \(z\ge1/\sqrt6>1/3\). Inequality (6) is equivalent to \(12^2<25\cdot6\).

This excludes every height-five tree. The only case still possible is a seven-node Hamiltonian chain.

## 3. The seven-node chain is impossible

Let the chain be \(x_0,x_1,\ldots,x_6\), with \(|x_0|=1\) and \(x_i\) escaping to \(x_{i-1}\). Define
\[
r=x_0,\quad b=x_2,\quad s=|b|,\quad c=x_4,\quad t=|c|,\quad u=t/s.
\]
We derive incompatible necessary inequalities from the reflections of **only \(x_0\) and \(x_2\)**.

### 3.1. The second-node norm satisfies \(1/3<s<5/11\)

Every node of depth at most three has negative-root projection at most \(1/4\). Therefore \(-r/3\in K\) forces some node of index at least four to have norm at least \(1/3\); hence
\(t\ge1/3\) and \(s>1/3\).

Apply (5) to the five-node tail \(\{x_2,\ldots,x_6\}\). The node \(x_1\) has negative projection on its separator, because
\[
\cos\angle(x_1,b)>\frac{s}{|x_1|}\ge s>1/3>\sin\phi.
\]
Thus the original root must supply the support needed to contain \(-b/3\).
Let \(\alpha=\angle(r,b)\). Equation (3) gives
\(\alpha\le2\arccos\sqrt s\). Since \(s>1/3\), this angle plus \(\phi\) is less than \(\pi\), and any separator in the stated cap satisfies
\[
w\cdot r\le(1-2s)\cos\phi+2\sqrt{s(1-s)}\sin\phi.
\]
Consequently
\[
\frac{s}{3}\le1-2s+2\tan\phi\sqrt{s(1-s)},
\]
so
\[
\frac73s\le1+\tan\phi<1+\frac2{33}=\frac{35}{33}.
\]
Hence
\[
\boxed{s<5/11.}
\tag{7}
\]

### 3.2. Only the endpoint can supply the negative-\(b\) support

First show that the original root cannot satisfy
\(-r\cdot b\ge s^2/3\). If it did, then
\(\cos\alpha\le-s/3\), while (3) gives \(\cos\alpha>2s-1\). Thus
\(s<3/7\) and \(\alpha>\pi/2\).

The prefix \(\{x_0,x_1\}\) lies in \(B(r/2,1/2)\). Put
\(\psi=(\pi-\alpha)/4\), tilt \(-r\) by \(\psi\) away from \(b\), and apply (2) to the four-edge tail rooted at \(b\). Its support is at most \(s\cos^5\psi\), and the prefix-ball support is less than \(\cos\psi/3\). Reflection of \(r\) would therefore require
\[
\frac13\le s\cos^4\psi
\le f_2(s):=\frac s4(1+\sqrt{1-s})^2.
\]
The function \(f_2\) is increasing for \(s\le3/7\), but
\[
f_2(3/7)=\frac{33}{196}+\frac3{7\sqrt7}<\frac13.
\tag{8}
\]
Its derivative has the sign of \(\sqrt{1-s}+1-2s>0\), and (8) is equivalent to \(252^2<97^2\cdot7\). This is a contradiction.

The node \(x_1\) has positive dot product with \(b\). The nodes \(x_2,\ldots,x_5\), being at depth at most three from \(b\), have negative-\(b\) projection at most \(s/4\). Therefore \(-b/3\in K\) forces
\[
-b\cdot x_6\ge s^2/3.
\tag{9}
\]
In particular, \(\angle(b,x_6)>\pi/2\). Four applications of the escape inequality and (7) imply
\[
|x_6|<s\cos^4(\pi/8)
<\frac5{11}\frac{3+2\sqrt2}{8}<\frac13.
\tag{10}
\]
The last comparison is equivalent to \(30^2\cdot2<43^2\).

By (10), \(x_6\) cannot supply the negative-root support either. The nodes \(x_0,\ldots,x_3\) cannot supply it by their depth bound. Therefore **one of \(x_4,x_5\) must have negative-root projection at least \(1/3\)**.

### 3.3. The two-step split gives the final contradiction

Since \(t\ge1/3\) and \(s<5/11\),
\[
u=t/s>11/15.
\]
The angle \(\gamma=\angle(b,c)\) is at most \(2\arccos\sqrt u\). Applying (2) to the two-edge tail from \(c\) to \(x_6\), using (9), yields
\[
\frac13\le B(u):=u\cos^3\!\left(\frac{\pi-2\arccos\sqrt u}{3}\right).
\tag{11}
\]
The function \(B\) is decreasing for \(u>\cos^2(\pi/5)\). To see this, put \(v=\arccos\sqrt u\); the derivative of \(\log B\) with respect to \(v\) is
\[
-2\tan v+2\tan((\pi-2v)/3)>0\quad(0\le v<\pi/5),
\]
whereas \(v\) decreases with \(u\). Our range \(u>11/15\) is within that interval.

An exact scalar comparison gives
\[
B(39/50)<1/3,\qquad\text{hence}\qquad u<39/50.
\tag{12}
\]
One algebraic certificate for the comparison avoids inverse trigonometric evaluation. If
\(z=\cos((\pi-2\arccos\sqrt{39/50})/3)\), then
\(4z^3-3z=1-2(39/50)\) and \(z>1/2\). The cubic is increasing there. Direct rational substitution gives
\[
4(751/1000)^3-3(751/1000)>1-2(39/50),\qquad
(39/50)(751/1000)^3<1/3.
\]

Now put \(a=\arccos\sqrt s\) and \(v=\arccos\sqrt u\). The angle from \(r\) to \(c\) is at most \(2(a+v)\). Also \(a+v<\pi/2\), since
\(s+u\ge2\sqrt{su}=2\sqrt t\ge2/\sqrt3>1\).
The one-edge tail \(\{x_4,x_5\}\) therefore has negative-root support at most
\[
A(s,u):=su\left(\sqrt{s(1-u)}+\sqrt{u(1-s)}\right)^2.
\tag{13}
\]
But that tail must supply projection at least \(1/3\), as established after (10).

On the rectangle
\(1/3\le s\le5/11\), \(11/15\le u\le39/50\), the function \(A\) increases in both arguments. For the first argument, use
\[
\sqrt A=\sqrt u\left[s\sqrt{1-u}+\sqrt{s(1-s)}\sqrt u\right]
\]
and \(s<1/2\). For the second, use
\(\sqrt A=\sqrt s\cos v\sin(a+v)\); its derivative with respect to \(v\) is \(\sqrt s\cos(a+2v)<0\). The latter sign follows from
\(s<1/2<4u(1-u)\) throughout this rectangle. Since \(v\) decreases with \(u\), the claimed monotonicity follows.

Finally,
\[
A(s,u)\le A(5/11,39/50)
=\frac{11271}{60500}+\frac{117\sqrt{1430}}{30250}
<\frac13.
\tag{14}
\]
The last comparison is exactly
\[
702^2\cdot1430<26687^2,
\quad 26687^2-702^2\cdot1430=7486249>0.
\]
Equations (13)–(14) contradict the required support. This closes the Hamiltonian chain and completes the seven-point theorem.

## 4. Homogeneous-centroid and polar consequences

For a uniformly filled convex three-polytope \(P\) with ordinary volume centroid zero, \(-P/3\subseteq P\). A direct proof is to fix any \(z\in P\) and cone an outward boundary triangulation from \(z\). The nonnegative-volume tetrahedra partition \(P\), and their centroids are \((z+a+b+c)/4\). Their volume-weighted mean being zero implies that \(-z/3\) is a convex combination of the boundary-triangle centroids \((a+b+c)/3\), which lie in \(P\).

For a nondegenerate U1 polytope, each other vertex has a strictly positive outgoing directional derivative toward a neighboring vertex. Otherwise its radial normal would give an unstable or degenerate equilibrium. Choosing one such neighbor at each nonroot yields a rooted tree, since the norm strictly increases along every escape. The seven-point theorem gives \(V\ge8\).

For a nondegenerate S1 polytope write
\(P=\{x:q_f\cdot x\le1\}\), using its actual maximal facets and its own centroid as the origin. A nonstable facet's perpendicular foot \(q_f/|q_f|^2\) lies strictly outside \(P\), so some other pole satisfies
\[
q_f\cdot(q_j-q_f)>0.
\]
The actual vertices of \(Q=P^\circ\) therefore have a positive-escape tree rooted at the unique stable pole. Crucially, polarity transfers the inclusion:
\[
-P/3\subseteq P\quad\Longrightarrow\quad Q\subseteq-3Q
\quad\Longleftrightarrow\quad -Q/3\subseteq Q.
\]
It does **not** transfer the ordinary volume-centroid equation. Applying the seven-point theorem to these \(F\) poles gives \(F\ge8\). No ordinary-centroid assumption about \(Q\) has been made. Nonsimple vertices and nonsimplicial facets are covered because neither the tree theorem nor these reductions require triangular faces or degree-three vertices.

## 5. Exact boundary fixtures: seven at 5/16, eight at 1/3

All displayed points are the integer triples below divided by \(D=100000\). The complete verifier following this section rebuilds their hulls by exhaustive supporting triples, checks every reflected vertex against every maximal facet, integrates both bodies and their polars exactly, and audits all faces, vertices and true edges at both the reference origin and the respective ordinary centroids.

### Seven-point fixture: the old factor 5/16 does not extend

```text
100000 0 0
37472 48366 0
4866 51328 1996
-19492 39135 -215
-31513 19401 -1743
-31482 0 0
19358 -39486 0
```

The parent vector is `[-1,0,1,2,3,4,0]`. The body has \((V,E,F)=(7,15,10)\), minimum escape \(487971/5000000000>0\), and exact maximum reflection factor
\[
q_{\max}=15741/50000=0.31482>5/16.
\]
Thus \(-(5/16)Q\subset\operatorname{int}Q\). Its minimum dimensionless reflection slack is \(116/15741\). At the origin it has strict census \((S,U,H)=(2,1,1)\); at its own volume centroid it has \((2,7,7)\). Its reference asymmetry is \(50000/15741\), between 3 and 16/5. This is an exact counterexample to retaining the six-point theorem's factor 5/16 at seven, **not** a counterexample to the new factor-1/3 theorem.

### Eight-point fixture: full centroid-reflection becomes feasible

```text
100000 0 0
49679 49949 0
15628 58859 1996
-13608 51027 1071
-32219 32539 111
-38247 10608 -638
-33400 -8417 506
24414 -42908 -1356
```

The parent vector is `[-1,0,1,2,3,4,5,0]`. The body has \((V,E,F)=(8,18,12)\), minimum escape \(1177511/10000000000>0\), and
\[
q_{\max}=\frac{1398245775349}{3933878900000}>\frac13.
\]
Its minimum dimensionless reflection slack at \(q=1/3\) is
\(260858426047/4194737326047>0\). Thus every reflected vertex is strictly interior. The exhaustive reference census is \((2,1,1)\), with unstable vertex 0; the own-centroid census is \((2,8,8)\). The polar has reference census \((1,2,1)\) and own-centroid census \((6,2,6)\), all nondegenerate.

The eight-point body's exact ordinary centroid is
\[
g(Q)=\frac{(3387442937270005109,\ 2913666043264121915,\ 31766685389095077)}{19239697548410800000}\ne0.
\]
The exact polar integration also gives \(18<g(Q^\circ)_z<19\), so the origin is not the Santaló point of \(Q\). Indeed,
\[
\nabla_z\operatorname{Vol}((Q-z)^\circ)\big|_{z=0}
=4\int_{Q^\circ}x\,dx=4\operatorname{Vol}(Q^\circ)g(Q^\circ).
\]
This follows directly by differentiating
\(\tfrac13\int_{S^2}(h_Q(v)-z\cdot v)^{-3}\,d\sigma(v)\).
The nonzero derivative excludes a Santaló minimum at zero. Thus reference asymmetry, ordinary centering, and Santaló centering are explicitly separated by exact data.

These fixtures establish the precise limitation of the method: **eight is the minimum number of vectors for a full-dimensional positive-escape set satisfying the factor-1/3 reflection condition**, but no eight-vertex homogeneous mono-unstable solid, eight-facet homogeneous monostable solid, or minimal Gömböc is constructed here.

## 6. Recovery capsule and observed verification

Identity: `ATLAS13_SEVEN_POINT_REFLECTION_AND_BOUNDARY_FIXTURES_V1`.

Conceptual parent: the lead's 2026-09-07 05:17:19 and 05:21:20 journal entries. The supplied `research-journal(3).md` is 1762897 bytes, SHA-256 `1c791e9817a707242443a9eb0884cc1be0353c79fee5a48fb769c8c737ae1065`. No parent file is needed to execute the recovery below: every exact fixture input and every helper is included. The historical V>=8 summary is not an input or premise.

Save the following source verbatim, with LF line endings and its final LF, as `seven_point_reflection.py`. It is **9195 bytes**, SHA-256 **`caf6ef8e9926f12e4e3954e1cd1ee5e7cc2ae5c8fc5a04dd7f6a10eb5008173c`**. The executed environment was **Python 3.13.5, standard library only**. Run:

```sh
python -S seven_point_reflection.py
```

Assertions must remain enabled. The observed terminal output was:

```text
SEVEN_POINT_REFLECTION_CONSTANTS_PASS
SEVEN_Q5_16_FULL_EXACT_PASS
EIGHT_Q1_3_FULL_EXACT_PASS
REPORT_BYTES 9120
REPORT_SHA256 60f4f57f7b8fbd3180b2d49c4e5a7ed60f100562b39dbc66abdd64effddbb806
SEVEN_POINT_REFLECTION_RECOVERY_PASS
```

The deterministic `seven_point_reflection_report.json` is **9120 bytes**, SHA-256 **`60f4f57f7b8fbd3180b2d49c4e5a7ed60f100562b39dbc66abdd64effddbb806`**. It contains complete facet lists, exact volumes and primal/polar centroids, reflection factors, escape margins, and all four feature censuses for each fixture. Direct exact reintegration after centroid subtraction returns literally zero first moments for each primal and polar.

The program certifies scalar inequalities and the two exact fixtures. The universal impossibility result is established by Sections 1–4, not by any unsuccessful search or finite sample.

```python
"""Exact constants and full-dimensional boundary fixtures.
Python 3.13.5 standard library; run with assertions enabled.
The universal seven-point proof is in the accompanying handoff, not inferred
from the fixture checks or from a numerical search.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from functools import reduce
import hashlib
import json
from pathlib import Path

assert __debug__
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def sub(a, b): return tuple(x-y for x, y in zip(a, b))
def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a, b, c): return dot(a, cross(b, c))
def atan_sum(x, n):
    return sum((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n))
def cos_upper(x):
    return 1-x*x/2+x**4/24-x**6/720+x**8/40320

# Machin's identity and alternating-series enclosures for pi.
piL = 16*atan_sum(F(1, 5), 6)-4*atan_sum(F(1, 239), 3)
piU = 16*atan_sum(F(1, 5), 5)-4*atan_sum(F(1, 239), 2)
pL, pU = F(314159, 100000), F(3927, 1250)
assert pL < piL < piU < pU
A = cos_upper(55*pL/224)**4
B = cos_upper(57*pL/280)**5
c = pU/56
assert A < F(1331, 4000) and B < F(1331, 4000)
assert 1-c*c/2 > F(624, 625)
assert F(208, 625)-F(1331, 4000) == F(1, 20000)
assert c < F(3, 50) and 1-c*c/2 > F(99, 100)
assert F(3, 50)/F(99, 100) == F(2, 33)
# Broom bounds, root-reflection bound, final chain bounds.
assert F(5,9) < F(9,16)             # sqrt(5)/3 < 3/4
assert F(83, 400) < F(11, 50)
assert cos_upper(pL/5)**4 < F(1,2)
assert 1-(pU/5)**2/2 > F(3,5)
assert 12**2 < 25*6                   # f1(2/3) < 1/3
assert 252**2 < 97**2*7               # f2(3/7) < 1/3
assert 30**2*2 < 43**2                # (5/11)cos(pi/8)^4 < 1/3
U, z = F(39, 50), F(751, 1000)
assert 4*z**3-3*z > 1-2*U and z > F(1, 2)
assert U*z**3 < F(1, 3)               # B(U) < 1/3
assert cos_upper(pL/5)**2 < F(11,15)
assert F(5,11) < F(1,2) < 4*U*(1-U)
assert 702**2*1430 < 26687**2         # A(5/11,39/50) < 1/3
print('SEVEN_POINT_REFLECTION_CONSTANTS_PASS')

D = 100000
FIXTURES = {
    'seven_q5_16': (
        [(100000,0,0),(37472,48366,0),(4866,51328,1996),
         (-19492,39135,-215),(-31513,19401,-1743),(-31482,0,0),
         (19358,-39486,0)],
        [-1,0,1,2,3,4,0], F(5,16)),
    'eight_q1_3': (
        [(100000,0,0),(49679,49949,0),(15628,58859,1996),
         (-13608,51027,1071),(-32219,32539,111),(-38247,10608,-638),
         (-33400,-8417,506),(24414,-42908,-1356)],
        [-1,0,1,2,3,4,5,0], F(1,3))}

def simplicial_hull(I):
    faces, planes = [], []
    for a, b, c in combinations(range(len(I)), 3):
        n = cross(sub(I[b], I[a]), sub(I[c], I[a]))
        if n == (0, 0, 0): continue
        h = dot(n, I[a])
        slack = [h-dot(n, x) for x in I]
        if max(slack) <= 0:
            b, c = c, b
            n, h = tuple(-t for t in n), -h
            slack = [-t for t in slack]
        if min(slack) < 0: continue
        assert sum(t == 0 for t in slack) == 3
        assert h > 0
        g = reduce(gcd, (abs(t) for t in (*n, h)))
        planes.append((tuple(t//g for t in n), h//g))
        faces.append((a, b, c))
    assert set(v for f in faces for v in f) == set(range(len(I)))
    edges = edge_map(faces)
    assert len(I)-len(edges)+len(faces) == 2
    return faces, planes, edges

def edge_map(faces):
    edges = {}
    for f, cyc in enumerate(faces):
        for a, b in zip(cyc, cyc[1:]+cyc[:1]):
            edges.setdefault(tuple(sorted((a,b))), []).append((f,a,b))
    assert all(len(v) == 2 and v[0][1:] == v[1][1:][::-1]
               for v in edges.values())
    return edges

def mass(X, faces):
    W, M = F(0), [F(0)]*3
    for cyc in faces:
        a = X[cyc[0]]
        for i in range(1, len(cyc)-1):
            b, c = X[cyc[i]], X[cyc[i+1]]
            d = det(a, b, c)
            assert d > 0
            W += d
            for j in range(3): M[j] += d*(a[j]+b[j]+c[j])
    assert W > 0
    return W/6, tuple(t/(4*W) for t in M)

def polar(I, faces, planes, edges):
    Y = [tuple(F(D*t,h) for t in n) for n,h in planes]
    cycles = []
    for i, x in enumerate(I):
        inc = {f for f, cyc in enumerate(faces) if i in cyc}
        adj = {f: [] for f in inc}
        for (a,b), ee in edges.items():
            if i not in (a,b): continue
            f,g = ee[0][0], ee[1][0]
            adj[f].append(g); adj[g].append(f)
        assert all(len(v) == 2 for v in adj.values())
        start = min(inc); cyc = [start]; prev = None; cur = start
        while True:
            nxt = min(j for j in adj[cur] if j != prev)
            if nxt == start: break
            assert nxt not in cyc
            cyc.append(nxt); prev,cur = cur,nxt
        assert set(cyc) == inc
        a,b,c = (Y[j] for j in cyc[:3])
        orient = det(sub(b,a),sub(c,a),x)
        assert orient != 0
        if orient < 0: cyc = [cyc[0]]+list(reversed(cyc[1:]))
        assert all(dot(x,y) <= D for y in Y)
        assert {j for j,y in enumerate(Y) if dot(x,y) == D} == inc
        cycles.append(tuple(cyc))
    edge_map(cycles)
    return Y, cycles

def census(X, faces, center):
    Z = [sub(x,center) for x in X]
    planes = []
    for cyc in faces:
        a,b,c = (Z[j] for j in cyc[:3])
        n = cross(sub(b,a),sub(c,a)); h = dot(n,a)
        assert h > 0
        planes.append((n,h))
    stable, unstable, saddle, degenerate = [],[],[],[]
    for f,(n,h) in enumerate(planes):
        foot = tuple(h*t/dot(n,n) for t in n)
        guards = [k-dot(m,foot) for j,(m,k) in enumerate(planes) if j != f]
        if min(guards) > 0: stable.append(f)
        elif min(guards) == 0: degenerate.append(('F',f))
    for i,a in enumerate(Z):
        guards = [dot(a,sub(a,b)) for j,b in enumerate(Z) if j != i]
        if min(guards) > 0: unstable.append(i)
        elif min(guards) == 0: degenerate.append(('V',i))
    for (i,j), ee in sorted(edge_map(faces).items()):
        a,b = Z[i],Z[j]; e = sub(b,a); L = dot(e,e); T = -dot(a,e)
        z = tuple(L*a[k]+T*e[k] for k in range(3))
        n,m = (planes[v[0]][0] for v in ee)
        nn,mm,nm = dot(n,n),dot(m,m),dot(n,m)
        assert nn*mm-nm*nm > 0
        v1 = tuple(mm*n[k]-nm*m[k] for k in range(3))
        v2 = tuple(nn*m[k]-nm*n[k] for k in range(3))
        guards = [T,L-T,dot(z,v1),dot(z,v2)]
        if min(guards) > 0: saddle.append((i,j))
        elif min(guards) == 0: degenerate.append(('E',i,j))
    assert len(stable)+len(unstable)-len(saddle) == 2 or degenerate
    return {'S':stable, 'U':unstable, 'H':saddle, 'degenerate':degenerate}

def verify(name, I, parents, q):
    X = [tuple(F(t,D) for t in row) for row in I]
    faces,planes,edges = simplicial_hull(I)
    escape = [dot(X[i],sub(X[p],X[i])) for i,p in enumerate(parents) if p >= 0]
    assert min(escape) > 0
    assert all(dot(X[0],sub(x,X[0])) < 0 for x in X[1:])
    refl = [F(h)+q*dot(n,x) for n,h in planes for x in I]
    assert min(refl) > 0
    qmax = min(F(h,-dot(n,x)) for n,h in planes for x in I if dot(n,x) < 0)
    assert qmax > q
    volume,g = mass(X,faces)
    Y,pfaces = polar(I,faces,planes,edges)
    pvolume,pg = mass(Y,pfaces)
    assert any(g) and any(pg)
    assert mass([sub(x,g) for x in X],faces) == (volume,(F(0),)*3)
    assert mass([sub(y,pg) for y in Y],pfaces) == (pvolume,(F(0),)*3)
    origin = (F(0),)*3
    ref = census(X,faces,origin)
    own = census(X,faces,g)
    pref = census(Y,pfaces,origin)
    pown = census(Y,pfaces,pg)
    assert ref['U'] == [0] and not ref['degenerate']
    assert not own['degenerate'] and not pref['degenerate'] and not pown['degenerate']
    assert tuple(len(ref[k]) for k in ('S','U','H')) == (2,1,1)
    assert tuple(len(own[k]) for k in ('S','U','H')) == (2,len(X),len(X))
    assert tuple(len(pref[k]) for k in ('S','U','H')) == (1,2,1)
    assert tuple(len(pown[k]) for k in ('S','U','H')) == (len(X)-2,2,len(X)-2)
    if len(X) == 7:
        assert qmax == F(15741,50000) and 17 < pg[2] < 18
    else:
        assert qmax == F(1398245775349,3933878900000) and 18 < pg[2] < 19
    result = {
        'D':D, 'I':I, 'parents':parents, 'q':str(q),
        'V_E_F':[len(X),len(edges),len(faces)], 'facets':faces,
        'minimum_escape':str(min(escape)), 'minimum_primitive_reflection_guard':str(min(refl)),
        'maximum_reflection_factor':str(qmax), 'reference_asymmetry':str(1/qmax),
        'minimum_dimensionless_reflection_slack':str(1-q/qmax),
        'volume':str(volume), 'ordinary_centroid':list(map(str,g)),
        'polar_volume':str(pvolume), 'polar_ordinary_centroid':list(map(str,pg)),
        'reference_census':ref, 'own_centroid_census':own,
        'polar_reference_census':pref, 'polar_own_centroid_census':pown,
        'scope':'Exact reference-reflection fixture; origin is neither its volume centroid nor its Santalo point.'}
    print(name.upper()+'_FULL_EXACT_PASS')
    return result

report = {name:verify(name,*data) for name,data in FIXTURES.items()}
raw = (json.dumps(report,sort_keys=True,indent=2)+'\n').encode('ascii')
Path('seven_point_reflection_report.json').write_bytes(raw)
print('REPORT_BYTES',len(raw))
print('REPORT_SHA256',hashlib.sha256(raw).hexdigest())
print('SEVEN_POINT_REFLECTION_RECOVERY_PASS')
```

## 7. Evidence limits, primary-source comparison, and continuation

The productive sequence was to generalize the near-antipode lemma to a common internal bottleneck, exclude the entire branched seven-node case, and then split the remaining chain at indices 2 and 4. The decisive extra observation was that the endpoint required to support the reflection of \(x_2\) becomes too short to support the reflection of \(x_0\). This replaces the unresolved two-prefix difficulty by the explicit two-variable inequality (14). Numerical exploration helped locate the boundary fixtures, but no search failure or numerical optimality assertion is a premise of the theorem or of their acceptance; their literal rational definitions and exact verifier suffice to reproduce every claimed property.

The checked primary paper by Bozóki–Domokos–Papp–Regős, arXiv:2401.17906v2, proves the homogeneous lower bound V>=7 using 5943 certified quadratic systems. The proof above independently strengthens that bound in the present strict nondegenerate scope and gives a separate facet-side result. I do not claim historical priority relative to all later work. :contentReference[oaicite:2]{index=2} The older eight-vertex result for uniform point masses concerns a different center and is not used here. :contentReference[oaicite:3]{index=3}

The new analytic proof has a complete case split and its nontrivial constants have passed exact rational checks, but it has not yet received an independent mathematician's review. The two boundary fixtures have been fully checked by the provided exact implementation; this is not a claim of two independent verifier implementations. There is no new homogeneous Gömböc upper witness and no determination of the exact minimum.

**The most useful continuation is now the true E=14 boundary, which necessarily has V=F=8.** A further lower bound must use joint mechanics or actual mass information beyond the one-sided reflection relaxation. On the vertex side the missing equation is the literal quartic moment condition
\[
\sum_{(a,b,c)}\det(a,b,c)(a+b+c)=0
\]
for an outward triangulation of the actual boundary. On the facet-pole side it is the corresponding equation for the actual vertices of \(Q^\circ\), equivalently \(g(Q^\circ)=0\), not \(g(Q)=0\). The eight-point fixture is an exact regression test against silently replacing either condition by \(-Q/3\subseteq Q\). The counting/bottleneck lemma also continues to exclude every eight-node escape tree of height at most four.

Convenience copies: [complete exact source](sandbox:/mnt/data/atlas13/seven_point_reflection.py) and [exact report](sandbox:/mnt/data/atlas13/seven_point_reflection_report.json). The complete inline source and literal input points above, rather than these links, define the recoverable handoff.
