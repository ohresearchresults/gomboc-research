# material-b9a080a95e0a

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---



# Preserved span 275 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 276 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 277 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 278 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 279 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 280 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 281 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 282 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 283 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 284 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 285 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 286 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 287 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 288 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 289 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 290 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 291 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 292 (literal-source)

```python
"""Full next joint incidence frontier709, with exact automorphism group count.
This is a necessary combinatorial frontier, not a feasibility certificate.
"""
from pathlib import Path
import json,subprocess,sys
import c34_joint48_filter as h
assert __debug__
raw=Path('c34_674_frontier.py').read_bytes()
assert h.pin(raw)==[5046,'0dd9880d4588c5fcf276c181cd29df2616b7ee03d639e26fe7c70e6ff1f6d04c']
s=raw.decode()
patches=[('P=(0,0,1,2,3,4,5,5,5,4)','P=(0,0,1,2,3,4,5,6,6,6)'),('==674','==709'),("len(domains)==167 and Counter(d['facet_tree'] for d in domains)=={253:14,266:77,272:62,278:14}","len(domains)==782 and Counter(d['facet_tree'] for d in domains)=={253:122,266:228,272:310,278:122}")]
for before,after in patches:
 assert s.count(before)==1;s=s.replace(before,after)
s=s.replace('TREE674','TREE709').replace('c34_674_frontier.json','c34_709_frontier.json').replace('ALL_167_DOMAINS','ALL_782_DOMAINS')
Path('c34_709_frontier.py').write_text(s)
subprocess.run([sys.executable,'-S','c34_709_frontier.py'],check=True)
f=Path('c34_709_frontier.json').read_bytes();data=json.loads(f)
cat=Path('c34_catalogue.json').read_bytes()
assert h.pin(cat)==[1111066,'1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77']
maps=json.loads(cat)['slices'][1]['maps'];groups={}
for i,d in enumerate(data['domains']):
 key=(d['map'],min((a[d['root']],tuple(sorted(tuple(sorted((a[u],a[v]))) for u,v in d['primal_edges']))) for a in maps[d['map']]['automorphisms']))
 groups.setdefault(key,[]).append(i)
out=h.serial(dict(identity='C34_TREE709_FULL_FRONTIER_GROUPS_V1',frontier_pin=h.pin(f),counts=data['counts'],groups=list(groups.values()),retained_domains=data['retained_domains'],feasibility_claimed=False))
Path('c34_709_groups.json').write_bytes(out)
print('TREE709_EXACT_GROUPS',len(groups),'DOMAINS',sum(map(len,groups.values())))
for name in ('rebuild_c34_frontier709.py','c34_709_frontier.py','c34_709_frontier.json','c34_709_groups.json'):print(name,*h.pin(Path(name).read_bytes()))
print('C34_TREE709_NEXT_NECESSARY_FRONTIER_PASS')
```


# Preserved span 293 (literal-source)

```python
"""Exact accepted joint43 landscape, leaf groups and next necessary frontier.
Counts of tree placements are not counts of root orbits or physical objects.
"""
from pathlib import Path
from collections import defaultdict
import json
import c34_joint48_filter as h
assert __debug__
pins={
 'c34_joint43_filter.json':[4073764,'3f789af697751bfc53e3a6b33298c4ea36a335973a7c8c0eb433c55daaf3a760'],
 'c34_709_frontier.json':[944857,'7d638f7e452a9fbac4fdd2ac577b34e142178d9f62ff7c6187714efd2b4be040'],
 'c34_709_groups.json':[7416,'561505815c2f3873690c61e3e87b2898683ceb5e9bb501e605f185114fee8e34']}
for n,p in pins.items():assert h.pin(Path(n).read_bytes())==p
x=json.loads(Path('c34_joint43_filter.json').read_bytes())
assert set(x['remaining_vertex_trees'])==set(h.REMAIN)-set(range(671,676))
parents={h.INDEX[c]:h.parent_tuple(c) for c in h.INDEX}
leaves=defaultdict(list);kmin=defaultdict(list)
for t in x['remaining_vertex_trees']:
 p=parents[t];degree=[0]*10
 for i in range(1,10):degree[i]+=1;degree[p[i]]+=1
 ell=sum(d==1 for d in degree)
 leaves[ell].append(t);kmin[ell+int(degree[0]==1)].append(t)
assert {k:len(v) for k,v in leaves.items()}=={2:5,3:21,4:17}
assert {k:len(v) for k,v in kmin.items()}=={2:4,3:13,4:14,5:12}
hits=x['shape_hits'];nexts=[]
for t in sorted(x['remaining_vertex_trees'],key=lambda t:(sum(v.get(str(t),0) for v in hits.values()),t))[:12]:
 counts=[hits[str(k)].get(str(t),0) for k in h.TREES]
 nexts.append(dict(tree=t,parent=parents[t],counts_by_facet_tree=counts,total=sum(counts)))
f=json.loads(Path('c34_709_frontier.json').read_bytes())
g=json.loads(Path('c34_709_groups.json').read_bytes())
assert len(f['domains'])==782 and len(g['groups'])==551
assert sorted(i for group in g['groups'] for i in group)==list(range(782))
out=h.serial(dict(identity='C34_JOINT43_LANDSCAPE_V1',inputs=pins,totals=x['totals'],leaves=dict(leaves),minimum_leaf_window_requirement=dict(kmin),next_shapes=nexts,tree709_state_counts=f['counts'],tree709_retained_domains=len(f['retained_domains']),tree709_representatives=551,feasibility_claimed=False))
Path('joint43_landscape.json').write_bytes(out)
print(out.decode(),end='')
print('C34_JOINT43_LANDSCAPE_EXACT_PASS')
print('OUTPUT',*h.pin(out));print('SOURCE',*h.pin(Path(__file__).read_bytes()))
```


