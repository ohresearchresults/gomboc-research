"""NOVA54_MP45_WHOLE_GRAPH_ACTUAL_MOMENTS_V4, root0 component.
Exact arithmetic checker imports no numerical locator. No historical MP9 plans.
"""
from pathlib import Path
import sys,json,hashlib,collections,itertools,multiprocessing,subprocess,os
sys.path.insert(0,'nova54_recovery')
import comb,exact_check as C
FS=tuple(tuple(map(int,s))for s in '014 021 032 043 125 154 235 347 365 376 458 487 568 678'.split())
T=(0,0,1,2,3,4,5,6,0)
PARENT='asg_E8jhRERA9v_K8-YHafCvHQXS'
PH='a8dc9aab660b5e9b5a6b4db109797d548b9562b9dac14a8ca2fa04f55e999eee'

def emit(name,obj):
 b=comb.encoded(obj);Path(name).write_bytes(b);return comb.pin(b)

def graph():
 ee,rot=comb.incidence(FS);es=sorted((a,b)for a,b in ee if a<b)
 au=[list(a)for a in comb.auto_maps(FS)]
 assert au==comb.aut_independent(es)and comb.three_connected(set(ee))
 lap=[[sum(i in e for e in es)if i==j else -int(tuple(sorted((i,j)))in es)for j in range(8)]for i in range(8)]
 n=comb.det(lap);assert n==36300
 return dict(facets=FS,edges=es,aut=au,trees=n)

def broom(p):
 ch=[[]for _ in p]
 for i,j in enumerate(p):
  if i!=j:ch[j].append(i)
 assert len(ch[0])==2
 leaf=next(i for i in ch[0]if not ch[i]);v=next(i for i in ch[0]if ch[i]);b=[0]
 while True:
  b.append(v)
  if not ch[v]:break
  assert len(ch[v])==1;v=ch[v][0]
 assert len(b)==8 and set(b)|{leaf}==set(range(9))
 b.append(leaf);assert [p[b[j]]for j in range(9)]==[b[T[j]]for j in range(9)]
 return b

def enumeration():
 g=graph();ps=comb.parent_trees(g,0);assert ps==comb.edge_trees(g,0)and len(ps)==18150
 tri={frozenset(t)for t in FS};bc=comb.code(T);counts=collections.Counter();terminal=[];omitted=[]
 for i,p in enumerate(ps):
  if comb.code(p)!=bc:counts['nonbroom']+=1;continue
  b=broom(p);row=dict(index=i,parent=list(p),broom=b)
  if frozenset(b[5:8])in tri:terminal.append(row);counts['terminal']+=1
  else:omitted.append(row);counts['omit']+=1
 assert dict(counts)==dict(nonbroom=17964,terminal=134,omit=52)
 # Third enumeration: every labelled long chain and disjoint short leaf.
 es=set(map(tuple,g['edges']));aa=[a for a in g['aut']if a[0]==0];bt=set();allb=set()
 assert aa==[[0,1,2,3,4,5,6,7,8],[0,2,1,4,3,5,8,7,6]]
 for tail in itertools.permutations(range(1,9)):
  b=(0,)+tail
  if not all(tuple(sorted((b[j],b[T[j]])))in es for j in range(1,9)):continue
  p=[0]*9
  for j in range(9):p[b[j]]=b[T[j]]
  q=comb.images(p,aa);allb.add(q)
  if frozenset(b[5:8])in tri:bt.add(q)
 assert bt=={tuple(r['parent'])for r in terminal}and len(allb)==186
 assert allb-bt=={tuple(r['parent'])for r in omitted}
 out=dict(graph=g,root=0,parents=ps,terminal=terminal,coverage=dict(counts))
 assert comb.pin(comb.encoded(out))==[373296,'b2e204cbabc4cdb2351d3b2c8f7d1264966d2431639d3da627fd0283bc932bab']
 emit('root0_enumeration.json',out)
 print('ROOT0_THREE_ENUMERATIONS_36300_LABELLED_18150_ORBITS_186_BROOMS_134_TERMINAL_PASS',flush=True)
 return out,omitted

