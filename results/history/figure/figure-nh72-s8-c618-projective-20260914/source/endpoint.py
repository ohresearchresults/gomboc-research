"""Exact whole-body projective/physical-metric images of S8 with explicit H-row loss.
Usage: python -B -S endpoint.py NAME OUT BUILD|A|B|MASS
All exact inputs and helpers are in the same source directory.
"""
import json,sys,math,hashlib,subprocess
from pathlib import Path
from fractions import Fraction as F
assert __debug__
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent
from RECONSTRUCT import recover,solve

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(A):return dot(A[0],cross(A[1],A[2]))
def inverse(A):
 d=det(A);assert d!=0;cols=[cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1])]
 return [[cols[j][i]/d for j in range(3)] for i in range(3)]
def mv(A,x):return tuple(dot(row,x) for row in A)
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encode(v) for v in x]
 return x
def dump(p,x):p.write_text(json.dumps(encode(x),sort_keys=True,separators=(',',':')))
def build(name,out):
 gen=(R/'BASE_GENERATOR.json').read_bytes();assert len(gen)==9599 and hashlib.sha256(gen).hexdigest()=='bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2'
 data=json.loads(gen);assert data['n_supports']==137 and data['grid']==10**8
 rows=recover(data)['H'];assert len(rows)==137
 par=json.loads((R/'PARAMETERS.json').read_text())[name];D=par['D'];t=tuple(F(v,D) for v in par['t']);A=[[F(v,D) for v in row] for row in par['A']];B=inverse(A);assert det(A)>0
 ids=[j for j in range(137) if j!=par['delete']];q=[tuple(F(v,h[3]) for v in h[:3]) for h in rows]
 use=par['admissibility_supports']
 if use:
  assert len(use)==3 and set(use)<=set(ids)
  alpha=solve([[q[i][j] for i in use] for j in range(3)],[-v for v in t]);lower=1-sum(alpha);assert min(alpha)>=0 and lower>0
  vertex=tuple(solve([q[i] for i in use],[F(1)]*3));assert all(dot(q[i],vertex)<=1 for i in ids)
  assert 1+dot(t,vertex)==lower
 else:assert t==(0,0,0);alpha=[];lower=F(1);vertex=None
 new=[]
 for i in ids:
  h=rows[i];n=tuple(F(h[k])+h[3]*t[k] for k in range(3));row=tuple(sum(B[k][j]*n[k] for k in range(3)) for j in range(3))+(F(h[3]),)
  den=math.lcm(*(v.denominator for v in row));num=[int(v*den) for v in row];gg=math.gcd(*num);new.append([v//gg for v in num])
 assert len(set(map(tuple,new)))==136
 out.mkdir(parents=True,exist_ok=False);dump(out/'raw.json',{'H':new});dump(out/'LABELS.json',ids);dump(out/'INPUT.json',par)
 dump(out/'ADMISSIBILITY.json',dict(t=t,A=A,determinant=det(A),support_ids=use,alpha=alpha,minimum_denominator=lower,attaining_base_vertex=vertex,condition_squared_frobenius_bound=sum(v*v for r in A for v in r)*sum(v*v for r in B for v in r)))
 print('EXACT_S8_FILTER_AND_FINITE_PROJECTIVE_BUILD',name,flush=True)
def main():
 name=sys.argv[1];out=Path(sys.argv[2]);stage=sys.argv[3]
 if stage=='BUILD':build(name,out)
 elif stage in ('A','B'):subprocess.run([sys.executable,'-B','-S',str(R/('check_'+stage+'.py')),str(out/'raw.json'),str(out/(stage+'.json'))],check=True)
 elif stage=='MASS':
  import centred_mass
  a=json.loads((out/'A.json').read_text());assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes();dump(out/'CENTRED_MASS.json',centred_mass.run(a));print('EXACT_THIRD_FILLED_CENTRED_MASS',name,flush=True)
 else:raise ValueError(stage)
if __name__=='__main__':main()
