# material-0b8645fa76b4

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Numerical polynomial-profile method and six exact input checkpoints

These are numerical research methods and frozen IEEE-double checkpoints, NOT certificates of global positivity, polyhedral110 constructions or optima. The independently exact MORSE6_RATIONAL_A7_100 is defined instead by materials [internal-source-reference] and [internal-source-reference]. This capsule preserves the complete producing algorithms and every numerical non-record profile encountered in the progression, including the simpler degree4 profile.

Save the three fenced source units under their named filenames, UTF-8/LF. Environment actually used: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1. No hidden input file is needed for the frozen replay. Source hashes/bytes:
profile_scout.py 3739B cd8e70df46b0f3df975429427e9e8637aa946d83c1ad785b4bb08ee4077e3920
profile_margin.py 1804B 2a6cda813fa4227a05717008dac078be8c0416702e638d1c90eee1618cd0bd41
profile_checkpoints.py 3711B b576da3271b2b8f9c30362d8db31f0c9e2c8d196d51c2f26687eb413c404246d

Reconstruction/check command: OPENBLAS_NUM_THREADS=1 python profile_checkpoints.py
Observed marker NUMERICAL_PROFILE_CHECKPOINTS_REPLAYED_NOT_EXACT_CERTIFICATES.
Observed output profile_replayed.json 5138B SHA19c9bf92c0ff7d330ee102253f732a004ff4da78441aba28233d7d2ea0bb9e6f. This regenerates complete numerical P/Q/B/H coefficients and all six frozen parameter sets plus dense-grid checks; no optimizer rerun is required to recover them. Exact cross-platform optimizer trajectories are not claimed.

Producing commands (prefix all with OPENBLAS_NUM_THREADS=1):
python profile_scout.py --out deg2.json
python profile_scout.py --degree 3 --rdegree 1 --grid 301 --margin 0.0001 --iterations 500 --out deg3r1.json
python profile_scout.py --degree 4 --rdegree 2 --grid 301 --margin 0.0001 --iterations 500 --out deg4r2.json
python profile_scout.py --degree 6 --rdegree 3 --grid 501 --margin 0.0001 --iterations 700 --out deg6r3.json
python profile_margin.py --start deg4r2.json --out morse4.json --a 0.07 --iterations 400
python profile_margin.py --start deg6r3.json --out morse6.json --a 0.07 --iterations 500
The frozen profile_checkpoints.py data can also be written as the start JSON containing degree,rdegree,z to reproduce a particular continuation without repeating earlier optimization. Each start's literal binary-double-defining decimal vector is complete below. All calls used seed0/noise0.

Amplitude scouts found a approximately .07229146,.07336485,.07607173,.07836628 for degrees2,3,4,6. Their dense tests violate the requested sampled-grid margin slightly; in particular degree2 is not accepted as a positive-gap body. Fixed-a=.07 margin scouts found mu approximately .25597899 (degree4) and .30543877 (degree6), again not exact global certificates. The exact degree6 rationalized body separately proves mu>3/10 and curvature numerator gap>1/2000 over the entire interval. The certificate does not claim these numerical optimizers found a maximum, or that the whole family is excluded beyond it.

