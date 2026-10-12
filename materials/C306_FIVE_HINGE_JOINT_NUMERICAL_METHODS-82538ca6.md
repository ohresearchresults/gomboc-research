# material-82538ca6284d

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Joint five-hinge and five-affine-metric finite search

Exact dependency: [internal-source-reference], C306_FIVE_HINGE_GAUGED_EXACT_RECOVERY.md. That capsule supplies the complete input and exact builder. Execute it to generate C306_FIVE_HINGE_FAMILY.json,617009bytes,SHA2568871c18923c8ff222c24c0ea8a38634081de2939245d44a2efc4548ad1693976. This material plus that exact capsule is a complete source closure. The giant previous archive is NOT required for these three programs.

Environment actually executed: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1. These numerical searches do not certify equilibria, no-extra-weak conditions, or global exclusions. Fixed open-cube maximal complex V64/E180/F118/C360 comes from the exact builder, not approximate coplanar grouping. All five t parameters are restricted numerically to[.0001,.9999]; any exact candidate on the boundary requires a new maximal-complex census. The determinant-one lower-triangular affine matrix has five real parameters; the full unrestricted parameterization covers SPD metrics up to scale/rotation, but these finite programs impose the explicit finite bounds below. The exact mass chart fixes the actual own volume centroid, not a fictitious reference point.

## Finite runs actually executed

Commands, run in the directory containing all source files and the generated exact family:

    OPENBLAS_NUM_THREADS=1 python joint_hinge_scout.py --method powell --starts 4 --maxfev 2500 --out JOINT_FIRST4.json
    OPENBLAS_NUM_THREADS=1 python joint_hinge_scout.py --method de --starts 1 --maxfev 300 --out JOINT_DE300.json
    OPENBLAS_NUM_THREADS=1 python sample_joint_hinges.py
    OPENBLAS_NUM_THREADS=1 python constrained_hinge.py --n 4 --maxiter 250 --mode rooted --out CONSTRAINED_ROOTED_0.json

All unspecified options are the exact defaults in the complete sources. Both optimizers use seed19092653, the three-distribution sample uses seed19092654, constrained initialization uses seed19092655. The sample source was reconstructed from the executed inline unit and then actually replayed to the SAME395759byte output hash.

Expected observed output identities (floating-point optimizer files can differ on another numerical platform; such a difference is not an exact geometric claim):
- JOINT_FIRST4.json4045bytes SHA2565c19b714ce5f32a0093514d1a018bd530e428ba48b770410cdda543153d25ba4.
- JOINT_DE300.json1650bytes SHA256571415ca73b144f2682673b6300685aaed4d9756be6e7fd098e932ef683cd433.
- SAMPLE12000.json395759bytes SHA2563cb3d63bba4f94c9601745624fee9a6de90a8aba0c1bac21346ed34c8cf1c919.
- CONSTRAINED_ROOTED_0.json4855bytes SHA25692eafc4c31cbe6dbdf189ff1f9c952b255da04b9ed2b94f9e6e200e3c52c942b.

Observed terminal summaries:
- JOINT_FINITE_DONE4,zero numericalSU11; four Powell endpoints had(S,U)=(2,4),(3,3),(2,3),(4,2), losses approximately.06197493,.002630822,.03430120,.55017581.
- JOINT_FINITE_DONE1,zero numericalSU11; DE300 took30221evaluations and ended at its iteration limit. Best local all-pair deficit squared sum3.572194730693746e-5 hadS3U3, affine condition177.3895. This lower residual is NOT class improvement. Its ten-parameter checkpoint is[0.7734873165964101,0.6789802088226832,0.6664222695133647,0.6927395067340832,0.46978034937754176,-1.6724544056236097,-1.0005239029768542,-0.6818223063108667,2.954067876333075,2.5484735493822264].
- JOINT_SAMPLE_12000_FINITE_DONE3957593cb3d63bba4f94c9601745624fee9a6de90a8aba0c1bac21346ed34c8cf1c919;2197sampledS1U2 and4sampledS1U3,noU1 sample. BestS1U2 local loss.05214406654359218 atsample3303, identitymetric and t=[.0016362816058040062,.03846091826561658,.6148639285359283,.006106104283667757,.05570776618734776].
- CONSTRAINED_FINITE_DONE4; all endpointsS1U2, rooted physical bottlenecks approximately[-.6952120169945,-.6189995998589,-.6952122526078,-.6189996194389]. The fixed optimizer roots alternate familyvertex2/19; these are family labels, not an implicit raw-lex renaming of a parent. Retested constraint violations were below3e-12. All are finite local endpoints, not a family obstruction. Positive S escape floor was1e-7, not an exact certificate.

