# material-ee4f389e0d5b

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Complete physical VE wall atlas and sharp fixed-foot condition

## Identity, evidence and scope
COMPLETE_PHYSICAL_VE_WALL_ATLAS_AND_SHARP_FIXED_FOOT_CONDITION_V1. This is a coordinator analytical result, not a numerical C592 result and not a new attaining construction. It extends STABLE_FACET_FIXED_TWO_PARAMETER_UH_WALL_AND_RANK_ONE_CANCELLATION_V1, immutable material [internal-source-reference], SHA256 5ebab73947b01b989cef70552ea91bd2b446f88eb695cf78e780636a9f62e5a8. The motivating exact object is the new C592=(164,296,134),own121physicalweak000 of the completely read result minimum-0289, SHA256 34d98fdf4c645c0d704314609e30ba0213e34d9c7a1ec981a360eadaab1e6217. No evaluation of the new atlas on that object is claimed.

All geometry below is at the actual uniform volume centroid of a fixed full-dimensional convex polytope P. Thus zero is strictly interior. A physical metric M is positive definite, and N is always its actual inverse. An invertible linear image of the uniformly filled body realizes each such metric without changing the centroid from zero. True maximal facets and true edges are used. There is no polar recentering, surrogate moment system or independently fitted inverse.

The first theorem describes EVERY physical vertex-edge collision at a designated directed true edge, modulo positive scale. It does not assume that either adjacent facet is the body's stable facet. Requiring one of them to be stable is an explicit additional geometric condition, not an implicit restriction. The last theorem sharpens the earlier rank-one result: its optimum is the optimum of the COMPLETE fixed-stable-foot metric class, not just of the rank-one subclass.

## 1. A fixed geometric frame for a directed true edge
Let [u,v] be a true edge and e=v-u. Let q.x=1 and r.x=1 be its two normalized incident support planes. Choose any vector d with q.d=0 and r.d=1. It exists because q,r are independent. Then

T=[u,e,d]

is invertible: q.u=1, q.e=q.d=0, r.e=0, r.d=1. Coordinates in this frame are used only within this note. They do not rename the polytope's vertex or facet labels. In the frame,

u=(1,0,0), e=(0,1,0), v=(1,1,0),
q=(1,0,0), r=(1,0,1),

where poles are covectors. A different allowed choice of d is a coordinate change, not a different physical polytope.

A physical VE collision at u along [u,v], interior to the actual edge-normal cone, means

u^T M e=0,
M u is a positive linear combination of q and r.

Normalize u^T M u=1 by positive metric scale. Since q.u=r.u=1, there is a unique tau in (0,1) with

M u=(1-tau)q+tau r.

This normalization preserves every primitive sign and every equilibrium.

## 2. Complete four-parameter atlas with an explicit inverse
In the T frame every such metric, and no other one, is

G(tau,A,L,eta)=
[[1,0,tau],
 [0,A,A eta],
 [tau,A eta,tau^2+A eta^2+L]],

where

0<tau<1, A>0, L>0, eta is any real number.

The physical matrices are M=T^{-T}G T^{-1} and N=T G^{-1}T^T. The exact inverse in the frame is

G^{-1}=
[[1+tau^2/L, tau eta/L, -tau/L],
 [tau eta/L, 1/A+eta^2/L, -eta/L],
 [-tau/L, -eta/L, 1/L]].

Proof. The prescribed first column is (1,0,tau). The Schur complement of its leading1 is an arbitrary positive two-by-two matrix. Write that matrix uniquely as [[A,A eta],[A eta,A eta^2+L]], with A>0 and L>0. Conversely

x^T G x=(x0+tau x2)^2+A(x1+eta x2)^2+L x2^2,

which is positive definite on the stated domain. Multiplication gives the displayed inverse. This proves completeness and positivity without any condition-number truncation.

The reverse primal arrow is v^T M(u-v)=-A<0. For every other true arrow u->j,

u^T M(x_j-u)=((1-tau)q+tau r).(x_j-u)<0,

because an interior normal of a true edge exposes exactly that edge. The two incident dual primitives are

q^T N(r-q)=-tau/L<0,
r^T N(q-r)=-(1-tau)/L<0.

Thus throughout the atlas the designated packet is exactly [0,-,-,-]. This is a genuine isolated-carrier VE contact, not a VF contact, a flat edge, or an algebraically harmless zero. Other physical contacts elsewhere still have to be counted.

