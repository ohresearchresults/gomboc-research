# figure-0310

Historical AI scientific report · saved 2026-09-05 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Vivid Lynx 76 — finite-layer compression handoff

## 1. Result and acceptance status

**No new homogeneous polyhedral Gömböc was obtained.** The strongest promoted construction in this handoff is an independently replayed, rational, uniform-volume body with

\[
(V,E,F)=(65,146,83),\qquad 2E=292,\qquad(S,U,H)=(3,1,2).
\]

It has 42 triangular maximal faces, 40 quadrilateral maximal faces and one hexagonal maximal face. It is not a `(1,1,0)` successor or a compression record for the successful large Gömböcs. Throughout, 292 is the requested edge-budget quantity `2E`; the script field `C` uses that convention. The equilibrium-subtracted definition `V+E+F-(S+U+H)` would instead give 288 for this nonwinner. :contentReference[oaicite:0]{index=0}

The more consequential result is a **global obstruction to the proposed fixed-polygon discretization**, not a failed parameter sweep:

* A centrally symmetric, reflection-compatible polygonal central section is incompatible with a nondegenerate `C2`-symmetric polyhedral Gömböc, even when the three-dimensional body is not centrally symmetric.
* For the prescribed phase and amplitude `epsilon=1/50`, **every reflection-compatible regular polygon B is blocked**, regardless of the number or placement of horizontal knots, vertical rescaling, or the choice of an even physical x-centre correction, provided the resulting layered body is convex and mechanics use its actual volume centroid.
* An explicit rational pentagon is also blocked. For this pentagon the obstruction holds whenever the first-band shear ratio is below the exact threshold `rho_* = 334932435151317941936/345214080486663242745`, approximately `0.9702166107452778`. The prescribed phase is rigorously below `0.54`, not merely observed to be small. The same proof blocks amplitudes up to `1/28` for this pentagon.

The regular-polygon phase claim uses the piecewise-linear interpolants of the displayed a and c_y samples, symmetric point-end sections, and an arbitrary even c_x profile. It does not cover arbitrary changes to a or c_y. These exclusions do **not** cover all nonregular polygons, layer-dependent polygons, asymmetric architectures, or all bodies with `2E<1000`. In particular, `C2` symmetry itself is not an obstruction: the published symmetry classification allows it. The obstruction below concerns the finite central-section geometry, not the abstract symmetry group. :contentReference[oaicite:1]{index=1}

No immutable worker parent was used or modified. No old small-winner alias is promoted here. The new exact body, the proofs, and all reconstruction data are given below.

## 2. Exact finite geometry and own-volume equations

Let B be a convex planar polygon with area A and area centroid zero. Write its sides as `u_j dot b <= h_j`. Set

\[
K_z=c(z)+a(z)B,\qquad a\geq0,
\]

with a and c piecewise affine on common ordered knots. At a band from z_i to z_{i+1}, define

\[
f_j(z)=h_j a(z)+u_j\cdot c(z),\quad
s_{ij}=\frac{f_j(z_{i+1})-f_j(z_i)}{z_{i+1}-z_i}.
\]

**Global convexity is equivalent to every sequence `s_ij` being nonincreasing.** Checking only the side normals is sufficient: every horizontal direction belongs to the positive cone of two consecutive side normals, and both the polygon support value and the translated/scaled section support value are the corresponding positive linear combinations.

An explicit H-description is supplied by all inequalities

\[
u_j\cdot x-s_{ij}z\leq f_j(z_i)-s_{ij}z_i,
\]

together with the endpoint height bounds when needed. Identical support planes must be merged. This is not permission to retain triangulation diagonals as edges.

For a band of height d, endpoint scales a,b and section centres c_i,c_j, put

\[
v=\frac d3(a^2+ab+b^2),\qquad
w_0=\frac d{12}(3a^2+2ab+b^2),\qquad
w_1=\frac d{12}(a^2+2ab+3b^2).
\]

The band volume is `A v`, and its three-dimensional first moment is

\[
A\{w_0(c_i,z_i)+w_1(c_j,z_j)\}.
\]

Thus all three own-centroid coordinates are computed, not fitted to a reference point. With B invariant under `(x,y)->(x,-y)`, a and c_x even, and c_y odd, the filled body has the half-turn symmetry

\[
R(x,y,z)=(x,-y,-z),
\]

so only the x moment remains. Translating by the computed x centroid preserves this architecture.

## 3. A central-section obstruction independent of density fitting

