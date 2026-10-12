from pathlib import Path
import json,sys,itertools,time
from deletion import Model,canon
raw=json.loads(Path(sys.argv[1]).read_text());m=Model(raw);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
# Start with the recovered co-record chart; then the entire pair-deletion family.
pairs=list(dict.fromkeys([tuple(sorted((132,j)))for j in range(len(m.X))if j!=132]+list(itertools.combinations(range(len(m.X)),2))))
f=(out/'pairs.jsonl').open('w');start=time.monotonic();best=999
for k,ij in enumerate(pairs):
 try:r=m.screen(ij)
 except Exception as e:r=dict(deleted=list(ij),error=repr(e))
 f.write(canon(r)+'\n');f.flush()
 if 'counts'in r:
  score=sum(r['counts'])
  if score<best or (r['counts']==[1,1,0]):
   best=min(best,score);print(k,{z:r[z]for z in ['deleted','VEF','C','counts','U','H']},flush=True)
 if k%500==0:print('step',k,'secs',round(time.monotonic()-start,2),flush=True)
f.close();print('PAIR_SCREEN_DONE',len(pairs),flush=True)
