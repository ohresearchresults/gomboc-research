# material-7342542c0971

AI research material

---

"""Complete literal census and joint-moment search for K3 quadrivalent path ends.
python -S k3_endpoints.py build CENSUS_DIR PINNED_joint_exact.py
python k3_endpoints.py locate INDEX [INDEX ...]
python -S k3_endpoints.py inventory
python -S k3_endpoints.py verify
The index below is a NEW input-table index, never a census or quotient alias.
No local file or numerical proposal by itself is accepted research state.
"""
from pathlib import Path
from collections import Counter
import hashlib,importlib.util,json,os,subprocess,sys
assert __debug__
HERE=Path(__file__).resolve().parent
ID='MINIMUM_K3_QUADRIVALENT_PATH_ENDS_V1'
PINS={
 'k3_census.py':[13141,'9d87d21a211545b6174a755b75feda6620e3df8ac4074f0e4703cc51bb9be68a'],
 'k3_domains.json':[2724409,'f0fae254b43adff66173b78de6f77853370253113b1d331e6f45c9c94ec85ed6'],
 'k3_reduction.py':[5178,'d3138f67a9a65d5f240fab64d68093d3833a9ae7c0c6655bc0e1403732e4a18b'],
 'k3_classes.json':[2332920,'e339f0a91bc369b599f7066ffa93075a2321978c3647e738db63195eaa4bc25c']}
BASE=[14595,'160343c32a9362961247308dc845709241b9ef00efa72a716411fbe35dd6590b']
ENV=dict(os.environ,PYTHONHASHSEED='0',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',
         MKL_NUM_THREADS='1',OPENBLAS_CORETYPE='SkylakeX')
