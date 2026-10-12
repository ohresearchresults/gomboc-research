# material-52810e09ba8f

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# ROOT_CONE_SLICE_DEFICIT_V2

## Evidence and scope
Coordinator analytic theorem for actual uniformly filled proper root-only bodies. These are necessary coupled height/location inequalities, NOT a complete T<51/25 theorem, a high-trace polytope, or a mechanical110 construction. Bounds34<=Cmin<=622 unchanged. The self-contained proof extends ROOT_A_CONE_LOCATION_MOMENT_V1, [internal-source-reference],SHA302ded340f271dfe184b72b8f3620ee26dd10bce2e66ec192a63a5bfcec693a8, read completely. Prior handoff [internal-source-reference] proposed the first deficit inequalities, without preserved code. New here: reflected height bound, sharp affine-test envelope, finite-support strip strengthening, complete exact source, and two provenance corrections. The original uniform measure is never replaced by projective refilling.

## 1. Actual geometry
A=0,B=e_z,C=e_y,D=e_x. P=conv(A,B,C,D,F), with F compact positive-area convex in ell=0,x>0,y>0. Set ell=1-delta*x-epsilon*y-alpha*z, alpha=1-b,epsilon=1-c,delta=1-d,0<b,c,d<1. Negative z is allowed; ABC and ABD are maximal triangles. For ORIGINAL uniform volume define V=int1,t=6V,g=int(x,y,z)/V,u=4gx,v=4gy,w=4gz,m=4ell(g),eta=alpha*epsilon*delta,M=max(b,c,d),W=delta*u+epsilon*v. Thus m=4-W-alpha*w.
Transform to X=delta*x,Y=epsilon*y,q=ell, absolute Jacobian eta. A-radial projection to q0 sends B,C,D to(0,0),(0,1),(1,0). Let Delta be that unit triangle and K=conv(F inXY,Delta),kappa=2AreaK>=1. K has both coordinate-axis bases exactly unit length. Q=cone(A,K) containsP. Forq>=M its section equalsP's: every projected B/C/D generator at that height already lies in its actual A-to-canonical segment, and the root generators are filled toq0. Convexity gives equality of the whole section. The normalized height density p therefore has top law p(q)=3kappa(1-q)^2/(eta*t).

## 2. Planar upper moments
For a planar convex set with nonnegative affine height h, let beta=length(base h0)/|grad h|, areaA0, and coarea widthf(s). Thenf is concave,f0=beta,maxheightR<=H=2A0/beta. Compareg(s)=beta(1-s/H) on[0,H], extendingf byzero afterR. Their masses agree. On[0,R],f-g is concave and zeroat0, so(f-g)/s is nonincreasing; its sign changes only frompositive tonegative, and afterR is nonpositive. Thus int s*f<=int s*g=2A0^2/(3beta).
ForK,h=X orY,beta1 gives int_K X,int_K Y<=kappa^2/6. Also max_K X,max_K Y<=kappa, by the triangle with the opposite unit axisbase. The portion ofK belowX+Y1 is exactlyDelta. Its uppercap has area(kappa-1)/2 and h=X+Y-1,beta1, so int_K(X+Y)<=kappa(kappa+1)/6. Consequently, for positive coefficientsA0,B0,
int_K(A0X+B0Y)<=[max(A0,B0)kappa^2+min(A0,B0)kappa]/6.
The kappa1 limit holds directly.

## 3. Slice deficit and exact moments
Define d_*(q)=kappa(1-q)^2-eta*t*p(q)/3. It is twice the missingXYsectionarea Q_q minusP_q, hence nonnegative and supported on[0,M]. Put
D0=kappa-eta*t; D1=kappa-eta*t*m;
L=kappa(kappa+1)-eta*t*W;
Lx=kappa^2-eta*t*delta*u; Ly=kappa^2-eta*t*epsilon*v.
Then S0=int d_*=D0/3 and S1=int q*d_*=D1/12, since intp1 and intqp=m/4. D0>0 implies D1>0 and4MD0-D1>0: an integrable positive-mass density cannot be concentrated at one endpoint. Zero deficit is handled directly or by limit.

