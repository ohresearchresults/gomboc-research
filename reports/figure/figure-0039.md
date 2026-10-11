# figure-0039

Historical AI scientific report · saved 2026-08-23 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Effective circumscribed transfer theorem for the exact spectral-phase seed

## 0. Result and correction

The earlier one-cone proposal is discarded. A straight cone can acquire stable side faces when the two principal radial curvatures are unequal. The construction below uses two different fixed local mechanisms:

* a rational tangent-sphere collar around the stable equilibrium of the polar;
* a rational Thales spiral around the unstable equilibrium of the polar.

The spiral is the effective version of the decreasing-distance polygonal curve in Lángi's Lemma 3 and unstable-patch construction. Lángi proves qualitative equilibrium-preserving polyhedral approximation, but his proof leaves the mesh size, cap depths, number of rotations, finite cover, and centroid tolerance unevaluated. :contentReference[oaicite:0]{index=0}

The fixed constants below remove those choices for the transcript's particular smooth body.

## 1. Seed and polar

For `u=(x,y,z) in S^2`, put

`eta(z)=(3*pi/2)(z-z^3/3)`,

`f(t)=sin(2t)/50+cos(4t)/100`,

`p(z)=eta(z)+f(eta(z))`,

`q(u)=x cos p(z)+y sin p(z)`,

`rho(u)=(1+q(u)/15)^(1/4)`.

Let `K={lambda u: 0<=lambda<=rho(u)}`. The transcript proves that the uniform centroid of `K` is exactly zero, its radial function has exactly one maximum and one minimum, and its radial second-fundamental-form numerator satisfies

`B_K >= (1/30) I`.                                                    (1)

The two critical directions are

`u_+=(cos(1/100),sin(1/100),0)` and `u_-=-u_+`.

The maximum of `rho` is at `u_+`; the minimum is at `u_-`. These are the unique unstable and stable equilibria of `K`, respectively. :contentReference[oaicite:1]{index=1}

Let `L=K^o`. Its support function is explicit:

`h(u)=h_L(u)=1/rho(u)=(1+q(u)/15)^(-1/4)`.                              (2)

Thus `h` has a strict minimum at `u_+` and a strict maximum at `u_-`. Write

`x(u)=h(u)u+grad h(u)` and `A(u)=Hess h(u)+h(u)I`.

`A` is the principal-radius matrix of `L`.

## 2. Fully evaluated smooth constants

Direct differentiation, using `pi<22/7`, gives

`|p'|<51/10`, `|p''|<16`, `|p'''|<127`,                               (3)

where these derivatives are taken in the Cartesian variable `z`. For the spherical phase `P(theta)=p(cos theta)`, the sharper direct bounds are

`|P_theta|<51/10`, `|P_thetatheta|<113/10`.

In the orthonormal spherical frame they give

`|grad q|<31/5`, `||Hess q||<50`.                                      (4)

For `R(t)=(1+t/15)^(1/4)` and `H(t)=1/R(t)` on `[-1,1]`,

`49/50 < rho,h < 51/50`,

`0<R'<1/56`, `|R''|<1/1000`,

`1/66<|H'|<1/55`, `0<H''<1/600`, `|H'''|<1/3000`.                      (5)

The identity

`A=(rho^2 I+2 drho tensor drho-rho Hess rho)/rho^3 = B_K/rho^3`          (6)

and (1), (3)-(5) imply the global rolling-radius bounds

`(1/32)I < A(u) < (9/4)I` for every `u in S^2`.                         (7)

For the upper bound, `|grad rho|<31/280`, `||Hess rho||<1`, and hence the numerator in (6) is below `(21/10)I`; division by `(49/50)^3` is below `9/4`. For the lower bound, `(1/30)/(51/50)^3>1/32`.

At either critical point the absolute Hessian of `q` has determinant one and trace below 29. Consequently every absolute eigenvalue of `Hess h` there is greater than

`1/(66*29)>2^-11`.                                                      (8)

A componentwise differentiation of the ambient formula for `q`, followed by the spherical restriction formulas, gives

`||nabla^3 h||<2^12`.                                                    (9)

For reproducibility, the only nontrivial ambient third derivative is bounded by

`|p'''|+|p'|^3+3|p'p''|<512`;

all remaining terms in `nabla^3 h` are bounded by (3)-(5).

