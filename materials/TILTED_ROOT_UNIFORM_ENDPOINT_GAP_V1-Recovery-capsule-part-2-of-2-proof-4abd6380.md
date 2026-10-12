# material-4abd6380be39

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# TILTED_ROOT_UNIFORM_ENDPOINT_GAP_V1 — Recovery capsule part 2/2: proof and commands

## Evidence and recovery

Part 1 is the entire literal source material **[internal-source-reference]**, 4984 bytes, SHA-256 **c8bc45599c4d2d565594baaabe9c903fd8349232de5e2d288ca969e2333fac1e**. Save its text without alteration as tilt_gap_exact.py (UTF-8, LF, final LF).

Reconstruction: `python -S tilt_gap_exact.py > tilt_gap_exact.json`.
Output: tilt_gap_exact.json, 919 bytes, SHA-256 **ac0182ce0de4b725556f3d2b4ea9e7678a6907cdf4407988f965096a8b4a8f54**.
Terminal marker inside JSON: **COMPACT_EQUAL_CAP_65_32_AND_TILT_GAPS_EXACT_PASS**.
Verification:
```text
python -S -c "from pathlib import Path; import hashlib,json; pins={'tilt_gap_exact.py':(4984,'c8bc45599c4d2d565594baaabe9c903fd8349232de5e2d288ca969e2333fac1e'),'tilt_gap_exact.json':(919,'ac0182ce0de4b725556f3d2b4ea9e7678a6907cdf4407988f965096a8b4a8f54')}; assert all((len(Path(n).read_bytes()),hashlib.sha256(Path(n).read_bytes()).hexdigest())==p for n,p in pins.items()); assert json.loads(Path('tilt_gap_exact.json').read_text())['terminal']=='COMPACT_EQUAL_CAP_65_32_AND_TILT_GAPS_EXACT_PASS'; print('TILT_GAP_RECOVERY_PASS')"
```
The source was recovered and executed again in the present coordinator turn; both byte counts and hashes matched. The reference environment is CPython 3.13.5, standard library, assertions enabled. There are no random inputs, optimizers, external files, or unspecified parameters. This is a replay of the new rational algebra, not of the entire earlier lower-bound certificates or a proof-assistant formalization of localization.

The proof was recovered from archived coordinator output **[internal-source-reference]**, SHA-256 b087eec9cd244ea123afe4ea540396edd94057879476069818e7985f28ebfcc7, read completely. Its administrative statements about read-only tools and idle workers are stale and are NOT adopted. Only the mathematical content below is accepted, relative to its two mathematical parents.

Both parents were read anew from cursor 0 through eof:true, preserving the first SHA-256:
- **Calm Harbor 51**, minimum-0082, SHA f1793b348240dce32e3de0ca3e06e50e64942c2561980cb2dc1c75bb9b6b636c: ANISOTROPIC_EQUAL_ENDPOINT_TRACE_V1. Supplies the equal-endpoint theorem A, sign-guarded mixed planar test, genuine single-facet cap 10/9, and two-pyramid compactification t<45/7 at high trace.
- **Keen Raven 13**, minimum-0083, SHA 3e86de882ea208c90af36b6583bb49754e528559555e8db9ce7efe04cd37020d: TILTED_ROOT_GRAPH_AND_IMBALANCE_V1. Supplies the same-body tilt transfer, actual volume visibility and own-centroid strip.

A successor using this theorem must include BOTH exact assignment IDs in parent_assignment_ids and BOTH capsule parts in material_ids. The literal immutable parent payloads remain authoritative. Raven's intermediate statement that the unrestricted equal-endpoint case was open is superseded by Harbor, not used here.

## Theorem and exact domain

