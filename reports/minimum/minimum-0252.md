# minimum-0252

Historical AI scientific report · saved 2026-09-26 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# H5_APEX_CLUSTER_JOINT_EXCLUSION_V1

## 1. New result and its exact scope

**Every genuine, uniformly filled member of the literal H5 family with 0 < lambda <= 1/400000 is excluded from proper110, for every physical SPD metric. All four basal parameters are free over their entire admissible domain.**

The proof is genuinely joint. It does not establish U >= 2 for every arbitrary metric. Instead, in a covariance-weighted metric cone containing every joint S1/U1 candidate, it proves three assertions:

1. There is a strict unstable basal vertex.
2. There is a strict stable facet other than the basal facet.
3. If U = 1, the basal facet is itself strictly stable.

Consequently U = 1 implies S >= 2 in that cone. No contraction to eta = 0 is used. The actual inverse of the same metric is essential in the second assertion.

In the original block chart M = [[G,Gv],[v^T G,v^T Gv+eta]], assertion 3 is the concrete shear restriction

    U = 1  =>  g_xy + g_z v belongs to relint((1-lambda) B).

This is proved on the stated small-taper domain, not asserted on all H5. The simultaneous nonbasal stable facet makes that necessary basal foot incompatible with S = 1.

The excluded domain is five-dimensional, not a neighborhood of one basal shape. For example, its endpoint shape (x,r,p,q,lambda) = (4/5,9/10,1/3,1/2,1/400000) is outside both supplied all-taper macros and the off-macro tube. Combining this result with the accepted full-basal lambda >= 3/5 exclusion leaves

    1/400000 < lambda < 3/5

as the remaining taper interval, still outside the other accepted exclusions. No whole-H5, whole-incidence, registry-count, or minimum-bound conclusion follows. The accepted interval remains 34 <= C_min <= 622. The starting exclusion map and bounds are recorded in the supplied memory. fileciteturn0file4L910-L919

The argument produces strict equilibria and tolerates incidental weak contacts. In particular, it also excludes a body with exactly one strict S and one strict U plus additional weak rests: such a body supplies the nonnegative primal and polar escape trees used below. No claim of existence of an all-U1 metric outside the joint cone is made.

## 2. Reading, source identity, and limitations

I read the entire supplied journal, including its branch memory and the complete literal parent through EOF, and all four standalone source files. The initially truncated journal display was continued consecutively through its final line 1723. All five mounted files matched the supplied byte counts and SHA-256 values:

| Supplied file | Bytes | SHA-256 |
|---|---:|---|
| H5_JOINT110_UNIFORM_METRIC_COMPACTNESS_V1_proof.md | 13378 | bc036d025d06467cacaaad0ae5ff7b57daecdb49320e098b328a8e1f89f7f20e |
| h5_joint_compact.py.txt | 8897 | 18d44bfc27e0e4830a36c071cb90da9320e65659c5db4d46e15fdcdd5ccf1e18 |
| FINITE_HEIGHT_RECIPROCAL_DOMAIN_V1.md | 10171 | e7daf31f7dddffac638b3bb0d7005af5613e4b2473b0979daff4357ebf5894db |
| COVARIANCE_NINE_RATIO_AND_PHYSICAL_CONTAINER_V1.md | 11958 | e43bdb2b1745cf265601df70863e60face5ee25d5ebc4e36d120c8d361bed173 |
| research-journal(20260926-193217).md | 330628 | e9e788bf2712733d7b132aee6d15fa15606b3cab60515a55c8e8edc481eb0486 |

The parent is the embedded minimum-0250, registered SHA-256 2cf87f1bc07e373e4dd87a52a48d1a91b98eb48ba17601cf28e76afe3e39c233. Its three extracted Python sources matched their literal source pins: h5_normal_cone.py, 11669 bytes, 3ee5d85e8d3489286a3afbe3704f25250849036ec79328b759d4aae68a0a7f76; h5_taper_atlas.py, 5309 bytes, ef1abbd36b9d78c35aed1cf2e2adb5f34788fa2d689990688eccbe05703cee10; h5_verify_taper.py, 6488 bytes, a50817ce6f03a99fabc54085f477d87282f55aa2c23d7a8b917e1db75e6bffd6.

There is a byte-representation qualification: hashing the parent Markdown literally from its H5 title through journal EOF gives 42922 bytes and 449496fe9e89d6d1839526b35c5b553d58abf8dd065368f047cb871901ab3c96, not the registered parent digest. I do not infer the unavailable original hashed envelope from that difference. The literal geometry and all three code pins agree, and no semantic/incidence conflict was found. The older covariance bibliographic digest inside the finite-height source is likewise not the digest of the supplied current covariance bytes, as already noted in the compactness proof. fileciteturn0file0L23-L29

No unprovided archive, parent output certificate, or research connector was used. Historical exclusions are working premises, not newly replayed results. The new proof and source below need no additional exact dependency.

