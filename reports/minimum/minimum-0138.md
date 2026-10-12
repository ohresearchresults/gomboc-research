# minimum-0138

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# COORDINATE_SATURATED_ROOT_SHARP_TRACE_V1

## 1. Determination

A complete seven-parameter root-only class is now bounded sharply, including its **three- and four-true-canonical-vertex strata**, unequal endpoint values, all root sizes and unbounded overhang. The geometric condition is that every true vertex of the positive-area root lies on one of the coordinate planes x=0 or y=0. The root may be triangular or quadrilateral; its two inner intercepts and two outer intercepts are independent. The canonical points C,D are not assumed contained in conv(A,B,F), and may both be genuine additional vertices.

For every such actual uniformly filled marked support-patch body,

    T <= Cstar < 203/100 < 51/25,
    2.0287830356734117251411563027 < Cstar
      < 2.0287830356734117251411563029.

Cstar is the exact algebraic constant from the literal parent. The new assertion is the whole-class upper bound with C and/or D true, not another computation in the solved two-canonical class. When c,d>0 the displayed upper bound by Cstar is strict. Nevertheless, Cstar is the supremum separately over the positive, unequal-endpoint three-canonical and four-canonical subfamilies; complete rational sequences proving sharpness are supplied below.

The proof has a finite, exhaustive actual-body moment atlas. Single exterior canonical points and opposite upper/lower points are controlled by genuine endpoint-changing comparisons. The difficult both-upper sector is handled by a coupled numerator/denominator inequality with an actual zero-endpoint comparison body. In the both-lower sector, and in the both-upper sector with at least one opposite endpoint at least one, the stronger T<=2 holds. All parameter ranges are continuous and unbounded where appropriate; there is no shape-grid exclusion.

This does **not** solve the whole root-only problem. A terminal patch with f<=9 and at most eight root vertices can still have root vertices with both x,y positive. A remaining T>=51/25 terminal patch must have three or four true canonical vertices **and at least one such nonaxial root vertex**. Arbitrary positive-ell auxiliaries remain outside this root-only theorem.

Two precisely reconstructed negative controls explain the complement. A proper contraction of a four-canonical axis-root patch can strictly INCREASE its original trace on a whole interval. On a genuine proper four-canonical body, a root-vertex neighbor-chord motion preserves root area but changes BOTH original denominator integrals to first order. Thus neither contraction monotonicity nor the two-canonical area-preserving chord argument can simply be extended to the unsolved mixed-anchor stars.

All controls are nonwinning; none is a threshold counterexample or a 110 body. No global complexity bound or incidence-registry count changes.

## 2. Source authority, reading and execution

The entire current research-journal(20260920-180557).md was read in consecutive chunks through EOF, including the complete literal parent and its encoded recovery. It has 324592 bytes and SHA-256 9aec3e0731016cfbfa375cc09722e4ac25a2630a2c76d1cea5382ee7610725dc. The required parent is **minimum-0131**, supplied immutable SHA-256 **d3756f66557a0c54904607b6213c9e6307c97e45dfc49c2b044b0538c73ac499**. Its two-canonical sharp theorem and proper-versus-patch distinction are inherited as stated.

The complete new analytic material POLYHEDRAL_TRACE_STATIONARITY_RIGIDITY_V1, [internal-source-reference], was also read: 14798 bytes, SHA-256 8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9. Its 90-vertex conclusion is conditional on a polyhedral local maximum over the full marked class. No polyhedral-attainment or unrestricted finite-supremum claim is imported from it. The new theorem below does not require that hypothesis.

The earlier complete transverse reduction and the parent's two complete source units were available and read; unchanged historical inputs were not restarted. No source-authority conflict or missing dependency affects the new result. The parent's sharp algebra is included self-contained in the new recovery, with its rational isolator inlined. No old sandbox import is needed.

The new geometry and algebra builds and verifications were executed successfully. A fresh extraction from the final embedded wrapper followed by build and verify reproduced all three report hashes and the final recovery markers. Numerical probing was not used as a proof of any whole-shape claim; every load-bearing computed finding is regenerated by the exact sources below.

## 3. Exact class and original integral atlas

Put

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    alpha=1-b, h=1+b, 0<b<1, c,d>=0,
    ell=1+(d-1)x+(c-1)y-alpha*z,
    n=(h+c)x+(h+d)y.

Let F=P intersect {ell=0} be a genuine positive-area polygonal root and

    P=conv(A,B,C,D,F).

Require x,y>=0 on P, A,B true, and every true root vertex on x=0 or y=0. This is the coordinate-saturated root class. Its actual projected root is

    R=conv((rho,0),(X,0),(0,Y),(0,sigma)),
    0<rho<=X, 0<sigma<=Y, rho*sigma<X*Y.       (1)

Coincident successive generators are removed; a triangular root is allowed. The excluded origin would lift to (0,0,1/alpha) and make B nonextreme. If c=0 or d=0, the corresponding canonical point belongs to the actual root: include it and re-hull before defining the true intercepts in (1). It is not a positive-density auxiliary and must not be counted twice.

Define the ORIGINAL uniform-body integrals

    V=integral_P 1, Bell=integral_P ell, N=integral_P n,
    L=6*alpha*V, E=24*alpha*Bell, M=24*alpha*N.

Then, exactly,

    T=alpha*M/(L*E).                            (2)

Use the affine coordinates (x,y,w)=(x,y,ell), with absolute Jacobian alpha. All following upper/lower terminology refers to w, not to the physical z coordinate. This change of coordinates retains the original uniform density up to that constant Jacobian. It is not the balanced projectivity or a refill of its image.

The actual AB-core is K=conv(A,B,F). Its two off-root points in this chart are (0,0,1),(0,0,b). With kx=h+c, ky=h+d its exact scaled integrals are

    L0=X*Y-b*rho*sigma,
    E0=X*Y-b^2*rho*sigma,
    M0=X*Y*(kx*X+ky*Y)-b*rho*sigma*(kx*rho+ky*sigma).    (3)

These follow by the actual radial-cone integrations in the parent, or directly from two positive tetrahedral fans. Its upper boundary over the quadrant triangle is w=1-x/X-y/Y. Its lower boundary is the positive part of b*(1-x/rho-y/sigma).

The canonical point C=(0,1,c) is above the core if c>UC=1-1/Y, below it if c<LC=b*max(0,1-1/sigma), and otherwise contained. If Y<1 it is necessarily above. D has the analogous tests UD=1-1/X, LD=b*max(0,1-1/rho). Equalities are actual face mergers. These tests exhaust every possibility.

An upper C sees exactly the old upper triangle. Its tetrahedral addition has determinant delta=X*[1+(c-1)Y]>0, and adds to (L,E,M)

    delta*(1, 1+c, kx*X+ky*(Y+1)).              (4)

A lower C sees exactly the old lower triangle. Here delta=rho*[(b-c)sigma-b]>0, and the increment is

    delta*(1, b+c, kx*rho+ky*(sigma+1)).          (5)

Swap x,y and c,d for D. Each row is an actual tetrahedron's volume and affine vertex-average integrals; the weights are not free scalar moments. Root-plane, coordinate-plane and canonical containment constraints are retained when using these formulas.

### The two-exterior-point cells

If C is upper and D lower, both additions are disjoint actual visible caps. The new plane through C and the two outer root points does not become visible from D: for Y>1, c>UC while d<UD, and therefore d*UC<c*UD; for Y<=1 the same signed inequality is automatic. The exact simplified expressions are

    L=X*(1+cY)-sigma*(d*rho+b),
    E=X*(1+c+c^2Y)-sigma*(d^2*rho+b*(b+d)),
    M=kx*[X^2*(1+cY)-sigma*(d*rho^2+d*rho+b)]
      +ky*[X*(1+cY+cY^2)-sigma^2*(d*rho+b)].       (6)

The opposite mixed case is its reflection.

If both points are lower, rho,sigma>1. Reflect if needed so c/LC<=d/LD. Add C first, then D sees only the new triangle through B,C and (rho,0,0); its determinant is rho*(b-d)-b. The full actual integrals are

    L=X*Y-c*rho*sigma-d*rho-b,
    E=X*Y-c^2*rho*sigma-d*(c+d)*rho-b*(b+c+d),
    M=kx*[X^2Y-c*rho^2*sigma-d*rho*(rho+1)-b]
      +ky*[X*Y^2-c*rho*sigma*(sigma+1)-d*rho-b].    (7)

If both points are upper, reflect if needed to impose

    d*(1-1/Y) <= c*(1-1/X).                       (8)

Then the plane through C and the two outer root points supports D on its inner side. After adding C, D sees only the triangle through A,C and (X,0,0), with determinant 1+(d-1)X. Therefore

    L=1+dX+cXY-b*rho*sigma,
    E=1+c+d+d*(c+d)X+c^2XY-b^2*rho*sigma,
    M=kx*[1+dX*(X+1)+cX^2Y]
      +ky*[1+dX+cXY*(Y+1)]
      -b*rho*sigma*(kx*rho+ky*sigma).             (9)

At equality in (8), coplanar triangles are merged into their actual maximal polygon. They are not separately counted as facets or edges. Equations (3)–(9), including their closures, are the complete moment atlas. The physical root area is

    sqrt((1-c)^2+(1-d)^2+alpha^2)*(XY-rho*sigma)/(2*alpha)>0.

Throughout actual comparisons V>=1/6 and Bell>=(1+b+c+d)/24. Every denominator-clearing multiplier below is strictly positive on the actual domain; its algebraic zero faces are used only to close a coefficient certificate.

## 4. Three-canonical and mixed-stratum comparisons

### 4.1. One exterior point: remove the contained endpoint's penalty

