# minimum-0262

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_W_ACTUAL_CHORD_AND_TANGENTIAL_GATE_V1

## 1. Findings and scope

The new result is an **actual-chord obstruction for the W-only problem**, followed by an exact elimination of all tangential SPD metrics and positive normal heights from a necessary top-maximizer escape test. Neither step assumes R7 or the stronger containment C.

For an actual W-and-A body with gamma≤1/3 and at most seven basal vertices, a joint S1/U1 metric must satisfy the following stronger conditions at every top norm-maximizer a and every genuine nonnegative spoke a→b:

    |(1-2gamma)Y_b+2gamma Y_a|_G² < tau_a(v)² |Y_a|_G²,
    tau_a(v)>1,
    2c-a_xy-(1-2gamma)v ∈ relint B,
    (tau_a(v)-1)|Y_a|_G² > (1-2gamma)(1-gamma)eta.

Here tau_a(v) is the **actual far endpoint of the basal chord through the physical basal foot in direction -Y_a**. It is determined by the actual shape and shear, independently of G and eta. Replacing tau_a(v) by its universal W bound 2gamma/(1-2gamma) recovers the weaker lens and normal inequality in the primary parent. Thus this is a strict geometric strengthening, not a relabeling of those inequalities. The parent W-only lens and its distinction from R7 remain the starting premises. fileciteturn34file0L206-L230

At a fixed actual shape and shear, each of the seven genuine top-to-base ports reduces to an **open interval in one rational scalar X**. Its nonemptiness is necessary and sufficient for the local conjunction of top-norm maximality, a positive-height spoke escape, and the strict actual-chord lens. Adding the actual-covariance normal consequence of the joint spectral floor adds one strictly positive concave quadratic on that interval. These decisions require no tangential-metric grid, numerical optimizer, or separately chosen polar metric.

This yields a new exclusion on an explicit, full-dimensional **shape-and-shear region** throughout the genuine W-and-A class below gamma=1/3, with every remaining G>0 and eta>0 allowed. A concrete unbounded shear region over the parent's actual W_ONLY_RESIDUAL shape is given in Section 5. It is outside the previously closed five-dimensional shape boxes, and contains an entire open set of physical metrics, not just one fixed G.

**This does not close the entire W-only shape projection.** In particular, it does not prove that every W-and-A H5 body is excluded for every shear. The global residual taper remains 1/300<lambda<3/5 outside the accepted exclusions. The central cube x,r,p,q∈[1/5,1/2] is already closed for the entire taper and is not a target of the new work. fileciteturn36file0L21-L47 No minimum bound, canonical registry count, or attaining construction changes.

### Execution and reading qualification

The retained continuation record contains the complete primary seven-turn parent and the complete central-cube parent. Their registered identities are:

    minimum-0255
    b02e9ea175553f06a5fc27b626e52977c8baf76d50df0e70d68eff5fb913393e

    minimum-0256
    9e71d008aa4b1d85333f293fd38dd05ab80a944563fa4e8fb4c5509dfcebb28e

There is a specific limitation in this resumed execution: attempts to inspect journal lines 1–267, and subsequent execution checks, returned no inspectable tool-response body. The retained reading record covers lines 268–2331/EOF, including both literal parents. I therefore do **not** claim that the entire latest journal was successfully inspected in this resumed pass. This is a response-access limitation, not a claim that the attached file itself is truncated. Its supplied manifest is 381054 bytes, SHA-256 `2976cb75124e14ba28a4de95a4886228b67f4e1e7285a5638a95496ca326df6e`.

The proof below is analytic. The exact extension unit in Section 8 reconstructs and audits the examples, but I received no inspectable successful execution result for it. Consequently this handoff does not promote a new execution-certified numerical record or invent output hashes. The last fully audited computational checkpoint remains the primary parent. The supplied exact inputs and verification unit preserve the additional probes for continuation.

## 2. Definitions: one actual body, one actual inverse

Let

    P=conv((B,0),(T,1)),   g=(c,gamma),   0<gamma≤1/3,

where B and T are full-dimensional planar convex polygons and B has n≤7 true vertices. In the H5 application, g is the actual uniform-volume centroid. A theorem at a specified reference does not license choosing a convenient false centroid for a homogeneous body.

Write

    H=1-gamma,   k=1-2gamma,   b0=2gamma.

The hypotheses are the parent's weak reflection and actual opposite-top pole condition:

    -k B_g-b0 T_g ⊂ B_g,                                      (W)
    q·a>-1 for every nonbasal true pole q and every a∈T_g.       (A)

All poles use P-g and the same origin, never the polar's own volume centroid.

For the physical metric write

    M=((G,Gv),(v^T G,v^T Gv+eta)),   G>0, eta>0,
    N=M^-1.

Define the actual basal foot and the sheared horizontal vectors by

    beta=c+gamma v,
    Y_i=Z_i,xy-c+(Z_i,z-gamma)v.

For a top vertex a, Y_a=a_xy-c+Hv. The physical realization can be taken as horizontal map C with C^T C=G and vertical scale sqrt(eta). Thus these are genuine coordinates of one physical body, not independent primal and dual normalizations.

