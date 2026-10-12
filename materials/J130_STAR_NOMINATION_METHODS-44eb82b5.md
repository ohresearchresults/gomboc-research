# material-44eb82b5584d

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J130 star nomination methods — complete sources, versions and exact float checkpoints

Dependency: the complete literal DETACHED_G6.txt in [internal-source-reference], J130_EXACT_STAR_CELLS_AND_LOCAL_GATES.md. That primary material independently reconstructs the two exact bodies and all exact certificates; no optimizer is required for its verification. This companion preserves the numerical methods that produced the nominations. Save each fenced unit with the indicated filename and one terminal newline. No C622 data or old workspace is required.

Executed environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1. All SLSQP outputs and floating spectral decompositions are nomination evidence only. The function bars ignores depths<=1e-13 FOR NUMERICAL SCOUTING ONLY. It is not the exact census, and this omission demonstrably hid small stable births in the initial continuation. The exact primary engine counts every positive bar with rational arithmetic. No numerical experiment here proves family infeasibility. Optimizer replay may depend on environment; exact selected endpoints are frozen in the primary material.

## Executed chronology and commands

First run the exact version generator: python variants130.py. Preserve current star130.py as star130_current.py while choosing historical modules. Each subprocess must start fresh so the selected version is imported.

Initial pilot:
```
cp star130.py star130_current.py
cp star130_initial.py star130.py
OPENBLAS_NUM_THREADS=1 python star130.py 45 0 .1
OPENBLAS_NUM_THREADS=1 python continue130.py RUN_45_0_0p1.npy 12 0
```
Initial RUN45 gave floating211, Q~.461530033927635,25-dimensional cell/4094 inequalities and6 iterations. SEQ0..7 gave main Q approximately .46095430800943404,.4607635930661187,.4607475961074817,.45912487254001355,.45908817285807557,.45908809811098794,.4590880980750226,.4590880980742158. The last was floating S4/U1, not211; two positive facet guards were about9.945e-13 and5.012e-13. The positive bars are not excused by the scout threshold. The continuation stopped on its next initial-state check. Floating near-zero mass residual is not an exact proof.

Fixed-margin nomination:
```
cp star130_fixed_margins.py star130.py
OPENBLAS_NUM_THREADS=1 python star130.py 5 0 .25
OPENBLAS_NUM_THREADS=1 python star130.py 38 0 .25
```
RUN5 had Q~.46159625032336293 (24 iterations). RUN38 had Q~.4607785313985475 (23 iterations,19 dimensions,max inequality~9.56e-14). Its selected11 vertices are the primary exact-star source: rationally project rounded free displacements on exact mass equations and take scale19/20. That exact endpoint and segment are verified separately.

Adaptive nomination:
```
cp star130_current.py star130.py
OPENBLAS_NUM_THREADS=1 python adaptive130.py 0 RUN_38_0_0p25.npy
OPENBLAS_NUM_THREADS=1 python adaptive130.py 1 BEST_0.npy
OPENBLAS_NUM_THREADS=1 python adaptive130.py 2 BEST_1.npy
OPENBLAS_NUM_THREADS=1 python adaptive130.py 3 BEST_2.npy
OPENBLAS_NUM_THREADS=1 python adaptive130.py 4 BEST_3.npy
OPENBLAS_NUM_THREADS=1 python adaptive130.py 5 BEST_4.npy
```
Each round tested three current junior-face drivers and three stated seeds,54 floating nominees total. All reported211. Best choices were ADAPT_0_38_2/.45953368264929473, ADAPT_1_45_4/.45869163025061166, ADAPT_2_5_8/.4579564950485805, ADAPT_3_45_10/.4573881694347227, ADAPT_4_38_12/.4571488481800329, ADAPT_5_5_15/.45705261299536337. Trust.3,maxiter70 and ftol1e-11 are literal in the scripts. BEST5 rounded to grid1e10 gives the primary exact own211 body, Q~.45705261300095035 and a small NONZERO exact centroid. No whole-Q cancellation occurred.