The local mode computes every-point escape deficits; the rooted mode computes maximin paths on the TRUE open-family graph. Both choose a farthest-norm root for evaluation. Constrained optimization instead fixes its explicitly named root and retains a positive nonroot polar-escape floor. Improvement of local deficits is not proof of removal of the whole negative true-edge basin. The open scientific question is a construction or a rigorously scoped explanation of the surviving barrier, including different projection directions or low-complexity shifts outside this fixed five-hinge chart.

Save literal files using the exact UTF8 byte counts after each <<<FILE header; each Python source ends with one newline.

<<<FILE joint_hinge_scout.py 5187 3102f63913f80b9f3f0be785d53e0624c6d173fef301d733e11c7eb59518b22b>>>
"""Finite joint five-hinge/five-affine-metric search, never exact acceptance.
Requires the exact builder's C306_FIVE_HINGE_FAMILY.json. All geometries have
constant filled volume/centroid by its proved polynomial identities. Open-cube
facets are known, not inferred using approximate coplanar merging. Near the
boundary, this scout does not certify which degenerate features remain true.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,json,pathlib,time,hashlib
import numpy as np
from fractions import Fraction
from scipy.optimize import minimize,differential_evolution
ROOT=pathlib.Path(__file__).resolve().parent
FAMILY_SHA='8871c18923c8ff222c24c0ea8a38634081de2939245d44a2efc4548ad1693976'
def readarr(x):
 if isinstance(x,list):return [readarr(q)for q in x]
 return float(Fraction(x))
class Family:
 def __init__(self):
  raw=(ROOT/'C306_FIVE_HINGE_FAMILY.json').read_bytes();assert hashlib.sha256(raw).hexdigest()==FAMILY_SHA
  z=json.loads(raw);G=z['grid'];self.c=np.array(readarr(z['centroid_grid']))/G
  self.X=np.array(readarr(z['points_grid']))/G-self.c
  self.B=np.array(readarr(z['displacements_grid']))/G
  self.N=np.array(readarr(z['normals']));self.H=np.array(readarr(z['own_heights_grid']))/G
  self.faces=z['faces'];E={}
  for f,t in enumerate(self.faces):
   for i,j in zip(t,t[1:]+t[:1]):E.setdefault(tuple(sorted((i,j))),[]).append(f)
  self.E=np.array(list(E));self.D=np.array(list(E.values()));assert self.E.shape==self.D.shape==(180,2)
 def points(self,t):
  x=self.X.copy();x[:,2]+=self.B@t
  return x
 def geometry(self,t):
  x=self.points(t[:5]);N=self.N[:,0]+np.einsum('fkj,k->fj',self.N[:,1:],t[:5]);h=self.H[:,0]+self.H[:,1:]@t[:5]
  assert min(h)>0
  a,b,c,d,e=t[5:];L=np.array([[np.exp(a),0,0],[c,np.exp(b),0],[d,e,np.exp(-a-b)]])
  x=x@L;q=(N/h[:,None])@np.linalg.inv(L).T
  return x,q,L
 def evaluate(self,t,margin=1e-4,mode='local',details=False):
  x,q,L=self.geometry(t);counts=[];scores=[];bad=[];roots=[];res=[]
  for y,edges in [(x,self.E),(q,self.D)]:
   rad=np.linalg.norm(y,axis=1);delta=y[None,:,:]-y[:,None,:];dist=np.linalg.norm(delta,axis=2)
   W=np.einsum('ij,ikj->ik',y,delta)/(rad[:,None]*np.maximum(dist,1e-100));np.fill_diagonal(W,-np.inf)
   w=W.max(1);root=int(np.argmax(rad));counts.append(int((w < -1e-8).sum()));roots.append(root)
   ids=np.setdiff1d(np.arange(len(y)),[root]);scores.append(float(min(w[ids])))
   if mode=='rooted':
    adj=[[]for _ in y]
    for i,j in edges:adj[i].append(j);adj[j].append(i)
    cap=np.full(len(y),-np.inf);cap[root]=1.;done=np.zeros(len(y),bool)
    for _ in y:
     j=int(np.argmax(np.where(done,-np.inf,cap)));done[j]=True
     for i in adj[j]:
      if not done[i]:cap[i]=max(cap[i],min(cap[j],W[i,j]))
    w=cap
   r=np.maximum(margin-w[ids],0);res.extend(r);bad.append(float(min(w[ids])))
  loss=float(np.dot(res,res))
  if not details:return loss
  return loss,dict(U=counts[0],S=counts[1],roots=roots,min_nonroot_local=scores,
    min_nonroot_objective=bad,condition=float(np.linalg.cond(L)),parameters=list(map(float,t)),
    min_vertex_separation=float(np.min(np.linalg.norm(x[:,None]-x[None,:],axis=2)+np.eye(len(x))*1e30)))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--method',choices=['powell','de','lbfgs'],default='powell')
 ap.add_argument('--starts',type=int,default=20);ap.add_argument('--maxfev',type=int,default=3000)
 ap.add_argument('--seed',type=int,default=19092653);ap.add_argument('--mode',choices=['local','rooted'],default='local')
 ap.add_argument('--margin',type=float,default=1e-4);ap.add_argument('--out',default='JOINT_SCOUT.json');args=ap.parse_args()
 f=Family();rng=np.random.default_rng(args.seed);records=[];best=None;t0=time.time()
 bounds=[(1e-4,1-1e-4)]*5+[(-2.,2.)]*2+[(-3.,3.)]*3
 def obj(t):return f.evaluate(t,args.margin,args.mode)
 for k in range(args.starts):
  init=np.r_[rng.uniform(.05,.95,5),np.zeros(5)if k%3==0 else rng.normal(0,.3,5)]
  if k==0:init[:5]=.5
  if args.method=='de':
   opt=differential_evolution(obj,bounds,popsize=10,maxiter=args.maxfev,seed=args.seed+k,polish=True,tol=1e-9,atol=1e-13,updating='immediate')
  elif args.method=='lbfgs':
   opt=minimize(obj,init,method='L-BFGS-B',bounds=bounds,options=dict(maxfun=args.maxfev,ftol=1e-14,gtol=1e-8,maxls=40))
  else:
   opt=minimize(obj,init,method='Powell',bounds=bounds,options=dict(maxfev=args.maxfev,ftol=1e-10,xtol=1e-7))
  loss,met=f.evaluate(opt.x,args.margin,args.mode,True)
  rec=dict(start=k,initial=init.tolist(),loss=loss,metric=met,nfev=int(opt.nfev),success=bool(opt.success),message=str(opt.message));records.append(rec)
  if best is None or loss<best['loss']:best=rec
  out=dict(args=vars(args),family_sha256=FAMILY_SHA,bounds=bounds,records=records,best=best)
  (ROOT/args.out).write_text(json.dumps(out,sort_keys=True,separators=(',',':')))
  print('JOINT',k,loss,'SU',met['S'],met['U'],'cond',met['condition'],'seconds',round(time.time()-t0,2),flush=True)
  if met['S']==met['U']==1:print('NUMERICAL_SU11_REQUIRES_EXACT_CENSUS',met,flush=True)
 print('JOINT_FINITE_DONE',len(records),sum(r['metric']['S']==r['metric']['U']==1 for r in records),'best',best['loss'],flush=True)
if __name__=='__main__':main()
<<<FILE constrained_hinge.py 3223 fb0da165b0c4473ec3724fdfc350daf785ea9fb7c575466ea39cb9acc9ea558d>>>
"""Finite S1-constrained joint hinge/metric search with a true-edge U bottleneck.
No optimizer status or negative finite result is an exact geometric certificate.
All reported feasibility is explicitly retested against the numerical constraints.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,json,pathlib,time
import numpy as np
from scipy.optimize import minimize
from joint_hinge_scout import Family,ROOT,FAMILY_SHA

