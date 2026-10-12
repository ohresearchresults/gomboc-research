"""Strict110 search on a <=248-edge contact family with convexity kept hard.

Only valid, full-dimensional physical contact bodies are admitted during the
equilibrium phase. A complete exact audit is triggered at every numerical110.
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack

from contact_numpy import Chart
from contact_physical_110 import PhysicalGuards,freeze
from contact_quota_polish import metric


def run(source,out,steps):
    c=Chart(source);assert 17<=c.meta['E']<=248
    out=Path(out);out.mkdir(parents=True,exist_ok=False);q=c.q0.copy();G=PhysicalGuards(c,True)
    g=c.physical(q);v,J,t,JT,cl=G.evaluate(g)
    gapfloor=min(1e-8,float(min(g['noncontact']))*.1);turnfloor=min(1e-9,float(min(t))*.1)
    assert min(t)>0
    (out/'source_construction.json').write_bytes(Path(source).read_bytes())
    (out/'method.json').write_text(json.dumps(dict(gapfloor=gapfloor,turnfloor=turnfloor,maximum_E=248,scope='hard physical convexity and actual uniform mass throughout the strict110 search; E248 gives2E496 andEuler sum498'),indent=2))
    trace=[];trust=.025;start=time.time()
    for it in range(steps):
        g=c.physical(q);v,J,t,JT,cl=G.evaluate(g);merit=float(np.maximum(1e-9-v,0).sum())
        row=dict(it=it,merit=merit,trust=trust,gap=float(min(g['noncontact'])),turn=float(min(t)),seconds=time.time()-start,**cl)
        trace.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(trace,indent=2))
        if it%10==0:print('BOUNDED_CONVEX_GOAL',out,row,flush=True)
        if cl['S']==cl['U']==1:freeze(c,q,out/f'exact_nomination_it{it}')
        W=metric(c,g);d=c.d;m=len(v);bound=trust/np.sqrt(d)
        hval=np.r_[g['noncontact']-gapfloor,t-turnfloor];HJ=np.vstack((g['Dgap'][~c.incidence],JT))@W
        keep=hval<=bound*np.sum(abs(HJ),axis=1)+1e-10;HJ=HJ[keep];hval=hval[keep]
        I=eye(d);O=csr_matrix((d,m));sc=.001
        A=vstack([hstack([-csr_matrix(J@W/sc),-eye(m),csr_matrix((m,d))]),
                  hstack([-csr_matrix(HJ/sc),csr_matrix((len(HJ),m+d))]),
                  hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-1e-9)/sc,hval/sc,np.zeros(2*d)]
        r=linprog(np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)],A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(0,None)]*(m+d),method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=10.))
        if not r.success:row['error']=r.message;trust*=.4
        else:
            dq=W@r.x[:d];ok=False
            for k in range(17):
                qq=q+2.**-k*dq
                try:
                    gg=c.physical(qq);vv,_,tt,_,cc=G.evaluate(gg)
                except(ValueError,np.linalg.LinAlgError):continue
                if min(gg['noncontact'])<gapfloor*.9 or min(tt)<turnfloor*.9:continue
                if cc['S']==cc['U']==1:freeze(c,qq,out/f'exact_nomination_it{it}_line{k}')
                mm=float(np.maximum(1e-9-vv,0).sum())
                if mm<merit-max(1e-13,merit*1e-7):q=qq;ok=True;row['alpha']=2.**-k;break
            if ok and k==0:trust=min(.3,trust*1.3)
            if not ok:trust*=.4
        if trust<1e-11:break
    np.save(out/'endpoint_q.npy',q);print('BOUNDED_CONVEX_GOAL_FINITE_STOP',out,trace[-1],flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=1000);a=p.parse_args();run(a.source,a.out,a.steps)
