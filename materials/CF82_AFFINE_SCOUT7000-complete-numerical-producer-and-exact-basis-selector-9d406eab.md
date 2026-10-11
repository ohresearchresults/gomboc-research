# material-9d406eabb135

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# CF82_AFFINE_SCOUT7000: complete executed numerical producer and basis selector

This preserves a finite numerical survey and the nominations used by the NEW exact two-component exclusion. The finite survey itself is NOT an exact/global exclusion. Actual execution:3500 metrics per input,7000 total; seed2026092152; seven logarithmic perturbation scales0.002,0.01,0.05,0.2,0.7,2,4;500 draws per scale. Each draw is G=exp(scale*(Z+Z^T)/2 with trace removed), independent Gaussian Z entries; the code below fixes order and RNG. Physical census uses G; stable census uses the inverse metric on the polar at the same actual physical centroid. Both actual centroids are integrated exactly once, not optimized as free parameters. No sampled metric had numerical S1 or U1. Identity baselines remain own211; random sampling deliberately does not include identity. Thus absence of sampled U1 is not a claim that U1 affine images do not exist. No exact endpoint construction or full weak/H census was performed for these sampled metrics. The strongest accepted conclusion is the separate exact CONNECTED-component exclusion, not this survey.

## Dependencies, replay and receipts
Complete point inputs are in mandatory proof-data material [internal-source-reference]. Write its JSON block as AFFINE_CF82_DATA.json. Recreate each original named input with json.dumps(record['body'],separators=(',',':')).encode(), WITHOUT newline. Their complete literal coordinates and expected hashes are in that data. No worker result or old material is otherwise needed.
Save the first block as affine_scout.py and run:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python affine_scout.py
Observed CPython3.13.5,NumPy2.3.5,SciPy1.17.0. Complete producer6272bytes SHA9ae434e61f55f3248be4ea372fe64a8d644f8cb5bf403b9f193e8254dc8b7860. Output SCOUT_REPORT.json14845bytes SHA0ec0f273388437f7c5555e4b2238f0480f3b4437447f580ad39fded547aec567. Terminal CF82_AFFINE_SCOUT_COMPLETE 14845 0ec0f273388437f7c5555e4b2238f0480f3b4437447f580ad39fded547aec567. Report includes every histogram bin, best nominated metric, all LP entries/active-row nominations, and exact input centroids. No unrecorded optimization follows those7000 trials.

For independent regeneration of the exact certificate DATA from numerical nominations, also save VERIFY_AFFINE_CF82.py from [internal-source-reference] and the second block here as BUILD_AFFINE_DATA.py. Run OPENBLAS_NUM_THREADS=1 python BUILD_AFFINE_DATA.py. The1496byte selector SHA776ec8d6fbe622bfa2de6a1a8bd48bc2e5bed537a1b96924df3a62450e7ea62a rationally chooses valid five-row bases from the LP active lists. It checks exact nonnegative dual coefficients and exact feasibility; it does not trust float LP status. Output AFFINE_CF82_DATA.json7352bytes SHA60913fb5964ab5f86537760ede7e77f112f2b959420070bc5ba282f5a951cfdf. Terminal CF82_AFFINE_DATA_SOURCE_COMPLETE. Exact verification thereafter needs only the two proof parts and standard library, not this producer or optimizer.

