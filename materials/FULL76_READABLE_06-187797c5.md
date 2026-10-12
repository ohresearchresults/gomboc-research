# material-187797c56631

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# FULL76 exact readable source, part 6/8
# Each FILE header gives the exact following UTF-8 byte count and SHA-256.
# The newline after each payload is a framing separator, not a source byte.

FILE methods/ROOTED_ROUTING.py 3082 d6d7e5da04b732e9866c8cf9ff05f7451ed06659f9a3c79e225171c817006c42
"""Cycle-free least-deficit escape routing followed by full physical/mass correction.
Dijkstra proposals are numerical choices, not exclusion certificates. A competing
radial extremum may require switching its escape rather than selecting its local
best neighbour (which can create a two-cycle). Exact final auditing is separate.
"""
from MERGE_CONTACT import *
import heapq,time

def routing(A,root,power=2,tie=1e-14):
 W=arrows(A);n=len(A);cost=np.maximum(-W,0)**power+tie;np.fill_diagonal(cost,np.inf);dist=np.full(n,np.inf);dist[root]=0;queue=[(0.,root)];seen=set();nxt={}
 while queue:
  d,j=heapq.heappop(queue)
  if j in seen:continue
  seen.add(j)
  for i in range(n):
   if i in seen:continue
   nd=d+cost[i,j]
   if nd<dist[i]:dist[i]=nd;nxt[i]=j;heapq.heappush(queue,(float(nd),i))
 assert len(seen)==n and len(nxt)==n-1
 for i in range(n):
  s=set();j=i
  while j!=root:assert j not in s;s.add(j);j=nxt[j]
 return nxt,dist

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--power',type=int,default=2);ap.add_argument('--epochs',type=int,default=6);ap.add_argument('--steps',type=int,default=20);ap.add_argument('--goal',type=float,default=1e-7);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));raw=RECONSTRUCT.recover(G);sys.path.insert(0,str(ROOT/'parent'));import check_B
 rep=check_B.run(raw);(a.out/'INITIAL_B.json').write_bytes(B(rep));(a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'INPUT.json').write_bytes(B(dict(source_G_sha256=hashlib.sha256(B(G)).hexdigest(),power=a.power,epochs=a.epochs,steps=a.steps,goal=a.goal,versions=[platform.python_version(),np.__version__,scipy.__version__])));Q=np.array([[float(F(x,row[-1])) for x in row[:3]] for row in raw['H']]);s=FlexibleAtlas(G,rep,Q);z=np.zeros(s.n);history=[]
 print('INITIAL_ROUTING_B',rep['V'],rep['E'],rep['F'],rep['counts'],rep['weak'],flush=True)
 for epoch in range(a.epochs):
  s.forcedp={};s.forcedq={};s.last=None;v,J,g=s.evaluate(z);X=g['X'];c=g['centroid'] if 'centroid' in g else g['g'];p,pc=routing(X-c,s.U,a.power);q,qc=routing(g['Q']/(1-g['Q']@c)[:,None],s.S,a.power);s.forcedp=p;s.forcedq=q;s.last=None;(a.out/('ROUTES_'+str(epoch)+'.json')).write_bytes(B(dict(primal=p,polar=q)));old=z.copy();z=repair(s,z,a.out/str(epoch),steps=a.steps,goal=a.goal);v,J,g=s.evaluate(z);row=dict(epoch=epoch,minimum=float(v[:s.mechlen-2].min()),slack=float(g['slack'].min()),change=float(np.linalg.norm(z-old)));history.append(row);print('ROOTED_ROUTING_EPOCH',row,flush=True);GG=copy.deepcopy(s.G);GG['grid']=10**12;GG['controls']=np.rint(g['Y']*GG['grid']).astype(np.int64).tolist();(a.out/'GENERATOR.json').write_bytes(B(GG));(a.out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(a.out/'HISTORY.json').write_bytes(B(history));(a.out/'STATUS.json').write_bytes(B(row))
  if row['minimum']>0 and row['slack']>0:print('POSITIVE_NUMERICAL_ROUTING_ONLY',flush=True);break
  if row['change']<1e-15:break
if __name__=='__main__':main()

END FILE methods/ROOTED_ROUTING.py

FILE methods/S8_CHART.py 712 851b1a889a1690aae023f7fc258ba48f6250b7f8df03865495a144979e7a3d57
import json,hashlib,sys
from pathlib import Path
import chart
from check_A import encode
root=Path(sys.argv[1]);base=root/'baseline';base.mkdir(exist_ok=False)
for src,dst in [('raw.json','raw.json'),('B.json','A.json')]: (base/dst).write_bytes((root/src).read_bytes())
(base/'PROVENANCE.txt').write_text('The canonical A.json-format report in this numerical helper directory was emitted by completed exact auditor B, not a new execution of auditor A.\n')
d=chart.recover(root=root);out=json.dumps(encode(d),sort_keys=True,separators=(',',':')).encode();(root/'chart_exact.json').write_bytes(out);print('S8_EXACT_FAITHFUL_CHART',len(out),hashlib.sha256(out).hexdigest(),len(d['edges']),d['outer'],d['boundary'])

END FILE methods/S8_CHART.py

FILE methods/SEARCH.py 2608 ff346836c485eb24052a815784f9024fc4f05a633d3827cd3cf06176a735a69d
"""Finite next-union trials; numerical states are never exact acceptance."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from general_atlas import *
from REFINE import correct,warm
from numeric import Chart
import argparse,time,hashlib,platform,scipy
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def seed(c,e,mode):
 if mode=='stress':
  w=c.w.copy();w[e]=0.;return c.solve(w)[0]
 return c.Q.copy()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--edge',type=int);ap.add_argument('--steps',type=int,default=50);ap.add_argument('--warm',type=int,default=0);ap.add_argument('--mode',default='stress');ap.add_argument('--out',type=Path);a=ap.parse_args();c=Chart()
 if a.edge is None:
  results=[]
  for candidate in json.loads((ROOT/'ELIGIBLE.json').read_text()):
   for mode in ('stress','direct'):
    try:
     Q=seed(c,candidate['edge'],mode);s=GeneralAtlas(candidate['edge'],Q);v,J,g=s.evaluate(np.zeros(s.n))
     results.append(dict(**candidate,mode=mode,n=s.n,merit=float(np.linalg.norm(s.residual(np.zeros(s.n)))),mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),patch=s.patch))
    except Exception as ex:results.append(dict(**candidate,mode=mode,error=str(ex)))
  (ROOT/'SCREEN.json').write_bytes(B(results));print(json.dumps(sorted([r for r in results if 'merit' in r],key=lambda r:r['merit'])[:30],indent=2));return
 out=a.out;out.mkdir(parents=True,exist_ok=False);Q=seed(c,a.edge,a.mode);s=GeneralAtlas(a.edge,Q);s.checkpoint_dir=out;z=np.zeros(s.n);t=time.time()
 checkpoint=dict(edge=a.edge,mode=a.mode,patch=s.patch,initial_Q_hex=[[float(x).hex() for x in row] for row in Q],versions=[platform.python_version(),np.__version__,scipy.__version__],warm=a.warm,steps=a.steps)
 (out/'INPUT.json').write_bytes(B(checkpoint))
 if a.warm:z=warm(s,a.warm);(out/'WARM_Z.json').write_bytes(B([float(x).hex() for x in z]))
 z,records=correct(s,z,steps=a.steps);v,J,g=s.evaluate(z)
 G=copy.deepcopy(s.G);G['grid']=10**9;G['controls']=np.rint(g['Y']*G['grid']).astype(np.int64).tolist()
 (out/'GENERATOR.json').write_bytes(B(G));(out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(out/'RECORDS.json').write_bytes(B(records))
 status=dict(edge=a.edge,mode=a.mode,merit=float(np.linalg.norm(s.residual(z))),mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),time=time.time()-t,gen_sha=hashlib.sha256(B(G)).hexdigest())
 (out/'STATUS.json').write_bytes(B(status));print('FINITE_TRIAL_END',json.dumps(status),flush=True)
if __name__=='__main__':main()

END FILE methods/SEARCH.py

FILE methods/SOFT_SVD.py 4682 0c21b1562e23bcd80c4473cdc0761a6470c35b06a7d45033baa550d3e58932a6
"""Adaptive damped Gauss-Newton in the full physical SVD metric, own-filled mass.
All mechanical exits are reevaluated; numerical proposals only. Boundaries are
checked nonlinearly. The exact hull and all cone census are external acceptance.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from flexible import *
from TREE_REPAIR import tree
from scipy.linalg import svd,cho_factor,cho_solve
import argparse,platform,scipy,time,hashlib
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT,check_B
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def repair(s,z,out,steps=500,goal=3e-7,trust=.02):
 z=z.copy();out=Path(out);mu=1e-4;history=[];t0=time.time();gf=1e-8;tf=1e-10;geomweight=100.
 def residual(v,J,g):
  qi,vi=np.where(s.mask);gs=g['slack'][qi,vi];tri=g['v6'];vm=v[:s.mechlen-2];active=vm<goal;ag=gs<gf;at=tri<tf;dcs=-np.einsum('icp,ic->ip',g['DQ'][qi[ag]],g['X'][vi[ag]])-np.einsum('ic,icp->ip',g['Q'][qi[ag]],g['DX'][vi[ag]]);dtri=(J[s.mechlen+s.nq:s.mechlen+s.nq+len(s.tris)]*s.tscale[:,None])[at]
  r=np.r_[vm[active]-goal,geomweight*(gs[ag]-gf),geomweight*(tri[at]-tf)];D=np.vstack((J[:s.mechlen-2][active],geomweight*dcs,geomweight*dtri));return r,D
 for it in range(steps):
  v,J,g=s.evaluate(z);r,D=residual(v,J,g);score=float(r@r);row=dict(it=it,score=score,mech=float(v[:s.mechlen-2].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),mu=mu);history.append(row)
  if it%5==0:print('SOFT_SVD',json.dumps(row),flush=True)
  G=copy.deepcopy(s.G);G['grid']=10**12;G['controls']=np.rint(g['Y']*G['grid']).astype(np.int64).tolist();(out/'GENERATOR.json').write_bytes(B(G));(out/'Z.json').write_bytes(B([float(t).hex() for t in z]));(out/'HISTORY.json').write_bytes(B(history))
  if v[:s.mechlen-2].min()>goal*.99 and g['slack'].min()>gf and g['v6'].min()>tf:break
  mat=np.vstack((g['DQ'].reshape(-1,s.n)/2,g['DX'].reshape(-1,s.n)));_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);W=Vt.T/np.maximum(dd,1e-9);A=D@W;grad=A.T@r;row['gradient']=float(np.linalg.norm(grad));accepted=False
  for trial in range(8):
   try:dy=cho_solve(cho_factor(A.T@A+mu*np.eye(s.n),lower=True,check_finite=False),-grad,check_finite=False)
   except np.linalg.LinAlgError:mu*=10;continue
   if np.max(abs(dy))>trust:dy*=trust/np.max(abs(dy))
   for ls in range(15):
    zz=z+(2.**-ls)*W@dy
    try:vn,Jn,gn=s.evaluate(zz);rn,Dn=residual(vn,Jn,gn);sn=float(rn@rn)
    except (ValueError,np.linalg.LinAlgError):continue
    # Strictly convex source stays on the same nominal exposed complex.
    keepgeo=(g['slack'].min()<=0 or gn['slack'].min()>1e-11) and (g['v6'].min()<=0 or gn['v6'].min()>1e-13)
    if np.isfinite(sn) and keepgeo and np.min(1-gn['Q']@gn['g'])>.2 and sn<score*(1-1e-6*2.**-ls):z=zz;accepted=True;break
   if accepted:
    mu=max(1e-12,mu*(.3 if ls<2 else 3));break
   mu=min(1e12,mu*10)
  row['accepted']=accepted;row['halvings']=ls
  if not accepted:break
 v,J,g=s.evaluate(z);G=copy.deepcopy(s.G);G['grid']=10**12;G['controls']=np.rint(g['Y']*G['grid']).astype(np.int64).tolist();(out/'GENERATOR.json').write_bytes(B(G));(out/'Z.json').write_bytes(B([float(t).hex() for t in z]));(out/'HISTORY.json').write_bytes(B(history));status=dict(mech=float(v[:s.mechlen-2].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),seconds=time.time()-t0,sha=hashlib.sha256(B(G)).hexdigest());(out/'STATUS.json').write_bytes(B(status));print('SOFT_END_NUMERICAL_ONLY',json.dumps(status),flush=True)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--steps',type=int,default=500);ap.add_argument('--goal',type=float,default=3e-7);ap.add_argument('--tree',action='store_true');a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));raw=RECONSTRUCT.recover(G);rep=check_B.run(raw);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=FlexibleAtlas(G,rep,Q);(a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'SOURCE_B.json').write_bytes(B(rep));v,J,g=s.evaluate(np.zeros(s.n))
 if a.tree:
  s.forcedp,p=tree(g['X']-g['g'],s.U,a.goal);s.forcedq,q=tree(Q/(1-Q@g['g'])[:,None],s.S,a.goal);(a.out/'WITNESSES.json').write_bytes(B(dict(primal=s.forcedp,polar=s.forcedq,stats=[p,q])));s.last=None
 (a.out/'INPUT.json').write_bytes(B(dict(steps=a.steps,goal=a.goal,tree=a.tree,versions=[platform.python_version(),np.__version__,scipy.__version__])));print('SOFT_INITIAL_EXACT_B',rep['V'],rep['E'],rep['F'],rep['counts'],rep['weak'],flush=True);repair(s,np.zeros(s.n),a.out,steps=a.steps,goal=a.goal)