Suppose only C is exterior, while D is contained. Necessarily d<1 and X>=1/(1-d). Set u=rho/X. In (3)+(4) or (3)+(5), after cancelling the common powers of X in (2), the only remaining X-dependence is a positive coefficient times ky/X. Decreasing X to 1/(1-d), with rho=uX, therefore does not decrease T. The lower containment test for D only becomes weaker.

Next decrease d to zero while setting X=1/(1-d), rho=uX. The same actual formulas now depend on this change through

    ky/X=(h+d)(1-d)=h-bd-d^2,

which increases as d decreases. D stays contained: its upper boundary is exactly d and its lower boundary is at most bd. Thus this is a genuine nondecreasing-trace comparison leading to d=0,X=1. It changes the root plane, actual volume and density integral; it does NOT purport to preserve fixed-endpoint data or those moments. They are recomputed together by the same exact formula.

### 4.2. Single upper C

With rho=u, sigma=vY, d=0,X=1, define

    U(c)=(h+c)*(1+cY-b*u^2*vY)
           +h*(1+cY+cY^2-b*u*v^2Y^2),
    D(c)=(1+cY-buvY)*(1+c+c^2Y-b^2uvY).

The trace is alpha*U(c)/D(c). For 0<Y<=1 the exact certificate proves

    U(0)D(c)-U(c)D(0)>=0       for all c>=0.       (10)

For Y>1 set c0=1-1/Y. It proves

    U(c0)D(c)-U(c)D(c0)>=0     for all c>=c0.      (11)

At the comparison endpoint C is contained or is on the root. If Y<1 and c becomes zero, the ACTUAL root enlarges to include C; the outer root point at y=Y can become redundant. This is not the old root held fixed under a false deletion step. The resulting body is in the parent's solved two-canonical class, so T<=Cstar.

The comparisons are strict for an upper C with positive excess c-c0: after clearing denominators the highest excess-cubic coefficient is a strictly positive multiple of U(c0), while the other certified coefficients are nonnegative. If c0>0 the parent's endpoint gap also suffices for strictness. Thus the positive-endpoint three-canonical upper sector has T<Cstar.

### 4.3. Single lower C

Now write sigma=Y>1, far intercept Y/v, rho=u, X=1,d=0. The actual reduced expressions are

    L=Y/v-u*(cY+b),
    E=Y/v-u*(c^2Y+b*(b+c)),
    M=(h+c)*(Y/v-u^2*(cY+b))
       +h*((Y/v)^2-u*(cY^2+cY+b)).

Raise c to c0=b*(1-1/Y). The exact denominator-cleared comparison gives

    T(c)<=T(c0),  0<=c<=c0.                      (12)

C is contained at the endpoint, and c0>0. The parent therefore yields the strict bound by Cstar. The comparison changes the endpoint density and physical root heights; it never replaces the original moments by free variables.

### 4.4. Opposite upper/lower points

For (6), raise d to d0=b*(1-1/rho), leaving the root xy coordinates and b,c fixed. The certificate proves

    T(c,d)<=T(c,d0),  0<=d<=d0.                  (13)

The endpoint has D contained and is covered by 4.2. To cover the entire geometry in (13), use

    rho=1/k, X=1/(ku), sigma=vY, d=d0*z,
    0<k,u,v<=1, 0<=z<=1.

For Y<=1 keep c as a nonnegative orthant variable. For Y>1 set Y=1/l, c=1-l+e with 0<l<=1,e>=0. Multiplying L,E by ku and M by (ku)^2 clears the root denominators. Divide the comparison numerator by d0-d; in the second chart multiply by l^4. The resulting polynomial is nonnegative on each ENTIRE product of its closed unit box and nonnegative orthant. This proves all of the mixed sector, not just a neighborhood of a special root.

## 5. Both-lower sector: T<=2

For (7), set

    rho=1/k, sigma=1/l, X=1/(ku), Y=1/(lv),
    c=b*(1-l)*t,
    d=b*(1-k)*[t+(1-t)z],
    b,k,l,u,v,t,z in [0,1].

In the actual strict cell k,l,u,v>0; lower-point ordering is exactly the displayed parametrization of c/LC<=d/LD. It covers all possibilities after reflection. Scale L,E by kluv and M by (kluv)^2. The polynomial

    2*Lhat*Ehat-(1-b)*Mhat

has 9216 nonnegative tensor Bernstein coefficients on the WHOLE unit cube. Consequently T<=2. Flat root or infinite-intercept faces of the cleared parameter cube are not asserted to be actual class members; the certificate is simply stronger by including them algebraically.

## 6. Both-upper sector: the coupled denominator comparison

### 6.1. Complete moderate-endpoint parametrization

First let 0<=c,d<1. Introduce endpoint odds C0=c/(1-c), D0=d/(1-d) and outer-intercept deficits

    p=1/[(1-d)X]-1,
    q=1/[(1-c)Y]-1.

In a strict both-upper cell p,q>0. Condition (8) is precisely C0*p<=D0*q. It has the complete parametrization

    C0=q*a, D0=p*(a+t), a,t>=0,
    X=(1+D0)/(1+p), Y=(1+C0)/(1+q),
    rho=uX, sigma=vY, 0<u,v<=1.

Boundary cells with p=0 or q=0 follow by actual body/moment continuity; they are not obtained by dividing by zero. Let

    Fp=(1+p)(1+q), Hp=(1+C0)(1+D0),
    Lhat=Fp*L, Ehat=Fp*Hp*E, Mhat=Fp^2*Hp*M,
    Dhat=Lhat*Ehat.

The original trace is still alpha*Mhat/Dhat. Set a=t=0 in these SAME formulas to define Dhat0,Mhat0. Explicitly,

    Dhat0=(Fp-buv)*(Fp-b^2uv),
    Mhat0=h*[2Fp^2-buv*(u*(1+q)+v*(1+p))].       (14)

This baseline is an ACTUAL zero-endpoint patch: outer root intercepts of the true hull are one, while the inner intercepts are u/(1+p), v/(1+q). Canonical C,D become root points; any redundant supplied outer generators are removed. Its original T0=alpha*Mhat0/Dhat0 is bounded by Cstar.

### 6.2. Exact coupled inequality

With tau0=101/50, the certificates prove on the whole unit box b,u,v and unbounded orthant p,q,a,t:

    Dhat-Dhat0 >= 0,
    tau0*(Dhat-Dhat0)-alpha*(Mhat-Mhat0) >= 0.   (15)

They do not assert that the PHYSICAL product V*Bell is monotone; Dhat includes the explicitly displayed positive coordinate factors. Using the SAME denominator in the numerator comparison gives

    T <= tau0+(T0-tau0)*Dhat0/Dhat
      <= max(tau0,T0)
      <= Cstar.                               (16)

This is the critical new variational substitute for an unproved pointwise deletion or projection rule. The extra canonical mass is controlled together with the denominator that its actual geometry produces. The weaker maximum comparison, rather than a claim T<=T0 in every case, is what is certified.

For c+d>0 the inequality by Cstar is strict. Indeed, put z1=buv,z2=b^2uv,Gp=1+q. Direct expansion gives

    Lhat=(Fp-z1)+D0*(Gp-z1)+C0*(1-z1)+C0*D0*(1-z1),
    Ehat=Fp*(1+2C0+2D0+3C0D0)
          +Gp*(C0D0+D0^2+2C0D0^2)
          +C0^2*(1+2D0+D0^2)
          -z2*(1+C0)^2*(1+D0)^2.

Every nonconstant coefficient in C0,D0 is positive, since Fp,Gp>=1 and z1,z2<1. Therefore Dhat>Dhat0. If T0>tau0, (16) is strictly less than T0; otherwise it is at most tau0<Cstar. This argument also treats actual moderate-endpoint boundary cells by continuity of the displayed formulas.

### 6.3. At least one opposite endpoint at least one

For the remaining both-upper case, use s=1/X,t=1/Y and rescale L,E by st, M by (st)^2. The exact expressions are

    L=st+dt+c-buv,
    E=st*(1+c+d)+d*(c+d)t+c^2-b^2uv,
    M=(h+c)*[s^2t^2+d*(s+1)t^2+ct]
      +(h+d)*[s^2t^2+dst^2+cs*(t+1)]
      -buv*[(h+c)ut+(h+d)vs].                  (17)

The constraints are s,t>0, s>=1-d,t>=1-c and cs-dt<=c-d. The following FOUR complete charts exhaust them after the controller choice (8). All capitals C0,D0 and variables z,e are nonnegative orthant parameters; a and the unspecified smaller endpoint are in [0,1].

|Chart|Substitution|Positive multiplier for 2LE-alpha*M|
|---|---|---|
|c>=1,d<=1|c=1+C0, t=z, s=1-d+d*a*(C0+z)/(1+C0)|(1+C0)^2|
|d>=1,c<=1|d=1+D0, s=z, t=1-c/(1+D0)+cz/(1+D0)+e|(1+D0)^2|
|c>=d>=1|c=1+D0+C0,d=1+D0,t=z,s=a*[C0+(1+D0)z]/(1+D0+C0)|(1+D0+C0)^2|
|d>=c>=1|c=1+C0,d=1+C0+D0,t=D0/(1+C0+D0)+z,s=a*(1+C0+D0)z/(1+C0)|(1+C0)^2*(1+C0+D0)^2|

For example, in the first chart the allowed s-interval is exactly [1-d,(c-d+dt)/c]; in the fourth, nonnegativity forces t>=(d-c)/d. The other bounds are the same linear support inequality solved for the remaining reciprocal intercept. Thus these are parameterizations of the complete domains, not heuristic sufficient subsets.

After the stated multiplier, every orthant coefficient has nonnegative tensor Bernstein coefficients in the unit variables. This proves T<=2 throughout the four charts, including c=1 and d=1 seams.

## 7. Exact continuous coverage and inherited sharp endpoint

