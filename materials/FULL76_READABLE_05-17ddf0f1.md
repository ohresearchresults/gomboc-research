# material-17ddf0f1b2ef

AI research material

---

# FULL76 exact readable source, part 5/8
# Each FILE header gives the exact following UTF-8 byte count and SHA-256.
# The newline after each payload is a framing separator, not a source byte.

FILE methods/GLOBAL8.py 4218 2414e693ba09eb808e0dbbbd4562c23fae4e8881f3306b0ef3d37f6a8cac4e55
"""Eight physical global variables with true recomputation of uniform filled mass.
X'=B X/(1+u.X), Q'=B^{-T}(Q+u), B=(1+u_z)A,
A=[[exp(a),0,0],[b,exp(c),0],[d,e,1]]. Apex001 is retained.
Numerical discovery only. Exact inputs are the audited raw H body and rational
matrix/translation serialized after quantization; no reference centre is used.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,sys,math,time,argparse,hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import least_squares
sys.set_int_max_str_digits(0)
BLOB=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--audit',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--starts',type=int,default=12);ap.add_argument('--steps',type=int,default=1000);ap.add_argument('--seed',type=int,default=420624);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);raw=json.load(open(a.audit/'raw.json'));rep=json.load(open(a.audit/'A.json'));Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);X=np.array([[float(F(t)) for t in row] for row in rep['raw_vertices']]);tri=np.array([(cy[0],cy[j],cy[j+1]) for cy in rep['faces'] for j in range(1,len(cy)-1)]);U=next(i for i,x in enumerate(X) if list(x)==[0,0,1]);S=rep['active_input_indices'][rep['stable_face_ids'][0]];active=rep['active_input_indices'];Q=Q[active];S=active.index(S)
 def edges_domain(edges,n):
  ed=np.array([e for p in edges for e in [p,p[::-1]]]);return ed[:,0],ed[:,1],[[k for k,(i,j) in enumerate(ed) if i==v] for v in range(n)]
 ep=edges_domain(rep['edges'],len(X));dual=set()
 for i,j in rep['edges']:
  ff=[f for f,cy in enumerate(rep['faces']) if i in cy and j in cy];assert len(ff)==2;dual.add(tuple(ff))
 eq=edges_domain(sorted(dual),len(Q));keep1=[i for i in range(len(X)) if i!=U];keep2=[i for i in range(len(Q)) if i!=S];last={}
 def escape(Z,ed):
  i,j,adj=ed;e=Z[j]-Z[i];val=np.einsum('ij,ij->i',Z[i],e)/np.sqrt(np.maximum(np.sum(Z[i]**2,axis=1)*np.sum(e**2,axis=1),1e-40));return np.array([max(val[g]) for g in adj])
 def evaluate(p):
  A=np.array([[np.exp(p[0]),0,0],[p[2],np.exp(p[1]),0],[p[3],p[4],1.]]);u=p[5:];B=(1+u[2])*A;den=1+X@u;xx=(X@B.T)/den[:,None];qq=(Q+u)@np.linalg.inv(B);tr=xx[tri];v6=np.einsum('ij,ij->i',tr[:,0],np.cross(tr[:,1],tr[:,2]));V=v6.sum()/6;g=(v6[:,None]*tr.sum(1)).sum(0)/(24*V);h=1-qq@g;H=qq/h[:,None];vp=escape(xx-g,ep);vq=escape(H,eq);values=np.r_[vp[keep1],vq[keep2],-vp[U],-vq[S]];return values,den,V,g,A,u,h
 goal=1e-7;floor=np.r_[np.full(len(X)+len(Q)-2,goal),1e-7,1e-7]
 def residual(p):
  v,de,V,g,A,u,h=evaluate(p);return np.r_[np.maximum(floor-v,0),np.maximum(.05-de,0)*10,np.maximum(.05-h,0)*10,max(.01-V,0)*10]
 rng=np.random.default_rng(a.seed);records=[];best=(float('inf'),None)
 for k in range(a.starts):
  p=np.zeros(8) if k==0 else rng.normal(size=8)*[.003,.01,.03,.1][(k-1)%4];ans=least_squares(residual,p,bounds=([-1,-1,-1,-1,-1,-.4,-.4,-.4],[1,1,1,1,1,.4,.4,.4]),max_nfev=a.steps,ftol=1e-13,xtol=1e-13,gtol=1e-13,diff_step=1e-5);v,de,V,g,A,u,h=evaluate(ans.x);score=float(residual(ans.x)@residual(ans.x));row=dict(start=k,score=score,minimum=float(v.min()),counts_SU=[int(sum(v[len(keep1):len(keep1)+len(keep2)]<0)+(v[-1]>0)),int(sum(v[:len(keep1)]<0)+(v[-2]>0))],nfev=ans.nfev,parameters=[float(x).hex() for x in ans.x]);records.append(row);print('GLOBAL8',json.dumps(row),flush=True)
  if score<best[0]:
   best=(score,ans.x.copy());data=dict(scale=10**12,A=np.rint(A*10**12).astype(np.int64).tolist(),u=np.rint(u*10**12).astype(np.int64).tolist(),parameters=row['parameters'],input_raw_sha256=hashlib.sha256(BLOB(raw)).hexdigest(),formula='B=(1+u_z)*A; Qnew=B^-T*(Q+u)');(a.out/'GLOBAL.json').write_bytes(BLOB(data));(a.out/'SOURCE_RAW.json').write_bytes(BLOB(raw))
  (a.out/'RECORDS.json').write_bytes(BLOB(records))
  if v.min()>goal*.9 and de.min()>.05 and h.min()>.05:break
 (a.out/'INPUT.json').write_bytes(BLOB(dict(seed=a.seed,starts=a.starts,steps=a.steps,goal=goal,numpy=np.__version__)));print('GLOBAL8_END_NUMERICAL_ONLY',best[0],flush=True)
if __name__=='__main__':main()

END FILE methods/GLOBAL8.py

FILE methods/G_FREE_CODEC.py 2430 a47787a38329aebedfa3608ae877b36416953099c78e192282b4522a40195f78
"""Lossless compact encoding of rational contact generators.
Only free controls define the body. Small stored corrections to rounded dependent
coordinates recover the ORIGINAL complete generator bytes as well, not an alias.
"""
import json,sys,copy,hashlib
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def solve(A,b):
 M=[list(a)+[v] for a,v in zip(A,b)];n=len(A)
 for k in range(n):
  p=next(j for j in range(k,n) if M[j][k]);M[k],M[p]=M[p],M[k];d=M[k][k];M[k]=[v/d for v in M[k]]
  for j in range(n):
   if j!=k:
    d=M[j][k];M[j]=[v-d*w for v,w in zip(M[j],M[k])]
 return [r[-1] for r in M]
def free_indices(G):
 n=G['n_supports'];ax={i:a for i,d,a in G['plan']};return [(i,k) for i in range(n+len(G['groups'])) if i!=n for k in range(3) if k not in ax[i]]
def rounded(G):
 D=G['grid'];n=G['n_supports'];Y=[[F(x,D) for x in r] for r in G['controls']];Y[n]=[F(0),F(0),F(1)];done={n}
 for i,deps,axes in G['plan']:
  assert i not in done and set(deps)<=done;rest=[k for k in range(3) if k not in axes]
  if deps:
   M=[[Y[j][k] for k in axes] for j in deps];rhs=[1-sum(Y[j][k]*Y[i][k] for k in rest) for j in deps]
   for k,v in zip(axes,solve(M,rhs)):Y[i][k]=v
  done.add(i)
 assert len(done)==len(Y)
 return [[round(v*D) for v in row] for row in Y]
def encode(G):
 orig=B(G);meta={k:v for k,v in G.items() if k!='controls'};free=free_indices(G);base=rounded(G);cor=[[i,k,x-base[i][k]] for i,row in enumerate(G['controls']) for k,x in enumerate(row) if x!=base[i][k]];return dict(meta=meta,free=[G['controls'][i][k] for i,k in free],dependent_corrections=cor,original_bytes=len(orig),original_sha256=hashlib.sha256(orig).hexdigest())
def decode(data):
 G=copy.deepcopy(data['meta']);n=G['n_supports'];G['controls']=[[0,0,0] for _ in range(n+len(G['groups']))];G['controls'][n]=[0,0,G['grid']];free=free_indices(G);assert len(free)==len(data['free'])
 for (i,k),v in zip(free,data['free']):G['controls'][i][k]=v
 G['controls']=rounded(G)
 for i,k,d in data['dependent_corrections']:G['controls'][i][k]+=d
 b=B(G);assert len(b)==data['original_bytes'] and hashlib.sha256(b).hexdigest()==data['original_sha256'];return G
if __name__=='__main__':
 from pathlib import Path
 data=json.loads(Path(sys.argv[1]).read_text());G=decode(data);Path(sys.argv[2]).write_bytes(B(G));print('EXACT_ORIGINAL_GENERATOR_RECOVERED',data['original_sha256'])

END FILE methods/G_FREE_CODEC.py

FILE methods/HOMOTOPY.py 5869 be45e371bab2e799f18d256ac1e013216517e59f2e86d9ba0dff66f9d909c91f
"""Own-volume-mass guarded physical panel-gap homotopy with full contact coordinates.
Proposal only: the exact finite merged generator is accepted solely by independent audits.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from flexible import *
from general_atlas import GeneralAtlas
from scipy.optimize import linprog
import argparse,time,hashlib,platform,scipy
from numeric import Chart
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def build(edges):
 c=Chart();G=json.load(open(ROOT/'parent/GENERATOR.json'));rep=json.load(open(ROOT/'baseline/A.json'));s=FlexibleAtlas(G,rep,c.Q);specs={a['edge']:a for a in json.load(open(ROOT/'HOMOTOPY_CANDIDATES.json'))};spec=[specs[e] for e in edges]
 s.blockedp=[]
 for r in spec:
  u,v=r['panels'];l,k=r['third'];s.blockedp.extend([(u,v),(v,u)]);s.mask[k,u]=False;s.mask[l,v]=False
  for t,tri in enumerate(s.tris):
   if u in tri and v in tri:s.floor[s.mechlen+s.nq+t]=0.
 s.last=None
 return s,c,spec