The exact original binary64 starting checkpoints for both continuations are below. They avoid requiring the initial optimizer to match before studying the sequence. Restore them with:
```
python - <<'PY'
import json,numpy as np
from pathlib import Path
from hashlib import sha256
b=Path('FLOAT_STARTS130.json').read_bytes()
assert len(b)==5821 and sha256(b).hexdigest()=='dc19bb1352e6b789f8b8575ce4628a70e86ed927bb90145cb8ce352264bad909'
expected={'RUN_45_0_0p1':'1a531944ccd9935f8d35d8efa920abed5fc34b3c8171c437c7ed60443c0ed8c7','RUN_38_0_0p25':'4cfe41502efed1219c0328240c0553539a1e84d16ab5c6ac1df6590f1e476b21'}
for name,rows in json.loads(b).items():
    a=np.array(rows,dtype=np.float64);assert a.shape==(47,3)
    np.save(name+'.npy',a)
    raw=Path(name+'.npy').read_bytes()
    assert len(raw)==1256 and sha256(raw).hexdigest()==expected[name]
print('J130_FLOAT_STARTS_RESTORED')
PY
```
These are exact FLOAT inputs, not rationally certified bodies; do not promote them independently of the primary exact audit.

## Source manifest

star130.py7260B SHA5ff902f5c6d651312e4a58204de6d3be4704236bc6358a0a16d3889f596cbddf
variants130.py1673B SHAb159ac2102d96ecf67f4122dd25bdef8e208ca32d01286ed198838e3d989b2bf
continue130.py1179B SHA365125233f52925796d36b62682605b49ab2ce1886a90ee34cf2f51ba7275062
adaptive130.py1094B SHA68e3f3603d5a7790b8dc643a469c53d095f4a566faa6727314c027e0b62297f0
FLOAT_STARTS130.json5821B SHAdc19bb1352e6b789f8b8575ce4628a70e86ed927bb90145cb8ce352264bad909
Generated exact versions: star130_initial.py7233B SHAcc13f4833357260f5413944d70578c9291ca5a6fc7f3adfa4afc1ae461f984d6; star130_fixed_margins.py7214B SHA78aa7627daba43820a38cffb1e13c82841b046bd46891495e1d1ee54ef6b8006. The version generator was executed and these hashes matched. Floating reports contain elapsed times, so their file hashes are not reproducibility assertions. Terminal START/CELL/END, STEP/STOP and CHOSEN identify nomination execution, not exact success.

