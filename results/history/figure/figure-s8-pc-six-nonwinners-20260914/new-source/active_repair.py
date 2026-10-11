"""Own-mass elastic repair on an exact support-deletion atlas.
Numerical discovery only. All checkpoints require independent exact validation.
Usage: active_repair.py INPUT OUTPUT STEPS [goal trust ridge]
Requires unchanged 30-file S8 source tree at ./source. The original anchor137
and incidence plan are retained; active_ids selects physical supports afterwards.
"""
import sys,json,hashlib,time,itertools
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import minimize
R=Path(__file__).resolve().parent;S=R/'source'
sys.path[:0]=[str(S/'parent/mechanism'),str(S/'parent/mechanism/parent_sources')]
from numeric import mechanics,topology
src=S/'parent/mechanism/parent_sources/atlas_opt.py'
manifest=json.loads((S/'SOURCE_MANIFEST.json').read_text());assert hashlib.sha256(src.read_bytes()).hexdigest()==manifest[str(src.relative_to(S))]['sha256']
txt=src.read_text()
patches=[("self.n=data['n_supports'];self.M=len(data['controls'])","self.n=data['n_supports'];self.M=len(data['controls']);self.ids=np.array(data.get('active_ids',list(range(self.n))),int);self.nphys=len(self.ids)"),
("best_triples(X[:self.n],self.owners)","best_triples(X[self.ids],self.owners)"),
("np.zeros((len(self.owners),self.n),bool)","np.zeros((len(self.owners),self.nphys),bool)"),
("X[:self.n][self.triples]","X[self.ids][self.triples]"),
("range(self.n) if i!=self.Sroot","range(self.nphys) if i!=self.Sroot"),
("q=XX[:self.n];dq=DXX[:self.n]","q=XX[self.ids];dq=DXX[self.ids]"),
("q=XX[:self.n]","q=XX[self.ids]")]
for a,b in patches:
 assert a in txt,a
 txt=txt.replace(a,b)
ns={};exec(compile(txt,'active_atlas_exact_source_patch','exec'),ns);Atlas=ns['Atlas']

def rooted(cos,root,mask=None):
 """Maximum-bottleneck paths to root; parents are always settled earlier."""
 n=len(cos); score=np.full(n,-np.inf);score[root]=np.inf
 parent=np.full(n,-1,int);done=np.zeros(n,bool)
 for _ in range(n):
  i=int(np.argmax(np.where(done,-np.inf,score)));assert not done[i]
  assert i==root or np.isfinite(score[i])
  done[i]=True
  w=cos[:,i].copy()
  if mask is not None:w[~mask[:,i]]=-np.inf
  cand=np.minimum(score[i],w); improve=(~done)&(cand>score)
  score[improve]=cand[improve];parent[improve]=i
 for start in range(n):
  j=start;seen=set()
  while j!=root:
   assert j not in seen and j>=0;seen.add(j);j=int(parent[j])
 parent[root]=root
 return parent,score