**Finite-section feature lemma.** Let a full-dimensional convex polyhedron be invariant under R. If both x-extremes of its section at `z=0` are polygon vertices, it cannot have exactly one nondegenerate stable equilibrium. If both x-extremes are relative interiors of polygon sides, it cannot have exactly one unstable equilibrium.

Proof: a unique equilibrium of a specified type must be fixed by R, hence must lie at one of the two boundary points of the x axis. In the first case neither point can lie in the relative interior of a three-dimensional facet: an interior facet point would give a line segment through that point in the central section, unless that facet were horizontal, which is impossible at an interior height. Thus neither axial point can be a nondegenerate stable equilibrium. Stable equilibria must occur in off-axis pairs. In the second case each axial point already lies inside a nontrivial segment of the central section, so neither is a vertex of the three-dimensional body; unstable equilibria occur in off-axis pairs. This proves the assertion.

Consequently, **every centrally symmetric B compatible with the reflection symmetry is excluded**, since its two x-extreme features have the same type. This includes the even regular polygons in either reflection-compatible orientation. This argument does not assume that K is centrally symmetric.

Another unsuccessful escape is omitting the knot at zero. With an even, piecewise-affine a and c_x and an odd, piecewise-affine c_y on one central band, the middle of that band is an affine prism. Its axial points lie in nontrivial segments and are not vertices. A unique unstable equilibrium is again impossible. A special nonhomothetic critical cap could change this conclusion; merely removing the central knot cannot.

## 4. The own-centroid restriction needed for the odd-polygon obstruction

Normalize `a(0)=1`, and suppose the symmetric end sections are points. Let

\[
h_+=\max_{b\in B}b_x,\qquad h_-=-\min_{b\in B}b_x,
\]

and let `c_0=c_x(0)` **after translation to the actual volume centroid**.

### 4.1 Exact centroid interval

For every convex body in this even-section architecture,

\[
\boxed{-h_+/4\leq c_0\leq h_-/4.}
\]

Here is a proof which includes the volume constraint. Convexity makes a concave: a positive multiple of a is any section-width function. On the positive half of the height interval, let `ell(t)` be the length of the superlevel interval `{z:a(z)>=t}`. Concavity of a implies concavity of ell. Therefore `ell(t)/(1-t)` is nondecreasing for `0<t<1`. The elementary monotone-covariance inequality with weight `t(1-t)` gives

\[
\frac{\int a^3\,dz}{\int a^2\,dz}
=\frac32\frac{\int_0^1t^2\ell(t)\,dt}{\int_0^1t\ell(t)\,dt}
\geq\frac34.
\]

Both horizontal support functions are even and concave, hence

\[
c_0-h_-(1-a(z))\leq c_x(z)\leq c_0+h_+(1-a(z)).
\]

Multiply by `a(z)^2`, integrate, and use the **actual** centroid equation `integral a^2 c_x = 0`. The boxed bound follows. No ballast, dual centroid, or arbitrary centre is being substituted.

### 4.2 A general two-vertex certificate

Let the first positive knot have scale `a_1<1`; put

\[
d=1-a_1,\qquad \Delta x=c_x(z_1)-c_0,\qquad r=|c_y(z_1)|/d.
\]

Choose two upper-half vertices b_R,b_L of B. Suppose, uniformly over the centroid interval above:

1. `p_R=c_0 e_x+b_R` has positive x coordinate and `p_L=c_0 e_x+b_L` has negative x coordinate;
2. each p_i satisfies `p_i dot (b_neighbor-b_i)<0` for both adjacent vertices of B;
3. `N_i=|b_i|^2+c_0 b_ix-r|b_iy|>0` for i=R,L.

The largest radial dot product from p_i to its two first-band meridional neighbours is

\[
\Delta x\,(c_0+b_{ix})-dN_i.
\]

If `Delta x<=0`, both meridional dots at p_R are negative. If `Delta x>=0`, both at p_L are negative. Together with the planar inequalities, this produces a strictly unstable central vertex and its distinct half-turn mate.

This is also a **global supporting-plane proof**, not merely a local edge heuristic. The planar inequalities make b_i the unique maximizer of the horizontal functional p_i on B. Thus the support of section K_z in that direction is `a(z) p_i dot b_i + p_i dot c(z)`. It is concave in z, affine on the two first bands, and has strictly descending slopes away from zero on both sides. Its unique global maximum is at the indicated central vertex. The radial supporting plane therefore contacts the entire body at that vertex alone. Coplanar face merging or longer true meridional edges cannot invalidate the conclusion.

