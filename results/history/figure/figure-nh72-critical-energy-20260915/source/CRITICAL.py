"""Exact 12-control deformation of the whole PAIR99 critical disk.
Caps are identity in this new rational endpoint. All retained contacts are checked.
"""
import json,math,sys
from fractions import Fraction as Q
import BUILD as B
sys.set_int_max_str_digits(0)
CHANGED=[106,109,112,114,117,120,124,146,148,149]

def solve(A,b):return [B.dot(row,b) for row in B.inverse(A)]
def points(base,param):
 P,keep,faces,labels,beta=B.setup(base,'PAIR99');X=P.copy();q={}
 for local,(n,h) in enumerate(zip(base['normals'],base['offsets'])):
  label=local if local<99 else local+1;q[label]=tuple(Q(v,h) for v in n)
 oldq=q.copy();free73=param['normal73_free_axes'];axis73=next(i for i in range(3) if i not in free73)
 free={int(k):v for k,v in param['free_axes'].items()}
 controls=list(q[72])+[q[73][k] for k in free73]+[P[i][k] for i in [124,112,146,148,149] for k in free[i]]
 z=[Q(n,param['control_denominator'])*Q(param['control_scale']) for n in param['control_numerators']]
 assert len(controls)==len(z)==12 and param['cap_parameters']==[0]*6
 controls=[a+b for a,b in zip(controls,z)];q[72]=tuple(controls[:3]);n=list(q[73])
 for k,v in zip(free73,controls[3:5]):n[k]=v
 n[axis73]=(1-sum(n[k]*P[69][k] for k in free73))/P[69][axis73];q[73]=tuple(n)
 for i,ns in [(106,[15,71,72]),(109,[15,72,75]),(114,[17,71,73]),(117,[71,72,73]),(120,[3,72,73])]:
  X[i]=tuple(solve([q[j] for j in ns],[Q(1)]*3))
 k=5
 for i,ns in [(124,[3,72]),(112,[75]),(146,[80]),(148,[69,80]),(149,[3,69])]:
  ax=[j for j in range(3) if j not in free[i]];p=list(P[i])
  for a in free[i]:p[a]=controls[k];k+=1
  sol=solve([[q[j][a] for a in ax] for j in ns],[1-sum(q[j][a]*p[a] for a in free[i]) for j in ns])
  for a,v in zip(ax,sol):p[a]=v
  X[i]=tuple(p)
 assert k==12
 assert [i for i in keep if X[i]!=P[i]]==CHANGED
 return X,keep,faces,labels

def build(base,param):
 X,keep,faces,labels=points(base,param);H=[]
 for cy in faces:
  a,b,c=(X[j] for j in cy[:3]);n=B.cross(B.sub(b,a),B.sub(c,a));h=B.dot(n,a);assert h>0
  assert all(B.dot(n,X[j])==h for j in cy)
  assert all(B.dot(n,X[j])<h for j in keep if j not in cy)
  for i,j in zip(cy,cy[1:]+cy[:1]):
   assert all(B.dot(n,B.cross(B.sub(X[j],X[i]),B.sub(X[k],X[i])))>0 for k in cy if k not in (i,j))
  d=math.lcm(*(v.denominator for v in (*n,h)));row=[int(v*d) for v in (*n,h)];g=math.gcd(*row);H.append([v//g for v in row])
 assert len(H)==138 and len(set(map(tuple,H)))==138
 return {'H':H},dict(identity=param['identity'],changed_base_vertices=CHANGED,original_vertex_ids=keep,input_support_labels=labels,planned_faces=faces)
if __name__=='__main__':
 from pathlib import Path
 b=json.loads(Path(sys.argv[1]).read_text());p=json.loads(Path(sys.argv[2]).read_text());r,l=build(b,p)
 for name,obj in [('raw.json',r),('LABELS.json',l)]:Path(sys.argv[3],name).write_text(json.dumps(obj,sort_keys=True,separators=(',',':')))
 print('EXACT_CRITICAL_DISK_INPUT_BUILT',len(r['H']))
