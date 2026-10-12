# material-e2120a3d88bf

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# UNEQUAL_RECIPROCAL_CURVED_BOUNDARY_V1
## Recovery capsule part2/2: complete runnable source

The proof is [internal-source-reference]. Save the following fence as unequal_reciprocal.py with its final LF. Source4583bytes SHA256d7922332fa9bd5b44e9946c44e3ab264b14e1c0fcf3a2121d6a391d91fea9fad. Python>=3.10 standard library, assertions enabled, no external input. Run python -B -S unequal_reciprocal.py build then python -B -S unequal_reciprocal.py check. Reconstructed unequal_reciprocal.json1018bytes SHA25629dd4d9efcd9d77c0ff1d8dd00028a6d17da681b09f961891ab928279c0e3b18. Both commands were executed by the coordinator. Expected terminal line: UNEQUAL_RECIPROCAL_CURVED_BOUNDARY_PASS 1018 29dd4d9efcd9d77c0ff1d8dd00028a6d17da681b09f961891ab928279c0e3b18.

```python
#!/usr/bin/env python3
"""Exact controls for UNEQUAL_RECIPROCAL_CURVED_BOUNDARY_V1.
Python >=3.10, standard library only, assertions enabled. No external inputs.
Run: python -B -S unequal_reciprocal.py build | check
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import sys

P_CAP = F(7024915, 10**6)
Q_CAP = F(6832329, 10**6)


def spectrum(r, s):
    if r < 1 or s < 1:
        raise ValueError('ordered adjacent ratios must be at least one')
    a = [r*s/(r*s+s+1), s/(r*s+s+1), 1/(r*s+s+1)]
    b = [1/(r*s+r+1), r/(r*s+r+1), r*s/(r*s+r+1)]
    assert sum(a) == sum(b) == 1
    assert a[0]*b[0] == a[1]*b[1] == a[2]*b[2]
    return a, b


def endpoint_z(p, q, r, s):
    a, b = spectrum(r, s)
    d, e = p*q+q+1, p*q+p+1
    return [(d*x+q*e*y-q*(p+1))/((q-1)*(p*q-1))
            for x, y in zip(a, b)]


def tangent(q, t):
    p0, q0 = q*t+q+1, q*t+t+1
    beta = q*q0*q0/(p0*p0)
    c = t*q/p0+beta/q0
    assert 1-c == (q*q+q+1)/(p0*p0)
    return beta, c


def corner_gap_numerator(p, q, t):
    d, e = p*q+q+1, p*q+p+1
    p0, q0 = q*t+q+1, q*t+t+1
    return q*e*p0*p0+p*q*d*q0*q0-d*e*q*(q*t*t+2*q*t+2*t+1)


def report():
    p, q = P_CAP, Q_CAP
    assert p > q > 4
    t0 = (p+q)/2
    # One-orbit separation identity, including the actual strict-ratio control.
    for pp, qq in [(F(3), F(2)), (F(9), F(2)), (p, q)]:
        rr = (pp+qq)/2
        z = endpoint_z(pp, qq, rr, qq)[0]
        expected = -qq*(pp-qq)**2*(qq+1)/((qq-1)*(pp*qq-1)
                    *(pp*qq+qq*qq+2*qq+2)
                    *(pp*qq+pp+qq*qq+qq+2))
        assert z == expected < 0
        assert endpoint_z(pp, qq, pp, qq) == [0, 0, 1]
    strict_s = q-F(1, 10**6)
    strict_z = endpoint_z(p, q, t0, strict_s)[0]
    assert 1 < t0 < p and 1 < strict_s < q and strict_z < 0

    # N(t) is explicitly quadratic. These are its degree-two Bernstein
    # coefficients on [t0,p], without sampling as a feasibility substitute.
    n0 = corner_gap_numerator(p, q, t0)
    n2 = corner_gap_numerator(p, q, p)
    nm = corner_gap_numerator(p, q, (t0+p)/2)
    n1 = 2*nm-(n0+n2)/2
    bernstein = [n0, n1, n2]
    assert all(v > 0 for v in bernstein)
    for u in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
        tt = t0+(p-t0)*u
        assert corner_gap_numerator(p, q, tt) == n0*(1-u)**2+2*n1*u*(1-u)+n2*u*u

    # Tangent equality and the complete rational square identity on s=q.
    beta, c = tangent(q, t0)
    assert beta > 4 and 0 < c < 1
    for rr in [F(1), q, t0, p]:
        a, b = spectrum(rr, q)
        lhs = a[0]+beta*b[0]-c
        rhs = q*(q+1)*(rr-t0)**2*(q*q+q+1)/((q*rr+q+1)
                *(q*rr+rr+1)*(q*t0+q+1)**2)
        assert lhs == rhs >= 0
    a0, b0 = spectrum(t0, q)
    assert a0[0]+beta*b0[0] == c
    assert all(a0[j]+beta*b0[j] > c for j in [1, 2])
    a1, b1 = spectrum(p, q)
    assert all(a1[j]+beta*b1[j] > c for j in range(3))

    # The old equal-gap hull remains strictly larger: its genuine endpoint
    # pair fails this new valid asymmetric-domain inequality.
    k = F(281, 40)
    ak, bk = spectrum(k, k)
    old_gap = ak[1]+beta*bk[1]-c
    assert old_gap < 0
    # Move strictly into that old hull, keeping a negative new functional.
    eps = F(1, 10**7)
    ai = [(1-eps)*v+eps/3 for v in ak]
    bi = [(1-eps)*v+eps/3 for v in bk]
    assert ai[1]+beta*bi[1]-c < 0
    d = k*k+k+1
    for x, y in zip(ai, bi):
        assert x+y < (k*k+1)/d
        assert k*x+y > k*(k+1)/d
        assert x+k*y > k*(k+1)/d
    return {
        'object': 'UNEQUAL_RECIPROCAL_CURVED_BOUNDARY_V1',
        'p': str(p), 'q': str(q), 't_interval': [str(t0), str(p)],
        'strict_control_s': str(strict_s), 'strict_control_z1': str(strict_z),
        'corner_gap_Bernstein_coefficients': list(map(str, bernstein)),
        'tangent_beta_at_midpoint': str(beta), 'tangent_c_at_midpoint': str(c),
        'old_equal_hull_gap': str(old_gap),
        'old_equal_hull_strict_interior_epsilon': str(eps),
        'checks': 'PASS'
    }


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ('build', 'check'):
        raise SystemExit('usage: unequal_reciprocal.py build | check')
    data = (json.dumps(report(), sort_keys=True, indent=2)+'\n').encode()
    path = Path('unequal_reciprocal.json')
    if sys.argv[1] == 'build':
        path.write_bytes(data)
    elif path.read_bytes() != data:
        raise AssertionError('saved report differs from exact reconstruction')
    print('UNEQUAL_RECIPROCAL_CURVED_BOUNDARY_PASS',len(data),sha256(data).hexdigest())


if __name__ == '__main__':
    main()
```
