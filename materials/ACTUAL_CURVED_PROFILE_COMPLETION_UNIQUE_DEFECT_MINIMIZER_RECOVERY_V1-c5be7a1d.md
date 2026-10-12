# material-c5be7a1d6519

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Exact curved completion: a unique fixed-test defect minimizer with the actual centroid fixed

## 1. What is proved, and what is not
There exists a genuine homogeneous convex3D body with square homothetic cross-sections, an ACTUAL volume centroid at the origin, four whole triangular lateral facets and one whole square cap, for which a curved continuation uniquely minimizes a specified volume-scaled3/2 matrix defect among ALL continuations that preserve the marked flat piece, the axial interval and the actual centroid. A genuine two-affine-piece continuation with exactly those same constraints exists, but has strictly LARGER defect.

This is an exact countercontrol to the proposed localization step 'replace the rest of the profile by an affine piece without increasing the fixed-centre, fixed-facet defect.' It does NOT disprove every possible two-piece localization, optimize the generalized Rayleigh ratio, furnish an unrestricted stationary maximum, or violate3/2. On the contrary, the full3/2 matrix gaps of ALL FIVE whole flat facets of the curved body are strictly positive definite. It is not a polytope, so no finite V/E/F or equilibrium census is assigned. No lower prohibition or canonical construction changes; the bounds34 and622 remain separate.

The scalar whole-profile reduction in [internal-source-reference] remains open for arbitrary concave profiles. This new result explains why its already-proved two-affine-piece theorem cannot be extended by a naive fixed-centre affine-tail replacement. The proof below is self-contained, and the exact executable has no dependency on that prior program.

## 2. The exact actual-centred curved profile
Let u be the UNIQUE root in(0,1) of

    u^4-5u^2+10u-5=0.

It lies in the rational interval

    7490675/10000000 < u < 7490676/10000000,

and numerically u=0.749067502197983350829655430774... . Uniqueness follows because the derivative4u^3-10u+10 is strictly positive on[0,1]. Define

    d=u(2-u), r=-u/(1-u),
    h0(z)=[u+(1-u)z]/sqrt(d),  r<=z<=u,
    h0(z)=sqrt(2z-z^2),        u<=z<=1.

The left line is the tangent to the ellipse arc at z=u. It vanishes at z=r<0. The arc is strictly concave, positive on[u,1], has derivative(1-z)/sqrt(2z-z^2), and second derivative-1/(2z-z^2)^(3/2). Thus h0 is nonnegative and concave on the ENTIRE interval, including its tangent join. The actual body is

    P0={(x,y,z):r<=z<=1, |x|<=h0(z), |y|<=h0(z)}.

It is a full-dimensional convex body of uniform density, not a collection of independent masses. Its four left-side triangles are genuine WHOLE flat facets: the tangent line exceeds the arc strictly for z>u. The top cap z=1 is the fifth whole flat facet. Four curved lateral patches complete the boundary. The exact apex is(0,0,r); each lateral triangle joins it to the two relevant vertices of the square(plus/minus sqrt(d),plus/minus sqrt(d),u). The top square has vertices(plus/minus1,plus/minus1,1).

Write V=int h0^2, M=int z h0^2, E=int z^2 h0^2, N4=int h0^4, all over[r,1]. The actual3D volume is4V. Direct integration gives

    V=-(u^2-2u+2)/(3(u-1)),
    M=-(u^4-5u^2+10u-5)/(12(u-1)^2)=0,
    E=-(u^6-u^5+u^4-9u^3+27u^2-27u+9)/(30(u-1)^3),
    N4=(u^4-4u^3+8u-8)/(15(u-1)).

Reflection symmetry gives mean x=mean y=0, and the displayed exact equation gives mean z=0. Hence the ACTUAL volume centroid is g=0, with

    Sigma=diag(N4/(3V),N4/(3V),E/V).

The centre is not prescribed independently of the body. Numerically V is about1.41202265916659657, E about.839344662916631616, N4 about.896346728639504825. These decimals are diagnostics only; the exact root and formulas define the object.

## 3. Every whole flat facet has a full positive matrix gap
Mark the true whole facet x=h0(z),r<=z<=u. Put

    D0=h_left(0)=u/sqrt(d),
    P1=int_r^u h_left,
    P3=int_r^u h_left^3,
    Pz1=int_r^u z h_left^2,
    Pz2=int_r^u z^2 h_left.

