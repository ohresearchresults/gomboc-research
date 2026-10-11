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
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
assert digest(parent)==(504653,'d01383b4720b9615d019f4a229429b97a57f16755998b305033b5ff3506b2752')
P=json.loads(parent.read_text())
X=[tuple(map(F,r)) for r in P['raw_vertices']]
removed={3,5,6};keep=[i for i in range(len(X)) if i not in removed]
I=[]
for p in X:
 d=lcm(*(v.denominator for v in p));I.append(tuple(int(v*d) for v in p)+(d,))
rows={tuple(n)+(d,) for n,d,cy in zip(P['normals'],P['offsets'],P['faces']) if len(set(cy)-removed)>=3}
triples=[[4,23,26],[4,30,32],[4,26,30],[4,36,44],[4,32,36],[4,8,7],[4,16,19],[7,13,16],[4,19,20],[4,9,8],[4,11,10],[4,20,23],[1,11,4],[4,7,16],[7,12,13],[1,55,58],[4,49,50],[4,50,55],[1,58,65],[4,54,49],[1,4,55]]
for ids in triples:
 a,b,c=[I[i] for i in ids]
 u=tuple(b[i]*a[3]-a[i]*b[3] for i in range(3))
 v=tuple(c[i]*a[3]-a[i]*c[3] for i in range(3))
 n=cross(u,v);r=tuple(x*a[3] for x in n)+(dot(n,a[:3]),)
 g=gcd(*r);assert g
 r=tuple(x//g for x in r)
 if r[3]<0:r=tuple(-x for x in r)
 assert r[3]>0
 assert all(dot(r[:3],I[i][:3])<=r[3]*I[i][3] for i in keep)
 rows.add(r)
assert len(rows)==131
dump(out/'raw.json',{'H':sorted(rows)})
assert digest(out/'raw.json')==(40168,'5fa9c4c33a0a45df541edbfce74ec52d077ce47aca01c17f2ed2463ad8a9b57a')
for script,dst in [('check_A.py','A.json'),('check_B.py','B.json')]:
 subprocess.run([sys.executable,'-B','-S',str(core/script),str(out/'raw.json'),str(out/dst)],check=True)
assert digest(out/'A.json')==(499908,'e1913a7610265741039439577f3513073c36578a6646144595e1e0dfdbae273c')
assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes()
A=json.loads((out/'A.json').read_text())
assert [A[k] for k in ('V','E','F')]==[161,290,131]
assert A['counts']==[2,2,2] and A['weak']==[0,0,0]
assert A['active_input_indices']==list(range(131))
assert A['stable_face_ids']==[94,99] and A['unstable_vertices']==[0,159]
assert A['saddle_edges']==[[2,89],[3,4]]
assert all(A[k]==0 for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'])
assert set(tuple(map(F,r)) for r in A['raw_vertices'])=={X[i] for i in keep}
sys.path.insert(0,str(core))
from centred_mass import run as mass
M=mass(A)
assert M['tetrahedra']==318 and M['filled_first_moments']==[0,0,0]
assert M['common_centred_denominator_bits']==91696
dump(out/'MASS.json',M)
assert digest(out/'MASS.json')==(223,'bde47f45a7b626e4cf98e2840165369515981bab97658f3c91e9c0b351338282')
print('PM580_EXACT_HULL_TWO_AUDITS_AND_CENTRED_MASS_PASS')
