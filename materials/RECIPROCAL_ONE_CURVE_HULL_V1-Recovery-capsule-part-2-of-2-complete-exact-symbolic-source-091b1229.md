# material-091b1229065b

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# RECIPROCAL_ONE_CURVE_HULL_V1
## Recovery capsule part2/2: complete exact source

Part1 is [internal-source-reference],16913bytes,SHAa2edffd255ed78ef4751b92a40b40468fe5dde1809262244340ade836ffae779. Deliver both parts for computational continuation. All inputs are literal in this source; no older recovery files are required.

Save the following entire fenced source as reciprocal_frontier.py, UTF-8/LF with its final newline. Source3798bytes,SHA256d67f33c69b3bb307329e704ec599dae3ed2cb08a2e2fc31adb75c382f881ae6d. Python>=3.10,SymPy1.14.0. Author CPython3.13.5/SymPy1.14.0 executed both commands:

 python -B reciprocal_frontier.py build .
 python -B reciprocal_frontier.py check .

Expected identical terminal marker:
 RECIPROCAL_FRONTIER_EXACT_PASS 2741 7aca43abb79f656a99dfec0b302e66d2e9ec5cb2b2a26815554fb93f1e3111a1

Reproduced report reciprocal_frontier.json2741bytes,SHA2567aca43abb79f656a99dfec0b302e66d2e9ec5cb2b2a26815554fb93f1e3111a1. This computes27 entire symbolic Bernstein entries, their reconstructed polynomials and every shifted rational coefficient sign. No numerical grid or random parameters are used.

```python
#!/usr/bin/env python3
"""Exact algebra for RECIPROCAL_ONE_CURVE_HULL_V1.
Python >=3.10, SymPy 1.14.0. No external data, numerical sampling, or random seed.
Usage: python -B reciprocal_frontier.py build|check [output-directory]
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import sys
import sympy as s


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def compute() -> dict:
    p, q, t, x, u, v = s.symbols('p q t x u v')
    P, Q = p*t+t+1, p*t+p+1
    Pc, Qc = p*q+q+1, p*q+p+1
    C = s.Matrix([[p*q, q, 1], [1, p, p*q], [1, 1, 1]])
    require(s.expand(C.det()+(p-1)*(q-1)*(p*q-1))==0, 'corner determinant')
    a, b = [p*t/P,t/P,1/P], [1/Q,p/Q,p*t/Q]
    rows = [C.inv()*s.Matrix([Pc*a[i],Qc*b[i],1]) for i in range(3)]
    W = s.Matrix(3,3,lambda i,j:s.factor(rows[i][j]))
    for i in range(3):
        require(s.cancel(sum(W[i,j] for j in range(3))-1)==0,'row sum')
        require(s.cancel(sum(W[j,i] for j in range(3))-1)==0,'column sum')
    denominators = [
      [(p-1)*(p*q-1)*P*Q,(p-1)*(q-1)*P*Q,(q-1)*(p*q-1)*P*Q],
      [(p-1)*(p*q-1)*P*Q,(p-1)*(q-1)*P*Q,(q-1)*(p*q-1)*P*Q],
      [(p-1)*(p*q-1)*P*Q,(p-1)*(q-1)*P*Q,(q-1)*(p*q-1)*P*Q]]
    coefficients=[]
    positive_terms=[]
    for i in range(3):
        for j in range(3):
            n=s.cancel(W[i,j]*denominators[i][j])
            require(s.denom(n)==1,'polynomial numerator')
            pol=s.Poly(s.expand(n.subs(t,1+(q-1)*x)),x)
            require(pol.degree()<=2,'quadratic numerator')
            powers=[pol.nth(k) for k in range(3)]
            bern=[s.factor(sum(powers[k]*s.Rational(s.binomial(h,k),s.binomial(2,k)) for k in range(h+1))) for h in range(3)]
            rebuilt=sum(bern[h]*s.binomial(2,h)*x**h*(1-x)**(2-h) for h in range(3))
            require(s.expand(rebuilt-pol.as_expr())==0,'Bernstein identity')
            for h,beta in enumerate(bern):
                expansion=s.Poly(s.expand(beta.subs({p:2+v+u,q:2+v},simultaneous=True)),u,v)
                require(all(c>=0 for c in expansion.coeffs()),f'negative coefficient {i}{j}/{h}')
                positive_terms.append(sum(bool(c>0) for c in expansion.coeffs()))
                coefficients.append([i,j,h,str(beta)])
    # Explicit failure below the theorem's q>=2 hypothesis.
    bad=s.factor(W[0,2].subs({p:2,q:s.Rational(6,5),t:1}))
    require(bad<0,'q<2 control')
    # Strict-saddle multiplier A+B<I: exact scalar equivalence.
    aa,bb,cc=s.symbols('a b c',positive=True)
    multiplier=1-aa/(aa+bb+cc)-bb*cc/(aa*bb+aa*cc+bb*cc)
    expected=aa*(bb*bb+bb*cc+cc*cc)/((aa+bb+cc)*(aa*bb+aa*cc+bb*cc))
    require(s.cancel(multiplier-expected)==0,'strict-saddle positive multiplier')
    return {'theorem':'RECIPROCAL_ONE_CURVE_HULL_V1',
            'hypotheses':'real Sym3; p>=q>=2; r<=p,t<=q',
            'corner_determinant':str(s.factor(C.det())),
            'bernstein_coefficients':coefficients,
            'nonnegative_shift_coefficient_counts':positive_terms,
            'q_below_two_negative_weight':str(bad),
            'proof_scope':'27 exact polynomial identities and coefficient signs; no body exclusion'}


def main() -> None:
    if len(sys.argv) not in (2,3) or sys.argv[1] not in ('build','check'):
        raise SystemExit(__doc__)
    out=Path(sys.argv[2] if len(sys.argv)==3 else '.')
    out.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(compute(),ensure_ascii=True,sort_keys=True,indent=2)+'\n').encode('utf-8')
    path=out/'reciprocal_frontier.json'
    if sys.argv[1]=='build':
        path.write_bytes(raw)
    else:
        require(path.read_bytes()==raw,'report mismatch')
    print('RECIPROCAL_FRONTIER_EXACT_PASS',len(raw),hashlib.sha256(raw).hexdigest())

if __name__=='__main__':
    main()
```