For a power polynomial P in unit variables x_i with degrees n_i, the certificate uses its exact tensor Bernstein coefficients

    B_k = sum_{j<=k} A_j * product_i binom(k_i,j_i)/binom(n_i,j_i).

Every nonnegative orthant variable is left in ordinary nonnegative powers; its coefficient is separately certified on the complete unit box. The verifier independently reconstructs the original power polynomial from each Bernstein tensor by finite differences. No sampling, numerical tolerance, solver status, discarded infeasible cell, or unspecified leaf list is involved.

The exact certificate totals are:

|Continuous cell family|Tensors|Coefficients|Positive|Zero|
|---|---:|---:|---:|---:|
|Single upper, Y<=1|3|955|808|147|
|Single upper, Y>=1|3|737|692|45|
|Single lower to containment|1|2700|1374|1326|
|Mixed, Y<=1|5|19035|13071|5964|
|Mixed, Y>=1|5|13185|9151|4034|
|Both lower|1|9216|8710|506|
|Both upper denominator increment|117|2043|1853|190|
|Both upper 101/50 increment|129|3117|2927|190|
|Upper c>=1,d<=1|20|1775|1662|113|
|Upper d>=1,c<=1|53|1408|1361|47|
|Upper c>=d>=1|78|1555|1481|74|
|Upper d>=c>=1|147|2891|2695|196|
|TOTAL|562|58617|45785|12832|

For the 101/50 increment only, four orthant exponent groups in order (p,q,a,t), namely (1,1,0,1),(1,0,1,0),(1,0,0,1),(0,1,1,0), use the FOUR CLOSED b-intervals [j/4,(j+1)/4], j=0,1,2,3. All other coefficients use the full cube. This is the complete subdivision rule, embedded in the source. Zeros are intentional: the final strict threshold margin comes from Cstar<2.03<51/25, not from calling every coefficient strictly positive.

The algebra unit constructs (10), (11) directly as cross-products. For (12) it substitutes Y=1/k,c=b(1-k)z, multiplies M and LE by k^2v^2 and divides out 1-z. For (13) it uses the quotient described in 4.4. For the both-lower and both-upper cells it uses exactly (7), (9), and (17) with the stated substitutions. Thus every polynomial and coefficient stream is recoverable without a coefficient table download.

For completeness, the inherited sharp envelope is

    H(b,r)=2*(1-b^2)*(1-b*r^3)/[(1-b*r^2)*(1-b^2*r^2)].

Its maximum is Cstar. Define

    g(r)=r^8+4r^7-2r^6-12r^5-7r^4-4r^3-12r^2+12r+8,
    B(r)=(3r^7+11r^6-9r^5-33r^4-20r^3-12r+40)/16.

Then rstar is the unique root of g in (0,1), bstar=B(rstar), Cstar=H(bstar,rstar). The retained exact algebra verifies the derivative eliminations, the resultant and Groebner identities, the one-sign-change transformed polynomial, and 110 rational isolating bisections. The inherited boundary estimate H-2<=1-r handles the joint b,r->1 corner. No novelty is claimed for that inherited computation. The exact rational value H(1/4,5/6)=133020/65569>101/50 justifies the strict last comparison in (16).

## 8. Sharpness separately in the remaining canonical strata

Cstar is attained in the full nonnegative-endpoint axis-patch class by the parent's c=d=0 root rstar<=x+y<=1, with z=(1-x-y)/(1-bstar). Its true f-vector is 6/9/5 and its coordinate facets are quadrilaterals. It is not a proper triangular-pair attainer.

The new upper bound is sharp even when one insists on **positive unequal c,d and exactly three or four off-root canonical vertices**. Here is a complete rational recipe. For each integer n>=4, bisect g on [0,1] exactly 2n+20 times, using g(mid)>0 to replace the lower endpoint, and take the final midpoint r_n. Put b_n=B(r_n), c_n=2^-n,d_n=c_n/2. Define:

    Three-canonical sequence:
       X=1/(1-d_n), Y=1, rho=r_n*X, sigma=r_n.

    Four-canonical sequence:
       X=1, Y=1-c_n^2, rho=sigma=r_n.

Lift the four root generators by ell=0 and take their hull with T0. In the first sequence C is above the AB-core and D is contained; the true f-vector is 7/11/6. In the second both are above and the true f-vector is 8/13/7. All root areas are positive. The parent isolator gives .830<rstar<.831 and .236<bstar<.237; the polynomial B has |B'(r)|<=21 on [0,1], so the nested bisection error already at n=4 guarantees 0<b_n<1 and the required strict intercept inequalities for the entire sequence. All parameters are rational, c_n!=d_n, and both sequences converge to the same sharp patch. Original volume and moments converge, so T tends to Cstar.

The complete exact audit includes n=4,8,16 in both sequences. For orientation their traces are approximately (1.9983588112,2.0275951491,2.0287785997) in the three-canonical sequence and (1.9923006361,2.0275673047,2.0287785993) in the four-canonical sequence. The convergence proof is analytic, not inferred from these six controls. These are patch sequences, not proper triangle-pair sequences.

## 9. Actual controls and the exact failed extensions

All parameter tuples below use the order

    (b,c,d,rho,X,sigma,Y).

The canonical input labels are 0=A,1=B,2=C,3=D. Root labels 4,5,6,7 are the lifts of (rho,0),(X,0),(0,Y),(0,sigma), in that order. Every reported body is re-hulled; redundant labels are not counted as vertices.

### 9.1. A high four-canonical body and a genuinely unequal three-canonical body

The four-canonical control is

    (1/4,1/1000,1/2000,5/6,999/1000,5/6,999/1000).

It is true 8/13/7, has a genuine quadrilateral root and maximal facet cycles

    01762, 03541, 023, 147, 263, 365, 4567.

Its coordinate facets are pentagons. Its ORIGINAL data are

    V=14901964009/81000000000,
    Bell=34491562928009/648000000000000,
    N=231682833486715919/1944000000000000000,
    T=94779340971838330500000/46726548124304434184371
      approximately 2.0283831093129607.

The three-canonical control is

    (1/4,1/12,1/1000,5/6,1000/999,5/6,109/100).

It is true 7/11/6: C is a true vertex and D is a nonvertex mark. Its maximal cycles in the original input labels are

    01762, 0541, 025, 147, 265, 4567.

Its actual data are

    V=44035/215784,
    Bell=603385/10357632,
    N=3698358433003/25868185920000,
    T=33285225897027/16606286546875
      approximately 2.004375018043433.

Here c=1/12 exceeds 1/15 and Y=109/100 is an actual overhang; no assertion is made that this individual body fails every prior sufficient test. Both controls have own-centroid strict S/U/H=4/4/6, no weak packets and all true-edge primitives nonzero. They are not 110 bodies or the 10/17/9 layer.

Coalescent controls are also retained: the lower-order wall (3/5,3/40,1/10,3/2,7/4,4/3,8/5) is true 8/12/6; the upper-controller wall (1/4,1/13,1/13,26/45,13/15,52/75,13/15) is true 8/12/6; and the triangular-root control (1/4,1/13,7/67,67/72,67/72,13/20,13/16) is true 7/12/7. They are actual maximal-facet controls, not generic triangulations assigned the wrong f-vector. Their complete volumes, moments and mechanics are regenerated by the source.

### 9.2. Proper root contraction can strictly increase T

Use the moderate four-canonical axis patch

    p=(1/4,1/13,7/67,67/90,67/72,117/160,13/16).

It is true 8/13/7, with

    V=58711/259200,
    Bell=8692253/133785600,
    N=289699722181/1733861376000,
    T=152473537990/80578557771
      approximately 1.892234636704739.

Let q be the arithmetic mean of its four actual root vertices and form

    F_epsilon=(1-epsilon)F+epsilon*q,
    P_epsilon=conv(T0,F_epsilon).

For EVERY 0<epsilon<=1/100 this is a genuine 8/17/11 body with exact full ABC and ABD, positive root area, and trace STRICTLY INCREASING in epsilon. In particular it exceeds the axis patch value. At epsilon=1/100,

    V=1041974219/4608000000,
    Bell=320814261749/4939776000000,
    N=22841729975852747/136996454400000000,
    T=8223022791306988920000/4345642467789686037403
      approximately 1.8922455890600327.

The complete closed interval is certified by the actual supporting-facet polynomials: 188 nonpositive Bernstein coefficients, of which 138 are negative and 50 zero, and 27 oriented fan coefficients. The cleared trace derivative has SEVEN strictly positive Bernstein coefficients. Root area is multiplied by (1-epsilon)^2. Exact endpoint volume/first-moment integration agrees with the full interval polynomials.

This is a genuine continuous counterexample to nonincrease under proper root contraction. It is not a counterexample to the new axis-class bound: P_epsilon has nonaxial root vertices and is outside that class. It remains far below 51/25. Initial and endpoint own-centroid controls are strict4/4/6 with all primitives nonzero; no whole-interval mechanical census is asserted.

### 9.3. Root area preservation does not preserve the actual denominator moments

On that same proper P_(1/100), move only input root vertex 4 by

    v4(t)=v4+t*(v5-v7), |t|<=1/10000,
    v5-v7=(737/800,-11583/16000,-209/1000).

The entire interval retains its genuine 8/17/11 lattice, exact coordinate triangles and root plane. Its root xy area is CONSTANT,

    Area_xy(F)=6639633/64000000.

But the original integrals have the exact nonzero derivatives

    dV/dt=7080359/384000000,
    dBell/dt=2007863/1228800000.

The certificate includes all 124 supporting coefficients, 86 negative and 38 zero, and the complete original volume, first-moment and trace polynomials. Three actual bodies at t=-1/10000,0,1/10000 are independently re-hulled and integrated, each at its own centroid. Thus the failure is a whole true-lattice interval, not a spurious diagonal event or a density substitution.

