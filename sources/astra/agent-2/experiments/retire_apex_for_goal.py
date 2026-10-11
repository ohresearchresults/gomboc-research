"""Literal apex-plane retirements to redistribute the finite edge budget.
Every remaining halfspace stays unchanged. Only actual-centroid U1 and at
most two S survive this branch; all rejected physical trials are recorded.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import QhullError
from apex_polygon_supports import ApexFamily
from support_persistence import ROOT

def run(src,out,m=42,stages=2):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_q.npy').write_bytes(raw);q=np.load(out/'source_q.npy');(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),apex_candidates=m,method=__doc__),indent=2)+'\n')
    for stage in range(stages):
        s=ApexFamily(m,allow_top_retirement=True,edge_limit=249).state(q);star=[int(s['A'][i]) for i,f in enumerate(s['faces']) if 0 in f];others=[int(i) for i in s['A'] if int(i) not in star];rows=[];best=None
        if len(star)<=3:break
        for i in star:
            order=[j for j in star if j!=i]+others;H=s['H'][order].copy();mm=len(star)-1;H[:mm,2]=1;family=ApexFamily(mm,allow_top_retirement=True,edge_limit=249);qq=family.pack(H);label=f'stage{stage:02d}_drop{i:03d}';np.save(out/(label+'_q.npy'),qq)
            try:
                t=family.state(qq);row={k:t[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,old_plane=i,new_apex_candidates=mm);np.save(out/(label+'_H.npy'),t['H'])
                if t['S']==t['U']==1:
                    (out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');from audit_free_supports import audit;audit(out/(label+'_H.npy'),out/'exact_nomination_g16',10**16);return row
                if t['U']==1 and t['S']<=2 and (best is None or t['Qmax']<best[0]):best=(t['Qmax'],row,qq,t['H'])
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as e:row=dict(label=label,old_plane=i,new_apex_candidates=mm,error=repr(e))
            rows.append(row)
        (out/f'stage{stage:02d}_screen.json').write_text(json.dumps(rows,indent=2)+'\n')
        if best is None:print('NO_DIRECT_STRICT_RETIREMENT',stage,flush=True);break
        _,row,q,H=best;m=row['new_apex_candidates'];np.save(out/'latest_q.npy',q);np.save(out/'latest_H.npy',H);(out/'latest.json').write_text(json.dumps(row,indent=2)+'\n');print('GOAL_BUDGET_RETIREMENT',row,flush=True)
    return json.loads((out/'latest.json').read_text()) if (out/'latest.json').exists() else None

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 42,int(sys.argv[4]) if len(sys.argv)>4 else 2)
