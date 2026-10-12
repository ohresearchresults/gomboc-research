# material-b1d05ed4c845

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# ROOT_FAN_BERWALD_MOMENT_OBSTRUCTION_V1

## Status and scope

These are necessary geometric moment conditions for an actual uniformly filled convex three-dimensional body with two canonical supporting triangle patches, and stronger conditions at a genuine joint local maximum of the original adjacent-triangle trace. They eliminate an entire previously surviving formal covariance fiber at T=11/5. They do NOT prove the universal T<51/25 bound. A second, exactly specified, UNREALIZED formal moment datum at T=51/25 passes the finite collection of necessary conditions listed below. It is not a polyhedron, not an asserted realizability result, and not a counterexample to the trace conjecture. No new equilibrium count, registry delta, C34 exclusion, or attaining110 construction follows. The accepted minimum bracket remains34<=Cmin<=622.

The background stationarity identities were established in ROOT_DUALITY_JOINT_VARIATIONS_V1, complete proof [internal-source-reference], SHA73eb04d63deeab693d29533819d3b95c4e1af3cc01d756987381aaa2bb4c2ed8, and exact audit [internal-source-reference]. The actual local rigidity statement G>0 at all noncanonical vertices is in [internal-source-reference], SHA8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9. Both full proofs were read before this extension. The principal identities needed here are derived again below, so the new inequalities can be read without those files. No claim of priority is made for the classical affine moment inequality.

## 1. One actual body and notation

A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0), T0=conv(A,B,C,D). Let P contain T0 and lie in x>=0,y>=0, with ABC and ABD supporting patches. They need not be entire maximal faces for the inequalities below. Define a nonzero affine support function

ell=a+(d-a)x+(c-a)y+(b-a)z>=0 on P,

with root face F=P intersect {ell=0} of positive area. Let

n=(a+b+c)x+(a+b+d)y,
V=Vol(P), E=integral_P ell, N=integral_P n,
g=(u,v,z)=actual UNIFORM volume centroid,
t=6V, p=u+v, r=n(g), mu=ell(g), q=N/E=tT,
T=N/(6VE)=r/(t mu), m=3p/t,
w=(v/(3p),u/(3p),1/3), G=n-r-q ell, beta=grad G.

Here ell is a root SUPPORT FUNCTION, not a physical density. Covariance Sigma is that of the same uniformly filled P. In particular E=Vmu and N=Vr. We assume r>0,mu>0,t>1 in the high-trace situation.

Root-variation conclusions explicitly assume a genuine joint local maximum with a,b,c,d>0, allowing arbitrary sufficiently small two-sided affine rotations/translations of the root support while retaining the other constraints, and G>0 on F. The last positivity follows at the accepted polyhedral high-trace maximizer from the actual vertex-shave argument, because all canonical points then lie strictly off the root. It is stated as a hypothesis here rather than silently transferred to zero-endpoint walls.

## 2. Affine second moments of an actual convex body

### Lemma
If K is a full-dimensional convex body in R^n with uniform probability measure and f>=0 is affine, then

E_K f^2 <= [2(n+1)/(n+2)] (E_K f)^2.

For n=3 this is Var_K(f)<=3(E_K f)^2/5. For n=2 the raw second moment is at most3(E_K f)^2/2. If f is everywhere strictly positive on compact K, the inequality is strict (unless the zero-dimensional situation, not relevant here).

### Elementary proof
The constant case is immediate and strict when the constant is positive. Otherwise put M=max_K f, V0=Vol(K), and Q(s)=Vol({x in K:f(x)>=s}) for0<=s<=M. Brunn--Minkowski applied to these actual nested superlevel bodies gives concavity of psi(s)=Q(s)^(1/n). Let A0=(n+1)E_K f and compare Q with Qc(s)=V0(1-s/A0)_+^n. Both have the same integral over s>=0, by the layer-cake formula.

