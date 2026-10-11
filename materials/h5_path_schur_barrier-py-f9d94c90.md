# material-f9d94c90a9b7

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact H5 optimized-single-cut Schur barrier and three-arrow prism.
Python >= 3.11, standard library, assertions enabled. No external input files.
Optional --locate requires NumPy 2.3.5 / SciPy 1.17.0; discovery only.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, lcm
from pathlib import Path
import argparse, hashlib, json, sys

TITLE='H5_OPTIMIZED_SINGLE_PATH_SCHUR_BARRIER_AND_THREE_ARROW_PRISM_V1'
PARENT='f31e0f04d48f1b80f427df0b3ac4342cd2b61e84f1edaaf280330521e356cce1'
METHOD='6dc7106cabaa16510d7f067ac60cff45a53c08dd55482a97025aa011b8ad4866'
ZERO=(0,)*5
PAIRS=tuple((i,j)for i in range(3)for j in range(i,3))
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
       (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
FAN=((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),
     (0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9))
EDGES=tuple(sorted({tuple(sorted((a,b)))for f in FACES for a,b in zip(f,f[1:]+f[:1])}))
TREE=((0,1),(1,2),(3,2),(4,3),(5,6),(6,0),(7,0),(8,2),(9,3))
WEIGHTS=((1,2,2),(5,6,5),(7,0,2))
POINT=tuple(map(F,('31/32','3/8','3/8','3/8','1/32')))
OMEGA=tuple((t-F(1,256),t+F(1,256))for t in POINT)
PRISM=tuple(tuple(map(F,pair))for pair in(('15/16','1'),('1/4','1/2'),('5/16','7/16'),('5/16','7/16'),('0','1/16')))
GAP=F(1,2048)

class P:
 def __init__(self,x=0):
  if isinstance(x,P):self.d=x.d.copy()
  elif isinstance(x,dict):self.d={k:F(v)for k,v in x.items()if v}
  else:self.d={}if not x else {ZERO:F(x)}
 def __add__(self,b):
  d=self.d.copy()
  for k,v in P(b).d.items():d[k]=d.get(k,F(0))+v
  return P(d)
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.d.items()})
 def __sub__(self,b):return self+-P(b)
 def __rsub__(self,b):return P(b)+-self
 def __mul__(self,b):
  d={}
  for k,v in self.d.items():
   for j,w in P(b).d.items():
    z=tuple(a+c for a,c in zip(k,j));d[z]=d.get(z,F(0))+v*w
  return P(d)
 __rmul__=__mul__
 def __truediv__(self,b):return self*(1/F(b))
 def __pow__(self,n):
  z=P(1)
  for _ in range(n):z=z*self
  return z
 def __eq__(self,b):return self.d==P(b).d

def var(i):
 k=[0]*5;k[i]=1
 return P({tuple(k):1})
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(*vs):return tuple(map(sum,zip(*vs)))
def mul(c,v):return tuple(c*x for x in v)
def sub(a,b):return add(a,mul(-1,b))
def outer(v):return tuple(v[i]*v[j]for i,j in PAIRS)
def sym(v,w):return tuple((v[i]*w[j]+v[j]*w[i])/2 for i,j in PAIRS)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def minors(row):
 a,b,c,d,e,f=row
 return a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b

