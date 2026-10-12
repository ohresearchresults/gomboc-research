# material-7af4db22c8c4

AI research material

---

"""Exact acceptance, floating discovery of paired-arrow spectral thresholds.
Requires h5_reference_core.py and h5_paired_arrow_core.py. No interval input.
CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1.
Every exclusion is a rational Farkas certificate; a relaxed feasible point is
not a true common-inverse equilibrium metric. All parameters are arguments.
"""
import json,sys
from pathlib import Path
from functools import reduce
from math import gcd
import numpy as np
from scipy.optimize import linprog
import h5_paired_arrow_core as pc
from h5_reference_core import *

OPTIONS={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9}

def setup(theta,kappa):
    b=body(tuple(map(Q,theta)));pc.B0=b
    pc.C=aligned_reference(b,9,pc.W9);pc.CI=inv(pc.C)
    pc.K=Q(kappa);den=pc.K**2+pc.K+1
    pc.LOW=1/den;pc.UP=pc.K**2/den;pc.SUM=(pc.K**2+1)/den
    pc.E=(tuple(pc.traceprod(pc.C,e) for e in pc.BASIS)+pc.Z,
          pc.Z+tuple(pc.traceprod(pc.CI,e) for e in pc.BASIS))
    c=np.array(pc.C,float);ci=np.array(pc.CI,float);basis=np.array(pc.BASIS,float);z=np.zeros_like(basis)
    blocks=[(-float(pc.LOW)*ci,np.concatenate((basis,z))),
            (float(pc.UP)*ci,np.concatenate((-basis,z))),
            (-float(pc.LOW)*c,np.concatenate((z,basis))),
            (float(pc.UP)*c,np.concatenate((z,-basis))),
            (float(pc.SUM)*c,np.concatenate((-np.array([c@e@c for e in basis]),-basis)))]
    return b,blocks


def label_psd(bid,v):
    r=np.rint(v/np.max(np.abs(v))*10**6).astype(int).tolist();g=abs(reduce(gcd,r));r=[x//g for x in r]
    if next(x for x in r if x)<0:r=[-x for x in r]
    return ['psd',bid,r]


def one_case(b,blocks,top,spoke,polar,maxcuts=80):
    labs=[];aa=[];bb=[];eq=np.array(pc.E,float)
    def add(lab):
        a,rhs=pc.row(lab,spoke,polar,b,top);af=np.array(a,float);s=max(np.linalg.norm(af),abs(float(rhs)),1e-30)
        labs.append(lab);aa.append(af/s);bb.append(float(rhs)/s)
    directions=list(np.eye(3))
    for i in range(3):
        for j in range(i+1,3):
            for sign in (-1,1):directions.append(np.eye(3)[i]+sign*np.eye(3)[j])
    for bid in range(5):
        for d in directions:add(label_psd(bid,d))
    for a in [['primal'],['polar']]+[['order',j] for j in (7,8,9) if j!=top]:add(a)
    for it in range(maxcuts):
        A=np.array(aa);rhs=np.array(bb)
        r=linprog(np.zeros(12),A_ub=A,b_ub=rhs,A_eq=eq,b_eq=[1,1],bounds=[(None,None)]*12,method='highs',options=OPTIONS)
        if r.status==2:
            n=len(labs);E=np.vstack((np.c_[A.T,eq.T],np.r_[np.ones(n),0,0]))
            d=linprog(np.r_[rhs,1,1],A_eq=E,b_eq=np.r_[np.zeros(12),1],bounds=[(0,None)]*n+[(None,None)]*2,method='highs',options=OPTIONS)
            assert d.success and d.fun<0
            labels=[labs[i] for i in np.flatnonzero(d.x[:n]>1e-8)]
            y,z,gap=pc.exact_dual(labels,spoke,polar,b,top)
            return {'top':top,'spoke':spoke,'polar':polar,'status':'exact_excluded','labels':labels,'gap':str(gap),'rounds':it}
        if not r.success:return {'top':top,'spoke':spoke,'polar':polar,'status':'numerical_unknown','message':r.message}
        bad=[];minimum=1.
        for bid,(base,co) in enumerate(blocks):
            vals,vec=np.linalg.eigh(base+np.einsum('k,kij->ij',r.x,co));minimum=min(minimum,min(vals))
            for i in np.flatnonzero(vals < -1e-9):bad.append((bid,vec[:,i]))
        if not bad:return {'top':top,'spoke':spoke,'polar':polar,'status':'relaxed_feasible_numeric','x':r.x.tolist(),'minimum_eigenvalue':float(minimum),'rounds':it}
        for bid,d in bad:add(label_psd(bid,d))
    return {'top':top,'spoke':spoke,'polar':polar,'status':'cut_limit'}


def run(theta,kappa):
    b,blocks=setup(theta,kappa)
    result=[]
    for top,spokes in ((7,(0,5,6)),(8,(1,2)),(9,(3,4))):
        for spoke in spokes:
            for polar in range(1,8):result.append(one_case(b,blocks,top,spoke,polar))
    return {'theta':list(map(str,theta)),'kappa':str(kappa),'reference':'aligned top9 with fixed W9 of paired-arrow core','results':result}


if __name__=='__main__':
    lam=Q(sys.argv[1]) if len(sys.argv)>1 else Q(13,100)
    kappa=Q(sys.argv[2]) if len(sys.argv)>2 else Q(9,2)
    report=run((Q(3,20),Q(3,20),Q(3,20),Q(9,20),lam),kappa)
    out=Path(sys.argv[3] if len(sys.argv)>3 else 'H5_PAIR_SPECTRAL_FRONTIER.json')
    out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    from collections import Counter
    print(dict(Counter(r['status'] for r in report['results'])))
    print('H5_PAIR_SPECTRAL_FRONTIER_DISCOVERY_FINISHED')