Let `Phi(v)=rho_L(v)^2`, where `rho_L` is the radial function of `L`. On each geodesic cap of radius `2^-42` about `u_+` or `u_-`, the normal-to-radial map has singular values in `[1/3,2]`. Equations (7)-(9) therefore yield

`Hess Phi >= 2^-16 I` near `u_+`,

`Hess Phi <= -2^-16 I` near `u_-`,                                    (10)

and `||Hess Phi||<64` on both caps. Hence, if `s=d(v,u_+)<=2^-42`,

`rho_L(v) >= h(u_+)+2^-20 s^2`,                                       (11)

and if `s=d(v,u_-)<=2^-42`,

`h(u_-)-32s^2 <= rho_L(v) <= h(u_-)-2^-20 s^2`.                        (12)

The longitude-twist map

`Psi(x,y,z)=(x cos p(z)+y sin p(z),-x sin p(z)+y cos p(z),z)`

and its inverse have differential norm below seven. Since `q` becomes the first coordinate after this twist,

`|grad h(u)| >= 2^-13 d(u,{u_+,u_-})`.                                 (13)

This is a global separation estimate, not a compactness assertion.

## 3. Two quantitative lemmas

### 3.1 Support-gap lemma

If a smooth convex body has `mI<=A<=MI`, then the ball of radius `M` tangent at `x(n)` contains the body. Therefore, for `y in L`,

`h(n)-n dot y <= eps  =>  |y-x(n)|<=sqrt(2M eps)`.                      (14)

If `y` is an equilibrium relative to a reference point `e`, so that `y-e` is parallel to `n`, then

`|grad h(n)|<=|e|+sqrt(2M eps)`.                                       (15)

This applies without distinguishing faces, edges, and vertices: at any polyhedral equilibrium the radial direction is itself a supporting normal.

### 3.2 Explicit net lemma

Let a finite set of unit normals be a chordal `delta`-net. If every associated support plane is shifted inward by `8delta`, with support-evaluation and dyadic-rounding errors below `delta`, then their intersection `Q_0` satisfies

`(1-16delta)L subset Q_0 subset L`,                                    (16)

and

`0<=h_L-h_{Q_0}<17delta`.                                              (17)

Proof: a nearest net normal first gives `|x|<2` for `x in Q_0`; a second nearest-normal estimate, together with the fact that `L subset (51/50)B`, gives `n dot x<h(n)` for every unit `n`. The reverse inclusion follows because every rounded offset is at least `h(n_i)-9delta` and `h>49/50`.

## 4. Fixed rational oracle

No precision is selected at run time.

1. Evaluate `pi=16 arctan(1/5)-4 arctan(1/239)` with exactly 4096 terms of each alternating series.
2. Evaluate every sine and cosine with exactly 4096 Taylor terms and an outward rational remainder bound.
3. Evaluate each fourth root by exactly 4096 rational bisection steps.
4. Return intervals of width below `2^-2000`.
5. Every support offset is rounded downward to the grid `2^-2048 Z`.

All trigonometric arguments have absolute value below four. The stated term counts make every omitted remainder smaller than `2^-8000`.

Write `floor_B(t)=2^-B floor(2^B t)`.

## 5. Global rational halfspaces

Set

`delta=2^-300`, `D=2^304`.

Use the rational stereographic chart

`sigma(a,b)=(2a,2b,1-a^2-b^2)/(1+a^2+b^2)`

at each of the six signed coordinate poles. In every chart take

`a=i/D`, `b=j/D`, `-D<=i,j<=D`.

The union is a chordal `delta`-net because every point belongs to a chart with `|a|,|b|<=1` and `sigma` is 2-Lipschitz there. The number of normals is

`N_g <= 6(2D+1)^2 < 2^614`.                                            (18)

For each normal `n_i`, let `[l_i,r_i]` be its oracle interval for `h(n_i)` and put

`b_i=floor_2048(l_i-8delta)`.

Define

`Q_0=intersection_i {x:n_i dot x<=b_i}`.                               (19)

Equations (16)-(17) hold, and all coefficients in (19) are rational.

## 6. Rational azimuth polygon

Set `J=2^48`. In a rational orthonormal tangent basis use the unit vectors

`w_j=((J^2-j^2)/(J^2+j^2),2Jj/(J^2+j^2))`, `-J<=j<=J`,

together with their negatives. Let

`W={y:w dot y<=1 for every listed w}`.                                 (20)

