# minimum-0283

Historical AI scientific report · saved 2026-09-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# C600 cap surgery: a whole-family obstruction and an exact completion-response law

## 1. Status and strongest results

**No new attaining own110physicalweak000 endpoint is claimed. The durable construction checkpoint remains the final C600 own121physicalweak000 body of the literal parent. Canonical C622 is unchanged.**

The principal new result is a quantified obstruction to an entire class of genuine cap and crease surgeries. It is stronger than the parent's protection of two unchanged vertex stars: **the old unstable vertices may be deleted, their incident edges may disappear, and arbitrarily many new true facets and vertices may be introduced.** The conclusion still forces two strict unstable vertices, provided specified old supporting halfspaces and two small radial witnesses are retained. There is no forest, saddle, stable-facet, or fixed-incidence assumption.

Three related results make the obstruction useful for constructive continuation:

1. An exact, nonperturbative identity describes how the actual-centroid completion plane responds to material rejected by added caps. Its normalized support value decreases at the centroid of that rejected material whenever the completion changes.
2. For a genuine small cap at the degree-four unstable vertex, the removed volume is exactly cubic and its first moment is exactly cubic plus quartic in cap depth. The completing plane135 consequently moves first at cubic order. Its initial response at the old unstable vertex has a definite sign, rather than being an uncontrolled centre residual.
3. In the cap regime where the removed tip is independent of plane135, **the parent's exact interval Jacobian can be reused unchanged**. The new centring problem differs only by an explicitly known polynomial first-moment residual. This gives a direct exact-certification method for future cap candidates without pretending that the old centre stayed correct after cutting material away.

The obstruction identifies a concrete distinction for the next search: a sufficiently shallow inward cap, or an inward crease that preserves the old supporting halfspaces, does not defeat the trap merely by changing the true vertex star. A successful modification must either pass the stated retained-point barrier or release at least one of the trapping supporting halfspaces. This is a necessary condition, not a sufficiency claim for cancellation.

## 2. Sources and verification scope

The current journal update was read through EOF, including the entire literal parent payload. Its identity is:

- `research-journal(20260927-182943).md`: 349937 bytes; SHA-256 `0a3f93750556df8935935af31de290033e499cfb18604a45ce5727208fc33e05`.
- Required literal parent: `minimum-0278`; SHA-256 `f20aca01e1f5d111d6d5de2fe39c1ebba8127bafb72c2248dfaaa00d40521022`.
- Its retained recovery wrapper: `recover_c600_complete.py`, 33593 bytes; SHA-256 `59fbb3d09a056dd5cff1ee7847cdced3cf435af9a30eaa2d78b152acd5e225d9`.
- Its complete 20-unit decoded source/input map: 85755 bytes; SHA-256 `36ab4293d22ad4356a0c279609747f2340b2b8f50d73008b7485c214de2f8289`.

The retained earlier exact sources remained accessible. No canonical C622 coordinates were substituted for the protected raw labels. The proof below uses the parent's exact true-edge angle certificate, actual-centroid completion, and bounded released-kernel certificate. It does not assert a new replay of all sixteen parent output pins.

The relevant parent output pins are:

```text
contract600_complete.json
271086 bytes
35419d0277e8c5c2d5e95923e956659dd478d355363a4805562f17569857fd6f

barrier600.json
6952179 bytes
5857077ea48020fa73691cff2490a6b64b2b40f5bdda73625c639168ba6025fa

reachability.json
8247 bytes
74020ffb5022f44c3ee8088827f437f9657335f66a67d65e763d9ad2b536ea67
```

The mathematical results below are proved explicitly. No new algebraic actuator normal is being passed off as certified from a floating residual. Exploratory cap, local-facet, and metric calculations did not yield a newly accepted exact endpoint. Those numerical candidates are not used in the proofs and are not promoted as durable successors.

## 3. Physical coordinates and the exact parent fact used

