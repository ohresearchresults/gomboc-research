"""Exact two-cap images of two separately named multivertex truncations."""
import json,sys,math
from fractions import Fraction as Q
from pathlib import Path
sys.set_int_max_str_digits(0)
CASES={
 'PAIR99':dict(deleted_support=99,removed_vertices=[129,145],added_faces=[[124,149,146],[112,124,146]],dropped_faces=[],caps=[dict(vertices=[0,2],boundary=[1,3,10,95]),dict(vertices=[83,85,87,91,93,96,98,102,105,110,113],boundary=[79,90,95,116])]),
 'TRIPLE117':dict(deleted_support=117,removed_vertices=[77,78,81],added_faces=[[75,76,84],[71,75,84],[76,86,84]],dropped_faces=[55],caps=[dict(vertices=[0,2],boundary=[1,3,10,93]),dict(vertices=[82,83,85,89,91,94,96,100,103,108,111],boundary=[79,88,93,114])])}
SELECT=[(0,2),(1,0),(1,1)]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def inverse(A):
 n=len(A);M=[[Q(v) for v in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
 for k in range(n):
  i=next(i for i in range(k,n) if M[i][k]);M[k],M[i]=M[i],M[k];d=M[k][k];M[k]=[v/d for v in M[k]]
  for i in range(n):
   if i!=k:d=M[i][k];M[i]=[x-d*y for x,y in zip(M[i],M[k])]
 return [row[n:] for row in M]
def setup(base,case):
 spec=CASES[case];P=[tuple(map(Q,p)) for p in base['raw_vertices']];rm=set(spec['removed_vertices']);keep=[i for i in range(len(P)) if i not in rm];faces=[];labels=[];original=[i for i in range(137) if i!=spec['deleted_support']]
 for f,cy in enumerate(base['faces']):
  cy=[i for i in cy if i not in rm]
  if f in spec['dropped_faces']:
   assert len(cy)<3 or not any(cross(sub(P[cy[1]],P[cy[0]]),sub(P[cy[2]],P[cy[0]])))
   continue
  assert len(cy)>=3
  faces.append(cy);labels.append(original[base['active_input_indices'][f]])
 for k,cy in enumerate(spec['added_faces']):faces.append(cy);labels.append(case+'_CUT_'+str(k))
 beta={}
 for ci,cap in enumerate(spec['caps']):
  assert not rm&(set(cap['vertices'])|set(cap['boundary']))
  B=[[P[i][a] for i in cap['boundary']] for a in range(3)]+[[Q(1)]*4];Bi=inverse(B)
  for i in cap['vertices']:beta[ci,i]=tuple(dot(row,(*P[i],Q(1))) for row in Bi)
  cset=set(cap['vertices']);outside=set(keep)-cset-set(cap['boundary'])
  assert all(not (set(cy)&cset and set(cy)&outside) for cy in faces),'mixed facet'
 return P,keep,faces,labels,beta

def points(base,case,eta):
 P,keep,faces,labels,beta=setup(base,case);out=P.copy();denominators=[]
 for ci,cap in enumerate(CASES[case]['caps']):
  for i in cap['vertices']:
   den=Q(1);num=P[i]
   for k,(cc,j) in enumerate(SELECT):
    if cc==ci:
     v=eta[k]*beta[ci,i][j];den+=v;num=add(num,mul(v,P[cap['boundary'][j]]))
   assert den>0;denominators.append(den);out[i]=mul(1/den,num)
 assert all(1+e>0 for e in eta)
 return out,keep,faces,labels,denominators

def raw(base,case,eta):
 P,keep,faces,labels,den=points(base,case,eta);rows=[]
 for cy in faces:
  a,b,c=[P[i] for i in cy[:3]];n=cross(sub(b,a),sub(c,a));h=dot(n,a);assert h>0
  assert all(dot(n,P[i])==h for i in cy)
  assert all(dot(n,P[i])<h for i in keep if i not in cy),'bad support'
  d=math.lcm(*(x.denominator for x in (*n,h)));row=[int(d*x) for x in (*n,h)];g=math.gcd(*row);rows.append([x//g for x in row])
 assert len(set(map(tuple,rows)))==len(rows)
 return {'H':rows},dict(input_support_labels=labels,original_vertex_ids=keep,planned_faces=faces,projective_denominators=list(map(str,den)))

def mass(P,faces):
 V=Q(0);M=(Q(0),)*3
 for cy in faces:
  for k in range(1,len(cy)-1):
   a,b,c=[P[i] for i in (cy[0],cy[k],cy[k+1])];v=det(a,b,c)/6;assert v>0;V+=v;M=add(M,mul(v/4,add(add(a,b),c)))
 return V,M
if __name__=='__main__':
 basepath,case,param,out=sys.argv[1:];base=json.loads(Path(basepath).read_text());p=json.loads(Path(param).read_text())[case];eta=[Q(v,1<<p['centre_bits']) for v in p['eta_numerators']];r,labels=raw(base,case,eta);Path(out).write_text(json.dumps(r,sort_keys=True,separators=(',',':')))
