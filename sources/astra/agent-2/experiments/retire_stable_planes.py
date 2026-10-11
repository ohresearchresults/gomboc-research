"""Literal stable-facet deletions at the integrated body's own centroid.
No plane is merged by a numerical tolerance. Each candidate actually removes
one input halfspace and rebuilds the resulting body. A bounded beam retains
only actual numerical U1 bodies while trying to remove every extra stable face.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.spatial import QhullError
from apex_polygon_supports import ApexFamily

def run(src,out,m=4,rounds=12,width=5):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_q.npy').write_bytes(raw);q=np.load(out/'source_q.npy');states=[(q,m,'source')];rows=[];best=None;start=time.time()
    (out/'source.json').write_text(json.dumps(dict(path=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,rounds=rounds,width=width,method=__doc__),indent=2)+'\n')
    for round in range(rounds):
        next=[]
        for qi,mm,parent in states:
            s=ApexFamily(mm,allow_top_retirement=True,edge_limit=249).state(qi);sr=int(np.argmax(np.sum(s['Y']**2,1)));stable=np.flatnonzero(s['sguards']<0)
            for f in stable:
                if f==sr:continue
                owner=int(s['A'][f]);newm=mm-int(owner<mm)
                if newm<3:continue
                H=np.delete(s['H'],owner,axis=0);fam=ApexFamily(newm,allow_top_retirement=True,edge_limit=249);qq=fam.pack(H);label=f'r{round:02d}_c{len(rows):04d}_drop{owner:03d}'
                try:t=fam.state(qq)
                except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError):continue
                row={k:t[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,parent=parent,deleted_support=owner,m=newm);rows.append(row);np.save(out/(label+'_q.npy'),qq)
                if t['U']!=1:continue
                key=(t['S'],t['Qmax']);next.append((key,qq,newm,label))
                if best is None or key<best[0]:best=key,row;np.save(out/'best_q.npy',qq);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('LITERAL_STABLE_PLANE_RETIREMENT',row,flush=True)
                if t['S']==1:
                    np.save(out/'NUMERICAL_NOMINATION_H.npy',t['H']);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return row
        (out/'screen.json').write_text(json.dumps(dict(rows=rows,seconds=time.time()-start,goal_complete=False),indent=2)+'\n')
        if not next:break
        next.sort(key=lambda r:r[0]);states=[(q,mm,label) for _,q,mm,label in next[:width]]
    return None if best is None else best[1]

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 4)
