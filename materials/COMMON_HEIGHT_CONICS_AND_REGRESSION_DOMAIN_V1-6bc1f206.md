# material-6bc1f2062d78

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Common-height conics and the exact spectral shear domain

## Scope and chronology
This is a coordinator analytic extension of the established normal-parameter method, not a claim that affine elimination of the normal parameter is new. The fully read historical source [internal-source-reference], APICAL_U1_NORMAL_PARAMETER_COMPACTNESS_V1,11104B,SHA0537508d170a3851746d054aa9d13b4d3b66836d9c587cfefff15a0786143aeb already proves the general one-parameter reciprocal formulas, small/large normal exclusions, and the exact proper110 set as a finite union of open intervals after removing closed physical-contact intervals. The closed method branch [internal-source-reference] remains a valid completed analytical direction. What is added here is the degree-two structure of the remaining tangential problem at fixed shear, a precise interpretation of a relaxed determinant lift, exact projection of a spectral necessary domain, and its connection to the NEW amplified normal bound and actual region [internal-source-reference].

No whole E17 or whole H5 orbit is excluded by this reduction alone. No full conic arrangement has been executed. The bracket34<=Cmin<=622 and canonical C622 remain unchanged. Every claimed physical calculation uses the actual volume centroid, true facets and one inverse; abstract identities at an interior reference do not license replacing that centroid for a homogeneous body.

## 1. All true primitive signs share one affine normal parameter
Let centered true vertices be x_i=(r_i,h_i), actual poles q_f=(a_f,b_f), and fix a two-component shear v. Every SPD metric with this shear has

    M=[[G,Gv],[v^T G,v^T Gv+eta]], G>0,eta>0,
    N=M^-1=[[G^-1+vv^T/eta,-v/eta],[-v^T/eta,1/eta]].

Set y_i=r_i+h_i v and l_f=b_f-v.a_f. Then the genuine directed primal and polar edge primitives satisfy

    D_ij=y_i^T G(y_j-y_i)+eta h_i(h_j-h_i),
    eta det(G) E_fg=eta a_f^T adj(G)(a_g-a_f)
                     +det(G) l_f(l_g-l_f).

The same strictly positive multiplier eta det(G) is used for every polar row. This keeps all signs, including zero, without selecting another metric or recentering the polar. Top/base norm comparisons are also affine in eta and G.

A harmless zero primitive is not automatically an extra weak equilibrium. Proper stable and unstable equilibria require all appropriate outgoing primitives strictly negative. A closed physical edge contact requires its four incident primal/polar primitives all nonpositive. Vertex/facet degeneracies must likewise be interpreted through their full incident conditions. These are finite Boolean combinations of the primitive signs, not a demand that all4E primitives be nonzero.

## 2. Fixed shear leaves only conics after the exact common-height elimination
Scale the physical metric positively to set G11=1. Write

    G=[[1,b],[b,c]], d=c-b^2>0.

For a fixed actual body and fixed v, a primal row is r_i eta+P_i(b,c), where r_i is constant and P_i is affine. A positively scaled polar row is Q_j(b,c) eta+d s_j, with Q_j affine and s_j constant.

For any specified sign packet, eliminate eta>0 by exact affine-interval intersection, branching on the sign of its eta coefficients. The needed zero-coefficient and endpoint tests have degree at most two in(b,c). Indeed:

* primal/primal endpoint comparison is r_i P_k-r_k P_i, affine;
* primal/polar comparison is P_i Q_j-r_i d s_j, quadratic;
* polar/polar comparison is d(s_j Q_k-s_k Q_j); cancel the STRICTLY POSITIVE d to obtain an affine test.

The coefficient-sign tests are constant or affine. Comparisons of endpoints with eta=0 need signs of P_i or d s_j, again affine or constant after positive cancellation. Equality cases are retained; dividing by Q_j is allowed only in a branch with a known nonzero sign. Identically zero rows are handled by their requested sign rather than deleted as impossible mechanics.

Consequently, the existence of a physical metric realizing ANY prescribed full primitive-sign pattern at fixed v is a Boolean combination of polynomial equalities and inequalities of degree at most two in(b,c), with d>0. Taking the finite union of patterns corresponding to proper110 without extra weak equilibria gives an exact semialgebraic decision problem over a planar conic arrangement. This is not a claim that the exponentially large sign-pattern enumeration is the preferred implementation. Sign-invariant strata of the finite coefficient/endpoint-comparison arrangement can instead be traversed with exact root isolation, and the one-dimensional eta intervals reconstructed on each stratum.

The full two-dimensional arrangement has NOT been generated here. The durable executable [internal-source-reference] checks all2278 pair comparisons in the literal H5 control:561 primal/primal degree<=1,1156 mixed degree<=2,561 polar/polar degree<=1. It also implements a complete fixed-G positive-height sweep, not the full tangential arrangement. This distinguishes a proved finite procedure from a completed all-metric exclusion.

