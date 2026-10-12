# material-d9418ad83e60

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# RECIPROCAL_EXTREME_COUPLING_V1

Coordinator analytical continuation AFTER dispatching the genuine heptagon–triangle residual. This gives a SHARP nonlinear eigenvalue inequality and an explicit robust forbidden region for normalized reciprocal sums, not just an isolated countercontrol. It is a matrix-domain result, NOT a new actual polyhedron, E17 exclusion, canonical type subtraction, or attaining construction. Bounds34<=C_min<=622 remain unchanged.

## 1. Sharp theorem
Let A be real symmetric positive definite3x3,trA=1, B=A^-1/tr(A^-1), and S=A+B. Here S is a MATRIX sum, not stable-equilibrium count. Suppose BOTH ordered consecutive eigenvalue ratios of A are<=k, k>1. Put c_k=3k/(k^2+4k+1). Then
 lambda_max(S)+c_k lambda_min(S)<=1.             (1)
The coefficient c_k is the LARGEST possible with the right side fixed at1. Equality holds exactly when A is proportional, up to orthogonal conjugacy, to diag(k,1,1) or its reciprocal diag(1,k,k). If both adjacent ratios are strictly<k, (1) is STRICT.

In the ACTUAL covariance gauge with joint stable count S_eq=1 and U=1, the accepted covariance theorem supplies strict ratio9. Consequently
 118lambda_max(S)+27lambda_min(S)<118.           (2)
This specialization is not U1-only. The preconditioner C must be the actual covariance (or a legitimately equivalent gauge), not an arbitrary optimized preconditioner relabelled as covariance.

## 2. Complete elementary proof
Inverting the normalized pair swaps its two adjacent ratios without changing S. Therefore choose the member whose larger gap comes first and rescale its raw spectrum to(rt,t,1), with1<=t<=r<=k. Let
 P=rt+t+1, Q=rt+r+1,
 a=rt/P+1/Q, b=1/P+rt/Q, c=t/P+r/Q.
These are the three eigenvalues of S in this raw-spectrum basis. Exact differences are
 a-b=(r-t)(rt-1)/(PQ)>=0,
 b-c=(t-1)(r^2 t-1)/(PQ)>=0.
Thus a=lambda_max(S), c=lambda_min(S). No guess about which physical eigendirection is largest is used.

Set D=r^2 t+rt^2+2rt+r+t>0 and f(r)=3r/(r^2+4r+1). Direct algebra gives the ENTIRE rational identity
 (1-a)/c = r(t^2+t+1)/D
 = f(r)+r(t-1)^2(r^2+r+1)/[(r^2+4r+1)D].        (3)
Also
 f(r)-f(k)=3(k-r)(kr-1)/[(r^2+4r+1)(k^2+4k+1)]>=0. (4)
Equations(3)(4) imply (1-a)/c>=f(k), which is(1). For k>1 equality forces r=k and t=1. Conversely that raw spectrum gives equality, establishing sharpness of c_k and the stated equality family. With r<k the difference in(4) is positive, including r=1, so (1) is strict. These are exact positive rational identities on the whole domain, not numerical optimization.

This theorem can also be regarded as the supporting tangent at the lower-double-eigenvalue boundary of NORMALIZED_RECIPROCAL_SUM_FIBERS_V1 (complete prior proof [internal-source-reference]/source [internal-source-reference]), but the proof above is independent and complete. It avoids the nested radicals in the exact fibre ratio while being only NECESSARY, not sufficient, away from its sharp equality stratum.

## 3. A full forbidden region, with an exact quantitative margin
Take S0=diag(9/10,11/20,11/20). It satisfies0<S0<I,trS0=2 and the weaker sum-hull cap S0<82I/91. Indeed A_rel=B_rel=S0/2 even lies strictly inside the exact PAIR hull and commutes. Nevertheless
 lambda_max(S0)+(27/118)lambda_min(S0)-1=61/2360>0.
Thus it violates(1) for k9. This independently proves the no-ratio9-lift result of the prior fibre theorem without reconstructing its radical eigenvalues.

For ANY real symmetric S with ||S-S0||_op<=1/50, the variational definitions of the largest and smallest eigenvalues give
 lambda_max(S)>=9/10-1/50,
 lambda_min(S)>=11/20-1/50.
Hence
 lambda_max(S)+(27/118)lambda_min(S)-1
 >=61/2360-(1+27/118)/50=3/2360>0.                (5)
Consequently the ENTIRE CLOSED operator-norm ball of radius1/50 around S0 contains NO sum of a normalized reciprocal pair with adjacent ratios<=9. In particular this excludes its trace2 SPD slice. Orthogonal conjugates of this ball satisfy the same conclusion. It is not merely an isolated or eigenvalue-degenerate obstruction.