def scores(y):
 d=y[None]-y[:,None];r=np.linalg.norm(y,axis=1);s=np.linalg.norm(d,axis=2)
 W=np.einsum('ij,ikj->ik',y,d)/(r[:,None]*np.maximum(s,1e-100));np.fill_diagonal(W,-np.inf)
 return W,W.max(1)
def rooted(W,E,root):
 n=len(W);adj=[[]for _ in range(n)]
 for i,j in E:adj[i].append(j);adj[j].append(i)
 cap=np.full(n,-np.inf);cap[root]=1.;done=np.zeros(n,bool)
 for _ in range(n):
  j=int(np.argmax(np.where(done,-np.inf,cap)));done[j]=True
  for i in adj[j]:
   if not done[i]:cap[i]=max(cap[i],min(cap[j],W[i,j]))
 return cap

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,default=0);ap.add_argument('--n',type=int,default=4)
 ap.add_argument('--maxiter',type=int,default=350);ap.add_argument('--gamma',type=float,default=1e-7)
 ap.add_argument('--mode',choices=['local','rooted'],default='rooted');ap.add_argument('--out',default='CONSTRAINED.json');args=ap.parse_args()
 f=Family();rng=np.random.default_rng(19092655);records=[];tt=time.time();starts=[]
 for k in range(args.start+args.n):
  for trial in range(10000):
   t=np.r_[rng.beta(.4,4,5)*.998+.001,np.zeros(5)]
   x,q,_=f.geometry(t);_,ws=scores(q)
   if (ws<-1e-8).sum()==1 and min(ws[1:])>args.gamma:break
  else:raise RuntimeError('No admissible initial S1 point in finite initialization')
  starts.append(t)
 bounds=[(.0001,.9999)]*5+[(-2.,2.)]*2+[(-3.,3.)]*3+[(-2.,1.)]
 for k in range(args.start,args.start+args.n):
  t=starts[k];ru=[2,19][k%2];rs=0;iu=np.setdiff1d(np.arange(64),[ru]);ip=np.setdiff1d(np.arange(118),[rs])
  def con(z):
   x,q,_=f.geometry(z[:10]);W,wu=scores(x);_,ws=scores(q)
   if args.mode=='rooted':wu=rooted(W,f.E,ru)
   return np.r_[wu[iu]-z[10],ws[ip]-args.gamma]
  zz=np.r_[t,-1.];zz[10]+=min(con(zz)[:63])
  opt=minimize(lambda z:-z[10],zz,method='SLSQP',bounds=bounds,constraints=[dict(type='ineq',fun=con)],
    options=dict(maxiter=args.maxiter,ftol=1e-10,disp=False))
  loss,m=f.evaluate(opt.x[:10],details=True);viol=float(min(con(opt.x)));W,_=scores(f.geometry(opt.x[:10])[0])
  rcap=rooted(W,f.E,ru)
  rec=dict(k=k,initial=zz.tolist(),rootU=ru,rootS=rs,parameters=opt.x.tolist(),
    nfev=int(opt.nfev),nit=int(opt.nit),success=bool(opt.success),message=str(opt.message),
    min_constraint=viol,feasible_to_1e_7=viol>=-1e-7,true_edge_rooted_beta=float(min(rcap[iu])),metric=m,loss=loss)
  records.append(rec);(ROOT/args.out).write_text(json.dumps(dict(seed=19092655,args=vars(args),family_sha256=FAMILY_SHA,bounds=bounds,records=records),sort_keys=True,separators=(',',':')))
  print('CONSTRAINED',k,'delta',opt.x[10],'beta',rec['true_edge_rooted_beta'],'violation',viol,'SU',m['S'],m['U'],'nit',opt.nit,'seconds',time.time()-tt,flush=True)
 print('CONSTRAINED_FINITE_DONE',len(records),flush=True)
