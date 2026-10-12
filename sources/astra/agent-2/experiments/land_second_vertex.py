"""Land a nearly incident support exactly onto a genuine degree-four vertex.
The three defining supports and added support form a new prescribed polar
quadrilateral, disjoint from the old apex star. This is an explicit physical
deformation, followed by a new whole-body hull, centroid and census.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import QhullError
from apex_polygon_supports import ApexFamily
from two_apex_supports import TwoApexFamily

def run(src,out,m=4):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_q.npy').write_bytes(raw);q=np.load(out/'source_q.npy');s=ApexFamily(m,allow_top_retirement=True,edge_limit=249).state(q);H=s['H'];X=s['X'];gap=1-H@X.T;pairs=[]
    for v in range(1,len(X)):
        tri=list(map(int,s['R'][v]))
        if min(tri)<m or abs(X[v,2])<1e-4:continue
        for j in s['A']:
            if j>=m and int(j) not in tri:pairs.append((float(gap[j,v]),int(j),v,tri))
    pairs.sort();rows=[];best=None;fam=TwoApexFamily(m,4)
    (out/'source.json').write_text(json.dumps(dict(path=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,method=__doc__),indent=2)+'\n')
    for k,(distance,j,v,tri) in enumerate(pairs[:80]):
        if distance>.02:break
        second=tri+[j];order=list(range(m))+second+[i for i in range(m,len(H)) if i not in second];HH=H[order].copy();point=X[v].copy();HH[m+3]+=distance*point/(point@point)
        try:
            qq=fam.pack(HH,point);t=fam.state(qq)
        except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError):continue
        row={key:t[key] for key in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=f'landing{k:03d}',original_vertex=v,original_plane=j,original_gap=distance,second_plane_group=second,permutation=order);np.save(out/(row['label']+'_q.npy'),qq);rows.append(row)
        if t['U']!=1:continue
        key=(t['S'],t['Qmax'])
        if best is None or key<best[0]:
            best=key,row;np.save(out/'best_q.npy',qq);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('SECOND_GENUINE_VERTEX_LANDING',row,flush=True)
        if t['S']==1:
            np.save(out/'NUMERICAL_NOMINATION_q.npy',qq);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');break
    (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');return None if best is None else best[1]

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 4)
