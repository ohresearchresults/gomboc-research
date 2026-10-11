"""Finite multi-coordinate integer-grid screen from an exact rational checkpoint.
MILP is discovery only. Actual geometry/own-centroid census is recomputed; all
accepted constructions subsequently require two independent exact full audits.
Usage: integer_milp.py BQ_SOURCE input_dir fresh_output
"""
from pathlib import Path
import json,sys,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import csr_matrix,bmat,eye
base,src,out=map(lambda x:Path(x).resolve(),sys.argv[1:]);sys.path[:0]=[str(base/'parent/mechanism/parent_sources')]
from atlas_opt import Atlas
from numeric import recover,mechanics
pd=json.loads((base/'BASIN69_96/GENERATOR.json').read_text());pf=json.loads((base/'BASIN69_96/faces.json').read_text());pm=Atlas(pd,pf);ps=pm.state(pm.u0,False);pa=ps['cu'].argmax(1);a=pm.owners.index([16,18,94]);b=pm.owners.index([18,71,94]);alias=lambda i:(a if i==b else i)-(i>b);pp=[]
for i in range(len(pa)):
 if i==b:continue
 j=int(pa[i]);seen={i}
 while j in (a,b):
  assert j not in seen;seen.add(j);j=int(pa[j])
 pp.append(alias(j))
d=json.loads((src/'GENERATOR.json').read_text());fs=json.loads((src/'faces.json').read_text());m=Atlas(d,fs);m.uparent=np.array(pp);m.sparent=ps['cs'].argmax(1);s=m.state(m.u0);J=s['J']/(d['grid']*m.scale)[None,:];n=m.np;goal=1e-8;bound=8;scale=1e8
A=bmat([[csr_matrix(J*scale),None],[eye(n),-eye(n)],[-eye(n),-eye(n)]],format='csr');lower=np.r_[(goal-s['vals'])*scale,np.full(2*n,-np.inf)];upper=np.r_[np.full(len(s['vals']),np.inf),np.zeros(2*n)]
opts=dict(time_limit=15.,mip_rel_gap=0.,presolve=True)
r=milp(c=np.r_[np.zeros(n),np.ones(n)],integrality=np.r_[np.ones(n),np.zeros(n)],bounds=Bounds(np.r_[np.full(n,-bound),np.zeros(n)],np.full(2*n,bound)),constraints=LinearConstraint(A,lower,upper),options=opts)
print('MILP',r.status,r.message, 'objective',r.fun,flush=True)
if r.x is None:raise SystemExit('NO_INTEGER_ENDPOINT_IN_FINITE_SCREEN')
v=np.rint(r.x[:n]).astype(np.int64);assert np.max(np.abs(v-r.x[:n]))<1e-6
assert min(s['vals']+J@v)>=goal-1e-12
z=json.loads(json.dumps(d));patch=[]
for j in np.flatnonzero(v):
 i,k=map(int,m.free[j]);delta=int(v[j]);z['controls'][i][k]+=delta;patch.append([i,k,delta])
report=mechanics(recover(z)[:m.n],fs,tol=1e-13);out.mkdir(parents=True,exist_ok=False)
for name,obj in [('GENERATOR.json',z),('faces.json',fs),('NUMERICAL.json',report),('PATCH.json',dict(grid=d['grid'],changes=patch,goal=goal,bound=bound,options=opts,solver_status=int(r.status),objective=float(r.fun)))]: (out/name).write_text(json.dumps(obj,sort_keys=True,separators=(',',':')))
print('INTEGER_MILP_ENDPOINT',patch,report,flush=True)
