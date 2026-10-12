# material-09aa70ca0b47

AI research material

---

# FULL76 exact readable source, part 8/8
# Each FILE header gives the exact following UTF-8 byte count and SHA-256.
# The newline after each payload is a framing separator, not a source byte.

FILE methods/parent/check_B.py 6351 b0cb62d5486b32d020b60f717f3dfe9d07c6c9a978492928f54c3a38f396fc24
from fractions import Fraction as Q
from itertools import combinations
from math import lcm
import sys,json
sys.set_int_max_str_digits(0)
ZERO=(0,0,0)
def plus(a,b):return (a[0]+b[0],a[1]+b[1],a[2]+b[2])
def minus(a,b):return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def times(a,s):return tuple(x*s for x in a)
def inner(a,b):return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def outer(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def determinant(a,b,c):return inner(a,outer(b,c))
def sg(x):return 1 if x>0 else -1 if x<0 else 0
def encode(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x

def run(raw):
 rows=[tuple(map(int,r)) for r in raw['H']];assert len(rows)>=4 and all(len(r)==4 and r[-1]>0 for r in rows);assert len(set(rows))==len(rows)
 normals=[r[:3] for r in rows];hs=[r[-1] for r in rows];points=set();lineedges=set()
 for a,b in combinations(range(len(rows)),2):
  n,m=normals[a],normals[b];d=outer(n,m);dd=inner(d,d)
  if not dd:continue
  p=plus(times(outer(m,d),hs[a]),times(outer(d,n),hs[b]));low=None;high=None;empty=False
  for nn,hh in zip(normals,hs):
   coeff=inner(nn,d);rhs=hh*dd-inner(nn,p)
   if coeff>0:
    t=Q(rhs,coeff);high=t if high is None or t<high else high
   elif coeff<0:
    t=Q(rhs,coeff);low=t if low is None or t>low else low
   elif rhs<0:empty=True;break
   if low is not None and high is not None and low>high:empty=True;break
  if empty:continue
  # An unbounded supporting line would be an unbounded edge/ray.
  assert low is not None and high is not None
  x=times(plus(p,times(d,low)),Q(1,dd));y=times(plus(p,times(d,high)),Q(1,dd));points.add(x);points.add(y)
  if low<high:lineedges.add(tuple(sorted((x,y))))
 X=sorted(points);assert len(X)>=4;index={p:i for i,p in enumerate(X)};pair_edges={tuple(sorted((index[x],index[y]))) for x,y in lineedges};faces=[];active=[]
 for fi,(normal,offset) in enumerate(zip(normals,hs)):
  ids=[i for i,p in enumerate(X) if inner(normal,p)==offset]
  if len(ids)<3:continue
  succ={}
  for a,b in combinations(ids,2):
   e=minus(X[b],X[a]);ee=inner(e,e);values={i:inner(normal,outer(e,minus(X[i],X[a]))) for i in ids};zero=[i for i in ids if values[i]==0];projections=[inner(e,minus(X[i],X[a])) for i in zero]
   if min(projections)<0 or max(projections)>ee:continue
   if min(values.values())>=0 and max(values.values())>0:succ[a]=b
   elif max(values.values())<=0 and min(values.values())<0:succ[b]=a
  if not succ:continue
  assert len(succ)>=3 and set(succ)==set(succ.values());start=min(succ);cycle=[start];b=succ[start]
  while b!=start:assert b not in cycle;cycle.append(b);b=succ[b]
  assert len(cycle)==len(succ)==len(ids);faces.append(cycle);active.append(fi)
 nrm=[normals[i] for i in active];off=[hs[i] for i in active];edges={};triangles=[];adj=[set() for _ in X]
 for fi,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append((fi,i,j));adj[i].add(j);adj[j].add(i)
  triangles.extend((cy[-1],cy[j],cy[j+1]) for j in range(len(cy)-2))
 assert set(edges)==pair_edges;assert len(X)-len(edges)+len(faces)==2;assert all(len(v)==2 and v[0][1:]==v[1][1:][::-1] for v in edges.values())
 visited=set();queue=[0]
 while queue:
  i=queue.pop()
  if i not in visited:visited.add(i);queue.extend(adj[i]-visited)
 assert len(visited)==len(X)
 rho=min(Q(h,100*(1+sum(map(abs,n)))) for n,h in zip(normals,hs));base=(rho,2*rho,3*rho);assert all(inner(n,base)<h for n,h in zip(normals,hs));Z=[minus(x,base) for x in X];volume=Q(0);localmoment=ZERO
 for a,b,c in triangles:
  v=determinant(Z[a],Z[b],Z[c])/6;assert v>0;volume+=v;localmoment=plus(localmoment,times(plus(plus(Z[a],Z[b]),Z[c]),v/4))
 centre=plus(base,times(localmoment,1/volume));moment=times(centre,volume);assert minus(moment,times(centre,volume))==ZERO
 C=lcm(*(v.denominator for v in centre));M=tuple(int(C*v) for v in centre);bs=[lcm(*(v.denominator for v in p)) for p in X];aa=[tuple(int(b*v) for v in p) for p,b in zip(X,bs)];zz=[minus(times(a,C),times(M,b)) for a,b in zip(aa,bs)]
 def edge(i,j):return minus(times(aa[j],bs[i]),times(aa[i],bs[j]))
 SF=[];SW=[];UV=[];UW=[];EH=[];EW=[];fs=[];vs=[];es=[];fz=0;ez=0
 for fi,cy in enumerate(faces):
  n=nrm[fi];hc=off[fi]*C-inner(n,M);nn=inner(n,n);assert hc>0;vals=[]
  for i,j in zip(cy,cy[1:]+cy[:1]):
   p=minus(times(n,bs[i]*hc),times(zz[i],nn));vals.append(inner(n,outer(edge(i,j),p)))
  signs=[sg(v) for v in vals];fs.append(signs);fz+=signs.count(0)
  if min(signs)>0:SF.append(fi)
  elif min(signs)>=0:SW.append(fi)
 for i in range(len(X)):
  largest=max(inner(zz[i],edge(i,j)) for j in adj[i]);classification=sg(largest)
  if classification<0:UV.append(i)
  elif classification==0:UW.append(i)
  best=None;jbest=None
  for j in range(len(X)):
   if j==i:continue
   value=inner(zz[i],edge(i,j))
   if best is None or value*bs[jbest]>=best*bs[j]:best=value;jbest=j
  assert sg(best)==classification;vs.append([jbest,sg(best)])
 for (i,j),pair in sorted(edges.items()):
  e=edge(i,j);ee=inner(e,e);ze=inner(zz[i],e);p=minus(times(zz[i],ee),times(e,ze));n,m=[nrm[v[0]] for v in pair];d=outer(n,m);assert inner(d,d)>0
  vals=[-ze*bs[j],C*ee+ze*bs[j],inner(outer(p,m),d),inner(outer(n,p),d)];signs=[sg(v) for v in vals];es.append([i,j,*signs]);ez+=signs.count(0)
  if min(signs)>0:EH.append([i,j])
  elif min(signs)>=0:EW.append([i,j])
 return encode(dict(V=len(X),E=len(edges),F=len(faces),active_input_indices=active,raw_vertices=X,faces=faces,edges=sorted(edges),normals=nrm,offsets=off,ordinary_volume=volume,raw_first_moments=moment,raw_centroid=centre,centred_first_moments=ZERO,centred_centroid=ZERO,counts=[len(SF),len(UV),len(EH)],weak=[len(SW),len(UW),len(EW)],stable_face_ids=SF,unstable_vertices=UV,saddle_edges=EH,weak_faces=SW,weak_vertices=UW,weak_edges=EW,face_signs=fs,vertex_max_escape_signs=vs,edge_signs=es,face_primitive_zero_count=fz,vertex_max_zero_count=len(UW),edge_primitive_zero_count=ez,edge_primitive_count=4*len(edges),integration_triangle_count=len(triangles)))
if __name__=='__main__':
 from pathlib import Path
 raw=json.loads(Path(sys.argv[1]).read_text());out=run(raw);Path(sys.argv[2]).write_text(json.dumps(out,sort_keys=True,separators=(',',':')));print('B',out['V'],out['E'],out['F'],out['counts'],out['weak'],flush=True)

END FILE methods/parent/check_B.py

FILE methods/qp.py 2412 da8c3f00ac7df51676d6a9c9de13c01b0f0f800519eaaf08de23a677371f55c0
"""Small dense infeasible-start primal-dual predictor-corrector convex QP.
This numerical proposal solver does not participate in exact acceptance.
"""
import numpy as np
import scipy.linalg as la

def solve(A,lo,hi,lb,ub,cost,maxiter=80,tol=1e-8):
 n=len(lb);eye=np.eye(n);A=np.vstack((A,eye));lo=np.r_[lo,lb];hi=np.r_[hi,ub]
 eq=np.isfinite(hi)&(lo==hi);il=np.isfinite(lo)&~eq;ih=np.isfinite(hi)&~eq
 E=A[eq];b=lo[eq];G=np.vstack((-A[il],A[ih]));h=np.r_[-lo[il],hi[ih]]
 scale=np.maximum(1.,np.linalg.norm(G,axis=1));G=G/scale[:,None];h=h/scale
 scale=np.maximum(1.,np.linalg.norm(E,axis=1));E=E/scale[:,None];b=b/scale
 p=cost**2;m=len(h);x=np.zeros(n);y=np.zeros(len(b));s=np.maximum(1.,h-G@x);z=np.ones(m)
 def maxstep(v,d):
  t=d<0
  return min(1.,float(np.min(-v[t]/d[t]))) if np.any(t) else 1.
 for it in range(maxiter):
  rd=p*x+G.T@z+E.T@y;rp=G@x+s-h;re=E@x-b;mu=float(s@z/m)
  primal=max(np.max(np.abs(rp)),np.max(np.abs(re)) if len(re) else 0.)
  dual=np.max(np.abs(rd));err=max(primal,dual,mu)
  if primal<tol and mu<tol:
   v=A@x
   if max(np.max(lo-v),np.max(v-hi))<1e-6:return x,None
  if not np.isfinite(err) or mu>1e20:return None,'QP diverged'
  D=z/s;K=np.diag(p)+(G.T*D)@G
  try:
   cho=la.cho_factor(K,lower=True,check_finite=False);KE=la.cho_solve(cho,E.T,check_finite=False);Schur=E@KE
   def direction(rc):
    rhs=-rd+G.T@(rc/s-D*rp);u=la.cho_solve(cho,rhs,check_finite=False)
    dy=la.solve(Schur,E@u+re,assume_a='sym',check_finite=False) if len(b) else np.zeros(0)
    dx=u-KE@dy;ds=-rp-G@dx;dz=(-rc-z*ds)/s
    return dx,dy,ds,dz
   dx,dy,ds,dz=direction(s*z);ap=maxstep(s,ds);ad=maxstep(z,dz)
   muaff=float((s+ap*ds)@(z+ad*dz)/m);sigma=min(1.,max(0.,(muaff/mu)**3))
   dx,dy,ds,dz=direction(s*z+ds*dz-sigma*mu)
   ap=min(1.,.995*maxstep(s,ds));ad=min(1.,.995*maxstep(z,dz))
   x+=ap*dx;s+=ap*ds;y+=ad*dy;z+=ad*dz
  except (la.LinAlgError,ValueError,FloatingPointError) as ex:return None,f'QP numerical factorization it={it} error={err:g} primal={primal:g} dual={dual:g} mu={mu:g}: {ex}'
  if min(s.min(),z.min())<=0:return None,'QP lost interior'
 return None,f'QP iteration limit error={err:g} primal={primal:g} dual={dual:g} mu={mu:g}'

if __name__=='__main__':
 A=np.array([[1.,1.]]);lo=np.array([1.]);hi=np.array([np.inf]);lb=np.array([0.,0.]);ub=np.array([2.,2.]);x,e=solve(A,lo,hi,lb,ub,np.array([1.,2.]));assert e is None and np.max(abs(x-[.8,.2]))<1e-7;print('QP_TEST',x)

END FILE methods/qp.py

FILE methods/union_atlas.py 4054 6d2a6d5bbf19734dc649fb269c83a6231f5adf00ed3242a795309d26b2da486b
"""General triangular-panel union with an unused support's previous contacts retained."""
from contact import *
from fractions import Fraction as F
class UnionAtlas(Atlas):
 def __init__(self,G,rep,pair,Qinit,S=3):
  self.G=G=copy.deepcopy(G);self.parents=rep;self.forcedp={};self.forcedq={};self.nq=G['n_supports'];self.S=S
  root=next(v for v,r in enumerate(rep['raw_vertices']) if list(map(F,r))==[0,0,1]);owners=[[rep['active_input_indices'][f] for f,cy in enumerate(rep['faces']) if v in cy] for v in range(rep['V'])];assert rep['active_input_indices']==list(range(self.nq))
  ends=[i for i,o in enumerate(owners) if all(q in o for q in pair)];assert len(ends)==2 and all(len(owners[i])==3 for i in ends) and root not in ends
  gone,keep=sorted(ends);union=sorted(set(owners[gone]+owners[keep]));assert len(union)==4
  plan={i:(deps,axes) for i,deps,axes in G['plan']};used={d for _,deps,_ in G['plan'] for d in deps};eligible=[i for i in pair if len(plan[i][0])<3 and i not in used];assert eligible,'Needs rechart: no unused support with free coordinate'
  def pt(ids):
   tri=max(itertools.combinations(ids,3),key=lambda a:abs(np.linalg.det(Qinit[list(a)])))
   return np.linalg.solve(Qinit[list(tri)],np.ones(3))
  shift=np.array([0.,0.,1.])-pt(G['groups'][0]);Qinit=Qinit/(1+Qinit@shift)[:,None];x=pt(union);Y=np.vstack((Qinit,[pt(g) for g in G['groups']]));new=len(G['controls'])
  choices=[]
  for i in eligible:
   tri=[q for q in union if q!=i];xx=pt(tri);rows=np.vstack((Y[plan[i][0]],xx))
   for aa in itertools.combinations(range(3),len(rows)):
    determinant=abs(np.linalg.det(rows[:,aa]));score=abs(np.linalg.det(Qinit[tri]))*determinant
    choices.append((score,i,list(aa),xx))
  score,chosen,axes,x=max(choices,key=lambda c:c[0]);assert score>0;deps=plan[chosen][0]+[new]
  G['controls'].append(np.rint(x*G['grid']).astype(np.int64).tolist());G['groups'].append(union);G['plan']=[r for r in G['plan'] if r[0]!=chosen]+[[new,[q for q in union if q!=chosen],[0,1,2]],[chosen,deps,axes]]
  self.patch=dict(pair=list(pair),gone=gone,keep=keep,union=union,new_node=new,solved_support=chosen,old_solve=list(plan[chosen]),deps=deps,axes=axes)
  axmap={i:ax for i,dd,ax in G['plan']};self.free=[(i,k) for i in range(len(G['controls'])) if i!=self.nq for k in range(3) if k not in axmap[i]];self.n=len(self.free);self.base=np.array([G['controls'][i][a]/G['grid'] for i,a in self.free]);self.scale=np.ones(self.n)
  old=[i for i in range(rep['V']) if i!=gone];mapping={v:i for i,v in enumerate(old)};mapping[gone]=mapping[keep];owners[keep]=union;self.owners=[owners[i] for i in old];self.oldids=old;self.U=mapping[root];self.nv=len(old);self.mechlen=self.nv+self.nq;self.merged=mapping[keep]
  faces=[]
  for cy in rep['faces']:
   cc=[mapping[i] for i in cy];out=[]
   for v in cc:
    if not out or v!=out[-1]:out.append(v)
   if out[0]==out[-1]:out.pop()
   assert len(set(out))==len(out) and len(out)>=3,'Requires true polar vertex suppression';faces.append(out)
  self.faces=faces;self.tris=np.array([(cy[0],cy[k],cy[k+1]) for cy in faces for k in range(1,len(cy)-1)])
  groups={frozenset(g):self.nq+k for k,g in enumerate(G['groups'])};self.direct=np.array([groups.get(frozenset(o),-1) for o in self.owners]);self.simple=np.where(self.direct<0)[0];assert all(len(self.owners[v])==3 for v in self.simple);self.trip=np.array([self.owners[v] for v in self.simple]);self.mask=np.ones((self.nq,self.nv),bool)
  for v,own in enumerate(self.owners):self.mask[own,v]=False
  self.keptp=np.array([i for i in range(self.nv) if i!=self.U]);self.keptq=np.array([i for i in range(self.nq) if i!=S]);self.last=None;self.tscale=np.ones(len(self.tris));install(self,Qinit)
  val,jac,geo=self.evaluate(np.zeros(self.n));self.floor=np.zeros(len(val));self.floor[:self.mechlen-2]=1e-7;self.floor[self.mechlen-2:self.mechlen]=1e-5;self.floor[self.mechlen:self.mechlen+self.nq]=1e-9;self.floor[self.mechlen+self.nq:-self.nq-1]=1e-6;self.floor[-self.nq-1:-1]=.001;self.floor[-1]=.02
  self.rescale=np.ones(len(val));self.rescale[:self.mechlen+self.nq]=1e-3

END FILE methods/union_atlas.py
