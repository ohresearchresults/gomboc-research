"""Release every support direction and offset with <=84 supplied supports.
Generic full-dimensional hulls have E<=3F-6<=246; final exact counts are separate.
Own uniform mass and all persistence bars are recomputed for every evaluation.
"""
import sys,json,time,hashlib,numpy as np
from pathlib import Path
from scipy.optimize import minimize
from scipy.spatial import QhullError
from gmpy2 import mpq
import jax,jax.numpy as jnp
from support_persistence import ROOT,barcode,edge_graphs
from support_search import complex_for
from support_forest import points
sys.set_int_max_str_digits(0)
@jax.jit
def valuegrad(Y,ds,tr,tm,p,wp,q,wq,eta):
 def fun(H):
  X=jnp.linalg.solve(H[ds],jnp.ones((len(ds),3,1))).squeeze(-1);a,b,c=X[tr[:,0]],X[tr[:,1]],X[tr[:,2]];six=jnp.sum(a*jnp.cross(b,c),axis=1)*tm;g=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*six.sum());Z=X-g;Q=H/(1-H@g)[:,None]
  def loss(A,pp,w):
   root,a,b=A[pp[:,0]],A[pp[:,1]],A[pp[:,2]];d=b-a;t=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.maximum(jnp.sum(d*d,axis=1),1e-40),0,1);birth=jnp.sum(root*root,axis=1);depth=jnp.maximum(birth-jnp.sum((a+t[:,None]*d)**2,axis=1),0)*w/birth;return jnp.sum(jnp.log1p(depth/eta))
  return loss(Z,p,wp)+loss(Q,q,wq)
 return jax.value_and_grad(fun)(Y)
def geometry(H,eta):
 ds,xm,tr,tm,ym=complex_for(H);Z,Q=points(H,ds,tr,tm);eu,es=edge_graphs(ds,xm);p,wp,P=barcode(Z,xm,eu)
 # Pad unused supplied support vertices out of persistence via their valid edge graph.
 active=np.flatnonzero(ym);remap=np.full(len(H),-1,int);remap[active]=np.arange(len(active));qp,qw,Qb=barcode(Q[active],np.ones(len(active)),remap[es]);q=active[qp];q=np.vstack([q,np.tile(q[0],(len(H)-1-len(q),1))]);wq=np.r_[qw,np.zeros(len(H)-1-len(qw))];P=P/np.sum(Z[p[:len(P),0]]**2,1);Qb=Qb/np.sum(Q[active[qp[:,0]]]**2,1);v,G=valuegrad(H,ds,tr,tm,p,wp,q,wq,eta);info=dict(V=int(xm.sum()),F=int(ym.sum()),E_bound=int(xm.sum()+ym.sum()-2),Pmax=float(P.max()),Qmax=float(Qb.max()),loss=float(v),P=P.tolist(),Q=Qb.tolist());return float(v),np.asarray(G),info
def run(src,out,seed,jitter=1e-6):
 src=Path(src);out=Path(out);out.mkdir(exist_ok=False)
 if src.suffix=='.npy':H=np.load(src).copy()
 else:
  r=json.loads(src.read_text());cent=np.array([float(mpq(v)) for v in r['raw_centroid']]);H=np.array([[float(mpq(x,mpq(h))) for x in n] for n,h in zip(r['normals'],r['offsets'])]);H=H/(1-H@cent)[:,None]
 H/=np.sqrt(np.mean(H*H));assert len(H)<=84;rng=np.random.default_rng(seed);H+=rng.normal(size=H.shape)*jitter;np.save(out/'initial.npy',H);(out/'provenance.json').write_text(json.dumps(dict(source=str(src),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),seed=seed,initial_jitter=jitter),indent=2)+'\n');start=time.time();history=[]
 for k,eta in enumerate([1.,.3,.1,.03,.01,.003,.001,.0001,.00001]):
  d=out/f'stage{k}';d.mkdir();calls=0;best=[np.inf]
  def eval(flat):
   nonlocal calls
   A=flat.reshape(H.shape);calls+=1
   try:v,G,info=geometry(A,eta)
   except (ValueError,np.linalg.LinAlgError,QhullError,AssertionError):return 1e4,np.zeros_like(flat)
   if not np.isfinite(v) or not np.isfinite(G).all():return 1e4,np.zeros_like(flat)
   if v<best[0]:
    best[0]=v;np.save(d/'best.npy',A);info.update(calls=calls,seconds=time.time()-start);(d/'best.json').write_text(json.dumps(info,indent=2)+'\n')
   if max(info['Pmax'],info['Qmax'])<1e-10:np.save(d/f'NUMERICAL_NOMINATION_{calls}.npy',A)
   return v,G.ravel()
  opt=minimize(eval,H.ravel(),jac=True,method='L-BFGS-B',options=dict(maxiter=2500,maxls=60,maxcor=30,gtol=1e-11,ftol=1e-16));H=np.load(d/'best.npy');info=geometry(H,eta)[2];row=dict(stage=k,eta=eta,V=info['V'],F=info['F'],Pmax=info['Pmax'],Qmax=info['Qmax'],calls=calls,nit=int(opt.nit),seconds=time.time()-start,message=str(opt.message));history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('FREE_SUPPORT_STAGE',row,flush=True)
 np.save(out/'final.npy',H)

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]))
