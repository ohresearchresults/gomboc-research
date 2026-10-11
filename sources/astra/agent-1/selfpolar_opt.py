"""Finite self-polar realization-space optimization; output still requires full audit."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,torch,json,pathlib,time,argparse
from scipy.optimize import minimize
from selfpolar_search import mesh_indexed,stats,balance
from persistence_search import pairs

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
def optimize(X,out,iters=500,kind='log'):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);n=len(X);m,mp,tri,ed=mesh_indexed(X)
 aa,bb=np.triu_indices(n,1);initial=X@X.T+1;on=initial[aa,bb]<1e-7;off=~on;ca,cb=aa[on],bb[on];ia,ib=aa[off],bb[off]
 print('STRUCTURE',n,len(ca),len(ia),'centroid',stats(X)['g'],flush=True)
 tt=torch.tensor(tri);cache={};history=[];t0=time.time();calls=0
 def calc(z):
  x=z.reshape(n,3);T=x[tt];v=(T[:,0]*torch.linalg.cross(T[:,1],T[:,2])).sum(1)/6;g=(v[:,None]*T.sum(1)).sum(0)/(4*v.sum())
  return torch.cat([g,v])
 def get(z):
  if cache.get('z') is None or not np.array_equal(cache['z'],z):
   x=z.reshape(n,3);zz=torch.tensor(z);allv=calc(zz).detach().numpy();J=torch.func.jacrev(calc)(zz).detach().numpy()
   eq=np.r_[(x[ca]*x[cb]).sum(1)+1,allv[:3]];eqJ=np.zeros((len(ca)+3,z.size))
   for k in range(3):eqJ[np.arange(len(ca)),3*ca+k]=x[cb,k];eqJ[np.arange(len(ca)),3*cb+k]=x[ca,k]
   eqJ[-3:]=J[:3]
   ineq=np.r_[(x[ia]*x[ib]).sum(1)+1-1e-8,allv[3:]-1e-10];iqJ=np.zeros((len(ia)+len(tri),z.size))
   for k in range(3):iqJ[np.arange(len(ia)),3*ia+k]=x[ib,k];iqJ[np.arange(len(ia)),3*ib+k]=x[ia,k]
   iqJ[len(ia):]=J[3:]
   pp,_=pairs(x-allv[:3],ed);zzt=torch.tensor(z,requires_grad=True);xt=zzt.reshape(n,3);g=calc(zzt)[:3];p=xt-g
   if len(pp):
    bi=torch.tensor(pp[:,0]);ee=torch.tensor(ed[pp[:,1]]);a=p[ee[:,0]];d=p[ee[:,1]]-a;t=(-(a*d).sum(1)/(d*d).sum(1).clamp(min=1e-30)).clamp(0,1);death=((a+t[:,None]*d)**2).sum(1);birth=(p[bi]**2).sum(1);bars=(1-death/birth).clamp(min=0)
    f=torch.log1p(bars/.005).sum()*.005 if kind=='log' else bars.sum()
   else:f=p.sum()*0
   fgrad=torch.autograd.grad(f,zzt)[0].detach().numpy();cache.update(z=z.copy(),eq=eq,eqJ=eqJ,ineq=ineq,iqJ=iqJ,f=float(f.detach()),grad=fgrad,barcount=len(pp))
  return cache
 def fun(z):
  nonlocal calls
  calls+=1;d=get(z)
  if calls%20==1:print('EVAL',calls,'loss',d['f'],'bars',d['barcount'],'eq',float(abs(d['eq']).max()),'slack',float(d['ineq'].min()),'s',time.time()-t0,flush=True)
  return d['f'],d['grad']
 def callback(z):
  d=get(z);row=dict(loss=d['f'],bars=d['barcount'],equality=float(abs(d['eq']).max()),slack=float(d['ineq'].min()),seconds=time.time()-t0);history.append(row)
  np.savez(out/'latest.npz',X=z.reshape(n,3),Q=-z.reshape(n,3));(out/'history.json').write_text(json.dumps(history,indent=2))
 res=minimize(fun,X.ravel(),jac=True,method='SLSQP',constraints=[{'type':'eq','fun':lambda z:get(z)['eq'],'jac':lambda z:get(z)['eqJ']},{'type':'ineq','fun':lambda z:get(z)['ineq'],'jac':lambda z:get(z)['iqJ']}],callback=callback,options={'maxiter':iters,'ftol':1e-12,'disp':True})
 Y=res.x.reshape(n,3);np.savez(out/'final.npz',X=Y,Q=-Y)
 record={'message':res.message,'nit':res.nit,'fun':float(res.fun),'eq':float(abs(get(res.x)['eq']).max()),'slack':float(get(res.x)['ineq'].min())}
 try:record['actual']=stats(Y)
 except Exception as e:record['actual_error']=str(e)
 (out/'result.json').write_text(json.dumps(record,indent=2));print(json.dumps(record),flush=True)
 return Y
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--iters',type=int,default=500);ap.add_argument('--kind',default='log');a=ap.parse_args();optimize(np.load(a.input)['X'],a.out,a.iters,a.kind)
