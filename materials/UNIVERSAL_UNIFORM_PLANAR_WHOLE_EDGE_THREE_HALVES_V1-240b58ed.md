# material-240b58ed6bde

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Sharp universal three-halves theorem for uniform planar supports

## The theorem and its precise scope
Let K be ANY compact full-dimensional convex planar body with uniform area density and a genuine whole edge e. Let t be an inward affine coordinate with e={t=0}. Let g be the ACTUAL area centroid, Sigma the area covariance, and T the uniform edge second moment about that SAME g. Define alpha=(mean_K t) times the coarea length of e divided by Area(K). Then

    alpha T <= (3/2) Sigma.

The constant3/2 is sharp, attained in the normal direction of a rectangle. Thus for every affine test Y centred at the actual mean,

    R = J B2/(V I) <= 3/2,
    V=int_K 1, J=int_K t, I=int_K Y^2, Bj=int_e Y^j/|grad t|.

The weaker centred edge-centroid leverage follows by B1^2<=B0 B2. This theorem covers all convex planar supports, not just polygons, all numbers of vertices, all curved boundaries and all oblique test directions. It does NOT yet cover NONCONSTANT nonnegative affine density in the planar reduction. Accordingly the general actual uniform3D whole-facet inequality remains open. No U2 theorem, whole E17 exclusion or improved minimum is inferred. The separate accepted bracket is still34<=Cmin<=622.

Every actual uniform prism over an arbitrary convex planar base inherits the full lateral-facet matrix bound: its horizontal block is the theorem and its independent vertical block has ratio alpha<=2/3 by the two-dimensional endpoint-profile bound. For its two base facets the tangential ratio is1/2 and normal ratio3/2. Hence every facet of every affine image of such a prism satisfies the full3D covariance inequality. This prism corollary still does not cover arbitrary affine-height lifts.

## Dependencies and what is newly closed
The fully read literal planar parent is minimum-0290, SHA a1afff32561b16a73bf7a017e7ad3233330ac76bf67282f7cac952c02cc464a8. It supplies the general planar equivalence and the accepted normal3/2 theorem. The actual-centred variation is proved in [internal-source-reference]. Strong attainment and the pointwise finite-conic boundary theorem are proved in [internal-source-reference], SHA703e40d96d509e9d8ce54ea5ea74481e283d5c31250b4baaaeb489bbb94814b5. This material closes the ENTIRE constant-density case by a new one-wing reduction, two-edge stationarity and exact elimination. Its complete standalone algebra source has no external computational dependency.

The strong-attainment proof applies separately within the constant-density subclass: its symmetric constant-height lift remains a constant-height lift under the block-affine isotropization and Hausdorff limit used there. The common inner ball prevents its height from vanishing. Enlargement of a limiting marked segment to its whole edge increases B2. Thus a hypothetical strong uniform-planar supremum above3/2 is attained by an actual constant-density support. No separate attainment premise for the weaker ratio is required.

## 1. The actual first variation at a hypothetical supercritical maximizer
Assume a maximum R>3/2 exists. Normal tests are already bounded, so t,Y are independent affine coordinates. For fixed whole e and a signed change of area away from e,

    delta log R = int Phi d(delta area)+O(||delta area||^2),
    Phi=t/J-1/V-Y^2/I-2 eta Y/V, eta=B1/B2.

The moving centroid term is included. Put h=J/V. The finite-conic result gives at most THREE straight boundary edges, including e; every other boundary point lies on the SAME parabola

    t=f(Y)=h+(J/I)Y^2+(2J eta/V)Y.

Every positive-density straight edge other than e must be incident to an endpoint of e. This is a local variational statement over all convex supports, not a vertex bound on arbitrary counterexamples. Completing the square and the endpoint-mass bound alpha<=3/4 give min f>h/2>0 at R>3/2. The sharper planar alpha<=2/3 is available but unnecessary here.

If the support is polygonal, at most three edges are possible. A uniform triangle satisfies alpha=2/3 and T=2 Sigma, hence alpha T=(4/3)Sigma. For example an affine normalization to vertices (0,-1),(0,1),(1,u) verifies these identities directly about g=(1/3,u/3). Therefore a supercritical maximizer must have a nonempty parabolic arc.

## 2. Why exactly one curved wing remains for constant density
Write the marked edge in the raw affine y coordinate as t=0, a0<=y<=b0, and write f(y)=m+A(y-c)^2 with A>0,m>0. At any smooth point y of a parabolic boundary arc, its tangent line is supporting and below the whole marked edge. If y>=c, the tangent at b0 satisfies

    m+A(y-c)^2+2A(y-c)(b0-y)<=0,

forcing y>b0; if y<c the analogous test at a0 forces y<a0. Thus every curved arc lies strictly outside the projection interval of the marked edge.