W implies two strict conclusions already established in the parent and used here. First, a basal norm-maximizer is a strict U: a nonnegative derivative toward a top vertex would make its W-reflected point strictly farther away, contradicting maximality. Second, W and A force a nonbasal strict S under the same inverse. For completeness, if q is a largest nonbasal pole and mu=min_top q·a>-1, put

    delta=1-gamma+gamma mu,
    u=k/delta,   w=gamma(1+mu)/delta.

Then u,w>0, u+w=1, and -u q-w q_B lies in a top-vertex face of the actual polar, hence in the nonbasal polar hull. If q·(q_B-q)≥0 its norm would exceed |q|. Therefore q is a strict polar U and its primal facet is a strict nonbasal S. In original coordinates its foot is Nq/(q^T Nq).

Consequently a joint S1/U1 metric must have beta outside relint B. Otherwise the basal facet and the nonbasal facet supply two strict S. No weak-contact exclusion is being assumed.

## 3. Strict actual-chord theorem

Assume W and U=1, with beta not in relint B. Let a be any top norm-maximizer, and let a→b be any genuine spoke with nonnegative physical derivative. Such a spoke exists: a basal strict U already exists, while all same-layer derivatives at a top norm-maximizer are strictly negative.

### 3.1 The chord is shape-and-shear data, not tangential-metric data

Set A=Y_a. It is nonzero. Define

    I_a(v)={t≥0 : beta-tA ∈ B},
    tau=tau_a(v)=max I_a(v).

This chord can be computed exactly from the true basal supports. If n_e·x≤h_e is one such support, put

    f_e=n_e·beta-h_e,   e_e=n_e·A.

The corresponding constraint is f_e-e_e t≤0. Positive e_e gives a lower bound on t; negative e_e gives an upper bound. Hence tau is the minimum of the finite rational upper bounds f_e/e_e for e_e<0. Directions parallel to an edge retain their constant slack test; they are not divided by zero.

For fixed a the W map has the interior fixed point

    -[gamma/(1-gamma)]a

in centered physical coordinates. In raw basal coordinates this point is

    (c-gamma a_xy)/(1-gamma),

independent of the metric. It lies strictly inside the chord. Because beta is not interior, the entire chord is on the negative-A side of beta. Invariance under W yields

    0<tau≤r0:=2gamma/(1-2gamma)≤2.                              (1)

### 3.2 The actual lens must be strict

In physical horizontal coordinates rotate C A to (d,0), where d²=A^T G A. Let the physical end-plane separation be h=sqrt(eta). A nonnegative spoke a→b gives

    (C A)·(C Y_b) ≥ d²+(1-gamma)h²>d².

Thus b has first horizontal coordinate greater than d and is off the axial chord. Its W-reflected point has horizontal vector

    z=-k C Y_b-b0 C A.

It lies in the opposite open half-plane, with first coordinate strictly less than -d. In particular |z|>d.

Suppose |z|≥tau d. Maximize horizontal norm on that opposite closed half of the basal polygon. There is a maximizer off the separating chord. If equality with the chord maximum occurs, strict convexity of squared norm still ensures that the off-chord maximizer is a genuine basal vertex, rather than an interior point of a chord or an integration artifact.

This vertex has radius rho>d. Its same-layer derivatives are strictly negative by local maximality. Its derivative to any top vertex is at most

    rho d-rho²-gamma h²<0.

It is therefore a strict U, and under U1 it is the unique root in the opposite half-plane.

Follow genuine nonnegative escape edges from the selected a→b to that root. Squared physical norm increases strictly along every escape. After the first spoke, the path cannot return to a top vertex, because every top norm is at most the original norm of a. The remainder stays on the basal polygon. There are at most seven arrows in total.

Truncate at the first subsequent crossing of the axial line. The endpoint lies on its negative ray and has horizontal norm at most tau d≤2d. Every projected arrow is nonnegative, and the first is strictly positive because eta>0. For a planar chain u_0,...,u_m with these arrows,

    |u_0|/|u_m| ≤ product_j cos(theta_j),

with strict inequality here. Its endpoints are antipodal, so sum theta_j≥pi. Concavity of log cos and m≤7 give

    product_j cos(theta_j) ≤ cos(pi/7)^7<1/2.

Thus the endpoint norm is strictly greater than 2d, a contradiction. The exact seven-turn cosine bound is part of the primary parent's certified algebra.

Therefore

    |kY_b+b0Y_a|_G² < tau_a(v)² |Y_a|_G².                      (2)

The strict inequality matters: equality also produces the forbidden half-turn.

### 3.3 Two additional necessary consequences

The first coordinate of k C Y_b+b0 C A is greater than

    d+k(1-gamma)eta/d.

Combining this with (2) gives

    tau_a(v)>1,
    (tau_a(v)-1)|Y_a|_G² > k(1-gamma)eta.                      (3)

The chord's interior fixed point occurs at t=gamma/(1-gamma)≤1/2, while its far endpoint has t=tau>1. Hence the point at t=1 is strictly interior:

    beta-Y_a=2c-a_xy-kv ∈ relint B.                            (4)

