# material-2e6f673714f0

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""TREE253_K2_COVERAGE278_V1: exact delta from the accepted246 theorem.
Commands, assertions enabled:
  python recover_affine15_17.py recover 15
  python recover_affine15_17.py recover 17
  python -S coverage278.py
  python -S coverage278.py --verify
The six original pinned sources and deterministic environment are specified in
[internal-source-reference]. No old coefficient array or sandbox is an input.
The246 theorem is inherited from [internal-source-reference], not rerun here.
The new certificates are checked by integer Bareiss AND rational Schur.
Only genuine maximal-facet/path transports are used; full pole graphs are NOT
identified. Endpoint exclusions are inherited separately at each native row.
The resulting278 positions are NOT278 global combinatorial types.
"""
from pathlib import Path
import hashlib,json,sys
assert __debug__
HERE=Path(__file__).resolve().parent
PINS={
'flip_moments.py':[13811,'7542ef43f2e0e5b4759f076086c8de3539da8ef5051c80dae2a71e778a21faa7'],
'native55.txt':[2630,'58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e'],
'affine_moments.py':[5980,'fa8371daf690ac9ff0a9a61b3ad8e8ca2dc6652b2a0f76cc70826163fff01805'],
'common_roots.py':[6011,'4d3e16daf49c9dbb4c4d5a88fce37f0337409502be51f1049ceaac3f6c4f0d62'],
'affine_roots.py':[1541,'d0866dbf849c91fd39fec55b162ad74f319eade5180c878f7209713f5d249576'],
'recover_affine15_17.py':[3808,'cb189f2e4fd6676253586320f2355736daa0bfb53f3b398de5ce560533b21a1f']}
def pin(b):return[len(b),hashlib.sha256(b).hexdigest()]
for name,p in PINS.items():assert pin((HERE/name).read_bytes())==p,name
# The adapter has a command-line main; execute its checks only through the
# original recovery driver in a fresh process to avoid altering literal IDs.
import subprocess
import flip_moments as fm
import recover_affine15_17 as rec
W06=[4,8,9,10,11,13,14,15,17,19,20,24,25,26,39,41,43,44,46,48]
OPEN26=[15,17,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,43,44,48,51,52,53,54]
PAIRS=[(15,19),(17,20)]
P=[0,8,4,9,7,6,2,5,1,3]
FP=[4,3,2,1,0,7,8,5,6]
def build():
 oldwhole=list(range(15))+[16,18]
 old={(i,r) for i in range(55) for r in range(10) if i in oldwhole or r in (0,9)}
 assert len(old)==246
 covered=set(old);transports=[];reports=[];data=fm.inputs()
 for a,b in PAIRS:
  subprocess.run([sys.executable,'-S',str(HERE/'recover_affine15_17.py'),'verify',str(a)],check=True)
  record=json.loads((HERE/f'affine_certificate_{a}_root.json').read_bytes())
  report=json.loads((HERE/f'affine_certificate_{a}_root.verified.json').read_bytes())
  assert record['identity']=='ALL_AFFINE_SIMPLEX_AFFINE_ROOTS_V1'
  assert report['roots']==list(range(1,9)) and record['mode']=='root'
  assert report['total_leading_minors']==report['total_blocks']*10
  reports.append({'native_index':a,'record_pin':rec.EXPECTED[a]['record'],
      'report_pin':rec.EXPECTED[a]['report'],'blocks':report['total_blocks'],
      'leading_minors':report['total_leading_minors']})
  pa,ea,fa=fm.geometry(data[a]);pb,eb,fb=fm.geometry(data[b])
  assert sorted(P)==list(range(10))
  assert all(P[pa[j]]==pb[9-j] for j in range(10))
  assert sorted(tuple(sorted((P[i],P[j]))) for i,j in ea)==eb
  for f,cy in enumerate(fa):
   assert {P[pa[v]] for v in cy}=={pb[v] for v in fb[FP[f]]}
  transports.append({'source':a,'target':b,'vertex_permutation':P,'facet_permutation':FP,
      'source_path':pa,'target_path':pb,'root_position_map':list(reversed(range(10)))})
  covered.update((i,r) for i in (a,b) for r in range(1,9))
 universe={(i,r) for i in range(55) for r in range(10)}
 added=sorted(covered-old);remaining=sorted(universe-covered)
 whole=[i for i in range(55) if all((i,r) in covered for r in range(10))]
 wclosed=sorted(q for q in covered if q[0] in W06)
 wopen=sorted(q for q in universe-covered if q[0] in W06)
 reps=[i for i in OPEN26 if i not in (15,17)]
 assert len(added)==32 and len(covered)==278 and len(remaining)==272
 assert whole==list(range(21)) and len(whole)==21
 assert len(wclosed)==128 and len(wopen)==72 and len(reps)==24
 assert sum(r['blocks'] for r in reports)==2200
 return fm.enc({'identity':'TREE253_K2_COVERAGE278_V1',
   'inherited246_source':'[internal-source-reference]',
   'exact_object_recovery_source':'[internal-source-reference]',
   'physical_moment_proof':'[internal-source-reference]',
   'native_endpoint_and_path_authority':'minimum-0078',
   'whole_native_rows':whole,'excluded':sorted(covered),'remaining':remaining,'new32':added,
   'direct_matrix_reports':reports,'actual_facet_path_transports':transports,
   'open_class_representatives':reps,
   'w06':{'excluded':wclosed,'remaining':wopen,'whole':[i for i in W06 if i in whole]},
   'scope':'native incidence/root POSITION domains; NOT global types',
   'unchanged':['C>=34','global632_types_52585_joint_roots','TREE410_17383_of_24847'],
   'excluded_unpersisted_candidates':['archived_native21_and23_vector_certificates']})
if __name__=='__main__':
 assert sys.argv[1:] in ([],['--verify'])
 b=build();p=HERE/'coverage278.json'
 if sys.argv[1:]:assert p.read_bytes()==b
 else:p.write_bytes(b)
 print('TREE253_K2_COVERAGE278_EXACT_PASS 246 32 278 272 21 128 72 24')
 print('OUTPUT',*pin(b))
