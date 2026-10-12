# material-3f26d06e0feb

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

from fractions import Fraction as F
import numpy as np
import scipy
from scipy.optimize import linprog


def K(z,t):
    if z==1: return max(1-t,0)
    lo,hi=0.,1.
    if z>1: lo=max(lo,(t-1)/(z-1))
    else: hi=min(hi,(t-1)/(z-1))
    lo=max(lo,0.);hi=min(hi,1.)
    if hi<=lo:return 0.
    return (1-t)*(hi**3-lo**3)+.75*(z-1)*(hi**4-lo**4)

def tentcall(t):
    if t<=1: return 1-t+t**4/8
    return (2-t)**4/8

if __name__=='__main__':
    nodes=np.r_[0,np.linspace(.02,.98,49),np.linspace(1.02,2,50)]
    ts=np.linspace(0,2,401)
    calls=np.array([[K(z,t)/3 for z in nodes] for t in ts])
    A=np.vstack([-calls,calls])
    b=np.r_[-np.array([tentcall(t) for t in ts]), (2-ts)**2/4]
    eq=np.vstack([np.ones(len(nodes)),nodes,np.array([1]+[0]*(len(nodes)-1))])
    res=linprog((nodes-1)**2/5,A_ub=A,b_ub=b,A_eq=eq,b_eq=[3,3,.4],bounds=(0,None),method='highs')
    print('versions',np.__version__,scipy.__version__)
    print(res.message)
    print('variance',res.fun,'sharp weak new',.1+1688/234375)
    if res.success:
        for z,x in zip(nodes,res.x):
            if x>1e-7:print(z,x, F(float(z)).limit_denominator(10000),F(float(x)).limit_denominator(10000))
