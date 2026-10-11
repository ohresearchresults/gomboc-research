"""Own-filled-mass support-deletion repair with additive adjacent rooted forests.
Finite numerical searches only; no optimization outcome is an exact certificate.
Input: GENERATOR.json plus complete exact A.json. Depends on active_repair.py and
its hash-checked persisted S8 source tree. All nonlinear checks recompute COM.
"""
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog,minimize
from scipy.sparse import csr_matrix,hstack,vstack,eye
from active_repair import Atlas,mechanics

def paths(cos,root,mask,floors):
    n=len(cos);dist=np.full(n,np.inf);dist[root]=0.
    done=np.zeros(n,bool);parent=np.full(n,-1,int)
    costs=np.maximum(floors[:,None]-cos,0.)**2;costs[~mask]=np.inf
    for _ in range(n):
        i=int(np.argmin(np.where(done,np.inf,dist)))
        assert not done[i] and np.isfinite(dist[i]);done[i]=True
        cand=dist[i]+costs[:,i];improve=(~done)&(cand<dist)
        dist[improve]=cand[improve];parent[improve]=i
    parent[root]=root
    for k in range(n):
        seen=set();j=k
        while j!=root:
            assert 0<=j<n and j not in seen;seen.add(j);j=int(parent[j])
    return parent,dist

