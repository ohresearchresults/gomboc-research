"""Add genuine physical halfspaces through positive-shadow normal caps.

The normal hull is used only for proposing inequalities. Every score and mass
constraint concerns the uniformly filled primal intersection Q_i.x<=1. Every
potential actual own110 is exact-audited; normal-hull mass is never substituted.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from vertex_geometry import geometry as normal_hull
from direct_face_polish import face_scores
from bounded_cap_beam_goal import points
from dual_shadow_goal import Generator,model,restore,bars,freeze,run as refine
from support_geometry import geometry,census

def run(source,out,rounds,width):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);Q=np.load(source);Q=Q[ConvexHull(Q).vertices];rng=np.random.default_rng(782013);history=[];serial=0;start=time.time()
    for level in range(rounds):
        if len(Q)>=84:break
        ld=out/f'level{level:02d}';ld.mkdir();np.save(ld/'source_supports.npy',Q);physical=geometry(Q,False);old=float(max(bars(dict(physical,edges=np.unique(np.array([sorted((i,j))for cy in physical['faces']for i,j in zip(cy,cy[1:]+cy[:1])]),axis=0)),False)[0],default=0.))
        nh=normal_hull(Q,False);ref=dict(nh,Z=Q,g=np.zeros(3),H=np.linalg.solve(Q[nh['T']],np.ones((len(nh['T']),3,1)))[:,:,0]);scores,_,_=face_scores(ref,False);stable=list(map(int,np.flatnonzero(scores<0)));rootface=int(np.argmax(np.linalg.norm(ref['H'],axis=1)));targets=[i for i in sorted(stable,key=lambda i:-np.linalg.norm(ref['H'][i]))if i!=rootface][:4];pool=[]
        with(ld/'trials.jsonl').open('w')as log:
            for w,info in points(ref,targets,rng):
                serial+=1;QQ=np.vstack((Q,w));row=dict(serial=serial,normal=w.tolist(),**info)
                try:
                    g=geometry(QQ,False);ed=np.unique(np.array([sorted((i,j))for cy in g['faces']for i,j in zip(cy,cy[1:]+cy[:1])]),axis=0);g['edges']=ed;vv,_=bars(g,False);cc=census(g);row.update(Pmax=float(max(vv,default=0.)),centroid_norm=float(np.linalg.norm(g['g'])),census=cc)
                    if cc['S']==cc['U']==1:freeze(g,ld/f'exact_raw_goal_{serial:06d}')
                    pool.append((row['Pmax']+row['centroid_norm'],QQ,row))
                except(ValueError,np.linalg.LinAlgError)as err:row['rejected']=repr(err)
                log.write(json.dumps(row)+'\n')
        pool.sort(key=lambda r:r[0]);closed=[];seen=set()
        for _,QQ,row in pool:
            key=(row['facet'],row['witness'],row['fraction'])
            if key in seen:continue
            seen.add(key)
            if len(seen)>30:break
            try:
                F=Generator(QQ);q,g,corr=restore(F,F.q,limit=120)
                if q is None:continue
                cc=census(g)
                if cc['S']!=1:continue
                vv,_=bars(g,False);value=float(max(vv,default=0.));row.update(closed_P=value,closed_census=cc,mass_correction=corr);closed.append((value,g['Q'],row))
                if cc['U']==1:freeze(g,ld/f'exact_closed_goal_{row["serial"]:06d}')
            except(ValueError,np.linalg.LinAlgError):continue
        closed.sort(key=lambda r:r[0]);results=[]
        for k,(value,QQ,row)in enumerate(closed[:width]):
            d=ld/f'candidate{k:02d}';d.mkdir();np.save(d/'supports.npy',QQ);(d/'construction.json').write_text(json.dumps(row,indent=2));refine(d/'supports.npy',d/'goal_refinement',1400,732175+row['serial']);rr=json.loads((d/'goal_refinement/latest.json').read_text());results.append((rr['Pmax'],d/'goal_refinement/endpoint_supports.npy',rr))
        if not results:print('DUAL_CAP_NO_ADMITTED_CONTINUATION',level,len(pool),flush=True);break
        value,path,cc=min(results,key=lambda r:r[0]);row=dict(level=level,trials=len(pool),mass_closed=len(closed),old_P=old,best_P=value,selected=str(path),census=cc,seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('DUAL_SHADOW_CAP_GOAL',row,flush=True)
        if value>=old-1e-8:break
        QQ=np.load(path);Q=QQ[ConvexHull(QQ).vertices];np.save(out/'latest_supports.npy',Q)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--rounds',type=int,default=6);p.add_argument('--width',type=int,default=4);a=p.parse_args();run(a.source,a.out,a.rounds,a.width)