def gaps(s,z,spec):
 v,J,g=s.evaluate(z);vv=[];jj=[]
 for r in spec:
  u,_=r['panels'];k=r['third'][1];a=(1-g['Q'][k]@g['X'][u])/r['gap'];b=-(g['DQ'][k].T@g['X'][u]+g['Q'][k]@g['DX'][u])/r['gap'];vv.append(a);jj.append(b)
 return np.array(vv),np.array(jj)

def proposal(s,z,spec,trust,qbound,maxprogress):
 v,J,g=s.evaluate(z);f,Df=gaps(s,z,spec);n=s.n;JQ=g['DY'][:s.nq].reshape(-1,n)
 # s.evaluate DY already includes the parameter scale.
 floor=s.floor*1.04
 A=np.vstack((-J/s.rescale[:,None],JQ,-JQ));b=np.r_[(v-floor)/s.rescale,np.full(3*s.nq,qbound),np.full(3*s.nq,qbound)]
 # Variables: dz[n], nonnegative absolute values[n], common fractional progress.
 A=np.column_stack((A,np.zeros((len(A),n+1))));A=np.vstack((A,np.column_stack((np.eye(n),-np.eye(n),np.zeros(n))),np.column_stack((-np.eye(n),-np.eye(n),np.zeros(n)))))
 b=np.r_[b,np.zeros(2*n)];E=np.column_stack((Df,np.zeros((len(f),n)),f))
 ans=linprog(np.r_[np.zeros(n),np.full(n,1e-8),-1.],A_ub=A,b_ub=b,A_eq=E,b_eq=np.zeros(len(f)),bounds=[(-trust,trust)]*n+[(0,None)]*n+[(0,maxprogress)],method='highs-ds',options={'time_limit':10.,'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10})
 if not ans.success:return None,None,ans.message
 return ans.x[:n],float(ans.x[-1]),None

def merged_generator(s,Q,edges):
 G=copy.deepcopy(s.G);patches=[]
 for edge in edges:
  a=GeneralAtlas(edge,Q.copy());p=a.patch;old=p['new_node'];new=len(G['controls']);chosen=p['solved_support'];assert all(chosen not in deps for i,deps,axes in G['plan'])
  G['plan']=[row for row in G['plan'] if row[0]!=chosen]+[[new,[q for q in p['union'] if q!=chosen],[0,1,2]],[chosen,[new],[p['axis']]]];G['groups'].append(p['union']);G['controls'].append([0,0,0]);patches.append(dict(p,new_node=new))
 def point(ids):
  tri=max(itertools.combinations(ids,3),key=lambda p:abs(np.linalg.det(Q[list(p)])));return np.linalg.solve(Q[list(tri)],np.ones(3))
 shift=np.array([0.,0.,1.])-point(G['groups'][0]);Q=Q/(1+Q@shift)[:,None];Y=np.vstack((Q,[point(ids) for ids in G['groups']]));G['grid']=10**9;G['controls']=np.rint(Y*G['grid']).astype(np.int64).tolist()
 return G,patches

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--edges',type=int,nargs='+',required=True);ap.add_argument('--steps',type=int,default=500);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--trust',type=float,default=.003);ap.add_argument('--qbound',type=float,default=.001);ap.add_argument('--resume',type=Path);a=ap.parse_args();out=a.out;out.mkdir(parents=True,exist_ok=False);s,c,spec=build(a.edges);z=np.zeros(s.n) if a.resume is None else np.array([float.fromhex(t) for t in json.load(open(a.resume))]);records=[];trust=a.trust;qbound=a.qbound;t=time.time()
 (out/'INPUT.json').write_bytes(B(dict(edges=a.edges,steps=a.steps,trust=a.trust,qbound=a.qbound,versions=[platform.python_version(),np.__version__,scipy.__version__],spec=spec,resume=None if a.resume is None else [float(x).hex() for x in z])))
 for it in range(a.steps):
  v,J,g=s.evaluate(z);f,Df=gaps(s,z,spec);row=dict(it=it,gaps=f.tolist(),mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),minimum_floor_buffer=float((v-s.floor).min()),trust=trust,qbound=qbound);records.append(row);print('HOMOTOPY',json.dumps(row),flush=True)
  (out/'LIVE_Z.json').write_bytes(B([float(x).hex() for x in z]));(out/'RECORDS.json').write_bytes(B(records))
  if max(abs(f))<1e-7:break
  dz,eta,error=proposal(s,z,spec,trust,qbound,.3 if min(f)<.05 else .15)
  if dz is None or eta<1e-9:
   row['failure']=error or 'No finite LP progress';trust=min(.1,trust*1.5);qbound=min(.03,qbound*1.5)
   if it>5 and all('failure' in r for r in records[-5:]):break
   continue
  row['eta']=eta;accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625,.001953125,.0009765625]:
   zz=z+alpha*dz;vv,JJ,gg=s.evaluate(zz);ff,_=gaps(s,zz,spec)
   if np.all(np.isfinite(vv)) and np.all(vv>=s.floor-1e-13) and np.min(1-gg['Q']@gg['X'].T)>-1e-12 and np.min(ff)>-1e-10 and ff.sum()<f.sum()-1e-10:accepted=True;z=zz;break
  row['alpha']=alpha;row['accepted']=accepted
  if not accepted:trust*=.5;qbound*=.5
  elif alpha>=.5:trust=min(.05,trust*1.15);qbound=min(.015,qbound*1.15)
  elif alpha<.125:trust=max(1e-6,trust*.8);qbound=max(1e-7,qbound*.8)
  if trust<1e-9:break
 v,J,g=s.evaluate(z);f,Df=gaps(s,z,spec);G,patch=merged_generator(s,g['Q'],a.edges);(out/'GENERATOR.json').write_bytes(B(G));(out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(out/'PATCHES.json').write_bytes(B(patch));(out/'RECORDS.json').write_bytes(B(records));status=dict(gaps=f.tolist(),mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),time=time.time()-t,gen_sha=hashlib.sha256(B(G)).hexdigest());(out/'STATUS.json').write_bytes(B(status));print('HOMOTOPY_END_NUMERICAL_ONLY',json.dumps(status),flush=True)
