"""Thick Conway pyramids and common-root rotational convex unions.

Longer positive-angle Conway spirals move the base centroid toward the
spiral origin. This leaves an appreciable interval of apex heights inside
the apex-excluding Thales circle while keeping the pyramid centroid below
that origin. Rotated copies fix the reference root and retain every positive
reference vertex witness. The new union's OWN uniform centroid is integrated.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from support_geometry import escape
from vertex_geometry import geometry
from rotated_pyramid_goal import evaluate
from goal_nomination import preserve

def pyramid(n,extra_angle,apex_fraction,height_fraction):
    alpha=np.pi/n;eps=np.deg2rad(extra_angle);i=np.arange(1,n+1);r=(np.cos(alpha+eps)/np.cos(eps))**(n-i);theta=-np.pi/2+i*alpha;x=r*np.cos(theta);y=r*np.sin(theta);x[-1]=0.;base=np.column_stack((np.r_[x,-x[-2::-1]],np.r_[y,y[-2::-1]]));nextp=np.roll(base,-1,axis=0);cross=base[:,0]*nextp[:,1]-base[:,1]*nextp[:,0];area=cross.sum()/2;by=float(np.sum(cross*(base[:,1]+nextp[:,1]))/(6*area));bottom=float(min(base[:,1]));upper=min(by,-3*by)
    if upper<=bottom:raise ValueError('no allowed pyramid apex interval')
    ay=bottom+apex_fraction*(upper-bottom);az=height_fraction*np.sqrt((by-ay)*(ay-bottom));g=np.array([0.,(3*by+ay)/4,az/4]);X=np.vstack((np.column_stack((base,np.zeros(len(base)))),[0.,ay,az]))-g;root=n-1;u=X[root]/np.linalg.norm(X[root]);e=np.array([1.,0.,0.]);R=np.array([e,np.cross(u,e),u]);X=X@R.T/np.linalg.norm(X[root]);X[root]=[0.,0.,1.]
    values,_=escape(X);assert sum(values<0)==1 and np.argmin(values)==root,'numerical source pyramid lost its strict referenceU1 witness';gg=geometry(X,False);assert np.linalg.norm(gg['g'])<1e-10
    return np.delete(X,root,axis=0),dict(base_centroid_y=by,bottom_y=bottom,apex_y=ay,apex_z=az,pyramid_centroid=g.tolist(),source_reference_min_escape=float(min(np.delete(values,root))))

def rotations(k):
    if k==2:return [np.eye(3),np.diag([-1.,-1.,1.])]
    if k==4:return [np.linalg.matrix_power(np.array([[0.,-1.,0.],[1.,0.,0.],[0.,0.,1.]]),j)for j in range(4)]
    return [np.array([[np.cos(2*np.pi*j/k),-np.sin(2*np.pi*j/k),0.],[np.sin(2*np.pi*j/k),np.cos(2*np.pi*j/k),0.],[0.,0.,1.]])for j in range(k)]

def run(out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);rows=[];best=[];bestU=[];bestS=[];serial=0;start=time.time();(out/'method.json').write_text(json.dumps(dict(maximum_points=83,maximum_edges=243,source_geometry='Conway spiral angles90+epsilon degrees; apex in the source-base-centroid/bottom-midpoint Thales circle',physical_definition='uniform convex hull of common-root rotated point copies; all actual own-centroid counts recomputed, optionally after a new physical projective transform'),indent=2))
    for n in range(9,22):
        for k in [2,3,4]:
            if k*(2*n-1)+1>84:continue
            for extra in [.02,.2,.5,1.,2.]:
                for af in [.1,.3,.5,.7,.9]:
                    for hf in [.1,.3,.6,.9,.99]:
                        try:X,meta=pyramid(n,extra,af,hf)
                        except(ValueError,AssertionError):continue
                        X=np.vstack((*[X@R.T for R in rotations(k)],[[0.,0.,1.]]))
                        for ratio in [.65,.8,1.,1.2,1.5]:
                            Y=X*np.array([ratio,ratio,1.])
                            for projective in [False,True]:
                                serial+=1;row=dict(serial=serial,n=n,copies=k,extra_angle_degrees=extra,apex_fraction=af,height_fraction=hf,transverse_ratio=ratio,projective=projective,**meta)
                                try:g,p,cl=evaluate(Y,projective)
                                except(ValueError,np.linalg.LinAlgError)as err:row['error']=str(err);rows.append(row);continue
                                if cl['V']<11:row['excluded']='activeV<11: not pursuing any below34-complexity possibility';rows.append(row);continue
                                row.update(projective_p=p.tolist(),**cl);rows.append(row)
                                # A symmetric maximal face can have its foot
                                # on an integration diagonal. Small Q is only
                                # a nomination for the full exact census, not
                                # permission to erase any positive bar.
                                if cl['U']==1 and(cl['S']==1 or cl['Qmax']<1e-10):preserve(g['X'],out/f'exact_goal_{serial:07d}','thick Conway-pyramid common-root rotor, actual uniform-centroid equilibrium nomination, <=83points; strict full rational audit decides all coplanar facets and weak contacts')
                                item=(cl['Pmax']+cl['Qmax'],serial,g['Z'].copy(),row);best.append(item);best.sort(key=lambda z:z[0]);best=best[:12]
                                if cl['U']==1:bestU.append(item);bestU.sort(key=lambda z:z[0]);bestU=bestU[:12]
                                if cl['S']==1:bestS.append(item);bestS.sort(key=lambda z:z[0]);bestS=bestS[:12]
                                if serial%500==0:
                                    (out/'screen.json').write_text(json.dumps(rows,indent=2));print('THICK_CONWAY_ROTOR',serial,'best',best[0][3],'bestU',bestU[0][3]if bestU else None,'bestS',bestS[0][3]if bestS else None,'seconds',time.time()-start,flush=True)
        for label,data in [('best',best),('bestU',bestU),('bestS',bestS)]:
            for i,(_,_,X,row)in enumerate(data):np.save(out/f'{label}{i:02d}.npy',X);(out/f'{label}{i:02d}.json').write_text(json.dumps(row,indent=2))
        (out/'screen.json').write_text(json.dumps(rows,indent=2))
    print('THICK_CONWAY_ROTOR_FINITE_STOP',serial,'seconds',time.time()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('out');a=p.parse_args();run(a.out)
