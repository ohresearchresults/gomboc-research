# minimum-0153

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# ONE_ZERO_FULL_TWO_NORMAL_NF_TRACE_203_V1

## 1. Main result

**The entire two-normal NF is below the requested threshold, without an aspect or sigma restriction:**

    T(P) < 203/100 < 51/25.

This includes every finite continuous concave upper profile U, both root-section regimes, the regime switch, m=0, and the closed lower-cut boundary m=q. The proof actually drops the parent's weighted maximizing-D condition. It retains p<=q, max ell=ell(A)=1, and the actual marked tetrahedron; those are genuine geometric hypotheses, not normalizations of an arbitrary one-zero body.

Consequently the parent's entire CH class, with arbitrary compatible lower section geometry and every aspect, also has T<203/100 by its accepted trace-dominating reduction. The parent proves an actual-body reduction, not an independently fitted section law. Its last operation changes V,E and root area, and the present theorem evaluates the resulting body's own moments. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

There is no extension here to all proper one-zero bodies, to the full thirteen-vertex localization, or to max ell>ell(A). No E17 incidence count, minimum-complexity bound, or attaining construction changes.

Two useful failed strengthenings are preserved as exact actual bodies. A genuine high-root NF has T>2. Also, deleting an early upper-profile corner while fixing b,d,U(d),m lowers trace even when BOTH original and replacement traces exceed 2. Thus neither “the high branch has T<=2” nor unconditional pointwise chord deletion is valid.

## 2. Source authority and completed reading

The new journal was read completely through EOF, including its entire literal parent. Unchanged earlier evidence was retained; the previously supplied source, exact report and receipt were accessible. No research connector or inaccessible archive was used.

New journal: 298090 bytes, SHA-256

    ef543b30a6424770a9e18170f8020136d00b96defc81ab1aa1acfa071f2b33ee.

Required parent: minimum-0150. Extracting its Markdown from its title through EOF, retaining one final LF, and serializing the version-2 envelope with ensure_ascii=False and separators=(',',':') produces **41391 bytes** and exactly

    5e8296567dc16cfab235ec6069f21d3ce50e228fd6f176791acae439b2ff8f43.

The notebook's 44586B label is therefore a byte-count metadata discrepancy for that authenticated compact envelope, not a theorem or incidence conflict. The conflicting label is present in both common and branch summaries. :contentReference[oaicite:2]{index=2}

The new NF estimate is self-contained and does not use Cstar or the unavailable older optimizer certificate. Only the corollary back to CH uses the supplied parent's accepted geometric reductions. The new finite certificate and all three physical controls were executed normally and then from the sole source file in a clean directory, with byte-identical reports and receipts.

## 3. Exact enlarged NF and physical marks

Let

    0<b<1, 0<=d<=1, alpha=1-b, h=1+b, q=h+d,
    U:[0,1]->[0,infinity) continuous and concave,
    U(0)=1, u=U(d)>0, p=h/u<=q, 0<=m<=q.

Define one convex body in level coordinates by

    K = {0<=w<=1, xi,eta>=0,
         xi+eta<=U(w),
         p xi+q eta+(m/b)w>=m}.

Its original physical coordinates are

    x=xi/u, y=eta,
    z=[1+(d-1)x-y-w]/alpha.

This is an invertible affine transformation, with volume multiplier 1/(alpha u). The physical affine functions are

    ell=w=1+(d-1)x-y-alpha z,
    n=h x+q y=p xi+q eta.

All integrals below use uniform volume on this actual body:

    V=int_P 1, X=int_P x, Y=int_P y, Z=int_P z,
    E=int_P ell, N=int_P n, T=N/(6VE).

Concavity gives U(w)>=1-w. The points A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0) belong to P. For D the only nontrivial lower-cut check is d<b, where

    m(1-d/b) <= q(1-d/b)
                 = h-d(1+d)/b < h=n(D).

For d>=b the cut is zero. At d=0, u=1 and p=q=h, so D also survives, including m=q. A and B lie on the retained axis interval; C satisfies n(C)=q>=m. Thus the canonical tetrahedron is retained and V,E are positive. These checks do not require a root perturbation, an interior-root assumption, or a maximizing-D derivative condition.

For m<q the root section is two-dimensional. For m=q it can collapse to a point or segment; the closed-body estimate still applies directly. The coordinate maximal faces need not equal ABC and ABD. The theorem is about the stated marked trace, not a false identification of those marked triangles with entire maximal facets.

The parent's NF additionally imposes

    (h+w)U(w)<=q U(d).

That restriction is **not used** in this proof. The new rational controls nevertheless satisfy it exactly.

## 4. Coupled actual-section accounting, including the high branch

Put t(w)=m(1-w/b)_+, and write

    A=int_0^1 area(K_w) dw,
    B_w=int_0^1 w area(K_w) dw,
    J=int_0^1 int_(K_w) n dxi deta dw,
    D2=3 int_0^1 U^2, C3=4 int_0^1 U^3.

Then

    V=A/(alpha u), E=B_w/(alpha u), N=J/(alpha u),
    T=alpha u J/(6 A B_w).

Since t(w)<=q(1-w/b)_+<=q(1-w)<=qU(w), the lower cut never passes beyond the upper y-intercept. When p<q, set e(w)=(t-pU)_+. The triangle

    {xi,eta>=0, p xi+q eta<=t, xi+eta>U}

