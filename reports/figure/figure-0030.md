# figure-0030

AI research report · 2026-08-22 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Exact eight-cap moment-control theorem for the rational Reshetov cancellation seed

## Verdict

No homogeneous polyhedral Gömböc is obtained in this direction. The completed result is the requested quantitative fallback: an explicit finite rational moment-control family, exact volume/first-moment polynomials, a full-rank three-control Jacobian, a certified open `(S,U,H)=(1,1,0)` parameter box, and an exact proof that the current centroid target is outside the reachable set of the entire eight-control family.

The persistent transcript had already localized the remaining task to full-basin cancellation followed by exact centroid restoration.

## Seed

The parent polyhedron has exact rational data

\[
(V,E,F)=(27,58,33),\qquad (S,U,H)_C=(1,1,0),
\]

relative to the original Reshetov centroid `C`, with minimum normalized sign margin `2.8957131465e-5`. Numerically,

\[
C=(-104.1014775785565,8.465022473324968,-47.56244776570032),
\]

while its own uniform centroid is

\[
c_0=(-2589.6385146523567,10.129056745597389,-50.441025273326).
\]

Write `Q(P)=Vol(P)(c(P)-C)`. Then

\[
Q_0\approx(-3.286331659622633\times10^{12},
2.200155712869\times10^9,-3.806002588931\times10^9).
\]

The parent residual `R=M-4CD` equals `24Q`.

## Explicit controls

Use the unchanged simple seed vertices

\[
I=\{4,5,6,7,8,9,11,12\},
\]

with neighbor triples

```text
4:(2,6,21)   5:(3,7,11)   6:(4,8,22)   7:(5,16,17)
8:(6,9,12)   9:(8,23,24) 11:(5,14,15) 12:(8,25,26).
```

None is the unique unstable vertex and none lies on the unique stable face. For control vertex `v_i`, neighbors `w_{i1},w_{i2},w_{i3}`, and depth `t_i`, replace `v_i` by

\[
p_{ij}=v_i+t_i(w_{ij}-v_i),\qquad j=1,2,3.
\]

This removes the tetrahedron `conv(v_i,p_i1,p_i2,p_i3)`. All exact control coordinates and coefficients are in `remote_caps_certificate.json`.

Put

\[
e_{ij}=w_{ij}-v_i,
\quad A_i=|\det(e_{i1},e_{i2},e_{i3})|/6,
\quad b_i=v_i-C,
\quad s_i=e_{i1}+e_{i2}+e_{i3}.
\]

Then exactly

\[
\boxed{V(t)=V_0-\sum_{i\in I}A_it_i^3}
\]

and

\[
\boxed{Q(t)=Q_0-\sum_{i\in I}A_it_i^3\left(b_i+\frac{t_i}{4}s_i\right)}.
\]

These are separable rational polynomials of degree at most four. The exact constructor independently cross-checks them against the oriented boundary tetrahedral sum.

## Exact controlled body

For all eight depths equal to `2/5`, every cap plane is a strict one-vertex cut: the intended old vertex is outside and every other parent vertex has positive exact slack. The exact volume identity shows the eight maximal tetrahedral caps are interior-disjoint; smaller caps are nested, so `[0,2/5]^8` is a valid simultaneous control domain.

The resulting rational body has

\[
(V,E,F)=(43,82,41),\qquad C_{mech}=164,
\]

and, relative to `C`,

\[
\boxed{(S,U,H)=(1,1,0)}.
\]

The unique stable face is face 25 and the unique unstable vertex is vertex 1. Its exact centroid is stored in the certificate; numerically,

\[
c=(-2588.6111367968138,10.12767880014713,-50.503381604847974),
\]

so it is not homogeneous.

## Certified mechanical box

Take primary controls `{5,8,11}`. Fix the other five depths at `2/5` and allow

\[
\boxed{2499/6250\le t_5,t_8,t_{11}\le2/5}
\]

independently, i.e. `[0.39984,0.4]^3`.

An exact rational interval audit and an independent 160-digit outward-rounded audit certify throughout this whole box:

