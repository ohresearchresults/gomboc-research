"""J91 full actual-hull finite outer growth with own-moment retraction.
Old rational-source vertices are fixed in the true old-centroid frame. New
points have positive chords to old points; this is a sufficient U1 condition
at exactly that centroid. Rebuilding the hull allows finite normal-fan changes.
All numeric outcomes require later exact rational reconstruction and census.
"""
from pathlib import Path
import sys,json
import numpy as np,torch
from scipy.optimize import linprog,minimize
from capflow91 import setup
from envelope91 import hullpoly,ref
from j90 import report,score
ROOT=Path(__file__).resolve().parent
torch.set_default_dtype(torch.float64);torch.set_num_threads(1)

def init():
 m=setup();W=np.array(json.loads((ROOT/'J91_CAPFLOW.json').read_text())['apexes']);return m,m['z']['x'],W

def chart(old,W):
 zz=hullpoly(np.vstack([old,W]));labs=zz['labels'];fs=[[labs[i] for i in f] for f in zz['faces'].values()];tri=[[f[0],f[j],f[j+1]] for f in fs for j in range(1,len(f)-1)]
 # A noncollinear supporting triple; selected by area, not arbitrary collinear prefix.
 ft=[];x=np.vstack([old,W])
 for f in fs:
  ts=np.array([[f[0],f[j],f[j+1]] for j in range(1,len(f)-1)]);a=x[ts];k=np.argmax(np.linalg.norm(np.cross(a[:,1]-a[:,0],a[:,2]-a[:,0]),axis=1));ft.append(ts[k])
 O=torch.tensor(old);T=torch.tensor(tri);FT=torch.tensor(np.array(ft))
 def fields(w):
  X=torch.cat([O,w]);a=X[FT];n=torch.linalg.cross(a[:,1]-a[:,0],a[:,2]-a[:,0]);h=(n*a[:,0]).sum(1);q=n/h[:,None]
  t=X[T];D=(t[:,0]*torch.linalg.cross(t[:,1],t[:,2])).sum(1);vol=D.sum()/6;M=(D[:,None]*t.sum(1)).sum(0)/24
  return q,M,vol
 return zz,fields

def retract(old,W,tol=2e-14,maxit=10):
 w=np.array(W,copy=True)
 for it in range(maxit):
  zz,fields=chart(old,w);a=torch.tensor(w);M=fields(a)[1].numpy()
  if np.max(abs(M))<=tol:return w,zz,True
  J=torch.func.jacrev(lambda v:fields(v)[1])(a).numpy().reshape(3,-1)
  if np.linalg.matrix_rank(J,tol=1e-12)<3:return w,zz,False
  d=np.linalg.lstsq(J,-M,rcond=None)[0].reshape(w.shape);prev=np.linalg.norm(M);accepted=False
  for bt in range(12):
   trial=w+d*2**-bt
   try:zt,ff=chart(old,trial);Mt=ff(torch.tensor(trial))[1].numpy()
   except Exception:continue
   if np.linalg.norm(Mt)<prev:
    w=trial;accepted=True;break
  if not accepted:return w,zz,False
 zz,_=chart(old,w);return w,zz,np.max(abs(zz['g']))<tol

def scout():
 m,old,W=init();z=hullpoly(np.vstack([old,W]));r=ref(z);vals=score(z['y']).max(1);nonroots=[i for i in np.argsort(vals) if i not in r['S']];chosen=nonroots[:4];table=[];best=None
 for fi in chosen:
  cy=z['faces'][fi];a=z['x'][cy];cf=a.mean(0);n=z['y'][fi]/np.linalg.norm(z['y'][fi]);height=1/np.linalg.norm(z['y'][fi]);foot=height*n
  for bias in [0.,.5,.85]:
   for corner in range(len(a)):
    v=(1-bias)*cf+bias*a[corner]
    for h in [1e-5,1e-4,5e-4,2e-3]:
     b=v+h*n
     if np.max(b@(old-b).T)<=1e-9:continue
     try:
      w,zz,ok=retract(old,np.vstack([W,b]));rr=report(zz)
     except Exception:continue
     guards=np.einsum('ij,ikj->ik',w,old[None]-w[:,None]).max(1)
     row=dict(face=int(fi),base_labels=[z['labels'][v] for v in cy],bias=bias,corner=corner,height=h,closed=ok,min_U_safe=float(guards.min()),report=rr)
     table.append(row)
     if not ok or min(guards)<=1e-9 or rr['E']>249 or len(rr['U'])!=1 or len(rr['S'])>2:continue
     key=(len(rr['S']),rr['Q'][0]['depth'] if rr['Q'] else 0.)
     if best is None or key<best[0]:
      best=(key,w,row);print('SCOUT_BEST',key,row,flush=True);(ROOT/'J91_TWO_APEX_START.json').write_text(json.dumps(dict(apexes=w.tolist(),cap_ids=m['ids']+[-1],frame_shift=m['g'].tolist(),nomination=row),indent=2)+'\n')
 (ROOT/'J91_TWO_APEX_SCOUT.json').write_text(json.dumps(table,indent=2)+'\n');print('J91_TWO_APEX_SCOUT_COMPLETED',len(table),bool(best),flush=True)