is the part of the full n-cut triangle lying OUTSIDE the actual upper triangle. Its area and n-moment are exactly

    o(w)=e(w)^2/[2p(q-p)],
    j_over(w)=o(w)[pU(w)+2t(w)]/3.

These are zero in the low regime. The formula is ordinary triangular geometry, not a new section chosen independently at each height. In particular 0<=j_over<=m o. Let O=int o and O_w=int w o. Exact subtraction and restoration give

    A=(D2-b rho2)/6+O,
    B_w=(12 int wU^2-b^2 rho2)/24+O_w,
    J=[(p+q)C3-2b m rho2]/24+int j_over,
    rho2=m^2/(pq).

The SAME actual O enters volume and the mixed moment. This is the coupling that is lost by treating section area and centroid as independent variables.

For m<=p, U>=1-w makes e identically zero. For m>p, again using the same U>=1-w,

    e(w)<=p[(a_c-1)-(a_c/b-1)w]_+,
    a_c=m/p.

Therefore, for sigma=q/p>=1,

    0<=6O<=Zstar=b(a_c-1)^3/[(sigma-1)(a_c-b)].       (4.1)

For p=q, m<=p and O=0; no division by q-p is used. The high/low seam is included by the same positive-part formulas.

## 5. The only upper-profile inequalities needed

Three elementary consequences of concavity are enough:

    C3<=D2^(3/2),
    12 int_0^1 w U(w)^2 dw >= D2,
    D2>=D0:=u^2+d(1+u).                             (5.1)

Here is a self-contained justification of the first, rather than an unverified localization substitution. The decreasing rearrangement f of U is concave: its superlevel lengths are concave in the level, because the original superlevel sets are intervals and their Minkowski interpolation lies in the intermediate superlevel set. Taking the decreasing inverse preserves concavity. A tent below U from a maximum M to the two endpoints gives int U^2>=M^2/3. Thus, with c=sqrt(D2), f(0)<=c. Compare f with g(s)=c(1-s). Their squared integrals agree. The concave difference f-g changes sign at most once, from negative to positive. The ratio

    (f^3-g^3)/(f^2-g^2)=(f^2+fg+g^2)/(f+g)

is nonincreasing in s, since f and g are nonincreasing and the displayed function is increasing in each nonnegative argument. The one-sign-change comparison gives int f^3<=int g^3=c^3/4. Zero endpoint values and constant pieces follow by continuity.

For the second inequality, U(w)/(1-w) is nondecreasing by concavity and U(1)>=0. Apply the elementary covariance inequality for two increasing functions, w and U(w)^2/(1-w)^2, under density 3(1-w)^2. That density has mean 1/4. Integrability holds even when U(1)>0. This proves the stated inequality without a monotonicity assumption on U itself.

For the third, integrate the two actual chords through (0,1),(d,u),(1,0), which lie below U. The formula is also valid at d=0 or d=1 with the corresponding endpoint interpretation.

There is a useful exact denominator identity. Set sigma=1+z and q=h+d. Then

    q^2(D0-sigma)
      =h^2 z^2+[h^2(1-d)+2bh d+bd^2]z
        +d(2h+d)(b+d) >=0.                         (5.2)

Thus D2>=D0>=sigma. Since a_c<=sigma and b<1, all denominator factors used below are strictly positive.

## 6. From the same body's moments to a finite inequality

Combining Sections 4 and 5, and writing Z_o=6O and H=1-b^2, gives the actual-body upper bound

    T <= F(D2,Z_o),
    F(D,Z)=H[(1+sigma)D^(3/2)-2b a_c^3/sigma+4a_c Z]
           /[(D-b a_c^2/sigma+Z)(D-b^2 a_c^2/sigma)].            (6.1)

We do not assert that arbitrary scalar values in this larger domain are realizable. Proving the following inequalities on that larger domain is sufficient for every actual NF body.

### 6.1. Entire sigma>=2 sector

Discard the removed numerator moment and use rho2<=sigma. Then

    T <= H(1+sigma)D2^(3/2)
           /[(D2-b sigma)(D2-b^2 sigma)].

This right side is strictly decreasing in D2: its logarithmic derivative is

    3/(2D2)-1/(D2-b sigma)-1/(D2-b^2 sigma)<0.

Set tau=2/sigma in [0,1], and define

    R=4h^2+2dhq tau+dq^2 tau^2,
    A1=R-2bq^2 tau, A2=R-2b^2q^2 tau.

After substituting D0, the bound is H q(2+tau)R^(3/2)/(A1 A2). Exact tensor-product Bernstein expansion on the ENTIRE closed cube (b,d,tau) in [0,1]^3 proves

    41209 A1^2 A2^2-10000 H^2 q^2(2+tau)^2 R^3 >0.

All 1755 coefficients, at degrees (14,12,8), are strictly positive; their minimum is 309504. The 48 and 60 coefficients certifying A1,A2 have minimum 4. Thus T<203/100 throughout this unbounded-aspect sector, including its tau=0 algebraic boundary as a limit.

### 6.2. Entire 1<=sigma<=2 sector

For fixed b,d,sigma,a_c,D, (6.1) is a ratio of affine functions of Z with a positive denominator. Its maximum on [0,Zstar] is attained at an endpoint. Thus it suffices to bound two cases: Z=0 for every 0<=a_c<=sigma, and Z=Zstar in the high branch.

