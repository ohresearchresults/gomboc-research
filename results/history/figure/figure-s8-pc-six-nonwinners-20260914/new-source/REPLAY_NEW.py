"""Cold exact replay against golden records, not a numerical search or winner claim.
Requires the already journal-persisted 30-file S8 source capsule at ./source.
Usage: python -B -S REPLAY_NEW.py OBJECT OUT STAGE
OBJECT: DEL99 DEL117 DEL84 CONTACT120 PC3 CONTACT_RPC; STAGE: A B MASS FINISH.
"""
import sys,json,hashlib,types
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'source'))
import REPLAY,RECONSTRUCT,verify_family
C=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def definition(name):
 if name in ('PC3','CONTACT_RPC'):
  src='DEL99_PC3' if name=='PC3' else 'CONTACT120_RPC1'
  return json.loads((R/src/'GENERATOR.json').read_text())
 d=REPLAY.generator('S8')
 if name.startswith('DEL'):d['active_ids']=[i for i in range(137) if i!=int(name[3:])]
 else:
  assert name=='CONTACT120' and len(d['controls'])==179 and len(d['groups'])==42
  factor=10**12//d['grid'];d['controls']=[[x*factor for x in row] for row in d['controls']];d['grid']=10**12
  d['controls'].append([0,0,0]);d['groups'].append([101,102,120,121]);d['plan'].remove([120,[],[]]);d['plan']+=[[179,[101,102,121],[0,1,2]],[120,[179],[0]]]
 return d
if __name__=='__main__':
 name=sys.argv[1];out=Path(sys.argv[2]);stage=sys.argv[3];want=json.loads((R/'EXACT_EXPECTED.json').read_text())[name]
 REPLAY.sources()
 if stage=='A':
  inp=out.parent/(out.name+'_definition');inp.mkdir(parents=True,exist_ok=False);(inp/'GENERATOR.json').write_bytes(C(definition(name)))
 else:inp=R
 verify_family.main(types.SimpleNamespace(input=inp,out=out,stage=stage))
 for n in {'A':['GENERATOR.json','ACTIVE_IDS.json','raw.json','A.json'],'B':['B.json'],'MASS':['CENTRED_MASS.json','STATS.json'],'FINISH':['RECEIPT.json']}[stage]:
  b=(out/n).read_bytes();got=dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest());assert got==want['files'][n],(name,n,got,want['files'][n])
 if stage=='FINISH':print('S8_PC_SOURCE_ONLY_EXACT_COLD_NONWINNER_PASS',name)
