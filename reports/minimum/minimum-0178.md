# minimum-0178

Historical AI scientific report · saved 2026-09-22 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; runtime-path-removed; unreviewed-encoded-blocks-omitted.

---

# PROPER33_STATIONARY_L_AND_U_SMALL_D_EXCLUSION_V1

## 1. Result

The entire **L_D chart is excluded at a full maximum with T>=2**. In the U_D chart, the entire both-negative C/D sector is excluded at T>=51/25, together with a continuous mixed-sign sector extending strictly past G(D)=r/6.

Precisely, retain the accepted hypotheses of the literal parent: positive endpoints a>b>0, c>=d>0, positive root area, true maximal coordinate triangles ABC and ABD, true canonical marks, negative-z material, and a full marked-body[private-runtime-path] polyhedral local maximum with a negative C/D value. Retain the inherited **same-body joint moment inequality**

    gx,gy>=1/4,  4(gx+gy)<=t+1,  t=6V.                (J)

Then:

**L.** No L_D maximum has T>=2.

**U.** A non-root-only maximum with T>=51/25 must be U_D and must satisfy

    G(C)<0,
    G(D)/r > eta_* := 581537111/3371659200
                     approximately 0.1724780223932478
                     >5/29>1/6.                      (U)

In particular, the entire U_D class with G(D)<=5r/29 is closed at the target threshold, including all G(D)<=0. The exact constant eta_* is a sufficient separation from zero, **not an asserted optimal constant**.

Consequently, every full proper33 negative-z maximum in the stated negative-anchor domain with G(C),G(D)<=0 and T>=51/25 is **root-only**. The remaining positive-ell-auxiliary complement is just U_D with the strict, quantitatively separated mixed signs in (U). These are full-maximum exclusions, **not value bounds for every nonstationary body with these incidences**. The whole remaining mixed U_D chart is not excluded.

The proof identifies an improving true-facet motion. In L_D, T>=2 forces the whole ADU hinge to have strictly negative outward work. In U_D, T>=51/25, b+c>=9a/8 and G(D)<=eta_* r force the whole BDU hinge to have strictly negative outward work. Moving the respective entire triangular support inward therefore strictly increases the original T. The root and all four canonical marks remain fixed during this local motion.

## 2. Reading, authority, and evidence tier

I read the complete new 1,800-line journal through EOF, including the common notebook, branch update, literal parent, and both embedded source units. The earlier unchanged evidence remains in this chat. The supplied parent source, JSON and stdout were also read in full. No earlier source has been replaced by an inferred alias.

The new journal is 295,216 bytes, SHA-256:

    252eaeb9e4ce9551a0ce9876c9c44b737778e51e7f9951d9e673e4d1acd75d6a

Required literal parent:

    minimum-0176
    SHA-256 9b2d327e6f4fbd2bfdf827e072ff769efde7981b0257bb418cc5e5f4df5aabe2

Its complete two-chart reduction, true incidences, full-volume cone budget and original-density conventions are accepted working premises. The parent expressly did not close either simultaneous stationary system. :contentReference[oaicite:0]{index=0}

The additional inherited input is (J), as recorded in the supplied common notebook's actual fan-variable bounds. It is a relation for the **same actual body**, not a newly fitted moment constraint. The endpoint screen used below is likewise the accepted actual-body large-endpoint theorem. I did not replay the larger archived endpoint certificate; its exact archive is not supplied for a computational successor. The present polynomial certificate and controls have no computational dependency on that archive. :contentReference[oaicite:1]{index=1}

The new statements are analytic deductions under these accepted inputs. Exact algebra and actual-control recovery were executed normally and then in an empty directory from the new source alone. They are not proof-assistant formalizations. No new parent conflict was found; the earlier B-B correction to 61/2040 is already incorporated in the supplied update.

## 3. One actual body and its necessary inequalities

Use

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    s=a+b, hc=s+c, hd=s+d, alpha=a-b,
    ell=a+(d-a)x+(c-a)y-alpha*z,
    n=hc*x+hd*y,
    V=int_P1, J=(X,Y,Z)=int_P(x,y,z),
    E=int_Pell, N=int_Pn,
    g=J/V, mu=E/V, r=N/V, q=N/E=Tt,
    t=6V, T=N/(6VE), G=n-r-q*ell.

E is the ell integral, not an edge count. In particular r=6TE and q=Tt. All quantities below use these same original uniform integrals.

The parent full-boundary fan gives, at every p in the actual proper33 body,

    24E >= n(p)+t*ell(p).                             (C)