Translate the parent's actual uniform volume centroid `g0` to zero, without otherwise changing its physical Euclidean coordinates. Write the resulting body as `P0`. Its physical reference metric is `I`.

Let `u` be the degree-four strict unstable vertex and `v` the degree-42 strict unstable vertex of the final C600 body. In the parent's final output indexing they are respectively `150` and `89`. These indices refer only to that exact final output.

The active raw facet labels at `u` are

```text
3, 41, 67, 68.
```

For any vertex `w` of `P0`, let `A(w)` be its actual incident maximal facets and let

`T(w) = {w+d : q_f·d <= 0 for every f in A(w)}`,

where `q_f·x <= 1` is the actual centred support equation. Thus `T(w)` is the whole tangent polyhedron at `w`, not merely a neighbourhood made from integration triangles.

The parent's exact certificate proves, for all 46 directed true edges leaving `u` or `v`,

`w·e < 0`,

`441 (w·e)^2 > ||w||^2 ||e||^2`.

Here `e` is the actual outgoing edge vector. Equivalently,

`w·e < -(1/21)||w||||e||`.

The new arguments need precisely this certified datum and the actual tangent cones. They do not need the old escape forests.

### Extension from edges to the entire tangent cone

Every nonzero direction `d` of the tangent cone is a nonnegative combination of its true edge rays. Therefore

`w·d < -(1/21)||w||||d||`                                               (3.1)

for every nonzero tangent direction `d`.

Indeed, write `d = sum_i lambda_i e_i`, with `lambda_i >= 0`. The certified edge inequalities give

`w·d < -(1/21)||w|| sum_i lambda_i ||e_i|| <= -(1/21)||w||||d||`.

This is the important change in scope. **Preserving the old incident supporting inequalities preserves (3.1), even when none of the old incident edges remains a true edge of the modified body.** The supporting inequalities need not remain irredundant facets.

## 4. Quantified normal-cone cap barrier

### General theorem

Let `P0` be a full-dimensional polytope containing zero in its interior. Suppose distinct vertices `w_1,...,w_m` satisfy

`w_i·d <= -a ||w_i||||d||`

for all directions of their respective tangent cones, with `a>0`. Strict inequalities may be used, as in the C600 application.

Let `P` be any full-dimensional convex polytope such that

`P subset intersection_i T(w_i)`.

The old vertices need not belong to `P`. Its graph, number of vertices, and number of facets are unrestricted.

Let its actual uniform centroid be zero. Let `M` be any SPD physical metric with condition number at most `kappa`, and use `N=M^-1` for the polar mechanics. Put

`eta = (kappa-1)/(kappa+1)`,

`r = (a-eta)/(1+eta)`.

Assume `eta<a`. If, for every `i`, the modified body contains a point `z_i` satisfying

`||z_i-w_i|| <= epsilon ||w_i||`,

where

`2 epsilon < r^2`,                                                   (4.1)

then `P` has at least `m` distinct **strict** unstable vertices under `M`.

In particular, these are not merely weak rests or formal sink components.

### Proof

Scale `M` so that the midpoint of its largest and smallest eigenvalues is one. This does not affect equilibrium signs. Then

`||M-I||_op <= eta`, and `M <= (1+eta)I`.

For a tangent direction `d` at `w`,

`w^T M d <= -(a-eta)||w||||d||`.

Consequently, for `F(x)=x^T M x`,

`F(w+d)-F(w) <= -2(a-eta)||w||||d|| + (1+eta)||d||^2`.                (4.2)

On the sphere of radius `r||w||` about `w`, this gives

`F(x) <= F(w) - (1+eta)r^2 ||w||^2`.

On the other hand, a retained point satisfying the stated distance bound obeys

`F(z) >= F(w) - 2(1+eta)epsilon ||w||^2`.

Condition (4.1) puts its value strictly above every value on that sphere. Maximizing `F` on the compact set