def build_one(task):
 import locator
 row,plan=task;index,kind,spec,power,selected=plan
 assert index==row['index']and power==8
 rec=locator.make_record(graph(),0,row['parent'],kind,spec,power,selected)
 n,h=C.checked(rec,FS)
 return dict(index=index,parent=row['parent'],plan=plan,record=rec,matrices=n,scalar_sha=h)

def transports(g):
 out=[]
 for r in (0,1,2,6,7,8):
  phi=min(a for a in g['aut']if a[0]==r)
  fm=[next(j for j,f in enumerate(FS)if set(f)=={phi[i]for i in t})for t in FS]
  signs={1 if comb.cycle(tuple(phi[i]for i in t))==comb.cycle(FS[fm[j]])else -1 for j,t in enumerate(FS)}
  assert len(signs)==1;sg=signs.pop()
  assert all(comb.cycle(tuple(phi[i]for i in t))==comb.cycle(FS[fm[j]]if sg==1 else tuple(reversed(FS[fm[j]])))for j,t in enumerate(FS))
  assert {tuple(sorted((phi[i],phi[j])))for i,j in g['edges']}==set(map(tuple,g['edges']))
  out.append(dict(root=r,vertices=phi,facets=fm,orientation=sg))
 assert sorted({min(a[r]for a in g['aut'])for r in range(9)})==[0,3]
 return out

def audit(data,omitted):
 g=data['graph'];terminal=data['terminal'];ps=data['parents']
 plans=json.loads(Path('plans0.json').read_bytes());rows=json.loads(Path('root0_certificates.json').read_bytes())
 assert len(plans)==len(rows)==134 and [p[0]for p in plans]==[r['index']for r in terminal]
 assert [r['plan']for r in rows]==plans
 stream=hashlib.sha256();nm=0;methods=collections.Counter();ledger=[]
 for r,t in zip(rows,terminal):
  rec=r['record'];assert r['index']==t['index']and r['parent']==t['parent']==rec['parent']and rec['root']==0
  _,kind,spec,power,selected=r['plan'];assert kind in ('ordinary','shared','volume','cycle')and power==8
  allowed={'root','parent','kind','fans','z'}|({'relations'}if kind in('volume','cycle')else set())
  assert set(rec)==allowed and rec['kind']==kind and rec['fans']==[[a,0]for a in selected]
  n,h=C.checked(rec,FS);assert(n,h)==(r['matrices'],r['scalar_sha'])
  stream.update(comb.encoded([r['index'],n,h]));nm+=n;methods[kind]+=1;ledger.append([r['index'],n,h])
 print('ROOT0_134_ACTUAL_CERTIFICATES_BAREISS_LDL_PASS',nm,9*nm,dict(methods),flush=True)
 sys.path.insert(0,'quad_recovery');import verify_universal as U
 u=json.loads(Path('quad_recovery/universal285.json').read_bytes());trees,_=U.rooted_trees()
 assert [r['parent']for r in u['records']]==[list(t)for t in trees if t!=T]
 good={comb.code(r['parent'])for r in u['records']};assert len(good)==285
 assert all(comb.code(p)in good or comb.code(p)==comb.code(T)for p in ps)
 import omission as O
 o=json.loads(Path('omission.json').read_bytes());assert o['parent']==list(T)and o['omitted']==[0,5,6,7]
 assert O.verify(o['z'])==o['scalar_sha']
 tx=transports(g)
 report=dict(identity='NOVA54_MP45_WHOLE_GRAPH_ACTUAL_MOMENTS_V4',parent_assignment=PARENT,parent_sha256=PH,
  facets=FS,edges=g['edges'],automorphisms=g['aut'],root0_stabilizer=[a for a in g['aut']if a[0]==0],
  labelled_trees=36300,root0_tree_orbits=18150,coverage=data['coverage'],terminal=terminal,omitted=omitted,
  root0_records=134,root0_matrices=nm,root0_leading_minors=9*nm,method_counts=dict(methods),scalar_ledger=ledger,
  scalar_stream_sha256=stream.hexdigest(),root0_transports=tx,root0_charts=[list(f)for f in FS if 0 not in f],
  inherited_closed_roots=[3,4,5],new_closed_roots=[0,1,2,6,7,8],all_closed_roots=list(range(9)),
  root0_remaining=[],whole_graph_remaining=[],canonical_C32_transports=[],
  enumeration_pin=comb.pin(comb.encoded(data)),certificate_pin=comb.pin(Path('root0_certificates.json').read_bytes()),
  plan_pin=comb.pin(Path('plans0.json').read_bytes()),
  universal_pin=comb.pin(Path('quad_recovery/universal285.json').read_bytes()),omission_pin=comb.pin(Path('omission.json').read_bytes()))
 print('ROOT0_REPORT',*emit('root0_report.json',report),flush=True)
 print('ROOT0_COVERAGE_17964_PLUS_52_PLUS_134_EQUALS_18150_PASS',flush=True)
 print('NOVA54_MP45_ROOT0_ALL_CONTINUOUS_AND_GENUINE_COFACIAL_DOMAINS_PASS',flush=True)
 print('NOVA54_WHOLE_MP45_BY_NEW_ROOT0_AND_IMMUTABLE_E8_ROOT3_PASS_NO_C32_TRANSPORT',flush=True)
 return report