## File: star130.py
```python
#!/usr/bin/env python3
"""J130 numerical nomination in mass-neutral independent-star cells.
Convex quadratic inner constraints; literal final rational audit is separate.
Python3.13.5 NumPy2.3.5 SciPy1.17.0. No optimizer outcome is a family exclusion.
"""
import json,sys,hashlib,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from scipy.linalg import null_space
ROOT=Path(__file__).resolve().parent

def load():
 b=(ROOT/'DETACHED_G6.txt').read_bytes()
 assert hashlib.sha256(b).hexdigest()=='a5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50'
 v=np.array(list(map(int,b.split())));return v[2:].reshape(v[0],3)/v[1]

def geometry(X):
 h=ConvexHull(X);faces=[]
 for t in h.simplices:
  t=list(map(int,t));a,b,c=X[t]
  if np.dot(np.cross(b-a,c-a),h.equations[len(faces),:3])<0:t[1],t[2]=t[2],t[1]
  faces.append(t)
 faces=np.array(sorted(faces));A,B,C=X[faces[:,0]],X[faces[:,1]],X[faces[:,2]]
 dets=np.einsum('ij,ij->i',A,np.cross(B,C));V=dets.sum()/6;g=np.einsum('i,ij->j',dets,A+B+C)/(24*V)
 X=X-g;A,B,C=X[faces[:,0]],X[faces[:,1]],X[faces[:,2]]
 n=np.cross(B-A,C-A);hh=np.einsum('ij,ij->i',n,A);q=n/hh[:,None]
 edges={}
 for fi,t in enumerate(faces):
  for i in range(3):edges.setdefault(tuple(sorted((t[i],t[(i+1)%3]))),[]).append(fi)
 assert all(len(e)==2 for e in edges.values())
 neigh=[[]for _ in X]
 for a,b in edges:neigh[a].append(b);neigh[b].append(a)
 uguards=np.array([max(np.dot(x,X[j]-x)for j in neigh[i])for i,x in enumerate(X)])
 sguards=np.stack([np.einsum('ij,ij->i',n,np.cross(X[faces[:,j]],X[faces[:,(j+1)%3]]))for j in range(3)],axis=1)
 S=np.where(sguards.min(axis=1)>0)[0];U=np.where(uguards<0)[0]
 return dict(X=X,V=V,g=g,F=faces,n=n,h=hh,q=q,E=edges,neigh=neigh,S=S,U=U,sg=sguards,ug=uguards)

def bars(P,edges):
 r=np.einsum('ij,ij->i',P,P);a=list(range(len(P)));peak=r.copy();out=[];es=[]
 for i,j in edges:
  d=P[j]-P[i];t=np.clip(-P[i]@d/(d@d),0,1);z=P[i]+t*d;es.append((z@z,i,j))
 def root(i):
  while a[i]!=i:a[i]=a[a[i]];i=a[i]
  return i
 for lev,i,j in sorted(es,reverse=True):
  i,j=root(i),root(j)
  if i==j:continue
  if peak[i]<peak[j]:i,j=j,i
  de=1-lev/peak[j]
  if de>1e-13:out.append(de)
  a[j]=i
 return sorted(out,reverse=True)

def stats(X):
 d=geometry(X)
 return dict(V=len(set(d['F'].ravel())),E=len(d['E']),F=len(d['F']),SU=[len(d['S']),len(d['U'])],volume=d['V'],g=d['g'].tolist(),S=d['F'][d['S']].tolist(),U=d['U'].tolist(),P=bars(d['X'],d['E']),Q=bars(d['q'],d['E'].values()))

def positive(Q):
 e,v=np.linalg.eigh((Q+Q.T)/2)
 # Exact mathematical formulation uses Q_+. Floating matrix is nomination only.
 return (v*np.maximum(e,0))@v.T

def make_cell(X,driver,seed,trust=.1):
 d=geometry(X);X=d['X'];F=d['F'];N=len(X)
 assert len(d['S'])==2 and len(d['U'])==1
 root=int(d['U'][0]);sr=int(d['S'][np.argmax(np.linalg.norm(d['q'][d['S']],axis=1))]);target=int(next(s for s in d['S']if s!=sr))
 assert driver in F[target] and driver!=root
 rng=np.random.default_rng(seed);order=rng.permutation(N)
 forb={root}|(set(F[target])-{driver});selected=[driver];used=set(d['neigh'][driver])|{driver}|forb
 for i in order:
  if i not in used:selected.append(int(i));used|=set(d['neigh'][i])|{int(i)}
 k=len(selected);p=2*k;P=np.zeros((N,3,p));Dm=np.zeros((3,p));volnormals=[]
 for j,i in enumerate(selected):
  vt=F[np.any(F==i,axis=1)];crosses=[];other=[];det=0
  for t in vt:
   a=t.tolist().index(i);u,w=X[t[(a+1)%3]],X[t[(a+2)%3]];c=np.cross(u,w)
   crosses.append(c);other.append(u+w);det+=X[i]@c
  csum=np.sum(crosses,axis=0);T=null_space(csum.reshape(1,3));assert T.shape==(3,2)
  P[i,:,2*j:2*j+2]=T;volnormals.append(csum/6)
  Di=(det*np.eye(3)+np.einsum('ni,nj->ij',np.array(other),np.array(crosses)))/24
  Dm[:,2*j:2*j+2]=Di@T
 Z=null_space(Dm);P=np.einsum('ijk,kl->ijl',P,Z);p=P.shape[-1]
 assert np.linalg.norm(Dm@Z)<1e-12
 f0=[];G=[];M=[];types=[]
 def put(c,g,Q,kind,margin=0):
  f0.append(c+margin);G.append(g);M.append(positive(Q));types.append(kind)
 # Actual fixed-centre physical forest, all material vertices, no discarded old U.
 parents={}
 for i in range(N):
  if i==root:continue
  j=max(d['neigh'][i],key=lambda j:X[i]@(X[j]-X[i]));parents[i]=j
  a,b=X[i],X[j];A,B=P[i],P[j];rr=a@a
  c=a@(a-b)/rr;g=(A.T@(2*a-b)-B.T@a)/rr;Q=(A.T@(A-B))/rr
  assert c<0
  put(c,g,Q,'U',min(1e-6,-c*.9))
 target_data=None
 for fi,t in enumerate(F):
  a,b,c=X[t];A,B,C=P[t];n=np.cross(b-a,c-a)
  D=np.cross((B-A).T,c-a).T+np.cross(b-a,(C-A).T).T
  h=n@a;hg=D.T@a+A.T@n;nn=n@n;norm=np.sqrt(nn)
  # All point-plane support comparisons, not just adjacent edges.
  for j in range(N):
   if j in t:continue
   Q=D.T@P[j]/norm;g=(D.T@X[j]+P[j].T@n-hg)/norm;c0=(n@X[j]-h)/norm
   assert c0<1e-9
   put(c0,g,Q,'hull',min(1e-9,-c0*.9))
  edges=[]
  for ell in range(3):
   i,j=int(t[ell]),int(t[(ell+1)%3]);aa,bb=X[i],X[j];AA,BB=P[i],P[j]
   cr=np.cross(aa,bb);L=np.cross(AA.T,bb).T+np.cross(aa,BB.T).T
   c0=n@cr/nn;g=(D.T@cr+L.T@n)/nn;Q=D.T@L/nn
   edges.append((c0,g,Q,i,j))
  if fi==target:
   e=next(e for e in edges if driver not in e[-2:]);assert np.linalg.norm(e[2])<1e-10
   target_data=e[:3]
  elif fi==sr:
   for c0,g,Q,i,j in edges:put(-c0,-g,-Q,'Sroot',min(1e-6,c0*.9))
  else:
   c0,g,Q,i,j=min(edges,key=lambda e:e[0]);assert c0<0
   put(c0,g,Q,'S',min(1e-6,-c0*.9))
 # Algebraic checks: all constraints are quadratic and all physical/volume maps exact in their charts.
 f0=np.array(f0);G=np.array(G);M=np.array(M);obj0,objg,objQ=target_data
 return dict(X=X,P=P,d=d,f0=f0,G=G,M=M,obj0=obj0,objg=objg,objQ=objQ,selected=selected,parents=parents,root=root,sr=sr,target=target,Z=Z,trust=trust,types=types)

def solve_cell(c,maxiter=80):
 f0,G,M=c['f0'],c['G'],c['M'];p=G.shape[1]
 def vals(z):return f0+G@z+np.einsum('i,kij,j->k',z,M,z,optimize=True)
 def jac(z):return G+2*np.einsum('kij,j->ki',M,z,optimize=True)
 def obj(z):return float(c['obj0']+c['objg']@z+1e-6*(z@z))
 def grad(z):return c['objg']+2e-6*z
 start=time.monotonic()
 sol=minimize(obj,np.zeros(p),jac=grad,constraints=[dict(type='ineq',fun=lambda z:-vals(z),jac=lambda z:-jac(z))],bounds=[(-c['trust'],c['trust'])]*p,method='SLSQP',options=dict(maxiter=maxiter,ftol=1e-11,disp=False))
 XX=c['X']+np.einsum('ijk,k->ij',c['P'],sol.x)
 st=stats(XX)
 report=dict(success=bool(sol.success),message=str(sol.message),iterations=int(sol.nit),seconds=time.monotonic()-start,selected=c['selected'],oldtarget=c['d']['F'][c['target']].tolist(),root=c['root'],rootface=c['d']['F'][c['sr']].tolist(),initial_objective=float(c['obj0']),final_objective=obj(sol.x),max_inequality=float(vals(sol.x).max()),dimension=p,trust=c['trust'],z=sol.x.tolist(),stats=st)
 return XX,report

def main():
 driver=int(sys.argv[1])if len(sys.argv)>1 else 45;seed=int(sys.argv[2])if len(sys.argv)>2 else 0;trust=float(sys.argv[3])if len(sys.argv)>3 else.1
 X=load()if len(sys.argv)<5 else np.load(sys.argv[4]);print('START',stats(X),flush=True)
 cell=make_cell(X,driver,seed,trust);print('CELL',cell['selected'],cell['G'].shape,flush=True)
 XX,r=solve_cell(cell);name=f'RUN_{driver}_{seed}_{str(trust).replace(".","p")}'
 np.save(ROOT/(name+'.npy'),XX);(ROOT/(name+'.json')).write_text(json.dumps(r,indent=2)+'\n');print('END',json.dumps(r),flush=True)
if __name__=='__main__':main()
```