if __name__=='__main__':main()

END FILE methods/SOFT_SVD.py

FILE methods/STRESS_MERGE.py 2047 6b6616f5460db56bf3baff2ab7ca8d9e1d6341c630242181dd42c18a53f36fc5
"""Nonsimple panel identification initialized by its actual maximal stress chart."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from MERGE_CONTACT import *
from numeric import Chart

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--chart',type=Path,required=True);ap.add_argument('--nodes',type=int,nargs=2,required=True);ap.add_argument('--steps',type=int,default=120);ap.add_argument('--goal',type=float,default=1e-7);ap.add_argument('--dynamic',action='store_true');ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));rep=json.load(open(a.chart/'baseline/A.json'));GG,nr,changes=merge(G,rep,*a.nodes);c=Chart(a.chart);pair=sorted(set(changes['parent_groups'][0])&set(changes['parent_groups'][1]));edge=next(i for i,p in enumerate(c.edges) if list(p)==pair);weights=c.w.copy();weights[edge]=0;from RELIFT import seed
 Q,relift=seed(c,weights);(a.out/'RELIFT.json').write_bytes(B(relift));s=FlexibleAtlas(GG,nr,Q)
 if not a.dynamic:
  s.forcedp,mp,ch=inherited(rep,s.owners);g=np.array([float(F(x)) for x in rep['raw_centroid']]);aq=arrows(c.Q/(1-c.Q@g)[:,None]);sp=np.argmax(aq,axis=1);s.forcedq={i:int(sp[i]) for i in range(s.nq) if i!=s.S};(a.out/'WITNESSES.json').write_bytes(B(dict(primal=s.forcedp,polar=s.forcedq)))
 s.last=None;(a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'INITIAL_GENERATOR.json').write_bytes(B(GG));(a.out/'NOMINAL_COMPLEX.json').write_bytes(B(nr));(a.out/'CHANGES.json').write_bytes(B(changes));(a.out/'INITIAL_Q_HEX.json').write_bytes(B([[float(x).hex() for x in row] for row in Q]));(a.out/'INPUT.json').write_bytes(B(dict(nodes=a.nodes,pair=pair,edge=edge,steps=a.steps,goal=a.goal,dynamic=a.dynamic,versions=[platform.python_version(),np.__version__,scipy.__version__])));print('STRESS_MERGE_START',pair,edge,flush=True);repair(s,np.zeros(s.n),a.out,steps=a.steps,goal=a.goal)
if __name__=='__main__':main()

END FILE methods/STRESS_MERGE.py

FILE methods/SVD_CORRECT.py 2944 2f292886d9825bd6fcc106a5163b8e0b52696bb9887ed38ab68cbe93a5dd8daf
"""Full physical-coordinate SVD reconditioning, actual-mass correction and inherited exits.
Adapted to the contact atlas from the literal S8 repair method. Numerical only.
"""
from contact import *
from scipy.linalg import svd
import minnorm_qp, time, hashlib
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def repair(s,z,out,steps=80,goal=1e-7,trust=.03):
 z=np.array(z).copy();out=Path(out);out.mkdir(parents=True,exist_ok=True);history=[];gf=1e-8;tf=1e-10;t0=time.time()
 def merit(v,g):
  ev=np.minimum(v[:s.mechlen-2]-goal,0);gv=np.minimum(g['slack'][np.isfinite(g['slack'])]-gf,0);dv=np.minimum(g['v6']-tf,0)
  return float(np.sqrt(ev@ev+100*gv@gv+100*dv@dv))
 for it in range(steps):
  v,J,g=s.evaluate(z);m=merit(v,g);r=dict(it=it,merit=m,mech=float(v[:s.mechlen-2].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),trust=trust);history.append(r);print('SVD_CORRECT',json.dumps(r),flush=True)
  G=copy.deepcopy(s.G);G['grid']=10**12;G['controls']=np.rint(g['Y']*G['grid']).astype(np.int64).tolist();(out/'GENERATOR.json').write_bytes(B(G));(out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(out/'HISTORY.json').write_bytes(B(history))
  if m<1e-12 and v[:s.mechlen-2].min()>goal*.9:break
  mat=np.vstack((g['DQ'].reshape(-1,s.n)/2,g['DX'].reshape(-1,s.n)));_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);W=Vt.T/np.maximum(dd,1e-9);r['condition']=float(dd.max()/max(dd.min(),1e-30))
  qi,vi=np.where(s.mask&(g['slack']<.06));dcs=-np.einsum('icp,ic->ip',g['DQ'][qi],g['X'][vi])-np.einsum('ic,icp->ip',g['Q'][qi],g['DX'][vi]);dtri=J[s.mechlen+s.nq:s.mechlen+s.nq+len(s.tris)]*s.tscale[:,None]
  A=np.vstack((J[:s.mechlen-2],dcs,dtri))@W;b=np.r_[goal*1.1-v[:s.mechlen-2],gf-g['slack'][qi,vi],tf-g['v6']]
  dz,why=minnorm_qp.solve(A,b,bound=trust,tol=2e-12,seconds=12,maxsteps=10000);r['qp']=why;print('SVD_QP',why,flush=True)
  if dz is None:
   trust=min(.2,trust*1.5)
   if it>2 and all('qp' in rr and rr['qp'].get('why')!='pass' for rr in history[-3:]):break
   continue
  good=False
  for ls in range(20):
   zz=z+2.**-ls*(W@dz)
   try:vn,Jn,gn=s.evaluate(zz);mn=merit(vn,gn)
   except (ValueError,np.linalg.LinAlgError,FloatingPointError):continue
   if np.min(1-gn['Q']@gn['g'])>.2 and np.isfinite(mn) and mn<m*(1-1e-4*2.**-ls):z=zz;good=True;break
  r['accepted']=good;r['halvings']=ls
  if not good:
   trust*=.5
   if trust<1e-6:break
 v,J,g=s.evaluate(z);G=copy.deepcopy(s.G);G['grid']=10**12;G['controls']=np.rint(g['Y']*G['grid']).astype(np.int64).tolist();(out/'GENERATOR.json').write_bytes(B(G));(out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(out/'HISTORY.json').write_bytes(B(history));status=dict(mech=float(v[:s.mechlen-2].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),time=time.time()-t0,sha=hashlib.sha256(B(G)).hexdigest());(out/'STATUS.json').write_bytes(B(status));print('SVD_END_NUMERICAL_ONLY',json.dumps(status),flush=True);return z

END FILE methods/SVD_CORRECT.py

FILE methods/SVD_REPAIR.py 1543 f41e74b5c350f2e5cdf95d3ad38932ce836b32cc0ca13fe014308894ac99763d
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from flexible import *
from SVD_CORRECT import repair
from TREE_REPAIR import tree
import argparse,platform,scipy
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT,check_B
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--tree',action='store_true');ap.add_argument('--goal',type=float,default=1e-7);ap.add_argument('--steps',type=int,default=80);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));raw=RECONSTRUCT.recover(G);rep=check_B.run(raw);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);(a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'SOURCE_B.json').write_bytes(B(rep));s=FlexibleAtlas(G,rep,Q);v,J,g=s.evaluate(np.zeros(s.n))
 if a.tree:
  Z=g['X']-g['g'];q=g['Q'];H=q/(1-q@g['g'])[:,None];s.forcedp,pp=tree(Z,s.U,a.goal);s.forcedq,qq=tree(H,s.S,a.goal);(a.out/'WITNESSES.json').write_bytes(B(dict(primal=s.forcedp,polar=s.forcedq,stats=[pp,qq])));s.last=None
 (a.out/'INPUT.json').write_bytes(B(dict(tree=a.tree,goal=a.goal,steps=a.steps,versions=[platform.python_version(),np.__version__,scipy.__version__])));print('SVD_INITIAL_EXACT_B',rep['V'],rep['E'],rep['F'],rep['counts'],rep['weak'],flush=True);repair(s,np.zeros(s.n),a.out,steps=a.steps,goal=a.goal)
if __name__=='__main__':main()

END FILE methods/SVD_REPAIR.py

FILE methods/TREE_REPAIR.py 5095 66ff2d65519701a7ba191fc7b1839d66c4d1e27acb6b3a712a4019ce956896d7
"""Rooted escape-tree pivots in full-contact own-filled-mass coordinates.
Every chosen arrow points to an earlier-settled Dijkstra vertex, excluding
impossible directed cycles. This is a search restriction, not an existence theorem.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from flexible import *
from REFINE import correct
from scipy.optimize import least_squares
import argparse,heapq,hashlib,time,scipy,platform
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT,check_B
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def arrows(A):
 e=A[None,:,:]-A[:,None,:];den=np.sqrt(np.maximum(np.sum(A*A,axis=1)[:,None]*np.sum(e*e,axis=2),1e-40));v=np.einsum('ic,ijc->ij',A,e)/den;np.fill_diagonal(v,-1e10);return v