# Preserved span 294 (literal-source)

```python
"""Complete deterministic TREE709 actual-volume moment campaign.
Commands: python replay_c34_709.py prepare|stage1|stage2|freeze|all
No UNKNOWN is accepted as an exclusion; frozen proof uses only stdlib.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
os.environ['OPENBLAS_CORETYPE']='SkylakeX'
from pathlib import Path
import hashlib,json,subprocess,sys
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
INPUTS={
 'c34_674_probe.py':[3895,'53c28448b4dec9cf8f7c4d6935605e2a6e11280fafa07af78cccc8b3faf66223'],
 'c34_674_exact_check.py':[6344,'a19849583af82be178e12b67859b242683980846f07d9853269888a0d6796166'],
 'c34_674_freeze.py':[1855,'d3266c3ae1a185a092b3796387405b6d77ab422fa8f9384fbc83863caa9227dc'],
 'c34_709_frontier.json':[944857,'7d638f7e452a9fbac4fdd2ac577b34e142178d9f62ff7c6187714efd2b4be040'],
 'c34_709_frontier.py':[5050,'f442fc5dd63bf403cf866111ea3b35e02fae74a2eb4c67db54491f56227aa16c'],
 'c34_joint48_filter.py':[6928,'058a5573ffe5a35256c252ea7778f3d0828660cdd74666be3381848134c9a7aa'],
 'c34_catalogue.json':[1111066,'1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77'],
 'ten_successor/work/continue10_cells/coupled.py':[5991,'f5973659810ea240367024f7a46c48f18b82e8866df86a7eba34a809157cf7f1'],
 'ten_successor/work/universal10_engine/engine.py':[5104,'a254810e332f31e5cdae6e88dc05a84c6c9718f2903ef84f6a900668d1b8f226'],
 'ten_successor/work/universal10_engine/fast.py':[2737,'3a54df86eca10711bcddd96099ec8eab9b71a7d4aa0f1a1aadeed6db1fe36f5c']}
for name,want in INPUTS.items():assert pin(Path(name).read_bytes())==want,(name,'INPUT_PIN')
for name in ('c34_674_probe.py','c34_674_exact_check.py','c34_674_freeze.py'):
 s=Path(name).read_text()
 old="[217868,'878a2420cfe3c2bac089385d534e24f593d91d457fa02b4e4110bc5120d091d7']"
 new="[944857,'7d638f7e452a9fbac4fdd2ac577b34e142178d9f62ff7c6187714efd2b4be040']"
 assert s.count(old)==int(not name.endswith('freeze.py'));s=s.replace(old,new)
 s=s.replace('c34_674','c34_709').replace('C34_674','C34_709').replace('TREE674','TREE709').replace('coupled674','coupled709')
 if name.endswith('probe.py'):
  assert s.count('len(gs)==134 and sum(map(len,gs))==167')==1
  s=s.replace('len(gs)==134 and sum(map(len,gs))==167','len(gs)==551 and sum(map(len,gs))==782')
 elif name.endswith('exact_check.py'):
  assert s.count('P=(0,0,1,2,3,4,5,5,5,4)')==1
  s=s.replace('P=(0,0,1,2,3,4,5,5,5,4)','P=(0,0,1,2,3,4,5,6,6,6)').replace('len(domains)==167','len(domains)==782').replace('set(range(167))','set(range(782))')
 else:
  s=s.replace('(0,5,9)','(0,6,9)').replace('(0,1,4,5,9)','(0,1,2,6,9)').replace('[0,0,1,2,3,4,5,5,5,4]','[0,0,1,2,3,4,5,6,6,6]').replace('len(records)==134 and len(attempts)==181','len(records)==551 and 551<=len(attempts)<=1102').replace('134_CERTIFICATES_AND_181_ATTEMPTS','551_CERTIFICATES')
  s=s.replace('0,5,9 ','0,6,9 ').replace('0,1,4,5,9 ','0,1,2,6,9 ')
 Path(name.replace('674','709')).write_text(s)
mode=sys.argv[1] if len(sys.argv)>1 else 'all'
assert mode in ('prepare','stage1','stage2','freeze','all')
if mode=='prepare':
 print('C34_709_THREE_SOURCES_PREPARED_PASS')
 for name in ('replay_c34_709.py','c34_709_probe.py','c34_709_exact_check.py','c34_709_freeze.py'):print(name,*pin(Path(name).read_bytes()))
 raise SystemExit
assert sys.version_info[:3]==(3,12,14)
import numpy,scipy,scipy.linalg,threadpoolctl
assert (numpy.__version__,scipy.__version__,threadpoolctl.__version__)==('2.3.5','1.17.0','3.6.0')
blas=[p for p in threadpoolctl.threadpool_info() if p['internal_api']=='openblas']
assert blas and all(p['version']=='0.3.30' and p['architecture']=='SkylakeX' and p['num_threads']==1 for p in blas)
from c34_709_probe import groups
reps=[g[0] for g in groups()];assert len(reps)==551 and sum(map(len,groups()))==782
if mode in ('stage1','all'):
 subprocess.run([sys.executable,'c34_709_probe.py','0,6,9',','.join(map(str,reps)),'0','12'],check=True)
if mode in ('stage2','all'):
 unknown=[]
 for i in reps:
  r=json.loads(Path('c34_709_d'+str(i)+'_a069_m0.json').read_bytes())
  assert r['status'] in ('EXACT_CERTIFICATE','UNKNOWN')
  if r['status']=='UNKNOWN':unknown.append(i)
 print('STAGE1_UNKNOWN',unknown,flush=True)
 if unknown:subprocess.run([sys.executable,'c34_709_probe.py','0,1,2,6,9',','.join(map(str,unknown)),'0','12'],check=True)
 left=[i for i in unknown if json.loads(Path('c34_709_d'+str(i)+'_a01269_m0.json').read_bytes())['status']!='EXACT_CERTIFICATE']
 print('STAGE2_UNKNOWN',left,flush=True)
 if left:raise SystemExit('UNCLOSED_DOMAINS_NO_WHOLE_TREE_CLAIM')
if mode in ('freeze','all'):
 subprocess.run([sys.executable,'c34_709_freeze.py'],check=True)
 subprocess.run([sys.executable,'-S','c34_709_exact_check.py'],check=True)
 print('C34_709_PROVISIONAL_ENDPOINT_EXACT_CHECK_PASS_NOT_YET_JOURNALED')
```


