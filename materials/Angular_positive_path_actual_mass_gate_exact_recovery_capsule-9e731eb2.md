# material-9e731eb26824

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Angular positive-path envelopes and actual uniform-mass obstruction

This capsule preserves a derived necessary theorem and its complete deterministic arithmetic verifier. It does NOT contain a new polyhedron, does NOT prove that the requested general C<500 construction is impossible, and does NOT replace an actual maximal-hull/centroid/strict-and-weak equilibrium audit. All roots and polars below use the actual physical volume centroid as origin. The earlier Cauchy ball/ellipsoid gate is preserved separately in [internal-source-reference] with compulsory receipt correction [internal-source-reference]; neither is an input to this self-contained verifier.

## 1. Angular path lemma
Let a=R e_z be the unique strict unstable vertex of a weak-free convex polyhedron K. Every other vertex has a true incident edge to a vertex w with v dot (w-v)>0. Following such arrows strictly increases squared norm, so it terminates at a. Suppose these paths use at most k edges, k>1. On a j-edge path p_0=v,...,p_j=a write r_i=|p_i| and delta_i=angle(p_i,p_{i+1}). Positivity gives r_i<r_{i+1} cos(delta_i), with 0<=delta_i<pi/2. If theta=angle(v,a), then theta<=sum delta_i. Concavity of log cos gives

|v| < R product cos(delta_i) <= R cos(theta/j)^j <= R cos(theta/k)^k.

The last comparison follows because j log cos(theta/j) increases with j on its admissible interval; paths exist only where theta/j<pi/2. At the root itself theta=0 and equality |a|=R is allowed.

For a unit support direction w making angle phi with a, a point in direction theta has projection at most R cos(theta/k)^k cos(theta-phi). Nonpositive projections need no bound. For positive projections, apply log-cos concavity to k copies of theta/k and one copy of phi-theta. Their sum is phi, so

h_K(w) <= R cos(phi/(k+1))^(k+1).

For every phi>0 the inequality is strict for a finite K with strict arrows. This is sharp as a one-path envelope, not a claim that a single finite graph realizes all equality directions simultaneously.

Define A_k(R) by this rotational support function. It is the convex hull of the radial path envelope, not the generally nonconvex raw radial plot. In polar angle theta from +z its radial function is

rho_A(theta)=R cos(theta/k)^k, 0<=theta<=theta_star=k*pi/(k+1);
rho_A(theta)=R d_k/(-cos theta), theta_star<=theta<=pi,
where d_k=cos(pi/(k+1))^(k+1).

The second part is the disk in z=-R d_k. Maximizing support gives theta=k*phi/(k+1), including the disk at phi=pi.

## 2. Same-centre polar and necessary moment inequality
Assume the unique stable face has outward normal -e_z and distance r from the origin. Then the same-centre polar Q=K^polar has unique unstable vertex b=-e_z/r. If positive paths in Q have at most l edges, l>1, the angular support lemma for Q implies

K contains I_l(r)=A_l(1/r, root direction -e_z)^polar,
rho_I(theta)=r sec((pi-theta)/(l+1))^(l+1).

Let N_k=-integral over A_k(1) intersect {z<0} of z dV / pi, and P_l=integral over I_l(1) intersect {z>0} of z dV / pi. Radial integration yields

N_k=(1/2) integral from pi/2 to k*pi/(k+1) of cos(theta/k)^(4k) (-cos theta sin theta) dtheta
    +(1/4) cos(pi/(k+1))^(4k+4) tan(pi/(k+1))^2;
P_l=(1/2) integral from 0 to pi/2 of sec((pi-theta)/(l+1))^(4l+4) cos theta sin theta dtheta.

Uniform centroid zero requires positive and negative z first moments to balance. The mandatory positive part is at least pi*r^4*P_l; the available negative part is at most pi*R^4*N_k. A finite polytope misses positive volume in the negative curved part of A_k, so the necessary inequality is STRICT:

(R/r)^4 > P_l/N_k.

This uses actual filled volume, not a freely adjustable centre. It applies to opposite roots as stated. It is not the arbitrary-root-angle formula needed for a generic nonsymmetric body.