The entire boundary is coned from p: the true ABC and ABD pyramids contribute x(p)/6 and y(p)/6, and the apex ell(p) contribution uses the whole V. The parent explains why the t in (C) is not merely the volume of conv(T0,p). :contentReference[oaicite:2]{index=2}

Because c>=d, (J) implies

    4r=4hc(gx+gy)-4(hc-hd)gy <= hc*t+hd.              (M)

At C, (C) gives

    4r/T >= hd+t*c.                                  (C_C)

Consider a genuine maximal two-mark triangle XDU, where X=A or B, and put

    e_X=ell(X), w=ell(U)>0,
    H_XD=G(X)+G(D)+2G(U).

Its whole hinge has the sign of H_XD. In fact, since X,D have y=0,

    int_XDU G*y/|grad f_XD|
      =Area_xy(XDU)*y(U)*H_XD/12.                    (H)

Both factors outside H_XD are strictly positive. This is the entire maximal triangle, not a triangle inside a pentagon.

Using (C) at U and r=6TE gives the following signed inequality, whether or not the hinge is stationary:

    H_XD <= hc+(8/T-4)r-q(e_X+d)-2(q+t)w.

For T>=2, substitute the lower bound (C_C) into its nonpositive r coefficient:

    H_XD <= hc-(T-2)hd
             -t[T(e_X+d)+(T-2)c+2(T+1)w].            (S)

Thus **even the weaker assumption H_XD>=0**, not merely stationarity H_XD=0, forces the parent's inequality (11). This observation is what converts the exclusions below into explicitly signed whole-facet ascents.

## 4. The entire L_D chart: a continuous contradiction

For L_D, X=A. Suppose T>=2 and H_AD>=0. Equation (S), w>0 and c,d>0 imply

    2(a+d)t < hc.                                    (L1)

Meanwhile (C_C) and (M) imply

    (T-1)hd <= (hc-Tc)t.

At T>=2 this gives

    hd <= (s-c)t.                                    (L2)

In particular s-c>0. Combining (L1)-(L2) requires

    2(a+d)hd < (s-c)hc.

The exact difference is instead

    (s-c)hc-2(a+d)hd
      = b^2-a^2-c^2-4ad-2bd-2d^2 <0,

because a>b>0 and c,d>0. Contradiction. Therefore H_AD<0 and the entire inward ADU hinge is an ascent.

This proof is independent of the endpoint screen, G(D)'s sign and the root reaction equations. More generally it excludes T>=2 stationarity of any genuine two-mark ADU triangle with ell(U)>=0 under these proper33 and same-body moment premises. The analogous ACU triangle with the larger endpoint c is already impossible directly from (C): its stationary/nonnegative hinge would require 2(a+c)<=hd, whereas 2(a+c)-hd=a-b+2c-d>0. A three-mark ACD facet is not covered: the proposed two-mark hinge would move D and is not an allowed variation of that three-mark facet.

## 5. U_D: elimination of the actual volume parameter

Scale ell and its endpoints by 1/a, so a=1 without changing the body, q, T or G(D)/r. Write

    hc=1+b+c, hd=1+b+d,
    A_T=T(b+d)+(T-2)c,
    B_T=hc-(T-2)hd.

For U_D, X=B. Suppose T>=tau=51/25 and H_BD>=0. Equation (S) gives

    A_T>0, B_T>0, t*A_T<B_T.                         (U1)

From (C_C)-(M),

    (T-1)hd <= (hc-Tc)t,

so hc-Tc>0. Combining this with (U1) gives

    P(T):=(hc-Tc)B_T-(T-1)hd*A_T >0.                 (U2)

Next suppose G(D)<=epsilon*r, with 0<=epsilon<3. Since

    G(D)=hc-r-q*d,

we have

    4hc <= (1+epsilon)(hc*t+hd)+4Ttd.

Both

    L_epsilon=4hc-(1+epsilon)hd>0,
    C_epsilon(T)=(1+epsilon)hc+4Td>0.

Thus L_epsilon<=C_epsilon(T)t and (U1) imply

    Q_epsilon(T):=C_epsilon(T)B_T-L_epsilon*A_T>0.     (U3)

No volume, centroid or star mass was independently optimized in this elimination. These are consequences of the actual t,r,mu,w, together with the single whole BDU hinge sign.

### Threshold monotonicity

Freezing T=tau is justified by exact derivatives, not an approximation. For all b,c,d>0,

    P'(2)=-4b^2-bc-7bd-5b-c^2-c-3d^2-4d-1<0,
    P''(T)=-2(b+d)(b+d+1)<0.