# Preserved span 295 (literal-source)

```python
"""Complete next joint incidence frontier701 and exact rooted-tree orbits.
No physical feasibility is asserted by this necessary finite catalogue.
"""
from pathlib import Path
from collections import Counter
import json,subprocess,sys
import c34_joint48_filter as h
assert __debug__
raw=Path('c34_674_frontier.py').read_bytes()
assert h.pin(raw)==[5046,'0dd9880d4588c5fcf276c181cd29df2616b7ee03d639e26fe7c70e6ff1f6d04c']
s=raw.decode()
patches=[('P=(0,0,1,2,3,4,5,5,5,4)','P=(0,0,1,2,3,4,5,6,5,5)'),('==674','==701'),("len(domains)==167 and Counter(d['facet_tree'] for d in domains)=={253:14,266:77,272:62,278:14}","len(domains)==1917")]
for before,after in patches:
 assert s.count(before)==1;s=s.replace(before,after)
s=s.replace('TREE674','TREE701').replace('c34_674_frontier.json','c34_701_frontier.json').replace('ALL_167_DOMAINS','ALL_1917_DOMAINS')
Path('c34_701_frontier.py').write_text(s)
subprocess.run([sys.executable,'-S','c34_701_frontier.py'],check=True)
f=Path('c34_701_frontier.json').read_bytes();data=json.loads(f)
cat=Path('c34_catalogue.json').read_bytes()
assert h.pin(cat)==[1111066,'1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77']
maps=json.loads(cat)['slices'][1]['maps'];groups={}
for i,d in enumerate(data['domains']):
 key=(d['map'],min((a[d['root']],tuple(sorted(tuple(sorted((a[u],a[v]))) for u,v in d['primal_edges']))) for a in maps[d['map']]['automorphisms']))
 groups.setdefault(key,[]).append(i)
out=h.serial(dict(identity='C34_TREE701_FULL_FRONTIER_GROUPS_V1',frontier_pin=h.pin(f),counts=data['counts'],groups=list(groups.values()),retained_domains=data['retained_domains'],feasibility_claimed=False))
Path('c34_701_groups.json').write_bytes(out)
print('TREE701_EXACT_GROUPS',len(groups),'DOMAINS',sum(map(len,groups.values())))
print('BY_FACET_TREE',dict(Counter(d['facet_tree'] for d in data['domains'])))
for name in ('rebuild_c34_frontier701.py','c34_701_frontier.py','c34_701_frontier.json','c34_701_groups.json'):print(name,*h.pin(Path(name).read_bytes()))
print('C34_TREE701_NEXT_NECESSARY_FRONTIER_PASS')
```


# Preserved span 296 (literal-source)