Equations (2)–(4) are necessary for **every** top-maximizer escape in a putative U1 metric with non-interior basal foot. They use no spectral cap. Using only tau≤r0 in (3) gives the parent's weaker condition

    (4gamma-1)|Y_a|_G² > (1-gamma)k² eta.

The new obstruction uses the actual chord before making that lossy substitution.

## 4. Exact all-G and all-positive-height port elimination

Fix the actual shape and shear v, with beta not in relint B. Consider one genuine port a→b. Put A=Y_a and B1=Y_b.

If A and B1 are collinear, this port cannot be a top-maximizer escape: the basal axial chord is entirely on the negative-A side, so the physical cross derivative is negative. The zero-A case cannot be a top norm-maximizer of a genuine top polygon either.

Otherwise J=[A B1] is invertible. Normalize A^T G A=1 and write

    X=A^T G B1,   Y=B1^T G B1.

Tangential SPD is exactly Y>X². Express every other top vector as

    Y_j=u_j A+v_j B1.

The local requirements are:

    u_j²+2u_j v_j X+v_j²Y≤1,                                  (top maximum)
    X-1-(1-gamma)eta≥0,   eta>0,                              (true spoke)
    k²Y+2kb0X+b0²<tau².                                      (actual lens)

### Exact criterion

There exists G>0 and eta>0 satisfying this entire local packet if and only if the following open interval is nonempty:

    1<X<(tau-b0)/k,
    -1<u_j+v_j X<1 for every v_j≠0,                           (5)

and every constant row v_j=0 satisfies |u_j|≤1.

All coefficients are rational for rational shape and shear. Strictness of a variable top row follows from Y>X²; constant norm ties are retained rather than incorrectly rejected. A weak spoke at positive eta still requires X>1, so the endpoint X=1 is not feasible.

Necessity follows by substituting Y>X². For sufficiency, choose a rational X strictly inside the interval and choose epsilon>0 smaller than all the positive quantities

    1,
    [tau²-(kX+b0)²]/k²,
    [1-(u_j+v_jX)²]/v_j²  for v_j≠0.

Then use

    Gram=((1,X),(X,X²+epsilon)),
    G=J^-T Gram J^-1,
    eta=(X-1)/(2(1-gamma)).

This constructs one actual SPD M and its actual inverse. It does not assert U1 or S1: all other primal and polar rows remain to be audited.

### Optional joint-covariance strengthening

Let Sigma be the actual uniform covariance, c_z=Sigma_zz, and suppose the necessary joint spectral floor is

    Sigma^(1/2) M Sigma^(1/2) ≥ ell tr(Sigma M) I.

The safe closed floor from the supplied finite-height constants is

    ell=200000000000/11165771895407.

This is a joint S1/U1 premise, not an all-U1 restriction. Inverting the matrix inequality and using the actual N_zz=1/eta gives

    eta ≥ ell tr(Sigma M)/c_z.

Put

    C_v=Sigma_xy+Sigma_xy,z v^T+v Sigma_z,xy+c_z vv^T,
    T=J^-1 C_v J^-T.

Since tr(Sigma M)=tr(G C_v)+c_z eta, the necessary normal bound is

    eta ≥ ell tr(G C_v)/[c_z(1-ell)].

The local packet (5), augmented by this scalar consequence of the joint floor, is feasible exactly when its interval contains an X for which

    F(X)=c_z(1-ell)(X-1)
         -ell(1-gamma)(T11+2T12 X+T22 X²)>0.                 (6)

This is a strictly concave rational quadratic. Its maximum over the closed interval is attained at the clamped rational vertex; feasibility of the open interval is equivalent to that maximum being positive. Thus no irrational-root approximation is needed. A positive F permits an epsilon small enough to preserve all top and lens inequalities and a positive eta between its covariance lower bound and spoke upper bound.

Passing (6) verifies only this normal consequence, **not the full spectral matrix inequality**, and certainly not the remaining joint equilibrium system. Empty tests, however, are genuine exclusions of that port. If every genuine port is excluded, the actual shape/shear has no joint S1/U1 metric for any G or eta. This is an exact sufficient exclusion test, with a complete local feasibility calculation inside it.

## 5. Explicit actual W-only coverage beyond R7

Equation (4) immediately gives a metric-independent necessary shear region. Every joint W-and-A metric below gamma=1/3 must have

    v ∈ union_a (2c-a_xy-relint B)/k,                         (7)

with beta outside relint B and at least one top vertex in that union capable of being a norm-maximizer. This is not merely a compactness statement: outside the union the proof supplies two strict S or two strict U, and tests (5)–(6) remove additional portions inside it.

For H5, let xi=c-(1-gamma)v be the top foot and let y_max=max_{b∈B} b_y. The three inequalities

    xi_x<lambda/2,
    xi_y>lambda/2,
    xi_x+xi_y>lambda/2

make top vertex 9 strictly incapable of being a norm-maximizer under **any** G>0. Indeed its barycentric coefficient relative to the top foot strictly exceeds the sum of the absolute values of the other two coefficients, so Y9 lies strictly inside the symmetric convex hull of ±Y7 and ±Y8.

