# material-e7daf31f7ddd

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# FINITE_HEIGHT_RECIPROCAL_DOMAIN_V1

## Scope and exact dependencies
Coordinator-derived necessary-condition theorem, not a V10/E17/F9 exclusion or attaining construction. The accepted interval remains 34 <= C_min <= 622. The shadow-chain theorem below is independent of centroid assumptions. Its homogeneous-body corollary uses the accepted covariance containment lemma in [internal-source-reference] (SHA256 4f0c333687903feecee35b55d4e4ab9d9982a71e5c339e26a128b4f148cf8ecfd6): whitening the own volume covariance gives sqrt(5/3) B contained in K contained in sqrt(15) B. The reciprocal convex-hull corollary uses [internal-source-reference] (SHA256 a3559464d478c6a8d4e837b75031623542f94e59fe27456a8fc40ff9d28503d6d7eb). Both complete sources were read. No new polyhedron is claimed.

## 1. Sharp finite shadow-chain estimate
Let e be a Euclidean unit vector. Suppose nonzero vectors z_0,...,z_d satisfy e dot z_0=0 and z_j dot z_{j-1} >= ||z_j||^2 for 1<=j<=d, d>=1. Then

|e dot z_d| <= b_d ||z_0||,    b_d = cos(pi/[2(d+1)])^(d+1).

Proof. Put theta_j=angle(z_j,z_{j-1}); the hypothesis gives 0<=theta_j<pi/2 and ||z_j||<=||z_{j-1}|| cos(theta_j). Put Theta=angle(z_d,z_0). Spherical triangle inequality and concavity of log cos give

||z_d|| <= ||z_0|| product_j cos(theta_j) <= ||z_0|| cos(Theta/d)^d.

Indeed Theta<=sum theta_j, their average is less than pi/2, and cos is decreasing there. Since e is perpendicular to z_0, |e dot z_d|<=||z_d|| sin(Theta). On 0<=Theta<=pi with Theta<d*pi/2, the maximum of sin(Theta) cos(Theta/d)^d occurs at Theta=d*pi/[2(d+1)]: below pi/2 its logarithmic derivative is cot(Theta)-tan(Theta/d), and above pi/2 it is negative. The maximum is b_d. The bound is sharp for a planar chain of equal angular steps pi/[2(d+1)] whose lengths decrease by the common cosine. The b_d increase with d: the derivative of t log cos(pi/[2t]) is log cos(x)+x tan(x)>0, x=pi/[2t], since this expression vanishes at x=0 and has derivative x sec(x)^2>0.

## 2. A one-root escape tree controls the top spectral gap
Let Q be a convex three-polyhedron with r B contained in Q contained in R B, r>0. Let H be positive definite with eigenvalues lambda_1>=lambda_2>=lambda_3>0. Suppose each vertex other than a designated root U has a true-edge successor w with v^T H(w-v)>=0, and these successors form a rooted tree of maximum depth h. Then

lambda_1/lambda_2 <= (R/r)^2 cos(pi/[2(h+1)])^(2(h+1)).       (FH)

The conclusion is non-strict; no equality classification is assumed.

Proof. Choose a unit lambda_1 eigenvector e with e dot U>=0. As r B is contained in Q, some vertex v has e dot v<=-r. Follow its successors toward U and let y be the first point of the resulting polygonal path in e dot y=0. If necessary y truncates its last edge. The segment preceding y begins at a negative vertex u and satisfies u^T H(y-u)>=0, since it is a nonnegative multiple of the full escape arrow. In particular y cannot be zero. Reverse the truncated path from y back to v and transform all points by H^(1/2). This gives a chain of section 1 with d<=h, whose initial point remains perpendicular to e. Thus

r sqrt(lambda_1) <= |e dot H^(1/2)v| <= b_d ||H^(1/2)y|| <= b_h R sqrt(lambda_2).

The last inequality uses y in Q, ||y||<=R and y perpendicular to e. Squaring proves (FH).