## 3. Meaning of the determinant lift: two heights are not one inverse
Alternatively scale eta to1 and put K=G/eta. Then

    M/eta=[[K,Kv],[v^T K,v^T Kv+1]],
    eta N=[[K^-1+vv^T,-v],[-v^T,1]].

Writing K=[[a,b],[b,c]],delta=det K makes every primal sign linear in(a,b,c,1), and every polar sign, after multiplication by delta, linear in(a,b,c,delta). The only algebraic compatibility left is delta=ac-b^2, together with K>0.

Dropping this determinant equality does NOT keep a common inverse. For delta>0 and a fixed positive K, the relaxed polar rows correspond exactly to

    N_rel=[[adj(K)/delta+vv^T,-v],[-v^T,1]],

whose physical inverse uses K'=(delta/det K)K rather than K. The primal rows still use K. Thus the relaxation permits different tangential/normal ratios on the two sides while preserving only the shear and tangential conformal class. Equivalently it assigns two independent normal heights to the same tangential shape. A feasible relaxed pair is not a physical S1/U1 metric. Section2 restores the missing compatibility by keeping one common eta throughout the interval intersections.

This interpretation explains why eliminating the common height before relaxing the tangential variables can be materially stronger than independently feasible primal and inverse-polar packets.

## 4. Exact projection of a consecutive-gap domain onto shear
Let Sigma>0 be the actual covariance, and put

    z=Sigma_zz, m=Sigma_Hz/z, D=(Sigma^-1)_HH,
    w=v+m, t=z w^T D w,
    C_v=Sigma_HH+Sigma_Hz v^T+v Sigma_zH+z vv^T
       =D^-1+z ww^T.

Consider ONLY the spectral conditions on H=Sigma^(1/2) M Sigma^(1/2): its ordered eigenvalues obey lambda3/lambda2<=p and lambda2/lambda1<=q, with fixed p,q>1. Their exact projection onto the shear plane, after allowing all G>0,eta>0, is

    t <= (pq-1)^2/(4pq).                                    (SHEAR)

Strict gap inequalities have the corresponding strict shear inequality. This statement is necessary and sufficient for the SPECTRAL domain alone, not for any equilibrium census.

Proof. Under the shear the covariance becomes

    Sigma_v=[[C_v,z w],[z w^T,z]],

and the metric is block diagonal diag(G,eta). Its canonical horizontal/vertical correlation is invariant under invertible block changes and equals

    r=sqrt(z w^T C_v^-1 w)=sqrt(t/(1+t)).

Choose the horizontal vector attaining that correlation and the vertical vector. Their two-dimensional principal compression has diagonals alpha,beta>0 and off-diagonal r sqrt(alpha beta). Its eigenvalue ratio is at least(1+r)/(1-r), with equality when alpha=beta. Interlacing gives the same lower bound on the full condition number. Since it is at most pq, this proves(SHEAR).

Conversely, horizontally whiten C_v, rotate the correlation direction to the first axis, scale the second horizontal axis freely, and set the vertical variance to1. The resulting physical covariance has the form

    [[1,0,r],[0,s,0],[r,0,1]],

with arbitrary s>0. Choose s between1-r and1+r and also in[(1+r)/p,q(1-r)]. This is possible exactly when(1+r)/(1-r)<=pq. The eigenvalues are1-r,s,1+r, so both required adjacent gaps hold. All transformations are one actual block metric G and one eta. Strict inequalities follow by choosing an interior s when(SHEAR)is strict. Squaring and rearranging r<= (pq-1)/(pq+1) gives the displayed t bound.

For the accepted actual-body17/2 theorem minimum-0261, use p=23884711/3600000,q=38716531/6000000 and kappa=pq=924733153857541/21600000000000. No claim is made that this realizes the underlying joint equilibria. In particular an entire spectral shear ellipse can contain no mechanically feasible metric.

## 5. Two exact compact tangential conics
With kappa=pq and rho=kappa/(1+kappa)^2, the same spectral hypothesis implies

    det(C_v)det(G)-rho tr(C_v G)^2 >=0,
    det(D)det(G)-rho tr(D adj(G))^2 >=0.                      (CONICS)

The first is the two-dimensional compression of the actual primal covariance/metric product; the second follows from the inverse compression, which uses the SAME G^-1 and the tangential covariance block D of Sigma^-1. Indeed, after the shear the inverse covariance has HH block D, while the inverse metric is diag(G^-1,1/eta). Every principal two-dimensional compression of a matrix with condition<=kappa also has that bound. For a2x2 positive matrix, condition<=kappa is exactly determinant/trace^2>=rho. Multiplying the inverse relation by(det G)^2 yields the second polynomial.