If additionally

    2c_y-kv_y>y_max,

then the necessary points (4) for top vertices 7 and 8 are outside B. Thus no top-maximizer escape can meet the actual-chord theorem. The following open region therefore excludes joint S1/U1 for every G>0 and eta>0:

    v_x > (c_x-lambda/2)/(1-gamma),
    v_y < (c_y-lambda/2)/(1-gamma),
    v_x+v_y < (c_x+c_y-lambda/2)/(1-gamma),
    v_y < (2c_y-y_max)/(1-2gamma).                            (8)

This region is unbounded and nonempty for every actual W-and-A H5 shape with gamma≤1/3. Reflections and different violated basal supports give further regions. Formula (8), together with the literal actual moment and W/A inequalities, is an explicit semialgebraic **shape-and-shear** domain; it is not an unevaluated small neighborhood or a fixed-G control.

### Actual parent shape

Take the parent's W_ONLY_RESIDUAL body:

    theta=(1/10,9/10,3/25,3/5,3/20),
    Vol=881291/9600000,
    c=(7368835529,3427883561)/28201312000,
    gamma=50317/153268.

It has strict W and A slacks but fails R7. Those are previously audited actual-centroid facts, not conclusions inferred from a failed coefficient search. fileciteturn34file0L189-L204 Here y_max=17/50, and the redundant upper bound on v_y can be removed from (8). The exact excluded wedge is

    v_x > 5253737129/18942984000,
    v_y < -1366339479/4842328000,
    v_x+v_y < 868162069/1894298400.                            (9)

In particular, the entire closed rectangle

    7/20≤v_x≤9/20,
    -9/20≤v_y≤-7/20

is excluded for every G>0 and every eta>0. On its subrectangle v_y≤-2/5 the basal foot has negative second coordinate; there the conclusion is actually U≥2 for every G and eta, without a covariance cap. Elsewhere the joint conclusion also allows the direct two-stable-facet alternative.

The parent's fully audited physical control uses

    M=((5,1,2),(1,3,-1),(2,-1,4)),
    N=((11,-6,-7),(-6,16,7),(-7,7,14))/35,
    v=(1/2,-1/2),   eta=5/2,

and has strict (S,U,H)=(2,6,6), weak points 0, and 68 nonzero primitives. Its shear lies in the unbounded wedge (9). The new result covers every G and eta over that shear, and an open set of neighboring shears, rather than merely retaining this one census.

Relative to the current named closures, this actual shape is outside the central cube, every seven-turn box, the asymmetric covariance-atlas box and its reflection, the all-taper macro/reflection, and the tiny off-macro tubes. Its lambda=3/20 is neither in the universal lower cutoff nor in lambda≥3/5. The new statement is nevertheless a restricted-shear exclusion on this shape, not a new all-metric exclusion of its whole affine orbit.

## 6. Reusable limitations and exact diagnostic inputs

### Testing all true cross pairs does not weaken a uniform reflection

A potentially misleading shortcut can be ruled out analytically. For fixed positive reflection coefficients, the vertices of the weighted Minkowski sum alpha B+beta T are attained at pairs of end vertices having a common exposing horizontal normal. Such pairs are precisely genuine cross-edge pairs of the prismatoid. Consequently checking a uniform reflection on all seven true H5 cross pairs is equivalent to checking it on all 21 basal/top pairs.

This can compress a certificate from 147 support tests to 49, but it does **not** enlarge its geometric scope. A genuine weakening must use a proper subset of ports justified by top-maximality, escape orientation, or another physical condition. The actual-chord gate does that without assuming that a passing local port is a complete U1 system.

### Probe 1: the old lens can pass while the actual chord forbids the port

On the same actual shape, set

    v=(2/5,-2/5),   eta=1/100,
    G(t)=diag(1,t),   7/50≤t≤4/25.

The complete physical metric is

    M(t)=((1,0,2/5),
          (0,t,-2t/5),
          (2/5,-2t/5,4/25+4t/25+1/100)).

The supplied checker verifies that top vertex 8 is the top norm-maximizer, that 8→1 is a positive true spoke, and that the parent's coarse lens and normal inequality pass. The actual chord has tau_8<1, so the strengthened gate rejects that port independently of G and eta. This family lies in the analytically excluded wedge (9).

The checker also reconstructs all physical primitives over the entire t interval. Primal rows are affine in t and positively scaled polar rows tE are affine in t, permitting exact endpoint sign certificates rather than sampling. No interval census from this new unit is being claimed as an observed execution result in this handoff.

### Probe 2: a passing exact local gate still does not supply a full U1 body

Again retain the same actual shape. Put

    p*=(1/10,13/50),
    v=(2c-(0,lambda)-p*)/(1-2gamma),
    A=Y9,   B1=Y3,   J=[A B1],
    Gram=((1,11/10),(11/10,73/50)),
    G=J^-T Gram J^-1,
    eta=1/[20(1-gamma)].

This is a completely specified rational physical metric with its actual inverse. The useful exact vectors are

    A=(5474537129,-2886041479)/9684656000,
    B1=(-1503828169,3660813959)/9684656000,
    A+B1=(41/100,2/25).