def tree(A,root,floor,seed=0,noise=0.):
 V=arrows(A);cost=np.maximum(floor-V,0.)**2
 if noise:cost*=np.exp(np.random.default_rng(seed).normal(0,noise,cost.shape))
 np.fill_diagonal(cost,np.inf);dist=np.full(len(A),np.inf);dist[root]=0;parent={};done=np.zeros(len(A),bool);order=[]
 for _ in A:
  j=int(np.argmin(np.where(done,np.inf,dist)));assert np.isfinite(dist[j]);done[j]=True;order.append(j)
  for i in np.where(~done)[0]:
   w=dist[j]+cost[i,j]
   if w<dist[i]:dist[i]=w;parent[int(i)]=j
 rank={v:i for i,v in enumerate(order)};assert all(rank[j]<rank[i] for i,j in parent.items());return parent,dict(max_cost=float(dist.max()),sum_cost=float(sum(cost[i,j] for i,j in parent.items())),order=order)

def cycles(A,root):
 js=np.argmax(arrows(A),axis=1);ans=set()
 for start in range(len(A)):
  seen=[];v=start
  while v!=root and v not in seen:seen.append(v);v=int(js[v])
  if v!=root:
   cy=seen[seen.index(v):];k=cy.index(min(cy));ans.add(tuple(cy[k:]+cy[:k]))
 return sorted(ans)

