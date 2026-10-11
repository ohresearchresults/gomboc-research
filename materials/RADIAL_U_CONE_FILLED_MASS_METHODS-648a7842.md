# material-648a7842bd7f

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Fixed-ray physical U-flow cone with actual filled-mass restoration

This is complete runnable numerical source, an exact floating checkpoint, and a scoped failed construction method. Exact retained rational descendants are in [internal-source-reference], audited by [internal-source-reference]. That geometry material also reconstructs the required complete points.json (1220bytes SHAe9fc32feffd3e01d64119a9abe2476af5dfd46d3e06558c40a9e0578abb36d1f). None of these results is an own110 winner.

## Mathematical chart and evidence boundary

For fixed nonzero rays d_i and positive scales s_i, physical input vertices v_i=s_i d_i have a strict escape i→j exactly when `(d_i·d_j)s_j-||d_i||²s_i>0`. These are linear inequalities in s. Equivalently with h_i=1/s_i the inequality is `(d_i·d_j)h_i-||d_i||²h_j>0`. A positive rootward graph over all input points rules out every other unstable vertex even when exposure changes. Positive arrows strictly increase norm, so no directed cycle is possible. This is a reference-center statement. The ordinary FILLED centroid must also be zero; first-order centering alone did not suffice.

For a fixed oriented triangular hull, volume is cubic and first moment quartic in radial scales. Both routines below rebuild the actual floating hull for each proposed finite step. The first failed scout enforces centroid only to first order. At its first accepted step the actual center was approximately(0.00015147,0.00018871,0.00014809), and numerical U rose from1 to4. Its attempted40-step call actually produced20 iteration records and then LP_FAIL at iteration20; do not call this an executed40-step run or a geometric exclusion.

The corrected method restores the actual filled centroid by repeated minimum-norm constrained Newton/SLSQP corrections inside a positive physical-flow cone, then recomputes the actual hull and own U count before acceptance. Its polar objective is a minimum-total-defect rootward arborescence, not merely a single local saddle residual. All-pair graph values in these routines are NOT the true-edge bottleneck values of GLOBAL_DIAGNOSTIC. The positive-sign feasibility is related, but bottleneck magnitudes and cuts must not be interchanged. q nominations are merged at8 decimal places in state(); the final exact maximal complex can differ.

Actual first30 restored iterations, guard2e-6, initial trust.03, produced numerical V54/F104,S7/U1. The last record was loss0.6104402015062623→0.6103736485382893, polar all-pair beta-0.0699279852739938, physical beta1.9477703870881554e-6, filled centroid approximately(7.88e-16,-5.19e-15,-2.61e-15). Polar root46 and physical input root0 are this floating nomination order, not canonical RAW labels. This is not stable-pair cancellation. Subsequent100-iteration continuation with initial trust.04 was still a finite numerical continuation, not an exclusion; the exact retained G6 body is defined by its literal coordinates, not by assuming a later checkpoint is the same body.

Environment used: Python3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, NetworkX3.6.1; OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. No nonuniform density or point-cloud mean is used. All positive-centroid facts in this material are floating diagnostics until the separate exact audit is applied. Scipy hull orientation in scout.topology assumes the current raw origin remains inside, as in this radial positive-scale cone; this helper should not be reused without correction for arbitrary point clouds with an exterior origin.

## scout.py

Save verbatim including final newline:5183bytes,SHA261aa0f905891f2dd12a4bc8e4dd780109e0ed33b37c8f3930999fb934fe7246.