def run(a):
    inp,out=a.input.resolve(),a.out.resolve();out.mkdir(parents=True,exist_ok=False)
    d=json.loads((inp/'GENERATOR.json').read_text());ar=json.loads((inp/'A.json').read_text());fs=ar['faces']
    m=Atlas(d,fs,stable=a.sroot,unstable=a.uroot);u=m.u0.copy();np_=m.np
    um=np.zeros((len(m.owners),len(m.owners)),bool);sm=np.zeros((m.nphys,m.nphys),bool)
    for (i,j),ff in m.ef.items():um[i,j]=um[j,i]=True;sm[tuple(ff)]=sm[tuple(ff[::-1])]=True
    sf=np.full(m.nphys,a.goal);uf=np.full(len(m.owners),a.goal)
    def assign(s):
        m.uparent,_=paths(s['cu'],m.Uroot,um,uf);m.sparent,_=paths(s['cs'],m.Sroot,sm,sf)
    st=m.state(u,False);assign(st);st=m.state(u,False)
    floors=np.maximum(a.goal,np.minimum(a.floor_fraction*st['vals'],a.floor_cap))
    sf[m.si]=floors[:len(m.si)];uf[m.ui]=floors[len(m.si):]
    good=st['vals']>0
    def merit(s):
        r=np.maximum(floors-s['vals'],0)
        if a.mode in ('linear','hardgood'):v=r.sum()
        elif a.mode=='maxmin':v=r.max()
        else:v=np.linalg.norm(r)
        return float(v+100*np.maximum(a.gapfloor-s['gaps'][~m.inc],0).sum()+100*np.maximum(a.tetrafloor-s['det'],0).sum())
    hist=[];t0=time.monotonic();trust=a.trust
    for it in range(a.steps):
        st=m.state(u,False);assign(st);st=m.state(u);loss=merit(st)
        rec=dict(it=it,loss=loss,minexit=float(st['vals'].min()),negative=int((st['vals']<=0).sum()),mingap=float(st['gaps'][~m.inc].min()),minheight=float(st['h'].min()),trust=trust)
        hist.append(rec);(out/'history.json').write_text(json.dumps(hist,sort_keys=True,separators=(',',':')));(out/'floors.json').write_text(json.dumps(floors.tolist()))
        if it%5==0:print(out.name,rec,flush=True)
        if st['vals'].min()>0 and loss<1e-12:print('NUMERICAL_POSITIVE_FORESTS',out.name,flush=True);break
        geom=np.r_[st['dq'].reshape(-1,np_)/2,st['dP'].reshape(-1,np_)]
        _,ss,Vt=svd(geom,full_matrices=False,check_finite=False);W=Vt.T/np.maximum(ss,a.svd_floor)
        vi,qi=np.where((~m.inc)&(st['gaps']<a.gapcut))
        J=st['J']@W;G=np.r_[m.gap_jac(st,vi,qi),st['ddet']]@W
        gb=np.r_[a.gapfloor-st['gaps'][vi,qi],a.tetrafloor-st['det']]
        b=floors-st['vals'];nrows=len(b)
        if a.mode=='quadratic':
            A=np.r_[J,10*G];bb=np.r_[b,10*gb]
            def fun(z):
                r=np.maximum(bb-A@z,0);return .5*(r@r+a.ridge*(z@z)),-A.T@r+a.ridge*z
            rr=minimize(fun,np.zeros(np_),jac=True,method='L-BFGS-B',bounds=[(-trust,trust)]*np_,options=dict(maxiter=300,ftol=1e-15,gtol=1e-11,maxls=40,maxcor=30))
            z=rr.x;status=str(rr.message)
        elif a.mode=='maxmin':
            mat=np.r_[np.c_[-J,-np.ones(nrows)],np.c_[-G,np.zeros(len(G))]]
            rr=linprog(np.r_[np.zeros(np_),1.],A_ub=mat,b_ub=-np.r_[b,gb],bounds=[(-trust,trust)]*np_+[(0,None)],method='highs',options=dict(dual_feasibility_tolerance=1e-9,primal_feasibility_tolerance=1e-9,threads=1,time_limit=8.))
            status=str(rr.message);z=rr.x[:np_] if rr.success else None
        else:
            slackidx=np.where(~good)[0] if a.mode=='hardgood' else np.arange(nrows)
            ns=len(slackidx);I=np.zeros((nrows,ns));I[slackidx,np.arange(ns)]=-1
            mat=np.r_[np.c_[-J,I],np.c_[-G,np.zeros((len(G),ns))]]
            rr=linprog(np.r_[np.zeros(np_),np.ones(ns)],A_ub=mat,b_ub=-np.r_[b,gb],bounds=[(-trust,trust)]*np_+[(0,None)]*ns,method='highs',options=dict(dual_feasibility_tolerance=1e-9,primal_feasibility_tolerance=1e-9,threads=1,time_limit=8.))
            status=str(rr.message);z=rr.x[:np_] if rr.success else None
        if z is None:
            print('LINEAR_FAILURE',it,status,flush=True);break
        du=W@z;accepted=False
        for ls in range(a.max_linesearch):
            step=2.**(-ls)
            try:sn=m.state(u+step*du,False)
            except (np.linalg.LinAlgError,ValueError,FloatingPointError):continue
            newloss=merit(sn)
            feasible=sn['h'].min()>.02 and sn['gaps'][~m.inc].min()>=a.gapfloor*.5 and sn['det'].min()>=a.tetrafloor*.5
            if a.mode=='hardgood':feasible=feasible and np.all(sn['vals'][good]>0)
            if feasible and np.isfinite(newloss) and newloss<loss*(1-1e-6*step):
                u+=step*du;rec.update(step=step,linear_status=status);accepted=True;m.save(u,out/'CHECKPOINT.json');break
        if not accepted:
            trust*=.2
            if trust<a.min_trust:print('NO_IMPROVEMENT',it,status,flush=True);break
        elif a.adapt_trust:
            trust=min(a.trust,trust*(1.5 if ls<2 else .8 if ls>5 else 1.))
    st=m.state(u,False);assign(st);st=m.state(u,False)
    m.save(u,out/'GENERATOR.json');(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')))
    rm=Atlas(json.loads((out/'GENERATOR.json').read_text()),fs,stable=m.Sroot,unstable=m.Uroot);rs=rm.state(rm.u0,False)
    rep=mechanics(rs['q'],fs,P=rs['P'],tol=1e-12)
    def dump(n,x):(out/n).write_text(json.dumps(x,sort_keys=True,separators=(',',':')))
    dump('NUMERICAL.json',rep);dump('history.json',hist);dump('METHOD.json',{k:str(v) if isinstance(v,Path) else v for k,v in vars(a).items()});dump('floors.json',floors.tolist())
    print('FINAL',out.name,'counts',[len(rep[k]) for k in ('S','U','H')],'minexit',float(st['vals'].min()),'negative',int((st['vals']<=0).sum()),'sec',time.monotonic()-t0,flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('out',type=Path)
    p.add_argument('--mode',choices=['quadratic','linear','hardgood','maxmin'],default='hardgood');p.add_argument('--steps',type=int,default=100);p.add_argument('--goal',type=float,default=1e-7);p.add_argument('--trust',type=float,default=.01);p.add_argument('--ridge',type=float,default=1e-6);p.add_argument('--sroot',type=int,default=3);p.add_argument('--uroot',type=int,default=None)
    p.add_argument('--floor-fraction',type=float,default=.1);p.add_argument('--floor-cap',type=float,default=1e-4);p.add_argument('--gapfloor',type=float,default=1e-7);p.add_argument('--tetrafloor',type=float,default=1e-10);p.add_argument('--svd-floor',type=float,default=1e-7);p.add_argument('--gapcut',type=float,default=.03);p.add_argument('--max-linesearch',type=int,default=24);p.add_argument('--min-trust',type=float,default=1e-9);p.add_argument('--adapt-trust',action='store_true');run(p.parse_args())
