"""J91 finite mass-balanced U-safe cap chart, dynamic polar witness policies.
Numerical nomination: every accepted step is a genuinely convex old-facet cap
complex, has reintegrated own centroid, full root census and all positive bars.
A 1e-14 floating bar nomination floor is not an exact zero certificate.
"""
from pathlib import Path
import json,sys
from fractions import Fraction
import numpy as np,torch
from scipy.optimize import linprog,minimize
from j90 import geometry,report,score,radial
from masscaps90 import face_data,add_caps
ROOT=Path(__file__).resolve().parent
torch.set_default_dtype(torch.float64);torch.set_num_threads(1)

def setup(source=None):
 y=np.loadtxt(ROOT/'J90_DETACHED_C390_G8.txt',skiprows=1)/1e8;raw=geometry(y);g=raw['g'];z=geometry(raw['q']);ids=[6,14,16,19,39,41,43,65]
 cap=json.loads((ROOT/'J90_BALANCED_C452_G14_CAPS.json').read_text())['apexes'];W=np.array([[float(Fraction(s)) for s in cap[str(i)]] for i in ids])-g
 if source is not None:W=np.array(json.loads(Path(source).read_text())['apexes'])
 centres=[];normals=[];areas=[];qrows=[];fi_owner=[];ca=[];cb=[]
 for j,i in enumerate(ids):
  c,n,a=face_data(z,i);centres.append(c);normals.append(n);areas.append(a)
 for fi,cy in z['faces'].items():
  if fi not in ids:
   qrows.append(z['y'][fi]);fi_owner.append(-1);ca.append([0,0,0]);cb.append([0,0,0])
  else:
   j=ids.index(fi)
   for a,b in zip(cy,cy[1:]+cy[:1]):
    qrows.append([0,0,0]);fi_owner.append(j);ca.append(z['x'][a]);cb.append(z['x'][b])
 model=dict(z=z,g=g,ids=ids,W=W,c=np.array(centres),n=np.array(normals),a=np.array(areas),q0=np.array(qrows),owner=np.array(fi_owner),ca=np.array(ca),cb=np.array(cb))
 return model

