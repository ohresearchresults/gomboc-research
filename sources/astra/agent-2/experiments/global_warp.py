"""Global quadratic support deformations with actual homogeneous mass.
CMA nominates shapes; only a subsequent exact audit can establish the goal.
"""
import sys,json,time
from pathlib import Path
import numpy as np
import cma
from support_persistence import ROOT,complex_for,points,edge_graphs,barcode
from geometry import angular_scores

def family(Y,t):
    scale=np.mean(np.linalg.norm(Y,axis=1));u=Y/scale;x,y,z=u.T
    phi=np.array([x*x,y*y,z*z,x*y,x*z,y*z]).T
    a,b,c,d,e,f=t[3:9];M=np.array([[a,d,e],[d,b,f],[e,f,c]])
    return Y+scale*(t[:3]+u@M+phi@t[9:].reshape(6,3))

def assess(Y,tau=.03):
    ds,xm,tr,tm,ym=complex_for(Y);Z,Q=points(Y,ds,tr,tm);eu,es=edge_graphs(ds,xm);bu,wu,p=barcode(Z,xm,eu);bs,ws,q=barcode(Q,ym,es)
    p=np.array([v/np.dot(Z[r[0]],Z[r[0]]) for r,v in zip(bu,p)]);q=np.array([v/np.dot(Q[r[0]],Q[r[0]]) for r,v in zip(bs,q)])
    u=angular_scores(Z);u[:,xm==0]=-np.inf;u=u.max(axis=1);s=angular_scores(Q);s[:,ym==0]=-np.inf;s=s.max(axis=1)
    return float(np.log1p(p/tau).sum()+np.log1p(q/tau).sum()),{'S':int(((s<0)&(ym>0)).sum()),'U':int(((u<0)&(xm>0)).sum()),'V':int(xm.sum()),'F':int(ym.sum()),'Pmax':float(max(p)),'Qmax':float(max(q)),'floor':float(min(np.sort(u[xm>0])[1],np.sort(s[ym>0])[1]))}

if __name__=='__main__':
    seed=int(sys.argv[1]) if len(sys.argv)>1 else 1
    path=Path(sys.argv[2]) if len(sys.argv)>2 else ROOT/'artifacts/kf27d/supports.npy'
    Y0=np.load(path);out=ROOT/'artifacts/global_warp'/f'seed{seed}';out.mkdir(parents=True,exist_ok=True);np.save(out/'base.npy',Y0)
    best=np.inf;bestcount=10000;log=[];beg=time.time();calls=0;found=False
    for restart,sigma in enumerate([.005,.015,.05,.15]):
        es=cma.CMAEvolutionStrategy(np.zeros(27),sigma,{'seed':seed*100+restart,'popsize':36,'maxiter':500,'bounds':[-.6,.6],'verbose':-9,'verb_log':0,'verb_disp':0,'tolfun':1e-10})
        while not es.stop():
            candidates=es.ask();values=[]
            for t in candidates:
                Y=family(Y0,np.array(t));calls+=1
                try:cost,rec=assess(Y)
                except (ValueError,AssertionError,np.linalg.LinAlgError):cost=1e6;rec=None
                values.append(cost)
                if rec is not None and (cost<best or rec['S']+rec['U']<bestcount):
                    rec.update(cost=cost,restart=restart,calls=calls,seconds=time.time()-beg,coefficients=list(map(float,t)))
                    if cost<best:best=cost;np.save(out/'lowest_loss.npy',Y);(out/'lowest_loss.json').write_text(json.dumps(rec,indent=2)+'\n')
                    if rec['S']+rec['U']<bestcount:bestcount=rec['S']+rec['U'];np.save(out/'fewest_equilibria.npy',Y);(out/'fewest_equilibria.json').write_text(json.dumps(rec,indent=2)+'\n')
                    log.append(rec)
                if rec is not None and rec['S']==rec['U']==1 and rec['floor']>1e-10:
                    np.save(out/'numerical_target.npy',Y);(out/'numerical_target.json').write_text(json.dumps(rec,indent=2)+'\n');print('NUMERICAL_TARGET',out,flush=True);found=True;break
            if found:break
            es.tell(candidates,values)
            if es.countiter%50==0:print('WARP',seed,restart,es.countiter,'best',best,'minimum equilibria',bestcount,'seconds',time.time()-beg,flush=True)
        if found:break
        # Restart from the strongest physical candidate, allowing a new smooth chart.
        Y0=np.load(out/'lowest_loss.npy');np.save(out/f'base_restart{restart+1}.npy',Y0)
        print('RESTART_DONE',seed,restart,best,bestcount,flush=True)
    (out/'improvements.json').write_text(json.dumps(log,indent=2)+'\n')