The upper t-boundary as a function of y is concave, so it cannot contain an open arc of this strictly convex parabola. It is consequently made of straight edges. If the support projection extended beyond both ends of [a0,b0], both marked endpoints would be on the lower boundary at interior projection coordinates. No upper edge could then be incident to an endpoint of e, contrary to the edge-incidence rule. Thus there is only one wing, after reflection the right wing. A support with no projection extension cannot contain any parabolic arc and was already excluded.

The leftmost upper endpoint must equal the left endpoint of e: an extra vertical edge there would leave the adjoining upper edge with both endpoints off e. The upper graph is one line from that left endpoint to the far right point. On the lower boundary there is e, then at most one straight stem incident to its right endpoint, then one continuous arc of f to the far point. Additional lower straight segments would have both endpoints off e; disconnected arcs without such a segment would be one arc of the same parabola. A vertical stem at an interior y-coordinate is impossible because a convex lower graph is continuous there.

Normalize the marked edge to -1<=y<=1 and the far point to(t,y)=(1,1+d), d>0. The support therefore has upper boundary

    U(y)=(y+1)/(d+2),

and lower boundary0 on[-1,1], a straight line on[1,1+dz], and one quadratic arc on[1+dz,1+d]. Here0<z<1: the arc is nonempty and min f>0 prevents it from meeting the marked edge directly. Write the stem t=L(y-1)/d, with0<L<1. This is an exact extremizer classification within the constant-density subclass, not an assumed model for arbitrary bodies.

## 3. A tangent stem cannot be a maximizer
If the stem is tangent to f at its joining point P, then on its open interior

    Phi=(stem-f)/J=-(A/J)(y-y_P)^2<0.

Rotate the stem slightly upwards about(0,1), keeping the marked edge fixed, and join it to the unchanged parabola at the new right intersection. The new lower graph is convex, since that intersection lies beyond the new tangency point; it remains below U for a sufficiently small rotation. This removes a positive-area thin region over the original stem, where Phi<0, while the small additional change near P has higher order because Phi(P)=0. The actual first variation is strictly positive. This contradicts maximality.

Thus the stem meets the parabola transversely with a positive derivative jump. The upper line also meets it transversely: an upper supporting chord cannot be tangent to the strictly convex parabola while lying above a nonempty arc. Both lines can now be independently rotated by either sign about their respective fixed marked endpoints, leaving the same genuine whole e and an admissible convex support.

## 4. The two exact line-rotation conditions
Write the raw-coordinate parabola as

    f(y)=A(y^2+2B y+C), A>0.

Along any line from a marked endpoint y0 to a point y1 on f, the function J Phi=line-f is quadratic, equals-f(y0) at y0 and0 at y1. Rotating that line about its marked endpoint has velocity proportional to y-y0. Its first variation vanishes exactly when

    f(y0) = A(y1-y0)^2/2.

For the upper line and stem respectively this gives

    f(-1)=A(d+2)^2/2,
    f(1)=A d^2 z^2/2.

Together with f(1+d)=1 and f(1+dz)=Lz, these identities force

    B=-[(d+2)^2-d^2 z^2]/8,
    C=[(d+2)^2+d^2 z^2]/4-1,
    A=4/[d(d+2)(d z^2-d+2)],
    L=[d^2 z^2-d^2+6dz-4d+4]/[(d+2)(d z^2-d+2)].

All denominators are nonzero at a genuine supercritical extremizer: A is positive and the actual support has positive area. The source checks all four identities exactly. In the earlier four-parameter stem notation the conditions also imply v=2(1-z)/(2-z), strictly between0 and1. No separate numerical assumption about that parameter is used.

## 5. Actual centroid and curvature cannot be self-consistent
Integrate this exact candidate support with density1. Put

    V=int1, Jt=int t, Jy=int y, Kyy=int y^2,
    I=Kyy-Jy^2/V, gy=Jy/V.

Since the parabola must be the first-variation zero set, its curvature and linear coefficient must satisfy

    A I-Jt=0,
    B(V^2/3+Jy^2)+Jy(V/3+Kyy)=0.

The second identity uses the ACTUAL centroid: on the fixed uniform edge[-1,1], eta=-gy/(1/3+gy^2), and B=-gy+eta I/V. Omitting this re-centring relation would invalidate the elimination.

The standalone source integrates the actual three-piece support, reduces these two rational expressions, and computes the resultant of their numerators with respect to d. It is

    10995116277760000 (z-1)^22 (z^3-3z-1)
    * (2z^5-5z^4-10z^3+15z^2+15z+3) * P22(z).

The degree22 polynomial P22 is generated literally in the exact report; the complete generator below is its smallest recovery representation. In Bernstein form on[0,1], its23 coefficients are ALL strictly negative, with minimum-6328125 and maximum-27. The cubic has Bernstein coefficients(-1,-2,-3,-3), all negative. The quintic has coefficients(3,6,21/2,31/2,19,20), all positive. The remaining factor z-1 is strictly negative for0<z<1. Therefore this resultant NEVER vanishes at any admissible joining parameter. The two necessary actual-moment equations cannot both hold, even over complex d at such a real z. We do not infer real-root exclusion from a numerical resultant sample.

