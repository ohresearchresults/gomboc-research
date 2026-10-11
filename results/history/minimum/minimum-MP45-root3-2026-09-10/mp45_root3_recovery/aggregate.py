"""Exact MP9:45/root3 coverage. Check mode imports no numerical library."""
from pathlib import Path
import sys,json,hashlib,collections,subprocess,os
sys.path.insert(0,'nova54_recovery')
import comb,exact_check as C
import mp45_norm80_fixed as N
import ratio_probe as R
import omission as O
IDENTITY='NOVA54_MP45_ROOT3_WHOLE_DOMAIN_V3'
PARENT='asg_nYsTs3PVKdXSfXeBpy1AbvkP'
PH='0a98364ee55c3f09547ba8066a783f79a5e89ad9e2571bb1311a08f257d09875'

def enc(x):return comb.encoded(x)
def pin(name):return comb.pin(Path(name).read_bytes())
def audit():
 raw=Path('input.json').read_bytes()
 assert comb.pin(raw)==[7550,'f25c306cca45047cfc524dca05654cbe7b82540afff19b0bf80ff331779e734e']
 data=json.loads(raw);graphs=comb.catalogue(True);g=graphs[45]
 assert data['graph']==g and tuple(map(tuple,g['facets']))==N.FS
 pp=comb.parent_trees(g,3);assert pp==comb.edge_trees(g,3)and len(pp)==9140 and g['trees']==36300
 sys.path.insert(0,'quad_recovery');import verify_universal as U
 u=json.loads(Path('quad_recovery/universal285.json').read_bytes());ps,counts=U.rooted_trees()
 assert [r['parent']for r in u['records']]==[list(p)for p in ps if tuple(p)!=tuple(U.T)]
 universal_codes={comb.code(r['parent'])for r in u['records']};broom_code=comb.code(U.T)
 assert len(universal_codes)==285 and broom_code not in universal_codes
 terminal={};coverage=collections.Counter()
 triangles={frozenset(f)for f in N.FS}
 for i,p in enumerate(pp):
  co=comb.code(p,3)
  if co!=broom_code:
   assert co in universal_codes;coverage['universal_other_shapes']+=1;continue
  order=N.broom(p);assert [p[order[j]]for j in range(9)]==[order[j]for j in U.T]
  if frozenset(order[5:8])not in triangles:coverage['omitted_terminal_cell']+=1;continue
  terminal[i]=list(p);coverage['terminal_brooms']+=1
 assert dict(coverage)=={'universal_other_shapes':9052,'terminal_brooms':66,'omitted_terminal_cell':22}
 assert {str(i):p for i,p in terminal.items()}==data['terminal']
 assert all(terminal[i]==p for i,p in N.P.items())
 old=json.loads(Path('mp45_old55.json').read_bytes())
 assert [{k:r[k]for k in ('index','parent','serial','plan')}for r in old]==data['old']
 assert {r['index']for r in old}==set(terminal)-set(N.P)
 stream=hashlib.sha256();oldm=0
 for r in old:
  assert r['parent']==terminal[r['index']]==r['record']['parent'] and r['record']['root']==3
  assert r['record']['kind']==r['plan'][0] and 'order'not in r['record'] and 'comparisons'not in r['record']
  n,h=C.checked(r['record'],N.FS);assert(n,h)==(r['matrices'],r['scalar_sha'])
  oldm+=n;stream.update(enc(['old',r['index'],n,h]))
 assert oldm==1429
 print('TARGETED_55_OLD_EXACT_PASS',len(old),oldm,flush=True)
 rows=json.loads(Path('mp45_norm80.json').read_bytes())
 assert [(r['index'],r['order'])for r in rows]==N.cases()and len(rows)==80
 for r in rows:
  i,o=r['index'],r['order'];assert r['parent']==terminal[i]
  assert r['pairs']==[list(t)for t in N.comparisons(i,o)] and r['power']in(6,8,10,12)
  h=N.check_record(i,o,r['z']);assert h==r['scalar_sha'];stream.update(enc(['norm',i,o,63,h]))
 print('TARGETED_80_NORM_CHAMBERS_EXACT_PASS',len(rows),5040,flush=True)
 ratio=json.loads(Path('ratio16.json').read_bytes())
 jobs=[[i,a,a+1,2,0]for i in N.P if i not in N.WHOLE for a in range(2)]
 assert ratio['jobs']==jobs and len(ratio['records'])==16
 for j,r in zip(jobs,ratio['records']):
  assert r is not None and r['job']==j and r['power']in(6,8,10,12)
  h=R.check(r);assert h==r['scalar_sha'];stream.update(enc(['ratio',j,63,h]))
 print('EIGHT_TOP_LEAF_CHAMBERS_TWO_CLOSED_RATIO_HALVES_EXACT_PASS',16,1008,flush=True)
 omission=json.loads(Path('omission.json').read_bytes())
 assert omission['parent']==list(U.T)and omission['omitted']==[0,5,6,7]
 oh=O.verify(omission['z']);assert oh==omission['scalar_sha']
 # Each of the eleven original trees has a complete closed cover, including every tie.
 for i in N.P:
  orders={r['order']for r in rows if r['index']==i}
  if i in N.WHOLE:assert orders==set(range(8))
  else:
   assert orders==set(range(1,8))
   assert [j[1:4]for j in jobs if j[0]==i]==[[0,1,2],[1,2,2]]
 assert len(old)+len(N.P)==66
 orbit=sorted({a[3]for a in g['aut']});assert orbit==[3,4,5]
 transports=[]
 for phi in ([0,2,1,4,3,5,8,7,6],[1,0,2,5,4,3,6,8,7]):
  assert phi in g['aut']
  fm=[next(j for j,f in enumerate(N.FS)if set(f)=={phi[i]for i in t})for t in N.FS]
  assert all(comb.cycle(tuple(phi[i]for i in t))==comb.cycle(tuple(reversed(N.FS[fm[j]])))for j,t in enumerate(N.FS))
  assert {tuple(sorted((phi[i],phi[j])))for i,j in g['edges']}==set(map(tuple,g['edges']))
  transports.append(dict(vertex_map=phi,facet_map=fm,orientation=-1,target_root=phi[3]))
 files=['mp45_old55.json','mp45_norm80.json','ratio16.json','omission.json',
        'quad_recovery/universal285.json','quad_recovery/universal285_verification.json']
 report=dict(version=3,identity=IDENTITY,parent_assignment=PARENT,parent_sha256=PH,
             facets=N.FS,edges=g['edges'],root=3,root_orbit=orbit,automorphisms=g['aut'],root_transports=transports,
             graph_catalogue_pin=comb.pin(enc(graphs)),labeled_spanning_trees=36300,
             rooted_tree_orbits=len(pp),coverage=dict(coverage),old_indices=[r['index']for r in old],
             original_eleven=N.P,new_half_jobs=jobs,root_specific_records=151,
             root_specific_matrices=7477,root_specific_leading_minors=67293,
             universal_matrices=17416,omission_matrices=55,total_matrices=24948,
             total_leading_minors=224532,scalar_stream_sha256=stream.hexdigest(),
             omission_scalar_sha256=oh,remaining_root3_cases=[],remaining_top_leaf_chambers=[],
             canonical_C32_transports=[],unclaimed_other_MP9_root_representatives=[0],
             files={name:pin(name)for name in files})
 b=enc(report);Path('root3_report.json').write_bytes(b)
 print('ROOT3_COVERAGE_9052_PLUS_22_PLUS_66_EQUALS_9140_PASS',flush=True)
 print('ROOT3_REPORT',*comb.pin(b),flush=True)
 print('NOVA54_MP45_ROOT3_WHOLE_CONTINUOUS_DOMAIN_PASS',flush=True)
 return report