## profile_scout.py
```python
"""Numerical sufficient-condition search for polynomial circular sections.
No numerical output is a polyhedron or a rigorous certificate.
Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0.
"""
import argparse,json,os
import numpy as np
from numpy.polynomial import polynomial as pp
from scipy.optimize import minimize
from pathlib import Path

def pad(a,n):
    return np.pad(np.asarray(a,float),(0,max(0,n-len(a))))[:n]
def moment(p):return sum(p/(2*np.arange(len(p))+1))
def setup(z,degree=2,rdegree=0):
    # a, lambda; free P coefficients except constant and quadratic mass closure;
    # all Q shape coefficients; B(0)=1.
    a,lam=z[:2]; j=2
    p=np.zeros(degree+1);p[0]=1
    for k in range(1,degree+1):
        if k!=2:p[k]=z[j];j+=1
    q=z[j:j+degree+1];j+=degree+1
    B=np.r_[1,z[j:j+rdegree]]
    H=pp.polymul([1,-1],pp.polymul(B,B))
    p[2]=-moment(pp.polymul(H,p))/moment(np.r_[0,0,H])
    return a*p,a*q,B,H,lam

def initial(degree=2,rdegree=0):
    a=1/14;lam=497/500
    pf=[-279/40]+[0]*(degree-2)
    q=[77/20,-37/5,10/7]+[0]*(degree-2)
    return np.array([a,lam]+pf+q+[0]*rdegree,float)

def constraints(z,y,degree=2,rdegree=0,margin=1e-8):
    P,Q,B,H,lam=setup(z,degree,rdegree)
    hp=pp.polyder(H);hpp=pp.polyder(hp)
    pv=pp.polyval(y,P);qv=pp.polyval(y,Q)
    p1=pp.polyval(y,pp.polyder(P));q1=pp.polyval(y,pp.polyder(Q))
    p2=pp.polyval(y,pp.polyder(P,2));q2=pp.polyval(y,pp.polyder(Q,2))
    h=pp.polyval(y,H);h1=pp.polyval(y,hp);h2=pp.polyval(y,hpp)
    D=pv*pv+y*qv*qv;dp=2*pv*p1+qv*qv+2*y*qv*q1
    Rprime=h1*D+h*dp;Jprime=lam*lam+h1+dp
    A=h*h1+2*y*h*h2-y*h1*h1
    N=2*p1+4*y*p2;L=6*q1+4*y*q2
    s=np.sqrt(np.maximum(0,h)/np.maximum(1e-20,D))
    w=-Rprime/np.maximum(1e-20,D)
    curvature=-A-np.maximum(0,h)**1.5*np.sqrt(N*N+y*L*L)
    return np.r_[pp.polyval(y,B)-.05,D/(z[0]**2)-1e-6,w-s*Jprime-margin,w+s*Jprime-margin,curvature-margin]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--degree',type=int,default=2);ap.add_argument('--rdegree',type=int,default=0)
    ap.add_argument('--iterations',type=int,default=300);ap.add_argument('--start');ap.add_argument('--out',default='scout.json');ap.add_argument('--grid',type=int,default=101);ap.add_argument('--margin',type=float,default=1e-7);ap.add_argument('--seed',type=int,default=0);ap.add_argument('--noise',type=float,default=0)
    args=ap.parse_args();z=initial(args.degree,args.rdegree)
    if args.start:z=np.array(json.loads(Path(args.start).read_text())['z'])
    if args.noise:z[2:]+=np.random.default_rng(args.seed).normal(size=len(z)-2)*args.noise
    y=(1-np.cos(np.linspace(0,np.pi,args.grid)))/2
    bounds=[(.01,.4),(.5,1.5)]+[(-100,100)]*(len(z)-2-args.rdegree)+[(-.8,.8)]*args.rdegree
    calls=[0]
    def callback(z):
        calls[0]+=1
        if calls[0]%25==0:print('step',calls[0], 'a',z[0], 'min',constraints(z,y,args.degree,args.rdegree,args.margin).min(),flush=True)
    r=minimize(lambda z:-z[0],z,method='SLSQP',bounds=bounds,constraints=[{'type':'ineq','fun':lambda z:constraints(z,y,args.degree,args.rdegree,args.margin)}],callback=callback,options={'maxiter':args.iterations,'ftol':1e-12,'disp':True})
    vals=constraints(r.x,np.linspace(0,1,10001),args.degree,args.rdegree,args.margin)
    data={'degree':args.degree,'rdegree':args.rdegree,'z':r.x.tolist(),'success':bool(r.success),'message':r.message,'min_dense_grid':float(vals.min()),'grid':args.grid,'margin':args.margin,'iterations':args.iterations,'seed':args.seed,'noise':args.noise,'coefficients':[v.tolist() if isinstance(v,np.ndarray) else v for v in setup(r.x,args.degree,args.rdegree)]}
    Path(args.out).write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    print(json.dumps(data),flush=True)
if __name__=='__main__':main()
```

## profile_margin.py
```python
"""Finite numerical scout: maximize normalized radial monotonicity margin."""
import argparse,json
import numpy as np
from pathlib import Path
from scipy.optimize import minimize
from profile_scout import initial,setup,constraints

def main():
    p=argparse.ArgumentParser();p.add_argument('--start',required=True);p.add_argument('--out',required=True);p.add_argument('--a',type=float,default=.07);p.add_argument('--grid',type=int,default=501);p.add_argument('--iterations',type=int,default=500);p.add_argument('--curvature',type=float,default=.001);args=p.parse_args()
    data=json.loads(Path(args.start).read_text());d=data['degree'];rd=data['rdegree'];z=np.r_[data['z'],0.0];z[0]=args.a
    y=(1-np.cos(np.linspace(0,np.pi,args.grid)))/2;n=len(y)
    def cons(z,y=y):
        cs=constraints(z[:-1],y,d,rd,0);n=len(y)
        cs[2*n:4*n]-=z[-1];cs[4*n:]-=args.curvature
        return cs
    bounds=[(args.a,args.a),(.3,2)]+[(-1000,1000)]*(len(z)-3-rd)+[(-2,2)]*rd+[(0,2)]
    count=[0]
    def cb(z):
        count[0]+=1
        if count[0]%25==0:print('step',count[0],'mu',z[-1],'gap',cons(z).min(),flush=True)
    result=minimize(lambda z:-z[-1],z,bounds=bounds,method='SLSQP',constraints=[{'type':'ineq','fun':cons}],callback=cb,options={'maxiter':args.iterations,'ftol':1e-11,'disp':True})
    z=result.x;data.update({'z':z[:-1].tolist(),'mu':float(z[-1]),'success':bool(result.success),'message':result.message,'margin_objective':True,'grid':args.grid,'iterations':args.iterations,'curvature':args.curvature,'min_dense_grid':float(cons(z,np.linspace(0,1,10001)).min()),'coefficients':[v.tolist() if isinstance(v,np.ndarray) else v for v in setup(z[:-1],d,rd)]})
    Path(args.out).write_text(json.dumps(data,sort_keys=True,indent=2)+'\n');print(json.dumps(data))
if __name__=='__main__':main()
```

