from pathlib import Path
import json,shutil,subprocess,os,sys,hashlib
R=Path(__file__).parent
name=sys.argv[1];src=R/name;dst=R/(name+'_COLD')
assert not dst.exists();dst.mkdir()
files=['GENERATOR.json','META.json','RECONSTRUCT.py','check_A.py','check_B.py','EXTRA.py','REPLAY.py','FROZEN_OUTPUTS.json']
receipts={}
for f in files:
 shutil.copyfile(src/f,dst/f);receipts[f]=hashlib.sha256((dst/f).read_bytes()).hexdigest()
(dst/'SOURCE_ONLY_INPUTS.json').write_text(json.dumps(receipts,sort_keys=True,separators=(',',':')))
with open(dst/'REPLAY_COLD.log','w') as f:
 p=subprocess.Popen([sys.executable,'-u','-S','REPLAY.py'],cwd=dst,stdout=f,stderr=subprocess.STDOUT,start_new_session=True);print(name,'pid',p.pid)