def solve(G,rep,Q,out,phases=10,warm=1000,steps=40,seed=0,noise=0.,floor=1e-7):
 s=FlexibleAtlas(G,rep,Q);s.checkpoint_dir=out;s.floor[:s.mechlen-2]=floor;s.floor[s.mechlen-2:s.mechlen]=1e-5;s.floor[s.mechlen:s.mechlen+s.nq]=1e-9;s.floor[s.mechlen+s.nq:-s.nq-1]=1e-7;z=np.zeros(s.n);records=[];t=time.time()
 for phase in range(phases):
  s.forcedp={};s.forcedq={};s.last=None;v,J,g=s.evaluate(z);Z=g['X']-g['g'];Q=g['Q'];H=Q/(1-Q@g['g'])[:,None];cp,cq=cycles(Z,s.U),cycles(H,s.S);fp,tp=tree(Z,s.U,floor,seed+2*phase,noise);fq,tq=tree(H,s.S,floor,seed+2*phase+1,noise);s.forcedp=fp;s.forcedq=fq;s.last=None
  record=dict(phase=phase,initial_primal_argmax_cycles=cp,initial_polar_argmax_cycles=cq,primal_tree=fp,polar_tree=fq,primal_stats=tp,polar_stats=tq)
  print('TREE_PHASE',phase,'cycles',cp,cq,'cost',tp['sum_cost'],tq['sum_cost'],flush=True);best=[float('inf'),z.copy()];calls=[0]
  def fun(zz):
   r=s.residual(zz);m=float(r@r);calls[0]+=1
   if m<best[0]:best[:]=[m,zz.copy()]
   if calls[0]%200==0:print('TREE_WARM',phase,calls[0],best[0],flush=True)
   return r
  if warm:least_squares(fun,z,jac=s.derivative,max_nfev=warm,ftol=1e-13,xtol=1e-13,gtol=1e-13,x_scale='jac');z=best[1]
  (out/('WARM_'+str(phase)+'.json')).write_bytes(B([float(x).hex() for x in z]));z,h=correct(s,z,steps);record['correction']=h;s.forcedp={};s.forcedq={};s.last=None;v,J,g=s.evaluate(z);record['actual_mech']=float(v[:s.mechlen].min());record['slack']=float(g['slack'].min());record['det']=float(g['v6'].min());records.append(record)
  GG=copy.deepcopy(s.G);GG['grid']=10**12;GG['controls']=np.rint(g['Y']*GG['grid']).astype(np.int64).tolist();(out/'GENERATOR.json').write_bytes(B(GG));(out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(out/'RECORDS.json').write_bytes(B(records));(out/('GENERATOR_'+str(phase)+'.json')).write_bytes(B(GG));print('TREE_ACTUAL',phase,record['actual_mech'],record['slack'],record['det'],flush=True)
  if record['actual_mech']>floor*.7 and record['slack']>1e-10 and record['det']>0:break
 status=dict(mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),phases=len(records),time=time.time()-t,sha=hashlib.sha256(B(GG)).hexdigest());(out/'STATUS.json').write_bytes(B(status));print('TREE_NUMERICAL_ONLY',json.dumps(status),flush=True)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--phases',type=int,default=8);ap.add_argument('--warm',type=int,default=800);ap.add_argument('--steps',type=int,default=40);ap.add_argument('--seed',type=int,default=0);ap.add_argument('--noise',type=float,default=0);ap.add_argument('--floor',type=float,default=1e-7);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));raw=RECONSTRUCT.recover(G);rep=check_B.run(raw);(a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'SOURCE_B.json').write_bytes(B(rep));Q=np.array([[float(F(v,r[-1])) for v in r[:3]] for r in raw['H']]);(a.out/'INPUT.json').write_bytes(B(dict(phases=a.phases,warm=a.warm,steps=a.steps,seed=a.seed,noise=a.noise,floor=a.floor,versions=[platform.python_version(),np.__version__,scipy.__version__])));solve(G,rep,Q,a.out,a.phases,a.warm,a.steps,a.seed,a.noise,a.floor)