Exactly one unstable vertex with no other weak unstable vertices supplies such a tree: every other vertex has a nonnegative escape along a true edge. Along each escape,

w^T H w-v^T H v = 2 v^T H(w-v)+(w-v)^T H(w-v)>0.

Choosing one escape per non-root therefore yields no directed cycle, so all paths end at the unique root and h<=V-1. The lemma also applies whenever an eligible one-root tree is known directly. No saddle condition is used.

## 3. Own-centroid homogeneous corollary and polarity
Let P be a homogeneous three-polyhedron at its own volume centroid 0 with covariance M positive definite. K=M^(-1/2)P has uniform covariance I and physical squared distance x^T H x with H=M. The accepted containment lemma gives R/r=3. Hence one unstable vertex implies

lambda_1(H)/lambda_2(H) <= 9 cos(pi/[2V])^(2V).

The polar K* has (1/R) B contained in K* contained in (1/r) B, so its containment ratio is also 3. For a true facet y dot x<=1 of K, the H-orthogonal support projection is p=H^(-1)y/(y^T H^(-1)y). It is stable exactly when the polar vertex y is unstable under H^(-1): all adjacent polar vertices y' satisfy y^T H^(-1)(y'-y)<0. Weak cases use the corresponding non-strict inequalities. One stable facet without additional weak stable facets therefore supplies a one-root polar escape tree, of depth at most F-1. Applying (FH) to K* and H^(-1) gives

lambda_2(H)/lambda_3(H) <= 9 cos(pi/[2F])^(2F).

The polar need not have centroid 0 or covariance I. Only its inherited radial containment ratio is used. Actual primal and polar tree depths h_p,h_d can replace V-1,F-1.

For V=10,F=9, the exact rational verifier below proves

lambda_1/lambda_2 < p=7024915/1000000,
lambda_2/lambda_3 < q=6832329/1000000,
lambda_1/lambda_3 < p*q=9599306095407/200000000000 < 48.

Here 48-p*q=693904593/200000000000>0. Strict rational inequalities follow because p and q strictly exceed the analytic cosine bounds, not from an unproved strict form of (FH).

## 4. Stronger exact coupled reciprocal domain
Put A=H/tr(H), B=H^(-1)/tr(H^(-1)), k=281/40. As p<k and q<k, the reciprocal-pair theorem cited above gives

A+B < (80561/91801) I,
k A+B > (90201/91801) I,
A+k B > (90201/91801) I,
tr(A)=tr(B)=1,

in the strict Loewner order. Here k^2+k+1=91801/1600. Each of A,B also lies strictly between (1600/91801) I and (78961/91801) I. These are joint necessary conditions, stronger than the k=9 domain. Convexifying reciprocal pairs does not impose AB proportional to I, whole-facet realization, or the own-centroid equations. Thus this result neither closes C=34 nor advances the upper construction bound.

The asymmetric p,q bounds do not by themselves justify identifying their full joint convex hull with the single orbit of diag(pq,p,1) and its normalized inverse. That unequal-bound analogue requires a separate argument and is not asserted here.

## 5. Complete executable recovery
The sole Python block is the full source of verify_finite_height.py, including a final LF: 2746 bytes, SHA256 9c3d332329913930f610449ae0ad03a24c9c9bc7d6eefb17d26c024ac587382c.

Reconstruct from this exact material saved as SOURCE.md:
python3 -c 'from pathlib import Path; t=Path("SOURCE.md").read_text(); s=t.split("```python\n",1)[1].split("```",1)[0]; Path("verify_finite_height.py").write_text(s)'

Verify:
python3 verify_finite_height.py > finite_height_verification.txt

Python >=3.8, standard library only. No external input, random seed, omitted helper or non-default numerical parameter. Arithmetic is exact rational. Machin's identity follows by tangent addition with the first-quadrant angle; alternating arctangent sums bound pi. On (0,1), the degree-eight alternating cosine sum is an upper bound and cosine decreases, so its value at a lower argument remains an upper bound.