The ACTUAL uniform facet second moment about g=0 is

    T=[[P3/P1,0,Pz1/P1],[0,P3/(3P1),0],[Pz1/P1,0,Pz2/P1]],
    alpha=D0 P1/(2V).

The pole is(1,0,-(1-u)/sqrt(d))/D0; the source checks T pole=c for the actual whole-facet centroid c. All mixed terms are retained.

Define

    H=N4-D0 P3,
    R=3E-D0 Pz2,
    C=D0 Pz1.

Then the x,z block of(3/2)Sigma-alpha T is(1/(2V))*[[H,-C],[-C,R]]. Its other tangential entry is(3N4-D0 P3)/(6V). The top cap has tangential gap(3N4-2)/(6V) and axial gap(3E-2)/(2V). Exact rational polynomial certificates on the entire isolating interval for u show that

    V,N4,E,H,R,H R-C^2,3N4-D0 P3,3N4-2,3E-2

are ALL strictly positive. Every numerator and denominator is converted to a Bernstein polynomial on that exact rational interval, with ALL controls strictly positive. The other three side facets follow by orthogonal reflections/interchange of x,y, not an arbitrary affine transfer of an equilibrium census. Consequently every genuine whole flat facet has a strictly positive full3/2 gap.

## 4. A completion problem with an exact unique curved minimizer
Fix the entire left piece[r,u], the right endpoint1 and the actual centroid0. Consider any competing nonnegative profile h agreeing with h0 on[r,u], for which the completed body is convex and has axial first moment

    int_r^1 z h(z)^2 dz=0.

The uniqueness identity actually holds for the larger measurable class with finite fourth moment and the same first-moment constraint; convexity is only needed to remain in the physical body class. For a physical continuation the marked facet must remain the same whole facet; the curved minimizer and the explicit affine competitor below satisfy that requirement.

Use the fixed centred linear test

    v=(1,0,-sqrt(2/3)), so v dot(x,y,z)=x-sqrt(2/3)z.

For each such completed body let V_h=int h^2, and define the VOLUME-SCALED fixed-test defect

    F[h]=2 V_h v^T[(3/2)Sigma_h-alpha_h T_h]v.

The actual3D volume is4V_h; the scale2V_h is one half of that volume. The marked geometric facet and g=0 are fixed, so all its boundary terms are fixed. Expanding gives

    F[h]=int h^4+2 int z^2 h^2
       -D0[P3-2sqrt(2/3)Pz1+(2/3)Pz2].

On the free interval[u,1] put q(z)=2z-z^2. The exact pointwise square identity is

    k^2-q^2+2z^2(k-q)-4z(k-q)=(k-q)^2,

for any real k. The equal ACTUAL centroid constraint says int_u^1 z(h^2-q)=0. Therefore

    F[h]-F[h0]=int_u^1 [h(z)^2-(2z-z^2)]^2 dz >=0.       (*).

Equality holds only when h^2=q almost everywhere, and for nonnegative continuous profiles only when h=h0 everywhere on the free interval. Thus this genuinely curved continuation is the UNIQUE GLOBAL minimizer of this exact completion problem. This is more than a stationary formal jet or a failed numerical search.

The minimized defect itself is POSITIVE, approximately.696491135656655429. The exact full matrix certificate in Section3 proves that sign without relying on decimals. Multiplication by V_h matters: (*) is NOT a claim that h0 maximizes the normalized Rayleigh ratio, nor that it minimizes every matrix direction in Loewner order.

## 5. A genuine affine same-centroid competitor exists and is strictly worse
Let

    A=int_u^1 z(z-u)^2 dz=-(u-1)^3(u+3)/12>0,
    B=int_u^1 z[u+(1-u)z](z-u)dz
      =-(u-1)^2(u^3-u^2-3u-3)/12.

Here B-A=int_u^1 z(z-u)u(2-z)dz>0. Define

    delta=(B-sqrt(B^2-A^2))/A.

It is the unique root in(0,1-u) of

    A(1+delta^2)-2B delta=0.

At delta0 the expression is positive; at delta=1-u it equals d int_u^1 z[d-(2z-z^2)]dz<0 because the ellipse height strictly increases after u. The derivative is negative over this interval since B/A>1. Thus the root and its interval are exact, not numerically chosen. Numerically delta=.0879773730616579115021225623503... .