The exact positive-radius threshold furnished by this Lipschitz estimate is61/2900: any strictly smaller radius gives a positive uniform margin. No optimal distance-to-the-physical-set claim is made. At the endpoint the estimate gives zero only, so the stated strictly positive certified ball uses1/50.

The inequality is NONLINEAR as a matrix-domain condition: lambda_min is involved along with lambda_max. It does not contradict the exact pair convex-hull theorem and cannot serve as a new unconditional affine separator. Geometry must still force the normalized sum into such a region. No actual true-arrow packet has yet been shown to do so.

## 4. Reproduction and evidence level
Save the complete code fence below as reciprocal_extreme_coupling.py, UTF8/LF with final newline. It needs Python>=3.11 and SymPy1.14.0; no input files, RNG, optimization package or network. The author executed CPython3.13.5 with assertions enabled:
 python -B reciprocal_extreme_coupling.py build
 python -B reciprocal_extreme_coupling.py check
Both printed
 RECIPROCAL_EXTREME_COUPLING_EXACT_PASS 423 67930ac9570c3dad4561a8976385f0b967c862ce62cbf42ef1a30c0e6b09df3a
Pins:
 reciprocal_extreme_coupling.py1876bytes SHAe6ed574e89bdb12649cea0afbc19a38abf63c107ce09c0d1e9a06281dfdb148f;
 reciprocal_extreme_coupling.json423bytes SHA67930ac9570c3dad4561a8976385f0b967c862ce62cbf42ef1a30c0e6b09df3a.
Six whole symbolic identities and all exact rational margins are checked. The analytical ordering, positivity, sharpness and variational eigenvalue argument above prove the continuum claims. No independent second-authored replay or proof-assistant formalization is claimed. The exploratory identities used to find the theorem are all included in this runnable source.

```python
#!/usr/bin/env python3
"""Exact identities for RECIPROCAL_EXTREME_COUPLING_V1.
Python >=3.11 and SymPy1.14.0; no input data or network.
python -B reciprocal_extreme_coupling.py build|check
"""
import hashlib,json,sys
from pathlib import Path
import sympy as s
assert __debug__ and sys.version_info>=(3,11) and s.__version__=='1.14.0'
R=s.Rational

def calculation():
 r,t,k=s.symbols('r t k',positive=True)
 P=(r+1)*t+1;Q=r*(t+1)+1
 a=r*t/P+1/Q;b=1/P+r*t/Q;c=t/P+r/Q
 assert s.factor(a-b-(r-t)*(r*t-1)/(P*Q))==0
 assert s.factor(b-c-(t-1)*(r*r*t-1)/(P*Q))==0
 den=r*r*t+r*t*t+2*r*t+r+t
 f=lambda z:3*z/(z*z+4*z+1)
 assert s.factor((1-a)/c-r*(t*t+t+1)/den)==0
 rem=r*(t-1)**2*(r*r+r+1)/((r*r+4*r+1)*den)
 assert s.factor((1-a)/c-f(r)-rem)==0
 assert s.factor(f(r)-f(k)-3*(k-r)*(k*r-1)/((r*r+4*r+1)*(k*k+4*k+1)))==0
 assert s.factor(a.subs(t,1)+f(r)*c.subs(t,1)-1)==0
 gap=R(9,10)+R(27,118)*R(11,20)-1
 tube=gap-(1+R(27,118))*R(1,50)
 assert gap==R(61,2360) and tube==R(3,2360)
 assert gap/(1+R(27,118))==R(61,2900)
 return dict(identity='RECIPROCAL_EXTREME_COUPLING_V1',whole_symbolic_identities=6,
  sharp_coefficient='3*k/(k**2+4*k+1)',ratio9_coefficient='27/118',
  formal_sum=['9/10','11/20','11/20'],formal_gap=str(gap),
  closed_operator_norm_radius='1/50',uniform_rejection_margin=str(tube),
  maximal_radius_from_this_Lipschitz_estimate='61/2900',
  scope='Analytic spectral necessary condition; no actual polyhedron or E17 exclusion.')

def main():
 if sys.argv[1:] not in (['build'],['check']):raise SystemExit('usage: build|check')
 data=(json.dumps(calculation(),sort_keys=True,separators=(',',':'))+'\n').encode()
 path=Path(__file__).with_suffix('.json')
 if sys.argv[1]=='build':path.write_bytes(data)
 else:assert path.read_bytes()==data
 print('RECIPROCAL_EXTREME_COUPLING_EXACT_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
```