This contradiction excludes every hypothetical supercritical maximum. Strong attainment then proves the universal uniform-planar bound. Rectangles attain3/2 in the normal direction, so the constant is sharp. Equality is not otherwise classified by this argument.

## Complete exact recovery and execution
Save the source below as uniform_planar_universal.py, LF newlines and one final newline. Python3.13.5, SymPy1.14.0, assertions enabled; no external input, seed, precision or checkpoint. Both reconstruction and verification are:

    python -B uniform_planar_universal.py

Expected marker: UNIFORM_PLANAR_THREE_HALVES_EXACT_ELIMINATION_PASS.
Input2492B SHA256999f1864bce7cf9f8fb558d9884d76dd89250c809c2dbdb270393418be728a43.
Output uniform_planar_universal_report.json3466B SHA2569f6a92130a8b3448a97a5df084666a1f1129a37b445948c6625e04a65c6c2caa.
Normal and fresh source-only runs BOTH completed and produced byte-identical reports. An initial report-serialization failure was corrected by converting SymPy integer metadata to Python integers; no mathematical assertion had failed. The source below is the final executed version. This is an analytical proof with exact symbolic elimination, not proof-assistant certification.

## Complete source uniform_planar_universal.py

```python
"""Exact elimination certificate for the universal uniform-planar 3/2 bound.
Standalone actual stem-wing moments and two-edge stationarity. The geometric
attainment/cap/one-wing proof accompanies this source; algebra alone is not
polygonal localization. Python3.13.5 SymPy1.14.0. No inputs. Assertions required.
"""
import sympy as s,json,hashlib
from pathlib import Path
d,z,y=s.symbols('d z y',positive=True)
B=-((d+2)**2-d**2*z**2)/8;C=((d+2)**2+d**2*z**2)/4-1
A=4/(d*(d+2)*(d*z*z-d+2))
L=(d*d*z*z-d*d+6*d*z-4*d+4)/((d+2)*(d*z*z-d+2))
f=A*(y*y+2*B*y+C);U=(y+1)/(d+2);line=L*(y-1)/d
assert s.factor(f.subs(y,1+d)-1)==0
assert s.factor(f.subs(y,1+d*z)-L*z)==0
assert s.factor(f.subs(y,-1)-A*(d+2)**2/2)==0
assert s.factor(f.subs(y,1)-A*(d*z)**2/2)==0

def integ(p,lo,hi):
    P=s.Poly(s.expand(p),y)
    return s.factor(sum(c*(hi**(i+1)-lo**(i+1))/s.Integer(i+1) for (i,),c in P.terms()))

def mom(i,j):
    return s.factor((integ(y**j*U**(i+1),-1,1+d)-integ(y**j*line**(i+1),1,1+d*z)-integ(y**j*f**(i+1),1+d*z,1+d))/s.Integer(i+1))
V=mom(0,0);Jt=mom(1,0);Jy=mom(0,1);Kyy=mom(0,2)
I=s.factor(Kyy-Jy*Jy/V)
P=s.factor(A*I-Jt)
Q=s.factor(B*(V*V/3+Jy*Jy)+Jy*(V/3+Kyy))
p,pden=s.fraction(P);q,qden=s.fraction(Q)
res=s.factor(s.resultant(p,q,d))
constant,factors=s.factor_list(res,z)
assert constant!=0
records=[]
for fac,power in factors:
    poly=s.Poly(fac,z);n=poly.degree()
    controls=[s.factor(sum(poly.nth(j)*s.binomial(i,j)/s.binomial(n,j) for j in range(i+1))) for i in range(n+1)]
    if n==1 and s.factor(fac-(z-1))==0:
        sign='strict_negative_on_open_interval'
        assert power==22 and controls==[-1,0]
    else:
        assert all(c>0 for c in controls) or all(c<0 for c in controls)
        sign='positive' if controls[0]>0 else 'negative'
    records.append({'factor':str(fac),'multiplicity':int(power),'degree':int(n),'bernstein_controls':list(map(str,controls)),'sign_on_0_1':sign})
assert sorted(r['degree'] for r in records)==[1,3,5,22]
report={'identity':'UNIFORM_PLANAR_WHOLE_EDGE_THREE_HALVES_ELIMINATION_V1','volume':str(V),'first_t':str(Jt),'first_y':str(Jy),'second_y':str(Kyy),'curvature_residual':str(P),'centering_residual':str(Q),'resultant':str(res),'constant':str(constant),'factor_certificates':records}
b=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode();Path(__file__).with_name('uniform_planar_universal_report.json').write_bytes(b)
print('UNIFORM_PLANAR_THREE_HALVES_EXACT_ELIMINATION_PASS',len(b),hashlib.sha256(b).hexdigest(),flush=True)
```
