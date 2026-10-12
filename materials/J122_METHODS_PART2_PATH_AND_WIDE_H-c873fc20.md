# material-c873fc20c232

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J122 numerical methods — Recovery capsule part 2/4: linear whole-path and finite widest-H methods

Complete numerical producing units, not exact equilibrium verifiers. Required geometry121.py is in [internal-source-reference],5112B/SHA b64da8c4140fba3954b28323d603be3813b0643ed6aca18b195a2b62f2c44bf2. Required forest122.py is complete in part1,[internal-source-reference]. Original exact J121_PAIRED_RELAYQ_G8 input is in [internal-source-reference]; new exact J122_QPATH_H_G8 in [internal-source-reference]. Part4 supplies literal consumed intermediate fields.

Observed Python3.13.5,NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu,float64,one BLAS/OMP/Torch thread. Numerical maximal-facet grouping is not exact incidence. geometry121.describe displays bars above a floor but includes all_positive_float_P/Q. Exact zero-bar/class claims belong to the rational auditor. Improved angular width below can DEEPEN principal P.

## pathflow122.py — complete7685B
SHA d33a8a23b3168c1bfcc9d411c39cdd0ea6c93c63da9a4e14cc0f5afa11ce3be7.
```python
"""J122 numerical whole-return-path continuation, at actual uniform mass.
Releases guards on a widest root-to-elder path, not cyclic local root targets.
Old positive off-path guards and new off-path vertices remain protected.
No floating census or stopping condition is an exact certificate.
"""
import sys,json,time,argparse
from pathlib import Path
import numpy as np,torch
from scipy.optimize import linprog,minimize
from scipy.spatial import QhullError
from geometry121 import geometry,tensors,read_h,arrows,describe,normalize,bars
from forest122 import widest,path

def keys(G,side):
    return [tuple(sorted(map(int,t))) for t in G['triples']] if side==0 else [int(i) for i in G['active']]

def policy(G,mode):
    out=[]
    for side,(x,ed) in enumerate([(G['p'],G['pe']),(G['q'],G['qe'])]):
        a,w,mat=arrows(x);elder=int(np.argmax((x*x).sum(1)))
        roots=np.where((a<0)&(np.arange(len(x))!=elder))[0]
        lv,par,order=widest(mat,elder);chosen={};paths=[]
        targeted=(mode=='both' or mode==['P','Q'][side])
        if targeted:
            for root in roots:
                p=path(par,int(root));paths.append(p)
                for i,j in zip(p[:-1],p[1:]):chosen[i]=j
        idx=[];dst=[];oldkeys=keys(G,side);free=[]
        for i in range(len(x)):
            if i==elder:free.append(oldkeys[i]);continue
            if i in chosen:j=chosen[i]
            elif a[i]>0:j=int(w[i])
            else:free.append(oldkeys[i]);continue
            idx.append(i);dst.append(j)
            if mat[i,j]<=0:free.append(oldkeys[i])
        widths=lv[np.arange(len(x))!=elder]
        out.append(dict(side=side,idx=idx,dst=dst,free=free,keys=oldkeys,paths=paths,elder=elder,roots=roots.tolist(),width=float(widths.min()),targeted=targeted))
    return out

def model(n,mode):
    G=geometry(n);pol=policy(G,mode)
    def fn(flat):
        p,q,g,V=tensors(flat.reshape(n.shape),G);out=[]
        for x,P in zip((p,q),pol):
            a=x[P['idx']];d=x[P['dst']]-a
            out.append((a*d).sum(1)/torch.sqrt((a*a).sum(1)*(d*d).sum(1)))
        return torch.cat(out+[g,torch.log(V)[None]])
    z=torch.tensor(n.ravel());v=fn(z).detach().numpy()
    J=torch.autograd.functional.jacobian(fn,z,vectorize=True).detach().numpy()
    return G,v[:-4],J[:-4],J[-4:],pol

def admission(G,oldpol,tau):
    info=[];ok=True
    for side,(x,ed),P in zip(range(2),[(G['p'],G['pe']),(G['q'],G['qe'])],oldpol):
        a,w,mat=arrows(x);kk=keys(G,side);free=set(P['free']);elder=int(np.argmax((x*x).sum(1)))
        protected=[i for i,k in enumerate(kk) if i!=elder and k not in free]
        mn=float(a[protected].min()) if protected else 1.
        lv,_,_=widest(mat,elder);width=float(np.delete(lv,elder).min())
        ok &= mn>=tau*.49
        bb=bars(x,ed)
        info.append(dict(min_protected=mn,width=width,roots=int(sum(a<0)),maxbar=float(bb[0]['depth']) if bb else 0))
    return bool(ok),info

def run(inp,prefix,mode='Q',steps=250,trust=.03,tau=1e-7,qp=False,cap=None):
    start=time.time();n=read_h(inp);n=n[geometry(n)['active']];n=normalize(n);initial=n.copy();delta=trust;history=[];accepted=0;reason='iteration_limit'
    prefix=str(prefix);Path(prefix).parent.mkdir(parents=True,exist_ok=True)
    for it in range(steps):
        G,a,J,gauge,pol=model(n,mode);dim=n.size;scale=np.repeat(np.linalg.norm(n,axis=1),3)
        neg=a<tau
        # Every already-positive tree guard is restored to fixed tau. Negative
        # path guards improve by a common fraction toward tau, without forcing
        # their old reverse guards. This is not the previous cyclic policy.
        coeff=np.where(neg,tau-a,0.0);rhs=np.where(neg,0.,a-tau)
        A=np.column_stack([-J*scale,coeff]);eq=np.column_stack([gauge*scale,np.zeros(4)])
        lp=linprog(np.r_[np.zeros(dim),-1],A_ub=A,b_ub=rhs,A_eq=eq,b_eq=np.zeros(4),bounds=[(-delta,delta)]*dim+[(0,.4)],method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
        if not lp.success:
            reason='linear_solver_failure';history.append(dict(iteration=it,message=lp.message,trust=delta,policy=pol));break
        gain=float(lp.x[-1]);z=lp.x[:-1]
        if gain<1e-10:
            reason='linear_path_stall';history.append(dict(iteration=it,gain=gain,policy=pol,duals=(-lp.ineqlin.marginals).tolist()));break
        if qp:
            goal=.5*gain;aa=A[:,:-1];bb=rhs-A[:,-1]*goal;ee=eq[:,:-1]
            res=minimize(lambda x:(.5*x@x,x),z,jac=True,method='SLSQP',bounds=[(-delta,delta)]*dim,constraints=[dict(type='ineq',fun=lambda x:bb-aa@x,jac=lambda x:-aa),dict(type='eq',fun=lambda x:ee@x,jac=lambda x:ee)],options=dict(maxiter=100,ftol=1e-14))
            if res.success and (bb-aa@res.x).min()>-1e-9:z=res.x;gain=goal
        step=(z*scale).reshape(n.shape);trials=[];good=False
        for k in range(18):
            alpha=2.**(-k)
            try:
                nn=n+alpha*step;gg=geometry(nn)
                if not gg['simple']:raise ValueError('nonsimple derivative wall')
                ok,inf=admission(gg,pol,tau)
                for s in range(2):
                    if pol[s]['targeted']:
                        old=pol[s]['width'];wanted=old+.02*alpha*gain*(tau-old)
                        ok &= inf[s]['width']>=wanted-1e-13
                    elif cap is not None:ok &= inf[s]['maxbar']<=cap
                ok &= len(gg['pe'])<=249
                trials.append(dict(alpha=alpha,accepted=bool(ok),info=inf,VEF=[len(gg['v']),len(gg['pe']),len(gg['active'])]))
                if ok:good=True;break
            except (ValueError,AssertionError,QhullError,np.linalg.LinAlgError) as ex:trials.append(dict(alpha=alpha,error=str(ex)))
        rec=dict(iteration=it,gain=gain,trust=delta,policy=pol,negative_guards=int(sum(neg)),accepted=good,trials=trials)
        if good:
            n=normalize(nn);accepted+=1;delta=min(.12,delta*(1.2 if k<2 else .85));st=describe(n);rec['stats']=st
            Path(prefix+'.last.json').write_text(json.dumps(dict(n=n.tolist(),stats=st,accepted=accepted,iteration=it),indent=2)+'\n')
            if st['rho']>1e-8:reason='NUMERICAL_ONE_ROOT_EACH_NEEDS_EXACT';history.append(rec);break
            if mode=='Q' and len(st['S'])==1:reason='NUMERICAL_Q_CANCELLATION_NEEDS_EXACT';history.append(rec);break
            if mode=='P' and len(st['U'])==1:reason='NUMERICAL_P_CANCELLATION_NEEDS_EXACT';history.append(rec);break
        else:
            delta*=.25
            if delta<1e-9:reason='finite_path_trust_stall';history.append(rec);break
        history.append(rec)
        if it%10==0 or not good:
            print('PATHFLOW122',mode,it,'accept',accepted,'widths',[p['width'] for p in pol],'=>',[v['width'] for v in (trials[k]['info'] if good else [])],'negative',sum(neg),'P/Q',len(rec.get('stats',{}).get('P',[])),len(rec.get('stats',{}).get('Q',[])),'delta',delta,flush=True)
    out=dict(n=n.tolist(),initial=initial.tolist(),stats=describe(n),reason=reason,accepted=accepted,mode=mode,steps=steps,trust=trust,tau=tau,qp=qp,cap=cap,seconds=time.time()-start,history=history)
    Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PATHFLOW122_DONE',reason,accepted,out['stats'],flush=True);return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('prefix');p.add_argument('--mode',choices=['P','Q','both'],default='Q');p.add_argument('--steps',type=int,default=250);p.add_argument('--trust',type=float,default=.03);p.add_argument('--tau',type=float,default=1e-7);p.add_argument('--qp',action='store_true');p.add_argument('--cap',type=float)
    a=p.parse_args();run(a.input,a.prefix,a.mode,a.steps,a.trust,a.tau,a.qp,a.cap)
```

