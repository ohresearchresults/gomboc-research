# figure-0045

AI research report · 2026-08-23 UTC

---

# Exact yes/no outcome for the affine-corridor asymmetric-cap route

## Canonical gate status

**PRIOR GATE STATUS (verbatim):**

> No verified winner survived the final independent verifier in this run, so the result is the exact reconstructed shell plus the sharply isolated finite cap inequalities, not a claim of a homogeneous body.

**FINAL GATE STATUS (verbatim):**

> **NO VERIFIED HOMOGENEOUS POLYHEDRAL GÖMBÖC WAS PRODUCED BY THE ASYMMETRIC-CAP ROUTE.** The exact moment-closed connected skew-cap branch has `(S,U,H)=(3,2,3)`, while the complete one-, two-, and three-cap noninteracting one-face visibility families are exactly moment-infeasible on the whole corridor square. The next one-sided rail capable even of removing the new cap maximum requires at least 17 intermediate rail vertices; its global centroid-and-mechanics closure remains outside the certified result.

This is a definitive **no** for the verifier-selected branch and for the previously derived one-/two-/three-cap affine visibility polytopes. It is not a nonexistence theorem for arbitrary connected multi-face patches or long rails.

The saved independent verifier outputs state, verbatim:

> INDEPENDENT VERIFIER GATE: FAIL — the exact moment-closed skew one-apex body has (S,U,H)=(3,2,3), not (1,1,0).

> INDEPENDENT VERIFIER GATE: FAIL — no one-, two-, or three-cap closure exists in the certified noninteracting one-face cap family on the entire corridor square.

The source transcript records that the earlier search had not supplied the requested exact body and explicitly rejected treating a near-candidate as a solution.

## 1. Recovered corridor, unchanged

At reference centroid `C`, translated to the origin, the exact family is

\[
P(u,v)=\operatorname{conv}\left(P_0\cup
\{b_k+u d_k+v e_k:1\le k\le53\}\right),
\qquad (u,v)\in[-1,1]^2.
\]

All coordinates are rational. The canonical coefficient table is
`affine_corridor_certificate.json`, SHA-256

`7a6f51c52a16bef208df2883e0e63a43bb95a9ce5bc9c9f68c0112fddee30716`.

The independent checker reconstructs, over the **entire** square,

\[
(V,E,F)=(55,159,106),\qquad (S,U,H)=(1,1,0).
\]

All 106 maximal faces are triangles. The unique stable face is published face 6,
with input vertices `(3,58,43)`, and the unique unstable vertex is input vertex 1.
The minimum full-box nonincidence lower bound is approximately
`2102.007652637433` in the unnormalised exact predicates.

Writing

\[
V(u,v)=\frac16\sum_f\det(a_f,b_f,c_f),
\qquad
Q(u,v)=\frac1{24}\sum_f\det(a_f,b_f,c_f)(a_f+b_f+c_f),
\]

one has `deg V<=3`, `deg Q_i<=4`, with every coefficient stored exactly.
Poincaré–Miranda gives an `x,z` zero in

\[
-3\cdot10^{-6}\le u\le-10^{-6},
\qquad
-10^{-6}\le v\le10^{-6},
\]

but throughout the whole mechanics-preserving square

\[
-1.5594686249511022\times10^{14}
<Q_y(u,v)<
-1.5591631056985403\times10^{14}<0.
\]

Thus every successful third controller must supply at least

\[
1.5591631056985403\times10^{14}
\]

of positive `y` first moment.

## 2. Exact connected skew-cap solution of all three moment equations

The first new branch deliberately leaves the independent-cap architecture. Add one
apex `p` that sees the connected old-face patch

\[
\mathcal F=\{1,3,4,5,6\}.
\]

For each visible face `f=(a,b,c)`, put

\[
n_f=(b-a)\times(c-a),\qquad h_f=n_f\cdot a,
\qquad s_f=a+b+c,
\qquad \delta_f=n_f\cdot p-h_f.
\]

The exact cap contribution is

\[
24Q_{\rm cap}=\sum_{f\in\mathcal F}\delta_f(s_f+p).
\]

Set

\[
N=\sum_f n_f,
\quad H=\sum_f h_f,
\quad A=\sum_f s_fn_f^{\mathsf T},
\quad b=\sum_f h_fs_f,
\quad c=b-24Q_0,
\quad \lambda=N\cdot p-H.
\]