```python
"""V-radial whole-complex scout; floating hypotheses only, not exact acceptance."""
import argparse,json,pathlib,time
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog, minimize
import torch
DT=torch.float64
torch.set_num_threads(1)

def topology(v):
 h=ConvexHull(v)
 f=h.simplices.copy()
 d=np.einsum('ij,ij->i',v[f[:,0]],np.cross(v[f[:,1]],v[f[:,2]]))
 f[d<0]=f[d<0][:,[0,2,1]]
 return f

def mass_np(v,f):
 a,b,c=v[f[:,0]],v[f[:,1]],v[f[:,2]]
 det=np.einsum('ij,ij->i',a,np.cross(b,c))
 return np.sum(det[:,None]*(a+b+c),axis=0)/(4*sum(det)),sum(det)/6

def quantities(s,base,f,center=True):
 p=base*s[:,None]
 a,b,c=p[f[:,0]],p[f[:,1]],p[f[:,2]]
 det=(a*torch.linalg.cross(b,c)).sum(1)
 ctr=(det[:,None]*(a+b+c)).sum(0)/(4*det.sum())
 if center:
  p=p-ctr
  a,b,c=p[f[:,0]],p[f[:,1]],p[f[:,2]]
 n=torch.linalg.cross(b-a,c-a)
 q=n/(n*a).sum(1)[:,None]
 return p,q,ctr

def arrow_matrix(v):
 norm=(v*v).sum(1)
 return (v@v.T-norm[:,None])/norm[:,None]

def tree(v,root=None):
 a=arrow_matrix(v)
 if root is None:root=int(np.argmax((v*v).sum(1)))
 m=len(v); best=np.full(m,-np.inf);best[root]=np.inf
 used=np.zeros(m,bool);parent=np.full(m,-1,int)
 for k in range(m):
  j=int(np.argmax(np.where(used,-np.inf,best)));used[j]=True
  cand=np.minimum(best[j],a[:,j]);sel=(~used)&(cand>best)
  best[sel]=cand[sel];parent[sel]=j
 return float(min(best)),parent,root

def diag(v):
 a=arrow_matrix(v);np.fill_diagonal(a,-np.inf)
 return dict(count=int(sum(np.max(a,axis=1)<-1e-10)),weakish=int(sum(abs(np.max(a,axis=1))<=1e-10)),beta=tree(v)[0],minlocal=float(min(np.max(a,axis=1))),root=tree(v)[2])

def state(s,base):
 v=base*s[:,None];f=topology(v)
 p,q,c=quantities(torch.tensor(s,dtype=DT),torch.tensor(base,dtype=DT),torch.tensor(f))
 p,q,c=p.numpy(),q.numpy(),c.numpy()
 ids=np.unique(np.round(q,8),axis=0,return_index=True)[1];q=q[np.sort(ids)]
 return dict(V=len(np.unique(f)),F=len(q),triangles=len(f),centroid=c.tolist(),S=diag(q),U=diag(p)),f,p,q

def prepare(path):
 points=np.array(json.load(open(path)),float)/1e5
 c,vol=mass_np(points,topology(points))
 return points-c

def run(base,out,steps=100,trust=.02,guard=1e-7,root=None):
 n=len(base);s=np.ones(n)
 if pathlib.Path(out,'checkpoint.json').exists(): s=np.array(json.load(open(pathlib.Path(out,'checkpoint.json')))['s'])
 bt=torch.tensor(base,dtype=DT)
 a=arrow_matrix(base);np.fill_diagonal(a,-np.inf);rr=np.argmax(a,axis=1);ur=int(np.argmax((base*base).sum(1)))
 ui=np.array([i for i in range(n) if i!=ur]);uj=rr[ui]
 L=np.zeros((len(ui),n))
 for k,(i,j) in enumerate(zip(ui,uj)):
  L[k,j]=base[i]@base[j];L[k,i]-=base[i]@base[i]
 ref=(base[ui]*base[ui]).sum(1)
 history=[]
 for it in range(steps):
  st,f,p,q=state(s,base)
  ft=torch.tensor(f)
  pt,qt,ct=quantities(torch.tensor(s,dtype=DT),bt,ft)
  q0=qt.numpy();beta,par,rt=tree(q0,root)
  ix=np.array([i for i in range(len(q0)) if i!=rt]);jx=par[ix]
  def fun(x):
   p,q,c=quantities(x,bt,ft)
   u=q[torch.tensor(ix)];w=q[torch.tensor(jx)]
   flow=(u*(w-u)).sum(1)/(u*u).sum(1)
   return torch.cat([c,flow])
  ts=torch.tensor(s,dtype=DT,requires_grad=True)
  val=fun(ts).detach().numpy();jac=torch.autograd.functional.jacobian(fun,ts,vectorize=True).numpy()
  m=len(ix)
  cost=np.r_[np.zeros(n),np.ones(m)]
  Aub=np.vstack([np.c_[-jac[3:],-np.eye(m)],np.c_[-L,np.zeros((len(ui),m))]])
  bub=np.r_[val[3:]-guard,L@s-guard*ref]
  Aeq=np.c_[jac[:3],np.zeros((3,m))];beq=-val[:3]
  lp=linprog(cost,A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=beq,bounds=[(-trust*max(abs(t),.2),trust*max(abs(t),.2)) for t in s]+[(0,None)]*m,method='highs')
  if not lp.success:
   print('LP_FAIL',it,lp.message,flush=True);break
  oldloss=float(sum(np.maximum(guard-val[3:],0)))
  ds=lp.x[:n];accepted=False
  for alpha in [1,.5,.25,.125,.0625,.03125,.015625]:
   sp=s+alpha*ds
   if min(sp)<=0:continue
   st2,f2,p2,q2=state(sp,base)
   _,par2,rt2=tree(q2)
   ar=arrow_matrix(q2);newloss=sum(max(0,guard-ar[i,par2[i]]) for i in range(len(q2)) if i!=rt2)
   merit=newloss+50*np.linalg.norm(st2['centroid'])
   oldmerit=oldloss+50*np.linalg.norm(st['centroid'])
   if merit < oldmerit-1e-9:
    s=sp;accepted=True;break
  record=dict(iteration=it,oldloss=oldloss,newloss=float(newloss),alpha=alpha,accepted=accepted,**(st2 if accepted else st))
  history.append(record)
  pathlib.Path(out).mkdir(exist_ok=True,parents=True)
  json.dump(dict(s=s.tolist(),base=base.tolist(),history=history),open(pathlib.Path(out,'checkpoint.json'),'w'),indent=2)
  print(json.dumps(record),flush=True)
  if not accepted:
   trust*=.5
   if trust<1e-7:break
  else: trust=min(trust*1.1,.05)
  if record['S']['count']==1 and record['U']['count']==1 and record['S']['weakish']==0 and record['U']['weakish']==0:
   print('NUMERICAL_SU11_ONLY_EXACT_AUDIT_REQUIRED',flush=True);break
 return s

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--points',default='points.json');ap.add_argument('--out',default='run');ap.add_argument('--steps',type=int,default=100);ap.add_argument('--trust',type=float,default=.02);a=ap.parse_args()
 base=prepare(a.points)
 print(json.dumps(state(np.ones(len(base)),base)[0]),flush=True)
 run(base,a.out,a.steps,a.trust)
```

