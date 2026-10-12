# material-ebb79e4eef0c

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J71 L18 root-pair theorem and exact G3 turnover — Recovery capsule part 2/2

Object identity: J71_L18_ROOTPAIR_G3. BOTH parts are required. Part1 is material [internal-source-reference] and contains the complete exact input, scope, commands and observed output identities. This part contains the COMPLETE executable rootpair_exact.py,12447 bytes,SHA256 6db7a6739614e3a9318f9e12700874e1f05415fd718008edfe06c8aca3f44887. Extract the code verbatim including one terminal LF. Python standard library only. The exact G3 body is a NONRECORD strict345/weak000, not own110.

```python
"""Complete exact L18 root-pair support-cell theorem, standard library only.
python -B -S rootpair_exact.py --input l18_exact_points.json --out rootpair_exact.json
An exhaustive exact hull enumeration fixes the source identity and actual COM.
Rational support combinations prove whole-cell statements, not sampled tests.
No SciPy, external certificate, or originating sandbox is required.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
from functools import reduce
from math import gcd,lcm

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def primitive(a):
 g=reduce(gcd,map(abs,a));return tuple(x//g for x in a)
def fraction_key(a):
 d=lcm(*(x.denominator for x in a));return primitive(tuple(int(x*d) for x in a))
def polygon(ids,p,n):
 drop=max(range(3),key=lambda k:abs(n[k]));u,v=[k for k in range(3) if k!=drop];ids=sorted(ids,key=lambda i:(p[i][u],p[i][v]))
 def turn(i,j,k):return (p[j][u]-p[i][u])*(p[k][v]-p[i][v])-(p[j][v]-p[i][v])*(p[k][u]-p[i][u])
 def half(seq):
  out=[]
  for i in seq:
   while len(out)>1 and turn(out[-2],out[-1],i)<=0:out.pop()
   out.append(i)
  return out
 cyc=half(ids)[:-1]+half(reversed(ids))[:-1]
 if dot(cross(sub(p[cyc[1]],p[cyc[0]]),sub(p[cyc[2]],p[cyc[0]])),n)<0:cyc.reverse()
 j=cyc.index(min(cyc));return cyc[j:]+cyc[:j]
def exact_hull(data):
 p=[tuple(map(int,v)) for v in data['points']];D=int(data['denominator']);planes=set()
 for i,j,k in combinations(range(len(p)),3):
  n=cross(sub(p[j],p[i]),sub(p[k],p[i]))
  if n==(0,0,0):continue
  h=dot(n,p[i]);pos=neg=False
  for q in p:
   a=dot(n,q)-h;pos=pos or a>0;neg=neg or a<0
   if pos and neg:break
  if pos and neg or not pos and not neg:continue
  if pos:n=tuple(-v for v in n);h=-h
  planes.add(primitive((*n,h)))
 faces=[];edges=defaultdict(list);W=0;M=[0,0,0]
 for plane in sorted(planes):
  cyc=polygon([i for i,q in enumerate(p) if dot(plane[:3],q)==plane[3]],p,plane[:3]);faces.append(cyc)
  for i,j in zip(cyc,cyc[1:]+cyc[:1]):edges[tuple(sorted((i,j)))].append(len(faces)-1)
  for j in range(1,len(cyc)-1):
   ids=(cyc[0],cyc[j],cyc[j+1]);d=dot(p[ids[0]],cross(p[ids[1]],p[ids[2]]));W+=d
   for k in range(3):M[k]+=d*sum(p[i][k] for i in ids)
 active=sorted({v for e in edges for v in e});assert all(len(v)==2 for v in edges.values());assert len(active)-len(edges)+len(faces)==2 and W>0
 c=tuple(F(M[k],4*W*D) for k in range(3));P=[tuple(F(v,D) for v in q) for q in p];nb=defaultdict(list)
 for i,j in edges:nb[i].append(j);nb[j].append(i)
 for ns in nb.values():ns.sort()
 return p,D,P,faces,edges,nb,c


def solve(A,b):
 n=len(b);a=[list(row)+[rhs] for row,rhs in zip(A,b)]
 for k in range(n):
  j=next(j for j in range(k,n) if a[j][k]);a[j],a[k]=a[k],a[j];s=a[k][k];a[k]=[v/s for v in a[k]]
  for j in range(n):
   if j!=k:
    s=a[j][k];a[j]=[x-s*y for x,y in zip(a[j],a[k])]
 return [row[-1] for row in a]
def normalized(a,b):
 s=max(map(abs,a));assert s>0;return tuple(x/s for x in a),b/s,s
def L1_box(p,lo,hi):return sum(max(abs(a-b),abs(a-c)) for a,b,c in zip(p,lo,hi))
def projection_certificate(R,ids,m,r2):
 A=[R[i][0] for i in ids];B=[R[i][1] for i in ids]
 lam=solve([[dot(a,b) for b in A] for a in A],[dot(a,m)-b for a,b in zip(A,B)])
 assert all(x>=0 for x in lam)
 a=tuple(sum(w*v[k] for w,v in zip(lam,A)) for k in range(3));h=sum(w*b for w,b in zip(lam,B));d=dot(a,m)-h;aa=dot(a,a)
 assert aa>0 and d>0 and r2-d*d/aa<0
 return {'ids':ids,'lambda':lam,'d':d,'aa':aa,'upper':r2-d*d/aa}
def census(P,faces,edges,c):
 x=[sub(v,c) for v in P];normals=[cross(sub(x[f[1]],x[f[0]]),sub(x[f[2]],x[f[0]])) for f in faces];nb=defaultdict(list);strict=[[],[],[]];weak=[[],[],[]];zeros=[0,0,0]
 for i,j in edges:nb[i].append(j);nb[j].append(i)
 def rec(k,label,a):
  zeros[k]+=sum(v==0 for v in a)
  if all(v>0 for v in a):strict[k].append(label)
  elif all(v>=0 for v in a):weak[k].append(label)
 for fi,f in enumerate(faces):rec(0,f,[dot(cross(normals[fi],sub(x[j],x[i])),tuple(-v for v in x[i])) for i,j in zip(f,f[1:]+f[:1])])
 for i,ns in nb.items():rec(1,i,[-dot(x[i],sub(x[j],x[i])) for j in ns])
 for (i,j),(f,g) in edges.items():
  e=sub(x[j],x[i]);ee=dot(e,e);t=-dot(x[i],e);v=tuple(ee*x[i][k]+t*e[k] for k in range(3));n,m=normals[f],normals[g];nn=dot(n,n);mm=dot(m,m);nm=dot(n,m);assert nn*mm-nm*nm>0
  rec(2,[i,j],[t,ee-t,mm*dot(n,v)-nm*dot(m,v),nn*dot(m,v)-nm*dot(n,v)])
 assert not any(map(len,weak)) and len(strict[0])+len(strict[1])-len(strict[2])==2
 return {'strict':list(map(len,strict)),'additional_weak':list(map(len,weak)),'primitive_zero':zeros,'stable':strict[0],'roots':strict[1],'saddles':strict[2]}
def verify(data):
 p,D,P,faces,edges,nb,c=exact_hull(data)
 assert (len(nb),len(edges),len(faces))==(75,204,131)
 parent=census(P,faces,edges,c);assert parent['strict']==[2,2,2] and parent['additional_weak']==parent['primitive_zero']==[0,0,0]
 assert nb[62]==[49,58,59,64,65,68,70] and nb[58]==[49,54,55,59,62]
 sources=[('fixed',[65,73,70],None),('fixed',[54,58,59],None),('star',[62,64,59],58),('star',[62,65,70],68),('star',[62,49,65],58),('star',[62,58,49],55)]
 R=[]
 for kind,f,w in sources:
  assert f in faces or any(set(f)==set(g) for g in faces)
  if kind=='fixed':
   n=cross(sub(P[f[1]],P[f[0]]),sub(P[f[2]],P[f[0]]));a=n;b=dot(n,P[f[0]])
   assert all(dot(a,v)<=b for v in P)
  else:
   root,i,j=f;assert root==62;n=cross(sub(P[i],P[w]),sub(P[j],P[w]));a=tuple(-v for v in n);b=-dot(n,P[w]);assert dot(a,P[62])<b
  R.append(normalized(a,b))
 bound_ids=[(0,-1,[1,3,5]),(0,1,[0,2,4]),(1,-1,[0,1,4]),(1,1,[0,2,5]),(2,-1,[1,3,5]),(2,1,[0,2,4])]
 lo=[None]*3;hi=[None]*3
 for k,sgn,ids in bound_ids:
  lam=solve([[R[i][0][j] for i in ids] for j in range(3)],[F(sgn*(j==k)) for j in range(3)]);assert all(x>=0 for x in lam);h=sum(w*R[i][1] for i,w in zip(ids,lam))
  if sgn>0:hi[k]=h
  else:lo[k]=-h
 assert all(a<b for a,b in zip(lo,hi))
 ball_ids={49:[2,3,5],59:[2,3,4],64:[0,2,4],65:[0,2],68:[0,2,4],70:[0,2,4]};balls={};thresholds=[]
 for w,ids in ball_ids.items():
  m=tuple((a+b)/2 for a,b in zip(P[w],c));r2=dot(sub(P[w],c),sub(P[w],c))/4;balls[w]=projection_certificate(R,ids,m,r2)
  thresholds.append((f'62-to-{w}',-balls[w]['upper']/L1_box(P[w],lo,hi)))
 for w in nb[58]:
  if w==62:continue
  q=dot(sub(P[58],c),sub(P[w],P[58]));assert q<0;thresholds.append((f'58-to-{w}',-q/sum(map(abs,sub(P[w],P[58])))))
 r6=dot(sub(P[6],c),sub(P[6],c));r58=dot(sub(P[58],c),sub(P[58],c));r62=sum(max((lo[k]-c[k])**2,(hi[k]-c[k])**2) for k in range(3))
 thresholds.extend([('radius6-over-62',(r6-r62)/(2*L1_box(P[6],lo,hi))),('radius6-over-58',(r6-r58)/(2*sum(map(abs,sub(P[6],P[58])))))])
 eps=F(1,20);assert all(eps<t for name,t in thresholds)
 # Loss of 62 forces three fixed local roots. For a perturbed actual centre,
 # q_v(z,c)>=0 relaxes the old non-U halfspace by eps*max_box |v-z|_1.
 eps4=F(1,1000);m=tuple((a+b)/2 for a,b in zip(P[58],c));r2=dot(sub(P[58],c),sub(P[58],c))/4;extra={}
 for v,ids in [(59,[1,4,6]),(64,[4,7])]:
  a=tuple(-x for x in sub(P[v],c));R.append(normalized(a,dot(a,P[v])));idx=len(R)-1;assert idx==ids[-1]
  proof=projection_certificate(R,ids,m,r2);herror=proof['lambda'][-1]*eps4*L1_box(P[v],lo,hi)/R[idx][2]
  assert proof['d']>herror
  perturbed=r2-(proof['d']-herror)**2/proof['aa']+eps4*L1_box(P[58],lo,hi);assert perturbed<0
  for w in nb[v]:
   if w!=62:assert dot(sub(P[v],c),sub(P[w],P[v]))+eps4*sum(map(abs,sub(P[w],P[v])))<0
  rv=dot(sub(P[v],c),sub(P[v],c));assert r6-rv-2*eps4*sum(map(abs,sub(P[6],P[v])))>0
  extra[v]={'fixed_center_q58_bound':str(proof['upper']),'relaxed_q58_upper':str(perturbed)}
 print('L18_EXACT_ENUMERATED_HULL_PASS',len(nb),len(edges),len(faces))
 print('L18_ROOTPAIR_CUBE_EXACT_PASS',str(eps))
 print('L18_ROOT62_LOSS_FOUR_U_CUBE_EXACT_PASS',str(eps4))
 return {'centroid':list(map(str,c)),'parent_census':parent,'sources':sources,'box':{'lower':list(map(str,lo)),'upper':list(map(str,hi))},'two_root_cube_halfwidth':str(eps),'four_root_loss_cube_halfwidth':str(eps4),'local_stars':{str(i):nb[i] for i in (58,59,62,64)},'ball_upper_bounds':{str(w):str(b['upper']) for w,b in balls.items()},'cube_thresholds':{name:str(t) for name,t in thresholds},'four_root_bounds':extra,'scope':'Retain the named local support faces and stars, anchors fixed,62 arbitrary. Other geometry may vary; bounds concern the actual homogeneous centroid. Not a global exclusion of changed-support descendants.'}

def full_bars(x,edges):
 # Exact superlevel 0-dimensional persistence; retain every positive bar.
 from itertools import groupby
 from collections import deque
 edges=sorted({tuple(sorted(e)) for e in edges});birth=[dot(v,v) for v in x]
 def gate(u,v):
  a=dot(u,u);b=dot(u,v);c=dot(v,v);d=a+c-2*b
  if not d or b>=a:return a
  if b>=c:return c
  return (a*c-b*b)/d
 weight={e:gate(x[e[0]],x[e[1]]) for e in edges};par=list(range(len(x)));peak=par.copy();members=[{i} for i in par];out=[]
 def find(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 def path(s,t,level):
  adj=[[] for v in x]
  for i,j in edges:
   if weight[i,j]>=level:adj[i].append(j);adj[j].append(i)
  prev={s:None};todo=deque([s])
  while todo and t not in prev:
   i=todo.popleft()
   for j in sorted(adj[i]):
    if j not in prev:prev[j]=i;todo.append(j)
  assert t in prev
  result=[]
  while t is not None:result.append(t);t=prev[t]
  return result[::-1]
 for level,ee in groupby(sorted(edges,key=lambda e:(-weight[e],e)),key=lambda e:weight[e]):
  adj=defaultdict(set)
  for i,j in ee:
   a,b=find(i),find(j)
   if a!=b:adj[a].add(b);adj[b].add(a)
  unseen=set(adj)
  while unseen:
   a=min(unseen);unseen.remove(a);group={a};todo=[a]
   while todo:
    u=todo.pop()
    for v in adj[u]:
     if v in unseen:unseen.remove(v);group.add(v);todo.append(v)
   elder=max(group,key=lambda a:(birth[peak[a]],-peak[a]))
   for a in sorted(group):
    if a==elder or birth[peak[a]]==level:continue
    assert birth[peak[a]]>level;comp=members[a];cut=[e for e in edges if (e[0] in comp)!=(e[1] in comp)];assert max(weight[e] for e in cut)==level
    pp=path(peak[a],peak[elder],level);assert min(weight[tuple(sorted(e))] for e in zip(pp,pp[1:]))==level
    out.append({'peak':peak[a],'elder':peak[elder],'birth':birth[peak[a]],'death':level,'depth':(birth[peak[a]]-level)/birth[peak[a]],'component':sorted(comp),'cut':cut,'attaining_edge':next(e for e in cut if weight[e]==level),'attaining_path':pp})
   merged=set().union(*(members[a] for a in group))
   for a in group:par[a]=elder
   members[elder]=merged
 assert len({find(i) for i in range(len(x))})==1
 return sorted(out,key=lambda b:(-b['depth'],b['peak'],b['elder']))
def turnover(data):
 original=exact_hull(data);g0=original[-1];new={'denominator':data['denominator'],'points':[list(v) for v in data['points']],'cap':data['cap']}
 assert new['denominator']==100000000;new['points'][62]=[49100000,-34900000,-69800000]
 p,D,P,faces,edges,nb,c=exact_hull(new);assert {tuple(f) for f in faces}=={tuple(f) for f in original[3]}
 assert max(abs(a-b) for a,b in zip(c,g0))<F(1,1000)
 audit=census(P,faces,edges,c);assert audit['strict']==[3,4,5] and audit['additional_weak']==audit['primitive_zero']==[0,0,0];assert set(audit['roots'])=={6,58,59,64}
 x=[sub(v,c) for v in P];q=[]
 for f in faces:
  n=cross(sub(x[f[1]],x[f[0]]),sub(x[f[2]],x[f[0]]));h=dot(n,x[f[0]]);assert h>0;q.append(tuple(v/h for v in n))
 PB=full_bars(x,edges);QB=full_bars(q,edges.values());assert len(PB)==3 and len(QB)==2
 print('L18_ROOT_TURNOVER_G3_EXACT_PASS',audit['strict'],[float(b['depth']) for b in PB],[float(b['depth']) for b in QB])
 return {'name':'L18_ROOT_TURNOVER_G3','replacement':{'label':62,'integer_point':new['points'][62],'denominator':D},'counts':[len(nb),len(edges),len(faces)],'centroid':list(map(str,c)),'audit':audit,'P':PB,'Q':QB,'status':'Exact useful nonrecord, not own110; only vertex62 moved, all original maximal facets retained.'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input',default='l18_exact_points.json');ap.add_argument('--out',default='rootpair_exact.json');a=ap.parse_args();data=json.loads(Path(a.input).read_text());r=verify(data);r['turnover']=turnover(data);Path(a.out).write_text(json.dumps(r,sort_keys=True,separators=(',',':'),default=str)+'\n')
if __name__=='__main__':main()
```