## 3. Exact elementary antiderivatives
Put t_a=cos(pi/(k+1))^2, t_0=cos(pi/(2k))^2. Let U_{k-1}(2t-1) be the shifted Chebyshev polynomial of the second kind, and J'(t)=t^(2k) U_{k-1}(2t-1). Then

N_k=k/4 [J(t_a)-J(t_0)]+t_a^(2k+1)(1-t_a)/4.

For L=l+1, expand

(1+x^2)^(L-1) Im((1+i*x)^(2L))=sum_s c_s*x^(2s+1),
F(y)=sum_s c_s*y^(s+1)/(s+1).

With y_0=tan(pi/(2L))^2 and y_1=tan(pi/L)^2,
P_l=-L/8 [F(y_1)-F(y_0)].

Calibration: N_2=91/81920 and P_2=7168/135.

## 4. Orthogonal half-turn architecture is automatic for weak-free110
If K is invariant under an orthogonal half-turn, its actual centroid lies on the fixed axis. The unique U vertex and unique S face are invariant. The vertex therefore lies on the axis; the face normal is axial, and its strict foot is the axial point in the relative interior of the face. They cannot occupy the same end of the axial intersection segment. No interior point of that segment is a vertex, and no other invariant facet can meet the other axial endpoint in its relative interior while that endpoint is a vertex. Thus there is exactly one fixed vertex and exactly one fixed facet: an axial top and opposite full stable base. All other vertices and facets occur in pairs.

Write V=2k+1, F=2l+1. Norm strictly increases along every escape path, so no equal-radius half-turn orbit can recur. Paths need at most k physical and l polar edges. Euler gives E=2(k+l), and the vertex/face degree inequalities give k<=2l-2 and l<=2k-2. Therefore E<=249 implies k+l<=124. There are 2461 admissible integer pairs k,l>=2. The exact interval verifier proves a unique minimum of P_l/N_k at (62,62).

Necessary bounds for every such orthogonal-half-turn weak-free110 body with E<=249:
R/r > a threshold in [1.094959517178,1.094959517179),
r/R < a threshold in [0.913275773498,0.913275773499).

The latter is stronger than the older Cauchy-envelope bound 0.947713283483. The automatic-architecture argument broadens its applicability from an assumed top/base ansatz to every body with this orthogonal half-turn and weak-free110. It does not transfer to symmetry-breaking affine metrics.

For a general polyhedron with opposite roots but without the half-turn, use k=V-1,l=F-1, E=k+l<=249, k<=2l-3,l<=2k-3. The verifier finds the unique minimum at (125,124), giving
R/r > a threshold in [1.046395423816,1.046395423817),
r/R < a threshold in [0.955661671715,0.955661671716).

These are still opposite-root, not arbitrary-root, bounds.

## 5. Scoped low-complexity corollary
For an actual-centred body with axial apex height R and opposite supporting plane z=-r, triangulate its boundary away from the apex and cone to the apex. All other tetrahedron vertices have z>=-r, so each tetrahedron centroid has z>=(R-3r)/4. Their positive-volume average is zero. Hence R/r<=3.

Combining this with the angular mass gate excludes all seven admissible half-turn pairs k+l<10. At k+l=10 the pairs (4,6) and (6,4) are excluded too; only (5,5) passes this necessary test. Consequently C>=40 for this orthogonal-half-turn weak-free110 family. At C40, only V=F=11 survives this test. This is not a construction and not an upgrade of the general independently proved lower bound C>=34.

## 6. Strict angular-envelope nesting still does not realize mass
For balanced k=l=n let d=cos(pi/(n+1))^(n+1). The exact criterion I_n(r) subset A_n(R) is R/r>=1/d. To see it, compare the radial functions. On 0<=theta<=n*pi/(n+1), the logarithm of rho_I/rho_A is convex; its maximum occurs at an endpoint and is at most -log d by log-cos concavity. On the disk portion, put psi=pi-theta. The ratio is cos psi/[d*cos(psi/(n+1))^(n+1)]<=1/d. Equality occurs at an axial endpoint.

