# material-2a0e881ded61

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# MORSE6 reversed-skew finite terminal points — exact construction resource, NOT a polyhedron

This is a self-contained exact continuation from MORSE6_RATIONAL_A7_100 and the terminal-edge formula proved in immutable result figure-0500 (SHA628f77cad0ad9de768f16dbaf232b8d0b68852fcd00e848696417f026f6d9f5b). It preserves all literal P/Q/B coefficients needed here. The full smooth-body proof remains materials [internal-source-reference] and [internal-source-reference]; this module does not recertify global convexity.

Exact evaluated terminal data: p1=-3384507/6250000, q0=2794981/10000000, h1=-13551/12500. At smooth centre0 the maximizing skew for fixed infinitesimal X is gamma*=-2794981/4650000; F(gamma*,0)=1758400598420927/4650000000000000>0. A simpler gamma=-3/5 gives F(gamma,1/10)=6271868760739/50000000000000>0. Thus the positive terminal cone is genuinely nonempty for this literal MORSE6 parent, not merely an unevaluated condition.

The source produces five exact rational surface points. At t=1/100,1/50,1/20 their direct physical incoming scores (v-(0,c,0))·(U-v) are strictly positive for EVERY c≤1/10, because Y<U and the score decreases with c. At t=1/10 and1/5 the score at c=1/10 is negative: the infinitesimal criterion alone does not license those coarser terminal steps. These latter two are failed controls for the stated uniform bound, NOT exclusions at every actual centre. All points are exact boundary points by the implicit-circle identity. Reflection gives the paired points. No full polyhedron, finite mass bound, unique equilibrium claim, edge count or exact finite mechanics result is asserted.

Recovery: save the following entire code block as morse6_skew.py, UTF-8/LF with a final newline. It is2552bytes,SHA256 dde3d7cb908c28b1f4acb1e8a6a803c67e053aa0ed4c0be98974a2be8b93a40a. Run `python -B -S morse6_skew.py` (CPython3.13.5 standard library observed). Output MORSE6_SKEW_EXACT.json3595bytes,SHA256 f87bcba8235de2a389916d337f0fe1db2f7ff6fd71944f12f2f1cc84db53158f. Observed markers MORSE6_THREE_POSITIVE_TWO_COARSE_SKEW_POINTS_PASS and UNIFORM_INCOMING_FOR_ACTUAL_AXIAL_CENTROID_C_LE_1_10. The source fully reconstructs all literal point coordinates and rational scores; no originating sandbox is needed.

```python
"""Exact finite terminal points for MORSE6; NOT a complete polyhedron.
Source inputs: immutable MORSE6_RATIONAL_A7_100 P/Q/B and CW56 terminal formula.
Python >=3.10 standard library. Run python -B -S morse6_skew.py.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
A=F(7,100);L=F(1029667,1000000);U=F(107,100)
P=[A,A*F(-7736016,10**6),F(62596542623293333606272461,134072992002035843625000000),A*F(-11309209,10**6),A*F(49285282,10**6),A*F(-72918101,10**6),A*F(33874704,10**6)]
Q=[A*F(k,10**6) for k in [3992830,-9033836,7320751,-36032083,88425030,-81073624,27231889]]
B=[F(1),F(-42040,10**6),F(19011,10**6),F(-150151,10**6)]
GAMMA=F(-3,5);CENTRE_BOUND=F(1,10)
def val(p,x):
 r=F(0)
 for a in p[::-1]:r=r*x+a
 return r
def point(t):
 t=F(t);x=2*t/(1+t*t);y=x*x;rho=(1-t*t)*val(B,y)/(1+t*t);s=GAMMA*t
 e1=(1-s*s)/(1+s*s);e2=2*s/(1+s*s)
 v=[L*x,val(P,y)+rho*e1,x*val(Q,y)+rho*e2]
 assert (v[1]-val(P,y))**2+(v[2]-x*val(Q,y))**2==(1-y)*val(B,y)**2
 return v
def leading(g,c):
 R=U-c;p1=P[1];q0=Q[0];h1=2*B[1]-1
 return (R-2)*g*g-4*q0*g-R*(2*p1+h1)-2*L*L-2*q0*q0
def pack(z):
 if isinstance(z,F):return str(z)
 if isinstance(z,dict):return {k:pack(v) for k,v in z.items()}
 if isinstance(z,list):return [pack(v) for v in z]
 return z
def main():
 h1=2*B[1]-1;q0=Q[0];p1=P[1];gstar=-2*q0/F(93,100)
 curvature=(q0*q0-2*p1-h1)/(L*L)
 rows=[]
 for t in [F(1,100),F(1,50),F(1,20),F(1,10),F(1,5)]:
  v=point(t);score=(v[1]-CENTRE_BOUND)*(U-v[1])-v[0]**2-v[2]**2
  assert U>v[1]
  assert (score>0)==(t<=F(1,20))
  rows.append({'t':t,'point':v,'score_at_c_bound':score,'uniform_positive_for_c_le_bound':score>0})
 assert leading(GAMMA,CENTRE_BOUND)>0
 data={'object':'MORSE6_REVERSED_SKEW_TERMINAL_POINTS','status':'exact surface points and sufficient incoming-edge inequalities, not a polyhedron',
       'P':P,'Q':Q,'B':B,'lambda':L,'gamma':GAMMA,'centre_upper_bound':CENTRE_BOUND,
       'K':[[curvature,-q0/L],[-q0/L,F(1)]],'gamma_star_at_zero':gstar,
       'F_star_at_zero':leading(gstar,F(0)),'F_at_gamma_and_c_bound':leading(GAMMA,CENTRE_BOUND),'rows':rows}
 raw=(json.dumps(pack(data),sort_keys=True,separators=(',',':'))+'\n').encode()
 Path('MORSE6_SKEW_EXACT.json').write_bytes(raw)
 print('MORSE6_THREE_POSITIVE_TWO_COARSE_SKEW_POINTS_PASS')
 print('UNIFORM_INCOMING_FOR_ACTUAL_AXIAL_CENTROID_C_LE_1_10')
 print('MORSE6_SKEW_EXACT.json',len(raw),hashlib.sha256(raw).hexdigest())
 print('SOURCE',len(Path(__file__).read_bytes()),hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':main()
```
