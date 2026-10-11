"""Prepare the verified C626 maximal chart for subsequent triangle-panel unions.
This constructs continuation inputs only; it does not claim a third loss.
"""
import argparse,hashlib,json,shutil,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import RECONSTRUCT,check_A,check_B,chart
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();out=a.out.resolve();out.mkdir(parents=True,exist_ok=False)
 for f in ['contact.py','general_atlas.py','numeric.py','qp.py','REFINE.py']:shutil.copyfile(ROOT/f,out/f)
 shutil.copytree(ROOT/'parent',out/'parent');shutil.copyfile(ROOT/'candidate/GENERATOR.json',out/'parent/GENERATOR.json')
 G=json.loads((out/'parent/GENERATOR.json').read_text());raw=RECONSTRUCT.recover(G);p,q=check_A.run(raw),check_B.run(raw);assert p==q and hashlib.sha256(B(p)).hexdigest()=='da2fa56ff31186699a59b79a1a2bce6362aa362bcd34c735c2fb0a2424d811dd'
 folder=out/'baseline';folder.mkdir()
 for name,obj in [('raw.json',raw),('A.json',p),('B.json',q)]: (folder/name).write_bytes(B(obj))
 seed=chart.recover(root=out);(out/'chart_exact.json').write_bytes(B(check_A.encode(seed)))
 root=p['unstable_vertices'][0];deps={i:d for i,d,a in G['plan']};used={j for i,d,a in G['plan'] for j in d};eligible=[]
 for e,(i,j) in enumerate(seed['edges']):
  panels=[f for f,cy in enumerate(seed['faces']) if i in cy and j in cy]
  if len(panels)==2 and seed['outer'] not in panels and min(len(p['faces'][k]) for k in (i,j))>=4 and root not in panels and all(len(seed['faces'][f])==3 for f in panels) and any(not deps[k] and k not in used for k in (i,j)):
   eligible.append(dict(edge=e,pair=[i,j],panels=panels))
 (out/'ELIGIBLE.json').write_bytes(B(eligible));print('C626_CONTINUATION_CHART_PREPARED',len(seed['edges']),len(eligible),flush=True)
if __name__=='__main__':main()