This closes a concrete methodological question: a neighbor-chord motion has the automatic denominator preservation used by the parent only in the appropriate two-anchor star. Mixed canonical/root facets create additional first-order volume and ell-integral terms. Preserving the planar root area is not enough to suppress them.

### 9.4. Complete geometric audit scope

The report contains 38 fully reconstructed body records plus the three chord-interval body audits, including their shared middle control. It retains all seven-parameter inputs, comparison endpoints, large-endpoint controls, a triangular root, controller walls, ten proper contractions and both sharp rational sequences. Every body has all its true-edge primitives nonzero and no weak edge packets; the strict counts are reported individually, not asserted identical across the family.

Each hull is reconstructed by exact supporting triples and actual polygonal facet cycles. An independent supporting-plane intersection computation recovers precisely its true vertices. True edges satisfy Euler's identity. Two positive interior tetrahedral fans give identical original volume and full first moment; every centroid and mechanical audit uses that body's own uniform-volume centroid.

The actual balanced image is separately re-hulled. Two image fans integrate the transformed ORIGINAL density and verify exactly

    I4=Jp*V, Iell=Jp*Bell, In=Jp*N,
    T=Jp*In/(6*I4*Iell), Jp=b*(1+b+c+d)^2.

No uniformly refilled image centroid is used. Three additional complete original-height comparison intervals are checked by supporting polynomials and exact moment identities. The global exclusion, however, comes from the exhaustive atlas and algebraic certificates, not from these controls.

## 10. Boundary scope and precise open complement

The theorem assumes 0<b<1 and a true positive-area root. Its estimates have the uniform ceiling Cstar<51/25, so they pass by continuity of the ORIGINAL integrals to any full-dimensional Hausdorff limit of this class with the retained T0. This includes zero-endpoint limits and limits with a collapsed root support; a collapsed support is not called a facet. No claim is made by dividing by alpha at b=1. The separately accepted balanced theorem retains its own hypotheses.

All canonical status changes and c=1,d=1, upper/lower-controller equalities are included by the actual formulas and hull coalescences. A formal unit-cube face representing an infinite intercept, a zero denominator in reciprocal coordinates, or a zero-area root is only part of the algebraic overcover, never an asserted geometric member.

The supplied transverse theorem yields a dominating f<=9 marked patch at fixed positive endpoint values; the literal parent strengthens its root count to k<=8 and its proper supremum count to 12. If that dominating patch is coordinate-saturated, the new uniform bound excludes T>=51/25 for the starting proper body, INCLUDING equality. No proper resolution is needed for that implication.

Conversely, a bound for coordinate-saturated patches does not automatically bound all their proper contractions: Section 9.2 shows why. The general contraction theorem transfers strict violations and suprema, not equality, attainment, moment preservation or a fixed face lattice. The remaining root-only terminal strata have three or four true canonical vertices and at least one root vertex with x,y>0. There is no proof here that the remaining roots can be reduced to the axes, that the unrestricted maximum is polyhedral, or that arbitrary positive-ell auxiliaries disappear.

## 11. Most useful continuation

The exact mixed-anchor moment atlas has resolved the whole coordinate-saturated case, including the real freedom of two independently active canonical endpoints. Its both-upper proof uses the actual ratio's common denominator instead of assuming that all extra mass lowers the trace.

The decisive remaining difficulty is an interior root vertex whose neighboring lateral facets use different positive-ell canonical anchors. A root-area-preserving slide then changes both denominator integrals, as the genuine interval in Section 9.3 proves. A useful successor must compensate those terms by a coupled multi-vertex motion, or control their signed contribution analytically while handling actual fan switches. The conditional 90-vertex stationarity theorem does not by itself supply that compensation or polyhedral attainment.

The universal root-only T<51/25 statement, the full unrestricted weighted trace, the global 34..622 interval and every incidence-registry count remain unchanged outside the newly excluded shape class.

## 12. Complete recovery and observed terminal receipts

Save the complete source below as recover_axis_root_v1.py, UTF-8/LF with a final LF. Run

    python -S recover_axis_root_v1.py sources work
    python -S recover_axis_root_v1.py build work
    python -S recover_axis_root_v1.py verify work

Actual environment: CPython3.13.5, assertions enabled. The geometry child uses only standard-library Fraction arithmetic. The two algebra children require SymPy1.14.0 and are deliberately launched without -S. No optimizer, random seed, old source file, journal, report download or external coefficient array is required.

|Object|Bytes|SHA-256|
|---|---:|---|
|recover_axis_root_v1.py|18046|ce74cdf8158cb4fbfc8419146d06bb65dc50794f6e95d7162dfb4e0c1405dbaf|
|Complete three-source payload|37081|d1c74ff26522811c1eb81a1b7cae8d0ecaa9e57f32a06a7ea1439ea730bdc5e3|
|axis_trace_geometry_v1.py|23071|fce11750f4e377851cebb39fd565e6a81bfc0e16c02523ee7101d55a6ab874e6|
|axis_trace_algebra_v1.py|7801|a67520914fca58e5d7307e1956ea1cf6545ce8bc70cb67c31238ce8541ce08db|
|axis_sharp_constant_v1.py|5408|0a5103ea246accd62a4dcb30296236d168fc9aa2d1a04f196151e87a4904e352|
|axis_trace_geometry_v1.json|541300|21b8843385cf30d7c6e03ecd1d2f666c948b1a0542134bfb71c7c3c711ec0d11|
|axis_trace_algebra_v1.json|277590|132bdd86db6290e0c08463e7f2a35991b68ad1d7ce14ed8a009201d7248d09f4|
|axis_sharp_constant_v1.json|5715|3efd2b3deb81d6a58360b04fd6c4f2580df6c2c6c0a0286a6204a19cffb251f9|

Original and fresh final-wrapper source-only build/verify runs produced matching reports. Observed markers are COORDINATE_SATURATED_ROOT_ACTUAL_GEOMETRY_AND_WEIGHTS_PASS, COORDINATE_SATURATED_ROOT_ALL_ORTHANTS_BERNSTEIN_PASS, TWO_CANONICAL_ROOT_UNIQUE_SHARP_MAXIMUM_PASS and COORDINATE_SATURATED_ROOT_SELF_CONTAINED_RECOVERY_PASS. Every coefficient tensor, original power polynomial, input body, true facet, volume, first moment, transformed-density identity and interval guard regenerates from the source. Hashes are not being used as substitutes for missing arrays. This is exact computational algebra plus the geometric proof above, not a proof-assistant formalization.

Convenience copies: autonomous recovery (`recover_axis_root_v1.py`), plain actual-body audit (`axis_trace_geometry_v1.py`), plain continuous algebra certificate (`axis_trace_algebra_v1.py`), and complete sources and reports (`axis_root_v1_complete.zip`). The complete embedded recovery, not these links, is the durable handoff.

### Complete autonomous source