## profile_checkpoints.py
```python
"""Frozen numerical checkpoints; not exact geometric certificates.
Run: python profile_checkpoints.py (requires profile_scout.py).
"""
import json,hashlib
from pathlib import Path
import numpy as np
from profile_scout import setup,constraints
CHECKPOINTS = {'deg2': {'degree': 2, 'rdegree': 0, 'z': [0.07229146094039673, 0.9943282139533522, -6.916445504016611, 3.839551197045385, -7.267993449731267, 1.333015784194128], 'grid': 101, 'iterations': 300, 'margin': 1e-07, 'seed': 0, 'noise': 0, 'min_dense_grid': -0.0001291455260209919, 'success': True}, 'deg3r1': {'degree': 3, 'rdegree': 1, 'z': [0.07336484762282573, 0.9925939594752591, -6.742231701479309, 1.5501861915441506, 3.802549912576649, -6.688915670479745, -0.4348110335401329, 0.6727775665153185, 0.00528351732161924], 'grid': 301, 'iterations': 500, 'margin': 0.0001, 'seed': 0, 'noise': 0, 'min_dense_grid': -4.327916802070785e-06, 'success': True}, 'deg4r2': {'degree': 4, 'rdegree': 2, 'z': [0.07607172929837522, 1.0203140624844997, -6.745236901966104, 10.038092002238828, -8.25442774773679, 3.7235742037227895, -5.556644782100843, -7.578981364712291, 14.83377103321684, -5.5740148287828095, -0.013171835659777831, -0.06586008601211327], 'grid': 301, 'iterations': 500, 'margin': 0.0001, 'seed': 0, 'noise': 0, 'min_dense_grid': -3.895390019974651e-05, 'success': True}, 'deg6r3': {'degree': 6, 'rdegree': 3, 'z': [0.0783662760584383, 1.0603991185225004, -7.465018214495054, -14.966134414216787, 52.80004577854575, -70.95450174691412, 31.766252558366237, 3.945391213018268, -8.288700097991589, 8.532255681267092, -42.320496990239796, 92.2338011958383, -78.51786067590143, 24.94005939941893, -0.08510115175283534, 0.034972040120745174, -0.3174653414862292], 'grid': 501, 'iterations': 700, 'margin': 0.0001, 'seed': 0, 'noise': 0, 'min_dense_grid': -1.775093436772917e-05, 'success': True}, 'morse4': {'degree': 4, 'rdegree': 2, 'z': [0.07, 0.9984582375488326, -7.094257916076955, 9.060576252048751, -8.460328002570952, 3.786706174487576, -6.632449268457887, -5.645095900760376, 13.529056721206151, -5.046965418841848, 0.002901945874612787, -0.011981200668401007], 'grid': 501, 'iterations': 400, 'margin': 0.0001, 'seed': 0, 'noise': 0, 'min_dense_grid': -4.3981542796611706e-06, 'success': True, 'curvature': 0.001, 'margin_objective': True, 'mu': 0.25597898989326523}, 'morse6': {'degree': 6, 'rdegree': 3, 'z': [0.07, 1.0296672071036308, -7.736015664670783, -11.309209241981469, 49.28528177408844, -72.91810136435402, 33.87470441445325, 3.992830336912136, -9.033835788961241, 7.320751074500841, -36.0320826603622, 88.42502980248324, -81.07362403558939, 27.231888700609733, -0.04203962209817957, 0.019010771823422225, -0.150151443390074], 'grid': 501, 'iterations': 500, 'margin': 0.0001, 'seed': 0, 'noise': 0, 'min_dense_grid': -1.205775938206699e-05, 'success': True, 'curvature': 0.001, 'margin_objective': True, 'mu': 0.30543877076287396}}

def main():
    out={}
    for name,c in CHECKPOINTS.items():
        z=np.asarray(c['z']);d=c['degree'];rd=c['rdegree']
        cs=constraints(z,np.linspace(0,1,10001),d,rd,0 if c.get('margin_objective') else c['margin'])
        if c.get('margin_objective'):
            cs[20002:40004]-=c['mu'];cs[40004:]-=c['curvature']
        out[name]={'checkpoint':c,'recomputed_min_dense_grid':float(cs.min()),'coefficients':[x.tolist() if isinstance(x,np.ndarray) else x for x in setup(z,d,rd)]}
    raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('profile_replayed.json').write_bytes(raw)
    print('NUMERICAL_PROFILE_CHECKPOINTS_REPLAYED_NOT_EXACT_CERTIFICATES')
    print('profile_replayed.json',len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```