First M<=A0. If M>A0, the concave difference psi(s)-V0^(1/n)(1-s/A0), whose value at0 is0 and whose value at M is positive, is positive on(0,M). This gives Q>Qc on(0,A0) as well as nonnegative extra mass beyond A0, contradicting equality of their integrals.

On[0,M], the same difference divided by s is nonincreasing by concavity and its zero value at0. Consequently Q-Qc has at most one sign change, from positive to negative; after M it is nonpositive. The equal integrals imply integral s(Q-Qc)ds<=0. Therefore

E_K f^2 = (2/V0) integral sQ(s)ds
 <= 2 A0^2/[(n+1)(n+2)]
 = [2(n+1)/(n+2)] (E_K f)^2.

Equality in the weighted integral comparison requires Q=Qc almost everywhere. If min_K f>0, Q is constant near0 while Qc decreases, so equality is impossible. This proves the strict form used on F.

External primary reference checked: Dylan Langharst and Eli Putterman, Weighted Berwald's Inequality, arXiv:2210.04438, v7 dated12August2024, Theorem1.1 (the classical Berwald inequality), PDF https://arxiv.org/pdf/2210.04438. The relevant PDF page was visually read. The proof above establishes exactly the affine special case needed here.

### Geometric equivalent
For actual covariance Sigma, the inequality holds for every affine support function c+alpha.x>=0 on P. Hence the ellipsoid

g+sqrt(5/3) Sigma^(1/2) {v:|v|<=1}

is contained in P. This follows by checking every supporting halfspace. It is a necessary containment, not a replacement of P by an ellipsoid or a sufficient mechanical criterion.

## 3. Projective stationarity and elimination of an entire covariance fiber

The canonical-point-fixing projectivity

Phi_epsilon(x)=(I+epsilon diag(s))x/(1+epsilon s.x)

fixes A,B,C,D. It must be uniformly refilled after transformation. Its infinitesimal velocity is diag(s)x-(s.x)x and divergence tr(diag(s))-4s.x. The transported affine root has endpoint derivatives a'=0,b'=-b s_z,c'=-c s_y,d'=-d s_x. Thus its total transported derivative is -ell(s.x).

Let Bn=a+b+c,Dn=a+b+d. The direct endpoint derivative of n is -b s_z(x+y)-c s_y x-d s_x y. Combining this with position transport and the volume Jacobian, differentiating log T at a genuine maximum gives

0=-sum_i s_i + [(Bn u-dv)s_x+(Dn v-cu)s_y-bp s_z]/r
  +4s.g -(5/r) s.Sigma beta.

Here the means cancel because E(n-qell)=0. Since s is arbitrary and r=Bn u+Dn v, this is exactly

5 Sigma beta = (4ru-(a+b+2d)v,
                4rv-(a+b+2c)u,
                4rz-r-bp).

This derivation uses actual volume and actual covariance, not independent formal moment choices.

The contained tetrahedron T0 has volume1/6, centroid g0=(1/4,1/4,1/4), covariance Sigma0=(4I-11^T)/80. Decompose uniform P into T0 and its complement, of probability masses1/t and(t-1)/t. Jensen for the complement yields

Sigma >= Q0 := Sigma0/t+(g-g0)(g-g0)^T/(t-1).

Write h for the right side of the stationarity equation divided by5, y=h-Q0 beta and delta=beta.y. For K=Sigma-Q0>=0, K beta=y. Therefore delta>=0. If delta=0, positivity forces y=0. If delta>0, matrix Cauchy--Schwarz gives

K >= yy^T/delta,
Sigma >= Qstar := Q0+yy^T/delta.

Apply the affine second-moment lemma to ell, with alpha=grad ell. Every ACTUAL covariance in this entire fiber must satisfy

D0 := (3/5)mu^2-alpha^T Q0 alpha >=0,
delta D0-(alpha.y)^2>=0.

Equivalently alpha^T Qstar alpha<=(3/5)mu^2. The same necessary inequality holds for every other genuinely nonnegative affine function on P. Testing a finite list of functions is not the same as testing all supports of an unknown body.