For the high branch write sigma=S=1+z and a_c=1+r z, with z,r in [0,1]. Then

    L=1-b+r z, Zstar=b r^3 z^2/L.

Moreover

    Zstar/(b a_c^2/S)
      =S(a_c-1)^3/[a_c^2(S-1)(a_c-b)]
      <=(S-1)/S<=1/2,

with zero cases treated directly. Consequently the non-cubic term in the numerator of (6.1) is nonpositive. This makes the squaring below sign-safe.

Here are the exact polynomial inputs; the capsule generates every coefficient, with no table dependency. Put

    R0=h^2 S^2+dq^2+dhSq, v=q^2D-R0>=0, R=R0+v.

Use either

    BASE: a_c=S r, L=1, Znum=0,
    HIGH: a_c=1+r z, L=1-b+r z, Znum=b r^3 z^2.

For each case form

    E1=RS L-b a_c^2 q^2 L+Znum q^2 S,
    E2=RS-b^2 a_c^2 q^2,
    C=-2b a_c^3 L+4a_c Znum S,
    Q=203E1E2-100Hq^4 S C,
    P=Q^2-10000H^2q^2 S^4 L^2(1+S)^2 R^3.          (6.2)

Because E1,E2 are positive and C<=0, P>0 implies F<203/100, not the opposite branch of a squared inequality.

The exact proof of P>0 is as follows. P has degree four in the NONNEGATIVE variable v. Every positive-v coefficient is nonnegative on [0,1]^4 by a global Bernstein expansion. For BASE, its constant coefficient has a complete 43-node binary subdivision, 22 closed leaves, maximum depth 10. No cell is discarded as infeasible. Every leaf coefficient is nonnegative; every corner zero lies on b=1. Therefore it is strictly positive at every actual b<1. The source independently reconstructs each leaf in the power basis by direct affine substitution and compares it to inverse Bernstein conversion.

For HIGH, expand the v-constant coefficient in d. All twelve positive-d coefficients have globally nonnegative Bernstein expansions on (b,z,r) in [0,1]^3. At d=0 put

    e1=S^3 L-b a_c^2 L+Znum S, e2=S^3-b^2 a_c^2,
    mid=203e1e2-100HSC, rad=100HS^5 L(1+S).

The exact identity is

    P|_(v=d=0)=h^8(mid-rad)(mid+rad).

The plus factor is positive by the same sign guards. For the minus factor use two closed charts covering the entire (1-b,z) square:

    z<=1-b: b=1-e, z=e t;
    1-b<=z: b=1-e t, z=e.

Both expansions have an exact factor e^3. After cancellation, the first chart has degrees (6,7,5); splitting t at 1/2 gives two strictly positive Bernstein arrays, with minima 3 and 75/4. The second has degrees (6,4,5), 203 positive and seven zero coefficients. All seven zeros have both t-index and r-index zero. At any actual b<1 this chart has e>0 and t>0, so the polynomial is strictly positive there too.

This proves P>0 for both endpoint cases at every b<1, D>=D0 and every aspect 1<=sigma<=2. Together with Section 6.1 and the actual endpoint comparison in Z, it proves the entire NF theorem.

The proof never deletes an upper corner, replaces two different normals by a parallel band, or assumes that the maximizing-D reaction vanishes. No unproved upper-profile extremal classification is needed.

## 7. Boundaries, limits and proper-pair consequence

The same proof directly covers m=q, even though the root may cease to be a maximal facet. It covers p=q by its low-regime formula, sigma=2 by either sector, d=1 by the endpoint chord calculation, and U(1)>0 without forcing A to be the only top point. For d=0, actual consistency gives u=1 and sigma=1; the general coefficient cube is merely an overcover of that boundary. The original coordinate map remains invertible because 0<b<1.

The formal parameter endpoints b=0,1 do not justify declaring a collapsed chart a physical three-dimensional successor. Nevertheless every sequence of actual NF bodies obeys the uniform estimate, hence limsup T<=203/100 even if its geometry degenerates. There is no equality at 51/25, and the actual gap from that threshold is greater than 1/100.

The sharp supremum is NOT identified by this certificate. The familiar real limiting family remains: take u=1, U=1 up to d and U=(1-w)/(1-d) afterwards, m=(1+b)rho, and let d decrease to zero. Its limit trace is exactly

    2(1-b^2)(1-b rho^3)/[(1-b rho^2)(1-b^2 rho^2)].

For b=1/5,rho=4/5 this is 44880/22127>2. Thus the theorem is not a disguised T<=2 claim, and there is no purported characterization of all extremizing U.

For a positive-root NF, choose q0 in the root's relative interior with positive original x,y and form the actual body

    P_lambda=conv(Tetra,lambda P+(1-lambda)q0).

Its coordinate maximal faces are exactly ABC and ABD. Since the contracted body lies strictly inside both coordinate halfspaces,

    V_lambda>=lambda^3 V, E_lambda>=lambda^4 E, N_lambda<=N,
    T(P_lambda)<=lambda^(-7)T(P).

This is a proved bound, not trace monotonicity. For EVERY 9993/10000<=lambda<1, Bernoulli's inequality gives lambda^7>=9951/10000 and therefore

    T(P_lambda)<20300/9951<51/25,
    51/25-20300/9951=1/248775.