def geometry(pt):
 x,r,p,q,l=pt;s=1-l
 B=((F(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),
    (0,1-3*r/4),(0,F(1,4)),(F(1,16),F(1,16)))
 z=tuple((s*a,s*b,0)for a,b in B)+((0,0,1),(l,0,1),(0,l,1))
 A=(31-24*x*p-24*r*q)/64
 bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
 by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
 V=A*s*s/3+l/6
 J=(s**3*bx/4+s*s*l*(1-3*x*p/4)/24+l*l/24,
    s**3*by/4+s*s*l*(1-3*r*q/4)/24+l*l/24,
    A*s*s/12+l/12+l*l/24)
 return z,V,J

def component(a):
 D={a:0}
 while True:
  new={i:D[j]+1 for i,j in TREE if j in D and i not in D}
  if not new:return tuple(sorted(D.items()))
  D.update(new)

def interval(i,n,k,lo,hi):
 return sum(F(comb(k,j)*comb(i,j),comb(n,j))*lo**(k-j)*(hi-lo)**j for j in range(min(i,k)+1))

def rectangular(polys,box):
 polys=tuple(map(P,polys));keys={k for p in polys for k in p.d}
 if not keys:return [[0]*len(polys)],1,ZERO
 deg=tuple(max(k[i]for k in keys)for i in range(5))
 ids=tuple(product(*(range(d+1)for d in deg)));loc={k:i for i,k in enumerate(ids)}
 den=lcm(*(c.denominator for p in polys for c in p.d.values()))
 data=[[int(p.d.get(k,F(0))*den)for p in polys]for k in ids]
 for ax,n in enumerate(deg):
  T=[[interval(i,n,k,*box[ax])for k in range(n+1)]for i in range(n+1)]
  dt=lcm(*(v.denominator for row in T for v in row));T=[[int(v*dt)for v in row]for row in T]
  new=[[0]*len(polys)for _ in ids]
  others=product(*(range(d+1)if a!=ax else (0,)for a,d in enumerate(deg)))
  for idx in others:
   pos=[loc[idx[:ax]+(k,)+idx[ax+1:]]for k in range(n+1)]
   for i in range(n+1):
    new[pos[i]]=[sum(T[i][k]*data[pos[k]][j]for k in range(n+1))for j in range(len(polys))]
  data=new;den*=dt
 return data,den,deg

def integer_matrix(row):
 den=lcm(*(F(x).denominator for x in row));n=[int(x*den)for x in row]
 return {'denominator':den,'upper_numerators':n,'leading_numerators':minors(n)}

def exact_shadows(pt):
 """Return numerator N and positive denominator L for each candidate n=N/L."""
 z,V,J=geometry(pt);U=tuple(sub(mul(V,a),J)for a in z);x,r,p,q,l=pt
 Nh=(p,-(1-p-(1-3*x/4)),0)
 N3=sub(sub(mul(V,cross(z[4],z[9])),cross(z[4],J)),cross(J,z[9]))
 L3=dot(N3,sub(z[3],z[4]))
 return {0:((0,-V,0),J[1]),1:(mul(V,Nh),dot(Nh,U[1])),3:(N3,L3)}

def shadow_guards(pt):
 z,V,J=geometry(pt);U=tuple(sub(mul(V,a),J)for a in z)
 shadows=exact_shadows(pt);guards=[];identities=[];labels=[]
 parent=dict(TREE)
 for a,(N,L)in shadows.items():
  guards.append(P(L));labels.append((a,'denominator'))
  own=dot(N,U[a])-V*L
  assert own==0;identities.append((a,'source_normalization'))
  expr=dot(N,sub(z[parent[a]],z[a]))
  if expr==0:identities.append((a,'parent'))
  else:guards.append(P(expr));labels.append((a,'parent'))
  for i,d in component(a):
   sigma=F(d-1,d+1)
   for name,expr in (('upper',V*L-dot(N,U[i])),('lower',dot(N,U[i])+sigma*V*L)):
    if expr==0:identities.append((a,i,name))
    else:guards.append(P(expr));labels.append((a,i,name))
 return guards,labels,identities,shadows

def all_extensions():
 fixed={a:b for a,b,_ in WEIGHTS};adj={i:tuple(b if a==i else a for a,b in EDGES if i in(a,b))for i in range(10)}
 ans=[]
 for root in range(10):
  if root in fixed:continue
  missing=[i for i in range(10)if i!=root and i not in fixed]
  for targets in product(*(adj[i]for i in missing)):
   parent=dict(fixed);parent.update(zip(missing,targets));ok=True
   for i in range(10):
    j=i;seen=set()
    while j!=root:
     if j in seen:ok=False;break
     seen.add(j);j=parent[j]
    if not ok:break
   if ok:ans.append((root,tuple(sorted(parent.items()))))
 assert (2,TREE)in ans
 return ans

def point_fidelity(z,V,J):
 vf=F(0);jf=(F(0),)*3;volumes=[]
 for ids in FAN:
  a,b,c,d=(z[i]for i in ids);dv=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6
  assert dv>0;volumes.append(dv);vf+=dv;jf=add(jf,mul(dv/4,add(*(z[i]for i in ids))))
 assert vf==V and jf==J
 g=mul(1/V,J);slacks=[]
 for face in FACES:
  a,b,c=(z[i]for i in face[:3]);N=cross(sub(b,a),sub(c,a));h=dot(N,a)
  if dot(N,g)>h:N=mul(-1,N);h=-h
  assert h-dot(N,g)>0
  for i in range(10):
   t=h-dot(N,z[i]);assert t==0 if i in face else t>0
   if i not in face:slacks.append(t)
 assert len(slacks)==56
 return {'fan_volumes':volumes,'strict_support_count':56,'minimum_support_slack':min(slacks)}

def clean(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):clean(v)for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [clean(v)for v in x]
 return x

def save(path,data):
 raw=(json.dumps(clean(data),sort_keys=True,separators=(',',':'))+'\n').encode()
 path.write_bytes(raw)
 return {'filename':path.name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

def locate():
 """Optional deterministic discovery, not a numerical proof or required recovery."""
 import numpy as np
 import scipy
 from scipy.optimize import linprog
 z,V,J=geometry(POINT);U=np.array([sub(a,mul(1/V,J))for a in z],float)
 items=((0,1),(1,2),(5,6),(6,0),(7,0))
 mats=np.array([-(np.outer(U[a],U[b]-U[a])+np.outer(U[b]-U[a],U[a]))/2 for a,b in items])
 directions=[np.eye(3)[i]for i in range(3)]
 directions += [np.array(t)/np.linalg.norm(t)for t in product((-1,0,1),repeat=3)if any(t)]
 rows=[np.r_[-np.einsum('i,kij,j->k',v,mats,v),1.]for v in directions]
 for iteration in range(300):
  sol=linprog(np.r_[np.zeros(5),-1.],A_ub=np.array(rows),b_ub=np.zeros(len(rows)),
    A_eq=np.array([np.r_[np.ones(5),0.]]),b_eq=[1.],bounds=[(0,None)]*5+[(None,None)],method='highs')
  if not sol.success:raise RuntimeError(sol.message)
  C=np.einsum('k,kij->ij',sol.x[:-1],mats);ev,evec=np.linalg.eigh(C)
  if ev[0]>1e-8:break
  v=evec[:,0];rows.append(np.r_[-np.einsum('i,kij,j->k',v,mats,v),1.])
 else:raise RuntimeError('Optional locator did not find a strict point stress.')
 assert [i for i,w in enumerate(sol.x[:-1])if w>1e-8]==[1,2,4]
 # The literal small integer candidate (2,5,2) is accepted only by exact main().
 print('H5_THREE_ARROW_OPTIONAL_LOCATION_PASS',np.__version__,scipy.__version__,iteration,flush=True)


def main(out):
 if not __debug__:raise RuntimeError('Assertions required; do not use -O.')
 out.mkdir(parents=True,exist_ok=True)
 assert len(EDGES)==17
 pt=tuple(var(i)for i in range(5));z,V,J=geometry(pt)
 vf=P(0);jf=(P(0),)*3
 for ids in FAN:
  a,b,c,d=(z[i]for i in ids);dv=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6
  vf+=dv;jf=add(jf,mul(dv/4,add(*(z[i]for i in ids))))
 assert vf==V and all(x==y for x,y in zip(jf,J))
 C=add(*(mul(-w,sym(sub(mul(V,z[a]),J),sub(z[b],z[a])))for a,b,w in WEIGHTS))
 shifted=[v-(GAP if a==b else 0)for v,(a,b)in zip(C,PAIRS)]
 rows,den,degrees=rectangular(shifted,PRISM)
 minimum=None
 for row in rows:
  mm=minors(row)
  assert min(mm)>0,('stress coefficient',degrees,mm)
  minimum=mm if minimum is None else tuple(min(a,b)for a,b in zip(minimum,mm))
 matrix_pin=save(out/'h5_three_arrow_matrices.json',{'domain':PRISM,'weights':WEIGHTS,'gap_in_VC':GAP,'degrees':degrees,'denominator':den,'upper_numerators':rows})
 guards,labels,identities,shadows=shadow_guards(pt)
 srows,sden,sdegrees=rectangular(guards,OMEGA)
 assert min(v for row in srows for v in row)>0,('shadow guard failure',sdegrees)
 shadow_pin=save(out/'h5_schur_barrier_guards.json',{'box':OMEGA,'labels':labels,'identities':identities,'degrees':sdegrees,'denominator':sden,'numerators':srows})
 small=[(a,b,component(a))for a,b in TREE if a not in shadows]
 assert all(len(d)<3 for _,_,d in small)
 pz,pV,pJ=geometry(POINT);pg=mul(1/pV,pJ);pu=tuple(sub(v,pg)for v in pz)
 fidelity=point_fidelity(pz,pV,pJ)
 pn=exact_shadows(POINT);cert=[]
 for a,(N,L)in pn.items():
  assert L>0
  n=mul(1/L,N);assert dot(n,pu[a])==1
  b=dict(TREE)[a];assert dot(n,sub(pu[b],pu[a]))>=0
  vals=[]
  for i,d in component(a):
   v=dot(n,pu[i]);sigma=F(d-1,d+1);assert -sigma<=v<=1
   vals.append((i,d,v))
  cert.append({'edge':(a,b),'normal':n,'descendant_values':vals,'parent_value':dot(n,pu[b])})
 pc=add(*(mul(-w,sym(pu[a],sub(pu[b],pu[a])))for a,b,w in WEIGHTS))
 assert min(minors(pc))>0
 assert all(PRISM[i][0]<=OMEGA[i][0]<OMEGA[i][1]<=PRISM[i][1]for i in range(5))
 assert OMEGA[4][0]>F(1,64)and OMEGA[2][1]<F(9,16)and OMEGA[3][1]<F(9,16)
 assert OMEGA[2][0]+OMEGA[3][0]>F(1,2)and OMEGA[2][1]+OMEGA[3][1]<1
 extensions=all_extensions();counts=[sum(root==i for root,_ in extensions)for i in range(10)]
 report={'title':TITLE,'parent_sha256':PARENT,'method_sha256':METHOD,'facets':FACES,'edges':EDGES,'fan':FAN,'tree':TREE,'weights':WEIGHTS,'weight_sum':sum(w for _,_,w in WEIGHTS),
 'moment_identities':4,'prism':PRISM,'gap_in_VC':GAP,'stress_degrees':degrees,'stress_blocks':len(rows),'stress_minors':3*len(rows),
 'minimum_shifted_leading_minors':[F(v,den**(i+1))for i,v in enumerate(minimum)],'mean_arrow_gap':F(6)*GAP/sum(w for _,_,w in WEIGHTS),
 'schur_barrier_box':OMEGA,'shadow_guard_count':len(guards),'shadow_coefficient_count':len(srows)*len(guards),'shadow_degrees':sdegrees,
 'shadow_identity_count':len(identities),'minimum_shadow_coefficient':F(min(v for row in srows for v in row),sden),
 'small_components':small,'point':{'parameters':POINT,'vertices':pz,'volume':pV,'first_moment':pJ,'centroid':pg,'fidelity':fidelity,'all_full_rank_cut_shadows':cert,'stress_C':integer_matrix(pc)},
 'extensions':extensions,'root_counts':counts,'extension_total':len(extensions),'matrix_file':matrix_pin,'shadow_file':shadow_pin,
 'scope':'All nine individual optimized G-r*r^T sufficient tests fail on Omega, not every full path stress or a general arrow SDP. Three-arrow stress excludes its complete extensions on the stated prism, not all roots or a global complexity layer.'}
 pin=save(out/'h5_path_schur_barrier_report.json',report)
 print('H5_PATH_SCHUR_ACTUAL_FAN_IDENTITIES_PASS',4)
 print('H5_THREE_ARROW_RESIDUAL_PRISM_PASS',len(rows),3*len(rows),len(extensions))
 print('H5_ALL_NINE_OPTIMIZED_SINGLE_PATH_SCHUR_TESTS_FAIL_PASS',len(shadows),len(small),len(guards),len(srows)*len(guards),len(identities))
 print('H5_OPTIMIZED_SINGLE_PATH_SCHUR_BARRIER_AND_THREE_ARROW_PRISM_PASS')
 print(json.dumps({'report':pin,'matrices':matrix_pin,'guards':shadow_pin},sort_keys=True))

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('out',type=Path,nargs='?',default=Path('output'));ap.add_argument('--locate',action='store_true');args=ap.parse_args()
 if args.locate:locate()
 main(args.out)
