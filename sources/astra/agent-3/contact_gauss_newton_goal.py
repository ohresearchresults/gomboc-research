"""Full physical Figure feasibility by nonlinear least-squares contact steps.

Every exact contact equation is built into the rational chart. All noncontact
convexity signs, oriented face turns, own-centroid facet-foot and vertex-edge
signs enter the residual. A small residual is never accepted as a body or an
equilibrium cancellation. Any valid numerical110 is immediately exact-audited.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse import csr_matrix
from contact_numpy import Chart
from contact_physical_110 import PhysicalGuards,freeze
from contact_quota_polish import metric

def run(source,parameters,out,epochs=16,evaluations=100):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);c=Chart(source);assert c.meta['E']<=248;q=np.load(parameters).copy();np.save(out/'initial_q.npy',q);(out/'construction.json').write_bytes(Path(source).read_bytes());G=PhysicalGuards(c,True);rows=[];start=time.time();serial=0;trust=.03
    for epoch in range(epochs):
        base=q.copy();g=c.physical(base,require_valid=False);W=metric(c,g);cache={};trace=[]
        def evaluate(y):
            nonlocal serial
            if 'y'in cache and np.array_equal(y,cache['y']):return cache['r'],cache['J']
            qq=base+W@y;g=c.physical(qq,require_valid=False);v,J,t,JT,cl=G.evaluate(g);gap=g['noncontact'];values=np.r_[gap,t,v];targets=np.r_[np.full(len(gap),1e-9),np.full(len(t),1e-10),np.full(len(v),1e-8)];derivatives=np.vstack((g['Dgap'][~c.incidence],JT,J))@W;weights=np.r_[np.full(len(gap),4.),np.full(len(t),2.),np.ones(len(v))]/1e-4;active=values<targets;r=np.maximum(targets-values,0)*weights;JJ=-derivatives*(weights*active)[:,None];serial+=1
            row=dict(epoch=epoch,evaluation=serial,merit=float(r@r),valid=bool(g['valid']),gap=float(min(gap)),turn=float(min(t)),seconds=time.time()-start,**cl);trace.append(row);np.save(out/'latest_q.npy',qq);(out/'latest.json').write_text(json.dumps(row,indent=2))
            if serial%20==0:print('CONTACT_GAUSS_NEWTON',out,row,flush=True)
            if g['valid']and cl['S']==cl['U']==1:freeze(c,qq,out/f'exact_nomination_{serial:06d}')
            cache.update(y=y.copy(),r=r,J=csr_matrix(JJ));return r,cache['J']
        def fun(y):return evaluate(y)[0]
        def jac(y):return evaluate(y)[1]
        radius=trust/np.sqrt(c.d)
        try:sol=least_squares(fun,np.zeros(c.d),jac=jac,bounds=(-radius,radius),method='trf',tr_solver='lsmr',ftol=1e-12,xtol=1e-12,gtol=1e-12,max_nfev=evaluations,tr_options=dict(atol=1e-12,btol=1e-12,maxiter=500))
        except(ValueError,np.linalg.LinAlgError)as e:
            (out/f'epoch{epoch:02d}_error.json').write_text(json.dumps(dict(error=str(e),scope='undefined nonlinear proposal rejected; previous epoch body retained'),indent=2));trust*=.3;continue
        q=base+W@sol.x;np.save(out/f'epoch{epoch:02d}_q.npy',q);(out/f'epoch{epoch:02d}_trace.json').write_text(json.dumps(trace,indent=2));row=dict(epoch=epoch,cost=float(sol.cost),optimality=float(sol.optimality),evaluations=sol.nfev,status=int(sol.status),message=sol.message,trust=trust,seconds=time.time()-start);rows.append(row);(out/'epochs.json').write_text(json.dumps(rows,indent=2));print('CONTACT_GAUSS_NEWTON_EPOCH',out,row,flush=True)
        if np.linalg.norm(sol.x)>radius*.5:trust=min(.15,trust*1.4)
        else:trust*=.7
    np.save(out/'endpoint_q.npy',q);print('CONTACT_GAUSS_NEWTON_FINITE_STOP',out,rows[-1]if rows else None,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('parameters');p.add_argument('out');p.add_argument('--epochs',type=int,default=16);p.add_argument('--evaluations',type=int,default=100);a=p.parse_args();run(a.source,a.parameters,a.out,a.epochs,a.evaluations)