`P intersect closed_ball(w,r||w||)`

therefore produces a maximizer strictly inside the ball. It is a vertex of `P`: a positive-dimensional face cannot have a local maximum of a strictly convex quadratic at a relative-interior point. At this vertex every outgoing true-edge primitive is strictly negative. A zero primitive would also make the quadratic increase along that edge at second order, contradicting local maximality.

It remains to separate the resulting vertices. For two original vertices `w_i,w_j`, each lies in the other's tangent polyhedron. Adding their two cone inequalities gives

`||w_i-w_j|| >= a(||w_i||+||w_j||)`.

The inequalities are strict for the certified C600 cones. Since `r<=a`, the localization balls are disjoint in the strict case. More generally, using `r<a` separates them even when the cone bounds are non-strict. Thus the unstable vertices obtained in the different balls are distinct.

### Explicit C600 forms

Use the certified rational value `a=1/21`.

**Euclidean metric.** For `M=I`, take

`r=1/21`, `epsilon=1/900`.

The strict gap is exactly

`r^2 - 2 epsilon = 1/22050 > 0`.

Thus any actual-centred convex polytope that remains in the two old tangent polyhedra and retains one point within `||u||/900` of `u` and one within `||v||/900` of `v` has at least two strict unstable vertices. The old vertices themselves may both have been removed.

**All metric orientations with condition at most `21/20`.** Here

`eta=1/41`, `r=10/441`, `epsilon=1/4000`,

and

`r^2 - 2 epsilon = 5519/388962000 > 0`.

This is an all-orientation, all-scale theorem in the parent's stated physical coordinate system. It is not an affine-invariant prohibition on changing the body's shape.

**Extension to the parent's entire condition sector `kappa<=11/10`.** Define the following exact algebraic number from the parent's 46 certified edges:

`a_* = min { -(w·e)/(||w||||e||) : w in {u,v}, e a true outgoing edge at w }`.

The parent proves `a_*>1/21`. At `kappa=11/10`, set

`r_* = (21 a_* - 1)/22 > 0`,

`epsilon_* = r_*^2/4`.

These are exact recovery formulas, not decimal estimates of a small margin. With these constants the same theorem protects two strict unstable vertices throughout the full `11/10` sector, **even after their old true stars have been replaced by cap geometry**. The data needed to evaluate `a_*` are exactly the 46 actual edge records already present in the pinned parent output.

### Actual centre motion is also allowed

There is a useful variant for a modification whose uniform centroid is recomputed as `c`, rather than completed back to zero. Suppose

`||c|| <= h min_i ||w_i||`.

The preceding proof, applied to `(x-c)^T M(x-c)`, works with localization radius

`(r-h)||w_i||`

provided `h<r` and

`2(1+h)epsilon < (r-h)^2`.                                          (4.3)

For example, at `kappa<=21/20`, one may take

`h=1/1000`, `epsilon=1/5000`.

The exact positive gap in (4.3) is

`67521443/972405000000`.

This variant is expressly about the modified body's actual uniform centroid. It does not freeze a centre while changing mass.

## 5. Direct application to the real plane135-completed cap class

Let `K` be the final C600 body with plane135 released, expressed about `g0=0`. It is bounded: the parent's `reachability.json` supplies a bounded common kernel even with both planes19 and135 removed, and adding plane19 can only shrink that kernel.

Add any finite collection of genuine halfspaces

`a_j·x <= 1`,

with zero in the interior of their intersection with `K`. Complete that new kernel by the unique plane

`q_*(caps)·x <= 1`

whose actual uniform body centroid is zero.

Global completion exists because the old plane135 already gives a bounded completion of the smaller kernel. All original supporting inequalities other than135 remain present. In particular, the two old tangent-cone systems remain valid; plane135 is not incident to either of the two parent unstable vertices.

For the Euclidean metric, sufficient retained-point tests are simply

