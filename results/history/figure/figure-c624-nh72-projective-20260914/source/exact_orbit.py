"""Exact finite projective/metric endpoints of literal C624. Standard library only.
Usage: python -B -S exact_orbit.py SOURCE MODERATE|FAR OUTPUT BUILD|A|B|MASS|EXTRA|FINISH
BUILD requires a nonexistent OUTPUT. No centre, vertex or incidence cache is input.
"""
import sys,json,math,hashlib,subprocess
from pathlib import Path
from fractions import Fraction as F
assert __debug__
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(A):return dot(A[0],cross(A[1],A[2]))
def inverse(A):
 D=det(A);assert D!=0
 cols=[cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1])]
 return [[cols[j][i]/D for j in range(3)] for i in range(3)]
def matvec(A,x):return tuple(dot(row,x) for row in A)
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return{k:encode(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return[encode(v) for v in x]
 return x
def dump(p,d):p.write_text(json.dumps(encode(d),sort_keys=True,separators=(',',':')),encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bits(x):
 x=list(map(F,x));return[max(abs(v.numerator).bit_length() for v in x),max(v.denominator.bit_length() for v in x)]
def data(source,which):
 sys.path.insert(0,str(source));from RECONSTRUCT import recover,solve
 p=source/'BASE_GENERATOR.json';assert sha(p)=='9794a36115719432a426f28f25ec8a16f28224237acc2b94b2acb4625dcfbede'
 raw=recover(json.loads(p.read_text()));b=json.dumps(raw,sort_keys=True,separators=(',',':')).encode()
 assert hashlib.sha256(b).hexdigest()=='0c4c48f26393826d341e55ac9ae0da5610b084345ffabada6deb6255de9409e5'
 par=json.loads((source/'PARAMETERS.json').read_text())[which];D=par['D'];t=tuple(F(v,D) for v in par['t']);A=[[F(v,D) for v in row] for row in par['A']];inv=inverse(A);assert det(A)>0
 q=[tuple(F(v,h[3]) for v in h[:3]) for h in raw['H']]
 assert all(sum(map(abs,n))<5 for n in q)
 ids=par['admissibility_supports'];alpha=solve([[q[i][j] for i in ids] for j in range(3)],[-v for v in t]);assert min(alpha)>=0;lower=1-sum(alpha);assert lower>0
 assert all(sum(alpha[k]*q[i][j] for k,i in enumerate(ids))==-t[j] for j in range(3))
 return raw,par,t,A,inv,alpha,lower

def extra(out,t,A,inv,lower):
 a=json.loads((out/'A.json').read_text());X=[tuple(map(F,row)) for row in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));V=F(a['ordinary_volume']);M=tuple(map(F,a['raw_first_moments']));assert M==mul(V,g)
 Y=[matvec(inv,x) for x in X];back=[]
 for y in Y:
  h=1-dot(t,y);assert h>0;back.append(mul(1/h,y))
 order=sorted(range(len(back)),key=lambda i:back[i]);parent_of={j:i for i,j in enumerate(order)}
 assert back[order[96]]==(0,0,1)
 ds=[1+dot(t,x) for x in back];assert min(ds)>=lower
 C=math.lcm(*(v.denominator for v in g));gc=tuple(int(C*v) for v in g);bs=[math.lcm(*(v.denominator for v in x)) for x in X];aa=[tuple(int(b*v) for v in x) for b,x in zip(bs,X)];zz=[sub(mul(C,x),mul(b,gc)) for x,b in zip(aa,bs)]
 graph=[[] for _ in X];rev=[[] for _ in X]
 for i,j in a['edges']:
  e=sub(mul(bs[i],aa[j]),mul(bs[j],aa[i]));u=dot(zz[i],e);v=dot(zz[j],e)
  if u>0:graph[i].append(j);rev[j].append(i)
  if v<0:graph[j].append(i);rev[i].append(j)
 lengths=[dot(z,z) for z in zz];root=0
 for j in range(1,len(X)):
  if lengths[j]*bs[root]**2>lengths[root]*bs[j]**2:root=j
 assert root in a['unstable_vertices'];seen={root};queue=[root]
 while queue:
  j=queue.pop()
  for i in rev[j]:
   if i not in seen:seen.add(i);queue.append(i)
 bad=set(range(len(X)))-seen;assert all(set(graph[i])<=bad for i in bad)
 boundary=[e for e in a['edges'] if (e[0] in bad)!=(e[1] in bad)]
 output=dict(parent_index_of_new=[parent_of[i] for i in range(len(X))],new_index_of_parent=order,
  unstable_in_parent_labels=[parent_of[i] for i in a['unstable_vertices']],
  saddles_in_parent_labels=[[parent_of[i],parent_of[j]] for i,j in a['saddle_edges']],
  global_root_in_parent_labels=parent_of[root],root_reaching_parent_labels=sorted(parent_of[i] for i in seen),
  closed_unwanted_parent_labels=sorted(parent_of[i] for i in bad),boundary_edges_parent_labels=[[parent_of[i],parent_of[j]] for i,j in boundary],
  projective_denominator_min=min(ds),certificate_lower=lower,physical_A_determinant=det(A),
  frobenius_condition_squared_bound=sum(v*v for row in A for v in row)*sum(v*v for row in inv for v in row),
  projective_volume=V/det(A),projective_centroid=matvec(inv,g),
  sizes=dict(raw_vertices=bits(v for x in X for v in x),volume=bits([V]),first_moments=bits(M),centroid=bits(g),
   centred_vertices=bits(x[k]-g[k] for x in X for k in range(3))),
  active_original_supports=a['active_input_indices'])
 dump(out/'EXTRA.json',output)

def main():
 source=Path(sys.argv[1]).resolve();which=sys.argv[2];out=Path(sys.argv[3]).resolve();stage=sys.argv[4]
 raw,par,t,A,inv,alpha,lower=data(source,which)
 if stage=='BUILD':
  out.mkdir(parents=True,exist_ok=False);new=[]
  for h in raw['H']:
   n=add(tuple(map(F,h[:3])),mul(F(h[3]),t));z=tuple(sum(inv[k][j]*n[k] for k in range(3)) for j in range(3))+(F(h[3]),);D=math.lcm(*(v.denominator for v in z));r=[int(v*D) for v in z];d=math.gcd(*r);new.append([v//d for v in r])
  assert len(set(map(tuple,new)))==137;dump(out/'raw.json',{'H':new});dump(out/'INPUT.json',par);dump(out/'ADMISSIBILITY.json',dict(alpha=alpha,lower=lower,determinant=det(A),cube_halfside=F(1,5)))
  print('FINITE_RATIONAL_PHYSICAL_PROJECTIVE_ENDPOINT_BUILT',which,flush=True)
 elif stage in ('A','B'):
  subprocess.run([sys.executable,'-B','-S',str(source/('check_'+stage+'.py')),str(out/'raw.json'),str(out/(stage+'.json'))],check=True)
 elif stage=='MASS':
  sys.path.insert(0,str(source));import centred_mass;dump(out/'CENTRED_MASS.json',centred_mass.run(json.loads((out/'A.json').read_text())));print('THIRD_OWN_FILLED_MASS_PASS',which,flush=True)
 elif stage=='EXTRA':
  assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes();extra(out,t,A,inv,lower);print('EXACT_WHOLE_BASIN_AND_PROJECTIVE_MAPPING_PASS',which,flush=True)
 elif stage=='FINISH':
  a=json.loads((out/'A.json').read_text());assert [a[k] for k in ['V','E','F']]==par['expected_VEF'];assert a['counts']==par['expected_counts'];assert a['weak']==par['expected_weak'];assert a['active_input_indices']==list(range(137))
  assert a['edge_primitive_count']==1248 and a['edge_primitive_zero_count']==0 and a['face_primitive_zero_count']==0 and a['vertex_max_zero_count']==0
  assert json.loads((out/'CENTRED_MASS.json').read_text())['filled_first_moments']==[0,0,0]
  expected=json.loads((source/'EXPECTED.json').read_text())[which]
  for name,r in expected.items():assert (out/name).stat().st_size==r['bytes'] and sha(out/name)==r['sha256'],name
  print('NH72_C624_PROJECTIVE_METRIC_TWO_EXACT_AND_COLD_PASS',which,flush=True)
 else:raise ValueError(stage)
if __name__=='__main__':main()