### 4.3 An explicit rational polygon with a global no-go certificate

Start with the CCW pentagon

\[
C=\left[(1,0),\left(\frac{57}{185},\frac{176}{185}\right),
\left(-\frac{1431}{1769},\frac{1040}{1769}\right),
\left(-\frac{1431}{1769},-\frac{1040}{1769}\right),
\left(\frac{57}{185},-\frac{176}{185}\right)\right].
\]

Its area centroid is `(beta,0)`, with

\[
\beta=-\frac{20031451}{131975829285}.
\]

Set `B=C-(beta,0)`. The admissible own-centred central translation satisfies

\[
c_0\in\left[-\frac{32998965184}{131975829285},
\frac{26684846816}{131975829285}\right].
\]

Take b_R=B[1] and b_L=B[2], using zero-based indices. Exact endpoint evaluation of the affine-in-c_0 inequalities gives:

| Uniform quantity | Certified bound |
|---|---:|
| `c_0+b_Rx` | `>1/20` |
| `c_0+b_Lx` | `<-3/5` |
| negative of either angular dot at p_R | `>2/5` |
| negative of either angular dot at p_L | `>9/20` |

The two limiting shear ratios for positivity of N_i are

\[
\rho_R=\frac{334932435151317941936}{345214080486663242745},\qquad
\rho_L=\frac{303437888046237404464}{213330557472230098875}.
\]

Thus for

\[
\boxed{r<\rho_*:=\rho_R\approx0.9702166107452778}
\]

**Every convex, homogeneous, own-centred body in this symmetric fixed-B architecture has at least two strict unstable equilibria.** There is no restriction on how many other knots or x-centre controls it has. This is a global exclusion of the stated parameter class.

## 5. A rigorous continuum bound for the prescribed phase

Write the source coordinate as `s` to distinguish it from a possible vertically rescaled physical height:

\[
\eta(s)=\frac{3\pi}{2}(s-s^3/3),\qquad
P(\eta)=\eta-\frac{41}{100}\sin(2\eta)-\frac9{200}\sin(4\eta).
\]

Since P is nondecreasing, P(0)=0 and P(pi)=pi, the sine below is nonnegative on the entire source interval. For `epsilon=1/50`, define

\[
r(s)=\frac{\sin P(\eta(s))}{50(1-\sqrt{1-s^2})},\quad 0<s\leq1.
\]

The replay below proves

\[
\boxed{r(s)<27/50=0.54\quad\text{for every }0<s\leq1.}
\]

The numerical maximum observed during exploration was approximately `0.527185`; that observation is not used in the proof.

The continuum certificate uses

\[
P'(\eta)=(1-\cos2\eta)\left(\frac{59}{50}+\frac9{25}\cos2\eta\right)\geq0.
\]

For `s<=1/10`, the inequalities `P(eta)<=77 eta^3/75` and `pi<22/7` prove the required bound directly. The first follows by bounding `1-cos(2eta)<=2eta^2`, bounding the second factor by `77/50`, and integrating. For `s>=3/10`, `1-sqrt(1-s^2)>=s^2/2` gives `r<=4/9`.

The remaining interval is covered by **400 rational interval inequalities**, not 400 sampled function values. For `n=200,...,599`, set `a=n/2000`, `b=(n+1)/2000`, and

\[
E=\frac{33}{7}(b-b^3/3),\quad
L_{11}(t)=\sum_{j=0}^{5}\frac{(-1)^j t^{2j+1}}{(2j+1)!},
\]
\[
\overline P=E-\frac{41}{100}L_{11}(2E)-\frac9{200}L_{11}(4E),\quad
U_n=\frac{\overline P-\overline P^3/6+\overline P^5/120}{25a^2}.
\]

The alternating-series remainder makes L_11 a lower bound for sine on all arguments used. Monotonicity of P in eta, and monotonicity of `t-t^3/6+t^5/120` on `[0,3/2]`, make U_n an upper bound for **every real s in the corresponding interval**. Exact rational evaluation verifies `0<Pbar<3/2` and `U_n<27/50` for every n. The largest interval upper bound occurs at `n=397` and is approximately `0.535745876731503`.

For amplitude epsilon the bound scales to `r(s)<27 epsilon`. In particular, `epsilon<=1/28` gives `r<27/28<rho_*` for the rational pentagon. A remote even x bump cannot alter this exclusion: its effect on the true centroid is already included in the centroid interval, and Delta x was arbitrary in the proof.

