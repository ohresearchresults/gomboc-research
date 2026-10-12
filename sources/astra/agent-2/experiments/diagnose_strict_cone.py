"""Explicit linearized physical constraint multipliers for a saved own211 body."""
import sys,json,numpy as np,jax,jax.numpy as jnp
from pathlib import Path
from scipy.linalg import svd
from scipy.optimize import linprog
from canonical_atlas import ROOT,Chart
from support_persistence import barcode
from geometry import angular_scores
from io import BytesIO
f=ROOT/sys.argv[1];inp=f/sys.argv[2];out=f/sys.argv[3];out.mkdir(exist_ok=False);b=inp.read_bytes();(out/'source_q.npy').write_bytes(b);q=np.load(BytesIO(b));c=Chart(f);V,F=c.meta['V'],c.F;D=len(q);flat=np.flatnonzero(~c.incidence.ravel());K=len(flat);nm=V+F;g=c.graph(q);ur=int(np.argmax((g['Z']**2).sum(1)));sr=int(np.argmax((g['Q']**2).sum(1)));bp,bw,bb=barcode(g['Q'],np.ones(F),c.es);child=int(bp[np.argmax(bb),0]);active=np.ones(nm,bool);active[[ur,V+sr,V+child]]=False;up=angular_scores(g['Z']).argmax(1);sp=angular_scores(g['Q']).argmax(1)
def pieces(q):
 X,Y,Z,Q,cent,vol,gap=c.physical(q)
 def angles(A,p):
  d=A[p]-A;return jnp.sum(A*d,axis=1)/jnp.sqrt(jnp.maximum(jnp.sum(A*A,axis=1)*jnp.sum(d*d,axis=1),1e-40))
 return jnp.concatenate([gap.ravel()[flat],angles(Z,up),angles(Q,sp),X.ravel(),Y.ravel()])
J=np.asarray(jax.jacfwd(pieces)(q));raw=np.asarray(pieces(q));cost,grad=c.lossgrad(q,g['bp'],g['bw'],g['bq'],g['qw'],-1.,0.);jp=J[K+nm:];metric=np.vstack([jp[:3*V]/np.sqrt(np.mean(g['X']**2)),jp[3*V:]/np.sqrt(np.mean(g['Y']**2)),np.eye(D)*.05]);_,dd,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/dd;C=np.vstack([J[:K],J[K:K+nm][active]])@W;rhs=np.r_[raw[:K]-1e-8,raw[K:K+nm][active]-1e-7];trust=.02;bound=trust/np.sqrt(D);keep=rhs<=bound*np.sum(abs(C),axis=1)+1e-10;ids=np.flatnonzero(keep);C=C[keep];rhs=rhs[keep];scale=np.r_[np.ones(K),np.full(active.sum(),1000.)][keep];lp=linprog(np.asarray(grad)@W,A_ub=-C*scale[:,None],b_ub=rhs*scale,bounds=[(-bound,bound)]*D,method='highs-ipm',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-9});assert lp.success,lp.message
rows=[]
for k,idx in enumerate(ids):
 if idx<K:node=int(flat[idx]//V);other=int(flat[idx]%V);kind='noncontact'
 else:
  z=int(np.flatnonzero(active)[idx-K]);kind='U_guard' if z<V else 'S_guard';node=z if z<V else z-V;other=int(up[z]) if z<V else int(sp[z-V])
 rows.append(dict(kind=kind,node=node,other=other,slack=float(rhs[k]),multiplier=float(-lp.ineqlin.marginals[k]*scale[k]),row_norm=float(np.linalg.norm(C[k]))))
rows.sort(key=lambda a:a['multiplier'],reverse=True);res=dict(cost=float(cost),directional_derivative=float(lp.fun),kept_constraints=len(C),roots=dict(U=ur,S=[sr,child]),rows=rows);(out/'report.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({**res,'rows':rows[:24]},indent=2))