```python
"""Freeze all TREE709 domains using exact decimal coarsening of certificates.
This alters coefficients only after exact PD checks; no numerical tolerance.
Run after all first-stage and all required second-stage probe records exist.
"""
from pathlib import Path
import json,sys,subprocess
import c34_joint48_filter as h
from c34_709_probe import groups,c
assert __debug__
def rounded(v,d):
 sign=-1 if v<0 else 1;q,r=divmod(abs(v),d)
 return sign*(q+int(2*r>d or (2*r==d and q%2==1)))
def main():
 records=[];attempts=[];divisors={}
 for group in groups():
  index=group[0];chosen=None
  for apices in ((0,6,9),(0,1,2,6,9)):
   name='c34_709_d'+str(index)+'_a'+''.join(map(str,apices))+'_m0.json'
   raw=Path(name).read_bytes();r=json.loads(raw)
   assert r['index']==index and r['actual_apices']==list(apices) and r['fan_mode']==0 and r['maxouter']==12
   assert r['status'] in ('EXACT_CERTIFICATE','UNKNOWN')
   attempts.append(dict(index=index,actual_apices=apices,status=r['status'],source_file=name,source_pin=h.pin(raw)))
   if r['status']=='EXACT_CERTIFICATE':chosen=r;break
  assert chosen is not None,('UNCLOSED_DOMAIN',index)
  cert=chosen['certificate'];assert cert['identity']=='C34_709_ACTUAL_SHARED_TETRA_PATTERNS_V1' and cert['parent']==[0,0,1,2,3,4,5,6,6,6]
  assert not cert['mass_cut'] and not cert['scalar_forms'] and not cert['norms']
  assert cert['apices']==list(range(len(apices)))
  original=cert['z'];assert all(type(v)==int for v in original)
  original_audit=cert['audit'];assert c.audit(cert)==original_audit
  for power in range(len(str(max(map(abs,original)))),-1,-1):
   divisor=10**power;cert['z']=[rounded(v,divisor) for v in original]
   try:audit=c.audit(cert)
   except AssertionError:continue
   break
  else:raise AssertionError('ORIGINAL_CERTIFICATE_LOST')
  divisors[divisor]=divisors.get(divisor,0)+1
  records.append(dict(index=index,fan_apices=apices,fan_mode=0,z=cert['z'],expected_audit=audit,exact_coarsening_divisor=divisor))
  print('COARSENED',index,divisor,audit,flush=True)
 assert len(records)==551 and 551<=len(attempts)<=1102
 out=h.serial(dict(identity='C34_709_FROZEN_ACTUAL_MOMENT_CERTIFICATES_V1',records=records))
 Path('c34_709_certificates.json').write_bytes(out)
 discovery=h.serial(dict(identity='C34_709_EXACT_COMPACT_DISCOVERY_LEDGER_V1',attempts=attempts,groups=groups(),divisor_counts=divisors,replay_commands=['python replay_c34_709.py stage1','python replay_c34_709.py stage2','python c34_709_freeze_compact.py'],coarsening='Largest passing decimal divisor, exact ties-to-even; B-I strictly positive definite by Bareiss and Fraction LDL.'))
 Path('c34_709_discovery.json').write_bytes(discovery)
 print('C34_709_ALL_551_CERTIFICATES_EXACTLY_COARSENED_PASS',divisors,flush=True)
 subprocess.run([sys.executable,'-S','c34_709_exact_check.py'],check=True)
 for name in ('c34_709_freeze_compact.py','c34_709_certificates.json','c34_709_discovery.json','c34_709_exact_report.json'):print(name,*h.pin(Path(name).read_bytes()))
 print('C34_709_COMPACT_ENDPOINT_EXACT_CHECK_PASS_NOT_YET_JOURNALED')
if __name__=='__main__':main()
```


# Preserved span 297 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 298 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 299 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 300 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 301 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 302 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 303 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 304 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 305 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 306 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 307 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 308 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 309 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 310 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 311 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 312 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 313 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 314 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 315 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 316 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 317 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 318 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 319 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 320 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 321 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 322 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 323 (literal-source)

```python
"""Exact uniform separation extracted from the accepted TREE709 certificates.
Output bounds the normalized violation of the full necessary signed-shadow system.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import c34_709_exact_check as e
import c34_joint48_filter as h
assert __debug__
raw=Path('c34_709_certificates.json').read_bytes()
assert h.pin(raw)==[1993377,'2915c7113c1b8c2c75f867a91a31fc8c7678f4cb97c2252564f7959bf84d60b7']
records=json.loads(raw)['records'];out=[]
for rec in records:
 pats,arcs,order=e.model(e.domains[rec['index']],rec['fan_apices'],rec['fan_mode'])
 m=len(arcs);start=10*len(rec['fan_apices']);z=rec['z']
 sums=[sum(z[start+m*k:start+m*(k+1)]) for k in range(len(pats))]
 assert all(type(x)==int and x>=0 for x in sums)
 M=max(sums);assert M>0
 out.append(dict(index=rec['index'],max_block_multiplier_sum=M,strict_shadow_violation_lower_bound=[1,2*M]))
maximum=max(r['max_block_multiplier_sum'] for r in out)
report=json.loads(Path('c34_709_exact_report.json').read_bytes())
assert h.pin(Path('c34_709_exact_report.json').read_bytes())==[210515,'1c8951e37a5e8782d629837d5f127dcaeb89dadb939cb1b9ad0e3bd2312e581e']
assert report['whole_tree_excluded'] and len(report['coverage'])==782
byid={r['index']:r for r in out}
assert set(byid)=={r['index'] for r in report['results']}
for row in report['coverage']:assert row['certificate_index'] in byid
output=h.serial(dict(identity='C34_709_EXACT_SIGNED_SHADOW_SEPARATION_V1',certificate_pin=h.pin(raw),records=out,covered_domains=782,max_block_multiplier_sum=maximum,uniform_strict_lower_bound=[1,2*maximum],normalization='D_ij=x_i^T M(x_j-x_i); divide by tr(X M X^T). Violation=max_e(-sign_e*D_e).',interpretation='Full necessary signed-arrow system for these782 domains; not a global C34 approximate-equilibrium or centroid-error bound.'))
Path('c34_709_quantitative.json').write_bytes(output)
print('UNIFORM_SIGNED_SHADOW_VIOLATION_STRICTLY_GREATER_THAN',F(1,2*maximum))
print('C34_709_ALL782_DOMAINS_EXACT_QUANTITATIVE_SEPARATION_PASS')
print('SOURCE',*h.pin(Path(__file__).read_bytes()));print('OUTPUT',*h.pin(output))
```


