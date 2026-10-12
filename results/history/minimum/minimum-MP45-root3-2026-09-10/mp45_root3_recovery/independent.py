"""Separate scalar checks for both norm covers; imports no numerical builder."""
from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,'nova54_recovery')
import comb,exact_check as C
from mp45_mass_gate import geometry,FS
assert __debug__
WHOLE={1200,1472,1752}
P={1200:[1,2,5,3,0,3,3,4,7],1205:[1,2,5,3,0,3,3,8,4],
1472:[1,2,5,3,3,8,3,6,7],1752:[1,4,0,3,3,2,5,3,6],
1775:[1,4,0,3,3,2,8,3,5],3058:[1,4,3,3,7,6,3,8,5],
3124:[1,4,3,3,8,3,5,6,7],3149:[1,4,3,3,8,6,7,3,5],
3966:[1,5,3,3,0,2,3,4,7],5772:[2,0,5,3,1,3,3,4,7],
7000:[2,4,3,3,0,1,5,3,6]}
CELLS,BOUNDARY,BETA,FAN=geometry()
assert len(CELLS)==63 and len(BETA)==10

def order(p):
 ch=[[]for _ in p]
 for i,j in enumerate(p):
  if i!=j:ch[j].append(i)
 assert len(ch[3])==2
 leaf=next(i for i in ch[3]if not ch[i]);v=next(i for i in ch[3]if ch[i]);b=[3]
 while True:
  b.append(v)
  if not ch[v]:break
  assert len(ch[v])==1;v=ch[v][0]
 assert len(b)==8 and set(b)|{leaf}==set(range(9));return b+[leaf]

def block_stream(index,z):
 rec=dict(root=3,parent=P[index],kind='cycle',fans=[[a,0]for a in range(9)],relations=BETA,z=z[:1063])
 return C.scalar_matrices(rec,FS)

def main():
 data=json.loads(Path('input.json').read_bytes());old=json.loads(Path('mp45_old55.json').read_bytes())
 assert len(old)==55 and [{k:r[k]for k in ('index','parent','serial','plan')}for r in old]==data['old']
 stream=hashlib.sha256();counts=[0,0,0];ledger=[]
 for r in old:
  rec=r['record'];assert rec['parent']==r['parent']and rec['root']==3
  assert rec['kind']==r['plan'][0] and 'comparisons'not in rec and 'order'not in rec
  n,h=C.checked(rec,FS);assert(n,h)==(r['matrices'],r['scalar_sha'])
  stream.update(comb.encoded(['old',r['index'],n,h]));counts[0]+=n
  ledger.append(['old',r['index'],n,h])
 norm=json.loads(Path('mp45_norm80.json').read_bytes())
 assert [(r['index'],r['order'])for r in norm]==[(i,k)for i in P for k in range(8)if i in WHOLE or k>0]
 for r in norm:
  i,k=r['index'],r['order'];assert r['parent']==P[i];b=order(P[i]);z=r['z']
  pairs=[]
  if k>0:pairs.append((b[8],b[k]))
  if k<7:pairs.append((b[k+1],b[8]))
  assert r['pairs']==[list(q)for q in pairs]
  m=len(pairs);assert len(z)==1063+63*m and all(type(v)is int for v in z)and min(z[1063:])>=0
  h=hashlib.sha256()
  for u,Q in enumerate(block_stream(i,z)):
   for j,(a,c)in enumerate(pairs):
    v=z[1063+u*m+j];Q[a][a]+=2*v;Q[c][c]-=2*v
   bb=C.bareiss(Q);assert bb==C.ldl(Q);h.update(comb.encoded([Q,bb]));counts[1]+=1
  hh=h.hexdigest();assert hh==r['scalar_sha'];stream.update(comb.encoded(['norm',i,k,63,hh]));ledger.append(['norm',i,k,63,hh])
 ratio=json.loads(Path('ratio16.json').read_bytes());jobs=[[i,k,k+1,2,0]for i in P if i not in WHOLE for k in range(2)]
 assert ratio['jobs']==jobs and len(ratio['records'])==16
 for job,r in zip(jobs,ratio['records']):
  i,k,hi,den,mode=job;assert r['job']==job and r['parent']==P[i]
  z=r['z'];assert len(z)==1252 and all(type(v)is int for v in z)and min(z[1063:])>=0
  root,first,*_=order(P[i]);leaf=order(P[i])[8];h=hashlib.sha256()
  for u,Q in enumerate(block_stream(i,z)):
   top,lower,upper=z[1063+3*u:1063+3*u+3]
   # Independent expansion of top order and the two scalar-ratio bounds.
   Q[first][first]+=2*top
   Q[leaf][leaf]+=2*(-top-2*lower+2*upper)
   Q[root][root]+=2*(k*lower-(k+1)*upper)
   bb=C.bareiss(Q);assert bb==C.ldl(Q);h.update(comb.encoded([Q,bb]));counts[2]+=1
  hh=h.hexdigest();assert hh==r['scalar_sha'];stream.update(comb.encoded(['ratio',job,63,hh]));ledger.append(['ratio',job,63,hh])
 assert counts==[1429,5040,1008] and len(ledger)==151
 report=json.loads(Path('root3_report.json').read_bytes());assert stream.hexdigest()==report['scalar_stream_sha256']
 out=dict(identity='NOVA54_ROOT3_INDEPENDENT_DIAGONAL_AUDIT_V1',counts=counts,
          records=151,matrices=sum(counts),leading_minors=9*sum(counts),
          scalar_stream_sha256=stream.hexdigest(),ledger=ledger)
 b=comb.encoded(out);Path('independent_report.json').write_bytes(b)
 print('INDEPENDENT_DIAGONAL_RECONSTRUCTION_151_RECORDS_7477_BLOCKS_PASS')
 print('INDEPENDENT_REPORT',*comb.pin(b))
if __name__=='__main__':main()