if __name__=='__main__':main()

END FILE methods/TREE_REPAIR.py

FILE methods/TRI_SVD.py 1829 f6d2b974e7dc48d53b9b6668c30713110f2cbe1f9171306b7c1ccc33d4529bf7
"""Exact-contact triangular union, inherited parent rooted exits, full-mass SVD repair."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from union_atlas import *
from CROSS_CAP import inherited
from TREE_REPAIR import arrows
from SVD_CORRECT import repair
import argparse,platform,scipy
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--report',type=Path,required=True);ap.add_argument('--pair',type=int,nargs=2,required=True);ap.add_argument('--steps',type=int,default=80);ap.add_argument('--goal',type=float,default=1e-7);ap.add_argument('--dynamic',action='store_true');ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));rep=json.load(open(a.report));raw=RECONSTRUCT.recover(G);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=UnionAtlas(G,rep,a.pair,Q)
 if not a.dynamic:
  s.forcedp,mp,ch=inherited(rep,s.owners);c=np.array([float(F(x)) for x in rep['raw_centroid']]);aq=arrows(Q/(1-Q@c)[:,None]);sp=np.argmax(aq,axis=1);s.forcedq={i:int(sp[i]) for i in range(s.nq) if i!=s.S};(a.out/'WITNESSES.json').write_bytes(B(dict(primal=s.forcedp,polar=s.forcedq,mapping=mp)))
 s.last=None;(a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'PATCH.json').write_bytes(B(s.patch));(a.out/'INITIAL_GENERATOR.json').write_bytes(B(s.G));(a.out/'INPUT.json').write_bytes(B(dict(pair=a.pair,steps=a.steps,goal=a.goal,dynamic=a.dynamic,versions=[platform.python_version(),np.__version__,scipy.__version__])));repair(s,np.zeros(s.n),a.out,steps=a.steps,goal=a.goal)
if __name__=='__main__':main()

END FILE methods/TRI_SVD.py

FILE methods/TURNOVER.py 4219 5bba2ed44bef8e960373299098108fed795d6d30b44ecc97d270bc4260458ee4
"""Finite incidence turnover: delete a triangular support and split an old quad.
All row labels in the input are original C626 labels. Numerical output needs exact audit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from flexible import *
from REFINE import warm,correct
import argparse,hashlib,platform,time,scipy
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT,check_B
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def exact_mixed(G):
 Y=[[F(v,G['grid']) for v in r] for r in G['controls']];Y[G['n_supports']]=[F(0),F(0),F(1)]
 for i,deps,axes in G['plan']:
  if not deps:continue
  rest=[k for k in range(3) if k not in axes];A=[[Y[j][a] for a in axes] for j in deps];b=[1-sum(Y[j][a]*Y[i][a] for a in rest) for j in deps]
  # Generic exact Gaussian elimination, dimension at most three.
  C=[row+[x] for row,x in zip(A,b)];n=len(deps)
  for k in range(n):
   p=next(j for j in range(k,n) if C[j][k]);C[k],C[p]=C[p],C[k];d=C[k][k];C[k]=[x/d for x in C[k]]
   for j in range(n):
    if j!=k:
     d=C[j][k];C[j]=[x-d*y for x,y in zip(C[j],C[k])]
  for a,row in zip(axes,C):Y[i][a]=row[-1]
 return Y