def enc(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def put(name,b):
 p=HERE/name
 if p.exists():assert p.read_bytes()==b,('OUTPUT_MISMATCH',name)
 else:p.write_bytes(b)
 return pin(b)
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
 sys.modules[name]=m;spec.loader.exec_module(m);return m
def predicate(row,r):
 return row['kind']=='path_simple_and_quadrivalent_leaf' and row['tree_degrees'][r]==1 and row['primal_degrees'][r]==4

def build(census,base):
 census=Path(census).resolve();a={n:(census/n).read_bytes() for n in PINS}
 for n,b in a.items():assert pin(b)==PINS[n],n
 raw=Path(base).read_bytes();assert pin(raw)==BASE
 C=module('k3_census',census/'k3_census.py');R=module('k3_reduction',census/'k3_reduction.py')
 rows=json.loads(a['k3_domains.json'])['rows'];classes=json.loads(a['k3_classes.json'])['classes']
 chosen=[c for c in classes if predicate(rows[c['representative'][0]],c['representative'][1])]
 assert len(chosen)==186
 target={(row['k3_index'],q['vertex']) for row in rows for q in row['roots'] if q['status']=='open' and predicate(row,q['vertex'])}
 assert len(target)==266
 assert {(m['k3_index'],m['root']) for c in chosen for m in c['members']}==target
 table=''.join(str(k)+': '+' '.join(''.join(map(str,v)) for v in rows[c['representative'][0]]['incidence'])+'\n' for k,c in enumerate(chosen)).encode()
 source=raw.decode()
 changes=[("'native55.txt'","'k3_endpoint_templates.txt'"),
  ("INPUT_PIN=[2630,'58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e']",'INPUT_PIN='+repr(pin(table))),
  ("IDENTITY='MINIMUM_JOINT_MOMENT_V2'",'IDENTITY='+repr(ID)),
  ('assert sorted(d)==list(range(55))','assert sorted(d)==list(range(186))'),
  ('all(1<=r<=8 for r in roots)','all(0<=r<=9 for r in roots)'),
  ('native_index','endpoint_index'),
  ('Requires only the pinned native55.txt.','Requires only the pinned k3_endpoint_templates.txt.'),
  ('not native labels.','not the lexicographic census vertex labels.')]
 for old,new in changes:assert old in source,old;source=source.replace(old,new)
 sources={'k3_endpoint_templates.txt':put('k3_endpoint_templates.txt',table),
          'k3_endpoint_joint.py':put('k3_endpoint_joint.py',source.encode())}
 J=module('k3_endpoint_joint',HERE/'k3_endpoint_joint.py');entries=[]
 for k,c in enumerate(chosen):
  i,r=c['representative'];row=rows[i];path,edges,faces=J.geometry(k);root=path.index(r)
  assert root in (0,9) and c['tree_index']==718 and row['roots'][r]['status']=='open'
  assert edges==list(map(tuple,row['edges']))
  assert {tuple(sorted(path[v] for v in f)) for f in faces}=={tuple(sorted(f)) for f in row['facet_cycles']}
  key,alpha=R.canonical(row,r)
  for m in c['members']:
   dest=rows[m['k3_index']];q=m['root'];other,beta=R.canonical(dest,q);assert key==other and predicate(dest,q)
   p,f,o=R.transport(row,dest,alpha,beta,r,q)
   assert (p,f,o)==(m['vertex_map'],m['facet_map'],m['orientation'])
  entries.append({'endpoint_index':k,'census_index':i,'vertex':r,'path_root':root,'path':path,'rooted_class':c})
 plan={'identity':ID+'_PLAN','base_pin':BASE,'census_pins':PINS,'source_pins':sources,'entries':entries,
       'old_open_positions':11743,'old_open_classes':8739,'domains':2307,
       'known_removed_positions':[[287,6]],'known_removed_class':1491,
       'target_positions':sorted(target),'scope':'Quadrivalent leaves of the complementary path only. True primal facet/tree transport, no full polar-label aliases.'}
 assert len([e for e in entries if e['rooted_class']['class_index']==1491])==1
 print('K3_ALL_QUADRIVALENT_PATH_ENDS_EXACT_CENSUS_PASS',186,266,*put('k3_endpoint_plan.json',enc(plan)),flush=True)
 for n,p in sources.items():print('K3_ENDPOINT_SOURCE_PIN',n,*p,flush=True)

def load():
 b=(HERE/'k3_endpoint_plan.json').read_bytes();p=json.loads(b);assert enc(p)==b and p['identity']==ID+'_PLAN'
 for n,q in p['source_pins'].items():assert pin((HERE/n).read_bytes())==q
 return p

def locate(indices):
 p=load();assert indices and len(indices)==len(set(indices)) and all(0<=i<186 for i in indices)
 for i in indices:
  e=p['entries'][i];assert e['endpoint_index']==i
  name=f'joint_certificate_{i}_matrix.json';dest=HERE/name
  assert not dest.exists(),('EXISTING_CERTIFICATE_DO_NOT_OVERWRITE',i)
  subprocess.run([sys.executable,'k3_endpoint_joint.py','locate',str(i),'matrix',str(e['path_root'])],cwd=HERE,env=ENV,check=True)
  if dest.exists():print('K3_ENDPOINT_LOCATED_AND_EXACT_CHECKED',i,e['rooted_class']['class_index'],*pin(dest.read_bytes()),flush=True)
  else:print('K3_ENDPOINT_UNKNOWN_NOT_EXCLUSION',i,e['rooted_class']['class_index'],flush=True)


def inventory(exact):
 p=load();J=module('k3_endpoint_joint',HERE/'k3_endpoint_joint.py');closed=[];unknown=[];unrun=[];records=[];blocks=0;minors=0
 for e in p['entries']:
  i=e['endpoint_index'];name=f'joint_certificate_{i}_matrix.json';dest=HERE/name
  if not dest.exists():
   (unknown if (HERE/f'joint_proposal_{i}_matrix.json').exists() else unrun).append(i);continue
  b=dest.read_bytes();r=json.loads(b);assert enc(r)==b and r['endpoint_index']==i and r['roots']==[e['path_root']] and r['kind']=='matrix'
  rb=dest.with_suffix('.verified.json').read_bytes();report=json.loads(rb);assert enc(report)==rb and report['record_pin']==pin(b)
  if exact:
   assert enc(J.check(r))==rb
   J.columns.cache_clear();J.build.cache_clear()
  closed.append(i);blocks+=report['blocks'];minors+=report['minors']
  records.append({'endpoint_index':i,'certificate_pin':pin(b),'report_pin':pin(rb),'class_index':e['rooted_class']['class_index']})
 removed={tuple(x) for x in p['known_removed_positions']};cl={p['known_removed_class']}
 for i in closed:
  c=p['entries'][i]['rooted_class'];cl.add(c['class_index']);removed.update((m['k3_index'],m['root']) for m in c['members'])
 out={'identity':ID+'_INVENTORY','plan_pin':pin(enc(p)),'exact_checks_repeated':exact,
      'closed_endpoint_indices':closed,'unknown_endpoint_indices':unknown,'unrun_endpoint_indices':unrun,
      'records':records,'blocks':blocks,'minors':minors,'removed_positions':sorted(removed),'removed_classes':sorted(cl),
      'open_positions':11743-len(removed),'open_classes':8739-len(cl),
      'scope':'Only exact positive records count; unknown and unrun are not exclusions. No global C change. Local inventory is not durable acceptance.'}
 name='k3_endpoint_exact_inventory.json' if exact else 'k3_endpoint_observed_inventory.json'
 (HERE/name).write_bytes(enc(out))
 print('K3_ENDPOINT_INVENTORY',len(closed),len(unknown),len(unrun),len(removed),out['open_positions'],out['open_classes'],blocks,minors,*pin(enc(out)),flush=True)

def main():
 a=sys.argv[1:];assert a
 if a[0]=='build' and len(a)==3:build(a[1],a[2])
 elif a[0]=='locate':locate(list(map(int,a[1:])))
 elif a==['inventory']:inventory(False)
 elif a==['verify']:inventory(True)
 else:raise ValueError('build CENSUS_DIR BASE_SOURCE | locate INDEX... | inventory | verify')
if __name__=='__main__':main()
