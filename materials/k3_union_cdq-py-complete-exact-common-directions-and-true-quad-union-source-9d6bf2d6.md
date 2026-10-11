# material-9d6bf2d64fdf

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

"""Exact union of accepted C,D common directions and genuine quad1789/root direction.
python -S k3_union_cdq.py build|check
C and D remain separate body-wide directions; never mix their per-facet tests.
The quad dissection uses only the common root direction.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import hashlib,json,sys
assert __debug__
PINS={
 'k3_census.py':(13141,'9d87d21a211545b6174a755b75feda6620e3df8ac4074f0e4703cc51bb9be68a'),
 'k3_domains.json':(2724409,'f0fae254b43adff66173b78de6f77853370253113b1d331e6f45c9c94ec85ed6'),
 'k3_classes.json':(2332920,'e339f0a91bc369b599f7066ffa93075a2321978c3647e738db63195eaa4bc25c'),
 'quad1789_exact.py':(5801,'fae2a51174c73a0a27ad6aafa549a54ed645f64fa13c04549f6774bed3f8ff17'),
 'triangle_bounds_exact.py':(3661,'fa629a519fa4541239f3b41e8ad54089c62fbef46ef8cb21cf886629c02f758d'),
 'quad1789_delta.py':(15916,'29437de31c79ae02f0682b93efec4d9beb43d2a2343f594174799750cb21f516'),
 'quad1789_delta.json':(99954,'030b06e0651d9ce4682270d3373d5b998bddb934ed991a2aaf7083a3e0566ad3')}
def pin(b):return(len(b),hashlib.sha256(b).hexdigest())
def enc(x):return(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
for name,want in PINS.items():assert pin(Path(name).read_bytes())==want,('INPUT',name)
import quad1789_delta as Q
PREMISES={
 'C_proof':'[internal-source-reference]',
 'C_certificate':'[internal-source-reference]',
 'C_literal_application':'[internal-source-reference]',
 'D_proof':'[internal-source-reference]',
 'D_certificate':'[internal-source-reference]',
 'D_literal_application':'[internal-source-reference]',
 'quad_capsule_part1':'[internal-source-reference]',
 'quad_capsule_part2':'[internal-source-reference]'}
ALL=set(combinations([i for i in range(10) if i!=3],3))
BAD_C={(0,1,8),(0,1,9),(0,7,8),(0,7,9),(0,8,9),(1,8,9)}
BAD_D={(0,8,9),(7,8,9)}
GOOD_C=ALL-BAD_C;GOOD_D=ALL-BAD_D
assert len(GOOD_C)==78 and len(GOOD_D)==82

def path_order(row,root):
 pp=Q.paths(row,root)
 ends=[i for i in range(10) if sum(i in e for e in row['tree_edges'])==1]
 assert len(ends)==2 and all(sum(i in e for e in row['tree_edges'])<=2 for i in range(10))
 short,long=sorted((pp[v][::-1] for v in ends),key=len)
 path=tuple(short+long[-2::-1]);assert len(path)==len(set(path))==10 and path[3]==root
 assert len(short)==4 and len(long)==7
 return path

def triangulate(face,good):
 @lru_cache(None)
 def dp(i,j):
  if j-i<2:return ()
  for k in range(i+1,j):
   t=(face[i],face[k],face[j])
   if tuple(sorted(t)) not in good:continue
   a,b=dp(i,k),dp(k,j)
   if a is not None and b is not None:return a+b+(t,)
  return None
 out=dp(0,len(face)-1)
 if out is not None:
  assert len(out)==len(face)-2
  boundary={Q.edge(face[i],face[(i+1)%len(face)]) for i in range(len(face))}
  counts=Counter(Q.edge(t[i],t[(i+1)%3]) for t in out for i in range(3))
  assert {e for e,n in counts.items() if n==1}==boundary
  assert all(n==(1 if e in boundary else 2) for e,n in counts.items())
  ix={v:i for i,v in enumerate(face)}
  diagonals=[tuple(sorted(ix[v] for v in e)) for e in counts if e not in boundary]
  assert all(not(a<c<b<d or c<a<d<b) for (a,b),(c,d) in combinations(diagonals,2))
 return out

def build():
 rows=json.loads(Path('k3_domains.json').read_text())['rows']
 classes=json.loads(Path('k3_classes.json').read_text())['classes']
 qdata=json.loads(Path('quad1789_delta.json').read_text())
 raw=set();old=set();C=set();D=set();Cw=[];Dw=[]
 for row in rows:
  i=row['k3_index'];es=Q.validate_faces(row['facet_cycles'],list(range(10)))
  assert len(es)==17 and es==set(map(tuple,row['edges'])) and set(map(tuple,row['tree_edges']))<=es
  for q in row['roots']:
   if q['status']!='open':continue
   r=q['vertex'];key=(i,r);raw.add(key);pp=Q.paths(row,r)
   _,tri,_,_=Q.predicate(pp,r)
   if all(tri(tuple(f)) is not None for f in row['facet_cycles'] if r not in f):old.add(key)
   if q['tree_index']!=585:continue
   path=path_order(row,r);inv={v:j for j,v in enumerate(path)}
   faces=[(j,tuple(inv[v] for v in f)) for j,f in enumerate(row['facet_cycles']) if r not in f]
   for good,passed,witness in ((GOOD_C,C,Cw),(GOOD_D,D,Dw)):
    cells=[triangulate(f,good) for j,f in faces]
    if all(c is not None for c in cells):
     passed.add(key);witness.append({'position':key,'path':path,'facets':[{'facet_index':j,'cycle':f,'triangles':t} for (j,f),t in zip(faces,cells)]})
 _,A,B=Q.inherited_central(rows);extra=A|B|{(287,6)}
 before=raw-old-extra;afterC=before-C;afterCD=afterC-D
 quad=set(map(tuple,qdata['new_positions']))
 assert len(raw)==11743 and len(old)==5055 and len(extra)==29
 assert len(before)==6659 and len(afterC)==5871 and len(afterCD)==5702
 assert len(before-C)==len(before)-788 and len(afterC-D)==len(afterC)-169
 assert len(quad)==147 and quad<=before
 fresh=quad&afterCD;after=afterCD-quad
 mapping={};classsets={name:set() for name in ('before','afterC','afterCD','quad','quad_new','after','C_delta','D_delta')}
 for cl in classes:
  i,r=cl['representative'];members={(m['k3_index'],m['root']) for m in cl['members']}
  for m in cl['members']:
   Q.transport(rows[i],rows[m['k3_index']],m,r);key=(m['k3_index'],m['root']);assert key not in mapping;mapping[key]=cl['class_index']
  for name,positions in (('before',before),('afterC',afterC),('afterCD',afterCD),('quad',quad),('quad_new',fresh),('after',after),('C_delta',before-afterC),('D_delta',afterC-afterCD)):
   if members&positions:assert members<=positions,(name,cl['class_index']);classsets[name].add(cl['class_index'])
 assert set(mapping)==raw
 assert [len(classsets[n]) for n in ('before','afterC','afterCD','quad','C_delta','D_delta')]==[4817,4316,4164,125,501,152]
 assert classsets['quad']==set(qdata['new_classes'])
 # Every retained quad certificate and cell is checked with the same root direction.
 for rec in qdata['proof_records']:
  key=tuple(rec['position']);assert mapping[key]==rec['class_index'];i,r=key;pp=Q.paths(rows[i],r);bound,*_=Q.predicate(pp,r)
  faces={f['facet_index'] for f in rec['facet_dissection']}
  assert faces=={j for j,f in enumerate(rows[i]['facet_cycles']) if r not in f}
  for f in rec['facet_dissection']:
   assert min(Q.validate_cells(tuple(rows[i]['facet_cycles'][f['facet_index']]),f['cells'],pp,r,bound))>=Q.F(1,1000)
 open_before={i for i,r in before};openCD={i for i,r in afterCD};open_after={i for i,r in after}
 def stat(pos):return{'positions':len(pos),'classes':len({mapping[p] for p in pos})}
 summary={'baseline':stat(before),'C_delta':stat(before-afterC),'D_further_delta':stat(afterC-afterCD),'afterCD':stat(afterCD),'quad_old_delta':stat(quad),'quad_overlap_C':stat(quad&(before-afterC)),'quad_overlap_D_further':stat(quad&(afterC-afterCD)),'quad_fresh':stat(fresh),'afterCDQ':stat(after),'open_domains_baseline':len(open_before),'open_domains_CD':len(openCD),'open_domains_CDQ':len(open_after),'fully_excluded_domains_CD':len(rows)-len(openCD),'fully_excluded_domains_CDQ':len(rows)-len(open_after)}
 print('K3_CDQ_UNION_COUNTS',json.dumps(summary,sort_keys=True),flush=True)
 return {'identity':'MINIMUM_K3_COMMON_C_D_QUAD1789_EXACT_UNION_V1','input_pins':PINS,'accepted_premises':PREMISES,'summary':summary,'quad_fresh_positions':sorted(fresh),'quad_fresh_classes':sorted(classsets['quad_new']),'quad_fresh_records':[r for r in qdata['proof_records'] if tuple(r['position']) in fresh],'quad_overlap_C_positions':sorted(quad&(before-afterC)),'quad_overlap_D_positions':sorted(quad&(afterC-afterCD)),'C_positions':sorted(before-afterC),'D_positions':sorted(afterC-afterCD),'C_witnesses':[r for r in Cw if tuple(r['position']) in before],'D_witnesses':[r for r in Dw if tuple(r['position']) in afterC],'remaining_positions':sorted(after),'remaining_classes':sorted(classsets['after']),'remaining_class_trees':dict(sorted(Counter(classes[i]['tree_index'] for i in classsets['after']).items())),'fresh_quad_class_trees':dict(sorted(Counter(classes[i]['tree_index'] for i in classsets['quad_new']).items())),'CD_newly_closed_domains':sorted(open_before-openCD),'quad_further_closed_domains':sorted(openCD-open_after),'fully_closed_domains':sorted(set(range(len(rows)))-open_after),'scope':'Local marked K3/FULL253 incidence register only; no new universal complexity bound, no attainer, no unmarked type count.'}

def main():
 assert sys.argv[1:] in (['build'],['check'])
 b=enc(build());p=Path('k3_union_cdq.json')
 if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==b
 else:p.write_bytes(b)
 print('K3_COMMON_C_D_QUAD1789_EXACT_UNION_PASS',*pin(b))
if __name__=='__main__':main()
