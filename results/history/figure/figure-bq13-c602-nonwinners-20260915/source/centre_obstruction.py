"""Exact dual certificates for a scoped centre-only repair obstruction.
All selected healthy identities, every outgoing bad-vertex true edge, and the
body/stable/apex constraints are literal finite inputs rebuilt from an exact audit.
Numerical LP is discovery only; signed rational identities are acceptance.
"""
import sys,json,itertools,hashlib,argparse,math
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def solve(rows,b):
 D=dot(rows[0],cross(rows[1],rows[2]))
 if not D:return None
 cols=[cross(rows[1],rows[2]),cross(rows[2],rows[0]),cross(rows[0],rows[1])]
 return [sum(b[i]*cols[i][j]for i in range(3))/D for j in range(3)]
def run(a):
 z=json.loads(a.audit.read_text());P=[tuple(map(F,p))for p in z['raw_vertices']];g=list(map(F,z['raw_centroid']));q=[tuple(F(v,h)for v in n)for n,h in zip(z['normals'],z['offsets'])];root=z['unstable_vertices'][-1];bad=next(i for i in z['unstable_vertices']if P[i]!=(F(0),F(0),F(1)));root=next(i for i,p in enumerate(P)if p==(F(0),F(0),F(1)));stable=z['stable_face_ids'][0];edges=z['edges'];nei=[[]for p in P]
 for i,j in edges:nei[i].append(j);nei[j].append(i)
 A=[];B=[];names=[];witnesses=[]
 GD=math.lcm(*(v.denominator for v in g));GI=[v.numerator*(GD//v.denominator)for v in g]
 def evalg(n,b):
  D=math.lcm(*(v.denominator for v in [*n,b]));v=sum(t.numerator*(D//t.denominator)*w for t,w in zip(n,GI))-b.numerator*(D//b.denominator)*GD;return v,D*GD
 def add(n,b,name):
  assert evalg(n,b)[0]<0,(name,'own centre is not in strict interior of guard cell');A.append(tuple(n));B.append(b);names.append(name)
 for i in range(len(P)):
  if i in [bad,root]:continue
  js=[]
  for j in nei[i]:
   d=tuple(v-u for u,v in zip(P[i],P[j]));v,D=evalg(tuple(-t for t in d),-dot(P[i],d))
   if v>0:js.append(((v/D)/sum(float(t)**2 for t in d)**.5,j,d))
  assert js;j,d=max(js)[1:];add(d,dot(P[i],d),f'primal:{i}:{j}');witnesses.append(['primal',i,j])
 for i in range(len(q)):
  if i==stable:continue
  rows=[];aa=dot(q[i],q[i])
  for j in range(len(q)):
   if i==j:continue
   ab=dot(q[i],q[j]);n=tuple(aa*q[j][k]-ab*q[i][k]for k in range(3));b=aa-ab;v,D=evalg(n,b)
   if v>0:rows.append(((v/D)/max(1e-300,sum(float(t)**2 for t in n)**.5),j,n,b))
  assert rows;_,j,n,b=max(rows);add(tuple(-v for v in n),-b,f'dual:{i}:{j}');witnesses.append(['dual',i,j])
 for i,qq in enumerate(q):add(qq,F(1),f'interior:{i}')
 for j in nei[root]:
  d=tuple(v-u for u,v in zip(P[root],P[j]));add(tuple(-v for v in d),-dot(P[root],d),f'apex:{root}:{j}')
 aa=dot(q[stable],q[stable])
 for j in range(len(q)):
  if j==stable:continue
  ab=dot(q[stable],q[j]);n=tuple(aa*q[j][k]-ab*q[stable][k]for k in range(3));b=aa-ab;add(n,b,f'stable:{stable}:{j}')
 af=np.array([[float(v)for v in n]for n in A]);bf=np.array(list(map(float,B)));sc=np.linalg.norm(af,axis=1);sc[sc==0]=1
 cert=[];failed=[]
 for j in sorted(nei[bad]):
  d=tuple(v-u for u,v in zip(P[bad],P[j]));c=tuple(-v for v in d);constant=dot(P[bad],d)
  lp=linprog(list(map(float,d)),A_ub=af/sc[:,None],b_ub=bf/sc,bounds=[(None,None)]*3,method='highs')
  if not lp.success:failed.append([j,lp.message]);continue
  active=np.flatnonzero(abs(lp.ineqlin.marginals)>1e-10).tolist();got=None
  for ix in itertools.combinations(active,3):
   mat=[[A[ix[k]][r]for k in range(3)]for r in range(3)];lam=solve(mat,c)
   if lam is None or min(lam)<0:continue
   assert all(sum(lam[k]*A[ix[k]][r]for k in range(3))==c[r]for r in range(3))
   upper=constant+sum(lam[k]*B[ix[k]]for k in range(3))
   if upper<0:got=dict(neighbour=j,constraint_indices=list(ix),constraints=[names[k]for k in ix],weights=list(map(str,lam)),upper_bound=str(upper),upper_decimal=float(upper));break
  if got is None:failed.append([j,'no exact negative dual',float(constant)-float(lp.fun),active])
  else:cert.append(got)
 out=dict(status='EXACT_SCOPED_CENTRE_OBSTRUCTION_PASS'if not failed else 'SCOPED_CENTRE_CERTIFICATE_PARTIAL',bad_rawlex=bad,apex_rawlex=root,stable=stable,guard_count=len(A),neighbours=sorted(nei[bad]),witnesses=witnesses,certificates=cert,failed=failed,rows=[[list(map(str,n)),str(b),s]for n,b,s in zip(A,B,names)],input_audit_sha256=hashlib.sha256(a.audit.read_bytes()).hexdigest(),scope='All centres satisfying these fixed closed halfspace guards; not all witness switches or physical deformations.')
 a.out.write_text(json.dumps(out,sort_keys=True,separators=(',',':')));print(out['status'],'bad',bad,'certs',len(cert),'of',len(nei[bad]),'failed',failed,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--audit',type=Path,required=True);p.add_argument('--out',type=Path,required=True);run(p.parse_args())
