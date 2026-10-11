from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from hashlib import sha256
import json,subprocess,sys
sys.set_int_max_str_digits(0)
assert __debug__
core=Path(sys.argv[1]).resolve()
parent=Path(sys.argv[2]).resolve()
out=Path(sys.argv[3]).resolve()
assert not out.exists()
out.mkdir(parents=True)
def digest(p):
 b=p.read_bytes()
 return len(b),sha256(b).hexdigest()
def dump(p,a):
 p.write_text(json.dumps(a,sort_keys=True,separators=(',',':')))
assert digest(parent)==(28264,'1286c05904d1aee57346b1bbeb200d8998b1656b0319d2cf56b2bfbb071c3599')
D=1000000000000
b=tuple(F(v,D) for v in [231165476175,-287690514274,-722193871745])
L=tuple(tuple(F(v,D) for v in row) for row in [[6195174799506,0,0],[-1419836775816,189361598103,0],[-4331762107070,485380338385,852421755373]])
assert all(L[i][i]>0 for i in range(3))
assert all(L[i][j]==0 for i in range(3) for j in range(i+1,3))
raw=json.loads(parent.read_text());H=[]
for n0,n1,n2,d in raw['H']:
 rhs=[F(n,d)+c for n,c in zip((n0,n1,n2),b)];z=[]
 for i in range(3):
  z.append((rhs[i]-sum(L[i][j]*z[j] for j in range(i)))/L[i][i])
 k=lcm(*(v.denominator for v in z));row=[int(v*k) for v in z]+[k]
 g=gcd(*row);row=[v//g for v in row]
 assert row[3]>0
 H.append(row)
assert len(H)==len(set(map(tuple,H)))==137
dump(out/'raw.json',{'H':H})
assert digest(out/'raw.json')==(42455,'df60591a327f8d36f1c1e66f7d7d4db48cf14433a3bb59e4bd9a668c88c79fcd')
for script,src,dst in [('check_A.py',parent,out/'PARENT_A.json'),('check_A.py',out/'raw.json',out/'A.json'),('check_B.py',out/'raw.json',out/'B.json')]:
 subprocess.run([sys.executable,'-B','-S',str(core/script),str(src),str(dst)],check=True)
assert digest(out/'PARENT_A.json')==(435251,'97e6687a0fd4a47515153da6efe8ed9168ea0e2b5ec603b2e1ef7c6b8bf230b9')
assert digest(out/'A.json')==(504653,'d01383b4720b9615d019f4a229429b97a57f16755998b305033b5ff3506b2752')
assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes()
P=json.loads((out/'PARENT_A.json').read_text());A=json.loads((out/'A.json').read_text())
assert [A[k] for k in ('V','E','F')]==[164,299,137]
assert A['counts']==[3,3,4] and A['weak']==[0,0,0]
assert A['active_input_indices']==list(range(137))
assert A['stable_face_ids']==[104,114,125]
assert A['unstable_vertices']==[0,162,163]
assert A['saddle_edges']==[[1,65],[2,92],[5,6],[162,163]]
assert all(A[k]==0 for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'])
X=[tuple(map(F,r)) for r in A['raw_vertices']]
lookup={p:i for i,p in enumerate(X)};pts=[];den=[]
for row in P['raw_vertices']:
 p=tuple(map(F,row));s=1+sum(v*c for v,c in zip(p,b));assert s>0
 den.append(s)
 pts.append(tuple(sum(p[i]*L[i][j] for i in range(3))/s for j in range(3)))
assert min(den)==F(55561225651,200000000000)
assert len(set(pts))==len(X)==164 and set(pts)==set(X)
mp=[lookup[p] for p in pts]
assert sorted(sorted([mp[i],mp[j]]) for i,j in P['edges'])==A['edges']
for cy,old in zip(A['faces'],P['faces']):
 mapped=[mp[i] for i in old]
 assert len(mapped)==len(cy) and set(mapped)==set(cy)
 assert any(cy==mapped[k:]+mapped[:k] for k in range(len(cy)))
sys.path.insert(0,str(core))
from centred_mass import run as mass
M=mass(A)
assert M['tetrahedra']==324
assert M['common_centred_denominator_bits']==92094
assert M['filled_first_moments']==[0,0,0]
dump(out/'MASS.json',M)
assert digest(out/'MASS.json')==(223,'228edbb5a0f660741a63f224022c51e3183e46730dff92dfd46140fd03c151c2')
print('PM598_EXACT_TWO_AUDITS_WHOLE_COMPLEX_AND_CENTRED_MASS_PASS')