## 4. The missing horizontal moment controls its L^(3/2) norm
For any measurable subsetS of the nonnegative quadrant with areaA,
int_S(X+Y)>=2sqrt(2)A^(3/2)/3.
Proof: Area(S intersect{X+Y>s})>=max(A-s^2/2,0); integrate ins. Equality is the sublevel triangle. With missing area d_*/2, its moment is at least d_*^(3/2)/3. Cone integration gives int_Q(X+Y)=int_K(X+Y)/4, whereas transformed int_P(X+Y)=eta*t*W/24. Therefore
L>=8I, I=int_0^M d_*^(3/2).                            (A)
Weighted quadrant rearrangement similarly gives, for everyA0,B0>0,
max(A0,B0)kappa^2+min(A0,B0)kappa-eta*t(A0delta*u+B0epsilon*v)>=8sqrt(A0B0)I. (B)
Choosing A0=(1+b+c)/delta,B0=(1+b+d)/epsilon directly bounds the ORIGINAL trace numerator, not free location variables.

## 5. Three elementary polynomial consequences
Jensen gives I>=S0^(3/2)/sqrt(M), hence
27ML^2>=64D0^3.                                      (C)
LetH=4S1/S0 and psi=(1-q/H)_+. Sincepsi>=1-q/H, intpsi*d_*>=3S0/4. Holder exponents3/2 and3 with int_0^infty psi^3=H/4 gives I>=3sqrt(3)S0^2/(8sqrt(S1))=D0^2/(4sqrt(D1)). Thus
L^2D1>=4D0^4.                                       (D)
Reflectionq->M-q gives
L^2(4MD0-D1)>=4D0^4.                                (E)
H need not be<=M: extending the test integral toinfinity merely weakens a valid inequality.

## 6. Full affine-test envelope and its sharp scalar minimizer
For everyh>0,f(q)=(h-q)_+ satisfies intf*d_*>=max(hS0-S1,0), and int_0^M f^3=[h^4-(h-M)_+^4]/4. Holder and(A) prove
27L^2[h^4-(h-M)_+^4]>=4(4hD0-D1)_+^3, for allh>0.    (F)
Also apply the reflected family D1->4MD0-D1. Its large-h limit is(C); it improves(D)/(E) by retaining finite support.
The complete scalar minimization of int_0^M f^(3/2), f>=0, massS0 andfirstmomentS1, is explicit. Write z=S1/(MS0). For0<z<=1/4, the unique minimizer is a squared decreasing affine function on[0,4Mz], zero thereafter, and Imin=3sqrt(3)S0^2/(8sqrt(S1)); z>=3/4 follows by reflection. For1/4<=z<=3/4, let r>=0 solve
(4z-3)r^2+(4z-2)r+(4z-1)=0,
with r=infinity atz3/4. The minimizing density is proportional to(1+(r-1)q/M)^2, and
Imin^2=27S0^3/(16M)*(r^3+r^2+r+1)^2/(r^2+r+1)^3.
Proof: equality in the corresponding positive-part Holder test holds for exactly an affine square. Its mass andmean yield z(r)=(3r^2+2r+1)/(4(r^2+r+1)), strictly increasing from1/4 to3/4; the derivative's numerator isr^2+4r+1>0. Strict convexity proves global uniqueness, not just stationarity. Hence in the middle regime,
ML^2(r^2+r+1)^3>=4D0^3(r^3+r^2+r+1)^2.              (G)
The family is strictly stronger than(C),(D),(E): exact scalar tuple D0=3,D1=4,M=1,L=901/100 satisfies allthree strictly but violates(F) ath3/2. This tuple is NOT claimed to be a density or body.

## 7. Directional strip losses
At heightq the missing set's Y-extent is at most kappa(1-q). Its Xmoment, for areaA=d_*/2, is at least A^2/[2kappa(1-q)]=d_*^2/[8kappa(1-q)], by the same layer-cake argument. Thus
kappa*Lx>=3int_0^M d_*^2/(1-q), and likewiseLy.      (H)
Let A_M=M-M^2/2,B_M=M^2/2-M^3/3,C_M=M^3/3-M^4/4,Delta_M=A_MC_M-B_M^2=M^4(M^2-6M+6)/72>0.
Weighted Cauchy, or expanding int[d_* /(1-q)-a-bq]^2(1-q)>=0 and optimizing a,b, gives int d_*^2/(1-q)>=(C_MS0^2-2B_MS0S1+A_MS1^2)/Delta_M. Therefore
48Delta_M*kappa*Lx>=16C_MD0^2-8B_MD0D1+A_MD1^2,
and the same forLy.                                  (I)
Using the larger interval[0,1] gives the weaker convenient inequalities
4kappa*Lx,4kappa*Ly>=8D0^2-8D0D1+3D1^2.              (J)
All moments in these formulas are of one and the same P.