Let P be a finite full-dimensional convex 3-polytope of constant volume density. Let ABC and ABD be genuine maximal triangular facets sharing the genuine edge AB. In affine coordinates put
```text
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0).
```
Thus P lies in x>=0,y>=0 and contains T0=ABCD. For any nonzero affine ell>=0 on P put
```text
a=ell(A), b=ell(B), c=ell(C), d=ell(D), M=max(a,b,c,d)>0,
V=Vol(P), t=6V>=1, g_P=(x,y,zeta), s=x+y, mu=ell(g_P)>0,
T=[(a+b+c)x+(a+b+d)y]/(t*mu).
```
All moments refer to the SAME actual P and its own volume centroid. When ell=0 is a genuine root facet, T is the sum of the corresponding two entries in one physical Lambda. An auxiliary nonnegative ell is not declared a new facet.

Then
```text
T>=51/25  implies  227326*|a-b|>49*M.
```
In particular |a-b|>M/4640. Under the additional condition max(a,b)=M,
```text
T>=51/25  implies  6963*|a-b|>7*M,
```
hence |a-b|>M/995. There is no restriction on c-d, facet count, projection, symmetry or mechanical metric. Constants are not claimed optimal. Negations with <= describe excluded CLOSED strips.

No polyhedron is constructed. This theorem does not exclude all E=17, does not change a FULL/LOCAL counter, and does not raise the accepted global lower bound C>=34. External novelty and peer review are not established.

## 1. Compact equal-endpoint lemma

We prove a=b and 1<=t<=45/7 imply T<sigma=65/32.

If a=b=0, Harbor gives T<=1. Otherwise divide ell by a and write ell=1-p*x-q*y with p,q<=1. If both coefficients are nonnegative, Harbor theorem A gives T<=2. If both are nonpositive, T<=3/2. After interchanging x,y the only remaining case is 0<=p<=1,q<0.

Set kappa=10/9. If beta_sigma=3-p+sigma*t*q>=0, then alpha_sigma=3-q+sigma*t*p>0. Harbor's mixed-sign planar test B(t,p,q)<2 on [1,45/7], with these coefficient signs, yields T<sigma. The sign guard is essential; no unconditional T<=B is asserted when q<0.

If beta_sigma<0, use Harbor's bound from the genuine single-facet cap and the actual centroid inequality s<=(t+1)/4:
```text
T<=U(t,p,q)
 =kappa+(3-p)*[(t+1)(3-q+kappa*t*p)-4*kappa*t]
             /[t(3-q)(4-q(t+1))].
```
Put A0=3-p in [2,3], rho=-q>A0/(sigma*t), lambda=sigma-kappa=265/288. All denominators are positive. U<sigma is equivalent to Phi>0, where
```text
Phi=lambda*t*(3+rho)*(4+rho*(t+1))
    -A0*[(t+1)(3+rho+kappa*t*(3-A0))-4*kappa*t].
```
The coefficient of rho^2 is positive. The linear coefficient is at least
```text
461/144+(2581/288)*(t-1)+(265/96)*(t-1)^2>0.
```
Therefore it suffices to test rho=A0/(sigma*t). With v=A0-2 in [0,1], the exact identity is
```text
73728*sigma^2*t*Phi(t,A0,A0/(sigma*t))=P0(t)+v*P1(t)+v^2*P2(t),
P0=-676000*t^3+4388475*t^2-223680*t-327680,
P1=338000*t^3+1190800*t^2-275680*t-327680,
P2=80*(t+1)*(65*t-32)*(65*t+32).
```
P2>0 for t>=1. For w=t-1>=0,
```text
P1(1+w)=925440+3119920*w+2204800*w^2+338000*w^3>0.
(P0/t^2)''=-1920*(233*t+1024)/t^4<0,
P0(1)=3161115,
P0(45/7)=524485/343>0.
```
A concave function lies above its endpoint chord, so P0/t^2, and hence P0, is positive throughout the closed interval. Thus Phi>0 and the lemma follows on the entire continuous domain, not a parameter grid.

## 2. Same-body transfer exploiting the high trace

Suppose T>=tau=51/25. Harbor's genuine two-centroid-pyramid tail gives t<45/7: at u=11/8, total cone mass m=13/15 and T=tau, the forbidden excess is exactly 29035697/279130931200>0. The tail is applied to the actual T, never to an arbitrary planar relaxation.

