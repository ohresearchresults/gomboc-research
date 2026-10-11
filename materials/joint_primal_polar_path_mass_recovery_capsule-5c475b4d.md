# material-5c475b4df1a0

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Joint primal-polar path envelopes and exact uniform-mass obstruction

## Status and scope
This is a newly derived necessary condition and two exact envelope counterexamples, NOT a new polyhedron, not a110 construction, and not an exclusion of all C<500 bodies. The physical body is uniformly filled and centred at its actual volume centroid. Its polar is taken about that same centre; no polar-own-mass assumption is used. The elementary positive-path argument was already preserved in [internal-source-reference]. The present capsule gives a self-contained proof of the additional joint mass constraint and the full runnable exact computation, without requiring that earlier file.

## 1. Positive paths and containing balls
For a physical vertex path p_0=v,...,p_j=a consisting of true positive ascent edges, p_i dot(p_{i+1}-p_i)>0. Therefore ||p_{i+1}||^2-||p_i||^2>||p_{i+1}-p_i||^2. Summing and applying Cauchy gives ||a-v||^2<j(||a||^2-||v||^2). If all non-root vertices have such a path with j<=k, then K is contained in B(a/(k+1), k||a||/(k+1)). Every non-root vertex is strictly inside that ball. The root a is on its boundary. The containment extends to all material points by convexity. A weak-free U1 polytope admits such paths: every other vertex has some positive true-edge escape and squared radius strictly increases, so a path cannot cycle and ends at the unique unstable vertex. The same assertion applies to the same-centre polar Q=K° when K is weak-free S1. No unproved choice of a mass reference is involved.
For an orthogonal symmetry fixing the actual centre, an ascent path cannot visit two vertices in the same orbit, because all vertices in one orbit have equal norm. With m physical orbits one can take k=m-1, and with n polar orbits l=n-1.

## 2. Opposite roots give an outer ball and an inner ellipsoid
Assume the unique physical unstable vertex is a=R e_z and the unique polar unstable vertex is b=-e_z/r, where R,r>0. Thus the physical unique stable face has outward normal -e_z and support distance r. Suppose positive physical/polar paths require at most k,l edges, respectively, with k,l>1.
The physical path bound gives the outer ball B with centre R/(k+1)e_z and radius kR/(k+1).
The polar path bound gives Q contained in the ball with centre b/(l+1) and radius l||b||/(l+1). Polarity reverses inclusion. Consequently K contains the ellipsoid E={x: l||x||-z <= (l+1)r}.
Its centre is r/(l-1)e_z, its axial semiaxis is lr/(l-1), and its two transverse semiaxes are r sqrt((l+1)/(l-1)). Its axial extent is [-r,(l+1)r/(l-1)]. These signs are important: the compulsory ellipsoid is shifted TOWARD the physical top. More generally for stable outward unit normal n the centre is -rn/(l-1), with the same semiaxes parallel/perpendicular to n.

## 3. Actual mass imposes a condition beyond E subset B
For any uniformly filled K satisfying E subset K subset B,
integral_K z dV >= integral_{E intersect {z>0}} z dV + integral_{B intersect {z<0}} z dV.
Indeed the positive compulsory material cannot be removed, and the whole negative half-ball is the largest available source of negative first moment. For a finite polytope the displayed inequality is strict: a curved open portion of the negative spherical cap is absent from K, and z<0 there. In the path setting all negative-cap points are separated from the sole ball contact at the positive root.
Direct section integration gives
-integral_{B,z<0} z dV / pi = R^4 N_k, N_k=(k-1)^3(3k+1)/(12(k+1)^4),
integral_{E,z>0} z dV / pi = r^4 P_l, P_l=(l+1)^4(3l-1)/(12 l^2(l-1)^3).
The actual centroid is zero, so a necessary condition is
(R/r)^4 > Q(k,l)=P_l/N_k
=(k+1)^4(l+1)^4(3l-1)/[l^2(k-1)^3(3k+1)(l-1)^3].
This is not sufficient for any polyhedron or equilibrium signature. It does not prove that the convex set satisfying the moment budget exists. It is an additional obstruction even when E strictly fits inside B.
For nonopposite root directions, the general necessary test remains available: for every unit u, integral_{E,u dot x>0}(u dot x)dV + integral_{B,u dot x<0}(u dot x)dV <=0. The closed rational opposite-root formula above must not be transferred to arbitrary root angles, in particular not to the broken-symmetry C92 affine entrance.

