# material-5a6df59c028c

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J124 numerical method — Recovery capsule part 1/3

Complete materially used numerical core. Parts2/3 contain nomination code, exact floating checkpoints, earlier-version patches and the full finite-trial recipe. This is search code, not an absence certificate or independent equilibrium auditor. Exact endpoint inputs are separately preserved in [internal-source-reference] and [internal-source-reference], with exact auditor [internal-source-reference]. All numerical findings remain distinguished from those exact bodies.

Save each named code block with its terminal newline. Environment actually used: Python3.13.5, NumPy2.3.5, SciPy1.17.0, torch2.10.0+cpu; one Torch/BLAS/OpenMP thread. geometry121.py5112B/SHA b64da8c4140fba3954b28323d603be3813b0643ed6aca18b195a2b62f2c44bf1; coalesce.py2720B/SHA b49fc9c36b198c71c3c8620efb63dffe586b50188a05031311dff343629834b7; apexflow.py9768B/SHA7e7132cc217859c18f8fb2eb3318f968314819b2fae9d496164f8403dee011ec. Local historical import-path changes are explicitly represented by the part3 patch; no original sandbox is needed for these portable units.

## geometry121.py
```python
"""Actual uniform-mass H-hull geometry for J121 numerical experiments.
Search only: floating signs are never absence certificates. Python 3.13.5,
NumPy 2.3.5, SciPy 1.17.0, torch 2.10.0+cpu. Input n_i.x <= 1.
Complete current facets/true edges are grouped, not counted as triangulation.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json
from pathlib import Path
import numpy as np
import torch
from scipy.spatial import ConvexHull, QhullError
from scipy.spatial.distance import pdist
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def read_h(path):
    if str(path).endswith('.json'):return np.asarray(json.loads(Path(path).read_text())['n'],float)
    lines=Path(path).read_text().splitlines();m,D=map(int,lines[0].split());r=np.array([list(map(int,l.split())) for l in lines[1:] if l.strip()],float)
    assert len(r)==m
    return r/D if D else r[:,:3]/r[:,3,None]

def geometry(n):
    n=np.asarray(n,float);h=ConvexHull(n)
    if h.equations[:,3].max()>=-1e-10:raise ValueError('origin not strictly inside polar')
    raw=-h.equations[:,:3]/h.equations[:,3,None]
    # Generic input fast path; nonsimple vertices are merged and distinguished.
    simple=len(raw)<2 or pdist(raw).min()>1e-9
    verts=[];groups=[];mp=[]
    for i,v in enumerate(raw):
        hits=[] if simple else [j for j,w in enumerate(verts) if np.linalg.norm(v-w)<1e-9]
        if hits:j=hits[0];groups[j].append(i)
        else:j=len(verts);verts.append(v);groups.append([i])
        mp.append(j)
    v=np.array(verts);tri=np.array([h.simplices[z[0]] for z in groups],int)
    faces={};tet=[];owners={}
    for f in sorted(h.vertices):
        ids=sorted({mp[k] for k,t in enumerate(h.simplices) if f in t});a=n[f]
        axis=np.eye(3)[np.argmin(abs(a))];e=np.cross(a,axis);e/=np.linalg.norm(e);ff=np.cross(a,e)
        delta=v[ids]-v[ids].mean(0);cy=np.array(ids)[np.argsort(np.arctan2(delta@ff,delta@e))].tolist()
        faces[int(f)]=cy
        for x,y in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((x,y))),[]).append(int(f))
        for b,c in zip(cy[1:-1],cy[2:]):tet.append([cy[0],b,c])
    assert all(len(a)==2 for a in owners.values())
    assert len(v)-len(owners)+len(faces)==2
    assert np.max(v@n.T-1)<1e-7
    tet=np.asarray(tet,int);w=np.linalg.det(v[tet])/6
    if w.min()<=0:raise ValueError('nonpositive tetrahedron')
    V=w.sum();g=(w[:,None]*v[tet].sum(1)/4).sum(0)/V
    active=np.array(sorted(faces),int);remap={f:i for i,f in enumerate(active)}
    pe=np.array(sorted(owners),int);qe=np.array([[remap[f] for f in owners[tuple(e)]] for e in pe],int)
    q=n[active]/(1-n[active]@g)[:,None];p=v-g
    return dict(n=n,v=v,p=p,q=q,pe=pe,qe=qe,faces=faces,active=active,tet=tet,triples=tri,g=g,volume=V,simple=simple)

def tensors(n,G):
    if not G['simple']:raise ValueError('free-H derivative requires simple current fan')
    v=torch.linalg.solve(n[G['triples']],torch.ones((len(G['v']),3,1))).squeeze(-1)
    tet=v[G['tet']];w=torch.linalg.det(tet)/6;V=w.sum();g=(w[:,None]*tet.sum(1)/4).sum(0)/V
    p=v-g;nn=n[G['active']];q=nn/(1-nn@g)[:,None]
    return p,q,g,V

def arrows(x,angular=True):
    d=x[None,:,:]-x[:,None,:];sq=(x*x).sum(1);num=np.einsum('ik,ijk->ij',x,d)
    if angular:
        den=np.sqrt(sq[:,None]*(d*d).sum(2));den[np.diag_indices(len(x))]=1
        a=num/den
    else:a=num/sq[:,None]
    a[np.diag_indices(len(x))]=-np.inf
    return a.max(1),a.argmax(1),a

def bars(x,edges):
    sq=(x*x).sum(1);d=x[edges[:,1]]-x[edges[:,0]];dd=(d*d).sum(1)
    t=np.clip(-np.einsum('ij,ij->i',x[edges[:,0]],d)/dd,0,1)
    z=x[edges[:,0]]+t[:,None]*d;lev=(z*z).sum(1)
    # Rounding-level errors are clipped only in this numerical diagnostic.
    lev=np.minimum(lev,np.minimum(sq[edges[:,0]],sq[edges[:,1]]))
    par=np.arange(len(x));out=[]
    def root(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return int(i)
    for k in sorted(range(len(edges)),key=lambda k:(-lev[k],tuple(edges[k]))):
        a,b=map(root,edges[k])
        if a==b:continue
        if (sq[a],-a)<(sq[b],-b):a,b=b,a
        depth=1-lev[k]/sq[b]
        if depth>0:out.append(dict(depth=float(depth),root=b,edge=edges[k].tolist(),birth=float(sq[b]),death=float(lev[k])))
        par[b]=a
    return sorted(out,key=lambda b:-b['depth'])

def describe(n):
    G=geometry(n);pa,pw,_=arrows(G['p']);qa,qw,_=arrows(G['q']);pr=int(np.argmax((G['p']**2).sum(1)));qr=int(np.argmax((G['q']**2).sum(1)))
    pidx=np.arange(len(pa))!=pr;qidx=np.arange(len(qa))!=qr
    P=bars(G['p'],G['pe']);Q=bars(G['q'],G['qe'])
    return dict(VEF=[len(G['v']),len(G['pe']),len(G['active'])],S=G['active'][qa<-1e-10].tolist(),U=np.where(pa<-1e-10)[0].tolist(),P=[b for b in P if b['depth']>1e-12],Q=[b for b in Q if b['depth']>1e-12],all_positive_float_P=P,all_positive_float_Q=Q,minp=float(pa[pidx].min()),minq=float(qa[qidx].min()),rho=float(min(pa[pidx].min(),qa[qidx].min())),volume=float(G['volume']),g=G['g'].tolist(),numerical_only=True)

def normalize(n):
    G=geometry(n);return n/(1-n@G['g'])[:,None]*G['volume']**(1/3)
```

