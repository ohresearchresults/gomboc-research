from pathlib import Path
import json,shutil,subprocess,os,sys
R=Path(__file__).parent
name=sys.argv[1];gen=Path(sys.argv[2]);VEF=list(map(int,sys.argv[3:6]));D=R/name;D.mkdir(exist_ok=True)
for f in ['RECONSTRUCT.py','check_A.py','check_B.py','EXTRA.py']:shutil.copyfile(R/'parent650/C650'/f,D/f)
shutil.copyfile(gen,D/'GENERATOR.json');shutil.copyfile(R/'CERTIFY_TEMPLATE.py',D/'REPLAY.py')
H=[list(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines()];G=[list(map(int,l.split())) for l in (R/'C650_polar_edges.txt').read_text().splitlines()]
(D/'META.json').write_text(json.dumps(dict(tag=name,VEF=VEF,H213_edges=H,G650_edges=G,require_H213=('--allow-missing-H213' not in sys.argv)),sort_keys=True,separators=(',',':')))
with open(D/'REPLAY_NOW.log','w') as f:
 p=subprocess.Popen([sys.executable,'-u','-S','REPLAY.py'],cwd=D,stdout=f,stderr=subprocess.STDOUT,start_new_session=True,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'});print(p.pid,D)
