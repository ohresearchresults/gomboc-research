"""Exact S8 finite contact stratum with owner set [101,102,120,121]."""
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'source'));import REPLAY,RECONSTRUCT
out=R/'CONTACT120';out.mkdir(exist_ok=False)
d=REPLAY.generator('S8');assert len(d['controls'])==179 and len(d['groups'])==42
factor=10**12//d['grid'];assert factor*d['grid']==10**12
d['controls']=[[x*factor for x in row] for row in d['controls']];d['grid']=10**12
d['controls'].append([0,0,0]);d['groups'].append([101,102,120,121])
assert [120,[],[]] in d['plan'];d['plan'].remove([120,[],[]]);d['plan']+=[[179,[101,102,121],[0,1,2]],[120,[179],[0]]]
def dump(n,x):(out/n).write_text(json.dumps(x,sort_keys=True,separators=(',',':')))
dump('GENERATOR.json',d);dump('raw.json',RECONSTRUCT.recover(d));print('S8_CONTACT120_SOURCE_RECONSTRUCTED')