`a_j·u <= 900/899`, `a_j·v <= 900/899` for every added cap,

and

`q_*(caps)·u <= 900/899`, `q_*(caps)·v <= 900/899`.

These inequalities say that the two exact radial witnesses

`(899/900)u`, `(899/900)v`

survive in the actually completed body. Under these conditions the completed body has at least two strict unstable vertices, regardless of how many old vertices the caps remove or what new true incidence they create.

For `kappa<=21/20`, replace the witnesses by `(3999/4000)u` and `(3999/4000)v`, and the support thresholds by `4000/3999`.

This is a whole-family obstruction, not a failure of a finite cap scan. It allows large remote boundary changes and does not require a globally small Hausdorff displacement. Its restrictions are the retained tangent inequalities, the stated retained points, and the actual-centre/metric conditions.

### Consequence for the ten-edge headroom

Adding a genuine small quadrilateral cap at the degree-four unstable vertex uses four true edges of the ten-edge headroom. It removes the old vertex, but that alone does not evade this theorem. Subsequent shallow caps at the newly created simple unstable vertex can change its true star again while still retaining the same original radial witness.

Therefore a sequence of small inward truncations is not automatically a cancellation mechanism just because the protected degree-four vertex and all four of its old incident edges have disappeared. To leave this certified domain, the construction must either remove the retained radial witness or permit points outside at least one of the old incident supporting halfspaces. An outward whole-facet actuation or an outward crease can do the latter; an inward crease preserving those halfspaces cannot.

No converse is claimed: leaving the domain may only move the extra unstable component elsewhere.

## 6. Exact global response of the completion to rejected material

There is a second result that is useful beyond the shallow-cap domain.

Let `P0=K intersect {q0·x<=1}` be the original centred completion. Let `K'` be the kernel after adding arbitrary caps, and let

`P1=K' intersect {q1·x<=1}`

be its actual-centred completion. Define the bounded body before applying those caps at the new completion plane by

`B=K intersect {q1·x<=1}`,

and let

`R=B minus K'`

be the material actually rejected by the caps at that plane. All moments in the following identity are actual uniform volume integrals.

Since `P1` is centred,

`J(B)=J(R)`, while `J(P0)=0`.

Put `Delta q=q1-q0`. Directly comparing the two halfspace completions gives the exact identity

`-Delta q · J(R)`

`    = integral over (B symmetric-difference P0) of |Delta q·x| dx`.    (6.1)

To verify it, on `B minus P0` one has `Delta q·x<0`, whereas on `P0 minus B` one has `Delta q·x>0`. Subtracting the two first-moment integrals gives (6.1).

If the completion plane changes, the right side is strictly positive. Thus, whenever `R` has positive volume,

`Delta q · centroid(R) < 0`.                                        (6.2)

This says that the normalized support value of the completing plane decreases at the centroid of the rejected material. It does **not** say that the entire rotated halfspace expands by set inclusion.

Identity (6.1) is nonperturbative. It permits arbitrary cap normals and incidence events elsewhere in the body. In this C600 application boundedness of `K` is already certified; no unstated extension of the completion domain is needed.

For a rejected region whose centroid lies exactly on the positive ray of the trapped vertex, (6.2) forces the completion plane to loosen, rather than tighten, its normalized support value along that ray. For a general cap, the exact rejected centroid must be used. Substituting the old vertex for that centroid without controlling their difference would be incorrect.

## 7. Genuine local cap geometry and cubic actual-centre completion

The following is a local construction theorem and an exact certification recipe. **It is not a newly persisted fixed-depth checkpoint:** no particular rational depth and new actuator isolating box are promoted here.

### Complete cap recipe from the literal parent

Work about `g0=0`. Let `e_1,...,e_4` be the four actual outgoing edge vectors at `u`, listed in the cyclic order of its true vertex link. Let `q_1,...,q_4` be its four active poles, carrying raw labels `3,41,67,68`.