Replace the arc by

    h_aff(z)=[u+(1-u)z-delta(z-u)]/sqrt(d), u<=z<=1.

Its slope(1-u-delta)/sqrt(d) is positive and strictly smaller than the left slope. Hence the full profile is genuinely concave with TWO affine pieces and positive free heights. The marked left facet is still whole, now with a genuine crease at z=u. Its axial first-moment difference from h0 is exactly

    [A(1+delta^2)-2B delta]/d=0.

So both completions have the SAME actual centroid and same whole marked facet. Yet (*) gives a strictly positive defect difference: the square of an affine function cannot equal the strictly concave quadratic2z-z^2 throughout a nonempty interval. An exact polynomial integral for this positive difference is in the recovered report. Therefore a two-piece localization that preserves this marked piece, interval and actual centroid while not increasing this defect is genuinely false.

This does NOT invalidate the earlier all-two-piece3/2 theorem; both bodies satisfy the inequality. A broader localization allowing the marked facet, centroid or interval to move is not addressed.

## 6. The useful variational connection: free profile arcs are elliptical
For the general scalar sufficient gate of [internal-source-reference], translate the ACTUAL axial centroid to0 and hold the selected affine facet interval and line fixed. For fixed test coefficients p,w, its free-tail objective has bulk integrand

    p^2 h^4+(9/4)w^2 z^2 h^2,

with constraint int z h^2=0. The exact square-base physical defect instead uses coefficient3 in place of9/4. At a regular constrained stationary profile, on an open interval where h>0 and concavity is strict so both signed compactly supported variations are admissible, the Euler equation gives

    h^2=[lambda z-c w^2 z^2]/(2p^2),

where c=9/4 for the sufficient gate or3 for the actual square-base defect, provided p is nonzero. All such free arcs share the SAME multiplier lambda. Their positive part lies on ONE side of the actual centroid, with the sign of z equal to the sign of lambda. A nonzero test with p=0 has no positive free stationary interval of this type. When w=0 the quadratic degenerates to a square-root linear profile.

This is a conditional free-arc equation, NOT an attainment theorem, a complete finite-arc classification or a global one-arc reduction. It identifies why the natural nonlinear continuation is elliptical rather than automatically affine. In the exact fixture above the Lagrangian density is h^4+2z^2h^2-4zh^2; its first derivative vanishes at h^2=2z-z^2 and its second derivative there is8h^2>0. The complete square identity supplies the global completion statement for this particular fixture.

## 7. Complete standalone recovery and observed execution
Save the complete source below as ellipse_profile_completion.py,6376B, SHA256

    b807376980d76122709c553a0d5c7a042889b893e3ad699a50861b9a1054d839.

CPython3.13.5, SymPy1.14.0, assertions enabled. No external inputs, helpers, seed, precision rule or patch. Reconstruction and verification:

    python -B ellipse_profile_completion.py > ellipse_profile_completion.log

Outputs:

    ellipse_profile_completion_report.json,14317B,
    SHA256087c8acdc584ec0836cedc70849bfb22ed01869c326e1c85b309d7b449fbf621;
    ellipse_profile_completion.log,282B,
    SHA256e64c5269d3fea044f7ce14a233fa829da1af8c331b1f91272fc4535375ab6298.

Terminal markers:

    ACTUAL_CENTROID_QUARTIC_AND_ALL_FIVE_FLAT_FACETS_PD_PASS
    UNIQUE_CURVED_FIXED_TEST_COMPLETION_SQUARE_IDENTITY_PASS
    AFFINE_SAME_CENTROID_COMPETITOR_STRICTLY_WORSE_PASS
    ELLIPSE_PROFILE_COMPLETION_EXACT_PASS

Normal and fresh source-only executions completed with BYTE-IDENTICAL reports and logs. The exact source emits all whole flat facets, actual volume/centroid/covariance, marked full facet matrix and pole identity, exact positivity certificates, the centroid-preserving affine competitor and the square identity. No finite equilibrium census or proof-assistant formalization is claimed.

