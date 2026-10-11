# material-2bba40eb3411

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Live homogeneous H-chart continuation with at most 85 material supports.
Full normal/offset freedom; global witnesses reselected after every finite trial.
No reference centre is substituted for the filled centre. Numerical nomination.
"""
from pathlib import Path
import os,json,time,argparse
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np,torch as T
from scipy.optimize import minimize
import hsearch93 as H
from search93 import edges,bars
T.set_default_dtype(T.float64);T.set_num_threads(1)

def build(q,pquota=2,qquota=1):
 info,chart,points,(pe,qe)=H.state(q,graphs=True);tr,f,active=chart;P,Q=points
 ps=bars(P,pe);qs=bars(Q,qe);pairs=[];marg=[];allow=[]
 for X,bs,quota in[(P,ps,pquota),(Q,qs,qquota)]:
  root=[int(np.argmax((X*X).sum(1)))];root+= [v[1]for v in bs if v[1]not in root][:quota-1]
  score=X@X.T/(X*X).sum(1)[:,None]-1;np.fill_diagonal(score,-np.inf);idx=np.array([i for i in range(len(X))if i not in root]);w=np.argmax(score[idx],1);pairs.append(np.c_[idx,w]);marg.append(score[idx,w]);allow.append(root)
 return dict(q=q,tr=tr,f=f,active=active,P=P,Q=Q,pe=pe,qe=qe,pb=ps,qb=qs,pairs=pairs,marg=marg,info=info,allow=allow)

def values(q,s):
 P,Q,g,V,p=H.geometry(q,s['tr'],s['f'],s['active']);out=[]
 for X,bs,ed in[(P,s['pb'],s['pe']),(Q,s['qb'],s['qe'])]:
  val=X.sum()*0
  for depth,root,k in bs:
   i,j=ed[k];d=X[j]-X[i];t=T.clamp(-(X[i]*d).sum()/(d*d).sum(),0,1);lr=T.log((X[root]**2).sum()/((X[i]+t*d)**2).sum());val+=T.clamp(lr,min=1e-24)**.5
  out.append(val.reshape(1))
 for X,pr in zip((P,Q),s['pairs']):
  a=X[pr[:,0]];d=X[pr[:,1]]-a;out.append((a*d).sum(1)/(a*a).sum(1))
 return T.cat(out)

def derivative(q,s):
 x=T.tensor(q.ravel(),requires_grad=True);f=lambda x:values(x.reshape(q.shape),s);v=f(x).detach().numpy();j=T.autograd.functional.jacobian(f,x,vectorize=True).detach().numpy();assert np.isfinite(j).all();return v,j

def qp(desire,j,b,radius):
 norm=np.maximum(np.linalg.norm(j,axis=1),1e-14);A=j/norm[:,None];rhs=b/norm
 res=minimize(lambda x:(.5*np.dot(x-desire,x-desire),x-desire),np.zeros(len(desire)),jac=True,method='SLSQP',bounds=[(-radius,radius)]*len(desire),constraints={'type':'ineq','fun':lambda x:A@x-rhs,'jac':lambda x:A},options={'maxiter':150,'ftol':1e-12})
 if not np.isfinite(res.x).all()or np.min(A@res.x-rhs)<-1e-8:return None
 return res.x

def run(source,out,steps=100,radius=.03,minradius=1e-10,maxradius=.3,margin=1e-10,corrections=5,backtracks=7,pquota=2,qquota=1,pweight=1.,qweight=0.,drive=10.):
 q=np.array(json.loads(Path(source).read_text()),float);out=Path(out);out.mkdir(parents=True,exist_ok=True);trace=[];accepted=0;t0=time.monotonic();initial_radius=radius
 for it in range(steps+1):
  s=build(q,pquota,qquota);v,j=derivative(q,s);m=np.r_[*s['marg']];rec=dict(it=it,accepted=accepted,radius=radius,minP=float(s['marg'][0].min()),minQ=float(s['marg'][1].min()),energies=v[:2].tolist(),seconds=time.monotonic()-t0,**s['info']);trace.append(rec);print('HR',out.name,json.dumps(rec),flush=True);H.freeze(q,out/'FINAL.json');(out/'TRACE.json').write_text(json.dumps(trace,separators=(',',':'))+'\n')
  if it==steps or(s['info']['S']==1 and s['info']['U']==1):break
  target=np.full(len(m),margin);repair=m.min()<margin*(1-1e-6)
  gradient=pweight*j[0]+qweight*j[1];desire=np.zeros(q.size)if repair else-radius*drive*gradient/max(np.linalg.norm(gradient),1e-12)
  rhs=target-v[2:] if repair else np.minimum(target,v[2:])-v[2:];step=qp(desire,j[2:],rhs,radius);done=False
  if step is not None:
   for bt in range(backtracks):
    trial=q+2.**-bt*step.reshape(q.shape)
    try:
     for k in range(corrections):
      st=build(trial,pquota,qquota);mm=np.r_[*st['marg']]
      if mm.min()>=margin*(1-1e-6):break
      vv,jj=derivative(trial,st);dd=qp(np.zeros(q.size),jj[2:],1.01*margin-vv[2:],radius*.7)
      if dd is None:break
      trial+=dd.reshape(q.shape)
     st=build(trial,pquota,qquota);vv=values(T.tensor(trial),st).numpy();mm=np.r_[*st['marg']]
     better=mm.min()>m.min()+1e-14 if repair else pweight*(vv[0]-v[0])+qweight*(vv[1]-v[1])<-1e-11
     if mm.min()>=margin*(1-1e-6)and st['info']['S']<=qquota and st['info']['U']<=pquota and st['info']['E']<=249 and better:
      q=trial;accepted+=1;done=True;radius=min(maxradius,radius*1.2);H.freeze(q,out/f'PIN{accepted}.json');break
    except Exception:pass
  if not done:
   radius*=.5
   if radius<minradius:print('H_LOCAL_TRUST_STOP',flush=True);break
 (out/'PARAMETERS.json').write_text(json.dumps(dict(source=source,steps=steps,initial_radius=initial_radius,minradius=minradius,maxradius=maxradius,margin=margin,corrections=corrections,backtracks=backtracks,pquota=pquota,qquota=qquota,pweight=pweight,qweight=qweight,drive=drive),separators=(',',':'))+'\n');print('H_RETRACT_DONE',accepted,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=100);p.add_argument('--radius',type=float,default=.03);p.add_argument('--minradius',type=float,default=1e-10);p.add_argument('--maxradius',type=float,default=.3);p.add_argument('--margin',type=float,default=1e-10);p.add_argument('--corrections',type=int,default=5);p.add_argument('--backtracks',type=int,default=7);p.add_argument('--pquota',type=int,default=2);p.add_argument('--qquota',type=int,default=1);p.add_argument('--pweight',type=float,default=1.);p.add_argument('--qweight',type=float,default=0.);p.add_argument('--drive',type=float,default=10.);run(**vars(p.parse_args()))