## 3. The actual body and the physical normalization

Put s = 1-lambda and

    B = conv((1/4,0), (1-3x/4,0), (1-p,p), (q,1-q),
             (0,1-3r/4), (0,1/4), (1/16,1/16)),
    P = conv((sB,0), ((0,0),1), ((lambda,0),1), ((0,lambda),1)),

where 0 < x,r < 1, p,q > 0, p+q < 1. The nine true facet cycles and seventeen true edges are those in the supplied literal geometry and are repeated in the complete code. fileciteturn0file0L31-L40

Suppose, for contradiction, that one physical M > 0 gives S = U = 1. Let Sigma be the actual uniform-volume covariance. The supplied finite-height theorem bounds the adjacent eigenvalue ratios of H = Sigma^(1/2) M Sigma^(1/2) by

    p0 = 7024915/1000000,  q0 = 6832329/1000000,

both strictly smaller than kappa = 281/40. The polar tree uses M^(-1) at the same origin. fileciteturn0file2L36-L53

This step does not require rejecting harmless or physical weak zeros. At every vertex other than the unique strict U, some true-edge derivative is nonnegative. A nonnegative arrow strictly increases squared M-norm, so choosing one per nonroot yields a rooted tree. Apply the identical reasoning to the actual same-origin polar and its unique strict U, which is the primal strict S. Thus the finite-height tree hypotheses hold even in the presence of additional weak rests.

Scale M so tr(Sigma M) = 1, apply its actual physical linear map L with L^T L = M, and then use a rigid motion to make the two end planes horizontal. This is not a whitening followed by a metric reset. The covariance of the physical body has the eigenvalues of H and trace one. The two adjacent ratio bounds give

    lambda_min(H) > 1600/91801,
    lambda_max(H) < 78961/91801.

The supplied actual covariance sandwich then implies, for the physical body centered at its actual centroid,

    (1/6) Ball is contained in P-g, and P-g is contained in (18/5) Ball.       (1)

Indeed 8000/275403 > 1/36 and 1184415/91801 < 324/25. The covariance sandwich concerns actual volume, not vertex averages. fileciteturn0file3L9-L20

The proof below in fact works for every M whose two covariance-weighted adjacent ratios are at most 281/40. It is this closed metric cone, containing all joint candidates, that is excluded. The unrestricted all-U1 cone is not constrained this way.

## 4. Two actual geometric estimates: the new anchor and the true centroid drift

Let Q be the actual uniformly filled pyramid obtained by retaining the same scaled basal polygon and just top vertex 7:

    Q = conv((sB,0),(0,0,1)).

Write g_Q for its own uniform centroid. Q is an auxiliary comparison body, not a replacement for P's centroid. In physical coordinates put

    delta = |g-g_Q|,    t = max_j |a_j-a_7|,    j in {7,8,9}.

I claim, throughout 0 < lambda <= 1/400000,

    delta < 17 lambda,    t < 43 lambda.                                  (2)

### 4.1 A larger fixed basal diamond

Besides the three fixed anchors already used by the coordinator, every B contains (1/5,1/5). The exact convex combination is

    (1/5,1/5) = (4p/5)(1/4,0)
                 + (4(1-p)/5)(0,1/4)
                 + (1/5)(1-p,p).

Thus B contains the diamond with vertices (1/4,0), (1/5,1/5), (0,1/4), (1/16,1/16). This elementary additional anchor is useful independently of the exclusion.

Let C be the physical horizontal linear map. The differences between the two axis anchors and between the two diagonal anchors are orthogonal. Since the physical diameter is at most 36/5 by (1),

    ||C||_op^2 <= ||C||_F^2 <= 5401728/[3025 s^2] < 43^2.

Consequently both top offsets have physical length less than 43 lambda.

### 4.2 Actual added volume, not a transported old centroid

The actual six-volume is

    D = lambda + 2 A s^2,    A = (31-24xp-24rq)/64 >= 7/64,

whereas Q has six-volume D0 = 2 A s^2. Thus the actual added volume P minus Q is lambda/6 before the common physical linear map. These are the literal actual moment formulas, independently checked in the source. fileciteturn0file1L65-L81

At g = 0 let c_add be the centroid of the actual added region. The exact balance is

    D0 g_Q + lambda c_add = 0.

The added-region centroid is in P, so |c_add| <= 18/5. Hence

    delta <= (18/5) lambda/D0
          <= [576/(35 s^2)] lambda
          < 17 lambda.

This is sharper than a diameter-only centroid perturbation estimate and explicitly uses the same actual filled body.

## 5. A quantitative primal implication: U1 forces the basal foot inside

The following argument uses physical Euclidean coordinates after the one physical map. Set R = 18/5 and r_ball = 1/6.