Its actual chord endpoint is

    tau_9=1+2227470880/28562868961.

The Gram determinant is 1/4. The local spoke is exactly

    D_93=1/20>0,

and the reflected horizontal squared norm, normalized by |A|_G²=1, is

    1+k/5+13k²/50 < tau_9².

The other two top norms are strictly less than one. Thus this input realizes the exact local gate, including the strict actual lens, rather than only an independently feasible arrow. It is a diagnostic for the remaining full-tree obstruction, not a claimed U1 or 110 construction.

The extension unit computes its complete same-inverse census and checks the six genuine outgoing derivatives at basal vertices 3 and 6. The intended nonattaining diagnostic is that both are strict U. Because I did not receive an inspectable execution result, I preserve the complete rational input and audit rather than assigning it an execution-certified census, output hash, or successor-record status. No part of the theorem in Sections 2–5 depends on this probe passing an unobserved test.

## 7. Remaining problem and useful continuation

The whole W-only implication is still unresolved. The sharper remaining search is now explicit: an actual shape/shear must have a non-interior basal foot and at least one genuine top-to-base port whose actual-chord interval (5) passes; a joint candidate must also survive the actual-covariance quadratic (6). A passing port still needs **one common metric** realizing all required primal and actual inverse-polar signs. Separate port witnesses must not be combined as though they used the same metric.

The structural gain is that the discarded geometry is now visible: the parent's radius 2gamma/(1-2gamma) was only a worst-case chord bound. The actual chord can already be shorter than the top radius, even while the coarse lens and normal inequalities pass. The finite seven-arrow half-turn makes that loss consequential and supplies strict root conclusions despite weak arrows.

A further complete W-only exclusion would need to close the surviving intervals using the remaining basal escape obligations or the nonroot polar constraints. The exact local witness construction above is useful for separating such a genuine obstruction from a failure of R7, from a fixed-G failure, or from an overly strong scalar covariance relaxation.

## 8. Exact recovery extension and verification status

The extension below uses the **literal reconstructible primary parent source**:

    h5_seven_turn_reflection.py
    18109 bytes
    SHA-256 125da77daa965228d1486bad45fdf6dce556a54e6269aa08c0242d9741170d97

Save that source from the primary parent under its displayed filename, and save the complete unit below as `h5_w_actual_chord.py` in the same directory. The parent is an explicit supplied dependency, not a missing archive. Its helpers retain the actual geometry, full moment integration, and physical weak-point census. The extension checks the parent bytes before importing it.

Dependencies are CPython compatible with the primary parent's 3.13.5 environment and SymPy 1.14.0. There is no numerical optimizer or random input. Run

    python -B h5_w_actual_chord.py

The unit writes `h5_w_actual_chord_report.json`, prints its own source and report byte counts and SHA-256 values, and finishes with

    H5_W_ACTUAL_CHORD_GATE_EXACT_PASS

**That marker is a verification target, not a marker observed in this resumed execution.** No new report hash or cold-replay claim is supplied. The report, when successfully generated, contains the actual support hull, moments, covariance, every metric and inverse, complete physical censuses, all local interval witnesses, the scalar-floor tests, and the exact affine primitive coefficients for Probe 1.

