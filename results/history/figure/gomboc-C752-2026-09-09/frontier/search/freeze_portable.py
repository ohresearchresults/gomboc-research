"""Copy unchanged exact auditors and specialize only the defining-data assertions.
Usage: python freeze_portable.py RAW.json new_directory V E F --source C762
Then: cd new_directory; python -S REPLAY.py. No optimizer in exact verification.
"""
import argparse,json,hashlib,re,shutil
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('raw');p.add_argument('out');p.add_argument('V',type=int);p.add_argument('E',type=int);p.add_argument('F',type=int);p.add_argument('--source',required=True);a=p.parse_args();src=Path(a.source);out=Path(a.out);out.mkdir(exist_ok=False);raw=Path(a.raw).read_bytes();old=(src/'RAW.json').read_bytes();sha=hashlib.sha256(raw).hexdigest();oldsha=hashlib.sha256(old).hexdigest();D=json.loads(raw)['D'];tag=f'COORD_H{a.F}_C{2*a.E}_D{D}'
s=(src/'REPLAY.py').read_text().replace(oldsha,sha)
s=re.sub(r"assert \[e\[k\] for k in \['V','E','F'\]\]==\[\d+, \d+, \d+\]",f"assert [e[k] for k in ['V','E','F']]==[{a.V}, {a.E}, {a.F}]",s)
s=re.sub(r"e\['edge_primitive_count'\]==\d+",f"e['edge_primitive_count']=={4*a.E}",s)
s=re.sub(r"e\['V'\]\+e\['E'\]\+e\['F'\]-2==\d+",f"e['V']+e['E']+e['F']-2=={2*a.E}",s)
s=re.sub(r'COORD_H\d+_C\d+_D\d+',tag,s)
(out/'RAW.json').write_bytes(raw);(out/'REPLAY.py').write_text(s)
for n in ['audit_A.py','audit_B.py','dual_A.py','dual_B.py','exact_extra.py']:shutil.copyfile(src/n,out/n)
print(tag,sha)
