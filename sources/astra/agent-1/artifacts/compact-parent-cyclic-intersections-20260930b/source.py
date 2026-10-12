"""Direct cyclic intersections of compact own-monostable physical parents."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,pathlib,numpy as np
from gmpy2 import mpq
from geometry import halfspace_mesh,census,arrows
from rotated_monostable_intersections import centered_body


def run(out):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);rows=[]
    parents=['A1_RECT_C374_G50','A1_RECT_MERGED_C456_RECHART_G50','A1_C486_CAP_RETRACT_G15','c162']
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    for name in parents:
        path=pathlib.Path('artifacts')/name/'audit.json';a=json.loads(path.read_text())
        H=np.array([[float(mpq(v)/mpq(row[3])) for v in row[:3]] for row in a['raw_halfspaces']])
        m=halfspace_mesh(H);Q=H/(1-H@m['g'])[:,None];ss=np.flatnonzero(arrows(Q).max(1)<0)
        if len(ss)!=1:raise ValueError('Required parent S1 failed numerical readback')
        s=int(ss[0]);scale=np.linalg.norm(Q[s]);axis=-Q[s]/scale
        x=np.cross(np.eye(3)[np.argmin(abs(axis))],axis);x/=np.linalg.norm(x);y=np.cross(axis,x);R=np.stack([x,y,axis])
        Q=Q@R.T/scale;Q[s]=[0,0,-1];other=np.delete(Q,s,axis=0)
        p=out/name;p.mkdir();np.savez(p/'aligned_parent.npz',Q=Q,stable=s,rotation=R,scale=scale)
        for n in [2,3,4,5,6]:
            copies=[]
            for angle in 2*np.pi*np.arange(n)/n:
                c,t=np.cos(angle),np.sin(angle);RR=np.array([[c,-t,0],[t,c,0],[0,0,1]]);copies.append(other@RR.T)
            q=np.concatenate(copies);HH=np.r_[[[0,0,-1]],q];row=dict(parent=name,n=n)
            try:
                mm=halfspace_mesh(HH);cc=census(mm,0)
                row=dict(parent=name,n=n,initial=cc,referenceS=int(np.sum(arrows(HH[mm['active']]).max(1)<0)))
                Qc,mc,stats=centered_body(q);row['centered']=stats;np.savez(p/f'n{n}-mass-closed.npz',Q=Qc,X=mc['X'])
                if stats['S']==stats['U']==1 and 17<=stats['E']<250:
                    np.savez(out/'POTENTIAL_OWN110.npz',Q=Qc,X=mc['X']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2))
                    rows.append(row);(out/'history.json').write_text(json.dumps(rows,indent=2));return
            except (ValueError,RuntimeError,np.linalg.LinAlgError) as error:
                row['closure_error']=repr(error)
            rows.append(row);(out/'history.json').write_text(json.dumps(rows,indent=2))
            print('COMPACT_INTERSECTION',name,n,'initial',[row.get('initial',{}).get(k) for k in ['S','U','E','g']],
                  'closed',{k:row.get('centered',{}).get(k) for k in ['S','U','E','g']},flush=True)
