"""Independent lattice-pyramid Figure branch with root extension and caps."""
import json,time,argparse
from pathlib import Path
import numpy as np
from strict110_contact_coarsening import load
from radial_power_projective_goal import screen
from goal_nomination import preserve

def run(source,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);a,X,Y=load(source);assert a['counts']==[2,1,1]and len(X)<=83;root=a['unstable_vertices'][0];r=X[root];records=[];best=[];start=time.time();serial=0
    for f in a['stable_face_ids']:
        n=Y[f]/np.linalg.norm(Y[f]);h=1/np.linalg.norm(Y[f]);e=r-n*(r@n);e/=np.linalg.norm(e);e2=np.cross(n,e)
        for alpha in np.r_[0.,np.geomspace(.001,3.,24)]:
            for phi in np.linspace(0,2*np.pi,12,endpoint=False):
                u=n+alpha*(np.cos(phi)*e+np.sin(phi)*e2);u/=np.linalg.norm(u);dot=u@r
                if dot<=0:continue
                rad=1/max(Y@u)
                for depth in [.001,.003,.01,.03,.1,.3,1.,3.]:
                    radius=rad*(1+depth);growth=max(1.,radius/dot*(1+1e-5))
                    for extra in [1.,1.02,1.1]:
                        serial+=1;Z=X.copy();Z[root]=r*growth*extra;Z=np.vstack((Z,radius*u));row=dict(serial=serial,facet=f,alpha=float(alpha),phi=float(phi),depth=depth,growth=float(growth*extra),cap=(radius*u).tolist())
                        try:g,p,hist,cl=screen(Z)
                        except(ValueError,np.linalg.LinAlgError)as err:row['rejected']=str(err);records.append(row);continue
                        row.update(projective_p=p.tolist(),**cl);records.append(row)
                        if cl['S']==cl['U']==1:preserve(g['X'],out/f'exact_goal_{serial:06d}','lattice P2 coupled root extension and Thales cap, physical projective mass closure, <=19 points')
                        score=cl['Pmax']+cl['Qmax'];best.append((score,serial,g['X'],Z,row));best.sort(key=lambda z:z[0]);best=best[:16]
                        if serial%300==0:(out/'screen.json').write_text(json.dumps(records,indent=2));print('PYRAMID_CAP_PROJECTIVE',serial,row,'best',best[0][4],'seconds',time.time()-start,flush=True)
    (out/'screen.json').write_text(json.dumps(records,indent=2))
    for k,(score,_,X,Z,row)in enumerate(best):
        np.save(out/f'best{k:02d}_physical.npy',X);np.save(out/f'best{k:02d}_reference.npy',Z);(out/f'best{k:02d}.json').write_text(json.dumps(row,indent=2))
    print('PYRAMID_CAP_PROJECTIVE_FINITE_STOP',serial,'seconds',time.time()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');a=p.parse_args();run(a.source,a.out)