def run():
 mode=sys.argv[1]if len(sys.argv)>1 else'build';assert mode in('build','check','enumerate','search')
 data,omitted=enumeration()
 if mode=='enumerate':return
 if mode=='search':
  import explore0;Path('root0_records').mkdir(exist_ok=True)
  with multiprocessing.get_context('fork').Pool(4)as pool:rows=list(pool.imap(explore0.work,data['terminal']))
  emit('root0_exploration.json',rows)
  print('ROOT0_TARGETED_LOCATOR_FINISHED',len(rows),sum('record'in r for r in rows),flush=True);return
 if mode=='build':
  env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',OPENBLAS_CORETYPE='SkylakeX')
  for tag,cwd,args in [('universal','quad_recovery',['build_universal.py']),('omission','.', ['omission.py','build'])]:
   with open(tag+'_build.log','w')as log:subprocess.run([sys.executable]+args,cwd=cwd,stdout=log,stderr=subprocess.STDOUT,env=env,check=True)
   print('RECONSTRUCTED',tag,flush=True)
  plans=json.loads(Path('plans0.json').read_bytes())
  assert [p[0]for p in plans]==[r['index']for r in data['terminal']]
  with multiprocessing.get_context('fork').Pool(4)as pool:rows=list(pool.imap(build_one,zip(data['terminal'],plans)))
  print('RECONSTRUCTED_ROOT0_134',*emit('root0_certificates.json',rows),flush=True)
 with open('universal_check.log','w')as log:subprocess.run([sys.executable,'-S','verify_universal.py','universal285.json'],cwd='quad_recovery',stdout=log,stderr=subprocess.STDOUT,check=True)
 print('UNIVERSAL_285_STANDARD_LIBRARY_CHECK_EXECUTED',flush=True)
 audit(data,omitted)
 subprocess.run([sys.executable,'-S','physical0.py'],check=True)
 if Path('expected0.json').exists():
  for name,pin in json.loads(Path('expected0.json').read_bytes()).items():assert comb.pin(Path(name).read_bytes())==pin,('OUTPUT_PIN_MISMATCH',name)
  print('NOVA54_MP45_ROOT0_ALL_FROZEN_OUTPUT_PINS_PASS',flush=True)

if __name__=='__main__':run()
