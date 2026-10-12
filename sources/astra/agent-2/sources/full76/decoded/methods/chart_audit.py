"""Exact common-boundary projective chart, full self-stress and Maxwell round trips.
Only finite H generators and exact auditors are authoritative inputs.
"""
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from collections import deque,defaultdict
sys.path.insert(0,str(Path(__file__).parent/'parent'))
from check_A import dot,cross,add,sub,mul,det,encode
from chart import load,recover,inv3
sys.set_int_max_str_digits(0)

def stats(values):
 vals=[]
 def rec(x):
  if isinstance(x,(tuple,list)):
   for v in x:rec(v)
  else:vals.append(F(x))
 rec(values)
 return dict(numerator=max(abs(v.numerator).bit_length() for v in vals),denominator=max(v.denominator.bit_length() for v in vals))

def verify_geometry(Q,seed,calibrate=True):
 faces=seed['faces'];outer=seed['outer'];boundary=seed['boundary'];Q0=seed['Q']
 # Unique origin-fixing linear calibration of the three outer vertices.
 T=[inv3([Q[i] for i in boundary],[Q0[i][k] for i in boundary]) for k in range(3)] if calibrate else [(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
 QQ=[tuple(dot(row,q) for row in T) for q in Q]
 assert all(QQ[i]==Q0[i] for i in boundary)
 # Preserve the parent's fixed Schlegel map, including its delta.
 a,b,c,d,delta=[seed[k] for k in ('a','b','c','d','delta')];D=det(a,b,d)
 rows=[mul(1/D,cross(b,d)),mul(1/D,cross(d,a)),mul(1/D,cross(a,b))]
 R=[];planes=[];X=[]
 for q in QQ:
  p=tuple(dot(row,sub(q,c)) for row in rows);de=1-p[2]/delta;assert de>0;R.append(mul(1/de,p))
 for f,cy in enumerate(faces):
  x=inv3([QQ[i] for i in cy[:3]],[F(1)]*3);X.append(x)
  assert all(dot(x,QQ[i])==1 for i in cy)
  assert all(dot(x,q)<=1 for q in QQ)
  if f==outer:planes.append((F(0),)*3);continue
  k=dot(x,d)+(dot(x,c)-1)/delta;assert k<0,'viewpoint no longer Schlegel'
  planes.append(tuple(-v/k for v in (dot(x,a),dot(x,b),dot(x,c)-1)))
 left={}
 for f,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):left[i,j]=f
 edges=seed['edges'];W=[];zero=[];outer_edges=[];forces=[[F(0),F(0)] for _ in Q]
 for e,(i,j) in enumerate(edges):
  v=sub(R[j][:2],R[i][:2]);J=(-v[1],v[0]);L,H=left[i,j],left[j,i]
  diff=sub(planes[L][:2],planes[H][:2]);w=dot(diff,J)/dot(v,v);W.append(w)
  assert diff==mul(w,J) and planes[L][2]-planes[H][2]==-w*dot(J,R[i][:2])
  if outer in (L,H):assert w<0;outer_edges.append(e)
  else:assert w>=0
  if w==0:zero.append(e)
  for k in range(2):forces[i][k]+=w*(R[j][k]-R[i][k]);forces[j][k]-=w*(R[j][k]-R[i][k])
 assert all(f==[0,0] for f in forces)
 # The positive-edge Dirichlet graph reaches the boundary, so harmonic positions are unique.
 adj=defaultdict(list)
 for (i,j),w in zip(edges,W):
  if w>0:adj[i].append(j);adj[j].append(i)
 seen=set(boundary);todo=list(boundary)
 while todo:
  i=todo.pop()
  for j in adj[i]:
   if j not in seen:seen.add(j);todo.append(j)
 assert len(seen)==len(Q)
 # Independently integrate the face-gradient/intercept cocycle from a zero root plane.
 dual=defaultdict(list)
 for e,(i,j) in enumerate(edges):
  L,H=left[i,j],left[j,i]
  if outer in (L,H):continue
  v=sub(R[j][:2],R[i][:2]);J=(-v[1],v[0]);jump=mul(W[e],(J[0],J[1],-dot(J,R[i][:2])))
  dual[H].append((L,jump));dual[L].append((H,mul(-1,jump)))
 root=next(f for f in range(len(faces)) if f!=outer);p={root:(F(0),)*3};dq=deque([root])
 while dq:
  f=dq.popleft()
  for g,jump in dual[f]:
   if g not in p:p[g]=add(p[f],jump);dq.append(g)
   else:assert p[g]==add(p[f],jump)
 assert len(p)==len(faces)-1
 h=[]
 for i in range(len(Q)):
  vals=[dot(p[f],(*R[i][:2],F(1))) for f,cy in enumerate(faces) if i in cy and f!=outer]
  assert len(set(vals))==1;h.append(vals[0])
 affine=inv3([(*R[i][:2],F(1)) for i in boundary],[h[i] for i in boundary])
 h=[v-dot(affine,(*R[i][:2],F(1))) for i,v in enumerate(h)]
 assert h==[r[2] for r in R]
 for q,qhat,r in zip(Q,QQ,R):
  de=1+r[2]/delta;assert de>0
  back=add(c,mul(1/de,add(add(mul(r[0],a),mul(r[1],b)),mul(r[2],d))))
  assert back==qhat and inv3(T,back)==q
 result=dict(outer_panel=outer,boundary=boundary,old_edges=edges,zero_edges=zero,zero_endpoint_pairs=[edges[e] for e in zero],negative_outer_edges=outer_edges,positive_interior_count=sum(w>0 for w in W),calibration=T,weights=W,projected=R,face_planes=planes,delta=delta,a=a,b=b,c=c,d=d,weight_bits=stats(W),projection_bits=stats(R),calibration_bits=stats(T),exact_equilibrium_residual_zero=True,positive_dirichlet_connected=True,exact_maxwell_roundtrip=True,exact_inverse_roundtrip=True)
 return encode(result)

if __name__=='__main__':
 root=Path(__file__).parent;folder=root/(sys.argv[1] if len(sys.argv)>1 else 'exact10000000000');seed=recover();raw=json.loads((folder/'raw.json').read_text());Q=[tuple(F(v,row[3]) for v in row[:3]) for row in raw['H']]
 out=verify_geometry(Q,seed);data=json.dumps(out,sort_keys=True,separators=(',',':')).encode();(folder/'STRESS.json').write_bytes(data)
 print('COMMON_CHART_EXACT_HARMONIC_MAXWELL_INVERSE_PASS',out['zero_endpoint_pairs'],out['positive_interior_count'],out['weight_bits'],'bytes',len(data),'sha',hashlib.sha256(data).hexdigest(),flush=True)
