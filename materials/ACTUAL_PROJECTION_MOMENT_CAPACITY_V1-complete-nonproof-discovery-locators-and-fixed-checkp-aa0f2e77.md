# material-aa0f2e7700aa

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# ACTUAL_PROJECTION_MOMENT_CAPACITY_V1: nonproof discovery methods

These are complete numerical locator sources, NOT a body construction and NOT an exclusion theorem. The exact rational controls/proof are instead the two-part capsule [internal-source-reference] and [internal-source-reference]. Do not substitute numerical search outcomes for its exact assertions.

Environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1. All inputs and nondefault parameters are below. File1 supplies the shared functions used by file2. There are no other local dependencies. Save the two code fences verbatim with one final newline each.

File1 sym_locator_fibre.py,2706 bytes,SHA256 59e94190d016031155f1bb214240b9d6d3b29ce8fe6c3979a77f1ec22fae4d04.
```python
"""Nonproof symmetric formal moment feasibility locator; not a body or exclusion.
Python3.13.5 NumPy2.3.5 SciPy1.17.0. Seed fixed below.
"""
import numpy as np
from scipy.optimize import differential_evolution, minimize
T=2.04

def constraints(x, data=False):
    b,k,t,p,rho,varadd=x
    h=1+b+k;r=h*p;q=t*T;mu=r/q;z=(1+(k-1)*p-mu)/(1-b);m=3*p/t
    g=np.array([p/2,p/2,z]);ell=np.array([k-1,k-1,b-1]);bet=np.array([h,h,0.])-q*ell
    Q0=(4*np.eye(3)-np.ones((3,3)))/(80*t)+np.outer(g-.25,g-.25)/(t-1)
    targ=np.array([2*r*p-(1+b+2*k)*p/2]*2+[4*r*z-r-b*p])/5
    y=targ-Q0@bet;delta=bet@y
    Q=Q0+np.outer(y,y)/max(delta,1e-10)
    vec=np.array([bet[2],bet[2],-2*bet[0]]);vec/=np.linalg.norm(vec)
    Q+=varadd*np.outer(vec,vec)
    r0=(q-3*p)**2/(3*q*(3*p-1))
    Bp=p/t*((mu+1+b+k)**2+mu*mu+1+b*b+k*k)/(20*mu*mu)
    kap=1-p/t-rho
    fan=Bp+rho/10+(1-(T+p/t+rho)/4)**2/max(kap,1e-10)
    AR=t*(1-b)*rho/(2*mu);AK=t/2-b/(1-b)*AR
    W1=t*t*(1-b)*(T-m)/6
    W2=t*t*(1-b)*m*(r-h/3)/6
    # Scalar root moments fix root n first and second.
    NR=r*AR+W1;NR2=r*r*AR+2*r*W1+W2
    NK=4*(t/6)*r-b/(1-b)*NR
    # Initial covariance completion Qstar, not general fiber.
    var=h*h*(Q[0,0]+2*Q[0,1]+Q[1,1])
    NK2=5*(t/6)*(r*r+var)-b/(1-b)*NR2
    B0=AK-.5;B1=NK-h/3;B2=NK2-h*h/4
    M0=AK-AR-r*r/(2*h*h)
    M1=t*r/6-W1/(1-b)+r**3/(6*h*h)
    M2=5*t*var/6-W2/(1-b)-r**4/(12*h*h)
    sRT=p*(q-1)/(q-3*p)
    hh=(2*(W2/W1-r)+np.sqrt(4*r*r+10*r*(W2/W1)+4*(W2/W1)**2))/3
    WB=(r*hh*hh/2+hh**3/3)/(h*h)
    c=np.array([p-.5,(t+1)/4-p,t/2-p,mu-.25,4*mu-b,4*mu-k,
      4*t*mu-k*t-1-b-k,b-4*mu*(T-2), t+2-4*p-4*z,z-(1-t),m-13/15,45/7-t,
      delta, .6*mu*mu-ell@Q@ell, h-r-q*k,
      rho-r0,1.5*r0-rho,kap,1.6-fan,AK-.5,M0,M1,M2,M0*M2-M1*M1,
      B1-h*B0,t*h*B0-B1,B0*B2-B1*B1,WB-W1,2*AK-sRT,
      1.5*NK*NK-AK*NK2,
    ])
    if data:return c,dict(x=x.tolist(),z=z,m=m,r=r,mu=mu,rho0=r0,fan=fan,Q=Q.tolist(),projection=(AK,AR,NK,NR,NK2,NR2),omega=(M0,M1,M2),sRT=sRT,labels=('p_low','jointp','p_high','mu','bmu','kmu','massface','endpoint','g_zup','g_zlo','m','t','covdel','ellvar','Gc','rhoLow','rhoHigh','fanrest','fan','Karea','Om0','Om1','Om2','OmH','outside_min','outside_max','outsideH','rootband','centroid_area','Kberwald'))
    return c

def cost(x):
    try:
      c=constraints(x);bad=np.minimum(c,0);return float(np.sum(bad*bad))
    except (ValueError,ZeroDivisionError):return 1e6
if __name__=='__main__':
  bd=[(.041,.995),(.0001,.7),(1.01,3.46),(.501,.999),(.0001,.9),(0.,2.)]
  res=differential_evolution(cost,bd,seed=43100,maxiter=900,popsize=12,tol=1e-10,polish=True)
  c,d=constraints(res.x,True)
  print('NONPROOF_FORMAL_SYMMETRIC_LOCATOR',res.fun,d)
  print(list(zip(d['labels'],c)))
```