There are fewer than `2^51` listed normals. Their maximum angular gap is below `2/J`; hence

`B^2 subset W subset (1+2^-94)B^2`.                                   (21)

The same `W` is used in both local patches.

## 7. Stable tangent-collar patch in the polar

Let

`t_0=floor_2048(tan(1/200))`,

`d_s=((1-t_0^2)/(1+t_0^2),2t_0/(1+t_0^2),0)`,

`e_{s1}=(-d_{s2},d_{s1},0)`, `e_{s2}=(0,0,1)`.

Then `d(d_s,u_+)<2^-2040`.

Put

`h_s=(16/15)^(-1/4)`,

`A_s=floor_2048(h_s)-2^-240`,

`eta_s=A_s+2^-13`, `sigma_s=2^-65`,

`tau_s=2 eta_s sigma_s^2/(1+sigma_s^2)`,

`r_s=2 eta_s sigma_s/(1+sigma_s^2)`,

`z_s=A_s-tau_s`.                                                       (22)

Add the central plane

`d_s dot x<=z_s`.                                                       (23)

For every `w=(w_1,w_2)` from (20), write

`w^*=w_1 e_{s1}+w_2 e_{s2}`

and add

`(eta_s-tau_s)(d_s dot x-(A_s-eta_s))+r_s w^* dot x<=eta_s^2`.         (24)

All quantities are rational. On the plane (23), equations (24) reduce exactly to `w^* dot x<=r_s`; hence the intended face is

`F_s={z_s d_s+y:y in r_s W}`.

The radius matrix of `L` exceeds `eta_s I` throughout the relevant normal cap by more than `2^-13 I`. Thus the spherical cap of the ball with center `(A_s-eta_s)d_s` and radius `eta_s` lies inside `(1-16delta)L`. The outward inflation in (21) is below `2^-158`, while the ball-to-`L` gap at the rim is above `2^-145`. Consequently `F_s subset int(Q_0)` and its orthogonal projection of the origin, `z_s d_s`, is in its relative interior with Euclidean margin greater than `2^-65`.

For a boundary point represented by `w in bd(W)`, the ray

`x(t)=(z_s-t r_s)d_s+(r_s+t(eta_s-tau_s))w^*`, `t>=0`,                 (25)

lies on a side facet. Its radial derivative at `t=0` is

`x(0) dot x'(0)=r_s[(eta_s-tau_s)|w|^2-z_s]`

`>=r_s(eta_s-A_s)=2^-13 r_s>2^-79`,                                   (26)

and the derivative increases with `t`. Therefore every side face, side edge, side vertex, and every transition feature with `Q_0` has a nonzero radial tangent. The sole equilibrium in this patch is the stable face `F_s`.

## 8. Unstable rational Thales-spiral patch in the polar

Set `d_u=-d_s`, `e_{u1}=-e_{s1}`, `e_{u2}=e_{s2}` and

`h_u=(14/15)^(-1/4)`,

`A_u=floor_2048(h_u)-2^-240`,

`k=2^31`, `t=2^-82`,

`C=(1-t^2)/(1+t^2)`, `S=2t/(1+t^2)`,

`epsilon=2^-154`, `a=C-epsilon`.                                      (27)

Let `(C_i,S_i)` be defined exactly by

`C_i+i S_i=(C+iS)^i`, `0<=i<=k`.

Put

`z_i=A_u a^i C_i`, `r_i=A_u a^i S_i`.                                 (28)

The angle increment is `Delta=2 arctan t`; thus

`2^-51<k Delta<2^-50`.                                                  (29)

For every `1<=i<=k`,

`Delta z_i=z_i-z_{i-1}<0`, `Delta r_i=r_i-r_{i-1}>0`.                  (30)

For each `w=(w_1,w_2)` from (20), put `w^*=w_1e_{u1}+w_2e_{u2}` and add the rational halfspace

`Delta r_i (d_u dot x)-Delta z_i (w^* dot x)`

`<=Delta r_i z_{i-1}-Delta z_i r_{i-1}`.                              (31)

The meridional points `X_i=A_u a^i(C_i,S_i)` satisfy the exact identities

`X_i dot (X_i-X_{i-1})=A_u^2 a^(2i-1)(a-C)<0`,                         (32)

`det(X_i-X_{i-1},X_{i+1}-X_i)`

`=A_u^2 a^(2i-1) S(1+a^2-2aC)>0`.                                    (33)