Translate the basal area centroid to the horizontal origin. Let the actual centroid have horizontal foot e and height k; let h be the total height and H = h-k. By (1), k,H >= r_ball. Set d = |e|. The comparison pyramid has centroid at one quarter of its apex vector. Therefore every actual centered top vertex has the form

    (3e+w_j,H),    |w_j| <= W := 4 delta+t < 111 lambda.

A centered basal point is (b-e,-k). Also |b-e| <= R and d <= R.

### 5.1 The basal reflection and an unavoidable basal U

For a planar convex body B0 centered at its area centroid, -B0/2 is contained in B0. A short proof: in any direction, fan from a minimizing vertex of height -a. Every triangle's other two vertex heights are at most the support height b, so its mean height is at most (-a+2b)/3. The actual area mean is zero, hence a <= 2b. Apply this in every support direction.

Choose a basal vertex maximizing |b-e|. Its reflected point -b/2 is in the base and cannot have greater distance from e. With e = (d,0), this implies

    3 e dot (b-e) - |b-e|^2 <= 0.                                         (3)

For completeness, put z = b-e and rho = |z|. If rho >= 3d, (3) follows by Cauchy-Schwarz. If rho <= 3d, the reflection comparison gives

    3 e dot z - rho^2 <= (rho^2-9d^2)/2 <= 0.

Thus its derivative to every top vertex is at most

    -kh + R W < -1/18 + (18/5)111 lambda < -1/20.                         (4)

Its derivatives to other basal vertices are strictly negative by maximality and the positive edge length. It is a true strict U of P. This remains valid at norm ties and with unrelated weak contacts.

### 5.2 If the basal foot is not interior, U cannot equal one

Assume U = 1. The strict U just found is basal. Choose a top vertex of maximum norm among the top vertices. Its same-layer derivatives are strictly negative. Since it is not U, it has a nonnegative true cross-edge derivative to some basal vertex b.

For its w = w_j, direct expansion gives

    D_top,b = 3 e dot b - 12d^2 - Hh
              + w dot (b-7e) - |w|^2.

Consequently

    3 e dot b >= 12d^2 + E,
    E := Hh - 7R W > 1/18 - (126/5)111 lambda > 1/25.                     (5)

Suppose e is not in the relative interior of the base. Since its area centroid is interior, d > 0. On the line through 0 and e, the positive basal endpoint is at most d; half-reflection puts the negative endpoint no farther than 2d. The entire basal chord therefore has distance at most 3d from e.

Take the e-direction as the x-axis. Equation (5) gives

    b_x >= 4d + E/(3d).

Both b and -b/2 lie off that chord, on opposite sides of its line. Their squared distances from e exceed 9d^2+E. Maximize distance separately on the two closed halves of the base. Both maximizers are off the separating chord and hence are genuine basal vertices. Their true basal derivatives are strictly negative. Their radii exceed 3d, so the Cauchy-Schwarz branch of (3), together with (4), makes every top derivative strictly negative as well. They are two distinct strict unstable vertices, contradicting U = 1.

Therefore the basal foot must be interior. In the original metric coordinates this is exactly g_xy+g_z v in relint(sB), so the basal facet is strictly stable.

## 6. The same-inverse polar argument forces another strict S

It remains to prove a strict stable facet other than the base without assuming the base is stable. All poles in this section use the actual corresponding reference and the same inverse physical metric; in physical coordinates that metric is Euclidean.

### 6.1 A reusable approximate-maximizer lemma

Consider a pyramid with a planar base C, apex a, and reference one quarter of the way from a half-reflection center c of C to a. Assume c-(C-c)/2 is contained in C. Let h_* be its height. If s is in C and its reflected point s' satisfies

    |s'|^2 - |s|^2 <= E0,

then

    s dot (a-s) <= -h_*^2/4 + 2 E0.                                    (6)

To verify it, use base coordinates centered at c, apex horizontal coordinate 4d, and reference horizontal coordinate d. Put rho^2 = (x-d)^2+y^2 and rho_ref^2 = (-x/2-d)^2+y^2/4. The exact identity is

    3d(x-d)-rho^2-h_*^2/4
      = (rho^2-9d^2)/2-h_*^2/4-2(rho^2-rho_ref^2).

For rho <= 3d apply the assumed reflection gap. For rho >= 3d use Cauchy-Schwarz instead. This proves (6) for all points, not only vertices.

### 6.2 The polar of the actual comparison pyramid

Center Q at its own actual g_Q. Its polar is conv(b0,S), where b0 is the basal pole and S is the side-pole polygon. If A is Q's centered apex, then

    A dot s = 1 for s in S,    A dot b0 = -3.

S has half-reflection center b_* = -b0/3. This does not assert that S has area centroid b_* or that Q's polar has volume centroid zero.

An explicit verification is available. With the original basal area centroid at 0, uncentered apex (a_H,h), and u in the planar polar of the base,

    s(u) = (4u/3, 4(1-a_H dot u)/(3h)),
    b_* = (0,0,4/(3h)),    b0 = -3 b_*.

