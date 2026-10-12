# material-15a94febb513

AI research material

---

#!/usr/bin/env python3
"""Exact own-centroid projective-pencil identities for the complete E17 chart.
Requires the complete sibling full_cut_stack_chart.py and SymPy 1.14.0.
Run with assertions: python -B full_cut_stack_centroid_pencil.py.
"""
import hashlib
import json
from pathlib import Path
import sympy as s
import full_cut_stack_chart as core


def rat(x): return s.Rational(x.numerator,x.denominator)
def can(x): return s.cancel(x)

def main():
    if not __debug__:raise RuntimeError('Assertions must remain enabled')
    a=s.Symbol('a');p=list(map(rat,core.P));q=list(map(rat,core.Q));u=list(map(rat,core.U))
    ps=rat(core.PS);beta=rat(core.BETA);excess=can(ps-sum(u[j]*p[j] for j in range(3)))
    d=[1+a*x for x in p];e=[1+(1-a)*x for x in q];ds=1+a*ps
    B=[s.Matrix([0,-beta,0]),s.Matrix([0,1-beta,0]),s.Matrix([0,0,1])]
    L=[s.Matrix([-p[j]/d[j],B[j][1]/d[j],B[j][2]/d[j]]) for j in range(3)]
    R=[s.Matrix([q[j]/e[j],B[j][1]/e[j],B[j][2]/e[j]]) for j in range(3)]
    us=sum((u[j]*B[j] for j in range(3)),s.zeros(3,1))
    S=s.Matrix([-ps/ds,us[1]/ds,us[2]/ds]);V=B+L+R+[S]
    w=[p[2]/d[2],p[1]/(d[1]*d[2]),p[0]/s.prod(d),excess/(ds*s.prod(d)),
       q[2]/e[2],q[1]/(e[1]*e[2]),q[0]/s.prod(e)]
    D=can(sum(w));J=s.zeros(3,1);K=s.zeros(3,3)
    for ids,weight in zip(core.TETS,w):
        vv=[V[i] for i in ids];ss=sum(vv,s.zeros(3,1))
        J+=weight*ss;K+=weight*(ss*ss.T+sum((v*v.T for v in vv),s.zeros(3,3)))
    g=(J/(4*D)).applyfunc(can)
    Sigma=(K/(20*D)-g*g.T).applyfunc(can)
    assert can(g[0]-s.diff(D,a)/(4*D))==0
    for j in range(3):assert can(s.diff(g[j],a)-5*Sigma[j,0]-g[j]*g[0])==0
    assert can(s.diff(s.diff(D,a)/D,a)-20*Sigma[0,0]-4*g[0]*g[0])==0
    n,h=map(lambda x:s.Poly(x,a,domain=s.QQ),s.fraction(D))
    assert n.degree()<=5 and h.degree()<=7
    derivative_num=s.Poly(s.fraction(can(s.diff(D,a)))[0],a,domain=s.QQ)
    lo=-1/max(p+[ps]);hi=1+1/max(q)
    assert (lo,hi)==(s.Rational(-5,4),s.Rational(3))
    assert derivative_num.count_roots(lo,hi)==1
    # Locate the single actual COM-crossing exactly to a prescribed rational grid.
    lower,upper=lo,hi
    for _ in range(48):
        mid=(lower+upper)/2;value=can(s.diff(D,a)).subs(a,mid)
        if value<0:lower=mid
        elif value>0:upper=mid
        else:lower=upper=mid;break
    assert upper-lower<=s.Rational(17,4*2**48)
    if lower<upper:
        assert s.diff(D,a).subs(a,lower)<0<s.diff(D,a).subs(a,upper)
        assert derivative_num.count_roots(lower,upper)==1
    evaluations=[]
    for aa in core.ALPHAS:
        aa=rat(aa);points,weights=core.geometry(core.BETA,core.F(int(s.numer(aa)),int(s.denom(aa))),core.P,core.Q,core.U,core.PS)
        DD,JJ,KK,*_=core.surface(points)
        assert D.subs(a,aa)==rat(DD)
        assert list(g.subs(a,aa))==list(map(rat,core.scale(1/(4*DD),JJ)))
        evaluations.append({'a':str(aa),'D':str(D.subs(a,aa)),'gx':str(g[0].subs(a,aa)),
                            'gx_derivative':str(s.diff(g[0],a).subs(a,aa))})
    data={'identity':'FULL_CUT_STACK_OWN_CENTROID_MONOTONE_PROJECTIVE_PENCIL_V1',
          'sympy_version':s.__version__,'source_chart_sha256':hashlib.sha256(Path(core.__file__).read_bytes()).hexdigest(),
          'D':str(D),'D_numerator_coefficients':list(map(str,n.all_coeffs())),
          'D_denominator_coefficients':list(map(str,h.all_coeffs())),
          'D_derivative_numerator_coefficients':list(map(str,derivative_num.all_coeffs())),
          'degrees':[n.degree(),h.degree(),derivative_num.degree()],
          'centroid':list(map(str,g)),'covariance':[[str(Sigma[i,j]) for j in range(3)] for i in range(3)],
          'admissible_interval':[str(lo),str(hi)],'centroid_crossing_root_count':1,
          'centroid_crossing_exact_bracket':[str(lower),str(upper)],'evaluations':evaluations,
          'scope':'Symbolic-in-a exact moment identities and unique root for the literal positive chart inputs. The general monotonicity and completeness claims have an analytic proof; no all-root equilibrium exclusion is asserted.',
          'marker':'FULL_CUT_STACK_MIXED_CENTROID_PENCIL_EXACT_PASS'}
    print(json.dumps(data,sort_keys=True,indent=2))

if __name__=='__main__':main()
