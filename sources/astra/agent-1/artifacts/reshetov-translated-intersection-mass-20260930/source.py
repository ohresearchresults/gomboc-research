"""Direct actual-centroid intersection path with no imposed rotational symmetry.
Two parent side-support sets are intersected after a relative axial rotation
and a planar translation. Translation and the common lower support height are
solved against the actual three-component uniform centroid. The body has at
most27 planes; every final equilibrium count is computed on that same hull.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.spatial import QhullError
from geometry import halfspace_mesh,census


def run(parent,out,samples=320):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);d=np.load(parent);H=d['Q'];q=np.delete(H,int(d['stable']),axis=0)
    m=halfspace_mesh(H);t_scale=np.maximum(np.sqrt(np.mean(m['X'][:,:2]**2,axis=0)),.1)
    g_scale=np.r_[t_scale,1.];history=[];start=time.time();best=999;previous=np.zeros(3)
    (out/'definition.json').write_text(json.dumps(dict(parent=str(pathlib.Path(parent).resolve()),samples=samples,translation_scale=t_scale.tolist(),
        scope='Literal two-copy physical intersections; three-component uniform mass closure and actual census, no inherited reference claim'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    for i,angle in enumerate(np.linspace(.002,np.pi,samples)):
        cc,ss=np.cos(angle),np.sin(angle);R=np.array([[cc,-ss,0],[ss,cc,0],[0,0,1]]);qr=q@R.T
        def body(z):
            t=z[:2]*t_scale;den=1+qr[:,:2]@t
            if den.min()<=1e-10:raise ValueError('Translated parent excludes the target centroid')
            height=float(np.exp(z[2]));Q=np.r_[[[0,0,-1/height]],q,qr/den[:,None]]
            mm=halfspace_mesh(Q);return Q,mm,mm['g']/g_scale
        z=previous.copy();records=[];ok=False
        try:Q,mm,g=body(z)
        except (ValueError,QhullError,np.linalg.LinAlgError):
            # A separate, declared seed for this angle, not a fabricated body.
            z=np.zeros(3);Q,mm,g=body(z)
        initial=z.copy()
        for it in range(35):
            error=float(np.linalg.norm(g));records.append(dict(it=it,parameters=z.tolist(),centroid=mm['g'].tolist(),scaled_residual=error))
            if error<1e-11:ok=True;break
            J=np.empty((3,3));step=2e-5;derivative_ok=True
            for j in range(3):
                delta=np.eye(3)[j]*step
                try:gp=body(z+delta)[2];gm=body(z-delta)[2];J[:,j]=(gp-gm)/(2*step)
                except (ValueError,QhullError,np.linalg.LinAlgError):derivative_ok=False;break
            if not derivative_ok or np.linalg.cond(J)>1e12:break
            dz=np.linalg.solve(J,-g);dz*=min(1.,.5/max(np.linalg.norm(dz),1e-30));accepted=False
            for level in range(12):
                zz=z+dz*2**-level
                try:QQ,mmm,gg=body(zz)
                except (ValueError,QhullError,np.linalg.LinAlgError):continue
                if np.linalg.norm(gg)<error*(1-1e-5*2**-level):z,Q,mm,g=zz,QQ,mmm,gg;accepted=True;break
            if not accepted:break
        row=dict(sample=i,angle=float(angle),closed=ok,parameters=z.tolist(),newton_steps=len(records),centroid=mm['g'].tolist(),seconds=time.time()-start)
        if ok:
            previous=z.copy();st=census(mm,0);row.update(st)
            if 17<=st['E']<250 and st['S']+st['U']<best:
                best=st['S']+st['U'];p=out/f'sample{i:04d}';p.mkdir();np.savez(p/'body.npz',Q=Q,X=mm['X']);(p/'newton.json').write_text(json.dumps(records,indent=2));row['folder']=str(p.resolve());(p/'summary.json').write_text(json.dumps(row,indent=2));print('TRANSLATED_INTERSECTION_CLOSED',json.dumps({k:v for k,v in row.items() if k not in ['S_ids','U_ids']}),flush=True)
            if 17<=st['E']<250 and st['S']==st['U']==1:
                np.savez(out/'POTENTIAL_OWN110.npz',Q=Q,X=mm['X']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2));return
        history.append(row)
        if i%10==0:(out/'history.json').write_text(json.dumps(history,indent=2))
    (out/'history.json').write_text(json.dumps(history,indent=2))