## 4. Exact root moment identities

Put k=|grad ell| and I(h)=integral_F G h dA/k. Perturb the root to ell+epsilon h while holding other facet supports fixed. All affine h are admissible locally under the strictly positive canonical endpoint hypothesis. The direct numerator derivative is3Vp h(w). The root boundary displacement contributes integral_F n h/k to N and integral_F h/k to V, while E'=Vh(g) because ell=0 on F. First-order stationarity is

I(h)=6V^2[T h(g)-m h(w)].

For h=1,x,y,z this gives

I1=integral_F G/k=6V^2(T-m),
integral_F G xvector/k=6V^2(Tg-mw).

The G-weighted root centroid is RT=(Tg-mw)/(T-m), in relint F when G>0. Taking h=ell gives Tmu=m ell(w). Since G(g)=-r and qmu=r, taking h=G then yields

I2=integral_F G^2/k=6V^2 m[r-n(w)].

In particular T>m and r>n(w) under the positive-root hypotheses.

Let rho be the actual volume fraction of conv(g,F):

rho=mu Area(F)/(3Vk).

Cauchy--Schwarz gives the earlier lower bound

rho>=rho0:=(T-m)^2/[3Tm(1-n(w)/r)].

Applying the TWO-dimensional affine second-moment lemma to the same positive affine G on F gives I0 I2<(3/2)I1^2, where I0=Area(F)/k. Consequently the new two-sided restriction is

rho0<=rho<(3/2)rho0.

Also rho<=1-p/t because the root pyramid and the two canonical patch pyramids have disjoint interiors. This restriction is not automatically valid at a zero-endpoint wall, where arbitrary root rotations may no longer be admissible.

## 5. The actual three-pyramid second-moment budget

The pyramids conv(g,ABC), conv(g,ABD), conv(g,F) are subsets of the SAME convex body and have disjoint interiors. The first two have volume fractions u/t and v/t; the third has fraction rho. This remains true for supporting TRIANGLE PATCHES contained in larger coordinate facets: different supporting planes give disjoint radial boundary directions.

For a uniform tetrahedron whose affine ell values at its four vertices are e0,e1,e2,e3,

mean ell=(sum ei)/4,
mean ell^2=[(sum ei)^2+sum ei^2]/20.

Set w0=p/t and define

Bp={u[(mu+a+b+c)^2+mu^2+a^2+b^2+c^2]
   +v[(mu+a+b+d)^2+mu^2+a^2+b^2+d^2]}/(20t mu^2).

The two patch pyramids together contribute normalized first moment (T+w0)/4 and normalized raw second moment Bp. Indeed u(a+b+c)+v(a+b+d)=r=tTmu.

In the root pyramid, ell is zero on its base and mu at its apex g. Its normalized first moment is1/4 and second moment1/10, regardless of the polygonal shape of F. Thus its contributions are rho/4 and rho/10.

Let kappa=1-w0-rho be the remaining probability mass. Jensen on this actual remaining subset gives

E_P ell^2/mu^2 >=
Bp+rho/10+[1-(T+w0+rho)/4]^2/(1-w0-rho).

Combining with the three-dimensional affine moment upper bound yields the necessary inequality

FAN(rho):=Bp+rho/10+[1-(T+w0+rho)/4]^2/(1-w0-rho)<=8/5.

For2<T<3, kappa cannot be zero: otherwise the first moments of the three pyramids force T=3. In terms of positive kappa,

FAN(rho)=Bp+(1-w0)/10+(3-T)/8
              +(3-T)^2/(16kappa)-3kappa/80.

Hence d FAN/d rho=(3-T)^2/(16kappa^2)+3/80>0. At the positive-root stationary maximum, FAN(rho0)<=8/5 is therefore necessary without needing to know rho exactly.

This is not an independent optimization of unrelated facet masses: the disjoint subsets and their exact affine values are present in every eligible actual body.