The planar half-reflection transfers to its polar and hence to S. Its normal height as the base of Q's polar is 4/|A|. Thus (6) has the term -4/|A|^2.

The centered P and Q have Hausdorff distance at most delta+t < 60 lambda. Therefore Q has inradius greater than 10/61 and circumradius less than 73/20. All its poles have norm at most 61/10, and

    4/|A|^2 > 3/10.                                                     (7)

The corresponding bounds for P are pole norm at most 6 and vertex norm at most 18/5.

### 6.3 Compare the entire nonbasal polar hull, not individual frozen facets

Let C_P be the convex hull of all nonbasal poles of P. Every nonbasal facet contains a top vertex. Let Delta = g-g_Q, so |Delta| = delta. The top offsets t_j are measured from the retained apex a_7 and include t_7 = 0.

For any nonbasal pole q of P, set

    r_q = q/(1+q dot Delta).

Then r_q belongs to Q's polar. If q's facet contains top vertex j,

    1-A dot r_q = (q dot t_j)/(1+q dot Delta) >= 0.

Write r_q = (1-alpha)s+alpha b0 with s in S. The coefficient is alpha = (1-A dot r_q)/4. The preceding bounds give

    |q-r_q| < 614 lambda,    alpha < 65 lambda,
    |q-s| < 1450 lambda.                                                (8)

Conversely, for every s in S put

    mu_s = max_j s dot t_j >= 0,
    q_s = s/(1-s dot Delta+mu_s).

This point belongs to C_P: it is on a polar face corresponding to a top vertex attaining mu_s, and that polar face has no basal pole. Its displacement obeys

    |q_s-s| < 2250 lambda.                                              (9)

The actual basal pole q_B of P also satisfies

    |q_B-b0| < 623 lambda.                                              (10)

These comparisons explicitly keep the actual centroid change. No independently recentered polar, fixed supporting plane, or old-centroid census is substituted.

Choose a nonbasal pole q of P of maximum norm. Associate s using (8), reflect s to s' in S, and map s' to q_s' using (9). Since q_s' is in C_P, |q_s'| <= |q|. Hence

    |s'|^2-|s|^2 <= (6+61/10)(1450+2250) lambda
                  = 44770 lambda.

Apply (6)-(7), then transfer its derivative using (8)-(10). The transfer error is at most

    (6+2(61/10))1450 lambda + 6(623)lambda = 30128 lambda.

It follows that

    q dot (q_B-q)
       < -3/10 + (2(44770)+30128)lambda
       = -3/10 + 119668 lambda
       <= -83/100000 < 0.                                              (11)

All derivatives from q to other nonbasal poles are strictly negative by its norm maximality and their distinctness. Therefore q is a strict unstable vertex of the actual polar. Its primal facet is a strict S and is not the basal facet.

Combining this with Section 5, a putative U1 metric in the joint cone has both the basal strict S and a nonbasal strict S. This proves the new exclusion.

## 7. Exact controls, performed checks, and what was not proved

Two new actual controls use the same endpoint theta = (4/5,9/10,1/3,1/2,1/400000). Their raw actual volume and centroid are

    V = 11040008800069/153600000000000,
    g_x = 337556440056590538299/1413121126408832000000,
    g_y = 255210109389787871159/1413121126408832000000,
    g_z = 11040072800229/44160035200276.

The comparison pyramid has volume 3679981600023/51200000000000 and centroid

    (2109728059/8832000000, 1595062679/8832000000, 1/4).

For the first control M_raw = Sigma^(-1). For the second,

    M_raw = (1/1000000) *
      [[ 508511640, -261705386, -171632506],
       [-261705386,  668094787,  738335803],
       [-171632506,  738335803, 1038663123]].

In each case M = M_raw/tr(Sigma M_raw) and N = M^(-1), computed exactly. The second control's unnormalized covariance-weighted eigenvalues are certified, without floating eigenvalues, to lie respectively in (99/100,101/100), (599/100,601/100), and (3599/100,3601/100). Both adjacent ratios are therefore strictly below 281/40.

| Control | Strict (S,U,H) | Strict stable facets | Strict unstable vertices | Physical weak points | Zero primitives |
|---|---|---|---|---:|---:|
| COVARIANCE_ISOTROPIC | (7,8,13) | 0,2,3,4,5,7,8 | 1,2,3,4,6,7,8,9 | 0 | 0 |
| BASE_NOT_STABLE | (2,2,2) | 1,5 | 1,9 | 0 | 0 |

The second control's saddles are true edges (2,8) and (4,9). It confirms that the proof does not assume the basal foot is always interior. Neither control is U1 or proper110. The complete source reconstructs every coordinate, actual covariance, true support, M/N, all 68 true-edge primitives, all facet feet, physical weak-point deduplication, and the auxiliary polar reflection comparisons.