For n=62 and R/r=13/12 the angular envelopes are STRICTLY nested, yet no uniformly filled measurable set between them can have zero z first moment. The exact verifier encloses:
- nesting threshold 1/d in [1.081514830046,1.081514830047);
- (13/12)*d-1 in [0.001681440916113378,0.001681440916113379];
- P_62-(13/12)^4*N_62 in [0.012527460281913980,0.012527460281913981].

This isolates a genuine moment obstruction beyond support-envelope containment. It is not evidence of a finite polyhedron between the two envelopes.

## 7. Recovery, verification, precision and expected identities
Save the complete first Python block below as angle_gate_exact.py, preserving ASCII bytes and LF newlines, including its final newline. It has 10470 bytes, SHA-256 b9e0c23651bff694876dcde9591c64bbb77cc594a928ce0f32f02aa917a0ae50.

Command, with assertions enabled:
python -B -S angle_gate_exact.py

No input checkpoint, random seed or external file is required. Python >=3.10 standard library suffices; execution was observed on Python3.13.5. All arithmetic is integer/rational with outward rounding on a 2^-1024 grid. Machin's identity uses 300 terms for atan(1/5) and 100 for atan(1/239), with exact alternating remainders. Cosine uses 160 terms and an explicit next-term absolute remainder on angles at most pi/3. Interval antiderivatives enclose every value; each minimum is separated by comparing the chosen upper bound with EVERY other lower bound, not by trusting a floating argmin. All fourth-root brackets use exact integer comparisons.

Expected output file ANGLE_PATH_MASS.json: 62245 bytes, SHA-256 9b915175afe359c27f2db15bb283b3ff518526577322ba5a5bcf10cf923056e7.
Expected terminal markers:
ANGLE_PATH_MASS_RIGOROUS_PASS 62245 9b915175afe359c27f2db15bb283b3ff518526577322ba5a5bcf10cf923056e7
C2_FAMILY_C_GE_40_ONLY_NOT_A_CONSTRUCTION 7
ANGLE_NESTED_BUT_NO_ZERO_MASS_PASS 62 13/12

The second Python block is the complete optional binary64 scout, scout.py, 1046 bytes, SHA-256 ce33245a9beca0631a6b34ee657545135e80661b9a71e050bb5fd0afe017cb0a. It materially preceded the exact verifier. Observed environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0. Command python scout.py. Its general-pair loop used the looser -2 inequalities; the exact verifier correctly uses -3 for the general nonsymmetric opposite-root graph. The scout is not a certificate, and its optional dependency is not needed for the exact results.