### Regular-polygon corollary

For an odd regular m-gon with its right axial point a vertex, put `delta=pi/m`, `h=cos(delta)`, and `c_0 in [-1/4,h/4]`. For `m>=5`, choose the vertices at angles `2delta` and `pi-delta`. Their own-centred x coordinates have opposite signs. Their angular dots are strictly negative throughout this centroid interval. For example, the two dots at the first vertex are

\[
-2(1-c_0)\sin^2\delta,
\qquad -2\sin^2\delta-2c_0\sin3\delta\sin\delta,
\]

and the two at the left vertex are

\[
-2\sin^2\delta,
\qquad 2\sin^2\delta(2h c_0-1).
\]

Each corresponding N is positive at the prescribed amplitude, since `N>=1-|c_0|-r>0`. The two-vertex certificate applies. It also applies for amplitudes up to `1/28`: then `c_0^2+r^2 < 1/16+(27/28)^2 =389/392<1`, so positivity follows from Cauchy-Schwarz.

For `m=3`, convexity gives `Delta x/d>=-1/2`; at either left vertex the maximal meridional dot is at most

\[
d\frac{\sqrt3}{2}\left(r-\frac{\sqrt3}{2}\right)<0
\]

at amplitude `1/50`. Both left vertices are strictly unstable. Even m was excluded by the finite-section feature lemma. Reflection deals with the opposite odd-polygon orientation.

**Conclusion:** arbitrarily refining the prescribed symmetric fixed-regular-polygon construction cannot solve the task. The obstruction survives exact own-centroid correction and is independent of the complexity budget.

## 6. Strongest promoted finite body: L65-E146

This body uses a deliberately nonregular B and escapes the central angular obstruction, but retains two additional stable equilibria.

### Exact defining data

Let `D=1000000`. Form the upper boundary of a raw planar polygon C from these integer coordinate arrays, divided by D:

```text
X = [1837050,1294218,970076,511759,118107,-222122,
     -489425,-696987,-842204,-948773,-1000000]
Y = [0,598985,956656,1187510,1251964,1214204,
     1118196,990454,863324,738175,668248]
```

Append the y-reflections in reverse order, excluding the first point. There are 21 vertices. Its exact area and centroid are

\[
A=\frac{2592260208481}{500000000000},\qquad
\beta=\frac{417476689055911501}{1944195156360750000},\qquad g_C=(\beta,0).
\]

Set `B=C-(beta,0)`, `h=1+beta`, and

```text
a     = 504224/D
Xend  = -1211133/D
Yhalf = 197472/D
Yend  = 387075/D
H     = 51967/D
Xhalf = h*(a-1)
```

The positive profiles have knots `z=(0,H/2,H)`, scales `(1,a,0)`, x centres `(0,Xhalf,Xend)` and y centres `(0,Yhalf,Yend)`. Reflect with x even and y odd. The exact pretranslation x centroid is

\[
g=\frac{Xhalf(1+2a+6a^2)+a^2Xend}{4(1+a+2a^2)}
=-\frac{289084456180544437160561243088259}{955345832784965746104000000000000}.
\]

The following coordinates, in the following order, define K as their convex hull:

* vertex 0: `(Xend-g,-Yend,-H)`;
* vertices 1 through 21: `(Xhalf-g+a*b_x,-Yhalf+a*b_y,-H/2)`, in B order;
* vertices 22 through 42: `(b_x-g,b_y,0)`, in B order;
* vertices 43 through 63: `(Xhalf-g+a*b_x,Yhalf+a*b_y,H/2)`, in B order;
* vertex 64: `(Xend-g,Yend,H)`.

All coordinates are rational. Density is identically one throughout the filled convex hull.

### Exact mass, convexity, maximal faces and mechanics

The volume is

\[
\operatorname{Vol}(K)=\frac{AH(1+a+2a^2)}3
=\frac{2068602370514013121991107}{11444091796875000000000000}
\approx0.1807572332720085.
\]

The own volume centroid and all three first moments are exactly zero. This was checked both by the layer equations and by an independently reconstructed tetrahedral decomposition with a hull vertex as apex.

The rational base-polygon audit has **399 strict nonincident side-support inequalities**, with minimum `465799/500000000000`. The layer audit has **62 strictly positive slope drops and exactly one zero drop**, the central left-side drop. Its minimum positive unnormalized drop is

\[
\frac{2786777958925921058852941}{526218696305203621093750000}>0.
\]