if __name__=='__main__':main()

END FILE methods/HOMOTOPY.py

FILE methods/HOMOTOPY_SCREEN.py 1406 f7d509dc50cc3cbe1f9c93f7740cb54b999e3ad070851bd763dc4cd7aeb2a728
import os,sys
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1';sys.set_int_max_str_digits(0)
import numpy as np,json
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).parent;r=json.load(open(root/'baseline/A.json'));X=np.array([[float(F(t)) for t in row] for row in r['raw_vertices']]);g=np.array([float(F(t)) for t in r['raw_centroid']]);Z=X-g;e=Z[None]-Z[:,None];den=np.sqrt((Z*Z).sum(1)[:,None]*(e*e).sum(2));vals=np.einsum('ik,ijk->ij',Z,e)/np.maximum(den,1e-50);np.fill_diagonal(vals,-np.inf)
raw=json.load(open(root/'baseline/raw.json'))['H'];Q=np.array([[float(F(t,row[-1])) for t in row[:3]] for row in raw]);owners=[[f for f,cy in enumerate(r['faces']) if v in cy] for v in range(r['V'])];out=[]
for c in json.load(open(root/'ELIGIBLE.json')):
 u,v=c['panels'];aa=vals[u].copy();bb=vals[v].copy();aa[v]=-np.inf;bb[u]=-np.inf;k=next(i for i in owners[v] if i not in owners[u]);l=next(i for i in owners[u] if i not in owners[v]);gap=1-Q[k]@X[u];out.append(dict(**c,blockedmin=float(min(aa.max(),bb.max())),external=[int(aa.argmax()),int(bb.argmax())],length=float(np.linalg.norm(X[u]-X[v])),gap=float(gap),third=[l,k]))
(root/'HOMOTOPY_CANDIDATES.json').write_text(json.dumps(out));print('both_external',sum(c['blockedmin']>0 for c in out),'of',len(out))
for c in sorted([c for c in out if c['blockedmin']>0],key=lambda c:c['length']):print(c)

END FILE methods/HOMOTOPY_SCREEN.py