## 8. Complete exact verifier
```python
#!/usr/bin/env python3
"""Rigorous angle-path volume-moment gates, Python >=3.10 standard library.
No inputs, random seed, third-party package, or external files.
The interval grid is 2^-1024 and all arithmetic is integer/rational.
"""
from fractions import Fraction as F
from math import comb
import hashlib
import json

BITS = 1024
SCALE = 1 << BITS


def ceildiv(a, b):
    assert b > 0
    return -((-a)//b)


class I:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None):
        self.lo = int(lo)
        self.hi = self.lo if hi is None else int(hi)
        assert self.lo <= self.hi

    @staticmethod
    def exact(x):
        x = F(x)
        return I((x.numerator*SCALE)//x.denominator,
                 ceildiv(x.numerator*SCALE, x.denominator))

    def __add__(self, other):
        if not isinstance(other, I):
            other = I.exact(other)
        return I(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other if isinstance(other, I) else -F(other))

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        if not isinstance(other, I):
            q = F(other)
            a, b = self.lo*q.numerator, self.hi*q.numerator
            if a > b:
                a, b = b, a
            return I(a//q.denominator, ceildiv(b, q.denominator))
        products = [a*b for a in (self.lo,self.hi)
                    for b in (other.lo,other.hi)]
        return I(min(products)//SCALE, ceildiv(max(products), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other,I):
            return self * (1/F(other))
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError('interval contains zero')
        if other.hi < 0:
            return (-self)/(-other)
        numerators = [(a*SCALE,b) for a in (self.lo,self.hi)
                      for b in (other.lo,other.hi)]
        return I(min(a//b for a,b in numerators),
                 max(ceildiv(a,b) for a,b in numerators))

    def __rtruediv__(self, other):
        return I.exact(other)/self

    def __pow__(self, power):
        assert isinstance(power,int) and power >= 0
        result, x = I.exact(1), self
        while power:
            if power & 1:
                result = result*x
            x = x*x
            power >>= 1
        return result

    def rational_bounds(self):
        return F(self.lo,SCALE),F(self.hi,SCALE)

    def decimal_bracket(self, digits=30):
        d=10**digits
        return [str(F(self.lo*d//SCALE,d)),
                str(F(ceildiv(self.hi*d,SCALE),d))]


def atan_reciprocal_bounds(q, terms):
    # Alternating arctangent series. q>=2 and an even number of terms.
    assert q >= 2 and terms % 2 == 0
    s=F(0)
    for j in range(terms):
        s += F((-1)**j,(2*j+1)*q**(2*j+1))
    remainder=F(1,(2*terms+1)*q**(2*terms+1))
    return s,s+remainder


def pi_interval():
    a,b=atan_reciprocal_bounds(5,300)
    c,d=atan_reciprocal_bounds(239,100)
    low,high=16*a-4*d,16*b-4*c
    assert F(3)<low<high<F(22,7)
    return I(I.exact(low).lo,I.exact(high).hi)


def cos_interval(x):
    # All angles in this proof are positive and at most pi/3 < 22/21.
    # The 160-term alternating series has absolute error at most its next term.
    assert 0 <= x.lo <= x.hi < I.exact(F(22,21)).hi
    square=x*x
    total=term=I.exact(1)
    for j in range(1,160):
        term=(-term)*square/F((2*j-1)*(2*j))
        total=total+term
    next_abs=(term*square/F(319*320))
    error=max(abs(next_abs.lo),abs(next_abs.hi))
    return I(total.lo-error,total.hi+error)


def chebyshev_u_shifted(n):
    # Ascending integer coefficients of U_n(2*t-1).
    if n==0:
        return [1]
    old,current=[1],[-2,4]
    for unused in range(1,n):
        nxt=[0]*(len(current)+1)
        for j,c in enumerate(current):
            nxt[j]-=2*c
            nxt[j+1]+=4*c
        for j,c in enumerate(old):
            nxt[j]-=c
        old,current=current,nxt
    return current


def horner(x, coefficients):
    out=I.exact(0)
    for c in reversed(coefficients):
        out=out*x+F(c)
    return out


def negative_outer(k, pi):
    # N_k is -integral_{A_k,z<0} z / pi with root norm R=1.
    ta=cos_interval(pi/F(k+1))**2
    t0=cos_interval(pi/F(2*k))**2
    u=chebyshev_u_shifted(k-1)
    coefficients=[F(c,2*k+j+1) for j,c in enumerate(u)]
    def primitive(t):
        return t**(2*k+1)*horner(t,coefficients)
    out=F(k,4)*(primitive(ta)-primitive(t0))
    out=out+F(1,4)*ta**(2*k+1)*(1-ta)
    assert out.lo>0
    return out


def positive_inner(l, pi):
    # P_l is integral_{A_l(-e_z)^polar,z>0} z / pi for r=1.
    L=l+1
    c0=cos_interval(pi/F(2*L))**2
    c1=cos_interval(pi/F(L))**2
    y0=(1-c0)/c0
    y1=(1-c1)/c1
    odd=[(-1)**j*comb(2*L,2*j+1) for j in range(L)]
    binomial=[comb(L-1,j) for j in range(L)]
    coefficients=[0]*(2*L-1)
    for j,a in enumerate(odd):
        for k,b in enumerate(binomial):
            coefficients[j+k]+=a*b
    primitive_coefficients=[F(0)]+[F(a,j+1) for j,a in enumerate(coefficients)]
    out=-F(L,8)*(horner(y1,primitive_coefficients)-horner(y0,primitive_coefficients))
    assert out.lo>0
    return out


def fourth_root_bracket(x, digits=12):
    assert x.lo>0
    d=10**digits
    def floor_at(q):
        left,right=0,d
        while right**4*SCALE<=q*d**4:
            right*=2
        while right-left>1:
            mid=(left+right)//2
            if mid**4*SCALE<=q*d**4:
                left=mid
            else:
                right=mid
        return left
    a,b=floor_at(x.lo),floor_at(x.hi)+1
    assert a**4*SCALE<=x.lo*d**4
    assert b**4*SCALE>x.hi*d**4
    return [str(F(a,d)),str(F(b,d))]


def prove_minimum(pairs, values, expected):
    candidates=[(values[l][1]/values[k][0],k,l) for k,l in pairs]
    chosen=[t for t in candidates if (t[1],t[2])==expected]
    assert len(chosen)==1
    q,k,l=chosen[0]
    others=[x for x,i,j in candidates if (i,j)!=expected]
    assert all(x.lo>q.hi for x in others)
    separation=min(x.lo-q.hi for x in others)
    return dict(admissible_integer_pairs=len(candidates),
                unique_minimizer=[k,l],
                P_over_N_enclosure=q.decimal_bracket(),
                minimum_separation_from_other_pairs=str(F(separation,SCALE)),
                R_over_r_threshold=fourth_root_bracket(q),
                r_over_R_threshold=fourth_root_bracket(1/q))


def main():
    pi=pi_interval()
    values={k:(negative_outer(k,pi),positive_inner(k,pi)) for k in range(2,166)}
    # Closed rational calibration when all squared trig endpoints are rational.
    assert values[2][0].lo<=F(91,81920)*SCALE<=values[2][0].hi
    assert values[2][1].lo<=F(7168,135)*SCALE<=values[2][1].hi
    c2=[(k,l) for k in range(2,125) for l in range(2,125)
        if k+l<=124 and k<=2*l-2 and l<=2*k-2]
    assert len(c2)==2461
    general=[(k,l) for k in range(2,166) for l in range(2,166)
             if k+l<=249 and k<=2*l-3 and l<=2*k-3]
    # For C2, E=2(k+l). R/r<=3 by the exact apex tetrahedral mass decomposition.
    c2_below40=[(k,l) for k,l in c2 if k+l<10]
    assert all(values[l][1].lo>81*values[k][0].hi for k,l in c2_below40)
    c2_at40=[(k,l) for k,l in c2 if k+l==10]
    assert c2_at40==[(4,6),(5,5),(6,4)]
    assert all(values[l][1].lo>81*values[k][0].hi
               for k,l in c2_at40 if (k,l)!=(5,5))
    # (5,5) passes this NECESSARY moment test; this does not construct a polytope.
    assert values[5][1].hi<81*values[5][0].lo
    # For balanced k=l=n, exact angular-envelope nesting is R/r>=1/d.
    # This strictly nested pair nevertheless has a positive forced moment.
    n=62
    ratio=F(13,12)
    d=cos_interval(pi/F(n+1))**(n+1)
    nesting_margin=ratio*d-1
    forced_moment=values[n][1]-ratio**4*values[n][0]
    assert nesting_margin.lo>0 and forced_moment.lo>0
    report=dict(
        theorem='strict necessary actual-uniform-mass gate from sharp positive-path angular support envelopes; opposite roots only',
        status='no new polyhedron and no general C<500 exclusion',
        arithmetic=dict(grid_bits=BITS,atan_terms_5=300,atan_terms_239=100,cos_terms=160,
                        pi_enclosure=pi.decimal_bracket(60),packages='Python standard library only'),
        formulas=dict(outer_support='h_k(phi)=R*cos(phi/(k+1))^(k+1)',
                      inner_radial='rho_l(theta)=r*sec((pi-theta)/(l+1))^(l+1)',
                      strict_necessary='(R/r)^4 > P_l/N_k'),
        values={str(k):dict(N=v[0].decimal_bracket(),P=v[1].decimal_bracket())
                for k,v in values.items()},
        C2_E249=prove_minimum(c2,values,(62,62)),
        general_opposite_roots_E249=prove_minimum(general,values,(125,124)),
        C2_complexity_floor=dict(excluded_pairs_below_C40=[list(t) for t in c2_below40],
                                excluded_pairs_at_C40=[[4,6],[6,4]],
                                first_unexcluded_pair=[5,5],
                                conclusion='C>=40 necessary for this orthogonal half-turn, axial top/full opposite base family only'),
        strictly_nested_but_mass_impossible=dict(k=n,l=n,R_over_r=str(ratio),
            exact_nesting_condition='R/r >= sec(pi/(n+1))^(n+1)',
            nesting_threshold=(1/d).decimal_bracket(12),
            nesting_margin_Rd_over_r_minus_1=nesting_margin.decimal_bracket(18),
            positive_forced_moment_div_pi_r4=forced_moment.decimal_bracket(18)),
        limits='Sharp one-path support bounds allow an entire continuous envelope; simultaneous finite primal/polar path realization, convex mass feasibility and the weak-free110 census remain open. The opposite-root moment formulas are not arbitrary-root-angle formulas.')
    payload=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
    with open('ANGLE_PATH_MASS.json','wb') as out:
        out.write(payload)
    print('ANGLE_PATH_MASS_RIGOROUS_PASS',len(payload),hashlib.sha256(payload).hexdigest())
    for name in ('C2_E249','general_opposite_roots_E249'):
        print(name,report[name]['unique_minimizer'],report[name]['R_over_r_threshold'],report[name]['r_over_R_threshold'])
    print('C2_FAMILY_C_GE_40_ONLY_NOT_A_CONSTRUCTION',len(c2_below40))
    print('ANGLE_NESTED_BUT_NO_ZERO_MASS_PASS',n,str(ratio),
          report['strictly_nested_but_mass_impossible'])


if __name__=='__main__':
    main()
```