For 0<=epsilon<3,

    Q_epsilon'(2)
      =-4b^2-8bc-(7-epsilon)bd-(5+epsilon)b
       -4c^2-4c-(7-epsilon)d^2-8d-epsilon-1<0,
    Q_epsilon''(T)=-8d(b+d+1)<0.

Hence (U2)-(U3) require P(tau)>0 and Q_epsilon(tau)>0 throughout the entire real T>=tau domain.

## 6. Exact endpoint certificate, including a positive mixed-sign interval

Define these integer polynomials:

    P0=625P(tau)
      =600-726b^2-25bc-2677bd-126b
          -650c^2-25c-1326d^2-1351d,

    Q0=625Q_0(tau)
      =600-3225b^2-3950bc+2321bd-2625b
          +525c^2+1150c+1071d^2+1046d,

    D0=1875b^2+1250bc+2525bd+2475b
          +625c^2+1250c+1275d^2+1250d+600.

Then

    625Q_epsilon(tau)=Q0+epsilon*D0,

and every coefficient of D0 is positive.

The accepted negative-z full-maximum theorem gives

    T<3(1+b+c)/(2+b+c),

so a putative target maximum requires b+c>9/8. This condition is explicitly retained in the local ascent statement; it is not imposed on arbitrary bodies by a clipping operation. :contentReference[oaicite:3]{index=3}

The accepted actual-body large-endpoint screen gives

    R=9405c^2+1013cd+10418c(1+b)
       +1750d^2-6737d(1+b)-8487(1+b)^2 <0,           (R)

as well as 0<b<1, d<3/4 and c<943(1+b)/1352<7/5, whenever T>=tau. These are inherited actual-body exclusions, not newly asserted realizability conditions. :contentReference[oaicite:4]{index=4}

Put h=b+c-9/8, so h>0. The decisive exact identity is

    14P0+6Q0+D0-R = -F(b,d,h),                       (I)

where

    F=664(b-1301/5312)^2 + 19593911/42496
      +13277bd+3758bh+12613d^2+1013dh
      +(46325/8)d+14730h^2+(71521/2)h.                (F)

Every displayed term after the square is nonnegative on b,d,h>=0, and the constant

    K=19593911/42496

is strictly positive. Identity (I) is verified by direct coefficient comparison in the source.

For epsilon=1/6, the left side of (I) is exactly

    14P0+6[625Q_(1/6)(tau)]-R.

It would be positive by (U2), (U3) and R<0, but (I) makes it negative. This alone excludes the entire G(D)<=r/6 sector, without a bounded shape-parameter search.

### Extension to 5/29 and the stronger eta_*

On the whole closed endpoint box

    0<=b<=1, 0<=c<=7/5, 0<=d<=3/4,

coefficient positivity gives

    D0<=Dmax=D0(1,7/5,3/4)=211575/16.

For epsilon=5/29,

    14P0+6[625Q_(5/29)(tau)]-R
       =-F+D0/29
       <=-K+Dmax/29
       =-6280219/1232384<0.                          (G)

Thus the whole closed G(D)<=5r/29 sector is excluded with an explicit positive algebraic margin. No sampling or feasibility pruning occurs.

In fact the same calculation works with

    eta_*=1/6+K/(6Dmax)=581537111/3371659200.

The right side is then nonpositive, still contradicting the strictly positive required left side. This proves (U), including exclusion of equality G(D)=eta_* r. For reference,

    eta_*-5/29=6280219/97778116800>0.

The proof covers every finite u,v,kappa,lambda realizing the true chart, however large or small; none of these variables appears in the final certificate. Its endpoint polynomial inequalities also hold on the displayed closed box and h>=0. This does not identify a degenerate limiting incidence with the strict eight-vertex chart; those incidence boundaries remain governed by the parent classification.

### Useful retained endpoint-dependent cut

For any remaining candidate put delta=G(D)/r. The actual lower bounds gx,gy>=1/4 imply delta<3, since r>hc/4 and delta=hc/r-1-d/mu. Thus the preceding Q_delta monotonicity remains valid. A remaining candidate must satisfy

    delta > 1/6+[F(b,d,h)+14P0-R]/(6D0).              (CUT)

This is stronger than the uniform eta_* bound and keeps the endpoint information instead of immediately replacing D0 by its box maximum. It is another necessary cut, not a sufficiency assertion for a body or a stationary solution.

## 7. The true inward motion and what it does not prove

In L_D the three true neighbors of U are A,D,Q; in U_D they are B,D,R. Write X=A and W=Q in the first case, X=B and W=R in the second. W lies on the fixed root. Move

    U_theta=(1-theta)U+theta W,  0<=theta<=1,