def run(steps=60,source=None,tag='J91_CAPFLOW'):
 m=setup(source);z=m['z'];ids=m['ids'];W=m['W'];C=torch.tensor(m['c']);N=torch.tensor(m['n']);areas=torch.tensor(m['a']);Y=torch.tensor(z['y']);old=torch.tensor(z['x']);own=m['owner'];moving=np.where(own>=0)[0];Q0=torch.tensor(m['q0']);A=torch.tensor(m['ca'][moving]);B=torch.tensor(m['cb'][moving]);O=torch.tensor(own[moving]);h0=np.sum((W-m['c'])*m['n'],axis=1)
 activepairs=[(j,fi) for j,i in enumerate(ids) for fi in range(len(z['y'])) if fi!=i];jj=torch.tensor([j for j,i in activepairs]);ff=torch.tensor([i for j,i in activepairs]);hist=[];trust=.02
 def fields(w):
  n=torch.linalg.cross(B-A,w[O]-A);h=(n*A).sum(1);q=Q0.clone();q[moving]=n/h[:,None]
  height=((w-C)*N).sum(1);vol=areas*height/3;mom=(vol[:,None]*(3*C+w)/4).sum(0)
  return q,height,mom,vol
 def owncheck(w):
  zz=add_caps(z,{i:w[j] for j,i in enumerate(ids)});return zz,report(zz)
 for k in range(steps):
  zz,rr=owncheck(W);q=zz['q'];main=rr['Q'][0] if rr['Q'] else None
  if main is None:print('REFERENCE_Q_ABSENT',rr,flush=True);break
  peak=main['root'];ea,eb=main['edge'];elder=int(np.argmax(np.sum(q*q,axis=1)));Sroot=set([peak,elder]);qi=np.array([i for i in range(len(q)) if i not in Sroot]);qj=score(q).argmax(1)[qi]
  wi=np.argmax(np.einsum('ik,ijk->ij',W,z['x'][None]-W[:,None]),axis=1)
  def fun(w):
   q,h,mom,v=fields(w)
   # chart constraints and sufficient inherited-old-point U-safe witnesses
   parent=1-(Y[ff]*w[jj]).sum(1)
   mutual=(1-q[moving]@w.T).flatten()
   us=(w*(old[wi]-w)).sum(1)
   dq=q[qj]-q[qi];qc=(q[qi]*dq).sum(1)/(torch.linalg.vector_norm(q[qi],dim=1)*torch.linalg.vector_norm(dq,dim=1))
   d=q[eb]-q[ea];t=torch.clamp(-(q[ea]*d).sum()/(d*d).sum(),0,1);f=q[ea]+t*d;loss=1-(f*f).sum()/(q[peak]*q[peak]).sum()
   return torch.cat([h,parent,mutual,us,qc,mom,loss[None]])
  tW=torch.tensor(W);vals=fun(tW).numpy();J=torch.func.jacrev(fun,chunk_size=64)(tW).numpy().reshape(len(vals),-1)
  nc=len(vals)-4;v=vals[:nc];G=J[:nc];MG=J[nc:nc+3];grad=J[-1]
  target=np.minimum(v,np.full(nc,1e-8));target[:len(W)]=np.minimum(v[:len(W)],1e-7)
  # Exact-incidence rows (each apex lies on its own fan) have zero Jacobian.
  nr=np.linalg.norm(G,axis=1);keep=nr>1e-9;scale=np.maximum(nr[keep],1e-8);GG=G[keep]/scale[:,None];rhs=(target-v)[keep]/scale
  ms=np.maximum(np.linalg.norm(MG,axis=1),1e-6);EE=MG/ms[:,None];ee=-vals[nc:nc+3]/ms
  op=linprog(grad,A_ub=-GG,b_ub=-rhs,A_eq=EE,b_eq=ee,bounds=[(-trust,trust)]*W.size,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  rec=dict(k=k,old=float(vals[-1]),trust=trust,lp=op.success,accepted=False)
  if op.success and grad@op.x<-1e-12:
   L=np.vstack([GG,-grad]);lb=np.r_[rhs,-.7*grad@op.x]
   fit=minimize(lambda d:(.5*d@d,d),op.x,jac=True,method='SLSQP',bounds=[(-trust,trust)]*W.size,constraints=[{'type':'ineq','fun':lambda d:L@d-lb,'jac':lambda d:L},{'type':'eq','fun':lambda d:EE@d-ee,'jac':lambda d:EE}],options={'maxiter':150,'ftol':1e-17})
   delta=fit.x if min(L@fit.x-lb)>-1e-8 and max(abs(EE@fit.x-ee))<1e-9 else op.x
   delta=delta.reshape(W.shape)
   for bt in range(20):
    w=W+delta*2**-bt
    # Finite actual moment correction by minimum-norm Newton, not tangent alone.
    for correction in range(8):
     wt=torch.tensor(w);mom=fields(wt)[2].numpy()
     if max(abs(mom))<1e-15:break
     MJ=torch.func.jacrev(lambda a:fields(a)[2])(wt).numpy().reshape(3,-1)
     dw=np.linalg.lstsq(MJ,-mom,rcond=None)[0];w+=dw.reshape(w.shape)
    vv=fun(torch.tensor(w)).numpy();
    if np.min(vv[:nc]-target)<-1e-9 or np.max(abs(vv[nc:nc+3]))>1e-13:continue
    try:zzz,r=owncheck(w)
    except Exception:continue
    loss=r['Q'][0]['depth'] if r['Q'] else 0.
    if len(r['S'])>2 or len(r['U'])!=1 or r['P'] or loss>=rec['old']-1e-12:continue
    W=w;rec.update(accepted=True,alpha=2**-bt,new=loss,report=r,moment=vv[nc:nc+3].tolist(),min_U_guard=float(vv[-4-len(qi)-len(W):-4-len(qi)].min()));break
  hist.append(rec);print(tag,json.dumps(rec),flush=True)
  (ROOT/(tag+'.json')).write_text(json.dumps(dict(base='J90_DETACHED_C390_G8',frame_shift=m['g'].tolist(),cap_ids=ids,apexes=W.tolist(),history=hist,report=owncheck(W)[1]),indent=2)+'\n')
  if rec['accepted']:
   if rec['alpha']>=.5:trust=min(.05,trust*1.25)
  else:trust*=.5
  if trust<1e-7:break
 print('J91_FIXED_CAP_CHART_NUMERICAL_ONLY',flush=True)
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 60,sys.argv[2] if len(sys.argv)>2 else None,sys.argv[3] if len(sys.argv)>3 else 'J91_CAPFLOW')