## restored.py

Save verbatim including final newline:4534bytes,SHA293977f889ed2866074bb1358a31cdf3eed41dff6404479f680bca291f8210b7. This includes the exact later history-retention patch; it changes continuation record numbering, not geometry calculations. The first30 fresh-run geometry was produced by the same algorithm before that bookkeeping patch.

```python
"""Radial positive-flow cones with nonlinear filled-centroid restoration.
Float scout only. An SU11 report requires independent exact audit before acceptance.
"""
import argparse,json,pathlib
import numpy as np, torch, networkx as nx
from scipy.optimize import linprog, minimize, LinearConstraint
from scout import DT, topology, quantities, state, prepare, arrow_matrix

def policy(base,s,guard):
 p=base*s[:,None];a=arrow_matrix(p);np.fill_diagonal(a,-np.inf)
 root=int(np.argmax((p*p).sum(1)));ii=np.array([i for i in range(len(p)) if i!=root]);jj=np.argmax(a[ii],axis=1)
 L=np.zeros((len(ii),len(p)))
 for k,(i,j) in enumerate(zip(ii,jj)):
  L[k,j]=base[i]@base[j];L[k,i]=-base[i]@base[i]
 refs=(base[ii]*base[ii]).sum(1)
 return L,guard*refs,root

def arbo(v,guard=1e-6):
 a=arrow_matrix(v);n=len(v);r=int(np.argmax((v*v).sum(1)))
 G=nx.DiGraph();G.add_nodes_from(range(n))
 for i in range(n):
  if i==r:continue
  for j in range(n):
   if i==j:continue
   G.add_edge(j,i,weight=max(0,guard-a[i,j])+1e-13/(1+max(a[i,j],0)))
 tr=nx.minimum_spanning_arborescence(G,attr='weight')
 edges=np.array([(i,j) for j,i in tr.edges()],int)
 assert len(edges)==n-1
 loss=sum(max(0,guard-a[i,j]) for i,j in edges)
 return float(loss),edges,r

def restore(sp,base,L,rhs,tol=2e-12):
 bt=torch.tensor(base,dtype=DT);s=sp.copy()
 for it in range(12):
  f=torch.tensor(topology(base*s[:,None]));ts=torch.tensor(s,dtype=DT,requires_grad=True)
  fn=lambda x:quantities(x,bt,f)[2]
  c=fn(ts).detach().numpy()
  if max(abs(c))<tol and min(L@s-rhs)>-1e-11:return s
  J=torch.autograd.functional.jacobian(fn,ts,vectorize=True).numpy()
  res=minimize(lambda d:.5*(d@d),np.zeros(len(s)),jac=lambda d:d,
    constraints=[LinearConstraint(J,-c,-c),LinearConstraint(L,rhs-L@s,np.inf)],
    bounds=[(-.1*max(x,.1),.1*max(x,.1)) for x in s],
    method='SLSQP',options={'ftol':1e-20,'maxiter':100})
  if not res.success and np.linalg.norm(J@res.x+c)>1e-10:return None
  s+=res.x
  if min(s)<=0:return None
 return None

def run(base,out,steps=100,trust=.03,guard=2e-6):
 dest=pathlib.Path(out);dest.mkdir(parents=True,exist_ok=True)
 s=np.ones(len(base))
 if (dest/'checkpoint.json').exists():s=np.array(json.load(open(dest/'checkpoint.json'))['s'])
 bt=torch.tensor(base,dtype=DT);history=[]
 if (dest/'checkpoint.json').exists():history=json.load(open(dest/'checkpoint.json')).get('history',[])
 offset=len(history)
 for it in range(steps):
  st,f,p,q=state(s,base)
  ft=torch.tensor(f);ts=torch.tensor(s,dtype=DT,requires_grad=True)
  p0,q0,c0=quantities(ts,bt,ft);qn=q0.detach().numpy()
  oldloss,edges,root=arbo(qn,guard);ii=torch.tensor(edges[:,0]);jj=torch.tensor(edges[:,1])
  L,rhs,ur=policy(base,s,guard)
  def fn(x):
   p,q,c=quantities(x,bt,ft);u=q[ii];v=q[jj]
   return torch.cat([c,(u*(v-u)).sum(1)/(u*u).sum(1)])
  val=fn(ts).detach().numpy();J=torch.autograd.functional.jacobian(fn,ts,vectorize=True).numpy()
  n=len(s);m=len(edges)
  lp=linprog(np.r_[np.zeros(n),np.ones(m)],
    A_ub=np.vstack([np.c_[-J[3:],-np.eye(m)],np.c_[-L,np.zeros((len(L),m))]]),
    b_ub=np.r_[val[3:]-guard,L@s-rhs],A_eq=np.c_[J[:3],np.zeros((3,m))],b_eq=-val[:3],
    bounds=[(-trust*max(v,.2),trust*max(v,.2)) for v in s]+[(0,None)]*m,method='highs')
  if not lp.success:
   print('LP_FAIL',it,lp.message,flush=True);break
  ds=lp.x[:n];accepted=False;loss2=oldloss
  for alpha in [1,.5,.25,.125,.0625,.03125]:
   sp=restore(s+alpha*ds,base,L,rhs)
   if sp is None:continue
   st2,f2,p2,q2=state(sp,base)
   if st2['U']['count']!=1 or st2['U']['weakish']!=0:continue
   loss2,edges2,root2=arbo(q2,guard)
   if loss2 < oldloss-1e-10:
    s=sp;accepted=True;break
  rec=dict(iteration=offset+it,loss=oldloss,trial_loss=loss2,trust=trust,alpha=alpha,accepted=accepted,**(st2 if accepted else st))
  history.append(rec)
  json.dump(dict(s=s.tolist(),base=base.tolist(),history=history,guard=guard),open(dest/'checkpoint.json','w'),indent=2)
  print(json.dumps(rec),flush=True)
  if not accepted:
   trust*=.5
   if trust<1e-6:break
  else:trust=min(trust*1.2,.08)
  if rec['S']['count']==1 and rec['S']['weakish']==0:
   print('NUMERICAL_SU11_ONLY_EXACT_AUDIT_REQUIRED',flush=True);break
 return s

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--points',default='points.json');ap.add_argument('--out',default='restored');ap.add_argument('--steps',type=int,default=100);ap.add_argument('--trust',type=float,default=.03);ap.add_argument('--guard',type=float,default=2e-6);a=ap.parse_args()
 run(prepare(a.points),a.out,a.steps,a.trust,a.guard)
```

