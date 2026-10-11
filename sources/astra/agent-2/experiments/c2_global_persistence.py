"""Complete P/Q minimization with necessary axial global-extremum penalties.
All points/supports belong to one C2-symmetric physical hull; mass is recomputed.
Penalty residuals, bar residuals, and counts are reported separately. Only a
separate complete exact physical audit can accept an own110 candidate.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.spatial import QhullError
import jax
import jax.numpy as jnp
from support_persistence import ROOT
from c2_twisted_ladder import coordinates,NumericalGoal

def run(src,out,side='point'):
    if side=='point':from c2_twisted_ladder import state,physical,core
    elif side=='support':from c2_dual_morse import state,physical,core
    else:raise ValueError('explicit point or support family required')
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();q=np.load(src);(out/'source.npy').write_bytes(raw);(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),side=side),indent=2)+'\n');D=len(q);bounds=[(-4,1)]*3+[b for _ in range((D-3)//3) for b in [(-8,8),(-3,3),(-3,3)]]
    def global_penalty(q,T,R,A):
        X,Z,Y,g,v,raw=physical(q,T,R) if side=='point' else physical(q,R,T,A)
        z=jnp.sum(Z*Z,1);y=jnp.sum(Y*Y,1);p=jnp.maximum(z[1:]/z[0]-1+1e-7,0);s=jnp.maximum(y[1:]/y[0]-1+1e-7,0);return jnp.sum(p*p)+jnp.sum(s*s)
    gp=jax.jit(jax.value_and_grad(global_penalty))
    for stage,weight in enumerate([.1,1.,10.,100.,10.,1.,.1]):
        folder=out/f'stage{stage}';folder.mkdir();best=np.inf;fewest=(999,np.inf);calls=0;history=[];start=time.time()
        def eval(q):
            nonlocal best,fewest,calls
            try:
                s=state(q);A=s['active'] if side=='support' else np.array([],int)
                value,gradient=core(q,s['T'],s['R'],s['bp'],s['bw'],s['bq'],s['qw'],-1.) if side=='point' else core(q,s['R'],s['T'],A,s['bp'],s['bw'],s['bq'],s['qw'],-1.)
                global_value,gg=gp(q,s['T'],s['R'],A);value=float(value);global_value=float(global_value);cost=value+weight*global_value;gradient=np.asarray(gradient)+weight*np.asarray(gg)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):return 1e4,np.zeros_like(q)
            calls+=1;row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','loss','centroid','volume']};row.update(calls=calls,global_penalty=global_value,weight=weight,objective=cost,seconds=time.time()-start)
            if cost<best:best=cost;np.save(folder/'best_q.npy',q);np.save(folder/('best_points.npy' if side=='point' else 'best_supports.npy'),np.asarray(coordinates(q)));(folder/'best.json').write_text(json.dumps(row,indent=2)+'\n')
            key=(s['S']+s['U'],s['loss'])
            if key<fewest:
                fewest=key;history.append(row);np.save(folder/'fewest_q.npy',q);(folder/'fewest.json').write_text(json.dumps(row,indent=2)+'\n');print('C2_GLOBAL_PERSISTENCE_FEWEST',row,flush=True)
            if s['S']==s['U']==1 and 17<=s['E']<=248:
                np.save(folder/'NUMERICAL_NOMINATION_q.npy',q);np.save(folder/'NUMERICAL_NOMINATION_physical.npy',np.asarray(coordinates(q)));(folder/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');raise NumericalGoal()
            if calls%400==0:print('C2_GLOBAL_PERSISTENCE_CALLS',stage,calls,best,fewest,flush=True)
            return cost,gradient
        try:opt=minimize(eval,q,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=800,maxls=40,maxcor=15,ftol=1e-13,gtol=1e-10))
        except NumericalGoal:(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(dict(folder=str(folder),side=side),indent=2)+'\n');print('C2_GLOBAL_NUMERICAL_REQUIRES_EXACT',str(folder),flush=True);return
        q=np.load(folder/'best_q.npy');(folder/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('C2_GLOBAL_PERSISTENCE_STAGE_DONE',stage,best,fewest,opt.message,flush=True)
    (out/'FINITE_SEARCH_END.json').write_text(json.dumps(dict(side=side,goal_complete=False),indent=2)+'\n')

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],sys.argv[3] if len(sys.argv)>3 else 'point')