Choose a rational vector `n` in the relative interior of `conv(q_1,...,q_4)`, with the genericity conditions below. Then `n·u=1` and

`b_i=-n·e_i>0`, `r_i=e_i/b_i`.

For depth `t>0`, add the actual halfspace

`n·x <= 1-t`.

For sufficiently small `t`, it cuts off only the old vertex. The four new vertices are exactly

`c_i(t)=u+t r_i`.

The new maximal facet is the true quadrilateral with those four vertices. It is not an independently folded collection of integration triangles.

A deterministic rational choice of `n` is available without optimization: enumerate positive integer weight quadruples in increasing maximum weight, then lexicographically, and set

`n=(sum_i w_i q_i)/(sum_i w_i)`.

Accept the first quadruple for which all four values `u·r_i` are distinct and, for every incident pole `q_f`,

`n·(q_f-n) != 0`, `q_f·(n-q_f) != 0`.

These exclude only finitely many proper algebraic subsets of the interior normal polygon, so the enumeration terminates. All inputs to this recipe are exact rational data from the final parent's non135 planes and the rational target centre. No older canonical labels are needed.

### Complete true-incidence update rule

For each of the four old facet cycles containing consecutive vertices `a,u,b`, replace that corner by the two cut points on `u--a` and `u--b`, preserving the cycle orientation. Replace each old edge `u--v_i` by `c_i--v_i`; retain every other old edge; add the four edges of the new quadrilateral. Add its supporting plane `n·x=1-t`.

The remote vertices incident to plane135 are reconstructed using the new completed plane, not left at their old positions. For sufficiently small depth its original incidence chamber persists.

The feature counts are therefore

`(V,E,F)=(171,304,135)`, `C=608`.

All of these are maximal-facet and true-edge counts.

### Exact removed moments

Let

`T=conv(0,r_1,r_2,r_3,r_4)`,

`W=Vol(T)`, `L=integral_T x dx`.

In the cyclic order above, the complete rational formulas are

`d1=|det(r_1,r_2,r_3)|`, `d2=|det(r_1,r_3,r_4)|`,

`W=(d1+d2)/6`,

`L=[d1(r_1+r_2+r_3)+d2(r_1+r_3+r_4)]/24`.

The removed tip is `u+tT`. Consequently its actual volume and first moment are exactly

`Vol(tip)=W t^3`,

`J(tip)=W u t^3 + L t^4`.                                           (7.1)

These are physical cone moments. No independently fitted facet masses or tetrahedral-centroid covariance is used.

### Completion expansion, including its sign

Let `q0` be the original centred pole135. Let

`H0 = [Area(F135)/||q0||] E_F135(xx^T)`.

This is the actual whole-facet matrix; it is positive definite. For sufficiently small depth the removed tip is independent of the changing plane135, because that plane is initially strictly inactive at `u`.

The exact completion equation is then

`J(P(q(t))) = W u t^3 + L t^4`,

where `P(q)` is the body before applying the new cap. Since `D_q J=-H0` at `q0`, the local solution satisfies

`q(t)=q0 - W H0^-1 u t^3 - H0^-1 L t^4 + O(t^6)`.                   (7.2)

There is no fifth-order term: the forcing in (7.1) has only third- and fourth-order terms, while the first nonlinear inverse-map contribution is quadratic in that forcing and begins at order six.

In particular,

`d^3[q(t)·u]/dt^3 at t=0 = -6W u^T H0^-1 u < 0`.                  (7.3)

Thus the leading actual-centre correction loosens the completing plane's support value at the old unstable vertex. A cap's linear geometric displacement is not accompanied by a first-order centre-actuator motion that somehow cancels its trap.

The completed volume also has an exact leading expansion:

`Vol(completed cap body)`

` = Vol(P0) - W(1-q0·u)t^3 + (q0·L)t^4 + O(t^6)`.                 (7.4)

