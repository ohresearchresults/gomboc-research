"""Literal plane replacements that increase the genuine apex valence.
One non-apex raw normal is replaced by (hx,hy,1), with every other normal
unchanged. This is a different physical halfspace intersection. Each trial
is re-hulled and re-integrated; no reference-center census is inherited.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import QhullError
from apex_polygon_supports import ApexFamily
from support_persistence import ROOT

def run(src,out,m=4):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);H=np.load(src);family=ApexFamily(m+1);rows=[];best=None
    (out/'source.npy').write_bytes(src.read_bytes());(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),old_apex=m,new_apex=m+1,method=__doc__),indent=2)+'\n')
    for i in range(m,len(H)):
        order=list(range(m))+[i]+[j for j in range(m,len(H)) if j!=i];HH=H[order].copy();HH[m,2]=1.;q=family.pack(HH);label=f'lift{i:03d}';np.save(out/(label+'_q.npy'),q);np.save(out/(label+'_H.npy'),HH)
        try:
            s=family.state(q);row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(lifted=i,label=label,old_z=float(H[i,2]),centroid=s['g'].tolist(),volume=s['volume']);print('LITERAL_APEX_LIFT',row,flush=True)
            if s['U']==1 and (best is None or s['Qmax']<best['Qmax']):best=row;np.save(out/'best_U1_q.npy',q);np.save(out/'best_U1_H.npy',HH);(out/'best_U1.json').write_text(json.dumps(row,indent=2)+'\n')
        except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as e:row=dict(lifted=i,label=label,error=repr(e))
        rows.append(row)
    (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n');return rows

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 4)