## Exact floating continuation checkpoint

Save the next one-line JSON without a trailing newline as RADIAL30_FLOAT_CHECKPOINT.json,4582bytes,SHA1aa8f941b5c82685935bb90e5d45b2c139846da6d976d1ed45c425adbb3f5213. This preserves all scientific inputs s/base/guard from the first30 restored iterations; the chronological history is deliberately not an input to the geometry algorithm. Decimal strings round-trip the actual binary64 values. For a continuation independent of recomputing base, load this checkpoint and call `restored.run(np.array(d['base']),out,steps,trust,d['guard'])`, placing the same JSON at out/checkpoint.json first. Re-numbering without an old history is harmless and should be identified as new records.

```json
{"s":[1.0614283900615467,1.0954958584406673,1.1117600925272988,1.0951386602630495,1.1214341124857554,1.1188113202743615,1.0821786902325619,0.6482976916911732,1.1120643620972168,1.094934897428424,1.0946886935972207,1.092718096708005,1.0926779373906255,1.0926029445550394,1.0918078143215335,1.091756626256096,1.0913200220005628,1.0912889688651213,1.0912750050483722,1.0910197845656384,1.0909975156432288,1.0909515444325566,1.0908414151861232,1.0907298180807863,1.0871440527988885,1.0830480012242145,1.0829287159421166,1.0828616067214587,1.0828538186199808,1.0825501646094147,1.0887721917388478,1.087828272710889,1.0862575308232103,1.0879740323570282,1.0867272268502504,1.09830353555202,1.1423136282770634,1.057926483397906,0.6482976916911732,1.170822334123421,1.1119780924740852,1.0787848465934358,1.1997848370098525,1.043718586799083,1.0893367027940988,1.0403935274712517,1.1108635111000524,1.1271474284414749,1.1064713181340438,1.124133056463906,1.0895293225953062,1.089649200371694,1.0672109667407303,1.0624885493768954,0.9924298328340019,1.172503213604551,0.6626269443268886],"base":[[-0.8356928365420778,-0.1963462836135381,-1.1730738071865945],[-0.05518283654207773,-0.0666362836135381,1.0434961928134054],[-0.00543283654207773,0.012483716386461896,1.0521461928134055],[0.3629571634579223,0.3239337163864619,1.0503461928134055],[0.3925071634579223,0.31594371638646185,-0.3238438071865946],[0.6152471634579222,0.5137337163864619,0.5713161928134054],[0.6076571634579222,0.43196371638646186,-0.10590380718659458],[0.6726971634579222,0.5224037163864619,0.4331061928134054],[0.7077571634579223,0.5259037163864618,0.16694619281340542],[0.18852716345792228,0.47650371638646183,1.0638161928134056],[0.09858716345792227,0.5533637163864619,1.0456261928134054],[0.010197163457922272,0.6078537163864619,1.0275561928134056],[-0.07869283654207773,0.6568537163864618,0.9995061928134054],[-0.1670928365420777,0.7023237163864618,0.9627661928134054],[-0.2570328365420777,0.7400337163864619,0.9207461928134054],[-0.3450228365420777,0.7728737163864619,0.8698661928134054],[-0.4272228365420777,0.8057237163864619,0.8087561928134054],[-0.5137928365420777,0.8221937163864619,0.7466761928134054],[-0.5937228365420778,0.8369237163864619,0.6754861928134054],[-0.6701928365420777,0.8447637163864619,0.5990861928134054],[-0.7417428365420777,0.8462137163864619,0.5170561928134054],[-0.8082328365420778,0.8407437163864618,0.4307561928134054],[-0.8687128365420778,0.8291237163864619,0.3403261928134054],[-0.9214428365420778,0.8130337163864618,0.24540619281340545],[-0.9741528365420777,0.7878337163864618,0.15210619281340543],[-1.0186228365420777,0.7592537163864619,0.05495619281340543],[-1.0519228365420776,0.7220237163864619,-0.04440380718659458],[-1.0758128365420776,0.6811637163864619,-0.14520380718659456],[-1.0883628365420777,0.6394437163864619,-0.24812380718659457],[-1.0972728365420776,0.5868237163864619,-0.3465438071865946],[-1.0941028365420777,0.5364337163864619,-0.4469338071865946],[-1.0893628365420776,0.4719237163864619,-0.5392438071865946],[-1.0806428365420777,0.40259371638646185,-0.6274338071865946],[-1.0623928365420776,0.32883371638646186,-0.7120438071865945],[-1.0324628365420776,0.25539371638646186,-0.7934638071865946],[-0.9721928365420778,0.08627371638646189,-0.9357238071865946],[0.7860071634579222,0.11477371638646189,0.2909261928134054],[0.09306716345792226,-0.3231262836135381,-0.9683538071865946],[-0.21086283654207771,-0.6346762836135381,-0.8844438071865947],[-0.030272836542077727,-0.8709662836135381,-0.4759938071865946],[0.1938071634579223,-0.9636162836135381,-0.3433638071865946],[0.22265716345792227,-0.9798962836135381,-0.08766380718659457],[0.04397716345792227,-0.8975462836135382,-0.25724380718659456],[0.46983716345792226,-0.1897462836135381,-0.6934338071865946],[-0.2633828365420777,-0.44304628361353815,-1.1716538071865945],[0.3188371634579223,-0.3950962836135381,-0.9295438071865946],[0.6042771634579223,-0.4221262836135381,-0.6394738071865946],[0.6408271634579222,-0.3111962836135381,-0.4637238071865946],[0.6949471634579222,0.03320371638646189,0.7352461928134054],[0.7038671634579222,-0.1845062836135381,0.3391661928134054],[0.08261716345792226,-0.6503362836135381,-1.0095338071865945],[0.2776571634579223,-0.8399262836135382,-0.7078638071865946],[0.4809871634579223,-0.1166462836135381,0.9071261928134055],[0.4872571634579223,-0.8641262836135382,-0.3995038071865946],[0.5114671634579222,-0.8744862836135381,-0.06458380718659458],[0.7375171634579222,-0.1441762836135381,0.17405619281340542],[0.5639271634579223,-0.4041062836135381,0.5452761928134054]],"guard":2e-06}
```

## Reconstruction and finite search commands

First recover points.json with RECOVER_LITERAL_RADIAL.py from [internal-source-reference]. Save the two complete source blocks above. In a clean directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scout.py --out initial40 --steps 40 --trust .02
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python restored.py --out restored30 --steps 30 --trust .03 --guard .000002
```

These are scientific finite-search replays, not guaranteed bit-identical floating branching across different library/platform versions. The exact descendant coordinates are independently literal and do not depend on repeating those optimizer decisions. To regenerate their defining integer points directly from the preserved floating checkpoint in the executed environment:

```python
import json,pathlib,numpy as np
x=json.load(open('RADIAL30_FLOAT_CHECKPOINT.json'))
p=np.asarray(x['base'])*np.asarray(x['s'])[:,None]
for g in [3,5,6]:
 o={'grid':10**g,'points':np.rint(p*10**g).astype(np.int64).tolist()}
 pathlib.Path(f'RADIAL30_G{g}.json').write_text(json.dumps(o,separators=(',',':')))
print('RADIAL30_ROUNDING_INPUTS_REPRODUCED')
```

Expected exact input hashes and complete independently checkable output identities are in the literal geometry material. The source hashes in this material identify all runnable helpers; no omitted helper or hidden path is needed.