A matrix analogue used in the exact control is also valid. For the two patch tetrahedra, compute their weighted first moment Fp relative to g and weighted second moment Sp relative to g. Since their total probability is w0, the complement has relative first moment -Fp. Jensen gives Sigma>=Sp+Fp Fp^T/(1-w0). The audit calculates these matrices from the literal A,B,C,D,g coordinates.

## 6. A necessary planar root weighted-mass bound

Assume additionally a>b and write alpha0=a-b>0, Bn=a+b+c>0,Dn=a+b+d>0. The root plane is a graph in z and dA/k=dxdy/alpha0. Its projected actual root polygon K is in x,y>=0, with

G=Bn x+Dn y-r>0.

The root identities prescribe its weighted mass and weighted mean of G:

W=integral_K G dxdy=t^2 alpha0(T-m)/6,
H=(integral_K G^2)/(integral_K G)=m[r-n(w)]/(T-m)>0.

For h>0 let Bh be the full band in the quadrant with0<=G<=h. Direct integration along Bn x+Dn y=r+s gives

Wband(h)=(r h^2/2+h^3/3)/(Bn Dn),
Qband(h)=(r h^3/3+h^4/4)/(Bn Dn).

Its weighted mean is h(4r+3h)/(6r+4h), strictly increasing from0 to infinity. There is a unique h>H with this mean equal to H:

h={2(H-r)+sqrt(4r^2+10rH+4H^2)}/3.

On the quadrant, G(1-G/h) is nonnegative precisely on Bh among points with G>=0, and negative for G>h. Therefore ANY measurable K in G>0 satisfies

W-Q/h <= Wband(h)-Qband(h)/h.

Putting Q=HW and Qband=HWband, and using h>H, gives W<=Wband(h). For the actual compact root with min_F G>0, strict inequality holds, since equality would require agreement with the entire band almost everywhere, including points with arbitrarily small positive G. Thus the necessary root condition is

t^2(a-b)(T-m)/6 < (r h^2/2+h^3/3)/[(a+b+c)(a+b+d)].

This is a bound on actual root moments. It does NOT assert that replacing a root by the band preserves body volume, centroid, ell moments, true facets or proper33 status. The freedom of those coupled body data is still the essential issue.

## 7. Exact elimination of the old formal11/5 fiber

Use the EXACT old data from ROOT_DUALITY_JOINT_VARIATIONS_V1, without changing the object:

a=1,b=1/2,c=d=2/5,t=5,T=11/5,u=v=3/4.

Then g=(3/4,3/4,-7/22), r=57/20,mu=57/220,m=9/10,
beta=(17/2,17/2,11/2),
y=(1063/1600,1063/1600,-23961/35200),delta=48323/6400.

The actual stationary covariance fiber must lie above Qstar as constructed in section3. Exact rational calculation gives

alpha^T Qstar alpha=3220124117/58470830000,
alpha^T Qstar alpha-(3/5)mu^2=108137839/7308853750>0.

This excludes EVERY covariance in that fiber, not just one guessed covariance matrix.

Separately rho0=169/462 and Bp=148559/108300. The three-pyramid bound gives

FAN(rho0)=5307608093/3218892600,
FAN(rho0)-8/5=157379933/3218892600>0.

Thus the actual fan second moments independently exclude the same formal datum. It had already been shown not to be a body using the equality4(u+v)=t+1 and its forced apex with ell<0. The new contribution is two transferable moment obstructions not using that special equality classification.

## 8. Exact formal threshold datum and the limitation it proves

The following is FORMAL MOMENT DATA ONLY, with no asserted body realization:

a=1,b=2/3,c=d=1/60,t=9/5,T=51/25,u=v=11/32,rho=1/4.

The defining formulas give

r=1111/960,mu=27775/88128,z=1937/73440,m=55/48,
rho0=1151329/5202000.