## 4. Exact strict-containment but impossible-mass examples
Normalize r=1. Since the ellipsoid's largest semiaxis is l/(l-1), a sufficient strict containment certificate is
kR/(k+1) - |1/(l-1)-R/(k+1)| - l/(l-1) >0.
For k=l=10, R=13/10, that margin is 7/110, while the compulsory-positive-minus-available-negative first moment divided by pi is 151107676469/1280794680000 >0.
For k=l=62, R=21/20, the margin is 1/60, while the corresponding positive moment gap divided by pi is 183752908107773/33923381800320000 >0.
Hence in each example the inner ellipsoid strictly fits the outer ball, but NO uniformly filled measurable set between those envelopes has zero centroid. These are envelope/mass counterexamples, not polyhedral constructions or equilibrium audits.

## 5. Exact C2/E249 consequence
Assume an orthogonal half-turn about z, a sole axial top vertex, a full opposite horizontal base facet, and weak-free own strict110. The actual centroid is axial. The base is necessarily stable, and the sole unstable vertex is the axial top. All other vertices and facets occur in two-element orbits: the only fixed vertex is the top, and the only fixed facet is the base. Thus V=2k+1, F=2l+1 and E=2(k+l). With E<=249, E is actually <=248 and k+l<=124. The elementary minimum degrees of the primal and dual graphs give k<=2l-2 and l<=2k-2. In particular k,l>=2 and each is at most82.
An exhaustive EXACT rational comparison over all2461 admissible integer pairs shows a UNIQUE minimum of Q(k,l) at k=l=62:
Q_min=45908819349491385/37034287661168908.
Consequently every body in this explicitly scoped family with E<=249 and own weak-free110 must satisfy R/r > Q_min^(1/4), and r/R < Q_min^(-1/4).
The exact enclosures at denominator10^12 are:
105517145051/100000000000 <= Q_min^(1/4) < 1055171450511/1000000000000,
473856641741/500000000000 <= Q_min^(-1/4) < 947713283483/1000000000000.
Thus r/R<0.947713283483 is a convenient strict necessary bound. This excludes near-spherical candidates in the stated finite C2 budget but leaves the known MASS/MORSE6-style entrances far from excluded. The earlier axial cone argument separately gives r/R>=1/3; the two conditions leave a broad interval. Neither condition solves existence.

## 6. Recovery and verification
No external inputs, random seed, numerical library or nondefault parameter is needed for the exact certificate. Save the complete code below as joint_path_mass.py with UTF-8 LF line endings. Runtime used: CPython3.13.5; only standard-library fractions, hashlib and json are required (Python>=3.10).
Reconstruction and verification command: python -B -S joint_path_mass.py
The command checks the cap-integral identities over82x82=6724 pairs, two strict geometric/mass examples, and all2461 C2 graph-budget pairs, then writes JOINT_PATH_MASS.json.
Expected source: joint_path_mass.py,5191 bytes,SHA256 6899e4e189196731c876aa2e8b06883b7746dbe3f4ae1d9e96c4a8c43e502f3c.
Expected output: JOINT_PATH_MASS.json,2164 bytes,SHA256 ce6cc99a2e6a2a639b813b4927a7efc60fe6db594613e6f9ab7598a395ed8e54f.
Expected terminal marker: JOINT_PATH_MASS_EXACT_PASS 2164 ce6cc99a2e6a2a639b813b4927a7efc60fe6db594613e6f9ab7598a395ed8e54f
The hash identifies exact bytes; the complete source below reconstructs every output. The mathematical proof, not a transport or hashing receipt, establishes the scoped theorem.

