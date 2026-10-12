"""Finite U=1-preserving deletion beam on a saved C96-derived point set."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.spatial import QhullError

from geometry import census,persistence,write_json


def main():
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('--out',required=True)
    ap.add_argument('--beam',type=int,default=10)
    args=ap.parse_args();out=Path(args.out);out.mkdir(exist_ok=False)
    binary=Path(args.input).read_bytes();p=np.array(json.loads(binary)['points'],float)
    first=tuple(sorted(census(p,True)['hull'].vertices.tolist()))
    level=[first];seen={first};tested=0;best={};levels=[]
    for depth in range(len(first)-3):
        bucket={}
        for ids in level:
            for delete in ids:
                keep=tuple(i for i in ids if i!=delete)
                if keep in seen:
                    continue
                seen.add(keep);tested+=1
                try:
                    r=census(p[list(keep)],True)
                    if r['U']!=1 or r['S_uncertain'] or r['U_uncertain']:
                        continue
                    rr=census(p[list(keep)])
                    barrier=persistence(r['q'])/max(np.einsum('ij,ij->i',r['x'],r['x']))
                    rank=(r['E_proposal'],barrier,len(keep),keep)
                    rec=dict(ids=list(keep),deleted=int(delete),depth=depth,barrier=barrier,
                             census=rr,points=p[list(keep)].tolist())
                    key=r['S']
                    bucket.setdefault(key,[]).append((rank,rec))
                    if key not in best or rank<best[key]:
                        best[key]=rank;write_json(out/('BEST_'+str(key)+'_1.json'),rec)
                        print('DELETE_BEST',key,rank[:3],flush=True)
                    if key==1:
                        write_json(out/'PROPOSAL110.json',rec)
                except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):
                    continue
        level=[]
        for key,entries in sorted(bucket.items()):
            entries.sort(key=lambda x:x[0])
            level.extend(tuple(rec['ids']) for _,rec in entries[:args.beam])
        levels.append(dict(depth=depth,tested=tested,width=len(level)))
        write_json(out/'SEARCH.json',dict(config=vars(args),input_sha256=hashlib.sha256(binary).hexdigest(),
                                        levels=levels,tested=tested,classes=sorted(best)))
        if not level or (out/'PROPOSAL110.json').exists():
            break
    print('U1_DELETION_BEAM_FINISHED',tested,sorted(best),flush=True)


if __name__=='__main__':
    main()
