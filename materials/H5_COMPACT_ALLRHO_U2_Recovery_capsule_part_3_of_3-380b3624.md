# material-380b36249f85

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_COMPACT_ALLRHO_11PARAMETER_U2_V1 — Recovery capsule part 3/3

All THREE ordered parts are required. Part 1 contains the common manifest, commands, pins and allroot_stress.py; part 2 contains taylor_tube.py. This part contains the complete tube_cover.py. Save its fence UTF-8/LF with final newline: 9179 bytes, SHA256 e4f0071f6333237eb55f11f66548a395d4d17a837e94ab1966ca283a849b28b3. Build and exact check commands and all expected terminal markers are in part 1. No parent implementation or precomputed certificate is required.

```python
#!/usr/bin/env python3
"""Finite compactified ALL-rho H5 box cover: deterministic numerical locator, exact rational proof."""
from taylor_tube import *

def build(folder,mult=F(1)):
 import numpy as np
 from scipy.optimize import linprog
 folder=Path(folder);folder.mkdir(exist_ok=True,parents=True)
 if not (folder/'primal_search.json').exists():search('primal',folder)
 db=json.loads((folder/'primal_search.json').read_text())['certificates']
 keys={tuple(tuple(z) for z in t) for t in db}
 ij=tuple((i,j) for a,b in EDGES for i,j in ((a,b),(b,a)));ids={e:k for k,e in enumerate(ij)}
 tree_data=list(rooted_trees(10,EDGES));trees=np.array([sum(1<<ids[e] for e in t) for r,t in tree_data],np.uint64)
 masks=[sum(1<<ids[(i,j)] for i,j,w in t) for t in db]
 leaves=[];nodes=0;solves=0;start=time.time()
 def install(terms):
  key=tuple(tuple(z) for z in terms)
  if key in keys:return db.index(terms)
  keys.add(key);db.append(terms);masks.append(sum(1<<ids[(i,j)] for i,j,w in terms));return len(db)-1
 def point_w(tree,pp,lo,hi):
  nonlocal solves
  X,C,*_=actual(rho=(lo+hi)/2);eig,U=np.linalg.eigh(np.array(C,float));T=(U*(1/np.sqrt(eig)))@U.T;Z=np.array(X,float)@T.T
  rows=[]
  for e in tree:
   A=T@pp[ids[e],0]@T.T
   rows.append([A[0,0],A[1,1],A[2,2],2*A[0,1],2*A[0,2],2*A[1,2]])
  rays=[np.array(v,float) for v in product((-1,0,1),repeat=3) if any(v)];rays += [Z[b]-Z[a] for a,b in EDGES];rays+=list(Z)
  G=[]
  for v in rays:
   v=v/np.linalg.norm(v);G.append([-v[0]**2,-v[1]**2,-v[2]**2,-2*v[0]*v[1],-2*v[0]*v[2],-2*v[1]*v[2],0.])
  A=np.vstack((np.array(G),np.c_[-np.array(rows),np.ones(len(tree))]));eq=np.zeros((1,7));eq[0,:3]=1.;obj=np.zeros(7);obj[-1]=-1.
  sol=linprog(obj,A_ub=A,b_ub=np.zeros(len(A)),A_eq=eq,b_eq=[1.],bounds=[(None,None)]*7,method='highs');solves+=1
  if not sol.success or sol.x[-1]>=-1e-8:return None
  return -sol.ineqlin.marginals[len(G):]
 def robust_w(tree,pp,er,H):
  nonlocal solves
  es=[ids[e] for e in tree];nn=len(tree);Q=-np.einsum('ik,enkl,jl->enij',H,pp[es],H);R=np.einsum('ik,ekl,jl->eij',abs(H),er[es],abs(H))
  C=[];D=[]
  for i in range(3):
   j,k=[z for z in range(3) if z!=i]
   for s,t in product((-1,1),repeat=2):
    a=Q[:,:,i,i]-s*Q[:,:,i,j]-t*Q[:,:,i,k]
    C.append(a[:,0]-np.sum(R[:,i,:],axis=1));D.append(a[:,1:].T)
  C=np.array(C);D=np.array(D);nv=nn+12*N+1
  A=np.zeros((12+24*N,nv));rowno=0
  for r in range(12):
   A[rowno,:nn]=-C[r];A[rowno,nn+r*N:nn+(r+1)*N]=1;A[rowno,-1]=1;rowno+=1
   for k in range(N):
    A[rowno,:nn]=D[r,k];A[rowno,nn+r*N+k]=-1;rowno+=1
    A[rowno,:nn]=-D[r,k];A[rowno,nn+r*N+k]=-1;rowno+=1
  eq=np.zeros((1,nv));eq[0,:nn]=1;obj=np.zeros(nv);obj[-1]=-1
  sol=linprog(obj,A_ub=A,b_ub=np.zeros(len(A)),A_eq=eq,b_eq=[1.],bounds=[(0,None)]*(nv-1)+[(None,None)],method='highs');solves+=1
  return (sol.x[:nn],sol.x[-1]) if sol.success else (None,None)
 def locate(tree,pp,er,rr,lo,hi):
  ww=point_w(tree,pp,lo,hi)
  if ww is None:return None
  es=[ids[e] for e in tree]
  for iteration in range(4):
   P=-np.einsum('e,enij->nij',ww,pp[es]);E=np.einsum('e,eij->ij',ww,er[es]);H=template(P[0])
   if H is None:return None
   HH=proof_H(H)
   if margin_float(P,E,H)>1e-7:
    for den in (1000,100000,10000000,1000000000):
     terms=[(i,j,str(F(float(w)).limit_denominator(den))) for (i,j),w in zip(tree,ww) if F(float(w)).limit_denominator(den)>0]
     if terms and accept(rr,ids,terms,HH):return terms,HH
   ww,value=robust_w(tree,pp,er,H)
   if ww is None:return None
  return None
 def solve(lo,hi,depth):
  nonlocal nodes
  nodes+=1
  # Wide rho intervals are split before allocating a high-dimensional locator.
  if hi-lo>F(13,16):
   m=(lo+hi)/2;solve(lo,m,depth+1);solve(m,hi,depth+1);return
  ij2,rr,V=compile_box(lo,hi,mult);assert ij2==ij
  pp,er=numerical(rr);good=[];covered=np.zeros(len(trees),bool)
  for no,terms in enumerate(db):
   es=[ids[(i,j)] for i,j,w in terms];w=np.array([float(F(w)) for i,j,w in terms]);P=-np.einsum('e,enij->nij',w,pp[es]);E=np.einsum('e,eij->ij',w,er[es]);H=template(P[0])
   if H is None or margin_float(P,E,H)<=1e-7:continue
   good.append((no,proof_H(H)));covered|=(trees&np.uint64(masks[no]))==masks[no]
  failed=None
  for ti in np.flatnonzero(~covered):
   if covered[ti]:continue
   found=locate(tree_data[ti][1],pp,er,rr,lo,hi)
   if found is None:failed=int(ti);break
   terms,H=found;k=install(terms);good.append((k,H));covered|=(trees&np.uint64(masks[k]))==masks[k]
  if failed is not None:
   print('SPLIT',lo,hi,'covered',int(sum(covered)),'failed',failed,'depth',depth,'solves',solves,flush=True)
   if depth>=11:
    (folder/'failure.json').write_text(jdump({'lo':str(lo),'hi':str(hi),'mult':str(mult),'tree':tree_data[failed],'covered':int(sum(covered)),'solves':solves}))
    raise RuntimeError('Locator unresolved: not a mathematical exclusion or counterexample')
   m=(lo+hi)/2;solve(lo,m,depth+1);solve(m,hi,depth+1);return
  # Greedy support cover followed by exact acceptance of every chosen use.
  gm=np.array([masks[k] for k,H in good],np.uint64);hit=(trees[None,:]&gm[:,None])==gm[:,None]
  remain=np.ones(len(trees),bool);scores=hit.sum(axis=1);chosen=[]
  while np.any(remain):
   gi=int(np.argmax(scores));assert scores[gi]>0;k,H=good[gi]
   if not accept(rr,ids,db[k],H):
    scores[gi]=0;hit[gi,:]=False;continue
   new=remain&hit[gi];chosen.append({'stress':k,'H':H});remain&=~new;scores-=hit[:,new].sum(axis=1)
  leaves.append({'lo':str(lo),'hi':str(hi),'uses':chosen})
  (folder/'partial.json').write_text(jdump({'version':1,'mult':str(mult),'leaves':leaves,'stress_certificates':db,'nodes':nodes,'solves':solves}))
  print('LEAF',lo,hi,'uses',len(chosen),'database',len(db),'nodes',nodes,'solves',solves,'sec',round(time.time()-start,1),flush=True)
 solve(F(0),F(1),0)
 used=sorted({use['stress'] for leaf in leaves for use in leaf['uses']});reindex={old:k for k,old in enumerate(used)}
 for leaf in leaves:
  for use in leaf['uses']:use['stress']=reindex[use['stress']]
 result={'version':1,'mult':str(mult),'theta':list(map(str,THETA)),'radii':list(map(str,RADII)),'projectivity_radius':'1/200','range':['0','1'],'gauge':'compact-lambda-horizontal','stress_certificates':[db[k] for k in used],'leaves':leaves,'nodes':nodes,'solves':solves}
 path=folder/'tube_certificate.json';path.write_text(jdump(result))
 print('H5_COMPACT_ALLRHO_TUBE_BUILT',len(used),len(leaves),sum(len(x['uses']) for x in leaves),path.stat().st_size,'seconds',time.time()-start,flush=True)
 return result

def check(path):
 data=json.loads(Path(path).read_text());assert data['version']==1;mult=F(data['mult']);assert 0<mult<=1
 assert data['theta']==list(map(str,THETA)) and data['radii']==list(map(str,RADII)) and data['projectivity_radius']=='1/200' and data['range']==['0','1'] and data['gauge']=='compact-lambda-horizontal'
 # Genuine raw-lattice chart and positive homogeneous denominators throughout.
 low=[c-r for c,r in zip(THETA,RADII)];up=[c+r for c,r in zip(THETA,RADII)]
 b,c,p,q,a,d,u,v=range(8)
 assert 0<low[b]<up[b]<low[c]<up[c]<1 and 0<low[a]<up[a]<low[d]<up[d]<1
 assert low[p]>0 and low[q]>0 and up[p]+up[q]<1 and low[u]>0 and low[v]>0 and up[u]/low[b]+up[v]/low[a]<1
 assert 1-F(7,200)>0
 ij=tuple((i,j) for a,b in EDGES for i,j in ((a,b),(b,a)));ids={e:k for k,e in enumerate(ij)}
 trees=[sum(1<<ids[e] for e in t) for r,t in rooted_trees(10,EDGES)];assert len(trees)==48790
 db=data['stress_certificates'];masks=[]
 for terms in db:
  assert terms and all(F(w)>0 for i,j,w in terms) and len({(i,j) for i,j,w in terms})==len(terms)
  masks.append(sum(1<<ids[(i,j)] for i,j,w in terms))
 end=F(0);uses=0;guards=0;minmargin=None;minvol=None
 for leaf in data['leaves']:
  lo,hi=F(leaf['lo']),F(leaf['hi']);assert lo==end and lo<hi;end=hi
  ij2,rr,V=compile_box(lo,hi,mult);assert ij==ij2 and V.c-V.dev()>F(1,10)
  minvol=V.c-V.dev() if minvol is None else min(minvol,V.c-V.dev())
  ms=[]
  for use in leaf['uses']:
   k=use['stress'];m=accept(rr,ids,db[k],use['H']);assert m>F(1,8192)
   W=sum(F(w) for i,j,w in db[k]);assert W*sum(F(x)**2 for row in use['H'] for x in row)<2**14
   minmargin=m if minmargin is None else min(m,minmargin);uses+=1;guards+=12;ms.append(masks[k])
  assert all(any(t&m==m for m in ms) for t in trees)
  print('CHECK_LEAF',str(lo),str(hi),len(ms),flush=True)
 assert end==1 and data['nodes']==2*len(data['leaves'])-1
 print('H5_COMPACT_ALLRHO_11_PARAMETER_ALLROOT_U2_PASS',len(db),len(data['leaves']),uses,48790,flush=True)
 print('H5_RATIONAL_TAYLOR_GERSHGORIN_GUARDS_PASS',guards,'mult',mult,flush=True)
 print('H5_TRUE_VOLUME_POSITIVE_PASS',float(minvol),'minimum_guard',float(minmargin),flush=True)
 # V<2 from the positive-coordinate cube; these are exact rational guards.
 assert F(200,199)**3<2 and 3*F(200,199)**2<4
 delta=F(1,2**43);assert delta<F(1,1680) and 3362*delta<1 and 8*3362*delta<F(1,2**28)
 print('H5_ALLRHO_NORMALIZED_STRESS_MARGIN_PASS 2^-28',flush=True)
 print('H5_ALLRHO_TRUE_LATTICE_DISPLACEMENT_TUBE_PASS 2^-43',flush=True)
 return data

if __name__=='__main__':
 if sys.argv[1]=='build':build(sys.argv[2],F(sys.argv[3]) if len(sys.argv)>3 else F(1))
 elif sys.argv[1]=='check':check(sys.argv[2])
 else:raise ValueError('build FOLDER [MULT] | check CERTIFICATE')
```