## 8. Radial filling and projective location
For root directionp inK, let h(p) be the fraction of its A-to-root segment filled byP. Put Ij=int_K h^j. Direct original-volume integration gives eta*t=2I3 and m=4-3I4/I3. Powermean I4/AreaK>=(I3/AreaK)^(4/3) yields m<=4-3(eta*t/kappa)^(1/3), or withlambda=kappa/t,
lambda(4-m)^3>=27eta.                                (K)
Under projective coordinates s=q/(1-q), the lowerroof phi=1/h-1 is convex and h=(1+phi)^-1. The original density is1/[eta(1+s)^4]. In particular u=3int_K pXh^4/(delta I3),v=3int_K pYh^4/(epsilon I3); replacing these with free horizontal moments loses actual geometry.

## 9. Exact formal control and corrected provenance
All following input numerators have denominator10^6:
b698790,c429624,d269604,t4553454,rho315569,omega146601,gamma314802,u2433965,v3116075;lambda=1-rho-omega-gamma. Its four-law mixture is lambda*mu[1,c,d,b]+rho*mu[c000]+omega*mu[cd00]+gamma*mu[cdb0]. Setm to the weighted knot sums andw=(4-delta*u-epsilon*v-m)/alpha.
The exact trace is88391785273906250/43151360396679507, approximately2.048412482511397. The priorhandoff's3715650164016236260/1818209506696777731 is NOT the trace of these literal inputs and is withdrawn for this object.
The new Fraction source checks every knot interval: full density positivity, nonnegative quadratic discriminant ensuring sqrt-density concavity, C1joins and doublezero at1, exactmass1/meanm4, and pointwise cone domination. It also checks oldL,Lx,Ly positivity,b+c>9/8,u+v<t+1,2-t<w<t+2-u-v, and actual-form full-t C/D endpoint cuts. Nevertheless(C),(D) and directional strip bounds fail. This is a FORMAL relaxation separator, NOT an actual or stationary polyhedron.
The previously proposed seven-law ordering also failed. Put last=(lambda-1/t)/(1-b),j=gamma-b*last. Correct nonnegative masses are[1/t,rho,0,omega,0,j,last] on T0=[1,b,c,d],CFFF=[c000],CBFF=[cb00],CDFF=[cd00],CAFF=[c100],CBDF=[cbd0],CADF=[c1d0]. Source verifies equality of EVERY piecewise quadratic density coefficient. The old ending[c1d0],[c1b0] does not give that identity. None of these formal fan weights asserts realization.

## 10. Complete durable recovery source
Exact source material [internal-source-reference], filename source-48d39b7cbd9fadbcc87fd3f7ca7b4505f32882bb2aa7d59e8a0db753ca0ad3fd.txt,7458B,SHA18a96fa5b221a769c9f60389fe57fa671cf27d0fc1a3d48d2714971c05334b40, was accepted according to the current state. Save those literal UTF8 bytes as deficit_exact.py. No external inputs,RNG,omittedhelpers,or nonstandarddependencies. CPython3.13.5stdlib,assertions enabled. Reconstruction/verification:
python -S deficit_exact.py > deficit_control.out
sha256sum deficit_exact.py deficit_control.json deficit_control.out
Expected report deficit_control.json6450B,SHAc2eee89ba9cbed67bc1653b1ae74fd101d93803bb90afc09d722b07d8001dd97; stdout526B,SHA74f4743f5404c46b400d3f7dd7df2556a5b59463dacb8b61fe430d505b7292d0. Expected terminal markers:

[Encoded source block omitted; the code in this passage is incomplete.]

T=88391785273906250/43151360396679507
report_bytes=6450
report_sha256=c2eee89ba9cbed67bc1653b1ae74fd101d93803bb90afc09d722b07d8001dd97
ROOT_CONE_SLICE_DEFICIT_V2_RECOVERY_PASS
Normal coordinator execution succeeded. No separate cold pass is claimed at storage. The capsule preserves an exact formal control and reusable full-interval method, not a new canonical best polyhedron.

## 11. Open interface
All stated low-endpoint root-only VALUE bodies satisfy these inequalities; no stationarity or zsign was assumed. No whole T>=51/25 contradiction is yet proved. Next useful question: does the sharp envelope together with the actual C-fan and convex projective roof close the residual class, or does a formal control passing these cuts identify a stronger missing same-body compatibility? The two proper33 offroot charts are a separate full-maximum direction. The mechanicalE17 bridge and exactminimum remain open.