Expected terminal marker: FINITE_HEIGHT_RECIPROCAL_DOMAIN_V1 PASS.
Output finite_height_verification.txt: 662 bytes, SHA256 b54a0974cb740c10062dcb77e199385e45ca019f77d284570af4ee3ad77b8694. The coordinator ran this executable successfully before preservation. It certifies the rational constants, not the analytic geometry proof or a construction.

```python
#!/usr/bin/env python3
"""Exact rational arithmetic for FINITE_HEIGHT_RECIPROCAL_DOMAIN_V1.
Run: python3 verify_finite_height.py
Python >=3.8; standard library only. No external input or random choices.
The analytic shadow-chain and polar arguments are in the accompanying proof.
"""
from fractions import Fraction as F
from math import factorial
import json


def atan_interval(inv: int, terms: int = 30):
    """Consecutive alternating-series sums enclose atan(1/inv)."""
    if inv < 2 or terms < 1:
        raise ValueError("inv >= 2 and terms >= 1 required")
    x = F(1, inv)
    s = sum(((-1)**j * x**(2*j + 1) / (2*j + 1)
             for j in range(terms)), F(0))
    t = s + (-1)**terms * x**(2*terms + 1) / (2*terms + 1)
    return min(s, t), max(s, t)


def cosine_upper(x: F) -> F:
    """Degree-eight alternating Taylor upper bound on cos(x), 0<x<1."""
    if not F(0) < x < F(1):
        raise ValueError("0 < x < 1 required")
    return sum(((-1)**j * x**(2*j) / factorial(2*j)
                for j in range(5)), F(0))


def main():
    lo5, hi5 = atan_interval(5)
    lo239, hi239 = atan_interval(239)
    # Machin identity pi = 16 atan(1/5) - 4 atan(1/239).
    pi_lo, pi_hi = 16*lo5 - 4*hi239, 16*hi5 - 4*lo239
    decimal_lo = F(3141592653589793, 10**15)
    decimal_hi = F(3141592653589794, 10**15)
    assert decimal_lo < pi_lo < pi_hi < decimal_hi
    p, q = F(7024915, 10**6), F(6832329, 10**6)
    # Since cos is decreasing on (0,1), a lower pi bound supplies an upper cos bound.
    exact_upper10 = 9 * cosine_upper(decimal_lo / 20)**20
    exact_upper9 = 9 * cosine_upper(decimal_lo / 18)**18
    assert exact_upper10 < p and exact_upper9 < q
    assert p*q == F(9599306095407, 200000000000)
    assert 48-p*q == F(693904593, 200000000000) > 0
    k = F(281, 40)
    assert p < k and q < k
    d = k*k + k + 1
    c, a = (k*k+1)/d, k*(k+1)/d
    assert d == F(91801, 1600)
    assert c == F(80561, 91801)
    assert a == F(90201, 91801)
    assert 1/d == F(1600, 91801)
    assert k*k/d == F(78961, 91801)
    print(json.dumps({
        "object": "FINITE_HEIGHT_RECIPROCAL_DOMAIN_V1",
        "pi_decimal_bracket": [str(decimal_lo), str(decimal_hi)],
        "gap_lambda1_lambda2_strict_upper": str(p),
        "gap_lambda2_lambda3_strict_upper": str(q),
        "condition_number_strict_upper": str(p*q),
        "48_minus_condition_upper": str(48-p*q),
        "common_kappa": str(k),
        "pair_sum_upper": str(c),
        "weighted_pair_lower": str(a),
        "individual_eigenvalue_lower": str(1/d),
        "individual_eigenvalue_upper": str(k*k/d),
        "exact_checks": "PASS"
    }, sort_keys=True, indent=2))
    print("FINITE_HEIGHT_RECIPROCAL_DOMAIN_V1 PASS")


if __name__ == "__main__":
    main()
```