if __name__=='__main__':main()
<<<FILE sample_joint_hinges.py 1172 5ee8088e708e51aaf81f3aace984eec9eff8b1c411b599a939336b1d3d1f89c7>>>
"""Replay the finite three-distribution 12000-point joint family scout.
Not a continuum exclusion. Requires the companion exact family and evaluator.
"""
from joint_hinge_scout import Family,ROOT
import numpy as np
import json,collections,hashlib
f=Family();rng=np.random.default_rng(19092654)
cs=collections.Counter();best={};rows=[]
for k in range(12000):
 if k<4000:t=np.r_[rng.beta(.3,3,5)*.9998+.0001,np.zeros(5)]
 elif k<8000:t=np.r_[rng.uniform(.0001,.9999,5),rng.normal(0,.25,5)]
 else:t=np.r_[rng.beta(.3,3,5)*.9998+.0001,rng.normal(0,.1,5)]
 loss,m=f.evaluate(t,details=True);key=(m['S'],m['U']);cs[key]+=1
 if key not in best or loss<best[key]['loss']:best[key]=dict(loss=loss,metric=m,k=k)
 if key in [(1,2),(2,1),(1,1)] and(len(rows)<500 or key==(1,1)):
  rows.append(dict(loss=loss,metric=m,k=k))
out=dict(seed=19092654,n=12000,counts={str(k):v for k,v in cs.items()},
 best={str(k):v for k,v in best.items()},onepair=rows)
raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode()
(ROOT/'SAMPLE12000.json').write_bytes(raw)
print('JOINT_SAMPLE_12000_FINITE_DONE',len(raw),hashlib.sha256(raw).hexdigest(),dict((k,v)for k,v in cs.items()if min(k)==1))