In the G11=1 chart each condition is a closed bounded filled ellipse lying strictly inside c>b^2. Its quadratic part is strictly negative definite: determinant contributes -b^2, and the squared trace has a nonzero c coefficient because the relevant covariance is positive definite. A point on c=b^2 would be a nonzero positive-semidefinite G with positive covariance trace, violating the inequality. Thus these are genuine compact conic restrictions, not arbitrary conditioning cutoffs. They are not sufficient for the full3D spectral domain at that specific G,eta.

In a port Gram chart S=[[1,X],[X,Y]], J=[Y_a,Y_b], define T=J^-1 C_v J^-T and U=J^T D J. The same conditions are the concave quadratic inequalities

    Y-X^2 >= rho (T11+2T12X+T22Y)^2/det T,
    Y-X^2 >= rho (U22-2U12X+U11Y)^2/det U.

These may be combined with the actual top-maximality, chord lens and amplified-normal halfplanes from [internal-source-reference] in a small convex local feasibility problem. A failed numerical solver is not an exclusion; exact separating multipliers or polynomial coverage are still needed.

## 6. Parallel two-end bodies have monotone proper instability along a fixed-height pencil
For raw levels0 and1 and actual centroid height0<gamma<1, every cross-layer primal eta slope is negative: -gamma from the base and -(1-gamma) from the top. Every same-layer slope is zero. Hence at fixed actual body,G,v, once a vertex is proper unstable it remains proper unstable for every larger eta. The proper unstable set is nested as eta grows.

At least one proper unstable vertex exists for every eta>0, since a global metric norm-maximizer is strict at every true neighbor. For sufficiently large eta there is a proper unstable vertex on each end layer: choose a tangential norm-maximizer on that layer, whose same-layer derivatives are strictly negative, and let its finitely many cross derivatives become negative. Thus U1, when present, occupies only an initial bounded part of the positive-height ray. A threshold may still have a weak additional contact, so proper110 without extra weak equilibria must remove the corresponding closed BAD intervals rather than treat the endpoint as harmless.

Every facet's proper-stability set along this same ray is an open interval, because all its positively scaled outgoing polar primitives are affine in eta. Thus the full proper110 test can combine the monotone primal root filtration with the finite interval arrangement of actual stable facets and physical contact sets. This is additional parallel-body structure within the already established common-normal method, not a replacement for the actual inverse.

## 7. Exact complementary nonwinners and what remains
The new exact region [internal-source-reference] excludes joint S1/U1 in a full shear rectangle of the literal W_ONLY_RESIDUAL H5 body, all G and eta. Its233weak000 countercontrol passes both(CONICS), the old scalar normal floor, the true top/spoke packet and strict actual chord, but fails the regression-amplified normal floor. This proves that keeping only the two tangential conics misses a real local obstruction.

A second exact control, source [internal-source-reference], shows the complementary limitation. On the same actual H5 body, let l=(0,66/5), a=a9,H=1-gamma, a'=a-c-Hm, L=l^T D^-1 l, s=(1-l.a')/H, w=s D^-1 l/L, v=w-m. Put A=Y9, h=(-A_y,A_x), G=ll^T+hh^T/10000. Then l.A=1, A^T G A=1 and det G=1/10000. Set eta to the arithmetic mean of the amplified lower bound and the true-spoke upper bound[(A^T G Y3)-1]/H.

This rational physical metric has a strict top9 maximum, positive true spoke9->3, passes the amplified normal inequality and the strict actual-chord lens, and has the necessary chord point strictly inside B. Nevertheless BOTH tangential conic slacks are negative. The exact full census is own435weak000, all68 primitives nonzero. Approximate diagnostic shear(.3390986451,.0704297587), eta1.3379410075, tau1.9096728142 are descriptive only; the exact source reconstructs every rational. This is neither the233 control nor the literal parent's different222 probe, and none is110.

The complete control dependency is [internal-source-reference] saved as lift_core.py,5750B,SHAa28576fb18443f2d0a10e06a2a82fa9e08132e29a7aefb4713f20da9d7577195, plus [internal-source-reference] saved as regression_rank_one_control.py,2211B,SHAae119dce474abd973be69ef4d9583c405f2604ac3bc12df6d04365ad2750b252. Environment CPython3.13.5,SymPy1.14.0. Run python -B regression_rank_one_control.py > regression_rank_one_control.out. Expected9191B,SHAcb0a2d351e4caa421a38e0a268d34a628c5d958568375400fe233db2dad274c9; marker REGRESSION_RANK_ONE_ACTUAL_CONTROL_V1_PASS. Coordinator normal and fresh-directory source-only runs were observed with identical output. The source uses no numerical solver or omitted data.

The conic and spectral statements in Sections1--6 are analytic derivations, not claims that the complete moduli problem was computationally decided. Their immediate useful connection is to impose the actual chord, both tangential conics and amplified normal information together, or to carry the full remaining true-arrow and root-facet constraints through the common-height elimination. Separate successes at independently chosen heights or metrics must not be combined into one physical witness.