The zero drop merges exactly two quadrilateral patches into the hexagonal maximal face. Hence

\[
(V,E,F)=(65,146,83),\quad
\{\text{face sizes}\}=\{3:42,\ 4:40,\ 6:1\}.
\]

The complete equilibrium ledger is:

```text
stable maximal faces:
  [11,12,33,54,53,32]          # intended left hexagon
  [43,64,63]                 # upper cap triangle
  [0,2,1]                    # lower cap triangle

unique unstable vertex:
  22

saddle true edges:
  [11,12]
  [53,54]

face/vertex/edge equilibrium degeneracies:
  none
```

No saddle count was inferred from Euler's relation. All 146 true edges were classified. All vertex tests used either every true incident edge or, in the independent replay, every other vertex of the complete hull. Nonsimple vertices and nonsimplicial faces are therefore included.

The first exact checker’s complete feature-sign digest is

```text
3a5698aa714dce85556d225129f9d2fd34fa3602c27dec0fbe63c988569de455
```

### Why this is not a near-winner despite tiny floating face margins

The intended hexagon is at distance

\[
r_S=\frac{871402621746184877848310468911741}{955345832784965746104000000000000}
\approx0.9121331687876056
\]

from the centroid. Each extra stable triangle is at distance approximately `0.031492277755426026`. Exact rational comparisons certify `r_S>9/10` and that the squared distance to either extra stable plane is `<1/625`.

Thus the tiny positive in-face margins produced by numerical optimization were not a small global mechanical gap. The body remains very thin in the transverse direction.

A useful necessary condition for continuation is: if a specified facet is the only stable facet in a nondegenerate body, its centroid distance must be no greater than the distance to **every** supporting facet plane. This follows because the largest centred inscribed ball has radius `min_f h_f/||n_f||`, and its contact point on a minimizing facet is a stable equilibrium unless degenerate. For this C2 body the axial right point cannot be stable, and the intended left stable point is not the global minimum. Therefore an off-axis stable pair is forced. Continuing to reduce the tiny local margins while retaining this large support-distance gap cannot produce a Gömböc.

## 7. Independent replay and what was actually tried

A fresh ZIP extraction passed both standalone commands and both geometric implementations under `python3 -S`; the extracted outputs reproduced the same exact volume, zero centroid, `(65,146,83)` incidence and `(3,1,2)` class. The rational obstruction replay also passed.

Three reconstruction/check paths were completed: a rational raw-patch support/merge checker using local full normal cones; an independent exhaustive all-triples hull reconstruction using global radial supporting-plane tests; and a literal-data standalone replay rebuilding the coordinates from the integer arrays above. The last two examine all `binomial(65,3)=43680` triples. The literal generator was checked to give exactly the same rational vertices as the first certificate, not just close floating coordinates.

The standalone replay below is standard-library Python. It reconstructs **all maximal supporting planes without Qhull**, computes their true polygon boundaries, obtains true edges from those boundaries, recomputes filled-volume moments, and independently counts faces, vertices and edge feet. For edge feet it tests the radial supporting plane against every other vertex; it does not use a two-normal approximation or skip shallow normal cones.

Exploration included fixed regular polygons with several layer counts and amplitudes, free nonregular reflection-symmetric polygons, skew two-apex fans, one-base/one-apex layered families, and symmetry-breaking profile perturbations. These were genuine coordinate-and-mass searches. Infeasible support profiles and floating near-zero classes were not promoted. One early exploratory polygon test based only on consecutive turns was insufficient without simplicity/global support; the accepted certificate uses exhaustive support planes instead. Later restarts imposing the necessary insphere condition did not produce an accepted winner, and some optimizations failed numerically. None of these finite searches is presented as a global infeasibility theorem.

The proofs here are narrower and stronger than those searches: they exclude the specified entire classes. They have not been checked in a formal proof assistant or subjected to independent human review. The rational subclaims and the finite body have executable exact replays.

## 8. Most useful continuation

Do not spend another branch refining the regular fixed-B phase mesh or adding further even x-centroid actuators to it. That route is excluded, not merely underresolved. Also reject centrally symmetric polygonal B under the retained half-turn symmetry before optimization.