This closes an all-aspect proper-resolution family. It does not represent arbitrary proper one-zero bodies and supplies no equilibrium-count claim for the whole family.

## 8. Exact non-record controls and failed shortcuts

All three controls are rational full-dimensional convex polytopes. They retain the four canonical marks, their stated root, max ell=1, and the weighted maximizing-D condition. Their own volume centroids are recalculated. Each has strict (S,U,H)=(4,4,6), weak000, and all four primitives on every true edge are nonzero. Maximal facets and true edges are reconstructed independently of the integration triangulations. None is proper33, E17, or 110.

**High-root control.** Take

    b=7/10, d=1/10000, u=501/500,
    p=(1+b)/u, q=1+b+d,
    m=p+(q-p)/1000=2833339167/1670000000,
    U through (0,1),(d,u),(1,0).

The high-to-low seam is exactly 122507/1275000175010. Its actual f-vector is 8/12/6; the coordinate maximal facets have 5 and 4 vertices. Its exact trace is

    66836586574386148159652140159864341373926294299439426364001
    /33416037281951166401271119029435243384900510293251496375507
    = approximately 2.000135025300748.

This defeats the stronger proposed bound T<=2 for the entire high-root branch.

**Upper-corner deletion control and its actual replacement.** Both bodies have

    b=1/5, d=1/100, u=499/500, m=100067/100000.

The original U has knots

    (0,1), (1/100000,60877501/60500000), (1/100,499/500), (1,0).

The replacement removes only the second knot. Both lower cuts are wholly in the low regime; this failure is not caused by a missed high-root seam. The original has f=10/15/7 and coordinate faces 6/6; the replacement has f=8/12/6 and coordinate faces 5/5. Their exact traces are respectively

    13210507350560212437427345364518410000000
    /6545749520234525181244243398173290963307,

    788512784416576348656000/390781562542748106206281.

They are approximately 2.018181005815036 and 2.017784000058394. The first is strictly larger. V,X,Y,Z,E,N and the own COM change; no old moment is reused after deletion. The capsule computes the exact positive difference and independently matches every actual moment to rational section integration.

These failures explain the successful change of approach: retain the real overshoot in the volume and numerator together, rather than assume a shape-deletion monotonicity. Exploratory numerical searches were used only to locate tests; no failed search is used as an exclusion or optimality statement.

## 9. Complete deterministic recovery capsule

Save the complete source below as nf_full_certificate.py, UTF-8/LF with one final LF. Run with assertions enabled:

    python nf_full_certificate.py > nf_full_receipt.txt

Tested: CPython 3.13.5, NumPy 2.3.5, SymPy 1.14.0. There are no external inputs or random choices. NumPy arrays use dtype=object, integer transformations, and exact cross multiplication; no floating result participates in acceptance.

Observed normal and clean-directory pins:

    nf_full_certificate.py: 16768 bytes
    SHA256 5538f746d6845225abd1c95f065f9d49adefcbc68f4c8a98f1f8e82a2f165908
    nf_full_certificate.json: 13328 bytes
    SHA256 7978551bdb4bb2a266107a9bd50b62ca0c419f6644fea0eee1abc023768b535c
    nf_full_receipt.txt: 687 bytes
    SHA256 5ca472893a2b0d1ba080a74a9ea6c94540ef167be824a16bf3607bcb98503509

Expected terminal marker:

    ONE_ZERO_FULL_TWO_NORMAL_NF_TRACE_203_EXACT_RECOVERY_PASS

The report contains every control vertex, maximal face, supporting plane, true edge, all V,X,Y,Z,E,N, own COM, mechanical labels, exact seams, complete subdivision paths and certificate statistics. The source reconstructs them all without the parent code. Exact inverse basis conversion and independent affine substitution check the finite certificate; three separate volume fans and a fourth exact sectional integration check the physical controls. This is an executed exact-arithmetic certificate, not a proof-assistant formalization.

