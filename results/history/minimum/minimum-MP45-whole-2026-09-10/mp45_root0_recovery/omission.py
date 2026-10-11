from pathlib import Path
import sys,json,hashlib,itertools
sys.path.insert(0,'nova54_recovery')
import exact_check as C,comb
T=[0,0,1,2,3,4,5,6,0]
CELLS=[(0,)+t for t in itertools.combinations(range(1,9),3)if t!=(5,6,7)]
def verify(z):
 assert len(z)==449 and all(type(x)is int for x in z)and min(z[9:])>=0
 h=hashlib.sha256()
 for u,t in enumerate(CELLS):
  w=[int(i in t)for i in range(9)]
  Q=[[z[i]*w[j]+z[j]*w[i]for j in range(9)]for i in range(9)]
  for i,l in zip(range(1,9),z[9+8*u:9+8*(u+1)]):
   Q[i][i]+=2*l;Q[i][T[i]]-=l;Q[T[i]][i]-=l
  a=C.bareiss(Q);assert a==C.ldl(Q);h.update(comb.encoded([Q,a]))
 return h.hexdigest()
if __name__=='__main__':
 if sys.argv[1]=='build':
  sys.path.insert(0,'quad_recovery');import engine
  z=engine.certify(T,[CELLS],eps=1e-7,maxouter=11,power=8)
  assert z is not None
  o=dict(parent=T,omitted=[0,5,6,7],z=z,scalar_sha=verify(z))
  Path('omission.json').write_bytes(comb.encoded(o))
 else:
  o=json.loads(Path('omission.json').read_bytes());assert o['parent']==T and o['omitted']==[0,5,6,7]
  assert verify(o['z'])==o['scalar_sha']
 b=Path('omission.json').read_bytes();print('OMISSION_PIN',len(b),hashlib.sha256(b).hexdigest())
 print('NOVA54_OMITTED_TERMINAL_55_BLOCKS_495_MINORS_PASS',o['scalar_sha'])