File2 first_pass_capacity_fail_locator.py,992 bytes,SHA256 3bf110f51d0c66d02c2390feb9faab658ffdbe9a40a4d3c850a6c8177bbba3b9.
```python
"""Nonproof search separating selected first-moment tests from density-capacity cut."""
import numpy as np
from scipy.optimize import differential_evolution
from sym_locator_fibre import constraints

def extra(x):
 b,k,t,p,rho,va=x;h=1+b+k;q=t*2.04;r=h*p;al=1-b;mu=r/q
 ar=t*al*rho/(2*mu);a=t/2-b/al*ar
 w1=al*t*(q-3*p)/6;w2=al*t*p*(r-h/3)/2
 s0=w1*w1/w2;gam=w2/w1;kap=4*(r+gam)*gam/(3*h*h*s0);ep=min(.5,1/(2*kap))
 slb=(s0-4*(r+gam)*gam*ep**3/(3*h*h))/(1-ep*ep);aq=t/2-b/al*slb
 def phi(z):return 2*h*z*z+(h-3*r)*z-r*t/2+b*t*(q-3*p)/2
 return np.array([phi(a),-phi(aq)-.00005]),dict(a=a,aq=aq,phi=phi(a),phiQ=phi(aq))

def fun(x):
 c=np.r_[constraints(x),extra(x)[0]];v=np.minimum(c,0);return v@v
if __name__=='__main__':
 res=differential_evolution(fun,[(.04001,.7),(.00001,.25),(1.0001,2.5),(.50001,.87),(.01,.8),(0,1)],seed=11516,maxiter=1100,popsize=14,tol=1e-10,polish=True)
 print('NONPROOF_CAPACITY_SEPARATION_LOCATOR',res.fun,res.x.tolist(),extra(res.x),constraints(res.x).tolist())
```

Reconstruction/execution commands:
OPENBLAS_NUM_THREADS=1 python sym_locator_fibre.py > fibre_probe_stdout.txt
OPENBLAS_NUM_THREADS=1 python first_pass_capacity_fail_locator.py > capacity_separation_stdout.txt

Expected initial terminal markers are NONPROOF_FORMAL_SYMMETRIC_LOCATOR and NONPROOF_CAPACITY_SEPARATION_LOCATOR. In the stated environment both attained objective0.0. Their fixed captured floating checkpoints are:
P1=[0.269757465906179,0.04891537147572178,1.2432981713962103,0.5547899468237838,0.15106261174630708,0.02739661763040202].
P2=[0.14811074414080194,0.004989903285354064,1.138318466967803,0.5269783178233205,0.13644068085241567,0.029360089271305068].
They were rounded componentwise to denominator10^6 and then checked exactly by the separate standard-library audit. That exact audit, not floating bit-for-bit replay, is the result's proof boundary.

Captured discovery stdout identifiers (supplementary generated outputs, reconstructible in the stated environment, not essential exact inputs):
fibre_probe_stdout.txt,2612 bytes,SHA256 a9ed10f3b6442c2cf3074ed11f8337e6b38b3692909efdcf90804c596fb94bd5.
capacity_separation_stdout.txt,1009 bytes,SHA256 d72ea235259557dfe621c8b0e2208af0f3695d8d00813d2a925ff5589a696c25.
Different numerical-library builds may print different float representations or search paths. No mathematical claim rests on that identity.

Correction to a transient coordinator-context summary: the P1 generator uses seed43100,maxiter900,popsize12 as the literal source states, not seed51404,maxiter1800,popsize20. The literal default was rerun and reproduced P1. A separate run with the latter parameters returned another formal point, not P1, and is not claimed as the source of this control. The immutable exact checkpoint and audit are unchanged.

Verification of exact numerical findings is ONLY:
python exact_capacity_audit.py --out projection_capacity_audit.json
with the full part1 source and hashes/terminal markers specified in part2. These locators are retained as reusable research methods; failed or successful finite searches are not promoted to continuum proofs or equilibrium certificates.
