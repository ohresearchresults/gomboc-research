"""Direct own110 family: bottom cut plus mass-balanced axial apex height.

Raising a positive axial apex cannot remove any positive reference escape
arrow into it: such an arrow's source necessarily has positive z. Other
arrows are unchanged. Hull changes and cutting are nevertheless independently
checked. This is a construction lemma, not an inherited own-centroid census.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.optimize import brentq
from scipy.spatial import QhullError
from stable_face_augmentation import halfspaces
from geometry import halfspace_mesh,census


def run(inputs,out,samples=70):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);history=[];start=time.time();best=999
    (out/'definition.json').write_text(json.dumps(dict(inputs=[str(pathlib.Path(p).resolve()) for p in inputs],samples=samples,
        scope='Literal base-cut and raised-apex hulls; actual uniform centroid solved, complete own census and E<250 required before exact verification'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    for source_index,input in enumerate(inputs):
        X=np.load(input)['X'].copy();ax=np.flatnonzero(np.linalg.norm(X[:,:2],axis=1)<1e-7)
        if not len(ax):history.append(dict(source=source_index,error='No axial vertex'));continue
        apex=int(ax[np.argmax(X[ax,2])]);old=float(X[apex,2]);maximum=-float(X[:,2].min())
        for j,height in enumerate(np.linspace(.15*maximum,maximum*(1-1e-7),samples)):
            def body(A):
                Y=X.copy();Y[apex]=[0,0,A];H=halfspaces(Y);Q=np.r_[H,[[0.,0.,-1/height]]]
                return Q,halfspace_mesh(Q)
            try:
                Q0,m0=body(old)
                if m0['g'][2]>-1e-10:
                    history.append(dict(source=source_index,sample=j,height=float(height),scope='No upward apex mass closure from this cut'));continue
                hi=old*1.5
                while hi<12*old and body(hi)[1]['g'][2]<0:hi*=1.5
                A=float(brentq(lambda a:float(body(a)[1]['g'][2]),old,hi,xtol=2e-12))
                Q,m=body(A);st=census(m,0)
                if abs(m['g']).max()>2e-9:raise ValueError('Final uniform centroid not closed')
                row=dict(source=source_index,input=str(pathlib.Path(input).resolve()),sample=j,height=float(height),apex_height=A,
                         seconds=time.time()-start,**st)
                if 17<=st['E']<250 and st['S']+st['U']<best:
                    best=st['S']+st['U'];p=out/f'source{source_index:02d}-cut{j:03d}';p.mkdir()
                    np.savez(p/'body.npz',Q=Q,X=m['X']);row['folder']=str(p.resolve());(p/'summary.json').write_text(json.dumps(row,indent=2))
                    print('APEX_MASS_CANDIDATE',json.dumps({k:v for k,v in row.items() if k not in ['S_ids','U_ids']}),flush=True)
                if 17<=st['E']<250 and st['S']==st['U']==1:
                    np.savez(out/'POTENTIAL_OWN110.npz',Q=Q,X=m['X']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2));return
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as error:
                row=dict(source=source_index,sample=j,height=float(height),error=repr(error))
            history.append(row)
            if j%5==0:(out/'history.json').write_text(json.dumps(history,indent=2))
        (out/'history.json').write_text(json.dumps(history,indent=2))