For a nonregular fixed B, compute the interval `[-h_+/4,h_-/4]` first and search for the two opposing angular-normal vertices in Section 4. If that rational certificate exists and the first-band shear remains below its threshold, reject the entire profile chart. A successful continuation must destroy at least one of those angular-normal stars, exceed the applicable shear bound while keeping global convexity and own-centroid balance, break the relevant symmetry, or introduce layer-dependent/nonhomothetic critical geometry. In particular, a separately constructed finite unstable cap and stable-face patch changes the obstruction hypotheses in a way that x mass correction does not.

Use the necessary centred-insphere and maximum-radius inequalities alongside local equilibrium predicates from the beginning. The L65-E146 benchmark is useful for testing the exact layered machinery and for demonstrating the misleading-small-margin failure mode; its present thin chamber is not a promising final-death checkpoint.

## Appendix A — complete standalone finite-body replay

Save this block as `replay_handoff.py` and run `python3 -S replay_handoff.py` with Python 3.9 or newer. Do not disable assertions. It has no dependency on the journal, archives, SciPy, a mesh file, or any companion file.

```python
#!/usr/bin/env python3
# Independently discover every supporting plane from every triple.
# GLOBAL radial supporting-plane tests replace local normal-cone coefficients.
from fractions import Fraction as Q
from itertools import combinations
from math import gcd,lcm
from functools import reduce
from collections import defaultdict,Counter
import json

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def normplane(n,h):
 d=reduce(gcd,map(abs,(*n,h)));return tuple(x//d for x in (*n,h))
def cyc(P,ids,n):
 # Exact angular ordering about polygon average: no atan2.
 from functools import cmp_to_key
 drop=max(range(3),key=lambda j:abs(n[j]));axes=[j for j in range(3) if j!=drop];N=len(ids)
 sm=[sum(P[i][j] for i in ids) for j in axes]
 v={i:(N*P[i][axes[0]]-sm[0],N*P[i][axes[1]]-sm[1]) for i in ids}
 def half(i):
  x,y=v[i];return 0 if y>0 or y==0 and x>=0 else 1
 def cmp(i,j):
  if half(i)!=half(j):return -1 if half(i)<half(j) else 1
  x,y=v[i];X,Y=v[j];s=x*Y-y*X
  if s:return -1 if s>0 else 1
  return (dot(v[i],v[i])>dot(v[j],v[j]))-(dot(v[i],v[i])<dot(v[j],v[j]))
 f=sorted(ids,key=cmp_to_key(cmp))
 if dot(cross(sub(P[f[1]],P[f[0]]),sub(P[f[2]],P[f[1]])),n)<0:f.reverse()
 start=f.index(min(f));return f[start:]+f[:start]
def replay(d):
 raw=[[Q(x) for x in p] for p in d['vertices']];D=reduce(lcm,(x.denominator for p in raw for x in p),1)
 P=[tuple(int(x*D) for x in p) for p in raw];planes=set();ntri=0
 for i,j,k in combinations(range(len(P)),3):
  ntri+=1;n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
  if not any(n):continue
  h=dot(n,P[i]);sign=0;ok=True
  for p in P:
   s=dot(n,p)-h
   if s:
    ss=1 if s>0 else -1
    if sign and sign!=ss:ok=False;break
    sign=ss
  if not ok or not sign:continue
  if sign>0:n=tuple(-x for x in n);h=-h
  planes.add(normplane(n,h))
 planes=sorted(planes);faces=[]
 for pl in planes:
  ids=[i for i,p in enumerate(P) if dot(pl[:3],p)==pl[3]]
  f=cyc(P,ids,pl[:3]);assert len(f)>=3
  # No collinear nonvertices in this particular exact certificate.
  assert all(dot(cross(sub(P[f[(j+1)%len(f)]],P[f[j]]),sub(P[f[(j+2)%len(f)]],P[f[(j+1)%len(f)]])),pl[:3])>0 for j in range(len(f)))
  faces.append(f)
 E=defaultdict(list)
 for i,f in enumerate(faces):
  for a,b in zip(f,f[1:]+f[:1]):E[tuple(sorted((a,b)))].append(i)
 assert all(len(v)==2 for v in E.values());assert len(P)-len(E)+len(faces)==2
 # Recompute integral moments using vertex 0 as tetrahedral apex.
 O=P[0];T=0;M=[0,0,0]
 for f in faces:
  if 0 in f:continue
  for j in range(1,len(f)-1):
   a,b,c=[P[u] for u in (f[0],f[j],f[j+1])];vol=det(sub(a,O),sub(b,O),sub(c,O));assert vol>0
   T+=vol
   for v in range(3):M[v]+=vol*(O[v]+a[v]+b[v]+c[v])
 assert T>0;g=[Q(x,4*T) for x in M];L=4*T;W=[tuple(L*p[j]-M[j] for j in range(3)) for p in P]
 U=[];H=[];S=[];deg=[]
 for i,p in enumerate(W):
  vals=[dot(p,sub(q,p)) for j,q in enumerate(W) if i!=j]
  if max(vals)<0:U.append(i)
  elif max(vals)==0:deg.append(['vertex',i])
 for (i,j) in sorted(E):
  a=W[i];e=sub(W[j],a);ee=dot(e,e);ae=dot(a,e)
  if not (0 < -ae < ee):continue
  q=tuple(ee*x-ae*y for x,y in zip(a,e));qq=dot(q,q)
  vals=[ee*dot(q,p)-qq for k,p in enumerate(W) if k not in (i,j)]
  if max(vals)<0:H.append([i,j])
  elif max(vals)==0:deg.append(['edge',i,j])
 for fi,(f,pl) in enumerate(zip(faces,planes)):
  n=pl[:3];ns=dot(n,n);hh=dot(n,W[f[0]])
  # Rational plane foot q=hh*n/ns. Test every in-plane boundary side.
  vals=[]
  for i,j in zip(f,f[1:]+f[:1]):
   dlt=sub(W[j],W[i]);rel=tuple(hh*n[t]-ns*W[i][t] for t in range(3));vals.append(dot(cross(dlt,rel),n))
  if min(vals)>0:S.append(fi)
  elif min(vals)==0:deg.append(['face',fi])
 assert not deg,deg
 vol=Q(T,6*D**3);g=[v/D for v in g]
 assert vol==Q(d['layer_volume']);assert g==[Q(x) for x in d['layer_centroid']]
 return {'status':'INDEPENDENT_ALL_TRIPLES_GLOBAL_SUPPORT_REPLAY_PASS','triples_examined':ntri,'V':len(P),'E':len(E),'F':len(faces),'C':2*len(E),'class':[len(S),len(U),len(H)],'stable_faces':S,'unstable_vertices':U,'saddle_edges':H,'volume':str(vol),'centroid':[str(x) for x in g],'face_sizes':dict(Counter(map(len,faces))),'degeneracies':deg,'maximal_faces':faces,'primitive_support_planes':[list(p) for p in planes]}

def literal_body():
 D=10**6
 X=[1837050,1294218,970076,511759,118107,-222122,-489425,-696987,-842204,-948773,-1000000]
 Y=[0,598985,956656,1187510,1251964,1214204,1118196,990454,863324,738175,668248]
 C=[(Q(x,D),Q(y,D)) for x,y in zip(X,Y)]
 C += [(x,-y) for x,y in C[:0:-1]]
 cross2=lambda p,q:p[0]*q[1]-p[1]*q[0]
 W=C[1:]+C[:1];s=[cross2(p,q) for p,q in zip(C,W)];A=sum(s)/2
 beta=sum(v*(p[0]+q[0]) for v,p,q in zip(s,C,W))/(6*A)
 assert sum(v*(p[1]+q[1]) for v,p,q in zip(s,C,W))==0
 B=[(x-beta,y) for x,y in C];h=1+beta
 a=Q(504224,D);Xend=Q(-1211133,D);Yhalf=Q(197472,D);Yend=Q(387075,D);H=Q(51967,D)
 Xhalf=h*(a-1)
 g=(Xhalf*(1+2*a+6*a*a)+a*a*Xend)/(4*(1+a+2*a*a))
 vol=A*H*(1+a+2*a*a)/3
 P=[(Xend-g,-Yend,-H)]
 P += [(Xhalf-g+a*x,-Yhalf+a*y,-H/2) for x,y in B]
 P += [(x-g,y,Q(0)) for x,y in B]
 P += [(Xhalf-g+a*x,Yhalf+a*y,H/2) for x,y in B]
 P += [(Xend-g,Yend,H)]
 return {'vertices':[[str(x) for x in p] for p in P], 'layer_volume':str(vol),'layer_centroid':['0','0','0']}

if __name__ == '__main__':
 data=literal_body()
 r=replay(data)
 assert (r['V'],r['E'],r['F'],r['C'])==(65,146,83,292)
 assert r['class']==[3,1,2]
 assert r['stable_faces']==[50,68,69]
 assert r['unstable_vertices']==[22]
 assert r['saddle_edges']==[[11,12],[53,54]]
 assert not r['degeneracies']
 P=[[Q(x) for x in row] for row in data['vertices']]
 rs=-P[11][0]
 assert rs>Q(9,10)
 for fi in [68,69]:
  f=r['maximal_faces'][fi];n=cross(sub(P[f[1]],P[f[0]]),sub(P[f[2]],P[f[0]]));hh=dot(n,P[f[0]])
  assert hh*hh/dot(n,n)<Q(1,625)
 print(json.dumps({k:v for k,v in r.items() if k not in ('maximal_faces','primitive_support_planes')},indent=2))
```

