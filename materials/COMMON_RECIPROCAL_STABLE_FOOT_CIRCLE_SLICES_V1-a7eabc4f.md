# material-a7eabc4fb074

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# COMMON_RECIPROCAL_STABLE_FOOT_CIRCLE_SLICES_V1

## Status and purpose

This is a new coordinator analytical result about ONE physical metric and its literal inverse. It applies to any fixed genuine convex three-dimensional polyhedron with an interior origin; for the research problem the origin is its actual uniformly filled volume centroid. It does not replace that centroid by vertex weights, does not count triangulation diagonals, and does not supply a C34 construction or exclude the entire E17 layer. The accepted interval remains 34 <= C_min <= 622.

The general normal descent and finite five-contact alternative in fully read parent minimum-0218 (SHA d2708a7da6c6867a9f47f2960251aa8600f88769bc3d919060ca8719add3a723) motivated looking at a fixed facet foot. The new results below are direct algebra and planar geometry: an exact five-dimensional metric atlas, a convex common-root-eligibility domain, a three-pole formula for the minimum tangential trace, and a finite circle-arrangement solution of every two-dimensional reciprocal slice. They do not assume that full-rank components touch rank two.

## 1. Exact stable-foot atlas for metric rays

Let P=conv(X_i) be a full-dimensional polyhedron with 0 in its interior. Its actual maximal facets have poles q_g, so q_g.X_i<=1. Fix a candidate stable facet S. Apply ONE fixed invertible linear coordinate change such that q_S=e_3. Vertices and poles transform contragrediently, and the physical M and N=M^{-1} transform by the corresponding congruences. Actual volume centring is preserved. No Euclidean orthogonality of this convenient coordinate chart is asserted.

The foot of the origin on the plane q_S.X=1 in metric M is

    p = N q_S / (q_S^T N q_S).

Write p=(f_1,f_2,1), f=(f_1,f_2). S is strictly stable exactly when p lies in the relative interior of the ACTUAL facet S. Put s=q_S^T N q_S>0. Multiplying M by s does not change any mechanical sign, and gives M p=e_3. Thus every metric ray with that foot has the unique representative

    M(f,J) = [ J        -J f             ]
             [ -f^T J   1+f^T J f        ],

where J is a symmetric positive definite two-by-two matrix. Conversely every such J gives an SPD matrix, since

    (y,h)^T M(y,h) = (y-h f)^T J(y-h f)+h^2.

Its literal inverse is

    N(f,J) = [ J^{-1}+ff^T   f ]
             [ f^T          1 ].

In particular N e_3=p and q_S^T N q_S=1. Therefore (f,J), with p in relint(S), is a bijective atlas for metric rays making S strictly stable. It has two foot coordinates and three coordinates of J, not independent primal and dual metrics.

Write

    J = (1/2) [ r+x  y   ] ,   r>0,   x^2+y^2<r^2.
              [ y    r-x ]

Thus fixing f and the tangential trace r leaves a genuine two-dimensional open disk of physical metrics. No definiteness limit or nondegeneracy of equilibrium contacts is assumed in this parametrization.

## 2. All true-edge primitives are lines or circles on a slice

Write X_i=(y_i,h_i), q_g=(a_g,b_g), with two-dimensional y_i,a_g. Define

    u_i = y_i-h_i f,
    v_g = b_g+a_g.f,
    d = det(J) = (r^2-x^2-y^2)/4 > 0.

For a true oriented primal edge i->j put e=u_j-u_i and beta=h_i(h_j-h_i). Its physical primitive, in the normalized metric, is

    D_ij = u_i^T J e + beta
         = beta + r(u_i.e)/2
           + x(u_i1 e1-u_i2 e2)/2
           + y(u_i1 e2+u_i2 e1)/2.

It is affine in (x,y); its zero locus is a line, empty, or identically zero.

For a true adjacent-pole arrow g->h, put b=a_h-a_g and gamma=v_g(v_h-v_g). Its reciprocal primitive is

    Q_gh = a_g^T J^{-1} b + gamma.

Multiplication by the SAME positive d yields

    d Q_gh = gamma(r^2-x^2-y^2)/4 + r(a_g.b)/2
             + x(-a_g1 b1+a_g2 b2)/2
             - y(a_g1 b2+a_g2 b1)/2.                 (CIRCLE)

Its zero locus is a circle, a line, empty, or identically zero. When gamma>0, Q_gh>0 is the INSIDE of the corresponding disk, if nonempty. When gamma<0 it is the OUTSIDE; arbitrary convex averaging of metric witnesses therefore need not preserve positive reciprocal escapes. No claim that all reciprocal feasible sets are convex is made.

For the fixed stable root, a_S=0 and v_S=1, so

    Q_Sg = v_g-1 < 0

for all adjacent facets. Those k=degree(S) outgoing root primitives contribute NO interior zero curves. All other arrows use (CIRCLE), including height ties gamma=0. An identically zero primitive is retained as a fixed zero sign; it is not discarded as an absent mechanical constraint.

## 3. Convex simultaneous GLOBAL-root eligibility at a fixed foot

