# material-e8de65b9498c

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""Exact ledger integration of the already proved literal K3 quadleaf root.
python -S k3_root287_delta.py build|check CENSUS_DIR CERTIFICATE_DIR
All imported sources and recovery inputs are pinned. The inherited census and
class files stay immutable; only an explicitly identified exclusion delta is made.
"""
from pathlib import Path
from collections import Counter
import hashlib,importlib.util,json,sys
assert __debug__ and len(sys.argv)==4 and sys.argv[1] in ('build','check')
HERE=Path(__file__).resolve().parent
CENSUS=Path(sys.argv[2]).resolve();CERT=Path(sys.argv[3]).resolve()
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def enc(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def read(root,name,want):
 b=(root/name).read_bytes();assert pin(b)==want,(name,pin(b),want);return b
PINS={
 'k3_census.py':[13141,'9d87d21a211545b6174a755b75feda6620e3df8ac4074f0e4703cc51bb9be68a'],
 'k3_domains.json':[2724409,'f0fae254b43adff66173b78de6f77853370253113b1d331e6f45c9c94ec85ed6'],
 'k3_reduction.py':[5178,'d3138f67a9a65d5f240fab64d68093d3833a9ae7c0c6655bc0e1403732e4a18b'],
 'k3_classes.json':[2332920,'e339f0a91bc369b599f7066ffa93075a2321978c3647e738db63195eaa4bc25c']}
CPINS={
 'k3_joint_exact.py':[14671,'24b58ea9ff77f522de30fdd3565dfa75ac2dc1dec7729044193f8b114f26ac03'],
 'k3_explicit_templates.txt':[47,'0e808a290a3160e89479e0c27989bfc434c9a311d17276e89090f8b1a8635fbc'],
 'joint_certificate_0_matrix.json':[27698,'ce1f3866d1605f410ca28fe5d47405bc1ac46c2853f612cdb5f4fafde9fa60e3'],
 'joint_certificate_0_matrix.verified.json':[647,'0b74e51166dd120539f72db6feb12307deb4a14fd1765ea846ffde6ac432874b']}
a={n:read(CENSUS,n,p) for n,p in PINS.items()};b={n:read(CERT,n,p) for n,p in CPINS.items()}
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
 sys.modules[name]=m;spec.loader.exec_module(m);return m
C=module('k3_census',CENSUS/'k3_census.py');R=module('k3_reduction',CENSUS/'k3_reduction.py')
J=module('k3_joint_exact',CERT/'k3_joint_exact.py')
rows=json.loads(a['k3_domains.json'])['rows'];classes=json.loads(a['k3_classes.json'])['classes']
inc=[list(map(int,s)) for s in '012 016 023 037 067 1256 2345 3478 458 5678'.split()]
match=[r for r in rows if r['incidence']==inc];assert len(match)==1
row=match[0];i=row['k3_index'];assert i==287 and rows[i]==row
path,edges,faces=J.geometry(0)
assert path==[0,2,3,7,8,9,4,1,5,6] and path[9]==6
assert edges==list(map(tuple,row['edges']))
assert {tuple(sorted(path[v] for v in f)) for f in faces}=={tuple(sorted(f)) for f in row['facet_cycles']}
assert row['roots'][6]=={'status':'open','tree_index':718,'vertex':6}
assert row['primal_degrees'][6]==4 and row['tree_degrees'][6]==1
record=json.loads(b['joint_certificate_0_matrix.json'])
assert record['template_index']==0 and record['roots']==[9] and record['kind']=='matrix'
report=J.check(record);assert enc(report)==b['joint_certificate_0_matrix.verified.json']
assert report['blocks']==137 and report['minors']==1370
cl=[c for c in classes if any(m['k3_index']==i and m['root']==6 for m in c['members'])]
assert len(cl)==1;cl=cl[0]
assert cl['class_index']==1491 and cl['representative']==[287,6] and len(cl['members'])==1
key,labels=R.canonical(row,6)
for m in cl['members']:
 target=rows[m['k3_index']];other,beta=R.canonical(target,m['root']);assert other==key
 p,f,o=R.transport(row,target,labels,beta,6,m['root'])
 assert (p,f,o)==(m['vertex_map'],m['facet_map'],m['orientation'])
old={(r['k3_index'],q['vertex']) for r in rows for q in r['roots'] if q['status']=='open'}
removed={(m['k3_index'],m['root']) for m in cl['members']}
new=old-removed;assert len(old)==11743 and removed=={(287,6)} and len(new)==11742
remaining_classes=[c for c in classes if c['class_index']!=1491]
assert len(classes)==8739 and len(remaining_classes)==8738
assert {(m['k3_index'],m['root']) for c in remaining_classes for m in c['members']}==new
before_domains={i for i,r in old};after_domains={i for i,r in new}
assert before_domains==after_domains and len(after_domains)==1949
out={'identity':'MINIMUM_K3_LITERAL_ROOT287_VERTEX6_INTEGRATED_DELTA_V1',
 'certificate_authority':'[internal-source-reference]','source_pins':PINS,'certificate_pins':CPINS,
 'literal_incidence':inc,'census_index':287,'census_vertex':6,'incident_facets':[2,3,4,5],
 'certificate_template_index':0,'certificate_root_position':9,'certificate_path':path,
 'rooted_class':cl,'removed_positions':sorted(removed),
 'counts':{'old_open_positions':len(old),'open_positions':len(new),'old_open_classes':len(classes),
 'open_classes':len(remaining_classes),'open_incidence_domains':len(after_domains),
 'fully_excluded_incidence_domains':len(rows)-len(after_domains)},
 'remaining_class_kinds':dict(sorted(Counter(c['kind'] for c in remaining_classes).items())),
 'remaining_class_trees':dict(sorted(Counter(c['tree_index'] for c in remaining_classes).items())),
 'exact_report':report,
 'unchanged':['C>=34','no global E17 exclusion','no C34 attainer','Figure650 unverified',
              'inherited raw census and rooted-class files are not rewritten'],
 'scope':'Only the literal (k3_index287,vertex6) position; class1491 is a singleton. No new whole incidence exclusion.'}
data=enc(out);dest=HERE/'k3_root287_delta.json'
if sys.argv[1]=='check' or dest.exists():assert dest.read_bytes()==data
else:dest.write_bytes(data)
print('K3_ROOT287_LITERAL_CERTIFICATE_AND_LEDGER_DELTA_PASS',11742,8738,1949,358,*pin(data),flush=True)