# Preserved span 324 (literal-source)

```python
"""Exact current joint42 landscape and full prepared TREE701 frontier."""
from pathlib import Path
from collections import defaultdict
import json
import c34_joint48_filter as h
assert __debug__
pins={
 'c34_joint42_filter.json':[4073587,'588154dcf31841f96468ba114a612064fe6868163a64e12a582c4690058119e4'],
 'c34_701_frontier.json':[2246318,'bf3512f2fdbe7fd0e378499fb83a978afbe89183f2db3df06833984e1c68014c'],
 'c34_701_groups.json':[19795,'389ba41345dc581ebe5a2369e7f503c38a9ea793c30bbd40225ce28c5f376e69']}
for name,pin in pins.items():assert h.pin(Path(name).read_bytes())==pin
x=json.loads(Path('c34_joint42_filter.json').read_bytes())
assert set(x['remaining_vertex_trees'])==set(h.REMAIN)-{671,672,673,674,675,709}
parents={h.INDEX[c]:h.parent_tuple(c) for c in h.INDEX}
leaves=defaultdict(list);kmin=defaultdict(list)
for t in x['remaining_vertex_trees']:
 p=parents[t];degree=[0]*10
 for i in range(1,10):degree[i]+=1;degree[p[i]]+=1
 ell=sum(d==1 for d in degree)
 leaves[ell].append(t);kmin[ell+int(degree[0]==1)].append(t)
assert {k:len(v) for k,v in leaves.items()}=={2:5,3:21,4:16}
assert {k:len(v) for k,v in kmin.items()}=={2:4,3:13,4:14,5:11}
hits=x['shape_hits'];nexts=[]
for t in sorted(x['remaining_vertex_trees'],key=lambda t:(sum(v.get(str(t),0) for v in hits.values()),t))[:12]:
 counts=[hits[str(k)].get(str(t),0) for k in h.TREES]
 nexts.append(dict(tree=t,parent=parents[t],counts_by_facet_tree=counts,total=sum(counts)))
f=json.loads(Path('c34_701_frontier.json').read_bytes());g=json.loads(Path('c34_701_groups.json').read_bytes())
assert len(f['domains'])==1917 and len(g['groups'])==1265
assert sorted(i for group in g['groups'] for i in group)==list(range(1917))
out=h.serial(dict(identity='C34_JOINT42_LANDSCAPE_V1',inputs=pins,totals=x['totals'],leaves=dict(leaves),minimum_leaf_window_requirement=dict(kmin),next_shapes=nexts,tree701_state_counts=f['counts'],tree701_retained_domains=len(f['retained_domains']),tree701_representatives=1265,feasibility_claimed=False))
Path('joint42_landscape.json').write_bytes(out)
print(out.decode(),end='');print('C34_JOINT42_LANDSCAPE_EXACT_PASS')
print('OUTPUT',*h.pin(out));print('SOURCE',*h.pin(Path(__file__).read_bytes()))
```


# Preserved span 325 (literal-source)

