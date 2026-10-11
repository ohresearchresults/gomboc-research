"""Convex unions of rotated mono-unstable pyramids sharing one radial root.

Each rotation fixes the reference origin and the common unstable vertex.
Every old nonroot point keeps a positive shadow witness in its own copy, so
the union has referenceU1. Its uniformly filled convex hull has a NEW mass
centroid; no inherited own-centroid claim is made. Two to four copies have
at most35,52,69 input points respectively, unconditionally below C500.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from vertex_geometry import geometry
from unrestricted_shadow_goal import census
from shadow_mass_retracted_goal import bars as qbars
from dual_shadow_goal import bars as pbars
from canonical_projective_mass import normalize
from goal_nomination import preserve

def evaluate(X,projective):
    if projective:g,p,h=normalize(X)
    else:g=geometry(X,False);p=np.zeros(3)
    cl=census(g);edges=set()
    for tri in g['T']:
        for i,j in zip(tri,np.roll(tri,-1)):edges.add(tuple(sorted((int(i),int(j)))))
    g['edges']=np.array(list(edges));P=pbars(g,False)[0];Q=qbars(g,False)[0];cl.update(Pmax=float(max(P,default=0.)),Qmax=float(max(Q,default=0.)));return g,p,cl

def run(source,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);root=np.argmax(np.linalg.norm(X,axis=1));u=X[root]/np.linalg.norm(X[root]);e=np.eye(3)[np.argmin(abs(u))];e-=u*(e@u);e/=np.linalg.norm(e);R=np.array([e,np.cross(u,e),u]);X=X@R.T/np.linalg.norm(X[root]);X[root]=[0.,0.,1.];nr=np.delete(X,root,axis=0);records=[];best=[];bestU=[];start=time.time();serial=0
    (out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),rotation=R.tolist(),root_source_id=int(root),construction='convex hull of2..4 rotated copies sharing the literal root(0,0,1), followed by a radial power and axial affine scaling; ordinary or physical projective centering',maximum_points=69,maximum_edges=201),indent=2));powers=[.25,.5,.75,1.,1.1,1.3,1.6,2.,3.,5.,8.]
    for copies in [2,3,4]:
        for twist in [0.,.1,.3,.7]:
            angles=[2*np.pi*j/copies+twist*np.sin(1.73*j)for j in range(copies)];parts=[]
            for angle in angles:
                c,s=np.cos(angle),np.sin(angle);rot=np.array([[c,-s,0],[s,c,0],[0,0,1]]);parts.append(nr@rot.T)
            Y=np.vstack((*parts,[[0.,0.,1.]]));r=np.linalg.norm(Y,axis=1)
            for power in powers:
                Z=Y*r[:,None]**(power-1)
                for ratio in np.geomspace(.025,40.,55):
                    P=Z*np.array([ratio,ratio,1.])
                    for projective in [False,True]:
                        serial+=1;row=dict(serial=serial,copies=copies,twist=twist,angles=angles,power=power,transverse_scale=float(ratio),projective_centroid=projective)
                        try:g,p,cl=evaluate(P,projective)
                        except(ValueError,np.linalg.LinAlgError)as err:row['rejected']=str(err);records.append(row);continue
                        row.update(projective_p=p.tolist(),**cl);records.append(row)
                        if cl['S']==cl['U']==1:preserve(g['X'],out/f'exact_goal_{serial:06d}','rotated pyramid union, actual uniformly filled own-centroid numerical110, <=69points')
                        item=(cl['Pmax']+cl['Qmax'],serial,g['Z'].copy(),row);best.append(item);best.sort(key=lambda z:z[0]);best=best[:10]
                        if cl['U']==1:bestU.append(item);bestU.sort(key=lambda z:z[0]);bestU=bestU[:10]
                        if serial%500==0:(out/'screen.json').write_text(json.dumps(records,indent=2));print('ROTATED_PYRAMID_GOAL',serial,'best',best[0][3],'bestU',bestU[0][3]if bestU else None,'seconds',time.time()-start,flush=True)
    (out/'screen.json').write_text(json.dumps(records,indent=2))
    for name,items in [('best',best),('bestU',bestU)]:
        for k,(_,_,X,row)in enumerate(items):np.save(out/f'{name}{k:02d}.npy',X);(out/f'{name}{k:02d}.json').write_text(json.dumps(row,indent=2))
    print('ROTATED_PYRAMID_FINITE_STOP',serial,'seconds',time.time()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');a=p.parse_args();run(a.source,a.out)