## affine_scout.py
```python
"""Finite affine scout of two exactly specified CF82 inputs, NOT a global exclusion.
CPython 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0. Single-thread environment.
Input identities and all settings are literal. Seed 2026092152.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import hashlib,json,sys
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog
ROOT=Path(__file__).resolve().parent
SOURCES={'CF82_RESERVE42_G5.json':'b3cb940d430aa31dae1444de1ec07fa72a6092d2b9326cb5bfc99b61f7a395e6','CF82_MAIN83_G7.json':'1d63a06ee4e9c0d39d258f1016dbc6ded1b141b5394af12e33f9ef959265b95a'}
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def coeff(x,d): return [x[0]*d[0],x[1]*d[1],x[2]*d[2],x[0]*d[1]+x[1]*d[0],x[0]*d[2]+x[2]*d[0],x[1]*d[2]+x[2]*d[1]]
def model(name):
 raw=(ROOT/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==SOURCES[name]
 d=json.loads(raw);p=list(map(tuple,d['points']));grid=d['grid'];hull=ConvexHull(np.array(p,dtype=float)/grid)
 faces=[];owners={}
 for tri in hull.simplices:
  a,b,c=map(int,tri);n=cross(sub(p[b],p[a]),sub(p[c],p[a]));h=dot(n,p[a]);ss=[dot(n,v)-h for v in p]
  if min(ss)>=0:b,c=c,b;n=tuple(-v for v in n);h=-h;ss=[-v for v in ss]
  assert max(ss)==0 and sum(v==0 for v in ss)==3
  faces.append((a,b,c,n,h))
 faces.sort(key=lambda f:tuple(sorted(f[:3])))
 for k,f in enumerate(faces):
  for a,b in zip(f[:3],f[1:3]+f[:1]):owners.setdefault(tuple(sorted((a,b))),[]).append(k)
 active=sorted({i for e in owners for i in e});assert len(active)-len(owners)+len(faces)==2 and all(len(v)==2 for v in owners.values())
 reached={active[0]}
 while True:
  new=reached|{j for i,j in owners if i in reached}|{i for i,j in owners if j in reached}
  if new==reached:break
  reached=new
 assert len(reached)==len(active)
 for i in active:
  links={}
  for f in faces:
   if i in f[:3]:
    a,b=[v for v in f[:3] if v!=i];links.setdefault(a,set()).add(b);links.setdefault(b,set()).add(a)
  assert all(len(v)==2 for v in links.values());reach={next(iter(links))}
  while True:
   new=reach|set().union(*(links[j] for j in reach))
   if new==reach:break
   reach=new
  assert len(reach)==len(links)
 D=sum(dot(p[a],cross(p[b],p[c])) for a,b,c,n,h in faces);assert D>0
 N=tuple(sum(dot(p[a],cross(p[b],p[c]))*(p[a][k]+p[b][k]+p[c][k]) for a,b,c,n,h in faces) for k in range(3))
 centroid=tuple(F(v,4*D*grid) for v in N)
 Xexact={i:tuple(F(p[i][k],grid)-centroid[k] for k in range(3)) for i in active}
 Qexact={i:tuple(F(t)/(F(h,grid)-dot(n,centroid)) for t in n) for i,(a,b,c,n,h) in enumerate(faces)}
 def pack(V,edges):
  ids=list(V);v=np.array([[float(t) for t in V[i]] for i in ids]);idx={j:i for i,j in enumerate(ids)};adj={i:[] for i in ids}
  for i,j in edges:adj[i].append(j);adj[j].append(i)
  arrows=[(i,j) for i in ids for j in sorted(adj[i])];co=np.array([[float(t) for t in coeff(V[i],sub(V[j],V[i]))] for i,j in arrows]);delta=np.array([[float(t) for t in sub(V[j],V[i])] for i,j in arrows])
  vi=np.array([idx[i] for i,j in arrows]);dest=np.array([idx[j] for i,j in arrows]);offset=np.cumsum([0]+[len(adj[i]) for i in ids])[:-1]
  return dict(ids=ids,v=v,adj=adj,arrows=arrows,co=co,delta=delta,vi=vi,dest=dest,offset=offset)
 return dict(name=name,Xexact=Xexact,Qexact=Qexact,centroid=centroid,faces=faces,owners=owners,P=pack(Xexact,owners),Q=pack(Qexact,[tuple(o) for o in owners.values()]))
def census(pack,G):
 gv=np.array([G[0,0],G[1,1],G[2,2],G[0,1],G[0,2],G[1,2]])
 vals=pack['co']@gv;rad=np.einsum('ij,jk,ik->i',pack['v'],G,pack['v']);dd=np.einsum('ij,jk,ik->i',pack['delta'],G,pack['delta']);cos=vals/np.sqrt(rad[pack['vi']]*dd)
 escape=np.maximum.reduceat(cos,pack['offset']);return [pack['ids'][i] for i in np.where(escape<0)[0]],escape,cos,rad

def cone(m):
 pack=m['P'];roots,esc,cos,rad=census(pack,np.eye(3));assert roots==[0]
 arrows=[];rows=[]
 for i,k in enumerate(pack['ids']):
  if k==0:continue
  lo=pack['offset'][i];hi=pack['offset'][i+1] if i+1<len(pack['ids']) else len(cos);j=lo+int(np.argmax(cos[lo:hi]));arrows.append(pack['arrows'][j]);rows.append(pack['co'][j])
 C=np.array(rows);Cn=C/np.linalg.norm(C,axis=1)[:,None];trace=np.array([1,1,1,0,0,0.]);out=[]
 for k in range(6):
  for sign in [1,-1]:
   obj=np.eye(6)[k]*sign;r=linprog(obj,A_ub=-Cn,b_ub=np.zeros(len(C)),A_eq=trace[None,:],b_eq=[3],bounds=[(None,None)]*6,method='highs')
   out.append(dict(coordinate=k,sign=sign,status=int(r.status),x=r.x.tolist() if r.success else None,active=np.where(np.abs(Cn@r.x)<1e-7)[0].tolist() if r.success else []))
 return dict(arrows=arrows,bounds=out)

def run():
 rng=np.random.default_rng(2026092152);report=dict(seed=2026092152,settings=dict(samples_per_scale=500,log_scales=[0.002,0.01,0.05,0.2,0.7,2.0,4.0]),bodies={})
 for name in SOURCES:
  m=model(name);P,Q=m['P'],m['Q'];c=cone(m);hist={};s1=[];u1=[];best=None
  for scale in report['settings']['log_scales']:
   for j in range(500):
    z=rng.normal(size=(3,3));H=(z+z.T)/2;H-=np.eye(3)*np.trace(H)/3;w,v=np.linalg.eigh(H*scale);G=(v*np.exp(w))@v.T;Gi=(v*np.exp(-w))@v.T
    U,ep,cp,rp=census(P,G);S,eq,cq,rq=census(Q,Gi);key=f'{len(S)},{len(U)}';hist[key]=hist.get(key,0)+1
    loss=float(np.sum(np.minimum(ep[np.arange(len(ep))!=np.argmax(rp)],0)**2)+np.sum(np.minimum(eq[np.arange(len(eq))!=np.argmax(rq)],0)**2));rec=dict(scale=scale,iteration=j,S=S,U=U,loss=loss,G=G.tolist())
    if best is None or loss<best['loss']:best=rec
    if len(S)==1:s1.append(rec)
    if len(U)==1:u1.append(rec)
  report['bodies'][name]=dict(complex=[len(P['ids']),len(m['owners']),len(Q['ids'])],centroid=list(map(str,m['centroid'])),initial_S=census(Q,np.eye(3))[0],initial_U=census(P,np.eye(3))[0],cone=c,histogram=hist,best=best,s1=s1,u1=u1)
  print(name,report['bodies'][name]['complex'],'hist',hist,'S1',len(s1),'U1',len(u1),'best',best['S'],best['U'],best['loss'],flush=True)
 payload=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode();(ROOT/'SCOUT_REPORT.json').write_bytes(payload);print('CF82_AFFINE_SCOUT_COMPLETE',len(payload),hashlib.sha256(payload).hexdigest(),flush=True)
if __name__=='__main__':run()
```