## 3. Allowing the stable foot to move, or allowing another stable facet
The foot of q in these coordinates is

p=(1, tau eta/(L+tau^2), -tau/(L+tau^2)).

It is independent of A. Put h=-p2=tau/(L+tau^2)>0 and z=p1. Then h tau<1 and z=h eta. Conversely a point p=(1,z,-h) with h>0 and a tau satisfying 0<tau<min(1,1/h) gives

eta=z/h, L=tau/h-tau^2>0.

Hence the atlas includes every foot in the q-plane on the inward side of r that is compatible with the chosen edge-normal coefficient. It is not confined to the original foot or to a bounded neighborhood.

The facet q is strictly stable exactly when p lies in the relative interior of its actual maximal polygon. For any other normalized support pole s=(s0,s1,s2), the corresponding strict inequality is

(s0-1)(L+tau^2)+tau(eta s1-s2)<0.

It suffices to impose this on the true facet neighbors of q. The r inequality is automatically -tau<0. Requiring all actual supports instead gives the same polygon and is also valid. The condition is independent of A and has total degree at most2 in tau,eta,L.

For a prescribed stable foot p=(1,z,-h), define w=u-p and F=[p,e,w]. The complete normalized wall then takes the equivalent form

F^T M F=diag(1-tau h, A, tau h),

with A>0, 0<tau<1 and tau h<1. Thus moving p supplies the two dimensions absent from the earlier fixed-foot wall. The complete four-parameter atlas can also be searched without imposing q stability, allowing the unique stable facet to have another label.

## 4. All genuine primitive signs have low-degree formulas
Let x_i=T^{-1}X_i and delta=x_j-x_i for an actual true primal arrow i->j. Define

VE_ij=(x_i0+tau x_i2)(delta0+tau delta2)
      +A(x_i1+eta x_i2)(delta1+eta delta2)
      +L x_i2 delta2.

For any actual dual arrow a->b, let pi=T^T a and epsilon=T^T(b-a), and put

kappa(pi)=tau pi0+eta pi1-pi2.

Then

EF_ab=pi0 epsilon0+pi1 epsilon1/A+kappa(pi)kappa(epsilon)/L.

Multiplying by the strictly positive A L preserves its sign:

A L EF_ab=pi0 epsilon0 A L+pi1 epsilon1 L+kappa(pi)kappa(epsilon) A.

Both displayed sign polynomials have total degree at most3 in tau,eta,A,L. They encode one exact common inverse; there is no reciprocal relaxation. The target primal polynomial vanishes identically, and any other identically-zero primitive must be kept in the physical packet census.

For fixed tau and eta, every primal zero is a line in (A,L), and every dual zero has the form alpha A L+beta L+gamma A=0. Thus the line/bilinear arrangement of the previous two-amplitude atlas now sits inside a COMPLETE atlas of the physical VE wall. The additional two variables are geometrically meaningful normal direction and shear, rather than unspecified metric coefficients.

For fixed tau,eta,L, every primitive sign is a linear polynomial in A after multiplication by A where necessary. Therefore the set of A>0 for which a fixed vertex is strictly unstable is an open interval, empty, or the whole positive ray. The same is true for a fixed strictly stable facet and for a fixed strict saddle edge: each property is the conjunction of finitely many strict affine inequalities in A. Zero constant rows make the corresponding strict feature impossible and must not be discarded.

Consequently a complete one-dimensional census at fixed outer variables needs only the positive endpoints of these intervals (or, equivalently, all positive primitive roots). Sort them, sample the open intervals, and test the complete physical packets at endpoints. This avoids an enumeration of rooted trees when the objective is a census of this particular wall family. It is an algorithmic reduction, not an executed C592 classification. Negative signs at a few chosen rows do not replace the complete census.

## 5. A clean wall gives a proper110 endpoint at the same complexity
At a wall metric replace G by G+epsilon(E01+E10). For sufficiently small epsilon the matrix remains positive definite. The designated source primal is epsilon and the reverse is -A-epsilon. Its two dual primitives remain strictly negative by continuity; every other outgoing edge at u remains strictly negative by the exposed-edge margin. Thus epsilon<0 creates the local strict U/H pair, while epsilon>0 removes both.

Suppose a wall point in the atlas has strict counts (S,U,H)=(1,1,0), and the target VE packet is its only physical weak equilibrium. Then sufficiently small positive epsilon gives proper110physicalweak000 with exactly the same true V,E,F. Every other strict equilibrium and every strict positive exclusion persists. Harmless unchosen primitive zeros are allowed if their feature packets have a strict positive exclusion; a zero is not automatically another rest.

