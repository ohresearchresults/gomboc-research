"""Direct physical candidates from stable-pair retirement and apex mass closure.
The support replacement is literal and changes the body. No reference census
is inherited; every candidate is checked at its newly integrated centroid.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.optimize import brentq
from scipy.spatial import QhullError
from geometry import halfspace_mesh,census,arrows
from stable_face_augmentation import halfspaces


def run(inputs,out,samples=70):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);history=[];best=999;start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(inputs=[str(pathlib.Path(p).resolve()) for p in inputs],samples=samples,
        scope='Literal retirement of two reference-stable support planes, one new axial lower plane, full same-body mass and census'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    def save_if_goal(Q,m,row):
        st=census(m,0);row.update(st)
        if 17<=st['E']<250 and st['S']==st['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',Q=Q,X=m['X']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2));return True
        return False
    for si,input in enumerate(inputs):
        H=np.load(input)['Q'];m=halfspace_mesh(H);ids=np.flatnonzero(arrows(H).max(1)<0)
        if len(ids)!=2:continue
        other=np.delete(H,ids,axis=0);scale=-float(m['X'][:,2].min())
        for j,height in enumerate(scale*np.geomspace(.35,2.,samples)):
            row=dict(source=si,input=str(pathlib.Path(input).resolve()),sample=j,retired=ids.tolist(),height=float(height),seconds=time.time()-start)
            try:
                Q=np.r_[other,[[0,0,-1/height]]];m=halfspace_mesh(Q)
                if save_if_goal(Q,m,row):return
                row['initial_counts']=[row['S'],row['U']]
                if m['g'][2]<-1e-9:
                    X=m['X'];ax=np.flatnonzero(np.linalg.norm(X[:,:2],axis=1)<1e-7)
                    if not len(ax):raise ValueError('No axial carrier after literal support retirement')
                    apex=int(ax[np.argmax(X[ax,2])]);old=float(X[apex,2])
                    def lifted(A):
                        Y=X.copy();Y[apex]=[0,0,A];G=halfspaces(Y);return G,halfspace_mesh(G)
                    hi=old*1.5
                    while hi<12*old and lifted(hi)[1]['g'][2]<0:hi*=1.5
                    A=float(brentq(lambda a:float(lifted(a)[1]['g'][2]),old,hi,xtol=2e-12));Q,m=lifted(A)
                    if abs(m['g']).max()>2e-9:raise ValueError('Independent apex first moment failed')
                    row['apex_height']=A
                    if save_if_goal(Q,m,row):return
                if 17<=row['E']<250 and row['S']+row['U']<best:
                    best=row['S']+row['U'];p=out/f'source{si:02d}-sample{j:03d}';p.mkdir();np.savez(p/'body.npz',Q=Q,X=m['X']);row['folder']=str(p.resolve());(p/'summary.json').write_text(json.dumps(row,indent=2))
                    print('PAIR_RETIREMENT_DIRECT',json.dumps({k:v for k,v in row.items() if k not in ['S_ids','U_ids']}),flush=True)
            except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as error:row['error']=repr(error)
            history.append(row)
            if j%5==0:(out/'history.json').write_text(json.dumps(history,indent=2))
        (out/'history.json').write_text(json.dumps(history,indent=2))