Equation (33) proves convexity of the profile. Equation (32) is the strict, rational version of the Thales-chain condition in Lángi's Lemma 3. :contentReference[oaicite:2]{index=2}

For a side point with a fixed `w in bd(W)`, the endpoint radial derivative is

`z_i Delta z_i+|w|^2 r_i Delta r_i`.

At `|w|=1` this is the left side of (32). By (21),

`(|w|^2-1)r_i Delta r_i<2^-210`,

whereas the magnitude in (32) is greater than `2^-156`. Hence the radial distance strictly decreases along every complete side segment, with normalized margin greater than `2^-80`.

The first ring lies strictly inside `Q_0`: its radial loss is greater than `2^-155`, whereas (12) and its angular radius give a loss of the smooth boundary below `2^-156`. Thus the spiral replaces every ray in a cap of radius `2^-84` about `d_u`.

The last ring lies strictly outside `L`: Bernoulli's inequality and (27) give

`1-a^k<k(1-a)<2^-123+2^-131<2^-122.9`,

while (12), (29), and the lower angular radius of `W` give a smooth radial loss greater than `2^-122`. The two bounds differ by more than `2^-125`.

The first family of planes in (31) meets at the rational apex

`q_u=A_u d_u`.                                                         (34)

Every other point of the patch has a feasible direction along which radial distance decreases. Moreover, `d_u dot x<A_u` for every other point of the resulting body, so the plane `d_u dot x=A_u` supports it only at `q_u`. Thus `q_u` is the unique unstable equilibrium in this patch. All side faces, edges, vertices, and all transition features are excluded by the normalized monotonicity margin above.

The number of planes in (31) is below

`k(4J+2)<2^82`.                                                        (35)

## 9. The inner polar polytope and global exclusion

Let `Q` be the intersection of `Q_0` with all halfspaces (23), (24), and (31).

Every local halfspace contains `(9/10)B`, so

`(9/10)B subset Q subset L subset (51/50)B`.                           (36)

The first stable ring and first unstable ring lie in `int(Q_0)`. Hence any boundary feature of `Q` not incident with a local-patch plane has radial direction at distance at least `2^-84` from both critical directions.

For such a feature, (17) gives a support gap below `17delta<2^-295`. If it were an equilibrium relative to the origin, (14) would give

`|grad h|<2^-145`,

whereas (13) gives

`|grad h|>2^-97`.

This contradiction excludes every remaining face, vertex, and edge equilibrium.

The local arguments in Sections 7-8 give exactly one stable face and one unstable vertex and no edge equilibrium. Therefore

`S(Q,0)=1`, `U(Q,0)=1`, `H(Q,0)=0`.                                   (37)

The normalized origin-reference margin of every intended or excluded feature is greater than

`gamma_Q=2^-100`.                                                       (38)

The four sources of this minimum are: `2^-65` for the stable-face inradius, `2^-79` for the stable collar, `2^-80` for the spiral, and `2^-97` for the global region.

## 10. Circumscribed polytope

Define

`P_0=Q^o`.                                                             (39)

Since `Q subset L=K^o`, polarity gives `K subset P_0`.

Enumerate every vertex of `Q` by solving every nonsingular triple of boundary-plane equations and retaining exactly the solutions satisfying the complete rational halfspace list. Equal solutions are grouped; zero determinants are retained as nonsimple incidences rather than perturbed.

If `Vert(Q)={v_1,...,v_N}`, the required rational circumscribed list is

`P_0=intersection_{j=1}^N {x:v_j dot x<=1}`.                           (40)

Clearing denominators makes (40) an integer halfspace list.

Polarity sends a `k`-dimensional equilibrium feature relative to the origin to a `(2-k)`-dimensional equilibrium feature. Thus (37) gives

`S(P_0,0)=1`, `U(P_0,0)=1`, `H(P_0,0)=0`.                              (41)

The unique stable face of `P_0` is dual to the apex `q_u`; its plane is `q_u dot x=1`. The unique unstable vertex is dual to `F_s` and equals

`v_s=d_s/z_s`.                                                         (42)

## 11. Hausdorff and centroid transfer

Outside two normal caps the support deficit is below `2^-295`. Every new unstable-patch normal is within `2^-49` of `d_u`, every new stable-patch normal is within `2^-63` of `d_s`, and the strong monotonicity following from (7) puts every adjacent global normal inside a cap of radius `2^-38`.