A rational polytope with rational atlas parameters at such a clean point permits a sufficiently small positive rational epsilon and a rational SPD matrix. Its positive square root gives an exact algebraic Euclidean realization of a uniformly filled body. A rational three-by-three Gram factor is NOT asserted for every rational SPD matrix.

This is a sufficient constructive criterion. No assertion is made that every proper110 metric cell of every fixed polytope has a boundary with only one physical weak packet. Persistent simultaneous walls or other stable labels must not be silently removed. The atlas itself covers each designated physical VE collision even in the presence of other contacts; the clean-wall implication requires the stated full census.

## 6. Sharp condition number with a prescribed stable foot
Now assume the initial M0 is SPD, u is strictly unstable, [u,v] is a strict saddle edge, and q is a strict stable facet. Let N0=M0^{-1}, Q=q^T N0q, p=N0q/Q, w=u-p and

l=e^T M0 e>0,
d=w^T M0 e=u^T M0 e<0,
w2=w^T M0w>0,
rho=-d/sqrt(l w2), with 0<rho<1.

Consider ALL SPD wall metrics preserving precisely p as the foot of q, modulo positive scale. Their minimum possible relative condition number, measured as the eigenvalue ratio of M0^{-1/2} M M0^{-1/2}, is

K_fixed=(1+rho)/(1-rho).

This optimum is achieved inside the genuine edge-normal cone, not merely on the algebraic equation u^T M e=0.

Lower bound. Set a=w/sqrt(w2), b=e/sqrt(l). Their M0 squared norms are1 and their M0 inner product is -rho. Since a wall metric preserving p has w^T M e=0, one has

(a+b)^T M(a+b)=(a-b)^T M(a-b).

If m and Mmax are its extreme relative eigenvalues, then

2m(1+rho) <= (a-b)^T M(a-b)
           = (a+b)^T M(a+b) <= 2Mmax(1-rho).

Thus Mmax/m >= K_fixed. This proof does not assume a rank-one path.

Attainment. Normalize the metric scale so that M p=M0 p=q/Q. In the frame F=[p,e,w], the initial and optimal matrices are

F^T M0 F=[[1/Q,0,0],[0,l,d],[0,d,w2]],
F^T Mstar F=diag(1/Q,l(1-rho),w2(1-rho)).

The three relative eigenvalues are 1,1,(1-rho)/(1+rho), so the lower bound is attained. It is exactly the positive rank-one inverse construction from the earlier material at

lambda=sqrt(w2/l),
z=w-lambda e,
T=-d/(lambda(l w2-d^2)),
Nstar=N0+T z z^T, Mstar=Nstar^{-1}.

Because q.z=0 the stable foot is fixed. The q->r primitive stays constant and negative; the r->q primitive decreases by T(r.z)^2 and stays negative. Therefore the optimal wall is a genuine VE contact and is reached with the local target pair intact before collision. Other equilibria can still be born elsewhere.

More generally the scale-normalized tangent matrices diag(k l,k w2), with 1-rho<=k<=1+rho, have the same optimal relative condition number whenever they satisfy the true edge-normal-cone inequality. The endpoint k=1-rho always does under the stated initial saddle hypotheses. No claim is made that these metrics have globally minimal equilibrium count.

Since u^T M0u=1/Q+w2>w2, the unrestricted angle parameter |u^T M0e|/sqrt((u^T M0u)(e^T M0e)) is strictly smaller than rho. Thus fixing the stable foot has a strictly greater minimum conditioning cost than the unrestricted sharp targeted collision of the C592 parent's rank-two pencil. The latter's no110 classification and the new fixed-foot optimum concern different metric classes.

## 7. Interpretation and next concrete questions
The new results are exact analytical parameterizations and an attained optimization theorem. They do not improve the canonical attaining C622, do not exclude any entire E17 incidence, and do not change 34<=C_min<=622.

For the new C592 one can now distinguish: the already closed positive rank-two pencil; the complete original-fixed-foot two-parameter wall; the full four-parameter physical VE wall retaining stable facet3 but moving its foot; and the still larger census on that same complete wall allowing a different stable label. All are actual fixed-body metric questions. Shape changes remain independent degrees of freedom and must use the true moving uniform centroid. No unsuccessful finite search on one of these domains proves exclusion of another.