The cubic loss is strictly positive because plane135 is inactive at `u`. This agrees with the parent's global maximum-volume characterization of the centred completion.

### Strict physical census of the sufficiently small generic-cap family

This family has strict census `(S,U,H)=(1,2,1)` and physical weak census `(0,0,0)` for all sufficiently small positive depths.

The proof is direct. On the new quadrilateral,

`D(c_i -> c_j)=t u·(r_j-r_i)+t^2 r_i·(r_j-r_i)`.

The generic linear functional `u·r` has a unique maximum on that convex quadrilateral. Its maximizing vertex has negative outgoing primitives along both cap edges; its remaining old-edge direction is negative by the original strict unstable cone. It is therefore a strict unstable vertex. Every other cap vertex has a strictly positive cap-edge escape.

Each cap edge has a strictly positive primal primitive at one endpoint for sufficiently small depth, so no cap edge is a saddle. The cap's orthogonal foot is not near `u`: otherwise `n` would be parallel to `u`, contrary to the distinct-value condition. Thus the new facet is not stable. The generic dual inequalities ensure that the added dual primitives are also nonzero for sufficiently small depth.

The old stable facet3, the other unstable vertex, and the old saddle remain strict by their original margins and the cubic size of the actual completion change. The retained old edge and facet tests have their actual signs, not selected-forest signs. Therefore no physical weak contacts appear.

This is a genuine change from a degree-four unstable vertex to a simple unstable vertex, but it is not cancellation. It supplies a controlled nonwinning cap mechanism and explains why changing the star alone is insufficient.

One can repeat the argument with successively smaller generic caps at the newly created simple unstable vertex. The next two local families have

```text
first cap:   171 / 304 / 135, C608, own121 physicalweak000
second cap:  173 / 307 / 136, C614, own121 physicalweak000
third cap:   175 / 310 / 137, C620, own121 physicalweak000
```

The depths must be chosen successively small enough for each stated local regime. These are local family theorems, not three newly isolated numerical checkpoints. While the original radial witnesses are retained, the whole-family theorem in Section 4 also rules out cancellation throughout such a cap stack.

## 8. Exact actuator isolation can reuse the parent Jacobian

There is a useful implementation simplification here.

Use the parent's raw-coordinate centring function

`F(q)=J_raw(P(q))-V(P(q))g0`.

For a fixed cap tip independent of `q`, the new function is exactly

`F_cap(q)=F(q)-mu(t)`,

`mu(t)=W u t^3+L t^4`.

Thus its derivative with respect to the three raw plane135 parameters is **identical** to the old derivative. There is no new derivative approximation or independent mass fit.

The parent final raw normal box is the coordinatewise box of radius `2^-35` about the exact rational midpoint

```text
(2.180055506877234,
 -0.5126742306391376,
 -0.9005169151446033).
```

These decimals are finite rational inputs. They are not the actual algebraic normal.

Let `A` be the parent's exact rational interval-Newton preconditioner, `rho` its derivative contraction bound, and `r_B=2^-35`. The new normal is rigorously isolated in this same box once

`||A(F(q_mid)-mu(t))||_infinity < (1-rho)r_B`                       (8.1)

and the actual cap-incidence tests hold throughout the box. The derivative contraction bound remains `rho`.

A simpler sufficient test is

`||A mu(t)||_infinity`

` < (1-rho)r_B - ||A F(q_mid)||_infinity`.

The right side is strictly positive in the parent certificate. The left side is `O(t^3)`. Hence a deterministic dyadic halving procedure terminates: choose the generic rational cap normal as above, try `t=2^-k` starting at `k=20`, and increase `k` until (8.1), the complete true-support tests, and all physical primitive sign tests pass.

The cap vertices and their new local supports are rational. The only remaining algebraic variable is the same three-component actuator normal, now isolated by (8.1). Because the actual tip moments have been subtracted, this is a real uniform-centroid certificate, not reuse of an obsolete centre.