def open_contact(G,point):
 G=copy.deepcopy(G);n=G['n_supports'];assert point>=n;Y=exact_mixed(G);mapping={i:i-(i>point) for i in range(len(Y)) if i!=point};plan=[];changed=[]
 for i,deps,axes in G['plan']:
  if i==point:continue
  dd=[j for j in deps if j!=point];aa=axes
  if len(dd)!=len(deps):
   assert not dd,'This exact turnover opens a one-equation support solve';aa=[];changed.append([i,deps,axes,dd,aa])
  plan.append([mapping[i],[mapping[j] for j in dd],aa])
 removed=G['groups'].pop(point-n);G['plan']=plan;D=10**12;G['grid']=D;G['controls']=[[round(y*D) for y in row] for i,row in enumerate(Y) if i!=point]
 return G,dict(opened_original_group=removed,removed_contact_node=point,old_to_new=mapping,changed_plan=changed)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--delete',type=int,required=True);ap.add_argument('--point',type=int,choices=[179,180],required=True);ap.add_argument('--sign',type=int,choices=[-1,1],required=True);ap.add_argument('--eps',type=str,default='1/10000000');ap.add_argument('--warm',type=int,default=1500);ap.add_argument('--steps',type=int,default=70);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--loose',action='store_true');a=ap.parse_args();out=a.out;out.mkdir(parents=True,exist_ok=False)
 G=json.load(open(ROOT/'parent/GENERATOR.json'));G,change=open_contact(G,a.point);support=18 if a.point==179 else 127;G['controls'][support][2]+=a.sign*round(F(a.eps)*G['grid']);Y=exact_mixed(G);Q=np.array(Y[:G['n_supports']],float);GG,change2=delete_generator(G,a.delete,Q);raw=RECONSTRUCT.recover(GG);rep=check_B.run(raw);(out/'INITIAL_GENERATOR.json').write_bytes(B(GG));(out/'INITIAL_B.json').write_bytes(B(rep));(out/'CHANGES.json').write_bytes(B([change,change2]));print('TURNOVER_INITIAL_EXACT_B',rep['V'],rep['E'],rep['F'],rep['counts'],rep['weak'],flush=True)
 Q=np.array([[float(F(v,r[-1])) for v in r[:3]] for r in raw['H']]);s=FlexibleAtlas(GG,rep,Q);s.checkpoint_dir=out
 if a.loose:
  s.floor[:s.mechlen-2]=1e-7;s.floor[s.mechlen-2:s.mechlen]=1e-5;s.floor[s.mechlen:s.mechlen+s.nq]=1e-9;s.floor[s.mechlen+s.nq:-s.nq-1]=1e-6
 (out/'INPUT.json').write_bytes(B(dict(delete=a.delete,point=a.point,sign=a.sign,eps=a.eps,warm=a.warm,steps=a.steps,loose=a.loose,versions=[platform.python_version(),np.__version__,scipy.__version__])))
 t=time.time();z=warm(s,a.warm) if a.warm else np.zeros(s.n);(out/'WARM_Z.json').write_bytes(B([float(x).hex() for x in z]));z,h=correct(s,z,a.steps);v,J,g=s.evaluate(z);GG=copy.deepcopy(s.G);GG['grid']=10**12;GG['controls']=np.rint(g['Y']*GG['grid']).astype(np.int64).tolist();(out/'GENERATOR.json').write_bytes(B(GG));(out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(out/'RECORDS.json').write_bytes(B(h));status=dict(mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),n=s.n,time=time.time()-t,gen_sha=hashlib.sha256(B(GG)).hexdigest());(out/'STATUS.json').write_bytes(B(status));print('TURNOVER_FINAL_NUMERICAL_ONLY',json.dumps(status),flush=True)
if __name__=='__main__':main()

END FILE methods/TURNOVER.py

