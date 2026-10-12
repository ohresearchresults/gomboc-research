"""Finite free-normal own-mass continuation, with rebuilt fans and P/Q guards.
This produces numerical candidates only. It deliberately does not constrain
both unstable roots to remain unstable. Every accepted endpoint is recounted.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','1');os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np,torch,json,sys,time
from scipy.optimize import linprog
from geometry115 import geometry,read_h,census,bars
from pathlib import Path
torch.set_num_threads(1); torch.set_default_dtype(torch.float64)

def properties(n,m):
    nt=n; vv=torch.linalg.solve(nt[m['triples']],torch.ones((len(m['triples']),3,1))).squeeze(-1)
    tet=vv[m['tetrahedra']];vol=torch.linalg.det(tet)/6
    g=(vol[:,None]*tet.sum(dim=1)/4).sum(dim=0)/vol.sum()
    p=vv-g; q=nt/(1-nt@g)[:,None]
    return p,q,g

def global_scores(x):
    A=x@x.T-np.sum(x*x,axis=1)[:,None];np.fill_diagonal(A,-np.inf)
    return np.max(A,axis=1),np.argmax(A,axis=1)

def diagnostics(n):
    m=geometry(n);pc,pw=global_scores(m['p']);qc,qw=global_scores(m['q']);act=m['active']
    proot=np.argmax(np.sum(m['p']**2,axis=1));qroot=np.argmax(np.sum(m['q']**2,axis=1))
    pb=bars(m['p'],m['edges']);qb=bars(m['q'],m['dual_edges'])
    P=[x for x in pb if x[0]>1e-12];Q=[x for x in qb if x[0]>1e-12]
    pi=np.argsort(pc);qids=[i for i in act if i!=qroot];pids=[i for i in range(len(pc)) if i not in pi[:2]]
    return m,dict(P=P,Q=Q,U=int(np.sum(pc<-1e-10)),S=int(np.sum(qc[act]<-1e-10)),E=len(m['edges']),F=len(act),
        volume=m['volume'],centroid=m['g'].tolist(),proot=int(proot),qroot=int(qroot),
        minP=float(np.min(pc[pids])),minQ=float(np.min(qc[qids])),pc=pc,pw=pw,qc=qc,qw=qw)

def run(source,out,steps=100,radius=.006):
    out=Path(out)
    if out.exists():saved=json.loads(out.read_text());n=np.asarray(saved['normals']);trace=saved['trace']
    else:n=np.asarray(json.loads(Path(source).read_text())['normals']) if str(source).endswith('.json') else read_h(source);trace=[]
    initial=n.copy();accepted=0;start=time.time()
    for it in range(steps):
        m,c=diagnostics(n);p,q=m['p'],m['q'];P=c['P']
        if len(P)==0 and len(c['Q'])==0:print('NUMERIC_ZERO_BARS_REQUIRES_EXACT_AUDIT',flush=True);break
        if len(P)!=1 or len(c['Q']):print('wrong entrance',len(P),len(c['Q']));break
        birth=P[0][1];a,b=P[0][2];proot=c['proot'];qroot=c['qroot']
        ip=np.array([i for i in range(len(p)) if i not in [birth,proot]]);iq=np.array([i for i in m['active'] if i!=qroot])
        wp=c['pw'][ip];wq=c['qw'][iq]
        ps=np.sum(p[ip]**2,axis=1);qs=np.sum(q[iq]**2,axis=1)
        def f(flat):
            nt=flat.reshape(n.shape);pt,qt,g=properties(nt,m)
            x,y=pt[a],pt[b];d=y-x;t=torch.clamp(-(x@d)/(d@d),0,1);dd=x+t*d
            loss=1-(dd@dd)/(pt[birth]@pt[birth])
            cp=(pt[ip]*(pt[wp]-pt[ip])).sum(dim=1)/torch.as_tensor(ps)
            cq=(qt[iq]*(qt[wq]-qt[iq])).sum(dim=1)/torch.as_tensor(qs)
            return torch.cat((loss.reshape(1),cp,cq))
        x=torch.tensor(n.flatten());val=f(x).detach().numpy();J=torch.func.jacrev(f)(x).detach().numpy()
        # Existing strict guards are protected; no guard preserves the unwanted U.
        target=np.minimum(val[1:]*.2,1e-7);target=np.maximum(target,1e-12)
        scale=np.repeat(np.linalg.norm(n,axis=1),3)
        r=radius;found=False
        for trial in range(5):
            opt=linprog(J[0]*scale,A_ub=-J[1:]*scale,b_ub=val[1:]-target,
                        bounds=[(-r,r)]*n.size,method='highs')
            if not opt.success: r*=.35;continue
            direction=(opt.x*scale).reshape(n.shape)
            pred=float(J[0]@direction.ravel())
            for alpha in [1,.5,.25,.125,.0625,.03125,.015625]:
                z=n+alpha*direction
                try:mm,cc=diagnostics(z)
                except (ValueError,AssertionError):continue
                score=sum(v[0] for v in cc['P']);old=P[0][0]
                if cc['E']<=249 and len(cc['Q'])==0 and cc['S']==1 and len(cc['P'])<=1 and cc['U']<=2 and cc['minQ']>1e-12 and cc['minP']>1e-12 and score<old-1e-11:
                    n=z;accepted+=1;found=True
                    trace.append(dict(step=len(trace),P=score,E=cc['E'],F=cc['F'],U=cc['U'],S=cc['S'],alpha=alpha,radius=r,predicted=pred,minP=cc['minP'],minQ=cc['minQ']))
                    out.write_text(json.dumps(dict(normals=n.tolist(),trace=trace,source=Path(source).name,parameters=dict(radius=radius,guard_target=1e-7,guard_floor=1e-12,classification_threshold=1e-10,bar_threshold=1e-12)),indent=2)+'\n')
                    if accepted%10==0:print(trace[-1],flush=True)
                    break
            if found:break
            r*=.35
        if not found:
            print('NO_ACCEPTED_STEP',it,c['P'],c['minQ'],c['minP'],flush=True);break
    _,cc=diagnostics(n);print('DONE',accepted,'P',cc['P'],'Q',cc['Q'],'SU',cc['S'],cc['U'],'EF',cc['E'],cc['F'],'sec',time.time()-start,flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 100,float(sys.argv[4]) if len(sys.argv)>4 else .006)