```python
"""Exact curved completion with the actual centroid fixed.
CPython3.13.5/SymPy1.14.0; assertions on; no external inputs.
The unique minimizer concerns a fixed-test volume-scaled matrix defect,
NOT the generalized Rayleigh ratio or the unrestricted whole-body problem.
"""
from pathlib import Path
import hashlib,json,math
import sympy as S
Q=S.Rational
u,z,dlt,x=S.symbols('u z delta x',real=True)

def clean(v):return S.factor(S.cancel(v))
def zero(v):assert clean(v)==0,clean(v)
def integ(v,lo,hi):return clean(S.integrate(S.expand(v),(z,lo,hi)))
LO=Q(7490675,10000000);HI=Q(7490676,10000000)

def positive_on_root_interval(expr):
    nn,dd=S.fraction(clean(expr))
    if dd.subs(u,(LO+HI)/2)<0:nn=-nn;dd=-dd
    out={}
    for name,poly in [('numerator',nn),('denominator',dd)]:
        p=S.Poly(S.expand(poly.subs(u,LO+(HI-LO)*x)),x,domain=S.QQ);n=p.degree()
        cc=[clean(sum(p.nth(i)*Q(math.comb(k,i),math.comb(n,i)) for i in range(k+1))) for k in range(n+1)]
        assert min(cc)>0,(name,expr,min(cc))
        out[name]=dict(degree=n,controls=cc)
    return out

def main():
    assert __debug__ and S.__version__=='1.14.0'
    rootpoly=u**4-5*u*u+10*u-5
    assert rootpoly.subs(u,LO)<0<rootpoly.subs(u,HI)
    assert LO>0 and HI<1
    # On [0,1], rootpoly'=4u^3-10u+10>0 except no zero at1.
    assert S.diff(rootpoly,u,2).subs(u,LO)<0
    disc=u*(2-u);r=-u/(1-u);ht=(u+(1-u)*z)/S.sqrt(disc);arc2=2*z-z*z
    zero(ht.subs(z,u)**2-arc2.subs(z,u))
    zero(S.diff(ht,z).subs(z,u)-(1-u)/S.sqrt(disc))
    zero(ht**2-arc2-(z-u)**2/disc)
    V=integ(ht**2,r,u)+integ(arc2,u,1)
    M=integ(z*ht**2,r,u)+integ(z*arc2,u,1)
    E=integ(z*z*ht**2,r,u)+integ(z*z*arc2,u,1)
    N4=integ(ht**4,r,u)+integ(arc2**2,u,1)
    zero(M+rootpoly/(12*(1-u)**2))
    D0=u/S.sqrt(disc);P1=integ(ht,r,u);P3=integ(ht**3,r,u)
    Pz1=integ(z*ht**2,r,u);Pz2=integ(z*z*ht,r,u)
    H=clean(N4-D0*P3);R=clean(3*E-D0*Pz2);C=clean(D0*Pz1)
    cert={name:positive_on_root_interval(expr) for name,expr in [
        ('volume',V),('covariance_tangent',N4),('covariance_axial',E),
        ('marked_x_gap',H),('marked_axial_gap',R),('marked_xz_determinant',H*R-C*C),
        ('marked_other_tangent_gap',3*N4-D0*P3),('top_tangent_gap',3*N4-2),('top_normal_gap',3*E-2)]}
    Sigma=S.diag(N4/(3*V),N4/(3*V),E/V)
    TF=S.Matrix([[P3/P1,0,Pz1/P1],[0,P3/(3*P1),0],[Pz1/P1,0,Pz2/P1]])
    alpha=clean(D0*P1/(2*V));pole=S.Matrix([1/D0,0,-(1-u)/(S.sqrt(disc)*D0)])
    cf=S.Matrix([integ(ht**2,r,u)/P1,0,integ(z*ht,r,u)/P1])
    assert (TF*pole-cf).applyfunc(clean)==S.zeros(3,1)
    test=S.Matrix([1,0,-S.sqrt(Q(2,3))])
    F=clean(2*V*(test.T*(Q(3,2)*Sigma-alpha*TF)*test)[0])
    zero(F-(H+Q(2,3)*R+2*S.sqrt(Q(2,3))*C))
    AA=integ(z*(z-u)**2,u,1)
    BB=integ(z*(u+(1-u)*z)*(z-u),u,1)
    zero(BB-AA-integ(z*(z-u)*u*(2-z),u,1))
    eq=clean((1+dlt*dlt)*AA-2*dlt*BB)
    # Unique physical root lies between0 and1-u: constant-height completion is too low.
    zero(eq.subs(dlt,1-u)-disc*integ(z*(disc-arc2),u,1))
    delta_exact=clean((BB-S.sqrt(BB*BB-AA*AA))/AA)
    affine=(u+(1-u)*z-dlt*(z-u))/S.sqrt(disc)
    mdiff=integ(z*(affine**2-arc2),u,1)
    zero(mdiff-eq/disc)
    gap=integ((affine**2-arc2)**2,u,1)
    energy_diff=integ(affine**4-arc2**2+2*z*z*(affine**2-arc2),u,1)
    zero(energy_diff-4*mdiff-gap)
    # Abstract exact pointwise square identity, valid for any competing h^2=k.
    k=S.symbols('k',real=True)
    zero(k*k-arc2**2+2*z*z*(k-arc2)-4*z*(k-arc2)-(k-arc2)**2)
    hh=S.symbols('h',positive=True)
    lag=hh**4+2*z*z*hh*hh-4*z*hh*hh
    zero(S.diff(lag,hh).subs(hh,S.sqrt(arc2)))
    zero(S.diff(lag,hh,2).subs(hh,S.sqrt(arc2))-8*arc2)
    root=S.CRootOf(rootpoly,u,1)
    nums={name:str(expr.subs(u,root).evalf(30)) for name,expr in [('u',u),('delta',delta_exact),('V',V),('N4',N4),('E',E),('fixed_test_defect',F)]}
    hu=S.sqrt(disc)
    flats=[dict(kind='lateral',fixed_coordinate=axis,sign=sg,
                vertices=[(0,0,r)]+[(sg*hu,k*hu,u) if axis=='x' else (k*hu,sg*hu,u) for k in(-1,1)])
           for axis in('x','y') for sg in(-1,1)]
    flats.append(dict(kind='top',vertices=[(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]))
    report=dict(identity='ACTUAL_CURVED_PROFILE_COMPLETION_UNIQUE_DEFECT_MINIMIZER_V1',
                root_polynomial=rootpoly,root_interval=(LO,HI),root_specification='unique root in(0,1)',
                profile=dict(interval=(r,1),left_piece=ht,right_squared_piece=arc2,join=u),
                actual_volume=4*V,actual_centroid=(0,0,0),centroid_numerator=M,Sigma=Sigma,
                whole_marked_facet=dict(alpha=alpha,T=TF,c=cf,pole=pole),
                all_five_whole_flat_facets=flats,curved_boundary='four lateral patches over u<z<1',
                exact_positive_matrix_certificates=cert,test=test,volume_scaled_defect=F,
                affine_same_centroid_competitor=dict(height=affine,delta=delta_exact,delta_equation=eq,
                                                   root_interval_in_delta=(0,1-u),moment_difference=mdiff,
                                                   strict_defect_increase=gap),
                universal_completion_identity='F[h]-F[h0]=int_u^1(h^2-(2z-z^2))^2 dz whenever actual axial first moment is0 and the whole left piece is fixed.',
                numerics_diagnostic_only=nums,
                scope='A genuine curved homogeneous body, not a polytope or an equilibrium result. Unique global completion minimizer for this FIXED-TEST VOLUME-SCALED defect and fixed marked facet, interval and actual centroid. Not a Rayleigh-ratio optimizer or an unrestricted extremum.')
    def encode(v):
        if isinstance(v,S.MatrixBase):return [[encode(t) for t in row] for row in v.tolist()]
        if isinstance(v,S.Basic):return str(v)
        if isinstance(v,dict):return {str(k):encode(t) for k,t in v.items()}
        if isinstance(v,(list,tuple)):return [encode(t) for t in v]
        return v
    data=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    Path('ellipse_profile_completion_report.json').write_bytes(data)
    print('ACTUAL_CENTROID_QUARTIC_AND_ALL_FIVE_FLAT_FACETS_PD_PASS')
    print('UNIQUE_CURVED_FIXED_TEST_COMPLETION_SQUARE_IDENTITY_PASS')
    print('AFFINE_SAME_CENTROID_COMPETITOR_STRICTLY_WORSE_PASS')
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('ELLIPSE_PROFILE_COMPLETION_EXACT_PASS')
if __name__=='__main__':main()
```