## File: variants130.py
```python
#!/usr/bin/env python3
"""Recover the two exact historical star130 versions from the current engine."""
from pathlib import Path
from hashlib import sha256
R=Path(__file__).resolve().parent
s=(R/'star130.py').read_text()
assert sha256(s.encode()).hexdigest()=='5ff902f5c6d651312e4a58204de6d3be4704236bc6358a0a16d3889f596cbddf'
def replace_once(s,a,b):
 assert s.count(a)==1,(a,s.count(a))
 return s.replace(a,b)
def save(name,text,expected):
 assert sha256(text.encode()).hexdigest()==expected
 (R/name).write_text(text)
 print(name,len(text.encode()),expected)
f=s
for a,b in [
 ("put(c,g,Q,'U',min(1e-6,-c*.9))","put(c,g,Q,'U',1e-6)"),
 ("put(c0,g,Q,'hull',min(1e-9,-c0*.9))","put(c0,g,Q,'hull',1e-9)"),
 ("put(-c0,-g,-Q,'Sroot',min(1e-6,c0*.9))","put(-c0,-g,-Q,'Sroot',1e-6)"),
 ("put(c0,g,Q,'S',min(1e-6,-c0*.9))","put(c0,g,Q,'S',1e-6)")]:f=replace_once(f,a,b)
save('star130_fixed_margins.py',f,'78aa7627daba43820a38cffb1e13c82841b046bd46891495e1d1ee54ef6b8006')
f=s
for a,b in [
 ('assert driver in F[target] and driver!=root','assert driver in F[target] and driver not in F[sr] and driver!=root'),
 ('forb={root}|(set(F[target])-{driver});','forb=set(F[sr])|{root}|(set(F[target])-{driver});'),
 ("put(c,g,Q,'U',min(1e-6,-c*.9))","put(c,g,Q,'U',min(-c*.05,1e-8))"),
 ("put(c0,g,Q,'hull',min(1e-9,-c0*.9))","put(c0,g,Q,'hull',min(max(-c0,0)*.005,1e-10))"),
 ("  elif fi==sr:\n   for c0,g,Q,i,j in edges:put(-c0,-g,-Q,'Sroot',min(1e-6,c0*.9))\n  else:\n","  elif fi!=sr:\n"),
 ("put(c0,g,Q,'S',min(1e-6,-c0*.9))","put(c0,g,Q,'S',min(-c0*.02,1e-9))")]:f=replace_once(f,a,b)
save('star130_initial.py',f,'cc13f4833357260f5413944d70578c9291ca5a6fc7f3adfa4afc1ae461f984d6')
```

