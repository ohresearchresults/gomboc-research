# material-0844362db835

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 2/3: L18 finite own-centroid mass repair

Requires part1, [internal-source-reference] (input and complete geometry helper). Part3 supplies the extension runner, fixed rational nominations and verification commands. This is the complete original executed l18_masslift.py, not an excerpt. Save with final LF:11623 bytes, SHA-2562a115ec11fa06b2153da36c86db018d76ad4fc305c2e493235a7c5913863c794.

The numerical linear algebra nominates rational coefficients rounded at denominator10^6; acceptance, finite moment repair, supporting conditions and the full weak/strict/P/Q census are exact. Physical correction is performed in uncentred coordinates through residual M-cV. Primary tangency in this version is specialized to labels13,22. When adding other cap vertices, generalize that guard rather than silently moving them off the retained cap. The original CLI returns the first valid weak-free endpoint having exactly one P and one Q bar, both reduced; this is explicitly NOT a110 acceptance rule.

## l18_masslift.py
```python
"""Finite homogeneous mass repair on L18, adapted from Clear Harbor 55's analytic
masslift57 result.  Uses uncentred coordinates and residual M-c*V to avoid needlessly
large translated input denominators.  Numeric selection only nominates a rational
direction; exact identities and signs accept it. This is not a global no-go search.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations,groupby
from collections import deque
from pathlib import Path
import json,sys
import numpy as np
from l18_support_search import exact_structure,dot,sub,cross
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ZERO=(F(0),)*3
PRIMARY=[13,22,14,16,24]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,s):return tuple(x*s for x in a)
def det(a,b,c):return dot(a,cross(b,c))
def triangles(faces):
 for f in faces:
  for j in range(1,len(f)-1):yield f[0],f[j],f[j+1]
def mass(p,faces):
 V=F(0);M=ZERO
 for i,j,k in triangles(faces):
  a,b,c=p[i],p[j],p[k];w=det(a,b,c)/6;V+=w;M=add(M,mul(add(add(a,b),c),w/4))
 return V,M
def normals(p,faces):return [cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]])) for f in faces]
def gate(u,v):
 A=dot(u,u);B=dot(u,v);C=dot(v,v);D=A+C-2*B
 if D==0 or B>=A:return A
 if B>=C:return C
 return (A*C-B*B)/D
def bars(x,edges):
 edges=sorted({tuple(sorted(e)) for e in edges});birth=[dot(p,p) for p in x];weight={e:gate(x[e[0]],x[e[1]]) for e in edges}
 par=list(range(len(x)));peak=par.copy();members=[{i} for i in par];result=[]
 def find(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 def path(s,t,level):
  adj=[[] for _ in x]
  for i,j in edges:
   if weight[(i,j)]>=level:adj[i].append(j);adj[j].append(i)
  prev={s:None};todo=deque([s])
  while todo and t not in prev:
   i=todo.popleft()
   for j in sorted(adj[i]):
    if j not in prev:prev[j]=i;todo.append(j)
  assert t in prev
  out=[];i=t
  while i is not None:out.append(i);i=prev[i]
  return out[::-1]
 for level,ee in groupby(sorted(edges,key=lambda e:(-weight[e],e)),key=lambda e:weight[e]):
  adj={}
  for i,j in ee:
   a,b=find(i),find(j)
   if a!=b:adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
  unseen=set(adj);groups=[]
  while unseen:
   a=min(unseen);unseen.remove(a);cc={a};todo=[a]
   while todo:
    u=todo.pop()
    for v in adj[u]:
     if v in unseen:unseen.remove(v);cc.add(v);todo.append(v)
   groups.append(sorted(cc))
  for cc in groups:
   elder=max(cc,key=lambda a:(birth[peak[a]],-peak[a]))
   for a in cc:
    if a==elder or birth[peak[a]]==level:continue
    assert birth[peak[a]]>level;comp=members[a];cut=[e for e in edges if (e[0] in comp)!=(e[1] in comp)]
    assert cut and max(weight[e] for e in cut)==level
    pp=path(peak[a],peak[elder],level)
    assert min(weight[tuple(sorted(e))] for e in zip(pp,pp[1:]))==level
    result.append(dict(peak=peak[a],elder=peak[elder],birth=birth[peak[a]],death=level,depth=(birth[peak[a]]-level)/birth[peak[a]],component=sorted(comp),cut=cut,attaining_edge=next(e for e in cut if weight[e]==level),attaining_path=pp))
   merged=set().union(*(members[a] for a in cc))
   for a in cc:par[a]=elder
   members[elder]=merged
 assert len({find(i) for i in range(len(x))})==1
 return sorted(result,key=lambda b:(-b['depth'],b['peak'],b['elder']))
def load_source(path):
 data=json.loads(Path(path).read_text());z,ff,ee,W,M=exact_structure(data['points']);D=data['denominator'];p=[tuple(F(v,D) for v in q) for q in z];faces=[f['cycle'] for f in ff];edges=list(ee);owners=[ee[e] for e in edges];V,M=mass(p,faces);c=mul(M,1/V);x=[sub(q,c) for q in p];n=normals(x,faces);q=[mul(a,1/dot(a,x[f[0]])) for a,f in zip(n,faces)]
 return dict(p=p,faces=faces,edges=edges,owners=owners,V=V,c=c,x=x,P=bars(x,edges),Q=bars(q,owners))
def null_plane(a):
 k=next(i for i in range(3) if a[i]);out=[]
 for j in range(3):
  if j==k:continue
  v=[F(0)]*3;v[j]=F(1);v[k]=-a[j]/a[k];out.append(tuple(v))
 return out
def star(p,faces,i):
 a=ZERO;B=[[F(0)]*3 for _ in range(3)]
 for f in faces:
  if i not in f:continue
  assert len(f)==3;k=f.index(i);b=p[f[(k+1)%3]];c=p[f[(k+2)%3]];w=cross(b,c);a=add(a,mul(w,F(1,6)))
  for r in range(3):
   for s in range(3):B[r][s]+=(b[r]+c[r])*w[s]/24
 tau=dot(a,p[i]);A=[[B[r][s]+(tau/4 if r==s else 0) for s in range(3)] for r in range(3)];basis=null_plane(a);images=[tuple(dot(row,v) for row in A) for v in basis]
 return a,basis,images
def solve_columns(C,b):
 D=det(*C);assert D
 return [det(*(b if j==k else C[j] for j in range(3)))/D for k in range(3)]
def mass_derivative(p,d,faces):
 v=F(0);out=ZERO
 for i,j,k in triangles(faces):
  a,b,c=p[i],p[j],p[k];da,db,dc=d[i],d[j],d[k];w=det(a,b,c);dw=det(da,b,c)+det(a,db,c)+det(a,b,dc);v+=dw/6
  out=add(out,mul(add(mul(add(add(a,b),c),dw),mul(add(add(da,db),dc),w)),F(1,24)))
 return v,out
def polar_velocity(x,d,faces):
 q=[];dq=[]
 for f in faces:
  a,b,c=[x[i] for i in f[:3]];da,db,dc=[d[i] for i in f[:3]];n=cross(sub(b,a),sub(c,a));dn=add(cross(sub(db,da),sub(c,a)),cross(sub(b,a),sub(dc,da)));h=dot(n,a);dh=dot(dn,a)+dot(n,da)
  q.append(mul(n,1/h));dq.append(mul(sub(mul(dn,h),mul(n,dh)),1/(h*h)))
 return q,dq
def gate_derivative(u,v,du,dv):
 A=dot(u,u);B=dot(u,v);C=dot(v,v);dA=2*dot(u,du);dB=dot(du,v)+dot(u,dv);dC=2*dot(v,dv);D=A+C-2*B
 if D==0 or B>=A:return A,dA
 if B>=C:return C,dC
 N=A*C-B*B;dN=dA*C+A*dC-2*B*dB;dD=dA+dC-2*dB
 return N/D,(dN*D-N*dD)/(D*D)
def depth_derivative(x,d,b):
 i,j=b['attaining_edge'];k=b['peak'];g,dg=gate_derivative(x[i],x[j],d[i],d[j]);r=dot(x[k],x[k]);dr=2*dot(x[k],d[k]);return -dg/r+g*dr/(r*r)
def mechanics(p,faces,edges,owners,c):
 x=[sub(q,c) for q in p];n=normals(x,faces);strict=[[],[],[]];weak=[[],[],[]];zeros=[0,0,0];nb=[set() for _ in x]
 for i,j in edges:nb[i].add(j);nb[j].add(i)
 def rec(k,label,vals):
  zeros[k]+=sum(a==0 for a in vals)
  if all(a>0 for a in vals):strict[k].append(label)
  elif all(a>=0 for a in vals):weak[k].append(label)
 for fi,f in enumerate(faces):rec(0,fi,[dot(cross(n[fi],sub(x[j],x[i])),mul(x[i],-1)) for i,j in zip(f,f[1:]+f[:1])])
 for i in range(len(x)):rec(1,i,[-dot(x[i],sub(x[j],x[i])) for j in sorted(nb[i])])
 for (i,j),(f,g) in zip(edges,owners):
  d=sub(x[j],x[i]);dd=dot(d,d);t=-dot(x[i],d);R=add(mul(x[i],dd),mul(d,t));a,b=n[f],n[g];aa=dot(a,a);ab=dot(a,b);bb=dot(b,b);assert aa*bb-ab*ab>0
  rec(2,[i,j],[t,dd-t,bb*dot(R,a)-ab*dot(R,b),aa*dot(R,b)-ab*dot(R,a)])
 q=[mul(a,1/dot(a,x[f[0]])) for a,f in zip(n,faces)];PB=bars(x,edges);QB=bars(q,owners)
 if not any(map(len,weak)):
  s,u,h=map(len,strict);assert s+u-h==2 and len(PB)==u-1 and len(QB)==s-1
 return dict(strict=list(map(len,strict)),additional_weak=list(map(len,weak)),primitive_zero=zeros,stable=[faces[f] for f in strict[0]],roots=strict[1],saddles=strict[2],P=PB,Q=QB)
def valid_complex(p,faces):
 failures=[]
 for fi,f in enumerate(faces):
  n=cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]]));h=dot(n,p[f[0]]);sf=set(f)
  for j,q in enumerate(p):
   gap=h-dot(n,q)
   if (j in sf and gap!=0) or (j not in sf and gap<=0):failures.append((fi,f,j,gap))
  for i,j in zip(f,f[1:]+f[:1]):
   u=cross(n,sub(p[j],p[i]))
   for k in f:
    if k not in (i,j) and dot(u,sub(p[k],p[i]))<=0:failures.append((fi,f,('rim',i,j,k),F(-1)))
 return failures

def make_chart(R,pair=None,selection=None):
 p=R['p'];faces=R['faces'];big=max(faces,key=len);n=cross(sub(p[big[1]],p[big[0]]),sub(p[big[2]],p[big[0]]));axes=[tuple(F(i==j) for i in range(3)) for j in range(3)];modes=[];labels=[]
 for i in PRIMARY:
  choices=null_plane(n) if i in (13,22) else axes
  for b in choices:
   d=[ZERO for _ in p];d[i]=b;modes.append(d);labels.append((i,b))
 forbidden=set(PRIMARY)
 for f in faces:
  if set(f)&set(PRIMARY):forbidden.update(f)
 eligible=[i for i in range(len(p)) if i not in forbidden and all(len(f)==3 for f in faces if i in f)]
 pairs=[pair] if pair else combinations(eligible,2)
 for u,v in pairs:
  if any(u in f and v in f for f in faces):continue
  controls=[];images=[]
  for i in [u,v]:
   a,basis,im=star(p,faces,i);controls.extend((i,b) for b in basis);images.extend(im)
  for sel in ([selection] if selection else combinations(range(4),3)):
   C=[images[j] for j in sel]
   if not det(*C):continue
   control=[controls[j] for j in sel];gp=[];gq=[];full=[]
   for d0 in modes:
    dv,dm=mass_derivative(p,d0,faces);rr=sub(dm,mul(R['c'],dv));coef=solve_columns(C,mul(rr,-1));d=list(d0)
    for a,(i,b) in zip(coef,control):d[i]=add(d[i],mul(b,a))
    dv,dm=mass_derivative(p,d,faces);assert sub(dm,mul(R['c'],dv))==ZERO
    q,dq=polar_velocity(R['x'],d,faces);gp.append(depth_derivative(R['x'],d,R['P'][0]));gq.append(depth_derivative(q,dq,R['Q'][0]));full.append(d)
   G=np.array([[float(v) for v in gp],[float(v) for v in gq]])
   if np.linalg.matrix_rank(G)<2:continue
   # Nominate minimal Euclidean physical vertex velocity, not merely parameter norm.
   T=np.asarray(full,float).reshape(len(modes),-1).T;inv=np.linalg.pinv(T.T@T,rcond=1e-12);weights=-inv@G.T@np.linalg.solve(G@inv@G.T,np.ones(2))
   physical=T@weights;scale=max(1,float(np.max(np.abs(physical))));weights=weights/scale
   exact=[F(round(float(w)*10**6),10**6) for w in weights]
   if dot(gp,exact)>=0 or dot(gq,exact)>=0:continue
   direction=[ZERO for _ in p];velocity=[ZERO for _ in p]
   for w,d0,df in zip(exact,modes,full):
    for i in range(len(p)):direction[i]=add(direction[i],mul(d0[i],w));velocity[i]=add(velocity[i],mul(df[i],w))
   return dict(pair=[u,v],selection=list(sel),controls=control,C=C,determinant=det(*C),direction=direction,velocity=velocity,derivative_P=dot(gp,exact),derivative_Q=dot(gq,exact),weights=exact,mode_labels=labels)
 return None

def construct(R,ch,t):
 y=[add(q,mul(d,t)) for q,d in zip(R['p'],ch['direction'])];V0,M0=mass(y,R['faces']);coef=solve_columns(ch['C'],mul(sub(M0,mul(R['c'],V0)),-1))
 for a,(i,b) in zip(coef,ch['controls']):y[i]=add(y[i],mul(b,a))
 V,M=mass(y,R['faces']);assert V==V0 and M==mul(R['c'],V)
 return y,V

def dump(path,value):Path(path).write_text(json.dumps(value,sort_keys=True,separators=(',',':'),default=str)+'\n')

def main():
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('--out',default='/mnt/data/masslift');args=ap.parse_args();out=Path(args.out);out.mkdir(exist_ok=True);R=load_source(args.input);ch=make_chart(R);assert ch
 dump(out/'chart.json',ch)
 print('CHART',ch['pair'],ch['selection'],'rank3','dP',float(ch['derivative_P']),'dQ',float(ch['derivative_Q']),flush=True)
 baseline=mechanics(R['p'],R['faces'],R['edges'],R['owners'],R['c']);dump(out/'parent.json',baseline)
 print('BASE',baseline['strict'],'P',float(R['P'][0]['depth']),'Q',float(R['Q'][0]['depth']),flush=True)
 tests=[]
 for j in range(0,32):
  t=F(1,2**j);y,V=construct(R,ch,t);bad=valid_complex(y,R['faces']);row={'j':j,'t':t,'invalid_count':len(bad),'first_failures':bad[:3]}
  if bad:
   tests.append(row);print('STEP',j,'INVALID',len(bad),'FIRST',bad[0][:3],flush=True);continue
  A=mechanics(y,R['faces'],R['edges'],R['owners'],R['c']);row.update(A);row['volume']=V
  print('STEP',j,A['strict'],'P',float(A['P'][0]['depth']) if A['P'] else 0,'Q',float(A['Q'][0]['depth']) if A['Q'] else 0,flush=True)
  tests.append(row)
  if not any(A['additional_weak']) and not any(A['primitive_zero']) and len(A['P'])==len(A['Q'])==1 and A['P'][0]['depth']<R['P'][0]['depth'] and A['Q'][0]['depth']<R['Q'][0]['depth']:
   dump(out/'endpoint.json',{'points':y,'centroid':R['c'],'density':1,'volume':V,'t':t});dump(out/'endpoint_audit.json',A);print('EXACT_FINITE_MASS_REPAIR_JOINT_DESCENT_PASS',j,flush=True);break
 dump(out/'tests.json',tests)
if __name__=='__main__':main()
```