```python
"""Deterministic actual-volume moment campaign for the literal joint tree701.
Commands: python replay_c34_701.py prepare|stage1|stage2|freeze|all
UNKNOWN is never an exclusion. The frozen proof is independently checked.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
 os.environ[key]='1'
os.environ['OPENBLAS_CORETYPE']='SkylakeX'
from pathlib import Path
import hashlib,json,subprocess,sys
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
INPUTS={
 'c34_709_probe.py':[3895,'a7a26766887de6d48b5ee34d7ec1c1cee5e5b3afc735ece6bcdfaad0ffb90f0f'],
 'c34_709_exact_check.py':[6344,'b9d5a3be5c78b1146dab0144ae26f225e2c239d6130ed8f9ce31f4a3dd9a77da'],
 'c34_709_freeze_compact.py':[3090,'6455578409427834690c66b436b19e5bb68e1333a85b6c24b26e5ac09e942e52'],
 'c34_701_frontier.py':[4971,'75b0f87ede6f036749f134058299e6bcd1f31aa1e3b2e4e571fe21e7b7e3a3ff'],
 'c34_701_frontier.json':[2246318,'bf3512f2fdbe7fd0e378499fb83a978afbe89183f2db3df06833984e1c68014c'],
 'c34_joint48_filter.py':[6928,'058a5573ffe5a35256c252ea7778f3d0828660cdd74666be3381848134c9a7aa'],
 'c34_catalogue.json':[1111066,'1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77'],
 'ten_successor/work/continue10_cells/coupled.py':[5991,'f5973659810ea240367024f7a46c48f18b82e8866df86a7eba34a809157cf7f1'],
 'ten_successor/work/universal10_engine/engine.py':[5104,'a254810e332f31e5cdae6e88dc05a84c6c9718f2903ef84f6a900668d1b8f226'],
 'ten_successor/work/universal10_engine/fast.py':[2737,'3a54df86eca10711bcddd96099ec8eab9b71a7d4aa0f1a1aadeed6db1fe36f5c']}
for name,want in INPUTS.items():assert pin(Path(name).read_bytes())==want,(name,'INPUT_PIN')
def replace_once(s,a,b):
 assert s.count(a)==1,(a,s.count(a))
 return s.replace(a,b)
for name in ('c34_709_probe.py','c34_709_exact_check.py','c34_709_freeze_compact.py'):
 s=Path(name).read_text()
 if not name.endswith('compact.py'):
  s=replace_once(s,"[944857,'7d638f7e452a9fbac4fdd2ac577b34e142178d9f62ff7c6187714efd2b4be040']","[2246318,'bf3512f2fdbe7fd0e378499fb83a978afbe89183f2db3df06833984e1c68014c']")
 if name.endswith('probe.py'):
  s=replace_once(s,'len(gs)==551 and sum(map(len,gs))==782','len(gs)==1265 and sum(map(len,gs))==1917')
 elif name.endswith('exact_check.py'):
  s=replace_once(s,'P=(0,0,1,2,3,4,5,6,6,6)','P=(0,0,1,2,3,4,5,6,5,5)')
  s=replace_once(s,'len(domains)==782','len(domains)==1917')
  s=s.replace('range(782)','range(1917)')
 else:
  s=replace_once(s,'((0,6,9),(0,1,2,6,9))','((0,5,7),(0,1,3,5,7))')
  s=replace_once(s,'[0,0,1,2,3,4,5,6,6,6]','[0,0,1,2,3,4,5,6,5,5]')
  s=replace_once(s,'len(records)==551 and 551<=len(attempts)<=1102','len(records)==1265 and 1265<=len(attempts)<=2530')
  s=s.replace('ALL_551_CERTIFICATES','ALL_1265_CERTIFICATES')
 s=s.replace('c34_709','c34_701').replace('C34_709','C34_701').replace('TREE709','TREE701').replace('coupled709','coupled701')
 Path(name.replace('709','701')).write_text(s)
mode=sys.argv[1] if len(sys.argv)>1 else 'all'
assert mode in ('prepare','stage1','stage2','freeze','all')
if mode=='prepare':
 print('C34_701_THREE_SOURCES_PREPARED_PASS')
 for name in ('replay_c34_701.py','c34_701_probe.py','c34_701_exact_check.py','c34_701_freeze_compact.py'):print(name,*pin(Path(name).read_bytes()))
 raise SystemExit
if mode!='freeze':
 assert sys.version_info[:3]==(3,12,14)
 import numpy,scipy,scipy.linalg,threadpoolctl
 assert (numpy.__version__,scipy.__version__,threadpoolctl.__version__)==('2.3.5','1.17.0','3.6.0')
 blas=[p for p in threadpoolctl.threadpool_info() if p['internal_api']=='openblas']
 assert blas and all(p['version']=='0.3.30' and p['architecture']=='SkylakeX' and p['num_threads']==1 for p in blas)
from c34_701_probe import groups
reps=[g[0] for g in groups()]
assert len(reps)==1265 and sum(map(len,groups()))==1917
if mode in ('stage1','all'):
 subprocess.run([sys.executable,'c34_701_probe.py','0,5,7',','.join(map(str,reps)),'0','12'],check=True)
if mode in ('stage2','all'):
 unknown=[]
 for i in reps:
  r=json.loads(Path('c34_701_d'+str(i)+'_a057_m0.json').read_bytes())
  assert r['status'] in ('EXACT_CERTIFICATE','UNKNOWN')
  if r['status']=='UNKNOWN':unknown.append(i)
 print('STAGE1_UNKNOWN',unknown,flush=True)
 if unknown:subprocess.run([sys.executable,'c34_701_probe.py','0,1,3,5,7',','.join(map(str,unknown)),'0','12'],check=True)
 left=[i for i in unknown if json.loads(Path('c34_701_d'+str(i)+'_a01357_m0.json').read_bytes())['status']!='EXACT_CERTIFICATE']
 print('STAGE2_UNKNOWN',left,flush=True)
 if left:raise SystemExit('UNCLOSED_DOMAINS_NO_WHOLE_TREE_CLAIM')
if mode in ('freeze','all'):
 subprocess.run([sys.executable,'c34_701_freeze_compact.py'],check=True)
 print('C34_701_PROVISIONAL_ENDPOINT_EXACT_CHECK_PASS_NOT_YET_JOURNALED')
```


# Preserved span 326 (literal-source)