A sole strict U must be the unique global M-norm maximum among actual vertices. A sole strict S must be the unique global N-norm maximum among actual poles. These are necessary, not sufficient, because additional local maxima may remain.

The vertex-root inequalities for a prescribed U are

    tr[J(u_U u_U^T-u_i u_i^T)] + h_U^2-h_i^2 > 0   (i != U).

They are LINEAR halfspaces in the three entries of J.

The normalized polar-root norm is q_S^T N q_S=1. For every g!=S, unique global polar-root eligibility is exactly

    a_g^T J^{-1} a_g + v_g^2 < 1.

It first requires |v_g|<1. With delta_g=1-v_g^2>0, it is equivalent to

    J - a_g a_g^T/delta_g  is positive definite.    (ROOT-LMI)

Proof: conjugate by J^{-1/2}; I-ww^T is positive definite precisely when ||w||^2<1. Consequently the simultaneous global-U/global-S eligibility set at a fixed actual foot is the intersection of J>0, linear primal halfspaces, and the translated two-by-two SPD cones (ROOT-LMI). It is CONVEX in J, despite the nonlinear complete reciprocal escape problem.

The foot condition |v_g|<1 for all g!=S has a direct actual-body meaning:

    p in relint(S) and -p in int(P).

It is also sufficient for SOME metric with S the unique global polar norm maximum: choose J=t I with t sufficiently large. This does not imply that S is the sole local stable equilibrium. In particular a global-root-eligible metric or a nonempty convex root arena is not an own110 construction.

## 4. Root-radius disks and an exact at-most-three-pole threshold

For fixed f and each g!=S with delta_g>0, put

    L_g = ||a_g||^2/delta_g,
    c_g = ((a_g1^2-a_g2^2)/delta_g,
           2 a_g1 a_g2/delta_g).

Then ||c_g||=L_g. Within the slice, (ROOT-LMI) is equivalent to

    r > L_g,   ||(x,y)-c_g|| < r-L_g.              (ROOT-DISK)

This follows by substituting adj(J) in a_g^T adj(J)a_g<delta_g det(J) and completing the square. Each root disk is contained in the SPD disk ||(x,y)||<r and internally tangent to its boundary. If a_g=0, L_g=c_g=0 and it contributes just the SPD disk.

Therefore the minimum tangential trace for strict global polar-root eligibility is the exact threshold

    r_0(f) = min_z max_(g!=S) ( ||z-c_g||+L_g ).

Feasibility holds precisely for r>r_0(f); at r=r_0 at least one global norm tie remains. The minimum exists by coercivity. For strict feasibility, at least one nonzero tangential pole exists because the polar body is full-dimensional; the root disks force J>0. The convex root arena at a fixed r is their intersection, further cut by the primal root halfplanes.

An optimizer of this two-dimensional convex minimax problem is determined by at most THREE active poles. Here is an elementary justification and exact candidate prescription, so no unproved numerical optimization assertion is used.

If an optimizer z coincides with some active c_i, then its value is L_i and that single candidate can be tested against all remaining disks. Otherwise every active distance is differentiable. If zero were outside the convex hull of active unit vectors (z-c_i)/||z-c_i||, a separating direction would strictly decrease every active function and, for a sufficiently small step, the inactive ones would still be below the old maximum. Thus zero belongs to that convex hull. A minimal planar convex representation of zero uses two or three vectors: any four coefficients admit an affine dependence, allowing a coefficient to be removed. Two opposite vectors give the pair case. Three genuinely necessary vectors imply noncollinear active centers.

Single candidate: z=c_i, r=L_i, accepted only if every ||z-c_g||+L_g<=r.

Pair candidate: for d_ij=||c_i-c_j||>0,

    r = (L_i+L_j+d_ij)/2,
    z = c_i + ((r-L_i)/d_ij)(c_j-c_i).

Since d_ij>=|L_i-L_j|, the point lies on the segment. Test every remaining disk. Coincident centers reduce to the single case.

Triple candidate: for noncollinear centers c_i,c_j,c_k, solve the TWO linear equations

    w.(c_i-c_j)=L_i-L_j,
    w.(c_i-c_k)=L_i-L_k.

At a genuine three-active optimizer z=r w. The common boundary equation gives

    r = 2(L_i-w.c_i)/(1-||w||^2),   z=r w.

Only candidates with ||w||<1, r>=max(L_i,L_j,L_k), and all disk inequalities may be accepted. A genuine three-active optimum satisfies these conditions: it is not a single-center contact, hence r>L_i for its active centers, and the intersection point is strictly inside the SPD disk; equality on that disk would force all active centers to the same radial direction, contradicting noncollinearity. This also excludes a zero denominator in the genuine triple case.

The smallest feasible value from these finitely many candidates is r_0. At rational body/foot data, the single/triple candidates are rational and pair candidates use only a square root of a rational number. Testing the inequalities can be done by sign-aware squaring after checking r>=L_g. No generic high-degree polynomial is needed for this polar global-root threshold. Adding primal root halfspaces may require additional active constraints; the three-pole statement applies to r_0 itself, not to the full U/S eligibility optimization.

## 5. A finite exact solution of each physical two-dimensional slice

