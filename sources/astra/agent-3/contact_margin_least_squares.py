"""Nonlinear margin growth, with every accepted physical own-census saved.

Temporary nonlinear proposals need not satisfy the desired census. Only
strict physical own110 states are eligible as the saved margin incumbent.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from contact_numpy import Chart
from contact_quota_polish import metric,guards
from exact_contact_audit import audit
from exact_barcode_report import report

def run(source,out,epochs,target):
 c=Chart(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=c.q0.copy();g=c.physical(q);v,_,cl=guards(c,g,1,1);assert cl==[1,1];best=float(min(v));np.save(out/'best_q.npy',q);(out/'source_construction.json').write_bytes(Path(source).read_bytes());start=time.time();calls=0;rows=[]
 for epoch in range(epochs):
  d=out/f'epoch{epoch:02d}';d.mkdir();base=q.copy();gg=c.physical(base,require_valid=False);W=metric(c,gg);cache={};trust=.3/np.sqrt(c.d)
  def compute(z):
   nonlocal best,calls
   if 'z'in cache and np.array_equal(cache['z'],z):return cache['r'],cache['J']
   calls+=1;qq=base+W@z;g=c.physical(qq,require_valid=False);v,J,cl=guards(c,g,1,1);gapmat=np.where(c.incidence,np.inf,g['gap']);which=gapmat.argmin(1);gap=gapmat[np.arange(c.F),which];Jgap=g['Dgap'][np.arange(c.F),which];T=c.T;X=g['X'];DX=g['DX'];a,b,cc=X[T[:,0]],X[T[:,1]],X[T[:,2]];da,db,dc=DX[T[:,0]],DX[T[:,1]],DX[T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,cc));Dv6=np.einsum('ic,icp->ip',np.cross(b,cc),da)+np.einsum('ic,icp->ip',np.cross(cc,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc);den=g['den'];Dden=-np.einsum('fcp,c->fp',g['DY'],g['centroid'])-g['Y']@g['Dcentroid'];values=np.r_[v,gap,v6,den];floor=np.r_[np.full(len(v),target),np.full(c.F,1e-7),np.full(len(v6),1e-8),np.full(c.F,1e-4)];scales=np.r_[np.full(len(v),target),np.full(c.F,.0001),np.full(len(v6),.0001),np.full(c.F,.001)];JJ=np.vstack((J,Jgap,Dv6,Dden));active=values<floor;r=np.maximum(floor-values,0)/scales;DJ=-(JJ@W)/scales[:,None]*active[:,None]
   if g['valid']and cl==[1,1]and min(v)>best:
    best=float(min(v));np.save(out/'best_q.npy',qq);(out/'best.json').write_text(json.dumps(dict(epoch=epoch,calls=calls,margin=best,gap=float(min(g['noncontact'])),seconds=time.time()-start),indent=2))
   if calls%25==0:print('MARGIN_LS',dict(epoch=epoch,calls=calls,cost=float(r@r),best_margin=best,S=cl[1],U=cl[0],valid=bool(g['valid']),seconds=time.time()-start),flush=True)
   cache.update(z=z.copy(),r=r,J=DJ);return r,DJ
  try:
   r=least_squares(lambda z:compute(z)[0],np.zeros(c.d),jac=lambda z:compute(z)[1],bounds=(-trust,trust),method='trf',max_nfev=100,ftol=1e-11,gtol=1e-11,xtol=1e-11);q=base+W@r.x;np.save(d/'endpoint_q.npy',q);g=c.physical(q,require_valid=False);v,_,cl=guards(c,g,1,1);row=dict(epoch=epoch,cost=float(r.cost),S=cl[1],U=cl[0],valid=bool(g['valid']),margin=float(min(v)),best_margin=best,message=r.message,nfev=r.nfev);rows.append(row);(out/'epochs.json').write_text(json.dumps(rows,indent=2));print('MARGIN_LS_EPOCH',row,flush=True)
   if g['valid']and min(v)>target*.95 and cl==[1,1]:break
  except (ValueError,np.linalg.LinAlgError)as err:
   (d/'ERROR.json').write_text(json.dumps(dict(error=repr(err),scope='finite nonlinear solve failed; no invalid proposal accepted')));break
 a=audit(source,out/'best_q.npy',out/'exact_best_g15',10**15);report(out/'exact_best_g15');s=json.loads((out/'exact_best_g15/summary.json').read_text());print('MARGIN_LS_EXACT',{k:s[k]for k in ['V','E','F','counts','weak','goal_met']},flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--epochs',type=int,default=10);p.add_argument('--target',type=float,default=1e-4);a=p.parse_args();run(a.source,a.out,a.epochs,a.target)
