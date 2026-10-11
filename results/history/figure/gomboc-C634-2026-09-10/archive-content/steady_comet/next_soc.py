"""One full-coordinate own-mass conditioning/contact attempt from exact C634."""
from pathlib import Path
import json,time,numpy as np
from atlas_opt import Atlas,optimize
from adaptive_homotopy import candidate_screen
from soc_contact import run
R=Path(__file__).parent
out=R/'soc_next';out.mkdir(exist_ok=True)
g=json.loads((R/'C634_SOC/GENERATOR.json').read_text());fs=json.loads((R/'C634_SOC_faces.json').read_text());m=Atlas(g,fs);m.checkpoint=out/'CONDITION_CURRENT'
u,st,msg=optimize(m,steps=240,trust=.0002,keep=1e-6,goal=1e-5,stopgap=5e-9)
m.save(u,out/'CONDITION_GENERATOR.json');(out/'CONDITION_faces.json').write_text(json.dumps(fs,separators=(',',':')))
print('NEXT_CONDITION',msg,st['vals'].min(),st['gaps'][~m.inc].min(),flush=True)
H={tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines()};keep=max(1e-8,min(5e-7,st['vals'].min()/4))
cs=candidate_screen(m,st,u,H,keep,limit=30)
(out/'SCREEN.json').write_text(json.dumps([list(c[:6]) for c in cs],default=lambda x:x.tolist() if hasattr(x,'tolist') else x,indent=2))
print('NEXT_SCREEN',[(c[:6]) for c in cs[:5]],flush=True)
if cs:
 _,_,a,b,tg,pol,nu=cs[0];m.save(nu,out/'SEED_GENERATOR.json');print('NEXT_CHOICE',a,b,pol,tg,keep,flush=True)
 run(out/'SEED_GENERATOR.json',out/'CONDITION_faces.json',out/'NEXT_SOC',tg,steps=240,keep=keep)
