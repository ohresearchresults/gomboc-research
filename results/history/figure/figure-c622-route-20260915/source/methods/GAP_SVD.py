"""Staged full-physical SVD gap contraction, actual filled mass and fixed external exits.
Final contact equality is imposed rationally only after numerical root convergence.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from flexible import *
from union_atlas import UnionAtlas
from TREE_REPAIR import arrows
from scipy.linalg import svd
import minnorm_qp,argparse,time,platform,scipy
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--report',type=Path,required=True);ap.add_argument('--pair',nargs=2,type=int,required=True);ap.add_argument('--steps',type=int,default=150);ap.add_argument('--goal',type=float,default=1e-7);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--fraction',type=float,default=.2);a=ap.parse_args();out=a.out;out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));rep=json.load(open(a.report));raw=RECONSTRUCT.recover(G);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=FlexibleAtlas(G,rep,Q);pair=a.pair;u,v=[i for i,o in enumerate(s.owners) if all(q in o for q in pair)];assert len(s.owners[u])==len(s.owners[v])==3;assert u!=s.U and v!=s.U
 third=[next(k for k in s.owners[u] if k not in pair),next(k for k in s.owners[v] if k not in pair)];k=third[1];s.blockedp=[(u,v),(v,u)];s.mask[k,u]=False;s.mask[third[0],v]=False;keeptri=np.array([not(u in t and v in t) for t in s.tris]);z=np.zeros(s.n);vv,J,g=s.evaluate(z);az=arrows(g['X']-g['g']);az[u,v]=az[v,u]=-np.inf;s.forcedp={i:int(az[i].argmax()) for i in range(s.nv) if i!=s.U};ah=arrows(Q/(1-Q@g['g'])[:,None]);s.forcedq={i:int(ah[i].argmax()) for i in range(s.nq) if i!=s.S};s.last=None;norm=1-Q[k]@g['X'][u];assert norm>0;target=1-a.fraction;history=[];trust=.03;t0=time.time();gf=1e-8;tf=1e-10
 def get(z):
  vv,J,g=s.evaluate(z);f=(1-g['Q'][k]@g['X'][u])/norm;df=-(g['DQ'][k].T@g['X'][u]+g['Q'][k]@g['DX'][u])/norm;return vv,J,g,f,df
 def merit(vv,g,f):
  ev=np.minimum(vv[:s.mechlen-2]-a.goal,0);gv=np.minimum(g['slack'][np.isfinite(g['slack'])]-gf,0);dt=np.minimum(g['v6'][keeptri]-tf,0);return float(np.sqrt(ev@ev+100*gv@gv+100*dt@dt+(f-target)**2*.01))
 (out/'INPUT.json').write_bytes(B(dict(pair=pair,steps=a.steps,goal=a.goal,fraction=a.fraction,versions=[platform.python_version(),np.__version__,scipy.__version__])));(out/'SOURCE_GENERATOR.json').write_bytes(B(G));(out/'WITNESSES.json').write_bytes(B(dict(primal=s.forcedp,polar=s.forcedq,panels=[u,v],third=third,gap=norm)))
 for it in range(a.steps):
  vv,J,g,f,df=get(z);m=merit(vv,g,f);row=dict(it=it,gap=float(f),target=float(target),merit=m,mech=float(vv[:s.mechlen-2].min()),slack=float(g['slack'].min()),trust=trust);history.append(row);print('GAP_SVD',json.dumps(row),flush=True);(out/'Z.json').write_bytes(B([float(t).hex() for t in z]));(out/'HISTORY.json').write_bytes(B(history))
  if abs(f-target)<2e-8 and m<2e-7:
   if target==0:break
   target=max(0,target-a.fraction);m=merit(vv,g,f)
  mat=np.vstack((g['DQ'].reshape(-1,s.n)/2,g['DX'].reshape(-1,s.n)));_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);W=Vt.T/np.maximum(dd,1e-9);qi,vi=np.where(s.mask&(g['slack']<.06));dcs=-np.einsum('icp,ic->ip',g['DQ'][qi],g['X'][vi])-np.einsum('ic,icp->ip',g['Q'][qi],g['DX'][vi]);dtri=(J[s.mechlen+s.nq:s.mechlen+s.nq+len(s.tris)]*s.tscale[:,None])[keeptri];A=np.vstack((J[:s.mechlen-2],dcs,dtri))@W;b=np.r_[a.goal*1.1-vv[:s.mechlen-2],gf-g['slack'][qi,vi],tf-g['v6'][keeptri]];dz,why=minnorm_qp.solve(A,b,E=(df@W)[None,:],r=[target-f],bound=trust,tol=2e-12,seconds=12,maxsteps=10000);row['qp']=why
  if dz is None:
   trust=min(.2,trust*1.5)
   if it>3 and all(r.get('qp',{}).get('why')!='pass' for r in history[-4:]):break
   continue
  good=False
  for ls in range(20):
   zz=z+2.**-ls*(W@dz)
   try:vn,jn,gn,fn,dfn=get(zz);mn=merit(vn,gn,fn)
   except (ValueError,np.linalg.LinAlgError):continue
   if np.min(1-gn['Q']@gn['g'])>.2 and fn>=-1e-8 and np.isfinite(mn) and mn<m*(1-1e-4*2.**-ls):z=zz;good=True;break
  row['accepted']=good;row['halvings']=ls
  if not good:trust*=.5
  if trust<1e-7:break
 vv,J,g,f,df=get(z);GG=copy.deepcopy(G);GG['grid']=10**12;GG['controls']=np.rint(g['Y']*GG['grid']).astype(np.int64).tolist();(out/'UNMERGED_GENERATOR.json').write_bytes(B(GG));(out/'Z.json').write_bytes(B([float(t).hex() for t in z]));(out/'HISTORY.json').write_bytes(B(history));status=dict(gap=float(f),mech=float(vv[:s.mechlen-2].min()),slack=float(g['slack'].min()),seconds=time.time()-t0,root_converged=bool(abs(f)<2e-8))
 if status['root_converged']:
  merged=UnionAtlas(GG,rep,pair,g['Q']);_,_,gg=merged.evaluate(np.zeros(merged.n));GG=copy.deepcopy(merged.G);GG['grid']=10**12;GG['controls']=np.rint(gg['Y']*GG['grid']).astype(np.int64).tolist();(out/'GENERATOR.json').write_bytes(B(GG));(out/'PATCH.json').write_bytes(B(merged.patch))
 (out/'STATUS.json').write_bytes(B(status));print('GAP_END_NUMERICAL_ONLY',json.dumps(status),flush=True)
if __name__=='__main__':main()
