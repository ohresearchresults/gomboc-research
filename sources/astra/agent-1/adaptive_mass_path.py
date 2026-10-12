"""Density continuation with explicitly recycled inactive zero-mass controls.
At most85 supplied physical points, hence E<=249, throughout. Only independently
tested homogeneous centroids are own-centroid nominations.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,numpy as np,json,argparse,time
from mass_homotopy import mesh,guards,repair,check_own
from homotopy_predictor import run as predict

def run(input,out,epochs=15,steps=20,eps=2e-7):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);src=pathlib.Path(input);history=[];start=time.time()
    for epoch in range(epochs):
        d=np.load(src);X=d['X'];w=d['w'];lam=float(d['lam']);assert len(X)<=85
        if check_own(X,w,out):return
        m,c,v,pa,sg,st=guards(X,w,lam);idle=[int(i) for i in range(len(X)) if w[i]==0 and i not in m['active']];p=out/f'epoch{epoch:03d}';p.mkdir(exist_ok=True);np.savez(p/'parent.npz',X=X,w=w,lam=lam)
        if idle:
            T=m['polar_triangles'];a=X[T];cross=np.cross(a[:,1]-a[:,0],a[:,2]-a[:,0]);area=np.linalg.norm(cross,axis=1);chosen=[int(k) for k in np.argsort(-area) if k!=st['rootQ']][:len(idle)];Y=X.copy();height=1e-7*np.sqrt(np.mean((X-c)**2));record=[]
            for i,k in zip(idle,chosen):
                Y[i]=a[k].mean(0)+height*cross[k]/area[k];record.append(dict(point=i,triangle=T[k].tolist(),before=X[i].tolist(),after=Y[i].tolist(),height=height))
            (p/'recycle.json').write_text(json.dumps(record,indent=2));np.savez(p/'recycled.npz',X=Y,w=w,lam=lam);Y,ok,stats=repair(Y,w,lam,p/'recycle-repair',steps=180,eps=eps)
            if not ok:print('RECYCLE_RETRACTION_FAILED',epoch,lam,flush=True);break
            src=p/'recycle-repair/strict_reference110.npz'
        predict(src,p/'predictor',stages=steps,eps=eps)
        if (p/'predictor/NOMINATION_OWN110.npz').exists():
            d=np.load(p/'predictor/NOMINATION_OWN110.npz');np.savez(out/'NOMINATION_OWN110.npz',X=d['X'],w=d['w'],lam=1.);return
        if not (p/'predictor/latest-strict.npz').exists():print('NO_MASS_PROGRESS',epoch,flush=True);break
        src=p/'predictor/latest-strict.npz';d=np.load(src);newlam=float(d['lam']);row=dict(epoch=epoch,before=lam,after=newlam,recycled=len(idle),seconds=time.time()-start,source=str(src));history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest-strict.npz',X=d['X'],w=d['w'],lam=d['lam']);print('ADAPTIVE_MASS_EPOCH',json.dumps(row),flush=True)
        if newlam<=lam+1e-8:print('ADAPTIVE_MASS_LOCAL_STALL',flush=True);break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--epochs',type=int,default=15);ap.add_argument('--steps',type=int,default=20);ap.add_argument('--epsilon',type=float,default=2e-7);a=ap.parse_args();run(a.input,a.out,a.epochs,a.steps,a.epsilon)