## File: continue130.py
```python
import star130 as s
import numpy as np,json,sys,time
from pathlib import Path
X=np.load(sys.argv[1])if len(sys.argv)>1 else s.load()
num=int(sys.argv[2])if len(sys.argv)>2 else 12
start=int(sys.argv[3])if len(sys.argv)>3 else 0
out=[]
for j in range(start,start+num):
 d=s.geometry(X)
 if len(d['S'])!=2 or len(d['U'])!=1:print('STOP',s.stats(X),flush=True);break
 sr=int(d['S'][np.argmax(np.linalg.norm(d['q'][d['S']],axis=1))]);target=int(next(a for a in d['S']if a!=sr))
 driver=45 if 45 in d['F'][target] and 45 not in d['F'][sr]else int(next(a for a in d['F'][target]if a not in d['F'][sr]and a!=d['U'][0]))
 c=s.make_cell(X,driver,j,.25)
 XX,r=s.solve_cell(c,80);r['seed']=j;r['driver']=driver
 if r['max_inequality']>1e-7:print('REJECT',j,r['max_inequality'],flush=True);break
 X=XX;np.save(s.ROOT/f'SEQ_{j}.npy',X);out.append(r)
 (s.ROOT/f'SEQ_{j}.json').write_text(json.dumps(r,indent=2)+'\n')
 print('STEP',j,'SU',r['stats']['SU'],'Q',r['stats']['Q'],'obj',r['initial_objective'],r['final_objective'],'change',np.max(np.linalg.norm(XX-c['X'],axis=1)),'ineq',r['max_inequality'],flush=True)
 if r['stats']['SU']==[1,1]:print('NUMERICAL110_NOT_EXACT',j,flush=True);break
```