FILE methods/LOCAL_SCREEN.py 1319 2a7affa942bc6a431c66390e45629b7c16e170a6e54e7e05338855b0c42c673c
from LOCAL_UNION import *
ap=argparse.ArgumentParser();ap.add_argument('--chart',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();c=Chart(a.chart);rep=json.load(open(a.chart/'baseline/A.json'));rows=[]
for k,pair in enumerate(c.edges.tolist()):
 if c.w[k]<=0 or min(len(rep['faces'][q]) for q in pair)<=3:continue
 for lam in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
  try:
   s,nr,patch,Y=make_local(c,rep,pair,lam);v,J,g=s.evaluate(np.zeros(s.n));dm=float(v[:s.mechlen-2].min());s.forcedp,mp,ch=inherited(rep,s.owners);s.last=None;vv,jj,gg=s.evaluate(np.zeros(s.n));rows.append(dict(pair=pair,lam=str(lam),dynamic_mech=dm,inherited_primal=float(vv[:s.mechlen-2].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),union=patch['child_group']))
  except (AssertionError,ValueError,np.linalg.LinAlgError,ZeroDivisionError) as e:rows.append(dict(pair=pair,lam=str(lam),error=str(e)))
 a.out.write_bytes(B(rows));good=[t for t in rows[-5:] if t.get('slack',-1)>1e-9 and t.get('det',-1)>0];print('LOCAL_SCREEN',k,sorted(good,key=lambda t:t['dynamic_mech'],reverse=True)[:1],flush=True)
good=[r for r in rows if r.get('slack',-1)>1e-9 and r.get('det',-1)>0];print('FINAL_LOCAL_RANK',json.dumps(sorted(good,key=lambda r:r['dynamic_mech'],reverse=True)[:25],indent=2),flush=True)

END FILE methods/LOCAL_SCREEN.py

FILE methods/LOCAL_SCREEN_FAST.py 2190 6379cb21a97368223233ad34edd819d6fbb999cacf70fb103d3b91a9f276b473
"""Complete finite initial local-contraction screen without unused Jacobian work."""
from LOCAL_UNION import *
from contact import contact

def values(s,Y):
 coords=np.array([Y[i,a] for i,a in s.free]);YY,_=contact(s.G,coords,s.free,False);Q=YY[:s.nq];X=np.empty((s.nv,3));ix=s.direct>=0;X[ix]=YY[s.direct[ix]];X[s.simple]=np.linalg.solve(Q[s.trip],np.ones((len(s.simple),3,1)))[:,:,0];tr=X[s.tris];v6=np.einsum('ic,ic->i',tr[:,0],np.cross(tr[:,1],tr[:,2]));V=v6.sum()/6;g=(v6[:,None]*tr.sum(1)).sum(0)/(24*V);sl=np.where(s.mask,1-Q@X.T,np.inf);az=arrows(X-g);h=1-Q@g;aq=arrows(Q/h[:,None]);ep=az.max(1);eq=aq.max(1);dynamic=min(ep[s.keptp].min(),eq[s.keptq].min());fp=min(az[i,j] for i,j in s.forcedp.items());return dict(dynamic_mech=float(dynamic),inherited_primal=float(min(fp,eq[s.keptq].min())),slack=float(sl.min()),det=float(v6.min()),minimum_centred_offset=float(h.min()))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--chart',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();c=Chart(a.chart);rep=json.load(open(a.chart/'baseline/A.json'));rows=[];oldX=c.X
 for k,pair in enumerate(c.edges.tolist()):
  if c.w[k]<=0 or min(len(rep['faces'][q]) for q in pair)<=3:continue
  try:
   s,nr,patch,Y0=make_local(c,rep,pair,F(1,2));s.forcedp,mp,ch=inherited(rep,s.owners);node=s.G['n_supports']+s.G['groups'].index(patch['child_group']);u,v=patch['parent_vertex_indices']
   for lam in [F(t,10) for t in range(11)]:
    Y=Y0.copy();Y[node]=(1-float(lam))*oldX[u]+float(lam)*oldX[v];row=values(s,Y);row.update(pair=pair,lam=str(lam),union=patch['child_group']);rows.append(row)
  except (AssertionError,ValueError,np.linalg.LinAlgError,ZeroDivisionError) as e:rows.append(dict(pair=pair,error=str(e)))
  a.out.write_bytes(B(rows));good=[t for t in rows[-11:] if t.get('slack',-1)>1e-9 and t.get('det',-1)>0];print('FAST_LOCAL_SCREEN',k,sorted(good,key=lambda t:t['dynamic_mech'],reverse=True)[:1],flush=True)
 good=[t for t in rows if t.get('slack',-1)>1e-9 and t.get('det',-1)>0];print('FAST_FINAL_RANK',json.dumps(sorted(good,key=lambda t:t['dynamic_mech'],reverse=True)[:30],indent=2),flush=True)
if __name__=='__main__':main()

END FILE methods/LOCAL_SCREEN_FAST.py

FILE methods/LOCAL_UNION.py 2934 c8ac45d00964030176f91f70f05c19928ac10cf077f225119dba9c4b299d3972
"""Local physical-edge contraction seed in the full recharted contact atlas.
Unlike a frozen support-triple projection, the new contact point is initialized
at a prescribed affine combination of the two actual physical endpoints. All
incident support equations are then solved in the acyclic full-contact plan.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from ANY_UNION import *

def make_local(c,rep,pair,lam):
 nr,owners,patch=quotient(rep,pair);root=next(v for v,row in enumerate(rep['raw_vertices']) if list(map(F,row))==[0,0,1]);anchorowners=[i for i,cy in enumerate(rep['faces']) if root in cy];assert set(anchorowners)!=set(patch['child_group']);G,Q=atlas_generator(owners,c.Q.copy(),anchorowners);s=FlexibleAtlas(G,nr,Q);X=np.array([[float(F(x)) for x in row] for row in rep['raw_vertices']]);oldowners=[[i for i,cy in enumerate(rep['faces']) if v in cy] for v in range(rep['V'])];u,v=patch['parent_vertex_indices'];union=patch['child_group'];points=[]
 for gr in G['groups']:
  if gr==union:points.append((1-float(lam))*X[u]+float(lam)*X[v])
  else:points.append(X[oldowners.index(gr)])
 Y=np.vstack((c.Q,points));G['controls']=np.rint(Y*G['grid']).astype(np.int64).tolist();s.G=G;s.base=np.array([Y[i,a] for i,a in s.free]);s.scale=np.ones(s.n);s.last=None;s.tscale=np.ones(len(s.tris));vv,JJ,gg=s.evaluate(np.zeros(s.n));s.scale=1/np.maximum(1.,np.linalg.norm(gg['DQ'].reshape(-1,s.n),axis=0));s.tscale=np.maximum(abs(gg['v6']),1e-10);s.last=None;patch['lam']=str(lam);return s,nr,patch,Y

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--chart',type=Path,required=True);ap.add_argument('--pair',nargs=2,type=int,required=True);ap.add_argument('--lam',default='1/2');ap.add_argument('--steps',type=int,default=100);ap.add_argument('--goal',type=float,default=1e-7);ap.add_argument('--dynamic',action='store_true');ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);c=Chart(a.chart);rep=json.load(open(a.chart/'baseline/A.json'));s,nr,patch,Y=make_local(c,rep,sorted(a.pair),F(a.lam))
 if not a.dynamic:
  s.forcedp,mp,ch=inherited(rep,s.owners);g=np.array([float(F(x)) for x in rep['raw_centroid']]);aq=arrows(c.Q/(1-c.Q@g)[:,None]);sp=aq.argmax(1);s.forcedq={i:int(sp[i]) for i in range(s.nq) if i!=s.S};(a.out/'WITNESSES.json').write_bytes(B(dict(primal=s.forcedp,polar=s.forcedq,mapping=mp)))
 s.last=None;(a.out/'INITIAL_GENERATOR.json').write_bytes(B(s.G));(a.out/'NOMINAL_COMPLEX.json').write_bytes(B(nr));(a.out/'PATCH.json').write_bytes(B(patch));(a.out/'INITIAL_Y_HEX.json').write_bytes(B([[float(x).hex() for x in row] for row in Y]));(a.out/'INPUT.json').write_bytes(B(dict(pair=a.pair,lam=a.lam,steps=a.steps,goal=a.goal,dynamic=a.dynamic,versions=[platform.python_version(),np.__version__,scipy.__version__])));repair(s,np.zeros(s.n),a.out,steps=a.steps,goal=a.goal)
if __name__=='__main__':main()

END FILE methods/LOCAL_UNION.py

FILE methods/MERGE_CONTACT.py 4402 8b0daadac7f9cb67df4e6f4f748708cd203e22c68d16bf8b5799d4350f2b39b0
"""Nonsimple physical-vertex union by exact identification of two free contact nodes.
Duplicated support equations are removed, and their freed coordinates are restored
from the actual parent mixed realization. No triangulation diagonal is counted.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from flexible import *
from TURNOVER import exact_mixed
from CROSS_CAP import inherited
from TREE_REPAIR import arrows
from SVD_CORRECT import repair
import argparse,hashlib,platform,scipy
sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def merge(G,rep,a,b,lam=F(1,2)):
 G=copy.deepcopy(G);n=G['n_supports'];assert a>=n and b>=n and a!=b;Y=exact_mixed(G);plan={i:(d,ax) for i,d,ax in G['plan']};assert plan[a]==plan[b]==([],[])
 ga,gb=G['groups'][a-n],G['groups'][b-n];assert len(set(ga)&set(gb))==2;owners=[[f for f,cy in enumerate(rep['faces']) if v in cy] for v in range(rep['V'])];va=owners.index(ga);vb=owners.index(gb);assert sorted([va,vb]) in [sorted(e) for e in rep['edges']]
 union=sorted(set(ga+gb));Y[a]=[(1-lam)*u+lam*v for u,v in zip(Y[a],Y[b])];mapping={i:i-(i>b) for i in range(len(Y)) if i!=b};alias=lambda i:mapping[a if i==b else i];newplan=[];changed=[]
 for i,deps,axes in G['plan']:
  if i==b:continue
  dd=list(dict.fromkeys(a if j==b else j for j in deps));aa=axes
  if len(dd)!=len(deps):
   choices=list(itertools.combinations(range(3),len(dd)));aa=list(max(choices,key=lambda ax:abs(np.linalg.det(np.array([[float(Y[j][k]) for k in ax] for j in dd])))));changed.append([i,deps,axes,dd,aa])
  newplan.append([alias(i),[alias(j) for j in dd],aa])
 G['groups'][a-n]=union;G['groups'].pop(b-n);G['plan']=newplan;G['grid']=10**12;G['controls']=[[round(x*G['grid']) for x in row] for i,row in enumerate(Y) if i!=b]
 keep=min(va,vb);gone=max(va,vb);old=[i for i in range(rep['V']) if i!=gone];vmap={i:k for k,i in enumerate(old)};vmap[gone]=vmap[keep];fs=[]
 for cy in rep['faces']:
  out=[]
  for v in cy:
   k=vmap[v]
   if not out or k!=out[-1]:out.append(k)
  if out[0]==out[-1]:out.pop()
  assert len(set(out))==len(out) and len(out)>=3;fs.append(out)
 nr=copy.deepcopy(rep);nr['V']-=1;nr['E']-=1;nr['faces']=fs;nr['raw_vertices']=[rep['raw_vertices'][i] for i in old];nr['edges']=sorted({tuple(sorted((u,v))) for cy in fs for u,v in zip(cy,cy[1:]+cy[:1])});assert nr['V']-len(nr['edges'])+len(fs)==2
 changes=dict(parent_contact_nodes=[a,b],parent_groups=[ga,gb],child_group=union,lam=str(lam),parent_vertex_ids=[va,vb],physical_old_to_new=vmap,contact_old_to_new={i:alias(i) for i in range(len(Y))},changed_plan_before_reindex=changed)
 return G,nr,changes

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,default=ROOT/'parent/GENERATOR.json');ap.add_argument('--report',type=Path,default=ROOT/'baseline/A.json');ap.add_argument('--nodes',type=int,nargs=2,required=True);ap.add_argument('--lam',default='1/2');ap.add_argument('--goal',type=float,default=1e-7);ap.add_argument('--steps',type=int,default=120);ap.add_argument('--dynamic',action='store_true');ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);G=json.load(open(a.generator));rep=json.load(open(a.report));GG,nr,changes=merge(G,rep,*a.nodes,F(a.lam));raw=RECONSTRUCT.recover(GG);Q=np.array([[float(F(x,row[-1])) for x in row[:3]] for row in raw['H']]);s=FlexibleAtlas(GG,nr,Q)
 if not a.dynamic:
  s.forcedp,mp,ch=inherited(rep,s.owners);oldraw=RECONSTRUCT.recover(G);q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in oldraw['H']]);c=np.array([float(F(x)) for x in rep['raw_centroid']]);sp=np.argmax(arrows(q/(1-q@c)[:,None]),axis=1);s.forcedq={i:int(sp[i]) for i in range(s.nq) if i!=3};(a.out/'WITNESSES.json').write_bytes(B(dict(primal=s.forcedp,polar=s.forcedq)))
 (a.out/'SOURCE_GENERATOR.json').write_bytes(B(G));(a.out/'NOMINAL_COMPLEX.json').write_bytes(B(nr));(a.out/'INITIAL_GENERATOR.json').write_bytes(B(GG));(a.out/'CHANGES.json').write_bytes(B(changes));(a.out/'INPUT.json').write_bytes(B(dict(nodes=a.nodes,lam=a.lam,goal=a.goal,steps=a.steps,dynamic=a.dynamic,versions=[platform.python_version(),np.__version__,scipy.__version__])));s.last=None;print('MERGE_CONTACT_START',changes,s.n,flush=True);repair(s,np.zeros(s.n),a.out,steps=a.steps,goal=a.goal)
