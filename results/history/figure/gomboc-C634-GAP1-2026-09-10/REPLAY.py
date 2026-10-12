"""Cold source-only replay: no geometry/certificate cache enters the temporary directory."""
import hashlib,json,subprocess,sys,tempfile,shutil
from pathlib import Path
P=Path(__file__).resolve().parent
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
EXPECTED={'RAW.json':'081e1bc169a91497f568c3d54c973277771d02c779b41058e6f292e35ae62969','A.json':'0cadbba6ecd6bdf881f21c76790ff35f810a8db7a17ac0adf13ff26530aa97c4','B.json':'0cadbba6ecd6bdf881f21c76790ff35f810a8db7a17ac0adf13ff26530aa97c4'}
with tempfile.TemporaryDirectory(prefix='gap1_source_only_') as temp:
 d=Path(temp)
 for f in ['GENERATOR.json','RECONSTRUCT.py','check_A.py','check_B.py']:
  shutil.copy2(P/f,d/f)
 for args in [['RECONSTRUCT.py','GENERATOR.json','RAW.json'],['check_A.py','RAW.json','A.json'],['check_B.py','RAW.json','B.json']]:
  subprocess.run([sys.executable,*args],cwd=d,check=True)
 assert (d/'A.json').read_bytes()==(d/'B.json').read_bytes()
 for f in ['RAW.json','A.json','B.json']:
  assert h(d/f)==EXPECTED[f]
  if (P/f).exists():assert (d/f).read_bytes()==(P/f).read_bytes()
  else:shutil.copy2(d/f,P/f)
 a=json.loads((d/'A.json').read_text());assert [a['V'],a['E'],a['F'],a['counts'],a['weak']]==[182,317,137,[1,1,0],[0,0,0]]
 receipt={'marker':'C634_ONE_SLACK_APPROACH_FULL_EXACT_SOURCE_ONLY_PASS','counts':a['counts'],'weak_only':a['weak'],'V':a['V'],'E':a['E'],'F':a['F'],'source_sha256':{f:h(P/f) for f in ['GENERATOR.json','RECONSTRUCT.py','check_A.py','check_B.py']},'matched_output_sha256':{f:h(d/f) for f in ['RAW.json','A.json','B.json']}}
(P/'COLD_RECEIPT.json').write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
print(receipt['marker'],flush=True)