keeping the other seven vertices fixed. For 0<theta<1 this is the inward pivot of the entire true triangle XDU about XD. Equivalently decrease v in fAD=z+vy for L_D, or decrease lambda in fBD=1-z-x-(1-lambda)y for U_D. All canonical points and all three root vertices stay fixed.

The actual simple-vertex cone proves the removed part is exactly tet(X,D,U,U_theta). In affine cone coordinates based on U and its three true neighbors, every other true vertex has nonnegative coordinates whose sum is at least one; otherwise it would lie inside the neighbors' tetrahedron. This verifies the whole interval of inward cuts up to the neighbor plane. It is not an independent displacement of integration triangles.

Let

    Delta=Vol(tet(X,D,U,W))>0,
    L=e_X+d+2w,
    K_n=n(X)+n(D)+2n(U).

The original uniform moments on this actual path are exactly

    V_theta=V-Delta*theta,
    J_theta=J-(Delta*theta/4)(X+D+2U)
                -(Delta*theta^2/4)(W-U),
    E_theta=E-(Delta*L/4)theta+(Delta*w/4)theta^2,
    N_theta=N-(Delta*K_n/4)theta
                -(Delta/4)[n(W)-n(U)]theta^2.

Here X,D,U,W in the J equation denote their position vectors. In particular,

    dT_theta/dtheta at 0 = -Delta*H_XD/(24VE)>0

in the excluded high-trace sectors. Root geometry is held fixed because the actual pivot triangle has no root vertex; the bulk moments change by this same physical tetrahedral sliver.

The full trace-comparison polynomial is

    N_theta-6T V_theta E_theta
      =(Delta/4){-H_XD*theta
          -[G(W)-G(U)+6T*Delta*L]theta^2
          +6T*Delta*w*theta^3}.

This also records a useful limit of the method: at a hypothetical zero hinge, its quadratic coefficient need not favor removal. **No assertion that deleting U completely raises T is made.** The new result is the strictly signed local ascent under the proved sector conditions, not a substitute for the separately active global deletion/value problem.

## 8. Exact controls and actual verification

No new body is presented as a stationary or high-trace witness. The capsule independently reconstructs all three unchanged rational parent controls, including their complete true facets and edges, from the exact seven halfspaces. All have endpoints

    (a,b,c,d)=(1,1/2,7/10,1/20).

The exact slope tuples (u,v,kappa,lambda) are

    L_mixed:        (1/99,1/10,10,4/5),
    U_mixed:        (1,2,1/50,101/49),
    U_both_negative:(11/10,2,1/50,101/49).

Their recovered T values are approximately 1.502496380229249, 1.400125863440336 and 1.377434209075113. Their own G(D)/r values are approximately 0.030713672557679, 0.041733298165115 and -0.054974370107418. Thus both-negative signs and small positive G(D) certainly occur in actual geometry below the stated threshold; the new theorem must not be read as an unconditional geometric impossibility.

All three are true 8/13/7 proper33 bodies, have one negative-z positive-ell auxiliary, positive G at every auxiliary, both coordinate-mark supports, and positive root area. Their original V,J,E,N,T,G, vertex lists, facets and edges were compared **exactly** with the supplied parent JSON and matched. Original A- and B-apex fans and a third interior-apex fan agree. The genuine B-root pyramid has E_root=b V_root/4. Their whole hinges and root reaction residuals are nonzero, so none is stationary. Their actual own-centroid Euclidean mechanics remain strict 446,345,345, weak000; all 156 true-edge primal/polar primitives are nonzero. The parent provides these controls as nonstationary bodies, not as 110 attainments. :contentReference[oaicite:5]{index=5}

The new exact report retains every original integral and full fan piece, adds the actual joint-moment slack, normalized G(D), and complete quadratic moment polynomials for the genuine inward ear path. The source below is a complete reconstruction recipe; the report is not the only source of any continuation-critical datum.

## 9. Remaining actual system

At the target threshold, the positive-ell-auxiliary complement is now only U_D with (U) and (CUT). Its exact seven supports are

    x>=0, y>=0, ell>=0,
    z+ux>=0, z+vy>=0,
    1-z-y-(1-kappa)x>=0,
    1-z-x-(1-lambda)y>=0.

After a=1, the seven actual parameters are b,c,d,u,v,kappa,lambda. With labels A0,B1,C2,D3,U4,P5,Q6,R7:

    U=AD/BC/BD, P=AC/BC/root, Q=AC/AD/root, R=AD/BC/root;
    maximal facets:
    (012),(013),(0256),(03476),(12574),(134),(567);
    true edges:
    AB,AC,AD,AQ,BC,BD,BU,CP,DU,UR,PQ,PR,QR.