This procedure is justified to terminate in the local generic-cap regime. I have not run it to a newly pinned fixed-depth endpoint in this handoff. Accordingly the C600 parent, rather than an unreported C608 normal, remains the last persisted exact object.

## 9. Small complete checker for the new rational collar constants

The following unit reproduces the exact scalar inequalities used in Sections 4 and 5. It has no external input, no random seed, and no nonstandard dependency. It does not purport to replay the parent geometry or to certify a new actuator normal. The mathematical cone and moment proofs above are not replaced by this scalar check.

Environment: CPython 3.13.5, standard library only. Save as `cap_collar_constants.py` and run `python -B -S cap_collar_constants.py`.

```python
from fractions import Fraction as F


def collar(kappa):
    if kappa < 1:
        raise ValueError('Condition bound must be at least one')
    a = F(1, 21)
    eta = (kappa - 1) / (kappa + 1)
    if eta >= a:
        raise ValueError('Use the strict parent algebraic margin at this boundary')
    return (a - eta) / (1 + eta)


cases = [
    ('Euclidean', F(1), F(0), F(1, 900), F(1, 22050)),
    ('condition_21_over_20', F(21, 20), F(0), F(1, 4000),
     F(5519, 388962000)),
    ('actual_centre_motion', F(21, 20), F(1, 1000), F(1, 5000),
     F(67521443, 972405000000)),
]

for name, kappa, h, epsilon, expected in cases:
    r = collar(kappa)
    assert r > h
    gap = (r - h)**2 - 2*(1 + h)*epsilon
    assert gap == expected
    assert gap > 0
    print(name, 'radius_coefficient', r, 'strict_gap', gap)

assert collar(F(1)) == F(1, 21)
assert collar(F(21, 20)) == F(10, 441)
assert 1/(1-F(1, 900)) == F(900, 899)
assert 1/(1-F(1, 4000)) == F(4000, 3999)
assert 1/(1-F(1, 5000)) == F(5000, 4999)
print('C600_CAP_COLLAR_RATIONAL_CONSTANTS_PASS')
```

Expected terminal marker:

```text
C600_CAP_COLLAR_RATIONAL_CONSTANTS_PASS
```

No new cold-replay receipt, output byte count, or SHA-256 is asserted for this supplied checker. The exact fractions are independently derived in the proof, and no claimed new body depends on an unobserved run.

## 10. What is closed, what remains open, and the next viable mechanism

**Closed by this handoff:** the stated whole family of actual-centred cap-completed bodies retaining the old tangent inequalities and radial witnesses cannot have U=1. This includes bodies with changed true incidence and deleted old unstable vertices. The explicit rational collar covers every orientation and scale with condition at most `21/20`; the exact algebraic-margin version extends the conclusion to the parent's full `11/10` sector. The actual-centre-motion variant has its separately stated bounds.

**Not closed:** large caps that remove the witnesses, outward releases of a trapping supporting halfspace, metrics outside the stated sectors, or arbitrary deformations of the body. The response identity in Section 6 constrains their actual mass compensation but does not exclude cancellation. No whole-interval equilibrium census is inferred from a local cap expansion.

**No record change:** there is no new own110physicalweak000 object, and no new fixed C608/C614/C620 algebraic endpoint is presented as persisted. The local family constructions have complete geometric and moment recipes, but a particular actuator normal still requires the described isolation and full census checks before promotion.

The most useful constructive continuation is now more sharply defined. Use a true whole-facet or outward-crease actuation that releases one of the degree-four trap's supporting inequalities, or make a sufficiently deep cap that explicitly removes its radial witness and reaches the saddle-connected boundary. The centre equation should be solved with the actual removed moments; where the tip is independent of135, reuse the exact residual-shift method instead of rebuilding an unnecessarily larger algebraic system. The already certified noncancelling `83/135 -> 3/45` flip is not revisited or treated as cancellation.
