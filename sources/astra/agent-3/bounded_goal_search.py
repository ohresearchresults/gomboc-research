"""Direct search in families with at most 84 vertices or 84 maximal facets.

Euler's relation and the planar graph bound give E<=246, hence both 2E<500
and V+E+F<500 for every nondegenerate 3D member. The initial large own110 body
only supplies shape coordinates; no intermediate nonwinner is exactly polished.
Every numerical strict110 nominee receives an immediate complete exact audit.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, eye, hstack, vstack

from strict110_contact_coarsening import load
from vertex_geometry import geometry as vg
from support_geometry import geometry as sg, escape
from direct_face_polish import guards as vertex_guards, run as vertex_repair
from exact_audit_supports import audit as support_audit
from goal_nomination import ExactGoalCandidateFound


def support_guards(g, derivative=True):
    vals=[];Js=[];cl=[]
    for name,dname in [('Z','DZ'),('H','DH')]:
        A=g[name]
        if derivative:
            v,_,J=escape(A,g[dname],angular=False)
        else:
            v,_=escape(A,angular=False)
        root=int(np.argmax(np.sum(A*A,axis=1)));mask=np.arange(len(A))!=root
        vals.append(v[mask]);cl.append(int(sum(v<0)))
        if derivative:Js.append(J[mask])
    return np.concatenate(vals),np.vstack(Js)if derivative else None,dict(S=cl[1],U=cl[0],V=g['nv'],F=g['nf'])


def exact_support(Q,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);np.save(out/'literal_supports.npy',Q)
    grid=max(float(v).as_integer_ratio()[1]for v in Q.ravel())
    a=support_audit(out/'literal_supports.npy',out/'exact',grid)
    if a['counts']==[1,1,0]and a['weak']==[0,0,0]and 34<=2*a['E']<500 and a['V']+a['E']+a['F']<500:
        raise ExactGoalCandidateFound('Exactly verified bounded-family Figure: '+str(out))
    return a


def repair_support(source,out,steps):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);Q=np.load(source);assert len(Q)<=84
    trace=[];trust=.004;start=time.time()
    for it in range(steps):
        g=sg(Q);v,J,cl=support_guards(g);merit=float(np.maximum(1e-9-v,0).sum())
        row=dict(it=it,merit=merit,minimum=float(min(v)),trust=trust,seconds=time.time()-start,**cl)
        trace.append(row);np.save(out/'latest.npy',Q);(out/'trace.json').write_text(json.dumps(trace,indent=2))
        if it%10==0:print('BOUNDED_SUPPORT_GOAL',out,row,flush=True)
        if cl['S']==cl['U']==1:
            exact_support(Q,out/f'exact_nomination_it{it}')
        d=Q.size;sx=np.sqrt(np.mean(g['Z']**2));sq=np.sqrt(np.mean(Q**2));M=np.vstack((g['DX'].reshape(-1,d)/sx,np.eye(d)/sq))
        _,s,V=svd(M,full_matrices=False,check_finite=False);W=V.T/s;m=len(v);I=eye(d);O=csr_matrix((d,m));sc=.001
        A=vstack([hstack([-csr_matrix(J@W/sc),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr')
        b=np.r_[(v-1e-9)/sc,np.zeros(2*d)];bound=trust/np.sqrt(d)
        r=linprog(np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)],A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(0,None)]*(m+d),method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=10.))
        if not r.success:row['error']=r.message;trust*=.4
        else:
            dq=(W@r.x[:d]).reshape(Q.shape);ok=False
            for k in range(14):
                qq=Q+2.**-k*dq
                try:
                    gg=sg(qq,False);vv,_,cc=support_guards(gg,False);mm=float(np.maximum(1e-9-vv,0).sum())
                except(ValueError,np.linalg.LinAlgError):continue
                if cc['S']==cc['U']==1:exact_support(qq,out/f'exact_nomination_it{it}_line{k}')
                if mm<merit-max(1e-13,merit*1e-7):Q=qq;ok=True;row['alpha']=2.**-k;break
            if ok and k==0:trust=min(.2,trust*1.3)
            if not ok:trust*=.4
        if trust<1e-11:break
    np.save(out/'endpoint.npy',Q)
    print('BOUNDED_SUPPORT_FINITE_STOP',out,trace[-1],flush=True)


def screen(X,kind):
    if kind=='vertices':
        g=vg(X,False);v,_,cl=vertex_guards(g,False)
    else:
        g=sg(X,False);v,_,cl=support_guards(g,False)
    residual=np.maximum(1e-9-v,0)
    return float(residual.sum()),float(residual@residual),cl


def run(source,out,kind,seeds,steps):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);a,X,Y=load(source)
    assert a['counts']==[1,1,0] and a['weak']==[0,0,0]
    start=X if kind=='vertices'else Y
    (out/'method.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),source_audit_sha256=hashlib.sha256((Path(source)/'audit.json').read_bytes()).hexdigest(),kind=kind,maximum_inputs=84,maximum_true_edges=246,maximum_2E=492,maximum_VplusEplusF=494,physical_scope='uniformly filled hull in vertex mode; uniformly filled intersection of supports in facet mode; actual centroid recomputed at every proposal'),indent=2))
    for seed in range(seeds):
        d=out/f'seed{seed:02d}';d.mkdir();rng=np.random.default_rng(91904+seed);noise=rng.normal(size=start.shape)*1e-8*np.sqrt(np.mean(start*start));body=start+noise
        np.save(d/'initial.npy',body);np.save(d/'initial_noise.npy',noise);hist=[]
        while len(body)>84:
            rows=[]
            for j in range(len(body)):
                trial=np.delete(body,j,axis=0)
                try:l1,l2,cl=screen(trial,kind)
                except(ValueError,np.linalg.LinAlgError):continue
                rows.append(dict(removed=j,L1=l1,L2=l2,**cl))
            if not rows:raise ValueError('no full-dimensional bounded deletion candidate')
            key='L2'if seed==1 else'L1';rows.sort(key=lambda r:r[key]);pick=0 if seed<2 else int(rng.integers(min(3,len(rows))));row=rows[pick]
            body=np.delete(body,row['removed'],axis=0);row['inputs']=len(body);hist.append(row)
            np.save(d/'decimation_latest.npy',body);(d/'decimation.json').write_text(json.dumps(hist,indent=2))
        np.save(d/'bounded_initial.npy',body)
        print('BOUNDED_GOAL_SEED',d,kind,screen(body,kind),flush=True)
        if kind=='vertices':vertex_repair(d/'bounded_initial.npy',d/'goal_repair',steps,1e-8)
        else:repair_support(d/'bounded_initial.npy',d/'goal_repair',steps)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--kind',choices=['vertices','supports'],required=True);p.add_argument('--seeds',type=int,default=3);p.add_argument('--steps',type=int,default=800);a=p.parse_args();run(a.source,a.out,a.kind,a.seeds,a.steps)