The exact checker verifies the new anchor, the reflection identity, the top-exit expansion, the polar pyramid formula, every rational constant above, and the actual controls. I executed it normally and in a fresh directory containing only the source; the reports were byte-identical. The written universal proof is not claimed to have been proof-assistant formalized. The finite-height and covariance theorems are accepted supplied inputs, not newly replayed research.

The route that succeeded was a quantitative apex-cluster comparison, not a fixed-G census or an unrestricted U1 search. Direct numerical exploration did not yield an exactly verifiable U1 or 110 body; no exclusion or numerical optimum is inferred from that failure. The exact control matrices above, rather than any floating search state, are the retained objects.

## 8. Reusable general criterion and continuation

The proof supplies a scale-covariant criterion for other parallel prismatoids. For P = conv(B,{a+t_j}), t_0 = 0, let Q = conv(B,a) be the actual homogeneous comparison pyramid. At the actual physical reference let r,R bound the centered inradius/circumradius, delta = |g-g_Q|, t = max|t_j|, and W = 4delta+t. Put

    L = 1/r,   L0 = 1/(r-delta-t),
    zeta = [L^2 delta + (L L0 t)/2]/(1-L delta),
    zeta_prime = L0^2(delta+t)/(1-L0 delta),
    zeta_base = L L0 delta,
    Epol = 2(L+L0)(zeta+zeta_prime)
           + (L+2L0)zeta + L zeta_base.

Require all displayed denominators positive. Then

    7 R W < 2 r^2,    Epol < 4/(R+delta)^2

imply U1 => S >= 2 by the same proof. The criterion is expressed in one physical metric and its actual inverse. It is neither a separately centered polar condition nor an all-U1 compactness assumption.

The most useful continuation is to combine this moving, body-specific delta/t criterion with the supplied regression ellipsoid and finite-height metric cone on the remaining 1/400000 < lambda < 3/5 region. The uniform constants deliberately sacrifice sharpness to cover every basal shape. A larger certified taper cutoff requires improved uniform or cellwise bounds, not extrapolation of the present constants. No conclusion is drawn from failure of this sufficient test.

## 9. Complete recovery capsule

Save the following source exactly as h5_apex_cluster_joint.py, including its final LF. It is self-contained; it does not import the parent sources or read a saved certificate. Dependencies are CPython 3.13.5 and SymPy 1.14.0; no random seed, numerical solver, or additional input is used in reconstruction or acceptance.

    python -B h5_apex_cluster_joint.py

Expected source pin:

    h5_apex_cluster_joint.py
    11918 bytes
    d956d2609f5406319a1dbd6e7ecd88ac411d0b606d36fd39a75ba68ca97115c2

Expected output pin:

    h5_apex_cluster_joint_report.json
    57886 bytes
    ae8bc21e11a6ed9a19eceb6a6240d56074b2dcf15e32ee9b7db696d81993bc44

Expected stdout, including final LF: 233 bytes, SHA-256 7db0a5afd54cfdc6f5ac469253dda794322ac3c2bebe9f92c6665e470c433def. Its final marker is H5_APEX_CLUSTER_JOINT_EXCLUSION_V1_PASS; the two census lines are COVARIANCE_ISOTROPIC (7, 8, 13) WEAK 0 ZEROS 0 and BASE_NOT_STABLE (2, 2, 2) WEAK 0 ZEROS 0.

Convenience copies supplement, but are not required by, the complete source below: [source](sandbox:/mnt/data/h5_apex_cluster_joint.py) and [exact report](sandbox:/mnt/data/h5_apex_cluster_joint_report.json).