All three root vertices are below z=0. Retain strict off-facet support slacks, positive root area and ell(U)>0; positive parameter values alone do not certify this incidence.

The remaining equations are still the four whole-facet hinges

    int_AC Gx/kAC=int_AD Gy/kAD=int_BC Gx/kBC=int_BD Gy/kBD=0,

and the full root reactions, with p=X+Y and k0=|grad ell|,

    int_root G/k0=qV-3p,
    int_root Gx/k0=qX-Y,
    int_root Gy/k0=qY-X,
    int_root Gz/k0=qZ-p.

There are three independent root equations. They are reactions of the original root/body/frame objective, not independent moment fits. :contentReference[oaicite:6]{index=6} The new proof does not purport to solve this full system outside the excluded sector: it proves that a necessary subsystem already fails inside the stated sector.

The most useful continuation is this single, strongly mixed U_D system with its actual root triangle and the endpoint-dependent cut retained. The parent L_D determinant problem and the U_D both-negative search are no longer the appropriate high-trace frontier under (J).

## 10. Recovery capsule

Exact dependency versions and commands:

    CPython 3.13.5
    SymPy 1.14.0
    assertions enabled; no random input; no parent import or external data

    python proper33_stationary_sector_v1.py > proper33_stationary_sector_v1.out
    sha256sum proper33_stationary_sector_v1.py \
      proper33_stationary_sector_v1.json proper33_stationary_sector_v1.out

Pins for the complete source below and its outputs:

    source: 13035 bytes
    SHA256 c061d9fc5ee52dfdf7cd26f5f4f6135741b7ee5b7a97338c6c8286ef6b4d80bc
    report: 46890 bytes
    SHA256 1122d59373a64677538a9fb5962d16925e0ea2978858d7f14b2ef6e224e7528a
    stdout: 942 bytes
    SHA256 9913b68485e62a36e760e62a806a8868a19ea64d22d5e999a0e79f8d107e78b2

Complete expected stdout:

    L_CHART_T_GE_2_POSITIVE_ENDPOINT_IDENTITY_PASS
    U_CHART_ENDPOINT_ELIMINATION_AND_MONOTONICITY_IDENTITIES_PASS
    GLOBAL_SOS_14_P_PLUS_6_Q_MINUS_R_PASS

[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]

    U_mixed T=5374273708344352525/3838421850974805261 GD/r=75088313107502860279711607/1799242245614526488613593893
    U_both_negative T=51633397849952286673900/37485200752072113976791 GD/r=-56808876852835876700371460281337/1033370218555175692228106025518337
    report_bytes=46890
    report_sha256=1122d59373a64677538a9fb5962d16925e0ea2978858d7f14b2ef6e224e7528a
    PROPER33_STATIONARY_SECTOR_V1_RECOVERY_PASS

Normal execution and a separate empty-directory source-only execution were actually completed, with byte-identical report and stdout. Optional copies: [source](sandbox:/mnt/data/proper33_stationary_sector_v1.py), [full report](sandbox:/mnt/data/proper33_stationary_sector_v1.json), [stdout](sandbox:/mnt/data/proper33_stationary_sector_v1.out).

The search for a hinge determinant was not resumed. The useful connection was the actual joint first-moment budget (J) with the parent's full-t cone bound. Exact polynomial elimination and an exact choice of positive multipliers produced (I); the complete identity, rather than success or failure of a numerical search, proves the continuous exclusion.


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


## 11. Scope and unresolved minimum

The only added research premise beyond the parent reduction is the explicitly retained inherited same-body inequality (J), together with the already accepted actual-body endpoint screen at the target threshold. No independently weighted triangle/star, surrogate G, extra root-moment completion, or assumed simultaneous stationarity of integration triangles is used. The all-positive endpoints, a>b, proper33, true maximal triangles and actual uniform filling are essential hypotheses. No statement is made for a fixed-lattice or fixed-sign constrained optimizer that lacks the accepted full-class reactions.

The remaining strongly mixed U_D chart is genuinely unresolved here. Low-endpoint negative-z root-only VALUE, zero endpoints, other protected-facet patterns and the actual trace-to-mechanical-incidence bridge remain separate. In particular, no numerical determinant survey is an exclusion, and an auxiliary 8/13/7 trace reduction is not a mechanical E17 decrement. There is no new 110 attainer and no change to 34<=C_min<=622; the whole minimum remains open. :contentReference[oaicite:7]{index=7}