FILE methods/UNION_SEARCH.py 1922 6679d4c4c7e34b6be4ea4e2b7f4907a274dd88bfb02e1a3ea7236efb352bfee0
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from union_atlas import *
from REFINE import warm,correct
import argparse,time,hashlib,scipy,platform
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--report',type=Path,required=True);ap.add_argument('--pair',type=int,nargs=2,required=True);ap.add_argument('--warm',type=int,default=1000);ap.add_argument('--steps',type=int,default=100);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 G=json.load(open(a.generator));rep=json.load(open(a.report));raw=RECONSTRUCT.recover(G);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=UnionAtlas(G,rep,a.pair,Q);s.checkpoint_dir=a.out;(a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'SOURCE_REPORT.json').write_bytes(B(rep));(a.out/'INPUT.json').write_bytes(B(dict(pair=a.pair,warm=a.warm,steps=a.steps,versions=[platform.python_version(),np.__version__,scipy.__version__])));(a.out/'PATCH.json').write_bytes(B(s.patch));t=time.time();z=warm(s,a.warm) if a.warm else np.zeros(s.n);(a.out/'WARM_Z.json').write_bytes(B([float(x).hex() for x in z]));z,h=correct(s,z,a.steps);v,J,g=s.evaluate(z);G=s.G;G['grid']=10**12;G['controls']=np.rint(g['Y']*G['grid']).astype(np.int64).tolist();(a.out/'GENERATOR.json').write_bytes(B(G));(a.out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(a.out/'RECORDS.json').write_bytes(B(h));status=dict(mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),time=time.time()-t,sha=hashlib.sha256(B(G)).hexdigest());(a.out/'STATUS.json').write_bytes(B(status));print('UNION_NUMERICAL_ONLY',json.dumps(status),flush=True)
if __name__=='__main__':main()

END FILE methods/UNION_SEARCH.py

FILE methods/VERIFY_EXTRA.py 5075 28f26b9498e48a442ae43c4edc9d8e95f30c3ca16f1252ebeff996b26707b80a
"""Additional exact contact inverse, lineage, stress and connectivity checks."""
import sys,json,copy,itertools,hashlib
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent;sys.path.insert(0,str(ROOT/'parent'))
import RECONSTRUCT,check_A,check_B,chart,chart_audit
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def owners(rep):return {frozenset(rep['active_input_indices'][f] for f,cy in enumerate(rep['faces']) if v in cy):v for v in range(rep['V'])}
def atlas(G,raw,rep):
 n=G['n_supports'];D=G['grid'];Y=[[F(v,D) for v in row] for row in G['controls']];Y[n]=[F(0),F(0),F(1)]
 for i,deps,axes in G['plan']:
  if deps:
   rest=[k for k in range(3) if k not in axes];M=[[Y[j][k] for k in axes] for j in deps];rhs=[1-sum(Y[j][k]*Y[i][k] for k in rest) for j in deps]
   for k,value in zip(axes,RECONSTRUCT.solve(M,rhs)):Y[i][k]=value
  assert all(check_A.dot(Y[i],Y[j])==1 for j in deps)
 Q=[tuple(F(v,row[3]) for v in row[:3]) for row in raw['H']];assert list(map(tuple,Y[:n]))==Q;own=owners(rep);X=[tuple(map(F,row)) for row in rep['raw_vertices']]
 for j,g in enumerate(G['groups']):
  assert tuple(Y[n+j])==X[own[frozenset(g)]];tri=next(t for t in itertools.combinations(g,3) if check_A.det(*(Q[k] for k in t)));assert chart.inv3([Q[k] for k in tri],[F(1)]*3)==tuple(Y[n+j])
 axes={i:ax for i,d,ax in G['plan']};free=[(i,k) for i in range(len(Y)) if i!=n for k in range(3) if k not in axes[i]];assert all(Y[i][k]==F(G['controls'][i][k],D) for i,k in free);eq=sum(map(len,G['groups']));assert eq==sum(len(d) for i,d,ax in G['plan']);assert len(free)==rep['E']+3
 return dict(nodes=len(Y),supports=n,nonsimple_contact_points=len(G['groups']),contact_equations=eq,free_coordinates=len(free),free_indices=free,exact_forward_inverse_pass=True)
def connectivity(n,edges):
 adj=[set() for _ in range(n)]
 for u,v in edges:adj[u].add(v);adj[v].add(u)
 count=0
 for k in range(3):
  for gone in itertools.combinations(range(n),k):
   ban=set(gone);root=next(i for i in range(n) if i not in ban);seen={root};todo=[root]
   while todo:
    u=todo.pop()
    for v in adj[u]-ban-seen:seen.add(v);todo.append(v)
   assert len(seen)==n-k;count+=1
 return count