If a local plane and a global plane are simultaneously active, (7) and (14) give

`d(n_local,n_global)<=64 sqrt(2(9/4)2^-96)<2^-38`.

On those two caps,

`0<=h_L-h_Q<2^-96`.                                                     (43)

Their total spherical area is below `2^-72`. Therefore

`integral_{S^2}(h_L-h_Q) d omega <2^-167`.                             (44)

Since `h_Q>9/10` and `h_L>49/50`,

`0<=rho_{P_0}-rho_K<2(h_L-h_Q)`.                                      (45)

Consequently

`d_H(P_0,K)<2^-94`.                                                     (46)

For a star body `B`,

`V(B)=(1/3) integral rho_B^3 d omega`,

`M(B)=(1/4) integral rho_B^4 u d omega`.

The seed has `M(K)=0`. Equations (36), (44), and (45) give

`|M(P_0)|<2^-165`.

Also `V(P_0)>V(K)>3`. Hence the exact uniform-volume centroid satisfies

`|c(P_0)|<2^-160`.                                                       (47)

This bound is evaluated; no centroid-control caps or continuity choice are used.

For bodies between `(50/51)B` and `(10/9)B`, every normalized face, vertex, or edge equilibrium predicate is 64-Lipschitz in the reference point. Polarity changes the normalized margin (38) by a factor smaller than 64, so every origin-reference predicate of `P_0` has absolute margin above `2^-106`. By (47), changing the reference point from zero to `c(P_0)` changes it by less than `2^-154`. Therefore

`S(P_0,c(P_0))=1`, `U(P_0,c(P_0))=1`, `H(P_0,c(P_0))=0`.               (48)

## 12. Exact centroid and exact feature certificate

All vertices of `P_0` are rational. Group coplanar triangles into maximal faces and triangulate each face from its lexicographically least vertex. For every outward triangle `(a,b,c)`, set

`D_abc=det(a,b,c)`.

Then

`V(P_0)=sum D_abc/6`,

`c(P_0)=sum D_abc(a+b+c)/(4 sum D_abc)`.                               (49)

Thus the centroid is an exact rational vector.

The certificate audits every feature relative to this exact centroid.

* Face `F` in `n dot x=b`: compute `p=c+((b-n dot c)/(n dot n))n`; exact oriented edge determinants test `p in relint(F)`.
* Vertex `v`: it is unstable exactly when `(v-c) dot (w-v)<0` for every other vertex `w`.
* Edge `[v,w]`: put `t=-((v-c) dot (w-v))/|w-v|^2` and `p=v+t(w-v)`. It is an edge equilibrium exactly when `0<t<1` and `(p-c) dot (z-p)<=0` for every vertex `z`, with equality exactly on the edge.

The output records one positive stable-face certificate, one positive unstable-vertex certificate, and one strict excluding witness for every other face, vertex, and edge. These checks use rational arithmetic only and independently verify (48).

The centered representation is obtained without approximation:

`v_j dot x <= 1-v_j dot c(P_0)`.                                       (50)

It describes `P_0-c(P_0)` and has centroid exactly zero.

## 13. Evaluated size and deterministic control flow

The number of halfspaces defining `Q` is below

`2^614+2^82+2^51+1<2^615`.                                             (51)

Every three-dimensional polytope with `F` facets has at most `2F-4` vertices. Hence the final circumscribed list (40) has

`N<2^616` rows.                                                         (52)

Fewer than `2^1845` triple-plane systems are tested. No simplicity assumption is used.

The complete algorithm is:

**SPG-EFFECTIVE**

1. Run the fixed 4096-term rational oracle.
2. Generate the `D=2^304` stereographic normal net and offsets (19).
3. Generate `W` with `J=2^48`.
4. Append the stable planes (23)-(24).
5. Generate `k=2^31` spiral levels by exact rational recurrence and append (31).
6. Enumerate all feasible triple intersections to obtain `Vert(Q)`.
7. Return the circumscribed list (40).
8. Reconstruct maximal faces and true edges exactly.
9. Compute the exact centroid by (49).
10. Audit every face, vertex, and edge by the predicates in Section 12.
11. Return both (40) and the centered list (50), together with the witness table.

Every loop bound, denominator, rounding direction, patch depth, angular mesh, and acceptance predicate is fixed above. The construction uses no phrase of the form `sufficiently fine`, `sufficiently close`, `generic`, or `after a perturbation`.
