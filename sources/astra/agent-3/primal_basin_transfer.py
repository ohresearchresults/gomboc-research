"""Physical own-mass transfers out of the unwanted unstable basin.
The idea of committed positive reachability comes from the pinned peer1
polar-basin method. This is an independent NumPy implementation on literal
primal free vertices, with actual uniform centroid derivatives. P may deepen;
only the actual strict census and reachability govern transfer acceptance.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from vertex_geometry import geometry
from support_geometry import escape
from polish_121 import forest
from projected_p_flow_max import retract
from persistence_birth import evaluate
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def scores(A):
 e=A[None]-A[:,None];aa=np.sum(A*A,axis=1);ee=np.sum(e*e,axis=2);W=np.einsum('ic,ijc->ij',A,e)/np.sqrt(np.maximum(aa[:,None]*ee,1e-60));np.fill_diagonal(W,-np.inf);return W

def state(X,elder=None,derivative=True):
 g=geometry(X,derivative);W=scores(g['Z']);U=np.flatnonzero(W.max(1)<0);S=np.flatnonzero(escape(g['H'])[0]<0);elder=int(np.argmax(np.sum(g['Z']**2,axis=1))) if elder is None else elder;reach=np.zeros(len(X),bool);reach[elder]=True
 while True:
  new=reach|(W[:,reach]>5e-9).any(1)
  if np.array_equal(new,reach):break
  reach=new
 return dict(g=g,W=W,U=U,S=S,elder=elder,reach=reach)

def derivatives(e,target):
 g=e['g'];u,v=target;elder=e['elder'];assert len(e['U'])==2 and len(e['S'])==1 and elder in e['U'];junior=next(int(i)for i in e['U']if i!=elder);pE=forest(g['Z'],[elder]);pJ=forest(g['Z'],[junior]);pp=np.where(e['reach'],pE,pJ);sign=np.ones(len(pp));sign[e['U']]=-1;vp,_,JP=escape(g['Z'],g['DZ'],angular=True,chosen=pp);keep=np.ones(len(pp),bool)
 if u==junior:keep[u]=False
 vq,jq,JQ=escape(g['H'],g['DH'],angular=True);sq=np.ones(len(vq));sq[e['S']]=-1;vals=np.r_[(sign*vp)[keep],sq*vq];J=np.vstack(((sign[:,None]*JP)[keep],sq[:,None]*JQ));chosen=pp.copy();chosen[u]=v;cross,_,JC=escape(g['Z'],g['DZ'],angular=True,chosen=chosen);d=g['X'].size;sx=np.sqrt(np.mean(g['Z']**2));sh=np.sqrt(np.mean(g['H']**2));M=np.vstack((g['DX'].reshape(-1,d)/sx,g['DH'].reshape(-1,d)/sh));_,s,V=svd(M,full_matrices=False,check_finite=False);assert min(s)>1e-12;W=V.T/s;return vals,J,float(cross[u]),JC[u],W,junior

def healthy(e,committed):
 if len(e['U'])!=2 or len(e['S'])!=1:return False
 vp=escape(e['g']['Z'],angular=True)[0];vq=escape(e['g']['H'],angular=True)[0];vp[e['U']]*=-1;vq[e['S']]*=-1;return min(min(vp),min(vq))>7e-8 and e['reach'][committed].all()

def transfer(X,elder,target,committed,out,steps):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);trust=.03;history=[];start=time.time();u,v=target
 for it in range(steps):
  e=state(X,elder);value=e['W'][u,v];row=dict(it=it,source=u,destination=v,cross_score=float(value),reachable=int(e['reach'].sum()),S=len(e['S']),U=len(e['U']),trust=trust,seconds=time.time()-start);history.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(history,indent=2))
  if it%10==0:print('PRIMAL_TRANSFER',out,row,flush=True)
  if len(e['S'])==len(e['U'])==1:np.save(out/'potential.npy',X);return X,True
  if e['reach'][u] and value>1e-8 and e['reach'][committed].all():np.save(out/'success.npy',X);return X,True
  guards,J,objective,Dobj,W,junior=derivatives(e,target);A=J@W;grad=Dobj@W;d=X.size;floor=1e-7;bound=trust/np.sqrt(d);lp=linprog(-grad,A_ub=-A,b_ub=guards-floor,bounds=[(-bound,bound)]*d,method='highs',options=OPT)
  if not lp.success or grad@lp.x<1e-11:
   trust*=.4
   if trust<1e-8:break
   continue
  desired=.7*(grad@lp.x);qp=minimize(lambda t:(.5*t@t,t),lp.x*.7,jac=True,method='SLSQP',bounds=Bounds(-bound,bound),constraints=[LinearConstraint(A,floor-guards,np.inf),LinearConstraint(grad,desired,np.inf)],options=dict(maxiter=60,ftol=1e-13))
  if min(A@qp.x+guards-floor)<-1e-8 or grad@qp.x<desired-1e-8:
   trust*=.4
   if trust<1e-8:break
   continue
  dx=(W@qp.x).reshape(X.shape);ok=False
  for k in range(15):
   Y=X+2.**-k*dx
   try:
    ee=state(Y,elder,False)
    if len(ee['S'])==len(ee['U'])==1:np.save(out/'potential.npy',Y);return Y,True
    if k<2 and not healthy(ee,committed):Y,good,corr=retract(Y,[elder,junior],1e-7,limit=12);ee=state(Y,elder,False)
   except (ValueError,np.linalg.LinAlgError):continue
   if len(ee['S'])==len(ee['U'])==1:np.save(out/'potential.npy',Y);return Y,True
   if elder in ee['U'] and healthy(ee,committed) and ee['W'][u,v]>objective+max(1e-11,abs(objective)*1e-7):X=Y;ok=True;row['alpha']=2.**-k;break
  if ok and k==0:trust=min(.3,trust*1.3)
  if not ok:trust*=.4
  if trust<1e-8:break
 return X,False

def run(source,out,stages,steps):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);X=np.load(source);assert len(X)<=84;e=state(X,derivative=False);elder=e['elder'];records=[];np.save(out/'initial.npy',X);start=time.time()
 for stage in range(stages):
  e=state(X,elder,False);committed=np.flatnonzero(e['reach']);junior=next(int(i)for i in e['U']if i!=elder);I=np.array([i for i in e['g']['vertices']if not e['reach'][i]]);J=np.array([i for i in e['g']['vertices']if e['reach'][i]]);W=e['W'][np.ix_(I,J)];used=set();targets=[]
  for ij in np.argsort(-W.ravel()):
   a,b=np.unravel_index(ij,W.shape);u,v=int(I[a]),int(J[b])
   if u not in used:targets.append((u,v));used.add(u)
   if len(targets)==5:break
  targets.append((junior,int(J[np.argmax(e['W'][junior,J])])));accepted=False
  for k,target in enumerate(targets):
   Y,ok=transfer(X,elder,target,committed,out/f'stage{stage:02d}_attempt{k}',steps);ee=state(Y,elder,False);info=evaluate(Y)[2];row=dict(stage=stage,attempt=k,target=target,accepted=ok,reachable_before=len(committed),reachable_after=int(ee['reach'].sum()),P=info['Pmax'],Q=info['Qmax'],S=len(ee['S']),U=len(ee['U']),seconds=time.time()-start);records.append(row);(out/'stages.json').write_text(json.dumps(records,indent=2))
   if ok and len(ee['S'])==len(ee['U'])==1:np.save(out/'potential.npy',Y);print('PRIMAL_TRANSFER_POTENTIAL_REQUIRES_EXACT',row,flush=True);return
   if ok and ee['reach'].sum()>len(committed):X=Y;accepted=True;np.save(out/'latest_transfer.npy',X);print('PRIMAL_TRANSFER_ACCEPTED',row,flush=True);break
  if not accepted:print('PRIMAL_TRANSFER_FINITE_SEARCH_STOPPED',stage,flush=True);break

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--stages',type=int,default=20);p.add_argument('--steps',type=int,default=70);a=p.parse_args();run(a.input,a.out,a.stages,a.steps)