## BUILD_AFFINE_DATA.py
```python
"""Deterministic exact selection from the finite scout's LP nominations.
Dependencies: affine_scout.py and its complete named literal inputs, SCOUT_REPORT.json,
VERIFY_AFFINE_CF82.py. CPython 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0.
"""
import json,hashlib
from itertools import combinations
from fractions import Fraction as F
from pathlib import Path
from affine_scout import model,SOURCES
from VERIFY_AFFINE_CF82 import coeff,sub,solve,dot
ROOT=Path(__file__).resolve().parent;r=json.loads((ROOT/'SCOUT_REPORT.json').read_bytes());out={}
for name,rec in sorted(r['bodies'].items()):
 m=model(name);X=m['Xexact'];tree=rec['cone']['arrows'];C=[coeff(X[i],sub(X[j],X[i])) for i,j in tree];trace=[F(1)]*3+[F(0)]*3;bases=[]
 for item in rec['cone']['bounds']:
  k=item['coordinate'];sign=item['sign'];c=[F(0)]*6;c[k]=F(sign);chosen=None
  for ids in combinations(item['active'],5):
   B=[C[i] for i in ids]+[trace]
   try:v=solve(B,[0]*5+[3]);y=solve(list(map(list,zip(*B))),c)
   except StopIteration:continue
   if min(y[:5])>=0 and all(dot(row,v)>=0 for row in C):chosen=list(ids);break
  assert chosen is not None,(name,item);bases.append(chosen)
 out[name]=dict(body=json.loads((ROOT/name).read_bytes()),input_sha256=SOURCES[name],faces=[list(f[:3]) for f in m['faces']],tree=tree,bases=bases)
raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();(ROOT/'AFFINE_CF82_DATA.json').write_bytes(raw);print('CF82_AFFINE_DATA_SOURCE_COMPLETE',len(raw),hashlib.sha256(raw).hexdigest())
```