Executed PATHQ122 from literal J121 input: modeQ,steps250,trust.03,tau1e-7,qpFalse,capNone. Only68 accepted steps through iteration67 saved before45-second process cutoff;250 completion is NOT claimed. DEBUGQ122 ran3 steps with the same settings except steps3. Early finite steps needed alpha1/256 to retain opposite guards. Width increased approximately-.21323 to-.21265, but sixQ and a largerP appeared. Linear mass derivatives do not control finite quadratic guard loss. No family exclusion. Nonlinear part1 later reached a separately exact-audited Q-empty body.

## widefinite122.py — complete v2,5743B
SHA625f7594d281e50e83d2f53ea17d399b0e10826ee5f9d94d11024b5ee9893a0c.
```python
"""J122 actual-mass widest-path landscape continuation, numerical only.
A complete widest tree is rebuilt at every trial. Its distinct parent-edge
scores share one moving bottleneck floor; local outgoing maxima alone are not
used. This version does not protect the entire sorted level profile. Current true hulls/mass and
piecewise path bottlenecks are re-evaluated for every finite nonlinear trial.
The opposite polar landscape retains positive individual all-point arrows.
"""
import json,sys,time,argparse
from pathlib import Path
import numpy as np,torch
from scipy.optimize import minimize
from geometry121 import geometry,tensors,read_h,normalize,describe,arrows
from forest122 import widest,path

def policy(x):
 a,w,A=arrows(x);elder=int(np.argmax((x*x).sum(1)));L,parent,_=widest(A,elder)
 ids=np.array([i for i in range(len(x)) if i!=elder],int)
 pairs=np.array([(i,parent[i]) for i in ids],int);scores=np.array([A[i,j] for i,j in pairs]);order=np.argsort(scores)
 assert abs(scores.min()-L[ids].min())<1e-12
 return scores[order],pairs[order],dict(elder=elder,ids=ids[order].tolist(),parent=parent.tolist(),local_juniors=np.where(a<0)[0].tolist())

class Model:
 def __init__(self,n,tau,side='P'):
  self.n=n.copy();self.tau=tau;self.scale=np.repeat(np.linalg.norm(n,axis=1),3);self.last=None;self.calls=0;self.side=side
  G=geometry(n);x=G['p'] if side=='P' else G['q'];b,pairs,pol=policy(x)
  self.count=2*len(n)-5 if side=='P' else len(n)-1
  self.base=np.full(self.count,float(b.min()));self.target=self.base.copy();self.coeff=tau-self.base
  self.opcount=len(n)-1 if side=='P' else 2*len(n)-5
  self.meta=dict(base=self.base.tolist(),policy=pol,initial_pairs=pairs.tolist(),side=side)
 def calc(self,z):
  if self.last is not None and np.array_equal(z,self.last):return self.val,self.jac
  nn=self.n+(z[:-1]*self.scale).reshape(self.n.shape);G=geometry(nn)
  if not G['simple']:raise ValueError('nonsimple derivative fan')
  x=G['p'] if self.side=='P' else G['q'];levels,pairs,pol=policy(x)
  y=G['q'] if self.side=='P' else G['p'];a,w,_=arrows(y);idx=np.argsort(a)[1:]
  pad=self.count-len(levels);opad=self.opcount-len(idx)
  assert pad>=0 and opad>=0
  def fn(t):
   n=torch.tensor(self.n)+(t[:-1]*torch.tensor(self.scale)).reshape(nn.shape);p,q,g,V=tensors(n,G)
   x=p if self.side=='P' else q;y=q if self.side=='P' else p
   u=x[pairs[:,0]];d=x[pairs[:,1]]-u
   scores=(u*d).sum(1)/torch.sqrt((u*u).sum(1)*(d*d).sum(1))
   scores=torch.cat([scores,torch.ones(pad)])-torch.tensor(self.target)-t[-1]*torch.tensor(self.coeff)
   u=y[idx];d=y[w[idx]]-u
   op=(u*d).sum(1)/torch.sqrt((u*u).sum(1)*(d*d).sum(1))-self.tau
   return torch.cat([scores,op,torch.ones(opad),g,torch.log(V)[None]])
  t=torch.tensor(z);self.val=fn(t).detach().numpy();self.jac=torch.autograd.functional.jacobian(fn,t,vectorize=True).detach().numpy();self.last=z.copy();self.calls+=1
  return self.val,self.jac

def run(inp,prefix,outer=2,maxiter=100,trust=.04,tau=1e-5,gaincap=.2,side='P'):
 n=normalize(read_h(inp));initial=n.copy();hist=[];accepted=0;reason='outer_iteration_limit';start=time.time()
 for it in range(outer):
  M=Model(n,tau,side);z=np.zeros(n.size+1)
  try:
   res=minimize(lambda z:(-z[-1]+1e-5*z[:-1]@z[:-1],np.r_[2e-5*z[:-1],-1.]),z,jac=True,method='SLSQP',bounds=[(-trust,trust)]*n.size+[(0,gaincap)],constraints=[dict(type='ineq',fun=lambda z:M.calc(z)[0][:-4],jac=lambda z:M.calc(z)[1][:-4]),dict(type='eq',fun=lambda z:M.calc(z)[0][-4:],jac=lambda z:M.calc(z)[1][-4:])],options=dict(maxiter=maxiter,ftol=1e-12))
   val,_=M.calc(res.x);nn=n+(res.x[:-1]*M.scale).reshape(n.shape);G=geometry(nn);D=describe(nn)
   levels=policy(G['p'] if side=='P' else G['q'])[0];levels=np.r_[levels,np.ones(M.count-len(levels))]
   op=arrows(G['q'] if side=='P' else G['p'])[0];op=np.sort(op)[1:]
   target=np.where(M.base<0,M.base+.5*res.x[-1]*(tau-M.base),tau*.1)
   good=(levels-target).min()>=-1e-12 and op.min()>=tau*.1 and res.x[-1]>1e-7 and D['VEF'][1]<=249
   rec=dict(iteration=it,n=nn.tolist(),stats=D,accepted=bool(good),success=bool(res.success),message=res.message,nit=int(res.nit),t=float(res.x[-1]),min_constraint=float(val[:-4].min()),gauge=float(abs(val[-4:]).max()),calls=M.calls,policy=M.meta,step=res.x.tolist(),minpath=float(levels.min()),minop=float(op.min()))
  except Exception as ex:rec=dict(iteration=it,accepted=False,error=repr(ex),calls=M.calls,policy=M.meta);good=False
  hist.append(rec);print('WIDEFINITE122',it,{k:rec.get(k) for k in ['accepted','t','minpath','minop','min_constraint','calls','error']},flush=True)
  if good:
   n=normalize(nn);accepted+=1;Path(prefix+'.last.json').write_text(json.dumps(dict(n=n.tolist(),stats=describe(n),accepted=accepted),indent=2)+'\n')
   if rec['minpath']>0:reason='NUMERICAL_TARGET_NEEDS_EXACT';break
  else:reason='no_finite_accepted_retraction';break
  Path(prefix+'.history.json').write_text(json.dumps(hist,indent=2)+'\n')
 out=dict(n=n.tolist(),initial=initial.tolist(),history=hist,stats=describe(n),accepted=accepted,outer=outer,maxiter=maxiter,trust=trust,tau=tau,gaincap=gaincap,side=side,seconds=time.time()-start,reason=reason)
 Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n');print('WIDEFINITE122_DONE',reason,accepted,out['stats'],flush=True);return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('prefix');p.add_argument('--outer',type=int,default=2);p.add_argument('--maxiter',type=int,default=100);p.add_argument('--trust',type=float,default=.04);p.add_argument('--tau',type=float,default=1e-5);p.add_argument('--gaincap',type=float,default=.2);p.add_argument('--side',default='P',choices=['P','Q']);a=p.parse_args();run(a.input,a.prefix,a.outer,a.maxiter,a.trust,a.tau,a.gaincap,a.side)
```