## Appendix B — complete rational obstruction subcertificate

The analytic reductions in Sections 4–5 turn the continuum statement into the rational assertions checked here. Save as `no_go_certificate.py` and run it with standard-library Python.

```python
#!/usr/bin/env python3
# Each grid cell bounds an entire real interval, not a sampled value.
from fractions import Fraction as Q
from math import factorial

def polygon_certificate():
 C=[(Q(1),Q(0)),(Q(57,185),Q(176,185)),(Q(-1431,1769),Q(1040,1769)),(Q(-1431,1769),Q(-1040,1769)),(Q(57,185),Q(-176,185))]
 W=C[1:]+C[:1];w=[p[0]*q[1]-p[1]*q[0] for p,q in zip(C,W)];area=sum(w)/2
 beta=sum(t*(p[0]+q[0]) for t,p,q in zip(w,C,W))/(6*area)
 B=[(x-beta,y) for x,y in C];lo=-B[0][0]/4;hi=-B[2][0]/4
 thresholds=[]
 for i in [1,2]:
  x,y=B[i]
  if i==1:assert x+lo>Q(1,20)
  else:assert x+hi < -Q(3,5)
  for j in [(i-1)%5,(i+1)%5]:
   X,Y=B[j];margin=min(-(c+x)*(X-x)-y*(Y-y) for c in [lo,hi])
   assert margin>(Q(2,5) if i==1 else Q(9,20))
  thresholds.append(min(x*x+y*y+c*x for c in [lo,hi])/y)
 rho=min(thresholds)
 assert rho==Q(334932435151317941936,345214080486663242745)
 assert Q(27,28)<rho
 return beta,lo,hi,rho

def phase_certificate():
 # pi < 22/7; eta(s) <= (33/7)(s-s^3/3).
 k=Q(33,7);A=Q(77,75)
 def sin_lower_11(x):return sum((-1)**j*x**(2*j+1)/factorial(2*j+1) for j in range(6))
 def sin_upper_5(x):return x-x**3/6+x**5/120
 # Small s <= 1/10: r <= A*k^3*s/25.
 assert A*k**3/Q(250)<Q(27,50)
 # Large s >= 3/10: r <= 1/(25*s^2) <= 4/9.
 assert Q(4,9)<Q(27,50)
 upper=[]
 for n in range(200,600):
  a=Q(n,2000);b=Q(n+1,2000);eta=k*(b-b**3/3)
  assert 0<eta<Q(3,2) and (4*eta)**2<14*15
  p=eta-Q(41,100)*sin_lower_11(2*eta)-Q(9,200)*sin_lower_11(4*eta)
  assert 0<p<Q(3,2)
  u=sin_upper_5(p)/(25*a*a)
  assert u<Q(27,50),(n,u)
  upper.append((u,n))
 return max(upper)

if __name__=='__main__':
 b,lo,hi,rho=polygon_certificate();u,n=phase_certificate()
 print('EXACT_RATIONAL_CENTRAL_STAR_AND_400_INTERVAL_PHASE_OBSTRUCTION_PASS')
 print('beta =',b,'centroid_shift_interval =',lo,hi)
 print('rho_star =',rho,'approx =',float(rho))
 print('interval_max =',n,'upper =',float(u),'certified global r < 27/50 at epsilon=1/50')
 print('extended amplitude epsilon <= 1/28 gives r < 27/28 < rho_star')
```

## Supplemental files

[Exact replay package](sandbox:/mnt/data/layered_compression_handoff.zip) contains both independent checkers, the literal replay, exact inputs and outputs, fresh-extraction replay logs, the obstruction subcertificate, and this handoff. The final archive is 44,228 bytes with SHA-256 `192687fc0bf61194f767b1e0c73daf1a9199575eb9b0de1b721f2201a3b7fdff`. [Standalone Markdown handoff](sandbox:/mnt/data/layered_compression_result.md). All continuation-critical definitions, claims, and replay algorithms are reproduced above; these links are supplements.