if __name__=='__main__':
 if sys.argv[1]=='build':
  env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',OPENBLAS_CORETYPE='SkylakeX')
  jobs=[('universal_build','quad_recovery',['build_universal.py']),
        ('omission_build','.', ['omission.py','build']),
        ('old55_build','.', ['build_old.py','build']),
        ('norm80_build','.', ['mp45_norm80_fixed.py','build']),
        ('ratio16_build','.', ['ratio_all.py'])]
  for tag,cwd,args in jobs:
   with open(tag+'.log','w')as log:subprocess.run([sys.executable]+args,cwd=cwd,stdout=log,stderr=subprocess.STDOUT,env=env,check=True)
   print('RECONSTRUCTED',tag,flush=True)
 elif sys.argv[1]not in('check','audit'):raise SystemExit('use build, check, or audit')
 with open('universal_check.log','w')as log:
  subprocess.run([sys.executable,'-S','verify_universal.py','universal285.json'],cwd='quad_recovery',stdout=log,stderr=subprocess.STDOUT,check=True)
 print('UNIVERSAL_285_INDEPENDENT_CHECK_EXECUTED',flush=True)
 audit()
 subprocess.run([sys.executable,'-S','independent.py'],check=True)
 if Path('expected.json').exists():
  expected=json.loads(Path('expected.json').read_bytes())
  for name,v in expected.items():assert pin(name)==v,('OUTPUT_PIN_MISMATCH',name,pin(name),v)
  print('NOVA54_ROOT3_ALL_FROZEN_OUTPUT_PINS_PASS',flush=True)