### Complete exact patch restoring original v1
Save as recover_wide_version122.py. Restores complete5671B/SHA5e58cd0d1ee9e151169157172e11c211447519e2f91d5d0eb74a325089fc5a03. No helper is omitted. V1 repeats bottleneck pairs; v2 uses distinct tree edges with a common worst floor. Neither guarantees simultaneous persistence improvement.
```python
from pathlib import Path
import hashlib
s=Path('widefinite122.py').read_text()
assert hashlib.sha256(s.encode()).hexdigest()=='625f7594d281e50e83d2f53ea17d399b0e10826ee5f9d94d11024b5ee9893a0c'
s=s.replace('A complete widest tree is rebuilt at every trial. Its distinct parent-edge\nscores share one moving bottleneck floor; local outgoing maxima alone are not\nused. This version does not protect the entire sorted level profile. Current true hulls/mass and\n','The complete directed max-min path level for every actual nonelder vertex is\nconstrained, not its merely local outgoing margin. Current true hulls/mass and\n')
a=s.index(' ids=np.array([i for i in range(len(x)) if i!=elder],int)')
b=s.index('\n\nclass Model:',a)
s=s[:a]+''' ids=np.array(sorted([i for i in range(len(x)) if i!=elder],key=lambda i:(L[i],i)),int)
 pairs=[]
 for i in ids:
  pp=path(parent,i);ij=min(zip(pp[:-1],pp[1:]),key=lambda t:A[t[0],t[1]])
  pairs.append(ij)
 return L[ids],np.array(pairs,int),dict(elder=elder,ids=ids.tolist(),parent=parent.tolist(),local_juniors=np.where(a<0)[0].tolist())'''+s[b:]
s=s.replace('self.base=np.full(self.count,float(b.min()));self.target=self.base.copy();self.coeff=tau-self.base','self.base=np.r_[b,np.ones(self.count-len(b))];self.target=np.where(self.base<0,self.base,tau);self.coeff=np.where(self.base<0,tau-self.base,0)')
assert len(s.encode())==5671
assert hashlib.sha256(s.encode()).hexdigest()=='5e58cd0d1ee9e151169157172e11c211447519e2f91d5d0eb74a325089fc5a03'
Path('widefinite122_v1.py').write_bytes(s.encode())
print('J122_WIDE_ORIGINAL_VERSION_EXACT_PASS')
```

