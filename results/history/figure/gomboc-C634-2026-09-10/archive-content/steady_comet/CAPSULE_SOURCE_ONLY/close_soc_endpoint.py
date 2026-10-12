from pathlib import Path
import json,sys
from atlas_opt import Atlas
from condition_events import merge_rechart
from numeric import recover,mechanics
R=Path(__file__).parent
src=R/'soc_records/E318_TARGET60_66_FINAL.json'
g=json.loads(src.read_text());fs=json.loads(src.with_name('E318_TARGET60_66_FINAL_faces.json').read_text());m=Atlas(g,fs);st=m.state(m.u0)
z,f,d=merge_rechart(g,fs,60,66,controls=st['X']);rr=mechanics(recover(z)[:137],f,tol=1e-11)
assert rr['counts']==[1,1,0] and rr['E']==317 and rr['min_gap']>1e-5 and min(rr['polar_escape_min'],rr['primal_escape_min'])>1e-8
for name,obj in [('C634_SOC_GENERATOR.json',z),('C634_SOC_faces.json',f),('C634_SOC_numeric.json',rr)]:
 (R/name).write_text(json.dumps(obj,sort_keys=True,separators=(',',':')))
print(rr)