```python
#!/usr/bin/env python3
"""H5_APEX_CLUSTER_JOINT_EXCLUSION_V1: exact constants and actual controls.
CPython 3.13.5 / SymPy 1.14.0. No input files or numerical optimizer.
The universal geometric argument is in the accompanying research handoff.
"""
import hashlib
import json
from pathlib import Path
import sympy as S

F = S.Rational
FACETS = ((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
          (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES = tuple(sorted({tuple(sorted((f[i],f[(i+1)%len(f)])))
                      for f in FACETS for i in range(len(f))}))
ARROWS = tuple(sorted((i,j) for a,b in EDGES for i,j in ((a,b),(b,a))))
EF = tuple(tuple(k for k,f in enumerate(FACETS) if a in f and b in f)
           for a,b in EDGES)
DUAL = tuple(sorted((i,j) for a,b in EF for i,j in ((a,b),(b,a))))
THETA = tuple(map(F,('4/5','9/10','1/3','1/2','1/400000')))
M0_NUMERATORS = ((508511640,-261705386,-171632506),
                 (-261705386,668094787,738335803),
                 (-171632506,738335803,1038663123))
CAP = F(1,400000)


def enc(x):
    if isinstance(x,S.MatrixBase):
        return [[str(x[i,j]) for j in range(x.cols)] for i in range(x.rows)]
    if isinstance(x,S.Basic):
        return str(x)
    if isinstance(x,dict):
        return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [enc(v) for v in x]
    return x


def pd(A):
    out = [S.factor(A[:k,:k].det()) for k in (1,2,3)]
    assert all(t>0 for t in out)
    return out


def verts(theta):
    x,r,p,q,la = theta
    assert 0<x<1 and 0<r<1 and p>0 and q>0 and p+q<1 and 0<la<=CAP
    s=1-la
    B=((F(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),
       (0,1-3*r/4),(0,F(1,4)),(F(1,16),F(1,16)))
    return tuple(S.Matrix((s*a,s*b,0)) for a,b in B)+(S.Matrix((0,0,1)),
                    S.Matrix((la,0,1)),S.Matrix((0,la,1)))


def moments(z,facets):
    D=S.Integer(0); K=S.zeros(3,1); L=S.zeros(3)
    for f in facets:
        for j in range(1,len(f)-1):
            a,b,c=(z[k] for k in (f[0],f[j],f[j+1]))
            d=a.dot(b.cross(c)); t=a+b+c
            D+=d; K+=d*t/4
            L+=d*(t*t.T+a*a.T+b*b.T+c*c.T)/20
    assert D>0
    g=K/D
    return D,g,(L/D-g*g.T).applyfunc(S.factor)


def poles(z,g,facets):
    out=[]
    for f in facets:
        a,b,c=(z[j] for j in f[:3]); n=(b-a).cross(c-a); h=n.dot(a)
        assert n!=S.zeros(3,1)
        for j in range(len(z)):
            assert n.dot(z[j])==h if j in f else n.dot(z[j])<h
        H=h-n.dot(g); assert H>0
        out.append(n/H)
    return tuple(out)


def audit(z,g,q,M,N):
    X=tuple(a-g for a in z)
    P={(i,j):(X[i].T*M*(X[j]-X[i]))[0] for i,j in ARROWS}
    E={(i,j):(q[i].T*N*(q[j]-q[i]))[0] for i,j in DUAL}
    U=[i for i in range(10) if all(v<0 for (a,b),v in P.items() if a==i)]
    stable=[i for i in range(9) if all(v<0 for (a,b),v in E.items() if a==i)]
    saddles=[]; weak={}
    for (i,j),(a,b) in zip(EDGES,EF):
        vals=(P[i,j],P[j,i],E[a,b],E[b,a])
        if max(vals)<0: saddles.append((i,j))
        if max(vals)<=0 and any(v==0 for v in vals):
            pp=next((X[k] for k,l in ((i,j),(j,i)) if P[k,l]==0),None)
            qq=next((N*q[k]/(q[k].T*N*q[k])[0]
                     for k,l in ((a,b),(b,a)) if E[k,l]==0),None)
            if pp is not None and qq is not None: assert pp==qq
            w=pp if pp is not None else qq
            assert w is not None
            kind='VF' if pp is not None and qq is not None else ('VE' if pp is not None else 'EF')
            key=tuple(w)
            if key not in weak: weak[key]={'point':w,'kind':kind,'edges':[]}
            weak[key]['edges'].append((i,j))
            if kind=='VF': weak[key]['kind']='VF'
    assert len(stable)+len(U)-len(saddles)==2
    return {'S':stable,'U':U,'H':saddles,'weak':list(weak.values()),
            'counts':(len(stable),len(U),len(saddles)),
            'zero_primitives':sum(v==0 for v in P.values())+sum(v==0 for v in E.values()),
            'primal':[(i,j,P[i,j]) for i,j in ARROWS],
            'polar':[(i,j,E[i,j]) for i,j in DUAL]}


def constants_and_algebra():
    r=F(1,6); R=F(18,5); k=F(281,40); e=CAP
    guards={}
    def positive(name,t):
        t=S.factor(t); assert t>0; guards[name]=t
    positive('covariance_inner_square',5/(3*(k*k+k+1))-r*r)
    positive('covariance_outer_square',R*R-15*k*k/(k*k+k+1))
    positive('centroid_drift_coefficient',17-R*32/(7*(1-e)**2))
    positive('horizontal_operator_square',43**2-F(5401728,3025)/(1-e)**2)
    positive('comparison_pyramid_inradius',r-60*e-F(10,61))
    positive('comparison_pyramid_circumradius',F(73,20)-R-17*e)
    positive('dual_pyramid_escape',4/F(73,20)**2-F(3,10))
    positive('polar_radial_displacement',614-612/(1-102*e))
    positive('polar_base_weight',65-F(129,2)/(1-102*e))
    positive('nonbase_to_side_polygon',1450-614-F(61,5)*65)
    positive('side_polygon_to_nonbase_hull',2250-F(3721,100)*60/(1-F(1037,10)*e))
    positive('base_pole_drift',623-F(183,5)*17)
    assert F(121,10)*(1450+2250)==44770
    assert F(91,5)*1450+6*623==30128
    assert 2*44770+30128==119668
    positive('nonbase_polar_exit_margin',F(3,10)-119668*e)
    assert guards['nonbase_polar_exit_margin']==F(83,100000)
    positive('basal_exit_margin_above_one_twentieth',2*r*r-R*111*e-F(1,20))
    positive('opposite_half_energy_gap_above_one_twentyfifth',2*r*r-7*R*111*e-F(1,25))
    x,y,d,h,u,v,H,kk,p=S.symbols('x y d h u v H kk p',real=True)
    rr=(x-d)**2+y*y; reflected=(-x/2-d)**2+y*y/4
    DV=3*d*(x-d)-rr-h*h/4
    assert S.expand(DV-((rr-9*d*d)/2-h*h/4-2*(rr-reflected)))==0
    top=(3*d+u)*(x-4*d-u)+v*(y-v)-H*(H+kk)
    expected=3*d*x-12*d*d-H*(H+kk)+u*(x-7*d)+v*y-u*u-v*v
    assert S.expand(top-expected)==0
    anchor=F(4,5)*p*S.Matrix((F(1,4),0))+F(4,5)*(1-p)*S.Matrix((0,F(1,4)))+F(1,5)*S.Matrix((1-p,p))
    assert anchor.applyfunc(S.expand)==S.Matrix((F(1,5),F(1,5)))
    assert F(10368,25)+F(165888,121)==F(5401728,3025)
    # Exact affine formula for the side polygon of a centred homogeneous pyramid.
    ax,ay,bx,by,ux,uy=S.symbols('ax ay bx by ux uy',real=True)
    HH=S.symbols('HH',positive=True)
    A=S.Matrix((3*ax/4,3*ay/4,3*HH/4))
    q=S.Matrix((4*ux/3,4*uy/3,4*(1-ax*ux-ay*uy)/(3*HH)))
    b=S.Matrix((bx-ax/4,by-ay/4,-HH/4))
    assert S.expand(q.dot(A)-1)==0
    assert S.expand(q.dot(b)-(4*(ux*bx+uy*by)-1)/3)==0
    return guards


def control(name,z,g,Sigma,q,D,g0,q0,Mraw,spectral):
    tau=S.factor(S.trace(Sigma*Mraw)); assert tau>0
    M=(Mraw/tau).applyfunc(S.factor); N=M.inv().applyfunc(S.factor)
    assert M*N==S.eye(3) and S.trace(Sigma*M)==1
    minors=pd(M)
    if spectral=='isotropic':
        assert Sigma*Mraw==S.eye(3)
        eigen_brackets=((F(1),F(1)),)*3
    else:
        Z=Sigma*Mraw
        eigen_brackets=((F(99,100),F(101,100)),
                        (F(599,100),F(601,100)),
                        (F(3599,100),F(3601,100)))
        for a,b in eigen_brackets:
            assert (Z-a*S.eye(3)).det()*(Z-b*S.eye(3)).det()<0
        assert eigen_brackets[1][1]/eigen_brackets[0][0]<F(281,40)
        assert eigen_brackets[2][1]/eigen_brackets[1][0]<F(281,40)
    X=tuple(a-g for a in z)
    vv=[(a.T*M*a)[0] for a in X]
    pp=[(a.T*N*a)[0] for a in q]
    r2=min(1/a for a in pp); R2=max(vv)
    assert r2>F(1,36) and R2<F(324,25)
    delta=g-g0; la=THETA[4]
    delta2=(delta.T*M*delta)[0]
    top_offsets=tuple(z[j]-z[7] for j in (7,8,9))
    top2=max((t.T*M*t)[0] for t in top_offsets)
    assert delta2<(17*la)**2 and top2<(43*la)**2
    bi=max(range(7),key=lambda i:vv[i])
    cross=[(X[bi].T*M*(X[j]-X[bi]))[0] for j in (7,8,9)]
    assert max(cross)<-F(1,20)
    fi=max(range(1,9),key=lambda i:pp[i])
    polar_exit=(q[fi].T*N*(q[0]-q[fi]))[0]
    assert polar_exit<-F(83,100000)
    # Exact reconstruction of the reflected-side comparison used in the proof.
    A=z[7]-g0; b0=q0[0]; bstar=-b0/3; qq=q[fi]
    rr=qq/(1+qq.dot(delta)); alpha=S.factor((1-A.dot(rr))/4)
    assert 0<=alpha<1
    side=((rr-alpha*b0)/(1-alpha)).applyfunc(S.factor)
    assert A.dot(side)==1
    assert all((z[j]-g0).dot(side)<=1 for j in range(8))
    reflected=3*bstar/2-side/2
    assert A.dot(reflected)==1
    assert all((z[j]-g0).dot(reflected)<=1 for j in range(8))
    mu=max(reflected.dot(t) for t in top_offsets)
    mapped=(reflected/(1-reflected.dot(delta)+mu)).applyfunc(S.factor)
    assert all(a.dot(mapped)<=1 for a in X)
    assert any(X[j].dot(mapped)==1 for j in (7,8,9))
    assert (mapped.T*N*mapped)[0]<=pp[fi]
    assert ((qq-side).T*N*(qq-side))[0]<(1450*la)**2
    assert ((mapped-reflected).T*N*(mapped-reflected))[0]<(2250*la)**2
    assert ((q[0]-b0).T*N*(q[0]-b0))[0]<(623*la)**2
    cc=audit(z,g,q,M,N)
    assert not cc['weak'] and cc['zero_primitives']==0
    assert any(j!=0 for j in cc['S']) and bi in cc['U'] and fi in cc['S']
    assert 0 in cc['S'] or len(cc['U'])>=2
    feet=tuple(g+N*a/(a.T*N*a)[0] for a in q)
    return {'name':name,'metric_before_scalar_normalization':Mraw,'normalization':tau,
            'M':M,'N':N,'M_leading_minors':minors,
            'raw_covariance_weighted_eigen_brackets':eigen_brackets,
            'physical_squared_inradius':r2,'physical_squared_circumradius':R2,
            'actual_centroid_drift_square':delta2,'top_spread_square':top2,
            'basal_norm_maximizer':bi,'its_three_top_derivatives':cross,
            'nonbase_pole_norm_maximizer':fi,'its_base_pole_derivative':polar_exit,
            'comparison_side_point':side,'reflected_side_point':reflected,
            'mapped_nonbase_point':mapped,'comparison_base_weight':alpha,
            'raw_facet_feet':feet,'census':cc}


def main():
    guards=constants_and_algebra()
    z=verts(THETA); D,g,Sigma=moments(z,FACETS); pd(Sigma)
    q=poles(z,g,FACETS)
    assert len(EDGES)==17 and len(DUAL)==34 and all(len(e)==2 for e in EF)
    x,r,p,qq,la=THETA; s=1-la; area=(31-24*x*p-24*r*qq)/64
    bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*qq*qq/8
    by=F(509,3072)-3*r*qq/8+3*r*r*qq/32+r*qq*qq/8-x*p*p/8
    expectedK=S.Matrix((3*s**3*bx/2+s*s*la*(1-3*x*p/4)/4+la*la/4,
                        3*s**3*by/2+s*s*la*(1-3*r*qq/4)/4+la*la/4,
                        area*s*s/2+la/2+la*la/4))
    assert D==la+2*area*s*s and D*g==expectedK
    QFAC=(FACETS[0],)+tuple((i,(i+1)%7,7) for i in range(7))
    d0,g0,C0=moments(z[:8],QFAC); q0=poles(z[:8],g0,QFAC)
    assert D-d0==la and d0==2*area*s*s
    assert g0==S.Matrix((3*s*bx/(4*area),3*s*by/(4*area),F(1,4)))
    mr=S.Matrix(M0_NUMERATORS)/10**6
    controls=[control('COVARIANCE_ISOTROPIC',z,g,Sigma,q,D,g0,q0,Sigma.inv(),'isotropic'),
              control('BASE_NOT_STABLE',z,g,Sigma,q,D,g0,q0,mr,'three_intervals')]
    assert 0 not in controls[1]['census']['S']
    assert controls[1]['census']['counts']==(2,2,2)
    report={'identity':'H5_APEX_CLUSTER_JOINT_EXCLUSION_V1',
            'python':'3.13.5','sympy':S.__version__,
            'scope':'All genuine H5 basal parameters, 0<lambda<=1/400000: no proper110. The proof uses one actual covariance-weighted physical metric and its inverse; it does not assert all-metric U>=2.',
            'lambda_upper':CAP,'positive_rational_guards':guards,
            'theta':THETA,'raw_vertices':z,'true_facets':FACETS,'true_edges':EDGES,
            'volume':D/6,'actual_centroid':g,'actual_covariance':Sigma,
            'actual_poles':q,'comparison_pyramid_volume':d0/6,
            'comparison_pyramid_centroid':g0,'comparison_pyramid_poles':q0,
            'controls':controls,'status':'PASS'}
    raw=(json.dumps(enc(report),sort_keys=True,indent=2)+'\n').encode()
    out=Path('h5_apex_cluster_joint_report.json');out.write_bytes(raw)
    print(out.name,len(raw),hashlib.sha256(raw).hexdigest())
    for c in controls:
        print(c['name'],c['census']['counts'],'WEAK',len(c['census']['weak']),
              'ZEROS',c['census']['zero_primitives'])
    print('H5_APEX_CLUSTER_JOINT_EXCLUSION_V1_PASS')


if __name__=='__main__':
    main()
```