## coalesce.py
```python
"""Finite shared-apex coalescence scout, actual filled H-body at every trial.
Search output is numerical only. Exact replay must rationally enforce the apex
incidences rather than rounding final normal rows independently.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,time,argparse
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
import geometry121 as geom

def info(N):
 G=geom.geometry(N);pa,_,_=geom.arrows(G['p']);qa,_,_=geom.arrows(G['q']);P=geom.bars(G['p'],G['pe']);Q=geom.bars(G['q'],G['qe'])
 return G,dict(V=len(G['v']),E=len(G['pe']),F=len(G['active']),S=G['active'][qa<0].tolist(),U=np.where(pa<0)[0].tolist(),P=[b for b in P if b['depth']>1e-12],Q=[b for b in Q if b['depth']>1e-12],min_positive_p=float(min(pa[pa>0])),min_positive_q=float(min(qa[qa>0])),volume=float(G['volume']),g=G['g'].tolist())

def run(inp,out,limit=249):
 N=geom.read_h(inp);G,base=info(N);out=Path(out);out.mkdir(parents=True,exist_ok=True);start=time.time();records=[];good=[]
 supports=[np.where(abs(N@x-1)<1e-8)[0] for x in G['v']]
 edges=sorted(G['pe'].tolist(),key=lambda e:np.linalg.norm(G['v'][e[0]]-G['v'][e[1]]))[:limit]
 for ei,(i,j) in enumerate(edges):
  rows=sorted(set(supports[i])|set(supports[j]));u,v=G['v'][[i,j]]
  for lam in [0.,.25,.5,.75,1.]:
   a=(1-lam)*u+lam*v;NN=N.copy()
   for k in rows:NN[k]+=(1-NN[k]@a)*a/(a@a)
   rec=dict(edge=[i,j],end_supports=[supports[i].tolist(),supports[j].tolist()],rows=list(map(int,rows)),lam=lam,apex=a.tolist(),max_normal_change=float(abs(NN-N).max()))
   try:
    GG,r=info(NN);rec['report']=r
    if r['E']<base['E'] and r['F']==base['F'] and len(r['S'])==1 and len(r['U'])<=2:
     rec['file']=f'CAND{len(good)}.json';good.append(rec);(out/rec['file']).write_text(json.dumps(dict(planes=NN.tolist(),recipe=rec),separators=(',',':'))+'\n')
     print('APEX_ADMIT',len(good)-1,ei,lam,'VEF',r['V'],r['E'],r['F'],'P', [b['depth'] for b in r['P']],'qmargin',r['min_positive_q'],flush=True)
   except (ValueError,AssertionError,np.linalg.LinAlgError) as ex:rec['error']=str(ex)
   records.append(rec)
  if ei%25==0:print('SCOUT',ei,'good',len(good),'sec',time.time()-start,flush=True)
 (out/'SCAN.json').write_text(json.dumps(dict(input=inp,base=base,records=records,good=good,parameters=dict(lambdas=[0,.25,.5,.75,1],support_nomination_tolerance=1e-8,limit=limit),seconds=time.time()-start),separators=(',',':'))+'\n')
 print('SCOUT_DONE',len(records),len(good),time.time()-start,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('inp');p.add_argument('out');p.add_argument('--limit',type=int,default=249);run(**vars(p.parse_args()))
```

