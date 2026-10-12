"""Complete rational contact reconstruction followed by true exact hull/mass audit."""
from pathlib import Path
from math import gcd,lcm
from io import BytesIO
import sys,json,time,hashlib,numpy as np
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=mpq

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def solve(A,b):
 n=len(b);M=[list(a)+[v] for a,v in zip(A,b)]
 for k in range(n):
  p=next((j for j in range(k,n) if M[j][k]),None)
  if p is None:raise ValueError('singular rational contact minor')
  M[k],M[p]=M[p],M[k];d=M[k][k];M[k]=[v/d for v in M[k]]
  for j in range(n):
   if j!=k:
    d=M[j][k];M[j]=[v-d*w for v,w in zip(M[j],M[k])]
 return [r[-1] for r in M]
def blob(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def reconstruct(data):
 A=[[mpq(0) for k in range(3)] for i in range(data['nodes'])];free=[mpq(v,data['grid']) for v in data['free_controls']];done=set()
 for row in data['plan']:
  i=row['node'];
  for axis,value in row['fixed'].items():A[i][int(axis)]=mpq(value)
  deps=row['deps'];axes=row['axes'];rest=row['free_axes'];indices=row['free_indices'];assert i not in done and set(deps)<=done
  for k,v in zip(rest,indices):A[i][k]=free[v]
  if deps:
   M=[[A[j][k] for k in axes] for j in deps];b=[1-sum(A[j][k]*A[i][k] for k in range(3) if k not in axes) for j in deps];v=solve(M,b)
   for k,x in zip(axes,v):A[i][k]=x
  assert all(dot(A[i],A[j])==1 for j in deps);done.add(i)
 assert len(done)==len(A)
 F=data['F'];H=[]
 for row in A[:F]:
  den=lcm(*(int(v.denominator) for v in row));ints=[int(v*den) for v in row]+[den];d=gcd(*ints);H.append([v//d for v in ints])
 return A,{'H':H}
def audit(folder,inputfile,out,D=10**12):
 start=time.time();meta=json.loads((folder/'chart.json').read_text());rawbytes=inputfile.read_bytes();q=np.load(BytesIO(rawbytes));out.mkdir(exist_ok=False,parents=True);(out/'source_q.npy').write_bytes(rawbytes);data={k:meta[k] for k in ['nodes','V','F','E','plan','faces']};data.update(grid=D,free_controls=[int(round(float(v)*D)) for v in q],source_q_sha256=hashlib.sha256(rawbytes).hexdigest(),source_q_path=str(inputfile));(out/'construction.json').write_bytes(blob(data));A,H=reconstruct(data);F=data['F'];X=A[F:];Y=A[:F];inc=np.zeros((F,len(X)),bool)
 for f,vs in enumerate(data['faces']):inc[f,vs]=True
 for f,y in enumerate(Y):
  for v,x in enumerate(X):
   d=1-dot(y,x)
   if inc[f,v]:assert d==0
   else:assert d>0,'rational rounding violates strict nonincidence'
 (out/'H.json').write_bytes(blob(H));print('RATIONAL_ATLAS_RECONSTRUCTED',len(H['H']),time.time()-start,flush=True);r=check_B.run(H);vertices={tuple(mpq(v) for v in row) for row in r['raw_vertices']};assert vertices=={tuple(x) for x in X};assert (r['V'],r['E'],r['F'])==(data['V'],data['E'],data['F'])
 (out/'audit.json').write_bytes(blob(r));summary={k:r[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summary.update(C=2*r['E'],seconds=time.time()-start,goal_candidate=r['counts']==[1,1,0] and r['weak']==[0,0,0] and 34<=2*r['E']<500);summary['sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.is_file()};(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('EXACT_ATLAS',summary,flush=True)
 return r
if __name__=='__main__':
 f=ROOT/sys.argv[1];audit(f,f/sys.argv[2],f/sys.argv[3],10**int(sys.argv[4]) if len(sys.argv)>4 else 10**12)