def verify(parent_root,child_audit,out):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);parent_root=Path(parent_root);child_audit=Path(child_audit);seed=chart.recover(root=parent_root);before=json.load(open(parent_root/'baseline/A.json'));after=json.load(open(child_audit/'A.json'));raw=json.load(open(child_audit/'raw.json'));G=json.load(open(child_audit/'GENERATOR.json'));a=atlas(G,raw,after);(out/'ATLAS.json').write_bytes(B(a));old,new=owners(before),owners(after);removed=sorted([sorted(o) for o in old.keys()-new.keys()]);added=sorted([sorted(o) for o in new.keys()-old.keys()]);assert removed==[[71,94,109,119],[71,109,116,126]];assert added==[[71,94,109,116,119,126]]
 protected=[[16,18,71,94],[87,108,122,127]];assert all(frozenset(g) in new for g in protected);Q=[tuple(F(v,row[3]) for v in row[:3]) for row in raw['H']];st=chart_audit.verify_geometry(Q,seed);assert st['zero_endpoint_pairs']==[[71,109]];assert st['positive_interior_count']==309;(out/'STRESS.json').write_bytes(B(st));refined=copy.deepcopy(seed)
 for group,pair in zip(protected,[[18,94],[87,127]]):
  f=next(i for i,cy in enumerate(refined['faces']) if set(cy)==set(group));cy=refined['faces'][f];i=cy.index(pair[0]);cy=cy[i:]+cy[:i];j=cy.index(pair[1]);first=cy[:j+1];second=cy[j:]+[cy[0]];assert len(first)==len(second)==3;refined['faces'][f]=first;refined['faces'].append(second)
 refined['edges']=sorted({tuple(sorted((i,j))) for cy in refined['faces'] for i,j in zip(cy,cy[1:]+cy[:1])});rs=chart_audit.verify_geometry(Q,refined);assert rs['zero_endpoint_pairs']==[[18,94],[71,109],[87,127]];(out/'REFINED_STRESS.json').write_bytes(B(rs));dualedges=set()
 for u,v in after['edges']:
  ff=[f for f,cy in enumerate(after['faces']) if u in cy and v in cy];assert len(ff)==2;dualedges.add(tuple(ff))
 assert dualedges==set(map(tuple,seed['edges']))-{(71,109)};conn=connectivity(after['F'],dualedges);assert conn==9454;result=dict(removed_owner_sets=removed,added_owner_sets=added,protected=[dict(owners=g,before=old[frozenset(g)],after=new[frozenset(g)]) for g in protected],merged_vertex=new[frozenset(added[0])],stable_faces=after['stable_face_ids'],unstable_vertices=after['unstable_vertices'],stable_cycle=after['faces'][3],degree_histogram=dict(Counter(map(len,new))),facet_histogram=dict(Counter(map(len,after['faces']))),zero_stresses=rs['zero_endpoint_pairs'],zero_stress_indices=rs['zero_edges'],weight_bits=rs['weight_bits'],three_connectivity_checks=conn,files={p.name:dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in out.iterdir() if p.is_file()});(out/'EXTRA.json').write_bytes(B(result));print('C624_FULL_CONTACT_LINEAGE_STRESS_INVERSE_PASS',json.dumps(result),flush=True);return result
if __name__=='__main__':verify(sys.argv[1],sys.argv[2],sys.argv[3])

END FILE methods/VERIFY_EXTRA.py

FILE methods/VERIFY_WINNER.py 3182 31b878582c6187850091742029ee533202d98746720e5b737bd011bb860460be
"""Exact C626-to-C622 maximal incidence, atlas inverse, and common stress audit."""
from VERIFY_EXTRA import *

def verify(parent_root,child_audit,out):
 parent_root=Path(parent_root);child_audit=Path(child_audit);out=Path(out);out.mkdir(parents=True,exist_ok=False);seed=chart.recover(root=parent_root);before=json.load(open(parent_root/'baseline/A.json'));after=json.load(open(child_audit/'A.json'));raw=json.load(open(child_audit/'raw.json'));G=json.load(open(child_audit/'GENERATOR.json'));aa=atlas(G,raw,after);(out/'ATLAS.json').write_bytes(B(aa));old,new=owners(before),owners(after)
 removed=sorted([sorted(o) for o in old.keys()-new.keys()]);added=sorted([sorted(o) for o in new.keys()-old.keys()]);assert removed==[[56,57,88,118],[71,94,109,119],[71,109,116,126],[88,118,122]];assert added==[[56,57,88,118,122],[71,94,109,116,119,126]];protected=[[16,18,71,94],[87,108,122,127]];assert all(frozenset(g) in new for g in protected)
 assert [after[k] for k in ['V','E','F']]==[176,311,137] and after['counts']==[1,1,0] and after['weak']==[0,0,0];assert after['active_input_indices']==list(range(137));Q=[tuple(F(v,row[3]) for v in row[:3]) for row in raw['H']];st=chart_audit.verify_geometry(Q,seed);assert st['zero_endpoint_pairs']==[[71,109],[88,118]] and st['positive_interior_count']==308;(out/'STRESS.json').write_bytes(B(st));refined=copy.deepcopy(seed)
 for group,pair in zip(protected,[[18,94],[87,127]]):
  f=next(i for i,cy in enumerate(refined['faces']) if set(cy)==set(group));cy=refined['faces'][f];i=cy.index(pair[0]);cy=cy[i:]+cy[:i];j=cy.index(pair[1]);first=cy[:j+1];second=cy[j:]+[cy[0]];assert len(first)==len(second)==3;refined['faces'][f]=first;refined['faces'].append(second)
 refined['edges']=sorted({tuple(sorted((i,j))) for cy in refined['faces'] for i,j in zip(cy,cy[1:]+cy[:1])});rs=chart_audit.verify_geometry(Q,refined);assert rs['zero_endpoint_pairs']==[[18,94],[71,109],[87,127],[88,118]];(out/'REFINED_STRESS.json').write_bytes(B(rs));dualedges=set()
 for u,v in after['edges']:
  ff=[f for f,cy in enumerate(after['faces']) if u in cy and v in cy];assert len(ff)==2;dualedges.add(tuple(ff))
 assert dualedges==set(map(tuple,seed['edges']))-{(71,109),(88,118)};conn=connectivity(after['F'],dualedges);assert conn==9454
 result=dict(removed_owner_sets=removed,added_owner_sets=added,protected=[dict(owners=g,before=old[frozenset(g)],after=new[frozenset(g)]) for g in protected],merged_vertices=[dict(owners=g,index=new[frozenset(g)]) for g in added],stable_faces=after['stable_face_ids'],unstable_vertices=after['unstable_vertices'],stable_cycle=after['faces'][3],degree_histogram=dict(Counter(map(len,new))),facet_histogram=dict(Counter(map(len,after['faces']))),zero_stresses=rs['zero_endpoint_pairs'],zero_stress_indices=rs['zero_edges'],weight_bits=rs['weight_bits'],three_connectivity_checks=conn,files={p.name:dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in out.iterdir() if p.is_file()});(out/'EXTRA.json').write_bytes(B(result));print('C622_FULL_CONTACT_LINEAGE_STRESS_INVERSE_PASS',json.dumps(result),flush=True);return result
if __name__=='__main__':verify(sys.argv[1],sys.argv[2],sys.argv[3])

END FILE methods/VERIFY_WINNER.py
