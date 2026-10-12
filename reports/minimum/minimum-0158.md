# minimum-0158

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# TWO_ANCHOR_FLAT_STARS_AND_UPPER_DEFECT_VALUE_V1

## Result and exact remaining boundary

I obtained genuine value exclusions, not a completion of the whole two-anchor problem:

1. **A full positive-endpoint joint marked-body local maximum in the two-anchor class necessarily has the actual maximal coordinate triangles ABC and ABD.** Enlarged coordinate patches are impossible at that maximum. In particular C and D are true simple vertices and the root misses both coordinate facets.
2. **The entire flat lower-star joint-extremal sector with G(C),G(D)>=0 has T < 65/32 = 2.03125 < 51/25.** The new geometric step eliminates its initially permitted positive-ell auxiliary vertices. It reduces an actual full-class stationary body to the single-B root family, rather than assuming that family. I supply an independent, self-contained rational-polynomial value certificate for that family. Its constant is deliberately weaker than the previously accepted Cstar bound on the already root-only family; the new result is the enlarged stationary-sector reduction.
3. **The entire flat upper-star sector with G(C),G(D)>=0 has T < 257/128 = 2.0078125.** This conclusion does not require stationarity once the actual two-anchor geometry and proper marks are given. More generally, the whole actual geometric chamber

       epsilon_B := 6(a-b)/a * integral_Delta [x+y-hB(x,y)] dxdy <= 1/64

   has T < 51/25 in that G sector. This allows arbitrary lower-star geometry, positive-ell auxiliary vertices, and overhang. The proof uses an actual upper-facet flux budget and the inherited actual joint-mass theorem, not independently fitted projection moments.
4. I constructed and exactly audited a **new proper33 two-anchor 10/17/9 body with T = 2.0286234686803257...**, a positive-ell auxiliary vertex, and already optimal greedy vertical placement for its own K,R. Its true own-centroid Euclidean census is strict (S,U,H)=(4,4,6), with no physical weak point. It is not stationary: an ordinary A-facet is a genuine quadrilateral. This is a near-sharp nonwinning continuation fixture, not a threshold counterexample or a mono-monostatic body.

The unresolved putative high-trace joint maximum must therefore have **both nonroot stars nonflat, proper33, epsilon_B > 1/64**, and all the full polygon/ordinary/root stationarity conditions. I have not proved T < 51/25 on that remaining sector and have not constructed T >= 51/25. Nothing here changes 34 <= Cmin <= 622 or excludes the mechanical E17 layer. The notebook's separation between those obligations remains essential.

## Input reading, identities, and missing dependencies

I read all seven supplied files, including the entire 1,112-line journal and branch memory, through EOF. No supplied text was truncated. Their exact mounted-byte identities were:

| Supplied unit | Bytes | SHA-256 |
|---|---:|---|
| research-journal(20260921-090347).md | 252134 | a495900d10f3208e5ec95235aa6bf0ce0eaf52d319b48ee8b9d39706cea7c5a2 |
| [internal-source-reference], greedy proof, part 2 | 18369 | 29b81610f3eabd674a9478200d167796866dd41458062ef843eec458b0e0b114 |
| [internal-source-reference], projected-mass proof | 17871 | 04208701b3956e834908a02b2ffacbc4a05ce01be9e36a1535905bf5fdc2df72 |
| [internal-source-reference], source erratum | 2946 | af41a30f6e0977119943bc9ecf98885ae9b10988c58ed93399f0dfafd0605de3 |
| [internal-source-reference], facet rigidity | 14798 | 8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9 |
| [internal-source-reference], hinge/small fan | 21305 | 213f109c9edcabe8224f12a24f57b7431a34621d23d1ef9867ef903a7d3a0ecd |
| [internal-source-reference], joint root variation | 18784 | 73eb04d63deeab693d29533819d3b95c4e1af3cc01d756987381aaa2bb4c2ed8 |

The branch asks for the old greedy executable [internal-source-reference] as well as its proof, but that executable was not attached. The old root-duality executable [internal-source-reference] and the full capacity source [internal-source-reference] were also not attached. I did not invent or replay those programs. The supplied greedy proof explicitly identifies the absent part 1; its analytic theorem is nevertheless fully present. The supplied projected-mass erratum was read; it distinguishes exact source-byte repair from mathematical correction.

The prior assignment is identified in the supplied branch as an unrelated duplicate; it contributes no two-anchor result here.

One inherited analytic input is used explicitly below: for an actual eligible proper body, t=6V and its own centroid satisfy

    gx,gy >= 1/4,       4(gx+gy) <= t+1.

The latter is the accepted actual joint-mass theorem in the supplied notebook, not a theorem about free moments. Its full original proof source is not separately attached, and I do not claim a new independent proof of that inherited theorem. The new flat-B and upper-defect implications are proved from this stated input. The flat-A geometric reduction and its independent value certificate do not use the joint upper bound.

## 1. Optimization class and notation

Normalize a=1 when proving numerical bounds; scaling all endpoint values leaves T unchanged. Before normalization let a>b>0 and c,d>0, alpha=a-b, H=a/alpha, and

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    ell=a+(d-a)x+(c-a)y-alpha z,
    n=(a+b+c)x+(a+b+d)y.

P is the actual uniformly filled bounded convex three-polytope

    P={x,y>=0: hA(x,y)<=z<=min(1-hB(x,y),H-l0(x,y))},
    l0=((a-d)x+(a-c)y)/alpha,

with convex homogeneous piecewise-linear hA,hB, containing T0=conv(A,B,C,D), and with a genuine positive-area root. Write

    V=integral_P 1, E=integral_P ell, N=integral_P n,
    g=(gx,gy,gz), r=N/V, q=N/E, t=6V, T=q/t,
    G=n-r-q ell.

All moments are those of this same uniformly filled P. No reference center is chosen independently. Every numerical joint-extremal conclusion below is in the sector G(C),G(D)>=0; the mark-reaction lemma itself does not need those two signs. A joint local maximum means a maximum among all nearby marked bodies and positive affine endpoint data, with all face lattices permitted. The supplied proof obtains this two-anchor representation from the genuine G(C),G(D)>=0 joint-extremal sector; it is not an assertion about fixed-lattice critical points.

## 2. Joint mark reactions force proper33

This uses a variation already allowed by the full joint marked problem, not a new restriction on it.