## 9. Complete optional numerical scout
```python
import math,json
from scipy.integrate import quad


def angle_N(k):
    if k<=1:return 0
    a=math.pi/(k+1);t=k*a
    integ=quad(lambda th:math.cos(th/k)**(4*k)*(-math.cos(th)*math.sin(th)), math.pi/2,t,epsabs=1e-13,epsrel=1e-13)[0]/2
    return integ+math.cos(a)**(4*k+4)*math.tan(a)**2/4

def angle_P(l):
    L=l+1
    return quad(lambda th:math.cos((math.pi-th)/L)**(-4*L)*math.cos(th)*math.sin(th),0,math.pi/2,epsabs=1e-12,epsrel=1e-13)[0]/2

if __name__=='__main__':
    values={k:(angle_N(k),angle_P(k)) for k in range(2,166)}
    for k in [2,3,4,5,10,20,40,62,83,124,165]:
        n,p=values[k];print(k,n,p,(p/n)**.25,(n/p)**.25)
    C2=[(values[l][1]/values[k][0],k,l) for k in range(2,125) for l in range(2,125) if k+l<=124 and k<=2*l-2 and l<=2*k-2]
    general=[(values[l][1]/values[k][0],k,l) for k in range(2,166) for l in range(2,166) if k+l<=249 and k<=2*l-2 and l<=2*k-2]
    print('C2 best',min(C2),min(C2)[0]**.25,min(C2)[0]**(-.25))
    print('general opposite best',min(general),min(general)[0]**.25,min(general)[0]**(-.25))
```

## 10. Remaining constructive gap
The angular envelopes are necessary relaxed bodies. Even compatible nesting and first moments do not supply one finite mutually polar graph, a convex intermediate with actual centroid zero, or strict110/weak000. Potential refinements are the compulsory stable plane z>=-r, mandatory apex a, angular packing with a finite total vertex budget, and projected moment inequalities for nonopposite roots. None is claimed computed here. The C2 bound leaves a broad admissible interval 1/3<=r/R<0.913275773499, so it does not exclude the active changed-corpus or actual-mass construction fronts.