def run(source,steps=60,tag='J91_OUTERFLOW'):
 m,old,unused=init();W=np.array(json.loads(Path(source).read_text())['apexes']);hist=[];trust=.02;O=torch.tensor(old)
 for k in range(steps):
  zz,fields=chart(old,W);rr=report(zz);q=zz['y'];bars=rr['Q'];
  if not bars:print('NUMERICAL_OWN_S1_CANDIDATE',rr,flush=True);break
  peak=bars[0]['root'];a,b=bars[0]['edge'];elder=int(np.argmax((q*q).sum(1)));qi=np.array([i for i in range(len(q)) if i not in [peak,elder]]);qj=score(q).argmax(1)[qi];wi=np.argmax(np.einsum('ik,ijk->ij',W,old[None]-W[:,None]),axis=1)
  def fun(w):
   Q,M,V=fields(w);D=Q[qj]-Q[qi];qc=(Q[qi]*D).sum(1)/(torch.linalg.vector_norm(Q[qi],dim=1)*torch.linalg.vector_norm(D,dim=1));us=(w*(O[wi]-w)).sum(1)
   d=Q[b]-Q[a];t=torch.clamp(-(Q[a]*d).sum()/(d*d).sum(),0,1);f=Q[a]+t*d;loss=1-(f*f).sum()/(Q[peak]*Q[peak]).sum()
   return torch.cat([us,qc,M,loss[None]])
  wt=torch.tensor(W);v=fun(wt).numpy();J=torch.func.jacrev(fun,chunk_size=64)(wt).numpy().reshape(len(v),-1);nc=len(v)-4;G=J[:nc];MG=J[nc:nc+3];grad=J[-1]
  target=np.minimum(v[:nc],1e-8);target[:len(W)]=np.minimum(v[:len(W)],1e-7);nr=np.linalg.norm(G,axis=1);keep=nr>1e-9;scale=np.maximum(nr[keep],1e-8);GG=G[keep]/scale[:,None];rhs=(target-v[:nc])[keep]/scale;ms=np.maximum(np.linalg.norm(MG,axis=1),1e-6);EE=MG/ms[:,None];ee=-v[nc:nc+3]/ms
  op=linprog(grad,A_ub=-GG,b_ub=-rhs,A_eq=EE,b_eq=ee,bounds=[(-trust,trust)]*W.size,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9});rec=dict(k=k,old=float(v[-1]),trust=trust,lp=op.success,accepted=False)
  if op.success and grad@op.x<-1e-13:
   L=np.vstack([GG,-grad]);lb=np.r_[rhs,-.7*grad@op.x];fit=minimize(lambda d:(.5*d@d,d),op.x,jac=True,method='SLSQP',bounds=[(-trust,trust)]*W.size,constraints=[{'type':'ineq','fun':lambda d:L@d-lb,'jac':lambda d:L},{'type':'eq','fun':lambda d:EE@d-ee,'jac':lambda d:EE}],options={'maxiter':120,'ftol':1e-17});d=fit.x if min(L@fit.x-lb)>-1e-8 and max(abs(EE@fit.x-ee))<1e-9 else op.x;d=d.reshape(W.shape)
   for bt in range(17):
    try:w,zt,closed=retract(old,W+2**-bt*d,tol=2e-15,maxit=8);r=report(zt)
    except Exception:continue
    us=np.einsum('ik,ijk->ij',w,old[None]-w[:,None]).max(1);new=r['Q'][0]['depth'] if r['Q'] else 0.
    if not closed or min(us)<=1e-10 or r['E']>249 or len(r['U'])!=1 or len(r['S'])>2 or r['P'] or new>=rec['old']-1e-12:continue
    W=w;rec.update(accepted=True,alpha=2**-bt,new=new,report=r,min_U_safe=float(us.min()),min_Q_nonroot=float(np.sort(score(zt['q']).max(1))[2]));break
  hist.append(rec);print(tag,json.dumps(rec),flush=True)
  (ROOT/(tag+'.json')).write_text(json.dumps(dict(base='J90_DETACHED_C390_G8',frame_shift=m['g'].tolist(),apexes=W.tolist(),history=hist,report=report(chart(old,W)[0])),indent=2)+'\n')
  if rec['accepted']:
   if rec['alpha']>=.5:trust=min(.1,trust*1.25)
  else:trust*=.5
  if trust<1e-7:break
 print('J91_FULL_OUTER_FLOW_NUMERICAL_ONLY',flush=True)
if __name__=='__main__':
 if sys.argv[1]=='scout':scout()
 else:run(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 60,sys.argv[3] if len(sys.argv)>3 else 'J91_OUTERFLOW')