For fixed f,r, all mechanical signs are constant on open cells of the line/circle arrangement inside the SPD disk. Evaluate the original true-edge primitives or their exactly equal polynomial forms. Count strict U and S from all true outgoing arrows; count strict saddles and physical weak contacts from the full four-primitive true-edge packets. In particular a packet with maximum<0 is a strict saddle and maximum=0 is an edge/endpoint physical weak contact, with the usual physical deduplication of coincident endpoint contacts. Identically zero primitives remain in the packets.

A proper own110 metric, with no additional weak equilibrium, belongs to an OPEN metric set. This follows directly from strict outgoing inequalities at the two roots, a strict positive escape at each nonroot vertex and nonroot pole, and a strict positive primitive in every true-edge packet when H=0 and physicalweak000. Hence a proper110 metric in a fixed slice also has an open relative neighborhood in that slice. Even if it lies on harmless zero curves, that neighborhood contains a two-dimensional arrangement cell. Testing one point in EACH open cell is therefore enough to decide proper110 on the fixed slice. Weak-only witnesses cannot be promoted by this argument.

This yields an elementary exact sampling procedure for rational or real-algebraic fixed data. Compute curve intersections, circle x-extrema, vertical lines and the SPD-disk extrema. Isolate their x-coordinates; choose a rational x in each consecutive open interval. At that x, sort all curve heights and choose rational y values in the intervening intervals lying in the SPD disk. These vertical samples meet every two-dimensional cell. Pair intersections and extrema solve linear/quadratic equations; ordering and sample selection are exact real-algebraic operations. This procedure is not asserted to have been implemented by the companion identity-check program.

An explicit arrangement-cell upper bound incorporates the true reverse-arrow identity. Let E be the number of true edges and k the number of sides of S. There are at most L=2E primal lines and C=2E-k reciprocal curves (circle or line), excluding the root's k constant-negative outgoing primitives. Each curve meets the open SPD disk in at most one connected arc or one closed circle. Inserting a curve adds at most one plus its intersections with earlier curves to the number of regions. Distinct reverse primal arrows cannot both vanish inside SPD because their sum is -||X_i-X_j||_M^2<0; the same holds for reciprocal reverse arrows. There are E primal reverse pairs and E-k reciprocal reverse pairs among the retained curves. All other primal pairs meet at most once; a pair involving a reciprocal curve at most twice. Degenerate, tangent, empty or coincident curves cannot increase the bound (duplicates are treated as one curve). Thus the number of open cells is at most

    1 + (2E)+(2E-k)
      + [binom(2E,2)-E]
      + 2(2E)(2E-k)
      + 2[binom(2E-k,2)-(E-k)]
    = 14E^2-8Ek+k^2-2E+2k+1.

For E17, k>=3, this is at most 3620 cells. For a heptagonal stable facet it is at most 3124. These are analytical upper bounds per fixed (f,r), NOT an executed catalogue census. The remaining outer parameters are the two foot coordinates and r; their continuous coverage is still a real problem. Neither finitely many sampled feet/traces nor nonempty root disks resolve all metrics on a body.

## 6. Independent exact actual-body algebra controls (not a new exclusion)

The separate complete source common_metric_slice.py fixes the literal family of fully read minimum-0217 (SHA d855f740fcfc32469432ae2866c68ca98d0ad139ac857c8d7bd8c391897262d0) at epsilon=1 and transverse c=(1/5,-1/20,1/10). It reconstructs its TRUE 10/17/9 hull and NEW uniform-volume centroid with two positive fans. For each of nine stable-root charts it chooses a strict interior foot and three rational (r,x,y) values. All 27 physical M/N pairs satisfy MN=I exactly. All1836 true directed primal/reciprocal polynomial identities and all216 root-radius disk equivalences pass exactly. Full S/U/H and weak packets are reported for the controls; these checks are algebra/geometry controls, not a proof of any full-domain exclusion.

Execution used CPython3.13.5 with assertions, standard library only for build/check. Commands:

    python -B common_metric_slice.py build
    python -B common_metric_slice.py check

Expected markers:


[Encoded source block omitted; the code in this passage is incomplete.]

common_metric_slice.json:606110 bytes, SHA ca14bd96a6e4af63237744068c689c3ea9befe6ea7efe1ca6193e0e1d2145c62. Complete source is stored separately; this proof does not require rerunning its numerical locator. Source-only reconstruction, not this output hash alone, preserves the controls. No upper/lower bound is advanced by them.

## 7. What changed and what remains

The full reciprocal problem at a fixed stable foot has not become globally convex. Its GLOBAL-root necessary arena is convex and has explicit internally tangent disks. Its remaining TRUE nonroot signs are one exact circle arrangement at each tangential trace. This retains the common inverse rather than replacing it by a second feasibility variable, and retains full-rank components rather than assuming they reach a singular boundary.

Useful continuations include actual continuous foot/trace cell coverage, nonroot negative-height escape obstructions inside the root arena, and the interaction of these circles with the actual uniform-centroid/facet-area identities. No claim here closes the six-pole five-cube, the two-cap finite interior, another E17 incidence, or the minimum problem.