```python
"""Exact constants for the centroid/signed-shadow certificate tradeoff.
The proof is the actual-fan identity in the research journal. Standard library.
These constants concern the full frozen necessary signed-shadow list.
"""
from pathlib import Path
from math import isqrt
import json
import c34_joint48_filter as h
import c34_709_exact_check as ck
assert __debug__
INPUTS={
 'c34_joint48_filter.py':[6928,'058a5573ffe5a35256c252ea7778f3d0828660cdd74666be3381848134c9a7aa'],
 'c34_709_exact_check.py':[6344,'b9d5a3be5c78b1146dab0144ae26f225e2c239d6130ed8f9ce31f4a3dd9a77da'],
 'c34_709_certificates.json':[1993377,'2915c7113c1b8c2c75f867a91a31fc8c7678f4cb97c2252564f7959bf84d60b7'],
 'c34_709_exact_report.json':[210515,'1c8951e37a5e8782d629837d5f127dcaeb89dadb939cb1b9ad0e3bd2312e581e'],
 'c34_709_frontier.json':[944857,'7d638f7e452a9fbac4fdd2ac577b34e142178d9f62ff7c6187714efd2b4be040'],
 'c34_catalogue.json':[1111066,'1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77']}
for name,want in INPUTS.items():assert h.pin(Path(name).read_bytes())==want,name
certs=json.loads(Path('c34_709_certificates.json').read_bytes())['records']
report=json.loads(Path('c34_709_exact_report.json').read_bytes())
assert report['uncovered_domains']==[] and len(report['coverage'])==782
assert len(certs)==551
rows=[]
for r in certs:
 pats,arcs,order=ck.model(ck.domains[r['index']],r['fan_apices'],r['fan_mode'])
 A=len(r['fan_apices']);m=len(arcs);z=r['z'];end=10*A+m*len(pats)
 assert len(z)==end+56*(A-1) and all(type(t)==int for t in z)
 assert min(z[10*A:end])>=0
 gamma=[sum(z[10*a+i] for a in range(A)) for i in range(10)]
 q=sum(v*v for v in gamma);assert q>0
 k=max(sum(z[10*A+m*t:10*A+m*(t+1)]) for t in range(len(pats)))
 assert k>0
 b=isqrt(q);b+=int(b*b<q)
 assert (b-1)**2<q<=b*b
 rows.append(dict(index=r['index'],gamma_sum=gamma,gamma_norm_squared=q,
  gamma_norm_integer_upper=b,maximum_shadow_multiplier_sum=k,
  centroid_ratio_strict_lower_if_all_signed_shadows_hold_squared=[1,64*q],
  centroid_ratio_rational_strict_lower_if_all_signed_shadows_hold=[1,8*b]))
by_id={r['index']:r for r in rows}
assert len(by_id)==551 and all(c['certificate_index'] in by_id for c in report['coverage'])
qmax=max(r['gamma_norm_squared'] for r in rows)
kmax=max(r['maximum_shadow_multiplier_sum'] for r in rows)
bmax=isqrt(qmax);bmax+=int(bmax*bmax<qmax)
assert qmax==6845021155266 and kmax==36881720 and bmax==2616300
out=h.serial(dict(identity='C34_709_CENTROID_SIGNED_SHADOW_TRADEOFF_V1',
 inputs=INPUTS,records=rows,coverage=report['coverage'],
 maximum_gamma_norm_squared=qmax,maximum_gamma_norm_integer_upper=bmax,
 maximum_shadow_multiplier_sum=kmax,
 uniform_rational_tradeoff=dict(centroid_coefficient=8*bmax,shadow_coefficient=2*kmax,strict_lower=1),
 normalization='eta=norm_M(g)/sqrt(sum_i norm_M(x_i)^2); epsilon=max(0,max_e(-s_e D_e))/sum_i norm_M(x_i)^2',
 scope='Full frozen signed-shadow systems; additional redirected negative signs are not automatic for arbitrary reference-centre 110 bodies.',
 number_of_certificates=len(rows),number_of_domains=len(report['coverage'])))
Path('c34_709_centroid_shadow_tradeoff.json').write_bytes(out)
print('C34_709_ALL782_DOMAINS_CENTROID_SHADOW_TRADEOFF_EXACT_PASS')
print('UNIFORM_STRICT_TRADEOFF',8*bmax,'eta +',2*kmax,'epsilon > 1')
print('OUTPUT',*h.pin(out));print('SOURCE',*h.pin(Path(__file__).read_bytes()))
```


# Preserved span 327 (literal-source)

