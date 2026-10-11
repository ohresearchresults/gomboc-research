# material-c8bc45599c4d

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

"""TILTED_ROOT_UNIFORM_ENDPOINT_GAP_V1: new rational algebra only.
CPython 3.13.5; standard library; assertions must be enabled.
Run: python -S tilt_gap_exact.py > tilt_gap_exact.json
Geometric inputs are the complete accepted results
minimum-0082 (f1793b348240dce32e3de0ca3e06e50e64942c2561980cb2dc1c75bb9b6b636c)
and minimum-0083 (3e86de882ea208c90af36b6583bb49754e528559555e8db9ce7efe04cd37020d).
No random input, external files, floating arithmetic, or optimizer.
"""
from fractions import Fraction as F
from math import comb
import json
assert __debug__

def const(x):
    return {(0,0):F(x)} if x else {}
def var(i):
    e=[0,0];e[i]=1
    return {tuple(e):F(1)}
def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items():out[e]=out.get(e,F(0))+c
    return {e:c for e,c in out.items() if c}
def scale(p,c):
    return {e:a*c for e,a in p.items() if a*c}
def mul(p,q):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            g=tuple(e[i]+f[i] for i in range(2))
            out[g]=out.get(g,F(0))+a*b
    return {e:c for e,c in out.items() if c}
def power(p,n):
    out=const(1)
    for _ in range(n):out=mul(out,p)
    return out
def sub(p,q):return add(p,scale(q,-1))
def evaluate(p,t,v):return sum(c*t**i*v**j for (i,j),c in p.items())
def shifted_t_coefficients(p):
    out={}
    for (i,j),a in p.items():
        assert j==0
        for k in range(i+1):out[k]=out.get(k,F(0))+a*comb(i,k)
    return [out.get(i,F(0)) for i in range(max(out)+1)]
def rows(p):return [[i,j,p[i,j]] for i,j in sorted(p)]

def run():
    tau=F(51,25);sigma=F(65,32);cap=F(10,9);upper=F(45,7)
    lam=sigma-cap
    t,v=var(0),var(1);one=const(1);a=add(const(2),v)
    # sigma^2*t*Phi at rho=a/(sigma*t), with all denominators cleared.
    first=scale(mul(add(scale(t,3*sigma),a),
                    add(scale(t,4*sigma),mul(a,add(t,one)))),lam)
    inner=sub(mul(add(t,one),add(scale(t,3*sigma),a,
                     scale(mul(power(t,2),sub(const(3),a)),cap*sigma))),
              scale(power(t,2),4*cap*sigma))
    cleared=sub(first,scale(mul(a,inner),sigma))
    P0=add(scale(power(t,3),-676000),scale(power(t,2),4388475),
           scale(t,-223680),const(-327680))
    P1=add(scale(power(t,3),338000),scale(power(t,2),1190800),
           scale(t,-275680),const(-327680))
    P2=scale(mul(add(t,one),sub(scale(power(t,2),4225),const(1024))),80)
    assert scale(cleared,73728)==add(P0,mul(v,P1),mul(power(v,2),P2))
    ends=[evaluate(P0,F(1),F(0)),evaluate(P0,upper,F(0))]
    assert ends==[F(3161115),F(524485,343)] and min(ends)>0
    # t^4*(P0/t^2)'' = 2*c1*t+6*c0 < 0 for t>=1.
    concavity=add(scale(t,2*P0[1,0]),const(6*P0[0,0]))
    assert concavity==scale(add(scale(t,233),const(1024)),-1920)
    shifted=shifted_t_coefficients(P1)
    assert shifted==list(map(F,[925440,3119920,2204800,338000]))
    assert min(shifted)>0 and F(65)-32>0
    rho_derivative_lower=[10*lam-6,13*lam-3,3*lam]
    assert rho_derivative_lower==[F(461,144),F(2581,288),F(265,96)]
    assert min(rho_derivative_lower)>0
    def trace_coefficient(k,t):
        return k*(5*t-2)-(k+3-2/t)*tau*t/3
    slope=5*sigma-tau*(sigma+3)/3
    assert slope>0
    maximum=trace_coefficient(sigma,upper)
    threshold=(tau-sigma)/maximum
    assert maximum==F(113663,2800) and threshold==F(49,227326)
    endpoint_max=trace_coefficient(F(2),upper)
    endpoint_threshold=(tau-2)/endpoint_max
    assert endpoint_max==F(6963,175) and endpoint_threshold==F(7,6963)
    assert threshold>F(1,4640) and endpoint_threshold>F(1,995)
    # Earlier, weaker strips follow but are not the final constant.
    assert threshold>F(35,177683)>F(63,407992)
    # Negative control: this scalar upper bound cannot itself prove cap 2.
    tt=upper;pp=F(1);qq=F(-4,25)
    U=cap+(3-pp)*((tt+1)*(3-qq+cap*tt*pp)-4*cap*tt)/(tt*(3-qq)*(4-qq*(tt+1)))
    beta2=3-pp+2*tt*qq
    assert U==F(108740,53799)>2 and beta2==F(-2,35)<0
    return {
      'identity':'TILTED_ROOT_UNIFORM_ENDPOINT_GAP_V1',
      'terminal':'COMPACT_EQUAL_CAP_65_32_AND_TILT_GAPS_EXACT_PASS',
      'parameters':{'tau':tau,'sigma':sigma,'single_facet_cap':cap,'t_max':upper},
      'polynomials':{'P0':rows(P0),'P1':rows(P1),'P2':rows(P2)},
      'P0_endpoints':ends,'P1_shifted_coefficients':shifted,
      'rho_derivative_lower_coefficients':rho_derivative_lower,
      'transfer_max':maximum,'uniform_endpoint_gap':threshold,
      'endpoint_dominant_transfer_max':endpoint_max,
      'endpoint_dominant_gap':endpoint_threshold,
      'scalar_negative_control':{'t':tt,'p':pp,'q':qq,'beta_for_2':beta2,'U':U,'is_actual_polytope':False},
      'new_geometry_constructed':False,'claim_C_ge_36':False}

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

if __name__=='__main__':
    print(json.dumps(encode(run()),sort_keys=True,separators=(',',':')))
