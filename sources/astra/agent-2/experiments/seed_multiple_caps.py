"""Construct two real, contact-preserving caps at the unwanted stable region."""
import json,sys,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import QhullError
from apex_polygon_supports import ApexFamily
from physical_multiple_cap_family import MultipleCapFamily

def proposals(s):
    root=int(s['qp'][np.argmax(s['Q']),0]); H=s['H'][s['A']]
    face=s['faces'][root]
    if len(face)!=3:return
    Y=s['Y'][root];foot=s['g']+Y/(Y@Y);direction=foot-s['g']
    for v in sorted(face,key=lambda v:-s['Z'][v]@s['Z'][v]):
        for t in [.03,.2,.6,.9]:
            base=(1-t)*foot+t*s['X'][v];den=H@direction;num=1-H@base
            mask=(den>0)&(np.arange(len(H))!=root)
            if not mask.any():continue
            limit=float(np.min(num[mask]/den[mask]))
            if limit<=0:continue
            for fraction in [.02,.3,.85]:
                point=base+limit*fraction*direction
                if np.max((point-s['g'])@(s['X']-point).T)<=0:continue
                yield point,dict(carrier=root,t=t,toward=v,fraction=fraction)

def run(src,out,m=44):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    raw=src.read_bytes();(out/'source_q.npy').write_bytes(raw);q=np.load(out/'source_q.npy')
    base=ApexFamily(m,allow_top_retirement=True,edge_limit=249).state(q)
    (out/'source.json').write_text(json.dumps(dict(path=str(src),sha256=hashlib.sha256(raw).hexdigest(),apex=m,method=__doc__),indent=2)+'\n')
    one=MultipleCapFamily(m,1,249);two=MultipleCapFamily(m,2,249);rows=[];best=None
    for i,(p,first) in enumerate(proposals(base)):
        try:s=one.state(np.r_[q,p])
        except (ValueError,QhullError,np.linalg.LinAlgError):continue
        if s['U']!=1 or s['S']>2:continue
        for j,(pp,second) in enumerate(proposals(s)):
            z=np.r_[q,p,pp]
            try:t=two.state(z)
            except (ValueError,QhullError,np.linalg.LinAlgError):continue
            row={k:t[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']}
            row.update(label=f'cap{i:03d}_{j:03d}',first=first,second=second)
            rows.append(row)
            if t['U']!=1:continue
            key=(t['S'],t['Qmax'])
            if best is None or key<best[0]:
                best=key,row;np.save(out/'best_z.npy',z);np.save(out/'best_base_H.npy',t['baseH']);np.save(out/'best_cap_points.npy',t['cap_points'])
                (out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('PHYSICAL_MULTICAP_SEED',row,flush=True)
            if t['S']==1:
                np.save(out/'NUMERICAL_NOMINATION_z.npy',z);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return
        (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')
    return None if best is None else best[1]

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44)