```python
# COORDINATE_SATURATED_ROOT_SHARP_TRACE_V1 autonomous recovery.
# Parent minimum-0131 SHA256
# d3756f66557a0c54904607b6213c9e6307c97e45dfc49c2b044b0538c73ac499.
# CPython3.13.5; geometry standard library; algebra SymPy1.14.0.
import base64,zlib,json,hashlib,subprocess,sys
from pathlib import Path
assert __debug__
PAYLOAD_PIN=(37081, 'd1c74ff26522811c1eb81a1b7cae8d0ecaa9e57f32a06a7ea1439ea730bdc5e3')
SOURCE_PINS={'axis_trace_geometry_v1.py': (23071, 'fce11750f4e377851cebb39fd565e6a81bfc0e16c02523ee7101d55a6ab874e6'), 'axis_trace_algebra_v1.py': (7801, 'a67520914fca58e5d7307e1956ea1cf6545ce8bc70cb67c31238ce8541ce08db'), 'axis_sharp_constant_v1.py': (5408, '0a5103ea246accd62a4dcb30296236d168fc9aa2d1a04f196151e87a4904e352')}
REPORT_PINS={'axis_trace_geometry_v1.json': (541300, '21b8843385cf30d7c6e03ecd1d2f666c948b1a0542134bfb71c7c3c711ec0d11'), 'axis_trace_algebra_v1.json': (277590, '132bdd86db6290e0c08463e7f2a35991b68ad1d7ce14ed8a009201d7248d09f4'), 'axis_sharp_constant_v1.json': (5715, '3efd2b3deb81d6a58360b04fd6c4f2580df6c2c6c0a0286a6204a19cffb251f9')}
BLOB='''
c-q~44R_l%vglvo?w<2RQjkqb{)i<b=OngMr;Ss`adMkgv^o??+p;B*AtgsrZ~yz94}b(IInB0xZ{N8&tpyUmU@#cW3<d-6*S`nL
aX!rNf-D_|$t<4-v-$AR-$_@0@BaNC*2&L5U!A^w`{Md+`2NN9hbu^&4zGUx`Fi;N{KeJf@cQb-$=UFu-?gx26ikv?Y>j7kaW<aE
kwtJ@@$504Bx!7gaW)^{jKg3a?|h#9!#Z0A;oM4tES}A+U~(IevcSsXc`%;EQO_FBb89?JlMF#+!F-&|f{8WGlSwd7GDtv66D(?t
0RC43d2+d$-z77vv*UMm_J#F+HN9L}{*J%5<Ly`{$utdS0LQwGlW9E9R@P!Ro--(Geh0r{kmidC;>S%}`D&W3tRT1Y&$F8>nF7A^
yUBQ@P_r)K(I}jY`#hP6yCBCxpJzdyL$9sjFp5Wu+u_gxGFkb~aQGN!IbbpzO4(ri8lPt)k%_rjh({5MNL+}iSj&6|P#7hX+-{7l
%$i#Z>(L6W$hxqm*1F+98<X@dkbY~_yOVws8hyK%%C>968+YXJZ|1rkD0&*tq<YR&4yQlQUX3I?xqDc2ui1w8ZU@r`MtWbBclTO*
u1a<^3@S%|Tkr$`Gg;JY7KL@atjRB^d<W}&p501#^Q=iI9JbojddqKf%ZIvM0z+@JCjK;^eV)CPHZ^qE^nI>&#I-sduGaR-dd)r0
+4T>K!O3^xCGbUL=R48(=Eer{37{L$ss%|`y@f}33s~7%%Xi#YBS%W_n=rDiFfxY;<=P{JV~?5$En{d|oWp?Mz`RH@00obW3C>CT
)kwU`pnYevMJU81d!|rx4<Lb1VK8l?lH=Yo{2yKd_}eUrN3%Gy`waDVAb{~o$dhqCw|{sEHTwPmj1K&H359_FVcMlQRTv$oTcDD~
Q$Tl~+{Sa5{C2vNFGjgN5-%NRC&-7h#Wc=f3e1wJ?ex8YxD~3y(_{n~T_%$i)DMGM7*A~5Z_XX;&Mkw1Ik8Lc97oJ+Xl5}^q&Ttx
&`vO!fE0^wZgLyS0{YLy;elu$9f*VWo;W=0i2c21!iRUQX98FOx|EM^XSwXdB!h$<I2QIXz&_RiTH_ll7?k8+Ozq|0<ccaR#R{ve
$Ei&K1^w;&-2tNEf1dqQ8ncB4r%7|9K9;~Mz+uQW$RjX6frtLNozZae0+rgWf3~=sJ)$bj3_&|hNI(Iut7YwC7Jpd;6A;N!nv6l}
j*<n)Ba}%fZD+}B7T<!TeT=Or21yMsK@y&xvdmbxkA=*@^yk?x(!Ohk^fGjMpYSQ7rwB6NNfJ!1{fn!rW2NRN{qzV=&hF{y=b1)F
SAd>`&Cm^<N=0}ZH6u52HUR`6B1xVr2zQL3YcHCQC`WWDMM2GHK<!<m^}B)~tpbw6y!R-8n7fODj_*;WSxGt{PseN0Nmg<Lsw1}M
UlZT~m{#z29%o^k0!4$l_3HI6XQ$Q(B{~s0SwJr786fQ>$ZliZ?Th9Vx#PlJyX)rET|?(+lp&?bzD5B+m0&hy<3}1R2~|ccNT3?Z
Tn9m*sJbAo&>6rl>*fXW$cSESl0?ZVYC)`>7V#idt2bF9=C(`R;GrPYhdj0}Wbm)Hn9BHHZEK!bFjL1jE8w~LofQ*5g2JDLcX4ig
9fR6lkhTR?Hx8{F_%w@KS(1Qhki%q4k=97EK*Xj_46L{z(j*@fC9bnY3>1ROk)~?k2F=)w702MCyTBI(^W;;Q=JnDz{Q@XNdJ~ys
lUCRWGs&-uE|lC2#A7#r-}pC}|5Fm&ak9u6sTMU;o66fDtpSR^6#@-{Dt7@b1!4;A#=kk+p;Cidg2ubSlK{jT|L$Vnoox*>cmii~
9VvH3BUJFjRt3?J`xG%9t@2x{e6!4<N>B13wF#<1OGAL4xphQvbdd81%azF+E3}SIQcx~(1^T45f8egrvN$~SFaefL``OVmOzwk$
aMYpfy;jHD+rw0+)j2xAlB?EHrvsM5s^xc%jt;=y2vfPC^hkKGP<T7vqy7N1C$;^p2vaDsMcJQ_w(mUiJ<r=agv7JM1Mivd?;o}g
yo2^3{5#r%ep0WQBxJSTWY7xEAZ@q4QZLZ7ef4<;;@(Q*$6#WopkuqAXBPZ}87W`cp2JV5=t5L;X}{ZT`GYQI!~gEQ8FC4*-51#m
tAV9)^0Tx-*|t&9iq@WJ9dfEI_Jr?ni#WZ9BrdV#5vUv8^du2?V`^NyvV8-C#cToU9?<~VaT`}E;lJrPlJ+EN-i@8zcKLd&y9am)
DC0c$x|2jgsw@*v^0*7F7B3a?%Zif(>OC)?p^-|@3G2@@?%ZgY+zc}t%p{fjM@&=(rAaglqR0kgqX4-CZfdTOrIvjkQ~sb<112-q
U_{rlAGo8^%2`r!gvr&Qr=U*9GkfibX|RN!8oX%yXu?w@LKL2R6<X9Vu>D=cPT-F>aOz-@U2QV8#InTIRt(@dbsnUmiVxSaLZ3>*
YXBzzOo(7Y$El9jS`(O8z!grEzVB&Fva#I4s+>0(%W5y6wSCccMC+B^5qpmCFtv{<eA5yB0i}*80nF{I1m!p)(>$d}>m85AKr#I5
4~~7+Xj@jgIU0-6*y&}p*V!1s^|DUwb-Qc@#v0`OB$$q(z*=@e$S!G^TF6?e49Kr40O(>HQ3iD{Dj5XL9ziCj>PTiCrx*i}hjL5h
jVjp4wyZW~DPW;73do{>vVaDvq<m#J+B;tR+2ON}*V#Wf?CkmeVSC?)pZ$Z5*FJ1G#~~3rBx3(w`J+Y^zOL2wU@Sea%4^X$oHJwL
ACXBIoDrnOi41Wtm=VKC9L(%u3V_%e=VS8AgfYybSH;ZF=NS~+UJ9Ek3jT^EADk{je&iL-gLtIbzcZf4Q&`;mwjGc?U!;>*;7ZFW
0QM`87|x*5)g|^O8Qn|j^E|kfjqCsVd3f^T?ayytpS*Z8{CIYCefA4`k}h9dpPbkHNew}67g=$Xh*DBprS>1f`Vl$^%W+}6%=l#n
(+TG-&P!0f<6uJXZyhnJzkBJJ@C#K;dGO>2y=sQVB9WdKe%SjTUJeAT7RQU67mKiNif1s+ec;GS!KW9i1GDj)@iLBvdPy?eF!!<j
`b$UDYHgTnSgZcB(&v*pN!W%EC&MZ=PKX>NF=b6|8WzhWp4s^--vK-y!4B!L<4e7OX+my<#%M8~L=Dm4r2$T-EchyI^r7uUVD#rU
GaE1yGzoUg@F8BYSt{~44Kj2E=F$cbqS0+QPP6g(^Q__Q#IrDoV%zDVyH28$uE3_>M!5#8ZeSy&LZyr4cfO+kayVMeW3ZiruTY$9
18omrkt_}(RRX#Pg+9;H3<tc%>crz8-oAeK;Y>04#fx8FUwpU##()35A&^ekgmxM307={X2lQ^|E?!3C+c=*SW&bYNT{{QUEgmX|
=^yac;_~cLd0q3{;lt#g580ReX!bbY+j|qe^ut%@zg%Y5!h&jm3Kow#hx-RN2M7E6hk+OF?;Ux22j1c6pzU|UqZnl2VR&>H@9jr7
;oec$9)Sft^7cE=!oyAgZ;njoY{fUruFswYd}#$h^*dO6!}5=ohdpbCOX?KXg)oDz-u|$~EBpRC?OQ4YgPP3~SQ_X;X_iEbaIUha
Fs?c$Os1pnaQK?eUXWS&6As_^PdR*9=+EOB@V1T9O*|IX?4^9qjxl=gLPl?v%gdc8zRluzNbavv0bK3?XRPBa=|Umf6R>6n&U(~V
N}7BH(e>+D_Z4bUJKRZ0b3@{b!xHLDkYRPX14NoCe^;pVLLjOBPMD-C+c3rM1=@L5ObeV~9^12uEk0Y$<*&b$&qgzW);vaWUF4y(
?$7%712Jp*^<wz%CwbQI-Vd7ggK(Nqu<3UPo23AU{!ar5KRd8avwvc1vKhKy4#F5iWo*L{^f2QGrvwuq%|a7%grsmcNd)2#Bz{1R
oN*&ui&jj`XSQo|x3EW)OXLHhIfIHJfd)7Nbe>CPRR6<z4Xl!ac*kk`GR{Cr$KzRRp0sFaK)2BTO}1dJAFV)*%m7ad7t%3I_Ao~8
331De)Q}7|$FriP7*}K?#IQ23a+U+3dfNv0Cnl3><Qu~rm&5$iH-`C4{=~x^!!ZB!)G)858o=0bDHRI@>bN#}#O=66kK6g<tmF?h
bj`IJ8jD9ou<v9AHHf+v&mCnTp>`t`wQ~<@+MWif4TC0Vus4*~rv3N`GBOxVVzAh8`WMxqvS7K8!_Ww7aYz$c_JI_rwnN2`G2@=o
zM9SRT6LmohNyoPlZIpp;##`g&=DR!_sXRi=c6d%JSjIaH(LRYA5USKftVKD?;zrFFl9X}3stG!vZj>3qd2!TrbcGSWJ+PYwBt~@
C15UPkv&S12Qdq#u~3p(0L|_sfXvg$cn*mTQT<-~Y1njfu>$c1Cdk2Hy-jAZ8rbA3%5y{BmZkbOG*gA9Wd!ZQAm%v;Et*3Br(1D#
gb5J63j$#d>!!Hs1)-Y60oaM!g!_l}Dp_RK$(x_wpPd$~^Be#I#mLPKY%tDZYt%whM4*NaW6<4cwwR4)w>wpEBl(!aa%yw#-<NZL
Z`-8DtzxOvVnKy4(S9|1)Vz0g_kckP1y`@Vvq&S-NHBhq1`&x%+uPgc5Dk@6lwvwbMd-~os{F)sk~Xb6?0d1tyo>3kk5A4PG?Bk{
f)s_ijVL=cS5&ozNs=(Zj`#lheil7JF0G-w1zkN|&=x9WJZ*J|PqdBwASPlhU;>FRA`o+NB2GmPlf~H5#;xp6w5k1IO{_Jjh1B|D
1=id;u}-aAFR^KByN5W){y^)*_rP+K*jfNmxTP{nX5%mbX2cbcuo863@`HtQf#M1TpbNS<j;u&};%X^<#j`J<fzbWbdx^ie`{aJ&
j1PK~>xJHnaz8oEJ9x(O?kBw$g=vNC=|ZZ~Sk|>)>OHff#0O7)U~UeD=k!iJdAcZ{xy(CRu>J?nJzcauxTjE7sh4+UaVZPeTPe62
IT2?_#2J1XLK4>1?_lom*f;{}YPS3^g|?LMUE%fXr>?*IAi}QSdT6e<?F+aM?t`N-)IB!<=^p(tNM`S+3}_8~bx)_Q4^#MCzN(XC
{k<f)ElKjANU|<SQgGLV>?>lU9qSxSDeIHWR>Hbk$xpkFPx8|zPeQMISjyXdtg+J7s)d|n0|R-@kwffswQ}h-y~OuAQ&ASgOPP=F
-Qt<w;1*!%;{0HYDAJd<OA8wJ09-jxlPv{8Ptu;t!{&I{1?z@5AQNQFiSf!Q)4XFz^+gsVbD($bo$y<0u`UJ<bG|iT6SilPVKI%(
VH4|e%zjSEFi|pLm&Y!MqA_nDS}$?)u_h^USb4@4n9i{px@^fqhd=g%yKs8hN<M0N@J3!Oao-Av?zFO%Ye#Ojq+KjFS5+>H5M6@H
;0Q$;*^7c1mhKjaSV2K{nrdUcD8`b93L6+W8o^>@-?)f=IjCo4)>$p<qRhG=c34!h(OX+Ez#I2WJ8|n=VvKT8{DS!*5)rTq0BT*}
U*jbhuU-pMTN%P&ymw`tlCdfbGbJw=`?)?<nB)_%i7E2ljmEcSm){wpYC@uF(%ia_>rPyEuP&>$pui3~L;>0<v6v7Ru_0xMBZ*IU
tgCnujN%DymWR7<LhD#s(e9gQ$2tX@E1X-`$Fg1JQD96!7+E!2?k-T;WGgLgh*3dAgv3p&7IH~zWUwjamAQ6^OonAhk~E|3j9Ne}
fWoqN35&PZ$YfL&X9_x$SYZi9VLP8rD9qzYUae<u@au$%EUIE`Q+Bmo;NBK*CSNE?^=sHAE}l5<Ttr>P(XKsjLSpU!uWj8I-!k|Z
+`!_hV7>_r{M?jMH0C6s1X(6oGMRv!I_X*wHtp|Tt(;>Ss`S#?(G@RXU5JhrOZ$0q1Tak}F}zbI9Y$1w9SDY8EkcE(EflPiRDN-T
-f1dR*AAL<5cr`yNiopsB!%f7$y0hbO%>L_V*H42p#-oRm&NBVAR?D?0qnt|@@l1r*l$J=yl#e};++w5gl0n!XTWI@ma-}3sM1D-
N)_ftiVb4W$ZZ(mqAFk==EJBgQ#6k{6AC*T4cAuCfP+<?Y^8eqDwWh#mpgc#st&s*St?BYDt(H7&(msVg?lLzLl|moyCHK?3VX7U
oxcWMPt3dCZvfAe7xkAFZ$tqHLA2~wX%WyxNq#8Jrh2UluLUMboAK1KGz+Fo^U)<bInEPi7flK_x+n-@JVUqra6Ah^&clMTfm?Mg
L=0yP8)9n3py!NQaofJ|g(rL{K)+z=af;vJ8+^Ap?ceWQsR&}*_k6JripbWDI!YSY7p)8L=~>MkXnSoF@pqdTvv;7r^Qc-qhE%8H
wLNjLzkhJ#z?^=eL!i%Fu<}~O9L{W=<ntig*(Nap++7LsxrNczMJV5MuskX13NRn1S%T&b$C{P#Xgiu`b9WBL#k?8vQ0mDDui18q
oTk<Xb2MZ$htw28?qUrDW#<@WO0gjByifyWey;Lz6skP`h=mx?0`j=Zqnj6lSCQ0eoA)lraA(bK@MwgrXBz?}ILu9u-4XEqTI8U>
F<3Bg?UUx3MAQk$aQlSRFO3+CRfNm~894QdCB6n78K7Z73*cet3ZUlzIwZ-6UgWh(fvsSl;!?K&9}@7>?ZAnlLR^4E3ingO9vfl&
33CR(_@C+?oSJ>$MxN>eH4|Yop+O?}OU;}TSrB{GAU|=Ro^0$y#r$zuXw`5_k^cdt5P25_#?}i|niQ}>BWL(DC@ia(pXezpBx0Dj
Sj~OEgN}2^8<B7JF+fLY292`Io3@|f9Y3k~TN|AZIZi`%X*kO5S@D?Fy>;&#p{r?koawOH?hmBykvB#0X0kvRsrH9sqZ!O&XbvkH
JrAK27v9O^c@*CS&{-SG_8SPjF%Z0OPQIQTR+SYOtXH~TJ@&GCCawUy-%wQ>gQoPW-uZ`k#XGMi%!X)an2<!64X2BMpfrF$%rLd-
j;5{s@7;E62$plQ@vU9QM#02fT6=jLe|8J91Pr`34Zuv{F%X*0G`zTOFv6gDrx{;Xea7Kk96lIc<ME9(9OB^7_TF$fg+=Oc*r*0c
{n0IPG6jNpP}vvPPPad{D~_RiTQ<d&k9h0GI8>?Ziz7y=in%$C#j1PbSWs<3@&@_S4D;g6o8iw_*XJ+ZUcVo{JiB`P{`&0oTVto3
8m(`Y)5~w}mFwd^f9PlvhbqJW7&$*mqLmdaqVb%zv|mrBaWqDQJpB)BsB=*N-C{D?ohE3HAcdzikMrUnl|`G_urk0C6Cm8s>p{5k
_B!oj=Ln6;1+ZF}MEV$%u<jF>?7>9nkarNYxQDa^KzJIfI7gKR;X`m6Z|?J}lVMo|t-}HY9cRobv{@g|&_f;3J_2v>|B2mv-1kG%
5-Wbk-o4(or#<|wd-vMG9VK%+5Ti2o3Y3+-bT`g^V3{IZk-`cWqe?{zr?Qu=?KQa$#<qo^YpZoacUi^}1*&M6C3#+Hzz$%}x+9p)
tpNT&${z@o^6;I<xk9CUeCKnn0vg5CS+HL;Q0_iAhVM0^7?^V@zQ*I*JJ3tCW1s|{e%Hs?-2p`+T+#-Y%D@wMZ^?Say)N~#qF%Vy
Na(L_+P@!A=f8?n6HL_+myWYbrTE#Y?=E$Up-3i=aR;?*F0#8KOd;gW5d`UCo&#$vi6n5tss$fa(6g}!fDs`QI7I2W8wq?FVlXb}
)Lv3iY<f2;woY*Fw(W6*h6$J$1zPY%svTO)1o5szG{;?=i}uF@f?7NP^l=$m2}^!J)E<j_@nG(-(a=f_W6gwJlj`BJ6}yK!TksB;
^r7Y%STz;=L+^E&5(BXL#-Q@zFD3%0disN^RWhdi$oNZb%j@gi82#_SJy6Mc?vui#ZozZE1#C>e)bV5Kk%~%_)UIt@;cK;THQwwU
MXMXnj5JW)>0@+pvv}rcV}5InAF%eOp1%aeNBSN{|FVo;Ud*D3fk-6hc;-@e8G#p2RdlM67d#J9vRq=+#3c;9Blz(_Jvx;g-x(gE
nXT-Zvt>sZm>p*KjO+FC35apo=U1uIimc+u-{qhJ6!++<v~%noW1u)cY~OP(^PhX&nM4WK^2H3NS}W3xwhRGBuZ#whnPh>mW_A_x
YS<A2$EM~|dPeu7EJ-Ccucd)GmDb&0l-o0y1h|E?j6q(l%juwNAk_8WBtkMUf`!R_9K!sBwP@PM%E0;qp_2Y!;A|&dxC$q+<Y^CT
rvOtOG8_PNoT(N<6*>)#=~3qw?OLV-^gZ^v^kPSa^q3Rl-jkd+21Z^|%mqCIDHulvb?<dy3Q)3p?^UKP@UppnQ4*VlmI9>$h}EN*
iDL8P2Fx;`H$efuE#tlv0LpL%y*L7su9z}vg8e$C@(2TAVl{$S$`XA1O-h`7mC0npI^B$gtsyv7b|PREp~>ySI>6R*<5-%L!`UdS
a2&JBDq*u8)KI`WR%l|IPE9I`d#&yWQT&5vN}H7Ef-LG1d7c~vl<0V9wm)#R0KBQ4F2F8PP!FKeE(5w5F1e#}+i|vtw-)|TF{g=1
rWpXyF=lh*IJV-bg9hnAn0`a%F{GN@qga_fWwEX+#~PqjWfQ4yQs&#EU>>Du43t3IHK5fwSq}bVG58xC=yWR`-@)@Jk4`Nt%%qHD
1)(Peo<$z?*qF}?HA$`nIxS<_Y;`$8Szlmbjdd{LxD;E8-3OJZy^nOBs`n$BWgeJiogRkn<P~ka!RgShbNp0qtNgl=-~DFbk1zCS
JFTsee`o|zKH53-d#`_+!2CTnW%{VPp5lgL$dd_Kb!?DhpGbI)%4A4MXZK*UvZ4vV&_|rie;=C?ayH-BB3Xf(e*{5Cg<V*^-{3=l
e@6Hxgg?&i-nLjK7$QA;$ruCxriNF{QWW_pSO)wEGrxx%RpdaUg22@#w1NOsmQtsEMZ}NdM_J}?dVqKnN?r;U==4{x&{jf-Wdyw&
DydJe`thI)1Fe+Z7KL~-e2np!q*SaeO7SC1q480E6gT56pAQ*p`J=d1w!?DwV`*Xh=m?r^_@}VOr!g3NvvHW)=VfHydB4G(Yz%t0
_;d@2N7+ZFNyY6JJ)b5Rbk#>Q$KSQ17Eh#GQpp<=1ppH6je)KWrc6wezxP4*(Wj#qP`&r&GqnOH8;BTcZqWN02N)dHLkC{2H)60o
(gUFF#GRuR3N%a9YYc=+4iy?TsVhkiJi;8KY4V73@R5v6!5Q~DV~iOXJzXC@EJxV(Z@4T!+zo_&tAG{n%R)E0(A}WolKlY9{U7p7
dV^!H_W>H_M;{;GLp^?M^W&X*?7-uOX$l!=Dk(~qa}AZ}_QKMmrHH4ZFS|(jr|QvYG$|BzsY79xsv;gwq0ufX8$%_qfU|AN;ds+u
j4^~)LtqqbZY-<j#s@MtmIGb#{gWl%>yn$3Pt`q_ibMkYJ0zyj+=_2R;eDcm2t)F(O6tGR<<u`txvhsT#3Y=G+c46epv5e#IC(hQ
syI0TE!wGO*_0RadTX{^KBju{h-;w~SB%}%Tq#zZ4yp1Opzcn^m(me~ZS^fM_d(y_Nx5SN%}xx@Y1&^ZIbVvLx^_lB;<|zhI*z5?
FSGa-J5<5QTpDTY@-RSL4L1$rw{%0Ju!fqVFrv<=4r?1g;n8F~TINaXu?VUhlA5A{kAIA+C6HMCaq}M3T;PtXv_<SP=ZTZ%>u;Si
U(5Bz8S}MvR%PQylU_uFv71(G0@L0|!74%*Cih?CgJZqvsMDvdzu~P*>n=V8iUIIomKvh0w&}Vno20=CP@azHXbM5$clY=Xg|B0-
5O7<(4N{{`+u^tsUbItpUGnt7W(320vVVdPUzd<J{DKO2y5Sid#TgJ<&}n!*!ZXR#Z~48jU_LzZVV)-XJ%%&vse3#v5|Tv~@QDv}
Ub&ORb?ti!-nkpMCW+&^4^KE2L!f4P3h2H#0(9?eco83P%esyMB5%Y%2a{pd8<b?@TUg#q<fXdO07JWS4>j~<#k7YtV$GkSt2))N
ekg_l3{8!$f>t`VdY3w#>fnQiI8Ha#UjM&&oV2@Xt=&!QC*4h@uW75J36=}}34xgK@n+LO<Y>em2jA%)x>xR@`_eshzv*5^u=gA8
A*8&H%rAYseS2NHiq<t(k?OW4C6BK*q7k0cJ157HU0d;RNuVVda-41qfDp_d+e&UY0Q3NCTh^BLsexrxZJrz2IKX&a!+zFh#=o(S
`@JTgTrv){ZiBACQutc8`BB{)K}+3_u+H7^JX~)$#J8*>dyzDRp1F)hA^lOX29EFw2XRm_PPZ@ps2V0zO%lJ6Abo-VV-BtbK@j0z
x*I~Y_v&|6l<PYryE0X9LlQ_Z5?@4A*@=nd7jlVIcU<)SCdI{p4@*2=(frbTSWzO<8@rQKPlvSYH(@d3JD^;>0T?@+#2o;-Iw|e9
6=%(iIuA=O{;;C5T;N=q;<EP<S5+TjRrQPbB>ssH<_fN%Dgo<G<VS_VFRJ}ds_}pJW)hnE1>5=5o6Fg*ec*m{u}*cZi*KH@^*&YS
@351?SmhZ}Y`k9mwc=DWW?6-0h$~HI25zpg^KUv(B*`Kay|MfiH>taNr)Rsz&_s>2Kp!g&(9zBJxGeepN>cp4>7!-IytMRx2Otu_
Mqi{};D@VFxu_A2Ko7TvzHQ(1Y8y~M_FS3kWJPfpWQigamF*R8SGiX(_mO9=*o(){-k|R91PlcHPu@=aMQ5i|T<D`k7c`(fGN4z9
ftyk9J_zN=%{}-}Eeq0$x~*ex+89#NqB+CAIvV}P^!ub~u~>sPkTSbBf>J)FMl=z2Z}hBv%`!VJp}huvP~Hp>)Wq(^W4U+s#;|Jr
76k(57_>;UiH4$S`@18agl(f@oYrebR1+)W(--xmCnN8i;zmZ*+sLjWq!l6@%&L?^&wzF#*1Xp2q9PLmA=Dgu^B5Qtzz>@JG~JZB
6XUen8v%tu_hJy3#GT}xaXcCiM|+$8MOyYiqgcn4%W8oDoo~CC)nm^A*pAf_>_I@25}B4rxyvR6n6sKW0V{z{w7R>F{SCS@kecd$
CjdPRnz>l!7%l+ScU_LWb;Sb)>e#^e?ni-tQOZ%Gb^#8)G5{c>f}Awpz!Wtffz6~;`=jUDpm~Xsn3{MiXX0AU`I438YRFR_{_vYe
4D&z<N@AoGdu2xXuI_dyd~wqB$_b4e-8pib;h}p2U%j7(E{Go`^j3_g0eUIeOPQwiRyezGE>@=I79;0>+Z{b*J`rtfKDC)G#nn<|
D{-|dJ)nK&MVykaMCuqiz_u~+nirjA1a=XVT^w1yl6@OMQ)G;=uZk3zY0#8PWh<wO<Ylvu3sej{Wxc;_+9Cd~FeDbQH#L{8SH-qG
UcWjFgFL2g;VoE+F<Rksl%`ptiN(RPjWYju<l>@$aH68)g0Kxf+fl)?QJzZE2mn@K-38wuE1zctyX&qQqSbY$ZLU0&HT0=kFOMqk
6;LB+FO<^2go6vCznSmM7*v2F-iR}CAq`w3-JAlhFNAAM$61zS!$z~LS3P5-j#Ko`<P(QB)ai={JfVSB8g!{VgYiJ8-5yru*$dSn
=yat6CB?J2Vd8=1Yh^17NTLppb2o}7^FSTbV|GINvKYbhC~E&r7P#`6k=p5OhJuHm>`@C3kU*ykD5DA#?i(M0+SqC%IHoGoeN<;3
8_hfvZ<<t0obj)c(c(fqa#K}SU`ADJP<H;WXMrkp%LW+%qroWLAbJ!@I)gK6sgq}0=o2b?J&LwbiB8)!kU)5N2niI@5eA1&6yb48
q*7>bo;m?U`49T++LO$;(F+t1yY`6BW<eF_c~m|wo%%-RUq$8LJJ9#<9_r&+`LO)1Q+-6W?>W+Ej*NK}&gh7~(Nq(-CVa~SaL>#0
Z~s>Wm*3=*VNae*YevN(7%KPVfwTwW>dIL(<0u*uuiDn;A+${aSfL`*NTbgx1}1#AviUdy9)idcC{tPcZ|EMWRCtg%TDL!`{fhx%
!010f?-{~3Mk7x1@g$jnb<V}`P6~`~kQ|=S-|NEK@KRp(yL({pvmHT(F;#Q$7GO@g9C;OpwKkGd!Jtfgg8&vzgwpE~;?d!AeSCth
!N5nlI}DzS6$SU5ijsj!XD>Oj7>aQhwsgGK>Fq4Ioqz_%gQd-9nb_MQ+I!_Qn$)#dZyRWP+tiK$405o2Ko@_oCvVO!;Ax|vY847x
H#RS&RDCojDXrK5Chm^dCf^kq<TU}q2+93i`o;bKstq0cQ@gxG`zQpvO|;!erXt?$3AQ4oJI;piRPdQ^o^re(MK+ffP>9?l7>7x<
6xZ|{c+h`XTmdjlZf=Ii4Cpl7*2M35PpWl}_lQbWS6NuN%6N2f!T#K<`e98l-8L-e`aqMxc0cP>odO1~(-*7Y5yWEJ8!y$Aua$Iq
Cw%%>AO6+B&?kKKs~5>rKG@b%$9`+4e$}DhYD_fG0XzhZvj7hP^E^;HB<lR7`r1q$e_7zAWcEyyV?jH{wP@PebICNV6(c^v3wF8m
?YC~5?tS-l(rtIvY<vICh0?d*eVuexhco&^UoGL0BImH{QV?yZ0itbErIM7LF5hE;A7#MdBS%WMl$koLof(rBN>Vly^U;c+az&By
LgHiIP4|wo<?+>0r&q`N*msp9s!~y{q50H%c{3aem|XVD6O5I+TIfQDhOis{?p{N{U*DsjHvR1H`bY5F_W0L-w%gu^-y<yLn5QBu
FxBx+yV23m4A9SZ36e)YNBr(!cYiB5W#b^AeFLj4fDWiYXSZF2qik60U7KneV9F}^cW-OAOiOD!7F_?3>hJA#2(SI8fDFGXVs}*A
d;cCJEuOU5Qi!X9#Ef9aAbN+uZ6CENyx~nygV`}T0w3B1U<TQSx6bD2SnlQ~c6&9vJOzTmRRHlVA0dxjryvj2=KH@;Lb<Q(y=P(%
EIt77Y<JHu_+qb)nY!1v1XuwJ|L<>r_Mds8?H?j=NbW*%8%REJjBwjT6COc=25F*_qT#;E={yN0D#2&~d(7mA*eApR;XT{!P!INY
eZLBeHwwXU%2@S&H;ee&27!W&iVHDHDdDOA_jeBp;&G}{{SKDW!<%H0l}15T(s)|dcqO!>qa&SDd$9?7euww9ZU^2r+feAi!|o9t
SS?-<=tkjAqa!p```;<gU&E8O*z{g+s6Tv`8<(fOpc9S71p=)s&SU%{P&AJ7Ugg?H67a=QKfEjnPef0_xQ?Tp+Uakzb+q~oP5S%m
5gk8(ciG8p8lW3;40FUk8C`n=dQ2%UQ~5pthowHi;Z^1zf~0%`p)9=s-vbAoMzZu27&g5u2ea82(r9Jl92O;FiwcD`RxzA<x8VFK
!~eOQ#ml+9q=#~c1i!U|(SF5}iPlW|uHXRHZ{L`ZdS03GS{XDj>Z&hwsa=_*l`i7&Z|M@ks_tHVXHV+-$2pel%~e-$2!u>fbbop2
+#hUbWt({!&)QL<qZ0=@@k}TDgF!uH3D&p##WcLS#AEvt6OgR0b{G%c{|ZZR7Wx7~@&ibR*8G^z_oFCtx_W4!YADw*qq~RgJ@E{`
J5fVLb7Z4xtSbcAOb4|1aps6`8241x*}AU7V2*Ds$YAY8)wfnYuWqB-{X^mV;$Xn{pR(zz?ox#wcElkp*Pz$+YBpDMHmliOt&TeY
D9BOVw1goyMQ3}(VAQ8)dE~HJGJKN<w^`IGmwAsMZ-&NaGnKgaMCyxV6473O9=d;6ANl)QNKPvU-cO+3?6y_j>W^m|rz5-&4?p@g
nOHwxz5e0#+ZS&vy_=>%X}^Y*%;@T<uXo8Lw!%q*i>0F1#l@#P)@w|SDfVF|3Z0_C!TcM8{HDN&IUY@K;ifo#A(U?`h$pKZ>upkO
`k`8iZew*M-HOJ+EpnIAHK`{nJ5qQ9Wa?MnfvwdW$<%{st9Ol4pY}|Zzx2}6zAqO5^e+AK(RXS)Uldhp2V&g{lsC%oQ(*w*Mg--h
CoX-huJ3}$jRwVQ#yQ9KsCqO*)4B3<aeUvPX9me21clVKhV+y><QtJze=5|fxC^=(ySOc&3N+TYkL4I0t;;~X6^6pDQa+UvfT+V%
RHV{5Bw=(%lH*MAE|y|tU&aW4$RCX`RKMnr$1d#P1qP^NwBH(!xs-8a>V`DQ;|@&Z4}hc4e?w_#<h0CdQ(l|$+C}&t?U5IuT@)|I
A-s@06?ps=?8G1GOGstLNtuDIs5r47u?hAZY3Ofd87Iv3{N|{DSZS%q@CW7nbC;z^7~_TV<N3;Z90wqA(6-Z`+U4Vacy$B|0gzLV
@yz0T#?@Q|GV?R(Se$&t;acRMH878WzQ3es0jGZONLN0Vo%$v8#Ds^YUczsY-Gij=p?y-glIQ3|o^Np<dn^RDIcwdj#aa2x*GDl2
wex0IdutsMmYheu!0fYKTf1t_{I`^OVPqOnN1(4+6(eeD{~N?OF|FCnbM4qJ<Pji?>Ym~o;K%2m_MqT(`&_w{&r4VGdFetfJ0>dq
5GB@Ij+vAfN`t&5YDz#C$tkt!!6Q`in$BDizw;=|x7&`86#8hmaiKiDpfLBKyixwxt9|V2$t&em?v^uS3;e_m>8#=tHPwsW4gY^d
%@zkre#a7i%6nn%zqssTlmM$|DxILdS>n-diBdhjgy-s}iMAk-;dS~uw@o}_-{h~-YNmerUFB9eC8zpWL<|3A8qNCyDvb{o4|++4
3`r?1T(BE^j@W*uNKFA2ovA27m?7U*glS?ZyFesL#l=PH22!T3+otKpGgM^H)uA+{_?~;JOB=dQW4_+5e+`7<Lg(HTsdY{HepB^g
m|gx&Wn0kgX}zhnATR*#sg!CFZ(gaqctTGa05C>0tU#b>XNT`MHsZ2bqB)>$bYx}mA+197^5LVm4t;2@Jf-uNKSYMtOX8K7z2dqy
qF4#&iJ{cRi}1#CPw#Yk#a5@UU-{})buY=|4Y_ll7t6>NnBKZgCgrbQw@;gKKn+fH2F4vF=UQ)_7kcY_i{2`9ky1saCi;_#h<0(M
TJPdsaVgC8_aT*F6vfI!HuTQ)oLpyrT1U}!0z#D-R#esUxO%A5C|78#jgy~SKZ3#&HehvB$AB{{U%4~B*JiMlW}u<@kv#puAgOb=
eij9CK%`$w#X#Z)4<X?*GZII2VtnV2KUymr#%BJ%+KsKBkC}y&1%CNTHqL<SR+e|HY8*@QeButf+G|Hfy@ORJ-P)#(olaI(FapDq
zEDoF?rAU&?{*rc7QX|wX0&D)b(%~T)A;|1K7aSLI)BHp4`qOaZ|uImlkfhbh=_NFW{>ESaHKQ}>UaJ9fq2(H1SGN`8ZUBLdY)>Q
0BC#1JYi~p*G5BsZy-&x0oom)DrV4b(KMZwdQxGUHp4rocMXf#?>rcE_Xkw_=FYn0P!O*3Ok;Js2(l>Ox~#qa_tg0})M{l}`?O*W
lgg?VI<u);!-RAzqph_oyfltor~^=yV}C5f_ryL3@O@Bh!afj(@b?hEPh<9zg1AxrVjy>+?Jm`YW0!n_!%%pa>h`fqKFd*l?1mt*
QYBc*F6<fZKYS0Wf%lW~!T6AHWl?_Z^!`(}!N%=3AL+6j#P}l=`<pVnFo%o=orw>eueR9r7FC7S=E^<HL#-_WV>~V|tIngfm>VYs
tEP3YSUp}|RxAT^KAeB!01Dd*=YPajs2Bl%(So#wwt3C~u~7`uD=1qyT+hF0NEqursl=^N-c~9!B!MCKM0&T%$thjR)*`h<*%|i7
<DS)eZo%KCHFxdD{njJQHS53U|E;v1=k=^of9DqH6l*SX&f2C(l@RBjE%pq3{tv(Cv~d^%nR^Sax@$^b8Wt{c^{#5DD25H0g%o$|
a{rz=#j>lm=3gsAiuhWWC`_oeHlZrno6VN9to%lTX@pz>d8`@6PmhwUMYaP89<V{;9L-9)XEaJ;4tP{=V|4+n#nhrpP$!d?_M6iZ
@GiC}lB0#6S%3m`fqUc0&t%a?t1JUy^c@!eRv1X{%SL(HQ+}$vaXS}(v2x2MgZhF=7L0TK=^ahV28EHSfEB0MO1}P@Sh&^QLf$K{
qzBk^O@1z*MHm2(C%0BWXXWWyloozDE=(q%l!4|uCIO649IxntzY*M{x^M3GKUK8Wb1f;h^}n)VJWt4sS3Nhg8jdk$l^~*Wchs+i
4-vve*@JJE{Sz3gV-Wm}f~OJx6L)zl_T?W@GE|W=h3qgH6`v-RPdeQM8}gO1zi--a5dly%mW>zmSwdP@7)|oWp7>5@J@*9PSirkn
Eu(PjCYX+40m2`c8_|`AjsMVv-+ZD=3z7e2_kN#Te|Yg`_`})H7iZU3pN22qo(})(?DY@l*YE$(<=?;k4?N<V)&
'''

def checked(raw,pin):
    assert (len(raw),hashlib.sha256(raw).hexdigest())==pin

def main():
    assert len(sys.argv)==3 and sys.argv[1] in ('sources','build','verify')
    mode=sys.argv[1];out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
    raw=zlib.decompress(base64.b85decode(''.join(BLOB.split())))
    checked(raw,PAYLOAD_PIN);files=json.loads(raw);assert set(files)==set(SOURCE_PINS)
    for name,text in files.items():
        raw=text.encode();checked(raw,SOURCE_PINS[name]);p=out/name
        if p.exists():assert p.read_bytes()==raw
        else:p.write_bytes(raw)
    if mode!='sources':
        for name in ('axis_trace_geometry_v1','axis_trace_algebra_v1','axis_sharp_constant_v1'):
            command=[sys.executable]+(['-S'] if name=='axis_trace_geometry_v1' else [])
            report=out/(name+'.json')
            subprocess.run(command+[str(out/(name+'.py')),mode,str(report)],check=True)
            checked(report.read_bytes(),REPORT_PINS[name+'.json'])
    print('COORDINATE_SATURATED_ROOT_SELF_CONTAINED_RECOVERY_PASS',mode)
if __name__=='__main__':main()
```