```python
#!/usr/bin/env python3
'''Exact extension of the supplied H5 seven-turn parent.
No numerical solver. A passing local gate is not a U1 or joint witness.
'''
import hashlib
import importlib.util
import itertools
import json
import sys
from pathlib import Path

BASE = Path(__file__).with_name('h5_seven_turn_reflection.py')
BASE_HASH = '125da77daa965228d1486bad45fdf6dce556a54e6269aa08c0242d9741170d97'
assert len(BASE.read_bytes()) == 18109
assert hashlib.sha256(BASE.read_bytes()).hexdigest() == BASE_HASH
spec = importlib.util.spec_from_file_location('h5_turn_parent', BASE)
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)
S, R = P.S, P.R
assert S.__version__ == '1.14.0'
THETA = tuple(map(R, ('1/10','9/10','3/25','3/5','3/20')))
ELL = R(200000000000,11165771895407)
assert ELL == 1/(R(7024915,10**6)*R(6832329,10**6)+R(6832329,10**6)+1)
PORTS = tuple((a,b) for a,b in P.ARROWS if a>=7 and b<7)
assert len(PORTS) == 7


def bil(a,M,b):
    return (a.T*M*b)[0]


def geometry():
    z = P.vertices(THETA)
    D,K,L,_ = P.moments(z)
    d2,k2,l2,cells = P.moments(z,7)
    assert D==d2 and K==k2 and L==l2 and len(cells)==9
    g=K/D
    assert D/6==R(881291,9600000)
    assert g==S.Matrix((R(7368835529,28201312000),
                        R(3427883561,28201312000),R(50317,153268)))
    C=(L/D-g*g.T).applyfunc(S.factor)
    P.pd(C)
    hull=set()
    for i,j,k in itertools.combinations(range(10),3):
        n=(z[j]-z[i]).cross(z[k]-z[i])
        if n==S.zeros(3,1):
            continue
        vals=[n.dot(a-z[i]) for a in z]
        if max(vals)<=0 or min(vals)>=0:
            hull.add(tuple(t for t in range(10) if vals[t]==0))
    assert hull=={tuple(sorted(f)) for f in P.FACETS}
    poles=[]; supports=[]
    for f in P.FACETS:
        a,b,c=(z[j] for j in f[:3])
        n=(b-a).cross(c-a); h=n.dot(a)
        slacks=[h-n.dot(t) for t in z]
        assert all(slacks[j]==0 if j in f else slacks[j]>0 for j in range(10))
        H=h-n.dot(g); assert H>0
        poles.append(n/H)
        supports.append({'normal':n,'offset':h,'slacks':slacks})
    base=[]
    for i in range(7):
        e=z[(i+1)%7][:2,0]-z[i][:2,0]
        n=S.Matrix((e[1],-e[0])); h=n.dot(z[i][:2,0])
        assert all(n.dot(a[:2,0])<=h for a in z[:7])
        base.append((n,h))
    ga=g[2]; k=1-2*ga
    assert R(1,4)<ga<R(1,3)
    W=[]
    for i in range(7):
        for j in range(7,10):
            point=2*g-k*z[i]-2*ga*z[j]
            assert point[2]==0
            W.extend(h-n.dot(point[:2,0]) for n,h in base)
    A=[1+q.dot(z[j]-g) for q in poles[1:] for j in range(7,10)]
    assert min(W)>0 and min(A)>0
    alpha=ga+R(1,4); beta=ga*(1+alpha)/(1-ga)
    rg=[]
    for i in range(7):
        for j in range(7,10):
            point=(1+alpha+beta)*g-alpha*z[i]-beta*z[j]
            rg.extend(h-n.dot(point[:2,0]) for n,h in base)
    assert min(rg)<0
    return {'z':z,'g':g,'Sigma':C,'D':D,'K':K,'L':L,
            'positive_apex_fan':cells,'poles':tuple(poles),'supports':supports,
            'base':base,'hull':sorted(hull),'minimum_W_slack':min(W),
            'minimum_A_slack':min(A),'minimum_R7_slack':min(rg)}


def horizontal(data,v):
    g=data['g']; v=S.Matrix(v)
    return tuple(a[:2,0]-g[:2,0]+(a[2]-g[2])*v for a in data['z'])


def basal_inside(data,v):
    g=data['g']; beta=g[:2,0]+g[2]*S.Matrix(v)
    return all(n.dot(beta)<h for n,h in data['base'])


def chord(data,v,A):
    g=data['g']; beta=g[:2,0]+g[2]*S.Matrix(v)
    lo=R(0); hi=None; guards=[]
    for n,h in data['base']:
        f=n.dot(beta)-h; e=n.dot(A)
        if e>0:
            lo=max(lo,f/e)
        elif e<0:
            hi=f/e if hi is None else min(hi,f/e)
        else:
            assert f<=0
        guards.append((f,e))
    assert hi is not None and lo<g[2]/(1-g[2])<hi
    assert hi<=2*g[2]/(1-2*g[2])<=2
    return hi,lo,guards


def metric(G,v,eta):
    v=S.Matrix(v); w=G*v
    M=G.row_join(w).col_join(w.T.row_join(S.Matrix([[bil(v,G,v)+eta]])))
    N=M.inv().applyfunc(S.factor)
    P.pd(M); P.pd(N)
    assert eta>0 and M*N==S.eye(3) and N[2,2]==1/eta
    return M,N


def physical(data,G,v,eta):
    M,N=metric(G,v,eta)
    cc=P.audit(data['z'],data['g'],data['poles'],M,N)
    return {'G':G,'v':S.Matrix(v),'eta':eta,'M':M,'N':N,'census':cc}


def gate(data,v,a,b,ell=R(0)):
    '''Complete LOCAL port test, optionally with the scalar normal-floor row.
    Never interpret a passing test as full U1 or S1/U1 feasibility.
    '''
    assert (a,b) in PORTS
    v=S.Matrix(v); g=data['g']; H=1-g[2]; k=1-2*g[2]; bb=2*g[2]
    out={'port':(a,b),'v':v,'ell':ell}
    if basal_inside(data,v):
        out['status']='BASE_STABLE_EXCLUDES_JOINT'
        return out
    Y=horizontal(data,v); A,B=Y[a],Y[b]
    J=S.Matrix.hstack(A,B)
    if J.det()==0:
        out.update(status='NO_LOCAL_PACKET',reason='collinear or zero top vector')
        return out
    Ji=J.inv(); tau,near,cguards=chord(data,v,A)
    lo=R(1); hi=(tau-bb)/k; coords=[]
    out.update(tau=tau,near=near,chord_guards=cguards)
    for j in range(7,10):
        u,w=Ji*Y[j]; coords.append((j,u,w))
        if w==0:
            if abs(u)>1:
                out.update(status='NO_LOCAL_PACKET',reason='constant top row')
                return out
        else:
            ends=sorted(((-1-u)/w,(1-u)/w))
            lo=max(lo,ends[0]); hi=min(hi,ends[1])
    out.update(open_interval=(lo,hi),top_coordinates=coords)
    if lo>=hi:
        out.update(status='NO_LOCAL_PACKET',reason='empty open interval')
        return out
    X=(lo+hi)/2
    floor=None; Cv=None
    if ell:
        C=data['Sigma']; cz=C[2,2]; bvec=C[:2,2]
        Cv=C[:2,:2]+bvec*v.T+v*bvec.T+cz*v*v.T
        T=Ji*Cv*Ji.T; P.pd(T)
        q2=-ell*H*T[1,1]
        q1=cz*(1-ell)-2*ell*H*T[0,1]
        q0=-cz*(1-ell)-ell*H*T[0,0]
        fun=lambda t:q2*t*t+q1*t+q0
        peak=max(lo,min(hi,-q1/(2*q2)))
        floor={'quadratic':(q2,q1,q0),'closed_interval_maximizer':peak,
               'maximum':fun(peak),'meaning':'scalar normal consequence only'}
        out['normal_floor_test']=floor
        if fun(peak)<=0:
            out.update(status='NO_LOCAL_PACKET',reason='normal-floor quadratic')
            return out
        while fun(X)<=0:
            X=(X+peak)/2
    limits=[R(1),(tau*tau-(k*X+bb)**2)/(k*k)]
    limits.extend((1-(u+w*X)**2)/(w*w) for j,u,w in coords if w!=0)
    if ell:
        limits.append(fun(X)/(ell*H*T[1,1]))
    assert min(limits)>0
    eps=min(limits)/2
    Gram=S.Matrix(((1,X),(X,X*X+eps)))
    G=(Ji.T*Gram*Ji).applyfunc(S.factor)
    upper=(X-1)/H
    lower=ell*S.trace(G*Cv)/(cz*(1-ell)) if ell else R(0)
    assert upper>lower>=0
    eta=(upper+lower)/2
    pp=physical(data,G,v,eta)
    assert bil(A,G,A)==1
    assert all(bil(Y[j],G,Y[j])<=1 for j in range(7,10))
    assert bil(k*B+bb*A,G,k*B+bb*A)<tau*tau
    assert bil(A,G,B-A)-H*eta>0
    if ell:
        assert eta>=ell*S.trace(data['Sigma']*pp['M'])/cz
    out.update(status='LOCAL_PACKET_FEASIBLE',X=X,epsilon=eps,witness=pp,
               scope='Full physical census is reported separately; this status asserts only the displayed local packet.')
    return out


def wedge(data):
    c=data['g'][:2,0]; ga=data['g'][2]; H=1-ga; k=1-2*ga; la=THETA[4]
    ymax=max(a[1] for a in data['z'][:7])
    lower_x=(c[0]-la/2)/H
    upper_y=min((c[1]-la/2)/H,(2*c[1]-ymax)/k)
    upper_sum=(c[0]+c[1]-la/2)/H
    assert ymax==R(17,50)
    assert lower_x==R(5253737129,18942984000)
    assert upper_y==-R(1366339479,4842328000)
    assert upper_sum==R(868162069,1894298400)
    corners=[]
    for vx,vy in itertools.product((R(7,20),R(9,20)),(-R(9,20),-R(7,20))):
        assert vx>lower_x and vy<upper_y and vx+vy<upper_sum
        v=S.Matrix((vx,vy)); xi=c-H*v
        assert xi[0]<la/2 and xi[1]>la/2 and sum(xi)>la/2
        assert 2*c[1]-k*vy>ymax
        corners.append((vx,vy))
    return {'lower_vx':lower_x,'upper_vy':upper_y,'upper_vsum':upper_sum,
            'strict_rectangle_corner_checks':corners,
            'scope':'All G>0 and eta>0; no fixed-G assumption.'}


def family_probe(data):
    t=S.symbols('t',positive=True)
    v=S.Matrix((R(2,5),-R(2,5))); eta=R(1,100)
    G=S.diag(1,t); M,N=metric(G,v,eta)
    Y=horizontal(data,v); A=Y[8]; B=Y[1]
    ga=data['g'][2]; H=1-ga; k=1-2*ga; bb=2*ga
    tau,near,cg=chord(data,v,A); assert tau<1
    d2=bil(A,G,A); ref=bil(k*B+bb*A,G,k*B+bb*A)
    guards={'spoke81':bil(A,G,B-A)-H*eta,
            'old_lens':(bb/k)**2*d2-ref,
            'old_normal':(4*ga-1)*d2-H*k*k*eta,
            'actual_lens_failure':ref-tau*tau*d2}
    for j in (7,9):guards['top_maximum_'+str(j)]=d2-bil(Y[j],G,Y[j])
    ends=(R(7,50),R(4,25))
    for f in guards.values():
        assert S.diff(S.cancel(f),t,2)==0
        assert all(f.subs(t,e)>0 for e in ends)
    X3=tuple(a-data['g'] for a in data['z']); rows=[]
    for i,j in P.ARROWS:
        f=S.cancel(bil(X3[i],M,X3[j]-X3[i]))
        assert S.diff(f,t,2)==0
        vals=tuple(f.subs(t,e) for e in ends)
        assert vals[0]*vals[1]>0
        rows.append({'side':'primal','arrow':(i,j),'positive_scale':1,
                     'affine_coefficients':(f.subs(t,0),S.diff(f,t)),
                     'endpoint_values':vals})
    for i,j in P.DUAL:
        f=S.cancel(t*bil(data['poles'][i],N,data['poles'][j]-data['poles'][i]))
        assert S.diff(f,t,2)==0
        vals=tuple(f.subs(t,e) for e in ends)
        assert vals[0]*vals[1]>0
        rows.append({'side':'polar','arrow':(i,j),'positive_scale':'t',
                     'affine_coefficients':(f.subs(t,0),S.diff(f,t)),
                     'endpoint_values':vals})
    portraits=[physical(data,S.diag(1,e),v,eta) for e in (ends[0],R(3,20),ends[1])]
    assert all(not c['census']['weak'] and c['census']['zero_primitives']==0 for c in portraits)
    assert all(c['census']['counts']==portraits[0]['census']['counts'] for c in portraits)
    return {'parameter_interval':ends,'v':v,'eta':eta,'tau':tau,
            'guards':guards,'all_68_affine_primitive_certificates':rows,
            'physical_portraits':portraits}


def passing_probe(data):
    g=data['g']; c=g[:2,0]; ga=g[2]; H=1-ga; k=1-2*ga
    point=S.Matrix((R(1,10),R(13,50)))
    a_raw=S.Matrix((0,THETA[4])); v=(2*c-a_raw-point)/k
    Y=horizontal(data,v); A,B=Y[9],Y[3]
    assert A==S.Matrix((5474537129,-2886041479))/9684656000
    assert B==S.Matrix((-1503828169,3660813959))/9684656000
    J=S.Matrix.hstack(A,B); Ji=J.inv()
    Gram=S.Matrix(((1,R(11,10)),(R(11,10),R(73,50))))
    assert Gram.det()==R(1,4)
    G=(Ji.T*Gram*Ji).applyfunc(S.factor); eta=1/(20*H)
    tau,near,guards=chord(data,v,A)
    assert tau==1+R(2227470880,28562868961)
    assert not basal_inside(data,v)
    assert bil(A,G,A)==1 and bil(A,G,B-A)-H*eta==R(1,20)
    assert all(bil(Y[j],G,Y[j])<1 for j in (7,8))
    reflected=bil(k*B+2*ga*A,G,k*B+2*ga*A)
    assert reflected==1+k/5+13*k*k/50 and reflected<tau*tau
    pp=physical(data,G,v,eta)
    # This is the diagnostic distinction from a complete U1 witness.
    for root in (3,6):
        assert all(d<0 for i,j,d in pp['census']['primal'] if i==root)
    pp.update(tau=tau,reflected_squared_norm=reflected,chosen_basal_point=point,
              local_gate=gate(data,v,9,3),
              scalar_floor_gate=gate(data,v,9,3,ELL))
    return pp


def main():
    data=geometry()
    assert P.algebra_and_turning()['half_minus_cosine_upper_seventh_power']>0
    w=wedge(data)
    parent_metric=S.Matrix(((5,1,2),(1,3,-1),(2,-1,4)))
    parent_inverse=S.Matrix(((11,-6,-7),(-6,16,7),(-7,7,14)))/35
    assert parent_metric*parent_inverse==S.eye(3)
    parent_census=P.audit(data['z'],data['g'],data['poles'],parent_metric,parent_inverse)
    assert parent_census['counts']==(2,6,6)
    assert not parent_census['weak'] and parent_census['zero_primitives']==0
    tests=[]
    for v in (S.Matrix((R(2,5),-R(2,5))),S.Matrix((R(1,2),-R(1,2)))):
        rows=[gate(data,v,a,b) for a,b in PORTS]
        assert all(row['status']=='NO_LOCAL_PACKET' for row in rows)
        tests.append(rows)
    report={'identity':'H5_W_ACTUAL_CHORD_AND_TANGENTIAL_GATE_V1',
            'environment':{'python':sys.version.split()[0],'sympy':S.__version__},
            'parent_source_sha256':BASE_HASH,'theta':THETA,
            'geometry':data,'wedge':w,'parent_metric':parent_metric,
            'parent_inverse':parent_inverse,'parent_census':parent_census,
            'all_port_rejections':tests,'coarse_lens_family':family_probe(data),
            'passing_local_probe':passing_probe(data),
            'scope':'Actual-chord necessary conditions and complete local gate. No full W-only shape-projection exclusion or U1 construction is asserted.',
            'status':'EXACT_PASS'}
    raw=(json.dumps(P.enc(report),sort_keys=True,indent=2)+'\n').encode()
    out=Path('h5_w_actual_chord_report.json'); out.write_bytes(raw)
    src=Path(__file__).read_bytes()
    print(Path(__file__).name,len(src),hashlib.sha256(src).hexdigest())
    print(out.name,len(raw),hashlib.sha256(raw).hexdigest())
    print('H5_W_ACTUAL_CHORD_GATE_EXACT_PASS')


if __name__=='__main__':
    main()
```