### Executed widest-H runs
All sideP. Settings outer/maxiter/trust/tau/gaincap. Inputs denote part4 fields unless the explicit exact parent is named.
A(v1),exactJ122_QPATH_H_G8,1/100/.04/1e-6/.25:0 admitted, oppositeQnegative.
B(v1),sameexactinput,2/120/.005/1e-5/.03:2 admitted,90/135/47,numS1/U5,fourP~.6382163774,.0002306623,.0000343931,.0000305841,minpath-.4820396.
C(v1),B.last,2/110/.015/1e-5/.09:2 admitted,88/132/46,S1/U5,fourP~.6512315724,.00072309485,.00046965189,.00024740801,minpath-.39917665.
D(v1),C.last,2/115/.04/1e-5/.25:first rejected, Qguard~-.000557;not two rounds.
E(v1),C.last,2/150/.01/1e-4/.08:ONE admitted before45-second cutoff during second.84/126/44,S1/U5,fourP~.6555859496,.001187822809,.000885240163,.000223259339,minpath-.37931956,minq.00009987876.
F(v2),E.last,2/90/.025/1e-4/.2:one admitted,second rejected(Qguard~-.000270).76/114/40,S1/U5,fourP~.6716678582,.0140576020,.00160192424,1.816474082e-9,minpath-.33279987,minq.00008507893. Numerical bars can leave~1e-16 roundoff; no exact weak-free/bar-empty audit of these endpoints.

76 extreme vertices permit arbitrary V motion with sufficient E<=222 without preserving every old coplanarity. Part3 executes that freedom. Improved negative path width alone is not actual basin cancellation.