## File: adaptive130.py
```python
import star130 as s
import numpy as np,json,sys
roundid=int(sys.argv[1]);X=np.load(sys.argv[2]);d=s.geometry(X)
sr=int(d['S'][np.argmax(np.linalg.norm(d['q'][d['S']],axis=1))]);target=int(next(a for a in d['S']if a!=sr));old=s.stats(X);best=old['Q'][0];bestX=X;bestid=None
for dr in d['F'][target]:
 if dr==d['U'][0]:continue
 for seed in range(roundid*3,roundid*3+3):
  c=s.make_cell(X,int(dr),seed,.3);XX,r=s.solve_cell(c,70);r['driver']=int(dr);r['seed']=seed
  label=f'ADAPT_{roundid}_{dr}_{seed}'
  np.save(s.ROOT/(label+'.npy'),XX);(s.ROOT/(label+'.json')).write_text(json.dumps(r,indent=2)+'\n')
  st=r['stats'];q=max(st['Q'],default=0)
  good=(r['max_inequality']<1e-9 and st['SU']in([2,1],[1,1]))
  print(label,'SU',st['SU'],'Q',q,'obj',r['final_objective'],'ineq',r['max_inequality'],'good',good,flush=True)
  if good and q<best:best=q;bestX=XX;bestid=label
np.save(s.ROOT/f'BEST_{roundid}.npy',bestX)
(s.ROOT/f'BEST_{roundid}.json').write_text(json.dumps(dict(parent=sys.argv[2],selected=bestid,oldQ=old['Q'],newQ=best),indent=2)+'\n')
print('CHOSEN',roundid,bestid,best,flush=True)
```

