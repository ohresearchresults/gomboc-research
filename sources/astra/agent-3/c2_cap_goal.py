"""Paired Thales caps with actual axial volume-centroid closure.

Adds a C2 pair above an unwanted stable facet. The uniform centroid is closed
by the existing apex height, then the whole actual body is audited numerically.
Only hulls with <=85 genuine numerical vertices enter the beam; every numerical
110 is immediately preserved and subjected to a complete exact hull census.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from vertex_geometry import geometry
from direct_face_polish import face_scores
from support_geometry import escape
from bounded_cap_beam_goal import points
from goal_nomination import preserve

def census(X):
    g=geometry(X,False);vf,_,_=face_scores(g,False);mask=~np.all(g['T']<4,axis=1)
    stable=np.flatnonzero((vf<0)&mask);vu,_=escape(g['Z'][g['vertices']],angular=True)
    return g,stable,int(sum(vu<0)),float(np.maximum(-vf[mask],0).sum())

def close(X,tipindex):
    Y=X.copy()
    def z(t):
        Y[tipindex,2]=t
        return float(geometry(Y,False)['g'][2])
    lower=max(1.,max(np.delete(Y[:,2],tipindex))+1e-8)
    if z(lower)>0:return None
    upper=max(lower*1.5,float(X[tipindex,2]))
    while z(upper)<0 and upper<10:upper*=1.5
    t=brentq(z,lower,upper,xtol=5e-15,rtol=9e-16);Y[tipindex,2]=t
    return Y

def run(source,out,width,depth):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);root=len(X)-1
    rng=np.random.default_rng(832094);beam=[(X,root)];history=[];serial=0;start=time.time()
    with (out/'trials.jsonl').open('w')as log:
        for level in range(depth):
            pool=[]
            for k,(X,root)in enumerate(beam):
                g,stable,U,score=census(X);assert U==1
                stable=[f for f in stable if g['H'][f,0]>0]
                for p,info in points(g,stable,rng):
                    serial+=1;Y=np.vstack((X,p+g['g'],(p+g['g'])*[-1,-1,1]))
                    row=dict(serial=serial,level=level,parent=k,point=Y[-2].tolist(),**info)
                    try:
                        Y=close(Y,root)
                        if Y is None:continue
                        gg,ss,uu,value=census(Y);row.update(V=len(gg['vertices']),S=1+len(ss),U=uu,score=value,tip=float(Y[root,2]))
                        if len(gg['vertices'])>85:continue
                        if not np.all(np.isin(np.arange(4),gg['vertices'])):continue
                        if uu==1 and len(ss)==0:
                            preserve(Y,out/f'exact_goal_{serial:06d}','C2 paired positive-shadow caps with actual axial uniform centroid closure and numerical110')
                        if uu==1 and 1+len(ss)<=5:
                            pool.append((Y,root,row))
                    except(ValueError,np.linalg.LinAlgError)as err:row['error']=repr(err)
                    log.write(json.dumps(row)+'\n')
                log.flush()
            if not pool:print('C2_CAP_NO_ADMISSION',level,serial,flush=True);break
            pool.sort(key=lambda x:(x[2]['score'],x[2]['S']));beam=[];seen=set()
            for Y,root,row in pool:
                key=(row['parent'],tuple(np.round(Y[-2],4)))
                if key in seen:continue
                seen.add(key);beam.append((Y,root));d=out/f'level{level:02d}_beam{len(beam)-1:02d}';d.mkdir();np.save(d/'physical_points.npy',Y);(d/'construction.json').write_text(json.dumps(row,indent=2))
                if len(beam)>=width:break
            row=dict(level=level,trials=serial,admitted=len(pool),best=pool[0][2],seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('C2_CAP_GOAL',row,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--width',type=int,default=5);p.add_argument('--depth',type=int,default=5);a=p.parse_args();run(a.source,a.out,a.width,a.depth)