- fixed topology `(V,E,F)=(43,82,41)`;
- 1599 strict nonincidence convexity inequalities;
- 40 nonstable-face exclusion witnesses and all 3 signs of the unique stable face;
- 42 strict comparisons for the unique unstable vertex and 42 ascent witnesses for all other vertices;
- all 82 edge lengths and all 82 no-saddle certificates: 32 feet beyond the second endpoint, 25 before the first endpoint, and 25 interior feet with a nonsupport witness.

Thus every face, vertex, and edge inequality remains strict, with `(S,U,H)=(1,1,0)` everywhere in the box.

## Full-rank moment control

At `t=2/5`, the exact Jacobian columns for controls `5,8,11` are approximately

\[
J_5=(7.0016007240\!\times\!10^9,-3.5265139398\!\times\!10^8,2.5724902880\!\times\!10^8)^T,
\]

\[
J_8=(2.7495823609\!\times\!10^9,1.9201002949\!\times\!10^8,-2.4140312159\!\times\!10^8)^T,
\]

\[
J_{11}=(1.3263187184\!\times\!10^9,-6.2781951143\!\times\!10^7,5.4086779242\!\times\!10^8)^T.
\]

Their exact rational determinant is nonzero; numerically it is `1.1484561205080022e27`. The condition number is about `32.0046`. Hence the controls span all three first-moment directions locally; the obstruction is magnitude, not rank.

## Exact global no-go for this family

For the x-component, the positive correction from control `i` is

\[
f_i(t)=-A_it^3\left(b_{i,x}+\frac{t}{4}s_{i,x}\right),
\]

and

\[
f_i'(t)=-A_it^2(3b_{i,x}+ts_{i,x}).
\]

For every one of the eight controls, exact rational checks give

\[
3b_{i,x}<0,
\qquad 3b_{i,x}+(2/5)s_{i,x}<0.
\]

Therefore each `f_i` is nondecreasing on `[0,2/5]`; the largest possible positive x correction on the full product domain is attained when every depth is `2/5`. Exactly,

\[
\max\Delta Q_x\approx4.372543409026824\times10^9,
\]

whereas

\[
|Q_{0,x}|\approx3.286331659622633\times10^{12}.
\]

Thus the correction fraction is only

\[
0.0013305240803141943,
\]

and even at the best corner

\[
Q_x\le-3.2819591162136064\times10^{12}<0.
\]

Consequently

\[
\boxed{Q(t)\ne0\text{ for every }t\in[0,2/5]^8.}
\]

The three centroid equations have no solution anywhere in this finite control architecture. The shortfall factor is about `751.5835`.

## Independent verification and artifacts

`independent_check.py` imports no construction code. It reconstructs the parent coefficients, checks every published controlled vertex against its exact parameter formula, rebuilds the 82-edge graph from the face cycles, proves every listed face is a complete strict supporting face, recomputes exact volume and centroid, classifies every face/vertex/edge, rechecks the moment formula, and verifies the no-go and Jacobian determinant.

- Complete self-contained package (`remote_cap_certificate.zip`)
- Full rational coordinate/face/moment certificate (`remote_caps_certificate.json`)
- Exact constructor and verifier (`verify_remote_caps.py`)
- Independent exact checker (`independent_check.py`)
- Exact rational interval report (`remote_caps_interval_report_fraction.json`)
- Outward-rounded interval report (`remote_caps_interval_report.json`)
- OBJ (`remote_caps_baseline.obj`)

Package SHA-256:

```text
d16fae7c7c63955376f8dab9748f9dfb38e84499c958639f60b1d5c96bc5dabe
```

Run `./run_all.sh`; it regenerates the exact certificate and OBJ, repeats both interval audits, runs the independent checker, and validates `SHA256SUMS`.

## Scope

Proved: explicit controls, exact moment maps, exact strict baseline mechanics, a certified open mechanical box, full local moment rank, and exact global nonreachability for `[0,2/5]^8`.

Not proved: no homogeneous polyhedral Gömböc is produced, and the no-go does not apply to larger corridor replacements, outward additions, normal rotations, projective changes, or other control architectures. The correct staged use is to let the enlarged replacement corridor remove most of the residual first; the present full-rank controls can then close the final three equations inside their certified sign neighborhood.