## File: FLOAT_STARTS130.json
```json
{"RUN_45_0_0p1":[[-0.2374769006777858,-0.1797619378389082,0.774145405299187],[-0.4875499006777858,-0.26152093783890823,0.6518774052991871],[-0.36181755943635874,-0.21036776468647098,0.7290340407534052],[-0.8444339006777859,-0.3540579378389082,0.026523405299187036],[-0.8181768988522848,-0.3113221926764643,-0.17372311748924332],[-0.6345689006777858,-0.3196749378389082,0.518699405299187],[-0.8196879006777859,-0.4009329378389082,0.24238440529918703],[0.6916240993222141,0.20337406216109177,0.007380405299187032],[0.6125070993222141,0.3441000621610918,0.0016094052991870375],[0.09290409932221419,-0.0855689378389082,0.794793405299187],[0.2897390993222142,-0.04119593783890821,0.734533405299187],[0.19555690696440695,-0.06907665065004442,0.7701202525862845],[0.45398464898008695,-0.04332532192759644,0.6309062033298181],[0.3758680993222142,-0.04922393783890821,0.686775405299187],[0.6300900993222142,-0.023921937838908204,0.428961405299187],[0.5205250993222141,-0.04080193783890821,0.5703384052991871],[0.5790020156984758,-0.03352383733546987,0.5034678885413104],[0.7340220993222142,0.037044062161091795,0.09911940529918703],[-0.1142177517394787,-0.14795981518977389,0.7976930741287908],[-0.009259900677785801,-0.1211429378389082,0.802949405299187],[0.7022650993222141,0.0024950621610917937,0.269375405299187],[0.6706266461553498,-0.011744328743415671,0.3519891667710991],[0.7232949838127744,0.018285492598590428,0.18607946671961936],[0.7335130993222142,0.060932062161091795,0.012839405299187034],[0.7214130993222142,0.07593706216109179,-0.08077959470081296],[0.5756300993222141,0.23149906216109178,-0.33248959470081296],[0.6428850993222142,0.18799806216109177,-0.24643859470081297],[0.6905160993222141,0.13138406216109177,-0.16549659470081296],[0.6858705236562376,-0.04772636957099854,-0.1818799138573441],[-0.7531399006777858,-0.2835159378389082,-0.34065359470081297],[0.21158420115851706,0.44377272769404896,-0.3365989052642635],[0.036884703248524234,0.5518779258493574,-0.16209835117918675],[0.1255020993222142,0.4814490621610918,-0.29138059470081296],[0.5491870993222141,-0.0769789378389082,-0.338534594700813],[0.5953970993222142,-0.20684093783890822,-0.15452559470081298],[0.4478000993222142,0.49105806216109177,-0.03724459470081297],[-0.5041419006777859,-0.4514569378389082,-0.429373594700813],[0.5352190993222141,0.1094140621610918,-0.401202594700813],[-0.036142900677785805,0.5458600621610918,-0.028894594700812973],[0.33389509932221423,0.4335310621610918,-0.356730594700813],[0.5607576905655949,0.33334203650818756,-0.235188791407533],[0.1829180993222142,0.5219060621610918,-0.27153559470081295],[-0.5509028456881631,-0.3196522498513067,-0.5289356149727894],[-0.5016879006777858,-0.15807893783890822,-0.611130594700813],[0.4561680993222142,0.2833470621610918,-0.424964594700813],[-0.3331242020227785,0.1777901106531761,0.10602408943387648],[-0.2101229006777858,-0.3127869378389082,0.10564740529918704]],"RUN_38_0_0p25":[[-0.2374769006777858,-0.1797619378389082,0.774145405299187],[-0.4875499006777858,-0.26152093783890823,0.6518774052991871],[-0.3612459006777858,-0.21009293783890823,0.7291934052991871],[-0.8444339006777859,-0.3540579378389082,0.026523405299187036],[-0.8217729006777859,-0.3150939378389082,-0.16282659470081295],[-0.6345689006777858,-0.3196749378389082,0.518699405299187],[-0.8196879006777859,-0.4009329378389082,0.24238440529918703],[0.6916240993222141,0.20337406216109177,0.007380405299187032],[0.6125070993222141,0.3441000621610918,0.0016094052991870375],[0.09290409932221419,-0.0855689378389082,0.794793405299187],[0.2897390993222142,-0.04119593783890821,0.734533405299187],[0.20189696545455693,-0.06829499722926183,0.7676640357005106],[0.44990354303418545,-0.043015618490387,0.6347169908809568],[0.3758680993222142,-0.04922393783890821,0.686775405299187],[0.6300900993222142,-0.023921937838908204,0.428961405299187],[0.5205250993222141,-0.04080193783890821,0.5703384052991871],[0.5755377085043053,-0.03186618991160012,0.5086503018196062],[0.7340220993222142,0.037044062161091795,0.09911940529918703],[-0.1196719006777858,-0.14891493783890822,0.7975314052991871],[-0.009259900677785801,-0.1211429378389082,0.802949405299187],[0.7022650993222141,0.0024950621610917937,0.269375405299187],[0.6684064638842377,-0.010124901076235938,0.3577642888005303],[0.7224444672922202,0.017969550588028637,0.19199107979941882],[0.7335130993222142,0.060932062161091795,0.012839405299187034],[0.7214130993222142,0.07593706216109179,-0.08077959470081296],[0.5756300993222141,0.23149906216109178,-0.33248959470081296],[0.6428850993222142,0.18799806216109177,-0.24643859470081297],[0.6905160993222141,0.13138406216109177,-0.16549659470081296],[0.6843277168965964,-0.04171366206617455,-0.18905634663263388],[-0.7531399006777858,-0.2835159378389082,-0.34065359470081297],[0.24337616467007733,0.4747681529462712,-0.32121387129378315],[0.043807099322214195,0.5527190621610918,-0.16664859470081297],[0.1255020993222142,0.4814490621610918,-0.29138059470081296],[0.5491870993222141,-0.0769789378389082,-0.338534594700813],[0.5953970993222142,-0.20684093783890822,-0.15452559470081298],[0.4478000993222142,0.49105806216109177,-0.03724459470081297],[-0.5041419006777859,-0.4514569378389082,-0.429373594700813],[0.5352190993222141,0.1094140621610918,-0.401202594700813],[-0.03959949599206995,0.5431232983795077,-0.02685556475492962],[0.33389509932221423,0.4335310621610918,-0.356730594700813],[0.543570395899599,0.3491811055870076,-0.2367312933059304],[0.1829180993222142,0.5219060621610918,-0.27153559470081295],[-0.5295881449765489,-0.2653800078372717,-0.560472675962813],[-0.5016879006777858,-0.15807893783890822,-0.611130594700813],[0.4561680993222142,0.2833470621610918,-0.424964594700813],[-0.4328389006777858,0.0554110621610918,0.14541540529918703],[-0.021634208275454814,-0.2871338000066846,0.05156221436319062]]}
```