```python
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, lcm
from pathlib import Path
import hashlib
import json
import numpy as np
from sympy.polys.rings import ring
from sympy.polys.domains import ZZ

PARENT = 'minimum-0150'
PARENT_SHA256 = '5e8296567dc16cfab235ec6069f21d3ce50e228fd6f176791acae439b2ff8f43'
# CPython 3.13.5, NumPy 2.3.5, SymPy 1.14.0; all acceptance arithmetic is exact.
# No external inputs, floating locator, random seed, or numerical hull is used.

def axis_map(A, M, j):
    return np.moveaxis(np.tensordot(M, A, axes=(1,j)),0,j)

def inverse_bern(A):
    B=A.copy()
    for j,n in enumerate(x-1 for x in A.shape):
        M=np.array([[comb(n,k)*comb(k,i)*(-1)**(k-i) if i<=k else 0
                     for i in range(n+1)] for k in range(n+1)],dtype=object)
        B=axis_map(B,M,j)
    return B

def bern(pp):
    dim=len(next(iter(pp)))
    n=tuple(max(a[j] for a in pp) for j in range(dim))
    power=np.zeros(tuple(x+1 for x in n),dtype=object)
    for a,c in pp.items(): power[a]=int(c)
    A=power.copy(); den=1
    for j,nn in enumerate(n):
        L=lcm(*(comb(nn,k) for k in range(nn+1))); den*=L
        M=np.array([[L*comb(i,k)//comb(nn,k) if k<=i else 0
                     for k in range(nn+1)] for i in range(nn+1)],dtype=object)
        A=axis_map(A,M,j)
    assert np.array_equal(inverse_bern(A),power*den)
    return A,den,power

def split(A,j):
    n=A.shape[j]-1
    L=np.array([[2**(n-i)*comb(i,k) if k<=i else 0 for k in range(n+1)]
                for i in range(n+1)],dtype=object)
    R=np.array([[2**i*comb(n-i,k-i) if k>=i else 0 for k in range(n+1)]
                for i in range(n+1)],dtype=object)
    return axis_map(A,L,j),axis_map(A,R,j),2**n

def affine_power(P,box):
    # Independent direct substitution x_j=lo_j+(hi_j-lo_j)y_j in the POWER basis.
    A=P.copy(); den=1
    for j,(lo,hi) in enumerate(box):
        width=hi-lo; c=lcm(lo.denominator,width.denominator)
        a=int(lo*c); w=int(width*c); n=A.shape[j]-1
        M=np.array([[comb(i,k)*a**(i-k)*w**k*c**(n-i) if k<=i else 0
                     for i in range(n+1)] for k in range(n+1)],dtype=object)
        A=axis_map(A,M,j); den*=c**n
    return A,den

def stats(A,den):
    vals=[int(x) for x in A.flat]
    return dict(degrees=[x-1 for x in A.shape],coefficients=len(vals),
                positive=sum(x>0 for x in vals),zero=sum(x==0 for x in vals),
                negative=sum(x<0 for x in vals),minimum=str(F(min(vals),den)))

def global_check(pp,strict=False):
    A,den,power=bern(pp)
    assert min(A.flat)>0 if strict else min(A.flat)>=0
    return stats(A,den)

def cube_check(pp):
    A,den,power=bern(pp); stack=[('',A,den,[(F(0),F(1))]*4)]
    leaves=[]; nodes=0
    while stack:
        path,C,scale,box=stack.pop(); nodes+=1
        if min(C.flat)>=0:
            direct,dd=affine_power(power,box)
            assert np.array_equal(inverse_bern(C)*dd,direct*scale)
            # A nonnegative Bernstein polynomial is strictly positive for b<1
            # when all its corner zeros lie on b=1. Check this on EVERY leaf.
            for bits in product([0,1],repeat=4):
                idx=tuple(bits[j]*(C.shape[j]-1) for j in range(4))
                if C[idx]==0: assert box[0][bits[0]]==1
            leaves.append(dict(path=path,box=[[str(l),str(u)]for l,u in box],
                               **stats(C,scale)))
            continue
        assert len(path)<16
        j=(0,3,2,1)[len(path)%4]; C0,C1,factor=split(C,j)
        mid=sum(box[j])/2
        for bit,child in [(1,C1),(0,C0)]:
            bb=box.copy(); bb[j]=(mid,box[j][1]) if bit else (box[j][0],mid)
            stack.append((path+str(bit),child,scale*factor,bb))
    paths=[x['path'] for x in leaves]
    assert sum(F(1,2**len(p)) for p in paths)==1
    assert not any(a!=b and b.startswith(a) for a in paths for b in paths)
    assert nodes==43 and len(leaves)==22 and max(map(len,paths))==10
    return dict(nodes=nodes,leaves=leaves,max_depth=10)

def exact_polynomials():
    out={}
    R3,b,d,t=ring('b,d,t',ZZ); h=1+b; q=h+d; H=1-b*b
    R=4*h*h+2*d*h*q*t+d*q*q*t*t
    D1=R-2*b*q*q*t; D2=R-2*b*b*q*q*t
    Q=41209*D1**2*D2**2-10000*H**2*q*q*(2+t)**2*R**3
    out['large']=[global_check(dict(p),True) for p in [D1,D2,Q]]
    assert out['large'][2]['coefficients']==1755
    R5,b,d,z,r,v=ring('b,d,z,r,v',ZZ)
    h=1+b; q=h+d; S=1+z; H=1-b*b
    R=h*h*S*S+d*q*q+d*h*S*q+v
    all_pp={}
    for typ in ['base','high']:
        a=S*r if typ=='base' else 1+r*z
        L=R5.one if typ=='base' else 1-b+r*z
        Znum=R5.zero if typ=='base' else b*r**3*z*z
        E1=R*S*L-b*a*a*q*q*L+Znum*q*q*S
        E2=R*S-b*b*a*a*q*q
        C=-2*b*a**3*L+4*a*Znum*S
        A=203*E1*E2-100*H*q**4*S*C
        P=A*A-10000*H**2*q*q*S**4*L*L*(1+S)**2*R**3
        pp=[{ii[:4]:int(c) for ii,c in P.items() if ii[4]==k} for k in range(5)]
        all_pp[typ]=pp
        out[typ+'_positive_v']=[global_check(x) for x in pp[1:]]
    out['base_constant']=cube_check(all_pp['base'][0])
    high0=all_pp['high'][0]
    out['high_positive_d']=[global_check({(a[0],a[2],a[3]):c
                              for a,c in high0.items() if a[1]==k}) for k in range(1,13)]
    R3,b,z,r=ring('b,z,r',ZZ); h=1+b; S=1+z; H=1-b*b
    a=1+r*z; L=1-b+r*z; Znum=b*r**3*z*z
    e1=S**3*L-b*a*a*L+Znum*S; e2=S**3-b*b*a*a
    C=-2*b*a**3*L+4*a*Znum*S
    mid=203*e1*e2-100*H*S*C
    rad=100*H*S**5*L*(1+S)
    gap=mid-rad; plus=mid+rad
    d0=R3.from_dict({(a[0],a[2],a[3]):c for a,c in high0.items() if a[1]==0})
    assert d0==h**8*gap*plus
    R3,e,t,rr=ring('e,t,r',ZZ)
    charts=[]
    for which,bb,zz in [('z_le_alpha',1-e,e*t),('alpha_le_z',1-e*t,e)]:
        P=R3.zero
        for (i,j,k),c in gap.items(): P+=int(c)*bb**i*zz**j*rr**k
        assert min(a[0] for a in P)==3
        pp={(i-3,j,k):int(c) for (i,j,k),c in P.items()}
        A,den,power=bern(pp)
        if which=='z_le_alpha':
            C0,C1,factor=split(A,1)
            checks=[]
            for bit,C in enumerate([C0,C1]):
                assert min(C.flat)>0
                box=[(F(0),F(1)),(F(bit,2),F(bit+1,2)),(F(0),F(1))]
                direct,dd=affine_power(power,box)
                assert np.array_equal(inverse_bern(C)*dd,direct*den*factor)
                checks.append(stats(C,den*factor))
        else:
            assert min(A.flat)>=0
            assert all(j==0 and k==0 for i,j,k in np.ndindex(A.shape) if A[i,j,k]==0)
            checks=[stats(A,den)]
        charts.append(dict(chart=which,cancelled_e_power=3,checks=checks))
    out['high_root_gap']=charts
    # Algebraic denominator bound: q^2(D0-S) has this manifestly nonnegative form.
    R3,b,d,z=ring('b,d,z',ZZ);h=1+b;q=h+d;S=1+z
    R0=h*h*S*S+d*q*q+d*h*S*q
    assert R0-S*q*q==h*h*z*z+(h*h*(1-d)+2*b*h*d+b*d*d)*z+d*(2*h+d)*(b+d)
    out['denominator_identity']='PASS'
    return out

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def average(v): return tuple(sum(p[j] for p in v)/len(v) for j in range(3))
def ratrow(row): return tuple(F(x) for x in row)

def solve3(rows,rhs):
    d=det(*rows)
    if not d: return None
    return tuple(det(*(tuple(rhs[i] if k==j else rows[i][k] for k in range(3))
                      for i in range(3)))/d for j in range(3))

def from_halfspaces(H):
    P=set()
    for ids in combinations(range(len(H)),3):
        p=solve3([H[i][0] for i in ids],[H[i][1] for i in ids])
        if p is not None and all(dot(n,p)<=s for n,s in H): P.add(p)
    assert len(P)>=4
    return sorted(P)

def cycle(P,ids,n):
    drop=next(j for j in range(3) if n[j])
    keep=[j for j in range(3) if j!=drop]
    Q=sorted((P[i][keep[0]],P[i][keep[1]],i) for i in ids)
    def turn(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[]
    for p in Q:
        while len(lo)>=2 and turn(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(Q):
        while len(hi)>=2 and turn(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    return tuple(p[2] for p in lo[:-1]+hi[:-1])

def hull(candidates):
    Q=sorted(set(candidates)); raw={}
    for i,j,k in combinations(range(len(Q)),3):
        n=cross(sub(Q[j],Q[i]),sub(Q[k],Q[i]))
        if n==(0,0,0): continue
        s=dot(n,Q[i]); vals=[dot(n,p)-s for p in Q]
        if all(v<=0 for v in vals): pass
        elif all(v>=0 for v in vals): n=mul(-1,n); s=-s; vals=[-v for v in vals]
        else: continue
        ids=tuple(i for i,v in enumerate(vals) if v==0)
        raw[ids]=(n,s)
    extreme=set()
    for ids,(n,s) in raw.items(): extreme.update(cycle(Q,ids,n))
    P=[Q[i] for i in sorted(extreme)]
    index={p:i for i,p in enumerate(P)}; ff={}
    for ids,(n,s) in raw.items():
        face=tuple(sorted(index[Q[i]] for i in cycle(Q,ids,n)))
        ff[face]=(n,s)
    faces=[]; planes=[]
    for ids,(n,s) in sorted(ff.items()):
        f=cycle(P,ids,n)
        faces.append(f); planes.append((n,s))
    edges={}
    for f_id,f in enumerate(faces):
        for i in range(len(f)):
            edge=tuple(sorted((f[i],f[(i+1)%len(f)])))
            edges.setdefault(edge,[]).append(f_id)
    assert all(len(v)==2 for v in edges.values())
    assert len(P)-len(edges)+len(faces)==2
    for p in P:
        active=[n for n,s in planes if dot(n,p)==s]
        assert any(det(*triple)!=0 for triple in combinations(active,3))
    return P,faces,planes,edges

def moments(P,faces,o):
    V=F(0); J=(F(0),)*3
    for f in faces:
        a=P[f[0]]
        for i in range(1,len(f)-1):
            b,c=P[f[i]],P[f[i+1]]
            v=abs(det(sub(a,o),sub(b,o),sub(c,o)))/6
            V+=v
            J=add(J,mul(v/4,add(add(o,a),add(b,c))))
    return V,J

def world(p,b,d):
    x,y,w=p
    return x,y,(1+(d-1)*x-y-w)/(1-b)

def audit(K,b,d,proper):
    P,faces,planes,edges=hull([world(p,b,d) for p in K])
    V,J=moments(P,faces,average(P))
    for o in [P[0],P[-1]]: assert moments(P,faces,o)==(V,J)
    g=mul(1/V,J); X=[sub(p,g) for p in P]
    Q=[mul(1/(s-dot(n,g)),n) for n,s in planes]
    E=V+(d-1)*J[0]-J[1]-(1-b)*J[2]
    N=(1+b)*J[0]+(1+b+d)*J[1]
    T=N/(6*V*E)
    ell=lambda p: 1+(d-1)*p[0]-p[1]-(1-b)*p[2]
    assert min(map(ell,P))==0 and max(map(ell,P))==1
    canonical=[ratrow(r) for r in [(0,0,0),(0,0,1),(0,1,0),(1,0,0)]]
    assert all(all(dot(n,p)<=s for n,s in planes) for p in canonical)
    root=[i for i,p in enumerate(P) if ell(p)==0]
    assert any(set(f)==set(root) for f in faces)
    coord=[]
    for j in [0,1]:
        ids=[i for i,p in enumerate(P) if p[j]==0]
        assert any(set(f)==set(ids) for f in faces)
        coord.append(ids)
    if proper:
        assert {P[i] for i in coord[0]}=={canonical[i] for i in [0,1,2]}
        assert {P[i] for i in coord[1]}=={canonical[i] for i in [0,1,3]}
    pv=[[] for p in P]; pf=[[] for f in faces]; saddles=[]; weak=[]; zero=0
    for edge,(f,h) in sorted(edges.items()):
        i,j=edge
        a=dot(X[i],sub(X[j],X[i])); bb=dot(X[j],sub(X[i],X[j]))
        c=dot(Q[f],sub(Q[h],Q[f])); dd=dot(Q[h],sub(Q[f],Q[h]))
        vals=[a,bb,c,dd]; zero+=sum(v==0 for v in vals)
        pv[i].append(a); pv[j].append(bb); pf[f].append(c); pf[h].append(dd)
        if all(v<0 for v in vals): saddles.append(edge)
        if all(v<=0 for v in vals) and any(v==0 for v in vals): weak.append(edge)
    S=[i for i,v in enumerate(pf) if all(x<0 for x in v)]
    U=[i for i,v in enumerate(pv) if all(x<0 for x in v)]
    # Weak edge-packets are reported, not silently equated with physical-point counts.
    return dict(vertices=P,facets=faces,edges=sorted(edges),planes=planes,
                f_vector=[len(P),len(edges),len(faces)],V=V,X=J[0],Y=J[1],Z=J[2],
                E=E,N=N,T=T,centroid=g,root=root,coordinate_faces=coord,
                strict_SUH=[len(S),len(U),len(saddles)],stable=S,unstable=U,
                saddle_edges=saddles,weak_edge_packets=weak,zero_primitives=zero)


def interp(knots,w):
    for (l,a),(r,b) in zip(knots[:-1],knots[1:]):
        if l<=w<=r: return a+(b-a)*(w-l)/(r-l)
    raise AssertionError('height outside profile')

def nf_moments(b,d,u,m,knots):
    h=1+b;p=h/u;q=h+d
    cuts=sorted(set([w for w,z in knots]+[b,d]))
    seams=[]
    for l,r in zip(cuts[:-1],cuts[1:]):
        v0=m*max(1-l/b,0)-p*interp(knots,l)
        v1=m*max(1-r/b,0)-p*interp(knots,r)
        if v0*v1<0: seams.append(l+(r-l)*v0/(v0-v1))
    cuts=sorted(set(cuts+seams))
    integrals=[F(0)]*4
    for l,r in zip(cuts[:-1],cuts[1:]):
        for k,weight in enumerate([1,3,3,1]):
            w=l+(r-l)*F(k,3);U=interp(knots,w);t=m*max(1-w/b,0)
            if t<=p*U:
                area=U*U/2-t*t/(2*p*q)
                ix=U**3/6-t**3/(6*p*p*q)
                iy=U**3/6-t**3/(6*p*q*q)
            else:
                z=q*U-t;area=z*z/(2*q*(q-p))
                ix=area*z/(3*(q-p))
                iy=area*(U-z/(3*q)-z/(3*(q-p)))
            for j,val in enumerate([area,w*area,ix,iy]):
                integrals[j]+=(r-l)*weight*val/8
    A,B,Ix,Iy=integrals; alpha=1-b
    V=A/(alpha*u);E=B/(alpha*u);X=Ix/(alpha*u*u);Y=Iy/(alpha*u)
    N=h*X+q*Y;Z=(V+(d-1)*X-Y-E)/alpha
    return dict(V=V,X=X,Y=Y,Z=Z,E=E,N=N,T=N/(6*V*E)),seams

def nf_control(b,d,u,m,knots):
    h=1+b;q=h+d;p=h/u
    assert 0<b<1 and 0<d<=1 and 0<=m<q and p<=q
    assert knots[0]==(0,1) and knots[-1][0]==1 and interp(knots,d)==u
    slopes=[(v1-v0)/(w1-w0) for (w0,v0),(w1,v1) in zip(knots[:-1],knots[1:])]
    assert all(a>=c for a,c in zip(slopes[:-1],slopes[1:]))
    assert all(v>=0 for w,v in knots)
    H=[(ratrow(n),F(s)) for n,s in
       [((-1,0,0),0),((0,-1,0),0),((0,0,-1),0),((0,0,1),1)]]
    for (l,U),(r,W),slope in zip(knots[:-1],knots[1:],slopes):
        c=U-slope*l
        H.append(((u,F(1),-slope),c))
        cand=[l,r]
        if slope<0:
            t=-(c+h*slope)/(2*slope)
            if l<t<r:cand.append(t)
        assert all((h+t)*(c+slope*t)<=q*u for t in cand)
    H.append(((-h,-q,-m/b),-m))
    K=from_halfspaces(H); result=audit(K,b,d,False)
    integ,seams=nf_moments(b,d,u,m,knots)
    assert all(result[k]==val for k,val in integ.items())
    assert result['zero_primitives']==0 and not result['weak_edge_packets']
    assert result['T']<F(203,100)
    result.update(inputs=dict(b=b,d=d,u=u,m=m,knots=knots),
                  high_branch=m>p,section_seams=seams,
                  maximal_face_sizes=[len(f) for f in result['facets']])
    return result

def physical_controls():
    # Genuine high-root branch with T>2: lower and upper normals are NOT parallel.
    b,d,u=F(7,10),F(1,10000),F(501,500)
    h=1+b;q=h+d;p=h/u;m=p+(q-p)/1000
    high=nf_control(b,d,u,m,[(F(0),F(1)),(d,u),(F(1),F(0))])
    assert high['high_branch'] and high['T']>2 and len(high['section_seams'])==1
    # Genuine early upper curvature whose deletion LOWERS trace above 2.
    b,d,u=F(1,5),F(1,100),F(499,500)
    q=1+b+d;m=q*F(827,1000); t=d/1000
    peak=1+(u-1)*t/d+(d-t)*((u-1)/d+u/q)
    bent=nf_control(b,d,u,m,[(F(0),F(1)),(t,peak),(d,u),(F(1),F(0))])
    chord=nf_control(b,d,u,m,[(F(0),F(1)),(d,u),(F(1),F(0))])
    assert not bent['high_branch'] and not chord['high_branch']
    assert bent['T']>chord['T']>2
    assert bent['centroid']!=chord['centroid']
    return dict(high_root=high,bent_upper=bent,chord_upper=chord,
                chord_trace_loss=bent['T']-chord['T'])

def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x

def main():
    assert __debug__
    algebra=exact_polynomials();controls=physical_controls()
    report=dict(version=1,parent=PARENT,parent_sha256=PARENT_SHA256,
                threshold='203/100',algebra=algebra,controls=controls)
    data=(json.dumps(serial(report),sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('nf_full_certificate.json').write_bytes(data)
    print('LARGE_ASPECT_GLOBAL_BERNSTEIN',1755)
    print('BASE_CONSTANT_CLOSED_CUBE',43,22,10)
    print('HIGH_CONSTANT_D_COEFFICIENTS',12,'ROOT_BLOWUP_CHARTS',2)
    print('EXACT_INVERSE_BERNSTEIN_AND_INDEPENDENT_LEAF_SUBSTITUTION_PASS')
    for key in ['high_root','bent_upper','chord_upper']:
        a=controls[key]
        print(key,*a['f_vector'],'T',a['T'],'SUH',*a['strict_SUH'],'ZERO',a['zero_primitives'])
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('ONE_ZERO_FULL_TWO_NORMAL_NF_TRACE_203_EXACT_RECOVERY_PASS')

if __name__=='__main__':main()
```

