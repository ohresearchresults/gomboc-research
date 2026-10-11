"""Finite LP nominations for all genuine cross-component physical chords.
The linear prediction is never accepted as a physical transfer. Its sole role
is to select nonlinear experiments with full re-hull and own-mass verification.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.linalg import svd
import jax,jax.numpy as jnp
from free_hull_metric121 import state,physical,jacobian,embedding_jac
from basin_transfer121 import reachable
from geometry import angular_scores
from support_persistence import ROOT

@jax.jit
def chords(X,T,pairs):
    Z,Q,g,v=physical(X,T);a=Z[pairs[:,0]];b=Z[pairs[:,1]];d=b-a
    return jnp.sum(a*d,1)/jnp.sqrt(jnp.sum(a*a,1)*jnp.sum(d*d,1))
jacchords=jax.jit(jax.jacfwd(chords,argnums=0))

def run(src,out,elder=0,trust=.1,eps=5e-8):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();X=np.load(src);s=state(X);n=len(X);D=3*n;valid=np.zeros(n,bool);valid[np.unique(s['T'])]=True;seen,sc=reachable(s['Z'],elder,.5*eps);pairs=np.array([(i,j) for i in np.flatnonzero(valid&~seen) for j in np.flatnonzero(valid&seen)],int);np.save(out/'source.npy',X)
    scores=angular_scores(s['Z']);scores[np.ix_(seen,~seen)]=-np.inf;scores[:,~valid]=-np.inf;up=scores.argmax(1);guards=s['guards'].copy();guards[:n]=scores[np.arange(n),up]
    J=np.asarray(jacobian(X,s['T'],up,s['sp'],s['p'],s['w'])).reshape(-1,D);K=np.asarray(embedding_jac(X,s['T'])).reshape(-1,D);M=np.vstack([K[:D]/np.sqrt(np.mean(s['Z']**2)),K[D:]/np.sqrt(np.mean(s['Q']**2)),np.eye(D)*.05]);_,d,Vt=svd(M,full_matrices=False,check_finite=False);W=Vt.T/d
    C=J[:-1][s['active']]@W;rhs=guards[s['active']]-eps;bound=trust/np.sqrt(D);keep=rhs<=bound*np.sum(abs(C),1)+1e-10;C=C[keep];rhs=rhs[keep]
    val=np.asarray(chords(X,s['T'],pairs));G=np.asarray(jacchords(X,s['T'],pairs)).reshape(len(pairs),D)@W;rows=[];start=time.time()
    for k,(i,j) in enumerate(pairs):
        opt=linprog(-G[k],A_ub=-C*1000,b_ub=rhs*1000,bounds=[(-bound,bound)]*D,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=5.))
        row=dict(child=int(i),parent=int(j),cross=float(val[k]),lp_success=bool(opt.success))
        if opt.success:row.update(predicted_cross=float(val[k]+G[k]@opt.x),predicted_gain=float(G[k]@opt.x))
        else:row['message']=opt.message
        rows.append(row)
        if k%100==0:print('CROSS_LP',k,'of',len(pairs),'seconds',time.time()-start,flush=True)
    rows.sort(key=lambda x:x.get('predicted_cross',-1e100),reverse=True);meta=dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),elder=elder,trust=trust,eps=eps,V=s['V'],E=s['E'],F=s['F'],S=s['S'],U=s['U'],initial_reachable=np.flatnonzero(seen&valid).tolist(),linear_only=True,rows=rows,seconds=time.time()-start);(out/'nominations.json').write_text(json.dumps(meta,indent=2)+'\n');print('LINEAR_ONLY_TOP',rows[:10],flush=True)
    return rows
if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2])
