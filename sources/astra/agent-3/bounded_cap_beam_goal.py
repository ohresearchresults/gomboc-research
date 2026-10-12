"""Goal-only point-cap beam search in the <=84-vertex physical family.

Each added point is sampled above a current stable facet and inside an old
vertex's open Thales ball. This excludes that new point as an unstable root
at the OLD reference point only. The entire filled hull and its OWN centroid
are recomputed for every trial; only those actual results guide acceptance.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np

from direct_face_polish import face_scores
from goal_nomination import preserve
from persistence_birth import evaluate as persistence
from support_geometry import escape
from vertex_geometry import geometry


def census(X):
    g=geometry(X,False);vf,_,_=face_scores(g,False);vu,_=escape(g['Z'][g['vertices']],angular=True)
    return g,np.flatnonzero(vf<0),int(sum(vu<0))


def points(g,stable,rng):
    X=g['Z'][g['vertices']]
    for f in stable:
        H=g['H'][f];n=H/np.linalg.norm(H);h=1/np.linalg.norm(H)
        tangent=np.eye(3)[np.argmin(abs(n))];tangent-=n*(n@tangent);tangent/=np.linalg.norm(tangent);t2=np.cross(n,tangent)
        foot=h*n
        for w,v in enumerate(X):
            cb=v/2;radius=np.linalg.norm(v)/2;top=cb@n+radius
            if top<=h+1e-10:continue
            for fraction in [.0001,.001,.01,.07,.25,.6]:
                z=h+fraction*(top-h);centre=cb+(z-cb@n)*n;rr=np.sqrt(max(0.,radius**2-(z-cb@n)**2))
                desired=foot+(z-h)*n-centre
                desired-=n*(n@desired);length=np.linalg.norm(desired)
                nearest=centre+desired*min(1.,rr*.98/max(length,1e-300))
                if nearest@(v-nearest)>0:
                    yield nearest,dict(facet=int(f),witness=w,fraction=fraction,mode='nearest facet foot')
                theta=rng.uniform(0,2*np.pi);rho=rr*np.sqrt(rng.uniform(.05,.95));p=centre+rho*(np.cos(theta)*tangent+np.sin(theta)*t2)
                if p@(v-p)>0:
                    yield p,dict(facet=int(f),witness=w,fraction=fraction,mode='ball slice')


def run(source,out,width,depth):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);assert len(X)<=84;g,s,u=census(X);X=g['Z'][g['vertices']];X/=max(np.linalg.norm(X,axis=1));np.save(out/'initial.npy',X)
    (out/'method.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest(),max_vertices=84,max_edges=246,width=width,depth=depth,acceptance='actual complete numerical own-centroid census; any own110 immediately frozen as exact dyadic physical points'),indent=2))
    rng=np.random.default_rng(93500);beam=[(X,dict(parent='initial',Qmax=None))];history=[];serial=0;start=time.time()
    with (out/'trials.jsonl').open('w')as log:
        for level in range(depth):
            pool=[]
            for parent,(X,meta)in enumerate(beam):
                g,stable,U=census(X)
                assert U==1,'beam source must retain actual numerical unique U'
                X=g['Z'][g['vertices']]
                if len(X)>=84:continue
                parentpath=out/f'level{level:02d}_parent{parent:02d}.npy';np.save(parentpath,X)
                for p,info in points(g,stable,rng):
                    serial+=1;Y=np.vstack((X,p));row=dict(serial=serial,level=level,parent=parent,parent_points=str(parentpath.resolve()),point=p.tolist(),**info)
                    try:
                        gg,ss,uu=census(Y);row.update(S=len(ss),U=uu,V=len(gg['vertices']))
                        if len(ss)==uu==1:
                            preserve(Y,out/f'exact_goal_nomination{serial}','bounded <=84-vertex cap beam reached numerical own110 at freshly integrated centroid')
                        if uu==1 and 1<=len(ss)<=4 and len(gg['vertices'])>len(X):
                            value,_,bars=persistence(Y,.01);row.update(Qmax=bars['Qmax'],Qsum=float(sum(bars['Q'])),Pmax=bars['Pmax']);pool.append((Y,row))
                    except(ValueError,np.linalg.LinAlgError)as err:row['rejected']=repr(err)
                    log.write(json.dumps(row)+'\n')
                log.flush()
            if not pool:
                print('CAP_BEAM_FINITE_STOP_NO_ADMITTED_POINT',level,serial,flush=True);break
            pool.sort(key=lambda z:(z[1]['Qmax'],z[1]['Qsum'],z[1]['S']))
            beam=[];keys=set()
            for Y,row in pool:
                # This only allocates finite search effort among candidate
                # points. It does not round or identify physical vertices.
                key=(row['parent'],row['facet'],tuple(np.round(Y[-1],4)))
                if key in keys:continue
                keys.add(key);beam.append((Y,row))
                np.save(out/f'level{level:02d}_beam{len(beam)-1:02d}.npy',Y)
                if len(beam)>=width:break
            rec=dict(level=level,trials=serial,admitted=len(pool),beam=[r for _,r in beam],seconds=time.time()-start);history.append(rec);(out/'history.json').write_text(json.dumps(history,indent=2))
            print('BOUNDED_CAP_GOAL_BEAM',dict(level=level,trials=serial,admitted=len(pool),bestQ=beam[0][1]['Qmax'],best_counts=[beam[0][1]['S'],beam[0][1]['U']],vertices=len(beam[0][0]),seconds=time.time()-start),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--width',type=int,default=6);p.add_argument('--depth',type=int,default=6);a=p.parse_args();run(a.source,a.out,a.width,a.depth)
