"""Exact rank-three physical centroid controller on two disjoint S8 caps.
Input: a full exact parent report; no arbitrary assigned centre is used.
The three parameters change two piecewise projective caps. In barycentric
coordinates beta relative to four fixed boundary points q0..q3, the map is
 p -> (p + sum_j eta_j beta_j(p) q_j)/(1 + sum_j eta_j beta_j(p)).
All eta start at zero. This file differentiates actual filled volume moments.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
import json,sys,hashlib
sys.set_int_max_str_digits(0)
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def inverse(A):
 n=len(A);M=[[Q(x) for x in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
 for k in range(n):
  i=next(i for i in range(k,n) if M[i][k]);M[k],M[i]=M[i],M[k];d=M[k][k];M[k]=[x/d for x in M[k]]
  for i in range(n):
   if i!=k:d=M[i][k];M[i]=[x-d*y for x,y in zip(M[i],M[k])]
 return [row[n:] for row in M]
def caps(data):
 n=data['V'];adj=[set() for _ in range(n)]
 for a,b in data['edges']:adj[a].add(b);adj[b].add(a)
 seps=set()
 for a in range(n):
  for c in range(a+1,n):
   for b,d in combinations(adj[a]&adj[c],2):seps.add(tuple(sorted((a,b,c,d))))
 P=[tuple(map(Q,p)) for p in data['raw_vertices']];out=[]
 for sep in sorted(seps):
  unseen=set(range(n))-set(sep);cc=[]
  while unseen:
   stack=[min(unseen)];unseen.remove(stack[0]);comp=[]
   while stack:
    i=stack.pop();comp.append(i);new=adj[i]&unseen;unseen-=new;stack.extend(sorted(new))
   cc.append(sorted(comp))
  if len(cc)<2:continue
  cap=min(cc,key=lambda x:(len(x),x));other=set(range(n))-set(cap)-set(sep)
  if any(set(f)&set(cap) and set(f)&other for f in data['faces']):continue
  B=[[P[i][j] for i in sep] for j in range(3)]+[[Q(1)]*4]
  try:Bi=inverse(B)
  except StopIteration:continue
  out.append(dict(sep=list(sep),cap=cap,inverse=Bi))
 small=next(x for x in out if len(x['cap'])==2);large=max(out,key=lambda x:len(x['cap']));assert not set(small['cap'])&set(large['cap']);assert not set(small['sep'])&set(large['cap']) and not set(large['sep'])&set(small['cap']);return [small,large]
def run(data):
 P=[tuple(map(Q,p)) for p in data['raw_vertices']];C=tuple(map(Q,data['raw_centroid']));V=Q(data['ordinary_volume']);cp=caps(data);chosen=[(0,2),(1,0),(1,1)];J=[];details=[]
 for which,k in chosen:
  cap=cp[which];anchor=P[cap['sep'][k]];vel=[(Q(0),)*3 for p in P]
  for i in cap['cap']:
   beta=dot(cap['inverse'][k],(*P[i],Q(1)));vel[i]=tuple(beta*(q-p) for q,p in zip(anchor,P[i]))
  dV=Q(0);dM=[Q(0)]*3
  for face in data['faces']:
   if not set(face)&set(cap['cap']):continue
   for j in range(1,len(face)-1):
    i1,i2,i3=face[0],face[j],face[j+1];a,b,c=P[i1],P[i2],P[i3];va,vb,vc=vel[i1],vel[i2],vel[i3]
    D=det(a,b,c);dD=det(va,b,c)+det(a,vb,c)+det(a,b,vc);dV+=dD/6
    for ax in range(3):dM[ax]+=(dD*(a[ax]+b[ax]+c[ax])+D*(va[ax]+vb[ax]+vc[ax]))/24
  col=[(dM[j]-C[j]*dV)/V for j in range(3)];J.append(col);details.append(dict(cap_index=which,lambda_index=k,volume_derivative=str(dV),moment_derivative=list(map(str,dM))))
 determinant=det(*J);assert determinant!=0
 return dict(status='EXACT_TWO_CAP_PHYSICAL_CENTROID_RANK3_PASS',caps=[{k:v for k,v in c.items() if k!='inverse'} for c in cp],selected_parameters=[list(x) for x in chosen],jacobian_columns=[[str(x) for x in col] for col in J],determinant=str(determinant),details=details,meaning='The actual uniform-volume centroid is locally freely controllable in three dimensions by these two piecewise projective caps, with unchanged incidence in an open identity neighbourhood. No global mechanical cancellation or finite radius is asserted.')
if __name__=='__main__':
 rp,out=map(Path,sys.argv[1:]);rb=rp.read_bytes();ans=run(json.loads(rb));ans['parent_sha256']=hashlib.sha256(rb).hexdigest();out.write_text(json.dumps(ans,sort_keys=True,separators=(',',':')));print(ans['status'],flush=True)