Normalize M=1. Reflect z -> 1-x-y-z if necessary so a>=b; this exchanges A,B and fixes C,D. Put alpha=a-b>=0 and r=t-1. Volume visibility of conv(T0,p), for every p in P, gives
```text
1+(-z_p)_+ +(x_p+y_p+z_p-1)_+<=t,
```
so z_p+r>=0. On the UNCHANGED body define
```text
ell_equal=ell+alpha*(z+r)>=0.
```
Its nodes are (a+alpha*r,a+alpha*r,c+alpha*r,d+alpha*r); c-d is preserved. Exactly,
```text
mu_equal-mu=alpha*(zeta+r),
T_equal*mu_equal-T*mu=alpha*(3-2/t)*s.
```
The compact lemma applies to this auxiliary function even if its zero set is not a facet. Hence
```text
T<sigma+alpha*[sigma*(zeta+r)-(3-2/t)*s]/mu.       (1)
```
The genuine vertex fan from a node with ell=1 gives mu>=1/4: each positive tetrahedron in that fan has ell-mean at least 1/4. The genuine own-centroid strip from Raven is
```text
zeta<=1/2-s+t/4.
```
To recall its geometry, cut at z=0. The lower part, if nonempty, has base area >=1/2 and volume W<=V-1/6. Concavity of the square root of its section area, compared with the linear pyramid profile of equal volume, gives -int_lower z<=3*W^2/2. The positive part contains T0 with int_T0 z=1/24. Dividing by V yields zeta>=1/2-t/4. Reflecting A,B yields the displayed upper strip. If the lower part is empty, the bound follows directly. These are actual moments, not a free centroid vector.

Since all four nodes are <=1, high trace itself gives
```text
3*s >= (a+b+c)x+(a+b+d)y = t*mu*T >= tau*t*mu,
s/mu>=tau*t/3.                                       (2)
```
The numerator of the correction in (1) is at most
```text
sigma*(5*t/4-1/2)-(sigma+3-2/t)*s.
```
The first coefficient and sigma+3-2/t are positive for t>=1. Use 1/mu<=4 and (2), with signs retained:
```text
[ sigma*(zeta+r)-(3-2/t)*s ]/mu
 <=C_tau(t,sigma)
 :=sigma*(5*t-2)-(sigma+3-2/t)*tau*t/3
 =(2694*t-1081)/400.
```
This is increasing, so it is at most C_tau(45/7,65/32)=113663/2800. Therefore
```text
tau<=T<sigma+alpha*(113663/2800),
alpha>(tau-sigma)/(113663/2800)=49/227326.
```
Restoring M proves the first claim.

If max(a,b)=M, then after reflection a=1. The equal endpoint values of ell_equal dominate its C,D values, so Harbor theorem A gives T_equal<=2. The same transfer with k=2 gives
```text
C_tau(t,2)=(165*t-66)/25,
C_tau(45/7,2)=6963/175.
```
For alpha=0 high T is impossible. For alpha>0, strict t<45/7 and monotonicity imply T<2+alpha*(6963/175), hence alpha>7/6963. This does not incorrectly make the exceptional tetrahedral T_equal=2 case strict.

## 3. Application boundary and negative method control

In FULL253 this theorem applies only when the selected facets really are adjacent maximal TRIANGLES and the actual root row requires T>=51/25. It does not automatically apply to nontriangular facets, a whole tree or all (10,17,9). Splitting by sign(a-b) and the maximum-node index gives a linear necessary inequality in the actual root values. Any substitution must retain the same real vertices, root covector and own COM; polynomial degree must be recalculated in its concrete coordinate model.

A stronger sufficient test fails: at t=45/7,p=1,q=-4/25,
```text
beta_2=-2/35<0,
U=108740/53799>2.
```
This is a scalar-envelope failure, NOT an actual polytope and NOT a counterexample to a physical T<=2 theorem. No claim of C>=36 or exact minimum follows.