```python
"""Sound common signs across every surviving state in each exact moment group.
All changes of vertex labels are actual rooted-map automorphisms.
"""
from pathlib import Path
from collections import Counter
import json
import c34_joint48_filter as h
import c34_701_exact_check as ck
assert __debug__
PINS={
 'c34_701_frontier.json':[2246318,'bf3512f2fdbe7fd0e378499fb83a978afbe89183f2db3df06833984e1c68014c'],
 'c34_701_groups.json':[19795,'389ba41345dc581ebe5a2369e7f503c38a9ea793c30bbd40225ce28c5f376e69'],
 'c34_701_joint_redirect.json':[798098,'2f8bf91007fdb6a270fcf5d94069f61f9cd4d02127b9f93f392e2ff1edbc5577'],
 'c34_catalogue.json':[1111066,'1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77'],
 'c34_joint48_filter.py':[6928,'058a5573ffe5a35256c252ea7778f3d0828660cdd74666be3381848134c9a7aa'],
 'c34_701_exact_check.py':[6347,'6664fddb3ca52621df15d298a16099543d5e596b525617a56507da157bfcd81b']}
for name,want in PINS.items():assert h.pin(Path(name).read_bytes())==want,name
domains=json.loads(Path('c34_701_frontier.json').read_bytes())['domains']
groups=json.loads(Path('c34_701_groups.json').read_bytes())['groups']
redirect=json.loads(Path('c34_701_joint_redirect.json').read_bytes())
rr={(r['domain'],r['state']):r for r in redirect['records']}
assert len(rr)==9837
maps=json.loads(Path('c34_catalogue.json').read_bytes())['slices'][1]['maps']
rows=[];counts=Counter()
for group in groups:
 rep=group[0];target=domains[rep];root=target['root']
 inv={old:new for new,old in enumerate(target['new_to_old'])}
 tree={tuple(e) for e in target['primal_edges']}
 common=None;witnesses=[];domain_rows=[]
 _,baseline,_=ck.model(target,[0,5,7],0)
 for di in group:
  d=domains[di];assert d['map']==target['map']
  autos=[a for a in maps[d['map']]['automorphisms'] if a[d['root']]==root and {tuple(sorted((a[u],a[v]))) for u,v in d['primal_edges']}==tree]
  assert autos
  a=min(autos);pi=[inv[a[i]] for i in range(10)]
  assert sorted(pi)==list(range(10))
  domain_common=None
  for si,st in enumerate(d['states']):
   if st['reason']!='retained':continue
   row=rr[di,si]
   if row['excluded']:
    counts['excluded_states']+=1;continue
   counts['retained_states']+=1
   signs={(pi[i],pi[j],1) for i,js in enumerate(st['forced_primal']) for j in js}
   signs.update((pi[r['arrow'][0]],pi[r['arrow'][1]],-1) for r in row['new_negative'])
   common=signs if common is None else common&signs
   domain_common=signs if domain_common is None else domain_common&signs
   witnesses.append(dict(domain=di,state=si,old_to_representative_new=pi))
  assert domain_common is not None
  domain_new=sorted(domain_common-set(baseline))
  counts['domains']+=1
  if domain_new:counts['domains_with_new_common_signs']+=1
  counts['domain_new_common_signs']+=len(domain_new)
  domain_rows.append(dict(domain=di,new_common_signs=domain_new))
 assert common is not None and witnesses
 new=sorted(common-set(baseline))
 counts['groups']+=1;counts['new_signs']+=len(new)
 if new:counts['groups_with_new_signs']+=1
 counts['new_positive']+=sum(s==1 for _,_,s in new)
 counts['new_negative']+=sum(s==-1 for _,_,s in new)
 rows.append(dict(index=rep,domains=group,new_common_signs=new,per_domain_common_signs=domain_rows,state_transports=witnesses))
assert counts['groups']==1265 and counts['retained_states']==9823 and counts['excluded_states']==14
out=h.serial(dict(identity='C34_701_COMMON_SURVIVING_STATE_SIGNS_V1',inputs=PINS,counts=dict(sorted(counts.items())),records=rows))
Path('c34_701_common_state_signs.json').write_bytes(out)
print('C34_701_COMMON_SURVIVING_STATE_SIGNS_EXACT_PASS',dict(counts))
print('OUTPUT',*h.pin(out));print('SOURCE',*h.pin(Path(__file__).read_bytes()))
```


# Preserved span 328 (literal-source)

```python
"""Complete next joint incidence frontier669 and exact rooted-map groups.
No physical feasibility follows from survival in this finite necessary cover.
"""
from pathlib import Path
from collections import Counter
import json,subprocess,sys
import c34_joint48_filter as h
assert __debug__
raw=Path('c34_674_frontier.py').read_bytes()
assert h.pin(raw)==[5046,'0dd9880d4588c5fcf276c181cd29df2616b7ee03d639e26fe7c70e6ff1f6d04c']
s=raw.decode()
patches=[('P=(0,0,1,2,3,4,5,5,5,4)','P=(0,0,1,2,3,4,5,5,4,8)'),('==674','==669'),("len(domains)==167 and Counter(d['facet_tree'] for d in domains)=={253:14,266:77,272:62,278:14}","len(domains)==2971")]
for before,after in patches:
 assert s.count(before)==1;s=s.replace(before,after)
s=s.replace('TREE674','TREE669').replace('c34_674_frontier.json','c34_669_frontier.json').replace('ALL_167_DOMAINS','ALL_2971_DOMAINS')
Path('c34_669_frontier.py').write_text(s)
subprocess.run([sys.executable,'-S','c34_669_frontier.py'],check=True)
f=Path('c34_669_frontier.json').read_bytes();data=json.loads(f)
cat=Path('c34_catalogue.json').read_bytes()
assert h.pin(cat)==[1111066,'1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77']
maps=json.loads(cat)['slices'][1]['maps'];groups={}
for i,d in enumerate(data['domains']):
 key=(d['map'],min((a[d['root']],tuple(sorted(tuple(sorted((a[u],a[v]))) for u,v in d['primal_edges']))) for a in maps[d['map']]['automorphisms']))
 groups.setdefault(key,[]).append(i)
out=h.serial(dict(identity='C34_TREE669_FULL_FRONTIER_GROUPS_V1',frontier_pin=h.pin(f),counts=data['counts'],groups=list(groups.values()),retained_domains=data['retained_domains'],feasibility_claimed=False))
Path('c34_669_groups.json').write_bytes(out)
print('TREE669_EXACT_GROUPS',len(groups),'DOMAINS',sum(map(len,groups.values())))
print('BY_FACET_TREE',dict(Counter(d['facet_tree'] for d in data['domains'])))
for name in ('rebuild_c34_frontier669.py','c34_669_frontier.py','c34_669_frontier.json','c34_669_groups.json'):print(name,*h.pin(Path(name).read_bytes()))
print('C34_TREE669_NEXT_NECESSARY_FRONTIER_PASS')
```


# Preserved span 329 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 330 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 331 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 332 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 333 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 334 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 335 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 336 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 337 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 338 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 339 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 340 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 341 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 342 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 343 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 344 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 345 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 346 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 347 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 348 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 349 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 350 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]
