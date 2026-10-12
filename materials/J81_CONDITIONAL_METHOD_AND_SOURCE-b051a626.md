# material-b051a62697f6

AI research material

---

# J81 conditional spectral and local-response method

STATUS: new coordinator mathematics, NOT a Figure construction. Actual J80 derivation, branch prose and material-160/161 were unavailable. The incompatible notebook returned by the brief reader has not been adopted. Only the J80 quadratic expressions printed in state metadata motivated the following independent conditional lemmas. No new body or C reduction; accepted C622 unchanged.

## Gauge and exact closure

For Q_B[s]=integral(2s'^2-Ws^2)alpha^-4 and Q_J[s]=integral R s^2 alpha^-6, assume alpha>0 is C^2 and W,R bounded on a compact interval. Set z=s/alpha^2, a=alpha'/alpha, U=8a^2-4a'-W, r=R/alpha^2. Expansion gives

(2s'^2-Ws^2)alpha^-4=2z'^2+Uz^2+(4az^2)'.

Hence QB=integral(2z'^2+Uz^2), QJ=integral r z^2 when z vanishes at both endpoints. Otherwise keep [4az^2]. Application to actual constrained Hessians is NOT established by this gauge.

Let F(h)=0 be C^3 exact closure constraints. Choose correction directions T with A=DF(h0)T invertible. For DF(h0)s=0, implicit closure h(t)=h0+ts+T c(t) has c'(0)=0 and c''(0)=-A^-1 D^2F[s,s]. Thus the actual second derivative of response m is

Qhat_m[s]=D^2m[s,s]-Dm T A^-1 D^2F[s,s].

This correction need not be local or finite-rank as a quadratic form in s. Include DB[s]=DJ[s]=0 when seeking a purely second-order joint response; independent extra restrictions count in the codimension. A source using the t^2 coefficient rather than the Hessian must divide all terms consistently by two. The toy constraint F=y-x^2, m=y has raw x-Hessian 0 but closed Hessian 2.

IF exact closed-chart quantities satisfy B+gamma J=D with fixed D and nonzero constant gamma, then Qhat_B+gamma Qhat_J=0 and fixed B cannot change J. This is a conditional identity lemma, not an identification of the unavailable J79 symbols; reconcile its actual endpoint/normalization identity first.

## Cone criterion and exact continuation

On a finite admissible tangent span write ACTUAL corrected forms as c^T Bc,c^T Jc. If J is positive definite, attainable QB/QJ ratios are exactly the interval of generalized eigenvalues of (B,J): conjugation by J^-1/2 reduces the quotient to a weighted average of eigenvalues. Thus QB=0,QJ>0 requires lambda_min<=0<=lambda_max; a regular robust crossing has both signs. Negative QB with positive QJ is equivalent to lambda_min<0. Replace B by B-tau J for target ratio tau. Rank independence is insufficient: B=diag(1,2),J=I have independent forms but ratios only [1,2].

When two directions have zero cross terms in BOTH actual forms, put q_i=QJ[z_i]>0, lambda_i=QB[z_i]/q_i. For lambda_1<tau<lambda_2 and QJ=T0>0, use a^2=T0(lambda_2-tau)/(q_1(lambda_2-lambda_1)) and b^2=T0(tau-lambda_1)/(q_2(lambda_2-lambda_1)). Disjoint supports justify zero cross terms for local integral forms, not automatically after nonlocal closure corrections.

An exact local consequence: let a finite-dimensional C^3 parametrization Psi(u) impose F=0, and let first derivatives of B composed with Psi and J composed with Psi vanish at zero. Write H=B-tau J. If Qhat_H has a regular isotropic direction v(lambda0), with derivative in lambda nonzero and Qhat_J[v(lambda0)]>0, then K(t,lambda)=(H(Psi(t v(lambda)))-H(h0))/t^2 extends C^1 to t=0 with value Qhat_H[v(lambda)]/2. The implicit function theorem produces lambda(t) with Delta B=tau Delta J exactly and Delta J=t^2 Qhat_J[v(lambda0)]/2+O(t^3)>0. Positive definite J and indefinite B-tau J supply such a direction. This proves small-response continuation, not the finite amplitude or finite-edge realization needed by Figure.

## Width, codimension and exact moment-annihilating family

Assume the ACTUAL corrected form remains integral(2z'^2+Uz^2), r is bounded above and below by positive constants, and k continuous linear constraints are imposed on H_0^1(I), length L. If U>=-M, Poincare gives QB>=(2pi^2/L^2-M)integral z^2, so a negative direction requires ML^2>2pi^2. If U<=-m_depth, the first k+1 sine modes contain a nonzero constrained vector, giving sufficiency m_depth L^2>2pi^2(k+1)^2. Compact test approximations retain strict negativity and exact finite constraints can be restored: a dense linear subspace has the same image under a finite-dimensional continuous constraint map. More than k negative spectral directions likewise force a constrained negative direction. These statements do not count edges.

For p=u(1-u), 0<=u<=1, integers k>=0,m>=1 define z_(k,m)=D^k[p^(k+m)]. It has endpoint zeros of order at least m and integral u^j z_(k,m)=0 for j<k by integration by parts. Exact identity for all k,m:

integral z_(k,m)'^2 / integral z_(k,m)^2 = (2m/(2m-1))(2k+1)(2k+4m+1).

Proof: differentiating p g'-(k+m)p'g=0, g=p^(k+m), k+1 times gives pz''+(1-m)p'z'+lambda z=0, lambda=(k+1)(k+2m). Set A0=integral z^2, B0=integral z'^2,C0=integral pz'^2. Multiplication by z and then by p'z', with integration by parts and p''=-2,p'^2=1-4p, gives C0=(lambda-m)A0 and (1/2-m)B0+(4m-1)C0+lambda A0=0. Elimination proves the identity. Boundary terms vanish for m>=1.

For m=3, zero extension is C^2 with zero value and first two derivatives at endpoints. The quotient is (6/5)(2k+1)(2k+13), divided by L^2 after scaling. If transformed constraint weights are EXACT polynomials of degree <k, the moment constraints hold exactly and U<=-m_depth is sufficient for negativity when m_depth L^2>(12/5)(2k+1)(2k+13). Taylor approximations to actual centroid weights do not establish exact closure.

For k=0,m=3 the norm is 1/12012, derivative energy 1/770, quotient 78/5. One explicit two-jet bump is negative when m_depth L^2>156/5. With k arbitrary continuous linear constraints, instead use k+1 disjoint bumps of width L/(k+1) and a nonzero constraint-matrix kernel vector: locality gives sufficiency m_depth L^2>(156/5)(k+1)^2. Different hypotheses, no polyhedral edge bound.

## Recovery source and exact checks

Save the complete following block as verify_J81.py; run python verify_J81.py. Tested Python 3.13.5, SymPy 1.14.0. No external input, seeds, numerical quadrature or omitted helpers. Input source is 4450 bytes, SHA-256 1ef758589cc416f2b622a2e01bfcc402df9f01f2583296da48cc243b4ffc801a. Output J81_CHECKS.json is 764 bytes, SHA-256 bbebf3c40b5d417c37e99be9e493fbd766bab169b8dcbdcb8dd4a824d119d2d6. Terminal markers J81_EXACT_ALGEBRA_PASS and NOT_A_POLYHEDRON_CERTIFICATE.

```python
#!/usr/bin/env python3
"""Exact algebra checks for J81. No polyhedron is generated or certified.
Tested with Python 3.13.5 / SymPy 1.14.0. Run: python verify_J81.py
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import sympy as sp


def integral(poly: sp.Expr, u: sp.Symbol) -> sp.Rational:
    """Integrate an exact polynomial on [0,1], without numerical quadrature."""
    p = sp.Poly(sp.expand(poly), u, domain=sp.QQ)
    return sum((v / sp.Integer(d[0] + 1) for d, v in p.terms()), sp.Rational(0))


def bump(k: int, m: int, u: sp.Symbol) -> sp.Expr:
    if not isinstance(k, int) or not isinstance(m, int) or k < 0 or m < 1:
        raise ValueError("Expected integer k >= 0 and m >= 1")
    return sp.expand(sp.diff((u * (1-u)) ** (k+m), u, k))


def main() -> None:
    u = sp.Symbol("u", real=True)
    A, A1, A2, Z, Z1, W = sp.symbols("A A1 A2 Z Z1 W", nonzero=True)
    a = A1/A
    ap = A2/A - a*a
    raw = 2*(A*A*Z1 + 2*A*A1*Z)**2/A**4 - W*Z**2
    transformed = 2*Z1**2 + (8*a*a - 4*ap - W)*Z**2
    boundary_derivative = 4*ap*Z**2 + 8*a*Z*Z1
    assert sp.factor(raw - transformed - boundary_derivative) == 0

    pairs = 0
    ratios_m3 = []
    p = u*(1-u)
    for m in range(1, 5):
        for k in range(7):
            z = bump(k, m, u)
            zp = sp.diff(z, u)
            lam = (k+1)*(k+2*m)
            assert sp.expand(p*sp.diff(z,u,2) + (1-m)*(1-2*u)*zp + lam*z) == 0
            norm = integral(z*z, u)
            energy = integral(zp*zp, u)
            expected = sp.Rational(2*m,2*m-1)*(2*k+1)*(2*k+4*m+1)
            assert energy == expected*norm
            assert all(integral(u**j*z,u) == 0 for j in range(k))
            for derivative in range(m):
                zd = sp.diff(z,u,derivative)
                assert zd.subs(u,0) == zd.subs(u,1) == 0
            pairs += 1
            if m == 3:
                ratios_m3.append(str(expected))

    # Abstract potential test: U=-120, r=1 and the exact constraint integral(z)=0.
    # It is NOT a support function, centroid computation, or Figure certificate.
    z1, z2 = bump(1,3,u), bump(2,3,u)
    n1, n2 = integral(z1*z1,u), integral(z2*z2,u)
    b1 = integral(2*sp.diff(z1,u)**2-120*z1*z1,u)
    b2 = integral(2*sp.diff(z2,u)**2-120*z2*z2,u)
    assert integral(z1,u) == integral(z2,u) == 0
    assert integral(z1*z2,u) == 0
    assert integral(2*sp.diff(z1,u)*sp.diff(z2,u)-120*z1*z2,u) == 0
    assert b1/n1 == -12 and b2/n2 == 84
    c1sq, c2sq = sp.Rational(7,8)/n1, sp.Rational(1,8)/n2
    assert c1sq*n1+c2sq*n2 == 1
    assert c1sq*b1+c2sq*b2 == 0

    # Raw independence does not imply that B=0, J>0 is attainable.
    B, J = sp.diag(1,2), sp.eye(2)
    t = sp.Symbol("t")
    assert sp.factor((B-t*J).det()) == (t-2)*(t-1)

    # Curvature correction for F(x,y)=y-x^2=0, m(x,y)=y.
    x,y = sp.symbols("x y")
    F, objective = y-x*x, y
    tangent, corrector = sp.Matrix([1,0]), sp.Matrix([0,1])
    jac = sp.Matrix([[sp.diff(F,x), sp.diff(F,y)]]).subs({x:0,y:0})
    dm = sp.Matrix([[sp.diff(objective,x), sp.diff(objective,y)]])
    AF = (jac*corrector)[0]
    hF = (tangent.T*sp.hessian(F,(x,y))*tangent)[0]
    hm = (tangent.T*sp.hessian(objective,(x,y))*tangent)[0]
    corrected = hm - (dm*corrector)[0]*hF/AF
    assert hm == 0 and corrected == 2

    result = {
        "status": "J81_EXACT_ALGEBRA_PASS",
        "evidence_scope": "conditional algebra; not a polyhedron or equilibrium certificate",
        "sympy_version_tested": "1.14.0",
        "gauge_identity": True,
        "bump_pairs_checked": pairs,
        "m3_derivative_ratios_k0_to_k6": ratios_m3,
        "twojet_base_norm": "1/12012",
        "twojet_base_energy": "1/770",
        "abstract_mean_zero_example": {
            "potential_U": -120, "weight_r": 1,
            "generalized_eigenvalues": [-12,84],
            "coefficient_squares_for_QJ_1_QB_0": [str(c1sq),str(c2sq)]
        },
        "independence_counterexample_eigenvalues": [1,2],
        "curvature_example_raw_then_closed": [0,2]
    }
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).resolve().with_name("J81_CHECKS.json")
    path.write_text(output, encoding="utf-8")
    print("J81_EXACT_ALGEBRA_PASS")
    print("NOT_A_POLYHEDRON_CERTIFICATE")
    print(f"{path.name} bytes={len(output.encode('utf-8'))} sha256={hashlib.sha256(output.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
```

The script passed 28 exact polynomial-pair checks, gauge, endpoint/moment, counterexample and curvature checks. Its U=-120,r=1 example has the constraint integral z=0, directions z_(1,3),z_(2,3), zero mutual B/J cross terms, eigenvalue ratios -12 and 84, and coefficient squares 315315/32 and 51051/160 giving QJ=1,QB=0. This is an abstract functional example, not geometric input.

Next use: retrieve actual J80 and current branch memory; resolve J79 endpoint identity and normalization; compute actual nonlinear closure corrections; locate a positive-r patch and test its constrained spectrum. A strict crossing yields only an exact small response. Required amplitude, convexity, own centroid, finite E, strict equilibrium inequalities and absence of weak equilibria remain unproved. Label this material CONDITIONAL METHOD, never a Figure acceptance.