Take Sigma=Qstar=Q0+yy^T/delta, with delta>0 defined exactly in section3. This is an exact matrix, not floating input; the full matrix is deterministically generated and printed by the source in capsule part1. The audit proves all the following FINITE checks strictly:

u,v>=1/4; u,v<=t/4;4p<=t+1;4z<=t+2-4p;z>=1-t;
m>=13/15;t<=45/7;mu>=1/4;4mu>=b,c,d;
4tmu-ct-a-b-d>=0 and4tmu-dt-a-b-c>=0;
b-4mu(T-2)>=0;
delta>0 and Sigma beta=h;
rho0<rho<(3/2)rho0 and1-p/t-rho>0;
FAN(rho)<8/5;
Berwald variance bounds for x,y,ell,t-x-y,z-1+t,t-x-y-z;
the matrix two-patch covariance bound from section5;
the root-band bound from section6.

In particular

FAN(1/4)=99145502717513/71366196000000<8/5,
8/5-FAN(1/4)=15040410882487/71366196000000,
(alpha^T Sigma alpha)/mu^2=140853006074403053/278811909948385000<3/5.

For the root-band test no algebraic approximation is needed: the rational cutoff h=1 has Qband(1)/Wband(1)<H and Wband(1)>W. Monotonicity then implies the mass bound at the prescribed larger cutoff.

The audit checks positive leading principal minors for Sigma minus the explicit patch-covariance lower matrix. It does NOT check every conceivable nonnegative affine function on an unknown body. It does NOT prove simultaneous realizability of the root polygon, these moments and the canonical supporting patches. In particular this is not an actual counterexample to T<51/25 and cannot change the minimum bracket.

## 9. Reconstruction and verification

Capsule part1 is the complete literal root_fan_berwald_audit.py source: material [internal-source-reference],6733UTF-8 bytes, SHA2561ea07f5b736d7e65e2c9ce80536fe0e2f32bcf5a280596d24e68ddf2d9e0a8ce. Save its ENTIRE text unchanged to that filename, with its final newline. It contains every rational input and every helper; no originating sandbox or external data file is needed.

Tested runtime: Python3.13.5,SymPy1.14.0. Reconstruction and verification command:

python root_fan_berwald_audit.py --output root_fan_berwald_report.json

Expected terminal markers, in order:
ROOT_FAN_BERWALD_EXACT_AUDIT_PASS
OLD_ENTIRE_COVARIANCE_FIBER_EXCLUDED
NEW_THRESHOLD_FORMAL_DATA_ONLY_NOT_A_BODY

The generated report is5302UTF-8 bytes, SHA256eb9dcc547473a62590333a01dacb73c0486b844f514d866366b7ef5c57da5fb3. It contains the full exact matrices, coordinates of formal RT, rational invariants and positive margins. The coordinator executed this exact source and observed all assertions and markers. This is an exact symbolic arithmetic audit of the stated finite constraints, not a geometric realization audit. Hashes identify bytes and do not substitute for the full source, which is in part1.

### Complete exploratory source and its evidentiary boundary

A symmetric diagnostic search c=d,u=v at fixed T=51/25 found a feasible finite-moment region, from which the simpler rational datum above was chosen and checked exactly. Symmetry is NOT without loss of generality. The following complete source is only a locator, not an exclusion certificate or a body. Tested numerical versions:NumPy2.1.3,SciPy1.16.0. Save the code block unchanged as root_fan_berwald_exploratory_search.py,1579bytes,SHA256bd66e485bf488f3841e725866e1cfca41b9526225e4587bb00f781520b7e41c8. Run python root_fan_berwald_exploratory_search.py. Its terminal prefix is EXPLORATORY_FLOATING_SEARCH_NOT_A_BODY; floating output need not be byte-stable across numerical libraries. All scientific exact claims are instead checked by part1.