if __name__=='__main__':main()

END FILE methods/MERGE_CONTACT.py

FILE methods/NONSIMPLE_SCREEN.py 1722 c1cfbb5683891be46bf1a333d65324df27ccd4ae85e2ccea6ab610620059be34
"""Finite full-atlas adjacency and convex seed screen for genuine nonsimple unions."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from MERGE_CONTACT import *
import argparse

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--generator',type=Path,required=True);ap.add_argument('--report',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();G=json.load(open(a.generator));rep=json.load(open(a.report));n=G['n_supports'];free=[i for i,deps,axes in G['plan'] if i>n and not deps];rows=[]
 for i,j in itertools.combinations(free,2):
  if len(set(G['groups'][i-n])&set(G['groups'][j-n]))!=2:continue
  for lam in map(lambda k:F(k,10),range(11)):
   try:
    GG,nr,changes=merge(G,rep,i,j,lam);raw=RECONSTRUCT.recover(GG);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=FlexibleAtlas(GG,nr,Q);v,J,g=s.evaluate(np.zeros(s.n));ownmin=float(v[:s.mechlen-2].min());s.forcedp,mp,ch=inherited(rep,s.owners);s.last=None;v,J,g=s.evaluate(np.zeros(s.n));row=dict(nodes=[i,j],lam=str(lam),dynamic_mech=ownmin,inherited_primal=float(v[:s.mechlen-2].min()),slack=float(g['slack'].min()),det=float(g['v6'].min()),groups=changes['parent_groups']);rows.append(row)
   except (AssertionError,ValueError,np.linalg.LinAlgError,ZeroDivisionError) as e:rows.append(dict(nodes=[i,j],lam=str(lam),error=str(e)))
  a.out.write_bytes(B(rows));print('NON_SIMPLE_SCREEN',i,j,len(rows),flush=True)
 good=[r for r in rows if r.get('slack',-1)>0 and r.get('det',-1)>0];print('CONVEX_INITIAL_SEEDS',len(good));print(json.dumps(sorted(good,key=lambda r:r['inherited_primal'],reverse=True)[:30],indent=2),flush=True)
if __name__=='__main__':main()

END FILE methods/NONSIMPLE_SCREEN.py

FILE methods/PREPARE_CHART.py 961 83819e027058732d32825f62008f1fa1f851891d713c2d8801a2c7f357f74ab4
"""Reconstruct both exact audits and the faithful maximal-complex stress chart."""
import argparse,json,sys,hashlib
from pathlib import Path
import chart
from check_A import encode
sys.path.insert(0,str(Path(__file__).parent/'parent'));import RECONSTRUCT,check_A,check_B
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
ap=argparse.ArgumentParser();ap.add_argument('generator',type=Path);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);base=a.out/'baseline';base.mkdir();raw=RECONSTRUCT.recover(json.loads(a.generator.read_text()));A=check_A.run(raw);BB=check_B.run(raw);assert B(A)==B(BB)
for n,x in [('raw',raw),('A',A),('B',BB)]: (base/(n+'.json')).write_bytes(B(x))
d=chart.recover(root=a.out);b=B(encode(d));(a.out/'chart_exact.json').write_bytes(b);print('EXACT_MAXIMAL_STRESS_CHART',len(b),hashlib.sha256(b).hexdigest(),len(d['edges']),d['outer'],d['boundary'],flush=True)

END FILE methods/PREPARE_CHART.py

FILE methods/RANK_DELETIONS.py 1332 6e6139d598c9242462bcb5b9947eb4eca0a7912d19ff9446b6d5f0824b730be9
"""Ranking only; actual exact acceptance is not inferred from hull tolerances."""
from numeric import *
import sys,hashlib
ROOT=Path(__file__).resolve().parent;sys.path.insert(0,str(ROOT/'parent'));import RECONSTRUCT
from TREE_REPAIR import arrows
D=Path(sys.argv[1]);G=json.loads((D/'SOURCE_GENERATOR.json').read_text());raw=RECONSTRUCT.recover(G);Q=np.array([[float(Fraction(x,row[-1])) for x in row[:3]] for row in raw['H']]);out=[]
for row in json.loads((D/'RESULTS.json').read_text()):
 if row.get('counts') not in ([1,2,1],[2,1,1]):continue
 f=row['deleted_input'];q=np.delete(Q,f,0);hu=ConvexHull(q);XX=-hu.equations[:,:3]/hu.equations[:,3,None];X=[]
 for p in XX:
  if not any(np.linalg.norm(p-x)<1e-9 for x in X):X.append(p)
 X=np.array(X);g=np.array(row['centroid']);ep=arrows(X-g).max(1);eq=arrows(q/(1-q@g)[:,None]).max(1);root=np.argmin(np.linalg.norm(X-[0,0,1],axis=1));ep[root]=np.inf;eq[3-(f<3)]=np.inf;out.append(dict(deleted=f,counts=row['counts'],E=row['E'],primal=float(ep.min()),polar=float(eq.min()),sum_deficit=float(np.sum(np.minimum(ep,0)**2)+np.sum(np.minimum(eq,0)**2)),bad_owners=[np.where(abs(q@X[i]-1)<1e-9)[0].tolist() for i in np.where(ep<0)[0]]))
out.sort(key=lambda d:d['sum_deficit']);(D/'RANK.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':')));print(json.dumps(out,indent=2))

END FILE methods/RANK_DELETIONS.py

FILE methods/REFERENCE_SCREEN.py 1280 368f0c700797baa7e7acb9ca7c0be75d0c30c8c91f960d6b6e51df301328897f
"""Reference-centre diagnostic only; no reference110 is called an own-centred result."""
from general_atlas import *
from numeric import Chart
from TREE_REPAIR import arrows
from fractions import Fraction as F
c=Chart();rep=json.load(open(ROOT/'baseline/A.json'));oldg=np.array([float(F(x)) for x in rep['raw_centroid']]);results=[]
for row in json.load(open(ROOT/'ELIGIBLE.json')):
 for mode in ['direct','stress']:
  try:
   if mode=='stress':w=c.w.copy();w[row['edge']]=0;Q=c.solve(w)[0]
   else:Q=c.Q.copy()
   s=GeneralAtlas(row['edge'],Q);v,J,g=s.evaluate(np.zeros(s.n));P=g['X']-oldg;H=g['Q']/(1-g['Q']@oldg)[:,None];ep=arrows(P).max(1);eq=arrows(H).max(1);m=min(np.delete(ep,s.U).min(),np.delete(eq,3).min());results.append(dict(edge=row['edge'],pair=row['pair'] if 'pair' in row else c.edges[row['edge']].tolist(),mode=mode,ref_mech=float(m),own_mech=float(v[:s.mechlen-2].min()),centroid_shift=float(np.linalg.norm(g['g']-oldg)),slack=float(g['slack'].min())))
  except Exception as ex:results.append(dict(edge=row['edge'],mode=mode,error=str(ex)))
Path('../REFERENCE_SCREEN.json').write_text(json.dumps(results,sort_keys=True,separators=(',',':')));print(json.dumps(sorted([r for r in results if 'ref_mech' in r],key=lambda r:-r['ref_mech'])[:20],indent=2),flush=True)

END FILE methods/REFERENCE_SCREEN.py

FILE methods/REFINE.py 3220 b94b0682da1c60a234f2a2b8886d5216e9bb07f3dee2701df5d2a100c1e7f5fb
"""Full-contact-chart semismooth correction; numerical discovery, not an exact certificate."""
from general_atlas import *
from scipy.optimize import linprog
import qp

def lp_l1(A,lo,hi,lb,ub,cost):
 n=len(lb);eq=np.isfinite(hi)&(lo==hi);il=np.isfinite(lo)&~eq;ih=np.isfinite(hi)&~eq
 AA=np.vstack((-A[il],A[ih]));bb=np.r_[-lo[il],hi[ih]]
 AA=np.column_stack((AA,np.zeros_like(AA)))
 AA=np.vstack((AA,np.column_stack((np.eye(n),-np.eye(n))),np.column_stack((-np.eye(n),-np.eye(n)))))
 bb=np.r_[bb,np.zeros(2*n)];Ae=np.column_stack((A[eq],np.zeros_like(A[eq])))
 ans=linprog(np.r_[np.zeros(n),cost],A_ub=AA,b_ub=bb,A_eq=Ae,b_eq=lo[eq],bounds=list(zip(lb,ub))+[(0,None)]*n,method='highs-ipm',options={'time_limit':10,'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10,'ipm_optimality_tolerance':1e-10})
 return (ans.x[:n],None) if ans.success else (None,ans.message)

def warm(s,steps=2000):
 best=[np.inf,None];calls=[0]
 def fun(z):
  r=s.residual(z);obj=float(r@r)
  calls[0]+=1
  if obj<best[0]:best[:]=[obj,z.copy()]
  if calls[0]%100==0:
   print('WARM',calls[0],best[0],flush=True)
   dest=getattr(s,'checkpoint_dir',None)
   if dest is not None:(Path(dest)/'WARM_LIVE_Z.json').write_text(json.dumps([float(x).hex() for x in best[1]]))
  return r
 least_squares(fun,np.zeros(s.n),jac=s.derivative,max_nfev=steps,ftol=1e-13,xtol=1e-13,gtol=1e-13,x_scale='jac',verbose=0)
 return best[1]

def correct(s,z,steps=100):
 z=np.array(z).copy();trust=.03;qbound=.004;records=[]
 for it in range(steps):
  v,J,g=s.evaluate(z);merit=float(np.linalg.norm(s.residual(z)))
  row=dict(iteration=it,merit=merit,minimum_mechanical=float(v[:s.mechlen].min()),minimum_nonowner_slack=float(g['slack'].min()),trust=trust)
  records.append(row);print('CORRECT',json.dumps(row),flush=True)
  from pathlib import Path
  dest=getattr(s,'checkpoint_dir',None)
  if dest is not None:
   dest=Path(dest);dest.mkdir(parents=True,exist_ok=True);(dest/'LIVE_Z.json').write_text(json.dumps([float(x).hex() for x in z]));(dest/'LIVE_RECORDS.json').write_text(json.dumps(records))
  if it>4 and trust>=.5 and all(abs(r['merit']-merit)<1e-14 for r in records[-5:]):
   records[-1]['failure']='Repeated finite hard-QP failure at maximum trust';break
  if v[:s.mechlen].min()>1.5e-7 and g['slack'].min()>1e-8 and g['v6'].min()>0:return z,records
  Y,DY=contact(s.G,s.base+s.scale*z,s.free);JQ=(DY[:s.nq]*s.scale[None,None,:]).reshape(-1,s.n)
  A=np.vstack((J/s.rescale[:,None],JQ));lo=np.r_[(s.floor-v)/s.rescale,np.full(3*s.nq,-qbound)];hi=np.r_[np.full(len(v),np.inf),np.full(3*s.nq,qbound)];lb=np.full(s.n,-trust);ub=np.full(s.n,trust)
  dz,status=qp.solve(A,lo,hi,lb,ub,np.ones(s.n))
  if dz is None:
   dz,status=lp_l1(A,lo,hi,lb,ub,np.ones(s.n))
   if dz is None:
    records[-1]['failure']=status;trust=min(.5,trust*1.5);qbound=min(.05,qbound*1.5);continue
  accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125]:
   zz=z+alpha*dz;new=float(np.linalg.norm(s.residual(zz)))
   if np.isfinite(new) and (new<merit*(1-1e-5) or new<1e-8):z=zz;accepted=True;break
  records[-1]['alpha']=alpha;records[-1]['accepted']=accepted
  if not accepted:trust*=.5;qbound*=.5
  if trust<1e-7:break
 return z,records

END FILE methods/REFINE.py

FILE methods/RELIFT.py 1424 c26272bf84467d425c2e4732943a3ca560ace9b4430ac908fccd88b5a355117c
"""Faithful inverse-pole avoiding height rescale; an actual physical projectivity.
A single positive Maxwell stress scaling is gauge in a normalized chart but NOT
here: unnormalized height changes the inverse projective body, whose mass must
be recomputed. Used only for numerical seed creation, never as a mass assignment.
"""
import numpy as np

def seed(chart,weights):
 try:return chart.solve(weights)[0],dict(height_scale=1.)
 except ValueError as e:
  if str(e)!='inverse pole':raise
 # Recover r,h through the same Dirichlet and dual-tree equations without inverse.
 import scipy.linalg as la
 wi=weights[chart.ie];L=(chart.Bi*wi)@chart.Bi.T;rhs=-((chart.Bi*wi)@chart.Bb.T)@chart.rb;r=np.empty((chart.n,2));r[chart.boundary]=chart.rb;r[chart.inner]=la.solve(L,rhs,assume_a='pos',check_finite=False);e=r[chart.edges[chart.ie,1]]-r[chart.edges[chart.ie,0]];J=e[:,::-1]*[-1,1];off=-np.einsum('ij,ij->i',J,r[chart.edges[chart.ie,0]]);planes=chart.T@(wi[:,None]*np.column_stack((J,off)));h=np.einsum('ij,ij->i',planes[chart.vf],np.column_stack((r,np.ones(chart.n))));h-=np.column_stack((r,np.ones(chart.n)))@(chart.Ainv@h[chart.boundary]);h[chart.boundary]=0;h*=chart.R[:,2].sum()/h.sum();alpha=min(1.,.9/(-h/chart.delta).max());h*=alpha;den=1+h/chart.delta;assert den.min()>0;Q=chart.c+(np.column_stack((r,h))@chart.basis)/den[:,None];return Q,dict(height_scale=float(alpha),minimum_inverse_denominator=float(den.min()))

END FILE methods/RELIFT.py

FILE methods/RETRACT.py 3797 fb2fb7749d434222a0f32e77ed7578497e1484d980b1792f252efd3251d1e3a1
"""Finite own-mass retraction at successively smaller actual panel gaps.
Only completed convex stage endpoints have an actual filled-mass interpretation.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from HOMOTOPY import *
from REFINE import lp_l1
import qp