def run(inp,out,steps,goal,trust,ridge):
 out.mkdir(parents=True,exist_ok=False)
 d=json.loads((inp/'GENERATOR.json').read_text());a=json.loads((inp/'A.json').read_text())
 fs=a['faces'];m=Atlas(d,fs);u=m.u0.copy()
 # Constrain outgoing arrows to genuine primal/dual adjacency. This is a
 # sufficient, complete-at-positive-sign test, not an assertion every argmax is adjacent.
 umask=np.zeros((len(m.owners),len(m.owners)),bool);smask=np.zeros((m.nphys,m.nphys),bool)
 for (i,j),ff in m.ef.items():umask[i,j]=umask[j,i]=True;smask[tuple(ff)]=smask[tuple(ff[::-1])]=True
 gf=1e-7;tf=1e-10;cut=.03
 def assign(s):
  m.uparent,_=rooted(s['cu'],m.Uroot,umask);m.sparent,_=rooted(s['cs'],m.Sroot,smask)
 def merit(s):
  e=np.maximum(goal-s['vals'],0);g=np.maximum(gf-s['gaps'][~m.inc],0);t=np.maximum(tf-s['det'],0)
  return float(np.sqrt(e@e+100*g@g+100*t@t))
 hist=[];t0=time.monotonic();last=None
 for it in range(steps):
  st=m.state(u,False);assign(st);st=m.state(u);loss=merit(st)
  rec=dict(it=it,loss=loss,minexit=float(st['vals'].min()),mingap=float(st['gaps'][~m.inc].min()),minheight=float(st['h'].min()),sec=time.monotonic()-t0)
  hist.append(rec)
  if it%10==0:print(out.name,rec,flush=True)
  if loss<1e-12 and st['vals'].min()>0:print('NUMERICAL_POSITIVE_ROOTED_FORESTS',out.name,flush=True);break
  geom=np.r_[st['dq'].reshape(-1,m.np)/2,st['dP'].reshape(-1,m.np)]
  _,ss,Vt=svd(geom,full_matrices=False,check_finite=False);W=Vt.T/np.maximum(ss,1e-7)
  vi,qi=np.where((~m.inc)&(st['gaps']<cut))
  A=np.r_[st['J'],10*m.gap_jac(st,vi,qi),10*st['ddet']]@W
  b=np.r_[goal-st['vals'],10*(gf-st['gaps'][vi,qi]),10*(tf-st['det'])]
  def fun(z):
   r=np.maximum(b-A@z,0);return .5*(r@r+ridge*(z@z)),-A.T@r+ridge*z
  rr=minimize(fun,np.zeros(W.shape[1]),jac=True,method='L-BFGS-B',bounds=[(-trust,trust)]*W.shape[1],options=dict(maxiter=250,ftol=1e-15,gtol=1e-11,maxls=30,maxcor=30))
  dz=W@rr.x;accepted=False
  for ls in range(20):
   un=u+2.**(-ls)*dz
   try:sn=m.state(un,False)
   except (np.linalg.LinAlgError,ValueError,FloatingPointError):continue
   newloss=merit(sn)
   if np.isfinite(newloss) and sn['h'].min()>.02 and newloss<loss*(1-1e-5*2.**(-ls)):
    u=un;accepted=True;rec.update(step=2.**(-ls),linear_status=rr.message);break
  if not accepted:
   print('LINESEARCH_NO_IMPROVEMENT',it,rr.message,flush=True);break
  last=loss
 st=m.state(u,False);assign(st);st=m.state(u,False)
 m.save(u,out/'GENERATOR.json')
 (out/'faces.json').write_text(json.dumps(fs,separators=(',',':')))
 (out/'history.json').write_text(json.dumps(hist,sort_keys=True,separators=(',',':')))
 # Re-evaluate the rounded integer checkpoint, not just the floating iterate.
 rd=json.loads((out/'GENERATOR.json').read_text());rm=Atlas(rd,fs);rs=rm.state(rm.u0,False)
 rep=mechanics(rs['q'],fs,P=rs['P'],tol=1e-12);rep.update(goal=goal,trust=trust,ridge=ridge,steps=steps,method='elastic_rooted_adjacent_LBFGSB',sec=time.monotonic()-t0)
 (out/'NUMERICAL.json').write_text(json.dumps(rep,sort_keys=True,separators=(',',':')))
 (out/'METHOD.json').write_text(json.dumps(dict(goal=goal,trust=trust,ridge=ridge,steps=steps,gapfloor=gf,tetrafloor=tf,gapcut=cut,svd_floor=1e-7,lbfgsb=dict(maxiter=250,ftol=1e-15,gtol=1e-11,maxls=30,maxcor=30),max_linesearch=20,primal_root=m.Uroot,dual_root=m.Sroot,roots_fixed=True,parents='maximum-bottleneck adjacent paths recomputed each iteration',parent_count=m.M,physical_support_count=m.nphys),sort_keys=True,separators=(',',':')))
 print('FINAL',out.name,rep,flush=True)
if __name__=='__main__':
 run(Path(sys.argv[1]).resolve(),Path(sys.argv[2]).resolve(),int(sys.argv[3]),float(sys.argv[4]) if len(sys.argv)>4 else 1e-6,float(sys.argv[5]) if len(sys.argv)>5 else .01,float(sys.argv[6]) if len(sys.argv)>6 else 1e-6)