Hold the physical body and ell fixed and choose a nearby C'=(0,y,z) in its x=0 supporting face, y>0. Affinely renormalize A,B,C',D to the canonical four points. The determinant is y. Transforming the actual uniform integrals gives exactly

    T_new = { y[a+b+ell(C')] X + (a+b+d)Y }/(6VE),

where X=integral_P x and Y=integral_P y are the old physical moments. Thus the derivative at C in direction (0,dy,dz) has the sign of

    (b+2c)dy-alpha dz.

Both the determinant factor and the changed endpoint value are included. This is the actual mark-reaction formula in the supplied joint-variation proof.

Containment gives hA(0,1)<=0. If it were negative, choose C'=(0,1,-epsilon) inside the existing vertical fibre, with epsilon>0 arbitrarily small. The displayed exact numerator increases by alpha epsilon X. The affine image remains a uniformly filled admissible marked body, its endpoint values remain positive, and it converges to P. This contradicts joint local maximality. Hence hA(0,1)=0. The same argument at D gives hA(1,0)=0.

Now suppose hB(0,1)<1. At C the root is strictly inactive because c>0. Consequently, for sufficiently small epsilon>0, (0,1+epsilon,0) belongs to P: the lower graph is zero on this axis and both upper inequalities are still strict at radius 1. Moving C to this point has strictly positive first derivative (b+2c)X. Therefore hB(0,1)=1. Similarly hB(1,0)=1.

Homogeneity now makes the actual x=0 section exactly ABC and y=0 section exactly ABD. The root is positive throughout those triangles, so it meets neither coordinate facet. At C only x=0 and the unique active lower and upper axis-adjacent planes are incident; distinct slopes tying on the axis reduce to one extremal active form on the interior side. Thus C is a true degree-three vertex. The same holds for D.

This argument is not licensed for a merely fixed-endpoint or fixed-lattice maximum. It is also not a claim that an arbitrary enlarged patch can be replaced monotonically while keeping its f-vector.

### A useful endpoint bound in this sector

A positive tetrahedral fan from a vertex maximizing x gives gx>=max_P x/4>=1/4; similarly gy>=1/4. Set a=1, s=1+b, m=max(c,d), nu=min(c,d). After exchanging x,y if necessary, the G condition at the mark whose endpoint is m gives

    r+qm <= s+nu,
    r >= (2s+m+nu)/4.

Therefore

    m <= s/(2q-1).

At T>=51/25, q=Tt>=51/25 and s<2, so m<50/77<1. At T>=65/32 the same argument also gives m<1. This is used below only to justify the positive-octant flat-A chart, not as a purported realizability certificate.

## 3. Flat A: removal of the off-root freedom at a genuine local maximum

Assume hA=0. There is one lower facet, the actual z=0 polygon. The preceding section makes the coordinate faces proper33 at a joint maximum.

The necessary full-class fixed-ell variations remain available. For clarity, their role is as follows. Cap removal, including the thin-edge equality cap, gives G>0 at every auxiliary true vertex. An outward pyramid on a free facet gives max_F G+3 mean_F G<=0. Both-sign pivots of a facet containing only B give integral_F G(G-G(B))=0. Exact triangle moments and the pyramid inequality then force every ordinary B-facet to be a true triangle [B,Y,Z] with

    G(Y)=G(Z)=LB=(r+qb)/3>0.

The variations act on an entire polygonal facet and allow nonsimple vertices to split. They do not assume an available fixed-lattice vertex slide. These are the supplied full geometric lemmas.

There are exactly two special upper facets, containing BC and BD respectively. If they were the same facet, hB=x+y, and with hA=0 the root would be inactive on T0. An ordinary B-base can lie only on the root or on the one flat lower facet. Each of those polygons can contain at most one supporting edge at level LB. There cannot be one on each: the root then has an ordinary base as a supporting level-LB edge and lies entirely on one side of it. If the root lies below that level, the two noncollinear bases force a positive constant-G facet; if it lies above, the genuine root-lower edge would coincide with the lower facet's ordinary base and be incident to three facets. This is the flat-star count argument, including the genuine root-lower edge, not a triangulation count. Hence there is at most one ordinary B-facet.

**New angular step.** Write theta=x/(x+y). With hA=0,

    D(theta)=H hB(theta,1-theta)-l0(theta,1-theta).

D is convex and piecewise affine. Its negative set I is one nonempty interval strictly inside (0,1), because c,d>0 and proper33 hold. If the ordinary B-triangle had its base on z=0, its entire open angular interval would be nonroot-visible. The remaining two angular pieces are the two special upper planes. The connected interval I would then lie in one affine piece of D. An affine function cannot be strictly negative between two zero endpoints. Thus the ordinary B-base must be on the root.

If there is no ordinary B-facet, the unique breakpoint between the special upper planes must be in the closure of I, by the same affine-function argument. If there is one, both its bounding breakpoints are root vertices because its whole base is a root edge. Every auxiliary off-root vertex in a flat-A body would have to be on z=0 at an upper-envelope breakpoint. All those breakpoints have just been accounted for on the root. Consequently **every noncanonical true vertex is on the root**.

The root is the triangle cut out by the two special B-planes and z=0, possibly truncated at its inner corner by one ordinary B-plane. This proves the required actual reduction. The old hypothesis 'all auxiliary vertices are root vertices' has not been assumed.

## 4. Complete actual flat-root family and its uniform moments

For a high-trace flat-A maximum, Section 2 gives 0<c,d<1. Set

    beta=(1-b)/b>0, e=c/(1-c)>0, f=d/(1-d)>0,
    Z=beta+s+t, DU=1+(s+t)f, DV=1+(s+t)e,

where s,t>0 parametrize the positive inner corner W of the enlarged root triangle. Removing a possible ordinary B-plane lowers the two-plane envelope, so its root shadow remains nonempty; its single angular kink is root-visible. Thus that inner corner has all three coordinates positive. Conversely, for a positive corner W, put Z=(1+beta)/W_z, s=Z W_x/(1+f), t=Z W_y/(1+e); its root equation gives Z=beta+s+t. This verifies coverage, not only construction of examples. In this section s,t are chart parameters, not 1+b or 6V. Define

    U=((1+f)(1+sf)/DU, t(1+e)f/DU, 0),
    V0=(s(1+f)e/DV, (1+e)(1+te)/DV, 0),
    W=(s(1+f)/Z, t(1+e)/Z, (1+beta)/Z).

The notation V0 denotes a vertex, not body volume. These are the intersections of the actual planes B-D-W, B-C-W, ell=0 and z=0. The root triangle is WUV0. For 0<=u,v<=1 put

    Pu=W+u(U-W), Pv=W+v(V0-W),
    P(beta,s,t,e,f,u,v)=conv(A,B,C,D,U,V0,Pu,Pv).

Coincident or redundant labels on boundary strata must be re-hulled. This chart includes the root triangle when uv=0 and every root truncation obtained in Section 3. It is an actual convex hull with canonical marks, not a chosen moment tuple.

Let b=1/(1+beta), c=e/(1+e), d=f/(1+f), and retain the original n=(1+b+c)x+(1+b+d)y. Put

    dA=U_y,
    dC=(V0)_x,
    dM=det(U_xy,(V0)_xy),
    dR=det(W-B,U-B,V0-B)
       =(1+e)(1+f)(1+et+fs)/(Z DU DV)>0.

The actual body before the corner cut is the positive B-fan over the base pentagon A,D,U,V0,C and the root triangle W,U,V0. The cut removes exactly the tetrahedron B,W,Pu,Pv, of six-volume uv dR. Thus, writing Ahat=6 Vol(P), Ehat=24 integral_P ell, Nhat=24 integral_P n,

    Ahat=dA+dC+dM+dR(1-uv),

    Ehat=dA(b+1+d)+dC(b+1+c)+dM(b+1)+b dR(1-uv),

    Nhat=dA[n(D)+n(U)]+dC[n(V0)+n(C)]+dM[n(U)+n(V0)]
      +dR{n(U)+n(V0)+n(W)
        -uv[3n(W)+u(n(U)-n(W))+v(n(V0)-n(W))]}.

In particular T=Nhat/(Ahat Ehat). These are actual uniform tetrahedral integrals, including the changed body when e,f change. They preserve neither the old centroid nor the old volume.

### Coupled endpoint dominance, with a complete finite certificate

For the same beta,s,t,u,v, let Ahat0,Ehat0,Nhat0 denote the e=f=0 body after its actual re-hull. The first recovery program proves

    Nhat0 Ahat Ehat - Nhat Ahat0 Ehat0 >= 0,

hence T(e,f)<=T(0,0). This is a simultaneous actual family comparison; no separate monotonicity in c or d is asserted.

Here is the certificate's mathematical structure. Clearing the explicitly positive common denominator produces an integer polynomial G with 16,648 monomials. Set k=uv, w=1-k and

    Bv=-8k^2+2kv+7k-1,
    Cv=(1-k)(1+2k+3kv-6k^2),
    Dv=(1-k)^2(2-3k+kv).

Subtract the two reflected blocks

    e[2s^4+Bv s^3+Cv s^2+Dv s]

and its reflection (s,t;e,f;u,v)->(t,s;f,e;v,u). Both are nonnegative. Indeed Bv>=-w, Cv>=w^2, Dv>=0, and

    2s^4+Bv s^3+Cv s^2
      >=s^2[2(s-w/4)^2+7w^2/8].

Every coefficient of the remainder in the unbounded nonnegative variables beta,s,t,e,f is a polynomial in u,v whose degree-(4,4) Bernstein coefficients are nonnegative on the entire closed square. The executable generates and checks all 4,319 coefficient polynomials: 106,414 positive coefficients, 1,561 zero coefficients, minimum positive 1/8. There is no sampled-parameter or infeasible-cell pruning. The complete generator is embedded below; no table or omitted helper is needed. To make its algebraic bridge explicit, the source variables p,s,t,e,f,u,v have p=beta and L=(1+p)(1+e)(1+f). Its integer numerators satisfy

    Ahat=AN/(Z DU DV),
    Ehat=EN/(L Z DU DV),
    Nhat=NN/(L Z^2 DU^2 DV^2),
    Ahat0=A0/Z, Ehat0=E0/((1+p)Z), Nhat0=N0/((1+p)Z^2).

Hence G=N0 AN EN-NN A0 E0 is exactly the stated cross-product times (1+p)L Z^4 DU^2 DV^2>0. These equalities follow directly by substitution into the displayed actual fan formulas.

### An elementary bound for the zero-endpoint family

Set rho=sqrt(uv), h=1-rho^2, C_rho=(1-rho)^2(1+2rho), and z=beta+s+t. AM-GM gives u+v>=2rho. The explicit numerator therefore yields

    T(0,0) <= (beta+2)[2z^2+3zh-beta C_rho]
                 /[(z+h)((beta+2)z+h)].

When h=0 the right side is 2. Otherwise put R=z/h and J=C_rho/h^2=(1+2rho)/(1+rho)^2>=3/4. For tau=65/32 and delta=1/32, the numerator of tau minus the last ratio, divided by h^2, is at least

    delta(beta+2)R^2+[(delta-1)beta+3delta]R
      +tau+(3/4)beta(beta+2).

This quadratic is strictly positive for every real R. Four times the product of its leading and constant coefficients minus the square of its linear coefficient is

    [96 beta^3-577 beta^2+830 beta+511]/1024 > 0.

On beta in [0,3], the cubic has Bernstein coefficients (511,1341,440,400). For beta=3+x, x>=0, it is

    96x^3+287(x-20/287)^2+114400/287 > 0.

This proves T<65/32 for the entire displayed seven-parameter family, and hence for the full flat-A joint-extremal sector. It does not need the absent old single-B executable or its sharper Cstar optimization.

## 5. Flat B and a genuine open upper-defect chamber

This proof keeps the actual body throughout and applies without stationary fan hypotheses.

Set a=1, alpha=1-b, S=c+d, m=max(c,d), nu=min(c,d), s=1+b, and

    fB=x+y-hB >= 0,
    epsilon_B=6 alpha integral_Delta fB.

The nonnegativity follows from convex homogeneity and canonical containment. The exact A-based divergence identity in the supplied greedy proof is

    4E=V+integral_(K\R) ell_upper,
    ell_upper=b+(d-b)x+(c-b)y-alpha fB.

On K\R this integrand is nonnegative. Delta belongs to K, and restricting to Delta gives at least integral_Delta (ell_upper)_+, which is at least integral_Delta ell_upper. Consequently

    24E >= t+b+S-epsilon_B.                    (5.1)

This does not assume R misses Delta when the upper star is nonflat; the positive part is essential. If hB=x+y, epsilon_B=0 and it gives the stronger flat-upper flux budget 24E>=t+b+S.

The inherited actual joint-mass theorem and gx,gy>=1/4 imply

    4r <= (s+m)t+s+nu.                         (5.2)

The G condition at the mark with larger endpoint gives

    r+qm <= s+nu.                              (5.3)

Let tau=2+delta and suppose T>=tau. Combining (5.1)-(5.3), for an upper bound epsilon on epsilon_B, gives the following two inequalities. Both uses below have epsilon<=1/64, so t+b+S-epsilon>0:

    tau(t+b+m+nu-epsilon) <= (s+m)t+s+nu,
    tau t(1+4m) <= 4(s+nu)-tau(b+m+nu-epsilon).

Put x=m-alpha-delta. If delta-tau epsilon>0, the first inequality is impossible for x<=0: its deficit at t=1 is delta s+(1+delta)(m+nu)-tau epsilon>0 and then increases with t. Thus x>0, and

    t >= tau + [alpha+delta(3+delta)+(1+delta)nu-tau epsilon]/x.

Substitute this lower bound into the second inequality. It would force H_delta,epsilon<=0, where

    H_delta,epsilon=
      tau[tau x+alpha+delta(3+delta)+(1+delta)nu-tau epsilon]
          (1+4alpha+4delta+4x)
      -x[6-3delta-delta^2-4alpha-tau x+(2-delta)nu+tau epsilon].

For epsilon=0 its expansion is

    (8+4delta)alpha^2 +(8+12delta+4delta^2)alpha nu
    +(28+20delta+4delta^2)alpha x
    +(2+33delta+24delta^2+4delta^3)alpha
    +(6+13delta+4delta^2)nu x
    +(2+11delta+13delta^2+4delta^3)nu
    +(18+17delta+4delta^2)x^2
    +(-2+47delta+38delta^2+8delta^3)x
    +(6delta+29delta^2+21delta^3+4delta^4).

All coefficients except possibly that of x are positive. The x-quadratic has 4AC-B^2=-4+620delta+439delta^2+40delta^3-16delta^4.

**Flat upper star.** Take delta=1/128, epsilon=0. The last expression equals 14605631/16777216>0, so H>0. This proves T<257/128.

**Open upper-defect chamber.** Take delta=1/25 and epsilon=1/64. Now delta-tau epsilon=13/1600>0. All terms involving alpha or nu still have positive coefficients. The remaining quadratic is

    (11679/625)x^2 -(350663/1000000)x +5308131/25000000,

whose 4AC-B^2 is 25195860671/1600000000>0. Thus H>0 again, proving T<51/25 whenever epsilon_B<=1/64. The executable verifies both polynomial identities and all exact signs.

The condition is an integral of the actual concave upper excess over the canonical triangle. It is not an independently assignable root mass, covariance, or projected moment completion. No assertion is made that epsilon_B<=1/64 is automatic at every joint maximum.

## 6. New exact near-sharp positive-ell/greedy control

Use

    a=1, b=6/25, c=d=1/10000,
    hA=max(-x/10000, -y/10000, -x/10^10-y/20000),
    hB=max(y-9x, x-9y, 15(x+y)/16).

The root is ell=1-9999(x+y)/10000-19z/25=0; n=12401(x+y)/10000. The complete halfspaces are these three lower and three upper graph inequalities plus x>=0,y>=0,ell>=0. They define the actual uniform body. Boundedness is explicit: hA>=-(x+y)/10000 and the root inequality give (62489/62500)(x+y)<=1; then both z endpoints are bounded. The listed root vertices give its genuine positive area.

The true vertices, in the verifier's lexicographic order, are:

    0: (0,0,0)
    1: (0,0,1)
    2: (0,1,0)
    3: (10000/999902399,999992400/999902399,-1/999902399)
    4: (5/958,795/958,104/479)
    5: (5000000000/14998110001,1428570000/2142587143,-500000/14998110001)
    6: (795/958,5/958,104/479)
    7: (1,0,0)
    8: (5000000000/4999909999,10000/4999909999,-1/4999909999)
    9: (999991200000000/999901199421601,9999997600/999901199421601,-599999/999901199421601)

All nine genuine maximal facet cycles are

    (0,1,2), (0,7,1), (0,2,3,5), (0,8,7), (0,5,9,8),
    (1,4,3,2), (1,7,8,9,6), (1,6,4), (3,4,6,9,5).

All seventeen physical edges are

    (0,1),(0,2),(0,5),(0,7),(0,8),(1,2),(1,4),(1,6),(1,7),
    (2,3),(3,4),(3,5),(4,6),(5,9),(6,9),(7,8),(8,9).

Canonical labels are A=0,B=1,C=2,D=7. The root is the pentagon (3,4,6,9,5). Vertex 8 is the sole positive-ell auxiliary. All auxiliary G values and G(C),G(D) are strictly positive.

The exact trace is

    14124322840448424028188441097651440533251704989945219507814135646961862888967136812395646748086987293977723
    /6962515744549024935937609531105639953258292564617668472034911500595689111645955127797612030892371394440000,

so 507/250 < T < 51/25 and T=2.0286234686803257... . The recovery recomputes V, all three original first moments, E,N, and the actual centroid from positive tetrahedra over the literal maximal facets. No fixed reference substitutes for that centroid.

The angular root shadow is exactly

    I=(25/2500006, 1249989000000/1250001499997).

There is exactly one curvature atom outside I, at theta=500000/500001, and

    eta''{theta}=kappa''{theta}=500001/10^10.

There is no other tail curvature. Both proper endpoint budgets are therefore already filled greedily. The body is in the inherited exact vertical normal form for its own actual K,R, without replaying the missing old greedy program. The stated greedy criterion is the one proved in the attached complete analytic source.

Its actual star defects, with epsilon_A=-6 alpha integral_Delta hA, are

    epsilon_A=4750018999981/187500249999750000,
    epsilon_B=3021/32000 > 1/64.

It lies outside the newly excluded upper-defect chamber. The ordinary A-facet (0,5,9,8) is a quadrilateral containing A and no other canonical mark, so it violates full ordinary-facet rigidity. It is emphatically not a joint stationary counterexample; merely having the small f-vector and greedy placement is insufficient.

At the actual centroid and M=Nmetric=I, strict stable facets are (0,1,4,7), strict unstable vertices are (0,1,3,9), and strict saddle edges are (0,1),(0,2),(0,7),(1,4),(1,6),(5,9). Every one of the 68 physical edge primitives is nonzero, so the physical weak count is zero. The code constructs the poles at that same centroid and uses the same Euclidean metric for primal and polar tests.

## 7. What was tried, limits, and continuation

I first examined canonical mark reactions and direct gauge optimization rather than adding another covariance completion. The mark argument supplied proper33. The decisive flat-A observation was angular: with one flat star, a nonroot ordinary interval would leave the root shadow trapped in a single affine piece. The value proof then used the actual base/root fan, simultaneous endpoint re-hulling, and a global polynomial certificate. Separately, the A-based flux identity yielded the flat-B and upper-defect value theorem.

Floating thirteen-parameter lower/upper-envelope locators and a comparison with the z>=0 cut were exploratory only. They yielded no verified T>=51/25 example and no monotonicity theorem. No numerical nonfinding is used in a proof. The exact rational control and its complete verifier, rather than a floating optimizer checkpoint, are the durable successor object.

Important limits:

- The flat-A proof is a full-class stationary reduction, not an arbitrary-body flattening theorem. I did not prove T(P)<=max(2,T(P intersect {z>=0})) for the whole two-anchor class.
- Simultaneous e=f=0 dominance is proved only for the explicit flat-root family. It is not independent monotonicity of the two endpoints or a general deformation of nonflat two-anchor bodies.
- The upper-defect proof retains the positive part of the actual upper ell value on Delta. Dropping it or pretending that R misses Delta for every nonflat upper star would be incorrect.
- Small f-vector bounds and greedy tail allocation do not imply full stationarity, as the new exact control demonstrates.
- The inherited joint-mass theorem is an explicit analytic premise of Section 5. The new coefficient programs verify the derived polynomial implications, not that old theorem or a proof-assistant formalization of shape derivatives.

The most useful continuation is now the genuinely nonflat proper33 fan with epsilon_B>1/64. In its high-trace sector c,d<50/77, C,D are true simple vertices, the root has at most six physical edges, and the supplied ordinary A/B levels and polygon reactions must all be imposed. The exact positive-ell control is useful for testing any proposed deletion or stationarity relaxation, but its ordinary quad must not be silently promoted to a stationary triangle. A proof of the entire remaining sector, or an actual threshold body satisfying its physical hypotheses, is still needed.

## 8. Complete recovery capsule

The following two source blocks are the complete deterministic recovery of the proved finite certificates and new actual body. The body has no exact parent checkpoint: its nine literal halfspaces define a new construction, GREEDY_TWO_ANCHOR_POSITIVE_ELL_E17_TRACE_2028_CONTROL_V1. They need no parent file, downloaded data, hidden helper, random seed, old executable, or optimizer. Save their literal contents as UTF-8/LF files with one final LF. Environment actually used: CPython 3.13.5; SymPy 1.14.0 for the value certificate; standard library only for the body audit. Assertions must remain enabled.

Commands, in a fresh directory:

    python flat_value_certificate.py > flat_value_stdout.txt
    python -S greedy_high_trace_control.py > greedy_high_trace_stdout.txt
    sha256sum flat_value_certificate.py greedy_high_trace_control.py \
      flat_value_report.json greedy_high_trace_control.json \
      flat_value_stdout.txt greedy_high_trace_stdout.txt

Both programs were executed, then copied alone into a fresh directory and executed again. The final sources, including explicit Bernstein-degree and census assertions, were subsequently cold-replayed once more. Both JSON outputs were byte-identical to the first execution. This is a completed source-only cold replay of the new units, not a claim to have replayed any missing parent executable.

| File | Bytes | SHA-256 |
|---|---:|---|
| flat_value_certificate.py | 5374 | 9b016c79afa08e4a3432c841e3cbbc6e67eb616953019dd959952b360d787852 |
| greedy_high_trace_control.py | 8787 | 485b7ac57babb17490b20df33972fa4f32dc175f19bc671782e5e0b8df3bfab4 |
| flat_value_report.json | 577 | d9f245b652942dd62998215ee7472f566448f6bcf831926995a55757cac6b76f |
| greedy_high_trace_control.json | 31940 | 5b25374d053b9f39d910949d42044614a0a8005e2b10eb0fee0a7b01a5e5b8fa |
| flat_value_stdout.txt | 902 | c83fddbc773dd15d4b02abb0b328034d30b69912f88259c781a26d2a9a27ab7e |
| greedy_high_trace_stdout.txt | 1761 | 4313fd6bdcbe14d4a85c6bd6857aa48edc48c6ee8d826f40b6c6b379456549ca |

The generated complete Bernstein coefficient stream has 2,424,062 bytes and SHA-256 652fbe7b975ae07e64a9a317fb45c78b724104634c895078f4d4d377a1aad4a6. It is regenerated and checked in memory by the source; its hash is not a substitute for that source.

Expected proof markers:

    FLAT_ROOT_FAMILY_COUPLED_ENDPOINT_DOMINATION_PASS 16648 4319 106414 1561
    ZERO_ENDPOINT_ALL_PARAMETER_VALUE_LT_65_OVER_32_PASS
    FLAT_B_ACTUAL_FACET_FLUX_AND_G_SECTOR_VALUE_LT_257_OVER_128_PASS
    ACTUAL_UPPER_DEFECT_LE_1_OVER_64_VALUE_LT_51_OVER_25_PASS

Expected body markers include:

    ACTUAL_PROPER33_TWO_ANCHOR_10_17_9_PASS
    STRICT_SUH 4 4 6 WEAK 0
    GREEDY_HIGH_TRACE_CONTROL_PASS_NOT_A_JOINT_MAXIMUM

### Source 1: flat_value_certificate.py

```python
"""Exact flat-star value certificate. CPython 3.13.5, SymPy 1.14.0.
No files, random inputs, or earlier programs are needed.
"""
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import sympy
from sympy.polys.rings import ring
from sympy.polys.domains import ZZ
assert __debug__
assert sympy.__version__ == '1.14.0'
R,p,s,t,e,f,u,v=ring('p,s,t,e,f,u,v',ZZ)
Z=p+s+t; DU=1+(s+t)*f; DV=1+(s+t)*e
M=(1+e)*(1+f)*(1+e*t+f*s)
HC=p+2+(2*p+3)*e; HD=p+2+(2*p+3)*f
NU=HC*(1+f)**2*(1+s*f)+HD*t*(1+e)**2*f
NV=HC*s*(1+f)**2*e+HD*(1+e)**2*(1+t*e)
NW=HC*s*(1+f)**2+HD*t*(1+e)**2
AN=t*(1+e)*f*Z*DV+s*(1+f)*e*Z*DU+M*(Z+1-u*v)
EN=(t*(1+e)**2*f*Z*DV*HD+s*(1+f)**2*e*Z*DU*HC
    +(1+e)*(1+f)*M*((p+2)*Z+1-u*v))
NN=(t*(1+e)*f*Z**2*DV**2*(HC*(1+f)*DU+NU)
    +s*(1+f)*e*Z**2*DU**2*(NV+HD*(1+e)*DV)
    +M*Z**2*(NU*DV+NV*DU)
    +M*(Z*DV*NU*(1-u*u*v)+Z*DU*NV*(1-u*v*v)
         +DU*DV*NW*(1-3*u*v+u*u*v+u*v*v)))
A0=Z+1-u*v;E0=(p+2)*Z+1-u*v
N0=(p+2)*(2*Z**2+2*p+3*(s+t)-p*u*v*(u+v)-3*(s+t)*u*v)
G=N0*AN*EN-NN*A0*E0
assert len(G)==16648
# The positive denominator of T00-Tef is
# (1+e)(1+f)(1+p)^2 Z^4 DU^2 DV^2 times the positive trace denominators.
# In fact G clears N00*Aef*Eef-Nef*A00*E00, not the already divided traces.
k=u*v; w=1-k
B=-8*k*k+2*k*v+7*k-1
C=(1-k)*(1+2*k+3*k*v-6*k*k)
D=(1-k)**2*(2-3*k+k*v)
assert B+w == 2*k*(3+v-4*k)
assert C-w*w == 3*k*w*(1+v-2*k)
# B >= -w; C >= w^2; D >= 0 on 0<=u,v<=1.
# 2*s^4+B*s^3+C*s^2 >= s^2*(2*(s-w/4)^2+7*w^2/8).
block=e*(2*s**4+B*s**3+C*s*s+D*s)
# Reflection swaps s,t; e,f; u,v.
def swap(poly):
    return R.from_dict({(a,c,b,g,h,j,i):z for (a,b,c,h,g,i,j),z in poly.items()})
block2=swap(block)
H=G-block-block2
assert H[(5,0,0,1,0,0,0)]==1
assert H[(5,0,0,0,1,0,0)]==1
# All remaining coefficients in p,s,t,e,f are polynomials in u,v.
# Certify each on the ENTIRE closed unit square by degree-(4,4) Bernstein.
groups=defaultdict(dict)
for ex,c in H.items():groups[ex[:5]][ex[5:]]=int(c)
assert len(groups)==4319
assert all(a<=4 and b<=4 for terms in groups.values() for a,b in terms)
records=[];positive=zero=0;minimum=None
for ex in sorted(groups):
    terms=groups[ex]
    for i in range(5):
        for j in range(5):
            z=sum((F(c*comb(i,a)*comb(j,b),comb(4,a)*comb(4,b))
                   for (a,b),c in terms.items() if a<=i and b<=j),F(0))
            assert z>=0,(ex,i,j,z)
            if z:positive+=1;minimum=z if minimum is None else min(minimum,z)
            else:zero+=1
            records.append([*ex,i,j,str(z)])
raw=(json.dumps(records,separators=(',',':'))+'\n').encode()
# The zero-endpoint value bound uses only this positive cubic.
# Its Bernstein coefficients on p in [0,3] are all positive.
coefs=[F(511),F(2490),F(-5193),F(2592)]
bern=[sum((coefs[j]*F(comb(i,j),comb(3,j)) for j in range(i+1)),F(0)) for i in range(4)]
assert bern==[511,1341,440,400]
# For p=3+x: cubic=96*x^3+287*(x-20/287)^2+114400/287.
assert F(287)*F(20,287)**2+F(114400,287)==400
assert -2*287*F(20,287)==-40
# A separate whole flat-B sector certificate from actual upper-facet flux.
# alpha=1-b, nu=min(c,d), x=max(c,d)-alpha-delta.
aa,xx,nn,dd=sympy.symbols('aa xx nn dd')
tau=2+dd
HH=sympy.Poly(sympy.expand(tau*(tau*xx+aa+dd*(3+dd)+(1+dd)*nn)
      *(1+4*aa+4*dd+4*xx)
      -xx*(6-3*dd-dd*dd-4*aa-tau*xx+(2-dd)*nn)),aa,nn,xx)
base=sympy.Poly(HH.as_expr().subs({aa:0,nn:0}),xx)
qa,qb,qc=base.all_coeffs()
disc=sympy.factor(4*qa*qc-qb*qb)
assert disc == -16*dd**4+40*dd**3+439*dd**2+620*dd-4
D=sympy.Rational(1,128)
for ex,z in HH.terms():
    if ex==(0,0,1):continue
    assert z.subs(dd,D)>0
flat_b_gap=disc.subs(dd,D)
assert flat_b_gap==sympy.Rational(14605631,16777216)>0
# The upper-defect chamber: delta=1/25, epsilon_B<=1/64.
D2=sympy.Rational(1,25);eps=sympy.Rational(1,64);T2=2+D2
HE=sympy.Poly(sympy.expand(HH.as_expr().subs(dd,D2)
    -T2**2*eps*(1+4*aa+4*D2+4*xx)-T2*eps*xx),aa,nn,xx)
for ex,z in HE.terms():
    if ex==(0,0,1):continue
    assert z>0
qa2,qb2,qc2=sympy.Poly(HE.as_expr().subs({aa:0,nn:0}),xx).all_coeffs()
eps_gap=sympy.factor(4*qa2*qc2-qb2**2)
assert eps_gap==sympy.Rational(25195860671,1600000000)>0
assert D2-T2*eps==sympy.Rational(13,1600)>0
report={'name':'TWO_ANCHOR_FLAT_STARS_AND_UPPER_DEFECT_VALUE_V1',
        'G_terms':len(G),'remaining_groups':len(groups),'Bernstein_positive':positive,
        'Bernstein_zero':zero,'minimum_positive':str(minimum),
        'coefficient_stream_bytes':len(raw),'coefficient_stream_sha256':sha256(raw).hexdigest(),
        'cubic_Bernstein_0_3':[str(x) for x in bern],
        'trace_bound_flat_A':'65/32','target_gap_flat_A':'7/800',
        'trace_bound_flat_B':'257/128','flat_B_quadratic_discriminant_gap':str(flat_b_gap),
        'upper_defect_max':'1/64','upper_defect_quadratic_gap':str(eps_gap)}
# 51/25-65/32=7/800.
assert F(51,25)-F(65,32)==F(7,800)
out=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode()
Path('flat_value_report.json').write_bytes(out)
print('FLAT_ROOT_FAMILY_COUPLED_ENDPOINT_DOMINATION_PASS',len(G),len(groups),positive,zero)
print('ZERO_ENDPOINT_ALL_PARAMETER_VALUE_LT_65_OVER_32_PASS')
print('FLAT_B_ACTUAL_FACET_FLUX_AND_G_SECTOR_VALUE_LT_257_OVER_128_PASS')
print('ACTUAL_UPPER_DEFECT_LE_1_OVER_64_VALUE_LT_51_OVER_25_PASS')
print('REPORT',len(out),sha256(out).hexdigest())
print(out.decode(),end='')
```

### Source 2: greedy_high_trace_control.py

```python
"""A rational proper33, two-anchor, greedy high-trace nonstationary control.
CPython 3.13.5, standard library only. No external files or inputs.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from pathlib import Path
from hashlib import sha256
import json
assert __debug__
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(c,a):return tuple(c*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def solve(rows,rhs):
    D=det(*rows)
    if not D:return None
    return tuple(det(*[tuple(rhs[i] if k==j else rows[i][k] for k in range(3)) for i in range(3)])/D for j in range(3))
def hull2(points):
    pts=sorted(set(points))
    def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[];hi=[]
    for p in pts:
        while len(lo)>=2 and turn(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi)>=2 and turn(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    return x
A=(F(0),F(0),F(0));B=(F(0),F(0),F(1));C=(F(0),F(1),F(0));D=(F(1),F(0),F(0))
a,b,c,d=F(1),F(6,25),F(1,10000),F(1,10000)
alpha=a-b;hc=a+b+c;hd=a+b+d
# hA>=-(x+y)/10000; the root then bounds x+y and both z endpoints.
assert a-d-alpha/F(10000)>0 and a-c-alpha/F(10000)>0
lower=[(-F(1,10000),F(0)),(F(0),-F(1,10000)),(-F(1,10**10),-F(1,20000))]
upper=[(-F(9),F(1)),(F(1),-F(9)),(F(15,16),F(15,16))]
# Normals are outward and every inequality is normal.point <= offset.
planes=[((-F(1),F(0),F(0)),F(0)),((F(0),-F(1),F(0)),F(0))]
planes += [((x,y,-F(1)),F(0)) for x,y in lower]
planes += [((x,y,F(1)),F(1)) for x,y in upper]
planes += [((a-d,a-c,alpha),a)]
verts=set()
for ids in combinations(range(len(planes)),3):
    v=solve([planes[i][0] for i in ids],[planes[i][1] for i in ids])
    if v is not None and all(dot(n,v)<=h for n,h in planes):verts.add(v)
verts=sorted(verts);facets=[];plane_ids=[]
for j,(n,h) in enumerate(planes):
    ids=[i for i,v in enumerate(verts) if dot(n,v)==h]
    if len(ids)<3:continue
    drop=next(i for i,z in enumerate(n) if z);axes=[i for i in range(3) if i!=drop]
    mapping={tuple(verts[i][k] for k in axes):i for i in ids}
    cyc=[mapping[p] for p in hull2(mapping)]
    if len(cyc)<3:continue
    if dot(cross(sub(verts[cyc[1]],verts[cyc[0]]),sub(verts[cyc[2]],verts[cyc[0]])),n)<0:cyc.reverse()
    z=cyc.index(min(cyc));cyc=cyc[z:]+cyc[:z]
    assert set(cyc)==set(ids)
    facets.append(tuple(cyc));plane_ids.append(j)
edges=sorted({tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in facets for i in range(len(f))})
inc={edge:[j for j,f in enumerate(facets) if set(edge).issubset(f)] for edge in edges}
assert all(len(x)==2 for x in inc.values())
assert len(verts)-len(edges)+len(facets)==2
assert (len(verts),len(edges),len(facets))==(10,17,9)
mark_ids=[verts.index(p) for p in (A,B,C,D)]
assert set(facets[plane_ids.index(0)])=={mark_ids[i] for i in (0,1,2)}
assert set(facets[plane_ids.index(1)])=={mark_ids[i] for i in (0,1,3)}
for i in mark_ids[2:]:assert sum(i in edge for edge in edges)==3
ell=lambda p:a+(d-a)*p[0]+(c-a)*p[1]-alpha*p[2]
nn=lambda p:hc*p[0]+hd*p[1]
O=tuple(sum(v[j] for v in verts)/len(verts) for j in range(3))
assert all(dot(n,O)<h for n,h in planes)
vol=F(0);J=(F(0),)*3;E=N=F(0)
for face in facets:
    for j in range(1,len(face)-1):
        pts=[O,verts[face[0]],verts[face[j]],verts[face[j+1]]]
        w=det(*(sub(x,O) for x in pts[1:]))/6
        assert w>0
        vol+=w;J=add(J,mul(w/4,tuple(sum(x[k] for x in pts) for k in range(3))))
        E+=w*sum(ell(x) for x in pts)/4;N+=w*sum(nn(x) for x in pts)/4
g=mul(1/vol,J);r=N/vol;q=N/E;T=N/(6*vol*E)
GG=lambda p:nn(p)-r-q*ell(p)
assert E==vol*ell(g) and N==vol*nn(g)
assert T>F(507,250) and T<F(51,25)  # 2.028 < T < 2.04.
aux=[i for i in range(len(verts)) if i not in mark_ids]
posell=[i for i in aux if ell(verts[i])>0]
root=facets[plane_ids.index(8)]
assert len(posell)==1 and len(root)==5
assert min(GG(verts[i]) for i in aux+mark_ids[2:])>0
# Exact angular envelope, including every crossing and root-shadow endpoint.
def at(form,t):return form[0]*t+form[1]*(1-t)
cuts={F(0),F(1)}
for forms in (lower,upper):
    for x,y in combinations(forms,2):
        den=x[0]-x[1]-y[0]+y[1]
        if den:
            z=(y[1]-x[1])/den
            if 0<z<1:cuts.add(z)
def pieces(cuts):
    ans=[]
    cs=sorted(cuts)
    for l,h in zip(cs,cs[1:]):
        mid=(l+h)/2
        ia=max(range(3),key=lambda i:at(lower[i],mid));ib=max(range(3),key=lambda i:at(upper[i],mid))
        ans.append((l,h,ia,ib))
    return ans
l0=((a-d)/alpha,(a-c)/alpha)
def angular(ia,ib,t):
    eta=at(lower[ia],t)+at(l0,t)
    kappa=at(lower[ia],t)+at(upper[ib],t)
    return eta,kappa,a/alpha*kappa-eta
for l,h,ia,ib in pieces(cuts):
    dl=angular(ia,ib,l)[2];dh=angular(ia,ib,h)[2]
    if dl*dh<0:cuts.add(l+(h-l)*dl/(dl-dh))
ps=pieces(cuts);visible=[(l,h) for l,h,ia,ib in ps if angular(ia,ib,(l+h)/2)[2]<0]
I=(min(l for l,h in visible),max(h for l,h in visible))
assert 0<I[0]<I[1]<1
epsilon_B=alpha*sum((h-l)*(2-at(upper[ib],l)-at(upper[ib],h)) for l,h,ia,ib in ps)
epsilon_A=-alpha*sum((h-l)*(at(lower[ia],l)+at(lower[ia],h)) for l,h,ia,ib in ps)
assert epsilon_B>F(1,64) and epsilon_A>0
atoms=[]
for left,right in zip(ps,ps[1:]):
    l,h,ia,ib=left;ll,hh,ja,jb=right
    if (ia,ib)==(ja,jb):continue
    slope=lambda f:f[0]-f[1]
    de=slope(lower[ja])-slope(lower[ia])
    dk=de+slope(upper[jb])-slope(upper[ib])
    assert 0<=de<=dk
    if dk:atoms.append((h,de,dk))
tail_atoms=[x for x in atoms if x[0]<=I[0] or x[0]>=I[1]]
assert len(tail_atoms)==1 and tail_atoms[0][1]==tail_atoms[0][2]>0
# Every tail curvature atom is fully assigned to eta; there are no other tail
# atoms, so the inherited exact greedy allocation is already satisfied.
# Explicit failure of full ordinary-facet rigidity: the third lower facet
# contains only A among the canonical marks but is a quadrilateral.
ordinary=facets[plane_ids.index(4)]
assert len(ordinary)==4 and set(ordinary).intersection(mark_ids)=={mark_ids[0]}
# True own-COM Euclidean mechanics: all four primitives per physical edge.
X=[sub(v,g) for v in verts]
poles=[mul(1/(planes[i][1]-dot(planes[i][0],g)),planes[i][0]) for i in plane_ids]
primal={};dual={};packets=[]
for edge in edges:
    i,j=edge;f,h=inc[edge]
    dij=dot(X[i],sub(X[j],X[i]));dji=dot(X[j],sub(X[i],X[j]))
    dfh=dot(poles[f],sub(poles[h],poles[f]));dhf=dot(poles[h],sub(poles[f],poles[h]))
    primal[i,j]=dij;primal[j,i]=dji;dual[f,h]=dfh;dual[h,f]=dhf
    packets.append((edge,(f,h),(dij,dji,dfh,dhf)))
assert all(all(v!=0 for v in signs) for edge,faces,signs in packets)
unstable=[i for i in range(len(verts)) if all(z<0 for (a0,b0),z in primal.items() if a0==i)]
stable=[i for i in range(len(facets)) if all(z<0 for (a0,b0),z in dual.items() if a0==i)]
saddle=[edge for edge,faces,signs in packets if max(signs)<0]
assert len(stable)+len(unstable)-len(saddle)==2
assert (len(stable),len(unstable),len(saddle))==(4,4,6)
report={'name':'GREEDY_TWO_ANCHOR_POSITIVE_ELL_E17_TRACE_2028_CONTROL_V1',
        'endpoint_values':(a,b,c,d),'lower':lower,'upper':upper,'planes':planes,
        'vertices':verts,'facets':facets,'facet_plane_ids':plane_ids,'edges':edges,
        'canonical_indices':mark_ids,'V':vol,'J':J,'Eell':E,'N':N,'centroid':g,'trace':T,
        'root_vertices':root,'positive_ell_auxiliary':posell,
        'vertex_ell':[ell(p) for p in verts],'vertex_G':[GG(p) for p in verts],
        'root_shadow':I,'epsilon_B':epsilon_B,'epsilon_A':epsilon_A,'curvature_atoms':atoms,'tail_atoms':tail_atoms,
        'nonstationary_ordinary_quad':ordinary,'poles_at_own_centroid':poles,
        'strict_stable_facets':stable,'strict_unstable_vertices':unstable,
        'strict_saddle_edges':saddle,'physical_weak_count':0,'true_edge_packets':packets}
raw=(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n').encode()
Path('greedy_high_trace_control.json').write_bytes(raw)
print('ACTUAL_PROPER33_TWO_ANCHOR_10_17_9_PASS')
print('TRACE',T,float(T))
print('V',vol,'E',E,'N',N,'CENTROID',g)
print('POSITIVE_ELL_AUX',posell,'ROOT',root,'NONSTATIONARY_ORDINARY_QUAD',ordinary)
print('ROOT_SHADOW',I,'TAIL_ATOMS',tail_atoms)
print('STAR_DEFECTS',epsilon_A,epsilon_B)
print('STRICT_SUH',len(stable),len(unstable),len(saddle),'WEAK',0)
print('REPORT',len(raw),sha256(raw).hexdigest())
print('GREEDY_HIGH_TRACE_CONTROL_PASS_NOT_A_JOINT_MAXIMUM')
```

## 9. Complete optional discovery locators: nonproof preservation

These three additional units preserve the exploratory searches mentioned in Section 7. They are not dependencies of either proof or the exact body recovery. Save them under their literal filenames in `/mnt/data/two_anchor_work` (the original output directory is explicit in the source), then run `python search.py 51`, `python search_cut.py`, and `python search_flat_b.py`. Executed versions were CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, Numba 0.65.1. All bounds, tolerances, seeds, population sizes, iteration limits and polish settings are in the source. No repeat of these stochastic floating runs is claimed by the exact cold replay; their original terminal records are reproduced literally below.

The first search ended at a floating flat-lower, zero-c,d boundary with T about 2.028699; this is not a certified optimum. The cut comparison reached its iteration cap with apparent gain about 3e-14, which is at roundoff scale and establishes neither monotonicity nor a counterexample. The flat-upper search approached T=2 and likewise proves no bound. The exact certificate above supersedes the associated symbolic discovery scripts; it regenerates the whole decisive polynomial and every accepted coefficient from literal inputs.

| Locator | Bytes | SHA-256 |
|---|---:|---|
| search.py | 3128 | 4349a2afa88b65c93c5daaeeffe371dba358a4edec8e2100e84048c7bf8651fb |
| search_cut.py | 709 | 035939e064d3a319e57720b774f78fc94898135554107eececb15fbfc28f0fef |
| search_flat_b.py | 612 | 1f9f8a3d1ddc0e1ed54de3cece1dbeb7d037347de8f25fe835b2bc1b5ea9ebd5 |

### search.py

```python
import numpy as np
from numba import njit
from scipy.optimize import differential_evolution, minimize
import json,sys
@njit
def evaluate(v):
    b,c,d=v[:3];alpha=1-b
    # Four lower forms; three upper forms. All proper33 axis equalities automatic.
    aa=np.array([[-v[3],0.],[0.,-v[4]],[-v[5],-v[6]],[-v[7],-v[8]]])
    bb=np.array([[1-v[9],1.],[1.,1-v[10]],[1-v[11],1-v[12]]])
    ts=[0.,1.]
    for arr in (aa,bb):
      for i in range(len(arr)):
       for j in range(i):
        den=arr[i,0]-arr[i,1]-arr[j,0]+arr[j,1]
        if abs(den)>1.e-15:
         t=(arr[j,1]-arr[i,1])/den
         if t>0 and t<1:ts.append(t)
    ts.sort()
    V=0.;E=0.;N=0.;X=0.;Y=0.;rootarea=0.
    for k in range(len(ts)-1):
      l,h=ts[k],ts[k+1]
      if h-l<1.e-15:continue
      mid=(l+h)/2
      ia=np.argmax(aa[:,0]*mid+aa[:,1]*(1-mid))
      ib=np.argmax(bb[:,0]*mid+bb[:,1]*(1-mid))
      # U=a-ell(lower), W=b-ell(upper) per unit radius.
      U0=1-c+alpha*aa[ia,1];U1=1-d+alpha*aa[ia,0]
      W0=1-c-alpha*bb[ib,1];W1=1-d-alpha*bb[ib,0]
      dl=(W0-b*U0)*(1-l)+(W1-b*U1)*l
      dh=(W0-b*U0)*(1-h)+(W1-b*U1)*h
      cuts=[l,h]
      if dl*dh<0:cuts=[l,l+(h-l)*dl/(dl-dh),h]
      for j in range(len(cuts)-1):
       l1,h1=cuts[j],cuts[j+1];dt=h1-l1
       ul=U0+(U1-U0)*l1;uh=U0+(U1-U0)*h1
       wl=W0+(W1-W0)*l1;wh=W0+(W1-W0)*h1
       root=(wl+wh-b*(ul+uh))>0
       fl=(1+b+c)*l1+(1+b+d)*(1-l1)
       fh=(1+b+c)*h1+(1+b+d)*(1-h1)
       if root:
        if min(ul,uh,wl,wh)<=1.e-9:return np.array([-1.,0.,0.,0.,0.,0.])
        iu=dt/(ul*uh);iw=dt/(wl*wh)
        inu=dt*(fl/(ul*ul*uh)+fh/(ul*uh*uh))/2
        inw=dt*(fl/(wl*wl*wh)+fh/(wl*wh*wh))/2
        ixu=dt*(l1/(ul*ul*uh)+h1/(ul*uh*uh))/2
        ixw=dt*(l1/(wl*wl*wh)+h1/(wl*wh*wh))/2
        iyu=dt*((1-l1)/(ul*ul*uh)+(1-h1)/(ul*uh*uh))/2
        iyw=dt*((1-l1)/(wl*wl*wh)+(1-h1)/(wl*wh*wh))/2
        V+=(iu-b**3*iw)/(6*alpha)
        E+=(iu-b**4*iw)/(24*alpha)
        N+=(inu-b**4*inw)/(12*alpha)
        X+=(ixu-b**4*ixw)/(12*alpha)
        Y+=(iyu-b**4*iyw)/(12*alpha)
        rootarea+=(iu-b*b*iw)/2
       else:
        kl=(ul-wl)/alpha;kh=(uh-wh)/alpha
        if min(kl,kh)<=1.e-9:return np.array([-1.,0.,0.,0.,0.,0.])
        ik=dt/(kl*kh)
        ink=dt*(fl/(kl*kl*kh)+fh/(kl*kh*kh))/2
        iuk=dt*(ul/(kl*kl*kh)+uh/(kl*kh*kh))/2
        V+=ik/6
        E+=(3+b)*ik/24-iuk/12
        N+=ink/12
        X+=dt*(l1/(kl*kl*kh)+h1/(kl*kh*kh))/24
        Y+=dt*((1-l1)/(kl*kl*kh)+(1-h1)/(kl*kh*kh))/24
    if V<=0 or E<=0:return np.array([-1.,0.,0.,0.,0.,0.])
    return np.array([N/(6*V*E),V,E,N,X,Y])
def objective(v):
    out=evaluate(v)
    return -out[0]
if __name__=='__main__':
    bounds=[(.04,.99),(0.,.9),(0.,.9)]+[(0.,10.)]*10
    seed=int(sys.argv[1]) if len(sys.argv)>1 else 51
    res=differential_evolution(objective,bounds,seed=seed,popsize=16,maxiter=1500,tol=1e-9,polish=True,workers=1)
    out={'seed':seed,'x':res.x.tolist(),'moments':evaluate(res.x).tolist(),'message':str(res.message),'nfev':int(res.nfev)}
    print(json.dumps(out),flush=True)
    open(f'/mnt/data/two_anchor_work/search_{seed}.json','w').write(json.dumps(out)+'\n')
```

### search_cut.py

```python
import sys,json,numpy as np
sys.path.insert(0,'/mnt/data/two_anchor_work')
from search import evaluate
from scipy.optimize import differential_evolution

def objective(v):
 t=evaluate(v)[0]
 w=v.copy();w[3]=0.;w[4]=0.
 tf=evaluate(w)[0]
 return -(t-max(2.,tf))
bounds=[(.04,.95),(0.,.7),(0.,.7)]+[(0.,10.)]*10
seed=513
r=differential_evolution(objective,bounds,seed=seed,popsize=16,maxiter=1600,tol=1e-9,polish=True)
w=r.x.copy();w[3]=w[4]=0
out={'seed':seed,'x':r.x.tolist(),'gain':-r.fun,'moments':evaluate(r.x).tolist(),'flat_moments':evaluate(w).tolist(),'nfev':int(r.nfev),'message':str(r.message)}
print(json.dumps(out));open('/mnt/data/two_anchor_work/search_cut.json','w').write(json.dumps(out)+'\n')
```

### search_flat_b.py

```python
import json,numpy as np
from scipy.optimize import differential_evolution
from search import evaluate
bounds=[(.04,.99),(0,.9),(0,.9)]+[(0,15.)]*6
# variable b,c,d, lower six parameters; 4 upper deficits fixed zero.
def expand(x):return np.array(list(x)+[0.]*4)
r=differential_evolution(lambda x:-evaluate(expand(x))[0],bounds,seed=515,popsize=16,maxiter=1600,tol=1e-10,polish=True)
o={'seed':515,'x':expand(r.x).tolist(),'moments':evaluate(expand(r.x)).tolist(),'nfev':int(r.nfev),'message':str(r.message)}
print(json.dumps(o));open('/mnt/data/two_anchor_work/search_flat_b.json','w').write(json.dumps(o)+'\n')
```

### Original terminal record: search_51.json

437 bytes, SHA-256 c125a94c6eff7c57f6bfe355bba6b03d872599225351871a3acb52d251c109f7.

```json
{"seed": 51, "x": [0.23607872022015466, 0.0, 0.0, 4.701261263162482, 0.0, 4.373764509364796, 6.4212591396773435, 5.983320433566368, 6.772068307662887, 9.999947942786234, 9.999967546050197, 0.06328143716882778, 0.06327892384940116], "moments": [2.0286991525020963, 0.18259509689869974, 0.05244337086524671, 0.11655975031533529, 0.0471490236104714, 0.047148975706736436], "message": "Optimization terminated successfully.", "nfev": 74284}
```

### Original terminal record: search_cut.json

671 bytes, SHA-256 bd45e27929e4d43ba92619e81d4810108fc96527ef7998aab4162a7bdd5a70f0.

```json
{"seed": 513, "x": [0.9449564281877526, 0.0002589944553025858, 9.29660788433484e-05, 5.151401204771583, 3.552713678800501e-15, 3.8569501628897624, 7.769383555323765, 2.6170058836040635, 7.129540217387405, 0.015817899479776187, 1.8431329079181804, 1.6177573129856748, 6.43256483783653], "gain": 3.019806626980426e-14, "moments": [2.00001565367995, 0.16927938123935563, 0.08167174566841981, 0.16590540936278445, 0.042967006211303775, 0.04232557098982984], "flat_moments": [2.00001565367992, 0.1692793812393561, 0.08167174566842002, 0.16590540936278284, 0.0429670062113036, 0.04232557098982952], "nfev": 333022, "message": "Maximum number of iterations has been exceeded."}
```

### Original terminal record: search_flat_b.json

434 bytes, SHA-256 16224018be985acfcaa9ca77b4970b71af6e8d5e92696ce4b6266be1dcb483e9.

```json
{"seed": 515, "x": [0.9500791828749631, 9.863831973433435e-12, 6.211864356231445e-12, 3.6693315053071274e-11, 8.344704252984142, 3.448750808833246, 3.359336681299583, 8.791553226764416, 1.8177969277899333, 0.0, 0.0, 0.0, 0.0], "moments": [1.9999999999908153, 0.16666666667278243, 0.08125329928865545, 0.16250659858252772, 0.041666666669724274, 0.041666666668195525], "nfev": 29098, "message": "Optimization terminated successfully."}
```

Convenience copy: complete new sources, exact reports, and discovery records (`two_anchor_recovery.zip`). The full recovery sources and exact inputs above remain authoritative; this archive is supplementary.