def merit(s,z,spec,target):
 v,J,g=s.evaluate(z);f,Df=gaps(s,z,spec)
 return float(np.linalg.norm(np.r_[np.maximum(s.floor-v,0)/s.rescale,10*(f-target)]))

def retract(s,start,spec,target,steps=40):
 z=start.copy();trust=.03;qbound=.004;history=[]
 for it in range(steps):
  v,J,g=s.evaluate(z);f,Df=gaps(s,z,spec);m=merit(s,z,spec,target)
  row=dict(it=it,merit=m,mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),gap=f.tolist(),trust=trust);history.append(row)
  if np.max(abs(f-target))<1e-9 and np.min(v-s.floor)>-1e-12 and np.min(1-g['Q']@g['X'].T)>-1e-11:return z,True,history
  JQ=g['DY'][:s.nq].reshape(-1,s.n);floor=s.floor*1.10
  A=np.vstack((J/s.rescale[:,None],10*Df,JQ));lo=np.r_[(floor-v)/s.rescale,10*(target-f),np.full(3*s.nq,-qbound)];hi=np.r_[np.full(len(v),np.inf),10*(target-f),np.full(3*s.nq,qbound)]
  lb=np.full(s.n,-trust);ub=np.full(s.n,trust);dz,error=qp.solve(A,lo,hi,lb,ub,np.ones(s.n),tol=1e-10)
  if dz is None:dz,error=lp_l1(A,lo,hi,lb,ub,np.ones(s.n))
  if dz is None:
   row['failure']=error;trust=min(1.,trust*1.5);qbound=min(.08,qbound*1.5)
   if it>4 and all('failure' in r for r in history[-4:]):return z,False,history
   continue
  accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625]:
   zz=z+alpha*dz;mm=merit(s,zz,spec,target)
   if np.isfinite(mm) and (mm<m*(1-1e-5) or mm<1e-9):z=zz;accepted=True;break
  row['alpha']=alpha;row['accepted']=accepted
  if not accepted:trust*=.5;qbound*=.5
  if trust<1e-8:break
 return z,False,history

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--edges',type=int,nargs='+',required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--stages',type=int,default=100);ap.add_argument('--step',type=float,default=.02);ap.add_argument('--resume',type=Path);a=ap.parse_args();out=a.out;out.mkdir(parents=True,exist_ok=False);s,c,spec=build(a.edges);z=np.zeros(s.n) if a.resume is None else np.array([float.fromhex(x) for x in json.load(open(a.resume))]);step=a.step;records=[];t=time.time()
 (out/'INPUT.json').write_bytes(B(dict(edges=a.edges,stages=a.stages,step=a.step,resume=None if a.resume is None else [float(x).hex() for x in z],versions=[platform.python_version(),np.__version__,scipy.__version__])))
 for stage in range(a.stages):
  v,J,g=s.evaluate(z);f,Df=gaps(s,z,spec);print('RETRACT_STAGE',stage,'gaps',f,'mech',v[:s.mechlen].min(),'step',step,flush=True)
  (out/'LIVE_Z.json').write_bytes(B([float(x).hex() for x in z]))
  if np.max(abs(f))<1e-9:break
  target=np.maximum(0,f-step);zz,ok,history=retract(s,z,spec,target)
  row=dict(stage=stage,source_gap=f.tolist(),target=target.tolist(),success=ok,inner=history);records.append(row);(out/'RECORDS.json').write_bytes(B(records));print('RETRACTION',stage,ok,'inner',len(history),'last',history[-1],flush=True)
  if ok:z=zz;step=min(.2,step*(1.5 if len(history)<8 else 1.05))
  else:step*=.5
  if step<1e-6:break
 v,J,g=s.evaluate(z);f,Df=gaps(s,z,spec);G,patch=merged_generator(s,g['Q'],a.edges);(out/'GENERATOR.json').write_bytes(B(G));(out/'Z.json').write_bytes(B([float(x).hex() for x in z]));(out/'PATCHES.json').write_bytes(B(patch));(out/'RECORDS.json').write_bytes(B(records));status=dict(gaps=f.tolist(),mech=float(v[:s.mechlen].min()),slack=float(g['slack'].min()),time=time.time()-t,gen_sha=hashlib.sha256(B(G)).hexdigest());(out/'STATUS.json').write_bytes(B(status));print('RETRACTION_END_NUMERICAL_ONLY',json.dumps(status),flush=True)
if __name__=='__main__':main()

END FILE methods/RETRACT.py