Then all three centroid equations reduce exactly to

\[
(A+\lambda I)p=c
\]

and the scalar quartic

\[
\boxed{
(\lambda+H)\det(A+\lambda I)
-N^{\mathsf T}\operatorname{adj}(A+\lambda I)c=0.}
\]

The primitive integer quartic coefficient list is included in
`single_apex_certificate.json`; its canonical coefficient-list SHA-256 is

`1dc17b6b77a3626dad283630b1670cd8389d01c514852f14784564ca704aef6a`.

The chosen real root is uniquely isolated by

\[
\frac{7024023454492050055211639377756688}
     {15893102429450936605809}
<\lambda<
\frac{45737640828322566395177746386352593}
     {103489547732231375149972}.
\]

Numerically,

\[
\lambda\approx 441954205333.509005218752748409,
\]

and

\[
p\approx
(1486.4951373218556,
 8033.5722773441961,
 -192.54441896064678).
\]

Each coordinate is the published rational function of `lambda`; the rational
isolating boxes have widths below `4.8e-53`. Sturm root counting proves exactly one
quartic root in the interval. Exact support signs prove that `p` violates precisely
faces `1,3,4,5,6` and no others. The quartic identity then proves

\[
Q_{\rm new}=0,
\qquad c_{\rm uniform}=(0,0,0)
\]

**exactly**, not numerically.

### Global hull and own-centroid audit

The rebuilt global hull has

\[
(V,E,F)=(55,159,106),
\qquad \operatorname{Vol}\approx1.707841984147974\times10^{11}.
\]

Its full input-index face list and true edge list are in the certificate. Every
listed triangle strictly supports all nonincident input points; the minimum exact
nonincidence lower bound has decimal value

\[
2263.9355363094187.
\]

At its **own exact uniform-volume centroid**, the complete audit is

\[
\boxed{(S,U,H)=(3,2,3)}.
\]

The stable face cycles are

- published new face 1: `(28,81,1)`;
- published new face 18: `(38,1,81)`;
- published new face 56: `(58,43,81)`.

The unstable vertices are input vertices `1` and `81` (the new apex). The saddle
edges are

\[
(1,81),\qquad(43,81),\qquad(58,81).
\]

Representative exact sign separations are:

\[
\begin{aligned}
&\min(\text{stable-edge predicate})
  >1.50719\times10^{28},\\
&\max(\text{nonstable witness})
  <-5.74354\times10^{19},\\
&\max(\text{unstable comparison})
  <-4.63037\times10^7,\\
&\min(\text{nonunstable ascent witness})
  >859.93866,\\
&\max(\text{saddle support comparison})
  <-1.58218\times10^{21}.
\end{aligned}
\]

Therefore the failure is open and strict. It is not a root-isolation, rounding,
centroid, topology, or tolerance error. The exact connected one-apex moment solution
is **not** a homogeneous polyhedral Gömböc.

## 3. Exact infeasibility of the one-, two-, and three-cap visibility polytopes

Now return to the cap family derived in the previous result: each apex is outside
exactly one old triangular face and lies under every other old supporting plane.
Caps are noninteracting, so their tetrahedral moments add.

For face `f`, define its one-face visibility polyhedron

\[
W_f=\{p:n_g\cdot p\le h_g\quad(g\ne f)\}.
\]

Let

\[
D_f=\max_{p\in W_f}(n_f\cdot p-h_f),
\qquad
Y_f=\max_{p\in W_f}p_y.
\]

For every outward cap on `f`,

\[
(Q_{\rm cap})_y
=\frac{(n_f\cdot p-h_f)(s_{f,y}+p_y)}{24}
\le
\frac{\max(0,D_f)\max(0,s_{f,y}+Y_f)}{24}.
\]

Both maxima are linear programmes. The certificate divides `[-1,1]^2` into
sixteen rational boxes. On every box it supplies:

1. an exact primal active triple;
2. an exact positive dual solution;
3. a Neumann enclosure with
   `||A_0^{-1} Delta A||_infinity<1`;
4. a strict lower bound for every unused face-plane slack;
5. exact upper bounds for `D_f`, `Y_f`, and the resulting `y` moment.

Only seven faces can contribute positive `y` moment anywhere in the square:

\[
\{3,4,5,6,8,9,10\}.
\]

The independent verifier checks all sixteen boxes and obtains the following
**uniform** upper bounds:

| cap count | maximum possible positive `Q_y` |
|---:|---:|
| 1 | `1.3851562196909827e12` |
| 2 | `2.0650493487569440e12` |
| 3 | `2.0824172632258520e12` |
| all seven positive faces | `2.1072741330885710e12` |

The weakest exact LP certificates still have

- minimum dual multiplier lower bound `7.877481161856032e-10 > 0`;
- minimum unused-plane slack lower bound `3.1831697554802266e6 > 0`;
- maximum Neumann radius `0.004826551764796759 < 1`.

The three-cap reachable `y` moment falls short by a certified factor greater than

\[
74.8727,
\]

and even using every positive one-face cap falls short by a factor greater than

\[
73.9895.
\]

Hence

\[
\boxed{
\text{no one-, two-, or three-cap affine visibility solution exists}
}
\]

anywhere in the full corridor square. In fact, no noninteracting collection of
any number of these one-face caps can close the centroid.

This is an exact reachability theorem, not a failed optimizer run.

## 4. The next smallest controller is necessarily a long one-sided rail

The connected moment-closing apex is an extra unstable vertex. A natural cure is a
strict ascent rail from that apex `p` to the retained unstable vertex `v_1`.
For a chain

\[
x_0=p,x_1,\ldots,x_m=v_1
\]

with

\[
x_i\cdot(x_{i+1}-x_i)>0,
\]

write `r_i=||x_i||` and let `theta_i` be the angle between successive rays. Then

\[
r_{i+1}\cos\theta_i>r_i.
\]

Multiplying and using the concavity of `log cos` gives the necessary inequality

\[
\frac{r_m}{r_0}\cos(\Theta/m)^m>1,
\]

where `Theta` is the endpoint angle.

For the exact algebraic apex and retained unstable vertex,

\[
\frac{r_0}{r_m}\approx0.9159318480726938,
\qquad
\Theta\approx99.18677940808026^\circ.
\]

Exact rational Chebyshev brackets prove

\[
\cos(\Theta/17)^{17}<0.9154908980018333
<\frac{r_0}{r_m},
\]

whereas

\[
\cos(\Theta/18)^{18}>0.9200070334615847
>\frac{r_0}{r_m}.
\]

Therefore a strict ascent rail needs at least

\[
\boxed{18\text{ edges and }17\text{ intermediate rail vertices}.}
\]

This is a necessary lower bound. It explains why a one-sided displacement or one
additional rail point cannot repair the cap apex. It does not assert that an
18-edge rail automatically preserves convexity, closes the three moments, or removes
all stable/saddle pairs. That connected long-rail family is the next controller not
excluded by the present theorem.

## 5. Independent verifier-selected outcome

Run

```bash
./run_all.sh
```

The independent outputs are:

- corridor: `(V,E,F,S,U,H)=(55,159,106,1,1,0)` on the full parameter square;
- exact skew cap: `(V,E,F,S,U,H)=(55,159,106,3,2,3)` at its exact own centroid;
- full-box cap capacity: one-, two-, three-, and all-cap infeasibility all `true`;
- rail lower bound: minimum 18 ascent edges / 17 intermediate vertices.

No floating-point number is used as an acceptance premise. Floating values in this
report are previews of exact rational or isolated algebraic quantities.

## 6. Scope

### Proved

- Complete recovery and independent audit of the exact 55-vertex corridor.
- An exact algebraic connected skew-cap solution of all three centroid equations.
- Complete global hull reconstruction and own-centroid feature audit of that body.
- Exact mechanical failure `(3,2,3)` of the connected one-apex branch.
- Exact full-square infeasibility of the previous one-, two-, and three-cap affine
  visibility polytopes; indeed of every noninteracting one-face-cap collection.
- Exact directed lower bound of 17 intermediate vertices for the next one-sided
  ascent rail.

### Not proved

- No homogeneous polyhedral Gömböc is produced.
- Interacting two-/three-apex connected patches are not globally excluded.
- The necessary 18-edge rail has not been made simultaneously convex,
  moment-closing, and mechanically inactive.
- Nothing here is a nonexistence theorem for homogeneous polyhedral Gömböcs.