## apexflow.py
```python
"""Own-mass H continuation with explicitly shared physical apices.
Each selected support row is orthogonally projected to pass through its named
apices. True maximal facets/edges and the full filled centroid are rebuilt at
every finite trial. No numerical endpoint is an exact acceptance certificate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,time,argparse
from pathlib import Path
import numpy as np,torch
from scipy.optimize import linprog,minimize
sys.path.insert(0,str(Path(__file__).resolve().parent))
from coalesce import geom,info

def transform(raw,config):
 m=config['m'];N=raw[:3*m].reshape(m,3);A=raw[3*m:].reshape(-1,3)
 for i,ids in config['row_apices'].items():
  B=A[ids];nn=N[i];delta=B.T@torch.linalg.solve(B@B.T,torch.ones(len(ids))-B@nn)
  N=N.index_copy(0,torch.tensor([i]),(nn+delta).reshape(1,3))
 return N,A

def widest(x,roots):
 r=(x*x).sum(1);_,_,s=geom.arrows(x);cap=np.full(len(x),-np.inf);pa=np.full(len(x),-1);cap[roots]=np.inf;todo=set(range(len(x)))
 while todo:
  j=max(todo,key=lambda i:(cap[i],r[i],-i));todo.remove(j)
  for i in todo:
   v=min(cap[j],s[i,j])
   if v>cap[i] or(v==cap[i] and(pa[i]<0 or s[i,j]>s[i,pa[i]])):cap[i]=v;pa[i]=j
 ids=np.array([i for i in range(len(x))if i not in roots],int)
 return ids,pa[ids],cap[ids]

def setup(raw,config,pquota=2,qquota=1):
 N,A=transform(torch.tensor(raw),config);N=N.numpy();A=A.numpy();G,r=info(N)
 # Every nominated common apex must genuinely survive, with its whole star.
 api=[]
 for k,a in enumerate(A):
  ds=np.linalg.norm(G['v']-a,axis=1);i=int(ds.argmin())
  if ds[i]>1e-7:raise ValueError('apex no longer actual')
  # Assigned planes may retire while still touching the apex.
  # Their retirement does not violate the raw multi-apex edge budget.
  if np.linalg.matrix_rank(N[config['apex_rows'][k]])<3:raise ValueError('apex rank lost')
  api.append(i)
 if len(set(api))!=len(api):raise ValueError('protected apices merged')
 pairs=[]
 for x,bs,quota in [(G['p'],r['P'],pquota),(G['q'],r['Q'],qquota)]:
  root=int(np.argmax((x*x).sum(1)));roots=[root]+[b['root']for b in bs if b['root']!=root][:quota-1]
  i,j,c=widest(x,roots);pairs.append((i,j))
 G.update(report=r,pairs=pairs,api=api)
 return G

def fields(raw,config,G):
 N,A=transform(raw,config);v=torch.linalg.solve(N[G['triples']],torch.ones((len(G['v']),3,1))).squeeze(-1)
 if len(G['api']):v=v.index_copy(0,torch.tensor(G['api']),A)
 t=v[G['tet']];w=torch.linalg.det(t)/6;V=w.sum();g=(w[:,None]*t.sum(1)/4).sum(0)/V
 p=v-g;nn=N[G['active']];q=nn/(1-nn@g)[:,None]
 return p,q,g,V

def values(raw,config,G,objective='P'):
 p,q,g,V=fields(raw,config,G);out=[]
 for x,(i,j)in zip((p,q),G['pairs']):
  a=x[i];d=x[j]-a;out.append((a*d).sum(1)/(torch.linalg.vector_norm(a,dim=1)*torch.linalg.vector_norm(d,dim=1)))
 loss=p.sum()*0
 if objective in ['P','Q']:
  x=p if objective=='P'else q
  for b in G['report'][objective]:
   i,j=b['edge'];d=x[j]-x[i];t=torch.clamp(-(x[i]*d).sum()/(d*d).sum(),0,1);h=((x[i]+t*d)**2).sum();loss+=1-h/(x[b['root']]**2).sum()
 return torch.cat([*out,loss[None]])

def retract(raw,config,pquota,qquota,objective,margin,trust,ceiling,steps=4):
 for k in range(steps):
  G=setup(raw,config,pquota,qquota);tt=torch.tensor(raw);v=values(tt,config,G,objective).numpy()
  if min(v[:-1])>=margin*.8:return raw,k
  J=torch.func.jacrev(lambda t:values(t,config,G,objective),chunk_size=64)(tt).numpy();W=J[:-1];scale=np.maximum(np.linalg.norm(W,axis=1),1e-10);A=W/scale[:,None];rhs=(margin-v[:-1])/scale;n=len(raw)
  # Keep a predicted share of the actual objective improvement during repair.
  gn=max(np.linalg.norm(J[-1]),1e-10);L=np.vstack([A,-J[-1]/gn]);lb=np.r_[rhs,(v[-1]-ceiling)/gn]
  U=np.vstack([np.c_[-L,np.zeros(len(L))],np.c_[np.eye(n),-np.ones(n)],np.c_[-np.eye(n),-np.ones(n)]])
  op=linprog(np.r_[np.zeros(n),1.],A_ub=U,b_ub=np.r_[-lb,np.zeros(2*n)],bounds=[(-trust,trust)]*n+[(0,trust)],method='highs')
  if not op.success:return raw,k
  d=op.x[:-1];fit=minimize(lambda z:(.5*z@z,z),d,jac=True,method='SLSQP',bounds=[(-trust,trust)]*n,constraints={'type':'ineq','fun':lambda z:L@z-lb,'jac':lambda z:L},options={'maxiter':40,'ftol':1e-13})
  if min(L@fit.x-lb)>-1e-8:d=fit.x
  bad=np.maximum(0,margin-v[:-1]);loss=float(bad@bad);ok=False
  for bt in range(8):
   rr=raw+d*2.**(-bt)
   try:
    zz=setup(rr,config,pquota,qquota);vv=values(torch.tensor(rr),config,zz,objective).numpy();bb=np.maximum(0,margin-vv[:-1]);nl=float(bb@bb)
    if zz['report']['E']<=249 and nl<loss*(1-1e-5*2.**(-bt)) and vv[-1]<=ceiling+1e-9:raw=rr;ok=True;break
   except (ValueError,AssertionError,np.linalg.LinAlgError,RuntimeError):pass
  if not ok:return raw,k
 return raw,steps

def encode(x):return json.dumps(x,separators=(',',':'))+'\n'

def run(inp,out,steps=20,trust=.005,margin=1e-6,objective='P',pquota=2,qquota=1,edge_rank=0,lam=0.,allow_p_increase=.003):
 out=Path(out);out.mkdir(exist_ok=True,parents=True);src=json.loads(Path(inp).read_text())if str(inp).endswith('.json')else None
 if src and 'raw' in src:
  raw=np.array(src['raw']);config=src['config'];config['row_apices']={int(i):v for i,v in config['row_apices'].items()};recipe=src.get('initial_recipe')
 else:
  N=np.array(src['planes'])if src else geom.read_h(inp);G,r=info(N);e=sorted(G['pe'].tolist(),key=lambda e:np.linalg.norm(G['v'][e[0]]-G['v'][e[1]]))[edge_rank];u,v=G['v'][e]
  su=np.where(abs(N@u-1)<1e-8)[0].tolist();sv=np.where(abs(N@v-1)<1e-8)[0].tolist();rows=sorted(set(su)|set(sv));a=(1-lam)*u+lam*v
  config=dict(m=len(N),row_apices={i:[0]for i in rows},apex_rows=[rows]);raw=np.r_[N.ravel(),a];recipe=dict(edge=e,end_supports=[su,sv],lambda_=lam)
 start=setup(raw,config,pquota,qquota);baseP=sum(b['depth']for b in start['report']['P']);hist=[];accepted=0;t0=time.time()
 params=dict(source=inp,steps=steps,trust=trust,margin=margin,objective=objective,pquota=pquota,qquota=qquota,edge_rank=edge_rank,lam=lam,allow_p_increase=allow_p_increase,assigned_planes_may_retire=True,retraction_steps=4,retraction_radius_fraction=.5)
 def save():
  G=setup(raw,config,pquota,qquota);N,A=transform(torch.tensor(raw),config)
  (out/'FINAL.json').write_text(encode(dict(raw=raw.tolist(),config=config,planes=N.numpy().tolist(),apices=A.numpy().tolist(),initial_recipe=recipe,report=G['report'],history=hist,parameters=params,seconds=time.time()-t0)))
 save()
 for it in range(steps):
  G=setup(raw,config,pquota,qquota);tt=torch.tensor(raw);v=values(tt,config,G,objective).numpy();J=torch.func.jacrev(lambda t:values(t,config,G,objective),chunk_size=64)(tt).numpy();W=J[:-1];s=np.maximum(np.linalg.norm(W,axis=1),1e-10);A=W/s[:,None];repair=v[:-1].min()<margin*.8
  rec=dict(iteration=it,accepted=False,repair=bool(repair),min_guard=float(min(v[:-1])),objective=float(v[-1]),counts=[G['report'][k]for k in ['V','E','F']],S=len(G['report']['S']),U=len(G['report']['U']))
  if repair:
   rhs=(margin-v[:-1])/s
   op=linprog(np.r_[np.zeros(len(raw)),1.],A_ub=np.c_[-A,-np.ones(len(A))],b_ub=-rhs,bounds=[(-trust,trust)]*len(raw)+[(0,None)],method='highs')
   if not op.success:hist.append(rec);save();break
   d=op.x[:-1];lower=rhs-1.005*op.x[-1]-1e-12
   fit=minimize(lambda z:(.5*z@z,z),d,jac=True,method='SLSQP',bounds=[(-trust,trust)]*len(raw),constraints={'type':'ineq','fun':lambda z:A@z-lower,'jac':lambda z:A},options={'maxiter':50,'ftol':1e-13})
   if min(A@fit.x-lower)>-1e-8:d=fit.x
  else:
   if objective=='repair':hist.append(rec);save();break
   rhs=(np.minimum(v[:-1],margin)-v[:-1])/s;grad=J[-1];gn=max(np.linalg.norm(grad),1e-15);grad=grad/gn
   op=linprog(grad,A_ub=-A,b_ub=-rhs,bounds=[(-trust,trust)]*len(raw),method='highs')
   if not op.success:hist.append(rec);save();break
   d=op.x;L=np.vstack([A,-grad]);lb=np.r_[rhs,-.7*grad@d]
   fit=minimize(lambda z:(.5*z@z,z),d,jac=True,method='SLSQP',bounds=[(-trust,trust)]*len(raw),constraints={'type':'ineq','fun':lambda z:L@z-lb,'jac':lambda z:L},options={'maxiter':50,'ftol':1e-13})
   if min(L@fit.x-lb)>-1e-8:d=fit.x
  loss=float(np.maximum(0,margin-v[:-1])@np.maximum(0,margin-v[:-1]))
  for bt in range(18):
   trial=raw+d*2.**(-bt)
   try:
    nretract=0
    if not repair:trial,nretract=retract(trial,config,pquota,qquota,objective,margin,trust*.5,float(v[-1]-1e-10))
    GG=setup(trial,config,pquota,qquota);vv=values(torch.tensor(trial),config,GG,objective).numpy();rr=GG['report'];bad=np.maximum(0,margin-vv[:-1]);nl=float(bad@bad)
    if rr['E']>249 or sum(b['depth']for b in rr['P'])>baseP+allow_p_increase:continue
    good=nl<loss*(1-1e-5*2.**(-bt)) if repair else min(vv[:-1])>=margin*.75 and vv[-1]<v[-1]-1e-12
    if good:
     raw=trial;accepted+=1;rec.update(accepted=True,alpha=2.**(-bt),retractions=nretract,new_min=float(min(vv[:-1])),new_objective=float(vv[-1]),report=rr);(out/f'PIN{accepted}.json').write_text(encode(dict(raw=raw.tolist(),config=config,planes=transform(torch.tensor(raw),config)[0].numpy().tolist(),initial_recipe=recipe,report=rr)));break
   except (ValueError,AssertionError,np.linalg.LinAlgError,RuntimeError):pass
  hist.append(rec);save();print('APEXFLOW',json.dumps(rec),flush=True)
  if not rec['accepted']:break
 print('APEXFLOW_DONE',accepted,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('inp');p.add_argument('out');p.add_argument('--steps',type=int,default=20);p.add_argument('--trust',type=float,default=.005);p.add_argument('--margin',type=float,default=1e-6);p.add_argument('--objective',choices=['P','Q','repair'],default='P');p.add_argument('--pquota',type=int,default=2);p.add_argument('--qquota',type=int,default=1);p.add_argument('--edge-rank',type=int,default=0);p.add_argument('--lam',type=float,default=0.);p.add_argument('--allow-p-increase',type=float,default=.003);run(**vars(p.parse_args()))
```
