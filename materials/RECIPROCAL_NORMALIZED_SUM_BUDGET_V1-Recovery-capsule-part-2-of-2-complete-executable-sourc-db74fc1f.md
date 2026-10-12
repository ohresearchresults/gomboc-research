# material-db74fc1fa17d

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# RECIPROCAL_NORMALIZED_SUM_BUDGET_V1 — Recovery capsule part 2 of 2

Part1 is [internal-source-reference], SHA9602faff6f074210688078e47506926d0cfe8984ea82817735b80ff5bad3fc69. This part contains EVERY byte of the exact deterministic verifier and optional numerical discovery unit. No external data, originating sandbox or old family workspace is needed for the verifier. Save the first fence as reciprocal_budget.py with UTF8/LF/final newline. Run python -B -S reciprocal_budget.py build, then python -B -S reciprocal_budget.py check. Python>=3.10,stdlib only, assertions enabled.
Expected source7281B SHAeb1c5324c09a7886adf29a4abdf40a7a04177dd2d6158d72e3fd3fdbee1b079f; regenerated reciprocal_budget.json28737B SHAc983c9e193033fe23e4196020471511657171f9974b039f61dc9d64937ec848f.

```python
#!/usr/bin/env python3
"""Exact true-10/17/9 common-inverse obstruction. Python >=3.10, stdlib.
Run: python -B -S reciprocal_budget.py build|check [output.json]
The 12 positive weights are solved from literal support, not rounded LP output.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json,sys
assert __debug__
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,c):return tuple(c*x for x in a)
def zero(n=3):return tuple(tuple(F(0) for j in range(n)) for i in range(n))
def eye(n=3):return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def ma(A,B):return tuple(add(a,b) for a,b in zip(A,B))
def ms(A,c):return tuple(scale(a,c) for a in A)
def tr(A):return sum((A[i][i] for i in range(len(A))),F(0))
def tp(A):return tuple(zip(*A))
def mv(A,x):return tuple(dot(a,x) for a in A)
def mm(A,B):return tuple(tuple(dot(a,b) for b in tp(B)) for a in A)
def outer(a,b):return tuple(tuple(x*y for y in b) for x in a)
def sym(a,b):return ms(ma(outer(a,b),outer(b,a)),F(1,2))
def solve(A,b):
 n=len(A);assert len(b)==n and all(len(row)==n for row in A)
 R=[list(row)+[v] for row,v in zip(A,b)]
 for j in range(n):
  p=next((i for i in range(j,n) if R[i][j]),None);assert p is not None
  R[j],R[p]=R[p],R[j];v=R[j][j];R[j]=[t/v for t in R[j]]
  for i in range(n):
   if i!=j:
    v=R[i][j];R[i]=[x-v*y for x,y in zip(R[i],R[j])]
 return tuple(row[-1] for row in R)
def inv(A):return tp(tuple(solve(A,e) for e in eye(len(A))))
def det(A):
 if len(A)==1:return A[0][0]
 return sum(((-1)**j*A[0][j]*det(tuple(tuple(x for k,x in enumerate(row) if k!=j) for row in A[1:])) for j in range(len(A))),F(0))
def spd(A):return all(det(tuple(tuple(A[i][j] for j in range(k)) for i in range(k)))>0 for k in (1,2,3))
def smat(seq):
 ans=zero()
 for A in seq:ans=ma(ans,A)
 return ans
def fan(Y,faces,apex):
 volume=F(0);first=(F(0),)*3;second=zero()
 for f in faces:
  for j in range(1,len(f)-1):
   T=[Y[i] for i in (apex,f[0],f[j],f[j+1])]
   d=abs(det(tuple(sub(T[i],T[0]) for i in (1,2,3))))/6
   s=tuple(sum(v[i] for v in T) for i in range(3))
   volume+=d;first=add(first,scale(s,d/4))
   second=ma(second,ms(ma(outer(s,s),smat(outer(v,v) for v in T)),d/20))
 g=scale(first,1/volume)
 cov=ma(ms(second,1/volume),ms(outer(g,g),-1))
 return volume,g,cov
Y=tuple(tuple(F(v) for v in row) for row in [
 (F(3,8),0,0),(F(3,4),0,0),(F(3,4),F(1,4),0),
 (F(1,3),F(2,3),0),(0,F(2,3),0),(0,F(1,4),0),
 (F(1,8),F(1,8),0),(0,0,1),(1,0,1),(0,1,1)])
FACETS=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
 (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
P_SUPPORT=((0,6),(0,7),(3,9),(4,5),(5,6),(5,7))
R_SUPPORT=((0,2),(0,7),(1,2),(7,2),(3,4),(5,4))
volume,g,C=fan(Y,FACETS,0);assert (volume,g,C)==fan(Y,FACETS,9)
assert volume==F(1583,3456) and g==(F(25691,75984),F(49717,151968),F(3311,6332))
X=tuple(sub(v,g) for v in Y);Ci=inv(C);assert spd(C)
poles=[]
for f in FACETS:
 q=None
 for ids in combinations(f,3):
  A=tuple(X[i] for i in ids)
  if det(A):q=solve(A,(F(1),)*3);break
 assert q is not None
 assert tuple(i for i,v in enumerate(X) if dot(q,v)==1)==tuple(sorted(f))
 assert all(dot(q,v)<=1 for v in X)
 poles.append(q)
poles=tuple(poles)
edges=sorted({tuple(sorted((f[i-1],f[i]))) for f in FACETS for i in range(len(f))})
assert len(edges)==17 and len(poles)==9 and len(X)==10
# Convex support intersections and cyclic facet boundaries are checked above.
# Each of the 17 boundary edges is in precisely two maximal facets.
edges_dual={e:tuple(i for i,f in enumerate(FACETS) if all(v in f for v in e)) for e in edges}
assert all(len(d)==2 for d in edges_dual.values())
def tensor(points,e):i,j=e;return ms(sym(points[i],sub(points[j],points[i])),-1)
def vector(A):return tuple(A[i][j] for i,j in ((0,0),(1,1),(2,2),(0,1),(0,2),(1,2)))
def weights(points,support,target):
 cols=tuple(vector(tensor(points,e)) for e in support)
 w=solve(tp(cols),vector(target));assert all(t>0 for t in w)
 assert smat(ms(tensor(points,e),a) for e,a in zip(support,w))==target
 return w
r=tuple(map(F,(3,4,2)));s=mv(Ci,r);k=dot(r,s);beta=F(5,3)
Q=ma(C,ms(outer(r,r),-beta/k));R=ma(Ci,ms(outer(s,s),-beta/k))
wp=weights(X,P_SUPPORT,Q);wr=weights(poles,R_SUPPORT,R)
assert R==mm(mm(Ci,Q),Ci)
assert all(tuple(sorted(e)) in edges for e in P_SUPPORT)
assert all(tuple(sorted(e)) in edges_dual.values() for e in R_SUPPORT)
M0=ma(Ci,ms(outer(s,s),F(7)/k));N0=ma(C,ms(outer(r,r),F(7)/k))
Ni=ma(C,ms(outer(r,r),-F(7,8)/k));Mi=ma(Ci,ms(outer(s,s),-F(7,8)/k))
assert all(spd(a) for a in (M0,N0,Mi,Ni))
assert mm(M0,Ni)==eye() and mm(Mi,N0)==eye()
assert mm(M0,N0)==ma(eye(),ms(outer(s,r),F(63)/k))
def primitive(points,e,M):i,j=e;return dot(points[i],mv(M,sub(points[j],points[i])))
pp=tuple(primitive(X,e,M0) for e in P_SUPPORT);rr=tuple(primitive(poles,e,N0) for e in R_SUPPORT)
assert all(x>0 for x in pp+rr)
assert tr(mm(M0,C))==10 and tr(mm(N0,Ci))==10
assert sum(a*b for a,b in zip(wp,pp))/10==F(1,3)
assert sum(a*b for a,b in zip(wr,rr))/10==F(1,3)
# The two separately feasible normalized spectra are exactly (8,1,1)/10.
B=mm(M0,C);assert mm(ma(B,ms(eye(),-1)),ma(B,ms(eye(),-8)))==zero()
B=mm(N0,Ci);assert mm(ma(B,ms(eye(),-1)),ma(B,ms(eye(),-8)))==zero()
def census(M,N):
 assert mm(M,N)==eye();dp={};dr={}
 for e,d in edges_dual.items():
  for i,j in (e,e[::-1]):dp[(i,j)]=primitive(X,(i,j),M)
  for f,h in (d,d[::-1]):dr[(f,h)]=primitive(poles,(f,h),N)
 assert len(dp)==len(dr)==34 and all(x!=0 for x in tuple(dp.values())+tuple(dr.values()))
 U=[i for i in range(10) if all(v<0 for (j,l),v in dp.items() if j==i)]
 S=[i for i in range(9) if all(v<0 for (j,l),v in dr.items() if j==i)]
 H=[list(e) for e,d in edges_dual.items() if max(dp[e],dp[e[::-1]],dr[d],dr[d[::-1]])<0]
 assert len(S)+len(U)-len(H)==2
 return {'stable':S,'unstable':U,'saddle_edges':H,'weak':[0,0,0],
         'primal':[[list(e),str(dp[e])] for e in sorted(dp)],
         'polar':[[list(e),str(dr[e])] for e in sorted(dr)]}
def frac(A):
 if isinstance(A,(tuple,list)):return [frac(v) for v in A]
 return str(A)
report={'name':'ACTUAL_PRISM_12_ARROW_COMMON_INVERSE_BUDGET_CONTROL_V1',
 'vertices':frac(Y),'facets':FACETS,'edges':edges,'volume':str(volume),'centroid':frac(g),
 'covariance':frac(C),'poles':frac(poles),'r':frac(r),'k':str(k),'beta':str(beta),
 'primal_support':P_SUPPORT,'polar_support':R_SUPPORT,'primal_weights':frac(wp),'polar_weights':frac(wr),
 'Q':frac(Q),'R':frac(R),'M0':frac(M0),'N0':frac(N0),
 'primal_selected_positive':frac(pp),'polar_selected_positive':frac(rr),
 'physical_M0':census(M0,Ni),'physical_N0_inverse':census(Mi,N0),
 'unrestricted_strict_gap':'1/3','ratio9_strict_gap':'136/273'}
raw=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
assert len(sys.argv) in (2,3) and sys.argv[1] in ('build','check')
path=Path(sys.argv[2]) if len(sys.argv)==3 else Path(__file__).with_suffix('.json')
if sys.argv[1]=='build':path.write_bytes(raw)
else:assert path.read_bytes()==raw
print('ACTUAL_PRISM_12_ARROW_COMMON_INVERSE_EXACT_PASS',len(raw),hashlib.sha256(raw).hexdigest())
for key in ('physical_M0','physical_N0_inverse'):
 d=report[key];print(key,'S',d['stable'],'U',d['unstable'],'H',d['saddle_edges'],'weak000')
```