```python
from scipy.optimize import differential_evolution, minimize
import numpy as np, math, time
def sym_constraints(x, target=2.04, retdata=False):
    # x=(b,k,t,p); T fixed, g=(p/2,p/2,z).
    b,k,t,p=map(float,x); T=target;s=1+b
    r=(s+k)*p;mu=r/(t*T);q=t*T
    z=(1+(k-1)*p-mu)/(1-b)
    g=np.array([p/2,p/2,z]);m=3*p/t
    alpha=np.array([k-1,k-1,b-1])
    beta=np.array([s+k,s+k,0.])-q*alpha
    Q0=(4*np.eye(3)-np.ones((3,3)))/(80*t)+np.outer(g-.25,g-.25)/(t-1)
    targetv=np.array([4*r*p/2-(s+2*k)*p/2]*2+[4*r*z-r-b*p])/5
    y=targetv-Q0@beta;delta=beta@y
    D=.6*mu*mu-alpha@Q0@alpha
    C0=np.array([
        p-.5,(t+1)/4-p,t/2-p,mu-.25,4*mu-b,4*mu-k,
        4*t*mu-k*t-s-k,b-4*mu*(T-2),
        t+2-4*p-4*z,z-(1-t),
        m-13/15,45/7-t, delta,D,(delta*D-(alpha@y)**2)/(1+abs(delta)),
    ])
    theta=1/(3*p)
    rho0=(T-m)**2/(3*T*m*(1-theta))
    kr=1-m/3-rho0
    Bpatch=(p/t*((mu+1+b+k)**2+mu*mu+1+b*b+k*k))/(20*mu*mu)
    budget=Bpatch+rho0/10+(1-(T+m/3+rho0)/4)**2/max(kr,1e-10)
    cons=np.r_[C0, kr, 1.6-budget]
    if retdata: return cons, dict(T=T,b=b,k=k,t=t,p=p,z=z,mu=mu,m=m,delta=delta,D=D,rho0=rho0,budget=budget,Q0=Q0,beta=beta,y=y)
    return cons
bounds=[(.040001,.999),(.00001,2.5),(1.0001,6.4285),(.500001,1.85)]
def penalty(x):
    c=sym_constraints(x);return np.sum(np.minimum(c,0)**2)
start=time.time()
res=differential_evolution(penalty,bounds,seed=101,maxiter=600,popsize=12,polish=True,tol=1e-10)
res.fun,res.x,time.time()-start,sym_constraints(res.x,retdata=True)
print("EXPLORATORY_FLOATING_SEARCH_NOT_A_BODY", res.fun, res.x.tolist())
```

## 10. Useful failed bridges and next geometric connection

The new moment cuts do not determine the whole actual section geometry. In particular the scalar/fiber-matrix relaxation still passes an unrealized threshold datum. The point RT need not enter P merely because a finite collection of covariance/first-moment inequalities holds. Likewise a measurable root band maximizing weighted mass is not an admissible simultaneous replacement of an entire convex body with its canonical patches.

Lifting vertical fibers to meet ell=0 would preserve volume and some planar numerator moments while lowering ell moments, but generally loses canonical marks A,B,C,D. Reattaching T0 changes the ratio; no global monotonic reduction follows. Similarly a centroid-asymmetry argument for RT membership only gives a much weaker regime such as T>=4m, not the target threshold.

Ordinary facet stationarity does constrain root-only geometry: an ordinary triangle with one canonical vertex X and two noncanonical vertices v,w has GX=-3L,Gv=Gw=L>0. But facets containing three canonical marks can be rigid supports ACD or BCD, and a special facet containing two marks may be a quadrilateral. These are genuine exceptions to a naive claim that every root vertex lies on the ordinary G levels. In the new symmetric formal datum, G-weighted root mean is below the B-ordinary level; this only indicates the need for exceptional/special vertices and is not a contradiction. General all-auxiliary bodies have still more coupled freedom.

The next useful work is a real root/facet/section realizability theorem using these local levels and actual convexity, or a strong coupled higher-moment inequality. Neither independent covariance completion nor separately optimized section profiles can be treated as the missing physical proof.