## Complete joint_path_mass.py
```python
#!/usr/bin/env python3
"""Exact necessary mass gate from primal/polar path balls. Python >=3.10.
No inputs, randomness, numerical packages, or external files.
"""
from fractions import Fraction as F
import hashlib
import json


def primitive(t: F, c: F, h: F, multiplier: F) -> F:
    """Integral of t*multiplier*(1-((t-c)/h)**2)."""
    return multiplier * (t*t/F(2) -
        (t**4/F(4) - F(2)*c*t**3/F(3) + c*c*t*t/F(2))/(h*h))


def cap_moment(c: F, h: F, multiplier: F, positive: bool) -> F:
    """First moment divided by pi; multiplier is section area/pi at centre."""
    lo = max(F(0), c-h) if positive else c-h
    hi = c+h if positive else min(F(0), c+h)
    return F(0) if lo >= hi else primitive(hi,c,h,multiplier)-primitive(lo,c,h,multiplier)


def coefficients(k: int, l: int) -> tuple[F,F]:
    if k <= 1 or l <= 1:
        raise ValueError('path bounds must exceed one')
    negative_ball = F((k-1)**3*(3*k+1),12*(k+1)**4)
    positive_ellipsoid = F((l+1)**4*(3*l-1),12*l*l*(l-1)**3)
    return negative_ball, positive_ellipsoid


def fourth_root_interval(q: F, denominator: int=10**12) -> tuple[F,F]:
    """Integer-bisection enclosure, no binary floating-point dependence."""
    if q <= 0 or denominator <= 0:
        raise ValueError('positive arguments required')
    low, high = 0, denominator
    while F(high,denominator)**4 <= q:
        high *= 2
    while high-low > 1:
        middle=(low+high)//2
        if F(middle,denominator)**4 <= q:
            low=middle
        else:
            high=middle
    assert F(low,denominator)**4 <= q < F(high,denominator)**4
    return F(low,denominator),F(high,denominator)


def main() -> None:
    # Independent section-antiderivative checks of both closed coefficients.
    checked=0
    for k in range(2,84):
        c=F(1,k+1);rho=F(k,k+1)
        got_ball=-cap_moment(c,rho,rho*rho,False)
        total_ball=primitive(c+rho,c,rho,rho*rho)-primitive(c-rho,c,rho,rho*rho)
        assert total_ball==F(4,3)*rho**3*c
        for l in range(2,84):
            d=F(1,l-1);a=F(l,l-1);b2=F(l+1,l-1)
            got_ellipse=cap_moment(d,a,b2,True)
            total_ellipse=primitive(d+a,d,a,b2)-primitive(d-a,d,a,b2)
            assert total_ellipse==F(4,3)*a*b2*d
            neg,pos=coefficients(k,l)
            assert neg==got_ball and pos==got_ellipse
            checked+=1
    assert checked==6724

    witnesses=[]
    for k,l,R in [(10,10,F(13,10)),(62,62,F(21,20))]:
        # r=1. The axial ellipsoid semiaxis is the largest one, so
        # |centre_E-centre_B|+a < radius_B rigorously implies E subset int(B).
        c=R/F(k+1);rho=R*F(k,k+1)
        d=F(1,l-1);a=F(l,l-1)
        containment_margin=rho-abs(d-c)-a
        neg,pos=coefficients(k,l)
        moment_gap=pos-R**4*neg
        assert containment_margin>0 and moment_gap>0
        witnesses.append(dict(k=k,l=l,R_over_r=str(R),
            strict_containment_margin=str(containment_margin),
            compulsory_positive_minus_available_negative_over_pi=str(moment_gap),
            status='ellipsoid strictly fits outer ball, but no zero-centroid filled set between them'))

    # Orthogonal C2 with one axial top vertex and one full horizontal base:
    # V=2k+1,F=2l+1,E=2(k+l). Primal/dual degree bounds give the two inequalities.
    candidates=[]
    for k in range(2,125):
        for l in range(2,125):
            if k+l<=124 and k<=2*l-2 and l<=2*k-2:
                neg,pos=coefficients(k,l)
                candidates.append((pos/neg,k,l))
    assert len(candidates)==2461
    optimum=min(candidates)
    q,k,l=optimum
    assert (k,l)==(62,62)
    assert sum(t[0]==q for t in candidates)==1
    report=dict(
        theorem='necessary own-volume-centroid gate for opposite roots and finite positive-path bounds; not a110 construction',
        exact_coefficient_checks=checked,
        formulas=dict(N_k='(k-1)^3*(3*k+1)/(12*(k+1)^4)',
                      P_l='(l+1)^4*(3*l-1)/(12*l^2*(l-1)^3)',
                      strict_necessary='(R/r)^4 > P_l/N_k'),
        witnesses=witnesses,
        C2_E249=dict(
            assumptions='one axial top vertex, full opposite horizontal base, orthogonal half-turn, uniform actual centroid, strict110 and no additional weak equilibria',
            identity='V=2k+1,F=2l+1,E=2(k+l)<=248',
            constraints='k,l>=2;k+l<=124;k<=2*l-2;l<=2*k-2',
            enumerated_pairs=len(candidates),unique_minimizer=[k,l],
            necessary_R_over_r_fourth_gt=str(q),
            lower_threshold_R_over_r_enclosure=[str(x) for x in fourth_root_interval(q)],
            upper_threshold_r_over_R_enclosure=[str(x) for x in fourth_root_interval(1/q)]),
        limits='Does not exclude all C2 shapes; does not apply the opposite-root formula to broken-symmetry C92. Envelopes and mass are necessary only; no existence or weak-edge conclusion follows.')
    payload=(json.dumps(report,indent=2,sort_keys=True)+'\n').encode()
    open('JOINT_PATH_MASS.json','wb').write(payload)
    print('JOINT_PATH_MASS_EXACT_PASS',len(payload),hashlib.sha256(payload).hexdigest())

if __name__=='__main__':
    main()
```