## Complete numerical discovery unit
This is not needed for verification or recovery of the frozen object. Save as discover_fixed2.py. Exact3427B SHA5d4c6298df5cb4bd138981eeea3423eb3f4da3cc7e01938976ba88f152b16fba. Run mkdir -p /mnt/data/reciprocal_budget; OPENBLAS_NUM_THREADS=1 python discover_fixed2.py. Python3.13.5,NumPy2.3.5,SciPy1.17.0,SymPy1.14.0. The literal absolute path is this optional discovery unit's output destination, not an external input dependency. The canonical stdlib verifier above accepts an arbitrary output path and needs no such directory.

```python
import itertools, json
import sympy as S
import numpy as np
from scipy.optimize import linprog
F=S.Rational
V=[S.Matrix(x) for x in [(F(3,8),0,0),(F(3,4),0,0),(F(3,4),F(1,4),0),(F(1,3),F(2,3),0),(0,F(2,3),0),(0,F(1,4),0),(F(1,8),F(1,8),0),(0,0,1),(1,0,1),(0,1,1)]]
faces=[(6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9)]
vol=F(0); first=S.zeros(3,1); second=S.zeros(3)
for f in faces:
 for i in range(1,len(f)-1):
  T=[V[k] for k in (0,f[0],f[i],f[i+1])]
  d=abs(S.det(S.Matrix.hstack(T[1]-T[0],T[2]-T[0],T[3]-T[0])))/6
  sm=sum(T,S.zeros(3,1)); vol+=d; first+=d*sm/4
  second+=d*(sm*sm.T+sum((t*t.T for t in T),S.zeros(3)))/20
cent=first/vol; X=[v-cent for v in V]; cov=second/vol-cent*cent.T; ci=cov.inv()
assert vol==F(1583,3456)
poles=[]
for face in faces:
 for triple in itertools.combinations(face,3):
  B=S.Matrix.vstack(*(X[j].T for j in triple))
  if B.det():
   q=B.inv()*S.ones(3,1);break
 assert all((q.dot(x)<=1) for x in X)
 assert all(q.dot(X[i])==1 for i in face)
 poles.append(q)
edges=sorted({tuple(sorted((f[k-1],f[k]))) for f in faces for k in range(len(f))})
dual=sorted(tuple(i for i,f in enumerate(faces) if a in f and b in f) for a,b in edges)
def sy(a,b):return (a*b.T+b*a.T)/2
def tensors(points,eds):return {(i,j):-sy(points[i],points[j]-points[i]) for a,b in eds for i,j in ((a,b),(b,a))}
P=tensors(X,edges); R=tensors(poles,dual)
def vec(m):return S.Matrix([m[i,j] for i,j in ((0,0),(1,1),(2,2),(0,1),(0,2),(1,2))])
print('cov',cov,'edges',edges,'dual',dual, flush=True)
covnp=np.array(cov,dtype=float);cinp=np.array(ci,dtype=float)
Pe=list(P);Re=list(R);Pm=np.array([np.array(P[e],dtype=float) for e in Pe]);Rm=np.array([np.array(R[e],dtype=float) for e in Re])
for it,r0 in enumerate([(3,4,2)]):
 if r0==(0,0,0):continue
 r=S.Matrix(r0);sr=ci*r;k=(r.T*sr)[0]
 # Both individual normalised spectra are (8,1,1)/10.
 mp=ci+7*sr*sr.T/k; np_=cov+7*r*r.T/k
 pf=[e for e in Pe if S.trace(P[e]*mp)<0];rf=[e for e in Re if S.trace(R[e]*np_)<0]
 if len(pf)<3 or len(rf)<3:continue
 z=S.zeros(6,1)
 A=S.Matrix.hstack(*[vec(P[e]).col_join(z) for e in pf],*[z.col_join(vec(R[e])) for e in rf],vec(r*r.T/k).col_join(vec(sr*sr.T/k)))
 target=vec(cov).col_join(vec(ci));An=np.array(A,dtype=float);bn=np.array(target,dtype=float).ravel()
 scale=np.maximum(np.max(abs(An),axis=1),abs(bn));An=An/scale[:,None];bn=bn/scale
 objective=np.zeros(A.cols);objective[-1]=0
 result=linprog(objective,A_eq=An,b_eq=bn,bounds=[(0,None)]*(A.cols-1)+[(1.6666666666666667,1.6666666666666667)],method='highs')
 if result.success:
  inds=[j for j,val in enumerate(result.x) if val>1e-7]
  last=inds.pop(); assert last==A.cols-1
  sol=S.linsolve((A[:,inds],target-F(5,3)*A[:,-1])); vals=list(sol)[0]+(F(5,3),); inds.append(last)
  if any(v.free_symbols for v in vals):continue
  if any(v<0 for v in vals):continue
  assert inds[-1]==A.cols-1
  b=vals[-1]
  if b>=F(91,41):continue
  data={'r':r0,'beta':str(b),'primal':[],'polar':[],'vol':str(vol),'centroid':list(map(str,cent)),'cov':[[str(cov[i,j]) for j in range(3)] for i in range(3)]}
  for j,v in zip(inds,vals):
   if j<len(pf):data['primal'].append([pf[j],str(v)])
   elif j<len(pf)+len(rf):data['polar'].append([rf[j-len(pf)],str(v)])
  print('FOUND',json.dumps(data),flush=True)
  open('/mnt/data/reciprocal_budget/control_fixed.json','w').write(json.dumps(data,indent=2)+'\n')
  break
else:print('NO_EXACT_CONTROL_FOUND',flush=True)
```