## 10. Scientific effect and precise remaining complement

The full NF threshold problem is closed, as is the parent's all-aspect CH class under its accepted actual-body domination. No additional upper-profile localization assumption remains in that implication.

What remains is genuinely different geometry: one-zero sections not satisfying CH, including sections missing an axis or extending beyond their outer axis chord; and bodies with max ell>ell(A). The earlier proper high-trace control that loses B under naive n-aligned radial replacement remains a valid warning for that complement. Neither the present overshoot estimate nor the CH reduction licenses that replacement there. :contentReference[oaicite:3]{index=3}

The most useful next geometric target is an actual upper section with more than one supporting positive normal, retaining its common-edge interval and common uniform mass. The reusable ingredient here is the simultaneous accounting of the same clipped-away auxiliary region in volume and mixed moment, followed by a sign-safe bound on its actual size. A freely assigned section centroid or an independent area profile would not supply that identity.

No E17 exclusion, new monostatic body, improved complexity endpoint, or sharp NF supremum is claimed. The source and the exact nonwinning constructions are durable in this handoff.

Convenience copies, not dependencies: [source](sandbox:/mnt/data/nf_work/nf_full_certificate.py), [exact report](sandbox:/mnt/data/nf_work/nf_full_certificate.json), [execution receipt](sandbox:/mnt/data/nf_work/nf_full_receipt.txt).
