"""Finite deletion beam over the standalone 49-integer C282 point set.
Only actual filled-volume centroids are used. Numerical selection is not proof.
"""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import QhullError
from dual_chain import census,encoded

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--beam',type=int,default=6);p.add_argument('--maxsu',type=int,default=3);a=p.parse_args();out=Path(a.out);out.mkdir(exist_ok=False)
 b=(Path(__file__).resolve().parent/'POINTS49.json').read_bytes();assert hashlib.sha256(b).hexdigest()=='c01c8c5eb79a099250ea9f2c8cf8d85a17546abe7ab2b58129a78a6df3e1aaa7';P=np.array(json.loads(b)['points'],float)/1000
 level=[list(range(len(P)))];seen={tuple(level[0])};best={};rows=[];tested=0;winner=False
 for depth in range(1,len(P)-3):
  bucket={}
  for ids in level:
   for delete in ids:
    keep=tuple(i for i in ids if i!=delete)
    if keep in seen:continue
    seen.add(keep);tested+=1
    try:r=census(P[list(keep)])
    except (ValueError,QhullError,AssertionError):continue
    if r['S_uncertain'] or r['U_uncertain'] or r['S']+r['U']>a.maxsu:continue
    r['ids']=list(keep);key=(r['S'],r['U']);rank=(r['E_proposal'],r['min_s'],r['ids']);bucket.setdefault(key,[]).append(r)
    if key not in best or rank<(best[key]['E_proposal'],best[key]['min_s'],best[key]['ids']):best[key]=r;(out/('BEST_%d%d.json'%key)).write_bytes(encoded(r));print('BEST',depth,key,r['V'],r['E_proposal'],flush=True)
    if key==(1,1):winner=True;break
   if winner:break
  level=[]
  for key,rr in sorted(bucket.items()):level+=[r['ids'] for r in sorted(rr,key=lambda r:(r['E_proposal'],r['min_s'],r['ids']))[:a.beam]]
  rows.append({'depth':depth,'tested':tested,'level':level});(out/'SEARCH.json').write_bytes(encoded({'parameters':vars(a),'levels':rows,'best':list(best.values())}));print('LEVEL',depth,tested,len(level),flush=True)
  if not level or winner:break
 print('C282_INTEGER_VERTEX_BEAM_ENDED',tested,winner,[(k,v['V'],v['E_proposal']) for k,v in best.items()],flush=True)
if __name__=='__main__':main()
